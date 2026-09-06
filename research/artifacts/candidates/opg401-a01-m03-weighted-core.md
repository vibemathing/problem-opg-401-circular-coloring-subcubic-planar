# A three-connected weighted core and thirteen unavoidable face types

Status: candidate_only. Primary owner: math-derivation.
Candidate: candidate:opg401-a01-m03-weighted-core.
Problem: problem:opg-401-circular-coloring-subcubic-planar.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1.
Target: obligation:opg401-root.
Local dependency remains open: obligation:opg401-z20-extension.
Cycle base: 14ff31894821f87b620bb83482a73a37deecda47.

## 1. Conditional setting and previously generated inputs

Let G have minimum vertex order among non-(20,7)-colorable finite
simple triangle-free planar subcubic graphs, assuming one exists.
Every smaller graph in this class is colorable.
All structural assertions about G below use this hypothesis.

We use c01/c03's exact path relations: an edge requires circular
distance at least seven, a two-edge path requires distance at most
six, a three-edge path requires unequal colors, and longer paths
have unrestricted endpoints. Write S={7,...,13} in Z20.

The m01 arguments give: G is 2-connected, has no dominated vertex,
no degree-two vertex on a four-cycle, no five-cycle with at least
three degree-two vertices, and is not a cycle. Each maximal thread
has degree-three ends and one, two or three edges. Two three-edge
threads cannot share an end. If a degree-three vertex has two
degree-two neighbors, their other neighbors are distinct and adjacent.
In particular it cannot have three degree-two neighbors.

These are generated proof inputs, not admitted Evidence. This
candidate supplies the further arguments needed to replace m01's
larger unavoidable family by thirteen precise types.

## 2. Tighten a low-degree edge without moving its outside colors

Claim K1 (claim:opg401-m03-tight-edge):
in any (20,7)-colored triangle-free graph H, an edge st with
deg_H(s),deg_H(t)<=2 can be recolored at s,t only so that
delta(phi(s),phi(t))=7.

If both vertices have other neighbors x,y, those neighbors are
distinct because H is triangle-free. The existing colored path
x-s-t-y has three edges, so phi(x)!=phi(y).
The endpoint sums permitting a middle increment of seven or
thirteen are, as integer intervals,
  S+{7}+S=[21,33], S+{13}+S=[27,39].
Their union is [21,39], one representative of every nonzero
residue modulo twenty. It is exactly the endpoint relation of
any three-edge path.

Choose the representative of phi(y)-phi(x) in [21,39]. Choose the
middle increment as seven or thirteen so that the other two
increments have sum in [14,26], and split that sum into two
members of S. This recolors s,t, preserves x,y, and makes the
middle edge have circular distance seven.
When at most one outside neighbor exists, first respect that
neighbor (if present), then choose the other endpoint at difference
seven. These cases also hold with all other colors fixed.

This is a local recoloring claim, not a new graph-colorability
assumption. A middle increment of thirteen has the same shortest
distance seven, so both orientations are handled.

## 3. Complete the two-edge-bond restriction

The exact m01 gluing rule says that two fixed side colorings across
a two-edge cut can be joined by a whole-side translation/reflection
if and only if their endpoint circular distances dA,dB satisfy
|dA-dB|<=6.

For a bond with both sides containing at least two vertices,
m01 further leaves only the case where the internal endpoints
on one side A are adjacent and on the other side B are nonadjacent
with a common neighbor. The four endpoints are distinct within
their respective sides and cofacial in their side embeddings.

Suppose |A|>=3. Color the smaller induced graph on A, and use K1
to make dA=7: each endpoint has lost a cut edge and has degree
at most two on this side. On B, add a new three-edge path between
its two endpoints, using two new vertices. Cofaciality gives a
planar drawing of this added path. It increases each endpoint
degree by one, preserves the subcubic bound, and creates no
triangle. The resulting graph has |B|+2<|G| vertices.

Minimality colors this augmented B. Its endpoint distance dB
is nonzero by the three-edge relation, hence 1<=dB<=10.
Now |7-dB|<=6, so the two side colorings glue, a contradiction.
The auxiliary path is not retained in G.

Therefore |A|=2. Both vertices of A are incident with one cut
edge and with their common internal edge, so both have degree
two in G. A singleton side of a two-edge bond is separately a
degree-two vertex. Since G has no bridge, any two-edge cut that
disconnects G is such a bond.

