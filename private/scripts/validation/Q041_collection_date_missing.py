#!/usr/bin/env python3
"""Validate all strains with missing CollectionDate."""

from __future__ import annotations

from validation_utils import field_missing, load_complete_records, unique_sorted_accessions, write_accessions_tsv


def database_result() -> list[str]:
    return unique_sorted_accessions(
        load_complete_records(),
        lambda record: field_missing(record, "CollectionDate"),
    )


def main() -> None:
    accessions = database_result()
    write_accessions_tsv("Q041_collection_date_missing.tsv", accessions)
    print(f"database_rows={len(accessions)}")


if __name__ == "__main__":
    main()
