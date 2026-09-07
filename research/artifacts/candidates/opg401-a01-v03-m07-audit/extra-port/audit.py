"""Reconstruct graph tables, test M07, and preserve the unresolved quantifiers."""
import csv
import json
from pathlib import Path
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from engine import ADJ, edges, theta_count, witness, valid, small_replacements

ROOT = Path(__file__).resolve().parent
input_data = json.loads((ROOT/'input.json').read_text())
assert (input_data['palette'],input_data['lower'],input_data['upper']) == (20,7,13)
graphs = input_data['graphs']
O, J, JU, QV = (graphs[k] for k in ('original','replacement','alpha_U','q_V'))


def boundary(p,q,r,s):
    return dict(p=p,q=q,r=r,s=s)


def classification(p,r,h):
    # Specification under test; never used by the graph counter or DFS.
    if ((h == 0 and r in (19,0,1)) or (1 <= h <= 7 and 0 <= r <= h)
            or (8 <= h <= 10 and r in (0,h))):
        return 'basic'
    if h == 0 and r == 2 and p in tuple(range(14,20))+(0,1): return 'K1'
    if h == 0 and r == 18 and p in (19,0,1,2,3,4,5,6): return 'K2'
    if h == 1 and r == 19 and 0 <= p <= 7: return 'K3'
    if h == 1 and r == 2 and p in tuple(range(14,20))+(0,1): return 'K4'
    return 'good'


def forbidden(t,r,s):
    # Exact statement of M07 B, compared to nine-vertex edge counts below.
    d, z = (s-r)%20, (t-r)%20
    if d > 10: d, z = 20-d, -z%20
    return d == 0 or d == 1 and z in (7,8,9) or d == 2 and z in (8,9)


rows=[]; residual=[]; counts={}; zero=0; sum_counts=0
for h in range(11):
    for r in range(20):
        mask=0; augmented=0
        jj=theta_count(J,boundary(0,0,r,h))
        qv=theta_count(QV,boundary(0,0,r,h))
        for p in range(20):
            cc=boundary(p,0,r,h)
            n=theta_count(O,cc); counts[p,r,h]=n
            lab=classification(p,r,h)
            assert bool(n) == (lab == 'good'), (cc,n,lab)
            assert bool(jj) == (lab != 'basic')
            mask |= int(n>0)<<p
            aa=theta_count(JU,cc); augmented |= int(aa>0)<<p
            zero += n==0; sum_counts+=n
            # This direct-edge DFS is separate from path sum-products.
            ww=witness(O,cc)
            assert (ww is not None) == bool(n)
            if ww is not None: assert valid(O,cc,ww)
            neg={k:-v%20 for k,v in cc.items()}
            shifted={k:(v+1)%20 for k,v in cc.items()}
            assert theta_count(O,neg)==n and theta_count(O,shifted)==n
            if lab not in ('basic','good'):
                jw=witness(J,cc); assert jw is not None and valid(J,cc,jw)
                uw=witness(JU,cc)
                if uw is not None:
                    assert valid(JU,cc,uw) and uw['V']==p
                residual.append({'class':lab,'boundary':cc,'original_count':n,
                                 'replacement_count':jj,'replacement_witness':jw,
                                 'alpha_U_count':aa,'alpha_U_witness':uw,
                                 'q_V_count':qv})
        rows.append([h,r,format(mask,'05x'),jj,format(augmented,'05x'),qv])
with (ROOT/'boundary-table.csv').open('w',newline='') as f:
    wr=csv.writer(f,lineterminator='\n');wr.writerow(['h','r','original_p_mask','J_count','JU_p_mask','JqV_count']);wr.writerows(rows)

nine=[]
for s in range(20):
    rr=[]
    for t in range(20):
        # P has one edge to t; its color x is the SAME vertex on both old p/q ports.
        n=sum(theta_count(O,boundary(x,x,0,s)) for x in ADJ[t])
        assert (n==0)==forbidden(t,0,s)
        rr.append(n)
    nine.append(rr)
