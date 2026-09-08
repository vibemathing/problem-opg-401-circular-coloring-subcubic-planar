# V05: complete auxiliary-axis failures and a common unit-step target

Status: NONTERMINAL_CHECKPOINT. Verdict: candidate_only.
Candidate: candidate:opg401-a01-v05-axis-blockers. Primary owner: math-proof.
Repository: vibemathing/problem-opg-401-circular-coloring-subcubic-planar.
Problem: problem:opg-401-circular-coloring-subcubic-planar.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1. Target: obligation:opg401-root.
Read base: de730bc8fbebd354651f8768d2ed63a257745df9 (PR29 merged).
Both admitted obligations and all four whole residual classes remain open.

## 1. Definitions, quantifiers and scope

Colors are residues 0,...,19. EdgeOK(a,b) means 7 <= [b-a]20 <= 13.
The undirected circular distance is min([b-a]20,[a-b]20). An arbitrary integer
lift is never used in the absolute-value implementation. A(a)=a+{7,...,13}.
The eight distinct vertices of O are a,u,b,c,v,d,e,f, with nine inner edges
au,ub,bc,cv,va,cd,de,ef,fb and ports aP,dQ,eR,fS. P,Q,R,S are distinct
vertices in disk order P,S,R,Q; equal colors do not identify vertices.
C1 has (p,q,r,s)=(1,0,2,0) or (14,0,2,0); C2 is color negation.
H keeps every exterior edge and its actual valid coloring f. A fixed set B
has the actual prescribed values f|B. It cannot be silently recolored.

