# An explicit twenty-vertex sharpness witness for the bound 20/7

Status: candidate_only. Transport status: working draft for a subsequent immutable packet.
Primary owner: math-derivation.
Candidate: candidate:opg401-a01-m06-sharp-twenty-vertex-draft.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1.
Target: obligation:opg401-root.
Local dependency remains open: obligation:opg401-z20-extension.
This is a sharpness candidate, NOT a counterexample to the root. No program run, verifier receipt, new packet, or completed PR is asserted.

## 1. Explicit graph, with no external identification needed

Define D on vertices 0,...,19. Include the twenty cyclic edges i-(i+1) modulo20 and the following ten additional edges:
  0-10, 1-8, 2-6, 3-19, 4-17,
  5-15, 7-14, 9-13, 11-18, 12-16.
The additional edges form a perfect matching, are not cyclic edges, and have distinct endpoints within each pair. Thus D is finite, simple, connected and cubic.

A triangle cannot contain two matching edges, since two edges in a triangle share a vertex. A triangle with one matching edge would require its endpoints to be two steps apart on the twenty-cycle. The listed matching distances are four, seven and ten, never two. The twenty-cycle has no triangle by itself. Therefore D is triangle-free.

For planarity, put the twenty-cycle on a circle. Draw the chords
  0-10, 1-8, 2-6, 11-18, 12-16
inside the circle, and draw
  3-19, 4-17, 5-15, 7-14, 9-13
outside it. Within each of these two lists the endpoint pairs are nested or disjoint, never alternating, so they can be drawn without crossings in their respective disks on the sphere. This gives a plane embedding after choosing an outer point away from the drawing.

The following twelve oriented boundary walks are all pentagons of this embedding:

| face | cyclic boundary |
|---|---|
| F1 | 2,3,4,5,6 |
| F2 | 19,3,2,1,0 |
| F3 | 9,13,12,11,10 |
| F4 | 12,13,14,15,16 |
| F5 | 0,1,8,9,10 |
| F6 | 1,2,6,7,8 |
| F7 | 3,19,18,17,4 |
| F8 | 4,17,16,15,5 |
| F9 | 10,11,18,19,0 |
| F10 | 11,12,16,17,18 |
| F11 | 13,9,8,7,14 |
| F12 | 14,7,6,5,15 |

Every edge occurs in two opposite directions in this table. A further direct disk audit avoids assuming planarity just from a numerical Euler check: F1,F6,F5,F9,F10,F4 form one chain of six pentagons, each new pentagon glued along one boundary matching edge and adding three new vertices. Its boundary is the entire twenty-cycle. The other chain F2,F7,F8,F12,F11,F3 forms the other disk in the same way, with the opposite boundary orientation. Gluing these two disks gives the claimed embedding. The counts are n=20,m=30,f=12 and n-m+f=2.

No graph library, enumeration, or drawing recognition is a premise of this construction.

## 2. An explicit coloring at the requested bound

Claim S1 (claim:opg401-m06-explicit-coloring):
  phi(i)=7i modulo20
is a (20,7)-coloring of D.

Each forward cyclic edge, including 19-to-0, has directed difference seven. On the matching edges the cyclic index separations are four, seven, or ten, up to sign. Multiplication by seven sends these to eight, nine, or ten, up to sign, modulo20. The corresponding shortest color distances are eight, nine, or ten and hence legal.

This gives a complete constructive witness for the upper bound on this graph. The next section shows why the same example prevents silently strengthening the root's constant.

## 3. No coloring of this graph has ratio below 20/7

Claim S2 (claim:opg401-m06-sharp-lower-bound):
For every integers p>=2q>0, if D has a (p,q)-coloring, then p/q>=20/7. Together with S1, the circular chromatic number of this explicit graph is 20/7.

It suffices to rule out p/q<20/7. If necessary double p,q and all palette labels, preserving their ratio, so that the palette size P is even. Write Q for the resulting lower edge bound and c=P/2-Q. For each oriented edge put
  h_e=[phi(v)-phi(u)]P-P/2,
so |h_e|<=c.

As in the fully proved dual formulation m05, every pentagonal face has centered boundary sum b_f congruent to P/2 modulo P. Its absolute value is at most 5c. Under the putative ratio P/Q<20/7, one has c<3P/20, so 5c<3P/4. Therefore any such b_f must be either P/2 or -P/2; the next possible congruent magnitudes are 3P/2 and are excluded. If this bound is too small even to permit P/2, nonexistence is already immediate. In all remaining cases the asserted coloring supplies these two signs.

Summing all face boundary sums cancels every edge, so the twelve signs consist of six positive and six negative faces. Let U be the six positive faces, and let K be the set of primal edges separating a positive face from a negative one. Summing the divergences on U gives
  3P <= c*|K|.

