"""Integration preflight gate for the DeadZone legacy build pipeline."""
from __future__ import annotations

import argparse
import importlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path
from typing import Any


_REPO_ROOT = Path(__file__).resolve().parents[2]
_REPORT_JSON = "17_integration_preflight_report.json"
_REPORT_TXT = "17_integration_preflight_report.txt"

_REQUIRED_MODULES = [
    "factory.pipeline.legacy_build_orchestrator",
    "factory.notify.telegram_live",
    "factory.patch.common_rom.project_legacy",
    "factory.patch.legend.jar_patch",
    "factory.patch.apk.provision_legacy",
    "factory.images.pipeline_legacy",
    "factory.repack.pipeline_erofs_legacy",
    "factory.repack.pipeline_super_legacy",
    "factory.output.final_zip_legacy",
]

_OPTIONAL_MODULES = [
    "factory.patch.common_rom.assets_legacy",
    "factory.patch.apk.systemui_legend",
]

_HELP_MODULES = [
    "factory.pipeline.legacy_build_orchestrator",
    "factory.output.final_zip_legacy",
    "factory.repack.pipeline_super_legacy",
    "factory.repack.pipeline_erofs_legacy",
]

_OPTIONAL_HELP_MODULES = [
    "factory.patch.apk.systemui_legend",
]

_ALLOWED_FINAL_ZIP_ENTRIES = [
    "bin/windows/fastboot.exe",
    "bin/windows/AdbWinApi.dll",
    "bin/windows/AdbWinUsbApi.dll",
    "images/*.img",
    "windows_install_and_format_data.bat",
    "windows_install_upgrade.bat",
    "windows_format_data_only.bat",
]

_ASCII_DIRS = [
    _REPO_ROOT / "factory" / "pipeline",
    _REPO_ROOT / "factory" / "output",
    _REPO_ROOT / "factory" / "repack",
    _REPO_ROOT / "factory" / "images",
    _REPO_ROOT / "factory" / "patch" / "apk",
]

_NO_BACKUP_DIRS = [
    _REPO_ROOT / "factory" / "pipeline",
    _REPO_ROOT / "factory" / "output",
    _REPO_ROOT / "factory" / "repack",
    _REPO_ROOT / "factory" / "images",
    _REPO_ROOT / "factory" / "patch" / "apk",
]

_NO_BACKUP_PATTERNS = [".bak", "output/backups", "backup_and_restore"]


def _rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(_REPO_ROOT).as_posix()
    except ValueError:
        return str(path)


def _status(ok: bool) -> str:
    return "OK" if ok else "MISSING"


def _path_record(path: Path) -> dict[str, Any]:
    return {
        "path": str(path),
        "exists": path.exists(),
        "is_file": path.is_file(),
        "is_dir": path.is_dir(),
        "status": _status(path.exists()),
    }


def _append_problem(report: dict[str, Any], severity: str, message: str) -> None:
    key = "errors" if severity == "error" else "warnings"
    report[key].append(message)


def _module_present(module_name: str) -> bool:
    spec = importlib.util.find_spec(module_name)
    return spec is not None


def _check_modules(report: dict[str, Any]) -> dict[str, Any]:
    modules: dict[str, Any] = {}
    for module_name in [*_REQUIRED_MODULES, *_OPTIONAL_MODULES]:
        optional = module_name in _OPTIONAL_MODULES
        record: dict[str, Any] = {
            "optional": optional,
            "present": _module_present(module_name),
            "imported": False,
            "origin": None,
            "status": "NOT_RUN",
            "error": None,
        }
        if not record["present"]:
            record["status"] = "OPTIONAL_MISSING" if optional else "MISSING"
            message = f"{'Optional' if optional else 'Required'} module missing: {module_name}"
            _append_problem(report, "warning" if optional else "error", message)
            modules[module_name] = record
            continue
        try:
            module = importlib.import_module(module_name)
            record["imported"] = True
            record["origin"] = getattr(module, "__file__", None)
            record["status"] = "OK"
        except Exception as exc:
            record["error"] = f"{type(exc).__name__}: {exc}"
            record["status"] = "OPTIONAL_IMPORT_FAILED" if optional else "IMPORT_FAILED"
            message = f"{'Optional' if optional else 'Required'} module import failed: {module_name}: {exc}"
            _append_problem(report, "warning" if optional else "error", message)
        modules[module_name] = record
    return modules


