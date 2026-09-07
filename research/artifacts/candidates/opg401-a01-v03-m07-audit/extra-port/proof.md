# M07 three-port audit, extra-port reductions, and the four residual rows

Status: NONTERMINAL_CHECKPOINT. Verdict: candidate_only.
Candidate: candidate:opg401-a01-v03-extra-port-audit.
Primary owner: math-proof; finite calculations are candidate-generator checks.
Problem: problem:opg-401-circular-coloring-subcubic-planar.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1. Target: obligation:opg401-root.
Read base: 7928d42a5c57e0c94bbc694b1ee2efc63836ee39.
Local obligation: obligation:opg401-z20-extension remains open.

## Relation to the retained V03 candidate

The existing unpacketized branch payload at f872b4f248707d4fedcc06021974bcb9c1a89c5d
is preserved without overwriting its proof, C++ engine, standard-library engine
or recorded observations. Its ../proof.md supplies the frozen m06 graph, the
four residual rows C1-C4, complete M07 audit, old failed lifting witness and
a connected-outside pressure test. Here K1-K4 denote those same C1-C4 rows,
not new admitted obligation IDs. This supplement strengthens the region lemma
and gives additional degree/adjacency restrictions. It does not eliminate an
entire color row. The scripts and execution.json in THIS subdirectory are a
new edge-matrix/direct-DFS cross-check; they do not import either retained engine.
The retained observations are not represented as new executions by this supplement.

At the frozen main, the colors use r(a,b)=[b-a]20, shortest delta=min(r,20-r),
and EdgeOK iff 7<=r<=13, equivalently 7<=abs(a-b)<=13 for representatives 0..19.
A(a)=a+{7,...,13}; B6(a) is the radius-six ball. The original graph has edges
au,ub,bc,cv,va,cd,de,ef,fb and outside edges aP,dQ,eR,fS with colors p,q,r,s.
J is D-U-V-F-E-D with QD,RE,SF; JU adds PU; JqV adds QV only as a palette test.
After q=0 and s=h normalization, K1=(h0,r2,p in [14,21]20),
K2=(h0,r18,p in [19,26]20), K3=(h1,r19,p in [0,7]),
K4=(h1,r2,p in [14,21]20). Outside vertices are different from color variables.
The explicit rotation, old edge-by-edge witness checks and full normalized table
are also included in this subdirectory's audit.json and boundary-table.csv.

## 3. A local ear input with its derivation

For the 122 ear a-u-b-c-v-a, let the outside colors at a,b,c be p,F,D.
It extends iff D!=F and either delta(D,F)>=2 or p is outside A(D) union A(F).
In the latter alternative delta(D,F)=1 is understood.

For completeness, fix color z at a and translate z to zero. A boundary color
P in 1,...,19 gives the allowed signed lifts at the adjacent branch vertex
I(P)=[max(-6,P-13),min(6,P-7)]; P=0 gives the empty set. Two lifts lie in
[-6,6], so their edge is legal exactly when their ordinary separation is at
least seven. For P<Q the maximum separation is
min(6,Q-7)-max(-6,P-13), which is at least seven iff P<=12 and Q>=8.
This follows by separating P<=7 from P>=8 and clipping the endpoints at six.

Now normalize F=0,D=d in 1,...,10. The possible colors at a BEFORE imposing
its p edge are exactly [1,d-1] union [max(8,d+1),min(19,d+12)]. The endpoints
0,d give an empty branch list. For 1<=z<d the two residues are d-z,20-z;
for d<z<=19 they are 20-z,20+d-z. Applying the preceding endpoint test gives
the two displayed intervals. When d=1 this is [8,13], avoided by A(p) exactly
for p=7,...,14=A(0) union A(1). For 2<=d<=6 the complement consists of two
arcs, each of at most six colors, so cannot contain the seven consecutive
colors of A(p). For 7<=d<=10 the complement is just {0,d}. Equal D,F cannot
color adjacent b,c in their common span-six interval. This proves the input,
including both directions, and supplies choices that fill the two 2-edge paths.

For the four additional rows, the only distinct (D,F) and their central E are:
K1: E=15,(7,8) or (8,7); K2: E=5,(12,13) or (13,12);
K3: E=6,(13,14); K4: E=15,(7,8).
Intersecting the two lists A(q) intersect A(E), A(s) intersect A(E) gives
these entries; requiring a separation of two instead gives no E in A(r).
Their bad-p sets follow from the just-proved ear input. All four rows really
are nonempty fixed-boundary obstructions.

