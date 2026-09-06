# Four odd faces: a cut-count proof and a global reduction

Status: candidate_only. Transport status: working draft for a subsequent immutable packet.
Primary owner: math-derivation.
Candidate: candidate:opg401-a01-m07-four-odd-face-reduction-draft.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1.
Target: obligation:opg401-root.
Local dependency remains open: obligation:opg401-z20-extension.
No new packet, final PR state, mathematical execution, verifier receipt, or obligation closure is asserted.

## 1. The auxiliary four-terminal inequality

Let H be a finite undirected multigraph, loops ignored in cuts. Let T={t1,t2,t3,t4} be four distinct designated vertices. Suppose every cut containing an odd number of T vertices has at least five edges. Suppose also that every cut containing an even number of T vertices has even size. In the intended dual application, T is exactly the set of odd-degree vertices, so this parity condition is automatic.

For each of the three partitions of T into two pairs, let lambda_i be the minimum size of a cut that separates those pairs. The side containing t1 may contain arbitrary nonterminal vertices. Such minima exist because there are finitely many vertex subsets.

Claim C1 (claim:opg401-m07-four-terminal-cut-sum):
  lambda_12|34 + lambda_13|24 + lambda_14|23 >=20.
Consequently at least one of these three pair-separating minima is at least eight.

Choose minimizing vertex sets U1,U2,U3 containing respectively the pairs {t1,t2}, {t1,t3}, {t1,t4}. Give every vertex its three-bit membership code in these sets. The terminal codes are
  t1:111, t2:100, t3:010, t4:001.
They are distinct, and any two differ in exactly two positions.
Let B_j be the full atom of vertices with the same code as t_j. It contains exactly one terminal, so |delta(B_j)|>=5.

For an edge whose endpoint codes differ, its contribution to the sum of the three U_i cut sizes is their Hamming distance. Its contribution to the sum of the four B_j cut sizes is two when both endpoints have distinct terminal codes, one when exactly one endpoint has a terminal code, and zero otherwise. The Hamming distance is respectively at least two, one, or zero. If both codes are equal, both contributions are zero. Hence edge by edge,
  sum_i |delta(U_i)| >= sum_j |delta(B_j)| >=20.
This proves the inequality, without assuming the cuts are nested or disjoint and without identifying nonterminal atoms with terminal atoms.

All three lambda_i are even under the stated parity hypothesis. If each were less than eight, all would be at most six and their sum at most eighteen, contradicting C1. This proves the final assertion.

The inequality is a direct finite cut argument; no uncrossing theorem or external packing result is being silently invoked.

## 2. The plane-graph application

Claim C2 (claim:opg401-m07-four-odd-face-coloring):
Every finite connected simple triangle-free plane graph with at most four odd faces has an (8,3)-coloring, and therefore a (20,7)-coloring. This auxiliary result does not need a maximum-degree hypothesis.

Let H be the planar dual, with edge multiplicities retained. The odd-degree vertices of H are exactly the odd facial boundary walks of the primal. As proved in m05, every dual cut containing an odd number of odd faces has odd size and corresponds to an Eulerian primal edge set with an odd cycle. Simplicity and triangle-freeness make that odd cycle length at least five. Thus every such cut has size at least five. The identity |delta(U)|=sum_{v in U}deg(v) modulo2 supplies the even-cut parity condition as well.

Use a palette of size eight, midpoint four, and centered edge capacities one. The m05 reconstruction applies verbatim: a dual integer flow h with |h_e|<=1 and facial divergence b_f=4*ell(f) modulo8 reconstructs edge differences 4+h_e in {3,4,5}, hence an (8,3)-coloring.

If there are no odd faces, take h=0. If there are two, assign charge +4 and -4 to them and zero elsewhere. Any nonzero-charge cut then has magnitude four and at least five edges, so the unit-capacity cut criterion from m05 supplies the required integer flow.

If there are four odd faces, apply C1 and choose a pair partition whose separating minimum is at least eight. Assign charge +4 to the two faces on one side of this terminal partition, -4 to the other two, and zero to all even faces. Check an arbitrary face subset U:
- If it contains zero or four odd faces, its total charge is zero.
- If it contains one or three, its total charge has magnitude four and its cut has size at least five.
- If it contains two with opposite signs, its total charge is zero.
- If it contains the two with the same sign, its total charge has magnitude eight. Its cut realizes the selected pair separation and therefore has size at least eight.

