"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/miui/systemui/controller/WeatherController$QueryHandler.smali
DEX group    : classes3
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/miui/systemui/controller/WeatherController$QueryHandler.smali'
CLASS_FALLBACK_NAMES = ['WeatherController$QueryHandler.smali']
DEX_GROUP            = 'classes3'

PATCHES = [
    {
        'id':          'class_add_com_miui_systemui_controller_WeatherController$QueryHandler',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public final Lcom/miui/systemui/controller/WeatherController$QueryHandler;\n.super Landroid/content/AsyncQueryHandler;\n\n\n# instance fields\n.field public final synthetic this$0:Lcom/miui/systemui/controller/WeatherController;\n\n\n# direct methods\n.method public constructor <init>(Lcom/miui/systemui/controller/WeatherController;Landroid/content/Context;)V\n    .registers 3\n\n    iput-object p1, p0, Lcom/miui/systemui/controller/WeatherController$QueryHandler;->this$0:Lcom/miui/systemui/controller/WeatherController;\n\n    invoke-virtual {p2}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;\n\n    move-result-object p2\n\n    invoke-direct {p0, p2}, Landroid/content/AsyncQueryHandler;-><init>(Landroid/content/ContentResolver;)V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public final createHandler(Landroid/os/Looper;)Landroid/os/Handler;\n    .registers 3\n\n    new-instance v0, Lcom/miui/systemui/controller/WeatherController$QueryHandler$CatchingWorkerHandler;\n\n    invoke-direct {v0, p0, p1}, Lcom/miui/systemui/controller/WeatherController$QueryHandler$CatchingWorkerHandler;-><init>(Lcom/miui/systemui/controller/WeatherController$QueryHandler;Landroid/os/Looper;)V\n\n    return-object v0\n.end method\n\n.method public final onQueryComplete(ILjava/lang/Object;Landroid/database/Cursor;)V\n    .registers 4\n\n    iget-object p0, p0, Lcom/miui/systemui/controller/WeatherController$QueryHandler;->this$0:Lcom/miui/systemui/controller/WeatherController;\n\n    invoke-virtual {p0, p3}, Lcom/miui/systemui/controller/WeatherController;->updateWeather(Landroid/database/Cursor;)V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
