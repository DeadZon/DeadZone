from pathlib import Path
import yaml

from factory.core.paths import REGISTRY_ROOT, MEZO_CORE

SUPERCONFIG_ROOT = MEZO_CORE / "SuperConfig"

EXPECTED_SOCS = ["snapdragon", "mtk"]

EXPECTED_PLATFORMS = [
    "miui_a13",
    "os1_a13",
    "os1_a14",
    "os2_a14",
    "os2_a15",
    "os3_a15",
    "os3_a16",
]

EXPECTED_FLAVORS = [
    "deadzone",
    "deadzone_gaming",
    "deadzone_epic",
    "deadzone_legend",
]

GOLDEN_DEVICES = {
    "snapdragon": ["garnet"],
    "mtk": ["zircon"],
}

REQUIRED_IMAGES = [
    "boot.img",
    "init_boot.img",
    "vendor_boot.img",
    "vbmeta.img",
    "super.img",
]

REQUIRED_ENTRY_FIELDS = ["codename", "name", "choice", "source", "status"]


def _load(path: Path) -> dict | None:
    try:
        with path.open() as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"  [ERROR] Cannot parse {path}: {e}")
        return None


def validate_registry() -> bool:
    ok = True

    # ── [1] SOC files ──────────────────────────────────────────────────────────
    print("[1] Checking SOC files...")
    for soc in EXPECTED_SOCS:
        p = REGISTRY_ROOT / "soc" / f"{soc}.yml"
        if not p.exists():
            print(f"  [FAIL] Missing: {p}")
            ok = False
        else:
            data = _load(p)
            if data is None:
                ok = False
            else:
                print(f"  [OK] {p.name}")

    # ── [2] Platform files ────────────────────────────────────────────────────
    print("[2] Checking platform files...")
    for plat in EXPECTED_PLATFORMS:
        p = REGISTRY_ROOT / "platforms" / f"{plat}.yml"
        if not p.exists():
            print(f"  [FAIL] Missing: {p}")
            ok = False
        else:
            data = _load(p)
            if data is None:
                ok = False
            else:
                print(f"  [OK] {p.name}")

    # ── [3] Flavor files ──────────────────────────────────────────────────────
    print("[3] Checking flavor files...")
    for flavor in EXPECTED_FLAVORS:
        p = REGISTRY_ROOT / "flavors" / f"{flavor}.yml"
        if not p.exists():
            print(f"  [FAIL] Missing: {p}")
            ok = False
        else:
            data = _load(p)
            if data is None:
                ok = False
            else:
                print(f"  [OK] {p.name}")

    # ── [4] Golden device registry files ─────────────────────────────────────
    print("[4] Checking golden device files...")
    valid_socs = set(EXPECTED_SOCS)
    for soc_track, devices in GOLDEN_DEVICES.items():
        for dev in devices:
            p = REGISTRY_ROOT / "devices" / soc_track / f"{dev}.yml"
            if not p.exists():
                print(f"  [FAIL] Missing: {p}")
                ok = False
                continue
            data = _load(p)
            if data is None:
                ok = False
                continue
            dev_soc = data.get("soc")
            if dev_soc not in valid_socs:
                print(f"  [FAIL] {dev}.yml has invalid soc: '{dev_soc}'")
                ok = False
            else:
                print(f"  [OK] {p.name} -> soc:{dev_soc}")
            req_imgs = data.get("required_images", [])
            missing = [img for img in REQUIRED_IMAGES if img not in req_imgs]
            if missing:
                print(f"  [FAIL] {dev}.yml missing required_images: {missing}")
                ok = False
            else:
                print(f"  [OK] {p.name} -> required_images: complete")

    # ── [5] Device groups: structure, paths, registry_file references ─────────
    print("[5] Checking device_groups files...")
    LIVE_STATUSES = {"golden", "ready"}
    all_grouped: dict[str, str] = {}  # codename -> group_name

    for group_name in ["snapdragon", "mtk"]:
        gp = REGISTRY_ROOT / "device_groups" / f"{group_name}.yml"
        if not gp.exists():
            print(f"  [FAIL] device_groups/{group_name}.yml missing")
            ok = False
            continue
        gdata = _load(gp)
        if gdata is None:
            ok = False
            continue
        print(f"  [OK] device_groups/{group_name}.yml")
        group_soc = gdata.get("soc", "")

        for entry in gdata.get("devices", []):
            codename = entry.get("codename", "?")

            # Required fields
            missing_fields = [f for f in REQUIRED_ENTRY_FIELDS if f not in entry]
            if missing_fields:
                print(f"  [FAIL] {codename}: missing fields: {missing_fields}")
                ok = False

            # Duplicate across groups
            if codename in all_grouped:
                print(
                    f"  [FAIL] {codename}: duplicate — appears in both "
                    f"'{all_grouped[codename]}' and '{group_name}'"
                )
                ok = False
            else:
                all_grouped[codename] = group_name

            status = entry.get("status", "unknown")
            if status not in LIVE_STATUSES:
                continue  # todo/unknown entries are not validated further

            # source_path must exist for superconfig devices
            source = entry.get("source", "")
            source_path = entry.get("source_path")
            if source == "superconfig":
                if not source_path:
                    print(f"  [FAIL] {codename}: source=superconfig but source_path is null")
                    ok = False
                else:
                    sp = REGISTRY_ROOT.parent / source_path
                    if not sp.exists():
                        print(f"  [FAIL] {codename}: source_path not found: {source_path}")
                        ok = False

            # registry_file (if not null) must exist
            reg_file = entry.get("registry_file")
            if reg_file:
                reg_path = REGISTRY_ROOT.parent / reg_file
                if not reg_path.exists():
                    print(f"  [FAIL] {codename}: registry_file not found: {reg_file}")
                    ok = False

    # Count per group for summary
    sd_count = sum(1 for g in all_grouped.values() if g == "snapdragon")
    mtk_count = sum(1 for g in all_grouped.values() if g == "mtk")
    print(f"  [INFO] Grouped: {sd_count} Snapdragon, {mtk_count} MTK, {len(all_grouped)} total")

    # ── [6] SuperConfig coverage: every folder must be in exactly one group ───
    print("[6] Checking SuperConfig coverage...")
    if not SUPERCONFIG_ROOT.exists():
        print(f"  [WARN] SuperConfig root not found: {SUPERCONFIG_ROOT} — skipping coverage check")
    else:
        sc_codenames = {d.name for d in SUPERCONFIG_ROOT.iterdir() if d.is_dir()}
        ungrouped = sc_codenames - set(all_grouped.keys())
        if ungrouped:
            for c in sorted(ungrouped):
                print(f"  [FAIL] {c}: in SuperConfig but not assigned to any panel group")
            ok = False
        else:
            print(f"  [OK] All {len(sc_codenames)} SuperConfig devices are assigned to a panel")

    if ok:
        print("\n[PASS] Registry is valid.")
    else:
        print("\n[FAIL] Registry has errors — fix the issues listed above.")
    return ok
