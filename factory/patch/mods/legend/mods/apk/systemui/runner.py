"""
Legend MiuiSystemUI APK patch runner - clean Python rules edition.

Architecture
============
All patch logic lives in generated rule modules; no reference-pack directories
or patch comparison files are read at runtime.

  factory/patch/legend/systemui/smali/          -> 114 modified class patches
  factory/patch/legend/systemui/smali_added/    -> 313 added class patches
  factory/patch/legend/systemui/resources/      -> layout + arsc + values rules
  factory/patch/legend/assets/systemui/         -> managed XML assets

Pipeline (execute mode):
  1. Find MiuiSystemUI.apk in the ROM project tree.
  2. Copy to timestamped work directory.
  3. Decompile with APKEditor.
  4. Copy managed drawable/layout resource assets.
  5. Apply add-resource XMLs from managed assets.
  6. Apply layout XML changes from generated rules.
  7. Apply arsc resource changes from generated rules.
  8. Apply smali method patches with smart class/method matching.
  9. Place added smali classes into a valid smali_classesN root.
  10. Rebuild APK with APKEditor.
  11. Verify rebuilt APK (size > 0).
  12. Restore to exact original path as MiuiSystemUI.apk (no backup, no renamed copies).

Flavor guard:
  Only runs for: legend, deadzone_legend (case-insensitive).

Reports:
  output/reports/legend_systemui_report.json
  output/reports/legend_systemui_report.txt

Public API:
  apply_systemui_patch(project_dir, flavor, execute=False,
                       work_dir=None) -> dict
"""
from __future__ import annotations

import difflib
import importlib
import json
import pkgutil
import re
import shutil
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any, Optional

from factory.patch.apk.apkeditor_tools import resolve_apkeditor_jar
from factory.patch.apk.apk_workspace import (
    copy_apk_to_work,
    decompile_apk,
    find_apk,
    prepare_apk_work_dir,
    rebuild_apk,
    restore_rebuilt_apk_no_backup,
)
from factory.patch.mods.legend.smart_smali_patcher import (
    ClassMatchStatus,
    MethodMatchStatus,
    PatchApplyStatus,
    apply_smart_patch,
    find_class,
    insert_method_if_missing,
    add_class_if_missing,
)
from factory.patch.mods.legend.mods.apk.systemui.model import (
    ClassPatch,
    ClassResult,
    PatchResult,
    PatchStatus,
    load_class_patch,
)

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

def _find_repo_root(start: Path) -> Path:
    """Walk upward until a directory with factory/ and (.git or third_party/) is found."""
    p = start.resolve()
    while p != p.parent:
        if (p / 'factory').is_dir() and ((p / '.git').exists() or (p / 'third_party').is_dir()):
            return p
        p = p.parent
    raise RuntimeError(
        f"Cannot locate repo root from {start!r}: "
        "no directory with factory/ + (.git or third_party/) found"
    )

_REPO_ROOT   = _find_repo_root(Path(__file__).resolve().parent)
_PKG_ROOT    = Path(__file__).resolve().parent
_OUTPUT_ROOT = _REPO_ROOT / "output"
_REPORTS_DIR = _OUTPUT_ROOT / "reports"

SYSTEMUI_APK_NAME  = "MiuiSystemUI.apk"
_WORK_DIR_DEFAULT  = _OUTPUT_ROOT / "work" / "systemui_legend_apk_work"
_LEGEND_FLAVORS    = frozenset({"legend", "deadzone_legend"})

# ---------------------------------------------------------------------------
# Flavor guard
# ---------------------------------------------------------------------------

def _is_legend(flavor: str) -> bool:
    return flavor.strip().lower() in _LEGEND_FLAVORS


# ---------------------------------------------------------------------------
# Smali root helpers
# ---------------------------------------------------------------------------

def _find_smali_roots(decompiled_dir: Path) -> list[Path]:
    """Return all smali* subdirectories, sorted."""
    roots: list[Path] = []
    for child in sorted(decompiled_dir.iterdir()):
        if child.is_dir() and child.name.startswith("smali"):
            roots.append(child)
    return roots


def _next_smali_root(decompiled_dir: Path) -> Path:
    """Return the next available smali_classesN path (creates no directory)."""
    existing = {r.name for r in _find_smali_roots(decompiled_dir)}
    # APKEditor uses: smali/, smali_classes2/, smali_classes3/, ...
    if "smali" not in existing:
        return decompiled_dir / "smali"
    n = 2
    while f"smali_classes{n}" in existing:
        n += 1
    return decompiled_dir / f"smali_classes{n}"


# ---------------------------------------------------------------------------
# Class rule module discovery
# ---------------------------------------------------------------------------

def _load_modified_class_patches() -> list[ClassPatch]:
    """Import every module in smali/ (modified classes)."""
    result: list[ClassPatch] = []
    smali_pkg = "factory.patch.mods.legend.mods.apk.systemui.smali"
    smali_path = _PKG_ROOT / "smali"
    if not smali_path.is_dir():
        return result
    for finder, name, ispkg in pkgutil.iter_modules([str(smali_path)]):
        if name == "__init__":
            continue
        try:
            mod = importlib.import_module(f"{smali_pkg}.{name}")
            cp = load_class_patch(mod)
            if cp.target_class:
                result.append(cp)
        except Exception as exc:
            print(f"[systemui_runner] WARNING: could not load smali/{name}: {exc}")
    return result


def _load_added_class_patches() -> list[ClassPatch]:
    """Import every module in smali_added/classes_auto/ (added classes)."""
    result: list[ClassPatch] = []
    pkg = "factory.patch.mods.legend.mods.apk.systemui.smali_added.classes_auto"
    added_path = _PKG_ROOT / "smali_added"
    if not added_path.is_dir():
        return result
    group_path = added_path / "classes_auto"
    if not group_path.is_dir():
        return result
    for finder, name, ispkg in pkgutil.iter_modules([str(group_path)]):
        if name == "__init__":
            continue
        try:
            mod = importlib.import_module(f"{pkg}.{name}")
            cp = load_class_patch(mod)
            if cp.target_class:
                result.append(cp)
        except Exception as exc:
            print(f"[systemui_runner] WARNING: could not load smali_added/classes_auto/{name}: {exc}")
    return result


