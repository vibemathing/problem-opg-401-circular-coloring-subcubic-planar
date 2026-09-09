"""Finite controls for the pinned-stem theorem; not trusted verification.
All graph checks use literal edges. The O search uses representative distances;
message tables use modular differences. No earlier candidate module is imported.
"""
from pathlib import Path
from functools import lru_cache
from itertools import product
from math import comb
import json

P=range(20)
OE=((0,1),(1,2),(2,3),(3,4),(4,0),(3,5),(5,6),(6,7),(7,2))
PI=(0,5,6,7)
def ok(a,b):return 7 <= (b-a)%20 <= 13
def scalar(a,b):return 0<=a<20 and 0<=b<20 and 7<=abs(a-b)<=13
A=[{b for b in P if ok(a,b)} for a in P]

@lru_cache(None)
def fill(boundary):
    adj=[set() for _ in range(8)]
    for a,b in OE:adj[a].add(b);adj[b].add(a)
    ds=[set(P) for _ in range(8)]
    for v,c in zip(PI,boundary):ds[v]={z for z in P if scalar(c,z)}
    nodes=0
    def rec(d,sol):
        nonlocal nodes
        nodes+=1
        if nodes>100000:raise RuntimeError('O search node limit, not a negative result')
        if len(sol)==8:return [sol[v] for v in range(8)]
        u=min((v for v in range(8) if v not in sol),key=lambda v:(len(d[v]),v))
        for x in sorted(d[u]):
            nd=d.copy();ns=dict(sol);ns[u]=x
            for v in adj[u]:
                if v in ns:
                    if not scalar(x,ns[v]):break
                else:
                    nd[v]={z for z in d[v] if scalar(x,z)}
                    if not nd[v]:break
            else:
                w=rec(nd,ns)
                if w is not None:return w
        return None
    return rec(ds,{})

@lru_cache(None)
def root_options(p,w):
    out=[]
    for y in P:
        if not scalar(y,w):continue
        qr=[q for q in P if scalar(q,13) and scalar(q,y)]
        for q,r in product(qr,repeat=2):
            inner=fill((p,q,r,0))
            if inner is not None:out.append((q,r,y,inner))
    return out

def messages(m,s):
    """Complete tail counts and minimum Hamming costs, with argmin witnesses."""
    n=m+1;inf=n+1;cnt=None;cost=None;layers=[]
    for i in range(m,-1,-1):
        old=(16-7*i)%20;pin=(old+7)%20
        nc=[0]*20;nd=[inf]*20;arg=[None]*20
        for x in P:
            if not ok(x,pin):continue
            if i==m:
                if not ok(x,(old+7+s)%20):continue
                nc[x]=1;nd[x]=int(x!=old)
            else:
                children=[z for z in P if ok(x,z) and cnt[z]]
                nc[x]=sum(cnt[z] for z in children)
                if children:
                    z=min(children,key=lambda z:(cost[z],z));nd[x]=int(x!=old)+cost[z];arg[x]=z
        layers.append({'vertex':i,'counts':nc,'costs':[None if z==inf else z for z in nd],'argmin':arg})
        cnt,cost=nc,nd
    layers.reverse()
    return cnt,cost,layers

def brute_tail(m,s):
    """Different implementation: bounded literal pin/edge DFS, no displacement formula."""
    counts=[0]*20;costs=[m+2]*20;nodes=0
    def rec(seq):
        nonlocal nodes
        nodes+=1
        if nodes>500000:raise RuntimeError('tail brute-force node cap')
        i=len(seq)
        if i==m+1:
            counts[seq[0]]+=1;c=sum(x!=(16-7*j)%20 for j,x in enumerate(seq));costs[seq[0]]=min(costs[seq[0]],c);return
        old=(16-7*i)%20
        for x in P:
            if not scalar(x,(old+7)%20):continue
            if i==m and not scalar(x,(old+7+s)%20):continue
            if seq and not scalar(seq[-1],x):continue
            rec(seq+[x])
    rec([])
    return counts,costs,nodes

