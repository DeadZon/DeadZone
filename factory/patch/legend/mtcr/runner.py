"""
Legend MTCR JAR patch runner — class/method-level edition.

Architecture
============
Real patch logic lives in two layers:

  1. Per-class rule modules (auto-discovered):
       factory/patch/legend/mods/jars/framework/      → framework.jar
       factory/patch/legend/mods/jars/services/       → services.jar
       factory/patch/legend/mods/jars/miui_framework/ → miui-framework.jar
       factory/patch/legend/mods/jars/miui_services/  → miui-services.jar

  2. Config-gated mod modules (registry-driven):
       factory/patch/legend/mods/jars/<group>/<mod_id>/mod.py
       Registered in factory/patch/legend/mods/registry.py

Each class-rule module exposes TARGET_JAR, TARGET_CLASS, and PATCHES.
Each mod module exposes apply(unpack_dir, config, dry_run) -> dict.

This runner imports all of them, groups by JAR, and applies them.

Pipeline per JAR (execute mode):
  1. Locate JAR in project dir.
  2. Copy to timestamped work directory.
  3. Unpack JAR + baksmali all DEX files into smali_classes* dirs.
  4. Apply add_dex_payload rules (optional, non-blocking).
  5. Apply every per-class PATCHES list — class by class, method by method.
  6. Apply config-gated mods for this JAR group.
  7. smali → DEX (compile each smali_classes* dir).
  8. DEX → JAR (repack dir back to JAR).
  9. Restore rebuilt JAR to exact original filename at exact original ROM path.

Reports (class/method-level):
  output/reports/legend_mtcr_report.json
  output/reports/legend_mtcr_report.txt

Flavor guard:
  Only runs for: legend, deadzone_legend (case-insensitive).

Public API:
  apply_legend_mtcr_patches(project_dir, flavor, execute=False) -> dict

CLI:
  python -m factory.patch.legend.mtcr.runner \\
      --project "path/to/unpacked" \\
      --flavor legend [--execute]
"""
from __future__ import annotations

import argparse
import importlib
import json
import pkgutil
import shutil
import sys
import time
from pathlib import Path
from typing import Any

from factory.patch.common.jar_workspace import (
    repack_dir_to_jar,
    repack_smali_to_dex,
    resolve_partition_file,
    restore_rebuilt_jar_no_backup,
    unpack_dir_for,
    unpack_jar,
)
from factory.patch.legend.mtcr.smart_smali_patcher import (
    ClassMatchStatus,
    MethodMatchStatus,
    PatchApplyStatus,
    apply_smart_patch,
    find_class,
    normalize_smali_for_match,
)
from factory.patch.common.add_dex_merger import merge_add_dex
from factory.patch.legend.mods.registry import (
    LEGEND_JAR_MODS,
    merge_profile,
)

# ── Paths ──────────────────────────────────────────────────────────────────────

_REPO_ROOT      = Path(__file__).resolve().parents[4]
_MODS_JARS_PKG  = Path(__file__).resolve().parents[1] / "mods" / "jars"
_OUTPUT_ROOT    = _REPO_ROOT / "output"
_REPORTS_DIR    = _OUTPUT_ROOT / "reports"

_ADD_DEX_CANONICAL = _REPO_ROOT / "third_party" / "mezo_core" / "MEZO_LEGEND" / "jar"
_ADD_DEX_FALLBACK  = _REPO_ROOT / "Legend" / "jar"

_REPORT_JSON = "legend_mtcr_report.json"
_REPORT_TXT  = "legend_mtcr_report.txt"

_LEGEND_FLAVORS = frozenset({"legend", "deadzone_legend"})

# ── JAR configuration ──────────────────────────────────────────────────────────

_JARS: list[dict] = [
    {
        "jar_name":   "framework.jar",
        "partition":  "system",
        "rel_path":   "framework/framework.jar",
        "pkg_subdir": "framework",
    },
    {
        "jar_name":   "services.jar",
        "partition":  "system",
        "rel_path":   "framework/services.jar",
        "pkg_subdir": "services",
    },
    {
        "jar_name":   "miui-framework.jar",
        "partition":  "system_ext",
        "rel_path":   "framework/miui-framework.jar",
        "pkg_subdir": "miui_framework",
    },
    {
        "jar_name":   "miui-services.jar",
        "partition":  "system_ext",
        "rel_path":   "framework/miui-services.jar",
        "pkg_subdir": "miui_services",
    },
]


