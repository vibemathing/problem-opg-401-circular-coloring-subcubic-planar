"""Bounded literal-edge controls for V05. No imports of earlier candidates."""
import copy
import itertools
import json
import sys
from collections import deque
from pathlib import Path

P = range(20)
O_EDGES = [(0,1),(1,2),(2,3),(3,4),(4,0),(3,5),(5,6),(6,7),(7,2)]
O_PORTS = [0,5,6,7]

def ok(a,b):
    return 7 <= (b-a)%20 <= 13

def literal(a,b):
    return 0 <= a < 20 and 0 <= b < 20 and 7 <= abs(a-b) <= 13

def neighbors(n, edges):
    out=[set() for _ in range(n)]
    for a,b in edges:
        assert 0 <= a < n and 0 <= b < n and a != b and b not in out[a]
        out[a].add(b); out[b].add(a)
    return out

def axis(n,edges,f,ports,target,new,ell,pins=()):
    """Exact V04 selector test. Returned paths retain the actual input colors."""
    if target in pins and new!=f[target]: return [ell,'T',target,f[target],new]
    adj=neighbors(n,edges); links=[set() for _ in range(n)]
    for a,b in edges:
        if not ok((ell-f[a])%20,f[b]):
            links[a].add(b); links[b].add(a)
    allowed={x for x in P if ok(x,f[target]) and ok(x,new)}
    forbidden={v for v in set(ports)|set(pins) if (ell-f[v])%20 != f[v]}
    required=[]
    for v in sorted(adj[target]):
        a=f[v] in allowed; b=(ell-f[v])%20 in allowed
        if not a and not b:
            return [ell,'N',v,f[v],(ell-f[v])%20]
        if not a: required.append(v)
        if not b: forbidden.add(v)
    parent={v:None for v in required}; q=deque(required)
    while q:
        v=q.popleft()
        if v in forbidden:
            path=[v]
            while parent[path[-1]] is not None: path.append(parent[path[-1]])
            return [ell,'P',path[::-1]]
        for w in sorted(links[v]):
            if w not in parent: parent[w]=v; q.append(w)
    first=[(ell-c)%20 if v in parent else c for v,c in enumerate(f)]
    second=first.copy(); second[target]=new
    assert all(ok(first[a],first[b]) and ok(second[a],second[b]) for a,b in edges)
    assert all(first[v]==f[v] for v in set(ports)|set(pins))
    return [ell,'Y',sorted(parent),first,second]

def verify_failure(n,edges,f,ports,target,new,row,pins=()):
    """Another code path: check the supplied local/path certificate, not closure."""
    ell,kind=row[:2]; adj=neighbors(n,edges)
    allowed={x for x in P if literal(x,f[target]) and literal(x,new)}
    if kind=='T': return target in pins and new!=f[target] and row[2:]==[target,f[target],new]
    if kind=='N':
        v,old,changed=row[2:]
        return (v in adj[target] and old==f[v] and changed==(ell-old)%20
                and old not in allowed and changed not in allowed)
    if kind!='P': return False
    path=row[2]
    if not path or len(path)!=len(set(path)): return False
    if path[0] not in adj[target]: return False
    if f[path[0]] in allowed or (ell-f[path[0]])%20 not in allowed: return False
    for u,v in zip(path,path[1:]):
        if v not in adj[u] or literal((ell-f[u])%20,f[v]): return False
    v=path[-1]
    fixed=v in set(ports)|set(pins) and (ell-f[v])%20!=f[v]
    old_only=v in adj[target] and f[v] in allowed and (ell-f[v])%20 not in allowed
    return fixed or old_only

def face_walks(rot):
    seen=set(); result=[]
    for a in sorted(rot):
        for b in rot[a]:
            if (a,b) in seen: continue
            u,v=a,b; walk=[]
            while (u,v) not in seen:
                seen.add((u,v)); walk.append(u)
                rr=rot[v]; u,v=v,rr[(rr.index(u)+1)%len(rr)]
            assert (u,v)==(a,b)
            result.append(walk)
    assert len(seen)==sum(map(len,rot.values()))
    return result

