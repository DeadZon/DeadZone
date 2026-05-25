"""Legend APK patcher — orchestrates Provision, PowerKeeper, and SystemUI APK patches."""
from __future__ import annotations

import importlib
from pathlib import Path
from typing import Optional


def patch_apks(
    root: Path,
    flavor: str,
    *,
    execute: bool = False,
    report_lines: Optional[list[str]] = None,
) -> dict:
    """
    Apply all Legend APK patches in order:
      1. Provision.apk
      2. MiuiSystemUI.apk
      3. PowerKeeper.apk

    Each sub-patcher is loaded via the existing factory.patch.apk.* modules.
    """
    results: dict = {
        "provision": {},
        "systemui": {},
        "powerkeeper": {},
        "errors": [],
        "dry_run": not execute,
    }

    # Provision
    _log(report_lines, "[apk_patcher] Patching Provision.apk")
    try:
        prov = importlib.import_module("factory.patch.apk.provision_legacy")
        r = prov.apply_provision_legacy_patch(project_dir=root, flavor=flavor, execute=execute)
        results["provision"] = r
        _log(report_lines, f"[apk_patcher]   provision: {r.get('final_status', r.get('status'))}")
    except Exception as exc:
        msg = f"provision patch error: {exc}"
        results["errors"].append(msg)
        results["provision"] = {"status": "FAILED", "errors": [msg]}
        _log(report_lines, f"[apk_patcher]   ERROR: {msg}")

    # SystemUI
    _log(report_lines, "[apk_patcher] Patching MiuiSystemUI.apk")
    try:
        sui = importlib.import_module("factory.patch.apk.systemui_legend")
        r = sui.apply_legend_systemui_patch(project_dir=root, flavor=flavor, execute=execute)
        results["systemui"] = r
        _log(report_lines, f"[apk_patcher]   systemui: {r.get('final_status', r.get('status'))}")
    except Exception as exc:
        msg = f"systemui patch error: {exc}"
        results["errors"].append(msg)
        results["systemui"] = {"status": "FAILED", "errors": [msg]}
        _log(report_lines, f"[apk_patcher]   ERROR: {msg}")

    # PowerKeeper
    _log(report_lines, "[apk_patcher] Patching PowerKeeper.apk")
    try:
        pk = importlib.import_module("factory.patch.apk.powerkeeper_legend")
        r = pk.apply_legend_powerkeeper_patch(project_dir=root, flavor=flavor, execute=execute)
        results["powerkeeper"] = r
        _log(report_lines, f"[apk_patcher]   powerkeeper: {r.get('final_status', r.get('status'))}")
    except Exception as exc:
        msg = f"powerkeeper patch error: {exc}"
        results["errors"].append(msg)
        results["powerkeeper"] = {"status": "FAILED", "errors": [msg]}
        _log(report_lines, f"[apk_patcher]   ERROR: {msg}")

    return results


def _log(report_lines: Optional[list[str]], msg: str) -> None:
    print(msg)
    if report_lines is not None:
        report_lines.append(msg)
