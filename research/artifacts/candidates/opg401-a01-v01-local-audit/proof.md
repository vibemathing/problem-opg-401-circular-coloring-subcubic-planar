# Z20 extension: hand proof, complete finite certificate, and faithfulness audit

Status: RESULT_CANDIDATE_READY. Verdict: candidate_only.
Candidate: candidate:opg401-a01-v01-local-audit.
Primary owner: math-derivation; computation is a bounded frontend cross-check.
Problem: problem:opg-401-circular-coloring-subcubic-planar.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1.
Target: obligation:opg401-z20-extension.
Read base: 165b7db2b8cdb65fd06121494f24f21fb690ad1f.

## Definition freeze and semantic comparison

The canonical contract uses representatives in {0,...,p-1} and the
edge condition q <= |phi(u)-phi(v)| <= p-q. C01 explicitly defines
r(a,b)=[b-a]_20 and d_20(a,b)=delta(a,b)=min(r(a,b),20-r(a,b)).
We retain exactly this UNDIRECTED shortest distance, taking values 0..10.
The directed residue r is a different function; it is not the distance
argument in the cardinality formula below.

For fixed representatives a,b, let h=|b-a|. The residues r and 20-r
are h and 20-h in some order (the zero case is separate and immediate).
Thus the following edge predicates are equivalent:
  7 <= h <= 13;
  7 <= r(a,b) <= 13;
  delta(a,b) >= 7.
Consequently A(a)={x:7<=d_20(x,a)<=13}=a+{7,...,13}.
The upper bound 13 is redundant for d_20<=10, but not for r.
There is no conflicting allowed-color predicate in the prompt and C01.
Arbitrary integer lifts, rather than these fixed representatives, are
not permitted inside the absolute value. This resolves the notational
comparison by equivalence, without choosing a different ProblemContract.

Exact local target: for EVERY a,b in Z20, determine the set cardinality
and nonemptiness, including a=b. Its negation would be one ordered pair
with a different cardinality or nonemptiness truth value.

## Rotation first, then reflection

Translate every color by -a. This sends (a,b) to (0,r(a,b)) and sends
A(a) intersect A(b) bijectively onto A(0) intersect A(r(a,b)).
Next put t=min(r(a,b),20-r(a,b)). If r>10 reflect x to -x; otherwise
do not reflect. With epsilon respectively -1 or +1, the composite is
T(x)=epsilon*(x-a), T(a)=0, T(b)=t, and T^{-1}(y)=a+epsilon*y.
The set S={7,...,13} satisfies -S=S in Z20, so both operations preserve
allowed-color membership. Delta is invariant, making t a complete
class invariant. At t=0 and t=10 either reflection choice gives the
same set, so neither symmetry fixed point is lost.

## Full table and proof

Intervals in this table use ordinary inclusive integer representatives.

| t | A(t) | A(0) intersect A(t) | cardinality |
|---|---|---|---|
| 0 | [7,13] | [7,13] | 7 |
| 1 | [8,14] | [8,13] | 6 |
| 2 | [9,15] | [9,13] | 5 |
| 3 | [10,16] | [10,13] | 4 |
| 4 | [11,17] | [11,13] | 3 |
| 5 | [12,18] | [12,13] | 2 |
| 6 | [13,19] | {13} | 1 |
| 7 | [14,19] union {0} | empty | 0 |
| 8 | [15,19] union [0,1] | empty | 0 |
| 9 | [16,19] union [0,2] | empty | 0 |
| 10 | [17,19] union [0,3] | empty | 0 |

For 0<=t<=6, t+S=[7+t,13+t] does not wrap because 13+t<=19.
Its intersection with S is [7+t,13], with 13-(7+t)+1=7-t elements.
For 7<=t<=10, t+S=[t+7,19] union [0,t-7]. The first part starts
at least at 14 and the second ends at most at 3; neither meets S.
Applying T^{-1} proves for all ordered pairs:

  |A(a) intersect A(b)| = max(0,7-delta(a,b));
  A(a) intersect A(b) is nonempty iff delta(a,b)<=6.

For t<=6, the actual set is {a+epsilon*y:7+t<=y<=13}; in particular
a+epsilon*13 is a deterministic witness. No enumeration is a premise.

Atomic claims: claim:opg401-v01-definitions, claim:opg401-v01-symmetry,
claim:opg401-v01-count, claim:opg401-v01-extension-bijection.
Dependency chain: definitions -> symmetry -> interval table -> count
and witness -> preserving-extension bijection. No root claim follows.

## Exact degree-two extension bijection

Let G be a finite simple graph, v a vertex with exactly two distinct
neighbors u,w, and psi a valid (20,7)-coloring of the induced G-v.
Set a=psi(u), b=psi(w). Neighbor vertices are distinct but their colors
may be equal. Define Ext(psi,v) as full colorings f of G satisfying
f(x)=psi(x) for EVERY x other than v.

