from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from factory.core.stage_registry import (
    BUILD_STAGE_MAP,
    progress_for_completed_stages,
    registry_stage_for,
)
from factory.state.build_state import BuildState


def _utc_ms() -> str:
    return (
        datetime.now(timezone.utc)
        .isoformat(timespec="milliseconds")
        .replace("+00:00", "Z")
    )


class EventBus:
    def __init__(self, output_dir: Path, build_state: BuildState | None = None) -> None:
        self.output_dir = output_dir
        self.build_state = build_state
        self.events_path = output_dir / "logs" / "events.ndjson"
        self._completed_registry_stages: set[str] = set()
        self._ensure_dir()

    def _ensure_dir(self) -> None:
        try:
            self.events_path.parent.mkdir(parents=True, exist_ok=True)
            if not self.events_path.exists():
                self.events_path.write_text("", encoding="utf-8")
        except Exception as exc:
            print(f"[EVENT BUS] Warning: failed to initialise events log: {exc}")

    def emit_event(
        self,
        stage: str,
        status: str,
        message: str,
        progress: float | None = None,
        file: str | None = None,
        data: dict[str, Any] | None = None,
    ) -> None:
        event: dict[str, Any] = {
            "timestamp": _utc_ms(),
            "stage": stage,
            "status": status,
            "message": message,
            "file": file or "",
            "progress": progress,
            "data": data or {},
        }
        self._write_event(event)
        if self.build_state is not None:
            self._update_state(stage, status, message, progress, file)

    def _write_event(self, event: dict[str, Any]) -> None:
        try:
            with self.events_path.open("a", encoding="utf-8") as fh:
                fh.write(json.dumps(event, ensure_ascii=False) + "\n")
        except Exception as exc:
            print(f"[EVENT BUS] Warning: failed to write event: {exc}")

    def _update_state(
        self,
        stage: str,
        status: str,
        message: str,
        progress: float | None,
        file: str | None,
    ) -> None:
        state = self.build_state
        assert state is not None
        state.current_stage = stage
        state.current_action = message
        if file:
            state.last_file = file

        upper = status.upper()
        if upper in {"OK", "DONE", "COMPLETE", "SUCCESS"}:
            reg = registry_stage_for(stage)
            self._completed_registry_stages.add(reg)

        if progress is not None:
            state.progress = float(progress)
        else:
            state.progress = progress_for_completed_stages(self._completed_registry_stages)

        if upper in {"FAIL", "FAILED", "ERROR"}:
            state.status = "FAILED"
            err = f"[{stage}] {message}"
            if err not in state.errors:
                state.errors.append(err)

        state.save()

    def copy_events_to(self, destination: Path) -> None:
        if not self.events_path.is_file():
            return
        try:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(self.events_path.read_bytes())
        except Exception as exc:
            print(f"[EVENT BUS] Warning: failed to copy events log: {exc}")

    def read_recent_events(self, n: int = 20) -> list[dict[str, Any]]:
        if not self.events_path.is_file():
            return []
        try:
            lines = self.events_path.read_text(encoding="utf-8").splitlines()
            result = []
            for line in lines[-n:]:
                line = line.strip()
                if line:
                    try:
                        result.append(json.loads(line))
                    except json.JSONDecodeError:
                        pass
            return result
        except Exception:
            return []
