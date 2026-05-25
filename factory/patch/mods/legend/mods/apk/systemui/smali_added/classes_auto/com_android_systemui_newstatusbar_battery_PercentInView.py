"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/battery/PercentInView.smali'
CLASS_FALLBACK_NAMES = ['PercentInView.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/battery/PercentInView;
.super Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;

# interfaces
.implements Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;


# instance fields
.field private final controller:Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 4

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    const-class v0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/PercentInView;->controller:Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 5

    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    const-class v0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/PercentInView;->controller:Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;

    return-void
.end method


# virtual methods
.method protected getData()Lcom/android/systemui/newstatusbar/data/TextData;
    .registers 3

    goto/32 :goto_11

    nop

    :goto_4
    const/4 v1, 0x0

    goto/32 :goto_9

    nop

    :goto_9
    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->getTextData(Z)Lcom/android/systemui/newstatusbar/data/TextData;

    move-result-object v0

    goto/32 :goto_17

    nop

    :goto_11
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/PercentInView;->controller:Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;

    goto/32 :goto_4

    nop

    :goto_17
    return-object v0
.end method

.method protected onAttached()V
    .registers 2

    goto/32 :goto_13

    nop

    :goto_4
    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->addCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V

    goto/32 :goto_c

    nop

    :goto_b
    return-void

    :goto_c
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/PercentInView;->onIconChange()V

    goto/32 :goto_b

    nop

    :goto_13
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/PercentInView;->controller:Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;

    goto/32 :goto_4

    nop
.end method

.method protected onDetached()V
    .registers 2

    goto/32 :goto_5

    nop

    :goto_4
    return-void

    :goto_5
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/PercentInView;->controller:Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;

    goto/32 :goto_b

    nop

    :goto_b
    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->removeCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V

    goto/32 :goto_4

    nop
.end method

.method public onIconChange()V
    .registers 1

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/PercentInView;->update()V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_battery_PercentInView',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
