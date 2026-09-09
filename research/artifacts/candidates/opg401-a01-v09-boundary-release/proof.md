# V09: releasing actual boundary vertices, weighted slack, and a coupled-cut obstruction

Status: NONTERMINAL_CHECKPOINT. Verdict: candidate_only.
Candidate: candidate:opg401-a01-v09-boundary-release. Owner: math-proof.
Repository: vibemathing/problem-opg-401-circular-coloring-subcubic-planar.
Problem: problem:opg-401-circular-coloring-subcubic-planar.
Attempt: attempt:web-20260906-opg401-a01. Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1. Target: obligation:opg401-root.
Read base: 2e835d8cc6674ecc31ff5b596f1ac5e1dfdd89bc (V08/PR32 merged).
All C1-C4 classes and both admitted obligations remain open. C2 is not advanced.

## 1. Scope, frozen objects, and the gap not claimed closed

Colors are Z20 with representatives 0..19. E(a,b) means 7 <= [b-a]20 <= 13;
the undirected distance is min([b-a]20,[a-b]20). A(a)=a+{7,...,13}.
On fixed representatives E is also 7<=abs(a-b)<=13. No arbitrary integer
lift is substituted for this distance. O has ordered vertices a,u,b,c,v,d,e,f,
edges au,ub,bc,cv,va,cd,de,ef,fb and incidences aP,dQ,eR,fS.
C1 is (P,Q,R,S)=(p,0,2,0), p=1 or14, with four DISTINCT physical vertices.

The task concerns an actual coloring f of H=G-V(O), not a projected boundary
representative. When a region is enlarged, ALL its induced edges, including
chords and repeated outside endpoint identities, are retained. A prescribed
fixed set B is never silently released. The graph and its given rotation
are unchanged by recoloring. Statements below about a pinned cut do not
assert that every genuine minimum root obstruction has that cut.

Inputs V03-V08 are candidates, not Evidence. C06 already gives uniform unit
shifts. Here different vertices have different bounded displacements and
all actual edge slacks and cut incidences enter one exact test. No claim of
novelty for difference-constraint methods is made. Proofs are provided below;
no external theorem is an unverified premise. No old excluded replacement,
one-port/one-reflection search, C40 control or same-axis pruning is replayed.

## 2. B1: exact bounded release on an arbitrary induced exterior, including chords

Fix any induced region Z of G containing O, and prescribe a concrete coloring
h on Z which satisfies EVERY edge inside G[Z]. It may change at most two O
ports; this requirement is checked separately on the actual vertex IDs.
Let K=G-Z. Its original coloring f is valid. We allow
                     g(v)=f(v)-d(v) mod20, 0<=d(v)<=6
on K and fix B subset K by d(v)=0. Unreleased vertices can also be pinned
by setting upper bound zero. This is an explicit MOVE FAMILY, not every
possible recoloring. The construction below works for EVERY actual f,h
passing its test, without replacing either by another fiber representative.

For each v in K form
 D_v={d in[0,6]: E(h(u),f(v)-d) for EVERY u in N(v) intersect Z}.
Without such neighbors D_v=[0,6]. Intersect with {0} when v is fixed.
These sets are empty or ordinary integer intervals [l_v,u_v]. Indeed a
single seven-color cyclic allowed interval, in displacement coordinates,
meets [0,6] in an interval: if it wraps at20 its high piece starts at least14
and cannot meet [0,6]. Intersections preserve the assertion. Multiple cut
edges to the SAME v all constrain THIS one d(v), not independent copies.
If any D_v is empty, the stated h has no allowed completion in this family.

For each actual K edge uv put r_uv=[f(v)-f(u)]20 in[7,13] and two arc weights
             w(u,v)=13-r_uv,    w(v,u)=r_uv-7.
Both weights are nonnegative and sum to6. The new residue has the integer
lift r_uv+d(u)-d(v) in[1,19], so it is legal EXACTLY when
             d(u)-d(v)<=w(u,v), d(v)-d(u)<=w(v,u).          (2.1)
No cycle or chord may be discarded. Zero-weight cycles are allowed.

Let dist be directed weighted shortest-path distance, infinity if unreachable.
Define
       d_*(v)=max(0, max_s (l_s-dist(s,v))).                (2.2)
Then the exact necessary and sufficient test is
                         d_*(v)<=u_v for every v.         (2.3)

