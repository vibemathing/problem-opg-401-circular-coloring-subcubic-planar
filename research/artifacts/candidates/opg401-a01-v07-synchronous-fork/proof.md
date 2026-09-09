# V07: a minimal simultaneous two-port fork, beyond all-target pivots and three-vertex supports

Status: NONTERMINAL_CHECKPOINT. Verdict: candidate_only.
Candidate: candidate:opg401-a01-v07-synchronous-fork. Primary owner: math-proof.
Repository: vibemathing/problem-opg-401-circular-coloring-subcubic-planar.
Problem: problem:opg-401-circular-coloring-subcubic-planar.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1. Target: obligation:opg401-root.
Read main: af3f0fd46484471dd27039dd61ff8cd45f47fb64.
No entire residual class, root, or trusted obligation closes.

## 1. Definitions and exact advance

The palette is Z20 with representatives 0..19. EdgeOK(a,b) means
7 <= [b-a]20 <= 13, equivalently 7 <= |b-a| <= 13 for these representatives.
The UNDIRECTED distance is delta(a,b)=min([b-a]20,[a-b]20).
A(c)=c+{7,...,13}. An equality of colors never identifies two vertices.
O has vertices in order (a,u,b,c,v,d,e,f), edges
au,ub,bc,cv,va,cd,de,ef,fb, and incidences aP,dQ,eR,fS.
The four exterior vertices are distinct; their disk order is P,S,R,Q.
C1 has actual port colors (p,0,2,0), p in {1,14}.
An actual exterior coloring f of H=G-V(O) is carried through every operation.
For a support U the ENTIRE complement H-U stays fixed, including every cut
vertex, incidence and any additional prescribed fixed set B disjoint from U.

Current V06 is now on the read main. Its one-preparatory-reflection template
and three-vertex path repair are candidate inputs, not Evidence. This note
does not rerun a small-replacement census or the C40/same-axis/selective-F
routes. All-target tests below only certify the hypotheses of NEW finite
controls. No C2 research or propagation is performed before C1 closure.

Main new result: a four-vertex claw can have a UNIQUE filling state requiring
both Q and R to change. No sequence of moves changing at most three of its
vertices per step, with its complement fixed, can reach that state. A single
simultaneous four-vertex move works for BOTH p values. This is a local colored
configuration, not a proof that every minimum-obstruction exterior contains it.

## 2. S1: exact pinned-fork state space

Suppose distinct exterior vertices Q,R,y,w induce the claw Qy,Ry,yw, with
y,w not ports. Their actual colors, in this order, are (0,2,9,16).
Q and R each have exactly one other neighbor, colored 13; these other neighbors
MAY be the same physical vertex. w has exactly two other neighbors, colored
3 and 4 respectively. They are different physical vertices. There are no
other edges incident with the four-vertex support. All stated cut colors
and the rest of H, including P and S, are kept fixed.

For a possible new state (q,r,Y,W), the exact constraints are
 q,r in {0,...,6}=A(13), W in {11,...,16}=A(3) intersect A(4),
 and EdgeOK(Y,q), EdgeOK(Y,r), EdgeOK(Y,W).
All 26 states have the following HAND-DERIVED classification:

| Y | q and r, chosen independently | W | number |
| 7 | {0} | {14,15,16} | 3 |
| 8 | {0,1} | {15,16} | 8 |
| 9 | {0,1,2} | {16} | 9 |
| 18 | {5,6} | {11} | 4 |
| 19 | {6} | {11,12} | 2 |

Proof of exhaustion: Y<=6 cannot neighbor either q or r. For Y=7,8,9,
ordinary separation with q,r gives the displayed low values, and separation
with W gives the displayed high values. For Y=10..17, its separation from
W in11..16 is at most six, impossible. Y=18,19 give the last two rows.
All differences lie between -19 and19, so the fixed-representative test is
exact and no linear-lift boundary is being discarded.

Call the first twenty states L and the last six states U. Every coordinate
of every L state differs from the corresponding coordinate of every U state:
 q,r <=2 versus >=5; Y<=9 versus >=18; W>=14 versus <=12.
Consequently every L-to-U pair has Hamming distance FOUR.
This classifies the entire pinned state space, not just one execution path.

## 3. S2: precisely one state fills O, for either p

Among those 26 states, the UNIQUE O-fillable state is
                      (q,r,Y,W)=(5,6,18,11).               (3.1)
Here is the negative proof, without relying on enumeration.

In L, q,r lie in0..2. If r<=q, e in A(r) and f in A(0) can be adjacent
only with e>=f+7, hence e>=14. The other incident edge forces d<=e-7<=r+6,
contradicting d>=q+7. If q<r, the three possibilities are (0,1),(0,2),(1,2).
For (0,1), e=14 and d=f=7; then b,c both lie in A(7), a span-six interval,
so bc is illegal. For (0,2), e=14 again forces equality d=f, or e=15 and
{d,f}={7,8}. Equal d,f is always impossible. For (1,2), e=15,d=8,f=7
is the sole unequal option. In the last two cases the remaining edges force
{b,c}={1,14}. The length-two paths a-u-b and a-v-c require
 a in B6(1) intersect B6(14)={15,16,17,18,19,0}.
