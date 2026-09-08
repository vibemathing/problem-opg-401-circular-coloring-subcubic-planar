# V04: conflict-Steiner invariance, exact absorption accounting, and a two-axis pivot

Status: NONTERMINAL_CHECKPOINT. Verdict: candidate_only.
Candidate: candidate:opg401-a01-v04-steiner-pivot.
Primary owner: math-proof.
Repository: vibemathing/problem-opg-401-circular-coloring-subcubic-planar.
Problem: problem:opg-401-circular-coloring-subcubic-planar.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1. Target: obligation:opg401-root.
Read base: d6e31ff07b0f3fb20f804da125e57a440545bb3a (after PR28).
Both admitted obligations and all four whole residual classes remain open.

## 1. Frozen input and the exact limitation being examined

All colors are residues in Z20, represented by 0,...,19. Write
r(a,b)=[b-a]20 and delta(a,b)=min(r(a,b),[a-b]20). EdgeOK means
7<=r<=13, equivalently delta>=7 or 7<=abs(a-b)<=13 on these representatives.
O has vertices a,u,b,c,v,d,e,f, edges au,ub,bc,cv,va,cd,de,ef,fb and
outside incidences aP,dQ,eR,fS. The four outside vertices are distinct;
their colors need not be. Their disk order is P,S,R,Q up to reversal.
C1 has (p,q,r,s)=(1,0,2,0) or (14,0,2,0). C2 is their color negation.

H=G-V(O) keeps EVERY original outside edge and its actual valid coloring f.
A fixed set B carries the actual values sigma=f|B. A new coloring must agree
with sigma, not with an existentially chosen representative of its projection.
For tau_k(c)=[k-c]20 define L_k(f) on V(H) by
 uv in E(L_k(f)) iff uv in E(H) and not EdgeOK(tau_k(f(u)),f(v)).
Every conflict edge represents BOTH selector implications u->v and v->u.
It is not necessarily a tight edge (directed difference 7). Do not replace
this conflict graph by the tight-edge digraph. The certificate records each
actual difference, its reverse, the mixed difference, and both implications.

V03 nonuniform-switch/proof.md is a candidate input, not Evidence. We use its
local masks only after restating the relevant witnesses or checking literal
edges. No rejected seven-point replacement family, retained-J family,
selective F, or forty-cycle control is searched or reexecuted here.

## 2. S1: same-axis reflection preserves the ENTIRE conflict graph

Let f be ANY valid coloring of a finite graph H. Let g be obtained by
reflecting a selector U with tau_k, and suppose g is valid. Then
                         L_k(g)=L_k(f).                     (2.1)
Also U is necessarily a union of components of L_k(f).

Proof. Put a=f(u), b=f(v) for an actual edge. If a conflict edge has exactly
one selected end, g violates that edge by definition. Thus a valid selector
cannot cut a conflict component. Conversely a union of components gives a
valid coloring: edges with zero selected ends keep f, edges with two selected
ends use a palette isometry, and crossing edges are mixed-compatible.
To prove (2.1), examine those same three cases. With zero selected ends the
conflict predicate is unchanged. With two selected ends its new mixed pair
is (a,tau_k(b)); applying tau_k to both entries shows this has the same
legality as (tau_k(a),b). With exactly one selected end, the edge was not a
conflict; its new mixed pair is either (a,b) or their simultaneous reflections,
which is legal. Thus it is still not a conflict. Every edge is covered.

Inductively, EVERY sequence of legal reflections using this SAME k preserves
L_k. The composition reflects precisely a symmetric difference of its initial
components. Extra fixed values only remove selectors; they never enable a cut.

Consequently, if P,Q,R,S lie in a single component, no sequence of these
same-axis moves can reflect a nonempty proper subset of the ports. A connecting
conflict tree certifies this for ALL selectors: for any proposed port-splitting
selector choose an inside port and an outside port, follow their tree path,
and exhibit the first crossing conflict edge. Its actual mixed colors fail.
This is an all-size cut proof, not extrapolation from enumerated masks.

Therefore the proposed shortcut 'prune a minimum conflict Steiner tree and
reflect the resulting proper pieces using the original axis' cannot work in
the stated remaining case. Nor can its tree length strictly decrease under
such a move: the entire graph defining that minimum is invariant. This rejects
ONLY this same-axis route. It does not reject changing axis, other recolorings,
absorption, M07, or the minimum-counterexample-specific disjunction.

