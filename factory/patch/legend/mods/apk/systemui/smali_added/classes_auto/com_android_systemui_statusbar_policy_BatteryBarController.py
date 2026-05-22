"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/statusbar/policy/BatteryBarController.smali'
CLASS_FALLBACK_NAMES = ['BatteryBarController.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/statusbar/policy/BatteryBarController;
.super Landroid/widget/LinearLayout;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/android/systemui/statusbar/policy/BatteryBarController$SettingsObserver;
    }
.end annotation


# instance fields
.field isAttached:Z

.field isVertical:Z

.field private mBatteryCharging:Z

.field private mBatteryLevel:I

.field private final mIntentReceiver:Landroid/content/BroadcastReceiver;

.field mLocation:I

.field mLocationToLookFor:I

.field private mSettingsObserver:Lcom/android/systemui/statusbar/policy/BatteryBarController$SettingsObserver;

.field mStyle:I


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 6

    const/4 v2, 0x0

    invoke-direct {p0, p1, p2}, Landroid/widget/LinearLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    iput v2, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->mStyle:I

    iput v2, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->mLocation:I

    iput v2, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->mLocationToLookFor:I

    iput v2, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->mBatteryLevel:I

    iput-boolean v2, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->mBatteryCharging:Z

    iput-boolean v2, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->isAttached:Z

    iput-boolean v2, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->isVertical:Z

    new-instance v1, Lcom/android/systemui/statusbar/policy/BatteryBarController$1;

    invoke-direct {v1, p0}, Lcom/android/systemui/statusbar/policy/BatteryBarController$1;-><init>(Lcom/android/systemui/statusbar/policy/BatteryBarController;)V

    iput-object v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->mIntentReceiver:Landroid/content/BroadcastReceiver;

    if-eqz p2, :cond_33

    if-eqz v1, :cond_27

    const-string v0, "http://schemas.android.com/apk/res/com.android.systemui"

    const-string v1, "viewLocation"

    invoke-interface {p2, v0, v1, v2}, Landroid/util/AttributeSet;->getAttributeIntValue(Ljava/lang/String;Ljava/lang/String;I)I

    move-result v1

    iput v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->mLocationToLookFor:I

    :cond_27
    if-eqz p2, :cond_33

    const-string v0, "http://schemas.android.com/apk/res/com.android.systemui"

    const-string v1, "viewLocation2"

    invoke-interface {p2, v0, v1, v2}, Landroid/util/AttributeSet;->getAttributeIntValue(Ljava/lang/String;Ljava/lang/String;I)I

    move-result v1

    iput v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->mLocationToLookFor:I

    :cond_33
    return-void
.end method

.method static synthetic access$000(Lcom/android/systemui/statusbar/policy/BatteryBarController;)Landroid/content/Context;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->mContext:Landroid/content/Context;

    return-object v0
.end method

.method static synthetic access$100(Lcom/android/systemui/statusbar/policy/BatteryBarController;)I
    .registers 2

    iget v0, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->mBatteryLevel:I

    return v0
.end method

.method static synthetic access$102(Lcom/android/systemui/statusbar/policy/BatteryBarController;I)I
    .registers 2

    iput p1, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->mBatteryLevel:I

    return p1
.end method

.method static synthetic access$202(Lcom/android/systemui/statusbar/policy/BatteryBarController;Z)Z
    .registers 2

    iput-boolean p1, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->mBatteryCharging:Z

    return p1
.end method


