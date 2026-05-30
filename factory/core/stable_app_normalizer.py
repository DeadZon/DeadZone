"""Stable canonical app normalization — Stage 15.

Compares the extracted partition trees against the canonical app list
(factory/app_registry/stable_canonical_apps.yml) and reports / applies:
  keep       — canonical app found at exact expected path
  rename     — app found with different folder name but matching package
  missing    — canonical app not found in partition trees
  remove     — extra app in managed location not in canonical list
  protected_extra — extra app that is on the protected list (never deleted)
"""
from __future__ import annotations

import json
import shutil
import time
from pathlib import Path
from typing import Any

import yaml

from factory.core.workspace import Workspace, read_json, write_json


# Partitions actively managed by this normalizer
MANAGED_PARTITIONS = ("system", "product", "system_ext")

# Subdirectory names that contain apps within a partition root
APP_CLASS_DIRS = ("app", "priv-app")

# Sub-paths to scan inside each partition root (handles system-as-root layout)
_SCAN_SUBDIRS: dict[str, list[str]] = {
    "system": ["app", "priv-app", "system/app", "system/priv-app"],
    "product": ["app", "priv-app"],
    "system_ext": ["app", "priv-app"],
}

_REGISTRY_PATH = Path("factory/app_registry/stable_canonical_apps.yml")
_PROTECTED_PATH = Path("factory/app_registry/stable_protected_apps.yml")


# ---------------------------------------------------------------------------
# Registry loading
# ---------------------------------------------------------------------------

