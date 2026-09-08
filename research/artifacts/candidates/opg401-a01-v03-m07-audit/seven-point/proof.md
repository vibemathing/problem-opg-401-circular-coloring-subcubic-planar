# V03: sharp eight-vertex boundary-model barrier and full-coloring reconfiguration controls

Status: NONTERMINAL_CHECKPOINT. Verdict: candidate_only.
Candidate: candidate:opg401-a01-v03-seven-point-barrier.
Owner: math-proof. Repository: vibemathing/problem-opg-401-circular-coloring-subcubic-planar.
Attempt: attempt:web-20260906-opg401-a01. Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1. Target: obligation:opg401-root.
Read main: 7928d42a5c57e0c94bbc694b1ee2efc63836ee39.
Reused V03 input head: 33ddea0b0c56b186b65598aff4351ccd967ce65a.
Both admitted obligations and all four m06 residual classes remain open.

## 1. Frozen boundary model and the precise quantifiers

All colors are in Z20 with representatives 0..19. An edge xy is legal iff
7 <= [color(y)-color(x)]20 <= 13. The shortest UNDIRECTED circular distance
is delta(x,y)=min([y-x]20,[x-y]20); edge legality is delta>=7.

The original region O has ordered vertices (a,u,b,c,v,d,e,f), edges
au,ub,bc,cv,va,cd,de,ef,fb and four boundary incidences aP,dQ,eR,fS.
P,Q,R,S are distinct outside vertices with colors (p,q,r,s). Equal colors
are permitted. The outside is not presumed freely recolorable.
J is D-U-V-F-E-D with QD,RE,SF; JU additionally has PU.

A stationary port replacement K is an arbitrary simple triangle-free
internal graph, possibly disconnected or empty, with at most one incidence
from each of P,Q,R,S to an internal vertex. Incidences may be omitted and
several different ports may meet the same internal vertex, subject to degree
at most three after attaching them. Internal isolated vertices are allowed.
There are NO new outside-outside edges, NO outside identifications, and NO
absorption or changing of existing outside edges in this particular model.
A planar disk-compatible replacement is a subset of this model.

Write Ext(K) for the set of all four-color tuples extendible over K while
fixing those four colors. Uniform fixed-boundary lifting means
  for EVERY b in Z20^4, b in Ext(K) implies b in Ext(O).
It is stronger than the existence of a convenient coloring of one exterior.

Claim S7: every stationary port replacement K with at most seven internal
vertices has Ext(K) not contained in Ext(O). This includes replacements
changing J's edges, ports, topology, component count or omitting a port.
The finite certificate covers a superset including nonplanar internal graphs;
no planarity inference is made from their occurrence in that superset.
The order bound is sharp in this stationary model: O itself has eight
vertices and identical boundary relation. This is a barrier to shrinking
this patch by a uniform stationary substitution, NOT a root counterexample.

## 2. Complete generation and finite positive certificates for S7

There are 129 internal graph isomorphism representatives of orders 0..7 in
this exact class. Their counts by order are 1,1,2,3,7,13,32,70. The generator
starts with the empty graph and adds a vertex with zero to three neighbors.
Its neighbors must have free degree and be pairwise nonadjacent. Every graph
in the class is covered by induction on its number of vertices: deleting
any vertex preserves simplicity, triangle-freeness and maximum degree three,
and reversing that deletion is one of the generated operations. No connectedness
assumption is used. This is a proof of coverage, not induction from a table.

The checker uses a different construction: for each fixed vertex order it
starts with no edges and repeatedly adds an edge whose endpoints have spare
degree, are nonadjacent and have no common neighbor. Deleting an edge proves
coverage by induction on edge count. The two exact canonical graph sets agree.
Canonicalization takes the minimum edge list over all permutations within
degree classes, with classes in degree order. Every isomorphism preserves
degree, so restricting to these permutations loses no graph. Automorphisms
are similarly checked by exact preservation of every edge, not by a graph hash.

For each internal graph, enumerate four port positions in {-1,0,...,n-1}^4,
where -1 means no incidence. Reject precisely degree overflow. Quotient only
by actual internal graph automorphisms; the labels P,Q,R,S are NEVER permuted.
This covers 44669 port-isomorphism representatives. In particular outside
color equality is not used as a vertex identification.

The 16 connected full-port cases retaining J's five edges and QD,RE,SF were
SKIPPED before color search, in accordance with the already proved no-go
family. Their hand argument is recalled in section 3; this continuation did
not run another color enumeration of them. The other 44653 representatives
are each covered by at least one of the 2445 positive witnesses in cover.json.
A witness consists of a bad-boundary index and all internal vertex colors.
The checker checks every internal edge and every attached boundary incidence.
It regenerates EVERY representative and verifies that at least one witness
covers it. Thus the file is not just a count or a solver's negative verdict.

