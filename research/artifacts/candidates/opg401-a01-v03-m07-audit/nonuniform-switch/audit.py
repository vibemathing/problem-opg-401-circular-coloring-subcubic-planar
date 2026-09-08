"""Exact candidate-generator controls. No old table or old checker is imported."""
import json
from collections import deque
from functools import lru_cache
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parent
N = 20
OK = tuple(tuple(7 <= abs(a-b) <= 13 for b in range(N)) for a in range(N))
MASK = tuple(sum(1 << b for b in range(N) if OK[a][b]) for a in range(N))
OE = ((0,1),(1,2),(2,3),(3,4),(4,0),(3,5),(5,6),(6,7),(7,2))
OP = (0,5,6,7)  # a,d,e,f; internal order a,u,b,c,v,d,e,f
W = (0,7,14,1,8,15,6,13,0,10,0,10,0,10,0,10,0,10,0,10)
FMAP = tuple(W[3*c % 20] for c in range(20))


def legal(edges, colors):
    return all(isinstance(c, int) and 0 <= c < N for c in colors) and all(
        7 <= (colors[b]-colors[a]) % N <= 13 for a,b in edges)


@lru_cache(maxsize=1024)
def original(boundary, omitted=None):
    """Literal-edge DFS, no interval/obstruction tables; returns all vertex values."""
    edges = tuple(e for e in OE if e != omitted)
    neighbors = [set() for _ in range(8)]
    for a,b in edges:
        neighbors[a].add(b); neighbors[b].add(a)
    domains = [(1 << N)-1]*8
    for v,c in zip(OP,boundary):
        domains[v] &= MASK[c]
    nodes = 0
    def search(dd, chosen):
        nonlocal nodes
        nodes += 1
        if nodes > 100000:
            raise RuntimeError('original DFS node bound')
        todo = [v for v in range(8) if chosen[v] < 0]
        if not todo:
            return tuple(chosen)
        v = min(todo, key=lambda x: (dd[x].bit_count(), x))
        m = dd[v]
        while m:
            bit = m & -m; m -= bit
            c = bit.bit_length()-1
            nd = dd[:]; cc = chosen[:]; cc[v] = c
            for z in neighbors[v]:
                if cc[z] < 0: nd[z] &= MASK[c]
            if all(nd[z] for z in todo if z != v):
                result = search(nd, cc)
                if result is not None: return result
        return None
    return search(domains, [-1]*8)


def validate_original(boundary, colors):
    return colors is not None and legal(OE, colors) and all(
        7 <= (c-colors[v]) % N <= 13 for v,c in zip(OP,boundary))


def switch(edges, f, transform, seeds, pins=()):
    """Least implication closure for choices f(v) or transform[f(v)]."""
    assert legal(edges, f) and len(transform) == N
    assert all(0 <= x < N for x in transform)
    n = len(f); arcs = [[] for _ in f]; bad = []
    for a,b in edges:
        if not OK[transform[f[a]]][f[b]]: arcs[a].append(b)
        if not OK[f[a]][transform[f[b]]]: arcs[b].append(a)
        if not OK[transform[f[a]]][transform[f[b]]]: bad.append((a,b))
    parents = {v: None for v in sorted(set(seeds))}
    q = deque(parents)
    while q:
        a = q.popleft()
        for b in sorted(arcs[a]):
            if b not in parents: parents[b] = a; q.append(b)
    selected = set(parents)
    def path(v):
        out = [v]
        while parents[v] is not None:
            v = parents[v]; out.append(v)
        return out[::-1]
    result = {'selected': sorted(selected), 'closure_vertices': len(selected)}
    pin_hits = sorted(v for v in pins if v in selected and transform[f[v]] != f[v])
    collisions = [(a,b) for a,b in bad if a in selected and b in selected]
    if pin_hits:
        result.update(success=False, reason='fixed_separator', paths=[path(pin_hits[0])])
    elif collisions:
        a,b = min(collisions)
        result.update(success=False, reason='bad_selected_edge', edge=[a,b], paths=[path(a),path(b)])
    else:
        g = [transform[x] if v in selected else x for v,x in enumerate(f)]
        assert legal(edges,g) and all(g[v] == f[v] for v in pins)
        result.update(success=True, colors=g)
    return result


def components(edges, f, axis):
    adj = [[] for _ in f]
    for a,b in edges:
        bad1 = not OK[(axis-f[a]) % N][f[b]]
        bad2 = not OK[f[a]][(axis-f[b]) % N]
        assert bad1 == bad2
        if bad1: adj[a].append(b); adj[b].append(a)
    seen = set(); out = []
    for v in range(len(f)):
        if v in seen: continue
        cc = {v}; q = [v]; seen.add(v)
        for a in q:
            for b in sorted(adj[a]):
                if b not in seen: seen.add(b); cc.add(b); q.append(b)
        out.append(sorted(cc))
    return out


