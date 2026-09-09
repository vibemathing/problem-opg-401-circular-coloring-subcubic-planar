#!/usr/bin/env python3
import json, sys
from itertools import product
from pathlib import Path
from collections import deque

HERE=Path(__file__).resolve().parent
inp=json.loads((HERE/"input.json").read_text())
cert=json.loads((HERE/"certificate.json").read_text())

def dist(a,b):
    d=(a-b)%20
    return min(d,20-d)
def edge(a,b):
    return dist(a,b)>=7

A=[[x for x in range(20) if edge(x,c)] for c in range(20)]
AM=[sum(1<<x for x in A[c]) for c in range(20)]
B6=[sum(1<<x for x in range(20) if dist(x,c)<=6) for c in range(20)]
OE=[(0,1),(1,2),(2,3),(3,4),(4,0),(3,5),(5,6),(6,7),(7,2)]
PORT=[0,5,6,7]
_cache={}
def find_o(P,Q,R,S):
    key=(P,Q,R,S)
    if key in _cache:return _cache[key]
    Ap=AM[P]
    for e in A[R]:
      for d in A[Q]:
       if edge(d,e):
        for f in A[S]:
         if edge(e,f):
          for b in A[f]:
           cm=AM[d]&AM[b]
           while cm:
            l=cm&-cm;c=l.bit_length()-1;cm-=l
            am=Ap&B6[b]&B6[c]
            if am:
             a=(am&-am).bit_length()-1
             um=AM[a]&AM[b];vm=AM[a]&AM[c]
             if um and vm:
              u=(um&-um).bit_length()-1
              v=(vm&-vm).bit_length()-1
              ans=(a,u,b,c,v,d,e,f);_cache[key]=ans;return ans
    _cache[key]=None;return None

rows={(r["p"],r["bits"]["X"],r["bits"]["y"],r["bits"]["P"],r["bits"]["S"]):r
      for r in cert["hit_rows"]}
assert len(rows)==32
hit_success=0
for p in (1,14):
 for x,h,pa,s in product((0,1),repeat=4):
  X=13-x;Y=12;y=9-h;P=(p-pa)%20;S=(-s)%20
  sols=[]
  for q,r in product(range(20),repeat=2):
   if edge(q,y) and edge(q,X) and edge(r,y) and edge(r,Y):
    w=find_o(P,q,r,S)
    if w:sols.append((q,r,w))
  expected=(not h) or ((not pa) and (x or s)) if p==1 else ((not h) or (not s))
  assert bool(sols)==expected
  row=rows[(p,x,h,pa,s)]
  assert row["good"]==expected
  if expected:
   hit_success+=1
   w=row["witness"];q=w["Q"];r=w["R"];ow=tuple(w["O"])
   assert edge(q,y) and edge(q,X) and edge(r,y) and edge(r,Y)
   assert ow==find_o(P,q,r,S) or all(edge(ow[u],ow[v]) for u,v in OE)
   assert all(edge(ow[v],c) for v,c in zip(PORT,(P,q,r,S)))
  else:
   assert row["witness"] is None
assert hit_success==23

rt={(r["S"],r["Q"],r["R"]):r["P_values"] for r in cert["restricted_O_table"]}
assert len(rt)==18
for S in (0,19):
 for q,r in product((0,1,19),repeat=2):
  Ps=[P for P in range(20) if find_o(P,q,r,S)]
  assert Ps==rt[(S,q,r)]
assert rt[(0,1,19)]==list(range(8,20))
assert rt[(0,19,1)]==list(range(1,13))
assert rt[(19,0,1)]==list(range(1,13))
assert rt[(19,19,1)]==list(range(1,13))

pairs=[(i,j) for i in range(5) for j in range(5) if i!=j]
seen=set();preorders=0
for mask in range(1<<20):
 reach=[1<<i for i in range(5)]
 for k,(i,j) in enumerate(pairs):
  if (mask>>k)&1:reach[i]|=1<<j
 for k in range(5):
  rk=reach[k];bk=1<<k
  for i in range(5):
   if reach[i]&bk:reach[i]|=rk
 rel=tuple(reach)
 if rel in seen:continue
 seen.add(rel);preorders+=1
 ex1=ex14=False
 for s in range(32):
  if not(s&1):continue
  if all(not((s>>i)&1) or not(reach[i]&~s) for i in range(5)):
   x=(s>>1)&1;h=(s>>2)&1;pa=(s>>3)&1;ss=(s>>4)&1
   ex1 |= (not h) or ((not pa) and (x or ss))
   ex14 |= (not h) or (not ss)
 pred1=not(bool((reach[0]>>2)&1) and
           (bool((reach[0]>>3)&1) or
            (bool((reach[1]>>3)&1) and bool((reach[4]>>3)&1))))
 pred14=not(bool((reach[0]>>2)&1) and bool((reach[0]>>4)&1))
 assert ex1==pred1 and ex14==pred14
assert preorders==6942

