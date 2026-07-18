#!/usr/bin/env python3
"""Validate all strains collected in Italy."""

from __future__ import annotations

from validation_utils import load_complete_records, locality_by_id, locality_value, unique_sorted_accessions, write_accessions_tsv


def database_result() -> list[str]:
    localities = locality_by_id()
    return unique_sorted_accessions(
        load_complete_records(),
        lambda record: locality_value(record, localities, "Country") == "Italy",
    )


def main() -> None:
    accessions = database_result()
    write_accessions_tsv("Q047_geoorigin_country_italy.tsv", accessions)
    print(f"database_rows={len(accessions)}")


if __name__ == "__main__":
    main()
