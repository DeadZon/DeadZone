from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from factory.state.build_state import BuildState

_APPS_LIST_ENV = "LISTMEZO_APPS_LIST"
_APPS_LIST_RELATIVE = "ListMezo/free/apps.list"
_APPS_LIST_ABSOLUTE = ""
_ALLOWED_PARTITIONS = {"system", "product", "system_ext", "vendor", "mi_ext"}


# ---------------------------------------------------------------------------
# apps.list parser
# ---------------------------------------------------------------------------

def _is_package_name(s: str) -> bool:
    return bool(re.match(r"^[a-zA-Z][a-zA-Z0-9_]*(\.[a-zA-Z0-9_]+){2,}$", s))


def _normalize_expected_path(value: str) -> tuple[str, str, str] | None:
    cleaned = re.sub(r"\s+", "", value.strip())
    if not cleaned or "/" not in cleaned:
        return None
    parts = [p for p in cleaned.split("/") if p]
    for idx, part in enumerate(parts):
        if part not in _ALLOWED_PARTITIONS:
            continue
        tail = parts[idx:]
        if len(tail) >= 2 and tail[1] == part:
            tail.pop(1)
        if len(tail) >= 3 and tail[1] in {"app", "priv-app"}:
            return tail[0], tail[1], tail[2]
        if len(tail) >= 2 and tail[1] in {"app", "priv-app"}:
            return tail[0], tail[1], ""
    return None


def _entry(name: str, package: str, partition: str, app_type: str) -> dict[str, str]:
    return {
        "name": name,
        "expected_folder_name": name,
        "package": package,
        "expected_package": package,
        "section": app_type,
        "partition": partition,
        "app_type": app_type,
        "expected_path": f"{partition}/{app_type}/{name}",
        "expected_apk_name": f"{name}.apk",
    }


def _is_section_header(s: str) -> bool:
    lower = s.lower()
    if "/" in s:
        return _normalize_expected_path(s + "/_placeholder") is not None
    return lower in {"or", "fine", "and", "remove", "replace", "delate", "delete"}


def _parse_apps_list(path: Path) -> list[dict[str, str]]:
    """Parse apps.list into [{name, package, section}] entries."""
    entries: list[dict[str, str]] = []
    current_partition = "system"
    current_section = "app"
    raw_lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    lines = [l.strip() for l in raw_lines]

    i = 0
    while i < len(lines):
        line = lines[i]

        if not line:
            i += 1
            continue

        path_entry = _normalize_expected_path(line)
        if path_entry and path_entry[2]:
            path_partition, path_app_type, path_name = path_entry
            j = i + 1
            while j < len(lines) and not lines[j]:
                j += 1
            next_line = lines[j] if j < len(lines) else ""
            if _is_package_name(next_line):
                entries.append(_entry(path_name, next_line, path_partition, path_app_type))
                i = j + 1
                continue

        section = _normalize_expected_path(line + "/_placeholder") if "/" in line else None
        if section:
            current_partition, current_section, _placeholder = section
            i += 1
            continue

        if _is_section_header(line):
            i += 1
            continue

        # ro.* properties (build.prop entries)
        if line.startswith("ro.") or line.startswith("=") or line.startswith("fine ") or line.startswith("remove "):
            i += 1
            continue

        # .apk file references (split APK hints)
        if line.lower().endswith(".apk"):
            i += 1
            continue

        # Skip pure number or short noise
        if len(line) < 3:
            i += 1
            continue

        # Look for the next non-empty line
        j = i + 1
        while j < len(lines) and not lines[j]:
            j += 1

        next_line = lines[j] if j < len(lines) else ""

        if _is_package_name(line) and _is_package_name(next_line):
            # line = folder name that happens to be a package, next_line = package
            entries.append(_entry(line, next_line, current_partition, current_section))
            i = j + 1
            continue

        if not _is_package_name(line) and _is_package_name(next_line):
            # Normal: name then package
            entries.append(_entry(line, next_line, current_partition, current_section))
            i = j + 1
            continue

        if _is_package_name(line) and not _is_package_name(next_line):
            # Standalone package name = folder name
            folder_name = line.split(".")[-1] if "." in line else line
            entries.append(_entry(folder_name, line, current_partition, current_section))
            i += 1
            continue

        # Non-package, non-section line with no package following — skip
        i += 1

    return entries


def _find_apps_list() -> Path | None:
    override = os.environ.get(_APPS_LIST_ENV, "").strip()
    if override:
        p = Path(override)
        return p if p.is_file() else None
    candidates = [
        _APPS_LIST_RELATIVE,
    ]
    for candidate in candidates:
        if not candidate:
            continue
        p = Path(candidate)
        if p.is_file():
            return p
    return None


# ---------------------------------------------------------------------------
# Comparison logic
# ---------------------------------------------------------------------------

