from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path
from typing import Any

from factory.core.detector import DYNAMIC_PARTITIONS, RomInfo
from factory.core.fs_config import mezo_regenerate_fs_metadata
from factory.core.image_extractor import _detect_format
from factory.core.partition_modifications import (
    get_partition_modification,
    is_partition_modified,
)
from factory.core.super_builder import build_super_image
from factory.core.toolchain import resolve_toolchain
from factory.core.workspace import Workspace, write_json


class PartitionRepackError(RuntimeError):
    def __init__(self, payload: dict[str, Any]):
        self.payload = payload
        super().__init__(json.dumps(payload, sort_keys=True))


# ── helpers ───────────────────────────────────────────────────────────────────

def _image_for_partition(ws: Workspace, partition: str) -> Path:
    for name in (f"{partition}.img", f"{partition}_a.img"):
        p = ws.images / name
        if p.is_file():
            return p
    return ws.images / f"{partition}.img"


def _tree_is_non_empty(tree: Path) -> bool:
    if not tree.is_dir():
        return False
    return any(True for p in tree.rglob("*") if p.is_file() or p.is_symlink())


def _run_cmd(command: list[str], log: Path) -> int:
    log.parent.mkdir(parents=True, exist_ok=True)
    with log.open("a", encoding="utf-8") as fh:
        fh.write("$ " + " ".join(str(c) for c in command) + "\n")
        try:
            proc = subprocess.run(command, stdout=fh, stderr=subprocess.STDOUT, text=True)
        except Exception as exc:
            fh.write(f"ERROR: {exc}\n")
            return 127
        fh.write(f"exit: {proc.returncode}\n\n")
    return proc.returncode


# ── EROFS rebuild ─────────────────────────────────────────────────────────────

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


def _erofs_compressors(mkfs: Path) -> list[str]:
    try:
        proc = subprocess.run(
            [str(mkfs), "--help"],
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            text=True, timeout=10,
        )
        output = proc.stdout.lower()
    except Exception:
        return ["lz4hc", "lz4"]
    choices: list[str] = []
    if "lz4hc" in output:
        choices.append("lz4hc")
    if "lz4" in output:
        choices.append("lz4")
    return choices or ["lz4"]


def _rebuild_erofs(
    partition: str,
    tree: Path,
    image: Path,
    mkfs: Path,
    tmp: Path,
    log: Path,
) -> tuple[str, str, str]:
    """Returns (status, command_used, compression_used).

    status is one of: ok | failed
    """
    original_compression = _detect_erofs_compression(image)
    candidates: list[tuple[list[str], str]] = []
    if original_compression not in ("unknown", ""):
        candidates.append(
            ([str(mkfs), "-z", original_compression, str(tmp), str(tree)], original_compression)
        )
    for comp in _erofs_compressors(mkfs):
        if comp != original_compression:
            candidates.append(([str(mkfs), "-z", comp, str(tmp), str(tree)], comp))
    candidates.append(([str(mkfs), str(tmp), str(tree)], "none"))

    # deduplicate while preserving order
    seen: set[tuple[str, ...]] = set()
    deduped: list[tuple[list[str], str]] = []
    for cmd, comp in candidates:
        key = tuple(cmd)
        if key not in seen:
            seen.add(key)
            deduped.append((cmd, comp))

    before = image.stat().st_size if image.is_file() else 0
    selected_cmd = ""
    selected_comp = ""
    last_code = 1

    for cmd, comp in deduped:
        if tmp.exists():
            tmp.unlink()
        code = _run_cmd(cmd, log)
        last_code = code
        if code == 0 and tmp.is_file():
            selected_cmd = " ".join(str(c) for c in cmd)
            selected_comp = comp
            if tmp.stat().st_size <= before:
                break  # best possible result: fits within original size

    if last_code != 0 or not tmp.is_file():
        return "failed", selected_cmd, selected_comp
    return "ok", selected_cmd, selected_comp


# ── EXT4 rebuild ──────────────────────────────────────────────────────────────

def _find_ext4_tool() -> Path | None:
    """Locate make_ext4fs or mke2fs from PATH."""
    for name in ("make_ext4fs", "mke2fs"):
        found = shutil.which(name)
        if found:
            return Path(found)
    return None


