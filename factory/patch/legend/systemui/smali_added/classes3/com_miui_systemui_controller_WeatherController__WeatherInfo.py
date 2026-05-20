"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/miui/systemui/controller/WeatherController$WeatherInfo.smali
DEX group    : classes3
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/miui/systemui/controller/WeatherController$WeatherInfo.smali'
CLASS_FALLBACK_NAMES = ['WeatherController$WeatherInfo.smali']
DEX_GROUP            = 'classes3'

PATCHES = [
    {
        'id':          'class_add_com_miui_systemui_controller_WeatherController$WeatherInfo',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public final Lcom/miui/systemui/controller/WeatherController$WeatherInfo;\n.super Ljava/lang/Object;\n\n\n# instance fields\n.field public cityName:Ljava/lang/String;\n\n.field public description:Ljava/lang/String;\n\n.field public temperature:I\n\n.field public temperatureUnit:I\n\n\n# direct methods\n.method public constructor <init>()V\n    .registers 1\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
