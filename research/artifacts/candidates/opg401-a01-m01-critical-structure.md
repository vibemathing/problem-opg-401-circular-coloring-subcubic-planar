# Minimal-obstruction structure and the discharging interface: m01

Status: candidate_only. Primary owner: math-derivation.
Candidate: candidate:opg401-a01-m01-critical-structure.
Problem: problem:opg-401-circular-coloring-subcubic-planar.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1.
Current target: obligation:opg401-root.
Local dependency remains open: obligation:opg401-z20-extension.
Cycle base: 6d62002c3d9a88823fa0dd76f99ae16f5aa32b24.

## 1. Conditional setting and the role of this candidate

Let C be the frozen class of finite simple triangle-free planar graphs
of maximum degree at most three. Suppose a member without a
(20,7)-coloring exists, and let G have minimum vertex order among
such members. Every smaller member of C is therefore colorable.
All conclusions about G below are conditional on this minimality.

Use the fixed Z20 definitions of c01. Write delta for shortest
circular distance, A(a)=a+{7,...,13}, and B6(a)=Z20 minus A(a).
The path relations from c03 are R1: delta>=7, R2: delta<=6,
R3: unequal colors, and unrestricted endpoints for length >=4.
These are generated inputs with their explicit proofs, not Evidence.

The purpose is to organize an unavoidable-configuration argument.
The endpoint of this note is a finite family of still-open face
patterns, NOT a contradiction or a proof of the root.

## 2. Connectivity and copying a dominated vertex

Claim M1: G is connected, has minimum degree at least two, has no
bridge or cut vertex, and is not a cycle.

Disconnected components are smaller and their colorings unite.
The degree-zero/one extension and cycle case are supplied by
c01/c03. For a cut vertex z, color each component of G-z together
with z, and translate its colors to give z the same color in all
pieces. All edges lie in pieces, so these colorings glue.
For a bridge xy, color its two sides and translate one side to
make the colors at x,y differ by ten. This also glues.
The pieces are smaller members of C. In particular G is
2-connected, and its facial boundaries in a plane embedding are cycles.

Claim M2: there are no distinct nonadjacent vertices v,z with
N(v) subset N(z). Indeed color G-v and copy the color of z to v.
For each neighbor x of v the edge zx already guarantees the
required color relation. No old color is changed.

Consequences:
(a) No four-cycle of G contains a degree-two vertex. The opposite
vertex is a permissible z in M2. This is stronger than the
conditional quotient consequence in c02 and needs no five-cycle
exception.
(b) No K2,3 configuration occurs. In a subcubic graph its two poles
have the same three neighbors, and hence are twins covered by M2.
This simplifies the minimal-obstruction consequence of g01; it
does not replace g01's stronger five-vertex-deletion statement.
(c) On a four-cycle all four vertices have degree three, and their
four outside neighbors are distinct. Adjacent coincidences would
give a triangle; opposite coincidences would give a K2,3.

## 3. Threads and two further reductions

A thread is a maximal path with degree-two internal vertices and
degree-three ends. By M1 its ends are distinct: a closed thread
with one branch vertex would make that branch vertex a cut vertex,
unless the whole graph were a cycle. By c03 every thread has
length one, two or three.

Claim M3: two length-three threads cannot share a degree-three end.
Write them v-u1-u2-a and v-w1-w2-b. Their four internal vertices
are distinct and have degree two. Delete those four vertices.
In the smaller graph v has only its third neighbor t. Color that
graph, and recolor v within A(phi(t)), avoiding phi(a),phi(b).
There are seven choices before at most two exclusions.
The endpoint colors of both missing paths are now unequal, so
R3 fills them. No other edge touches a deleted vertex.
The proof permits a=b. Thus length-three edges form a matching
in the cubic multigraph obtained by suppressing degree-two vertices.

Claim M4: if a degree-three vertex c has two degree-two neighbors
v,w, whose other neighbors are b,d, then b,d are distinct and
adjacent. Distinctness follows from M2 applied to the four-cycle
that b=d would create.

Suppose bd were absent. Identify v,w to h and suppress the two
parallel edges hc to one. The new neighborhood of h is {b,c,d}.
The degree of c decreases by one and all other degrees do not
increase. A new triangle would have to contain h and an edge
between two of b,c,d. The edges bc,cd are already forbidden by
the original triangles b-v-c-b and c-w-d-c; bd is absent by
assumption. Hence the new simple graph is triangle-free.

