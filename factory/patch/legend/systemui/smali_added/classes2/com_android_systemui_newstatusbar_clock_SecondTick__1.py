"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/clock/SecondTick$1.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/clock/SecondTick$1.smali'
CLASS_FALLBACK_NAMES = ['SecondTick$1.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_clock_SecondTick$1',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/newstatusbar/clock/SecondTick$1;\n.super Ljava/lang/Object;\n\n# interfaces\n.implements Ljava/lang/Runnable;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingMethod;\n    value = Lcom/android/systemui/newstatusbar/clock/SecondTick;->onTimeChanged()V\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic this$0:Lcom/android/systemui/newstatusbar/clock/SecondTick;\n\n.field final synthetic val$callBack:Lcom/android/systemui/newstatusbar/clock/SecondTick$CallBack;\n\n\n# direct methods\n.method constructor <init>(Lcom/android/systemui/newstatusbar/clock/SecondTick;Lcom/android/systemui/newstatusbar/clock/SecondTick$CallBack;)V\n    .registers 3\n\n    iput-object p1, p0, Lcom/android/systemui/newstatusbar/clock/SecondTick$1;->this$0:Lcom/android/systemui/newstatusbar/clock/SecondTick;\n\n    iput-object p2, p0, Lcom/android/systemui/newstatusbar/clock/SecondTick$1;->val$callBack:Lcom/android/systemui/newstatusbar/clock/SecondTick$CallBack;\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public run()V\n    .registers 2\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/SecondTick$1;->val$callBack:Lcom/android/systemui/newstatusbar/clock/SecondTick$CallBack;\n\n    invoke-interface {v0}, Lcom/android/systemui/newstatusbar/clock/SecondTick$CallBack;->secondTick()V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
