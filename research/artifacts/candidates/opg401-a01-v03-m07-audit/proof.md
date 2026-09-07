# V03: three-port propagation audit and six remaining boundary states

Status: NONTERMINAL_CHECKPOINT. Verdict: candidate_only.
Candidate: candidate:opg401-a01-v03-m07-audit.
Owner: math-proof. Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1. Target: obligation:opg401-root.
Repository: vibemathing/problem-opg-401-circular-coloring-subcubic-planar.
Read base: 7928d42a5c57e0c94bbc694b1ee2efc63836ee39.
The unpacketized V03 text at 1565e1b8d1d568b7db1f4e08836592ad77df91b1
is retained in branch history; this revision consolidates its proof and the
separate standard-library count audit. No M07 counterexample was found and
NO ENTIRE unconditional m06 residual class is closed. Both admitted
obligations remain open. Transport and these computations are not Evidence.

## 1. Exact graph, colors and failed lift

Ambient graphs are finite simple triangle-free planar with maximum degree
three. Fix an embedding where needed. Colors are represented by 0..19:
r(a,b)=[b-a]20; delta(a,b)=min(r,20-r) is UNDIRECTED shortest distance.
An edge requires r in [7,13], equivalently 7<=|a-b|<=13 for fixed representatives.
A(a)=a+{7,...,13}; B6(a) is its complement. V01's proof and V02's special
patch result are candidate inputs, not verified premises for the root.

The eight vertices, in the standard-library input order, are a,u,b,c,v,d,e,f.
Inner edges are exactly au,ub,bc,cv,va,cd,de,ef,fb. Boundary edges are
 a-alpha, d-Q, e-R, f-S,
with colors (p,q,r,s). The two five-cycles share bc. Only u,v have degree two.
The smaller replacement J has cycle D-U-V-F-E-D and QD,RE,SF; alpha is unused.
J_U adds alpha-U, J_V adds alpha-V. They are different graphs and their
colorings cannot be combined. The m06 replacement uses the two-face disk
with outer boundary a-u-b-f-e-d-c-v-a and port order alpha,S,R,Q.

Translate q to zero, then reflect if necessary to s=h=delta(q,s); p,r follow
the same map. This gives a covering family of 4400 representatives, not
4400 distinct orbits: h=0,10 retain reflection redundancies. Basic bad rows
are h0:r in {19,0,1}; h1..7:r in [0,h]; h8..10:r in {0,h}, for every p.
The additional rows and their remaining states are:

| class | h | r | original bad p (inclusive mod20) | J_U surviving p | J_V surviving p |
|---|---|---|---|---|---|
| C1 | 0 | 2 | [14,21] | 1,14 | 1,14 |
| C2 | 0 | 18 | [19,26] | 6,19 | 6,19 |
| C3 | 1 | 19 | [0,7] | 7 | 0 |
| C4 | 1 | 2 | [14,21] | 1 | 14 |

Old boundary (0,0,2,0) has J colors (D,U,V,F,E)=(7,14,1,8,15).
Cycle distances are 7,7,7,7,8; QD,RE,SF have distances 7,7,8.
Every replacement edge is legal. In the original region E=15 and distinct
(D,F) can only be (7,8) or (8,7). The ear then forces (b,c)=(1,14) or
(14,1). Their B6 intersection is {15,16,17,18,19,0}, disjoint from A(p)=A(0),
so a cannot be filled. The original graph can be colored after changing
its outside colors: inner (0,11,4,16,7,3,10,17), boundary (10,13,0,7).
All thirteen edges are checked. No graph noncolorability is inferred.

## 2. Quantified invariant and absorption

Define ordered B(t,r,s) by r=0,s=h normalization:
h0:every t; h1:t in {7,8,9}; h2:t in {8,9}; h>=3:none.
B is invariant under a common palette translation/reflection, not an
unaccompanied swap of r,s. If r!=s and delta(t,r)<=6 then not B.

Let Z be a proper connected INDUCED region with exactly three leaving
edges z_t T,z_r R,z_s S. Require distinct z_t,z_r,z_s and edge z_r z_s.
Property P(Z) means: for EVERY formal incidence triple (t,r,s) not in B,
there EXISTS c:Z->Z20 legal on EVERY inner edge with c(z_t) in A(t),
c(z_r) in A(r),c(z_s) in A(s). Formal incidence variables are separate;
an actual outside coloring uses only triples compatible with any identified
outside vertices. This is not a promise that B triples extend, nor a claim
restricted to just one ambient deletion coloring.