def _run_help(module_name: str) -> dict[str, Any]:
    command = [sys.executable, "-m", module_name, "--help"]
    started = time.monotonic()
    try:
        result = subprocess.run(
            command,
            cwd=str(_REPO_ROOT),
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=30,
        )
        stdout = result.stdout.strip()
        stderr = result.stderr.strip()
        return {
            "command": command,
            "returncode": result.returncode,
            "duration_seconds": round(time.monotonic() - started, 3),
            "stdout_preview": stdout[:1000],
            "stderr_preview": stderr[:1000],
            "status": "OK" if result.returncode == 0 else "FAILED",
        }
    except Exception as exc:
        return {
            "command": command,
            "returncode": None,
            "duration_seconds": round(time.monotonic() - started, 3),
            "stdout_preview": "",
            "stderr_preview": "",
            "status": "FAILED",
            "error": f"{type(exc).__name__}: {exc}",
        }


def _check_cli(report: dict[str, Any]) -> dict[str, Any]:
    checks: dict[str, Any] = {}
    for module_name in [*_HELP_MODULES, *_OPTIONAL_HELP_MODULES]:
        optional = module_name in _OPTIONAL_HELP_MODULES
        if optional and not _module_present(module_name):
            checks[module_name] = {"status": "OPTIONAL_MISSING", "optional": True}
            continue
        record = _run_help(module_name)
        record["optional"] = optional
        if record["status"] != "OK":
            message = f"CLI help check failed for {module_name}"
            _append_problem(report, "warning" if optional else "error", message)
        checks[module_name] = record
    return checks


def _check_tools(report: dict[str, Any], vbmeta_mode: str | None) -> dict[str, Any]:
    legacy_root = _REPO_ROOT / "third_party" / "mezo_core"
    tools: dict[str, Any] = {
        "APKEditor.jar": _path_record(legacy_root / "APKEditor.jar"),
        "baksmali.jar": _path_record(legacy_root / "baksmali.jar"),
        "smali.jar": _path_record(legacy_root / "smali.jar"),
    }

    try:
        from factory.repack.erofs_legacy import resolve_mkfs_erofs_binary_legacy

        mkfs = resolve_mkfs_erofs_binary_legacy()
        tools["mkfs.erofs"] = {
            "path": str(mkfs) if mkfs else None,
            "exists": bool(mkfs and Path(mkfs).exists()),
            "resolver": "factory.repack.erofs_legacy.resolve_mkfs_erofs_binary_legacy",
            "status": "OK" if mkfs else "MISSING",
        }
    except Exception as exc:
        tools["mkfs.erofs"] = {
            "path": None,
            "exists": False,
            "resolver": "factory.repack.erofs_legacy.resolve_mkfs_erofs_binary_legacy",
            "status": "FAILED",
            "error": str(exc),
        }

    try:
        from factory.repack.super_builder_legacy import resolve_lpmake_binary_legacy

        lpmake = resolve_lpmake_binary_legacy()
        tools["lpmake"] = {
            "path": str(lpmake) if lpmake else None,
            "exists": bool(lpmake and Path(lpmake).exists()),
            "resolver": "factory.repack.super_builder_legacy.resolve_lpmake_binary_legacy",
            "status": "OK" if lpmake else "MISSING",
        }
    except Exception as exc:
        tools["lpmake"] = {
            "path": None,
            "exists": False,
            "resolver": "factory.repack.super_builder_legacy.resolve_lpmake_binary_legacy",
            "status": "FAILED",
            "error": str(exc),
        }

    selected_vbmeta = str(vbmeta_mode or "").strip()
    avbtool_required = selected_vbmeta not in {"", "0", "none", "skip", "disabled"}
    avbtool = legacy_root / "vbmeta" / "avbtool.py"
    tools["avbtool.py"] = {
        **_path_record(avbtool),
        "required": avbtool_required,
        "reason": "vbmeta mode requires vbmeta stage tool" if avbtool_required else "vbmeta mode does not require patching",
    }

    for name, record in tools.items():
        if record.get("status") != "OK" and record.get("required", True):
            _append_problem(report, "error", f"Required tool missing or failed resolver: {name}")
    return tools


