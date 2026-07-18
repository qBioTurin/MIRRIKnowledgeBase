#!/usr/bin/env python3
"""Validate all strains with FormOfSupply equal to Agar."""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
COMPLETE_JSON = ROOT / "private" / "complete" / "TUCC_2026-07-18.json"
DATABASE_OUTPUT = ROOT / "private" / "validation" / "database" / "Q001_formofsupply_agar.tsv"


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
        supplies = record.get("FormOfSupply", [])
        if isinstance(supplies, str):
            supplies = [supplies]
        if "Agar" in [str(value).strip() for value in supplies]:
            accessions.add(accession)
    return sorted(accessions)

def main() -> None:
    database_accessions = database_result()
    write_tsv(DATABASE_OUTPUT, database_accessions)
    print(f"database_rows={len(database_accessions)}")


if __name__ == "__main__":
    main()
