"""Shared helpers for database-side validation scripts."""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
COMPLETE_JSON = ROOT / "private" / "complete" / "TUCC_2026-07-18.json"
DATABASE_DIR = ROOT / "private" / "validation" / "database"


def load_complete_records() -> list[dict[str, Any]]:
    with COMPLETE_JSON.open(encoding="utf-8") as handle:
        records = json.load(handle)
    if not isinstance(records, list):
        raise ValueError(f"{COMPLETE_JSON} must contain a JSON array")
    return records


def as_values(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    text = str(value).strip()
    return [text] if text else []


def accession_number(record: dict[str, Any]) -> str:
    return str(record.get("AccessionNumber", "")).strip()


def write_accessions_tsv(filename: str, accessionnumbers: list[str]) -> Path:
    path = DATABASE_DIR / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["accessionnumber"])
        for accessionnumber in accessionnumbers:
            writer.writerow([accessionnumber])
    return path


def write_rows_tsv(filename: str, fieldnames: list[str], rows: list[dict[str, Any]]) -> Path:
    path = DATABASE_DIR / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    return path


def unique_sorted_accessions(records: list[dict[str, Any]], predicate) -> list[str]:
    accessions = {
        accession
        for record in records
        if (accession := accession_number(record)) and predicate(record)
    }
    return sorted(accessions)


def field_equals(record: dict[str, Any], field: str, target: str) -> bool:
    return target in as_values(record.get(field))


def field_value(record: dict[str, Any], field: str) -> str:
    values = as_values(record.get(field))
    return values[0] if values else ""