At each cubic vertex there are three distinct incident faces in the displayed embedding. Among three cyclically ordered binary signs, at most two consecutive pairs differ. Hence at most two incident edges belong to K. Summing over twenty vertices gives 2|K|<=40, or |K|<=20. Thus
  3P <= 20c = 10P-20Q,
which rearranges to 20Q<=7P, contradicting P/Q<20/7.

This is an argument about every rational coloring ratio, not a search over a bounded set of palettes. Doubling an odd palette did not assume a smaller denominator or change the ratio. The proof uses only the explicit embedding, the modular edge condition, and finite face/edge counting.

The statement is a generated sharpness proof, not an admitted lower-bound Result. It does not deny the root at equality: S1 explicitly supplies equality.

## 4. A checkable centered-flow certificate for S1

Orient each cyclic edge from i to i+1 modulo20. Its centered increment for S1 is -3. Orient each matching edge from its smaller endpoint to its larger endpoint. In the displayed matching order the centered increments are
  0, -1, -2, 2, 1, 0, -1, -2, -1, -2.

Using the oriented face table gives b_f=+10 on
  F2,F3,F7,F8,F11,F12,
and b_f=-10 on
  F1,F4,F5,F6,F9,F10.
These twelve values can be reconstructed by five additions per row; they are hand-derived certificate entries, not output of an executed verifier.

The separating edges K for this sign assignment are exactly the twenty cyclic edges. Each matching edge has two face signs that agree. Both same-sign face subgraphs are six-vertex paths, namely the two pentagon chains listed in Section 1. The positive-to-negative cut has twenty edges, and the sixty units of face charge saturate its capacity-three bound.

## 5. Saturation constrains every optimal coloring of this graph

Claim S3 (claim:opg401-m06-optimal-tight-hamiltonian):
In every (20,7)-coloring of D, the edges separating the positive and negative pentagonal charges form a directed tight Hamiltonian cycle. In particular all twenty vertex colors are distinct.

At P=20,Q=7, the inequalities in Section 3 read
  60 <= 3|K| <= 60.
Equality forces |K|=20 and makes every vertex incident to exactly two edges of K. It also forces every crossing edge's centered flow to have magnitude three, with consistent flux from positive to negative faces. Therefore K is a spanning two-regular subgraph consisting of disjoint cycles, and every edge on it has color difference seven or thirteen.

Orient each interface edge with its positive face on the left. Its centered increment is three, by the saturated flux statement, so its color increment in that direction is thirteen. Reversing all these interface directions gives tight arcs of increment seven. At a cubic vertex with two incident interface edges, the local positive/negative sectors show that one interface edge enters and the other leaves. Thus each component is a directed tight cycle, not merely an undirected cycle of tight edges with arbitrary orientations.

On a directed tight cycle of length L, returning to the starting color requires 7L=0 modulo20. Since seven is invertible modulo20, twenty divides L. The components of K are vertex-disjoint simple cycles on a total of twenty vertices. Each has positive length at least twenty, so there is exactly one, and it is Hamiltonian. Its colors advance by seven and visit every residue once.

This necessity is special to the saturated twenty-vertex all-pentagon example. It is NOT a claim that every graph in the root class has a tight Hamiltonian cycle or that all (20,7)-colorable graphs are Hamiltonian. Non-Hamiltonian members of the class are not excluded by the root conjecture.

## 6. Research consequence and checkpoint

The constant 20/7 cannot be improved uniformly over the frozen class: the explicit graph satisfies all of its hypotheses and has the displayed sharpness argument. Any root proof by reducible configurations must still color this graph. In particular, proving every wholly cubic pentagon has an arbitrary-fixed-boundary extension, or requiring strictly positive slack everywhere, would be an unjustified strengthening and must be tested against this example.

The example also supplies a stringent positive certificate fixture for m05's dual interface: the graph, embedding, colors, edge increments, face signs and saturated cut are all explicit. A future checker can validate each layer separately. Such a checker has not been executed here, and generator-produced fixture data is not a trusted verification receipt.

No external graph name, classification theorem or literature claim is needed for the proof. Prior-art comparison remains necessary before making any novelty assertion; none is made. Sources are the frozen coloring contract, m05's explicitly proved centered-flow equivalence, and the elementary tight-cycle modular argument from c06.

best_verified_result: none. best_verified_candidate: none.
Open obligations: obligation:opg401-root; obligation:opg401-z20-extension.
Next target: allow the saturated sharp configuration in the discharging framework while proving a favorable-boundary or global charge-selection theorem for other minimal-obstruction cases. Finalizing this draft requires a fresh actual main, exact content hashing, one immutable packet, and the required candidate-only PR transport. No such finalization is asserted by this file alone.