def _check_references(report: dict[str, Any], template_zip: Path | None) -> dict[str, Any]:
    legacy_root = _REPO_ROOT / "third_party" / "mezo_core"
    canonical_systemui = legacy_root / "MEZO_LEGEND" / "MiuiSystemUI"
    fallback_systemui = _REPO_ROOT / "Legend" / "MiuiSystemUI"
    template_dir = legacy_root / "templates" / "deadzone_fastboot"
    template_zip_path = template_zip.resolve() if template_zip else None

    references: dict[str, Any] = {
        "legend_jar": _path_record(legacy_root / "MEZO_LEGEND" / "jar"),
        "legend_systemui_canonical": _path_record(canonical_systemui),
        "legend_systemui_fallback": _path_record(fallback_systemui),
        "fastboot_template_dir": _path_record(template_dir),
        "fastboot_template_zip": _path_record(template_zip_path) if template_zip_path else {
            "path": None,
            "exists": False,
            "status": "NOT_PROVIDED",
        },
    }
    references["legend_systemui_effective"] = {
        "path": str(canonical_systemui if canonical_systemui.is_dir() else fallback_systemui),
        "exists": canonical_systemui.is_dir() or fallback_systemui.is_dir(),
        "source": "canonical" if canonical_systemui.is_dir() else ("fallback" if fallback_systemui.is_dir() else None),
        "status": "OK" if canonical_systemui.is_dir() or fallback_systemui.is_dir() else "MISSING",
    }
    references["fastboot_template_effective"] = {
        "path": str(template_zip_path if template_zip_path and template_zip_path.is_file() else template_dir),
        "exists": bool((template_zip_path and template_zip_path.is_file()) or template_dir.is_dir()),
        "source": "template_zip" if template_zip_path and template_zip_path.is_file() else ("template_dir" if template_dir.is_dir() else None),
        "status": "OK" if ((template_zip_path and template_zip_path.is_file()) or template_dir.is_dir()) else "MISSING",
    }

    if references["legend_jar"]["status"] != "OK":
        _append_problem(report, "error", "Legend JAR reference directory missing")
    if references["legend_systemui_canonical"]["status"] != "OK":
        _append_problem(report, "warning", "Canonical MiuiSystemUI reference missing; fallback will be used if present")
    if references["legend_systemui_effective"]["status"] != "OK":
        _append_problem(report, "warning", "MiuiSystemUI reference missing from canonical and fallback locations")
    if references["fastboot_template_effective"]["status"] != "OK":
        _append_problem(report, "error", "Canonical DeadZone fastboot template folder or ZIP missing")
    return references


def _check_telegram() -> dict[str, Any]:
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = os.environ.get("TELEGRAM_CHAT_ID", "").strip()
    thread_id = os.environ.get("TELEGRAM_THREAD_ID", "").strip()
    message_thread_id = os.environ.get("TELEGRAM_MESSAGE_THREAD_ID", "").strip()
    missing = []
    if not token:
        missing.append("TELEGRAM_BOT_TOKEN")
    if not chat_id:
        missing.append("TELEGRAM_CHAT_ID")
    if not (thread_id or message_thread_id):
        missing.append("TELEGRAM_THREAD_ID or TELEGRAM_MESSAGE_THREAD_ID")
    return {
        "enabled": bool(token and chat_id),
        "status": "ENABLED" if token and chat_id else "DISABLED",
        "token_present": bool(token),
        "chat_id_present": bool(chat_id),
        "thread_id_present": bool(thread_id or message_thread_id),
        "missing": missing,
        "http_call_performed": False,
    }


