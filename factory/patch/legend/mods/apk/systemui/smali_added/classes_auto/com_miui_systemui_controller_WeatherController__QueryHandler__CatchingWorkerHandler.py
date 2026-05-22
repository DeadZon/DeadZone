"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/miui/systemui/controller/WeatherController$QueryHandler$CatchingWorkerHandler.smali'
CLASS_FALLBACK_NAMES = ['WeatherController$QueryHandler$CatchingWorkerHandler.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public final Lcom/miui/systemui/controller/WeatherController$QueryHandler$CatchingWorkerHandler;
.super Landroid/content/AsyncQueryHandler$WorkerHandler;


# instance fields
.field public final synthetic this$1:Lcom/miui/systemui/controller/WeatherController$QueryHandler;


# direct methods
.method public constructor <init>(Lcom/miui/systemui/controller/WeatherController$QueryHandler;Landroid/os/Looper;)V
    .registers 3

    iput-object p1, p0, Lcom/miui/systemui/controller/WeatherController$QueryHandler$CatchingWorkerHandler;->this$1:Lcom/miui/systemui/controller/WeatherController$QueryHandler;

    invoke-direct {p0, p1, p2}, Landroid/content/AsyncQueryHandler$WorkerHandler;-><init>(Landroid/content/AsyncQueryHandler;Landroid/os/Looper;)V

    return-void
.end method


# virtual methods
.method public final handleMessage(Landroid/os/Message;)V
    .registers 3

    :try_start_0
    invoke-super {p0, p1}, Landroid/content/AsyncQueryHandler$WorkerHandler;->handleMessage(Landroid/os/Message;)V
    :try_end_3
    .catch Landroid/database/sqlite/SQLiteDiskIOException; {:try_start_0 .. :try_end_3} :catch_4
    .catch Landroid/database/sqlite/SQLiteFullException; {:try_start_0 .. :try_end_3} :catch_4
    .catch Landroid/database/sqlite/SQLiteDatabaseCorruptException; {:try_start_0 .. :try_end_3} :catch_4

    return-void

    :catch_4
    move-exception v0

    const-string p0, "WeatherController"

    const-string p1, "Exception on background worker thread"

    invoke-static {p0, p1, v0}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_miui_systemui_controller_WeatherController_QueryHandler_CatchingWorkerHandler',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
