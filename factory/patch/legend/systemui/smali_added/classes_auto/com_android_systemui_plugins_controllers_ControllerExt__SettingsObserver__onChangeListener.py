"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$onChangeListener.smali'
CLASS_FALLBACK_NAMES = ['ControllerExt$SettingsObserver$onChangeListener.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public interface abstract Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$onChangeListener;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x609
    name = "onChangeListener"
.end annotation


# virtual methods
.method public onChange()V
    .registers 1

    return-void
.end method

.method public onChange(Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;Landroid/net/Uri;)V
    .registers 3
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver",
            "<+",
            "Lcom/android/systemui/plugins/controllers/ControllerExt",
            "<+",
            "Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;",
            ">;>;",
            "Landroid/net/Uri;",
            ")V"
        }
    .end annotation

    invoke-interface {p0}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$onChangeListener;->onChange()V

    return-void
.end method

.method public onChange(Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;Ljava/lang/String;)V
    .registers 3
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver",
            "<+",
            "Lcom/android/systemui/plugins/controllers/ControllerExt",
            "<+",
            "Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;",
            ">;>;",
            "Ljava/lang/String;",
            ")V"
        }
    .end annotation

    invoke-interface {p0, p2}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$onChangeListener;->onChange(Ljava/lang/String;)V

    return-void
.end method

.method public onChange(Ljava/lang/String;)V
    .registers 2

    invoke-interface {p0}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$onChangeListener;->onChange()V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_plugins_controllers_ControllerExt_SettingsObserver_onChangeListener',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
