"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/miui/systemui/controller/WeatherController$3.smali
DEX group    : classes3
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/miui/systemui/controller/WeatherController$3.smali'
CLASS_FALLBACK_NAMES = ['WeatherController$3.smali']
DEX_GROUP            = 'classes3'

PATCHES = [
    {
        'id':          'class_add_com_miui_systemui_controller_WeatherController$3',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public final Lcom/miui/systemui/controller/WeatherController$3;\n.super Landroid/database/ContentObserver;\n\n\n# instance fields\n.field public final synthetic this$0:Lcom/miui/systemui/controller/WeatherController;\n\n\n# direct methods\n.method public constructor <init>(Lcom/miui/systemui/controller/WeatherController;Landroid/os/Handler;)V\n    .registers 3\n\n    iput-object p1, p0, Lcom/miui/systemui/controller/WeatherController$3;->this$0:Lcom/miui/systemui/controller/WeatherController;\n\n    invoke-direct {p0, p2}, Landroid/database/ContentObserver;-><init>(Landroid/os/Handler;)V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public final onChange(Z)V\n    .registers 2\n\n    iget-object p0, p0, Lcom/miui/systemui/controller/WeatherController$3;->this$0:Lcom/miui/systemui/controller/WeatherController;\n\n    invoke-virtual {p0}, Lcom/miui/systemui/controller/WeatherController;->startQuery()V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
