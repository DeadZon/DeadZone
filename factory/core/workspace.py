from __future__ import annotations

import json
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Workspace:
    root: Path
    input: Path
    extracted: Path
    images: Path
    partitions: Path
    meta: Path
    reports: Path
    logs: Path
    final: Path


def create_workspace(root: Path = Path("output/workspace"), clean: bool = True) -> Workspace:
    root = Path(root)
    if clean and root.exists():
        shutil.rmtree(root)
    final_root = root.parent / "final"
    if clean and final_root.exists():
        shutil.rmtree(final_root)
    # Keep all generated state under one Universal Core workspace.
    ws = Workspace(
        root=root,
        input=root / "input",
        extracted=root / "extracted",
        images=root / "images",
        partitions=root / "partitions",
        meta=root / "meta",
        reports=root / "reports",
        logs=root / "logs",
        final=final_root,
    )
    for path in ws.__dict__.values():
        Path(path).mkdir(parents=True, exist_ok=True)
    return ws


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def read_json(path: Path, default: dict[str, Any] | None = None) -> dict[str, Any]:
    if not path.is_file():
        return default or {}
    return json.loads(path.read_text(encoding="utf-8"))
