"""
MiuiSystemUI APK patch stage -- Legend ROM flavor only.

Applies MiuiSystemUI APK modifications using the reference pack at:
  third_party/mezo_core/MEZO_LEGEND/MiuiSystemUI/   (canonical)
  Legend/MiuiSystemUI/                               (fallback)

Operations applied:
  1. Copy MiuiSystemUI.apk to work directory.
  2. Decompile with APKEditor.jar.
  3. Merge add/classes*.dex payload (via baksmali -> smali -> new smali_classesN root).
  4. Merge add/com.android.systemui/ resource XMLs into res/values*/.
  5. Apply compare/dex.mtcr: exact smali method/field changes only.
  6. Apply compare/xml.mtcr: exact layout XML block/attribute changes only.
  7. Apply compare/arsc.mtcr: safe resource value changes only.
  8. Rebuild MiuiSystemUI.apk.
  9. Verify rebuilt APK (exists, size > 0).
  10. Replace original MiuiSystemUI.apk (no backup).

Flavor guard:
  Only runs for: legend, deadzone_legend, DeadZone_Legend (case-insensitive).
  All other flavors: SKIPPED_NON_LEGEND, nothing modified.

CLI:
  # dry-run:
  python -m factory.patch.apk.systemui_legend ^
      --project "path/to/unpacked_project" ^
      --flavor legend

  # execute:
  python -m factory.patch.apk.systemui_legend ^
      --project "path/to/unpacked_project" ^
      --flavor legend ^
      --execute

  # custom reference dir:
  python -m factory.patch.apk.systemui_legend ^
      --project "path/to/unpacked_project" ^
      --flavor legend ^
      --execute ^
      --reference-dir "path/to/MiuiSystemUI"
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

from factory.patch.apk.apkeditor_tools import resolve_apkeditor_jar
from factory.patch.apk.apk_workspace import (
    copy_apk_to_work,
    decompile_apk,
    find_apk,
    prepare_apk_work_dir,
    rebuild_apk,
    restore_rebuilt_apk_no_backup,
)
from factory.patch.apk.mtcr_apk_reference import inspect_reference_pack
from factory.patch.apk.dex_payload_apk import apply_add_dex
from factory.patch.apk.resource_merge import apply_add_resources, apply_xml_mtcr, apply_arsc_mtcr
from factory.patch.apk.exact_smali_patch import apply_dex_mtcr

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_REPO_ROOT = Path(__file__).resolve().parents[3]
_OUTPUT_ROOT = _REPO_ROOT / "output"
_REPORTS_DIR = _OUTPUT_ROOT / "reports"
_WORK_DIR_DEFAULT = _OUTPUT_ROOT / "work" / "systemui_legend_apk_work"

SYSTEMUI_APK_NAME = "MiuiSystemUI.apk"
SYSTEMUI_APK_SRC_DIR_NAME = "MiuiSystemUI_apk_src"

# Legend flavor identifiers matched case-insensitively
_LEGEND_FLAVORS: frozenset[str] = frozenset({"legend", "deadzone_legend"})

# Reference pack search locations (canonical then fallback)
_CANONICAL_REF_DIR = _REPO_ROOT / "third_party" / "mezo_core" / "MEZO_LEGEND" / "MiuiSystemUI"
_FALLBACK_REF_DIR = _REPO_ROOT / "Legend" / "MiuiSystemUI"

_REPORT_JSON = "10_legend_systemui_apk_report.json"
_REPORT_TXT = "10_legend_systemui_apk_report.txt"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _is_legend_flavor(flavor: str) -> bool:
    return flavor.strip().lower() in _LEGEND_FLAVORS


def _resolve_reference_dir(user_ref: Path | None) -> Path | None:
    """Return the first existing MiuiSystemUI reference directory."""
    if user_ref is not None:
        return user_ref if user_ref.is_dir() else None
    if _CANONICAL_REF_DIR.is_dir():
        return _CANONICAL_REF_DIR
    if _FALLBACK_REF_DIR.is_dir():
        return _FALLBACK_REF_DIR
    return None


def _skipped_stage(report: dict, *keys: str) -> None:
    for k in keys:
        report[k] = "SKIPPED"


# ---------------------------------------------------------------------------
# Report formatting
# ---------------------------------------------------------------------------

def _format_text_report(report: dict) -> str:
    mode = "DRY RUN" if report.get("dry_run") else "EXECUTE"
    lines: list[str] = [
        f"DeadZone MiuiSystemUI APK Patch Report  [{mode}]",
        "=" * 64,
        f"Final status     : {report.get('final_status', '?')}",
        f"Stage            : {report.get('stage', '?')}",
        f"Flavor           : {report.get('flavor', '?')}",
        f"Dry run          : {report.get('dry_run', True)}",
        f"Backup policy    : {report.get('backup_policy', 'disabled')}",
        f"Project dir      : {report.get('project_dir', '?')}",
        f"Work dir         : {report.get('work_dir', '?')}",
        f"Reference dir    : {report.get('reference_dir', '?')}",
        "",
        "Tool:",
        f"  APKEditor jar  : {report.get('apkeditor_jar', '?')}",
        f"  jar exists     : {report.get('apkeditor_jar_exists', '?')}",
        "",
        "APK:",
        f"  MiuiSystemUI   : {report.get('miui_systemui_apk', '?')}",
        f"  APK found      : {report.get('miui_systemui_apk_found', '?')}",
        "",
        "Stage results:",
        f"  Decompile      : {report.get('decompile_status', 'N/A')}",
        f"  Add dex        : {report.get('add_dex_status', 'N/A')}",
        f"  Add resources  : {report.get('add_resource_status', 'N/A')}",
        f"  dex.mtcr       : {report.get('dex_mtcr_status', 'N/A')}",
        f"  xml.mtcr       : {report.get('xml_mtcr_status', 'N/A')}",
        f"  arsc.mtcr      : {report.get('arsc_mtcr_status', 'N/A')}",
        f"  Rebuild        : {report.get('rebuild_status', 'N/A')}",
        f"  Replace        : {report.get('replace_status', 'N/A')}",
        "",
    ]

    ref_summary = report.get("reference_summary", {})
    if ref_summary.get("ref_dir_exists"):
        lines.append("Reference pack summary:")
        for dex_info in ref_summary.get("add_dex", []):
            tag = "OK" if dex_info.get("exists") else "MISSING"
            size = dex_info.get("size", 0)
            lines.append(f"  add/{dex_info['name']}: {tag}  ({size} bytes)")
        lines.append(
            f"  add/ resource XMLs: {ref_summary.get('add_resource_files', 0)} total"
        )
        for t, c in sorted(ref_summary.get("add_resource_types", {}).items()):
            lines.append(f"    {t}: {c} files")
        for key in ("dex_mtcr", "xml_mtcr", "arsc_mtcr"):
            m = ref_summary.get(key) or {}
            if m.get("exists"):
                lines.append(
                    f"  compare/{key.replace('_', '.')}: "
                    f"a={m.get('a_count', 0)}  b={m.get('b_count', 0)}  "
                    f"modified={m.get('modified_count', 0)}  "
                    f"added={m.get('added_count', 0)}"
                )
            else:
                lines.append(f"  compare/{key.replace('_', '.')}: MISSING")
        lines.append("")

    warnings = report.get("warnings", [])
    lines.append("Warnings:")
    lines.extend(f"  ! {w}" for w in warnings) if warnings else lines.append("  (none)")

    lines.append("")
    errors = report.get("errors", [])
    lines.append("Errors:")
    lines.extend(f"  X {e}" for e in errors) if errors else lines.append("  (none)")

    lines.append("")
    return "\n".join(lines)


def _write_reports(report: dict) -> None:
    _REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    json_path = _REPORTS_DIR / _REPORT_JSON
    txt_path = _REPORTS_DIR / _REPORT_TXT
    json_path.write_text(
        json.dumps(report, indent=2, ensure_ascii=True, default=str),
        encoding="utf-8",
    )
    txt_path.write_text(_format_text_report(report), encoding="utf-8")
    print(f"[systemui_legend] JSON: {json_path}")
    print(f"[systemui_legend] TXT : {txt_path}")


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def apply_legend_systemui_patch(
    project_dir: Path,
    flavor: str,
    execute: bool = False,
    work_dir: Path | None = None,
    reference_dir: Path | None = None,
) -> dict:
    """
    Apply (or dry-run) the MiuiSystemUI APK patch for Legend ROM flavor.

    Parameters
    ----------
    project_dir : Path
        Root of the unpacked ROM project directory.
    flavor : str
        ROM flavor identifier (e.g. "legend", "deadzone_legend", "base").
    execute : bool
        True -> apply all changes.  False (default) -> dry-run, nothing modified.
    work_dir : Path | None
        Work directory.  Defaults to output/work/systemui_legend_apk_work.
    reference_dir : Path | None
        Path to MiuiSystemUI reference pack directory.  Auto-resolved if None.

    Returns
    -------
    dict
        Report with final_status and all stage detail keys.
    """
    effective_work_dir = work_dir if work_dir is not None else _WORK_DIR_DEFAULT

    apkeditor_jar = resolve_apkeditor_jar()
    ref_dir = _resolve_reference_dir(reference_dir)
    systemui_apk = find_apk(project_dir, SYSTEMUI_APK_NAME)

    apkeditor_str = str(apkeditor_jar) if apkeditor_jar else "(not found)"
    apkeditor_exists = apkeditor_jar is not None
    ref_str = str(ref_dir) if ref_dir else "(not found)"
    ref_found = ref_dir is not None
    apk_str = str(systemui_apk) if systemui_apk else "(not found)"
    apk_found = systemui_apk is not None

    warnings: list[str] = []
    errors: list[str] = []

    ref_summary: dict = inspect_reference_pack(ref_dir) if ref_found else {}

    report: dict = {
        "stage": "legend_systemui_apk",
        "flavor": flavor,
        "dry_run": not execute,
        "project_dir": str(project_dir),
        "work_dir": str(effective_work_dir),
        "reference_dir": ref_str,
        "apkeditor_jar": apkeditor_str,
        "apkeditor_jar_exists": apkeditor_exists,
        "miui_systemui_apk": apk_str,
        "miui_systemui_apk_found": apk_found,
        "backup_policy": "disabled",
        "decompile_status": "N/A",
        "add_dex_status": "N/A",
        "add_resource_status": "N/A",
        "dex_mtcr_status": "N/A",
        "xml_mtcr_status": "N/A",
        "arsc_mtcr_status": "N/A",
        "rebuild_status": "N/A",
        "replace_status": "N/A",
        "reference_summary": ref_summary,
        "add_dex": {},
        "add_resources": {},
        "dex_mtcr": {},
        "xml_mtcr": {},
        "arsc_mtcr": {},
        "warnings": warnings,
        "errors": errors,
        "final_status": "DRY_RUN",
    }

    # ------------------------------------------------------------------
    # Legend guard -- always checked first
    # ------------------------------------------------------------------
    if not _is_legend_flavor(flavor):
        report["final_status"] = "SKIPPED_NON_LEGEND"
        print(
            f"[systemui_legend] Flavor '{flavor}' is not Legend. "
            f"final_status=SKIPPED_NON_LEGEND"
        )
        return report

    # ------------------------------------------------------------------
    # DRY-RUN
    # ------------------------------------------------------------------
    if not execute:
        if not apkeditor_exists:
            warnings.append("APKEditor.jar not found in third_party/mezo_core")
        if not apk_found:
            warnings.append("MiuiSystemUI.apk not found in any partition location")
        if not ref_found:
            warnings.append("MiuiSystemUI reference directory not found")

        decompiled_dir = effective_work_dir / SYSTEMUI_APK_SRC_DIR_NAME
        planned: list[str] = [
            f"[1] Flavor check: '{flavor}' -> Legend OK",
            f"[2] MiuiSystemUI.apk: {apk_str}",
            f"[3] APKEditor.jar: {apkeditor_str}",
            f"[4] Reference dir: {ref_str}",
        ]

        if ref_found:
            planned.append("[5] Reference contents:")
            for d in ref_summary.get("add_dex", []):
                tag = "FOUND" if d.get("exists") else "MISSING"
                planned.append(f"    add/{d['name']}: {tag}")
            planned.append(
                f"    add/ resource XMLs: {ref_summary.get('add_resource_files', 0)}"
            )
            for key in ("dex_mtcr", "xml_mtcr", "arsc_mtcr"):
                m = ref_summary.get(key) or {}
                tag = "FOUND" if m.get("exists") else "MISSING"
                planned.append(f"    compare/{key.replace('_', '.')}: {tag}")
        else:
            planned.append("[5] Reference contents: MISSING (cannot inspect)")

        planned += [
            f"[6] Would copy {SYSTEMUI_APK_NAME} -> {effective_work_dir / SYSTEMUI_APK_NAME}",
            f"    Decompile -> {decompiled_dir.name}/",
            f"    Merge add/classes2.dex, classes3.dex, classes4.dex (baksmali -> smali -> smali_classesN)",
            f"    Merge add/com.android.systemui/ resource XMLs -> res/values*/",
            f"    Apply dex.mtcr: exact smali method/field changes (115 modified classes, 313 added)",
            f"    Apply xml.mtcr: exact layout XML block changes (20 layout files)",
            f"    Apply arsc.mtcr: safe resource value changes (20 modified groups, 140 added)",
            f"    Rebuild {SYSTEMUI_APK_NAME}",
            f"    Replace {apk_str} with rebuilt APK (no backup)",
        ]

        report["planned_steps"] = planned

        if not apk_found:
            report["final_status"] = "SKIPPED_MISSING_APK"
        elif not ref_found:
            report["final_status"] = "SKIPPED_MISSING_REFERENCE"
        elif not apkeditor_exists:
            report["final_status"] = "SKIPPED_MISSING_TOOL"
        else:
            report["final_status"] = "DRY_RUN"

        return report

    # ------------------------------------------------------------------
    # EXECUTE -- guard preconditions
    # ------------------------------------------------------------------
    if not apk_found:
        errors.append("MiuiSystemUI.apk not found in project; cannot patch")
        report["final_status"] = "SKIPPED_MISSING_APK"
        return report

    if not ref_found:
        errors.append("MiuiSystemUI reference directory not found; cannot patch")
        report["final_status"] = "SKIPPED_MISSING_REFERENCE"
        return report

    if not apkeditor_exists:
        errors.append("APKEditor.jar not found; cannot decompile/rebuild APK")
        report["final_status"] = "SKIPPED_MISSING_TOOL"
        return report

    # ------------------------------------------------------------------
    # Step 1: Copy APK to work directory
    # ------------------------------------------------------------------
    print(f"[systemui_legend] Copying {SYSTEMUI_APK_NAME} to work dir ...")
    try:
        prepare_apk_work_dir(effective_work_dir, SYSTEMUI_APK_NAME)
        work_apk = copy_apk_to_work(systemui_apk, effective_work_dir)
    except Exception as exc:
        errors.append(f"Copy failed: {exc}")
        _skipped_stage(
            report,
            "decompile_status", "add_dex_status", "add_resource_status",
            "dex_mtcr_status", "xml_mtcr_status", "arsc_mtcr_status",
            "rebuild_status", "replace_status",
        )
        report["final_status"] = "FAILED"
        return report

    # ------------------------------------------------------------------
    # Step 2: Decompile
    # ------------------------------------------------------------------
    decompiled_dir = effective_work_dir / SYSTEMUI_APK_SRC_DIR_NAME
    print(f"[systemui_legend] Decompiling {SYSTEMUI_APK_NAME} ...")
    decompile_ok = decompile_apk(apkeditor_jar, work_apk, decompiled_dir)
    report["decompile_status"] = "OK" if decompile_ok else "FAILED"

    if not decompile_ok:
        errors.append("Decompile failed; original APK not touched")
        _skipped_stage(
            report,
            "add_dex_status", "add_resource_status",
            "dex_mtcr_status", "xml_mtcr_status", "arsc_mtcr_status",
            "rebuild_status", "replace_status",
        )
        report["final_status"] = "FAILED"
        return report

    # ------------------------------------------------------------------
    # Step 3: Merge add/classes*.dex payload
    # ------------------------------------------------------------------
    print(f"[systemui_legend] Applying add/classes*.dex payload (via baksmali) ...")
    dex_work_dir = effective_work_dir / "dex_smali_work"
    add_dex_result = apply_add_dex(ref_dir, decompiled_dir, dex_work_dir)
    report["add_dex"] = add_dex_result
    report["add_dex_status"] = add_dex_result.get("status", "UNKNOWN")
    # Non-fatal: continue even if baksmali is missing
    for e in add_dex_result.get("errors", []):
        warnings.append(f"add_dex: {e}")

    # ------------------------------------------------------------------
    # Step 4: Merge add/ resource XMLs
    # ------------------------------------------------------------------
    print(f"[systemui_legend] Merging add/ resource XMLs ...")
    add_res_result = apply_add_resources(ref_dir, decompiled_dir)
    report["add_resources"] = add_res_result
    report["add_resource_status"] = add_res_result.get("status", "UNKNOWN")
    for e in add_res_result.get("errors", []):
        warnings.append(f"add_resources: {e}")

    # ------------------------------------------------------------------
    # Step 5: Apply dex.mtcr
    # ------------------------------------------------------------------
    dex_mtcr_path = ref_dir / "compare" / "dex.mtcr"
    if dex_mtcr_path.is_file():
        print(f"[systemui_legend] Applying dex.mtcr smali changes ...")
        dex_mtcr_result = apply_dex_mtcr(dex_mtcr_path, decompiled_dir)
        report["dex_mtcr"] = dex_mtcr_result
        report["dex_mtcr_status"] = dex_mtcr_result.get("status", "UNKNOWN")
        for e in dex_mtcr_result.get("errors", []):
            warnings.append(f"dex_mtcr: {e}")
    else:
        report["dex_mtcr_status"] = "SKIPPED_NOT_FOUND"
        warnings.append("compare/dex.mtcr not found in reference pack")

    # ------------------------------------------------------------------
    # Step 6: Apply xml.mtcr
    # ------------------------------------------------------------------
    xml_mtcr_path = ref_dir / "compare" / "xml.mtcr"
    if xml_mtcr_path.is_file():
        print(f"[systemui_legend] Applying xml.mtcr layout changes ...")
        xml_mtcr_result = apply_xml_mtcr(xml_mtcr_path, decompiled_dir)
        report["xml_mtcr"] = xml_mtcr_result
        report["xml_mtcr_status"] = xml_mtcr_result.get("status", "UNKNOWN")
        for e in xml_mtcr_result.get("errors", []):
            warnings.append(f"xml_mtcr: {e}")
    else:
        report["xml_mtcr_status"] = "SKIPPED_NOT_FOUND"
        warnings.append("compare/xml.mtcr not found in reference pack")

    # ------------------------------------------------------------------
    # Step 7: Apply arsc.mtcr
    # ------------------------------------------------------------------
    arsc_mtcr_path = ref_dir / "compare" / "arsc.mtcr"
    if arsc_mtcr_path.is_file():
        print(f"[systemui_legend] Applying arsc.mtcr resource changes ...")
        arsc_mtcr_result = apply_arsc_mtcr(arsc_mtcr_path, decompiled_dir)
        report["arsc_mtcr"] = arsc_mtcr_result
        report["arsc_mtcr_status"] = arsc_mtcr_result.get("status", "UNKNOWN")
        for e in arsc_mtcr_result.get("errors", []):
            warnings.append(f"arsc_mtcr: {e}")
    else:
        report["arsc_mtcr_status"] = "SKIPPED_NOT_FOUND"
        warnings.append("compare/arsc.mtcr not found in reference pack")

    # ------------------------------------------------------------------
    # Step 8: Rebuild APK
    # ------------------------------------------------------------------
    print(f"[systemui_legend] Rebuilding {SYSTEMUI_APK_NAME} ...")
    rebuild_ok = rebuild_apk(apkeditor_jar, decompiled_dir)
    report["rebuild_status"] = "OK" if rebuild_ok else "FAILED"

    if not rebuild_ok:
        errors.append("Rebuild failed; original APK not touched")
        report["replace_status"] = "SKIPPED"
        report["final_status"] = "FAILED"
        return report

    # Clean up temporary decompile directory
    try:
        shutil.rmtree(decompiled_dir, ignore_errors=True)
        print(f"[systemui_legend] Removed temp dir: {decompiled_dir.name}")
    except Exception:
        pass

    # ------------------------------------------------------------------
    # Step 9: Verify rebuilt APK
    # ------------------------------------------------------------------
    rebuilt_apk_path = effective_work_dir / SYSTEMUI_APK_NAME
    if not rebuilt_apk_path.is_file() or rebuilt_apk_path.stat().st_size == 0:
        errors.append("Rebuilt APK is missing or zero bytes; original APK not touched")
        report["replace_status"] = "SKIPPED"
        report["final_status"] = "FAILED"
        return report

    # ------------------------------------------------------------------
    # Step 10: Replace original APK (no backup)
    # ------------------------------------------------------------------
    print(f"[systemui_legend] Replacing original {SYSTEMUI_APK_NAME} (no backup) ...")
    replace_result = restore_rebuilt_apk_no_backup(rebuilt_apk_path, systemui_apk)
    replace_ok = replace_result["success"]
    report["replace_status"] = "OK" if replace_ok else "FAILED"

    if not replace_ok:
        errors.append(f"Replace failed: {replace_result.get('error', 'unknown')}")
        report["final_status"] = "FAILED"
        return report

    report["final_status"] = "APPLIED"
    return report


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="MiuiSystemUI APK patch stage -- Legend only (DeadZone factory)",
    )
    p.add_argument(
        "--project", required=True,
        help="Path to unpacked ROM project directory",
    )
    p.add_argument(
        "--flavor", required=True,
        help="ROM flavor: legend | deadzone_legend | DeadZone_Legend | <other>",
    )
    p.add_argument(
        "--work-dir", dest="work_dir", default=None,
        help="Work directory (default: output/work/systemui_legend_apk_work)",
    )
    p.add_argument(
        "--reference-dir", dest="reference_dir", default=None,
        help="Path to MiuiSystemUI reference pack directory",
    )
    p.add_argument(
        "--execute", action="store_true",
        help="Apply the patch (default is dry-run only)",
    )
    return p


def _main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    project_dir = Path(args.project).resolve()
    if not project_dir.is_dir():
        print(
            f"[systemui_legend] ERROR: project directory not found: {project_dir}",
            file=sys.stderr,
        )
        return 2

    work_dir = Path(args.work_dir).resolve() if args.work_dir else None
    ref_dir = Path(args.reference_dir).resolve() if args.reference_dir else None

    mode = "EXECUTE" if args.execute else "DRY-RUN"
    print(
        f"[systemui_legend] mode={mode}  flavor={args.flavor}  "
        f"project={project_dir}"
    )

    report = apply_legend_systemui_patch(
        project_dir=project_dir,
        flavor=args.flavor,
        execute=args.execute,
        work_dir=work_dir,
        reference_dir=ref_dir,
    )

    _write_reports(report)

    print(f"[systemui_legend] final_status={report['final_status']}")
    for w in report.get("warnings", []):
        print(f"[systemui_legend] WARNING: {w}")
    for e in report.get("errors", []):
        print(f"[systemui_legend] ERROR: {e}", file=sys.stderr)

    return 1 if report.get("errors") else 0


if __name__ == "__main__":
    sys.exit(_main())