# ── Module discovery ──────────────────────────────────────────────────────────

def _discover_class_modules(pkg_subdir: str) -> list[Any]:
    """
    Import all non-__init__ modules under
    factory.patch.legend.mods.jars.<pkg_subdir> and return them.
    """
    base_pkg = f"factory.patch.legend.mods.jars.{pkg_subdir}"
    sub_path = _MODS_JARS_PKG / pkg_subdir
    if not sub_path.is_dir():
        return []

    modules = []
    for info in pkgutil.iter_modules([str(sub_path)]):
        if info.name.startswith("__"):
            continue
        full_name = f"{base_pkg}.{info.name}"
        try:
            mod = importlib.import_module(full_name)
            modules.append(mod)
        except Exception as exc:
            print(f"[legend_mtcr] WARNING: could not import {full_name}: {exc}")
    return modules


# ── Add-DEX path resolver ─────────────────────────────────────────────────────

def _add_dex_dir() -> Path:
    return _ADD_DEX_CANONICAL if _ADD_DEX_CANONICAL.is_dir() else _ADD_DEX_FALLBACK


# ── Per-patch apply helpers ───────────────────────────────────────────────────

def _smali_dirs_in(unpack_dir: Path) -> list[Path]:
    from factory.patch.common.smali_tools import smali_dirs_in
    return smali_dirs_in(unpack_dir)


def _patch_result_to_dict(pr) -> dict:
    """Convert a smart_smali_patcher.PatchResult to the runner's report dict format."""
    return {
        "patch_id":        pr.patch_id,
        "method":          pr.method,
        "type":            pr.type,
        "status":          pr.status.value,
        "class_match":     pr.class_match.value,
        "method_match":    pr.method_match.value,
        "class_strategy":  pr.class_strategy,
        "method_strategy": pr.method_strategy,
        "message":         pr.message,
    }


def _apply_class_module(
    mod: Any,
    smali_roots: list[Path],
    dry_run: bool,
) -> dict:
    """
    Apply all PATCHES from one class-rule module using the smart smali patcher.

    Returns a class-level result dict with per-patch rows that include
    CLASS MATCH and METHOD MATCH strategy information.
    """
    jar_name       = getattr(mod, "TARGET_JAR",           "?")
    target_class   = getattr(mod, "TARGET_CLASS",         "?")
    patches        = getattr(mod, "PATCHES",              [])
    fallback_names = getattr(mod, "CLASS_FALLBACK_NAMES", [])
    class_anchors  = getattr(mod, "CLASS_ANCHORS",        [])

    cr: dict = {
        "class":         target_class,
        "jar":           jar_name,
        "status":        "NOT_APPLIED",
        "patch_count":   len(patches),
        "patch_results": [],
        "errors":        [],
    }

    smali_patches = [p for p in patches if p.get("type") != "dex_add"]

    for p in smali_patches:
        enriched = dict(p)
        enriched["target_class"] = target_class
        if fallback_names and "class_fallback_names" not in enriched:
            enriched["class_fallback_names"] = fallback_names
        if class_anchors and "class_anchors" not in enriched:
            enriched["class_anchors"] = class_anchors

        try:
            patch_result = apply_smart_patch(smali_roots, enriched, dry_run=dry_run)
            cr["patch_results"].append(_patch_result_to_dict(patch_result))
            if patch_result.status == PatchApplyStatus.FAILED:
                cr["errors"].append(
                    f"{patch_result.patch_id}: {patch_result.message}"
                )
        except Exception as exc:
            cr["patch_results"].append({
                "patch_id":        p.get("id", "?"),
                "method":          p.get("method", ""),
                "type":            p.get("type", "?"),
                "status":          "FAILED",
                "class_match":     "UNKNOWN",
                "method_match":    "UNKNOWN",
                "class_strategy":  "",
                "method_strategy": "",
                "message":         f"exception: {exc}",
            })
            cr["errors"].append(f"{p.get('id', '?')}: exception: {exc}")

    patched = sum(1 for r in cr["patch_results"] if r["status"] in ("PATCHED", "EXISTS"))
    would   = sum(1 for r in cr["patch_results"] if r["status"] == "WOULD_PATCH")
    failed  = sum(1 for r in cr["patch_results"] if r["status"] == "FAILED")

    if failed:
        cr["status"] = "FAILED"
    elif patched:
        cr["status"] = "PATCHED"
    elif would:
        cr["status"] = "WOULD_PATCH"
    else:
        cr["status"] = "SKIPPED"
    return cr


