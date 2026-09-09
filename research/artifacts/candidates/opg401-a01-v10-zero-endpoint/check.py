"""Finite controls only. Literal O DFS, scalar edges, no imported old tables."""
import json
from collections import deque
from functools import lru_cache
from itertools import product
from pathlib import Path

PAL=range(20)
OE=((0,1),(1,2),(2,3),(3,4),(4,0),(3,5),(5,6),(6,7),(7,2))
PORT=(0,5,6,7)

def edge(a,b): return 0<=a<20 and 0<=b<20 and 7<=abs(a-b)<=13

def weight(a,b):
    r=(b-a)%20
    assert 7<=r<=13
    return 13-r

A=[sum(1<<z for z in PAL if edge(c,z)) for c in PAL]

def valid(es,f): return all(edge(f[u],f[v]) for u,v in es)

@lru_cache(None)
def fill(bd):
    adj=[set() for _ in range(8)]; dom=[(1<<20)-1]*8
    for u,v in OE: adj[u].add(v); adj[v].add(u)
    for v,c in zip(PORT,bd): dom[v]=A[c]
    out=[-1]*8; nodes=0
    def rec(left,ds):
        nonlocal nodes
        nodes+=1
        if nodes>200000: raise RuntimeError('O DFS cap: no negative verdict')
        if not left: return out.copy()
        v=min(left,key=lambda u:(ds[u].bit_count(),u)); rest=left-{v}; mask=ds[v]
        while mask:
            bit=mask&-mask; mask-=bit; c=bit.bit_length()-1
            nd=ds.copy()
            for u in adj[v]&left-{v}:
                nd[u]&=A[c]
                if not nd[u]: break
            else:
                out[v]=c; ans=rec(rest,nd)
                if ans is not None: return ans
        out[v]=-1
        return None
    return rec(set(range(8)),dom)

def faces(rot):
    darts={(u,v) for u,ns in enumerate(rot) for v in ns}; seen=set(); fs=[]
    assert len(darts)==sum(map(len,rot))
    assert all((v,u) in darts for u,v in darts)
    for start in sorted(darts):
        if start in seen: continue
        u,v=start; row=[]
        while (u,v) not in seen:
            seen.add((u,v)); row.append(u); ns=rot[v]
            u,v=v,ns[(ns.index(u)+1)%len(ns)]
        assert (u,v)==start
        fs.append(row)
    return fs

def graphcheck(row):
    f=row['colors']; n=len(f); es={tuple(e) for e in row['edges']}
    assert all(0<=u<v<n for u,v in es) and valid(es,f)
    full=es|{(n+min(u,v),n+max(u,v)) for u,v in OE}
    full|={tuple(sorted((n+v,t))) for v,t in zip(PORT,row['ports'])}
    rot=row['full_rotation']
    assert len(rot)==n+8
    assert {tuple(sorted((u,v))) for u,ns in enumerate(rot) for v in ns}==full
    assert all(len(ns)==len(set(ns))<=3 for ns in rot)
    assert all(not(set(rot[u])&set(rot[v])) for u,v in full)
    seen={0}; q=[0]
    for u in q:
        for v in rot[u]:
            if v not in seen: seen.add(v); q.append(v)
    assert len(seen)==n+8
    fs=faces(rot); assert len(rot)-len(full)+len(fs)==2
    return sorted(full),fs

def zero_cone(row):
    f=row['colors']; r=row['roles']; n=len(f); adj=[[] for _ in f]
    removed={r['Q'],r['R']}
    for u,v in row['edges']:
        if u in removed or v in removed: continue
        if weight(f[u],f[v])==0: adj[u].append(v)
        if weight(f[v],f[u])==0: adj[v].append(u)
    par={r['Y']:None}; todo=deque([r['Y']])
    while todo:
        u=todo.popleft()
        for v in sorted(adj[u]):
            if v not in par: par[v]=u; todo.append(v)
    protected={row['ports'][0],row['ports'][3],r['y']}
    hits=sorted(set(par)&protected)
    path=None
    if hits:
        v=hits[0]; path=[v]
        while par[v] is not None: v=par[v]; path.append(v)
        path.reverse()
    return sorted(par),path

def ledger(row,W):
    W=set(W); n=len(row['colors']); ports=set(row['ports'])
    deg=[0]*n
    for u,v in row['edges']: deg[u]+=1;deg[v]+=1
    d=sum(3-deg[v]-(v in ports) for v in W)
    c=sum(u in W and v in W for u,v in row['edges'])-len(W)+1
    k=len(W&ports)
    cut=[list(e) for e in row['edges'] if (e[0] in W)!=(e[1] in W)]
    cut += [[n+v,t] for v,t in zip(PORT,row['ports']) if t not in W]
    assert len(cut)==len(W)+6-2*k-2*c-d
    endpoints=[v if u in W or u>=n else u for u,v in cut]
    return dict(n=len(W),k=k,c=c,d=d,b=len(cut),cut=cut,
                exterior_variables=sorted(set(endpoints)))

