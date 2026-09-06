# The single-ear region: complete boundary table and a constrained replacement

Status: candidate_only. Primary owner: math-derivation.
Candidate: candidate:opg401-a01-m06-single-ear-boundary.
Problem: problem:opg-401-circular-coloring-subcubic-planar.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1.
Target: obligation:opg401-root.
Local dependency remains open: obligation:opg401-z20-extension.
Cycle base: f9c03333f2dcc344fb85b904a7ab9ba0b3b675e6.

## 1. Exact region and normalization

The region has eight distinct vertices: a cubic pentagon
b-c-d-e-f-b and one ear a-u-b-c-v-a. The vertices u,v have degree
two. The other six have degree three. There are no additional
edges within the region. The four outside incidences at a,d,e,f
have fixed colors p,q,r,s, respectively. All outside colors stay
fixed in the local calculation. Repeated outside vertices are
allowed subject to the original graph's simplicity and triangles.

This region arises from m05's carrier theorem. Section 6 checks
that the no-extra-edge assumption and connected outside graph
actually hold in a hypothetical minimum obstruction; they are
not silently presumed from a drawing.

Let delta be shortest distance on Z20 and A(t)=t+{7,...,13}.
Normalize q=0 and s=h=delta(q,s) in {0,...,10} by one common
translation/reflection. The symbols p,r below mean the colors
in these same coordinates. A notation [i,j]_20 is the image of
the inclusive integer interval in Z20.

Claim E1 (claim:opg401-m06-complete-boundary):
the fixed boundary fails to extend exactly in the union of the
basic table and the additional table below.

Basic table: p is unrestricted.

| h | bad r |
|---|---|
| 0 | {19,0,1} |
| 1..7 | {0,1,...,h} |
| 8..10 | {0,h} |

Additional table:

| h | r | bad p |
|---|---|---|
| 0 | 2 | [14,21]_20 |
| 0 | 18 | [19,26]_20 |
| 1 | 19 | [0,7]_20 |
| 1 | 2 | [14,21]_20 |

The additional cases are disjoint from the basic cases.
This classifies every boundary, not just sufficient repair states.
A boundary outside both tables has a reconstructible extension.
No claim of an executed coloring enumeration is involved.

## 2. Reduce to two lists at the central vertex

Write D,E,F for prospective colors at d,e,f.
For a selected E in A(r), define
  I_E=A(q) intersect A(E), J_E=A(s) intersect A(E).
We must choose D in I_E and F in J_E.

Both D,F lie in the same seven-color interval A(E), so their
circular distance is at most six. The remaining ear sees
outside colors p,F,D at a,b,c. The m02 table says:
- D=F never extends;
- delta(D,F)>=2 extends for every p;
- for delta(D,F)=1, failure occurs exactly when
  p in A(D) union A(F).                                 (2.1)

The last identity is m02's eight-element bad arc in a
translation/reflection-invariant form. Therefore the only
additional obstructions beyond the existence of distinct D,F
can occur when every permissible choice has distance one.

## 3. Exact central-color sets for distances at least one and two

Define N_j(q,s) as the E for which I_E,J_E contain a pair D,F
at distance at least j, for j=1,2.

If either list is empty, E is not in N_j. Otherwise translate E
to zero and take the unique signed lifts Q,R of q-E,s-E in [-6,6].
Interchange the two lists if necessary to arrange Q<=R.
They are ordinary integer intervals
  I_Q=[7+max(0,Q),13+min(0,Q)],
  I_R=[7+max(0,R),13+min(0,R)].
The maximum distance between one member of each is
  M=6+min(0,R)-max(0,Q).                                 (3.1)
All colors are in [7,13], so this is an ordinary difference and
cannot wrap. The rightmost point of I_R and leftmost of I_Q
attain M; the opposite choice has no larger separation.

For M>=1, the only failures among nonempty lists are Q=R=6
or Q=R=-6. For M>=2, the failures are that both lifts lie in
{5,6}, or both lie in {-6,-5}.

Let B_j(t) be the radius-j color ball. It follows that
  N_1(q,q)=B_5(q), N_2(q,q)=B_4(q).
When delta(q,s)=1, after q=0,s=1 normalization,
  N_1=[-5,6]_20, N_2=[-4,5]_20.
