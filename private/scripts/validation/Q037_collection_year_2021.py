#!/usr/bin/env python3
"""Validate all strains collected in 2021."""

from __future__ import annotations

from validation_utils import field_year, load_complete_records, unique_sorted_accessions, write_accessions_tsv


def database_result() -> list[str]:
    return unique_sorted_accessions(
        load_complete_records(),
        lambda record: field_year(record, "CollectionDate") == "2021",
    )


def main() -> None:
    accessions = database_result()
    write_accessions_tsv("Q037_collection_year_2021.tsv", accessions)
    print(f"database_rows={len(accessions)}")


if __name__ == "__main__":
    main()
