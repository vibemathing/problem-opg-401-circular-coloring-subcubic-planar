# Preserving extensions: exact bijection and encoding witnesses

Status: candidate_only. Primary owner: math-derivation.
Candidate: candidate:opg401-a01-f01-extension-bijection.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1.
Target: obligation:opg401-z20-extension.
Root remains open: obligation:opg401-root.
Cycle base: ae202fd206b64b875d0c2ea75e272d0761469af1.

This is a mathematical bridge and semantic-audit candidate for the
unexecuted c07 formalization plan. It contains no compiled source,
execution receipt or assertion of verifier success.

## 1. Typed objects and hypotheses

Let V be a finite vertex set and E a symmetric, irreflexive relation
on V. Fix v in V and a total function c:V->Z20. The value c(v) is
only a placeholder; v is not yet constrained to have that color.

Use the modular edge relation R(a,b) iff 7<=[b-a]20<=13.
As in c01, R is symmetric and is equivalent to delta(a,b)>=7.
Assume Away(E,c,v): for every x,y distinct from v, E(x,y) implies
R(c(x),c(y)). This asserts exactly that the old coloring is valid
on the deletion, not that c already colors the whole graph.

Define:
Ext(E,c,v) = {f:V->Z20 : f is valid on every edge of E,
                         and f(x)=c(x) for every x!=v};
F(E,c,v) = {z in Z20 : R(z,c(x)) for every x with E(v,x)}.

Irreflexivity ensures that each x occurring in F is different
from v. Thus F never uses the placeholder c(v).

Claim F1 (claim:opg401-f01-extension-bijection):
under Away(E,c,v), evaluation f -> f(v) is a bijection
Ext(E,c,v) -> F(E,c,v).

Claim F2 (claim:opg401-f01-exact-extension-count):
the number of preserving extensions equals |F(E,c,v)|.
For a degree-two vertex with distinct neighbors u,w it equals
max(0,7-delta(c(u),c(w))).

Claim F3 (claim:opg401-f01-placeholder-invariance):
if c and d agree at every vertex except possibly v, their
extension sets and their available-color sets are identical.
The placeholder value cannot influence the extension problem.

## 2. Construct the inverse explicitly

For z in F define Ins(z):V->Z20 by
  Ins(z)(x) = z when x=v, and c(x) when x!=v.
It agrees with c everywhere off v by definition.

To check an edge E(x,y), split into three exhaustive cases.
If neither endpoint equals v, validity follows from Away.
If x=v, then y!=v by irreflexivity; the condition z in F gives
R(z,c(y)), precisely the required edge condition.
If y=v, then x!=v. Symmetry of E yields E(v,x), so F gives
R(z,c(x)); symmetry of R yields R(c(x),z), as required.
The case x=y=v is excluded by irreflexivity.
Thus Ins(z) belongs to Ext(E,c,v).

Conversely, for any f in Ext, every edge E(v,x) has x!=v and
R(f(v),f(x))=R(f(v),c(x)). Hence f(v) belongs to F.

Evaluation after insertion returns z. Insertion after evaluation
returns f at v and returns c(x)=f(x) everywhere else. The functions
are therefore equal at every input. These are two-sided inverses,
proving F1. No choice among unrelated graph colorings is used.

Because F is a subset of the twenty-element palette, F1 gives
F2 without enumerating 20^|V| functions. For two neighbors,
F=A(c(u)) intersect A(c(w)), so c01 supplies its exact count.
At degree zero F is the entire palette, with twenty choices;
at degree one F is a single allowed set, with seven choices.

For F3, the two agreement requirements defining Ext are the
same because they refer only to x!=v. Their full-edge validity
condition is also the same, independent of c and d.
Every neighbor of v is off v, so F is unchanged as well.
Both directions follow directly; Away is preserved by replacing
only the placeholder.

## 3. Optional extension using the c08 candidate

For any positive degree, let C={c(x):E(v,x)} be the SET of neighbor
colors, with repeated colors removed. Define D(C) as the maximum
pairwise shortest distance in C. From F1 and c08 the generated
extension count is max(0,7-D(C)).

This optional corollary depends on c08. F1, F3 and the degree-two
count do not. Deduplication removes redundant constraints, not
vertices or edges from the input graph. An empty C is handled
separately with count twenty, never with an invented value D=0
in the nonempty-family formula.

Dependency map:
frozen simple-graph and coloring definitions -> F1 and F3;
F1 plus c01 -> degree-two F2;
F1 plus c08 -> optional positive-degree count.
Nothing in this map closes the root obligation.

## 4. Eight exact witnesses against incorrect encodings

The following are mathematical audit requirements with explicit
truth values, not results of tests run by a program. Names M1-M8
identify proposed mutations, not admitted failed-route records.

M1. Truncated subtraction before modular reduction.
With a=13,b=0, the correct [b-a]20 is seven, so R(a,b) holds.
Natural-number (b-a)%20 instead gives zero and rejects the edge.
The safe proposed Fin20 expression (b.val+20-a.val)%20 depends on
both input values being bounded below twenty.

