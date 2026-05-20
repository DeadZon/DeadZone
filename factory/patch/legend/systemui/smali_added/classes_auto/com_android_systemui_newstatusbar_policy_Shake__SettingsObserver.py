"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/policy/Shake$SettingsObserver.smali'
CLASS_FALLBACK_NAMES = ['Shake$SettingsObserver.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/newstatusbar/policy/Shake$SettingsObserver;
.super Landroid/database/ContentObserver;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/systemui/newstatusbar/policy/Shake;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = "SettingsObserver"
.end annotation


# instance fields
.field final synthetic this$0:Lcom/android/systemui/newstatusbar/policy/Shake;


# direct methods
.method constructor <init>(Lcom/android/systemui/newstatusbar/policy/Shake;Landroid/os/Handler;)V
    .registers 3

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/policy/Shake$SettingsObserver;->this$0:Lcom/android/systemui/newstatusbar/policy/Shake;

    invoke-direct {p0, p2}, Landroid/database/ContentObserver;-><init>(Landroid/os/Handler;)V

    return-void
.end method


# virtual methods
.method observe()V
    .registers 4

    goto/32 :goto_5

    nop

    :goto_4
    return-void

    :goto_5
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/policy/Shake$SettingsObserver;->this$0:Lcom/android/systemui/newstatusbar/policy/Shake;

    goto/32 :goto_2d

    nop

    :goto_b
    invoke-static {v1}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    goto/32 :goto_21

    nop

    :goto_13
    const-string v1, "shake_mobile"

    goto/32 :goto_b

    nop

    :goto_19
    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    goto/32 :goto_13

    nop

    :goto_21
    const/4 v2, 0x0

    goto/32 :goto_26

    nop

    :goto_26
    invoke-virtual {v0, v1, v2, p0}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    goto/32 :goto_4

    nop

    :goto_2d
    iget-object v0, v0, Lcom/android/systemui/newstatusbar/policy/Shake;->mContext:Landroid/content/Context;

    goto/32 :goto_19

    nop
.end method

.method public onChange(Z)V
    .registers 4

    const-string v0, "shake_mobile"

    const/4 v1, 0x1

    invoke-static {v0, v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v0

    if-lez v0, :cond_14

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/policy/Shake$SettingsObserver;->this$0:Lcom/android/systemui/newstatusbar/policy/Shake;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/policy/Shake;->registerOnOffScreenListener()V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/policy/Shake$SettingsObserver;->this$0:Lcom/android/systemui/newstatusbar/policy/Shake;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/policy/Shake;->registerSensorListener()V

    return-void

    :cond_14
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/policy/Shake$SettingsObserver;->this$0:Lcom/android/systemui/newstatusbar/policy/Shake;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/policy/Shake;->unregisterOnOffScreenListener()V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/policy/Shake$SettingsObserver;->this$0:Lcom/android/systemui/newstatusbar/policy/Shake;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/policy/Shake;->unregisterSensorListener()V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_policy_Shake_SettingsObserver',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
