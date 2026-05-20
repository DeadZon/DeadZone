"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/statusbar/policy/BatteryBar$SettingsObserver.smali'
CLASS_FALLBACK_NAMES = ['BatteryBar$SettingsObserver.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/statusbar/policy/BatteryBar$SettingsObserver;
.super Landroid/database/ContentObserver;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/systemui/statusbar/policy/BatteryBar;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = "SettingsObserver"
.end annotation


# instance fields
.field final synthetic this$0:Lcom/android/systemui/statusbar/policy/BatteryBar;


# direct methods
.method public constructor <init>(Lcom/android/systemui/statusbar/policy/BatteryBar;Landroid/os/Handler;)V
    .registers 3

    iput-object p1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar$SettingsObserver;->this$0:Lcom/android/systemui/statusbar/policy/BatteryBar;

    invoke-direct {p0, p2}, Landroid/database/ContentObserver;-><init>(Landroid/os/Handler;)V

    return-void
.end method


# virtual methods
.method observer()V
    .registers 4

    goto/32 :goto_be

    nop

    :goto_4
    const-string/jumbo v1, "statusbar_battery_bar_low_color"

    goto/32 :goto_20

    nop

    :goto_b
    const-string/jumbo v1, "statusbar_battery_bar"

    goto/32 :goto_6a

    nop

    :goto_12
    const-string/jumbo v1, "statusbar_battery_bar_use_gradient_color"

    goto/32 :goto_28

    nop

    :goto_19
    invoke-virtual {v0, v1, v2, p0}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    goto/32 :goto_c3

    nop

    :goto_20
    invoke-static {v1}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    goto/32 :goto_98

    nop

    :goto_28
    invoke-static {v1}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    goto/32 :goto_46

    nop

    :goto_30
    const-string/jumbo v1, "statusbar_battery_bar_color"

    goto/32 :goto_a7

    nop

    :goto_37
    invoke-static {v1}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    goto/32 :goto_82

    nop

    :goto_3f
    invoke-virtual {v0, v1, v2, p0}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    goto/32 :goto_30

    nop

    :goto_46
    invoke-virtual {v0, v1, v2, p0}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    goto/32 :goto_54

    nop

    :goto_4d
    const-string/jumbo v1, "statusbar_battery_bar_animate"

    goto/32 :goto_72

    nop

    :goto_54
    return-void

    :goto_55
    invoke-virtual {v0, v1, v2, p0}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    goto/32 :goto_4

    nop

    :goto_5c
    const-string/jumbo v1, "statusbar_battery_bar_high_color"

    goto/32 :goto_d7

    nop

    :goto_63
    invoke-virtual {v0, v1, v2, p0}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    goto/32 :goto_4d

    nop

    :goto_6a
    invoke-static {v1}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    goto/32 :goto_3f

    nop

    :goto_72
    invoke-static {v1}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    goto/32 :goto_89

    nop

    :goto_7a
    invoke-virtual {v1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    goto/32 :goto_b

    nop

    :goto_82
    invoke-virtual {v0, v1, v2, p0}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    goto/32 :goto_12

    nop

    :goto_89
    invoke-virtual {v0, v1, v2, p0}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    goto/32 :goto_5c

    nop

    :goto_90
    invoke-static {v1}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    goto/32 :goto_ca

    nop

    :goto_98
    const-string/jumbo v1, "statusbar_battery_bar_low_color2"

    goto/32 :goto_37

    nop

    :goto_9f
    invoke-static {v1}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    goto/32 :goto_63

    nop

    :goto_a7
    invoke-static {v1}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    goto/32 :goto_19

    nop

    :goto_af
    invoke-static {v1}, Lcom/android/systemui/statusbar/policy/BatteryBar;->-get2(Lcom/android/systemui/statusbar/policy/BatteryBar;)Landroid/content/Context;

    move-result-object v1

    goto/32 :goto_7a

    nop

    :goto_b7
    const-string/jumbo v1, "statusbar_battery_bar_battery_low_color_warning"

    goto/32 :goto_9f

    nop

    :goto_be
    const/4 v2, 0x0

    goto/32 :goto_d1

    nop

    :goto_c3
    const-string/jumbo v1, "statusbar_battery_bar_charging_color"

    goto/32 :goto_90

    nop

    :goto_ca
    invoke-virtual {v0, v1, v2, p0}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    goto/32 :goto_b7

    nop

    :goto_d1
    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar$SettingsObserver;->this$0:Lcom/android/systemui/statusbar/policy/BatteryBar;

    goto/32 :goto_af

    nop

    :goto_d7
    invoke-static {v1}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    goto/32 :goto_55

    nop
.end method

.method public onChange(Z)V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/statusbar/policy/BatteryBar$SettingsObserver;->this$0:Lcom/android/systemui/statusbar/policy/BatteryBar;

    invoke-static {v0}, Lcom/android/systemui/statusbar/policy/BatteryBar;->-wrap1(Lcom/android/systemui/statusbar/policy/BatteryBar;)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_statusbar_policy_BatteryBar_SettingsObserver',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
