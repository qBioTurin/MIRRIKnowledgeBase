#!/usr/bin/env python3
"""Validate strain counts by country."""

from __future__ import annotations

from collections import Counter

from validation_utils import load_complete_records, locality_by_id, locality_value, write_rows_tsv


def database_result() -> list[dict[str, str | int]]:
    localities = locality_by_id()
    counts = Counter(
        country
        for record in load_complete_records()
        if (country := locality_value(record, localities, "Country"))
    )
    return [{"country": country, "strain_count": count} for country, count in sorted(counts.items())]


def main() -> None:
    rows = database_result()
    write_rows_tsv("Q050_strain_count_by_country.tsv", ["country", "strain_count"], rows)
    print(f"database_rows={len(rows)}")


if __name__ == "__main__":
    main()
