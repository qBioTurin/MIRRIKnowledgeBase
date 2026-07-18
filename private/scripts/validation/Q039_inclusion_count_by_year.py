#!/usr/bin/env python3
"""Validate strain inclusion counts by year."""

from __future__ import annotations

from collections import Counter

from validation_utils import field_year, load_complete_records, write_rows_tsv


def database_result() -> list[dict[str, str | int]]:
    counts = Counter(
        year
        for record in load_complete_records()
        if (year := field_year(record, "InclusionDate"))
    )
    return [{"year": year, "strain_count": count} for year, count in sorted(counts.items())]


def main() -> None:
    rows = database_result()
    write_rows_tsv("Q039_inclusion_count_by_year.tsv", ["year", "strain_count"], rows)
    print(f"database_rows={len(rows)}")


if __name__ == "__main__":
    main()
