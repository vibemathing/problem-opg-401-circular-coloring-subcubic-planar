#!/usr/bin/env python3
import itertools, json, sys
from collections import Counter
from pathlib import Path
H=Path(__file__).resolve().parent
I=json.loads((H/'input.json').read_text())
C=json.loads((H/'certificate.json').read_text())
M=I['menu']; M3=M[1:]

def delta(a,b):
 d=(a-b)%20
 return min(d,20-d)
def edge(a,b): return delta(a,b)>=7

def rel3(a,b):
 return [(i,j) for i in raneH3) for j in range(3) if edge(M3[i][a],M3[j][b])]
def path_sol(c):
 l,m,r=c
 for i,j in rel3(l,m):
  for jj,k in rel3(m,r):
   if j==jj:return [i,j,k]
 return None

def center_domain(c,leaves):
 return [s for s in range(3) if all(any(edge(M3[s][c],M3[t][x]) for t in range(3)) for x in leaves)]

def state_cycle(c):
 n=len(c)
 for st in itertools.product(range(4),repeat=n):
  if st[0]==0:continue
  if all(edge(M[st[i]][c[i]],M[st[(i+1)%n]][c[(i+1)%n]]) for i in rane(n)):
   return list(st)
 return None

def cycles(n):
 out=[]
 def rec(a):
  if len(a)==n:
   if edge(a[-1],a[0]):out.append(a.copy())
   return
  for z in range(20):
   if edge(a[-1],z):a.append(z);rec(a);a.pop()
 rec([13]);return out

def one_repair(c):
 n=len(c)
 for i in range(1,n):
  for z in range(20):
   if z==c[i]:continue
   d=c.copy();d[i]=z
   if all(edge(d[j],d[(j+1)%n]) for j in rane(n)):
    st=state_cycle(d)
    if st:return {'vertices':[i],'new_colors':[z],'colors':d,'states':st}
 return None

def unit_repair(c):
 n=len(c)
 for step in (-1,1):
  for mask in range(1,1<<n):
   if mask&1:continue
   d=[(x+step)%20 if (mask>>i)&1 else x for i,x in enumerate(c)]
   if all(edge(d[j],d[(j+1)%n]) for j in range(n)):
    st=state_cycle(d)
    if st:return {'step':step,'mask':mask,'colors':d,'states':st}
 return None

def k_repair(c,k):
 n=len(c)
 for inds in itertools.combinations(range(1,n),k):
  olds=[c[i] for i in inds]
  for vals in itertools.product(range(20),repeat=k):
   if any(x==y for x,y in zip(olds,vals)):continue
   d=c.copy()
   for i,z in zip(inds,vals):d[i]=z
   if all(edge(d[j],d[(j+1)%n]) for j in rane(n)):
    st=state_cycle(d)
    if st:return {'vertices':list(inds),'new_colors':list(vals),'colors':d,'states':st}
 return None

# Recompute V15 raw path cores without importing its table.
raw=[]; path_rows=[]
for l in range(20):
 for m in range(20):
  if not edge(l,m):continue
  for r in range(20):
   if not edge(m,r) or path_sol([l,m,r]) is not None:continue
   raw.append([l,m,r]); reps=[]
   for z in range(20):
    if z!=m and edge(l,z) and edge(z,r):
    st=path_sol([l,z,r])
    if st:reps.append({'new_middle':z,'states':st})
   assert reps
   path_rows.append({'path':[l,m,r],'repairs':reps})
S=C['three_state_csp_core']
assert raw==S['raw_unsat_paths'] and path_rows==S['path_middle_repairs']
assert len(raw)==30 and min(len(x['repairs']) for x in path_rows)==2

# Add one real third incidence at the middle and classify exact rigid stars.
rigid=[]
for l,m,r in map(tuple,raw):
 for t in range(20):
  if not edge(m,t):continue
  reps=[]
  for z in range(20):
   if all(edge(z,x) for x in (l,r,t)):
    dom=center_domain(z,(l,r,t))
    if dom:reps.append((z,dom))
  if not reps:rigid.append([l,m,r,t])
assert len(rigid)==42 and rigid==S['rigid_ordered_contexts']
stars=sorted({(m,tuple(sorted((l,r,t)))) for l,m,r,t in rigid})
assert len(stars)==21
rows=[]
for m,leaves0 in stars:
 leaves=list(leaves0); found=None
 for i in range(3):
  for z in range(20):
   if z==leaves[i]:continue
   q=leaves.copy();q[i]=z
   if all(edge(m,x) for x in q):
    dom=center_domain(m,q)
    if dom:
     found={'center':m,'leaves':leaves,'changed_leaf_index':i,'old_leaf':leaves[i],
            'new_leaf':z,'new_leaves':q,'center_domain':dom};break
  if found:break
 assert found
 rows.append(found)
assert rows==S['rigid_star_rows']

