"""Preflight cleanup — removes stale intermediate files before every build.

Run this before download and before any build stages to ensure:
  - No stale output/work files from a previous run
  - No old final images or ZIPs competing with the new build
  - Enough disk space for the new build
  - No confusion from partial downloads or leftover payload dumps

Preserved always:
  output/reports/   — build reports from previous runs (for debugging)
  output/logs/      — log files from previous runs

Preserved when active ROM is inside _input_roms/:
  _input_roms/      — the directory is kept when preserve_paths contains a
                      path inside it, so the downloaded ROM is not deleted.

Writes output/reports/preflight_cleanup_report.txt.
"""
from __future__ import annotations

import shutil
import time
from pathlib import Path


def preflight_cleanup(
    output_dir: Path | str,
    project_root: Path | str | None = None,
    preserve_paths: list[Path] | None = None,
    delete_input_roms: bool = True,
) -> dict:
    """Delete stale build intermediates before a new build starts.

    Parameters
    ----------
    output_dir:
        Factory output directory (typically ``output/``).
    project_root:
        Repository root.  When not supplied, inferred as ``output_dir.parent``.
        Used to clean ``_input_roms/``, ``*_unpacked/`` dirs at root level.
    preserve_paths:
        List of paths that must NOT be deleted.  If any path in this list
        lives inside ``_input_roms/`` (or is ``_input_roms/`` itself), the
        entire ``_input_roms/`` directory is preserved so a downloaded ROM
        is not wiped out before detect_rom can read it.
    delete_input_roms:
        When False, always skip deleting ``_input_roms/`` regardless of
        ``preserve_paths``.  Useful when the caller knows a ROM was already
        downloaded there and wants it kept unconditionally.
    """
    output_dir = Path(output_dir)
    project_root = Path(project_root) if project_root else output_dir.parent

    preserve_paths = [Path(p).resolve() for p in (preserve_paths or [])]
    input_roms_dir = (project_root / "_input_roms").resolve()

    # Determine whether _input_roms should be preserved
    _skip_input_roms = not delete_input_roms
    if not _skip_input_roms and preserve_paths:
        for pp in preserve_paths:
            try:
                pp.relative_to(input_roms_dir)
                _skip_input_roms = True
                break
            except ValueError:
                pass
            if pp.resolve() == input_roms_dir:
                _skip_input_roms = True
                break

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
    if _skip_input_roms and (project_root / "_input_roms").exists():
        preserved.append(str(project_root / "_input_roms"))
        print(f"[preflight_cleanup] preserved (active ROM): {project_root / '_input_roms'}")
    else:
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
    for chunk in list(project_root.glob("super.img.*")) + list(
        (output_dir / "work").glob("super.img.*")
        if (output_dir / "work").exists()
        else []
    ):
        _rm(chunk)

    # ── Preserved directories ─────────────────────────────────────────────────
    for keep in [output_dir / "reports", output_dir / "logs"]:
        if keep.exists():
            preserved.append(str(keep))

    duration = round(time.monotonic() - t0, 2)

    active_rom_path = str(preserve_paths[0]) if preserve_paths else None
    cleanup_phase = "post_download" if _skip_input_roms else "pre_download"

    result = {
        "status": "APPLIED",
        "removed": removed,
        "preserved": preserved,
        "errors": errors,
        "duration_seconds": duration,
        "active_rom_path": active_rom_path,
        "cleanup_phase": cleanup_phase,
        "input_roms_preserved": _skip_input_roms,
    }

    _write_preflight_report(output_dir / "reports", result)
    return result


def _write_preflight_report(reports_dir: Path, result: dict) -> None:
    try:
        reports_dir.mkdir(parents=True, exist_ok=True)
        removed = result.get("removed") or []
        preserved = result.get("preserved") or []
        errors = result.get("errors") or []
        active_rom = result.get("active_rom_path") or "(none)"
        phase = result.get("cleanup_phase") or "unknown"
        input_roms_preserved = result.get("input_roms_preserved", False)
        lines = [
            "=" * 60,
            "  DeadZone Factory — Preflight Cleanup Report",
            "=" * 60,
            f"  Status               : {result.get('status')}",
            f"  Cleanup phase        : {phase}",
            f"  Duration             : {result.get('duration_seconds')}s",
            f"  Removed paths        : {len(removed)}",
            f"  Preserved paths      : {len(preserved)}",
            f"  Errors               : {len(errors)}",
            f"  Active ROM path      : {active_rom}",
            f"  _input_roms deleted  : {not input_roms_preserved}",
            f"  _input_roms preserved: {input_roms_preserved}",
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