For the planarity step, choose the angle between cv,cw not
containing the third edge at c. The boundary segment v-c-w is
incident with a face there. Add an auxiliary edge vw very close
to that segment in the face, then contract the added edge.
After parallel-edge suppression the result is exactly the graph
just described. This is only a construction proving planarity;
the auxiliary triangle is not being asserted to lie in C.
The resulting graph has one fewer vertex and does lie in C.
Color it, then give v and w the color of h. Every original edge
is respected. This contradicts minimality and proves M4.

Thus c-v-b-d-w-c is a five-cycle. A degree-three vertex cannot
have three degree-two neighbors: their other ends would be
distinct by M2 and pairwise adjacent by M4, giving a triangle.

Claim M5: no six-cycle contains two adjacent degree-two vertices.
Deleting that pair leaves a three-edge path between the two
exterior endpoints. R3 forces those endpoints to have different
colors, and the missing three-edge thread can then be restored.
More generally a length-three thread is redundant whenever its
ends are joined outside it by a path of length one or three.

## 4. Exact two-edge-cut gluing and the residual cut type

Let two edges a1b1,a2b2 be all edges between two nonempty parts A,B.
Fix colorings f,g of the two induced sides. Put
dA=delta(f(a1),f(a2)), dB=delta(g(b1),g(b2)).
Claim M6: these colorings can be glued after a translation and
possibly a reflection of the entire B side exactly when
                         |dA-dB| <= 6.

For a chosen reflection sign epsilon, the translation t must lie
in the two allowed sets centered at
f(a1)-epsilon*g(b1) and f(a2)-epsilon*g(b2).
By c01 their intersection is nonempty exactly when the distance
between these centers is at most six.
Normalize the signed endpoint differences to dA,dB in [0,10].
The smaller of the distances for the two signs is |dA-dB|:
the other candidate is min(dA+dB,20-dA-dB), and both terms
are at least |dA-dB| because dA,dB<=10. This proves both directions.

Taking the attainable distance sets of the two sides makes this
an exact finite boundary-state rule. It does NOT say that every
pair of side colorings glues. For a two-VERTEX separator, the
corresponding rotation/reflection rule instead requires equality
of the two shared-vertex distances, hence intersection of the
two distance spectra; do not substitute the six-unit tolerance.

Now suppose the two cut edges are a bond in G and each side
contains at least two vertices. Then the two endpoints on each
side are distinct. If, for example, a1=a2=a, the connected A side
would have only one edge from a to the rest of A by the degree
bound, and that edge would be a bridge of G, contrary to M1.

The endpoint pair on each side is cofacial in its inherited
embedding: a path through the connected opposite side, together
with the two cut edges, supplies a curve outside the side joining
the endpoints.

If both pairs are nonadjacent, add a fresh vertex joined to the
two endpoints on each side. Each augmented side remains planar,
triangle-free and subcubic, and is smaller than G because the
opposite side has at least two vertices. Minimality gives
colorings with dA,dB<=6, which glue by M6.

If both pairs are adjacent, color the sides directly. Both
distances are in [7,10], so M6 glues them.

If one pair is adjacent and the other is nonadjacent without a
common neighbor in its own side, add the edge between that other
pair. Cofaciality supplies planarity, the cut leaves degree
capacity, and absence of a common neighbor excludes a new
triangle. Again both colored distances lie in [7,10] and glue.

Consequently a nontrivial two-edge bond in G must have internal
endpoint distances exactly one and two on its two sides.
The edge on one side, the two-edge path on the other, and the
two cut edges form a five-cycle. This is a residual obstruction
type, not an assertion that all two-edge cuts are reducible.
Singleton degree-two sides were explicitly excluded from this
classification and remain governed by c01.

## 5. Unavoidable faces after moving the degree-two charges

Fix a plane embedding of G. For a face f let k(f) count its
degree-three vertices. Start with charge 2*deg(v)-6 at vertices
and length(f)-6 at faces. Their total is -12 by Euler's formula.

Move the charge -2 of each degree-two vertex equally to its two
incident faces. All vertex charges become zero. The resulting
face charge is
       length(f)-6-(number of degree-two vertices on f)
                         = k(f)-6.
