#!/usr/bin/env python3
"""Validate the number of strains associated with P000252."""

from __future__ import annotations

from validation_utils import load_complete_records, person_ids_for_record, write_rows_tsv


PERSON_ID = "P000252"


def database_result() -> list[dict[str, str | int]]:
    count = sum(1 for record in load_complete_records() if PERSON_ID in person_ids_for_record(record))
    return [{"person_id": PERSON_ID, "strain_count": count}]


def main() -> None:
    rows = database_result()
    write_rows_tsv("Q064_strain_count_associated_with_P000252.tsv", ["person_id", "strain_count"], rows)
    print(f"database_rows={len(rows)}")


if __name__ == "__main__":
    main()
