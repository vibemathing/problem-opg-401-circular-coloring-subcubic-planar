# Pentagonal patch retraction and exclusion of the six-terminal odd-cycle signature

Status: candidate_only. Transport status: working draft for a subsequent immutable packet.
Primary owner: math-derivation.
Candidate: candidate:opg401-a01-m09-pentagonal-retraction-draft.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1.
Target: obligation:opg401-root.
Local dependency remains open: obligation:opg401-z20-extension.
No completed transport, mathematical execution, verifier receipt or root closure is asserted.

## 1. A boundary-preserving theorem, not arbitrary-boundary wishful thinking

Let P be a finite connected simple triangle-free plane graph whose outer boundary is a five-cycle C. Suppose exactly one of its internal faces has odd length. There are therefore exactly two odd faces when the outer face is counted.

Claim R1 (claim:opg401-m09-pentagonal-retraction):
There is a graph homomorphism rho:P->C whose restriction to C is the identity. Consequently every homomorphism of C into any target graph extends over P by composition. In particular every fixed (20,7)-coloring of C extends, with every boundary color unchanged.

By m05's fully derived two-odd-face theorem, P has a (10,4)-coloring. Map a palette representative i in {0,...,9} to floor(i/2) modulo five. Extend the floor expression by eta(i+10)=eta(i)+5 when checking wrapped edges. A legal difference four, five or six maps to a difference two or three modulo five. These are exactly the edges of a five-cycle target K_(5/2).

This supplies a homomorphism g:P->K_(5/2). Its restriction to the boundary five-cycle must be an isomorphism. Indeed, after relabeling the target cycle in cyclic order, each boundary step is +1 or -1. Five such steps form a closed walk, so their odd sum is a multiple of five. The only possibilities are +5 and -5, requiring all five steps to have the same sign. Thus the boundary map is bijective and preserves the cyclic order up to reversal.

Compose g with the inverse of this boundary isomorphism. The resulting rho fixes each vertex of C. Composing rho with any prescribed coloring of C proves the extension statement. The proof has not replaced a fixed boundary coloring by an arbitrary one: it constructs a retraction that works for all of them.

For comparison, a triangle-free plane patch with outer four-cycle and no odd internal face is bipartite. It retracts to that four-cycle K2,2: preserve its four boundary vertices and map every other vertex to a fixed boundary representative in its own bipartition class. Every cross-class pair of the four-cycle is an edge. This gives the analogous arbitrary-boundary extension for that even patch.

## 2. Consequences for a hypothetical minimal obstruction

Let G have minimum vertex order among non-(20,7)-colorable graphs of the frozen class, with a fixed plane embedding. It is connected and has minimum degree at least two by m01.

Claim R2 (claim:opg401-m09-one-odd-patch-exclusion):
A disk bounded by a five-cycle and containing exactly one odd face cannot contain any vertices strictly inside it. Thus it is a single pentagonal face.

Otherwise delete the strict interior vertices and color the smaller graph by minimality. The retained boundary is already colored. R1 extends that exact boundary coloring across the deleted patch. No edge joins a strict interior vertex to the exterior except through the boundary, so this colors G, a contradiction. If the disk has no strict interior vertices, it also has no chord: every chord of a five-cycle creates a triangle. Therefore it is one face.

Every separating five-cycle whose two sides contain vertices must consequently have at least three odd faces on each side: boundary parity makes each side's odd-face count odd, and the one-odd-face case is excluded. The corresponding four-cycle statement is that a nonempty side cannot have zero odd faces, by the bipartite-patch retraction; its odd-face count is even and hence at least two.

These are specific universal extension theorems for the stated patches, not an assertion that every colored short boundary extends.

## 3. Apply the five-cut equality data when there are six odd faces

Let H be the plane dual of such a minimal G and suppose H has exactly six odd-degree vertices. Define the small-pair-cut graph F as in m08. By m08 it has maximum degree two and no triangle.

Claim R3 (claim:opg401-m09-six-terminal-pair-graph-bipartite):
F has no five-cycle and is therefore bipartite.

Assume to the contrary that t1,...,t5 form its five-cycle, with t0 the remaining odd vertex. Choose the five realizing pair cuts. The equality proof in m08 gives six terminal atoms B0,...,B5, each with boundary size five and containing exactly one odd vertex. It also gives the Hamming-distance equality restrictions on edges between atoms.

A primal edge boundary of size five is Eulerian. Since G is simple and triangle-free, a decomposition into edge-disjoint cycles shows that it must be exactly one simple five-cycle: two cycles would need at least eight edges. The face set of each B_j lies on one side of that cycle. It contains exactly one odd face. R2 therefore says that this side is a single face. Hence each terminal atom consists of its one dual vertex t_j, and every t_j has degree five.

All remaining dual vertices are even-degree and have nonterminal codes. No edge joins distinct nonterminal-code atoms, by the equality signature. Consider a connected component C of the subgraph on these remaining vertices. It has one code and can attach only to terminals whose codes differ from it by one bit. Examining the five cyclic weight-two rim codes and the zero center code shows that its neighbors are a subset of
  {t0,ti,t(i+1)}
for some consecutive rim pair, or a subset of one such pair. It cannot touch two nonconsecutive rim terminals. This follows also from the triangle inequality for Hamming distance: those terminal codes differ by four.

## 4. Compress attachment multiplicities algebraically

For such a component C, let m_v be its number of attachment edges to a terminal v and let d_C=sum m_v. Its even-degree vertices imply d_C is even. Since t_v has degree five, the cut C union {v} has size
  d_C+5-2m_v.
It contains one odd terminal, so its size is at least five. Therefore m_v<=d_C/2 for each attached terminal.

