"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/policy/Shake$ShakeDetector$OnShakeListener.smali'
CLASS_FALLBACK_NAMES = ['Shake$ShakeDetector$OnShakeListener.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public interface abstract Lcom/android/systemui/newstatusbar/policy/Shake$ShakeDetector$OnShakeListener;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/systemui/newstatusbar/policy/Shake$ShakeDetector;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x609
    name = "OnShakeListener"
.end annotation


# virtual methods
.method public abstract onShake(I)V
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_policy_Shake_ShakeDetector_OnShakeListener',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