def _is_backup_disabled_comment(line: str) -> bool:
    stripped = line.strip().lower()
    if not stripped.startswith("#"):
        return False
    return "backup" in stripped and any(word in stripped for word in ["disabled", "no backup", "not used"])


def _is_no_backup_scanner_definition(line: str) -> bool:
    return "_NO_BACKUP_PATTERNS" in line


def _check_no_backup_policy() -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    for base in _NO_BACKUP_DIRS:
        if not base.is_dir():
            continue
        for path in sorted(base.rglob("*.py")):
            if "__pycache__" in path.parts:
                continue
            try:
                lines = path.read_text(encoding="utf-8").splitlines()
            except UnicodeDecodeError:
                lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
            for line_no, line in enumerate(lines, start=1):
                if _is_no_backup_scanner_definition(line):
                    continue
                normalized = line.replace("\\", "/")
                for pattern in _NO_BACKUP_PATTERNS:
                    if pattern in normalized and not _is_backup_disabled_comment(line):
                        findings.append({
                            "file": _rel(path),
                            "line": line_no,
                            "pattern": pattern,
                            "text": line.strip()[:200],
                        })
    return {
        "status": "WARNING" if findings else "OK",
        "patterns": list(_NO_BACKUP_PATTERNS),
        "findings": findings,
    }


def _check_ascii() -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    for base in _ASCII_DIRS:
        if not base.is_dir():
            continue
        for path in sorted(base.rglob("*.py")):
            if "__pycache__" in path.parts:
                continue
            data = path.read_bytes()
            for line_no, raw_line in enumerate(data.splitlines(), start=1):
                bad = [byte for byte in raw_line if byte > 127]
                if bad:
                    text = raw_line.decode("utf-8", errors="replace")
                    findings.append({
                        "file": _rel(path),
                        "line": line_no,
                        "text": text.strip()[:200],
                    })
    return {
        "status": "OK" if not findings else "FAILED",
        "checked_dirs": [_rel(path) for path in _ASCII_DIRS],
        "findings": findings,
    }


def _check_final_zip_safety(report: dict[str, Any]) -> dict[str, Any]:
    safety: dict[str, Any] = {
        "allowed_entries": list(_ALLOWED_FINAL_ZIP_ENTRIES),
        "module": "factory.output.final_zip_legacy",
        "status": "FAILED",
        "details": {},
        "errors": [],
    }
    try:
        module = importlib.import_module("factory.output.final_zip_legacy")
        required_public_files = list(getattr(module, "REQUIRED_PUBLIC_FILES", []))
        script_names = list(getattr(module, "SCRIPT_NAMES", []))
        has_is_allowed = callable(getattr(module, "_is_allowed_entry", None))
        has_validate_entries = callable(getattr(module, "_validate_entries", None))
        has_forbidden_reason = callable(getattr(module, "_forbidden_reason", None))
        expected_files = [
            "bin/windows/fastboot.exe",
            "bin/windows/AdbWinApi.dll",
            "bin/windows/AdbWinUsbApi.dll",
            "windows_install_and_format_data.bat",
            "windows_install_upgrade.bat",
            "windows_format_data_only.bat",
        ]
        details = {
            "REQUIRED_PUBLIC_FILES": required_public_files,
            "SCRIPT_NAMES": script_names,
            "_is_allowed_entry": has_is_allowed,
            "_validate_entries": has_validate_entries,
            "_forbidden_reason": has_forbidden_reason,
        }
        safety["details"] = details
        missing = [entry for entry in expected_files if entry not in required_public_files]
        if missing:
            safety["errors"].append("Required allowlist entries missing: " + ", ".join(missing))
        if not has_is_allowed or not has_validate_entries or not has_forbidden_reason:
            safety["errors"].append("Final ZIP module does not expose required validation helpers")
        if has_is_allowed:
            checker = getattr(module, "_is_allowed_entry")
            probes = {
                "bin/windows/fastboot.exe": True,
                "images/system.img": True,
                "images/nested/system.img": False,
                "README.md": False,
                "output/reports/report.json": False,
            }
            probe_results = {name: bool(checker(name)) for name in probes}
            details["probe_results"] = probe_results
            failed = [name for name, expected in probes.items() if probe_results[name] != expected]
            if failed:
                safety["errors"].append("Final ZIP allowlist probes failed: " + ", ".join(failed))
        safety["status"] = "OK" if not safety["errors"] else "FAILED"
    except Exception as exc:
        safety["errors"].append(f"{type(exc).__name__}: {exc}")

    for error in safety["errors"]:
        _append_problem(report, "error", error)
    return safety


