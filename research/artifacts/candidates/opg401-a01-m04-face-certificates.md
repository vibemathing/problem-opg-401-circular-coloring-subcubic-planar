# Exact face-extension certificates from bounded difference constraints

Status: candidate_only. Primary owner: math-derivation.
Candidate: candidate:opg401-a01-m04-face-certificates.
Problem: problem:opg-401-circular-coloring-subcubic-planar.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1.
Target: obligation:opg401-root.
Local dependency remains open: obligation:opg401-z20-extension.
Cycle base: dd58ab97b504c3e594b7c016fdd13d3c47c0819a.

## 1. A frozen boundary problem, not a global coloring assumption

Consider distinct branch vertices v_0,...,v_(n-1), n>=3, joined
cyclically by internally disjoint paths of lengths w_i in {1,2,3}.
Every internal path vertex has degree two. Each branch vertex has
exactly one outside neighbor, whose fixed color is t_i in Z20.
There are no other edges within the deleted region. All outside
vertices are already properly (20,7)-colored and remain unchanged.
Outside neighbors may coincide, in which case their t_i coincide.

The question is whether this specified coloring extends over the
region. The cycle may be a face, but the algebra itself does not
need planarity. It does NOT assert that every possible boundary
extends, or that every coloring of the deletion is favorable.

Write [z]20 for the representative in 0..19 and
  d_i=[t_(i+1)-t_i]20,
with cyclic indices. The possible branch colors have the unique
forms
  y_i=[t_i+7+s_i]20, with integers 0<=s_i<=6.              (1.1)

The three path endpoint relations from c01/c03 are:
R1: directed residue in {7,...,13};
R2: shortest distance at most six;
R3: directed residue nonzero.
Once these endpoint relations hold, the internal paths can be
filled separately, respecting every outside edge by (1.1).

## 2. The modular problem splits into tiny integer interval systems

Put z_i=s_(i+1)-s_i, which lies in [-6,6].
The raw integer d_i+z_i lies in [-6,25].

For w_i=1, the only translate of [7,13] modulo twenty meeting
[-6,25] is [7,13] itself. Thus the allowed z_i form
  D_i=[-6,6] intersect [7-d_i,13-d_i].                    (2.1)

For w_i=2, the allowed raw integers lie in [-6,6] or [14,26].
Consequently
  D_i=([-6,6] intersect [-6-d_i,6-d_i])
       union ([-6,6] intersect [14-d_i,26-d_i]).          (2.2)

For w_i=3, remove exactly the raw multiples zero and twenty:
  D_i={z in [-6,6]: z!=-d_i and z!=20-d_i}.              (2.3)
The two removed integers differ by twenty, so at most one lies
in [-6,6]. Hence (2.3) is a union of at most two integer intervals.

Discard empty intervals. Every weight-one edge has at most one
interval choice; every longer thread has at most two. Choose one
nonempty interval [l_i,u_i] for each edge. The resulting system is
  0<=s_i<=6,  l_i<=s_(i+1)-s_i<=u_i for all i.           (2.4)

Claim D1 (claim:opg401-m04-interval-split):
the original fixed-boundary extension exists if and only if at
least one of these interval systems has an integer solution.
No convex hull of disconnected D_i is substituted for D_i.

This follows in both directions from (1.1), the exact raw-integer
ranges, and the short-path relations. If D_i is empty for any i,
the boundary is immediately impossible.

## 3. A complete feasibility lemma with a short proof

Let arbitrary integer intervals [l_i,u_i], l_i<=u_i, be assigned
to the cyclic differences of n>=3 variables constrained to [0,6].
A proper cyclic segment consists of k consecutive edges with
1<=k<=n-1, in the chosen forward cyclic order.

Claim D2 (claim:opg401-m04-difference-criterion):
system (2.4) has an integer solution if and only if
  sum_i l_i <= 0 <= sum_i u_i,                           (3.1)
and for EVERY proper cyclic segment J,
  sum_(i in J) l_i <= 6,  sum_(i in J) u_i >= -6.        (3.2)

Necessity is telescoping. Around the full cycle the difference
sum is zero; along a proper segment its endpoint difference is
between -6 and 6. No relaxation or approximation is used.

