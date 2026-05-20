"""
Legend MTCR patch - class-level rule.

Target JAR   : framework.jar
Target class : android/preference/CustomUpdater$CustomObjectTransmitter
Source MTCR  : Framework_Legend.mtcr

This file is auto-generated from the MTCR archive.
The real logic lives here — not in the JAR-level patch_*.py wrappers.
"""
from __future__ import annotations

TARGET_JAR   = "framework.jar"
TARGET_CLASS = "android/preference/CustomUpdater$CustomObjectTransmitter.smali"

PATCHES = [
    {
        "id":          "add_class_android_preference_CustomUpdater__CustomObjectTran",
        "method":      "",
        "type":        "class_add",
        "search":      None,
        "replacement": """\
.class public interface abstract Landroid/preference/CustomUpdater$CustomObjectTransmitter;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Landroid/preference/CustomUpdater;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x609
    name = "CustomObjectTransmitter"
.end annotation


# virtual methods
.method public abstract onObjectArrived(Ljava/lang/Object;)V
.end method

""",
        "required":    True,
        "reason":      "Legend MTCR new class from Framework_Legend.mtcr",
    },
]
