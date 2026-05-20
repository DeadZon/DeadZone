"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/miui/systemui/controller/WeatherController$WeatherChangeListener.smali'
CLASS_FALLBACK_NAMES = ['WeatherController$WeatherChangeListener.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public interface abstract Lcom/miui/systemui/controller/WeatherController$WeatherChangeListener;
.super Ljava/lang/Object;


# virtual methods
.method public abstract onWeatherChange(Lcom/miui/systemui/controller/WeatherController$WeatherInfo;)V
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_miui_systemui_controller_WeatherController_WeatherChangeListener',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
