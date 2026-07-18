#!/usr/bin/env python3
"""Validate all strains with Substrate equal to Soil contaminated by PAHs."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
COMPLETE_JSON = ROOT / "private" / "complete" / "TUCC_2026-07-18.json"
DATABASE_OUTPUT = (
    ROOT
    / "private"
    / "validation"
    / "database"
    / "Q002_substrate_soil_contaminated_by_pahs.tsv"
)
TARGET_SUBSTRATE = "Soil contaminated by PAHs"


def write_tsv(path: Path, accessionnumbers: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["accessionnumber"])
        for accessionnumber in accessionnumbers:
            writer.writerow([accessionnumber])


def database_result() -> list[str]:
    with COMPLETE_JSON.open(encoding="utf-8") as handle:
        records = json.load(handle)

    accessions = set()
    for record in records:
        accession = str(record.get("AccessionNumber", "")).strip()
        substrate = record.get("Substrate")
        if isinstance(substrate, list):
            substrates = [str(value).strip() for value in substrate]
        else:
            substrates = [str(substrate).strip()] if substrate is not None else []
        if TARGET_SUBSTRATE in substrates:
            accessions.add(accession)
    return sorted(accessions)


def main() -> None:
    accessions = database_result()
    write_tsv(DATABASE_OUTPUT, accessions)
    print(f"database_rows={len(accessions)}")


if __name__ == "__main__":
    main()
