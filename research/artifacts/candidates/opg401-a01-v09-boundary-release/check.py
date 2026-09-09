"""Finite controls for actual-boundary release; no imports from old candidates."""
from collections import deque
from functools import lru_cache
from itertools import product
from pathlib import Path
import json

PALETTE=range(20)
OE=((0,1),(1,2),(2,3),(3,4),(4,0),(3,5),(5,6),(6,7),(7,2))
PI=(0,5,6,7)
def edge(a,b): return 7 <= (b-a)%20 <= 13
def scalar(a,b): return 0<=a<20 and 0<=b<20 and 7<=abs(a-b)<=13
A=[{b for b in PALETTE if scalar(a,b)} for a in PALETTE]
def valid(ee,f): return all(scalar(f[u],f[v]) for u,v in ee)
def adj(n,ee):
 out=[set() for _ in range(n)]
 for u,v in ee:
  assert 0<=u<v<n;out[u].add(v);out[v].add(u)
 return out

@lru_cache(None)
def ofill(beta):
 nb=adj(8,sorted(tuple(sorted(e)) for e in OE));dd=[set(PALETTE) for _ in range(8)]
 for u,c in zip(PI,beta):dd[u]&=A[c]
 vals={};nodes=0
 def dfs(left,ds):
  nonlocal nodes
  nodes+=1
  if nodes>100000: raise RuntimeError('literal O search budget, not a negative result')
  if not left:return tuple(vals[i] for i in range(8))
  u=min(left,key=lambda v:(len(ds[v]),-len(nb[v]),v));rest=left-{u}
  for c in sorted(ds[u]):
   nd=ds.copy()
   for v in nb[u]&rest:nd[v]=ds[v]&A[c]
   if all(nd[v] for v in nb[u]&rest):
    vals[u]=c;w=dfs(rest,nd)
    if w is not None:return w
  return None
 return dfs(set(range(8)),dd)

def weights(n,ee,f):
 out=[[] for _ in range(n)]
 for u,v in ee:
  r=(f[v]-f[u])%20;assert 7<=r<=13
  out[u].append((v,13-r));out[v].append((u,r-7))
 return [sorted(row) for row in out]

def slack(n,ee,f,lo,hi):
 assert valid(ee,f) and all(0<=lo[v]<=hi[v]<=6 for v in range(n))
 wa=weights(n,ee,f);d=lo.copy();paths=[[v] for v in range(n)];q=deque(range(n));updates=0
 while q:
  u=q.popleft()
  for v,w in wa[u]:
   x=d[u]-w
   if x>d[v]:
    d[v]=x;paths[v]=paths[u]+[v];updates+=1
    assert len(paths[v])==len(set(paths[v])) and updates<=6*n
    if d[v]>hi[v]:return {'possible':False,'path':paths[v],'updates':updates}
    q.append(v)
 return {'possible':True,'d':d,'updates':updates}

def verify_slack_failure(ee,f,lo,hi,path):
 if not path or len(path)!=len(set(path)):return False
 es={tuple(e) for e in ee};total=0
 for u,v in zip(path,path[1:]):
  if tuple(sorted((u,v))) not in es:return False
  total+=13-((f[v]-f[u])%20)
 return lo[path[0]]-total>hi[path[-1]]

def brute(n,ee,f,lo,hi):
 sols=[]
 for d in product(*(range(lo[v],hi[v]+1) for v in range(n))):
  g=[(f[v]-d[v])%20 for v in range(n)]
  if valid(ee,g):sols.append(d)
 return sols

def faces(rot):
 darts={(u,v) for u,row in enumerate(rot) for v in row};seen=set();out=[]
 assert len(darts)==sum(map(len,rot)) and all((v,u) in darts for u,v in darts)
 for start in sorted(darts):
  if start in seen:continue
  u,v=start;walk=[]
  while (u,v) not in seen:
   seen.add((u,v));walk.append(u);rr=rot[v];u,v=v,rr[(rr.index(u)+1)%len(rr)]
  assert (u,v)==start;out.append(walk)
 return out

