# Tight-arc recoloring and adjacent-pair restrictions: candidate c06

Status: candidate_only. Primary owner: math-derivation.
Candidate: candidate:opg401-a01-c06-tight-recoloring.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1.
Target: obligation:opg401-z20-extension. Root: obligation:opg401-root.
Fresh cycle base: 663d43cd29bd5b434a0a3f1fc52c3701d4615f41.

## 1. Frozen recoloring operation

For a finite simple graph H with a (20,7)-coloring phi, define D_phi
on V(H) by an arc x->y exactly when xy is an edge and
[phi(y)-phi(x)]20=7. Call these tight arcs. Reverse arcs would have
difference 13, not seven. For X subset V(H), define phi_X by adding
one modulo twenty to all colors in X simultaneously.

Claim T1 (claim:opg401-c06-unit-shift):
phi_X is a (20,7)-coloring if and only if no tight arc leaves X.

To check this, orient each crossing edge from x in X to y outside X.
Its original residue d=[phi(y)-phi(x)]20 lies in [7,13].
Its new residue is d-1 in [6,12], so it is legal exactly when d!=7.
Edges not crossing the cut keep their differences. This proves both
directions, including wraparound, without assuming a linear lift of
the vertex colors. Empty X and X=V(H) are included.

If R(a) is the set reachable from a in D_phi (including a), no arc
leaves R(a). Thus phi_R(a) is always a valid new coloring.
This is a simultaneous operation. It is NOT a claim that its effect
can be realized by changing one vertex at a time.

The general cut-recoloring idea has prior literature; see the source
note. The specialized proof above is explicit, and no source hit is
treated as verification of this candidate.

## 2. Forced equality yields long directed paths

Suppose H has at least one (20,7)-coloring and a!=b satisfy
  phi(a)=phi(b) in every (20,7)-coloring phi of H.          (F)
Claim T2 (claim:opg401-c06-forced-reachability):
for every such coloring, a and b are mutually reachable in D_phi.

If b is not in R(a), shift R(a). The new colors of a,b differ by one,
contradicting F. Interchanging a,b proves the other direction.
There is no restriction to colorings reachable by single-vertex moves
in the quantifier F; the simultaneous coloring is a valid competitor.

Along a directed path of L edges, the endpoint color difference is
7L modulo 20. For a path from a to b under F this is zero, hence
20 divides L because 7 is invertible modulo 20.
A shortest directed path is simple. Since a!=b, its positive length
is at least twenty, so |V(H)|>=21.
These are necessary consequences of F, not converses.

Now let G be a vertex-minimal non-(20,7)-colorable member of the
contract class containing a-u-v-b with deg(u)=deg(v)=2.
Triangle-freeness makes a,b distinct. In H=G-{u,v}, every coloring
has equal colors on a,b, by c03's length-three criterion.
Thus T2 applies. This first gives |V(G)|>=23; Section 4 improves
the bound to 24 by excluding its equality case.

## 3. A theta-shaped configuration is reducible

Claim T3 (claim:opg401-c06-theta-reduction):
a vertex-minimal obstruction cannot have six distinct vertices
a,b,u,v,z,w with the three internally disjoint paths
  a-u-v-b, a-z-b, a-w-b,
where u,v have degree two, a,b have degree three, and z,w have
degree at most three.

All three neighbors of each of a,b are already listed. The vertices
u,v have no other neighbors. Triangle-freeness forbids an edge zw.
Thus z,w each have at most one fixed outside-neighbor constraint.

Delete the six vertices and color the remaining, smaller graph.
The available lists I,J for z,w are either full Z20 or seven-element
cyclic intervals. There exist s in I,t in J with delta(s,t)<=4:
if I has length seven, its radius-four neighborhood is a cyclic
interval of fifteen elements, whose complement has only five;
a list J of at least seven elements cannot avoid it.
If I is full, the assertion is immediate.

By c01, A(s) intersect A(t) has at least three elements.
Choose distinct colors for a,b from that intersection.
The four edges of a-z-b and a-w-b are now proper.
Fill a-u-v-b using c03. All outside incidences of z,w were respected
by the lists; there are no other outside incidences of these six
vertices. This extends the smaller coloring, a contradiction.

The argument allows the two outside neighbors of z,w to coincide;
their fixed colors simply specify the two lists. It does not assume
that arbitrary individually legal lists at all six vertices extend.

