"""Repack ListMezo-modified partition folders back into .img files.

Pipeline stage: runs after listmezo_free_normalize, before super_execute.
For every partition folder that ListMezo modified in execute mode, this stage
repacks the folder into an EROFS image using the fs_config / file_contexts that
were captured during extraction, then replaces output/work/super_parts/<partition>.img
so that lpmake receives the updated content.

If ANY partition that is present in super_parts fails to repack, the stage
returns FAILED and the build is halted before final_zip.
"""
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path
from typing import Optional

from factory.repack.erofs_legacy import (
    build_erofs_commands_legacy,
    resolve_mkfs_erofs_binary_legacy,
)

_REPACKABLE_PARTITIONS: tuple[str, ...] = (
    "system",
    "product",
    "system_ext",
    "vendor",
    "odm",
    "mi_ext",
)

# Priority-ordered candidate dirs where ListMezo may have placed extracted partitions.
_ROM_ROOT_CANDIDATES: tuple[str, ...] = (
    "listmezo_partitions",
    "unpacked_rom",
    "partitions",
    "extracted_partitions",
)


def _find_listmezo_rom_root(work_dir: Path) -> Optional[Path]:
    """Return the dir under work_dir that holds ListMezo-modified partition folders."""
    for name in _ROM_ROOT_CANDIDATES:
        cand = work_dir / name
        if not cand.is_dir():
            continue
        for part in _REPACKABLE_PARTITIONS:
            p = cand / part
            if p.is_dir():
                try:
                    next(p.iterdir())
                    return cand
                except StopIteration:
                    pass
    return None


def _write_repack_report(
    reports_dir: Path,
    rom_root: Optional[Path],
    rebuilt: dict[str, str],
    failed: dict[str, str],
    skipped: dict[str, str],
    warnings: list[str],
) -> None:
    reports_dir.mkdir(parents=True, exist_ok=True)
    lines = [
        "═══════════════════════════════════════════════════════",
        "  DeadZone — ListMezo Partition Repack Report",
        "═══════════════════════════════════════════════════════",
        f"  ROM root : {rom_root or '(none)'}",
        f"  Rebuilt  : {len(rebuilt)}",
        f"  Failed   : {len(failed)}",
        f"  Skipped  : {len(skipped)}",
        "",
    ]
    if rebuilt:
        lines.append("  Rebuilt:")
        for part, img in sorted(rebuilt.items()):
            lines.append(f"    {part:20s} → {img}")
        lines.append("")
    if failed:
        lines.append("  Failed:")
        for part, reason in sorted(failed.items()):
            lines.append(f"    {part:20s}: {reason}")
        lines.append("")
    if skipped:
        lines.append("  Skipped:")
        for part, reason in sorted(skipped.items()):
            lines.append(f"    {part:20s}: {reason}")
        lines.append("")
    if warnings:
        lines.append("  Warnings:")
        for w in warnings:
            lines.append(f"    {w}")
        lines.append("")
    lines.append("═══════════════════════════════════════════════════════")
    (reports_dir / "repack_listmezo_report.txt").write_text(
        "\n".join(lines), encoding="utf-8"
    )


