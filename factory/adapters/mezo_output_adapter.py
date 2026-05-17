from pathlib import Path
import shutil

from factory.core.paths import MEZO_CORE, REPO_ROOT

REQUIRED_IMAGES = [
    "boot.img",
    "init_boot.img",
    "vendor_boot.img",
    "vbmeta.img",
    "super.img",
]


def find_mezo_output() -> Path | None:
    candidates = sorted(
        [
            d for d in MEZO_CORE.glob("DeadZone_*")
            if d.is_dir() and (d / "images").exists()
        ],
        key=lambda d: d.stat().st_mtime,
        reverse=True,
    )
    return candidates[0] if candidates else None


def collect_output(build_id: str, output_root: Path = None) -> Path:
    if output_root is None:
        output_root = REPO_ROOT / "output" / "work"

    src = find_mezo_output()
    if src is None:
        raise RuntimeError(
            "No DeadZone_* output folder with images/ found under mezo_core"
        )

    dest_images = output_root / build_id / "images"
    dest_images.mkdir(parents=True, exist_ok=True)

    missing = []
    for img in REQUIRED_IMAGES:
        src_img = src / "images" / img
        if src_img.exists():
            shutil.copy2(src_img, dest_images / img)
            print(f"  [COPY] {img}")
        else:
            missing.append(img)

    if missing:
        print(f"[WARN] Missing images not found in MEZO output: {missing}")

    print(f"[ADAPTER] Output collected to: {dest_images}")
    return dest_images
