# V15: rigidity of two-class global quotients and the exact three-map CSP

Status: NONTERMINAL_CHECKPOINT. Verdict: candidate_only.
Candidate: candidate:opg401-a01-v15-two-class-rigidity.
Repository: vibemathing/problem-opg-401-circular-coloring-subcubic-planar.
Attempt: attempt:web-20260906-opg401-a01. Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1. Target: obligation:opg401-root.
Read base: 6515f3e2178aefd2c2b34890e5d3f0afc90310ae (V14/PR38 merged).

All four residual classes and both admitted obligations remain open. V03--V14
are candidate inputs, not Evidence. This note attacks the exact next question:
can a single class-oblivious palette map preserve two non-tight distance
classes, or can the three V14 maps simply be chosen independently by vertex?
It does not repeat unit-shift, parity, support-cap, single-hit, or one-class
quotient searches.

## 1. Frozen objects

Colors are Z20 with representatives 0,...,19. Put
  delta(a,b)=min([b-a]_20,[a-b]_20).
An edge is legal exactly when delta is in {7,8,9,10}. The original region O
has ordered vertices (a,u,b,c,v,d,e,f), edges
  au,ub,bc,cv,va,cd,de,ef,fb
and incidences aP,dQ,eR,fS. C1 has (P,Q,R,S)=(p,0,2,0), p in {1,14}.

Use the frozen V10--V14 exterior interface in H=G-V(O):
  N_H(Q)={y,X}, N_H(R)={y,Y}, f(y)=9, f(X)=f(Y)=13,
with X,Y distinct, and put K=H-{Q,R}. Every actual edge, chord, repeated
physical endpoint, fixed value, and rotation is retained.

The three maps T8,T9,T10 are exactly those frozen in V14. A whole-palette map
below is applied to every vertex of K. A mixed assignment below chooses one
of these three maps separately at each actual vertex but still checks every
actual K edge.

## 2. Two non-tight source classes force a dihedral map

For D equal to one of
  {7,8,9}, {7,8,10}, {7,9,10},
let G_D be the Cayley graph on Z20 whose edges have circular distances in D.
Let J be the target (20,7) graph, whose edges have distances 7,8,9,10.

Claim R1. Every homomorphism T:G_D -> J is
  T(x)=c+x  or  T(x)=c-x  (mod 20).

The proof has a conceptual bijectivity step and a finite classification step.

### 2.1 Bijectivity

For each of the three D, alpha(G_D)=7. A consecutive block of seven residues
is independent, giving the lower bound. The exact upper bound is certified by
checking all C(20,8)=125970 eight-subsets against the explicit Cayley edge
list. The independent code path also counts the maximum seven-subsets:
  20, 20, 40
for the three D in the order above. This is a finite palette lemma; no graph-
size extrapolation is involved.

For j in Z20 let I_j={j,j+1,...,j+6}. It is independent in J. Hence
T^{-1}(I_j) is independent in G_D and has size at most seven. Summing over all
twenty j counts every domain vertex seven times, so
  sum_j |T^{-1}(I_j)|=140.
All twenty summands are therefore seven. If n_i=|T^{-1}(i)|, subtracting the
equations for I_j and I_{j+1} gives n_j=n_{j+7}. Since gcd(7,20)=1, all n_j
are equal. Their sum is twenty, so n_j=1 for every j. Thus T is bijective.

### 2.2 Exact normalized classification

Translate the target so T(0)=0. An exact injective backtracking proof then
classifies all permutations preserving the source edges. Independently, a
generic homomorphism solver permits repeated images and reaches the same two
solutions. The complete normalized table is

  T(7)   number of maps
    7          1
    8          0
    9          0
   10          0
   11          0
   12          0
   13          1.

The two maps are x and -x. The generic solver visits 38 nodes for each D;
the independent injective solver visits 2048, 2570, and 13296 nodes. The
certificate stores the maps and the seven T(7) subsearch counts. Undoing the
target translation proves R1.

The two implementations share the candidate generator trust domain, so their
agreement is an algorithmic cross-check, not independent trusted verification.

## 3. Dihedral maps cannot finish the frozen C1 interface

Claim R2. No map from R1, even followed by arbitrary new colors for Q,R,
produces an O extension in the frozen terminal interface.

For T(x)=c+x, translate by -c. The two colors available to either Q or R are
  A(9) intersect A(13)={0,1,2}.
For T(x)=c-x, translate and reflect; the available set
A(11) intersect A(7)={0,18,19} becomes the same {0,1,2}, while P becomes the
original p and S becomes zero. It therefore suffices to exclude all
q,r in {0,1,2} for both p values.

Here is the direct small-pair argument. If r<=q, the edges ef and de force
e>=f+7 and d<=e-7<=r+6<q+7<=d, a contradiction. If q<r, the possibilities
are (0,1),(0,2),(1,2). The first forces d=f=7, after which b,c lie in one
span-six allowed interval and cannot be adjacent. In the other two cases an
unequal pair forces {d,f}={7,8}, e=15, and then {b,c}={1,14}. The two
length-two branches require
  a in {15,16,17,18,19,0},
which is disjoint from both A(1) and A(14). Equal d,f is again impossible.
Thus no O coloring exists.

