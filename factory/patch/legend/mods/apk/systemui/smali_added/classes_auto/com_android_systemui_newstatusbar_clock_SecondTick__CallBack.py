"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/clock/SecondTick$CallBack.smali'
CLASS_FALLBACK_NAMES = ['SecondTick$CallBack.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public interface abstract Lcom/android/systemui/newstatusbar/clock/SecondTick$CallBack;
.super Ljava/lang/Object;

# interfaces
.implements Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/systemui/newstatusbar/clock/SecondTick;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x609
    name = "CallBack"
.end annotation


# virtual methods
.method public isSecondEnable()Z
    .registers 2

    const/4 v0, 0x0

    return v0
.end method

.method public abstract post(Ljava/lang/Runnable;)Z
.end method

.method public secondTick()V
    .registers 1

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_clock_SecondTick_CallBack',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
