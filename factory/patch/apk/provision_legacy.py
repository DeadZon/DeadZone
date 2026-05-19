"""
Provision.apk legacy smali patch stage.

Carries exact behavior of MEZOBuildRom.py functions:
  patch_provision_utils(work_dir)              lines 946-1020
  (decompile/rebuild/restore delegated to apk_workspace helpers)

Allowed changes from source:
  - log() -> print()
  - ROOT_DIR references -> _LEGACY_ROOT / resolved paths
  - APKEditor.jar resolved via apkeditor_tools (not copied to work_dir)
  - find_apk used instead of system_ext-only rglob
  - dry-run guard, report wrapper

Not changed:
  - target class: com/android/provision/Utils.smali
  - target method: setGmsAppEnabledStateForCn
  - smali replacement logic (if-eq/if-eqz -> if-ne)
  - search behavior (invoke_pattern, move-result scan, if-ne guard)
  - patch conditions, return behavior

CLI:
  # dry-run:
  python -m factory.patch.apk.provision_legacy ^
      --project "path/to/unpacked_project" ^
      --flavor legend

  # execute:
  python -m factory.patch.apk.provision_legacy ^
      --project "path/to/unpacked_project" ^
      --flavor legend ^
      --execute
"""
from __future__ import annotations

import argparse
import json
import re
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

_REPO_ROOT   = Path(__file__).resolve().parents[3]
_OUTPUT_ROOT = _REPO_ROOT / "output"
_REPORTS_DIR = _OUTPUT_ROOT / "reports"
_WORK_DIR_DEFAULT = _OUTPUT_ROOT / "work" / "provision_apk_work"

# Exact constants from MEZOBuildRom.py lines 39-42
PROVISION_APK_NAME        = "Provision.apk"
PROVISION_APK_SRC_DIR_NAME = "Provision_apk_src"

_REPORT_JSON = "09_provision_apk_legacy_report.json"
_REPORT_TXT  = "09_provision_apk_legacy_report.txt"


# ---------------------------------------------------------------------------
# Exact copy of MEZOBuildRom.py:patch_provision_utils (lines 946-1020)
# Changes: log() -> print()  |  PROVISION_APK_SRC_DIR_NAME used from module constant
# Nothing else changed.
# ---------------------------------------------------------------------------
def patch_provision_utils(work_dir: Path) -> bool:
    apk_src_dir = work_dir / PROVISION_APK_SRC_DIR_NAME
    utils_file = (
        apk_src_dir
        / "smali"
        / "classes"
        / "com"
        / "android"
        / "provision"
        / "Utils.smali"
    )
    invoke_pattern = re.compile(
        r"invoke-virtual \{v0, v\d+\}, "
        r"Landroid/content/pm/PackageManager;->getApplicationEnabledSetting\(Ljava/lang/String;\)I"
    )

    if not utils_file.is_file():
        print(f"File to patch not found: {utils_file}")
        return False

    try:
        lines = utils_file.read_text(encoding="utf-8", errors="ignore").splitlines(keepends=True)
        method_start = -1
        method_end = -1

        for idx, line in enumerate(lines):
            if line.startswith(".method "):
                method_start = idx
                method_end = -1
                continue

            if method_start != -1 and ".end method" in line:
                method_end = idx
                block_text = "".join(lines[method_start:method_end + 1])
                if "setGmsAppEnabledStateForCn" not in block_text:
                    method_start = -1
                    continue

                for block_idx in range(method_start, method_end):
                    if not invoke_pattern.search(lines[block_idx]):
                        continue

                    move_result_idx = -1
                    for scan_idx in range(block_idx + 1, method_end):
                        if "move-result" in lines[scan_idx]:
                            move_result_idx = scan_idx
                            break

                    if move_result_idx == -1:
                        print("    move-result after getApplicationEnabledSetting not found in Utils.smali")
                        return False

                    for scan_idx in range(move_result_idx + 1, method_end):
                        if "if-ne" in lines[scan_idx]:
                            print("    Skipping Provision Utils patch: content already present.")
                            return True
                        if "if-eq" not in lines[scan_idx]:
                            continue

                        lines[scan_idx] = re.sub(r"\bif-eqz?\b", "if-ne", lines[scan_idx], count=1)
                        utils_file.write_text("".join(lines), encoding="utf-8", errors="ignore")
                        print("    Patched Utils.smali for setGmsAppEnabledStateForCn")
                        return True

                    print("    if-eq/if-eqz line after move-result not found in Utils.smali")
                    return False

                print("    getApplicationEnabledSetting call not found in target method of Utils.smali")
                return False

        print("    Method containing setGmsAppEnabledStateForCn not found in Utils.smali")
        return False
    except Exception as exc:
        print(f"    Error patching Utils.smali: {exc}")
        return False


