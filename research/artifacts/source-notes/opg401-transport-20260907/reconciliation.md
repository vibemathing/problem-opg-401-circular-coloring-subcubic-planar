# Transport reconciliation: final payload and completion protocol

Status: candidate_only. Date: 2026-09-07. Transport only; no new mathematics.
Repository: vibemathing/problem-opg-401-circular-coloring-subcubic-planar.
Unique research Issue: #4.
Fresh base for this final payload: 20b2f42b1d308a4fb464599c6c5c0401818f7ad6.

## 1. Scope and completed recovery transactions

The audit started from actual main
5ba9f89a5c5272fd78e3e6e7a8a13e22d0bf0c42, not a remembered earlier SHA.
The open-PR collection was empty. Issue #4 was the single research
Issue. The admitted Attempt/Route/Graph/root/local objects and current
branch protection were read. Old descriptive pending-smoke labels were
not treated as missing admission or permission.

PR #21 recovered the older g02 draft plus its historical archive
checkpoint and manifest, with an intake note. The empty c09 seed was
reused after a force=false fast-forward. Its transaction is:
branch: web/attempt-opg401-a01-c09-k23-boundary
base: 5ba9f89a5c5272fd78e3e6e7a8a13e22d0bf0c42
final head: 066711278e09313b384ecfd3a971e5a0798a0ec3
workflow: 34070362089
web-attempt-packet: 101586438923, completed/success
web-harness-snapshot: 101586438882, completed/success
web-pr-diff-boundary: 101586438701, completed/success
squash merge: 5f2a09d712c9ccc6578f082de1ac66cbd4ff6a32
transport COMMENT review: 5127183272
Exactly five new allowed files, including one new packet, were added.

PR #22 recovered eight previously unpacketized drafts from the retained
m01 branch. They were found by comparing its current head to the head
of the already merged PR #15, rather than assuming a merged PR meant
the retained branch had no later work. Its transaction is:
branch: web/attempt-opg401-a01-m01-critical-structure
original orphan head: 474017b75fbb72a52a554248260b2d025fd86b6d
base: 5f2a09d712c9ccc6578f082de1ac66cbd4ff6a32
non-force two-parent synchronization: e23b66d528e8292abd9b886f19b62bced744ecff
source-note commit: 50aad3a874384418c61733159eca67466dbc1fa5
packet commit: 065fd4aaa4177383b911e77edfe4e78f8b0cf85b
PR-binding commit / final head: f5516bd648ca8b796fea040a54eea06146c5489c
workflow: 34071266214
web-attempt-packet: 101588938698, completed/success
web-harness-snapshot: 101588938739, completed/success
web-pr-diff-boundary: 101588938794, completed/success
squash merge: 20b2f42b1d308a4fb464599c6c5c0401818f7ad6
transport COMMENT review: 5127238315
Exactly ten new allowed files, including one new packet, were added.
All eight original mathematical blobs were retained without edits.

Each merge was followed by an actual main-ref read. These check IDs
were also read from their actual final-head check-runs endpoints, not
inferred from a prior head or from an overall green PR summary.

## 2. The final research payload

The remaining supplied file is
research/artifacts/candidates/opg401-a01-m07-three-port-propagation.md.
Its exact original UTF-8 bytes are preserved:
bytes: 14384
SHA-256: 93b231e13eb3835870a5ccb8a4ff536bb5f232c7c1b6bb1805cf28c65f683a41
Git blob: c68e525050e89e6e1f5239f89e2f7afa4e55344b
Candidate: candidate:opg401-a01-m07-three-port-propagation.

Its header's cycle base 5ba9f89a5c5272fd78e3e6e7a8a13e22d0bf0c42
records when it was prepared; it is not overwritten with a false
preparation date. The accompanying packet uses this transaction's
fresh base 20b2f42b1d308a4fb464599c6c5c0401818f7ad6. The new branch is
web/attempt-opg401-a01-m07-three-port-propagation; a fresh matching-ref
query returned no pre-existing branch before creation.

The m07 draft's unqualified m01,m02,m05,m06 dependencies refer to:
research/artifacts/candidates/opg401-a01-m01-critical-structure.md;
research/artifacts/candidates/opg401-a01-m02-pentagon-122.md;
research/artifacts/candidates/opg401-a01-m05-pentagon-clusters.md;
research/artifacts/candidates/opg401-a01-m06-single-ear-boundary.md.
They are NOT the differently named -draft sequence recovered by PR #22.
The distinction is necessary for source faithfulness; no theorem is
changed by making the names explicit. The existing c01 and c03 paths
retain their original meanings. All are generated inputs, not Evidence.

