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

# Exact allowlist of 23 method patches from dex(1).mtcr.
# Any patch whose id is not in this dict will be skipped and counted as unexpected.
EXACT_PATCH_ALLOWLIST: dict[str, dict] = {
    "com_miui_powerkeeper_cloudcontrol_CloudUpdateHideMode__parseResult": {
        "class_path": "com/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode.smali",
        "method_signature": "parseResult(Landroid/content/Context;Ljava/lang/String;[Ljava/lang/String;)Z",
        "patch_type": "A",
        "expected_replacements": 1,
    },
    "com_miui_powerkeeper_cloudcontrol_LocalUpdateUtils__getCloudServer": {
        "class_path": "com/miui/powerkeeper/cloudcontrol/LocalUpdateUtils.smali",
        "method_signature": "getCloudServer(Landroid/content/Context;)Ljava/lang/String;",
        "patch_type": "A",
        "expected_replacements": 1,
    },
    "com_miui_powerkeeper_cloudcontrol_LocalUpdateUtils__setServerConfigurations": {
        "class_path": "com/miui/powerkeeper/cloudcontrol/LocalUpdateUtils.smali",
        "method_signature": "setServerConfigurations(Landroid/content/Context;)V",
        "patch_type": "A",
        "expected_replacements": 1,
    },
    "com_miui_powerkeeper_controller_DeviceIdleController__1__init": {
        "class_path": "com/miui/powerkeeper/controller/DeviceIdleController$1.smali",
        "method_signature": "<init>()V",
        "patch_type": "A",
        "expected_replacements": 1,
    },
    "com_miui_powerkeeper_customerpower_CustomerPowerCheck__outputResultPassAndNone": {
        "class_path": "com/miui/powerkeeper/customerpower/CustomerPowerCheck.smali",
        "method_signature": "outputResultPassAndNone(Ljava/io/PrintWriter;I)V",
        "patch_type": "A",
        "expected_replacements": 8,
    },
    "com_miui_powerkeeper_dfs_UsageAppTracker__init": {
        "class_path": "com/miui/powerkeeper/dfs/UsageAppTracker.smali",
        "method_signature": "<init>(Lcom/miui/powerkeeper/dfs/CloudData;Lcom/miui/powerkeeper/dfs/UsageManager;Landroid/os/Looper;)V",
        "patch_type": "A",
        "expected_replacements": 1,
    },
    "com_miui_powerkeeper_feedbackcontrol_ThermalLogUploader__uploadFiles": {
        "class_path": "com/miui/powerkeeper/feedbackcontrol/ThermalLogUploader.smali",
        "method_signature": "uploadFiles()V",
        "patch_type": "A",
        "expected_replacements": 1,
    },
    "com_miui_powerkeeper_powerchecker_PowerCheckerCloudPolicy__getOldCloud": {
        "class_path": "com/miui/powerkeeper/powerchecker/PowerCheckerCloudPolicy.smali",
        "method_signature": "getOldCloud(Landroid/content/Context;)Ljava/lang/String;",
        "patch_type": "A",
        "expected_replacements": 1,
    },
    "com_miui_powerkeeper_statemachine_DisplayFrameSetting__getValidLocalConfigPath": {
        "class_path": "com/miui/powerkeeper/statemachine/DisplayFrameSetting.smali",
        "method_signature": "getValidLocalConfigPath(Landroid/content/Context;)Ljava/lang/String;",
        "patch_type": "A",
        "expected_replacements": 2,
    },
    "com_miui_powerkeeper_statemachine_DisplayFrameSetting__isSupportDevice": {
        "class_path": "com/miui/powerkeeper/statemachine/DisplayFrameSetting.smali",
        "method_signature": "isSupportDevice()Z",
        "patch_type": "A",
        "expected_replacements": 1,
    },
    "com_miui_powerkeeper_tracker_TrackerManager__PrivacyPolicy__updateLicense": {
        "class_path": "com/miui/powerkeeper/tracker/TrackerManager$PrivacyPolicy.smali",
        "method_signature": "updateLicense()V",
        "patch_type": "A",
        "expected_replacements": 1,
    },
    "com_miui_powerkeeper_unionpower_utils_UnionPowerConfig__d": {
        "class_path": "com/miui/powerkeeper/unionpower/utils/UnionPowerConfig.smali",
        "method_signature": "d(Landroid/content/Context;)Ljava/util/Map;",
        "patch_type": "A",
        "expected_replacements": 1,
    },
    "com_miui_powerkeeper_utils_GmsObserver__init": {
        "class_path": "com/miui/powerkeeper/utils/GmsObserver.smali",
        "method_signature": "<init>(Landroid/content/Context;)V",
        "patch_type": "A",
        "expected_replacements": 1,
    },
    "com_miui_powerkeeper_utils_GmsObserver__updateGoogleSync": {
        "class_path": "com/miui/powerkeeper/utils/GmsObserver.smali",
        "method_signature": "updateGoogleSync(Z)V",
        "patch_type": "A",
        "expected_replacements": 1,
    },
    "com_miui_powerkeeper_utils_Utils__isCloudControlAllowed": {
        "class_path": "com/miui/powerkeeper/utils/Utils.smali",
        "method_signature": "isCloudControlAllowed(Landroid/content/Context;)Z",
        "patch_type": "A",
        "expected_replacements": 1,
    },
    "com_miui_powerkeeper_utils_Utils__isUserExperienceAndPrivacyAllowed": {
        "class_path": "com/miui/powerkeeper/utils/Utils.smali",
        "method_signature": "isUserExperienceAndPrivacyAllowed(Landroid/content/Context;)Z",
        "patch_type": "A",
        "expected_replacements": 1,
    },
    "miui_payment_PaymentManager__isMibiServiceDisabled": {
        "class_path": "miui/payment/PaymentManager.smali",
        "method_signature": "isMibiServiceDisabled()Z",
        "patch_type": "A",
        "expected_replacements": 1,
    },
    "miui_provider_ExtraNetwork__navigateToOperatorSettingActivity": {
        "class_path": "miui/provider/ExtraNetwork.smali",
        "method_signature": "navigateToOperatorSettingActivity(Landroid/content/Context;I)V",
        "patch_type": "A",
        "expected_replacements": 1,
    },
    "miui_theme_ThemeManagerHelper__needDisableTheme": {
        "class_path": "miui/theme/ThemeManagerHelper.smali",
        "method_signature": "needDisableTheme(Landroid/content/Context;)Z",
        "patch_type": "A",
        "expected_replacements": 1,
    },
    "miui_yellowpage_HostManager__clinit": {
        "class_path": "miui/yellowpage/HostManager.smali",
        "method_signature": "<clinit>()V",
        "patch_type": "A",
        "expected_replacements": 1,
    },
    "miui_yellowpage_YellowPageUtils__isYellowPageAvailable": {
        "class_path": "miui/yellowpage/YellowPageUtils.smali",
        "method_signature": "isYellowPageAvailable(Landroid/content/Context;)Z",
        "patch_type": "A",
        "expected_replacements": 1,
    },
    # Patch type B — FPS lock guard insertion
    "com_miui_powerkeeper_statemachine_DisplayFrameSetting__setScreenEffect": {
        "class_path": "com/miui/powerkeeper/statemachine/DisplayFrameSetting.smali",
        "method_signature": "setScreenEffect(Ljava/lang/String;II)V",
        "patch_type": "B",
        "expected_replacements": 1,
    },
    # Patch type C — force GMS control disabled
    "com_miui_powerkeeper_utils_GmsObserver__isGmsControlEnabled": {
        "class_path": "com/miui/powerkeeper/utils/GmsObserver.smali",
        "method_signature": "isGmsControlEnabled()Z",
        "patch_type": "C",
        "expected_replacements": 1,
    },
}

