# Separated degree-two pentagon: exact boundary relation and forced overlap

Status: candidate_only. Transport status: working draft for a subsequent immutable packet.
Primary owner: math-derivation.
Candidate: candidate:opg401-a01-m02-separated-pentagon-draft.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1.
Target: obligation:opg401-root.
Local dependency remains open: obligation:opg401-z20-extension.
This draft does not claim that a new packet, PR or verification receipt exists.

## Frozen configuration

Let a-b-u-c-v-a be a five-cycle in a finite simple triangle-free planar subcubic graph. Vertices u,v have degree two; a,b,c have degree three. The cycle is chordless by triangle-freeness. Let p,q,r be the colors on the outside neighbors of a,b,c respectively. Colors need not be distinct; outside vertices may coincide whenever the graph assumptions permit it. All outside colors are fixed. All five cycle vertices may be colored anew.

Use the frozen Z20 convention, shortest circular distance delta, A(t)=t+{7,...,13}, and B6(t)={x:delta(x,t)<=6}. The only local inputs are c01's exact two-edge extension criterion and the definition of a legal edge.

Claim S1 (claim:opg401-m02-separated-pentagon-boundary):
The fixed boundary fails to extend exactly in the following cases:
(a) p=q, with any r;
(b) delta(p,q)=1 and r belongs to A(p) union A(q).
There are no bad values of r when delta(p,q)>=2.

This is different from the adjacent-degree-two pattern classified in c05. It is a statement about fixed boundary colors, not unrestricted colorability.

## Proof by signed intervals

Fix a proposed color z at c. Colors x,y at a,b must satisfy
x in A(p) intersect B6(z), y in A(q) intersect B6(z), and delta(x,y)>=7.
Then the two length-two paths a-v-c and b-u-c can be filled by c01, with no omitted incident edges. Also require z in A(r).

Translate z to zero. For P=[p-z]20 in {1,...,19}, the set A(P) intersect B6(0) has the unique signed representative interval
I(P)=[max(-6,P-13), min(6,P-7)] in [-6,6].
For P=0 it is empty. The formula follows by intersecting the translates of [7,13] with the two short arcs around zero; equivalently the surviving lift is [P-13,P-7] intersect [-6,6].

All possible x,y lie in [-6,6]. A legal edge therefore requires |x-y|>=7; its maximum possible separation is twelve, so the directed upper bound thirteen and its reverse cause no additional case. For 1<=P<Q<=19, the maximum separation is
min(6,Q-7)-max(-6,P-13).
It is at least seven exactly when P<=12 and Q>=8. Necessity follows from the separate endpoint bounds. For sufficiency, when P<=7 and Q>=13 the separation is twelve; when both are at most thirteen or both at least seven, substitution gives at least seven using Q>P; the two remaining clipped cases give the same bounds. More directly: if P<=7, the lower endpoint is -6 and Q>=8 makes the upper endpoint at least one. If P>=8, then Q>P implies Q>=9; for Q<=13 the separation is Q-P+6>=7, and for Q>=13 it is 19-P>=7. This exhausts the possibilities.

For p=q both a and b must lie in the same A(p), a seven-element interval of diameter six. They are adjacent, so extension is impossible.

For p!=q use a common translation/reflection to normalize p=0 and q=d with 1<=d<=10. The preceding interval test gives precisely the following feasible colors for c before imposing its outside edge:
F_d=[1,d-1] union [max(8,d+1), min(19,d+12)].
The first interval may be empty. To audit it, separate z in {1,...,d-1} from z in {d+1,...,19}. In the first region the two nonzero residues are d-z and 20-z, which satisfy the test. In the second they are 20-z and 20+d-z, and the test becomes z>=8 and z<=d+12. The endpoints z=0,d give an empty list and are excluded.

