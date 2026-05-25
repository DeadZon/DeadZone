"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/miui/systemui/controller/WeatherController$QueryHandler.smali'
CLASS_FALLBACK_NAMES = ['WeatherController$QueryHandler.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public final Lcom/miui/systemui/controller/WeatherController$QueryHandler;
.super Landroid/content/AsyncQueryHandler;


# instance fields
.field public final synthetic this$0:Lcom/miui/systemui/controller/WeatherController;


# direct methods
.method public constructor <init>(Lcom/miui/systemui/controller/WeatherController;Landroid/content/Context;)V
    .registers 3

    iput-object p1, p0, Lcom/miui/systemui/controller/WeatherController$QueryHandler;->this$0:Lcom/miui/systemui/controller/WeatherController;

    invoke-virtual {p2}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p2

    invoke-direct {p0, p2}, Landroid/content/AsyncQueryHandler;-><init>(Landroid/content/ContentResolver;)V

    return-void
.end method


# virtual methods
.method public final createHandler(Landroid/os/Looper;)Landroid/os/Handler;
    .registers 3

    new-instance v0, Lcom/miui/systemui/controller/WeatherController$QueryHandler$CatchingWorkerHandler;

    invoke-direct {v0, p0, p1}, Lcom/miui/systemui/controller/WeatherController$QueryHandler$CatchingWorkerHandler;-><init>(Lcom/miui/systemui/controller/WeatherController$QueryHandler;Landroid/os/Looper;)V

    return-object v0
.end method

.method public final onQueryComplete(ILjava/lang/Object;Landroid/database/Cursor;)V
    .registers 4

    iget-object p0, p0, Lcom/miui/systemui/controller/WeatherController$QueryHandler;->this$0:Lcom/miui/systemui/controller/WeatherController;

    invoke-virtual {p0, p3}, Lcom/miui/systemui/controller/WeatherController;->updateWeather(Landroid/database/Cursor;)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_miui_systemui_controller_WeatherController_QueryHandler',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
