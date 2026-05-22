"""
Legend MTCR patch - class-level rule.

Target JAR   : framework.jar
Target class : miui/util/VibrateReasonUtils
Source MTCR  : Framework_Legend.mtcr

This file is auto-generated from the MTCR archive.
The real logic lives here — not in the JAR-level patch_*.py wrappers.
"""
from __future__ import annotations

TARGET_JAR   = "framework.jar"
TARGET_CLASS = "miui/util/VibrateReasonUtils.smali"
CLASS_FALLBACK_NAMES = ['VibrateReasonUtils.smali']
CLASS_ANCHORS        = []

PATCHES = [
    {
        "id":          "add_class_miui_util_VibrateReasonUtils",
        "method":      "",
        "type":        "class_add",
        "search":      None,
        "replacement": """\
.class public Lmiui/util/VibrateReasonUtils;
.super Ljava/lang/Object;


# direct methods
.method private constructor <init>()V
    .registers 1

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method static vibrate(Landroid/os/SystemVibrator;ILjava/lang/String;Landroid/os/VibrationEffect;Ljava/lang/String;Landroid/media/AudioAttributes;)V
    .registers 6

    invoke-virtual/range {p0 .. p5}, Landroid/os/SystemVibrator;->vibrate(ILjava/lang/String;Landroid/os/VibrationEffect;Ljava/lang/String;Landroid/media/AudioAttributes;)V

    return-void
.end method

""",
        "required":    True,
        "reason":      "Legend MTCR new class from Framework_Legend.mtcr",
    },
]