# ---------------------------------------------------------------------------
# Stage: apply add/ resource XMLs from managed assets
# ---------------------------------------------------------------------------

def _apply_add_resources(decompiled_dir: Path, dry_run: bool) -> dict:
    """Merge managed add/ resource XMLs into the decompiled APK res/values*/ dirs."""
    from factory.patch.apk.resource_merge import (
        apply_add_resources as _orig_apply,
    )
    # Point to managed factory assets.
    from factory.patch.mods.legend.mods.apk.systemui.resources.values_rules import ADD_RESOURCES_SRC

    result: dict = {
        "assets_root": str(ADD_RESOURCES_SRC),
        "dry_run": dry_run,
        "status": "NOT_RUN",
    }

    if not ADD_RESOURCES_SRC.is_dir():
        result["status"] = "SKIPPED_MISSING_ASSETS"
        result["error"] = f"Managed assets not found: {ADD_RESOURCES_SRC}"
        return result

    if dry_run:
        # Count without applying
        total = sum(1 for _ in ADD_RESOURCES_SRC.rglob("*.xml"))
        result["status"] = "WOULD_APPLY"
        result["xml_files_found"] = total
        return result

    # Re-use the existing XML merger, redirected to managed assets
    class _FakeRefDir:
        """Adapter: gives resource_merge.apply_add_resources a fake ref_dir."""
        def __init__(self, assets_src: Path):
            self._src = assets_src
        def __truediv__(self, other: str):
            if other == "add":
                return _FakeAddDir(self._src)
            return Path(str(self)) / other
        def __str__(self):
            return str(self._src.parent)

    class _FakeAddDir:
        def __init__(self, assets_src: Path):
            self._src = assets_src
        def __truediv__(self, other: str):
            if other == "com.android.systemui":
                return self._src
            return Path(str(self._src)) / other

    try:
        sub = _orig_apply(
            ref_dir=_FakeRefDir(ADD_RESOURCES_SRC),  # type: ignore[arg-type]
            decompiled_dir=decompiled_dir,
        )
        result.update(sub)
        result["status"] = sub.get("status", "OK")
    except Exception as exc:
        result["status"] = "FAILED"
        result["error"] = str(exc)

    return result


def _apply_resource_copy_rules(decompiled_dir: Path, dry_run: bool) -> dict:
    """Copy managed drawable/layout assets into decompiled APK res/ folders."""
    from factory.patch.mods.legend.mods.apk.systemui.resources.add_resource_rules import (
        ADDED_LAYOUTS,
        ASSETS_ROOT,
        RESOURCE_RULES,
    )

    result: dict = {
        "asset_root": str(ASSETS_ROOT),
        "rules_total": len(RESOURCE_RULES),
        "copied": 0,
        "would_copy": 0,
        "missing_assets": [],
        "by_folder": {},
        "added_layouts": list(ADDED_LAYOUTS),
        "statuses": [],
        "dry_run": dry_run,
        "status": "NOT_RUN",
    }

    res_dir = decompiled_dir / "res"
    for rule in RESOURCE_RULES:
        rel_source = Path(rule["source"])
        source = ASSETS_ROOT / rel_source
        target = decompiled_dir / rule["target"]
        folder = rule["resource_type"]
        status = ""

        if not source.is_file():
            status = "FAILED_MISSING_ASSET"
            entry = {
                "id": rule["id"],
                "source": str(source),
                "target": str(target),
                "status": status,
                "required": rule.get("required", True),
            }
            result["missing_assets"].append(entry)
            result["statuses"].append(entry)
            if rule.get("required", True):
                result["status"] = "FAILED_MISSING_ASSET"
            continue

        if dry_run:
            status = "WOULD_COPY"
            result["would_copy"] += 1
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
            status = "COPIED"
            result["copied"] += 1

        by_folder = result["by_folder"]
        by_folder[folder] = by_folder.get(folder, 0) + 1
        result["statuses"].append({
            "id": rule["id"],
            "source": str(source),
            "target": str(target.relative_to(res_dir.parent)),
            "status": status,
            "required": rule.get("required", True),
        })

    if result["status"] != "FAILED_MISSING_ASSET":
        result["status"] = "WOULD_COPY" if dry_run else "COPIED"
    return result


# ---------------------------------------------------------------------------
# Stage: apply layout XML patches
# ---------------------------------------------------------------------------

def _apply_diff_hunks(a_text: str, b_text: str, target_text: str) -> tuple[str, int, list[str]]:
    """Compute unified diff a→b and apply each hunk to target_text."""
    a_lines = a_text.splitlines(keepends=True)
    b_lines = b_text.splitlines(keepends=True)
    diff_lines = list(difflib.unified_diff(a_lines, b_lines, n=2))
    if not diff_lines:
        return target_text, 0, []

    hunks: list[tuple[list[str], list[str]]] = []
    old_buf: list[str] = []
    new_buf: list[str] = []

    for line in diff_lines:
        if line.startswith("--- ") or line.startswith("+++ "):
            continue
        if line.startswith("@@"):
            if old_buf or new_buf:
                hunks.append((old_buf, new_buf))
            old_buf, new_buf = [], []
        elif line.startswith("-"):
            old_buf.append(line[1:])
        elif line.startswith("+"):
            new_buf.append(line[1:])

    if old_buf or new_buf:
        hunks.append((old_buf, new_buf))

    result_text = target_text
    applied = 0
    skipped: list[str] = []

    for old_lines, new_lines in hunks:
        if not old_lines:
            skipped.append(
                f"pure-addition hunk skipped: "
                f"{new_lines[0].strip()[:60]!r}" if new_lines else "empty hunk"
            )
            continue
        old_block = "".join(old_lines)
        new_block = "".join(new_lines)
        if old_block in result_text:
            result_text = result_text.replace(old_block, new_block, 1)
            applied += 1
        else:
            old_stripped = "\n".join(l.rstrip() for l in old_lines)
            tgt_stripped = "\n".join(l.rstrip() for l in result_text.splitlines())
            if old_stripped in tgt_stripped:
                result_text = result_text.replace(old_block, new_block, 1)
                applied += 1
            else:
                skipped.append(f"old block not found: {old_block.strip()[:60]!r}")

    return result_text, applied, skipped


