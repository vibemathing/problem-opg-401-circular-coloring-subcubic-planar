"""Full-coloring closed-orbit controls. No projection of hidden boundary colors."""
import sys;sys.path.insert(0,'.')
import itertools as it,json
from pathlib import Path
from finite import original_exists,legal


def faces(rotation):
 darts={(v,u) for v,nb in enumerate(rotation) for u in nb};unused=set(darts);out=[]
 while unused:
  start=min(unused);edge=start;face=[]
  while True:
   assert edge in unused;unused.remove(edge);v,u=edge;face.append(v)
   row=rotation[u];edge=(u,row[(row.index(v)+1)%len(row)])
   if edge==start:break
  out.append(face)
 return out

def segment(colors,start,end,left,right):
 length=(end-start)%40;delta=(right-left)%20;k=-((delta-7*length)//20)
 total=delta+20*k;assert 7*length<=total<=13*length
 remain=total-7*length;x=left;colors[start]=x
 for j in range(1,length+1):
  d=min(6,remain);remain-=d;x=(x+7+d)%20;colors[(start+j)%40]=x
 assert remain==0 and x==right

def fixture(pindex):
 ports=(pindex,0,26,20);inner=(0,11,4,16,7,3,10,17)
 base_edges=[(0,1),(1,2),(2,3),(3,4),(4,0),(3,5),(5,6),(6,7),(7,2)]
 edges=[(i,(i+1)%40) for i in range(40)]+[(40+u,40+v) for u,v in base_edges]+[(40+v,u) for v,u in zip((0,5,6,7),ports)]
 P,Q,R,S=ports
 rinner=[[44,41,P],[40,42],[41,43,47],[42,44,45],[43,40],[46,43,Q],[47,45,R],[42,46,S]]
 rotation=None
 for signs in it.product((0,1),repeat=4):
  rr=[[(i-1)%40,(i+1)%40] for i in range(40)]+rinner
  for i,v,k in zip(ports,(40,45,46,47),signs):
   rr[i]=[(i-1)%40,v,(i+1)%40] if k else [(i-1)%40,(i+1)%40,v]
  ff=faces(rr)
  if 48-len(edges)+len(ff)==2:rotation=rr;break
 assert rotation is not None
 assert all(1<=len(x)<=3 for x in rotation)
 assert all(v not in rotation[w] for u,v in edges for w in rotation[u] if w!=v)
 external=[7*i%20 for i in range(40)]
 boundary=[external[i] for i in ports]
 assert boundary in ([1,0,2,0],[14,0,2,0]) and not original_exists(boundary)
 # All single-vertex color alternatives are tested in each full dihedral state.
 orbit=set();checks=0
 for sign,t in it.product((1,-1),range(20)):
  f=tuple((sign*c+t)%20 for c in external);orbit.add(f)
  assert all(7<=(f[(i+1)%40]-f[i])%20<=13 for i in range(40))
  for v in range(40):
   allowed=[c for c in range(20) if all(7<=(c-f[u])%20<=13 for u in ((v-1)%40,(v+1)%40))]
   assert allowed==[f[v]];checks+=20
  assert not original_exists(tuple(f[i] for i in ports))
 assert len(orbit)==40
 # Integer reconstruction of a full original-graph coloring with changed exterior.
 full=[None]*48
 for x,y,a,b in [(0,P,13,10),(P,20,10,7),(20,26,7,0),(26,0,0,13)]:segment(full,x,y,a,b)
 full[40:]=inner
 assert legal(48,edges,(),(),full)
 return {'P_index':P,'outside_boundary':boundary,'original_vertices':list(range(48)),
 'edges':edges,'rotation':rotation,'face_walks':faces(rotation),'initial_outside_colors':external,
 'port_order_P_Q_R_S':ports,'changed_outside_full_coloring':full,
 'closed_orbit_definition':'colors[i]=(sign*7*i+translation)%20, sign in {1,-1}, translation in 0..19',
 'closed_orbit_size':len(orbit),'single_vertex_color_trials':checks,
 'each_orbit_state_has_no_original_extension':True,
 'C2_reflected_boundary':[(-c)%20 for c in boundary],
 'minimality_scope':'smallest simple-cycle exterior with a frozen coloring and two distinct same-colored Q,S ports; no global patch-minimality claim'}

if __name__=='__main__':
 ff=[fixture(3),fixture(2)]
 out={'verdict':'candidate_only','fixtures':ff,
 'universal_recoloring_claim_rejected':'single-vertex changes, arbitrary-subset uniform +/-1 changes, and global reflection always reach an extendible boundary for arbitrary valid exteriors',
 'subset_shift_check':'proved symbolically: a +1 shift set must be successor-closed in the tight directed C40; only empty/all. A -1 shift set must be predecessor-closed.',
 'not_a_minimal_root_obstruction':True,'closed_residual_classes':[],'open_residual_classes':['C1','C2','C3','C4'],'trusted_verifier_receipt':False}
 Path('recolor-certificate.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
 print(json.dumps({'fixtures':len(ff),'closed_orbit_states':sum(f['closed_orbit_size'] for f in ff),'single_vertex_color_trials':sum(f['single_vertex_color_trials'] for f in ff),'n_m_f':[[48,len(f['edges']),len(f['face_walks'])] for f in ff],'boundary_cases':[f['outside_boundary'] for f in ff]}))
