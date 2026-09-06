# Exact Z20 degree-two extension: candidate c01

Status: candidate_only. Primary owner: math-derivation.
Candidate: candidate:opg401-a01-c01-local-extension.
Problem: problem:opg-401-circular-coloring-subcubic-planar.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1.
Target: obligation:opg401-z20-extension.
Root remains open: obligation:opg401-root.
Base: 96b12a5204c72f49d26dfa9cf620e530489d821d.

## 1. Frozen objects, quantifiers, and scope

Z20 is the additive group of integers modulo 20. For an integer z, [z]20
is its unique representative in {0,...,19}. For a,b in Z20 define
r(a,b)=[b-a]20 and delta(a,b)=min(r(a,b),20-r(a,b)).
Thus delta takes values in {0,...,10}. Here d_20 in the target obligation
means this shortest circular distance, not an absolute difference of
arbitrarily chosen integer lifts.

For integers p>=2q>0, a (p,q)-coloring is a map phi:V(G)->Z_p such that,
on each edge uv, q <= [phi(v)-phi(u)]p <= p-q.
This is symmetric in u,v: replacing a nonzero residue r by p-r preserves
the interval. Equivalently the shortest circular distance is at least q.
For fixed representatives in {0,...,p-1}, it is also equivalent to
q <= |phi(v)-phi(u)| <= p-q. Arbitrary integer lifts are not permitted
in that last absolute-value formula.

Consequently, with S={7,8,9,10,11,12,13},
A(a)={x:7<=delta(x,a)<=13}=a+S.
The upper bound 13 is redundant for delta<=10; it is the meaningful
upper bound for the directed residue. Either convention produces this
same allowed-color set only after this equivalence is made explicit.

The local claim quantifies over every a,b in Z20; it needs no graph
hypotheses. Its graph application uses finite simple graphs, a vertex v
with exactly two distinct neighbors u,w, and a fixed (20,7)-coloring of
G-v. Planarity, triangle-freeness, and maximum degree three enter only
the minimal-counterexample application. Allowed background is finite
combinatorics and the finite/planar graph basics in the contract.

## 2. Atomic candidate claims

C01 (claim:opg401-c01-neighborhood): A(a)=a+S.
C02 (claim:opg401-c01-intersection): for t=delta(a,b),
    |A(a) intersect A(b)|=max(0,7-t).
In particular the intersection is nonempty exactly when t<=6.
C03 (claim:opg401-c01-extension): a fixed coloring of G-v extends without
changing any old color exactly when delta(phi(u),phi(w))<=6, with
exactly 7-delta(phi(u),phi(w)) possible colors when it extends.
C04 (claim:opg401-c01-critical-constraint): in a vertex-minimal member of
the contract class having no (20,7)-coloring, every coloring of G-v at
any degree-two vertex v has neighbor-color distance in {7,8,9,10}.
These are generated derivations, not verifier receipts.

Dependency map: frozen definitions -> C01 -> C02 -> C03 -> C04.
C04 also uses vertex minimality and closure of the class under deletion.
There is no implication here from C04 to the global root conclusion.

## 3. Symmetry and complete hand-auditable table

Translations and reflection x -> -x preserve delta and S=-S.
For any ordered pair (a,b), choose epsilon in {1,-1} with
epsilon*(b-a)=t modulo 20, where t=delta(a,b).
The bijection T(x)=epsilon*(x-a) sends (a,b) to (0,t) and sends their
allowed-color intersection to A(0) intersect A(t).
Conversely delta is invariant under these transformations, so t is a
complete class invariant. There are exactly eleven classes.

Notation [i,j] in this table means the ordinary integer set
{i,i+1,...,j}, not a wrapped interval.

| t | A(t), in fixed representatives | A(0) intersect A(t) | size |
|---|---|---|---|
| 0 | [7,13] | [7,13] | 7 |
| 1 | [8,14] | [8,13] | 6 |
| 2 | [9,15] | [9,13] | 5 |
| 3 | [10,16] | [10,13] | 4 |
| 4 | [11,17] | [11,13] | 3 |
| 5 | [12,18] | [12,13] | 2 |
| 6 | [13,19] | {13} | 1 |
| 7 | [14,19] union {0} | empty | 0 |
| 8 | [15,19] union [0,1] | empty | 0 |
| 9 | [16,19] union [0,2] | empty | 0 |
| 10 | [17,19] union [0,3] | empty | 0 |

For the original pair, apply T^{-1}(y)=a+epsilon*y to the displayed
intersection. This gives the set itself, not just its cardinality.

## 4. Derivation, without enumeration as a premise

For 0<=t<=6 the translated interval t+S=[7+t,13+t] does not wrap:
13+t<=19. Intersecting it with S=[7,13] gives [7+t,13], whose integer
cardinality is 13-(7+t)+1=7-t.

