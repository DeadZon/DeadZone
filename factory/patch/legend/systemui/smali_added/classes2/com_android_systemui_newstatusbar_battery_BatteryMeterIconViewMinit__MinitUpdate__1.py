"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate$1.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate$1.smali'
CLASS_FALLBACK_NAMES = ['BatteryMeterIconViewMinit$MinitUpdate$1.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_battery_BatteryMeterIconVi',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate$1;\n.super Landroid/content/BroadcastReceiver;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingMethod;\n    value = Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate;-><init>(Landroid/content/Context;)V\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic this$0:Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate;\n\n\n# direct methods\n.method constructor <init>(Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate;)V\n    .registers 2\n\n    iput-object p1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate$1;->this$0:Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate;\n\n    invoke-direct {p0}, Landroid/content/BroadcastReceiver;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public onReceive(Landroid/content/Context;Landroid/content/Intent;)V\n    .registers 5\n\n    invoke-virtual {p2}, Landroid/content/Intent;->getAction()Ljava/lang/String;\n\n    move-result-object v0\n\n    const-string v1, "com.three.minit.BATTERY_TYPE_CHANGED"\n\n    invoke-virtual {v1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z\n\n    move-result v0\n\n    if-eqz v0, :cond_0\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate$1;->this$0:Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate;\n\n    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate;->update()V\n\n    :cond_0\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
