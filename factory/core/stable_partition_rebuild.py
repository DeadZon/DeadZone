from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path
from typing import Any

from factory.core.image_extractor import _detect_format
from factory.core.toolchain import resolve_toolchain
from factory.core.workspace import Workspace, read_json, write_json


class StablePartitionRebuildError(RuntimeError):
    def __init__(self, payload: dict[str, Any]):
        self.payload = payload
        super().__init__(json.dumps(payload, sort_keys=True))


def _image_for_partition(ws: Workspace, partition: str) -> Path:
    candidates = [
        ws.images / f"{partition}.img",
        ws.images / f"{partition}_a.img",
    ]
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    return candidates[0]


def _tree_size(path: Path) -> int:
    total = 0
    if not path.exists():
        return total
    for item in path.rglob("*"):
        if item.is_file():
            try:
                total += item.stat().st_size
            except OSError:
                continue
    return total


def _env_bool(name: str, default: bool = False) -> bool:
    raw = os.environ.get(name, "").strip().lower()
    if not raw:
        return default
    return raw in {"1", "true", "yes", "on"}


def _env_int(name: str, default: int) -> int:
    raw = os.environ.get(name, "").strip()
    if not raw:
        return default
    try:
        return int(raw)
    except ValueError:
        return default


def _error(error_type: str, cause: str, suggested_fix: str, suggested_check: str, partition: str = "") -> dict[str, Any]:
    return {
        "error_type": error_type,
        "partition": partition,
        "cause": cause,
        "suggested_fix": suggested_fix,
        "suggested_check": suggested_check,
    }


def _run(command: list[str], log: Path) -> tuple[int, str]:
    log.parent.mkdir(parents=True, exist_ok=True)
    with log.open("a", encoding="utf-8") as fh:
        fh.write("$ " + " ".join(command) + "\n")
        proc = subprocess.run(command, stdout=fh, stderr=subprocess.STDOUT, text=True)
        fh.write(f"exit: {proc.returncode}\n\n")
    return proc.returncode, " ".join(command)


