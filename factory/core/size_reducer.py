from __future__ import annotations

import fnmatch
import shutil
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Callable

from factory.core.workspace import Workspace, read_json, write_json


LEVELS = ("safe", "balanced", "aggressive")
PARTITIONS = ("system", "system_ext", "product", "vendor", "odm", "mi_ext")
GENERATED_DIRS = {"oat", "arm", "arm64"}
GENERATED_SUFFIXES = {".odex", ".vdex", ".art", ".prof", ".dm"}
APP_SCOPES = {"app", "priv-app", "framework"}


@dataclass(frozen=True)
class ReductionRule:
    name: str
    reason: str
    source: str
    scope: str
    partition: str
    pattern: str
    safety_level: str
    kind: str = "path"

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


def _normalize_level(level: Any) -> str:
    value = str(level or "balanced").strip().lower()
    return value if value in LEVELS else "balanced"


def _level_enabled(rule_level: str, active_level: str) -> bool:
    order = {name: index for index, name in enumerate(LEVELS)}
    return order[_normalize_level(rule_level)] <= order[_normalize_level(active_level)]


def _path_size(path: Path) -> int:
    if path.is_file() or path.is_symlink():
        try:
            return path.stat().st_size
        except OSError:
            return 0
    total = 0
    for item in path.rglob("*"):
        if item.is_file() or item.is_symlink():
            try:
                total += item.stat().st_size
            except OSError:
                continue
    return total


def _tree_size(root: Path) -> int:
    return _path_size(root) if root.exists() else 0