Claim K2 (claim:opg401-m03-two-edge-cuts):
every two-edge cut of G has a side consisting either of one
degree-two vertex or of two adjacent degree-two vertices.
In particular there is no two-edge cut with a degree-three
vertex on each side.

The strict inequality |B|+2<|G| is essential. The two-vertex side
is not dismissed by applying minimality at the same order.

## 4. The suppressed core is simple and three-connected

Suppress every maximal thread to one edge with weight equal
to its original length, and call the resulting plane graph K.
The vertices of K are the degree-three vertices of G. It is
connected and cubic, and weights lie in {1,2,3}.

There is no loop: a thread returning to its only branch vertex
would make that vertex a cut vertex, unless G were a cycle.
There are no parallel edges. Two parallel threads would have
lengths among the unordered pairs:
1+1 (violates original simplicity), 1+2 (triangle),
1+3 or 2+2 (four-cycle containing degree-two vertices),
2+3 (five-cycle with three degree-two vertices), or
3+3 (two length-three threads sharing an end).
Each possibility was excluded explicitly.

A bridge of K would lift to a bridge of G. A two-edge cut of K
would lift, by cutting one original edge on each affected thread,
to a two-edge cut of G with core vertices on both sides,
contradicting K2. Thus K is three-edge-connected.

For completeness, a simple cubic three-edge-connected graph is
three-vertex-connected here. A cut vertex would leave at least
two components, each needing at least three edges to that vertex,
contradicting degree three. If {x,y} is a two-vertex cut, each
component of K-{x,y} needs at least three attachment edges.
At most six are available, so there are exactly two components,
xy is absent, and each receives exactly three attachments.
Neither component attaches only to x or only to y, since K
is connected and xy is absent (also there is no cut vertex).
The attachment counts are therefore 2+1, in opposite directions.
Taking one component together with the vertex having its two
attachments gives a two-edge cut, a contradiction.

Claim K3 (claim:opg401-m03-core-connectivity):
K is a finite simple three-connected cubic plane graph, with
the stated edge weights. This is a necessary critical structure,
not an assertion that every such weighted graph is uncolorable.

## 5. Two overlapping 122 pentagons are reducible

Consider seven distinct vertices A,B,C,D,u,v,w, with paths
  A-u-B, A-v-C, B-w-D
and edges B-C,A-D. The three internal vertices u,v,w have degree
two; A,B have degree three; C,D have degree at most three.
This is the overlap of two 122 pentagons along the middle
two-edge thread. At most one outside edge meets each of C,D.

Claim K4 (claim:opg401-m03-overlap-reduction):
this configuration cannot occur in G.

First derive its exact terminal relation with C,D colors fixed.
Normalize phi(C)=0, phi(D)=d=delta(phi(C),phi(D))<=10.
Write alpha,beta for the desired A,B colors. The five required
terminal relations are
  delta(alpha,0)<=6, delta(alpha,d)>=7,
  delta(beta,d)<=6, delta(beta,0)>=7,
  delta(alpha,beta)<=6.
The last relation permits filling A-u-B; the first and third
permit filling A-v-C and B-w-D.

For d=0 the first two requirements conflict.
For d=1 the first two force alpha=14, the next two force beta=7,
and their distance seven violates the last requirement.
For 2<=d<=7 take alpha=14, beta=d+6.
For 8<=d<=10 take alpha=d+7, beta=13.
Direct substitution gives all five inequalities in both ranges.
Consequently the exact terminal feasibility is d>=2.

Now delete all seven vertices and color the remaining graph.
If CD is absent, each of C,D has an available list of at least
seven colors: a translate of S or all twenty colors. Choose a
color at C, then a color at D outside its radius-one neighborhood,
which contains only three colors. The terminal distance is at
least two, so the displayed construction fills the configuration
and respects every outside edge.

If CD is present, neither C nor D has an outside neighbor.
Choose C=0,D=7, use the same construction, and also respect CD.
There can be no further unlisted edge among these seven vertices:
A,B and u,v,w are already saturated; CD was handled explicitly.
This proves reducibility, including coincident outside neighbors.
It does not assume arbitrary fixed terminal colors always extend.

## 6. Long edges and length-two components in K

Call a weight-two or weight-three edge long.
No weight-three edge is incident with any other long edge.
Indeed at a common end the near internal vertices of both
threads are degree two. By m01 their next vertices must be adjacent.
For a weight-three thread its next vertex is still degree two
and its remaining neighbor is the far degree-three end.
Thus the other thread would have to be a weight-two thread
with that very far end. This gives parallel edges in K, which
were just excluded. Two weight-three threads are also excluded.

