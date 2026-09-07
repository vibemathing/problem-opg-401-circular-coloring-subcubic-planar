# Retained m01 branch tail: transport provenance and source-name map

Status: candidate_only. Date: 2026-09-07. No new mathematics.
Repository: vibemathing/problem-opg-401-circular-coloring-subcubic-planar.
Issue: #4. Discovery checkpoint comment: 5563461767.
Actual recovery base: 5f2a09d712c9ccc6578f082de1ac66cbd4ff6a32.

## Discovery and non-force synchronization

The original m01 PR #15 is merged. Its merged head was
cc976e9a3686ee680b494c3ef71ab16a40531d92, but the retained branch
web/attempt-opg401-a01-m01-critical-structure had subsequently advanced to
474017b75fbb72a52a554248260b2d025fd86b6d. The fresh compare showed eight
additional commits adding the eight draft files below, with no packet.
Their exact blobs were read before synchronization. They were absent
from the actual main tree and are not the later similarly numbered
m02-m06 main candidates. Some subject matter overlaps, but these are
separately preserved derivations, witnesses and certificate interfaces.
No already-merged file is duplicated or edited by this recovery.

The synchronized tree starts from the complete current main tree
3506333dbbd57f1af8b713611567e430c18d303e and adds exactly these eight
existing blobs. The two-parent synchronization commit is
 e23b66d528e8292abd9b886f19b62bced744ecff,
with old branch head and actual main as its parents. Updating the
candidate ref used force=false. Both histories and all main files
are preserved. The first commit-creation request had a connection
error; a fresh ref read showed no branch movement, and one bounded
retry returned the commit above. No unreadable write is treated as
a delivered candidate. No protected ref or workflow was changed.

## Exact payload manifest

The local SHA-256 calculation used the complete texts freshly returned
by GitHub. For each text, the computed Git blob SHA-1 equals the original
remote blob below. This binds the SHA-256 to the actual preserved bytes,
not to a paraphrase. No mathematical program was run.

Path: `research/artifacts/candidates/opg401-a01-m02-separated-pentagon-draft.md`
Candidate: `candidate:opg401-a01-m02-separated-pentagon-draft`
Bytes: 8444
SHA-256: `e65a9030ca46e694b006bc130785cce0d621672933e8e437cefcc9a1fde38268`
Git blob: `81a8a0c48974b53f07ec2d87e8a169efc5587797`

Path: `research/artifacts/candidates/opg401-a01-m03-cubic-square-draft.md`
Candidate: `candidate:opg401-a01-m03-cubic-square-draft`
Bytes: 9480
SHA-256: `2f1383f13bb8cbbb37be769998c80e6976371d1e1ca485386a817ebcc6194e88`
Git blob: `3b9e0cdda848dd4891e9a95486734cbcbc32af06`

Path: `research/artifacts/candidates/opg401-a01-m04-short-face-attachments-draft.md`
Candidate: `candidate:opg401-a01-m04-short-face-attachments-draft`
Bytes: 9750
SHA-256: `fe83b6a0f2cc9bc70bb5655db098f870021b3f34c28ad053825eb018c08617b5`
Git blob: `598093602d76f6c6ec6127fa282d10c003afb031`

Path: `research/artifacts/candidates/opg401-a01-m05-dual-charge-certificates-draft.md`
Candidate: `candidate:opg401-a01-m05-dual-charge-certificates-draft`
Bytes: 13710
SHA-256: `6d87c4b09af2104b53d54160b34b5afafa2f7ce4d46fa32f138dc5b156352ea5`
Git blob: `6ca55620c791a1de5e7b11a96328dc7066722506`

Path: `research/artifacts/candidates/opg401-a01-m06-sharp-twenty-vertex-draft.md`
Candidate: `candidate:opg401-a01-m06-sharp-twenty-vertex-draft`
Bytes: 10125
SHA-256: `dc6f6f8d33d6157005590af1794c38061506778cacdd3bc181a6df9295a04623`
Git blob: `1ccda9544f83c164fcb0c48e695f3689ae35e6d3`

