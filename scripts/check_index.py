#!/usr/bin/env python
"""Lint the open work index.

Checks the mechanical rules only: column count, status vocabulary, duplicate
Work IDs and the documented sort order.  Content coverage is reviewed by the
program office.

Usage: python scripts/check_index.py [path]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

STATUS = {"planned", "in-progress", "review", "blocked", "shipped"}
WORKSTREAMS = ["ingestion", "platform", "quality", "serving", "tooling", "transform"]


def parse_rows(path: Path):
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != 5:
            if set(cells) <= {"---", "Work ID", "Workstream", "Summary", "Owner", "Status"}:
                continue
            raise SystemExit(f"bad column count ({len(cells)}): {line}")
        if cells[0] == "Work ID":
            continue
        if set(cells[0]) == {"-"}:
            continue
        rows.append(cells)
    return rows


def main() -> int:
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "docs/OPEN_WORK_INDEX.md")
    if not path.exists():
        print(f"missing index file: {path}")
        return 1
    rows = parse_rows(path)
    ids = [row[0] for row in rows]
    if len(ids) != len(set(ids)):
        print("duplicate Work IDs found")
        return 1
    bad_status = [row for row in rows if row[4] not in STATUS]
    if bad_status:
        print(f"invalid status values: {bad_status[:3]}")
        return 1
    def key(row):
        ws_index = WORKSTREAMS.index(row[1]) if row[1] in WORKSTREAMS else 99
        number = int(row[0].split("-")[1])
        return (ws_index, number)
    if any(key(rows[i]) > key(rows[i + 1]) for i in range(len(rows) - 1)):
        print("rows are not sorted by workstream then Work ID")
        return 1
    print(f"index ok: {len(rows)} rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
