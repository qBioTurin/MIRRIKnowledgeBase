#!/usr/bin/env python3
"""Validate all people associated with TUCC00000735."""

from __future__ import annotations

from collections import defaultdict

from validation_utils import as_values, accession_number, load_complete_records, people_by_id, person_label, person_roles_for_record, write_rows_tsv


TARGET_ACCESSION = "TUCC00000735"


def database_result() -> list[dict[str, str]]:
    people = people_by_id()
    target = next(record for record in load_complete_records() if accession_number(record) == TARGET_ACCESSION)
    roles_by_person: dict[str, list[str]] = defaultdict(list)
    for person_id in sorted({person_id for role in ["Collector", "Depositor", "Isolator"] for person_id in as_values(target.get(role))}):
        roles_by_person[person_id] = person_roles_for_record(target, person_id)
    return [
        {"person_id": person_id, "person_name": person_label(person_id, people), "roles": "; ".join(roles)}
        for person_id, roles in sorted(roles_by_person.items())
    ]


def main() -> None:
    rows = database_result()
    write_rows_tsv("Q066_people_associated_with_TUCC00000735.tsv", ["person_id", "person_name", "roles"], rows)
    print(f"database_rows={len(rows)}")


if __name__ == "__main__":
    main()
