#!/usr/bin/env python3
"""Third-order SKA learning: the learner reads the return of P₂ weighted by the direction of
the second-order run, one step per cycle.

    u_k = (z₂, ż₂, P₂) of cycle k, a point of the second-order cube
    s_k = u_k - u_k-1, the segment between two successive points
    c3_k = cos(s_k, s_k-1),   v3_k = (P₂_k - P₂_k-1) / P₂_k-1 * c3_k
    input  x_k = sigmoid(SCALE3 * v3_k)

v3_k is known at cycle k, so the step carries that time and the learner's dt3 is the
time between two cycles. Output, per cycle:
    z3 = ‖Z₃‖,  dt3,  zdot3 = dz3/dt3 (1/s),  P3 = exp(−|ΔH₃/H₃|)
The SKA learner is not included in this repository: set SKA_ENGINE to the folder holding
ska_core.py (default: ../SKA-ECG-Heart-Rate-Variability/ecg-ska-engine).

Usage
    python scripts/learn_third_order.py aging 0060 25 25 25    # first, second, third-order scales
        → aging/data/ska3_0060_scale25_scale25_scale25.csv
Requires: SKA-ECG-Second-Order/<dataset>/data/ska2_<record>_scale<s1>_scale<s2>.csv, numpy, pandas, torch
"""
import datetime as dt
import os
import pathlib
import sys

import numpy as np
import pandas as pd

from datasets import PROJECT, folder, record, second_order_csv

ENGINE = pathlib.Path(os.getenv("SKA_ENGINE", PROJECT / "SKA-ECG-Heart-Rate-Variability" / "ecg-ska-engine"))
sys.path.insert(0, str(ENGINE))
from ska_core import SKALearner                                   # noqa: E402


def main():
    ds, rec = sys.argv[1], sys.argv[2]
    s1, s2, s3 = (float(a) for a in sys.argv[3:6])
    rec, f = record(ds, rec), folder(ds)
    sec = pd.read_csv(second_order_csv(ds, rec, s1, s2)).dropna(subset=["P2", "zdot2"]).reset_index(drop=True)
    s = np.diff(sec[["z2", "zdot2", "P2"]].to_numpy(float), axis=0)
    c3 = (s[1:] * s[:-1]).sum(1) / (np.linalg.norm(s[1:], axis=1) * np.linalg.norm(s[:-1], axis=1))
    d = pd.DataFrame({"k": sec.k, "t": sec.t, "retP2": sec.P2 / sec.P2.shift() - 1, "c3": np.r_[np.nan, np.nan, c3]})
    d["v3"] = d.retP2 * d.c3
    d = d.dropna().reset_index(drop=True)
    d["x"] = 1.0 / (1.0 + np.exp(-np.clip(s3 * d.v3, -500, 500)))
    t0 = dt.datetime(2000, 1, 1)
    L, rows = SKALearner(init_std=0.01), []
    for e in d.itertuples():
        r = L.step(float(e.x), t0 + dt.timedelta(milliseconds=round(1000 * e.t)), int(e.k))
        Z, D = r["Z"], r["D"]
        rows.append({"k": e.k, "t": e.t, "retP2": e.retP2, "c3": e.c3, "v3": e.v3, "x": e.x, "z3": float(np.linalg.norm(Z)),
                     "decision3": float(D[-1]) if len(D) else 0.5, "entropy3": r["entropy"],
                     "dt3": r.get("delta_t")})
    out = pd.DataFrame(rows)
    H = out.entropy3.to_numpy(float)
    out["P3"] = np.r_[np.nan, np.exp(-np.abs(np.diff(H) / H[1:]))]
    out["zdot3"] = np.gradient(out.z3.to_numpy(float)) / out.dt3.to_numpy(float)
    csv = f / "data" / f"ska3_{rec}_scale{s1:g}_scale{s2:g}_scale{s3:g}.csv"
    out.to_csv(csv, index=False, float_format="%.6g")
    print(f"saved {csv}  ({len(out)} steps, x {d.x.min():.4f}..{d.x.max():.4f})")


if __name__ == "__main__":
    main()
