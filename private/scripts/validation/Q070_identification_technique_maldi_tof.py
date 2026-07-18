#!/usr/bin/env python3
"""Validate all strains identified with MALDI-TOF."""

from __future__ import annotations

from validation_utils import load_complete_records, semicolon_values, unique_sorted_accessions, write_accessions_tsv


TARGET_TECHNIQUE = "MALDI-TOF"


def database_result() -> list[str]:
    return unique_sorted_accessions(
        load_complete_records(),
        lambda record: TARGET_TECHNIQUE in semicolon_values(record.get("IdentificationTechnique")),
    )


def main() -> None:
    accessions = database_result()
    write_accessions_tsv("Q070_identification_technique_maldi_tof.tsv", accessions)
    print(f"database_rows={len(accessions)}")


if __name__ == "__main__":
    main()
