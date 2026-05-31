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
import zipfile
from pathlib import Path
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from factory.state.build_state import BuildState

from factory.reports.app_inventory import _find_apps_list, _is_package_name, _is_rejected_package


# Partitions and app-type pairs that Stable App Policy is allowed to operate on
# (scan, delete, rename, move).  vendor and mi_ext are intentionally excluded —
# the policy must never touch those partitions.
_POLICY_LOCATION_PAIRS: tuple[tuple[str, str], ...] = (
    ("system", "app"),
    ("system", "priv-app"),
    ("product", "app"),
    ("product", "priv-app"),
    ("system_ext", "app"),
    ("system_ext", "priv-app"),
)
_POLICY_PARTITIONS: frozenset[str] = frozenset(p for p, _ in _POLICY_LOCATION_PAIRS)
# Broader set kept only for path-string parsing (_normalize_expected_path,
# _resolve_app_path).  It is NOT used for any operational decision.
_ALLOWED_PARTITIONS: frozenset[str] = _POLICY_PARTITIONS | {"vendor", "mi_ext", "odm"}
_UNKNOWN = "UNKNOWN"

# Maps lowercased OS3/CN variant folder name → lowercased canonical (apps.list) folder name.
# Bidirectional: both the variant and the canonical resolve through _folder_canonical().
_FOLDER_ALIAS_MAP: dict[str, str] = {
    "fidoauthen2": "fidoauthen",
    "contentcatcheros3_1": "miuicontentcatcher",
    "lyrawos3cn": "miconnectservice",
    "miuicloudservice": "cloudservice",
    "micloudservice": "cloudservice",
    "miuifileexplorer": "fileexplorer",
    "miuiguardprovider": "guardprovider",
    "miuimicloudsync": "micloudsync",
    "miuinotificationcentert": "notificationcenter",
    "miuisecurityadd": "securityadd",
    "miuithememanager": "thememanager",
    "miuitouchassistant": "touchassistant",
    "miuixiaomiaccount": "xiaomiaccount",
    "nqnfcnci": "nfc",
    "nqnfc": "nfc",
}

# Prose / noise words that must never become app entries.
_PROSE_TOKENS: frozenset[str] = frozenset({
    "or", "fine", "and", "remove", "replace", "delate", "delete",
    "oat", "odex", "vdex", "any", "other", "waiting", "finish",
    "lines", "headings", "separators", "build.prop",
})


def _folder_canonical(name: str) -> str:
    """Return the alias-canonical lowercase form of a folder name."""
    lower = name.lower()
    return _FOLDER_ALIAS_MAP.get(lower, lower)


def _known_package(value: Any) -> str:
    package = str(value or "").strip()
    if not package or package.upper() == _UNKNOWN or package.lower() == "unknown":
        return ""
    return package


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
    return [partitions_root / partition / app_type for partition, app_type in _POLICY_LOCATION_PAIRS]


def _is_suspicious_package(pkg: str) -> bool:
    """Return True if *pkg* looks like an Android component class or system UID,
    not a real installable-app package root.  These must never drive deletions."""
    if not pkg or pkg.upper() == _UNKNOWN:
        return False
    return _is_rejected_package(pkg)


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


def _normalize_section(line: str) -> tuple[str, str] | None:
    cleaned = re.sub(r"\s+", "", line.strip().lower())
    if not cleaned or "/" not in cleaned:
        return None
    normalized = _normalize_expected_path(cleaned + "/_placeholder")
    if normalized:
        partition, app_type, _name = normalized
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
        # Skip known prose / noise tokens explicitly so they can never become app entries.
        if line.lower() in _PROSE_TOKENS:
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
                entries.append(
                    {
                        "name": path_name,
                        "expected_folder_name": path_name,
                        "package": next_line,
                        "expected_package": next_line,
                        "section": path_app_type,
                        "partition": path_partition,
                        "app_type": path_app_type,
                        "expected_path": f"{path_partition}/{path_app_type}/{path_name}",
                        "expected_apk_name": f"{path_name}.apk",
                    }
                )
                i = j + 1
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
                "expected_folder_name": name,
                "package": package,
                "expected_package": package,
                "section": app_type,
                "partition": partition,
                "app_type": app_type,
                "expected_path": f"{partition}/{app_type}/{name}",
                "expected_apk_name": f"{name}.apk",
            }
        )
    return entries


def _find_apk(folder: Path, expected_name: str = "") -> Path | None:
    apks = sorted(folder.rglob("*.apk"))
    if not apks:
        return None
    expected_lower = f"{expected_name.lower()}.apk" if expected_name else ""
    for apk in apks:
        if expected_lower and apk.name.lower() == expected_lower:
            return apk
    return sorted(apks, key=lambda p: (-p.stat().st_size, p.as_posix()))[0]


