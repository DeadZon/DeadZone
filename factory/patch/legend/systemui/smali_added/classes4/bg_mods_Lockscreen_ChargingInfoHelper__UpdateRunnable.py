"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : bg/mods/Lockscreen/ChargingInfoHelper$UpdateRunnable.smali
DEX group    : classes4
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'bg/mods/Lockscreen/ChargingInfoHelper$UpdateRunnable.smali'
CLASS_FALLBACK_NAMES = ['ChargingInfoHelper$UpdateRunnable.smali']
DEX_GROUP            = 'classes4'

PATCHES = [
    {
        'id':          'class_add_bg_mods_Lockscreen_ChargingInfoHelper$UpdateRunnable',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lbg/mods/Lockscreen/ChargingInfoHelper$UpdateRunnable;\n.super Ljava/lang/Object;\n\n# interfaces\n.implements Ljava/lang/Runnable;\n\n\n# instance fields\n.field final synthetic this$0:Lbg/mods/Lockscreen/ChargingInfoHelper;\n\n\n# direct methods\n.method constructor <init>(Lbg/mods/Lockscreen/ChargingInfoHelper;)V\n    .registers 2\n\n    iput-object p1, p0, Lbg/mods/Lockscreen/ChargingInfoHelper$UpdateRunnable;->this$0:Lbg/mods/Lockscreen/ChargingInfoHelper;\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public run()V\n    .registers 5\n\n    iget-object v0, p0, Lbg/mods/Lockscreen/ChargingInfoHelper$UpdateRunnable;->this$0:Lbg/mods/Lockscreen/ChargingInfoHelper;\n\n    invoke-static {v0}, Lbg/mods/Lockscreen/ChargingInfoHelper;->access$000(Lbg/mods/Lockscreen/ChargingInfoHelper;)V\n\n    iget-object v0, p0, Lbg/mods/Lockscreen/ChargingInfoHelper$UpdateRunnable;->this$0:Lbg/mods/Lockscreen/ChargingInfoHelper;\n\n    invoke-static {v0}, Lbg/mods/Lockscreen/ChargingInfoHelper;->access$100(Lbg/mods/Lockscreen/ChargingInfoHelper;)Landroid/os/Handler;\n\n    move-result-object v1\n\n    iget-object v0, p0, Lbg/mods/Lockscreen/ChargingInfoHelper$UpdateRunnable;->this$0:Lbg/mods/Lockscreen/ChargingInfoHelper;\n\n    invoke-static {v0}, Lbg/mods/Lockscreen/ChargingInfoHelper;->access$200(Lbg/mods/Lockscreen/ChargingInfoHelper;)I\n\n    move-result v0\n\n    int-to-long v2, v0\n\n    invoke-virtual {v1, p0, v2, v3}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
