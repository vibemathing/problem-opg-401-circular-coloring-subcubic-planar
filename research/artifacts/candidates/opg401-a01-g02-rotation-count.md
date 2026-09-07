# Draft: optimal component-rotation count for a planar K2,3 configuration

Status: candidate_only; offline preparation, not a registered packet.
The admitted Attempt/Route/Graph/target remain those of OPG-401 a01.
This refines the g01 candidate. No compilation or enumeration was run.

For two colors b,c in Z20 with d=delta(b,c), fix both K2,3 pole colors
at zero and rotate their common outside component. The largest possible
product of the two middle-vertex list sizes is

    P(d)=(7-floor(d/2))*(7-ceil(d/2)),  0<=d<=10.

Proof: if the rotated boundary colors have distances s,t from zero,
their positive list sizes are 7-s and 7-t. The triangle inequality
gives s+t>=d. Thus the sum of these positive integer list sizes is
at most 14-d. Their product is at most the balanced product
floor((14-d)/2)*ceil((14-d)/2), equal to P(d).
Rotating a shortest-arc midpoint to zero attains distances
floor(d/2),ceil(d/2), so attains the bound.

The hand-auditable table for d=0,...,10 is
49,42,36,30,25,20,16,12,9,6,4.
These are algebraic values of the displayed formula, not program output.

By the planar attachment lemma in g01, an outside connected component
touches at most two of the three middle vertices. Consequently at most
one component has two attachments. Every singleton attachment can be
rotated to color zero, giving seven choices; every unattached middle
also has seven choices. Therefore every deletion coloring can be
modified by component rotations to give at least 7*P(10)=28 internal
assignments with both poles fixed at zero.

This lower guarantee is sharp for this specified construction:
take the K2,3 and join its first two middle vertices by a new path of
length three, with two new internal vertices t1,t2. The deletion is
the edge t1t2. Prescribe its valid colors 0,10. Any rotation preserves
their distance ten, so the first two middle lists have product at most
four; the third middle has seven choices. Hence no rotation supplies
more than 28 assignments with the poles both zero. A centered rotation
attains 28. This does not bound assignments with distinct pole colors
or count different outside rotations as different internal extensions.

Parameter boundary (explicitly outside the frozen 20/7 specialization):
for integers 2q<=p<3q put k=p-2q and dmax=floor(p/2). The g01 promise
that EVERY deletion coloring can be extended by whole-component
rotations holds uniformly for these K2,3 configurations exactly when

    2k >= dmax.

Sufficiency: two colors can be centered at distances floor(d/2),
ceil(d/2), at most k. The general two-list count is k+1-delta,
so every required list is nonempty.

Necessity: on the same seven-vertex graph prescribe outside edge colors
0,dmax, a valid (p,q)-coloring since q<=dmax<=p-q.
Any extension would force the color a of either pole to satisfy
delta(a,0)<=k and delta(a,dmax)<=k. The triangle inequality would
give dmax<=2k. Rotation preserves dmax, so cannot repair the failure.
The graph is planar by drawing the new three-edge path inside the
four-face between the first two length-two pole paths; its shortest
new odd cycles have length five, and all degrees remain at most three.

The preserving-extension promise depends on the actual palette, not
just p/q. It holds for (5,2), where k=1,dmax=2, but fails for (10,4),
where k=2,dmax=5. This does not distinguish unrestricted colorability:
the seven-vertex graph has a (5,2)-coloring with poles 1, first and
third middles 3, second middle 4, and outside colors 0,2. Multiplying
these colors by two gives a (10,4)-coloring. The failing (10,4)
precoloring instead uses outside colors 0,5, which no rotation changes
to a pair of distance at most four.

Both admitted obligations remain open.
best_verified_result: none; best_verified_candidate: none.
No new admitted route or obligation is created by these statements.
Next action: fresh-read main and active PR state, compare existing
candidates for overlap, then bind a unique packet on a fresh branch.
