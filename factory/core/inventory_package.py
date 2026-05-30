from __future__ import annotations

import re
import zipfile
from pathlib import Path
from typing import Any

from factory.core.detector import RomInfo
from factory.core.workspace import Workspace, write_json


def _clean(value: object, default: str = "unknown") -> str:
    raw = str(value or default).strip() or default
    return re.sub(r"[^A-Za-z0-9._-]+", "_", raw)


def _android_tag(android: object) -> str:
    raw = str(android or "unknown").strip()
    if not raw or raw == "unknown":
        return "Aunknown"
    return raw if raw.upper().startswith("A") else f"A{raw}"


def _add_file(zf: zipfile.ZipFile, path: Path) -> None:
    if not path.is_file():
        return
    arcname = path.as_posix()
    zf.write(path, arcname)


def build_inventory_package(ws: Workspace, info: RomInfo, inventory: dict[str, Any] | None = None) -> Path:
    codename = _clean(getattr(info, "codename", "unknown"))
    android = _android_tag(_clean(getattr(info, "android_version", "unknown")))
    out = ws.final / f"DeadZone_Stable_{codename}_{android}_AppInventory.zip"
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        inventory_root = ws.root / "inventory"
        if inventory_root.is_dir():
            for path in sorted(p for p in inventory_root.rglob("*") if p.is_file()):
                _add_file(zf, path)
        for path in (
            ws.reports / "image_extraction_report.txt",
            ws.reports / "app_inventory_report.txt",
            ws.meta / "image_extraction.json",
            ws.meta / "app_inventory.json",
        ):
            _add_file(zf, path)
        for path in sorted(ws.logs.glob("image_extraction_*.log")):
            _add_file(zf, path)

    meta = {
        "feature": "Stable App Inventory",
        "zip": str(out),
        "zip_name": out.name,
        "zip_size": out.stat().st_size if out.is_file() else 0,
        "included_roots": [
            "output/workspace/inventory",
            "output/workspace/reports/image_extraction_report.txt",
            "output/workspace/reports/app_inventory_report.txt",
            "output/workspace/meta/image_extraction.json",
            "output/workspace/meta/app_inventory.json",
            "output/workspace/logs/image_extraction_*.log",
        ],
        "excluded": ["ROM ZIP", "super.img", "partition images", "extracted partition files", "secrets", "payload.bin"],
        "total_apps_found": (inventory or {}).get("total_apps_found"),
    }
    write_json(ws.meta / "inventory_package.json", meta)
    print(f"[APP INVENTORY] ZIP: {out}")
    return out