def _write_reports(report: dict[str, Any], output_dir: Path) -> dict[str, str]:
    reports_dir = output_dir / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    json_path = reports_dir / _REPORT_JSON
    txt_path = reports_dir / _REPORT_TXT
    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=True, default=str), encoding="utf-8")
    txt_path.write_text(_format_text_report(report), encoding="utf-8", newline="\n")
    return {"json": str(json_path), "txt": str(txt_path)}


def _format_section(title: str, values: dict[str, Any]) -> list[str]:
    lines = [title + ":"]
    for key, value in values.items():
        if isinstance(value, dict):
            status = value.get("status")
            if status is None and "exists" in value:
                status = _status(bool(value.get("exists")))
            detail = value.get("path") or value.get("origin") or value.get("source") or ""
            lines.append(f"  {key}: {status or value}")
            if detail:
                lines.append(f"    {detail}")
        else:
            lines.append(f"  {key}: {value}")
    return lines


def _format_text_report(report: dict[str, Any]) -> str:
    lines = [
        "DeadZone Integration Preflight Report",
        "=" * 64,
        f"Final status     : {report.get('final_status')}",
        f"Stage            : {report.get('stage')}",
        f"Project dir      : {report.get('project_dir')}",
        f"Output dir       : {report.get('output_dir')}",
        f"Build name       : {report.get('build_name')}",
        f"Device           : {report.get('device')}",
        f"SOC              : {report.get('soc')}",
        f"Platform         : {report.get('platform')}",
        f"Flavor           : {report.get('flavor')}",
        f"Android version  : {report.get('android_version')}",
        f"MI incremental   : {report.get('mi_incremental')}",
        "",
    ]
    lines.extend(_format_section("Tools", report.get("tools", {})))
    lines.append("")
    lines.extend(_format_section("Modules", report.get("modules", {})))
    lines.append("")
    lines.extend(_format_section("References", report.get("references", {})))
    lines.append("")
    lines.extend(_format_section("CLI help checks", report.get("cli_check", {})))
    lines.append("")
    lines.append(f"Telegram: {report.get('telegram', {}).get('status')}")
    missing = report.get("telegram", {}).get("missing") or []
    lines.append("  Missing: " + (", ".join(missing) if missing else "(none)"))
    lines.append("  HTTP call performed: False")
    lines.append("")
    lines.append(f"No-backup policy: {report.get('no_backup_policy', {}).get('status')}")
    for finding in report.get("no_backup_policy", {}).get("findings", []):
        lines.append(f"  {_rel(_REPO_ROOT / finding['file'])}:{finding['line']} {finding['pattern']}")
    lines.append("")
    lines.append(f"ASCII check: {report.get('ascii_check', {}).get('status')}")
    for finding in report.get("ascii_check", {}).get("findings", []):
        lines.append(f"  {finding['file']}:{finding['line']} {finding['text']}")
    lines.append("")
    lines.append(f"Final ZIP safety: {report.get('final_zip_safety', {}).get('status')}")
    lines.append("")
    lines.append("Warnings:")
    if report.get("warnings", []):
        lines.extend(f"  ! {warning}" for warning in report.get("warnings", []))
    else:
        lines.append("  (none)")
    lines.append("")
    lines.append("Errors:")
    if report.get("errors", []):
        lines.extend(f"  X {error}" for error in report.get("errors", []))
    else:
        lines.append("  (none)")
    lines.append("")
    return "\n".join(lines)


