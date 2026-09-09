# V10: a zero-slack boundary endpoint dichotomy and a joint C1 restart

Status: NONTERMINAL_CHECKPOINT. Verdict: candidate_only.
Candidate: candidate:opg401-a01-v10-zero-endpoint. Owner: math-proof.
Repository: vibemathing/problem-opg-401-circular-coloring-subcubic-planar.
Attempt: attempt:web-20260906-opg401-a01. Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1. Target: obligation:opg401-root.
Read main: 36318f5d88265148041a1407cadcb5e1665512a8 (V09/PR33 merged).
All whole classes and admitted obligations remain open; C2 is not advanced.
No minimum path-union region of a hypothetical unknown graph is fabricated;
the exact operations below use its whole actual exterior when applicable.

## 1. Exact input, provenance, and the first class actually treated

Colors are residues 0..19. E(a,b) means 7<=[b-a]20<=13; on these fixed
representatives it is equivalent to 7<=abs(a-b)<=13. The undirected distance
is min([b-a]20,[a-b]20). O has ordered vertices a,u,b,c,v,d,e,f and edges
au,ub,bc,cv,va,cd,de,ef,fb, with incidences aP,dQ,eR,fS. The four ports
are distinct physical vertices with actual colors (p,0,2,0), p=1 or14.

H=G-V(O) retains EVERY exterior edge, its actual valid f, and its rotation.
The selected local structural class has N_H(Q)={y,X}, N_H(R)={y,Y},
f(y)=9 and f(X)=f(Y)=13. X,Y may be the SAME physical vertex. This includes
the root fork of the V08 stem, but is not asserted to occur in every unknown
minimum-obstruction region. Its remote tail can be arbitrary. A permanent
fixed set B is respected; the sets we explicitly release must be eligible,
and Q,R must not belong to B for the paired move. P,S always stay fixed.

The current atomic class is a minimum-total-slack path of total ZERO reaching
the R-side boundary vertex Y, not all nonnegative path classes. For an actual
oriented edge put w(u,v)=13-[f(v)-f(u)]20. A zero arc has color difference13,
NOT7. The reflection conflict graphs L8/L16 are different graphs.

V03-V09 are candidate inputs. V09 already proves the general difference-bound
solver; c06 already treats tight cut shifts. We reuse that mathematics, not
claim a new shortest-path algorithm. The advance here is a DIFFERENT JOINT
interior target, a complete boundary-endpoint case split, and a sharp next
zero-return condition. No old single-port/axis or support-cap search is run.
The locally attached V09 archive and merged V09 have different hashes; the
source note preserves that distinction instead of overwriting PR33's packet.

## 2. Z1: a paired target changes which actual boundary bound is obstructing

Use the joint target Q=2,R=19, keep y=9, P=p,S=0. Neither Q=2 alone nor
R=19 alone belongs to the old single-port target set. Literal O witnesses are
 p1:  (14,7,0,8,1,15,6,13),
 p14: (1,8,0,7,14,14,6,13).
All nine O edges and four port incidences check directly. No two projected
exterior colorings are combined.

Let K=H-{Q,R}. Outside the two ports allow g(v)=f(v)-d(v) modulo20,
0<=d(v)<=6, with B,P,S fixed. Actual cut constraints are exactly:
 Y: d>=1 (and d<=6); X: d<=4; y: d=0; P,S,B: d=0.
All other K vertices have bounds0..6. If X=Y intersect the two bounds at
ONE vertex, obtaining1..4. No incidence or repeated identity is omitted.
Indeed E(19,13-d) requires1<=d<=6; E(2,13-d) requires0<=d<=4;
E(2,9-d) requires d=0. The second R-y constraint accepts that value.

Let C be the forward-reachable set from Y using ALL zero-weight arcs in K.
Then a completion in this bounded-drop family exists if and only if
                C does not meet {y,P,S} union B.                 (2.1)
When it exists the explicit least vector is d=1 on C,0 elsewhere.

Proof. Every zero arc u->v forces d(u)<=d(v). Since d(Y)>=1, every vertex
of C must be positive in any feasible vector, so a forbidden hit is impossible.
Conversely the indicator of C satisfies all edge inequalities: a selected to
unselected crossing has weight at least1; a selected-selected or unselected-
unselected edge has zero displacement difference. Reverse inequalities are
included. Every upper bound apart from the forbidden zeros is at least1.
The new integer edge difference r+d(u)-d(v) lies in[1,19], so there is no
hidden modular branch. The general bounds0..6 therefore have a solution
exactly when this binary vector works. This proves necessity for ALL bounded
vectors, not just selectors, and sufficiency on every actual graph edge.

Define the new full H coloring using this vector and the two port targets,
and append the displayed O witness. Its entire complement off C union{Q,R}
is unchanged. The graph, degree bounds, triangle-freeness and rotation are
unchanged. The least vector minimizes support within this specified family;
no claim of globally minimum arbitrary recoloring support is made.

