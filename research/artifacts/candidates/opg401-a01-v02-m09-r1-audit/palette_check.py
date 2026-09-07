"""Finite palette checks for M09 R1; not a checker for arbitrary plane patches."""
import itertools
import json
from pathlib import Path


def need(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def edge(p: int, q: int, a: int, b: int) -> bool:
    return q <= (b-a) % p <= p-q


def main() -> None:
    data = json.loads(Path('input.json').read_text())
    need(data['projection_source'] == [10,4], 'source palette')
    need(data['projection_target'] == [5,2], 'target palette')
    projection = [i//2 for i in range(10)]
    edge_rows = []
    for i in range(10):
        for r in (4,5,6):
            j = (i+r) % 10
            v = (projection[j]-projection[i]) % 5
            need(v in (2,3), 'projection lost an edge')
            edge_rows.append([i,j,projection[i],projection[j],v])
    homs = []
    for a in itertools.product(range(5), repeat=5):
        if all(edge(5,2,a[i],a[(i+1)%5]) for i in range(5)):
            need(len(set(a)) == 5, 'nonbijective boundary map')
            inverse = {a[i]:i for i in range(5)}
            need(all(inverse[a[i]] == i for i in range(5)), 'inverse identity')
            cyclic_labels = [(3*x)%5 for x in a]
            steps = [(cyclic_labels[(i+1)%5]-cyclic_labels[i])%5 for i in range(5)]
            need(steps == [1]*5 or steps == [4]*5, 'mixed closed five-step walk')
            homs.append(list(a))
    need(len(homs) == 10, 'boundary automorphism count')
    # Existing M09 palette warning: legal C5 precoloring need not extend to K8/3.
    fixed = {0:0,3:12,6:19,1:6,4:13}
    boundary = [0,3,6,1,4]
    need(all(edge(20,7,fixed[boundary[i]],fixed[boundary[(i+1)%5]]) for i in range(5)),
         'warning boundary is invalid')
    edges = [(i,j) for i in range(8) for j in range(i+1,8) if edge(8,3,i,j)]
    completions = 0
    for triple in itertools.product(range(20), repeat=3):
        c = {**fixed, **dict(zip((2,5,7),triple))}
        completions += all(edge(20,7,c[i],c[j]) for i,j in edges)
    need(completions == 0, 'warning unexpectedly extends')
    need(not ((projection[4]-projection[0])%5 in (1,4)), 'target-label mutant')
    shifted = [(2*i+1)%5 for i in range(5)]
    need(shifted in homs and shifted != list(range(5)), 'inverse-omission witness')
    seven_steps = [1,1,1,1,1,1,-1]
    need(sum(seven_steps)%5 == 0 and len(set(seven_steps)) == 2, 'length-seven warning')
    report = {'verdict':'candidate_only','projection':projection,
              'directed_edges_checked':30,'projection_edge_rows':edge_rows,
              'boundary_maps_examined':3125,'boundary_homomorphisms':homs,
              'all_boundary_homomorphisms_bijective':True,'inverse_identity_checks':50,
              'palette_warning_assignments_checked':8000,'palette_warning_completions':completions,
              'negative_controls':{'wrong_target_cycle_labeling':[0,4,0,2],
                                   'omitted_boundary_inverse':shifted,
                                   'seven_step_generalization':seven_steps},
              'arbitrary_patch_enumeration':False,'trusted_verifier_receipt':False}
    out = (json.dumps(report,separators=(',',':'))+'\n').encode()
    need(len(out)<=65536,'output cap')
    Path('palette-audit.json').write_bytes(out)
    print(json.dumps({'directed_edges':30,'boundary_maps':3125,'automorphisms':len(homs),
                      'warning_trials':8000,'warning_completions':completions}))


if __name__ == '__main__':
    main()
