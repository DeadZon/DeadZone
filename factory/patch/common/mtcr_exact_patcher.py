"""
Kousi-style exact MTCR patching — method and field level only.

Replaces the whole-class-replace behavior of mtcr_patch.apply_mtcr() with
a precise per-method / per-field strategy:

  Modified class (in both a/ and b/):
    ┌ For each method in b/ that differs from a/:
    │   Find the exact a/ method block in the target ROM class.
    │   Replace with the b/ block.
    │   If a/ block not found → SKIPPED_PATTERN_NOT_FOUND.
    └ For each method / field in b/ not in a/:
        Inject into target class.

  Added class (only in b/):
    Copy full b/ smali into the smali tree as a new class.
    Conflicts: EXISTS_IDENTICAL | CONFLICT.

  No whole-class replacement ever happens.
  No line-number patching.
  No guessing.
"""
from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Optional

from factory.patch.common.mtcr_patch import MtcrPack, _find_class_in_smali_roots


# ── Status ────────────────────────────────────────────────────────────────────
class PatchStatus(str, Enum):
    # Modified classes — per method/field operation
    WOULD_APPLY_EXACT_METHOD  = "WOULD_APPLY_EXACT_METHOD"
    APPLIED_EXACT_METHOD      = "APPLIED_EXACT_METHOD"
    WOULD_ADD_METHOD          = "WOULD_ADD_METHOD"
    ADDED_METHOD              = "ADDED_METHOD"
    WOULD_ADD_FIELD           = "WOULD_ADD_FIELD"
    ADDED_FIELD               = "ADDED_FIELD"
    # Added classes (b/ only) — whole-class operation
    WOULD_ADD_CLASS           = "WOULD_ADD_CLASS"
    ADDED_CLASS               = "ADDED_CLASS"
    # Shared
    EXISTS_IDENTICAL          = "EXISTS_IDENTICAL"
    CONFLICT                  = "CONFLICT"
    # Error / skip conditions
    SKIPPED_CLASS_NOT_FOUND   = "SKIPPED_CLASS_NOT_FOUND"
    SKIPPED_PATTERN_NOT_FOUND = "SKIPPED_PATTERN_NOT_FOUND"
    NEEDS_MANUAL_RULE         = "NEEDS_MANUAL_RULE"
    FAILED                    = "FAILED"


@dataclass
class MethodPatchResult:
    """One operation within a class (method, field, or class-level)."""
    class_name: str
    status: PatchStatus
    method_sig: Optional[str] = None    # e.g. ".method public getColor(I)I"
    field_decl: Optional[str] = None    # e.g. ".field public static NEW_FIELD:I"
    target_smali: Optional[Path] = None
    message: str = ""


# ── Smali parsing helpers ─────────────────────────────────────────────────────
def _normalize(text: str) -> str:
    """Strip trailing whitespace from every line; normalize line endings."""
    return "\n".join(line.rstrip() for line in text.splitlines())


def parse_smali_methods(content: str) -> dict[str, str]:
    """
    Parse all .method ... .end method blocks.
    Returns {stripped_first_line → full_block_text}.

    Key: ".method public getColor(I)I"
    Value: the complete block including .method and .end method lines.
    """
    methods: dict[str, str] = {}
    lines = content.splitlines()
    i = 0
    while i < len(lines):
        stripped = lines[i].strip()
        if stripped.startswith(".method "):
            start = i
            sig = stripped
            i += 1
            while i < len(lines):
                if lines[i].strip() == ".end method":
                    i += 1      # include .end method in slice
                    break
                i += 1
            # lines[start:i] ends one past .end method (or at EOF)
            block = "\n".join(lines[start:i])
            # De-duplicate: if same sig appears twice, last one wins.
            methods[sig] = block
        else:
            i += 1
    return methods


def parse_smali_fields(content: str) -> list[str]:
    """
    Return all .field declaration lines (stripped), preserving order.
    Includes both .field and multi-line .field ... .end field blocks as-is.
    For simplicity we only handle single-line .field declarations here
    (multi-line .field with annotations are left as-is).
    """
    fields: list[str] = []
    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith(".field "):
            fields.append(stripped)
    return fields


def _sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="replace")).hexdigest()


