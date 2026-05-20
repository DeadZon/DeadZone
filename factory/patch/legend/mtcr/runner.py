"""
Legend MTCR JAR patch runner.

Orchestrates per-JAR patch modules in order:
  patch_framework.py      → framework.jar       (system/framework/framework.jar)
  patch_services.py       → services.jar        (system/framework/services.jar)
  patch_miui_framework.py → miui-framework.jar  (system_ext/framework/miui-framework.jar)
  patch_miui_services.py  → miui-services.jar   (system_ext/framework/miui-services.jar)

Pipeline per JAR (execute mode):
  1. Locate JAR in project dir.
  2. Copy to timestamped work directory.
  3. Unpack JAR + baksmali all DEX files into smali_classes* dirs.
  4. Merge add.dex payload (if present) as new smali_classesN root.
  5. Apply MTCR patch via the dedicated patch module.
  6. smali → DEX (compile each smali_classes* dir).
  7. DEX → JAR (repack directory back to JAR).
  8. Restore rebuilt JAR to exact original filename at exact original ROM path.
     No backups. No _patched / _new / _mod suffixes.

Cross-JAR stages run AFTER all JARs are rebuilt and restored:
  signature_bypass_legacy  (optional, skipped if module missing)
  jar_misc_legacy          (optional, skipped if module missing)
  kaori_legacy             (optional, skipped if module missing)

Dry-run mode: no files are written; every step reports WOULD_* intent.

Reports:
  output/reports/legend_mtcr_report.json
  output/reports/legend_mtcr_report.txt

Flavor guard:
  Only runs for: legend, deadzone_legend (case-insensitive).
  All other flavors: SKIPPED_NON_LEGEND, nothing modified.

CLI:
  # dry-run:
  python -m factory.patch.legend.mtcr.runner \\
      --project "path/to/unpacked_project" \\
      --flavor legend

  # execute:
  python -m factory.patch.legend.mtcr.runner \\
      --project "path/to/unpacked_project" \\
      --flavor legend \\
      --execute
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
import time
from pathlib import Path
from typing import Callable

from factory.patch.common.jar_workspace import (
    repack_dir_to_jar,
    repack_smali_to_dex,
    resolve_partition_file,
    restore_rebuilt_jar_no_backup,
    unpack_dir_for,
    unpack_jar,
)
from factory.patch.legend.add_dex_rules import find_add_dex_for_jar
from factory.patch.common.add_dex_merger import merge_add_dex
from factory.patch.legend.mtcr.patch_framework import (
    apply_framework_mtcr_patch,
    TARGET_JAR_NAME       as _FW_JAR,
    TARGET_JAR_PARTITION  as _FW_PART,
    TARGET_JAR_REL_PATH   as _FW_PATH,
)
from factory.patch.legend.mtcr.patch_services import (
    apply_services_mtcr_patch,
    TARGET_JAR_NAME       as _SVC_JAR,
    TARGET_JAR_PARTITION  as _SVC_PART,
    TARGET_JAR_REL_PATH   as _SVC_PATH,
)
from factory.patch.legend.mtcr.patch_miui_framework import (
    apply_miui_framework_mtcr_patch,
    TARGET_JAR_NAME       as _MFW_JAR,
    TARGET_JAR_PARTITION  as _MFW_PART,
    TARGET_JAR_REL_PATH   as _MFW_PATH,
)
from factory.patch.legend.mtcr.patch_miui_services import (
    apply_miui_services_mtcr_patch,
    TARGET_JAR_NAME       as _MSVC_JAR,
    TARGET_JAR_PARTITION  as _MSVC_PART,
    TARGET_JAR_REL_PATH   as _MSVC_PATH,
)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_REPO_ROOT  = Path(__file__).resolve().parents[4]
_OUTPUT_ROOT = _REPO_ROOT / "output"
_REPORTS_DIR = _OUTPUT_ROOT / "reports"

_LEGEND_FLAVORS = frozenset({"legend", "deadzone_legend"})

_ADD_DEX_CANONICAL = _REPO_ROOT / "third_party" / "mezo_core" / "MEZO_LEGEND" / "jar"
_ADD_DEX_FALLBACK  = _REPO_ROOT / "Legend" / "jar"

_REPORT_JSON = "legend_mtcr_report.json"
_REPORT_TXT  = "legend_mtcr_report.txt"

# (jar_name, partition, rel_path, patch_function)
_JAR_PATCHES: list[tuple[str, str, str, Callable]] = [
    (_FW_JAR,   _FW_PART,   _FW_PATH,   apply_framework_mtcr_patch),
    (_SVC_JAR,  _SVC_PART,  _SVC_PATH,  apply_services_mtcr_patch),
    (_MFW_JAR,  _MFW_PART,  _MFW_PATH,  apply_miui_framework_mtcr_patch),
    (_MSVC_JAR, _MSVC_PART, _MSVC_PATH, apply_miui_services_mtcr_patch),
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _is_legend_flavor(flavor: str) -> bool:
    return flavor.strip().lower().replace("-", "_") in _LEGEND_FLAVORS


def _add_dex_dir() -> Path:
    if _ADD_DEX_CANONICAL.is_dir():
        return _ADD_DEX_CANONICAL
    return _ADD_DEX_FALLBACK


# ---------------------------------------------------------------------------
# Report formatting
# ---------------------------------------------------------------------------

def _format_text_report(report: dict) -> str:
    mode = "DRY RUN" if report.get("dry_run") else "EXECUTE"
    lines: list[str] = [
        f"DeadZone Legend MTCR JAR Patch Report  [{mode}]",
        "=" * 64,
        f"Final status  : {report.get('final_status', '?')}",
        f"Flavor        : {report.get('flavor', '?')}",
        f"Dry run       : {report.get('dry_run', True)}",
        f"Project dir   : {report.get('project_dir', '?')}",
        f"Work dir      : {report.get('work_dir', '?')}",
        f"Add-DEX dir   : {report.get('add_dex_dir', '?')}",
        "",
        "JAR results:",
    ]

    for jar_name, jr in report.get("jars", {}).items():
        lines.append(f"  {jar_name}:")
        lines.append(f"    original filename : {jr.get('original_filename', jar_name)}")
        lines.append(f"    original path     : {jr.get('project_jar_path', '(not found)')}")
        lines.append(f"    found             : {jr.get('found', False)}")
        lines.append(f"    unpack            : {jr.get('unpack_status', 'N/A')}")
        lines.append(f"    add_dex           : {jr.get('add_dex_status', 'N/A')}")
        lines.append(f"    mtcr              : {jr.get('mtcr_status', 'N/A')}")
        lines.append(f"    rebuild           : {jr.get('rebuild_status', 'N/A')}")
        lines.append(f"    restore           : {jr.get('restore_status', 'N/A')}")
        lines.append(f"    restored filename : {jr.get('restored_filename', '?')}")
        lines.append(f"    restored path     : {jr.get('restored_path', '?')}")
        lines.append(f"    final             : {jr.get('final_status', '?')}")
        for e in jr.get("errors", []):
            lines.append(f"    ! ERROR: {e}")
        for w in jr.get("warnings", []):
            lines.append(f"    ~ WARN : {w}")

        mtcr_r = jr.get("mtcr_result", {})
        mod  = mtcr_r.get("modified_count", 0)
        add  = mtcr_r.get("added_count", 0)
        cr   = mtcr_r.get("class_results", [])
        if mod or add or cr:
            lines.append(f"    MTCR: modified={mod} added={add} class_ops={len(cr)}")
        lines.append("")

    cross = report.get("cross_jar_stages", {})
    if cross:
        lines.append("Cross-JAR stages:")
        for stage_name, sr in cross.items():
            lines.append(f"  {stage_name}: {sr.get('status', '?')}")
            for e in sr.get("errors", []):
                lines.append(f"    ! {e}")
        lines.append("")

    warnings = report.get("warnings", [])
    lines.append("Warnings:")
    lines.extend(f"  ~ {w}" for w in warnings) if warnings else lines.append("  (none)")
    lines.append("")

    errors = report.get("errors", [])
    lines.append("Errors:")
    lines.extend(f"  ! {e}" for e in errors) if errors else lines.append("  (none)")
    lines.append("")

    return "\n".join(lines)


def _write_reports(report: dict) -> None:
    _REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    json_path = _REPORTS_DIR / _REPORT_JSON
    txt_path  = _REPORTS_DIR / _REPORT_TXT
    json_path.write_text(
        json.dumps(report, indent=2, ensure_ascii=True, default=str),
        encoding="utf-8",
    )
    txt_path.write_text(_format_text_report(report), encoding="utf-8")
    report["report_files"] = {"json": str(json_path), "txt": str(txt_path)}
    print(f"[legend_mtcr] JSON: {json_path}")
    print(f"[legend_mtcr] TXT : {txt_path}")


# ---------------------------------------------------------------------------
# Per-JAR patch orchestration
# ---------------------------------------------------------------------------

def _patch_one_jar(
    jar_name: str,
    partition: str,
    rel_path: str,
    patch_fn: Callable,
    project_dir: Path,
    work_dir: Path,
    add_dex_search: Path,
    execute: bool,
) -> dict:
    """Copy, unpack, patch, rebuild and restore one JAR."""
    jr: dict = {
        "jar_name":          jar_name,
        "partition":         partition,
        "rel_path":          rel_path,
        "original_filename": jar_name,
        "found":             False,
        "project_jar_path":  None,
        "unpack_status":     "N/A",
        "add_dex_status":    "N/A",
        "mtcr_status":       "N/A",
        "rebuild_status":    "N/A",
        "restore_status":    "N/A",
        "restored_filename": jar_name,
        "restored_path":     None,
        "final_status":      "FAILED",
        "warnings":          [],
        "errors":            [],
        "mtcr_result":       {},
    }

    parts = rel_path.split("/")
    project_jar = resolve_partition_file(project_dir, partition, *parts)
    if project_jar is None or not project_jar.is_file():
        msg = f"{jar_name} not found in project at {partition}/{rel_path}"
        jr["errors"].append(msg)
        jr["final_status"] = "SKIPPED_MISSING"
        print(f"[legend_mtcr] SKIPPED_MISSING: {jar_name}")
        return jr

    jr["found"]           = True
    jr["project_jar_path"] = str(project_jar)

    if not execute:
        jr["final_status"] = "WOULD_PATCH"
        jr["unpack_status"]   = "WOULD_UNPACK"
        jr["add_dex_status"]  = "WOULD_CHECK"
        jr["mtcr_status"]     = "WOULD_PATCH"
        jr["rebuild_status"]  = "WOULD_REBUILD"
        jr["restore_status"]  = "WOULD_RESTORE"
        jr["restored_path"]   = str(project_jar)
        return jr

    # Step 1: Copy JAR to workspace
    workspace_jar = work_dir / jar_name
    try:
        shutil.copy2(project_jar, workspace_jar)
        print(f"[legend_mtcr] Copied {jar_name} to workspace")
    except Exception as exc:
        jr["errors"].append(f"Copy failed: {exc}")
        return jr

    # Step 2: Unpack JAR + baksmali
    unpack_dir = unpack_dir_for(work_dir, jar_name)
    unpack_result = unpack_jar(workspace_jar, unpack_dir)
    if unpack_result.errors:
        jr["unpack_status"] = "FAILED"
        jr["errors"].extend(unpack_result.errors)
        print(f"[legend_mtcr] Unpack FAILED: {jar_name}")
        return jr
    jr["unpack_status"] = "OK"

    # Step 3: Merge add.dex payload (optional)
    add_dex_path = find_add_dex_for_jar(jar_name, add_dex_search)
    if add_dex_path is not None:
        print(f"[legend_mtcr] Merging add.dex: {add_dex_path.name} -> {jar_name}")
        adr = merge_add_dex(add_dex_path, unpack_dir, jar_name, dry_run=False)
        jr["add_dex_status"] = "OK" if not adr.errors else "PARTIAL"
        for e in adr.errors:
            jr["warnings"].append(f"add_dex: {e}")
    else:
        jr["add_dex_status"] = "SKIPPED_NOT_FOUND"
        print(f"[legend_mtcr] No add.dex for {jar_name}")

    # Step 4: Apply MTCR patch
    print(f"[legend_mtcr] Applying MTCR: {jar_name}")
    mtcr_result = patch_fn(unpack_dir, jr, execute)
    jr["mtcr_result"] = mtcr_result
    jr["mtcr_status"] = mtcr_result.get("status", "UNKNOWN")
    if mtcr_result.get("errors"):
        jr["warnings"].extend(mtcr_result["errors"])

    # Step 5: smali → DEX
    print(f"[legend_mtcr] Recompiling smali: {jar_name}")
    dex_results = repack_smali_to_dex(unpack_dir)
    failed_dex = [(n, e) for (n, ok, e) in dex_results if not ok]
    if failed_dex:
        jr["rebuild_status"] = "FAILED"
        for name, err in failed_dex:
            jr["errors"].append(f"smali→dex failed for {name}: {err}")
        print(f"[legend_mtcr] smali repack FAILED: {jar_name}")
        return jr
    jr["rebuild_status"] = "OK"

    # Step 6: DEX → JAR
    rebuilt_jar = work_dir / f"{jar_name}.rebuilt"
    jar_result = repack_dir_to_jar(unpack_dir, rebuilt_jar)
    if not jar_result.success:
        jr["rebuild_status"] = "FAILED_JAR"
        jr["errors"].append(f"JAR repack failed: {jar_result.error}")
        print(f"[legend_mtcr] JAR repack FAILED: {jar_name}")
        return jr

    # Step 7: Restore to exact original filename at exact original ROM path
    print(f"[legend_mtcr] Restoring {jar_name} -> {project_jar}")
    restore_result = restore_rebuilt_jar_no_backup(rebuilt_jar, project_jar)
    if not restore_result.success:
        jr["restore_status"] = "FAILED"
        jr["errors"].append(f"Restore failed: {restore_result.error}")
        print(f"[legend_mtcr] Restore FAILED: {jar_name}")
        return jr

    jr["restore_status"]   = "OK"
    jr["restored_filename"] = jar_name          # exact original filename
    jr["restored_path"]    = str(project_jar)   # exact original path
    jr["final_status"]     = "APPLIED"
    print(f"[legend_mtcr] APPLIED: {jar_name} -> {project_jar.name}")
    return jr


# ---------------------------------------------------------------------------
# Cross-JAR optional stages
# ---------------------------------------------------------------------------

def _run_cross_jar_stages(work_dir: Path, flavor: str, execute: bool) -> dict:
    """Run optional cross-JAR stages (sig bypass, misc legacy, kaori)."""
    stages: dict = {}

    for mod_name, attr_name, call_kwargs in [
        (
            "factory.patch.legend.signature_bypass_legacy",
            "apply_legacy_signature_bypass",
            {"work_dir": work_dir, "android_major": None, "flavor": flavor, "execute": execute},
        ),
        (
            "factory.patch.legend.jar_misc_legacy",
            "apply_legend_jar_misc_legacy_patches",
            {"work_dir": work_dir, "android_major": None, "flavor": flavor, "execute": execute},
        ),
        (
            "factory.patch.legend.kaori_legacy",
            "apply_kaori_legacy_patch",
            {"work_dir": work_dir, "flavor": flavor, "android_major": None, "execute": execute},
        ),
    ]:
        stage_key = mod_name.rsplit(".", 1)[-1]
        try:
            import importlib
            mod = importlib.import_module(mod_name)
            fn = getattr(mod, attr_name, None)
            if fn is None:
                stages[stage_key] = {"status": "SKIPPED_MISSING_MODULE"}
                continue
            if not execute:
                stages[stage_key] = {"status": "WOULD_RUN"}
                continue
            rep = fn(**call_kwargs)
            if hasattr(rep, "status"):
                # SigBypassReport-style object
                stages[stage_key] = {
                    "status":   str(getattr(rep, "status", "UNKNOWN")),
                    "warnings": list(getattr(rep, "warnings", [])),
                    "errors":   list(getattr(rep, "errors", [])),
                }
            else:
                stages[stage_key] = {
                    "status":   rep.get("status", "UNKNOWN"),
                    "warnings": rep.get("warnings", []),
                    "errors":   rep.get("errors", []),
                }
        except ImportError:
            stages[stage_key] = {"status": "SKIPPED_MISSING_MODULE"}
        except Exception as exc:
            stages[stage_key] = {"status": "FAILED", "errors": [str(exc)], "warnings": []}

    return stages


# ---------------------------------------------------------------------------
# Dry-run planning
# ---------------------------------------------------------------------------

def _build_dry_run_plan(project_dir: Path) -> list[dict]:
    plan: list[dict] = []
    for jar_name, partition, rel_path, _ in _JAR_PATCHES:
        parts = rel_path.split("/")
        project_jar = resolve_partition_file(project_dir, partition, *parts)
        found = project_jar is not None and project_jar.is_file()
        plan.append({
            "jar_name":          jar_name,
            "partition":         partition,
            "original_filename": jar_name,
            "found":             found,
            "project_path":      str(project_jar) if project_jar else "(not found)",
            "would_restore_as":  jar_name,
            "would_restore_to":  str(project_jar) if project_jar else "(not found)",
        })
    return plan


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def apply_legend_mtcr_patches(
    project_dir: Path,
    flavor: str,
    execute: bool = False,
) -> dict:
    """
    Apply (or dry-run) all Legend MTCR JAR patches.

    Each rebuilt JAR is restored with its exact original filename to its
    exact original ROM path.  No backup files are created.

    Parameters
    ----------
    project_dir : Path
        Root of the unpacked ROM project directory.
    flavor : str
        ROM flavor identifier (e.g. "legend", "deadzone_legend", "base").
    execute : bool
        True -> apply all changes.  False (default) -> dry-run only.

    Returns
    -------
    dict
        Report dict with final_status and per-JAR detail.
    """
    project_dir = Path(project_dir).resolve()
    ts = time.strftime("%Y%m%d_%H%M%S")
    work_dir = _OUTPUT_ROOT / "work" / f"legend_mtcr_{ts}"
    add_dex_dir = _add_dex_dir()

    report: dict = {
        "stage":        "legend_mtcr",
        "flavor":       flavor,
        "dry_run":      not execute,
        "project_dir":  str(project_dir),
        "work_dir":     str(work_dir),
        "add_dex_dir":  str(add_dex_dir),
        "backup_policy": "disabled",
        "jars":         {},
        "cross_jar_stages": {},
        "planned":      [],
        "warnings":     [],
        "errors":       [],
        "final_status": "DRY_RUN",
        "report_files": {},
    }

    # Flavor guard
    if not _is_legend_flavor(flavor):
        report["final_status"] = "SKIPPED_NON_LEGEND"
        print(
            f"[legend_mtcr] Flavor '{flavor}' is not Legend. "
            f"final_status=SKIPPED_NON_LEGEND"
        )
        _write_reports(report)
        return report

    mode = "EXECUTE" if execute else "DRY-RUN"
    print(f"[legend_mtcr] === Legend MTCR Patch Runner ({mode}) ===")
    print(f"[legend_mtcr] Project   : {project_dir}")
    print(f"[legend_mtcr] Work dir  : {work_dir}")
    print(f"[legend_mtcr] Add-DEX   : {add_dex_dir}")

    # Dry-run: just plan, don't touch anything
    if not execute:
        report["planned"] = _build_dry_run_plan(project_dir)
        report["cross_jar_stages"] = _run_cross_jar_stages(work_dir, flavor, execute=False)
        _write_reports(report)
        return report

    # Execute
    work_dir.mkdir(parents=True, exist_ok=True)
    any_failed = False

    for jar_name, partition, rel_path, patch_fn in _JAR_PATCHES:
        print(f"[legend_mtcr] --- Processing {jar_name} ---")
        jr = _patch_one_jar(
            jar_name=jar_name,
            partition=partition,
            rel_path=rel_path,
            patch_fn=patch_fn,
            project_dir=project_dir,
            work_dir=work_dir,
            add_dex_search=add_dex_dir,
            execute=execute,
        )
        report["jars"][jar_name] = jr
        if jr.get("final_status") not in ("APPLIED", "SKIPPED_MISSING"):
            any_failed = True
            report["errors"].extend(jr.get("errors", []))
        else:
            report["warnings"].extend(jr.get("warnings", []))

    # Cross-JAR stages run after all JARs are rebuilt and restored
    print("[legend_mtcr] --- Cross-JAR stages ---")
    report["cross_jar_stages"] = _run_cross_jar_stages(work_dir, flavor, execute=True)
    for stage_key, sr in report["cross_jar_stages"].items():
        if sr.get("errors"):
            report["warnings"].extend(
                f"{stage_key}: {e}" for e in sr["errors"]
            )

    report["final_status"] = "FAILED" if any_failed else "APPLIED"
    print(f"[legend_mtcr] final_status={report['final_status']}")
    _write_reports(report)
    return report


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Legend MTCR JAR patch runner (DeadZone factory)",
    )
    p.add_argument(
        "--project", required=True,
        help="Path to unpacked ROM project directory",
    )
    p.add_argument(
        "--flavor", required=True,
        help="ROM flavor: legend | deadzone_legend | <other>",
    )
    p.add_argument(
        "--execute", action="store_true",
        help="Apply patches (default is dry-run only)",
    )
    return p


def _main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    project_dir = Path(args.project).resolve()
    if not project_dir.is_dir():
        print(
            f"[legend_mtcr] ERROR: project directory not found: {project_dir}",
            file=sys.stderr,
        )
        return 2

    mode = "EXECUTE" if args.execute else "DRY-RUN"
    print(f"[legend_mtcr] mode={mode}  flavor={args.flavor}  project={project_dir}")

    report = apply_legend_mtcr_patches(
        project_dir=project_dir,
        flavor=args.flavor,
        execute=args.execute,
    )

    print(f"[legend_mtcr] final_status={report['final_status']}")
    for w in report.get("warnings", []):
        print(f"[legend_mtcr] WARNING: {w}")
    for e in report.get("errors", []):
        print(f"[legend_mtcr] ERROR: {e}", file=sys.stderr)

    return 1 if report.get("errors") else 0


if __name__ == "__main__":
    sys.exit(_main())
