# V16 supplement: exact CSP cores, degree-three rigid signatures, and the first cyclic pressure test

Status: NONTERMINAL_CHECKPOINT. Verdict: candidate_only.
Candidate: candidate:opg401-a01-v16-csp-core-supplement.
Repository: vibemathing/problem-opg-401-circular-coloring-subcubic-planar.
Attempt: attempt:web-20260906-opg401-a01. Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1. Target: obligation:opg401-root.
Read base: a0fcca856e7181091ef3646a5d9810a1e1d0d4a5 (V15/PR39 merged).

This file supplements, and does not replace, `proof.md`.  It attacks V15's
first empty-domain core and pressure-tests the cyclic branch left by the
source-faithful permanent-pin audit.  V03--V15 and the companion V16 proof are
candidate inputs, not Evidence.  No unit-zero-cone, single-hit, global one-class
map, support-cap, or bare-path route is repeated.

## 1. Frozen three-state edge CSP

Use V15's corrected maps `T8,T9,T10`.  For an actual colored edge with colors
`a,b`, retain the exact binary relation

    R(a,b)={(i,j): EdgeOK(T_i(a),T_j(b))},  i,j in {8,9,10}.

A colored length-two path `l-m-r` has an empty middle domain when there is no
single option at `m` supported across both relations.  This is a local
arc-consistency statement; it is not failure of arbitrary recoloring or of the
root problem.

Direct substitution in the three twenty-entry words gives exactly thirty
ordered empty-domain paths, stored in `certificate.json`.  Reversal leaves
fifteen representatives.  Every representative with a degree-two middle can
be removed by changing only the actual middle color; the displayed option
triple then satisfies both CSP edges:

| old path | new middle | states `left,middle,right` (8,9,10 are 0,1,2) |
|---|---:|---|
| `0-8-19` | 7 | `0,0,0` |
| `3-14-6` | 13 | `2,0,0` |
| `4-14-6` | 13 | `1,0,0` |
| `5-14-6` | 13 | `0,0,0` |
| `6-15-7` | 14 | `0,0,0` |
| `6-16-7` | 14 | `0,0,0` |
| `6-17-7` | 14 | `0,0,0` |
| `6-18-7` | 14 | `0,0,0` |
| `6-18-9` | 16 | `1,2,2` |
| `7-19-8` | 0 | `0,0,0` |
| `8-19-9` | 0 | `0,0,1` |
| `13-3-14` | 1 | `0,0,0` |
| `13-4-14` | 1 | `0,0,0` |
| `13-5-14` | 1 | `0,0,0` |
| `14-6-16` | 3 | `1,0,0` |

Reversing a row reverses its state triple.  Each proposed middle color is
adjacent in the original `(20,7)` palette to both unchanged endpoints.  Thus a
raw three-vertex core with a genuinely degree-two middle is not a stable local
obstruction.

## 2. The third incidence is essential: exact degree-three classification

Let `t` be the color of the middle vertex's third neighbor.  A **center-local
repair** is a new middle color `z` and one middle option `i` such that

1. `z` is `(20,7)`-adjacent to all three unchanged leaf colors; and
2. for each leaf separately, some leaf option supports `i` across that actual
   edge.

This is exactly the condition that the middle domain is nonempty when all
three leaf domains are initially full.  It is stronger than merely repairing
the original two-edge path, but still does not solve constraints farther down
the three branches.

There are `30*7=210` ordered path/third-neighbor contexts.  Exactly forty-two
have no center-local repair.  Forgetting which two leaves were first called the
path endpoints leaves the following twenty-one unordered star signatures.
The last two columns give a sharp escape when one indicated leaf has no other
fixed incidence: recolor that leaf, keep the center color, and the listed center
option domain becomes nonempty.

