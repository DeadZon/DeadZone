"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/layouts/ControlCenterStatusBarIcon.smali'
CLASS_FALLBACK_NAMES = ['ControlCenterStatusBarIcon.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/layouts/ControlCenterStatusBarIcon;
.super Lcom/android/systemui/controlcenter/phone/widget/ControlCenterStatusBarIcon;


# instance fields
.field private child:Landroid/view/ViewGroup;

.field private final controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;

.field private statusIcons:Landroid/view/ViewGroup;


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 4

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/controlcenter/phone/widget/ControlCenterStatusBarIcon;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/ControlCenterStatusBarIcon;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/ControlCenterStatusBarIcon;->setClipChildren(Z)V

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/ControlCenterStatusBarIcon;->setClipToPadding(Z)V

    return-void
.end method


# virtual methods
.method protected onFinishInflate()V
    .registers 4

    goto/32 :goto_33

    nop

    :goto_4
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/ControlCenterStatusBarIcon;->getContext()Landroid/content/Context;

    move-result-object v1

    goto/32 :goto_57

    nop

    :goto_c
    iput-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/ControlCenterStatusBarIcon;->statusIcons:Landroid/view/ViewGroup;

    goto/32 :goto_70

    nop

    :goto_12
    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/ControlCenterStatusBarIcon;->getChildAt(I)Landroid/view/View;

    move-result-object v1

    goto/32 :goto_63

    nop

    :goto_1a
    invoke-virtual {v1, v0}, Landroid/view/ViewGroup;->setClipToPadding(Z)V

    goto/32 :goto_4

    nop

    :goto_21
    invoke-virtual {v1, v0}, Landroid/view/ViewGroup;->setClipChildren(Z)V

    goto/32 :goto_4e

    nop

    :goto_28
    const/4 v0, 0x0

    goto/32 :goto_12

    nop

    :goto_2d
    iput-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/ControlCenterStatusBarIcon;->child:Landroid/view/ViewGroup;

    goto/32 :goto_69

    nop

    :goto_33
    invoke-super {p0}, Lcom/android/systemui/controlcenter/phone/widget/ControlCenterStatusBarIcon;->onFinishInflate()V

    goto/32 :goto_28

    nop

    :goto_3a
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/ControlCenterStatusBarIcon;->statusIcons:Landroid/view/ViewGroup;

    goto/32 :goto_21

    nop

    :goto_40
    check-cast v1, Landroid/view/ViewGroup;

    goto/32 :goto_c

    nop

    :goto_46
    invoke-virtual {p0, v1}, Lcom/android/systemui/newstatusbar/layouts/ControlCenterStatusBarIcon;->findViewById(I)Landroid/view/View;

    move-result-object v1

    goto/32 :goto_40

    nop

    :goto_4e
    return-void

    :goto_4f
    invoke-static {v1, v2}, Landroid/Utils/Utils;->IDtoID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v1

    goto/32 :goto_46

    nop

    :goto_57
    const-string v2, "statusIcons"

    goto/32 :goto_4f

    nop

    :goto_5d
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/ControlCenterStatusBarIcon;->child:Landroid/view/ViewGroup;

    goto/32 :goto_1a

    nop

    :goto_63
    check-cast v1, Landroid/view/ViewGroup;

    goto/32 :goto_2d

    nop

    :goto_69
    invoke-virtual {v1, v0}, Landroid/view/ViewGroup;->setClipChildren(Z)V

    goto/32 :goto_5d

    nop

    :goto_70
    invoke-virtual {v1, v0}, Landroid/view/ViewGroup;->setClipToPadding(Z)V

    goto/32 :goto_3a

    nop
.end method

.method protected onMeasure(II)V
    .registers 8

    goto/32 :goto_8b

    nop

    :goto_4
    invoke-virtual {v1, v3, v4}, Landroid/view/ViewGroup;->measure(II)V

    :goto_7
    goto/32 :goto_29

    nop

    :goto_b
    invoke-static {v0, v2}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v4

    goto/32 :goto_4

    nop

    :goto_13
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/ControlCenterStatusBarIcon;->getMeasuredWidth()I

    move-result v1

    goto/32 :goto_76

    nop

    :goto_1b
    iget v0, v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->statusBarHeight:I

    goto/32 :goto_38

    nop

    :goto_21
    invoke-static {v0, v2}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v2

    goto/32 :goto_67

    nop

    :goto_29
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/ControlCenterStatusBarIcon;->statusIcons:Landroid/view/ViewGroup;

    goto/32 :goto_2f

    nop

    :goto_2f
    if-nez v1, :cond_34

    goto/32 :goto_6a

    :cond_34
    goto/32 :goto_6e

    nop

    :goto_38
    if-gtz v0, :cond_3d

    goto/32 :goto_6a

    :cond_3d
    goto/32 :goto_13

    nop

    :goto_41
    if-nez v1, :cond_46

    goto/32 :goto_7

    :cond_46
    goto/32 :goto_50

    nop

    :goto_4a
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/ControlCenterStatusBarIcon;->child:Landroid/view/ViewGroup;

    goto/32 :goto_7d

    nop

    :goto_50
    invoke-virtual {v1}, Landroid/view/ViewGroup;->getMeasuredWidth()I

    move-result v3

    goto/32 :goto_83

    nop

    :goto_58
    return-void

    :goto_59
    invoke-static {v3, v2}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v3

    goto/32 :goto_21

    nop

    :goto_61
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/ControlCenterStatusBarIcon;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    goto/32 :goto_1b

    nop

    :goto_67
    invoke-virtual {v1, v3, v2}, Landroid/view/ViewGroup;->measure(II)V

    :goto_6a
    goto/32 :goto_58

    nop

    :goto_6e
    invoke-virtual {v1}, Landroid/view/ViewGroup;->getMeasuredWidth()I

    move-result v3

    goto/32 :goto_59

    nop

    :goto_76
    invoke-virtual {p0, v1, v0}, Lcom/android/systemui/newstatusbar/layouts/ControlCenterStatusBarIcon;->setMeasuredDimension(II)V

    goto/32 :goto_4a

    nop

    :goto_7d
    const/high16 v2, 0x40000000  # 2.0f

    goto/32 :goto_41

    nop

    :goto_83
    invoke-static {v3, v2}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v3

    goto/32 :goto_b

    nop

    :goto_8b
    invoke-super {p0, p1, p2}, Lcom/android/systemui/controlcenter/phone/widget/ControlCenterStatusBarIcon;->onMeasure(II)V

    goto/32 :goto_61

    nop
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_layouts_ControlCenterStatusBarIcon',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
