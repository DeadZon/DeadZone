"""
Patch-stage report generation.

Writes:
  output/reports/03_legend_jar_patch_report.json
  output/reports/03_legend_jar_patch_report.txt
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from factory.patch.common.mtcr_exact_patcher import MethodPatchResult, PatchStatus
from factory.patch.common.add_dex_merger import AddDexMergeResult

_REPORT_JSON = "03_legend_jar_patch_report.json"
_REPORT_TXT  = "03_legend_jar_patch_report.txt"


@dataclass
class MtcrPackReport:
    mtcr_name: str
    jar_name: str
    method_results: list[MethodPatchResult] = field(default_factory=list)


@dataclass
class JarReport:
    jar_name: str
    jar_partition_path: str      # e.g. system/framework/framework.jar
    found: bool
    mtcr_reports: list[MtcrPackReport] = field(default_factory=list)
    add_dex_reports: list[AddDexMergeResult] = field(default_factory=list)
    decompile_ok: bool = False
    decompile_errors: list[str] = field(default_factory=list)
    repack_ok: bool = False
    repack_errors: list[str] = field(default_factory=list)
    # restore_ok / restore_error are repurposed as replace_ok / replace_error
    # (backup_path is always None -- backup is disabled)
    restore_ok: bool = False
    backup_path: Optional[Path] = None
    restore_error: str = ""


@dataclass
class PatchSession:
    flavor: str
    dry_run: bool
    project_dir: Path
    work_dir: Path
    patch_dir: Path
    android_major: int | None = None
    jar_reports: list[JarReport] = field(default_factory=list)
    # Optional pipeline stages -- set to a status dict after each stage runs.
    # Format: {"module": str, "status": str, "warnings": list, "errors": list}
    signature_bypass_stage: dict | None = None
    jar_misc_legacy_stage: dict | None = None
    kaori_legacy_stage: dict | None = None
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)


# -- Serialise -
def _method_result_to_dict(mr: MethodPatchResult) -> dict:
    return {
        "class": mr.class_name,
        "status": mr.status.value,
        "method_sig": mr.method_sig,
        "field_decl": mr.field_decl,
        "target_smali": str(mr.target_smali) if mr.target_smali else None,
        "message": mr.message,
    }


def _add_dex_result_to_dict(adr: AddDexMergeResult) -> dict:
    return {
        "dex_path": str(adr.dex_path),
        "target_jar": adr.target_jar,
        "dex_valid": adr.dex_valid,
        "decompiled": adr.decompiled,
        "class_count": adr.class_count,
        "smali_root": str(adr.smali_root) if adr.smali_root else None,
        "merged_count": adr.merged_count,
        "conflict_count": adr.conflict_count,
        "errors": adr.errors,
        "class_results": [_method_result_to_dict(r) for r in adr.class_results],
    }


def _mtcr_report_to_dict(mr: MtcrPackReport) -> dict:
    return {
        "mtcr": mr.mtcr_name,
        "jar": mr.jar_name,
        "method_results": [_method_result_to_dict(r) for r in mr.method_results],
    }


def _jar_report_to_dict(jr: JarReport) -> dict:
    return {
        "jar": jr.jar_name,
        "partition_path": jr.jar_partition_path,
        "found": jr.found,
        "decompile_ok": jr.decompile_ok,
        "decompile_errors": jr.decompile_errors,
        "repack_ok": jr.repack_ok,
        "repack_errors": jr.repack_errors,
        "replace_ok": jr.restore_ok,       # backup disabled -- repurposed as replace
        "replace_error": jr.restore_error, # backup disabled -- repurposed as replace
        "backup_path": None,               # always None; backup is disabled
        "add_dex": [_add_dex_result_to_dict(a) for a in jr.add_dex_reports],
        "mtcr_packs": [_mtcr_report_to_dict(m) for m in jr.mtcr_reports],
    }


def _session_final_status(session: PatchSession) -> str:
    _legend = {"legend", "deadzone_legend"}
    if session.flavor.lower().replace("-", "_") not in _legend:
        return "SKIPPED_NON_LEGEND"
    if session.dry_run:
        return "DRY_RUN"
    if session.errors:
        return "FAILED"
    return "APPLIED"


def session_to_dict(session: PatchSession) -> dict:
    return {
        "flavor": session.flavor,
        "android_major": session.android_major,
        "dry_run": session.dry_run,
        "backup_policy": "disabled",
        "project_path": str(session.project_dir),
        "work_dir": str(session.work_dir),
        "patch_dir": str(session.patch_dir),
        "target_jars": [_jar_report_to_dict(jr) for jr in session.jar_reports],
        "signature_bypass_stage": session.signature_bypass_stage,
        "jar_misc_legacy_stage": session.jar_misc_legacy_stage,
        "kaori_legacy_stage": session.kaori_legacy_stage,
        "warnings": session.warnings,
        "errors": session.errors,
        "final_status": _session_final_status(session),
    }


# -- Text format -
_STATUS_ICONS: dict[str, str] = {
    # exact patcher statuses
    "APPLIED_EXACT_METHOD":       "OK",
    "WOULD_APPLY_EXACT_METHOD":   "~~",
    "ADDED_METHOD":               "+M",
    "WOULD_ADD_METHOD":           "~M",
    "ADDED_FIELD":                "+F",
    "WOULD_ADD_FIELD":            "~F",
    "ADDED_CLASS":                "+C",
    "WOULD_ADD_CLASS":            "~C",
    "EXISTS_IDENTICAL":           "==",
    "CONFLICT":                   "!!",
    "SKIPPED_CLASS_NOT_FOUND":    "??",
    "SKIPPED_PATTERN_NOT_FOUND":  "NF",
    "NEEDS_MANUAL_RULE":          "MR",
    "FAILED":                     "XX",
}


def _status_icon(s: str) -> str:
    return _STATUS_ICONS.get(s, s[:2])


def _fmt_method_result(mr: MethodPatchResult, indent: str = "      ") -> str:
    icon = _status_icon(mr.status.value)
    sig = mr.method_sig or mr.field_decl or mr.class_name
    msg = f"  ({mr.message})" if mr.message else ""
    return f"{indent}[{icon}] {sig}{msg}"


def _fmt_stage(label: str, stage: dict | None) -> list[str]:
    lines: list[str] = [f"  {label}:"]
    if stage is None:
        lines.append("    (not set)")
        return lines
    lines.append(f"    Status  : {stage.get('status', '?')}")
    lines.append(f"    Module  : {stage.get('module', '?')}")
    for w in stage.get("warnings", []):
        lines.append(f"    ! {w}")
    for e in stage.get("errors", []):
        lines.append(f"    X {e}")
    return lines


def format_text_report(session: PatchSession) -> str:
    mode = "DRY RUN" if session.dry_run else "EXECUTE"
    lines: list[str] = [
        f"DeadZone Legend JAR Patch Report  [{mode}]",
        "=" * 60,
        f"Final status  : {_session_final_status(session)}",
        f"Flavor        : {session.flavor}",
        f"Android major : {session.android_major if session.android_major is not None else '(not specified)'}",
        f"Dry run       : {session.dry_run}",
        f"Backup policy : disabled",
        f"Project       : {session.project_dir}",
        f"Work dir      : {session.work_dir}",
        f"Patch dir     : {session.patch_dir}",
        "",
        "Target JARs:",
    ]

    for jr in session.jar_reports:
        found_str = "FOUND" if jr.found else "NOT FOUND"
        lines.append(f"  JAR: {jr.jar_name}  [{found_str}]")
        lines.append(f"    Partition path : {jr.jar_partition_path}")

        if jr.found:
            lines.append(f"    Decompile      : {'OK' if jr.decompile_ok else 'FAILED'}")
            for e in jr.decompile_errors:
                lines.append(f"      ! {e}")

            for adr in jr.add_dex_reports:
                dex_name = Path(adr.dex_path).name
                lines.append(f"    add.dex: {dex_name}  ->  {adr.target_jar}")
                lines.append(f"      Valid DEX  : {adr.dex_valid}")
                lines.append(f"      Decompiled : {adr.decompiled}")
                lines.append(f"      Classes    : {adr.class_count}  Merged: {adr.merged_count}  Conflicts: {adr.conflict_count}")
                if adr.smali_root:
                    lines.append(f"      Smali root : {adr.smali_root}")
                for r in adr.class_results:
                    lines.append(_fmt_method_result(r, indent="      "))
                for e in adr.errors:
                    lines.append(f"      ! {e}")

            for mr in jr.mtcr_reports:
                lines.append(f"    MTCR pack: {mr.mtcr_name}")
                current_class: str | None = None
                for res in mr.method_results:
                    if res.class_name != current_class:
                        current_class = res.class_name
                        lines.append(f"      Class: {current_class}")
                    lines.append(_fmt_method_result(res, indent="        "))

            lines.append(f"    Repack         : {'OK' if jr.repack_ok else 'FAILED'}")
            for e in jr.repack_errors:
                lines.append(f"      ! {e}")

            if not session.dry_run:
                lines.append(f"    Replace (no bak): {'OK' if jr.restore_ok else 'FAILED'}")
                if jr.restore_error:
                    lines.append(f"      ! {jr.restore_error}")

        lines.append("")

    lines.append("Cross-JAR stages:")
    lines.extend(_fmt_stage("Signature bypass", session.signature_bypass_stage))
    lines.extend(_fmt_stage("JAR misc legacy", session.jar_misc_legacy_stage))
    lines.extend(_fmt_stage("Kaori legacy", session.kaori_legacy_stage))

    lines.append("")
    lines.append("Warnings:")
    if session.warnings:
        for w in session.warnings:
            lines.append(f"  ! {w}")
    else:
        lines.append("  (none)")

    lines.append("")
    lines.append("Errors:")
    if session.errors:
        for e in session.errors:
            lines.append(f"  X {e}")
    else:
        lines.append("  (none)")

    lines.append("")
    return "\n".join(lines)


# -- Write -
def write_reports(session: PatchSession, reports_dir: Path) -> tuple[Path, Path]:
    reports_dir.mkdir(parents=True, exist_ok=True)

    json_path = reports_dir / _REPORT_JSON
    txt_path  = reports_dir / _REPORT_TXT

    data = session_to_dict(session)
    json_path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False, default=str),
        encoding="utf-8",
    )
    txt_path.write_text(format_text_report(session), encoding="utf-8")

    print(f"[patch_report] JSON: {json_path}")
    print(f"[patch_report] TXT : {txt_path}")
    return json_path, txt_path
