# V01 definition and source comparison

Verdict: candidate_only. Read base: 165b7db2b8cdb65fd06121494f24f21fb690ad1f.
The canonical ProblemContract has not changed. C01 identifies d_20 with
shortest circular distance, while the edge condition may use a directed
residue or absolute difference of fixed representatives. V01 proves these
edge predicates equivalent; it does not identify their numerical distances.

Primary bibliographic cross-check, retrieved 2026-09-07:
Andre Raspaud and Xuding Zhu, List circular coloring of trees and cycles,
Journal of Graph Theory 55 (2007), 249-265, DOI 10.1002/jgt.20234.
https://onlinelibrary.wiley.com/doi/abs/10.1002/jgt.20234
Its abstract defines colors in {0,...,p-1} with inclusive edge bounds
q <= |phi(x)-phi(y)| <= p-q. This matches the canonical definition.
Only that definition is used; its list-coloring theorems are not imported.
No novelty claim is made for the local interval calculation.

Frozen read inputs: C01-C08, the canonical record, current obligation graph,
failed-route ledger (empty), and Issue #4 with its latest checkpoint.
Harness is now 1.2.4; the old transport checkpoint's 1.1.2/main fields are
historical. Current snapshot/importer binding was read from immutable
HARNESS_SNAPSHOT_HISTORY.json and WEB_BOOTSTRAP.md.

The user's conditional command request is fulfilled by foreground bounded
standard-library execution, not an asserted GitHub command capability.
No central-service receipt, repository verifier identity, mathematical
EvidenceLink, Result, Solution, or new admitted obligation is created here.
