"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/battery/PercentMarkView.smali'
CLASS_FALLBACK_NAMES = ['PercentMarkView.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/battery/PercentMarkView;
.super Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;

# interfaces
.implements Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;


# instance fields
.field private controller:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

.field private isMarkSettingsEnable:Z


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 4

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/PercentMarkView;->controller:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 5

    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/PercentMarkView;->controller:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    return-void
.end method


# virtual methods
.method protected getData()Lcom/android/systemui/newstatusbar/data/TextData;
    .registers 3

    goto/32 :goto_1e

    nop

    :goto_4
    xor-int/lit8 v1, v1, 0x1

    goto/32 :goto_16

    nop

    :goto_a
    return-object v0

    :goto_b
    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/battery/PercentMarkView;->isMarkSettingsEnable:Z

    goto/32 :goto_4

    nop

    :goto_11
    const/4 v0, 0x0

    goto/32 :goto_24

    nop

    :goto_16
    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->getTextData(Z)Lcom/android/systemui/newstatusbar/data/TextData;

    move-result-object v0

    goto/32 :goto_a

    nop

    :goto_1e
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/PercentMarkView;->controller:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    goto/32 :goto_29

    nop

    :goto_24
    return-object v0

    :goto_25
    goto/32 :goto_b

    nop

    :goto_29
    if-eqz v0, :cond_2e

    goto/32 :goto_25

    :cond_2e
    goto/32 :goto_11

    nop
.end method

.method protected onAttached()V
    .registers 2

    goto/32 :goto_c

    nop

    :goto_4
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/PercentMarkView;->onIconChange()V

    goto/32 :goto_b

    nop

    :goto_b
    return-void

    :goto_c
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/PercentMarkView;->controller:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    goto/32 :goto_12

    nop

    :goto_12
    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->addCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V

    goto/32 :goto_4

    nop
.end method

.method protected onDetached()V
    .registers 2

    goto/32 :goto_c

    nop

    :goto_4
    return-void

    :goto_5
    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->removeCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V

    goto/32 :goto_4

    nop

    :goto_c
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/PercentMarkView;->controller:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    goto/32 :goto_5

    nop
.end method

.method public onIconChange()V
    .registers 2

    const-string v0, "battery_percent_mark_settings_enable"

    invoke-static {v0}, Landroid/preference/SettingsMezoHelper;->getBoolofSettings1(Ljava/lang/String;)Z

    move-result v0

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/PercentMarkView;->isMarkSettingsEnable:Z

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/PercentMarkView;->update()V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_battery_PercentMarkView',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
