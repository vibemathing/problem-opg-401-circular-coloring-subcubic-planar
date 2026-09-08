# Nonuniform switching from actual colorings: exact closure, C1/C2 repair domains

Status: NONTERMINAL_CHECKPOINT. Verdict: candidate_only.
Candidate: candidate:opg401-a01-v03-nonuniform-switch.
Owner: math-proof. Problem: problem:opg-401-circular-coloring-subcubic-planar.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1. Target: obligation:opg401-root.
Read main: 7928d42a5c57e0c94bbc694b1ee2efc63836ee39.
Retained V03 input: 3e76541c54bb1f7bc8c30c0d3ab85ad45f39aaf6.
All four whole residual classes and both admitted obligations remain open.
No seven-vertex replacement search or retained-J search is performed here.

## 1. Exact objects, actual-color quantifiers and dependencies

The palette is Z20, represented by 0,...,19. EdgeOK(a,b) means
7 <= [b-a]20 <= 13. The UNDIRECTED distance is
 delta(a,b)=min([b-a]20,[a-b]20).
Thus EdgeOK is delta>=7, equivalently 7<=abs(a-b)<=13 for these representatives.
The original eight-vertex region O, in order a,u,b,c,v,d,e,f, has edges
 au,ub,bc,cv,va,cd,de,ef,fb,
and boundary incidences aP,dQ,eR,fS. P,Q,R,S are DISTINCT vertices;
colors may coincide. C1 has (p,q,r,s)=(1,0,2,0) or (14,0,2,0).
C2 has (19,0,18,0) or (6,0,18,0), the images under color negation.

An exterior H retains all its original edges and its actual valid coloring f.
A prescribed fixed separator is a set B with specified values f|B. It need
not be a minimal vertex cut. Every proposed g must be legal on ALL H edges
and must equal f on B. A region chosen for a move has its entire complement
fixed. Vertex identities and the embedding are unchanged by the moves below.
No assumption that a convenient exterior coloring can be substituted for f
is made. The statements quantify over EACH actual f satisfying their conditions.

V01, V02, M07, m06 and the existing V03 drafts remain candidate inputs.
V02's outer-five-cycle patch theorem does not apply to O's outer-eight-cycle
two-pentagon disk. No premise below is an EvidenceLink. Local nonextension
is proved directly in section 4; positive extensions have a complete table.

The previous matching-and-recolor candidate attachment supplies the proposed
map F and separator controls, with proof SHA-256
cc712b15476f0d7b4a38f8c6b7a952dd032a9bbe2134d46b997dd25e919351fe.
That attachment is not falsely described as already present on main. Its
relevant definitions are restated here; no old execution is claimed as new.

## 2. Exact binary-choice switching, including an obstruction certificate

Let T:Z20->Z20 be ANY fixed map, let S0 be required selected vertices, and
let B be the fixed separator. A selector is a subset S of V(H), containing S0;
its coloring is g(v)=T(f(v)) on S and f(v) otherwise. This is a finite-choice
restriction on possible new colorings, NOT a description of every recoloring.

For each actual edge uv insert an implication u->v when
 not EdgeOK(T(f(u)),f(v)),
and v->u when not EdgeOK(f(u),T(f(v))). Mark uv as a forbidden selected pair
when not EdgeOK(T(f(u)),T(f(v))). Mark v as pinned when v in B and T(f(v))!=f(v).
These definitions are made from the ACTUAL f, not a boundary projection.

Claim N1: let C be the forward closure of S0 in this implication graph.
There exists a legal selector S containing S0 and preserving B if and only if
 C contains no marked pin and no two ends of a forbidden selected edge.
When it exists, the smallest selector C itself is an explicit witness.

Proof. In any legal selector, a selected u must select every implication
successor v, because the mixed edge with v unselected is illegal. Induction
on path length forces C into S. A marked pin in C or a forbidden pair with
both ends in C is therefore impossible in EVERY possible legal selector.
Conversely choose C. An edge with neither end selected remains legal by f;
one with both ends selected is legal by the forbidden-pair test; an edge
with exactly one end selected is legal because C is forward closed. Pins
outside C are unchanged, and any pin inside C is fixed by T. This proves
both directions, including equal-colored distinct vertices and non-injective T.

A failed test produces one or two simple directed paths from S0 to the
marked pin/pair, with the actual offending edge colors. These paths are a
complete finite negative certificate for this BINARY-CHOICE model, not a
certificate against other maps or arbitrary simultaneous recoloring.
With an adjacency list, closure and all edge checks take O(|V(H)|+|E(H)|).
Discovery adds only previously unseen vertices; |V(H)|-|C| strictly decreases
on each addition. There is no unbounded retry or hidden graph-size induction.