def make_graph(data):
    N,M=data['outer'],data['inner']; n=N+M
    assert n<=20 and N>=4 and M>=4
    spokes=data['spokes']; ports=data['ports']
    edges=[(i,(i+1)%N) for i in range(N)]
    edges += [(N+i,N+(i+1)%M) for i in range(M)]
    edges += [(v,N+j) for j,v in enumerate(spokes)]
    edges=sorted(tuple(sorted(e)) for e in edges)
    full=sorted(edges+[(n+a,n+b) for a,b in O_EDGES]
                +[(ports[j],n+v) for j,v in enumerate(O_PORTS)])
    full=sorted(tuple(sorted(e)) for e in full)
    rot={i:[(i-1)%N,(i+1)%N] for i in range(N)}
    for j in range(M): rot[N+j]=[N+(j-1)%M,N+(j+1)%M]
    for j,i in enumerate(spokes): rot[i].insert(1,N+j);rot[N+j].append(i)
    assert n-len(edges)+len(face_walks(rot))==2
    inner=[[4,1,'P'],[0,2],[1,3,7],[2,4,5],[3,0],[6,3,'Q'],[7,5,'R'],[2,6,'S']]
    mp=dict(zip('PQRS',ports)); fullrot=None
    for pos,flip in itertools.product([0,1],[False,True]):
        rr=copy.deepcopy(rot)
        for j,v in enumerate(O_PORTS): rr[ports[j]].insert(pos,n+v)
        for v,ns in enumerate(inner):
            vals=[mp[x] if isinstance(x,str) else n+x for x in ns]
            rr[n+v]=vals[::-1] if flip else vals
        if n+8-len(full)+len(face_walks(rr))==2:
            fullrot=rr;break
    assert fullrot is not None
    for ee,rr,order in [(edges,rot,n),(full,fullrot,n+8)]:
        adj=neighbors(order,ee)
        assert all(set(rr[v])==adj[v] for v in range(order))
        assert max(map(len,adj))<=3
        assert all(not (adj[a]&adj[b]) for a,b in ee)
    return n,edges,full,rot,fullrot

def smallest_tree(n,edges,ports):
    adj=neighbors(n,edges); terminals=set(ports); rest=sorted(set(range(n))-terminals)
    tested=0
    for size in range(len(rest)+1):
        for xs in itertools.combinations(rest,size):
            tested+=1; S=terminals|set(xs); q=[min(S)]; seen=set(q); tree=[]
            for v in q:
                for w in sorted(adj[v]&S):
                    if w not in seen: seen.add(w);q.append(w);tree.append([v,w])
            if seen==S: return sorted(S),tree,tested
    raise AssertionError('ports disconnected')

def fill(n,edges,pinned):
    """Positive witness finder; the certificate is checked independently by edges."""
    adj=neighbors(n,edges); masks=[sum(1<<b for b in P if literal(a,b)) for a in P]
    domains=[(1<<20)-1]*n
    for v,c in pinned.items(): domains[v]=1<<c
    count=0
    def dfs(ds):
        nonlocal count
        count+=1
        if count>2000000: raise RuntimeError('node cap reached')
        todo=[v for v in range(n) if ds[v].bit_count()==1]; seen=set()
        while todo:
            v=todo.pop()
            if v in seen: continue
            seen.add(v); c=ds[v].bit_length()-1
            for w in adj[v]:
                z=ds[w]&masks[c]
                if not z: return None
                if z!=ds[w]:
                    ds[w]=z
                    if z.bit_count()==1: todo.append(w)
        left=[v for v in range(n) if ds[v].bit_count()>1]
        if not left: return [m.bit_length()-1 for m in ds]
        v=min(left,key=lambda a:(ds[a].bit_count(),-len(adj[a]),a)); bits=ds[v]
        while bits:
            bit=bits&-bits; bits-=bit; nd=ds.copy(); nd[v]=bit
            ans=dfs(nd)
            if ans is not None:return ans
        return None
    answer=dfs(domains)
    if answer is not None:
        assert all(ok(answer[a],answer[b]) for a,b in edges)
        assert all(answer[v]==c for v,c in pinned.items())
    return answer,count

