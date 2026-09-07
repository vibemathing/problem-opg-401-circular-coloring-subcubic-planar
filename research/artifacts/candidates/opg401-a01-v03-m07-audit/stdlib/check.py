"""Exact finite graph audit, version 1.0. No prior candidate code imported."""
from __future__ import annotations
import csv, io, json, sys
from functools import lru_cache
from itertools import product
from pathlib import Path

P = 20
FULL = (1 << P) - 1

def edge(a: int, b: int) -> bool:
    return 0 <= a < P and 0 <= b < P and 7 <= abs(a-b) <= 13

MASKS = tuple(sum(1 << b for b in range(P) if edge(a,b)) for a in range(P))

def require(ok: bool, msg: str) -> None:
    if not ok:
        raise ValueError(msg)

def fixed_valid(g: dict, boundary: list[int]) -> bool:
    ids = g.get('boundary_ids', list(range(len(boundary))))
    return (len(ids) == len(boundary) and all(type(x) is int and 0 <= x < P for x in boundary)
            and all(ids[i] != ids[j] or boundary[i] == boundary[j]
                    for i in range(len(ids)) for j in range(i)))

class Counter:
    """Variable elimination with exact component factorization and memoization.
    Retired coordinates are -1; all incident constraints are already propagated.
    Each branch lowers the number of active vertices. Counts are arbitrary integers.
    """
    def __init__(self, g: dict):
        self.g, self.n, self.calls = g, len(g['vertices']), 0
        self.ad = [0] * self.n
        for u,v in g['edges']:
            require(0 <= u < self.n and 0 <= v < self.n and u != v, 'invalid edge')
            self.ad[u] |= 1 << v
            self.ad[v] |= 1 << u
        @lru_cache(maxsize=40000)
        def rec(d: tuple[int,...]) -> int:
            self.calls += 1
            require(self.calls <= 3000000, 'count node limit')
            live = [i for i,x in enumerate(d) if x != -1]
            if not live:
                return 1
            if any(d[i] == 0 for i in live):
                return 0
            active = sum(1 << i for i in live)
            seen, comps = 0, []
            for v in live:
                if seen >> v & 1:
                    continue
                todo, comp = 1 << v, 0
                while todo:
                    bit = todo & -todo
                    todo -= bit
                    if seen & bit:
                        continue
                    seen |= bit
                    comp |= bit
                    todo |= self.ad[bit.bit_length()-1] & active & ~seen
                comps.append(comp)
            if len(comps) > 1:
                total = 1
                for comp in comps:
                    total *= rec(tuple(d[i] if comp >> i & 1 else -1 for i in range(self.n)))
                    if total == 0:
                        break
                return total
            v = min(live, key=lambda i: (d[i].bit_count(), -(self.ad[i] & active).bit_count()))
            choices, total = d[v], 0
            while choices:
                bit = choices & -choices
                choices -= bit
                nd = list(d)
                nd[v] = -1
                todo = self.ad[v] & active
                while todo:
                    nb = todo & -todo
                    todo -= nb
                    nd[nb.bit_length()-1] &= MASKS[bit.bit_length()-1]
                total += rec(tuple(nd))
            return total
        self.rec = rec

    def count(self, boundary: list[int]) -> int:
        if not fixed_valid(self.g, boundary):
            return 0
        d = [FULL] * self.n
        for v,k in self.g['ports']:
            d[v] &= MASKS[boundary[k]]
        return self.rec(tuple(d))

