from __future__ import annotations

import os
import sys
import threading
import time
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from factory.state.build_state import BuildState

_RICH_AVAILABLE: bool | None = None

_DETECTING = "Detecting..."
_UNKNOWN = "Unknown"


def _try_import_rich() -> bool:
    global _RICH_AVAILABLE
    if _RICH_AVAILABLE is not None:
        return _RICH_AVAILABLE
    try:
        import rich  # noqa: F401
        _RICH_AVAILABLE = True
    except ImportError:
        _RICH_AVAILABLE = False
    return _RICH_AVAILABLE


def _is_github_actions() -> bool:
    return os.environ.get("GITHUB_ACTIONS", "").lower() in {"1", "true"}


def _is_interactive() -> bool:
    try:
        return sys.stderr.isatty()
    except Exception:
        return False


def _bar(progress: float, width: int = 30) -> str:
    filled = int(min(width, max(0, progress / 100.0 * width)))
    return "[" + "#" * filled + "-" * (width - filled) + "]"


def _elapsed_str(started_at_ts: float) -> str:
    elapsed = int(max(0, time.monotonic() - started_at_ts))
    m, s = divmod(elapsed, 60)
    return f"{m:02d}:{s:02d}"


def _display(value: str, in_progress: bool = True) -> str:
    """Return the value for display; blank/unknown becomes Detecting... or Unknown."""
    v = (value or "").strip()
    if not v or v.lower() == "unknown":
        return _DETECTING if in_progress else _UNKNOWN
    return v


