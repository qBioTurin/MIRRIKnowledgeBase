#!/usr/bin/env python3
"""Validate all strains whose Substrate contains wood."""

from __future__ import annotations

from validation_utils import as_values, load_complete_records, unique_sorted_accessions, write_accessions_tsv


TARGET_TEXT = "wood"


def database_result() -> list[str]:
    target = TARGET_TEXT.casefold()
    return unique_sorted_accessions(
        load_complete_records(),
        lambda record: any(target in value.casefold() for value in as_values(record.get("Substrate"))),
    )


def main() -> None:
    accessions = database_result()
    write_accessions_tsv("Q003_substrate_contains_wood.tsv", accessions)
    print(f"database_rows={len(accessions)}")


if __name__ == "__main__":
    main()
