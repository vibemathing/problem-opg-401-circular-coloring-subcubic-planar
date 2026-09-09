#!/usr/bin/env python3
import json, sys
from itertools import combinations, product
from functools import lru_cache
from pathlib import Path

HERE=Path(__file__).resolve().parent
INP=json.loads((HERE/"input.json").read_text())
CERT=json.loads((HERE/"certificate.json").read_text())

def delta(a,b):
    d=(a-b)%20
    return min(d,20-d)
def edge(a,b):
    return delta(a,b)>=7

MAPS=INP["maps"]
PAIR_SETS=[set(x) for x in INP["pair_distance_sets"]]
OE=[tuple(x) for x in INP["O"]["edges"]]
PORT=INP["O"]["port_vertices"]

A=[[x for x in range(20) if edge(x,c)] for c in range(20)]
TARGET_N=[set(A[c]) for c in range(20)]

def graph_edges(D):
    out=set()
    for u in range(20):
        for d in D:
            out.add(tuple(sorted((u,(u+d)%20))))
    return sorted(out)

def generic_homs(D, fixed=None):
    fixed=fixed or {0:0}
    E=graph_edges(D)
    adj=[set() for _ in range(20)]
    for u,v in E:
        adj[u].add(v);adj[v].add(u)
    dom=[set(range(20)) for _ in range(20)]
    for u,x in fixed.items(): dom[u]={x}
    sols=[];nodes=0
    def ac3(ds):
        changed=True
        while changed:
            changed=False
            for u in range(20):
                for v in adj[u]:
                    nd={x for x in ds[u] if TARGET_N[x]&ds[v]}
                    if nd!=ds[u]:
                        ds[u]=nd;changed=True
                        if not nd:return False
        return True
    def rec(ds):
        nonlocal nodes
        nodes+=1
        ds=[set(x) for x in ds]
        if not ac3(ds):return
        if all(len(x)==1 for x in ds):
            sols.append(tuple(next(iter(x)) for x in ds));return
        u=min((i for i in range(20) if len(ds[i])>1),
              key=lambda i:(len(ds[i]),-len(adj[i]),i))
        for x in sorted(ds[u]):
            nd=[set(z) for z in ds];nd[u]={x};rec(nd)
    rec(dom)
    return sols,nodes

def injective_embeddings(D):
    E=graph_edges(D)
    adj=[set() for _ in range(20)]
    for u,v in E:
        adj[u].add(v);adj[v].add(u)
    assign={0:0};used={0};sols=[];nodes=0
    def candidates(v):
        out=[]
        for x in range(20):
            if x in used:continue
            if all(u not in assign or edge(x,assign[u]) for u in adj[v]):
                out.append(x)
        return out
    def rec():
        nonlocal nodes
        nodes+=1
        if len(assign)==20:
            sols.append(tuple(assign[i] for i in range(20)));return
        verts=[v for v in range(20) if v not in assign]
        v=min(verts,key=lambda z:(len(candidates(z)),
                                  -sum(u in assign for u in adj[z]),z))
        for x in candidates(v):
            assign[v]=x;used.add(x);rec();used.remove(x);del assign[v]
    rec()
    return sols,nodes

def independent_counts(D):
    E=graph_edges(D)
    masks=[(1<<u)|(1<<v) for u,v in E]
    def ok(C):
        m=sum(1<<v for v in C)
        return all((m&e)!=e for e in masks)
    n7=sum(ok(C) for C in combinations(range(20),7))
    n8=sum(ok(C) for C in combinations(range(20),8))
    return n7,n8

@lru_cache(None)
def find_o(P,Q,R,S):
    for e in A[R]:
      for d in A[Q]:
       if edge(d,e):
        for f in A[S]:
         if edge(e,f):
          for b in A[f]:
           for c in A[d]:
            if edge(b,c):
             for a in A[P]:
              us=[u for u in range(20) if edge(a,u) and edge(u,b)]
              vs=[v for v in range(20) if edge(a,v) and edge(v,c)]
              if us and vs:return (a,us[0],b,c,vs[0],d,e,f)
    return None

def valid_o(boundary,w):
    return (all(edge(w[u],w[v]) for u,v in OE) and
            all(edge(w[v],c) for v,c in zip(PORT,boundary)))

def mixed_exists(colors,edges):
    for opts in product(range(3),repeat=len(colors)):
        if all(edge(MAPS[opts[u]][colors[u]],MAPS[opts[v]][colors[v]])
               for u,v in edges):
            return opts
    return None