This is a forall-f-exists-a-specific-g statement on (2.1). Later operations
use that actual g. A zero-reachability scan marks each vertex once; the pair
(unseen vertices,queue length) decreases lexicographically. Constructing a
new vector, adopting it, and appending O are finite descending phases. Failure
of (2.1) returns a path, not a fictitious terminal extension.

## 3. Z2: exhaust the first endpoint's local structure

The endpoint case split treats a NONEMPTY path. A coincident source/endpoint
with length zero still uses the exact cone test of section2, but does not
supply a color0 predecessor for this local split. Suppose a simple zero-slack
path in K reaches Y with last edge AY. Necessarily
f(A)=0, because f(Y)=13 and the forward difference is13.

Shared endpoint X=Y. Since Y already neighbors Q,R, maximum degree3 permits
no K neighbor other than A. Its reverse arc Y->A has weight6. Thus C={Y},
and (2.1) succeeds unless Y is permanently pinned by B. An even smaller map
changes only Y13->12 and Q0->19, keeping R=2. Its O fills are
 p1: (14,7,0,13,1,6,14,7),
 p14: (7,14,1,13,0,6,15,8).
The support edge has difference7; the fixed Q-y,Y-R,Y-A edges have differences
10,10,12. Its total support two is minimal when Y must be released: changing
only Y leaves the original bad port tuple. This observation also proves that
the shared-endpoint zero-hit class is inconsistent with the prior universal
single-preparation blocking hypothesis. It is a structural contradiction,
not a repeated enumeration of that template.

Distinct endpoint X!=Y. Besides R,A, Y has at most one further neighbor T.
If it exists, its old color t lies in0..6. For t<=5, or no T, set
                   Q=2,R=19,Y=12,
leaving EVERY other H vertex fixed. E(12,t) holds precisely for t<=5;
all other changed-edge differences are Q-X11,Q-y7,R-y10,R-Y7,Y-A12.
The same O witnesses in section2 cover BOTH p values. A T coinciding with
another fixed vertex still keeps that one actual value.

For the first genuinely joint case t=5 this is a minimum total support3
inside {Q,R,Y}. With y9,X13,A0,T5 fixed, Y is12 or13 and Q is0,1,2.
If Y=13 then R is0,1,2; none of these small (Q,R) pairs fills O. If Y=12,
R is19,0,1,2; R=19 is necessary. Keeping Q=0 still fails: for boundary
(p,0,19,0), e in6..12 and d,f in7..13 force e6,d=f13, preventing bc.
Hence Q,R,Y must ALL change. Q2,R19,Y12 works for both p. For p1 it is the
only local filling triple; p14 additionally allows Q1,R19,Y12.

Here is the small-pair nonextension used above. If 0<=r<=q<=2, e-f and
e-d force d<=e-7<=r+6<q+7, impossible. If q<r, possibilities are(0,1),
(0,2),(1,2). The first forces d=f7. The other two either force equality
or {d,f}={7,8}, e15, {b,c}={1,14}. The a-u-b and a-v-c constraints give
a in{15,16,17,18,19,0}, disjoint from A(1) and A(14). This completes the
negative proof without an enumeration premise.

If t=6, Y is rigid while A,T remain fixed: A(0) intersect A(6)={13}.
The same small-pair argument proves NO change confined to {Q,R,Y} fills O,
even arbitrary simultaneous colors. But Y->T is now a ZERO arc. Thus the
only unresolved endpoint color forces an actual continuation; it is not a
certificate against releasing T or other vertices. If T has no zero successor
leading to a protected vertex, section2 selects its whole zero cone and works.

In particular, in a genuine minimum obstruction admitting this local class,
a shared endpoint or a distinct endpoint with t<=5 is excluded by an explicit
coloring of the original G. This does NOT establish that every current region
has this class, or that the remaining t6 continuation always escapes.

## 4. Z3: the exact next zero-return condition, and its scope

Without extra permanent pins B, failure of section2 forces a zero path from
Y13 to y9, Pp or S0. A simple path of L edges has final color13+13L modulo20.
Since13*17=1 modulo20, the respective positive lengths satisfy
 L=12 mod20 (y), L=16 mod20 (P1), L=17 mod20 (P14), L=19 mod20 (S).
Thus the first possible shortest return has12 edges and ends at y. If its
internal vertices avoid Q,R, adjoining y-R-Y forms a14-cycle. Its twelve
path edges and y-R have directed difference13, while R-Y has difference11;
the total oriented slack is2. This is not the old C40 control.

