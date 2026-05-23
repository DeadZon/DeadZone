"""Report writer for the legacy build pipeline orchestrator."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


REPORT_JSON = "16_legacy_build_pipeline_report.json"
REPORT_TXT = "16_legacy_build_pipeline_report.txt"


def _ascii(value: object) -> str:
    return str(value).encode("ascii", errors="replace").decode("ascii")


def _append_list(lines: list[str], values: object) -> None:
    if not values:
        lines.append("  (none)")
        return
    if not isinstance(values, list):
        values = [values]
    for value in values:
        lines.append(f"  - {_ascii(value)}")


def format_legacy_build_pipeline_report(report: dict[str, Any]) -> str:
    lines = [
        "DeadZone Legacy Build Pipeline Report",
        "====================================",
        f"Stage:               {report.get('stage')}",
        f"Final status:        {report.get('final_status')}",
        f"Dry run:             {report.get('dry_run')}",
        f"Execute:             {report.get('execute')}",
        f"Build name:          {report.get('build_name')}",
        f"Device:              {report.get('device')}",
        f"SoC:                 {report.get('soc')}",
        f"Platform:            {report.get('platform')}",
        f"Flavor:              {report.get('flavor')}",
        f"Android version:     {report.get('android_version')}",
        f"MI incremental:      {report.get('mi_incremental')}",
        f"Project dir:         {report.get('project_dir')}",
        f"ROM path:            {report.get('rom_path')}",
        f"Images dir:          {report.get('images_dir')}",
        f"Output dir:          {report.get('output_dir')}",
        f"Final ZIP:           {report.get('final_zip')}",
        f"Telegram enabled:    {report.get('telegram_enabled')}",
        f"Telegram message id: {report.get('telegram_message_id')}",
        "",
        "Stages:",
    ]
    for stage in report.get("stages") or []:
        lines.append(
            "  [{status}] {name} ({duration:.2f}s)".format(
                status=_ascii(stage.get("status")),
                name=_ascii(stage.get("name")),
                duration=float(stage.get("duration_seconds") or 0.0),
            )
        )
        if stage.get("reason"):
            lines.append(f"    Reason: {_ascii(stage.get('reason'))}")
        if stage.get("report_path"):
            lines.append(f"    Report: {_ascii(stage.get('report_path'))}")
    # ── Legend Runner sub-steps (fstab, debloat, etc.) ──────────────────────────
    legend_runner_report = (report.get("stage_reports") or {}).get("legend_jar")
    if isinstance(legend_runner_report, dict) and "steps" in legend_runner_report:
        lines.append("")
        lines.append("Legend Runner steps:")
        steps: dict = legend_runner_report.get("steps") or {}

        fstab = steps.get("fstab")
        if isinstance(fstab, dict):
            lines.append("  [fstab_patcher]")
            lines.append(f"    found_files       : {fstab.get('found_files', [])}")
            lines.append(f"    patched_files     : {fstab.get('patched_files', [])}")
            lines.append(f"    avb_flags_removed : {fstab.get('avb_flags_removed', 0)}")
            lines.append(f"    overlay_lines_added     : {fstab.get('overlay_lines_added', 0)}")
            lines.append(f"    miui_dlkm_lines_removed : {fstab.get('miui_dlkm_lines_removed', 0)}")
            fstab_status = "APPLIED" if (fstab.get("patched_files") and not fstab.get("dry_run")) \
                else ("DRY_RUN" if fstab.get("dry_run") else "NO_CHANGE")
            lines.append(f"    status            : {fstab_status}")

        debloat = steps.get("debloat")
        if isinstance(debloat, dict):
            lines.append("  [debloat_patcher]")
            lines.append(f"    final_status      : {debloat.get('final_status', 'UNKNOWN')}")
            lines.append(f"    removed_count     : {debloat.get('removed_count', 0)}")
            lines.append(f"    moved_count       : {debloat.get('moved_count', 0)}")
            lines.append(f"    renamed_count     : {debloat.get('renamed_count', 0)}")

        jar = steps.get("jar_mods")
        if isinstance(jar, dict):
            lines.append("  [jar_mods]")
            lines.append(f"    final_status      : {jar.get('final_status', jar.get('status', 'UNKNOWN'))}")

        apk = steps.get("apk_mods")
        if isinstance(apk, dict):
            lines.append("  [apk_mods]")
            lines.append(f"    final_status      : {apk.get('final_status', apk.get('status', 'UNKNOWN'))}")

    # ── Packaging metrics ─────────────────────────────────────────────────────
    lines.append("")
    lines.append("Packaging:")
    lines.append(f"  workspace_images_size_mib : {report.get('workspace_images_size_before_final_packaging_mib')}")
    lines.append(f"  final_zip_size_mib        : {report.get('final_zip_size_mib')}")
    lines.append(f"  super_img_validated       : {report.get('super_img_validated')}")
    fzip_images = report.get("final_zip_image_list") or []
    lines.append(f"  final_zip_images ({len(fzip_images)})    : {fzip_images}")
    excluded = report.get("dynamic_images_excluded_from_final_zip") or []
    lines.append(f"  excluded_dynamic ({len(excluded)})       : {excluded}")

    lines.append("")
    lines.append("Warnings:")
    _append_list(lines, report.get("warnings"))
    lines.append("")
    lines.append("Errors:")
    _append_list(lines, report.get("errors"))
    lines.append("")
    return "\n".join(lines)


def write_legacy_build_pipeline_report(report: dict[str, Any], output_dir: Path) -> dict[str, str]:
    reports_dir = Path(output_dir) / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    json_path = reports_dir / REPORT_JSON
    txt_path = reports_dir / REPORT_TXT
    json_path.write_text(
        json.dumps(report, indent=2, ensure_ascii=True, default=str),
        encoding="utf-8",
        newline="\n",
    )
    txt_path.write_text(
        format_legacy_build_pipeline_report(report),
        encoding="utf-8",
        newline="\n",
    )
    return {"json": str(json_path), "txt": str(txt_path)}