## 4. M07's quantified three-port invariant and absorption

Define B(t,r,s) by normalizing r=0,s=h with one palette isometry:
h=0: every t; h=1: t in {7,8,9}; h=2: t in {8,9}; h>=3: no t.
At h=0 or 10 the reflection choice has no effect. In particular
r!=s and delta(t,r)<=6 imply not B(t,r,s).

STRONG LOCAL PROPERTY U_B: Z is an induced connected region, and three
selected boundary edges have distinct inside endpoints z_t,z_r,z_s with
z_r z_s an edge. For EVERY assignment eta of colors to all boundary-edge
slots, not B(eta_t,eta_r,eta_s) implies the existence of an internal coloring
satisfying every internal edge AND EVERY boundary incidence. Boundary slots
are quantified independently even if actual outside vertices coincide.
Actual outside colorings are a subset of these assignments. This stronger
premise avoids a vacuous property depending on one uncolorable complement.

M07 has exactly three boundary edges. We state and prove the stronger version
allowing extra boundary edges whose colors are still universally quantified.
Extra constraints are never removed from the extension conclusion.

Let the selected outside endpoints be distinct T,R,S and suppose TR is an
ambient edge. Write y=color(T), x=color(R). A residual outside neighbor W
of T and V of R, when both exist outside Z, has specified colors. Normalize
V=0,W=d. All choices satisfying their edges and TR are
x in A(0) intersect B6(d), y in A(d) intersect A(x). We must avoid B(y,x,z),
where z is the unchanged color at S. The exact worst transfer table is:

| d | z for which every such choice is forbidden |
|---|---|
| 0 | all |
| 1 | 7,8 |
| 2 | 8 |
| 3..10 | none |

For 1<=d<=6, x=7,...,d+6 and y-x ranges over [7,13+d-x]. For each x,
all y are forbidden only if z=x, or z=x+1 and this interval has at most
three elements. The difference-two B row cannot contain its starting value
seven; negative differences reflect it outside the B row. At d=1 the bad
set is {7,8}; at d=2 it is {7,8} intersect {8,9}={8}. At d=3 the three
sets {7,8},{8,9},{9,10} have empty intersection. At d=4 use x=7,8 to get
{7} and {8,9}; at d=5,6 those two x each force a distinct singleton z.
For 7<=d<=10, x=7 and x=8 each have at least four possible y, whereas B
for z!=x forbids at most three. They cannot both fail. At d=0 the two
adjacent vertices would both be in A(0), impossible. This proves the table.
It is contained in B(z,0,d), so the enlarged region preserves U_B.

The new selected inside endpoints are old z_s,R,T, and outside roles are
S,V,W. For each fixed assignment on the other boundary slots, choose x,y
as above and assign these colors to every consumed old boundary slot ending
at R,T. The old U_B then satisfies those incidences as well as all unconsumed
extra incidences. Thus the quantifier over extra constraints is preserved.

A residual outside neighbor is missing if T or R has degree two, or if its
third incidence goes back to Z through an extra boundary edge. Impose an
auxiliary color for the missing constraint at distance at least three from
the other residual color (or choose two such colors if both are missing).
The transfer table then permits every actual color at S. The auxiliary
constraint only narrows choices; no artificial graph vertex is introduced.
All consumed extra incidences are still checked by the old U_B.

## 5. Maximality, all alias cases, and finite termination

Claim V03-U: no minimum obstruction contains such a U_B region of size at
least three, including the version with extra universally handled boundary
edges. Suppose otherwise, and choose a largest such region in this finite G.

The outside endpoints R,S are different, since equality with the inside edge
z_r z_s would create a triangle. If T=R or T=S, delete Z and replace it by
a 3-edge R-to-S path with two new vertices. Contracting a spanning tree of Z,
deleting extra boundary incidences and suppressing parallel edges gives a
2-terminal star; subdividing it gives the replacement, so it is planar.
It is simple and triangle-free even if RS is already present: the new cycle
then has length four. No outside degree exceeds its old value. The replacement
has fewer vertices, and a coloring exists by minimality. Three legal increments
sum into [21,39], so its endpoint colors differ. With t=r or t=s, not B holds,
and U_B restores all deleted edges while keeping the entire complement fixed.

