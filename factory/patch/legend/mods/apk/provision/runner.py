"""Legend Provision.apk patch runner."""
from __future__ import annotations

import importlib
import json
import pkgutil
import re
import shutil
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

from factory.patch.apk.apkeditor_tools import resolve_apkeditor_jar
from factory.patch.apk.apk_workspace import (
    copy_apk_to_work,
    decompile_apk,
    find_apk,
    prepare_apk_work_dir,
    rebuild_apk,
    restore_rebuilt_apk_no_backup,
)
from factory.patch.legend.mods.apk.provision.branding import apply_visible_branding
from factory.patch.legend.mods.apk.provision.model import load_class_patch
from factory.patch.legend.mods.apk.provision.policy import (
    MINIMAL_REAL_MODE,
    PROVISION_MINIMAL_REAL_ALLOWLIST,
    classify_provision_patch_skip,
)
from factory.patch.legend.smart_smali_patcher import (
    ClassMatchResult,
    ClassMatchStatus,
    MethodMatchStatus,
    PatchApplyStatus,
    apply_smart_patch,
    find_class,
    find_method,
    parse_smali_methods,
)

_REPO_ROOT = Path(__file__).resolve().parents[4]
_PKG_ROOT = Path(__file__).resolve().parent
_REPORTS_DIR = _REPO_ROOT / "output" / "reports"
_WORK_DIR_DEFAULT = _REPO_ROOT / "output" / "work" / "provision_legend_apk_work"
_LEGEND_FLAVORS = frozenset({"legend", "deadzone_legend"})

PROVISION_APK_NAME = "Provision.apk"
PROVISION_APK_SRC_DIR_NAME = "Provision_apk_src"


def _is_legend(flavor: str) -> bool:
    return flavor.strip().lower() in _LEGEND_FLAVORS


def _find_smali_roots(decompiled_dir: Path) -> list[Path]:
    return [p for p in sorted(decompiled_dir.iterdir()) if p.is_dir() and p.name.startswith("smali")]


def _load_smali_rules() -> list:
    result = []
    pkg = "factory.patch.legend.mods.apk.provision.smali"
    path = _PKG_ROOT / "smali"
    for _, name, ispkg in pkgutil.iter_modules([str(path)]):
        if ispkg or name == "__init__":
            continue
        mod = importlib.import_module(f"{pkg}.{name}")
        cp = load_class_patch(mod)
        if cp.target_class:
            result.append(cp)
    return result


def _load_list(module: str, attr: str) -> list[dict]:
    try:
        mod = importlib.import_module(module)
        return list(getattr(mod, attr, []))
    except Exception:
        return []


def _status_from_smart(status: PatchApplyStatus, message: str) -> str:
    if status == PatchApplyStatus.PATCHED:
        return "PATCHED"
    if status == PatchApplyStatus.WOULD_PATCH:
        return "WOULD_PATCH"
    if status == PatchApplyStatus.SKIPPED:
        return "SKIPPED_OPTIONAL"
    if "AMBIGUOUS" in message:
        return "FAILED_AMBIGUOUS"
    if status == PatchApplyStatus.FAILED:
        return "FAILED_NOT_FOUND"
    return status.value


