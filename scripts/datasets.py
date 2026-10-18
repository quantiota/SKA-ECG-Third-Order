"""The two datasets: where their second-order results are, where the third order is written."""
import pathlib

import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parent.parent
PROJECT = ROOT.parent
SECOND_ORDER = PROJECT / "SKA-ECG-Second-Order"
AGING_SELECTED = PROJECT / "SKA-ECG-Starter-Kit" / "data" / "selected_scales.csv"


def folder(ds):
    """aging/ or ptb/, with data/, figures/, vr/."""
    if ds not in ("aging", "ptb"):
        raise SystemExit("dataset: aging or ptb")
    f = ROOT / ds
    for sub in ("data", "figures", "vr"):
        (f / sub).mkdir(parents=True, exist_ok=True)
    return f


def second_order_csv(ds, rec, s1, s2):
    """The second-order run of this record (SKA-ECG-Second-Order)."""
    return SECOND_ORDER / ds / "data" / f"ska2_{rec}_scale{s1:g}_scale{s2:g}.csv"


def record(ds, rec):
    return rec.zfill(4) if ds == "aging" else rec


def source(ds, rec):
    """The database line of a description."""
    if ds == "aging":
        sel = pd.read_csv(AGING_SELECTED, dtype={"record_id": str})
        age = sel.set_index("record_id").age_band.get(rec, "?").replace("-", "–")
        return f"Record {rec}, PhysioNet Autonomic Aging (woman {age}, lead ECG1, 1000 Hz)"
    return f"Record {rec}, PhysioNet PTB Diagnostic ECG Database (lead II, 1000 Hz)"
