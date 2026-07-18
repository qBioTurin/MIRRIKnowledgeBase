#!/usr/bin/env python3
"""Validate all strains with species Diplodia seriata."""

from __future__ import annotations

from validation_utils import field_equals, load_complete_records, unique_sorted_accessions, write_accessions_tsv


def database_result() -> list[str]:
    return unique_sorted_accessions(
        load_complete_records(),
        lambda record: field_equals(record, "Genus", "Diplodia")
        and field_equals(record, "Species", "seriata"),
    )


def main() -> None:
    accessions = database_result()
    write_accessions_tsv("Q025_species_diplodia_seriata.tsv", accessions)
    print(f"database_rows={len(accessions)}")


if __name__ == "__main__":
    main()
