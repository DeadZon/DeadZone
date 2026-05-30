from __future__ import annotations

import csv
import re
import zipfile
from pathlib import Path
from typing import Any

from factory.core.workspace import Workspace, write_json


PARTITIONS = ("system", "product", "vendor", "system_ext", "mi_ext", "odm")
APP_PATHS = (
    "app",
    "priv-app",
    "product/app",
    "product/priv-app",
    "system/app",
    "system/priv-app",
    "system_ext/app",
    "system_ext/priv-app",
    "mi_ext/app",
    "mi_ext/priv-app",
    "vendor/app",
    "vendor/priv-app",
    "odm/app",
    "odm/priv-app",
)


def _relative(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


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


def _printable_manifest_text(apk: Path) -> str:
    try:
        with zipfile.ZipFile(apk) as zf:
            data = zf.read("AndroidManifest.xml")
    except Exception:
        return ""
    chunks = [
        data.decode("utf-8", errors="ignore"),
        data.decode("utf-16le", errors="ignore"),
    ]
    return "\n".join(chunks)


def _package_name(apk: Path) -> str:
    text = _printable_manifest_text(apk)
    if not text:
        return "unknown"
    patterns = [
        r'package\s*=\s*"([^"]+)"',
        r"package\s*=\s*'([^']+)'",
        r"\b([a-zA-Z][a-zA-Z0-9_]*(?:\.[a-zA-Z0-9_]+){2,})\b",
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            value = match.group(1).strip()
            if "." in value and "/" not in value:
                return value
    return "unknown"


def _vendor_guess(name: str, package_name: str, path: str) -> str:
    haystack = f"{name} {package_name} {path}".lower()
    if any(token in haystack for token in ("xiaomi", "miui", "hyperos", "micode", "mi.", "com.miui", "com.xiaomi")):
        return "Xiaomi"
    if any(token in haystack for token in ("google", "gms", "gboard", "youtube", "android.vending", "com.google")):
        return "Google"
    if package_name.startswith("android") or package_name.startswith("com.android"):
        return "Android"
    return "Unknown"


def _category_guess(name: str, package_name: str, path: str) -> str:
    haystack = f"{name} {package_name} {path}".lower()
    categories = {
        "launcher": ("launcher", "home"),
        "camera": ("camera", "gallery"),
        "telephony": ("telephony", "ims", "dialer", "mms", "contacts"),
        "media": ("music", "video", "player", "media", "sound"),
        "browser": ("browser", "webview", "chrome"),
        "security": ("security", "permission", "guard", "privacy"),
        "setup": ("setup", "provision", "wizard"),
        "service": ("service", "daemon", "framework", "provider"),
        "store": ("vending", "store", "market", "getapps"),
    }
    for category, tokens in categories.items():
        if any(token in haystack for token in tokens):
            return category
    return "unknown"


def _app_scope(path: Path, partition_root: Path) -> tuple[str, Path] | None:
    rel_parts = path.relative_to(partition_root).parts
    for index, part in enumerate(rel_parts):
        if part in {"app", "priv-app"}:
            if index + 1 < len(rel_parts):
                return part, partition_root.joinpath(*rel_parts[: index + 2])
            return part, path
    return None


def _scan_partition(partition: str, root: Path) -> list[dict[str, Any]]:
    apps: dict[str, dict[str, Any]] = {}
    search_roots = []
    for rel in APP_PATHS:
        candidate = root / rel
        if candidate.is_dir():
            search_roots.append(candidate)
    for search_root in search_roots:
        for apk in sorted(search_root.rglob("*.apk")):
            scope = _app_scope(apk, root)
            if not scope:
                continue
            app_type, folder = scope
            key = folder.resolve().as_posix()
            entry = apps.setdefault(
                key,
                {
                    "partition": partition,
                    "name": folder.name if folder.is_dir() else apk.stem,
                    "path": _relative(folder, root),
                    "absolute_path": str(folder),
                    "type": app_type,
                    "apk_files": [],
                    "apk_count": 0,
                    "split_apk": False,
                    "package_name": "unknown",
                    "size": 0,
                    "vendor_guess": "Unknown",
                    "category_guess": "unknown",
                },
            )
            entry["apk_files"].append(_relative(apk, root))
    for entry in apps.values():
        apk_paths = [root / rel for rel in entry["apk_files"]]
        entry["apk_files"] = sorted(entry["apk_files"])
        entry["apk_count"] = len(entry["apk_files"])
        entry["split_apk"] = len(entry["apk_files"]) > 1
        entry["size"] = _path_size(Path(entry["absolute_path"]))
        for apk in apk_paths:
            package = _package_name(apk)
            if package != "unknown":
                entry["package_name"] = package
                break
        entry["vendor_guess"] = _vendor_guess(entry["name"], entry["package_name"], entry["path"])
        entry["category_guess"] = _category_guess(entry["name"], entry["package_name"], entry["path"])
    return sorted(apps.values(), key=lambda item: (item["partition"], item["type"], item["path"]))


def _load_registry() -> set[str]:
    root = Path("factory/app_registry")
    if not root.is_dir():
        return set()
    packages: set[str] = set()
    package_re = re.compile(r"\b(?:package|package_name|id)\s*:\s*['\"]?([A-Za-z][A-Za-z0-9_]*(?:\.[A-Za-z0-9_]+)+)")
    bare_re = re.compile(r"\b([A-Za-z][A-Za-z0-9_]*(?:\.[A-Za-z0-9_]+){2,})\b")
    for path in sorted([*root.glob("*.yml"), *root.glob("*.yaml")]):
        text = path.read_text(encoding="utf-8", errors="ignore")
        packages.update(package_re.findall(text))
        packages.update(bare_re.findall(text))
    return packages


def _write_csv(path: Path, apps: list[dict[str, Any]]) -> None:
    fields = ["partition", "name", "package_name", "type", "path", "size", "apk_count", "split_apk", "vendor_guess", "category_guess"]
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for app in apps:
            writer.writerow({field: app.get(field, "") for field in fields})


def _write_text_outputs(ws: Workspace, data: dict[str, Any]) -> None:
    inv = ws.root / "inventory"
    apps = data.get("apps") or []
    lines = [
        "DeadZone Stable App Inventory",
        "=============================",
        f"total apps found: {data.get('total_apps_found')}",
        f"total APK files: {data.get('total_apk_files')}",
        "",
        "apps:",
    ]
    for app in apps:
        lines.append(
            f"- {app.get('partition')}/{app.get('path')} | {app.get('type')} | "
            f"{app.get('package_name')} | APKs={app.get('apk_count')} | size={app.get('size')} | {app.get('vendor_guess')}"
        )
    (inv / "apps_found.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")

    by_partition = []
    for partition, count in sorted((data.get("count_by_partition") or {}).items()):
        by_partition.append(f"{partition}: {count}")
        for app in [item for item in apps if item.get("partition") == partition]:
            by_partition.append(f"  - {app.get('path')} | {app.get('package_name')} | {app.get('size')}")
    (inv / "apps_by_partition.txt").write_text("\n".join(by_partition or ["(none)"]) + "\n", encoding="utf-8")

    missing = data.get("apps_missing_from_registry") or []
    (inv / "apps_missing_from_registry.txt").write_text("\n".join(missing or ["(none)"]) + "\n", encoding="utf-8")
    unknown = data.get("unknown_apps_not_in_registry") or []
    (inv / "apps_unknown.txt").write_text("\n".join(unknown or ["(none)"]) + "\n", encoding="utf-8")


def _write_report(ws: Workspace, data: dict[str, Any]) -> None:
    lines = [
        "DeadZone App Inventory Report",
        "=============================",
        "feature: Stable App Inventory",
        f"status: {data.get('status')}",
        f"total apps found: {data.get('total_apps_found')}",
        f"total APK files: {data.get('total_apk_files')}",
        f"Xiaomi apps count: {data.get('xiaomi_apps_count')}",
        f"Google apps count: {data.get('google_apps_count')}",
        f"unknown apps count: {data.get('unknown_apps_count')}",
        f"apps from registry found: {data.get('apps_from_registry_found')}",
        f"apps from registry missing: {data.get('apps_from_registry_missing')}",
        f"unknown apps not in registry: {len(data.get('unknown_apps_not_in_registry') or [])}",
        "",
        "count by partition:",
    ]
    for partition, count in sorted((data.get("count_by_partition") or {}).items()):
        lines.append(f"  - {partition}: {count}")
    lines += ["", "count by type:"]
    for app_type, count in sorted((data.get("count_by_type") or {}).items()):
        lines.append(f"  - {app_type}: {count}")
    lines += ["", "largest 100 app folders/files:"]
    for item in data.get("largest_100") or []:
        lines.append(f"  - {item.get('partition')}/{item.get('path')}: {item.get('size')} ({item.get('package_name')})")
    if not data.get("largest_100"):
        lines.append("  (none)")
    (ws.reports / "app_inventory_report.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def generate_app_inventory(ws: Workspace, extraction: dict[str, Any] | None = None) -> dict[str, Any]:
    inv = ws.root / "inventory"
    inv.mkdir(parents=True, exist_ok=True)
    apps: list[dict[str, Any]] = []
    for partition in PARTITIONS:
        root = ws.partitions / partition
        if root.is_dir():
            apps.extend(_scan_partition(partition, root))

    registry = _load_registry()
    found_packages = {app["package_name"] for app in apps if app.get("package_name") and app.get("package_name") != "unknown"}
    registry_found = sorted(found_packages & registry)
    registry_missing = sorted(registry - found_packages)
    unknown_not_registry = sorted(
        f"{app.get('partition')}/{app.get('path')} | {app.get('name')}"
        for app in apps
        if app.get("package_name") == "unknown" or app.get("package_name") not in registry
    )
    count_by_partition: dict[str, int] = {}
    count_by_type: dict[str, int] = {}
    for app in apps:
        count_by_partition[app["partition"]] = count_by_partition.get(app["partition"], 0) + 1
        count_by_type[app["type"]] = count_by_type.get(app["type"], 0) + 1

    data = {
        "feature": "Stable App Inventory",
        "status": "ok",
        "total_apps_found": len(apps),
        "total_apk_files": sum(int(app.get("apk_count") or 0) for app in apps),
        "count_by_partition": dict(sorted(count_by_partition.items())),
        "count_by_type": dict(sorted(count_by_type.items())),
        "xiaomi_apps_count": sum(1 for app in apps if app.get("vendor_guess") == "Xiaomi"),
        "google_apps_count": sum(1 for app in apps if app.get("vendor_guess") == "Google"),
        "unknown_apps_count": sum(1 for app in apps if app.get("vendor_guess") == "Unknown"),
        "apps_from_registry_found": len(registry_found),
        "apps_from_registry_missing": len(registry_missing),
        "registry_package_count": len(registry),
        "apps_missing_from_registry": registry_missing,
        "unknown_apps_not_in_registry": unknown_not_registry,
        "largest_100": sorted(apps, key=lambda item: int(item.get("size") or 0), reverse=True)[:100],
        "extraction_summary": (extraction or {}).get("summary") if isinstance(extraction, dict) else {},
        "apps": apps,
    }
    write_json(inv / "apps_found.json", data)
    write_json(ws.meta / "app_inventory.json", {key: value for key, value in data.items() if key != "apps"})
    _write_csv(inv / "apps_found.csv", apps)
    _write_text_outputs(ws, data)
    _write_report(ws, data)
    print(f"[APP INVENTORY] Apps found: {data['total_apps_found']}")
    print(f"[APP INVENTORY] Unknown: {data['unknown_apps_count']}")
    return data