## 3. Reflection components and preservation of a fixed actual separator

Specialize to the palette involution tau_k(c)=k-c modulo20. It preserves
EdgeOK. Applying tau_k to both entries shows that
 EdgeOK(tau_k(a),b) iff EdgeOK(a,tau_k(b)).
Thus the two implications on an edge coincide and there is no forbidden
selected pair. Let L_k(f) be the undirected graph of incompatible mixed edges:
 uv is an edge of L_k(f) iff uv in E(H) and
 not EdgeOK(tau_k(f(u)),f(v)).

Claim N2: reflecting any union of connected components of L_k(f) gives a
valid coloring of H, fixing all vertices outside that union. It preserves
B precisely when every selected vertex in B has tau_k(f(v))=f(v).
This is also the exact characterization of legal selectors for this tau_k.
Proof: apply N1 and the displayed symmetry. A crossing H edge need NOT end
at a color fixed by tau_k; it need only be mixed-compatible. This distinction
strictly enlarges the earlier fixed-color two-vertex-separator construction.

Since the underlying graph is unchanged, every simplicity, triangle-free,
planarity and degree property is retained. In an embedded H the same rotation
system works. Cut vertices, repeated face walks and disconnected complements
cause no exception: the proof examines every actual edge, not a drawing.
An extra prescribed separator must be checked; it is never silently released.

## 4. A complete positive local table covering BOTH C1 values

Use k=8 when p=1, and k=16 when p=14. Reflect a subset of the four port colors.
Port bits are P=1,Q=2,R=4,S=8. For either (p,k), O extends after the reflection
if and only if the port mask is nonempty and not all four ports.

Here are complete internal witnesses for the seven nonempty masks not containing
P. The internal order is a,u,b,c,v,d,e,f. Each row can be checked on the nine
listed inner edges and four port edges using only the integers in section 1.
The complementary mask is obtained by applying tau_k to EVERY color in the row;
that global reflection proves the other seven cases without changing the graph.

| p | k | reflected ports | new (p,q,r,s) | inner witness |
|---|---|---|---|---|
| 1 | 8 | Q | (1, 8, 2, 0) | (9, 2, 15, 8, 0, 1, 14, 7) |
| 1 | 8 | R | (1, 0, 6, 0) | (8, 1, 14, 2, 15, 9, 16, 7) |
| 1 | 8 | QR | (1, 8, 6, 0) | (9, 2, 15, 8, 0, 1, 14, 7) |
| 1 | 8 | S | (1, 0, 2, 8) | (9, 0, 8, 15, 2, 7, 14, 1) |
| 1 | 8 | QS | (1, 8, 2, 8) | (8, 0, 7, 14, 1, 1, 9, 0) |
| 1 | 8 | RS | (1, 0, 6, 8) | (9, 0, 8, 15, 2, 7, 14, 1) |
| 1 | 8 | QRS | (1, 8, 6, 8) | (8, 0, 7, 14, 1, 1, 13, 0) |
| 14 | 16 | Q | (14, 16, 2, 0) | (4, 11, 0, 10, 17, 3, 14, 7) |
| 14 | 16 | R | (14, 0, 14, 0) | (1, 8, 15, 2, 9, 9, 1, 8) |
| 14 | 16 | QR | (14, 16, 14, 0) | (1, 8, 15, 2, 9, 9, 1, 8) |
| 14 | 16 | S | (14, 0, 2, 16) | (4, 17, 10, 0, 11, 7, 14, 3) |
| 14 | 16 | QS | (14, 16, 2, 16) | (4, 11, 0, 10, 17, 3, 14, 7) |
| 14 | 16 | RS | (14, 0, 14, 16) | (1, 8, 15, 2, 9, 9, 1, 8) |
| 14 | 16 | QRS | (14, 16, 14, 16) | (1, 8, 15, 2, 9, 9, 1, 8) |

For mask zero, nonextension has a short hand proof. With q=s=0,r=2,
d,f lie in [7,13] and e in [9,15]. Legality gives e=14,d=f=7 or e=15.
Any d=f makes b,c lie in the same seven-color allowed interval and prevents
bc from being an edge. Hence e=15 and {d,f}={7,8}. The remaining edges force
{b,c}={1,14}. The two two-edge paths through u,v require a in
 {15,16,17,18,19,0}=B6(1) intersect B6(14).
