"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/layouts/NotificationIconContainer.smali'
CLASS_FALLBACK_NAMES = ['NotificationIconContainer.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;
.super Lcom/android/systemui/statusbar/phone/NotificationIconContainer;

# interfaces
.implements Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;


# static fields
.field private static TAG_ANIMATOR_TRANSLATION_Z:I


# instance fields
.field private final controller:Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;

.field private curIconSize:I

.field private mDimenPadding:I

.field private mDimenWidth:I

.field private realHeight:I


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 4

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/statusbar/phone/NotificationIconContainer;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->controller:Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/ElementController;->setNotificationIconContainer(Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;)V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->initDimens()V

    const/4 v0, 0x0

    invoke-virtual {p0, v0, v0, v0, v0}, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->setPadding(IIII)V

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->setWillNotDraw(Z)V

    invoke-virtual {p0, v0, v0, v0, v0}, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->setPaddingRelative(IIII)V

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->setClipChildren(Z)V

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->setClipToPadding(Z)V

    const-string v0, "translation_z_animator_tag"

    invoke-static {p1, v0}, Landroid/Utils/Utils;->IDtoID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v0

    sput v0, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->TAG_ANIMATOR_TRANSLATION_Z:I

    return-void
.end method


# virtual methods
.method public getActualPaddingEnd()F
    .registers 3

    iget v0, p0, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->mActualPaddingEnd:F

    const/high16 v1, -0x31000000

    cmpl-float v1, v0, v1

    if-nez v1, :cond_e

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->getPaddingEnd()I

    move-result v1

    int-to-float v1, v1

    goto :goto_f

    :cond_e
    move v1, v0

    :goto_f
    return v1
.end method

.method public getActualPaddingStart()F
    .registers 3

    iget v0, p0, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->mActualPaddingStart:F

    const/high16 v1, -0x31000000

    cmpl-float v1, v0, v1

    if-nez v1, :cond_e

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->getPaddingStart()I

    move-result v1

    int-to-float v1, v1

    goto :goto_f

    :cond_e
    move v1, v0

    :goto_f
    return v1
.end method

.method public getActualWidth()I
    .registers 3

    iget v0, p0, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->mActualLayoutWidth:I

    const/high16 v1, -0x80000000

    if-ne v0, v1, :cond_b

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->getWidth()I

    move-result v1

    goto :goto_c

    :cond_b
    move v1, v0

    :goto_c
    return v1
.end method

.method public initDimens()V
    .registers 7

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    iget v1, v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->statusBarHeight:I

    if-lez v1, :cond_1c

    iput v1, p0, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->realHeight:I

    iget-object v2, v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    invoke-virtual {v2}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->isOneLineBar()Z

    move-result v2

    if-eqz v2, :cond_1c

    iget v2, p0, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->realHeight:I

    div-int/lit8 v2, v2, 0x2

    iput v2, p0, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->realHeight:I

    :cond_1c
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->getResources()Landroid/content/res/Resources;

    move-result-object v2

    const-string v3, "status_bar_icon_height"

    const-string v4, "dimen"

    const-string v5, "com.android.systemui"

    invoke-virtual {v2, v3, v4, v5}, Landroid/content/res/Resources;->getIdentifier(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)I

    move-result v3

    invoke-virtual {v2, v3}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I

    move-result v3

    iput v3, p0, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->mDimenWidth:I

    const-string v3, "status_bar_notification_padding_end"

    invoke-virtual {v2, v3, v4, v5}, Landroid/content/res/Resources;->getIdentifier(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)I

    move-result v3

    invoke-virtual {v2, v3}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I

    move-result v3

    iput v3, p0, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->mDimenPadding:I

    const/4 v3, 0x0

    invoke-virtual {p0, v3}, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->setActualPaddingEnd(F)V

    invoke-virtual {p0, v3}, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->setActualPaddingStart(F)V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->requestLayout()V

    return-void
.end method

.method public isLayoutRtl()Z
    .registers 3

    const-string v0, "reverse_notification_sorting_order"

    const/4 v1, 0x1

    invoke-static {v0, v1}, Landroid/preference/SettingsMezoHelper;->getBoolofSettings(Ljava/lang/String;I)Z

    move-result v0

    return v0
.end method

.method public onAttachedToWindow()V
    .registers 3

    invoke-super {p0}, Lcom/android/systemui/statusbar/phone/NotificationIconContainer;->onAttachedToWindow()V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->controller:Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;

    const/4 v1, 0x0

    invoke-virtual {v0, p0, v1}, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;->addCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;Z)V

    return-void
.end method

.method public onDetachedFromWindow()V
    .registers 3

    invoke-super {p0}, Lcom/android/systemui/statusbar/phone/NotificationIconContainer;->onDetachedFromWindow()V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->controller:Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;

    const/4 v1, 0x0

    invoke-virtual {v0, p0, v1}, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;->removeCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;Z)V

    return-void