# ── DEX add merge ─────────────────────────────────────────────────────────────

def _apply_dex_patches_for_jar(
    modules: list[Any],
    unpack_dir: Path,
    jar_name: str,
    add_dex_search: Path,
    dry_run: bool,
) -> list[dict]:
    dex_results: list[dict] = []
    for mod in modules:
        for p in getattr(mod, "PATCHES", []):
            if p.get("type") != "dex_add":
                continue
            if p.get("target_jar") != jar_name:
                continue
            payload_name = p["payload_name"]
            output_dex   = p.get("output_dex", "classes_mezo.dex")
            payload_path = add_dex_search / payload_name
            dr: dict = {
                "patch_id":     p.get("id", "?"),
                "payload_name": payload_name,
                "output_dex":   output_dex,
                "status":       "UNKNOWN",
                "message":      "",
            }
            if not payload_path.is_file():
                dr["status"]  = "SKIPPED_NOT_FOUND"
                dr["message"] = f"payload not found: {payload_path}"
                dex_results.append(dr)
                continue
            if dry_run:
                dr["status"]  = "WOULD_ADD"
                dr["message"] = f"would merge {payload_name} -> {output_dex}"
                dex_results.append(dr)
                continue
            try:
                result = merge_add_dex(payload_path, unpack_dir, jar_name, dry_run=False)
                dr["status"]  = "PATCHED" if not result.errors else "PARTIAL"
                dr["message"] = "; ".join(result.errors) if result.errors else "ok"
            except Exception as exc:
                dr["status"]  = "FAILED"
                dr["message"] = str(exc)
            dex_results.append(dr)
    return dex_results


# ── Config-gated mod runner ───────────────────────────────────────────────────

def _run_jar_mods(
    jar_group: str,
    unpack_dir: Path,
    config: dict,
    dry_run: bool,
) -> dict[str, dict]:
    """
    Run all registered mods for a JAR group from the mod registry.
    Returns {mod_id: result_dict}.
    """
    mod_ids  = LEGEND_JAR_MODS.get(jar_group, [])
    base_pkg = f"factory.patch.legend.mods.jars.{jar_group}"
    results: dict[str, dict] = {}

    for mod_id in mod_ids:
        full_module = f"{base_pkg}.{mod_id}.mod"
        try:
            mod    = importlib.import_module(full_module)
            result = mod.apply(unpack_dir, config, dry_run)
            results[mod_id] = result
        except ImportError as exc:
            results[mod_id] = {
                "mod_id": mod_id, "status": "SKIPPED_MISSING_MODULE",
                "errors": [str(exc)], "warnings": [],
            }
        except Exception as exc:
            results[mod_id] = {
                "mod_id": mod_id, "status": "FAILED",
                "errors": [str(exc)], "warnings": [],
            }

    return results


# ── Per-JAR orchestration ─────────────────────────────────────────────────────