This is disjoint from A(1)=[8,14] and A(14)=[1,7]. For mask fifteen the same
nonextension follows by globally undoing tau_k. This proves the whole table,
not just agreement of two programs.

Claim N3 (uniform conditional C1 repair): for EVERY actual f with a C1 tuple,
if some eligible component C of L_k(f) meets a nonempty proper subset of the
four ports, reflect C and use the corresponding row (or its complement).
This gives a deterministic same-f witness g and a complete lift to O.
With no extra pins, such a C exists iff the four ports do NOT all lie in one
component of L_k(f). With pins, eligibility is the explicit N2 pin test.
This is a condition on actual graph connectivity, not on equal color labels.

Consequently, in a hypothetical minimum obstruction containing O, every
C1 exterior coloring must connect all four ports in L_8(f) for p1, and in
L_16(f) for p14. Otherwise N3 colors the original G. These are new necessary
conditions, NOT a proof that either connectivity is impossible in a minimum
obstruction. They add to, rather than replace, the old tight-reachability tests.

## 5. A real old-residual control: one chord defeats F but not N3

Take H on vertices 0,...,39, edges i--(i+1 modulo40) and the extra chord 18--28.
Let f(i)=7i modulo20. Use Q=0,R=26,S=20 and P=3 for p1 or P=2 for p14.
Four distinct ports have precisely the required colors and each has degree two
in H, hence degree three after O is inserted. H is simple triangle-free planar.
Its cycle remains a strongly connected directed Hamilton cycle of tight edges:
all the previously blocked tight-reachability relations hold. Each vertex is
fixed under any individual recoloring by its two cyclic tight neighbors.

For the earlier map, put
 W=(0,7,14,1,8,15,6,13,0,10,0,10,0,10,0,10,0,10,0,10),
 F(c)=W[3c modulo20]. It fixes 0,1,14 and takes 2 to 6.
The chord has actual colors 6,16, and F sends BOTH to zero. Thus the global
F move fails. Even an arbitrary selective application of this F cannot move R:
N1 forces the simple path 26->27->28->18, whose old colors are 2,9,16,6.
The first mixed choices are illegal, successively forcing the next vertex:
  F(2)=6 against old 9; F(9)=13 against old 16;
  F(16)=0 against old 6.
The selected chord then has colors F(16)=F(6)=0, impossible. This is an exact
negative certificate for 'choose old or F(old) at each vertex and move R'.
It is not a no-recoloring certificate: the next construction repairs it.

The fixed colors of tau_8 are 4 and14, occurring at vertices 2,12,22,32.
For the old construction with R selected and P,Q,S outside, the only possible
cycle interval isolated by one/two such fixed-color vertices without also
containing another port is the interval between 22 and32. The chord joins its
vertex28 to the outside vertex18. Thus none of those old separators works.
The certificate checks all ten sets of size one or two as a finite control.
There is no assertion that every possible reflection axis or separator failed.

Nonetheless the following N3 moves work, keeping their entire complements fixed:

| p | k | selected vertices | actual fixed separator | new tuple | inner witness |
|---|---|---|---|---|---|
|1|8|{39,0,1}|{38,2}, colors (6,14)|(1,8,2,0)|(9,2,15,8,0,1,14,7)|
|14|16|{38,39,0}|{37,1}, colors (19,7)|(14,16,2,0)|(4,11,0,10,17,3,14,7)|

These sets are precisely the Q components of the respective mixed-conflict
graphs. For p1 the changed colors at (39,0,1) are (15,8,1); for p14 the
changed colors at (38,39,0) are (10,3,16). The vertexwise changes are unequal.
All crossing edges and ALL other exterior edges are explicitly checked. The
fixed separator colors are not both fixed by the reflection; mixed-edge
compatibility, not the old fixed-color-separator shortcut, justifies the move.

A complete rotation system is specified algorithmically without omitting vertices:
in H use i:[i-1,i+1] modulo40, except 18:[17,19,28], 28:[27,29,18]. Its facial
walks have lengths40,11,31 and Euler characteristic40-41+3=2. For the full G,
label O's vertices40,...,47 in the internal order above. At each port t replace
[t-1,t+1] by [t-1,its O endpoint,t+1]. The inner rotations are
 a:[v,u,P]; u:[a,b]; b:[u,c,f]; c:[b,v,d]; v:[c,a];
 d:[e,c,Q]; e:[f,d,R]; f:[b,e,S].
