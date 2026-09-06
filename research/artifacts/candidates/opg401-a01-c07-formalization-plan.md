# Local-lemma formalization and faithfulness ToolPlan: c07

Status: candidate_only. Artifact type: ToolPlan / formalization design.
Execution status: not_executed. No proof-assistant build is claimed.
Step owner: math-toolchain; proposed encoding owner: math-formalization.
The mathematical derivation route remains owned by math-derivation.
Candidate: candidate:opg401-a01-c07-formalization-plan.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1.
Target: obligation:opg401-z20-extension. Root: obligation:opg401-root.
Fresh cycle base: 73d84621146f93191de810a5582af9dfc849ee65.
Target statement SHA-256:
16533194e20493e83312edbc99b93714f07282d4e65bb58c4cee1c734fa7594e.
Input derivation: research/artifacts/candidates/opg401-a01-c01-local-extension.md,
SHA-256 e735494086580ac664a075c3f97645c0c0358f418c7477cc05379d6945aba8e0.

## 1. Actual preconditions and the nonterminal execution gap

A frontend executable-presence check found no lean, lake or elan.
This was an executable lookup, not a compiler run; no version output,
exit code, generated proof object or receipt exists. The channel
profile independently declares command_execution=false.

The repository fixture declares leanprover/lean4:v4.33.0 in
fixtures/lean-proof/lean-toolchain. Its lake-manifest.json declares
Mathlib commit db584cd6d46c92f209a44c0f1c829460d327499d.
These are requested environment pins, not an observed installation.
The manifest Git blob ID is d1580b698c57aa5a2d6b2e8542c8fa3940832116;
this is not a SHA-256 digest of an execution environment.

The knowledge-source registry marks lean-mathlib-local quarantined.
The broader maturity entry T18 describes a tested verifier adapter;
it does not remove this exact source/version restriction.
The candidate generator has no verification capabilities.
The existing lean-kernel, lean-axiom-auditor and
lean-faithfulness-reviewer entries use fixture-specific policies.
A trusted executor must confirm their applicability to this new
graph obligation and resolve quarantine before issuing any receipt.

This plan does not install a tool, edit fixture files, change policy,
invoke a workflow, or appoint a verifier. It is not a populated
lean-obligation-request: that request needs real source files and a
frozen declaration, which have not yet been built here.

## 2. Definition-level design, before choosing tactics

Proposed finite color type: Fin 20, with representative a.val in 0..19.
Define the following mathematical functions in the planned module:

residue(a,b) = (b.val + 20 - a.val) % 20,
cdist(a,b) = min(residue(a,b), 20-residue(a,b)),
EdgeOK(a,b) = (7 <= residue(a,b) and residue(a,b) <= 13),
allowed(a) = {x : Fin 20 | EdgeOK(x,a)},
common(a,b) = allowed(a) intersect allowed(b).

The subtraction in residue is natural-number subtraction, but
b.val+20 >= a.val, so it cannot truncate before reduction.
The subtraction in the count theorem below IS deliberately truncated:
7-cdist denotes max(0,7-cdist) in natural numbers.
These are different uses and must not be silently interchanged.

The definition map to the frozen statement is:
- Fin 20 representatives <-> elements of Z20.
- residue <-> the unique directed cyclic difference.
- cdist <-> shortest cyclic distance d_20, which is at most ten.
- EdgeOK <-> an edge of a (20,7)-coloring.
- allowed <-> A(a), since 7<=cdist<=13 is equivalent to cdist>=7.
- common.card <-> the exact integer size of A(a) intersect A(b).

This choice does not change the ProblemContract's numerical bound,
graph class, or universal quantifier.

## 3. Finite theorem slices to be constructed

The following names are proposed declaration names, NOT new admitted
obligation IDs and NOT declarations claimed to exist in the repository.

F1: for all a,b : Fin 20, cdist(a,b)<=10.
F2: for all a,b : Fin 20, EdgeOK(a,b) iff EdgeOK(b,a).
F3: for all a,b : Fin 20, EdgeOK(a,b) iff 7<=cdist(a,b).
F4: for all a,b : Fin 20, common(a,b).card = 7-cdist(a,b).
F5: for all a,b : Fin 20,
    (exists x : Fin 20, EdgeOK(x,a) and EdgeOK(x,b))
      iff cdist(a,b)<=6.
F6: translations and reflection preserve cdist and common membership.

F1-F5 are closed finite propositions covering every ordered pair,
not just the eleven normalized examples. A first bounded proof attempt
may use ordinary decidable reduction after all variables are under
finite quantifiers. Do not use native evaluation as a silent shortcut.
If reduction exceeds the bound or gets stuck, split into the eleven
symmetry classes from c01 and prove the symmetry bridge F6 explicitly.
A successful finite table alone without F6 cannot justify reduction
of arbitrary colors to the table.

Proposed import surface: only finite types, finite sets, natural
arithmetic and the selected proof tactics from the exact locked
environment. Resolve the concrete import names in that environment
rather than claim that a current documentation hit pins them.
Do not import all of Mathlib merely to hide unresolved names.

## 4. Generic graph-extension bridge

The color-pair theorem does not by itself formalize graph extension.
Use a separate bridge so that a finite table cannot conceal a
misstated induction hypothesis.

For a vertex type V and relation E : V -> V -> Prop, define
Coloring(E,f) to mean:
  for all x,y, E(x,y) implies EdgeOK(f(x),f(y)).
Define PreservingExtension(E,old,v) to mean:
  there exists f such that Coloring(E,f), and
  for every x!=v, f(x)=old(x).