| center | leaf-color multiset | one free-leaf repair | resulting center options |
|---:|---|---|---|
| 3 | `13,14,16` | leaf 1: 13→10 | `0,1` |
| 4 | `13,14,16` | leaf 1: 13→11 | `2` |
| 5 | `13,14,16` | leaf 1: 13→12 | `1` |
| 6 | `13,14,16` | leaf 2: 14→13 | `1,2` |
| 14 | `3,6,7` | leaf 1: 3→1 | `0` |
| 14 | `4,6,7` | leaf 1: 4→1 | `0` |
| 14 | `5,6,7` | leaf 1: 5→1 | `0` |
| 15 | `3,6,7` | leaf 2: 6→2 | `0` |
| 15 | `4,6,7` | leaf 2: 6→2 | `0` |
| 15 | `5,6,7` | leaf 2: 6→2 | `0` |
| 15 | `6,7,8` | leaf 1: 6→2 | `0` |
| 16 | `3,6,7` | leaf 2: 6→3 | `0,1` |
| 16 | `4,6,7` | leaf 2: 6→3 | `0,1` |
| 16 | `5,6,7` | leaf 2: 6→3 | `0,1` |
| 16 | `6,7,8` | leaf 1: 6→3 | `0,1` |
| 17 | `4,6,7` | leaf 2: 6→4 | `2` |
| 17 | `5,6,7` | leaf 2: 6→4 | `2` |
| 17 | `6,7,8` | leaf 1: 6→4 | `2` |
| 18 | `5,6,7` | leaf 2: 6→5 | `1` |
| 18 | `6,7,8` | leaf 1: 6→5 | `1` |
| 19 | `6,7,8` | leaf 2: 7→6 | `1` |

The table is a complete finite certificate, not an extrapolation.  For a hand
check of the first genuinely rigid row, take center `14` and leaves `3,6,7`.
The only colors adjacent to all three leaves are `14,15,16`.  Their option
supports at the three leaves are respectively

    z=14: {9,10}, {8},      {8,9,10};
    z=15: {8,9,10}, {9,10}, {8};
    z=16: {8,9,10}, {10},   {8,9}.

Each row has empty three-way intersection.  Recoloring the leaf `3` to `1`
leaves all three actual star edges legal and gives center option `T8`.

Consequently the tempting strengthening

> every V15 empty path can be destroyed by recoloring its middle, regardless
> of the third subcubic incidence

is false.  The precise minimum counter-signature is the four-vertex star with
center `14` and leaves `3,6,7`; its complete rotation is `center:[leaf3,leaf6,leaf7]`, each leaf:`[center]`. It is a tree and not a root counterexample.  If the repair leaf is pendant, the table unpins the star immediately.  If the repair leaf enters a terminal-free bridge component, the companion V16 bridge-pruning lemma recolors and translates that proper component before installing the table row. Hence a source-faithful stable core must carry the repair obligation into a terminal-to-terminal, cyclic, or multi-attachment branch.  A frozen leaf color by itself is not a contract-level permanent pin.

## 3. First cyclic identity-pin cores under the four-state menu

Now use the companion menu `I,T8,T9,T10`, keep a root of actual color `13`, and ask whether the root can use a nonidentity state on a colored cycle.  The all-identity assignment always colors the actual cycle; root pinning is only a failure of this terminal-switch menu.

The exact rooted census is as follows:

| cycle | valid actual colorings | root pinned | minimum nonroot recolor support |
|---|---:|---:|---|
| C4 | 231 | 27 | all 27 have support 1 |
| C5 | 252 | 180 | 92 support 1; 78 support 2; 10 support 3 |

The support count allows arbitrary new colors on the stated nonroot vertices,, keeps the root color `13`, checks every cycle edge in the actual coloring, and then requires a four-state assignment with nonidentity root.  It is not a statement about external third-neighbor constraints.

Eighteen rooted C5 colorings resist both every one-vertex recoloring and every uniform `+1` or `-1` shift of an arbitrary nonroot subset.  The full list is in the certificate.  A representative is

    13 - 0 - 7 - 15 - 4 - 13.

