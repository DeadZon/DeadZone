"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate.smali'
CLASS_FALLBACK_NAMES = ['BatteryMeterIconViewMinit$MinitUpdate.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x8
    name = "MinitUpdate"
.end annotation


# instance fields
.field private final list:Ljava/util/List;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/List<",
            "Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;",
            ">;"
        }
    .end annotation
.end field


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 5

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate;->list:Ljava/util/List;

    new-instance v0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate$1;

    invoke-direct {v0, p0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate$1;-><init>(Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate;)V

    new-instance v1, Landroid/content/IntentFilter;

    const-string v2, "com.three.minit.BATTERY_TYPE_CHANGED"

    invoke-direct {v1, v2}, Landroid/content/IntentFilter;-><init>(Ljava/lang/String;)V

    const/4 v2, 0x2

    invoke-virtual {p1, v0, v1, v2}, Landroid/content/Context;->registerReceiver(Landroid/content/BroadcastReceiver;Landroid/content/IntentFilter;I)Landroid/content/Intent;

    return-void
.end method


# virtual methods
.method addCallBack(Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;)V
    .registers 3

    goto/32 :goto_5

    nop

    :goto_4
    return-void

    :goto_5
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate;->list:Ljava/util/List;

    goto/32 :goto_b

    nop

    :goto_b
    invoke-interface {v0, p1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    goto/32 :goto_4

    nop
.end method

.method removeCallBack(Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;)V
    .registers 3

    goto/32 :goto_c

    nop

    :goto_4
    invoke-interface {v0, p1}, Ljava/util/List;->remove(Ljava/lang/Object;)Z

    goto/32 :goto_b

    nop

    :goto_b
    return-void

    :goto_c
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate;->list:Ljava/util/List;

    goto/32 :goto_4

    nop
.end method

.method update()V
    .registers 3

    goto/32 :goto_1b

    nop

    :goto_4
    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    goto/32 :goto_14

    nop

    :goto_c
    invoke-interface {v0}, Ljava/util/List;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_10
    goto/32 :goto_36

    nop

    :goto_14
    check-cast v1, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;

    goto/32 :goto_26

    nop

    :goto_1a
    return-void

    :goto_1b
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate;->list:Ljava/util/List;

    goto/32 :goto_c

    nop

    :goto_21
    goto :goto_10

    :goto_22
    goto/32 :goto_1a

    nop

    :goto_26
    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->updateImage()V

    goto/32 :goto_21

    nop

    :goto_2d
    if-nez v1, :cond_32

    goto/32 :goto_22

    :cond_32
    goto/32 :goto_4

    nop

    :goto_36
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    goto/32 :goto_2d

    nop
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_battery_BatteryMeterIconViewMinit_MinitUpdate',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