def _relative(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def _in_app_scope(path: Path, root: Path) -> bool:
    parts = set(_relative(path, root).split("/"))
    return bool(parts & APP_SCOPES)


def _empty_dirs(root: Path) -> list[Path]:
    found: list[Path] = []
    for path in sorted((p for p in root.rglob("*") if p.is_dir()), key=lambda p: len(p.parts), reverse=True):
        try:
            if not any(path.iterdir()):
                found.append(path)
        except OSError:
            continue
    return found


def _find_partition_roots(ws: Workspace) -> dict[str, Path]:
    roots: dict[str, Path] = {}
    for base in (ws.partitions, ws.images, ws.extracted):
        for partition in PARTITIONS:
            candidate = base / partition
            if candidate.is_dir() and candidate.exists():
                roots.setdefault(partition, candidate)
    return {name: path for name, path in roots.items() if _is_writable_tree(path)}


def _is_writable_tree(path: Path) -> bool:
    return path.is_dir() and path.exists()


def _builtin_rules() -> list[ReductionRule]:
    rules = [
        ReductionRule(
            name="generated_compile_dirs",
            reason="Remove generated app/runtime compile directories that Android can rebuild.",
            source="universal_core_builtin",
            scope="app_or_framework_dirs",
            partition="*",
            pattern="**/{oat,arm,arm64}",
            safety_level="safe",
            kind="generated_dirs",
        ),
        ReductionRule(
            name="generated_compile_files",
            reason="Remove generated odex/vdex/art/prof/dm artifacts when located in app or framework scopes.",
            source="universal_core_builtin",
            scope="app_or_framework_files",
            partition="*",
            pattern="**/*.{odex,vdex,art,prof,dm}",
            safety_level="safe",
            kind="generated_files",
        ),
        ReductionRule(
            name="cache_dirs",
            reason="Remove cache and temporary working directories.",
            source="universal_core_builtin",
            scope="cache_dirs",
            partition="*",
            pattern="**/{cache,code_cache,dalvik-cache,tmp,temp,.cache}",
            safety_level="safe",
            kind="cache_dirs",
        ),
        ReductionRule(
            name="temporary_files",
            reason="Remove temporary duplicate or editor backup files.",
            source="universal_core_builtin",
            scope="temporary_files",
            partition="*",
            pattern="**/*.{tmp,temp,bak,orig,rej}",
            safety_level="safe",
            kind="temporary_files",
        ),
        ReductionRule(
            name="updater_download_cache",
            reason="Remove updater download cache directories.",
            source="universal_core_builtin",
            scope="updater_cache",
            partition="*",
            pattern="**/{downloaded_rom,ota,ota_package,update_cache}",
            safety_level="safe",
            kind="cache_dirs",
        ),
        ReductionRule(
            name="empty_dirs",
            reason="Remove empty directories left after base cleanup.",
            source="universal_core_builtin",
            scope="empty_dirs",
            partition="*",
            pattern="**/",
            safety_level="safe",
            kind="empty_dirs",
        ),
    ]
    return rules


def _profile_rules(ws: Workspace) -> list[ReductionRule]:
    device = read_json(ws.meta / "device_registry.json", {})
    section = device.get("size_reduction") if isinstance(device.get("size_reduction"), dict) else {}
    raw_rules = section.get("rules") if isinstance(section.get("rules"), list) else []
    rules: list[ReductionRule] = []
    for raw in raw_rules:
        if not isinstance(raw, dict):
            continue
        try:
            rules.append(
                ReductionRule(
                    name=str(raw["name"]),
                    reason=str(raw["reason"]),
                    source=str(raw.get("source") or "profile"),
                    scope=str(raw.get("scope") or "path"),
                    partition=str(raw.get("partition") or "*"),
                    pattern=str(raw["pattern"]),
                    safety_level=_normalize_level(raw.get("safety_level")),
                    kind=str(raw.get("kind") or "profile_path"),
                )
            )
        except KeyError:
            continue
    return rules


def _candidates_for_rule(rule: ReductionRule, root: Path) -> list[Path]:
    if rule.kind == "generated_dirs":
        return [
            path
            for path in root.rglob("*")
            if path.is_dir() and path.name in GENERATED_DIRS and _in_app_scope(path, root)
        ]
    if rule.kind == "generated_files":
        return [
            path
            for path in root.rglob("*")
            if path.is_file() and path.suffix.lower() in GENERATED_SUFFIXES and _in_app_scope(path, root)
        ]
    if rule.kind == "cache_dirs":
        names = {"cache", "code_cache", "dalvik-cache", "tmp", "temp", ".cache", "downloaded_rom", "ota", "ota_package", "update_cache"}
        return [path for path in root.rglob("*") if path.is_dir() and path.name.lower() in names]
    if rule.kind == "temporary_files":
        suffixes = {".tmp", ".temp", ".bak", ".orig", ".rej"}
        return [path for path in root.rglob("*") if path.is_file() and (path.suffix.lower() in suffixes or path.name.endswith("~"))]
    if rule.kind == "empty_dirs":
        return _empty_dirs(root)

    pattern = rule.pattern.strip().lstrip("/")
    matches: list[Path] = []
    for path in root.rglob("*"):
        rel = _relative(path, root)
        if fnmatch.fnmatch(rel, pattern) or fnmatch.fnmatch(path.name, pattern):
            matches.append(path)
    direct = root / pattern
    if direct.exists():
        matches.append(direct)
    return sorted(set(matches), key=lambda p: (len(p.parts), p.as_posix()), reverse=True)


def _remove_path(path: Path) -> None:
    if path.is_dir() and not path.is_symlink():
        shutil.rmtree(path)
    else:
        path.unlink()


def _partition_sizes(roots: dict[str, Path]) -> dict[str, int]:
    return {partition: _tree_size(root) for partition, root in sorted(roots.items())}


def _largest_remaining(roots: dict[str, Path], limit: int = 50) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    for partition, root in roots.items():
        for path in root.rglob("*"):
            if not path.exists():
                continue
            size = _path_size(path)
            if size <= 0:
                continue
            entries.append({
                "partition": partition,
                "path": _relative(path, root),
                "size": size,
                "type": "dir" if path.is_dir() else "file",
            })
    return sorted(entries, key=lambda item: int(item["size"]), reverse=True)[:limit]


def _write_partition_report(ws: Workspace, data: dict[str, Any]) -> None:
    lines = [
        "DeadZone Partition Size Report",
        "==============================",
        f"status: {data.get('status')}",
        "",
        "before/after:",
    ]
    before = data.get("before_partition_sizes") if isinstance(data.get("before_partition_sizes"), dict) else {}
    after = data.get("after_partition_sizes") if isinstance(data.get("after_partition_sizes"), dict) else {}
    for partition in sorted(set(before) | set(after)):
        removed = int(before.get(partition) or 0) - int(after.get(partition) or 0)
        lines.append(f"  - {partition}: before={before.get(partition, 0)} after={after.get(partition, 0)} removed={removed}")
    lines += ["", "largest remaining:"]
    for item in data.get("largest_remaining") or []:
        lines.append(f"  - {item.get('partition')}/{item.get('path')}: {item.get('size')} ({item.get('type')})")
    if not data.get("largest_remaining"):
        lines.append("  (none)")
    (ws.reports / "partition_size_report.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_reduction_report(ws: Workspace, data: dict[str, Any]) -> None:
    write_json(ws.meta / "size_reduction.json", data)
    lines = [
        "DeadZone Size Reduction Report",
        "==============================",
        f"status: {data.get('status')}",
        f"enabled: {data.get('enabled')}",
        f"level: {data.get('level')}",
        f"reason: {data.get('reason') or '(none)'}",
        f"recommendation: {data.get('recommendation') or '(none)'}",
        f"removed files count: {data.get('removed_count')}",
        f"removed bytes: {data.get('removed_bytes')}",
        f"estimated impact on final ZIP: {data.get('estimated_final_zip_impact_bytes')}",
        "",
        "per partition:",
    ]
    per_partition = data.get("removed_bytes_per_partition") if isinstance(data.get("removed_bytes_per_partition"), dict) else {}
    for partition, size in sorted(per_partition.items()):
        lines.append(f"  - {partition}: {size}")
    if not per_partition:
        lines.append("  (none)")
    lines += ["", "skipped rules:"]
    for item in data.get("skipped_rules") or []:
        lines.append(f"  - {item.get('name')}: {item.get('partition')} {item.get('pattern')} ({item.get('reason')})")
    if not data.get("skipped_rules"):
        lines.append("  (none)")
    lines += ["", "removed entries:"]
    for item in data.get("removed") or []:
        lines.append(
            f"  - {item.get('partition')}/{item.get('path')}: {item.get('size')} "
            f"[{item.get('rule_name')}] {item.get('reason')}"
        )
    if not data.get("removed"):
        lines.append("  (none)")
    lines += ["", "largest remaining:"]
    for item in data.get("largest_remaining") or []:
        lines.append(f"  - {item.get('partition')}/{item.get('path')}: {item.get('size')} ({item.get('type')})")
    if not data.get("largest_remaining"):
        lines.append("  (none)")
    (ws.reports / "size_reduction_report.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    _write_partition_report(ws, data)


def _skipped_result(ws: Workspace, enabled: bool, level: str, reason: str) -> dict[str, Any]:
    data: dict[str, Any] = {
        "status": "skipped",
        "enabled": enabled,
        "level": level,
        "reason": reason,
        "recommendation": "implement image mount/extract/rebuild stage for EROFS/EXT partitions",
        "removed": [],
        "removed_count": 0,
        "removed_bytes": 0,
        "removed_bytes_per_partition": {},
        "estimated_final_zip_impact_bytes": 0,
        "before_partition_sizes": {},
        "after_partition_sizes": {},
        "skipped_rules": [],
        "largest_remaining": [],
    }
    _write_reduction_report(ws, data)
    return data


def reduce_workspace_size(
    ws: Workspace,
    *,
    enabled: bool = True,
    level: str = "balanced",
) -> dict[str, Any]:
    active_level = _normalize_level(level)
    if not enabled:
        result = _skipped_result(ws, False, active_level, "size reduction disabled by CLI")
        print(f"[SIZE REDUCTION] Level: {active_level}")
        print("[SIZE REDUCTION] Removed: 0")
        print("[SIZE REDUCTION] Per partition: {}")
        print("[SIZE REDUCTION] Skipped: disabled")
        return result

    roots = _find_partition_roots(ws)
    if not roots:
        result = _skipped_result(ws, True, active_level, "no writable unpacked partition tree available")
        print(f"[SIZE REDUCTION] Level: {active_level}")
        print("[SIZE REDUCTION] Removed: 0")
        print("[SIZE REDUCTION] Per partition: {}")
        print("[SIZE REDUCTION] Skipped: no writable unpacked partition tree available")
        return result

    rules = [rule for rule in [*_builtin_rules(), *_profile_rules(ws)] if _level_enabled(rule.safety_level, active_level)]
    before = _partition_sizes(roots)
    removed: list[dict[str, Any]] = []
    skipped: list[dict[str, Any]] = []
    removed_seen: set[str] = set()

    for rule in rules:
        matching_partitions = [name for name in roots if rule.partition in ("*", name)]
        if not matching_partitions:
            skipped.append({**rule.as_dict(), "reason": "partition not available"})
            continue
        rule_hit = False
        for partition in matching_partitions:
            root = roots[partition]
            candidates = [path for path in _candidates_for_rule(rule, root) if path.exists()]
            if not candidates:
                continue
            for path in candidates:
                key = path.resolve().as_posix()
                if key in removed_seen or not path.exists():
                    continue
                size = _path_size(path)
                entry = {
                    "partition": partition,
                    "path": _relative(path, root),
                    "size": size,
                    "reason": rule.reason,
                    "rule_source": rule.source,
                    "rule_name": rule.name,
                    "scope": rule.scope,
                    "pattern": rule.pattern,
                    "safety_level": rule.safety_level,
                }
                _remove_path(path)
                removed_seen.add(key)
                removed.append(entry)
                rule_hit = True
        if not rule_hit:
            skipped.append({**rule.as_dict(), "reason": "path not present"})

    after = _partition_sizes(roots)
    per_partition: dict[str, int] = {}
    for item in removed:
        partition = str(item["partition"])
        per_partition[partition] = per_partition.get(partition, 0) + int(item["size"])
    total_removed = sum(per_partition.values())
    data = {
        "status": "ran",
        "enabled": True,
        "level": active_level,
        "reason": "",
        "recommendation": "rebuild dynamic partition images from reduced trees before final ZIP",
        "removed": removed,
        "removed_count": len(removed),
        "removed_bytes": total_removed,
        "removed_bytes_per_partition": dict(sorted(per_partition.items())),
        "estimated_final_zip_impact_bytes": total_removed,
        "before_partition_sizes": before,
        "after_partition_sizes": after,
        "skipped_rules": skipped,
        "largest_remaining": _largest_remaining(roots),
        "rules": [rule.as_dict() for rule in rules],
    }
    _write_reduction_report(ws, data)
    print(f"[SIZE REDUCTION] Level: {active_level}")
    print(f"[SIZE REDUCTION] Removed: {total_removed}")
    print(f"[SIZE REDUCTION] Per partition: {data['removed_bytes_per_partition']}")
    print(f"[SIZE REDUCTION] Skipped: {len(skipped)}")
    return data