def _apply_delete_rule(smali_roots: list[Path], rule: dict, dry_run: bool) -> dict:
    target_class = rule.get("target_class", "")
    found = find_class(
        smali_roots,
        target_class,
        rule.get("class_fallback_names", []),
        rule.get("class_anchors", []),
        rule.get("method_anchors", []),
    )
    if found.status == ClassMatchStatus.AMBIGUOUS:
        return {"id": rule["id"], "status": "FAILED_AMBIGUOUS", "message": found.strategy}

    # RELATIVE_PATH_MULTI: same relative path in multiple copies (e.g. across smali_classes* dirs).
    # For class_delete → delete ALL copies; never fail just because the basename is common.
    # For method_delete → fall through using the first copy (unusual case).
    if found.status == ClassMatchStatus.RELATIVE_PATH_MULTI:
        if rule["type"] == "class_delete":
            deleted = 0
            errors: list[str] = []
            if not dry_run:
                for cand in found.candidates:
                    try:
                        cand.unlink()
                        deleted += 1
                    except OSError as exc:
                        errors.append(str(exc))
            n = len(found.candidates)
            if errors:
                return {
                    "id": rule["id"],
                    "status": "FAILED_AMBIGUOUS",
                    "message": f"class_delete partial: {deleted}/{n} removed; errors: {errors}",
                }
            return {
                "id": rule["id"],
                "status": "WOULD_PATCH" if dry_run else "PATCHED",
                "message": f"class delete: {'would remove' if dry_run else 'removed'} {n} copies",
                "exact_path_match_count": n,
                "selected_class_path": str(found.candidates[0]),
            }
        # method_delete with multiple copies: use the first one
        found = ClassMatchResult(
            status=ClassMatchStatus.RELATIVE_PATH,
            path=found.candidates[0],
            strategy=found.strategy + " → first copy used for method_delete",
        )

    if found.status == ClassMatchStatus.NOT_FOUND or not found.path:
        return {"id": rule["id"], "status": "SKIPPED_OPTIONAL", "message": found.strategy}
    if rule["type"] == "class_delete":
        if not dry_run:
            found.path.unlink()
        return {
            "id": rule["id"],
            "status": "WOULD_PATCH" if dry_run else "PATCHED",
            "message": "class delete",
            "exact_path_match_count": 1,
            "selected_class_path": str(found.path),
        }
    text = found.path.read_text(encoding="utf-8", errors="replace")
    method = find_method(text, rule.get("method", ""), rule.get("method_name", ""), rule.get("method_anchors", []))
    if method.status == MethodMatchStatus.AMBIGUOUS:
        return {"id": rule["id"], "status": "FAILED_AMBIGUOUS", "message": method.strategy}
    if method.status == MethodMatchStatus.NOT_FOUND or not method.block:
        return {"id": rule["id"], "status": "FAILED_NOT_FOUND", "message": method.strategy}
    if not dry_run:
        new_text = text.replace(method.block, "", 1)
        found.path.write_text(new_text, encoding="utf-8")
    return {
        "id": rule["id"],
        "status": "WOULD_PATCH" if dry_run else "PATCHED",
        "message": "method delete",
        "exact_path_match_count": 1,
        "selected_class_path": str(found.path),
        "method_match": method.status.value,
    }


def _apply_smali_rules(decompiled_dir: Path, dry_run: bool) -> dict:
    roots = _find_smali_roots(decompiled_dir)
    results = []
    class_count = 0
    method_count = 0
    skipped_build_flag_ids: list[str] = []
    partial_build_flag_ids: list[str] = []

    # minimal_real mode skip buckets
    _minimal_skipped: dict[str, list[str]] = {
        "dex_mtcr_broad_rules_skipped": [],
        "skipped_elite_flag_rules": [],
        "skipped_library_rules": [],
        "skipped_onetrack_delete_rules": [],
    }
    minimal_real_applied: list[str] = []

    for cp in _load_smali_rules():
        class_count += 1
        for patch in cp.patches:
            # ── 1. Existing build-flag policy gate ──────────────────────────
            if patch.policy_status == "SKIPPED_BUILD_FLAG_POLICY" or patch.type == "policy_skip":
                skipped_build_flag_ids.append(patch.id)
                results.append({
                    "id": patch.id, "type": patch.type,
                    "target_class": cp.target_class,
                    "status": "SKIPPED_BUILD_FLAG_POLICY",
                })
                continue

            if patch.policy_status == "BUILD_FLAG_PARTIALLY_SKIPPED":
                partial_build_flag_ids.append(patch.id)

            # ── 2. minimal_real allowlist ───────────────────────────────────
            if MINIMAL_REAL_MODE and patch.id not in PROVISION_MINIMAL_REAL_ALLOWLIST:
                cat = classify_provision_patch_skip(
                    cp.target_class,
                    patch.id,
                    patch.search or "",
                    patch.reason or "",
                )
                _minimal_skipped[cat].append(patch.id)
                results.append({
                    "id": patch.id, "type": patch.type,
                    "target_class": cp.target_class,
                    "status": "SKIPPED_NOT_IN_ALLOWLIST",
                    "skip_reason": cat,
                })
                continue

            # ── 3. Apply ────────────────────────────────────────────────────
            rule = {
                "id": patch.id,
                "type": patch.type,
                "method": patch.method,
                "method_name": patch.method_name,
                "method_anchors": patch.method_anchors,
                "search": patch.search,
                "replacement": patch.replacement,
                "required": patch.required,
                "target_class": cp.target_class,
                "class_fallback_names": cp.class_fallback_names,
                "class_anchors": cp.class_anchors,
            }
            if patch.type in {"class_delete", "method_delete"}:
                item = _apply_delete_rule(roots, rule, dry_run)
                item.update({"type": patch.type, "target_class": cp.target_class})
                results.append(item)
            else:
                smart = apply_smart_patch(roots, rule, dry_run=dry_run)
                results.append({
                    "id": smart.patch_id,
                    "type": smart.type,
                    "target_class": cp.target_class,
                    "status": _status_from_smart(smart.status, smart.message),
                    "class_match": smart.class_match.value,
                    "method_match": smart.method_match.value,
                    "message": smart.message,
                })
            if patch.type.startswith("method_"):
                method_count += 1
            minimal_real_applied.append(patch.id)

    failures = [r for r in results if str(r.get("status", "")).startswith("FAILED")]
    return {
        "class_count": class_count,
        "method_patch_count": method_count,
        "results": results,
        "failures": failures,
        "skipped_build_flag_ids": skipped_build_flag_ids,
        "partial_build_flag_ids": partial_build_flag_ids,
        "dex_mtcr_broad_rules_skipped": _minimal_skipped["dex_mtcr_broad_rules_skipped"],
        "minimal_real_rules_applied": minimal_real_applied,
        "skipped_elite_flag_rules": _minimal_skipped["skipped_elite_flag_rules"],
        "skipped_library_rules": _minimal_skipped["skipped_library_rules"],
        "skipped_onetrack_delete_rules": _minimal_skipped["skipped_onetrack_delete_rules"],
    }


