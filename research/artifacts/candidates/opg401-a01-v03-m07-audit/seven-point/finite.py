"""Exact finite positive-cover synthesis/checking; candidate generation, not admission."""
import collections as co
import itertools as it
import json
import sys
from functools import lru_cache
from pathlib import Path
A='0123456789abcdefghij'
ALL=(1<<20)-1
ADJ=tuple(sum(1<<y for y in range(20) if 7<=abs(x-y)<=13) for x in range(20))
BAD=[(0,0,0,0),(0,0,0,1),(0,0,0,2),(0,0,1,1),(0,0,2,1),(0,0,19,1),(1,0,2,0),(1,0,2,1),(7,0,19,1),(8,0,0,1),(14,0,2,0),(14,0,2,1)]
O=((0,1),(1,2),(2,3),(3,4),(4,0),(3,5),(5,6),(6,7),(7,2))

def normal(edges):return tuple(sorted(tuple(sorted(e)) for e in edges))
def neighbors(n,edges):
 nb=[set() for _ in range(n)]
 for u,v in edges:nb[u].add(v);nb[v].add(u)
 return nb

def permutations_by_degree(n,edges):
 groups=co.defaultdict(list)
 for v,row in enumerate(neighbors(n,edges)):groups[len(row)].append(v)
 blocks=[groups[d] for d in sorted(groups)]
 for images in it.product(*(it.permutations(b) for b in blocks)):
  yield tuple(sum(images,()))

def canonical(n,edges):
 best=None
 for order in permutations_by_degree(n,edges):
  inverse={v:i for i,v in enumerate(order)}
  image=normal((inverse[u],inverse[v]) for u,v in edges)
  if best is None or image<best:best=image
 return best

def automorphisms(n,edges):
 nb=neighbors(n,edges);source=tuple(sorted(range(n),key=lambda v:(len(nb[v]),v)))
 for dest in permutations_by_degree(n,edges):
  p=dict(zip(source,dest))
  if normal((p[u],p[v]) for u,v in edges)==edges:yield tuple(p[v] for v in range(n))

def generate_vertices():
 levels=[set() for _ in range(8)];levels[0].add(())
 for n in range(7):
  for e in levels[n]:
   nb=neighbors(n,e);room=[v for v in range(n) if len(nb[v])<3]
   for k in range(4):
    for sub in it.combinations(room,k):
     if any(v in nb[u] for u,v in it.combinations(sub,2)):continue
     levels[n+1].add(canonical(n+1,e+tuple((v,n) for v in sub)))
 return [(n,e) for n in range(8) for e in sorted(levels[n])]

def generate_edges():
 # Different coverage construction: add one permissible edge, not one vertex.
 out=[]
 for n in range(8):
  seen={()};todo=[()]
  while todo:
   e=todo.pop();nb=neighbors(n,e)
   for u,v in it.combinations(range(n),2):
    if v in nb[u] or len(nb[u])==3 or len(nb[v])==3 or nb[u]&nb[v]:continue
    new=canonical(n,e+((u,v),))
    if new not in seen:seen.add(new);todo.append(new)
  out.extend((n,e) for e in sorted(seen))
 return out

def ports(n,e):
 deg=[len(x) for x in neighbors(n,e)];au=list(automorphisms(n,e))
 for p in it.product(range(-1,n),repeat=4):
  if any(deg[v]+k>3 for v,k in co.Counter(v for v in p if v>=0).items()):continue
  if p==min(tuple(a[v] if v>=0 else -1 for v in p) for a in au):yield p

def old_family(n,e,p):
 if -1 in p or n<5:return False
 nb=neighbors(n,e);seen={0}
 while True:
  nxt=seen|set().union(*(nb[v] for v in seen))
  if nxt==seen:break
  seen=nxt
 if len(seen)!=n:return False
 P,D,E,F=p
 return len({D,E,F})==3 and E in nb[D] and E in nb[F] and any(U in nb[D] and V in nb[U] and F in nb[V] for U,V in it.permutations(set(range(n))-{D,E,F},2))

def solver(n,e):
 nb=neighbors(n,e)
 @lru_cache(maxsize=50000)
 def rec(dom):
  d=list(dom)
  if 0 in d:return None
  changed=True
  while changed:
   changed=False
   for v in range(n):
    if d[v]&(d[v]-1)==0:
     for w in nb[v]:
      dd=d[w]&ADJ[d[v].bit_length()-1]
      if not dd:return None
      if dd!=d[w]:d[w]=dd;changed=True
  un=[v for v in range(n) if d[v]&(d[v]-1)]
  if not un:return tuple(x.bit_length()-1 for x in d)
  v=min(un,key=lambda z:(d[z].bit_count(),-len(nb[z]),z));mask=d[v]
  while mask:
   b=mask&-mask;mask-=b;x=d.copy();x[v]=b;r=rec(tuple(x))
   if r is not None:return r
  return None
 def call(p,b):
  d=[ALL]*n
  for v,c in zip(p,b):
   if v>=0:d[v]&=ADJ[c]
  return rec(tuple(d))
 return call

def legal(n,e,p,b,w):
 return len(w)==n and all(type(c)==int and 0<=c<20 for c in w) and all(7<=(w[v]-w[u])%20<=13 for u,v in e) and all(v<0 or 7<=(w[v]-c)%20<=13 for v,c in zip(p,b))