no_go=0
for dY,dS,dX,dP,dy in product(range(7),repeat=5):
 if not(dY<=dS<=dy and dX<=dy and dP<=dy):continue
 no_go+=1
 X=(13-dX)%20;Y=(13-dY)%20;y=(9-dy)%20
 P=(14-dP)%20;S=(-dS)%20
 possible=False
 for q,r in product(range(20),repeat=2):
  if edge(q,y) and edge(q,X) and edge(r,y) and edge(r,Y) and find_o(P,q,r,S):
   possible=True;break
 assert not possible
assert no_go==2730==cert["p14_bounded_drop_assignments_checked"]

def verify_fixture(F):
 V=set(F["vertices"]);E={tuple(sorted(e)) for e in F["edges"]}
 assert all(a in V and b in V and a!=b for a,b in E)
 adj={v:set() for v in V}
 for a,b in E:adj[a].add(b);adj[b].add(a)
 assert max(map(len,adj.values()))<=3
 q=deque([next(iter(V))]);seenV={q[0]}
 while q:
  u=q.popleft()
  for v in adj[u]:
   if v not in seenV:seenV.add(v);q.append(v)
 assert seenV==V
 assert not any((adj[a]&adj[b]) for a,b in E)
 rot=F["rotation"]
 assert set(rot)==V
 for v in V:assert set(rot[v])==adj[v] and len(rot[v])==len(adj[v])
 seenD=set();faces=[]
 for u in sorted(V):
  for v in rot[u]:
   if (u,v) in seenD:continue
   face=[];a,b=u,v
   while (a,b) not in seenD:
    seenD.add((a,b));face.append(a)
    ns=rot[b];c=ns[(ns.index(a)+1)%len(ns)]
    a,b=b,c
   faces.append(face)
 assert len(seenD)==2*len(E)
 assert len(V)-len(E)+len(faces)==2
 assert sorted(map(len,faces))==sorted(map(len,F["faces"]))
 old=F["old_exterior_colors"]
 for a,b in E:
  if a in old and b in old:assert edge(old[a],old[b])
 new=F["new_full_colors"]
 assert set(new)==V and all(edge(new[a],new[b]) for a,b in E)
 for path in F["zero_paths"].values():
  for a,b in zip(path,path[1:]):
   assert tuple(sorted((a,b))) in E
   assert (old[b]-old[a])%20==13
 Z={v:[] for v in old}
 for a,b in E:
  if a in old and b in old:
   if (old[b]-old[a])%20==13:Z[a].append(b)
   if (old[a]-old[b])%20==13:Z[b].append(a)
 def reach(s,t):
  dq=deque([s]);vis={s}
  while dq:
   u=dq.popleft()
   if u==t:return True
   for v in Z[u]:
    if v not in vis:vis.add(v);dq.append(v)
  return False
 if F["p"]==1:
  assert all(reach(a,b) for a,b in (("Y","y"),("X","P"),("X","y"),("S","P"),("S","y")))
 else:
  assert all(reach(a,b) for a,b in (("Y","S"),("S","y"),("X","y"),("P","y")))

for F in cert["fixtures"]:verify_fixture(F)

F1=next(F for F in cert["fixtures"] if F["p"]==1)
old=F1["old_exterior_colors"]
E={tuple(e) for e in F1["edges"]}
K=set(old)-{"Q","R"}
arcs={v:[] for v in K}
for a,b in E:
 if a in K and b in K:
  rab=(old[b]-old[a])%20
  arcs[a].append((b,13-rab));arcs[b].append((a,rab-7))
def shortest(src):
 INF=10**9;d={v:INF for v in K};d[src]=0
 used=set()
 while len(used)<len(K):
  u=min((v for v in K if v not in used),key=lambda v:d[v],default=None)
  if u is None or d[u]>=INF:break
  used.add(u)
  for v,w in arcs[u]:
   if d[v]>d[u]+w:d[v]=d[u]+w
 return d
dY=shortest("Y");dP=shortest("P")
ds={v:max(0,1-dY[v],2-dP[v]) for v in K}
assert {v:x for v,x in ds.items() if x}==cert["p1_fixture_least_positive_displacements"]
new={v:(old[v]-ds.get(v,0))%20 for v in old}
new["Q"]=1;new["R"]=19
ow=find_o(19,1,19,0)
for v,c in zip(inp["O"]["vertices"],ow):new[v]=c
assert all(edge(new[a],new[b]) for a,b in E)

assert edge(0,7) and edge(0,13)
assert not edge(0,6) and not edge(0,14)
assert (13-0)%20==13 and (7-0)%20==7
assert not rows[(1,0,1,1,0)]["good"]
assert rows[(1,1,1,0,0)]["good"]
assert not rows[(14,1,1,0,1)]["good"]
assert rows[(14,0,1,1,0)]["good"]
assert find_o(1,19,1,0) and not find_o(0,19,1,0)
assert find_o(14,1,19,0) and not find_o(14,1,19,19)
assert all((13+13*L)%20==t for L,t in ((12,9),(16,1),(17,14),(19,0)))
mutations=14

out={"status":"ok","hit_rows":32,"hit_success":hit_success,
 "restricted_O_rows":18,"preorders":preorders,
 "p14_bounded_drop_states":no_go,"fixtures":len(cert["fixtures"]),
 "mutations":mutations,"python":sys.version.split()[0]}
print(json.dumps(out,separators=(",",":"),sort_keys=True))
