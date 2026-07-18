#!/usr/bin/env python3
"""Validate the number of distinct species for each genus."""

from __future__ import annotations

from collections import defaultdict

from validation_utils import field_value, load_complete_records, write_rows_tsv


def database_result() -> list[dict[str, str | int]]:
    species_by_genus: dict[str, set[str]] = defaultdict(set)
    for record in load_complete_records():
        genus = field_value(record, "Genus")
        species = field_value(record, "Species")
        if genus and species:
            species_by_genus[genus].add(species)
    return [
        {"genus": genus, "distinct_species_count": len(species)}
        for genus, species in sorted(species_by_genus.items())
    ]


def main() -> None:
    rows = database_result()
    write_rows_tsv("Q029_distinct_species_count_by_genus.tsv", ["genus", "distinct_species_count"], rows)
    print(f"database_rows={len(rows)}")


if __name__ == "__main__":
    main()
