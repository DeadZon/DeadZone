"""
Legend MTCR patch - class-level rule.

Target JAR   : miui-framework.jar
Target class : mezo/xiaomi/util/JSONTranslator-IA
Source MTCR  : miui-framework_Legend.mtcr

This file is auto-generated from the MTCR archive.
The real logic lives here — not in the JAR-level patch_*.py wrappers.
"""
from __future__ import annotations

TARGET_JAR   = "miui-framework.jar"
TARGET_CLASS = "mezo/xiaomi/util/JSONTranslator-IA.smali"

PATCHES = [
    {
        "id":          "add_class_mezo_xiaomi_util_JSONTranslator_dash_IA",
        "method":      "",
        "type":        "class_add",
        "search":      None,
        "replacement": """\
.class public final synthetic Lmezo/xiaomi/util/JSONTranslator-IA;
.super Ljava/lang/Object;

""",
        "required":    True,
        "reason":      "Legend MTCR new class from miui-framework_Legend.mtcr",
    },
]
