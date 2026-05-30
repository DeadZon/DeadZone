"""Stable App Policy Enforcement — Stage: stable_app_policy.

For stable style: enforces apps.list as the source of truth by renaming
misnamed app folders and deleting extra apps from allowed locations.
For non-stable styles: generates a report only, no filesystem changes.

Allowed scan/delete locations:
  system/app, system/priv-app
  product/app, product/priv-app
  system_ext/app, system_ext/priv-app
  vendor/app, vendor/priv-app
  mi_ext/app, mi_ext/priv-app
"""
from __future__ import annotations

import json
import shutil
from pathlib import Path
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from factory.state.build_state import BuildState

from factory.reports.app_inventory import _find_apps_list, _parse_apps_list


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


def _build_allowed_dirs(partitions_root: Path) -> list[Path]:
    return [partitions_root / partition / app_type
            for partition, app_type in _ALLOWED_LOCATION_PAIRS]


def _is_in_allowed(app_absolute: str, allowed: list[Path]) -> bool:
    try:
        p = Path(app_absolute)
        for d in allowed:
            try:
                p.relative_to(d)
                return True
            except ValueError:
                continue
    except Exception:
        pass
    return False


def _classify(
    scanned_apps: list[dict[str, Any]],
    expected: list[dict[str, str]],
    allowed: list[Path],
) -> dict[str, list]:
    by_package: dict[str, dict[str, str]] = {
        e["package"].lower(): e for e in expected
    }
    by_name: dict[str, dict[str, str]] = {
        e["name"].lower(): e for e in expected
    }

    kept: list[dict[str, Any]] = []
    to_rename: list[dict[str, Any]] = []
    extra_in_allowed: list[dict[str, Any]] = []
    skipped_outside: list[dict[str, Any]] = []
    matched_packages: set[str] = set()

    for app in scanned_apps:
        pkg = (app.get("package_name") or "").lower()
        name = (app.get("name") or "").lower()
        abs_path = app.get("absolute_path", "")
        in_allowed = _is_in_allowed(abs_path, allowed)

        entry: dict[str, str] | None = None
        if pkg and pkg != "unknown" and pkg in by_package:
            entry = by_package[pkg]
        elif name and name in by_name:
            entry = by_name[name]

        if entry is not None:
            pkg_key = entry["package"].lower()
            if pkg_key not in matched_packages:
                matched_packages.add(pkg_key)
                expected_name = entry["name"]
                actual_name = app.get("name", "")
                if actual_name == expected_name:
                    kept.append({
                        "status": "FOUND",
                        "action": "KEEP",
                        "name": expected_name,
                        "package": entry["package"],
                        "partition": app.get("partition", ""),
                        "app_type": app.get("type", ""),
                        "found_at": abs_path,
                    })
                else:
                    to_rename.append({
                        "status": "FOUND_RENAMED",
                        "action": "RENAME_TO_EXPECTED",
                        "expected_name": expected_name,
                        "actual_name": actual_name,
                        "package": entry["package"],
                        "partition": app.get("partition", ""),
                        "app_type": app.get("type", ""),
                        "found_at": abs_path,
                        "in_allowed": in_allowed,
                    })
        else:
            if in_allowed:
                extra_in_allowed.append({
                    "status": "EXTRA",
                    "action": "DELETE",
                    "name": app.get("name", ""),
                    "package": app.get("package_name", "unknown"),
                    "partition": app.get("partition", ""),
                    "app_type": app.get("type", ""),
                    "found_at": abs_path,
                    "size": app.get("size", 0),
                })
            else:
                skipped_outside.append({
                    "status": "OUTSIDE_ALLOWED",
                    "action": "SKIP",
                    "name": app.get("name", ""),
                    "package": app.get("package_name", "unknown"),
                    "partition": app.get("partition", ""),
                    "found_at": abs_path,
                })

    missing: list[dict[str, Any]] = [
        {
            "status": "MISSING",
            "action": "REPORT_ONLY",
            "name": e["name"],
            "package": e["package"],
            "expected_section": e.get("section", ""),
        }
        for e in expected
        if e["package"].lower() not in matched_packages
    ]

    return {
        "kept": kept,
        "to_rename": to_rename,
        "extra_in_allowed": extra_in_allowed,
        "skipped_outside": skipped_outside,
        "missing": missing,
    }