Necessity: (2.1) summed along any s-to-v path gives
 d(v)>=d(s)-path_weight>=l_s-path_weight. Maximize over s and paths.
For sufficiency, the length-zero path gives d_*(v)>=l_v. For each u->v,
concatenate an optimal s-to-u path with that edge to obtain
 d_*(v)>=d_*(u)-w(u,v). Thus (2.1) holds. All coordinates are at most6
because l_s<=6 and weights are nonnegative. Condition(2.3) enforces pins
and every cut incidence. Combine h and f-d_*; internal Z edges use h,
internal K edges use (2.1), and every crossing edge uses D_v.
This proves the full same-f gluing statement edge by edge.

Moreover d_* is coordinatewise no larger than ANY feasible d. Its nonzero
support is therefore contained in every feasible support for this h and
move family. It minimizes support and every coordinatewise increasing cost
within that family; no global recoloring optimality is claimed.

A negative certificate for (2.3) is one simple path s->v with
             l_s - sum_path w > u_v.
Nonnegative weights allow deleting repeated-vertex cycles from a witness.
The certificate must keep vertex IDs, every actual oriented color difference,
weights, l_s and u_v. It rejects only the stated h and displacement family.

Implementation may initialize d=l and repeatedly enforce d(v)>=d(u)-w(u,v).
Each strict update increases an integer coordinate in[0,6]. There are at
most6|K| such updates; a queue removal without update decreases queue length.
The pair (6|K|-sum_v d(v), queue length) decreases lexicographically. At
termination, the vector is the least feasible lower envelope (2.2), as every
update is forced in any feasible vector and the final vector satisfies all
lower inequalities. If it exceeds an upper bound the stored forcing path
certifies failure. Zero-weight cycles do not permit nontermination.

Construct a NEW complete vector before using it. Individual assignments
need not have legal intermediate states. A later step acts on that actual
output and recomputes its constraints. Successful phases (solve, adopt,
fill/check O) decrease; failure is not falsely called a terminal fill.

## 3. B2: the exact terminal-release test for V08, with real exterior edges

Use V08's induced stem U={Q,R,y,w0,...,wm}, ci=16-7i, with actual colors
(0,2,9,ci), fixed Q/R neighbor color13, pins ai=ci+7, and terminal b=cm+7+s,
2<=s<=6. Initially it has no O fill with the whole complement fixed.
Assume b is a separate nonport vertex, has no other U incidence, and is not
one of the fixed ai or the Q/R pins. No other incidence of b is omitted.

First allow ONLY b's color to vary while all other H-U vertices stay fixed.
Without b, legal tail displacements satisfy 0>=x0>=...>=xm>=-6. The fork
fills O precisely when the root is10 or11, so the tail terminal must be
cm-6 or cm-5. Both values are attained. Therefore the complete possible
new b-color set before its OTHER edges is
            A(cm-6) union A(cm-5)=cm+{1,...,8}.            (3.1)
For s>=2 its old b-color is not in this set.

Write the colors of b's at most two other neighbors as cm+t_j, with the
unique lifts t_j in[s-6,s]. This is forced by the OLD valid b edges. A target
cm+j, 1<=j<=8, has directed integer difference j-t_j in[-5,12], so it is
legal exactly when j>=t_j+7. (The upper13 condition is automatic here.)
Consequently single-vertex boundary release, allowing ALL internal U colors,
is possible exactly when EVERY t_j<=1. Empty neighbor lists are allowed.
If so j=8 works and the explicit common C1 fill is available. If some
neighbor has t_j>=2, NO choice of b alone works, not merely the favored one.
This criterion checks real edges that the free-boundary response omits.

To propagate release through more of the ACTUAL complement without guessing
its shape, prescribe the positive stem vector Q5,R6,y18,wi=ci-5 and its O
fill. Let F be the UNION of all ai, the Q/R neighbors, P,S and the required fixed set B; pin every vertex in F.
The only positive cut lower bound in B1 is l_b=s-1; its upper bound is6.
All remaining mobile outside vertices have lower0 and upper6. Pinned cut
vertices permit their original values (the ai have displacement upper5,
and the Q/R pins are explicitly held zero). Thus release by this exact
nonuniform bounded family succeeds iff
             dist_w(b,F)>=s-1.                            (3.2)