def _summarize_smali_rules() -> dict:
    class_count = 0
    method_count = 0
    skipped: list[str] = []
    partial: list[str] = []
    _minimal_skipped: dict[str, list[str]] = {
        "dex_mtcr_broad_rules_skipped": [],
        "skipped_elite_flag_rules": [],
        "skipped_library_rules": [],
        "skipped_onetrack_delete_rules": [],
    }
    minimal_real_applied: list[str] = []

    for cp in _load_smali_rules():
        class_count += 1
        for patch in cp.patches:
            if patch.policy_status == "SKIPPED_BUILD_FLAG_POLICY" or patch.type == "policy_skip":
                skipped.append(patch.id)
                continue
            if patch.policy_status == "BUILD_FLAG_PARTIALLY_SKIPPED":
                partial.append(patch.id)
            if MINIMAL_REAL_MODE and patch.id not in PROVISION_MINIMAL_REAL_ALLOWLIST:
                cat = classify_provision_patch_skip(
                    cp.target_class,
                    patch.id,
                    patch.search or "",
                    patch.reason or "",
                )
                _minimal_skipped[cat].append(patch.id)
                continue
            if patch.type.startswith("method_"):
                method_count += 1
            minimal_real_applied.append(patch.id)

    return {
        "class_count": class_count,
        "method_patch_count": method_count,
        "skipped_build_flag_ids": skipped,
        "partial_build_flag_ids": partial,
        "dex_mtcr_broad_rules_skipped": _minimal_skipped["dex_mtcr_broad_rules_skipped"],
        "minimal_real_rules_applied": minimal_real_applied,
        "skipped_elite_flag_rules": _minimal_skipped["skipped_elite_flag_rules"],
        "skipped_library_rules": _minimal_skipped["skipped_library_rules"],
        "skipped_onetrack_delete_rules": _minimal_skipped["skipped_onetrack_delete_rules"],
    }


def _safe_write_xml(path: Path, replacement: str, dry_run: bool) -> dict:
    try:
        ET.fromstring(replacement)
    except ET.ParseError as exc:
        return {"status": "FAILED_MANIFEST_PATCH", "error": str(exc)}
    if not dry_run:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(replacement, encoding="utf-8")
    return {"status": "WOULD_PATCH" if dry_run else "PATCHED"}


def _apply_xml_rules(decompiled_dir: Path, dry_run: bool) -> dict:
    rules = []
    rules.extend(_load_list("factory.patch.legend.mods.apk.provision.manifest.manifest_rules", "MANIFEST_RULES"))
    rules.extend(_load_list("factory.patch.legend.mods.apk.provision.manifest.xml_rules", "XML_RULES"))
    results = []
    for rule in rules:
        path = decompiled_dir / rule["target"]
        result = _safe_write_xml(path, rule["replacement"], dry_run)
        result.update({"id": rule["id"], "target": rule["target"]})
        results.append(result)
    return {"count": len(rules), "results": results, "failures": [r for r in results if str(r["status"]).startswith("FAILED")]}


