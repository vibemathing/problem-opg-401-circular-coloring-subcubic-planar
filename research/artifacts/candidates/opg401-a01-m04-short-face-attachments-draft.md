# Short-face attachments and a coupled-pentagon reduction

Status: candidate_only. Transport status: working draft for a subsequent immutable packet.
Primary owner: math-derivation.
Candidate: candidate:opg401-a01-m04-short-face-attachments-draft.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1.
Target: obligation:opg401-root.
Local dependency remains open: obligation:opg401-z20-extension.
No mathematical runtime, new packet, completed PR, or verifier receipt is asserted here.

## 1. Outside component counting

Assume G has minimum vertex order among the non-(20,7)-colorable finite simple triangle-free planar subcubic graphs. Use the m01 candidate proofs that G is connected and bridgeless. For a vertex set X with nonempty deletion H=G-X, every connected component of H has at least two edges to X: no attachment would contradict connectivity, and a unique attachment would be a bridge.

Claim A1 (claim:opg401-m04-small-boundary-connected):
If X has at most three boundary edges, H is connected.
Two outside components would require at least four boundary edges.
This counts edges, not merely distinct outside vertices.

Consequently, the deletion of any pentagon having exactly two degree-two vertices is connected in a minimal obstruction. There are precisely three boundary edges, since the cycle is chordless and each of its three degree-three vertices has one outside neighbor. A nonempty deletion is forced by those degree-three vertices.

This applies to both adjacent and separated degree-two patterns. Separate whole-component rotations cannot alter their relative boundary colors: there is only one outside component. The exact c05 and m02 bad-state relations are invariant under a common palette rotation/reflection. The K2,3 multiple-component argument therefore cannot resolve these pentagons merely by being repeated.

## 2. Cubic facial squares have connected deletion

Claim A2 (claim:opg401-m04-square-outside-connected):
For a FACIAL four-cycle C in a minimal obstruction, G-V(C) is connected.

By m01, every vertex of C has degree three, and its four outside vertices are distinct. There are four boundary edges. If the outside graph were disconnected, A1's counting argument forces exactly two components, each with two boundary attachments.

The two pairs of attachment positions cannot alternate on C. To see this, view the exterior of the facial cycle as a closed disk on the sphere. In one component choose a simple path between its attachment edges. It gives a properly embedded arc joining its two boundary positions. Such an arc separates the disk; the alternating positions of the other pair lie on opposite boundary arcs. A connected path in the disjoint second component joining those positions would have to cross the first arc. This contradicts planarity. The assumption that C bounds an empty face is essential to this disk argument.

Thus, after cyclic renaming, one component attaches to v1,v2 and the other to v3,v4. Put each component together with those two cycle vertices. The resulting two pieces are connected smaller graphs, and the only edges between them are v2v3 and v4v1. Each piece includes its terminal edge, respectively v1v2 and v3v4. Minimality gives colorings of both pieces, whose terminal color distances are both in [7,10].

The exact two-edge gluing lemma m01 applies: two fixed piece colorings can be joined after a whole-piece translation/reflection iff their terminal distances differ by at most six. Here they differ by at most three. The combined coloring colors G, a contradiction. Hence the outside deletion is connected.

No analogous connected-deletion assertion is made for nonfacial four-cycles. Their two sides need not form the same empty-disk situation.

## 3. What survives for a wholly cubic pentagonal face

Claim A3 (claim:opg401-m04-cubic-pentagon-partition):
The outside graph of a facial pentagon whose vertices all have degree three is either connected, or has exactly two components with attachment multiplicities two and three. In the latter case the two-attachment positions are consecutive around the pentagon.

There are five boundary edges and every outside component needs at least two, which proves the count. A nonconsecutive pair separates the remaining three positions into two nonempty sets along the cyclic order. The same disk-arc argument would prevent the connected three-attachment component from reaching both sets. Hence the pair is consecutive.

The exceptional partition supplies a two-edge bond of G: put the two consecutive cycle vertices with the two-attachment component on one side, and the three other cycle vertices with the three-attachment component on the other. The two cycle edges between the groups are the bond. The terminal graph distance on the first side is one, while on the second it is exactly two, since the remaining three cycle vertices form a path and triangle-freeness forbids its endpoint chord.

This is exactly the (1,2) two-edge-bond exception retained by m01, not a contradiction to that lemma. It identifies the remaining separator state rather than silently assuming all two-edge cuts are reducible.

