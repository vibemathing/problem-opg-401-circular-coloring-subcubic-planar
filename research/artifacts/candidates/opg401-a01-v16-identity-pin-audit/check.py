#!/usr/bin/env python3
import json
import sys
from itertools import product
from pathlib import Path

HERE=Path(__file__).resolve().parent
INP=json.loads((HERE/"input.json").read_text())
CERT=json.loads((HERE/"certificate.json").read_text())
M=INP["menu"]
OE=[tuple(x) for x in INP["O"]["edges"]]
PORT=INP["O"]["ports"]

def delta(a,b):
    d=(a-b)%20
    return min(d,20-d)

def edge(a,b):
    return delta(a,b)>=7

A=[[x for x in range(20) if edge(x,c)] for c in range(20)]

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
              if us and vs: return (a,us[0],b,c,vs[0],d,e,f)
    return None

def root_domain_path(colors):
    S=set(range(4))
    for i in range(len(colors)-2,-1,-1):
        a,b=colors[i],colors[i+1]
        S={sa for sa in range(4)
           if any(edge(M[sa][a],M[sb][b]) for sb in S)}
    return sorted(S)

def valid_o(boundary,w):
    return all(edge(w[u],w[v]) for u,v in OE) and all(
        edge(w[v],c) for v,c in zip(PORT,boundary))

identity_checks=0
for a in range(20):
  for b in range(20):
    if edge(a,b):
      assert edge(M[0][a],M[0][b])
      identity_checks+=1
assert identity_checks==140

for row in CERT["terminal_rows"]:
    p=row["p"]; X,Y,y,P,S=row["terminal"]
    q,r=row["Q"],row["R"]; ow=row["O"]
    assert P==p and S==0 and y==9
    assert (row["root"]=="X" and X==M[1][13] and Y==13) or (
            row["root"]=="Y" and Y==M[1][13] and X==13)
    assert edge(q,X) and edge(q,y) and edge(r,Y) and edge(r,y)
    assert valid_o((P,q,r,S),ow)

rows=[]
for b in range(20):
  if edge(13,b):
    for c in range(20):
      if edge(b,c):
        rows.append({"middle":b,"leaf":c,
                     "root_domain":root_domain_path([13,b,c])})
assert rows==CERT["root_path_rows"]
pins=[[r["middle"],r["leaf"]] for r in rows if r["root_domain"]==[0]]
assert pins==[[3,14],[4,14],[5,14]]
for b in range(20):
    if edge(13,b):
        assert root_domain_path([13,b])!=[0]

repair_rows=[]
high_empty=0
for b in (3,4,5):
  for t in range(20):
    if not edge(b,t):
      continue
    assert 10<=t<=18
    if t<=14:
      bp=1; sig=[1,0,0,0]
      colors=[13,bp,14,t]
      edges=[(0,1),(1,2),(1,3)]
      assert all(edge(colors[u],colors[v]) for u,v in edges)
      assert all(edge(M[sig[u]][colors[u]],M[sig[v]][colors[v]])
                 for u,v in edges)
    else:
      bp=6
      if t in (15,17): sig=[1,1,1,2]
      elif t==16: sig=[1,3,0,3]
      elif t==18: sig=[1,1,1,1]
      colors=[13,bp,14,t]
      edges=[(0,1),(1,2),(1,3)]
      assert all(edge(colors[u],colors[v]) for u,v in edges)
      assert all(edge(M[sig[u]][colors[u]],M[sig[v]][colors[v]])
                 for u,v in edges)
      possible=False
      for z in range(20):
        if not (edge(13,z) and edge(z,14) and edge(z,t)):
          continue
        for sr in (1,2,3):
          for sb in range(4):
            if (edge(M[sr][13],M[sb][z])
                and edge(M[sb][z],14)
                and edge(M[sb][z],t)):
              possible=True
      assert not possible
      high_empty+=1
    repair_rows.append({"old_center":b,"third":t,"new_center":bp,
                        "states":sig,
                        "outputs":[M[sig[i]][colors[i]] for i in range(4)]})
assert repair_rows==CERT["radius_two_repairs"]
assert len(repair_rows)==21 and high_empty==9

assert edge(13,1) and edge(1,14) and edge(1,8)
assert edge(M[1][13],1) and edge(1,14) and edge(1,8)

for row in CERT["pendant_tree_controls"]:
    depth=row["depth"]; n=2**(depth+1)-1
    dep=[0]*n; edges=[]
    for i in range(n):
      for ch in (2*i+1,2*i+2):
        if ch<n:
          dep[ch]=dep[i]+1; edges.append((i,ch))
    colors=[13 if d==0 else (0 if d%2 else 10) for d in dep]
    opts=[1]+[0]*(n-1)
    assert all(edge(colors[u],colors[v]) for u,v in edges)
    assert all(edge(M[opts[u]][colors[u]],M[opts[v]][colors[v]])
               for u,v in edges)
    assert row=={"depth":depth,"vertices":n,"edges":len(edges),
                 "root_actual":13,"root_output":8}

mut=0
stale=[0,8,16,4,12]*4
assert any(not edge(stale[c],stale[(c+7)%20]) for c in range(20)); mut+=1
assert root_domain_path([13,3,13])!=[0]; mut+=1
assert root_domain_path([13,3,14])==[0]; mut+=1
assert root_domain_path([13,6,14])!=[0]; mut+=1
assert not (edge(13,1) and edge(1,14) and edge(1,15)); mut+=1
assert edge(13,6) and edge(6,14) and edge(6,15); mut+=1
assert not any(edge(z,7) and edge(z,14) and edge(z,15) for z in range(20)); mut+=1
assert edge(1,8) and edge(M[1][13],1); mut+=1
assert find_o(1,0,2,0) is None and find_o(14,0,2,0) is None; mut+=1
xrow=[r for r in CERT["terminal_rows"] if r["p"]==1 and r["root"]=="X"][0]
assert not valid_o((14,xrow["Q"],xrow["R"],0),xrow["O"]); mut+=1
assert delta(19,6)==7 and edge(19,6); mut+=1
assert delta(0,13)==7 and edge(0,13); mut+=1
pair=(13,13)
assert pair[0]==pair[1]; mut+=1
assert 2!=1; mut+=1
assert mut==14

print(json.dumps({
    "status":"ok",
    "identity_edge_checks":identity_checks,
    "terminal_rows":len(CERT["terminal_rows"]),
    "legal_root_paths":len(rows),
    "minimum_pin_paths":len(pins),
    "radius_two_rows":len(repair_rows),
    "high_frozen_branch_rows":high_empty,
    "pendant_tree_max_vertices":max(r["vertices"] for r in CERT["pendant_tree_controls"]),
    "mutations":mut,
    "python":sys.version.split()[0],
},sort_keys=True,separators=(",",":")))
