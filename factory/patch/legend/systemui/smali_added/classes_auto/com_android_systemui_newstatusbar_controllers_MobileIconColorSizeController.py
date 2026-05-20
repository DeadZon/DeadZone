"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/controllers/MobileIconColorSizeController.smali'
CLASS_FALLBACK_NAMES = ['MobileIconColorSizeController.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;
.super Lcom/android/systemui/newstatusbar/controllers/IconController;

# interfaces
.implements Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;


# static fields
.field private static final sKeys:[Ljava/lang/String;


# instance fields
.field private final simCallBacks:Ljava/util/ArrayList;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/ArrayList<",
            "Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;",
            ">;"
        }
    .end annotation
.end field

.field private final simData:Lcom/android/systemui/newstatusbar/data/IconData;

.field private final simTypeCallBacks:Ljava/util/ArrayList;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/ArrayList<",
            "Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;",
            ">;"
        }
    .end annotation
.end field

.field private final simTypeData:Lcom/android/systemui/newstatusbar/data/TextData;

.field private final simTypeInOutCallBacks:Ljava/util/ArrayList;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/ArrayList<",
            "Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;",
            ">;"
        }
    .end annotation
.end field

.field private final simTypeInOutData:Lcom/android/systemui/newstatusbar/data/IconData;

.field private final wifiCallBacks:Ljava/util/ArrayList;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/ArrayList<",
            "Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;",
            ">;"
        }
    .end annotation
.end field

.field private final wifiData:Lcom/android/systemui/newstatusbar/data/IconData;

.field private final wifiInOutCallBacks:Ljava/util/ArrayList;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/ArrayList<",
            "Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;",
            ">;"
        }
    .end annotation
.end field

.field private final wifiInOutData:Lcom/android/systemui/newstatusbar/data/IconData;


