# V06: all target colors, complete pivot blockers, and a three-vertex repair

Status: NONTERMINAL_CHECKPOINT. Verdict: candidate_only.
Candidate: candidate:opg401-a01-v06-all-target-blockers.
Primary owner: math-proof.
Repository: vibemathing/problem-opg-401-circular-coloring-subcubic-planar.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1. Target: obligation:opg401-root.
Read main: de730bc8fbebd354651f8768d2ed63a257745df9.
Both admitted obligations and all four entire residual classes remain open.

## 1. Freeze, provenance, and scope

Colors are residues 0..19. Write r(a,b)=[b-a]20 and
 delta(a,b)=min([b-a]20,[a-b]20).
EdgeOK(a,b) means 7<=r(a,b)<=13, equivalently delta>=7; only fixed
representatives may be used in 7<=abs(a-b)<=13. Set A(c)=c+{7,...,13}.
O has the eight distinct vertices (a,u,b,c,v,d,e,f), nine internal edges
 au,ub,bc,cv,va,cd,de,ef,fb,
and four incidences aP,dQ,eR,fS. The outside vertices are distinct, in disk
order P,S,R,Q, although Q and S have equal COLORS. C1 is (p,0,2,0), p=1,14.
C2 is its color negation, p=19,6, r=18.
H=G-V(O) keeps every actual outside edge and a given valid coloring f.
A fixed set B has its actual values f|B; it is never silently released.

Read inputs are V03/nonuniform-switch and V04/steiner-pivot on the read main,
the separate pending attachment V05/axis-exhaustion, and the four-file remote
V05/axis-blockers draft at 34f07affc1212cd385e801d078b654a53ae33b48.
The latter and the attachment are different inputs, not interchangeable names.
No old execution is represented as a new run. V03/V04/V05 are candidate inputs,
not mathematical Evidence. Main's failed-route ledger was read empty.

The current minimum-counterexample disjunction is not proved or disproved.
We disprove universal success of ONE port-preserving reflection followed by
ONE port recoloring, even with every O-compatible target allowed, on arbitrary
plane subcubic exteriors satisfying the stated degree/conflict conditions.
The explicit graphs have successful three-vertex recolorings and are NOT
root counterexamples. No claim that all absorptions fail is made.
No stationary <=7 replacement, retained-J, selective-F, C40, or same-axis
Steiner-pruning search is conducted.

## 2. T1: complete symbolic single-port target table

For a boundary beta, D_t(beta) consists of all z for which replacing just
beta_t by z admits a coloring of O. For BOTH C1 inputs the exact table is:

| old p | change P | change Q | change R | change S |
| 1 | 2..13 | 8..19 | 3..17 | 8..19 |
| 14 | 2..13 | 8..19 | 3..18 | 8..19 |

All intervals are inclusive ordinary representatives. There are 51 and52
(port,target) pairs respectively, not merely the primary reflection targets.
The certificate supplies a full eight-color O witness for every positive row.
The negative cases follow from the following short interval derivation.

Ear calculation. Given colors D,F on d,f, the a-u-b-c-v-a ear with its p
incidence extends precisely when D!=F and either delta(D,F)>=2 or, when
that distance is one, p is outside A(D) union A(F).
Here is a derivation rather than an assumption from an earlier candidate.
Fix a's color z and translate it to zero. The two branch colors lie in the
signed interval [-6,6]. A nonzero outside residue j permits exactly
 [max(-6,j-13),min(6,j-7)]; residue0 permits none. For two nonzero residues
P<Q, their two permitted intervals admit a legal edge iff their extreme
separation is at least7, namely iff P<=12 and Q>=8. Clipping at -6 and6
proves this in the cases P<=7 and P>=8. Normalize F=0,D=d in1..10.
Undoing the translation shows that a's possible colors BEFORE imposing p are
 {1,...,d-1} union [max(8,d+1),min(19,d+12)].
For d=1 this is [8,13], which A(p) misses exactly for p in[7,14]. For d>=2
the complement contains no seven consecutive cyclic colors, so EVERY A(p)
meets it. If D=F, b,c lie in the same span-six allowed interval and cannot
be adjacent. This proves the ear criterion, including sufficiency; the two
length-two paths are then filled by intersection of their allowed-color sets.