When delta(q,s)>=2,
  N_1=N_2=B_6(q) intersect B_6(s).                       (3.2)

For the last set, normalize q=0,s=h:
  1<=h<=7: B_6(0) intersect B_6(h)=[h-6,6]_20;
  8<=h<=10: it is [h-6,6] union [14,h+6].
The two pieces in the second row do not wrap. These formulas
check all integer endpoints explicitly.

## 4. Derive the full tables, including the four additional cases

The condition A(r) intersect N_1 empty is exactly the basic table.
For h=0, the complement of B_5(0) is [6,14], which contains a
translate A(r) exactly for r=19,0,1.
For 1<=h<=7, the complement is the cyclic interval [7,h+13]_20;
it contains A(r) exactly for r in [0,h].
For 8<=h<=10 the complement has two seven-color components,
A(0) and A(h), so the only possibilities are r=0,h.

Similarly A(r) intersect N_2 is empty exactly for:
h=0: r in {18,19,0,1,2};
h=1: r in {19,0,1,2};
h>=2: the same basic cases as above.
Indeed the h=0 complement is [5,15], and the h=1 complement is
[6,15]; translate containment gives those two lists.

Consequently, outside the basic obstructions, failure of the
distance-at-least-two repair occurs in exactly the four extra
rows. In those rows every distinct terminal choice is as follows:

| h | r | E | permissible distinct (D,F) |
|---|---|---|---|
| 0 | 2 | 15 | (7,8) or (8,7) |
| 0 | 18 | 5 | (12,13) or (13,12) |
| 1 | 19 | 6 | (13,14) |
| 1 | 2 | 15 | (7,8) |

These values follow by intersecting A(r) with N_1 and then
the displayed intervals I_E,J_E. Formula (2.1) now gives precisely
the additional bad-p arcs in Section 1. Outside the two bad
tables, choose E,D,F in this way, or by an E in A(r) intersect
N_2, and apply m02 to fill the ear. This proves E1 in both
directions and supplies an explicit extension procedure.

For a fixed q there are 83 basic bad pairs (r,s):
3 at s=q, twice sum_(h=1)^7(h+1)=70, eight from h=8,9,
and two from h=10. Each permits all twenty p.
There are six additional actual (r,s) cases before reflection:
two with s=q and two for each neighbor s=q+1,q-1.
Each has eight bad p. Hence the number of bad ordered quadruples is
  20*(83*20+6*8)=34160 out of 20^4=160000.
The extra part has 960 quadruples. These are counts derived
from the proved tables, not observed computer output.

## 5. A smaller five-cycle that narrows, but does not close, the gap

Let H be the deletion of the eight-vertex region. Denote the
outside vertices at a,d,e,f by alpha,delta0,epsilon,phi0,
respectively, to distinguish vertices from their colors p,q,r,s.

Construct J from H by adding five new vertices D0,U,V,F0,E0
forming the cycle D0-U-V-F0-E0-D0. Add the three outside edges
delta0-D0, epsilon-E0, phi0-F0. The outside vertex alpha has
no new incidence. The new region has a three-edge D0-to-F0
path and a two-edge D0-to-F0 path through E0.

Its fixed-boundary relation is exactly A(r) intersect N_1(q,s)
nonempty, because the three-edge path requires D!=F.
Thus it covers the basic table and ignores the four additional
p-dependent cases. This is a statement comparison, not an
unconditional lifting theorem.

Claim E2 (claim:opg401-m06-replacement-rigidity):
for a minimum obstruction G with this carrier, J belongs to
the frozen class, is smaller by three vertices and is colorable.
EVERY coloring of J must give (p,q,r,s) in the additional table.
In particular its delta0,phi0 colors have distance at most one,
and the triple q,r,s lies in an arc of span two with r different
from both q and s and at distance two from at least one.

The new cycle can be drawn inside the deleted two-face disk.
The boundary incidences appear cyclically as alpha,phi0,epsilon,
delta0; after omitting alpha this is compatible with the cyclic
order of the three new outside edges.
The vertices delta0 and epsilon are distinct, as are epsilon
and phi0: equality would already create a triangle on de or ef
in G. Delta0 and phi0 may coincide, because D0,F0 are not adjacent.
These observations exclude new triangles and loops.
Each outside vertex regains no more incidences than it lost;
every new degree is at most three. Planarity and the degree
bound are therefore preserved, including repeated outside vertices.
The order is |G|-8+5=|G|-3, so minimality gives a coloring.

