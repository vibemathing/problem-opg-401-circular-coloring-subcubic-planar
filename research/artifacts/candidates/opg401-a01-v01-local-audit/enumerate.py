"""Generate all 400 intersections directly; the closed form is not used."""
import json
import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 3:
        raise ValueError("usage: enumerate.py input.json certificate.json")
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    if (data.get("p"), data.get("q")) != (20, 7):
        raise ValueError("this frozen audit accepts only p=20, q=7")
    rows, counts = [], []
    for a in range(20):
        count_row = []
        for b in range(20):
            common = []
            for x in range(20):
                # Direct two-edge predicate, with neither distance nor formula.
                if 7 <= (x - a) % 20 <= 13 and 7 <= (x - b) % 20 <= 13:
                    common.append(x)
            rows.append([a, b, sum(1 << x for x in common)])
            count_row.append(len(common))
        counts.append(count_row)
    result = {"format": "opg401-pair-masks-v1", "p": 20, "q": 7,
              "row_order": "a major, then b; bit x means color x is allowed",
              "rows": rows, "counts": counts, "verdict": "candidate_only"}
    encoded = (json.dumps(result, separators=(",", ":")) + "\n").encode()
    if len(encoded) > 65536:
        raise ValueError("output exceeds fixed 64 KiB bound")
    Path(sys.argv[2]).write_bytes(encoded)
    print(json.dumps({"pairs": len(rows), "candidate_colors_examined": 8000,
                      "certificate_bytes": len(encoded)}))


if __name__ == "__main__":
    main()
