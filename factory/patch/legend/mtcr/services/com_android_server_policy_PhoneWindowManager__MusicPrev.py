"""
Legend MTCR patch - class-level rule.

Target JAR   : services.jar
Target class : com/android/server/policy/PhoneWindowManager$MusicPrev
Source MTCR  : Service_Legend.mtcr

This file is auto-generated from the MTCR archive.
The real logic lives here — not in the JAR-level patch_*.py wrappers.
"""
from __future__ import annotations

TARGET_JAR   = "services.jar"
TARGET_CLASS = "com/android/server/policy/PhoneWindowManager$MusicPrev.smali"

PATCHES = [
    {
        "id":          "add_class_com_android_server_policy_PhoneWindowManager__Musi",
        "method":      "",
        "type":        "class_add",
        "search":      None,
        "replacement": """\
.class public Lcom/android/server/policy/PhoneWindowManager$MusicPrev;
.super Ljava/lang/Object;

# interfaces
.implements Ljava/lang/Runnable;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/server/policy/PhoneWindowManager;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x1
    name = "MusicPrev"
.end annotation


# instance fields
.field final synthetic this$0:Lcom/android/server/policy/PhoneWindowManager;


# direct methods
.method public constructor <init>(Lcom/android/server/policy/PhoneWindowManager;)V
    .registers 2

    iput-object p1, p0, Lcom/android/server/policy/PhoneWindowManager$MusicPrev;->this$0:Lcom/android/server/policy/PhoneWindowManager;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public run()V
    .registers 3

    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager$MusicPrev;->this$0:Lcom/android/server/policy/PhoneWindowManager;

    sget v1, Lcom/android/server/policy/VolBtnHelper;->mVolBtnVolDown:I

    invoke-virtual {v0, v1}, Lcom/android/server/policy/PhoneWindowManager;->sendMediaButtonEvent(I)V

    const/4 v0, 0x1

    sput-boolean v0, Lcom/android/server/policy/VolBtnHelper;->mIsVolLongPressed:Z

    return-void
.end method

""",
        "required":    True,
        "reason":      "Legend MTCR new class from Service_Legend.mtcr",
    },
]
