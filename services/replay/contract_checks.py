# WORK-ID: SOL-287
# WORKSTREAM: tooling
# OWNER: oscar.duarte
# SUMMARY: Contract regression checks for replay fixtures
"""Replay support module.

Registered through the work metadata block above; keep it in sync with
docs/OPEN_WORK_INDEX.md when the item lands.
"""

from __future__ import annotations


def apply(records: list[dict]) -> list[dict]:
    """Return the records that are eligible for replay."""
    return [record for record in records if record.get('eligible')]