def _package_tools_status() -> dict[str, list[str]]:
    names = ["aapt", "apkanalyzer", "bundletool"]
    available = [name for name in names if shutil.which(name)]
    return {"available": available, "missing": [name for name in names if name not in available]}


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
        # Parse only the manifest package attribute — do not accept raw output lines
        match = re.search(r"package: name='([^']+)'", output) or re.search(r"package=\"([^\"]+)\"", output)
        if match:
            candidate = match.group(1).strip()
        elif source == "apkanalyzer":
            # apkanalyzer application-id outputs one line: the package id
            candidate = output.splitlines()[0].strip()
        else:
            continue
        if _is_package_name(candidate) and not _is_rejected_package(candidate):
            confidence = "medium" if source == "bundletool" and not match else "high"
            return candidate, source, confidence
    return "", "unknown", "low"


def _package_from_manifest(apk: Path) -> tuple[str, str, str]:
    try:
        with zipfile.ZipFile(apk) as zf:
            data = zf.read("AndroidManifest.xml")
    except Exception:
        return "", "unknown", "low"
    text = "\n".join(
        (
            data.decode("utf-8", errors="ignore"),
            data.decode("utf-16le", errors="ignore"),
        )
    )
    # Priority 1+2: explicit package= attribute from manifest root
    for pattern in (r'package\s*=\s*"([^"]+)"', r"package\s*=\s*'([^']+)'"):
        match = re.search(pattern, text)
        if match:
            candidate = match.group(1).strip()
            if _is_package_name(candidate) and not _is_rejected_package(candidate):
                return candidate, "manifest", "medium"
    # Priority 3: broad search with strict validation — no fallback for manifest tokens
    for m in re.finditer(r"\b([A-Za-z][A-Za-z0-9_]*(?:\.[A-Za-z0-9_]+){2,})\b", text):
        candidate = m.group(1).strip()
        if _is_package_name(candidate) and not _is_rejected_package(candidate):
            return candidate, "manifest", "medium"
    return "", "unknown", "low"


def _extract_package(apk: Path | None, inventory_package: str = "") -> tuple[str, str, str]:
    if apk:
        package, source, confidence = _package_from_tool(apk)
        if package:
            return package, source, confidence
        package, source, confidence = _package_from_manifest(apk)
        if package:
            return package, source, confidence
    fallback = _known_package(inventory_package)
    if fallback and _is_package_name(fallback) and not _is_rejected_package(fallback):
        return fallback, "inventory", "medium"
    return _UNKNOWN, "unknown", "low"


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
    # Only scan policy partitions — vendor/mi_ext/odm are never touched.
    for partition, app_type in _POLICY_LOCATION_PAIRS:
        base = partitions_root / partition / app_type
        if not base.is_dir():
            continue
        for folder in sorted(p for p in base.iterdir() if p.is_dir()):
            inv = inventory.get(str(folder.resolve()), {})
            apk = _find_apk(folder, folder.name)
            package, source, confidence = _extract_package(apk, str(inv.get("package_name") or ""))
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
    seen = {a["absolute_path"] for a in apps}
    for inv in scanned_apps:
        # Skip non-policy partitions from inventory (vendor, mi_ext, odm, …).
        inv_partition = str(inv.get("partition") or "")
        if inv_partition and inv_partition not in _POLICY_PARTITIONS:
            continue
        resolved = _resolve_app_path(inv.get("absolute_path") or inv.get("found_at") or inv.get("path") or "", partitions_root)
        if not resolved or str(resolved) in seen:
            continue
        package = _known_package(inv.get("package_name")) or _UNKNOWN
        source = "inventory" if package != _UNKNOWN else "unknown"
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


