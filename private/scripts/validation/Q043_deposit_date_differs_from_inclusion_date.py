#!/usr/bin/env python3
"""Validate all strains whose DepositDate differs from InclusionDate."""

from __future__ import annotations

from validation_utils import accession_number, field_value, load_complete_records, write_rows_tsv


def database_result() -> list[dict[str, str]]:
    rows = []
    for record in load_complete_records():
        accession = accession_number(record)
        deposit_date = field_value(record, "DepositDate")
        inclusion_date = field_value(record, "InclusionDate")
        if accession and deposit_date and inclusion_date and deposit_date != inclusion_date:
            rows.append(
                {
                    "accessionnumber": accession,
                    "depositdate": deposit_date,
                    "inclusiondate": inclusion_date,
                }
            )
    return sorted(rows, key=lambda row: row["accessionnumber"])


def main() -> None:
    rows = database_result()
    write_rows_tsv(
        "Q043_deposit_date_differs_from_inclusion_date.tsv",
        ["accessionnumber", "depositdate", "inclusiondate"],
        rows,
    )
    print(f"database_rows={len(rows)}")


if __name__ == "__main__":
    main()
