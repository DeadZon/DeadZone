"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/controlcenter/phone/ControlPanelWindowManager$OnWindowChangeListener.smali'
CLASS_FALLBACK_NAMES = ['ControlPanelWindowManager$OnWindowChangeListener.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public interface abstract Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager$OnWindowChangeListener;
.super Ljava/lang/Object;


# virtual methods
.method public abstract onExpandChange(Z)V
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_controlcenter_phone_ControlPanelWindowManager_OnWindowChangeListener',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