P row: q=s=0,r=2 forces e=15 and {d,f}={7,8}; equal d,f is impossible.
The remaining edges force {b,c}={1,14}. Thus a must lie in
 B6(1) intersect B6(14)={15,16,17,18,19,0}.
A(p) meets this set exactly for p in2..13.

R row: d,f must be DISTINCT elements of A(0) intersect A(e). The intersection
has at least three elements exactly for e in[-4,4]20; then the ear can use a
pair at distance at least2 and any p works. At e=5 its two elements are12,13:
p1 fails the distance-one ear condition, but p14 works. At e=15 the two
elements are7,8 and both p1 and p14 fail. Other e give at most one element.
Thus the permissible central colors are [-4,4]20 for p1 and[-4,5]20 for p14.
Intersecting with A(r) gives exactly r=3..17 or3..18.

Q row: with r=2,s=0, the pair(e,f) is (14,7), (15,7), or(15,8).
For (14,7), the ear permits d=1..6 for p1 and1..5 for p14.
For e=15 and f chosen from7,8, it permits d=2..6 for either p.
The union is d=1..6 in both cases. Hence A(q) must meet[1,6], equivalent
to q=8..19. Every listed d has its stated e,f witness. The S row follows
by the graph automorphism exchanging b,c; d,f; u,v, while fixing a,e.
This proves the whole table without extrapolating any finite computation.

## 3. T2: complete test of every target on ONE actual coloring

Given t,z, put c=f(t), I=A(c) intersect A(z). Stage one fixes ALL four ports
and B and chooses one palette reflection tau_ell(x)=[ell-x]20 on some vertices.
Stage two changes only t to z. If t is fixed in B and z!=c, reject the move.
The locally eligible axes are exactly
 E(f,t,z)=intersection_(v in N(t), f(v) notin I) (f(v)+I).
With no constraints E is the whole palette. With constraints, if m=|I| and
w is the diameter of the representatives [f(v)-c]20 for constrained neighbors,
                         |E|=max(0,m-w).
These neighbors lie in[7,13]. Lift the cyclic interval I to an integer interval;
all its translates by these representatives fit in span at most12, so modular
projection is injective there. Their common length is m-w. Empty I with a
nonempty neighborhood gives no eligible axis. This concerns local choices,
not whether a globally legal reflection exists.

For ell outside E, one neighbor has neither old nor reflected color in I.
For ell in E, require the old-outside-I neighbors selected; forbid any old-only
neighbor, and every port or B vertex whose color the reflection would change.
Let U be the union of actual L_ell(f) components containing required vertices.
The move exists iff U misses every forbidden vertex. Necessity: a legal
selector cannot cut a conflict edge. Sufficiency: reflect precisely U; edges
inside U use an isometry, edges outside keep f, and crossing edges are mixed
compatible. The actual f1 fixes ports and B. All t-neighbors lie in I, so
changing t gives actual f2; adjoining T1's exact O fill is valid on every edge.
A failed case has a zero-choice neighbor or a required-to-forbidden path,
whose tail may be an OLD-ONLY NEIGHBOR, not necessarily a port.

This is an exact criterion for the specified template, not a theorem that
some pair (z,ell) succeeds. All 51*20=1020 or52*20=1040 pairs are considered.
Local E filtering is done before closure. Complexity for a fixed four-port
input is at most1600 graph scans plus the fixed-size O table. Discovery marks
new vertices once, using the lexicographic rank (unseen vertices,queue length).
The outer count of unchecked pairs decreases. A successful phase rank proceeds
prepare -> change target -> fill O; exhaustion is an OPEN case, not a fill.
Every subsequent transformation is computed on the actual preceding coloring.

In particular all-target failure can NEVER be explained by zero-choice alone.
Each port has an adjacent good target: P1->2 or P14->13, R2->3, Q0->19,S0->19.
For a +1 target the only locally bad old neighbor color is c+7, and the six
axes are 2c+{15,16,17,18,19,0}; for a -1 target it is c+13 and the six axes
are 2c+{0,1,2,3,4,5}. If no such neighbor occurs, change the port directly.
Thus a complete failure forces neighbors8/7 at P,9 at R,13 at Q and S,
and at least six path certificates per port. Paths are required separately
for every target and are not reused merely because port projections agree.