This is disjoint from A(1)={8,...,14} and A(14)={1,...,7}.
(The length-two condition follows by intersecting two translates of A.)
Thus none of the twenty L states fills O for either original p.

For the six U states, if r<=q the same inequality d>=q+7>r+6>=e-7
excludes a fill; all relevant A intervals still do not wrap. The only r>q
choice is q=5,r=6,Y=18,W=11. Explicit fills in the O vertex order are
 p1:  (8,1,14,2,15,12,19,7),
 p14: (1,8,15,2,9,12,19,7).
Each of the nine O edges and four port edges is checked directly. This proves
both directions of (3.1), and positive existence is not a solver assertion.

For EVERY actual valid exterior f satisfying the complete fork hypotheses,
define g=f off the support and
                 g(Q)=5, g(R)=6, g(y)=18, g(w)=11.          (3.2)
The internal support differences are13,12,7. The cut differences are8 at Q,
7 at R, and8/7 at w. Every other edge is unchanged. Adjoin the appropriate
O fill above. This is an explicit forall-f-exists-g, not an existential
choice from another exterior coloring with the same port projection.
Two ports change, not three or four. In particular (p,5,2,0) is not fillable:
the joint choice must not be split into a claim about Q alone.

## 4. Minimal simultaneous size, composition, and strict termination

The original state (0,2,9,16) belongs to L, while the unique filling state
belongs to U. Since every cross-phase pair differs in all four coordinates,
ANY sequence of valid intermediate pinned-fork states whose steps change at
most THREE vertices remains in L. It cannot fill O, no matter how long the
sequence is. This includes all earlier three-vertex repairs restricted to
this support and fixed complement. It does NOT forbid changes outside this
support or release of the actual cut colors.

Thus four changed vertices are necessary and sufficient in this pinned region;
the two-port update (3.2) is genuinely simultaneous in this move model. It
must not be executed as four individually assumed-legal assignments.
As a mathematical map, the old and new full colorings are both legal. A
program constructs g in a separate vector, checks it, then uses that vector.
The graph itself is unchanged, so its same rotation is still a plane embedding;
simplicity, triangle-freeness and maximum degree are automatic invariants.

Composition carries the complete actual g and fixed values to the next step.
The successful local algorithm performs finite pattern/cut checks, one atomic
vector update, and one explicit O fill. Its remaining-phase rank decreases
2 -> 1 -> 0. Pattern discovery scans finitely many length-two exterior paths.
Failure to find the pattern is OPEN, not a fake terminal extension. No rank
asserting universal progress on all minimum-obstruction exteriors is claimed.

Consequently a genuine minimum counterexample cannot have an actual C1
exterior coloring containing this colored fork with the permitted support.
The unproved bridge is the universal existence of this or another successful
configuration after the previous blockers are imposed.

## 5. Finite controls with all old pivots blocked and no three-vertex support

Two NEW controls have 28 and46 exterior vertices. They are NOT C40 controls,
replacement gadgets, or asserted minimum root obstructions. Both are colored.
Their construction is fully determined by input.json:
- start with the cycle 0..n0-1 and its four ordered ports;
- enumerate nonports v_j in cyclic order, m=n0-4;
- use a middle cycle of3m vertices, connecting v_j to middle vertex3j;
- connect middle vertices3j+1 and3j+2 to consecutive vertices2j and2j+1
  of a final cycle of2m vertices. No other exterior edges exist.
Thus every nonport is cubic, each port has degree two in H, and all are
cubic after O is inserted. The middle rotation puts inward and outward
spokes on different sides. The certificate expands every edge, vertex,
rotation and facial walk. Correct dart counting gives sphere characteristic2.
Its full graphs have (V,E,F)=(36,53,19) and(54,80,28).

For p1 the literal initial colors are the first input row. A minimal support
is the path (0,1,8,19), whose old colors are(1,8,15,2). Its new colors are
(2,9,0,7). The fixed other neighbor colors, along this path, are13;0;8;14,14.
The three new path differences are7,9,7 and the fixed-cut differences are
11;9;8;7,7. The entire complement is unchanged and the final O tuple is
(2,0,2,0), with fill (15,2,14,1,8,8,15,7). This support has one changed port.
Unlike the pinned fork, this path can also be executed in reverse path order;
its minimum TOTAL changed support is four, not a claim of indivisible execution.

For p14 the minimal support is the fork with (Q,R,y,w)=(6,4,5,17).
Its complete fixed-cut colors are precisely13,13,4,3. Formula(3.2) applies:
 Q0->5,R2->6,y9->18,w16->11, with the p14 fill in section3. All other42
