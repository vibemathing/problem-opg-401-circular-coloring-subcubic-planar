# Cubic square: complete fixed-boundary relation and a failed replacement

Status: candidate_only. Transport status: working draft for a subsequent immutable packet.
Primary owner: math-derivation.
Candidate: candidate:opg401-a01-m03-cubic-square-draft.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1.
Target: obligation:opg401-root.
Local dependency remains open: obligation:opg401-z20-extension.
No new packet, PR, mathematical run or verification receipt is asserted by this draft.

## 1. Exact configuration and boundary normalization

Let v1-v2-v3-v4-v1 be a four-cycle in a finite simple triangle-free subcubic graph, with all four cycle vertices of degree three. There are no chords. Write p,q,r,s for the fixed colors of their outside neighbors, in that cyclic order. The vertices outside the square are already properly colored. All four internal colors may be chosen anew, but outside colors are held fixed.

Repeated outside colors are permitted. The relation below remains correct when graph-allowed outside vertices coincide. In a hypothetical vertex-minimal obstruction, m01 shows the four outside vertices are distinct, but it does not imply their colors are distinct.

Use delta and A from c01 and B6(t)={x:delta(x,t)<=6}. Choose epsilon in {1,-1} so epsilon*(s-q)=t modulo20, where t=delta(q,s) in {0,...,10}. Translate and reflect all colors to normalize q=0,s=t. Put P=[epsilon*(p-q)]20 and R=[epsilon*(r-q)]20.

Claim Q1 (claim:opg401-m03-square-table):
The fixed coloring extends exactly under these conditions:
- 0<=t<=7: P,R both belong to {t+1,...,19}, and |P-R|<=12 using these fixed representatives.
- 8<=t<=10: P,R both belong to {1,...,t-1}, or both belong to {t+1,...,19}.
These two regimes are a complete classification, not merely sufficient tests.

## 2. Reduction to two interval choices

Let x,z be the colors assigned to the opposite vertices v1,v3. Their outside edges require x in A(P) and z in A(R). By c08, the three constraints at v2 have a common allowed color exactly when x,z,0 are pairwise within distance six. The corresponding statement at v4 requires x,z,t to be pairwise within distance six. Consequently extension is equivalent to
x in A(P) intersect J_t, z in A(R) intersect J_t, delta(x,z)<=6,
where J_t=B6(0) intersect B6(t).

This is only a color-choice reduction; no outside coloring is changed. Once x,z are selected, the common-neighborhood theorem supplies v2 and v4 independently, as these two vertices are nonadjacent. There are no further edges to check.

Represent B6(0) by the distinct integer lifts [-6,6]. Direct intersection gives
J_t=[t-6,6] for 0<=t<=7,
J_t=[t-6,6] union [-6,t-14] for 8<=t<=10.
The possible second interval arises from the lift t-20 of the other center. It is empty before t=8; no wraparound component is suppressed.

For a nonzero P in {1,...,19}, A(P) intersect B6(0) is
I(P)=[max(-6,P-13),min(6,P-7)]
in signed representatives. For P=0 the intersection is empty. These formulas follow from the original modular intervals and can be checked without enumerating graph colorings.

## 3. The connected-interval regime

For 0<=t<=7, intersect I(P) with [t-6,6]. The result is nonempty exactly when P in {t+1,...,19}, and then is
K_t(P)=[max(t-6,P-13),min(6,P-7)].
The same applies to R.

Suppose P<=R. Both endpoint functions are nondecreasing, so the least linear distance between the two intervals is
max(0,max(t-6,R-13)-min(6,P-7)).
All possible x,z lie in [-6,6], so their absolute separation is at most twelve. The condition delta(x,z)<=6 is equivalent to |x-z|<=6 here: the other circular alternative would require |x-z|>=14, which cannot occur.

The least distance is at most six exactly when R-P<=12. For necessity, if R-P>=13 then max(t-6,R-13)-min(6,P-7)>=R-P-6>=7. For sufficiency, it is enough to compare both terms of the maximum on the left with both terms of min(6,P-7)+6. The only nonautomatic comparison is R-13<=P-1, namely R-P<=12. The other comparisons follow from t<=7, P>=t+1 and R<=19. This proves Q1 in this regime, including t=0 and t=7.

## 4. The split-interval regime

For 8<=t<=10, J_t has two components
L=[-6,t-14], U=[t-6,6].
Their closest linear separation is eight. The largest linear separation is twelve, so even via the opposite arc every cross-component pair has circular distance at least eight. Thus x,z must lie in the same component.