# direct methods
.method static constructor <clinit>()V
    .registers 5

    const-string v0, "sim_zoom"

    const-string v1, "wifiview_color"

    const-string v2, "airplaneview_color"

    const-string v3, "mobile_inout_color"

    const-string v4, "mobile_type_color"

    filled-new-array {v0, v1, v2, v3, v4}, [Ljava/lang/String;

    move-result-object v0

    sput-object v0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->sKeys:[Ljava/lang/String;

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;)V
    .registers 6

    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/controllers/IconController;-><init>(Landroid/content/Context;)V

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->simCallBacks:Ljava/util/ArrayList;

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->wifiCallBacks:Ljava/util/ArrayList;

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->wifiInOutCallBacks:Ljava/util/ArrayList;

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->simTypeCallBacks:Ljava/util/ArrayList;

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->simTypeInOutCallBacks:Ljava/util/ArrayList;

    new-instance v0, Lcom/android/systemui/newstatusbar/data/IconData;

    const-string v1, "simview"

    invoke-direct {v0, p1, v1}, Lcom/android/systemui/newstatusbar/data/IconData;-><init>(Landroid/content/Context;Ljava/lang/String;)V

    const/4 v1, 0x0

    new-array v2, v1, [Ljava/lang/String;

    invoke-virtual {v0, v2}, Lcom/android/systemui/newstatusbar/data/IconData;->addKeys([Ljava/lang/String;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    const-string v2, "sim_one_color"

    const-string v3, "sim_two_color"

    filled-new-array {v2, v3}, [Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v0, v2}, Lcom/android/systemui/newstatusbar/data/Data;->addKeys([Ljava/lang/String;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    new-instance v2, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController$1;

    invoke-direct {v2, p0}, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController$1;-><init>(Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;)V

    invoke-virtual {v0, v2}, Lcom/android/systemui/newstatusbar/data/Data;->addListener(Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/data/Data;->update()Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/data/IconData;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->simData:Lcom/android/systemui/newstatusbar/data/IconData;

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->updateSimData()V

    new-instance v0, Lcom/android/systemui/newstatusbar/data/IconData;

    const-string v2, "wifiview"

    invoke-direct {v0, p1, v2}, Lcom/android/systemui/newstatusbar/data/IconData;-><init>(Landroid/content/Context;Ljava/lang/String;)V

    new-array v2, v1, [Ljava/lang/String;

    invoke-virtual {v0, v2}, Lcom/android/systemui/newstatusbar/data/IconData;->addKeys([Ljava/lang/String;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    new-instance v2, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController$2;

    invoke-direct {v2, p0}, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController$2;-><init>(Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;)V

    invoke-virtual {v0, v2}, Lcom/android/systemui/newstatusbar/data/Data;->addListener(Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/data/Data;->update()Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/data/IconData;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->wifiData:Lcom/android/systemui/newstatusbar/data/IconData;

    new-instance v0, Lcom/android/systemui/newstatusbar/data/IconData;

    const-string v2, "airplaneview"

    invoke-direct {v0, p1, v2}, Lcom/android/systemui/newstatusbar/data/IconData;-><init>(Landroid/content/Context;Ljava/lang/String;)V

    new-array v2, v1, [Ljava/lang/String;

    invoke-virtual {v0, v2}, Lcom/android/systemui/newstatusbar/data/IconData;->addKeys([Ljava/lang/String;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    new-instance v2, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController$3;

    invoke-direct {v2, p0}, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController$3;-><init>(Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;)V

    invoke-virtual {v0, v2}, Lcom/android/systemui/newstatusbar/data/Data;->addListener(Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/data/Data;->update()Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/data/IconData;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->wifiInOutData:Lcom/android/systemui/newstatusbar/data/IconData;

    new-instance v0, Lcom/android/systemui/newstatusbar/data/IconData;

    const-string v2, "mobile_inout"

    invoke-direct {v0, p1, v2}, Lcom/android/systemui/newstatusbar/data/IconData;-><init>(Landroid/content/Context;Ljava/lang/String;)V

    new-array v2, v1, [Ljava/lang/String;

    invoke-virtual {v0, v2}, Lcom/android/systemui/newstatusbar/data/IconData;->addKeys([Ljava/lang/String;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    new-instance v2, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController$4;

    invoke-direct {v2, p0}, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController$4;-><init>(Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;)V

    invoke-virtual {v0, v2}, Lcom/android/systemui/newstatusbar/data/Data;->addListener(Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/data/Data;->update()Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/data/IconData;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->simTypeInOutData:Lcom/android/systemui/newstatusbar/data/IconData;

    new-instance v0, Lcom/android/systemui/newstatusbar/data/TextData;

    const-string v2, "mobile_type"

    invoke-direct {v0, p1, v2}, Lcom/android/systemui/newstatusbar/data/TextData;-><init>(Landroid/content/Context;Ljava/lang/String;)V

    new-array v1, v1, [Ljava/lang/String;

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/data/TextData;->addKeys([Ljava/lang/String;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    new-instance v1, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController$5;

    invoke-direct {v1, p0}, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController$5;-><init>(Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;)V

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/data/Data;->addListener(Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/data/Data;->update()Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/data/TextData;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->simTypeData:Lcom/android/systemui/newstatusbar/data/TextData;

    return-void
.end method

.method static synthetic access$000(Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;)V
    .registers 1

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->updateSimData()V

    return-void
.end method

.method static synthetic access$100(Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;)Ljava/util/ArrayList;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->simCallBacks:Ljava/util/ArrayList;

    return-object v0
.end method

.method static synthetic access$200(Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;)Ljava/util/ArrayList;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->wifiCallBacks:Ljava/util/ArrayList;

    return-object v0
.end method

.method static synthetic access$300(Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;)Ljava/util/ArrayList;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->wifiInOutCallBacks:Ljava/util/ArrayList;

    return-object v0
.end method

.method static synthetic access$400(Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;)Ljava/util/ArrayList;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->simTypeInOutCallBacks:Ljava/util/ArrayList;

    return-object v0
.end method

.method static synthetic access$500(Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;)Ljava/util/ArrayList;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->simTypeCallBacks:Ljava/util/ArrayList;

    return-object v0
.end method

.method private updateSimData()V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->simData:Lcom/android/systemui/newstatusbar/data/IconData;

    const-string v1, "sim_one_color"

    invoke-static {v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v1

    iput v1, v0, Lcom/android/systemui/newstatusbar/data/IconData;->color:I

    const-string v1, "sim_two_color"

    invoke-static {v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v1

    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    iput-object v1, v0, Lcom/android/systemui/newstatusbar/data/IconData;->additional:Ljava/lang/Object;

    return-void
.end method


# virtual methods
.method public addCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V
    .registers 3

    instance-of v0, p1, Lcom/android/systemui/newstatusbar/sim/SimIcon;

    if-eqz v0, :cond_a

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->simCallBacks:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_35

    :cond_a
    instance-of v0, p1, Lcom/android/systemui/newstatusbar/views/WifiView;

    if-eqz v0, :cond_14

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->wifiCallBacks:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_35

    :cond_14
    instance-of v0, p1, Lcom/android/systemui/newstatusbar/sim/SimInOutView;

    if-eqz v0, :cond_1e

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->simTypeInOutCallBacks:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_35

    :cond_1e
    instance-of v0, p1, Lcom/android/systemui/newstatusbar/views/WifiInOutView;

    if-eqz v0, :cond_28

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->wifiInOutCallBacks:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_35

    :cond_28
    instance-of v0, p1, Lcom/android/systemui/newstatusbar/sim/SimTypeView;

    if-nez v0, :cond_30

    instance-of v0, p1, Lcom/android/systemui/newstatusbar/sim/MobileTypeImageView;

    if-eqz v0, :cond_35

    :cond_30
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->simTypeCallBacks:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    :cond_35
    :goto_35
    new-instance v0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController$6;

    invoke-direct {v0, p0, p1}, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController$6;-><init>(Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V

    invoke-interface {p1, v0}, Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;->post(Ljava/lang/Runnable;)Z

    return-void
.end method

.method public bridge synthetic addCallBack(Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;)V
    .registers 2

    check-cast p1, Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;

    invoke-virtual {p0, p1}, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->addCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V

    return-void
.end method

.method public getSimData()Lcom/android/systemui/newstatusbar/data/IconData;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->simData:Lcom/android/systemui/newstatusbar/data/IconData;

    return-object v0
.end method

.method public getSimTypeData()Lcom/android/systemui/newstatusbar/data/TextData;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->simTypeData:Lcom/android/systemui/newstatusbar/data/TextData;

    return-object v0
.end method

.method public getSimTypeInOutData()Lcom/android/systemui/newstatusbar/data/IconData;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->simTypeInOutData:Lcom/android/systemui/newstatusbar/data/IconData;

    return-object v0
.end method

.method public getWifiData()Lcom/android/systemui/newstatusbar/data/IconData;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->wifiData:Lcom/android/systemui/newstatusbar/data/IconData;

    return-object v0
.end method

.method public getWifiInOutData()Lcom/android/systemui/newstatusbar/data/IconData;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->wifiInOutData:Lcom/android/systemui/newstatusbar/data/IconData;

    return-object v0
.end method

.method public onDataChanged(Ljava/lang/String;)V
    .registers 2

    return-void
.end method

.method public removeCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V
    .registers 3

    instance-of v0, p1, Lcom/android/systemui/newstatusbar/sim/SimIcon;

    if-eqz v0, :cond_a

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->simCallBacks:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    goto :goto_31

    :cond_a
    instance-of v0, p1, Lcom/android/systemui/newstatusbar/views/WifiView;

    if-eqz v0, :cond_14

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->wifiCallBacks:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    goto :goto_31

    :cond_14
    instance-of v0, p1, Lcom/android/systemui/newstatusbar/sim/SimInOutView;

    if-eqz v0, :cond_1e

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->simTypeInOutCallBacks:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    goto :goto_31

    :cond_1e
    instance-of v0, p1, Lcom/android/systemui/newstatusbar/views/WifiInOutView;

    if-eqz v0, :cond_28

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->wifiInOutCallBacks:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    goto :goto_31

    :cond_28
    instance-of v0, p1, Lcom/android/systemui/newstatusbar/sim/SimTypeView;

    if-eqz v0, :cond_31

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->simTypeCallBacks:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    :cond_31
    :goto_31
    return-void
.end method

.method public bridge synthetic removeCallBack(Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;)V
    .registers 2

    check-cast p1, Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;

    invoke-virtual {p0, p1}, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->removeCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_controllers_MobileIconColorSizeController',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