Now T,R,S are distinct. If TR is absent, replace Z by new X,Y and edges
TX,RX,XY,YS. This is the contracted 3-terminal star with its S-edge subdivided;
extra old boundary edges are deleted, not reinterpreted as free obligations.
Only TR could create a new triangle, and it is absent. Outside degrees do
not grow and |Z|>=3 makes the graph smaller. Its coloring gives delta(t,r)<=6
via common X, and r!=s via R-X-Y-S. Thus not B holds, and the full U_B lifts it.

If TR is present and either residual outside constraint is missing, the
previous section extends a coloring of G-(Z union {T,R}) for every actual
remaining boundary assignment, a contradiction. Otherwise both residual
neighbors are outside Z. Set Z'=Z union {T,R}. This is connected and induced;
it gains exactly two vertices. Its selected inside endpoints old z_s,R,T
are distinct, and R,T are adjacent. The old S remains outside, so Z' is proper.
Its remaining extra boundary incidences are inherited, and the previous
section proves U_B for them. This contradicts maximality.

Aliasing S=V or S=W causes no unrecorded edge and is handled by the next
alias case; V=W would already create triangle T-R-V in the ambient graph.
The proof does not require the complement to be connected or 2-connected.
Contraction of a connected plane subgraph and subdivision work even with
cut vertices or repeated facial walks. Intermediary contracted multigraphs
are not claimed to be members of the root class; the final replacements are.
The invariant is U_B with its full quantifiers. The decreasing natural number
|V(G)|-|Z| drops by two on absorption; at most floor((|V(G)|-|Z0|)/2) absorptions
are possible. Each terminal case has an explicit smaller-graph coloring lift.
This is not an assertion that a stalled recoloring algorithm proves the root.

## 6. Audit of the nine-vertex specialization and repeated terminals

In O identify the outside vertices P=Q and include that vertex in Z. Its
third neighbor is T; the other ports are R at e and S at f. For colors D,E,F
at d,e,f and a prospective color x at P, the two edges PT,Pd give
D in B6(t). If D=F the ear cannot extend. If delta(D,F)=1 it is also blocked,
since x in A(D) belongs to the bad ear arc. If delta(D,F)>=2 it extends for
every x. Therefore the exact feasible condition is
E in A(r), D in A(E) intersect B6(t), F in A(E) intersect A(s), delta(D,F)>=2.

Normalize r=0,s=h. For h>=1 the possible E are 7,...,min(13,h+6).
At fixed E translate E to zero. The first list is empty for t=E, a prefix
[7,6+j] if t-E=j in 1..6, a suffix [14-j,13] if t-E=-j, and all of A(0)
if the distance is at least seven. The second nonempty list is a prefix or
suffix of A(0). A first list of length at least three permits separation
at least two from a member of the second: even at length three, its only
possible radius-one central singleton is not an endpoint singleton.
For first-list lengths one or two, failure occurs exactly at the same end:
t-E in {1,2}, s-E in {-6,-5}, or their simultaneous negatives.
In the normalized E range only the first alternative can occur. Hence the
bad t for fixed E are {E}, plus {E+1,E+2} only for E=h+5 or h+6.
Intersecting over E gives h=1: {7,8,9}; h=2: {8,9}; h>=3: empty. At h=0,
e,f cannot be adjacent within A(0), so every t is bad. This is exactly B.

Thus M07 P1, P2 and P3 have a complete candidate proof; the graph-edge checker
agrees on every normalized transfer and all 400 normalized nine-vertex states.
No counterexample to those precise claims was obtained.

M07 P4's carrier-terminal distinctness uses additional structural inputs.
Here is its dependency audit, not a silent elevation of those inputs:
Q=R or R=S creates a triangle on de or ef. If Q=S=W, the 4-cycle d-e-f-W-d
has either a forbidden degree-two vertex W (m01) or is all cubic and facial
(m05 C2). In the latter case it and the facial carrier C5 would both use the
same ed,ef corner at degree-three e, impossible in a cyclic order of three
incidences. P=R is excluded by the smaller J: p=r lies in no extra row, and
basic rows cannot color J. If P=Q, that vertex has degree three because a
already has two degree-two neighbors u,v (m01 M4 excludes three). Its third
neighbor is outside O by saturation, triangles, and the just-excluded Q=S.
The nine-vertex region above has U_B and is excluded by V03-U. P=S is its
carrier reflection. This distinguishes vertex identities from color equalities.

