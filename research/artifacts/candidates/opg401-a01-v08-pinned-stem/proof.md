# V08: exact pinned-stem response and unbounded minimum two-port support

Status: NONTERMINAL_CHECKPOINT. Verdict: candidate_only.
Candidate: candidate:opg401-a01-v08-pinned-stem.
Owner: math-proof. Repository: vibemathing/problem-opg-401-circular-coloring-subcubic-planar.
Attempt: attempt:web-20260906-opg401-a01. Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1. Target: obligation:opg401-root.
Read main: 1044c32fc3622e5809dcb65a97db657d1dab8985 (V07/PR31 merged).
All C1-C4 classes and both admitted obligations remain open. No C2 work is done.

## 1. Scope and complete incidence freeze

EdgeOK(a,b) means 7 <= [b-a]20 <= 13. Colors are in Z20 with representatives
0..19. The undirected distance is min([b-a]20,[a-b]20), not a directed difference.
O has vertices (a,u,b,c,v,d,e,f), edges au,ub,bc,cv,va,cd,de,ef,fb and
incidences aP,dQ,eR,fS. P,Q,R,S are distinct, with actual colors (p,0,2,0),
p in {1,14}. A(c)=c+{7,...,13}. V03-V07 are candidate inputs, not Evidence.

This note replaces one fixed-size fork by an ALL-LENGTH response calculation.
It does not assert that its colored stem must occur in every minimum obstruction.
It does not turn the finite examples into minimum root counterexamples.
No exhausted replacement, C40, same-axis or selective-F search is repeated.

Let m>=0 and s in {0,...,6}. In the actual exterior H choose distinct vertices
 U={Q,R,y,w_0,...,w_m}
inducing precisely Qy,Ry,yw_0 and w_i w_(i+1) (0<=i<m).
Q and R each have one other exterior neighbor, both colored13. They may be
ONE shared physical vertex when the ambient simple subcubic graph permits it.
y has no other neighbor. For i<m, w_i has exactly one other neighbor a_i;
w_m has exactly two other neighbors a_m,b. Put c_i=[16-7i]20. The ACTUAL colors are
 f(Q)=0, f(R)=2, f(y)=9, f(w_i)=c_i,
 f(a_i)=[c_i+7]20, f(b)=[c_m+7+s]20.
These lists include EVERY edge leaving U. Other incidences or chords must be
reported, not ignored. Cut vertices of equal color may coincide only if every
incidence and the single actual color of that vertex remain consistent.
All of H-U, including P,S and all a_i,b, is fixed. An additional fixed set
must be outside the changed support (or have unchanged actual values).
The assumption is on one actual f; there is no replacement of f by a boundary
projection representative. The formulas apply for both original values of p.

## 2. R1: an exact all-length root response, not a heuristic propagation

Write a new color at w_i uniquely as c_i+x_i mod20, x_i in [-6,0]. The unique
lift is justified by its a_i incidence: A(c_i+7)=c_i+[-6,0]. The last b
incidence additionally requires x_m>=s-6. For the edge w_i w_(i+1), its directed
new difference from child to parent has the integer lift 7+x_i-x_(i+1), in
[1,13]. Consequently that edge is legal EXACTLY when x_i>=x_(i+1).
Thus the complete tail state space is
             0 >= x_0 >= x_1 >= ... >= x_m >= s-6.          (2.1)
No chosen integer lift outside these ranges is used in a distance test.
Necessity follows from each listed edge and pin. Conversely every vector in
(2.1) satisfies every tail edge and pin. This is a full two-way characterization.
The root response before its edge to y is therefore
             M_(m,s)={10+s,11+s,...,16}.                   (2.2)
Every value is attained by a constant x-vector. In particular it is independent
of length, whereas the least NUMBER of changed vertices need not be bounded.

For an independent counting control, set d=6-s. For a fixed x_0=a in[-d,0],
the number of completions is binomial(m+a+d,m): the remaining m entries form
a weakly decreasing multiset from a+d+1 values. This follows by recording the
multiplicity of each value, summing to m; separators among m identical positions
give the stated binomial coefficient. This counting identity is not the proof
of existence or optimality; (2.1) provides the actual vectors.

## 3. R2: exact repair threshold, both C1 values, and minimal support

The pinned Q/R incidences require q,r in0..6. If W=f_new(w_0)>=11, the only
possible y-colors are 7,8,9,18,19, with the complete table
 Y7: q=r=0, W14..16;
 Y8: q,r in0..1, W15..16;
 Y9: q,r in0..2, W16;
 Y18: q,r in5..6, W11;
 Y19: q=r=6, W11..12.
This follows directly by intersecting A(Y) with [0,6] and [11,16].