def _apply_renames(
    to_rename: list[dict[str, Any]],
    enforce: bool,
) -> tuple[list[dict[str, Any]], list[str]]:
    done: list[dict[str, Any]] = []
    errors: list[str] = []
    for item in to_rename:
        if not enforce:
            done.append({**item, "enacted": False, "reason": "report-only mode"})
            continue
        if not item.get("in_allowed"):
            done.append({**item, "enacted": False, "reason": "outside allowed location"})
            continue
        src = Path(item["found_at"])
        target = src.parent / item["expected_name"]
        if target.exists():
            errors.append(
                f"CONFLICT: rename target already exists: {target} "
                f"(wanted to rename '{item['actual_name']}' -> '{item['expected_name']}')"
            )
            continue
        try:
            src.rename(target)
            done.append({**item, "enacted": True, "new_path": str(target)})
            print(
                f"[STABLE APP POLICY] RENAMED: '{item['actual_name']}' -> "
                f"'{item['expected_name']}' ({item['package']})"
            )
        except Exception as exc:
            errors.append(f"RENAME FAILED: {src} -> {target}: {exc}")
    return done, errors


def _apply_deletes(
    extras: list[dict[str, Any]],
    enforce: bool,
) -> tuple[list[dict[str, Any]], list[str]]:
    done: list[dict[str, Any]] = []
    errors: list[str] = []
    for item in extras:
        if not enforce:
            done.append({**item, "enacted": False, "reason": "report-only mode"})
            continue
        path = Path(item["found_at"])
        if not path.exists():
            done.append({**item, "enacted": False, "reason": "path not found"})
            continue
        try:
            if path.is_dir():
                shutil.rmtree(path)
            else:
                path.unlink()
            done.append({**item, "enacted": True})
            print(f"[STABLE APP POLICY] DELETED EXTRA: {item['name']} ({item['package']})")
        except Exception as exc:
            errors.append(f"DELETE FAILED: {path}: {exc}")
    return done, errors


