# V12: multi-hit zero-cone quotient and the first weighted fallback

Status: NONTERMINAL_CHECKPOINT. Verdict: candidate_only.
Candidate: candidate:opg401-a01-v12-multihit-quotient.
Repository: vibemathing/problem-opg-401-circular-coloring-subcubic-planar.
Attempt: attempt:web-20260906-opg401-a01.
Route: route:degree-two-extension-criterion-v1.
Graph: graph:opg401-initial-v1. Target: obligation:opg401-root.
Read base: 30df2a21110f6acbe91ead718d0f985cc4091948 (V11/PR35 merged).

All four residual classes and both admitted obligations remain open. This candidate closes a large multi-hit subcase and gives exact obstruction signatures. It does not claim that a genuine minimum obstruction has the V10 interface, and it does not advance C2.

## 1. Frozen interface and actual-state semantics

Colors are residues 0,...,19. EdgeOK(a,b) means 7 <= [b-a]_20 <= 13; equivalently, for the fixed representatives, 7 <= |a-b| <= 13. The undirected distance is the shortest cyclic distance, not an arbitrary integer lift.

The eight-vertex region O has ordered vertices (a,u,b,c,v,d,e,f), edges au,ub,bc,cv,va,cd,de,ef,fb, and port incidences aP,dQ,eR,fS. C1 has actual port colors (P,Q,R,S)=(p,0,2,0), where p is 1 or 14.

Use the V10 exterior interface in H=G-V(O): N_H(Q)={y,X}, N_H(R)={y,Y}, f(y)=9 and f(X)=f(Y)=13. The present branch has X and Y distinct. Put K=H-{Q,R}. Every edge and chord of K, every repeated physical boundary endpoint, and the inherited rotation are retained. A repeated endpoint is one vertex with one color, although all of its incidences remain in the cut ledger.

Orient a zero arc u->v precisely when [f(v)-f(u)]_20=13. For a vertex z let R(z) be its full forward reachable set in this actual zero digraph. A set D is forward closed when u in D and u->v imply v in D. All ordinary boundary vertices explicitly declared releasable may change. A permanent pin may not.

## 2. Unit downshift on an arbitrary closed set

If D is forward closed, define f_D(v)=f(v)-1 on D and f_D(v)=f(v) outside D. Then f_D is a valid (20,7)-coloring of K.

Indeed, an edge with both ends on the same side is unchanged. Orient a crossing edge from u in D to v outside D and put r=[f(v)-f(u)]_20 in {7,...,13}. Its new residue is r+1, hence it is legal unless r=13. The excluded value would be a zero arc leaving D. This checks every actual edge; no tree projection or shortest-path deletion is used. The graph and rotation are unchanged.

Conversely, for every two vertices s,t there exists a forward-closed D with s in D and t not in D exactly when t is not reachable from s: use R(s) for sufficiency, and use closure for necessity. This elementary separation fact turns the multi-hit problem into a five-terminal reachability quotient.

## 3. Exact local response of a closed set containing Y

Take any forward-closed D containing Y and avoiding every permanent pin. Write four membership bits x=1[X in D], h=1[y in D], alpha=1[P in D], beta=1[S in D]. After the unit downshift the five relevant colors are Y'=12, X'=13-x, y'=9-h, P'=p-alpha, S'=-beta (mod 20). All other hits of D are released together and do not alter the O boundary.

There exist colors q,r for Q,R, legal on Qy,QX,Ry,RY, and a full coloring of O if and only if

p=1: h=0 OR (alpha=0 AND (x=1 OR beta=1));

p=14: h=0 OR beta=0.

These are exact, not merely sufficient.

### 3.1 Positive witnesses

When h=0, if beta=0 choose (q,r)=(2,19); if beta=1 choose (q,r)=(0,2). These choices work for x=0 or 1 and either alpha. Complete O witnesses are recorded in certificate.json.

