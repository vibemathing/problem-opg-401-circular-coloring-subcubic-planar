# V16 transport repair and independent finite cross-check

Status: NONTERMINAL_CHECKPOINT. Verdict: candidate_only.

This clean supplement preserves the mathematical scope of the unique open V16
transaction without relying on its corrupted certificate byte stream.

## Exact finite facts

Using the corrected V15 maps T8,T9,T10, the three-state edge CSP has exactly
30 ordered legal length-two color paths whose middle option domain is empty.
When the middle has degree two, every such source-color core admits a legal
recoloring of the middle that restores a nonempty local menu.

With a third actual neighbor retained, the center is source-rigid in exactly
21 leaf-unordered colored stars. They collapse to five complete neighbor-list
families; in each row EVERY physically legal center color is menu-empty:

* neighbors {13,14,16}: center colors {3,4,5,6};
* neighbors {3,6,7}: center colors {14,15,16};
* neighbors {4,6,7}: center colors {14,15,16,17};
* neighbors {5,6,7}: center colors {14,15,16,17,18};
* neighbors {6,7,8}: center colors {15,16,17,18,19}.

Thus the first honest degree-three local core is not a single frozen color:
the whole available center interval is menu-empty. Any repair must change a
branch color/state or enlarge the region.

For the four-state menu {I,T8,T9,T10} with a rooted cycle whose root source
color is 13, the exact finite census is: C4 has 27 identity-pinned source
colorings and every one is unpinned by one nonroot recolor. C5 has 180
identity-pinned source colorings; 88 resist one-vertex recoloring, 26 resist
every uniform +/-1 shift of a nonroot subset, and exactly 18 resist both
families. The representative 13-0-7-15-4 is one of those 18, but the legal
two-vertex recoloring 15,4 -> 14,1 produces 13-0-7-14-1 and unpins the root.
So it is not an all-recoloring obstruction or root counterexample.

## Source-faithful permanent-pin boundary

The companion V16 proof's all-size bridge argument remains the graph-level
piece: a terminal-free component attached by one bridge cannot be an absolute
pin in a vertex-minimal root obstruction, because its smaller-side coloring
may be translated at the sole attachment and glued. Therefore a genuine
permanent pin must propagate to another terminal/fixed role, a cyclic block,
or a multiattachment block.

The finite star/cycle data are controls for these exact palette objects only.
They do not show that every remaining C1 exterior contains one of them and
do not close C1, any later class, or either admitted obligation.