def run_repack_listmezo_partitions_stage(
    work_dir: Path,
    super_parts_dir: Path,
    reports_dir: Path,
    listmezo_stage_report: Optional[dict] = None,
    execute: bool = True,
) -> dict:
    """
    Repack ListMezo-modified partition folders back into .img files and replace
    super_parts/<partition>.img before super_execute runs lpmake.

    Parameters
    ----------
    work_dir:
        output/work — root of the session workspace.
    super_parts_dir:
        output/work/super_parts — directory holding dynamic partition .img files.
    reports_dir:
        output/reports — destination for repack_listmezo_report.txt.
    listmezo_stage_report:
        Stage report dict from listmezo_free_normalize; used to decide whether
        anything was actually modified (status must be "APPLIED").
    execute:
        False → dry-run, no filesystem changes.

    Returns a stage-report dict:
        status   : APPLIED | SKIPPED | DRY_RUN | FAILED
        rebuilt  : {partition_name: img_path_str}
        failed   : {partition_name: reason}
        skipped  : {partition_name: reason}
        errors   : list[str]
        warnings : list[str]
    """
    _base: dict = {
        "rebuilt": {},
        "failed": {},
        "skipped": {},
        "errors": [],
        "warnings": [],
    }

    if not execute:
        return {**_base, "status": "DRY_RUN"}

    # Only repack when ListMezo actually modified files (execute mode).
    if listmezo_stage_report is not None:
        lm_status = listmezo_stage_report.get("status", "")
        if lm_status != "APPLIED":
            return {
                **_base,
                "status": "SKIPPED",
                "reason": f"listmezo_free_normalize status={lm_status!r} — nothing to repack",
            }

    rom_root = _find_listmezo_rom_root(work_dir)
    if rom_root is None:
        return {
            **_base,
            "status": "SKIPPED",
            "reason": "no extracted partition dirs found under work_dir",
        }

    if not super_parts_dir.is_dir():
        return {
            **_base,
            "status": "SKIPPED",
            "reason": f"super_parts dir not found at {super_parts_dir}",
        }

    config_dir = rom_root / "config"
    mkfs_path = resolve_mkfs_erofs_binary_legacy()

    rebuilt: dict[str, str] = {}
    failed: dict[str, str] = {}
    skipped: dict[str, str] = {}
    warnings: list[str] = []

    for part_name in _REPACKABLE_PARTITIONS:
        part_dir = rom_root / part_name
        if not part_dir.is_dir():
            skipped[part_name] = "partition dir not present in rom_root"
            continue

        target_img = super_parts_dir / f"{part_name}.img"
        if not target_img.is_file():
            # Folder exists but no corresponding img to replace — skip silently.
            skipped[part_name] = "no corresponding img in super_parts"
            continue

        fs_config = config_dir / f"{part_name}_fs_config"
        file_contexts = config_dir / f"{part_name}_file_contexts"

        if not fs_config.is_file():
            failed[part_name] = f"fs_config not found: {fs_config}"
            continue
        if not file_contexts.is_file():
            failed[part_name] = f"file_contexts not found: {file_contexts}"
            continue
        if mkfs_path is None:
            failed[part_name] = "mkfs.erofs not found in bundled bin/ or PATH"
            continue

        tmp_img = super_parts_dir / f"{part_name}_listmezo_rebuilt.img"
        tmp_img.unlink(missing_ok=True)

        cmds = build_erofs_commands_legacy(
            partition_name=part_name,
            partition_root=part_dir,
            output_img=tmp_img,
            fs_config=fs_config,
            file_contexts=file_contexts,
        )

        success = False
        last_err = ""
        for cmd in cmds:
            cmd[0] = str(mkfs_path)
            tmp_img.unlink(missing_ok=True)
            try:
                r = subprocess.run(cmd, capture_output=True, timeout=300)
                if r.returncode == 0 and tmp_img.is_file() and tmp_img.stat().st_size > 0:
                    success = True
                    break
                last_err = r.stderr.decode(errors="replace").strip()
            except Exception as exc:
                last_err = str(exc)

        if not success:
            tmp_img.unlink(missing_ok=True)
            failed[part_name] = f"mkfs.erofs failed: {last_err[:300]}"
            continue

        # Atomically replace the super_parts image.
        target_img.unlink(missing_ok=True)
        shutil.move(str(tmp_img), str(target_img))
        rebuilt[part_name] = str(target_img)
        print(f"[repack_listmezo] {part_name}.img rebuilt → {target_img}")

    _write_repack_report(reports_dir, rom_root, rebuilt, failed, skipped, warnings)

    if failed:
        return {
            **_base,
            "status": "FAILED",
            "rebuilt": rebuilt,
            "failed": failed,
            "skipped": skipped,
            "errors": [f"Partition repack failed for: {', '.join(sorted(failed))}"],
            "warnings": warnings,
        }

    return {
        **_base,
        "status": "APPLIED" if rebuilt else "SKIPPED",
        "rebuilt": rebuilt,
        "failed": {},
        "skipped": skipped,
        "errors": [],
        "warnings": warnings,
        **({"reason": "no partitions needed repacking"} if not rebuilt else {}),
    }
