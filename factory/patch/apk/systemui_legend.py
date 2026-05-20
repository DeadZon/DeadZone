"""
MiuiSystemUI APK patch stage -- Legend ROM flavor only.  (Thin wrapper)

All patch logic has been converted to clean Python rules.
No MTCR files are read at runtime.
No Legend/ or third_party/mezo_core/MEZO_LEGEND/ directories are accessed.

Real implementation lives in:
  factory/patch/legend/systemui/runner.py

Rule modules:
  factory/patch/legend/systemui/smali/          — 114 modified class patches
  factory/patch/legend/systemui/smali_added/    — 313 added class patches
  factory/patch/legend/systemui/resources/      — layout + arsc + values rules
  factory/patch/legend/systemui/dex/            — managed dex payload declarations
  factory/assets/legend/systemui/               — managed add-resource XMLs + dex payloads

Operations (in order):
  1. Find MiuiSystemUI.apk in the ROM project tree.
  2. Decompile with APKEditor.
  3. Merge managed add/ resource XMLs.
  4. Apply layout XML patches (text-diff hunks — 20 layouts).
  5. Apply arsc resource patches (XML merge — 20 modified + 140 added groups).
  6. Apply smali method patches (smart Tier 1-4 — 114 modified classes).
  7. Place added smali classes into smali_classesN roots (313 added classes).
  8. Apply DEX payloads via baksmali (non-blocking if baksmali missing).
  9. Rebuild MiuiSystemUI.apk.
  10. Restore to exact original path as MiuiSystemUI.apk.
      No MiuiSystemUI_new.apk, no backup files, no renamed copies.

Flavor guard:
  Only runs for: legend, deadzone_legend (case-insensitive).

CLI:
  # dry-run:
  python -m factory.patch.apk.systemui_legend \\
      --project "path/to/unpacked_project" \\
      --flavor legend

  # execute:
  python -m factory.patch.apk.systemui_legend \\
      --project "path/to/unpacked_project" \\
      --flavor legend \\
      --execute
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from factory.patch.legend.systemui.runner import apply_systemui_patch, _write_reports


# ---------------------------------------------------------------------------
# Public entry point (preserved signature for pipeline compatibility)
# ---------------------------------------------------------------------------

def apply_legend_systemui_patch(
    project_dir: Path,
    flavor: str,
    execute: bool = False,
    work_dir: Path | None = None,
    reference_dir: Path | None = None,  # ignored — no runtime MTCR reads
) -> dict:
    """
    Apply (or dry-run) the MiuiSystemUI APK patch for Legend ROM flavor.

    Parameters
    ----------
    project_dir   : Path  Root of the unpacked ROM project directory.
    flavor        : str   ROM flavor ("legend" | "deadzone_legend" | other).
    execute       : bool  True → apply.  False (default) → dry-run.
    work_dir      : Path  Optional work directory override.
    reference_dir : Path  Ignored (no MTCR or Legend/ reads at runtime).

    Returns
    -------
    dict  Report with final_status and all stage detail keys.
    """
    return apply_systemui_patch(
        project_dir=project_dir,
        flavor=flavor,
        execute=execute,
        work_dir=work_dir,
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="MiuiSystemUI APK patch stage -- Legend only (DeadZone factory)",
    )
    p.add_argument("--project", required=True,
                   help="Path to unpacked ROM project directory")
    p.add_argument("--flavor",  required=True,
                   help="ROM flavor: legend | deadzone_legend | <other>")
    p.add_argument("--work-dir", dest="work_dir", default=None,
                   help="Work directory (default: output/work/systemui_legend_apk_work)")
    p.add_argument("--reference-dir", dest="reference_dir", default=None,
                   help="Ignored (no MTCR reads at runtime)")
    p.add_argument("--execute", action="store_true",
                   help="Apply the patch (default is dry-run only)")
    return p


def _main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args   = parser.parse_args(argv)

    project_dir = Path(args.project).resolve()
    if not project_dir.is_dir():
        print(
            f"[systemui_legend] ERROR: project directory not found: {project_dir}",
            file=sys.stderr,
        )
        return 2

    work_dir = Path(args.work_dir).resolve() if args.work_dir else None
    mode     = "EXECUTE" if args.execute else "DRY-RUN"

    print(
        f"[systemui_legend] mode={mode}  flavor={args.flavor}  "
        f"project={project_dir}"
    )

    report = apply_legend_systemui_patch(
        project_dir=project_dir,
        flavor=args.flavor,
        execute=args.execute,
        work_dir=work_dir,
    )

    print(f"[systemui_legend] final_status={report['final_status']}")
    for w in report.get("warnings", []):
        print(f"[systemui_legend] WARNING: {w}")
    for e in report.get("errors", []):
        print(f"[systemui_legend] ERROR: {e}", file=sys.stderr)

    return 1 if report.get("errors") else 0


if __name__ == "__main__":
    sys.exit(_main())
