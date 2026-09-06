# Class-preserving neighbor identification: candidate c02

Status: candidate_only. Primary owner: math-derivation.
Candidate: candidate:opg401-a01-c02-neighbor-quotient.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1.
Target: obligation:opg401-z20-extension.
Root remains open: obligation:opg401-root.
Fresh cycle base: 7bc59e6daf30bb8b2f79132a976d74dd1e0675bf.
Prior candidate: research/artifacts/candidates/opg401-a01-c01-local-extension.md
(prior SHA-256 e735494086580ac664a075c3f97645c0c0358f418c7477cc05379d6945aba8e0).

## 1. Frozen statement

Let G be a finite simple triangle-free planar graph with maximum degree
at most three. Let v have exactly two distinct neighbors u,w.
Write U=N_G(u) minus {v}, W=N_G(w) minus {v}, and c=|U intersect W|.
Triangle-freeness implies u,w are not adjacent, so U,W lie outside
{u,v,w}. Define H by deleting v, identifying u and w to a single
vertex h, and replacing parallel edges by single edges.

Candidate Q1 (claim:opg401-c02-class-preservation):
H is in the same graph class if and only if BOTH
  (i) |U union W|=deg_G(u)+deg_G(w)-2-c <=3,
  (ii) no five-cycle of G contains v.

Candidate Q2 (claim:opg401-c02-quotient-extension):
Every (20,7)-coloring of H lifts to a coloring of G-v in which u,w have
the same color, and then has exactly seven extensions at v.
Consequently a vertex-minimal non-(20,7)-colorable member of the class
cannot contain v satisfying (i) and (ii).

These are candidate refinements of the graph application of the
admitted local lemma, not new admitted obligation records. Background:
finite graph basics, preservation of planarity under edge contraction,
and the explicit local extension rule from c01.

## 2. Quotient construction and degree audit

Contract vu and then the image of vw in a planar drawing of G. Because
v has no other neighbors, the resulting simple graph, after suppressing
parallel edges, is exactly H. Therefore H is finite, simple and planar.
Its vertex order is |V(G)|-2. No noncontracted edge becomes a loop,
because uw is absent.

The neighborhood of h is precisely U union W. Its degree is
deg_G(u)-1 + deg_G(w)-1 - c.
An outside vertex adjacent to both u,w loses one incidence after
parallel-edge suppression; every other outside vertex keeps its
degree. Thus outside degrees are at most three, and H is subcubic if
and only if (i) holds. Counting the union, rather than the sum alone,
is essential when u,w have a common neighbor.

## 3. Exact triangle audit

Any triangle of H not containing h would already have been a triangle
of G, which is impossible. A triangle h-x-y-h exists precisely when
xy is an edge of G and x,y lie in U union W.

No such xy can have both endpoints in U: otherwise u-x-y-u is a
triangle of G. The same applies to W. In particular an endpoint in
U intersect W cannot participate in such an xy.
Therefore every remaining triangle h-x-y-h corresponds, after possibly
interchanging x,y, to
  x in U minus W, y in W minus U, xy in E(G).
It gives a path u-x-y-w of length three in G-v, and together with
w-v-u gives a five-cycle through v. All five vertices are distinct.

Conversely, a five-cycle through a degree-two vertex v necessarily has
the form v-u-x-y-w-v. Its middle edge xy survives identification, and
the three distinct quotient vertices h,x,y form a triangle in H.
It follows that H is triangle-free if and only if (ii) holds.

Combined with the degree audit, this proves both directions of Q1.
The five-cycle condition is about any five-cycle through v, not just a
face of a chosen embedding.

## 4. Coloring lift and minimal-counterexample use

For a (20,7)-coloring psi of H, color u,w by psi(h) and color each
other vertex of G-v by its image color. Every edge of G-v maps to an
edge of H; no loop or uw edge interferes. This is a valid coloring.
At v the neighbor-color distance is zero, so c01 gives seven choices
psi(h)+7,...,psi(h)+13 modulo 20.

