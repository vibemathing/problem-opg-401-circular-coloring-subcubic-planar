# Pentagon clusters: connected boundaries, cubic carriers, and a two-ear reduction

Status: candidate_only. Primary owner: math-derivation.
Candidate: candidate:opg401-a01-m05-pentagon-clusters.
Problem: problem:opg-401-circular-coloring-subcubic-planar.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1.
Target: obligation:opg401-root.
Local dependency remains open: obligation:opg401-z20-extension.
Cycle base: 88a42d5c35568268e15cda980a81919432d753dd.

## 1. Frozen critical setting and scope

Let G be a minimum-order non-(20,7)-colorable graph in the frozen
finite simple triangle-free planar subcubic class, assuming one exists.
Fix a plane embedding and the simple three-connected cubic core K
obtained by suppressing threads, as derived in m03.
All structural conclusions below are conditional on this minimum G.

Use shortest circular distance delta on Z20 and A(t)=t+{7,...,13}.
A two-edge thread can be filled exactly when its endpoint distance
is at most six. The c01 proof of this statement is retained as a
generated dependency, not as an admitted EvidenceLink.

A 122 face means a pentagon a-u-b-c-v-a with u,v of degree two
and a,b,c of degree three. Its core triangle has one weight-one
edge bc and two weight-two edges. We call this a 122 ear on bc
when describing it together with a neighboring face.
An all-cubic cycle has degree three at every one of its vertices
in G; it is not merely a cycle in the suppressed core.

## 2. Every face in the thirteen-type family has a connected deletion

Claim C1 (claim:opg401-m05-connected-face-deletion):
deleting all vertices of any expanded face in m03's thirteen-type
family leaves a nonempty connected graph.

The core face has k in {3,4,5} branch vertices. Its boundary is
induced, as in m04's planar two-cut argument. Each branch vertex
therefore contributes exactly one edge to the outside; internal
thread vertices contribute none. There are k attachment edges.

An outside component with just one attachment would make that
attachment a bridge. A component with exactly two attachments
forms a two-edge bond: its complement is connected through the
face and the other components. By m03 it must consist of one
degree-two vertex or two adjacent degree-two vertices, because
the complement contains branch vertices.
It would therefore give an outside thread joining two vertices
of the core face. Equal ends violate the subcubic bound; adjacent
ends give parallel core edges, and other ends give a core chord.
All possibilities are excluded by core simplicity and the induced
face boundary.

Every outside component must thus have at least three attachments.
Since k<=5 there is at most one, and there is at least one because
each core face vertex has its third incident edge outside the face.
This proves C1.

Consequently the whole-component rotations of g01 do not supply
separate adjustable boundary groups for these particular deletions.
There is only one outside component. A translation or reflection
of every outside color preserves extension feasibility, by applying
the same palette automorphism to a proposed extension and its inverse.
This observation does not prohibit internal recoloring of that
component; it identifies the operation that cannot change a bad state.

## 3. Every all-cubic four- or five-cycle is facial

Claim C2 (claim:opg401-m05-short-cubic-cycle-facial):
an all-cubic cycle of length four or five in G bounds a face, and
deleting its vertices leaves a nonempty connected graph.

The cycle has no chord, since a chord would create a triangle.
An outside component has at least two attachments, by absence of
bridges. Suppose it has exactly two. By m03 it is a single degree-two
vertex or an adjacent degree-two pair, joining two distinct cycle
vertices by a thread of length two or three.

A length-two thread creates either a triangle or a four-cycle
containing its degree-two vertex: on C4 or C5 the shorter cycle
arc between its ends has length one or two.
For a length-three thread whose ends are adjacent, there is again
a four-cycle containing degree-two vertices.
For nonadjacent ends on C5, the other cycle arc has length three;
together they form a six-cycle with adjacent degree-two vertices,
excluded by the alternate-three-edge-path argument in m01.
For opposite ends on C4, the cycle supplies two internally disjoint
two-edge paths and the added thread supplies a three-edge path.
This is precisely the reducible theta (3,2,2) of c06.
Thus no outside component has only two attachments.

