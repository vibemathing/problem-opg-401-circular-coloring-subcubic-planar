# V16: identity-anchored terminal switches and a source-faithful permanent-pin audit

Status: NONTERMINAL_CHECKPOINT. Verdict: candidate_only.
Candidate: candidate:opg401-a01-v16-identity-pin-audit.
Repository: vibemathing/problem-opg-401-circular-coloring-subcubic-planar.
Attempt: attempt:web-20260906-opg401-a01. Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1. Target: obligation:opg401-root.
Read base: a0fcca856e7181091ef3646a5d9810a1e1d0d4a5 (corrected V15/PR39 merged).

All residual classes and admitted obligations remain open. V12--V15 are
candidate inputs, not Evidence. This step audits the word "permanent": a state
may be forced only for one frozen deletion coloring, yet disappear after a
legal recoloring of the same graph. No support-cap, bare-path, single-hit, or
class-oblivious whole-palette search is repeated.

## 1. Frozen menu and terminal objective

Use the corrected V14 maps T8,T9,T10 from V15 and adjoin the identity I.
At an actual vertex v with old color f(v), a state s in

  {I,T8,T9,T10}

outputs s(f(v)). For every actual K edge uv retain the exact binary relation
of state pairs whose two outputs form a (20,7) edge. The all-I assignment is
always a solution on K; the issue is whether a terminal X or Y can use a
nonidentity state.

The V10 terminal colors are X=Y=13,y=9,P=p,S=0, p in {1,14}. If X uses T8
and Y,y,P,S use I, choose

  Q=16, R=1.

The complete O fills, in order (a,u,b,c,v,d,e,f), are

  p=1:  (14,7,0,10,1,3,14,7),
  p=14: (4,11,0,10,17,3,14,7).

If Y uses T8 and X,y,P,S use I, choose

  Q=0, R=16,

with fills

  p=1:  (11,18,5,17,4,10,3,12),
  p=14: (1,11,4,17,8,10,3,11).

Every one of the nine O edges, four O incidences, and four Q/R exterior edges
is checked directly. Hence realizing T8 at either terminal is sufficient for
both C1 values. This is a terminal lemma, not a claim that such a state must
always be realizable.

## 2. Frozen-color pinning is real but very small

A rooted colored graph pins a root x to identity if every state assignment
satisfying its actual edge relations gives state I at x. Fix f(x)=13.

For a three-vertex path x-b-c, with both old edges legal, the exact root-state
classification has only three identity pins:

  (f(b),f(c))=(3,14),(4,14),(5,14).

There are only 49 legal ordered pairs (b,c), since b is one of the seven
neighbors of 13 and c one of the seven neighbors of b. `certificate.json`
contains every root-state domain. Direct substitution in the four map words
checks the table.

The minimum is sharp: one edge never pins the root, while each displayed path
does. Thus the path 13-3-14 is the minimum frozen-color tree pin. It is not a
source-faithful permanent pin yet, because the actual middle color is not
prescribed by the root problem.

## 3. Exact radius-two audit

Suppose the middle b in one of the three paths has one additional neighbor t.
Subcubic degree gives no further neighbor. Since b is 3,4,or5 and bt is legal,

  10 <= t <= 18

in ordinary representatives.

### 3.1 Low third-neighbor colors are eliminated locally

If t<=14, recolor b to 1, leaving every other actual color unchanged. The
three actual edges have differences

  |13-1|=12, |14-1|=13, and |t-1| in {9,10,11,12,13}.

Assign T8 to x and identity to b,c,t and to the entire complement. The output
at x is 8, while the other three outputs remain 1,14,t. The same three
differences are 7,13, and 9..13 after replacing 13 by 8 at the root. Thus the
root is no longer pinned. No edge incident with c or t outside the displayed
star changes, because their colors and states remain identity.

This is a same-graph, same-complement construction. In a minimum obstruction,
the low range cannot be the first source-faithful pin.

### 3.2 The high range identifies the first genuine continuation

If 15<=t<=18 and c,t are required to remain in identity state, no recoloring
of b and no state choice at b can make x nonidentity. Indeed a nonidentity
state at color13 outputs 7 or8. The output z at b would have to lie in

  A(7 or 8) intersect A(14) intersect A(t),

and this intersection is empty for each t=15,16,17,18. This proves failure of
every operation confined to x and b with the two branches frozen, not just
failure of a listed algorithm.

The frozen four-vertex star can nevertheless be unpinned if branch states are
allowed to change. The certificate gives explicit rows. This distinction is
the point: a high third neighbor transfers the obligation into that branch;
it does not create an absolute pin.

## 4. A terminal-free bridge branch cannot be permanent