def _erofs_compressors(mkfs: Path) -> list[str]:
    try:
        proc = subprocess.run([str(mkfs), "--help"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=10)
    except Exception:
        return ["lz4hc", "lz4"]
    output = proc.stdout.lower()
    choices: list[str] = []
    if "lz4hc" in output:
        choices.append("lz4hc")
    if "lz4" in output:
        choices.append("lz4")
    return choices or ["lz4"]


def _detect_erofs_compression(image: Path) -> str:
    if not image.is_file():
        return "unknown"
    try:
        sample = image.read_bytes()[:1024 * 1024].lower()
    except OSError:
        return "unknown"
    if b"lz4hc" in sample:
        return "lz4hc"
    if b"lz4" in sample:
        return "lz4"
    return "unknown"


def _mkfs_erofs_commands(mkfs: Path, tmp: Path, tree: Path, original_compression: str) -> list[tuple[list[str], str]]:
    commands: list[tuple[list[str], str]] = []
    if original_compression and original_compression not in {"unknown", "none"}:
        commands.append(([str(mkfs), "-z", original_compression, str(tmp), str(tree)], original_compression))
    for compressor in _erofs_compressors(mkfs):
        if compressor != original_compression:
            commands.append(([str(mkfs), "-z", compressor, str(tmp), str(tree)], compressor))
    commands.append(([str(mkfs), str(tmp), str(tree)], "none"))
    deduped: list[tuple[list[str], str]] = []
    seen: set[tuple[str, ...]] = set()
    for command, compressor in commands:
        key = tuple(command)
        if key not in seen:
            seen.add(key)
            deduped.append((command, compressor))
    return deduped


def _growth_error(partition: str, before: int, after: int) -> dict[str, Any]:
    return _error(
        "REBUILT_IMAGE_TOO_LARGE",
        f"{partition}.img grew from {before} to {after}",
        "Rebuild EROFS with compression/options matching original, reduce more content, or do not rebuild this partition",
        "Check stable_partition_rebuild_report.json and super_profile_report.txt",
        partition,
    )


def _validate_growth(partition: str, before: int, after: int) -> tuple[bool, str]:
    if _env_bool("DEADZONE_ALLOW_REBUILT_IMAGE_GROWTH", False):
        return True, "growth allowed by DEADZONE_ALLOW_REBUILT_IMAGE_GROWTH"
    tolerance = _env_int("DEADZONE_REBUILT_IMAGE_GROWTH_TOLERANCE_MB", 32) * 1024 * 1024
    if after > before + tolerance:
        return False, f"rebuilt image grew by {after - before} bytes, tolerance is {tolerance} bytes"
    return True, "passed"


def _write_report(ws: Workspace, data: dict[str, Any]) -> None:
    ws.reports.mkdir(parents=True, exist_ok=True)
    write_json(ws.reports / "stable_partition_rebuild_report.json", data)
    lines = [
        "DeadZone Stable Partition Rebuild Report",
        "========================================",
        f"status: {data.get('status')}",
        f"changed_partitions: {', '.join(data.get('changed_partitions') or []) or '(none)'}",
        "",
        "partitions:",
    ]
    for item in data.get("partitions") or []:
        lines.append(
            f"  - {item.get('partition')}: {item.get('status')} "
            f"{item.get('original_size')} -> {item.get('rebuilt_size')} "
            f"tool={item.get('tool_used') or '(none)'} compression={item.get('compression_used') or '(none)'}"
        )
    if data.get("error"):
        err = data["error"]
        lines += [
            "",
            "error:",
            f"  error_type: {err.get('error_type')}",
            f"  cause: {err.get('cause')}",
            f"  suggested_fix: {err.get('suggested_fix')}",
            f"  suggested_check: {err.get('suggested_check')}",
        ]
    (ws.reports / "stable_partition_rebuild_report.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def rebuild_stable_partitions(ws: Workspace, policy_report: dict[str, Any] | None = None) -> dict[str, Any]:
    policy = policy_report or read_json(ws.reports / "stable_app_policy_report.json", {})
    changed = sorted(str(p) for p in (policy.get("changed_partitions") or []) if p)
    toolchain = resolve_toolchain(ws)
    entries: list[dict[str, Any]] = []
    data: dict[str, Any] = {"status": "ok", "changed_partitions": changed, "partitions": entries}
    if not changed:
        _write_report(ws, data)
        return data

    for partition in changed:
        tree = ws.partitions / partition
        image = _image_for_partition(ws, partition)
        before = image.stat().st_size if image.is_file() else 0
        fmt, detail = _detect_format(image, toolchain.path("file")) if image.is_file() else ("missing", "partition image missing")
        tmp = ws.images / f".{partition}.rebuilt.img"
        log = ws.logs / f"stable_partition_rebuild_{partition}.log"
        entry = {
            "partition": partition,
            "source_tree": str(tree),
            "image": str(image),
            "detected_format": fmt,
            "fs_type": fmt.replace("raw_", ""),
            "original_size": before,
            "original_used_bytes": _tree_size(tree),
            "compression_detected": _detect_erofs_compression(image) if fmt == "raw_erofs" else "",
            "size_before": before,
            "rebuilt_size": 0,
            "size_after": 0,
            "size_delta": 0,
            "bytes_saved": 0,
            "growth_allowed": _env_bool("DEADZONE_ALLOW_REBUILT_IMAGE_GROWTH", False),
            "tool_used": "",
            "command": "",
            "command_used": "",
            "compression_used": "",
            "validation_status": "pending",
            "errors": [],
            "status": "pending",
        }
        entries.append(entry)
        if not tree.is_dir():
            payload = _error("PARTITION_TREE_MISSING", f"Modified partition tree is missing: {tree}", "Verify image extraction completed before Stable App Policy execution", "stable_package_scan_report and image_extraction_report", partition)
            data.update(status="failed", error=payload)
            entry.update(status="failed", validation_status="failed")
            entry["errors"].append(payload["cause"])
            _write_report(ws, data)
            raise StablePartitionRebuildError(payload)
        if fmt == "raw_erofs":
            mkfs = toolchain.path("mkfs.erofs")
            if not mkfs:
                payload = _error(
                    "PARTITION_REBUILD_TOOL_MISSING",
                    "mkfs.erofs is required to rebuild modified EROFS partitions",
                    "Install erofs-utils or include mkfs.erofs in tools/helper/linux",
                    "Verify mkfs.erofs is available before Stable App Policy execution",
                    partition,
                )
                data.update(status="failed", error=payload)
                entry.update(status="failed", validation_status="failed")
                entry["errors"].append(payload["cause"])
                _write_report(ws, data)
                raise StablePartitionRebuildError(payload)
            best_tmp = tmp
            selected_command = ""
            selected_compression = ""
            last_code = 1
            if best_tmp.exists():
                best_tmp.unlink()
            for command, compression in _mkfs_erofs_commands(mkfs, best_tmp, tree, entry["compression_detected"]):
                if best_tmp.exists():
                    best_tmp.unlink()
                code, command_text = _run(command, log)
                last_code = code
                if code == 0 and best_tmp.is_file():
                    selected_command = command_text
                    selected_compression = compression
                    if best_tmp.stat().st_size <= before:
                        break
            entry.update(tool_used=str(mkfs), command=selected_command, command_used=selected_command, compression_used=selected_compression)
            if last_code != 0 or not best_tmp.is_file():
                payload = _error("PARTITION_REBUILD_FAILED", f"mkfs.erofs failed for {partition}: exit {last_code}", "Check stable_partition_rebuild log and partition tree contents", "stable_partition_rebuild_report", partition)
                data.update(status="failed", error=payload)
                entry["status"] = "failed"
                entry["errors"].append(payload["cause"])
                entry["validation_status"] = "failed"
                _write_report(ws, data)
                raise StablePartitionRebuildError(payload)
        elif fmt == "raw_ext4":
            payload = _error(
                "EXT_PARTITION_REBUILD_NOT_IMPLEMENTED",
                "EXT4 partition rebuild support is not implemented for Stable App Policy changes",
                "Add EXT4 image rebuild support before applying Stable App Policy to EXT4 partitions",
                "stable_partition_rebuild_report",
                partition,
            )
            data.update(status="failed", error=payload)
            entry.update(status="failed", validation_status="failed")
            entry["errors"].append(payload["cause"])
            _write_report(ws, data)
            raise StablePartitionRebuildError(payload)
        else:
            payload = _error("PARTITION_REBUILD_FORMAT_UNKNOWN", f"Cannot rebuild {partition}: {detail}", "Ensure the partition image is a supported EROFS or EXT4 raw image", "image_extraction_report and stable_partition_rebuild_report", partition)
            data.update(status="failed", error=payload)
            entry.update(status="failed", validation_status="failed")
            entry["errors"].append(payload["cause"])
            _write_report(ws, data)
            raise StablePartitionRebuildError(payload)
        after = tmp.stat().st_size
        ok, validation_reason = _validate_growth(partition, before, after)
        entry.update(
            rebuilt_size=after,
            size_after=after,
            size_delta=after - before,
            bytes_saved=max(0, before - after),
            tree_bytes=_tree_size(tree),
            validation_status="passed" if ok else "failed",
        )
        if not ok:
            payload = _growth_error(partition, before, after)
            payload["cause"] = f"{payload['cause']}; {validation_reason}"
            data.update(status="failed", error=payload)
            entry["status"] = "failed"
            entry["errors"].append(payload["cause"])
            _write_report(ws, data)
            if tmp.exists():
                tmp.unlink()
            raise StablePartitionRebuildError(payload)
        if after > before:
            entry["warnings"] = [validation_reason]
        shutil.move(str(tmp), image)
        entry.update(status="rebuilt")

    super_layout = read_json(ws.meta / "super_layout.json", {})
    dynamic = super_layout.get("dynamic_images")
    if isinstance(dynamic, dict):
        for partition in changed:
            image = _image_for_partition(ws, partition)
            if image.is_file():
                dynamic[partition] = str(image)
        write_json(ws.meta / "super_layout.json", super_layout)
    _write_report(ws, data)
    return data
