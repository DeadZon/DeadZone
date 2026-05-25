"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/MiuiPhoneStatusBarView.smali'
CLASS_FALLBACK_NAMES = ['MiuiPhoneStatusBarView.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;
.super Lcom/android/systemui/statusbar/phone/MiuiPhoneStatusBarView;

# interfaces
.implements Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarViewSettingsController$CallBack;


# static fields
.field public static final TAG:Ljava/lang/String; = "Mezologs"

.field public static final keyHeight:Ljava/lang/String; = "custom_status_bar_height"

.field public static final keyLeftRight:Ljava/lang/String; = "custom_status_bar_left_right"

.field public static final keyOpen:Ljava/lang/String; = "custom_statusbar_dialog_open"

.field public static final keyTop:Ljava/lang/String; = "custom_status_bar_top"


# instance fields
.field private downX:F

.field private downY:F

.field private isChanged:Z

.field private statusBar:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

.field private status_bar_container:Landroid/view/View;


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 4

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/statusbar/phone/MiuiPhoneStatusBarView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->isChanged:Z

    return-void
.end method

.method static synthetic access$000(Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;)Landroid/view/View;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->status_bar_container:Landroid/view/View;

    return-object v0
.end method

.method private refreshStatusBarHeight(Z)V
    .registers 17

    sget-object v0, Lcom/android/systemui/Dependency;->sDependency:Lcom/android/systemui/Dependency;

    const-class v1, Lcom/android/systemui/statusbar/window/StatusBarWindowControllerStore;

    invoke-virtual {v0, v1}, Lcom/android/systemui/Dependency;->getDependencyInner(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/statusbar/window/StatusBarWindowControllerStore;

    if-eqz v0, :cond_65

    nop

    invoke-interface {v0}, Lcom/android/systemui/statusbar/window/StatusBarWindowControllerStore;->getDefaultDisplay()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/systemui/statusbar/window/StatusBarWindowController;

    check-cast v1, Lcom/android/systemui/statusbar/window/StatusBarWindowControllerImpl;

    if-eqz p1, :cond_20

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->getContext()Landroid/content/Context;

    move-result-object v2

    invoke-static {v2}, Lcom/android/internal/policy/SystemBarUtils;->getStatusBarHeight(Landroid/content/Context;)I

    move-result v2

    goto :goto_22

    :cond_20
    const/16 v2, 0xfa

    :goto_22
    iput v2, v1, Lcom/android/systemui/statusbar/window/StatusBarWindowControllerImpl;->mBarHeight:I

    iget-object v2, v1, Lcom/android/systemui/statusbar/window/StatusBarWindowControllerImpl;->mCurrentState:Lcom/android/systemui/statusbar/window/StatusBarWindowControllerImpl$State;

    invoke-virtual {v1, v2}, Lcom/android/systemui/statusbar/window/StatusBarWindowControllerImpl;->apply(Lcom/android/systemui/statusbar/window/StatusBarWindowControllerImpl$State;)V

    iget-object v10, v1, Lcom/android/systemui/statusbar/window/StatusBarWindowControllerImpl;->mStatusBarWindowView:Lcom/android/systemui/statusbar/window/StatusBarWindowView;

    const/16 v2, 0x8

    invoke-virtual {v10, v2}, Landroid/view/View;->setVisibility(I)V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->getResources()Landroid/content/res/Resources;

    move-result-object v2

    invoke-virtual {v2}, Landroid/content/res/Resources;->getConfiguration()Landroid/content/res/Configuration;

    move-result-object v11

    iget v12, v11, Landroid/content/res/Configuration;->orientation:I

    sget-object v2, Lcom/android/systemui/Dependency;->sDependency:Lcom/android/systemui/Dependency;

    const-class v3, Lcom/android/systemui/statusbar/policy/ConfigurationController;

    invoke-virtual {v2, v3}, Lcom/android/systemui/Dependency;->getDependencyInner(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v2

    move-object v13, v2

    check-cast v13, Lcom/android/systemui/statusbar/phone/ConfigurationControllerImpl;

    if-eqz v13, :cond_51

    if-nez v12, :cond_4b

    const/4 v2, 0x1

    goto :goto_4c

    :cond_4b
    const/4 v2, 0x0

    :goto_4c
    iput v2, v11, Landroid/content/res/Configuration;->orientation:I

    invoke-virtual {v13, v11}, Lcom/android/systemui/statusbar/phone/ConfigurationControllerImpl;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    :cond_51
    new-instance v14, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView$1;

    move-object v2, v14

    move-object v3, p0

    move-object v4, v10

    move-object v5, v1

    move/from16 v6, p1

    move-object v7, v13

    move-object v8, v11

    move v9, v12

    invoke-direct/range {v2 .. v9}, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView$1;-><init>(Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;Landroid/view/View;Lcom/android/systemui/statusbar/window/StatusBarWindowControllerImpl;ZLcom/android/systemui/statusbar/phone/ConfigurationControllerImpl;Landroid/content/res/Configuration;I)V

    const-wide/16 v2, 0x1f4

    invoke-virtual {v10, v14, v2, v3}, Landroid/view/View;->postDelayed(Ljava/lang/Runnable;J)Z

    goto :goto_6c

    :cond_65
    const-string v1, "Mezologs"

    const-string v2, "refreshStatusBarHeight: store == null"

    invoke-static {v1, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    :goto_6c
    return-void
.end method


# virtual methods
.method public onAttachedToWindow()V
    .registers 2

    invoke-super {p0}, Lcom/android/systemui/statusbar/phone/MiuiPhoneStatusBarView;->onAttachedToWindow()V

    const-class v0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarViewSettingsController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarViewSettingsController;

    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarViewSettingsController;->addCallBack(Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;)V

    const/4 v0, 0x0

    invoke-virtual {p0, v0, v0, v0, v0}, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->setPadding(IIII)V

    return-void
.end method

.method public onDetachedFromWindow()V
    .registers 2

    invoke-super {p0}, Lcom/android/systemui/statusbar/phone/MiuiPhoneStatusBarView;->onDetachedFromWindow()V

    const-class v0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarViewSettingsController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarViewSettingsController;

    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarViewSettingsController;->removeCallBack(Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;)V

    return-void
.end method

.method public onFinishInflate()V
    .registers 4

    invoke-super {p0}, Lcom/android/systemui/statusbar/phone/MiuiPhoneStatusBarView;->onFinishInflate()V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->getContext()Landroid/content/Context;

    move-result-object v0

    const-string v1, "status_bar_container"

    invoke-static {v0, v1}, Landroid/Utils/Utils;->IDtoID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v0

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->findViewById(I)Landroid/view/View;

    move-result-object v0

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->status_bar_container:Landroid/view/View;

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->getContext()Landroid/content/Context;

    move-result-object v0

    const-string v1, "status_bar_contents"

    invoke-static {v0, v1}, Landroid/Utils/Utils;->IDtoID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v0

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->findViewById(I)Landroid/view/View;

    move-result-object v0

    :try_start_21
    const-string v1, "com.android.systemui.newstatusbar.layouts.MainLayout"

    invoke-static {v1}, Ljava/lang/Class;->forName(Ljava/lang/String;)Ljava/lang/Class;

    move-result-object v1

    if-eqz v1, :cond_32

    instance-of v2, v0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    if-eqz v2, :cond_32

    move-object v2, v0

    check-cast v2, Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    iput-object v2, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->statusBar:Lcom/android/systemui/newstatusbar/layouts/MainLayout;
    :try_end_32
    .catch Ljava/lang/Exception; {:try_start_21 .. :try_end_32} :catch_33

    :cond_32
    goto :goto_34

    :catch_33
    move-exception v1

    :goto_34
    return-void
.end method

.method public onSettingsChange(Ljava/lang/String;)V
    .registers 5

    const-string v0, "custom_statusbar_dialog_open"

    invoke-virtual {v0, p1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v1

    const/4 v2, 0x0

    if-eqz v1, :cond_1f

    invoke-static {v0}, Landroid/preference/SettingsMezoHelper;->getBoolofSettings(Ljava/lang/String;)Z

    move-result v0

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->isChanged:Z

    if-eqz v0, :cond_14

    const v2, -0xff0100

    :cond_14
    invoke-virtual {p0, v2}, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->setBackgroundColor(I)V

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->isChanged:Z

    xor-int/lit8 v0, v0, 0x1

    invoke-direct {p0, v0}, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->refreshStatusBarHeight(Z)V

    goto :goto_29

    :cond_1f
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->updateHeight()V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->getPaddingBottom()I

    move-result v0

    invoke-virtual {p0, v2, v2, v2, v0}, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->setPadding(IIII)V

    :goto_29
    return-void
.end method

.method public setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V
    .registers 5

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-static {v0}, Lcom/android/internal/policy/SystemBarUtils;->getStatusBarHeight(Landroid/content/Context;)I

    move-result v0

    iput v0, p1, Landroid/view/ViewGroup$LayoutParams;->height:I

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->isChanged:Z

    const/4 v1, 0x0

    if-eqz v0, :cond_22

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string v2, "custom_status_bar_height"

    invoke-static {v0, v2, v1}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v0

    move v2, v0

    if-lez v0, :cond_22

    iput v2, p1, Landroid/view/ViewGroup$LayoutParams;->height:I

    :cond_22
    instance-of v0, p1, Landroid/view/ViewGroup$MarginLayoutParams;

    if-eqz v0, :cond_34

    move-object v0, p1

    check-cast v0, Landroid/view/ViewGroup$MarginLayoutParams;

    const-string v2, "custom_status_bar_left_right"

    invoke-static {v2, v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v1

    iput v1, v0, Landroid/view/ViewGroup$MarginLayoutParams;->leftMargin:I

    iput v1, v0, Landroid/view/ViewGroup$MarginLayoutParams;->rightMargin:I

    goto :goto_3b

    :cond_34
    const-string v0, "Mezologs"

    const-string v1, "setLayoutParams: params not margin"

    invoke-static {v0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    :goto_3b
    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/phone/MiuiPhoneStatusBarView;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->statusBar:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    if-eqz v0, :cond_4f

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    iget v1, p1, Landroid/view/ViewGroup$LayoutParams;->height:I

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/controllers/ElementController;->updateHeight(I)V

    :cond_4f
    return-void
.end method

.method public setPadding(IIII)V
    .registers 8

    const/4 v0, 0x0

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->getPaddingTop()I

    move-result v1

    const-string v2, "custom_status_bar_top"

    invoke-static {v2, v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result p2

    invoke-super {p0, v0, p2, v0, p4}, Lcom/android/systemui/statusbar/phone/MiuiPhoneStatusBarView;->setPadding(IIII)V

    return-void
.end method

.method public updateCutoutLocation()V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->mCutoutSpace:Landroid/view/View;

    if-nez v0, :cond_14

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->getContext()Landroid/content/Context;

    move-result-object v0

    const-string v1, "cutout_space_view"

    invoke-static {v0, v1}, Landroid/Utils/Utils;->IDtoID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v0

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->findViewById(I)Landroid/view/View;

    move-result-object v0

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->mCutoutSpace:Landroid/view/View;

    :cond_14
    const/4 v0, 0x0

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->mDisplayCutout:Landroid/view/DisplayCutout;

    invoke-super {p0}, Lcom/android/systemui/statusbar/phone/MiuiPhoneStatusBarView;->updateCutoutLocation()V

    return-void
.end method

.method updateHeight()V
    .registers 1

    goto/32 :goto_4

    nop

    :goto_4
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->updateStatusBarHeight()V

    goto/32 :goto_b

    nop

    :goto_b
    return-void
.end method

.method public updateNotificationIconAreaInnnerParent()V
    .registers 7

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->mNotificationIconAreaInner:Landroid/view/View;

    if-eqz v0, :cond_88

    const/4 v0, 0x0

    :try_start_5
    const-class v1, Lcom/android/systemui/statusbar/phone/MiuiPhoneStatusBarView;

    const-string v2, "onLayoutChangeListener"

    invoke-virtual {v1, v2}, Ljava/lang/Class;->getField(Ljava/lang/String;)Ljava/lang/reflect/Field;

    move-result-object v1

    const/4 v2, 0x1

    invoke-virtual {v1, v2}, Ljava/lang/reflect/Field;->setAccessible(Z)V

    invoke-virtual {v1, p0}, Ljava/lang/reflect/Field;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v2

    check-cast v2, Landroid/view/View$OnLayoutChangeListener;
    :try_end_17
    .catch Ljava/lang/Exception; {:try_start_5 .. :try_end_17} :catch_19

    move-object v0, v2

    goto :goto_1a

    :catch_19
    move-exception v1

    :goto_1a
    if-nez v0, :cond_27

    const-string v1, "Mezologs"

    const-string v2, "updateNotificationIconAreaInnnerParent: error"

    invoke-static {v1, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    invoke-super {p0}, Lcom/android/systemui/statusbar/phone/MiuiPhoneStatusBarView;->updateNotificationIconAreaInnnerParent()V

    return-void

    :cond_27
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->mFullscreenStatusBarNotificationIconArea:Landroid/view/ViewGroup;

    invoke-virtual {v1, v0}, Landroid/view/ViewGroup;->removeOnLayoutChangeListener(Landroid/view/View$OnLayoutChangeListener;)V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->mDripStatusBarNotificationIconArea:Landroid/view/ViewGroup;

    invoke-virtual {v1, v0}, Landroid/view/ViewGroup;->removeOnLayoutChangeListener(Landroid/view/View$OnLayoutChangeListener;)V

    iget v1, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->mCurrentStatusBarType:I

    if-nez v1, :cond_38

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->mFullscreenStatusBarNotificationIconArea:Landroid/view/ViewGroup;

    goto :goto_3a

    :cond_38
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->mDripStatusBarNotificationIconArea:Landroid/view/ViewGroup;

    :goto_3a
    invoke-virtual {v1, v0}, Landroid/view/ViewGroup;->addOnLayoutChangeListener(Landroid/view/View$OnLayoutChangeListener;)V

    iget v2, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->mCurrentStatusBarType:I

    const/4 v3, -0x2

    if-eqz v2, :cond_63

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->mNotificationIconAreaInner:Landroid/view/View;

    invoke-virtual {v2}, Landroid/view/View;->getParent()Landroid/view/ViewParent;

    move-result-object v2

    if-eqz v2, :cond_57

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->mNotificationIconAreaInner:Landroid/view/View;

    invoke-virtual {v2}, Landroid/view/View;->getParent()Landroid/view/ViewParent;

    move-result-object v2

    check-cast v2, Landroid/view/ViewGroup;

    iget-object v4, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->mNotificationIconAreaInner:Landroid/view/View;

    invoke-virtual {v2, v4}, Landroid/view/ViewGroup;->removeView(Landroid/view/View;)V

    :cond_57
    iget-object v2, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->mNotificationIconAreaInner:Landroid/view/View;

    new-instance v4, Landroid/view/ViewGroup$LayoutParams;

    const/4 v5, -0x1

    invoke-direct {v4, v3, v5}, Landroid/view/ViewGroup$LayoutParams;-><init>(II)V

    invoke-virtual {v1, v2, v4}, Landroid/view/ViewGroup;->addView(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    goto :goto_88

    :cond_63
    iget-object v2, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->mNotificationIconAreaInner:Landroid/view/View;

    invoke-virtual {v2}, Landroid/view/View;->getParent()Landroid/view/ViewParent;

    move-result-object v2

    if-eqz v2, :cond_7d

    invoke-interface {v2}, Landroid/view/ViewParent;->getParent()Landroid/view/ViewParent;

    move-result-object v4

    if-eqz v4, :cond_7d

    invoke-interface {v2}, Landroid/view/ViewParent;->getParent()Landroid/view/ViewParent;

    move-result-object v4

    check-cast v4, Landroid/view/ViewGroup;

    move-object v5, v2

    check-cast v5, Landroid/view/View;

    invoke-virtual {v4, v5}, Landroid/view/ViewGroup;->removeView(Landroid/view/View;)V

    :cond_7d
    move-object v4, v2

    check-cast v4, Landroid/view/View;

    new-instance v5, Landroid/view/ViewGroup$LayoutParams;

    invoke-direct {v5, v3, v3}, Landroid/view/ViewGroup$LayoutParams;-><init>(II)V

    invoke-virtual {v1, v4, v5}, Landroid/view/ViewGroup;->addView(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    :cond_88
    :goto_88
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_MiuiPhoneStatusBarView',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
