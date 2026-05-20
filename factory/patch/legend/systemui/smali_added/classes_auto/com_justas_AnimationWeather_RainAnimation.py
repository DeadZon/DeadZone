"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/justas/AnimationWeather/RainAnimation.smali'
CLASS_FALLBACK_NAMES = ['RainAnimation.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/justas/AnimationWeather/RainAnimation;
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

    iput-object p1, p0, Lcom/justas/AnimationWeather/RainAnimation;->mContext:Landroid/content/Context;

    new-instance v0, Landroid/widget/RelativeLayout$LayoutParams;

    invoke-direct {v0, v1, v1}, Landroid/widget/RelativeLayout$LayoutParams;-><init>(II)V

    iput-object v0, p0, Lcom/justas/AnimationWeather/RainAnimation;->mLayoutParams:Landroid/widget/RelativeLayout$LayoutParams;

    return-void
.end method

.method static synthetic access$000(Lcom/justas/AnimationWeather/RainAnimation;III)V
    .registers 4

    invoke-direct {p0, p1, p2, p3}, Lcom/justas/AnimationWeather/RainAnimation;->showAnimation(III)V

    return-void
.end method

.method private showAnimation(III)V
    .registers 20

    new-instance v12, Ljava/util/Random;

    invoke-direct {v12}, Ljava/util/Random;-><init>()V

    invoke-virtual/range {p0 .. p0}, Lcom/justas/AnimationWeather/RainAnimation;->getWidth()I

    move-result v13

    invoke-virtual {v12, v13}, Ljava/util/Random;->nextInt(I)I

    move-result v12

    int-to-float v10, v12

    invoke-virtual/range {p0 .. p0}, Lcom/justas/AnimationWeather/RainAnimation;->getHeight()I

    move-result v12

    int-to-float v11, v12

    new-instance v12, Ljava/util/Random;

    invoke-direct {v12}, Ljava/util/Random;-><init>()V

    invoke-virtual {v12}, Ljava/util/Random;->nextFloat()F

    move-result v12

    const v13, 0x3f0ccccd  # 0.55f

    invoke-static {v12, v13}, Ljava/lang/Math;->max(FF)F

    move-result v9

    new-instance v12, Ljava/util/Random;

    invoke-direct {v12}, Ljava/util/Random;-><init>()V

    invoke-virtual {v12}, Ljava/util/Random;->nextFloat()F

    move-result v12

    const v13, 0x3f0ccccd  # 0.55f

    invoke-static {v12, v13}, Ljava/lang/Math;->max(FF)F

    move-result v2

    :try_start_33
    new-instance v8, Landroid/widget/ImageView;

    move-object/from16 v0, p0

    iget-object v12, v0, Lcom/justas/AnimationWeather/RainAnimation;->mContext:Landroid/content/Context;

    invoke-direct {v8, v12}, Landroid/widget/ImageView;-><init>(Landroid/content/Context;)V

    move-object/from16 v0, p0

    iget-object v12, v0, Lcom/justas/AnimationWeather/RainAnimation;->mLayoutParams:Landroid/widget/RelativeLayout$LayoutParams;

    move-object/from16 v0, p0

    invoke-virtual {v0, v8, v12}, Lcom/justas/AnimationWeather/RainAnimation;->addView(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    move/from16 v0, p2

    invoke-virtual {v8, v0}, Landroid/widget/ImageView;->setImageResource(I)V

    invoke-virtual {v8, v10}, Landroid/widget/ImageView;->setX(F)V

    invoke-virtual {v8, v9}, Landroid/widget/ImageView;->setScaleX(F)V

    invoke-virtual {v8, v9}, Landroid/widget/ImageView;->setScaleY(F)V

    const/high16 v12, 0x41400000  # 12.0f

    invoke-virtual {v8, v12}, Landroid/widget/ImageView;->setRotation(F)V

    const-string v12, "alpha"

    const/4 v13, 0x2

    new-array v13, v13, [F

    const/4 v14, 0x0

    const/4 v15, 0x0

    aput v15, v13, v14

    const/4 v14, 0x1

    aput v2, v13, v14

    invoke-static {v8, v12, v13}, Landroid/animation/ObjectAnimator;->ofFloat(Ljava/lang/Object;Ljava/lang/String;[F)Landroid/animation/ObjectAnimator;

    move-result-object v3

    const-wide/16 v12, 0x3e8

    invoke-virtual {v3, v12, v13}, Landroid/animation/ObjectAnimator;->setDuration(J)Landroid/animation/ObjectAnimator;

    const-string v12, "translationY"

    const/4 v13, 0x1

    new-array v13, v13, [F

    const/4 v14, 0x0

    aput v11, v13, v14

    invoke-static {v8, v12, v13}, Landroid/animation/ObjectAnimator;->ofFloat(Ljava/lang/Object;Ljava/lang/String;[F)Landroid/animation/ObjectAnimator;

    move-result-object v6

    const-string v12, "translationX"

    const/4 v13, 0x1

    new-array v13, v13, [F

    const/4 v14, 0x0

    const/high16 v15, 0x43480000  # 200.0f

    sub-float v15, v10, v15

    aput v15, v13, v14

    invoke-static {v8, v12, v13}, Landroid/animation/ObjectAnimator;->ofFloat(Ljava/lang/Object;Ljava/lang/String;[F)Landroid/animation/ObjectAnimator;

    move-result-object v5

    move/from16 v0, p1

    int-to-float v12, v0

    const v13, 0x3eb33333  # 0.35f

    add-float/2addr v13, v9

    div-float/2addr v12, v13

    float-to-long v12, v12

    invoke-virtual {v5, v12, v13}, Landroid/animation/ObjectAnimator;->setDuration(J)Landroid/animation/ObjectAnimator;

    new-instance v4, Landroid/animation/AnimatorSet;

    invoke-direct {v4}, Landroid/animation/AnimatorSet;-><init>()V

    const/4 v12, 0x3

    new-array v12, v12, [Landroid/animation/Animator;

    const/4 v13, 0x0

    aput-object v6, v12, v13

    const/4 v13, 0x1

    aput-object v5, v12, v13

    const/4 v13, 0x2

    aput-object v3, v12, v13

    invoke-virtual {v4, v12}, Landroid/animation/AnimatorSet;->playTogether([Landroid/animation/Animator;)V

    new-instance v12, Landroid/view/animation/AccelerateInterpolator;

    invoke-direct {v12}, Landroid/view/animation/AccelerateInterpolator;-><init>()V

    invoke-virtual {v6, v12}, Landroid/animation/ObjectAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)V

    move/from16 v0, p1

    int-to-float v12, v0

    const v13, 0x3eb33333  # 0.35f

    add-float/2addr v13, v9

    div-float/2addr v12, v13

    float-to-long v12, v12

    invoke-virtual {v6, v12, v13}, Landroid/animation/ObjectAnimator;->setDuration(J)Landroid/animation/ObjectAnimator;

    new-instance v12, Lcom/justas/AnimationWeather/RainAnimation$2;

    move-object/from16 v0, p0

    invoke-direct {v12, v0, v8}, Lcom/justas/AnimationWeather/RainAnimation$2;-><init>(Lcom/justas/AnimationWeather/RainAnimation;Landroid/widget/ImageView;)V

    invoke-virtual {v6, v12}, Landroid/animation/ObjectAnimator;->addListener(Landroid/animation/Animator$AnimatorListener;)V

    invoke-virtual {v4}, Landroid/animation/AnimatorSet;->start()V
    :try_end_ca
    .catch Ljava/lang/Exception; {:try_start_33 .. :try_end_ca} :catch_cb

    :goto_ca
    return-void

    :catch_cb
    move-exception v7

    move-object/from16 v0, p0

    iget-object v12, v0, Lcom/justas/AnimationWeather/RainAnimation;->mContext:Landroid/content/Context;

    invoke-virtual {v12}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

    move-result-object v13

    invoke-virtual {v7}, Ljava/lang/Exception;->getMessage()Ljava/lang/String;

    move-result-object v12

    invoke-static {v12}, Ljava/util/Objects;->requireNonNull(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v12

    check-cast v12, Ljava/lang/String;

    invoke-static {v13, v12}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_ca
.end method


# virtual methods
.method public startAnimation(IIII)V
    .registers 13

    iget-object v0, p0, Lcom/justas/AnimationWeather/RainAnimation;->mHandler:Landroid/os/Handler;

    if-nez v0, :cond_17

    new-instance v0, Landroid/os/Handler;

    invoke-direct {v0}, Landroid/os/Handler;-><init>()V

    iput-object v0, p0, Lcom/justas/AnimationWeather/RainAnimation;->mHandler:Landroid/os/Handler;

    new-instance v0, Lcom/justas/AnimationWeather/RainAnimation$1;

    move-object v1, p0

    move v2, p1

    move v3, p2

    move v4, p3

    move v5, p4

    invoke-direct/range {v0 .. v5}, Lcom/justas/AnimationWeather/RainAnimation$1;-><init>(Lcom/justas/AnimationWeather/RainAnimation;IIII)V

    iput-object v0, p0, Lcom/justas/AnimationWeather/RainAnimation;->mRunable:Ljava/lang/Runnable;

    :cond_17
    iget-object v0, p0, Lcom/justas/AnimationWeather/RainAnimation;->mHandler:Landroid/os/Handler;

    iget-object v1, p0, Lcom/justas/AnimationWeather/RainAnimation;->mRunable:Ljava/lang/Runnable;

    invoke-virtual {v0, v1}, Landroid/os/Handler;->removeCallbacks(Ljava/lang/Runnable;)V

    if-eqz p4, :cond_2a

    const-wide/16 v6, 0xc8

    :goto_22
    iget-object v0, p0, Lcom/justas/AnimationWeather/RainAnimation;->mHandler:Landroid/os/Handler;

    iget-object v1, p0, Lcom/justas/AnimationWeather/RainAnimation;->mRunable:Ljava/lang/Runnable;

    invoke-virtual {v0, v1, v6, v7}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z

    return-void

    :cond_2a
    const-wide/16 v6, 0x64

    goto :goto_22
.end method

.method public stopAnimation()V
    .registers 3

    iget-object v0, p0, Lcom/justas/AnimationWeather/RainAnimation;->mHandler:Landroid/os/Handler;

    if-eqz v0, :cond_b

    iget-object v0, p0, Lcom/justas/AnimationWeather/RainAnimation;->mHandler:Landroid/os/Handler;

    iget-object v1, p0, Lcom/justas/AnimationWeather/RainAnimation;->mRunable:Ljava/lang/Runnable;

    invoke-virtual {v0, v1}, Landroid/os/Handler;->removeCallbacks(Ljava/lang/Runnable;)V

    :cond_b
    invoke-virtual {p0}, Lcom/justas/AnimationWeather/RainAnimation;->removeAllViews()V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_justas_AnimationWeather_RainAnimation',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