def make_graph(p,m,s):
    f={'Q':0,'R':2,'y':9,'AQ':13,'AR':13,'z':0,'P':p,'S':0}
    rot={'AQ':['z','Q','P'],'AR':['R','z','S'],'P':['AQ','o0'],
         'Q':['y','o5','AQ'],'R':['y','AR','o6'],'S':['o7','AR'],
         'y':['Q','R','w0'],'z':['AR','AQ'],'w0':['y','a0','b'],'a0':['w0'],'b':['w0'],
         'o0':['P','o4','o1'],'o1':['o0','o2'],'o2':['o1','o3','o7'],
         'o3':['o2','o4','o5'],'o4':['o3','o0'],'o5':['o3','Q','o6'],
         'o6':['o5','R','o7'],'o7':['o6','S','o2']}
    if p==14:
        rot['AQ'][2]='p_mid';rot['P'][0]='p_mid';rot['p_mid']=['AQ','P'];f['p_mid']=1
    for i in range(m+1):
        old=(16-7*i)%20;f['w'+str(i)]=old;f['a'+str(i)]=(old+7)%20
        if i:
            prev='w'+str(i-1);cur='w'+str(i);pin='a'+str(i)
            rot[prev][rot[prev].index('b')]=cur;rot['b']=[cur]
            rot[cur]=[prev,pin,'b'];rot[pin]=[cur]
    f['b']=(f['w'+str(m)]+7+s)%20
    edges=sorted({tuple(sorted((u,v))) for u,row in rot.items() for v in row})
    he=[e for e in edges if not any(v.startswith('o') for v in e)]
    support=['Q','R','y']+['w'+str(i) for i in range(m+1)]
    return f,rot,edges,he,support

def graph_check(rot,edges):
    assert all(len(row)==len(set(row)) and len(row)<=3 and v not in row for v,row in rot.items())
    assert all(u in rot[v] for u,row in rot.items() for v in row)
    assert all(not set(rot[u])&set(rot[v]) for u,v in edges)
    seen={next(iter(rot))};queue=list(seen)
    for u in queue:
        for v in rot[u]:
            if v not in seen:seen.add(v);queue.append(v)
    assert len(seen)==len(rot)
    darts={(u,v) for u,row in rot.items() for v in row};used=set();faces=[]
    for start in sorted(darts):
        if start in used:continue
        u,v=start;walk=[]
        while (u,v) not in used:
            used.add((u,v));walk.append(u);rr=rot[v];u,v=v,rr[(rr.index(u)+1)%len(rr)]
        assert (u,v)==start;faces.append(walk)
    assert used==darts and len(rot)-len(edges)+len(faces)==2
    return faces

def valid(edges,f):return all(scalar(f[a],f[b]) for a,b in edges)

