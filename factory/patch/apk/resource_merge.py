"""
Resource XML merging for MiuiSystemUI APK patch stage.

Handles three distinct operations:
  1. apply_add_resources  -- merge add/com.android.systemui/ XMLs into decompiled APK res/
  2. apply_xml_mtcr       -- apply exact changed blocks/attributes in layout XMLs
  3. apply_arsc_mtcr      -- apply safe resource value changes from arsc.mtcr

Safety rules:
  - Never replace whole resource files.
  - Merge missing entries only; identical entries are noted, conflicts are skipped.
  - For xml.mtcr: only apply a changed block when the exact old (a/) text is found
    in the target.  If not found: SKIPPED_PATTERN_NOT_FOUND.
  - For arsc.mtcr: only apply a changed value when the target old value matches a/.
    If not matched or type requires binary tools: NEEDS_MANUAL_RESOURCE_RULE.
  - No backup files are created.
"""
from __future__ import annotations

import difflib
import xml.etree.ElementTree as ET
from pathlib import Path

from factory.patch.apk.mtcr_apk_reference import read_mtcr_pack


# ---------------------------------------------------------------------------
# Shared XML helpers
# ---------------------------------------------------------------------------

_VALUE_TYPES = frozenset({"string", "array", "bool", "dimen", "integer", "plurals"})

# Candidate filenames to search first before falling back to content scan.
_TYPE_FILE_CANDIDATES: dict[str, list[str]] = {
    "string":  ["strings.xml",   "string.xml"],
    "array":   ["arrays.xml",    "array.xml"],
    "bool":    ["booleans.xml",  "bool.xml"],
    "dimen":   ["dimens.xml",    "dimen.xml"],
    "integer": ["integers.xml",  "integer.xml"],
    "plurals": ["plurals.xml"],
}

# Tags that indicate a file covers a given resource type.
_TYPE_TO_TAGS: dict[str, tuple[str, ...]] = {
    "string":  ("string",),
    "array":   ("string-array", "integer-array", "array"),
    "bool":    ("bool",),
    "dimen":   ("dimen",),
    "integer": ("integer",),
    "plurals": ("plurals",),
}

_TYPE_DEFAULT_FILENAME: dict[str, str] = {
    "string":  "strings.xml",
    "array":   "arrays.xml",
    "bool":    "booleans.xml",
    "dimen":   "dimens.xml",
    "integer": "integers.xml",
    "plurals": "plurals.xml",
}


def _find_res_file_for_type(values_dir: Path, res_type: str) -> Path | None:
    """
    Locate the resource file in values_dir that holds entries of res_type.

    Tries known candidate filenames first, then scans XML content as fallback.
    Returns None if the directory does not exist.
    """
    if not values_dir.is_dir():
        return None

    for name in _TYPE_FILE_CANDIDATES.get(res_type, [f"{res_type}s.xml", f"{res_type}.xml"]):
        f = values_dir / name
        if f.is_file():
            return f

    # Content-based fallback: look for the type's XML tags inside any .xml file
    search_tags = _TYPE_TO_TAGS.get(res_type, (res_type,))
    for xml_file in sorted(values_dir.glob("*.xml")):
        try:
            text = xml_file.read_text(encoding="utf-8", errors="replace")
            if any(f"<{tag}" in text for tag in search_tags):
                return xml_file
        except Exception:
            continue
    return None


def _qualifier_from_stem(stem: str) -> str:
    """
    Extract Android resource qualifier from a resource file stem.

    "string-ar"      -> "ar"
    "array-zh-rCN"   -> "zh-rCN"
    "bool-ja"        -> "ja"
    "array"          -> "" (default, no qualifier)
    """
    parts = stem.split("-", 1)
    return parts[1] if len(parts) == 2 else ""


def _res_values_dir(decompiled_dir: Path, qualifier: str) -> Path:
    """Return the res/values[-qualifier]/ path inside the decompiled APK."""
    name = f"values-{qualifier}" if qualifier else "values"
    return decompiled_dir / "res" / name


