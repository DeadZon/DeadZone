"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$1.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$1.smali'
CLASS_FALLBACK_NAMES = ['BatteryMeterIconViewMinit$1.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_battery_BatteryMeterIconVi',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$1;\n.super Ljava/lang/Object;\n\n# interfaces\n.implements Ljava/lang/Runnable;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingMethod;\n    value = Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->setImage()V\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic this$0:Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;\n\n\n# direct methods\n.method constructor <init>(Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;)V\n    .registers 2\n\n    iput-object p1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$1;->this$0:Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public run()V\n    .registers 4\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$1;->this$0:Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;\n\n    invoke-static {v0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->access$000(Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;)Landroid/graphics/drawable/Drawable;\n\n    move-result-object v0\n\n    sget-object v1, Lcom/android/systemui/newstatusbar/thread/ThreadUtils$HandlerHolder;->INSTANCE:Landroid/os/Handler;\n\n    new-instance v2, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$1$1;\n\n    invoke-direct {v2, p0, v0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$1$1;-><init>(Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$1;Landroid/graphics/drawable/Drawable;)V\n\n    invoke-virtual {v1, v2}, Landroid/os/Handler;->post(Ljava/lang/Runnable;)Z\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
