"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/clock/SecondTick$SecondTimerTask.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/clock/SecondTick$SecondTimerTask.smali'
CLASS_FALLBACK_NAMES = ['SecondTick$SecondTimerTask.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_clock_SecondTick$SecondTim',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/newstatusbar/clock/SecondTick$SecondTimerTask;\n.super Ljava/util/TimerTask;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingClass;\n    value = Lcom/android/systemui/newstatusbar/clock/SecondTick;\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = "SecondTimerTask"\n.end annotation\n\n\n# instance fields\n.field final synthetic this$0:Lcom/android/systemui/newstatusbar/clock/SecondTick;\n\n\n# direct methods\n.method constructor <init>(Lcom/android/systemui/newstatusbar/clock/SecondTick;)V\n    .registers 2\n\n    iput-object p1, p0, Lcom/android/systemui/newstatusbar/clock/SecondTick$SecondTimerTask;->this$0:Lcom/android/systemui/newstatusbar/clock/SecondTick;\n\n    invoke-direct {p0}, Ljava/util/TimerTask;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public run()V\n    .registers 2\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/SecondTick$SecondTimerTask;->this$0:Lcom/android/systemui/newstatusbar/clock/SecondTick;\n\n    invoke-static {v0}, Lcom/android/systemui/newstatusbar/clock/SecondTick;->access$000(Lcom/android/systemui/newstatusbar/clock/SecondTick;)V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
