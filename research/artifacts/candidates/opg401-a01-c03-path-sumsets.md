# Exact path endpoint relations: candidate c03

Status: candidate_only. Primary owner: math-derivation.
Candidate: candidate:opg401-a01-c03-path-sumsets.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1.
Target: obligation:opg401-z20-extension. Root: obligation:opg401-root.
Fresh cycle base: 44e8c3aa7d6ed9633cac080f1950dc2e433fd084.

## 1. Frozen extension question

Use Z20, the fixed residue [z]20, shortest distance delta, and the
allowed increment set S={7,...,13} from candidate c01.
Let P=x0-x1-...-xL be a path of L>=1 edges. Fix endpoint colors a,b.
Internal vertices have no additional constraints. Write r=[b-a]20.

Claim P1 (claim:opg401-c03-path-sumset):
P admits an endpoint-preserving (20,7)-coloring exactly when
r belongs to the image of the integer interval [7L,13L] modulo 20.

Claim P2 (claim:opg401-c03-path-classification):
for L=1 the condition is delta(a,b)>=7;
for L=2 it is delta(a,b)<=6;
for L=3 it is a!=b;
for every L>=4 it is automatic.

This extends the admitted local lemma along degree-two chains, without
changing the target obligation or claiming any new admitted ID.
Repeated colors on nonadjacent vertices are allowed.

## 2. Interval-sum proof and constructive witness

For each oriented edge choose its unique allowed increment
si=[phi(xi)-phi(x(i-1))]20 in S. Then b-a=sum(si) modulo 20.
Every such integer sum lies in [7L,13L].

Conversely, every integer h in [7L,13L] is a sum of L members of S.
Indeed write k=h-7L, so 0<=k<=6L. Successively assign
di=min(6,remaining k) to each of L positions, subtracting di.
The residual reaches zero within L positions because the total
capacity is 6L. Then si=7+di and phi(xi)=a+sum(s1,...,si) modulo 20.
All edge constraints hold, and the endpoint is b whenever h=r mod 20.

Thus the sumset has no gaps. For L=1 and L=2 its residues give the
stated conditions. For L=3 the interval is [21,39], whose residues
are exactly 1,...,19, so equality of endpoint colors is the only failure.
For L>=4 it contains the twenty consecutive integers
7L,...,7L+19, since 19<=6L. These represent every residue.

A deterministic witness for L>=4 chooses the unique h congruent to r
in [7L,7L+19], then applies the construction above. This avoids a
greedy choice of vertex colors that could get stuck at the last edge.
The same sum construction applies to a closed cycle with the last
endpoint identified with the first, provided the internal vertices
are distinct: use r=0 and then identify the endpoints consistently.

## 3. Exact counts for short paths, derived by coefficients

With the initial color fixed, increment sequences correspond
bijectively to internal colorings with a specified endpoint color.
Let C_L(k) be the coefficient of z^k in (1+z+...+z^6)^L.
The exact number is
  N_L(r)=sum C_L(k),
where the sum is over integers 0<=k<=6L with k=r-7L modulo 20.
This formula is finite and includes all possible wraps.

A hand-reproducible expression for C_L(k) is
  sum from j=0 to L of (-1)^j * binom(L,j)
       * binom(k-7j+L-1,L-1).
Here binom(n,m)=0 for n<m or n<0.
To derive it, expand
(1+z+...+z^6)^L=(1-z^7)^L*(1-z)^(-L)
as a formal power series, and take the coefficient of z^k.
The second factor has coefficient binom(k+L-1,L-1), equivalently
the elementary count of weak compositions into L parts.
No analytic convergence or infinite-limit interchange is used.

The counts depend only on t=delta(a,b), by reflection.
For L=2 they are the c01 table. For L=3, at t=1,...,10 use k=t-1;
there is only one allowable integer sum, and
N_3(t)=binom(t+1,2)-3*binom(t-6,2).
At t=0 the count is zero.

| t | N_2(t) | N_3(t) |
|---|---|---|
| 0 | 7 | 0 |
| 1 | 6 | 1 |
| 2 | 5 | 3 |
| 3 | 4 | 6 |
| 4 | 3 | 10 |
| 5 | 2 | 15 |
| 6 | 1 | 21 |
| 7 | 0 | 28 |
| 8 | 0 | 33 |
| 9 | 0 | 36 |
| 10 | 0 | 37 |