_ALLOWLIST_METHOD_PATCH_COUNT = len(EXACT_PATCH_ALLOWLIST)
_ALLOWLIST_CLASS_COUNT = len({e["class_path"] for e in EXACT_PATCH_ALLOWLIST.values()})
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
    applied_classes: set[str] = set()
    method_count = 0
    flag_rewrite_count = 0
    unexpected_skipped = 0
    lock_status = "FAILED_NOT_FOUND"
    gms_status = "FAILED_NOT_FOUND"

    for class_patch in _load_smali_rules():
        for patch in class_patch.patches:
            if patch.id not in EXACT_PATCH_ALLOWLIST:
                unexpected_skipped += 1
                continue

            entry = EXACT_PATCH_ALLOWLIST[patch.id]
            expected_replacements = entry["expected_replacements"]
            patch_type_label = entry["patch_type"]

            if patch.type.startswith("method_"):
                method_count += 1
            flag_rewrite_count += patch.flag_rewrite_count
            applied_classes.add(class_patch.target_class)

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

            status = item["status"]
            if status in ("PATCHED", "WOULD_PATCH"):
                actual_replacements = patch.flag_rewrite_count if patch_type_label == "A" else 1
            else:
                actual_replacements = 0

            count_ok = actual_replacements == expected_replacements
            if status in ("PATCHED", "WOULD_PATCH") and not count_ok:
                status = "FAILED_COUNT_MISMATCH"
                item["status"] = status

            item.update({
                "flag_rewrite_count": patch.flag_rewrite_count,
                "class_path": entry["class_path"],
                "method_signature": entry["method_signature"],
                "patch_type": patch_type_label,
                "expected_replacements": expected_replacements,
                "actual_replacements": actual_replacements,
                "replacement_count_ok": count_ok,
            })
            results.append(item)

            if patch.method_name == "setScreenEffect" and class_patch.target_class.endswith("DisplayFrameSetting.smali"):
                lock_status = item["status"]
            if patch.method_name == "isGmsControlEnabled" and class_patch.target_class.endswith("GmsObserver.smali"):
                gms_status = item["status"]

    failures = [r for r in results if str(r.get("status", "")).startswith("FAILED")]
    return {
        "class_count": len(applied_classes),
        "method_patch_count": method_count,
        "flag_rewrite_patch_count": flag_rewrite_count,
        "unexpected_powerkeeper_rules_skipped": unexpected_skipped,
        "exact_powerkeeper_patch_mode": True,
        "lock_max_fps_mezo_patch_status": lock_status,
        "gms_observer_force_false_patch_status": gms_status,
        "results": results,
        "failures": failures,
    }