def _patch_one_jar(
    jar_cfg: dict,
    project_dir: Path,
    work_dir: Path,
    add_dex_search: Path,
    execute: bool,
    mods_config: dict,
) -> dict:
    jar_name  = jar_cfg["jar_name"]
    partition = jar_cfg["partition"]
    rel_path  = jar_cfg["rel_path"]
    pkg_sub   = jar_cfg["pkg_subdir"]

    jr: dict = {
        "jar_name":          jar_name,
        "partition":         partition,
        "original_filename": jar_name,
        "found":             False,
        "project_jar_path":  None,
        "unpack_status":     "N/A",
        "dex_add_results":   [],
        "class_results":     [],
        "mod_results":       {},
        "rebuild_status":    "N/A",
        "restore_status":    "N/A",
        "restored_filename": jar_name,
        "restored_path":     None,
        "final_status":      "FAILED",
        "warnings":          [],
        "errors":            [],
    }

    # Discover per-class modules for this JAR
    modules = _discover_class_modules(pkg_sub)
    smali_patches_mods = [m for m in modules if any(
        p.get("type") != "dex_add" for p in getattr(m, "PATCHES", [])
    )]

    # Locate JAR in project
    parts = rel_path.split("/")
    project_jar = resolve_partition_file(project_dir, partition, *parts)
    if project_jar is None or not project_jar.is_file():
        msg = f"{jar_name} not found in project at {partition}/{rel_path}"
        jr["errors"].append(msg)
        jr["final_status"] = "SKIPPED_MISSING"
        print(f"[legend_mtcr] SKIPPED_MISSING: {jar_name}")
        return jr

    jr["found"]            = True
    jr["project_jar_path"] = str(project_jar)

    if not execute:
        mod_ids = LEGEND_JAR_MODS.get(pkg_sub, [])
        jr["mod_results"] = {
            mod_id: {"mod_id": mod_id, "status": "WOULD_RUN"}
            for mod_id in mod_ids
        }
        jr["final_status"] = "WOULD_PATCH"
        jr["unpack_status"]  = "WOULD_UNPACK"
        jr["rebuild_status"] = "WOULD_REBUILD"
        jr["restore_status"] = "WOULD_RESTORE"
        jr["restored_path"]  = str(project_jar)
        jr["class_results"]  = [
            {
                "class":  getattr(m, "TARGET_CLASS", "?"),
                "jar":    getattr(m, "TARGET_JAR",   "?"),
                "status": "WOULD_PATCH",
                "patch_count": len(getattr(m, "PATCHES", [])),
                "patch_results": [
                    {
                        "patch_id":        p.get("id", "?"),
                        "method":          p.get("method", ""),
                        "type":            p.get("type", "?"),
                        "status":          "WOULD_PATCH",
                        "class_match":     "N/A",
                        "method_match":    "N/A",
                        "class_strategy":  "",
                        "method_strategy": "",
                        "message":         "dry-run (no JAR unpacked)",
                    }
                    for p in getattr(m, "PATCHES", [])
                    if p.get("type") != "dex_add"
                ],
                "errors": [],
            }
            for m in smali_patches_mods
        ]
        return jr

    # ── Execute ──────────────────────────────────────────────────────────────

    # Copy JAR to workspace
    workspace_jar = work_dir / jar_name
    try:
        shutil.copy2(project_jar, workspace_jar)
        print(f"[legend_mtcr] Copied {jar_name} to workspace")
    except Exception as exc:
        jr["errors"].append(f"Copy failed: {exc}")
        return jr

    # Unpack JAR + baksmali
    unpack_dir_path = unpack_dir_for(work_dir, jar_name)
    unpack_result   = unpack_jar(workspace_jar, unpack_dir_path)
    if unpack_result.errors:
        jr["unpack_status"] = "FAILED"
        jr["errors"].extend(unpack_result.errors)
        print(f"[legend_mtcr] Unpack FAILED: {jar_name}")
        return jr
    jr["unpack_status"] = "OK"

    # DEX add payloads
    smali_roots = _smali_dirs_in(unpack_dir_path)
    dex_results = _apply_dex_patches_for_jar(
        modules, unpack_dir_path, jar_name, add_dex_search, dry_run=False,
    )
    jr["dex_add_results"] = dex_results
    smali_roots = _smali_dirs_in(unpack_dir_path)   # refresh after possible dex merge

    # Per-class patches
    print(f"[legend_mtcr] Applying {len(smali_patches_mods)} class patches: {jar_name}")
    for mod in smali_patches_mods:
        cr = _apply_class_module(mod, smali_roots, dry_run=False)
        jr["class_results"].append(cr)
        s   = cr["status"]
        cls = cr["class"]
        print(f"[legend_mtcr]   {s:30s}  {cls}")
        if cr["errors"]:
            jr["warnings"].extend(cr["errors"])

    # Config-gated mods
    print(f"[legend_mtcr] Running mods for: {jar_name}")
    jr["mod_results"] = _run_jar_mods(pkg_sub, unpack_dir_path, mods_config, dry_run=False)
    for mod_id, mr in jr["mod_results"].items():
        st = mr.get("status", "?")
        print(f"[legend_mtcr]   mod {mod_id}: {st}")
        if mr.get("errors"):
            jr["warnings"].extend(f"{mod_id}: {e}" for e in mr["errors"])

    # smali → DEX
    print(f"[legend_mtcr] Recompiling smali: {jar_name}")
    dex_compile = repack_smali_to_dex(unpack_dir_path)
    failed_dex  = [(n, e) for (n, ok, e) in dex_compile if not ok]
    if failed_dex:
        jr["rebuild_status"] = "FAILED"
        for name, err in failed_dex:
            jr["errors"].append(f"smali→dex failed for {name}: {err}")
        print(f"[legend_mtcr] smali repack FAILED: {jar_name}")
        return jr
    jr["rebuild_status"] = "OK"

    # DEX → JAR
    rebuilt_jar = work_dir / f"{jar_name}.rebuilt"
    jar_result  = repack_dir_to_jar(unpack_dir_path, rebuilt_jar)
    if not jar_result.success:
        jr["rebuild_status"] = "FAILED_JAR"
        jr["errors"].append(f"JAR repack failed: {jar_result.error}")
        print(f"[legend_mtcr] JAR repack FAILED: {jar_name}")
        return jr

    # Restore to exact original filename and path
    print(f"[legend_mtcr] Restoring {jar_name} -> {project_jar}")
    restore_result = restore_rebuilt_jar_no_backup(rebuilt_jar, project_jar)
    if not restore_result.success:
        jr["restore_status"] = "FAILED"
        jr["errors"].append(f"Restore failed: {restore_result.error}")
        print(f"[legend_mtcr] Restore FAILED: {jar_name}")
        return jr

    jr["restore_status"]   = "OK"
    jr["restored_filename"] = jar_name
    jr["restored_path"]     = str(project_jar)
    jr["final_status"]      = "APPLIED"
    print(f"[legend_mtcr] APPLIED: {jar_name} -> {project_jar.name}")
    return jr


