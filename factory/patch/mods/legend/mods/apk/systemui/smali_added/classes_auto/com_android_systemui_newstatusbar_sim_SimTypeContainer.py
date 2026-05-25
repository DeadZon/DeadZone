"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/sim/SimTypeContainer.smali'
CLASS_FALLBACK_NAMES = ['SimTypeContainer.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;
.super Landroid/widget/FrameLayout;

# interfaces
.implements Lcom/android/systemui/newstatusbar/controllers/SimTypePositionController$CallBack;
.implements Lcom/android/systemui/statusbar/policy/ConfigurationController$ConfigurationListener;


# static fields
.field private static final TAG:Ljava/lang/String; = "Nastya"


# instance fields
.field private final controller:Lcom/android/systemui/newstatusbar/controllers/SimTypePositionController;

.field private inOut:Landroid/view/View;

.field public isHorizontal:Z

.field private isStatusBar:Z

.field private mobileView:Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;

.field private final requestRunable:Ljava/lang/Runnable;

.field private simType:Landroid/view/View;


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 5
    .param p1  # Landroid/content/Context;
        .annotation build Landroidx/annotation/NonNull;
        .end annotation
    .end param
    .param p2  # Landroid/util/AttributeSet;
        .annotation build Landroidx/annotation/Nullable;
        .end annotation
    .end param

    const/4 v1, 0x0

    invoke-direct {p0, p1, p2}, Landroid/widget/FrameLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/SimTypePositionController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/SimTypePositionController;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->controller:Lcom/android/systemui/newstatusbar/controllers/SimTypePositionController;

    iput-boolean v1, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->isStatusBar:Z

    new-instance v0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer$1;

    invoke-direct {v0, p0}, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer$1;-><init>(Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;)V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->requestRunable:Ljava/lang/Runnable;

    invoke-virtual {p0, v1}, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->setClipChildren(Z)V

    invoke-virtual {p0, v1}, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->setClipToPadding(Z)V

    return-void
.end method

.method private updateMargin()V
    .registers 3

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v0

    check-cast v0, Landroid/view/ViewGroup$MarginLayoutParams;

    const-string v1, "sim_type_margin"

    invoke-static {v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v1

    iput v1, v0, Landroid/view/ViewGroup$MarginLayoutParams;->rightMargin:I

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    return-void
.end method


# virtual methods
.method public getInOut()Landroid/view/View;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->inOut:Landroid/view/View;

    return-object v0
.end method

.method protected onAttachedToWindow()V
    .registers 2

    goto/32 :goto_1f

    nop

    :goto_4
    invoke-static {v0}, Lcom/android/systemui/SysDependency;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    goto/32 :goto_2e

    nop

    :goto_c
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->controller:Lcom/android/systemui/newstatusbar/controllers/SimTypePositionController;

    goto/32 :goto_26

    nop

    :goto_12
    const-class v0, Lcom/android/systemui/statusbar/policy/ConfigurationController;

    goto/32 :goto_4

    nop

    :goto_18
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->onPositionChange()V

    goto/32 :goto_2d

    nop

    :goto_1f
    invoke-super {p0}, Landroid/widget/FrameLayout;->onAttachedToWindow()V

    goto/32 :goto_c

    nop

    :goto_26
    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/SimTypePositionController;->addCallBack(Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;)V

    goto/32 :goto_12

    nop

    :goto_2d
    return-void

    :goto_2e
    check-cast v0, Lcom/android/systemui/statusbar/policy/ConfigurationController;

    goto/32 :goto_34

    nop

    :goto_34
    invoke-interface {v0, p0}, Lcom/android/systemui/statusbar/policy/ConfigurationController;->addCallback(Ljava/lang/Object;)V

    goto/32 :goto_18

    nop
.end method

.method public onConfigChanged(Landroid/content/res/Configuration;)V
    .registers 3

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v0

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    return-void
.end method

.method protected onDetachedFromWindow()V
    .registers 2

    goto/32 :goto_b

    nop

    :goto_4
    return-void

    :goto_5
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->controller:Lcom/android/systemui/newstatusbar/controllers/SimTypePositionController;

    goto/32 :goto_12

    nop

    :goto_b
    invoke-super {p0}, Landroid/widget/FrameLayout;->onDetachedFromWindow()V

    goto/32 :goto_5

    nop

    :goto_12
    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/SimTypePositionController;->removeCallBack(Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;)V

    goto/32 :goto_4

    nop
.end method

.method protected onFinishInflate()V
    .registers 2

    goto/32 :goto_c

    nop

    :goto_4
    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->getChildAt(I)Landroid/view/View;

    move-result-object v0

    goto/32 :goto_26

    nop

    :goto_c
    invoke-super {p0}, Landroid/widget/FrameLayout;->onFinishInflate()V

    goto/32 :goto_1b

    nop

    :goto_13
    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->getChildAt(I)Landroid/view/View;

    move-result-object v0

    goto/32 :goto_20

    nop

    :goto_1b
    const/4 v0, 0x0

    goto/32 :goto_13

    nop

    :goto_20
    iput-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->simType:Landroid/view/View;

    goto/32 :goto_2c

    nop

    :goto_26
    iput-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->inOut:Landroid/view/View;

    goto/32 :goto_31

    nop

    :goto_2c
    const/4 v0, 0x1

    goto/32 :goto_4

    nop

    :goto_31
    return-void
.end method

.method protected onLayout(ZIIII)V
    .registers 14

    goto/32 :goto_d

    nop

    :goto_4
    if-nez v5, :cond_9

    goto/32 :goto_9f

    :cond_9
    goto/32 :goto_42

    nop

    :goto_d
    const/4 v7, 0x0

    goto/32 :goto_b5

    nop

    :goto_12
    invoke-virtual {v5, v7, v2, v4, v6}, Landroid/view/View;->layout(IIII)V

    goto/32 :goto_73

    nop

    :goto_19
    iget-object v5, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->simType:Landroid/view/View;

    goto/32 :goto_50

    nop

    :goto_1f
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->getMeasuredHeight()I

    move-result v0

    goto/32 :goto_a3

    nop

    :goto_27
    div-int/lit8 v2, v6, 0x2

    goto/32 :goto_af

    nop

    :goto_2d
    invoke-virtual {v5, v4, v7, v6, v0}, Landroid/view/View;->layout(IIII)V

    :goto_30
    goto/32 :goto_9e

    nop

    :goto_34
    invoke-virtual {v5}, Landroid/view/View;->getMeasuredWidth()I

    move-result v5

    goto/32 :goto_8f

    nop

    :goto_3c
    iget-boolean v5, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->isHorizontal:Z

    goto/32 :goto_4

    nop

    :goto_42
    iget-object v5, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->simType:Landroid/view/View;

    goto/32 :goto_98

    nop

    :goto_48
    invoke-virtual {v5}, Landroid/view/View;->getMeasuredWidth()I

    move-result v4

    goto/32 :goto_19

    nop

    :goto_50
    invoke-virtual {v5}, Landroid/view/View;->getMeasuredHeight()I

    move-result v1

    goto/32 :goto_1f

    nop

    :goto_58
    add-int v6, v4, v3

    goto/32 :goto_2d

    nop

    :goto_5e
    iget-object v5, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->simType:Landroid/view/View;

    goto/32 :goto_bb

    nop

    :goto_64
    iget-object v5, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->inOut:Landroid/view/View;

    goto/32 :goto_88

    nop

    :goto_6a
    if-nez v5, :cond_6f

    goto/32 :goto_30

    :cond_6f
    goto/32 :goto_82

    nop

    :goto_73
    iget-object v5, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->inOut:Landroid/view/View;

    goto/32 :goto_58

    nop

    :goto_79
    goto :goto_30

    :goto_7a
    invoke-virtual {v5}, Landroid/view/View;->getMeasuredWidth()I

    move-result v3

    goto/32 :goto_3c

    nop

    :goto_82
    iget-object v5, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->simType:Landroid/view/View;

    goto/32 :goto_34

    nop

    :goto_88
    invoke-virtual {v5, v7, v7, v3, v0}, Landroid/view/View;->layout(IIII)V

    goto/32 :goto_79

    nop

    :goto_8f
    if-gtz v5, :cond_94

    goto/32 :goto_30

    :cond_94
    goto/32 :goto_a9

    nop

    :goto_98
    sub-int v6, v0, v1

    goto/32 :goto_27

    nop

    :goto_9e
    return-void

    :goto_9f
    goto/32 :goto_5e

    nop

    :goto_a3
    iget-object v5, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->inOut:Landroid/view/View;

    goto/32 :goto_7a

    nop

    :goto_a9
    iget-object v5, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->simType:Landroid/view/View;

    goto/32 :goto_48

    nop

    :goto_af
    add-int v6, v2, v1

    goto/32 :goto_12

    nop

    :goto_b5
    iget-object v5, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->simType:Landroid/view/View;

    goto/32 :goto_6a

    nop

    :goto_bb
    invoke-virtual {v5, v7, v7, v4, v1}, Landroid/view/View;->layout(IIII)V

    goto/32 :goto_64

    nop
.end method

.method protected onMeasure(II)V
    .registers 9

    goto/32 :goto_91

    nop

    :goto_4
    if-nez v2, :cond_9

    goto/32 :goto_1f

    :cond_9
    goto/32 :goto_57

    nop

    :goto_d
    invoke-virtual {v3}, Landroid/view/View;->getMeasuredHeight()I

    move-result v3

    goto/32 :goto_dc

    nop

    :goto_15
    if-eqz v2, :cond_1a

    goto/32 :goto_9f

    :cond_1a
    goto/32 :goto_f7

    nop

    :goto_1e
    goto :goto_64

    :goto_1f
    goto/32 :goto_10f

    nop

    :goto_23
    const-wide/16 v4, 0x64

    goto/32 :goto_ab

    nop

    :goto_29
    iget-boolean v2, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->isHorizontal:Z

    goto/32 :goto_fd

    nop

    :goto_2f
    invoke-virtual {v3}, Landroid/view/View;->getMeasuredHeight()I

    move-result v3

    goto/32 :goto_115

    nop

    :goto_37
    goto :goto_53

    :goto_38
    if-nez v2, :cond_3d

    goto/32 :goto_ed

    :cond_3d
    goto/32 :goto_63

    nop

    :goto_41
    iget-boolean v2, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->isHorizontal:Z

    goto/32 :goto_38

    nop

    :goto_47
    if-gtz v2, :cond_4c

    goto/32 :goto_1f

    :cond_4c
    goto/32 :goto_98

    nop

    :goto_50
    invoke-virtual {p0, v1, v0}, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->setMeasuredDimension(II)V

    :goto_53
    goto/32 :goto_ec

    nop

    :goto_57
    iget-object v2, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->simType:Landroid/view/View;

    goto/32 :goto_89

    nop

    :goto_5d
    iget-object v3, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->simType:Landroid/view/View;

    goto/32 :goto_d

    nop

    :goto_63
    const/4 v2, 0x1

    :goto_64
    goto/32 :goto_5d

    nop

    :goto_68
    iget-object v2, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->inOut:Landroid/view/View;

    goto/32 :goto_a3

    nop

    :goto_6e
    invoke-virtual {v2}, Landroid/view/View;->getMeasuredWidth()I

    move-result v1

    goto/32 :goto_c8

    nop

    :goto_76
    iget-object v3, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->inOut:Landroid/view/View;

    goto/32 :goto_2f

    nop

    :goto_7c
    invoke-virtual {v2}, Landroid/view/View;->getHeight()I

    move-result v2

    goto/32 :goto_106

    nop

    :goto_84
    const/4 v2, 0x2

    goto/32 :goto_1e

    nop

    :goto_89
    invoke-virtual {v2}, Landroid/view/View;->getWidth()I

    move-result v2

    goto/32 :goto_47

    nop

    :goto_91
    invoke-super {p0, p1, p2}, Landroid/widget/FrameLayout;->onMeasure(II)V

    goto/32 :goto_c2

    nop

    :goto_98
    iget-object v2, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->simType:Landroid/view/View;

    goto/32 :goto_7c

    nop

    :goto_9e
    float-to-int v1, v2

    :goto_9f
    goto/32 :goto_29

    nop

    :goto_a3
    invoke-virtual {v2}, Landroid/view/View;->getMeasuredWidth()I

    move-result v2

    goto/32 :goto_e1

    nop

    :goto_ab
    invoke-virtual {p0, v2, v4, v5}, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->postDelayed(Ljava/lang/Runnable;J)Z

    goto/32 :goto_37

    nop

    :goto_b2
    if-nez v2, :cond_b7

    goto/32 :goto_9f

    :cond_b7
    goto/32 :goto_f1

    nop

    :goto_bb
    invoke-virtual {p0, v2}, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->removeCallbacks(Ljava/lang/Runnable;)Z

    goto/32 :goto_e6

    nop

    :goto_c2
    iget-object v2, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->requestRunable:Ljava/lang/Runnable;

    goto/32 :goto_bb

    nop

    :goto_c8
    iget-boolean v2, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->isHorizontal:Z

    goto/32 :goto_15

    nop

    :goto_ce
    iget-object v2, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->simType:Landroid/view/View;

    goto/32 :goto_6e

    nop

    :goto_d4
    invoke-virtual {v2}, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->getTextInPaint()F

    move-result v2

    goto/32 :goto_9e

    nop

    :goto_dc
    mul-int/2addr v2, v3

    goto/32 :goto_76

    nop

    :goto_e1
    add-int/2addr v1, v2

    :goto_e2
    goto/32 :goto_50

    nop

    :goto_e6
    iget-object v2, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->simType:Landroid/view/View;

    goto/32 :goto_4

    nop

    :goto_ec
    return-void

    :goto_ed
    goto/32 :goto_84

    nop

    :goto_f1
    iget-object v2, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->mobileView:Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;

    goto/32 :goto_d4

    nop

    :goto_f7
    iget-object v2, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->mobileView:Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;

    goto/32 :goto_b2

    nop

    :goto_fd
    if-nez v2, :cond_102

    goto/32 :goto_e2

    :cond_102
    goto/32 :goto_68

    nop

    :goto_106
    if-gtz v2, :cond_10b

    goto/32 :goto_1f

    :cond_10b
    goto/32 :goto_41

    nop

    :goto_10f
    iget-object v2, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->requestRunable:Ljava/lang/Runnable;

    goto/32 :goto_23

    nop

    :goto_115
    invoke-static {v2, v3}, Ljava/lang/Math;->max(II)I

    move-result v0

    goto/32 :goto_ce

    nop
.end method

.method public onMiuiThemeChanged(Z)V
    .registers 2

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->requestLayout()V

    return-void
.end method

.method public onPositionChange()V
    .registers 2

    const-string v0, "sim_type_position"

    invoke-static {v0}, Landroid/preference/SettingsMezoHelper;->getBoolofSettings(Ljava/lang/String;)Z

    move-result v0

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->isHorizontal:Z

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->updateMargin()V

    return-void
.end method

.method protected onSizeChanged(IIII)V
    .registers 5

    goto/32 :goto_4

    nop

    :goto_4
    invoke-super {p0, p1, p2, p3, p4}, Landroid/widget/FrameLayout;->onSizeChanged(IIII)V

    goto/32 :goto_c

    nop

    :goto_b
    return-void

    :goto_c
    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->updateMargin()V

    goto/32 :goto_b

    nop
.end method

.method public setIsStatusBar()V
    .registers 2

    const/4 v0, 0x1

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->isStatusBar:Z

    return-void
.end method

.method public setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V
    .registers 4

    const/16 v1, 0x10

    instance-of v0, p1, Landroid/widget/LinearLayout$LayoutParams;

    if-eqz v0, :cond_1a

    move-object v0, p1

    check-cast v0, Landroid/widget/LinearLayout$LayoutParams;

    iput v1, v0, Landroid/widget/LinearLayout$LayoutParams;->gravity:I

    :cond_b
    :goto_b
    move-object v0, p1

    check-cast v0, Landroid/view/ViewGroup$MarginLayoutParams;

    const-string v1, "sim_type_margin"

    invoke-static {v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v1

    iput v1, v0, Landroid/view/ViewGroup$MarginLayoutParams;->rightMargin:I

    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    return-void

    :cond_1a
    instance-of v0, p1, Landroid/widget/FrameLayout$LayoutParams;

    if-eqz v0, :cond_b

    move-object v0, p1

    check-cast v0, Landroid/widget/FrameLayout$LayoutParams;

    iput v1, v0, Landroid/widget/FrameLayout$LayoutParams;->gravity:I

    goto :goto_b
.end method

.method public setMobileView(Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;)V
    .registers 2

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->mobileView:Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->onPositionChange()V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_sim_SimTypeContainer',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
