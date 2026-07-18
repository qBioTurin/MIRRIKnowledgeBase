#!/usr/bin/env python3
"""Validate all genera with both bacterial and fungal strains."""

from __future__ import annotations

from collections import Counter, defaultdict

from validation_utils import field_value, load_complete_records, write_rows_tsv


FUNGAL_TYPES = {"Filamentous Fungi", "Yeasts"}


def database_result() -> list[dict[str, str | int]]:
    organism_types_by_genus: dict[str, set[str]] = defaultdict(set)
    strain_counts = Counter()
    for record in load_complete_records():
        genus = field_value(record, "Genus")
        organism_type = field_value(record, "OrganismType")
        if genus and organism_type:
            organism_types_by_genus[genus].add(organism_type)
            strain_counts[genus] += 1

    rows = []
    for genus, organism_types in sorted(organism_types_by_genus.items()):
        has_bacteria = "Bacteria" in organism_types
        has_fungi = bool(FUNGAL_TYPES.intersection(organism_types))
        if has_bacteria and has_fungi:
            rows.append(
                {
                    "genus": genus,
                    "organism_types": "; ".join(sorted(organism_types)),
                    "strain_count": strain_counts[genus],
                }
            )
    return rows


def main() -> None:
    rows = database_result()
    write_rows_tsv(
        "Q032_genera_with_bacterial_and_fungal_strains.tsv",
        ["genus", "organism_types", "strain_count"],
        rows,
    )
    print(f"database_rows={len(rows)}")


if __name__ == "__main__":
    main()
