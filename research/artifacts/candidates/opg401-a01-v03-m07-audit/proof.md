# M07 three-port audit, exact boundary certificates, and the remaining gap

Status: NONTERMINAL_CHECKPOINT. Verdict: candidate_only.
Candidate: candidate:opg401-a01-v03-m07-audit.
Primary owner: math-proof (same admitted derivation route).
Problem: problem:opg-401-circular-coloring-subcubic-planar.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1. Target: obligation:opg401-root.
Read revision: 7928d42a5c57e0c94bbc694b1ee2efc63836ee39.
Local dependency obligation:opg401-z20-extension remains open.

This package does NOT eliminate an unconditional M06 residual class. No
counterexample to M07 P1-P3 was found. It gives a quantified proof audit,
complete finite cross-checks, a new conditional reducible configuration,
and an exact obstruction to a proposed stronger absorption strategy.
The finite programs and this proof are in the generator trust domain.

## 1. Frozen objects, both replacement directions, and the old witness

Colors are Z20 with representatives 0..19. Write r(x,y)=[y-x]20 and
Delta(x,y)=min(r(x,y),20-r(x,y)). Delta is UNDIRECTED and at most ten.
An edge is legal iff 7<=r(x,y)<=13, equivalently
7<=|x-y|<=13 on these fixed representatives, equivalently Delta(x,y)>=7.
A(x)=x+{7,...,13}. V01 supplies the hand argument for
|A(x) intersect A(y)|=max(0,7-Delta(x,y)); its status remains candidate.
No arbitrary integer lift is used in the absolute-value predicate.

M06's induced region has eight distinct vertices a,b,c,d,e,f,u,v and
EXACTLY nine internal edges:
  bc, cd, de, ef, fb, au, ub, cv, va.
The shared edge bc is counted once. Its four boundary edges are
  a-alpha, d-Q, e-R, f-S,
with boundary colors p,q,r,s. The vertices u,v have degree two; the other
six have degree three after restoring the boundary edges. Outside
vertices may coincide only when their actual graph and fixed colors
permit it. Vertex identification is not equality of color values.

The smaller graph J replaces these eight vertices by the five-cycle
  D-U-V-F-E-D
and edges QD, RE, SF. The alpha incidence is not restored. Its vertex
count is smaller by three. In the M06 carrier setting the region is a
two-face disk with simple outer boundary a-u-b-f-e-d-c-v-a; the port
order is alpha,S,R,Q. This disk hypothesis is part of the replacement
argument, not a property inferred from boundary colors alone.

Translate q to zero and, if necessary, reflect all colors to make s=h,
where h=Delta(q,s) is in 0..10. Transform p,r by the same isometry.
The basic bad states, for every p, are:
  h=0: r in {19,0,1};
  1<=h<=7: r in {0,...,h};
  8<=h<=10: r in {0,h}.
The four additional bad rows are:

| class | h | r | bad p | distinct D,F in a J coloring | E |
|---|---:|---:|---|---|---:|
| I | 0 | 2 | {14,15,16,17,18,19,0,1} | (7,8) or (8,7) | 15 |
| II | 0 | 18 | {19,0,1,2,3,4,5,6} | (12,13) or (13,12) | 5 |
| III | 1 | 19 | {0,1,2,3,4,5,6,7} | (13,14) | 6 |
| IV | 1 | 2 | {14,15,16,17,18,19,0,1} | (7,8) | 15 |

The displayed normalization is a covering family of 4400 representatives,
not an assertion of 4400 distinct symmetry orbits; fixed points h=0,10
retain some redundant representatives. No omitted-state conclusion is
based on incorrectly weighting these fixed points.

For the existing witness (p,q,r,s)=(0,0,2,0), color J in order D,U,V,F,E
by 7,14,1,8,15. Its nine-vertex version includes four distinct outside
vertices, with alpha isolated. Check every edge:

| edge | colors | shortest distance |
|---|---|---:|
| DU | 7,14 | 7 |
| UV | 14,1 | 7 |
| VF | 1,8 | 7 |
| FE | 8,15 | 7 |
| ED | 15,7 | 8 |
| QD | 0,7 | 7 |
| RE | 2,15 | 7 |
| SF | 0,8 | 8 |

The original region cannot preserve this boundary. The only distinct
D,F choices are (7,8) and (8,7), with E=15. Adjacent b,c must then have
colors (1,14) or (14,1). The two length-two paths require the color of
a to lie in B6(b) intersect B6(c). For (D,F)=(7,8), b=1,c=14, so
B6(1) intersect B6(14)={15,16,17,18,19,0}.
This is disjoint from A(0)={7,...,13}. Interchanging D,F gives the same
intersection. Thus there is no preserving extension.