def _xml_safe_write(tree_root: ET.Element, dest: Path) -> None:
    """Write an ElementTree root to dest with indentation and XML declaration."""
    ET.indent(tree_root, space="    ")
    text = '<?xml version="1.0" encoding="utf-8"?>\n' + ET.tostring(
        tree_root, encoding="unicode"
    )
    dest.write_text(text, encoding="utf-8")


# ---------------------------------------------------------------------------
# 1. apply_add_resources
# ---------------------------------------------------------------------------

def _merge_resource_entries(src_path: Path, dst_path: Path | None,
                             values_dir: Path, res_type: str) -> dict:
    """
    Merge resource entries from src_path into dst_path.

    If dst_path is None or does not exist, a new file is created under values_dir
    using the default filename for res_type.

    Returns a per-file summary dict.
    """
    summary: dict = {
        "src": str(src_path),
        "dst": None,
        "entries_found": 0,
        "entries_added": 0,
        "exists_identical": 0,
        "conflicts": [],
        "errors": [],
    }

    try:
        src_root = ET.fromstring(
            src_path.read_text(encoding="utf-8", errors="replace")
        )
    except Exception as exc:
        summary["errors"].append(f"Parse src XML failed: {exc}")
        return summary

    src_entries: dict[str, ET.Element] = {
        child.get("name", ""): child
        for child in src_root
        if child.get("name")
    }
    summary["entries_found"] = len(src_entries)

    if not src_entries:
        return summary

    # Resolve or create destination file
    if dst_path is None or not dst_path.is_file():
        if dst_path is None:
            fname = _TYPE_DEFAULT_FILENAME.get(res_type, f"{res_type}s.xml")
            dst_path = values_dir / fname
        summary["dst"] = str(dst_path)
        values_dir.mkdir(parents=True, exist_ok=True)
        dst_path.write_text(
            '<?xml version="1.0" encoding="utf-8"?>\n<resources>\n</resources>\n',
            encoding="utf-8",
        )

    summary["dst"] = str(dst_path)

    try:
        dst_root = ET.fromstring(
            dst_path.read_text(encoding="utf-8", errors="replace")
        )
    except Exception as exc:
        summary["errors"].append(f"Parse dst XML failed: {exc}")
        return summary

    dst_entries: dict[str, ET.Element] = {
        child.get("name", ""): child
        for child in dst_root
        if child.get("name")
    }

    modified = False
    for name, src_child in src_entries.items():
        if name in dst_entries:
            src_str = ET.tostring(src_child, encoding="unicode").strip()
            dst_str = ET.tostring(dst_entries[name], encoding="unicode").strip()
            if src_str == dst_str:
                summary["exists_identical"] += 1
            else:
                summary["conflicts"].append(name)
        else:
            dst_root.append(src_child)
            summary["entries_added"] += 1
            modified = True

    if modified:
        try:
            _xml_safe_write(dst_root, dst_path)
        except Exception as exc:
            summary["errors"].append(f"Write failed: {exc}")

    return summary


def apply_add_resources(ref_dir: Path, decompiled_dir: Path) -> dict:
    """
    Merge all add/com.android.systemui/ resource XMLs into the decompiled APK.

    Maps add/{type}/{type-qualifier}.xml -> res/values-{qualifier}/{type}s.xml.
    Merges missing entries; reports conflicts and identical entries.

    Returns a summary dict.
    """
    result: dict = {
        "files_found": 0,
        "files_added": 0,
        "entries_merged": 0,
        "exists_identical": 0,
        "conflicts": [],
        "errors": [],
        "details": [],
        "status": "NOT_RUN",
    }

    add_res_dir = ref_dir / "add" / "com.android.systemui"
    if not add_res_dir.is_dir():
        result["status"] = "SKIPPED_NOT_FOUND"
        result["errors"].append(f"add/com.android.systemui/ not found: {add_res_dir}")
        return result

    for res_type in ("string", "array", "bool", "dimen", "integer", "plurals"):
        type_dir = add_res_dir / res_type
        if not type_dir.is_dir():
            continue

        for src_file in sorted(type_dir.glob("*.xml")):
            qualifier = _qualifier_from_stem(src_file.stem)
            values_dir = _res_values_dir(decompiled_dir, qualifier)
            dst_file = _find_res_file_for_type(values_dir, res_type)

            result["files_found"] += 1

            summary = _merge_resource_entries(src_file, dst_file, values_dir, res_type)
            result["details"].append(summary)
            result["entries_merged"] += summary.get("entries_added", 0)
            result["exists_identical"] += summary.get("exists_identical", 0)
            result["conflicts"].extend(summary.get("conflicts", []))
            result["errors"].extend(summary.get("errors", []))
            if summary.get("entries_added", 0) > 0:
                result["files_added"] += 1

    result["status"] = "OK" if not result["errors"] else "PARTIAL"
    return result


