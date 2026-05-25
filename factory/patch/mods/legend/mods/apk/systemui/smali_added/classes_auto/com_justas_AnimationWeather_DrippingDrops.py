"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/justas/AnimationWeather/DrippingDrops.smali'
CLASS_FALLBACK_NAMES = ['DrippingDrops.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/justas/AnimationWeather/DrippingDrops;
.super Lcom/justas/AnimationWeather/RainAnimation;


# instance fields
.field private mHandler:Landroid/os/Handler;

.field private mRunable:Ljava/lang/Runnable;


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 3

    invoke-direct {p0, p1, p2}, Lcom/justas/AnimationWeather/RainAnimation;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    return-void
.end method

.method static synthetic access$000(Lcom/justas/AnimationWeather/DrippingDrops;)V
    .registers 1

    invoke-direct {p0}, Lcom/justas/AnimationWeather/DrippingDrops;->showAnimation()V

    return-void
.end method

.method private showAnimation()V
    .registers 12

    const/high16 v10, 0x40000000  # 2.0f

    new-instance v8, Ljava/util/Random;

    invoke-direct {v8}, Ljava/util/Random;-><init>()V

    invoke-virtual {p0}, Lcom/justas/AnimationWeather/DrippingDrops;->getWidth()I

    move-result v9

    invoke-virtual {v8, v9}, Ljava/util/Random;->nextInt(I)I

    move-result v8

    int-to-float v5, v8

    new-instance v8, Ljava/util/Random;

    invoke-direct {v8}, Ljava/util/Random;-><init>()V

    invoke-virtual {p0}, Lcom/justas/AnimationWeather/DrippingDrops;->getHeight()I

    move-result v9

    div-int/lit8 v9, v9, 0x3

    invoke-virtual {v8, v9}, Ljava/util/Random;->nextInt(I)I

    move-result v8

    int-to-float v6, v8

    invoke-virtual {p0}, Lcom/justas/AnimationWeather/DrippingDrops;->getHeight()I

    move-result v8

    int-to-float v8, v8

    div-float/2addr v8, v10

    add-float v7, v6, v8

    :try_start_28
    new-instance v4, Landroid/widget/ImageView;

    invoke-virtual {p0}, Lcom/justas/AnimationWeather/DrippingDrops;->getContext()Landroid/content/Context;

    move-result-object v8

    invoke-direct {v4, v8}, Landroid/widget/ImageView;-><init>(Landroid/content/Context;)V

    const/16 v8, 0xc8

    const/16 v9, 0xc8

    invoke-virtual {p0, v4, v8, v9}, Lcom/justas/AnimationWeather/DrippingDrops;->addView(Landroid/view/View;II)V

    invoke-virtual {p0}, Lcom/justas/AnimationWeather/DrippingDrops;->getContext()Landroid/content/Context;

    move-result-object v8

    const-string v9, "weather_rainy_m_rain03"

    invoke-static {v8, v9}, Landroid/Utils/Utils;->DrawableToID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v8

    invoke-virtual {v4, v8}, Landroid/widget/ImageView;->setImageResource(I)V

    invoke-virtual {v4, v5}, Landroid/widget/ImageView;->setX(F)V

    invoke-virtual {v4, v6}, Landroid/widget/ImageView;->setY(F)V

    const-string v8, "alpha"

    const/4 v9, 0x3

    new-array v9, v9, [F

    fill-array-data v9, :array_ac

    invoke-static {v4, v8, v9}, Landroid/animation/ObjectAnimator;->ofFloat(Ljava/lang/Object;Ljava/lang/String;[F)Landroid/animation/ObjectAnimator;

    move-result-object v0

    const-wide/16 v8, 0x2328

    invoke-virtual {v0, v8, v9}, Landroid/animation/ObjectAnimator;->setDuration(J)Landroid/animation/ObjectAnimator;

    const-string v8, "translationY"

    const/4 v9, 0x1

    new-array v9, v9, [F

    const/4 v10, 0x0

    aput v7, v9, v10

    invoke-static {v4, v8, v9}, Landroid/animation/ObjectAnimator;->ofFloat(Ljava/lang/Object;Ljava/lang/String;[F)Landroid/animation/ObjectAnimator;

    move-result-object v2

    new-instance v1, Landroid/animation/AnimatorSet;

    invoke-direct {v1}, Landroid/animation/AnimatorSet;-><init>()V

    const/4 v8, 0x2

    new-array v8, v8, [Landroid/animation/Animator;

    const/4 v9, 0x0

    aput-object v2, v8, v9

    const/4 v9, 0x1

    aput-object v0, v8, v9

    invoke-virtual {v1, v8}, Landroid/animation/AnimatorSet;->playTogether([Landroid/animation/Animator;)V

    new-instance v8, Landroid/view/animation/DecelerateInterpolator;

    const/high16 v9, 0x40000000  # 2.0f

    invoke-direct {v8, v9}, Landroid/view/animation/DecelerateInterpolator;-><init>(F)V

    invoke-virtual {v2, v8}, Landroid/animation/ObjectAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)V

    const-wide/16 v8, 0x2328

    invoke-virtual {v2, v8, v9}, Landroid/animation/ObjectAnimator;->setDuration(J)Landroid/animation/ObjectAnimator;

    new-instance v8, Lcom/justas/AnimationWeather/DrippingDrops$2;

    invoke-direct {v8, p0, v4}, Lcom/justas/AnimationWeather/DrippingDrops$2;-><init>(Lcom/justas/AnimationWeather/DrippingDrops;Landroid/widget/ImageView;)V

    invoke-virtual {v2, v8}, Landroid/animation/ObjectAnimator;->addListener(Landroid/animation/Animator$AnimatorListener;)V

    invoke-virtual {v1}, Landroid/animation/AnimatorSet;->start()V
    :try_end_93
    .catch Ljava/lang/Exception; {:try_start_28 .. :try_end_93} :catch_94

    :goto_93
    return-void

    :catch_94
    move-exception v3

    invoke-virtual {p0}, Lcom/justas/AnimationWeather/DrippingDrops;->getContext()Landroid/content/Context;

    move-result-object v8

    invoke-virtual {v8}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

    move-result-object v9

    invoke-virtual {v3}, Ljava/lang/Exception;->getMessage()Ljava/lang/String;

    move-result-object v8

    invoke-static {v8}, Ljava/util/Objects;->requireNonNull(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v8

    check-cast v8, Ljava/lang/String;

    invoke-static {v9, v8}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_93

    nop

    :array_ac
    .array-data 4
        0x0
        0x41200000  # 10.0f
        0x0
    .end array-data
.end method


# virtual methods
.method public startDropAnimation()V
    .registers 5

    invoke-virtual {p0}, Lcom/justas/AnimationWeather/DrippingDrops;->getBackground()Landroid/graphics/drawable/Drawable;

    move-result-object v0

    if-nez v0, :cond_1b

    invoke-virtual {p0}, Lcom/justas/AnimationWeather/DrippingDrops;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-virtual {p0}, Lcom/justas/AnimationWeather/DrippingDrops;->getContext()Landroid/content/Context;

    move-result-object v1

    const-string v2, "klipartz"

    invoke-static {v1, v2}, Landroid/Utils/Utils;->DrawableToID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v1

    invoke-virtual {v0, v1}, Landroid/content/Context;->getDrawable(I)Landroid/graphics/drawable/Drawable;

    move-result-object v0

    invoke-virtual {p0, v0}, Lcom/justas/AnimationWeather/DrippingDrops;->setBackground(Landroid/graphics/drawable/Drawable;)V

    :cond_1b
    iget-object v0, p0, Lcom/justas/AnimationWeather/DrippingDrops;->mHandler:Landroid/os/Handler;

    if-nez v0, :cond_2d

    new-instance v0, Landroid/os/Handler;

    invoke-direct {v0}, Landroid/os/Handler;-><init>()V

    iput-object v0, p0, Lcom/justas/AnimationWeather/DrippingDrops;->mHandler:Landroid/os/Handler;

    new-instance v0, Lcom/justas/AnimationWeather/DrippingDrops$1;

    invoke-direct {v0, p0}, Lcom/justas/AnimationWeather/DrippingDrops$1;-><init>(Lcom/justas/AnimationWeather/DrippingDrops;)V

    iput-object v0, p0, Lcom/justas/AnimationWeather/DrippingDrops;->mRunable:Ljava/lang/Runnable;

    :cond_2d
    iget-object v0, p0, Lcom/justas/AnimationWeather/DrippingDrops;->mHandler:Landroid/os/Handler;

    iget-object v1, p0, Lcom/justas/AnimationWeather/DrippingDrops;->mRunable:Ljava/lang/Runnable;

    invoke-virtual {v0, v1}, Landroid/os/Handler;->removeCallbacks(Ljava/lang/Runnable;)V

    iget-object v0, p0, Lcom/justas/AnimationWeather/DrippingDrops;->mHandler:Landroid/os/Handler;

    iget-object v1, p0, Lcom/justas/AnimationWeather/DrippingDrops;->mRunable:Ljava/lang/Runnable;

    const-wide/16 v2, 0xbb8

    invoke-virtual {v0, v1, v2, v3}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z

    return-void
.end method

.method public stopAnimation()V
    .registers 3

    iget-object v0, p0, Lcom/justas/AnimationWeather/DrippingDrops;->mHandler:Landroid/os/Handler;

    if-eqz v0, :cond_b

    iget-object v0, p0, Lcom/justas/AnimationWeather/DrippingDrops;->mHandler:Landroid/os/Handler;

    iget-object v1, p0, Lcom/justas/AnimationWeather/DrippingDrops;->mRunable:Ljava/lang/Runnable;

    invoke-virtual {v0, v1}, Landroid/os/Handler;->removeCallbacks(Ljava/lang/Runnable;)V

    :cond_b
    invoke-virtual {p0}, Lcom/justas/AnimationWeather/DrippingDrops;->removeAllViews()V

    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Lcom/justas/AnimationWeather/DrippingDrops;->setBackground(Landroid/graphics/drawable/Drawable;)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_justas_AnimationWeather_DrippingDrops',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
