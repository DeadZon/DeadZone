"""
Legend MTCR patch - class-level rule.

Target JAR   : framework.jar
Target class : android/preference/CustomUpdater
Source MTCR  : Framework_Legend.mtcr

This file is auto-generated from the MTCR archive.
The real logic lives here — not in the JAR-level patch_*.py wrappers.
"""
from __future__ import annotations

TARGET_JAR   = "framework.jar"
TARGET_CLASS = "android/preference/CustomUpdater.smali"

PATCHES = [
    {
        "id":          "add_class_android_preference_CustomUpdater",
        "method":      "",
        "type":        "class_add",
        "search":      None,
        "replacement": """\
.class public abstract Landroid/preference/CustomUpdater;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Landroid/preference/CustomUpdater$CustomUpdaterI;,
        Landroid/preference/CustomUpdater$CustomObjectTransmitter;,
        Landroid/preference/CustomUpdater$CustomReceiver;
    }
.end annotation


# static fields
.field private static customUpdater:Landroid/preference/CustomUpdater;


# direct methods
.method public constructor <init>()V
    .registers 1

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method public static getInstance()Landroid/preference/CustomUpdater;
    .registers 1

    sget-object v0, Landroid/preference/CustomUpdater;->customUpdater:Landroid/preference/CustomUpdater;

    if-nez v0, :cond_0

    new-instance v0, Landroid/preference/CustomUpdater$CustomUpdaterI;

    invoke-direct {v0}, Landroid/preference/CustomUpdater$CustomUpdaterI;-><init>()V

    sput-object v0, Landroid/preference/CustomUpdater;->customUpdater:Landroid/preference/CustomUpdater;

    :cond_0
    sget-object v0, Landroid/preference/CustomUpdater;->customUpdater:Landroid/preference/CustomUpdater;

    return-object v0
.end method


# virtual methods
.method public abstract addCustomObjectTransmitter(Landroid/preference/CustomUpdater$CustomObjectTransmitter;)V
.end method

.method public abstract addCustomReceiver(Landroid/preference/CustomUpdater$CustomReceiver;Ljava/lang/String;)V
.end method

.method public varargs abstract addCustomReceiver(Landroid/preference/CustomUpdater$CustomReceiver;[Ljava/lang/String;)V
.end method

.method public abstract beginChange(Ljava/lang/String;)V
.end method

.method public abstract beginTransmition(Ljava/lang/Object;)V
.end method

.method public abstract clearAllReceiver()V
.end method

.method public abstract removeCustomObjectTransmitter(Landroid/preference/CustomUpdater$CustomObjectTransmitter;)V
.end method

.method public abstract removeCustomReceiver(Landroid/preference/CustomUpdater$CustomReceiver;Ljava/lang/String;)V
.end method

.method public varargs abstract removeCustomReceiver(Landroid/preference/CustomUpdater$CustomReceiver;[Ljava/lang/String;)V
.end method

""",
        "required":    True,
        "reason":      "Legend MTCR new class from Framework_Legend.mtcr",
    },
]