Path: `research/artifacts/candidates/opg401-a01-m07-four-odd-face-reduction-draft.md`
Candidate: `candidate:opg401-a01-m07-four-odd-face-reduction-draft`
Bytes: 10026
SHA-256: `e0c87162ac56052bbcef80cb78b7eb685d5eec4091360f6c888a3871fc8ca548`
Git blob: `78d0528f125c1b0b6411952bef891fa8a8e9d307`

Path: `research/artifacts/candidates/opg401-a01-m08-six-terminal-cut-structure-draft.md`
Candidate: `candidate:opg401-a01-m08-six-terminal-cut-structure-draft`
Bytes: 11201
SHA-256: `eddd8cce0e3872fe9f18627488c5d9d36c38e4dc16d38a26003e42b110b4919f`
Git blob: `3fe285abcfc84b88d989af3d6e43eb720844c7cc`

Path: `research/artifacts/candidates/opg401-a01-m09-pentagonal-retraction-draft.md`
Candidate: `candidate:opg401-a01-m09-pentagonal-retraction-draft`
Bytes: 12578
SHA-256: `797d79669261f4abae73f422da22aff11bc3dde4af5e9f66ff97816594bb5c58`
Git blob: `2a129f22042d113aa8df7e012c521adc959f4e65`

## Source-name disambiguation and semantic limits

Within this retained draft sequence, unqualified references to m02,
m03, m04, m05, m06, m07, m08 and m09 refer respectively to the eight
-draft paths in the manifest, not to the differently named later
pentagon/core/carrier sequence on main. In particular m05 means the
dual-charge draft, m06 the twenty-vertex sharpness draft, and m07 the
four-odd-face draft. The separately supplied m07-three-port-propagation
is another candidate and is not one of these eight. References to m01
mean opg401-a01-m01-critical-structure.md already on main. References
to c01/c03/c05/c06/c08 and f01 retain their existing main meanings.
This mapping preserves provenance without rewriting mathematical text.

All preparation-time statements about having no packet are historical.
The recovery packet supplies the current transport binding, but does
not upgrade proof, counterexample, computation or formalization status.
The original files contain no standalone executed code or binary proof.
Their tables, graph instances, cut certificates, boundary warnings and
reproduction arguments travel as part of their original text. No Lean,
SMT, graph enumeration, mathematical solver or trusted verifier replay
was performed. Every mathematical claim remains pending/unverified.

## Ref census at recovery

Fresh historical PR metadata matched the retained heads for PRs
#5-#14 and #16-#20; these PRs are merged and have no post-merge head
advance in the enumerated refs. PR #15 was the exception above.
The previously empty c09 seed was reused for g02 PR #21, now merged
at 5f2a09d712c9ccc6578f082de1ac66cbd4ff6a32 after final-head checks.
The smoke branch web/attempt-web-20260906-opg401-a01-transport-smoke
remains at 4e4abebb1ec7145a575355db3b2887a8c7f8faf2. Its PR #3 is
closed without merge, and its inspected two-file patch is expressly
non-mathematical testing with no atomic claims. It is retired audit
history, not a pending research Candidate. It is retained, not deleted,
and no obsolete smoke packet is imported into the active inbox.

## Recovery transaction and remaining work

The eight files already co-reside on one branch and are transported
together as one ordered recovery bundle with exactly ONE new packet:
research/artifacts/web-inbox/opg401-a01-r01-retained-drafts.packet.json.
No existing packet is changed. The packet must receive its actual PR
binding and all three final-head checks before this recovery is counted
merged. This note is frozen pre-merge provenance, not a final receipt.

The supplied m07-three-port draft still requires its separate packet
and PR after this bundle. The final Issue #4 checkpoint will list actual
merge SHAs, all content hashes, retained refs and any outstanding work.
best_verified_candidate: none. best_verified_result: none.
Open obligations: obligation:opg401-root; obligation:opg401-z20-extension.
No EvidenceLink, Result, Solution, registry or truth ledger is modified.
