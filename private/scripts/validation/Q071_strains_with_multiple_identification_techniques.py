#!/usr/bin/env python3
"""Validate all strains with more than one identification technique."""

from __future__ import annotations

from validation_utils import accession_number, load_complete_records, semicolon_values, write_rows_tsv


def database_result() -> list[dict[str, str | int]]:
    rows = []
    for record in load_complete_records():
        accession = accession_number(record)
        techniques = semicolon_values(record.get("IdentificationTechnique"))
        if accession and len(techniques) > 1:
            rows.append(
                {
                    "accessionnumber": accession,
                    "technique_count": len(techniques),
                    "identificationtechniques": "; ".join(techniques),
                }
            )
    return sorted(rows, key=lambda row: (-int(row["technique_count"]), str(row["accessionnumber"])))


def main() -> None:
    rows = database_result()
    write_rows_tsv(
        "Q071_strains_with_multiple_identification_techniques.tsv",
        ["accessionnumber", "technique_count", "identificationtechniques"],
        rows,
    )
    print(f"database_rows={len(rows)}")


if __name__ == "__main__":
    main()
