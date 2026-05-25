"""
Legend OS3 debloat profile guard and metadata.

This module is the single source of truth for which build configurations
are allowed to trigger the Legend OS3 debloat profile.  It must be
checked at the top of every entry point that touches OS3 debloat logic.

Guard conditions (ALL must match):
  flavor          in {"legend", "deadzone_legend"}
  os_family       in {"os3", "hyperos3"}   (case-insensitive, dash/space-tolerant)
  debloat_profile == "legend_os3"

Must NOT run for: Gaming, EPiC, base DeadZone, common profiles, other OS versions.
"""
from __future__ import annotations

PROFILE_NAME = "legend_os3_debloat"

SUPPORTED_FLAVORS: frozenset[str] = frozenset({"legend", "deadzone_legend"})
SUPPORTED_OS_FAMILIES: frozenset[str] = frozenset({"os3", "hyperos3"})
REQUIRED_DEBLOAT_PROFILE = "legend_os3"


def _norm_flavor(value: str) -> str:
    return value.lower().replace("-", "_").strip()


def _norm_os_family(value: str) -> str:
    return value.lower().replace(" ", "").replace("-", "").replace("_", "").strip()


def matches_profile(flavor: str, os_family: str, debloat_profile: str) -> bool:
    """Return True only when all three conditions are satisfied."""
    return (
        _norm_flavor(flavor) in SUPPORTED_FLAVORS
        and _norm_os_family(os_family) in SUPPORTED_OS_FAMILIES
        and debloat_profile.lower().strip() == REQUIRED_DEBLOAT_PROFILE
    )


def guard(flavor: str, os_family: str, debloat_profile: str) -> None:
    """Raise ValueError with a descriptive message when profile does not match.

    Callers should treat this as a clean skip, not a fatal error.
    """
    if not matches_profile(flavor, os_family, debloat_profile):
        raise ValueError(
            f"[LEGEND OS3] Profile skipped: not Legend OS3 "
            f"(flavor={flavor!r}, os_family={os_family!r}, "
            f"debloat_profile={debloat_profile!r})"
        )
