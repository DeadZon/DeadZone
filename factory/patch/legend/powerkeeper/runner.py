"""Legend PowerKeeper APK patch runner."""
from __future__ import annotations

import importlib
import json
import pkgutil
import shutil
import sys
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
from factory.patch.legend.powerkeeper.policy import POWERKEEPER_ALLOWED_FLAG_REWRITES
from factory.patch.legend.powerkeeper.model import load_class_patch
from factory.patch.legend.smart_smali_patcher import (
    ClassMatchStatus,
    MethodMatchStatus,
    PatchApplyStatus,
    apply_smart_patch,
    find_class,
    find_method,
)

_REPO_ROOT = Path(__file__).resolve().parents[4]
_PKG_ROOT = Path(__file__).resolve().parent
_REPORTS_DIR = _REPO_ROOT / "output" / "reports"
_WORK_DIR_DEFAULT = _REPO_ROOT / "output" / "work" / "powerkeeper_legend_apk_work"
_LEGEND_FLAVORS = frozenset({"legend", "deadzone_legend"})

POWERKEEPER_APK_NAME = "PowerKeeper.apk"
POWERKEEPER_APK_SRC_DIR_NAME = "PowerKeeper_apk_src"


def _is_legend(flavor: str) -> bool:
    return flavor.strip().lower().replace("-", "_") in _LEGEND_FLAVORS


def _resolve_partition_root(project_dir: Path, partition: str) -> Path | None:
    direct = project_dir / partition
    nested = direct / partition
    if nested.is_dir():
        return nested
    if direct.is_dir():
        return direct
    return None


def _find_powerkeeper_apk(project_dir: Path) -> Path | None:
    for partition in ("system_ext", "system", "product"):
        root = _resolve_partition_root(project_dir, partition)
        if root is None:
            continue
        candidate = root / "priv-app" / "PowerKeeper" / POWERKEEPER_APK_NAME
        if candidate.is_file():
            return candidate
    return find_apk(project_dir, POWERKEEPER_APK_NAME)


def _find_smali_roots(decompiled_dir: Path) -> list[Path]:
    return [p for p in sorted(decompiled_dir.iterdir()) if p.is_dir() and p.name.startswith("smali")]


def _load_smali_rules() -> list:
    result = []
    package = "factory.patch.legend.powerkeeper.smali"
    path = _PKG_ROOT / "smali"
    if not path.is_dir():
        return result
    for _, name, ispkg in pkgutil.iter_modules([str(path)]):
        if ispkg or name == "__init__":
            continue
        module = importlib.import_module(f"{package}.{name}")
        class_patch = load_class_patch(module)
        if class_patch.target_class:
            result.append(class_patch)
    return result


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
    found = find_class(
        smali_roots,
        rule.get("target_class", ""),
        rule.get("class_fallback_names", []),
        rule.get("class_anchors", []),
        rule.get("method_anchors", []),
    )
    if found.status == ClassMatchStatus.AMBIGUOUS:
        return {"id": rule["id"], "status": "FAILED_AMBIGUOUS", "message": found.strategy}
    if found.status == ClassMatchStatus.NOT_FOUND or not found.path:
        status = "FAILED_NOT_FOUND" if rule.get("required", True) else "SKIPPED_OPTIONAL"
        return {"id": rule["id"], "status": status, "message": found.strategy}
    if rule["type"] == "class_delete":
        if not dry_run:
            found.path.unlink()
        return {"id": rule["id"], "status": "WOULD_PATCH" if dry_run else "PATCHED", "message": "class delete"}

    text = found.path.read_text(encoding="utf-8", errors="replace")
    method = find_method(text, rule.get("method", ""), rule.get("method_name", ""), rule.get("method_anchors", []))
    if method.status == MethodMatchStatus.AMBIGUOUS:
        return {"id": rule["id"], "status": "FAILED_AMBIGUOUS", "message": method.strategy}
    if method.status == MethodMatchStatus.NOT_FOUND or not method.block:
        return {"id": rule["id"], "status": "FAILED_NOT_FOUND", "message": method.strategy}
    if not dry_run:
        found.path.write_text(text.replace(method.block, "", 1), encoding="utf-8")
    return {"id": rule["id"], "status": "WOULD_PATCH" if dry_run else "PATCHED", "message": "method delete"}


