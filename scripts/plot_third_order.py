#!/usr/bin/env python3
"""Figure of a third-order run: the cube (z₃, ż₃, P₃) and P₃ along the cycle index,
coloured by the input learned, v₃ = ln(P₂_k / P₂_k−1) · c₃.

Usage
    python scripts/plot_third_order.py aging 0060 25 25 25
        → aging/figures/ska3_0060_scale25_scale25_scale25.png
Requires: <dataset>/data/ska3_<record>_scale<s1>_scale<s2>_scale<s3>.csv (learn_third_order.py), pandas, matplotlib
"""
import sys

import matplotlib
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from datasets import folder, record


def main():
    ds, rec = sys.argv[1], sys.argv[2]
    s1, s2, s3 = (float(a) for a in sys.argv[3:6])
    rec, f = record(ds, rec), folder(ds)
    tag = f"scale{s1:g}_scale{s2:g}_scale{s3:g}"
    d = pd.read_csv(f / "data" / f"ska3_{rec}_{tag}.csv").dropna(subset=["P3", "zdot3"])
    v = max(abs(d.v3.quantile(.02)), abs(d.v3.quantile(.98)))
    kw = dict(c=d.v3, cmap="coolwarm", vmin=-v, vmax=v, s=6)
    fig = plt.figure(figsize=(13, 5.5))
    ax = fig.add_subplot(1, 2, 1, projection="3d")
    sc = ax.scatter(d.z3, d.zdot3, d.P3, **kw)
    ax.set_xlabel("z₃"); ax.set_ylabel("ż₃ (1/s)"); ax.set_zlabel("P₃")
    fig.colorbar(sc, ax=ax, shrink=.6, label="v₃ = ln(P₂ₖ/P₂ₖ₋₁) · c₃")
    b = fig.add_subplot(1, 2, 2)
    b.scatter(d.k, d.P3, **kw)
    b.set_xlabel("cycle index k"); b.set_ylabel("P₃"); b.grid(alpha=.3)
    fig.suptitle(f"Record {rec}: third-order SKA learning of the return of P₂ times c₃ "
                 f"(scales {s1:g} / {s2:g} / {s3:g})")
    fig.tight_layout()
    out = f / "figures" / f"ska3_{rec}_{tag}.png"
    fig.savefig(out, dpi=120)
    print(f"saved {out}")


if __name__ == "__main__":
    main()