def _load_registry() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Return (canonical_apps, deferred_build_prop_rules)."""
    if not _REGISTRY_PATH.is_file():
        return [], []
    data: dict[str, Any] = yaml.safe_load(_REGISTRY_PATH.read_text(encoding="utf-8")) or {}
    return data.get("apps") or [], data.get("deferred_build_prop_rules") or []


def _load_protected() -> tuple[set[str], set[str]]:
    """Return (protected_folder_names, protected_package_names)."""
    if not _PROTECTED_PATH.is_file():
        return set(), set()
    data: dict[str, Any] = yaml.safe_load(_PROTECTED_PATH.read_text(encoding="utf-8")) or {}
    folders = {str(x).strip() for x in (data.get("protected") or []) if x}
    packages = {str(x).strip().lower() for x in (data.get("protected_packages") or []) if x}
    return folders, packages


# ---------------------------------------------------------------------------
# Actual app loading
# ---------------------------------------------------------------------------

def _path_size(path: Path) -> int:
    if not path.exists():
        return 0
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


def _scan_partition_for_apps(partition: str, root: Path) -> list[dict[str, Any]]:
    """Scan a single partition tree for app folders containing APKs."""
    apps: list[dict[str, Any]] = []
    seen: set[str] = set()
    for subdir in _SCAN_SUBDIRS.get(partition, ["app", "priv-app"]):
        container = root / subdir
        if not container.is_dir():
            continue
        app_class = "priv-app" if "priv-app" in subdir else "app"
        for folder in sorted(container.iterdir()):
            if not folder.is_dir():
                continue
            key = folder.resolve().as_posix()
            if key in seen:
                continue
            seen.add(key)
            apks = list(folder.rglob("*.apk"))
            if not apks:
                continue
            rel = folder.relative_to(root).as_posix()
            apps.append({
                "partition": partition,
                "name": folder.name,
                "path": rel,
                "absolute_path": str(folder),
                "type": app_class,
                "package_name": "unknown",
                "apk_count": len(apks),
                "size": _path_size(folder),
            })
    return apps


def _load_actual_apps(ws: Workspace) -> list[dict[str, Any]]:
    """Load actual apps from apps_found.json or fallback to direct scan."""
    apps_json = ws.root / "inventory" / "apps_found.json"
    if apps_json.is_file():
        data = read_json(apps_json)
        apps: list[dict[str, Any]] = data.get("apps") or []
        if apps:
            managed = [
                a for a in apps
                if a.get("partition") in MANAGED_PARTITIONS
                and a.get("type") in APP_CLASS_DIRS
            ]
            if managed:
                return managed
    # Fallback: scan partition trees directly
    result: list[dict[str, Any]] = []
    for partition in MANAGED_PARTITIONS:
        root = ws.partitions / partition
        if root.is_dir():
            result.extend(_scan_partition_for_apps(partition, root))
    return result


# ---------------------------------------------------------------------------
# Action computation
# ---------------------------------------------------------------------------

def _is_protected(name: str, pkg: str, protected_folders: set[str], protected_packages: set[str]) -> bool:
    if name in protected_folders:
        return True
    pkg_lower = (pkg or "").lower()
    return bool(pkg_lower and pkg_lower in protected_packages)


def _compute_actions(
    canonical: list[dict[str, Any]],
    actual: list[dict[str, Any]],
    protected_folders: set[str],
    protected_packages: set[str],
) -> dict[str, Any]:
    """Determine keep / rename / missing / remove / protected_extra for each app."""

    # Build lookup maps
    # (partition, type, folder_name) → actual entry
    by_key: dict[tuple[str, str, str], dict[str, Any]] = {}
    # (partition, type, package_lower) → actual entry (for rename detection)
    by_pkg: dict[tuple[str, str, str], dict[str, Any]] = {}

    for app in actual:
        p = app.get("partition", "")
        t = app.get("type", "app")
        n = app.get("name", "")
        pkg = (app.get("package_name") or "").lower()
        key = (p, t, n)
        if key not in by_key:
            by_key[key] = app
        if pkg and pkg != "unknown":
            pkg_key = (p, t, pkg)
            if pkg_key not in by_pkg:
                by_pkg[pkg_key] = app

    matched_abs: set[str] = set()
    kept: list[dict[str, Any]] = []
    renamed: list[dict[str, Any]] = []
    missing: list[dict[str, Any]] = []

    for entry in canonical:
        partition = entry.get("partition", "")
        app_class = entry.get("app_class", "app")
        folder = entry.get("canonical_folder_name", "")
        pkg = (entry.get("package_name") or "").lower()

        lookup_key = (partition, app_class, folder)
        actual_app = by_key.get(lookup_key)

        if actual_app:
            matched_abs.add(actual_app["absolute_path"])
            kept.append({
                "action": "keep",
                "canonical": entry,
                "actual": actual_app,
                "partition": partition,
                "path": actual_app.get("path", ""),
                "absolute_path": actual_app["absolute_path"],
                "size_before": actual_app.get("size", 0),
                "size_after": actual_app.get("size", 0),
                "reason": "exact folder name match",
            })
            continue

        # Try package-name match (rename case)
        if pkg and pkg != "unknown":
            pkg_lookup = (partition, app_class, pkg)
            actual_app = by_pkg.get(pkg_lookup)
            if actual_app and actual_app["absolute_path"] not in matched_abs:
                matched_abs.add(actual_app["absolute_path"])
                renamed.append({
                    "action": "rename",
                    "canonical": entry,
                    "actual": actual_app,
                    "partition": partition,
                    "path": actual_app.get("path", ""),
                    "absolute_path": actual_app["absolute_path"],
                    "size_before": actual_app.get("size", 0),
                    "size_after": actual_app.get("size", 0),
                    "rename_from": actual_app.get("name", ""),
                    "rename_to": folder,
                    "reason": (
                        f"package match: {entry.get('package_name', '')} — "
                        f"folder rename: {actual_app['name']} → {folder}"
                    ),
                    "apk_renamed": False,
                    "apk_rename_skipped": False,
                    "apk_rename_reason": "",
                })
                continue

        missing.append({
            "action": "missing",
            "canonical": entry,
            "actual": None,
            "partition": partition,
            "expected_path": entry.get("expected_path", ""),
            "package_name": entry.get("package_name", ""),
            "reason": "not found in extracted partition trees",
            "size_before": 0,
            "size_after": 0,
        })

    extras: list[dict[str, Any]] = []
    protected_extra: list[dict[str, Any]] = []

    for app in actual:
        if app["absolute_path"] in matched_abs:
            continue
        partition = app.get("partition", "")
        app_type = app.get("type", "app")
        if partition not in MANAGED_PARTITIONS or app_type not in APP_CLASS_DIRS:
            continue
        name = app.get("name", "")
        pkg = app.get("package_name", "unknown")
        if _is_protected(name, pkg, protected_folders, protected_packages):
            protected_extra.append({
                "action": "protected_extra",
                "canonical": None,
                "actual": app,
                "partition": partition,
                "path": app.get("path", ""),
                "absolute_path": app["absolute_path"],
                "size_before": app.get("size", 0),
                "size_after": app.get("size", 0),
                "reason": f"extra but protected: {name} ({pkg})",
            })
        else:
            extras.append({
                "action": "remove",
                "canonical": None,
                "actual": app,
                "partition": partition,
                "path": app.get("path", ""),
                "absolute_path": app["absolute_path"],
                "size_before": app.get("size", 0),
                "size_after": 0,
                "reason": "extra app not in Stable canonical list",
            })

    return {
        "kept": kept,
        "renamed": renamed,
        "missing": missing,
        "extras": extras,
        "protected_extra": protected_extra,
    }


# ---------------------------------------------------------------------------
# Apply actions
# ---------------------------------------------------------------------------

def _apply_renames(renamed: list[dict[str, Any]]) -> None:
    for item in renamed:
        src = Path(item["absolute_path"])
        canonical = item["canonical"]
        target_name = canonical.get("canonical_folder_name", "")
        if not src.exists() or not target_name:
            item["action"] = "rename_skipped"
            item["reason"] += " — source not found"
            continue
        dst = src.parent / target_name
        if dst.exists():
            item["action"] = "rename_skipped"
            item["reason"] += " — destination already exists"
            continue
        try:
            src.rename(dst)
        except OSError as exc:
            item["action"] = "rename_failed"
            item["reason"] += f" — error: {exc}"
            continue
        item["absolute_path"] = str(dst)
        item["size_after"] = item["size_before"]
        # Rename APK if single-APK folder and canonical name provided
        apk_name = canonical.get("canonical_apk_name")
        if apk_name and not canonical.get("multi_apk"):
            apks = list(dst.glob("*.apk"))
            if len(apks) == 1:
                apk_src = apks[0]
                apk_dst = dst / apk_name
                if apk_src != apk_dst:
                    try:
                        apk_src.rename(apk_dst)
                        item["apk_renamed"] = True
                    except OSError as exc:
                        item["apk_rename_skipped"] = True
                        item["apk_rename_reason"] = f"rename error: {exc}"
            else:
                item["apk_rename_skipped"] = True
                item["apk_rename_reason"] = f"split APK ({len(apks)} files) — folder rename only"
        elif canonical.get("multi_apk"):
            item["apk_rename_skipped"] = True
            item["apk_rename_reason"] = "multi_apk — folder rename only per canonical spec"


def _apply_removals(extras: list[dict[str, Any]]) -> None:
    for item in extras:
        folder = Path(item["absolute_path"])
        if not folder.exists():
            item["action"] = "remove_skipped"
            item["reason"] += " — path not found"
            continue
        # Safety: only delete inside managed app paths
        path_str = str(folder)
        safe = any(
            f"/{p}/{c}/" in path_str or path_str.endswith(f"/{p}/{c}")
            for p in MANAGED_PARTITIONS
            for c in APP_CLASS_DIRS
        )
        if not safe:
            item["action"] = "remove_blocked"
            item["reason"] += " — path outside managed app dirs"
            continue
        size = _path_size(folder)
        try:
            if folder.is_dir():
                shutil.rmtree(folder)
            else:
                folder.unlink(missing_ok=True)
            item["action"] = "removed"
            item["removed_size"] = size
        except OSError as exc:
            item["action"] = "remove_failed"
            item["reason"] += f" — error: {exc}"


# ---------------------------------------------------------------------------
# Report writers
# ---------------------------------------------------------------------------

def _inv_path(ws: Workspace) -> Path:
    p = ws.root / "inventory"
    p.mkdir(parents=True, exist_ok=True)
    return p


def _write_list_file(path: Path, items: list[dict[str, Any]], fields: list[str]) -> None:
    lines = []
    for item in items:
        parts = []
        for f in fields:
            v = item.get(f, "")
            if isinstance(v, dict):
                v = v.get("canonical_folder_name") or v.get("name") or ""
            if v is not None:
                parts.append(f"{f}={v}")
        lines.append(" | ".join(str(p) for p in parts))
    path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")


def _format_bytes(n: int) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.1f} {unit}"
        n //= 1024
    return f"{n:.1f} GB"


def _write_reports(ws: Workspace, result: dict[str, Any], deferred_bp: list[dict[str, Any]], mode: str) -> None:
    inv = _inv_path(ws)

    kept = result["kept"]
    renamed = result["renamed"]
    missing = result["missing"]
    extras = result["extras"]
    protected = result["protected_extra"]

    removed_bytes = sum(
        int(item.get("removed_size") or item.get("size_before") or 0)
        for item in extras
        if item.get("action") in ("removed", "remove")
    )
    removed_by_partition: dict[str, int] = {}
    for item in extras:
        if item.get("action") in ("removed", "remove"):
            p = item.get("partition", "unknown")
            removed_by_partition[p] = removed_by_partition.get(p, 0) + int(
                item.get("removed_size") or item.get("size_before") or 0
            )

    # apps_kept.txt
    _write_list_file(
        inv / "apps_kept.txt",
        kept,
        ["partition", "path", "action", "reason"],
    )

    # apps_renamed.txt
    _write_list_file(
        inv / "apps_renamed.txt",
        renamed,
        ["partition", "rename_from", "rename_to", "action", "apk_renamed", "apk_rename_skipped", "apk_rename_reason"],
    )

    # apps_missing.txt
    _write_list_file(
        inv / "apps_missing.txt",
        missing,
        ["partition", "expected_path", "package_name", "action", "reason"],
    )

    # apps_extra.txt (all extras including protected)
    _write_list_file(
        inv / "apps_extra.txt",
        extras + protected,
        ["partition", "path", "action", "size_before", "reason"],
    )

    # apps_removed.txt
    _write_list_file(
        inv / "apps_removed.txt",
        [e for e in extras if e.get("action") in ("removed", "remove")],
        ["partition", "path", "size_before", "action"],
    )

    # stable_app_normalize_report.txt
    report_lines = [
        "DeadZone Stable App Normalization Report",
        "========================================",
        f"mode: {mode}",
        f"source: ListMezo/free/apps.list",
        f"canonical entries: {len(result.get('canonical_count', [0]))}",
        f"kept: {len(kept)}",
        f"renamed: {len(renamed)}",
        f"missing: {len(missing)}",
        f"extras found: {len(extras) + len(protected)}",
        f"  removed: {sum(1 for e in extras if e.get('action') in ('removed', 'remove'))}",
        f"  remove_failed: {sum(1 for e in extras if e.get('action') == 'remove_failed')}",
        f"  remove_blocked: {sum(1 for e in extras if e.get('action') == 'remove_blocked')}",
        f"  protected_extra: {len(protected)}",
        f"removed bytes total: {removed_bytes} ({_format_bytes(removed_bytes)})",
        "",
        "removed bytes by partition:",
    ]
    for p, b in sorted(removed_by_partition.items()):
        report_lines.append(f"  {p}: {b} ({_format_bytes(b)})")

    if removed_by_partition:
        top_removed = sorted(extras, key=lambda x: int(x.get("removed_size") or x.get("size_before") or 0), reverse=True)[:20]
        report_lines += ["", "top removed apps by size:"]
        for item in top_removed:
            sz = int(item.get("removed_size") or item.get("size_before") or 0)
            report_lines.append(f"  {item.get('partition')}/{item.get('path')} — {_format_bytes(sz)}")

    report_lines += ["", "partition rebuild status:"]
    report_lines.append(
        "  Stable normalization planned changes but partition rebuild is not available."
        if mode == "plan"
        else "  Partition rebuild not implemented for EROFS/EXT in this stage."
        "  Deletions applied to extracted partition trees only."
        "  Final ZIP is not yet affected."
    )

    if deferred_bp:
        report_lines += ["", "deferred build.prop rules (not applied this stage):"]
        for rule in deferred_bp:
            report_lines.append(
                f"  [{rule.get('action')}] {rule.get('partition')}/{rule.get('file')}"
                f"  {rule.get('key')}={rule.get('value', '')}"
            )

    if missing:
        report_lines += ["", "missing canonical apps:"]
        for item in missing:
            report_lines.append(
                f"  {item['partition']}/{item.get('expected_path', '')} ({item.get('package_name', '')})"
            )

    if renamed:
        report_lines += ["", "renamed apps:"]
        for item in renamed:
            report_lines.append(
                f"  {item['partition']}: {item.get('rename_from', '')} → {item.get('rename_to', '')} [{item['action']}]"
            )

    if protected:
        report_lines += ["", "protected extras (not deleted):"]
        for item in protected:
            report_lines.append(f"  {item['partition']}/{item.get('path', '')} — {item.get('reason', '')}")

    (ws.reports / "stable_app_normalize_report.txt").write_text(
        "\n".join(report_lines) + "\n", encoding="utf-8"
    )

    # stable_app_normalize.json (machine-readable)
    json_data: dict[str, Any] = {
        "feature": "Stable App Normalization",
        "source": "ListMezo/free/apps.list",
        "mode": mode,
        "kept_count": len(kept),
        "renamed_count": len(renamed),
        "missing_count": len(missing),
        "extras_count": len(extras),
        "protected_extra_count": len(protected),
        "removed_count": sum(1 for e in extras if e.get("action") in ("removed", "remove")),
        "removed_bytes_total": removed_bytes,
        "removed_bytes_by_partition": removed_by_partition,
        "partition_rebuild_available": False,
        "final_zip_affected": False,
        "deferred_build_prop_rules": deferred_bp,
        "kept": [
            {
                "partition": i["partition"],
                "path": i.get("path", ""),
                "action": i["action"],
            }
            for i in kept
        ],
        "renamed": [
            {
                "partition": i["partition"],
                "rename_from": i.get("rename_from", ""),
                "rename_to": i.get("rename_to", ""),
                "action": i["action"],
                "apk_renamed": i.get("apk_renamed", False),
            }
            for i in renamed
        ],
        "missing": [
            {
                "partition": i["partition"],
                "expected_path": i.get("expected_path", ""),
                "package_name": i.get("package_name", ""),
            }
            for i in missing
        ],
        "extras": [
            {
                "partition": i["partition"],
                "path": i.get("path", ""),
                "action": i["action"],
                "size_before": i.get("size_before", 0),
                "removed_size": i.get("removed_size", 0),
            }
            for i in extras
        ],
        "protected_extra": [
            {
                "partition": i["partition"],
                "path": i.get("path", ""),
                "reason": i.get("reason", ""),
            }
            for i in protected
        ],
    }
    write_json(ws.meta / "stable_app_normalize.json", json_data)


# ---------------------------------------------------------------------------
# Console summary
# ---------------------------------------------------------------------------

def _print_summary(canonical_count: int, result: dict[str, Any], removed_bytes: int) -> None:
    kept = result["kept"]
    renamed = result["renamed"]
    missing = result["missing"]
    extras = result["extras"]
    protected = result["protected_extra"]
    removed_count = sum(1 for e in extras if e.get("action") in ("removed", "remove"))
    print(f"[STABLE APPS] Canonical entries: {canonical_count}")
    print(f"[STABLE APPS] Kept:              {len(kept)}")
    print(f"[STABLE APPS] Removed extras:    {removed_count}")
    print(f"[STABLE APPS] Renamed:           {len(renamed)}")
    print(f"[STABLE APPS] Missing:           {len(missing)}")
    print(f"[STABLE APPS] Protected:         {len(protected)}")
    print(f"[STABLE APPS] Removed bytes:     {removed_bytes} ({_format_bytes(removed_bytes)})")
    if not result.get("_partition_rebuild_available"):
        print(
            "[STABLE APPS] Partition rebuild: NOT available — "
            "final ZIP is not affected by this stage yet"
        )


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------

def normalize_stable_apps(
    ws: Workspace,
    style: str = "stable",
    mode: str = "apply",
) -> dict[str, Any]:
    """Run Stable canonical app normalization.

    Args:
        ws:    Workspace instance.
        style: ROM style key (normalizer only active for 'stable').
        mode:  'apply' executes renames and deletions;
               'plan'  computes and reports without touching files.

    Returns:
        Result dict with kept/renamed/missing/extras/protected_extra.
    """
    started = time.monotonic()

    if style.lower() not in ("stable",):
        msg = f"Stable app normalization is disabled for style '{style}' in this stage."
        print(f"[STABLE APPS] {msg}")
        ws.reports.mkdir(parents=True, exist_ok=True)
        (ws.reports / "stable_app_normalize_report.txt").write_text(
            f"Stable App Normalization\nskipped: {msg}\n", encoding="utf-8"
        )
        return {"skipped": True, "reason": msg}

    canonical, deferred_bp = _load_registry()
    protected_folders, protected_packages = _load_protected()
    actual = _load_actual_apps(ws)

    result = _compute_actions(canonical, actual, protected_folders, protected_packages)
    result["_partition_rebuild_available"] = False
    result["canonical_count"] = [None] * len(canonical)

    if mode == "apply":
        _apply_renames(result["renamed"])
        _apply_removals(result["extras"])

    removed_bytes = sum(
        int(item.get("removed_size") or item.get("size_before") or 0)
        for item in result["extras"]
        if item.get("action") in ("removed", "remove")
    )

    _write_reports(ws, result, deferred_bp, mode)
    _print_summary(len(canonical), result, removed_bytes)

    duration = time.monotonic() - started
    return {
        "feature": "Stable App Normalization",
        "mode": mode,
        "style": style,
        "canonical_entries": len(canonical),
        "kept": len(result["kept"]),
        "renamed": len(result["renamed"]),
        "missing": len(result["missing"]),
        "extras": len(result["extras"]),
        "protected_extra": len(result["protected_extra"]),
        "removed_count": sum(1 for e in result["extras"] if e.get("action") in ("removed", "remove")),
        "removed_bytes": removed_bytes,
        "partition_rebuild_available": False,
        "final_zip_affected": False,
        "duration_seconds": round(duration, 2),
        "deferred_build_prop_rules_count": len(deferred_bp),
    }
