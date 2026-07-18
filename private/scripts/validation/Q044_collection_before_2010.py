#!/usr/bin/env python3
"""Validate all strains collected before 2010."""

from __future__ import annotations

from validation_utils import field_year, load_complete_records, unique_sorted_accessions, write_accessions_tsv


def database_result() -> list[str]:
    return unique_sorted_accessions(
        load_complete_records(),
        lambda record: (year := field_year(record, "CollectionDate")) != "" and int(year) < 2010,
    )


def main() -> None:
    accessions = database_result()
    write_accessions_tsv("Q044_collection_before_2010.tsv", accessions)
    print(f"database_rows={len(accessions)}")


if __name__ == "__main__":
    main()
