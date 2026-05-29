from __future__ import annotations

import re
import tarfile
import zipfile
from dataclasses import asdict, dataclass, field
from pathlib import Path
from urllib.parse import unquote, urlparse

from factory.core.workspace import Workspace, write_json

ROM_PAYLOAD = "payload_ota"
ROM_FASTBOOT_TGZ = "fastboot_tgz"
ROM_FASTBOOT_ZIP = "fastboot_zip"
ROM_EU = "xiaomi_eu_zip"
ROM_RAW_SUPER = "raw_super"
ROM_SPLIT_SUPER = "split_super"
ROM_NEW_DAT = "new_dat_br"
ROM_IMAGES = "images_folder"
ROM_UNKNOWN = "unknown"

REGION_CODES = {
    "CNXM": "CN",
    "MIXM": "Global",
    "EUXM": "EEA",
    "INXM": "India",
    "RUXM": "Russia",
    "TRXM": "Turkey",
    "IDXM": "Indonesia",
    "TWXM": "Taiwan",
}

DYNAMIC_PARTITIONS = {
    "system", "system_ext", "product", "vendor", "odm", "mi_ext",
    "vendor_dlkm", "system_dlkm", "odm_dlkm",
}


@dataclass
class RomInfo:
    source: str
    rom_type: str = ROM_UNKNOWN
    archive_type: str = "directory"
    codename: str = "unknown"
    android_version: str = "unknown"
    build: str = "unknown"
    region: str = "unknown"
    soc: str = "unknown"
    slot_mode: str = "unknown"
    filesystem: str = "unknown"
    has_payload: bool = False
    has_super: bool = False
    has_split_super: bool = False
    has_new_dat_br: bool = False
    super_rebuild_required: bool = False
    members: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def _members(path: Path) -> tuple[str, list[str]]:
    if path.is_dir():
        return "directory", [str(p.relative_to(path)) for p in path.rglob("*") if p.is_file()]
    if zipfile.is_zipfile(path):
        with zipfile.ZipFile(path) as zf:
            return "zip", zf.namelist()
    if tarfile.is_tarfile(path):
        with tarfile.open(path, "r:*") as tf:
            ext = path.suffixes[-2:] if len(path.suffixes) >= 2 else path.suffixes
            return "tgz" if ".gz" in ext or path.name.endswith((".tgz", ".tar.gz")) else "tar", tf.getnames()
    return "raw", [path.name]


def _parse_filename(source: str) -> dict[str, str]:
    name = Path(unquote(urlparse(str(source)).path)).name or Path(str(source)).name
    patterns = [
        re.compile(r"^(?P<codename>[a-z][a-z0-9]+)_images_(?P<build>(?:OS|V)[A-Z0-9.]+)_(?P<date>\d[\d.]*)_(?P<android>\d[\d.]*)_(?P<region>[a-z]+)_", re.I),
        re.compile(r"^(?P<codename>[a-z][a-z0-9]+)-ota(?:_full)?-(?P<build>(?:OS|V)[A-Z0-9.]+)-user-(?P<android>\d[\d.]*)-", re.I),
        re.compile(r"xiaomi\.eu_multi_(?P<codename>[a-z][a-z0-9]+)_(?P<build>(?:OS|V)[A-Z0-9.]+)_(?P<android>\d[\d.]*)", re.I),
    ]
    for pattern in patterns:
        m = pattern.search(name)
        if not m:
            continue
        build = m.groupdict().get("build", "")
        region_hint = m.groupdict().get("region", "")
        return {
            "codename": m.groupdict().get("codename", "").lower(),
            "build": build,
            "android_version": (m.groupdict().get("android") or "").split(".")[0],
            "region": _region_from_build(build, region_hint),
        }
    return {}


def _region_from_build(build: str, hint: str = "") -> str:
    if hint.lower() == "cn":
        return "CN"
    upper = build.upper()
    for suffix, region in REGION_CODES.items():
        if upper.endswith(suffix):
            return region
    return "unknown"


def _slot_mode(names: list[str]) -> str:
    lowers = [n.lower() for n in names]
    has_a = any(re.search(r"_(a)\.img$", n) or "/system_a." in n for n in lowers)
    has_b = any(re.search(r"_(b)\.img$", n) or "/system_b." in n for n in lowers)
    if any("virtual_ab" in n or "vab" in n for n in lowers) or (has_a and has_b):
        return "VAB"
    if has_a:
        return "A/B"
    return "A-only"


