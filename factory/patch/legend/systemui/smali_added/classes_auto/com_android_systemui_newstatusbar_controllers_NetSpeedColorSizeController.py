"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/controllers/NetSpeedColorSizeController.smali'
CLASS_FALLBACK_NAMES = ['NetSpeedColorSizeController.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/controllers/NetSpeedColorSizeController;
.super Lcom/android/systemui/newstatusbar/controllers/IconController;


# static fields
.field private static final key:Ljava/lang/String; = "net_speed"


# instance fields
.field private final callBacks:Ljava/util/ArrayList;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/ArrayList<",
            "Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;",
            ">;"
        }
    .end annotation
.end field

.field private final currData:Lcom/android/systemui/newstatusbar/data/TextData;


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 5

    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/controllers/IconController;-><init>(Landroid/content/Context;)V

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/NetSpeedColorSizeController;->callBacks:Ljava/util/ArrayList;

    new-instance v0, Lcom/android/systemui/newstatusbar/data/TextData;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/NetSpeedColorSizeController;->context:Landroid/content/Context;

    const-string v2, "net_speed"

    invoke-direct {v0, v1, v2}, Lcom/android/systemui/newstatusbar/data/TextData;-><init>(Landroid/content/Context;Ljava/lang/String;)V

    const/4 v1, 0x0

    new-array v1, v1, [Ljava/lang/String;

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/data/TextData;->addKeys([Ljava/lang/String;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    const-string v1, "net_speed_height"

    filled-new-array {v1}, [Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/data/Data;->addKeys([Ljava/lang/String;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    new-instance v1, Lcom/android/systemui/newstatusbar/controllers/NetSpeedColorSizeController$1;

    invoke-direct {v1, p0}, Lcom/android/systemui/newstatusbar/controllers/NetSpeedColorSizeController$1;-><init>(Lcom/android/systemui/newstatusbar/controllers/NetSpeedColorSizeController;)V

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/data/Data;->addListener(Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/data/Data;->update()Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/data/TextData;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/NetSpeedColorSizeController;->currData:Lcom/android/systemui/newstatusbar/data/TextData;

    return-void
.end method


# virtual methods
.method public addCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/NetSpeedColorSizeController;->callBacks:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    return-void
.end method

.method public bridge synthetic addCallBack(Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;)V
    .registers 2

    check-cast p1, Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;

    invoke-virtual {p0, p1}, Lcom/android/systemui/newstatusbar/controllers/NetSpeedColorSizeController;->addCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V

    return-void
.end method

.method public getCurrData()Lcom/android/systemui/newstatusbar/data/TextData;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/NetSpeedColorSizeController;->currData:Lcom/android/systemui/newstatusbar/data/TextData;

    return-object v0
.end method

.method public onCustomChanged(Ljava/lang/String;)V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/NetSpeedColorSizeController;->currData:Lcom/android/systemui/newstatusbar/data/TextData;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/data/TextData;->update()Lcom/android/systemui/newstatusbar/data/Data;

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/NetSpeedColorSizeController;->callBacks:Ljava/util/ArrayList;

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/controllers/NetSpeedColorSizeController;->updateCallBacks(Ljava/util/ArrayList;)V

    return-void
.end method

.method public removeCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/NetSpeedColorSizeController;->callBacks:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    return-void
.end method

.method public bridge synthetic removeCallBack(Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;)V
    .registers 2

    check-cast p1, Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;

    invoke-virtual {p0, p1}, Lcom/android/systemui/newstatusbar/controllers/NetSpeedColorSizeController;->removeCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_controllers_NetSpeedColorSizeController',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