# ── Exact replacement helpers ──────────────────────────────────────────────────
def _replace_method_block(
    target_content: str,
    a_block: str,
    b_block: str,
) -> tuple[str, bool]:
    """
    Search *target_content* for the normalized *a_block* and replace with *b_block*.
    Returns (result_content, was_replaced).
    Both target and replacement are normalized before comparison and writing.
    """
    norm_target = _normalize(target_content)
    norm_a = _normalize(a_block)
    norm_b = _normalize(b_block)

    if norm_a not in norm_target:
        return norm_target, False

    return norm_target.replace(norm_a, norm_b, 1), True


def _inject_method_block(target_content: str, b_block: str) -> str:
    """
    Inject *b_block* (a complete .method ... .end method block) into
    *target_content* just before the end of the class.

    Insertion point priority:
      1. Before ".end class" if present.
      2. Otherwise append after the last ".end method".
      3. Otherwise append at end of file.
    """
    norm = _normalize(target_content)
    norm_b = _normalize(b_block)

    if "\n.end class" in norm:
        return norm.replace("\n.end class", f"\n\n{norm_b}\n\n.end class", 1)

    # Find position after last .end method
    marker = "\n.end method"
    pos = norm.rfind(marker)
    if pos != -1:
        insert_at = pos + len(marker)
        return norm[:insert_at] + f"\n\n{norm_b}" + norm[insert_at:]

    return norm.rstrip("\n") + f"\n\n{norm_b}\n"


def _inject_field(target_content: str, field_decl: str) -> str:
    """
    Inject *field_decl* into *target_content* after the last existing .field line
    (or before the first .method if no .field lines exist).
    """
    lines = _normalize(target_content).splitlines()
    last_field_idx = -1
    first_method_idx = -1

    for idx, line in enumerate(lines):
        s = line.strip()
        if s.startswith(".field "):
            last_field_idx = idx
        elif s.startswith(".method ") and first_method_idx == -1:
            first_method_idx = idx

    if last_field_idx >= 0:
        insert_at = last_field_idx + 1
    elif first_method_idx >= 0:
        insert_at = first_method_idx
    else:
        insert_at = len(lines)

    lines.insert(insert_at, field_decl)
    return "\n".join(lines)


def _method_exists_in_target(target_methods: dict[str, str], sig: str) -> Optional[str]:
    """Return the method block if sig exists in target, else None."""
    return target_methods.get(sig)


def _field_exists_in_target(target_content: str, field_decl: str) -> bool:
    """Return True if field_decl is already present in target_content."""
    stripped = field_decl.strip()
    for line in target_content.splitlines():
        if line.strip() == stripped:
            return True
    return False


