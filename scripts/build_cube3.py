#!/usr/bin/env python3
"""3D cube (HTML, Three.js, WebXR) of a third-order run: one point per cycle.

Axes: z₃ = ‖Z₃‖, ż₃ = dz₃/dt₃ (1/s), P₃ = exp(−|ΔH₃/H₃|) of the third-order learner.
Colour = the sign of the input it learned, v₃ = (P₂_k − P₂_k−1) / P₂_k−1 · c₃. With dt, the vertical axis is Δt₃ (ms), the time
between two cycles, instead of P₃. Open the HTML file in a browser.

Usage
    python scripts/build_cube3.py aging 0060 25 25 25    # → aging/vr/ska3_ecg_0060_scale25_scale25_scale25_vr.html
    python scripts/build_cube3.py aging 0060 25 25 25 dt # → aging/vr/ska3_ecg_0060_scale25_scale25_scale25_dt_vr.html
Requires: <dataset>/data/ska3_<record>_scale<s1>_scale<s2>_scale<s3>.csv (learn_third_order.py), pandas
"""
import json
import sys

import pandas as pd

from datasets import ROOT, folder, record, source

NAMES = ["v₃ ≥ 0", "v₃ < 0"]
COLORS = ["#e8604c", "#3987e5"]


def main():
    ds, rec = sys.argv[1], sys.argv[2]
    s1, s2, s3 = (float(a) for a in sys.argv[3:6])
    dt = len(sys.argv) > 6 and sys.argv[6] == "dt"                    # vertical axis = dt3 (ms), not P3
    rec, f = record(ds, rec), folder(ds)
    tag = f"scale{s1:g}_scale{s2:g}_scale{s3:g}"
    d = pd.read_csv(f / "data" / f"ska3_{rec}_{tag}.csv").dropna(subset=["P3", "zdot3"])
    D = dict(z=d.z3.round(3).tolist(), zd=d.zdot3.round(4).tolist(), p=d.P3.round(4).tolist(),
             t=[0 if r >= 0 else 1 for r in d.v3], names=NAMES, colors=COLORS,
             zmax=float(d.z3.max()), zdmax=float(d.zdot3.max()))
    if dt:
        D["p"] = (1000 * d.dt3).round(1).tolist()
        D["ymax"] = float(1000 * d.dt3.max())
    desc = (f"{source(ds, rec)}. Third-order SKA learning, {len(d):,} steps, one per cycle. "
            f"Input: v₃ = (P₂_k − P₂_k−1) / P₂_k−1 · c₃_k, c₃_k = cos(s_k, s_k−1), s_k = the segment between two successive points "
            f"(z₂, ż₂, P₂) of the second-order run (first-order scale {s1:g}, "
            f"second-order scale {s2:g}); third-order scale {s3:g}. Horizontal axes: z₃ = ‖Z₃‖ and "
            f"ż₃ = dz₃/dt₃ (1/s), dt₃ = the time between two cycles; "
            + ("vertical axis: Δt₃, the time between two cycles (ms). " if dt else "vertical axis: P₃ = exp(−|ΔH₃/H₃|). ")
            + "2 colours = the sign of v₃.")
    s = (ROOT / "scripts" / ("ska_ecg_vr_template_dt.html" if dt else "ska_ecg_vr_template.html")).read_text(encoding="utf-8")
    s = s.replace("__DATA__", json.dumps(D, separators=(",", ":"), ensure_ascii=False)).replace("__DESCRIPTION__", desc)
    out = f / "vr" / f"ska3_ecg_{rec}_{tag}{'_dt' if dt else ''}_vr.html"
    out.write_text(s, encoding="utf-8")
    print(f"saved {out}  ({len(d):,} steps)")


if __name__ == "__main__":
    main()