def witness(g: dict, boundary: list[int]) -> list[int] | None:
    """Separate direct-assignment DFS: no count recursion, masks, tables or cache."""
    if not fixed_valid(g,boundary):
        return None
    n, values, calls = len(g['vertices']), [None] * len(g['vertices']), 0
    def visit() -> list[int] | None:
        nonlocal calls
        calls += 1
        require(calls <= 2000000, 'witness node limit')
        if all(x is not None for x in values):
            return list(values)
        best, opts = -1, list(range(21))
        for v in range(n):
            if values[v] is not None:
                continue
            candidates = [c for c in range(20)
                if all(edge(c,boundary[k]) for u,k in g['ports'] if u == v)
                and all(values[w] is None or edge(c,values[w])
                        for u,w in g['edges'] if u == v)
                and all(values[u] is None or edge(c,values[u])
                        for u,w in g['edges'] if w == v)]
            if not candidates:
                return None
            if len(candidates) < len(opts):
                best, opts = v, candidates
        for c in opts:
            values[best] = c
            found = visit()
            if found is not None:
                return found
        values[best] = None
        return None
    return visit()

def valid(g: dict, b: list[int], colors: list[int] | None) -> bool:
    return (colors is not None and len(colors) == len(g['vertices']) and fixed_valid(g,b)
            and all(type(c) is int and 0 <= c < 20 for c in colors)
            and all(edge(colors[u],colors[v]) for u,v in g['edges'])
            and all(edge(colors[u],b[k]) for u,k in g['ports']))

def face_audit(g: dict, rotation: list[list[int]]) -> dict:
    n = len(g['vertices'])
    es = {tuple(sorted(e)) for e in g['edges']}
    require(len(es) == len(g['edges']) and all(u != v for u,v in es), 'not simple')
    ad = [{v for u,v in es if u == i} | {u for u,v in es if v == i} for i in range(n)]
    require(all(set(rotation[i]) == ad[i] and len(rotation[i]) == len(ad[i]) for i in range(n)), 'rotation mismatch')
    require(all(len(a) <= 3 for a in ad), 'degree bound')
    require(not any(ad[u] & ad[v] for u,v in es), 'triangle')
    seen, todo = set(), [0]
    while todo:
        u = todo.pop()
        if u not in seen:
            seen.add(u)
            todo.extend(ad[u] - seen)
    require(len(seen) == n, 'disconnected fixture')
    darts = {(u,v) for u,v in es} | {(v,u) for u,v in es}
    faces = []
    while darts:
        start = min(darts)
        dart, f = start, []
        while True:
            require(dart in darts, 'invalid face orbit')
            darts.remove(dart)
            u,v = dart
            f.append(u)
            row = rotation[v]
            dart = (v,row[(row.index(u)+1) % len(row)])
            if dart == start:
                break
        faces.append(f)
    require(n-len(es)+len(faces) == 2, 'not sphere rotation')
    return {'vertices':n,'edges':len(es),'faces':faces,'euler':2,'max_degree':max(map(len,ad)),
            'triangle_free':True,'connected':True}

