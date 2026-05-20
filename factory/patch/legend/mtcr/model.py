"""
Data model for Legend MTCR class/method-level patch rules.

Every per-class rule file under framework/, services/, miui_framework/,
miui_services/ is a plain Python module that exposes:

  TARGET_JAR   : str   — e.g. "services.jar"
  TARGET_CLASS : str   — e.g. "com/android/server/pm/PackageManagerService.smali"
  PATCHES      : list[dict]   — one dict per SmaliMethodPatch or DexAddPatch

Dict keys (SmaliMethodPatch):
  id          str   — unique patch id within the class
  method      str   — full .method signature line (e.g. ".method public foo()V")
  type        str   — "method_replace" | "method_add" | "class_add"
  search      str | None   — a/ smali block (for method_replace); None for add
  replacement str   — b/ smali block (for replace/add) or full class text
  required    bool
  reason      str

Dict keys (DexAddPatch):
  id           str
  type         str   — "dex_add"
  target_jar   str
  payload_name str   — filename of the add.dex asset
  output_dex   str   — desired dex name inside the rebuilt JAR
  required     bool
  reason       str
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class SmaliMethodPatch:
    id: str
    method: str
    type: str                      # "method_replace" | "method_add" | "class_add"
    replacement: str
    required: bool = True
    reason: str = ""
    search: Optional[str] = None   # a/ block; None for pure additions


@dataclass
class DexAddPatch:
    id: str
    target_jar: str
    payload_name: str
    output_dex: str
    required: bool = True
    reason: str = ""
    type: str = "dex_add"


@dataclass
class MtcrClassPatch:
    """Aggregates all patches for one class."""
    target_jar: str
    target_class: str              # e.g. "com/android/server/pm/PackageManagerService.smali"
    patches: list[SmaliMethodPatch] = field(default_factory=list)


def load_class_patch(module) -> MtcrClassPatch:
    """
    Build a MtcrClassPatch from a per-class rule module.

    The module must expose TARGET_JAR, TARGET_CLASS, and PATCHES.
    """
    patches: list[SmaliMethodPatch] = []
    for p in getattr(module, "PATCHES", []):
        if p.get("type") == "dex_add":
            continue  # DexAddPatch handled separately
        patches.append(SmaliMethodPatch(
            id=p["id"],
            method=p.get("method", ""),
            type=p["type"],
            replacement=p["replacement"],
            required=p.get("required", True),
            reason=p.get("reason", ""),
            search=p.get("search"),
        ))
    return MtcrClassPatch(
        target_jar=module.TARGET_JAR,
        target_class=module.TARGET_CLASS,
        patches=patches,
    )


def load_dex_patches(module) -> list[DexAddPatch]:
    """Extract DexAddPatch entries from a rule module."""
    result: list[DexAddPatch] = []
    for p in getattr(module, "PATCHES", []):
        if p.get("type") == "dex_add":
            result.append(DexAddPatch(
                id=p["id"],
                target_jar=p["target_jar"],
                payload_name=p["payload_name"],
                output_dex=p["output_dex"],
                required=p.get("required", True),
                reason=p.get("reason", ""),
            ))
    return result