The resulting graph has48 vertices,54 edges,8 facial walks; its full edges,
rotations, faces, initial exterior colors and repaired full colors are in the
certificate. This specifies a simple plane subcubic graph, not just a sketch.

This exterior is minimum ONLY within the restricted family containing a
spanning directed tight cycle with distinct equally colored Q,S and an edge
not preserved by F: a tight cycle has length divisible by20, and length20 has
no repeated color, so at least40 vertices are needed; without an extra edge
F preserves every edge. Our one chord realizes that restricted minimum.
No global minimum over all exteriors is claimed. This G has long degree-two
threads and an explicit full coloring, so it is NOT a minimum root obstruction.
The statement that every actual exterior satisfying the three OLD obstructions
admits selective F is withdrawn; the corresponding claim restricted to genuine
minimum obstructions is not disproved by this nonminimum graph.

## 6. C2, same-witness composition, strict descent and the remaining gap

For C2 use color negation. If p'=19 or6, let f=-f' and apply the corresponding
C1 construction with p=1 or14, then negate the ACTUAL resulting g. Its reflection
axis is -8 or -16 modulo20, and the nonuniform map is F2(c)=-F(-c).
All edge conditions, pin equality, rotations and the obstruction paths transfer
bijectively. Both explicit C2 fixtures and their full repairs are checked.
This processes C2 without merging colorings of two different replacements.

For composition carry the entire current f, graph, and fixed values. N1/N2
produce their specific g from that input, and any next operation recomputes
its predicates on THIS g. If f agrees with sigma on B, every step does too.
An induction on the finite number of such steps proves compositional soundness;
there is no existential boundary fiber substitution.

For N3 an algorithm finds the actual component by marking each vertex once.
Let u be its number of discovered vertices and q its remaining work queue size.
The pair (|V(H)|-u,q), ordered lexicographically, strictly decreases when a
vertex is newly discovered or a processed queue item adds no new vertex.
A simpler implementation marks the full successor set in one processing step;
then either the first coordinate decreases or the queue shrinks. The graph
is finite. After the component test succeeds, phase2 is replaced by phase1
(the actual reflection), and phase1 by phase0 (the explicit O extension).
Thus every certified successful instance terminates in a REAL full coloring.
A failed connectivity/pin test is an open case, not falsely called a terminal
extension. No rank proving coverage of all relevant exteriors is supplied.

Remaining exact obligation: in a hypothetical minimum obstruction, show that
one of the above actual-color conflict components is eligible and separates
ports, or give another separator-preserving nonuniform move / absorbed-region
replacement with a strict total vertex decrease. In the remaining case all
four ports can still belong to one L_8 or L_16 component. Planarity of L_k as
a subgraph alone does NOT forbid that: a connected embedded tree can contain
four cofacial terminals. A genuine extra structural argument is still missing.
No arbitrary 'no absorption' certificate or counterexample to the root exists
here. M07's three-port maximal-region lemma is not withdrawn.

## 7. Reproducibility and truth boundaries

Run python3 -I -S run.py from this directory. The child uses only exact standard-
library integers, literal graph edges and a fresh DFS. No old table constrains
the search. The proof above supplies all-size arguments separately. The actual
replay checks32 complete boundary masks,2800 directed palette edge/axis cases,
1260 selector-closure controls (all valid edges and three-vertex paths in the
stated tests),four full graph fixtures, and12 detected mutation witnesses.
All negative local masks are checked by literal-edge DFS; its completeness is
induction on the number of unassigned vertices, branching once over every
remaining color and pruning only an impossible incident edge.

Execution.json records the actual version, input/source/output hashes, exit
status and resource limits. The frontend generator's two code paths are not
separate trust principals. No Lean, SMT, trusted verifier, EvidenceLink, Result
or obligation admission occurred. Existing V03 observations are not replays
of this run, and transport checks do not verify these mathematical claims.

Atomic candidate claims: N1 exact switch closure; N2 component reflection;
N3 C1/C2 local table and conditional repair; N4 old-residual chord control and
selective-F failure; N5 actual-state composition and successful-instance descent.
Probabilistic and asymptotic methods are inapplicable. Global terminal coverage
is explicitly unresolved; the two old exhausted replacement families are untouched.

closed_residual_classes: []. open_residual_classes: [C1,C2,C3,C4].
first_open_state: C1 (1,0,2,0), with its p14 partner still required.
best_verified_candidate: none. best_verified_result: none.
Open obligations: obligation:opg401-root; obligation:opg401-z20-extension.
