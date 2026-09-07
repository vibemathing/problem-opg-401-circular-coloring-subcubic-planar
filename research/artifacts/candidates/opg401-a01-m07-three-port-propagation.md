# Three-port propagation and exclusion of repeated carrier terminals

Status: candidate_only. Primary owner: math-derivation.
Candidate: candidate:opg401-a01-m07-three-port-propagation.
Problem: problem:opg-401-circular-coloring-subcubic-planar.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1.
Target: obligation:opg401-root.
Local dependency remains open: obligation:opg401-z20-extension.
Cycle base: 5ba9f89a5c5272fd78e3e6e7a8a13e22d0bf0c42.

## 1. An explicit three-color forbidden relation

Use shortest distance delta on Z20 and A(t)=t+{7,...,13}.
Define a relation B(t,r,s) by translating/reflecting r to zero
and s to h=delta(r,s), transforming t by the same coordinates:

| h | t for which B holds |
|---|---|
| 0 | all twenty colors |
| 1 | {7,8,9} |
| 2 | {8,9} |
| 3..10 | none |

At h=0 the choice of reflection is irrelevant; at h=10 the row
is empty. Thus the definition is well-defined and invariant under
common translations and reflection.

In particular, B cannot hold if
  r!=s and delta(t,r)<=6.                               (1.1)
It also cannot hold with r!=s and t=r or t=s.

This is a finite relation, not an assertion that every graph
boundary can attain colors outside it.

## 2. A boundary property that survives absorption of an edge

Suppose a connected induced region Z has exactly three edges to
its complement. Label their outside endpoints T,R,S and their
inside endpoints z_t,z_r,z_s, respectively. The inside endpoints
are distinct, and z_r,z_s are adjacent. Assume:

(P) for every fixed coloring of the complement whose boundary
colors (t,r,s) do NOT satisfy B, that coloring extends over Z.

It suffices that the internal region has the stronger purely
local property that every such triple extends, with all outside
edges satisfied. We use this local formulation throughout the
propagation proof, so the property is not restricted to the
outside colorings of one particular ambient graph.

Let T,R,S be distinct and suppose TR is an edge. If both T,R
have degree three, their remaining neighbors, beyond their
respective edges to Z and the edge TR, are W,V. Absorb T,R into
the region. Its new outside terminals, in roles (t,r,s), are
  S,V,W,
and its new distinguished adjacent inside endpoints are R,T.

Claim P1 (claim:opg401-m07-absorption):
the enlarged region also has property (P). More precisely its
possible bad triples are contained in the smaller table

| delta(V,W), normalized V=0,W=d | bad color at S |
|---|---|
| 0 | all colors |
| 1 | {7,8} |
| 2 | {8} |
| 3..10 | none |

Here the table refers to the colors of these vertices. The new
outside endpoints may coincide; a later step handles that case.

Proof. For normalized outside colors V=0,W=d, choose the prospective
color x of R in
  A(0) intersect B_6(d),
where B_6 is the radius-six color ball. Then the possible colors y
of T form A(d) intersect A(x). By c01 these lists exactly express
the outside edges at T,R and the edge TR.

For 1<=d<=6,
  x in [7,d+6],
  y-x in [7,13+d-x].
The latter interval has length d+7-x and starts at seven.
For a fixed x, all choices y are forbidden by the old B relation
only if the color of S equals x, or if it equals x+1 AND
d+7-x<=3. The other nonzero differences allowed in B cannot
contain the starting value seven in this interval.

For d=1 this leaves colors 7,8 for S. For d=2, intersect the
possibilities {7,8} at x=7 and {8,9} at x=8, leaving {8}.
For d=3, the three possibilities {7,8}, {8,9}, {9,10} have
empty intersection. For d=4, x=7 permits only S=7 while x=8
permits S=8 or 9, already disjoint. For d=5,6, x=7 and x=8
each have at least four y choices, so force distinct equalities
S=7 and S=8 if all choices are forbidden.

For 7<=d<=10, both x=7 and x=8 are permitted, and their y lists
have at least four colors. When S!=x the old B relation forbids
at most three y colors. Thus these two choices again cannot
both fail. At d=0, A(0) intersect B_6(0) is empty, which is
included in the first bad row.

Whenever a choice is not forbidden, color T,R by y,x and use (P)
for the old region. This proves the smaller table and (P), since
that table is contained in B. All coordinate inversions preserve
the unchanged actual outside colors.

If T or R has degree two rather than three, the corresponding
new outside constraint is absent. Give this missing constraint
an auxiliary color chosen at distance at least three from the
other new outside color; if both are absent choose two colors
at distance three. The proved table then supplies an extension
for every actual color at S. These auxiliary colors impose
stronger local requirements and do not add vertices or edges
to the graph being colored.

