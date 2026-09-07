# Exact dual-charge certificates and the two-odd-face reduction

Status: candidate_only. Transport status: working draft for a subsequent immutable packet.
Primary owner: math-derivation.
Candidate: candidate:opg401-a01-m05-dual-charge-certificates-draft.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1.
Target: obligation:opg401-root.
Local dependency remains open: obligation:opg401-z20-extension.
No new packet, completed PR, program execution, mathematical verifier receipt, or obligation closure is asserted here.

## 1. Frozen plane-graph conventions

Let G be a finite connected simple plane graph. A plane embedding is part of this auxiliary input. The root still concerns graphs admitting such an embedding; it does not prescribe one particular drawing. Orient each edge e=uv arbitrarily and let L(e),R(e) be the faces on its left and right. The faces may coincide on a bridge. Facial boundaries are walks, with edge-side multiplicity. Write ell(f) for a face's boundary-walk length. Thus sum_f ell(f)=2|E(G)|.

The directed difference of a (20,7)-coloring on e is d_e=[phi(v)-phi(u)]20 in {7,...,13}. Define its centered increment h_e=d_e-10 in {-3,...,3}. Reverse traversal has increment 10-h_e modulo20, not -10+h_e. This follows because -10=10 modulo20. No arbitrary integer lift of a vertex color is used.

Orient the corresponding dual edge from L(e) to R(e), and define divergence as outgoing minus incoming signed flow. A dual loop contributes zero to divergence. Then the sum of the signed h_e around a face, oriented with that face on the left, is exactly its dual divergence b_f.

## 2. Exact equivalence, including the converse

Claim D1 (claim:opg401-m05-dual-charge-equivalence):
G has a (20,7)-coloring if and only if there are integers h_e and b_f satisfying
  -3 <= h_e <= 3 for every edge;
  div_D(h)(f)=b_f for every face;
  b_f = 10*ell(f) modulo20 for every face.
Consequently sum_f b_f=0 automatically.

Forward proof: a coloring gives the h_e above. The sum of its modular differences around every facial walk is zero. For a walk of length ell, this sum is 10*ell+b_f modulo20. Thus b_f=-10*ell=10*ell modulo20. All capacity and divergence conditions follow by construction.

Backward proof: set the modular increment on oriented e to 10+h_e and its reverse to its negative. The displayed congruence makes each facial circulation zero modulo20. For a simple primal cycle, sum the oriented boundaries of all faces on one side. Internal edge sides cancel, leaving the cycle, so its circulation is zero as well. Every closed walk is decomposable into simple cycles and backtracking pairs, hence also has zero circulation.

Choose a root vertex with color zero. Define any other vertex's color by summing increments along a root-to-vertex path. Two choices of path differ by a closed walk, so this is well-defined. On each oriented edge the color difference is 10+h_e in [7,13], which is exactly the required edge condition. Bridges cause no exception: their two facial contributions cancel and a path potential still assigns both endpoints consistently.

For connected G, each admissible h determines a unique coloring once the root color is fixed. Conversely every coloring determines h. Thus colorings modulo a common translation correspond bijectively to admissible h. This is an exact graph-wide equivalence, not a necessary-only cut test or a proof that an admissible h always exists.

## 3. Eliminate the flow for a fixed charge vector

For an integer vector b with sum b_f=0, let delta_D(U) be the multiset of non-loop dual edges with exactly one endpoint in a face set U. Parallel edges retain multiplicity.

Claim D2 (claim:opg401-m05-fixed-charge-cut-criterion):
There is an integer dual flow h with divergence b and |h_e|<=3 exactly when
  |sum_{f in U} b_f| <= 3*|delta_D(U)|
for every face subset U.

Necessity: sum the divergences on U. All internal contributions cancel, leaving the net flux across its boundary. Its absolute value is at most the sum of capacities.

Sufficiency can be proved directly by the integral augmenting-path argument. Replace each non-loop undirected dual edge by the two opposite directed arcs, each of capacity three. Add a source S with an arc of capacity b_f to each face with b_f>0; add an arc from each face with b_f<0 to a sink T of capacity -b_f. Let B=sum_{b_f>0} b_f.

