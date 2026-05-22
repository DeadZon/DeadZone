"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/justas/AnimationWeather/MoonAnimation.smali'
CLASS_FALLBACK_NAMES = ['MoonAnimation.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/justas/AnimationWeather/MoonAnimation;
.super Landroid/widget/RelativeLayout;


# instance fields
.field private mHandler:Landroid/os/Handler;

.field private mRunable:Ljava/lang/Runnable;


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 3

    invoke-direct {p0, p1, p2}, Landroid/widget/RelativeLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    return-void
.end method

.method static synthetic access$000(Lcom/justas/AnimationWeather/MoonAnimation;)V
    .registers 1

    invoke-direct {p0}, Lcom/justas/AnimationWeather/MoonAnimation;->generateStars()V

    return-void
.end method

.method private generateStars()V
    .registers 9

    iget-object v3, p0, Lcom/justas/AnimationWeather/MoonAnimation;->mHandler:Landroid/os/Handler;

    if-nez v3, :cond_12

    new-instance v3, Landroid/os/Handler;

    invoke-direct {v3}, Landroid/os/Handler;-><init>()V

    iput-object v3, p0, Lcom/justas/AnimationWeather/MoonAnimation;->mHandler:Landroid/os/Handler;

    new-instance v3, Lcom/justas/AnimationWeather/MoonAnimation$1;

    invoke-direct {v3, p0}, Lcom/justas/AnimationWeather/MoonAnimation$1;-><init>(Lcom/justas/AnimationWeather/MoonAnimation;)V

    iput-object v3, p0, Lcom/justas/AnimationWeather/MoonAnimation;->mRunable:Ljava/lang/Runnable;

    :cond_12
    iget-object v3, p0, Lcom/justas/AnimationWeather/MoonAnimation;->mHandler:Landroid/os/Handler;

    iget-object v4, p0, Lcom/justas/AnimationWeather/MoonAnimation;->mRunable:Ljava/lang/Runnable;

    invoke-virtual {v3, v4}, Landroid/os/Handler;->removeCallbacks(Ljava/lang/Runnable;)V

    iget-object v3, p0, Lcom/justas/AnimationWeather/MoonAnimation;->mHandler:Landroid/os/Handler;

    iget-object v4, p0, Lcom/justas/AnimationWeather/MoonAnimation;->mRunable:Ljava/lang/Runnable;

    const-wide/16 v6, 0x3e8

    invoke-virtual {v3, v4, v6, v7}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z

    new-instance v2, Landroid/widget/ImageView;

    invoke-virtual {p0}, Lcom/justas/AnimationWeather/MoonAnimation;->getContext()Landroid/content/Context;

    move-result-object v3

    invoke-direct {v2, v3}, Landroid/widget/ImageView;-><init>(Landroid/content/Context;)V

    invoke-virtual {p0}, Lcom/justas/AnimationWeather/MoonAnimation;->getContext()Landroid/content/Context;

    move-result-object v3

    const-string v4, "blue_star_25"

    invoke-static {v3, v4}, Lcom/justas/AnimationWeather/Weather;->DrawableToID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v3

    invoke-virtual {v2, v3}, Landroid/widget/ImageView;->setImageResource(I)V

    invoke-virtual {p0, v2}, Lcom/justas/AnimationWeather/MoonAnimation;->addView(Landroid/view/View;)V

    invoke-virtual {v2}, Landroid/widget/ImageView;->getDrawable()Landroid/graphics/drawable/Drawable;

    move-result-object v3

    invoke-virtual {v3}, Landroid/graphics/drawable/Drawable;->getIntrinsicHeight()I

    move-result v1

    invoke-virtual {p0}, Lcom/justas/AnimationWeather/MoonAnimation;->getWidth()I

    move-result v3

    if-lez v3, :cond_75

    new-instance v3, Ljava/util/Random;

    invoke-direct {v3}, Ljava/util/Random;-><init>()V

    invoke-virtual {p0}, Lcom/justas/AnimationWeather/MoonAnimation;->getWidth()I

    move-result v4

    invoke-virtual {v3, v4}, Ljava/util/Random;->nextInt(I)I

    move-result v3

    sub-int/2addr v3, v1

    invoke-static {v1, v3}, Ljava/lang/Math;->max(II)I

    move-result v3

    int-to-float v3, v3

    invoke-virtual {v2, v3}, Landroid/widget/ImageView;->setX(F)V

    new-instance v3, Ljava/util/Random;

    invoke-direct {v3}, Ljava/util/Random;-><init>()V

    invoke-virtual {p0}, Lcom/justas/AnimationWeather/MoonAnimation;->getWidth()I

    move-result v4

    invoke-virtual {v3, v4}, Ljava/util/Random;->nextInt(I)I

    move-result v3

    sub-int/2addr v3, v1

    invoke-static {v1, v3}, Ljava/lang/Math;->max(II)I

    move-result v3

    int-to-float v3, v3

    invoke-virtual {v2, v3}, Landroid/widget/ImageView;->setY(F)V

    :cond_75
    const-string v3, "alpha"

    const/4 v4, 0x3

    new-array v4, v4, [F

    fill-array-data v4, :array_92

    invoke-static {v2, v3, v4}, Landroid/animation/ObjectAnimator;->ofFloat(Ljava/lang/Object;Ljava/lang/String;[F)Landroid/animation/ObjectAnimator;

    move-result-object v0

    const-wide/16 v4, 0xbb8

    invoke-virtual {v0, v4, v5}, Landroid/animation/ObjectAnimator;->setDuration(J)Landroid/animation/ObjectAnimator;

    new-instance v3, Lcom/justas/AnimationWeather/MoonAnimation$2;

    invoke-direct {v3, p0, v2}, Lcom/justas/AnimationWeather/MoonAnimation$2;-><init>(Lcom/justas/AnimationWeather/MoonAnimation;Landroid/widget/ImageView;)V

    invoke-virtual {v0, v3}, Landroid/animation/ObjectAnimator;->addListener(Landroid/animation/Animator$AnimatorListener;)V

    invoke-virtual {v0}, Landroid/animation/ObjectAnimator;->start()V

    return-void

    :array_92
    .array-data 4
        0x0
        0x3f800000  # 1.0f
        0x0
    .end array-data
.end method


# virtual methods
.method public startAnimation()V
    .registers 4

    new-instance v0, Landroid/widget/ImageView;

    invoke-virtual {p0}, Lcom/justas/AnimationWeather/MoonAnimation;->getContext()Landroid/content/Context;

    move-result-object v1

    invoke-direct {v0, v1}, Landroid/widget/ImageView;-><init>(Landroid/content/Context;)V

    invoke-virtual {p0}, Lcom/justas/AnimationWeather/MoonAnimation;->getContext()Landroid/content/Context;

    move-result-object v1

    const-string v2, "moon_1_1"

    invoke-static {v1, v2}, Lcom/justas/AnimationWeather/Weather;->DrawableToID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v1

    invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setImageResource(I)V

    invoke-virtual {p0, v0}, Lcom/justas/AnimationWeather/MoonAnimation;->addView(Landroid/view/View;)V

    invoke-direct {p0}, Lcom/justas/AnimationWeather/MoonAnimation;->generateStars()V

    return-void
.end method

.method public stopAnimation()V
    .registers 3

    iget-object v0, p0, Lcom/justas/AnimationWeather/MoonAnimation;->mHandler:Landroid/os/Handler;

    if-eqz v0, :cond_b

    iget-object v0, p0, Lcom/justas/AnimationWeather/MoonAnimation;->mHandler:Landroid/os/Handler;

    iget-object v1, p0, Lcom/justas/AnimationWeather/MoonAnimation;->mRunable:Ljava/lang/Runnable;

    invoke-virtual {v0, v1}, Landroid/os/Handler;->removeCallbacks(Ljava/lang/Runnable;)V

    :cond_b
    invoke-virtual {p0}, Lcom/justas/AnimationWeather/MoonAnimation;->removeAllViews()V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_justas_AnimationWeather_MoonAnimation',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
