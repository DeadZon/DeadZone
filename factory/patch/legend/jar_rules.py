"""
Legend JAR patch rules — maps each MTCR pack to its target JAR.

Canonical MTCR directory:
  third_party/mezo_core/MEZO_LEGEND/jar/

Fallback directory (current working location):
  Legend/jar/     (repo root)

To add a new Legend JAR patch: place <name>_Legend.mtcr in the canonical dir
and add an entry to LEGEND_JAR_RULES below.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[3]
_MEZO_CORE = _REPO_ROOT / "third_party" / "mezo_core"

# Canonical location per project spec.
_CANONICAL_MTCR_DIR = _MEZO_CORE / "MEZO_LEGEND" / "jar"
# Fallback: where the MTCR files currently live in this repo.
_FALLBACK_MTCR_DIR  = _REPO_ROOT / "Legend" / "jar"


@dataclass(frozen=True)
class LegendJarRule:
    """Links one MTCR pack to the JAR it patches."""
    mtcr_filename: str        # e.g. Framework_Legend.mtcr
    jar_name: str             # e.g. framework.jar
    jar_partition: str        # e.g. system
    jar_rel_path: str         # e.g. framework/framework.jar  (within partition root)


# Order matters for apply: framework → services → miui-framework → miui-services
LEGEND_JAR_RULES: list[LegendJarRule] = [
    LegendJarRule(
        mtcr_filename="Framework_Legend.mtcr",
        jar_name="framework.jar",
        jar_partition="system",
        jar_rel_path="framework/framework.jar",
    ),
    LegendJarRule(
        mtcr_filename="Service_Legend.mtcr",
        jar_name="services.jar",
        jar_partition="system",
        jar_rel_path="framework/services.jar",
    ),
    LegendJarRule(
        mtcr_filename="miui-framework_Legend.mtcr",
        jar_name="miui-framework.jar",
        jar_partition="system_ext",
        jar_rel_path="framework/miui-framework.jar",
    ),
    LegendJarRule(
        mtcr_filename="miui-services_Legend.mtcr",
        jar_name="miui-services.jar",
        jar_partition="system_ext",
        jar_rel_path="framework/miui-services.jar",
    ),
]


def find_mtcr_dir() -> Path | None:
    """
    Return the directory containing Legend MTCR packs.

    Priority:
    1. Canonical: third_party/mezo_core/MEZO_LEGEND/jar/  (preferred going forward)
    2. Fallback:  Legend/jar/  (current repo-root location)
    """
    # Check canonical first — even a single .mtcr there takes priority.
    if _CANONICAL_MTCR_DIR.is_dir():
        if any(_CANONICAL_MTCR_DIR.glob("*.mtcr")):
            return _CANONICAL_MTCR_DIR

    if _FALLBACK_MTCR_DIR.is_dir():
        if any(_FALLBACK_MTCR_DIR.glob("*.mtcr")):
            return _FALLBACK_MTCR_DIR

    return None


def resolve_mtcr_path(rule: LegendJarRule, mtcr_dir: Path) -> Path | None:
    """Return the full path to a rule's MTCR file, or None if missing."""
    p = mtcr_dir / rule.mtcr_filename
    return p if p.is_file() else None