There cannot be only one attached terminal. For two terminals the two multiplicities must be equal. For three terminals a,b,c, replace the attachment star in a purely algebraic terminal graph by edges of multiplicities
  w_ab=(m_a+m_b-m_c)/2,
  w_ac=(m_a+m_c-m_b)/2,
  w_bc=(m_b+m_c-m_a)/2.
They are nonnegative integers by even parity and the preceding inequalities. This step is an algebraic cut representation, not an asserted graph contraction preserving the root class.

For a fixed terminal subset A, the boundary contributed by this replacement equals min(m(A),d_C-m(A)), the smaller of the two costs of putting the whole component on either side. Thus the resulting terminal multigraph J has degree five at every terminal, and its pair-cut boundary for {ti,t(i+1)} is at most the original realizing boundary six. Every original realizing cut keeps each C intact, since its code is constant.

The support of J is contained in a wheel: rim edges ti-t(i+1) and spokes t0-ti. Write b_i for rim multiplicities and a_i for spokes. Its degree equations are
  sum a_i=5,
  a_i+b_(i-1)+b_i=5.
Summing the second equation gives sum b_i=10. The consecutive pair boundary bound gives 10-2b_i<=6, so b_i>=2 for every i. It follows that b_i=2 and a_i=1 for all i.

In particular each consecutive rim pair is joined either directly in H, or through a connected nonterminal component touching that pair and making a positive contribution to its b_i. A component can contribute to only one rim pair, because its terminal neighbors are contained in one wheel triangle. Choose one such direct edge or simple component path for each of the five rim pairs. The chosen paths are internally vertex-disjoint. They form an embedded simple cycle R through t1,...,t5, avoiding t0.

## 5. The triangular-face winding contradiction

Take the disk on the side of R that does not contain t0. Its boundary may have intermediate nonterminal vertices on the five chosen paths. All other vertices in the disk are nonterminal.

Give terminal ti the label i modulo five in cyclic order. Give all vertices of any nonterminal component C a single label equal to one of its rim-neighbor labels. Such a rim neighbor exists: a component attached only to t0 was already excluded by m_v<=d_C/2. Its possible rim-neighbor labels are equal or consecutive. Thus every edge in this disk joins equal or adjacent labels on a five-cycle. Edges to t0 are not in the disk. Edges between distinct nonterminal components do not exist, and nonconsecutive rim-terminal edges are prohibited by the equality signature.

Along each of the five selected boundary paths from ti to t(i+1), all its intermediate vertices have one of the two endpoint labels. The total signed cyclic label increment is therefore +1. The boundary circulation around R is five.

Every face of the dual H has length at most three, because every primal vertex has degree at most three. On a facial closed walk of length at most three, the signed increments -1,0,1 have sum a multiple of five and absolute value at most three. Their sum must be zero. Summing these zero circulations over all faces of the disk cancels its internal edges and gives boundary circulation zero. This contradicts the value five.

This proves that F cannot contain a five-cycle. A triangle-free graph of maximum degree two on six vertices has no other possible odd cycle, so R3 follows. No unproved claim that arbitrary contractions preserve triangular faces was needed; the winding calculation is performed in the original dual embedding.

## 6. What this does and does not close

For a six-odd-face minimal obstruction, the small pair cuts can now be assigned opposite terminal signs consistently, and their path/even-cycle components permit a balanced three-plus/three-minus signing. This eliminates the first odd-cycle sign obstruction identified in m08.

The three-versus-three cut requirements remain. A same-sign triple of charges has magnitude thirty and needs a boundary of at least ten, hence at least eleven by odd parity. Bipartiteness of F alone does not prove these bounds. Also, more than six odd faces permit longer odd cycles in F for which the five-cycle equality argument does not apply unchanged. The root remains open.

## 7. A precise boundary-strength warning

The retraction proof R1 uses the fact that every homomorphism of a five-cycle to a five-cycle is an isomorphism. It cannot be replaced by the statement that a patch merely has an (8,3)-coloring.

For an explicit palette-level witness, K_(8/3) has the five-cycle 0-3-6-1-4-0. Prescribe (20,7) colors on these five target vertices in that order as
  0,12,19,6,13.
The cyclic edge increments are 12,7,7,7,7, all legal.
The remaining palette vertices are 2,5,7. Vertex 5 sees the prescribed colors 0 and 6, so c01 forces its color to 13. Vertex 2 then sees colors 19 (at vertex 6) and 13 (at vertex 5), forcing its color to 6. Vertex 7 sees prescribed colors 12 (at vertex 3) and 13 (at vertex 4), so its available colors lie in {0,...,5}; none is adjacent to the forced color 6 at vertex 2. Thus the prescribed boundary coloring does not extend to this palette graph.

This is not a primal planar-graph counterexample. It pinpoints why an ordinary lower-ratio coloring theorem does not automatically yield arbitrary-fixed-boundary lifting, whereas the explicit retraction does.

## Provenance and checkpoint

Sources: m05's two-odd-face construction and integral flow proof; m07's explicit palette projection; m08's equality signature; m01's minimality framework. All needed additional graph, cut and winding arguments are included here. No external classification, numerical experiment, graph enumeration, theorem-prover run or verifier receipt is assumed. No novelty claim is made.

best_verified_result: none. best_verified_candidate: none.
Open obligations: obligation:opg401-root; obligation:opg401-z20-extension.
Next action: analyze the residual odd triple cuts in the six-terminal case, and the longer odd cycles of the pair-cut graph when there are more odd faces. Finalized transport requires a freshly observed actual main and exact content digests; this working draft does not assert those steps are complete.
