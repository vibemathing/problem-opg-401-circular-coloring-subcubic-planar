"""Exact finite-object audit. No import of old candidates or target tables.

Certificate format: each target row lists exactly twenty failures, in axis order.
An integer v certifies a zero-choice neighbor. A list [v0,...,vj] certifies a
required-to-forbidden conflict path. All graph edges and actual colors are saved.
The independently recomputed scalar checker checks certificates, not BFS output.
"""
from collections import deque
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path
import json

P=tuple(range(20))
OE=((0,1),(1,2),(2,3),(3,4),(4,0),(3,5),(5,6),(6,7),(7,2))
PORT_INNER=(0,5,6,7)

def edge(a,b): return 7 <= (b-a)%20 <= 13

def scalar(a,b): return 0<=a<20 and 0<=b<20 and 7<=abs(a-b)<=13

A=tuple(frozenset(b for b in P if edge(a,b)) for a in P)

def adjacency(n,edges):
    rows=[set() for _ in range(n)]
    for a,b in edges:
        assert 0<=a<b<n
        rows[a].add(b);rows[b].add(a)
    return rows

@lru_cache(None)
def fill(boundary):
    """Ordinary absolute-difference DFS, literal O edges, no imported table."""
    nb=adjacency(8,sorted(tuple(sorted(e)) for e in OE))
    ds=[set(P) for _ in range(8)]
    for v,c in zip(PORT_INNER,boundary):ds[v]={z for z in P if scalar(c,z)}
    chosen={};nodes=0
    def rec(todo,dd):
        nonlocal nodes
        nodes+=1
        if nodes>100000:raise RuntimeError('O DFS node budget')
        if not todo:return tuple(chosen[v] for v in range(8))
        v=min(todo,key=lambda u:(len(dd[u]),-len(nb[u]),u));rest=todo-{v}
        for c in sorted(dd[v]):
            nd=dd.copy()
            for u in nb[v]&rest:
                nd[u]={z for z in dd[u] if scalar(c,z)}
                if not nd[u]:break
            else:
                chosen[v]=c;ans=rec(rest,nd)
                if ans is not None:return ans
        chosen.pop(v,None)
        return None
    return rec(set(range(8)),ds)

def valid(edges,f):return all(0<=c<20 for c in f) and all(scalar(f[u],f[v]) for u,v in edges)

def ring(n,ports):
    free=[v for v in range(n) if v not in ports];m=len(free)
    rot=[[(i-1)%n,(i+1)%n] for i in range(n)]
    for j,v in enumerate(free):rot[v].append(n+j)
    rot += [[n+(j-1)%m,v,n+(j+1)%m] for j,v in enumerate(free)]
    ee=sorted({tuple(sorted((u,v))) for u,row in enumerate(rot) for v in row})
    return ee,rot

def faces(rot):
    darts={(u,v) for u,row in enumerate(rot) for v in row};seen=set();out=[]
    assert len(darts)==sum(map(len,rot))
    for start in sorted(darts):
        if start in seen:continue
        u,v=start;row=[]
        while (u,v) not in seen:
            seen.add((u,v));row.append(u);rr=rot[v]
            u,v=v,rr[(rr.index(u)+1)%len(rr)]
        assert (u,v)==start
        out.append(row)
    return out

def join_O(rot,ports):
    n=len(rot);rr=[row.copy() for row in rot]
    for t,x in zip(ports,PORT_INNER):rr[t].insert(1,n+x)
    p,q,r,s=ports
    rr += [[n+4,n+1,p],[n,n+2],[n+1,n+3,n+7],[n+2,n+4,n+5],
           [n+3,n],[n+6,n+3,q],[n+7,n+5,r],[n+2,n+6,s]]
    ee=sorted({tuple(sorted((u,v))) for u,row in enumerate(rr) for v in row})
    return ee,rr

