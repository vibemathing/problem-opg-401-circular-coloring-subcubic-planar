# Transport reconciliation: frozen intake and legacy provenance

Status: candidate_only. Date: 2026-09-07.
Task: transport existing material only; no new mathematical research.
Repository: vibemathing/problem-opg-401-circular-coloring-subcubic-planar.
Initial main: 5ba9f89a5c5272fd78e3e6e7a8a13e22d0bf0c42.
Coordination Issue: #4; intake checkpoint comment: 5563392187.

## Scope and source-of-state distinction

The two supplied artifacts are opg401_candidate_checkpoint.zip and
opg401-a01-m07-three-port-propagation.md. Their bytes are research
payloads, not authorities for current GitHub state. Current main,
refs, the open Issue and PR collection, and artifact trees were read
from GitHub. There were no open PRs at intake; PR #20 was merged.
The Attempt/Route/Graph and both obligations remain bound as declared.
The failed-route ledger was empty. Nothing here admits mathematics.

The legacy-continuation-checkpoint.json in this directory is an exact
historical archive member. Its old main, PR14 uncertainty and future
instructions MUST NOT be interpreted as current state. It is preserved
only for provenance. The legacy-artifact-manifest.json also preserves
archive member names and digests, not repository path names.

## Exact byte inventory and deduplication

SHA-256 values below were computed from the actual supplied bytes.
For the two existing copies, the computed Git blob SHA-1 was also
compared to the current main tree; both matched. This is content-address
reconciliation, not a mathematical check or an execution receipt.

| Archive or supplied item | Bytes | SHA-256 | Disposition |
|---|---:|---|---|
| g01.md | 9692 | f352ab0a3e464b448bb1d57c8770f40da96eb2c21b95a7ff0015f781565ae16e | Already on main; do not duplicate |
| f01.md | 10410 | 2963b681e2f49202b05a135f5651bb4ab4438aa8859a959308a64ece028c2d56 | Already on main; do not duplicate |
| g02-draft.md | 3979 | a01d293b7fcb9fa508fa61e36e9211d07d4b430b637c56e2a299d003d5dcdb42 | Transport unchanged in this g02 packet |
| continuation-checkpoint.json | 1198 | 8bb9271137d0f297b7f67636f68fe6db2591cbc028f8019f322d738d1937f9d3 | Historical JSON in this directory |
| artifact-manifest.json | 508 | c6dcc318b1167a32107a77a54a12bb37f5fed80cd632ec3425e443887fc2ee2a | Historical JSON in this directory |
| opg401-a01-m07-three-port-propagation.md | 14384 | 93b231e13eb3835870a5ccb8a4ff536bb5f232c7c1b6bb1805cf28c65f683a41 | Separate subsequent packet; not added by this PR |

Existing repository paths are:
research/artifacts/candidates/opg401-a01-g01-planar-k23.md
(Git blob 662d5835a39c252e9f6b36188f1f349e5831069a), and
research/artifacts/candidates/opg401-a01-f01-extension-bijection.md
(Git blob 3e3a808729e2de0d28bf8df04e2b8defeaa7dc60).

The recovered draft destination is
research/artifacts/candidates/opg401-a01-g02-rotation-count.md.
Its preparation-time header and next-action paragraph are preserved
verbatim. The new packet, not that historical header, defines its
current transport binding. Claim summaries only restate this draft.
The general parameter statement is explicitly outside the root's
fixed (20,7) specialization; no ProblemContract is changed.

## Existing branch and uncertain-write reconciliation

The ref web/attempt-opg401-a01-c09-k23-boundary was an unused seed at
 d0f1000ba8b4378d91a1946c417ac9947360af2e.
The fresh compare against initial main returned ahead_by=0,
behind_by=8 and files=[]. It contained no lost candidate or packet.
It is reused by a non-force fast-forward to initial main before
adding the recovered g02 material; no second K2,3 seed is created.
Historical merged branches are retained, not deleted or force-updated.

The previous uncertain f01 transport is no longer an open transaction:
its exact artifact is in main and current open PR enumeration is empty.
The latest previous checkpoint, Issue comment 5560848439, is readable.
The current transaction must still receive a real PR binding and all
three required final-head checks before merge is counted successful.

## Privacy, execution and coverage

The archive contained exactly the five named regular text files.
There was no separate untransported calculation code, input/output
pair, Lean/SMT source, compiled proof, verifier receipt or full paper.
The mathematical witnesses, definitions, semantic qualifications and
reproduction arguments reside inside the drafts and are preserved.
No hidden reasoning transcript, full chat, credentials, machine paths
or raw service logs are copied. The ZIP container itself is not an
additional mathematical result and need not be duplicated remotely.

No mathematical computation, enumeration, Lean or SMT replay occurred
in this transport task. Their verification remains pending/unverified.
Hashing and text preparation are transport operations only. Existing
formalization ToolPlans keep their original not-executed status.

This is a frozen INTAKE record, not the final completion checkpoint.
After the g02 merge, fresh-read main and transport m07 in its own PR.
The final Issue checkpoint and reconciliation note will list actual
heads, checks, merge SHAs, content hashes and remaining transactions.
best_verified_candidate: none.
Open obligations: obligation:opg401-root; obligation:opg401-z20-extension.
