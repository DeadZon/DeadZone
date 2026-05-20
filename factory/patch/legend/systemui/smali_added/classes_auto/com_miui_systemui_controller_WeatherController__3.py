"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/miui/systemui/controller/WeatherController$3.smali'
CLASS_FALLBACK_NAMES = ['WeatherController$3.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public final Lcom/miui/systemui/controller/WeatherController$3;
.super Landroid/database/ContentObserver;


# instance fields
.field public final synthetic this$0:Lcom/miui/systemui/controller/WeatherController;


# direct methods
.method public constructor <init>(Lcom/miui/systemui/controller/WeatherController;Landroid/os/Handler;)V
    .registers 3

    iput-object p1, p0, Lcom/miui/systemui/controller/WeatherController$3;->this$0:Lcom/miui/systemui/controller/WeatherController;

    invoke-direct {p0, p2}, Landroid/database/ContentObserver;-><init>(Landroid/os/Handler;)V

    return-void
.end method


# virtual methods
.method public final onChange(Z)V
    .registers 2

    iget-object p0, p0, Lcom/miui/systemui/controller/WeatherController$3;->this$0:Lcom/miui/systemui/controller/WeatherController;

    invoke-virtual {p0}, Lcom/miui/systemui/controller/WeatherController;->startQuery()V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_miui_systemui_controller_WeatherController_3',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
