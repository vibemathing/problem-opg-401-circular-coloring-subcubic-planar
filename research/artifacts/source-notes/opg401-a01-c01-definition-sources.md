# Definition and source-faithfulness note for c01

Status: candidate_only. Retrieved 2026-09-06.
Bound target: obligation:opg401-z20-extension.
Repository base: 96b12a5204c72f49d26dfa9cf620e530489d821d.

## Frozen repository sources

The canonical ProblemContract is
problem-library/records/canonical-problems.jsonl, contract SHA-256
76b2207954d4831261d0a61359a19e803cf8d913301756673c4c5ab962d8c8d6.
It quantifies over finite simple triangle-free planar graphs of maximum
degree at most three and explicitly asks for (20,7)-colorings.
The target record is in research/records/obligation-graphs.jsonl with
statement SHA-256
16533194e20493e83312edbc99b93714f07282d4e65bb58c4cee1c734fa7594e.

The phrase "using cyclic representatives" is made explicit in c01:
fixed representatives or modular difference in {0,...,19}, NOT
arbitrary lifts. Shortest circular distance is separately denoted delta.
The upper bound 13 in A is redundant for delta but not for a directed
residue. These equivalent conventions give A(a)=a+{7,...,13}.
The contract and target are not edited.

## External primary-source comparison

1. X. Zhu, author-hosted problem page,
https://www.math.nsysu.edu.tw/~zhu/open-problems/chic-k3free-planar.htm
The indexed page states the same maximum-degree-three, triangle-free
planar circular-coloring question with bound 20/7. Relation: exact
mathematical target, after the repository's finite/simple convention.
The page is historical and also lists fractional-coloring conjectures.
It is not a current-status certificate, a proof, or novelty evidence.
A direct open returned an internal fetch error; this comparison uses
the returned indexed source excerpt, not a claimed full-page download.

2. X. Zhu, "The fractional version of Hedetniemi's conjecture is true",
European Journal of Combinatorics (2011),
https://doi.org/10.1016/j.ejc.2011.03.004
The indexed primary article excerpt defines circular (p,q)-coloring by
a map to {0,...,p-1} with edge differences between q and p-q, inclusive.
Relation: exact definition used in c01; no product-graph theorem from
this article is invoked. The full article was not audited.

3. Z. Dvorak, J.-S. Sereni, J. Volec, "Subcubic triangle-free graphs
have fractional chromatic number at most 14/5",
https://arxiv.org/abs/1301.5296
and https://doi.org/10.1112/jlms/jdt085
The abstract concerns FRACTIONAL chromatic number. It cannot be
substituted for a theorem about circular chromatic number or the
specific local allowed-color intersection. Relation: different
parameter; not a proof node covering the contract.
Likewise the abstract of Dvorak, Lidicky, Postle,
https://arxiv.org/abs/2204.12683
concerns fractional 11/4-colorability, despite its shorter title.

4. R. C. Brewster and B. Moore, "Characterizing circular colouring
mixing for p/q<4", Journal of Graph Theory 102 (2023), 271-294,
https://doi.org/10.1002/jgt.22870
and https://arxiv.org/abs/2008.12185
The available abstract studies recoloring between existing colorings.
It does not supply a coloring of every graph in this contract class.
Relation: possible later recoloring background, not a closed gap.
No theorem from it is a premise of c01; no assumption of universal
single-vertex recoloring connectivity is made.

## Reuse decision and limitations

The local intersection follows directly from a seven-element modular
interval and is derived in full rather than attributed as a new
literature theorem. The small search above did not establish novelty,
nor does it establish the current global problem status.
No PDF was analyzed, no full paper copied, and no external code run.
No source hit is mathematical verification of the generated candidate.
The remaining gap is graph-class reducibility/recoloring and, beyond
that, the global root proof with the required verification capabilities.