def conflict(n,ee,f,ell):
    adj=[[] for _ in range(n)]
    for a,b in ee:
        if not edge((ell-f[a])%20,f[b]):adj[a].append(b);adj[b].append(a)
    return [sorted(row) for row in adj]

def reached(adj,seeds):
    parent={v:None for v in sorted(seeds)};queue=deque(sorted(seeds))
    while queue:
        u=queue.popleft()
        for v in adj[u]:
            if v not in parent:parent[v]=u;queue.append(v)
    return parent

def eligible(f,neighbors,c,z):
    I=A[c]&A[z];ans=set(P)
    for v in neighbors:
        if f[v] not in I:ans &= {(f[v]+x)%20 for x in I}
    return I,ans

def certificate_failure(n,ee,nb,f,ports,t,z,ell,pins=()):
    I=A[f[t]]&A[z]
    for v in sorted(nb[t]):
        if f[v] not in I and (ell-f[v])%20 not in I:return v
    must={v for v in nb[t] if f[v] not in I}
    forbidden={v for v in nb[t] if (ell-f[v])%20 not in I}
    forbidden |= {v for v in set(ports)|set(pins) if (ell-f[v])%20!=f[v]}
    par=reached(conflict(n,ee,f,ell),must)
    hits=sorted(set(par)&forbidden)
    if not hits:return None
    path=[hits[0]]
    while par[path[-1]] is not None:path.append(par[path[-1]])
    return list(reversed(path))

def verify_failure(ee,f,ports,t,z,ell,record,pins=()):
    """Scalar certificate verification: neither BFS nor the generated I is used."""
    n=len(f);es={tuple(sorted(e)) for e in ee}
    neighbors={b if a==t else a for a,b in ee if t in (a,b)}
    def in_I(x):return scalar(f[t],x) and scalar(z,x)
    if isinstance(record,int):
        return record in neighbors and not in_I(f[record]) and not in_I((ell-f[record])%20)
    if not record or len(record)!=len(set(record)) or any(not 0<=v<n for v in record):return False
    a,b=record[0],record[-1]
    required=a in neighbors and not in_I(f[a]) and in_I((ell-f[a])%20)
    forbidden=((b in set(ports)|set(pins) and (ell-f[b])%20!=f[b]) or
               (b in neighbors and in_I(f[b]) and not in_I((ell-f[b])%20)))
    return required and forbidden and all(tuple(sorted((u,v))) in es and
           not scalar((ell-f[u])%20,f[v]) for u,v in zip(record,record[1:]))

def steiner(n,ee,f,k,ports):
    adj=conflict(n,ee,f,k);others=[v for v in range(n) if v not in ports];tested=0
    for size in range(len(others)+1):
        for extra in combinations(others,size):
            tested+=1;W=set(ports)|set(extra)
            local=[[v for v in adj[u] if v in W] if u in W else [] for u in range(n)]
            par=reached(local,[ports[0]])
            if not set(ports)<=set(par):continue
            assert set(par)==W
            te=sorted(tuple(sorted((v,u))) for v,u in par.items() if u is not None)
            c=sum(a in W and b in W for a,b in ee)-(len(W)-1)
            cut=[list(e) for e in ee if (e[0] in W)!=(e[1] in W)]
            assert len(cut)==len(W)-2-2*c
            return {'vertices':sorted(W),'edges':te,'n':len(W),'c':c,'d':0,'b':len(cut),
                    'cut_edges':cut,'subsets_checked':tested}
    raise AssertionError('primary ports disconnected')