def faces(rotation, edges):
    rotation = {int(v): list(ws) for v,ws in rotation.items()}
    assert all(len(ws) == len(set(ws)) for ws in rotation.values())
    darts = {(a,b) for a,b in edges} | {(b,a) for a,b in edges}
    assert {(v,w) for v,ws in rotation.items() for w in ws} == darts
    todo = set(darts); fs = []
    while todo:
        start = min(todo); d = start; walk = []
        while True:
            assert d in todo
            todo.remove(d); a,b = d; walk.append(a)
            ws = rotation[b]; d = (b,ws[(ws.index(a)+1) % len(ws)])
            if d == start: break
        fs.append(walk)
    assert len(rotation)-len(edges)+len(fs) == 2
    return fs


def build_fixture(p, sign=1):
    P = 3 if p == 1 else 2
    ports = [P,0,26,20]
    edges = [(i,(i+1) % 40) for i in range(40)] + [(18,28)]
    f = [sign*7*i % 20 for i in range(40)]
    rH = {i:[(i-1)%40,(i+1)%40] for i in range(40)}
    rH[18] = [17,19,28]; rH[28] = [27,29,18]
    axis = (sign*(8 if p == 1 else 16)) % 20
    chosen = next(c for c in components(edges,f,axis) if 0 in c)
    separator = sorted({b for a,b in edges if a in chosen and b not in chosen} |
                       {a for a,b in edges if b in chosen and a not in chosen})
    result = switch(edges, f, [(axis-c)%20 for c in range(20)], [0], separator)
    assert result['success'] and result['selected'] == chosen
    g = result['colors']; boundary = tuple(g[v] for v in ports)
    inner = original(boundary)
    assert validate_original(boundary,inner)
    ge = edges+[(40+a,40+b) for a,b in OE]+[(40+a,t) for a,t in zip(OP,ports)]
    rr = {i:ws[:] for i,ws in rH.items()}
    for a,t in zip(OP,ports):
        rr[t] = [(t-1)%40,40+a,(t+1)%40]
    ro = {0:[4,1,'P'],1:[0,2],2:[1,3,7],3:[2,4,5],4:[3,0],
          5:[6,3,'Q'],6:[7,5,'R'],7:[2,6,'S']}
    names = dict(zip('PQRS',ports))
    for v,ws in ro.items(): rr[40+v] = [40+x if isinstance(x,int) else names[x] for x in ws]
    gf = faces(rr,ge)
    degree = [0]*48
    for a,b in ge: degree[a]+=1;degree[b]+=1
    assert max(degree) <= 3 and len(set(tuple(sorted(e)) for e in ge)) == len(ge)
    ad = [set() for _ in degree]
    for a,b in ge:ad[a].add(b);ad[b].add(a)
    assert all(not (ad[a] & ad[b]) for a,b in ge)
    full = g+list(inner); assert legal(ge,full)
    assert original(tuple(f[v] for v in ports)) is None
    transform = FMAP if sign == 1 else tuple(-FMAP[-c%20] %20 for c in range(20))
    rejected = switch(edges,f,transform,[26])
    assert not rejected['success'] and rejected['reason'] == 'bad_selected_edge'
    k = sign*8 %20
    fixed_vertices = [i for i,c in enumerate(f) if (k-c)%20 == c]
    old_separators = []
    for count in (1,2):
        for cut in combinations(fixed_vertices,count):
            adj=[[] for _ in f]
            for a,b in edges:
                if a not in cut and b not in cut:adj[a].append(b);adj[b].append(a)
            reach={26};q=[26]
            for a in q:
                for b in adj[a]:
                    if b not in reach:reach.add(b);q.append(b)
            if not (reach & {ports[0],ports[1],ports[3]}):old_separators.append(cut)
    assert not old_separators
    assert all(MASK[f[(v-1)%40]] & MASK[f[(v+1)%40]] == 1<<f[v] for v in range(40))
    return {'p':p,'conjugate':sign == -1,'ports':ports,'outside_edges':edges,'outside_rotation':rH,
            'outside_faces':faces(rH,edges),'initial_colors':f,'initial_boundary':[f[v] for v in ports],
            'all_tight_reachability_blocked':'directed Hamilton cycle in tight graph',
            'F_mask_failure':rejected,'old_axis_fixed_vertices':fixed_vertices,
            'old_separator_tests':len(fixed_vertices)+len(list(combinations(fixed_vertices,2))),
            'old_reflection_separators':[], 'repair_axis':axis,'selected':chosen,'fixed_separator':separator,
            'new_outside_colors':g,'new_boundary':boundary,'inner_colors':inner,
            'full_edges':ge,'full_rotation':rr,'full_faces':gf,'full_colors':full,
            'not_a_minimum_obstruction':'explicit full coloring; long degree-two threads'}