def structural(n,ee,rot):
 assert len(ee)==len({tuple(e) for e in ee}) and ee==sorted(ee)
 nb=adj(n,ee);assert all(len(x)<=3 for x in nb)
 assert all(not nb[u]&nb[v] for u,v in ee)
 assert [set(row) for row in rot]==nb
 reached={0};stack=[0]
 while stack:
  for v in nb[stack.pop()]-reached:reached.add(v);stack.append(v)
 assert len(reached)==n
 ff=faces(rot);assert n-len(ee)+len(ff)==2
 return ff

def coupled_response(a1,a2,p):
 # Exhaust complete U states, by literal edges and interval lists, not the claimed response.
 counts=[0,0];witness=None
 for w0 in sorted(A[3]):
  for w1 in sorted(A[a1]&A[w0]):
   for w2 in sorted(A[a2]&A[9]&A[w1]):
    for y in sorted(A[w0]):
     qr=sorted(A[13]&A[y])
     for q,r in product(qr,repeat=2):
      counts[0]+=1;inside=ofill((p,q,r,0))
      if inside is not None:
       counts[1]+=1;witness={'U':[q,r,y,w0,w1,w2],'O':inside}
 return {'legal_U_states':counts[0],'fillable_U_states':counts[1],'witness':witness}

def cut_record(case,W):
 n=len(case['colors']);Z=set(W)|set(range(n,n+8));full=case['full_edges']
 cut=[e for e in full if (e[0] in Z)!=(e[1] in Z)]
 endpoints=[e[1] if e[0] in Z else e[0] for e in cut]
 k=len(set(W)&set(case['ports']));c=sum(u in W and v in W for u,v in case['edges'])-len(W)+1
 nb=adj(n+8,full);d=sum(3-len(nb[v]) for v in W)
 assert len(cut)==len(W)+6-2*k-2*c-d
 return {'W':sorted(W),'n':len(W),'k':k,'c':c,'d':d,'b':len(cut),'edges':cut,
         'outside_endpoint_occurrences':endpoints,'distinct_outside_vertices':sorted(set(endpoints))}