# ---------------------------------------------------------------------------
# 2. apply_xml_mtcr
# ---------------------------------------------------------------------------

def _find_layout_file(decompiled_dir: Path, layout_name: str) -> Path | None:
    """
    Find a layout XML file by name inside the decompiled APK.

    Searches res/layout*/ directories first (fastest), then falls back to a
    recursive search anywhere under res/ that contains 'layout' in the path.
    """
    res_dir = decompiled_dir / "res"
    if res_dir.is_dir():
        for layout_dir in sorted(res_dir.iterdir()):
            if layout_dir.is_dir() and layout_dir.name.startswith("layout"):
                candidate = layout_dir / layout_name
                if candidate.is_file():
                    return candidate
        # Broader fallback
        for found in res_dir.rglob(layout_name):
            if "layout" in found.parent.name and found.is_file():
                return found
    return None


def _apply_diff_hunks(a_text: str, b_text: str, target_text: str) -> tuple[str, int, list[str]]:
    """
    Compute a unified diff between a_text and b_text, then apply each changed
    hunk to target_text by finding the exact old block.

    Returns (new_target_text, applied_count, skipped_list).
    Skipped hunks are reported with a short description.
    """
    a_lines = a_text.splitlines(keepends=True)
    b_lines = b_text.splitlines(keepends=True)

    diff_lines = list(difflib.unified_diff(a_lines, b_lines, n=2))
    if not diff_lines:
        return target_text, 0, []

    # Parse diff into (old_lines, new_lines) hunks
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
        else:
            # Context line: belongs to both sides (we don't include in the replace block)
            pass

    if old_buf or new_buf:
        hunks.append((old_buf, new_buf))

    result_text = target_text
    applied = 0
    skipped: list[str] = []

    for old_lines, new_lines in hunks:
        if not old_lines:
            # Pure addition with no anchor -- cannot place safely
            skipped.append(
                f"pure-addition hunk skipped (no old block to anchor): "
                f"{new_lines[0].strip()[:60]!r}" if new_lines else "empty hunk"
            )
            continue

        old_block = "".join(old_lines)
        new_block = "".join(new_lines)

        if old_block in result_text:
            result_text = result_text.replace(old_block, new_block, 1)
            applied += 1
        else:
            # Try a whitespace-relaxed match: strip trailing spaces per line
            old_stripped = "\n".join(l.rstrip() for l in old_lines)
            target_lines = result_text.splitlines()
            target_stripped = "\n".join(l.rstrip() for l in target_lines)
            if old_stripped in target_stripped:
                result_text = result_text.replace(old_block, new_block, 1)
                applied += 1
            else:
                skipped.append(
                    f"old block not found in target: {old_block.strip()[:80]!r}"
                )

    return result_text, applied, skipped