The pendant version of the original graph itself is colorable: in order
(a,b,c,d,e,f,u,v,p,q,r,s) use
  (0,4,16,3,10,17,11,7,10,13,0,7).
All thirteen edges are checked by audit.py. fixtures.json gives its full
rotation system. Facial permutation (u,v)->(v,next_v(u)) has three
orbits and V-E+F=12-13+3=2. This is a planar triangle-free subcubic
witness AGAINST universal fixed-boundary lifting, not against the root.

## 2. Quantified three-port lemma

Define B(t,r,s) as follows. Translate r to zero and reflect s to
h=Delta(r,s), transforming t by the same operation. B holds for:
  h=0, every t; h=1, t in {7,8,9}; h=2, t in {8,9}; no other case.
This ordered relation is invariant under common palette isometries.
It is NOT invariant under swapping the r and s roles without also
changing the graph. For example B(8,0,1) holds but B(8,1,0) does not.
In particular, r!=s and Delta(t,r)<=6 implies not B(t,r,s).

A local three-port graph is an induced connected vertex set Z in a
finite simple triangle-free planar subcubic graph G, with distinct
inside endpoints z_t,z_r,z_s and exactly the boundary edges
  z_t T, z_r R, z_s S,
and with z_r z_s an edge. Define its property P by the FULL quantifiers:

For every (t,r,s) in Z20^3, if not B(t,r,s), there exists a coloring
f:Z->Z20 legal on EVERY edge of G[Z], with
  f(z_t) adjacent in the palette to t,
  f(z_r) adjacent in the palette to r,
  f(z_s) adjacent in the palette to s.

This is a statement about the local graph with three labeled dangling
incidences, not just about colors attainable in one particular outside
component. If actual outside vertices are identified, only compatible
triples are used when P is applied. The proof never assigns two colors
to one vertex.

Candidate lemma L1: if T,R,S are distinct, TR is an edge, and T,R have
degree three, then Z'=Z union {T,R} has property P. Its new port roles
(t,r,s) are (S,V,W), where W is T's remaining neighbor and V is R's
remaining neighbor. Its new inside endpoints are (z_s,R,T).
Its possible bad triples are contained in B', defined by
  h=0, all t; h=1, t in {7,8}; h=2, t=8; no other case.
Thus B' is a subset of B.

Proof. Normalize the new colors at V,W to 0,d. Choose x at R in
A(0) intersect B6(d), and y at T in A(d) intersect A(x). The old
region extends whenever not B(y,x,t), with t the color at S.
For 1<=d<=6 the possible x are exactly 7..d+6, and y-x ranges over
7..13+d-x. For a fixed x all these choices are bad only for S=x,
or for S=x+1 when there are at most three choices of y. The h=2
part of the old B cannot contain the starting increment seven;
negative relative differences also do not contain it.
For d=1 the only pair is (x,y)=(7,14), leaving S=7,8. For d=2,
x=7 leaves S in {7,8} and x=8 leaves S in {8,9}, leaving only 8.
For d=3 intersect {7,8},{8,9},{9,10}, obtaining the empty set.
For d=4 the x=7 and x=8 tests give {7} and {8,9}, disjoint.
For d=5,6 both x=7,8 have at least four y choices, and would force
incompatible equalities S=7 and S=8. For 7<=d<=10 those same x
are available and each has at least four y choices; when S!=x,
B forbids at most three y colors. At d=0 no adjacent pair of
colors both in A(0) exists. This proves the bound B' in all cases.
The chosen colors check TW, RV and TR; P checks every old incidence.

If one of T,R has degree two, omit its nonexistent outside constraint.
Temporarily impose an auxiliary color at distance at least three from
the other new constraint, or choose two such colors if both are absent.
The d>=3 case proves extension for every real color at S. This is a
stronger palette restriction used in a proof, not a new vertex or edge.

## 3. Topological and termination audit of M07 P2

Candidate lemma L2: a graph of minimum vertex order among the noncolorable
members of the frozen class cannot contain a region satisfying P with
|Z|>=3 and the three-port geometry above.

Assume such a minimum graph G and choose a region Z of maximum order
among those satisfying the stated local conditions. The maximum exists
in the finite power set of V(G). G-Z is not required to be connected.

