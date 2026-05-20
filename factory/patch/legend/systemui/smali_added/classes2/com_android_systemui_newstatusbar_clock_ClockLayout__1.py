"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/clock/ClockLayout$1.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/clock/ClockLayout$1.smali'
CLASS_FALLBACK_NAMES = ['ClockLayout$1.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_clock_ClockLayout$1',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/newstatusbar/clock/ClockLayout$1;\n.super Ljava/lang/Object;\n\n# interfaces\n.implements Landroid/view/animation/Animation$AnimationListener;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingMethod;\n    value = Lcom/android/systemui/newstatusbar/clock/ClockLayout;->startAnimDots(Z)V\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic this$0:Lcom/android/systemui/newstatusbar/clock/ClockLayout;\n\n\n# direct methods\n.method constructor <init>(Lcom/android/systemui/newstatusbar/clock/ClockLayout;)V\n    .registers 2\n\n    iput-object p1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$1;->this$0:Lcom/android/systemui/newstatusbar/clock/ClockLayout;\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public onAnimationEnd(Landroid/view/animation/Animation;)V\n    .registers 4\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$1;->this$0:Lcom/android/systemui/newstatusbar/clock/ClockLayout;\n\n    iget-object v0, v0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clockSettings:Lcom/android/systemui/newstatusbar/clock/ClockSettings;\n\n    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->getClockData()Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;\n\n    move-result-object v0\n\n    iget-boolean v0, v0, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->isSecondEnable:Z\n\n    if-nez v0, :cond_0\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$1;->this$0:Lcom/android/systemui/newstatusbar/clock/ClockLayout;\n\n    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->isShown()Z\n\n    move-result v0\n\n    if-eqz v0, :cond_0\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$1;->this$0:Lcom/android/systemui/newstatusbar/clock/ClockLayout;\n\n    invoke-static {v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->access$000(Lcom/android/systemui/newstatusbar/clock/ClockLayout;)Lcom/android/systemui/newstatusbar/clock/ClockView;\n\n    move-result-object v1\n\n    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/clock/ClockView;->getText()Ljava/lang/String;\n\n    move-result-object v1\n\n    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->onTextChanged(Ljava/lang/CharSequence;)V\n\n    :cond_0\n    return-void\n.end method\n\n.method public onAnimationRepeat(Landroid/view/animation/Animation;)V\n    .registers 2\n\n    return-void\n.end method\n\n.method public onAnimationStart(Landroid/view/animation/Animation;)V\n    .registers 2\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
