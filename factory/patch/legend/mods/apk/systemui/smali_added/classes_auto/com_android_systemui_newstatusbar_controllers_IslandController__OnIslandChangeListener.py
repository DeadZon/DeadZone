"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/controllers/IslandController$OnIslandChangeListener.smali'
CLASS_FALLBACK_NAMES = ['IslandController$OnIslandChangeListener.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public interface abstract Lcom/android/systemui/newstatusbar/controllers/IslandController$OnIslandChangeListener;
.super Ljava/lang/Object;

# interfaces
.implements Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/systemui/newstatusbar/controllers/IslandController;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x609
    name = "OnIslandChangeListener"
.end annotation


# virtual methods
.method public abstract onIslandShowChange(Z)V
.end method

.method public onIslandSizeChange(II)V
    .registers 3

    return-void
.end method

.method public onIslandSizeChange(Landroid/graphics/Rect;)V
    .registers 2

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_controllers_IslandController_OnIslandChangeListener',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