M2. Linear distance replacing shortest circular distance.
For a=19,b=0, delta=1 and A(19) intersect A(0)={7,...,12},
of size six. Substituting |19-0|=19 into max(0,7-t) gives zero.

M3. Strict endpoints replacing inclusive edge inequalities.
For neighbor colors 0 and 6, the sole common allowed color is 13.
Both required edge distances are seven. A strict lower bound
discards it; a strict directed upper bound discards the residue
13 on the edge from 0. The correct count is one, not zero.

M4. A duplicate palette entry inflating cardinality.
A(7) intersect A(13)={0}. A list formed from integers 0,...,20
and then reduced modulo twenty contains color zero twice.
Filtering that list counts two entries rather than one color.
A formal length-based count therefore needs a complete,
duplicate-free enumeration or a finite SET cardinality.

M5. Omitting agreement with the old coloring.
On the cycle v-u-x-y-w-v take deletion colors
c(u),c(x),c(y),c(w)=0,7,14,7.
Away holds, but F is empty and hence Ext is empty.
The full graph has the valid cyclic coloring 0,8,16,4,12.
Replacing Ext by all full-graph colorings therefore changes
a false preserving-extension assertion into a true assertion.

M6. Requiring agreement also at the uncolored vertex.
On the path u-v-w take c(u)=c(w)=c(v)=0.
Away holds and the true Ext has seven members, with f(v)=7,...,13.
A definition requiring f=c on ALL vertices forces f(v)=0 and
has no valid member. Compare also the placeholder c(v)=10:
the true Ext stays the same, but this mutated definition now
has one member. Both discrepancies violate F3.

M7. Dropping the Away hypothesis.
Let v be isolated and let the two other vertices u,w form an
edge. Put c(u)=c(w)=0. The available set F has twenty colors,
but no valid full coloring agreeing off v exists.
This is an invalid input for F1 because Away fails. An encoding
without that premise would assert a false equality 0=20.

M8. Applying the nonempty-family formula to degree zero.
For the one-vertex graph with no edges, Ext has twenty members.
Defining the empty family's diameter as zero and applying
max(0,7-D) would give seven. The degree-zero branch must be
separate, despite placeholder irrelevance and valid Away.

All graph witnesses except the explicitly invalid old coloring
in M7 satisfy the stated Away condition. All the graphs themselves
are finite simple triangle-free planar and subcubic.
The errors concern semantics and quantifiers, not a contradiction
to the ProblemContract.

## 5. Encoding interface and execution boundary

The proposed formal implementation may represent the total old
map c with an arbitrary value at v, provided Ext enforces agreement
only off v and Away checks only off-v edges. F3 certifies that this
representation matches a genuinely partial old coloring.

For the degree-two specialization require u!=v, w!=v, u!=w,
and E(v,x) iff x=u or x=w. These hypotheses identify two distinct
graph neighbors; equal COLORS c(u)=c(w) remain allowed.
Keep edge symmetry and irreflexivity explicit in a relation-based
encoding, or derive them from the chosen simple-graph type.

A future source module should expose evaluation, insertion,
their two inverse identities, and the cardinality transfer before
specializing to the finite local table. This separates the generic
graph bridge from the 400-pair color arithmetic and makes missing
agreement or edge hypotheses visible in declaration types.

The eight mutation witnesses should be checked against the exact
declarations and definition bodies, in addition to positive
theorem compilation. They are not a replacement for a kernel check
or statement-faithfulness review, and no axiom-audit result is
asserted here. No Lean file is claimed to exist for this candidate.

The c07 execution boundary remains unchanged: there is no
authorized local compilation or mathematical enumeration in this
step. No toolchain installation, quarantine bypass, fixture-policy
expansion or verifier-registry edit is performed. An authorized
executor must first freeze real source bytes and environment
identities and satisfy the existing verification prerequisites.

## 6. Sources and checkpoint

Sources at the cycle base:
problem-library/records/canonical-problems.jsonl;
research/records/obligation-graphs.jsonl;
research/records/failed-routes.jsonl;
research/artifacts/candidates/opg401-a01-c01-local-extension.md;
research/artifacts/candidates/opg401-a01-c07-formalization-plan.md;
research/artifacts/candidates/opg401-a01-c08-common-neighborhoods.md.

This candidate fills the mathematical graph-to-local bridge and
adds explicit negative encoding witnesses; it does not merely
rename the c07 execution plan. No external theorem or package
behavior is used as a proof premise. No novelty claim is made.
All counts above are justified by the exhibited sets or bijection,
not reported as machine enumeration.

best_verified_result: none. best_verified_candidate: none.
Best new generated claim: the preserving-extension bijection,
with placeholder invariance and eight semantic mutation witnesses.
Open obligations: obligation:opg401-z20-extension; obligation:opg401-root.
Registered failed-route IDs checked: [].
Route status: active_candidate_derivation.
Next action: use the bijection and common-color sets to derive
compact boundary signatures for a connected configuration rather
than replacing a fixed-color extension problem with unrestricted
graph colorability; keep future formal execution separate.
