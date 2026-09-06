# Common-neighborhood cardinality and two-color certificates: c08

Status: candidate_only. Primary owner: math-derivation.
Candidate: candidate:opg401-a01-c08-common-neighborhoods.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1.
Target: obligation:opg401-z20-extension. Root: obligation:opg401-root.
Fresh cycle base: 19f2a1d50ccfd55d79ca291bb248022daef95e36.

## 1. Explicit generalization of the local target

Use Z20, shortest circular distance delta and A(a)=a+{7,...,13}
from c01. For a NONEMPTY set C of colors, define
D(C)=max{delta(a,b): a,b in C}.
Repeated entries of a neighbor-color list may be removed; they do
not change the common allowed-color set. A singleton has D=0.

Claim H1 (claim:opg401-c08-common-cardinality):
  |intersection over a in C of A(a)| = max(0,7-D(C)).
In particular the whole family has nonempty intersection exactly
when every pair of centers has circular distance at most six.

Claim H2 (claim:opg401-c08-two-color-certificate):
there exist a,b in C, possibly equal, such that
  intersection over c in C of A(c) = A(a) intersect A(b).
If the full intersection is empty, two incompatible centers certify
that failure; if it is nonempty, two extreme centers determine it.

This strengthens the two-center result but concerns only a fixed
collection of colors. It does not change the root ProblemContract
and is not a claim that arbitrary graph-coloring constraints are
globally solved by pairwise tests.

## 2. Clustering proof: the wraparound obstruction is absent

If D(C)>=7, choose a,b attaining D. By c01 their allowed sets are
disjoint, so H1 and the empty-intersection part of H2 follow.

Now suppose D(C)<=6. Translate a chosen center to zero.
Each center has a unique integer lift in [-6,6], because its
distance from zero is at most six and 12<20.
Let the minimum lift be -c and the maximum lift be b, with
0<=b,c<=6; zero is one of the lifts.

For the extreme centers, the clockwise separation is b+c<=12.
Their circular distance is min(b+c,20-b-c)<=6.
The alternative 20-b-c<=6 would require b+c>=14, impossible.
Therefore b+c<=6.

Thus all centers lie in one ordinary lifted interval [-c,b] of
span h=b+c<=6. All pairwise differences have magnitude at most
h<10, so D(C)=h: the two extrema attain the diameter without wrapping.
After a second translation, all lifted centers lie in [0,h],
and both zero and h occur.

For a lifted center t in [0,h], A(t)=[7+t,13+t], with no wrap
because 13+h<=19. Intersecting all these intervals gives
  [7+h,13].
Its cardinality is 7-h=7-D(C), proving H1.
The two intervals at t=0,h already have exactly this intersection;
all intervening intervals contain it. Translating back proves H2.

The proof uses the strict numerical separation 12<14. Without it,
pairwise close centers could wind around the circle instead of
lying in one short interval.

## 3. Exact vertex-extension consequence, including degree zero

Let G be a finite simple graph and let a fixed (20,7)-coloring of
G-v be given. Let C be the set of colors on the neighbors of v.

If v has no neighbors, every one of the twenty colors is available.
This is an empty intersection of constraints; D(C) is not defined,
and the nonempty-family formula must not be applied.

If v has at least one neighbor, H1 gives exactly
  max(0,7-D(C))
extensions, with every old color preserved.
Extension is possible exactly when all pairs of neighbor colors
are at distance at most six. In the subcubic case this covers the
one-, two- and three-neighbor cases without a missing triple test.

For a degree-three vertex, one of its three pairwise allowed-set
intersections equals the full triple intersection. The determining
pair can depend on the coloring. H2 does NOT authorize removing a
particular incident edge before the colors are known.

For example, in the three-leaf star, leaf colors 0,0,10 give an
empty full intersection, whereas the first two leaves alone permit
seven colors. Dropping the third fixed constraint would be wrong.
The star itself is colorable after changing its leaf colors.

In a hypothetical vertex-minimal obstruction in the frozen class,
every coloring of G-v must therefore exhibit two neighbor colors
at distance at least seven. This is a necessary condition only;
the pair may vary with the deletion coloring.

Atomic claim: claim:opg401-c08-vertex-extension.

## 4. Parameter generalization with a sharp boundary

Here is an explicitly stronger parameter statement, not a change to
the problem's fixed (20,7) parameters.

Let integers p,q satisfy 2q<=p<3q, with q>0.
Put k=p-2q, so k>=0 and 3k<p. On Z_p define
A_pq(a)=a+{q,q+1,...,p-q}, and let delta_p be shortest distance.
For every nonempty center set C, put D_p=max(delta_p(a,b)).
Then
  |intersection over a in C of A_pq(a)| = max(0,k+1-D_p).

Pair case: two allowed sets meet exactly when their center difference
is represented by an integer in [-k,k]. Indeed the interval of
allowed increments has difference set [-k,k]. Since 2k<p, these
representatives are distinct modulo p. This is equivalent to
delta_p<=k, with multiplicity k+1-delta_p.

For a family with all pair distances at most k, translate one center
to zero and use unique lifts in [-k,k]. If the extreme lifts have
span h<=2k, their shortest distance is min(h,p-h)<=k.
The wrapped alternative h>=p-k is impossible because p-k>2k.
Thus h<=k. Translate the extremes to zero and h.
The intervals [q+t,p-q+t], 0<=t<=h, do not wrap:
p-q+h<=p-q+k=2p-3q<p.
Their intersection is [q+h,p-q], of size k+1-h.
If a pair distance exceeds k, the pair case makes the full
intersection empty. This proves the formula in both cases.

The strict upper bound p<3q cannot simply be replaced by p<=3q.
At p=18,q=6 take centers 0,6,12. Their allowed sets are
A(0)={6,...,12},
A(6)={12,...,17,0},
A(12)={0,...,6}.
Every pair intersects in one endpoint, but all three have empty
intersection. Here k=6 and D_p=6, so the extrapolated cardinal
formula would incorrectly predict one.
This is a counterexample to that proposed parameter extension,
not to the frozen (20,7) graph problem.

Atomic claim: claim:opg401-c08-parameter-range.

## 5. Reproduction, sources, and checkpoint

Check the signed-lift argument, the extreme-pair witness, the
nonwrapping interval endpoints, and the empty-family exception.
The proof is finite combinatorics, not an executed enumeration.
No graph search, solver, theorem prover or receipt is reported.

The main generated input is
research/artifacts/candidates/opg401-a01-c01-local-extension.md
at this cycle base. The finite graph-extension bridge in c07 is a
not-executed formalization plan; it is not a verification premise.
No external Helly theorem is used without proof, and no novelty
claim is made for this intersection property.

best_verified_result: none. best_verified_candidate: none.
Best generated local family: c01 and this c08; other graph
consequences retain their explicit dependencies.
Open obligations: obligation:opg401-z20-extension; obligation:opg401-root.
Registered failed-route IDs checked: [].
Discarded strengthening: the same formula at ratio three, with the
explicit (18,6) three-center witness above.
Current route remains active.
Next action: use the three-neighbor criterion to classify the exact
outside-color obstruction of the K2,3 configuration and identify
which degree patterns or repeated boundary colors force extension.