The pertinent m01 folding argument identifies two degree-two neighbors of
a cubic vertex when their other ends are nonadjacent; their new common
neighborhood has size three and has no internal edge. A local face angle
supplies a planar identification, and the graph strictly loses a vertex.
Applying this to all three degree-two neighbors would force a triangle among
their other ends. The m05 faciality input uses the earlier two-edge-bond/thread
reductions to rule out outside components with two attachments; with at most
five attachments the deletion is then connected and lies on one side.
Those earlier core/separator reductions are explicit dependencies, not all
revalidated by this finite palette check. The isolated U_B theorem needs none
of them, and remains a useful separately testable reducible configuration.

## 7. New necessary local structure from extra boundary ports

Work in the precise m06 carrier setting with the structural inputs just named.
Claim V03-D: all four distinct outside vertices P,Q,R,S have degree three in
a hypothetical minimum obstruction. P is already forced by the two degree-two
neighbors of a. Suppose Q has degree two with other neighbor T. Include Q
in O. The remaining selected ports are QT,eR,fS, with inside endpoints Q,e,f;
aP is an EXTRA port. For not B(t,r,s), the list argument in section 6 chooses
E,D,F with delta(D,F)>=2 and D in B6(t). Choose color(Q) in A(t) intersect
A(D). The ear input extends for EVERY p at the extra port aP. Hence this
nine-vertex region has U_B, and V03-U excludes it. The reflection excludes
degree two at S as well. The third neighbor cannot have been in O: saturation,
triangles and distinctness of P,Q,R,S exclude each possible additional incidence.

Suppose instead R has degree two, with other neighbor T. Take a coloring of
the smaller J, whose q,s distance is at most one by m06. Hold all vertices
outside O union {R} fixed. The set of central colors E permitting D,F with
separation at least two is N2(q,s). At q=s it is B4(q), of size nine; at
distance one, normalized q=0,s=1, it is [-4,5], of size ten. To derive this,
translate E to zero and intersect A(q),A(s) with A(E); their endpoint maximum
separation fails to reach two exactly when both signed center lifts lie in
{5,6} or both in {-6,-5}. These give the displayed intervals.
B6(color(T)) has thirteen colors, so it intersects either N2 by cardinality.
Choose E in that intersection, choose D,F with separation at least two, and
choose color(R) in A(E) intersect A(color(T)). The ear extends for every p.
All remaining outside edges and both edges incident with R are satisfied.
This contradicts minimum noncolorability. Minimum degree is at least two by
single-vertex extension, so all four outside vertices are cubic.

Claim V03-E: neither QR nor RS can be an edge in that minimum setting.
Suppose QR is an edge and absorb Q,R into O, leaving extra port aP. The
selected inside endpoints are f,R,Q with adjacent R,Q; their outside roles
are S,V,W, where V,W are the remaining neighbors of R,Q. Distinctness and
induced shape ensure V,W stay outside; aliases with other outside vertices
are allowed. For chosen x=color(R), y=color(Q), a legal xy gives delta(x,y)>=7.
The original region extends for EVERY p provided x!=color(S). Indeed its
only possible bad states when q and r form a legal edge are r=s in the basic
table: the extra rows have delta(q,r)<=2. This follows either from that
hand table or the N2 endpoint test above.
Normalize V=0,W=d. Choose x in A(0),y in A(d),y in A(x),x!=color(S).
The exact failure table is d=0: every color(S); d=1: only 7; d>=2: none.
For d=1 only x=7 is possible; for d>=2 both x=7,8 are possible. This table
is contained in B and hence proves U_B for the enlarged ten-vertex region,
including its extra p port. V03-U excludes it. Reflecting proves RS absent.

These are necessary reducible-configuration restrictions, NOT deletion of
any entire K row. The completed checker verifies 4400 extra-p Q-absorption
states, 800 R-absorption states with q,s at distance at most one, and every
normalized QR transfer. The all-size graph deductions use the hand proof.

## 8. Exact enumeration, negative controls, and the actual remaining gap

engine.py builds its adjacency matrix from 7<=abs(x-y)<=13. For a path,
T_next[a,b]=sum_x T[a,x]*allowed(x)*EdgeOK(x,b) enumerates every internal
color. Products for internally disjoint paths are conditional on their common
endpoint colors; summing endpoints counts every full coloring exactly once.
O's three b-to-c paths and J's two D-to-F paths are checked against the explicit
edge lists before counting. This construction never calls an old table or
imports old candidate code. A separately implemented direct-edge DFS supplies
positive witnesses and checks zero/nonzero for all 4400 normalized boundaries.
Boundary-table.csv has 220 rows; bit p in original_p_mask or JU_p_mask records
extendibility for that p. The CSV therefore covers all 4400 states. Counts are
integers, not numerical tolerances. Dynamic programming sums over all internal
colors; it does not claim to explicitly print 20^8 assignments per boundary.

