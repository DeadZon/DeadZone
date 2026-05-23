"""
DeadZone Legend unified patch runner.

This is the ONLY active code path that applies Legend patches.

Public API
----------
    run_legend(root, output_dir=None, report_path=None, context=None) -> dict

Pipeline order
--------------
  1. validate single Legend home
  2. patch fstab files
  3. patch props (if rules present)
  4. apply APK mods (Provision, SystemUI, PowerKeeper)
  5. apply JAR mods (MTCR: framework, services, miui-framework, miui-services)
  6. MTCR framework patches (included in step 5 via jar_patcher)
  7. inject SystemUI resources (handled inside APK runner, step 4)
  8. patch permissions (if rules present)
  9. write full report

All steps write to:
    output/reports/deadzone_patch_report.txt

Flavor guard: only runs for "legend" and "deadzone_legend".
"""
from __future__ import annotations

import sys
import time
from pathlib import Path
from typing import Any, Optional

_LEGEND_FLAVORS = frozenset({"legend", "deadzone_legend"})
_REPO_ROOT = Path(__file__).resolve().parents[3]


def run_legend(
    root: Path | str,
    output_dir: Optional[Path | str] = None,
    report_path: Optional[Path | str] = None,
    context: Optional[dict[str, Any]] = None,
) -> dict:
    """
    Apply (or dry-run) all DeadZone Legend patches against an unpacked ROM.

    Parameters
    ----------
    root        : Path  Root of the unpacked ROM project.
    output_dir  : Path  Output directory (default: <repo_root>/output).
    report_path : Path  Ignored — report is always written to the canonical
                        output/reports/deadzone_patch_report.txt.
    context     : dict  Optional keys:
                          flavor        (str)  default "legend"
                          execute       (bool) default False
                          android_major (int)  optional

    Returns
    -------
    dict  Unified report with final_status, per-step results, warnings, errors.
    """
    ctx = context or {}
    flavor = str(ctx.get("flavor", "legend"))
    execute = bool(ctx.get("execute", False))
    android_major: Optional[int] = ctx.get("android_major")

    root = Path(root).resolve()
    _output_dir = Path(output_dir).resolve() if output_dir else _REPO_ROOT / "output"

    # ── Flavor guard ──────────────────────────────────────────────────────────
    norm_flavor = flavor.strip().lower().replace("-", "_")
    if norm_flavor not in _LEGEND_FLAVORS:
        return {
            "stage": "legend_runner",
            "final_status": "SKIPPED_NON_LEGEND",
            "flavor": flavor,
            "warnings": [f"Flavor '{flavor}' is not a Legend flavor — skipped"],
            "errors": [],
        }

    from factory.patch.legend.reports.writer import (
        append_section,
        start_report,
        write_final_summary,
    )

    start_report(flavor, execute, root)
    mode = "EXECUTE" if execute else "DRY-RUN"
    print(f"[legend_runner] === DeadZone Legend Runner ({mode}) ===")
    print(f"[legend_runner] Project : {root}")
    print(f"[legend_runner] Flavor  : {flavor}")

    report: dict = {
        "stage": "legend_runner",
        "flavor": flavor,
        "dry_run": not execute,
        "android_major": android_major,
        "project_dir": str(root),
        "output_dir": str(_output_dir),
        "steps": {},
        "warnings": [],
        "errors": [],
        "final_status": "DRY_RUN" if not execute else "PENDING",
    }

    any_failed = False

    # ── Step 1: Validate Legend home ─────────────────────────────────────────
    print("[legend_runner] Step 1: validate Legend home")
    step_lines: list[str] = []
    try:
        from factory.patch.legend.actions.validate_legend_home import validate
        val_result = validate(quiet=True)
        step_lines.append(f"passed: {val_result['passed']}")
        if not val_result["passed"]:
            for v in val_result["violations"]:
                msg = f"stray reference: {v['file']}:{v['line']} — {v['snippet']}"
                step_lines.append(f"  VIOLATION: {msg}")
                report["warnings"].append(msg)
        report["steps"]["validate_home"] = val_result
    except Exception as exc:
        step_lines.append(f"ERROR: {exc}")
        report["warnings"].append(f"validate_home error: {exc}")
        report["steps"]["validate_home"] = {"passed": False, "error": str(exc)}
    append_section("1. Validate Legend Home", step_lines)

    # ── Step 2: Fstab patch ───────────────────────────────────────────────────
    print("[legend_runner] Step 2: fstab patch")
    step_lines = []
    try:
        from factory.patch.legend.patchers.fstab_patcher import patch_fstab
        fstab_result = patch_fstab(root, execute=execute, report_lines=step_lines)
        report["steps"]["fstab"] = fstab_result
        if fstab_result["errors"]:
            report["warnings"].extend(fstab_result["errors"])
    except Exception as exc:
        step_lines.append(f"ERROR: {exc}")
        report["errors"].append(f"fstab_patcher: {exc}")
        report["steps"]["fstab"] = {"errors": [str(exc)]}
        if execute:
            any_failed = True
    append_section("2. Fstab Patch", step_lines)

    # ── Step 3: Props patch ───────────────────────────────────────────────────
    print("[legend_runner] Step 3: props patch")
    step_lines = []
    try:
        from factory.patch.legend.patchers.props_patcher import patch_props
        props_result = patch_props(root, execute=execute, report_lines=step_lines)
        report["steps"]["props"] = props_result
    except Exception as exc:
        step_lines.append(f"ERROR: {exc}")
        report["warnings"].append(f"props_patcher: {exc}")
        report["steps"]["props"] = {"errors": [str(exc)]}
    append_section("3. Props Patch", step_lines)

    # ── Step 3b: Debloat (OS3 only — guard inside executor) ──────────────────
    print("[legend_runner] Step 3b: debloat patch")
    step_lines = []
    try:
        from factory.patch.legend.patchers.debloat_patcher import patch_debloat
        os_family = str(ctx.get("os_family", "OS3"))
        debloat_result = patch_debloat(
            root, flavor,
            os_family=os_family,
            execute=execute,
            report_lines=step_lines,
        )
        report["steps"]["debloat"] = debloat_result
        if debloat_result.get("errors"):
            report["warnings"].extend(debloat_result["errors"])
    except Exception as exc:
        step_lines.append(f"ERROR: {exc}")
        report["warnings"].append(f"debloat_patcher: {exc}")
        report["steps"]["debloat"] = {"errors": [str(exc)]}
    append_section("3b. Debloat Patch", step_lines)

    # ── Step 4: APK mods ─────────────────────────────────────────────────────
    print("[legend_runner] Step 4: APK mods (Provision, SystemUI, PowerKeeper)")
    step_lines = []
    try:
        from factory.patch.legend.patchers.apk_patcher import patch_apks
        apk_result = patch_apks(root, flavor, execute=execute, report_lines=step_lines)
        report["steps"]["apk_mods"] = apk_result
        if apk_result.get("errors"):
            report["warnings"].extend(apk_result["errors"])
    except Exception as exc:
        step_lines.append(f"ERROR: {exc}")
        report["errors"].append(f"apk_patcher: {exc}")
        report["steps"]["apk_mods"] = {"errors": [str(exc)]}
        if execute:
            any_failed = True
    append_section("4. APK Mods", step_lines)

    # ── Step 5: JAR mods (MTCR) ──────────────────────────────────────────────
    print("[legend_runner] Step 5: JAR mods via MTCR runner")
    step_lines = []
    try:
        from factory.patch.legend.patchers.jar_patcher import patch_jars
        jar_result = patch_jars(
            root, flavor,
            execute=execute,
            android_major=android_major,
            report_lines=step_lines,
        )
        report["steps"]["jar_mods"] = jar_result
        if jar_result.get("errors"):
            report["errors"].extend(jar_result["errors"])
            if execute:
                any_failed = True
    except Exception as exc:
        step_lines.append(f"ERROR: {exc}")
        report["errors"].append(f"jar_patcher: {exc}")
        report["steps"]["jar_mods"] = {"errors": [str(exc)]}
        if execute:
            any_failed = True
    append_section("5. JAR Mods (MTCR)", step_lines)

    # ── Step 6: SystemUI assets present? ─────────────────────────────────────
    print("[legend_runner] Step 6: SystemUI assets check")
    step_lines = []
    try:
        from factory.patch.legend.patchers.systemui_resources import validate_assets_present
        assets_ok = validate_assets_present(step_lines)
        report["steps"]["systemui_assets"] = {"present": assets_ok}
    except Exception as exc:
        step_lines.append(f"ERROR: {exc}")
        report["warnings"].append(f"systemui_resources: {exc}")
        report["steps"]["systemui_assets"] = {"errors": [str(exc)]}
    append_section("6. SystemUI Assets", step_lines)

    # ── Step 7: Permissions patch ─────────────────────────────────────────────
    print("[legend_runner] Step 7: permissions patch")
    step_lines = []
    try:
        from factory.patch.legend.patchers.permissions_patcher import patch_permissions
        perm_result = patch_permissions(root, execute=execute, report_lines=step_lines)
        report["steps"]["permissions"] = perm_result
    except Exception as exc:
        step_lines.append(f"ERROR: {exc}")
        report["warnings"].append(f"permissions_patcher: {exc}")
        report["steps"]["permissions"] = {"errors": [str(exc)]}
    append_section("7. Permissions Patch", step_lines)

    # ── Final status ──────────────────────────────────────────────────────────
    if execute:
        report["final_status"] = "FAILED" if any_failed else "APPLIED"
    else:
        report["final_status"] = "DRY_RUN"

    print(f"[legend_runner] final_status={report['final_status']}")
    write_final_summary(report)
    return report


# ── CLI ───────────────────────────────────────────────────────────────────────

def _main(argv: list[str] | None = None) -> int:
    import argparse
    p = argparse.ArgumentParser(description="DeadZone Legend unified patch runner")
    p.add_argument("--project", required=True, type=Path)
    p.add_argument("--flavor", default="legend")
    p.add_argument("--android-major", dest="android_major", type=int, default=None)
    p.add_argument("--output-dir", dest="output_dir", type=Path, default=None)
    p.add_argument("--execute", action="store_true")
    args = p.parse_args(argv)

    project = Path(args.project).resolve()
    if not project.is_dir():
        print(f"[legend_runner] ERROR: not a directory: {project}", file=sys.stderr)
        return 2

    report = run_legend(
        root=project,
        output_dir=args.output_dir,
        context={
            "flavor": args.flavor,
            "android_major": args.android_major,
            "execute": args.execute,
        },
    )
    return 1 if report.get("errors") else 0


if __name__ == "__main__":
    sys.exit(_main())