# ── Report formatting ─────────────────────────────────────────────────────────

def _format_text_report(report: dict) -> str:
    mode  = "DRY RUN" if report.get("dry_run") else "EXECUTE"
    lines: list[str] = [
        f"DeadZone Legend MTCR Patch Report  [{mode}]",
        "=" * 72,
        f"Final status  : {report.get('final_status', '?')}",
        f"Flavor        : {report.get('flavor', '?')}",
        f"Dry run       : {report.get('dry_run', True)}",
        f"Project dir   : {report.get('project_dir', '?')}",
        f"Work dir      : {report.get('work_dir', '?')}",
        "",
        "JAR results:",
    ]

    for jar_name, jr in report.get("jars", {}).items():
        lines.append(f"\n  JAR: {jar_name}")
        lines.append(f"    found          : {jr.get('found', False)}")
        lines.append(f"    original path  : {jr.get('project_jar_path', '(not found)')}")
        lines.append(f"    unpack         : {jr.get('unpack_status', 'N/A')}")
        lines.append(f"    rebuild        : {jr.get('rebuild_status', 'N/A')}")
        lines.append(f"    restore        : {jr.get('restore_status', 'N/A')}")
        lines.append(f"    restored path  : {jr.get('restored_path', '?')}")
        lines.append(f"    final          : {jr.get('final_status', '?')}")

        for e in jr.get("errors", []):
            lines.append(f"    ! ERROR: {e}")

        dex_results = jr.get("dex_add_results", [])
        if dex_results:
            lines.append("    DEX additions:")
            for dr in dex_results:
                lines.append(
                    f"      [{dr['status']:30s}] {dr['patch_id']}  "
                    f"payload={dr['payload_name']} -> {dr['output_dex']}"
                )

        class_results = jr.get("class_results", [])
        if class_results:
            lines.append(f"    Classes patched ({len(class_results)}):")
            for cr in class_results:
                lines.append(f"      CLASS : {cr['class']}")
                lines.append(f"        jar    : {cr['jar']}")
                lines.append(f"        status : {cr['status']}")
                for pr in cr.get("patch_results", []):
                    cm = pr.get("class_match",    "")
                    mm = pr.get("method_match",   "")
                    cs = pr.get("class_strategy", "")
                    ms = pr.get("method_strategy","")
                    lines.append(
                        f"        PATCH [{pr['status']:20s}]  "
                        f"CLASS={cm:10s}  METHOD={mm:12s}  "
                        f"{pr['type']:16s}  {pr['method'][:50]}"
                    )
                    if cs:
                        lines.append(f"          class  via: {cs}")
                    if ms:
                        lines.append(f"          method via: {ms}")
                    if pr.get("message"):
                        lines.append(f"          msg: {pr['message']}")
                for ce in cr.get("errors", []):
                    lines.append(f"        ! {ce}")

        mod_results = jr.get("mod_results", {})
        if mod_results:
            lines.append(f"    Config-gated mods ({len(mod_results)}):")
            for mod_id, mr in mod_results.items():
                st = mr.get("status", "?")
                lines.append(f"      [{st:30s}]  {mod_id}")
                if "patched_classes" in mr:
                    for cls in mr.get("patched_classes", []):
                        lines.append(f"        patched : {cls}")
                if "skipped_missing" in mr:
                    for cls in mr.get("skipped_missing", []):
                        lines.append(f"        missing : {cls}")
                if "invoke_custom_files_found" in mr:
                    lines.append(f"        invoke_custom_found   : {mr['invoke_custom_files_found']}")
                    lines.append(f"        invoke_custom_patched : {mr['invoke_custom_files_patched']}")
                if "files_patched" in mr:
                    for f in mr.get("files_patched", []):
                        lines.append(f"        replaced : {f}")
                    lines.append(f"        occurrences : {mr.get('occurrences_replaced', 0)}")
                if "freeform_max_count" in mr:
                    lines.append(f"        freeform_max_count : {mr['freeform_max_count']}")
                for e in mr.get("errors", []):
                    lines.append(f"        ! {e}")
                for w in mr.get("warnings", []):
                    lines.append(f"        ~ {w}")

    mods = report.get("legend_jar_mods", {})
    if mods:
        lines.append("\nlegend_jar_mods (effective config):")
        _REPORT_KEYS = (
            "mezo_core",
            "volume_button_music_control",
            "gboard_replace_baidu",
            "multi_floating_window",
            "freeform_max_count",
            "invoke_custom_handling",
            "kaorios_toolbox_v203",
            "signature_verification_bypass",
            "process_control",
            "greeze_policy",
            "shortcut_settings_observer",
        )
        for k in _REPORT_KEYS:
            if k in mods:
                lines.append(f"  {k}: {mods[k]}")

    warnings = report.get("warnings", [])
    lines.append("\nWarnings:")
    lines.extend(f"  ~ {w}" for w in warnings) if warnings else lines.append("  (none)")

    errors = report.get("errors", [])
    lines.append("\nErrors:")
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


