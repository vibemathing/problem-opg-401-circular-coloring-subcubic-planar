# V06 input identity and pending historical transport

Status: candidate_only. Repository: vibemathing/problem-opg-401-circular-coloring-subcubic-planar.
Read main: de730bc8fbebd354651f8768d2ed63a257745df9. Issue: 4.

The V03 nonuniform-switch and V04 steiner-pivot proofs on this main are
candidate inputs, not Evidence. Their exact actual-color selector semantics,
fixed separator, rotation and induced-cut accounting are retained by V06.
The live failed-route ledger was empty. No truth record is written here.

Two DIFFERENT V05 inputs exist:

1. The prior attachment opg401_v05_axis_exhaustion_candidate.zip has SHA-256
   d98ca564f1fecb0355cc65173d1004b111d5ab2dee19d812ab2418597d88507b.
   Its proof path is research/artifacts/candidates/opg401-a01-v05-axis-exhaustion/proof.md,
   SHA-256 9e6ea6fbb8b41a65f26bb81d79ecd25253b8c29d89baa337bcbd8d98903103a7.
   Its checkpoint path is research/artifacts/source-notes/opg401-a01-v05-checkpoint.json,
   SHA-256 9a2e366019450f14d784c40dc4c14cd877e3ef7f44b34ca42865d64b1aa9de4d.
   These bytes were read as input; no old computation is claimed reexecuted.
2. Fresh refs also exposed branch web/attempt-opg401-a01-v05-axis-blockers at
   34f07affc1212cd385e801d078b654a53ae33b48. Its four additions are check.py,
   input.json, proof.md and run.py below research/artifacts/candidates/opg401-a01-v05-axis-blockers/.
   The proof blob is 7e092f6cef74e19622be599574fa48d62831594a. This is a
   different graph/argument package; it has been read without overwriting it.
   No open PR existed at the time of the fresh read. No completed transport
   or replay of that branch is asserted by the V06 PR.

V06's input.json freezes its own actual colors. Its audit imports neither
old engine. Only the new bounded execution in execution.json is asserted.
The separator color description in V06's proof was corrected to distinguish
A's colors1,9,15,16 from B's colors1,9,14,16. The actual stored graphs,
color arrays, failure certificates and legal repair steps were unchanged.

The earlier matching-and-recolor attachment also remains a separate pending
payload, already inventoried in research/artifacts/source-notes/opg401-a01-v04-pending-intake.json.
This note does not transport either old attachment. The new PR is exclusively
V06 with one new packet. It is not a full historical transport reconciliation.

No hidden reasoning, complete conversation, private infrastructure inventory,
credentials, or opaque encoded payload is included. The certificate is a
plain finite JSON graph/edge/color/path object, not a verifier receipt.
