"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/layouts/ElementLayout.smali'
CLASS_FALLBACK_NAMES = ['ElementLayout.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public abstract Lcom/android/systemui/newstatusbar/layouts/ElementLayout;
.super Lcom/android/systemui/newstatusbar/layouts/SingleLayout;


# instance fields
.field private isNeedOvewflowLayout:Z

.field private overflowLayout:Landroid/view/ViewGroup;


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 3

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementLayout;->createView()V

    return-void
.end method

.method private createView()V
    .registers 4

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementLayout;->isNotif()Z

    move-result v0

    if-nez v0, :cond_f

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementLayout;->isStatus()Z

    move-result v0

    if-eqz v0, :cond_d

    goto :goto_f

    :cond_d
    const/4 v0, 0x0

    goto :goto_10

    :cond_f
    :goto_f
    const/4 v0, 0x1

    :goto_10
    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/layouts/ElementLayout;->isNeedOvewflowLayout:Z

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementLayout;->getView()Landroid/view/View;

    move-result-object v0

    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/layouts/ElementLayout;->isNeedOvewflowLayout:Z

    if-eqz v1, :cond_25

    new-instance v1, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementLayout;->getContext()Landroid/content/Context;

    move-result-object v2

    invoke-direct {v1, v2}, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;-><init>(Landroid/content/Context;)V

    iput-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/ElementLayout;->overflowLayout:Landroid/view/ViewGroup;

    :cond_25
    if-eqz v0, :cond_47

    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/layouts/ElementLayout;->isNeedOvewflowLayout:Z

    if-eqz v1, :cond_36

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/ElementLayout;->overflowLayout:Landroid/view/ViewGroup;

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementLayout;->getViewLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v2

    invoke-virtual {v1, v0, v2}, Landroid/view/ViewGroup;->addView(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/ElementLayout;->overflowLayout:Landroid/view/ViewGroup;

    :cond_36
    const/4 v1, -0x1

    iget-boolean v2, p0, Lcom/android/systemui/newstatusbar/layouts/ElementLayout;->isNeedOvewflowLayout:Z

    if-eqz v2, :cond_40

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementLayout;->getContainerLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v2

    goto :goto_44

    :cond_40
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementLayout;->getViewLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v2

    :goto_44
    invoke-super {p0, v0, v1, v2}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->addView(Landroid/view/View;ILandroid/view/ViewGroup$LayoutParams;)V

    :cond_47
    return-void
.end method

.method private isNotif()Z
    .registers 4

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementLayout;->getId()I

    move-result v0

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementLayout;->getContext()Landroid/content/Context;

    move-result-object v1

    const-string v2, "fullscreen_notification_icon_area"

    invoke-static {v1, v2}, Landroid/Utils/Utils;->IDtoID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v1

    if-ne v0, v1, :cond_12

    const/4 v0, 0x1

    goto :goto_13

    :cond_12
    const/4 v0, 0x0

    :goto_13
    return v0
.end method

.method private isStatus()Z
    .registers 4

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementLayout;->getId()I

    move-result v0

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementLayout;->getContext()Landroid/content/Context;

    move-result-object v1

    const-string v2, "elem_status"

    invoke-static {v1, v2}, Landroid/Utils/Utils;->IDtoID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v1

    if-ne v0, v1, :cond_12

    const/4 v0, 0x1

    goto :goto_13

    :cond_12
    const/4 v0, 0x0

    :goto_13
    return v0
.end method


# virtual methods
.method public addView(Landroid/view/View;ILandroid/view/ViewGroup$LayoutParams;)V
    .registers 5

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/ElementLayout;->overflowLayout:Landroid/view/ViewGroup;

    if-eqz v0, :cond_8

    invoke-virtual {v0, p1, p2, p3}, Landroid/view/ViewGroup;->addView(Landroid/view/View;ILandroid/view/ViewGroup$LayoutParams;)V

    return-void

    :cond_8
    invoke-super {p0, p1, p2, p3}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->addView(Landroid/view/View;ILandroid/view/ViewGroup$LayoutParams;)V

    return-void
.end method

.method getContainerLayoutParams()Landroid/view/ViewGroup$LayoutParams;
    .registers 4

    goto/32 :goto_22

    nop

    :goto_4
    iput v1, v0, Landroid/widget/LinearLayout$LayoutParams;->gravity:I

    goto/32 :goto_15

    nop

    :goto_a
    const/16 v1, 0x10

    goto/32 :goto_4

    nop

    :goto_10
    const/4 v1, -0x2

    goto/32 :goto_16

    nop

    :goto_15
    return-object v0

    :goto_16
    const/4 v2, -0x1

    goto/32 :goto_1b

    nop

    :goto_1b
    invoke-direct {v0, v1, v2}, Landroid/widget/LinearLayout$LayoutParams;-><init>(II)V

    goto/32 :goto_a

    nop

    :goto_22
    new-instance v0, Landroid/widget/LinearLayout$LayoutParams;

    goto/32 :goto_10

    nop
.end method

.method abstract getView()Landroid/view/View;
.end method

.method getViewLayoutParams()Landroid/view/ViewGroup$LayoutParams;
    .registers 3

    goto/32 :goto_2d

    nop

    :goto_4
    const/16 v1, 0x10

    goto/32 :goto_a

    nop

    :goto_a
    iput v1, v0, Landroid/widget/LinearLayout$LayoutParams;->gravity:I

    goto/32 :goto_33

    nop

    :goto_10
    invoke-direct {v0, v1, v1}, Landroid/widget/LinearLayout$LayoutParams;-><init>(II)V

    goto/32 :goto_22

    nop

    :goto_17
    const/4 v1, -0x2

    goto/32 :goto_10

    nop

    :goto_1c
    iput v1, v0, Landroid/widget/LinearLayout$LayoutParams;->rightMargin:I

    goto/32 :goto_4

    nop

    :goto_22
    const/4 v1, 0x3

    goto/32 :goto_27

    nop

    :goto_27
    iput v1, v0, Landroid/widget/LinearLayout$LayoutParams;->leftMargin:I

    goto/32 :goto_1c

    nop

    :goto_2d
    new-instance v0, Landroid/widget/LinearLayout$LayoutParams;

    goto/32 :goto_17

    nop

    :goto_33
    return-object v0
.end method

.method protected onLayout(ZIIII)V
    .registers 7

    goto/32 :goto_2a

    nop

    :goto_4
    if-eqz v0, :cond_9

    goto/32 :goto_15

    :cond_9
    goto/32 :goto_55

    nop

    :goto_d
    invoke-super {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->setVisibility(I)V

    goto/32 :goto_14

    nop

    :goto_14
    goto :goto_39

    :goto_15
    goto/32 :goto_36

    nop

    :goto_19
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementLayout;->isVisibleByPlaceCalculation()Z

    move-result v0

    goto/32 :goto_4

    nop

    :goto_21
    if-nez v0, :cond_26

    goto/32 :goto_15

    :cond_26
    goto/32 :goto_31

    nop

    :goto_2a
    invoke-super/range {p0 .. p5}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->onLayout(ZIIII)V

    goto/32 :goto_46

    nop

    :goto_31
    const/4 v0, 0x4

    goto/32 :goto_d

    nop

    :goto_36
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementLayout;->updateVisibility()V

    :goto_39
    goto/32 :goto_63

    nop

    :goto_3d
    if-eqz v0, :cond_42

    goto/32 :goto_15

    :cond_42
    :goto_42
    goto/32 :goto_19

    nop

    :goto_46
    sub-int v0, p5, p3

    goto/32 :goto_4c

    nop

    :goto_4c
    if-nez v0, :cond_51

    goto/32 :goto_42

    :cond_51
    goto/32 :goto_5d

    nop

    :goto_55
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementLayout;->getPosition()I

    move-result v0

    goto/32 :goto_21

    nop

    :goto_5d
    sub-int v0, p4, p2

    goto/32 :goto_3d

    nop

    :goto_63
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_layouts_ElementLayout',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
