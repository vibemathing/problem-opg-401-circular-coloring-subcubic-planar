# M09 R1 audit: a pentagonal patch retracts onto its boundary

Status: RESULT_CANDIDATE_READY. Verdict: candidate_only.
Candidate: candidate:opg401-a01-v02-m09-r1-audit.
Primary owner: math-derivation.
Problem: problem:opg-401-circular-coloring-subcubic-planar.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1. Target: obligation:opg401-root.
Local dependency remains open: obligation:opg401-z20-extension.
Cycle base: 741c5a422e61a6ed0fd71952464101ef477fcda5.

## 1. Exact audited statement and dependencies

Let P be a finite connected simple triangle-free plane graph. Its outer
boundary is a simple five-cycle C, and exactly one internal face has odd
boundary-walk length. Length counts edge sides with multiplicity; a bridge
traversed twice contributes two. A plane embedding is part of this auxiliary
statement. No maximum-degree hypothesis is needed for THIS patch theorem.
The root's subcubic hypothesis is unchanged.

Audited claim R1: there exists a graph homomorphism rho:P->C with
rho(c)=c for every vertex c of C. Therefore, for EVERY target graph T and
EVERY homomorphism f:C->T, f composed with rho extends f over P.
Specializing T to the (20,7) palette preserves each prescribed boundary
color, not just boundary feasibility up to rotation.

The logical dependencies read from the repository are:
- M09 R1 in opg401-a01-m09-pentagonal-retraction-draft.md;
- D4, D2 and the potential reconstruction in
  opg401-a01-m05-dual-charge-certificates-draft.md;
- the frozen modular coloring definition and elementary plane boundary
  cancellation. The similarly numbered m05-pentagon-clusters.md is NOT
  the two-odd-face dependency.

These are generated inputs, not Evidence. Sections 2-5 provide the needed
arguments in full rather than treating a prior Candidate as a trusted premise.
The negation of R1 would be a patch meeting every hypothesis but with no
boundary-fixing homomorphism to C. No such counterexample was found here.
M09's later six-terminal claims are not audited or promoted by this note.

## 2. Recheck the existence of a (10,4)-coloring

There are exactly two odd faces, the outer face s and one internal face t.
Let H be the plane dual, retaining parallel edges. Dual loops do not belong
to cuts. Assign charges b_s=5, b_t=-5, and zero at every other face.

For any face subset U separating s,t, the primal edges corresponding to
its dual cut have even degree at every primal vertex: while turning around
that vertex, membership of successive face sectors in U changes an even
number of times. Also
  |delta_H(U)| = sum_{f in U} length(f) modulo 2,
since internal edge sides contribute twice. The cut thus has odd size.
A finite even-degree edge set decomposes into edge-disjoint cycles by
splitting closed trails. Odd total size forces an odd cycle. Simplicity
and triangle-freeness make its length at least five. Hence every s-t cut
in H has size at least five. Cuts not separating s,t have zero net charge.

Here is the required integral flow argument. Replace every non-loop dual
edge by both directed arcs, each with capacity one. Start with zero s-t
flow and augment along a residual s-t path, by the minimum residual
capacity on the path. All flows and capacities remain integers. If the
flow has value less than five but no augmenting path, vertices reachable
from s form a cut whose outgoing arcs are saturated and incoming arcs
carry zero. Its capacity equals the current value, less than five,
contradicting the cut bound. Thus an integer flow of value five is reached
in at most five unit augmentations (stop immediately at value five).
Subtract the opposite arc flows on each undirected dual edge to obtain
signed h_e in {-1,0,1} with divergence b. Put h=0 on dual loops.

Orient primal edges arbitrarily and orient each dual edge from the left
face to the right face. Interpret h in these signed coordinates. Give an
oriented primal edge the Z10 increment 5+h_e and its reverse the increment
5-h_e, its additive inverse modulo ten. Both are in {4,5,6}.
For a facial walk oriented with its face on the left, the circulation is
  5*length(f)+b_f = 0 modulo 10.
This holds on even faces with b=0 and on the two odd faces with b=+/-5.
Bridge sides cancel under reverse traversal, so they cause no exception.
Summing facial circulations on one side of a simple cycle shows that
cycle's circulation is zero. Every closed walk splits into simple cycles
and immediate backtracks, and hence also has zero circulation.

Fix a vertex and define its color as zero. Define every other color by
summing increments along any path from that vertex. Zero closed-walk
circulation gives path independence. The color difference on each edge
is its specified increment in {4,5,6}, proving a (10,4)-coloring exists.
This is an all-size hand proof with a finite constructive algorithm, not
an inference from a search over patches.

## 3. Projection: specify the target cycle labeling correctly

For i in {0,...,9}, put eta(i)=floor(i/2) in Z5, and extend the lift by
eta(i+10)=eta(i)+5 to handle wrapped differences. If j-i has directed
residue r in {4,5,6}, the projected directed residue is
  floor((i+r)/2)-floor(i/2) modulo five.
For r=4 it is two; for r=5 it is two or three according to parity of i;
for r=6 it is three. These are precisely the edges of K_(5/2), which is
a five-cycle with cyclic order 0,2,4,1,3,0.

Thus composing the (10,4)-coloring with eta gives a homomorphism
  g:P -> K_(5/2).
The unlabeled target is C5, but its numeric labels are NOT the usual
adjacency +/-1 convention. Relabeling j to 3j modulo five changes
residues two,three into +1,-1. The edge 0--4 in the source projects to
0--2; it is a direct witness against forgetting this target relabeling.

