"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/miui/systemui/controller/WeatherController$WeatherChangeListener.smali
DEX group    : classes3
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/miui/systemui/controller/WeatherController$WeatherChangeListener.smali'
CLASS_FALLBACK_NAMES = ['WeatherController$WeatherChangeListener.smali']
DEX_GROUP            = 'classes3'

PATCHES = [
    {
        'id':          'class_add_com_miui_systemui_controller_WeatherController$WeatherChange',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public interface abstract Lcom/miui/systemui/controller/WeatherController$WeatherChangeListener;\n.super Ljava/lang/Object;\n\n\n# virtual methods\n.method public abstract onWeatherChange(Lcom/miui/systemui/controller/WeatherController$WeatherInfo;)V\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
