"""Solstice serving stage module 015.

Managed by the platform program office; see docs/OPEN_WORK_INDEX.md.
"""

from __future__ import annotations


def process_serving_015(record: dict) -> dict:
    """Return a normalized copy of ``record``."""
    return {key: value for key, value in record.items() if value is not None}
