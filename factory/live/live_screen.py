from __future__ import annotations

import os
import sys
import threading
import time
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from factory.state.build_state import BuildState

_RICH_AVAILABLE: bool | None = None


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


class LiveScreen:
    def __init__(
        self,
        build_state: "BuildState",
        *,
        enabled: bool = True,
        gha_interval: float = 30.0,
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
            from rich.panel import Panel
            from rich.text import Text

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
            from rich.text import Text
        except ImportError:
            return None
        state = self._state
        lines = self._status_lines()
        body = "\n".join(lines)
        return Panel(
            body,
            title="[bold cyan]DeadZone Factory Live[/bold cyan]",
            border_style="cyan",
            expand=False,
        )

    # ------------------------------------------------------------------
    # Simple mode — periodic one-liner to stderr (GitHub Actions / no TTY)
    # ------------------------------------------------------------------

    def _run_simple(self) -> None:
        while not self._stop.is_set():
            self._print_tick()
            self._stop.wait(self._interval)

    def _print_tick(self) -> None:
        state = self._state
        elapsed = _elapsed_str(self._monotonic_start)
        line = (
            f"[LIVE | {elapsed}] "
            f"Stage: {state.current_stage or '(init)'} | "
            f"Status: {state.status} | "
            f"Progress: {state.progress:.0f}% {_bar(state.progress, 20)} | "
            f"Action: {state.current_action or '...'}"
        )
        counters = state.counters
        if counters.default_found or counters.extra_apps or counters.missing_apps:
            line += (
                f" | Apps: found={counters.default_found} "
                f"extra={counters.extra_apps} "
                f"missing={counters.missing_apps}"
            )
        if counters.images_total:
            line += (
                f" | Images: {counters.images_extracted}/{counters.images_total}"
            )
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
            f"  Edition   : {state.edition or 'unknown'}",
            f"  Device    : {state.device or 'unknown'}",
            f"  ROM       : {state.rom_version or 'pending detection'}",
            f"  Android   : {state.android_version or 'pending detection'}",
            f"  SoC       : {state.soc or 'unknown'}",
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
            f"  Final stage : {state.current_stage}",
            f"  Progress    : {state.progress:.0f}% {_bar(state.progress, 20)}",
            f"  Apps found  : {counters.default_found} | extra: {counters.extra_apps} | missing: {counters.missing_apps}",
            f"  Images      : {counters.images_extracted}/{counters.images_total} extracted",
            "=" * 60,
        ]
        for line in lines:
            print(line, file=sys.stderr, flush=True)

    def _status_lines(self) -> list[str]:
        state = self._state
        elapsed = _elapsed_str(self._monotonic_start)
        counters = state.counters
        return [
            f"Developer : Mezo",
            f"Edition   : {state.edition or 'unknown'}",
            f"Device    : {state.device or 'unknown'}",
            f"ROM       : {state.rom_version or 'pending'}",
            f"Android   : {state.android_version or 'pending'}",
            f"SoC       : {state.soc or 'unknown'}",
            "",
            f"Stage     : {state.current_stage or '(init)'}",
            f"Status    : {state.status}",
            f"Progress  : {state.progress:.0f}% {_bar(state.progress, 28)}",
            f"Elapsed   : {elapsed}",
            "",
            f"Action    : {state.current_action or '...'}",
            f"Last file : {state.last_file or '...'}",
            "",
            f"Apps found       : {counters.default_found}",
            f"Apps extra       : {counters.extra_apps}",
            f"Apps missing     : {counters.missing_apps}",
            f"Delete candidates: {counters.delete_candidates}",
            f"Renamed apps     : {counters.renamed_apps}",
            f"Images extracted : {counters.images_extracted}/{counters.images_total}",
        ]

    def update_rom_info(self, device: str = "", rom_version: str = "", android_version: str = "") -> None:
        state = self._state
        if device:
            state.device = device
        if rom_version:
            state.rom_version = rom_version
        if android_version:
            state.android_version = android_version