Hence the exact identity is
                         sum_f (6-k(f)) = 12.             (1)
Faces are counted with their embedding incidences. M1 ensures
their boundaries are cycles, so no hidden repeated-vertex
convention is required here.

There is no cycle with only zero or one degree-three vertex,
by connectedness, the cycle case and the cut-vertex exclusion.
A cycle with two degree-three vertices consists of two threads.
Lengths 1+2 give a triangle; 1+3 or 2+2 give a four-cycle with
degree-two vertices; 2+3 gives a five-cycle with three degree-two
vertices, excluded by c04; 3+3 violates M3. A pair 1+1 would
require parallel edges in the original simple graph.

For a cycle with exactly three degree-three vertices, classify
the three thread lengths up to order. The only surviving types
are (1,1,3) and (1,2,2), both five-cycles with two degree-two
vertices:
- (1,1,1) is a triangle; (1,1,2) is a forbidden four-cycle.
- (1,2,3) is excluded by M5.
- (2,2,2) is excluded by M4: the forced edge between two
  far ends makes a triangle with the third length-two thread.
- (2,2,3) is excluded by M4 and M2: the forced edge closes
  a four-cycle with the length-three thread.
- All types with two or three length-three threads violate M3.

Claim M7: equation (1) forces a face in one of the following
still-open classes:
(i) a five-face with two degree-two vertices, adjacent or not;
(ii) a face with four degree-three vertices and thread lengths
     in {1,2,3}, with the length-three threads nonincident;
(iii) the analogous face with five degree-three vertices.
For k=4 or 5, at most floor(k/2) boundary threads have length
three. Thus the original face length is at most
2k+floor(k/2): at most ten in (ii) and twelve in (iii).

This is a genuine unavoidable-family reduction, but not a
closed unavoidable-plus-reducible proof. In particular it
contains the all-cubic four-face and all-cubic five-face.
These must not be omitted because earlier work emphasized
degree-two configurations.

## 6. Precise failure of the old structural-only closure

Claim M8: the older degree-two exclusions, the K2,3 exclusion,
connectivity restrictions, and Euler charge accounting alone
are consistent with a graph in C.

A witness is the pentagonal prism on ti,bi for i modulo five:
edges ti-t(i+1), bi-b(i+1), ti-bi.
Draw two nested pentagons with matching radial edges. It is
simple, planar, cubic and triangle-free, with five square faces
and two pentagonal faces. It has no cut vertex: deleting one
vertex leaves one intact pentagon and each remaining vertex
of the other attached to it. Every edge lies on a cycle, so
there is no bridge. A K2,3 would require equal three-neighbor
sets, impossible from these displayed prism neighborhoods.
All degree-two exclusions are vacuous.

The old face charges sum to 5*(-2)+2*(-1)=-12. There is no
contradiction. This graph is NOT a counterexample to the root:
an explicit coloring is
              phi(ti)=8i, phi(bi)=8i+10 modulo twenty.
Cycle edges have distance eight, including the wrap, and
rungs have distance ten.

This witness rejects only the shortcut that the previous
structural exclusions themselves already force a contradiction.
It does not reject discharging with additional reductions.

## 7. Sources, audits and next actual obstruction

Generated sources at the cycle base:
c01-local-extension, c03-path-sumsets, c04-recoloring,
c06-tight-recoloring and g01-planar-k23 under
research/artifacts/candidates/opg401-a01-*.md.
The frozen contract, graph and failed-route ledger were read.
No new external theorem is needed for M1-M8.

Audit the color-copy condition, the angle used in M4, every
degree change, the exact two-cut quantifiers, both size bounds
on the augmented sides, and the incidence count in (1).
No mathematical enumeration, solver or proof assistant was run.
Content hashing is transport preparation, not verification.

best_verified_result: none. best_verified_candidate: none.
Best generated new object: the minimal-obstruction system M1-M7.
Open obligations: obligation:opg401-root and
obligation:opg401-z20-extension.
Registered failed-route IDs checked: [].
Discarded shortcut: old local exclusions already close Euler.
Next action: classify the (1,2,2) pentagon boundary exactly and
then use the all-cubic four-face boundary relation to attack
classes (i)-(iii), rather than adding an unrelated local lemma.
The conditional deductions and the prism witness require the
registered kernel/axiom/faithfulness gates before any admission.
