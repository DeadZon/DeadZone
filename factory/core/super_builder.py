from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from factory.core.detector import RomInfo
from factory.core.repacker import DYNAMIC_IMAGES
from factory.core.workspace import Workspace, read_json, write_json

DEFAULT_SUPER_SIZE = 8_500_000_000


def _lpmake() -> str | None:
    return shutil.which("lpmake")


def _partition_name(file_name: str) -> str:
    return Path(file_name).stem


def _build_vab_entries(dynamic: list[Path], group: str) -> list[str]:
    args: list[str] = []
    for img in dynamic:
        base = _partition_name(img.name).removesuffix("_a").removesuffix("_b")
        size = img.stat().st_size
        args += ["--partition", f"{base}_a:readonly:{size}:{group}_a", "--image", f"{base}_a={img}"]
        args += ["--partition", f"{base}_b:readonly:0:{group}_b"]
    return args


def build_super(ws: Workspace, info: RomInfo, inspection: dict) -> dict:
    final_super = ws.images / "super.img"
    dynamic = sorted(p for p in ws.partitions.glob("*.img") if p.name in DYNAMIC_IMAGES)
    if final_super.is_file() and not inspection.get("needs_super_rebuild"):
        result = {"status": "PRESERVED", "super_img": str(final_super), "super_size": final_super.stat().st_size}
        write_json(ws.meta / "super_build_result.json", result)
        print("[SUPER] preserved original")
        return result
    if final_super.is_file() and not dynamic:
        result = {"status": "PRESERVED", "super_img": str(final_super), "super_size": final_super.stat().st_size}
        write_json(ws.meta / "super_build_result.json", result)
        print("[SUPER] preserved available super.img")
        return result
    if not dynamic:
        result = {"status": "SKIPPED", "reason": "no dynamic partition images available"}
        write_json(ws.meta / "super_build_result.json", result)
        print("[SUPER] skipped")
        return result

    lpmake = _lpmake()
    layout = read_json(ws.meta / "super_layout.json", {})
    target_size = max(int(layout.get("super_size") or 0), DEFAULT_SUPER_SIZE)
    group = "dynamic_partitions"
    if not lpmake:
        result = {"status": "FAILED", "reason": "lpmake binary not found", "super_target_size": target_size}
        write_json(ws.meta / "super_build_result.json", result)
        raise RuntimeError(result["reason"])

    group_args = ["--group", f"{group}_a:{target_size // 2}", "--group", f"{group}_b:0"]
    part_args = _build_vab_entries(dynamic, group)
    cmd = [
        lpmake,
        "--metadata-size", "65536",
        "--metadata-slots", "3",
        "--device", f"super:{target_size}",
        "--sparse",
        "--output", str(final_super),
        *group_args,
        *part_args,
    ]
    log = ws.logs / "lpmake.log"
    with log.open("w", encoding="utf-8") as fh:
        proc = subprocess.run(cmd, stdout=fh, stderr=subprocess.STDOUT, text=True)
    if proc.returncode != 0:
        raise RuntimeError(f"lpmake failed with code {proc.returncode}; see {log}")
    result = {
        "status": "OK",
        "super_img": str(final_super),
        "super_size": final_super.stat().st_size,
        "super_target_size": target_size,
        "vab_b_partitions_zero_size": info.slot_mode == "VAB",
        "dynamic_images": [p.name for p in dynamic],
    }
    write_json(ws.meta / "super_build_result.json", result)
    print("[SUPER] rebuilt")
    return result
