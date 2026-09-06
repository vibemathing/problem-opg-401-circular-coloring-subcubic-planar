# Exact outside-color obstruction for a pentagon: candidate c05

Status: candidate_only. Primary owner: math-derivation.
Candidate: candidate:opg401-a01-c05-pentagon-boundary.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1.
Target: obligation:opg401-z20-extension. Root: obligation:opg401-root.
Fresh cycle base: ae6daf7c02c8dbd1067d5003e0cfc1306d75584b.

## 1. Frozen boundary extension problem

Let a-u-v-b-z-a be a five-cycle in a graph of the contract class.
Assume u,v have degree two and a,b,z have degree three.
The five-cycle has no chord, since a chord would form a triangle.
Let p,q,r be the colors of the respective outside neighbors of a,b,z.
All outside vertices and their colors are fixed. Recoloring all five
cycle vertices is permitted. The outside coloring is already proper.

The letters p,q,r denote colors, not necessarily distinct vertices.
Coincidences of outside vertices allowed by the graph simply restrict
which triples can be realized; the following classification holds for
all color triples, so does not assume those vertices are distinct.

Use the c01 convention: delta is shortest circular distance on Z20,
A(p)=p+{7,...,13}, and C_k(p)={t:delta(t,p)<=k}.
Use c03: a three-edge path extends exactly when its endpoint colors
are distinct. All conclusions below remain generated candidates.

## 2. Exact criterion for a fixed triple

Choose a prospective color t for z. It must belong to A(r).
The available lists at a,b are
  I=A(p) intersect A(t), J=A(q) intersect A(t).
The path a-u-v-b can then be filled exactly when there exist
x in I and y in J with x!=y. The two remaining cycle edges are
already enforced by membership in A(t).

If p!=q, nonempty I,J always admit distinct choices.
The only way two nonempty lists fail this is when both equal the same
singleton. For fixed t, c01 says a singleton intersection arises only
at p=t+6 or p=t-6, giving respectively {t+13} and {t+7}.
These two singletons are different, so equal singleton lists imply p=q.
It follows that, when p!=q, extension exists exactly when
  A(r) intersect C_6(p) intersect C_6(q) is nonempty.       (E1)

Since Z20 minus C_6(p) is A(p), the failure condition is equivalently
  A(r) is a subset of A(p) union A(q).                     (E2)

If p=q, then I=J and distinct choices exist exactly when its size
is at least two. By c01 this is delta(p,t)<=5.
Thus extension exists exactly when
  A(r) intersect C_5(p) is nonempty.                       (E3)
In this case extension fails exactly when delta(p,r)<=1:
translate p to zero; the complement of C_5(0) is [6,14],
and the seven-consecutive-element set A(r) fits inside it exactly
at r=19,0,1.

Atomic claim: claim:opg401-c05-boundary-criterion.
This is an if-and-only-if result for the specified fixed boundary,
not a theorem of unconditional graph-class reducibility.

## 3. Complete eleven-row symmetry classification

Choose epsilon in {1,-1} so epsilon*(q-p)=d modulo 20,
where d=delta(p,q). Put s=[epsilon*(r-p)]20.
Translations and reflection preserve all relevant edge constraints.
In this normalization p=0,q=d. The table lists exactly the values
of s for which the entire five-cycle cannot be colored while
preserving the outside colors.

| d | Bad s values, in fixed representatives | Number |
|---|---|---|
| 0 | {19,0,1} | 3 |
| 1 | {0,1} | 2 |
| 2 | {0,1,2} | 3 |
| 3 | {0,1,2,3} | 4 |
| 4 | {0,1,2,3,4} | 5 |
| 5 | {0,1,2,3,4,5} | 6 |
| 6 | {0,1,2,3,4,5,6} | 7 |
| 7 | {0,1,2,3,4,5,6,7} | 8 |
| 8 | {0,8} | 2 |
| 9 | {0,9} | 2 |
| 10 | {0,10} | 2 |

For d=0 the reflection choice is immaterial because its bad set is
reflection-invariant; the same is true for d=10. The table therefore
does not depend on a choice in these exceptional symmetry classes.

Derivation for 1<=d<=7:
A(0) union A(d) is the single cyclic interval [7,13+d] modulo 20,
of length 7+d. At d=7 the two intervals are adjacent, with no gap.
A seven-element cyclic interval A(s) is contained in this union
exactly when its starting point s+7 ranges from 7 to 7+d along that
component, which means s in {0,...,d}. This gives E2's failure rows.

