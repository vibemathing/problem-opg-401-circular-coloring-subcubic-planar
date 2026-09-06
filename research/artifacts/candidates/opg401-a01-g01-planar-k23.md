# Planar K2,3 configuration: component rotations and reducibility

Status: candidate_only. Primary owner: math-derivation.
Candidate: candidate:opg401-a01-g01-planar-k23.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1.
Target: obligation:opg401-z20-extension.
Root remains open: obligation:opg401-root.
Cycle base: d0f1000ba8b4378d91a1946c417ac9947360af2e.

## Frozen claim and quantifiers

Let G be a finite simple triangle-free planar graph of maximum degree
at most three. Suppose five distinct vertices u,v,x1,x2,x3 span the
six edges uxi,vxi, for i=1,2,3. Put X={u,v,x1,x2,x3} and H=G-X.

Claim G1 (claim:opg401-g01-planar-k23):
G has a (20,7)-coloring if and only if H does.
More precisely, every (20,7)-coloring of H can be rotated separately
on each connected component of H, and the modified coloring extends
to G with both u and v colored zero.

This does NOT say that every fixed coloring of H extends unchanged.
The allowed changes are explicitly whole-component rotations.
It is a reducibility candidate obtained from the exact local
criterion, not a proof of the root ProblemContract.

Use residues in Z20 and shortest distance delta as frozen in c01.
A(a)=a+{7,...,13}. The local candidate input is
|A(a) intersect A(b)|=max(0,7-delta(a,b)).
Its proof is reproduced by the interval argument in c01; successful
transport of c01 is not mathematical verification.

## 1. Which edges can meet the five-vertex configuration?

The two poles u,v already have degree three, so have no other
neighbors. They are not adjacent, because that would create a
triangle with each xi (as well as violate the degree bound).
No two middle vertices xi,xj are adjacent: they share u and would
form a triangle. Each xi therefore has either no outside neighbor
or exactly one outside neighbor ti in H. The outside vertices ti
are allowed to coincide.

These facts ensure that after choosing colors for u,v the three
middle vertices can be colored independently, subject only to
their stated outside constraints.

## 2. Planarity bounds each outside component's attachments

Claim G2 (claim:opg401-g01-two-attachments):
Every connected component C of H is adjacent to at most two of
the three middle vertices.

Suppose instead C is adjacent to all three. Contract a spanning
tree of C to one vertex z. Delete all other outside components,
suppress loops and parallel edges, and retain the six pole-middle
edges and one edge zxi for each i. This gives a K3,3 minor, with
parts {u,v,z} and {x1,x2,x3}. All six vertices are distinct
because C is disjoint from X.

Edge contraction and deletion preserve planarity. For a direct
audit of the obstruction, K3,3 cannot be planar: it has n=6,m=9,
is bipartite and has no bridge. In a plane embedding each facial
boundary would have length at least four. Thus 2m>=4f, while
Euler's formula gives f=2-n+m=5; these inequalities would require
18>=20. This is impossible. Consequently the asserted component
C cannot exist, proving G2.

The statement bounds the number of middle vertices touched, not
just the number of distinct outside vertices. It still rules out
one outside vertex adjacent to all three.

## 3. Center two boundary colors by a rotation

Claim G3 (claim:opg401-g01-two-color-centering):
Any family of at most two colors in Z20 can be translated so that
all its members have shortest distance at most five from zero.

For one color translate it to zero. For two colors, order them as
a,b so that [b-a]20=d=delta(a,b)<=10. Such an ordering exists by
choosing a direction of a shortest arc. Translate by
-a-floor(d/2). The resulting colors have integer representatives
-floor(d/2) and ceil(d/2). Both have absolute value at most five,
hence shortest circular distance at most five from zero.
For equal colors take d=0. The two antipodal colors d=10 become
-5 and 5, so the extremal case is included.

Ordering the two boundary labels is not a graph modification.
The color change itself is a translation of ALL colors in the
component, not a partial recoloring and not a reflection.

## 4. Construct the extension

Start with any (20,7)-coloring of H.
For each component C having attachments, gather the colors of
the outside neighbors ti belonging to C. By G2 there are at most
two entries. Apply G3 and translate every color in that component
by the resulting common residue. Components without attachments
may be left unchanged.

Every edge of H has both ends in one component, so all edge
differences remain unchanged. There are no edges between
different components. The translated coloring of H is therefore
valid. Each outside neighbor ti now has color bi with
delta(0,bi)<=5.

