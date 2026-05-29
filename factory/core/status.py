from __future__ import annotations

import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from factory.core.workspace import Workspace, write_json


STAGE_NAMES = [
    "prepare",
    "download",
    "detect",
    "device",
    "unpack",
    "inspect",
    "super_profile",
    "style",
    "repack",
    "super",
    "final_zip",
    "upload",
    "telegram",
    "cleanup",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


@dataclass
class StageRecord:
    name: str
    started_at: str = ""
    finished_at: str = ""
    status: str = "PENDING"
    duration: float = 0.0
    error: str = ""
    output_path: str = ""
    _started_monotonic: float = field(default=0.0, repr=False)

    def as_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "started_at": self.started_at,
            "finished_at": self.finished_at,
            "status": self.status,
            "duration": round(self.duration, 3),
            "error": self.error,
            "output_path": self.output_path,
        }


class StageTracker:
    def __init__(self, ws: Workspace):
        self.ws = ws
        self.records = {name: StageRecord(name=name) for name in STAGE_NAMES}
        self.write()

    def start(self, name: str) -> None:
        record = self._record(name)
        record.started_at = utc_now()
        record.finished_at = ""
        record.status = "RUNNING"
        record.error = ""
        record._started_monotonic = time.monotonic()
        self.write()

    def finish(self, name: str, status: str = "OK", error: str = "", output_path: str | Path | None = None) -> None:
        record = self._record(name)
        record.finished_at = utc_now()
        record.status = status
        if record._started_monotonic:
            record.duration = time.monotonic() - record._started_monotonic
        record.error = str(error or "")
        if output_path:
            record.output_path = str(output_path)
        self.write()

    def timeline(self) -> list[dict[str, Any]]:
        return [self.records[name].as_dict() for name in STAGE_NAMES]

    def write(self) -> Path:
        path = self.ws.reports / "stage_status.json"
        write_json(path, {"stages": self.timeline()})
        return path

    def _record(self, name: str) -> StageRecord:
        if name not in self.records:
            self.records[name] = StageRecord(name=name)
        return self.records[name]
