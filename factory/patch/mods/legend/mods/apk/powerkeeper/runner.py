"""Legend PowerKeeper APK patch runner."""
from __future__ import annotations

import importlib
import json
import pkgutil
import re
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
    rebuild_apk_with_diagnostics,
    restore_rebuilt_apk_no_backup,
)
from factory.patch.mods.legend.mods.apk.powerkeeper.policy import POWERKEEPER_ALLOWED_FLAG_REWRITES
from factory.patch.mods.legend.mods.apk.powerkeeper.model import load_class_patch

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
from factory.patch.mods.legend.smart_smali_patcher import (
    ClassMatchStatus,
    MethodMatchStatus,
    PatchApplyStatus,
    apply_smart_patch,
    find_class,
    find_method,
)

_REPO_ROOT = Path(__file__).resolve().parents[5]
_PKG_ROOT = Path(__file__).resolve().parent
_REPORTS_DIR = _REPO_ROOT / "output" / "reports"
_LOGS_DIR = _REPO_ROOT / "output" / "logs"
_WORK_DIR_DEFAULT = _REPO_ROOT / "output" / "work" / "powerkeeper_legend_apk_work"
_LEGEND_FLAVORS = frozenset({"legend", "deadzone_legend"})

POWERKEEPER_APK_NAME = "PowerKeeper.apk"
POWERKEEPER_APK_SRC_DIR_NAME = "PowerKeeper_apk_src"
POWERKEEPER_STOCK_SRC_DIR_NAME = "PowerKeeper_stock_apk_src"
POWERKEEPER_BISECT_SRC_DIR_NAME = "PowerKeeper_bisect_apk_src"


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
    package = "factory.patch.mods.legend.mods.apk.powerkeeper.smali"
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


def _apply_smali_rules(
    decompiled_dir: Path,
    dry_run: bool,
    only_groups: set[str] | None = None,
) -> dict:
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

            if only_groups is not None and patch_type_label not in only_groups:
                continue

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


# ── Diagnostics helpers ───────────────────────────────────────────────────────

def _first_error_line(text: str) -> str:
    """Extract the first meaningful error/exception line from rebuild output."""
    for line in text.splitlines():
        stripped = line.strip()
        if stripped and any(kw in stripped.lower() for kw in ("error", "exception", "failed", "cannot", "unable")):
            return stripped
    for line in reversed(text.splitlines()):
        if line.strip():
            return line.strip()
    return "(no output)"


def _write_rebuild_logs(rebuild_result: dict, prefix: str = "powerkeeper") -> dict:
    """Write rebuild diagnostics to output/logs/. Returns paths dict."""
    _LOGS_DIR.mkdir(parents=True, exist_ok=True)
    cmd_path    = _LOGS_DIR / f"{prefix}_rebuild_command.txt"
    stdout_path = _LOGS_DIR / f"{prefix}_rebuild_stdout.txt"
    stderr_path = _LOGS_DIR / f"{prefix}_rebuild_stderr.txt"
    cmd_path.write_text(rebuild_result.get("command", ""), encoding="utf-8")
    stdout_path.write_text(rebuild_result.get("stdout", ""), encoding="utf-8")
    stderr_path.write_text(rebuild_result.get("stderr", ""), encoding="utf-8")
    return {
        "rebuild_command": str(cmd_path),
        "rebuild_stdout":  str(stdout_path),
        "rebuild_stderr":  str(stderr_path),
    }


# ── Pre-rebuild smali validation ─────────────────────────────────────────────

def _has_invalid_smali_escape(line: str) -> bool:
    """Return True if a const-string smali line has an invalid escape sequence."""
    m = re.search(r'const-string[^"]*"(.*)"', line)
    if not m:
        return False
    s = m.group(1)
    i = 0
    valid_escapes = set('\\nrt"\' 0abfvuNxX')
    while i < len(s):
        if s[i] == '\\':
            if i + 1 >= len(s) or s[i + 1] not in valid_escapes:
                return True
            i += 2
        else:
            i += 1
    return False


