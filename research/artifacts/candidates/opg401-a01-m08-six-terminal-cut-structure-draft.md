# Small pair cuts, six odd faces, and a rejected counterexample construction

Status: candidate_only. Transport status: working draft for a subsequent immutable packet.
Primary owner: math-derivation.
Candidate: candidate:opg401-a01-m08-six-terminal-cut-structure-draft.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1.
Target: obligation:opg401-root.
Local dependency remains open: obligation:opg401-z20-extension.
No program run, new packet, final PR state, verifier receipt, or root closure is asserted.

## 1. Freeze the small-pair-cut graph

Let H be a finite connected undirected multigraph. Let T be exactly its odd-degree vertices, with even cardinality at least four. Suppose every cut containing an odd number of T has at least five edges. The dual of a connected simple triangle-free plane graph has this property by m05.

For distinct i,j in T let lambda(i,j) be the minimum cut size among vertex sets U with U intersect T={i,j}. Define F on T by the edge ij exactly when lambda(i,j)<=6. Pair cuts are even, since T is the odd-degree set. This definition does not use a chosen coloring or charge signing.

Claim P1 (claim:opg401-m08-pair-cut-degree):
F has maximum degree at most two and has no triangle. Thus its components are paths and cycles of length at least four, including isolated vertices as trivial paths.

Suppose a terminal i had three F-neighbors j,k,l. Choose cuts realizing the pairs ij,ik,il, each of size at most six. Their membership codes on these four terminals are 111,100,010,001. The four corresponding atoms each contain one terminal, so each boundary has size at least five. Any two of the displayed codes have Hamming distance two. The edgewise inequality from m07 says the sum of the three chosen cut sizes is at least the sum of those four atom boundaries, at least twenty. But it is at most eighteen, a contradiction.

If i,j,k formed an F-triangle, choose the three pair cuts ij,jk,ki. The three terminal codes are 101,110,011; every other terminal has code 000. Since |T|-3 is odd, the entire 000 atom also has an odd number of terminals. These four atoms each have boundary at least five, and their four codes again have mutual Hamming distance two. The identical edgewise inequality contradicts the upper bound eighteen. This proves P1 for every even |T|>=4, not just six.

## 2. Relation to the exact charge problem

For the principal charge family b_t=10*sigma_t, sigma_t in {-1,1}, and zero charges on nonterminals, an F-edge forces its terminal signs to be opposite. If two same-sign terminals were the only terminals in a realizing cut of size at most six, that cut would have charge magnitude twenty but capacity at most eighteen.

On primal embeddings whose even faces have length at most six and odd faces length at most nine, these are all possible charges in m05: even faces permit only zero, and odd faces permit only plus/minus ten. For longer faces this is a restricted sufficient-construction family, not automatically the full coloring problem; their other allowed charges must be retained.

Consequently an odd cycle of F is a complete obstruction to this principal-charge family. Under the stated exact-domain length bounds it would be a genuine noncolorability certificate, provided the graph, embedding, and all the realizing cuts were explicitly verified. No such subcubic counterexample is claimed here.

For six terminals, P1 leaves only a five-cycle as a possible odd cycle. If no such cycle occurs, F is bipartite, and its components can be two-colored with three terminals of each sign: even paths/cycles are balanced, and the number of odd-order path components is even, so their one-vertex imbalances can be paired with opposite choices. This satisfies the pair-cut requirements but does NOT yet check the three-versus-three cuts. For those, a same-sign triple needs boundary at least eleven at capacity three. The remaining condition is explicitly retained.

## 3. An exact equality signature for a five-cycle of small pair cuts

Assume |T|=6 and that t1,t2,t3,t4,t5 form a cycle in F. Let t6 be the remaining terminal. For each cyclic consecutive pair ti,t(i+1), choose a cut U_i of size at most six with exactly those terminals.

The code of t_j in these five cuts has ones precisely in positions j-1,j, modulo five; t6 has code 00000. Any two terminal codes differ in at least two positions. Let B_j be the atom containing t_j. Each B_j has one terminal and therefore boundary at least five. Applying the same edgewise count gives
  sum_{i=1}^5 |delta(U_i)| >= sum_{j=1}^6 |delta(B_j)| >=30.
The left side is at most thirty. Hence every chosen pair cut has size six, every terminal atom has boundary five, and every edge attains equality in the Hamming-distance count.

Claim P2 (claim:opg401-m08-five-cycle-equality-signature):
Any such five-cycle has all the equality properties above. In addition:
- No edge joins the atoms of two nonconsecutive rim terminals, whose codes have distance four rather than two.
- No edge joins two distinct nonterminal-code atoms.
- An edge from a terminal-code atom to a nonterminal-code atom can change exactly one code bit.
- Direct edges between terminal atoms can only follow the five rim adjacencies or connect a rim atom to the t6 atom.

These statements concern edges crossing the atoms; edges inside an atom are not excluded.

