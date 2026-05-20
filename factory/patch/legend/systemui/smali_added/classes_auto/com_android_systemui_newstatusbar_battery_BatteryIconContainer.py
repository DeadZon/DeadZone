"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/battery/BatteryIconContainer.smali'
CLASS_FALLBACK_NAMES = ['BatteryIconContainer.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/battery/BatteryIconContainer;
.super Landroid/widget/FrameLayout;


# instance fields
.field private hollow:Landroid/view/View;

.field private icon:Landroid/view/View;


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 3

    invoke-direct {p0, p1, p2}, Landroid/widget/FrameLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 4

    invoke-direct {p0, p1, p2, p3}, Landroid/widget/FrameLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    return-void
.end method


# virtual methods
.method protected onFinishInflate()V
    .registers 2

    goto/32 :goto_4

    nop

    :goto_4
    invoke-super {p0}, Landroid/widget/FrameLayout;->onFinishInflate()V

    goto/32 :goto_19

    nop

    :goto_b
    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/battery/BatteryIconContainer;->getChildAt(I)Landroid/view/View;

    move-result-object v0

    goto/32 :goto_13

    nop

    :goto_13
    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryIconContainer;->icon:Landroid/view/View;

    goto/32 :goto_2c

    nop

    :goto_19
    const/4 v0, 0x0

    goto/32 :goto_b

    nop

    :goto_1e
    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/battery/BatteryIconContainer;->getChildAt(I)Landroid/view/View;

    move-result-object v0

    goto/32 :goto_26

    nop

    :goto_26
    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryIconContainer;->hollow:Landroid/view/View;

    goto/32 :goto_31

    nop

    :goto_2c
    const/4 v0, 0x1

    goto/32 :goto_1e

    nop

    :goto_31
    return-void
.end method

.method protected onMeasure(II)V
    .registers 7

    goto/32 :goto_4

    nop

    :goto_4
    invoke-super {p0, p1, p2}, Landroid/widget/FrameLayout;->onMeasure(II)V

    goto/32 :goto_90

    nop

    :goto_b
    iget-object v3, p0, Lcom/android/systemui/newstatusbar/battery/BatteryIconContainer;->icon:Landroid/view/View;

    goto/32 :goto_4a

    nop

    :goto_11
    if-ne v0, v2, :cond_16

    goto/32 :goto_c1

    :cond_16
    goto/32 :goto_1f

    nop

    :goto_1a
    move v0, v1

    :goto_1b
    goto/32 :goto_b

    nop

    :goto_1f
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryIconContainer;->icon:Landroid/view/View;

    :goto_21
    goto/32 :goto_25

    nop

    :goto_25
    invoke-virtual {v0}, Landroid/view/View;->getMeasuredWidth()I

    move-result v0

    goto/32 :goto_bf

    nop

    :goto_2d
    goto :goto_98

    :goto_2e
    goto/32 :goto_64

    nop

    :goto_32
    invoke-virtual {v3}, Landroid/view/View;->getVisibility()I

    move-result v3

    goto/32 :goto_a7

    nop

    :goto_3a
    const/16 v2, 0x8

    goto/32 :goto_11

    nop

    :goto_40
    if-ne v3, v2, :cond_45

    goto/32 :goto_9d

    :cond_45
    goto/32 :goto_96

    nop

    :goto_49
    return-void

    :goto_4a
    invoke-virtual {v3}, Landroid/view/View;->getVisibility()I

    move-result v3

    goto/32 :goto_40

    nop

    :goto_52
    invoke-virtual {v0}, Landroid/view/View;->getVisibility()I

    move-result v0

    goto/32 :goto_b6

    nop

    :goto_5a
    goto :goto_21

    :goto_5b
    goto/32 :goto_1a

    nop

    :goto_5f
    const/4 v1, 0x0

    goto/32 :goto_3a

    nop

    :goto_64
    invoke-virtual {p0, v0, v1}, Lcom/android/systemui/newstatusbar/battery/BatteryIconContainer;->setMeasuredDimension(II)V

    :goto_67
    goto/32 :goto_49

    nop

    :goto_6b
    invoke-virtual {v0}, Landroid/view/View;->getVisibility()I

    move-result v0

    goto/32 :goto_5f

    nop

    :goto_73
    iget-object v3, p0, Lcom/android/systemui/newstatusbar/battery/BatteryIconContainer;->hollow:Landroid/view/View;

    goto/32 :goto_32

    nop

    :goto_79
    if-nez v0, :cond_7e

    goto/32 :goto_67

    :cond_7e
    goto/32 :goto_6b

    nop

    :goto_82
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryIconContainer;->hollow:Landroid/view/View;

    goto/32 :goto_2d

    nop

    :goto_88
    invoke-virtual {v1}, Landroid/view/View;->getMeasuredHeight()I

    move-result v1

    goto/32 :goto_9c

    nop

    :goto_90
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryIconContainer;->icon:Landroid/view/View;

    goto/32 :goto_79

    nop

    :goto_96
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryIconContainer;->icon:Landroid/view/View;

    :goto_98
    goto/32 :goto_88

    nop

    :goto_9c
    goto :goto_2e

    :goto_9d
    goto/32 :goto_73

    nop

    :goto_a1
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryIconContainer;->hollow:Landroid/view/View;

    goto/32 :goto_52

    nop

    :goto_a7
    if-ne v3, v2, :cond_ac

    goto/32 :goto_2e

    :cond_ac
    goto/32 :goto_82

    nop

    :goto_b0
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryIconContainer;->hollow:Landroid/view/View;

    goto/32 :goto_5a

    nop

    :goto_b6
    if-ne v0, v2, :cond_bb

    goto/32 :goto_5b

    :cond_bb
    goto/32 :goto_b0

    nop

    :goto_bf
    goto/16 :goto_1b

    :goto_c1
    goto/32 :goto_a1

    nop
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_battery_BatteryIconContainer',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
