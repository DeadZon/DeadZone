"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/plugins/controllers/ControllerExt$CallBack.smali'
CLASS_FALLBACK_NAMES = ['ControllerExt$CallBack.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public interface abstract Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/systemui/plugins/controllers/ControllerExt;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x609
    name = "CallBack"
.end annotation


# virtual methods
.method public post(Ljava/lang/Runnable;)Z
    .registers 3

    const/4 v0, 0x0

    return v0
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_plugins_controllers_ControllerExt_CallBack',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