Set phi(u)=phi(v)=0. For each attached xi, choose any color from
A(0) intersect A(bi). By c01 this set has size
7-delta(0,bi)>=2. For each unattached xi choose any color in A(0),
which has size seven. By Section 1 these choices have no mutual
constraints. They satisfy all edges of G, completing the extension.

If k of the middle vertices have outside neighbors, the chosen
component rotations and pole colors leave at least
2^k * 7^(3-k) choices for their colors. This is a lower bound on
extensions of the modified coloring, not a count over all choices
of component rotations or all colorings of G.

The reverse implication of G1 follows simply by restricting a
coloring of G to H.

## 5. Consequence for a hypothetical minimal counterexample

Deletion of X preserves all graph-class assumptions and reduces
the vertex order by five. Hence a member of the class of minimum
vertex order having no (20,7)-coloring cannot contain K2,3.

Equivalently, such a minimal member cannot have two distinct
vertices with three common neighbors. In a subcubic simple graph
the three common neighbors saturate both vertices' degrees and
produce exactly the configuration covered above.
This is a necessary structural exclusion; there are many graphs
without this configuration, and the root remains open.

The argument produces the required favorable neighbor-color
pairs for the three degree-two extension steps by controlling
outside component rotations. It does not silently assume that
a randomly chosen deletion coloring has favorable boundary colors.

## 6. Adversarial checks and limitations

Fixed-boundary shortcut:
Take K2,3 and add three distinct pendant outside vertices t1,t2,t3,
one adjacent to each xi. Prescribe colors 0,7,14 on these three
isolated vertices of H. If G extended this fixed coloring and a
were the color of u, each xi would be a common allowed color for
a and the corresponding ti. Necessarily delta(a,bi)<=6 for all
bi in {0,7,14}.

This is impossible. Let B6(b)={a:delta(a,b)<=6}=Z20 minus A(b).
The three sets A(0)=[7,13], A(7)=[14,19] union {0}, and
A(14)=[1,7] cover Z20. Thus the three B6 sets have empty
intersection. Nevertheless this graph is bipartite and colorable:
color u,v,t1,t2,t3 by zero and all xi by ten. Its isolated outside
components can be rotated to the displayed equal boundary colors.
The fixed-color failure therefore does not contradict G1.

Planarity boundary:
In K3,3, delete a K2,3 formed by two vertices on one side and the
three on the other. The remaining single vertex touches all three
middle vertices, showing that G2 uses planarity essentially.
K3,3 itself is bipartite and (20,7)-colorable, so this is not a
counterexample to a coloring statement.

Degree boundary:
Without the subcubic bound a middle vertex might have two or more
outside neighbors. Section 4 would then involve additional
simultaneous constraints and is not justified by this proof.

The proof also covers H empty, repeated ti, one or two attachments,
and an outside component touching two antipodally colored ti.
No assertion is made about keeping the original outside coloring
unchanged; the rotations are part of the claim.

## Sources, reproducibility, verification and checkpoint

Repository sources at the cycle base:
- problem-library/records/canonical-problems.jsonl
- research/records/obligation-graphs.jsonl
- research/records/failed-routes.jsonl
- research/artifacts/candidates/opg401-a01-c01-local-extension.md

Only elementary finite graph operations, Euler's formula and the
fully stated local interval criterion are used. No external
classification or recoloring-connectivity theorem is assumed.
The c08 general family theorem is compatible but is not needed
as a proof premise here. No novelty claim is made.

Reproduce by checking the spanning-tree contraction, the three
edge categories, the explicit two-color translation, and the
pendant-boundary witness. No graph enumeration, solver, proof
assistant or mathematical runtime was executed for this candidate.
Text serialization and content hashing are transport helpers only.

Requested future verification: faithful graph encoding of G1-G3,
kernel_check, axiom_escape_audit, and statement_faithfulness. The
fixture verifier policies require a separate suitability check.
best_verified_result: none. best_verified_candidate: none.
Best generated advance: unconditional K2,3 reducibility after
component rotations, conditional only on the stated class.
Open obligations: obligation:opg401-z20-extension; obligation:opg401-root.
Registered failed-route IDs checked: [].
Discarded shortcut: extension with arbitrary outside colors fixed;
the small pendant-boundary witness above is its exact obstruction.
The admitted route remains active.
Next action: distinguish this component-controlled reduction from
configurations having three boundary constraints in one connected
outside graph; refine the frozen formalization interface without
claiming compilation or altering the verifier registry.
