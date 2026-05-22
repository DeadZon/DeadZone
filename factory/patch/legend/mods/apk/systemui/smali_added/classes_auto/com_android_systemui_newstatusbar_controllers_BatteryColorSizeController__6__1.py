"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/controllers/BatteryColorSizeController$6$1.smali'
CLASS_FALLBACK_NAMES = ['BatteryColorSizeController$6$1.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$6$1;
.super Ljava/lang/Object;

# interfaces
.implements Ljava/lang/Runnable;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$6;->run()V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$1:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$6;


# direct methods
.method constructor <init>(Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$6;)V
    .registers 2

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$6$1;->this$1:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$6;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public run()V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$6$1;->this$1:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$6;

    iget-object v0, v0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$6;->this$0:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    invoke-static {v0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->access$900(Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;)Lcom/android/systemui/newstatusbar/data/TextData;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/data/TextData;->update()Lcom/android/systemui/newstatusbar/data/Data;

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$6$1;->this$1:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$6;

    iget-object v0, v0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$6;->this$0:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    invoke-static {v0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->access$400(Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$6$1;->this$1:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$6;

    iget-object v0, v0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$6;->this$0:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$6$1;->this$1:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$6;

    iget-object v1, v1, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$6;->this$0:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    invoke-static {v1}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->access$500(Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;)Ljava/util/ArrayList;

    move-result-object v1

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->updateCallBacks(Ljava/util/ArrayList;)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$6$1;->this$1:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$6;

    iget-object v0, v0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$6;->this$0:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$6$1;->this$1:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$6;

    iget-object v1, v1, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$6;->this$0:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    invoke-static {v1}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->access$200(Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;)Ljava/util/ArrayList;

    move-result-object v1

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->updateCallBacks(Ljava/util/ArrayList;)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$6$1;->this$1:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$6;

    iget-object v0, v0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$6;->this$0:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$6$1;->this$1:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$6;

    iget-object v1, v1, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$6;->this$0:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    invoke-static {v1}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->access$300(Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;)Ljava/util/ArrayList;

    move-result-object v1

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->updateCallBacks(Ljava/util/ArrayList;)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_controllers_BatteryColorSizeController_6_1',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
