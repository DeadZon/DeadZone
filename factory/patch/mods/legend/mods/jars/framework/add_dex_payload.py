"""
Legend MTCR DEX addition rule: framework.jar

Adds the MEZO payload DEX into framework.jar during the MTCR rebuild pipeline.
The payload file is sourced from the canonical third_party asset directory.
"""
from __future__ import annotations

TARGET_JAR   = "framework.jar"
TARGET_CLASS = ""    # DEX addition — no single class target

PATCHES = [
    {
        "id":           "add_dex_framework_payload",
        "type":         "dex_add",
        "target_jar":   "framework.jar",
        "payload_name": "freamwork add.dex",
        "output_dex":   "classes_mezo.dex",
        "required":     False,
        "reason":       (
            "Legend MTCR add.dex payload for framework.jar. "
            "Source: factory/patch/legend/assets/jar/freamwork add.dex (typo in original filename preserved). "
            "Injected as an additional DEX before JAR repack."
        ),
    },
]
