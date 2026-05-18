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
    jar_reports: list[JarReport] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)


# ── Serialise ─────────────────────────────────────────────────────────────────
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
        "restore_ok": jr.restore_ok,
        "backup_path": str(jr.backup_path) if jr.backup_path else None,
        "restore_error": jr.restore_error,
        "add_dex": [_add_dex_result_to_dict(a) for a in jr.add_dex_reports],
        "mtcr_packs": [_mtcr_report_to_dict(m) for m in jr.mtcr_reports],
    }


def session_to_dict(session: PatchSession) -> dict:
    return {
        "flavor": session.flavor,
        "dry_run": session.dry_run,
        "project_dir": str(session.project_dir),
        "work_dir": str(session.work_dir),
        "patch_dir": str(session.patch_dir),
        "jars": [_jar_report_to_dict(jr) for jr in session.jar_reports],
        "warnings": session.warnings,
        "errors": session.errors,
    }


# ── Text format ───────────────────────────────────────────────────────────────
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


def format_text_report(session: PatchSession) -> str:
    mode = "DRY RUN" if session.dry_run else "EXECUTE"
    lines: list[str] = [
        f"DeadZone Legend JAR Patch Report  [{mode}]",
        "=" * 60,
        f"Flavor:       {session.flavor}",
        f"Dry run:      {session.dry_run}",
        f"Project:      {session.project_dir}",
        f"Work dir:     {session.work_dir}",
        f"Patch dir:    {session.patch_dir}",
        "",
    ]

    for jr in session.jar_reports:
        found_str = "FOUND" if jr.found else "NOT FOUND"
        lines.append(f"JAR: {jr.jar_name}  [{found_str}]")
        lines.append(f"  Partition path: {jr.jar_partition_path}")

        if jr.found:
            lines.append(f"  Decompile: {'OK' if jr.decompile_ok else 'FAILED'}")
            for e in jr.decompile_errors:
                lines.append(f"    ! {e}")

            # add.dex results
            for adr in jr.add_dex_reports:
                dex_name = Path(adr.dex_path).name
                lines.append(f"  add.dex: {dex_name}  ->  {adr.target_jar}")
                lines.append(f"    Valid DEX:  {adr.dex_valid}")
                lines.append(f"    Decompiled: {adr.decompiled}")
                lines.append(f"    Classes:    {adr.class_count}  "
                              f"Merged: {adr.merged_count}  "
                              f"Conflicts: {adr.conflict_count}")
                if adr.smali_root:
                    lines.append(f"    Smali root: {adr.smali_root}")
                for r in adr.class_results:
                    lines.append(_fmt_method_result(r, indent="    "))
                for e in adr.errors:
                    lines.append(f"    ! {e}")

            # MTCR results
            for mr in jr.mtcr_reports:
                lines.append(f"  MTCR pack: {mr.mtcr_name}")
                # Group by class for readability
                current_class: str | None = None
                for res in mr.method_results:
                    if res.class_name != current_class:
                        current_class = res.class_name
                        lines.append(f"    Class: {current_class}")
                    lines.append(_fmt_method_result(res, indent="      "))

            lines.append(f"  Repack:    {'OK' if jr.repack_ok else 'FAILED'}")
            for e in jr.repack_errors:
                lines.append(f"    ! {e}")

            if not session.dry_run:
                lines.append(f"  Restore:   {'OK' if jr.restore_ok else 'FAILED'}")
                if jr.backup_path:
                    lines.append(f"  Backup:    {jr.backup_path}")
                if jr.restore_error:
                    lines.append(f"    ! {jr.restore_error}")

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


# ── Write ─────────────────────────────────────────────────────────────────────
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
