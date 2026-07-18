#!/usr/bin/env python3
"""Validate all strains with OrganismType equal to Yeasts."""

from __future__ import annotations

from validation_utils import as_values, load_complete_records, unique_sorted_accessions, write_accessions_tsv


TARGET_ORGANISM_TYPE = "Yeasts"


def database_result() -> list[str]:
    return unique_sorted_accessions(
        load_complete_records(),
        lambda record: TARGET_ORGANISM_TYPE in as_values(record.get("OrganismType")),
    )


def main() -> None:
    accessions = database_result()
    write_accessions_tsv("Q007_organismtype_yeasts.tsv", accessions)
    print(f"database_rows={len(accessions)}")


if __name__ == "__main__":
    main()
