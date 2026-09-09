# V13: bidirectional zero-cone quotient and an exact parity-collapse chamber

Status: NONTERMINAL_CHECKPOINT. Verdict: candidate_only.
Candidate: candidate:opg401-a01-v13-bidirectional-parity.
Repository: vibemathing/problem-opg-401-circular-coloring-subcubic-planar.
Attempt: attempt:web-20260906-opg401-a01. Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1. Target: obligation:opg401-root.
Read base: e1e019398fe2fbacd847746218ddd4ca7513b896 (V12/PR36 merged).

All residual classes and both admitted obligations remain open.  V12 is a
candidate input, not Evidence.  This note completes the reverse unit-shift
quotient, combines it with V12's forward quotient, and then gives an exact
larger parity-collapse chamber together with its smallest repeated-endpoint
obstruction.  It does not assert that an unknown minimum obstruction enters
that chamber, and it does not advance C2.

## 1. Frozen actual interface

Colors are residues 0,...,19.  EdgeOK(a,b) means
7 <= [b-a]_20 <= 13.  Equivalently the shortest cyclic distance is at least
seven.  The eight-vertex region O, in the order (a,u,b,c,v,d,e,f), has edges
au,ub,bc,cv,va,cd,de,ef,fb and incidences aP,dQ,eR,fS.  C1 has
(P,Q,R,S)=(p,0,2,0), p in {1,14}.

Use the V10/V12 exterior interface in H=G-V(O):
 N_H(Q)={y,X}, N_H(R)={y,Y}, f(y)=9, f(X)=f(Y)=13,
with X and Y distinct.  Put K=H-{Q,R}.  Every actual K edge, chord, repeated
physical endpoint, fixed value and inherited rotation is retained.  A zero
arc u->v is an actual oriented edge with [f(v)-f(u)]_20=13.

V12 proved the exact forward-closed downshift quotient.  Here a set D is
predecessor closed when u->v and v in D imply u in D, equivalently no zero
arc enters D.

## 2. Reverse unit shift: all-size edge lemma

If D is predecessor closed, add one modulo twenty to every color in D and
leave the complement fixed.  The result is a valid (20,7)-coloring of K.

For a crossing edge orient it from u outside D to v inside D and put
r=[f(v)-f(u)]_20 in {7,...,13}.  The new residue is r+1 and is legal exactly
when r is not 13.  The excluded value is precisely a zero arc entering D.
Edges with both ends on the same side keep their difference.  This checks
every actual edge, not a chosen path or tree.  The graph and rotation do not
change.

For vertices s,t, a predecessor-closed set containing s but omitting t exists
if and only if t does not reach s in the zero digraph.  Necessity is closure.
For sufficiency take all zero ancestors of s.  More generally, to contain a
finite seed set T and omit z, take the union of their ancestor sets; it works
exactly when z reaches no member of T.

## 3. Exact local response of an upshift containing Y

Let D be predecessor closed, contain Y, and avoid every permanent pin.  Put
 x=1[X in D], h=1[y in D], alpha=1[P in D], beta=1[S in D].
After the upshift,
 Y'=14, X'=13+x, y'=9+h, P'=p+alpha, S'=beta.

There are colors q,r for Q,R, legal on QX,Qy,RY,Ry, and a full coloring of O
if and only if

 p=1:  (alpha=1 OR h=1) AND (x=0 OR beta=0);               (3.1)
 p=14: h=1 AND NOT(x=1 AND alpha=1 AND beta=1).            (3.2)

This is a hand-checkable finite local statement, not an extrapolation.
The neighbor intersections are

 x h | available q | available r
 0 0 | {0,1,2}     | {1,2}
 0 1 | {0,1,2,3}   | {1,2,3}
 1 0 | {1,2}       | {1,2}
 1 1 | {1,2,3}     | {1,2,3}.

On these sets the exact O table needed for necessity is:

 p'=1,S'=0:  (q,r)=(0,3),(1,3),(2,3);
 p'=1,S'=1:  (q,r)=(0,3);
 p'=2,S'=0:  (0,2),(0,3),(1,2),(1,3),(2,3);
 p'=2,S'=1:  (0,2),(0,3);
 p'=14,S'=0 or1: (0,3),(1,3),(2,3), except that
                  p'=15,S'=1 leaves only (0,3);
 p'=15,S'=0: (0,3),(1,3),(2,3).

