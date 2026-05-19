"""
MTCR reference pack reader for MiuiSystemUI APK patch stage.

MTCR files are ZIP archives containing:
  info.json      -- metadata (type, version codes, comparison flags)
  a/<path>       -- original reference files (before modification)
  b/<path>       -- modified reference files (after modification)

Classes only in b/ are additions.
Classes in both a/ and b/ are modifications.
"""
from __future__ import annotations

import json
import zipfile
from pathlib import Path
from typing import NamedTuple


class MtcrPack(NamedTuple):
    info: dict
    a_entries: dict  # stripped-path -> bytes
    b_entries: dict  # stripped-path -> bytes


def read_mtcr_pack(pack_path: Path) -> MtcrPack | None:
    """
    Read an MTCR ZIP pack.

    Returns MtcrPack(info, a_entries, b_entries) on success.
    Returns None if the file cannot be read or is not a valid ZIP.
    """
    if not pack_path.is_file():
        return None
    try:
        with zipfile.ZipFile(pack_path) as z:
            names = z.namelist()
            info: dict = {}
            if "info.json" in names:
                info = json.loads(z.read("info.json").decode("utf-8", errors="replace"))
            a_entries: dict = {}
            b_entries: dict = {}
            for name in names:
                if name == "info.json":
                    continue
                if name.startswith("a/"):
                    a_entries[name[2:]] = z.read(name)
                elif name.startswith("b/"):
                    b_entries[name[2:]] = z.read(name)
            return MtcrPack(info=info, a_entries=a_entries, b_entries=b_entries)
    except Exception as exc:
        print(f"[mtcr_apk_reference] ERROR reading {pack_path.name}: {exc}")
        return None


def inspect_reference_pack(ref_dir: Path) -> dict:
    """
    Inspect a MiuiSystemUI reference pack directory.

    Returns a summary dict covering:
      - presence and size of add/classes*.dex
      - count of add/ resource XML files by type
      - presence and entry counts for compare/dex.mtcr, xml.mtcr, arsc.mtcr
    """
    summary: dict = {
        "ref_dir": str(ref_dir),
        "ref_dir_exists": ref_dir.is_dir(),
        "add_dex": [],
        "add_resource_files": 0,
        "add_resource_types": {},
        "dex_mtcr": None,
        "xml_mtcr": None,
        "arsc_mtcr": None,
        "warnings": [],
        "errors": [],
    }

    if not ref_dir.is_dir():
        summary["errors"].append(f"Reference directory not found: {ref_dir}")
        return summary

    # add/ dex files
    add_dir = ref_dir / "add"
    for dex_name in ("classes2.dex", "classes3.dex", "classes4.dex"):
        dex_path = add_dir / dex_name
        exists = dex_path.is_file()
        summary["add_dex"].append({
            "name": dex_name,
            "exists": exists,
            "size": dex_path.stat().st_size if exists else 0,
            "path": str(dex_path),
        })

    # add/ resource XMLs by type
    res_dir = add_dir / "com.android.systemui"
    if res_dir.is_dir():
        for type_dir in sorted(res_dir.iterdir()):
            if type_dir.is_dir():
                count = sum(1 for f in type_dir.glob("*.xml"))
                summary["add_resource_types"][type_dir.name] = count
                summary["add_resource_files"] += count
    else:
        summary["warnings"].append("add/com.android.systemui/ directory not found")

    # compare/ MTCR packs
    compare_dir = ref_dir / "compare"
    for mtcr_name in ("dex.mtcr", "xml.mtcr", "arsc.mtcr"):
        key = mtcr_name.replace(".", "_")  # dex_mtcr, xml_mtcr, arsc_mtcr
        mtcr_path = compare_dir / mtcr_name
        if mtcr_path.is_file():
            pack = read_mtcr_pack(mtcr_path)
            if pack is not None:
                a_set = set(pack.a_entries)
                b_set = set(pack.b_entries)
                summary[key] = {
                    "path": str(mtcr_path),
                    "exists": True,
                    "info": pack.info,
                    "a_count": len(a_set),
                    "b_count": len(b_set),
                    "added_count": len(b_set - a_set),
                    "modified_count": len(a_set & b_set),
                }
            else:
                summary[key] = {
                    "path": str(mtcr_path),
                    "exists": True,
                    "error": "read failed",
                }
        else:
            summary[key] = {"path": str(mtcr_path), "exists": False}
            summary["warnings"].append(f"compare/{mtcr_name} not found")

    return summary