For a cut whose face vertices on the S side are U, its capacity is
  B - sum_{f in U} b_f + 3*|delta_D(U)|,
which is at least B by the assumed inequality. Starting with zero flow, repeatedly augment along a residual S-to-T path. All residual capacities are integral, so each augmentation raises the value by at least one. If the value were less than B and no augmenting path remained, the vertices reachable from S would define a cut whose capacity equals that smaller value: forward boundary arcs are saturated and reverse boundary arcs carry zero. This contradicts the cut bound. Therefore value B is reached in at most B augmentations. Source and sink demand arcs are saturated.

On each dual edge subtract the two opposite arc flows. Their difference lies in [-3,3] and has the required divergence. Set any unused dual-loop flow to zero. This proves the integral, not merely fractional, conclusion. It also covers B=0.

No flow program was executed for this draft; the argument supplies the existence proof for each fixed b.

## 4. Finite positive and negative certificate interfaces

Every valid coloring's charge satisfies
  b_f in B_f={z in Z: |z|<=3*ell(f), z=10*ell(f) modulo20}.
These are finite domains, fully determined by the embedding. Combining D1-D2 gives:
G is (20,7)-colorable iff some b in the product of these domains, with total zero, satisfies all the fixed-charge cut inequalities.

A positive certificate may simply contain the edge increments h. Check the integer bounds and each facial congruence, then reconstruct the vertex colors by a spanning tree and check every original edge. The final explicit coloring is an even simpler positive certificate; a trusted verification policy must decide how it is admitted.

A cut that violates D2 certifies failure of ONE particular charge vector. It is not a certificate of noncolorability of G. A negative certificate for G must cover every charge tuple in the stated finite domains whose sum is zero, giving a valid violating cut for each. A finite branching certificate may split on charge choices; each leaf must either prove the remaining domains cannot sum to zero, or identify a face subset U for which every remaining completion violates a cut inequality. Coverage and every leaf inequality must be checked, not presumed from a solver's word 'unsatisfiable'.

The embedding and graph-class hypotheses are separate obligations for a root counterexample. In particular, capacity infeasibility for a stronger restricted family of b choices is not noncolorability. The congruence permits nonzero even-face charges when a face is long enough; deleting those choices without proof would change the problem.

This interface is a finite-state certificate design supported by D1-D2. It does not claim that any search, certificate generator, checker, or SAT solver ran.

## 5. Specialization when all facial lengths are between four and seven

Claim D3 (claim:opg401-m05-short-face-signing):
For a connected plane graph all of whose facial lengths lie in {4,5,6,7}, the exact charge domains are
  b_f=0 on a four- or six-face;
  b_f in {-10,10} on a five- or seven-face.

For the even faces, the absolute bound is at most eighteen, and the only multiple of twenty in it is zero. For the odd faces, the absolute bound is fifteen or twenty-one, and the only integers congruent to ten modulo20 are -10 and ten. Thus no valid charge choice has been removed.

Let T be the set of odd faces. A coloring is therefore equivalent to choosing signs sigma_f in {-1,1}, f in T, with total zero, such that
  10*|sum_{f in U intersect T} sigma_f| <= 3*|delta_D(U)|
for every U. The number |T| is even because the sum of all face lengths is even. Global negation of all charges preserves feasibility. For |T|>0 there are binom(|T|,|T|/2)/2 charge assignments up to that negation.

For a fixed terminal subset A subset T, define lambda(A) as the smallest |delta_D(U)| over U with U intersect T=A. There are finitely many U. The signing condition is equivalent to
  10*|sum_{f in A} sigma_f| <= 3*lambda(A)
for every A subset T. This separates the graph-dependent terminal-cut data from the small sign-selection problem.

For example, a cubic plane graph with only pentagonal and hexagonal faces has exactly twelve pentagons: Euler and 3|V|=2|E| give sum_f(6-ell(f))=12. Its exact charge-sign search therefore has binom(12,6)/2=462 assignments up to negation, irrespective of its number of hexagons. No assertion that one of those assignments always succeeds is made here. This is a precise remaining signing question, not a completed theorem about all such graphs.