absorption=[]
for d in range(11):
    bad=[]; witnesses=[]
    for z in range(20):
        choices=[(x,y) for x in ADJ[0] for y in ADJ[d] if y in ADJ[x] and not forbidden(y,x,z)]
        if not choices: bad.append(z)
        else: witnesses.append([z,*choices[0]])
    expected=list(range(20)) if d==0 else [7,8] if d==1 else [8] if d==2 else []
    assert bad==expected
    absorption.append({'d':d,'bad_t':bad,'good_witnesses_t_R_T':witnesses})

old_b=boundary(0,0,2,0); old_w=input_data['replacement_witness']
assert valid(J,old_b,old_w) and theta_count(O,old_b)==0
changed_b=input_data['original_full_boundary']; changed_w=input_data['original_full_coloring']
assert valid(O,changed_b,changed_w) and changed_b!=old_b
mutations=[]
def killed(name,detail): mutations.append({'name':name,'detected':True,'witness':detail})
assert any(abs(old_w[a]-old_w[b])==7 for a,b in J['edges'])
assert not (7 < abs(old_w['D']-old_w['U']) <= 13)
killed('exclude_7',{'edge':['D','U'],'colors':[7,14]})
assert abs(old_w['E']-old_b['r'])==13
assert not (7 <= abs(old_w['E']-old_b['r']) < 13)
killed('exclude_13',{'edge':['E','outside_r'],'colors':[15,2]})
assert 14>=7 and 14 not in ADJ[0]
killed('directed_distance_with_no_upper_bound',{'colors':[0,14],'true_distance':6})
cc=boundary(14,0,2,0); refl={k:-v%20 for k,v in cc.items()}; wrong=dict(refl,p=cc['p'])
assert theta_count(O,refl)==0 and theta_count(O,wrong)>0
killed('reflection_fails_to_transform_p',{'correct':refl,'mutant':wrong})
shifted_w={k:(v+1)%20 for k,v in old_w.items()}; shifted_b={k:(v+1)%20 for k,v in old_b.items()}
assert valid(J,shifted_b,shifted_w) and not valid(J,old_b,shifted_w)
killed('translation_moves_internal_colors_only',{'shift':1,'edge':['D','outside_q']})
cc=boundary(2,0,2,0); ww=witness(O,cc)
assert ww is not None and valid(O,cc,ww) and not valid(O,cc,ww,[('p','q')])
killed('ignore_identified_outside_vertex',{'alias':['p','q'],'boundary':cc})
omitted=tuple(sorted(('b','c'))); ww=witness(O,old_b,remove_edge=omitted)
mutant_O=dict(O,edges=[e for e in O['edges'] if tuple(e)!=omitted])
assert ww is not None and valid(mutant_O,old_b,ww) and not valid(O,old_b,ww)
killed('omit_internal_edge_bc',{'boundary':old_b,'mutant_witness':ww})
assert valid(O,changed_b,changed_w) and not valid(O,old_b,changed_w)
killed('silently_change_fixed_boundary',{'required':old_b,'returned':changed_b,'coloring':changed_w})
cc=boundary(0,0,18,0)
assert witness(J,cc) is not None and witness(J,cc,omit_color=19) is None
killed('omit_palette_color_19',{'boundary':cc})
role_witness=None
for d in range(11):
    for z in range(20):
        good=any(y in ADJ[x] and not forbidden(y,x,z) for x in ADJ[0] for y in ADJ[d])
        mutant=any(y in ADJ[x] and not forbidden(x,y,z) for x in ADJ[0] for y in ADJ[d])
        if good!=mutant: role_witness=[d,z,good,mutant];break
    if role_witness is not None:break