def _write_txt_report(path: Path, data: dict[str, Any]) -> None:
    kept = data.get("kept_apps", [])
    renamed = data.get("renamed_apps", [])
    missing = data.get("missing_apps", [])
    deleted = data.get("deleted_extra_apps", [])
    skipped = data.get("skipped_outside_allowed_locations", [])
    errors = data.get("errors", [])
    summary = data.get("summary", {})

    lines = [
        "DeadZone Stable App Policy Report",
        "==================================",
        f"style              : {data.get('style', 'unknown')}",
        f"enforce_mode       : {data.get('enforce_mode', False)}",
        f"apps_list_path     : {data.get('apps_list_path', '(not found)')}",
        f"total_expected     : {data.get('total_expected', 0)}",
        "",
        "SUMMARY:",
        f"  kept             : {summary.get('kept', 0)}",
        f"  renamed          : {summary.get('renamed', 0)}",
        f"  missing          : {summary.get('missing', 0)}",
        f"  deleted_extra    : {summary.get('deleted_extra', 0)}",
        f"  skipped_outside  : {summary.get('skipped_outside', 0)}",
        f"  errors           : {summary.get('errors', 0)}",
        "",
        "KEPT APPS (FOUND — exact match):",
    ]
    for app in kept:
        lines.append(
            f"  [KEEP] {app['name']} ({app['package']}) @ {app['found_at']}"
        )
    if not kept:
        lines.append("  (none)")

    lines += ["", "RENAMED APPS (FOUND_RENAMED):"]
    for app in renamed:
        enacted = app.get("enacted", False)
        tag = "RENAMED" if enacted else "WOULD_RENAME"
        lines.append(
            f"  [{tag}] '{app.get('actual_name')}' -> '{app.get('expected_name')}' "
            f"({app['package']}) @ {app['found_at']}"
        )
    if not renamed:
        lines.append("  (none)")

    lines += ["", "MISSING APPS (not found — report only):"]
    for app in missing:
        lines.append(
            f"  [MISS] {app['name']} ({app['package']}) "
            f"expected_section={app.get('expected_section', '')}"
        )
    if not missing:
        lines.append("  (none)")

    lines += ["", "DELETED EXTRA APPS (in allowed locations, not in apps.list):"]
    for app in deleted:
        enacted = app.get("enacted", False)
        tag = "DELETED" if enacted else "WOULD_DELETE"
        lines.append(
            f"  [{tag}] {app['name']} ({app['package']}) @ {app['found_at']} "
            f"size={app.get('size', 0)}"
        )
    if not deleted:
        lines.append("  (none)")

    lines += ["", "SKIPPED (outside allowed locations — never deleted):"]
    for app in skipped:
        lines.append(
            f"  [SKIP] {app['name']} ({app['package']}) @ {app['found_at']}"
        )
    if not skipped:
        lines.append("  (none)")

    if errors:
        lines += ["", "ERRORS:"]
        for err in errors:
            lines.append(f"  [ERR] {err}")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def enforce_stable_app_policy(
    reports_dir: Path,
    partitions_root: Path,
    scanned_apps: list[dict[str, Any]],
    style: str,
    build_state: "BuildState | None" = None,
) -> dict[str, Any]:
    """Enforce Stable App Policy against apps.list.

    stable style   — renames misnamed folders and deletes extra apps.
    non-stable     — report-only, no filesystem modifications.

    Raises RuntimeError when:
      - style is stable and apps.list is missing
      - a rename target already exists (CONFLICT)
      - a delete operation fails
    """
    style_key = style.strip().lower()
    enforce = style_key == "stable"

    apps_list_path = _find_apps_list()
    if apps_list_path is None:
        if enforce:
            raise RuntimeError(
                "Stable App Policy requires ListMezo/free/apps.list "
                "but the file was not found"
            )
        print("[STABLE APP POLICY] apps.list not found; skipping (non-stable style)")
        return {
            "status": "skipped",
            "reason": "apps.list not found",
            "style": style,
            "enforce_mode": enforce,
        }

    print(f"[STABLE APP POLICY] apps.list: {apps_list_path}")
    try:
        expected = _parse_apps_list(apps_list_path)
    except Exception as exc:
        raise RuntimeError(
            f"Stable App Policy failed to parse apps.list: {exc}"
        ) from exc

    print(
        f"[STABLE APP POLICY] Expected={len(expected)} "
        f"Scanned={len(scanned_apps)} "
        f"enforce={enforce}"
    )

    allowed = _build_allowed_dirs(partitions_root)
    classification = _classify(scanned_apps, expected, allowed)

    renamed_done, rename_errors = _apply_renames(classification["to_rename"], enforce)
    deleted_done, delete_errors = _apply_deletes(classification["extra_in_allowed"], enforce)

    all_errors = rename_errors + delete_errors
    if enforce and all_errors:
        raise RuntimeError(
            f"Stable App Policy failed with {len(all_errors)} error(s):\n"
            + "\n".join(all_errors)
        )

    kept_count = len(classification["kept"])
    renamed_count = sum(1 for r in renamed_done if r.get("enacted"))
    missing_count = len(classification["missing"])
    deleted_count = sum(1 for d in deleted_done if d.get("enacted"))
    skipped_count = len(classification["skipped_outside"])

    summary = {
        "kept": kept_count,
        "renamed": renamed_count,
        "missing": missing_count,
        "deleted_extra": deleted_count,
        "skipped_outside": skipped_count,
        "errors": len(all_errors),
    }

    data: dict[str, Any] = {
        "status": "ok",
        "style": style,
        "enforce_mode": enforce,
        "apps_list_path": str(apps_list_path),
        "total_expected": len(expected),
        "summary": summary,
        "kept_apps": classification["kept"],
        "renamed_apps": renamed_done,
        "missing_apps": classification["missing"],
        "deleted_extra_apps": deleted_done,
        "skipped_outside_allowed_locations": classification["skipped_outside"],
        "errors": all_errors,
    }

    if build_state is not None:
        try:
            build_state.counters.update(
                stable_kept_apps=kept_count,
                stable_renamed_apps=renamed_count,
                stable_missing_apps=missing_count,
                stable_deleted_extra_apps=deleted_count,
            )
            build_state.save()
        except Exception as exc:
            print(f"[STABLE APP POLICY] Warning: counters update failed: {exc}")

    reports_dir.mkdir(parents=True, exist_ok=True)

    txt_path = reports_dir / "stable_app_policy_report.txt"
    try:
        _write_txt_report(txt_path, data)
        print(f"[STABLE APP POLICY] Written: {txt_path}")
    except Exception as exc:
        print(f"[STABLE APP POLICY] Warning: txt report write failed: {exc}")

    json_path = reports_dir / "stable_app_policy_report.json"
    try:
        json_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        print(f"[STABLE APP POLICY] Written: {json_path}")
    except Exception as exc:
        print(f"[STABLE APP POLICY] Warning: json report write failed: {exc}")

    print(
        f"[STABLE APP POLICY] kept={kept_count} "
        f"renamed={renamed_count} "
        f"missing={missing_count} "
        f"deleted_extra={deleted_count} "
        f"skipped_outside={skipped_count}"
    )
    return data
