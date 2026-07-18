#!/usr/bin/env python3
"""Validate all genera with more than 50 strains."""

from __future__ import annotations

from collections import Counter

from validation_utils import field_value, load_complete_records, write_rows_tsv


def database_result() -> list[dict[str, str | int]]:
    counts = Counter(
        genus
        for record in load_complete_records()
        if (genus := field_value(record, "Genus"))
    )
    return [
        {"genus": genus, "strain_count": count}
        for genus, count in sorted(counts.items())
        if count > 50
    ]


def main() -> None:
    rows = database_result()
    write_rows_tsv("Q030_genera_more_than_50_strains.tsv", ["genus", "strain_count"], rows)
    print(f"database_rows={len(rows)}")


if __name__ == "__main__":
    main()
