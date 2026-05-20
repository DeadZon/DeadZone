"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/layouts/ControlCenterStatusBar.smali'
CLASS_FALLBACK_NAMES = ['ControlCenterStatusBar.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/layouts/ControlCenterStatusBar;
.super Lcom/android/keyguard/AlphaOptimizedLinearLayout;


# instance fields
.field private final controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 3

    invoke-direct {p0, p1}, Lcom/android/keyguard/AlphaOptimizedLinearLayout;-><init>(Landroid/content/Context;)V

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/ControlCenterStatusBar;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 4

    invoke-direct {p0, p1, p2}, Lcom/android/keyguard/AlphaOptimizedLinearLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/ControlCenterStatusBar;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 5

    invoke-direct {p0, p1, p2, p3}, Lcom/android/keyguard/AlphaOptimizedLinearLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/ControlCenterStatusBar;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V
    .registers 6

    invoke-direct {p0, p1, p2, p3, p4}, Lcom/android/keyguard/AlphaOptimizedLinearLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/ControlCenterStatusBar;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    return-void
.end method


# virtual methods
.method protected onFinishInflate()V
    .registers 4

    goto/32 :goto_40

    nop

    :goto_4
    new-instance v1, Ljava/util/ArrayList;

    goto/32 :goto_2e

    nop

    :goto_a
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/ControlCenterStatusBar;->getContext()Landroid/content/Context;

    move-result-object v0

    goto/32 :goto_35

    nop

    :goto_12
    check-cast v2, Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer;

    goto/32 :goto_50

    nop

    :goto_18
    invoke-static {v0, v1}, Landroid/Utils/Utils;->IDtoID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v0

    goto/32 :goto_20

    nop

    :goto_20
    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/ControlCenterStatusBar;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto/32 :goto_28

    nop

    :goto_28
    instance-of v1, v0, Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer;

    goto/32 :goto_47

    nop

    :goto_2e
    invoke-direct {v1}, Ljava/util/ArrayList;-><init>()V

    goto/32 :goto_3b

    nop

    :goto_35
    const-string v1, "statusIcons"

    goto/32 :goto_18

    nop

    :goto_3b
    move-object v2, v0

    goto/32 :goto_12

    nop

    :goto_40
    invoke-super {p0}, Lcom/android/keyguard/AlphaOptimizedLinearLayout;->onFinishInflate()V

    goto/32 :goto_a

    nop

    :goto_47
    if-nez v1, :cond_4c

    goto/32 :goto_53

    :cond_4c
    goto/32 :goto_4

    nop

    :goto_50
    invoke-virtual {v2, v1}, Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer;->addIgnoredSlots(Ljava/util/List;)V

    :goto_53
    goto/32 :goto_57

    nop

    :goto_57
    return-void
.end method

.method protected onMeasure(II)V
    .registers 5

    goto/32 :goto_1b

    nop

    :goto_4
    return-void

    :goto_5
    invoke-virtual {p0, v0, v1}, Lcom/android/systemui/newstatusbar/layouts/ControlCenterStatusBar;->setMeasuredDimension(II)V

    :goto_8
    goto/32 :goto_4

    nop

    :goto_c
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/ControlCenterStatusBar;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    goto/32 :goto_12

    nop

    :goto_12
    if-nez v0, :cond_17

    goto/32 :goto_8

    :cond_17
    goto/32 :goto_28

    nop

    :goto_1b
    invoke-super {p0, p1, p2}, Lcom/android/keyguard/AlphaOptimizedLinearLayout;->onMeasure(II)V

    goto/32 :goto_c

    nop

    :goto_22
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/ControlCenterStatusBar;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    goto/32 :goto_30

    nop

    :goto_28
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/ControlCenterStatusBar;->getMeasuredWidth()I

    move-result v0

    goto/32 :goto_22

    nop

    :goto_30
    iget v1, v1, Lcom/android/systemui/newstatusbar/controllers/ElementController;->statusBarHeight:I

    goto/32 :goto_5

    nop
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_layouts_ControlCenterStatusBar',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