These rows follow by intersecting the seven-color lists on the d-e-f side
and then applying the distance-one ear criterion; certificate.json stores a
literal O witness for every surviving row.  Intersecting this table with the
four displayed q/r lists gives (3.1)-(3.2).

A compact positive choice is also useful.  For p=1, if alpha=1 take
(q,r)=(x,2); otherwise h=1 and take (q,r)=(x,3).  For p=14 take
(q,r)=(x,3).  The formula hypotheses are exactly the conditions under which
these choices and their stored O witnesses are legal.

## 4. Exact reverse reachability quotient and the combined skeleton

For p=1, an upshift succeeds exactly when there exist
 t in {P,y} and z in {X,S}
such that z reaches neither Y nor t.  Choose the ancestor closure of {Y,t}.
Formula (3.1) proves sufficiency; necessity chooses an included member of
{P,y} and an omitted member of {X,S}.  Thus every upshift fails exactly when

 [X reaches Y OR (X reaches P AND X reaches y)] AND
 [S reaches Y OR (S reaches P AND S reaches y)].            (4.1)

For p=14, an upshift succeeds exactly when some z in {X,P,S} reaches neither
Y nor y.  Hence every upshift fails exactly when each z in {X,P,S} reaches
Y or y.                                                       (4.2)

Combine this with V12's exact downshift no-go signatures.  Both directions
simplify to the following small skeletons:

 p=1:  Y->y, X->P, X->y, S->P, S->y;                       (4.3)
 p=14: Y->S, S->y, X->y, P->y.                             (4.4)

For (4.3), V12 downshift failure follows from Y->y together with X,S->P.
Conversely, if V12 fails through Y->P then (4.1) sends each of X,S either
through Y or directly to both P,y; if it fails through X,S->P, (4.1) and
Y->y again force both X,S->y.  This proves (4.3).  For (4.4), V12 gives
Y->S and Y->y.  Applying (4.2) to S forces S->y (possibly through Y);
the same argument forces X,P->y.  The converses are immediate.

The independent checker enumerates all 6,942 labeled preorders on
{Y,X,y,P,S}; the equivalences above hold in every case.  That enumeration is
a pressure test, while the closure arguments are the all-size proof.

## 5. A larger exact chamber: collapse actual old parity

Let C be an actual vertex set of K containing X,Y,y,P,S and all paths used
for (4.3) or (4.4).  We propose one simultaneous map on C:
 every vertex whose old color is odd receives A,
 every vertex whose old color is even receives B.
Vertices outside C stay fixed.  Q,R and O are colored afterwards.

For this fixed C the proposal is legal exactly under the following conditions.

1. Every edge of G[C] joins opposite old parities.  A same-parity internal
   edge would become A-A or B-B, and is impossible; an opposite-parity edge
   becomes A-B and is legal precisely when EdgeOK(A,B).
2. Let L_odd be the intersection of A(f(z)) over every actual crossing edge
   vz with v in C of odd old color and z outside C.  Define L_even analogously.
   Every crossing incidence is included.  Repeated outside endpoints keep one
   actual color but impose all their incidences.
3. Fixed selected vertices, if permitted at all, constrain A or B to their
   specified actual value.  Distinct fixed values of the same parity make the
   corresponding list empty.
4. There is a pair (A,B) in L_odd x L_even with EdgeOK(A,B).

Necessity is edgewise.  Sufficiency colors C by parity, checks every internal
and crossing edge by the four clauses, and leaves every other edge unchanged.
Thus the criterion is exact and constructive.  It retains chords and physical
endpoint identities rather than projecting C to its zero-path drawing.

The terminal response is unexpectedly favorable.  For every legal ordered
pair (A,B), Q and R can be chosen so that O fills for BOTH combined skeletons:
for p=1 the new boundary is (A,q,r,B), while for p=14 it is (B,q,r,B).
After rotating A to zero, d=[B-A]_20 is in {7,...,13}; the complete table is

 d | q r | O for p=1, order (a,u,b,c,v,d,e,f)
 7 | 7 10 | (7,0,8,1,14,14,2,15)
 8 | 7 11 | (7,0,8,1,14,14,2,15)
 9 | 7 12 | (7,0,8,1,14,14,3,16)