For completeness, this lift has a converse at the deletion level:
any coloring of G-v with equal colors on u,w descends to H. Thus
H-colorability is equivalent to the existence of an equal-neighbor
coloring of G-v. Equal colors are a sufficient special case of the
distance-at-most-six criterion, not a necessary case for extension.

If G had minimum order among the non-(20,7)-colorable graphs of the
contract class and (i),(ii) held, then H would be a smaller member
of the class, so H would have such a coloring. The lift and extension
would color G. This contradiction is conditional on that hypothetical
minimal graph; it is not a proof that all configurations meet (i),(ii).

## 5. Explicit structural consequences

Because deg_G(u),deg_G(w)<=3:
- If one of u,w has degree at most two, (i) holds automatically.
- If both have degree three, (i) holds exactly when c>=1.

Hence in any vertex-minimal obstruction every degree-two vertex v
must satisfy at least one of the following alternatives:
v is on a five-cycle; or both neighbors have degree three and their
external neighborhoods U,W are disjoint.
This is a necessary condition, not an existence theorem for obstructions.

In particular, a degree-two vertex adjacent to another degree-two
vertex must be on a five-cycle. A degree-two vertex on a four-cycle
must also be on a five-cycle: the opposite vertex of the four-cycle
is a common neighbor of u,w, so (i) is automatic.
These consequences follow by contrapositive from Q1-Q2.

## 6. Cheapest attacks: why neither condition may be dropped

Five-cycle witness:
G=v-u-x-y-w-v has all degrees two and satisfies (i).
The quotient H on h,x,y is a triangle. Thus deleting condition (ii)
destroys class preservation. In fact a triangle has no (20,7)-coloring:
c01 says the neighborhoods of two legal edge colors, whose distance
is at least seven, have empty intersection.
The original C5 is colorable by 0,8,16,4,12 around the cycle.
This rejects universal equal-neighbor reduction, not the root conjecture.

Degree-growth witness:
Let G be the tree with edges vu,vw,ux1,ux2,wy1,wy2, on seven distinct
vertices. It is triangle-free, planar, subcubic and has no five-cycle.
The quotient is the four-leaf star centered at h, so deg_H(h)=4.
It violates (i) and leaves the contract class. Both G and H are
colorable (they are bipartite, using colors 0 and 10).
The failure is the minimality argument's domain, not colorability.

Common-neighbor audit:
If u,w both have degree three but share a vertex z outside v, the
quotient degree is at most three, not four. Such a common neighbor
does not create a loop. Its two incidences merge to one.
If U=W, the quotient degree is two and no cross edge is possible,
since an edge within U would already form an original triangle.

## 7. Reproduction, source reuse, and limitations

Reconstruct H directly by the stated contraction and union rule.
Check that the only possible new triangles contain h and correspond
bijectively, up to reversing the middle path, to five-cycles through v.
Check the two explicit small witnesses. No program was run for these
mathematical checks; text preparation and SHA-256 hashing are transport
helpers only.

No additional literature theorem is asserted. Definitions and the
circular/fractional distinction are preserved from
research/artifacts/source-notes/opg401-a01-c01-definition-sources.md.
The prior candidate is a generated input, not upgraded to Evidence by
its successful PR transport. The argument above supplies the missing
class-preservation reasoning in full.

Request faithful graph encoding, kernel_check, axiom_escape_audit and
statement_faithfulness under the existing target acceptance. Do not
reuse fixture-only verifier policies without confirming applicability.
The root and the local obligation remain open pending those gates.

## 8. Checkpoint and next refinement

best_verified_result: none. best_verified_candidate: none.
best_candidate: c02 together with c01, both generated/self-audited.
Route status: active; exact local criterion and a conditional
class-preserving reduction are now explicit.
Registered failed-route IDs checked: [].
Discarded shortcuts: universal fixed-color greedy extension (c01 C5);
unconditional neighbor identification (C5 and degree-growth tree).
These do not negate the admitted exact-criterion route.
Open obligations: obligation:opg401-z20-extension; obligation:opg401-root.
Next action within this same target: derive exact endpoint feasibility
for chains of degree-two vertices by modular sumsets, and distinguish
fixed-boundary extension failures from actual reducible configurations.
