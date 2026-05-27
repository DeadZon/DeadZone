"""Parse Xiaomi ROM filename metadata for DeadZone Factory.

Used as a fallback when build.prop metadata cannot be extracted from the ROM archive.
Supports common Xiaomi fastboot TGZ and OTA ZIP filename patterns.

Supported patterns
------------------
A) Fastboot TGZ:
   zorn_images_OS3.0.303.0.WOKCNXM_20260425.0000.00_16.0_cn_e6cf5ef711.tgz
   garnet_images_OS3.0.304.0.WNRCNXM_20260428.0000.00_16.0_cn_xxxxx.tgz

B) OTA ZIP:
   zircon-ota_full-OS3.0.303.0.WNOCNXM-user-16.0-09c35a83d6.zip
"""
from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote, urlparse


# Region suffix → 2-letter code used in intake reports
_REGION_CODES: dict[str, str] = {
    "CNXM": "CN",
    "MIXM": "Global",
    "EUXM": "EEA",
    "INXM": "India",
    "RUXM": "Russia",
    "TRXM": "Turkey",
    "IDXM": "Indonesia",
    "TWXM": "Taiwan",
}

# Fastboot TGZ / TAR.GZ:
# <codename>_images_<build_incremental>_<build_date>_<android>_<region_suffix>_<hash>.tgz
_FASTBOOT_RE = re.compile(
    r"^(?P<codename>[a-z][a-z0-9]+)_images_"
    r"(?P<build_incremental>(?:OS|V)\d[a-zA-Z0-9.]+)"
    r"_(?P<build_date>\d{8}[\d.]*)"
    r"_(?P<android_version>\d[\d.]*)"
    r"_(?P<region_suffix>[a-z]+)"
    r"_[0-9a-f]+\.tgz$",
    re.IGNORECASE,
)

# OTA ZIP:
# <codename>-ota[_full]-<build_incremental>-user-<android>-<hash>.zip
_OTA_RE = re.compile(
    r"^(?P<codename>[a-z][a-z0-9]+)-ota(?:_full)?-"
    r"(?P<build_incremental>(?:OS|V)\d[a-zA-Z0-9.]+)"
    r"-user-"
    r"(?P<android_version>\d[\d.]*)"
    r"-[0-9a-f]+\.zip$",
    re.IGNORECASE,
)


def _detect_region(build_incremental: str, region_suffix: str = "") -> str:
    """Return region code from region_suffix or build_incremental tail."""
    if region_suffix.lower() == "cn":
        return "CN"
    inc_upper = build_incremental.upper()
    for code, region in _REGION_CODES.items():
        if inc_upper.endswith(code):
            return region
    suffix_upper = region_suffix.upper()
    for code, region in _REGION_CODES.items():
        if suffix_upper == code or suffix_upper.endswith(code):
            return region
    return ""


def _detect_os(build_incremental: str) -> tuple[str, str, str]:
    """Return (os_family, os_major, os_name) from build_incremental prefix."""
    inc_upper = build_incremental.upper()
    m = re.match(r"^OS(\d+)", inc_upper)
    if m:
        major = m.group(1)
        return "HyperOS", major, f"HyperOS {major}"
    m2 = re.search(r"MIUI(\d+)", inc_upper)
    if m2:
        major = m2.group(1)
        return "MIUI", major, f"MIUI {major}"
    m3 = re.match(r"^V(\d+)", inc_upper)
    if m3:
        major = m3.group(1)
        return "MIUI", major, f"MIUI {major}"
    return "", "", ""


def parse_xiaomi_rom_metadata(path_or_name: str) -> dict:
    """Parse a Xiaomi ROM filename and return metadata dict.

    Returns a dict with keys:
        codename, build_incremental, android_version, region,
        os_family, os_major, os_name, build_date

    Returns an empty dict when the filename does not match any known pattern.
    """
    name = Path(path_or_name).name

    m = _FASTBOOT_RE.match(name)
    if m:
        codename = m.group("codename").lower()
        build_inc = m.group("build_incremental")
        android_ver = m.group("android_version")
        build_date = m.group("build_date")
        region_suffix = m.group("region_suffix")
        region = _detect_region(build_inc, region_suffix)
        os_family, os_major, os_name = _detect_os(build_inc)
        return {
            "codename": codename,
            "build_incremental": build_inc,
            "android_version": android_ver,
            "region": region,
            "os_family": os_family,
            "os_major": os_major,
            "os_name": os_name,
            "build_date": build_date,
        }

    m = _OTA_RE.match(name)
    if m:
        codename = m.group("codename").lower()
        build_inc = m.group("build_incremental")
        android_ver = m.group("android_version")
        region = _detect_region(build_inc, "")
        os_family, os_major, os_name = _detect_os(build_inc)
        return {
            "codename": codename,
            "build_incremental": build_inc,
            "android_version": android_ver,
            "region": region,
            "os_family": os_family,
            "os_major": os_major,
            "os_name": os_name,
            "build_date": "",
        }

    return {}


def _basename_from_source(source: str) -> tuple[str, str]:
    text = str(source or "").strip()
    if not text:
        return "", ""
    parsed = urlparse(text)
    if parsed.scheme and parsed.netloc:
        name = Path(unquote(parsed.path)).name
        return name, "rom_url_filename"
    return Path(text).name, "local_filename"


def parse_xiaomi_rom_metadata_from_sources(*sources: str) -> dict:
    """Parse Xiaomi metadata from multiple names/paths/URLs.

    Sources are tried in order. Non-empty values from earlier useful sources win;
    later sources fill only missing fields. URLs are parsed by path basename.
    """
    merged: dict = {}
    attempted: list[str] = []
    useful_sources: list[str] = []

    for source in sources:
        name, label = _basename_from_source(str(source or ""))
        if not name:
            continue
        attempted.append(name)
        parsed = parse_xiaomi_rom_metadata(name)
        if not parsed:
            continue
        added = False
        for key, value in parsed.items():
            if value and not merged.get(key):
                merged[key] = value
                added = True
        if added:
            useful_sources.append(label)

    if merged:
        merged["metadata_source"] = useful_sources[0] if useful_sources else "unknown"
        merged["metadata_sources_attempted"] = attempted
    return merged
