# V14: three global distance-class quotients for the remaining C1 interface

Status: NONTERMINAL_CHECKPOINT. Verdict: candidate_only.
Candidate: candidate:opg401-a01-v14-distance-quotients.
Repository: vibemathing/problem-opg-401-circular-coloring-subcubic-planar.
Attempt: attempt:web-20260906-opg401-a01. Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1. Target: obligation:opg401-root.
Read base: 25cebac2db8fd275f695cd073746533d2119f409 (V13/PR37 merged).

All residual classes and both admitted obligations remain open. V03--V13 are
candidate inputs, not Evidence. This note does not repeat a bounded support
search. It applies one explicit palette map to the complete actual exterior,
so every chord, repeated endpoint and inherited rotation is automatically
retained. It does not preserve an additional prescribed fixed-color set unless
the selected map fixes those actual values.

## 1. Frozen interface and realized distance classes

Colors are residues 0,...,19. Put

  delta(a,b)=min([b-a]_20,[a-b]_20).

An edge is legal exactly when delta is one of 7,8,9,10. The eight-vertex
region O has ordered vertices (a,u,b,c,v,d,e,f), edges
au,ub,bc,cv,va,cd,de,ef,fb, and incidences aP,dQ,eR,fS.
C1 is (P,Q,R,S)=(p,0,2,0), p in {1,14}.

Use the normalized V10--V13 exterior interface in H=G-V(O):
N_H(Q)={y,X}, N_H(R)={y,Y}, with f(y)=9 and f(X)=f(Y)=13. Put
K=H-{Q,R}. For its actual coloring f define

  Delta(K,f)={delta(f(u),f(v)): uv in E(K)}.

A map T:Z20->Z20 will be applied to EVERY vertex of K. Q and R are then
assigned explicitly, followed by an explicit coloring of O. No intermediate
fiber representative is substituted for f.

## 2. The {7,8} quotient

Let C=(0,8,16,4,12), indexed cyclically modulo five, and define

  T8(c)=C[2c mod 5].

If an old edge has cyclic distance 7 or 8, an oriented difference is one of
+/-7,+/-8. Multiplication by two modulo five sends these four residues to
+/-1. Consecutive entries of C differ by 8 modulo twenty. Hence T8 sends
every distance-7 or distance-8 edge to a legal edge.

The relevant images are

  T8(P)=16 for p=1, and 4 for p=14;
  T8(S)=0, T8(X)=T8(Y)=8, T8(y)=4.

Set Q=16,R=15. The four exterior incidences have cyclic distances
12,8,11,7 in the order Qy,QX,Ry,RY. Complete O witnesses are

  p=1, boundary (16,16,15,0): (3,11,4,17,10,9,2,11);
  p=14, boundary (4,16,15,0): (17,10,3,16,4,9,2,10).

The entries are in O order. Direct inspection checks all nine inner edges and
four port incidences.

## 3. The {7,9} quotient

Define

  T9(c)=0 if c is even, and 7 if c is odd.

Every oriented difference of cyclic distance 7 or 9 is odd. Thus its endpoints
have opposite parity and T9 sends the edge to colors 0 and 7.

Here T9(X)=T9(Y)=T9(y)=7, T9(S)=0, while T9(P)=7 for p=1 and 0 for p=14.
Set Q=0,R=14. All four exterior incidences have distance seven. Complete O
witnesses are

  p=1, boundary (7,0,14,0): (0,9,2,15,7,8,1,9);
  p=14, boundary (0,0,14,0): (9,16,3,15,2,8,1,10).

## 4. The {7,10} quotient

Define T10 by the following twenty-entry word, indexed by c=0,...,19:

  (0,7,14,0,7,0,1,7,0,3,7,0,7,8,0,7,10,0,7,14).

For a hand-auditable preservation certificate the rows below list
c, T10(c), the image of c+7 and its distance, then the image of c+10 and
its distance:

 c | T(c) | T(c+7),d7 | T(c+10),d10
 0 |  0 |  7,7 |  7,7
 1 |  7 |  0,7 |  0,7
 2 | 14 |  3,9 |  7,7
 3 |  0 |  7,7 |  8,8
 4 |  7 |  0,7 |  0,7
 5 |  0 |  7,7 |  7,7
 6 |  1 |  8,7 | 10,9
 7 |  7 |  0,7 |  0,7
 8 |  0 |  7,7 |  7,7
 9 |  3 | 10,7 | 14,9
10 |  7 |  0,7 |  0,7
11 |  0 |  7,7 |  7,7
12 |  7 | 14,7 | 14,7
13 |  8 |  0,8 |  0,8
14 |  0 |  7,7 |  7,7
15 |  7 | 14,7 |  0,7
16 | 10 |  0,10|  1,9
17 |  0 |  7,7 |  7,7
18 |  7 |  0,7 |  0,7
19 | 14 |  1,7 |  3,9.

Every displayed distance is legal. The table for c+7 also covers c-7 by
reindexing; c+10 is its own reverse.

The terminal images are T10(X)=T10(Y)=8, T10(y)=3, T10(S)=0, and T10(P)=7
or 0 for p=1 or 14. Set Q=16,R=15. The exterior incidence distances are
13,8,12,7. Complete O witnesses are

  p=1, boundary (7,16,15,0): (0,10,3,16,7,9,2,10);
  p=14, boundary (0,16,15,0): (10,17,4,16,3,9,2,11).

## 5. Structural consequence for a hypothetical obstruction

For d in {8,9,10}, if Delta(K,f) is contained in {7,d}, apply Td to all of K,
use the Q,R values in sections 2--4, and append the corresponding O witness.
Every K edge is legal by the quotient proof; every Q/R incidence and every O
edge is checked by the explicit data. This colors the original G.

Consequently, in any hypothetical uncolorable graph satisfying the frozen C1
interface, every actual coloring of H obtained by minimality must satisfy

  |Delta(K,f) intersect {8,9,10}| >= 2.                     (5.1)

This is a necessary condition, not a converse. The two non-tight classes may
occur far apart or in different exterior regions; no connected transition is
silently inferred.

## 6. Pressure tests and failure boundaries

Each quotient has a sharp declared scope.

* T8 sends the legal pairs 0--9 and 0--10 to distances 4 and 0, so it does not
  preserve classes 9 or 10.
* T9 sends 0--8 and 0--10 to equal colors, so it does not preserve classes 8
  or 10.
* T10 sends 0--8 and 0--9 to distances 0 and 3, so it does not preserve
  classes 8 or 9.

The checker verifies every source color and both orientations for each declared
class, all six terminal constructions, all nine O edges and four incidences,
translation of each O witness, and the six negative mutations above. The checker treats these finite checks only as controls; none is used to infer an
unbounded graph statement.

The graph is unchanged by all three operations, so simplicity,
triangle-freeness, planarity, degree bounds and the rotation system are
invariants. Construction has a finite rank: map the finitely many K vertices,
assign Q,R, append eight O colors, then perform one complete edge audit.

Dependencies:
  palette definitions -> edge-class preservation;
  terminal image calculation -> Q/R choices -> literal O witnesses;
  preservation + terminal witnesses -> theorem (5.1).

closed_residual_classes: [].
open_residual_classes: [C1,C2,C3,C4].
first_open_state: C1(1,0,2,0), with p=14 in the same general bridge.
best_verified_candidate: none. best_verified_result: none.

Next obligation: under (5.1), retain the first actual connected region carrying
two distinct non-tight classes. Test a three-level or signed potential whose
edge inequalities use both slacks, or give a net-smaller uniformly liftable
absorption. Do not conclude C1 from distance-class heterogeneity alone.