V03 and V04 are candidate inputs, not mathematical Evidence. V04's exact
pivot test keeps all four ports and B fixed in stage one, uses one auxiliary
reflection tau_ell(c)=ell-c, and then changes ONE target t from c to c'.
Its neighbors must lie in I=A(c) intersect A(c') during both stages.
A neighbor whose old color is outside I must be reflected. A vertex with
neither option in I is a zero-choice failure. Otherwise required reflected
vertices force their entire components in the actual mixed-conflict graph
L_ell(f). A forced component hitting a vertex required unreflected is a
failure. It has an explicit required-to-forbidden path. The terminal may
be a moved pin OR an old-only neighbor, not necessarily a port.

This note disproves universal auxiliary-axis success from the stated local
plane/degree/Steiner accounting data ALONE. It does NOT disprove the assertion
restricted to genuine minimum noncolorable graphs. Its controls are colorable,
and do not satisfy all prior tight-reachability obstructions. No universal
nonabsorption claim is made. The new all-size necessary condition in section 5
DOES apply to each actual C1 coloring of a hypothetical minimum obstruction.
No excluded small-replacement, selective-F, C40, or same-axis-pruning search is run.

## 2. A complete local zero-choice classification

For c=2,c'=6, I={13,14,15}, and every old neighbor color lies in {9,...,15}.
For two neighbors x,y, some ell supplies an old/reflected option in I for
BOTH neighbors if and only if {x,y}!={9,12}. For c=0,c'=16, I={7,8,9},
old neighbor colors lie in {7,...,13}, and the unique unordered exceptional
pair is {10,13}.

Proof. If an old color belongs to I, leave it unchanged. If both are outside
I they belong to one consecutive four-color interval. When their separation
is at most two, reflect the larger onto the first element of I: the smaller
then lands at most two later. When their separation is three, an isometry
cannot put both into the diameter-two interval I. The endpoints of those
four-color intervals are precisely the two displayed exceptional pairs.
This exhausts equal colors, both endpoints and all twenty possible ell.
Graph constraints may still block an ell that passes this local test.

## 3. Two saturated annular controls with all twenty axes certified

For each case use an outer cycle 0,...,N-1, an inner cycle N,...,N+M-1,
and the listed spokes v_j--(N+j). All edges are undirected. No other H edges
exist. O is added with labels n,...,n+7 in the fixed order, n=N+M.

A (p1): N=8,M=4, spokes (1,3,5,7), ports (P,Q,R,S)=(0,6,4,2).
Actual H colors, in vertex order:
 (1,8,0,13,2,9,0,13,15,3,16,3).
B (p14): N=12,M=8, spokes (1,2,3,4,6,8,10,11), ports (0,9,7,5).
Actual H colors:
 (14,7,14,1,13,0,9,2,13,0,10,1,0,7,14,3,16,4,17,8).

These are finite simple triangle-free plane subcubic graphs. After adding O,
EVERY vertex except the original u,v has degree three. There are no new leaves
or degree-two defects. The complete rotations and faces are in certificate.json.
They can also be reconstructed as follows. On the outer cycle start with
[i-1,i+1], insert the inner spoke between them; on the inner cycle use
[previous,next,outer-spoke]. The four ports lie on the outside face in the
required order. Insert O in that face with the given port incidences. The
certificate checks the two possible O orientations and records the sphere
rotation: every dart occurs exactly once and V-E+F=2. G has respectively
(V,E,F)=(20,29,11) and (28,41,15). No embedding or edge is discarded.

Every port belongs to a single PRIMARY conflict component, for k=8 or16.
In A, the prescribed V04 target R=4 has neighbors 3,5 with colors13,9.
For ell outside {2,3,4}, vertex5 has no option in I={13,14,15}.
For ell2 the failure path is 5--10--9--3, with colors9,16,3,13. Its three
mixed differences are3,17,14. The last vertex is an OLD-ONLY NEIGHBOR of R.
For ell3 and ell4 the path is5--6, ending at the fixed Q color0, with mixed
differences6 and5. This is a complete certificate for all twenty ell.
In B, the prescribed target Q=9 has neighbors8,10 of colors13,10. They are
the exceptional pair in section2. The axes making13 eligible are{0,1,2};
the axes making10 eligible are{17,18,19}. They are disjoint. Each of the
twenty failures therefore has a literal zero-choice neighbor.

The controls are stronger than a failure at just the chosen port: EVERY
choice of a target port followed by its PRIMARY reflection fails for every
ell. In A, P's two different neighbor colors8,13 cannot both reach its
singleton I={14}; Q and S have empty I. In B, P and R have empty I; S has
I={7,8,9} and the only locally possible ell0,1,2 have failure path
4--15--16--6, with colors13,3,16,9, ending at its old-only neighbor6.
The other axes have a zero-choice neighbor. Color negation gives two actual
C2 inputs and all their actual failure certificates. The file stores 320
primary-target failures (four targets x20 axes xfour inputs), with a separate
literal absolute-difference checker for every no-choice/path certificate.

Both examples also block the four elementary one-port escapes P1->2 or
P14->13, R2->3, Q0->19, S0->19: they have respectively the required adjacent
colors8 or7,9,13,13. This is not a certificate against a MULTI-vertex unit move.
Global minimum order is not proved for either exterior. A has the minimum
12 vertices in the specified two-cycle architecture with four independent
outer ports and all nonports spoked once; no comparable minimum claim is
made for B. Neither is a minimum root obstruction.

## 4. What the Steiner and mod-three identities do, and do not, imply

A minimum conflict Steiner tree in A has W={0,1,2,4,5,6,7}, n=7.
In B the minimum has W={0,1,2,3,4,5,7,8,9,10,11}, n=11.
The finite checker enumerates port-containing vertex sets in increasing size;
a connected set supplies a spanning tree, and any tree occurs on one such set.
Thus the first size gives the exact minimum edge count, not a heuristic tree.
For these W, c=|E(H[W])|-n+1=0 and d=sum_W(3-deg_G)=0. The induced
regions O union W therefore have b=n-2-2c-d=5 and9 leaving incidences.
Direct counting agrees. At most two tree branch vertices did not give b<=3.

For the entire primary component C, use V04's two open semicircle signs.
The tuples (sum_C epsilon, port contribution, degree-deficit contribution,
compatible-edge contribution) are (-2,-4,0,-2) and (0,-2,0,2).
Both satisfy 3 sum epsilon = port + deficit + compatible. In particular the
required nonzero contribution is supplied entirely by compatible edges, not
by a low-degree vertex. It is present even though every auxiliary pivot above
fails. The nonzero mod-three remainder alone does not prove pivot success.

Nor do auxiliary failure paths stay inside the primary Steiner region or
even the primary component. A's path5--10--9--3 uses vertex9 outside that
primary component. All actual failing paths and all zero-choice neighbors,
united with W, give connected sets of sizes10,15, excess-edge counts2,3 and
cuts4,7 respectively. These still are not three-port regions.
For any induced connected enlargement containing all four ports the same
formula b=n-2-2c-d holds. Adding a nonport vertex with j existing neighbors
changes the cut by deg_G(v)-2j; it can INCREASE the cut when j=1. Thus merely
collecting failure paths is not a strictly improving absorption algorithm.

These observations do not exclude other absorbed-region replacements.
Indeed certificate.json gives full restorations for BOTH selected Steiner
regions with the ACTUAL complement colors fixed. They are positive witnesses,
not universal boundary-extension theorems. Consequently no 'all allowed
absorptions fail' certificate can be attributed to these examples. A family
of permitted replacements and a universal lifting proof are still needed to
resolve the genuine minimum-obstruction disjunction.

## 5. A common target removes zero-choice from the remaining C1 obligation

Use R:2->3 for BOTH p1 and p14, not the previously prescribed6 or Q16.
The common list is J=A(2) intersect A(3)={10,11,12,13,14,15}.
If no R-neighbor has color9, simply change R to3. Otherwise only color9
neighbors require changes. For every
                   ell in E={19,0,1,2,3,4},
9 is reflected respectively to10,11,12,13,14,15, and every other old neighbor
color in{10,...,15} can be left unchanged. Thus NONE of these six axes has
a zero-choice neighbor, for ANY actual valid f. This includes repeated colors.
The hand argument covers all degree-two target neighborhoods; 294 local
pair/axis checks are controls, not the proof.

If R is additionally prescribed in B, changing it is forbidden before any
axis test; that is a fixed-value obstruction, not a successful move.
For a chosen ell form required/forbidden vertices exactly as in section1,
with all four ports and the actual fixed set B preserved. Let U be the union
of L_ell(f) components containing the required color9 neighbors. If U misses
all forbidden vertices, reflecting precisely U gives the actual f1, changing
R to3 gives the actual f2, and O is filled by one of the following vectors:
 p1:  (8,1,14,2,15,9,16,7);
 p14: (1,9,2,15,8,7,16,9).
Check all nine O edges and its four port edges. They have port tuples
(1,0,3,0) and(14,0,3,0). The construction preserves every H edge and B in
both stages. Quantifiers are: for EACH actual f satisfying the component
criterion, the specified U,f1,f2,fill is its own witness. No projected-fiber
representative is substituted and no different replacement colorings combine.

Required-to-forbidden paths are now the ONLY failure type in these six axes.
Hence in a hypothetical minimum noncolorable G, every actual C1 exterior f
must have at least one color9 neighbor at R and a path certificate for EVERY
ell in E (with B empty in the unrestricted exterior application). Otherwise
the displayed construction colors that very G. This is a new precise necessary
condition; it is not an assertion that such a six-path system is impossible.
The two controls also fail all six tests. For A, ell19,0,1,2 use
5--10--9--3; ell3,4 use5--6. For B they use6--16--17--8 and6--5 respectively.
The complete twenty-axis unit-target tests for both inputs and their negations
are also saved, without using a failed old target as evidence about the new one.

A useful short-path consequence follows for ell19, with B empty. A selected
color9 vertex can initially force ONLY a neighbor of color16: its old allowed
neighbors are16,...,19,0,1,2, whereas the reflected10 allows17,...,19,0,1,2,3.
After two conflict edges the color is in{3,...,9}. No original port color
0,1,2,14 is reached at that distance, and no old-only R-neighbor is reached.
Thus every minimal forbidden path has at least three edges. In the p1 case,
a three-edge path cannot end at a port: check its third edge to0,1,2, whose
mixed values are legal. It must end at R's OTHER neighbor. Together with R
this is an induced five-cycle (triangle-freeness rules out its chords).
For p14 there is one additional possible three-edge endpoint, P of color14;
otherwise the same five-cycle conclusion holds. Longer paths remain open.
With extra B pins this length conclusion is not asserted, although the exact
six-axis oracle still respects them. Negation gives the C2 version with
R18->17, axes{1,0,19,18,17,16} and first forced colors11->4.

Discovery terminates by the lexicographic measure (undiscovered vertices,
queue length). On success the stages pivot, target-change and O-fill decrease
in that order. Every subsequent operation must recompute its tests on the
actual preceding output. Failure is a path certificate, not a terminal fill.
No measure proving universal repair or universal absorption is supplied.

## 6. Exact scope of the counterexamples, checks and continuation

For each input the certificate also supplies an explicit full coloring: a
forward tight closure from R can be shifted by one (negatively for C2), and
the actual O fill is checked. This REUSES an earlier legal-move criterion only
to show that the controls are colorable; it is not a new general repair theorem.
In particular these controls do not have all the historical tight reachability
obstructions. They cannot refute the minimum-obstruction-specific bridge.
Only the inference from planarity, cubic degrees, conflict connectivity and
a nonzero mod-three contribution to auxiliary-axis success is rejected here.
Neither V04's conditional pivot criterion nor M07 is withdrawn.

The checker generates the supplied finite graphs from their explicit cycles,
spokes and port lists, and verifies every edge, rotation, pin and failure path.
A separate scalar predicate verifies each path certificate without running the
component algorithm. The positive witness finder branches only on literal
edge constraints, with a fixed node limit; no old table or candidate code is
imported. Tests include 320 old-target failures,80 unit-target failures,98
ordered neighborhood rows with all20 axes,294 guaranteed unit-axis local cases,
and14 detected mutations. Two code paths are not two trust principals.

Run python3 -I -S run.py in a fresh copy; it refuses to overwrite replay/.
The committed certificate.json and execution.json are unchanged copies of
the replay outputs. Execution.json binds actual source/input/output hashes, versions, exit status
and resource limits. No registered verifier, Lean/SMT, EvidenceLink, Result
or Solution admission occurs. Pure probability/asymptotic arguments are not used.
The prior matching-and-recolor attachment remains separately pending; this
round does not rerun or reconcile its exhausted replacement computations.

closed_residual_classes: []. open_residual_classes: C1,C2,C3,C4.
first_open_state: C1(1,0,2,0), with the p14 partner treated by the same R3 target.
Next atomic obligation: in a genuine minimum obstruction satisfying earlier
constraints, handle the six actual required-to-forbidden paths for the unit
R target. At ell19 separate the induced exterior-five-cycle case from the
length>=4 case (and the p14 path to P), retaining rotation and all induced
boundary incidences. Prove a new same-witness move or a net-smaller replacement;
do not infer b<=3 from a tree or from collecting those paths.
best_verified_candidate: none. best_verified_result: none.
Open admitted obligations: obligation:opg401-z20-extension; obligation:opg401-root.
