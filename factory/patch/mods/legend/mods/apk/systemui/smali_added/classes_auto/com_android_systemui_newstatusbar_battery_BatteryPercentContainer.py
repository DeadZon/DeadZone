"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/battery/BatteryPercentContainer.smali'
CLASS_FALLBACK_NAMES = ['BatteryPercentContainer.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;
.super Landroid/widget/LinearLayout;

# interfaces
.implements Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;


# instance fields
.field private final controller:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

.field private isItalicMark:Z

.field private isItalicPercent:Z

.field private mark:Landroid/widget/TextView;

.field private percent:Landroid/widget/TextView;


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 4

    invoke-direct {p0, p1, p2}, Landroid/widget/LinearLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;->controller:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 5

    invoke-direct {p0, p1, p2, p3}, Landroid/widget/LinearLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;->controller:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    return-void
.end method

.method private getDataMark()Lcom/android/systemui/newstatusbar/data/TextData;
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;->controller:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    const/4 v1, 0x0

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->getTextData(Z)Lcom/android/systemui/newstatusbar/data/TextData;

    move-result-object v0

    return-object v0
.end method

.method private getDataPercent()Lcom/android/systemui/newstatusbar/data/TextData;
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;->controller:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    const/4 v1, 0x1

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->getTextData(Z)Lcom/android/systemui/newstatusbar/data/TextData;

    move-result-object v0

    return-object v0
.end method


# virtual methods
.method protected onAttachedToWindow()V
    .registers 2

    goto/32 :goto_a

    nop

    :goto_4
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;->controller:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    goto/32 :goto_11

    nop

    :goto_a
    invoke-super {p0}, Landroid/widget/LinearLayout;->onAttachedToWindow()V

    goto/32 :goto_4

    nop

    :goto_11
    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->addCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V

    goto/32 :goto_18

    nop

    :goto_18
    return-void
.end method

.method protected onDetachedFromWindow()V
    .registers 2

    goto/32 :goto_12

    nop

    :goto_4
    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->removeCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V

    goto/32 :goto_11

    nop

    :goto_b
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;->controller:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    goto/32 :goto_4

    nop

    :goto_11
    return-void

    :goto_12
    invoke-super {p0}, Landroid/widget/LinearLayout;->onDetachedFromWindow()V

    goto/32 :goto_b

    nop
.end method

.method protected onFinishInflate()V
    .registers 2

    goto/32 :goto_10

    nop

    :goto_4
    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;->setClipToPadding(Z)V

    goto/32 :goto_2b

    nop

    :goto_b
    const/4 v0, 0x0

    goto/32 :goto_39

    nop

    :goto_10
    invoke-super {p0}, Landroid/widget/LinearLayout;->onFinishInflate()V

    goto/32 :goto_b

    nop

    :goto_17
    check-cast v0, Landroid/widget/TextView;

    goto/32 :goto_25

    nop

    :goto_1d
    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;->getChildAt(I)Landroid/view/View;

    move-result-object v0

    goto/32 :goto_41

    nop

    :goto_25
    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;->percent:Landroid/widget/TextView;

    goto/32 :goto_47

    nop

    :goto_2b
    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;->getChildAt(I)Landroid/view/View;

    move-result-object v0

    goto/32 :goto_17

    nop

    :goto_33
    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;->mark:Landroid/widget/TextView;

    goto/32 :goto_40

    nop

    :goto_39
    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;->setClipChildren(Z)V

    goto/32 :goto_4

    nop

    :goto_40
    return-void

    :goto_41
    check-cast v0, Landroid/widget/TextView;

    goto/32 :goto_33

    nop

    :goto_47
    const/4 v0, 0x1

    goto/32 :goto_1d

    nop
.end method

.method public onIconChange()V
    .registers 5

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;->getDataMark()Lcom/android/systemui/newstatusbar/data/TextData;

    move-result-object v0

    iget v0, v0, Lcom/android/systemui/newstatusbar/data/TextData;->typeFaseStyle:I

    const/4 v1, 0x1

    const/4 v2, 0x0

    const/4 v3, 0x2

    if-lt v0, v3, :cond_d

    move v0, v1

    goto :goto_e

    :cond_d
    move v0, v2

    :goto_e
    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;->isItalicMark:Z

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;->getDataPercent()Lcom/android/systemui/newstatusbar/data/TextData;

    move-result-object v0

    iget v0, v0, Lcom/android/systemui/newstatusbar/data/TextData;->typeFaseStyle:I

    if-lt v0, v3, :cond_19

    goto :goto_1a

    :cond_19
    move v1, v2

    :goto_1a
    iput-boolean v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;->isItalicPercent:Z

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;->requestLayout()V

    return-void
.end method

.method protected onLayout(ZIIII)V
    .registers 12

    goto/32 :goto_9e

    nop

    :goto_4
    return-void

    :goto_5
    iget-object v3, p0, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;->percent:Landroid/widget/TextView;

    goto/32 :goto_3c

    nop

    :goto_b
    return-void

    :goto_c
    goto/32 :goto_15

    nop

    :goto_10
    add-int/2addr v4, v1

    goto/32 :goto_b9

    nop

    :goto_15
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;->mark:Landroid/widget/TextView;

    goto/32 :goto_87

    nop

    :goto_1b
    invoke-virtual {v5}, Landroid/widget/TextView;->getBottom()I

    move-result v5

    goto/32 :goto_2b

    nop

    :goto_23
    invoke-virtual {v2}, Landroid/widget/TextView;->getTop()I

    move-result v3

    goto/32 :goto_b3

    nop

    :goto_2b
    invoke-virtual {v2, v1, v3, v4, v5}, Landroid/widget/TextView;->layout(IIII)V

    :goto_2e
    goto/32 :goto_4

    nop

    :goto_32
    goto :goto_83

    :goto_33
    goto/32 :goto_82

    nop

    :goto_37
    move v0, v2

    :goto_38
    goto/32 :goto_95

    nop

    :goto_3c
    if-eqz v0, :cond_41

    goto/32 :goto_33

    :cond_41
    goto/32 :goto_4d

    nop

    :goto_45
    invoke-static {v4, v5}, Lcom/android/systemui/newstatusbar/util/TextUtil;->measureText(Landroid/widget/TextView;Z)I

    move-result v4

    goto/32 :goto_10

    nop

    :goto_4d
    iget-boolean v4, p0, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;->isItalicPercent:Z

    goto/32 :goto_53

    nop

    :goto_53
    if-nez v4, :cond_58

    goto/32 :goto_33

    :cond_58
    goto/32 :goto_32

    nop

    :goto_5c
    goto :goto_38

    :goto_5d
    goto/32 :goto_37

    nop

    :goto_61
    if-eqz v0, :cond_66

    goto/32 :goto_5d

    :cond_66
    goto/32 :goto_a5

    nop

    :goto_6a
    invoke-static {v3, v1}, Lcom/android/systemui/newstatusbar/util/TextUtil;->measureText(Landroid/widget/TextView;Z)I

    move-result v1

    goto/32 :goto_72

    nop

    :goto_72
    iget-object v2, p0, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;->mark:Landroid/widget/TextView;

    goto/32 :goto_23

    nop

    :goto_78
    const/4 v2, 0x0

    goto/32 :goto_61

    nop

    :goto_7d
    const/4 v1, 0x1

    goto/32 :goto_78

    nop

    :goto_82
    move v1, v2

    :goto_83
    goto/32 :goto_6a

    nop

    :goto_87
    invoke-virtual {v0}, Landroid/widget/TextView;->getVisibility()I

    move-result v0

    goto/32 :goto_7d

    nop

    :goto_8f
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;->percent:Landroid/widget/TextView;

    goto/32 :goto_aa

    nop

    :goto_95
    if-nez v0, :cond_9a

    goto/32 :goto_2e

    :cond_9a
    goto/32 :goto_5

    nop

    :goto_9e
    invoke-super/range {p0 .. p5}, Landroid/widget/LinearLayout;->onLayout(ZIIII)V

    goto/32 :goto_8f

    nop

    :goto_a5
    move v0, v1

    goto/32 :goto_5c

    nop

    :goto_aa
    if-eqz v0, :cond_af

    goto/32 :goto_c

    :cond_af
    goto/32 :goto_b

    nop

    :goto_b3
    iget-object v4, p0, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;->mark:Landroid/widget/TextView;

    goto/32 :goto_bf

    nop

    :goto_b9
    iget-object v5, p0, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;->mark:Landroid/widget/TextView;

    goto/32 :goto_1b

    nop

    :goto_bf
    iget-boolean v5, p0, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;->isItalicMark:Z

    goto/32 :goto_45

    nop
.end method

.method protected onMeasure(II)V
    .registers 8

    goto/32 :goto_40

    nop

    :goto_4
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;->mark:Landroid/widget/TextView;

    goto/32 :goto_2f

    nop

    :goto_a
    invoke-virtual {p0, v1, v2}, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;->setMeasuredDimension(II)V

    :goto_d
    goto/32 :goto_77

    nop

    :goto_11
    if-eqz v0, :cond_16

    goto/32 :goto_c8

    :cond_16
    goto/32 :goto_55

    nop

    :goto_1a
    if-nez v0, :cond_1f

    goto/32 :goto_d

    :cond_1f
    goto/32 :goto_4

    nop

    :goto_23
    iget-boolean v3, p0, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;->isItalicMark:Z

    goto/32 :goto_bf

    nop

    :goto_29
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;->mark:Landroid/widget/TextView;

    goto/32 :goto_9f

    nop

    :goto_2f
    if-nez v1, :cond_34

    goto/32 :goto_d

    :cond_34
    goto/32 :goto_38

    nop

    :goto_38
    invoke-virtual {v0}, Landroid/widget/TextView;->getVisibility()I

    move-result v0

    goto/32 :goto_78

    nop

    :goto_40
    invoke-super {p0, p1, p2}, Landroid/widget/LinearLayout;->onMeasure(II)V

    goto/32 :goto_47

    nop

    :goto_47
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;->percent:Landroid/widget/TextView;

    goto/32 :goto_1a

    nop

    :goto_4d
    invoke-static {v3, v1}, Lcom/android/systemui/newstatusbar/util/TextUtil;->measureText(Landroid/widget/TextView;Z)I

    move-result v1

    goto/32 :goto_b1

    nop

    :goto_55
    iget-boolean v4, p0, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;->isItalicPercent:Z

    goto/32 :goto_61

    nop

    :goto_5b
    iget-object v3, p0, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;->percent:Landroid/widget/TextView;

    goto/32 :goto_11

    nop

    :goto_61
    if-nez v4, :cond_66

    goto/32 :goto_c8

    :cond_66
    goto/32 :goto_c7

    nop

    :goto_6a
    const/4 v2, 0x0

    goto/32 :goto_8c

    nop

    :goto_6f
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;->getMeasuredHeight()I

    move-result v2

    goto/32 :goto_a

    nop

    :goto_77
    return-void

    :goto_78
    if-eqz v0, :cond_7d

    goto/32 :goto_d

    :cond_7d
    goto/32 :goto_29

    nop

    :goto_81
    iget-object v2, p0, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;->mark:Landroid/widget/TextView;

    goto/32 :goto_23

    nop

    :goto_87
    move v0, v2

    :goto_88
    goto/32 :goto_5b

    nop

    :goto_8c
    if-eqz v0, :cond_91

    goto/32 :goto_9b

    :cond_91
    goto/32 :goto_95

    nop

    :goto_95
    move v0, v1

    goto/32 :goto_9a

    nop

    :goto_9a
    goto :goto_88

    :goto_9b
    goto/32 :goto_87

    nop

    :goto_9f
    invoke-virtual {v0}, Landroid/widget/TextView;->getVisibility()I

    move-result v0

    goto/32 :goto_ba

    nop

    :goto_a7
    move v1, v2

    :goto_a8
    goto/32 :goto_4d

    nop

    :goto_ac
    add-int/2addr v1, v2

    :goto_ad
    goto/32 :goto_6f

    nop

    :goto_b1
    if-nez v0, :cond_b6

    goto/32 :goto_ad

    :cond_b6
    goto/32 :goto_81

    nop

    :goto_ba
    const/4 v1, 0x1

    goto/32 :goto_6a

    nop

    :goto_bf
    invoke-static {v2, v3}, Lcom/android/systemui/newstatusbar/util/TextUtil;->measureText(Landroid/widget/TextView;Z)I

    move-result v2

    goto/32 :goto_ac

    nop

    :goto_c7
    goto :goto_a8

    :goto_c8
    goto/32 :goto_a7

    nop
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_battery_BatteryPercentContainer',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
