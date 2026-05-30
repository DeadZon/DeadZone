from __future__ import annotations

import json
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
            f"{item.get('size_before')} -> {item.get('size_after')} "
            f"tool={item.get('tool_used') or '(none)'}"
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
            "size_before": before,
            "size_after": 0,
            "bytes_saved": 0,
            "tool_used": "",
            "command": "",
            "status": "pending",
        }
        entries.append(entry)
        if not tree.is_dir():
            payload = _error("PARTITION_TREE_MISSING", f"Modified partition tree is missing: {tree}", "Verify image extraction completed before Stable App Policy execution", "stable_package_scan_report and image_extraction_report", partition)
            data.update(status="failed", error=payload)
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
                _write_report(ws, data)
                raise StablePartitionRebuildError(payload)
            command = [str(mkfs), str(tmp), str(tree)]
            code, command_text = _run(command, log)
            entry.update(tool_used=str(mkfs), command=command_text)
            if code != 0 or not tmp.is_file():
                payload = _error("PARTITION_REBUILD_FAILED", f"mkfs.erofs failed for {partition}: exit {code}", "Check stable_partition_rebuild log and partition tree contents", "stable_partition_rebuild_report", partition)
                data.update(status="failed", error=payload)
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
            _write_report(ws, data)
            raise StablePartitionRebuildError(payload)
        else:
            payload = _error("PARTITION_REBUILD_FORMAT_UNKNOWN", f"Cannot rebuild {partition}: {detail}", "Ensure the partition image is a supported EROFS or EXT4 raw image", "image_extraction_report and stable_partition_rebuild_report", partition)
            data.update(status="failed", error=payload)
            _write_report(ws, data)
            raise StablePartitionRebuildError(payload)
        shutil.move(str(tmp), image)
        after = image.stat().st_size
        entry.update(status="rebuilt", size_after=after, bytes_saved=max(0, before - after), tree_bytes=_tree_size(tree))

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