## 3. Termination gives a genuine reducibility theorem

Claim P2 (claim:opg401-m07-three-port-reduction):
a minimum-order obstruction G in the frozen graph class cannot
contain a connected induced region of at least three vertices
with exactly the three boundary edges and property (P) above.

Choose, among all such regions in G, one of maximum vertex order.
This maximum exists because G is finite. Write H=G-Z.

The outside vertices R,S cannot be equal: their two incidences
and the inside edge z_r z_s would create a triangle.

If T=R or T=S, replace Z by a three-edge path between R and S,
using two new vertices. This is planar: contracting a spanning
tree of the connected region gives the two-terminal star after
parallel-edge suppression, then subdividing gives the path.
It creates no triangle, including when RS is already an edge.
Each outside degree increases by at most the number of removed
incidences. The replacement is a smaller member of the class.
Its coloring gives r!=s, while t=r or t=s, so (1.1) and the table
supply a lift to G, a contradiction.

Now T,R,S are distinct. If TR is absent, replace Z by two new
vertices X,Y and the edges
  TX, RX, XY, YS.
This is obtained from the three-terminal star by subdividing
its S-edge; the star itself comes from contracting the connected
region. It is therefore planar. The only possible new triangle
would use the absent edge TR. The degree bound is preserved.
It is smaller because |Z|>=3.

A coloring of this replacement has delta(t,r)<=6, since t,r
have common allowed color at X, and r!=s, since R-X-Y-S has
three edges. Thus (1.1) holds and the coloring lifts through
property (P), another contradiction.

It remains that TR is present. Each of T,R has degree two or
three: its region incidence and TR are distinct edges, and the
ambient maximum degree is three. If either has degree two,
P1's missing-constraint case extends any coloring of the smaller
deletion of Z union {T,R}, again contradicting G's choice.
If both have degree three, P1 makes Z union {T,R} a larger
connected induced region with the same property and exactly
three boundary edges. Its new distinguished inside endpoints
are the adjacent T,R, and the third inside endpoint is the old
z_s. The old S stays outside, so this region is still proper.
This contradicts maximality.

There are no other incidences to audit: the old region had
exactly three boundary edges, and T,R,S were distinct before
absorption. The remaining neighbors W,V cannot lie inside the
old region, or there would already be another boundary edge.
If new terminal identifications occur, they are precisely the
cases handled at the start of the next maximality argument.
This proves P2. It is finite graph descent, not an unbounded
computation or a presumption of favorable fixed boundary colors.

## 4. The repeated-terminal nine-vertex region has property (P)

Take the single-ear carrier from m06: b-c-d-e-f-b together with
a-u-b-c-v-a. Suppose the outside neighbors of a and d coincide
at a vertex P. Include P in the region. The third neighbor of P
is T; the outside neighbors of e,f are R,S. Write their colors
as t,r,s. The only boundary edges of this nine-vertex region are
PT,eR,fS, and its distinguished inside endpoints e,f are adjacent.

Claim P3 (claim:opg401-m07-nine-vertex-boundary):
its exact bad relation is B(t,r,s).

Let x be the color of P and D,E,F those of d,e,f. Because P is
adjacent to both T and d, a choice for P exists exactly when
delta(t,D)<=6. In the remaining 122 ear the outside colors are
x,F,D. If D=F it fails; if delta(D,F)=1 it also fails, since
x is adjacent to D and thus belongs to the bad arc A(D) union
A(F) of m02. If delta(D,F)>=2 it extends for every x.

Consequently the exact question is whether some E in A(r) has
  D in A(E) intersect B_6(t),
  F in A(E) intersect A(s), with delta(D,F)>=2.           (4.1)

Normalize r=0,s=h. For h=0 there is no possible E: the adjacent
e,f would both have colors in the span-six interval A(0).
For h>=1 the possible central colors are
  E in [7,min(13,h+6)].

For a fixed E in this interval, translate E to zero. If t=E,
the first list in (4.1) is empty. If t-E=j with 1<=j<=6,
that list is the prefix [7,6+j] of A(0); for t-E=-j it is
the suffix [14-j,13]. At greater distance it is all of A(0).
The second nonempty list is a prefix or suffix of A(0).

A prefix or suffix of length at least three in the first list
always has a member at distance at least two from some member
of the second. For length three the only common radius-one
point would be an interior singleton, which the second list
cannot be; for longer lengths even that point is impossible.

For lengths one or two, failure occurs exactly when
  t-E in {1,2} and s-E in {-6,-5},
or
  t-E in {-2,-1} and s-E in {5,6}.
