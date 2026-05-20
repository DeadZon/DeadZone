"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/statusbar/policy/BatteryBar.smali'
CLASS_FALLBACK_NAMES = ['BatteryBar.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/statusbar/policy/BatteryBar;
.super Landroid/widget/RelativeLayout;

# interfaces
.implements Landroid/graphics/drawable/Animatable;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/android/systemui/statusbar/policy/BatteryBar$1;,
        Lcom/android/systemui/statusbar/policy/BatteryBar$SettingsObserver;
    }
.end annotation


# static fields
.field private static final TAG:Ljava/lang/String;


# instance fields
.field private isAnimating:Z

.field private mAttached:Z

.field mBarGradient:Landroid/graphics/drawable/GradientDrawable;

.field mBatteryBar:Landroid/view/View;

.field mBatteryBarLayout:Landroid/widget/LinearLayout;

.field private mBatteryCharging:Z

.field private mBatteryLevel:I

.field private mBatteryLowColorWarning:I

.field mCharger:Landroid/view/View;

.field mChargerLayout:Landroid/widget/LinearLayout;

.field private mChargingColor:I

.field private mChargingLevel:I

.field private mColor:I

.field mGradientColors:[I

.field private mHandler:Landroid/os/Handler;

.field private mHighColor:I

.field private final mIntentReceiver:Landroid/content/BroadcastReceiver;

.field private mLowColor:I

.field private shouldAnimateCharging:Z

.field private useGradientColor:Z

.field vertical:Z


# direct methods
.method static synthetic -get0(Lcom/android/systemui/statusbar/policy/BatteryBar;)Z
    .registers 2

    iget-boolean v0, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mBatteryCharging:Z

    return v0
.end method

.method static synthetic -get1(Lcom/android/systemui/statusbar/policy/BatteryBar;)I
    .registers 2

    iget v0, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mBatteryLevel:I

    return v0
.end method

.method static synthetic -get2(Lcom/android/systemui/statusbar/policy/BatteryBar;)Landroid/content/Context;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mContext:Landroid/content/Context;

    return-object v0
.end method

.method static synthetic -set0(Lcom/android/systemui/statusbar/policy/BatteryBar;Z)Z
    .registers 2

    iput-boolean p1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mBatteryCharging:Z

    return p1
.end method

.method static synthetic -set1(Lcom/android/systemui/statusbar/policy/BatteryBar;I)I
    .registers 2

    iput p1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mBatteryLevel:I

    return p1
.end method

.method static synthetic -wrap0(Lcom/android/systemui/statusbar/policy/BatteryBar;I)V
    .registers 2

    invoke-direct {p0, p1}, Lcom/android/systemui/statusbar/policy/BatteryBar;->setProgress(I)V

    return-void
.end method

.method static synthetic -wrap1(Lcom/android/systemui/statusbar/policy/BatteryBar;)V
    .registers 1

    invoke-direct {p0}, Lcom/android/systemui/statusbar/policy/BatteryBar;->updateSettings()V

    return-void
.end method

.method static constructor <clinit>()V
    .registers 1

    const-class v0, Lcom/android/systemui/statusbar/policy/BatteryBar;

    invoke-virtual {v0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object v0

    sput-object v0, Lcom/android/systemui/statusbar/policy/BatteryBar;->TAG:Ljava/lang/String;

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 4

    const/4 v0, 0x0

    invoke-direct {p0, p1, p2, v0}, Lcom/android/systemui/statusbar/policy/BatteryBar;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 12

    const/4 v4, 0x1

    const/4 v1, -0x1

    const/4 v3, 0x0

    invoke-direct {p0, p1, p2, p3}, Landroid/widget/RelativeLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    iput-boolean v3, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mAttached:Z

    iput v3, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mBatteryLevel:I

    iput v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mChargingLevel:I

    iput-boolean v3, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mBatteryCharging:Z

    iput-boolean v4, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->shouldAnimateCharging:Z

    iput-boolean v3, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->isAnimating:Z

    iput v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mColor:I

    iput v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mChargingColor:I

    iput v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mBatteryLowColorWarning:I

    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/BatteryBar;->getContext()Landroid/content/Context;

    move-result-object v5

    invoke-virtual {v5}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string/jumbo v5, "statusbar_battery_bar_low_color"

    const v6, -0xff2101

    invoke-static {v0, v5, v6}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v5

    iput v5, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mLowColor:I

    const v1, -0xffe701

    iput v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mHighColor:I

    iput-boolean v3, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->useGradientColor:Z

    new-instance v1, Landroid/os/Handler;

    invoke-direct {v1}, Landroid/os/Handler;-><init>()V

    iput-object v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mHandler:Landroid/os/Handler;

    iput-boolean v3, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->vertical:Z

    new-instance v1, Lcom/android/systemui/statusbar/policy/BatteryBar$1;

    invoke-direct {v1, p0}, Lcom/android/systemui/statusbar/policy/BatteryBar$1;-><init>(Lcom/android/systemui/statusbar/policy/BatteryBar;)V

    iput-object v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mIntentReceiver:Landroid/content/BroadcastReceiver;

    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/BatteryBar;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    const/4 v1, 0x2

    new-array v1, v1, [I

    iput-object v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mGradientColors:[I

    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mGradientColors:[I

    iget v2, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mLowColor:I

    aput v2, v1, v3

    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mGradientColors:[I

    iget v2, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mHighColor:I

    aput v2, v1, v4

    new-instance v1, Landroid/graphics/drawable/GradientDrawable;

    sget-object v2, Landroid/graphics/drawable/GradientDrawable$Orientation;->LEFT_RIGHT:Landroid/graphics/drawable/GradientDrawable$Orientation;

    iget-object v3, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mGradientColors:[I

    invoke-direct {v1, v2, v3}, Landroid/graphics/drawable/GradientDrawable;-><init>(Landroid/graphics/drawable/GradientDrawable$Orientation;[I)V

    iput-object v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mBarGradient:Landroid/graphics/drawable/GradientDrawable;

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;ZIZ)V
    .registers 6

    const/4 v0, 0x0

    invoke-direct {p0, p1, v0}, Lcom/android/systemui/statusbar/policy/BatteryBar;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    iput p3, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mBatteryLevel:I

    iput-boolean p2, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mBatteryCharging:Z

    iput-boolean p4, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->vertical:Z

    return-void
.end method

.method private colorToRgb(I)[I
    .registers 5

    const/4 v1, 0x4

    new-array v0, v1, [I

    const/high16 v1, -0x1000000

    and-int/2addr v1, p1

    shr-int/lit8 v1, v1, 0x18

    const/4 v2, 0x0

    aput v1, v0, v2

    const/high16 v1, 0xff0000

    and-int/2addr v1, p1

    shr-int/lit8 v1, v1, 0x10

    const/4 v2, 0x1

    aput v1, v0, v2

    const v1, 0xff00

    and-int/2addr v1, p1

    shr-int/lit8 v1, v1, 0x8

    const/4 v2, 0x2

    aput v1, v0, v2

    and-int/lit16 v1, p1, 0xff

    const/4 v2, 0x3

    aput v1, v0, v2

    return-object v0
.end method

.method private mixColors(IIF)I
    .registers 12

    const/4 v7, 0x3

    const/4 v6, 0x2

    const/4 v5, 0x1

    const/4 v4, 0x0

    invoke-direct {p0, p1}, Lcom/android/systemui/statusbar/policy/BatteryBar;->colorToRgb(I)[I

    move-result-object v0

    invoke-direct {p0, p2}, Lcom/android/systemui/statusbar/policy/BatteryBar;->colorToRgb(I)[I

    move-result-object v1

    aget v2, v0, v4

    aget v3, v1, v4

    invoke-direct {p0, v2, v3, p3}, Lcom/android/systemui/statusbar/policy/BatteryBar;->mixedValue(IIF)I

    move-result v2

    aput v2, v0, v4

    aget v2, v0, v5

    aget v3, v1, v5

    invoke-direct {p0, v2, v3, p3}, Lcom/android/systemui/statusbar/policy/BatteryBar;->mixedValue(IIF)I

    move-result v2

    aput v2, v0, v5

    aget v2, v0, v6

    aget v3, v1, v6

    invoke-direct {p0, v2, v3, p3}, Lcom/android/systemui/statusbar/policy/BatteryBar;->mixedValue(IIF)I

    move-result v2

    aput v2, v0, v6

    aget v2, v0, v7

    aget v3, v1, v7

    invoke-direct {p0, v2, v3, p3}, Lcom/android/systemui/statusbar/policy/BatteryBar;->mixedValue(IIF)I

    move-result v2

    aput v2, v0, v7

    invoke-direct {p0, v0}, Lcom/android/systemui/statusbar/policy/BatteryBar;->rgbToColor([I)I

    move-result v2

    return v2
.end method

.method private mixedValue(IIF)I
    .registers 7

    int-to-float v0, p1

    mul-float/2addr v0, p3

    const/high16 v1, 0x3f800000  # 1.0f

    sub-float/2addr v1, p3

    int-to-float v2, p2

    mul-float/2addr v1, v2

    add-float/2addr v0, v1

    const/high16 v1, 0x437f0000  # 255.0f

    invoke-static {v0, v1}, Ljava/lang/Math;->min(FF)F

    move-result v0

    float-to-int v0, v0

    return v0
.end method

.method private rgbToColor([I)I
    .registers 4

    const/4 v0, 0x0

    aget v0, p1, v0

    shl-int/lit8 v0, v0, 0x18

    const/4 v1, 0x1

    aget v1, p1, v1

    shl-int/lit8 v1, v1, 0x10

    add-int/2addr v0, v1

    const/4 v1, 0x2

    aget v1, p1, v1

    shl-int/lit8 v1, v1, 0x8

    add-int/2addr v0, v1

    const/4 v1, 0x3

    aget v1, p1, v1

    add-int/2addr v0, v1

    return v0
.end method

.method private setProgress(I)V
    .registers 12

    const-wide/high16 v6, 0x4059000000000000L  # 100.0

    const-wide/high16 v8, 0x3fe0000000000000L  # 0.5

    iget-boolean v3, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->vertical:Z

    if-eqz v3, :cond_46

    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/BatteryBar;->getHeight()I

    move-result v3

    int-to-double v4, v3

    div-double/2addr v4, v6

    int-to-double v6, p1

    mul-double/2addr v4, v6

    add-double/2addr v4, v8

    double-to-int v2, v4

    iget-object v3, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mBatteryBarLayout:Landroid/widget/LinearLayout;

    invoke-virtual {v3}, Landroid/widget/LinearLayout;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v0

    check-cast v0, Landroid/widget/RelativeLayout$LayoutParams;

    iput v2, v0, Landroid/widget/RelativeLayout$LayoutParams;->height:I

    iget-object v3, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mBatteryBarLayout:Landroid/widget/LinearLayout;

    invoke-virtual {v3, v0}, Landroid/widget/LinearLayout;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    :goto_21
    iget-boolean v3, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->useGradientColor:Z

    if-eqz v3, :cond_60

    int-to-float v3, p1

    const/high16 v4, 0x42c80000  # 100.0f

    div-float v1, v3, v4

    iget-object v3, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mGradientColors:[I

    iget v4, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mHighColor:I

    iget v5, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mLowColor:I

    invoke-direct {p0, v4, v5, v1}, Lcom/android/systemui/statusbar/policy/BatteryBar;->mixColors(IIF)I

    move-result v4

    const/4 v5, 0x1

    aput v4, v3, v5

    iget-object v3, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mBarGradient:Landroid/graphics/drawable/GradientDrawable;

    iget-object v4, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mGradientColors:[I

    invoke-virtual {v3, v4}, Landroid/graphics/drawable/GradientDrawable;->setColors([I)V

    iget-object v3, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mBatteryBar:Landroid/view/View;

    iget-object v4, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mBarGradient:Landroid/graphics/drawable/GradientDrawable;

    invoke-virtual {v3, v4}, Landroid/view/View;->setBackgroundDrawable(Landroid/graphics/drawable/Drawable;)V

    :goto_45
    return-void

    :cond_46
    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/BatteryBar;->getWidth()I

    move-result v3

    int-to-double v4, v3

    div-double/2addr v4, v6

    int-to-double v6, p1

    mul-double/2addr v4, v6

    add-double/2addr v4, v8

    double-to-int v2, v4

    iget-object v3, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mBatteryBarLayout:Landroid/widget/LinearLayout;

    invoke-virtual {v3}, Landroid/widget/LinearLayout;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v0

    check-cast v0, Landroid/widget/RelativeLayout$LayoutParams;

    iput v2, v0, Landroid/widget/RelativeLayout$LayoutParams;->width:I

    iget-object v3, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mBatteryBarLayout:Landroid/widget/LinearLayout;

    invoke-virtual {v3, v0}, Landroid/widget/LinearLayout;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    goto :goto_21

    :cond_60
    iget-object v4, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mBatteryBar:Landroid/view/View;

    iget-boolean v3, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mBatteryCharging:Z

    if-eqz v3, :cond_6c

    iget v3, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mChargingColor:I

    :goto_68
    invoke-virtual {v4, v3}, Landroid/view/View;->setBackgroundColor(I)V

    goto :goto_45

    :cond_6c
    const/16 v3, 0xf

    if-le p1, v3, :cond_73

    iget v3, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mColor:I

    goto :goto_68

    :cond_73
    iget v3, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mBatteryLowColorWarning:I

    goto :goto_68
.end method

.method private updateSettings()V
    .registers 6

    const/4 v4, -0x1

    const/4 v2, 0x1

    const/4 v3, 0x0

    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/BatteryBar;->getContext()Landroid/content/Context;

    move-result-object v1

    invoke-virtual {v1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string/jumbo v1, "statusbar_battery_bar_color"

    invoke-static {v0, v1, v4}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v1

    iput v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mColor:I

    const-string/jumbo v1, "statusbar_battery_bar_charging_color"

    invoke-static {v0, v1, v4}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v1

    iput v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mChargingColor:I

    const-string/jumbo v1, "statusbar_battery_bar_battery_low_color_warning"

    invoke-static {v0, v1, v4}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v1

    iput v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mBatteryLowColorWarning:I

    const-string/jumbo v1, "statusbar_battery_bar_low_color2"

    const v4, -0xff2101

    invoke-static {v0, v1, v4}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v1

    iput v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mLowColor:I

    const-string/jumbo v1, "statusbar_battery_bar_high_color"

    const v4, -0xffe701

    invoke-static {v0, v1, v4}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v1

    iput v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mHighColor:I

    const-string/jumbo v1, "statusbar_battery_bar_animate"

    invoke-static {v0, v1, v3}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v1

    if-ne v1, v2, :cond_73

    move v1, v2

    :goto_48
    iput-boolean v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->shouldAnimateCharging:Z

    const-string/jumbo v1, "statusbar_battery_bar_use_gradient_color"

    invoke-static {v0, v1, v3}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v1

    if-ne v1, v2, :cond_75

    :goto_53
    iput-boolean v2, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->useGradientColor:Z

    iget-boolean v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mBatteryCharging:Z

    if-eqz v1, :cond_77

    iget v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mBatteryLevel:I

    const/16 v2, 0x64

    if-ge v1, v2, :cond_77

    iget-boolean v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->shouldAnimateCharging:Z

    if-eqz v1, :cond_77

    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/BatteryBar;->start()V

    :goto_66
    iget v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mBatteryLevel:I

    invoke-direct {p0, v1}, Lcom/android/systemui/statusbar/policy/BatteryBar;->setProgress(I)V

    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mCharger:Landroid/view/View;

    iget v2, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mChargingColor:I

    invoke-virtual {v1, v2}, Landroid/view/View;->setBackgroundColor(I)V

    return-void

    :cond_73
    move v1, v3

    goto :goto_48

    :cond_75
    move v2, v3

    goto :goto_53

    :cond_77
    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/BatteryBar;->stop()V

    goto :goto_66
.end method


# virtual methods
.method public isRunning()Z
    .registers 2

    iget-boolean v0, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->isAnimating:Z

    return v0
.end method

.method protected onAttachedToWindow()V
    .registers 9

    goto/32 :goto_119

    nop

    :goto_4
    iget-object v4, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mChargerLayout:Landroid/widget/LinearLayout;

    goto/32 :goto_af

    nop

    :goto_a
    invoke-super {p0}, Landroid/widget/RelativeLayout;->onAttachedToWindow()V

    goto/32 :goto_dc

    nop

    :goto_11
    return-void

    :goto_12
    goto/32 :goto_68

    nop

    :goto_16
    iget-object v4, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mBatteryBarLayout:Landroid/widget/LinearLayout;

    goto/32 :goto_bc

    nop

    :goto_1c
    invoke-virtual {v2}, Lcom/android/systemui/statusbar/policy/BatteryBar$SettingsObserver;->observer()V

    goto/32 :goto_1db

    nop

    :goto_23
    new-instance v4, Landroid/view/View;

    goto/32 :goto_89

    nop

    :goto_29
    const/high16 v5, 0x3f000000  # 0.5f

    goto/32 :goto_5e

    nop

    :goto_2f
    iget-object v4, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mHandler:Landroid/os/Handler;

    goto/32 :goto_c8

    nop

    :goto_35
    const/4 v7, 0x0

    goto/32 :goto_4a

    nop

    :goto_3a
    invoke-direct {v6, v7, v7}, Landroid/widget/LinearLayout$LayoutParams;-><init>(II)V

    goto/32 :goto_1e2

    nop

    :goto_41
    if-eqz v4, :cond_46

    goto/32 :goto_1de

    :cond_46
    goto/32 :goto_16a

    nop

    :goto_4a
    invoke-virtual {v4, v5, v0, v7, v6}, Landroid/content/Context;->registerReceiver(Landroid/content/BroadcastReceiver;Landroid/content/IntentFilter;Ljava/lang/String;Landroid/os/Handler;)Landroid/content/Intent;

    goto/32 :goto_e2

    nop

    :goto_51
    new-instance v5, Landroid/widget/RelativeLayout$LayoutParams;

    goto/32 :goto_1b9

    nop

    :goto_57
    const-string/jumbo v4, "android.intent.action.BATTERY_CHANGED"

    goto/32 :goto_b5

    nop

    :goto_5e
    add-float/2addr v4, v5

    goto/32 :goto_151

    nop

    :goto_63
    mul-float/2addr v4, v5

    goto/32 :goto_29

    nop

    :goto_68
    iget-object v4, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mChargerLayout:Landroid/widget/LinearLayout;

    goto/32 :goto_1cc

    nop

    :goto_6e
    iget-object v5, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mIntentReceiver:Landroid/content/BroadcastReceiver;

    goto/32 :goto_e8

    nop

    :goto_74
    iget-boolean v4, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->vertical:Z

    goto/32 :goto_1d2

    nop

    :goto_7a
    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/BatteryBar;->getContext()Landroid/content/Context;

    move-result-object v4

    goto/32 :goto_6e

    nop

    :goto_82
    invoke-direct {v4, v5}, Landroid/widget/LinearLayout;-><init>(Landroid/content/Context;)V

    goto/32 :goto_16f

    nop

    :goto_89
    iget-object v5, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mContext:Landroid/content/Context;

    goto/32 :goto_a2

    nop

    :goto_8f
    const/16 v5, 0x8

    goto/32 :goto_124

    nop

    :goto_95
    invoke-virtual {v0, v4}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    goto/32 :goto_7a

    nop

    :goto_9c
    iget-object v5, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mContext:Landroid/content/Context;

    goto/32 :goto_197

    nop

    :goto_a2
    invoke-direct {v4, v5}, Landroid/view/View;-><init>(Landroid/content/Context;)V

    goto/32 :goto_10c

    nop

    :goto_a9
    iget v4, v1, Landroid/util/DisplayMetrics;->density:F

    goto/32 :goto_1c0

    nop

    :goto_af
    iget-object v5, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mCharger:Landroid/view/View;

    goto/32 :goto_1a5

    nop

    :goto_b5
    invoke-virtual {v0, v4}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    goto/32 :goto_190

    nop

    :goto_bc
    iget-object v5, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mBatteryBar:Landroid/view/View;

    goto/32 :goto_18a

    nop

    :goto_c2
    iput-boolean v4, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mAttached:Z

    goto/32 :goto_1c6

    nop

    :goto_c8
    invoke-direct {v2, p0, v4}, Lcom/android/systemui/statusbar/policy/BatteryBar$SettingsObserver;-><init>(Lcom/android/systemui/statusbar/policy/BatteryBar;Landroid/os/Handler;)V

    goto/32 :goto_1c

    nop

    :goto_cf
    invoke-direct {v5, v7, v3}, Landroid/widget/RelativeLayout$LayoutParams;-><init>(II)V

    goto/32 :goto_175

    nop

    :goto_d6
    iget-object v5, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mContext:Landroid/content/Context;

    goto/32 :goto_82

    nop

    :goto_dc
    iget-boolean v4, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mAttached:Z

    goto/32 :goto_41

    nop

    :goto_e2
    new-instance v2, Lcom/android/systemui/statusbar/policy/BatteryBar$SettingsObserver;

    goto/32 :goto_2f

    nop

    :goto_e8
    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/BatteryBar;->getHandler()Landroid/os/Handler;

    move-result-object v6

    goto/32 :goto_35

    nop

    :goto_f0
    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/BatteryBar;->getContext()Landroid/content/Context;

    move-result-object v4

    goto/32 :goto_149

    nop

    :goto_f8
    iget-object v4, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mChargerLayout:Landroid/widget/LinearLayout;

    goto/32 :goto_137

    nop

    :goto_fe
    invoke-virtual {v0, v4}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    goto/32 :goto_19e

    nop

    :goto_105
    invoke-virtual {v4, v5, v6}, Landroid/widget/LinearLayout;->addView(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    goto/32 :goto_f0

    nop

    :goto_10c
    iput-object v4, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mCharger:Landroid/view/View;

    goto/32 :goto_11e

    nop

    :goto_112
    invoke-virtual {p0, v4, v5}, Lcom/android/systemui/statusbar/policy/BatteryBar;->addView(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    goto/32 :goto_12b

    nop

    :goto_119
    const/4 v7, -0x1

    goto/32 :goto_a

    nop

    :goto_11e
    iget-object v4, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mChargerLayout:Landroid/widget/LinearLayout;

    goto/32 :goto_8f

    nop

    :goto_124
    invoke-virtual {v4, v5}, Landroid/widget/LinearLayout;->setVisibility(I)V

    goto/32 :goto_4

    nop

    :goto_12b
    new-instance v4, Landroid/view/View;

    goto/32 :goto_164

    nop

    :goto_131
    new-instance v4, Landroid/widget/LinearLayout;

    goto/32 :goto_d6

    nop

    :goto_137
    new-instance v5, Landroid/widget/RelativeLayout$LayoutParams;

    goto/32 :goto_cf

    nop

    :goto_13d
    iget-object v4, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mBatteryBarLayout:Landroid/widget/LinearLayout;

    goto/32 :goto_51

    nop

    :goto_143
    iput-object v4, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mBatteryBar:Landroid/view/View;

    goto/32 :goto_16

    nop

    :goto_149
    invoke-virtual {v4}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v4

    goto/32 :goto_1ab

    nop

    :goto_151
    float-to-int v3, v4

    goto/32 :goto_131

    nop

    :goto_156
    invoke-virtual {p0, v4, v5}, Lcom/android/systemui/statusbar/policy/BatteryBar;->addView(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    goto/32 :goto_183

    nop

    :goto_15d
    invoke-direct {v6, v7, v7}, Landroid/widget/LinearLayout$LayoutParams;-><init>(II)V

    goto/32 :goto_105

    nop

    :goto_164
    iget-object v5, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mContext:Landroid/content/Context;

    goto/32 :goto_1f0

    nop

    :goto_16a
    const/4 v4, 0x1

    goto/32 :goto_c2

    nop

    :goto_16f
    iput-object v4, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mChargerLayout:Landroid/widget/LinearLayout;

    goto/32 :goto_74

    nop

    :goto_175
    invoke-virtual {p0, v4, v5}, Lcom/android/systemui/statusbar/policy/BatteryBar;->addView(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    :goto_178
    goto/32 :goto_23

    nop

    :goto_17c
    invoke-direct {v5, v3, v7}, Landroid/widget/RelativeLayout$LayoutParams;-><init>(II)V

    goto/32 :goto_156

    nop

    :goto_183
    goto :goto_178

    :goto_184
    iput-object v4, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mBatteryBarLayout:Landroid/widget/LinearLayout;

    goto/32 :goto_13d

    nop

    :goto_18a
    new-instance v6, Landroid/widget/LinearLayout$LayoutParams;

    goto/32 :goto_15d

    nop

    :goto_190
    const-string/jumbo v4, "android.intent.action.SCREEN_OFF"

    goto/32 :goto_fe

    nop

    :goto_197
    invoke-direct {v4, v5}, Landroid/widget/LinearLayout;-><init>(Landroid/content/Context;)V

    goto/32 :goto_184

    nop

    :goto_19e
    const-string/jumbo v4, "android.intent.action.SCREEN_ON"

    goto/32 :goto_95

    nop

    :goto_1a5
    new-instance v6, Landroid/widget/LinearLayout$LayoutParams;

    goto/32 :goto_3a

    nop

    :goto_1ab
    invoke-virtual {v4}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;

    move-result-object v1

    goto/32 :goto_a9

    nop

    :goto_1b3
    new-instance v0, Landroid/content/IntentFilter;

    goto/32 :goto_1e9

    nop

    :goto_1b9
    invoke-direct {v5, v7, v7}, Landroid/widget/RelativeLayout$LayoutParams;-><init>(II)V

    goto/32 :goto_112

    nop

    :goto_1c0
    const/high16 v5, 0x40800000  # 4.0f

    goto/32 :goto_63

    nop

    :goto_1c6
    new-instance v4, Landroid/widget/LinearLayout;

    goto/32 :goto_9c

    nop

    :goto_1cc
    new-instance v5, Landroid/widget/RelativeLayout$LayoutParams;

    goto/32 :goto_17c

    nop

    :goto_1d2
    if-nez v4, :cond_1d7

    goto/32 :goto_12

    :cond_1d7
    goto/32 :goto_f8

    nop

    :goto_1db
    invoke-direct {p0}, Lcom/android/systemui/statusbar/policy/BatteryBar;->updateSettings()V

    :goto_1de
    goto/32 :goto_11

    nop

    :goto_1e2
    invoke-virtual {v4, v5, v6}, Landroid/widget/LinearLayout;->addView(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    goto/32 :goto_1b3

    nop

    :goto_1e9
    invoke-direct {v0}, Landroid/content/IntentFilter;-><init>()V

    goto/32 :goto_57

    nop

    :goto_1f0
    invoke-direct {v4, v5}, Landroid/view/View;-><init>(Landroid/content/Context;)V

    goto/32 :goto_143

    nop
.end method

.method protected onDetachedFromWindow()V
    .registers 3

    goto/32 :goto_4

    nop

    :goto_4
    invoke-super {p0}, Landroid/widget/RelativeLayout;->onDetachedFromWindow()V

    goto/32 :goto_2e

    nop

    :goto_b
    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mIntentReceiver:Landroid/content/BroadcastReceiver;

    goto/32 :goto_34

    nop

    :goto_11
    return-void

    :goto_12
    const/4 v0, 0x0

    goto/32 :goto_28

    nop

    :goto_17
    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/BatteryBar;->getContext()Landroid/content/Context;

    move-result-object v0

    goto/32 :goto_b

    nop

    :goto_1f
    if-nez v0, :cond_24

    goto/32 :goto_37

    :cond_24
    goto/32 :goto_12

    nop

    :goto_28
    iput-boolean v0, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mAttached:Z

    goto/32 :goto_17

    nop

    :goto_2e
    iget-boolean v0, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mAttached:Z

    goto/32 :goto_1f

    nop

    :goto_34
    invoke-virtual {v0, v1}, Landroid/content/Context;->unregisterReceiver(Landroid/content/BroadcastReceiver;)V

    :goto_37
    goto/32 :goto_11

    nop
.end method

.method public start()V
    .registers 11

    const-wide/16 v8, 0x3e8

    const/4 v6, 0x0

    const/4 v5, -0x1

    iget-boolean v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->shouldAnimateCharging:Z

    if-nez v1, :cond_9

    return-void

    :cond_9
    iget-boolean v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->vertical:Z

    if-eqz v1, :cond_42

    new-instance v0, Landroid/view/animation/TranslateAnimation;

    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/BatteryBar;->getX()F

    move-result v1

    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/BatteryBar;->getX()F

    move-result v2

    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/BatteryBar;->getHeight()I

    move-result v3

    int-to-float v3, v3

    iget-object v4, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mBatteryBarLayout:Landroid/widget/LinearLayout;

    invoke-virtual {v4}, Landroid/widget/LinearLayout;->getHeight()I

    move-result v4

    int-to-float v4, v4

    invoke-direct {v0, v1, v2, v3, v4}, Landroid/view/animation/TranslateAnimation;-><init>(FFFF)V

    new-instance v1, Landroid/view/animation/AccelerateInterpolator;

    invoke-direct {v1}, Landroid/view/animation/AccelerateInterpolator;-><init>()V

    invoke-virtual {v0, v1}, Landroid/view/animation/TranslateAnimation;->setInterpolator(Landroid/view/animation/Interpolator;)V

    invoke-virtual {v0, v8, v9}, Landroid/view/animation/TranslateAnimation;->setDuration(J)V

    invoke-virtual {v0, v5}, Landroid/view/animation/TranslateAnimation;->setRepeatCount(I)V

    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mChargerLayout:Landroid/widget/LinearLayout;

    invoke-virtual {v1, v0}, Landroid/widget/LinearLayout;->startAnimation(Landroid/view/animation/Animation;)V

    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mChargerLayout:Landroid/widget/LinearLayout;

    invoke-virtual {v1, v6}, Landroid/widget/LinearLayout;->setVisibility(I)V

    :goto_3e
    const/4 v1, 0x1

    iput-boolean v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->isAnimating:Z

    return-void

    :cond_42
    new-instance v0, Landroid/view/animation/TranslateAnimation;

    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/BatteryBar;->getWidth()I

    move-result v1

    int-to-float v1, v1

    iget-object v2, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mBatteryBarLayout:Landroid/widget/LinearLayout;

    invoke-virtual {v2}, Landroid/widget/LinearLayout;->getWidth()I

    move-result v2

    int-to-float v2, v2

    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/BatteryBar;->getTop()I

    move-result v3

    int-to-float v3, v3

    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/BatteryBar;->getTop()I

    move-result v4

    int-to-float v4, v4

    invoke-direct {v0, v1, v2, v3, v4}, Landroid/view/animation/TranslateAnimation;-><init>(FFFF)V

    new-instance v1, Landroid/view/animation/AccelerateInterpolator;

    invoke-direct {v1}, Landroid/view/animation/AccelerateInterpolator;-><init>()V

    invoke-virtual {v0, v1}, Landroid/view/animation/TranslateAnimation;->setInterpolator(Landroid/view/animation/Interpolator;)V

    invoke-virtual {v0, v8, v9}, Landroid/view/animation/TranslateAnimation;->setDuration(J)V

    invoke-virtual {v0, v5}, Landroid/view/animation/TranslateAnimation;->setRepeatCount(I)V

    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mChargerLayout:Landroid/widget/LinearLayout;

    invoke-virtual {v1, v0}, Landroid/widget/LinearLayout;->startAnimation(Landroid/view/animation/Animation;)V

    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mChargerLayout:Landroid/widget/LinearLayout;

    invoke-virtual {v1, v6}, Landroid/widget/LinearLayout;->setVisibility(I)V

    goto :goto_3e
.end method

.method public stop()V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mChargerLayout:Landroid/widget/LinearLayout;

    invoke-virtual {v0}, Landroid/widget/LinearLayout;->clearAnimation()V

    iget-object v0, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->mChargerLayout:Landroid/widget/LinearLayout;

    const/16 v1, 0x8

    invoke-virtual {v0, v1}, Landroid/widget/LinearLayout;->setVisibility(I)V

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/android/systemui/statusbar/policy/BatteryBar;->isAnimating:Z

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_statusbar_policy_BatteryBar',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
