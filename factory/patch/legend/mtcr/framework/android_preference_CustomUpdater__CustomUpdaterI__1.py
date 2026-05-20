"""
Legend MTCR patch - class-level rule.

Target JAR   : framework.jar
Target class : android/preference/CustomUpdater$CustomUpdaterI$1
Source MTCR  : Framework_Legend.mtcr

This file is auto-generated from the MTCR archive.
The real logic lives here — not in the JAR-level patch_*.py wrappers.
"""
from __future__ import annotations

TARGET_JAR   = "framework.jar"
TARGET_CLASS = "android/preference/CustomUpdater$CustomUpdaterI$1.smali"

PATCHES = [
    {
        "id":          "add_class_android_preference_CustomUpdater__CustomUpdaterI__",
        "method":      "",
        "type":        "class_add",
        "search":      None,
        "replacement": """\
.class Landroid/preference/CustomUpdater$CustomUpdaterI$1;
.super Landroid/content/BroadcastReceiver;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Landroid/preference/CustomUpdater$CustomUpdaterI;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Landroid/preference/CustomUpdater$CustomUpdaterI;


# direct methods
.method constructor <init>(Landroid/preference/CustomUpdater$CustomUpdaterI;)V
    .registers 2

    iput-object p1, p0, Landroid/preference/CustomUpdater$CustomUpdaterI$1;->this$0:Landroid/preference/CustomUpdater$CustomUpdaterI;

    invoke-direct {p0}, Landroid/content/BroadcastReceiver;-><init>()V

    return-void
.end method


# virtual methods
.method public onReceive(Landroid/content/Context;Landroid/content/Intent;)V
    .registers 6

    invoke-virtual {p2}, Landroid/content/Intent;->getAction()Ljava/lang/String;

    move-result-object v0

    if-eqz v0, :cond_0

    const-string v1, "my.settings.intent."

    const-string v2, ""

    invoke-virtual {v0, v1, v2}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;

    move-result-object v0

    const-string v1, ".CHANGE"

    const-string v2, ""

    invoke-virtual {v0, v1, v2}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;

    move-result-object v0

    iget-object v1, p0, Landroid/preference/CustomUpdater$CustomUpdaterI$1;->this$0:Landroid/preference/CustomUpdater$CustomUpdaterI;

    invoke-static {v1, v0}, Landroid/preference/CustomUpdater$CustomUpdaterI;->access$000(Landroid/preference/CustomUpdater$CustomUpdaterI;Ljava/lang/String;)V

    :cond_0
    return-void
.end method

""",
        "required":    True,
        "reason":      "Legend MTCR new class from Framework_Legend.mtcr",
    },
]
