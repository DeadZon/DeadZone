"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/controllers/SimTypePositionController.smali'
CLASS_FALLBACK_NAMES = ['SimTypePositionController.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/controllers/SimTypePositionController;
.super Lcom/android/systemui/plugins/controllers/ControllerExt;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/android/systemui/newstatusbar/controllers/SimTypePositionController$CallBack;
    }
.end annotation

.annotation system Ldalvik/annotation/Signature;
    value = {
        "Lcom/android/systemui/plugins/controllers/ControllerExt<",
        "Lcom/android/systemui/newstatusbar/controllers/SimTypePositionController$CallBack;",
        ">;"
    }
.end annotation


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 5

    invoke-direct {p0, p1}, Lcom/android/systemui/plugins/controllers/ControllerExt;-><init>(Landroid/content/Context;)V

    new-instance v0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    invoke-direct {v0, p0}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;-><init>(Lcom/android/systemui/plugins/controllers/ControllerExt;)V

    const-string v1, "sim_type_margin"

    const-string v2, "sim_type_position"

    filled-new-array {v1, v2}, [Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->addKeys([Ljava/lang/String;)Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    return-void
.end method


# virtual methods
.method public onSettingsChange()V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/SimTypePositionController;->callBacks:Ljava/util/ArrayList;

    invoke-virtual {v0}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_6
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_16

    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/systemui/newstatusbar/controllers/SimTypePositionController$CallBack;

    invoke-interface {v1}, Lcom/android/systemui/newstatusbar/controllers/SimTypePositionController$CallBack;->onPositionChange()V

    goto :goto_6

    :cond_16
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_controllers_SimTypePositionController',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
