#!/usr/bin/env python3
"""Validate all strains whose IsolationHabitat contains soil."""

from __future__ import annotations

from validation_utils import as_values, load_complete_records, unique_sorted_accessions, write_accessions_tsv


TARGET_TEXT = "soil"


def database_result() -> list[str]:
    target = TARGET_TEXT.casefold()
    return unique_sorted_accessions(
        load_complete_records(),
        lambda record: any(target in value.casefold() for value in as_values(record.get("IsolationHabitat"))),
    )


def main() -> None:
    accessions = database_result()
    write_accessions_tsv("Q056_isolation_habitat_contains_soil.tsv", accessions)
    print(f"database_rows={len(accessions)}")


if __name__ == "__main__":
    main()
