"""
Legend add.dex rules — maps each add.dex file to its target JAR.

Assets live in: factory/patch/legend/assets/jar/

Current files:
  freamwork add.dex     → system/framework/framework.jar
  miui-freamwork add.dex → system_ext/framework/miui-framework.jar

Aliases are supported for common spelling variants.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from factory.patch.mods.legend.jar_rules import find_mtcr_dir


@dataclass(frozen=True)
class AddDexRule:
    """One add.dex file and the JAR it targets."""
    # All filenames that identify this add.dex (typo variants included).
    dex_filenames: tuple[str, ...]
    jar_name: str             # e.g. framework.jar
    jar_partition: str        # e.g. system
    jar_rel_path: str         # e.g. framework/framework.jar


LEGEND_ADD_DEX_RULES: list[AddDexRule] = [
    AddDexRule(
        dex_filenames=("freamwork add.dex", "framework add.dex"),
        jar_name="framework.jar",
        jar_partition="system",
        jar_rel_path="framework/framework.jar",
    ),
    AddDexRule(
        dex_filenames=("miui-freamwork add.dex", "miui-framework add.dex"),
        jar_name="miui-framework.jar",
        jar_partition="system_ext",
        jar_rel_path="framework/miui-framework.jar",
    ),
]


def resolve_add_dex_path(rule: AddDexRule, search_dir: Path) -> Path | None:
    """
    Return the first matching add.dex path found in *search_dir* for *rule*,
    trying all filename aliases in order.
    """
    for filename in rule.dex_filenames:
        candidate = search_dir / filename
        if candidate.is_file():
            return candidate
    return None


def find_add_dex_for_jar(jar_name: str, search_dir: Path) -> Path | None:
    """
    Convenience: return the add.dex path for a given jar_name, or None.
    """
    for rule in LEGEND_ADD_DEX_RULES:
        if rule.jar_name == jar_name:
            return resolve_add_dex_path(rule, search_dir)
    return None
