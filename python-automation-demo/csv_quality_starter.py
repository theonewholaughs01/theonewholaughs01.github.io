#!/usr/bin/env python3
"""Small, transparent CSV quality-check demonstrator.

This script does not silently rewrite a client's data. It produces:
1. a normalized copy with trimmed text and normalized blank values,
2. a JSON quality report,
3. a CSV issue log for duplicate rows and missing values.

It is a starter demonstrator, not production software. Review outputs before delivery.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any

BLANK_MARKERS = {"", "na", "n/a", "null", "none", "-"}


def normalize(value: str) -> str:
    """Trim whitespace and convert common blank markers to an empty string."""
    cleaned = value.strip()
    if cleaned.lower() in BLANK_MARKERS:
        return ""
    return cleaned


def inspect_csv(input_path: Path, output_dir: Path) -> dict[str, Any]:
    """Create cleaned output, issue log, and quality report for one CSV file."""
    output_dir.mkdir(parents=True, exist_ok=True)
    cleaned_path = output_dir / f"{input_path.stem}_cleaned.csv"
    issues_path = output_dir / f"{input_path.stem}_issues.csv"
    report_path = output_dir / f"{input_path.stem}_quality_report.json"

    with input_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError("The CSV has no header row.")
        fieldnames = [name.strip() for name in reader.fieldnames]
        rows = []
        for row_number, row in enumerate(reader, start=2):
            normalized = {key.strip(): normalize(row.get(key, "")) for key in reader.fieldnames}
            normalized["__row_number__"] = row_number
            rows.append(normalized)

    issues: list[dict[str, str]] = []
    seen: dict[tuple[str, ...], int] = {}
    missing_by_column = {column: 0 for column in fieldnames}

    for row in rows:
        row_number = str(row["__row_number__"])
        signature = tuple(row[column] for column in fieldnames)
        if signature in seen:
            issues.append(
                {
                    "row_number": row_number,
                    "issue_type": "duplicate_row",
                    "column": "",
                    "details": f"Same normalized row as row {seen[signature]}; review before removing.",
                }
            )
        else:
            seen[signature] = int(row_number)

        for column in fieldnames:
            if row[column] == "":
                missing_by_column[column] += 1
                issues.append(
                    {
                        "row_number": row_number,
                        "issue_type": "missing_or_blank",
                        "column": column,
                        "details": "Value is blank or matched a common blank marker.",
                    }
                )

    with cleaned_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({column: row[column] for column in fieldnames})

    with issues_path.open("w", encoding="utf-8", newline="") as handle:
        issue_fields = ["row_number", "issue_type", "column", "details"]
        writer = csv.DictWriter(handle, fieldnames=issue_fields)
        writer.writeheader()
        writer.writerows(issues)

    report = {
        "input_file": str(input_path),
        "output_files": {
            "cleaned_csv": str(cleaned_path),
            "issues_csv": str(issues_path),
        },
        "row_count": len(rows),
        "column_count": len(fieldnames),
        "columns": fieldnames,
        "duplicate_row_issues": sum(issue["issue_type"] == "duplicate_row" for issue in issues),
        "missing_or_blank_issues": sum(issue["issue_type"] == "missing_or_blank" for issue in issues),
        "missing_by_column": missing_by_column,
        "assumptions": [
            "Whitespace was trimmed from headers and cell values.",
            "Common blank markers were converted to empty strings.",
            "Duplicate rows were reported but not deleted.",
            "No business rule was inferred for dates, categories, IDs, or required fields.",
        ],
    }
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description="Check and normalize one CSV file transparently.")
    parser.add_argument("input_csv", type=Path, help="Path to the source CSV")
    parser.add_argument("--output-dir", type=Path, default=Path("quality_output"))
    args = parser.parse_args()
    report = inspect_csv(args.input_csv, args.output_dir)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