The executed comparison found 912 bad normalized states, no disagreements,
400 correct nine-vertex states (30 bad before translation), and the M07 transfer
table above. Thirteen mutations are detected with actual witnesses: excluded
7; excluded 13; directed difference without the upper bound; failure to reflect
p; translating internal colors alone; ignoring an identified outside vertex;
omitting bc; secretly recoloring the fixed outside; omitting color 19; swapping
T,R absorption roles; omitting exactly DU; flipping a certificate bit; and
ignoring QV's outside degree growth. No claim of trusted verification is made.

After JU, the extra rows retain exactly these p values and internal witnesses:

| row | surviving p | (D,U,V,F,E) |
|---|---|---|
| K1 | 1 | (7,14,1,8,15) |
| K1 | 14 | (8,1,14,7,15) |
| K2 | 6 | (12,19,6,13,5) |
| K2 | 19 | (13,6,19,12,5) |
| K3 | 7 | (13,0,7,14,6) |
| K4 | 1 | (7,14,1,8,15) |

Every one satisfies p=color(V), exactly M07's forced-equality conclusion.
All rows survive on palette patches with DISTINCT outside vertices. These
patches are not asserted to be minimum obstructions; they show why distinct
vertices and a forced color equality do not by themselves remove a row.

JqV numerically removes K1,K2,K4 and retains K3. This is NOT an admissible
reduction in the remaining minimum setting: Q already lost only one original
edge but regains QD AND QV, giving degree four when Q was cubic. An explicit
witness is O with four pendants and two extra leaves at Q: the original graph
is planar triangle-free subcubic, while the proposed replacement has Q degree
four. Its edge list and the degree mutation are in audit.json. The inference
from the JqV table to whole-row elimination is withdrawn, not M07 itself.

The additional bounded search tests exactly the 71 parameterized cycle/theta
replacements generated in engine.small_replacements(), NOT all possible
seven-vertex patches. Each admits either a basic bad boundary or a witness
in each of K1,K2,K3,K4. replacement-screen.json freezes those witnesses in
compact indexed form; the same script decodes them and checks every edge.
This is a finite rejection certificate for that particular search family.

## 9. Verification boundaries, stopping state, and next obligation

Invariant checks, alias cases, strict size decrease, and smallest palette
boundaries are explicit above. No induction from sample graphs, probability,
asymptotic argument, or GPU computation is used. Local finite tests are not
an all-graph proof. All scripts, input, compact outputs, actual versions,
resource limits, binary/input/source/output hashes and exit status are in
execution.json. Reproduce with python3 -I -S run.py in this directory.
The runtime is the foreground candidate-generator sandbox, not the repository
command lane and not a verifier principal. No Lean or SMT was run.

Result for the requested milestone: NO entire residual color row is globally
eliminated and NO counterexample to M07 was obtained. Therefore this package
is NONTERMINAL_CHECKPOINT, not RESULT_CANDIDATE_READY for that milestone.
The strengthened U_B theorem and degree/adjacency reductions are bounded
candidate progress; they must not be relabeled as the requested row closure.

Remaining rows: K1,K2,K3,K4. First remaining JU boundary: (p,q,r,s)=(1,0,2,0),
with the first witness in section 8. The unaugmented old witness (0,0,2,0)
is also still a genuine fixed-boundary obstruction. Next exact obligation:
for a minimum obstruction with this carrier, four DISTINCT CUBIC outside
vertices, and QR,RS absent, find a class-preserving replacement or allowed
outside recoloring that escapes K1; do not use the degree-four QV operation
or combine colorings of different augmented replacements.

V01's separate statement comparison and admission-request.json bind its exact
proof and 400-pair certificate. Registered Lean principal names have only
fixture policies; the sole current workflow is the three transport checks.
There is no suitable verified invocation/receipt in this task. Request status
remains pending; fingerprint and trusted run are null. Both admitted obligations
remain open. best_verified_candidate=none; best_verified_result=none.

Source locators at the read base: m06-single-ear-boundary; m07-three-port-
propagation; m01-critical-structure; m02-pentagon-122; m05-pentagon-clusters;
v01-local-audit/proof; v02-m09-r1-audit/proof; m09-pentagonal-retraction-draft;
research/verifiers.json; research/records/obligation-graphs.jsonl. These are
candidate inputs and repository policy data, not mathematical EvidenceLinks.
