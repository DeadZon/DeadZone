"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/justas/AnimationWeather/DrippingDrops$2.smali
DEX group    : classes3
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/justas/AnimationWeather/DrippingDrops$2.smali'
CLASS_FALLBACK_NAMES = ['DrippingDrops$2.smali']
DEX_GROUP            = 'classes3'

PATCHES = [
    {
        'id':          'class_add_com_justas_AnimationWeather_DrippingDrops$2',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/justas/AnimationWeather/DrippingDrops$2;\n.super Ljava/lang/Object;\n\n# interfaces\n.implements Landroid/animation/Animator$AnimatorListener;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingMethod;\n    value = Lcom/justas/AnimationWeather/DrippingDrops;->showAnimation()V\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic this$0:Lcom/justas/AnimationWeather/DrippingDrops;\n\n.field final synthetic val$iv:Landroid/widget/ImageView;\n\n\n# direct methods\n.method constructor <init>(Lcom/justas/AnimationWeather/DrippingDrops;Landroid/widget/ImageView;)V\n    .registers 3\n\n    iput-object p1, p0, Lcom/justas/AnimationWeather/DrippingDrops$2;->this$0:Lcom/justas/AnimationWeather/DrippingDrops;\n\n    iput-object p2, p0, Lcom/justas/AnimationWeather/DrippingDrops$2;->val$iv:Landroid/widget/ImageView;\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public onAnimationCancel(Landroid/animation/Animator;)V\n    .registers 2\n\n    return-void\n.end method\n\n.method public onAnimationEnd(Landroid/animation/Animator;)V\n    .registers 4\n\n    iget-object v0, p0, Lcom/justas/AnimationWeather/DrippingDrops$2;->this$0:Lcom/justas/AnimationWeather/DrippingDrops;\n\n    iget-object v1, p0, Lcom/justas/AnimationWeather/DrippingDrops$2;->val$iv:Landroid/widget/ImageView;\n\n    invoke-virtual {v0, v1}, Lcom/justas/AnimationWeather/DrippingDrops;->removeView(Landroid/view/View;)V\n\n    return-void\n.end method\n\n.method public onAnimationRepeat(Landroid/animation/Animator;)V\n    .registers 2\n\n    return-void\n.end method\n\n.method public onAnimationStart(Landroid/animation/Animator;)V\n    .registers 2\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