Let xb be an edge of K, and let B be the component on the b side after deleting
that bridge. Assume B contains no terminal or externally prescribed vertex.
In a hypothetical vertex-minimal root obstruction, the proper graph G[B] is
(20,7)-colorable. Choose one concrete coloring psi and translate all its
colors so psi(b)=0.

Keep f(x)=13 and assign T8 to x. Assign identity to every vertex of B. Then

  delta(13,0)=7               in the actual recolored graph,
  delta(T8(13),0)=delta(8,0)=8 in the state output.

Every internal edge of B keeps the difference from psi; every chord and the
entire inherited rotation are retained. The bridge xb is the only crossing
edge. Therefore B can be filled to support T8 at x independently of its old
frozen colors.

More generally, every terminal-free component attached to x by one bridge can
be handled independently by its own translated coloring. Such components may
be deleted from a source-faithful pin certificate. Repeated pruning strictly
decreases the number of vertices outside the terminal block.

Applied to the high range of section 3: if the t branch is separated by the
edge bt and contains no other terminal, recolor that component so its
attachment has color 8, recolor b to1, put T8 at x, and use identity elsewhere
on the displayed interface. The actual/output differences on b--attachment
are both7. The fixed c=14 branch stays untouched. Thus the high continuation
can be permanent only if the t branch reconnects to the terminal block or
contains a genuinely prescribed vertex.

This is an explicit `for every coloring of the retained side, choose a
coloring of the proper bridge component, translate it, and glue` proof. It
does not substitute an unrelated coloring across a multi-edge separator.

## 5. Core consequence and relation to the remaining routes

After pruning terminal-free bridge components, a source-faithful identity pin
at X or Y must be supported by at least one of:

1. a path/block reaching another terminal or fixed role;
2. a cyclic two-connected block;
3. a multi-attachment component whose boundary variables cannot be translated
   independently.

A finite tree containing only the root terminal always has a terminal-free
leaf branch, so repeated bridge pruning removes the whole tree. An alternating
control makes this explicit: keep root color13, color depth-one vertices0 and
then alternate 10 and0 by depth; assign T8 at the root and identity elsewhere.
Root edges have actual/output distances7/8 and all other tree edges distance10.

Thus the three-vertex path pin is a warning against freezing the deletion
coloring, not a root-level permanent-pin certificate. The first honest
remaining pin core is necessarily terminal-to-terminal or cyclic. In the V10
language these are precisely the multi-hit/y-return directions already
isolated by V12--V13; this candidate does not assert those cores are reducible.

## 6. Termination, pressure tests, and trust boundary

The pruning potential is the number of vertices in terminal-free bridge
components. Each pruning step removes a nonempty component. Component
colorings are installed once, then the terminal state and explicit O fill are
installed in two finite phases. Later steps use the actual glued coloring.

The exact checker performs:

- all 140 legal old edge pairs for the all-identity baseline;
- the four terminal X/Y-T8 completions and every O edge;
- all 49 legal rooted three-vertex paths;
- the exact three frozen pin paths;
- all 21 possible third-neighbor rows for b=3,4,5;
- the low-range one-vertex recoloring;
- the high-range empty triple intersections;
- representative full binary trees through depth8;
- fourteen mutations, including stale T8, wrong endpoint14, omitted third
  edge, treating a frozen color as a contract pin, and changing a repeated
  physical endpoint independently.

The finite tables are controls for the stated Z20 cases. The bridge-pruning
and alternating-tree claims are hand proofs for all finite sizes. The two code
paths remain one generator trust domain. No Lean, SMT, registered verifier,
EvidenceLink, Result, or Solution admission occurs.

Dependency DAG:

  corrected V14 maps + identity
      -> terminal X/Y switch table
      -> sufficient C1 terminal factor;

  exact four-state edge relations
      -> minimum frozen pin paths
      -> radius-two low/high dichotomy;

  vertex-minimality + bridge separation
      -> translated component coloring
      -> terminal-free bridge pruning
      -> terminal-to-terminal/cyclic pin core.

closed_residual_classes: [].
open_residual_classes: [C1,C2,C3,C4].
first_open_state: C1(1,0,2,0), with p=14 in the same general bridge.
best_verified_candidate: none. best_verified_result: none.

Next obligation: retain the first terminal-to-terminal or cyclic pin core,
including its complete rotation, chords, and repeated endpoints. Run the
four-state terminal CSP on that exact block. A successful nonidentity terminal
state closes the block; a forced-identity core must carry a complete finite
pin certificate and then be tested for a net-smaller uniformly liftable
absorption. Do not return to frozen path pins or bridge-only branches.
