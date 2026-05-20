"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/justas/AnimationWeather/CloudAnimation.smali'
CLASS_FALLBACK_NAMES = ['CloudAnimation.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/justas/AnimationWeather/CloudAnimation;
.super Landroid/widget/RelativeLayout;


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 3

    invoke-direct {p0, p1, p2}, Landroid/widget/RelativeLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    return-void
.end method


# virtual methods
.method public startAnimation(I)V
    .registers 16

    const/4 v13, 0x0

    const/4 v12, -0x1

    const/4 v7, -0x2

    const/4 v11, 0x0

    const/4 v10, 0x1

    invoke-virtual {p0}, Lcom/justas/AnimationWeather/CloudAnimation;->getWidth()I

    move-result v6

    int-to-float v5, v6

    new-instance v2, Landroid/widget/ImageView;

    invoke-virtual {p0}, Lcom/justas/AnimationWeather/CloudAnimation;->getContext()Landroid/content/Context;

    move-result-object v6

    invoke-direct {v2, v6}, Landroid/widget/ImageView;-><init>(Landroid/content/Context;)V

    new-instance v3, Landroid/widget/ImageView;

    invoke-virtual {p0}, Lcom/justas/AnimationWeather/CloudAnimation;->getContext()Landroid/content/Context;

    move-result-object v6

    invoke-direct {v3, v6}, Landroid/widget/ImageView;-><init>(Landroid/content/Context;)V

    new-instance v4, Landroid/widget/RelativeLayout$LayoutParams;

    new-instance v6, Landroid/widget/RelativeLayout$LayoutParams;

    invoke-direct {v6, v7, v7}, Landroid/widget/RelativeLayout$LayoutParams;-><init>(II)V

    invoke-direct {v4, v6}, Landroid/widget/RelativeLayout$LayoutParams;-><init>(Landroid/widget/RelativeLayout$LayoutParams;)V

    const/16 v6, 0xa

    invoke-virtual {v4, v6}, Landroid/widget/RelativeLayout$LayoutParams;->addRule(I)V

    invoke-virtual {p0, v2, v4}, Lcom/justas/AnimationWeather/CloudAnimation;->addView(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    invoke-virtual {p0, v3, v4}, Lcom/justas/AnimationWeather/CloudAnimation;->addView(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    if-eq p1, v10, :cond_ab

    invoke-virtual {p0}, Lcom/justas/AnimationWeather/CloudAnimation;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    const-string v7, "cloud_24_1"

    const-string v8, "drawable"

    invoke-virtual {p0}, Lcom/justas/AnimationWeather/CloudAnimation;->getContext()Landroid/content/Context;

    move-result-object v9

    invoke-virtual {v9}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

    move-result-object v9

    invoke-virtual {v6, v7, v8, v9}, Landroid/content/res/Resources;->getIdentifier(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)I

    move-result v6

    invoke-virtual {v3, v6}, Landroid/widget/ImageView;->setImageResource(I)V

    invoke-virtual {p0}, Lcom/justas/AnimationWeather/CloudAnimation;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    const-string v7, "cloud_24_1"

    const-string v8, "drawable"

    invoke-virtual {p0}, Lcom/justas/AnimationWeather/CloudAnimation;->getContext()Landroid/content/Context;

    move-result-object v9

    invoke-virtual {v9}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

    move-result-object v9

    invoke-virtual {v6, v7, v8, v9}, Landroid/content/res/Resources;->getIdentifier(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)I

    move-result v6

    invoke-virtual {v2, v6}, Landroid/widget/ImageView;->setImageResource(I)V

    :goto_61
    const-string v6, "translationX"

    const/4 v7, 0x2

    new-array v7, v7, [F

    aput v11, v7, v13

    aput v5, v7, v10

    invoke-static {v2, v6, v7}, Landroid/animation/ObjectAnimator;->ofFloat(Ljava/lang/Object;Ljava/lang/String;[F)Landroid/animation/ObjectAnimator;

    move-result-object v0

    const-string v6, "translationX"

    const/4 v7, 0x2

    new-array v7, v7, [F

    neg-float v8, v5

    aput v8, v7, v13

    aput v11, v7, v10

    invoke-static {v3, v6, v7}, Landroid/animation/ObjectAnimator;->ofFloat(Ljava/lang/Object;Ljava/lang/String;[F)Landroid/animation/ObjectAnimator;

    move-result-object v1

    const-wide/32 v6, 0x88b8

    invoke-virtual {v0, v6, v7}, Landroid/animation/ObjectAnimator;->setDuration(J)Landroid/animation/ObjectAnimator;

    invoke-virtual {v0, v10}, Landroid/animation/ObjectAnimator;->setRepeatMode(I)V

    invoke-virtual {v0, v12}, Landroid/animation/ObjectAnimator;->setRepeatCount(I)V

    new-instance v6, Landroid/view/animation/LinearInterpolator;

    invoke-direct {v6}, Landroid/view/animation/LinearInterpolator;-><init>()V

    invoke-virtual {v0, v6}, Landroid/animation/ObjectAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)V

    new-instance v6, Landroid/view/animation/LinearInterpolator;

    invoke-direct {v6}, Landroid/view/animation/LinearInterpolator;-><init>()V

    invoke-virtual {v1, v6}, Landroid/animation/ObjectAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)V

    invoke-virtual {v0}, Landroid/animation/ObjectAnimator;->start()V

    const-wide/32 v6, 0x88b8

    invoke-virtual {v1, v6, v7}, Landroid/animation/ObjectAnimator;->setDuration(J)Landroid/animation/ObjectAnimator;

    invoke-virtual {v1, v10}, Landroid/animation/ObjectAnimator;->setRepeatMode(I)V

    invoke-virtual {v1, v12}, Landroid/animation/ObjectAnimator;->setRepeatCount(I)V

    invoke-virtual {v1}, Landroid/animation/ObjectAnimator;->start()V

    return-void

    :cond_ab
    invoke-virtual {p0}, Lcom/justas/AnimationWeather/CloudAnimation;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    const-string v7, "cloud_24_2"

    const-string v8, "drawable"

    invoke-virtual {p0}, Lcom/justas/AnimationWeather/CloudAnimation;->getContext()Landroid/content/Context;

    move-result-object v9

    invoke-virtual {v9}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

    move-result-object v9

    invoke-virtual {v6, v7, v8, v9}, Landroid/content/res/Resources;->getIdentifier(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)I

    move-result v6

    invoke-virtual {v3, v6}, Landroid/widget/ImageView;->setImageResource(I)V

    invoke-virtual {p0}, Lcom/justas/AnimationWeather/CloudAnimation;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    const-string v7, "cloud_24_2"

    const-string v8, "drawable"

    invoke-virtual {p0}, Lcom/justas/AnimationWeather/CloudAnimation;->getContext()Landroid/content/Context;

    move-result-object v9

    invoke-virtual {v9}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

    move-result-object v9

    invoke-virtual {v6, v7, v8, v9}, Landroid/content/res/Resources;->getIdentifier(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)I

    move-result v6

    invoke-virtual {v2, v6}, Landroid/widget/ImageView;->setImageResource(I)V

    goto :goto_61
.end method

.method public stopAnimation()V
    .registers 3

    const/4 v0, 0x0

    :goto_1
    invoke-virtual {p0}, Lcom/justas/AnimationWeather/CloudAnimation;->getChildCount()I

    move-result v1

    if-le v1, v0, :cond_11

    invoke-virtual {p0, v0}, Lcom/justas/AnimationWeather/CloudAnimation;->getChildAt(I)Landroid/view/View;

    move-result-object v1

    invoke-virtual {v1}, Landroid/view/View;->clearAnimation()V

    add-int/lit8 v0, v0, 0x1

    goto :goto_1

    :cond_11
    invoke-virtual {p0}, Lcom/justas/AnimationWeather/CloudAnimation;->removeAllViews()V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_justas_AnimationWeather_CloudAnimation',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
