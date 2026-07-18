#!/usr/bin/env python3
"""Validate all strains with GeoOrigin but missing IsolationHabitat."""

from __future__ import annotations

from validation_utils import field_missing, geo_origin, load_complete_records, unique_sorted_accessions, write_accessions_tsv


def database_result() -> list[str]:
    return unique_sorted_accessions(
        load_complete_records(),
        lambda record: bool(geo_origin(record)) and field_missing(record, "IsolationHabitat"),
    )


def main() -> None:
    accessions = database_result()
    write_accessions_tsv("Q057_geoorigin_present_isolation_habitat_missing.tsv", accessions)
    print(f"database_rows={len(accessions)}")


if __name__ == "__main__":
    main()