## 3. S2: what a minimum Steiner tree actually controls

Choose, among all connected subgraphs of L_k(f) containing the four ports,
one with a minimum number of edges. It is a tree T: deleting a cycle edge
would leave connectivity. Every leaf is a port: otherwise deleting that leaf
and its edge improves the objective. Maximum degree is at most three, and
ports have degree at most two in H because their O incidence uses one slot.
The identity n_1=n_3+2 for a finite subcubic tree follows by subtracting twice
the vertex count from its degree sum 2(|V(T)|-1). Hence n_3<=2. Degree-two
vertices can be arbitrarily numerous; neither their number nor the full graph
boundary is bounded by 'at most two branch vertices'. A fixed inherited
rotation on T keeps the order of incidences but does not delete unused edges.

Put W=V(T), n=|W| and Z=W union V(O). The absorbed region is the INDUCED
G[Z], not just the drawing of T. Let
 c=|E(H[W])|-(n-1), and d=sum_{v in W}(3-deg_G(v)).
Assume O has exactly its nine inner edges and four stated leaving incidences.
The exact number b of edges leaving Z is
                         b=n-2-2c-d.                       (3.1)
Indeed G[Z] has 9+4+(n-1)+c=n+12+c edges. O contributes degree sum22,
and W contributes 3n-d, so b=22+3n-d-2(n+12+c). This proves (3.1).

Absorbing an induced subgraph of G never loses simplicity, planarity or the
subcubic bound. Replacing it by a smaller gadget is a DIFFERENT operation:
one must account for ALL b incidences, actual fixed values, and at least one
vertex of net decrease. To invoke a three-port invariant, b=3 (or a genuinely
proved extra-port invariant) is needed, not merely n_3<=2. No universal
absorption impossibility or successful replacement is inferred from (3.1).

There is an additional color-dependent accounting constraint. For even k=2h,
all conflict edges join the two semicircles
 S+={h+1,...,h+9}, S-={h-9,...,h-1} modulo20; colors h,h+10 are isolated.
To prove this, translate h to0. Two colors x,y in1..9 can form a legal edge
only if their separation is7 or8; then x+y is9,10 or11 and the mixed pair is
legal. The negative semicircle follows by negation, and a fixed color of tau
cannot be incident with a conflict. Thus every nontrivial component is bipartite.
Let epsilon(v)=+1 or-1 on these parts, C the component containing all ports,
and let M consist of H edges that are NOT conflicts. Bipartite cancellation gives
 3 sum_C epsilon = sum_{v in C} epsilon(v)(3-deg_G(v))
                  + sum_ports epsilon
                  + sum_{v in C} epsilon(v) deg_M(v).       (3.2)
Each internal conflict edge cancels. The remaining degree incidences include
mixed-compatible internal edges TWICE and edges leaving C once. No edge may
be omitted on the ground that it was not in T.
For C1 p1,k8 the port sum is-4; for p14,k16 it is-2. Therefore the combined
nonport/compatible-edge contribution in (3.2) is respectively1 or2 modulo3.
It cannot vanish. This identifies a required degree or compatibility defect,
but does NOT yet prove that the defect provides a recoloring or smaller gadget.

## 4. S3: an exact two-stage pivot criterion with the SAME actual witness

Fix one actual f, a primary axis k, an auxiliary axis ell, and a target port t.
Write c=f(t), c'=tau_k(c), and I=A(c) intersect A(c'). During stage one ALL
ports and B are fixed. During stage two only t is changed. If t belongs to B
and c'!=c, this move is forbidden.

For every neighbor v of t compare f(v) and tau_ell(f(v)) with I.
If neither is in I, this auxiliary axis fails. If only the reflected value is
in I, require v to be selected. If only the old value is in I, require v to
be unselected. If both are in I, impose no selector restriction. Also require
any vertex of B or of the four ports that is moved by tau_ell to be unselected.
Let U be the union of components of L_ell(f) meeting required selected vertices.

There is a legal first-stage reflection satisfying all these conditions iff
U contains no required unselected vertex. In that case use U ITSELF.
Necessity follows from component closure in section2. Sufficiency follows
from the same edge-by-edge proof and the explicit unary restrictions. A failed
case has either a vertex with no admissible choice, or a path in L_ell(f) from
a required selected vertex to a forbidden one. This is a complete negative
certificate for this specified TWO-STAGE template, not arbitrary recoloring.

