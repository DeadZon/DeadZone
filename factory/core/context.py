"""
BuildContext — shared state object passed through the unpack pipeline.

All paths stored here must be absolute so that os.chdir() calls inside legacy
third_party code do not corrupt relative-path resolution.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class BuildContext:
    """Carries all paths and discovered metadata for one ROM unpack session."""

    # ── Paths ────────────────────────────────────────────────────────────────
    root_dir: Path       # repo root (c:\Users\hyper\Desktop\MEZO)
    work_dir: Path       # session scratch space (output/work/<rom_stem>/)
    input_rom: Path      # original ROM file supplied by the caller
    project_dir: Path    # directory where partitions are extracted
    output_dir: Path     # final output destination
    reports_dir: Path    # output/reports/ — where JSON/TXT reports land

    # ── Device metadata ───────────────────────────────────────────────────────
    # factory_device: injected by the caller (--device flag or env DEADZONE_DEVICE_CODENAME)
    # detected_device: what build.prop says (may be generic / placeholder)
    # effective_device: final authoritative codename used downstream
    factory_device: Optional[str] = None
    detected_device: Optional[str] = None
    effective_device: Optional[str] = None

    # ── ROM metadata ──────────────────────────────────────────────────────────
    android_version: Optional[str] = None
    mi_version: Optional[str] = None

    # ── Archive detection ─────────────────────────────────────────────────────
    archive_type: Optional[str] = None   # "zip" | "tar.gz" | "tgz" | "tar" | "img" | "dir"

    # ── Extraction results ────────────────────────────────────────────────────
    payload_found: bool = False
    super_found: bool = False
    partitions: list[str] = field(default_factory=list)
    images: list[str] = field(default_factory=list)       # standalone boot-class images

    # ── Diagnostics ───────────────────────────────────────────────────────────
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    # ─────────────────────────────────────────────────────────────────────────
    def warn(self, msg: str) -> None:
        print(f"[WARN] {msg}")
        self.warnings.append(msg)

    def error(self, msg: str) -> None:
        print(f"[ERROR] {msg}")
        self.errors.append(msg)
