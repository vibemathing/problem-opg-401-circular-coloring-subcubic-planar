# V15: corrected two-class rigidity and the exact three-map CSP

Status: NONTERMINAL_CHECKPOINT. Verdict: candidate_only.
Candidate: candidate:opg401-a01-v15-two-class-rigidity.
Repository: vibemathing/problem-opg-401-circular-coloring-subcubic-planar.
Attempt: attempt:web-20260906-opg401-a01. Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1. Target: obligation:opg401-root.
Read base: 6515f3e2178aefd2c2b34890e5d3f0afc90310ae (V14/PR38 merged).

All four residual classes and both admitted obligations remain open. V03--V14
are candidate inputs, not Evidence. This note attacks the exact next question:
can a class-oblivious palette map preserve two non-tight distance classes, or
can the three V14 maps be selected independently by actual vertex? It does not
repeat unit-shift, parity, support-cap, single-hit, or one-class quotient work.

## 0. Source-faithfulness correction

The first unpublished V15 branch draft transcribed V14's map T8 incorrectly as
the periodic word C[c mod 5]. The frozen V14 definition is

  C=(0,8,16,4,12),        T8(c)=C[2c mod 5],

so its correct twenty-entry word is

  (0,16,12,8,4, 0,16,12,8,4, 0,16,12,8,4, 0,16,12,8,4).

The stale word is not used in this candidate. `input.json` and
`certificate.json` record both words, and `check.py` now positively checks
every source color, both orientations, and every declared preserved class.
All CSP tables and terminal rows were regenerated from the corrected word.
This correction occurred before merge and creates no mathematical Evidence.

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

The corrected V14 maps are

  T8(c)=C[2c mod5], C=(0,8,16,4,12);
  T9(c)=0 for even c and 7 for odd c;
  T10=(0,7,14,0,7,0,1,7,0,3,7,0,7,8,0,7,10,0,7,14).

A whole-palette map below is applied to every vertex of K. A mixed assignment
below chooses one of these maps separately at each actual vertex and checks
every actual K edge.

## 2. Two non-tight source classes force a dihedral map

For D equal to one of

  {7,8,9}, {7,8,10}, {7,9,10},

let G_D be the Cayley graph on Z20 whose edges have circular distances in D.
Let J be the target (20,7) graph, whose edges have distances 7,8,9,10.

**Claim R1.** Every homomorphism T:G_D -> J is

  T(x)=c+x or T(x)=c-x (mod20).

### 2.1 Bijectivity

For each of the three D, alpha(G_D)=7. A consecutive block of seven residues
is independent. For the upper bound, the frozen finite palette certificate
checks every one of the C(20,8)=125970 eight-subsets against the explicit
Cayley edge list and finds none independent. This finite lemma has no
unbounded graph-size inference.

For j in Z20 put I_j={j,j+1,...,j+6}. It is independent in J. Hence
T^{-1}(I_j) is independent in G_D and has size at most seven. Summing over all
twenty j counts every domain vertex seven times:

  sum_j |T^{-1}(I_j)| = 140.

All twenty summands must therefore equal seven. If n_i=|T^{-1}(i)|,
subtracting the equations for I_j and I_{j+1} gives n_j=n_{j+7}. Since
gcd(7,20)=1, all n_j are equal. Their sum is twenty, so n_j=1 for every j.
Thus T is bijective.

The same palette computation counts the maximum seven-subsets as 20,20,40
for the three D. These counts are controls, not needed after the size-eight
upper bound.

### 2.2 Normalized finite classification

Translate the target so T(0)=0. An injective backtracking classification of
the remaining permutation, and a second generic homomorphism search allowing
repeated images, both return exactly

  T(x)=x and T(x)=-x.

For each D, fixing T(7) gives the table

  image of 7:  7  8  9  10 11 12 13
  map count:   1  0  0   0  0  0  1.

The generic solver visits 38 nodes for each D. The injective solver visits
2048, 2570, and 13296 nodes. The complete maps and subsearch counts are in
`certificate.json`. The two programs share one generator trust domain, so
their agreement is not independent verification. Undoing the translation
proves R1.

## 3. Dihedral maps cannot finish the frozen C1 interface

**Claim R2.** No map in R1, even followed by arbitrary new colors for Q,R,
produces an O extension in the frozen terminal interface.

For T(x)=c+x, translate by -c. The colors simultaneously allowed at either
Q or R are

  A(9) intersect A(13)={0,1,2}.

For T(x)=c-x, translate and reflect. The corresponding available set
A(11) intersect A(7)={0,18,19} becomes the same {0,1,2}, while P becomes the
original p and S becomes zero. It is therefore enough to exclude all
q,r in {0,1,2} for p=1 and p=14.

If r<=q, the edges ef and de force e>=f+7 and

  d<=e-7<=r+6<q+7<=d,

a contradiction. If q<r, the possibilities are (0,1),(0,2),(1,2).
The first forces d=f=7, after which b,c lie in one span-six allowed interval
and cannot be adjacent. In the other two cases, an unequal pair forces
{d,f}={7,8}, e=15, and then {b,c}={1,14}. The two length-two branches require

  a in {15,16,17,18,19,0},

which is disjoint from both A(1) and A(14). Equal d,f is again impossible.
Thus no O coloring exists.

