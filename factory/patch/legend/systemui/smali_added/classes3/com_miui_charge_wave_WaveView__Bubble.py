"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/miui/charge/wave/WaveView$Bubble.smali
DEX group    : classes3
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/miui/charge/wave/WaveView$Bubble.smali'
CLASS_FALLBACK_NAMES = ['WaveView$Bubble.smali']
DEX_GROUP            = 'classes3'

PATCHES = [
    {
        'id':          'class_add_com_miui_charge_wave_WaveView$Bubble',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public final Lcom/miui/charge/wave/WaveView$Bubble;\n.super Ljava/lang/Object;\n\n\n# instance fields\n.field public Vx:F\n\n.field public Vy:F\n\n.field public alpha:F\n\n.field public angle:F\n\n.field public initAlpha:F\n\n.field public radius:I\n\n.field public scale:F\n\n.field public sinRandom:F\n\n.field public final synthetic this$0:Lcom/miui/charge/wave/WaveView;\n\n.field public x:I\n\n.field public y:I\n\n\n# direct methods\n.method public constructor <init>(Lcom/miui/charge/wave/WaveView;)V\n    .registers 2\n\n    iput-object p1, p0, Lcom/miui/charge/wave/WaveView$Bubble;->this$0:Lcom/miui/charge/wave/WaveView;\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