def _find_layout_file(decompiled_dir: Path, layout_name: str) -> Optional[Path]:
    res_dir = decompiled_dir / "res"
    if res_dir.is_dir():
        for layout_dir in sorted(res_dir.iterdir()):
            if layout_dir.is_dir() and layout_dir.name.startswith("layout"):
                c = layout_dir / layout_name
                if c.is_file():
                    return c
        for found in res_dir.rglob(layout_name):
            if "layout" in found.parent.name and found.is_file():
                return found
    return None


def _apply_layout_patches(decompiled_dir: Path, dry_run: bool) -> dict:
    """Apply layout XML changes from layout_rules.py."""
    from factory.patch.mods.legend.mods.apk.systemui.resources.layout_rules import (
        MODIFIED_LAYOUTS, ADDED_LAYOUTS,
    )
    result: dict = {
        "modified_layouts": len(MODIFIED_LAYOUTS),
        "added_layouts": len(ADDED_LAYOUTS),
        "applied": 0,
        "skipped": [],
        "errors": [],
        "status": "NOT_RUN",
        "dry_run": dry_run,
    }

    if dry_run:
        result["status"] = "WOULD_APPLY"
        return result

    for layout_name, rule in MODIFIED_LAYOUTS.items():
        target = _find_layout_file(decompiled_dir, layout_name)
        if target is None:
            status_str = "FAILED_NOT_FOUND" if rule.get("required") else "SKIPPED_OPTIONAL"
            result["skipped"].append(f"{layout_name}: not found in decompiled APK [{status_str}]")
            continue
        try:
            target_text = target.read_text(encoding="utf-8", errors="replace")
        except Exception as exc:
            result["errors"].append(f"{layout_name}: read error: {exc}")
            continue

        new_text, applied, skipped = _apply_diff_hunks(
            rule["a_text"], rule["b_text"], target_text
        )
        result["applied"] += applied
        result["skipped"].extend(f"{layout_name}: {s}" for s in skipped)

        if applied > 0 and new_text != target_text:
            try:
                target.write_text(new_text, encoding="utf-8")
            except Exception as exc:
                result["errors"].append(f"{layout_name}: write error: {exc}")

    # Added layouts (b/ only entries)
    layout_dir = decompiled_dir / "res" / "layout"
    for layout_name, rule in ADDED_LAYOUTS.items():
        if _find_layout_file(decompiled_dir, layout_name) is not None:
            continue
        if layout_dir.is_dir():
            try:
                (layout_dir / layout_name).write_text(
                    rule["content"], encoding="utf-8"
                )
                result["applied"] += 1
            except Exception as exc:
                result["errors"].append(f"{layout_name}: add error: {exc}")

    result["status"] = "OK" if not result["errors"] else "PARTIAL"
    return result


# ---------------------------------------------------------------------------
# Stage: apply arsc resource patches
# ---------------------------------------------------------------------------

_VALUE_TYPES = frozenset({"string", "array", "bool", "dimen", "integer", "plurals"})
_TYPE_DEFAULT_FILENAME: dict[str, str] = {
    "string":  "strings.xml",
    "array":   "arrays.xml",
    "bool":    "booleans.xml",
    "dimen":   "dimens.xml",
    "integer": "integers.xml",
    "plurals": "plurals.xml",
}
_TYPE_FILE_CANDIDATES: dict[str, list[str]] = {
    "string":  ["strings.xml",   "string.xml"],
    "array":   ["arrays.xml",    "array.xml"],
    "bool":    ["booleans.xml",  "bool.xml"],
    "dimen":   ["dimens.xml",    "dimen.xml"],
    "integer": ["integers.xml",  "integer.xml"],
    "plurals": ["plurals.xml"],
}
_TYPE_TO_TAGS: dict[str, tuple[str, ...]] = {
    "string":  ("string",),
    "array":   ("string-array", "integer-array", "array"),
    "bool":    ("bool",),
    "dimen":   ("dimen",),
    "integer": ("integer",),
    "plurals": ("plurals",),
}


def _find_res_file(values_dir: Path, res_type: str) -> Optional[Path]:
    if not values_dir.is_dir():
        return None
    for name in _TYPE_FILE_CANDIDATES.get(res_type, [f"{res_type}s.xml", f"{res_type}.xml"]):
        f = values_dir / name
        if f.is_file():
            return f
    tags = _TYPE_TO_TAGS.get(res_type, (res_type,))
    for xml_file in sorted(values_dir.glob("*.xml")):
        try:
            text = xml_file.read_text(encoding="utf-8", errors="replace")
            if any(f"<{tag}" in text for tag in tags):
                return xml_file
        except Exception:
            continue
    return None


def _arsc_entry_to_type_qualifier(entry_path: str) -> tuple[str, str]:
    parts = entry_path.split("/")
    if len(parts) < 3:
        return "", ""
    res_type = parts[1]
    leaf = parts[2]
    leaf_parts = leaf.split("-", 1)
    qualifier = leaf_parts[1] if len(leaf_parts) == 2 else ""
    return res_type, qualifier


def _xml_safe_write(tree_root: ET.Element, dest: Path) -> None:
    ET.indent(tree_root, space="    ")
    text = '<?xml version="1.0" encoding="utf-8"?>\n' + ET.tostring(
        tree_root, encoding="unicode"
    )
    dest.write_text(text, encoding="utf-8")