For sufficiency construct a directed graph on the variables and
a new reference vertex o. An arc x->y of weight c represents
the upper bound s_y<=s_x+c. Include
  i -> i+1 with weight u_i,
  i+1 -> i with weight -l_i,
  o -> i with weight 6, and i -> o with weight 0.

Every directed simple cycle not using o is either a two-edge
return of weight u_i-l_i>=0, or an entire tour of the cycle
in one direction. The two tour weights are sum u_i and -sum l_i,
nonnegative by (3.1).

A directed simple cycle using o is either o-i-o of weight six,
or o-i followed by a simple path in the ordinary cycle and then
j-o. Such a path is a proper monotone segment in one direction.
Its full cycle weight is 6+sum_J u_i or 6-sum_J l_i,
nonnegative by (3.2). These exhaust the simple cycles.
Any negative closed walk would contain a negative simple cycle
by repeatedly splitting at repeated vertices. Thus none exists.

Let s_i be the minimum weight of a directed o-to-i path.
The minimum exists among finitely many simple paths: removing
a closed subwalk never increases weight. These distances are
integers. The direct arcs give s_i<=6. A negative o-to-i path
followed by the zero-weight i-to-o arc would be a negative
closed walk, so s_i>=0.
Appending any constraint arc, and removing any repetitions,
proves the corresponding upper bound on the distances.
The distances therefore solve all of (2.4), proving sufficiency.

This proof supplies the feasibility theorem here; an algorithm
name or an external solver verdict is not used as a premise.

## 4. Exact closed forms for all-cubic four- and five-faces

Suppose all w_i=1. Before intersecting with [-6,6], the difference
bounds are l_i=7-d_i and u_i=13-d_i. The variable bounds already
force differences into [-6,6], so these untruncated bounds give
the same system. They satisfy l_i<=u_i automatically.

Let D=sum_i d_i; it is a multiple of twenty by telescoping modulo
twenty. D2 becomes exactly
  7n<=D<=13n,
and, for every proper k-edge segment J,
  7k-6 <= sum_J d_i <= 13k+6.                            (4.1)

Claim D3 (claim:opg401-m04-cubic-four-face):
for n=4, extension is equivalent to
  D=40,
  1<=d_i<=19 for every i,
  8<=d_i+d_(i+1)<=32 for every i.                        (4.2)

Indeed the full bounds allow only the multiple 40.
The k=1 and k=2 cases are exactly the two displayed local bounds.
For k=3, the sum is 40-d_i in [21,39], automatically within
[15,45]. This proves necessity and sufficiency, not just a filter.

Claim D4 (claim:opg401-m04-cubic-five-face):
for n=5, extension is equivalent to ONE of these two cases:

Case A:
  D=40; every d_i in [1,18];
  every d_i+d_(i+1) in [8,25].

Case B:
  D=60; every d_i in [2,19];
  every d_i+d_(i+1) in [15,32].                          (4.3)

The full bounds allow only D=40 or 60.
The k=1 case gives d_i in [1,19]. The k=4 case, applied to the
complement of a single edge, intersects this with
[D-58,D-22], producing the stated single-edge ranges.
The k=2 case gives adjacent sums in [8,32]. The complementary
k=3 case intersects this with [D-45,D-15], producing precisely
the stated adjacent-sum ranges.
All proper segments have now been included.

Reflection of the colors exchanges these two feasible cases:
all their d_i are nonzero, so d_i becomes 20-d_i and D becomes
100-D. Translation leaves the d_i unchanged.
One must not use reflection to discard a nonzero-residue condition
at a boundary where consecutive colors happen to coincide.

## 5. Certificates for the whole unavoidable family

Every one of m03's thirteen patterns has at most two weights
different from one. Thus D1 has at most four interval systems.
This statement includes 113 and 122 triangles, not just the
four- and five-branch cases.

A positive certificate consists of:
- the chosen interval for each edge;
- integers s_0,...,s_(n-1) in [0,6] satisfying all edge bounds;
- a short-path filling for each internal thread, if present.

