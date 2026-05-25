"""
Legend MTCR patch - class-level rule.

Target JAR   : miui-framework.jar
Target class : com/android/internal/util/mezo/o0OOOo00
Source MTCR  : miui-framework_Legend.mtcr

This file is auto-generated from the MTCR archive.
The real logic lives here — not in the JAR-level patch_*.py wrappers.
"""
from __future__ import annotations

TARGET_JAR   = "miui-framework.jar"
TARGET_CLASS = "com/android/internal/util/mezo/o0OOOo00.smali"
CLASS_FALLBACK_NAMES = ['o0OOOo00.smali']
CLASS_ANCHORS        = []

PATCHES = [
    {
        "id":          "add_class_com_android_internal_util_mezo_o0OOOo00",
        "method":      "",
        "type":        "class_add",
        "search":      None,
        "replacement": """\
.class public abstract Lcom/android/internal/util/mezo/o0OOOo00;
.super Ljava/lang/Object;


# direct methods
.method public static OoOO0oo(I[Ljava/lang/String;J)J
    .registers 5

    invoke-static {p2, p3}, Lcom/android/internal/util/mezo/OOO0OO;->OoOO0oo(J)J

    move-result-wide p2

    div-int/lit16 v0, p0, 0x1fff

    aget-object p1, p1, v0

    rem-int/lit16 p0, p0, 0x1fff

    invoke-virtual {p1, p0}, Ljava/lang/String;->charAt(I)C

    move-result p0

    int-to-long p0, p0

    const/16 v0, 0x20

    shl-long/2addr p0, v0

    xor-long/2addr p0, p2

    return-wide p0
.end method

.method public static o0OOOo00(J[Ljava/lang/String;)Ljava/lang/String;
    .registers 14

    const-wide v0, 0xffffffffL

    and-long/2addr v0, p0

    invoke-static {v0, v1}, Lcom/android/internal/util/mezo/OOO0OO;->Oo00OO(J)J

    move-result-wide v0

    invoke-static {v0, v1}, Lcom/android/internal/util/mezo/OOO0OO;->OoOO0oo(J)J

    move-result-wide v0

    const/16 v2, 0x20

    ushr-long v3, v0, v2

    const-wide/32 v5, 0xffff

    and-long/2addr v3, v5

    invoke-static {v0, v1}, Lcom/android/internal/util/mezo/OOO0OO;->OoOO0oo(J)J

    move-result-wide v0

    const/16 v7, 0x10

    ushr-long v7, v0, v7

    const-wide/32 v9, -0x10000

    and-long/2addr v7, v9

    ushr-long/2addr p0, v2

    xor-long/2addr p0, v3

    xor-long/2addr p0, v7

    long-to-int p0, p0

    invoke-static {p0, p2, v0, v1}, Lcom/android/internal/util/mezo/o0OOOo00;->OoOO0oo(I[Ljava/lang/String;J)J

    move-result-wide v0

    ushr-long v3, v0, v2

    and-long/2addr v3, v5

    long-to-int p1, v3

    new-array v3, p1, [C

    const/4 v4, 0x0

    :goto_0
    if-ge v4, p1, :cond_0

    add-int v7, p0, v4

    add-int/lit8 v7, v7, 0x1

    invoke-static {v7, p2, v0, v1}, Lcom/android/internal/util/mezo/o0OOOo00;->OoOO0oo(I[Ljava/lang/String;J)J

    move-result-wide v0

    ushr-long v7, v0, v2

    and-long/2addr v7, v5

    long-to-int v7, v7

    int-to-char v7, v7

    aput-char v7, v3, v4

    add-int/lit8 v4, v4, 0x1

    goto :goto_0

    :cond_0
    new-instance p0, Ljava/lang/String;

    invoke-direct {p0, v3}, Ljava/lang/String;-><init>([C)V

    return-object p0
.end method

""",
        "required":    True,
        "reason":      "Legend MTCR new class from miui-framework_Legend.mtcr",
    },
]
