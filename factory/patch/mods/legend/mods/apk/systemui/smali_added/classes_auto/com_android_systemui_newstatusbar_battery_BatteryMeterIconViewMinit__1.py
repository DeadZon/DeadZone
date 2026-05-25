"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$1.smali'
CLASS_FALLBACK_NAMES = ['BatteryMeterIconViewMinit$1.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$1;
.super Ljava/lang/Object;

# interfaces
.implements Ljava/lang/Runnable;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->setImage()V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;


# direct methods
.method constructor <init>(Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;)V
    .registers 2

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$1;->this$0:Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public run()V
    .registers 4

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$1;->this$0:Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;

    invoke-static {v0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->access$000(Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;)Landroid/graphics/drawable/Drawable;

    move-result-object v0

    sget-object v1, Lcom/android/systemui/newstatusbar/thread/ThreadUtils$HandlerHolder;->INSTANCE:Landroid/os/Handler;

    new-instance v2, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$1$1;

    invoke-direct {v2, p0, v0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$1$1;-><init>(Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$1;Landroid/graphics/drawable/Drawable;)V

    invoke-virtual {v1, v2}, Landroid/os/Handler;->post(Ljava/lang/Runnable;)Z

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_battery_BatteryMeterIconViewMinit_1',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
