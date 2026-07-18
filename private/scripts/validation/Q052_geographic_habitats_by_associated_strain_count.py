#!/usr/bin/env python3
"""Validate geographic habitats ordered by associated strain count."""

from __future__ import annotations

from collections import Counter

from validation_utils import field_value, geo_origin, load_complete_records, locality_by_id, write_rows_tsv


def database_result() -> list[dict[str, str | int]]:
    localities = locality_by_id()
    counts = Counter(
        location_id
        for record in load_complete_records()
        if (location_id := geo_origin(record))
    )
    rows = []
    for location_id, count in counts.items():
        locality = localities.get(location_id, {})
        rows.append(
            {
                "geoorigin": location_id,
                "country": field_value(locality, "Country"),
                "city": field_value(locality, "City"),
                "locality": field_value(locality, "Locality"),
                "strain_count": count,
            }
        )
    return sorted(rows, key=lambda row: (-int(row["strain_count"]), str(row["geoorigin"])))


def main() -> None:
    rows = database_result()
    write_rows_tsv(
        "Q052_geographic_habitats_by_associated_strain_count.tsv",
        ["geoorigin", "country", "city", "locality", "strain_count"],
        rows,
    )
    print(f"database_rows={len(rows)}")


if __name__ == "__main__":
    main()