def original_exists(b):
 # Separate literal-edge search with directed residues and no propagation cache.
 nb=neighbors(8,O);fixed=dict(zip((0,5,6,7),b));chosen={}
 def rec():
  if len(chosen)==8:return True
  ds={v:[x for x in range(20) if (v not in fixed or 7<=(x-fixed[v])%20<=13) and all(7<=(x-chosen[u])%20<=13 for u in nb[v] if u in chosen)] for v in range(8) if v not in chosen}
  v=min(ds,key=lambda v:(len(ds[v]),-len(nb[v]),v))
  for x in ds[v]:
   chosen[v]=x
   if rec():return True
  chosen.pop(v,None);return False
 return rec()

def encode(n,e,ws):
 pairs=list(it.combinations(range(n),2));mask=sum(1<<pairs.index(x) for x in e)
 return [n,mask,[str(i)+':'+''.join(A[c] for c in w) for i,w in ws]]

def synthesize():
 rows=[];stats=co.Counter();spectra=co.Counter()
 for n,e in generate_vertices():
  pp=[];pool=set();call=solver(n,e)
  for p in ports(n,e):
   stats['all_port_graphs']+=1
   if old_family(n,e,p):stats['skipped_retained_J']+=1;continue
   pp.append(p)
   for i,b in enumerate(BAD):
    w=call(p,b)
    if w is not None:pool.add((i,w));break
   else:raise RuntimeError('uncovered graph: do not conclude no-go')
   mask=sum(int(call(p,b) is not None)<<k for k,b in enumerate(((1,0,2,0),(14,0,2,0),(6,0,18,0),(19,0,18,0))))
   spectra[str(mask)]+=1
  candidates=[]
  for i,w in sorted(pool):
   allow=[{-1}|{v for v,c in enumerate(w) if 7<=(c-b)%20<=13} for b in BAD[i]]
   mask=sum(1<<j for j,p in enumerate(pp) if all(v in allow[k] for k,v in enumerate(p)))
   candidates.append((mask,i,w))
  remain=(1<<len(pp))-1;ws=[]
  while remain:
   mask,i,w=max(candidates,key=lambda x:((x[0]&remain).bit_count(),x[1],x[2]))
   assert remain&mask
   ws.append((i,w));remain&=~mask
  rows.append(encode(n,e,ws))
 D={'verdict':'candidate_only','encoding':'row=[n,edge_mask,witnesses]; edge bits use combinations(range(n),2); witness=bad_boundary_index:base20_vertex_colors; outside order=P,Q,R,S; alphabet=0123456789abcdefghij','bad_boundaries':BAD,'covers':rows}
 Path('cover.json').write_text(json.dumps(D,separators=(',',':'))+'\n')
 stats['C1C2_spectra']=dict(spectra)
 Path('synthesis.json').write_text(json.dumps(dict(stats),sort_keys=True)+'\n')
 print(json.dumps(dict(stats),sort_keys=True))

def check():
 d=json.loads(Path('cover.json').read_text());sk=generate_edges();keys=[];total=skip=wc=0
 assert d['bad_boundaries']==list(map(list,BAD))
 assert all(not original_exists(b) for b in BAD)
 for n,mask,ws in d['covers']:
  possible=list(it.combinations(range(n),2));e=tuple(x for i,x in enumerate(possible) if mask>>i&1);assert len(e)==mask.bit_count();keys.append((n,e))
  ww=[(int(s.split(':')[0]),tuple(A.index(c) for c in s.split(':')[1])) for s in ws]
  for i,w in ww:assert 0<=i<len(BAD) and legal(n,e,(),(),w)
  wc+=len(ww)
  allowed=[[{-1}|{v for v,c in enumerate(w) if 7<=(c-b)%20<=13} for b in BAD[i]] for i,w in ww]
  for p in ports(n,e):
   if old_family(n,e,p):skip+=1;continue
   assert any(all(v in aa[k] for k,v in enumerate(p)) for aa in allowed),('missing cover',n,mask,p)
   total+=1
 assert keys==sk and len(set(keys))==len(sk)
 # Executed negative controls; finite controls do not provide trusted verification.
 tests={
 'exclude_7':7<=7<=13 and not 7<7<=13,
 'exclude_13':7<=13<=13 and not 7<=13<13,
 'omit_upper_bound':14>=7 and not 7<=14<=13,
 'unreduced_translation':not legal(2,((0,1),),(),(),(20,27)),
 'reflect_only_one_vertex':legal(2,((0,1),),(),(),(6,13)) and not legal(2,((0,1),),(),(),(6,7)),
 'release_fixed_boundary':legal(1,(),(),(),(0,)) and not legal(1,(),(0,),(0,),(0,)),
 'drop_internal_edge':legal(2,(),(),(),(0,0)) and not legal(2,((0,1),),(),(),(0,0)),
 'inconsistent_identified_port_colors':not legal(1,(),(0,0),(0,7),(10,)),
 'invalid_color_alphabet':not legal(1,(),(),(),(20,)),
 'erase_a_skeleton':keys[:-1]!=sk,
 'duplicate_a_skeleton':len(set(keys+[keys[0]]))!=len(keys)+1,
 'replace_bad_by_colorable_boundary':original_exists((10,13,0,7))}
 assert all(tests.values())
 report={'verdict':'candidate_only','internal_graphs':len(sk),'covered_new_port_graphs':total,'skipped_retained_J':skip,'positive_cover_witnesses':wc,'original_bad_boundaries':len(BAD),'mutations':tests,'trusted_verifier_receipt':False}
 Path('check-result.json').write_text(json.dumps(report,sort_keys=True)+'\n');print(json.dumps(report,sort_keys=True))
if __name__=='__main__':
 if sys.argv[1:] == ['--generate']:synthesize()
 elif not sys.argv[1:]:check()
 else:raise SystemExit('usage: finite.py [--generate]')
