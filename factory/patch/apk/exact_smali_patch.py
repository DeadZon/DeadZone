"""
Exact smali method/field patching for MiuiSystemUI APK patch stage.

Applies dex.mtcr changes to the decompiled APK:
  - Modified classes (in both a/ and b/): replace changed methods by signature,
    add new methods/fields if not present.
  - Added classes (only in b/): reported as info; actual injection handled by
    the dex payload (add/classes*.dex) step.

Safety rules:
  - Match by method signature line, never by line number.
  - Replace whole method body only when exact signature is found in target.
  - If signature not found: SKIPPED_PATTERN_NOT_FOUND.
  - Never overwrite a whole class file.
"""
from __future__ import annotations

import re
from pathlib import Path

from factory.patch.apk.mtcr_apk_reference import read_mtcr_pack


# ---------------------------------------------------------------------------
# Smali root discovery
# ---------------------------------------------------------------------------

def find_smali_roots(decompiled_dir: Path) -> list[Path]:
    """Return all smali* subdirectories in the decompiled APK directory, sorted."""
    roots = []
    if not decompiled_dir.is_dir():
        return roots
    for child in sorted(decompiled_dir.iterdir()):
        if child.is_dir() and child.name.startswith("smali"):
            roots.append(child)
    return roots


def find_class_file(decompiled_dir: Path, class_path: str) -> Path | None:
    """
    Find a smali class file by class path (e.g. "com/android/systemui/Foo").

    Searches all smali* roots. APKEditor may nest files under a 'classes'
    subdirectory (smali/classes/...) or place them directly (smali/...).
    Returns first match or None.
    """
    smali_rel = class_path + ".smali"
    smali_name = Path(smali_rel).name  # just the filename for rglob

    for root in find_smali_roots(decompiled_dir):
        # Direct layout: smali/com/android/...
        candidate = root / smali_rel
        if candidate.is_file():
            return candidate
        # APKEditor layout: smali/classes/com/android/...
        candidate2 = root / "classes" / smali_rel
        if candidate2.is_file():
            return candidate2
        # Generic recursive search with path suffix verification
        for found in root.rglob(smali_name):
            # Normalize to forward slashes for comparison
            found_posix = found.as_posix().replace("\\", "/")
            suffix = "/" + smali_rel.replace("\\", "/")
            if found_posix.endswith(suffix):
                return found
    return None


# ---------------------------------------------------------------------------
# Smali parsing helpers
# ---------------------------------------------------------------------------

def _parse_smali_methods(text: str) -> dict[str, dict]:
    """
    Parse smali text and return {signature_line: {body: [lines], start: int, end: int}}.

    Signature is the full '.method ...' declaration line (stripped).
    Body includes the .method line and .end method line.
    """
    methods: dict[str, dict] = {}
    lines = text.splitlines(keepends=True)
    i = 0
    while i < len(lines):
        stripped = lines[i].strip()
        if stripped.startswith(".method "):
            sig = stripped
            start = i
            j = i + 1
            while j < len(lines):
                if ".end method" in lines[j]:
                    body = lines[start : j + 1]
                    methods[sig] = {"body": body, "start": start, "end": j}
                    i = j + 1
                    break
                j += 1
            else:
                i += 1
        else:
            i += 1
    return methods


def _parse_smali_fields(text: str) -> list[str]:
    """Return all '.field ...' declaration lines from smali text, stripped."""
    return [
        line.strip()
        for line in text.splitlines()
        if line.strip().startswith(".field ")
    ]


def _field_identity(field_line: str) -> str:
    """
    Extract the name:Type signature from a .field declaration for identity comparison.

    ".field public static final TAG:Ljava/lang/String;" -> "TAG:Ljava/lang/String;"
    """
    m = re.search(r"\.field\s+(?:[\w]+\s+)*(\w+:.+)", field_line)
    return m.group(1).strip() if m else field_line


# ---------------------------------------------------------------------------
# Mutation helpers
# ---------------------------------------------------------------------------

def _replace_method_in_text(
    target_text: str,
    sig: str,
    new_body_lines: list[str],
) -> tuple[str, bool]:
    """
    Find the method with signature 'sig' in target_text and replace its body.

    sig is the stripped .method line.
    Returns (new_text, True) if replaced, (target_text, False) if not found.
    """
    lines = target_text.splitlines(keepends=True)
    i = 0
    while i < len(lines):
        if lines[i].strip() == sig:
            # Found start; locate matching .end method
            j = i + 1
            depth = 1
            while j < len(lines):
                if ".end method" in lines[j]:
                    depth -= 1
                    if depth == 0:
                        new_lines = lines[:i] + new_body_lines + lines[j + 1 :]
                        return "".join(new_lines), True
                elif lines[j].strip().startswith(".method "):
                    depth += 1
                j += 1
            break
        i += 1
    return target_text, False


def _add_method_to_text(
    target_text: str,
    method_body_lines: list[str],
) -> tuple[str, str]:
    """
    Add a method to target_text if not already present (matched by signature).

    Returns (new_text, status) where status is one of:
      ADDED, EXISTS_IDENTICAL, EXISTS_DIFFERENT, SKIPPED_EMPTY.
    """
    if not method_body_lines:
        return target_text, "SKIPPED_EMPTY"

    sig = method_body_lines[0].strip()
    existing = _parse_smali_methods(target_text)

    for ex_sig, ex_data in existing.items():
        if ex_sig == sig:
            ex_body = "".join(ex_data["body"]).strip()
            new_body = "".join(method_body_lines).strip()
            if ex_body == new_body:
                return target_text, "EXISTS_IDENTICAL"
            return target_text, "EXISTS_DIFFERENT"

    # Append before the final newline or at the end
    result = target_text.rstrip("\n") + "\n\n" + "".join(method_body_lines)
    if not result.endswith("\n"):
        result += "\n"
    return result, "ADDED"