def main():
    root=Path(__file__).resolve().parent;data=json.loads((root/'input.json').read_text())
    rows=[];brute_nodes=0;minima=[]
    for m in data['lengths']:
        for s in range(7):
            counts,costs,layers=messages(m,s);d=6-s
            expected=[0]*20
            for a in range(-d,1):expected[(16+a)%20]=comb(m+a+d,m)
            assert counts==expected
            if m<=3:
                bc,bd,nn=brute_tail(m,s);brute_nodes+=nn
                assert bc==counts and all(not counts[x] or bd[x]==costs[x] for x in P)
            for p in (1,14):
                total=0;best=None;witness=None
                for w in P:
                    if not counts[w]:continue
                    for q,r,y,inner in root_options(p,w):
                        total+=counts[w];c=int(q!=0)+int(r!=2)+int(y!=9)+costs[w]
                        if best is None or c<best:best=c;witness=[q,r,y,w]
                assert total==(m+5 if s==0 else 1 if s==1 else 0)
                assert best==(m+4 if s<=1 else None)
                rows.append([m,s,p,sum(counts),total,best])
            if s==1:minima.append([m,m+4])
    fixtures=[]
    for p in (1,14):
        for s in (1,2):
            m=1;f,rot,edges,he,U=make_graph(p,m,s);faces=graph_check(rot,edges)
            assert valid(he,f)
            k=8 if p==1 else 16
            ce=[(u,v) for u,v in he if not ok((k-f[u])%20,f[v])]
            reach={'P'};changed=True
            while changed:
                before=len(reach)
                for a,b in ce:
                    if a in reach:reach.add(b)
                    if b in reach:reach.add(a)
                changed=len(reach)>before
            assert {'P','Q','R','S'}<=reach
            Z=set(U)|{'o'+str(i) for i in range(8)}
            cut=[e for e in edges if (e[0] in Z)!=(e[1] in Z)]
            assert len(cut)==m+6
            g=dict(f);g.update(Q=5,R=6,y=18)
            for i in range(m+1):g['w'+str(i)]=(f['w'+str(i)]-5)%20
            pins=sorted(set(f)-set(U))
            if s==2:g['b']=(g['b']-1)%20
            inner=[8,1,14,2,15,12,19,7] if p==1 else [1,8,15,2,9,12,19,7]
            g.update({'o'+str(i):x for i,x in enumerate(inner)})
            assert valid(edges,g)
            assert all(g[v]==f[v] for v in pins if s==1 or v!='b')
            fixtures.append({'p':p,'m':m,'s':s,'outside_colors':f,'support':U,'fixed_vertices':pins,
                'full_edges':edges,'rotation':rot,'faces':faces,'primary_conflict_edges':ce,
                'cut_edges_of_O_union_support':cut,'ledger':{'n':len(U),'ports_in_support':2,'c':0,'d':0,'b':len(cut)},
                'full_coloring':g,'qualification':'fixed-complement repair' if s==1 else 'changes pin b; NOT a fixed-complement repair'})
    controls=[]
    def detect(name,test):
        assert test;controls.append(name)
    detect('exclude_endpoint7',scalar(0,7) and not 7<abs(0-7)<=13)
    detect('exclude_endpoint13',scalar(0,13) and not 7<=abs(0-13)<13)
    detect('wrong_modulus19',ok(19,6) and not 7<=((6-19)%19)<=13)
    detect('wrong_tail_orientation',ok(16,4) and not ok(11,9))
    detect('omit_terminal_pin',messages(1,1)[0][11]>0 and messages(1,2)[0][11]==0)
    detect('terminal_off_by_one',messages(1,0)[0][10]>0 and messages(1,1)[0][10]==0)
    detect('tail_color_is_not_ordinary_unwrapped_integer',(16-7*3)%20==15)
    detect('port_projection_witness_mix',fill((1,5,2,0)) is None and fill((1,5,6,0)) is not None)
    detect('update_root_before_children',not scalar(11,9))
    detect('update_fork_sequentially',not scalar(5,9))
    detect('forget_second_port_in_cut',(5-2)!=7)
    detect('fixed_pin_release_is_not_same_problem',messages(1,2)[0][11]==0 and messages(1,1)[0][11]>0)
    detect('constant_four_support_bound',messages(3,1)[1][11]+3==7)
    # Repeated physical pins must supply one consistent color, never two copies.
    duplicate=[('pin',13),('pin',12)];assigned={};consistent=True
    for v,x in duplicate:
        if v in assigned and assigned[v]!=x:consistent=False
        assigned[v]=x
    detect('split_repeated_boundary_vertex',not consistent)
    out={'schema':'opg401-v08-pinned-stem-v1','verdict':'candidate_only','rows_m_s_p_tail_count_fill_count_min_support':rows,
         'positive_minima':minima,'fixtures':fixtures,'mutations':controls,
         'counts':{'parameter_rows':len(rows),'brute_tail_nodes':brute_nodes,'complete_plane_fixtures':len(fixtures),'mutations':len(controls)},
         'scope':'Fixed-complement colored stems; not universal minimum-obstruction or root coverage. No C2 work.'}
    (root/'certificate.json').write_text(json.dumps(out,separators=(',',':'),sort_keys=True)+'\n')
    print(json.dumps(out['counts'],sort_keys=True))
if __name__=='__main__':main()