# ---------------------------------------------------------------------------
# Report helpers
# ---------------------------------------------------------------------------
def _format_text_report(report: dict) -> str:
    mode = "DRY RUN" if report.get("dry_run") else "EXECUTE"
    lines: list[str] = [
        f"DeadZone Provision APK Legacy Patch Report  [{mode}]",
        "=" * 60,
        f"Final status     : {report.get('final_status', '?')}",
        f"Stage            : {report.get('stage', '?')}",
        f"Flavor           : {report.get('flavor', '?')}",
        f"Dry run          : {report.get('dry_run', True)}",
        f"Backup policy    : {report.get('backup_policy', 'disabled')}",
        f"Project dir      : {report.get('project_dir', '?')}",
        f"Work dir         : {report.get('work_dir', '?')}",
        "",
        "Tool:",
        f"  APKEditor jar  : {report.get('apkeditor_jar', '?')}",
        f"  jar exists     : {report.get('apkeditor_jar_exists', '?')}",
        "",
        "APK:",
        f"  Provision path : {report.get('provision_apk', '?')}",
        f"  APK found      : {report.get('provision_apk_found', '?')}",
        "",
        "Stage results:",
        f"  Decompile      : {report.get('decompile_status', 'N/A')}",
        f"  Patch          : {report.get('patch_status', 'N/A')}",
        f"  Rebuild        : {report.get('rebuild_status', 'N/A')}",
        f"  Replace        : {report.get('replace_status', 'N/A')}",
        "",
    ]

    warnings = report.get("warnings", [])
    lines.append("Warnings:")
    if warnings:
        for w in warnings:
            lines.append(f"  ! {w}")
    else:
        lines.append("  (none)")

    lines.append("")
    errors = report.get("errors", [])
    lines.append("Errors:")
    if errors:
        for e in errors:
            lines.append(f"  X {e}")
    else:
        lines.append("  (none)")

    lines.append("")
    return "\n".join(lines)


