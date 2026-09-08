"""Exact finite controls for V04; not a trusted verifier or graph-class search."""
import hashlib
import itertools as it
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def ok(a, b):
    return 0 <= a < 20 and 0 <= b < 20 and 7 <= abs(a-b) <= 13

def tau(k, c):
    return (k-c) % 20

def valid(edges, f):
    return all(ok(f[u], f[v]) for u, v in edges)

def conflict(edges, f, k):
    return sorted(tuple(sorted((u,v))) for u,v in edges if not ok(tau(k,f[u]),f[v]))

def comps(n, edges):
    adj = [set() for _ in range(n)]
    for u,v in edges:
        adj[u].add(v); adj[v].add(u)
    remaining = set(range(n)); out = []
    while remaining:
        todo = [min(remaining)]; found = set(todo)
        for v in todo:
            for w in sorted(adj[v]-found):
                found.add(w); todo.append(w)
        out.append(sorted(found)); remaining -= found
    return out

def steiner(n, edges, ports):
    """Exhaustive edge subsets of ONE supplied graph, n<=10,m<=10."""
    assert n <= 10 and len(edges) <= 10
    for size in range(len(edges)+1):
        for es in it.combinations(edges,size):
            if any(set(ports) <= set(c) for c in comps(n, es)):
                return list(es)
    raise ValueError('ports disconnected')

def pivot(edges, f, ports, pins, k, ell, target):
    """Exact pivot-then-single-port criterion; actual full colors retained."""
    n = len(f); t = ports[target]; c = f[t]; dest = tau(k,c)
    if t in pins and dest != c:
        return None, {'reason':'final_target_pinned','vertex':t}
    neighbors = {v if u==t else u for u,v in edges if t in (u,v)}
    common = {a for a in range(20) if ok(c,a) and ok(dest,a)}
    required=set(); forbidden={v for v in set(pins)|set(ports.values()) if tau(ell,f[v])!=f[v]}
    for v in neighbors:
        old, new = f[v] in common, tau(ell,f[v]) in common
        if not old and not new:
            return None, {'reason':'no_neighbor_choice','vertex':v}
        if not old: required.add(v)
        if not new: forbidden.add(v)
    cc = comps(n, conflict(edges,f,ell))
    selected = set().union(*(set(c) for c in cc if set(c)&required))
    if selected & forbidden:
        return None, {'reason':'forced_component_hits_forbidden','vertices':sorted(selected & forbidden)}
    mid=[tau(ell,c) if v in selected else c for v,c in enumerate(f)]
    assert valid(edges,mid)
    assert all(mid[v]==f[v] for v in set(pins)|set(ports.values()))
    assert all(mid[v] in common for v in neighbors)
    assert all(t not in e for e in conflict(edges,mid,k))
    out=mid.copy(); out[t]=dest
    assert valid(edges,out) and all(out[v]==f[v] for v in pins)
    return out, {'selected':sorted(selected),'required':sorted(required),'forbidden':sorted(forbidden),
                 'common_neighbor_colors':sorted(common),'mid':mid,'final':out,'target':t,
                 'components_after_pivot':comps(n,conflict(edges,mid,k))}

INNER=['a','u','b','c','v','d','e','f']
OE=[(0,1),(1,2),(2,3),(3,4),(4,0),(3,5),(5,6),(6,7),(7,2)]
PI=[0,5,6,7]

def extension(boundary):
    """Literal-edge DFS, no old table imports."""
    neighbors=[set() for _ in range(8)]
    for u,v in OE: neighbors[u].add(v); neighbors[v].add(u)
    dd=[set(range(20)) for _ in range(8)]
    for v,c in zip(PI,boundary):dd[v]={a for a in range(20) if ok(a,c)}
    def dfs(colors, dom):
        todo=[v for v in range(8) if colors[v]<0]
        if not todo:return colors
        v=min(todo,key=lambda w:(len(dom[w]),-len(neighbors[w]),w))
        for a in sorted(dom[v]):
            cc=colors.copy(); cc[v]=a; nd=[x.copy() for x in dom]
            for w in neighbors[v]:
                if cc[w]<0: nd[w]={b for b in nd[w] if ok(a,b)}
            if all(nd[w] for w in todo if w!=v):
                answer=dfs(cc,nd)
                if answer is not None:return answer
        return None
    return dfs([-1]*8,dd)

