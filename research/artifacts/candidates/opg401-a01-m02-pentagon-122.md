# The (1,2,2) pentagon: exact boundary relation and critical consequences

Status: candidate_only. Primary owner: math-derivation.
Candidate: candidate:opg401-a01-m02-pentagon-122.
Problem: problem:opg-401-circular-coloring-subcubic-planar.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1.
Target: obligation:opg401-root.
Local dependency remains open: obligation:opg401-z20-extension.
Cycle base: 7da5e4f96aab1566b2110d82df377de03e618485.

## 1. Frozen configuration and boundary quantifier

Let G belong to the frozen finite simple triangle-free planar subcubic
class. Consider the cycle a-u-b-c-v-a, where u,v have degree two
and a,b,c have degree three. Its thread pattern after suppressing
u,v is (1,2,2). Write alpha,beta,gamma for the outside neighbors
of a,b,c, and p,q,r for their prescribed colors, respectively.
All vertices outside the cycle are already properly (20,7)-colored
and remain fixed. All five cycle vertices may be colored afresh.

A five-cycle in a triangle-free graph has no chord. Thus these are
all boundary constraints. For the local calculation p,q,r are
arbitrary colors; coincident outside vertices only restrict which
triples arise in a particular graph.

Use Z20 and shortest circular distance delta as in c01, and
A(t)=t+{7,...,13}, B6(t)={x:delta(x,t)<=6}.
Intervals below are inclusive integer intervals reduced modulo 20
only when explicitly stated. No arbitrary integer lifts are used
in an edge predicate.

Claim P1 (claim:opg401-m02-boundary-table):
normalize q=0 and r=d=delta(q,r) by one translation/reflection,
and let s be the correspondingly transformed value of p.
The five-cycle fails to extend exactly in these cases:

| d | bad s |
|---|---|
| 0 | all twenty residues |
| 1 | {7,8,9,10,11,12,13,14} |
| 2,3,4,5,6,7,8,9,10 | none |

This is different from c05, which treats the OTHER two-degree-two
pattern (1,1,3). Neither table may be substituted for the other.
In particular delta(q,r)>=2 guarantees extension for EVERY p.

## 2. First eliminate the two degree-two vertices

Give a the prospective color x. By the exact length-two relation
from c01, colors y,z for b,c can be completed at u,v exactly when

y in A(q) intersect B6(x), z in A(r) intersect B6(x),
and delta(y,z)>=7.                                      (2.1)

The missing external edge at a requires x in A(p).
Let T(q,r) denote all x for which (2.1) can be satisfied.
Therefore the full extension condition is exactly
                         A(p) intersect T(q,r) != empty. (2.2)

No old outside color is changed in this derivation.

## 3. A signed-lift certificate for membership in T

Translate x to zero. Both y,z have unique lifts in [-6,6].
Their absolute difference is at most twelve; their shortest
distance is at least seven exactly when that absolute difference
is at least seven. Consequently, after possibly swapping the
roles of b,c, write y=-i, z=j with 1<=i,j<=6 and i+j>=7.

Let Q=[q-x]20 and R=[r-x]20 for this ordering. The edge constraints
y-q and z-r become

7<=Q+i<=13, 7<=R-j<=13.

All involved possible allowed intervals lie in 1..19, so this
uses no wrapped integer inequality. The permissible maxima of
i and j are min(6,13-Q) and min(6,R-7), respectively.
Checking the interval endpoints gives the exact criterion

1<=Q<=12, 8<=R<=19, and Q<R,                             (3.1)

or the same criterion with Q,R swapped.

For sufficiency, choose those two permissible maxima. If Q<=7,
the first is six and the second is at least one. If R>=13,
the second is six and the first is at least one. In the remaining
case Q>=8 and R<=12, their sum is 6+R-Q>=7.
For necessity the membership intervals imply the first two bounds,
and i+j<=13-Q+R-7=6+R-Q forces Q<R.

Thus (3.1) is a reconstructible certificate, not merely a search test.

For q=r it is impossible, hence T(q,q) is empty.
For q!=r it fails precisely when x=q or x=r, or both directed
residues Q,R lie in {1,...,7}, or both lie in {13,...,19}.

## 4. Compute T and prove the boundary table

Normalize q=0,r=d with 1<=d<=10.

For 1<=d<=6, the two last failure conditions from Section 3 give
x in [d+13,19] or x in [d+1,7], respectively. Including x=0,d,
taking complements yields

              T(0,d)=[1,d-1] union [8,d+12].             (4.1)

For 7<=d<=10, two centers at distance d cannot lie in either
seven-element interval of span six, so

              T(0,d)=Z20 minus {0,d}.                   (4.2)

At d=1, (4.1) is [8,13]. Its complement is the fourteen-element
cyclic interval [14,27] modulo twenty. The seven-element A(s)
fits inside that complement exactly when s in [7,14].
This is precisely the bad row in P1.

For 2<=d<=6, the complement of (4.1) has two components:
[d,7] and [d+13,20] modulo twenty. Each has length 8-d<=6;
the nonempty intervening gaps prevent a seven-consecutive-element
set A(s) from lying in their union. Thus every A(s) meets T.
For 7<=d<=10, the complement in (4.2) has only two elements,
again too few to contain A(s). The d=0 case was separate.
This proves the entire table without an enumerator.

