"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/justas/AnimationWeather/MoonAnimation$2.smali
DEX group    : classes3
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/justas/AnimationWeather/MoonAnimation$2.smali'
CLASS_FALLBACK_NAMES = ['MoonAnimation$2.smali']
DEX_GROUP            = 'classes3'

PATCHES = [
    {
        'id':          'class_add_com_justas_AnimationWeather_MoonAnimation$2',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/justas/AnimationWeather/MoonAnimation$2;\n.super Ljava/lang/Object;\n\n# interfaces\n.implements Landroid/animation/Animator$AnimatorListener;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingMethod;\n    value = Lcom/justas/AnimationWeather/MoonAnimation;->generateStars()V\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic this$0:Lcom/justas/AnimationWeather/MoonAnimation;\n\n.field final synthetic val$star:Landroid/widget/ImageView;\n\n\n# direct methods\n.method constructor <init>(Lcom/justas/AnimationWeather/MoonAnimation;Landroid/widget/ImageView;)V\n    .registers 3\n\n    iput-object p1, p0, Lcom/justas/AnimationWeather/MoonAnimation$2;->this$0:Lcom/justas/AnimationWeather/MoonAnimation;\n\n    iput-object p2, p0, Lcom/justas/AnimationWeather/MoonAnimation$2;->val$star:Landroid/widget/ImageView;\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public onAnimationCancel(Landroid/animation/Animator;)V\n    .registers 2\n\n    return-void\n.end method\n\n.method public onAnimationEnd(Landroid/animation/Animator;)V\n    .registers 4\n\n    iget-object v0, p0, Lcom/justas/AnimationWeather/MoonAnimation$2;->this$0:Lcom/justas/AnimationWeather/MoonAnimation;\n\n    iget-object v1, p0, Lcom/justas/AnimationWeather/MoonAnimation$2;->val$star:Landroid/widget/ImageView;\n\n    invoke-virtual {v0, v1}, Lcom/justas/AnimationWeather/MoonAnimation;->removeView(Landroid/view/View;)V\n\n    return-void\n.end method\n\n.method public onAnimationRepeat(Landroid/animation/Animator;)V\n    .registers 2\n\n    return-void\n.end method\n\n.method public onAnimationStart(Landroid/animation/Animator;)V\n    .registers 2\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