def _apply_resource_rules(decompiled_dir: Path, dry_run: bool) -> dict:
    rules = []
    rules.extend(_load_list("factory.patch.legend.mods.apk.provision.resources.arsc_rules", "ARSC_RULES"))
    rules.extend(_load_list("factory.patch.legend.mods.apk.provision.resources.values_rules", "VALUES_RULES"))
    results = []
    for rule in rules:
        replacement = rule.get("replacement", "")
        if not replacement.lstrip().startswith("<?xml") and not replacement.lstrip().startswith("<resources"):
            if rule.get("required"):
                results.append({"id": rule["id"], "target": rule["target"], "status": "FAILED_RESOURCE_PATCH", "error": "non-XML resource group"})
            else:
                results.append({"id": rule["id"], "target": rule["target"], "status": "SKIPPED_OPTIONAL"})
            continue
        target = decompiled_dir / rule["target"]
        result = _safe_write_xml(target, replacement, dry_run)
        if result["status"].startswith("FAILED"):
            result["status"] = "FAILED_RESOURCE_PATCH"
        result.update({"id": rule["id"], "target": rule["target"]})
        results.append(result)
    return {"count": len(rules), "results": results, "failures": [r for r in results if str(r["status"]).startswith("FAILED")]}


def _apply_branding_rules(decompiled_dir: Path, dry_run: bool) -> dict:
    explicit = _load_list("factory.patch.legend.mods.apk.provision.resources.branding_string_rules", "BRANDING_STRING_RULES")
    changes = []
    review = []
    unsafe = []
    targets = {decompiled_dir / r["target"] for r in explicit}
    targets.update((decompiled_dir / "res").rglob("*.xml") if (decompiled_dir / "res").is_dir() else [])
    for path in sorted(targets):
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        new_text, file_changes, file_review = apply_visible_branding(text)
        for item in file_changes:
            item["target"] = str(path.relative_to(decompiled_dir))
        for item in file_review:
            item["target"] = str(path.relative_to(decompiled_dir))
        changes.extend(file_changes)
        review.extend(file_review)
        if new_text != text and not dry_run:
            path.write_text(new_text, encoding="utf-8")
    return {
        "count": sum(c.get("count", 1) for c in changes),
        "changes": changes,
        "unsafe": unsafe,
        "review": review,
        "failures": [],
    }


def _format_text_report(report: dict) -> str:
    lines = [
        "Legend Provision APK Patch Report",
        "=" * 60,
        f"Final status               : {report.get('final_status')}",
        f"Minimal-real mode          : {report.get('minimal_real_mode', MINIMAL_REAL_MODE)}",
        f"Original APK path          : {report.get('original_apk_path')}",
        f"Restored APK path          : {report.get('restored_apk_path')}",
        f"Final filename             : {report.get('final_filename')}",
        "",
        "Smali rule counts:",
        f"  minimal_real_rules_applied       : {report.get('minimal_real_rules_applied', 0)}",
        f"  dex_mtcr_broad_rules_skipped     : {report.get('dex_mtcr_broad_rules_skipped', 0)}",
        f"  skipped_elite_flag_rules         : {report.get('skipped_elite_flag_rules', 0)}",
        f"  skipped_library_rules            : {report.get('skipped_library_rules', 0)}",
        f"  skipped_onetrack_delete_rules    : {report.get('skipped_onetrack_delete_rules', 0)}",
        f"  skipped_build_flag_patch_count   : {report.get('skipped_build_flag_patch_count', 0)}",
        f"  smali_class_count                : {report.get('smali_class_count', 0)}",
        f"  smali_method_patch_count         : {report.get('smali_method_patch_count', 0)}",
        "",
        f"Manifest/XML patch count   : {report.get('manifest_xml_patch_count')}",
        f"ARSC/resource patch count  : {report.get('arsc_resource_patch_count')}",
        f"Branding changes count     : {report.get('branding_changes_count')}",
        "",
        "Failures:",
    ]
    failures = report.get("failure_list", [])
    lines.extend([f"  - {f}" for f in failures] or ["  (none)"])
    return "\n".join(lines) + "\n"


