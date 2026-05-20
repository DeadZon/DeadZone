"""
Legend MTCR patch - class-level rule.

Target JAR   : miui-framework.jar
Target class : com/android/internal/util/mezo/OOO0OO
Source MTCR  : miui-framework_Legend.mtcr

This file is auto-generated from the MTCR archive.
The real logic lives here — not in the JAR-level patch_*.py wrappers.
"""
from __future__ import annotations

TARGET_JAR   = "miui-framework.jar"
TARGET_CLASS = "com/android/internal/util/mezo/OOO0OO.smali"
CLASS_FALLBACK_NAMES = ['OOO0OO.smali']
CLASS_ANCHORS        = []

PATCHES = [
    {
        "id":          "add_class_com_android_internal_util_mezo_OOO0OO",
        "method":      "",
        "type":        "class_add",
        "search":      None,
        "replacement": """\
.class public abstract Lcom/android/internal/util/mezo/OOO0OO;
.super Ljava/lang/Object;


# direct methods
.method public static Oo00OO(J)J
    .registers 4

    const/16 v0, 0x21

    ushr-long v0, p0, v0

    xor-long/2addr p0, v0

    const-wide v0, 0x62a9d9ed799705f5L

    mul-long/2addr p0, v0

    const/16 v0, 0x1c

    ushr-long v0, p0, v0

    xor-long/2addr p0, v0

    const-wide v0, -0x34db2f5a3773ca4dL

    mul-long/2addr p0, v0

    const/16 v0, 0x20

    ushr-long/2addr p0, v0

    return-wide p0
.end method

.method public static OoOO0oo(J)J
    .registers 6

    const-wide/32 v0, 0xffff

    and-long v2, p0, v0

    long-to-int v2, v2

    int-to-short v2, v2

    const/16 v3, 0x10

    ushr-long/2addr p0, v3

    and-long/2addr p0, v0

    long-to-int p0, p0

    int-to-short p0, p0

    add-int p1, v2, p0

    int-to-short p1, p1

    const/16 v0, 0x9

    invoke-static {p1, v0}, Lcom/android/internal/util/mezo/OOO0OO;->o0OOOo00(SI)S

    move-result p1

    add-int/2addr p1, v2

    int-to-short p1, p1

    xor-int/2addr p0, v2

    int-to-short p0, p0

    const/16 v0, 0xd

    invoke-static {v2, v0}, Lcom/android/internal/util/mezo/OOO0OO;->o0OOOo00(SI)S

    move-result v0

    xor-int/2addr v0, p0

    int-to-short v0, v0

    shl-int/lit8 v1, p0, 0x5

    xor-int/2addr v0, v1

    int-to-short v0, v0

    const/16 v1, 0xa

    invoke-static {p0, v1}, Lcom/android/internal/util/mezo/OOO0OO;->o0OOOo00(SI)S

    move-result p0

    int-to-long v1, p1

    shl-long/2addr v1, v3

    int-to-long p0, p0

    or-long/2addr p0, v1

    shl-long/2addr p0, v3

    int-to-long v0, v0

    or-long/2addr p0, v0

    return-wide p0
.end method

.method public static o0OOOo00(SI)S
    .registers 3

    shl-int v0, p0, p1

    rsub-int/lit8 p1, p1, 0x20

    ushr-int/2addr p0, p1

    or-int/2addr p0, v0

    int-to-short p0, p0

    return p0
.end method

""",
        "required":    True,
        "reason":      "Legend MTCR new class from miui-framework_Legend.mtcr",
    },
]
