#!/usr/bin/env python3
"""Validate all strains isolated by Giovanna Cristina Varese."""

from __future__ import annotations

from validation_utils import as_values, load_complete_records, person_ids_by_name, unique_sorted_accessions, write_accessions_tsv


PERSON_NAME = "Giovanna Cristina Varese"


def database_result() -> list[str]:
    person_ids = set(person_ids_by_name(PERSON_NAME))
    return unique_sorted_accessions(
        load_complete_records(),
        lambda record: bool(person_ids.intersection(as_values(record.get("Isolator")))),
    )


def main() -> None:
    accessions = database_result()
    write_accessions_tsv("Q063_isolated_by_giovanna_cristina_varese.tsv", accessions)
    print(f"database_rows={len(accessions)}")


if __name__ == "__main__":
    main()
