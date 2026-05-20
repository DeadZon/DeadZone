"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/statusbar/policy/BatteryBarController$SettingsObserver.smali'
CLASS_FALLBACK_NAMES = ['BatteryBarController$SettingsObserver.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/statusbar/policy/BatteryBarController$SettingsObserver;
.super Landroid/database/ContentObserver;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/systemui/statusbar/policy/BatteryBarController;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = "SettingsObserver"
.end annotation


# instance fields
.field final synthetic this$0:Lcom/android/systemui/statusbar/policy/BatteryBarController;


# direct methods
.method public constructor <init>(Lcom/android/systemui/statusbar/policy/BatteryBarController;Landroid/os/Handler;)V
    .registers 3

    iput-object p1, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController$SettingsObserver;->this$0:Lcom/android/systemui/statusbar/policy/BatteryBarController;

    invoke-direct {p0, p2}, Landroid/database/ContentObserver;-><init>(Landroid/os/Handler;)V

    return-void
.end method


# virtual methods
.method observe()V
    .registers 4

    goto/32 :goto_4b

    nop

    :goto_4
    const-string v1, "battery_bar_thickness"

    goto/32 :goto_27

    nop

    :goto_a
    invoke-virtual {v0, v1, v2, p0}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    goto/32 :goto_4

    nop

    :goto_11
    invoke-static {v1}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    goto/32 :goto_a

    nop

    :goto_19
    invoke-virtual {v1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    goto/32 :goto_45

    nop

    :goto_21
    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController$SettingsObserver;->this$0:Lcom/android/systemui/statusbar/policy/BatteryBarController;

    goto/32 :goto_30

    nop

    :goto_27
    invoke-static {v1}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    goto/32 :goto_3e

    nop

    :goto_2f
    return-void

    :goto_30
    invoke-static {v1}, Lcom/android/systemui/statusbar/policy/BatteryBarController;->access$000(Lcom/android/systemui/statusbar/policy/BatteryBarController;)Landroid/content/Context;

    move-result-object v1

    goto/32 :goto_19

    nop

    :goto_38
    const-string v1, "battery_bar_style"

    goto/32 :goto_11

    nop

    :goto_3e
    invoke-virtual {v0, v1, v2, p0}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    goto/32 :goto_2f

    nop

    :goto_45
    const-string v1, "battery_bar"

    goto/32 :goto_57

    nop

    :goto_4b
    const/4 v2, 0x0

    goto/32 :goto_21

    nop

    :goto_50
    invoke-virtual {v0, v1, v2, p0}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    goto/32 :goto_38

    nop

    :goto_57
    invoke-static {v1}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    goto/32 :goto_50

    nop
.end method

.method public onChange(Z)V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController$SettingsObserver;->this$0:Lcom/android/systemui/statusbar/policy/BatteryBarController;

    invoke-virtual {v0}, Lcom/android/systemui/statusbar/policy/BatteryBarController;->updateSettings()V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_statusbar_policy_BatteryBarController_SettingsObserver',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
