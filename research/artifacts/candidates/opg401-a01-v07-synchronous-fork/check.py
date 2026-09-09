"""Exact checks for a simultaneous four-vertex C1 repair, candidate-only.
No imports of earlier candidate logic. All limits enforced by the runner.
"""
import itertools as it, json, hashlib, collections, heapq
from pathlib import Path
Z=range(20)
OE=((0,1),(1,2),(2,3),(3,4),(4,0),(3,5),(5,6),(6,7),(7,2))
PI=(0,5,6,7)
def edge(a,b): return 7 <= abs(a-b) <= 13
A=[set(b for b in Z if edge(a,b)) for a in Z]
def adjacency(n,ee):
    nb=[set() for _ in range(n)]
    for u,v in ee:
        if u==v or not(0<=u<n and 0<=v<n):raise ValueError('edge')
        nb[u].add(v);nb[v].add(u)
    return nb
ON=adjacency(8,OE)
_cache={}
def fill(b):
    b=tuple(b)
    if b in _cache:return _cache[b]
    ds=[set(Z) for _ in range(8)]
    for v,c in zip(PI,b):ds[v]&=A[c]
    chosen=[-1]*8;nodes=0
    def rec(todo,dd):
        nonlocal nodes
        nodes+=1
        if nodes>1000000:raise RuntimeError('O search cap, not nonextension')
        if not todo:return chosen.copy()
        v=min(todo,key=lambda x:(len(dd[x]),-len(ON[x]),x));rest=todo-{v}
        for c in sorted(dd[v]):
            nd=dd.copy();good=True
            for w in ON[v]&rest:
                nd[w]=dd[w]&A[c]
                if not nd[w]:good=False;break
            if good:
                chosen[v]=c;out=rec(rest,nd)
                if out is not None:return out
        chosen[v]=-1
        return None
    ans=rec(set(range(8)),ds);_cache[b]=ans;return ans

def valid(ee,f):return all(type(c)==int and 0<=c<20 for c in f) and all(edge(f[u],f[v]) for u,v in ee)
def faces(rot):
    darts={(u,v) for u,row in enumerate(rot) for v in row}
    assert len(darts)==sum(map(len,rot))
    assert all((v,u) in darts for u,v in darts)
    seen=set();fs=[]
    for st in sorted(darts):
        if st in seen:continue
        u,v=st;F=[]
        while (u,v) not in seen:
            seen.add((u,v));F.append(u);row=rot[v]
            u,v=v,row[(row.index(u)+1)%len(row)]
        assert (u,v)==st;fs.append(F)
    return fs

def joinO(rot,ports):
    n=len(rot);p,q,r,s=ports
    ins=[[n+4,n+1,p],[n,n+2],[n+1,n+3,n+7],[n+2,n+4,n+5],
         [n+3,n],[n+6,n+3,q],[n+7,n+5,r],[n+2,n+6,s]]
    for slots in it.product(*(range(len(rot[v])) for v in ports)):
        rr=[a.copy() for a in rot]
        for v,x,j in zip(ports,PI,slots):rr[v].insert(j,n+x)
        rr+=ins
        ee=sorted({tuple(sorted((u,v))) for u,row in enumerate(rr) for v in row})
        ff=faces(rr)
        if len(rr)-len(ee)+len(ff)==2:return ee,rr,ff
    raise AssertionError('disk order not preserved')