First R!=S, because R=S would create the triangle R-z_r-z_s-R.
If T=R or T=S, replace Z by a three-edge R-to-S path with two new
internal vertices. This replacement is planar: contract a spanning
tree of G[Z], delete its internal loops, suppress duplicated terminal
edges, and subdivide the resulting two-terminal path. It remains
triangle-free even when RS already exists (the new cycle has length
four). Outside degrees regain no more than the deleted incidences.
Its order is |G|-|Z|+2<|G|. A coloring gives r!=s, and t=r or t=s,
so not B and P lifts it, a contradiction.

Now T,R,S are distinct. If TR is absent, replace Z by two new vertices
X,Y and edges TX,RX,XY,YS. Contracting the connected region gives a
three-terminal star; subdividing its S-edge gives exactly this gadget.
The only possible new triangle is T-X-R-T, excluded by TR being absent.
Existing TS or RS edges create only four-cycles. Degrees are at most
three. A coloring of this smaller graph has Delta(t,r)<=6 and r!=s
(the latter from the three-edge path R-X-Y-S), so P again lifts it.

If TR is present and either endpoint has degree two, L1's missing-port
argument lifts any coloring of G-(Z union {T,R}), which is smaller.
Otherwise both have degree three. L1 applies to Z'=Z union {T,R}.
This is INDUCED and connected; it is still simple, planar and subcubic
because it is an induced subgraph of the unchanged G, not a contraction
with uncontrolled degrees. Its only boundary edges are z_s S, RV, TW.
The remaining neighbors V,W cannot be old vertices of Z: that would
have been a fourth old boundary edge. They cannot be the other member
of {T,R} again, by simplicity. They may coincide with each other or S;
those identifications do not alter the three distinct inside endpoints
and are handled by the earlier identified-terminal case. Simultaneous
V=W=S would already create the triangle TRS and cannot arise.
The new distinguished endpoints R,T are adjacent, while z_s is a third
distinct inside vertex. The old S stays outside, so Z' is proper.
Finally |Z'|=|Z|+2, contradicting the chosen maximum.

No facial-boundary simplicity or outside connectivity is used in this
lemma. Articulation vertices and repeated facial boundary walks cause
no missing case: only a connected induced region, its exact edge cut,
and elementary planar contractions are used. In an algorithmic reading,
|V(G)|-|Z| strictly decreases by two on every absorption; an unchanged
outside S ensures a positive remainder. The proof is finite maximality,
not an assertion that an unbounded search ran or that repeated local
improvement alone supplies a coloring.

## 4. M07 P3 and P4: exact local relation versus structural prerequisites

In the repeated-terminal carrier, identify the actual outside neighbors
of a,d as P and include P in the region. Its ninth vertex has third
neighbor T; the other outside incidences are eR,fS. No other internal
edge is present in this local statement. Let E be the color at e.
Exactly the following choices yield an extension:
  E in A(r), D in A(E) intersect B6(t),
  F in A(E) intersect A(s), Delta(D,F)>=2.
A common color for P exists precisely because Delta(t,D)<=6.
If D=F the adjacent b,c cannot be colored in a shared seven-color arc.
If Delta(D,F)=1, their colors are forced to opposite endpoints; the
color of P, being adjacent to D, blocks the remaining ear. For distance
at least two the M02 ear interval calculation supplies the extension
for every chosen P color. M02's signed-interval proof is a generated
dependency, not a transport-derived premise.

For a direct audit of that small ear input, normalizing D=0,F=d with
1<=d<=6, its attainable a colors before the P-edge are
  [1,d-1] union [8,d+12].
This follows by intersecting the intervals
[max(-6,L-13),min(6,L-7)] for the two neighbor residues L after
translating a to zero and requiring the selected b,c colors to differ
by at least seven. For d>=2 the complement has no component of seven
consecutive colors; every A(P) meets the set. For d=1 it is [8,13],
which A(P) avoids when P is adjacent to D. These are the precise parts
of M02 used here; no stronger universal boundary lifting is assumed.

Normalize r=0,s=h. If h=0, adjacent e,f would both lie in A(0), so
extension is impossible. Otherwise E ranges from 7 to min(13,h+6).
After translating E to zero, the D-list is empty at t=E, is a prefix
of length j for t-E=j in 1..6, a suffix of length j for t-E=-j, and
is all [7,13] at larger circular distance. The F-list is a nonempty
prefix or suffix of [7,13]. A D-list of length at least three permits
a distance-at-least-two pair: the sole possible common radius-one
point at length three is an interior point, which cannot be the
singleton F-list. The short-list failures are exactly
  t-E in {1,2}, s-E in {-6,-5},
