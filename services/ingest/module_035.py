"""Solstice ingest stage module 035.

Managed by the platform program office; see docs/OPEN_WORK_INDEX.md.
"""

from __future__ import annotations


def process_ingest_035(record: dict) -> dict:
    """Return a normalized copy of ``record``."""
    return {key: value for key, value in record.items() if value is not None}
