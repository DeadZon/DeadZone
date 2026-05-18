"""
Thin helpers for writing structured reports to disk.
Used by factory/unpack/report.py and future pipeline stages.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def write_json_report(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False, default=str)


def write_text_report(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as fh:
        fh.write(content)