def _filesystem(names: list[str]) -> str:
    joined = "\n".join(names).lower()
    if "erofs" in joined or ".new.dat.br" in joined:
        return "EROFS"
    if "f2fs" in joined:
        return "F2FS"
    if any(n.lower().endswith(".img") for n in names):
        return "EXT4/EROFS"
    return "unknown"


def detect_rom(path: Path, ws: Workspace, soc: str = "unknown", custom_codename: str = "") -> RomInfo:
    archive_type, names = _members(path)
    lower = [n.lower() for n in names]
    info = RomInfo(source=str(path), archive_type=archive_type, members=names[:2000], soc=soc.upper())
    info.has_payload = any(n.endswith("payload.bin") for n in lower)
    info.has_super = path.name == "super.img" or any(n == "super.img" or n.endswith("/super.img") for n in lower)
    info.has_split_super = len([n for n in lower if re.search(r"super\.img\.\d+$", n)]) >= 2
    info.has_new_dat_br = any(n.endswith(".new.dat.br") for n in lower)
    has_images = any((n.startswith("images/") or "/images/" in n or n.endswith(".img")) for n in lower)
    is_eu = "xiaomi.eu" in path.name.lower() or any("xiaomi.eu" in n or "eu_multilang" in n for n in lower)

    if info.has_payload:
        info.rom_type = ROM_PAYLOAD
    elif archive_type in {"tgz", "tar"} and has_images:
        info.rom_type = ROM_FASTBOOT_TGZ
    elif archive_type == "zip" and has_images and any(n.startswith("images/") for n in lower):
        info.rom_type = ROM_FASTBOOT_ZIP
    elif is_eu:
        info.rom_type = ROM_EU
    elif path.name.lower() == "super.img" or info.has_super:
        info.rom_type = ROM_RAW_SUPER
    elif info.has_split_super:
        info.rom_type = ROM_SPLIT_SUPER
    elif info.has_new_dat_br:
        info.rom_type = ROM_NEW_DAT
    elif path.is_dir() and has_images:
        info.rom_type = ROM_IMAGES

    meta = _parse_filename(str(path))
    info.codename = custom_codename or meta.get("codename") or "unknown"
    info.android_version = meta.get("android_version") or "unknown"
    info.build = meta.get("build") or "unknown"
    info.region = meta.get("region") or "unknown"
    info.slot_mode = _slot_mode(names)
    info.filesystem = _filesystem(names)
    info.super_rebuild_required = info.rom_type in {ROM_PAYLOAD, ROM_NEW_DAT, ROM_IMAGES} or not info.has_super

    write_json(ws.meta / "rom_info.json", asdict(info))
    write_json(ws.meta / "device_info.json", {
        "codename": info.codename,
        "android_version": info.android_version,
        "build": info.build,
        "region": info.region,
        "soc": info.soc,
        "slot_mode": info.slot_mode,
        "filesystem": info.filesystem,
    })
    write_json(ws.meta / "super_layout.json", {
        "slot_mode": info.slot_mode,
        "filesystem": info.filesystem,
        "default_target_super_size": 8_500_000_000,
        "rebuild_required": info.super_rebuild_required,
        "vab_b_partitions_zero_size": info.slot_mode == "VAB",
    })
    write_json(ws.meta / "partition_map.json", {
        "dynamic_partitions": sorted(DYNAMIC_PARTITIONS),
        "source_images_seen": sorted(Path(n).name for n in names if n.lower().endswith(".img"))[:500],
    })
    print_detected(info)
    return info


def print_detected(info: RomInfo) -> None:
    print(f"[ROM] Type: {info.rom_type}")
    print(f"[DEVICE] Codename: {info.codename}")
    print(f"[ANDROID] Version: {info.android_version}")
    print(f"[BUILD] {info.build}")
    print(f"[REGION] {info.region}")
    print(f"[SOC] {info.soc}")
    print(f"[SLOT] {info.slot_mode}")
    print(f"[FS] {info.filesystem}")
    print(f"[SUPER] {'rebuild required' if info.super_rebuild_required else 'preserve original'}")