If all nonempty proper cuts of H also have size at least four, each terminal atom and its complement are connected. For a disconnected terminal atom, its component containing the unique terminal already has boundary at least five, while any other component has boundary at least four, contradicting its total boundary five. For a disconnected complement, an odd-terminal component has boundary at least five and another component at least four, giving the same contradiction. Triangle-free simple plane duals have the required all-cut bound: a nonempty primal boundary is Eulerian and contains a cycle of length at least four.

The signature does not itself prove that a five-cycle is impossible when every dual face has length at most three. Establishing or disproving that root-specific realization is a distinct remaining topological question; no missing contraction or triangulation argument is silently filled in.

## 4. The non-subcubic model that attains the signature

Consider the plane multigraph H0 on center t0 and rim t1,...,t5. Its rim is a five-cycle with two parallel copies of each rim edge; each center-to-rim spoke has one copy. Every vertex has degree five. The dual primal graph is exactly the eleven-vertex subdivided-spoke wheel W described in m07: five rim vertices, five degree-two spoke vertices, and one degree-five center. Its six faces are all pentagons.

Every odd cut of H0 has size at least five. Singleton cuts have size five. A three-vertex set either contains three rim vertices, whose induced rim weight is at most four, or the center and two rim vertices, whose internal weight is at most four. Since its degree sum is fifteen, its boundary is at least seven. Complements give all remaining odd cases.

For a consecutive rim pair the cut size is 5+5-2*2=6. Thus its F is the five-cycle on the rim plus an isolated center. This supplies the exact odd-cycle obstruction to principal charges. H0 has an outer dual face of length five, which is the primal degree-five vertex and violates the root's maximum-degree-three hypothesis.

This example is a diagnostic of the domain condition, not a root counterexample.

## 5. Two natural attempts to repair the degree violation

Triangulate the outer pentagon of H0 by drawing noncrossing diagonals t1-t3 and t1-t4.

First attempt: add one copy of each diagonal. The two diagonals change the parity of t3 and t4 to even; t1 changes by two and stays odd. The resulting dual has only four odd vertices. Its primal is simple and triangle-free because adding dual edges cannot reduce any cut, and H0 had no cut smaller than five. Every dual face now has length two or three, so the primal is subcubic. But m07 now supplies a coloring. The construction loses the required six-terminal obstruction instead of producing a root counterexample.

Second attempt: add two copies of each diagonal, preserving the six terminal parities. Call the resulting plane multigraph H1. The degree sequence in order t0,t1,t2,t3,t4,t5 is
  5,9,5,7,7,5.
Again all dual faces have length two or three, and no cut is smaller than five, so its primal lies in the root graph class.

This second repair also fails as a counterexample construction. Assign charge +10 to {t0,t2,t5} and -10 to {t1,t3,t4}. The same-sign pair boundaries are:
  {t0,t2}:8; {t0,t5}:8; {t2,t5}:10;
  {t1,t3}:12; {t1,t4}:12; {t3,t4}:10.
The positive triple has boundary eleven, as does its negative complement: its three degrees sum to fifteen and its two internal spokes have total weight two, so 15-2*2=11.

Every odd cut still has size at least five, because H1 is obtained from H0 by adding edges. We can therefore check every charge-cut case without a solver:
- One or five terminals have charge magnitude ten and boundary at least five.
- A same-sign pair or its four-terminal complement has magnitude twenty and boundary at least eight, as listed.
- A mixed pair or its complement has charge zero.
- A same-sign triple has magnitude thirty and boundary eleven.
- A mixed triple has magnitude ten and boundary at least five.
- Empty and full sets have charge zero.
All satisfy |b(U)|<=3|delta(U)|. There are no nonterminal vertices in H1, so these cases exhaust all vertex subsets. The integral criterion m05 gives the required capacity-three flow and hence a (20,7)-coloring of its primal.

Claim P3 (claim:opg401-m08-repaired-wheel-colorable):
Both of these explicit subcubic repairs of the non-subcubic obstruction are colorable. The second assertion has a complete cut-feasibility proof, not just loss of one necessary obstruction.

## 6. Root-oriented continuation

P1 organizes low pair-cut requirements into paths and cycles rather than an arbitrary constraint graph. P2 freezes the exact saturation data of the smallest odd-cycle failure. P3 eliminates two concrete attempts to carry the degree-five obstruction into the subcubic domain. The remaining root-specific tasks are the topological realization of these signatures and the larger-terminal charge cuts; neither is discharged by merely knowing that F is bipartite.

Sources are the frozen contract, m05's complete integral cut theorem, and m07's explicitly proved code-count argument and degree-five boundary witness. No outside packing theorem, formal build, max-flow run, enumeration, or verifier receipt is used. No novelty claim is made.

best_verified_result: none. best_verified_candidate: none.
Open obligations: obligation:opg401-root; obligation:opg401-z20-extension.
Next action: analyze the P2 signature under the dual facial-length-at-most-three restriction, while retaining all m05 charge domains for longer primal faces. A finalized packet must use a freshly observed actual main and exact content hashes; this working draft does not assert that its transport is complete.