Among these states O fills for EITHER p exactly at (q,r,Y,W)=(5,6,18,11).
Here is the negative argument, restated rather than trusting V07. If r<=q,
the e-f edge, with e in[r+7,r+13] and f in[7,13], forces e>=f+7. The e-d
edge then gives d<=e-7<=r+6<q+7, impossible. In the low rows the remaining
q<r pairs are(0,1),(0,2),(1,2). For(0,1) only equal d=f=7 is possible,
preventing bc. For(0,2) or(1,2), unequal d,f force {d,f}={7,8}, e=15 and
{b,c}={1,14}. The two length-two branches then require a in
{15,16,17,18,19,0}, disjoint from A(1) and A(14). In the high rows r>q only
occurs at(5,6). The positive O fills, in order(a,u,b,c,v,d,e,f), are
 p1:  (8,1,14,2,15,12,19,7),
 p14: (1,8,15,2,9,12,19,7).
Checking all nine inner and four port edges proves their legitimacy.

For s=1, (2.2) is[11,16]. Hence the UNIQUE filling state on U is
 q=5,r=6,Y=18, and x_0=...=x_m=-5. All m+4 support vertices change.
For s>=2, M is contained in[12,16], so there is NO fixed-complement O fill,
even allowing every vertex of U to change arbitrarily and simultaneously.
This is an impossibility certificate for this exact pinned region, not merely
failure of one reflection/axis algorithm.

For completeness s=0 adds W=10. Additional possible filling states have
Y=17 and(q,r)=(4,5),(4,6),(5,6), or Y=18 and(q,r)=(5,6); their remaining
case W=11,Y=18,q=5,r=6 also works. For q=4 and r=5 or6, explicit O witnesses are
(8,1,14,2,15,11,18,7) for p1 and(1,8,15,2,9,11,18,7) for p14. The earlier
q5,r6 witnesses handle the other cases. These literal edge checks prove sufficiency. Necessity follows from r>q
as above and q,r in A(Y) intersect[0,6]. All filling states still change Q,R,y
and have x_0<=-5, which by(2.1) forces every tail vertex to change.

Consequently the exact result for every m is
 s=0 or1: fixed-complement repair exists; minimum total changed support=m+4;
 s=2,...,6: no repair with this complement fixed.
For s=0 there are m+5 filling U states; for s=1 there is one. The former count
has four W10 completions (all x=-6) and m+1 W11 completions, whose weakly
decreasing tail entries are -5 or-6. These counts apply identically to both p.

The same-f construction for EVERY positive instance is
 g(Q)=5,g(R)=6,g(y)=18,g(w_i)=[c_i-5]20; g=f on H-U.
The fork edge differences are13,12,7; every tail edge keeps difference7;
the a_i edges have difference12; the final b edge has difference12+s, legal
precisely for s=0,1 in this chosen construction. Adjoin the corresponding O
fill above. Only TWO ports change. Every other exterior edge keeps both colors.
A repeated physical cut vertex is still fixed once, not assigned different
colors by different local constraints. Simplicity, triangle-freeness, degrees
and the entire rotation system are unchanged.

For m>=1 there is no repair of total support at most four inside U. Therefore
none of the known three-point or V07 four-point colored repairs can succeed
there while respecting this complement. This does NOT claim their absence
elsewhere in H if additional outside vertices are allowed to change.
There is no universal constant bound on minimum TOTAL support even in this
pinned simple plane subcubic family. Per-step atomic size is a different matter.

## 4. R3: actual-state composition, a preparation algorithm and termination

For s<=1, process w_m,w_(m-1),...,w_1, changing w_i to c_i-5. At its step the
parent still has old color and the child (if present) already has new color.
The parent edge has difference12, child edge difference7, pin difference12,
and the last pin difference12+s. Thus every intermediate state is legal.
After these m preparations, simultaneously change Q,R,y,w_0 to(5,6,18,11).
Its fourth neighbor w_1 now has color4, while a_0 has color3, so the exact
V07 terminal fork is now AVAILABLE although it was absent as a repair at the
initial state. For m=0 the fixed terminal pin directly has color3 or4.
Finally adjoin O. The rank is (remaining unprepared tail vertices, remaining
terminal phases), with the terminal phases entered only when the first count
is zero. Equivalently count m+2 pending operations. It decreases at every
operation and ends with a real full coloring. All stages retain the same
actual complement and act on the preceding output; no fiber substitution.
The minimum total support m+4 is not a claim that m+4 vertices must all change
in one indivisible atomic step. The final four-point step is synchronous;
the earlier preparations have explicit individually legal intermediate states.

A general lossless response on an induced rooted TREE K with actual cut colors
can be carried as twenty counts and twenty minimum costs at each vertex:
 D_v=intersection of A(f(b)) over ALL fixed neighbors b of v;
 C_v(x)=1[x!=f(v)]+sum_child min_(z in A(x)) C_child(z), for x in D_v.
