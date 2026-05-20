"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/views/WeatherView$1.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/views/WeatherView$1.smali'
CLASS_FALLBACK_NAMES = ['WeatherView$1.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_views_WeatherView$1',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/newstatusbar/views/WeatherView$1;\n.super Ljava/lang/Object;\n\n# interfaces\n.implements Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingClass;\n    value = Lcom/android/systemui/newstatusbar/views/WeatherView;\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic this$0:Lcom/android/systemui/newstatusbar/views/WeatherView;\n\n\n# direct methods\n.method constructor <init>(Lcom/android/systemui/newstatusbar/views/WeatherView;)V\n    .registers 2\n\n    iput-object p1, p0, Lcom/android/systemui/newstatusbar/views/WeatherView$1;->this$0:Lcom/android/systemui/newstatusbar/views/WeatherView;\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public onDataChanged()V\n    .registers 2\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/WeatherView$1;->this$0:Lcom/android/systemui/newstatusbar/views/WeatherView;\n\n    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/views/WeatherView;->update()V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