A full concrete return uses path vertices v0..v12 with colors
(13,6,19,12,5,18,11,4,17,10,3,16,9), Y=v0,y=v12, plus R2 attached to both
ends. Q0 neighbors y and X13. A0 neighbors Y. S0 neighbors v6. For p1 use
P1-X13; for p14 use P14-M1-X13. There are no other H edges. H has19 or20
vertices. Input.json contains every edge and the full G rotation after O is
attached; certificate.json contains every face and actual old/new color.
These graphs have low-degree fixed vertices, are colorable, and are NOT
claimed to satisfy every earlier unpinned exclusion or to be minimum root
obstructions. The length12 and14-cycle minima are only for this zero-return
endpoint class, not minimum global exterior order.

On these graphs EVERY choice of bounded drops0..6 with the section2 port
targets fails: the12 zero inequalities force d(y)>=d(Y)>=1, whereas the
actual Q-y edge forces d(y)=0. Releasing further ordinary pins does not remove
that intrinsic inequality. This path certifies all choices in that family;
we do not claim to have enumerated7^|K| vectors or all possible absorptions.

There is nevertheless an explicit non-bounded-drop repair. Keep y=9 and all
vertices outside the path and Q,R fixed. Put v_i=12 at even i and2 at odd i
for0<=i<=11, and Q2,R19. Path differences are10 except its final edge to y,
which has difference7. R-Y has difference7; R-y10; Q-y7; Q-X11; Y-A12;
and the S-v6 edge8. Append section2's O fill. This proves these controls are
not root or all-release counterexamples. It is not a support-cap search.

The nonuniform repair must NOT be applied after forgetting a chord. For
example an extra edge v1-v5 is legal on the old colors6,18 but would have two
new colors2. Such a chord is a real new constraint; it and its external
incidences require a new response. No assertion that an arbitrary minimum
Steiner return is the bare cycle is made.

## 5. Complete boundary accounting and minimality distinctions

For any connected induced exterior W, let n=|W|, k=|W intersect {P,Q,R,S}|,
c=|E(H[W])|-n+1, and d=sum_W(3-deg_G(v)). The cut of O union W has
                         b=n+6-2k-2c-d.
This follows from degree sum22+3n-d and internal edge count n+8+k+c.
Absorbing a disjoint set C changes the cut by
 sum_C deg_G - 2|E(G[C])| - 2|E(C,Z)|.
Every old cut incidence, internal chord and physical outside endpoint matters.
Absorbing Y alone changes b by deg_G(Y)-2j, where j counts ALL its edges to Z.
For W={Q,R,y}, shared Y has j2 and usually changes5 to4; distinct Y has j1
and changes5 to6. This accounting is not a proof of a smaller replacement.

The eight fixtures retain this ledger before and after the actual zero cone
or return region, including repeated outside X. For the local t6 fixture,
Y alone cannot be released with T fixed; releasing Y and its leaf T6 together
lowers both by1 and does work. Consequently no all-absorption failure can be
claimed there. None of our recolorings changes graph order. A genuine
absorption still needs a net-smaller gadget and uniform lifting of EVERY
actual smaller-graph coloring; that missing assertion is not supplied.

## 6. Reproduction, trust, and the precise next obligation

Run python3 -I -S run.py in a fresh directory containing check.py,input.json,
run.py. It refuses to overwrite certificate.json or execution.json. The
bounded final run uses standard-library integers. A literal O DFS imports
no old target table; the local three-variable census has only792 legal
states across14 parameter rows. Eight complete graph fixtures,6860 edge/drop
checks and14 mutations are controls, not extrapolation to the root.
Resource bounds and actual source/input/output/interpreter hashes are saved.
The input rotations were prepared with NetworkX3.6.1; the final standard-
library checker verifies the rotations themselves, every dart, degree,
triangle exclusion and Euler count without importing that library.
No Lean, SMT, registered verifier, EvidenceLink, Result or admission ran.

Dependencies are acyclic: edge definitions -> paired O witnesses -> endpoint
case split; edge inequalities -> zero-cone criterion -> conditional repair;
case split and congruence -> next return condition. Hand claims do not use
finite tests as an all-size premise. Symmetry: BOTH original p cases are
checked with the same paired boundary and distinct O fills. C2 is untouched.
Probability methods are not applicable to these deterministic exact claims.

closed_residual_classes: []. open_residual_classes: [C1,C2,C3,C4].
best_verified_candidate: none. best_verified_result: none.
first_open_state: C1(1,0,2,0), with p14 still required.
Open admitted obligations: obligation:opg401-z20-extension; obligation:opg401-root.

New necessary condition in this structural class: the offending R-side pin
must be distinct from the Q pin, must have the additional color6 successor,
and its complete zero cone must reach y,P,S or a truly fixed value. The first
possible unpinned return is the12-edge path to y. Next retain its real chords
and third-neighbor boundary response, rather than the bare-cycle drawing,
and prove a safe release outside the bounded-drop chamber or a net-smaller
uniformly liftable absorption. Such an existence theorem for genuine minimum
obstructions remains OPEN. Do not turn the subcase exclusion into C1 closure.
