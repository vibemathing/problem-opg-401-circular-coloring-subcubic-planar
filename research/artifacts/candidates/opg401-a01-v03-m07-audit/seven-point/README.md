# V03 seven-point and full-coloring certificate replay

Verdict: candidate_only. This directory does not contain a trusted verifier receipt.
All C1-C4 residual classes and both admitted obligations remain open.

The complete positive cover is stored as five READABLE JSON row arrays,
cover-part-1.json through cover-part-5.json. These are not opaque archive chunks:
every edge mask, boundary index, and internal color is directly inspectable.
Their rows assemble to the exact 30078-byte cover.json with SHA-256
481592caf5b356242a393caaf58294872afbe131049c8fe0575dcddcb492413b.
The proof's references to cover.json mean this deterministic assembled object.

From a fresh copy of this directory, replay the actual finishing checks:

```sh
python3 -I -S assemble-cover.py
python3 -I -S finish-replay.py check
python3 -I -S finish-replay.py recolor
```

Assembly does not search. The check uses edge-addition coverage and verifies
all positive witnesses against exact edge predicates, skipping the sixteen
previously excluded retained-J cases without coloring them. Recolor checks
both full C1 orbit fixtures and their reflected C2 controls. Each child is
bounded to 40 seconds wall, 35 seconds CPU, 512 MiB, and one thread. A timeout
is inconclusive, not a mathematical negative result. Replays should be made
in a fresh local copy; they produce ordinary candidate outputs, not truth ledgers.

Optional regeneration uses the separately provided run.py phases generate,
check, recolor, summarize, each in its own command. The original generation
really ran successfully. Its observation was reconstructed from this turn's
actual tool output after a foreground runtime reset; it is not represented
as the exact bytes of the lost original observation file. The finishing
checks were then actually replayed with the same frozen finite.py/recolor.py
source hashes. execution.json records those two new observations explicitly.

The older M07 and extra-port files are retained input candidates. The missing
extra-port/replacement-screen.json is restored byte-for-byte to its historical
digest. Its input newline repair does not fabricate an earlier execution.
The old incomplete opaque replay capsule remains only in immutable branch
history; it is not promoted to an evidence object. Distinct material in the
older supplied local replay archive has not been claimed fully transported
by this finishing package. See the source provenance note and Issue checkpoint.