def _apply_arsc_patches(decompiled_dir: Path, dry_run: bool) -> dict:
    """Apply arsc resource changes from arsc_rules.py."""
    from factory.patch.mods.legend.mods.apk.systemui.resources.arsc_rules import (
        MODIFIED_GROUPS, ADDED_GROUPS,
    )
    result: dict = {
        "modified_groups": len(MODIFIED_GROUPS),
        "added_groups": len(ADDED_GROUPS),
        "applied": 0,
        "skipped": [],
        "errors": [],
        "status": "NOT_RUN",
        "dry_run": dry_run,
    }

    if dry_run:
        result["status"] = "WOULD_APPLY"
        return result

    def _values_dir(qualifier: str) -> Path:
        name = f"values-{qualifier}" if qualifier else "values"
        return decompiled_dir / "res" / name

    def _merge_entries(b_text: str, a_text: Optional[str], entry_path: str,
                       required: bool) -> int:
        res_type, qualifier = _arsc_entry_to_type_qualifier(entry_path)
        if not res_type or res_type not in _VALUE_TYPES:
            result["skipped"].append(f"{entry_path}: type '{res_type}' skipped")
            return 0

        values_dir = _values_dir(qualifier)
        target_file = _find_res_file(values_dir, res_type)

        try:
            b_root = ET.fromstring(b_text)
            b_entries: dict[str, ET.Element] = {
                el.get("name", ""): el for el in b_root if el.get("name")
            }
        except Exception as exc:
            result["errors"].append(f"{entry_path}: parse b/ XML error: {exc}")
            return 0

        a_entries: dict[str, ET.Element] = {}
        if a_text:
            try:
                a_root = ET.fromstring(a_text)
                a_entries = {el.get("name", ""): el for el in a_root if el.get("name")}
            except Exception:
                pass

        if target_file is None:
            if a_text is None:
                # Pure addition: create the file
                fname = _TYPE_DEFAULT_FILENAME.get(res_type, f"{res_type}s.xml")
                target_file = values_dir / fname
                values_dir.mkdir(parents=True, exist_ok=True)
                try:
                    _xml_safe_write(b_root, target_file)
                    return len(b_entries)
                except Exception as exc:
                    result["errors"].append(f"{entry_path}: create error: {exc}")
                    return 0
            result["skipped"].append(f"{entry_path}: target file not found")
            return 0

        try:
            target_root = ET.fromstring(
                target_file.read_text(encoding="utf-8", errors="replace")
            )
            target_entries: dict[str, ET.Element] = {
                el.get("name", ""): el for el in target_root if el.get("name")
            }
        except Exception as exc:
            result["errors"].append(f"{entry_path}: parse target error: {exc}")
            return 0

        changed = 0
        group_changed = False

        for name, b_el in b_entries.items():
            if name in a_entries:
                a_val = ET.tostring(a_entries[name], encoding="unicode").strip()
                b_val = ET.tostring(b_el, encoding="unicode").strip()
                if a_val == b_val:
                    continue
                if name not in target_entries:
                    result["skipped"].append(f"{entry_path}/{name}: not in target")
                    continue
                t_val = ET.tostring(target_entries[name], encoding="unicode").strip()
                if t_val != a_val:
                    result["skipped"].append(
                        f"{entry_path}/{name}: target differs from a/ — cannot apply safely"
                    )
                    continue
                t_el = target_entries[name]
                t_el.text = b_el.text
                t_el.tail = b_el.tail
                for k, v in b_el.attrib.items():
                    t_el.set(k, v)
                for k in [k for k in list(t_el.attrib) if k not in b_el.attrib and k != "name"]:
                    del t_el.attrib[k]
                for child in list(t_el):
                    t_el.remove(child)
                for child in b_el:
                    t_el.append(child)
                changed += 1
                group_changed = True
            else:
                if name not in target_entries:
                    target_root.append(b_el)
                    changed += 1
                    group_changed = True

        if group_changed:
            try:
                _xml_safe_write(target_root, target_file)
            except Exception as exc:
                result["errors"].append(f"{entry_path}: write error: {exc}")

        return changed

    # Modified groups
    for entry_path, rule in MODIFIED_GROUPS.items():
        n = _merge_entries(rule["b_text"], rule["a_text"], entry_path, rule.get("required", True))
        result["applied"] += n

    # Added groups
    for entry_path, rule in ADDED_GROUPS.items():
        n = _merge_entries(rule["b_text"], None, entry_path, rule.get("required", False))
        result["applied"] += n

    result["status"] = "OK" if not result["errors"] else "PARTIAL"
    return result


# ---------------------------------------------------------------------------
# Stage: apply modified smali class patches
# ---------------------------------------------------------------------------

def _apply_smali_patches(
    smali_roots: list[Path],
    class_patches: list[ClassPatch],
    dry_run: bool,
) -> tuple[list[ClassResult], dict]:
    """Apply method-level patches to modified classes."""
    class_results: list[ClassResult] = []
    summary = {
        "classes_found": 0,
        "classes_not_found": 0,
        "patches_applied": 0,
        "patches_skipped_optional": 0,
        "patches_failed": 0,
        "status": "OK",
    }

    for cp in class_patches:
        cr = ClassResult(target_class=cp.target_class, dex_group=cp.dex_group)
        patch_results: list[PatchResult] = []

        for patch in cp.patches:
            rule_dict = {
                "id": patch.id,
                "type": patch.type,
                "method": patch.method,
                "method_name": patch.method_name,
                "method_anchors": patch.method_anchors,
                "class_fallback_names": cp.class_fallback_names,
                "class_anchors": cp.class_anchors,
                "search": patch.search,
                "replacement": patch.replacement,
                "required": patch.required,
                "reason": patch.reason,
                "target_jar": SYSTEMUI_APK_NAME,
                "target_class": cp.target_class,
            }

            try:
                result = apply_smart_patch(smali_roots, rule_dict, dry_run)
                status_str = result.status.value
                pr = PatchResult(
                    patch_id=patch.id,
                    patch_type=patch.type,
                    target_class=cp.target_class,
                    status=PatchStatus[status_str] if status_str in PatchStatus.__members__ else PatchStatus.PATCHED,
                    class_match_strategy=str(result.class_match),
                    method_match_strategy=str(result.method_match),
                )
            except Exception as exc:
                pr = PatchResult(
                    patch_id=patch.id,
                    patch_type=patch.type,
                    target_class=cp.target_class,
                    status=PatchStatus.FAILED_NOT_FOUND if patch.required else PatchStatus.SKIPPED_OPTIONAL,
                    error=str(exc),
                )

            patch_results.append(pr)

            s = pr.status
            if s in (PatchStatus.PATCHED, PatchStatus.WOULD_PATCH, PatchStatus.EXISTS):
                summary["patches_applied"] += 1
                if cr.class_match_strategy == "":
                    cr.class_match_strategy = pr.class_match_strategy
            elif s == PatchStatus.SKIPPED_OPTIONAL:
                summary["patches_skipped_optional"] += 1
            elif s in (PatchStatus.FAILED_NOT_FOUND, PatchStatus.FAILED_AMBIGUOUS):
                if patch.required:
                    summary["patches_failed"] += 1
                else:
                    summary["patches_skipped_optional"] += 1

        cr.patch_results = patch_results
        class_results.append(cr)

    if summary["patches_failed"] > 0:
        summary["status"] = "PARTIAL"

    return class_results, summary


