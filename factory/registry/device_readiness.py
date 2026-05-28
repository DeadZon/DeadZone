"""Device readiness matrix for DeadZone Factory.

build_device_readiness_matrix(factory_devices_path) -> dict

For every device in factory_devices.json, produces a readiness record that
describes whether the device can be used with the Universal Smart ROM Engine.

Readiness rules
---------------
A device is workflow_ready when:
  - codename is non-empty
  - display_name is non-empty
  - enabled = true

A device is universal_engine_ready when:
  - workflow_ready is True
  - soc is one of: snapdragon, mtk, auto

dropdown_ready:
  - soc = "snapdragon" or "mtk" → True (appears in the corresponding workflow)
  - soc = "auto" → True if universal engine handles auto safely (it does)

requires_manual_soc:
  - True only when soc is completely absent or invalid
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


_VALID_SOCS = {"snapdragon", "mtk", "auto"}
_VALID_SOURCES = {"deadzone", "xiaomi_eu", "custom"}
_VALID_SUPPORT_LEVELS = {"official", "metadata", "auto_detect"}


def _build_record(device: dict[str, Any]) -> dict[str, Any]:
    codename     = (device.get("codename") or "").strip()
    display_name = (device.get("display_name") or "").strip()
    soc          = (device.get("soc") or "auto").strip().lower()
    source       = (device.get("source") or "custom").strip().lower()
    support_level = (device.get("support_level") or "metadata").strip().lower()
    enabled      = bool(device.get("enabled", True))

    notes: list[str] = []

    # Basic validity checks
    if not codename:
        notes.append("codename is empty")
    if not display_name:
        notes.append("display_name is empty")
    if soc not in _VALID_SOCS:
        notes.append(f"unknown soc value: {soc!r}")
    if source not in _VALID_SOURCES:
        notes.append(f"unknown source value: {source!r}")
    if support_level not in _VALID_SUPPORT_LEVELS:
        notes.append(f"unknown support_level value: {support_level!r}")

    workflow_ready = (
        bool(codename)
        and bool(display_name)
        and enabled
        and soc in _VALID_SOCS
    )

    # Devices with soc=auto are not in a specific workflow dropdown but the
    # universal engine can still handle them via the auto path.
    dropdown_ready = workflow_ready and soc in {"snapdragon", "mtk", "auto"}

    universal_engine_ready = workflow_ready  # universal engine is codename-agnostic

    requires_rom_url     = True              # all devices need a ROM URL to build
    requires_manual_soc  = soc not in _VALID_SOCS or not soc

    ready_for_free         = universal_engine_ready
    ready_for_paid_editions = universal_engine_ready

    return {
        "codename":              codename or device.get("codename", ""),
        "display_name":          display_name,
        "soc":                   soc,
        "source":                source,
        "support_level":         support_level,
        "enabled":               enabled,
        "workflow_ready":        workflow_ready,
        "dropdown_ready":        dropdown_ready,
        "universal_engine_ready": universal_engine_ready,
        "requires_rom_url":      requires_rom_url,
        "requires_manual_soc":   requires_manual_soc,
        "ready_for_free":        ready_for_free,
        "ready_for_paid_editions": ready_for_paid_editions,
        "notes":                 notes,
    }


def build_device_readiness_matrix(factory_devices_path: Path) -> dict[str, Any]:
    """Return a readiness matrix for all devices in factory_devices.json.

    Returns
    -------
    {
      "devices": [ <record>, ... ],
      "summary": {
        "total": N,
        "enabled": N,
        "disabled": N,
        "mtk_count": N,
        "snapdragon_count": N,
        "auto_count": N,
        "official_count": N,
        "metadata_count": N,
        "ready_for_free": N,
        "not_ready": N,
        "duplicate_codenames": [ ... ],
        "not_ready_devices": [ { codename, reasons } ],
      }
    }
    """
    path = Path(factory_devices_path)
    raw: list[dict] = json.loads(path.read_text(encoding="utf-8"))

    records = [_build_record(d) for d in raw]

    # Duplicate codename detection
    seen: dict[str, int] = {}
    for r in records:
        cn = r["codename"]
        seen[cn] = seen.get(cn, 0) + 1
    duplicates = sorted(cn for cn, cnt in seen.items() if cnt > 1)

    enabled_records = [r for r in records if r["enabled"]]
    not_ready = [
        {"codename": r["codename"], "reasons": r["notes"]}
        for r in records
        if not r["workflow_ready"]
    ]

    summary: dict[str, Any] = {
        "total":             len(records),
        "enabled":           sum(1 for r in records if r["enabled"]),
        "disabled":          sum(1 for r in records if not r["enabled"]),
        "mtk_count":         sum(1 for r in enabled_records if r["soc"] == "mtk"),
        "snapdragon_count":  sum(1 for r in enabled_records if r["soc"] == "snapdragon"),
        "auto_count":        sum(1 for r in enabled_records if r["soc"] == "auto"),
        "official_count":    sum(1 for r in enabled_records if r["support_level"] == "official"),
        "metadata_count":    sum(1 for r in enabled_records if r["support_level"] == "metadata"),
        "ready_for_free":    sum(1 for r in records if r["ready_for_free"]),
        "not_ready":         len(not_ready),
        "duplicate_codenames": duplicates,
        "not_ready_devices": not_ready,
    }

    return {"devices": records, "summary": summary}
