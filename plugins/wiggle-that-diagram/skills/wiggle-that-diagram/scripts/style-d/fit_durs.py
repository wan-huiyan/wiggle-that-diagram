#!/usr/bin/env python3
# Print the DURS array a style D film needs to pass the reading rule. Input: beats.<cut>.json written by film_beats.js.
"""Suggest per-shot durations that pass pace_check.py, never shorter than the film's current ones.

  python3 fit_durs.py beats.public.json [--step 0.5] [--pad 0.0]

Prints a JS array to paste into DURS.<cut>: max(current, the reading floor rounded UP to --step, plus --pad).
Same rule as scripts/common/pace_check.py (it imports that file), so a pasted array passes it.
"""
import json, math, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "common"))
from pace_check import toks  # noqa: E402

args = [a for a in sys.argv[1:] if not a.startswith("--")]
if not args:
    sys.exit(__doc__)
step = float(sys.argv[sys.argv.index("--step") + 1]) if "--step" in sys.argv else 0.5
pad = float(sys.argv[sys.argv.index("--pad") + 1]) if "--pad" in sys.argv else 0.0
data = json.loads(Path(args[0]).read_text())
for film, spec in data.items():
    if film.startswith("_"):
        continue
    seen, out = set(), []
    for b in spec["beats"]:
        cw = toks(b["caption"])
        pw = toks(b.get("picture", ""))
        new = list(dict.fromkeys(t for t in pw if t not in set(cw) and t not in seen))
        seen |= set(pw)
        floor = max(4.5, (len(cw) + len(new)) / 3 + 1.5) + pad
        out.append(max(float(b["dur"]), math.ceil(floor / step - 1e-9) * step))
    print(f"{film}: [{', '.join(f'{d:.1f}' for d in out)}]  total {sum(out):.1f} s")