For d=1, F_d=[8,13]. A(r) avoids this six-element interval exactly when r=7,...,14. These eight colors are A(0) union A(1).
For 2<=d<=6, the complement of F_d consists of two cyclic intervals, each of length 8-d<=6. A seven-consecutive-element A(r) cannot fit inside either interval or cross a gap, so it always meets F_d.
For 7<=d<=10, F_d is all of Z20 except 0,d. Again every A(r) meets it.
Choosing z in this intersection, then the separated interval endpoints x,y, and then the two c01 path fillings constructs an extension. The necessity argument already inspected every possible z. Thus S1 is an equivalence.

Claim S2 (claim:opg401-m02-separated-pentagon-count):
There are exactly 720 bad ordered triples and 7280 good ordered triples out of 8000. For each p, q=p contributes twenty bad r values and the two distance-one q values each contribute eight. Hence the count is 20*(20+2*8). This is derived arithmetic, not reported enumerator output.

## A forced second pentagon in a minimal obstruction

Assume G has minimum vertex order among non-(20,7)-colorable graphs in the contract class and contains the stated cycle. Let H be its five-vertex deletion, and let P,Q denote the actual outside vertices adjacent to a,b. They are distinct: equality would create the triangle P-a-b-P.

Every coloring of H must satisfy delta(phi(P),phi(Q))<=1, by S1. Thus P,Q are not adjacent in H. If they had no common neighbor in H, add edge PQ along the deleted route P-a-b-Q. This addition preserves planarity, since that route can be contracted and its other incident edges deleted. It preserves triangle-freeness because P,Q are nonadjacent and have no common neighbor. Both vertices lost an incident edge on deletion and regain at most one, so the augmented graph is subcubic and smaller than G.

Minimality supplies a coloring of H+PQ. Its P,Q colors have distance at least seven, so S1 extends its restriction over the original cycle, a contradiction.

Claim S3 (claim:opg401-m02-forced-overlapping-pentagon):
P,Q must be nonadjacent with a common neighbor Z in H. The five distinct vertices P,a,b,Q,Z therefore form another five-cycle sharing edge ab with the original one. This second five-cycle is not claimed to be facial. If the two outside vertices belonged to different components, the no-common-neighbor reduction would apply, so that case is also excluded.

## Tight-path size restriction

Claim S4 (claim:opg401-m02-conditional-order):
A vertex-minimal obstruction containing this separated-degree-two pentagon has at least twenty-three vertices.

H has a coloring by vertex minimality. If all its colorings have P and Q equal, c06's explicitly proved reachable-set shift lemma gives at least twenty-one vertices in H, a stronger bound than needed.

Otherwise choose a coloring and a common palette isometry with phi(P)=0, phi(Q)=1. In its tight digraph an arc has color increment seven. If P were not reachable from Q, add one simultaneously to the colors of all vertices reachable from Q. No tight arc leaves that set, so c06 shows that this is a valid coloring. It gives colors zero and two on P,Q, which extend by S1, a contradiction.

A tight Q-to-P path must therefore exist. Its length L satisfies 7L=19 modulo20, so L=17 modulo20. A shortest such path is simple and has at least seventeen edges, using at least eighteen vertices of H. Restoring the five cycle vertices gives |V(G)|>=23. This is a conditional order restriction for one configuration, not a global search bound or graph enumeration.

## Attacks, source map, and checkpoint

The p=q case demonstrates why close boundary colors are not necessarily favorable: a,b are adjacent and their common outside color constrains them to an interval with no legal internal edge. The p!=q threshold is two, not seven; no artificial edge on P,Q is asserted to be necessary for extension. The augmentation is only a way to produce a favorable deletion coloring when the graph-class hypotheses allow it.

Sources are the frozen contract, the admitted obligation graph, and candidates c01, c03, c05, c06 and the m01 minimal-obstruction organizer. No new external theorem, novelty claim, mathematical solver run or verifier receipt is a premise.

best_verified_result: none. best_verified_candidate: none.
Open obligations: obligation:opg401-root; obligation:opg401-z20-extension.
The next packet must freeze its actual fresh main base and the exact artifact digest before PR transport. No transport completion is asserted by this draft. Next mathematical action: complete the cubic square boundary relation and distinguish a failed matching replacement from genuine face reducibility.