def color_graph(n, edges, fixed):
    """Literal-edge witness search used only for supplied absorption controls."""
    adj=[set() for _ in range(n)]
    for u,v in edges: adj[u].add(v);adj[v].add(u)
    def go(colors,dom):
        free=[i for i in range(n) if colors[i]<0]
        if not free:return colors
        v=min(free,key=lambda w:(len(dom[w]),-len(adj[w]),w))
        for a in sorted(dom[v]):
            cc=colors.copy();cc[v]=a;dd=[x.copy() for x in dom]
            for w in adj[v]:
                if cc[w]<0:dd[w]={b for b in dd[w] if ok(a,b)}
            if all(dd[w] for w in free if w!=v):
                ans=go(cc,dd)
                if ans is not None:return ans
        return None
    colors=[fixed.get(i,-1) for i in range(n)]
    if any(u in fixed and v in fixed and not ok(fixed[u],fixed[v]) for u,v in edges):return None
    dom=[{a for a in range(20) if all(w not in fixed or ok(a,fixed[w]) for w in adj[i])} for i in range(n)]
    return go(colors,dom)

def faces(rotation):
    darts={(i,j) for i,ls in enumerate(rotation) for j in ls}
    assert all((b,a) in darts for a,b in darts)
    out=[]
    while darts:
        start=min(darts); a,b=start; walk=[]
        while True:
            assert (a,b) in darts
            darts.remove((a,b));walk.append(a)
            ls=rotation[b];a,b=b,ls[(ls.index(a)+1)%len(ls)]
            if (a,b)==start:break
        out.append(walk)
    return out