Consequently the V14 one-class construction cannot be extended to two
non-tight classes by any class-oblivious global palette homomorphism. This
does not exclude a map tailored to the sparse actual edge set.

## 4. Exact per-vertex three-map formulation

Let sigma(v) be one of {8,9,10} and define
  g(v)=T_{sigma(v)}(f(v)).
For each actual K edge uv retain the binary relation
  R_uv={(i,j): EdgeOK(T_i(f(u)),T_j(f(v)))}.
Then sigma is legal on K exactly when (sigma(u),sigma(v)) belongs to R_uv for
every actual edge. This is a three-state binary CSP on the actual graph; no
path projection deletes a chord or duplicates a physical endpoint.

The terminal factor is completely favorable. The possible images are
  X,Y in {7,8}, y in {3,4,7}, S=0,
  P in {7,16} for p=1, and P in {0,4} for p=14.
There are 24 distinct terminal color states for each p, induced by all 3^5
option choices on X,Y,y,P,S. For every one of the 48 distinct states there
are colors Q,R and a literal eight-color O witness. The certificate lists
all 48 rows, and the checker verifies all 486 option tuples before quotienting
duplicates.

Claim R3. If the three-state edge CSP on K has a solution, then the original G
has a (20,7)-coloring for both frozen C1 p values: use that exact actual option
assignment, read its terminal row, then append the recorded Q,R and O colors.

This is an exact equivalence only for existence inside the declared three-map
move family. Failure of the CSP is not failure of arbitrary recoloring.

## 5. Lossless propagation and termination

For a rooted tree component, define a message from child v to parent u:
M_{v->u}(i) is true exactly when v's whole rooted subtree can be colored by
map options while the parent uses option i. Recursively,
  M_{v->u}(i) =
    OR_j [ (i,j) in R_uv AND
           AND_{w child of v} M_{w->v}(j) ].
Store the witnessing j and all child witnesses. Induction on subtree size
proves necessity and constructive sufficiency. Reconstruction uses the same
actual vertex IDs and coloring.

For an arbitrary K, start every domain at {8,9,10} and repeatedly delete an
option having no support across some incident edge. Every deletion strictly
decreases the sum of domain sizes, initially at most 3|V(K)|, so propagation
terminates. An empty domain has a finite derivation tree certificate. On a
forest, a nonempty arc-consistent fixed point is sufficient by the preceding
tree reconstruction. On a graph with cycles it is only a necessary condition;
no cyclic completeness claim is made.

Thus a failed actual exterior splits exactly into:
  (i) a finite local/propagated empty-domain certificate, or
  (ii) a nonempty cyclic residual CSP core requiring a genuinely cyclic move
       or absorption.

## 6. A minimum local obstruction to independent mixing

The three-vertex path with old colors
  19 -- 8 -- 0
has legal edge distances 9 and 8. For its left edge, compatibility forces
the middle vertex to use T9 or T10; indeed the only option pairs are
  (T9,T9), (T9,T10).
For the right edge, compatibility forces the middle vertex to use T8; its
three option pairs are
  (T8,T8), (T8,T9), (T8,T10).
The middle domains are disjoint, so no mixed assignment exists.

Each single legal edge is satisfiable by choosing its V14 map at both ends.
Hence three vertices are minimum among connected colored graphs for failure
of this map menu. The complete rotation is
  left:[middle], middle:[left,right], right:[middle].
This path is simple, planar, triangle-free, and subcubic, but it is only a
counterexample to independent selection from {T8,T9,T10}; it is not a root
counterexample and need not satisfy the minimum-obstruction terminal skeleton.

The checker classifies all 8000 ordered color triples and finds exactly thirty
legal length-two paths with this empty-domain property. The full list is in
certificate.json. It also confirms that deleting either edge restores a map
assignment.

## 7. Pressure tests, dependency DAG, and open gap

Pressure tests include:
- all three two-class source graphs and all seven possibilities for T(7);
- both a generic noninjective solver and a bijective solver;
- all C(20,8) independent-set candidates for each source graph;
- every one of 486 terminal option tuples and all O edges;
- all ordered legal length-two colored paths;
- six omitted-class mutations for V14's maps;
- endpoint, cyclic-distance, missing-edge, and altered-O-witness controls.

Dependencies:
  finite alpha lemma -> interval-preimage averaging -> bijectivity;
  bijectivity + exact permutation classification -> dihedral rigidity;
  dihedral terminal reduction + direct small-pair proof -> global-map no-go;
  actual edge relations + complete terminal factor -> three-state CSP lemma;
  tree induction / domain deletion -> lossless finite-state propagation;
  two edge relation tables -> minimum path obstruction.

closed_residual_classes: [].
open_residual_classes: [C1,C2,C3,C4].
first_open_state: C1(1,0,2,0), with p=14 in the same general bridge.
best_verified_candidate: none. best_verified_result: none.

Next obligation: in the first actual connected region carrying at least two
non-tight classes, run the exact three-state CSP with all chords. If propagation
empties a domain, use its minimum derivation subgraph as a candidate reducible
configuration or absorption target. If a cyclic nonempty core remains, retain
its rotation and relation labels and seek a signed/non-potential move. Do not
return to class-oblivious global maps or independent per-vertex choices.