Consequently the V14 one-class construction cannot be extended to two
non-tight classes by a class-oblivious whole-palette homomorphism. This does
not exclude a map tailored to the sparse actual edge set.

## 4. The corrected three-map edge CSP

Let sigma(v) be one of {8,9,10} and define

  g(v)=T_{sigma(v)}(f(v)).

For every actual edge uv of K retain the binary relation

  R_uv={(i,j): EdgeOK(T_i(f(u)),T_j(f(v)))}.

Then sigma is legal on K exactly when (sigma(u),sigma(v)) belongs to R_uv for
every actual edge. This is a three-state binary CSP on the actual graph; no
path projection deletes a chord or duplicates a physical endpoint.

The map-preservation premises are checked positively:

- T8 preserves every edge of old distance 7 or 8;
- T9 preserves every edge of old distance 7 or 9;
- T10 preserves every edge of old distance 7 or 10.

The terminal factor is completely favorable. The possible corrected images
are

  X,Y in {7,8}, y in {3,4,7}, S=0,
  P in {7,16} for p=1, and P in {0,4} for p=14.

For all 3^5 option tuples on X,Y,y,P,S and each p, direct search finds Q,R
and an eight-color O witness. Quotienting identical terminal color tuples
leaves 48 distinct rows, all stored in `certificate.json`.

**Claim R3.** If the three-state edge CSP on K has a solution, then G has a
(20,7)-coloring for both frozen C1 values: use that exact option assignment,
read its terminal row, and append the recorded Q,R and O colors.

This is an exact equivalence only for existence inside the declared map menu.
Failure of the CSP is not failure of arbitrary recoloring.

## 5. Lossless propagation and termination

For a rooted tree component, define M_{v->u}(i) to be true exactly when the
whole rooted subtree below v can be assigned map options while its parent u
uses option i. Recursively,

  M_{v->u}(i)=OR_j[(i,j) in R_uv AND
                    AND_{w child of v} M_{w->v}(j)].

Store the witnessing j and all child witnesses. Induction on subtree size
proves necessity and constructive sufficiency. Reconstruction retains the same
actual vertex IDs and produces one actual coloring.

For arbitrary K, start every domain at {8,9,10} and repeatedly delete an option
having no support across some incident edge. Every deletion strictly decreases
the sum of domain sizes, initially at most 3|V(K)|, so propagation terminates.
An empty domain has a finite derivation-tree certificate. On a forest, a
nonempty arc-consistent fixed point is sufficient by tree reconstruction.
On a graph with cycles it is only necessary; no cyclic completeness is claimed.

Thus a failed actual exterior splits into:

1. a finite local/propagated empty-domain certificate; or
2. a nonempty cyclic residual CSP core requiring another move or absorption.

## 6. Minimum local obstruction to the corrected menu

The three-vertex path with old colors

  19 -- 8 -- 0

has legal edge distances 9 and 8. For the left edge, the corrected relations
are exactly

  (T9,T9), (T9,T10),

so the middle vertex must use T9 or T10. For the right edge they are exactly

  (T8,T8), (T8,T9), (T8,T10),

so the middle vertex must use T8. The middle domains are disjoint, hence no
mixed assignment exists.

Each single edge is satisfiable by its corresponding V14 map, so three
vertices are minimum among connected colored graphs for failure of this menu.
The complete rotation is

  left:[middle], middle:[left,right], right:[middle].

The path is simple, planar, triangle-free, and subcubic, but it is only a
counterexample to independent selection from {T8,T9,T10}; it is not a root
counterexample and need not occur in a minimum-obstruction terminal skeleton.

The corrected checker classifies all 8000 ordered color triples and again finds
exactly thirty legal length-two paths with this empty-domain property. The
complete list is in the certificate.

## 7. Pressure tests and open gap

Pressure tests include:

- positive preservation of all source colors, both orientations, for the
  declared classes of T8,T9,T10;
- the stale T8 word as a mutation, which fails the positive preservation test;
- all three two-class source graphs and all seven possibilities for T(7);
- a generic solver and an injective solver;
- all C(20,8) independent-set candidates;
- every one of 486 terminal option tuples and every O edge;
- all ordered legal length-two colored paths;
- six omitted-class mutations, endpoint and cyclic-distance controls.

Dependencies:

  finite alpha lemma
    -> interval-preimage averaging
    -> bijectivity
    -> normalized permutation classification
    -> dihedral rigidity;

  corrected V14 maps
    -> actual edge relations
    -> terminal completion table
    -> exact three-state CSP;

  tree induction / domain deletion
    -> lossless finite-state propagation;

  two edge relation tables
    -> minimum path obstruction.

closed_residual_classes: [].
open_residual_classes: [C1,C2,C3,C4].
first_open_state: C1(1,0,2,0), with p=14 in the same general bridge.
best_verified_candidate: none. best_verified_result: none.

Next obligation: in the first actual connected region carrying at least two
non-tight classes, run the corrected three-state CSP with every chord. If
propagation empties a domain, retain its minimum derivation subgraph and test a
uniformly liftable reduction. If a cyclic nonempty core remains, retain its
rotation and relation labels and seek a signed move or net-smaller absorption.
Do not return to class-oblivious global maps or independent unconstrained
per-vertex choices.