There are only four or five total attachments. Every component
now needs at least three, so the deletion is connected and nonempty.
A connected graph drawn disjointly from a Jordan cycle lies entirely
on one side. Hence the other side of the cycle is empty and is a face.
This proves C2 without presuming that an arbitrary short cycle is facial.

## 4. The external pentagon forced by a 122 face is all cubic

For a 122 face a-u-b-c-v-a, let alpha,beta,gamma be the outside
neighbors of a,b,c and let H be the deletion of the five face vertices.
m02 proves these outside vertices are distinct, H is connected,
beta,gamma are nonadjacent with a common neighbor z in H, and

  delta(phi(beta),phi(gamma))<=1 for every (20,7)-coloring phi of H. (4.1)

Claim C3 (claim:opg401-m05-cubic-carrier):
beta,gamma,z all have degree three in G. Thus b-beta-z-gamma-c-b
is an all-cubic pentagon face, on the other side of bc.

If beta had degree two in G, it would have degree one in H.
Holding all other H colors fixed would leave seven choices at beta;
at most three lie at distance at most one from the fixed gamma color.
Choosing another would contradict (4.1). The same argument applies
to gamma. Their degrees are therefore three.

Suppose z has degree two, so its neighbors are exactly beta,gamma.
Fix any coloring of H and write c=phi(beta), d=phi(gamma).
The available list at z is I=A(c) intersect A(d). By (4.1) it is
an interval of at least six colors inside the seven-color A(c).
Let t be beta's other H-neighbor and h=phi(t), which belongs to A(c).
There exists z' in I with delta(z',h)<=1: an interval of six or
seven in this seven-color interval omits at most an end color.
Recolor z by z'. This still respects its edges to beta and gamma.
The available list at beta is now A(z') intersect A(h), of size
at least six. Choose a member outside the three-color radius-one
neighborhood of d. Recoloring beta to it preserves every H edge
and violates (4.1), a contradiction.

Minimum degree is at least two, so z must have degree three.
The five vertices of b-beta-z-gamma-c-b are distinct by their
construction in m02. Apply C2: this all-cubic pentagon is facial.
Its interior side cannot be the already existing 122 face, so it
is the other face incident with bc. Each 122 face thus has a unique
all-cubic pentagon carrier.

## 5. Two 122 ears on one cubic pentagon are reducible

Claim C4 (claim:opg401-m05-double-ear-reduction):
an all-cubic pentagon in G cannot have two 122 ears.

First the two attachment edges cannot be consecutive on the
pentagon. At their common vertex there is only one off-pentagon
edge. The degree-two neighbor and its other neighbor then force
the two ear apices to be identical. That apex would have three
degree-two neighbors, excluded by m01. Thus ear attachment edges
form a matching. A pentagon has at most two disjoint edges of
a matching, so it remains to exclude exactly two.

Label the cubic pentagon b-c-d-e-f-b and the ears
  a-u-b-c-v-a and g-x-d-e-y-g.
The eleven vertices are distinct: a shared apex would need four
degree-two neighbors for disjoint attachment edges; shared internal
vertices would violate their degree-two incidences; and an apex
on the pentagon would give a core chord. The known edges saturate
b,c,d,e and u,v,x,y. Only a,g,f can have additional incidences.

The possible additional edges among these three are excluded in G.
An edge af creates the four-cycle a-u-b-f-a containing u of degree
two. An edge gf creates g-y-e-f-g containing y of degree two.
If ag existed, a and g would have no outside edge, leaving only
the third edge at f to attach this region to the rest of G.
That edge would be a bridge. It really must leave the region,
since af and gf are already excluded and every other vertex is
saturated. Therefore ag is also impossible.

Delete the eleven vertices and color the remaining, smaller graph.
Let p,q,r be the fixed outside colors adjacent to a,g,f, respectively.
The outside vertices may coincide; no distinctness is assumed here.
Choose F in A(r), and choose G0 in A(q) different from F.
There are at least six choices for the latter. Normalize this
ordered pair by a common translation/reflection of palette coordinates:
F=0 and G0=h with 1<=h<=10. The outside color p transforms with
the coordinates; no actual outside color is being changed.

Choose the prospective colors D at d and E at e by this small table:

| h | D | E |
|---|---|---|
| 1..4 | h+14 | 7 |
| 5..8 | 2 | 9 |
| 9..10 | 4 | 11 |

In every row,
  delta(G0,D)<=6, delta(G0,E)<=6,
  delta(D,E)>=7, delta(E,F)>=7, and delta(D,F)>=2.        (5.1)

For the first row the relevant distances are respectively
6, 7-h, min(h+7,13-h), 7, and 6-h.
For the second row they are h-2, 9-h, 7, 9, and 2.
For the third row they are h-4, 11-h, 7, 9, and 4.
All lie in the required ranges. Fill g-x-d and g-y-e using c01.
The assigned colors at g and f respect their outside neighbors.

Now the still uncolored 122 pentagon a-u-b-c-v-a has outside
colors p,F,D at a,b,c. The last inequality of (5.1) lets us apply
m02: when delta(F,D)>=2, EVERY p admits an extension.
Complete that pentagon, and invert the palette coordinate change.
This gives a coloring of G preserving the original outside coloring,
a contradiction. The displayed construction supplies the whole
eleven-vertex reduction, not merely a test of selected boundary states.

## 6. An injective carrier map and its exact charge implication

Claim C5 (claim:opg401-m05-carrier-count):
if F122 counts the 122 faces and F5c counts the all-cubic pentagon
faces in G, then F122<=F5c.

Map each 122 face to the unique carrier from C3. Claim C4 says
no carrier has two preimages, so the map is injective.
This includes every 122 face, not just a disjoint subcollection.

In the suppressed cubic core, a 122 face is a triangle and has
Euler curvature 6-3=3. Its all-cubic pentagon carrier has curvature
6-5=1. Thus each occupied carrier pair is a cluster of curvature
four. An unoccupied cubic pentagon contributes one.
These equalities do not contradict total curvature twelve:
the clusters still have positive curvature. The missing step is
a new reduction or charge-transfer argument for the one-ear
cluster or remaining cubic short faces, not a claim that the
inequality alone closes discharging.

The smallest unresolved occupied carrier region has eight
vertices: one cubic pentagon and one 122 ear. It must not be
declared reducible from the eleven-vertex argument by deleting
one of the two ears, since the proof used the freedom to choose
G0 from its outside list.

## 7. Audits, provenance, and checkpoint

Audit the two-edge-bond exceptions in C1/C2, the six-color lists
in C3, every potential extra edge in C4, and all three rows of
(5.1). The normalization in C4 is only a change of coordinates;
the outside coloring is preserved after inversion.
No graph enumerator, solver, compiler or mathematical runtime
was executed. These are hand derivations; text hashing is only
transport preparation. No novelty claim is made.

Generated dependencies at the cycle base:
c01 (exact two-edge relation), c06 (theta reduction), m01
(short-cycle exclusions), m02 (122 table and external pair),
m03 (two-edge cuts and core), m04 (induced face boundaries).
All remain candidate inputs. No truth ledger is modified.

best_verified_result: none. best_verified_candidate: none.
Open obligations: obligation:opg401-root; obligation:opg401-z20-extension.
Registered failed-route IDs last checked: [].
The m04 winding-only failed-route proposal remains a proposal,
not an admitted record. No new verifier or evidence status is implied.

Next action: attack the one-ear eight-vertex carrier cluster using
the exact m02/m04 boundary relations and class-preserving replacements
or internal recoloring of its connected outside graph. A bare cubic
four-face also remains a priority. Do not repeat separate-component
rotations for a deletion proved connected in C1.
Requested future capabilities: kernel_check, axiom_escape_audit,
statement_faithfulness, subject to trusted verifier-policy suitability.