# virtual methods
.method public addBars()V
    .registers 15

    const/4 v13, 0x1

    const/high16 v10, 0x43340000  # 180.0f

    const/high16 v12, 0x3f800000  # 1.0f

    const/4 v11, -0x1

    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/BatteryBarController;->getContext()Landroid/content/Context;

    move-result-object v6

    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    invoke-virtual {v6}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;

    move-result-object v3

    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/BatteryBarController;->getContext()Landroid/content/Context;

    move-result-object v6

    invoke-virtual {v6}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v6

    const-string v7, "battery_bar_thickness"

    invoke-static {v6, v7, v13}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v6

    int-to-float v2, v6

    iget v6, v3, Landroid/util/DisplayMetrics;->density:F

    mul-float/2addr v6, v2

    float-to-double v6, v6

    const-wide/high16 v8, 0x3fe0000000000000L  # 0.5

    add-double/2addr v6, v8

    double-to-int v5, v6

    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/BatteryBarController;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v4

    iget-boolean v6, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->isVertical:Z

    if-eqz v6, :cond_5a

    iput v5, v4, Landroid/view/ViewGroup$LayoutParams;->width:I

    :goto_33
    invoke-virtual {p0, v4}, Lcom/android/systemui/statusbar/policy/BatteryBarController;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/BatteryBarController;->getContext()Landroid/content/Context;

    move-result-object v6

    invoke-static {v6}, Lcom/android/systemui/statusbar/policy/Prefs;->getLastBatteryLevel(Landroid/content/Context;)I

    move-result v6

    iput v6, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->mBatteryLevel:I

    iget v6, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->mStyle:I

    if-nez v6, :cond_5d

    new-instance v6, Lcom/android/systemui/statusbar/policy/BatteryBar;

    iget-object v7, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->mContext:Landroid/content/Context;

    iget-boolean v8, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->mBatteryCharging:Z

    iget v9, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->mBatteryLevel:I

    iget-boolean v10, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->isVertical:Z

    invoke-direct {v6, v7, v8, v9, v10}, Lcom/android/systemui/statusbar/policy/BatteryBar;-><init>(Landroid/content/Context;ZIZ)V

    new-instance v7, Landroid/widget/LinearLayout$LayoutParams;

    invoke-direct {v7, v11, v11, v12}, Landroid/widget/LinearLayout$LayoutParams;-><init>(IIF)V

    invoke-virtual {p0, v6, v7}, Lcom/android/systemui/statusbar/policy/BatteryBarController;->addView(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    :cond_59
    :goto_59
    return-void

    :cond_5a
    iput v5, v4, Landroid/view/ViewGroup$LayoutParams;->height:I

    goto :goto_33

    :cond_5d
    iget v6, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->mStyle:I

    if-ne v6, v13, :cond_59

    new-instance v0, Lcom/android/systemui/statusbar/policy/BatteryBar;

    iget-object v6, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->mContext:Landroid/content/Context;

    iget-boolean v7, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->mBatteryCharging:Z

    iget v8, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->mBatteryLevel:I

    iget-boolean v9, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->isVertical:Z

    invoke-direct {v0, v6, v7, v8, v9}, Lcom/android/systemui/statusbar/policy/BatteryBar;-><init>(Landroid/content/Context;ZIZ)V

    new-instance v1, Lcom/android/systemui/statusbar/policy/BatteryBar;

    iget-object v6, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->mContext:Landroid/content/Context;

    iget-boolean v7, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->mBatteryCharging:Z

    iget v8, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->mBatteryLevel:I

    iget-boolean v9, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->isVertical:Z

    invoke-direct {v1, v6, v7, v8, v9}, Lcom/android/systemui/statusbar/policy/BatteryBar;-><init>(Landroid/content/Context;ZIZ)V

    iget-boolean v6, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->isVertical:Z

    if-eqz v6, :cond_93

    invoke-virtual {v1, v10}, Lcom/android/systemui/statusbar/policy/BatteryBar;->setRotationY(F)V

    new-instance v6, Landroid/widget/LinearLayout$LayoutParams;

    invoke-direct {v6, v11, v11, v12}, Landroid/widget/LinearLayout$LayoutParams;-><init>(IIF)V

    invoke-virtual {p0, v1, v6}, Lcom/android/systemui/statusbar/policy/BatteryBarController;->addView(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    new-instance v6, Landroid/widget/LinearLayout$LayoutParams;

    invoke-direct {v6, v11, v11, v12}, Landroid/widget/LinearLayout$LayoutParams;-><init>(IIF)V

    invoke-virtual {p0, v0, v6}, Lcom/android/systemui/statusbar/policy/BatteryBarController;->addView(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    goto :goto_59

    :cond_93
    invoke-virtual {v0, v10}, Lcom/android/systemui/statusbar/policy/BatteryBar;->setRotationY(F)V

    new-instance v6, Landroid/widget/LinearLayout$LayoutParams;

    invoke-direct {v6, v11, v11, v12}, Landroid/widget/LinearLayout$LayoutParams;-><init>(IIF)V

    invoke-virtual {p0, v0, v6}, Lcom/android/systemui/statusbar/policy/BatteryBarController;->addView(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    new-instance v6, Landroid/widget/LinearLayout$LayoutParams;

    invoke-direct {v6, v11, v11, v12}, Landroid/widget/LinearLayout$LayoutParams;-><init>(IIF)V

    invoke-virtual {p0, v1, v6}, Lcom/android/systemui/statusbar/policy/BatteryBarController;->addView(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    goto :goto_59
.end method

.method protected isLocationValid(I)Z
    .registers 3

    goto/32 :goto_1d

    nop

    :goto_4
    return v0

    :goto_5
    goto/32 :goto_13

    nop

    :goto_9
    goto :goto_19

    :goto_a
    if-eq v0, p1, :cond_f

    goto/32 :goto_5

    :cond_f
    goto/32 :goto_18

    nop

    :goto_13
    const/4 v0, 0x0

    goto/32 :goto_9

    nop

    :goto_18
    const/4 v0, 0x1

    :goto_19
    goto/32 :goto_4

    nop

    :goto_1d
    iget v0, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->mLocationToLookFor:I

    goto/32 :goto_a

    nop
.end method

.method protected onAttachedToWindow()V
    .registers 5

    goto/32 :goto_8a

    nop

    :goto_4
    new-instance v0, Landroid/content/IntentFilter;

    goto/32 :goto_9c

    nop

    :goto_a
    iput-boolean v2, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->isAttached:Z

    goto/32 :goto_4

    nop

    :goto_10
    invoke-virtual {v1, v2, v0, v3}, Landroid/content/Context;->registerReceiver(Landroid/content/BroadcastReceiver;Landroid/content/IntentFilter;I)Landroid/content/Intent;

    goto/32 :goto_a3

    nop

    :goto_17
    iput-boolean v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->isVertical:Z

    goto/32 :goto_a

    nop

    :goto_1d
    iput-object v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->mSettingsObserver:Lcom/android/systemui/statusbar/policy/BatteryBarController$SettingsObserver;

    goto/32 :goto_68

    nop

    :goto_23
    invoke-super {p0}, Landroid/widget/LinearLayout;->onAttachedToWindow()V

    goto/32 :goto_7d

    nop

    :goto_2a
    if-eqz v1, :cond_2f

    goto/32 :goto_92

    :cond_2f
    goto/32 :goto_a9

    nop

    :goto_33
    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/BatteryBarController;->getContext()Landroid/content/Context;

    move-result-object v1

    goto/32 :goto_58

    nop

    :goto_3b
    const-string v1, "android.intent.action.BATTERY_CHANGED"

    goto/32 :goto_b8

    nop

    :goto_41
    invoke-virtual {v1}, Lcom/android/systemui/statusbar/policy/BatteryBarController$SettingsObserver;->observe()V

    goto/32 :goto_8f

    nop

    :goto_48
    move v1, v2

    :goto_49
    goto/32 :goto_17

    nop

    :goto_4d
    const/4 v3, 0x2

    goto/32 :goto_10

    nop

    :goto_52
    new-instance v2, Landroid/os/Handler;

    goto/32 :goto_83

    nop

    :goto_58
    iget-object v2, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->mIntentReceiver:Landroid/content/BroadcastReceiver;

    goto/32 :goto_4d

    nop

    :goto_5e
    const/4 v3, -0x1

    goto/32 :goto_6e

    nop

    :goto_63
    return-void

    :goto_64
    goto/32 :goto_78

    nop

    :goto_68
    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->mSettingsObserver:Lcom/android/systemui/statusbar/policy/BatteryBarController$SettingsObserver;

    goto/32 :goto_41

    nop

    :goto_6e
    if-eq v1, v3, :cond_73

    goto/32 :goto_64

    :cond_73
    goto/32 :goto_48

    nop

    :goto_77
    goto :goto_49

    :goto_78
    const/4 v1, 0x0

    goto/32 :goto_77

    nop

    :goto_7d
    iget-boolean v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->isAttached:Z

    goto/32 :goto_2a

    nop

    :goto_83
    invoke-direct {v2}, Landroid/os/Handler;-><init>()V

    goto/32 :goto_b1

    nop

    :goto_8a
    const/4 v2, 0x1

    goto/32 :goto_23

    nop

    :goto_8f
    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/BatteryBarController;->updateSettings()V

    :goto_92
    goto/32 :goto_63

    nop

    :goto_96
    iget v1, v1, Landroid/view/ViewGroup$LayoutParams;->height:I

    goto/32 :goto_5e

    nop

    :goto_9c
    invoke-direct {v0}, Landroid/content/IntentFilter;-><init>()V

    goto/32 :goto_3b

    nop

    :goto_a3
    new-instance v1, Lcom/android/systemui/statusbar/policy/BatteryBarController$SettingsObserver;

    goto/32 :goto_52

    nop

    :goto_a9
    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/BatteryBarController;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v1

    goto/32 :goto_96

    nop

    :goto_b1
    invoke-direct {v1, p0, v2}, Lcom/android/systemui/statusbar/policy/BatteryBarController$SettingsObserver;-><init>(Lcom/android/systemui/statusbar/policy/BatteryBarController;Landroid/os/Handler;)V

    goto/32 :goto_1d

    nop

    :goto_b8
    invoke-virtual {v0, v1}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    goto/32 :goto_33

    nop
.end method

.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 6

    goto/32 :goto_1b

    nop

    :goto_4
    invoke-virtual {v0, v1, v2, v3}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z

    :goto_7
    goto/32 :goto_14

    nop

    :goto_b
    if-nez v0, :cond_10

    goto/32 :goto_7

    :cond_10
    goto/32 :goto_28

    nop

    :goto_14
    return-void

    :goto_15
    new-instance v1, Lcom/android/systemui/statusbar/policy/BatteryBarController$2;

    goto/32 :goto_30

    nop

    :goto_1b
    invoke-super {p0, p1}, Landroid/widget/LinearLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    goto/32 :goto_37

    nop

    :goto_22
    const-wide/16 v2, 0x1f4

    goto/32 :goto_4

    nop

    :goto_28
    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/BatteryBarController;->getHandler()Landroid/os/Handler;

    move-result-object v0

    goto/32 :goto_15

    nop

    :goto_30
    invoke-direct {v1, p0}, Lcom/android/systemui/statusbar/policy/BatteryBarController$2;-><init>(Lcom/android/systemui/statusbar/policy/BatteryBarController;)V

    goto/32 :goto_22

    nop

    :goto_37
    iget-boolean v0, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->isAttached:Z

    goto/32 :goto_b

    nop
.end method

.method protected onDetachedFromWindow()V
    .registers 3

    goto/32 :goto_1b

    nop

    :goto_4
    invoke-super {p0}, Landroid/widget/LinearLayout;->onDetachedFromWindow()V

    goto/32 :goto_27

    nop

    :goto_b
    if-nez v0, :cond_10

    goto/32 :goto_17

    :cond_10
    goto/32 :goto_35

    nop

    :goto_14
    invoke-virtual {v0, v1}, Landroid/content/ContentResolver;->unregisterContentObserver(Landroid/database/ContentObserver;)V

    :goto_17
    goto/32 :goto_4

    nop

    :goto_1b
    iget-boolean v0, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->isAttached:Z

    goto/32 :goto_b

    nop

    :goto_21
    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->mSettingsObserver:Lcom/android/systemui/statusbar/policy/BatteryBarController$SettingsObserver;

    goto/32 :goto_14

    nop

    :goto_27
    return-void

    :goto_28
    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->mIntentReceiver:Landroid/content/BroadcastReceiver;

    goto/32 :goto_3a

    nop

    :goto_2e
    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/BatteryBarController;->removeBars()V

    goto/32 :goto_57

    nop

    :goto_35
    const/4 v0, 0x0

    goto/32 :goto_51

    nop

    :goto_3a
    invoke-virtual {v0, v1}, Landroid/content/Context;->unregisterReceiver(Landroid/content/BroadcastReceiver;)V

    goto/32 :goto_41

    nop

    :goto_41
    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/BatteryBarController;->getContext()Landroid/content/Context;

    move-result-object v0

    goto/32 :goto_49

    nop

    :goto_49
    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    goto/32 :goto_21

    nop

    :goto_51
    iput-boolean v0, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->isAttached:Z

    goto/32 :goto_2e

    nop

    :goto_57
    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/BatteryBarController;->getContext()Landroid/content/Context;

    move-result-object v0

    goto/32 :goto_28

    nop
.end method

.method public removeBars()V
    .registers 1

    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/BatteryBarController;->removeAllViews()V

    return-void
.end method

.method public updateSettings()V
    .registers 4

    const/4 v2, 0x0

    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/BatteryBarController;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "battery_bar_style"

    invoke-static {v0, v1, v2}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v0

    iput v0, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->mStyle:I

    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/BatteryBarController;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "battery_bar"

    invoke-static {v0, v1, v2}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v0

    iput v0, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->mLocation:I

    iget v0, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController;->mLocation:I

    invoke-virtual {p0, v0}, Lcom/android/systemui/statusbar/policy/BatteryBarController;->isLocationValid(I)Z

    move-result v0

    if-nez v0, :cond_33

    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/BatteryBarController;->removeBars()V

    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/BatteryBarController;->addBars()V

    invoke-virtual {p0, v2}, Lcom/android/systemui/statusbar/policy/BatteryBarController;->setVisibility(I)V

    :goto_32
    return-void

    :cond_33
    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/BatteryBarController;->removeBars()V

    const/16 v0, 0x8

    invoke-virtual {p0, v0}, Lcom/android/systemui/statusbar/policy/BatteryBarController;->setVisibility(I)V

    goto :goto_32
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_statusbar_policy_BatteryBarController',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
