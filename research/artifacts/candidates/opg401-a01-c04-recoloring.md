# Bounded recoloring and a pentagon reduction: candidate c04

Status: candidate_only. Primary owner: math-derivation.
Candidate: candidate:opg401-a01-c04-recoloring.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1.
Target: obligation:opg401-z20-extension. Root: obligation:opg401-root.
Fresh cycle base: d3a2ca42cb71dc61d995d2b2772e064f2ad8bece.

## 1. Exact scope of allowed changes

Let v be degree two in a graph of the frozen class, with neighbors u,w.
Fix a (20,7)-coloring of G-v. We may recolor u,w and color v, but hold
every vertex outside {u,v,w} fixed. Triangle-freeness ensures uw is
not an edge. Let I and J be the available-color sets at u,w, computed
from their other, fixed neighbors. Their old colors show I,J nonempty.

Since each has at most two fixed neighbors, c01 implies each list is
either Z20, a seven-element cyclic interval, or a nonempty cyclic
interval of length at most seven. Two list choices are compatible
independently because uw is absent; shared fixed neighbors cause no
additional edge between the choices.

All distances and allowed sets use the c01 convention:
delta is shortest circular distance, A(a)=a+{7,...,13}.
The generated claims below refine local extension; they do not
establish graph-class colorability.

## 2. Complete two-list repair criterion

For a nonempty list I define
B(I)={y in Z20: delta(x,y)>=7 for every x in I}.
Then a recoloring of the allowed region exists exactly when
  J is not a subset of B(I).                              (R1)
Indeed a successful pair x in I,y in J must have delta(x,y)<=6
by c01, and this is exactly the negation of that subset condition.
Once such a pair is chosen, c01 explicitly supplies the color of v.
If I=Z20, B(I) is empty because the test x=y fails.

For a cyclic interval I=s+{0,...,m-1}, 1<=m<=7, translating s to zero
gives
  B(I)=s+{m+6,...,13},  |B(I)|=8-m.                       (R2)
Proof: B(I) is the intersection of A(s),...,A(s+m-1).
In translated representatives these are [7+i,13+i], 0<=i<m;
none wraps, and their intersection is [m+6,13].

Normalize I={0,...,m-1} and write J={r,...,r+n-1} modulo 20,
where 1<=n<=7 and r is its first cyclic element. Repair fails exactly
when
  m+6 <= r <= 14-n
in the fixed representatives 0,...,19. These bounds force J not to wrap.
Thus for fixed m,n there are max(0,9-m-n) bad relative start positions.
In particular,
  |I|+|J|>=9 guarantees repair.                           (R3)
This also holds if one list is Z20.

The threshold nine is sharp even for actual available lists in the
contract class. Take the seven-vertex tree with edges
vu,vw,ux1,ux2,wy1,wy2. Fix leaf colors
x1=10,x2=13,y1=0,y2=3.
Then I=A(10) intersect A(13)={0,1,2,3} and
J=A(0) intersect A(3)={10,11,12,13}.
A coloring of G-v exists, for example u=0,w=10.
Every choice from I and J has distance at least seven, so this fixed
outside coloring cannot be repaired in {u,v,w}, despite |I|+|J|=8.
The tree itself is colorable using 0 and 10 after changing its leaves;
this is not a counterexample to the frozen ProblemContract.

Atomic IDs: claim:opg401-c04-list-repair and
claim:opg401-c04-sharp-threshold.

## 3. Necessary signatures in a minimal obstruction

Assume G is vertex-minimal among non-(20,7)-colorable graphs of the
contract class. At a degree-two v whose neighbors both have degree
three, let t_u,t_w be the color distances between their respective
pairs of fixed outside neighbors in any coloring of G-v.
Each lies in [0,6], since the old endpoint color belongs to its list.
The list sizes are 7-t_u and 7-t_w. R3 therefore implies
  t_u+t_w>=6
in every such deletion coloring. This scalar constraint is necessary,
not sufficient for failure; the exact relative-position test R1-R2
is stronger.