def apply_xml_mtcr(xml_mtcr_path: Path, decompiled_dir: Path) -> dict:
    """
    Apply xml.mtcr layout changes to the decompiled APK.

    For each layout file in both a/ and b/:
      - Compute diff between a/ (reference) and b/ (modified).
      - Apply each changed block to the target only when the old a/ block
        is found verbatim.
      - Report SKIPPED_PATTERN_NOT_FOUND for any block not matched.

    For layouts only in b/ (added): add to res/layout/ if not present.

    Returns a status dict.
    """
    result: dict = {
        "pack_path": str(xml_mtcr_path),
        "modified_xml_files": 0,
        "applied_blocks": 0,
        "skipped_patterns": [],
        "added_files": 0,
        "conflicts": [],
        "errors": [],
        "status": "NOT_RUN",
    }

    pack = read_mtcr_pack(xml_mtcr_path)
    if pack is None:
        result["status"] = "FAILED_READ"
        result["errors"].append(f"Could not read {xml_mtcr_path.name}")
        return result

    a_set = set(pack.a_entries)
    b_set = set(pack.b_entries)
    modified = sorted(a_set & b_set)
    added_only = sorted(b_set - a_set)

    for xml_path in modified:
        layout_name = Path(xml_path).name
        target_file = _find_layout_file(decompiled_dir, layout_name)

        if target_file is None:
            result["skipped_patterns"].append(
                f"{layout_name}: not found in decompiled APK"
            )
            continue

        a_text = pack.a_entries[xml_path].decode("utf-8", errors="replace")
        b_text = pack.b_entries[xml_path].decode("utf-8", errors="replace")

        try:
            target_text = target_file.read_text(encoding="utf-8", errors="replace")
        except Exception as exc:
            result["errors"].append(f"{layout_name}: read error: {exc}")
            continue

        new_text, applied, skipped = _apply_diff_hunks(a_text, b_text, target_text)
        result["applied_blocks"] += applied
        result["skipped_patterns"].extend(f"{layout_name}: {s}" for s in skipped)

        if applied > 0 and new_text != target_text:
            try:
                target_file.write_text(new_text, encoding="utf-8")
                result["modified_xml_files"] += 1
            except Exception as exc:
                result["errors"].append(f"{layout_name}: write error: {exc}")

    # Handle layouts only in b/ (added files)
    for xml_path in added_only:
        layout_name = Path(xml_path).name
        if _find_layout_file(decompiled_dir, layout_name) is not None:
            continue  # already present
        # Add to default res/layout/
        layout_dir = decompiled_dir / "res" / "layout"
        if layout_dir.is_dir():
            new_file = layout_dir / layout_name
            try:
                new_file.write_bytes(pack.b_entries[xml_path])
                result["added_files"] += 1
            except Exception as exc:
                result["errors"].append(f"{layout_name}: add error: {exc}")

    result["status"] = "OK" if not result["errors"] else "PARTIAL"
    return result


# ---------------------------------------------------------------------------
# 3. apply_arsc_mtcr
# ---------------------------------------------------------------------------

def _arsc_entry_to_values_dir(decompiled_dir: Path, entry_path: str) -> tuple[str, str]:
    """
    Map an arsc.mtcr entry path to (res_type, qualifier).

    Entry format: "com.android.systemui/{type}/{type}[-qualifier]"
    Examples:
      "com.android.systemui/string/string"      -> ("string", "")
      "com.android.systemui/string/string-ar"   -> ("string", "ar")
      "com.android.systemui/array/array-zh-rCN" -> ("array", "zh-rCN")
    """
    parts = entry_path.split("/")
    if len(parts) < 3:
        return "", ""

    res_type = parts[1]           # e.g. "string"
    leaf = parts[2]               # e.g. "string-ar"

    leaf_parts = leaf.split("-", 1)
    qualifier = leaf_parts[1] if len(leaf_parts) == 2 else ""

    return res_type, qualifier


