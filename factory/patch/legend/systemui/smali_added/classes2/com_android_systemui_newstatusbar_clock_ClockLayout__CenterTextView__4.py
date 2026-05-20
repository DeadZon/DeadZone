"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$4.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$4.smali'
CLASS_FALLBACK_NAMES = ['ClockLayout$CenterTextView$4.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_clock_ClockLayout$CenterTe',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$4;\n.super Landroid/animation/AnimatorListenerAdapter;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingMethod;\n    value = Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->startAnimView()V\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic this$1:Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;\n\n\n# direct methods\n.method constructor <init>(Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;)V\n    .registers 2\n\n    iput-object p1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$4;->this$1:Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;\n\n    invoke-direct {p0}, Landroid/animation/AnimatorListenerAdapter;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public onAnimationCancel(Landroid/animation/Animator;)V\n    .registers 3\n\n    invoke-super {p0, p1}, Landroid/animation/AnimatorListenerAdapter;->onAnimationCancel(Landroid/animation/Animator;)V\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$4;->this$1:Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;\n\n    invoke-static {v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->access$200(Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;)V\n\n    return-void\n.end method\n\n.method public onAnimationEnd(Landroid/animation/Animator;)V\n    .registers 3\n\n    invoke-super {p0, p1}, Landroid/animation/AnimatorListenerAdapter;->onAnimationEnd(Landroid/animation/Animator;)V\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$4;->this$1:Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;\n\n    invoke-static {v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->access$200(Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;)V\n\n    return-void\n.end method\n\n.method public onAnimationPause(Landroid/animation/Animator;)V\n    .registers 3\n\n    invoke-super {p0, p1}, Landroid/animation/AnimatorListenerAdapter;->onAnimationPause(Landroid/animation/Animator;)V\n\n    invoke-virtual {p1}, Landroid/animation/Animator;->cancel()V\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$4;->this$1:Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;\n\n    invoke-static {v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->access$200(Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;)V\n\n    return-void\n.end method\n\n.method public onAnimationResume(Landroid/animation/Animator;)V\n    .registers 2\n\n    invoke-super {p0, p1}, Landroid/animation/AnimatorListenerAdapter;->onAnimationResume(Landroid/animation/Animator;)V\n\n    invoke-virtual {p1}, Landroid/animation/Animator;->cancel()V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