def scope_fixture(data,sign):
    n,edges,full,rot,fullrot=make_graph(data)
    f=[sign*c%20 for c in data['colors']]; ports=data['ports']; k=sign*data['primary']%20
    assert len(f)==n and all(literal(f[a],f[b]) for a,b in edges)
    L=[(a,b) for a,b in edges if not ok((k-f[a])%20,f[b])]
    W,tree,subsets=smallest_tree(n,L,ports); C=set(ports[:1]); queue=list(C);ladj=neighbors(n,L)
    for v in queue:
        for w in sorted(ladj[v]):
            if w not in C:C.add(w);queue.append(w)
    assert set(ports)<=C
    all_tables=[]
    for t in ports:
        new=(k-f[t])%20
        rows=[axis(n,edges,f,ports,t,new,ell) for ell in P]
        assert all(verify_failure(n,edges,f,ports,t,new,row) for row in rows)
        all_tables.append({'target':t,'new':new,'rows':rows})
    unit=sign*3%20;t=ports[2]
    unit_rows=[axis(n,edges,f,ports,t,unit,ell) for ell in P]
    assert all(verify_failure(n,edges,f,ports,t,unit,row) for row in unit_rows)
    relevant=[sign*x%20 for x in [19,0,1,2,3,4]]
    assert all(unit_rows[ell][1]=='P' for ell in relevant)
    degrees=neighbors(n+8,full)
    assert [v for v in range(n+8) if len(degrees[v])==2]==[n+1,n+4]
    chords=sum(a in W and b in W for a,b in edges)-(len(W)-1)
    deficit=sum(3-len(degrees[v]) for v in W);Z=set(W)|set(range(n,n+8))
    cut=[list(e) for e in full if (e[0] in Z)!=(e[1] in Z)]
    assert len(cut)==len(W)-2-2*chords-deficit
    half=(k//2)%10
    plus={(half+j)%20 for j in range(1,10)}
    minus={(half-j)%20 for j in range(1,10)}
    eps={v:(1 if f[v] in plus else -1) for v in C}
    assert all(f[v] in plus|minus for v in C)
    assert all(eps[a]!=eps[b] for a,b in L if a in C)
    compat=[e for e in edges if e not in L]; madj=neighbors(n,compat)
    signed={'sum':sum(eps.values()),'ports':sum(eps[v] for v in ports),
            'deficit':sum(eps[v]*(3-len(degrees[v])) for v in C),
            'compatible':sum(eps[v]*len(madj[v]) for v in C)}
    assert 3*signed['sum']==signed['ports']+signed['deficit']+signed['compatible']
    joined=set(W)
    for row in [r for tab in all_tables for r in tab['rows']]+unit_rows:
        joined.update(row[2] if row[1]=='P' else [row[2]])
    joined_chords=sum(a in joined and b in joined for a,b in edges)-len(joined)+1
    joined_Z=joined|set(range(n,n+8))
    joined_cut=[list(e) for e in full if (e[0] in joined_Z)!=(e[1] in joined_Z)]
    joined_deficit=sum(3-len(degrees[v]) for v in joined)
    assert len(joined_cut)==len(joined)-2-2*joined_chords-joined_deficit
    path_edges=set()
    for row in [r for tab in all_tables for r in tab['rows']]+unit_rows:
        if row[1]=='P':
            for a,b in zip(row[2],row[2][1:]):
                path_edges.add((row[0],a,b,(f[b]-f[a])%20,(f[a]-f[b])%20,(f[a]+f[b]-row[0])%20))
    # The existing directed-tight-closure theorem is used only to exhibit a full coloring.
    reach={t}; q=[t]; directed=[[] for _ in range(n)]
    for a,b in edges:
        if (f[b]-f[a])%20==sign*7%20: directed[a].append(b)
        if (f[a]-f[b])%20==sign*7%20: directed[b].append(a)
    for v in q:
        for w in directed[v]:
            if w not in reach:reach.add(w);q.append(w)
    assert reach.intersection(ports)=={t}
    g=[(c+sign)%20 if v in reach else c for v,c in enumerate(f)]
    whole,nodes=fill(n+8,full,dict(enumerate(g)))
    assert whole is not None
    keep={v:f[v] for v in range(n) if v not in W}
    absorbed,anodes=fill(n+8,full,keep)
    assert absorbed is not None
    # These are positive restorations for the ACTUAL separator only, not all boundary tuples.
    edge_notes=[[a,b,(f[b]-f[a])%20,(f[a]-f[b])%20,(f[a]+f[b]-k)%20] for a,b in L]
    return {'case':data['name'],'sign':sign,'n':n,'ports':ports,'primary':k,'colors':f,
            'H_edges':edges,'G_edges':full,'rotation':fullrot,'faces':face_walks(fullrot),
            'primary_conflicts':edge_notes,'component':sorted(C),'steiner_vertices':W,
            'steiner_edges':tree,'steiner_subsets_tested':subsets,'boundary':[len(W),chords,deficit,len(cut)],
            'cut_edges':cut,'signed':signed,'primary_target_failures':all_tables,
            'unit_target':unit,'unit_target_failures':unit_rows,
            'failure_edge_certificates':sorted(path_edges),
            'path_union':{'vertices':sorted(joined),'boundary':[len(joined),joined_chords,joined_deficit,len(joined_cut)],'cut_edges':joined_cut},
            'actual_repair':{'selected':sorted(reach),'fixed_complement':sorted(set(range(n))-reach),
                             'new_H_colors':g,'full_colors':whole,'nodes':nodes},
            'actual_absorption_restore':{'fixed':keep,'full_colors':absorbed,'nodes':anodes,
                                         'scope':'this actual fixed separator, not every assignment'}}

def local_tables():
    result=[]
    for old,new in [(2,6),(0,16)]:
        I={z for z in P if ok(z,old) and ok(z,new)}; old_allowed=[z for z in P if ok(z,old)]
        entries=[]
        for a,b in itertools.product(old_allowed,repeat=2):
            axes=[ell for ell in P if all(x in I or (ell-x)%20 in I for x in [a,b])]
            entries.append([a,b,sum(1<<ell for ell in axes)])
        absent=[r[:2] for r in entries if r[2]==0]
        expected=[[9,12],[12,9]] if old==2 else [[10,13],[13,10]]
        assert absent==expected
        result.append({'old':old,'new':new,'I':sorted(I),'rows':entries,'no_local_axis':absent})
    I=set(range(10,16)); checked=0
    for a,b in itertools.product(range(9,16),repeat=2):
        for ell in [19,0,1,2,3,4]:
            assert all(x in I or (ell-x)%20 in I for x in [a,b]);checked+=1
    return result,checked

def main():
    src=json.loads(Path(sys.argv[1]).read_text()); fixtures=[scope_fixture(d,s) for d in src['cases'] for s in [1,-1]]
    tables,local=local_tables()
    assert all(ok(a,b)==literal(a,b) for a,b in itertools.product(P,repeat=2))
    for p,inside in [(1,[8,1,14,2,15,9,16,7]),(14,[1,9,2,15,8,7,16,9])]:
        assert all(literal(inside[a],inside[b]) for a,b in O_EDGES)
        assert all(literal(inside[v],c) for v,c in zip(O_PORTS,[p,0,3,0]))
    # Mutation tests use actual changed values/certificates, not an assertion that tests exist.
    f0=fixtures[0];data=src['cases'][0];n=f0['n'];ee=f0['H_edges'];f=f0['colors'];ports=f0['ports']
    row=next(r for tab in f0['primary_target_failures'] for r in tab['rows'] if r[1]=='P')
    tab=next(t for t in f0['primary_target_failures'] if row in t['rows'])
    broken=copy.deepcopy(row);broken[2]=broken[2][:-1]
    no=next(r for r in f0['primary_target_failures'][0]['rows'] if r[1]=='N')
    corrupt=copy.deepcopy(no);corrupt[-1]=(corrupt[-1]+1)%20
    missing=[e for e in ee if set(e)!=set(row[2][:2])]
    bad_color=f.copy();bad_color[0]=(bad_color[0]+1)%20
    wrong_target=f0['actual_repair']['new_H_colors'].copy(); wrong_target[ports[2]]=6
    partly_negated=f0['actual_repair']['full_colors'].copy()
    partly_negated[:n]=[(-c)%20 for c in partly_negated[:n]]
    mutations={
        'exclude_7': literal(0,7) and not (7<abs(0-7)<=13),
        'exclude_13': literal(0,13) and not (7<=abs(0-13)<13),
        'wrong_directed_no_upper': (19>=7) and not ok(0,19),
        'corrupt_no_choice': not verify_failure(n,ee,f,ports,ports[0],7,corrupt),
        'truncate_failure_path': not verify_failure(n,ee,f,ports,tab['target'],tab['new'],broken),
        'omit_path_edge': not verify_failure(n,missing,f,ports,tab['target'],tab['new'],row),
        'wrong_input_coloring': not all(literal(bad_color[a],bad_color[b]) for a,b in ee),
        'wrong_absorption_boundary_three': f0['boundary'][3]!=3,
        'ignore_external_spokes': f0['boundary'][3]>2,
        'false_zero_choice_unit_axis': all(x in set(range(10,16)) or (19-x)%20 in set(range(10,16)) for x in [9,12]),
        'confuse_equal_colors_with_vertices': ports[1]!=ports[3] and f[ports[1]]==f[ports[3]],
        'old_primary_target_not_unit_target': not all(literal(wrong_target[a],wrong_target[b]) for a,b in ee),
        'partial_C2_conjugation': not all(literal(partly_negated[a],partly_negated[b]) for a,b in f0['G_edges']),
        'silently_change_fixed_target': axis(2,[(0,1)],[2,13],[0],0,3,19,pins=[0])[1]=='T',
    }
    assert all(mutations.values()),mutations
    out={'schema':'opg401-v05-axis-certificates-v1','verdict':'candidate_only','fixtures':fixtures,
         'local_axis_tables':tables,'unit_local_checks':local,'mutations':mutations,
         'closed_residual_classes':[],'open_residual_classes':['C1','C2','C3','C4'],
         'trust_scope':'candidate-generator execution only; no trusted closure'}
    Path(sys.argv[2]).write_text(json.dumps(out,separators=(',',':'),sort_keys=True)+'\n')
    print(json.dumps({'fixtures':len(fixtures),'primary_axes_failed':sum(20*len(x['primary_target_failures']) for x in fixtures),
                      'unit_axes_failed':20*len(fixtures),'unit_local_checks':local,
                      'mutations_detected':len(mutations),'whole_classes_closed':[]}))

if __name__=='__main__':main()
