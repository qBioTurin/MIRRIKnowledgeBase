"""Shared helpers for database-side validation scripts."""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
COMPLETE_JSON = ROOT / "private" / "complete" / "TUCC_2026-07-18.json"
LOCALITIES_JSON = ROOT / "private" / "complete" / "localities_2026-07-18.json"
PEOPLE_JSON = ROOT / "private" / "complete" / "people_2026-07-18.json"
DATABASE_DIR = ROOT / "private" / "validation" / "database"
PERSON_ROLE_FIELDS = ["Collector", "Depositor", "Isolator"]


def load_complete_records() -> list[dict[str, Any]]:
    with COMPLETE_JSON.open(encoding="utf-8") as handle:
        records = json.load(handle)
    if not isinstance(records, list):
        raise ValueError(f"{COMPLETE_JSON} must contain a JSON array")
    return records


def load_locality_records() -> list[dict[str, Any]]:
    with LOCALITIES_JSON.open(encoding="utf-8") as handle:
        records = json.load(handle)
    if not isinstance(records, list):
        raise ValueError(f"{LOCALITIES_JSON} must contain a JSON array")
    return records


def load_people_records() -> list[dict[str, Any]]:
    with PEOPLE_JSON.open(encoding="utf-8") as handle:
        records = json.load(handle)
    if not isinstance(records, list):
        raise ValueError(f"{PEOPLE_JSON} must contain a JSON array")
    return records


def locality_by_id() -> dict[str, dict[str, Any]]:
    return {field_value(record, "ID"): record for record in load_locality_records()}


def people_by_id() -> dict[str, dict[str, Any]]:
    return {field_value(record, "ID"): record for record in load_people_records()}


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


def field_year(record: dict[str, Any], field: str) -> str:
    value = field_value(record, field)
    return value[:4] if len(value) >= 4 and value[:4].isdigit() else ""


def field_missing(record: dict[str, Any], field: str) -> bool:
    return not as_values(record.get(field))


def semicolon_values(value: Any) -> list[str]:
    values: list[str] = []
    for item in as_values(value):
        values.extend(part.strip() for part in item.split(";") if part.strip())
    return values


def geo_origin(record: dict[str, Any]) -> str:
    return field_value(record, "GeoOrigin")


def locality_value(record: dict[str, Any], localities: dict[str, dict[str, Any]], field: str) -> str:
    locality = localities.get(geo_origin(record), {})
    return field_value(locality, field)


def person_name(person: dict[str, Any]) -> str:
    first_name = field_value(person, "FName")
    last_name = field_value(person, "LName")
    return " ".join(part for part in [first_name, last_name] if part)


def person_ids_by_name(name: str) -> list[str]:
    return sorted(
        field_value(person, "ID")
        for person in load_people_records()
        if person_name(person) == name and field_value(person, "ID")
    )


def person_label(person_id: str, people: dict[str, dict[str, Any]] | None = None) -> str:
    people = people if people is not None else people_by_id()
    person = people.get(person_id, {})
    return person_name(person) or person_id


def person_ids_for_record(record: dict[str, Any]) -> set[str]:
    ids: set[str] = set()
    for field in PERSON_ROLE_FIELDS:
        ids.update(as_values(record.get(field)))
    return ids


def person_roles_for_record(record: dict[str, Any], person_id: str) -> list[str]:
    return [field for field in PERSON_ROLE_FIELDS if person_id in as_values(record.get(field))]