def _write_reports(report: dict) -> None:
    _REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    (_REPORTS_DIR / "legend_provision_report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False, default=str), encoding="utf-8")
    (_REPORTS_DIR / "legend_provision_report.txt").write_text(_format_text_report(report), encoding="utf-8")


def apply_legend_provision_patch(project_dir: Path, flavor: str, execute: bool = False, work_dir: Path | None = None) -> dict:
    effective_work_dir = work_dir or _WORK_DIR_DEFAULT
    report: dict[str, Any] = {
        "stage": "legend_provision",
        "flavor": flavor,
        "dry_run": not execute,
        "minimal_real_mode": MINIMAL_REAL_MODE,
        "project_dir": str(project_dir),
        "work_dir": str(effective_work_dir),
        "original_apk_path": "",
        "restored_apk_path": "",
        "final_filename": PROVISION_APK_NAME,
        "smali_class_count": 0,
        "smali_method_patch_count": 0,
        "manifest_xml_patch_count": 0,
        "arsc_resource_patch_count": 0,
        "branding_changes_count": 0,
        "skipped_build_flag_patch_count": 0,
        "skipped_build_flag_patch_ids": [],
        "partial_build_flag_skips": [],
        # minimal_real mode counters
        "dex_mtcr_broad_rules_skipped": 0,
        "minimal_real_rules_applied": 0,
        "skipped_elite_flag_rules": 0,
        "skipped_library_rules": 0,
        "skipped_onetrack_delete_rules": 0,
        "unsafe_branding_candidates_skipped": [],
        "review_required_branding_candidates": [],
        "failure_list": [],
        "final_status": "WOULD_PATCH" if not execute else "PATCHED",
    }
    static_smali = _summarize_smali_rules()
    static_xml_count = len(_load_list("factory.patch.legend.mods.apk.provision.manifest.manifest_rules", "MANIFEST_RULES")) + len(_load_list("factory.patch.legend.mods.apk.provision.manifest.xml_rules", "XML_RULES"))
    static_res_count = len(_load_list("factory.patch.legend.mods.apk.provision.resources.arsc_rules", "ARSC_RULES")) + len(_load_list("factory.patch.legend.mods.apk.provision.resources.values_rules", "VALUES_RULES"))
    report.update({
        "smali_class_count": static_smali["class_count"],
        "smali_method_patch_count": static_smali["method_patch_count"],
        "manifest_xml_patch_count": static_xml_count,
        "arsc_resource_patch_count": static_res_count,
        "skipped_build_flag_patch_count": len(static_smali["skipped_build_flag_ids"]),
        "skipped_build_flag_patch_ids": static_smali["skipped_build_flag_ids"],
        "partial_build_flag_skips": static_smali["partial_build_flag_ids"],
        "dex_mtcr_broad_rules_skipped": len(static_smali["dex_mtcr_broad_rules_skipped"]),
        "minimal_real_rules_applied": len(static_smali["minimal_real_rules_applied"]),
        "skipped_elite_flag_rules": len(static_smali["skipped_elite_flag_rules"]),
        "skipped_library_rules": len(static_smali["skipped_library_rules"]),
        "skipped_onetrack_delete_rules": len(static_smali["skipped_onetrack_delete_rules"]),
    })
    if not _is_legend(flavor):
        report["final_status"] = "SKIPPED_OPTIONAL"
        _write_reports(report)
        return report

    apkeditor_jar = resolve_apkeditor_jar()
    provision_apk = find_apk(project_dir, PROVISION_APK_NAME)
    if not provision_apk:
        report["final_status"] = "FAILED_NOT_FOUND"
        report["failure_list"].append("Provision.apk not found")
        _write_reports(report)
        return report
    report["original_apk_path"] = str(provision_apk)
    report["restored_apk_path"] = str(provision_apk)
    if not apkeditor_jar:
        report["final_status"] = "FAILED_NOT_FOUND"
        report["failure_list"].append("APKEditor.jar not found")
        _write_reports(report)
        return report

    if not execute:
        decompiled_dir = effective_work_dir / PROVISION_APK_SRC_DIR_NAME
        smali = _apply_smali_rules(decompiled_dir, dry_run=True) if decompiled_dir.is_dir() else static_smali
        xml = {"count": len(_load_list("factory.patch.legend.mods.apk.provision.manifest.manifest_rules", "MANIFEST_RULES")) + len(_load_list("factory.patch.legend.mods.apk.provision.manifest.xml_rules", "XML_RULES"))}
        res = {"count": len(_load_list("factory.patch.legend.mods.apk.provision.resources.arsc_rules", "ARSC_RULES")) + len(_load_list("factory.patch.legend.mods.apk.provision.resources.values_rules", "VALUES_RULES"))}
        report.update({
            "smali_class_count": smali["class_count"],
            "smali_method_patch_count": smali.get("method_patch_count", 0),
            "manifest_xml_patch_count": xml["count"],
            "arsc_resource_patch_count": res["count"],
            "skipped_build_flag_patch_count": len(smali.get("skipped_build_flag_ids", [])),
            "skipped_build_flag_patch_ids": smali.get("skipped_build_flag_ids", []),
            "partial_build_flag_skips": smali.get("partial_build_flag_ids", []),
            "dex_mtcr_broad_rules_skipped": len(smali.get("dex_mtcr_broad_rules_skipped", [])),
            "minimal_real_rules_applied": len(smali.get("minimal_real_rules_applied", [])),
            "skipped_elite_flag_rules": len(smali.get("skipped_elite_flag_rules", [])),
            "skipped_library_rules": len(smali.get("skipped_library_rules", [])),
            "skipped_onetrack_delete_rules": len(smali.get("skipped_onetrack_delete_rules", [])),
        })
        _write_reports(report)
        return report

    prepare_apk_work_dir(effective_work_dir, PROVISION_APK_NAME)
    work_apk = copy_apk_to_work(provision_apk, effective_work_dir)
    decompiled_dir = effective_work_dir / PROVISION_APK_SRC_DIR_NAME
    if not decompile_apk(apkeditor_jar, work_apk, decompiled_dir):
        report["final_status"] = "FAILED_NOT_FOUND"
        report["failure_list"].append("APK decompile failed")
        _write_reports(report)
        return report

    smali = _apply_smali_rules(decompiled_dir, dry_run=False)
    xml = _apply_xml_rules(decompiled_dir, dry_run=False)
    res = _apply_resource_rules(decompiled_dir, dry_run=False)
    branding = _apply_branding_rules(decompiled_dir, dry_run=False)
    failures = smali["failures"] + xml["failures"] + res["failures"] + branding["failures"]
    report.update({
        "smali_class_count": smali["class_count"],
        "smali_method_patch_count": smali["method_patch_count"],
        "manifest_xml_patch_count": xml["count"],
        "arsc_resource_patch_count": res["count"],
        "branding_changes_count": branding["count"],
        "skipped_build_flag_patch_count": len(smali["skipped_build_flag_ids"]),
        "skipped_build_flag_patch_ids": smali["skipped_build_flag_ids"],
        "partial_build_flag_skips": smali["partial_build_flag_ids"],
        "dex_mtcr_broad_rules_skipped": len(smali["dex_mtcr_broad_rules_skipped"]),
        "minimal_real_rules_applied": len(smali["minimal_real_rules_applied"]),
        "skipped_elite_flag_rules": len(smali["skipped_elite_flag_rules"]),
        "skipped_library_rules": len(smali["skipped_library_rules"]),
        "skipped_onetrack_delete_rules": len(smali["skipped_onetrack_delete_rules"]),
        "unsafe_branding_candidates_skipped": branding["unsafe"],
        "review_required_branding_candidates": branding["review"],
        "failure_list": failures,
    })
    if failures:
        report["final_status"] = "FAILED_NOT_FOUND"
        _write_reports(report)
        return report
    if not rebuild_apk(apkeditor_jar, decompiled_dir):
        report["final_status"] = "FAILED_REBUILD"
        report["failure_list"].append("APK rebuild failed")
        _write_reports(report)
        return report
    shutil.rmtree(decompiled_dir, ignore_errors=True)
    replace_result = restore_rebuilt_apk_no_backup(effective_work_dir / PROVISION_APK_NAME, provision_apk)
    if not replace_result.get("success"):
        report["final_status"] = "FAILED_REBUILD"
        report["failure_list"].append(replace_result.get("error", "restore failed"))
    _write_reports(report)
    return report


def _main(argv: list[str] | None = None) -> int:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    parser.add_argument("--flavor", required=True)
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--work-dir", default=None)
    args = parser.parse_args(argv)
    report = apply_legend_provision_patch(
        Path(args.project).resolve(),
        args.flavor,
        execute=args.execute,
        work_dir=Path(args.work_dir).resolve() if args.work_dir else None,
    )
    print(f"[legend_provision] final_status={report['final_status']}")
    return 0 if not str(report["final_status"]).startswith("FAILED") else 1


if __name__ == "__main__":
    sys.exit(_main())
