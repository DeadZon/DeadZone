"""
Legend MTCR patch - class-level rule.

Target JAR   : framework.jar
Target class : android/Utils/Shell$CommandResult
Source MTCR  : Framework_Legend.mtcr

This file is auto-generated from the MTCR archive.
The real logic lives here — not in the JAR-level patch_*.py wrappers.
"""
from __future__ import annotations

TARGET_JAR   = "framework.jar"
TARGET_CLASS = "android/Utils/Shell$CommandResult.smali"

PATCHES = [
    {
        "id":          "add_class_android_Utils_Shell__CommandResult",
        "method":      "",
        "type":        "class_add",
        "search":      None,
        "replacement": """\
.class public Landroid/Utils/Shell$CommandResult;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Landroid/Utils/Shell;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x9
    name = "CommandResult"
.end annotation


# instance fields
.field public errorMsg:Ljava/lang/String;

.field public result:I

.field public successMsg:Ljava/lang/String;


# direct methods
.method public constructor <init>(I)V
    .registers 2

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    iput p1, p0, Landroid/Utils/Shell$CommandResult;->result:I

    return-void
.end method

.method public constructor <init>(ILjava/lang/String;Ljava/lang/String;)V
    .registers 4

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    iput p1, p0, Landroid/Utils/Shell$CommandResult;->result:I

    iput-object p2, p0, Landroid/Utils/Shell$CommandResult;->successMsg:Ljava/lang/String;

    iput-object p3, p0, Landroid/Utils/Shell$CommandResult;->errorMsg:Ljava/lang/String;

    return-void
.end method

""",
        "required":    True,
        "reason":      "Legend MTCR new class from Framework_Legend.mtcr",
    },
]