def main():
    root=Path(__file__).resolve().parent
    data=json.loads((root/'input.json').read_text());output={'schema':'opg401-all-target-certificate-v1','verdict':'candidate_only'}
    target_tables={};positive=0;negative=0
    for p in (1,14):
        bd=[p,0,2,0];table=[]
        assert fill(tuple(bd)) is None
        for t in range(4):
            row=[]
            for z in P:
                b=bd.copy();b[t]=z;w=fill(tuple(b))
                if w is not None:
                    assert all(scalar(w[a],w[b]) for a,b in OE)
                    assert all(scalar(w[v],c) for v,c in zip(PORT_INNER,b))
                    row.append({'z':z,'fill':w});positive+=1
                else:negative+=1
            table.append(row)
        expected=[list(range(2,14)),list(range(8,20)),list(range(3,18 if p==1 else 19)),list(range(8,20))]
        assert [[x['z'] for x in row] for row in table]==expected
        target_tables[str(p)]=table
    output['target_tables']=target_tables
    cases=[];totals={'target_rows':0,'axis_failures':0,'scalar_failures_checked':0,'path_failures':0,'zero_failures':0}
    for case in data['fixtures']:
        f=case['colors'];ports=case['ports'];n=len(f);p=case['p'];k=case['primary_axis']
        ee,rot=ring(case['inner_cycle'],ports);nb=adjacency(n,ee)
        assert valid(ee,f) and [f[v] for v in ports]==[p,0,2,0]
        assert all(len(nb[v])==(2 if v in ports else 3) for v in range(n))
        assert all(not nb[u]&nb[v] for u,v in ee)
        ff=faces(rot);assert n-len(ee)+len(ff)==2
        full,fr=join_O(rot,ports);fff=faces(fr);assert len(fr)-len(full)+len(fff)==2
        sg=steiner(n,ee,f,k,ports)
        primary=conflict(n,ee,f,k);C=set(reached(primary,[ports[0]]));assert set(ports)<=C
        h=k//2
        def eps(v):
            r=(f[v]-h)%20;assert r not in (0,10)
            return 1 if r<10 else -1
        md=[0]*n
        certedges=[]
        for a,b in ee:
            if b in primary[a]:
                certedges.append([a,b,(f[b]-f[a])%20,(f[a]-f[b])%20,(f[a]+f[b]-k)%20])
            else:md[a]+=1;md[b]+=1
        signed=[sum(eps(v) for v in C),sum(eps(v) for v in ports),sum(eps(v)*md[v] for v in C)]
        assert 3*signed[0]==signed[1]+signed[2]
        rows=[]
        for i,t in enumerate(ports):
            for entry in target_tables[str(p)][i]:
                z=entry['z'];I,E=eligible(f,nb[t],f[t],z);rec=[]
                for ell in P:
                    bad=certificate_failure(n,ee,nb,f,ports,t,z,ell)
                    assert bad is not None
                    assert isinstance(bad,list)==(ell in E)
                    assert verify_failure(ee,f,ports,t,z,ell,bad)
                    # The same path/zero object certifies the actual negated C2 state.
                    assert verify_failure(ee,[(-x)%20 for x in f],ports,t,(-z)%20,(-ell)%20,bad)
                    totals['scalar_failures_checked']+=2
                    totals['axis_failures']+=1
                    totals['path_failures' if isinstance(bad,list) else 'zero_failures']+=1
                    rec.append(bad)
                rows.append({'port':i,'target':z,'I':sorted(I),'eligible_mask':sum(1<<x for x in E),'failures':rec})
                totals['target_rows']+=1
        # Each fixture has a three-single-vertex repair with a fixed complement.
        w,y,t=case['repair_vertices'];assert t==ports[3]
        assert [f[v] for v in (w,y,t)]==[6,13,0]
        stages=[];cur=f.copy()
        for vertex,color in ((w,3),(y,10),(t,17)):
            cur=cur.copy();cur[vertex]=color;assert valid(ee,cur);stages.append(cur)
        pins=sorted(set(range(n))-{w,y,t})
        assert all(state[v]==f[v] for state in stages for v in pins)
        inside=fill(tuple(cur[v] for v in ports));assert inside is not None and valid(full,cur+list(inside))
        for state in [f]+stages:
            assert valid(ee,[(-x)%20 for x in state])
        assert valid(full,[(-x)%20 for x in cur+list(inside)])
        cases.append({'id':case['id'],'ports':ports,'colors':f,'edges':ee,'rotation':rot,'faces':ff,
                      'primary_axis':k,'conflict_edges_forward_reverse_mixed':certedges,'minimum_steiner':sg,
                      'signed_identity':signed,'all_targets':rows,'full_edges':full,'full_rotation':fr,'full_faces':fff,
                      'repair':{'order':[w,y,t],'colors':[3,10,17],'stages':stages,'fixed_vertices':pins,
                                'new_boundary':[cur[v] for v in ports],'O_fill':inside},
                      'C2_transport':'Negate every actual vertex color, target, axis and each intermediate state; leave graph, vertex IDs and failure paths unchanged.'})
    output['cases']=cases;output['counts']=dict(totals,positive_O_targets=positive,negative_O_targets=negative)
    mutations=[]
    def detect(name,predicate,example):
        assert predicate;mutations.append({'mutation':name,'witness':example})
    detect('exclude_7',edge(0,7) and not(7<7<=13),[0,7])
    detect('exclude_13',edge(7,0) and not(7<=13<13),[7,0])
    detect('directed_without_upper',not edge(0,14) and 14>=7,[0,14])
    detect('unreduced_negation',(-1)%20==19 and -1 not in P,[-1,19])
    detect('omit_good_target_17',any(r['z']==17 for r in target_tables['1'][3]),[1,3,17])
    case=cases[0];f=case['colors'];ee=case['edges'];pp=case['ports'];rp=case['repair'];w,y,t=rp['order']
    bad=f.copy();bad[y]=10
    detect('skip_first_helper',not valid(ee,bad),{'changed':y,'edge':[w,y]})
    bad=f.copy();bad[t]=17
    detect('skip_both_helpers',not valid(ee,bad),{'changed':t,'edge':[y,t]})
    pathrow,ell,path=next((r,i,x) for r in case['all_targets'] for i,x in enumerate(r['failures'])
                          if isinstance(x,list) and len(x)>1 and not verify_failure(ee,f,pp,pp[r['port']],r['target'],i,x[:-1]))
    shortened=path[:-1]
    detect('drop_forbidden_endpoint',not verify_failure(ee,f,pp,pp[pathrow['port']],pathrow['target'],ell,shortened),{'ell':ell,'path':path})
    e0=tuple(sorted(path[:2]));reduced=[e for e in ee if tuple(e)!=e0]
    detect('omit_conflict_edge',not verify_failure(reduced,f,pp,pp[pathrow['port']],pathrow['target'],ell,path),list(e0))
    oldonly=next((r,i,x) for r in case['all_targets'] for i,x in enumerate(r['failures']) if isinstance(x,list) and x[-1] not in pp)
    detect('assume_all_forbidden_are_ports',oldonly[2][-1] not in pp,{'port':oldonly[0]['port'],'z':oldonly[0]['target'],'axis':oldonly[1],'path':oldonly[2]})
    detect('equal_color_means_same_vertex',pp[1]!=pp[3] and f[pp[1]]==f[pp[3]],pp)
    detect('treat_tree_cut_as_three',case['minimum_steiner']['b']>3,case['minimum_steiner']['cut_edges'])
    detect('reuse_original_colors_in_second_step',not scalar(10,f[w]) and scalar(10,rp['stages'][0][w]),[f[w],rp['stages'][0][w]])
    detect('ignore_fixed_helper',rp['stages'][0][w]!=f[w],{'add_pin':w})
    assert len(mutations)==14
    output['mutations']=mutations;output['closed_residual_classes']=[];output['open_residual_classes']=['C1','C2','C3','C4']
    text=json.dumps(output,separators=(',',':'),sort_keys=True)+'\n'
    assert len(text.encode())<1048576
    (root/'certificate.json').write_text(text)
    print(json.dumps(dict(output['counts'],fixtures_with_negation=4,mutations_detected=len(mutations),certificate_bytes=len(text.encode()),verdict='candidate_only'),sort_keys=True))

if __name__=='__main__':main()
