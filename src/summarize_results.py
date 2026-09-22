"""Validate and summarize pressure-sore FEA result tables."""
from __future__ import annotations
import argparse
from pathlib import Path
import pandas as pd

REQUIRED = {
    "geometry", "pressure_kpa", "max_displacement_mm", "avg_displacement_mm",
    "max_strain", "avg_strain", "max_stress_pa", "avg_stress_pa",
}

def load_results(path: str | Path) -> pd.DataFrame:
    frame = pd.read_csv(path)
    missing = REQUIRED.difference(frame.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    numeric = REQUIRED.difference({"geometry"})
    frame[list(numeric)] = frame[list(numeric)].apply(pd.to_numeric, errors="raise")
    if (frame["pressure_kpa"] <= 0).any():
        raise ValueError("pressure_kpa must be positive")
    return frame.sort_values(["geometry", "pressure_kpa"])

def summarize(frame: pd.DataFrame) -> pd.DataFrame:
    return frame.groupby("geometry", as_index=False).agg(
        load_cases=("pressure_kpa", "count"),
        peak_displacement_mm=("max_displacement_mm", "max"),
        peak_stress_pa=("max_stress_pa", "max"),
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("csv")
    args = parser.parse_args()
    print(summarize(load_results(args.csv)).to_string(index=False))
