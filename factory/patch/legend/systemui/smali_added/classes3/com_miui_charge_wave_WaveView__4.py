"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/miui/charge/wave/WaveView$4.smali
DEX group    : classes3
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/miui/charge/wave/WaveView$4.smali'
CLASS_FALLBACK_NAMES = ['WaveView$4.smali']
DEX_GROUP            = 'classes3'

PATCHES = [
    {
        'id':          'class_add_com_miui_charge_wave_WaveView$4',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public final Lcom/miui/charge/wave/WaveView$4;\n.super Ljava/lang/Object;\n\n# interfaces\n.implements Landroid/animation/ValueAnimator$AnimatorUpdateListener;\n\n\n# instance fields\n.field public final synthetic this$0:Lcom/miui/charge/wave/WaveView;\n\n\n# direct methods\n.method public constructor <init>(Lcom/miui/charge/wave/WaveView;)V\n    .registers 2\n\n    iput-object p1, p0, Lcom/miui/charge/wave/WaveView$4;->this$0:Lcom/miui/charge/wave/WaveView;\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public final onAnimationUpdate(Landroid/animation/ValueAnimator;)V\n    .registers 2\n\n    iget-object p0, p0, Lcom/miui/charge/wave/WaveView$4;->this$0:Lcom/miui/charge/wave/WaveView;\n\n    invoke-virtual {p1}, Landroid/animation/ValueAnimator;->getAnimatedValue()Ljava/lang/Object;\n\n    move-result-object p1\n\n    check-cast p1, Ljava/lang/Integer;\n\n    invoke-virtual {p1}, Ljava/lang/Integer;->intValue()I\n\n    move-result p1\n\n    iput p1, p0, Lcom/miui/charge/wave/WaveView;->mWave2Dx:I\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