Impossible entries are infinity; store an argmin for each finite summand.
Counts use the same recurrence with sums/products instead of min/add costs.
Induction on subtree size proves both necessity and constructive sufficiency:
child interiors are disjoint, and shared external vertices retain the SAME
fixed f-value throughout. The parent color and all fixed values are carried,
not just existential terminal reachability. There are at most400 checks per
tree edge. Reconstruction visits each node once and produces the actual g.
An induced chord between subtrees INVALIDATES that recurrence unless explicitly
conditioned on its endpoints. A Steiner drawing alone does not remove chords.
This response calculation is exact but it does not prove a favorable response
exists in the unknown minimum-obstruction region.

## 5. R4: boundary accounting and the sharply delimited failed deletion

For any connected induced exterior set W of n vertices containing k of the
four O ports, let c=|E(H[W])|-(n-1), d=sum_W(3-deg_G(v)). Direct degree counting
gives for Z=O union W
                       b=n+6-2k-2c-d.                    (5.1)
Its internal edges number9+k+(n-1)+c=n+8+k+c; its degree sum is22+3n-d.
Formula(5.1) specializes to V04's n-2-2c-d ONLY WHEN k=4.
For this U: n=m+4,k=2,c=d=0, hence b=m+6. The cut comprises P,S, the Q/R
pinned incidences, all a_i incidences and b. Coincident outside endpoints
reduce the number of variables, never the number of these edge incidences.

For s>=2 the actual coloring of G-Z is a concrete failed lift for deletion
of exactly Z, since section3 rules out every filling of Z with that complement.
This rejects ONLY the assertion that this exact region can always be deleted
and lifted without any boundary condition or added replacement constraint.
It does not reject all smaller gadgets, expanding Z, changing cut colors,
or minimal-counterexample-specific absorption. No universal 'all absorptions
fail' certificate is asserted. In fact changing the one terminal pin b to
c_m+8 (outside U), then using the positive construction, gives a full coloring
of the finite controls. The negative controls are NOT root counterexamples.

## 6. Full plane controls, minimality scope and exact remaining gap

The certificate gives full outside and complete G rotations/colors for m=1,
s=1,2 and both p, not merely a disconnected palette instance. A shared fixed
outside core has edges AQ-z-AR, AQ-Q, AR-R, AR-S, with colors13,0,13,0,2,0.
For p1 add P-AQ; for p14 add P-p_mid-AQ with colors14,1,13. Add the induced
fork and tail and all stated pins. Complete the graph with O. The fixed core
contains the six-cycle Q-y-R-AR-z-AQ-Q, with P and S attached in the required
face order. The explicit base rotation has sphere characteristic2. Extending
a tail subdivides a pendant edge and attaches one pendant pin, preserving
planarity for EVERY m. The checker verifies every dart in the finite fixtures.
All four ports are primary-conflict connected (L8/L16); the certificate lists
the actual conflict edges. The controls have leaves/low-degree fixed vertices
and deliberately prescribed pins. They are NOT claimed to satisfy every prior
un-pinned all-axis obstruction or every genuine minimum-counterexample axiom.
Minimality is the PROVED support size m+4; m=1 is the first member beyond V07.
No global minimum exterior order is claimed.

All hand results are separate from finite checks. The modular message engine
is compared with a literal-distance tail DFS at m<=3, and every O decision
uses a literal-edge DFS importing no old table. Longer controls compare exact
integer formulas and explicit witnesses, not an extrapolated root claim.
The run checks m=0,1,2,3,4,8,16,64,128, all seven s and both p; bounds and
actual interpreter/source/input/output hashes are in execution.json.
Four full plane fixtures and fourteen mutations address endpoints, modular
wrap, tail direction, omitted cut edges, premature root updates, changing
fixed pins, splitting repeated outside vertices, and boundary-witness mixing.
No Lean/SMT, registered verifier, EvidenceLink or admission ran.

closed_residual_classes: []. open_residual_classes: [C1,C2,C3,C4].
best_verified_candidate: none. best_verified_result: none.
first_open_state: C1(1,0,2,0), with p14 still requiring the same general bridge.
The missing bridge is NOT the exact stem response: it is proving that the
actual minimum-obstruction path region admits enough boundary flexibility to
reach a favorable response, or that a blocked cut can be released/absorbed by
a strictly net-smaller class-preserving replacement. A pinned response of width
five or less may block every internal move. Neither the signed degree remainder
nor bounded-support enumeration has been shown to rule that out. Retain every
actual pin/path/chord when enlarging the region; do not just increase a fixed
support-search cap or claim every exterior contains this stem. C2 is untouched.
