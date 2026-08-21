# Python Automation Data Quality Demo

A beginner-friendly Python demonstration for cleaning and validating a safe sample CSV, recording issues, and producing a quality report.

> **Demonstration project — no client data or client results claimed.**

## What it demonstrates

This project follows a small, repeatable workflow:

```text
input → transform → validate → document
```

It is designed to show how a Python utility can:

- read a CSV file;
- normalize common text and date fields;
- identify missing values and duplicate rows;
- write a cleaned CSV;
- record issues in a readable log; and
- produce a compact JSON quality report.

## Files

| File | Purpose |
|---|---|
| `csv_quality_starter.py` | The demonstration command-line script. |
| `test_fixture.csv` | Safe synthetic input data. It contains no client or personal data. |

## Run the demonstration

Use Python 3.11 or a compatible Python 3 installation:

```bash
python3 csv_quality_starter.py test_fixture.csv --out-dir out
```

The script writes a cleaned CSV, an issue log, and a JSON report to the output directory. Use `--help` to view the available options.

## Verification

The script is intended to be run on a copy of the input. Review the generated files and compare the quality report with the fixture before adapting the workflow to another dataset.

## Scope and limitations

This is a portfolio demonstration, not a production data platform or a client case study. It does not claim business savings, client outcomes, enterprise reliability, regulated-data handling, or advanced analytics. It should not be used with passwords, payment data, identity documents, medical records, or other highly sensitive information.

A real project would begin with a written scope, a harmless sample or schema, explicit transformation rules, an agreed acceptance check, and documented handover.

## About the author

Oluwafolafunmi is an entry-level developer focused on practical Python automation, data processing, debugging, testing, and documentation. AI-assisted development and open-source resources may be used responsibly during research and implementation, with generated code reviewed and tested before delivery.

## Related service

For a small, clearly defined Python automation or data-processing workflow, contact the author through the public profile links. Initial discussions should use a workflow description or redacted/synthetic sample rather than confidential data.
