#!/usr/bin/env python3
from itertools import product
import json
I=list(range(20))
T8=[0,16,12,8,4,0,16,12,8,4,0,16,12,8,4,0,16,12,8,4]
T9=[0,7]*10
T10=[0,7,14,0,7,0,1,7,0,3,7,0,7,8,0,7,10,0,7,14]
M=[I,T8,T9,T10]; M3=[T8,T9,T10]
def d(a,b):
    q=(a-b)%20; return min(q,20-q)
def ok(a,b): return d(a,b)>=7
def rel4(a,b): return {(i,j) for i,A in enumerate(M) for j,B in enumerate(M) if ok(A[a],B[b])}
def rel3(a,b): return {(i,j) for i,A in enumerate(M3) for j,B in enumerate(M3) if ok(A[a],B[b])}
def unsat_path(a,b,c):
    if not(ok(a,b) and ok(b,c)): return False
    L=rel3(a,b); R=rel3(b,c)
    return not any((i,j) in L and (j,k) in R for i,j,k in product(range(3),repeat=3))
unsat=[(a,b,c) for a,b,c in product(range(20),repeat=3) if unsat_path(a,b,c)]
assert len(unsat)==30
def supp3(b,n): return {i for i in range(3) if any((i,j) in rel3(b,n) for j in range(3))}
rigid=set()
for a,b,c in unsat:
    for t in range(20):
        if not ok(b,t): continue
        avail=[x for x in range(20) if ok(x,a) and ok(x,c) and ok(x,t)]
        if avail and all(not(supp3(x,a)&supp3(x,c)&supp3(x,t)) for x in avail): rigid.add((b,tuple(sorted((a,c,t)))))
rigid=sorted(rigid); assert len(rigid)==21
groups={}
for b,ns in rigid: groups.setdefault(ns,[]).append(b)
assert groups=={(13,14,16):[3,4,5,6],(3,6,7):[14,15,16],(4,6,7):[14,15,16,17],(5,6,7):[14,15,16,17,18],(6,7,8):[15,16,17,18,19]}
def cycle_valid(col): return col[0]==13 and all(ok(col[i],col[(i+1)%len(col)]) for i in range(len(col)))
def root_unpinned(col):
    n=len(col); R=[rel4(col[i],col[(i+1)%n]) for i in range(n)]
    return any(s[0]!=0 and all((s[i],s[(i+1)%n]) in R[i] for i in range(n)) for s in product(range(4),repeat=n))
def root_pinned(col):
    if not cycle_valid(col): return False
    n=len(col); R=[rel4(col[i],col[(i+1)%n]) for i in range(n)]
    sols=[s for s in product(range(4),repeat=n) if all((s[i],s[(i+1)%n]) in R[i] for i in range(n))]
    return bool(sols) and all(s[0]==0 for s in sols)
def one_repair(col):
    n=len(col)
    for v in range(1,n):
        for c in range(20):
            if c==col[v]: continue
            q=list(col); q[v]=c
            if all(ok(q[i],q[(i+1)%n]) for i in range(n)) and root_unpinned(q): return (v,c,tuple(q))
def unit_repair(col):
    n=len(col)
    for mask in range(1,1<<(n-1)):
        vs=[i+1 for i in range(n-1) if mask>>i&1]
        for eps in (-1,1):
            q=list(col)
            for v in vs: q[v]=(q[v]+eps)%20
            if all(ok(q[i],q[(i+1)%n]) for i in range(n)) and root_unpinned(q): return (tuple(vs),eps,tuple(q))
stats={}; pins_by_n={}
for n in (4,5):
    pins=[]
    for tail in product(range(20),repeat=n-1):
        col=(13,)+tail
        if root_pinned(col): pins.append(col)
    no_one=[c for c in pins if one_repair(c) is None]
    no_unit=[c for c in pins if unit_repair(c) is None]
    no_both=[c for c in pins if one_repair(c) is None and unit_repair(c) is None]
    stats[n]={"pins":len(pins),"no_one":len(no_one),"no_unit":len(no_unit),"no_both":len(no_both),"no_both_rows":[list(x) for x in no_both]}; pins_by_n[n]=pins
assert stats[4]=={"pins":27,"no_one":0,"no_unit":0,"no_both":0,"no_both_rows":[]}
assert stats[5]["pins"]==180 and stats[5]["no_one"]==88 and stats[5]["no_unit"]==26 and stats[5]["no_both"]==18
rep=(13,0,7,15,4); rep2=(13,0,7,14,1)
assert rep in pins_by_n[5] and one_repair(rep) is None and unit_repair(rep) is None
assert cycle_valid(rep2) and root_unpinned(rep2)
out={"unsat_paths":[list(x) for x in unsat],"rigid_star_groups":[{"neighbors":list(k),"center_colors":v} for k,v in sorted(groups.items())],"cycle_stats":stats,"representative":{"old":list(rep),"two_vertex_repair":list(rep2),"changed_vertices":[3,4]},"status":"ok"}
print(json.dumps(out,separators=(",",":"),sort_keys=True))