A J coloring cannot induce a basic bad triple because it already
colors the new five-cycle. If its four-color boundary lay outside
the additional table, E1 would extend its restriction on H to G.
Thus all J colorings lie in the stated small family, proving E2.
No particular boundary coloring is claimed obtainable beyond what
the smaller graph and minimality actually supply.

## 6. Why the carrier really has four outside incidences

Claim E3 (claim:opg401-m06-critical-region-shape):
in a minimum obstruction the eight-vertex carrier region has
no extra internal edge and its deletion H is connected.

The only potentially extra edges are among a,d,e,f; all other
vertices are saturated. Edges ad and af create four-cycles
a-v-c-d-a and a-u-b-f-a containing degree-two vertices.
The edge df would create triangle def. These are excluded.
If ae existed, only the third edges at d,f would leave the region.
The outside is nonempty and connected, since a component with
one of these two attachments would give a bridge.
The resulting two-edge bond and m03 force the outside to be
one degree-two vertex or an adjacent degree-two pair, because
the inside contains many degree-three vertices. Then |G|<=10.
But m02 gives |G|>=23 for any minimum obstruction containing
this 122 face. This contradiction excludes ae.

There are now exactly four outside edges. If the deletion were
disconnected, absence of bridges would force exactly two components
with two attachments each. Each is one of m03's one/two-vertex
exceptions. Then |G|<=12, again contradicting m02.
Thus H is connected. The union of the two facial pentagons is
a disk with the simple outer boundary stated in Section 5.

This argument does not assume the four outside vertices are all
distinct. It proves only the properties used in E1/E2.

## 7. A precise failed shortcut and a reusable witness

The claim that every coloring of the smaller five-cycle lifts
to the original single-ear region is false.
Take four distinct isolated outside vertices with boundary
(p,q,r,s)=(0,0,2,0). Color the replacement cycle in order
D0,U,V,F0,E0 by (7,14,1,8,15).
Its cycle edge distances are 7,7,7,7,8, and its three outside
edges have legal differences. The outside alpha color is unused.

This quadruple lies in the first additional row: h=0,r=2 and
p=0 in [14,21]_20. In the original region E must be 15 and
the distinct pair D,F must be 7,8. The m02 bad arc contains zero,
so no extension preserves this boundary.
The witness uses finite triangle-free planar subcubic graphs on
both sides; it is a counterexample only to the fixed-boundary
replacement shortcut, not to the root.

The original region with its four pendant vertices is colorable
after choosing different outside colors. For example use
  a=0,u=11,b=4,c=16,v=7,d=3,e=10,f=17,
and give each pendant vertex the color of its incident region
vertex plus ten modulo twenty. All region and pendant edges
then satisfy the (20,7) rule.

## 8. Sources, certification, and checkpoint

The table is derived by explicit interval endpoints and the exact
m02 relation. The smaller replacement uses the c03 path criterion.
Critical geometry uses m03 and m05, and the already conditional
m02 order bound. These generated dependencies remain candidates.
No external theorem, novelty claim, solver run, graph enumeration,
proof-assistant run or verifier receipt is asserted.
Text serialization and SHA-256 hashing are transport helpers only.

best_verified_result: none. best_verified_candidate: none.
Open obligations: obligation:opg401-root; obligation:opg401-z20-extension.
Registered failed-route IDs last checked: [].
The universal five-cycle replacement is proposed as a failed
subroute with the explicit witness above. The corrected conditional
replacement and exact boundary classification remain active.

Next action: use the four additional signatures to seek a
class-preserving recoloring or a different planar replacement;
do not repeat the disproved universal lifting assertion.
For example, adding the alpha-to-U incidence to the replacement
when it preserves the class narrows every remaining bad state
to phi(alpha)=phi(V), because the length-three path between
consecutive D,F has uniquely determined increments.
This last sentence is a next-target derivation cue, not an
assertion that the extra incidence is always triangle-free.
A bare all-cubic four-face remains a separate unresolved type.
Requested future capabilities: kernel_check, axiom_escape_audit,
statement_faithfulness; trusted verifier suitability and admission
have not occurred.