The table is an analytic coefficient evaluation, not reported
enumerator output. As an arithmetic cross-check of total mass,
N_2(0)+2*sum(t=1..9)N_2(t)+N_2(10)=49=7^2, and
2*(1+3+6+10+15+21+28+33+36)+37=343=7^3.
Distance ten has only one residue; distances one through nine have two.

## 4. Minimal-obstruction consequences

Suppose G has minimum vertex order among graphs in the contract class
without a (20,7)-coloring. Deleting vertices preserves that class.

Claim P3 (claim:opg401-c03-long-thread-reduction):
G contains no path of four edges whose three internal vertices all
have degree two. Delete those vertices, color the smaller graph, and
apply P2 with L=4 to its fixed endpoint colors. No additional edges
touch the deleted vertices, so no omitted constraint remains.

There is no missing short-cycle exception when the two exterior
neighbors of three consecutive degree-two vertices coincide.
That configuration is a four-cycle with those three vertices of
degree two. Delete them and use the closed four-edge version at r=0;
increments 10,10,10,10 give an explicit extension. Thus three
consecutive degree-two vertices on a path or cycle are excluded.

Every cycle component of length at least four is colorable by P2
with equal endpoints and the closed-cycle interpretation.
The triangle-free assumption excludes the three-cycle.

Claim P4 (claim:opg401-c03-short-thread-reduction):
A four-cycle with two adjacent degree-two vertices is also excluded.
Write it a-u-v-b-a with deg(u)=deg(v)=2. After deleting u,v the edge
ab remains, so its colored endpoints differ. P2 with L=3 extends.

For a three-edge path a-u-v-b with u,v of degree two, shortening it to
edge ab is another valid reduction whenever ab is already present,
or whenever a,b have no common neighbor outside the deleted path.
Planarity follows by contracting the path, and endpoint degrees do
not increase. When a new edge ab is inserted, the only possible new
triangle consists of ab and a common neighbor. Such a neighbor gives
a five-cycle a-u-v-b-z-a in the original graph.
Hence an adjacent pair of degree-two vertices in a minimal obstruction
must lie on a five-cycle. This agrees with, but does not rely on,
the different quotient argument in c02.

## 5. Attacks on overstrong extensions

L=3 is sharp: three increments in [7,13] sum into [21,39], which
contains no multiple of twenty. Thus equal fixed endpoints cannot
be joined by a three-edge (20,7)-colored path.
This remains a boundary-coloring obstruction, not a graph counterexample.

Take C5 in order a-u-v-b-z-a. Delete u,v and color the remaining path
a-z-b by 0,10,0. Both edges are legal but the endpoints a,b are equal,
so the deletion coloring does not extend along the three-edge path.
C5 itself is colorable, as exhibited in c01. This witness rules out
the incorrect claim that every adjacent degree-two pair extends from
every fixed outside coloring.

Removing the internal-degree-two assumption would leave extra edges
whose color constraints are not represented by the path sumset.
No reduction with such omitted constraints is asserted.

## 6. Reproduction, provenance, and checkpoint

Reproduce P1 by the capacity construction; check the four possible
length regimes; derive the count table from the two coefficient
expressions and inspect all deleted-vertex incidences in P3/P4.
No graph enumerator, solver, or theorem prover was executed.
Text preparation and file hashing are transport helpers only.

Sources: the frozen contract and target at this cycle base;
research/artifacts/candidates/opg401-a01-c01-local-extension.md;
research/artifacts/candidates/opg401-a01-c02-neighbor-quotient.md;
research/artifacts/source-notes/opg401-a01-c01-definition-sources.md.
No external theorem is used to assert novelty or close the root.

best_verified_result: none. best_verified_candidate: none.
Best generated material: c01-c03, with explicit logical dependencies.
Open admitted obligations: obligation:opg401-z20-extension;
obligation:opg401-root. Registered failed-route IDs checked: [].
Rejected shortcuts: arbitrary fixed-color extension of one degree-two
vertex or of two adjacent degree-two vertices.
Next action: handle five-cycles containing several degree-two vertices
using endpoint recoloring, rather than repeating the fixed-boundary
extension that the C5 witness excludes.
Required future capabilities: kernel_check, axiom_escape_audit,
statement_faithfulness. No such receipt is produced here.