A direct check reconstructs the branch colors by (1.1).
For a two-edge path use the common allowed-color set from c01.
For a three-edge path take its nonzero endpoint difference,
represent it in [21,39], and split that integer into three
summands in [7,13]. This constructs every missing vertex color.

A negative certificate is either an empty D_i, or, for each of
the at most four interval choices, one violated total inequality
in (3.1) or one violated segment inequality in (3.2).
The checker verifies the interval decomposition covers D_i and
checks each displayed integer sum. No unbounded search or
unrecorded coloring enumeration is needed.

Claim D5 (claim:opg401-m04-thirteen-type-certificates):
each fixed boundary on one of the thirteen unavoidable types
has a complete certificate of one of these two forms.
This is a proved certificate format and finite decision method,
not a report that software has generated or verified certificates
for any collection of graphs.

For use on m03's actual core faces, there is no hidden chord.
A facial cycle in a three-connected plane graph is induced:
a chord must lie outside the empty face; together with the two
facial arcs it separates their nonempty interiors after its two
ends are removed, giving a two-vertex cut. Thus no such chord
exists. In the original graph this also excludes an external
thread between two branch vertices of that face. Every branch
vertex therefore has exactly the one outside incidence required
in Section 1. Repeated outside neighbors remain allowed.

## 6. Explicit attacks and hand-checkable certificates

Correct total winding alone is insufficient for a four-face.
Take cyclic outside colors (0,1,0,19). Then
  (d_0,d_1,d_2,d_3)=(1,19,19,1), D=40.
Every consecutive pair of outside colors is distinct, but
d_1+d_2=38>32. This two-edge segment is a negative certificate.
The complementary adjacent sum is 2<8 as a second witness.

For outside colors (0,1,0,1), choose offsets (0,6,0,6).
The inner four-cycle colors are (7,14,7,14), and every inner
edge has shortest distance seven. All four outside incidences
have differences seven or thirteen. This is a positive certificate.

For a five-face take t=(10,18,6,14,2). All d_i=8, so Case A holds.
Constant offsets s_i=3 give inner colors (0,8,16,4,12).
Reflection gives a Case B example with all d_i=12.
These are displayed arithmetic checks, not program output.

Convexifying a disconnected difference set is invalid:
for a length-two thread with d_i=10, formula (2.2) gives
[-6,-4] union [4,6]. Its convex hull would wrongly allow zero,
which leaves antipodal endpoint colors at distance ten.
For a length-three thread with d_i=0, formula (2.3) excludes
zero; filling the gap would falsely permit equal endpoints.

All examples can be realized by cycles with pendant outside
vertices, whose deletion coloring is proper. Their bad boundary
assignments do not prove those graphs uncolorable.
The graph-class question still requires obtaining a favorable
boundary coloring, or proving a larger reducible configuration.

## 7. Scope, reproduction, and checkpoint

No mathematical enumerator, SAT solver, proof assistant, or
external mathematical runtime was executed for this candidate.
The integer systems, closed forms and certificate examples have
the full hand derivations above. A future bounded implementation
may evaluate them exactly; a successful implementation run would
still not by itself create an EvidenceLink or close the root.

Generated inputs at the cycle base: c01 and c03 for path relations,
m03 for the thirteen-type unavoidable family. No prior-art or
novelty claim is made for difference constraints. The complete
needed feasibility proof was included to avoid an unchecked
appeal to an algorithm or theorem with different hypotheses.

best_verified_result: none. best_verified_candidate: none.
Open obligations: obligation:opg401-root; obligation:opg401-z20-extension.
Registered failed-route IDs checked: [].
Failed shortcut proposed for the ledger: correct four-face total
winding and unequal adjacent outside colors alone imply extension.
The explicit (0,1,0,19) boundary is its counterexample.
The certifying interval route itself remains active.

Next action: use m03's cut restrictions and m02's rigid external
pair to show where a 122 face can receive its required charge,
then apply these certificates to the resulting cubic-pentagon
clusters instead of assuming every isolated short face reduces.
Requested future verification: kernel_check, axiom_escape_audit,
statement_faithfulness, with verifier-policy suitability checked
by the trusted process. No receipt or admission is supplied here.
