"""Reconstruct the missing historical positive screen, not a new search family."""
import hashlib,itertools as it,json
from pathlib import Path
ADJ=tuple(tuple(y for y in range(20) if 7<=abs(x-y)<=13) for x in range(20))
def edges(paths):return sorted({tuple(sorted((a,b))) for path in paths for a,b in zip(path,path[1:])})
def graphs():
 for n in range(4,8):
  cyc=[str(i) for i in range(n)]
  for pos in it.combinations(range(1,n),3):
   ps={str(i):c for i,c in zip((0,)+pos,('p','s','r','q'))};paths=[cyc+[cyc[0]]]
   yield {'paths':paths,'ports':ps,'edges':edges(paths)}
 for lengths in ((1,3,3),(1,3,4),(2,2,4),(2,3,3)):
  nxt=2;paths=[]
  for length in lengths:
   paths.append(['0']+[str(i) for i in range(nxt,nxt+length-1)]+['1']);nxt+=length-1
  for inner in range(3):
   outer=[p for i,p in enumerate(paths) if i!=inner];order=outer[0]+outer[1][-2:0:-1];available=[v for v in order if v not in ('0','1')]
   for sel in it.combinations(available,4):
    cyc=[v for v in order if v in sel]
    for sh in range(4):
     yield {'paths':paths,'ports':{cyc[(sh+i)%4]:c for i,c in enumerate(('p','s','r','q'))},'edges':edges(paths)}
def witness(g,b):
 ee=g['edges'];vs=sorted({v for e in ee for v in e});nb={v:set() for v in vs}
 for a,c in ee:nb[a].add(c);nb[c].add(a)
 dd={v:set(ADJ[b[g['ports'][v]]]) if v in g['ports'] else set(range(20)) for v in vs};chosen={};nodes=0
 def rec(todo,d):
  nonlocal nodes
  nodes+=1
  if nodes>100000:raise RuntimeError('node cap')
  if not todo:return dict(chosen)
  v=min(todo,key=lambda z:(len(d[z]),-len(nb[z]),z));rest=todo-{v}
  for c in sorted(d[v]):
   nd=dict(d)
   for w in nb[v]&rest:
    nd[w]=d[w]&set(ADJ[c])
    if not nd[w]:break
   else:
    chosen[v]=c;r=rec(rest,nd)
    if r is not None:return r
  chosen.pop(v,None);return None
 return rec(set(vs),dd)
def tag(p,r,h):
 if (h==0 and r in (19,0,1)) or (1<=h<=7 and 0<=r<=h) or (8<=h<=10 and r in (0,h)):return 'basic'
 if h==0 and r==2 and p in (14,15,16,17,18,19,0,1):return 'K1'
 if h==0 and r==18 and p in (19,0,1,2,3,4,5,6):return 'K2'
 if h==1 and r==19 and p in range(8):return 'K3'
 if h==1 and r==2 and p in (14,15,16,17,18,19,0,1):return 'K4'
 return None
bad=[(p,r,h,tag(p,r,h)) for h in range(11) for r in range(20) for p in range(20) if tag(p,r,h)]
rows=[]
for i,g in enumerate(graphs()):
 ws=[];vs=sorted({v for e in g['edges'] for v in e})
 for label in ('K1','K2','K3','K4'):
  for p,r,h,t in bad:
   if t!=label:continue
   b={'p':p,'q':0,'r':r,'s':h};w=witness(g,b)
   if w is not None:ws.append([label,p,r,h,[w[v] for v in vs]]);break
 if len(ws)==4:reason='each_residual_class_survives'
 else:
  for p,r,h,t in bad:
   if t!='basic':continue
   b={'p':p,'q':0,'r':r,'s':h};w=witness(g,b)
   if w is not None:ws=[['basic',p,r,h,[w[v] for v in vs]]];break
  else:raise AssertionError('missing historical witness')
  reason='admits_a_basic_bad_state'
 for label,p,r,h,colors in ws:
  w=dict(zip(vs,colors));b={'p':p,'q':0,'r':r,'s':h}
  assert all(7<=(w[v]-w[u])%20<=13 for u,v in g['edges'])
  assert all(7<=(w[v]-b[t])%20<=13 for v,t in g['ports'].items())
 rows.append([i,reason,ws])
assert len(rows)==71
out={'verdict':'candidate_only','decoding':'Rows [index,reason,witnesses]; graph=index in engine.small_replacements(); witness=[class,p,r,h,colors in sorted internal vertex order], q=0.','not_an_exhaustive_graph_classification':True,'graphs':rows}
raw=(json.dumps(out,separators=(',',':'))+'\n').encode()
sha=hashlib.sha256(raw).hexdigest();assert sha=='c2188eca1d7d617eae62196d536e8187e945d15c56e173ce9130bf7bb1949d92'
Path('replacement-screen.json').write_bytes(raw)
print(json.dumps({'verdict':'candidate_only','bytes':len(raw),'sha256':sha,'graphs':len(rows)}))