In the normalized ranges E>=7 and h<=10, the second alternative
cannot occur because h-E<=3. Thus the bad t for a fixed E are
{E}, augmented by {E+1,E+2} only when E=h+5 or E=h+6.

At h=1 there is only E=7, leaving t=7,8,9.
At h=2 the two forbidden sets are {7,8,9} and {8,9,10},
whose intersection is {8,9}.
At h=3, E=7 requires t=7 whereas E=8 requires t in {8,9,10}.
For h>=4, E=7 and E=8 each require their distinct singleton t.
Thus no bad t remains. This proves precisely B in both directions.

In particular there are 20*(20+2*3+2*2)=600 bad ordered triples
out of 8000, as arithmetic derived from the table, not a claimed
enumeration result. Every good triple supplies the colors in
(4.1), then P and then the ear.

## 5. All four outside vertices of a single-ear carrier are distinct

Claim P4 (claim:opg401-m07-distinct-carrier-terminals):
in a minimum obstruction, the outside neighbors alpha,delta0,
epsilon,phi0 of a,d,e,f in the single-ear carrier are pairwise
distinct.

The equalities delta0=epsilon or epsilon=phi0 would create a
triangle with de or ef, respectively.
If delta0=phi0=W, there is the four-cycle d-e-f-W-d.
Degree two at W is excluded by m01's four-cycle restriction.
Otherwise it is an all-cubic four-cycle and hence facial by m05.
But the carrier pentagon is also facial and these two different
faces would both use the pair ed,ef at the degree-three vertex e.
Only one face corner can use that pair without the third edge;
this is impossible. Thus delta0!=phi0.

If alpha=epsilon, use the smaller five-cycle replacement J from
m06. It is a smaller member of the class and has a coloring.
Its induced boundary has p=r. None of m06's four additional
bad rows allows p=r, and its basic bad rows cannot occur in a
coloring of J. Hence the original carrier would extend, a
contradiction.

Suppose alpha=delta0=P. The vertex P has degree three: a already
has degree-two neighbors u,v and cannot have a third degree-two
neighbor by m01. Its third neighbor T lies outside the carrier:
all other possible region vertices are saturated, an edge Pe
would make triangle Pde, and an edge Pf would give the already
excluded delta0=phi0. The other outside neighbors R=epsilon,
S=phi0 are distinct and lie outside these nine vertices.
Thus this is exactly P3's connected induced nine-vertex region,
with three boundary edges and property (P). Apply P2 to exclude it.

Reflecting the carrier interchanges d,f and gives the same
argument for alpha=phi0. All possible equalities have now been
excluded. This proves P4, not just distinctness of color values.

## 6. Consequence for the next replacement, and boundaries

Since the four outside vertices are distinct, adding the edge
alpha-U to m06's five-cycle replacement is class-preserving.
The only potential new triangle would require alpha=delta0,
which P4 excludes. The degree of alpha is restored by at most
the incidence it lost; U goes from degree two to three.
The edge can be drawn along the unused alpha port of the deleted
two-face disk. The analogous edge alpha-V is also permissible.

For every coloring of the first augmented replacement, the
four additional bad rows of m06 force phi(alpha)=phi(V).
Indeed D,F are consecutive. Their three-edge path D-U-V-F has
unique increments, all seven or all thirteen. The bad alpha
arc is A(D) union A(F); its intersection with A(U) is exactly
{phi(V)}. For the other augmented replacement the analogous
forced equality is phi(alpha)=phi(U).

These are candidate reductions to forced-equality problems,
not a claim that such equalities are already impossible.
The two augmented graphs need not have the same coloring, and
their coloring constraints cannot be silently combined.

The absorption proof likewise never assumes that every fixed
outside coloring extends: it uses smaller replacement graphs
to obtain an admissible coloring, or enlarges a region with an
explicit invariant. No command, enumerator, solver, compiler,
or mathematical verifier ran. Only text preparation and hashing
were used for transportation.

Generated inputs at the cycle base: c01, c03, m01, m02, m05,
m06. The three-port table and termination proof are written
out above. No external novelty or theorem-reuse claim is made.

best_verified_result: none. best_verified_candidate: none.
Open obligations: obligation:opg401-root; obligation:opg401-z20-extension.
Registered failed-route IDs last checked: [].
Previous failed-route proposals remain proposals, not ledger entries.
Next action: analyze the two colorable augmented replacements and
their forced equalities without conflating their colorings; in
parallel use the three-port invariant to prune other short-face
clusters. The all-cubic four- and five-face root gap remains.
Requested future verification: kernel_check, axiom_escape_audit,
statement_faithfulness. No receipt or admission is supplied here.
