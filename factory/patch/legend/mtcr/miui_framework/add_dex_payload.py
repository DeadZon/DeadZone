"""
Legend MTCR DEX addition rule: miui-framework.jar

Adds the MEZO payload DEX into miui-framework.jar during the MTCR rebuild pipeline.
The payload file is sourced from the canonical third_party asset directory.
"""
from __future__ import annotations

TARGET_JAR   = "miui-framework.jar"
TARGET_CLASS = ""    # DEX addition — no single class target

PATCHES = [
    {
        "id":           "add_dex_miui_framework_payload",
        "type":         "dex_add",
        "target_jar":   "miui-framework.jar",
        "payload_name": "miui-freamwork add.dex",
        "output_dex":   "classes_mezo.dex",
        "required":     False,
        "reason":       (
            "Legend MTCR add.dex payload for miui-framework.jar. "
            "Source: Legend/jar/miui-freamwork add.dex (typo in original filename preserved). "
            "Injected as an additional DEX before JAR repack."
        ),
    },
]