class LiveScreen:
    def __init__(
        self,
        build_state: "BuildState",
        *,
        enabled: bool = True,
        gha_interval: float = 120.0,
        interactive_interval: float = 2.0,
    ) -> None:
        self._state = build_state
        self._enabled = enabled
        self._gha = _is_github_actions()
        self._interactive = _is_interactive() and not self._gha
        self._has_rich = _try_import_rich()
        self._interval = gha_interval if (self._gha or not self._interactive) else interactive_interval
        self._stop = threading.Event()
        self._thread: threading.Thread | None = None
        self._monotonic_start = time.monotonic()
        self._last_stage_printed: str = ""
        self._last_gha_print: float = 0.0

    def start(self) -> None:
        if not self._enabled:
            return
        self._print_header()
        self._thread = threading.Thread(target=self._run, name="DeadZoneLiveScreen", daemon=True)
        self._thread.start()

    def stop(self, final_status: str = "DONE") -> None:
        self._stop.set()
        if self._thread:
            self._thread.join(timeout=5.0)
        self._print_final(final_status)

    def _run(self) -> None:
        if self._has_rich and self._interactive:
            self._run_rich()
        else:
            self._run_simple()

    # ------------------------------------------------------------------
    # Rich interactive mode — redraws a compact panel on stderr
    # ------------------------------------------------------------------

    def _run_rich(self) -> None:
        try:
            from rich.console import Console
            from rich.live import Live

            console = Console(stderr=True, highlight=False)
            with Live(console=console, refresh_per_second=1, transient=False) as live:
                while not self._stop.is_set():
                    live.update(self._rich_panel())
                    self._stop.wait(self._interval)
                live.update(self._rich_panel())
        except Exception:
            self._run_simple()

    def _rich_panel(self) -> Any:
        try:
            from rich.panel import Panel
        except ImportError:
            return None
        body = "\n".join(self._status_lines())
        return Panel(
            body,
            title="[bold cyan]DeadZone Factory Live[/bold cyan]",
            border_style="cyan",
            expand=False,
        )

    # ------------------------------------------------------------------
    # Simple mode — stage-change or timed one-liner to stderr
    # GitHub Actions: only print when stage changes or 2-min timeout
    # ------------------------------------------------------------------

    def _run_simple(self) -> None:
        while not self._stop.is_set():
            self._maybe_print_tick()
            self._stop.wait(min(self._interval, 15.0))

    def _maybe_print_tick(self) -> None:
        state = self._state
        current_stage = state.current_stage or ""
        now = time.monotonic()
        stage_changed = current_stage != self._last_stage_printed
        timeout_elapsed = (now - self._last_gha_print) >= self._interval
        if self._gha and not stage_changed and not timeout_elapsed:
            return
        self._last_stage_printed = current_stage
        self._last_gha_print = now
        self._print_tick()

    def _print_tick(self) -> None:
        state = self._state
        elapsed = _elapsed_str(self._monotonic_start)
        stage = state.current_stage or "(init)"
        action = state.current_action or "..."
        line = (
            f"[LIVE | {elapsed}] "
            f"Stage: {stage} | "
            f"Style: {state.edition or _DETECTING} | "
            f"Status: {state.status} | "
            f"Progress: {state.progress:.0f}% {_bar(state.progress, 20)} | "
            f"Action: {action}"
        )
        counters = state.counters
        if counters.default_found or counters.extra_apps or counters.missing_apps:
            line += (
                f" | Apps: found={counters.default_found}"
                f" extra={counters.extra_apps}"
                f" missing={counters.missing_apps}"
            )
        if counters.stable_kept_apps or counters.stable_deleted_extra_apps or counters.stable_missing_apps:
            line += (
                f" | StablePolicy: kept={counters.stable_kept_apps}"
                f" renamed={counters.stable_renamed_apps}"
                f" missing={counters.stable_missing_apps}"
                f" deleted={counters.stable_deleted_extra_apps}"
            )
        if counters.images_total:
            line += f" | Images: {counters.images_extracted}/{counters.images_total}"
        print(line, file=sys.stderr, flush=True)

    # ------------------------------------------------------------------
    # Header / footer helpers
    # ------------------------------------------------------------------

    def _print_header(self) -> None:
        state = self._state
        lines = [
            "=" * 60,
            "  DeadZone Factory Live",
            "  Developer: Mezo",
            f"  Style     : {state.edition or _DETECTING}",
            f"  Device    : {_display(state.device)}",
            f"  ROM       : {_display(state.rom_version)}",
            f"  Android   : {_display(state.android_version)}",
            f"  SoC       : {_display(state.soc)}",
            f"  Build ID  : {state.build_id}",
            "=" * 60,
        ]
        for line in lines:
            print(line, file=sys.stderr, flush=True)

    def _print_final(self, status: str) -> None:
        state = self._state
        elapsed = _elapsed_str(self._monotonic_start)
        counters = state.counters
        lines = [
            "=" * 60,
            f"  DeadZone Factory {status} — {elapsed}",
            f"  Style       : {state.edition or _UNKNOWN}",
            f"  Device      : {_display(state.device, in_progress=False)}",
            f"  Final stage : {state.current_stage or _UNKNOWN}",
            f"  Progress    : {state.progress:.0f}% {_bar(state.progress, 20)}",
        ]
        if counters.default_found or counters.extra_apps or counters.missing_apps:
            lines.append(
                f"  Apps found  : {counters.default_found}"
                f" | extra: {counters.extra_apps}"
                f" | missing: {counters.missing_apps}"
            )
        if counters.stable_kept_apps or counters.stable_deleted_extra_apps or counters.stable_missing_apps:
            lines.append(
                f"  Stable policy: kept={counters.stable_kept_apps}"
                f" renamed={counters.stable_renamed_apps}"
                f" missing={counters.stable_missing_apps}"
                f" deleted={counters.stable_deleted_extra_apps}"
            )
        if counters.images_total:
            lines.append(
                f"  Images      : {counters.images_extracted}/{counters.images_total} extracted"
            )
        lines.append("=" * 60)
        for line in lines:
            print(line, file=sys.stderr, flush=True)

    def _status_lines(self) -> list[str]:
        state = self._state
        elapsed = _elapsed_str(self._monotonic_start)
        counters = state.counters
        running = state.status == "RUNNING"

        lines = [
            "Developer : Mezo",
            f"Style     : {state.edition or _DETECTING}",
            f"Device    : {_display(state.device, running)}",
            f"ROM       : {_display(state.rom_version, running)}",
            f"Android   : {_display(state.android_version, running)}",
            f"SoC       : {_display(state.soc, running)}",
            "",
            f"Stage     : {state.current_stage or '(init)'}",
            f"Status    : {state.status}",
            f"Progress  : {state.progress:.0f}% {_bar(state.progress, 28)}",
            f"Elapsed   : {elapsed}",
            "",
            f"Action    : {state.current_action or '...'}",
            f"Last file : {state.last_file or '...'}",
            f"Last event: {state.last_event or '...'}",
        ]

        # App counters — only when scan has produced real data
        app_data = any([
            counters.default_found,
            counters.extra_apps,
            counters.missing_apps,
            counters.delete_candidates,
            counters.renamed_apps,
        ])
        if app_data:
            lines += [
                "",
                f"Apps found       : {counters.default_found}",
                f"Apps extra       : {counters.extra_apps}",
                f"Apps missing     : {counters.missing_apps}",
                f"Delete candidates: {counters.delete_candidates}",
                f"Renamed apps     : {counters.renamed_apps}",
            ]

        # Stable App Policy counters — only when policy has run
        stable_data = any([
            counters.stable_kept_apps,
            counters.stable_renamed_apps,
            counters.stable_missing_apps,
            counters.stable_deleted_extra_apps,
        ])
        if stable_data:
            lines += [
                "",
                f"Stable kept      : {counters.stable_kept_apps}",
                f"Stable renamed   : {counters.stable_renamed_apps}",
                f"Stable missing   : {counters.stable_missing_apps}",
                f"Stable deleted   : {counters.stable_deleted_extra_apps}",
            ]

        # Image counters — only when extraction has started
        if counters.images_total:
            lines.append(f"Images extracted : {counters.images_extracted}/{counters.images_total}")

        return lines

    def update_rom_info(self, device: str = "", rom_version: str = "", android_version: str = "") -> None:
        state = self._state
        if device:
            state.device = device
        if rom_version:
            state.rom_version = rom_version
        if android_version:
            state.android_version = android_version