Suppose T,R,S are distinct vertices, TR is an edge and T,R are cubic.
Let W be T's third neighbor and V be R's third neighbor. Then Z'=Z+{T,R}
has ports (z_s,S),(R,V),(T,W), in roles (t,r,s)=(S,V,W), and P(Z').
Normalize V=0,W=d. Choose x at R in A(0) intersect B6(d), then y at T in
A(d) intersect A(x). P(Z) fills the old region whenever not B(y,x,S).
For 1<=d<=6, x ranges [7,d+6], and y-x ranges [7,13+d-x]. For a fixed x,
all y choices are bad only if S=x, or S=x+1 with at most three y choices.
The distance-two forbidden interval starts at eight, and reversed forbidden
intervals cannot cover the starting value seven. Intersect these failures
across x: d1 gives {7,8}, d2 gives {8}, d3 gives the intersection of
{7,8},{8,9},{9,10}, empty. For d4 the x7 and x8 failures are {7} and {8,9};
for d5,6 they are distinct singleton equalities. For d7..10, x7,8 each
have at least four y choices, while B forbids at most three unless S=x.
For d0 both colors would lie in A(0), which has no legal internal edge.
Thus the new possible bad table B' is h0:all, h1:{7,8}, h2:{8}, else empty.
Since B' is contained in B, the invariant is preserved.

If T or R has degree two, its third-neighbor constraint is absent. Impose
an auxiliary color at distance three from the other new color, or two such
auxiliary colors if both are absent. The d>=3 argument works for every
actual S; removing these stronger auxiliary requirements preserves validity.
No extra graph vertex or edge is introduced by this color argument.

Graph audit: V,W cannot belong to Z (that would be a fourth old boundary
edge), nor be the other T/R again, by simplicity. Z' remains induced,
connected, simple, planar and subcubic as a subgraph of the same G. Its
boundary has exactly the three stated edges and distinct inside endpoints;
R,T are adjacent. Old S remains outside. S=V or S=W may occur. V=W as
VERTICES would already form triangle V-R-T-V, so cannot occur here;
V,W can have equal COLORS. This clarifies the broader coincidence wording
in the retained draft without negating its propagation theorem.

## 3. Maximality, replacements and finite termination

Assume G has minimum vertex order among noncolorable members of the class.
If some Z with |Z|>=3 has P, choose a maximum-order such Z in the finite
power set. No assumption that G-Z is connected or that Z has a simple
facial boundary is imposed.

R=S is impossible: R-z_r-z_s-R would be a triangle. If T=R or T=S,
replace Z by a three-edge R-to-S path with two new vertices. Contracting a
spanning tree of the connected region, deleting loops and suppressing
parallel spokes, then subdividing, proves planarity. This creates no triangle,
even with an existing RS edge (the new cycle has length four). Degrees do
not increase beyond lost incidences. The replacement is smaller. Its coloring
gives r!=s because three increments in [7,13] sum into [21,39], with no
multiple of twenty. With t=r or s, B is false and P lifts the coloring.

If T,R,S are distinct and TR is absent, replace Z by X,Y with TX,RX,XY,YS.
This is the three-spoke star minor with its S edge subdivided. Its only
possible new triangle would use absent TR. Degrees are at most three and
its order is |G|-|Z|+2<|G|. A coloring gives delta(t,r)<=6 from common
neighbor X, and r!=s from the three-edge R-X-Y-S path. Thus not B; P lifts.

If TR is present and a terminal has degree two, the missing-constraint
argument fills Z+{T,R} from any coloring of its smaller deletion. Otherwise
absorption produces a region larger by two with P, contradicting maximality.
In an algorithmic reading, |G|-|Z| decreases by two per absorption, remains
at least one, and permits at most floor((|G|-|Z_initial|-1)/2) steps. The
terminal case supplies a smaller coloring and a genuine lift, not just
failure to grow. Reverse the recorded choices to fill absorbed vertices.
Cut vertices, inner bridges, disconnected complements and repeated facial
walks do not affect the connected-region star-minor construction. Every
outside edge is retained in each replacement. This is the audited M07 P2.

## 4. The nine-vertex seed and the precise P4 dependencies

For alpha=Q=P in the carrier, include P with edges Pa,Pd and third edge PT.
The boundary is PT,eR,fS, with adjacent inside endpoints e,f. Its exact
condition is: choose E in A(r), D in A(E) intersect B6(t), and F in
A(E) intersect A(s), with delta(D,F)>=2. Then choose P in A(t) intersect
A(D) and fill the m02 ear. D=F blocks adjacent b,c. At distance one every
P adjacent to D is in the ear's bad arc; at distance at least two m02's
signed-interval calculation supplies the ear for every P. That calculation
is a named candidate dependency, not a transport-verified theorem.

Normalize r0,s=h. For h>=1, E ranges [7,min(13,h+6)]. Relative to E, the
D-list is empty at t=E, a prefix of A(0) of length j when t-E=j in 1..6,
a suffix of length j when t-E=-j, and all A(0) at larger circular distance.
The F-list is a nonempty prefix or suffix. Lists of length at least three
permit a pair at distance at least two: at length three the only possible
common radius-one point is interior, not an eligible singleton F-list.
For lengths one/two, failure is exactly t-E in {1,2}, s-E in {-6,-5}, or
the reflected alternative. The latter requires h-E>=5, impossible here.
Hence the bad t for E are {E}, enlarged by {E+1,E+2} only at E=h+5,h+6.
Intersecting over E gives B exactly. At h0 adjacent e,f both lie in A(0),
so fail. A direct nine-vertex enumeration confirms both directions.

M07 P4 further uses m01's exclusion of degree-two vertices on C4 and of
three degree-two neighbors at one vertex, and m05's faciality of all-cubic
C4/C5. Given those explicit upstream candidate lemmas: Q=R or R=S makes
a triangle; Q=S makes d-e-f-Q-d, excluded either by its degree-two vertex
or by the impossible shared (ed,ef) facial corner at cubic e. Alpha=R
gives p=r, which occurs in no additional row and J excludes basic rows.
Alpha=Q gives the nine-vertex seed (P cubic and its third neighbor external
by the same exclusions), so P2 applies. Reflect to exclude alpha=S.
P4 excludes equal outside VERTICES, not equal COLORS. These all-size
structural prerequisites are not verified by the finite color enumeration.

## 5. Fixed point and conditional reducibility, not an unconditional closure

For a bad relation C, let F(C)(t,r,s) mean every x adjacent to r and y
adjacent to s with xy legal satisfies C(y,x,t). We have F(B)=B'. Also
F(B')=B': monotonicity gives containment in B'. For reverse inclusion,
h0 has no eligible x,y. At h1 the sole pair is (7,14): t7 makes old
centers equal, t8 gives old triple (7,0,1), in B'. At h2,t8 the three
pairs (7,14),(7,15),(8,15) give (7,0,1),(8,0,1), or equal centers.
These exhaust B'. The same abstract transfer will NOT strictly shrink
these nonempty rows on further iterations. This rejects a stronger
absorption strategy, not M07's actual region-size maximality argument.

A valid SPECIAL reduction: suppose BOTH alpha-Q and alpha-S are actual
outside edges and the four ports are distinct. Then G is colorable iff J
is. A J coloring excludes basic rows. Alpha-Q forces delta(p,q)>=7,
which excludes C1,C2,C4; alpha-S forces delta(p,s)>=7, excluding C3.
The original patch therefore extends. Conversely, any G coloring has D!=F,
so replace the ear by a three-edge D-U-V-F path and retain E and outside.
The size decreases by three. The retained tables.json gives a nonempty
12-vertex example, full coloring and sphere rotation system, including a
repeated facial walk at a leaf. These two edges are hypotheses about G,
not two edges that may freely be inserted. With only alpha-Q, C3 p7 survives.
No unconditional class is eliminated by this conditional proposition.

## 6. Six surviving augmented states and a connected-outside control

Under P4 and the m06 disk assumptions, J_U and J_V are class-preserving:
alpha's lost incidence is restored once; U or V rises to degree three;
the only new triangle needs alpha=Q or alpha=S respectively; the edge
fits the unused disk port. Both replacements are smaller.

In the additional rows J forces E,(D,F) to be C1:15,(7,8)/(8,7);
C2:5,(12,13)/(13,12); C3:6,(13,14); C4:15,(7,8). Consecutive D,F make
the three-edge path unique, with all increments seven or thirteen. The
bad p arc intersected with A(U) is exactly {V}; for J_V it is {U}.
Thus the J_U witnesses in order D,U,V,F,E are:
 C1 p1:(7,14,1,8,15); p14:(8,1,14,7,15).
 C2 p6:(12,19,6,13,5); p19:(13,6,19,12,5).
 C3 p7:(13,0,7,14,6). C4 p1:(7,14,1,8,15).
Every row survives. Excluding 26 individual tuples is not closing a row;
reflection exchanging C1/C2 is not a reducibility theorem either.

The standard-library input gives a stronger fixed-boundary pressure test:
outside cycle alpha-x-S-y-R-z-Q-w-alpha, and edges xN,yN,NM,zM,wM.
Attach its four distinct ports to the eight-vertex region. Fix
alpha1,Q0,R2,S0,x13,y13,z9,w8,N6,M19. The outside graph is connected and
every outside edge is legal. J_U has the C1 p1 witness, but the original
region has no preserving extension. The full 18-vertex original graph is
simple triangle-free planar subcubic and has an explicitly supplied full
coloring with changed outside colors. Its complete rotation system has
V-E+F=18-26+10=2. The 15-vertex augmented replacement has its own rotation
and complete preserving coloring. Both are checked dart by dart.
This is NOT a counterexample to M07 or root: no minimum-noncolorable
assumption holds. It disproves only sufficiency of distinct outside vertices
and connected outside for arbitrary fixed-boundary lifting. No minimality
of this pressure-test graph is claimed and no M07 assertion is withdrawn.

## 7. Actual finite work and reproducibility

The retained C++ engine imports no previous table. It tries every permitted
integer at a selected unassigned vertex and propagates only edge constraints.
Induction on unassigned vertices proves its count exhaustive; each assignment
is counted once. The n<=16, free<=12 bounds and checked uint64 addition
prevent overflow. Its separate Python DFS tests all 32 residual states.
The replay has 4400 original and J boundaries, 220 normalized nine-vertex
triples, full augmented-U counts, 139520 isometry witness checks, 12 actual
mutation witnesses, and 272 specified cofacial gadget probes. No tested
gadget eliminates a whole class without admitting a basic failure. This
is not enumeration of all small planar gadgets; gadget-search.json retains
compact counterexample witnesses for precisely the tested family.

The second engine in stdlib/check.py uses arbitrary-precision integer
variable elimination, memoization and factorization of disconnected residual
subgraphs. Induction proves exactness: zero-domain states contribute zero,
complete assignments one, alternative vertex colors sum, disconnected
components multiply. A separate direct DFS checks 320 graph/boundary cases.
All 4400 normalized boundaries are counted for each of original,J,J_U,J_V.
There are 912 original bad cases and 13594364 total inner completions;
J has 880 bad cases and 938700 completions. Its original/J masks agree
with the C++ replay on all 8800 boundary truth values. P3 is checked on
400 triples after fixing r0, and absorption on all 400 new boundary triples.
The CSV uses four 20-bit masks per h,r row; bit p means extension exists.

Eleven standard-library mutations have detected witnesses: excluding7;
excluding13; wrong directed distance; unreduced reflection; unreduced
translation; inconsistent identified outside vertex colors; requiring
outside colors distinct; omitted bc; secretly changed fixed p; swapped
q/r ports; omitted TR. It checks 8000 edge translations,400 reflections
and384 whole-graph residual transformations. These are two implementations
inside one generator trust domain, not independent verification.

Both run.py files bind actual source/input/output and runtime digests.
Top-level compilation: g++14.2.0, CPU12s/wall15s/memory512MiB; audit child
CPU30s/wall40s/memory256MiB; each engine call wall8s. Standard-library child:
CPython3.13.5, CPU30s/wall40s/memory512MiB, one thread, zero retries,
1MiB per file and64KiB stdout cap. No GPU,CAS,SAT,Lean or trusted verifier ran.
Run the standard-library package in a fresh copy without existing outputs;
it refuses to overwrite observations. Earlier exploratory probes were not
all exhaustive; a resource-limited partial gadget probe is not evidence
of universal failure. All claimed final counts are from the recorded replays.

## 8. Remaining obligation and admission boundary

First unresolved state: C1 (p,q,r,s)=(1,0,2,0), J_U=(7,14,1,8,15), with
alpha and V equal in COLOR. Next task: construct a class-preserving replacement
or allowed outside recoloring that handles both C1 survivors in a hypothetical
minimum obstruction, without combining different replacement colorings,
identifying equal-colored vertices, or reintroducing basic bad states.
The exact nonempty fixed point above rules out merely repeating abstract
absorption as this step. C1,C2,C3,C4 all remain open.

Dependencies: definitions -> local list/path relations -> quantified P ->
absorption -> maximum-region lemma -> nine-vertex seed; the P4 application
also depends on the named m01/m05/m06 structural candidates. Atomic claims:
claim:opg401-v03-absorption, claim:opg401-v03-termination,
claim:opg401-v03-nine-port-table, claim:opg401-v03-fixed-point,
claim:opg401-v03-conditional-reduction, claim:opg401-v03-count-audit,
claim:opg401-v03-connected-outside-warning. Probability and asymptotic methods
are inapplicable. The region-size monovariant, strict replacement decrease,
symmetry fixed points and graph/color quantifier distinctions are explicit.
V02/M09 R1 cover a different one-odd-face outer-C5 patch and are not a
reducibility premise for this outer-eight-cycle two-pentagon region.

best_verified_candidate: none. best_verified_result: none.
closed_residual_classes: []. open_residual_classes: [C1,C2,C3,C4].
Open admitted obligations: obligation:opg401-root; obligation:opg401-z20-extension.
V01 admission-request.json contains the exact statement comparison and pending
policy/formalization/receipt requirements. Registry entries are fixture-based;
the only workflow is the transport gate. No verifier was self-appointed,
no evidence records were written, and CI/merge do not admit a Result.