10 | 7 13 | (7,0,8,1,14,14,4,17)
11 | 7 13 | (7,0,8,1,14,14,5,18)
12 | 7 13 | (7,0,8,1,14,14,6,19)
13 | 8  7 | (9,2,15,8,0,1,14,2)

 d | q r | O for p=14
 7 | 7 10 | (15,2,9,1,8,14,3,16)
 8 | 7 11 | (15,2,9,1,8,14,3,16)
 9 | 7 12 | (2,15,8,1,9,14,3,16)
10 | 7 13 | (2,15,8,1,9,14,4,17)
11 | 7 13 | (2,15,8,1,9,14,5,18)
12 | 7 13 | (2,15,8,1,9,14,6,19)
13 | 8  7 | (2,9,16,8,15,1,14,3).

Add A to every entry to undo the rotation.  Each row checks Q/R against the
odd terminal color A and checks all nine O edges and four port incidences.
The checker additionally verifies all 140 ordered legal pairs (A,B).

A concrete common choice is A=12,B=2.  Then (q,r)=(0,3), with O witnesses
 (0,8,1,14,7,7,16,9) for original p=1 and
 (15,8,1,14,2,7,16,9) for original p=14.

## 6. Sharp obstruction to treating parity collapse as automatic

The five-cycle
 z-v0-v1-v2-v3-z
with old colors
 z=0, v0=13, v1=6, v2=19, v3=12
is a simple plane triangle-free subcubic control.  Select
C={v0,v1,v2,v3}.  Its three path edges are zero arcs.  The same physical
outside vertex z is adjacent to the odd vertex v0 and the even vertex v3.
Keeping z fixed forces both A and B into A(0)={7,...,13}; no two colors in
that span-six interval are adjacent.  If z is also selected, edge z-v3 has
two even old endpoints and becomes B-B.  Thus neither choice repairs this
control by parity collapse.

The complete rotation is
 z:[v3,v0], v0:[z,v1], v1:[v0,v2], v2:[v1,v3], v3:[v2,z].
There are two facial walks of length five.  The control is itself colorable
and is not a root counterexample.

This obstruction is smallest in the following stated sense.  If one outside
vertex is adjacent to both parity classes of a selected zero path, the two
attachments cannot be consecutive, because that would make a triangle.
Opposite parity along the path requires odd path length, so the least possible
distance is three edges, giving four selected vertices and the displayed
five-cycle.  This rejects only the inference that every combined reachability
skeleton automatically admits the two-color parity collapse.  It does not
reject a different simultaneous map, expanding the selected region, absorption,
or the root claim.

## 7. Boundary accounting, composition, tests, and exact open gap

No contraction of the reachability quotient changes the real cut.  For an
induced connected exterior set W containing k of the O ports,
 b=|W|+6-2k-2c-d0,
where c=|E(H[W])|-|W|+1 and d0=sum_W(3-deg_G(v)).  Chords increase c;
repeated outside vertices remain single variables but all incidences count.

Both constructions carry the entire actual coloring.  A closure search marks
each graph vertex once; the lexicographic pair (unseen vertices, queue length)
decreases.  After selecting a legal vector, adoption and the explicit O fill
are finite terminal phases.  Failure returns either a reachability path, an
internal same-parity edge, an empty boundary list, or a pair of exact list
masks with no legal A-B pair.

Pressure tests cover directed residues 7/13, all 32 upshift hit rows, all
6,942 terminal preorders, all 140 parity pairs, both original p values,
rotation/reflection, same-parity chords, repeated external endpoints, and
the five-cycle minimum.  The finite checker imports no V12 result table.

Dependencies:
 definitions -> predecessor-closed edge lemma -> local upshift table;
 local table + ancestor separation -> reverse quotient;
 reverse quotient + V12 forward quotient -> (4.3)-(4.4);
 parity edge/list criterion + seven-row terminal table -> conditional repair;
 five-cycle -> exact failure signature for that chamber.

closed_residual_classes: [].
open_residual_classes: [C1,C2,C3,C4].
first_open_state: C1(1,0,2,0), with p=14 required by the same general bridge.
best_verified_candidate: none. best_verified_result: none.

Next obligation: retain the actual even-difference chords and repeated
boundary endpoints in a combined-failure skeleton.  If the parity criterion
fails, use its first internal chord or incompatible list pair as the source
of a non-binary signed move, or build a uniformly liftable net-smaller
absorption.  The exact unit-shift and parity chambers do not close C1.
