# V11: single-hit zero-cone release for one fixed endpoint

Status: NONTERMINAL_CHECKPOINT. Verdict: candidate_only.
Candidate: candidate:opg401-a01-v11-single-hit-release.
Repository: vibemathing/problem-opg-401-circular-coloring-subcubic-planar.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1. Target: obligation:opg401-root.

## 1. Frozen interface

Colors are residues 0,...,19. EdgeOK(a,b) means 7 <= [b-a]_20 <= 13.
The original eight-vertex region O has vertices (a,u,b,c,v,d,e,f), edges
au,ub,bc,cv,va,cd,de,ef,fb and incidences aP,dQ,eR,fS.
C1 has actual port colors (P,Q,R,S)=(p,0,2,0), p in {1,14}.

Use the V10 zero-endpoint interface in the actual exterior H=G-V(O):
N_H(Q)={y,X}, N_H(R)={y,Y}, with actual colors
Q=0,R=2,y=9,X=13,Y=13.  X and Y are distinct in the current branch.
All real exterior edges, chords, repeated endpoint identities and the inherited
rotation are retained.  B denotes any additional set of vertices whose actual
colors are required to remain fixed unless one named endpoint is explicitly
released.

For an oriented H edge uv put
    w(u,v)=13-[f(v)-f(u)]_20.
A zero arc is therefore exactly an edge with forward color difference 13.
Let K=H-{Q,R} and let C be the complete forward-reachable set from Y in the
zero-arc digraph of K.  Thus C contains every branch and chord-reachable
zero successor; it is not a chosen Steiner path.

V10's paired target Q=2,R=19 requires Y to drop by at least one, X by at most
four, and y to stay fixed.  The present atomic class is that C hits the fixed
boundary in exactly one releasable endpoint.  The endpoint may be
(1) an ordinary member z of B, not y,P,S;
(2) P; or
(3) S.
In every case C avoids y and every other still-fixed vertex.  The named
endpoint is a single physical vertex even if it occurs on several boundary
incidences.

## 2. Zero-cone shift lemma

Let D be any set of vertices in a valid (20,7)-colored graph such that no
zero arc leaves D.  Define g(v)=f(v)-1 mod20 for v in D and g(v)=f(v)
otherwise.  Then g is valid.

Proof.  Edges with both or neither endpoints in D keep their difference.
For a crossing edge u in D, v outside D, let r=[f(v)-f(u)]_20 in[7,13].
After the shift its difference is r+1.  It is legal exactly when r<=12.
The only forbidden crossing is r=13, which is exactly a zero arc u->v.
The opposite crossing orientation is the same undirected edge viewed from
the endpoint in D; its new representative is the inverse of r+1 and is legal
by the same condition.  Since C is the full zero-forward closure, no zero arc
leaves C.  Hence subtracting one on C checks every actual edge, including
chords and edges incident with repeated boundary vertices.

The graph itself is unchanged, so simplicity, planarity, triangle-freeness,
maximum degree and the complete rotation system are unchanged.

## 3. One ordinary fixed endpoint

Suppose C meets {y,P,S} union B only in z in B, and z is eligible to be
released.  Drop every vertex of C by one, including z.  Keep every vertex
outside C fixed.  Then set Q=2,R=19 simultaneously.

All K edges are valid by section 2.  The four edges involving Q,R are:
Q-y: 2,9 (difference7);
Q-X: 2 with X=13 or12 (difference11 or10);
R-y: 19,9 (difference10);
R-Y: 19,12 (difference7).
Thus the actual exterior is valid.  The entire complement of C union{Q,R}
is unchanged.

The resulting O boundary is (p,2,19,0).  Complete O fills, in the order
(a,u,b,c,v,d,e,f), are
 p=1:  (14,7,0,8,1,15,6,13),
 p=14: (1,8,0,7,14,14,6,13).
Direct checking of the nine inner edges and four port edges proves both.

