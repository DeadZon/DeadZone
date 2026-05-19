"""Legacy-compatible partition discovery and config sync for EROFS repack."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from factory.repack.erofs_legacy import repack_erofs_legacy

_REPO_ROOT = Path(__file__).resolve().parents[2]
_LEGACY_ROOT = _REPO_ROOT / "third_party" / "mezo_core"
_LEGACY_SRC = _LEGACY_ROOT / "src"
_CONTEXT_RULES_FILE = _LEGACY_ROOT / "bin" / "context_rules.json"

if str(_LEGACY_SRC) not in sys.path:
    sys.path.insert(0, str(_LEGACY_SRC))

from core import contextpatch, fspatch  # type: ignore  # noqa: E402


KNOWN_PARTITIONS = [
    "system",
    "product",
    "system_ext",
    "vendor",
    "vendor_dlkm",
    "system_dlkm",
    "odm",
    "mi_ext",
]


def resolve_partition_root_legacy(project_dir: Path, partition_name: str) -> Path | None:
    direct_root = project_dir / partition_name
    nested_root = direct_root / partition_name

    if nested_root.is_dir():
        return nested_root
    if direct_root.is_dir():
        return direct_root
    return None


def _config_paths(project_dir: Path, partition_name: str) -> tuple[Path, Path]:
    return (
        project_dir / "config" / f"{partition_name}_fs_config",
        project_dir / "config" / f"{partition_name}_file_contexts",
    )


def _read_context_rules() -> dict:
    if not _CONTEXT_RULES_FILE.exists():
        return {}
    try:
        return json.loads(_CONTEXT_RULES_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {}


def sync_partition_configs_legacy(
    project_dir: Path,
    partition_name: str,
    execute: bool = False,
) -> dict:
    """Sync fs_config and file_contexts with the partition directory."""
    project_dir = Path(project_dir).resolve()
    part_dir = resolve_partition_root_legacy(project_dir, partition_name)
    fs_config, file_contexts = _config_paths(project_dir, partition_name)
    warnings: list[str] = []
    errors: list[str] = []

    report = {
        "partition": partition_name,
        "dry_run": not execute,
        "partition_root": str(part_dir) if part_dir else None,
        "fs_config": str(fs_config),
        "file_contexts": str(file_contexts),
        "fs_config_exists": fs_config.exists(),
        "file_contexts_exists": file_contexts.exists(),
        "fs_entries_added": 0,
        "context_entries_added": 0,
        "warnings": warnings,
        "errors": errors,
        "status": "DRY_RUN" if not execute else "PENDING",
    }

    if part_dir is None:
        errors.append(f"Partition directory is missing: {project_dir / partition_name}")
    if not fs_config.exists():
        errors.append(f"fs_config is missing: {fs_config}")
    if not file_contexts.exists():
        errors.append(f"file_contexts is missing: {file_contexts}")

    if not execute:
        report["status"] = "DRY_RUN" if not errors else "FAILED"
        return report

    if errors:
        report["status"] = "FAILED"
        return report

    try:
        current_fs = fspatch.scanfs(str(fs_config.resolve()))
        new_fs, fs_added = fspatch.fs_patch(current_fs, str(part_dir))
        with fs_config.open("w", encoding="utf-8", newline="\n") as file:
            file.writelines(f"{path} {' '.join(new_fs[path])}\n" for path in sorted(new_fs.keys()))
        report["fs_entries_added"] = fs_added

        current_contexts = contextpatch.scan_context(str(file_contexts.resolve()))
        new_contexts, context_added = contextpatch.context_patch(
            current_contexts,
            str(part_dir),
            _read_context_rules(),
        )
        with file_contexts.open("w", encoding="utf-8", newline="\n") as file:
            file.writelines(f"{path} {new_contexts[path]}\n" for path in sorted(new_contexts.keys()))
        report["context_entries_added"] = context_added
        report["status"] = "APPLIED"
    except Exception as exc:
        errors.append(f"Config sync failed for {partition_name}: {exc}")
        report["status"] = "FAILED"

    return report


def repack_single_partition_legacy(
    project_dir: Path,
    images_dir: Path,
    partition_name: str,
    root_dir: Path | None = None,
    execute: bool = False,
) -> dict:
    """Plan or execute repacking one partition image."""
    project_dir = Path(project_dir).resolve()
    images_dir = Path(images_dir).resolve()
    part_dir = resolve_partition_root_legacy(project_dir, partition_name)
    fs_config, file_contexts = _config_paths(project_dir, partition_name)
    output_img = images_dir / f"{partition_name}.img"
    warnings: list[str] = []
    errors: list[str] = []
    skipped_items: list[dict] = []

    if part_dir is None:
        skipped_items.append({"partition": partition_name, "reason": "partition directory missing"})
        return {
            "partition": partition_name,
            "dry_run": not execute,
            "status": "SKIPPED_MISSING_PARTITION",
            "partition_root": None,
            "fs_config": str(fs_config),
            "file_contexts": str(file_contexts),
            "output_img": str(output_img),
            "sync": None,
            "repack": None,
            "commands_planned": [],
            "commands_executed": [],
            "images_created": [],
            "skipped_items": skipped_items,
            "warnings": warnings,
            "errors": errors,
        }

    if not fs_config.exists() or not file_contexts.exists():
        if not fs_config.exists():
            errors.append(f"fs_config is missing: {fs_config}")
        if not file_contexts.exists():
            errors.append(f"file_contexts is missing: {file_contexts}")
        skipped_items.append({"partition": partition_name, "reason": "config files missing"})
        return {
            "partition": partition_name,
            "dry_run": not execute,
            "status": "FAILED",
            "partition_root": str(part_dir),
            "fs_config": str(fs_config),
            "file_contexts": str(file_contexts),
            "output_img": str(output_img),
            "sync": None,
            "repack": None,
            "commands_planned": [],
            "commands_executed": [],
            "images_created": [],
            "skipped_items": skipped_items,
            "warnings": warnings,
            "errors": errors,
        }

    sync_report = sync_partition_configs_legacy(project_dir, partition_name, execute=execute)
    if execute and sync_report.get("errors"):
        errors.extend(sync_report.get("errors", []))
        return {
            "partition": partition_name,
            "dry_run": False,
            "status": "FAILED",
            "partition_root": str(part_dir),
            "fs_config": str(fs_config),
            "file_contexts": str(file_contexts),
            "output_img": str(output_img),
            "sync": sync_report,
            "repack": None,
            "commands_planned": [],
            "commands_executed": [],
            "images_created": [],
            "skipped_items": skipped_items,
            "warnings": warnings,
            "errors": errors,
        }

    repack_report = repack_erofs_legacy(
        partition_name=partition_name,
        partition_root=part_dir,
        output_img=output_img,
        root_dir=root_dir,
        execute=execute,
    )

    warnings.extend(sync_report.get("warnings", []))
    warnings.extend(repack_report.get("warnings", []))
    errors.extend(repack_report.get("errors", []))
    skipped_items.extend(repack_report.get("skipped_items", []))

    status = repack_report.get("status", "FAILED")
    return {
        "partition": partition_name,
        "dry_run": not execute,
        "status": status,
        "partition_root": str(part_dir),
        "fs_config": str(fs_config),
        "file_contexts": str(file_contexts),
        "output_img": str(output_img),
        "sync": sync_report,
        "repack": repack_report,
        "commands_planned": repack_report.get("commands_planned", []),
        "commands_executed": repack_report.get("commands_executed", []),
        "images_created": repack_report.get("images_created", []),
        "skipped_items": skipped_items,
        "warnings": warnings,
        "errors": errors,
    }

