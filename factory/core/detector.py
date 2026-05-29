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
    needs_super_rebuild: bool = False
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


def _read_member_text(path: Path, member: str, limit: int = 256_000) -> str:
    try:
        if path.is_dir():
            target = path / member
            if target.is_file() and target.stat().st_size <= limit:
                return target.read_text(encoding="utf-8", errors="ignore")
        elif zipfile.is_zipfile(path):
            with zipfile.ZipFile(path) as zf:
                info = zf.getinfo(member)
                if info.file_size <= limit:
                    return zf.read(member).decode("utf-8", errors="ignore")
        elif tarfile.is_tarfile(path):
            with tarfile.open(path, "r:*") as tf:
                extracted = tf.extractfile(member)
                if extracted:
                    return extracted.read(limit).decode("utf-8", errors="ignore")
    except Exception:
        return ""
    return ""


def _parse_props(text: str) -> dict[str, str]:
    props: dict[str, str] = {}
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        props[key.strip()] = value.strip()
    return props


def _build_prop_metadata(path: Path, names: list[str]) -> dict[str, str]:
    prop_names = [
        n for n in names
        if Path(n).name == "build.prop" and any(part in n.lower() for part in ("system", "product", "vendor", "odm"))
    ]
    props: dict[str, str] = {}
    for name in sorted(prop_names, key=lambda n: ("/system/" not in f"/{n.lower()}", n.count("/"))):
        found = _parse_props(_read_member_text(path, name))
        for key, value in found.items():
            props.setdefault(key, value)

    codename = (
        props.get("ro.product.odm.device")
        or props.get("ro.product.vendor.device")
        or props.get("ro.product.product.device")
        or props.get("ro.product.system.device")
        or props.get("ro.product.device")
        or ""
    )
    android = (
        props.get("ro.system.build.version.release")
        or props.get("ro.build.version.release")
        or props.get("ro.vendor.build.version.release")
        or ""
    )
    build = (
        props.get("ro.mi.os.version.incremental")
        or props.get("ro.build.version.incremental")
        or props.get("ro.system.build.version.incremental")
        or ""
    )
    return {
        "codename": codename.lower(),
        "android_version": android,
        "build": build,
        "region": _region_from_build(build),
    }


def _payload_metadata(path: Path, names: list[str]) -> dict[str, str]:
    for name in names:
        if Path(name).name != "payload_properties.txt":
            continue
        props = _parse_props(_read_member_text(path, name))
        build = props.get("FILE_HASH") or ""
        post_build = props.get("POST_BUILD") or props.get("POST_BUILD_INCREMENTAL") or ""
        codename = ""
        android = ""
        if "/" in post_build:
            parts = post_build.split("/")
            if len(parts) > 1:
                codename = parts[1].lower()
            if len(parts) > 2 and ":" in parts[2]:
                android = parts[2].split(":", 1)[1]
        return {
            "codename": codename,
            "android_version": android or (props.get("POST_SECURITY_PATCH", "")[:4] if props.get("POST_SECURITY_PATCH") else ""),
            "build": post_build or build,
            "region": _region_from_build(post_build),
        }
    return {}