# ── Public API ────────────────────────────────────────────────────────────────

def apply_legend_mtcr_patches(
    project_dir: Path,
    flavor: str,
    execute: bool = False,
    android_major: int | None = None,
    legend_jar_mods: dict | None = None,
) -> dict:
    """
    Apply (or dry-run) all Legend MTCR JAR patches at class/method level.

    No MTCR binary files are read at runtime.  No Legend/ directory required
    for class-level patches (Kaorios DEX must be placed manually when enabled).

    Parameters
    ----------
    project_dir     : Path   Root of unpacked ROM project.
    flavor          : str    ROM flavor: "legend" | "deadzone_legend" | other.
    execute         : bool   True → apply; False (default) → dry-run.
    android_major   : int    Android major version (14, 15, 16, …).
    legend_jar_mods : dict   Mod-group enable/disable overrides applied on top
                             of LEGEND_MINIMAL_REAL_PROFILE.  Key examples:
                               signature_verification_bypass (default False)
                               gboard_replace_baidu          (default True)
                               multi_floating_window         (default True)
                               freeform_max_count            (default 50)
                               invoke_custom_handling        (default True)
                               kaorios_toolbox_v203          (default False)

    Returns
    -------
    dict  Report with final_status and per-JAR/per-class/per-method detail.
    """
    project_dir = Path(project_dir).resolve()
    ts          = time.strftime("%Y%m%d_%H%M%S")
    work_dir    = _OUTPUT_ROOT / "work" / f"legend_mtcr_{ts}"
    add_dex_dir = _add_dex_dir()
    mods_config = merge_profile(legend_jar_mods)
    if android_major is not None:
        mods_config["android_major"] = android_major

    report: dict = {
        "stage":           "legend_mtcr",
        "flavor":          flavor,
        "dry_run":         not execute,
        "android_major":   android_major,
        "project_dir":     str(project_dir),
        "work_dir":        str(work_dir),
        "add_dex_dir":     str(add_dex_dir),
        "backup_policy":   "disabled",
        "legend_jar_mods": mods_config,
        "jars":            {},
        "warnings":        [],
        "errors":          [],
        "final_status":    "DRY_RUN",
        "report_files":    {},
    }

    # Flavor guard
    norm_flavor = flavor.strip().lower().replace("-", "_")
    if norm_flavor not in _LEGEND_FLAVORS:
        report["final_status"] = "SKIPPED_NON_LEGEND"
        print(f"[legend_mtcr] Flavor '{flavor}' is not Legend → SKIPPED_NON_LEGEND")
        _write_reports(report)
        return report

    mode = "EXECUTE" if execute else "DRY-RUN"
    print(f"[legend_mtcr] === Legend MTCR Patch Runner ({mode}) ===")
    print(f"[legend_mtcr] Project  : {project_dir}")
    print(f"[legend_mtcr] Work dir : {work_dir}")
    print(f"[legend_mtcr] Add-DEX  : {add_dex_dir}")

    if execute:
        work_dir.mkdir(parents=True, exist_ok=True)

    any_failed = False

    for jar_cfg in _JARS:
        print(f"[legend_mtcr] --- Processing {jar_cfg['jar_name']} ---")
        jr = _patch_one_jar(
            jar_cfg=jar_cfg,
            project_dir=project_dir,
            work_dir=work_dir,
            add_dex_search=add_dex_dir,
            execute=execute,
            mods_config=mods_config,
        )
        report["jars"][jar_cfg["jar_name"]] = jr

        if execute and jr.get("final_status") not in ("APPLIED", "SKIPPED_MISSING"):
            any_failed = True
            report["errors"].extend(jr.get("errors", []))
        else:
            report["warnings"].extend(jr.get("warnings", []))

    if execute:
        report["final_status"] = "FAILED" if any_failed else "APPLIED"
    else:
        report["final_status"] = "DRY_RUN"

    print(f"[legend_mtcr] final_status={report['final_status']}")
    _write_reports(report)
    return report