The encoding is explicit: each row is [n,edge_mask,witnesses]. Edge bit i
refers to the i-th pair in combinations(range(n),2). The text "i:colors"
uses index i in bad_boundaries and the base-20 alphabet 0123456789abcdefghij,
in vertex order 0..n-1. These are compact exact integers, not opaque binary.
Every positive witness and coverage test is reproducible without SAT/SMT.

The twelve bad boundaries used, in order, are
 (0,0,0,0), (0,0,0,1), (0,0,0,2), (0,0,1,1),
 (0,0,2,1), (0,0,19,1), (1,0,2,0), (1,0,2,1),
 (7,0,19,1), (8,0,0,1), (14,0,2,0), (14,0,2,1).
The search imports no earlier boundary table. A separate literal-edge DFS
checks nonextension on O. Here is also a short hand proof for all twelve.
If q=r or r=s, adjacent d,e or e,f lie in the same span-six allowed interval,
so cannot form an edge. This handles the five basic cases.
For q=s=0,r=2, legality gives e=14 with d=f=7 (impossible since b,c then
lie in the same allowed interval), or e=15 with {d,f}={7,8}. Equal d=f is
always impossible. The remaining edges force {b,c}={1,14}; hence a lies in
B6(1) intersect B6(14)={15,16,17,18,19,0}. This is disjoint from A(1) and
A(14), proving both C1 cases. For q=0,s=1,r=2 the same argument forces
e=15,d=7,f=8,b=1,c=14, and that set for a also avoids A(0). This handles
the three C4 cases. Finally q=0,s=1,r=19 forces e=6,d=13,f=14,b=7,c=0.
Now a must lie in {1,...,6}, disjoint from A(0) and A(7), handling C3.
Two-edge-path conditions here follow directly by intersecting translates of
{7,...,13}; they are not inferred from a previous execution record.

Consequently every covered replacement has a concrete counterexample to its
own uniform implication. The original O with four pendant outside vertices
is itself planar triangle-free subcubic and is colorable with changed boundary:
inner colors (0,11,4,16,7,3,10,17), boundary (10,13,0,7). No full-graph
noncolorability is inferred from any prescribed-boundary obstruction.

## 3. The skipped family, and what cannot be inferred from C1/C2 masks

D,E,F in J are saturated by their existing ports and two internal edges.
Only U,V each have one free incidence. With at most two added internal vertices,
connectedness permits small trees singly attached at U or V, or an added
path U-L-M-V; one new vertex touching both would make a triangle.
For p in {1,14}, write o for the other color. J can be colored with E=15 and
(D,U,V,F)=(7,14,1,8) or (8,1,14,7), so U,V can be p,o in either order.
A direct P-to-root edge uses root=o. A two-edge P-to-root path uses root=p
and midpoint p+10. A three-edge path uses unequal endpoint colors p,o;
three increments in [7,13] cover every nonzero residue modulo20. Fill other
tree leaves ten away from their parent. For PL on U-L-M-V, use
U=p,V=o,L=o,M=o+10; all four added/port edges have distances 7,10,10,7.
For PM exchange the two sides. Both C1 values therefore extend in every
skipped case. This is the existing structural proof, not a repeated search.

As a finite diagnostic, among the 44653 new cases the masks for feasibility
of C1 p1,p14 and C2 p6,p19 are 0:4621, 6:1296, 9:3159, 15:35577.
Mask zero is NOT success: each such graph still leaks a different bad boundary.
Reflection of all colors takes C1 p1 to C2 p19 and C1 p14 to C2 p6. C2 is
therefore processed by the same exact isometry, not a separate conjectural
argument. No row is declared closed by replacing it with another bad row.

## 4. Full-coloring states, sound composition and an honest termination gate

For a finite retained exterior H and a permanently fixed separator coloring
sigma, let F_sigma be ALL actual valid colorings of H extending sigma. A state
is an entire f in F_sigma, or an encoding retaining all values needed to
reconstruct that f. A transition must give a legal next g in the SAME state
space, satisfying every retained edge and every fixed separator value.

Let T be the states whose actual port tuple extends to O. Define W0=T and
W_(k+1)=W_k union {f: there exists a permitted transition f->g with g in W_k}.
This stabilizes after at most |F_sigma| strict additions. For f in W let
rank(f) be the least k with f in W_k. If rank(f)>0, its defining witness is
one actual g with smaller rank. Repeating these chosen witnesses terminates
in T and then supplies a genuine extension. The original f, then its actual g,
then the actual next state are used; two transitions from incompatible hidden
colorings are never composed. If a projected boundary fiber B is to be
uniformly repairable, the additional obligation is EVERY f in B belongs to W.
A single existential representative in each projected boundary does not suffice.