Two incident weight-two edges have their other core ends joined
by a weight-one edge, again by m01's near-vertex fold.
Three successive weight-two edges on a simple four-vertex path
would therefore supply exactly K4's seven-vertex configuration.
A weight-two triangle is impossible, since the forced direct edge
between its far ends would form an original triangle with a
two-edge thread. Longer weight-two cycles contain such a path.

Claim K5 (claim:opg401-m03-long-edge-structure):
weight-three edges form a matching disjoint from all weight-two
edges. Each nonempty component of the weight-two edge subgraph
is a single edge or a two-edge path. The latter closes with a
weight-one edge to a 122 triangle of K.

## 7. The actual thirteen-type unavoidable family

Every triangle of the cubic plane graph K is facial.
There are exactly three edges from its vertices to the outside.
An outside component with just one attachment would give a
bridge. If vertices occupied both sides of the triangle,
there would be at least one component on each side, requiring
at least four attachments in total. Thus one side is empty.

At a vertex with two incident weight-two edges, the empty angle
between them belongs to the forced 122 triangle face; the third
edge is on the other side. Hence a face with at least four
core vertices cannot contain two consecutive long edges.
Weight-three adjacency was excluded in Section 6.

Euler's formula and cubic degree give
                    sum over faces f of (6-|f|)=12.
Faces have simple cyclic boundaries because K is three-connected.
Therefore some face has three, four or five core vertices.
The three-vertex cases are exactly 113 or 122, as in m01.
For a four- or five-face the long edges form a matching.

Up to cyclic rotation and reversal the complete surviving list is:

| core face size | cyclic thread weights | original face length |
|---|---|---|
| 3 | 113 | 5 |
| 3 | 122 | 5 |
| 4 | 1111 | 4 |
| 4 | 2111 | 5 |
| 4 | 2121 | 6 |
| 4 | 2131 | 7 |
| 4 | 3131 | 8 |
| 5 | 11111 | 5 |
| 5 | 21111 | 6 |
| 5 | 31111 | 7 |
| 5 | 21211 | 7 |
| 5 | 21311 | 8 |
| 5 | 31311 | 9 |

The otherwise possible four-face 3111 is excluded by m01 M5:
the length-three thread has a complementary three-edge path.
For each of sizes four and five there is one position class
for a single long edge, and one class for two disjoint long
edges; their unordered weights are 22,23,33. This accounts for
every row without claiming an executed enumeration.

Claim K6 (claim:opg401-m03-thirteen-faces):
a hypothetical minimum obstruction contains one of these thirteen
facial thread patterns. All listed original face lengths are at
most nine, tightening m01's maxima ten and twelve.

## 8. What remains, audits, and checkpoint

K6 is an unavoidable-family theorem, NOT a proof that all thirteen
types are reducible. The all-cubic four- and five-faces are still
present. The 122 table in m02 and the 113 table in c05 keep their
fixed-boundary failures; those failures have not disappeared merely
because the core is now three-connected.

Audit K1's two integer intervals, the strict vertex bound in the
B augmentation, every cut lifting and degree count, the seven-vertex
terminal assignments, and the angle used for the facial triangle.
Only stated small paths and interval arithmetic are used.
No graph enumerator, solver, proof assistant or mathematical runtime
was executed. Text hashing is transport preparation only.

Generated source paths at the cycle base:
research/artifacts/candidates/opg401-a01-c01-local-extension.md;
research/artifacts/candidates/opg401-a01-c03-path-sumsets.md;
research/artifacts/candidates/opg401-a01-c04-recoloring.md;
research/artifacts/candidates/opg401-a01-m01-critical-structure.md;
research/artifacts/candidates/opg401-a01-m02-pentagon-122.md.
The contract, obligation graph and failed-route history remain fixed.
No external structural theorem is used without its argument above.

best_verified_result: none. best_verified_candidate: none.
Open obligations: obligation:opg401-root; obligation:opg401-z20-extension.
Registered failed-route IDs checked: [].
Route status: active; the larger face family has been reduced to
thirteen explicit weighted types, with a three-connected core.
Next action: derive a certifying difference-constraint system for
all-cubic short faces, so each failed boundary has a small explicit
inequality witness and every feasible boundary has a reconstructible
coloring. Then link the remaining 122 faces to those cubic faces.
Requested future capabilities: kernel_check, axiom_escape_audit,
statement_faithfulness. No such receipt or admission is supplied here.
