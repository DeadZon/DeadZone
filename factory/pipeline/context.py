"""BuildContext — shared state passed through the entire factory pipeline."""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional


@dataclass
class BuildContext:
    # Inputs
    codename: str
    edition: str
    rom_url: Optional[str] = None
    mode: str = "dry_run"

    # Resolved from registry
    soc: Optional[str] = None
    platform: Optional[str] = None
    device_model: Optional[str] = None
    super_size: int = 9126805504
    slot_mode: str = "VAB"

    # Runtime paths
    rom_path: Optional[Path] = None
    project_dir: Optional[Path] = None
    output_dir: Optional[Path] = None
    images_dir: Optional[Path] = None
    final_dir: Optional[Path] = None

    # Detected from ROM
    android_version: Optional[str] = None
    mi_incremental: Optional[str] = None

    # Upload / notify
    upload_pixeldrain: bool = False
    notify_telegram: bool = False

    # Results
    final_zip: Optional[str] = None
    pixeldrain_link: Optional[str] = None
    telegram_message_id: Optional[int] = None

    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    stage_reports: dict[str, Any] = field(default_factory=dict)

    @property
    def execute(self) -> bool:
        return self.mode == "execute"

    @property
    def build_name(self) -> str:
        """Canonical output name per spec: DeadZone_<codename>[_<Edition>]_V1."""
        from factory.pipeline.resolver import resolve_output_name
        return resolve_output_name(self.codename, self.edition)
