"""Compare the pressure response of my three tissue-model geometries."""
from __future__ import annotations
import argparse
import pandas as pd

REQUIRED = {"geometry", "pressure_kpa", "max_displacement_mm", "max_strain", "max_stress_pa"}

def compare(path: str) -> pd.DataFrame:
    frame = pd.read_csv(path)
    missing = REQUIRED.difference(frame.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    frame = frame.copy()
    for column in REQUIRED - {"geometry"}:
        frame[column] = pd.to_numeric(frame[column], errors="raise")
    if frame.duplicated(["geometry", "pressure_kpa"]).any():
        raise ValueError("Each geometry and pressure combination must be unique")
    table = frame.pivot(index="pressure_kpa", columns="geometry",
                        values=["max_displacement_mm", "max_strain", "max_stress_pa"])
    return table.sort_index()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare matched FEA load cases by geometry.")
    parser.add_argument("csv")
    args = parser.parse_args()
    print(compare(args.csv).round(4).to_string())
