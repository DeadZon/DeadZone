"""
Data model for Legend MiuiSystemUI APK patch rules.

Every per-class rule file under smali/ and smali_added/classesN/ is a plain
Python module that exposes:

  TARGET_APK            : str        — "MiuiSystemUI.apk"
  TARGET_CLASS          : str        — e.g. "com/android/systemui/Foo.smali"
  CLASS_FALLBACK_NAMES  : list[str]  — alt basenames for smart class Tier-2 search
  CLASS_ANCHORS         : list[str]  — content lines for smart class Tier-3 scan
  PATCHES               : list[dict] — one dict per patch entry

  Optional (smali_added/ only):
  DEX_GROUP             : str        — "classes2" | "classes3" | "classes4"

Patch dict keys:
  id              str        — unique patch id within the class
  type            str        — "method_replace" | "method_add" | "field_add" | "class_add"
  method          str        — full .method signature line (or .field for field_add)
  method_name     str        — short name for smart Tier-2 method search
  method_anchors  list[str]  — instruction lines for smart Tier-3 method search
  search          str|None   — a/ smali block (method_replace only); None for add types
  replacement     str        — b/ smali block or full class text (class_add)
  required        bool
  reason          str

Status codes used in reports:
  PATCHED            — change applied in execute mode
  WOULD_PATCH        — dry-run: would apply
  EXISTS             — method/class already present and identical
  SKIPPED_OPTIONAL   — non-required and not found
  FAILED_NOT_FOUND   — required but class/method not found
  FAILED_AMBIGUOUS   — multiple class/method candidates found
  FAILED_REBUILD     — APK rebuild step failed
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


# ── Patch status ───────────────────────────────────────────────────────────────

class PatchStatus(Enum):
    PATCHED          = "PATCHED"
    WOULD_PATCH      = "WOULD_PATCH"
    EXISTS           = "EXISTS"
    SKIPPED_OPTIONAL = "SKIPPED_OPTIONAL"
    FAILED_NOT_FOUND = "FAILED_NOT_FOUND"
    FAILED_AMBIGUOUS = "FAILED_AMBIGUOUS"
    FAILED_REBUILD   = "FAILED_REBUILD"


# ── Data classes ───────────────────────────────────────────────────────────────

@dataclass
class SmaliPatch:
    id: str
    type: str                       # method_replace | method_add | field_add | class_add
    replacement: str
    required: bool = True
    reason: str = ""
    method: str = ""
    method_name: str = ""
    method_anchors: list[str] = field(default_factory=list)
    search: Optional[str] = None


@dataclass
class ClassPatch:
    """All patches for one class in MiuiSystemUI.apk."""
    target_class: str               # e.g. "com/android/systemui/Foo.smali"
    patches: list[SmaliPatch] = field(default_factory=list)
    class_fallback_names: list[str] = field(default_factory=list)
    class_anchors: list[str] = field(default_factory=list)
    dex_group: Optional[str] = None  # "classes2"|"classes3"|"classes4" for added classes


@dataclass
class PatchResult:
    patch_id: str
    patch_type: str
    target_class: str
    status: PatchStatus
    class_match_strategy: str = ""
    method_match_strategy: str = ""
    error: str = ""


@dataclass
class ClassResult:
    target_class: str
    dex_group: Optional[str]
    patch_results: list[PatchResult] = field(default_factory=list)
    class_match_strategy: str = ""
    error: str = ""


# ── Module loaders ─────────────────────────────────────────────────────────────

def load_class_patch(module) -> ClassPatch:
    """Build a ClassPatch from a per-class rule module."""
    patches: list[SmaliPatch] = []
    for p in getattr(module, "PATCHES", []):
        patches.append(SmaliPatch(
            id=p.get("id", ""),
            type=p.get("type", "method_replace"),
            method=p.get("method", ""),
            method_name=p.get("method_name", ""),
            method_anchors=p.get("method_anchors", []),
            search=p.get("search"),
            replacement=p.get("replacement", ""),
            required=p.get("required", True),
            reason=p.get("reason", ""),
        ))
    return ClassPatch(
        target_class=getattr(module, "TARGET_CLASS", ""),
        patches=patches,
        class_fallback_names=getattr(module, "CLASS_FALLBACK_NAMES", []),
        class_anchors=getattr(module, "CLASS_ANCHORS", []),
        dex_group=getattr(module, "DEX_GROUP", None),
    )