def main():
    config = json.loads((ROOT/'input.json').read_text())
    assert config['modulus'] == 20 and config['chord'] == [18,28]
    table=[]
    for p,axis in [(1,8),(14,16)]:
        boundary=(p,0,2,0)
        for mask in range(16):
            b=tuple((axis-c)%20 if mask>>i & 1 else c for i,c in enumerate(boundary))
            w=original(b)
            assert bool(w) == (0 < mask < 15)
            if w: assert validate_original(b,w)
            table.append({'p':p,'axis':axis,'mask':mask,'boundary':b,'witness':w})
    reflection_edges=0
    for axis in range(20):
        for a in range(20):
            for b in range(20):
                if not OK[a][b]:continue
                assert OK[(axis-a)%20][(axis-b)%20]
                assert OK[(axis-a)%20][b] == OK[a][(axis-b)%20]
                reflection_edges+=1
    # Exhaustively compare least-closure feasibility with all selector choices on every colored edge.
    closure_trials=0
    for a in range(20):
        for b in range(20):
            if not OK[a][b]:continue
            for seed in (0,1):
                got=switch([(0,1)],[a,b],FMAP,[seed])['success']
                expected=any(legal([(0,1)],[FMAP[x] if mask>>i&1 else x for i,x in enumerate([a,b])])
                             for mask in range(4) if mask>>seed&1)
                assert got == expected;closure_trials+=1
    # Three-vertex path: every valid f, two endpoint seeds, and all 8 selectors.
    for a in range(20):
        for b in range(20):
            if not OK[a][b]:continue
            for c in range(20):
                if not OK[b][c]:continue
                f=[a,b,c]; ee=[(0,1),(1,2)]; seeds=[0,2]
                got=switch(ee,f,FMAP,seeds)['success']
                expected=any(legal(ee,[FMAP[x] if mask>>i&1 else x for i,x in enumerate(f)])
                             for mask in range(8) if mask&5 == 5)
                assert got == expected;closure_trials+=1
    fixtures=[build_fixture(p,sgn) for p in (1,14) for sgn in (1,-1)]
    # Negative controls must witness actual errors; none are admitted results.
    mut=[]
    def detected(name,witness):mut.append({'name':name,'detected':True,'witness':witness})
    assert OK[0][7] and OK[0][13]
    detected('omit_endpoint_7',[0,7]);detected('omit_endpoint_13',[0,13])
    assert not OK[0][19] and ((19-0)%20 >= 7)
    detected('omit_directed_upper_bound',[0,19])
    assert not switch([(0,1)],[2,10],FMAP,[0])['success']
    detected('ignore_bad_selected_edge',{'old':[2,10],'new':[6,0]})
    fixture=fixtures[0]; ee=fixture['outside_edges'];f=fixture['initial_colors'];axis=fixture['repair_axis']
    g=f[:];g[0]=(axis-f[0])%20
    assert not legal(ee,g)
    detected('omit_implication_propagation',{'vertex':0,'old':f[0],'new':g[0]})
    assert not switch(ee,f,[(axis-c)%20 for c in range(20)],[0],[0])['success']
    detected('silently_change_pinned_color',{'pin':0,'color':0})
    g=f[:]
    for v in fixture['selected']:g[v]=(axis+f[v])%20
    assert not legal(ee,g)
    detected('replace_reflection_with_wrong_formula',{'axis':axis,'selected':fixture['selected']})
    assert original((1,0,2,0)) is None and original((1,0,2,0),(2,3)) is not None
    detected('omit_original_bc',{'boundary':[1,0,2,0]})
    assert original((1,0,2,0)) is None and original((3,0,2,0)) is not None
    detected('silently_recolor_fixed_original_P',{'from':1,'to':3})
    # Unequal vertex IDs Q,S have the same valid color. They are not identified.
    assert fixture['ports'][1] != fixture['ports'][3] and f[fixture['ports'][1]] == f[fixture['ports'][3]]
    Q,S=fixture['ports'][1],fixture['ports'][3]
    collapsed={tuple(sorted((Q if a == S else a,Q if b == S else b))) for a,b in fixture['full_edges']}
    assert all(a != b for a,b in collapsed)
    assert sum(Q in e for e in collapsed) == 6
    detected('identify_equal_colored_ports',{'vertices':[Q,S],'wrong_identified_degree':6})
    badrot={int(v):ws[:] for v,ws in fixture['outside_rotation'].items()}
    badrot[18]=[17,19]
    try:faces(badrot,ee)
    except AssertionError:detected('omit_chord_dart',{'vertex':18})
    else:raise AssertionError('rotation mutation survived')
    assert not OK[FMAP[0]][FMAP[10]] and OK[0][10]
    detected('assume_F_is_full_palette_homomorphism',{'old':[0,10],'new':[FMAP[0],FMAP[10]]})
    report={'verdict':'candidate_only','local_table':table,'reflection_edge_checks':reflection_edges,
            'switch_closure_selector_controls':closure_trials,'fixtures':fixtures,'mutations':mut,
            'closed_residual_classes':[],'open_residual_classes':['C1','C2','C3','C4'],
            'trusted_verifier_receipt':False,'arbitrary_exterior_enumeration':False}
    (ROOT/'certificate.json').write_text(json.dumps(report,sort_keys=True,separators=(',',':'))+'\n')
    print(json.dumps({'boundary_masks':len(table),'reflection_edge_checks':reflection_edges,
                      'closure_controls':closure_trials,'fixtures':len(fixtures),'mutations':len(mut),
                      'closed_residual_classes':[]}))

if __name__ == '__main__':main()
