from pathlib import Path
import yaml

from factory.core.paths import REGISTRY_ROOT

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


def _load(path: Path) -> dict | None:
    try:
        with path.open() as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"  [ERROR] Cannot parse {path}: {e}")
        return None


def validate_registry() -> bool:
    ok = True

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

    print("[4] Checking device files...")
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

    if ok:
        print("\n[PASS] Registry is valid.")
    else:
        print("\n[FAIL] Registry has errors — fix the issues listed above.")
    return ok
