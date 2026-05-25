"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/justas/AnimationWeather/SnowAnimation.smali'
CLASS_FALLBACK_NAMES = ['SnowAnimation.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/justas/AnimationWeather/SnowAnimation;
.super Landroid/widget/RelativeLayout;


# instance fields
.field private final mContext:Landroid/content/Context;

.field private mHandler:Landroid/os/Handler;

.field private final mLayoutParams:Landroid/widget/RelativeLayout$LayoutParams;

.field private mRunable:Ljava/lang/Runnable;


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 5

    const/4 v1, -0x2

    invoke-direct {p0, p1, p2}, Landroid/widget/RelativeLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    iput-object p1, p0, Lcom/justas/AnimationWeather/SnowAnimation;->mContext:Landroid/content/Context;

    new-instance v0, Landroid/widget/RelativeLayout$LayoutParams;

    invoke-direct {v0, v1, v1}, Landroid/widget/RelativeLayout$LayoutParams;-><init>(II)V

    iput-object v0, p0, Lcom/justas/AnimationWeather/SnowAnimation;->mLayoutParams:Landroid/widget/RelativeLayout$LayoutParams;

    return-void
.end method


# virtual methods
.method public final showAnimation(IIII)V
    .registers 23

    new-instance v14, Ljava/util/Random;

    invoke-direct {v14}, Ljava/util/Random;-><init>()V

    invoke-virtual/range {p0 .. p0}, Lcom/justas/AnimationWeather/SnowAnimation;->getWidth()I

    move-result v15

    invoke-virtual {v14, v15}, Ljava/util/Random;->nextInt(I)I

    move-result v14

    int-to-float v12, v14

    invoke-virtual/range {p0 .. p0}, Lcom/justas/AnimationWeather/SnowAnimation;->getHeight()I

    move-result v14

    int-to-float v13, v14

    new-instance v14, Ljava/util/Random;

    invoke-direct {v14}, Ljava/util/Random;-><init>()V

    const/16 v15, 0x2d

    invoke-virtual {v14, v15}, Ljava/util/Random;->nextInt(I)I

    move-result v14

    int-to-float v10, v14

    new-instance v14, Ljava/util/Random;

    invoke-direct {v14}, Ljava/util/Random;-><init>()V

    invoke-virtual {v14}, Ljava/util/Random;->nextFloat()F

    move-result v14

    const v15, 0x3f266666  # 0.65f

    invoke-static {v14, v15}, Ljava/lang/Math;->max(FF)F

    move-result v11

    move-object/from16 v0, p0

    iget-object v14, v0, Lcom/justas/AnimationWeather/SnowAnimation;->mContext:Landroid/content/Context;

    const/16 v15, 0x78

    invoke-static {v14, v15}, Lcom/justas/AnimationWeather/Weather;->convertDpToPx(Landroid/content/Context;I)I

    move-result v14

    int-to-float v9, v14

    new-instance v14, Ljava/util/Random;

    invoke-direct {v14}, Ljava/util/Random;-><init>()V

    invoke-virtual {v14}, Ljava/util/Random;->nextFloat()F

    move-result v14

    mul-float/2addr v14, v9

    const/high16 v15, 0x40000000  # 2.0f

    div-float v15, v9, v15

    sub-float v7, v14, v15

    :try_start_4a
    new-instance v6, Landroid/widget/ImageView;

    move-object/from16 v0, p0

    iget-object v14, v0, Lcom/justas/AnimationWeather/SnowAnimation;->mContext:Landroid/content/Context;

    invoke-direct {v6, v14}, Landroid/widget/ImageView;-><init>(Landroid/content/Context;)V

    move-object/from16 v0, p0

    iget-object v14, v0, Lcom/justas/AnimationWeather/SnowAnimation;->mLayoutParams:Landroid/widget/RelativeLayout$LayoutParams;

    move-object/from16 v0, p0

    invoke-virtual {v0, v6, v14}, Lcom/justas/AnimationWeather/SnowAnimation;->addView(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    move/from16 v0, p2

    invoke-virtual {v6, v0}, Landroid/widget/ImageView;->setImageResource(I)V

    invoke-virtual {v6, v12}, Landroid/widget/ImageView;->setX(F)V

    invoke-virtual {v6, v11}, Landroid/widget/ImageView;->setScaleX(F)V

    invoke-virtual {v6, v11}, Landroid/widget/ImageView;->setScaleY(F)V

    invoke-virtual {v6, v10}, Landroid/widget/ImageView;->setRotation(F)V

    invoke-static/range {p3 .. p3}, Landroid/content/res/ColorStateList;->valueOf(I)Landroid/content/res/ColorStateList;

    move-result-object v14

    invoke-virtual {v6, v14}, Landroid/widget/ImageView;->setImageTintList(Landroid/content/res/ColorStateList;)V

    const-string v14, "translationY"

    const/4 v15, 0x1

    new-array v15, v15, [F

    const/16 v16, 0x0

    aput v13, v15, v16

    invoke-static {v6, v14, v15}, Landroid/animation/ObjectAnimator;->ofFloat(Ljava/lang/Object;Ljava/lang/String;[F)Landroid/animation/ObjectAnimator;

    move-result-object v8

    const-string v14, "translationX"

    const/4 v15, 0x1

    new-array v15, v15, [F

    const/16 v16, 0x0

    add-float v17, v12, v7

    aput v17, v15, v16

    invoke-static {v6, v14, v15}, Landroid/animation/ObjectAnimator;->ofFloat(Ljava/lang/Object;Ljava/lang/String;[F)Landroid/animation/ObjectAnimator;

    move-result-object v2

    move/from16 v0, p1

    int-to-float v14, v0

    const v15, 0x3eb33333  # 0.35f

    add-float/2addr v15, v11

    div-float/2addr v14, v15

    float-to-long v14, v14

    invoke-virtual {v2, v14, v15}, Landroid/animation/ObjectAnimator;->setDuration(J)Landroid/animation/ObjectAnimator;

    new-instance v14, Landroid/view/animation/AccelerateInterpolator;

    invoke-direct {v14}, Landroid/view/animation/AccelerateInterpolator;-><init>()V

    invoke-virtual {v8, v14}, Landroid/animation/ObjectAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)V

    move/from16 v0, p1

    int-to-float v14, v0

    const v15, 0x3eb33333  # 0.35f

    add-float/2addr v15, v11

    div-float/2addr v14, v15

    float-to-long v14, v14

    invoke-virtual {v8, v14, v15}, Landroid/animation/ObjectAnimator;->setDuration(J)Landroid/animation/ObjectAnimator;

    const-string v14, "alpha"

    const/4 v15, 0x2

    new-array v15, v15, [F

    fill-array-data v15, :array_fa

    invoke-static {v6, v14, v15}, Landroid/animation/ObjectAnimator;->ofFloat(Ljava/lang/Object;Ljava/lang/String;[F)Landroid/animation/ObjectAnimator;

    move-result-object v3

    const-wide/16 v14, 0x5dc

    invoke-virtual {v3, v14, v15}, Landroid/animation/ObjectAnimator;->setDuration(J)Landroid/animation/ObjectAnimator;

    new-instance v4, Landroid/animation/AnimatorSet;

    invoke-direct {v4}, Landroid/animation/AnimatorSet;-><init>()V

    const/4 v14, 0x3

    new-array v14, v14, [Landroid/animation/Animator;

    const/4 v15, 0x0

    aput-object v8, v14, v15

    const/4 v15, 0x1

    aput-object v2, v14, v15

    const/4 v15, 0x2

    aput-object v3, v14, v15

    invoke-virtual {v4, v14}, Landroid/animation/AnimatorSet;->playTogether([Landroid/animation/Animator;)V

    new-instance v14, Lcom/justas/AnimationWeather/SnowAnimation$2;

    move-object/from16 v0, p0

    invoke-direct {v14, v0, v6}, Lcom/justas/AnimationWeather/SnowAnimation$2;-><init>(Lcom/justas/AnimationWeather/SnowAnimation;Landroid/widget/ImageView;)V

    invoke-virtual {v8, v14}, Landroid/animation/ObjectAnimator;->addListener(Landroid/animation/Animator$AnimatorListener;)V

    invoke-virtual {v4}, Landroid/animation/AnimatorSet;->start()V
    :try_end_e2
    .catch Ljava/lang/Exception; {:try_start_4a .. :try_end_e2} :catch_e3

    :goto_e2
    return-void

    :catch_e3
    move-exception v5

    invoke-virtual/range {p0 .. p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object v14

    invoke-virtual {v14}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object v15

    invoke-virtual {v5}, Ljava/lang/Exception;->getMessage()Ljava/lang/String;

    move-result-object v14

    invoke-static {v14}, Ljava/util/Objects;->requireNonNull(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v14

    check-cast v14, Ljava/lang/String;

    invoke-static {v15, v14}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_e2

    :array_fa
    .array-data 4
        0x0
        0x3f800000  # 1.0f
    .end array-data
.end method

.method public startAnimation(IIII)V
    .registers 13

    iget-object v0, p0, Lcom/justas/AnimationWeather/SnowAnimation;->mHandler:Landroid/os/Handler;

    if-nez v0, :cond_17

    new-instance v0, Landroid/os/Handler;

    invoke-direct {v0}, Landroid/os/Handler;-><init>()V

    iput-object v0, p0, Lcom/justas/AnimationWeather/SnowAnimation;->mHandler:Landroid/os/Handler;

    new-instance v0, Lcom/justas/AnimationWeather/SnowAnimation$1;

    move-object v1, p0

    move v2, p1

    move v3, p2

    move v4, p3

    move v5, p4

    invoke-direct/range {v0 .. v5}, Lcom/justas/AnimationWeather/SnowAnimation$1;-><init>(Lcom/justas/AnimationWeather/SnowAnimation;IIII)V

    iput-object v0, p0, Lcom/justas/AnimationWeather/SnowAnimation;->mRunable:Ljava/lang/Runnable;

    :cond_17
    iget-object v0, p0, Lcom/justas/AnimationWeather/SnowAnimation;->mHandler:Landroid/os/Handler;

    iget-object v1, p0, Lcom/justas/AnimationWeather/SnowAnimation;->mRunable:Ljava/lang/Runnable;

    invoke-virtual {v0, v1}, Landroid/os/Handler;->removeCallbacks(Ljava/lang/Runnable;)V

    if-eqz p4, :cond_2a

    const-wide/16 v6, 0x1c2

    :goto_22
    iget-object v0, p0, Lcom/justas/AnimationWeather/SnowAnimation;->mHandler:Landroid/os/Handler;

    iget-object v1, p0, Lcom/justas/AnimationWeather/SnowAnimation;->mRunable:Ljava/lang/Runnable;

    invoke-virtual {v0, v1, v6, v7}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z

    return-void

    :cond_2a
    const-wide/16 v6, 0x12c

    goto :goto_22
.end method

.method public stopAnimation()V
    .registers 3

    iget-object v0, p0, Lcom/justas/AnimationWeather/SnowAnimation;->mHandler:Landroid/os/Handler;

    if-eqz v0, :cond_b

    iget-object v0, p0, Lcom/justas/AnimationWeather/SnowAnimation;->mHandler:Landroid/os/Handler;

    iget-object v1, p0, Lcom/justas/AnimationWeather/SnowAnimation;->mRunable:Ljava/lang/Runnable;

    invoke-virtual {v0, v1}, Landroid/os/Handler;->removeCallbacks(Ljava/lang/Runnable;)V

    :cond_b
    invoke-virtual {p0}, Lcom/justas/AnimationWeather/SnowAnimation;->removeAllViews()V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_justas_AnimationWeather_SnowAnimation',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