def main():
    root=Path(__file__).resolve().parent
    data=json.loads((root/'input.json').read_text())
    out=dict(schema='opg401-zero-endpoint-certificate-v1',verdict='candidate_only')
    tables=[]
    for p,t in product((1,14),range(7)):
        states=0; positives=0; best=99; witness=None
        for q,r,z in product(PAL,repeat=3):
            if not(edge(q,13) and edge(q,9) and edge(r,9) and edge(r,z)
                   and edge(z,0) and edge(z,t)): continue
            states+=1; f=fill((p,q,r,0))
            if f is None: continue
            positives+=1; cost=(q!=0)+(r!=2)+(z!=13)
            if cost<best: best=cost; witness=[q,r,z,f]
        assert (positives>0)==(t<=5)
        if t==5: assert best==3
        tables.append(dict(p=p,t=t,legal_states=states,filling_states=positives,
                           min_support=None if best==99 else best,witness=witness))
    out['local_tables']=tables
    cases=[]
    for row in data['fixtures']:
        f=row['colors']; n=len(f); r=row['roles']; p=f[row['ports'][0]]
        full,fs=graphcheck(row)
        assert [f[v] for v in row['ports']]==[p,0,2,0]
        assert fill((p,0,2,0)) is None
        cone,path=zero_cone(row)
        g=f.copy();g[r['Q']]=2;g[r['R']]=19
        for v in cone:g[v]=(f[v]-1)%20
        forbidden=path is not None
        if not forbidden:
            assert valid(row['edges'],g)
            assert all(g[v]==f[v] for v in range(n) if v not in set(cone)|{r['Q'],r['R']})
        else:
            assert row['id'].startswith('return')
            assert path==list(range(13))
            assert all((f[v]-f[u])%20==13 for u,v in zip(path,path[1:]))
            assert f[path[0]]==13 and f[path[-1]]==9
            assert (17*(9-13))%20==12
            assert not valid(row['edges'],g)
            # This is an explicit non-unit escape, not a claim of a bounded shift.
            g=f.copy()
            for i in range(12):g[i]=12 if i%2==0 else 2
            g[r['Q']]=2;g[r['R']]=19
            assert valid(row['edges'],g)
        inn=fill(tuple(g[v] for v in row['ports']))
        assert inn is not None and valid(full,g+inn)
        shared=None
        if r['X']==r['Y']:
            shared=f.copy();shared[r['Y']]=12;shared[r['Q']]=19
            sf=fill(tuple(shared[v] for v in row['ports']))
            assert sf is not None and valid(full,shared+sf)
            shared=dict(colors=shared,O_fill=sf,support=[r['Q'],r['Y']])
        W0={r['Q'],r['R'],r['y']}; W1=W0|set(cone)
        if forbidden: W1=W0|set(range(13))
        cases.append(dict(id=row['id'],zero_cone=cone,failure_path=path,
              path_differences=[] if path is None else [13]*(len(path)-1),
              new_colors=g,O_fill=inn,shared_minimum=shared,
              changed_vertices=[v for v in range(n) if g[v]!=f[v]],
              fixed_vertices=[v for v in range(n) if g[v]==f[v]],
              full_faces=fs,before=ledger(row,W0),after=ledger(row,W1)))
    out['cases']=cases
    # Complete local scalar control of zero-slack implication, not a graph census.
    count=0
    for a,b in product(PAL,repeat=2):
        if not edge(a,b):continue
        for du,dv in product(range(7),repeat=2):
            truth=edge((a-du)%20,(b-dv)%20)
            pred=(du-dv<=weight(a,b) and dv-du<=weight(b,a))
            assert truth==pred;count+=1
    mutations=[]
    def test(name,detected):
        assert detected,name
        mutations.append(name)
    test('omit_7',edge(0,7) and not 7<abs(0-7)<=13)
    test('omit_13',edge(0,13) and not 7<=abs(0-13)<13)
    test('use_linear_lift',edge(19,6) and not 7<=abs(19-46)<=13)
    test('reverse_zero_direction',weight(0,13)==0 and weight(13,0)==6)
    test('ignore_third_neighbor_six',not edge(12,6))
    test('update_R_before_endpoint',not edge(19,13))
    test('retain_original_R_after_joint_fill',fill((1,2,2,0)) is None)
    row=next(x for x in data['fixtures'] if x['id']=='return-p1')
    g=next(x['new_colors'] for x in cases if x['id']=='return-p1')
    test('delete_chord',edge(row['colors'][1],row['colors'][5]) and not edge(g[1],g[5]))
    test('silently_release_y',not edge(2,8))
    test('collapse_shared_vertex',data['fixtures'][2]['roles']['X']==data['fixtures'][2]['roles']['Y'] and 12!=13)
    test('wrong_return_length',all((13+13*l)%20!=9 for l in range(12)))
    test('pretend_one_changed_vertex_suffices',not any(x['min_support']==1 for x in tables))
    test('use_four_port_cut_formula',cases[0]['before']['k']==2 and cases[0]['before']['b']!=cases[0]['before']['n']-2-2*cases[0]['before']['c']-cases[0]['before']['d'])
    test('erase_duplicate_pin_incidence',cases[2]['before']['b']>len(cases[2]['before']['exterior_variables']))
    out['mutations']=mutations
    out['counts']=dict(local_parameter_rows=len(tables),literal_local_states=sum(x['legal_states'] for x in tables),
                      complete_graphs=len(cases),edge_displacement_cases=count,mutations=len(mutations))
    target=root/'certificate.json'
    if target.exists():raise FileExistsError('certificate already exists')
    target.write_text(json.dumps(out,separators=(',',':'))+'\n')
    print(json.dumps(out['counts'],sort_keys=True))

if __name__=='__main__':main()
