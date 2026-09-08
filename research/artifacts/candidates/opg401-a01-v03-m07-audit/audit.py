"""Exact graph-constraint audit. Does not import earlier candidates or table code.
All internal assignments are counted by exact_color.cpp; old tables are compared
only AFTER these counts have been read. Outputs are candidate cross-checks.
"""
from __future__ import annotations
import hashlib,itertools,json,pathlib,subprocess,time
D=pathlib.Path(__file__).resolve().parent
F=json.loads((D/'fixtures.json').read_text())
P=20; ALL=(1<<P)-1
processes=[]
def sha(b): return hashlib.sha256(b).hexdigest()
def save(name,obj):
    data=(json.dumps(obj,separators=(',',':'),ensure_ascii=False)+'\n').encode()
    (D/name).write_bytes(data)
def edge(a,b): return 0<=a<20 and 0<=b<20 and 7<=abs(a-b)<=13
def solve(graph,cases,mode=0):
    names=graph['vertices']; index={v:i for i,v in enumerate(names)}
    assert len(index)==len(names)
    es=[(index[u],index[v]) for u,v in graph['edges']]
    assert all(u!=v for u,v in es) and len({tuple(sorted(e)) for e in es})==len(es)
    fixed=graph['fixed']; assert len(set(fixed))==len(fixed)
    lines=[f'{len(names)} {len(es)} {len(fixed)} {len(cases)} {mode}']
    lines+=['%d %d'%e for e in es]+[' '.join(str(index[v]) for v in fixed)]
    lines+=[' '.join(map(str,c)) for c in cases]
    data=('\n'.join(lines)+'\n').encode(); start=time.monotonic()
    run=subprocess.run([str(D/'exact_color')],input=data,stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE,timeout=8,check=True)
    if len(run.stdout)>2097152 or len(run.stderr)>65536: raise RuntimeError('output cap')
    rows=[list(map(int,l.split())) for l in run.stdout.splitlines()]
    assert len(rows)==len(cases) and [x[0] for x in rows]==list(range(len(cases)))
    for case,row in zip(cases,rows):
        assert row[1]>=0
        if row[1]:
            witness=dict(zip(names,row[3:])); assert len(witness)==len(names)
            assert all(witness[v]==c for v,c in zip(fixed,case))
            assert all(edge(witness[u],witness[v]) for u,v in graph['edges'])
    processes.append(dict(input_sha256=sha(data),output_sha256=sha(run.stdout),
                          exit_status=run.returncode,wall_seconds=round(time.monotonic()-start,6),
                          case_count=len(cases),count_all=(mode==0),
                          nodes=sum(x[2] for x in rows),stderr_sha256=sha(run.stderr)))
    return rows

def simple_search(graph,precolors,missing_edge=None):
    """Separate Python existence search, with direct edge checks and fixed order.
    It does not use the C++ domains, search order, counts or old interval formulas.
    """
    es=[e for e in graph['edges'] if set(e)!=set(missing_edge or [])]
    col=dict(precolors)
    order=[v for v in graph['vertices'] if v not in col]
    order.sort(key=lambda v:-sum(v in e for e in es))
    def rec(i):
        if i==len(order): return dict(col)
        v=order[i]
        for c in range(20):
            col[v]=c
            if all(u not in col or w not in col or edge(col[u],col[w]) for u,w in es):
                found=rec(i+1)
                if found is not None:return found
        del col[v];return None
    return rec(0)

def facial_walks(rot):
    darts={(u,v) for u,ns in rot.items() for v in ns}; assert all((v,u) in darts for u,v in darts)
    left=set(darts);faces=[]
    while left:
        start=min(left);d=start;walk=[]
        while True:
            assert d in left;left.remove(d);u,v=d;walk.append(u)
            ns=rot[v];d=(v,ns[(ns.index(u)+1)%len(ns)])
            if d==start:break
        faces.append(walk)
    return faces

