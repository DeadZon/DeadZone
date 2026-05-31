"""
DeadZone — Partition Modification Tracking.

Records which dynamic partitions were *actually* modified by a build stage so
that the repacker only rebuilds partitions whose content changed.  A partition
folder existing under ws.partitions/ is NOT proof of modification — the pipeline
extracts every partition for inspection.  Modification is recorded explicitly by
the stages that change files (app rename/delete, debloat, overlay copy, etc.).

Manifest (ws.meta/partition_modifications.json):

    {
      "schema": 1,
      "partitions": {
        "product": {
          "partition": "product",
          "modified": true,
          "index": 0,
          "stages": ["stable_partition_rebuild"],
          "reasons": ["stable app policy changed product"],
          "files_changed": [...],
          "files_added": [...],
          "files_removed": [...],
          "notes": ""
        }
      },
      "modified_partitions": ["product"]
    }

The per-partition ``index`` is a deterministic counter assigned in the order
partitions are first marked, so reports and tests are stable.

All public functions take a Workspace.  No partition is ever marked modified by
read-only scans, inventory generation, package scanning, metadata reads, or
validation — only by stages that change files on disk.
"""
from __future__ import annotations

from typing import Any, Iterable, Mapping

from factory.core.workspace import Workspace, read_json, write_json

MANIFEST_NAME = "partition_modifications.json"
SCHEMA_VERSION = 1


def _manifest_path(ws: Workspace):
    return ws.meta / MANIFEST_NAME


def _empty_manifest() -> dict[str, Any]:
    return {"schema": SCHEMA_VERSION, "partitions": {}, "modified_partitions": []}


def load_partition_modifications(ws: Workspace) -> dict[str, Any]:
    """Load the modification manifest, returning an empty manifest if absent."""
    data = read_json(_manifest_path(ws), {})
    if not isinstance(data, dict):
        return _empty_manifest()
    partitions = data.get("partitions")
    if not isinstance(partitions, dict):
        return _empty_manifest()
    data.setdefault("schema", SCHEMA_VERSION)
    data["modified_partitions"] = sorted(
        name for name, entry in partitions.items()
        if isinstance(entry, dict) and entry.get("modified")
    )
    return data


def save_partition_modifications(ws: Workspace, manifest: Mapping[str, Any]) -> None:
    """Persist the modification manifest to ws.meta/partition_modifications.json."""
    data = dict(manifest)
    partitions = data.get("partitions")
    if not isinstance(partitions, dict):
        partitions = {}
        data["partitions"] = partitions
    data["schema"] = SCHEMA_VERSION
    data["modified_partitions"] = sorted(
        name for name, entry in partitions.items()
        if isinstance(entry, dict) and entry.get("modified")
    )
    write_json(_manifest_path(ws), data)


def _normalize_files(files: Any) -> dict[str, list[str]]:
    """Coerce the *files* argument into changed/added/removed string lists."""
    changed: list[str] = []
    added: list[str] = []
    removed: list[str] = []
    if files is None:
        pass
    elif isinstance(files, Mapping):
        changed = [str(f) for f in (files.get("changed") or [])]
        added = [str(f) for f in (files.get("added") or [])]
        removed = [str(f) for f in (files.get("removed") or [])]
    elif isinstance(files, (str, bytes)):
        changed = [str(files)]
    elif isinstance(files, Iterable):
        changed = [str(f) for f in files]
    return {"changed": changed, "added": added, "removed": removed}


def _merge_unique(existing: list[str], extra: Iterable[str]) -> list[str]:
    seen = set(existing)
    merged = list(existing)
    for item in extra:
        if item not in seen:
            seen.add(item)
            merged.append(item)
    return merged


def mark_partition_modified(
    ws: Workspace,
    partition: str,
    reason: str,
    stage: str | None = None,
    files: Any = None,
) -> dict[str, Any]:
    """Record that *partition* was modified by a stage.

    Safe to call repeatedly: stages, reasons and file lists accumulate without
    duplicates, and the deterministic ``index`` is assigned only on first mark.
    Returns the partition's manifest entry.
    """
    partition = str(partition)
    manifest = load_partition_modifications(ws)
    partitions: dict[str, Any] = manifest.setdefault("partitions", {})

    entry = partitions.get(partition)
    if not isinstance(entry, dict):
        entry = {
            "partition": partition,
            "modified": True,
            "index": len(partitions),
            "stages": [],
            "reasons": [],
            "files_changed": [],
            "files_added": [],
            "files_removed": [],
            "notes": "",
        }
        partitions[partition] = entry

    entry["modified"] = True
    if stage:
        entry["stages"] = _merge_unique(entry.get("stages") or [], [str(stage)])
    if reason:
        entry["reasons"] = _merge_unique(entry.get("reasons") or [], [str(reason)])

    norm = _normalize_files(files)
    entry["files_changed"] = _merge_unique(entry.get("files_changed") or [], norm["changed"])
    entry["files_added"] = _merge_unique(entry.get("files_added") or [], norm["added"])
    entry["files_removed"] = _merge_unique(entry.get("files_removed") or [], norm["removed"])

    save_partition_modifications(ws, manifest)
    return entry


def is_partition_modified(ws: Workspace, partition: str) -> bool:
    """Return True only if *partition* was explicitly marked modified."""
    manifest = load_partition_modifications(ws)
    entry = manifest.get("partitions", {}).get(str(partition))
    return bool(isinstance(entry, dict) and entry.get("modified"))


def get_partition_modification(ws: Workspace, partition: str) -> dict[str, Any]:
    """Return the manifest entry for *partition*, or an empty dict if unmarked."""
    manifest = load_partition_modifications(ws)
    entry = manifest.get("partitions", {}).get(str(partition))
    return dict(entry) if isinstance(entry, dict) else {}


def list_modified_partitions(ws: Workspace) -> list[str]:
    """Return the sorted list of partitions explicitly marked modified."""
    return list(load_partition_modifications(ws).get("modified_partitions") or [])