def _validate_patched_smali(decompiled_dir: Path, patch_results: list[dict]) -> dict:
    """
    Validate patched smali files before rebuild.

    Checks:
      1. Each patched class file has balanced .method / .end method directives.
      2. No invalid smali escape sequences (e.g. \\. inside const-string values).

    Returns a dict with 'errors' (list[str]) and 'checked_count' (int).
    """
    errors: list[str] = []
    checked: set[str] = set()
    smali_roots = _find_smali_roots(decompiled_dir)

    for item in patch_results:
        if item.get("status") not in ("PATCHED",):
            continue
        class_path = item.get("class_path", "")
        if not class_path or class_path in checked:
            continue
        checked.add(class_path)

        # Locate the smali file
        smali_file: Path | None = None
        for root in smali_roots:
            candidate = root / class_path
            if candidate.is_file():
                smali_file = candidate
                break
        if smali_file is None:
            rel_suffix = "/" + class_path.replace("\\", "/")
            for root in smali_roots:
                for p in root.rglob("*.smali"):
                    if str(p).replace("\\", "/").endswith(rel_suffix):
                        smali_file = p
                        break
                if smali_file:
                    break

        if smali_file is None:
            continue

        try:
            text = smali_file.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue

        # Check .method / .end method balance
        method_count = len(re.findall(r"(?m)^\s*\.method\b", text))
        end_method_count = len(re.findall(r"(?m)^\s*\.end method\b", text))
        if method_count != end_method_count:
            errors.append(
                f"{class_path}: unbalanced .method ({method_count}) / "
                f".end method ({end_method_count}) — likely a partial replacement"
            )

        # Check for invalid smali escape sequences in string literals
        for lineno, line in enumerate(text.splitlines(), 1):
            if "const-string" in line and '"' in line and _has_invalid_smali_escape(line):
                errors.append(
                    f"{class_path}:{lineno}: invalid smali escape in string: {line.strip()!r}"
                )

    return {"errors": errors, "checked_count": len(checked)}


# ── Stock rebuild test ────────────────────────────────────────────────────────

def _run_stock_rebuild_test(
    apkeditor_jar: Path,
    work_dir: Path,
    work_apk: Path,
) -> dict:
    """
    Decompile work_apk into a separate stock dir and immediately rebuild it.
    Verifies that APKEditor can round-trip this APK before any patches are applied.
    Returns a dict with keys: status, error_line (on failure), rebuild_result (on failure).
    """
    stock_dir = work_dir / POWERKEEPER_STOCK_SRC_DIR_NAME
    print("[legend_powerkeeper] Stock rebuild test: decompiling ...")
    if not decompile_apk(apkeditor_jar, work_apk, stock_dir):
        return {"status": "FAILED_STOCK_DECOMPILE", "error_line": "Stock APK decompile failed"}

    print("[legend_powerkeeper] Stock rebuild test: rebuilding ...")
    result = rebuild_apk_with_diagnostics(apkeditor_jar, stock_dir)

    shutil.rmtree(stock_dir, ignore_errors=True)
    stock_rebuilt = work_dir / "PowerKeeper_stock.apk"
    try:
        stock_rebuilt.unlink(missing_ok=True)
    except Exception:
        pass

    if not result["success"]:
        combined = (result.get("stderr", "") + "\n" + result.get("stdout", "")).strip()
        return {
            "status": "FAILED_STOCK_REBUILD",
            "error_line": _first_error_line(combined),
            "returncode": result.get("returncode"),
            "rebuild_result": result,
        }

    print("[legend_powerkeeper] Stock rebuild test: OK")
    return {"status": "STOCK_REBUILD_OK"}


# ── Bisection ─────────────────────────────────────────────────────────────────