For 7<=t<=10, translation yields
[t+7,19] union [0,t-7]. Its high part begins at least at 14, and its low
part ends at most at 3. Neither part meets [7,13].
This proves both directions and every row.

A second algebraic audit is available. Common membership means
x=a+s=b+s' with s,s' in S, hence b-a=s-s' belongs to
S-S={-6,-5,...,5,6} modulo 20. Conversely any such difference has a
representation s-s', producing a common x. Each integer difference k
with |k|<=6 has exactly 7-|k| such representations.
Two different integers in [-6,6] cannot be equal modulo 20, because
their difference has absolute value at most 12<20. Thus no wrapped
representation is missing or double-counted. The nearest residue
difference is in this set exactly when delta(a,b)<=6.

## 5. Exact graph extension and the quantifier barrier

Only the two edges vu,vw need checking when G-v is already colored.
A choice for phi(v) is valid exactly when it belongs to both
A(phi(u)) and A(phi(w)). C02 therefore proves C03, with all old colors
held fixed. An explicit procedure normalizes the neighbor pair by T,
chooses any y in [7+t,13] for t<=6, and assigns phi(v)=a+epsilon*y.

Now suppose a graph without a (20,7)-coloring exists in the contract
class, and choose one G of minimum vertex order. Deleting a vertex
preserves finite simplicity, planarity, triangle-freeness and the
maximum-degree bound. Hence G-v has at least one (20,7)-coloring.
For a degree-two v, if even one such coloring had t<=6, C03 would
extend it to G. Thus every such coloring must have t>=7.
Vertices of degree zero or one extend using respectively 20 or seven
choices, so this minimal graph has minimum degree at least two.

This does NOT exclude all degree-two vertices. A reducibility proof
must supply a coloring of G-v with t<=6, possibly by a class-preserving
reduction or a justified recoloring argument. Triangle-freeness only
implies u,w are not adjacent; it does not constrain their colors to
distance at most six. Adding an edge uw would force t>=7, the opposite
of the desired local condition.

## 6. Adversarial tests and discarded shortcut

Boundary t=6: A(0) intersect A(6)={13}, so the threshold is inclusive.
Boundary t=7: A(0) intersect A(7)=empty, even though color difference
seven is itself legal on an edge.
Antipodal t=10: the intersection is empty.
Crossing zero: a=19,b=0 has delta=1 and intersection {7,...,12}, size six;
using the representative difference 19 as the shortest distance fails.
Crossing zero at the threshold: a=19,b=5 has intersection {12}.

The proposed shortcut "every coloring of G-v extends at a degree-two
vertex in this graph class" has this explicit counterexample to the
shortcut, NOT to the ProblemContract:
take the five-cycle v-u-x-y-w-v. Color G-v in path order
u,x,y,w by 0,7,14,7. All three differences are seven, but the uncolored
v sees 0 and 7, so its allowed-color intersection is empty.
The graph itself has a (20,7)-coloring: in cyclic order v,u,x,y,w use
0,8,16,4,12. All five shortest edge distances are eight.
Thus a failed extension of a fixed coloring is not noncolorability.

## 7. Reproduction and verification request

Manually reconstruct the eleven rows using the two interval formulas,
then check the inverse symmetry map and the three edges of the
five-cycle deletion witness. An optional future exact audit may loop
over all 20*20 pairs and all 20 candidate colors (8,000 membership
tests), compare the count with max(0,7-delta), and verify the witnesses.
That enumeration was NOT executed for this candidate; no runtime
output or solver version is claimed.

Request a faithful formalization of C01-C03, a kernel check and an
axiom-escape audit, plus a separate statement-faithfulness review of
the distance convention and graph application. Requested capabilities
are those in the admitted target acceptance. Existing registry entries
must be checked for task suitability; fixture policies do not by
themselves authorize a graph-theorem verification.

Source comparison: research/artifacts/source-notes/opg401-a01-c01-definition-sources.md.
No external theorem is a premise of the interval calculation.
The paper/source hits provide definitions, attribution and scope checks.

## 8. Checkpoint

best_verified_result: none.
best_verified_candidate: none.
best_candidate: candidate:opg401-a01-c01-local-extension (generated, self-audited).
Open admitted obligations: obligation:opg401-z20-extension;
obligation:opg401-root.
Registered failed-route IDs checked: [].
Discarded shortcut: unconditional extension of every fixed coloring,
with the explicit C5 witness above; the admitted exact-criterion route survives.
Next action within the same target: derive a class-preserving
neighbor-identification criterion and test precisely when short cycles
or degree growth invalidate that reduction. No new obligation ID is
claimed to have been admitted.