def _parse_filename(source: str) -> dict[str, str]:
    name = Path(unquote(urlparse(str(source)).path)).name or Path(str(source)).name
    patterns = [
        re.compile(r"^(?P<codename>[a-z][a-z0-9]+)_images_(?P<build>(?:OS|V)[A-Z0-9.]+)_(?P<date>\d[\d.]*)_(?P<android>\d[\d.]*)_(?P<region>[a-z]+)(?:_|\.|$)", re.I),
        re.compile(r"^(?P<codename>[a-z][a-z0-9]+)-ota(?:_full)?-(?P<build>(?:OS|V)[A-Z0-9.]+)-user-(?P<android>\d[\d.]*)-", re.I),
        re.compile(r"xiaomi\.eu_multi_(?P<codename>[a-z][a-z0-9]+)_(?P<build>(?:OS|V)[A-Z0-9.]+)_(?P<android>\d[\d.]*)", re.I),
        re.compile(r"^(?P<codename>[a-z][a-z0-9]+)_(?P<build>(?:OS|V)[A-Z0-9.]+)_(?P<android>\d[\d.]*)", re.I),
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
        if upper.endswith(suffix) or suffix in upper:
            return region
    return "unknown"


def _slot_mode(names: list[str]) -> str:
    lowers = [n.lower() for n in names]
    joined = "\n".join(lowers)
    has_a = any(re.search(r"_(a)\.(img|new\.dat\.br|transfer\.list)$", n) or "/system_a." in n for n in lowers)
    has_b = any(re.search(r"_(b)\.(img|new\.dat\.br|transfer\.list)$", n) or "/system_b." in n for n in lowers)
    if "virtual_ab" in joined or "virtual-a/b" in joined or "vab" in joined or (has_a and has_b):
        return "VAB"
    if has_a:
        return "A/B"
    return "A-only"


def _filesystem(names: list[str]) -> str:
    joined = "\n".join(names).lower()
    if "erofs" in joined:
        return "EROFS"
    if ".new.dat.br" in joined:
        return "EXT4/EROFS"
    if "f2fs" in joined:
        return "F2FS"
    if any(n.lower().endswith(".img") for n in names):
        return "EXT4/EROFS"
    return "unknown"


def _partition_map(names: list[str]) -> dict[str, str]:
    result: dict[str, str] = {}
    for name in names:
        path = Path(name)
        lower = path.name.lower()
        if lower.endswith(".img"):
            part = path.stem.removesuffix("_a").removesuffix("_b")
            result[part] = name
        elif lower.endswith(".new.dat.br"):
            part = lower[: -len(".new.dat.br")].removesuffix("_a").removesuffix("_b")
            result[part] = name
    return dict(sorted(result.items()))


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

    if is_eu:
        info.rom_type = ROM_EU
    elif info.has_payload:
        info.rom_type = ROM_PAYLOAD
    elif archive_type in {"tgz", "tar"} and has_images:
        info.rom_type = ROM_FASTBOOT_TGZ
    elif archive_type == "zip" and has_images and any(n.startswith("images/") or "/images/" in n for n in lower):
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

    filename_meta = _parse_filename(str(path))
    prop_meta = _build_prop_metadata(path, names)
    payload_meta = _payload_metadata(path, names)
    meta = {**filename_meta}
    for source_meta in (payload_meta, prop_meta):
        for key, value in source_meta.items():
            if value and (not meta.get(key) or meta.get(key) == "unknown"):
                meta[key] = value

    info.codename = custom_codename or meta.get("codename") or "unknown"
    info.android_version = meta.get("android_version") or "unknown"
    info.build = meta.get("build") or "unknown"
    info.region = meta.get("region") or _region_from_build(info.build) or "unknown"
    info.slot_mode = _slot_mode(names)
    info.filesystem = _filesystem(names)
    info.needs_super_rebuild = info.rom_type in {ROM_PAYLOAD, ROM_NEW_DAT, ROM_IMAGES} or not info.has_super
    info.super_rebuild_required = info.needs_super_rebuild

    write_json(ws.meta / "rom_info.json", asdict(info))
    write_json(ws.meta / "device_info.json", {
        "codename": info.codename,
        "android_version": info.android_version,
        "build": info.build,
        "region": info.region,
        "soc": info.soc,
        "slot_mode": info.slot_mode,
        "filesystem": info.filesystem,
        "has_payload": info.has_payload,
        "has_super": info.has_super,
        "needs_super_rebuild": info.needs_super_rebuild,
    })
    write_json(ws.meta / "super_layout.json", {
        "slot_mode": info.slot_mode,
        "filesystem": info.filesystem,
        "has_super": info.has_super,
        "has_split_super": info.has_split_super,
        "default_target_super_size": 8_500_000_000,
        "needs_super_rebuild": info.needs_super_rebuild,
        "rebuild_required": info.super_rebuild_required,
        "vab_b_partitions_zero_size": info.slot_mode == "VAB",
    })
    write_json(ws.meta / "partition_map.json", {
        "dynamic_partitions": sorted(DYNAMIC_PARTITIONS),
        "by_partition": _partition_map(names),
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