exterior vertices are kept fixed. This is the two-port simultaneous example.

For each fixture, the finite checker independently regenerates all O-fillable
single-port targets by literal-edge DFS. It verifies ALL twenty auxiliary-axis
failures for each such target in the SAME actual initial coloring:1020 for p1,
1040 for p14. Each failure is a zero-choice neighbor or a required-to-forbidden
path checked by scalar edge tests, including old-only neighbors. These are
hypothesis checks on new objects, not a renewed search of the failed template.

It then enumerates EVERY exact changed support of size1,2,3 meeting any port,
including supports with THREE ports. Supports meeting no port preserve the
original bad O tuple. For each support, intersect A of ALL fixed outside
neighbors, remove its old color, and branch over every remaining internal
color, pruning only an impossible incident edge. Each full coloring is
counted once. A separate literal O DFS decides each resulting actual tuple.
The two counts are1358 and3878 supports, and no such assignment fills O.
This excludes ALL initial-to-final repairs with total support at most three,
not just a chosen list of familiar lemmas. It does not forbid arbitrarily
many successive steps whose union of changed vertices is larger than three.
The explicit four-vertex fills prove that the minimum total support is FOUR
for these finite inputs. No GLOBAL minimum exterior order is claimed.

Also included are two small connected pinned-fork plane witnesses (11 and10
exterior vertices) sharing the physical color13 cut vertex. These demonstrate
that repeated external vertices are retained, not replaced by separate free
colors. Their fixed-complement state space is exactly sections2-4. They are
not asserted to meet every hypothesis of a minimum root counterexample.

## 6. Steiner bookkeeping is retained, not used as a false reduction

For the two large controls, choose a minimum-edge conflict tree connecting
all four ports. A four-terminal subset dynamic program supplies its exact
cost: initialize singleton terminal distances; merge smaller terminal subsets
at a common vertex; relax along conflict edges. Every recurrence constructs
a connecting subgraph. Conversely, root an optimal tree; either its root is
terminal, lies on a path to the first branch, or separates nonempty terminal
subsets. Deleting that path or splitting at the branch gives the same
recurrences, proving optimality. The finite certificate stores costs and
an attained tree; this is only a control, not a structural theorem about G.

With W its vertex set, n=|W|, c=|E(H[W])|-(n-1), and
 d=sum_W(3-deg_G(v)), the INDUCED absorption O union W has
                     b=n-2-2c-d.
Its degree sum is22+3n-d, and its internal edge count is n+12+c. Subtracting
twice the latter proves the formula. The controls give(7,0,0,5) and(16,0,0,14).
Every actual cut edge is listed, including repeated outside endpoints.
Nothing turns b=14 into three independent port constraints. A universal
smaller replacement or all-absorption failure certificate is NOT supplied.
The positive recolorings mean these graphs cannot be root counterexamples.

## 7. Computation, controls and exact remaining gap

The proof of the pinned fork and its phase separation is elementary above;
enumeration is only a cross-check. check.py imports no previous candidate
code or boundary table. The certificate uses explicit typed run-length tables:
[support repetition,nodes,legal assignments] in the stated lexicographic
support order; [axis repetition,failure record] in axis order. Round-trip
expansion is checked exactly. This is not a binary or opaque archive.

Run python3 -I -S run.py in a fresh copy. The runner refuses to overwrite
the three certificate files and execution.json. It records actual source/input/output and
interpreter hashes, version, exit status and resource limits. Exact finite
work includes26 pinned states, two unique fills,5236 smaller supports,2060
axis failures and14 negative controls. The runtime is the candidate generator,
not a trusted verifier or independent principal. No Lean/SMT/admission runs.
Preliminary bounded coloring probes were discovery only, not a graph census.
An exploratory rotation convention was corrected before the final frozen
replay; the final certificate checks every dart. No failed exploration is
represented as a successful execution or mathematical counterexample.

closed_residual_classes: []. open_residual_classes: [C1,C2,C3,C4].
first_open_state: C1(1,0,2,0), with p14 still requiring the same global bridge.
best_verified_candidate: none. best_verified_result: none.
Open obligations: obligation:opg401-z20-extension; obligation:opg401-root.

Next atomic action: for a genuine minimum-obstruction exterior satisfying all
previous pivot/path exclusions AND lacking this four-vertex fork and its
allowed C1 port-position variants, locate a smallest permitted simultaneous
support or prove a strictly net-smaller induced absorption while retaining
its entire actual cut. There is no proof here that such a support always
exists. The exact size-four necessity is a support statement, not proof that
all hard exteriors are solved. C2 is kept open and has not been substituted
for the still-open C1 task.

Certificate layout: fork-certificate.json contains the complete pinned states, small plane witnesses and encoding; case-p1.json and case-p14.json contain the complete large controls and all their typed tables.
