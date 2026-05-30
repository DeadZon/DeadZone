from __future__ import annotations

import json
import uuid
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


@dataclass
class BuildCounters:
    default_found: int = 0
    extra_apps: int = 0
    missing_apps: int = 0
    delete_candidates: int = 0
    renamed_apps: int = 0
    images_extracted: int = 0
    images_failed: int = 0
    images_total: int = 0
    stable_kept_apps: int = 0
    stable_renamed_apps: int = 0
    stable_missing_apps: int = 0
    stable_deleted_extra_apps: int = 0

    def as_dict(self) -> dict[str, int]:
        return asdict(self)

    def update(self, **kwargs: int) -> None:
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, int(value))


@dataclass
class BuildState:
    build_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    device: str = "Detecting..."
    soc: str = "Detecting..."
    edition: str = ""
    rom_version: str = "Detecting..."
    android_version: str = "Detecting..."
    current_stage: str = ""
    status: str = "RUNNING"
    progress: float = 0.0
    current_action: str = ""
    last_file: str = ""
    last_event: str = ""
    counters: BuildCounters = field(default_factory=BuildCounters)
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    started_at: str = field(default_factory=_utc_now)
    finished_at: str = ""
    _state_path: Path | None = field(default=None, repr=False, compare=False)

    def __post_init__(self) -> None:
        # Prefix build_id with style so it's traceable in logs and reports.
        if self.edition and self.edition.lower() not in ("", "unknown", "detecting..."):
            prefix = self.edition.upper()
            short = self.build_id.replace("-", "")[:8]
            self.build_id = f"DZ-{prefix}-{short}"

    def as_dict(self) -> dict[str, Any]:
        return {
            "build_id": self.build_id,
            "device": self.device,
            "soc": self.soc,
            "edition": self.edition,
            "rom_version": self.rom_version,
            "android_version": self.android_version,
            "current_stage": self.current_stage,
            "status": self.status,
            "progress": round(self.progress, 1),
            "current_action": self.current_action,
            "last_file": self.last_file,
            "last_event": self.last_event,
            "counters": self.counters.as_dict(),
            "errors": self.errors,
            "warnings": self.warnings,
            "started_at": self.started_at,
            "finished_at": self.finished_at,
        }

    def save(self) -> None:
        if self._state_path is None:
            return
        try:
            self._state_path.parent.mkdir(parents=True, exist_ok=True)
            self._state_path.write_text(
                json.dumps(self.as_dict(), indent=2) + "\n",
                encoding="utf-8",
            )
        except Exception as exc:
            print(f"[BUILD STATE] Warning: failed to save state: {exc}")

    def finish(self, status: str) -> None:
        self.status = status.upper()
        self.finished_at = _utc_now()
        self.progress = 100.0 if self.status == "OK" else self.progress
        self.save()


def create_build_state(output_dir: Path, **kwargs: Any) -> BuildState:
    state_path = output_dir / "state" / "build_state.json"
    state = BuildState(_state_path=state_path, **kwargs)
    state.save()
    return state


def load_build_state(output_dir: Path) -> dict[str, Any]:
    path = output_dir / "state" / "build_state.json"
    if not path.is_file():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}