Its actual witness is d(v)=max(0,s-1-dist_w(b,v)). A shorter path to a fixed
vertex is a complete negative certificate for this family. Every vertex
outside this weighted-radius region stays fixed, and only Q,R change among
the four ports. This is a conditional all-size criterion, NOT a proof that
minimum-obstruction geometry forces (3.2), nor a repetition of selective F.

The two internal O fills for Q5,R6 remain, in its stated order:
 p1: (8,1,14,2,15,12,19,7);
 p14: (1,8,15,2,9,12,19,7).
All nine inner edges and four port incidences satisfy E. A release that would
change a vertex also occurring as another pinned boundary variable must
use that same vertex's bound, and can fail for this reason.

## 4. B3: two individually flexible real boundary vertices may need joint release

This is a new exact colored-cut configuration, with a chord and repeated
external vertices retained. It demonstrates why 'one individually releasable
constraint must repair a negative response' needs a further structural proof.
It is not a counterexample to the genuine minimum-root-obstruction assertion.

Let U={Q,R,y,w0,w1,w2} induce Qy,Ry,yw0,w0w1,w1w2. Old colors are
             (Q,R,y,w0,w1,w2)=(0,2,9,16,9,2).
Fixed X has color13 and is adjacent to BOTH Q,R (one physical vertex).
There are distinct boundary vertices A0,A1,A2,B0,C0 with colors3,18,11,9,6.
The complete additional incidences are
 w0-A0, w1-A1, w2-A2, w2-B0, A1-A2, A2-A0, A1-C0.
A1 and A2 each have degree THREE. All vertices outside U union{A1,A2}
are fixed, including P=p,S=0,X,A0,B0,C0. Extra edges wholly in this fixed
complement cause no problem if the original f is valid. There are no extra
incidences at U,A1,A2. In particular A1-A2 is NOT deleted as a non-tree edge.

With the rest fixed, all allowable boundary PAIRS (A1,A2) are exactly
 (17,10),(18,10),(19,10),(18,11),(19,11),(19,12).             (4.1)
Proof: A1 must be in A(6)=[13,19], A2 in A(3)=[10,16], and their edge
requires A1>=A2+7. This enumerates the six pairs, not separate free lists.
The old pair is(18,11). Releasing A1 alone gives its two legal values18,19;
releasing A2 alone gives its two legal values10,11. Neither boundary vertex
is individually rigid, but the UNIQUE pair admitting an O fill is(17,10).

Here is a hand proof of that uniqueness. The fixed A0 makes w0 lie in[10,16].
The Q/R fork, including O with either p, requires w0=10 or11 (V08's interval
proof, restated by the pinned constraints q,r in[0,6] and the fork/O edges).
For a pair(4.1), w1 lies in[A1-13,A1-7], whose least element is at least4.
The edge w0-w1 therefore forces w0=11,w1=4,A1=17. Then(4.1) forces A2=10.
Now w2 is adjacent to4,10,9, and their common allowed set is exactly{17}.
The remaining fork values are uniquely Q5,R6,y18. Conversely this assignment
satisfies every stated edge and has the two explicit O fills in section3.

Thus NO internal U recoloring, however large or simultaneous, repairs the
state while releasing at most ONE of these eligible boundary vertices. The
minimum number of released real boundary vertices in D={A1,A2} is exactly2.
This is a release-cardinality minimum under an explicit fixed set, not a
claim of globally minimum planar exterior order or absence of all absorptions.
Other boundary vertices in B are not silently declared available.

For EVERY actual f satisfying the incidence/color hypotheses, the joint map is
 Q5,R6,y18,w0=11,w1=4,w2=17,A1=17,A2=10, unchanged elsewhere.                 (4.2)
Its support edges have absolute differences13,12,7,7,13,13,7,7;
its cut differences are8,7 at X;8,7 at the two A0 incidences;8 at B0;11 at C0.
These include EVERY changed edge. P,S remain fixed, so there are just TWO
changed ports. The map is the same concrete witness for both p values.
A legal sequence is A2->10, A1->17, w2->17, w1->4, then the four-point
Q/R/y/w0 update, then O fill. Each preparation has its actual neighbors as
listed and can be checked separately. The remaining six operations strictly
decrease; the final vector, not a substituted projection, enters later steps.
The scalar checker independently confirms that only(17,10) yields a fill.

