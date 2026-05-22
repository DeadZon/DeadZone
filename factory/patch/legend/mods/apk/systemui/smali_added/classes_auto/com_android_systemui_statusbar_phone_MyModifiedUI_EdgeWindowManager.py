"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager.smali'
CLASS_FALLBACK_NAMES = ['EdgeWindowManager.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;
.super Ljava/lang/Object;

# interfaces
.implements Lcom/android/systemui/statusbar/policy/ConfigurationController$ConfigurationListener;


# static fields
.field private static sInstance:Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;


# instance fields
.field private isCharging:Z

.field private isStarted:Z

.field private mBgDrawable:Landroid/graphics/drawable/AnimationDrawable;

.field private mBgDrawableLand:Landroid/graphics/drawable/AnimationDrawable;

.field private final mContext:Landroid/content/Context;

.field private mEnableChargeAnim:Z

.field private mImageLeft:Landroid/widget/ImageView;

.field private mImageRight:Landroid/widget/ImageView;

.field private final mKeyguardUpdateMonitorCallback:Lcom/android/keyguard/KeyguardUpdateMonitorCallback;

.field private mLeftPar:Landroid/view/WindowManager$LayoutParams;

.field private mLeftParChanged:Landroid/view/WindowManager$LayoutParams;

.field private mOrientation:I

.field private mRightPar:Landroid/view/WindowManager$LayoutParams;

.field private mRightParChanged:Landroid/view/WindowManager$LayoutParams;

.field private final mUpdateMonitor:Lcom/android/keyguard/KeyguardUpdateMonitor;

.field private mWindowManager:Landroid/view/WindowManager;


# direct methods
.method private constructor <init>(Landroid/content/Context;)V
    .registers 7

    const/4 v0, 0x1

    const/4 v1, 0x0

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    iput-boolean v1, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->isStarted:Z

    iput-boolean v1, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->isCharging:Z

    iput-object p1, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {p1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v2

    const-string v3, "lightning_animation"

    invoke-static {v2, v3, v1}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v2

    if-le v2, v0, :cond_2d

    :goto_17
    iput-boolean v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mEnableChargeAnim:Z

    sget-object v4, Lcom/android/systemui/Dependency;->sDependency:Lcom/android/systemui/Dependency;

    const-class v0, Lcom/android/keyguard/KeyguardUpdateMonitor;

    invoke-virtual {v4, v0}, Lcom/android/systemui/Dependency;->getDependencyInner(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/keyguard/KeyguardUpdateMonitor;

    iput-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mUpdateMonitor:Lcom/android/keyguard/KeyguardUpdateMonitor;

    new-instance v0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager$1;

    invoke-direct {v0, p0}, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager$1;-><init>(Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;)V

    iput-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mKeyguardUpdateMonitorCallback:Lcom/android/keyguard/KeyguardUpdateMonitorCallback;

    return-void

    :cond_2d
    move v0, v1

    goto :goto_17
.end method

.method static synthetic access$002(Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;Z)Z
    .registers 2

    iput-boolean p1, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->isCharging:Z

    return p1
.end method

.method static synthetic access$100(Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;)V
    .registers 1

    invoke-direct {p0}, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->updateView()V

    return-void
.end method

.method private apply()V
    .registers 4

    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mLeftParChanged:Landroid/view/WindowManager$LayoutParams;

    const/4 v1, 0x1

    invoke-direct {p0, v0, v1}, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->applyOrientation(Landroid/view/WindowManager$LayoutParams;Z)V

    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mRightParChanged:Landroid/view/WindowManager$LayoutParams;

    const/4 v1, 0x0

    invoke-direct {p0, v0, v1}, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->applyOrientation(Landroid/view/WindowManager$LayoutParams;Z)V

    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mLeftPar:Landroid/view/WindowManager$LayoutParams;

    iget-object v1, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mLeftParChanged:Landroid/view/WindowManager$LayoutParams;

    invoke-virtual {v0, v1}, Landroid/view/WindowManager$LayoutParams;->copyFrom(Landroid/view/WindowManager$LayoutParams;)I

    move-result v0

    if-eqz v0, :cond_1f

    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mWindowManager:Landroid/view/WindowManager;

    iget-object v1, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mImageLeft:Landroid/widget/ImageView;

    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mLeftPar:Landroid/view/WindowManager$LayoutParams;

    invoke-interface {v0, v1, v2}, Landroid/view/WindowManager;->updateViewLayout(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    :cond_1f
    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mRightPar:Landroid/view/WindowManager$LayoutParams;

    iget-object v1, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mRightParChanged:Landroid/view/WindowManager$LayoutParams;

    invoke-virtual {v0, v1}, Landroid/view/WindowManager$LayoutParams;->copyFrom(Landroid/view/WindowManager$LayoutParams;)I

    move-result v0

    if-eqz v0, :cond_32

    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mWindowManager:Landroid/view/WindowManager;

    iget-object v1, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mImageRight:Landroid/widget/ImageView;

    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mRightPar:Landroid/view/WindowManager$LayoutParams;

    invoke-interface {v0, v1, v2}, Landroid/view/WindowManager;->updateViewLayout(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    :cond_32
    return-void
.end method

.method private applyOrientation(Landroid/view/WindowManager$LayoutParams;Z)V
    .registers 9

    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mContext:Landroid/content/Context;

    const-string v1, "window"

    invoke-virtual {v0, v1}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/view/WindowManager;

    invoke-interface {v0}, Landroid/view/WindowManager;->getDefaultDisplay()Landroid/view/Display;

    move-result-object v1

    new-instance v2, Landroid/util/DisplayMetrics;

    invoke-direct {v2}, Landroid/util/DisplayMetrics;-><init>()V

    invoke-virtual {v1, v2}, Landroid/view/Display;->getMetrics(Landroid/util/DisplayMetrics;)V

    iget v4, v2, Landroid/util/DisplayMetrics;->widthPixels:I

    iget v5, v2, Landroid/util/DisplayMetrics;->heightPixels:I

    iput v5, p1, Landroid/view/WindowManager$LayoutParams;->height:I

    const/16 v4, 0x44

    const/high16 v3, 0x43340000  # 180.0f

    const/4 v2, 0x0

    iget v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mOrientation:I

    const/4 v1, 0x1

    if-ne v0, v1, :cond_42

    iput v5, p1, Landroid/view/WindowManager$LayoutParams;->height:I

    iput v4, p1, Landroid/view/WindowManager$LayoutParams;->width:I

    if-eqz p2, :cond_3a

    const/4 v0, 0x3

    :goto_2d
    iput v0, p1, Landroid/view/WindowManager$LayoutParams;->gravity:I

    if-eqz p2, :cond_3c

    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mImageLeft:Landroid/widget/ImageView;

    invoke-virtual {v0, v2}, Landroid/widget/ImageView;->setRotation(F)V

    :goto_36
    invoke-direct {p0}, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->updateView()V

    return-void

    :cond_3a
    const/4 v0, 0x5

    goto :goto_2d

    :cond_3c
    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mImageRight:Landroid/widget/ImageView;

    invoke-virtual {v0, v3}, Landroid/widget/ImageView;->setRotation(F)V

    goto :goto_36

    :cond_42
    iput v4, p1, Landroid/view/WindowManager$LayoutParams;->height:I

    iput v5, p1, Landroid/view/WindowManager$LayoutParams;->width:I

    if-eqz p2, :cond_54

    const/16 v0, 0x50

    :goto_4a
    iput v0, p1, Landroid/view/WindowManager$LayoutParams;->gravity:I

    if-eqz p2, :cond_57

    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mImageLeft:Landroid/widget/ImageView;

    invoke-virtual {v0, v2}, Landroid/widget/ImageView;->setRotation(F)V

    goto :goto_36

    :cond_54
    const/16 v0, 0x30

    goto :goto_4a

    :cond_57
    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mImageRight:Landroid/widget/ImageView;

    invoke-virtual {v0, v3}, Landroid/widget/ImageView;->setRotation(F)V

    goto :goto_36
.end method

.method private createLayoutParams()V
    .registers 5

    new-instance v0, Landroid/view/WindowManager$LayoutParams;

    const/16 v1, 0x7e8

    const v2, 0xc000738

    const/4 v3, -0x3

    invoke-direct {v0, v1, v2, v3}, Landroid/view/WindowManager$LayoutParams;-><init>(III)V

    iput-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mLeftPar:Landroid/view/WindowManager$LayoutParams;

    new-instance v0, Landroid/view/WindowManager$LayoutParams;

    invoke-direct {v0}, Landroid/view/WindowManager$LayoutParams;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mRightPar:Landroid/view/WindowManager$LayoutParams;

    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mRightPar:Landroid/view/WindowManager$LayoutParams;

    iget-object v1, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mLeftPar:Landroid/view/WindowManager$LayoutParams;

    invoke-virtual {v0, v1}, Landroid/view/WindowManager$LayoutParams;->copyFrom(Landroid/view/WindowManager$LayoutParams;)I

    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mLeftPar:Landroid/view/WindowManager$LayoutParams;

    const/4 v1, 0x1

    invoke-direct {p0, v0, v1}, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->applyOrientation(Landroid/view/WindowManager$LayoutParams;Z)V

    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mRightPar:Landroid/view/WindowManager$LayoutParams;

    const/4 v1, 0x0

    invoke-direct {p0, v0, v1}, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->applyOrientation(Landroid/view/WindowManager$LayoutParams;Z)V

    new-instance v0, Landroid/view/WindowManager$LayoutParams;

    invoke-direct {v0}, Landroid/view/WindowManager$LayoutParams;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mRightParChanged:Landroid/view/WindowManager$LayoutParams;

    new-instance v0, Landroid/view/WindowManager$LayoutParams;

    invoke-direct {v0}, Landroid/view/WindowManager$LayoutParams;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mLeftParChanged:Landroid/view/WindowManager$LayoutParams;

    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mLeftParChanged:Landroid/view/WindowManager$LayoutParams;

    iget-object v1, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mLeftPar:Landroid/view/WindowManager$LayoutParams;

    invoke-virtual {v0, v1}, Landroid/view/WindowManager$LayoutParams;->copyFrom(Landroid/view/WindowManager$LayoutParams;)I

    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mRightParChanged:Landroid/view/WindowManager$LayoutParams;

    iget-object v1, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mRightPar:Landroid/view/WindowManager$LayoutParams;

    invoke-virtual {v0, v1}, Landroid/view/WindowManager$LayoutParams;->copyFrom(Landroid/view/WindowManager$LayoutParams;)I

    return-void
.end method

.method private createView()V
    .registers 3

    new-instance v0, Landroid/widget/ImageView;

    iget-object v1, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mContext:Landroid/content/Context;

    invoke-direct {v0, v1}, Landroid/widget/ImageView;-><init>(Landroid/content/Context;)V

    iput-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mImageLeft:Landroid/widget/ImageView;

    new-instance v0, Landroid/widget/ImageView;

    iget-object v1, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mContext:Landroid/content/Context;

    invoke-direct {v0, v1}, Landroid/widget/ImageView;-><init>(Landroid/content/Context;)V

    iput-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mImageRight:Landroid/widget/ImageView;

    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mImageLeft:Landroid/widget/ImageView;

    sget-object v1, Landroid/widget/ImageView$ScaleType;->FIT_XY:Landroid/widget/ImageView$ScaleType;

    invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setScaleType(Landroid/widget/ImageView$ScaleType;)V

    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mImageRight:Landroid/widget/ImageView;

    sget-object v1, Landroid/widget/ImageView$ScaleType;->FIT_XY:Landroid/widget/ImageView$ScaleType;

    invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setScaleType(Landroid/widget/ImageView$ScaleType;)V

    return-void
.end method

.method public static declared-synchronized getInstance(Landroid/content/Context;)Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;
    .registers 4

    const-class v1, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;

    monitor-enter v1

    :try_start_3
    const-class v2, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;

    monitor-enter v2
    :try_end_6
    .catchall {:try_start_3 .. :try_end_6} :catchall_19

    :try_start_6
    sget-object v0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->sInstance:Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;

    if-nez v0, :cond_11

    new-instance v0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;

    invoke-direct {v0, p0}, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;-><init>(Landroid/content/Context;)V

    sput-object v0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->sInstance:Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;

    :cond_11
    sget-object v0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->sInstance:Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;

    monitor-exit v2
    :try_end_14
    .catchall {:try_start_6 .. :try_end_14} :catchall_16

    monitor-exit v1

    return-object v0

    :catchall_16
    move-exception v0

    :try_start_17
    monitor-exit v2
    :try_end_18
    .catchall {:try_start_17 .. :try_end_18} :catchall_16

    :try_start_18
    throw v0
    :try_end_19
    .catchall {:try_start_18 .. :try_end_19} :catchall_19

    :catchall_19
    move-exception v0

    monitor-exit v1

    throw v0
.end method

.method private updateView()V
    .registers 7

    const/4 v5, 0x0

    iget v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mOrientation:I

    const/4 v3, 0x1

    if-ne v2, v3, :cond_90

    iget-boolean v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->isCharging:Z

    if-eqz v2, :cond_5d

    iget-boolean v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mEnableChargeAnim:Z

    if-eqz v2, :cond_5d

    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mBgDrawable:Landroid/graphics/drawable/AnimationDrawable;

    if-nez v2, :cond_5c

    new-instance v2, Lcom/android/systemui/statusbar/phone/MyModifiedUI/LightningBackground;

    iget-object v3, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mContext:Landroid/content/Context;

    const-string/jumbo v4, "vertlight"

    invoke-direct {v2, v3, v4}, Lcom/android/systemui/statusbar/phone/MyModifiedUI/LightningBackground;-><init>(Landroid/content/Context;Ljava/lang/String;)V

    iput-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mBgDrawable:Landroid/graphics/drawable/AnimationDrawable;

    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mBgDrawableLand:Landroid/graphics/drawable/AnimationDrawable;

    if-eqz v2, :cond_3e

    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mBgDrawableLand:Landroid/graphics/drawable/AnimationDrawable;

    invoke-virtual {v2}, Landroid/graphics/drawable/AnimationDrawable;->stop()V

    iput-object v5, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mBgDrawableLand:Landroid/graphics/drawable/AnimationDrawable;

    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mImageLeft:Landroid/widget/ImageView;

    invoke-virtual {v2}, Landroid/widget/ImageView;->getDrawable()Landroid/graphics/drawable/Drawable;

    move-result-object v2

    instance-of v2, v2, Landroid/graphics/drawable/AnimationDrawable;

    if-eqz v2, :cond_3e

    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mImageLeft:Landroid/widget/ImageView;

    invoke-virtual {v2}, Landroid/widget/ImageView;->getDrawable()Landroid/graphics/drawable/Drawable;

    move-result-object v2

    check-cast v2, Landroid/graphics/drawable/AnimationDrawable;

    invoke-virtual {v2}, Landroid/graphics/drawable/AnimationDrawable;->stop()V

    :cond_3e
    new-instance v0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/LightningBackground;

    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mContext:Landroid/content/Context;

    const-string/jumbo v3, "vertlight"

    invoke-direct {v0, v2, v3}, Lcom/android/systemui/statusbar/phone/MyModifiedUI/LightningBackground;-><init>(Landroid/content/Context;Ljava/lang/String;)V

    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mImageRight:Landroid/widget/ImageView;

    iget-object v3, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mBgDrawable:Landroid/graphics/drawable/AnimationDrawable;

    invoke-virtual {v2, v3}, Landroid/widget/ImageView;->setImageDrawable(Landroid/graphics/drawable/Drawable;)V

    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mImageLeft:Landroid/widget/ImageView;

    invoke-virtual {v2, v0}, Landroid/widget/ImageView;->setImageDrawable(Landroid/graphics/drawable/Drawable;)V

    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mBgDrawable:Landroid/graphics/drawable/AnimationDrawable;

    invoke-virtual {v2}, Landroid/graphics/drawable/AnimationDrawable;->start()V

    invoke-virtual {v0}, Landroid/graphics/drawable/AnimationDrawable;->start()V

    :cond_5c
    :goto_5c
    return-void

    :cond_5d
    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mBgDrawable:Landroid/graphics/drawable/AnimationDrawable;

    if-eqz v2, :cond_7d

    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mBgDrawable:Landroid/graphics/drawable/AnimationDrawable;

    invoke-virtual {v2}, Landroid/graphics/drawable/AnimationDrawable;->stop()V

    iput-object v5, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mBgDrawable:Landroid/graphics/drawable/AnimationDrawable;

    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mImageLeft:Landroid/widget/ImageView;

    invoke-virtual {v2}, Landroid/widget/ImageView;->getDrawable()Landroid/graphics/drawable/Drawable;

    move-result-object v2

    instance-of v2, v2, Landroid/graphics/drawable/AnimationDrawable;

    if-eqz v2, :cond_7d

    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mImageLeft:Landroid/widget/ImageView;

    invoke-virtual {v2}, Landroid/widget/ImageView;->getDrawable()Landroid/graphics/drawable/Drawable;

    move-result-object v2

    check-cast v2, Landroid/graphics/drawable/AnimationDrawable;

    invoke-virtual {v2}, Landroid/graphics/drawable/AnimationDrawable;->stop()V

    :cond_7d
    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mContext:Landroid/content/Context;

    const-string v3, "left_edge"

    invoke-static {v2, v3}, Landroid/Utils/Utils;->DrawableToID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v1

    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mImageLeft:Landroid/widget/ImageView;

    invoke-virtual {v2, v1}, Landroid/widget/ImageView;->setImageResource(I)V

    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mImageRight:Landroid/widget/ImageView;

    invoke-virtual {v2, v1}, Landroid/widget/ImageView;->setImageResource(I)V

    goto :goto_5c

    :cond_90
    iget-boolean v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->isCharging:Z

    if-eqz v2, :cond_e6

    iget-boolean v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mEnableChargeAnim:Z

    if-eqz v2, :cond_e6

    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mBgDrawableLand:Landroid/graphics/drawable/AnimationDrawable;

    if-nez v2, :cond_5c

    new-instance v2, Lcom/android/systemui/statusbar/phone/MyModifiedUI/LightningBackground;

    iget-object v3, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mContext:Landroid/content/Context;

    const-string v4, "light"

    invoke-direct {v2, v3, v4}, Lcom/android/systemui/statusbar/phone/MyModifiedUI/LightningBackground;-><init>(Landroid/content/Context;Ljava/lang/String;)V

    iput-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mBgDrawableLand:Landroid/graphics/drawable/AnimationDrawable;

    new-instance v0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/LightningBackground;

    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mContext:Landroid/content/Context;

    const-string v3, "light"

    invoke-direct {v0, v2, v3}, Lcom/android/systemui/statusbar/phone/MyModifiedUI/LightningBackground;-><init>(Landroid/content/Context;Ljava/lang/String;)V

    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mBgDrawable:Landroid/graphics/drawable/AnimationDrawable;

    if-eqz v2, :cond_d0

    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mBgDrawable:Landroid/graphics/drawable/AnimationDrawable;

    invoke-virtual {v2}, Landroid/graphics/drawable/AnimationDrawable;->stop()V

    iput-object v5, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mBgDrawable:Landroid/graphics/drawable/AnimationDrawable;

    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mImageLeft:Landroid/widget/ImageView;

    invoke-virtual {v2}, Landroid/widget/ImageView;->getDrawable()Landroid/graphics/drawable/Drawable;

    move-result-object v2

    instance-of v2, v2, Landroid/graphics/drawable/AnimationDrawable;

    if-eqz v2, :cond_d0

    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mImageLeft:Landroid/widget/ImageView;

    invoke-virtual {v2}, Landroid/widget/ImageView;->getDrawable()Landroid/graphics/drawable/Drawable;

    move-result-object v2

    check-cast v2, Landroid/graphics/drawable/AnimationDrawable;

    invoke-virtual {v2}, Landroid/graphics/drawable/AnimationDrawable;->stop()V

    :cond_d0
    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mImageRight:Landroid/widget/ImageView;

    iget-object v3, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mBgDrawableLand:Landroid/graphics/drawable/AnimationDrawable;

    invoke-virtual {v2, v3}, Landroid/widget/ImageView;->setImageDrawable(Landroid/graphics/drawable/Drawable;)V

    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mImageLeft:Landroid/widget/ImageView;

    invoke-virtual {v2, v0}, Landroid/widget/ImageView;->setImageDrawable(Landroid/graphics/drawable/Drawable;)V

    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mBgDrawableLand:Landroid/graphics/drawable/AnimationDrawable;

    invoke-virtual {v2}, Landroid/graphics/drawable/AnimationDrawable;->start()V

    invoke-virtual {v0}, Landroid/graphics/drawable/AnimationDrawable;->start()V

    goto/16 :goto_5c

    :cond_e6
    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mBgDrawableLand:Landroid/graphics/drawable/AnimationDrawable;

    if-eqz v2, :cond_106

    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mBgDrawableLand:Landroid/graphics/drawable/AnimationDrawable;

    invoke-virtual {v2}, Landroid/graphics/drawable/AnimationDrawable;->stop()V

    iput-object v5, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mBgDrawableLand:Landroid/graphics/drawable/AnimationDrawable;

    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mImageLeft:Landroid/widget/ImageView;

    invoke-virtual {v2}, Landroid/widget/ImageView;->getDrawable()Landroid/graphics/drawable/Drawable;

    move-result-object v2

    instance-of v2, v2, Landroid/graphics/drawable/AnimationDrawable;

    if-eqz v2, :cond_106

    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mImageLeft:Landroid/widget/ImageView;

    invoke-virtual {v2}, Landroid/widget/ImageView;->getDrawable()Landroid/graphics/drawable/Drawable;

    move-result-object v2

    check-cast v2, Landroid/graphics/drawable/AnimationDrawable;

    invoke-virtual {v2}, Landroid/graphics/drawable/AnimationDrawable;->stop()V

    :cond_106
    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mContext:Landroid/content/Context;

    const-string v3, "bottom_edge"

    invoke-static {v2, v3}, Landroid/Utils/Utils;->DrawableToID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v1

    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mImageLeft:Landroid/widget/ImageView;

    invoke-virtual {v2, v1}, Landroid/widget/ImageView;->setImageResource(I)V

    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mImageRight:Landroid/widget/ImageView;

    invoke-virtual {v2, v1}, Landroid/widget/ImageView;->setImageResource(I)V

    goto/16 :goto_5c
.end method


# virtual methods
.method public destroy()V
    .registers 5

    const/4 v2, 0x0

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->isStarted:Z

    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mWindowManager:Landroid/view/WindowManager;

    iget-object v1, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mImageLeft:Landroid/widget/ImageView;

    invoke-interface {v0, v1}, Landroid/view/WindowManager;->removeView(Landroid/view/View;)V

    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mWindowManager:Landroid/view/WindowManager;

    iget-object v1, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mImageRight:Landroid/widget/ImageView;

    invoke-interface {v0, v1}, Landroid/view/WindowManager;->removeView(Landroid/view/View;)V

    sget-object v3, Lcom/android/systemui/Dependency;->sDependency:Lcom/android/systemui/Dependency;

    const-class v0, Lcom/android/systemui/statusbar/policy/ConfigurationController;

    invoke-virtual {v3, v0}, Lcom/android/systemui/Dependency;->getDependencyInner(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/statusbar/policy/ConfigurationController;

    invoke-interface {v0, p0}, Lcom/android/systemui/statusbar/policy/ConfigurationController;->removeCallback(Ljava/lang/Object;)V

    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mUpdateMonitor:Lcom/android/keyguard/KeyguardUpdateMonitor;

    iget-object v1, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mKeyguardUpdateMonitorCallback:Lcom/android/keyguard/KeyguardUpdateMonitorCallback;

    invoke-virtual {v0, v1}, Lcom/android/keyguard/KeyguardUpdateMonitor;->removeCallback(Lcom/android/keyguard/KeyguardUpdateMonitorCallback;)V

    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mBgDrawableLand:Landroid/graphics/drawable/AnimationDrawable;

    if-eqz v0, :cond_46

    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mBgDrawableLand:Landroid/graphics/drawable/AnimationDrawable;

    invoke-virtual {v0}, Landroid/graphics/drawable/AnimationDrawable;->stop()V

    iput-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mBgDrawableLand:Landroid/graphics/drawable/AnimationDrawable;

    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mImageLeft:Landroid/widget/ImageView;

    invoke-virtual {v0}, Landroid/widget/ImageView;->getDrawable()Landroid/graphics/drawable/Drawable;

    move-result-object v0

    instance-of v0, v0, Landroid/graphics/drawable/AnimationDrawable;

    if-eqz v0, :cond_46

    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mImageLeft:Landroid/widget/ImageView;

    invoke-virtual {v0}, Landroid/widget/ImageView;->getDrawable()Landroid/graphics/drawable/Drawable;

    move-result-object v0

    check-cast v0, Landroid/graphics/drawable/AnimationDrawable;

    invoke-virtual {v0}, Landroid/graphics/drawable/AnimationDrawable;->stop()V

    :cond_46
    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mBgDrawable:Landroid/graphics/drawable/AnimationDrawable;

    if-eqz v0, :cond_66

    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mBgDrawable:Landroid/graphics/drawable/AnimationDrawable;

    invoke-virtual {v0}, Landroid/graphics/drawable/AnimationDrawable;->stop()V

    iput-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mBgDrawable:Landroid/graphics/drawable/AnimationDrawable;

    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mImageLeft:Landroid/widget/ImageView;

    invoke-virtual {v0}, Landroid/widget/ImageView;->getDrawable()Landroid/graphics/drawable/Drawable;

    move-result-object v0

    instance-of v0, v0, Landroid/graphics/drawable/AnimationDrawable;

    if-eqz v0, :cond_66

    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mImageLeft:Landroid/widget/ImageView;

    invoke-virtual {v0}, Landroid/widget/ImageView;->getDrawable()Landroid/graphics/drawable/Drawable;

    move-result-object v0

    check-cast v0, Landroid/graphics/drawable/AnimationDrawable;

    invoke-virtual {v0}, Landroid/graphics/drawable/AnimationDrawable;->stop()V

    :cond_66
    return-void
.end method

.method public isStarted()Z
    .registers 2

    iget-boolean v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->isStarted:Z

    return v0
.end method

.method public onConfigChanged(Landroid/content/res/Configuration;)V
    .registers 4

    iget v0, p1, Landroid/content/res/Configuration;->orientation:I

    iget v1, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mOrientation:I

    if-eq v0, v1, :cond_d

    iget v0, p1, Landroid/content/res/Configuration;->orientation:I

    iput v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mOrientation:I

    invoke-direct {p0}, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->apply()V

    :cond_d
    return-void
.end method

.method public onDensityOrFontScaleChanged()V
    .registers 1

    return-void
.end method

.method public start()V
    .registers 5

    const/4 v0, 0x1

    iput-boolean v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->isStarted:Z

    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    invoke-virtual {v0}, Landroid/content/res/Resources;->getConfiguration()Landroid/content/res/Configuration;

    move-result-object v0

    iget v0, v0, Landroid/content/res/Configuration;->orientation:I

    iput v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mOrientation:I

    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mContext:Landroid/content/Context;

    const-string/jumbo v1, "window"

    invoke-virtual {v0, v1}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/view/WindowManager;

    iput-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mWindowManager:Landroid/view/WindowManager;

    invoke-direct {p0}, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->createView()V

    invoke-direct {p0}, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->updateView()V

    invoke-direct {p0}, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->createLayoutParams()V

    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mWindowManager:Landroid/view/WindowManager;

    iget-object v1, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mImageLeft:Landroid/widget/ImageView;

    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mLeftPar:Landroid/view/WindowManager$LayoutParams;

    invoke-interface {v0, v1, v2}, Landroid/view/WindowManager;->addView(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mWindowManager:Landroid/view/WindowManager;

    iget-object v1, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mImageRight:Landroid/widget/ImageView;

    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mRightPar:Landroid/view/WindowManager$LayoutParams;

    invoke-interface {v0, v1, v2}, Landroid/view/WindowManager;->addView(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    sget-object v3, Lcom/android/systemui/Dependency;->sDependency:Lcom/android/systemui/Dependency;

    const-class v0, Lcom/android/systemui/statusbar/policy/ConfigurationController;

    invoke-virtual {v3, v0}, Lcom/android/systemui/Dependency;->getDependencyInner(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/statusbar/policy/ConfigurationController;

    invoke-interface {v0, p0}, Lcom/android/systemui/statusbar/policy/ConfigurationController;->addCallback(Ljava/lang/Object;)V

    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mUpdateMonitor:Lcom/android/keyguard/KeyguardUpdateMonitor;

    iget-object v1, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mKeyguardUpdateMonitorCallback:Lcom/android/keyguard/KeyguardUpdateMonitorCallback;

    invoke-virtual {v0, v1}, Lcom/android/keyguard/KeyguardUpdateMonitor;->registerCallback(Lcom/android/keyguard/KeyguardUpdateMonitorCallback;)V

    return-void
.end method

.method public updateVariables()V
    .registers 5

    const/4 v0, 0x1

    const/4 v1, 0x0

    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v2}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v2

    const-string v3, "lightning_animation"

    invoke-static {v2, v3, v1}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v2

    if-le v2, v0, :cond_1a

    :goto_10
    iput-boolean v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->mEnableChargeAnim:Z

    iget-boolean v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->isStarted:Z

    if-eqz v0, :cond_19

    invoke-direct {p0}, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->updateView()V

    :cond_19
    return-void

    :cond_1a
    move v0, v1

    goto :goto_10
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_statusbar_phone_MyModifiedUI_EdgeWindowManager',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
