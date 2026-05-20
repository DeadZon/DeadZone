"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/justas/AnimationWeather/LightninAnimation.smali
DEX group    : classes3
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/justas/AnimationWeather/LightninAnimation.smali'
CLASS_FALLBACK_NAMES = ['LightninAnimation.smali']
DEX_GROUP            = 'classes3'

PATCHES = [
    {
        'id':          'class_add_com_justas_AnimationWeather_LightninAnimation',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public Lcom/justas/AnimationWeather/LightninAnimation;\n.super Landroid/widget/ImageView;\n\n\n# annotations\n.annotation build Landroid/annotation/SuppressLint;\n    value = {\n        "AppCompatCustomView"\n    }\n.end annotation\n\n\n# instance fields\n.field private mHandler:Landroid/os/Handler;\n\n.field private mRunable:Ljava/lang/Runnable;\n\n\n# direct methods\n.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n    .registers 5\n\n    invoke-direct {p0, p1, p2}, Landroid/widget/ImageView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n\n    invoke-virtual {p0}, Lcom/justas/AnimationWeather/LightninAnimation;->getContext()Landroid/content/Context;\n\n    move-result-object v0\n\n    const-string v1, "blue_lightnin_1"\n\n    invoke-static {v0, v1}, Lcom/justas/AnimationWeather/Weather;->DrawableToID(Landroid/content/Context;Ljava/lang/String;)I\n\n    move-result v0\n\n    invoke-virtual {p0, v0}, Lcom/justas/AnimationWeather/LightninAnimation;->setImageResource(I)V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public showLightnin()V\n    .registers 5\n\n    const/4 v1, 0x0\n\n    invoke-virtual {p0, v1}, Lcom/justas/AnimationWeather/LightninAnimation;->setVisibility(I)V\n\n    const-string v1, "alpha"\n\n    const/4 v2, 0x5\n\n    new-array v2, v2, [F\n\n    fill-array-data v2, :array_0\n\n    invoke-static {p0, v1, v2}, Landroid/animation/ObjectAnimator;->ofFloat(Ljava/lang/Object;Ljava/lang/String;[F)Landroid/animation/ObjectAnimator;\n\n    move-result-object v0\n\n    const-wide/16 v2, 0x7d0\n\n    invoke-virtual {v0, v2, v3}, Landroid/animation/ObjectAnimator;->setDuration(J)Landroid/animation/ObjectAnimator;\n\n    new-instance v1, Landroid/view/animation/DecelerateInterpolator;\n\n    invoke-direct {v1}, Landroid/view/animation/DecelerateInterpolator;-><init>()V\n\n    invoke-virtual {v0, v1}, Landroid/animation/ObjectAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)V\n\n    invoke-virtual {v0}, Landroid/animation/ObjectAnimator;->start()V\n\n    return-void\n\n    nop\n\n    :array_0\n    .array-data 4\n        0x0\n        0x3ecccccd\n        0x3e99999a\n        0x3f800000\n        0x0\n    .end array-data\n.end method\n\n.method public startLightnin()V\n    .registers 5\n\n    iget-object v0, p0, Lcom/justas/AnimationWeather/LightninAnimation;->mHandler:Landroid/os/Handler;\n\n    if-nez v0, :cond_0\n\n    new-instance v0, Landroid/os/Handler;\n\n    invoke-direct {v0}, Landroid/os/Handler;-><init>()V\n\n    iput-object v0, p0, Lcom/justas/AnimationWeather/LightninAnimation;->mHandler:Landroid/os/Handler;\n\n    new-instance v0, Lcom/justas/AnimationWeather/LightninAnimation$1;\n\n    invoke-direct {v0, p0}, Lcom/justas/AnimationWeather/LightninAnimation$1;-><init>(Lcom/justas/AnimationWeather/LightninAnimation;)V\n\n    iput-object v0, p0, Lcom/justas/AnimationWeather/LightninAnimation;->mRunable:Ljava/lang/Runnable;\n\n    :cond_0\n    iget-object v0, p0, Lcom/justas/AnimationWeather/LightninAnimation;->mHandler:Landroid/os/Handler;\n\n    iget-object v1, p0, Lcom/justas/AnimationWeather/LightninAnimation;->mRunable:Ljava/lang/Runnable;\n\n    invoke-virtual {v0, v1}, Landroid/os/Handler;->removeCallbacks(Ljava/lang/Runnable;)V\n\n    iget-object v0, p0, Lcom/justas/AnimationWeather/LightninAnimation;->mHandler:Landroid/os/Handler;\n\n    iget-object v1, p0, Lcom/justas/AnimationWeather/LightninAnimation;->mRunable:Ljava/lang/Runnable;\n\n    const-wide/16 v2, 0x1388\n\n    invoke-virtual {v0, v1, v2, v3}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z\n\n    return-void\n.end method\n\n.method public stopAnimation()V\n    .registers 3\n\n    iget-object v0, p0, Lcom/justas/AnimationWeather/LightninAnimation;->mHandler:Landroid/os/Handler;\n\n    if-eqz v0, :cond_0\n\n    iget-object v0, p0, Lcom/justas/AnimationWeather/LightninAnimation;->mHandler:Landroid/os/Handler;\n\n    iget-object v1, p0, Lcom/justas/AnimationWeather/LightninAnimation;->mRunable:Ljava/lang/Runnable;\n\n    invoke-virtual {v0, v1}, Landroid/os/Handler;->removeCallbacks(Ljava/lang/Runnable;)V\n\n    :cond_0\n    const/16 v0, 0x8\n\n    invoke-virtual {p0, v0}, Lcom/justas/AnimationWeather/LightninAnimation;->setVisibility(I)V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
