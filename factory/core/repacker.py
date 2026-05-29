from __future__ import annotations

import shutil

from factory.core.workspace import Workspace, write_json

DYNAMIC_IMAGES = {
    "system.img", "product.img", "vendor.img", "odm.img", "mi_ext.img",
    "system_ext.img", "vendor_dlkm.img", "system_dlkm.img", "odm_dlkm.img",
}


def repack_partitions(ws: Workspace) -> dict:
    # Placeholder for filesystem-aware repack after styles mutate mounted partitions.
    # Existing .img files are already normalized in workspace/images.
    staged = []
    for img in ws.images.glob("*.img"):
        if img.name in DYNAMIC_IMAGES:
            target = ws.partitions / img.name
            if img.resolve() != target.resolve():
                shutil.copy2(img, target)
            staged.append(img.name)
    result = {"status": "OK", "dynamic_images_staged": sorted(staged)}
    write_json(ws.meta / "repack_result.json", result)
    print(f"[REPACK] Dynamic images staged: {len(staged)}")
    return result