When h=1: for p=1, alpha=0,beta=1 choose (q,r)=(0,1), for either x; for p=1, alpha=0,beta=0,x=1 choose (q,r)=(19,1); for p=14,beta=0 choose (q,r)=(1,19), for either x and alpha. Each recorded witness checks all nine O edges and four port incidences.

### 3.2 Necessity and the small exact table

Assume h=1. Then y'=8,Y'=12. Hence r in A(8) intersect A(12)={0,1,19}, while q is in {0,1} if x=0 and in {0,1,19} if x=1.

The only O-fillable cases for q,r in {0,1,19} and S' in {0,19} are:

S'=0: (q,r)=(1,19) exactly when P' is in {8,...,19}; (q,r)=(19,1) exactly when P' is in {1,...,12}.

S'=19: (q,r)=(0,1) or (19,1) exactly when P' is in {1,...,12}.

No other pair fills O.

For a hand derivation, intersect the three seven-color lists on the second pentagon before treating the first ear. The only surviving (d,e,f) triples are: S'=0,(q,r)=(1,19): (14,6,13); S'=0,(q,r)=(19,1): (6,14,7); S'=19,(q,r)=(0,1): (7,14,6); S'=19,(q,r)=(19,1): (6,14,7) or (7,14,6). All other triples violate de, ef, or the requirement that the b-c ear have unequal end colors. In each surviving row d and f differ by one. The exact distance-one ear criterion says P' must lie outside A(d) union A(f), giving {8,...,19} for (14,13) and {1,...,12} for (6,7) or (7,6). Direct interval intersections construct b,c,a,u,v, so the table is necessary and sufficient.

Substituting P' in {1,0,14,13} proves the formulas, including all endpoints.

## 4. Exact reachability quotient for all multi-hit unit shifts

A successful forward-closed D containing Y exists precisely as follows, before permanent pins are considered.

For p=1: either y is not reachable from Y, or P is not reachable from Y and at least one z in {X,S} does not reach P.

For p=14: y is not reachable from Y, or S is not reachable from Y.

If y is absent from R(Y), take D=R(Y). Otherwise the p=1 local formula requires P not in D and X or S in D. Such a D exists exactly when P is absent from R(Y) and from R(z) for at least one z in {X,S}; take their union. The union is forward closed. The converse follows because any forward-closed D containing z contains R(z). The p=14 formula follows directly because every D containing Y contains R(Y).

With permanent pins B0, additionally require each selected reachability cone to avoid B0. Every number of ordinary fixed hits may be released together. Thus V11's one-hit result is not a cardinality bound.

The exact no-unit-shift signatures are therefore:

p=1: Y reaches y, and [Y reaches P OR (X reaches P AND S reaches P)].

p=14: Y reaches both y and S.

These concern all forward-closed unit downshifts containing Y, not all recolorings.

The checker independently enumerates all 6,942 labeled five-terminal preorders. It compares every upward-closed membership pattern with the exact local formulas and obtains precisely these signatures. The finite audit is not the proof; reachability separation is the all-size argument.

## 5. A stronger weighted fallback for the p=1 obstruction

For p=1 prescribe Q=1,R=19 and use the O witness (a,u,b,c,v,d,e,f)=(6,13,0,7,14,14,6,13). On K allow actual drops g(v)=f(v)-d(v), 0<=d(v)<=6. The cut domains are P:[2,6], Y:[1,6], y:[0,1], X:[0,5], S:{0}; every permanent pin is {0}; all other vertices have [0,6].

For each oriented K edge uv put w(u,v)=13-[f(v)-f(u)]_20. The exact edge inequalities are d(u)-d(v)<=w(u,v) and the reverse inequality. The coordinatewise least lower envelope is

d_*(v)=max(0,1-dist(Y,v),2-dist(P,v)).

Thus the target is feasible exactly when dist(Y,S)>=1, dist(P,S)>=2, dist(P,y)>=1 and, for every permanent pin b, dist(Y,b)>=1 and dist(P,b)>=2. All other upper bounds are automatic because d_*<=2. Necessity follows by summing edge inequalities along paths. Sufficiency follows from the directed triangle inequality. The stated O witness then finishes the same actual coloring, with every chord retained.

