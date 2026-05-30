from __future__ import annotations

import os
import re
from collections import deque
from pathlib import Path
from typing import Any

from factory.core.workspace import Workspace


# ── fs_config scanning ────────────────────────────────────────────────────────

def mezo_scan_fs_config(fs_config_path: Path) -> dict[str, list[str]]:
    """Parse an existing fs_config file into a dict keyed by path entry."""
    config: dict[str, list[str]] = {}
    if not fs_config_path.is_file():
        return config
    with fs_config_path.open("r", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            stripped = line.strip()
            if not stripped:
                continue
            try:
                parts = stripped.split()
                if len(parts) < 2:
                    continue
                filepath = parts[0]
                config[filepath] = parts[1:]
                if len(parts[1:]) > 4:
                    print(f"[FS_CONFIG] Warning: {filepath} has more than 4 fields ({len(parts[1:])}).")
            except Exception as exc:
                print(f"[FS_CONFIG] Warning: skipping malformed line {stripped!r}: {exc}")
    return config


def mezo_is_symlink(file_path: Path) -> str:
    """Return symlink target if path is a symlink, else empty string."""
    if os.name == "nt":
        if not file_path.is_dir():
            try:
                with file_path.open("rb") as fh:
                    if fh.read(10) == b"!<symlink>":
                        return fh.read().decode("utf-16")[:-1]
            except Exception:
                pass
    elif os.name == "posix":
        if file_path.is_symlink():
            try:
                return os.readlink(str(file_path))
            except Exception:
                pass
    return ""


def mezo_scan_partition_dir(folder: Path):
    """Yield all relative path entries in a partition directory, for fs_config comparison.

    Mirrors HyperUR scan_dir logic: yield root name, then all dirs and files
    relative to the folder, using the folder basename as prefix.
    """
    folder_str = str(folder)
    folder_name = folder.name
    if os.name == "nt":
        yield folder_name.replace("\\", "")
    elif os.name == "posix":
        yield folder_name.replace("/", "")
    else:
        yield folder_name

    allfiles = ["/", "/lost+found"]
    for root, dirs, files in os.walk(folder_str, topdown=True):
        for d in sorted(dirs):
            rel = os.path.join(root, d).replace(folder_str, folder_name).replace("\\", "/")
            yield rel
        for f in sorted(files):
            rel = os.path.join(root, f).replace(folder_str, folder_name).replace("\\", "/")
            yield rel
        yield from allfiles


def mezo_patch_fs_config(
    fs_config: dict[str, list[str]],
    folder: Path,
) -> tuple[dict[str, list[str]], int]:
    """Add missing entries to fs_config based on actual directory contents.

    Ported from HyperUR fs_patch() with mezo_ prefix. Core logic is
    identical: walk the directory and assign default permissions for any
    entry not already present in the existing fs_config.
    """
    new_fs: dict[str, list[str]] = {}
    new_add = 0
    seen: deque[str] = deque()
    folder_parent = folder.parent

    print(f"[FS_CONFIG] Patching: {folder.name} — original entries: {len(fs_config)}")

    for entry in mezo_scan_partition_dir(folder):
        if not entry.isprintable():
            clean = ""
            for ch in entry:
                clean += ch if ch.isprintable() else "*"
            entry = clean.replace(" ", "*")

        if entry in fs_config:
            new_fs[entry] = fs_config[entry]
            continue

        if entry in seen:
            continue

        file_path = folder_parent / entry.replace("/", os.sep)

        if file_path.is_dir():
            gid = "2000" if (
                "system/bin" in entry
                or "system/xbin" in entry
                or "vendor/bin" in entry
            ) else "0"
            config = ["0", gid, "0755"]
        elif not file_path.exists():
            config = ["0", "0", "0755"]
        else:
            link_target = mezo_is_symlink(file_path)
            if link_target:
                gid = "2000" if (
                    "system/bin" in entry
                    or "system/xbin" in entry
                    or "vendor/bin" in entry
                ) else "0"
                if "/bin" in entry or "/xbin" in entry:
                    mode = "0755"
                elif ".sh" in entry:
                    mode = "0750"
                else:
                    mode = "0644"
                config = ["0", gid, mode, link_target]
            elif "/bin" in entry or "/xbin" in entry:
                gid = "2000" if (
                    "system/bin" in entry
                    or "system/xbin" in entry
                    or "vendor/bin" in entry
                ) else "0"
                mode = "0750" if ".sh" in entry else "0755"
                config = ["0", gid, mode]
            else:
                config = ["0", "0", "0644"]

        print(f"[FS_CONFIG] Add: [{entry} {config}]")
        seen.append(entry)
        new_add += 1
        new_fs[entry] = config

    return new_fs, new_add


def mezo_write_fs_config(fs_config: dict[str, list[str]], fs_config_path: Path) -> None:
    """Write updated fs_config entries to file, sorted by path."""
    fs_config_path.parent.mkdir(parents=True, exist_ok=True)
    with fs_config_path.open("w", encoding="utf-8", newline="\n") as fh:
        for path_entry in sorted(fs_config.keys()):
            fh.write(f"{path_entry} {' '.join(fs_config[path_entry])}\n")


def mezo_regenerate_fs_config(partition_dir: Path, fs_config_path: Path) -> dict[str, Any]:
    """Update fs_config for a partition directory, adding entries for any missing files."""
    existing = mezo_scan_fs_config(fs_config_path)
    before_count = len(existing)
    updated, added = mezo_patch_fs_config(existing, partition_dir)
    mezo_write_fs_config(updated, fs_config_path)
    print(f"[FS_CONFIG] Updated {fs_config_path.name}: before={before_count} added={added} after={len(updated)}")
    return {
        "partition": partition_dir.name,
        "fs_config_path": str(fs_config_path),
        "entries_before": before_count,
        "entries_added": added,
        "entries_after": len(updated),
    }


# ── file_contexts scanning ────────────────────────────────────────────────────

def mezo_scan_file_contexts(file_contexts_path: Path) -> dict[str, str]:
    """Parse an existing file_contexts file into a dict keyed by path pattern."""
    contexts: dict[str, str] = {}
    if not file_contexts_path.is_file():
        return contexts
    with file_contexts_path.open("r", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            parts = stripped.split(None, 1)
            if len(parts) == 2:
                contexts[parts[0]] = parts[1]
    return contexts


def mezo_regenerate_file_contexts(partition_dir: Path, file_contexts_path: Path) -> dict[str, Any]:
    """Update file_contexts for a partition, adding default labels for missing entries."""
    existing = mezo_scan_file_contexts(file_contexts_path)
    before_count = len(existing)
    added = 0
    partition_name = partition_dir.name

    for entry in mezo_scan_partition_dir(partition_dir):
        if entry in ("/", "/lost+found"):
            continue
        rel_path = ("/" + entry.replace(partition_name + "/", "", 1).lstrip("/"))
        pattern = re.escape(rel_path)
        if pattern not in existing:
            existing[pattern] = "u:object_r:system_file:s0"
            added += 1

    if file_contexts_path.is_file() or added:
        file_contexts_path.parent.mkdir(parents=True, exist_ok=True)
        with file_contexts_path.open("w", encoding="utf-8", newline="\n") as fh:
            for path_pattern, label in sorted(existing.items()):
                fh.write(f"{path_pattern} {label}\n")

    print(f"[FILE_CONTEXTS] Updated {file_contexts_path.name}: before={before_count} added={added} after={len(existing)}")
    return {
        "partition": partition_name,
        "file_contexts_path": str(file_contexts_path),
        "entries_before": before_count,
        "entries_added": added,
        "entries_after": len(existing),
    }


# ── pipeline entry ────────────────────────────────────────────────────────────

def mezo_regenerate_fs_metadata(
    ws: Workspace,
    partition_name: str,
    partition_dir: Path,
) -> dict[str, Any]:
    """Regenerate both fs_config and file_contexts for a partition after extraction.

    Looks for fs_config and file_contexts inside the extracted partition tree
    first, then falls back to the workspace partitions directory.
    Only runs if the partition directory actually exists.
    """
    if not partition_dir.is_dir():
        return {
            "partition": partition_name,
            "status": "skipped",
            "reason": "partition directory not found",
        }

    fs_config_path = partition_dir / "fs_config"
    if not fs_config_path.is_file():
        fs_config_path = ws.partitions / partition_name / "fs_config"

    file_contexts_path = partition_dir / "file_contexts"
    if not file_contexts_path.is_file():
        file_contexts_path = ws.partitions / partition_name / "file_contexts"

    try:
        fs_result = mezo_regenerate_fs_config(partition_dir, fs_config_path)
    except Exception as exc:
        fs_result = {"partition": partition_name, "error": str(exc)}

    try:
        fc_result = mezo_regenerate_file_contexts(partition_dir, file_contexts_path)
    except Exception as exc:
        fc_result = {"partition": partition_name, "error": str(exc)}

    return {
        "partition": partition_name,
        "status": "ok",
        "fs_config": fs_result,
        "file_contexts": fc_result,
    }