Evaluation f -> f(v) maps Ext(psi,v) into A(a) intersect A(b), since
both incident edges must be legal. Conversely, for any z in the
intersection, set f(v)=z and f(x)=psi(x) otherwise. Edges not incident
to v are valid by the premise on psi; the remaining edges are precisely
vu and vw and are valid by the two memberships. These maps are inverse.
Thus both existence and the EXACT number of preserving extensions are
respectively delta(a,b)<=6 and max(0,7-delta(a,b)).

A total encoding old:V->Z20 may give v an arbitrary placeholder value.
That value is never read by either direction; only old off v must color
G-v. Changing the placeholder does not change Ext. Removing the validity
premise for old edges, or dropping preservation off v, changes the theorem.
Planarity, triangle-freeness and maximum degree three are not needed
for this local statement and are not removed from the root statement.

For G to be colorable it is enough that SOME deletion coloring has a
favorable pair; the theorem does not say EVERY deletion coloring does.
The C01 five-cycle deletion colors 0,7,14,7 are valid but do not extend
at its missing vertex. The full cycle colors 0,8,16,4,12 are valid.
Both facts are reproduced in the finite audit as quantifier controls.

## Executed formula-free certificate and different-code-path checker

Files in this directory are complete reproducible inputs, source and
outputs. enumerate.py tests each of 400 ordered pairs against all 20
possible colors using directed residues, with no closed-form call.
certificate.json stores every actual intersection as a 20-bit mask
and its 20x20 count matrix, in explicit a-major, b-minor row order.
check.py does not import enumerate.py. It reconstructs every set using
fixed-representative absolute differences, then checks the closed form,
threshold, inverse symmetry map, and agreement with the distance form.
The two methods are algorithmically separate but share the candidate
generator trust domain: this is not a trusted verifier receipt.

Actual observed results in audit.json: 400 pairs, 8000 candidate-color
membership cases, zero disagreements, 260 nonempty intersections,
980 total common-color occurrences. It also checks 400 swaps, 400
reflections, all 8000 common translations, all 400 inverse symmetry
maps, 20 equal pairs, 20 antipodal pairs and 80 endpoint controls.
The normalized counts are 7,6,5,4,3,2,1,0,0,0,0.
As a separate hand mass check, 20*(7+2*(6+5+4+3+2+1))=980.

Twelve negative tests detect: deletion of endpoint 7; deletion of 13;
natural subtraction truncation; omission of palette color 19; a missing
inclusive +1; use of directed residue as shortest distance; use of the
linear absolute difference as shortest distance; circumference 19;
threshold <=7; a flipped certificate bit; a missing row; a duplicated row.
Every detected mutant has a witness in audit.json. These tests are not
claimed to cover every possible bug in the checker.

## Execution boundary and reproduction

Command from this directory: python3 -I -S run.py.
Actual runtime: CPython 3.13.5. Arithmetic: exact Python integers only.
Each child process: 10-second wall timeout, 5-second CPU limit,
128 MiB address space, 64 KiB file/output cap, one thread, zero retries.
The finite generator loop has 8000 iterations; the finite transformation
checks have bounded loop domains. There is no asymptotic or induction claim.
execution.json binds actual source/input/output and binary SHA-256 values,
observed subprocess exit statuses and elapsed times. All final subprocesses
returned zero. preflight-failures.json preserves the initial killed startup
probe; switching to isolated no-site Python was the recorded correction.

The GitHub profile still describes command_execution=false. These are
actual foreground sandbox executions under the user's explicit conditional
command authorization, not executions inside the repository or its verifier
adapter. The skill-referenced scripts/compute_plan.py is absent at the read
base; no planner invocation, installed solver, GPU route or registry upgrade
is fabricated. The resource choice is an explicit bounded CPU fallback,
not a claimed run of that missing script. No Lean or SMT command was run.

## Reasoning discipline and checkpoint

Definitions, quantifiers, symmetry fixed points, constructive witness,
edge coverage, endpoints, and negative tests are explicit above. Termination
uses finite loop ranges, not an inference from samples. Probability and
asymptotic scale arguments are inapplicable to this fixed finite target.
The generic graph bridge is a hand bijection, not covered by a graph search.
C01-C08 were read at the base; their larger reductions are not premises here.
Bibliographic definition cross-check is in the accompanying source note.

best_verified_candidate: none. best_verified_result: none.
Local proof-and-cross-check package: RESULT_CANDIDATE_READY, candidate_only.
Open admitted obligations: obligation:opg401-z20-extension;
obligation:opg401-root. Required future capabilities remain kernel_check,
axiom_escape_audit, statement_faithfulness under a suitable trusted policy.
Next bounded target: audit ONLY M09 R1 and its disk-deletion consequence;
do not promote the rest of M09 or the root from this local result.
