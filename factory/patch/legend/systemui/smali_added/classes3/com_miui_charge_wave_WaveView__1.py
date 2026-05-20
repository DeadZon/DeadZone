"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/miui/charge/wave/WaveView$1.smali
DEX group    : classes3
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/miui/charge/wave/WaveView$1.smali'
CLASS_FALLBACK_NAMES = ['WaveView$1.smali']
DEX_GROUP            = 'classes3'

PATCHES = [
    {
        'id':          'class_add_com_miui_charge_wave_WaveView$1',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public final Lcom/miui/charge/wave/WaveView$1;\n.super Landroid/os/Handler;\n\n\n# instance fields\n.field public final synthetic this$0:Lcom/miui/charge/wave/WaveView;\n\n\n# direct methods\n.method public constructor <init>(Lcom/miui/charge/wave/WaveView;)V\n    .registers 2\n\n    iput-object p1, p0, Lcom/miui/charge/wave/WaveView$1;->this$0:Lcom/miui/charge/wave/WaveView;\n\n    invoke-direct {p0}, Landroid/os/Handler;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public final handleMessage(Landroid/os/Message;)V\n    .registers 3\n\n    invoke-super {p0, p1}, Landroid/os/Handler;->handleMessage(Landroid/os/Message;)V\n\n    iget p1, p1, Landroid/os/Message;->what:I\n\n    const/16 v0, 0x2711\n\n    if-ne p1, v0, :cond_0\n\n    iget-object p0, p0, Lcom/miui/charge/wave/WaveView$1;->this$0:Lcom/miui/charge/wave/WaveView;\n\n    invoke-virtual {p0}, Lcom/miui/charge/wave/WaveView;->tryCreateBubble()V\n\n    :cond_0\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