.end method

.method public onIconChange()V
    .registers 4

    iget v0, p0, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->mDimenWidth:I

    int-to-float v0, v0

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->controller:Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;

    const/4 v2, 0x0

    invoke-virtual {v1, v2}, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;->getCurrData(Z)Lcom/android/systemui/newstatusbar/data/IconData;

    move-result-object v1

    iget v1, v1, Lcom/android/systemui/newstatusbar/data/IconData;->zoom:I

    int-to-float v1, v1

    mul-float/2addr v0, v1

    const/high16 v1, 0x42c80000  # 100.0f

    div-float/2addr v0, v1

    float-to-int v0, v0

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->curIconSize:I

    const/4 v0, 0x0

    :goto_15
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->getChildCount()I

    move-result v1

    if-ge v0, v1, :cond_2c

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->getChildAt(I)Landroid/view/View;

    move-result-object v1

    instance-of v2, v1, Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;

    if-eqz v2, :cond_29

    move-object v2, v1

    check-cast v2, Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;

    invoke-interface {v2}, Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;->onIconChange()V

    :cond_29
    add-int/lit8 v0, v0, 0x1

    goto :goto_15

    :cond_2c
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->requestLayout()V

    return-void
.end method

.method public final onLayout(ZIIII)V
    .registers 14

    iget v0, p0, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->realHeight:I

    int-to-float v0, v0

    const/high16 v1, 0x40000000  # 2.0f

    div-float/2addr v0, v1

    const/4 v2, 0x0

    :goto_7
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->getChildCount()I

    move-result v3

    const/4 v4, 0x0

    if-ge v2, v3, :cond_27

    invoke-virtual {p0, v2}, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->getChildAt(I)Landroid/view/View;

    move-result-object v3

    iget v5, p0, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->curIconSize:I

    int-to-float v6, v5

    div-float/2addr v6, v1

    sub-float v6, v0, v6

    float-to-int v6, v6

    add-int v7, v6, v5

    invoke-virtual {v3, v4, v6, v5, v7}, Landroid/view/View;->layout(IIII)V

    if-nez v2, :cond_24

    iget v4, p0, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->curIconSize:I

    iput v4, p0, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->mIconSize:I

    :cond_24
    add-int/lit8 v2, v2, 0x1

    goto :goto_7

    :cond_27
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->mInject:Lcom/android/systemui/statusbar/phone/NotificationIconContainerInject;

    if-eqz p1, :cond_37

    iget-object v2, v1, Lcom/android/systemui/statusbar/phone/NotificationIconContainerInject;->_islandMonitor:Lcom/android/systemui/statusbar/IslandMonitor$RealContainerIslandMonitor;

    if-eqz v2, :cond_36

    iget-boolean v3, v2, Lcom/android/systemui/statusbar/IslandMonitor$RealContainerIslandMonitor;->islandShowing:Z

    if-eqz v3, :cond_36

    invoke-virtual {v2}, Lcom/android/systemui/statusbar/IslandMonitor$RealContainerIslandMonitor;->onLayoutChanged()V

    :cond_36
    goto :goto_3a

    :cond_37
    invoke-virtual {v1}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    :goto_3a
    iget-object v2, p0, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->mAbsolutePosition:[I

    invoke-virtual {p0, v2}, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->getLocationOnScreen([I)V

    iget-boolean v2, p0, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->mIsStaticLayout:Z

    if-eqz v2, :cond_4c

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->resetViewStates()V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->calculateIconXTranslations()V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->applyIconStates()V

    :cond_4c
    iput-boolean v4, v1, Lcom/android/systemui/statusbar/phone/NotificationIconContainerInject;->islandWidthChanged:Z

    const/4 v2, 0x1

    iput-boolean v2, v1, Lcom/android/systemui/statusbar/phone/NotificationIconContainerInject;->islandAnimate:Z

    return-void
.end method

.method protected onMeasure(II)V
    .registers 11

    goto/32 :goto_63

    nop

    :goto_4
    iput v7, v6, Landroid/view/ViewGroup$LayoutParams;->width:I

    goto/32 :goto_95

    nop

    :goto_a
    if-nez v6, :cond_f

    goto/32 :goto_9d

    :cond_f
    goto/32 :goto_5d

    nop

    :goto_13
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->getActualPaddingStart()F

    move-result v3

    goto/32 :goto_32

    nop

    :goto_1b
    iget v2, p0, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->curIconSize:I

    goto/32 :goto_2c

    nop

    :goto_21
    add-int/2addr v3, v7

    :goto_22
    goto/32 :goto_26

    nop

    :goto_26
    add-int/lit8 v4, v4, 0x1

    goto/32 :goto_a1

    nop

    :goto_2c
    const/high16 v3, 0x40000000  # 2.0f

    goto/32 :goto_8d

    nop

    :goto_32
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->getActualPaddingEnd()F

    move-result v4

    goto/32 :goto_af

    nop

    :goto_3a
    invoke-virtual {v5}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v6

    goto/32 :goto_a

    nop

    :goto_42
    iget v7, p0, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->curIconSize:I

    goto/32 :goto_21

    nop

    :goto_48
    iget v1, p0, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->mMaxIcons:I

    goto/32 :goto_1b

    nop

    :goto_4e
    invoke-virtual {p0, v3}, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->setActualLayoutWidth(I)V

    goto/32 :goto_b4

    nop

    :goto_55
    invoke-virtual {p0, v4}, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->getChildAt(I)Landroid/view/View;

    move-result-object v5

    goto/32 :goto_3a

    nop

    :goto_5d
    iget v7, p0, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->curIconSize:I

    goto/32 :goto_4

    nop

    :goto_63
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->getChildCount()I

    move-result v0

    goto/32 :goto_48

    nop

    :goto_6b
    const/4 v4, 0x0

    :goto_6c
    goto/32 :goto_a6

    nop

    :goto_70
    invoke-virtual {p0, v5, v2, v2}, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->measureChild(Landroid/view/View;II)V

    goto/32 :goto_7f

    nop

    :goto_77
    return-void

    :goto_78
    invoke-virtual {p0, v3, v4}, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->setMeasuredDimension(II)V

    goto/32 :goto_77

    nop

    :goto_7f
    if-lt v4, v1, :cond_84

    goto/32 :goto_22

    :cond_84
    goto/32 :goto_42

    nop

    :goto_88
    float-to-int v3, v3

    goto/32 :goto_6b

    nop

    :goto_8d
    invoke-static {v2, v3}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v2

    goto/32 :goto_13

    nop

    :goto_95
    iget v7, p0, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->curIconSize:I

    goto/32 :goto_9b

    nop

    :goto_9b
    iput v7, v6, Landroid/view/ViewGroup$LayoutParams;->height:I

    :goto_9d
    goto/32 :goto_70

    nop

    :goto_a1
    goto :goto_6c

    :goto_a2
    goto/32 :goto_4e

    nop

    :goto_a6
    if-lt v4, v0, :cond_ab

    goto/32 :goto_a2

    :cond_ab
    goto/32 :goto_55

    nop

    :goto_af
    add-float/2addr v3, v4

    goto/32 :goto_88

    nop

    :goto_b4
    iget v4, p0, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->realHeight:I

    goto/32 :goto_78

    nop
.end method

.method public onViewAdded(Landroid/view/View;)V
    .registers 3

    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/phone/NotificationIconContainer;->onViewAdded(Landroid/view/View;)V

    if-eqz p1, :cond_f

    instance-of v0, p1, Lcom/android/systemui/newstatusbar/views/StatusBarIconView;

    if-eqz v0, :cond_f

    move-object v0, p1

    check-cast v0, Lcom/android/systemui/newstatusbar/views/StatusBarIconView;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/views/StatusBarIconView;->setNotificationIcon()V

    :cond_f
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->onIconChange()V

    return-void
.end method

.method public setActualPaddingEnd(F)V
    .registers 3

    iget v0, p0, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->mDimenPadding:I

    int-to-float v0, v0

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->mActualPaddingEnd:F

    return-void
.end method

.method public setActualPaddingStart(F)V
    .registers 3

    iget v0, p0, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->mDimenPadding:I

    int-to-float v0, v0

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->mActualPaddingStart:F

    return-void
.end method

.method public setMaxIconsAmount(I)V
    .registers 3

    iget v0, p0, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->mMaxIcons:I

    if-eq p1, v0, :cond_7

    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/phone/NotificationIconContainer;->setMaxIconsAmount(I)V

    :cond_7
    return-void
.end method

.method public setPadding(IIII)V
    .registers 6

    const/4 v0, 0x0

    invoke-super {p0, p1, v0, p3, v0}, Lcom/android/systemui/statusbar/phone/NotificationIconContainer;->setPadding(IIII)V

    return-void
.end method

.method public setPaddingRelative(IIII)V
    .registers 6

    const/4 v0, 0x0

    invoke-super {p0, p1, v0, p3, v0}, Lcom/android/systemui/statusbar/phone/NotificationIconContainer;->setPaddingRelative(IIII)V

    return-void
.end method

.method public setVisibility(I)V
    .registers 2

    if-eqz p1, :cond_4

    const/16 p1, 0x8

    :cond_4
    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/phone/NotificationIconContainer;->setVisibility(I)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_layouts_NotificationIconContainer',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
