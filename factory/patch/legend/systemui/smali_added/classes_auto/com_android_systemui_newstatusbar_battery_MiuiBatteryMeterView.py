"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/battery/MiuiBatteryMeterView.smali'
CLASS_FALLBACK_NAMES = ['MiuiBatteryMeterView.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;
.super Lcom/android/systemui/statusbar/views/MiuiBatteryMeterView;

# interfaces
.implements Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;


# static fields
.field private static final Grafical:I = 0x0

.field private static final Percentage_Center_and_Graphical:I = 0x1

.field private static final Percentage_Left_and_Graphical:I = 0x6

.field private static final Percentage_Right_and_Graphical:I = 0x3

.field private static final Percentage_only:I = 0x5

.field private static final Style_Off:I = 0x4

.field private static final Top_bar:I = 0x2


# instance fields
.field TAG:Ljava/lang/String;

.field private isLeftPercent:Z

.field private isMarkViewVisible:Z

.field private mBatteryPercentMarkFolme:Lmiuix/animation/IFolme;


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 4

    const/4 v0, 0x0

    invoke-direct {p0, p1, p2, v0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 7

    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/statusbar/views/MiuiBatteryMeterView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->isLeftPercent:Z

    const/4 v0, 0x1

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->isMarkViewVisible:Z

    const-string v0, "Nastya_porn"

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->TAG:Ljava/lang/String;

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getLayoutTransition()Landroid/animation/LayoutTransition;

    move-result-object v0

    const/4 v1, 0x4

    invoke-virtual {v0, v1}, Landroid/animation/LayoutTransition;->enableTransitionType(I)V

    const-wide/16 v1, 0x12c

    invoke-virtual {v0, v1, v2}, Landroid/animation/LayoutTransition;->setDuration(J)V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->onIconChange()V

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->setnotClip()V

    return-void
.end method

.method public static HAS_NOTCH()Z
    .registers 1

    const/4 v0, 0x0

    return v0
.end method

.method private getNoUseAnimate()Z
    .registers 4

    const/4 v0, 0x0

    new-array v0, v0, [Ljava/lang/Object;

    const-string v1, "getNoUseAnimate"

    const/4 v2, 0x1

    invoke-static {p0, v1, v2, v0}, Landroid/Utils/ReflectionUtil;->invokeInSuperClass(Ljava/lang/Object;Ljava/lang/String;I[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Ljava/lang/Boolean;

    invoke-virtual {v0}, Ljava/lang/Boolean;->booleanValue()Z

    move-result v0

    return v0
.end method

.method private getUseAnimate()Z
    .registers 4

    const/4 v0, 0x0

    new-array v0, v0, [Ljava/lang/Object;

    const-string v1, "getUseAnimate"

    const/4 v2, 0x1

    invoke-static {p0, v1, v2, v0}, Landroid/Utils/ReflectionUtil;->invokeInSuperClass(Ljava/lang/Object;Ljava/lang/String;I[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Ljava/lang/Boolean;

    invoke-virtual {v0}, Ljava/lang/Boolean;->booleanValue()Z

    move-result v0

    return v0
.end method

.method private setUseLegacy()V
    .registers 3

    const-string v0, "use_legacy_drawable"

    invoke-static {v0}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v0

    if-lez v0, :cond_a

    const/4 v0, 0x1

    goto :goto_b

    :cond_a
    const/4 v0, 0x0

    :goto_b
    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mUseLegacyDrawable:Z

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryIconView:Lcom/android/systemui/statusbar/views/MiuiBatteryMeterIconView;

    invoke-virtual {v1, v0}, Lcom/android/systemui/statusbar/views/MiuiBatteryMeterIconView;->setUseLegacyDrawable(Z)V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mHollowBatteryIconView:Lcom/android/systemui/statusbar/views/MiuiHollowBatteryMeterIconView;

    invoke-virtual {v1, v0}, Lcom/android/systemui/statusbar/views/MiuiHollowBatteryMeterIconView;->setUseLegacyDrawable(Z)V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->updateChargeAndText()V

    return-void
.end method

.method private setnotClip()V
    .registers 3

    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->setClipChildren(Z)V

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->setClipToPadding(Z)V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryDigitalView:Landroid/widget/FrameLayout;

    invoke-virtual {v1, v0}, Landroid/widget/FrameLayout;->setClipChildren(Z)V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryDigitalView:Landroid/widget/FrameLayout;

    invoke-virtual {v1, v0}, Landroid/widget/FrameLayout;->setClipToPadding(Z)V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryPercentContainer:Landroid/widget/LinearLayout;

    invoke-virtual {v1, v0}, Landroid/widget/LinearLayout;->setClipChildren(Z)V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryPercentContainer:Landroid/widget/LinearLayout;

    invoke-virtual {v1, v0}, Landroid/widget/LinearLayout;->setClipToPadding(Z)V

    return-void
.end method

.method private updateCharge(ZZ)V
    .registers 5

    if-nez p1, :cond_7

    if-eqz p2, :cond_5

    goto :goto_7

    :cond_5
    const/4 v0, 0x0

    goto :goto_8

    :cond_7
    :goto_7
    const/4 v0, 0x1

    :goto_8
    const-string v1, "battery_charge_change"

    invoke-static {v1, v0}, Landroid/preference/SettingsMezoHelper;->putBoolinSettings(Ljava/lang/String;Z)V

    return-void
.end method

.method private updateLevel(I)V
    .registers 3

    const-string v0, "battery_level_change"

    invoke-static {v0, p1}, Landroid/preference/SettingsMezoHelper;->putIntinSettings(Ljava/lang/String;I)V

    return-void
.end method


# virtual methods
.method public folmeNotNull()Z
    .registers 2

    invoke-super {p0}, Lcom/android/systemui/statusbar/views/MiuiBatteryMeterView;->folmeNotNull()Z

    move-result v0

    if-eqz v0, :cond_c

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryPercentMarkFolme:Lmiuix/animation/IFolme;

    if-eqz v0, :cond_c

    const/4 v0, 0x1

    goto :goto_d

    :cond_c
    const/4 v0, 0x0

    :goto_d
    return v0
.end method

.method public isLayoutRtl()Z
    .registers 2

    invoke-super {p0}, Lcom/android/systemui/statusbar/views/MiuiBatteryMeterView;->isLayoutRtl()Z

    move-result v0

    if-nez v0, :cond_d

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->isLeftPercent:Z

    if-eqz v0, :cond_b

    goto :goto_d

    :cond_b
    const/4 v0, 0x0

    goto :goto_e

    :cond_d
    :goto_d
    const/4 v0, 0x1

    :goto_e
    return v0
.end method

.method public onAttachedToWindow()V
    .registers 4

    invoke-super {p0}, Lcom/android/systemui/statusbar/views/MiuiBatteryMeterView;->onAttachedToWindow()V

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getUseAnimate()Z

    move-result v0

    if-eqz v0, :cond_17

    const/4 v0, 0x1

    new-array v0, v0, [Landroid/view/View;

    const/4 v1, 0x0

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryPercentMarkView:Landroid/widget/TextView;

    aput-object v2, v0, v1

    invoke-static {v0}, Lmiuix/animation/Folme;->useAt([Landroid/view/View;)Lmiuix/animation/IFolme;

    move-result-object v0

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryPercentMarkFolme:Lmiuix/animation/IFolme;

    :cond_17
    const-class v0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->addCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V

    return-void
.end method

.method public onBatteryLevelChanged(IZZ)V
    .registers 4

    invoke-super {p0, p1, p2, p3}, Lcom/android/systemui/statusbar/views/MiuiBatteryMeterView;->onBatteryLevelChanged(IZZ)V

    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->updateLevel(I)V

    return-void
.end method

.method public onBatteryStyleChanged(I)V
    .registers 12

    iget v0, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mStoreRealStyle:I

    const/4 v1, 0x1

    const/4 v2, 0x0

    if-eq p1, v0, :cond_8

    move v0, v1

    goto :goto_9

    :cond_8
    move v0, v2

    :goto_9
    iput p1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mStoreRealStyle:I

    const/4 v3, 0x6

    if-ne p1, v3, :cond_12

    iput-boolean v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->isLeftPercent:Z

    const/4 p1, 0x3

    goto :goto_14

    :cond_12
    iput-boolean v2, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->isLeftPercent:Z

    :goto_14
    invoke-static {}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->HAS_NOTCH()Z

    move-result v3

    const/4 v4, 0x2

    if-eqz v3, :cond_1e

    if-ne p1, v4, :cond_1e

    const/4 p1, 0x0

    :cond_1e
    iget-boolean v3, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mIsIslandShowing:Z

    const/4 v5, 0x3

    if-eqz v3, :cond_33

    if-ne p1, v5, :cond_33

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getUseAnimate()Z

    move-result v3

    if-nez v3, :cond_31

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getNoUseAnimate()Z

    move-result v3

    if-eqz v3, :cond_33

    :cond_31
    move v3, v1

    goto :goto_34

    :cond_33
    move v3, v2

    :goto_34
    iget v6, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mStatusBarState:I

    const/4 v7, 0x5

    if-eqz v6, :cond_4a

    iget v6, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mLayoutFromTag:I

    if-eq v6, v7, :cond_41

    iget v6, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mLayoutFromTag:I

    if-ne v6, v1, :cond_4a

    :cond_41
    iget-boolean v6, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mHasIslandOnce:Z

    if-nez v6, :cond_4a

    iget-boolean v6, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mHasIslandInfoOper:Z

    if-eqz v6, :cond_4a

    const/4 v3, 0x0

    :cond_4a
    if-eqz v3, :cond_4d

    const/4 p1, 0x1

    :cond_4d
    iget-boolean v6, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mToAod:Z

    if-eqz v6, :cond_53

    if-ne p1, v5, :cond_54

    :cond_53
    move v5, p1

    :cond_54
    iget v6, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryStyle:I

    if-ne v6, v5, :cond_5a

    if-eqz v0, :cond_183

    :cond_5a
    iput v5, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryStyle:I

    const/4 v6, 0x4

    const-string v8, "battery_meter_view"

    const/16 v9, 0x8

    if-ne v5, v6, :cond_89

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getUseAnimate()Z

    move-result v1

    if-eqz v1, :cond_84

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->folmeNotNull()Z

    move-result v1

    if-nez v1, :cond_70

    goto :goto_84

    :cond_70
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->isNeedAnimateIsland()Z

    move-result v1

    if-eqz v1, :cond_7d

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryMeterViewFolme:Lmiuix/animation/IFolme;

    invoke-static {v1, p0, v8}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->animateHideView(Lmiuix/animation/IFolme;Landroid/view/View;Ljava/lang/String;)V

    goto/16 :goto_183

    :cond_7d
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryMeterViewFolme:Lmiuix/animation/IFolme;

    invoke-static {v1, p0, v8}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->hideView(Lmiuix/animation/IFolme;Landroid/view/View;Ljava/lang/String;)V

    goto/16 :goto_183

    :cond_84
    :goto_84
    invoke-virtual {p0, v9}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->setVisibility(I)V

    goto/16 :goto_183

    :cond_89
    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getUseAnimate()Z

    move-result v6

    if-eqz v6, :cond_a8

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->folmeNotNull()Z

    move-result v6

    if-nez v6, :cond_96

    goto :goto_a8

    :cond_96
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->isNeedAnimateIsland()Z

    move-result v6

    if-eqz v6, :cond_a2

    iget-object v6, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryMeterViewFolme:Lmiuix/animation/IFolme;

    invoke-static {v6, p0, v8}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->animateShowView(Lmiuix/animation/IFolme;Landroid/view/View;Ljava/lang/String;)V

    goto :goto_ab

    :cond_a2
    iget-object v6, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryMeterViewFolme:Lmiuix/animation/IFolme;

    invoke-static {v6, p0, v8}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->showView(Lmiuix/animation/IFolme;Landroid/view/View;Ljava/lang/String;)V

    goto :goto_ab

    :cond_a8
    :goto_a8
    invoke-virtual {p0, v2}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->setVisibility(I)V

    :goto_ab
    const-string v6, "battery_icon_container"

    if-eq v5, v4, :cond_db

    if-ne v5, v7, :cond_b2

    goto :goto_db

    :cond_b2
    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getUseAnimate()Z

    move-result v4

    if-eqz v4, :cond_d5

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->folmeNotNull()Z

    move-result v4

    if-nez v4, :cond_bf

    goto :goto_d5

    :cond_bf
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->isNeedAnimateIsland()Z

    move-result v4

    if-eqz v4, :cond_cd

    iget-object v4, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryDigitalViewFolme:Lmiuix/animation/IFolme;

    iget-object v7, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryDigitalView:Landroid/widget/FrameLayout;

    invoke-static {v4, v7, v6}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->animateShowView(Lmiuix/animation/IFolme;Landroid/view/View;Ljava/lang/String;)V

    goto :goto_103

    :cond_cd
    iget-object v4, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryDigitalViewFolme:Lmiuix/animation/IFolme;

    iget-object v7, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryDigitalView:Landroid/widget/FrameLayout;

    invoke-static {v4, v7, v6}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->showView(Lmiuix/animation/IFolme;Landroid/view/View;Ljava/lang/String;)V

    goto :goto_103

    :cond_d5
    :goto_d5
    iget-object v4, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryDigitalView:Landroid/widget/FrameLayout;

    invoke-virtual {v4, v2}, Landroid/widget/FrameLayout;->setVisibility(I)V

    goto :goto_103

    :cond_db
    :goto_db
    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getUseAnimate()Z

    move-result v4

    if-eqz v4, :cond_fe

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->folmeNotNull()Z

    move-result v4

    if-nez v4, :cond_e8

    goto :goto_fe

    :cond_e8
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->isNeedAnimateIsland()Z

    move-result v4

    if-eqz v4, :cond_f6

    iget-object v4, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryDigitalViewFolme:Lmiuix/animation/IFolme;

    iget-object v7, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryDigitalView:Landroid/widget/FrameLayout;

    invoke-static {v4, v7, v6}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->animateHideView(Lmiuix/animation/IFolme;Landroid/view/View;Ljava/lang/String;)V

    goto :goto_103

    :cond_f6
    iget-object v4, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryDigitalViewFolme:Lmiuix/animation/IFolme;

    iget-object v7, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryDigitalView:Landroid/widget/FrameLayout;

    invoke-static {v4, v7, v6}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->hideView(Lmiuix/animation/IFolme;Landroid/view/View;Ljava/lang/String;)V

    goto :goto_103

    :cond_fe
    :goto_fe
    iget-object v4, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryDigitalView:Landroid/widget/FrameLayout;

    invoke-virtual {v4, v9}, Landroid/widget/FrameLayout;->setVisibility(I)V

    :goto_103
    const-string v4, "hollow_battery_meter_icon_view"

    const-string v6, "battery_meter_icon_view"

    if-ne v5, v1, :cond_145

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getUseAnimate()Z

    move-result v1

    if-eqz v1, :cond_13a

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->folmeNotNull()Z

    move-result v1

    if-nez v1, :cond_116

    goto :goto_13a

    :cond_116
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->isNeedAnimateIsland()Z

    move-result v1

    if-eqz v1, :cond_12b

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryIconViewFolme:Lmiuix/animation/IFolme;

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryIconView:Lcom/android/systemui/statusbar/views/MiuiBatteryMeterIconView;

    invoke-static {v1, v2, v6}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->animateHideView(Lmiuix/animation/IFolme;Landroid/view/View;Ljava/lang/String;)V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mHollowBatteryIconViewFolme:Lmiuix/animation/IFolme;

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mHollowBatteryIconView:Lcom/android/systemui/statusbar/views/MiuiHollowBatteryMeterIconView;

    invoke-static {v1, v2, v4}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->animateShowView(Lmiuix/animation/IFolme;Landroid/view/View;Ljava/lang/String;)V

    goto :goto_180

    :cond_12b
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryIconViewFolme:Lmiuix/animation/IFolme;

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryIconView:Lcom/android/systemui/statusbar/views/MiuiBatteryMeterIconView;

    invoke-static {v1, v2, v6}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->hideView(Lmiuix/animation/IFolme;Landroid/view/View;Ljava/lang/String;)V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mHollowBatteryIconViewFolme:Lmiuix/animation/IFolme;

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mHollowBatteryIconView:Lcom/android/systemui/statusbar/views/MiuiHollowBatteryMeterIconView;

    invoke-static {v1, v2, v4}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->showView(Lmiuix/animation/IFolme;Landroid/view/View;Ljava/lang/String;)V

    goto :goto_180

    :cond_13a
    :goto_13a
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryIconView:Lcom/android/systemui/statusbar/views/MiuiBatteryMeterIconView;

    invoke-virtual {v1, v9}, Lcom/android/systemui/statusbar/views/MiuiBatteryMeterIconView;->setVisibility(I)V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mHollowBatteryIconView:Lcom/android/systemui/statusbar/views/MiuiHollowBatteryMeterIconView;

    invoke-virtual {v1, v2}, Lcom/android/systemui/statusbar/views/MiuiHollowBatteryMeterIconView;->setVisibility(I)V

    goto :goto_180

    :cond_145
    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getUseAnimate()Z

    move-result v1

    if-eqz v1, :cond_176

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->folmeNotNull()Z

    move-result v1

    if-nez v1, :cond_152

    goto :goto_176

    :cond_152
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->isNeedAnimateIsland()Z

    move-result v1

    if-eqz v1, :cond_167

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryIconViewFolme:Lmiuix/animation/IFolme;

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryIconView:Lcom/android/systemui/statusbar/views/MiuiBatteryMeterIconView;

    invoke-static {v1, v2, v6}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->animateShowView(Lmiuix/animation/IFolme;Landroid/view/View;Ljava/lang/String;)V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mHollowBatteryIconViewFolme:Lmiuix/animation/IFolme;

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mHollowBatteryIconView:Lcom/android/systemui/statusbar/views/MiuiHollowBatteryMeterIconView;

    invoke-static {v1, v2, v4}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->animateHideView(Lmiuix/animation/IFolme;Landroid/view/View;Ljava/lang/String;)V

    goto :goto_180

    :cond_167
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryIconViewFolme:Lmiuix/animation/IFolme;

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryIconView:Lcom/android/systemui/statusbar/views/MiuiBatteryMeterIconView;

    invoke-static {v1, v2, v6}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->showView(Lmiuix/animation/IFolme;Landroid/view/View;Ljava/lang/String;)V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mHollowBatteryIconViewFolme:Lmiuix/animation/IFolme;

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mHollowBatteryIconView:Lcom/android/systemui/statusbar/views/MiuiHollowBatteryMeterIconView;

    invoke-static {v1, v2, v4}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->hideView(Lmiuix/animation/IFolme;Landroid/view/View;Ljava/lang/String;)V

    goto :goto_180

    :cond_176
    :goto_176
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryIconView:Lcom/android/systemui/statusbar/views/MiuiBatteryMeterIconView;

    invoke-virtual {v1, v2}, Lcom/android/systemui/statusbar/views/MiuiBatteryMeterIconView;->setVisibility(I)V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mHollowBatteryIconView:Lcom/android/systemui/statusbar/views/MiuiHollowBatteryMeterIconView;

    invoke-virtual {v1, v9}, Lcom/android/systemui/statusbar/views/MiuiHollowBatteryMeterIconView;->setVisibility(I)V

    :goto_180
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->updateChargeAndText()V

    :cond_183
    :goto_183
    return-void
.end method

.method public onChargeStateChanged(ZZ)V
    .registers 3

    invoke-super {p0, p1, p2}, Lcom/android/systemui/statusbar/views/MiuiBatteryMeterView;->onChargeStateChanged(ZZ)V

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->updateCharge(ZZ)V

    return-void
.end method

.method public onDetachedFromWindow()V
    .registers 2

    invoke-super {p0}, Lcom/android/systemui/statusbar/views/MiuiBatteryMeterView;->onDetachedFromWindow()V

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getUseAnimate()Z

    move-result v0

    if-eqz v0, :cond_18

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->folmeNotNull()Z

    move-result v0

    if-eqz v0, :cond_18

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryPercentMarkFolme:Lmiuix/animation/IFolme;

    invoke-interface {v0}, Lmiuix/animation/IFolme;->state()Lmiuix/animation/IStateStyle;

    move-result-object v0

    invoke-interface {v0}, Lmiuix/animation/IStateStyle;->clean()V

    :cond_18
    const-class v0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->removeCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V

    return-void
.end method

.method public onIconChange()V
    .registers 2

    const-string v0, "battery_percent_mark_enable"

    invoke-static {v0}, Landroid/preference/SettingsMezoHelper;->getBoolofSettings1(Ljava/lang/String;)Z

    move-result v0

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->isMarkViewVisible:Z

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->setUseLegacy()V

    iget v0, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mStoreRealStyle:I

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->onBatteryStyleChanged(I)V

    return-void
.end method

.method public final onLayout(ZIIII)V
    .registers 23

    move-object/from16 v0, p0

    invoke-virtual/range {p0 .. p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->isLayoutRtl()Z

    move-result v1

    sub-int v2, p5, p3

    sub-int v3, p4, p2

    iget-object v4, v0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryDigitalView:Landroid/widget/FrameLayout;

    const/4 v5, 0x0

    const/16 v6, 0x8

    if-eqz v4, :cond_6e

    invoke-virtual {v4}, Landroid/widget/FrameLayout;->getVisibility()I

    move-result v7

    if-ne v7, v6, :cond_18

    goto :goto_6e

    :cond_18
    iget-object v7, v0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryDigitalView:Landroid/widget/FrameLayout;

    invoke-virtual {v7}, Landroid/widget/FrameLayout;->getMeasuredWidth()I

    move-result v7

    iget-object v8, v0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryDigitalView:Landroid/widget/FrameLayout;

    invoke-virtual {v8}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result v8

    invoke-virtual/range {p0 .. p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getPaddingStart()I

    move-result v9

    if-eqz v1, :cond_2e

    sub-int v10, v3, v9

    sub-int v9, v10, v7

    :cond_2e
    if-le v8, v2, :cond_32

    move v10, v5

    goto :goto_36

    :cond_32
    sub-int v10, v2, v8

    div-int/lit8 v10, v10, 0x2

    :goto_36
    invoke-virtual/range {p0 .. p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getPaddingTop()I

    move-result v11

    add-int/2addr v10, v11

    invoke-virtual/range {p0 .. p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getPaddingStart()I

    move-result v11

    if-eqz v1, :cond_44

    sub-int v12, v3, v11

    goto :goto_46

    :cond_44
    add-int v12, v11, v7

    :goto_46
    if-le v8, v2, :cond_4a

    move v13, v2

    goto :goto_4e

    :cond_4a
    add-int v13, v8, v2

    div-int/lit8 v13, v13, 0x2

    :goto_4e
    invoke-virtual/range {p0 .. p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getPaddingBottom()I

    move-result v14

    add-int/2addr v13, v14

    invoke-virtual {v4, v9, v10, v12, v13}, Landroid/widget/FrameLayout;->layout(IIII)V

    if-eqz v1, :cond_63

    invoke-virtual/range {p0 .. p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getPaddingStart()I

    move-result v12

    invoke-virtual/range {p0 .. p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getPaddingEnd()I

    move-result v13

    add-int/2addr v13, v7

    sub-int/2addr v3, v13

    goto :goto_6f

    :cond_63
    invoke-virtual/range {p0 .. p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getPaddingStart()I

    move-result v12

    add-int/2addr v12, v7

    invoke-virtual/range {p0 .. p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getPaddingEnd()I

    move-result v13

    sub-int/2addr v3, v13

    goto :goto_6f

    :cond_6e
    :goto_6e
    const/4 v12, 0x0

    :goto_6f
    iget-object v7, v0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryChargingView:Landroid/widget/ImageView;

    if-eqz v7, :cond_b1

    invoke-virtual {v7}, Landroid/widget/ImageView;->getVisibility()I

    move-result v8

    if-eq v8, v6, :cond_b1

    iget-object v8, v0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryChargingView:Landroid/widget/ImageView;

    invoke-virtual {v8}, Landroid/widget/ImageView;->getMeasuredWidth()I

    move-result v8

    iget-object v9, v0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryChargingView:Landroid/widget/ImageView;

    invoke-virtual {v9}, Landroid/widget/ImageView;->getMeasuredHeight()I

    move-result v9

    iget-object v10, v0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryChargingView:Landroid/widget/ImageView;

    if-nez v1, :cond_8c

    sub-int v11, v3, v8

    goto :goto_8d

    :cond_8c
    move v11, v12

    :goto_8d
    if-le v9, v2, :cond_91

    move v13, v5

    goto :goto_95

    :cond_91
    sub-int v13, v2, v9

    div-int/lit8 v13, v13, 0x2

    :goto_95
    invoke-virtual/range {p0 .. p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getPaddingTop()I

    move-result v14

    add-int/2addr v13, v14

    if-nez v1, :cond_9e

    move v14, v3

    goto :goto_a0

    :cond_9e
    add-int v14, v8, v12

    :goto_a0
    if-le v9, v2, :cond_a4

    move v15, v2

    goto :goto_a8

    :cond_a4
    add-int v15, v9, v2

    div-int/lit8 v15, v15, 0x2

    :goto_a8
    invoke-virtual/range {p0 .. p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getPaddingBottom()I

    move-result v16

    add-int v15, v15, v16

    invoke-virtual {v10, v11, v13, v14, v15}, Landroid/widget/ImageView;->layout(IIII)V

    :cond_b1
    iget-object v8, v0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryPercentContainer:Landroid/widget/LinearLayout;

    if-eqz v8, :cond_ef

    invoke-virtual {v8}, Landroid/widget/LinearLayout;->getVisibility()I

    move-result v9

    if-ne v9, v6, :cond_bc

    goto :goto_ef

    :cond_bc
    iget-object v6, v0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryPercentContainer:Landroid/widget/LinearLayout;

    invoke-virtual {v6}, Landroid/widget/LinearLayout;->getMeasuredWidth()I

    move-result v6

    iget-object v9, v0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryPercentContainer:Landroid/widget/LinearLayout;

    invoke-virtual {v9}, Landroid/widget/LinearLayout;->getMeasuredHeight()I

    move-result v9

    if-eqz v1, :cond_cd

    sub-int v10, v3, v6

    goto :goto_ce

    :cond_cd
    move v10, v12

    :goto_ce
    if-gt v9, v2, :cond_d4

    sub-int v5, v2, v9

    div-int/lit8 v5, v5, 0x2

    :cond_d4
    invoke-virtual/range {p0 .. p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getPaddingTop()I

    move-result v11

    add-int/2addr v5, v11

    if-nez v1, :cond_dd

    add-int v3, v10, v6

    :cond_dd
    invoke-virtual/range {p0 .. p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getPaddingBottom()I

    move-result v11

    if-gt v9, v2, :cond_e7

    add-int v12, v2, v9

    div-int/lit8 v2, v12, 0x2

    :cond_e7
    iget-object v12, v0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryPercentContainer:Landroid/widget/LinearLayout;

    add-int v13, v2, v11

    invoke-virtual {v12, v10, v5, v3, v13}, Landroid/widget/LinearLayout;->layout(IIII)V

    return-void

    :cond_ef
    :goto_ef
    return-void
.end method

.method public final onMeasure(II)V
    .registers 17
    .annotation system Ldalvik/annotation/Throws;
        value = {
            Landroid/content/res/Resources$NotFoundException;
        }
    .end annotation

    move-object v6, p0

    const/4 v7, 0x0

    const/4 v8, 0x0

    iget v0, v6, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryStyle:I

    const/16 v9, 0x8

    const/4 v10, 0x2

    if-eq v0, v10, :cond_31

    iget-object v0, v6, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryDigitalView:Landroid/widget/FrameLayout;

    move-object v11, v0

    if-eqz v0, :cond_31

    invoke-virtual {v11}, Landroid/widget/FrameLayout;->getVisibility()I

    move-result v0

    if-eq v0, v9, :cond_31

    iget-object v1, v6, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryDigitalView:Landroid/widget/FrameLayout;

    const/4 v3, 0x0

    const/4 v5, 0x0

    move-object v0, p0

    move v2, p1

    move/from16 v4, p2

    invoke-virtual/range {v0 .. v5}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->measureChildWithMargins(Landroid/view/View;IIII)V

    iget-object v0, v6, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryDigitalView:Landroid/widget/FrameLayout;

    invoke-virtual {v0}, Landroid/widget/FrameLayout;->getMeasuredWidth()I

    move-result v7

    const/4 v0, 0x0

    iget-object v1, v6, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryDigitalView:Landroid/widget/FrameLayout;

    invoke-virtual {v1}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result v1

    invoke-static {v0, v1}, Ljava/lang/Math;->max(II)I

    move-result v8

    :cond_31
    const/4 v11, 0x1

    iget v0, v6, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryStyle:I

    const/4 v12, 0x5

    if-eq v0, v10, :cond_40

    iget v0, v6, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryStyle:I

    const/4 v1, 0x1

    if-eq v0, v1, :cond_40

    iget v0, v6, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryStyle:I

    if-ne v0, v12, :cond_6b

    :cond_40
    iget-boolean v0, v6, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mCharging:Z

    if-eqz v0, :cond_6b

    iget-object v0, v6, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryChargingView:Landroid/widget/ImageView;

    move-object v13, v0

    if-eqz v0, :cond_6b

    invoke-virtual {v13}, Landroid/widget/ImageView;->getVisibility()I

    move-result v0

    if-eq v0, v9, :cond_6b

    iget-object v1, v6, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryChargingView:Landroid/widget/ImageView;

    const/4 v5, 0x0

    move-object v0, p0

    move v2, p1

    move v3, v7

    move/from16 v4, p2

    invoke-virtual/range {v0 .. v5}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->measureChildWithMargins(Landroid/view/View;IIII)V

    iget-object v0, v6, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryChargingView:Landroid/widget/ImageView;

    invoke-virtual {v0}, Landroid/widget/ImageView;->getMeasuredWidth()I

    move-result v0

    add-int/2addr v7, v0

    iget-object v0, v6, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryChargingView:Landroid/widget/ImageView;

    invoke-virtual {v0}, Landroid/widget/ImageView;->getMeasuredHeight()I

    move-result v0

    invoke-static {v8, v0}, Ljava/lang/Math;->max(II)I

    move-result v8

    :cond_6b
    iget v0, v6, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryStyle:I

    const/4 v1, 0x3

    if-eq v0, v1, :cond_74

    iget v0, v6, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryStyle:I

    if-ne v0, v12, :cond_9b

    :cond_74
    iget-object v0, v6, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryPercentContainer:Landroid/widget/LinearLayout;

    move-object v12, v0

    if-eqz v0, :cond_9b

    invoke-virtual {v12}, Landroid/widget/LinearLayout;->getVisibility()I

    move-result v0

    if-eq v0, v9, :cond_9b

    iget-object v1, v6, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryPercentContainer:Landroid/widget/LinearLayout;

    const/4 v5, 0x0

    move-object v0, p0

    move v2, p1

    move v3, v7

    move/from16 v4, p2

    invoke-virtual/range {v0 .. v5}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->measureChildWithMargins(Landroid/view/View;IIII)V

    iget-object v0, v6, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryPercentContainer:Landroid/widget/LinearLayout;

    invoke-virtual {v0}, Landroid/widget/LinearLayout;->getMeasuredWidth()I

    move-result v0

    add-int/2addr v7, v0

    iget-object v0, v6, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryPercentContainer:Landroid/widget/LinearLayout;

    invoke-virtual {v0}, Landroid/widget/LinearLayout;->getMeasuredHeight()I

    move-result v0

    invoke-static {v8, v0}, Ljava/lang/Math;->max(II)I

    move-result v8

    :cond_9b
    iget v0, v6, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryStyle:I

    if-ne v0, v10, :cond_ac

    if-nez v7, :cond_ac

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getContext()Landroid/content/Context;

    move-result-object v0

    const-string v1, "battery_meter_height"

    invoke-static {v0, v1}, Landroid/Utils/Utils;->getDimen(Landroid/content/Context;Ljava/lang/String;)I

    move-result v8

    goto :goto_ad

    :cond_ac
    move v11, v7

    :goto_ad
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getPaddingEnd()I

    move-result v0

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getPaddingStart()I

    move-result v1

    add-int/2addr v0, v1

    add-int/2addr v0, v11

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getPaddingBottom()I

    move-result v1

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getPaddingTop()I

    move-result v2

    add-int/2addr v1, v2

    add-int/2addr v1, v8

    invoke-virtual {p0, v0, v1}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->setMeasuredDimension(II)V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getHeight()I

    move-result v0

    int-to-float v0, v0

    const/high16 v1, 0x40000000  # 2.0f

    div-float/2addr v0, v1

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->setPivotY(F)V

    return-void
.end method

.method public onMinimalismModeChanged(Z)V
    .registers 2

    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/views/MiuiBatteryMeterView;->onMinimalismModeChanged(Z)V

    return-void
.end method

.method public setAlpha(F)V
    .registers 3

    const/high16 v0, 0x3f800000  # 1.0f

    invoke-super {p0, v0}, Lcom/android/systemui/statusbar/views/MiuiBatteryMeterView;->setAlpha(F)V

    return-void
.end method

.method public setScaleX(F)V
    .registers 3

    const/high16 v0, 0x3f800000  # 1.0f

    invoke-super {p0, v0}, Lcom/android/systemui/statusbar/views/MiuiBatteryMeterView;->setScaleX(F)V

    return-void
.end method

.method public setScaleY(F)V
    .registers 3

    const/high16 v0, 0x3f800000  # 1.0f

    invoke-super {p0, v0}, Lcom/android/systemui/statusbar/views/MiuiBatteryMeterView;->setScaleY(F)V

    return-void
.end method

.method public setTranslationX(F)V
    .registers 3

    const/4 v0, 0x0

    invoke-super {p0, v0}, Lcom/android/systemui/statusbar/views/MiuiBatteryMeterView;->setTranslationX(F)V

    return-void
.end method

.method public setTranslationY(F)V
    .registers 3

    const/4 v0, 0x0

    invoke-super {p0, v0}, Lcom/android/systemui/statusbar/views/MiuiBatteryMeterView;->setTranslationY(F)V

    return-void
.end method

.method public setVisibility(I)V
    .registers 2

    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/views/MiuiBatteryMeterView;->setVisibility(I)V

    return-void
.end method

.method public updateAll()V
    .registers 1

    invoke-super {p0}, Lcom/android/systemui/statusbar/views/MiuiBatteryMeterView;->updateAll()V

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->setUseLegacy()V

    return-void
.end method

.method public updateChargeAndText()V
    .registers 9

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryPercentView:Landroid/widget/TextView;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mLevelString:Ljava/lang/String;

    invoke-virtual {v0, v1}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getContext()Landroid/content/Context;

    move-result-object v0

    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mCharging:Z

    if-eqz v1, :cond_1a

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getContext()Landroid/content/Context;

    move-result-object v1

    const-string v2, "accessibility_battery_level_charging"

    invoke-static {v1, v2}, Landroid/Utils/Utils;->StringToID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v1

    goto :goto_24

    :cond_1a
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getContext()Landroid/content/Context;

    move-result-object v1

    const-string v2, "accessibility_battery_level"

    invoke-static {v1, v2}, Landroid/Utils/Utils;->StringToID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v1

    :goto_24
    const/4 v2, 0x1

    new-array v3, v2, [Ljava/lang/Object;

    iget v4, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mLevel:I

    invoke-static {v4}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v4

    const/4 v5, 0x0

    aput-object v4, v3, v5

    invoke-virtual {v0, v1, v3}, Landroid/content/Context;->getString(I[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v0

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->setContentDescription(Ljava/lang/CharSequence;)V

    iget v0, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryStyle:I

    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mCharging:Z

    const/4 v3, 0x5

    const/16 v4, 0x8

    const-string v6, "battery_charging_view"

    if-eqz v1, :cond_77

    const/4 v1, 0x2

    if-eq v0, v1, :cond_49

    if-eq v0, v2, :cond_49

    if-ne v0, v3, :cond_77

    :cond_49
    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mIsAddBatteryIsland:Z

    if-eqz v1, :cond_4e

    goto :goto_77

    :cond_4e
    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getUseAnimate()Z

    move-result v1

    if-eqz v1, :cond_71

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->folmeNotNull()Z

    move-result v1

    if-nez v1, :cond_5b

    goto :goto_71

    :cond_5b
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->isNeedAnimateIsland()Z

    move-result v1

    if-eqz v1, :cond_69

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryChargeingViewFolme:Lmiuix/animation/IFolme;

    iget-object v7, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryChargingView:Landroid/widget/ImageView;

    invoke-static {v1, v7, v6}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->animateShowView(Lmiuix/animation/IFolme;Landroid/view/View;Ljava/lang/String;)V

    goto :goto_9f

    :cond_69
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryChargeingViewFolme:Lmiuix/animation/IFolme;

    iget-object v7, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryChargingView:Landroid/widget/ImageView;

    invoke-static {v1, v7, v6}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->showView(Lmiuix/animation/IFolme;Landroid/view/View;Ljava/lang/String;)V

    goto :goto_9f

    :cond_71
    :goto_71
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryChargingView:Landroid/widget/ImageView;

    invoke-virtual {v1, v5}, Landroid/widget/ImageView;->setVisibility(I)V

    goto :goto_9f

    :cond_77
    :goto_77
    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getUseAnimate()Z

    move-result v1

    if-eqz v1, :cond_9a

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->folmeNotNull()Z

    move-result v1

    if-nez v1, :cond_84

    goto :goto_9a

    :cond_84
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->isNeedAnimateIsland()Z

    move-result v1

    if-eqz v1, :cond_92

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryChargeingViewFolme:Lmiuix/animation/IFolme;

    iget-object v7, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryChargingView:Landroid/widget/ImageView;

    invoke-static {v1, v7, v6}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->animateHideView(Lmiuix/animation/IFolme;Landroid/view/View;Ljava/lang/String;)V

    goto :goto_9f

    :cond_92
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryChargeingViewFolme:Lmiuix/animation/IFolme;

    iget-object v7, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryChargingView:Landroid/widget/ImageView;

    invoke-static {v1, v7, v6}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->hideView(Lmiuix/animation/IFolme;Landroid/view/View;Ljava/lang/String;)V

    goto :goto_9f

    :cond_9a
    :goto_9a
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryChargingView:Landroid/widget/ImageView;

    invoke-virtual {v1, v4}, Landroid/widget/ImageView;->setVisibility(I)V

    :goto_9f
    const/4 v1, 0x3

    const-string v6, "battery_percent_container"

    if-eq v0, v1, :cond_d1

    if-ne v0, v3, :cond_a7

    goto :goto_d1

    :cond_a7
    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getUseAnimate()Z

    move-result v1

    if-eqz v1, :cond_cb

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->folmeNotNull()Z

    move-result v1

    if-nez v1, :cond_b4

    goto :goto_cb

    :cond_b4
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->isNeedAnimateIsland()Z

    move-result v1

    if-eqz v1, :cond_c3

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryPercentContainerFolme:Lmiuix/animation/IFolme;

    iget-object v3, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryPercentContainer:Landroid/widget/LinearLayout;

    invoke-static {v1, v3, v6}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->animateHideView(Lmiuix/animation/IFolme;Landroid/view/View;Ljava/lang/String;)V

    goto/16 :goto_12b

    :cond_c3
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryPercentContainerFolme:Lmiuix/animation/IFolme;

    iget-object v3, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryPercentContainer:Landroid/widget/LinearLayout;

    invoke-static {v1, v3, v6}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->hideView(Lmiuix/animation/IFolme;Landroid/view/View;Ljava/lang/String;)V

    goto :goto_12b

    :cond_cb
    :goto_cb
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryPercentContainer:Landroid/widget/LinearLayout;

    invoke-virtual {v1, v4}, Landroid/widget/LinearLayout;->setVisibility(I)V

    goto :goto_12b

    :cond_d1
    :goto_d1
    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getUseAnimate()Z

    move-result v1

    if-eqz v1, :cond_11c

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->folmeNotNull()Z

    move-result v1

    if-nez v1, :cond_de

    goto :goto_11c

    :cond_de
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->isNeedAnimateIsland()Z

    move-result v1

    const-string v3, "battery_percent_mark_view"

    if-eqz v1, :cond_101

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryPercentContainerFolme:Lmiuix/animation/IFolme;

    iget-object v4, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryPercentContainer:Landroid/widget/LinearLayout;

    invoke-static {v1, v4, v6}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->animateShowView(Lmiuix/animation/IFolme;Landroid/view/View;Ljava/lang/String;)V

    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->isMarkViewVisible:Z

    if-eqz v1, :cond_f9

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryPercentMarkFolme:Lmiuix/animation/IFolme;

    iget-object v4, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryPercentMarkView:Landroid/widget/TextView;

    invoke-static {v1, v4, v3}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->animateShowView(Lmiuix/animation/IFolme;Landroid/view/View;Ljava/lang/String;)V

    goto :goto_12b

    :cond_f9
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryPercentMarkFolme:Lmiuix/animation/IFolme;

    iget-object v4, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryPercentMarkView:Landroid/widget/TextView;

    invoke-static {v1, v4, v3}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->animateHideView(Lmiuix/animation/IFolme;Landroid/view/View;Ljava/lang/String;)V

    goto :goto_12b

    :cond_101
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryPercentContainerFolme:Lmiuix/animation/IFolme;

    iget-object v4, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryPercentContainer:Landroid/widget/LinearLayout;

    invoke-static {v1, v4, v6}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->showView(Lmiuix/animation/IFolme;Landroid/view/View;Ljava/lang/String;)V

    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->isMarkViewVisible:Z

    if-eqz v1, :cond_114

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryPercentMarkFolme:Lmiuix/animation/IFolme;

    iget-object v4, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryPercentMarkView:Landroid/widget/TextView;

    invoke-static {v1, v4, v3}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->showView(Lmiuix/animation/IFolme;Landroid/view/View;Ljava/lang/String;)V

    goto :goto_12b

    :cond_114
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryPercentMarkFolme:Lmiuix/animation/IFolme;

    iget-object v4, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryPercentMarkView:Landroid/widget/TextView;

    invoke-static {v1, v4, v3}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->hideView(Lmiuix/animation/IFolme;Landroid/view/View;Ljava/lang/String;)V

    goto :goto_12b

    :cond_11c
    :goto_11c
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryPercentContainer:Landroid/widget/LinearLayout;

    invoke-virtual {v1, v5}, Landroid/widget/LinearLayout;->setVisibility(I)V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryPercentMarkView:Landroid/widget/TextView;

    iget-boolean v3, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->isMarkViewVisible:Z

    if-eqz v3, :cond_128

    move v4, v5

    :cond_128
    invoke-virtual {v1, v4}, Landroid/widget/TextView;->setVisibility(I)V

    :goto_12b
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mMiuiStatusBatteryContainer:Lcom/android/systemui/statusbar/views/MiuiStatusBatteryContainer;

    if-eqz v1, :cond_13e

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getContext()Landroid/content/Context;

    move-result-object v1

    invoke-static {v1}, Lcom/miui/utils/configs/MiuiConfigs;->isFlipTinyScreen(Landroid/content/Context;)Z

    move-result v1

    if-nez v1, :cond_13e

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mMiuiStatusBatteryContainer:Lcom/android/systemui/statusbar/views/MiuiStatusBatteryContainer;

    invoke-virtual {v1, v2}, Lcom/android/systemui/statusbar/views/MiuiStatusBatteryContainer;->setBatteryChanged(Z)V

    :cond_13e
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mMiuiStatusBatteryContainer:Lcom/android/systemui/statusbar/views/MiuiStatusBatteryContainer;

    if-eqz v1, :cond_14d

    iget-boolean v2, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mIsAodAnimate:Z

    if-nez v2, :cond_14a

    sget-boolean v2, Lcom/android/systemui/statusbar/StatusBarIslandControllerImpl;->MINIMAL_ANIMATION_ENABLED:Z

    if-eqz v2, :cond_14d

    :cond_14a
    invoke-virtual {v1, v5}, Lcom/android/systemui/statusbar/views/MiuiStatusBatteryContainer;->setBatteryChanged(Z)V

    :cond_14d
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->requestLayout()V

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryChargingView:Landroid/widget/ImageView;

    const/4 v3, 0x0

    invoke-virtual {v2, v3}, Landroid/widget/ImageView;->setImageTintList(Landroid/content/res/ColorStateList;)V

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryChargingView:Landroid/widget/ImageView;

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getContext()Landroid/content/Context;

    move-result-object v3

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->getHollowChargingIconId()I

    move-result v4

    invoke-virtual {v3, v4}, Landroid/content/Context;->getDrawable(I)Landroid/graphics/drawable/Drawable;

    move-result-object v3

    invoke-virtual {v2, v3}, Landroid/widget/ImageView;->setImageDrawable(Landroid/graphics/drawable/Drawable;)V

    iput v5, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mDark:I

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->onDarkChangedInternal()V

    return-void
.end method

.method public updateHomeBlock(Z)V
    .registers 3

    const/4 v0, 0x0

    invoke-super {p0, v0}, Lcom/android/systemui/statusbar/views/MiuiBatteryMeterView;->updateHomeBlock(Z)V

    return-void
.end method

.method public updateIslandChanged(ZZ)V
    .registers 3

    return-void
.end method

.method public updateIslandShowing(ZZZ)V
    .registers 4

    return-void
.end method

.method public updateVisibility$1$1()V
    .registers 3

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mHomeBlock:Z

    if-nez v0, :cond_1b

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mMinimalism:Z

    if-nez v0, :cond_1b

    iget v0, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryStyle:I

    const/4 v1, 0x4

    if-ne v0, v1, :cond_e

    goto :goto_1b

    :cond_e
    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mIsAddBatteryIsland:Z

    if-eqz v0, :cond_16

    invoke-virtual {p0, v1}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->setVisibility(I)V

    goto :goto_20

    :cond_16
    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->setVisibility(I)V

    goto :goto_20

    :cond_1b
    :goto_1b
    const/16 v0, 0x8

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->setVisibility(I)V

    :goto_20
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_battery_MiuiBatteryMeterView',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
