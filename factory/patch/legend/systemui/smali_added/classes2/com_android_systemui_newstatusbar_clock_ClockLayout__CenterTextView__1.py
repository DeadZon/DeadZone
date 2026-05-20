"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$1.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$1.smali'
CLASS_FALLBACK_NAMES = ['ClockLayout$CenterTextView$1.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_clock_ClockLayout$CenterTe',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$1;\n.super Ljava/lang/Object;\n\n# interfaces\n.implements Ljava/lang/Runnable;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingMethod;\n    value = Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setText(Ljava/lang/String;Z)V\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic this$1:Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;\n\n.field final synthetic val$animate:Z\n\n.field final synthetic val$text:Ljava/lang/String;\n\n\n# direct methods\n.method constructor <init>(Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;Ljava/lang/String;Z)V\n    .registers 4\n\n    iput-object p1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$1;->this$1:Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;\n\n    iput-object p2, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$1;->val$text:Ljava/lang/String;\n\n    iput-boolean p3, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$1;->val$animate:Z\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public run()V\n    .registers 4\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$1;->this$1:Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;\n\n    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$1;->val$text:Ljava/lang/String;\n\n    iget-boolean v2, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$1;->val$animate:Z\n\n    invoke-virtual {v0, v1, v2}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setText(Ljava/lang/String;Z)V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