## 4. T3: two saturated plane inputs where ALL targets and axes fail

Use a cycle 0..N-1 with ports on it. Enumerate its NONport vertices in cyclic
order v_j. Add a cycle on N..N+M-1, M=N-4, and spokes v_j--(N+j).
There are no other exterior edges. These are not replacement gadgets.

A: N=8, ports(P,Q,R,S)=(0,6,4,2), colors in vertex order
 (1,13,0,9,2,13,0,8, 6,16,6,15).
B: N=12, ports=(0,9,7,5), colors
 (14,7,14,1,13,0,9,2,13,0,8,1, 0,7,14,6,16,6,15,8).
They have 12 and20 exterior vertices. Every nonport is cubic; each port is
degree2 in H and cubic after O is inserted. All four ports lie in one L8
component for A, or one L16 component for B. Not every B cycle edge is claimed
conflicting. Their actual O boundary is exactly the stated C1 input.

Rotation: at a cycle vertex use[previous,next], appending its spoke if present;
at the spoke endpoint N+j use[N+(j-1)%M,v_j,N+(j+1)%M]. To insert O in the
port face, insert its neighbor between previous and next at each port; give
O the inherited rotations
 a:[v,u,P],u:[a,b],b:[u,c,f],c:[b,v,d],v:[c,a],
 d:[e,c,Q],e:[f,d,R],f:[b,e,S].
The certificate expands EVERY edge, rotation, face, and vertex color. The
checks verify simplicity, triangle-freeness, degrees and Euler characteristic2.
Equal colors at Q,S do not collapse their two vertices or boundary incidences.

For every positive T1 target, certificate.json contains exactly TWENTY
failure entries, ordered by ell=0..19. An integer is a zero-choice neighbor;
a vertex list is a required-to-forbidden path. Input colors, literal edges,
I and eligible-axis masks permit direct scalar verification of each entry.
There are 2060 C1 failures:1898 zero choices and162 conflict paths. Negating
actual colors, targets and axes leaves the same graph and path certificates;
the separate checker verifies all2060 C2 failures as well. No successful
instance was suppressed from this finite list. All good target colors, including
17 and18 when relevant, are present. Terminal old-only neighbors are retained.
This is a finite rejection certificate for EVERY move of the T2 template on
these two exact colorings, not a search-based assertion about arbitrary graphs.

The failure concerns the exchange family on arbitrary exteriors, not the
statement restricted to genuine minimum obstructions or its absorption
alternative. Both inputs have the explicit full repairs in section5. They
therefore cannot certify no coloring or no possible absorption.

Minimality boundary: A is order-minimal in the explicit two-cycle/spoke
architecture with four independent first-cycle ports: N>=8 and2N-4>=12.
There is no global minimum claim over planar exteriors. No corresponding
minimum-order claim is made for B; its20 vertices are an explicit bound, not
a proven optimum. Bounded exploratory coloring scans supplied the witnesses;
no completed graph census or proof by induction on tested graphs is claimed.

For each actual primary component and a minimum conflict Steiner tree T,
the certificate saves W=V(T), rotations, edge color differences in both
directions, mixed differences, and the two implications represented by each
conflict edge. For c=|E(H[W])|-|W|+1 and d=sum_W(3-deg_G), direct counting
verifies b=|W|-2-2c-d for the INDUCED O union W. Here d=0; missing tree
incidences are not discarded. The signed degree identity is also checked.
Neither small branch count nor the nonzero mod3 contribution proves success
of T2. No universal deletion or nonabsorption certificate is inferred.

## 5. T4: a common three-vertex repair, with quantified fixed-complement semantics

A useful replacement for the false universal T2 assertion is this exact
colored-configuration lemma. For EVERY actual valid H coloring having C1
boundary (p,0,2,0), p=1 or14, suppose distinct vertices w,y,S form an induced
path w-y-S; w,y are not ports. Let f(y)=13, f(S)=0. Assume
 * all neighbors of w other than y have colors in10..16;
 * all neighbors of y other than w,S have colors in0..3;
 * all neighbors of S other than y have colors in7..10.