def main() -> None:
    data = json.loads(Path('input.json').read_text())
    graphs = data['graphs']
    counters = {k:Counter(v) for k,v in graphs.items()}
    names = ['original','replacement','augmented_U','augmented_V']
    stream = io.StringIO()
    writer = csv.writer(stream,lineterminator='\n')
    writer.writerow(['h','r']+names)
    counts, zero, sums = {}, {k:0 for k in names}, {k:0 for k in names}
    for h in range(11):
        for r in range(20):
            masks = [0]*4
            for p in range(20):
                boundary = [p,0,r,h]
                row = [counters[k].count(boundary) for k in names]
                counts[h,r,p] = row
                for i,k in enumerate(names):
                    zero[k] += row[i] == 0
                    sums[k] += row[i]
                    masks[i] |= (row[i] > 0) << p
            writer.writerow([h,r]+[format(m,'05x') for m in masks])
    Path('extension-table.csv').write_text(stream.getvalue())
    residual_rows, survivors, direct_checks = [], {}, 0
    for number,c in enumerate(data['classes'],1):
        h,r,bad_p = c['h'],c['r'],c['p']
        survivors[str(number)] = {k:[] for k in names[1:]}
        for p in range(20):
            boundary = [p,0,r,h]
            row = counts[h,r,p]
            require((row[0] == 0) == (p in bad_p), 'extra row mismatch')
            ws = []
            for i,k in enumerate(names):
                w = witness(graphs[k],boundary)
                require((w is not None) == (row[i]>0), 'count/DFS disagreement')
                if w is not None:
                    require(valid(graphs[k],boundary,w), 'invalid DFS witness')
                direct_checks += 1
                if p in bad_p and i > 0 and row[i] > 0:
                    survivors[str(number)][k].append(p)
                ws.append(w)
            residual_rows.append([number,h,r,p,row,ws])
    # The generator above did not consult any previous analytic table.
    expected_disagreements = 0
    for (h,r,p),row in counts.items():
        basic = r in ([19,0,1] if h == 0 else list(range(h+1)) if h <= 7 else [0,h])
        additional = any(h == c['h'] and r == c['r'] and p in c['p'] for c in data['classes'])
        expected_disagreements += (row[0] == 0) != (basic or additional)
    require(expected_disagreements == 0, 'm06 comparison failed')
    # P3 is computed from its nine-vertex graph, not B's formula.
    p3 = [[counters['three_port'].count([t,0,s]) for t in range(20)] for s in range(20)]
    def good(t:int,r:int,s:int) -> bool:
        return p3[(s-r)%20][(t-r)%20] > 0
    p3_bad = [[t for t in range(20) if p3[s][t] == 0] for s in range(11)]
    require(p3_bad == [list(range(20)),[7,8,9],[8,9]]+[[] for _ in range(8)], 'P3 table mismatch')
    absorption = []
    for d in range(20):
        absorption.append([sum(edge(x,0) and edge(y,d) and edge(x,y) and good(y,x,z)
                               for x in range(20) for y in range(20)) for z in range(20)])
    p1_bad = [[z for z in range(20) if absorption[d][z] == 0] for d in range(11)]
    require(p1_bad == [list(range(20)),[7,8],[8]]+[[] for _ in range(8)], 'P1 table mismatch')
    require(all(absorption[d][z] > 0 or not good(z,0,d) for d in range(20) for z in range(20)), 'P invariant failure')
    mutations = []
    def killed(name:str, condition:bool, detail:dict) -> None:
        require(condition,'surviving mutation '+name)
        mutations.append({'name':name,'detected':True,'witness':detail})
    killed('exclude_7', edge(0,7) and not 7 < abs(0-7) <= 13, {'edge':[0,7]})
    killed('exclude_13', edge(0,13) and not 7 <= abs(0-13) < 13, {'edge':[0,13]})
    killed('directed_residue_as_short_distance',edge(0,13) and not 7 <= (13-0)%20 <= 10, {'edge':[0,13]})
    b, w = [1,0,2,0], [7,14,1,8,15]
    require(valid(graphs['augmented_U'],b,w),'frozen JU witness failed')
    killed('reflection_omits_modulo',not valid(graphs['augmented_U'],[(-x)%20 for x in b],[-x for x in w]),{'boundary':b,'colors':w})
    killed('translation_omits_modulo',not valid(graphs['augmented_U'],[(x+19)%20 for x in b],[x+19 for x in w]),{'shift':19,'boundary':b,'colors':w})
    alias = dict(graphs['replacement'],boundary_ids=['same','q','same','s'])
    killed('ignore_outside_vertex_identification',valid(graphs['replacement'],b,w) and not valid(alias,b,w),{'identified_ports':[0,2],'colors':[1,2]})
    killed('equal_colors_are_identical_vertices',valid(graphs['replacement'],b,w) and len(set(b)) < 4, {'distinct_vertices_equal_colors':b})
    missing = dict(graphs['original'],edges=[e for e in graphs['original']['edges'] if e != [2,3]])
    mw = witness(missing,b)
    killed('omit_shared_edge_bc',valid(missing,b,mw) and not valid(graphs['original'],b,mw),{'boundary':b,'colors':mw})
    changed = [2,0,2,0]
    cw = witness(graphs['original'],changed)
    killed('secretly_recolor_fixed_boundary',valid(graphs['original'],changed,cw) and not valid(graphs['original'],b,cw),{'fixed':b,'altered':changed,'colors':cw})
    badports = dict(graphs['augmented_U'],ports=[[u,2 if k==1 else 1 if k==2 else k] for u,k in graphs['augmented_U']['ports']])
    killed('swap_q_r_without_graph_map',not valid(badports,b,w),{'boundary':b,'colors':w})
    killed('absorption_omits_TR',good(7,7,0) and edge(7,0) and not edge(7,7),{'V':0,'W':0,'S':0,'R':7,'T':7})
    # Verify the old failure example and a positive coloring, edge by edge.
    ob = data['old_witness']
    require(valid(graphs['replacement'],ob['boundary'],ob['replacement_colors']), 'old replacement witness')
    require(counters['original'].count(ob['boundary']) == 0,'old obstruction witness')
    require(valid(graphs['original'],ob['positive_boundary'],ob['positive_colors']),'positive original witness')
    invariance = {'edge_translation':0,'edge_reflection':0,'residual_isometry':0}
    for a,b0 in product(range(20),repeat=2):
        require(edge(a,b0)==edge((-a)%20,(-b0)%20),'reflection predicate')
        invariance['edge_reflection'] += 1
        for shift in range(20):
            require(edge(a,b0)==edge((a+shift)%20,(b0+shift)%20),'translation predicate')
            invariance['edge_translation'] += 1
    for c in data['classes']:
        for p in c['p']:
            b0=[p,0,c['r'],c['h']]
            for sign,shift in [(-1,0),(1,19),(-1,7)]:
                b1=[(sign*x+shift)%20 for x in b0]
                for i,k in enumerate(names):
                    require(counters[k].count(b1)==counts[c['h'],c['r'],p][i], 'graph isometry')
                    invariance['residual_isometry'] += 1
    fixture_reports = []
    for f in data.get('fixtures',[]):
        g=f['graph']; report=face_audit(g,f['rotation'])
        require(valid(g,[],f['full_coloring']), 'fixture full coloring')
        mapping = dict(zip(g['vertices'],f['full_coloring']))
        fixed = f['outside_fixed_colors']
        require(all(edge(fixed[g['vertices'][u]],fixed[g['vertices'][v]])
                    for u,v in g['edges'] if g['vertices'][u] in fixed and g['vertices'][v] in fixed), 'outside coloring')
        preserved = all(mapping[v] == c for v,c in fixed.items())
        require(preserved == f['boundary_preserved_by_full_coloring'], 'boundary preservation control')
        report['fixed_outside_coloring_valid'] = True
        report['boundary_preserved_by_full_coloring'] = preserved
        report['name']=f['name']
        report['full_coloring']=f['full_coloring']
        fixture_reports.append(report)
    Path('residuals.json').write_text(json.dumps({'columns':['class','h','r','p','counts_O_J_JU_JV','witnesses_O_J_JU_JV'],
        'rows':residual_rows,'survivors':survivors},separators=(',',':'))+'\n')
    Path('three-port.json').write_text(json.dumps({'p3_counts_by_s_then_t':p3,'p1_choice_counts_by_d_then_S':absorption,
        'p3_bad_normalized':p3_bad,'p1_bad_normalized':p1_bad},separators=(',',':'))+'\n')
    result={'verdict':'candidate_only','normalized_boundaries':4400,'counts_are_exact_integer':True,
        'zero_counts':zero,'sum_internal_completion_counts':sums,'m06_table_disagreements':expected_disagreements,
        'separate_DFS_checks':direct_checks,'survivors':survivors,'whole_rows_eliminated':[],
        'mutations':mutations,'invariance':invariance,'fixtures':fixture_reports,
        'search_nodes':{k:c.calls for k,c in counters.items()},'trusted_verifier_receipt':False}
    Path('audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'normalized_boundaries':4400,'m06_disagreements':0,'mutations_detected':len(mutations),
                      'whole_rows_eliminated':[],'status':'NONTERMINAL_CHECKPOINT'}))

if __name__ == '__main__':
    main()
