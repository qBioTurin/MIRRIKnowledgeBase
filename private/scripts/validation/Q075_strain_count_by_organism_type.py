#!/usr/bin/env python3
"""Validate strain counts by OrganismType."""

from __future__ import annotations

from collections import Counter

from validation_utils import field_value, load_complete_records, write_rows_tsv


def database_result() -> list[dict[str, str | int]]:
    counts = Counter(
        organism_type
        for record in load_complete_records()
        if (organism_type := field_value(record, "OrganismType"))
    )
    return [
        {"organismtype": organism_type, "strain_count": count}
        for organism_type, count in sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    ]


def main() -> None:
    rows = database_result()
    write_rows_tsv("Q075_strain_count_by_organism_type.tsv", ["organismtype", "strain_count"], rows)
    print(f"database_rows={len(rows)}")


if __name__ == "__main__":
    main()