B1 also derives this release without ignoring A1-A2: for the fixed desired
interior in(4.2), both boundary displacements have lower1. The least feasible
outside vector is d(A1)=d(A2)=1, all other vertices zero. Their old difference
13 supplies a weight-zero arc A1->A2. The fixed A2-A0 edge supplies weight1,
allowing the displacement to terminate at the unchanged A0. This is an
explicit slack-based boundary release on a cyclic enlarged region.

## 5. Full plane objects, identities, and absorption accounting

Two complete fixtures use indices
 Q0,R1,y2,w0=3,w1=4,w2=5,X6,A0=7,A1=8,A2=9,B0=10,C0=11,P12,S13.
The common edges are all edges of section4, plus S-B0. For p1 add a new Z14
of color10 and P-Z-A0; for p14 add P-A0 directly. All other edges are absent.
Thus H has15 or14 vertices. O is then attached with its literal four edges.
The certificate lists complete rotations, facial walks and both actual colors.
Both full graphs are simple, triangle-free and planar with maximum degree3.
Their order is not claimed globally minimal. They have some low-degree fixed
vertices and are not certified to satisfy the prior UNPINNED all-target,
all-repair and minimum-counterexample hypotheses. They test the true-release
interface with prescribed fixed colors, not that stronger missing bridge.

Let Z=O union U. Its cut has EIGHT incidences but SEVEN distinct endpoint
variables: P,S,X (twice),A0,A1,A2,B0. C0 is initially beyond the cut.
After releasing A1,A2 the induced enlargement has again eight cut incidences,
now SIX distinct variables: P,S,X (twice),A0 (twice),B0,C0.
A tree projection would lose both the A1-A2 cycle and one A0 occurrence.
All cut occurrences are listed with their physical endpoint IDs.

For connected exterior W containing k O ports, write n=|W|,
c=|E(H[W])|-(n-1), d=sum_W(3-deg_G). Then b=n+6-2k-2c-d.
Initially(n,k,c,d,b)=(6,2,0,0,8); after the two releases it is(8,2,1,0,8).
Adding just A1 or just A2 increases the cut by one. In general an enlargement
D disjoint from Z changes b by
  sum_(v in D) deg_G(v) - 2|E(D,Z)| - 2|E(G[D])|.
This follows by partitioning all edges incident with D. It includes every
chord and is independent of how many outside vertices share incidences.
No cut decrease is asserted merely from absorbing a path.

The initial fixed complement is an actual failed lift for deletion of Z;
even either single-boundary enlargement still fails. The two-boundary
extension repairs THIS coloring. It is not a proof that every coloring of
the smaller deletion graph lifts: such a result must quantify over its
entire actual boundary relation, not just this recorded input. No universal
smaller replacement or all-absorption failure certificate is supplied.

## 6. Reproduction and the precise remaining atomic obligation

check.py uses standard-library integers, literal edges and fixed boundary
identities. A modular slack solver is checked against ordinary absolute-
difference brute force on bounded graphs; a separate literal-edge O DFS
checks the two fills and six-pair response. All-size proofs B1/B2 do not rely
on finite agreement. The new six-cycle-with-chord control tests whether a
non-tree edge is accidentally dropped; it is not an old C40 experiment.
run.py records actual source/input/output/interpreter hashes, limits and exit
status. No Lean/SMT, registered verifier, EvidenceLink or admission is invoked.

closed_residual_classes=[]; open_residual_classes=[C1,C2,C3,C4].
first_open_state=C1(1,0,2,0); p14 remains part of the same required bridge.
best_verified_candidate=none; best_verified_result=none.
Open admitted obligations: obligation:opg401-z20-extension; obligation:opg401-root.

The task's universal minimum-obstruction bridge is still OPEN. B1 identifies
exact quantitative path obstructions for a declared bounded release; B3
shows that individual flexibility of every candidate boundary vertex need
not supply a one-vertex release. Next use the REAL minimum-obstruction
path-union region (not an assumed stem), retain its full boundary-variable
relation, and prove an appropriate joint release is forced or build a
strictly smaller replacement with uniform lifting. No theorem here forces
that occurrence, forbids all releases, or closes C1/root. Raising a fixed
support cap, discarding chords, splitting repeated endpoints or replacing
an actual boundary state by another one are not permitted shortcuts.
