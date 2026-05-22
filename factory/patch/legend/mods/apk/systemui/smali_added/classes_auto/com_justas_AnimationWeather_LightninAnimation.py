"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/justas/AnimationWeather/LightninAnimation.smali'
CLASS_FALLBACK_NAMES = ['LightninAnimation.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/justas/AnimationWeather/LightninAnimation;
.super Landroid/widget/ImageView;


# annotations
.annotation build Landroid/annotation/SuppressLint;
    value = {
        "AppCompatCustomView"
    }
.end annotation


# instance fields
.field private mHandler:Landroid/os/Handler;

.field private mRunable:Ljava/lang/Runnable;


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 5

    invoke-direct {p0, p1, p2}, Landroid/widget/ImageView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    invoke-virtual {p0}, Lcom/justas/AnimationWeather/LightninAnimation;->getContext()Landroid/content/Context;

    move-result-object v0

    const-string v1, "blue_lightnin_1"

    invoke-static {v0, v1}, Lcom/justas/AnimationWeather/Weather;->DrawableToID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v0

    invoke-virtual {p0, v0}, Lcom/justas/AnimationWeather/LightninAnimation;->setImageResource(I)V

    return-void
.end method


# virtual methods
.method public showLightnin()V
    .registers 5

    const/4 v1, 0x0

    invoke-virtual {p0, v1}, Lcom/justas/AnimationWeather/LightninAnimation;->setVisibility(I)V

    const-string v1, "alpha"

    const/4 v2, 0x5

    new-array v2, v2, [F

    fill-array-data v2, :array_22

    invoke-static {p0, v1, v2}, Landroid/animation/ObjectAnimator;->ofFloat(Ljava/lang/Object;Ljava/lang/String;[F)Landroid/animation/ObjectAnimator;

    move-result-object v0

    const-wide/16 v2, 0x7d0

    invoke-virtual {v0, v2, v3}, Landroid/animation/ObjectAnimator;->setDuration(J)Landroid/animation/ObjectAnimator;

    new-instance v1, Landroid/view/animation/DecelerateInterpolator;

    invoke-direct {v1}, Landroid/view/animation/DecelerateInterpolator;-><init>()V

    invoke-virtual {v0, v1}, Landroid/animation/ObjectAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)V

    invoke-virtual {v0}, Landroid/animation/ObjectAnimator;->start()V

    return-void

    nop

    :array_22
    .array-data 4
        0x0
        0x3ecccccd  # 0.4f
        0x3e99999a  # 0.3f
        0x3f800000  # 1.0f
        0x0
    .end array-data
.end method

.method public startLightnin()V
    .registers 5

    iget-object v0, p0, Lcom/justas/AnimationWeather/LightninAnimation;->mHandler:Landroid/os/Handler;

    if-nez v0, :cond_12

    new-instance v0, Landroid/os/Handler;

    invoke-direct {v0}, Landroid/os/Handler;-><init>()V

    iput-object v0, p0, Lcom/justas/AnimationWeather/LightninAnimation;->mHandler:Landroid/os/Handler;

    new-instance v0, Lcom/justas/AnimationWeather/LightninAnimation$1;

    invoke-direct {v0, p0}, Lcom/justas/AnimationWeather/LightninAnimation$1;-><init>(Lcom/justas/AnimationWeather/LightninAnimation;)V

    iput-object v0, p0, Lcom/justas/AnimationWeather/LightninAnimation;->mRunable:Ljava/lang/Runnable;

    :cond_12
    iget-object v0, p0, Lcom/justas/AnimationWeather/LightninAnimation;->mHandler:Landroid/os/Handler;

    iget-object v1, p0, Lcom/justas/AnimationWeather/LightninAnimation;->mRunable:Ljava/lang/Runnable;

    invoke-virtual {v0, v1}, Landroid/os/Handler;->removeCallbacks(Ljava/lang/Runnable;)V

    iget-object v0, p0, Lcom/justas/AnimationWeather/LightninAnimation;->mHandler:Landroid/os/Handler;

    iget-object v1, p0, Lcom/justas/AnimationWeather/LightninAnimation;->mRunable:Ljava/lang/Runnable;

    const-wide/16 v2, 0x1388

    invoke-virtual {v0, v1, v2, v3}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z

    return-void
.end method

.method public stopAnimation()V
    .registers 3

    iget-object v0, p0, Lcom/justas/AnimationWeather/LightninAnimation;->mHandler:Landroid/os/Handler;

    if-eqz v0, :cond_b

    iget-object v0, p0, Lcom/justas/AnimationWeather/LightninAnimation;->mHandler:Landroid/os/Handler;

    iget-object v1, p0, Lcom/justas/AnimationWeather/LightninAnimation;->mRunable:Ljava/lang/Runnable;

    invoke-virtual {v0, v1}, Landroid/os/Handler;->removeCallbacks(Ljava/lang/Runnable;)V

    :cond_b
    const/16 v0, 0x8

    invoke-virtual {p0, v0}, Lcom/justas/AnimationWeather/LightninAnimation;->setVisibility(I)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_justas_AnimationWeather_LightninAnimation',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