This proves composition and strict-rank termination WHEN the coverage condition
is supplied. It does not assert W=F_sigma. A negative certificate is a nonempty
set of states closed under all permitted transitions and disjoint from T.
Sections 5-6 give exactly such certificates for a natural, fairly large move
library. Thus merely specifying full states and a rank definition cannot close C1.

## 5. Minimal cyclic frozen exteriors, including both C1 values

Take H=C40 with vertices 0..39, edges i--(i+1 mod40), and colors f(i)=7i mod20.
For p=1 put P=3; for p=14 put P=2. In both cases Q=0,R=26,S=20. The four
vertices are distinct and have boundary (p,0,2,0). Around H the port order
is P,S,R,Q, so O can be attached inside H in its required disk order.
The resulting G has 48 vertices,53 edges,7 faces, with all degrees at most3.
recolor-certificate.json contains its COMPLETE edges, rotations, face walks,
fixed outside colors and a full coloring with a changed exterior for each case.
The certificate uses O vertices 40..47 in order a,u,b,c,v,d,e,f.

At each exterior vertex colored c the two exterior neighbors have colors
c-7,c+7. Their common allowed set is the singleton {c}; a direct interval
intersection proves this. Therefore no nontrivial single-vertex recoloring
of H is possible, even allowing an arbitrary new color rather than +/-1.

Consider the larger move library consisting of such recolorings, a uniform
+1 or -1 shift of an arbitrary vertex subset, and a global reflection.
Orient a tight edge x->y when f(y)-f(x)=7 modulo20. A +1 shift of a subset
preserves every edge iff it has no outgoing tight edge: an outgoing tight
edge would change difference7 to6; all other crossing differences remain
in [7,13]. Dually -1 requires no incoming tight edge. The tight H is a
strongly connected directed cycle, so only the empty/full subsets qualify.
Every nontrivial permitted subset shift is thus a global translation.
Reflection reverses the directed cycle and preserves the same conclusion.

For each fixture the 40 states
  f_(epsilon,t)(i)=epsilon*7i+t mod20, epsilon in {1,-1}, t in Z20
form a nonempty closed orbit under the entire move library. All port tuples
are common translations/reflections of its C1 obstruction, so none extends
to O. Full state information does not help escape this orbit. The executable
control checks 80 complete orbit states and 64000 possible single-vertex
color trials across the two fixtures. The arbitrary-subset part is proved
by tight-edge closure, not by falsely claiming an enumeration of 2^40 subsets.

These exteriors are smallest in the explicit SIMPLE-CYCLE frozen family:
a frozen degree-two vertex must have neighbors c-7,c+7, because only an
intersection of size one can fix its color. Thus the entire cycle is directed
tight and has length divisible by20. Distinct equally colored Q,S require
at least40 vertices. This is not a claim of minimum order among all planar
exteriors or all patches. The 48-vertex examples are NOT minimum root
obstructions: they contain long degree-two threads and have the supplied
full colorings. No M07 hypothesis or conclusion is contradicted.

The precise failed lemma is: every valid exterior with a C1 port tuple can
be brought to an extendible tuple by the above move library while preserving
all outside edges. It fails for BOTH p=1,14. Applying reflection also supplies
C2 controls with p=19,6 and r=18. C2 is not marked solved by that failure.

## 6. Remaining research and verification scope

The stationary <=7 replacement search is exhausted in its stated scope; it
must not be relaunched as another random gadget screen. The recoloring move
library above is also insufficient for arbitrary exteriors. Valid next options
are absorption of actual exterior vertices with a strict total-order decrease,
changing exterior incidence structure with a class-preservation proof, or
nonuniform simultaneous recoloring using the stronger structural restrictions
of a hypothetical minimum obstruction. An eight-or-more internal gadget alone
is not a smaller replacement for O. The first open state remains
C1 (1,0,2,0), and its p14 partner must be handled by the same valid argument.

The full-coloring reachability closure must be proved for the relevant
minimum-obstruction exteriors; the cyclic frozen controls are not in that
restricted subclass. No dependency on V02/M09 R1 is smuggled into this outer-
eight-cycle, two-pentagon patch. M07's three-port maximal-region lemma is not
withdrawn. Existing extra-port degree/adjacency candidates remain inputs.

Actual scripts, compact positive cover and orbit certificates accompany this
proof. A different graph generator and a different literal-edge check are
algorithmic cross-checks inside ONE candidate-generator trust domain, not
trusted verification. The admitted requirements kernel_check, axiom_escape_audit,
and statement_faithfulness remain pending. The existing V01 request is not a
Lean proof or a verifier receipt. No truth ledger, registry or Result is changed.

closed_residual_classes: []. open_residual_classes: C1,C2,C3,C4.
best_verified_candidate: none. best_verified_result: none.
Open admitted obligations: obligation:opg401-root; obligation:opg401-z20-extension.