def _write_reports(report: dict) -> None:
    _REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    json_path = _REPORTS_DIR / _REPORT_JSON
    txt_path  = _REPORTS_DIR / _REPORT_TXT

    json_path.write_text(
        json.dumps(report, indent=2, ensure_ascii=False, default=str),
        encoding="utf-8",
    )
    txt_path.write_text(_format_text_report(report), encoding="utf-8")

    print(f"[provision_legacy] JSON: {json_path}")
    print(f"[provision_legacy] TXT : {txt_path}")


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------
def apply_provision_legacy_patch(
    project_dir: Path,
    flavor: str,
    execute: bool = False,
    work_dir: Path | None = None,
) -> dict:
    """
    Apply (or dry-run) the Provision.apk legacy smali patch.

    Allowed for all flavors (base, gaming, epic, legend, deadzone_*).
    If flavor is unknown, still runs but reports the flavor.

    Returns a report dict with final_status:
      DRY_RUN               -- dry-run completed, no files modified
      APPLIED               -- patch applied successfully
      SKIPPED_MISSING_APK   -- Provision.apk not found in project
      SKIPPED_MISSING_TOOL  -- APKEditor.jar not found
      FAILED                -- execute mode, one or more steps failed
    """
    effective_work_dir = work_dir if work_dir is not None else _WORK_DIR_DEFAULT

    # Resolve tool and APK upfront (needed for both dry-run and execute)
    apkeditor_jar = resolve_apkeditor_jar()
    provision_apk = find_apk(project_dir, PROVISION_APK_NAME)

    apkeditor_str    = str(apkeditor_jar) if apkeditor_jar else "(not found)"
    apkeditor_exists = apkeditor_jar is not None
    provision_str    = str(provision_apk) if provision_apk else "(not found)"
    provision_found  = provision_apk is not None

    warnings: list[str] = []
    errors:   list[str] = []

    # Base report skeleton
    report: dict = {
        "stage":                  "provision_apk_legacy",
        "flavor":                 flavor,
        "dry_run":                not execute,
        "project_dir":            str(project_dir),
        "work_dir":               str(effective_work_dir),
        "apkeditor_jar":          apkeditor_str,
        "apkeditor_jar_exists":   apkeditor_exists,
        "provision_apk":          provision_str,
        "provision_apk_found":    provision_found,
        "decompile_status":       "N/A",
        "patch_status":           "N/A",
        "rebuild_status":         "N/A",
        "replace_status":         "N/A",
        "backup_policy":          "disabled",
        "warnings":               warnings,
        "errors":                 errors,
        "final_status":           "DRY_RUN",
    }

    # --- DRY-RUN ---
    if not execute:
        if not apkeditor_exists:
            warnings.append(f"APKEditor.jar not found at expected path in third_party/mezo_core")
        if not provision_found:
            warnings.append("Provision.apk not found in any known partition location")

        decompiled_dir = effective_work_dir / PROVISION_APK_SRC_DIR_NAME
        utils_smali = (
            decompiled_dir
            / "smali" / "classes" / "com" / "android" / "provision" / "Utils.smali"
        )

        planned_steps = [
            f"copy {PROVISION_APK_NAME} -> {effective_work_dir / PROVISION_APK_NAME}",
            f"decompile {PROVISION_APK_NAME} -> {decompiled_dir.name}/",
            f"patch Utils.smali at {utils_smali}",
            f"rebuild {PROVISION_APK_NAME} from {decompiled_dir.name}/",
            f"replace {provision_str} with rebuilt APK (no backup)",
        ]
        report["planned_steps"] = planned_steps

        if not provision_found:
            report["final_status"] = "SKIPPED_MISSING_APK"
        elif not apkeditor_exists:
            report["final_status"] = "SKIPPED_MISSING_TOOL"
        else:
            report["final_status"] = "DRY_RUN"

        return report

    # --- EXECUTE ---
    if not provision_found:
        errors.append("Provision.apk not found in project; cannot patch")
        report["final_status"] = "SKIPPED_MISSING_APK"
        return report

    if not apkeditor_exists:
        errors.append("APKEditor.jar not found; cannot decompile/rebuild APK")
        report["final_status"] = "SKIPPED_MISSING_TOOL"
        return report

    # Step 1: Copy APK to work directory
    print(f"[provision_legacy] Copying {PROVISION_APK_NAME} to work dir ...")
    try:
        prepare_apk_work_dir(effective_work_dir, PROVISION_APK_NAME)
        work_apk = copy_apk_to_work(provision_apk, effective_work_dir)
    except Exception as exc:
        errors.append(f"Copy failed: {exc}")
        report["decompile_status"] = "SKIPPED"
        report["patch_status"]     = "SKIPPED"
        report["rebuild_status"]   = "SKIPPED"
        report["replace_status"]   = "SKIPPED"
        report["final_status"]     = "FAILED"
        return report

    # Step 2: Decompile
    decompiled_dir = effective_work_dir / PROVISION_APK_SRC_DIR_NAME
    print(f"[provision_legacy] Decompiling {PROVISION_APK_NAME} ...")
    decompile_ok = decompile_apk(apkeditor_jar, work_apk, decompiled_dir)
    report["decompile_status"] = "OK" if decompile_ok else "FAILED"

    if not decompile_ok:
        errors.append("Decompile failed; original APK not touched")
        report["patch_status"]   = "SKIPPED"
        report["rebuild_status"] = "SKIPPED"
        report["replace_status"] = "SKIPPED"
        report["final_status"]   = "FAILED"
        return report

    # Step 3: Patch Utils.smali (exact copy from MEZOBuildRom.py)
    print(f"[provision_legacy] Patching Utils.smali ...")
    patch_ok = patch_provision_utils(effective_work_dir)
    report["patch_status"] = "OK" if patch_ok else "FAILED"

    if not patch_ok:
        errors.append("Patch failed; original APK not touched")
        report["rebuild_status"] = "SKIPPED"
        report["replace_status"] = "SKIPPED"
        report["final_status"]   = "FAILED"
        return report

    # Step 4: Rebuild APK
    print(f"[provision_legacy] Rebuilding {PROVISION_APK_NAME} ...")
    rebuild_ok = rebuild_apk(apkeditor_jar, decompiled_dir)
    report["rebuild_status"] = "OK" if rebuild_ok else "FAILED"

    if not rebuild_ok:
        errors.append("Rebuild failed; original APK not touched")
        report["replace_status"] = "SKIPPED"
        report["final_status"]   = "FAILED"
        return report

    # Clean up decompiled source directory (mirrors recompile_provision_apk behavior)
    try:
        if decompiled_dir.exists():
            shutil.rmtree(decompiled_dir, ignore_errors=True)
            print(f"[provision_legacy] Removed temporary source dir: {decompiled_dir.name}")
    except Exception:
        pass

    # Step 5: Replace original APK (no backup)
    rebuilt_apk_path = effective_work_dir / PROVISION_APK_NAME
    print(f"[provision_legacy] Replacing original {PROVISION_APK_NAME} (no backup) ...")
    replace_result = restore_rebuilt_apk_no_backup(rebuilt_apk_path, provision_apk)
    replace_ok = replace_result["success"]
    report["replace_status"] = "OK" if replace_ok else "FAILED"

    if not replace_ok:
        errors.append(f"Replace FAILED: {replace_result.get('error', 'unknown error')}")
        report["final_status"] = "FAILED"
        return report

    report["final_status"] = "APPLIED"
    return report


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Provision.apk legacy smali patch stage (DeadZone factory)",
    )
    p.add_argument("--project",  required=True,
                   help="Path to unpacked project directory")
    p.add_argument("--flavor",   required=True,
                   help="ROM flavor (e.g. legend, base, gaming, epic)")
    p.add_argument("--work-dir", dest="work_dir", default=None,
                   help="Work directory (default: output/work/provision_apk_work)")
    p.add_argument("--execute",  action="store_true",
                   help="Apply the patch (default is dry-run)")
    return p


def _main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    project_dir = Path(args.project).resolve()
    if not project_dir.is_dir():
        print(
            f"[provision_legacy] ERROR: project directory not found: {project_dir}",
            file=sys.stderr,
        )
        return 2

    work_dir = Path(args.work_dir).resolve() if args.work_dir else None
    mode = "EXECUTE" if args.execute else "DRY-RUN"
    print(f"[provision_legacy] mode={mode}  flavor={args.flavor}  project={project_dir}")

    report = apply_provision_legacy_patch(
        project_dir=project_dir,
        flavor=args.flavor,
        execute=args.execute,
        work_dir=work_dir,
    )

    _write_reports(report)

    print(f"[provision_legacy] final_status={report['final_status']}")
    if report.get("warnings"):
        for w in report["warnings"]:
            print(f"[provision_legacy] WARNING: {w}")
    if report.get("errors"):
        for e in report["errors"]:
            print(f"[provision_legacy] ERROR: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(_main())
