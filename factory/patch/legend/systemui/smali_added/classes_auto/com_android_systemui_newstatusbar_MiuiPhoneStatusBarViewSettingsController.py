"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/MiuiPhoneStatusBarViewSettingsController.smali'
CLASS_FALLBACK_NAMES = ['MiuiPhoneStatusBarViewSettingsController.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarViewSettingsController;
.super Lcom/android/systemui/plugins/controllers/ControllerExt;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarViewSettingsController$CallBack;
    }
.end annotation

.annotation system Ldalvik/annotation/Signature;
    value = {
        "Lcom/android/systemui/plugins/controllers/ControllerExt<",
        "Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarViewSettingsController$CallBack;",
        ">;"
    }
.end annotation


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 6

    invoke-direct {p0, p1}, Lcom/android/systemui/plugins/controllers/ControllerExt;-><init>(Landroid/content/Context;)V

    new-instance v0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    const-string v1, "custom_status_bar_top"

    const-string v2, "custom_status_bar_left_right"

    const-string v3, "custom_statusbar_dialog_open"

    filled-new-array {v1, v2, v3}, [Ljava/lang/String;

    move-result-object v1

    invoke-direct {v0, p0, v1}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;-><init>(Lcom/android/systemui/plugins/controllers/ControllerExt;[Ljava/lang/String;)V

    new-instance v0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    const-string v1, "custom_status_bar_height"

    filled-new-array {v1}, [Ljava/lang/String;

    move-result-object v1

    sget-object v2, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;->Global:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;

    invoke-direct {v0, p0, v1, v2}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;-><init>(Lcom/android/systemui/plugins/controllers/ControllerExt;[Ljava/lang/String;Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;)V

    return-void
.end method


# virtual methods
.method public onSettingsChange(Ljava/lang/String;)V
    .registers 4

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarViewSettingsController;->callBacks:Ljava/util/ArrayList;

    invoke-virtual {v0}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_6
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_16

    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarViewSettingsController$CallBack;

    invoke-interface {v1, p1}, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarViewSettingsController$CallBack;->onSettingsChange(Ljava/lang/String;)V

    goto :goto_6

    :cond_16
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_MiuiPhoneStatusBarViewSettingsController',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