A failed case has an actual path of total slack 0 or 1 from P, or a zero path from Y, to the specified upper-bound vertex. This is the next bounded structural certificate, not an all-recoloring obstruction.

One complete plane control in certificate.json realizes the p=1 no-unit-shift signature yet satisfies these weighted conditions. Its least vector drops P by two and the full Y-to-y cone by one, then uses the displayed Q,R and O colors.

## 6. The p=14 reachability skeleton blocks every bounded downshift

For p=14 assume the sharper reachability skeleton Y->S->y, X->y, P->y. Every valid bounded-drop recoloring must satisfy d(Y)<=d(S)<=d(y), d(X)<=d(y), d(P)<=d(y).

Translate the final coloring globally so y again has color 9. Put A=d(y)-d(Y), B=d(y)-d(S), C=d(y)-d(X), D=d(y)-d(P). Then A>=B>=0 and C,D>=0. The colors become Y=13+A,S=B,X=13+C,P=14+D,y=9.

For Q and R to see y and X/Y, necessarily A,C<=2, with q in {C,...,2} and r in {A,...,2}. Also B<=A, so S is in {0,1,2}. For P in {14,15,16,17,18,19,0}, the exact O table on q,r,S in {0,1,2} is: S=0, no fill; S=1, only q=2,r=0; S=2, only q in {1,2},r=0.

A fill would require B>=1 and r=0. But r>=A and B<=A, forcing B=0, a contradiction. Hence no d:V(K)->{0,...,6} respecting the actual edges can repair this local interface under the stated reachability skeleton.

This rejects only the bounded nonnegative-downshift chamber. It does not reject signed or non-potential recolorings, a different structural reduction, absorption, or the root claim.

A second complete plane control realizes the skeleton. Its reduced zero network is the chain Y->S->P->X->y, with segment lengths 19,18,3,12. It is simple, triangle-free, planar and subcubic after subdivision. The certificate records the complete rotation, every face, the old exterior coloring and a different full coloring of G. It is not a root counterexample and has many degree-two path vertices.

## 7. Boundary accounting, termination, and pressure tests

For a connected induced exterior set W containing k of the four O ports, with n=|W|, c=|E(H[W])|-(n-1), and d0=sum_W(3-deg_G(v)), the cut of O union W remains b=n+6-2k-2c-d0. No reachability contraction changes this count. Repeated exterior endpoints reduce independent color variables, never edge incidences.

The unit-shift construction discovers actual cones by a finite queue; (unseen vertices, queue length) decreases lexicographically. It then constructs one complete vector, checks it, and appends a fixed O witness. The weighted fallback has at most 6|V(K)| strict integer increases; (6|V(K)|-sum d, queue length) decreases. Failure returns a path certificate.

Pressure tests cover directed 7/13 endpoints, h=0/1, both p values, X shifted/unshifted, P and S shifted together, whole/empty distinguished patterns, chords, repeated endpoints, permanent pins, the p=14 bounded no-go boundary, and full plane controls. The checker does not import the old V06 target table or use a projected exterior coloring.

Dependencies: definitions -> closed-set edge lemma -> local hit table; local hit table + reachability separation -> exact obstruction signatures; edge inequalities + fixed O target -> p=1 weighted fallback; p=14 reachability inequalities + small O table -> bounded no-go.

closed_residual_classes: []. open_residual_classes: [C1,C2,C3,C4]. first_open_state: C1(1,0,2,0), with p=14 required in the same general bridge. best_verified_candidate: none. best_verified_result: none.

Next obligation: for p=1 treat the total-slack 0/1 paths violating the weighted criterion, retaining their full joint response; for p=14 leave the bounded-downshift chamber and seek a signed/non-potential same-state recoloring or a uniformly liftable net-smaller absorption for the chain skeleton. Neither general bridge is proved here.