def _apply_smali_rules(decompiled_dir: Path, dry_run: bool) -> dict:
    roots = _find_smali_roots(decompiled_dir)
    results = []
    class_count = 0
    method_count = 0
    flag_rewrite_count = 0
    lock_status = "FAILED_NOT_FOUND"
    gms_status = "FAILED_NOT_FOUND"

    for class_patch in _load_smali_rules():
        class_count += 1
        for patch in class_patch.patches:
            if patch.type.startswith("method_"):
                method_count += 1
            flag_rewrite_count += patch.flag_rewrite_count
            rule = {
                "id": patch.id,
                "type": patch.type,
                "method": patch.method,
                "method_name": patch.method_name,
                "method_anchors": patch.method_anchors,
                "search": patch.search,
                "replacement": patch.replacement,
                "required": patch.required,
                "target_class": class_patch.target_class,
                "class_fallback_names": class_patch.class_fallback_names,
                "class_anchors": class_patch.class_anchors,
            }
            if patch.type in {"class_delete", "method_delete"}:
                item = _apply_delete_rule(roots, rule, dry_run)
                item.update({"type": patch.type, "target_class": class_patch.target_class})
            else:
                smart = apply_smart_patch(roots, rule, dry_run=dry_run)
                item = {
                    "id": smart.patch_id,
                    "type": smart.type,
                    "target_class": class_patch.target_class,
                    "status": _status_from_smart(smart.status, smart.message),
                    "class_match": smart.class_match.value,
                    "method_match": smart.method_match.value,
                    "message": smart.message,
                }
            item["flag_rewrite_count"] = patch.flag_rewrite_count
            results.append(item)
            if class_patch.target_class.endswith("DisplayFrameSetting.smali") and patch.method_name == "setScreenEffect":
                lock_status = item["status"]
            if class_patch.target_class.endswith("GmsObserver.smali") and patch.method_name == "isGmsControlEnabled":
                gms_status = item["status"]

    failures = [r for r in results if str(r.get("status", "")).startswith("FAILED")]
    return {
        "class_count": class_count,
        "method_patch_count": method_count,
        "flag_rewrite_patch_count": flag_rewrite_count,
        "lock_max_fps_mezo_patch_status": lock_status,
        "gms_observer_force_false_patch_status": gms_status,
        "results": results,
        "failures": failures,
    }


def _summarize_smali_rules() -> dict:
    class_count = 0
    method_count = 0
    flag_rewrite_count = 0
    lock_status = "WOULD_PATCH"
    gms_status = "WOULD_PATCH"
    results = []
    for class_patch in _load_smali_rules():
        class_count += 1
        for patch in class_patch.patches:
            if patch.type.startswith("method_"):
                method_count += 1
            flag_rewrite_count += patch.flag_rewrite_count
            item = {
                "id": patch.id,
                "type": patch.type,
                "target_class": class_patch.target_class,
                "status": "WOULD_PATCH",
                "flag_rewrite_count": patch.flag_rewrite_count,
            }
            results.append(item)
            if class_patch.target_class.endswith("DisplayFrameSetting.smali") and patch.method_name == "setScreenEffect":
                lock_status = item["status"]
            if class_patch.target_class.endswith("GmsObserver.smali") and patch.method_name == "isGmsControlEnabled":
                gms_status = item["status"]
    return {
        "class_count": class_count,
        "method_patch_count": method_count,
        "flag_rewrite_patch_count": flag_rewrite_count,
        "lock_max_fps_mezo_patch_status": lock_status,
        "gms_observer_force_false_patch_status": gms_status,
        "results": results,
        "failures": [],
    }


def _format_text_report(report: dict) -> str:
    lines = [
        "Legend PowerKeeper Patch Report",
        "================================",
        f"Status: {report.get('final_status')}",
        f"Dry run: {report.get('dry_run')}",
        f"Original APK path: {report.get('original_apk_path')}",
        f"Restored APK path: {report.get('restored_apk_path')}",
        f"Final filename: {report.get('final_filename')}",
        f"Changed class count: {report.get('changed_class_count')}",
        f"Method patch count: {report.get('method_patch_count')}",
        f"Flag rewrite patch count: {report.get('flag_rewrite_patch_count')}",
        f"lock_max_fps_mezo patch status: {report.get('lock_max_fps_mezo_patch_status')}",
        f"GmsObserver force false patch status: {report.get('gms_observer_force_false_patch_status')}",
        "",
        "Patch statuses:",
    ]
    for item in report.get("patch_statuses", []):
        lines.append(f"  - {item.get('id')}: {item.get('status')} ({item.get('target_class')})")
    lines.extend(["", "Failures:"])
    failures = report.get("failures", [])
    lines.extend([f"  - {failure}" for failure in failures] or ["  (none)"])
    return "\n".join(lines) + "\n"


def _write_reports(report: dict) -> None:
    _REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    json_path = _REPORTS_DIR / "legend_powerkeeper_report.json"
    txt_path = _REPORTS_DIR / "legend_powerkeeper_report.txt"
    report["report_files"] = {"json": str(json_path), "txt": str(txt_path)}
    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False, default=str), encoding="utf-8")
    txt_path.write_text(_format_text_report(report), encoding="utf-8")