# ── CLI ───────────────────────────────────────────────────────────────────────

def _main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Legend MTCR class/method-level patch runner")
    p.add_argument("--project",       required=True,
                   help="Path to unpacked ROM project directory")
    p.add_argument("--flavor",        required=True,
                   help="ROM flavor: legend | deadzone_legend | …")
    p.add_argument("--android-major", dest="android_major", type=int, default=None,
                   help="Android major version (14, 15, 16, …)")
    p.add_argument("--execute",       action="store_true",
                   help="Apply patches (default: dry-run)")
    p.add_argument("--enable-sig-bypass",     action="store_true", default=None,
                   help="Enable signature_verification_bypass mod (default: off)")
    p.add_argument("--enable-kaorios",        action="store_true", default=None,
                   help="Enable kaorios_toolbox_v203 mod (default: off)")
    p.add_argument("--disable-gboard",        action="store_true", default=None,
                   help="Disable gboard_replace_baidu mod (default: on)")
    p.add_argument("--disable-freeform",      action="store_true", default=None,
                   help="Disable multi_floating_window mod (default: on)")
    p.add_argument("--freeform-count",        dest="freeform_count", type=int, default=None,
                   help="Max freeform window count (default: 50)")
    p.add_argument("--disable-invoke-custom", action="store_true", default=None,
                   help="Disable invoke_custom_handling mod (default: on)")
    args = p.parse_args(argv)

    project_dir = Path(args.project).resolve()
    if not project_dir.is_dir():
        print(f"[legend_mtcr] ERROR: project directory not found: {project_dir}", file=sys.stderr)
        return 2

    mods_override: dict = {}
    if args.enable_sig_bypass:
        mods_override["signature_verification_bypass"] = True
    if args.enable_kaorios:
        mods_override["kaorios_toolbox_v203"] = True
    if args.disable_gboard:
        mods_override["gboard_replace_baidu"] = False
    if args.disable_freeform:
        mods_override["multi_floating_window"] = False
    if args.freeform_count is not None:
        mods_override["freeform_max_count"] = args.freeform_count
    if args.disable_invoke_custom:
        mods_override["invoke_custom_handling"] = False

    report = apply_legend_mtcr_patches(
        project_dir=project_dir,
        flavor=args.flavor,
        execute=args.execute,
        android_major=args.android_major,
        legend_jar_mods=mods_override if mods_override else None,
    )

    for w in report.get("warnings", []):
        print(f"[legend_mtcr] WARNING: {w}")
    for e in report.get("errors", []):
        print(f"[legend_mtcr] ERROR: {e}", file=sys.stderr)

    return 1 if report.get("errors") else 0


if __name__ == "__main__":
    sys.exit(_main())