# ---------------------------------------------------------------------------
# Stage: place added smali classes into smali_classesN root
# ---------------------------------------------------------------------------

def _apply_added_classes(
    decompiled_dir: Path,
    added_patches: list[ClassPatch],
    dry_run: bool,
) -> dict:
    """Write added class smali files into one valid smali_classesN root."""
    existing_roots = _find_smali_roots(decompiled_dir)

    result: dict = {
        "existing_smali_roots": [r.name for r in existing_roots],
        "new_roots_created": [],
        "smali_root_chosen": "",
        "classes_added": 0,
        "classes_would_add": 0,
        "classes_skipped_already_exists": 0,
        "duplicate_class_count": 0,
        "duplicate_conflict_count": 0,
        "errors": [],
        "class_results": [],
        "dry_run": dry_run,
        "status": "NOT_RUN",
    }

    if dry_run:
        chosen = _next_smali_root(decompiled_dir)
        result["smali_root_chosen"] = chosen.name

    write_root: Optional[Path] = None

    for cp in added_patches:
        patch = next((p for p in cp.patches if p.type == "class_add"), None)
        if patch is None:
            continue

        existing_matches = [root / cp.target_class for root in existing_roots if (root / cp.target_class).is_file()]
        class_result = {
            "target_class": cp.target_class,
            "status": "",
            "smali_root": "",
            "existing_paths": [str(p) for p in existing_matches],
            "required": patch.required,
        }

        if existing_matches:
            result["duplicate_class_count"] += 1
            identical = False
            for existing in existing_matches:
                try:
                    if existing.read_text(encoding="utf-8", errors="replace") == patch.replacement:
                        identical = True
                        break
                except Exception as exc:
                    result["errors"].append(f"{cp.target_class}: duplicate read error: {exc}")
            if identical:
                class_result["status"] = "SKIPPED_ALREADY_EXISTS"
                result["classes_skipped_already_exists"] += 1
            else:
                class_result["status"] = "FAILED_DUPLICATE_CLASS_CONFLICT"
                result["duplicate_conflict_count"] += 1
                message = f"{cp.target_class}: duplicate class differs from add rule"
                if patch.required:
                    result["errors"].append(message)
                else:
                    result.setdefault("warnings", []).append(message)
            result["class_results"].append(class_result)
            continue

        if dry_run:
            class_result["status"] = "WOULD_ADD_CLASS"
            class_result["smali_root"] = result["smali_root_chosen"]
            result["classes_would_add"] += 1
            result["class_results"].append(class_result)
            continue

        if write_root is None:
            write_root = _next_smali_root(decompiled_dir)
            write_root.mkdir(parents=True, exist_ok=True)
            result["smali_root_chosen"] = write_root.name
            if write_root.name not in result["existing_smali_roots"]:
                result["new_roots_created"].append(write_root.name)
            print(f"[systemui_runner] Created smali root for added classes: {write_root.name}")

        dest = write_root / cp.target_class
        dest.parent.mkdir(parents=True, exist_ok=True)
        try:
            dest.write_text(patch.replacement, encoding="utf-8")
            class_result["status"] = "ADDED_CLASS"
            class_result["smali_root"] = write_root.name
            result["classes_added"] += 1
        except Exception as exc:
            class_result["status"] = "FAILED_NOT_FOUND"
            result["errors"].append(f"{cp.target_class}: write error: {exc}")
            if patch.required:
                result["class_results"].append(class_result)
                result["status"] = "FAILED"
                return result
        result["class_results"].append(class_result)

    if result["duplicate_conflict_count"]:
        result["status"] = "FAILED_DUPLICATE_CLASS_CONFLICT"
    elif dry_run:
        result["status"] = "WOULD_ADD_CLASS"
    elif result["classes_added"] or result["classes_skipped_already_exists"]:
        result["status"] = "ADDED_CLASS"
    else:
        result["status"] = "OK"
    return result


# ---------------------------------------------------------------------------
# Report formatting
# ---------------------------------------------------------------------------

