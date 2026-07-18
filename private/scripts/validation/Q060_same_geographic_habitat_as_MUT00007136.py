#!/usr/bin/env python3
"""Validate all strains sharing geographic habitat with MUT00007136."""

from __future__ import annotations

from validation_utils import accession_number, geo_origin, load_complete_records, write_accessions_tsv


TARGET_ACCESSION = "MUT00007136"


def database_result() -> list[str]:
    records = load_complete_records()
    target = next(record for record in records if accession_number(record) == TARGET_ACCESSION)
    target_geo_origin = geo_origin(target)
    accessions = {
        accession
        for record in records
        if (accession := accession_number(record))
        and accession != TARGET_ACCESSION
        and geo_origin(record) == target_geo_origin
    }
    return sorted(accessions)


def main() -> None:
    accessions = database_result()
    write_accessions_tsv("Q060_same_geographic_habitat_as_MUT00007136.tsv", accessions)
    print(f"database_rows={len(accessions)}")


if __name__ == "__main__":
    main()
