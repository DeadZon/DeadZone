"""
import_xiaomi_eu_devices.py

Reads Xiaomi EU source data from registry/devices/sources/ and merges new
devices into registry/devices/factory_devices.json.

Source files (under registry/devices/sources/):
  devices_data.txt  — allowed build codenames, one per line
  devices.json      — codename -> marketing display name

Rules:
  - devices_data.txt is the authoritative codename allowlist
  - Existing "deadzone" source entries are preserved as-is
  - New EU devices get: source=xiaomi_eu, support_level=metadata, enabled=true
  - SoC is resolved from the embedded SOC_MAP; unknown -> "auto"
  - Devices with TV/Box/Watch/Band/Router keywords in display_name are excluded
  - Output is sorted by codename, written as deterministic JSON
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent

SOURCES_DIR = REPO_ROOT / "registry" / "devices" / "sources"
DEVICES_DATA_TXT = SOURCES_DIR / "devices_data.txt"
DEVICES_JSON = SOURCES_DIR / "devices.json"
FACTORY_JSON = REPO_ROOT / "registry" / "devices" / "factory_devices.json"

# SoC mapping: codename -> "mtk" | "snapdragon"
# Omitted codenames fall back to "auto"
SOC_MAP: dict[str, str] = {
    # MTK
    "agate": "mtk",
    "aristotle": "mtk",
    "biloba": "mtk",
    "bomb": "mtk",
    "cannon": "mtk",
    "cezanne": "mtk",
    "corot": "mtk",
    "daumier": "mtk",
    "fleur": "mtk",
    "light": "mtk",
    "miel": "mtk",
    "mondeo": "mtk",
    "pantah": "mtk",
    "pissaro": "mtk",
    "plato": "mtk",
    "renoir": "mtk",
    "rubens": "mtk",
    "zircon": "mtk",
    # Snapdragon
    "alioth": "snapdragon",
    "amethyst": "snapdragon",
    "apollo": "snapdragon",
    "aurora": "snapdragon",
    "babylon": "snapdragon",
    "breeze": "snapdragon",
    "cas": "snapdragon",
    "chenfeng": "snapdragon",
    "cmi": "snapdragon",
    "cupid": "snapdragon",
    "curtana": "snapdragon",
    "dada": "snapdragon",
    "dagu": "snapdragon",
    "diting": "snapdragon",
    "dizi": "snapdragon",
    "elish": "snapdragon",
    "enuma": "snapdragon",
    "flame": "snapdragon",
    "fuxi": "snapdragon",
    "garnet": "snapdragon",
    "gauguin": "snapdragon",
    "goku": "snapdragon",
    "haotian": "snapdragon",
    "haydn": "snapdragon",
    "houji": "snapdragon",
    "ingres": "snapdragon",
    "ishtar": "snapdragon",
    "lisa": "snapdragon",
    "liuqin": "snapdragon",
    "lmi": "snapdragon",
    "marble": "snapdragon",
    "mayfly": "snapdragon",
    "miro": "snapdragon",
    "mondrian": "snapdragon",
    "moonstone": "snapdragon",
    "munch": "snapdragon",
    "muyu": "snapdragon",
    "myron": "snapdragon",
    "nabu": "snapdragon",
    "nezha": "snapdragon",
    "nuwa": "snapdragon",
    "odin": "snapdragon",
    "onyx": "snapdragon",
    "opal": "snapdragon",
    "pandora": "snapdragon",
    "peridot": "snapdragon",
    "peux": "snapdragon",
    "piano": "snapdragon",
    "pipa": "snapdragon",
    "psyche": "snapdragon",
    "pudding": "snapdragon",
    "redwood": "snapdragon",
    "ruan": "snapdragon",
    "sapphire": "snapdragon",
    "sapphiren": "snapdragon",
    "sheng": "snapdragon",
    "shennong": "snapdragon",
    "sky": "snapdragon",
    "socrates": "snapdragon",
    "star": "snapdragon",
    "sunstone": "snapdragon",
    "sweet": "snapdragon",
    "taoyao": "snapdragon",
    "tapas": "snapdragon",
    "thor": "snapdragon",
    "thyme": "snapdragon",
    "topaz": "snapdragon",
    "uke": "snapdragon",
    "umi": "snapdragon",
    "unicorn": "snapdragon",
    "venus": "snapdragon",
    "vermeer": "snapdragon",
    "vili": "snapdragon",
    "xuanyuan": "snapdragon",
    "xun": "snapdragon",
    "yudi": "snapdragon",
    "yupei": "snapdragon",
    "zeus": "snapdragon",
    "zijin": "snapdragon",
    "ziyi": "snapdragon",
    "zizhan": "snapdragon",
    "zorn": "snapdragon",
    "popsicle": "snapdragon",
}

_EXCLUDE_KEYWORDS = {"tv", "box", "watch", "band", "router"}


def _is_excluded(display_name: str) -> bool:
    lower = display_name.lower()
    return any(kw in lower.split() or kw in lower for kw in _EXCLUDE_KEYWORDS)


def load_source_data(
    data_txt: pathlib.Path,
    names_json: pathlib.Path,
) -> tuple[list[str], dict[str, str]]:
    if not data_txt.exists():
        print(f"[ERROR] devices_data.txt not found: {data_txt}", file=sys.stderr)
        sys.exit(1)
    if not names_json.exists():
        print(f"[ERROR] devices.json not found: {names_json}", file=sys.stderr)
        sys.exit(1)

    codenames = [
        line.strip()
        for line in data_txt.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    ]
    names: dict[str, str] = json.loads(names_json.read_text(encoding="utf-8"))
    return codenames, names


def load_existing(factory_json: pathlib.Path) -> list[dict]:
    if not factory_json.exists():
        return []
    return json.loads(factory_json.read_text(encoding="utf-8"))


def merge_devices(
    existing: list[dict],
    eu_codenames: list[str],
    eu_names: dict[str, str],
) -> list[dict]:
    existing_by_codename: dict[str, dict] = {d["codename"]: d for d in existing}
    result: dict[str, dict] = dict(existing_by_codename)

    added = 0
    skipped_existing = 0
    skipped_excluded = 0
    skipped_no_name = 0

    for codename in eu_codenames:
        if codename in result:
            skipped_existing += 1
            continue

        display_name = eu_names.get(codename, "")
        if not display_name:
            print(f"[WARN] No display name for {codename!r} — skipping.")
            skipped_no_name += 1
            continue

        if _is_excluded(display_name):
            print(f"[SKIP] Excluded device: {codename} ({display_name})")
            skipped_excluded += 1
            continue

        soc = SOC_MAP.get(codename, "auto")
        result[codename] = {
            "codename": codename,
            "display_name": display_name,
            "soc": soc,
            "source": "xiaomi_eu",
            "support_level": "metadata",
            "enabled": True,
        }
        added += 1

    print(f"[INFO] Preserved {skipped_existing} existing entries.")
    print(f"[INFO] Added {added} new EU devices.")
    if skipped_excluded:
        print(f"[INFO] Excluded {skipped_excluded} non-phone/tablet devices.")
    if skipped_no_name:
        print(f"[WARN] Skipped {skipped_no_name} devices with no display name.")

    return sorted(result.values(), key=lambda d: d["codename"])


def write_factory_json(devices: list[dict], path: pathlib.Path, dry_run: bool) -> None:
    output = json.dumps(devices, indent=2, ensure_ascii=False) + "\n"
    if dry_run:
        print(f"[DRY-RUN] Would write {len(devices)} devices to {path}")
        return
    path.write_text(output, encoding="utf-8")
    print(f"[OK] Wrote {len(devices)} devices to {path}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Import Xiaomi EU devices into factory_devices.json")
    parser.add_argument("--dry-run", action="store_true", help="Print changes without writing")
    parser.add_argument("--sources-dir", type=pathlib.Path, default=SOURCES_DIR)
    parser.add_argument("--output", type=pathlib.Path, default=FACTORY_JSON)
    args = parser.parse_args(argv)

    data_txt = args.sources_dir / "devices_data.txt"
    names_json = args.sources_dir / "devices.json"

    eu_codenames, eu_names = load_source_data(data_txt, names_json)
    print(f"[INFO] EU source: {len(eu_codenames)} codenames, {len(eu_names)} display names.")

    existing = load_existing(args.output)
    print(f"[INFO] Existing factory_devices.json: {len(existing)} entries.")

    merged = merge_devices(existing, eu_codenames, eu_names)
    write_factory_json(merged, args.output, dry_run=args.dry_run)

    print(f"[DONE] Total devices: {len(merged)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
