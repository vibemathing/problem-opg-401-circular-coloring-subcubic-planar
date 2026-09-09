#!/usr/bin/env python3
import json,sys
from itertools import product
from pathlib import Path
H=Path(__file__).resolve().parent
I=json.loads((H/'input.json').read_text())
def delta(a,b):
 d=(a-b)%20
 return min(d,20-d)
def edge(a,b):return delta(a,b)>=7
OE=[(0,1),(1,2),(2,3),(3,4),(4,0),(3,5),(5,6),(6,7),(7,2)]
PORT=[0,5,6,7]
def valid(boundary,w):
 return all(edge(w[a],w[b]) for a,b in OE) and all(edge(w[v],c) for v,c in zip(PORT,boundary))
C=[0,8,16,4,12]
T8=[C[(2*c)%5] for c in range(20)]
T9=[7*(c%2) for c in range(20)]
T10=[0,7,14,0,7,0,1,7,0,3,7,0,7,8,0,7,10,0,7,14]
maps={8:(T8,{7,8}),9:(T9,{7,9}),10:(T10,{7,10})}
checks=0
for name,(T,classes) in maps.items():
 assert len(T)==20
 for c in range(20):
  for d in classes:
   for s in (-1,1):
    assert edge(T[c],T[(c+s*d)%20])
    checks+=1
for s in (-8,-7,7,8):assert (2*s)%5 in (1,4)
assert all(d%2 for d in (7,9,11,13))
tab=[]
for c in range(20):tab.append([c,T10[c],T10[(c+7)%20],delta(T10[c],T10[(c+7)%20]),T10[(c+10)%20],delta(T10[c],T10[(c+10)%20])])
assert tab==I['T10_table']
rows=I['terminal_rows'];assert len(rows)==6
translations=reflections=0
for r in rows:
 T=maps[r['map']][0];p=r['p'];P=T[p];S=T[0];X=T[13];Y=X;y=T[9];q=r['Q'];rr=r['R'];w=r['O']
 assert edge(q,X) and edge(q,y) and edge(rr,Y) and edge(rr,y)
 assert r['boundary']==[P,q,rr,S] and valid(r['boundary'],w)
 for t in range(20):
  b=[(x+t)%20 for x in r['boundary']];ww=[(x+t)%20 for x in w];assert valid(b,ww);translations+=1
  b=[(-x+t)%20 for x in r['boundary']];ww=[(-x+t)%20 for x in w];assert valid(b,ww);reflections+=1
neg=[(8,0,9),(8,0,10),(9,0,8),(9,0,10),(10,0,8),(10,0,9)]
for m,c,d in neg:
 T=maps[m][0];assert edge(c,(c+d)%20) and not edge(T[c],T[(c+d)%20])
subsets=covered=0
for mask in range(16):
 D={7+i for i in range(4) if (mask>>i)&1};subsets+=1
 ok=any(D<=classes for _,classes in maps.values());covered+=ok
 assert ok==(len(D-{7})<=1)
print(json.dumps({'status':'ok','map_edge_checks':checks,'terminal_rows':len(rows),'translations':translations,'reflections':reflections,'class_subsets':subsets,'covered_subsets':covered,'negative_mutations':len(neg),'python':sys.version.split()[0]},sort_keys=True,separators=(',',':')))
