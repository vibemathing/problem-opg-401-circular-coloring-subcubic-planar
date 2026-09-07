"""Separate exact checker: fixed-representative absolute differences as oracle.
No imports from enumerate.py. No trusted verification or admission is claimed.
"""
import copy
import json
import sys
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def edge(a: int, b: int) -> bool:
    return 7 <= abs(a - b) <= 13


def dist(a: int, b: int) -> int:
    d = abs(a - b)
    return min(d, 20 - d)


def colors(mask: int) -> set[int]:
    return {x for x in range(20) if (mask >> x) & 1}


def check_certificate(data: dict) -> dict[tuple[int, int], set[int]]:
    require(data.get("p") == 20 and data.get("q") == 7, "palette mismatch")
    rows = data["rows"]
    require(len(rows) == 400, "coverage must be exactly 400 rows")
    table = {}
    for i, row in enumerate(rows):
        require(type(row) is list and len(row) == 3, "invalid row")
        a, b, mask = row
        require((a, b) == divmod(i, 20), "wrong row order, duplicate or missing pair")
        require(type(mask) is int and 0 <= mask < 2**20, "invalid bitmask")
        expected = {x for x in range(20) if edge(x, a) and edge(x, b)}
        actual = colors(mask)
        require(actual == expected, f"membership mismatch at {a},{b}")
        require(data["counts"][a][b] == len(actual), "count/mask mismatch")
        require(len(actual) == max(0, 7 - dist(a, b)), "closed-form mismatch")
        require(bool(actual) == (dist(a, b) <= 6), "threshold mismatch")
        table[a, b] = actual
    return table


def main() -> None:
    if len(sys.argv) != 4:
        raise ValueError("usage: check.py input.json certificate.json audit.json")
    inp = json.loads(Path(sys.argv[1]).read_text())
    require((inp.get("p"), inp.get("q")) == (20, 7), "input mismatch")
    data = json.loads(Path(sys.argv[2]).read_text())
    table = check_certificate(data)
    for a in range(20):
        require(len(table[a, a]) == 7, "equal-color case")
        require(not table[a, (a + 10) % 20], "antipodal case")
        for jump in (7, 13):
            require(edge(a, (a + jump) % 20), "closed endpoint lost")
        for jump in (6, 14):
            require(not edge(a, (a + jump) % 20), "illegal endpoint accepted")
        for b in range(20):
            actual = table[a, b]
            require(actual == table[b, a], "swap failure")
            require({(-x) % 20 for x in actual} == table[(-a) % 20, (-b) % 20],
                    "reflection failure")
            t = dist(a, b)
            epsilon = 1 if (b - a) % 20 == t else -1
            normalized = set(range(7 + t, 14)) if t <= 6 else set()
            require(actual == {(a + epsilon * y) % 20 for y in normalized},
                    "inverse rotation/reflection failure")
            for k in range(20):
                require({(x + k) % 20 for x in actual} ==
                        table[(a + k) % 20, (b + k) % 20], "translation failure")
            # Compare the three interpretations of the edge predicate.
            r = (b - a) % 20
            require(edge(a, b) == (7 <= r <= 13) == (dist(a, b) >= 7),
                    "definition faithfulness failure")
    edge_mutants = {
        "exclude_7": lambda a, x: 7 < (x-a) % 20 <= 13,
        "exclude_13": lambda a, x: 7 <= (x-a) % 20 < 13,
        "natural_subtraction_truncates": lambda a, x: 7 <= max(x-a, 0) % 20 <= 13,
        "omit_color_19": lambda a, x: x < 19 and edge(a, x),
    }
    count_mutants = {
        "missing_inclusive_plus_one": lambda a,b: max(0,6-dist(a,b)),
        "directed_residue_as_distance": lambda a,b: max(0,7-(b-a)%20),
        "linear_abs_as_distance": lambda a,b: max(0,7-abs(b-a)),
        "wrong_circumference_19": lambda a,b: max(0,7-min(abs(b-a),19-abs(b-a))),
    }
    killed = []
    for name, pred in edge_mutants.items():
        for a in range(20):
            for b in range(20):
                wrong = {x for x in range(20) if pred(a,x) and pred(b,x)}
                if wrong != table[a,b]:
                    killed.append({"mutation":name,"pair":[a,b],
                                   "expected":sorted(table[a,b]),"mutant":sorted(wrong)})
                    break
            else:
                continue
            break
        else:
            raise ValueError("surviving edge mutant: " + name)
    for name, pred in count_mutants.items():
        witness = next(((a,b) for a in range(20) for b in range(20)
                        if pred(a,b) != len(table[a,b])), None)
        require(witness is not None, "surviving count mutant: " + name)
        a,b = witness
        killed.append({"mutation":name,"pair":[a,b],"expected":len(table[a,b]),
                       "mutant":pred(a,b)})
    require(not table[0,7] and dist(0,7) <= 7, "threshold mutant witness")
    killed.append({"mutation":"threshold_le_7","pair":[0,7],
                   "expected":False,"mutant":True})
    for mutation in ("flip_bit", "remove_row", "duplicate_row"):
        bad = copy.deepcopy(data)
        if mutation == "flip_bit": bad["rows"][0][2] ^= 1
        elif mutation == "remove_row": bad["rows"].pop()
        else: bad["rows"][1] = bad["rows"][0][:]
        try:
            check_certificate(bad)
        except ValueError:
            killed.append({"mutation":"certificate_" + mutation,"rejected":True})
        else:
            raise ValueError("corrupt certificate accepted")
    # Preserving-extension bridge fixtures; not a generic graph proof.
    deletion = [0,7,14,7]  # u-x-y-w of the c01 five-cycle witness
    require(all(edge(x,y) for x,y in zip(deletion,deletion[1:])), "old coloring")
    require(not any(edge(z,0) and edge(z,7) for z in range(20)), "bad C5 boundary")
    full = [0,8,16,4,12]
    require(all(edge(full[i],full[(i+1)%5]) for i in range(5)), "full C5 witness")
    report = {"verdict":"candidate_only","pairs_checked":400,
              "pair_color_memberships_checked":8000,"formula_disagreements":0,
              "definition_comparisons":400,"swap_checks":400,"reflection_checks":400,
              "translation_checks":8000,"inverse_symmetry_checks":400,
              "equal_pairs":20,"antipodal_pairs":20,"endpoint_checks":80,
              "nonempty_pairs":sum(bool(v) for v in table.values()),
              "total_common_color_occurrences":sum(len(v) for v in table.values()),
              "normalized_counts":[len(table[0,t]) for t in range(11)],
              "mutations_killed":len(killed),"mutation_witnesses":killed,
              "c5_fixed_boundary_and_full_coloring":"pass",
              "trusted_verifier_receipt":False}
    out = (json.dumps(report,indent=2) + "\n").encode()
    require(len(out) <= 65536, "output cap")
    Path(sys.argv[3]).write_bytes(out)
    print(json.dumps({k:report[k] for k in ("pairs_checked","formula_disagreements",
                                          "mutations_killed","nonempty_pairs")}))


if __name__ == "__main__":
    main()