# ── Per-class exact patcher ───────────────────────────────────────────────────
def _patch_modified_class(
    class_name: str,
    a_content: str,
    b_content: str,
    target_path: Path,
    dry_run: bool,
) -> list[MethodPatchResult]:
    """
    Apply exact method/field diff from (a_content → b_content) onto *target_path*.
    Returns one MethodPatchResult per operation attempted.
    """
    results: list[MethodPatchResult] = []

    # Parse all three sources
    a_methods = parse_smali_methods(a_content)
    b_methods = parse_smali_methods(b_content)
    a_fields  = parse_smali_fields(a_content)
    b_fields  = parse_smali_fields(b_content)

    target_content = target_path.read_text(encoding="utf-8", errors="replace")
    target_methods = parse_smali_methods(target_content)

    working_content = target_content  # accumulate changes

    # ── Methods present in both a/ and b/ (modified) ─────────────────────────
    for sig, b_block in b_methods.items():
        a_block = a_methods.get(sig)
        if a_block is None:
            continue  # added method — handled below

        norm_a = _normalize(a_block)
        norm_b = _normalize(b_block)
        if norm_a == norm_b:
            continue  # identical in a/ and b/ — no patch needed

        if dry_run:
            results.append(MethodPatchResult(
                class_name=class_name,
                method_sig=sig,
                status=PatchStatus.WOULD_APPLY_EXACT_METHOD,
                target_smali=target_path,
            ))
            print(f"[exact] WOULD_APPLY_EXACT_METHOD: {class_name}::{sig.split()[-1]}")
            continue

        new_content, replaced = _replace_method_block(working_content, a_block, b_block)
        if replaced:
            working_content = new_content
            results.append(MethodPatchResult(
                class_name=class_name,
                method_sig=sig,
                status=PatchStatus.APPLIED_EXACT_METHOD,
                target_smali=target_path,
            ))
            print(f"[exact] APPLIED_EXACT_METHOD: {class_name}::{sig.split()[-1]}")
        else:
            results.append(MethodPatchResult(
                class_name=class_name,
                method_sig=sig,
                status=PatchStatus.SKIPPED_PATTERN_NOT_FOUND,
                target_smali=target_path,
                message="a/ method block not found verbatim in target; ROM may differ",
            ))
            print(f"[exact] SKIPPED_PATTERN_NOT_FOUND: {class_name}::{sig.split()[-1]}")

    # ── Methods in b/ but not in a/ (added methods) ───────────────────────────
    for sig, b_block in b_methods.items():
        if sig in a_methods:
            continue  # already handled above

        # Check if this sig already exists in target
        target_block = _method_exists_in_target(target_methods, sig)
        if target_block is not None:
            if _sha256(_normalize(target_block)) == _sha256(_normalize(b_block)):
                results.append(MethodPatchResult(
                    class_name=class_name,
                    method_sig=sig,
                    status=PatchStatus.EXISTS_IDENTICAL,
                    target_smali=target_path,
                    message="method already present, identical",
                ))
                print(f"[exact] EXISTS_IDENTICAL method: {class_name}::{sig.split()[-1]}")
            else:
                results.append(MethodPatchResult(
                    class_name=class_name,
                    method_sig=sig,
                    status=PatchStatus.CONFLICT,
                    target_smali=target_path,
                    message="method already present with different body; not overwritten",
                ))
                print(f"[exact] CONFLICT method: {class_name}::{sig.split()[-1]}")
            continue

        if dry_run:
            results.append(MethodPatchResult(
                class_name=class_name,
                method_sig=sig,
                status=PatchStatus.WOULD_ADD_METHOD,
                target_smali=target_path,
            ))
            print(f"[exact] WOULD_ADD_METHOD: {class_name}::{sig.split()[-1]}")
            continue

        working_content = _inject_method_block(working_content, b_block)
        results.append(MethodPatchResult(
            class_name=class_name,
            method_sig=sig,
            status=PatchStatus.ADDED_METHOD,
            target_smali=target_path,
        ))
        print(f"[exact] ADDED_METHOD: {class_name}::{sig.split()[-1]}")

    # ── Fields in b/ but not in a/ (added fields) ────────────────────────────
    a_field_set = set(a_fields)
    b_field_set = set(b_fields)
    new_fields = b_field_set - a_field_set
    if not new_fields:
        # Also detect fields already in a/ but now different in b/ — these would
        # be complex annotation-level changes; report NEEDS_MANUAL_RULE.
        changed_fields = [(af, bf) for af, bf in zip(a_fields, b_fields) if af != bf and af.split(":")[0] == bf.split(":")[0]]
        for _, bf in changed_fields:
            results.append(MethodPatchResult(
                class_name=class_name,
                field_decl=bf,
                status=PatchStatus.NEEDS_MANUAL_RULE,
                target_smali=target_path,
                message="field annotation/value change requires manual rule",
            ))

    for field_decl in sorted(new_fields):
        if _field_exists_in_target(working_content, field_decl):
            results.append(MethodPatchResult(
                class_name=class_name,
                field_decl=field_decl,
                status=PatchStatus.EXISTS_IDENTICAL,
                target_smali=target_path,
                message="field already present",
            ))
            print(f"[exact] EXISTS_IDENTICAL field: {class_name}  {field_decl}")
            continue

        if dry_run:
            results.append(MethodPatchResult(
                class_name=class_name,
                field_decl=field_decl,
                status=PatchStatus.WOULD_ADD_FIELD,
                target_smali=target_path,
            ))
            print(f"[exact] WOULD_ADD_FIELD: {class_name}  {field_decl}")
            continue

        working_content = _inject_field(working_content, field_decl)
        results.append(MethodPatchResult(
            class_name=class_name,
            field_decl=field_decl,
            status=PatchStatus.ADDED_FIELD,
            target_smali=target_path,
        ))
        print(f"[exact] ADDED_FIELD: {class_name}  {field_decl}")

    # Write modified content back (execute only, and only if something changed)
    if not dry_run and working_content != _normalize(target_content):
        try:
            target_path.write_text(working_content, encoding="utf-8")
        except Exception as exc:
            results.append(MethodPatchResult(
                class_name=class_name,
                status=PatchStatus.FAILED,
                target_smali=target_path,
                message=f"write failed: {exc}",
            ))

    return results


