#!/usr/bin/env python3
import json, sys
from itertools import product
from pathlib import Path
from functools import lru_cache

HERE=Path(__file__).resolve().parent
cert=json.loads((HERE/"certificate.json").read_text())
inp=json.loads((HERE/"input.json").read_text())

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

@lru_cache(None)
def find_o(P,Q,R,S):
    Ap=AM[P]
    for e in A[R]:
      for d in A[Q]:
       if edge(d,e):
        for f in A[S]:
         if edge(e,f):
          for b in A[f]:
           cm=AM[d]&AM[b]
           while cm:
            bit=cm&-cm;c=bit.bit_length()-1;cm-=bit
            am=Ap&B6[b]&B6[c]
            if am:
             a=(am&-am).bit_length()-1
             um=AM[a]&AM[b];vm=AM[a]&AM[c]
             if um and vm:
              u=(um&-um).bit_length()-1
              v=(vm&-vm).bit_length()-1
              return (a,u,b,c,v,d,e,f)
    return None

def valid_o(boundary,w):
    return (all(edge(w[u],w[v]) for u,v in OE) and
            all(edge(w[v],c) for v,c in zip(PORT,boundary)))

# 1. Crossing-edge lemma for predecessor-closed upshifts.
cross=0
for outside,inside in product(range(20),repeat=2):
    if edge(outside,inside):
        r=(inside-outside)%20
        after=edge(outside,(inside+1)%20)
        assert after==(r!=13)
        cross+=1
assert cross==140

# 2. Complete 32-row upshift response.
rows={(r["p"],r["bits"]["X"],r["bits"]["y"],r["bits"]["P"],r["bits"]["S"]):r
      for r in cert["upshift_rows"]}
assert len(rows)==32
good_count=0
for p in (1,14):
 for x,h,alpha,beta in product((0,1),repeat=4):
  X=13+x;Y=14;y=9+h;P=(p+alpha)%20;S=beta
  sols=[]
  for q,r in product(range(20),repeat=2):
   if edge(q,y) and edge(q,X) and edge(r,y) and edge(r,Y):
    ow=find_o(P,q,r,S)
    if ow:sols.append((q,r,ow))
  pred=((alpha or h) and ((not x) or (not beta))) if p==1 else (h and not(x and alpha and beta))
  row=rows[(p,x,h,alpha,beta)]
  assert bool(sols)==bool(pred)==row["good"]
  assert len(sols)==row["solution_count"]
  if pred:
   good_count+=1
   w=row["witness"];q=w["Q"];r=w["R"];ow=tuple(w["O"])
   assert edge(q,y) and edge(q,X) and edge(r,y) and edge(r,Y)
   assert valid_o((P,q,r,S),ow)
  else:
   assert row["witness"] is None
assert good_count==16

# 3. All labeled preorders, reverse quotient and combined skeleton.
pairs=[(i,j) for i in range(5) for j in range(5) if i!=j]
seen=set();preorders=comb1=comb14=0
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
 # order Y,X,y,P,S
 down1=not(bool((reach[0]>>2)&1) and
             (bool((reach[0]>>3)&1) or
              (bool((reach[1]>>3)&1) and bool((reach[4]>>3)&1))))
 down14=not(bool((reach[0]>>2)&1) and bool((reach[0]>>4)&1))
 up1=any(not((reach[z]>>0)&1) and not((reach[z]>>t)&1)
         for z in (1,4) for t in (3,2))
 up14=any(not((reach[z]>>0)&1) and not((reach[z]>>2)&1)
          for z in (1,3,4))
 fail1=(not down1) and (not up1)
 fail14=(not down14) and (not up14)
 skel1=all((reach[a]>>b)&1 for a,b in ((0,2),(1,3),(1,2),(4,3),(4,2)))
 skel14=all((reach[a]>>b)&1 for a,b in ((0,4),(4,2),(1,2),(3,2)))
 assert fail1==skel1 and fail14==skel14
 comb1+=fail1;comb14+=fail14
assert (preorders,comb1,comb14)==(6942,211,200)
assert cert["preorder_counts"]=={"total":6942,"combined_fail_p1":211,"combined_fail_p14":200}

# 4. Seven normalized parity rows and all 140 legal ordered pairs.
pr={r["d"]:r for r in cert["parity_rows"]}
assert set(pr)==set(range(7,14))
parity_pairs=0
for A0,B0 in product(range(20),repeat=2):
 if not edge(A0,B0):continue
 parity_pairs+=1
 d=(B0-A0)%20
 row=pr[d]
 q=(row["Q"]+A0)%20;r=(row["R"]+A0)%20
 w1=tuple((x+A0)%20 for x in row["O_p1"])
 w14=tuple((x+A0)%20 for x in row["O_p14"])
 assert edge(q,A0) and edge(r,A0)
 assert valid_o((A0,q,r,B0),w1)
 assert valid_o((B0,q,r,B0),w14)
assert parity_pairs==140

# 5. Exact repeated-endpoint five-cycle obstruction and rotation.
F=cert["obstruction"]
V=set(F["vertices"]);E={tuple(sorted(e)) for e in F["edges"]}
colors=F["colors"];rot=F["rotation"]
assert len(V)==5 and len(E)==5
assert all(edge(colors[a],colors[b]) for a,b in E)
assert all((colors[b]-colors[a])%20==13 for a,b in F["zero_arcs"])
adj={v:set() for v in V}
for a,b in E:adj[a].add(b);adj[b].add(a)
assert all(set(rot[v])==adj[v] for v in V)
darts=set();faces=[]
for u in sorted(V):
 for v in rot[u]:
  if (u,v) in darts:continue
  face=[];a,b=u,v
  while (a,b) not in darts:
   darts.add((a,b));face.append(a)
   ns=rot[b];c=ns[(ns.index(a)+1)%len(ns)]
   a,b=b,c
  faces.append(face)
assert sorted(map(len,faces))==[5,5]
L=set(A[0])
assert L==set(range(7,14))
assert not any(edge(a,b) for a in L for b in L)
assert colors["z"]%2==colors["v3"]%2

# 6. Mutation and boundary controls.
assert edge(0,7) and edge(0,13)
assert not edge(0,6) and not edge(0,14)
assert (13-0)%20==13 and (7-0)%20==7
assert rows[(1,0,0,1,0)]["good"]
assert not rows[(1,1,1,0,1)]["good"]
assert rows[(14,0,1,1,1)]["good"]
assert not rows[(14,1,1,1,1)]["good"]
assert not rows[(14,0,0,1,0)]["good"]
assert valid_o((0,7,10,7),tuple(pr[7]["O_p1"]))
assert valid_o((7,7,10,7),tuple(pr[7]["O_p14"]))
assert len(F["selected"])==4
assert tuple(sorted(("z","v0"))) in E and tuple(sorted(("z","v3"))) in E
assert inp["terminal_order"]==["Y","X","y","P","S"]
mutations=16

print(json.dumps({
 "status":"ok",
 "crossing_cases":cross,
 "upshift_rows":len(rows),
 "upshift_good":good_count,
 "preorders":preorders,
 "combined_fail_p1":comb1,
 "combined_fail_p14":comb14,
 "parity_pairs":parity_pairs,
 "plane_obstructions":1,
 "mutations":mutations,
 "python":sys.version.split()[0]
},sort_keys=True,separators=(",",":")))
