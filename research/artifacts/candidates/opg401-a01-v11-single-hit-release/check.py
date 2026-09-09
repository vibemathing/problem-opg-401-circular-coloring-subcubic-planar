from itertools import product
P=range(20)
def edge(a,b): return 7 <= abs(a-b) <= 13
cross=[]
for a in P:
  for b in P:
    if edge(a,b):
      legal=edge((a-1)%20,b)
      r=(b-a)%20
      cross.append((r,legal))
assert all(legal==(r!=13) for r,legal in cross)
for X in (12,13):
  assert edge(2,9) and edge(2,X) and edge(19,9) and edge(19,12)
  assert edge(0,9) and edge(0,X) and edge(2,9) and edge(2,12)
OE=((0,1),(1,2),(2,3),(3,4),(4,0),(3,5),(5,6),(6,7),(7,2))
PORT=(0,5,6,7)
rows=[
 ((0,2,19,0),(7,14,1,8,0,15,6,13)),
 ((13,2,19,0),(1,8,0,7,14,14,6,13)),
 ((1,0,2,19),(14,1,13,0,7,7,14,6)),
 ((14,0,2,19),(7,0,13,1,14,8,15,6)),
 ((1,2,19,0),(14,7,0,8,1,15,6,13)),
 ((14,2,19,0),(1,8,0,7,14,14,6,13)),
]
for bd,w in rows:
  assert all(edge(w[u],w[v]) for u,v in OE)
  assert all(edge(w[v],c) for v,c in zip(PORT,bd))
def first_len(target):
  for L in range(1,21):
    if (13+13*L)%20==target: return L
assert first_len(1)==16
assert first_len(14)==17
assert first_len(0)==19
print({"crossing_cases":len(cross),"O_rows":len(rows),"path_lengths":{"P1":16,"P14":17,"S":19},"status":"ok"})
