"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/justas/AnimationWeather/Weather$1.smali'
CLASS_FALLBACK_NAMES = ['Weather$1.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/justas/AnimationWeather/Weather$1;
.super Landroid/database/ContentObserver;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/justas/AnimationWeather/Weather;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/justas/AnimationWeather/Weather;


# direct methods
.method constructor <init>(Lcom/justas/AnimationWeather/Weather;Landroid/os/Handler;)V
    .registers 3

    iput-object p1, p0, Lcom/justas/AnimationWeather/Weather$1;->this$0:Lcom/justas/AnimationWeather/Weather;

    invoke-direct {p0, p2}, Landroid/database/ContentObserver;-><init>(Landroid/os/Handler;)V

    return-void
.end method


# virtual methods
.method public onChange(Z)V
    .registers 3

    invoke-super {p0, p1}, Landroid/database/ContentObserver;->onChange(Z)V

    iget-object v0, p0, Lcom/justas/AnimationWeather/Weather$1;->this$0:Lcom/justas/AnimationWeather/Weather;

    invoke-static {v0}, Lcom/justas/AnimationWeather/Weather;->access$000(Lcom/justas/AnimationWeather/Weather;)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_justas_AnimationWeather_Weather_1',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