## 4. A coupled pair of pentagons is reducible

Let a,b,c,z,u,v,w,t be eight distinct vertices. Suppose their edges include ab and the paths
  a-u-c-v-b,
  a-w-z-t-b,
where u,v,w,t have degree two, a,b have degree three, and c,z have degree at most three. Work in the contract graph class.

Claim A4 (claim:opg401-m04-paired-pentagon-reduction):
Every coloring of the graph obtained by deleting these eight vertices extends to G, with all outside colors unchanged.

The listed edges saturate a,b and all four degree-two vertices. Triangle-freeness excludes edges ac,bc,az,bz. The only possible additional edge within the configuration is cz. If cz is present, it saturates c,z as well; there are no outside edges at all. An explicit valid coloring is
  a=0, b=8, c=14, z=2, u=7, v=1, w=10, t=15.
The two direct edges have distance eight. Along a-u-c-v-b the edge distances are 7,7,7,7; along a-w-z-t-b they are 10,8,7,7. Thus this isolated component is colorable and does not obstruct any outside coloring.

Suppose cz is absent. Each of c,z has at most one outside neighbor. Its available color set is therefore either the entire Z20 or a seven-element cyclic interval A(h). Call these lists I,J.

There exist s in I and r in J with delta(s,r)<=4. If I=Z20 this is immediate. Otherwise its radius-four neighborhood is a fifteen-element cyclic interval, leaving only five colors outside it; a list J containing at least seven colors cannot avoid it. This argument covers repeated outside neighbors as well.

Assign c=s,z=r. The intersection B6(s) intersect B6(r) contains a cyclic interval of span 12-delta(s,r)>=8. Indeed normalize s=0,r=d<=4, giving the signed interval [d-6,6]. Choose two elements at distance exactly seven from this interval and assign them to a,b. They satisfy ab and are each within distance six of both s and r.

Each of the four two-edge paths a-u-c, c-v-b, a-w-z, z-t-b now has endpoint distance at most six, so c01 fills its unique internal vertex. Those internal vertices are distinct and have no other edges. The chosen colors for c,z satisfy their outside constraints, and no other vertex of the configuration has an outside edge. This checks every restored edge and proves A4.

Therefore the eight-vertex configuration cannot occur in a vertex-minimal obstruction. The proof allows arbitrary fixed outside colors; unlike the failed single-pentagon shortcuts, the additional path and its two adjustable middle lists provide the needed flexibility.

## 5. Consequence for the separated-degree-two pentagon target

In m02, a pentagon a-b-u-c-v-a with two separated degree-two vertices forces another five-cycle P-a-b-Q-Z-P, where P,Q are the outside vertices at a,b and Z is their outside common neighbor. If P,Q both had degree two, these two five-cycles would form A4's configuration: the common edge is ab, the two length-four sides pass through c and Z, and their four other vertices are u,v,P,Q of degree two. This is impossible in a minimal obstruction.

Claim A5 (claim:opg401-m04-overlap-degree-growth):
For the common-edge second pentagon forced by m02, at least one of P,Q has degree three.

This is a structural restriction on the actual overlapping cycles, not a claim that any two pentagons sharing an edge are reducible.

## 6. Adversarial scope checks and continuation

A1 needs bridgelessness; otherwise several single-attachment outside components are possible, as in the earlier pendant-boundary witnesses. A2 needs faciality as well as planarity; alternating disjoint paths could use opposite sides of a nonfacial cycle. A3 explicitly retains the exceptional (1,2) cut instead of overstating connectivity. A4 includes the possible cz edge rather than incorrectly treating its two endpoints as free outside-list variables.

Sources: frozen contract and obligation graph; c01 exact local criterion; m01 connectivity, domination and two-edge gluing; m02 forced overlap. All are candidate inputs with explicit proofs and no admitted verification status. No theorem prover, graph enumerator, SAT solver or mathematical computation was run.

best_verified_result: none. best_verified_candidate: none.
Open obligations: obligation:opg401-root; obligation:opg401-z20-extension.
Next target: the connected-outside cubic square from A2, using m03's exact bad-state relation; and the connected three-port pentagons from A1. A future packet must freeze a fresh actual main and content digests before PR transport. These attachment restrictions do not yet provide the final discharging contradiction.