Therefore every actual coloring satisfying this single-hit hypothesis has one
specific composable repair; no boundary-projection substitution is used.

## 4. The one-port endpoints P and S

### P is the unique hit

Release P and drop the whole cone C by one.  Its new color is p-1 mod20.
Again set Q=2,R=19.  The four exterior Q/R edges are exactly as in section 3,
and all other H edges are covered by the cone-shift lemma.

The O boundary and fills are:
 p=1:  (P,Q,R,S)=(0,2,19,0),
       O=(7,14,1,8,0,15,6,13);
 p=14: (P,Q,R,S)=(13,2,19,0),
       O=(1,8,0,7,14,14,6,13).
Thus a zero cone whose only fixed hit is P is reducible for both C1 inputs.
This move changes three O ports in the p=1 row and also in the uniform
construction for p=14; no claim of a two-port bound is made here.

### S is the unique hit

Release S and drop the whole cone C by one, so S becomes19.  Here Q and R
need not change: keep Q=0,R=2.  The changed cut edges are still legal:
Q-y is 0,9; Q-X is 0 with X=13 or12; R-y is2,9; R-Y is2,12.
The O boundary is (p,0,2,19).  Fills are
 p=1:  (14,1,13,0,7,7,14,6),
 p=14: (7,0,13,1,14,8,15,6).

Hence the one-port S endpoint is safely releasable while every vertex outside
C remains fixed.

## 5. Minimum-path interpretation and termination

If one records only a shortest zero path from Y13 to a fixed endpoint, the
positive lengths to P1,P14,S0 satisfy respectively
  L=16,17,19 (mod20),
because 13L equals the endpoint color minus13 modulo20.
The proof above is stronger than a bare-path argument: it uses the entire
zero cone, so every zero branch and chord is automatically retained.  A
shortest path is only a certificate that the named endpoint lies in C.

Algorithmically, discover C by a queue.  The lexicographic pair
(number of undiscovered vertices, queue length) decreases on discovery/
processing.  After discovery there are exactly two finite phases: construct
and adopt the new exterior vector, then append the explicit O fill.
Every later operation uses that actual output.

Consequently, in a hypothetical minimum obstruction within the V10 structural
interface, the zero cone cannot have exactly one releasable fixed hit of the
types above.  If the first fixed endpoint is a one-port boundary endpoint,
another still-fixed vertex must occur in the same zero cone (or the endpoint
must be genuinely non-releasable by an external requirement).

This is a structural subcase exclusion only.  It does not show that every
remaining C1 coloring has such a single-hit cone, it does not close C1, and it
does not advance C2.

## 6. Boundary accounting

The recoloring does not delete vertices, so no cut incidence is discarded.
If one later absorbs the discovered cone, the induced-set formula must still
be used:
  b=n+6-2k-2c-d
for a connected induced exterior set W, with every real chord counted in c
and every physical cut edge counted once.  Repeated outside endpoints remain
one color variable but retain all of their edge incidences.

No absorption theorem is claimed in this packet.

## 7. Reproduction and open state

check.py exhaustively verifies the palette crossing-edge lemma, the Q/R cut
cases X=12,13, all four displayed O fills, and the three path-length
congruences.  These finite checks are controls, not the universal proof.
No Lean, SMT, trusted verifier, EvidenceLink or Result admission is run.

closed_residual_classes: [].
open_residual_classes: [C1,C2,C3,C4].
first_open_state: C1(1,0,2,0), with p=14 required in the same general bridge.
best_verified_candidate: none. best_verified_result: none.

Next atomic condition: in the V10 zero-return interface, every failed cone must
hit y or at least two still-fixed boundary vertices (or a genuinely permanent
pin).  Retain the joint fixed-hit set and prove a simultaneous multi-endpoint
release, or a net-smaller uniformly liftable absorption.  Do not return to
single-target axes, support-cap searches, or the already excluded shared-pin
class.