def _compare_apps(
    scanned: list[dict[str, Any]],
    expected: list[dict[str, str]],
) -> dict[str, Any]:
    expected_by_package: dict[str, dict[str, str]] = {}
    expected_by_name: dict[str, dict[str, str]] = {}
    for entry in expected:
        pkg = entry["package"].lower()
        name = entry["name"].lower()
        expected_by_package[pkg] = entry
        expected_by_name[name] = entry

    result_expected: list[dict[str, Any]] = []
    result_extra: list[dict[str, Any]] = []

    matched_expected: set[str] = set()

    for app in scanned:
        pkg = (app.get("package_name") or "").lower()
        name = (app.get("name") or "").lower()
        found_at = f"{app.get('partition', '')}/{app.get('path', '')}"

        if pkg and pkg != "unknown" and pkg in expected_by_package:
            entry = expected_by_package[pkg]
            matched_expected.add(entry["package"].lower())
            # Check for rename (folder name differs from expected)
            name_mismatch = entry["name"].lower() != name
            result_expected.append({
                "name": entry["name"],
                "package": entry["package"],
                "status": "DEFAULT_FOUND",
                "found_at": found_at,
                "renamed": name_mismatch,
                "found_name": app.get("name", ""),
            })
        elif name and name in expected_by_name:
            entry = expected_by_name[name]
            pkg_key = entry["package"].lower()
            if pkg_key not in matched_expected:
                matched_expected.add(pkg_key)
                result_expected.append({
                    "name": entry["name"],
                    "package": entry["package"],
                    "status": "DEFAULT_FOUND",
                    "found_at": found_at,
                    "renamed": False,
                    "found_name": app.get("name", ""),
                })
        else:
            result_extra.append({
                "name": app.get("name", ""),
                "package": app.get("package_name", "unknown"),
                "partition": app.get("partition", ""),
                "found_at": found_at,
                "status": "DELETE_CANDIDATE",
                "size": app.get("size", 0),
            })

    result_missing: list[dict[str, Any]] = []
    for entry in expected:
        if entry["package"].lower() not in matched_expected:
            result_missing.append({
                "name": entry["name"],
                "package": entry["package"],
                "status": "MISSING",
                "expected_section": entry.get("section", ""),
            })

    return {
        "found": result_expected,
        "extra": result_extra,
        "missing": result_missing,
    }


# ---------------------------------------------------------------------------
# Report writers
# ---------------------------------------------------------------------------

def _write_txt_report(path: Path, data: dict[str, Any]) -> None:
    found = data.get("found", [])
    extra = data.get("extra", [])
    missing = data.get("missing", [])
    counters = data.get("counters", {})

    lines = [
        "DeadZone App Inventory Policy Report",
        "=====================================",
        f"apps_list_path    : {data.get('apps_list_path', '(not found)')}",
        f"total_expected    : {data.get('total_expected', 0)}",
        f"default_found     : {counters.get('default_found', 0)}",
        f"extra_apps        : {counters.get('extra_apps', 0)}",
        f"missing_apps      : {counters.get('missing_apps', 0)}",
        f"delete_candidates : {counters.get('delete_candidates', 0)}",
        f"renamed_apps      : {counters.get('renamed_apps', 0)}",
        "",
        "DEFAULT FOUND:",
    ]
    for app in found:
        rename_note = f" [RENAMED from {app.get('found_name')}]" if app.get("renamed") else ""
        lines.append(f"  [OK] {app['name']} ({app['package']}) @ {app['found_at']}{rename_note}")
    if not found:
        lines.append("  (none)")

    lines += ["", "EXTRA APPS (DELETE CANDIDATES):"]
    for app in extra:
        lines.append(
            f"  [DEL] {app['name']} ({app['package']}) @ {app['found_at']} "
            f"size={app.get('size', 0)}"
        )
    if not extra:
        lines.append("  (none)")

    lines += ["", "MISSING EXPECTED APPS:"]
    for app in missing:
        lines.append(f"  [MISS] {app['name']} ({app['package']}) expected in {app.get('expected_section', '')}")
    if not missing:
        lines.append("  (none)")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------

def compare_app_policy(
    reports_dir: Path,
    scanned_apps: list[dict[str, Any]],
    build_state: "BuildState | None" = None,
) -> dict[str, Any]:
    """
    Compare scanned apps against the apps.list policy file.
    Writes output/reports/app_inventory_report.txt and .json.
    Updates build_state counters if provided.
    Returns counters dict.
    """
    apps_list_path = _find_apps_list()
    if apps_list_path is None:
        print("[APP POLICY] apps.list not found; skipping policy comparison")
        return {
            "status": "skipped",
            "reason": "apps.list not found",
            "counters": {},
        }

    print(f"[APP POLICY] Using apps.list: {apps_list_path}")
    try:
        expected = _parse_apps_list(apps_list_path)
    except Exception as exc:
        print(f"[APP POLICY] Warning: failed to parse apps.list: {exc}")
        return {"status": "failed", "reason": str(exc), "counters": {}}

    comparison = _compare_apps(scanned_apps, expected)
    found = comparison["found"]
    extra = comparison["extra"]
    missing = comparison["missing"]
    renamed = [a for a in found if a.get("renamed")]

    counters = {
        "default_found": len(found),
        "extra_apps": len(extra),
        "missing_apps": len(missing),
        "delete_candidates": len(extra),
        "renamed_apps": len(renamed),
    }

    if build_state is not None:
        try:
            build_state.counters.update(**counters)
            build_state.save()
        except Exception as exc:
            print(f"[APP POLICY] Warning: failed to update build_state counters: {exc}")

    data: dict[str, Any] = {
        "status": "ok",
        "apps_list_path": str(apps_list_path),
        "total_expected": len(expected),
        "counters": counters,
        "found": found,
        "extra": extra,
        "missing": missing,
    }

    reports_dir.mkdir(parents=True, exist_ok=True)
    try:
        txt_path = reports_dir / "app_inventory_report.txt"
        _write_txt_report(txt_path, data)
        print(f"[APP POLICY] Written: {txt_path}")
    except Exception as exc:
        print(f"[APP POLICY] Warning: failed to write txt report: {exc}")

    try:
        json_path = reports_dir / "app_inventory_report.json"
        json_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        print(f"[APP POLICY] Written: {json_path}")
    except Exception as exc:
        print(f"[APP POLICY] Warning: failed to write json report: {exc}")

    print(
        f"[APP POLICY] found={counters['default_found']} "
        f"extra={counters['extra_apps']} "
        f"missing={counters['missing_apps']} "
        f"renamed={counters['renamed_apps']}"
    )
    return data