For a fixed q there are twenty bad (p,r) with r=q and eight for
each of the two r at distance one: 36 altogether. Therefore
there are 720 bad and 7280 extendible ordered triples among 8000.
These counts are arithmetic consequences of the table, not
claimed program output.

An explicit construction chooses x in (2.2), applies (3.1) and
the permissible maxima to obtain y,z, and fills u,v by c01.

## 5. Structural consequence in a hypothetical minimum obstruction

Assume G has minimum order among non-(20,7)-colorable members of
the frozen class, and contains the stated pentagon. Set H=G-cycle.
The m01 dominated-vertex argument implies alpha,beta,gamma are
distinct: beta=gamma would create a triangle; alpha=beta or
alpha=gamma creates a four-cycle containing u or v of degree two.

Every component of H must have at least two edges to the cycle,
or its sole attachment would be a bridge of G. There are exactly
three attachment edges. Since H is nonempty and G is connected,
H is connected. In particular the three outside constraints cannot
be assigned unrelated component rotations in this minimal setting.

Every coloring of H must induce a bad row of P1. Hence

delta(phi(beta),phi(gamma))<=1 in every coloring of H,    (5.1)

with the additional stated s restriction when that distance is one.

Claim P2 (claim:opg401-m02-external-five-cycle):
beta,gamma are nonadjacent and have a common neighbor in H.

If they were adjacent, every coloring of H would have distance at
least seven, contradicting P1. If they were nonadjacent with no
common neighbor, add the edge beta-gamma to H. Their degrees in
H are at most two. The new edge creates no triangle. For planarity,
the deleted curve beta-b-c-gamma can be followed in the drawing
to add the edge without meeting H internally. Thus the augmented
graph is a smaller member of the frozen class. Its coloring gives
distance at least seven, and P1 extends it to G, a contradiction.

For a common neighbor z in H, b-beta-z-gamma-c-b is a second
five-cycle sharing edge bc with the original one. This does not
assert that the second five-cycle is a face. It is a new necessary
configuration; it is not yet a contradiction.

## 6. A quantitative rigidity consequence

Claim P3 (claim:opg401-m02-order-bound):
a minimum obstruction containing a (1,2,2) pentagon has at least
23 vertices. If every coloring of H gives beta,gamma equal colors,
the same argument gives at least 26.

For any coloring of H form tight arcs s->t when
[phi(t)-phi(s)]20=7. Adding one to every color in a set X is valid
exactly when no tight arc leaves X: a crossing residue from X to
its complement changes from d to d-1 and fails only at d=7.
Thus the vertices reachable from any start can always be shifted.

If a coloring has delta(phi(beta),phi(gamma))=1, name its two
endpoints l,h with phi(h)=phi(l)+1. If l were not reachable from h,
shifting the reachable set of h would give distance two, violating
(5.1). A shortest directed h-to-l path is simple. Its length L
satisfies 7L=-1 modulo twenty, hence L=17 modulo twenty since
7 inverse is 3. Therefore H has at least eighteen vertices and
G has at least 18+5=23.

If no coloring has distance one, (5.1) forces equality in every
coloring. The same reachable-set shift forces mutual reachability.
A positive simple path between these distinct, equally colored
endpoints has length divisible by twenty, hence H has at least
twenty-one vertices and G at least 26. These are conditional
order bounds only, not a graph enumeration or a global bound
for obstructions lacking this pentagon.

## 7. Attacks, sources, and the next gap

Equal q,r is genuinely fatal to a fixed boundary: the adjacent
vertices b,c would both lie in A(q), an interval of span six.
For q=0,r=1, p=7 is bad whereas p=6 is good.
A witness for the latter has cycle colors in order a,u,b,c,v:
13,0,7,14,1. Its edge distances are 7,7,7,7,8 and its external
distances to p=6,q=0,r=1 are 7,7,7.
At d=2, T={1} union [8,14], and every A(p) intersects it.
These tests check the strict threshold and the two components.

All bad triples can be realized as proper colors of three isolated
pendant outside vertices. The graph itself is a five-cycle with
leaves and is colorable; such a fixed-boundary failure is not a
counterexample to the root. Whole-component rotations are NOT
assumed to modify the relative colors within the connected H.

Generated inputs at the cycle base: c01, c03, c06, m01.
External literature is used only in the companion scope note.
No theorem-prover, graph/color enumerator, or mathematical runtime
was run for this candidate. Text serialization/hashing are transport
helpers. Reproduce the proof using (3.1), the two component formulas,
and the explicit coloring; a future checker may enumerate q=0
and all 400 pairs (p,r), but must not replace the proof by a count.

Requested verification: kernel_check, axiom_escape_audit,
statement_faithfulness. Fixture verifier suitability remains a
separate trusted decision. No receipt is created here.

best_verified_result: none. best_verified_candidate: none.
Open obligations: obligation:opg401-root; obligation:opg401-z20-extension.
Registered failed-route IDs checked: [].
Route status: active; one unresolved unavoidable pattern now has
an exact boundary relation and a forced overlapping five-cycle.
Next action: eliminate overlapping (1,2,2) faces sharing a
length-two thread, then tighten the weighted-core unavoidable
family; handle the remaining all-cubic four-face explicitly.