Derivation for 8<=d<=10:
A(0) and A(d) form two disjoint components, each of length seven,
with a nonempty gap on both sides. A seven-consecutive-element set
contained in their union cannot cross either gap, and so must equal
one of those components. Hence A(s) equals A(0) or A(d), giving
s=0 or s=d. The d=0 row was proved separately by E3.

Atomic claim: claim:opg401-c05-boundary-table.

## 4. Analytic count and bounded reproduction

For a fixed p, distances d=1,...,9 each occur for two choices of q,
whereas d=0 and d=10 each occur once. The number of bad ordered
pairs (q,r) for that p is therefore
  3 + 2*(2+3+4+5+6+7+8+2+2) + 2 = 83.
Across all 20 choices of p there are exactly 1660 bad ordered
triples and 6340 extendible triples out of 8000.

This is an arithmetic consequence of the hand-derived table,
NOT output of a graph or color enumerator.
Atomic claim: claim:opg401-c05-boundary-count.

A future exact audit can fix p=0, examine the 400 choices (q,r), and
for each examine the twenty choices t for z. For nonempty I,J,
accept if one list has at least two elements or their singleton
elements differ. Each list has at most seven entries.
This bounded check would verify E1-E3 without enumerating all
five-vertex colorings. No such program was run here.

## 5. Explicit attacks and witnesses

The zero triple p=q=r=0 is bad. It is realized by a five-cycle with
one pendant leaf at each of a,b,z, all three leaves precolored zero.
These outside vertices have no mutual edges, so this is a proper
outside coloring. No inside extension exists: a and z would both
belong to A(0)={7,...,13}, while they are adjacent.

The eight-vertex graph itself is colorable. In cycle order a,u,v,b,z
use 0,8,16,4,12, and on the leaves attached to a,b,z use respectively
10,14,2. Every cycle edge has distance eight; leaf edges have distance
ten. This witness negates an unconditional fixed-boundary reduction,
not the ProblemContract.

The exceptional equal-color row is sharp:
p=q=0,r=1 permits only t=14 in C_6(0) intersect A(1).
Both endpoint lists are then {7}, so the three-edge path is blocked.
The r=19 case is its reflection. At p=q=0,r=2 a valid cycle coloring
in order a,u,v,b,z is 7,14,1,8,15. Its cycle-edge distances are
7,7,7,7,8, and all three outside edges are legal.

The phase change between d=7 and d=8 is real. At p=0,q=8,r=4,
the valid cycle coloring 7,0,13,1,14 has edge distances 7,7,8,7,7,
and outside-edge distances 7,7,10. Thus the proposed extension
"every third color on the short arc from p to q is bad" cannot be
continued past d=7.

## 6. Minimal-obstruction interpretation and remaining gap

If a vertex-minimal obstruction contains this five-cycle, then every
coloring of the graph obtained by deleting the five cycle vertices
must induce one of the bad triples in the table. Otherwise this
candidate supplies an extension to the whole graph.

This does not imply the configuration is reducible: the zero-triple
example explicitly shows that some proper outside colorings fail.
A valid further reduction must show that some outside coloring avoids
the listed patterns, or justify recoloring outside the cycle.
The table replaces an unspecified recoloring gap by a finite exact
boundary relation. It makes no assertion that bad triples are
unrealizable in arbitrary graphs of the class.

## 7. Provenance and checkpoint

Generated dependencies at this cycle base:
research/artifacts/candidates/opg401-a01-c01-local-extension.md;
research/artifacts/candidates/opg401-a01-c03-path-sumsets.md;
research/artifacts/candidates/opg401-a01-c04-recoloring.md.
Frozen target: research/records/obligation-graphs.jsonl.
The c01 source/definition note remains applicable. No new external
theorem or novelty claim is a premise. No mathematical command ran.

best_verified_result: none. best_verified_candidate: none.
Best generated material: c01-c05, with fixed-boundary scope explicit.
Open obligations: obligation:opg401-z20-extension; obligation:opg401-root.
Registered failed-route IDs checked: [].
Discarded strengthening: all outside colorings extend over a
five-cycle with precisely two adjacent degree-two vertices.
The eight-vertex witness above is a certificate against that shortcut.
The admitted exact-criterion route remains active.
Next action: derive safe simultaneous recoloring rules for forced
equal-color endpoints and test whether repeated common-neighbor
configurations supply class-preserving reductions.
Future verification needs: kernel_check, axiom_escape_audit,
statement_faithfulness. These artifacts are not verifier receipts.