# ── Public API ────────────────────────────────────────────────────────────────
def apply_exact_mtcr(
    pack: MtcrPack,
    unpack_dir: Path,
    dry_run: bool = True,
) -> list[MethodPatchResult]:
    """
    Apply the MTCR pack to the smali workspace at *unpack_dir* using exact
    method-level / field-level patching.

    Modified classes (in both a/ and b/): exact method/field patching.
    Added classes (only in b/): injected as full smali files.
    """
    from factory.patch.common.smali_tools import smali_dirs_in

    smali_roots = smali_dirs_in(unpack_dir)
    results: list[MethodPatchResult] = []

    # Also need a/ content — load it from the pack
    a_content_map: dict[str, str] = {}
    import zipfile
    with zipfile.ZipFile(pack.mtcr_path, "r") as zf:
        for entry in zf.namelist():
            if entry.startswith("a/") and entry != "a/":
                class_name = entry[2:]
                try:
                    a_content_map[class_name] = zf.read(entry).decode("utf-8", errors="replace")
                except Exception:
                    pass

    # ── Modified classes ──────────────────────────────────────────────────────
    for class_name in pack.modified_classes:
        target_path = _find_class_in_smali_roots(smali_roots, class_name)
        if target_path is None:
            results.append(MethodPatchResult(
                class_name=class_name,
                status=PatchStatus.SKIPPED_CLASS_NOT_FOUND,
                message="class not found in any smali_classes* directory",
            ))
            print(f"[exact] SKIPPED_CLASS_NOT_FOUND: {class_name}")
            continue

        a_content = a_content_map.get(class_name, "")
        b_content = pack.b_content.get(class_name, "")

        try:
            class_results = _patch_modified_class(
                class_name=class_name,
                a_content=a_content,
                b_content=b_content,
                target_path=target_path,
                dry_run=dry_run,
            )
            results.extend(class_results)
        except Exception as exc:
            results.append(MethodPatchResult(
                class_name=class_name,
                status=PatchStatus.FAILED,
                target_smali=target_path,
                message=str(exc),
            ))
            print(f"[exact] FAILED: {class_name}: {exc}")

    # ── Added classes (b/ only) — injected as full smali files ───────────────
    # Determine injection smali root: prefer the root where modified classes landed.
    modified_root_names: list[str] = [
        r.class_name for r in results  # not quite right — need the actual root name
    ]
    # Re-derive inject root from smali_roots.
    inject_root = smali_roots[-1] if smali_roots else None

    for class_name in pack.added_classes:
        b_content = pack.b_content.get(class_name, "")
        existing = _find_class_in_smali_roots(smali_roots, class_name)

        if existing is not None:
            existing_content = existing.read_text(encoding="utf-8", errors="replace")
            if _sha256(_normalize(existing_content)) == _sha256(_normalize(b_content)):
                results.append(MethodPatchResult(
                    class_name=class_name,
                    status=PatchStatus.EXISTS_IDENTICAL,
                    target_smali=existing,
                    message="class already present, content identical",
                ))
                print(f"[exact] EXISTS_IDENTICAL class: {class_name}")
            else:
                results.append(MethodPatchResult(
                    class_name=class_name,
                    status=PatchStatus.CONFLICT,
                    target_smali=existing,
                    message="class already present with different content; not overwritten",
                ))
                print(f"[exact] CONFLICT class: {class_name}")
            continue

        if inject_root is None:
            results.append(MethodPatchResult(
                class_name=class_name,
                status=PatchStatus.FAILED,
                message="no smali_classes* directory found for injection",
            ))
            continue

        target_path = inject_root / (class_name + ".smali")

        if dry_run:
            results.append(MethodPatchResult(
                class_name=class_name,
                status=PatchStatus.WOULD_ADD_CLASS,
                target_smali=target_path,
                message=f"would inject into {inject_root.name}/",
            ))
            print(f"[exact] WOULD_ADD_CLASS: {class_name} -> {inject_root.name}/")
            continue

        try:
            target_path.parent.mkdir(parents=True, exist_ok=True)
            target_path.write_text(b_content, encoding="utf-8")
            results.append(MethodPatchResult(
                class_name=class_name,
                status=PatchStatus.ADDED_CLASS,
                target_smali=target_path,
                message=f"injected into {inject_root.name}/",
            ))
            print(f"[exact] ADDED_CLASS: {class_name} -> {inject_root.name}/")
        except Exception as exc:
            results.append(MethodPatchResult(
                class_name=class_name,
                status=PatchStatus.FAILED,
                target_smali=target_path,
                message=str(exc),
            ))
            print(f"[exact] FAILED adding class {class_name}: {exc}")

    return results