def apply_legend_powerkeeper_patch(
    project_dir: Path,
    flavor: str,
    execute: bool = False,
    work_dir: Path | None = None,
) -> dict:
    effective_work_dir = work_dir or _WORK_DIR_DEFAULT
    static_smali = _summarize_smali_rules()
    report: dict[str, Any] = {
        "stage": "legend_powerkeeper",
        "flavor": flavor,
        "dry_run": not execute,
        "project_dir": str(project_dir),
        "work_dir": str(effective_work_dir),
        "original_apk_path": "",
        "restored_apk_path": "",
        "final_filename": POWERKEEPER_APK_NAME,
        "changed_class_count": static_smali["class_count"],
        "method_patch_count": static_smali["method_patch_count"],
        "flag_rewrite_patch_count": static_smali["flag_rewrite_patch_count"],
        "build_flag_rewrite_rules": POWERKEEPER_ALLOWED_FLAG_REWRITES,
        "lock_max_fps_mezo_patch_status": static_smali["lock_max_fps_mezo_patch_status"],
        "gms_observer_force_false_patch_status": static_smali["gms_observer_force_false_patch_status"],
        "patch_statuses": static_smali["results"],
        "failures": [],
        "warnings": [],
        "errors": [],
        "final_status": "WOULD_PATCH" if not execute else "PATCHED",
    }
    if not _is_legend(flavor):
        report["final_status"] = "SKIPPED_OPTIONAL"
        _write_reports(report)
        return report

    powerkeeper_apk = _find_powerkeeper_apk(project_dir)
    if not powerkeeper_apk:
        report["final_status"] = "FAILED_NOT_FOUND"
        report["failures"].append("PowerKeeper.apk not found")
        report["errors"].append("PowerKeeper.apk not found")
        _write_reports(report)
        return report
    report["original_apk_path"] = str(powerkeeper_apk)
    report["restored_apk_path"] = str(powerkeeper_apk)

    apkeditor_jar = resolve_apkeditor_jar()
    if not apkeditor_jar:
        report["final_status"] = "FAILED_NOT_FOUND"
        report["failures"].append("APKEditor.jar not found")
        report["errors"].append("APKEditor.jar not found")
        _write_reports(report)
        return report

    if not execute:
        _write_reports(report)
        return report

    prepare_apk_work_dir(effective_work_dir, POWERKEEPER_APK_NAME)
    work_apk = copy_apk_to_work(powerkeeper_apk, effective_work_dir)
    decompiled_dir = effective_work_dir / POWERKEEPER_APK_SRC_DIR_NAME
    if not decompile_apk(apkeditor_jar, work_apk, decompiled_dir):
        report["final_status"] = "FAILED_NOT_FOUND"
        report["failures"].append("APK decompile failed")
        report["errors"].append("APK decompile failed")
        _write_reports(report)
        return report

    smali = _apply_smali_rules(decompiled_dir, dry_run=False)
    report.update({
        "changed_class_count": smali["class_count"],
        "method_patch_count": smali["method_patch_count"],
        "flag_rewrite_patch_count": smali["flag_rewrite_patch_count"],
        "lock_max_fps_mezo_patch_status": smali["lock_max_fps_mezo_patch_status"],
        "gms_observer_force_false_patch_status": smali["gms_observer_force_false_patch_status"],
        "patch_statuses": smali["results"],
        "failures": smali["failures"],
    })
    if smali["failures"]:
        report["final_status"] = "FAILED_NOT_FOUND"
        report["errors"].append(f"{len(smali['failures'])} required PowerKeeper smali patches failed")
        _write_reports(report)
        return report

    if not rebuild_apk(apkeditor_jar, decompiled_dir):
        report["final_status"] = "FAILED_REBUILD"
        report["failures"].append("APK rebuild failed")
        report["errors"].append("APK rebuild failed")
        _write_reports(report)
        return report
    shutil.rmtree(decompiled_dir, ignore_errors=True)

    rebuilt = effective_work_dir / POWERKEEPER_APK_NAME
    restore = restore_rebuilt_apk_no_backup(rebuilt, powerkeeper_apk)
    if not restore.get("success"):
        report["final_status"] = "FAILED_REBUILD"
        report["failures"].append(restore.get("error", "restore failed"))
        report["errors"].append(restore.get("error", "restore failed"))
        _write_reports(report)
        return report

    report["restored_apk_path"] = str(powerkeeper_apk)
    report["final_filename"] = POWERKEEPER_APK_NAME
    report["final_status"] = "PATCHED"
    _write_reports(report)
    return report


def _main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Legend PowerKeeper APK patch runner")
    parser.add_argument("--project", required=True)
    parser.add_argument("--flavor", required=True)
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--work-dir", default=None)
    args = parser.parse_args(argv)
    report = apply_legend_powerkeeper_patch(
        Path(args.project).resolve(),
        args.flavor,
        execute=args.execute,
        work_dir=Path(args.work_dir).resolve() if args.work_dir else None,
    )
    print(f"[legend_powerkeeper] final_status={report['final_status']}")
    return 0 if not str(report["final_status"]).startswith("FAILED") else 1


if __name__ == "__main__":
    sys.exit(_main())