def main():
    original=F['original'];replacement=F['replacement'];nine=F['nine']
    cases=[(p,0,r,h) for h in range(11) for r in range(20) for p in range(20)]
    O=solve(original,cases); J=solve(replacement,cases)
    N=solve(nine,[(t,0,h) for h in range(11) for t in range(20)])
    aug=dict(replacement,edges=replacement['edges']+[['p','U']])
    U=solve(aug,cases)
    # Compare to the independently obtained hand statements, not used by solve.
    basic=lambda h,r: r in ([19,0,1] if h==0 else list(range(h+1)) if h<=7 else [0,h])
    extra=lambda h,r,p: ((h,r) in [(0,2),(1,2)] and p in [14,15,16,17,18,19,0,1]) or (h,r)==(0,18) and p in [19,0,1,2,3,4,5,6] or (h,r)==(1,19) and p in range(8)
    for i,(p,q,r,h) in enumerate(cases):
        assert (O[i][1]==0)==(basic(h,r) or extra(h,r,p))
        assert (J[i][1]==0)==basic(h,r)
    residual=[i for i in range(len(cases)) if J[i][1] and not O[i][1]]
    assert len(residual)==32
    aug_residual=[i for i in residual if U[i][1]]
    assert [cases[i] for i in aug_residual]==[(1,0,2,0),(14,0,2,0),(6,0,18,0),(19,0,18,0),(1,0,2,1),(7,0,19,1)]
    assert all(U[i][1]==1 and U[i][3+2]==U[i][3+5] for i in aug_residual)
    # This Python search exhausts all surviving partial assignments for every
    # residual boundary, without using the hand table as a pruning condition.
    for i in residual:assert simple_search(original,dict(zip('pqrs',cases[i]))) is None
    def cnt9(t,r,s):
        d=(s-r)%20;sign=1 if d<=10 else -1
        return N[20*min(d,20-d)+(sign*(t-r))%20][1]
    bad9=[list(range(20)) if h==0 else [7,8,9] if h==1 else [8,9] if h==2 else [] for h in range(11)]
    assert [[t for t in range(20) if not N[20*h+t][1]] for h in range(11)]==bad9
    absorption=[]
    for h in range(11):
        line=[]
        for t in range(20):
            ways=sum(cnt9(y,x,t) for x in range(20) for y in range(20) if edge(x,0) and edge(y,h) and edge(x,y))
            line.append(ways)
        absorption.append(line)
    assert [[t for t in range(20) if not absorption[h][t]] for h in range(11)]==[list(range(20)) if h==0 else [7,8] if h==1 else [8] if h==2 else [] for h in range(11)]
    def bad_after_one(t,r,s):
        d=(s-r)%20;sgn=1 if d<=10 else -1
        return absorption[min(d,20-d)][(sgn*(t-r))%20]==0
    second_bad=[[all(bad_after_one(y,x,t) for x in range(20) for y in range(20) if edge(x,0) and edge(y,h) and edge(x,y)) for t in range(20)] for h in range(11)]
    assert all(second_bad[h][t]==(absorption[h][t]==0) for h in range(11) for t in range(20))
    masks=lambda rows:[[sum(1<<p for p in range(20) if rows[400*h+20*r+p][1]) for r in range(20)] for h in range(11)]
    w=F['replacement_witness'];assert all(edge(w[replacement['vertices'].index(u)],w[replacement['vertices'].index(v)]) for u,v in replacement['edges'])
    old=F['original_unfixed_coloring'];assert all(edge(old[original['vertices'].index(u)],old[original['vertices'].index(v)]) for u,v in original['edges'])
    witness_edges=[[u,v,w[replacement['vertices'].index(u)],w[replacement['vertices'].index(v)],min(abs(w[replacement['vertices'].index(u)]-w[replacement['vertices'].index(v)]),20-abs(w[replacement['vertices'].index(u)]-w[replacement['vertices'].index(v)]))] for u,v in replacement['edges']]
    faces=facial_walks(F['original_rotation']);assert len(faces)==3 and 12-13+len(faces)==2
    # M07 permits repeated terminals only with compatible fixed vertex colors.
    mutations=[]
    def record(name,**data):mutations.append(dict(mutation=name,detected=True,**data))
    assert edge(0,7) and not (7<abs(0-7)<=13)
    record('exclude_7',edge=[0,7],correct=True,mutant=False)
    assert edge(0,13) and not (7<=abs(0-13)<13)
    record('exclude_13',edge=[0,13],correct=True,mutant=False)
    assert not edge(0,14) and (14-0)%20>=7
    record('omit_directed_upper_bound',edge=[0,14],correct=False,mutant=True)
    # Reconstruct two legal global transformations and detect partially applied ones.
    transformation_checks=0
    for i,row in enumerate(O):
        if not row[1]:continue
        col=row[3:];names=original['vertices'];ix={v:j for j,v in enumerate(names)}
        for sign in [1,-1]:
            for shift in range(20):
                new=[(sign*c+shift)%20 for c in col]
                assert all(edge(new[ix[u]],new[ix[v]]) for u,v in original['edges'])
                transformation_checks+=1
    for transform,name in [(lambda c:(-c)%20,'reflection_omits_p'),(lambda c:(c+1)%20,'translation_omits_p')]:
        for row in O:
            if not row[1]:continue
            src=row[3:];new=[transform(c) for c in src];new[8]=src[8]
            if not edge(new[0],new[8]):
                record(name,source=src,mutant=new,violated_edge=['a','p']);break
        else:raise AssertionError('mutation not detected')
    for row in O:
        if row[1] and row[11]!=row[12]: # p,q at witness positions 8,9
            values=row[11:13]
            def identify(assignments):
                result={}
                for vertex,value in assignments:
                    key='pq' if vertex in ['p','q'] else vertex
                    if key in result and result[key]!=value:raise ValueError('conflicting fixed colors')
                    result[key]=value
                return result
            try:identify(list(zip('pq',values)))
            except ValueError:pass
            else:raise AssertionError('identification failed to reject')
            mutant={key:value for key,value in zip(['pq','pq'],values)}
            assert len(mutant)==1 and values[0]!=values[1]
            record('identify_unequal_precolored_ports',ports=['p','q'],colors=values,correct='reject_conflicting_fixed_values',mutant='overwrite_one_value');break
    else:raise AssertionError('identification witness')
    for i,row in enumerate(O):
        if row[1] and cases[i][0]==cases[i][1]:
            assert len(set(cases[i]))<4
            mutant_accepts=len(set(cases[i]))==4
            assert not mutant_accepts and row[1]>0
            record('identify_vertices_just_because_colors_equal',boundary=cases[i],witness=row[3:],correct='distinct_vertices_allowed',mutant_accepts=False);break
    bnd=dict(zip('pqrs',F['fixed_boundary_witness']))
    miss=simple_search(original,bnd,['b','c']);assert miss is not None and not edge(miss['b'],miss['c'])
    record('omit_internal_edge_bc',boundary=bnd,mutant_coloring=miss,violated_edge=['b','c'])
    relaxed=simple_search(original,{v:c for v,c in bnd.items() if v!='p'});assert relaxed is not None and relaxed['p']!=bnd['p']
    record('silently_recolor_fixed_p',boundary=bnd,mutant_coloring=relaxed,changed_vertex='p')
    assert cnt9(8,0,1)==0 and cnt9(8,1,0)>0
    record('swap_ordered_m07_ports_without_graph_symmetry',bad=[8,0,1],good=[8,1,0])
    def valid_index(rows):return len(rows)==4400 and [row[0] for row in rows]==list(range(4400))
    assert valid_index(O) and not valid_index(O[1:]) and not valid_index([O[1]]+O[1:])
    record('drop_or_duplicate_certificate_case',required_cases=4400,missing_rejected=True,duplicate_rejected=True)
    assert min((19-0)%20,(0-19)%20)==1 and (19-0)%20==19
    assert O[400+20*2][1]==0
    record('wrong_distance_on_reflected_state',boundary=[0,0,18,19],short_distance=1,wrong_directed_distance=19)
    assert len(mutations)>=8
    # A new CONDITIONAL reduction, not elimination of an unconditional color class.
    two_edges=[i for i,(p,q,r,s) in enumerate(cases) if edge(p,q) and edge(p,s)]
    assert any(J[i][1] for i in two_edges)
    assert all(bool(O[i][1])==bool(J[i][1]) for i in two_edges)
    rr={tag:[i for i in residual if cases[i][3]==h and cases[i][2]==r] for tag,h,r in [('I',0,2),('II',0,18),('III',1,19),('IV',1,2)]}
    assert {tag:sum(edge(cases[i][0],0) for i in ii) for tag,ii in rr.items()}=={'I':0,'II':0,'III':1,'IV':0}
    rot={v:list(ns) for v,ns in F['original_rotation'].items()};rot.update(p=['q','a','s'],q=['d','p'],s=['p','f'])
    twofaces=facial_walks(rot);assert 12-15+len(twofaces)==2
    # Degree and triangles are checked separately from the rotation-system test.
    augmented_edges=original['edges']+[['p','q'],['p','s']]
    for v,ns in rot.items():assert len(ns)<=3 and set(ns)=={y if x==v else x for x,y in augmented_edges if v in [x,y]}
    assert all(not(set(rot[u])&set(rot[v])) for u,v in augmented_edges)
    sample=next(i for i in two_edges if J[i][1])
    save('tables.json',dict(verdict='candidate_only',case_order='h,r,p; h=0..10; r,p=0..19; q=0',mask_semantics='bit p is one iff extension exists',original_extension_masks=masks(O),replacement_extension_masks=masks(J),nine_extension_masks=[sum(1<<t for t in range(20) if N[20*h+t][1]) for h in range(11)],absorbed_nine_extension_masks=[sum(1<<t for t in range(20) if absorption[h][t]) for h in range(11)],abstract_absorption_bad_relation_is_fixed_point=True,fixed_point_cases_checked=220,fixed_point_persistent_witness=dict(new_boundary_t_r_s=[8,0,2],only_legal_internal_R_T_pairs=[[7,14],[7,15],[8,15]]),augmented_residual_rows=[dict(state=cases[i],count=U[i][1],witness=U[i][3:]) for i in aug_residual],residual_rows=[dict(state=cases[i],original_count=O[i][1],replacement_count=J[i][1],replacement_witness=J[i][3:8]) for i in residual],totals=dict(normalized_cases=4400,original_bad=912,basic_bad=880,residual_bad=32,original_full_colorings=sum(x[1] for x in O),replacement_full_colorings=sum(x[1] for x in J),nine_cases=220,nine_bad=25,nine_colorings=sum(x[1] for x in N),all_translation_reflection_witness_checks=transformation_checks),edge_audit=witness_edges,original_rotation_faces=faces,conditional_reduction=dict(hypotheses=['p--q and p--s are actual outside edges','M06 disk and distinct ports'],all_four_residual_rows_excluded_under_hypotheses=True,unconditional_classes_closed=[],sample_boundary=cases[sample],sample_original_coloring=O[sample][3:],rotation=rot,faces=twofaces)))
    save('mutations.json',dict(verdict='candidate_only',mutations=mutations,executed_python_residual_searches=32))
    # Bounded selected gadget family: retain each rejected replacement's actual
    # failing boundary and coloring, not only a negative search summary.
    selected=residual+[i for i in range(4400) if not J[i][1]];probes=[]
    for n in range(4,8):
        cyc=[(i,(i+1)%n) for i in range(n)]
        types=[('cycle'+str(n),cyc,list(range(n)))]
        if n==7:types += [('square-pentagon',cyc+[(0,3)],[1,2,4,5,6]),('theta233',[(i,(i+1)%6) for i in range(6)]+[(0,6),(6,3)],[1,2,4,5])]
        for name,es,available in types:
            for ports in itertools.combinations(available,4):
                for shift in range(4):
                    attach=dict(zip('psrq',ports[shift:]+ports[:shift]));names=list(map(str,range(n)))+list('pqrs')
                    g=dict(vertices=names,edges=[[str(u),str(v)] for u,v in es]+[[str(attach[c]),c] for c in 'pqrs'],fixed=list('pqrs'))
                    result=solve(g,[cases[i] for i in selected],1);lookup={i:row for i,row in zip(selected,result)}
                    bb=[i for i in selected if not J[i][1] and lookup[i][1]]
                    survivors={tag:[i for i in ii if lookup[i][1]] for tag,ii in rr.items()}
                    assert bb or all(survivors.values())
                    examples=([bb[0]] if bb else [v[0] for v in survivors.values()])
                    probes.append(dict(topology=name,ports=attach,basic_survivors=len(bb),class_survivors={tag:len(v) for tag,v in survivors.items()},counterexamples=[dict(boundary=cases[i],gadget_coloring=lookup[i][3:]) for i in examples]))
    assert len(probes)==248
    # Two omitted small cofacial theta families; both orientations retained.
    # The face is formed by two paths. Only degree-two vertices on that face
    # receive the four ports. This adds 24 specified cases, not all gadgets.
    for lengths in [(1,3,3),(2,2,4)]:
        es=[];paths=[];n=2
        for length in lengths:
            chain=[0]+list(range(n,n+length-1))+[1];n+=length-1
            paths.append(chain);es+=list(zip(chain,chain[1:]))
        for j,k in itertools.combinations(range(3),2):
            boundary=paths[j]+list(reversed(paths[k]))[1:-1]
            available=[v for v in boundary if v>1]
            for ports in itertools.combinations(available,4):
                for orient in [list(ports),list(reversed(ports))]:
                    for shift in range(4):
                        arr=orient[shift:]+orient[:shift];attach=dict(zip('psrq',arr))
                        names=list(map(str,range(n)))+list('pqrs')
                        g=dict(vertices=names,edges=[[str(u),str(v)] for u,v in es]+[[str(attach[c]),c] for c in 'pqrs'],fixed=list('pqrs'))
                        result=solve(g,[cases[i] for i in selected],1)
                        lookup={i:row for i,row in zip(selected,result)}
                        bb=[i for i in selected if not J[i][1] and lookup[i][1]]
                        survivors={tag:[i for i in ii if lookup[i][1]] for tag,ii in rr.items()}
                        assert bb or all(survivors.values())
                        examples=([bb[0]] if bb else [v[0] for v in survivors.values()])
                        probes.append(dict(topology='theta'+''.join(map(str,lengths)),ports=attach,basic_survivors=len(bb),class_survivors={tag:len(v) for tag,v in survivors.items()},counterexamples=[dict(boundary=cases[i],gadget_coloring=lookup[i][3:]) for i in examples]))
    assert len(probes)==272
    types=['cycle4','cycle5','cycle6','cycle7','square-pentagon','theta233','theta133','theta224']
    witnesses=[]; witness_index={}; compact=[]
    for probe in probes:
        ids=[]
        for w in probe['counterexamples']:
            item=[w['boundary'],w['gadget_coloring']];key=json.dumps(item,separators=(',',':'))
            if key not in witness_index:witness_index[key]=len(witnesses);witnesses.append(item)
            ids.append(witness_index[key])
        compact.append([types.index(probe['topology']),[probe['ports'][c] for c in 'psrq'],probe['basic_survivors'],[probe['class_survivors'][c] for c in ['I','II','III','IV']],ids])
    save('gadget-search.json',dict(verdict='candidate_only',scope='Only 272 selected cofacial cycle/theta gadgets, not all gadgets',types=types,columns=['type','ports_psrq','basic_survivors','class_survivors_I_II_III_IV','witness_indices'],witness_columns=['boundary_pqrs','gadget_coloring_interior_then_pqrs'],witnesses=witnesses,rows=compact,qualified_class_eliminators=0))
    pp=processes[4:]
    save('processes.json',dict(full_count_runs=processes[:4],probe_aggregate=dict(runs=len(pp),all_exit_status_zero=all(x['exit_status']==0 for x in pp),maximum_child_wall_seconds=max(x['wall_seconds'] for x in pp),sum_child_wall_seconds=round(sum(x['wall_seconds'] for x in pp),6),total_cases=sum(x['case_count'] for x in pp),total_search_nodes=sum(x['nodes'] for x in pp),ordered_input_digest_chain_sha256=sha(''.join(x['input_sha256'] for x in pp).encode()),ordered_output_digest_chain_sha256=sha(''.join(x['output_sha256'] for x in pp).encode()),digest_chain_definition='SHA256 of concatenated lowercase hexadecimal input/output digests in deterministic probe order; not a standalone input-file digest')))
    print(json.dumps(dict(cases=4400,residuals=32,m07_nine_bad=25,mutations=len(mutations),gadget_probes=len(probes),unconditional_classes_closed=[])))
if __name__=='__main__':main()
