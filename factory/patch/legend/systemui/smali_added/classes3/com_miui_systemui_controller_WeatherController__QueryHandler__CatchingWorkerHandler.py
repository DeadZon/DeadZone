"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/miui/systemui/controller/WeatherController$QueryHandler$CatchingWorkerHandler.smali
DEX group    : classes3
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/miui/systemui/controller/WeatherController$QueryHandler$CatchingWorkerHandler.smali'
CLASS_FALLBACK_NAMES = ['WeatherController$QueryHandler$CatchingWorkerHandler.smali']
DEX_GROUP            = 'classes3'

PATCHES = [
    {
        'id':          'class_add_com_miui_systemui_controller_WeatherController$QueryHandler$',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public final Lcom/miui/systemui/controller/WeatherController$QueryHandler$CatchingWorkerHandler;\n.super Landroid/content/AsyncQueryHandler$WorkerHandler;\n\n\n# instance fields\n.field public final synthetic this$1:Lcom/miui/systemui/controller/WeatherController$QueryHandler;\n\n\n# direct methods\n.method public constructor <init>(Lcom/miui/systemui/controller/WeatherController$QueryHandler;Landroid/os/Looper;)V\n    .registers 3\n\n    iput-object p1, p0, Lcom/miui/systemui/controller/WeatherController$QueryHandler$CatchingWorkerHandler;->this$1:Lcom/miui/systemui/controller/WeatherController$QueryHandler;\n\n    invoke-direct {p0, p1, p2}, Landroid/content/AsyncQueryHandler$WorkerHandler;-><init>(Landroid/content/AsyncQueryHandler;Landroid/os/Looper;)V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public final handleMessage(Landroid/os/Message;)V\n    .registers 3\n\n    :try_start_0\n    invoke-super {p0, p1}, Landroid/content/AsyncQueryHandler$WorkerHandler;->handleMessage(Landroid/os/Message;)V\n    :try_end_0\n    .catch Landroid/database/sqlite/SQLiteDiskIOException; {:try_start_0 .. :try_end_0} :catch_0\n    .catch Landroid/database/sqlite/SQLiteFullException; {:try_start_0 .. :try_end_0} :catch_0\n    .catch Landroid/database/sqlite/SQLiteDatabaseCorruptException; {:try_start_0 .. :try_end_0} :catch_0\n\n    return-void\n\n    :catch_0\n    move-exception v0\n\n    const-string p0, "WeatherController"\n\n    const-string p1, "Exception on background worker thread"\n\n    invoke-static {p0, p1, v0}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