def graph_fixture(f, ports, k, ell, target):
    n=len(f);edges=[(i,(i+1)%n) for i in range(n)]
    assert valid(edges,f) and len(conflict(edges,f,k))==n
    rotation=[[(i-1)%n,(i+1)%n] for i in range(n)]
    tree=steiner(n,edges,ports.values()); W=sorted({v for e in tree for v in e})
    crossing=[]
    for mask in range(1,1<<n):
        S={v for v in range(n) if mask>>v&1}
        if set(ports.values())&S and set(ports.values())-S:
            e=next(e for e in tree if bool(e[0] in S)!=bool(e[1] in S))
            crossing.append([mask,list(e)])
    allowed=[];orbit_invariance=0
    for mask in range(1<<n):
        g=[tau(k,c) if mask>>v&1 else c for v,c in enumerate(f)]
        if valid(edges,g):
            allowed.append(mask);assert conflict(edges,g,k)==conflict(edges,f,k);orbit_invariance+=1
    assert allowed==[0,(1<<n)-1]
    t=ports[target]; selected={v if u==t else u for u,v in edges if t in (u,v)}
    pins=sorted(set(range(n))-(selected|{t}))
    g, move=pivot(edges,f,ports,pins,k,ell,target); assert g is not None
    assert set(move['selected'])==selected
    boundary=[g[ports[p]] for p in 'PQRS']; fill=extension(boundary);assert fill is not None
    assert extension([f[ports[p]] for p in 'PQRS']) is None
    full_edges=edges+[(n+u,n+v) for u,v in OE]+[(n+v,ports[p]) for v,p in zip(PI,'PQRS')]
    full_rotation=[ls.copy() for ls in rotation]
    for v,p in zip(PI,'PQRS'): full_rotation[ports[p]].insert(1,n+v)
    ir=[['v','u','P'],['a','b'],['u','c','f'],['b','v','d'],['c','a'],['e','c','Q'],['f','d','R'],['b','e','S']]
    for ls in ir:full_rotation.append([n+INNER.index(x) if x in INNER else ports[x] for x in ls])
    ff=faces(full_rotation)
    assert len(full_rotation)-len(full_edges)+len(ff)==2
    assert all(len(ls)<=3 and len(ls)==len(set(ls)) for ls in full_rotation)
    assert {tuple(sorted(e)) for e in full_edges}=={tuple(sorted((v,w))) for v,ls in enumerate(full_rotation) for w in ls}
    assert all(not (set(full_rotation[u])&set(full_rotation[v])) for u,v in full_edges)
    assert valid(full_edges,g+fill)
    Z=set(W)|set(range(n,n+8));cut=[e for e in full_edges if (e[0] in Z)!=(e[1] in Z)]
    chord_count=sum(u in W and v in W for u,v in edges)-(len(W)-1)
    deficit=sum(3-len(full_rotation[v]) for v in W)
    assert len(cut)==len(W)-2-2*chord_count-deficit
    complement=sorted(set(range(n))-set(W)); absorption=[]
    if len(complement)==1:
        pin=complement[0];shift=f[pin]
        witness=[(a-shift)%20 for a in g+fill]
        assert witness[pin]==0 and valid(full_edges,witness)
        absorption.append({'fixed':{str(pin):0},'colors':witness})
    else:
        assert len(complement)==2 and tuple(complement) in [tuple(sorted(e)) for e in edges]
        for distance in range(7,11):
            fixed={complement[0]:0,complement[1]:distance}
            witness=color_graph(n+8,full_edges,fixed);assert witness is not None
            assert valid(full_edges,witness) and all(witness[v]==c for v,c in fixed.items())
            absorption.append({'fixed':{str(v):c for v,c in fixed.items()},'colors':witness})
    h=k//2
    assert k%2==0
    signs=[1 if 1<=(c-h)%20<=9 else -1 for c in f]
    assert all((c-h)%20 not in (0,10) for c in f)
    port_charge=sum(signs[v] for v in ports.values())
    degree_charge=sum(signs[v]*(3-len(full_rotation[v])) for v in range(n))
    assert 3*sum(signs)==port_charge+degree_charge
    edge_certificate=[{'edge':[u,v],'colors':[f[u],f[v]],'directed_difference':(f[v]-f[u])%20,
                       'reverse_difference':(f[u]-f[v])%20,'mixed_difference':(f[v]-tau(k,f[u]))%20,
                       'implications':[[u,v],[v,u]]} for u,v in edges]
    # Test every possible selector for the chosen pivot model, including all pins.
    brute=[]
    target_color=tau(k,f[t]); nn={v if u==t else u for u,v in edges if t in (u,v)}
    for mask in range(1<<n):
        h=[tau(ell,c) if mask>>v&1 else c for v,c in enumerate(f)]
        if valid(edges,h) and all(h[v]==f[v] for v in set(pins)|set(ports.values())) and all(ok(target_color,h[v]) for v in nn):brute.append(mask)
    assert brute and sum(1<<v for v in move['selected']) in brute
    return {'exterior_colors':f,'ports':ports,'primary_axis':k,'pivot_axis':ell,'target':target,
            'exterior_edges':edges,'exterior_rotation':rotation,'conflict_edges':edge_certificate,
            'minimum_steiner_edges':tree,'minimum_steiner_size':len(tree),'steiner_vertices':W,
            'same_axis_legal_masks':allowed,'port_splitting_masks_rejected':len(crossing),
            'cut_obstruction_sha256':hashlib.sha256(json.dumps(crossing,separators=(',',':')).encode()).hexdigest(),
            'fixed_separator':pins,'move':move,'pivot_legal_masks':brute,'new_boundary':boundary,'inner_colors':fill,
            'full_edges':full_edges,'full_rotation':full_rotation,'full_faces':ff,'full_final_colors':g+fill,
            'absorption_cut':{'Z':sorted(Z),'edges':cut,'chords':chord_count,'deficit':deficit},
            'absorption_witnesses':absorption,'charge_identity':{'signs':signs,'port_charge':port_charge,'degree_charge':degree_charge}}