def run_integration_preflight(
    project_dir: Path,
    output_dir: Path,
    build_name: str,
    device: str,
    soc: str,
    platform: str,
    flavor: str,
    android_version: str,
    mi_incremental: str,
    vbmeta_mode: str | None = None,
    template_zip: Path | None = None,
) -> dict[str, Any]:
    project_dir = Path(project_dir).resolve()
    output_dir = Path(output_dir).resolve()
    report: dict[str, Any] = {
        "stage": "integration_preflight",
        "project_dir": str(project_dir),
        "project_dir_exists": project_dir.is_dir(),
        "output_dir": str(output_dir),
        "build_name": build_name,
        "device": device,
        "soc": soc,
        "platform": platform,
        "flavor": flavor,
        "android_version": android_version,
        "mi_incremental": mi_incremental,
        "vbmeta_mode": vbmeta_mode,
        "template_zip": str(template_zip.resolve()) if template_zip else None,
        "tools": {},
        "modules": {},
        "references": {},
        "telegram": {},
        "no_backup_policy": {},
        "ascii_check": {},
        "cli_check": {},
        "final_zip_safety": {},
        "warnings": [],
        "errors": [],
        "final_status": "FAILED",
    }

    if not project_dir.is_dir():
        report["errors"].append(f"Project directory does not exist: {project_dir}")

    report["modules"] = _check_modules(report)
    report["tools"] = _check_tools(report, vbmeta_mode)
    report["references"] = _check_references(report, template_zip)
    report["cli_check"] = _check_cli(report)
    report["telegram"] = _check_telegram()
    report["no_backup_policy"] = _check_no_backup_policy()
    if report["no_backup_policy"]["findings"]:
        report["warnings"].append("Backup-related patterns found in relevant factory modules")
    report["ascii_check"] = _check_ascii()
    if report["ascii_check"]["findings"]:
        report["errors"].append("Non-ASCII text found in checked factory modules")
    report["final_zip_safety"] = _check_final_zip_safety(report)

    if report["errors"]:
        report["final_status"] = "FAILED"
    elif report["warnings"]:
        report["final_status"] = "READY_WITH_WARNINGS"
    else:
        report["final_status"] = "READY"

    report["report_files"] = _write_reports(report, output_dir)
    return report


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="DeadZone integration preflight gate")
    parser.add_argument("--project", required=True, type=Path, help="Path to unpacked project")
    parser.add_argument("--output-dir", required=True, type=Path, help="Output directory")
    parser.add_argument("--build-name", required=True)
    parser.add_argument("--device", required=True)
    parser.add_argument("--soc", required=True)
    parser.add_argument("--platform", required=True)
    parser.add_argument("--flavor", required=True)
    parser.add_argument("--android-version", required=True)
    parser.add_argument("--mi-version", dest="mi_version", required=True)
    parser.add_argument("--vbmeta-mode", default=None)
    parser.add_argument("--template-zip", type=Path, default=None)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    report = run_integration_preflight(
        project_dir=args.project,
        output_dir=args.output_dir,
        build_name=args.build_name,
        device=args.device,
        soc=args.soc,
        platform=args.platform,
        flavor=args.flavor,
        android_version=args.android_version,
        mi_incremental=args.mi_version,
        vbmeta_mode=args.vbmeta_mode,
        template_zip=args.template_zip,
    )
    print(f"[integration_preflight] final_status={report['final_status']}")
    print(f"[integration_preflight] report_json={report['report_files']['json']}")
    print(f"[integration_preflight] report_txt={report['report_files']['txt']}")
    return 0 if report["final_status"] in {"READY", "READY_WITH_WARNINGS"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