The proposed bridge assumes:
- E is symmetric;
- v,u,w are pairwise distinct;
- for every x, E(v,x) iff x=u or x=w;
- old is a map V -> Fin 20 satisfying EdgeOK on every E-edge
  whose two endpoints are different from v.

Conclusion:
  PreservingExtension(E,old,v)
    iff cdist(old(u),old(w))<=6.

Forward derivation: any preserving extension supplies f(v) in the
two allowed sets, since u,w differ from v and their old colors are
preserved. Apply F5.

Backward derivation: use F5 to obtain a common color c. Set f(v)=c
and f(x)=old(x) off v. For each edge, separate the cases with first
endpoint v, second endpoint v, and neither endpoint v. Exact-neighbor
membership and symmetry reduce the first two cases to the two
allowed-color tests; the old-coloring assumption handles the last.

The value old(v) is irrelevant. In particular, do NOT assume old
already colors all of G: that would pre-assume the desired extension.
A coloring of G-v is represented by such an old map with an arbitrary
unused value at v. State this representation bridge explicitly.

The bridge is stronger than needed because it works for any symmetric
relation with the stated local neighborhood. Specializing to a finite
simple graph gives the required local application. Planarity,
triangle-freeness and the global maximum-degree bound are not needed
for this local bridge; they remain essential hypotheses of the root
question and are NOT removed from that root.

## 5. Adversarial statement-faithfulness cases

The future semantic review must test, as requirements rather than
claimed program output:
- a=19,b=0: shortest distance one and common cardinal six.
- distance six: exactly one extension, not zero.
- distance seven: no extension even though seven is legal on an edge.
- equal neighbor colors: seven choices.
- arbitrary integer lifts must not enter the edge predicate.
- the graph theorem preserves every old color off v.
- exactly two neighbors means two distinct vertices, not merely a
  degree upper bound with potentially missing edge obligations.
- the converse direction must recover the threshold from an actual
  extension, not just give a sufficient construction.

The C5 deletion witness in c01 must remain nonextendible for its
specified fixed coloring while the separately displayed full C5
coloring remains valid. This checks the crucial quantifier distinction.

The root's dependency on the local lemma is not sufficient to close
the root. No generic graph-colorability theorem is asserted by this
formalization plan.

## 6. Bounded execution and receipt plan

Selected registered source: lean-mathlib-local, current status
quarantined. Selected adapter family: T18, conditional on current
policy qualification. Exact requested Lean and Mathlib pins are in
Section 1; the executor must record binary, source and transitive
manifest digests from the real execution environment.

Initial budget, per attempted formal slice:
timeout_seconds=120; max_memory_bytes=1073741824;
max_output_bytes=1048576; threads=1; max_retries=0.
Use finite heartbeat/recursion limits; never set an unbounded limit.
If a finite proof exceeds this budget, refine the slice or proof
strategy rather than silently weaken its statement.

Planned actions for an authorized executor, not commands run here:
1. Check executable availability, exact versions and the current
   toolchain allowlist; verify quarantine has actually been resolved.
2. Freeze the generated source and expected declaration text, then
   compute their actual content digests and dependency-manifest digest.
3. Compile only that source using the qualified locked environment.
4. Replay the kernel check on the frozen input under the approved
   trust domain, and inspect transitive axioms and escape mechanisms.
5. Review the definition/quantifier map independently of compilation;
   the fixture statement-identity policy must be suitable for this
   generic graph claim before it is used.
6. Return separate receipts for the required capabilities. A trusted
   importer, not this candidate agent, decides their admission.

Failure categories: unavailable executable, version mismatch,
quarantined source, policy not applicable, elaboration failure,
resource limit, axiom/escape rejection, or statement mismatch.
None is a mathematical counterexample and none closes the target.
No expected stdout or success exit code is invented.

After real sources exist, fill the schema in
research/schema/lean-obligation-request.schema.json with the actual
fixture/workspace locator, module, declaration, source files, budgets,
permitted axioms and qualified verifier IDs. Do not fill these fields
with fictional proof files or silently broaden allowed_axioms.

## 7. Source and version comparison

Repository inputs read: the target graph, c01, WEB_CHANNEL_PROFILE.json,
research/verifiers.json, the fixture toolchain/manifest, and the three
math-knowledge source/operator/maturity registries.

Official reference retrieved 2026-09-06:
https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/
describes decidable reduction and the different trust implications of
native evaluation. The corresponding manual landing page reports
4.34.0-rc2, not the fixture's 4.33.0. Its syntax is discovery guidance,
not a claim of compatibility with the locked fixture.
https://lean-lang.org/doc/reference/latest/Basic-Types/Finite-Natural-Numbers/
documents Fin and its representatives; the mathematical map above is
given explicitly rather than relying on a package name.

No source code from another repository was cloned, changed or executed.
No mathematical verifier output is attached to this plan.

## 8. Checkpoint

best_verified_result: none. best_verified_candidate: none.
Best mathematical candidate for the atomic target: c01.
Additional generated graph consequences: c02-c06, with their stated
dependencies and restrictions. This c07 is planning/faithfulness work.
Open obligations: obligation:opg401-z20-extension; obligation:opg401-root.
Registered failed-route IDs checked: [].
Execution blockers are nonterminal and recorded in Issue #4.
Next action: continue a hand derivation of the multi-neighbor
intersection property on Z20, including the empty-neighborhood case
and a parameter-boundary attack; do not wait for a compiler or pretend
that the present transport checks execute this plan.
