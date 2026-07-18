#!/usr/bin/env python3
"""Validate the number of distinct genera."""

from __future__ import annotations

from validation_utils import field_value, load_complete_records, write_rows_tsv


def database_result() -> list[dict[str, int]]:
    genera = {field_value(record, "Genus") for record in load_complete_records() if field_value(record, "Genus")}
    return [{"distinct_genera": len(genera)}]


def main() -> None:
    rows = database_result()
    write_rows_tsv("Q028_distinct_genera_count.tsv", ["distinct_genera"], rows)
    print(f"database_rows={len(rows)}")


if __name__ == "__main__":
    main()