def apply_arsc_mtcr(arsc_mtcr_path: Path, decompiled_dir: Path) -> dict:
    """
    Apply arsc.mtcr resource value changes to the decompiled APK.

    For entries in both a/ and b/ (modified):
      - Only applies a value change when the target's current value matches a/.
      - Reports NEEDS_MANUAL_RESOURCE_RULE for types that require binary arsc tools.
    For entries only in b/ (added):
      - Merges new resource entries if they can be expressed as XML values.

    Returns a status dict.
    """
    result: dict = {
        "pack_path": str(arsc_mtcr_path),
        "modified_resource_groups": 0,
        "applied_safe_changes": 0,
        "needs_manual_rule": [],
        "skipped_changes": [],
        "errors": [],
        "status": "NOT_RUN",
    }

    pack = read_mtcr_pack(arsc_mtcr_path)
    if pack is None:
        result["status"] = "FAILED_READ"
        result["errors"].append(f"Could not read {arsc_mtcr_path.name}")
        return result

    a_set = set(pack.a_entries)
    b_set = set(pack.b_entries)

    # Process both modified (a & b) and added (b only) entries
    all_b_entries = sorted(b_set)

    for entry_path in all_b_entries:
        b_bytes = pack.b_entries[entry_path]
        a_bytes = pack.a_entries.get(entry_path)

        # Skip if identical to a/
        if a_bytes is not None and a_bytes == b_bytes:
            continue

        res_type, qualifier = _arsc_entry_to_values_dir(decompiled_dir, entry_path)

        if not res_type or res_type not in _VALUE_TYPES:
            result["needs_manual_rule"].append(
                f"{entry_path}: type '{res_type}' requires binary arsc tool"
            )
            continue

        values_dir = _res_values_dir(decompiled_dir, qualifier)
        target_file = _find_res_file_for_type(values_dir, res_type)

        if target_file is None:
            # No target file: for added entries, create it; for modified, skip.
            if a_bytes is None:
                # Pure addition -- merge via add resources approach
                try:
                    b_text = b_bytes.decode("utf-8", errors="replace")
                    b_root = ET.fromstring(b_text)
                except Exception as exc:
                    result["errors"].append(f"{entry_path}: parse error: {exc}")
                    continue

                fname = _TYPE_DEFAULT_FILENAME.get(res_type, f"{res_type}s.xml")
                new_file = values_dir / fname
                values_dir.mkdir(parents=True, exist_ok=True)
                try:
                    _xml_safe_write(b_root, new_file)
                    result["applied_safe_changes"] += len(list(b_root))
                    result["modified_resource_groups"] += 1
                except Exception as exc:
                    result["errors"].append(f"{entry_path}: create error: {exc}")
            else:
                result["skipped_changes"].append(
                    f"{entry_path}: target resource file not found in decompiled APK"
                )
            continue

        # Parse a/, b/, and target XML
        try:
            b_text = b_bytes.decode("utf-8", errors="replace")
            b_root = ET.fromstring(b_text)
            b_entries: dict[str, ET.Element] = {
                el.get("name", ""): el for el in b_root if el.get("name")
            }
        except Exception as exc:
            result["errors"].append(f"{entry_path}: parse b/ error: {exc}")
            continue

        a_entries: dict[str, ET.Element] = {}
        if a_bytes is not None:
            try:
                a_root = ET.fromstring(a_bytes.decode("utf-8", errors="replace"))
                a_entries = {el.get("name", ""): el for el in a_root if el.get("name")}
            except Exception:
                pass

        try:
            target_text = target_file.read_text(encoding="utf-8", errors="replace")
            target_root = ET.fromstring(target_text)
            target_entries: dict[str, ET.Element] = {
                el.get("name", ""): el for el in target_root if el.get("name")
            }
        except Exception as exc:
            result["errors"].append(f"{entry_path}: parse target error: {exc}")
            continue

        group_changed = False

        for name, b_el in b_entries.items():
            if name in a_entries:
                # Modified entry: only apply if target value matches a/ (old) value
                a_val = ET.tostring(a_entries[name], encoding="unicode").strip()
                b_val = ET.tostring(b_el, encoding="unicode").strip()
                if a_val == b_val:
                    continue  # unchanged

                if name not in target_entries:
                    result["skipped_changes"].append(
                        f"{entry_path}/{name}: not found in target"
                    )
                    continue

                t_val = ET.tostring(target_entries[name], encoding="unicode").strip()
                if t_val != a_val:
                    result["skipped_changes"].append(
                        f"{entry_path}/{name}: target value differs from a/ reference "
                        f"(cannot apply safely)"
                    )
                    continue

                # Safe to apply: update target element to match b/
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

                result["applied_safe_changes"] += 1
                group_changed = True

            else:
                # Added entry (only in b/) -- add if not present in target
                if name not in target_entries:
                    target_root.append(b_el)
                    result["applied_safe_changes"] += 1
                    group_changed = True

        if group_changed:
            result["modified_resource_groups"] += 1
            try:
                _xml_safe_write(target_root, target_file)
            except Exception as exc:
                result["errors"].append(f"{entry_path}: write error: {exc}")

    result["status"] = "OK" if not result["errors"] else "PARTIAL"
    return result