## 4. The boundary restriction must be an isomorphism

Write C=c_0...c_4c_0 in cyclic order, and relabel g's target as just above.
Each of the five boundary steps has a unique signed value +1 or -1.
Their sum is divisible by five because the walk is closed. It is odd
and lies between -5 and 5, so it can only be -5 or +5. All five steps
therefore have the same sign. The five boundary vertices have distinct
images; the five boundary edges cover the five target edges.
Consequently g restricted to C is a graph isomorphism, including an
edge-preserving inverse. There is no assertion that a general odd closed
walk has uniform signs; length five is essential.

Define, with explicit domains,
  rho = (g restricted to C)^{-1} composed with g : P -> C.
Both factors are graph homomorphisms and rho(c)=c for every c in C.
For ANY prescribed f:C->T, the map f composed with rho is a graph
homomorphism P->T and restricts exactly to f. No boundary color is changed.
This proves R1 and its preserving-extension consequence as candidates.

## 5. Corresponding reducible configuration, and no stronger conclusion

Suppose G is minimum-order among non-(20,7)-colorable graphs in the frozen
finite simple triangle-free planar subcubic class. Such a minimum exists
if any obstruction exists, because vertex orders are natural numbers.
It is connected: color each smaller component and combine otherwise.

Suppose a simple five-cycle bounds a disk containing exactly one odd face
and at least one strictly interior vertex. The subgraph P drawn in the
closed disk is connected: any interior component has a path in connected
G to the boundary, and cannot cross the boundary away from its vertices.
It meets all R1 hypotheses. Delete the strictly interior vertices. The
remaining graph retains C, is smaller and stays in the frozen graph class.
Minimality colors that graph, giving a particular boundary coloring f.
By R1, f extends across P without changing C. No edge joins a strict
interior vertex directly to an exterior vertex, by planarity. Combining
the two colorings therefore colors every edge of G, a contradiction.

This eliminates exactly that patch from a hypothetical minimal obstruction.
If the disk has no interior vertices, no chord of C is possible because
any five-cycle chord creates a triangle; the disk is a single face.
Boundary parity gives an odd number of odd faces on either side of a
separating five-cycle. If both sides contain vertices, each side must
therefore have at least three odd faces, not just one.
This does not eliminate arbitrary five-faces, general short-face clusters,
or every possible minimum obstruction, and does not prove the root.

## 6. Finite palette audit and negative controls

The actual bounded palette_check.py run inspects all 30 directed legal
source-palette edges and all 5^5=3125 maps of C5 vertices into K_(5/2).
Exactly ten are homomorphisms, all bijective; all fifty boundary inverse
identities are checked. palette-audit.json records their complete lists
and every projected edge. This supports the finite algebraic steps; it
is not an enumeration of arbitrary P or a replacement for Sections 2-5.

Three explicit negative controls are also checked:
- Treating the floor projection as a map to numerically labeled +/-1 C5
  fails on source edge 0--4, whose image is 0--2.
- On P=C5, the boundary map g(c_i)=2i+1 modulo five is a legal isomorphism
  to K_(5/2), but does not fix C's labels. Omitting its inverse would not
  prove retraction. Composing the inverse restores every boundary vertex.
- Six +1 steps and one -1 step have total five, giving a closed seven-step
  C5 walk with mixed signs. The five-step argument cannot be generalized
  merely by retaining odd length.

The run also rechecks M09's existing warning against replacing retraction
by mere (8,3)-colorability. In K_(8/3), the boundary cycle 0,3,6,1,4,0 has
fixed (20,7) colors 0,12,19,6,13. The remaining vertices are 2,5,7.
Vertex 5 must be colored 13 from neighbors colored 0 and 6; vertex 2
must then be colored 6 from neighbors colored 19 and 13; vertex 7 is
restricted by colors 12 and 13 to {0,...,5}, none adjacent to color 6.
All 20^3=8000 assignments to these three vertices were actually checked;
none extends the legal boundary. This palette witness is not a planar
root counterexample, nor is it an error in R1's stronger hypotheses.

## 7. Execution, scope and next obligation

Reproduce from this directory with python3 -I -S run.py. CPython 3.13.5,
exact integers and standard library only; child wall10s, CPU5s, address
space128MiB, file/output64KiB, one thread, zero retries. execution.json
contains the actual input/source/output and binary SHA-256, exit status
and timing. The isolated runtime smoke succeeded in V01. The repository's
missing compute_plan.py was not executed; this is bounded frontend work,
not an asserted repository execution capability or verifier adapter.
No Lean, SMT, patch enumerator or trusted mathematical verifier ran.

Hand proof invariants are integral residual capacities and flow divergence,
zero modular circulation, graph-homomorphism composition, and pointwise
boundary preservation. The flow value increases to five; the finite
palette loops have explicit bounds; the reduction strictly decreases
vertex order. There is no probability or asymptotic inference.
Audit disposition: no error found in the stated R1 chain or this particular
reducible configuration. No conclusion is assigned to M09 R3 or other
six-terminal/topological statements. No novelty claim is made.

best_verified_candidate: none. best_verified_result: none.
Open admitted obligations: obligation:opg401-z20-extension;
obligation:opg401-root. Candidate package status: RESULT_CANDIDATE_READY.
Next obligation: obtain suitable trusted replay and statement-faithfulness
for the frozen V01 local package; for subsequent research keep the remaining
three-versus-three cuts and general root configurations explicitly open.
