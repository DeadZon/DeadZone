from __future__ import annotations

import importlib

from factory.core.detector import RomInfo
from factory.core.workspace import Workspace, write_json

STYLE_LABELS = {
    "stable": "Stable",
    "legend": "Legend",
    "gaming": "Gaming",
    "epic": "EPiC",
}


def normalize_style(style: str) -> tuple[str, str]:
    key = style.strip().lower()
    if key not in STYLE_LABELS:
        raise ValueError(f"Unsupported style {style!r}; supported: Stable, Legend, Gaming, EPiC")
    return key, STYLE_LABELS[key]


def apply_style(style: str, ws: Workspace, info: RomInfo) -> dict:
    key, label = normalize_style(style)
    module = importlib.import_module(f"factory.styles.{key}")
    result = module.apply(ws=ws, info=info)
    result.update({"style": label, "style_key": key})
    write_json(ws.meta / "style_result.json", result)
    print(f"[STYLE] {label}")
    return result