def _run_bisection(
    apkeditor_jar: Path,
    work_apk: Path,
    work_dir: Path,
) -> dict:
    """
    Incremental group bisection on a fresh decompile of work_apk.
    Applies groups A → B → C in order, rebuilding after each.
    Stops at the first failing group and reports it.
    """
    bisect_dir = work_dir / POWERKEEPER_BISECT_SRC_DIR_NAME
    print("[legend_powerkeeper] Bisection: decompiling fresh ...")
    if not decompile_apk(apkeditor_jar, work_apk, bisect_dir):
        return {
            "status": "FAILED_BISECT_DECOMPILE",
            "failing_group": None,
            "last_patch_id_at_failure": None,
            "group_results": {},
        }

    group_results: dict[str, dict] = {}
    failing_group: str | None = None
    last_patch_id: str | None = None

    for group in ("A", "B", "C"):
        roots = _find_smali_roots(bisect_dir)
        patches_in_group: list[str] = []

        for class_patch in _load_smali_rules():
            for patch in class_patch.patches:
                if patch.id not in EXACT_PATCH_ALLOWLIST:
                    continue
                entry = EXACT_PATCH_ALLOWLIST[patch.id]
                if entry["patch_type"] != group:
                    continue

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
                    _apply_delete_rule(roots, rule, dry_run=False)
                else:
                    apply_smart_patch(roots, rule, dry_run=False)

                patches_in_group.append(patch.id)
                last_patch_id = patch.id

        print(f"[legend_powerkeeper] Bisection: rebuilding after group {group} ({len(patches_in_group)} patches) ...")
        rebuild_result = rebuild_apk_with_diagnostics(apkeditor_jar, bisect_dir)
        combined = (rebuild_result.get("stderr", "") + "\n" + rebuild_result.get("stdout", "")).strip()

        group_results[group] = {
            "patches_applied": len(patches_in_group),
            "patch_ids": patches_in_group,
            "last_patch_id": last_patch_id,
            "rebuild_success": rebuild_result["success"],
            "rebuild_returncode": rebuild_result["returncode"],
            "rebuild_error_line": _first_error_line(combined) if not rebuild_result["success"] else None,
        }

        if not rebuild_result["success"] and failing_group is None:
            failing_group = group
            break

    shutil.rmtree(bisect_dir, ignore_errors=True)
    bisect_rebuilt = work_dir / "PowerKeeper_bisect.apk"
    try:
        bisect_rebuilt.unlink(missing_ok=True)
    except Exception:
        pass

    if failing_group:
        status = f"BISECT_FAILED_GROUP_{failing_group}"
        last_id = group_results[failing_group].get("last_patch_id")
    else:
        status = "BISECT_ALL_GROUPS_OK"
        last_id = None

    return {
        "status": status,
        "failing_group": failing_group,
        "last_patch_id_at_failure": last_id,
        "group_results": group_results,
    }