Now consider a path a-u-v-b with u,v of degree two.
The endpoints a,b are distinct, because equality would give a triangle.
For any coloring of H=G-{u,v}, the c03 length-three result forces
phi(a)=phi(b)=c; otherwise the coloring extends immediately.
If the available list at a, with all other H colors fixed, contained
a color different from c, recoloring a alone and using c03 would
extend. Thus that list is the singleton {c}, and the same holds at b.
Since a,b each have at most two neighbors in H, they must have exactly
two, so both have degree three in G.
The c01 singleton characterization forces each outside-neighbor
color pair to be exactly
  {c+7,c+13} modulo 20.                                   (R4)
Conversely these two colors have allowed-set intersection {c}.
This describes necessary rigidity of a blocked deletion coloring,
not a claim that the deletion coloring is unique.

Atomic ID: claim:opg401-c04-pinning.
Dependencies: c01 interval counts, c03 length-three criterion, and
the explicitly stated hypothetical minimality.

## 4. Five-cycles with three degree-two vertices are reducible

Claim R5 (claim:opg401-c04-pentagon-reduction):
a vertex-minimal obstruction contains no five-cycle with at least
three degree-two vertices.

If three such vertices are consecutive, use c03's four-edge extension
(including its closed-endpoint exception). Otherwise the only cyclic
pattern has exactly three degree-two vertices. Name the cycle
a-u-v-b-z-a, with u,v,z of degree two and a,b of degree three.
A five-cycle is chordless in a triangle-free graph: every possible
chord creates a triangle.

Delete u,v and take a coloring of the smaller graph H.
If phi(a)!=phi(b), extend along the three-edge path by c03.
Otherwise write phi(a)=phi(b)=c.
Because z has only the two neighbors a,b, recolor it to c+10.
Both of its incident edges stay legal.

Vertex b has two neighbors left in H: z and an outside vertex q.
Its old color c is still legal after this recoloring, and
phi(q) belongs to c+{7,...,13}.
The distance between c+10 and phi(q) is at most three.
By c01, the available list at b now has size at least four.
Choose a new color for b different from c from this list.
Its edges to z and q stay legal; a is unchanged and there is no edge ab.
Now a,b are distinct in color, so color u,v using c03.

Every changed edge has been checked: za,zb,bq and the restored path
a-u-v-b. No other edge touches u,v,z, and b's only other neighbor q
was held fixed. This supplies a valid reducibility argument, not an
unsupported universal fixed-boundary extension.

## 5. Attacks and scope limits

The tree above shows R3 cannot be weakened to a size sum of eight.
R4 is only a necessary rigidity signature; it is not a contradiction
without a permitted recoloring or additional graph information.
R5 does not exclude five-cycles with exactly two degree-two vertices.
In that remaining case z may have a third fixed neighbor and need
not be freely recolorable to c+10.

A failure of R1 excludes only recolorings in the stated three-vertex
region with the outside colors fixed. It does not imply that no larger
recoloring or different deletion coloring could succeed.
Shared outside neighbors are allowed and were not silently assumed
distinct. Where q occurs in the pentagon proof, chordlessness and
the degree assumptions place it outside the cycle.

## 6. Reproduction and checkpoint

Derive R2 by interval intersection, check the bad-start inequalities,
and verify all six tree edges against the listed colors.
For R5, inspect the two cyclic patterns and each changed edge.
All mathematics is hand-derived. No graph enumeration, kernel check,
solver result, or verifier receipt is reported.

Sources at the cycle base: the frozen contract and target;
research/artifacts/candidates/opg401-a01-c01-local-extension.md;
research/artifacts/candidates/opg401-a01-c03-path-sumsets.md.
The source/definition comparison remains
research/artifacts/source-notes/opg401-a01-c01-definition-sources.md.
No new external theorem or novelty claim is a premise.

best_verified_result: none. best_verified_candidate: none.
Best generated material: c01-c04.
Open obligations: obligation:opg401-z20-extension; obligation:opg401-root.
Registered failed-route IDs checked: [].
Discarded strengthening: list-size sum eight would always permit repair.
Route remains active, with no global conclusion.
Next action: exactly classify the three outside-color obstructions for
a five-cycle with precisely two adjacent degree-two vertices, retaining
the outside-color quantifiers rather than claiming unconditional
reducibility of that remaining configuration.
Requested future capabilities: kernel_check, axiom_escape_audit,
statement_faithfulness. The current artifacts are not those receipts.