or t-E in {-2,-1}, s-E in {5,6}.
The latter is impossible in 7<=E<=13, h<=10. Thus a fixed E forbids
{E}, enlarged to {E,E+1,E+2} only when E=h+5 or h+6.
Intersect over E: h=1 gives {7,8,9}; h=2 gives {8,9}; h=3 gives
disjoint sets at E=7,8; for h>=4 E=7,8 force distinct singleton t.
This is exactly B and audits the local P3 statement in both directions.

P4 additionally uses the MINIMUM-COUNTEREXAMPLE structural lemmas:
M01's exclusions of a degree-two vertex on a four-cycle and a vertex
with three degree-two neighbors, and M05 C2's faciality of all-cubic
four-/five-cycles. Those remain upstream candidates; a local color
enumeration cannot verify these all-size graph assertions.
Given them, Q=R or R=S makes a triangle. Q=S would give d-e-f-Q-d;
Q of degree two violates M01, and otherwise M05 makes this square
facial. It and the facial carrier would use the SAME corner ed,ef
at the cubic vertex e, impossible for two different faces. This is a
rotation-system corner assertion, not a drawing intuition. Alpha=R
is eliminated by the J table, since p=r lies in no additional row.
For alpha=Q, the shared vertex P has degree three by M01. Its third
neighbor cannot be inside: the other vertices are saturated, Pe makes
a triangle, and Pf gives the already excluded Q=S. L1-L2 and the
nine-vertex P3 relation exclude it. Reflecting the graph handles
alpha=S. Thus P4's conclusion follows from its explicit dependencies.
It excludes equal VERTICES, not equal COLORS.

## 5. A new exact pressure test: absorption reaches a fixed relation

Let F(B) denote the abstract bad-boundary transfer under one absorption:
F(B)(t,r,s) holds iff EVERY pair x adjacent to r, y adjacent to s,
with xy legal, satisfies B(y,x,t). Section 2 gives F(B)=B' for the
exact B input. The finite checker confirms this independently from
full graph counts.

Candidate lemma L3: F(B')=B'. In particular, further applications of
this SAME abstract table do not eliminate its d=1 or d=2 rows.

Since B' is contained in B, monotonicity gives F(B') subset F(B)=B'.
For the reverse inclusion, d=0 has no legal x,y pair. At d=1 the sole
pair is x=7,y=14: t=7 gives equal old r,s, and t=8 gives the old
normalized triple (7,0,1), in B'. At d=2,t=8 the only legal pairs
(x,y) are (7,14),(7,15),(8,15). The first two give normalized old
triples (7,0,1),(8,0,1); the third has equal old r,s. All are in B'.
These are every entry of B', proving equality without extrapolation.

This disproves the proposed STRONGER subroute that repeated abstract
absorption must strictly shrink the bad relation until only r=s remains.
It does not contradict M07's maximal-region proof: that proof derives a
larger induced region when TR blocks the smaller replacement, rather
than claiming that its table strictly improves on every iteration.
No withdrawal of an M07 claim is made.

## 6. New conditional reducibility, and explicit limit of that progress

Candidate lemma L4. In the M06 disk configuration with distinct outside
vertices, suppose BOTH alpha-Q and alpha-S are actual outside edges.
Then G is (20,7)-colorable iff its smaller five-cycle replacement J is.
This is a nonempty special reducible configuration, not an elimination
of any unconditional residual color class.

Any J coloring satisfies its basic constraints. The two outside edges
also require Delta(p,q)>=7 and Delta(p,s)>=7. In I,II,IV every bad p
has Delta(p,q)<=6. In III every bad p has Delta(p,s)<=6. Hence no
additional row is possible, and the M06 extension reconstructs G while
preserving the outside coloring. Conversely a G coloring has D!=F;
a three-edge path from D to F can replace the ear, supplying J.
The size decrease is three. No new edge is added to the outside during
this reduction; the two stated edges are hypotheses about G.
With only alpha-Q, I,II,IV are excluded but III with p=7 survives.
Those conditional exclusions MUST NOT be reported as unconditional
closure of three classes.

The special graph with the four pendants and the two extra edges has
rotation system and a complete coloring in tables.json. Its five face
walks have lengths 5,5,6,6,8 (the last includes the r-leaf twice),
V-E+F=12-15+5=2, no triangle and maximum degree three. This checks
nonemptiness and the repeated-face-boundary edge case explicitly.

## 7. Executed finite audit and bounded failed replacement search