Each component has span at most four, so any pair within a component automatically has distance at most six. A color interval I(P) can meet L exactly when P in {1,...,t-1}; it can meet U exactly when P in {t+1,...,19}. It cannot meet both, since I(P) has span at most six while the gap between component endpoints is eight. The exceptional colors zero and t meet neither relevant set.

Therefore both P,R must lie in the same one of those two ranges. This proves the second part of Q1. The ambiguity of epsilon at t=10 just swaps the two ranges. At t=0 it reverses the nonzero representatives, preserving |P-R|, so the normalized criterion does not depend on either exceptional choice.

## 5. Hand-derived cardinalities

Claim Q2 (claim:opg401-m03-square-count):
For fixed normalized q=0 and s=t, the numbers N_t of extendible ordered pairs (P,R) are:

| t | N_t |
|---|---|
| 0 | 319 |
| 1 | 294 |
| 2 | 269 |
| 3 | 244 |
| 4 | 219 |
| 5 | 194 |
| 6 | 169 |
| 7 | 144 |
| 8 | 170 |
| 9 | 164 |
| 10 | 162 |

For t<=7, put m=19-t. There are m^2 pairs in the permitted interval. The number whose representative difference is at least thirteen is twice the sum of m-d over 13<=d<=m-1. Hence N_t=319-25t, including the zero-sum cases m=12,13. For t>=8, the two disjoint permitted ranges have sizes t-1 and 19-t, so N_t=(t-1)^2+(19-t)^2.

For each fixed q, distances one through nine have two choices of s and distances zero and ten have one. Thus the total number of good ordered quadruples is
20*(319+2*(294+269+244+219+194+169+144+170+164)+162)=84300.
The remaining 75700 of 160000 ordered boundary quadruples are bad. These are consequences of the interval formulas, not outputs of an enumeration or SAT solver.

## 6. A tempting planar replacement is not sound

A proposed shortcut deletes the square and merely adds the two outside edges p-q and r-s, hoping every coloring of that smaller graph will lift. Color labels here stand for four distinct outside vertices. The explicit boundary tuple
(p,q,r,s)=(7,0,17,10)
satisfies both added edge constraints, each of distance seven. But t=10, P=7 and R=17 lie in opposite permitted ranges, so Q1 proves that it does not extend across the original square.

The example can be realized in the contract class by taking the square with four distinct pendant outside vertices, and using those colors after replacing the square by the two disjoint edges. The original graph is bipartite and has a full coloring with its two bipartition classes colored zero and ten. Thus this is a failure certificate for the universal lifting assertion, not a root counterexample.

Similarly, the all-equal outside tuple is bad because adjacent internal vertices would be forced into the same seven-element independent palette interval. A whole-component rotation cannot remove equality between two outside vertices in that same component. Consequently the K2,3 component-rotation argument cannot be reused without inspecting this different boundary relation.

## 7. Connection to the unavoidable target

The m01 organizer forces a face with three, four or five degree-three vertices, after its stated reductions. A wholly cubic facial square is one unresolved case with k=4. Q1 now supplies its exact finite bad-state target and Q2 its analytic coverage counts. In a minimal obstruction every coloring of the square deletion must fall in Q1's complement. Proving that some deletion coloring avoids that complement, or finding an augmentation whose every coloring lifts, remains a genuine root obligation; this table does not discharge it.

The table handles a fixed coloring of the deletion. It does not prove arbitrary boundary tuples are realizable by every outside graph, nor that a bad tuple implies graph noncolorability. Any next reduction must preserve this quantifier distinction.

## Sources, verification requirements, and checkpoint

Sources: frozen contract and obligation graph; candidate c01 for two-center arithmetic, c08 for common-neighborhood existence, f01 for the preserving-extension interpretation, and m01 for the minimal-obstruction/face target. No external classification theorem is assumed. No code, solver, enumerator, theorem prover, or mathematical verifier was executed for this draft.

A future finite checker may normalize q=0 and inspect the 8000 triples (p,r,s), using the interval feasibility relation rather than 20^4 unconstrained assignments. Its output would need a separately frozen executable and certificates; none is fabricated here. The displayed table already has a direct hand derivation.

best_verified_result: none. best_verified_candidate: none.
Open obligations: obligation:opg401-root; obligation:opg401-z20-extension.
Transport remains to be frozen in a new packet against a freshly observed main. The rejected subroute is the two-edge matching replacement with unconditional lifting. Next action: constrain the outside component partition of a facial square using planarity and two-edge-bond gluing, then examine the connected-outside case left by those reductions.