The new packet is research/artifacts/web-inbox/opg401-a01-m07.packet.json.
It adds no new obligation or verifier. Four claim summaries restate
the existing draft's absorption, three-port reduction, nine-vertex
boundary and distinct-terminal claims. Its remaining forced-equality
questions remain open; this transport task does not investigate them.

## 3. Payload coverage, deduplication and immutable provenance

The attached ZIP contained five regular text members. The g01 and f01
copies match existing main files byte-for-byte and were not re-added:
research/artifacts/candidates/opg401-a01-g01-planar-k23.md
SHA-256 f352ab0a3e464b448bb1d57c8770f40da96eb2c21b95a7ff0015f781565ae16e;
research/artifacts/candidates/opg401-a01-f01-extension-bijection.md
SHA-256 2963b681e2f49202b05a135f5651bb4ab4438aa8859a959308a64ece028c2d56.

The other archive payloads are covered by PR #21. Their exact hashes,
source member names and historical/current-state distinction are in
research/artifacts/source-notes/opg401-transport-20260907/intake.md.
The eight remote draft payloads, their exact SHA-256/Git-blob pairs
and source-name mapping are in
research/artifacts/source-notes/opg401-transport-20260907/retained-tail.md.
The two historical JSON archive members remain explicitly historical
and do not direct current operations. The ZIP wrapper itself is not
an additional mathematical result to duplicate in the repository.

All identified proofs, graph/color examples, counterexample proposals,
certificate designs, semantic qualifications, reproduction directions
and mathematical checkpoints are inside these preserved texts.
No separate untransported enumerator code, inputs/raw outputs, Lean/SMT
source, compiled proof, theorem-prover log or trusted receipt was found.
Text preparation and hash calculations used for transport are not
mathematical execution and are not represented as verification logs.
No hidden reasoning transcript, full chat, credentials, machine paths
or full external paper is copied. Original mathematical execution
statuses stay pending/unverified or not-executed as applicable.

## 4. Retained refs and retired smoke

At the census, heads of the historical merged PRs #5-#14 and #16-#20
matched the corresponding retained branch refs. The m01 exception
was recovered by PR #22. The c09 seed now holds merged PR #21.
Do not confuse squash-unreachable source commits with untransported
content: use the actual PR status and content hashes, not ancestry alone.

One retired non-mathematical smoke branch remains:
web/attempt-web-20260906-opg401-a01-transport-smoke
head 4e4abebb1ec7145a575355db3b2887a8c7f8faf2, PR #3 closed without merge.
Its inspected two-file diff contains only a transport smoke with no
mathematical claims. It is not an active Candidate transaction and is
not imported into the current inbox. Keep the ref for audit history;
no force push or branch deletion is performed. The final receipt must
explicitly disclose it instead of claiming that every historical ref
is merged.

## 5. Completion is decided after this file's own transaction

This is a frozen pre-merge reconciliation note, not a prediction that
its containing PR has passed or merged. After the real PR number is
known, fill the packet, read all three checks on the final head,
inspect the allowed-file diff, and squash-merge only under protection.
Then fresh-read main, the open PR collection, all candidate refs, and
the recovered paths. Every expected SHA-256 must be backed by matching
actual main content. Check for any newly advanced retained branch.

The final checkpoint is appended to the same Issue #4 and then read
back. It records the final main, this transaction's actual commit/PR/
check/merge identifiers, all new and deduplicated path hashes, the
retired smoke ref and any remaining work. This avoids inventing a
self-referential merge SHA inside a file before its own merge exists.
Only an empty untransported research-material list and no pending
Candidate transaction justify declaring the transport reconciliation
complete. Any interruption must preserve the exact outstanding paths
and use NONTERMINAL_TRANSPORT_CHECKPOINTED, not a completion claim.

Existing checkpoints for this audit are Issue comments 5563392187
(intake), 5563461767 (orphan-tail discovery), and 5563554074 (tail merge).
All future continuation stays in Issue #4.

verdict: candidate_only.
best_verified_candidate: none. best_verified_result: none.
Open obligations: obligation:opg401-root; obligation:opg401-z20-extension.
No transport operation, Actions check or review closes mathematics.
