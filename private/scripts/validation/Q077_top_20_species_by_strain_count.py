#!/usr/bin/env python3
"""Validate the 20 most represented species by strain count."""

from __future__ import annotations

from collections import Counter

from validation_utils import field_value, load_complete_records, write_rows_tsv


def database_result() -> list[dict[str, str | int]]:
    counts = Counter(
        (genus, species)
        for record in load_complete_records()
        if (genus := field_value(record, "Genus")) and (species := field_value(record, "Species"))
    )
    return [
        {"genus": genus, "species": species, "strain_count": count}
        for (genus, species), count in sorted(
            counts.items(),
            key=lambda item: (-item[1], item[0][0], item[0][1]),
        )[:20]
    ]


def main() -> None:
    rows = database_result()
    write_rows_tsv("Q077_top_20_species_by_strain_count.tsv", ["genus", "species", "strain_count"], rows)
    print(f"database_rows={len(rows)}")


if __name__ == "__main__":
    main()
