#!/usr/bin/env python3
"""Split every complete JSON array into per-record raw JSON files."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import quote


DATE_SUFFIX = re.compile(r"_\d{4}-\d{2}-\d{2}$")

DATASET_CONFIG = {
    "TUCC": ("microorganisms", "AccessionNumber"),
    "growth-media": ("growth-media", "Acronym"),
    "jpapers": ("jpapers", "ID"),
    "localities": ("localities", "ID"),
    "markers": ("markers", "Acronym"),
    "ontobiotope": ("ontobiotope", "ID"),
    "people": ("people", "ID"),
}


def dataset_name(input_path: Path) -> str:
    return DATE_SUFFIX.sub("", input_path.stem)


def filename_from_value(value: object) -> str:
    if value is None:
        raise ValueError("Missing identifier value")

    text = str(value)
    if not text:
        raise ValueError("Empty identifier value")

    return f"{quote(text, safe='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._-')}.json"


def split_file(input_path: Path, output_dir: Path, id_field: str) -> int:
    with input_path.open(encoding="utf-8") as input_file:
        records = json.load(input_file)

    if not isinstance(records, list):
        raise ValueError(f"Expected a JSON array in {input_path}")

    output_dir.mkdir(parents=True, exist_ok=True)
    seen_filenames: set[str] = set()

    for index, record in enumerate(records):
        if not isinstance(record, dict):
            raise ValueError(f"Expected object at array index {index} in {input_path}")

        filename = filename_from_value(record.get(id_field))
        if filename in seen_filenames:
            raise ValueError(f"Duplicate {id_field} value in {input_path}: {record.get(id_field)!r}")
        seen_filenames.add(filename)

        output_path = output_dir / filename
        with output_path.open("w", encoding="utf-8") as output_file:
            json.dump(record, output_file, ensure_ascii=False, indent=2)
            output_file.write("\n")

    return len(records)


def split_complete(complete_dir: Path, raw_dir: Path) -> dict[str, int]:
    if not complete_dir.is_dir():
        raise FileNotFoundError(f"Missing directory: {complete_dir}")

    raw_dir.mkdir(parents=True, exist_ok=True)
    results: dict[str, int] = {}

    for input_path in sorted(complete_dir.glob("*.json")):
        dataset = dataset_name(input_path)
        if dataset not in DATASET_CONFIG:
            raise ValueError(f"No split configuration for dataset: {dataset}")

        output_name, id_field = DATASET_CONFIG[dataset]
        count = split_file(input_path, raw_dir / output_name, id_field)
        results[output_name] = count

    return results


def main() -> None:
    script_path = Path(__file__).resolve()
    project_root = script_path.parents[2]

    parser = argparse.ArgumentParser(
        description="Create per-record JSON files for every complete dataset."
    )
    parser.add_argument(
        "--raw-dir",
        type=Path,
        default=project_root / "raw",
        help="Directory where generated raw JSON folders will be written.",
    )
    parser.add_argument(
        "--complete-dir",
        type=Path,
        default=project_root / "private" / "complete",
        help="Directory containing the complete JSON array files.",
    )
    args = parser.parse_args()

    results = split_complete(args.complete_dir, args.raw_dir)
    for output_name, count in results.items():
        print(f"Created {count} JSON files in {args.raw_dir / output_name}")


if __name__ == "__main__":
    main()
