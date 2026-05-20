"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate.smali'
CLASS_FALLBACK_NAMES = ['BatteryMeterIconViewMinit$MinitUpdate.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_battery_BatteryMeterIconVi',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate;\n.super Ljava/lang/Object;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingClass;\n    value = Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x8\n    name = "MinitUpdate"\n.end annotation\n\n\n# instance fields\n.field private final list:Ljava/util/List;\n    .annotation system Ldalvik/annotation/Signature;\n        value = {\n            "Ljava/util/List<",\n            "Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;",\n            ">;"\n        }\n    .end annotation\n.end field\n\n\n# direct methods\n.method public constructor <init>(Landroid/content/Context;)V\n    .registers 5\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    new-instance v0, Ljava/util/ArrayList;\n\n    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V\n\n    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate;->list:Ljava/util/List;\n\n    new-instance v0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate$1;\n\n    invoke-direct {v0, p0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate$1;-><init>(Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate;)V\n\n    new-instance v1, Landroid/content/IntentFilter;\n\n    const-string v2, "com.three.minit.BATTERY_TYPE_CHANGED"\n\n    invoke-direct {v1, v2}, Landroid/content/IntentFilter;-><init>(Ljava/lang/String;)V\n\n    const/4 v2, 0x2\n\n    invoke-virtual {p1, v0, v1, v2}, Landroid/content/Context;->registerReceiver(Landroid/content/BroadcastReceiver;Landroid/content/IntentFilter;I)Landroid/content/Intent;\n\n    return-void\n.end method\n\n\n# virtual methods\n.method addCallBack(Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;)V\n    .registers 3\n\n    goto :goto_1\n\n    nop\n\n    :goto_0\n    return-void\n\n    :goto_1\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate;->list:Ljava/util/List;\n\n    goto :goto_2\n\n    nop\n\n    :goto_2\n    invoke-interface {v0, p1}, Ljava/util/List;->add(Ljava/lang/Object;)Z\n\n    goto :goto_0\n\n    nop\n.end method\n\n.method removeCallBack(Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;)V\n    .registers 3\n\n    goto :goto_2\n\n    nop\n\n    :goto_0\n    invoke-interface {v0, p1}, Ljava/util/List;->remove(Ljava/lang/Object;)Z\n\n    goto :goto_1\n\n    nop\n\n    :goto_1\n    return-void\n\n    :goto_2\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate;->list:Ljava/util/List;\n\n    goto :goto_0\n\n    nop\n.end method\n\n.method update()V\n    .registers 3\n\n    goto :goto_5\n\n    nop\n\n    :goto_0\n    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;\n\n    move-result-object v1\n\n    goto :goto_3\n\n    nop\n\n    :goto_1\n    invoke-interface {v0}, Ljava/util/List;->iterator()Ljava/util/Iterator;\n\n    move-result-object v0\n\n    :goto_2\n    goto :goto_a\n\n    nop\n\n    :goto_3\n    check-cast v1, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;\n\n    goto :goto_8\n\n    nop\n\n    :goto_4\n    return-void\n\n    :goto_5\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate;->list:Ljava/util/List;\n\n    goto :goto_1\n\n    nop\n\n    :goto_6\n    goto :goto_2\n\n    :goto_7\n    goto :goto_4\n\n    nop\n\n    :goto_8\n    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->updateImage()V\n\n    goto :goto_6\n\n    nop\n\n    :goto_9\n    if-nez v1, :cond_0\n\n    goto :goto_7\n\n    :cond_0\n    goto :goto_0\n\n    nop\n\n    :goto_a\n    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z\n\n    move-result v1\n\n    goto :goto_9\n\n    nop\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