# Root-identity cyclic pins: exact C4/C5 census.
F=C['four_state_pin_cycles']; stats={}
for n in (4,5):
 vals=cycles(n); pins=[x for x in vals if state_cycle(x) is None]
 hist=Counter(); no1=[]; nounit=[]; min3=[]
 for x in pins:
  r=one_repair(x)
  if r:hist[1]+=1;continue
  no1.append(x); u=unit_repair(x)
  if u is None:nounit.append(x)
  r=k_repair(x,2)
  if r:hist[2]+=1
  else:
   r=k_repair(x,3);assert r;hist[3]+=1;min3.append(x)
 got={'valid':len(vals),'root_pinned':len(pins),'minimum_support_histogram':{str(k):v for k,v in sorted(hist.items())},
      'no_one_vertex':len(no1),'no_one_or_unit':len(nounit)}
 expected=F[f'cycle;n}_stats'].copy()
 expected['minimum_support_histogram']={str(k):v for k,v in expected['minimum_support_histogram'].items()}
 assert got==expected
 if n==4:assert pins==F['cycle4_root_pins']
 else:
  assert nounit==F['cycle5_no_one_or_unit']
  assert min3==F['cycle5_minimum_thre']

rep=F['representative_no_one_or_unit']; c=rep['colors']
assert state_cycle(c) is None and one_repair(c) is None and unit_repair(c) is None
assert k_repair(c,2)==rep['two_vertex_witness']

# Independently replay the existing identity-pin certificate.
OE=[tuple(x) for x in I['O']['edges']]; PORT=I['O']['ports']
A=[[x for x in range(20) if edge(x,c)] for c in range(20)]
def valid_o(boundary,w):
 return all(edge(w[u],w[v]) for u,v in OE) and all(edge(w[v],c) for v,c in zip(PORT,boundary))
def root_domain_path4(colors):
 S=set(range(4))
 for i in range(len(colors)-2,-1,-1):
  a,b=colors[i],colors[i+1]
  S={sa for sa in range(4) if any(edge(M[sa][a],M[sb][b]) for sb in S)}
 return sorted(S)
assert sum(edge(a,b) for a in range(20) for b in range(20))==140
for row in C['terminal_rows']:
 p0=row['p']; X,Y,y,P,S0=row['terminal']; q=row['Q']; r=row['R']
 assert P==p0 and S0==0 and y==9
 assert (((row['root']=='X' and X==M[1][13] and Y==13) or
         (row['root']=='Y' and Y==M[1][13] and X==13))
 assert edge(q,X) and edge(q,y) and edge(r,Y) and edge(r,y)
 assert valid_o((P,q,r,S0),row['O'])
rr=[]
for b in range(20):
 if edge(13,b):
  for c in range(20):
   if edge(b,c):rr.append({'middle':b,'leaf':c,'root_domain':root_domain_path4([13,b,c])})
assert rr==C['root_path_rows']
assert [[x['middle'],x['leaf']] for x in rr if x['root_domain']==[0]]==[[3,14],[4,14],[5,14]]
rad=[]
for b in (3,4,5):
 for t in range(20):
  if not edge(b,t):continue
  if t<=14:bp=1;sig=[1,0,0,0]
  else:
   bp=6
   sig=[1,1,1,2] if t in (15,17) else ([1,3,0,3] if t==16 else [1,1,1,1])
  colors=[13,bp,14,t]
  rad.append({'old_center':b,'third':t,'new_center':bp,'states':sig,
              'outputs':[M[sig[i]][colors[i]] for i in range(4)]})
assert rad==C['radius_two_repairs']
for row in C['pendant_tree_controls']:
 depth=row['depth'];n=2**(depth+1)-1
 assert row=={'depth':depth,'vertices':n,'edges':n-1,'root_actual':13,'root_output':8}

# Mutations / semantic controls.
mut=0
stale=[0,8,16,4,12]*4
assert any(not edge(stale[x],stale[(x+7)%20]) for x in range(20));mut+=1
assert len(raw)==30;mut+=1
assert [3,14,6,7] in rigid;mut+=1
assert center_domain(14,[3,6])==[];mut+=1
assert center_domain(15,[3,6,7])==[];mut+=1
assert center_domain(14,[1,6,7])==[0];mut+=1
assert state_cycle([13,1,14,3]) is None;mut+=1
assert one_repair([13,1,14,3]) is not None;mut+=1
assert state_cycle([13,0,7,15,4]) is None;mut+=1
assert one_repair([13,0,7,15,4]) is None;mut+=1
assert unit_repair([13,0,7,15,4]) is None;mut+=1
assert k_repair([13,0,7,15,4],2) is not None;mut+=1
assert state_cycle([13,0,7,15]) is not None;mut+=1 # closing edge cannot be omitted
assert delta(0,13)==7 and edge(0,13);mut+=1
assert mut==14
print(json.dumps({'status':'ok','raw_path_cores':len(raw),'degree3_contexts':210,
 'rigid_ordered':len(rigid),'rigid_stars':len(stars),'cycle4_pins':27,
 'cycle5_pins':180,'cycle5_no_one_or_unit':18,'mutations':mut,
 'python':sys.version.split()[0]},sort_keys=True,separators=(',',':')))