expected_id=tuple(range(20))
expected_ref=(0,)+tuple(range(19,0,-1))
pair_rows=[]
for D in PAIR_SETS:
    sols,nodes=generic_homs(D)
    assert set(sols)=={expected_id,expected_ref}
    inj,inj_nodes=injective_embeddings(D)
    assert set(inj)==set(sols)
    n7,n8=independent_counts(D)
    assert n8==0 and n7 in (20,40)
    t7=[]
    for image in range(7,14):
        ss,nn=generic_homs(D,{0:0,7:image})
        t7.append({"image":image,"solutions":len(ss),"nodes":nn})
    pair_rows.append({
        "distances":sorted(D),"alpha":7,
        "max_independent_count":n7,"size8_independent_count":n8,
        "generic_nodes":nodes,"injective_nodes":inj_nodes,
        "normalized_maps":[list(x) for x in sols],"t7_table":t7})
assert pair_rows==CERT["pair_rows"]

unique={}
option_rows=0
for p in (1,14):
 for sig in product(range(3),repeat=5):
    X=MAPS[sig[0]][13];Y=MAPS[sig[1]][13]
    y=MAPS[sig[2]][9];P=MAPS[sig[3]][p];S=MAPS[sig[4]][0]
    ans=None
    for q in range(20):
     if edge(q,X) and edge(q,y):
      for r in range(20):
       if edge(r,Y) and edge(r,y):
        ow=find_o(P,q,r,S)
        if ow:ans=(q,r,ow);break
      if ans:break
    assert ans
    key=(p,X,Y,y,P,S)
    unique.setdefault(key,ans)
    option_rows+=1
assert option_rows==486 and len(unique)==48
cert_rows={(r["p"],*r["terminal"]):(r["Q"],r["R"],tuple(r["O"]))
           for r in CERT["terminal_unique_rows"]}
assert cert_rows=={k:(v[0],v[1],tuple(v[2])) for k,v in unique.items()}
for (p,X,Y,y,P,S),(q,r,ow) in unique.items():
    assert edge(q,X) and edge(q,y) and edge(r,Y) and edge(r,y)
    assert valid_o((P,q,r,S),ow)

bad=[]
for a,b,c in product(range(20),repeat=3):
    if edge(a,b) and edge(b,c) and mixed_exists([a,b,c],[(0,1),(1,2)]) is None:
        bad.append([a,b,c])
assert bad==CERT["all_unsat_ordered_paths"]
assert len(bad)==30
obs=CERT["path_obstruction"]
assert obs["colors"]==[19,8,0]
assert mixed_exists(obs["colors"],[(0,1),(1,2)]) is None
assert mixed_exists(obs["colors"],[(0,1)]) is not None
assert mixed_exists(obs["colors"],[(1,2)]) is not None
left={j for i in range(3) for j in range(3)
      if edge(MAPS[i][19],MAPS[j][8])}
right={i for i in range(3) for j in range(3)
       if edge(MAPS[i][8],MAPS[j][0])}
assert left=={1,2} and right=={0} and not(left&right)

mut=0
for m,c,d in [(0,0,9),(0,0,10),(1,0,8),(1,0,10),(2,0,8),(2,0,9)]:
    assert edge(c,(c+d)%20) and not edge(MAPS[m][c],MAPS[m][(c+d)%20]);mut+=1
for middle in range(3):
    assert not (middle in left and middle in right);mut+=1
assert mixed_exists([19,8,1],[(0,1),(1,2)]) is not None;mut+=1
assert mixed_exists([18,8,0],[(0,1),(1,2)]) is not None;mut+=1
assert all(valid_o((P,q,r,S),ow) for (p,X,Y,y,P,S),(q,r,ow) in unique.items());mut+=1
sample=next(iter(unique.items()))
(p,X,Y,y,P,S),(q,r,ow)=sample
badw=list(ow);badw[0]=(badw[0]+1)%20
assert not valid_o((P,q,r,S),badw);mut+=1
assert delta(19,8)==9 and delta(8,0)==8;mut+=1
assert len(set(tuple(x) for x in bad))==30;mut+=1
assert mut==15

print(json.dumps({
 "status":"ok","pair_graphs":3,
 "generic_nodes":sum(r["generic_nodes"] for r in pair_rows),
 "injective_nodes":sum(r["injective_nodes"] for r in pair_rows),
 "max_independent_counts":[r["max_independent_count"] for r in pair_rows],
 "terminal_option_rows":option_rows,"terminal_unique_states":len(unique),
 "unsat_ordered_paths":len(bad),"minimal_path_vertices":3,
 "mutations":mut,"python":sys.version.split()[0]
},sort_keys=True,separators=(",",":")))