Let f1 be the actual reflection on U. It keeps ALL original port values and B.
Every neighbor of t now lies in I, so t is isolated in L_k(f1). Set f2(t)=c'
and f2(v)=f1(v) elsewhere. The incident edges are legal by I; all other edges
were checked for f1; fixed B is respected. If the resulting port tuple has
an O witness, adjoining that witness is a full coloring. This proves
  for EVERY actual f satisfying the criterion, the specified f1,f2 and fill
  are a concrete, composable witness.
It never switches to another coloring having the same projected port tuple.

Finite discovery marks each vertex once. During discovery the lexicographic
pair (undiscovered vertices, work-queue length) decreases at a new discovery
or a queue removal with no discovery. After success the phase descends from
pivot to target-change to O-fill. Trying the twenty auxiliary axes is bounded;
a failed axis does not count as terminal extension. No claim that an axis must
always succeed is made. If later moves are used, their predicates are recomputed
on the ACTUAL f2, not on the old f or on an arbitrary fiber representative.

For C1 p1 choose t=R,k8, so c=2,c'=6 and I={13,14,15}.
For C1 p14 choose t=Q,k16, so c=0,c'=16 and I={7,8,9}.
An explicit O fill for the two resulting tuples, in order a,u,b,c,v,d,e,f, is
 (1,0,6,0): (8,1,14,2,15,9,16,7),
 (14,16,2,0): (4,11,0,10,17,3,14,7).
Check these nine inner and four port edges directly. The initial C1 tuples do
not extend: d,f in[7,13] and e in[9,15] force e=15 and {d,f}={7,8}, since
any d=f prevents the adjacent b,c. Then {b,c}={1,14}, and a must be in
B6(1) intersect B6(14)={15,16,17,18,19,0}, disjoint from A(1) and A(14).
This supplies both negative terminal cases without trusting an old table.

## 5. Four explicit plane controls: the same-axis obstruction is real

These controls target the current Steiner inference, NOT all the earlier
tight-reachability/F blockers and NOT the minimum-root-obstruction subclass.
In particular their extra degree-two vertices violate some earlier necessary
minimum-obstruction conditions. They are not used to withdraw that stronger
claim, and no old forty-cycle is re-tested.

For p1 use H=C8 on0..7 with colors (1,9,0,9,2,9,0,9), ports P0,Q6,R4,S2.
Every edge belongs to L8. The minimum Steiner tree is the path0-1-2-3-4-5-6,
with six edges. For p14 use H=C10 with colors
(14,1,11,0,11,2,11,0,11,1), ports P0,Q7,R5,S3. Every edge belongs to L16.
The minimum tree is0-1-2-3-4-5-6-7, with seven edges. Minimum tree lengths
follow by deleting a largest open gap of the cycle; the longest gaps have
lengths2 and3 respectively. Exhaustive subsets of THESE two edge sets agree.
Every same-axis selector is empty or all vertices. Every port-splitting
selector has an explicit failing edge on the recorded minimum tree path.
By (2.1), the obstruction persists through every same-axis sequence.

The cycle orders8 and10 are sharp ONLY among simple-cycle exteriors with the
prescribed cyclic port order and EVERY exterior cycle edge in the primary
conflict graph. For p1 adjacent specified port colors are never legal, so
four gaps need at least two edges each. For p14 the gaps P-S and Q-P must be
odd by bipartition and cannot have length one (distance6); hence at least3.
The other two gaps are positive even lengths, at least2. This totals10.
No minimum order among all external graphs or minimum counterexamples is claimed.

Nonetheless BOTH controls admit the new pivot, keeping their entire complements:
 p1: ell2, selected{3,5}, targetR4, fixed set{0,1,2,6,7}.
      Two old9 colors become13, then R changes2->6.
 p14: ell0, selected{6,8}, targetQ7, fixed set{0,1,2,3,4,5,9}.
      Two old11 colors become9, then Q changes0->16.
All pins keep their actual values in both stages. The target is isolated in
the recomputed PRIMARY conflict graph after the pivot. Thus this move really
escapes a single all-port primary component, rather than applying N3 where
its initial hypothesis already held.

For the exterior rotation use i:[i-1,i+1] modulo n. For the full graph label
O vertices n..n+7 in the fixed order. At each port insert its O endpoint between
its two listed neighbors; use O rotations
 a:[v,u,P], u:[a,b], b:[u,c,f], c:[b,v,d], v:[c,a],
 d:[e,c,Q], e:[f,d,R], f:[b,e,S].