assert role_witness is not None
killed('swap_absorption_T_R_roles',role_witness)
# A full witness accepted only when exactly the DU edge is removed.
wrong_map=witness(J,old_b,remove_edge=('D','U'))
mutant_J=dict(J,edges=[e for e in J['edges'] if tuple(e)!=('D','U')])
assert wrong_map and valid(mutant_J,old_b,wrong_map) and not valid(J,old_b,wrong_map)
killed('omit_D_U_check',{'boundary':old_b,'mutant_witness':wrong_map})
# A single altered certificate bit is rejected by the edge-derived mask.
mutant_rows=[x[:] for x in rows]; mutant_rows[0][2]=format(int(rows[0][2],16)^1,'05x')
assert mutant_rows!=rows and int(mutant_rows[0][2],16)!=sum(int(counts[p,0,0]>0)<<p for p in range(20))
killed('certificate_flip_bit',{'row':[0,0],'xor':1})

# Explicit plane embedding, including the repeated pendant outer-face walk.
rotation=input_data['original_pendant_rotation']
darts={(a,b) for a,ns in rotation.items() for b in ns}
assert all((b,a) in darts for a,b in darts)
assert all(len(ns)==len(set(ns)) and a not in ns for a,ns in rotation.items())
assert all(not(set(rotation[a]) & set(rotation[b])) for a,b in darts)
seen=set();faces=[]
for first in sorted(darts):
    if first in seen:continue
    face=[];a,b=first
    while (a,b) not in seen:
        seen.add((a,b));face.append(a)
        ns=rotation[b];a,b=b,ns[(ns.index(a)+1)%len(ns)]
    assert (a,b)==first
    faces.append(face)
assert seen==darts and len(rotation)-len(darts)//2+len(faces)==2
assert max(map(len,rotation.values()))==3
port_names={'p':'P','q':'Q','r':'R','s':'S'}
expected_edges={tuple(e) for e in O['edges']} | {tuple(sorted((v,port_names[t]))) for v,t in O['ports'].items()}
assert expected_edges=={tuple(sorted(e)) for e in darts}
replacement_edge_audit=[]
for a,b in J['edges']:
    replacement_edge_audit.append([a,b,old_w[a],old_w[b],min(abs(old_w[a]-old_w[b]),20-abs(old_w[a]-old_w[b]))])
for a,t in J['ports'].items():
    dd=abs(old_w[a]-old_b[t])
    replacement_edge_audit.append([a,'outside_'+t,old_w[a],old_b[t],min(dd,20-dd)])
# Degree mutation: original Q has two additional leaves. QV adds a forbidden fourth incidence.
old_edges=set(expected_edges)|{('L1','Q'),('L2','Q')}
new_edges={tuple(e) for e in J['edges']}|{tuple(sorted((v,port_names[t]))) for v,t in J['ports'].items()}|{('L1','Q'),('L2','Q'),('Q','V')}
def degrees(ee):
    dd={}
    for a,b in ee:dd[a]=dd.get(a,0)+1;dd[b]=dd.get(b,0)+1
    return dd
assert max(degrees(old_edges).values())==3 and degrees(new_edges)['Q']==4
killed('ignore_degree_growth_QV',{'original_Q_degree':3,'replacement_Q_degree':4,
                               'original_edges':sorted(old_edges),'replacement_edges':sorted(new_edges)})
# Recheck the new universally-quantified unused-p-port refinement directly from edge counts.
q_absorption_bad=[];q_absorption_checks=0
for h in range(11):
    for t in range(20):
        mask=0
        for p in range(20):
            n=sum(theta_count(O,boundary(p,x,0,h)) for x in ADJ[t])
            q_absorption_checks+=1
            assert n or forbidden(t,0,h)
            mask |= int(n==0)<<p
        if mask:q_absorption_bad.append([h,t,format(mask,'05x')])
r_absorption_checks=0
for h in (0,1):
    for t in range(20):
        for p in range(20):
            assert sum(theta_count(O,boundary(p,0,x,h)) for x in ADJ[t])>0
            r_absorption_checks+=1
qr_transfer=[]
for d in range(11):
    bad=[z for z in range(20) if not any(y in ADJ[x] and x!=z for x in ADJ[0] for y in ADJ[d])]
    assert bad==(list(range(20)) if d==0 else [7] if d==1 else [])
    qr_transfer.append([d,bad])
