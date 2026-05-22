"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/justas/AnimationWeather/SnowAnimation$2.smali'
CLASS_FALLBACK_NAMES = ['SnowAnimation$2.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/justas/AnimationWeather/SnowAnimation$2;
.super Ljava/lang/Object;

# interfaces
.implements Landroid/animation/Animator$AnimatorListener;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/justas/AnimationWeather/SnowAnimation;->showAnimation(IIII)V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/justas/AnimationWeather/SnowAnimation;

.field final synthetic val$iv:Landroid/widget/ImageView;


# direct methods
.method constructor <init>(Lcom/justas/AnimationWeather/SnowAnimation;Landroid/widget/ImageView;)V
    .registers 3

    iput-object p1, p0, Lcom/justas/AnimationWeather/SnowAnimation$2;->this$0:Lcom/justas/AnimationWeather/SnowAnimation;

    iput-object p2, p0, Lcom/justas/AnimationWeather/SnowAnimation$2;->val$iv:Landroid/widget/ImageView;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public onAnimationCancel(Landroid/animation/Animator;)V
    .registers 2

    return-void
.end method

.method public onAnimationEnd(Landroid/animation/Animator;)V
    .registers 4

    iget-object v0, p0, Lcom/justas/AnimationWeather/SnowAnimation$2;->this$0:Lcom/justas/AnimationWeather/SnowAnimation;

    iget-object v1, p0, Lcom/justas/AnimationWeather/SnowAnimation$2;->val$iv:Landroid/widget/ImageView;

    invoke-virtual {v0, v1}, Lcom/justas/AnimationWeather/SnowAnimation;->removeView(Landroid/view/View;)V

    return-void
.end method

.method public onAnimationRepeat(Landroid/animation/Animator;)V
    .registers 2

    return-void
.end method

.method public onAnimationStart(Landroid/animation/Animator;)V
    .registers 2

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_justas_AnimationWeather_SnowAnimation_2',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
