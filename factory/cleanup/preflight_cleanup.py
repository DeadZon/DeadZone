"""Preflight cleanup — removes stale intermediate files before every build.

Run this before download and before any build stages to ensure:
  - No stale output/work files from a previous run
  - No old final images or ZIPs competing with the new build
  - Enough disk space for the new build
  - No confusion from partial downloads or leftover payload dumps

Preserved:
  output/reports/   — build reports from previous runs (for debugging)
  output/logs/      — log files from previous runs

Writes output/reports/cleanup_report.txt.
"""
from __future__ import annotations

import shutil
import time
from pathlib import Path


def preflight_cleanup(
    output_dir: Path | str,
    project_root: Path | str | None = None,
) -> dict:
    """Delete stale build intermediates before a new build starts.

    Parameters
    ----------
    output_dir:
        Factory output directory (typically ``output/``).
    project_root:
        Repository root.  When not supplied, inferred as ``output_dir.parent``.
        Used to clean ``_input_roms/``, ``*_unpacked/`` dirs at root level.
    """
    output_dir = Path(output_dir)
    project_root = Path(project_root) if project_root else output_dir.parent

    removed: list[str] = []
    preserved: list[str] = []
    errors: list[str] = []
    t0 = time.monotonic()

    def _rm(path: Path) -> None:
        if not path.exists():
            return
        try:
            if path.is_dir():
                shutil.rmtree(path)
            else:
                path.unlink()
            removed.append(str(path))
            print(f"[preflight_cleanup] removed: {path}")
        except Exception as exc:
            errors.append(f"remove {path}: {exc}")
            print(f"[preflight_cleanup] ERROR removing {path}: {exc}")

    # ── output/ intermediate directories ─────────────────────────────────────
    _rm(output_dir / "work")
    _rm(output_dir / "tmp")
    _rm(output_dir / "images" / "source")
    _rm(output_dir / "images" / "final")
    _rm(output_dir / "final")

    # ── project-root level download and unpack directories ────────────────────
    _rm(project_root / "_input_roms")

    for unp in project_root.glob("*_unpacked"):
        if unp.is_dir():
            _rm(unp)

    # ── stale super / payload temp files ─────────────────────────────────────
    for pattern in [
        "super_parts",
        "super_workspace",
        "eu_adapter",
        "unpacked_rom",
        "source_images",
    ]:
        _rm(output_dir / pattern)

    # Remove leftover ZIP staging directories
    for p in output_dir.rglob("*_fastboot"):
        if p.is_dir() and p.name.endswith("_fastboot"):
            _rm(p)

    # Remove split super chunks at project root or work level
    for chunk in list(project_root.glob("super.img.*")) + list((output_dir / "work").glob("super.img.*") if (output_dir / "work").exists() else []):
        _rm(chunk)

    # ── Preserved directories ─────────────────────────────────────────────────
    for keep in [output_dir / "reports", output_dir / "logs"]:
        if keep.exists():
            preserved.append(str(keep))

    duration = round(time.monotonic() - t0, 2)

    result = {
        "status": "APPLIED",
        "removed": removed,
        "preserved": preserved,
        "errors": errors,
        "duration_seconds": duration,
    }

    # Write cleanup report
    _write_preflight_report(output_dir / "reports", result)
    return result


def _write_preflight_report(reports_dir: Path, result: dict) -> None:
    try:
        reports_dir.mkdir(parents=True, exist_ok=True)
        removed = result.get("removed") or []
        preserved = result.get("preserved") or []
        errors = result.get("errors") or []
        lines = [
            "=" * 60,
            "  DeadZone Factory — Preflight Cleanup Report",
            "=" * 60,
            f"  Status               : {result.get('status')}",
            f"  Duration             : {result.get('duration_seconds')}s",
            f"  Removed paths        : {len(removed)}",
            f"  Preserved paths      : {len(preserved)}",
            f"  Errors               : {len(errors)}",
            "",
            "  Removed:",
        ]
        for p in removed:
            lines.append(f"    - {p}")
        if not removed:
            lines.append("    (none)")
        lines += ["", "  Preserved:"]
        for p in preserved:
            lines.append(f"    + {p}")
        if not preserved:
            lines.append("    (none)")
        if errors:
            lines += ["", "  Errors:"]
            for e in errors:
                lines.append(f"    ! {e}")
        lines.append("=" * 60)
        (reports_dir / "preflight_cleanup_report.txt").write_text(
            "\n".join(lines) + "\n", encoding="utf-8"
        )
    except Exception as exc:
        print(f"[preflight_cleanup] Warning: could not write preflight_cleanup_report.txt: {exc}")