def layers(n0,ports):
    free=[v for v in range(n0) if v not in ports];m=len(free);n=n0+5*m
    rot=[[(v-1)%n0,(v+1)%n0] for v in range(n0)]
    rot += [[] for _ in range(5*m)]
    for j in range(3*m):
        v=n0+j;rad=free[j//3] if j%3==0 else n0+3*m+2*(j//3)+(j%3-1)
        rot[v]=([n0+(j-1)%(3*m),rad,n0+(j+1)%(3*m)] if j%3==0 else [n0+(j-1)%(3*m),n0+(j+1)%(3*m),rad])
    for j,v in enumerate(free):rot[v].append(n0+3*j)
    for j in range(2*m):
        rad=n0+3*(j//2)+(j%2)+1
        rot[n0+3*m+j]=[n0+3*m+(j-1)%(2*m),rad,n0+3*m+(j+1)%(2*m)]
    ee=sorted({tuple(sorted((u,v))) for u,row in enumerate(rot) for v in row})
    # Orient the last annular layer on the same sphere, if needed.
    if n-len(ee)+len(faces(rot))!=2:
        for v in range(n0+3*m,n):rot[v]=list(reversed(rot[v]))
    assert n-len(ee)+len(faces(rot))==2
    return ee,rot

def conflict(ee,f,ell):
    nb=[[] for _ in f]
    for u,v in ee:
        if not (7<=(f[u]+f[v]-ell)%20<=13):nb[u].append(v);nb[v].append(u)
    return [sorted(x) for x in nb]

def fail_one(ee,nb,f,ports,t,z,ell):
    I=A[f[t]]&A[z]
    for v in sorted(nb[t]):
        if f[v] not in I and (ell-f[v])%20 not in I:return v
    req={v for v in nb[t] if f[v] not in I}
    forb={v for v in nb[t] if (ell-f[v])%20 not in I}
    forb|={v for v in ports if (ell-f[v])%20!=f[v]}
    cn=conflict(ee,f,ell);par={v:None for v in sorted(req)};queue=collections.deque(sorted(req))
    while queue:
        u=queue.popleft()
        if u in forb:
            path=[u]
            while par[path[-1]] is not None:path.append(par[path[-1]])
            return path[::-1]
        for v in cn[u]:
            if v not in par:par[v]=u;queue.append(v)
    return None

def verify_fail(ee,f,ports,t,z,ell,rec):
    es={tuple(sorted(e)) for e in ee};neigh={v if u==t else u for u,v in ee if t in (u,v)}
    def good(c):return edge(c,f[t]) and edge(c,z)
    if type(rec)==int:return rec in neigh and not good(f[rec]) and not good((ell-f[rec])%20)
    if not rec or len(rec)!=len(set(rec)):return False
    a,b=rec[0],rec[-1]
    return a in neigh and not good(f[a]) and good((ell-f[a])%20) and (
        b in ports and (ell-f[b])%20!=f[b] or b in neigh and good(f[b]) and not good((ell-f[b])%20)) and all(
        tuple(sorted((u,v))) in es and not edge((ell-f[u])%20,f[v]) for u,v in zip(rec,rec[1:]))

def smaller_supports(ee,f,ports,maxsize=3):
    """Enumerate all EXACT changed supports, including three changed ports.
    Every feasible exterior assignment is counted; no boundary table is used.
    """
    n=len(f);nb=adjacency(n,ee);rows=[];terminals=0;nodes=0
    for size in range(1,maxsize+1):
        for ss in it.combinations(range(n),size):
            S=set(ss)
            if not S&set(ports):continue # otherwise original O tuple is unchanged
            ds={v:(set.intersection(*(A[f[w]] for w in nb[v]-S)) if nb[v]-S else set(Z))-{f[v]} for v in S}
            local=0;legal=0;success=0;cur=f.copy()
            def rec(todo,dd):
                nonlocal local,legal,success
                local+=1
                if not todo:
                    legal+=1
                    if fill([cur[t] for t in ports]) is not None:success+=1
                    return
                v=min(todo,key=lambda x:(len(dd[x]),x));rest=todo-{v}
                for c in sorted(dd[v]):
                    nd=dd.copy();possible=True
                    for w in nb[v]&rest:
                        nd[w]=dd[w]&A[c]
                        if not nd[w]:possible=False;break
                    if possible:cur[v]=c;rec(rest,nd)
                cur[v]=f[v]
            rec(S,ds);assert success==0,('smaller witness',ss)
            rows.append([list(ss),local,legal]);nodes+=local;terminals+=legal
    return {'support_rows':rows,'supports':len(rows),'nodes':nodes,'legal_exterior_assignments':terminals,'O_extensions':0,
            'omitted_supports':'Supports meeting no port leave the bad O tuple unchanged.'}

def graphcheck(ee,rot,f):
    n=len(f);nb=adjacency(n,ee);assert valid(ee,f)
    assert len(set(map(tuple,ee)))==len(ee)
    assert all(len(row)<=3 for row in nb)
    assert all(not nb[u]&nb[v] for u,v in ee)
    assert [set(row) for row in rot]==nb
    fs=faces(rot);assert n-len(ee)+len(fs)==2
    return fs

def steiner(ee,f,k,ports):
    """Four-terminal subset DP. Exact integer cost and reconstructible edge tree."""
    nb=conflict(ee,f,k);n=len(f);INF=10**6;d=[[INF]*n for _ in range(16)];witness=[[None]*n for _ in range(16)]
    for mask in range(1,16):
        if mask&(mask-1)==0:
            i=mask.bit_length()-1;d[mask][ports[i]]=0;witness[mask][ports[i]]=set()
        sub=(mask-1)&mask
        while sub:
            oth=mask^sub
            if oth:
                for v in range(n):
                    val=d[sub][v]+d[oth][v]
                    if val<d[mask][v]:
                        d[mask][v]=val;witness[mask][v]=witness[sub][v]|witness[oth][v]
            sub=(sub-1)&mask
        heap=[(d[mask][v],v) for v in range(n) if d[mask][v]<INF];heapq.heapify(heap)
        while heap:
            dist,u=heapq.heappop(heap)
            if dist!=d[mask][u]:continue
            for v in nb[u]:
                if dist+1<d[mask][v]:
                    d[mask][v]=dist+1;witness[mask][v]=witness[mask][u]|{tuple(sorted((u,v)))};heapq.heappush(heap,(dist+1,v))
    v=min(range(n),key=lambda v:d[15][v]);te=sorted(witness[15][v]);assert len(te)==d[15][v]
    W=set(sum((list(e) for e in te),[]));assert set(ports)<=W
    c=sum(u in W and v in W for u,v in ee)-len(W)+1
    defic=sum(3-len(adjacency(n,ee)[u])-(u in ports) for u in W)
    cut=[(u,v) for u,v in ee if (u in W)!=(v in W)]
    assert len(cut)==len(W)-2-2*c-defic
    return {'n':len(W),'c':c,'d':defic,'b':len(cut),'vertices':sorted(W),'edges':te,'cut_edges':cut,
            'minimum_edges':d[15][v],'dp_costs':[[None if x>=INF else x for x in row] for row in d[1:]]}

def fork_case(p):
    # Q,R,y,w,common13,cut3,cut4,P,S,tail10,(tail12 for p1)
    f=[0,2,9,16,13,3,4,p,0,10]+([12] if p==1 else [])
    rot=[[2,4],[4,2],[0,3,1],[2,6,5],[0,1],[3,9],[],[],[9],[5,8]]
    if p==1:rot[6]=[3,10];rot[7]=[10];rot.append([6,7])
    else:rot[6]=[3,7];rot[7]=[6]
    ee=sorted({tuple(sorted((u,v))) for u,row in enumerate(rot) for v in row});ports=[7,0,1,8]
    graphcheck(ee,rot,f);full,fr,ff=joinO(rot,ports)
    g=f.copy();g[:4]=[5,6,18,11];inn=fill([g[v] for v in ports]);assert inn and valid(full,g+inn)
    return {'p':p,'colors':f,'ports':ports,'edges':ee,'rotation':rot,'faces':faces(rot),'fixed_vertices':list(range(4,len(f))),
            'newcolors':g,'O_fill':inn,'full_edges':full,'full_rotation':fr,'full_faces':ff}

def main():
    root=Path(__file__).resolve().parent;data=json.loads((root/'input.json').read_text())
    # Exhaustively enumerate the pinned claw. Both colors in common pins are 13.
    states=[]
    for q,r,y,w in it.product(Z,repeat=4):
        if edge(q,13) and edge(r,13) and edge(w,3) and edge(w,4) and edge(y,q) and edge(y,r) and edge(y,w):
            states.append((q,r,y,w))
    lo=[s for s in states if s[2]<10];hi=[s for s in states if s[2]>=10]
    assert set(states)==set(lo+hi)
    assert all(s[0]<=2 and s[1]<=2 and 7<=s[2]<=9 and 14<=s[3]<=16 for s in lo)
    assert all(5<=s[0]<=6 and 5<=s[1]<=6 and 18<=s[2]<=19 and 11<=s[3]<=12 for s in hi)
    assert min(sum(a!=b for a,b in zip(s,t)) for s in lo for t in hi)==4
    good={}
    for p in (1,14):
        entries=[s for s in states if fill((p,s[0],s[1],0)) is not None]
        assert entries==[(5,6,18,11)];good[str(p)]=fill((p,5,6,0))
    out={'verdict':'candidate_only','schema':'opg401-sync-fork-v1','fork':{'low_states':lo,'high_states':hi,'good':good,
        'cross_phase_min_hamming':4,'unique_filling_state':[5,6,18,11]},'small_fixtures':[fork_case(1),fork_case(14)]}
    cases=[]
    for row in data['large_fixtures']:
        f=row['colors'];ports=row['ports'];p=f[ports[0]];ee,rot=layers(row['n0'],ports);n=len(f)
        fs=graphcheck(ee,rot,f);nb=adjacency(n,ee)
        assert all(len(nb[v])==(2 if v in ports else 3) for v in range(n))
        assert [f[v] for v in ports]==[p,0,2,0]
        full,fr,ff=joinO(rot,ports);bd=[f[t] for t in ports];axisrows=[];zcount=0;pathcount=0
        for i,t in enumerate(ports):
            for z in Z:
                b=bd.copy();b[i]=z
                if fill(b) is None:continue
                bads=[]
                for ell in Z:
                    bad=fail_one(ee,nb,f,ports,t,z,ell);assert bad is not None
                    assert verify_fail(ee,f,ports,t,z,ell,bad)
                    zcount+=type(bad)==int;pathcount+=type(bad)==list;bads.append(bad)
                axisrows.append([i,z,bads])
        minimum=smaller_supports(ee,f,ports)
        g=row['newcolors'];S=[v for v in range(n) if f[v]!=g[v]];assert len(S)==4 and len(set(S)&set(ports))<=2
        assert valid(ee,g);inside=fill([g[t] for t in ports]);assert inside is not None and valid(full,g+inside)
        sg=steiner(ee,f,8 if p==1 else 16,ports)
        cases.append({'p':p,'colors':f,'ports':ports,'edges':ee,'rotation':rot,'faces':fs,'full_edges':full,'full_rotation':fr,'full_faces':ff,
           'all_target_failures':axisrows,'failure_counts':[zcount,pathcount],'strict_smaller_supports':minimum,
           'support':S,'newcolors':g,'O_fill':inside,'fixed_vertices':[v for v in range(n) if v not in S],'steiner':sg})
    out['large_fixtures']=cases
    # Negative controls use genuine violating objects rather than only changed assertions.
    mutations=[]
    def add(name,test):assert test;mutations.append(name)
    add('exclude_7',edge(0,7) and not 7<abs(0-7)<=13)
    add('exclude_13',edge(0,13) and not 7<=abs(0-13)<13)
    add('directed_without_mod',edge(19,6) and not 7<=6-19<=13)
    a=fork_case(1);old=a['colors'];new=a['newcolors'];ee=a['edges']
    for j in range(4):
        wrong=new.copy();wrong[j]=old[j]
        add('omit_changed_vertex_'+str(j),not valid(ee,wrong) or fill([wrong[t] for t in a['ports']]) is None)
    wrong=new.copy();wrong[5]=2
    add('secretly_move_separator',valid(ee,wrong) and any(wrong[v]!=old[v] for v in a['fixed_vertices']))
    add('only_project_one_port',fill((1,5,2,0)) is None and fill((1,5,6,0)) is not None)
    add('compare_phase_hamming_only_on_ports',sum(s!=t for s,t in zip((0,2),(5,6)))==2 and sum(s!=t for s,t in zip((0,2,9,16),(5,6,18,11)))==4)
    # Removing an incident edge creates an illegal extra state in the original graph.
    example=None
    for vals in it.product(Z,repeat=4):
        q,r,y,w=vals
        if edge(q,13) and edge(r,13) and edge(w,3) and edge(y,q) and edge(y,r) and edge(y,w) and not edge(w,4):example=vals;break
    add('omit_fixed_cut_edge',example is not None)
    def consistent_pins(entries):
        saved={}
        for v,c in entries:
            if v in saved and saved[v]!=c:return False
            saved[v]=c
        return True
    add('identify_distinct_cut_colors',not consistent_pins([(5,3),(5,4)]))
    for case in cases:
        for i,z,recs in case['all_target_failures']:
            path=next((r for r in recs if type(r)==list and len(r)>1),None)
            if path:
                bad=path.copy();bad[-1]=len(case['colors'])
                ell=recs.index(path)
                try: accepted=verify_fail(case['edges'],case['colors'],case['ports'],case['ports'][i],z,ell,bad)
                except (IndexError,ValueError):accepted=False
                add('bad_conflict_path_p'+str(case['p']),not accepted);break
    out['mutations']=mutations
    # Typed run-length encoding, not an opaque compressed blob. Round-trip each table.
    for case in cases:
        original=case['strict_smaller_supports'].pop('support_rows')
        values=[row[1:] for row in original]
        rle=[[sum(1 for _ in group),*value] for value,group in it.groupby(values)]
        assert [row[1:] for row in rle for _ in range(row[0])]==values
        case['strict_smaller_supports']['rle_nodes_legal']=rle
        for entry in case['all_target_failures']:
            original=entry[2]
            entry[2]=[[sum(1 for _ in group),value] for value,group in it.groupby(original)]
            assert [row[1] for row in entry[2] for _ in range(row[0])]==original
    out['encoding']={
      'support_order':'Sizes 1,2,3; lexicographic vertex combinations; omit supports meeting no port. RLE [repeat,nodes,legal_exterior_assignments]; all O counts are zero.',
      'axis_order':'Each [port_index,target,runs] expands [repeat,record] in axis order 0..19; integer record is zero-choice neighbor, list is a required-to-forbidden conflict path.'}
    for case in cases:
        (root/('case-p'+str(case['p'])+'.json')).write_text(json.dumps(case,separators=(',',':'))+'\n')
    out.pop('large_fixtures')
    (root/'fork-certificate.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
    print(json.dumps({'pinned_fork_states':[len(lo),len(hi)],'unique_good_states':2,'global_no_support_le3_cases':len(cases),
       'smaller_supports':sum(c['strict_smaller_supports']['supports'] for c in cases),
       'axis_failures':sum(sum(c['failure_counts']) for c in cases),'mutations':len(mutations),'classes_closed':[]}))
if __name__=='__main__':main()