All unit-capacity cut inequalities hold. The fully included integral augmenting-path proof in m05 gives a flow with these divergences. The palette reconstruction proves C2. There is no omitted charge domain: we only need to exhibit one legal vector, and zero on even faces and plus/minus four on odd faces always have the required residues, regardless of face length.

## 3. An explicit map to the frozen palette

For i in {0,...,7}, define
  eta(i)=floor(5i/2) in {0,2,5,7,10,12,15,17} subset Z20.
Extend the integer expression by eta(i+8)=eta(i)+20 for checking wrapped differences. A directed legal (8,3) edge has residue three, four or five. The corresponding eta difference is respectively seven or eight, exactly ten, or twelve or thirteen. All lie in [7,13]. Thus composing an (8,3)-coloring with eta gives a (20,7)-coloring.

This explicit map avoids appealing to an unstated monotonicity theorem for circular chromatic number. It checks wrapped edges as well as linear representatives.

## 4. Root-oriented structural consequence

Claim C3 (claim:opg401-m07-minimum-six-odd-faces):
A vertex-minimal obstruction to the frozen root, if one exists, has at least six odd faces in any plane embedding used in its analysis.

It is connected by m01. The number of odd faces is even, because their total boundary length, together with the even faces, is twice the number of edges. Counts zero, two and four are all eliminated by C2. This proves the stated lower bound.

This advances m05's weaker four-odd-face necessary condition. It is not a claim that all remaining odd-face distributions are colorable. In particular, the twenty-vertex sharpness graph in m06 has twelve odd faces and is entirely consistent with this restriction.

## 5. Why the maximum-degree hypothesis matters beyond this subfamily

Here is a precise boundary attack against extending C2 indiscriminately to six odd faces while still omitting the root's maximum-degree condition.

Define W with vertices z, x0,...,x4, y0,...,y4. Include the five-cycle y0-y1-y2-y3-y4-y0 and the ten edges z-x_i, x_i-y_i. Draw the cycle as the outside boundary and its subdivided spokes radially to z. The five inside faces and the outside face are all pentagons. W is simple, triangle-free and planar. Its maximum degree is five at z; each y_i has degree three and each x_i degree two. Thus W is explicitly outside the frozen subcubic domain.

W has no (20,7)-coloring. Translate the putative color of z to zero. Every two-edge path z-x_i-y_i forces the color of y_i into B6(0), by c01. In the unique signed representatives [-6,6], any legal edge between two such colors must join a strictly negative color to a strictly positive color: two colors on the same side differ by at most six, and zero cannot have a legal neighbor within this set. A legal edge has absolute difference between seven and twelve here; the alternative wrapped range introduces no new same-side edge. This would give a bipartition of the odd y-cycle, impossible.

The obstruction concerns the degree-five graph W, not the root. Its six odd faces show that the no-degree-bound extension of C2 to that next even face count is false. No graph search or SAT result is involved: both the graph and the obstruction are explicit.

For an additional domain check, W is ordinarily three-colorable. Set z=0 and color y0,...,y4 by 0,1,0,1,2. Choose x_i=1 when y_i is zero or two, and x_i=2 when y_i is one. Every edge has distinct endpoints in this three-color palette. The failure of (20,7)-colorability is not a claim that W violates ordinary planar three-colorability.

## 6. Certificates, provenance and checkpoint

The four-terminal proof can be audited by the four displayed bit codes and a single edge-contribution inequality. The plane application explicitly checks every possible number and sign pattern of terminals in a cut. The actual vertex-color construction is supplied by the integral flow proof and the path-potential reconstruction in m05, followed by the explicit palette map eta.

No min-cut algorithm, graph enumerator, compiler, solver or mathematical verifier was executed for this draft. The minimum cut sets used in the proof exist by finite minimization; they are not invented outputs for a concrete graph. Prior-art comparison is still required before assigning novelty to the theorem or its cut argument. No novelty claim is made.

Sources: the frozen ProblemContract, m01's minimal connectedness, m05's boundary parity and integral-flow proofs, and c01's length-two endpoint relation for the explicit degree-bound counterexample. Both admitted obligations remain open until trusted verification and admission.

best_verified_result: none. best_verified_candidate: none.
Open obligations: obligation:opg401-root; obligation:opg401-z20-extension.
Next mathematical action: analyze six or more odd faces while retaining the subcubic restriction, which means each dual face has length at most three; the degree-five W obstruction identifies exactly a feature that is forbidden in that next problem. Finalized transport must use a fresh actual main and exact content digests; this file alone does not assert completed transport.