## 6. A fully derived colorable subfamily: at most two odd faces

Claim D4 (claim:opg401-m05-two-odd-faces):
Every finite connected simple triangle-free plane graph with at most two odd faces has a (10,4)-coloring and hence a (20,8)-coloring. In particular it has a (20,7)-coloring. No maximum-degree restriction is needed for this auxiliary subfamily result.

We use the mod-ten version of D1, with midpoint five and integer edge capacities one. If |h_e|<=1 and each facial divergence satisfies b_f=5*ell(f) modulo10, the increments 5+h_e lie in {4,5,6} and reconstruct a (10,4)-coloring by exactly the same path-potential proof. D2 with unit capacities has the same augmenting-path proof.

If there are no odd faces, take h=0. Every facial circulation is 5*ell(f)=0 modulo10, so the reconstruction already gives a coloring. This includes trees and bridges, whose face boundaries have even multiplicity.

There cannot be exactly one odd face because sum ell(f)=2|E|. Suppose there are exactly two, named s,t. Put b_s=5,b_t=-5 and all other charges zero.

We verify every unit-capacity cut inequality. If U contains neither or both of s,t, its total charge is zero. If U contains exactly one, its total charge has absolute value five. In that case the primal edges corresponding to delta_D(U) form an Eulerian edge set: around any primal vertex, membership of successive face sectors in U changes an even number of times. Moreover its number of edges is odd, because sum_{f in U} ell(f) is odd and internal edge sides contribute twice to that sum.

A finite Eulerian edge set decomposes into edge-disjoint cycles by taking closed trails and splitting at repeated vertices. If its total number of edges is odd, at least one cycle in that decomposition is odd. Simplicity and triangle-freeness force such a cycle to have length at least five. Therefore |delta_D(U)|>=5, exactly the required cut bound. This proof allows disconnected boundaries and does not replace an odd-cut condition by an unjustified connectivity assumption.

The integral cut criterion produces a unit-capacity flow with the chosen charges. The mod-ten reconstruction gives a (10,4)-coloring. Multiplying its colors by two modulo twenty gives edge differences 8,10,12, all in [8,12], hence a (20,8)-coloring and also a (20,7)-coloring.

This is a constructive mathematical argument: the only finite algorithm required for an explicit instance is the integral flow construction already proved above. No output of that algorithm is claimed in this draft.

## 7. Minimal-obstruction consequence and falsifier discipline

A hypothetical vertex-minimal obstruction in the frozen class is connected by m01. D4 shows that every plane embedding used to analyze it must have at least four odd faces. The obstruction cannot consist merely of one pair of odd-face defects separated by arbitrary even-faced material.

This consequence complements the m01 identity sum_f(6-k(f))=12. It does not force all short faces to be cubic, does not exclude four or more odd faces, and does not complete the discharging contradiction.

The exact D1-D2 formulation also diagnoses several tempting false inferences:
- A violated cut for one sign assignment does not eliminate other assignments.
- On faces of length at least eight or ten, additional charges may be allowed; the short-face signing restriction must not be applied unchanged.
- Fractional feasibility cannot be silently rounded without integrality; the explicit augmentation proof is why it is integral here.
- A fixed embedding's face data is not a proof that an arbitrary input graph is planar.
- A working certificate interface is not an executed verifier or an EvidenceLink.

## Sources and continuation checkpoint

The only proof ingredients are the frozen modular coloring definition, elementary plane boundary cancellation, Eulerian cycle decomposition, Euler's formula, and the fully included integral augmenting-path argument. No outside literature theorem is imported as an unstated premise and no novelty claim is made. Bibliographic comparison is still required before attributing novelty to this subfamily result or the standard dual formulation.

best_verified_result: none. best_verified_candidate: none.
Open obligations: obligation:opg401-root; obligation:opg401-z20-extension.
Next mathematical target: combine the short-face terminal-cut formulation with m02-m04's forced overlaps, or find a class-preserving reduction for the connected-outside cubic square. A finalized packet must freeze a freshly observed actual main and the exact artifact bytes before transport. This working draft does not assert that those transport steps have occurred.