def _write_matching_debug_report(
    reports_dir: Path,
    scanned: list[dict[str, Any]],
    expected: list[dict[str, str]],
    match_stats: dict[str, int] | None = None,
    alias_matches: list[dict[str, str]] | None = None,
    missing_apps: list[dict[str, Any]] | None = None,
) -> None:
    reports_dir.mkdir(parents=True, exist_ok=True)
    expected_packages = {e["package"].lower() for e in expected if _known_package(e.get("package"))}
    scanned_packages = {str(a.get("package_name") or "").lower() for a in scanned if _known_package(a.get("package_name"))}
    duplicate_expected = sorted(pkg for pkg in expected_packages if sum(1 for e in expected if e["package"].lower() == pkg) > 1)
    duplicate_scanned = sorted(pkg for pkg in scanned_packages if sum(1 for a in scanned if str(a.get("package_name") or "").lower() == pkg) > 1)

    ms = match_stats or {}
    lines = [
        "DeadZone Stable Matching Debug Report",
        "=====================================",
        "",
        "match stats:",
        f"  matched_by_package                : {ms.get('matched_by_package', 0)}",
        f"  matched_by_package_moved          : {ms.get('matched_by_package_moved', 0)}",
        f"  matched_by_folder                 : {ms.get('matched_by_folder', 0)}",
        f"  matched_by_alias                  : {ms.get('matched_by_alias', 0)}",
        f"  matched_by_path                   : {ms.get('matched_by_path', 0)}",
        f"  package_unknown_but_folder_matched : {ms.get('package_unknown_but_folder_matched', 0)}",
        f"  real_missing                      : {ms.get('real_missing', 0)}",
        f"  ambiguous_matches                 : {ms.get('ambiguous_matches', 0)}",
        f"  skipped_delete_vendor             : {ms.get('skipped_delete_vendor', 0)}",
        f"  skipped_delete_unknown_package    : {ms.get('skipped_delete_unknown_package', 0)}",
        f"  skipped_delete_ambiguous          : {ms.get('skipped_delete_ambiguous', 0)}",
        f"  skipped_delete_outside_allowed    : {ms.get('skipped_delete_outside_allowed', 0)}",
    ]

    if alias_matches:
        lines += ["", "alias matches:"]
        for am in alias_matches:
            lines.append(f"  - expected={am['expected_folder']} scanned={am['scanned_folder']} canonical={am['canonical']}")

    lines += ["", "top 50 scanned apps:"]
    for app in scanned[:50]:
        lines.append(
            "  - "
            f"partition={app.get('partition')} | "
            f"app_type={app.get('app_type') or app.get('type')} | "
            f"folder_name={app.get('folder_name') or app.get('name')} | "
            f"package_name={app.get('package_name')} | "
            f"package_source={app.get('package_source')} | "
            f"package_confidence={app.get('package_confidence')} | "
            f"apk_path={app.get('apk_path') or '(none)'}"
        )
    if not scanned:
        lines.append("  (none)")

    lines += ["", "top 50 expected apps:"]
    for entry in expected[:50]:
        lines.append(
            "  - "
            f"partition={entry.get('partition')} | "
            f"app_type={entry.get('app_type')} | "
            f"folder={entry.get('name')} | "
            f"package={entry.get('package')} | "
            f"expected_path={entry.get('expected_path')}"
        )
    if not expected:
        lines.append("  (none)")

    if missing_apps:
        lines += ["", "top 50 missing apps (after folder/path matching):"]
        for m in missing_apps[:50]:
            lines.append(
                "  - "
                f"partition={m.get('expected_partition')} | "
                f"app_type={m.get('expected_app_type')} | "
                f"folder={m.get('name')} | "
                f"package={m.get('package')} | "
                f"expected_path={m.get('expected_path')}"
            )

    sections = (
        ("common packages between scanned and expected", sorted(expected_packages & scanned_packages)),
        ("packages in expected but not scanned", sorted(expected_packages - scanned_packages)),
        ("packages in scanned but not expected", sorted(scanned_packages - expected_packages)),
        ("duplicate expected packages", duplicate_expected),
        ("duplicate scanned packages", duplicate_scanned),
    )
    for title, packages in sections:
        lines += ["", f"{title}:"]
        lines.extend(f"  - {pkg}" for pkg in packages[:500])
        if len(packages) > 500:
            lines.append(f"  ... {len(packages) - 500} more")
        if not packages:
            lines.append("  (none)")
    (reports_dir / "stable_matching_debug_report.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_app_safety_report(reports_dir: Path, guard: dict[str, Any], classification: dict[str, list], expected_count: int) -> None:
    reports_dir.mkdir(parents=True, exist_ok=True)
    ms = guard
    lines = [
        "DeadZone Stable App Safety Report",
        "==================================",
        f"expected_apps_count              : {expected_count}",
        f"scanned_apps_count               : {ms.get('scanned_apps_count', 0)}",
        f"matched_expected_count           : {ms.get('matched_expected_count', 0)}",
        f"matched_expected_ratio           : {ms.get('matched_expected_ratio', 0.0):.3f}",
        f"matched_by_package               : {ms.get('matched_by_package', 0)}",
        f"matched_by_folder                : {ms.get('matched_by_folder', 0)}",
        f"matched_by_alias                 : {ms.get('matched_by_alias', 0)}",
        f"matched_by_path                  : {ms.get('matched_by_path', 0)}",
        f"package_unknown_but_folder_matched: {ms.get('package_unknown_but_folder_matched', 0)}",
        f"real_missing                     : {ms.get('real_missing', 0)}",
        f"kept_apps                        : {ms.get('kept_apps', 0)}",
        f"missing_apps                     : {ms.get('missing_apps', 0)}",
        f"delete_candidates                : {ms.get('delete_candidates', 0)}",
        f"unknown_package_count            : {ms.get('unknown_package_count', 0)}",
        f"safety_guard_status              : {ms.get('status', 'unknown')}",
        f"safety_guard_reason              : {ms.get('reason') or '(none)'}",
    ]
    alias_list = classification.get("alias_matches") or []
    if alias_list:
        lines += ["", "alias matches used:"]
        for am in alias_list:
            lines.append(f"  - expected={am['expected_folder']} scanned={am['scanned_folder']} canonical={am['canonical']}")
    (reports_dir / "stable_app_safety_report.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


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
        "expected_folder_name": entry.get("expected_folder_name") or name,
        "expected_package": entry.get("expected_package") or entry.get("package", ""),
        "expected_path": entry.get("expected_path") or f"{partition}/{app_type}/{name}",
        "expected_apk_name": entry.get("expected_apk_name") or f"{name}.apk",
    }


def _classify(scanned_apps: list[dict[str, Any]], expected: list[dict[str, str]], allowed: list[Path]) -> dict[str, list]:
    by_pkg = _expected_by_package(expected)

    # Build package index (trusted known packages only) and location index.
    # Only index apps from policy partitions — vendor apps must never drive any
    # matching or deletion decision.
    scanned_by_pkg: dict[str, list[dict[str, Any]]] = {}
    scanned_by_location: dict[tuple[str, str, str], dict[str, Any]] = {}

    for app in scanned_apps:
        if "app_type" not in app:
            app["app_type"] = str(app.get("type") or "")
        if "folder_name" not in app:
            app["folder_name"] = str(app.get("name") or "")
        if "absolute_path" not in app:
            app["absolute_path"] = str(app.get("found_at") or "")

        # Vendor (and other non-policy) apps are excluded from all indices.
        if app.get("partition", "") not in _POLICY_PARTITIONS:
            continue

        pkg = str(app.get("package_name") or "").strip()
        loc_key: tuple[str, str, str] = (
            app.get("partition", ""),
            app.get("app_type", ""),
            app["folder_name"].lower(),
        )
        scanned_by_location[loc_key] = app

        # Only index packages that are real app package names (not suspicious/unknown).
        if pkg and pkg.upper() != _UNKNOWN and pkg.lower() != "unknown" and not _is_suspicious_package(pkg):
            scanned_by_pkg.setdefault(pkg.lower(), []).append(app)

    kept: list[dict[str, Any]] = []
    to_rename: list[dict[str, Any]] = []
    to_move: list[dict[str, Any]] = []   # wrong allowed partition → will be moved
    missing: list[dict[str, Any]] = []
    matched_paths: set[str] = set()
    ambiguous_packages: set[str] = set()

    match_stats: dict[str, int] = {
        "matched_by_package": 0,
        "matched_by_folder": 0,
        "matched_by_alias": 0,
        "matched_by_path": 0,
        "matched_by_package_moved": 0,
        "package_unknown_but_folder_matched": 0,
        "real_missing": 0,
        "ambiguous_matches": 0,
        "skipped_delete_vendor": 0,
        "skipped_delete_unknown_package": 0,
        "skipped_delete_ambiguous": 0,
        "skipped_delete_outside_allowed": 0,
    }
    alias_matches: list[dict[str, str]] = []

    for raw_entry in expected:
        entry = _normalize_expected(raw_entry)
        pkg_key = entry["package"].lower()
        actuals = scanned_by_pkg.get(pkg_key) or []
        exact = next((a for a in actuals if a["partition"] == entry["partition"] and a["app_type"] == entry["app_type"] and a["folder_name"] == entry["name"]), None)
        same_place = next((a for a in actuals if a["partition"] == entry["partition"] and a["app_type"] == entry["app_type"]), None)

        if exact and exact.get("apk_name") and exact.get("apk_name") != entry["expected_apk_name"]:
            matched_paths.add(exact["absolute_path"])
            match_stats["matched_by_package"] += 1
            to_rename.append({**exact, "status": "FOUND_RENAMED", "action": "RENAME_TO_EXPECTED", "expected": entry, "package": entry["package"], "expected_name": entry["name"], "actual_name": exact["folder_name"], "found_at": exact["absolute_path"], "in_allowed": _is_in_allowed(exact["absolute_path"], allowed), "match_method": "package"})
        elif exact:
            matched_paths.add(exact["absolute_path"])
            match_stats["matched_by_package"] += 1
            kept.append({**exact, "status": "FOUND", "action": "KEEP", "expected": entry, "package": entry["package"], "found_at": exact["absolute_path"], "match_method": "package"})
        elif same_place:
            matched_paths.add(same_place["absolute_path"])
            match_stats["matched_by_package"] += 1
            to_rename.append({**same_place, "status": "FOUND_RENAMED", "action": "RENAME_TO_EXPECTED", "expected": entry, "package": entry["package"], "expected_name": entry["name"], "actual_name": same_place["folder_name"], "found_at": same_place["absolute_path"], "in_allowed": _is_in_allowed(same_place["absolute_path"], allowed), "match_method": "package"})
        elif actuals:
            # Package found in wrong allowed partition/path → MOVE to expected location.
            match_stats["matched_by_package"] += 1
            match_stats["matched_by_package_moved"] += 1
            if len(actuals) > 1:
                ambiguous_packages.add(pkg_key)
                match_stats["ambiguous_matches"] += 1
            for actual in actuals:
                matched_paths.add(actual["absolute_path"])
            # Take the first actual as the move target; mark all as matched.
            to_move.append({
                **actuals[0],
                "status": "FOUND_WRONG_LOCATION",
                "action": "MOVE_TO_EXPECTED",
                "expected": entry,
                "package": entry["package"],
                "found_at": actuals[0]["absolute_path"],
                "match_method": "package_moved",
            })
        else:
            # No package match — try folder-name and alias matching.
            partition = entry["partition"]
            app_type = entry["app_type"]
            expected_folder_lower = entry["name"].lower()
            expected_canonical = _folder_canonical(entry["name"])

            folder_match: dict[str, Any] | None = None
            match_method = ""

            # Step 1: exact case-insensitive partition+app_type+folder_name match.
            loc_key = (partition, app_type, expected_folder_lower)
            candidate = scanned_by_location.get(loc_key)
            if candidate is not None and candidate["absolute_path"] not in matched_paths:
                folder_match = candidate
                match_method = "folder"

            # Step 2: alias match — scanned folder whose canonical equals the expected canonical.
            if folder_match is None:
                for loc_k, app in scanned_by_location.items():
                    if loc_k[0] != partition or loc_k[1] != app_type:
                        continue
                    if app["absolute_path"] in matched_paths:
                        continue
                    if _folder_canonical(app["folder_name"]) == expected_canonical:
                        folder_match = app
                        match_method = "alias"
                        alias_matches.append({
                            "expected_folder": entry["name"],
                            "scanned_folder": app["folder_name"],
                            "canonical": expected_canonical,
                        })
                        break

            if folder_match is not None:
                abs_path = folder_match["absolute_path"]
                matched_paths.add(abs_path)
                scanned_pkg = str(folder_match.get("package_name") or "").strip()
                is_unknown_pkg = not scanned_pkg or scanned_pkg.upper() == _UNKNOWN or scanned_pkg.lower() == "unknown"

                if match_method == "folder":
                    match_stats["matched_by_folder"] += 1
                else:
                    match_stats["matched_by_alias"] += 1
                if is_unknown_pkg:
                    match_stats["package_unknown_but_folder_matched"] += 1

                kept.append({
                    **folder_match,
                    "status": "FOUND",
                    "action": "KEEP",
                    "expected": entry,
                    "package": entry["package"],
                    "found_at": abs_path,
                    "match_method": match_method,
                })
            else:
                match_stats["real_missing"] += 1
                missing.append({
                    "status": "MISSING",
                    "action": "REPORT_ONLY",
                    "name": entry["name"],
                    "package": entry["package"],
                    "expected_partition": entry["partition"],
                    "expected_app_type": entry["app_type"],
                    "expected_path": entry["expected_path"],
                    "reason": "not found in system/system_ext/product",
                })

    extras: list[dict[str, Any]] = []
    outside: list[dict[str, Any]] = []
    unknown: list[dict[str, Any]] = []
    skipped_vendor: list[dict[str, Any]] = []

    for app in scanned_apps:
        abs_path = app["absolute_path"]
        if abs_path in matched_paths:
            continue
        pkg = str(app.get("package_name") or "").strip()
        partition = str(app.get("partition") or "")

        # VENDOR PROTECTION: never include vendor apps as delete candidates.
        if partition == "vendor":
            skipped_vendor.append({**app, "status": "SKIPPED_VENDOR", "action": "SKIP",
                                    "reason": "vendor partition is forbidden for Stable App Policy"})
            match_stats["skipped_delete_vendor"] += 1
            continue

        # Other non-policy partitions (odm, mi_ext, …).
        if partition not in _POLICY_PARTITIONS:
            outside.append({**app, "status": "OUTSIDE_ALLOWED", "action": "SKIP"})
            match_stats["skipped_delete_outside_allowed"] += 1
            continue

        # Unknown package → report only, never delete.
        if not pkg or pkg.upper() == _UNKNOWN or pkg.lower() == "unknown":
            unknown.append({**app, "status": "UNKNOWN_PACKAGE", "action": "REPORT_ONLY"})
            continue

        # Suspicious package name (component class, UID, etc.) → treat as unknown.
        if _is_suspicious_package(pkg):
            unknown.append({**app, "status": "SUSPICIOUS_PACKAGE", "action": "REPORT_ONLY"})
            match_stats["skipped_delete_unknown_package"] += 1
            continue

        # Ambiguous: package appears multiple times across scanned apps → don't delete.
        # Check both expected-match ambiguity AND unmatched-extra duplicates.
        is_ambiguous = pkg.lower() in ambiguous_packages
        if not is_ambiguous and len(scanned_by_pkg.get(pkg.lower(), [])) > 1:
            pkg_instances = scanned_by_pkg.get(pkg.lower(), [])
            if not any(a["absolute_path"] in matched_paths for a in pkg_instances):
                is_ambiguous = True
        if is_ambiguous:
            unknown.append({**app, "status": "AMBIGUOUS_PACKAGE", "action": "SKIP"})
            match_stats["skipped_delete_ambiguous"] += 1
            continue

        item = {**app, "status": "EXTRA", "action": "DELETE", "package": pkg, "found_at": abs_path}
        if pkg.lower() not in by_pkg and _is_in_allowed(abs_path, allowed):
            extras.append(item)
        elif not _is_in_allowed(abs_path, allowed):
            outside.append({**item, "status": "OUTSIDE_ALLOWED", "action": "SKIP"})
            match_stats["skipped_delete_outside_allowed"] += 1

    return {
        "kept": kept,
        "to_rename": to_rename,
        "to_move": to_move,
        "extra_in_allowed": extras,
        "skipped_outside": outside,
        "skipped_vendor": skipped_vendor,
        "missing": missing,
        "wrong_location": to_move,  # kept for backward compat (same list)
        "unknown": unknown,
        "match_stats": match_stats,
        "alias_matches": alias_matches,
    }


def _safety_thresholds() -> dict[str, Any]:
    return {
        "min_kept_apps": _env_int("DEADZONE_STABLE_MIN_KEPT_APPS", 20),
        "max_missing_apps": _env_int("DEADZONE_STABLE_MAX_MISSING_APPS", 80),
        "max_delete_candidates": _env_int("DEADZONE_STABLE_MAX_DELETE_CANDIDATES", 100),
        "min_match_ratio": _env_float("DEADZONE_STABLE_MIN_MATCH_RATIO", 0.40),
    }


def _stable_safety_guard(
    expected_count: int,
    classification: dict[str, list],
    enforce: bool,
    scanned_count: int = 0,
    package_tools: dict[str, list[str]] | None = None,
) -> dict[str, Any]:
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
        reasons.append("kept_apps below threshold")
    if missing > thresholds["max_missing_apps"]:
        reasons.append("missing_apps above threshold")
    if deletes > thresholds["max_delete_candidates"]:
        reasons.append("delete_candidates above threshold")
    if normal_rom and ratio < thresholds["min_match_ratio"]:
        reasons.append("matched_expected_ratio below threshold")
    if expected_count > 100 and matched < 50:
        reasons.append("matched_expected_count below safe minimum")
    status = "failed" if reasons and enforce else ("warning" if reasons else "passed")
    ms = classification.get("match_stats") or {}
    return {
        "status": status,
        "thresholds": thresholds,
        "reason": "; ".join(reasons),
        "reasons": reasons,
        "scanned_apps_count": scanned_count,
        "expected_apps_count": expected_count,
        "matched_expected_count": matched,
        "matched_expected_ratio": ratio,
        "kept_apps": kept,
        "missing_apps": missing,
        "delete_candidates": deletes,
        "unknown_package_count": len(classification["unknown"]),
        "package_tools_available": (package_tools or {}).get("available", []),
        "package_tools_missing": (package_tools or {}).get("missing", []),
        "matched_by_package": ms.get("matched_by_package", 0),
        "matched_by_folder": ms.get("matched_by_folder", 0),
        "matched_by_alias": ms.get("matched_by_alias", 0),
        "matched_by_path": ms.get("matched_by_path", 0),
        "package_unknown_but_folder_matched": ms.get("package_unknown_but_folder_matched", 0),
        "real_missing": ms.get("real_missing", 0),
    }


def _unsafe_payload(guard: dict[str, Any]) -> dict[str, str]:
    return {
        "error_type": "STABLE_APP_MATCHING_UNSAFE",
        "cause": f"Matching unsafe: matched {guard.get('matched_expected_count')} of {guard.get('expected_apps_count')} expected apps",
        "telegram_cause": f"Matching unsafe: matched {guard.get('matched_expected_count')} of {guard.get('expected_apps_count')} expected apps",
        "suggested_fix": "Fix package extraction or apps.list parsing before deleting apps",
        "suggested_check": "stable_matching_debug_report.txt and stable_package_scan_report.json",
        "details": f"Matching unsafe: matched {guard.get('matched_expected_count')} of {guard.get('expected_apps_count')} expected apps",
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


def _execute_moves(
    to_move: list[dict[str, Any]],
    partitions_root: Path,
    enforce: bool,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[str], set[str]]:
    """Move app folders from wrong allowed partition to the expected partition/path.

    vendor is never a valid source or destination.
    Returns (moved, skipped, errors, changed_partitions).
    """
    moved: list[dict[str, Any]] = []
    skipped: list[dict[str, Any]] = []
    errors: list[str] = []
    changed: set[str] = set()

    for item in to_move:
        entry = _normalize_expected(
            item.get("expected")
            or {
                "name": item.get("expected_name", ""),
                "package": item.get("package", ""),
                "partition": item.get("partition", ""),
                "app_type": item.get("app_type", ""),
            }
        )
        src = Path(item["found_at"])
        dest_partition = entry["partition"]
        dest_app_type = entry["app_type"]
        dest_name = entry.get("expected_folder_name") or entry["name"]
        target = partitions_root / dest_partition / dest_app_type / dest_name
        src_partition = str(item.get("partition", ""))

        if not enforce:
            skipped.append({**item, "enacted": False, "reason": "report-only mode"})
            continue
        # VENDOR PROTECTION: refuse to move from or to vendor.
        if src_partition == "vendor" or src_partition not in _POLICY_PARTITIONS:
            skipped.append({**item, "enacted": False,
                            "reason": f"source partition {src_partition!r} is not a policy partition"})
            continue
        if dest_partition == "vendor" or dest_partition not in _POLICY_PARTITIONS:
            skipped.append({**item, "enacted": False,
                            "reason": f"destination partition {dest_partition!r} is not a policy partition"})
            continue
        if not src.exists():
            skipped.append({**item, "enacted": False, "reason": "source path not found"})
            continue
        if target.exists() and target.resolve() != src.resolve():
            errors.append(f"CONFLICT: move target already exists: {target}")
            continue
        try:
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.resolve() != src.resolve():
                shutil.move(str(src), str(target))
            # Remove now-empty old parent dir (best-effort).
            try:
                src.parent.rmdir()
            except OSError:
                pass
            apk_change = _rename_apk(target, dest_name)
            result = {**item, "enacted": True, "new_path": str(target),
                      "found_at": str(target), "action": "MOVED"}
            if apk_change:
                result.update(apk_change)
            moved.append(result)
            # Mark both partitions modified — never vendor.
            if src_partition in _POLICY_PARTITIONS:
                changed.add(src_partition)
            if dest_partition in _POLICY_PARTITIONS:
                changed.add(dest_partition)
        except Exception as exc:
            errors.append(f"MOVE FAILED: {src} -> {target}: {exc}")

    return moved, skipped, errors, changed


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
    _write_inventory(inventory_dir / "apps_moved.txt", data.get("moved_apps") or [], lambda r: f"{r.get('found_at')} -> {r.get('new_path')} {r.get('package')}")
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
    for key in (
        "kept_apps", "renamed_apps", "moved_apps", "skipped_rename_apps", "skipped_move_apps",
        "missing_apps", "found_wrong_location_apps", "unknown_package_apps",
        "delete_candidates", "deleted_extra_apps", "skipped_delete_apps",
        "skipped_delete_vendor", "skipped_delete_unknown_package", "skipped_delete_ambiguous",
        "skipped_outside_allowed_locations", "changed_partitions",
    ):
        lines.append(f"  {key}: {summary.get(key, 0)}")
    guard = data.get("safety_guard") if isinstance(data.get("safety_guard"), dict) else {}
    if guard:
        lines += ["", "safety_guard:", f"  status: {guard.get('status')}", f"  reason: {guard.get('reason') or '(none)'}"]
    for title, key in (
        ("KEPT APPS", "kept_apps"),
        ("RENAMED APPS", "renamed_apps"),
        ("MOVED APPS (wrong allowed partition → expected)", "moved_apps"),
        ("SKIPPED RENAME APPS", "skipped_rename_apps"),
        ("SKIPPED MOVE APPS", "skipped_move_apps"),
        ("MISSING APPS", "missing_apps"),
        ("UNKNOWN PACKAGE APPS", "unknown_package_apps"),
        ("DELETE CANDIDATES", "delete_candidates"),
        ("DELETED EXTRA APPS", "deleted_extra_apps"),
        ("SKIPPED DELETE APPS", "skipped_delete_apps"),
        ("SKIPPED DELETE (vendor — forbidden)", "skipped_delete_vendor_apps"),
    ):
        lines += ["", f"{title}:"]
        rows = data.get(key) or []
        lines.extend(
            f"  - {r.get('path') or r.get('expected_path') or r.get('found_at')} "
            f"{r.get('package') or r.get('package_name')}"
            for r in rows
        )
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
    package_tools = _package_tools_status()
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
            "package_tools_available": len(package_tools["available"]),
            "package_tools_missing": len(package_tools["missing"]),
        },
        "package_tools_available": package_tools["available"],
        "package_tools_missing": package_tools["missing"],
        "scanned_apps": len(scanned),
        "unknown_package_apps": [a for a in scanned if str(a.get("package_name")).upper() == _UNKNOWN],
        "matched_by_package": sorted(expected_packages & scanned_known_packages),
        "unmatched_known_packages": sorted(scanned_known_packages - expected_packages),
    }
    _write_scan_reports(reports_dir, scan_data)
    # Matching debug report is updated again after classification with match_stats (see below).
    _write_matching_debug_report(reports_dir, scanned, expected)

    allowed = _build_allowed_dirs(partitions_root)
    classification = _classify(scanned, expected, allowed)
    # Re-write debug report with match_stats now that classification is done.
    _write_matching_debug_report(
        reports_dir, scanned, expected,
        match_stats=classification.get("match_stats"),
        alias_matches=classification.get("alias_matches"),
        missing_apps=classification.get("missing"),
    )
    # Collect non-policy-partition apps from inventory for reporting.
    # These are never scanned, never deleted, never moved — just noted.
    vendor_inventory_apps: list[dict[str, Any]] = []
    outside_inventory_apps: list[dict[str, Any]] = []
    for _inv_app in scanned_apps:
        _part = str(_inv_app.get("partition", "")).lower()
        if not _part or _part in _POLICY_PARTITIONS:
            continue
        if _part == "vendor":
            vendor_inventory_apps.append({
                **_inv_app,
                "status": "SKIPPED_VENDOR",
                "action": "SKIP",
                "reason": "vendor partition is forbidden for Stable App Policy",
            })
        else:
            outside_inventory_apps.append({
                **_inv_app,
                "status": "OUTSIDE_ALLOWED",
                "action": "SKIP",
                "reason": f"partition {_part!r} is not a Stable App Policy partition",
            })
    vendor_inventory_count = len(vendor_inventory_apps)

    guard = _stable_safety_guard(len(expected), classification, enforce, len(scanned), package_tools)
    _write_app_safety_report(reports_dir, guard, classification, len(expected))

    ms = classification.get("match_stats") or {}

    def _make_summary(data_: dict[str, Any], moved_: list, skipped_move_: list) -> dict[str, Any]:
        return {
            "expected_apps_count": len(expected),
            "matched_expected_count": guard["matched_expected_count"],
            "matched_expected_ratio": guard["matched_expected_ratio"],
            "kept_apps": len(data_["kept_apps"]),
            "renamed_apps": len(data_["renamed_apps"]),
            "moved_apps": len(moved_),
            "skipped_rename_apps": len(data_["skipped_rename_apps"]),
            "skipped_move_apps": len(skipped_move_),
            "missing_apps": len(data_["missing_apps"]),
            "found_wrong_location_apps": len(data_["found_wrong_location_apps"]),
            "unknown_package_apps": len(data_["unknown_package_apps"]),
            "delete_candidates": len(data_["delete_candidates"]),
            "deleted_extra_apps": len(data_["deleted_extra_apps"]),
            "skipped_delete_apps": len(data_["skipped_delete_apps"]),
            "skipped_delete_vendor": ms.get("skipped_delete_vendor", 0) + vendor_inventory_count,
            "skipped_delete_unknown_package": ms.get("skipped_delete_unknown_package", 0),
            "skipped_delete_ambiguous": ms.get("skipped_delete_ambiguous", 0),
            "skipped_outside_allowed_locations": len(data_["skipped_outside_allowed_locations"]),
            "changed_partitions": len(data_["changed_partitions"]),
            # legacy short keys
            "kept": len(data_["kept_apps"]),
            "renamed": len(data_["renamed_apps"]),
            "missing": len(data_["missing_apps"]),
            "deleted_extra": len(data_["deleted_extra_apps"]),
            "skipped_outside": len(data_["skipped_outside_allowed_locations"]),
        }

    if guard["status"] == "failed":
        payload = _unsafe_payload(guard)
        moved_guard: list[dict[str, Any]] = []
        skipped_move_guard: list[dict[str, Any]] = classification["to_move"]
        vendor_skipped = classification.get("skipped_vendor") or []
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
            "moved_apps": moved_guard,
            "skipped_rename_apps": classification["to_rename"],
            "skipped_move_apps": skipped_move_guard,
            "missing_apps": classification["missing"],
            "found_wrong_location_apps": classification["to_move"],
            "unknown_package_apps": classification["unknown"],
            "delete_candidates": classification["extra_in_allowed"],
            "deleted_extra_apps": [],
            "skipped_delete_apps": classification["extra_in_allowed"],
            "skipped_delete_vendor_apps": vendor_skipped,
            "skipped_outside_allowed_locations": classification["skipped_outside"] + outside_inventory_apps,
            "changed_partitions": [],
            "safety_guard": guard,
            "errors": [payload],
        }
        data["summary"] = _make_summary(data, moved_guard, skipped_move_guard)
        workspace_root = reports_dir.parent
        _write_inventory_files(workspace_root / "inventory", data)
        reports_dir.mkdir(parents=True, exist_ok=True)
        _write_txt_report(reports_dir / "stable_app_policy_report.txt", data)
        (reports_dir / "stable_app_policy_report.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        raise RuntimeError(json.dumps(payload, sort_keys=True))

    # Execute moves BEFORE renames/deletes so the source paths are still valid.
    moved, skipped_move, move_errors, move_changed = _execute_moves(
        classification["to_move"], partitions_root, enforce
    )
    renamed, skipped_rename, rename_errors, rename_changed = _execute_renames(classification["to_rename"], enforce)
    deleted, skipped_delete, skipped_outside_delete, delete_errors, delete_changed = _execute_deletes(
        classification["extra_in_allowed"], enforce, allowed
    )
    all_errors = move_errors + rename_errors + delete_errors

    # Ensure vendor is NEVER in changed_partitions.
    raw_changed = move_changed | rename_changed | delete_changed
    changed_partitions = sorted(
        p for p in raw_changed
        if p and p != "vendor" and p in _POLICY_PARTITIONS
    )
    if enforce and all_errors:
        raise RuntimeError("Stable App Policy failed with errors:\n" + "\n".join(all_errors))

    vendor_skipped = classification.get("skipped_vendor") or []
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
        "moved_apps": moved,
        "skipped_rename_apps": skipped_rename,
        "skipped_move_apps": skipped_move,
        "missing_apps": classification["missing"],
        "found_wrong_location_apps": moved + skipped_move,  # backward compat
        "unknown_package_apps": classification["unknown"],
        "delete_candidates": classification["extra_in_allowed"],
        "deleted_extra_apps": deleted,
        "skipped_delete_apps": skipped_delete,
        "skipped_delete_vendor_apps": vendor_skipped,
        "skipped_outside_allowed_locations": classification["skipped_outside"] + skipped_outside_delete + outside_inventory_apps,
        "changed_partitions": changed_partitions,
        "safety_guard": guard,
        "errors": all_errors,
    }
    data["summary"] = _make_summary(data, moved, skipped_move)

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
        f"moved={len(data['moved_apps'])} "
        f"missing={len(data['missing_apps'])} deleted_extra={len(data['deleted_extra_apps'])} "
        f"unknown={len(data['unknown_package_apps'])} vendor_skipped={len(vendor_skipped)}"
    )
    return data
