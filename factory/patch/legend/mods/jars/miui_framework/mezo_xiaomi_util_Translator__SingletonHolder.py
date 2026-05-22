"""
Legend MTCR patch - class-level rule.

Target JAR   : miui-framework.jar
Target class : mezo/xiaomi/util/Translator$SingletonHolder
Source MTCR  : miui-framework_Legend.mtcr

This file is auto-generated from the MTCR archive.
The real logic lives here — not in the JAR-level patch_*.py wrappers.
"""
from __future__ import annotations

TARGET_JAR   = "miui-framework.jar"
TARGET_CLASS = "mezo/xiaomi/util/Translator$SingletonHolder.smali"
CLASS_FALLBACK_NAMES = ['Translator$SingletonHolder.smali']
CLASS_ANCHORS        = []

PATCHES = [
    {
        "id":          "add_class_mezo_xiaomi_util_Translator__SingletonHolder",
        "method":      "",
        "type":        "class_add",
        "search":      None,
        "replacement": """\
.class final Lmezo/xiaomi/util/Translator$SingletonHolder;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lmezo/xiaomi/util/Translator;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x1a
    name = "SingletonHolder"
.end annotation


# static fields
.field private static final blacklist INSTANCE:Lmezo/xiaomi/util/Translator;


# direct methods
.method static bridge synthetic blacklist -$$Nest$sfgetINSTANCE()Lmezo/xiaomi/util/Translator;
    .registers 1

    sget-object v0, Lmezo/xiaomi/util/Translator$SingletonHolder;->INSTANCE:Lmezo/xiaomi/util/Translator;

    return-object v0
.end method

.method static constructor blacklist <clinit>()V
    .registers 2

    new-instance v0, Lmezo/xiaomi/util/Translator;

    const/4 v1, 0x0

    invoke-direct {v0, v1}, Lmezo/xiaomi/util/Translator;-><init>(Lmezo/xiaomi/util/Translator-IA;)V

    sput-object v0, Lmezo/xiaomi/util/Translator$SingletonHolder;->INSTANCE:Lmezo/xiaomi/util/Translator;

    return-void
.end method

.method private constructor blacklist <init>()V
    .registers 1

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

""",
        "required":    True,
        "reason":      "Legend MTCR new class from miui-framework_Legend.mtcr",
    },
]