It has no such one-step repair.  Nevertheless changing the last two nonroot colors `15,4` to `14,1` gives

    13 - 0 - 7 - 14 - 1 - 13,

and states `T8,I,I,I,I` are legal: the actual edge distances are `7,7,7,13,12`, while the output distances are `8,7,7,13,7`.

This freezes an exact failed-route signature:

> a cyclic identity pin is always removed by one vertex recoloring or a uniform unit shift of a nonroot subset.

The signature rejects only that repair portfolio.  It does not reject the explicit two-vertex repair, larger signed moves, branch recoloring, absorption, or the root claim.  The C5 has the standard rotation `v_i:[v_{i-1},v_{i+1}]` and is simple, planar, triangle-free and subcubic. No claim is made that it occurs in the V10 terminal interface.

## 4. Potential and termination boundary

Three independent well-founded processes remain valid:

* V15 domain deletion strictly lowers the sum of CSP domain sizes;
 * the companion V16 bridge pruning strictly lowers the number of vertices in terminal-free bridge components;
 * every finite table lookup and explicit recoloring above terminates after a bounded scan and one complete-vector  adoption.

They do not combine into a global root monovariant.  The C5 signature shows that neither “number of locally pinned vertices” nor availability of a unit shift alone is a sufficient strict potential on cyclic cores.  A future potential must retain at least the terminal block, actual branch attachments, and the full relation-labeled cyclic core.  Failure to find a local repair is therefore an open branch, not a terminal proof.

## 5. O refill audit and dependency DAG

`csp_core_check.py` independently replays the companio terminal table.  If `X` alone uses `T8`, choose `Q=16,R=1`; if `Y alone uses `T8`, choose `Q=0,R=16`.  The four literal O fills in `certificate.json` cover both `p=1` and `=14` and check all nine O edges, four O incidences and four Q/R exterior edges.  Thus every successful unpin above can be composed with an actual terminal fill only after its terminal identity and complete exterior assignment are retained.

Dependency DAG:

    corrected V15 maps
      -> exact two-edge relations
      -> 30 raw path cores
      -> 210 degree-three contexts
      -> 21 rigid star signatures
      -> free-leaf / bridge-transfer consequence;

    identity + corrected maps
      -> terminal T8 rows and O fills
       -> rooted C4/C5 pin census
      -> exact cyclic failed-route signature;

    vertex-minimality + bridge separation
      -> translated component coloring
      -> terminal-free pruning
      -> terminal-to-terminal/cyclic/multi-attachment next core.

## 6. Reproduction, pressure tests, and open scope

Run

    python3 -I -S csp_core_run.py

in this directory.  The checker reconstructs the thirty path cores from the map words, examines all 210 degree-three contexts, regenerates the twenty-one rigid stars and their leaf witnesses, and independently enumerates the rooted C4/C5 cycles.  It also replays the companion identity-pin certificate and four O rows.  Fourteen mutations cover the stale T8 word, omitted third edge, closing-edge omission, wrong root-state convention, cyclic distance endpoints, and the one/unit/two-vertex distinctions.

The recorded CPython run is a candidate-generator computation.  It is not an independent principal, Lean/SMT proof, EvidenceLink, Result, or admission.

closed_residual_classes: [].
open_residual_classes: [C1,C2,C3,C4].
first_open_state: C1(1,0,2,0), with p=14 in the same general bridge.
best_verified_candidate: none. best_verified_result: none.

Next obligation: retain the first actual terminal-to-terminal or cyclic block supporting one of the twenty-one rigid degree-three stars.  Include every third-neighbor branch, chord, repeated endpoint and rotation.  Run the full four-state terminal CSP on that block; if the terminal remains identity-pinned, seek a net-smaller uniformly liftable absorption.  Do not freeze a pendant leaf or a deletion-coloring artifact as a permanent pin, and do not restart single-hit/unit-shift/global-map searches.
