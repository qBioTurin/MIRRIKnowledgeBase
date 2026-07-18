#!/usr/bin/env python3
"""Validate organisms similar to MUT00007136 by same species."""

from __future__ import annotations

from validation_utils import accession_number, field_value, load_complete_records, write_accessions_tsv


TARGET_ACCESSION = "MUT00007136"


def database_result() -> list[str]:
    records = load_complete_records()
    target = next(record for record in records if accession_number(record) == TARGET_ACCESSION)
    target_genus = field_value(target, "Genus")
    target_species = field_value(target, "Species")
    accessions = {
        accession
        for record in records
        if (accession := accession_number(record))
        and accession != TARGET_ACCESSION
        and field_value(record, "Genus") == target_genus
        and field_value(record, "Species") == target_species
    }
    return sorted(accessions)


def main() -> None:
    accessions = database_result()
    write_accessions_tsv("Q034_similar_to_MUT00007136_same_species.tsv", accessions)
    print(f"database_rows={len(accessions)}")


if __name__ == "__main__":
    main()