The graph may have fewer than three neighbors at any of these vertices.
Any prescribed fixed set B must exclude the vertices whose values change.
Then the following SAME-f sequence is valid and keeps the whole complement:
                 w -> 3; then y -> 10; then S -> 17.
Proof: the first new color3 is adjacent to y13 and every color10..16.
The second new color10 is adjacent to w3,S0 and every color0..3. Finally17
is adjacent to y10 and every color7..10. Every other edge stays unchanged.
No unmentioned edge is allowed: the neighbor conditions quantify over the
complete actual neighbor lists. The same rotation remains a plane embedding.
S changes to a T1-good target for BOTH p values, so O has a specific fill.
For p1 use (12,0,11,18,5,7,14,4), and for p14 use (5,18,11,0,12,7,14,4),
in the order a,u,b,c,v,d,e,f. Check each of the nine inner and four port edges.
This proves an explicit forall-f-exists-witness statement on the given domain.

In A take(w,y,S)=(8,1,2); in B take(15,4,5). In BOTH fixtures their original
colors are(6,13,0). The first two changes are singleton reflections about
axes9 and3, computed on the actual current coloring. The fixed separator has
colors1,9,15,16; in fact every vertex outside the three-vertex support stays
fixed throughout. These singleton reflections become possible in that ORDER.
The original all-target pivot failed because it allowed only ONE preparatory
reflection, not because these colorings were unrepairable.

The stored full arrays f,f1,f2,f3 and O fills make composition explicit. A
rank equal to the number of remaining assignments, followed by the O-fill
phase, strictly decreases to zero. This is a bounded constructive repair,
not an unsupported claim of a decreasing global energy on all colorings.
For C2 negate every actual intermediate state and fill: the changes are
14->17,7->10,0->3. The supports, fixed vertices and graph stay the same.
The graph automorphism exchanging Q,S transfers the lemma to the other port
with the correspondingly permuted inner fill; no color identification is used.

No absorption is needed on these controls. We cannot assert that every
minimum-obstruction all-target blocker contains this path, or that arbitrary
Steiner absorption fails. Those are explicitly open graph-structural questions.

## 6. Reproducibility and pressure tests

Run python3 -I -S run.py from a fresh copy of this directory. A modular
implementation constructs E and conflict paths. The scalar verifier uses
ordinary representative distances, literal graph edges, actual pins and
old-only neighbor tests; it does not call the component search. A separate
literal-edge DFS supplies and checks the complete O target table. Branching
on every remaining color proves that finite DFS exact; its node cap causes
an error, not a negative answer. A finite vertex-subset check finds Steiner
minima only in the TWO supplied graphs, not an enumeration of replacements.

The actual run checks103 positive and57 negative O target entries,2060 C1
failures,2060 negated C2 failures, the full graph and three-stage witnesses,
and14 negative controls. An exploratory negative-control assertion was revised:
truncating a failure path may still leave another valid forbidden endpoint.
The final control selects a truncation that actually loses validity. This
was a control-design correction, not a mathematical counterexample or a hidden
successful run. Execution.json records the successful source/input/output
hashes, actual interpreter identity, exit status and resource limits.
No Lean/SMT, registered trusted verifier, EvidenceLink, Result or admission ran.
The implementations are in one generator trust domain, not separate principals.

## 7. Exact remaining obligation

All four whole classes C1,C2,C3,C4 remain open. The first open state is still
C1(1,0,2,0), and p14 must be covered in the same general argument.
The next unproved bridge concerns genuine minimum-obstruction exteriors where
ALL T1 targets and ALL T2 axes fail AND neither T4 nor its transported variants
supply a colored local repair. Their full path systems, actual embedding and
all induced boundary incidences must be retained. Prove the existence of a
longer same-witness local preparation or a strictly net-smaller absorption.
Do not equate exhaustive failure of this exchange family with failure of all
recolorings or all possible smaller replacements. M07 and the root are not
withdrawn. The exhausted replacement and same-axis routes must not be restarted.

best_verified_candidate: none. best_verified_result: none.
Open admitted obligations: obligation:opg401-z20-extension; obligation:opg401-root.
