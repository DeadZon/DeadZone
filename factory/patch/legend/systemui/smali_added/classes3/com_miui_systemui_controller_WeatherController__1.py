"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/miui/systemui/controller/WeatherController$1.smali
DEX group    : classes3
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/miui/systemui/controller/WeatherController$1.smali'
CLASS_FALLBACK_NAMES = ['WeatherController$1.smali']
DEX_GROUP            = 'classes3'

PATCHES = [
    {
        'id':          'class_add_com_miui_systemui_controller_WeatherController$1',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public final Lcom/miui/systemui/controller/WeatherController$1;\n.super Landroid/database/ContentObserver;\n\n\n# instance fields\n.field public final synthetic this$0:Lcom/miui/systemui/controller/WeatherController;\n\n\n# direct methods\n.method public constructor <init>(Lcom/miui/systemui/controller/WeatherController;Landroid/os/Handler;)V\n    .registers 3\n\n    iput-object p1, p0, Lcom/miui/systemui/controller/WeatherController$1;->this$0:Lcom/miui/systemui/controller/WeatherController;\n\n    invoke-direct {p0, p2}, Landroid/database/ContentObserver;-><init>(Landroid/os/Handler;)V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public final onChange(Z)V\n    .registers 5\n\n    iget-object p1, p0, Lcom/miui/systemui/controller/WeatherController$1;->this$0:Lcom/miui/systemui/controller/WeatherController;\n\n    iget-object v0, p1, Lcom/miui/systemui/controller/WeatherController;->mContext:Landroid/content/Context;\n\n    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;\n\n    move-result-object v0\n\n    const-string v1, "status_bar_show_weather"\n\n    const/4 v2, 0x1\n\n    invoke-static {v0, v1, v2}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I\n\n    move-result v0\n\n    if-ne v0, v2, :cond_0\n\n    goto :goto_0\n\n    :cond_0\n    const/4 v2, 0x0\n\n    :goto_0\n    iput-boolean v2, p1, Lcom/miui/systemui/controller/WeatherController;->mEnabled:Z\n\n    iget-object p0, p0, Lcom/miui/systemui/controller/WeatherController$1;->this$0:Lcom/miui/systemui/controller/WeatherController;\n\n    invoke-virtual {p0}, Lcom/miui/systemui/controller/WeatherController;->updateState()V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
