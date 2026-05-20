"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/miui/systemui/controller/WeatherController$2.smali
DEX group    : classes3
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/miui/systemui/controller/WeatherController$2.smali'
CLASS_FALLBACK_NAMES = ['WeatherController$2.smali']
DEX_GROUP            = 'classes3'

PATCHES = [
    {
        'id':          'class_add_com_miui_systemui_controller_WeatherController$2',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public final Lcom/miui/systemui/controller/WeatherController$2;\n.super Landroid/content/BroadcastReceiver;\n\n\n# instance fields\n.field public final synthetic this$0:Lcom/miui/systemui/controller/WeatherController;\n\n\n# direct methods\n.method public constructor <init>(Lcom/miui/systemui/controller/WeatherController;)V\n    .registers 2\n\n    iput-object p1, p0, Lcom/miui/systemui/controller/WeatherController$2;->this$0:Lcom/miui/systemui/controller/WeatherController;\n\n    invoke-direct {p0}, Landroid/content/BroadcastReceiver;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public final onReceive(Landroid/content/Context;Landroid/content/Intent;)V\n    .registers 3\n\n    invoke-virtual {p2}, Landroid/content/Intent;->getData()Landroid/net/Uri;\n\n    move-result-object p1\n\n    invoke-virtual {p1}, Landroid/net/Uri;->getSchemeSpecificPart()Ljava/lang/String;\n\n    move-result-object p1\n\n    const-string p2, "com.miui.weather2"\n\n    invoke-virtual {p2, p1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z\n\n    move-result p1\n\n    if-eqz p1, :cond_0\n\n    iget-object p0, p0, Lcom/miui/systemui/controller/WeatherController$2;->this$0:Lcom/miui/systemui/controller/WeatherController;\n\n    invoke-virtual {p0}, Lcom/miui/systemui/controller/WeatherController;->updateState()V\n\n    :cond_0\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