def _format_text_report(report: dict) -> str:
    mode = "DRY RUN" if report.get("dry_run") else "EXECUTE"
    lines: list[str] = [
        f"DeadZone Legend MiuiSystemUI APK Patch Report  [{mode}]",
        "=" * 70,
        f"Final status         : {report.get('final_status', '?')}",
        f"Flavor               : {report.get('flavor', '?')}",
        f"Project dir          : {report.get('project_dir', '?')}",
        f"Work dir             : {report.get('work_dir', '?')}",
        "",
        "APK:",
        f"  Original path      : {report.get('original_apk_path', '?')}",
        f"  Restored path      : {report.get('restored_apk_path', '?')}",
        f"  Original filename  : {report.get('original_apk_name', '?')}",
        f"  APK found          : {report.get('apk_found', '?')}",
        f"  Final filename     : {report.get('final_filename', 'MiuiSystemUI.apk')}",
        "",
        "Tool:",
        f"  APKEditor jar      : {report.get('apkeditor_jar', '?')}",
        f"  APKEditor exists   : {report.get('apkeditor_exists', '?')}",
        "",
        "Smali rule inventory:",
        f"  Modified classes   : {report.get('smali_modified_count', 0)}",
        f"  Added classes      : {report.get('smali_added_count', 0)}",
        "   classes_auto       : {}".format(report.get('smali_added_by_group', {}).get('classes_auto', 0)),
        "",
        "Managed resource inventory:",
        f"  Drawable/layout    : {report.get('managed_resource_count', 0)}",
        f"  Copied resources   : {report.get('copied_resource_count', 0)}",
        f"  Added layouts      : {', '.join(report.get('added_layouts', [])) or '(none)'}",
        f"  Layout rules       : {report.get('layout_rule_count', 0)}",
        f"  Arsc modified      : {report.get('arsc_modified_count', 0)}",
        f"  Arsc added         : {report.get('arsc_added_count', 0)}",
        f"  Add-resource XMLs  : {report.get('add_resource_xml_count', 0)}",
        "",
        "Stage results:",
        f"  Decompile          : {report.get('decompile_status', 'N/A')}",
        f"  Resource copies    : {report.get('resource_copy_status', 'N/A')}  (missing: {report.get('missing_asset_count', 0)})",
        f"  Asset root         : {report.get('systemui_asset_root', 'N/A')}",
        f"  Add resources      : {report.get('add_resource_status', 'N/A')}",
        f"  Layout patches     : {report.get('layout_status', 'N/A')}  ({report.get('layout_applied', 0)} blocks applied)",
        f"  Arsc patches       : {report.get('arsc_status', 'N/A')}  ({report.get('arsc_applied', 0)} entries applied)",
        f"  Smali patches      : {report.get('smali_status', 'N/A')}  ({report.get('smali_patches_applied', 0)} applied)",
        f"  Added classes      : {report.get('added_classes_status', 'N/A')}  ({report.get('added_classes_count', 0)} classes)",
        f"  Duplicate classes  : {report.get('duplicate_class_count', 0)}",
        f"  Rebuild            : {report.get('rebuild_status', 'N/A')}",
        f"  Restore            : {report.get('restore_status', 'N/A')}",
        "",
    ]

    # Smali patch summary
    cr_list = report.get("class_results", [])
    if cr_list:
        lines.append("Smali class/method patch details (first 20):")
        for cr in cr_list[:20]:
            lines.append(f"  {cr['target_class']}")
            lines.append(f"    class match: {cr.get('class_match_strategy', '?')}")
            for pr in cr.get("patch_results", [])[:5]:
                lines.append(
                    f"    [{pr.get('status', '?'):18}] {pr.get('patch_id', '?')}"
                    f"  method_match={pr.get('method_match_strategy', '?')}"
                )
        if len(cr_list) > 20:
            lines.append(f"  ... and {len(cr_list) - 20} more classes")
        lines.append("")

    # Added-class smali roots
    added_info = report.get("added_classes_info", {})
    if added_info:
        lines.append("Added-class smali roots:")
        for rn in added_info.get("existing_roots", []):
            lines.append(f"  existing: {rn}")
        if added_info.get("smali_root_chosen"):
            lines.append(f"  chosen  : {added_info.get('smali_root_chosen')}")
        for rn in added_info.get("new_roots_created", []):
            lines.append(f"  created : {rn}")
        lines.append("")

    warnings = report.get("warnings", [])
    lines.append("Warnings:")
    lines.extend(f"  ! {w}" for w in warnings) if warnings else lines.append("  (none)")

    errors = report.get("errors", [])
    lines.append("")
    lines.append("Errors:")
    lines.extend(f"  X {e}" for e in errors) if errors else lines.append("  (none)")

    lines.append("")
    return "\n".join(lines)


def _write_reports(report: dict) -> None:
    _REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    json_path = _REPORTS_DIR / "legend_systemui_report.json"
    txt_path  = _REPORTS_DIR / "legend_systemui_report.txt"
    json_path.write_text(
        json.dumps(report, indent=2, ensure_ascii=True, default=str),
        encoding="utf-8",
    )
    txt_path.write_text(_format_text_report(report), encoding="utf-8")
    print(f"[systemui_runner] JSON: {json_path}")
    print(f"[systemui_runner] TXT : {txt_path}")


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------

