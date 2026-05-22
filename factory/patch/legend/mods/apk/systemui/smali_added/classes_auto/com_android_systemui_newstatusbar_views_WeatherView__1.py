"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/views/WeatherView$1.smali'
CLASS_FALLBACK_NAMES = ['WeatherView$1.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/newstatusbar/views/WeatherView$1;
.super Ljava/lang/Object;

# interfaces
.implements Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/systemui/newstatusbar/views/WeatherView;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/android/systemui/newstatusbar/views/WeatherView;


# direct methods
.method constructor <init>(Lcom/android/systemui/newstatusbar/views/WeatherView;)V
    .registers 2

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/views/WeatherView$1;->this$0:Lcom/android/systemui/newstatusbar/views/WeatherView;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public onDataChanged()V
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/WeatherView$1;->this$0:Lcom/android/systemui/newstatusbar/views/WeatherView;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/views/WeatherView;->update()V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_views_WeatherView_1',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