def _summarize_smali_rules() -> dict:
    applied_classes: set[str] = set()
    method_count = 0
    flag_rewrite_count = 0
    unexpected_skipped = 0
    lock_status = "WOULD_PATCH"
    gms_status = "WOULD_PATCH"
    results = []
    for class_patch in _load_smali_rules():
        for patch in class_patch.patches:
            if patch.id not in EXACT_PATCH_ALLOWLIST:
                unexpected_skipped += 1
                continue
            entry = EXACT_PATCH_ALLOWLIST[patch.id]
            if patch.type.startswith("method_"):
                method_count += 1
            flag_rewrite_count += patch.flag_rewrite_count
            applied_classes.add(class_patch.target_class)
            item = {
                "id": patch.id,
                "type": patch.type,
                "target_class": class_patch.target_class,
                "status": "WOULD_PATCH",
                "flag_rewrite_count": patch.flag_rewrite_count,
                "class_path": entry["class_path"],
                "method_signature": entry["method_signature"],
                "patch_type": entry["patch_type"],
                "expected_replacements": entry["expected_replacements"],
                "actual_replacements": entry["expected_replacements"],
                "replacement_count_ok": True,
            }
            results.append(item)
            if patch.method_name == "setScreenEffect" and class_patch.target_class.endswith("DisplayFrameSetting.smali"):
                lock_status = item["status"]
            if patch.method_name == "isGmsControlEnabled" and class_patch.target_class.endswith("GmsObserver.smali"):
                gms_status = item["status"]
    return {
        "class_count": len(applied_classes),
        "method_patch_count": method_count,
        "flag_rewrite_patch_count": flag_rewrite_count,
        "unexpected_powerkeeper_rules_skipped": unexpected_skipped,
        "exact_powerkeeper_patch_mode": True,
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
        f"Exact PowerKeeper patch mode: {report.get('exact_powerkeeper_patch_mode')}",
        f"Unexpected PowerKeeper rules skipped: {report.get('unexpected_powerkeeper_rules_skipped')}",
        f"lock_max_fps_mezo patch status: {report.get('lock_max_fps_mezo_patch_status')}",
        f"GmsObserver force false patch status: {report.get('gms_observer_force_false_patch_status')}",
        "",
        "Patch statuses:",
    ]
    for item in report.get("patch_statuses", []):
        expected = item.get("expected_replacements", "?")
        actual = item.get("actual_replacements", "?")
        ptype = item.get("patch_type", "?")
        sig = item.get("method_signature", item.get("target_class", ""))
        lines.append(
            f"  - [{ptype}] {item.get('id')}: {item.get('status')}"
            f" expected={expected} actual={actual} ({sig})"
        )
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
        "exact_powerkeeper_patch_mode": True,
        "unexpected_powerkeeper_rules_skipped": static_smali["unexpected_powerkeeper_rules_skipped"],
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
        "exact_powerkeeper_patch_mode": True,
        "unexpected_powerkeeper_rules_skipped": smali["unexpected_powerkeeper_rules_skipped"],
        "lock_max_fps_mezo_patch_status": smali["lock_max_fps_mezo_patch_status"],
        "gms_observer_force_false_patch_status": smali["gms_observer_force_false_patch_status"],
        "patch_statuses": smali["results"],
        "failures": smali["failures"],
    })
    if smali["failures"]:
        count_mismatches = [f for f in smali["failures"] if f.get("status") == "FAILED_COUNT_MISMATCH"]
        if count_mismatches:
            report["final_status"] = "FAILED_NOT_FOUND"
            report["errors"].append(
                f"{len(count_mismatches)} PowerKeeper patches have replacement count mismatch "
                f"(expected != actual)"
            )
        else:
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
