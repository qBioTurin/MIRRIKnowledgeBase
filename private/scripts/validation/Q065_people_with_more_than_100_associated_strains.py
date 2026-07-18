#!/usr/bin/env python3
"""Validate all people with more than 100 associated strains."""

from __future__ import annotations

from collections import Counter

from validation_utils import load_complete_records, people_by_id, person_ids_for_record, person_label, write_rows_tsv


def database_result() -> list[dict[str, str | int]]:
    counts = Counter()
    for record in load_complete_records():
        for person_id in person_ids_for_record(record):
            counts[person_id] += 1
    people = people_by_id()
    rows = [
        {"person_id": person_id, "person_name": person_label(person_id, people), "strain_count": count}
        for person_id, count in counts.items()
        if count > 100
    ]
    return sorted(rows, key=lambda row: (-int(row["strain_count"]), str(row["person_id"])))


def main() -> None:
    rows = database_result()
    write_rows_tsv(
        "Q065_people_with_more_than_100_associated_strains.tsv",
        ["person_id", "person_name", "strain_count"],
        rows,
    )
    print(f"database_rows={len(rows)}")


if __name__ == "__main__":
    main()