def apply_systemui_patch(
    project_dir: Path,
    flavor: str,
    execute: bool = False,
    work_dir: Optional[Path] = None,
) -> dict:
    """
    Apply (or dry-run) the MiuiSystemUI APK patch for Legend ROM flavor.

    Parameters
    ----------
    project_dir : Path   Root of the unpacked ROM project.
    flavor      : str    ROM flavor ("legend" | "deadzone_legend" | other).
    execute     : bool   True → apply. False (default) → dry-run.
    work_dir    : Path   Optional work directory override.

    Returns
    -------
    dict  Report with final_status and all stage detail keys.
    """
    effective_work = work_dir or _WORK_DIR_DEFAULT
    apkeditor_jar  = resolve_apkeditor_jar()
    systemui_apk   = find_apk(project_dir, SYSTEMUI_APK_NAME)

    apkeditor_str = str(apkeditor_jar) if apkeditor_jar else "(not found)"
    apk_str       = str(systemui_apk)  if systemui_apk  else "(not found)"
    apk_name      = systemui_apk.name  if systemui_apk  else SYSTEMUI_APK_NAME

    warnings: list[str] = []
    errors:   list[str] = []

    # Load rule inventory counts
    modified_patches = _load_modified_class_patches()
    added_patches    = _load_added_class_patches()

    added_by_group: dict[str, int] = {}
    for cp in added_patches:
        g = cp.dex_group or "classes_auto"
        added_by_group[g] = added_by_group.get(g, 0) + 1

    try:
        from factory.patch.mods.legend.mods.apk.systemui.resources.layout_rules import MODIFIED_LAYOUTS, ADDED_LAYOUTS
        layout_count = len(MODIFIED_LAYOUTS) + len(ADDED_LAYOUTS)
    except Exception:
        layout_count = 0

    try:
        from factory.patch.mods.legend.mods.apk.systemui.resources.arsc_rules import MODIFIED_GROUPS, ADDED_GROUPS
        arsc_mod = len(MODIFIED_GROUPS)
        arsc_add = len(ADDED_GROUPS)
    except Exception:
        arsc_mod = arsc_add = 0

    try:
        from factory.patch.mods.legend.mods.apk.systemui.resources.values_rules import RESOURCE_FILE_COUNTS
        add_xml_count = sum(RESOURCE_FILE_COUNTS.values())
    except Exception:
        add_xml_count = 0

    try:
        from factory.patch.mods.legend.mods.apk.systemui.resources.add_resource_rules import (
            ADDED_LAYOUTS as RESOURCE_ADDED_LAYOUTS,
            RESOURCE_COUNTS_BY_FOLDER,
            RESOURCE_RULES,
        )
        managed_resource_count = len(RESOURCE_RULES)
        managed_resource_by_folder = dict(RESOURCE_COUNTS_BY_FOLDER)
        managed_added_layouts = list(RESOURCE_ADDED_LAYOUTS)
    except Exception:
        managed_resource_count = 0
        managed_resource_by_folder = {}
        managed_added_layouts = []

    report: dict = {
        "stage":                   "legend_systemui_apk",
        "flavor":                  flavor,
        "dry_run":                 not execute,
        "project_dir":             str(project_dir),
        "work_dir":                str(effective_work),
        "apkeditor_jar":           apkeditor_str,
        "apkeditor_exists":        apkeditor_jar is not None,
        "original_apk_path":       apk_str,
        "restored_apk_path":       apk_str,
        "original_apk_name":       apk_name,
        "final_filename":          SYSTEMUI_APK_NAME,
        "apk_found":               systemui_apk is not None,
        "backup_policy":           "disabled",
        "runtime_reads_legend_dir": False,
        "runtime_reads_mtcr_files": False,
        # Inventory
        "smali_modified_count":    len(modified_patches),
        "smali_added_count":       len(added_patches),
        "smali_added_by_group":    added_by_group,
        "managed_resource_count":  managed_resource_count,
        "managed_resource_by_folder": managed_resource_by_folder,
        "copied_resource_count":   0,
        "copied_resource_by_folder": {},
        "added_layouts":           managed_added_layouts,
        "failed_missing_assets":   [],
        "layout_rule_count":       layout_count,
        "arsc_modified_count":     arsc_mod,
        "arsc_added_count":        arsc_add,
        "add_resource_xml_count":  add_xml_count,
        # Stage placeholders
        "decompile_status":        "N/A",
        "resource_copy_status":    "N/A",
        "add_resource_status":     "N/A",
        "layout_status":           "N/A",
        "layout_applied":          0,
        "arsc_status":             "N/A",
        "arsc_applied":            0,
        "smali_status":            "N/A",
        "smali_patches_applied":   0,
        "added_classes_status":    "N/A",
        "added_classes_count":     0,
        "duplicate_class_count":   0,
        "added_classes_info":      {},
        "rebuild_status":          "N/A",
        "restore_status":          "N/A",
        "class_results":           [],
        "warnings":                warnings,
        "errors":                  errors,
        "final_status":            "DRY_RUN",
    }

    # ── Flavor guard ──────────────────────────────────────────────────────────
    if not _is_legend(flavor):
        report["final_status"] = "SKIPPED_NON_LEGEND"
        return report

    # ── Dry-run ───────────────────────────────────────────────────────────────
    if not execute:
        if not apkeditor_jar:
            warnings.append("APKEditor.jar not found")
        if not systemui_apk:
            warnings.append("MiuiSystemUI.apk not found in project")

        report["planned_steps"] = [
            f"[1] Flavor check: '{flavor}' → Legend OK",
            f"[2] APK: {apk_str}",
            f"[3] APKEditor: {apkeditor_str}",
            f"[4] Decompile → {effective_work / 'MiuiSystemUI_apk_src'}/",
            f"[5] Merge {add_xml_count} managed add/ resource XMLs",
            f"[6] Copy {managed_resource_count} managed drawable/layout resources",
            f"[7] Apply {layout_count} layout XML patches (text-diff hunks)",
            f"[8] Apply {arsc_mod + arsc_add} arsc resource changes",
            f"[9] Apply {len(modified_patches)} smali modified-class patches (smart Tier 1-4)",
            f"[10] Place {len(added_patches)} added classes into a valid smali_classesN root",
            f"     classes_auto={added_by_group.get('classes_auto',0)}",
            f"[11] Rebuild MiuiSystemUI.apk with APKEditor",
            f"[12] Restore to exact original path as MiuiSystemUI.apk (no backup, no renamed copy)",
        ]

        if not systemui_apk:
            report["final_status"] = "SKIPPED_MISSING_APK"
        elif not apkeditor_jar:
            report["final_status"] = "SKIPPED_MISSING_TOOL"
        else:
            report["final_status"] = "DRY_RUN"

        _write_reports(report)
        return report

    # ── Execute: guard preconditions ──────────────────────────────────────────
    if not systemui_apk:
        errors.append("MiuiSystemUI.apk not found in project")
        report["final_status"] = "SKIPPED_MISSING_APK"
        _write_reports(report)
        return report

    if not apkeditor_jar:
        errors.append("APKEditor.jar not found")
        report["final_status"] = "SKIPPED_MISSING_TOOL"
        _write_reports(report)
        return report

    # ── Step 1: Copy & decompile ──────────────────────────────────────────────
    print(f"[systemui_runner] Copying {SYSTEMUI_APK_NAME} to work dir ...")
    try:
        prepare_apk_work_dir(effective_work, SYSTEMUI_APK_NAME)
        work_apk = copy_apk_to_work(systemui_apk, effective_work)
    except Exception as exc:
        errors.append(f"Copy failed: {exc}")
        report["final_status"] = "FAILED"
        _write_reports(report)
        return report

    decompiled_dir = effective_work / "MiuiSystemUI_apk_src"
    print(f"[systemui_runner] Decompiling {SYSTEMUI_APK_NAME} ...")
    ok = decompile_apk(apkeditor_jar, work_apk, decompiled_dir)
    report["decompile_status"] = "OK" if ok else "FAILED"
    if not ok:
        errors.append("Decompile failed")
        report["final_status"] = "FAILED"
        _write_reports(report)
        return report

    smali_roots = _find_smali_roots(decompiled_dir)
    report["added_classes_info"]["existing_roots"] = [r.name for r in smali_roots]

    # ── Step 2: Drawable/layout resource copies ───────────────────────────────
    print(f"[systemui_runner] Copying managed drawable/layout resources ...")
    resource_copy = _apply_resource_copy_rules(decompiled_dir, dry_run=False)
    report["resource_copy_status"] = resource_copy.get("status", "UNKNOWN")
    report["systemui_asset_root"]  = resource_copy.get("asset_root", "UNKNOWN")
    report["copied_resource_count"] = resource_copy.get("copied", 0)
    report["copied_resource_by_folder"] = resource_copy.get("by_folder", {})
    missing_assets = resource_copy.get("missing_assets", [])
    report["failed_missing_assets"] = missing_assets
    report["missing_asset_count"]   = len(missing_assets)
    print(f"[systemui_runner] systemui_asset_root : {report['systemui_asset_root']}")
    print(f"[systemui_runner] missing_asset_count : {report['missing_asset_count']}")
    if resource_copy.get("status") == "FAILED_MISSING_ASSET":
        print(f"[systemui_runner] ERROR: required assets missing from {report['systemui_asset_root']}")
        for entry in missing_assets[:20]:
            src = entry.get("source", "?")
            req = "REQUIRED" if entry.get("required", True) else "optional"
            print(f"[systemui_runner]   [{req}] {src}")
        for missing in missing_assets:
            if missing.get("required", True):
                errors.append(f"resource_copy: missing asset {missing.get('source')}")
            else:
                warnings.append(f"resource_copy: optional asset missing (skipped) {missing.get('source')}")
        if any(m.get("required", True) for m in missing_assets):
            report["final_status"] = "FAILED_MISSING_ASSET"
            _write_reports(report)
            return report

    # ── Step 3: Add resource XMLs ─────────────────────────────────────────────
    print(f"[systemui_runner] Merging managed add/ resource XMLs ...")
    add_res = _apply_add_resources(decompiled_dir, dry_run=False)
    report["add_resource_status"] = add_res.get("status", "UNKNOWN")
    for e in add_res.get("errors", []):
        warnings.append(f"add_resources: {e}")

    # ── Step 4: Layout XML patches ────────────────────────────────────────────
    print(f"[systemui_runner] Applying layout XML patches ...")
    layout_res = _apply_layout_patches(decompiled_dir, dry_run=False)
    report["layout_status"]  = layout_res.get("status", "UNKNOWN")
    report["layout_applied"] = layout_res.get("applied", 0)
    for e in layout_res.get("errors", []):
        warnings.append(f"layout: {e}")

    # ── Step 5: Arsc resource patches ─────────────────────────────────────────
    print(f"[systemui_runner] Applying arsc resource patches ...")
    arsc_res = _apply_arsc_patches(decompiled_dir, dry_run=False)
    report["arsc_status"]  = arsc_res.get("status", "UNKNOWN")
    report["arsc_applied"] = arsc_res.get("applied", 0)
    for e in arsc_res.get("errors", []):
        warnings.append(f"arsc: {e}")

    # ── Step 6: Modified smali class patches ──────────────────────────────────
    print(f"[systemui_runner] Applying {len(modified_patches)} smali class patches ...")
    smali_roots_live = _find_smali_roots(decompiled_dir)
    class_results, smali_summary = _apply_smali_patches(
        smali_roots_live, modified_patches, dry_run=False
    )
    report["smali_status"]          = smali_summary.get("status", "UNKNOWN")
    report["smali_patches_applied"] = smali_summary.get("patches_applied", 0)
    report["class_results"] = [
        {
            "target_class": cr.target_class,
            "dex_group": cr.dex_group,
            "class_match_strategy": cr.class_match_strategy,
            "patch_results": [
                {
                    "patch_id": pr.patch_id,
                    "patch_type": pr.patch_type,
                    "status": pr.status.value,
                    "class_match_strategy": pr.class_match_strategy,
                    "method_match_strategy": pr.method_match_strategy,
                    "error": pr.error,
                }
                for pr in cr.patch_results
            ],
        }
        for cr in class_results
    ]
    if smali_summary.get("patches_failed", 0) > 0:
        errors.append(
            f"{smali_summary['patches_failed']} required smali patches failed"
        )

    # ── Step 7: Added smali classes ───────────────────────────────────────────
    print(f"[systemui_runner] Placing {len(added_patches)} added smali classes ...")
    added_res = _apply_added_classes(decompiled_dir, added_patches, dry_run=False)
    report["added_classes_status"] = added_res.get("status", "UNKNOWN")
    report["added_classes_count"]  = added_res.get("classes_added", 0)
    report["duplicate_class_count"] = added_res.get("duplicate_class_count", 0)
    report["added_classes_info"]["new_roots_created"] = added_res.get("new_roots_created", [])
    report["added_classes_info"]["smali_root_chosen"] = added_res.get("smali_root_chosen", "")
    report["added_classes_info"]["class_results"] = added_res.get("class_results", [])
    for e in added_res.get("errors", []):
        errors.append(f"added_classes: {e}")

    if added_res.get("status") in {"FAILED", "FAILED_DUPLICATE_CLASS_CONFLICT"}:
        report["final_status"] = "FAILED"
        _write_reports(report)
        return report
    # ── Step 8: Rebuild APK ───────────────────────────────────────────────────
    print(f"[systemui_runner] Rebuilding {SYSTEMUI_APK_NAME} ...")
    rebuild_ok = rebuild_apk(apkeditor_jar, decompiled_dir)
    report["rebuild_status"] = "OK" if rebuild_ok else "FAILED"

    if not rebuild_ok:
        errors.append("Rebuild failed — original APK not touched")
        report["restore_status"] = "SKIPPED"
        report["final_status"]   = "FAILED_REBUILD"
        _write_reports(report)
        return report

    try:
        shutil.rmtree(decompiled_dir, ignore_errors=True)
    except Exception:
        pass

    # ── Step 8: Verify rebuilt APK ────────────────────────────────────────────
    rebuilt = effective_work / SYSTEMUI_APK_NAME
    if not rebuilt.is_file() or rebuilt.stat().st_size == 0:
        errors.append("Rebuilt APK is missing or zero bytes")
        report["restore_status"] = "SKIPPED"
        report["final_status"]   = "FAILED_REBUILD"
        _write_reports(report)
        return report

    # ── Step 9: Restore — exact original filename, no backup ─────────────────
    print(f"[systemui_runner] Restoring {SYSTEMUI_APK_NAME} to original path ...")
    restore = restore_rebuilt_apk_no_backup(rebuilt, systemui_apk)
    ok = restore.get("success", False)
    report["restore_status"] = "OK" if ok else "FAILED"
    report["final_apk_path"] = str(systemui_apk)
    report["restored_apk_path"] = str(systemui_apk)
    report["final_apk_name"] = SYSTEMUI_APK_NAME
    report["final_filename"] = SYSTEMUI_APK_NAME

    if not ok:
        errors.append(f"Restore failed: {restore.get('error', 'unknown')}")
        report["final_status"] = "FAILED"
        _write_reports(report)
        return report

    report["final_status"] = "APPLIED"
    _write_reports(report)
    return report
