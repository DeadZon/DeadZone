"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/justas/AnimationWeather/SunAnimation.smali'
CLASS_FALLBACK_NAMES = ['SunAnimation.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/justas/AnimationWeather/SunAnimation;
.super Landroid/widget/FrameLayout;


# annotations
.annotation build Landroid/annotation/SuppressLint;
    value = {
        "AppCompatCustomView"
    }
.end annotation


# instance fields
.field private mView:Landroid/widget/ImageView;


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 3

    invoke-direct {p0, p1, p2}, Landroid/widget/FrameLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    return-void
.end method


# virtual methods
.method public startAnimation()V
    .registers 14

    const/4 v12, -0x1

    const v2, 0x400ccccd  # 2.2f

    const/high16 v6, 0x3f000000  # 0.5f

    const/high16 v1, 0x3f800000  # 1.0f

    const/4 v5, 0x1

    invoke-virtual {p0}, Lcom/justas/AnimationWeather/SunAnimation;->getChildCount()I

    move-result v3

    if-lez v3, :cond_12

    invoke-virtual {p0}, Lcom/justas/AnimationWeather/SunAnimation;->removeAllViews()V

    :cond_12
    iget-object v3, p0, Lcom/justas/AnimationWeather/SunAnimation;->mView:Landroid/widget/ImageView;

    if-eqz v3, :cond_1b

    iget-object v3, p0, Lcom/justas/AnimationWeather/SunAnimation;->mView:Landroid/widget/ImageView;

    invoke-virtual {v3}, Landroid/widget/ImageView;->clearAnimation()V

    :cond_1b
    new-instance v3, Landroid/widget/ImageView;

    invoke-virtual {p0}, Lcom/justas/AnimationWeather/SunAnimation;->getContext()Landroid/content/Context;

    move-result-object v4

    invoke-direct {v3, v4}, Landroid/widget/ImageView;-><init>(Landroid/content/Context;)V

    iput-object v3, p0, Lcom/justas/AnimationWeather/SunAnimation;->mView:Landroid/widget/ImageView;

    new-instance v11, Landroid/widget/ImageView;

    invoke-virtual {p0}, Lcom/justas/AnimationWeather/SunAnimation;->getContext()Landroid/content/Context;

    move-result-object v3

    invoke-direct {v11, v3}, Landroid/widget/ImageView;-><init>(Landroid/content/Context;)V

    invoke-virtual {p0}, Lcom/justas/AnimationWeather/SunAnimation;->getContext()Landroid/content/Context;

    move-result-object v3

    const-string v4, "sun_2"

    invoke-static {v3, v4}, Lcom/justas/AnimationWeather/Weather;->DrawableToID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v3

    invoke-virtual {v11, v3}, Landroid/widget/ImageView;->setImageResource(I)V

    iget-object v3, p0, Lcom/justas/AnimationWeather/SunAnimation;->mView:Landroid/widget/ImageView;

    invoke-virtual {p0, v3}, Lcom/justas/AnimationWeather/SunAnimation;->addView(Landroid/view/View;)V

    invoke-virtual {p0, v11}, Lcom/justas/AnimationWeather/SunAnimation;->addView(Landroid/view/View;)V

    iget-object v3, p0, Lcom/justas/AnimationWeather/SunAnimation;->mView:Landroid/widget/ImageView;

    invoke-virtual {p0}, Lcom/justas/AnimationWeather/SunAnimation;->getContext()Landroid/content/Context;

    move-result-object v4

    const-string v7, "sun_6"

    invoke-static {v4, v7}, Lcom/justas/AnimationWeather/Weather;->DrawableToID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v4

    invoke-virtual {v3, v4}, Landroid/widget/ImageView;->setImageResource(I)V

    new-instance v0, Landroid/view/animation/ScaleAnimation;

    move v3, v1

    move v4, v2

    move v7, v5

    move v8, v6

    invoke-direct/range {v0 .. v8}, Landroid/view/animation/ScaleAnimation;-><init>(FFFFIFIF)V

    const-wide/16 v2, 0xbb8

    invoke-virtual {v0, v2, v3}, Landroid/view/animation/ScaleAnimation;->setDuration(J)V

    invoke-virtual {v0, v5}, Landroid/view/animation/ScaleAnimation;->setRepeatMode(I)V

    invoke-virtual {v0, v12}, Landroid/view/animation/ScaleAnimation;->setRepeatCount(I)V

    new-instance v9, Landroid/view/animation/AlphaAnimation;

    const/4 v2, 0x0

    invoke-direct {v9, v1, v2}, Landroid/view/animation/AlphaAnimation;-><init>(FF)V

    const-wide/16 v2, 0xbb8

    invoke-virtual {v9, v2, v3}, Landroid/view/animation/AlphaAnimation;->setDuration(J)V

    invoke-virtual {v9, v5}, Landroid/view/animation/AlphaAnimation;->setRepeatMode(I)V

    invoke-virtual {v9, v12}, Landroid/view/animation/AlphaAnimation;->setRepeatCount(I)V

    new-instance v10, Landroid/view/animation/AnimationSet;

    invoke-direct {v10, v5}, Landroid/view/animation/AnimationSet;-><init>(Z)V

    invoke-virtual {v10, v9}, Landroid/view/animation/AnimationSet;->addAnimation(Landroid/view/animation/Animation;)V

    invoke-virtual {v10, v0}, Landroid/view/animation/AnimationSet;->addAnimation(Landroid/view/animation/Animation;)V

    new-instance v1, Landroid/view/animation/DecelerateInterpolator;

    invoke-direct {v1}, Landroid/view/animation/DecelerateInterpolator;-><init>()V

    invoke-virtual {v10, v1}, Landroid/view/animation/AnimationSet;->setInterpolator(Landroid/view/animation/Interpolator;)V

    iget-object v1, p0, Lcom/justas/AnimationWeather/SunAnimation;->mView:Landroid/widget/ImageView;

    invoke-virtual {v1, v10}, Landroid/widget/ImageView;->startAnimation(Landroid/view/animation/Animation;)V

    return-void
.end method

.method public stopAnimation()V
    .registers 2

    iget-object v0, p0, Lcom/justas/AnimationWeather/SunAnimation;->mView:Landroid/widget/ImageView;

    if-eqz v0, :cond_9

    iget-object v0, p0, Lcom/justas/AnimationWeather/SunAnimation;->mView:Landroid/widget/ImageView;

    invoke-virtual {v0}, Landroid/widget/ImageView;->clearAnimation()V

    :cond_9
    invoke-virtual {p0}, Lcom/justas/AnimationWeather/SunAnimation;->removeAllViews()V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_justas_AnimationWeather_SunAnimation',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