def main():
    data=json.loads((ROOT/'input.json').read_text());fixtures=[]
    for row in data['fixtures']:
        fixtures.append(graph_fixture(row['colors'],row['ports'],row['axis'],row['pivot'],row['target']))
        fixtures.append(graph_fixture([(-c)%20 for c in row['colors']],row['ports'],(-row['axis'])%20,(-row['pivot'])%20,row['target']))
    edges_test=0;invariants=0;half_tests=0
    for k in range(20):
        for a,b in it.product(range(20),repeat=2):
            if not ok(a,b):continue
            old=not ok(tau(k,a),b)
            assert old==(not ok(a,tau(k,b)))
            for u,v in it.product((0,1),repeat=2):
                aa=tau(k,a) if u else a;bb=tau(k,b) if v else b
                if ok(aa,bb):assert (not ok(tau(k,aa),bb))==old;invariants+=1
            if k%2==0 and old:
                h=k//2;x=(a-h)%20;y=(b-h)%20
                assert x not in (0,10) and y not in (0,10) and ((x<10)!=(y<10));half_tests+=1
            edges_test+=1
    mutations=[]
    def detected(name, condition):
        assert condition,name;mutations.append(name)
    detected('exclude_7', ok(0,7) and not 7<abs(0-7)<=13)
    detected('exclude_13',ok(0,13) and not 7<=abs(0-13)<13)
    detected('wrong_directed_distance',not ok(0,19) and (19-0)%20>=7)
    detected('no_modulo_on_reflection',tau(8,9)==19 and not ok(8-9,0) and ok(19,6))
    f=fixtures[0];ee=f['exterior_edges'];old=f['exterior_colors'];k=f['primary_axis']
    bad=old.copy();bad[f['ports']['R']]=tau(k,bad[f['ports']['R']])
    detected('split_conflict_component',not valid(ee,bad))
    v=next(v for v in range(len(old)) if v not in f['steiner_vertices'])
    omitted=old.copy();omitted[v]=tau(k,old[v])
    detected('ignore_nonsteiner_cut_edges',valid(f['minimum_steiner_edges'],omitted) and not valid(ee,omitted))
    detected('wrong_pivot_axis',pivot(ee,old,f['ports'],f['fixed_separator'],8,4,'R')[0] is None)
    pin=f['move']['selected'][0]
    detected('release_fixed_separator',pivot(ee,old,f['ports'],f['fixed_separator']+[pin],8,2,'R')[0] is None)
    detected('mix_old_and_new_witness',not valid(ee,bad) and valid(ee,f['move']['final']))
    detected('identify_equal_colored_ports',f['ports']['Q']!=f['ports']['S'] and old[f['ports']['Q']]==old[f['ports']['S']])
    cut=f['absorption_cut'];detected('omit_absorption_deficit',len(cut['edges'])!=len(f['steiner_vertices'])-2-2*cut['chords'])
    detected('call_absorption_three_port',len(cut['edges'])!=3)
    result={'verdict':'candidate_only','fixtures':fixtures,'palette_edge_axis_controls':edges_test,
            'legal_edge_selector_invariance_controls':invariants,'bipartite_edge_controls':half_tests,
            'mutations':mutations,'closed_residual_classes':[], 'open_residual_classes':['C1','C2','C3','C4'],
            'scope':'Two explicit cycle exteriors and their negations; no replacement search, no minimum-root-obstruction claim.'}
    (ROOT/'certificate.json').write_text(json.dumps(result,sort_keys=True,separators=(',',':'))+'\n')
    print(json.dumps({'fixtures':len(fixtures),'palette_controls':edges_test,'selector_invariance_controls':invariants,
                      'mutation_count':len(mutations),'closed_residual_classes':[]}))

if __name__=='__main__':main()
