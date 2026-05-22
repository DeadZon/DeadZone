"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/statusbar/policy/MyKeyguardStateController$CallBack.smali'
CLASS_FALLBACK_NAMES = ['MyKeyguardStateController$CallBack.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public interface abstract Lcom/android/systemui/statusbar/policy/MyKeyguardStateController$CallBack;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x609
    name = "CallBack"
.end annotation


# virtual methods
.method public abstract onKeyguardStateChange(Z)V
.end method

.method public abstract onScreenOnStateChange(Z)V
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_statusbar_policy_MyKeyguardStateController_CallBack',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