def _add_field_to_text(
    target_text: str,
    field_line: str,
) -> tuple[str, str]:
    """
    Add a .field declaration to target_text if not already present.

    Returns (new_text, status) where status is one of:
      ADDED, EXISTS_IDENTICAL, EXISTS_DIFFERENT.
    """
    field_id = _field_identity(field_line)
    lines = target_text.splitlines(keepends=True)

    for line in lines:
        ex = line.strip()
        if ex.startswith(".field "):
            if _field_identity(ex) == field_id:
                if ex == field_line:
                    return target_text, "EXISTS_IDENTICAL"
                return target_text, "EXISTS_DIFFERENT"

    # Insert after last class-level declaration header line
    insert_idx = 0
    header_prefixes = (".class ", ".super ", ".implements ", ".source ", ".field ")
    for idx, line in enumerate(lines):
        if line.strip().startswith(header_prefixes):
            insert_idx = idx + 1

    new_lines = lines[:insert_idx] + [field_line + "\n"] + lines[insert_idx:]
    return "".join(new_lines), "ADDED"


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def apply_dex_mtcr(dex_mtcr_path: Path, decompiled_dir: Path) -> dict:
    """
    Apply dex.mtcr exact smali changes to the decompiled APK directory.

    For each modified class (present in both a/ and b/):
      - Compares methods between a/ and b/.
      - Replaces changed method bodies in the target ROM class.
      - Adds methods/fields that exist only in b/ and are absent from target.

    Added classes (only in b/) are handled by the dex payload step; they are
    counted here but not written.

    Returns a status dict with detailed counters and lists.
    """
    result: dict = {
        "pack_path": str(dex_mtcr_path),
        "modified_classes": 0,
        "added_classes_skipped": 0,
        "applied_methods": 0,
        "added_methods": 0,
        "added_fields": 0,
        "skipped_patterns": [],
        "conflicts": [],
        "errors": [],
        "status": "NOT_RUN",
    }

    pack = read_mtcr_pack(dex_mtcr_path)
    if pack is None:
        result["status"] = "FAILED_READ"
        result["errors"].append(f"Could not read {dex_mtcr_path.name}")
        return result

    a_set = set(pack.a_entries)
    b_set = set(pack.b_entries)
    modified = sorted(a_set & b_set)
    added_only = b_set - a_set

    result["modified_classes"] = len(modified)
    result["added_classes_skipped"] = len(added_only)

    for class_path in modified:
        a_text = pack.a_entries[class_path].decode("utf-8", errors="replace")
        b_text = pack.b_entries[class_path].decode("utf-8", errors="replace")

        target_file = find_class_file(decompiled_dir, class_path)
        if target_file is None:
            result["skipped_patterns"].append(
                f"{class_path}: class file not found in decompiled APK"
            )
            continue

        try:
            target_text = target_file.read_text(encoding="utf-8", errors="replace")
        except Exception as exc:
            result["errors"].append(f"{class_path}: read error: {exc}")
            continue

        a_methods = _parse_smali_methods(a_text)
        b_methods = _parse_smali_methods(b_text)
        a_fields = set(_parse_smali_fields(a_text))
        b_fields = _parse_smali_fields(b_text)

        modified_text = target_text
        file_changed = False

        # Apply changed/added methods
        for sig, b_data in b_methods.items():
            if sig in a_methods:
                a_body = "".join(a_methods[sig]["body"]).strip()
                b_body = "".join(b_data["body"]).strip()
                if a_body == b_body:
                    continue  # method unchanged between a/ and b/
                # Method changed: replace in target by signature
                new_text, replaced = _replace_method_in_text(
                    modified_text, sig, b_data["body"]
                )
                if replaced:
                    modified_text = new_text
                    result["applied_methods"] += 1
                    file_changed = True
                else:
                    result["skipped_patterns"].append(
                        f"{class_path}: method signature not found in target: {sig}"
                    )
            else:
                # Method only in b/ -> add to target if absent
                new_text, status = _add_method_to_text(modified_text, b_data["body"])
                if status == "ADDED":
                    modified_text = new_text
                    result["added_methods"] += 1
                    file_changed = True
                elif status == "EXISTS_DIFFERENT":
                    result["conflicts"].append(
                        f"{class_path}: added method already exists with different "
                        f"content: {sig}"
                    )
                # EXISTS_IDENTICAL: already present, nothing to do

        # Apply added fields (present in b/ but not in a/)
        for field_line in b_fields:
            if field_line not in a_fields:
                new_text, status = _add_field_to_text(modified_text, field_line)
                if status == "ADDED":
                    modified_text = new_text
                    result["added_fields"] += 1
                    file_changed = True
                elif status == "EXISTS_DIFFERENT":
                    result["conflicts"].append(
                        f"{class_path}: added field already exists with different "
                        f"content: {field_line}"
                    )

        if file_changed:
            try:
                target_file.write_text(modified_text, encoding="utf-8")
            except Exception as exc:
                result["errors"].append(f"{class_path}: write error: {exc}")

    result["status"] = "OK" if not result["errors"] else "PARTIAL"
    return result
