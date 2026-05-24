"""Generic edition build package patcher.

Applies a build/ folder (or downloaded archive) partition-relative to a ROM tree.
Every top-level folder inside the build package must be a known ROM partition.
Unknown top-level folders cause an immediate FAILED result.
"""
from __future__ import annotations

import shutil
from pathlib import Path
from typing import Optional

_ALLOWED_PARTITIONS = frozenset({"system", "product", "system_ext", "vendor", "odm", "mi_ext"})


def apply_build_package(
    root: Path,
    build_dir: Optional[Path],
    build_url: Optional[str],
    edition: str,
    allowed_partitions: frozenset[str] = _ALLOWED_PARTITIONS,
    execute: bool = False,
) -> dict:
    """Copy build package contents into the unpacked ROM tree.

    build_dir takes priority over build_url.
    Returns a status dict compatible with the editions runner step format.
    """
    errors: list[str] = []
    warnings: list[str] = []
    copied: list[str] = []
    unknown_partitions: list[str] = []

    source = build_dir
    if source is None and build_url:
        return {
            "status": "SKIPPED_TEMPORARY",
            "reason": f"build_url download not yet implemented for {edition} edition",
            "warnings": [f"SKIPPED_TEMPORARY: set {edition.upper()}_BUILD_URL and implement download"],
            "errors": [],
        }

    if source is None or not source.is_dir():
        return {
            "status": "SKIPPED_TEMPORARY",
            "reason": f"build/ folder missing for {edition} edition",
            "warnings": [],
            "errors": [],
        }

    # Validate top-level folders
    for entry in sorted(source.iterdir()):
        if not entry.is_dir():
            warnings.append(f"non-directory top-level item ignored: {entry.name}")
            continue
        if entry.name not in allowed_partitions:
            unknown_partitions.append(entry.name)

    if unknown_partitions:
        return {
            "status": "FAILED",
            "unknown_partitions": unknown_partitions,
            "errors": [
                f"Unknown top-level partition(s) in {edition} build package: {unknown_partitions}. "
                f"Allowed: {sorted(allowed_partitions)}"
            ],
            "warnings": warnings,
        }

    if not execute:
        partitions_found = [e.name for e in source.iterdir() if e.is_dir()]
        return {
            "status": "DRY_RUN",
            "partitions": partitions_found,
            "warnings": warnings,
            "errors": [],
        }

    # Apply: copy files partition-relative
    for part_dir in sorted(source.iterdir()):
        if not part_dir.is_dir():
            continue
        dest_part = root / part_dir.name
        dest_part.mkdir(parents=True, exist_ok=True)
        for src_file in part_dir.rglob("*"):
            if not src_file.is_file():
                continue
            rel = src_file.relative_to(part_dir)
            dest_file = dest_part / rel
            dest_file.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src_file, dest_file)
            copied.append(f"{part_dir.name}/{rel.as_posix()}")

    return {
        "status": "APPLIED",
        "files_copied": len(copied),
        "copied": copied,
        "warnings": warnings,
        "errors": errors,
    }