def main():
 root=Path(__file__).resolve().parent;data=json.loads((root/'input.json').read_text())
 out={'verdict':'candidate_only','schema':'opg401-boundary-release-v1','scope':'finite controls, not a minimum-root-obstruction proof'}
 algebra=0
 for a,b in product(PALETTE,repeat=2):
  if not scalar(a,b):continue
  r=(b-a)%20
  for x,y in product(range(7),repeat=2):
   assert scalar((a-x)%20,(b-y)%20)==(x-y<=13-r and y-x<=r-7);algebra+=1
 intervals=[(a,b) for a in range(7) for b in range(a,7)];tests=0
 for r in range(7,14):
  ee=[(0,1)];f=[0,r];all_vectors=brute(2,ee,f,[0,0],[6,6])
  for (a,b),(c,d) in product(intervals,repeat=2):
   lo=[a,c];hi=[b,d];sols=[v for v in all_vectors if a<=v[0]<=b and c<=v[1]<=d]
   ans=slack(2,ee,f,lo,hi);assert ans['possible']==bool(sols)
   if sols:assert ans['d']==[min(v[i] for v in sols) for i in range(2)]
   else:assert verify_slack_failure(ee,f,lo,hi,ans['path'])
   tests+=1
 # All valid normalized old colors on a three-vertex path, several independent bounds.
 path_tests=0
 for a in range(7,14):
  for b in sorted(A[a]):
   f=[0,a,b];ee=[(0,1),(1,2)]
   for lo,hi in [([3,0,0],[6,6,0]),([0,2,1],[0,6,6]),([1,0,4],[3,6,4])]:
    sols=brute(3,ee,f,lo,hi);ans=slack(3,ee,f,lo,hi)
    assert ans['possible']==bool(sols)
    if sols:assert ans['d']==[min(v[i] for v in sols) for i in range(3)]
    else:assert verify_slack_failure(ee,f,lo,hi,ans['path'])
    path_tests+=1
 f=[0,7,0,13,6,13];ee=sorted([(0,1),(1,2),(2,3),(3,4),(4,5),(0,5),(0,3)])
 cyclic=[]
 for lo,hi in [([1,0,0,0,0,0],[6,6,6,0,6,6]),([3,0,0,0,0,0],[6,0,0,6,6,6])]:
  sols=brute(6,ee,f,lo,hi);ans=slack(6,ee,f,lo,hi);assert ans['possible']==bool(sols)
  if sols:assert ans['d']==[min(v[i] for v in sols) for i in range(6)]
  else:assert verify_slack_failure(ee,f,lo,hi,ans['path'])
  cyclic.append({'colors':f,'edges':ee,'lo':lo,'hi':hi,'result':ans})
 no_chord=slack(6,[e for e in ee if e!=(0,3)],f,[1,0,0,0,0,0],[6,6,6,0,6,6])
 assert no_chord['possible'] and not cyclic[0]['result']['possible'];out['chord_controls']=cyclic
 release_tests=0
 for s in range(2,7):
  choices=list(range(s-6,s+1))
  for degree in (0,1,2):
   for neigh in product(choices,repeat=degree):
    for c in PALETTE:
     actual=[(c+x)%20 for x in neigh]
     good=[(c+j)%20 for j in range(1,9) if all(scalar((c+j)%20,x) for x in actual)]
     assert bool(good)==all(x<=1 for x in neigh);release_tests+=1
 pairs=[(a,b) for a in range(13,20) for b in range(10,17) if scalar(a,b)]
 assert pairs==[(17,10),(18,10),(18,11),(19,10),(19,11),(19,12)]
 responses={}
 for p in (1,14):
  rows=[]
  for a,b in pairs:
   rr=coupled_response(a,b,p);rr['pair']=[a,b];rows.append(rr)
  assert [r['pair'] for r in rows if r['fillable_U_states']]==[[17,10]]
  assert next(r for r in rows if r['pair']==[17,10])['fillable_U_states']==1
  responses[str(p)]=rows
 out['response_tables']=responses
 outputs=[]
 for case in data['fixtures']:
  f=case['colors'];n=len(f);ee=case['edges'];rot=case['rotation'];p=case['p'];ports=case['ports']
  assert valid(ee,f) and [f[v] for v in ports]==[p,0,2,0]
  ff=structural(n,ee,rot);fff=structural(n+8,case['full_edges'],case['full_rotation'])
  # Every allowed single released vertex has real flexibility but no full response.
  assert valid(ee,f[:8]+[19]+f[9:])
  ff2=f.copy();ff2[9]=10;assert valid(ee,ff2)
  stages=[];cur=f.copy()
  for changes in ({9:10},{8:17},{5:17},{4:4},{0:5,1:6,2:18,3:11}):
   cur=cur.copy()
   for v,c in changes.items():cur[v]=c
   assert valid(ee,cur);stages.append(cur)
  support=set(range(6))|{8,9};fixed=sorted(set(range(n))-support)
  assert all(all(g[v]==f[v] for v in fixed) for g in stages)
  inside=ofill(tuple(cur[v] for v in ports));assert inside is not None
  gfull=cur+list(inside);assert valid(case['full_edges'],gfull)
  # Apply B1 with the literal chosen interior, every outside cut and repeated endpoint.
  Z=set(range(6))|set(range(n,n+8));K=sorted(set(range(n+8))-Z);idx={v:i for i,v in enumerate(K)}
  lower=[];upper=[]
  for v in K:
   cn=[u if w==v else w for u,w in case['full_edges'] if v in (u,w) and (u if w==v else w) in Z]
   ds=[d for d in range(7) if all(edge(gfull[u],(f[v]-d)%20) for u in cn)]
   if v in fixed:ds=[d for d in ds if d==0]
   assert ds and ds==list(range(min(ds),max(ds)+1));lower.append(min(ds));upper.append(max(ds))
  kee=sorted(tuple(sorted((idx[u],idx[v]))) for u,v in case['full_edges'] if u in idx and v in idx)
  kkf=[f[v] for v in K];ans=slack(len(K),kee,kkf,lower,upper)
  assert ans['possible'];new=[(kkf[i]-ans['d'][i])%20 for i in range(len(K))]
  assert {K[i]:ans['d'][i] for i in range(len(K)) if ans['d'][i]}=={8:1,9:1}
  assert new==[gfull[v] for v in K]
  stages_out={'fixed_vertices':fixed,'operations':[{9:10},{8:17},{5:17},{4:4},{0:5,1:6,2:18,3:11}],
              'stages':stages,'O_fill':inside,'full_final':gfull}
  outputs.append(dict(case,faces=ff,full_faces=fff,repair=stages_out,
    initial_cut=cut_record(case,set(range(6))),released_cut=cut_record(case,support),
    slack={'vertices':K,'lo':lower,'hi':upper,'result':ans}))
 out['fixtures']=outputs
 mutations=[]
 def detect(name,test):
  assert test,name;mutations.append(name)
 detect('exclude_7',scalar(0,7) and not 7<abs(0-7)<=13)
 detect('exclude_13',scalar(0,13) and not 7<=abs(0-13)<13)
 detect('reverse_zero_slack',13-((13-0)%20)==0 and ((13-0)%20)-7==6)
 detect('drop_induced_chord',no_chord['possible'] and not cyclic[0]['result']['possible'])
 detect('reverse_failure_path',not verify_slack_failure(ee=cyclic[0]['edges'],f=cyclic[0]['colors'],lo=cyclic[0]['lo'],hi=cyclic[0]['hi'],path=list(reversed(cyclic[0]['result']['path']))))
 detect('unjustified_large_displacement',scalar(0,(7-14)%20) and not 14<=0)
 q=outputs[0];g=q['repair']['full_final'];fe=q['full_edges'];bad=g.copy();bad[8]=16
 detect('omit_A1_A2',not valid(fe,bad) and valid([e for e in fe if e!=[8,9]],bad))
 bad=g.copy();bad[9]=9
 detect('omit_repeated_A0_incidence',not valid(fe,bad) and valid([e for e in fe if e!=[7,9]],bad))
 bad=g.copy();bad[7]=2
 detect('secretly_release_fixed_A0',valid(fe,bad) and bad[7]!=q['colors'][7])
 detect('independent_boundary_lists',[17,11] not in [r['pair'] for r in responses['1']])
 detect('one_boundary_not_joint',all(r['fillable_U_states']==0 for r in responses['1'] if r['pair'][0]==18 or r['pair'][1]==11))
 detect('count_incidence_as_variable',q['released_cut']['b']==8 and len(q['released_cut']['distinct_outside_vertices'])==6)
 detect('use_four_port_formula',q['initial_cut']['n']-2!=q['initial_cut']['b'])
 detect('drop_cycle_excess',q['released_cut']['n']+6-2*q['released_cut']['k']!=q['released_cut']['b'])
 bad=q['colors'].copy();bad[0]=5
 detect('assume_atomic_assignments_are_sequential',not valid(q['edges'],bad))
 detect('reuse_wrong_p_fill',not scalar(14,q['repair']['O_fill'][0]))
 out['mutations']=mutations
 out['counts']={'edge_displacement_controls':algebra,'two_vertex_all_interval_cases':tests,
                'three_vertex_cases':path_tests,'cycle_chord_cases':2,'terminal_release_cases':release_tests,
                'boundary_pairs_per_p':len(pairs),'full_plane_fixtures':len(outputs),'mutations':len(mutations)}
 (root/'certificate.json').write_text(json.dumps(out,separators=(',',':'),sort_keys=True)+'\n')
 print(json.dumps(out['counts'],sort_keys=True))
if __name__=='__main__':main()
