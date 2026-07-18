#!/usr/bin/env python3
"""Validate all strains associated with Parco del Meisino - Orto 53."""

from __future__ import annotations

from validation_utils import load_complete_records, locality_by_id, locality_value, unique_sorted_accessions, write_accessions_tsv


TARGET_LOCALITY = "Parco del Meisino - Orto 53"


def database_result() -> list[str]:
    localities = locality_by_id()
    return unique_sorted_accessions(
        load_complete_records(),
        lambda record: locality_value(record, localities, "Locality") == TARGET_LOCALITY,
    )


def main() -> None:
    accessions = database_result()
    write_accessions_tsv("Q049_geoorigin_locality_parco_del_meisino_orto_53.tsv", accessions)
    print(f"database_rows={len(accessions)}")


if __name__ == "__main__":
    main()
