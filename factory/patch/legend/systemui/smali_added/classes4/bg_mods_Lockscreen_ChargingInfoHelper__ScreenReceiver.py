"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : bg/mods/Lockscreen/ChargingInfoHelper$ScreenReceiver.smali
DEX group    : classes4
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'bg/mods/Lockscreen/ChargingInfoHelper$ScreenReceiver.smali'
CLASS_FALLBACK_NAMES = ['ChargingInfoHelper$ScreenReceiver.smali']
DEX_GROUP            = 'classes4'

PATCHES = [
    {
        'id':          'class_add_bg_mods_Lockscreen_ChargingInfoHelper$ScreenReceiver',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lbg/mods/Lockscreen/ChargingInfoHelper$ScreenReceiver;\n.super Landroid/content/BroadcastReceiver;\n\n\n# instance fields\n.field final synthetic this$0:Lbg/mods/Lockscreen/ChargingInfoHelper;\n\n\n# direct methods\n.method constructor <init>(Lbg/mods/Lockscreen/ChargingInfoHelper;)V\n    .registers 2\n\n    iput-object p1, p0, Lbg/mods/Lockscreen/ChargingInfoHelper$ScreenReceiver;->this$0:Lbg/mods/Lockscreen/ChargingInfoHelper;\n\n    invoke-direct {p0}, Landroid/content/BroadcastReceiver;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public onReceive(Landroid/content/Context;Landroid/content/Intent;)V\n    .registers 3\n\n    invoke-virtual {p2}, Landroid/content/Intent;->getAction()Ljava/lang/String;\n\n    move-result-object p1\n\n    const-string p2, "android.intent.action.SCREEN_ON"\n\n    invoke-virtual {p2, p1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z\n\n    move-result p2\n\n    if-eqz p2, :cond_0\n\n    iget-object p1, p0, Lbg/mods/Lockscreen/ChargingInfoHelper$ScreenReceiver;->this$0:Lbg/mods/Lockscreen/ChargingInfoHelper;\n\n    invoke-static {p1}, Lbg/mods/Lockscreen/ChargingInfoHelper;->access$000(Lbg/mods/Lockscreen/ChargingInfoHelper;)V\n\n    iget-object p0, p0, Lbg/mods/Lockscreen/ChargingInfoHelper$ScreenReceiver;->this$0:Lbg/mods/Lockscreen/ChargingInfoHelper;\n\n    invoke-static {p0}, Lbg/mods/Lockscreen/ChargingInfoHelper;->access$300(Lbg/mods/Lockscreen/ChargingInfoHelper;)V\n\n    goto :goto_0\n\n    :cond_0\n    const-string p2, "android.intent.action.SCREEN_OFF"\n\n    invoke-virtual {p2, p1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z\n\n    move-result p1\n\n    if-eqz p1, :cond_1\n\n    iget-object p0, p0, Lbg/mods/Lockscreen/ChargingInfoHelper$ScreenReceiver;->this$0:Lbg/mods/Lockscreen/ChargingInfoHelper;\n\n    invoke-static {p0}, Lbg/mods/Lockscreen/ChargingInfoHelper;->access$400(Lbg/mods/Lockscreen/ChargingInfoHelper;)V\n\n    :cond_1\n    :goto_0\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
