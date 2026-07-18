#!/usr/bin/env python3
"""Validate strain counts by city."""

from __future__ import annotations

from collections import Counter

from validation_utils import load_complete_records, locality_by_id, locality_value, write_rows_tsv


def database_result() -> list[dict[str, str | int]]:
    localities = locality_by_id()
    counts = Counter(
        city
        for record in load_complete_records()
        if (city := locality_value(record, localities, "City"))
    )
    return [{"city": city, "strain_count": count} for city, count in sorted(counts.items())]


def main() -> None:
    rows = database_result()
    write_rows_tsv("Q051_strain_count_by_city.tsv", ["city", "strain_count"], rows)
    print(f"database_rows={len(rows)}")


if __name__ == "__main__":
    main()
