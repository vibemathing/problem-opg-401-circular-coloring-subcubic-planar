# V01 statement comparison for an assigned verifier

Status: comparison_input_ready; verification_request_pending.
Verdict: candidate_only. This is not a verifier receipt or an admission decision.
Repository: vibemathing/problem-opg-401-circular-coloring-subcubic-planar.
Read revision: 7928d42a5c57e0c94bbc694b1ee2efc63836ee39.
Obligation: obligation:opg401-z20-extension.
Obligation statement SHA-256:
16533194e20493e83312edbc99b93714f07282d4e65bb58c4cee1c734fa7594e.
ProblemContract SHA-256:
76b2207954d4831261d0a61359a19e803cf8d913301756673c4c5ab962d8c8d6.

## Frozen sources

research/artifacts/candidates/opg401-a01-v01-local-audit/proof.md
SHA-256 b7aeabb37c0e358cfd6531e19c8cea3d161856b4da86524f95986a225b3d326a
Git blob 495d710ec5a49d0fdea4e936aed5bea283ad5892.

research/artifacts/candidates/opg401-a01-v01-local-audit/certificate.json
SHA-256 9e78a1668b638d72d49a47e33af9a2752d6bf65d6fd2559658e8177fd8474d53
Git blob 0c379ad356fd4dfac3cdeb57fe75501b3145ba18.

The source bytes supplied in the earlier archive were hashed again for this
request. Their computed Git blob IDs match the frozen repository source IDs.
The archive is only a byte source; its prose receipt is not verification.

## Exact mathematical statement to encode and compare

Let C=Z/20Z, with representatives 0,...,19. Define
r(a,b)=[b-a]20; delta(a,b)=min(r(a,b),20-r(a,b));
EdgeOK(a,b) iff 7<=r(a,b)<=13; A(a)={x:EdgeOK(x,a)}.
For every a,b in C:
(1) |A(a) intersect A(b)|=max(0,7-delta(a,b));
(2) (exists x, EdgeOK(x,a) and EdgeOK(x,b)) iff delta(a,b)<=6.
The original expression 7<=d20(x,a)<=13 uses d20=delta. Its upper bound is
redundant since delta<=10. It yields the same A as EdgeOK. The directed
residue MUST NOT replace delta in (1) or (2).

For every finite simple graph G and pairwise distinct vertices v,u,w with
N_G(v)={u,w}, and for every valid (20,7)-coloring psi of the induced G-v,
let Ext be the set of all colorings f of G such that f(x)=psi(x) for every
x!=v. Then evaluation f->f(v) is a bijection from Ext to
A(psi(u)) intersect A(psi(w)). Consequently Ext is nonempty iff the neighbor
color distance is at most six, and its exact cardinality is given by (1).

## Definition and quantifier comparison

- C represented by Fin 20 has precisely one value for each residue. Signed
  subtraction must precede reduction, or use (b.val+20-a.val)%20; subtracting
  natural representatives first would truncate. Natural subtraction in
  7-delta, in contrast, can faithfully express max(0,7-delta).
- The contract's fixed-representative absolute edge predicate, the directed
  interval predicate, and delta>=7 are equivalent, including equal colors.
  Arbitrary integer lifts inside an absolute value are NOT equivalent.
- The pair theorem includes a=b and antipodal distance ten, and the interval
  endpoints seven and thirteen are inclusive.
- The graph assumes a valid deletion coloring, NOT a coloring of all of G.
  A total old map may have any unused placeholder old(v); it never enters
  either the neighbor condition or preservation off v.
- Distinct vertices u,w may have equal colors. No injectivity of psi is added.
- Preservation is for ALL old vertices, not just the two neighbors. No other
  edge at v exists; each old edge is justified by the deletion-coloring premise.
- Both logical directions and both inverses of the evaluation/insertion maps
  must be checked. Checking an existence-only sufficient rule misses the target.
- The generic local theorem removes unnecessary planarity/triangle-free/degree
  assumptions only from that lemma. It does not change them in the root.
- The implication from a favorable deletion coloring to a full coloring does
  NOT say all deletion colorings extend, and does NOT close the root.

## Separate required verification capabilities

Kernel: an actual source module and declaration must encode the above finite
pair theorems and graph bridge. No such compiled declaration is supplied here.
Freeze the source, imports, exact toolchain and dependency manifests before
execution, and record actual resource bounds, command, exit and output hashes.

Axiom/escape audit: inspect transitive axioms and imported declarations; reject
admitted gaps, opaque computational shortcuts or changed definitions not allowed
by the qualified policy. A successful compiler invocation alone is insufficient.

Statement faithfulness: compare the frozen obligation, this precise statement,
and the ACTUAL formal declaration, with the quantifier and representation map
above. The finite certificate verifies a finite color table; it is not a graph
bridge proof, a formal theorem, or an independently issued semantic review.

Required adversarial fixtures: equal colors; distance 6/7/10; pair (0,14);
palette endpoints; arbitrary old(v); invalid old edge; changed old color;
coincident neighbor colors at distinct vertices; and the C5 fixed-color failure
with a separate valid full C5 coloring. All-size graph closure cannot be inferred
from these finite fixtures alone.

## Actual registry/action suitability

research/verifiers.json registers lean-kernel, lean-axiom-auditor and
lean-faithfulness-reviewer under lean-*-fixture-v1 policies. It assigns
chatgpt-web-github to generation with NO verifier capability. Their mere names
are not an invocation or proof that the fixture policies cover this graph lemma.

The only file in the current .github/workflows directory is
web-candidate-gate.yml. Its three jobs validate Harness snapshot, packet schema
and candidate diff. It supplies no Lean/semantic/admission job or dispatch entry.
The corresponding fingerprint, trusted run and receipts remain null/empty in
the request. No workflow is changed to manufacture that capability.

The trusted coordinator must qualify the exact policies, provide the frozen
formal declarations and issue actual receipts under the declared trust domains;
then the obligation closure gate must validate those bindings. This document
requests that process without altering any records, EvidenceLink, Result or
Solution. It neither self-grants a verifier role nor requests bypass of a gate.
