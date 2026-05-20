"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/justas/AnimationWeather/Weather$1.smali
DEX group    : classes3
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/justas/AnimationWeather/Weather$1.smali'
CLASS_FALLBACK_NAMES = ['Weather$1.smali']
DEX_GROUP            = 'classes3'

PATCHES = [
    {
        'id':          'class_add_com_justas_AnimationWeather_Weather$1',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/justas/AnimationWeather/Weather$1;\n.super Landroid/database/ContentObserver;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingClass;\n    value = Lcom/justas/AnimationWeather/Weather;\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic this$0:Lcom/justas/AnimationWeather/Weather;\n\n\n# direct methods\n.method constructor <init>(Lcom/justas/AnimationWeather/Weather;Landroid/os/Handler;)V\n    .registers 3\n\n    iput-object p1, p0, Lcom/justas/AnimationWeather/Weather$1;->this$0:Lcom/justas/AnimationWeather/Weather;\n\n    invoke-direct {p0, p2}, Landroid/database/ContentObserver;-><init>(Landroid/os/Handler;)V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public onChange(Z)V\n    .registers 3\n\n    invoke-super {p0, p1}, Landroid/database/ContentObserver;->onChange(Z)V\n\n    iget-object v0, p0, Lcom/justas/AnimationWeather/Weather$1;->this$0:Lcom/justas/AnimationWeather/Weather;\n\n    invoke-static {v0}, Lcom/justas/AnimationWeather/Weather;->access$000(Lcom/justas/AnimationWeather/Weather;)V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