The C++ program consumes only an explicit graph, fixed vertices and
colors. It chooses a remaining vertex, tries EVERY permitted integer
color and propagates only actual edge constraints. A branch is dropped
only when an unassigned neighbor has no legal value. Induction on the
number of unassigned vertices proves the recursion counts every full
coloring exactly once. The color domain strictly decreases in recursion
depth; full-count runs never stop after their first witness. Bounds
n<=16 and at most twelve free vertices prevent uint64 overflow because
20^12<2^64; addition overflow is separately checked. No M06 or M07
interval table enters this generator.

Actual outputs: all 4400 normalized original and J boundaries were
counted. They have respectively 912 and 880 zero rows, leaving exactly
32 additional rows, eight in each class. The full counts sum to
13,594,364 and 938,700 internal assignments across those inputs.
Nine-vertex checks cover 220 normalized triples and give exactly 25
zero rows. A separate Python search directly checks every one of the
32 residuals without interval-table pruning. All positive witnesses are
edge-checked and 139,520 global translate/reflect transformations pass.
Twelve injected errors have actual rejection witnesses in mutations.json.

The augmented replacement J+alpha-U is also exhaustively counted. Its
remaining bad states are exactly:
  I: p=1,14; II: p=6,19; III: p=7; IV: p=1.
Each has a unique internal coloring with alpha and V equal in color.
Thus all FOUR classes still have surviving representatives. The two
separately colorable alpha-U and alpha-V replacements may not have the
same outside coloring; their constraints are not conjoined here.

A bounded probe checks 272 explicitly generated cofacial replacements
with fewer than eight internal vertices: cycles of length four through
seven, a square/pentagon sharing an edge, and theta(2,3,3), theta(1,3,3),
and theta(2,2,4). It does not
claim to enumerate all small planar gadgets. Every probe either admits
a basic bad state, or leaves a representative of each of I-IV. The
compact witness dictionary in gadget-search.json permits direct edge
reconstruction for every rejection; the source and input/output digest
chains permit replay. This excludes exactly the tested replacement
subroute, not an all-size reducibility theorem. Some theta(2,2,4) portings block
all of III or IV but admit 501 basic bad boundaries, which makes them
invalid as a direct lifting reduction. These failures are retained.

Runtime: CPython 3.13.5 and g++ 14.2.0; exact standard-library integers.
run.py records actual compiler/runtime/binary hashes, input and output
hashes, observed exits and resource limits. Each engine invocation has
an eight-second wall limit; the entire audit child has wall 40 seconds,
CPU 30 seconds and 256 MiB address space. Compilation is separately
bounded by wall 15 seconds, CPU 12 seconds and 512 MiB. Output and file
caps are explicit. No GPU, CAS, SAT, Lean or registered verifier ran.
The GitHub transport lane is distinct from these foreground executions.
No trusted verification or mathematical admission is inferred from them.

## 8. Dependencies, readiness and next exact obligation

Fresh inputs at the read revision: M06 single-ear-boundary, M07
three-port-propagation, V01 local-audit, V02 m09-r1-audit, M09 R1,
M05 pentagon-clusters, the active Attempt/ObligationGraph and the empty
failed-route ledger. M09/V02 are not premises of L1-L4; no later M09
six-terminal claim is promoted here. Source bodies are unchanged.

The total graph-class theorem, P4's upstream critical-structure results,
and V01's trusted kernel/axiom/statement-faithfulness gates remain open.
The accompanying V01 statement comparison and admission_request are
candidate intake material. The only current workflow is the read-only
candidate transport gate; registered Lean policies are fixture policies,
not a discovered callable verification service for this graph theorem.

best_verified_candidate: none. best_verified_result: none.
Unconditional residual classes closed: []. Classes still open: I,II,III,IV.
First explicit surviving augmented state: (p,q,r,s)=(1,0,2,0), with
(D,U,V,F,E)=(7,14,1,8,15) and alpha=V in color.
Next exact obligation: for the colorable, class-preserving J+alpha-U
built from a minimum obstruction, produce a legal outside recoloring
that leaves the above residual family, or a different replacement whose
full boundary relation excludes one whole class without reintroducing
basic failures. Equality of the distinct outside vertices' colors must
not be replaced by vertex identification. The invariant fixed point in
Section 5 rules out simply repeating abstract absorption as that step.

Both admitted obligations remain open. This checkpoint is not task
completion and is not RESULT_CANDIDATE_READY under this launch's stricter
requirement of a whole residual class or a counterexample to M07 itself.
