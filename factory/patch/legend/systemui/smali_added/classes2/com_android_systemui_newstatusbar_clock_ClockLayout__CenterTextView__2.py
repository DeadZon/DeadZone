"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$2.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$2.smali'
CLASS_FALLBACK_NAMES = ['ClockLayout$CenterTextView$2.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_clock_ClockLayout$CenterTe',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$2;\n.super Ljava/lang/Object;\n\n# interfaces\n.implements Landroid/animation/ValueAnimator$AnimatorUpdateListener;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingMethod;\n    value = Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->startAnimView()V\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic this$1:Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;\n\n.field final synthetic val$height:F\n\n.field final synthetic val$width:F\n\n\n# direct methods\n.method constructor <init>(Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;FF)V\n    .registers 4\n\n    iput-object p1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$2;->this$1:Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;\n\n    iput p2, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$2;->val$height:F\n\n    iput p3, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$2;->val$width:F\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public onAnimationUpdate(Landroid/animation/ValueAnimator;)V\n    .registers 9\n\n    invoke-virtual {p1}, Landroid/animation/ValueAnimator;->getAnimatedValue()Ljava/lang/Object;\n\n    move-result-object v0\n\n    check-cast v0, Ljava/lang/Float;\n\n    invoke-virtual {v0}, Ljava/lang/Float;->floatValue()F\n\n    move-result v0\n\n    const/high16 v1, 0x3f000000\n\n    const/4 v2, 0x0\n\n    cmpg-float v3, v0, v2\n\n    if-gez v3, :cond_0\n\n    iget v2, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$2;->val$height:F\n\n    :cond_0\n    iget v3, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$2;->val$width:F\n\n    mul-float/2addr v3, v1\n\n    const/high16 v4, -0x3d4c0000\n\n    mul-float/2addr v4, v0\n\n    iget v5, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$2;->val$height:F\n\n    div-float/2addr v4, v5\n\n    iget-object v5, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$2;->this$1:Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;\n\n    invoke-virtual {v5, v3}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setPivotX(F)V\n\n    iget-object v5, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$2;->this$1:Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;\n\n    invoke-virtual {v5, v2}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setPivotY(F)V\n\n    invoke-static {v4}, Ljava/lang/Math;->abs(F)F\n\n    move-result v5\n\n    const/high16 v6, 0x42b40000\n\n    cmpl-float v5, v5, v6\n\n    if-lez v5, :cond_1\n\n    invoke-static {v4}, Ljava/lang/Math;->abs(F)F\n\n    move-result v5\n\n    div-float v5, v4, v5\n\n    mul-float v4, v5, v6\n\n    :cond_1\n    iget-object v5, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$2;->this$1:Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;\n\n    invoke-virtual {v5, v4}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setRotationX(F)V\n\n    iget-object v5, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$2;->this$1:Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;\n\n    invoke-static {v5}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->access$100(Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;)F\n\n    move-result v6\n\n    invoke-virtual {v5, v6}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setCameraDistance(F)V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
