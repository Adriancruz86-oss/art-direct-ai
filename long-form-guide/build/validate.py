"""Validation helpers for the long-form writing guide source."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

PROHIBITED_PATTERNS = {
    "unfinished task marker": re.compile(r"\b(?:TBD|TODO)\b", re.IGNORECASE),
    "dummy filler prose": re.compile(r"lorem\s+ipsum", re.IGNORECASE),
    "tool citation token": re.compile(r"(?:filecite|turn\d+(?:search|fetch|view)\d+)", re.IGNORECASE),
    "empty markdown heading": re.compile(r"^#{1,6}\s*$", re.MULTILINE),
}


def load_markdown_sections(content_dir: Path) -> dict[str, str]:
    """Return ordered Markdown sources keyed by their two-digit prefix."""
    if not content_dir.is_dir():
        raise FileNotFoundError(f"Content directory does not exist: {content_dir}")

    sections: dict[str, str] = {}
    for path in sorted(content_dir.glob("[0-9][0-9]-*.md")):
        key = path.name[:2]
        if key in sections:
            raise ValueError(f"Duplicate content prefix {key}: {path}")
        text = path.read_text(encoding="utf-8").strip()
        if not text:
            raise ValueError(f"Content file is empty: {path}")
        sections[key] = text
    return sections


def load_yaml_records(path: Path, required_keys: set[str]) -> list[dict[str, Any]]:
    """Load a YAML list and validate record shape and unique stable IDs."""
    if not path.is_file():
        raise FileNotFoundError(f"YAML source does not exist: {path}")

    # JSON is a strict subset of YAML. Keeping these records JSON-compatible
    # makes the source portable without adding a runtime dependency.
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError(f"YAML source must contain a list: {path}")

    records: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    for index, raw in enumerate(payload, start=1):
        if not isinstance(raw, dict):
            raise ValueError(f"Record {index} is not a mapping: {path}")
        missing = required_keys - raw.keys()
        if missing:
            raise ValueError(f"Record {index} missing {sorted(missing)}: {path}")
        record_id = raw.get("id")
        if not isinstance(record_id, str) or not record_id.strip():
            raise ValueError(f"Record {index} has an invalid id: {path}")
        if record_id in seen_ids:
            raise ValueError(f"Duplicate id {record_id!r}: {path}")
        seen_ids.add(record_id)
        records.append(raw)
    return records


def find_prohibited_text(text: str) -> list[str]:
    """Return human-readable labels for publication-blocking source text."""
    return [label for label, pattern in PROHIBITED_PATTERNS.items() if pattern.search(text)]
