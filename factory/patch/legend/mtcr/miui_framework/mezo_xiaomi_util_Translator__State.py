"""
Legend MTCR patch - class-level rule.

Target JAR   : miui-framework.jar
Target class : mezo/xiaomi/util/Translator$State
Source MTCR  : miui-framework_Legend.mtcr

This file is auto-generated from the MTCR archive.
The real logic lives here — not in the JAR-level patch_*.py wrappers.
"""
from __future__ import annotations

TARGET_JAR   = "miui-framework.jar"
TARGET_CLASS = "mezo/xiaomi/util/Translator$State.smali"

PATCHES = [
    {
        "id":          "add_class_mezo_xiaomi_util_Translator__State",
        "method":      "",
        "type":        "class_add",
        "search":      None,
        "replacement": """\
.class Lmezo/xiaomi/util/Translator$State;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lmezo/xiaomi/util/Translator;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x8
    name = "State"
.end annotation


# instance fields
.field public final blacklist indexList:Ljava/util/List;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/List<",
            "Ljava/lang/Integer;",
            ">;"
        }
    .end annotation
.end field

.field public final blacklist textList:Ljava/util/List;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/List<",
            "Ljava/lang/String;",
            ">;"
        }
    .end annotation
.end field

.field public final blacklist textSet:Ljava/util/Set;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/Set<",
            "Ljava/lang/String;",
            ">;"
        }
    .end annotation
.end field


# direct methods
.method public constructor blacklist <init>()V
    .registers 2

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    new-instance v0, Ljava/util/HashSet;

    invoke-direct {v0}, Ljava/util/HashSet;-><init>()V

    iput-object v0, p0, Lmezo/xiaomi/util/Translator$State;->textSet:Ljava/util/Set;

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lmezo/xiaomi/util/Translator$State;->textList:Ljava/util/List;

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lmezo/xiaomi/util/Translator$State;->indexList:Ljava/util/List;

    return-void
.end method

""",
        "required":    True,
        "reason":      "Legend MTCR new class from miui-framework_Legend.mtcr",
    },
]
