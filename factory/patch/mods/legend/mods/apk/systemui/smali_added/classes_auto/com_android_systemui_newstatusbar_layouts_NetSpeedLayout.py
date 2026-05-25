"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/layouts/NetSpeedLayout.smali'
CLASS_FALLBACK_NAMES = ['NetSpeedLayout.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/layouts/NetSpeedLayout;
.super Landroid/widget/LinearLayout;


# instance fields
.field TAG:Ljava/lang/String;

.field private bottom:Landroid/widget/TextView;

.field private height:I

.field private top:Landroid/widget/TextView;


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 3

    invoke-direct {p0, p1}, Landroid/widget/LinearLayout;-><init>(Landroid/content/Context;)V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/NetSpeedLayout;->updateHeight()V

    const-string v0, "Mezonetspeedlayout"

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/NetSpeedLayout;->TAG:Ljava/lang/String;

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 4

    invoke-direct {p0, p1, p2}, Landroid/widget/LinearLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/NetSpeedLayout;->updateHeight()V

    const-string v0, "Mezonetspeedlayout"

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/NetSpeedLayout;->TAG:Ljava/lang/String;

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 5

    invoke-direct {p0, p1, p2, p3}, Landroid/widget/LinearLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/NetSpeedLayout;->updateHeight()V

    const-string v0, "Mezonetspeedlayout"

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/NetSpeedLayout;->TAG:Ljava/lang/String;

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V
    .registers 6

    invoke-direct {p0, p1, p2, p3, p4}, Landroid/widget/LinearLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/NetSpeedLayout;->updateHeight()V

    const-string v0, "Mezonetspeedlayout"

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/NetSpeedLayout;->TAG:Ljava/lang/String;

    return-void
.end method

.method private isValid()Z
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/NetSpeedLayout;->top:Landroid/widget/TextView;

    if-eqz v0, :cond_a

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/NetSpeedLayout;->bottom:Landroid/widget/TextView;

    if-eqz v0, :cond_a

    const/4 v0, 0x1

    goto :goto_b

    :cond_a
    const/4 v0, 0x0

    :goto_b
    return v0
.end method


# virtual methods
.method protected onFinishInflate()V
    .registers 2

    goto/32 :goto_a

    nop

    :goto_4
    check-cast v0, Landroid/widget/TextView;

    goto/32 :goto_38

    nop

    :goto_a
    invoke-super {p0}, Landroid/widget/LinearLayout;->onFinishInflate()V

    goto/32 :goto_32

    nop

    :goto_11
    check-cast v0, Landroid/widget/TextView;

    goto/32 :goto_1f

    nop

    :goto_17
    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/NetSpeedLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v0

    goto/32 :goto_11

    nop

    :goto_1f
    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/NetSpeedLayout;->top:Landroid/widget/TextView;

    goto/32 :goto_25

    nop

    :goto_25
    const/4 v0, 0x1

    goto/32 :goto_2a

    nop

    :goto_2a
    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/NetSpeedLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v0

    goto/32 :goto_4

    nop

    :goto_32
    const/4 v0, 0x0

    goto/32 :goto_17

    nop

    :goto_37
    return-void

    :goto_38
    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/NetSpeedLayout;->bottom:Landroid/widget/TextView;

    goto/32 :goto_37

    nop
.end method

.method protected onMeasure(II)V
    .registers 5

    goto/32 :goto_24

    nop

    :goto_4
    invoke-static {v0, v1}, Ljava/lang/Math;->max(II)I

    move-result v0

    goto/32 :goto_2b

    nop

    :goto_c
    invoke-virtual {v0}, Landroid/widget/TextView;->getMeasuredWidth()I

    move-result v0

    goto/32 :goto_48

    nop

    :goto_14
    invoke-virtual {p0, v0, v1}, Lcom/android/systemui/newstatusbar/layouts/NetSpeedLayout;->setMeasuredDimension(II)V

    :goto_17
    goto/32 :goto_39

    nop

    :goto_1b
    if-nez v0, :cond_20

    goto/32 :goto_17

    :cond_20
    goto/32 :goto_42

    nop

    :goto_24
    invoke-super {p0, p1, p2}, Landroid/widget/LinearLayout;->onMeasure(II)V

    goto/32 :goto_3a

    nop

    :goto_2b
    iget v1, p0, Lcom/android/systemui/newstatusbar/layouts/NetSpeedLayout;->height:I

    goto/32 :goto_14

    nop

    :goto_31
    invoke-virtual {v1}, Landroid/widget/TextView;->getMeasuredWidth()I

    move-result v1

    goto/32 :goto_4

    nop

    :goto_39
    return-void

    :goto_3a
    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/layouts/NetSpeedLayout;->isValid()Z

    move-result v0

    goto/32 :goto_1b

    nop

    :goto_42
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/NetSpeedLayout;->top:Landroid/widget/TextView;

    goto/32 :goto_c

    nop

    :goto_48
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/NetSpeedLayout;->bottom:Landroid/widget/TextView;

    goto/32 :goto_31

    nop
.end method

.method public updateHeight()V
    .registers 4

    const-string v0, "net_speed_height"

    const v1, 0x28

    invoke-static {v0, v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v0

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/NetSpeedLayout;->height:I

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/NetSpeedLayout;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v0

    if-eqz v0, :cond_1c

    iget v1, v0, Landroid/view/ViewGroup$LayoutParams;->height:I

    iget v2, p0, Lcom/android/systemui/newstatusbar/layouts/NetSpeedLayout;->height:I

    if-eq v1, v2, :cond_1c

    iput v2, v0, Landroid/view/ViewGroup$LayoutParams;->height:I

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/NetSpeedLayout;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    :cond_1c
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_layouts_NetSpeedLayout',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