def _rebuild_ext4(
    partition: str,
    tree: Path,
    image: Path,
    fs_config_path: Path | None,
    file_contexts_path: Path | None,
    tmp: Path,
    log: Path,
) -> tuple[str, str]:
    """Returns (status, command_used).

    status is one of: ok | failed | failed_no_tool
    """
    tool = _find_ext4_tool()
    if tool is None:
        return "failed_no_tool", ""

    original_size = image.stat().st_size if image.is_file() else 0
    tool_name = tool.name

    if "make_ext4fs" in tool_name:
        cmd = [str(tool), "-l", str(original_size), "-a", f"/{partition}"]
        if fs_config_path and fs_config_path.is_file():
            cmd += ["-C", str(fs_config_path)]
        if file_contexts_path and file_contexts_path.is_file():
            cmd += ["-S", str(file_contexts_path)]
        cmd += [str(tmp), str(tree)]
    else:
        # mke2fs -d: requires e2fsprogs >= 1.43
        block_size = 4096
        block_count = max(1, (original_size + block_size - 1) // block_size)
        cmd = [
            str(tool), "-t", "ext4", "-b", str(block_size),
            "-L", partition,
            "-d", str(tree),
            str(tmp),
            str(block_count),
        ]

    if tmp.exists():
        tmp.unlink()
    code = _run_cmd(cmd, log)
    command_str = " ".join(str(c) for c in cmd)
    if code != 0 or not tmp.is_file():
        return "failed", command_str
    return "ok", command_str


# ── reports ───────────────────────────────────────────────────────────────────

def _write_repack_reports(ws: Workspace, data: dict[str, Any]) -> None:
    ws.reports.mkdir(parents=True, exist_ok=True)
    ws.meta.mkdir(parents=True, exist_ok=True)
    write_json(ws.meta / "partition_repack.json", data)
    lines = [
        "DeadZone Partition Repack Report",
        "================================",
        f"status: {data.get('status')}",
        "",
        "partitions:",
    ]
    for entry in data.get("partitions") or []:
        lines += [
            f"  {entry.get('partition')}:",
            f"    original_image  : {entry.get('original_image')}",
            f"    workspace_folder: {entry.get('workspace_folder')}",
            f"    filesystem_type : {entry.get('filesystem_type')}",
            f"    modified        : {entry.get('modified')}",
            f"    modified_by     : {', '.join(entry.get('modification_stages') or []) or '(none)'}",
            f"    modify_reasons  : {'; '.join(entry.get('modification_reasons') or []) or '(none)'}",
            f"    status          : {entry.get('status')}",
            f"    original_size   : {entry.get('original_size')}",
            f"    rebuilt_size    : {entry.get('rebuilt_size')}",
            f"    command         : {entry.get('command') or '(none)'}",
        ]
        if entry.get("reason"):
            lines.append(f"    reason          : {entry.get('reason')}")
        lines.append("")
    if data.get("failed_partitions"):
        lines += ["failed_partitions:"]
        lines += [f"  - {p}" for p in data["failed_partitions"]]
        lines.append("")
    (ws.reports / "partition_repack_report.txt").write_text(
        "\n".join(lines), encoding="utf-8"
    )


# ── main entry ────────────────────────────────────────────────────────────────

def repack_partitions(ws: Workspace) -> dict[str, Any]:
    """Rebuild only the dynamic partitions that were explicitly modified.

    Modification is driven by ws.meta/partition_modifications.json (written by
    the stages that actually change files — e.g. the Stable app policy), NOT by
    the mere presence of an extracted ws.partitions/{name}/ tree.  The pipeline
    extracts every partition for inspection, so an extracted-but-unmodified
    partition must keep its original image.

    For every dynamic partition:
    - modified → detect FS type from the original image header, repair
      fs_config/file_contexts, then rebuild (status: rebuilt / failed).
    - not modified → the original ws.images/{name}.img is used as-is
      (status: copied), or skipped if neither image nor mods exist.

    Raises PartitionRepackError (blocking super build) if any modified
    partition cannot be rebuilt.
    """
    toolchain = resolve_toolchain(ws)
    entries: list[dict[str, Any]] = []
    failed: list[str] = []

    for partition in sorted(DYNAMIC_PARTITIONS):
        tree = ws.partitions / partition
        image = _image_for_partition(ws, partition)
        original_size = image.stat().st_size if image.is_file() else 0
        modified = is_partition_modified(ws, partition)
        mod_info = get_partition_modification(ws, partition)

        entry: dict[str, Any] = {
            "partition": partition,
            "original_image": str(image),
            "workspace_folder": str(tree),
            "filesystem_type": "unknown",
            "modified": modified,
            "modification_stages": mod_info.get("stages") or [],
            "modification_reasons": mod_info.get("reasons") or [],
            "original_size": original_size,
            "rebuilt_size": 0,
            "command": "",
            "status": "pending",
            "reason": "",
        }
        entries.append(entry)

        if not modified:
            if not image.is_file():
                entry.update(
                    status="skipped",
                    reason="not modified and no original image present",
                )
            else:
                entry.update(
                    status="copied",
                    rebuilt_size=original_size,
                    reason="not modified — original image preserved",
                )
            print(f"[REPACK] {partition}: {entry['status']} (not modified)")
            continue

        # ── modified partition: it must have an extracted tree to rebuild from ──
        if not _tree_is_non_empty(tree):
            entry.update(
                status="failed",
                reason="partition marked modified but no extracted tree to rebuild from",
            )
            failed.append(partition)
            print(f"[REPACK] {partition}: FAILED — marked modified but tree is empty")
            continue

        # ── modified partition: detect FS and rebuild ──────────────────────
        if not image.is_file():
            entry.update(
                status="failed",
                reason="partition marked modified but original image not found — cannot detect filesystem type",
            )
            failed.append(partition)
            print(f"[REPACK] {partition}: FAILED — original image missing")
            continue

        fmt, detail = _detect_format(image, toolchain.path("file"))
        entry["filesystem_type"] = fmt

        print(f"[REPACK] {partition}: detected {fmt} ({detail})")

        # Repair fs_config and file_contexts before packing
        try:
            mezo_regenerate_fs_metadata(ws, partition, tree)
        except Exception as exc:
            print(f"[REPACK] {partition}: fs_metadata repair warning: {exc}")

        # Locate fs_config and file_contexts
        fs_config_path = tree / "fs_config"
        if not fs_config_path.is_file():
            fs_config_path = ws.partitions / partition / "fs_config"
        file_contexts_path = tree / "file_contexts"
        if not file_contexts_path.is_file():
            file_contexts_path = ws.partitions / partition / "file_contexts"

        tmp = ws.images / f".{partition}.repacked.img"
        log = ws.logs / f"repack_{partition}.log"

        if fmt == "raw_erofs":
            mkfs = toolchain.path("mkfs.erofs")
            if mkfs is None:
                entry.update(
                    status="failed",
                    reason=(
                        "mkfs.erofs not found — install erofs-utils or place "
                        "mkfs.erofs in tools/helper/linux"
                    ),
                )
                failed.append(partition)
                print(f"[REPACK] {partition}: FAILED — mkfs.erofs missing")
                continue

            status_code, cmd_used, compression = _rebuild_erofs(
                partition, tree, image, mkfs, tmp, log
            )
            entry["command"] = cmd_used

            if status_code == "failed":
                entry.update(status="failed", reason=f"mkfs.erofs failed; see {log}")
                failed.append(partition)
                if tmp.exists():
                    tmp.unlink()
                print(f"[REPACK] {partition}: FAILED — mkfs.erofs returned error")
                continue

        elif fmt == "raw_ext4":
            status_code, cmd_used = _rebuild_ext4(
                partition, tree, image,
                fs_config_path if fs_config_path.is_file() else None,
                file_contexts_path if file_contexts_path.is_file() else None,
                tmp, log,
            )
            entry["command"] = cmd_used

            if status_code == "failed_no_tool":
                entry.update(
                    status="failed",
                    reason=(
                        "no EXT4 tool available — install make_ext4fs or "
                        "mke2fs (e2fsprogs >= 1.43)"
                    ),
                )
                failed.append(partition)
                print(f"[REPACK] {partition}: FAILED — no EXT4 tool in PATH")
                continue
            elif status_code == "failed":
                entry.update(
                    status="failed",
                    reason=f"EXT4 rebuild failed; see {log}",
                )
                failed.append(partition)
                if tmp.exists():
                    tmp.unlink()
                print(f"[REPACK] {partition}: FAILED — EXT4 tool returned error")
                continue

        else:
            entry.update(
                status="failed",
                reason=f"unsupported filesystem format: {fmt} ({detail})",
            )
            failed.append(partition)
            print(f"[REPACK] {partition}: FAILED — unsupported format {fmt}")
            continue

        if not tmp.is_file():
            entry.update(status="failed", reason="rebuild produced no output file")
            failed.append(partition)
            print(f"[REPACK] {partition}: FAILED — no output produced")
            continue

        rebuilt_size = tmp.stat().st_size
        shutil.move(str(tmp), str(image))
        entry.update(status="rebuilt", rebuilt_size=rebuilt_size)
        print(
            f"[REPACK] {partition}: rebuilt {fmt} "
            f"original={original_size} rebuilt={rebuilt_size}"
        )

    status = "failed" if failed else "ok"
    data: dict[str, Any] = {
        "status": status,
        "partitions": entries,
        "failed_partitions": failed,
    }
    _write_repack_reports(ws, data)

    if failed:
        payload: dict[str, Any] = {
            "error_type": "PARTITION_REPACK_FAILED",
            "failed_partitions": failed,
            "cause": f"Failed to repack modified partitions: {', '.join(failed)}",
            "suggested_fix": (
                "Check partition_repack_report.txt and repack logs in logs/ "
                "for per-partition details"
            ),
        }
        raise PartitionRepackError(payload)

    print(f"[REPACK] all partitions done — {sum(1 for e in entries if e['status'] == 'rebuilt')} rebuilt")
    return data


def build_repacked_super(ws: Workspace, info: RomInfo, inspection: dict[str, Any]) -> dict[str, Any]:
    return build_super_image(ws, info, inspection)