screen=[]
bad_states=[(p,r,h,classification(p,r,h)) for h in range(11) for r in range(20) for p in range(20) if not counts[p,r,h]]
for gg in small_replacements():
    reps={}
    for lab in ('K1','K2','K3','K4'):
        for p,r,h,tag in bad_states:
            if tag!=lab:continue
            cc=boundary(p,0,r,h); ww=witness(gg,cc)
            if ww is not None:
                assert valid(gg,cc,ww);reps[lab]={'boundary':cc,'internal':ww};break
    if len(reps)==4:
        screen.append({'graph':gg,'reason':'each_residual_class_survives','witnesses':reps});continue
    for p,r,h,tag in bad_states:
        if tag!='basic':continue
        cc=boundary(p,0,r,h); ww=witness(gg,cc)
        if ww is not None:
            assert valid(gg,cc,ww)
            screen.append({'graph':gg,'reason':'admits_a_basic_bad_state','witnesses':{'basic':{'boundary':cc,'internal':ww}}});break
    else: raise AssertionError('new replacement found; stop and inspect')
assert len(screen)==71
# Compact certificates bind an index in the deterministic graph family, never just a claimed failure.
compact=[]
for index,entry in enumerate(screen):
    vv=sorted({v for e in entry['graph']['edges'] for v in e})
    ws=[]
    for label,w in entry['witnesses'].items():
        cc=w['boundary'];ws.append([label,cc['p'],cc['r'],cc['s'],[w['internal'][v] for v in vv]])
    compact.append([index,entry['reason'],ws])
for gg,entry in zip(small_replacements(),compact):
    vv=sorted({v for e in gg['edges'] for v in e})
    for label,p,r,h,colors in entry[2]:
        assert valid(gg,boundary(p,0,r,h),dict(zip(vv,colors)))
(ROOT/'replacement-screen.json').write_text(json.dumps({'verdict':'candidate_only',
 'decoding':'Rows [index,reason,witnesses]; graph=index in engine.small_replacements(); witness=[class,p,r,h,colors in sorted internal vertex order], q=0.',
 'not_an_exhaustive_graph_classification':True,'graphs':compact},separators=(',',':'))+'\n')

out={'verdict':'candidate_only','status':'NONTERMINAL_CHECKPOINT','normalized_states_checked':4400,
     'direct_DFS_crosschecks':4400,'boundary_table_rows':220,'unextendible_normalized_states':zero,
     'original_total_inner_completions':sum_counts, 'J_total_inner_completions':20*sum(row[3] for row in rows),
     'J_unextendible_normalized_states':20*sum(row[3]==0 for row in rows),
     'reflection_checks':4400,'translation_by_one_checks':4400,
     'nine_vertex_states_checked':400,'nine_vertex_unextendible_normalized_states':sum(n==0 for row in nine for n in row),
     'nine_vertex_counts_rows_s_columns_t':nine,'absorption':absorption,
     'plane_rotation':rotation,'face_walks':faces,'original_witness_graph_n_m_f':[len(rotation),len(darts)//2,len(faces)],
     'existing_replacement_edge_checks':replacement_edge_audit,
     'extra_port_Q_degree_two_checks':q_absorption_checks,'extra_port_Q_bad_h_t_p_masks':q_absorption_bad,
     'R_degree_two_close_q_s_checks':r_absorption_checks,'QR_edge_transfer':qr_transfer,
     'residual_states':residual,'mutation_tests':mutations,'mutations_detected':len(mutations),
     'replacement_screen_size':len(screen),'uniform_row_eliminations_in_screen':0,
     'm07_local_disagreements':0,'globally_eliminated_residual_classes':[],
     'remaining_residual_classes':['K1','K2','K3','K4'],
     'first_open_boundary':old_b,'trusted_verifier_receipt':False}
(ROOT/'audit.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
print(json.dumps({k:out[k] for k in ('normalized_states_checked','direct_DFS_crosschecks','m07_local_disagreements','mutations_detected','replacement_screen_size','globally_eliminated_residual_classes')},sort_keys=True))
