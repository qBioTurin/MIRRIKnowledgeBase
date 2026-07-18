#!/usr/bin/env python3
"""Validate strain counts by RiskGroup."""

from __future__ import annotations

from collections import Counter

from validation_utils import field_value, load_complete_records, write_rows_tsv


def database_result() -> list[dict[str, str | int]]:
    counts = Counter(
        risk_group
        for record in load_complete_records()
        if (risk_group := field_value(record, "RiskGroup"))
    )
    return [
        {"riskgroup": risk_group, "strain_count": count}
        for risk_group, count in sorted(counts.items(), key=lambda item: item[0])
    ]


def main() -> None:
    rows = database_result()
    write_rows_tsv("Q074_strain_count_by_riskgroup.tsv", ["riskgroup", "strain_count"], rows)
    print(f"database_rows={len(rows)}")


if __name__ == "__main__":
    main()