The resulting graphs have (V,E,F)=(16,21,7) and (18,23,7), respectively.
The certificate contains EVERY edge, rotation, facial walk, original outside
color, pivot color, and full repaired color. Euler characteristic2 and triangle/
degree checks are direct. The two C2 fixtures negate the actual colors and use
axes(12,18) and(4,0). Their full witnesses are checked, not combined with C1.

These are NOT all-absorption failure examples. In fact their Steiner absorption
has b=2, with n,c,d respectively(7,0,3) and(8,0,4), agreeing with (3.1).
In the first graph Z is all vertices except7. With outside color at7 normalized
to0 an entire coloring is
 (12,0,11,4,17,4,11,0,19,12,5,13,6,0,7,18).
Translate this vector to ANY actual color at7. Thus this exact fifteen-vertex
region can be deleted and restored while fixing its whole complement.
In the second graph Z is all vertices except8,9. The retained outside edge is
8--9. For colors0,t there with7<=t<=13, use
 (0,7,14,2,9,1,14,7,0,t,7,14,2,9,0,0,8,15).
The variable entry has only neighbors colored0. Translating handles every
actual legal pair. This exact sixteen-vertex region can be deleted and restored.
These special reductions strictly decrease the graph by15/16 vertices and
preserve every extra edge entirely in the complement. They assume NO further
edges leave Z and no additional pinned vertex inside Z. They do not supply an
absorption rule for an arbitrary Steiner region with b given by (3.1).

## 6. State of the actual minimum-counterexample problem

One proposed operation is now excluded exactly: same-axis splitting or strict
Steiner descent cannot occur once all ports lie in one conflict component.
The absorption alternative is not disproved. The two-axis template gives a
uniform repair on a nonempty explicit domain for BOTH C1 values, and color
negation transfers its criterion, fixed values and witnesses to C2 p19,p6.
None of the four whole residual classes closes.

The first open state remains C1(1,0,2,0), with p14 still required. A narrower
next obligation is the actual minimum-obstruction exterior where the primary
ports stay together and EVERY tested auxiliary-axis pivot certificate fails.
Use (3.2) to locate its required degree/compatible-edge defect, retain the
paths from selected neighbors to forbidden components, and show that this
specific defect permits another same-witness operation or an induced absorbed
region with all boundary incidences accounted for and strict total decrease.
No proof that such a defect always yields a repair, and no counterexample to
that minimum-obstruction assertion, is supplied here. A fixed-set infeasibility
certificate or a same-axis orbit is not a root noncolorability certificate.

## 7. Reproduction, provenance and trust boundaries

Run python3 -I -S run.py in a fresh copy. It refuses to overwrite its replay
directory. The finite checker uses literal edges and standard-library exact
integers; no old table constrains the DFS. Its edge-subset enumeration is only
for the supplied C8/C10 Steiner controls, not a new small-replacement census.
The all-size proofs above do not rely on execution. The replay checks four
fixtures (two and their negations),2800 palette-edge/axis cases,7560 legal
edge-selector invariance cases, all selectors of those four fixtures, exact
minimum Steiner lengths, explicit absorption fills, and12 detected mutations.
Source/input/output hashes, actual runtime version, bounds and exit status are
in execution.json. This is one candidate-generator trust domain; no registered
verifier, Lean/SMT, EvidenceLink, Result, or trusted closure was invoked.

Dependencies: definitions -> S1 edge invariance -> S2 Steiner/cut accounting;
definitions and S1 -> S3 pivot criterion -> explicit terminal fills. (3.2) uses
only bipartite cancellation, not a reused unverified global theorem. Source
locators are the main-base V01 and V03 nonuniform-switch proofs, m06 boundary,
M07 and the retained seven-point proof; the pending matching-and-recolor archive
has been hash-checked but not re-executed. Its intake status is separate from
this proof. Finite controls cannot establish the missing all-exterior coverage.
Probability and asymptotics are not used. The invariants, strict measures and
initial/terminal distinctions are explicit in their individual claims.

closed_residual_classes: []. open_residual_classes: [C1,C2,C3,C4].
best_verified_candidate: none. best_verified_result: none.
Open admitted obligations: obligation:opg401-z20-extension; obligation:opg401-root.
