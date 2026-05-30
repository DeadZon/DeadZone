"""Stable App Policy Enforcement - package-name-first identity.

Stable style mutates only app folders under the allowed partition locations.
Package names are identity; folder names are only the desired final layout.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
from pathlib import Path
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from factory.state.build_state import BuildState

from factory.reports.app_inventory import _find_apps_list, _is_package_name


_ALLOWED_LOCATION_PAIRS: tuple[tuple[str, str], ...] = (
    ("system", "app"),
    ("system", "priv-app"),
    ("product", "app"),
    ("product", "priv-app"),
    ("system_ext", "app"),
    ("system_ext", "priv-app"),
    ("vendor", "app"),
    ("vendor", "priv-app"),
    ("mi_ext", "app"),
    ("mi_ext", "priv-app"),
)
_ALLOWED_PARTITIONS = {p for p, _t in _ALLOWED_LOCATION_PAIRS}
_UNKNOWN = "UNKNOWN"


def _env_int(name: str, default: int) -> int:
    raw = os.environ.get(name, "").strip()
    if not raw:
        return default
    try:
        return int(raw)
    except ValueError:
        return default


def _env_float(name: str, default: float) -> float:
    raw = os.environ.get(name, "").strip()
    if not raw:
        return default
    try:
        return float(raw)
    except ValueError:
        return default


def _build_allowed_dirs(partitions_root: Path) -> list[Path]:
    return [partitions_root / partition / app_type for partition, app_type in _ALLOWED_LOCATION_PAIRS]


def _safe_relative(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def _is_in_allowed(app_absolute: str, allowed: list[Path]) -> bool:
    try:
        p = Path(app_absolute).resolve()
        for d in allowed:
            try:
                p.relative_to(d.resolve())
                return True
            except ValueError:
                continue
    except Exception:
        pass
    return False


def _normalize_section(line: str) -> tuple[str, str] | None:
    cleaned = re.sub(r"\s+", "", line.strip().lower())
    if not cleaned or "/" not in cleaned:
        return None
    parts = [p for p in cleaned.split("/") if p]
    for idx, part in enumerate(parts):
        if part in _ALLOWED_PARTITIONS:
            partition = part
            app_type = "priv-app" if "priv-app" in parts[idx + 1:] else "app"
            if idx + 1 < len(parts) and parts[idx + 1] in {"app", "priv-app"}:
                app_type = parts[idx + 1]
            return partition, app_type
    app_type = "priv-app" if "priv-app" in cleaned else ("app" if "app" in cleaned else "")
    return ("system", app_type) if app_type else None


def _parse_expected_apps(path: Path) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    partition = "system"
    app_type = "app"
    lines = [l.strip() for l in path.read_text(encoding="utf-8", errors="ignore").splitlines()]
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line:
            i += 1
            continue
        section = _normalize_section(line)
        if section:
            partition, app_type = section
            i += 1
            continue
        if line.startswith("ro.") or line.startswith("=") or line.lower().endswith(".apk"):
            i += 1
            continue
        j = i + 1
        while j < len(lines) and not lines[j]:
            j += 1
        next_line = lines[j] if j < len(lines) else ""
        if not _is_package_name(line) and _is_package_name(next_line):
            name, package = line, next_line
            i = j + 1
        elif _is_package_name(line):
            name, package = line.split(".")[-1], line
            i += 1
        else:
            i += 1
            continue
        entries.append(
            {
                "name": name,
                "package": package,
                "section": app_type,
                "partition": partition,
                "app_type": app_type,
                "expected_path": f"{partition}/{app_type}/{name}",
                "expected_apk_name": f"{name}.apk",
            }
        )
    return entries


def _find_apk(folder: Path, expected_name: str = "") -> Path | None:
    direct = folder / f"{expected_name}.apk" if expected_name else None
    if direct and direct.is_file():
        return direct
    apks = sorted(folder.glob("*.apk"))
    return apks[0] if apks else None


def _package_from_tool(apk: Path) -> tuple[str, str, str]:
    commands = (
        ("aapt", ("aapt", "dump", "badging", str(apk))),
        ("apkanalyzer", ("apkanalyzer", "manifest", "application-id", str(apk))),
        ("bundletool", ("bundletool", "dump", "manifest", "--bundle", str(apk))),
    )
    for source, command in commands:
        try:
            proc = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, timeout=20)
        except Exception:
            continue
        if proc.returncode != 0:
            continue
        output = proc.stdout.strip()
        if not output:
            continue
        match = re.search(r"package: name='([^']+)'", output) or re.search(r"package=\"([^\"]+)\"", output)
        candidate = match.group(1) if match else output.splitlines()[0].strip()
        if _is_package_name(candidate):
            confidence = "medium" if source == "bundletool" and not match else "high"
            return candidate, source, confidence
    return "", "unknown", "low"


def _inventory_index(scanned_apps: list[dict[str, Any]], partitions_root: Path) -> dict[str, dict[str, Any]]:
    index: dict[str, dict[str, Any]] = {}
    for app in scanned_apps:
        candidates = [app.get("absolute_path"), app.get("found_at"), app.get("path")]
        for value in candidates:
            resolved = _resolve_app_path(value or "", partitions_root)
            if resolved:
                index[str(resolved)] = app
    return index


def _resolve_app_path(value: str | Path, partitions_root: Path) -> Path | None:
    if not value:
        return None
    raw = Path(str(value))
    candidates: list[Path] = []
    if raw.is_absolute():
        candidates.append(raw)
    parts = [p for p in raw.parts if p not in {"", "."}]
    for idx, part in enumerate(parts):
        if part in _ALLOWED_PARTITIONS:
            tail = list(parts[idx:])
            if len(tail) >= 2 and tail[1] == part:
                tail.pop(1)
            candidates.append(partitions_root.joinpath(*tail))
            if len(tail) >= 3:
                candidates.append(partitions_root / tail[0] / tail[1] / tail[2])
            break
    if len(parts) >= 2 and parts[0] in {"app", "priv-app"}:
        for partition in _ALLOWED_PARTITIONS:
            candidates.append(partitions_root / partition / parts[0] / parts[1])
    seen: set[Path] = set()
    for candidate in candidates:
        if candidate in seen:
            continue
        seen.add(candidate)
        if candidate.exists():
            return candidate.resolve()
    return candidates[0].resolve() if candidates else None


def _scan_allowed_apps(partitions_root: Path, scanned_apps: list[dict[str, Any]]) -> list[dict[str, Any]]:
    inventory = _inventory_index(scanned_apps, partitions_root)
    apps: list[dict[str, Any]] = []
    for partition, app_type in _ALLOWED_LOCATION_PAIRS:
        base = partitions_root / partition / app_type
        if not base.is_dir():
            continue
        for folder in sorted(p for p in base.iterdir() if p.is_dir()):
            inv = inventory.get(str(folder.resolve()), {})
            apk = _find_apk(folder, folder.name)
            package = str(inv.get("package_name") or "").strip()
            source = "inventory" if package and package.upper() != _UNKNOWN else ""
            confidence = "medium" if source == "inventory" else "low"
            if (not package or package.lower() == "unknown") and apk:
                package, source, confidence = _package_from_tool(apk)
            if not package:
                package = _UNKNOWN
                source = "unknown"
                confidence = "low"
            size = 0
            try:
                size = sum(p.stat().st_size for p in folder.rglob("*") if p.is_file())
            except OSError:
                pass
            apps.append(
                {
                    "partition": partition,
                    "app_type": app_type,
                    "type": app_type,
                    "name": folder.name,
                    "folder_name": folder.name,
                    "path": f"{partition}/{app_type}/{folder.name}",
                    "absolute_path": str(folder.resolve()),
                    "apk_path": str(apk.resolve()) if apk else "",
                    "apk_name": apk.name if apk else "",
                    "package_name": package,
                    "package_source": source,
                    "package_confidence": confidence,
                    "size": size,
                }
            )
    allowed = _build_allowed_dirs(partitions_root)
    seen = {a["absolute_path"] for a in apps}
    for inv in scanned_apps:
        resolved = _resolve_app_path(inv.get("absolute_path") or inv.get("found_at") or inv.get("path") or "", partitions_root)
        if not resolved or str(resolved) in seen:
            continue
        package = str(inv.get("package_name") or _UNKNOWN)
        source = "inventory" if package and package.upper() != _UNKNOWN and package.lower() != "unknown" else "unknown"
        apps.append(
            {
                "partition": str(inv.get("partition") or ""),
                "app_type": str(inv.get("app_type") or inv.get("type") or ""),
                "type": str(inv.get("app_type") or inv.get("type") or ""),
                "name": str(inv.get("name") or resolved.name),
                "folder_name": str(inv.get("name") or resolved.name),
                "path": str(inv.get("path") or _safe_relative(resolved, partitions_root)),
                "absolute_path": str(resolved),
                "apk_path": "",
                "apk_name": "",
                "package_name": package if package.lower() != "unknown" else _UNKNOWN,
                "package_source": source,
                "package_confidence": "medium" if source == "inventory" else "low",
                "size": int(inv.get("size") or 0),
            }
        )
    return apps


def _write_scan_reports(reports_dir: Path, data: dict[str, Any]) -> None:
    reports_dir.mkdir(parents=True, exist_ok=True)
    (reports_dir / "stable_package_scan_report.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    lines = [
        "DeadZone Stable Package Scan Report",
        "===================================",
        f"scanned_apps: {data.get('summary', {}).get('scanned_apps', 0)}",
        f"unknown_package_apps: {data.get('summary', {}).get('unknown_package_apps', 0)}",
        f"matched_by_package: {data.get('summary', {}).get('matched_by_package', 0)}",
        f"unmatched_known_packages: {data.get('summary', {}).get('unmatched_known_packages', 0)}",
        "",
        "apps:",
    ]
    for app in data.get("apps") or []:
        lines.append(
            f"  - {app['path']} package={app['package_name']} "
            f"source={app.get('package_source')} confidence={app.get('package_confidence')} "
            f"apk={app.get('apk_name') or '(none)'}"
        )
    (reports_dir / "stable_package_scan_report.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def _expected_by_package(expected: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    return {e["package"].lower(): e for e in (_normalize_expected(e) for e in expected)}


def _normalize_expected(entry: dict[str, str]) -> dict[str, str]:
    app_type = entry.get("app_type") or entry.get("section") or "app"
    partition = entry.get("partition") or "system"
    name = entry["name"]
    return {
        **entry,
        "partition": partition,
        "app_type": app_type,
        "expected_path": entry.get("expected_path") or f"{partition}/{app_type}/{name}",
        "expected_apk_name": entry.get("expected_apk_name") or f"{name}.apk",
    }


def _classify(scanned_apps: list[dict[str, Any]], expected: list[dict[str, str]], allowed: list[Path]) -> dict[str, list]:
    by_pkg = _expected_by_package(expected)
    scanned_by_pkg: dict[str, list[dict[str, Any]]] = {}
    unknown: list[dict[str, Any]] = []
    for app in scanned_apps:
        if "app_type" not in app:
            app["app_type"] = str(app.get("type") or "")
        if "folder_name" not in app:
            app["folder_name"] = str(app.get("name") or "")
        if "absolute_path" not in app:
            app["absolute_path"] = str(app.get("found_at") or "")
        pkg = str(app.get("package_name") or "").strip()
        if not pkg or pkg.upper() == _UNKNOWN or pkg.lower() == "unknown":
            unknown.append({**app, "status": "UNKNOWN_PACKAGE", "action": "REPORT_ONLY"})
            continue
        scanned_by_pkg.setdefault(pkg.lower(), []).append(app)

    kept: list[dict[str, Any]] = []
    to_rename: list[dict[str, Any]] = []
    wrong_location: list[dict[str, Any]] = []
    missing: list[dict[str, Any]] = []
    matched_paths: set[str] = set()

    for raw_entry in expected:
        entry = _normalize_expected(raw_entry)
        pkg_key = entry["package"].lower()
        actuals = scanned_by_pkg.get(pkg_key) or []
        exact = next((a for a in actuals if a["partition"] == entry["partition"] and a["app_type"] == entry["app_type"] and a["folder_name"] == entry["name"]), None)
        same_place = next((a for a in actuals if a["partition"] == entry["partition"] and a["app_type"] == entry["app_type"]), None)
        if exact and exact.get("apk_name") and exact.get("apk_name") != entry["expected_apk_name"]:
            matched_paths.add(exact["absolute_path"])
            to_rename.append({**exact, "status": "FOUND_RENAMED", "action": "RENAME_TO_EXPECTED", "expected": entry, "package": entry["package"], "expected_name": entry["name"], "actual_name": exact["folder_name"], "found_at": exact["absolute_path"], "in_allowed": _is_in_allowed(exact["absolute_path"], allowed)})
        elif exact:
            matched_paths.add(exact["absolute_path"])
            kept.append({**exact, "status": "FOUND", "action": "KEEP", "expected": entry, "package": entry["package"], "found_at": exact["absolute_path"]})
        elif same_place:
            matched_paths.add(same_place["absolute_path"])
            to_rename.append({**same_place, "status": "FOUND_RENAMED", "action": "RENAME_TO_EXPECTED", "expected": entry, "package": entry["package"], "expected_name": entry["name"], "actual_name": same_place["folder_name"], "found_at": same_place["absolute_path"], "in_allowed": _is_in_allowed(same_place["absolute_path"], allowed)})
        elif actuals:
            for actual in actuals:
                matched_paths.add(actual["absolute_path"])
                wrong_location.append({**actual, "status": "FOUND_WRONG_LOCATION", "action": "REPORT_ONLY", "expected": entry, "package": entry["package"], "found_at": actual["absolute_path"]})
        else:
            missing.append({"status": "MISSING", "action": "REPORT_ONLY", "name": entry["name"], "package": entry["package"], "expected_partition": entry["partition"], "expected_app_type": entry["app_type"], "expected_path": entry["expected_path"]})

    extras: list[dict[str, Any]] = []
    outside: list[dict[str, Any]] = []
    for app in scanned_apps:
        pkg = str(app.get("package_name") or "").strip()
        if app["absolute_path"] in matched_paths or not pkg or pkg.upper() == _UNKNOWN or pkg.lower() == "unknown":
            continue
        item = {**app, "status": "EXTRA", "action": "DELETE", "package": pkg, "found_at": app["absolute_path"]}
        if pkg.lower() not in by_pkg and _is_in_allowed(app["absolute_path"], allowed):
            extras.append(item)
        elif not _is_in_allowed(app["absolute_path"], allowed):
            outside.append({**item, "status": "OUTSIDE_ALLOWED", "action": "SKIP"})

    return {
        "kept": kept,
        "to_rename": to_rename,
        "extra_in_allowed": extras,
        "skipped_outside": outside,
        "missing": missing,
        "wrong_location": wrong_location,
        "unknown": unknown,
    }


def _safety_thresholds() -> dict[str, Any]:
    return {
        "min_kept_apps": _env_int("DEADZONE_STABLE_MIN_KEPT_APPS", 20),
        "max_missing_apps": _env_int("DEADZONE_STABLE_MAX_MISSING_APPS", 80),
        "max_delete_candidates": _env_int("DEADZONE_STABLE_MAX_DELETE_CANDIDATES", 100),
        "min_match_ratio": _env_float("DEADZONE_STABLE_MIN_MATCH_RATIO", 0.40),
    }


def _stable_safety_guard(expected_count: int, classification: dict[str, list], enforce: bool) -> dict[str, Any]:
    thresholds = _safety_thresholds()
    kept = len(classification["kept"])
    renamed = len(classification["to_rename"])
    wrong_location = len(classification["wrong_location"])
    matched = kept + renamed + wrong_location
    missing = len(classification["missing"])
    deletes = len(classification["extra_in_allowed"])
    ratio = (matched / expected_count) if expected_count else 1.0
    normal_rom = expected_count > 100
    reasons: list[str] = []
    if normal_rom and kept < thresholds["min_kept_apps"]:
        reasons.append(f"kept_apps {kept} is below {thresholds['min_kept_apps']}")
    if missing > thresholds["max_missing_apps"]:
        reasons.append(f"missing_apps {missing} exceeds {thresholds['max_missing_apps']}")
    if deletes > thresholds["max_delete_candidates"]:
        reasons.append(f"delete_candidates {deletes} exceeds {thresholds['max_delete_candidates']}")
    if normal_rom and ratio < thresholds["min_match_ratio"]:
        reasons.append(f"matched_expected_ratio {ratio:.2f} is below {thresholds['min_match_ratio']:.2f}")
    if expected_count > 100 and matched < 50:
        reasons.append(f"expected apps count {expected_count} but matched apps count {matched}")
    status = "failed" if reasons and enforce else ("warning" if reasons else "passed")
    return {
        "status": status,
        "thresholds": thresholds,
        "reason": "; ".join(reasons),
        "expected_apps_count": expected_count,
        "matched_expected_count": matched,
        "matched_expected_ratio": ratio,
        "kept_apps": kept,
        "missing_apps": missing,
        "delete_candidates": deletes,
    }


def _unsafe_payload(guard: dict[str, Any]) -> dict[str, str]:
    return {
        "error_type": "STABLE_APP_MATCHING_UNSAFE",
        "cause": "Stable package matching is unsafe; too many expected apps are missing or too many extras are planned for deletion",
        "telegram_cause": (
            f"Matching unsafe: kept={guard.get('kept_apps')}, "
            f"missing={guard.get('missing_apps')}, "
            f"delete_candidates={guard.get('delete_candidates')}"
        ),
        "suggested_fix": "Fix package extraction/matching before deleting apps",
        "suggested_check": "Check stable_package_scan_report.json and stable_app_policy_report.json",
        "details": (
            f"Matching unsafe: kept={guard.get('kept_apps')}, "
            f"missing={guard.get('missing_apps')}, "
            f"delete_candidates={guard.get('delete_candidates')}"
        ),
    }


def _rename_apk(folder: Path, expected_name: str) -> dict[str, Any] | None:
    apk = _find_apk(folder)
    if not apk:
        return None
    target = folder / f"{expected_name}.apk"
    if apk == target:
        return None
    if target.exists():
        raise RuntimeError(f"CONFLICT: APK rename target already exists: {target}")
    apk.rename(target)
    return {"old_apk_path": str(apk), "new_apk_path": str(target)}


def _execute_renames(to_rename: list[dict[str, Any]], enforce: bool) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[str], set[str]]:
    renamed: list[dict[str, Any]] = []
    skipped: list[dict[str, Any]] = []
    errors: list[str] = []
    changed: set[str] = set()
    for item in to_rename:
        src = Path(item["found_at"])
        expected = _normalize_expected(item.get("expected") or {"name": item.get("expected_name", ""), "package": item.get("package", ""), "partition": item.get("partition", ""), "app_type": item.get("app_type", "")})
        target = src.parent / expected["name"]
        if not enforce:
            skipped.append({**item, "enacted": False, "reason": "report-only mode"})
            continue
        if not item.get("in_allowed"):
            skipped.append({**item, "enacted": False, "reason": "outside allowed location"})
            continue
        if not src.exists():
            skipped.append({**item, "enacted": False, "reason": "source path not found"})
            continue
        if target.exists() and target != src:
            errors.append(f"CONFLICT: rename target already exists: {target}")
            continue
        try:
            if target != src:
                src.rename(target)
            apk_change = _rename_apk(target, expected["name"])
            result = {**item, "enacted": True, "new_path": str(target), "found_at": str(target)}
            if apk_change:
                result.update(apk_change)
            renamed.append(result)
            changed.add(str(item.get("partition") or expected["partition"]))
        except Exception as exc:
            errors.append(f"RENAME FAILED: {src} -> {target}: {exc}")
    return renamed, skipped, errors, changed


def _apply_renames(to_rename: list[dict[str, Any]], enforce: bool) -> tuple[list[dict[str, Any]], list[str]]:
    renamed, skipped, errors, _changed = _execute_renames(to_rename, enforce)
    return renamed + skipped, errors


def _execute_deletes(extras: list[dict[str, Any]], enforce: bool, allowed: list[Path]) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]], list[str], set[str]]:
    deleted: list[dict[str, Any]] = []
    skipped: list[dict[str, Any]] = []
    outside: list[dict[str, Any]] = []
    errors: list[str] = []
    changed: set[str] = set()
    for item in extras:
        path = Path(item["found_at"])
        if not _is_in_allowed(str(path), allowed):
            outside.append({**item, "enacted": False, "reason": "outside allowed location"})
            continue
        if not enforce:
            skipped.append({**item, "enacted": False, "reason": "report-only mode"})
            continue
        if not path.exists():
            skipped.append({**item, "enacted": False, "reason": "path not found"})
            continue
        try:
            if path.is_dir():
                shutil.rmtree(path)
            else:
                path.unlink()
            deleted.append({**item, "enacted": True})
            changed.add(str(item.get("partition") or ""))
        except Exception as exc:
            errors.append(f"DELETE FAILED: {path}: {exc}")
    return deleted, skipped, outside, errors, changed


def _apply_deletes(extras: list[dict[str, Any]], enforce: bool) -> tuple[list[dict[str, Any]], list[str]]:
    allowed = _build_allowed_dirs(Path("/"))
    deleted, skipped, outside, errors, _changed = _execute_deletes(extras, enforce, allowed)
    return deleted + skipped + outside, errors


def _write_inventory(path: Path, rows: list[dict[str, Any]], formatter) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(formatter(row) for row in rows) + ("\n" if rows else ""), encoding="utf-8")


def _write_inventory_files(inventory_dir: Path, data: dict[str, Any]) -> None:
    _write_inventory(inventory_dir / "apps_missing.txt", data["missing_apps"], lambda r: f"{r['expected_path']} {r['package']}")
    _write_inventory(inventory_dir / "apps_removed.txt", data["deleted_extra_apps"], lambda r: f"{r['path']} {r['package']}")
    _write_inventory(inventory_dir / "apps_remove_skipped.txt", data["skipped_delete_apps"], lambda r: f"{r.get('path', r.get('found_at'))} {r.get('package')} reason={r.get('reason','')}")
    _write_inventory(inventory_dir / "apps_renamed.txt", data["renamed_apps"], lambda r: f"{r.get('actual_name')} -> {r.get('expected_name')} {r.get('package')}")
    _write_inventory(inventory_dir / "apps_rename_skipped.txt", data["skipped_rename_apps"], lambda r: f"{r.get('actual_name')} -> {r.get('expected_name')} {r.get('package')} reason={r.get('reason','')}")
    _write_inventory(inventory_dir / "apps_unknown_package.txt", data["unknown_package_apps"], lambda r: f"{r.get('path')} package=UNKNOWN")
    _write_inventory(inventory_dir / "apps_wrong_location.txt", data["found_wrong_location_apps"], lambda r: f"{r.get('path')} {r.get('package')} expected={r.get('expected', {}).get('expected_path', '')}")


def _write_txt_report(path: Path, data: dict[str, Any]) -> None:
    summary = data.get("summary", {})
    lines = [
        "DeadZone Stable App Policy Report",
        "==================================",
        f"style: {data.get('style')}",
        f"enforce_mode: {data.get('enforce_mode')}",
        f"apps_list_path: {data.get('apps_list_path')}",
        f"total_expected: {data.get('total_expected')}",
        "",
        "summary:",
    ]
    for key in ("kept_apps", "renamed_apps", "skipped_rename_apps", "missing_apps", "found_wrong_location_apps", "unknown_package_apps", "delete_candidates", "deleted_extra_apps", "skipped_delete_apps", "skipped_outside_allowed_locations", "changed_partitions"):
        lines.append(f"  {key}: {summary.get(key, 0)}")
    guard = data.get("safety_guard") if isinstance(data.get("safety_guard"), dict) else {}
    if guard:
        lines += ["", "safety_guard:", f"  status: {guard.get('status')}", f"  reason: {guard.get('reason') or '(none)'}"]
    for title, key in (
        ("KEPT APPS", "kept_apps"),
        ("RENAMED APPS", "renamed_apps"),
        ("SKIPPED RENAME APPS", "skipped_rename_apps"),
        ("MISSING APPS", "missing_apps"),
        ("WRONG LOCATION APPS", "found_wrong_location_apps"),
        ("UNKNOWN PACKAGE APPS", "unknown_package_apps"),
        ("DELETE CANDIDATES", "delete_candidates"),
        ("DELETED EXTRA APPS", "deleted_extra_apps"),
        ("SKIPPED DELETE APPS", "skipped_delete_apps"),
    ):
        lines += ["", f"{title}:"]
        rows = data.get(key) or []
        lines.extend(f"  - {r.get('path') or r.get('expected_path') or r.get('found_at')} {r.get('package') or r.get('package_name')}" for r in rows)
        if not rows:
            lines.append("  (none)")
    if data.get("errors"):
        lines += ["", "errors:", *[f"  - {e}" for e in data["errors"]]]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def enforce_stable_app_policy(
    reports_dir: Path,
    partitions_root: Path,
    scanned_apps: list[dict[str, Any]],
    style: str,
    build_state: "BuildState | None" = None,
    dry_run: bool = False,
) -> dict[str, Any]:
    style_key = style.strip().lower()
    env_dry_run = os.environ.get("DEADZONE_STABLE_DRY_RUN", "").strip().lower() in {"1", "true", "yes", "on"}
    dry_run = bool(dry_run or env_dry_run)
    enforce = style_key == "stable" and not dry_run
    apps_list_path = _find_apps_list()
    if apps_list_path is None:
        if enforce:
            raise RuntimeError("Stable App Policy requires ListMezo/free/apps.list but the file was not found")
        return {"status": "skipped", "reason": "apps.list not found", "style": style, "enforce_mode": enforce}

    expected = _parse_expected_apps(apps_list_path)
    scanned = _scan_allowed_apps(partitions_root, scanned_apps)
    expected_packages = {e["package"].lower() for e in expected}
    scanned_known_packages = {
        str(a.get("package_name") or "").lower()
        for a in scanned
        if str(a.get("package_name") or "").strip() and str(a.get("package_name")).upper() != _UNKNOWN
    }
    scan_data = {
        "status": "ok",
        "apps": scanned,
        "summary": {
            "scanned_apps": len(scanned),
            "unknown_package_apps": sum(1 for a in scanned if str(a.get("package_name")).upper() == _UNKNOWN),
            "matched_by_package": len(expected_packages & scanned_known_packages),
            "unmatched_known_packages": len(scanned_known_packages - expected_packages),
        },
        "scanned_apps": len(scanned),
        "unknown_package_apps": [a for a in scanned if str(a.get("package_name")).upper() == _UNKNOWN],
        "matched_by_package": sorted(expected_packages & scanned_known_packages),
        "unmatched_known_packages": sorted(scanned_known_packages - expected_packages),
    }
    _write_scan_reports(reports_dir, scan_data)

    allowed = _build_allowed_dirs(partitions_root)
    classification = _classify(scanned, expected, allowed)
    guard = _stable_safety_guard(len(expected), classification, enforce)
    if guard["status"] == "failed":
        payload = _unsafe_payload(guard)
        data = {
            "status": "failed",
            "style": style,
            "enforce_mode": enforce,
            "apps_list_path": str(apps_list_path),
            "total_expected": len(expected),
            "expected_apps_count": len(expected),
            "matched_expected_count": guard["matched_expected_count"],
            "matched_expected_ratio": guard["matched_expected_ratio"],
            "kept_apps": classification["kept"],
            "renamed_apps": [],
            "skipped_rename_apps": classification["to_rename"],
            "missing_apps": classification["missing"],
            "found_wrong_location_apps": classification["wrong_location"],
            "unknown_package_apps": classification["unknown"],
            "delete_candidates": classification["extra_in_allowed"],
            "deleted_extra_apps": [],
            "skipped_delete_apps": classification["extra_in_allowed"],
            "skipped_outside_allowed_locations": classification["skipped_outside"],
            "changed_partitions": [],
            "safety_guard": guard,
            "errors": [payload],
        }
        data["summary"] = {
            "expected_apps_count": len(expected),
            "matched_expected_count": guard["matched_expected_count"],
            "matched_expected_ratio": guard["matched_expected_ratio"],
            "kept_apps": len(data["kept_apps"]),
            "renamed_apps": 0,
            "skipped_rename_apps": len(data["skipped_rename_apps"]),
            "missing_apps": len(data["missing_apps"]),
            "found_wrong_location_apps": len(data["found_wrong_location_apps"]),
            "unknown_package_apps": len(data["unknown_package_apps"]),
            "delete_candidates": len(data["delete_candidates"]),
            "deleted_extra_apps": 0,
            "skipped_delete_apps": len(data["skipped_delete_apps"]),
            "skipped_outside_allowed_locations": len(data["skipped_outside_allowed_locations"]),
            "changed_partitions": 0,
            "kept": len(data["kept_apps"]),
            "renamed": 0,
            "missing": len(data["missing_apps"]),
            "deleted_extra": 0,
            "skipped_outside": len(data["skipped_outside_allowed_locations"]),
        }
        workspace_root = reports_dir.parent
        _write_inventory_files(workspace_root / "inventory", data)
        reports_dir.mkdir(parents=True, exist_ok=True)
        _write_txt_report(reports_dir / "stable_app_policy_report.txt", data)
        (reports_dir / "stable_app_policy_report.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        raise RuntimeError(json.dumps(payload, sort_keys=True))

    renamed, skipped_rename, rename_errors, rename_changed = _execute_renames(classification["to_rename"], enforce)
    deleted, skipped_delete, skipped_outside_delete, delete_errors, delete_changed = _execute_deletes(classification["extra_in_allowed"], enforce, allowed)
    all_errors = rename_errors + delete_errors

    changed_partitions = sorted(p for p in (rename_changed | delete_changed) if p)
    if enforce and all_errors:
        raise RuntimeError("Stable App Policy failed with errors:\n" + "\n".join(all_errors))

    data: dict[str, Any] = {
        "status": "ok",
        "style": style,
        "enforce_mode": enforce,
        "apps_list_path": str(apps_list_path),
        "total_expected": len(expected),
        "expected_apps_count": len(expected),
        "matched_expected_count": guard["matched_expected_count"],
        "matched_expected_ratio": guard["matched_expected_ratio"],
        "kept_apps": classification["kept"],
        "renamed_apps": renamed,
        "skipped_rename_apps": skipped_rename,
        "missing_apps": classification["missing"],
        "found_wrong_location_apps": classification["wrong_location"],
        "unknown_package_apps": classification["unknown"],
        "delete_candidates": classification["extra_in_allowed"],
        "deleted_extra_apps": deleted,
        "skipped_delete_apps": skipped_delete,
        "skipped_outside_allowed_locations": classification["skipped_outside"] + skipped_outside_delete,
        "changed_partitions": changed_partitions,
        "safety_guard": guard,
        "errors": all_errors,
    }
    data["summary"] = {
        "expected_apps_count": len(expected),
        "matched_expected_count": guard["matched_expected_count"],
        "matched_expected_ratio": guard["matched_expected_ratio"],
        "kept_apps": len(data["kept_apps"]),
        "renamed_apps": len(data["renamed_apps"]),
        "skipped_rename_apps": len(data["skipped_rename_apps"]),
        "missing_apps": len(data["missing_apps"]),
        "found_wrong_location_apps": len(data["found_wrong_location_apps"]),
        "unknown_package_apps": len(data["unknown_package_apps"]),
        "delete_candidates": len(data["delete_candidates"]),
        "deleted_extra_apps": len(data["deleted_extra_apps"]),
        "skipped_delete_apps": len(data["skipped_delete_apps"]),
        "skipped_outside_allowed_locations": len(data["skipped_outside_allowed_locations"]),
        "changed_partitions": len(changed_partitions),
        "kept": len(data["kept_apps"]),
        "renamed": len(data["renamed_apps"]),
        "missing": len(data["missing_apps"]),
        "deleted_extra": len(data["deleted_extra_apps"]),
        "skipped_outside": len(data["skipped_outside_allowed_locations"]),
    }

    workspace_root = reports_dir.parent
    _write_inventory_files(workspace_root / "inventory", data)
    reports_dir.mkdir(parents=True, exist_ok=True)
    _write_txt_report(reports_dir / "stable_app_policy_report.txt", data)
    (reports_dir / "stable_app_policy_report.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    if build_state is not None:
        try:
            build_state.counters.update(
                stable_kept_apps=len(data["kept_apps"]),
                stable_renamed_apps=len(data["renamed_apps"]),
                stable_missing_apps=len(data["missing_apps"]),
                stable_deleted_extra_apps=len(data["deleted_extra_apps"]),
            )
            build_state.save()
        except Exception as exc:
            print(f"[STABLE APP POLICY] Warning: counters update failed: {exc}")

    print(
        "[STABLE APP POLICY] "
        f"kept={len(data['kept_apps'])} renamed={len(data['renamed_apps'])} "
        f"missing={len(data['missing_apps'])} deleted_extra={len(data['deleted_extra_apps'])} "
        f"unknown={len(data['unknown_package_apps'])}"
    )
    return data