## 4. Unique common neighbor and the 24-vertex bound

In the setting of T2's minimal-obstruction application, c03 implies
a,u,v,b lie on a five-cycle, so a,b have a common neighbor in H.
By c04, a,b each have degree three in G and degree two in H.
If they had two distinct common neighbors z,w, T3 would apply.
Therefore they have exactly one common neighbor z.
Their other H-neighbors p and q are distinct vertices. The singleton
pinning in c04 gives phi(p)=phi(q) in every coloring of H: each of
{phi(z),phi(p)} and {phi(z),phi(q)} is {c+7,c+13} with c=phi(a)=phi(b).

Claim T4 (claim:opg401-c06-order-bound):
every vertex-minimal obstruction containing adjacent degree-two
vertices has at least 24 vertices.

Only the case |V(G)|=23 remains after T2. Then |V(H)|=21.
Fix one coloring of H and put phi(a)=phi(b)=c.
A shortest directed a-to-b path has length twenty and uses all
vertices of H. Denote its nineteen internal vertices x1,...,x19.
Their colors are c+7i modulo twenty, one vertex for each residue
different from c; only a and b have color c.

A shortest directed b-to-a path also has positive length divisible
by twenty, hence exactly twenty. Its first internal color must be
c+7, so its first internal vertex is x1; its last internal color
must be c+13, so its last internal vertex is x19.
The first path already has edges a-x1 and b-x19; the reverse-endpoint
path supplies b-x1 and a-x19. Thus a,b have two common neighbors,
contradicting T3. This excludes order 23 and proves T4.

The bound is conditional on the presence of adjacent degree-two
vertices. It is not a lower bound for all possible root obstructions,
and no enumeration of graphs of order at most 23 is claimed.

## 5. Attacks on false converse and sequencing claims

A single edge colored 0,7 shows that shifting an arbitrary subset
is not safe: shifting only its zero-colored endpoint gives distance
six. The no-outgoing-tight-arc condition is indispensable.

Mutual tight reachability in one coloring does not imply F.
Here is a precise counterexample to that converse. Take distinct
vertices a,b,x1,...,x19, edges xi-x(i+1) for 1<=i<19, and the four
edges a-x1,a-x19,b-x1,b-x19.
This is a planar triangle-free subcubic graph. Color a=b=0 and
xi=7i modulo twenty. Both a and b can reach the other by a directed
twenty-edge path in D_phi.

Nevertheless a second valid coloring has a=0,b=1,
xi=10 when i is odd and xi=0 when i is even.
All path edges then have distance ten; b's two incident edges have
distance nine. Thus equality is not forced in all colorings.
This graph also shows why the universal coloring quantifier in T2
must not be replaced by inspection of one coloring.

On a tight directed cycle, no first single vertex can change while
all others retain their colors: its two cycle neighbors have colors
c-7 and c+7 and c01 gives singleton available color {c}.
Yet shifting the entire graph preserves all edge differences.
Thus a successful simultaneous shift need not supply a sequence of
single-vertex recolorings. No such sequencing is used in T2-T4.

## 6. Reproduction, provenance, and checkpoint

Audit crossing-edge residues in T1, the reachability closure in T2,
all outside incidences in T3, and residue uniqueness in T4.
The converse counterexample has an explicit edge list and two
explicit colorings. No graph search, solver, or kernel was executed.

Generated dependencies: c01 local intersections; c03 path criterion
and five-cycle restriction; c04 endpoint pinning.
Source comparison:
research/artifacts/source-notes/opg401-a01-c06-recoloring-source.md.
All original contract hypotheses remain in the graph applications.
The abstract cut criterion itself needs no planarity assumption.

best_verified_result: none. best_verified_candidate: none.
Best generated material: c01-c06.
Open obligations: obligation:opg401-z20-extension; obligation:opg401-root.
Registered failed-route IDs checked: [].
Discarded implications: arbitrary-subset shifts are safe; one
coloring's tight reachability forces equality in every coloring;
simultaneous shifts necessarily admit single-vertex sequencing.
The admitted exact-criterion route remains active.
Next action: prepare a faithful finite formalization of the original
local intersection and extension statement, with explicit separate
kernel and statement-faithfulness verification requests.