# ── Report formatting ─────────────────────────────────────────────────────────

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

    stock = report.get("stock_rebuild")
    if stock:
        lines.extend(["", "Stock rebuild test:"])
        lines.append(f"  status: {stock.get('status')}")
        if stock.get("error_line"):
            lines.append(f"  error:  {stock['error_line']}")

    diag = report.get("rebuild_diagnostics")
    if diag:
        lines.extend(["", "Rebuild diagnostics:"])
        lines.append(f"  returncode: {diag.get('returncode')}")
        if diag.get("error_line"):
            lines.append(f"  error_line: {diag['error_line']}")

    bisect = report.get("bisection")
    if bisect:
        lines.extend(["", "Bisection:"])
        lines.append(f"  status:        {bisect.get('status')}")
        lines.append(f"  failing_group: {bisect.get('failing_group')}")
        lines.append(f"  last_patch_id: {bisect.get('last_patch_id_at_failure')}")
        for grp, gr in (bisect.get("group_results") or {}).items():
            lines.append(f"  group {grp}: rebuild_success={gr.get('rebuild_success')} patches={gr.get('patches_applied')}")
            if gr.get("rebuild_error_line"):
                lines.append(f"    error: {gr['rebuild_error_line']}")

    log_files = report.get("log_files", {})
    if log_files:
        lines.extend(["", "Log files:"])
        for k, v in log_files.items():
            lines.append(f"  {k}: {v}")

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
        "stock_rebuild": None,
        "rebuild_diagnostics": None,
        "bisection": None,
        "log_files": {},
        "report_files": {},
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

    # ── Execute ───────────────────────────────────────────────────────────────

    prepare_apk_work_dir(effective_work_dir, POWERKEEPER_APK_NAME)
    work_apk = copy_apk_to_work(powerkeeper_apk, effective_work_dir)

    # 1. Stock rebuild test: verify APKEditor can round-trip the APK unmodified
    stock = _run_stock_rebuild_test(apkeditor_jar, effective_work_dir, work_apk)
    report["stock_rebuild"] = stock
    if stock["status"] != "STOCK_REBUILD_OK":
        if "rebuild_result" in stock:
            report["log_files"] = _write_rebuild_logs(stock["rebuild_result"], "powerkeeper")
        report["final_status"] = "FAILED_STOCK_REBUILD"
        err = stock.get("error_line") or stock.get("status", "stock rebuild failed")
        report["failures"].append(err)
        report["errors"].append(err)
        _write_reports(report)
        return report

    # 2. Decompile for patching
    decompiled_dir = effective_work_dir / POWERKEEPER_APK_SRC_DIR_NAME
    if not decompile_apk(apkeditor_jar, work_apk, decompiled_dir):
        report["final_status"] = "FAILED_NOT_FOUND"
        report["failures"].append("APK decompile failed")
        report["errors"].append("APK decompile failed")
        _write_reports(report)
        return report

    # 3. Apply the 23 patches
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

    # 3.5. Pre-rebuild smali validation
    print("[legend_powerkeeper] Validating patched smali files ...")
    validation = _validate_patched_smali(decompiled_dir, smali["results"])
    report["smali_validation"] = validation
    if validation["errors"]:
        report["final_status"] = "FAILED_SMALI_VALIDATION"
        for err in validation["errors"]:
            report["failures"].append(err)
            report["errors"].append(err)
            print(f"[legend_powerkeeper] SMALI VALIDATION ERROR: {err}")
        _write_reports(report)
        return report
    print(f"[legend_powerkeeper] Smali validation OK ({validation['checked_count']} files checked)")

    # 4. Rebuild with full diagnostics
    print("[legend_powerkeeper] Rebuilding patched APK ...")
    rebuild_result = rebuild_apk_with_diagnostics(apkeditor_jar, decompiled_dir)
    report["log_files"] = _write_rebuild_logs(rebuild_result, "powerkeeper")
    report["report_files"]["log_files"] = report["log_files"]

    combined_output = (rebuild_result.get("stderr", "") + "\n" + rebuild_result.get("stdout", "")).strip()
    report["rebuild_diagnostics"] = {
        "returncode": rebuild_result["returncode"],
        "error_line": _first_error_line(combined_output) if not rebuild_result["success"] else None,
    }

    if not rebuild_result["success"]:
        # 5. Run bisection to find the failing patch group
        print("[legend_powerkeeper] Patched rebuild failed — running bisection ...")
        bisect = _run_bisection(apkeditor_jar, work_apk, effective_work_dir)
        report["bisection"] = bisect

        report["final_status"] = "FAILED_REBUILD_WITH_LOGS"
        error_line = report["rebuild_diagnostics"]["error_line"] or "APK rebuild failed"
        report["failures"].append(error_line)
        report["errors"].append(error_line)
        _write_reports(report)
        return report

    shutil.rmtree(decompiled_dir, ignore_errors=True)

    # 5. Restore rebuilt APK
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
