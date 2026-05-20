"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/controllers/StatusBarIconViewController.smali'
CLASS_FALLBACK_NAMES = ['StatusBarIconViewController.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;
.super Lcom/android/systemui/newstatusbar/controllers/IconController;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController$NotificationIconData;
    }
.end annotation


# instance fields
.field private final currNotificationData:Lcom/android/systemui/newstatusbar/data/IconData;

.field private final currStatusData:Lcom/android/systemui/newstatusbar/data/IconData;

.field private final notificationIcons:Ljava/util/ArrayList;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/ArrayList<",
            "Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;",
            ">;"
        }
    .end annotation
.end field

.field private final statusIcons:Ljava/util/ArrayList;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/ArrayList<",
            "Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;",
            ">;"
        }
    .end annotation
.end field


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 5

    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/controllers/IconController;-><init>(Landroid/content/Context;)V

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;->notificationIcons:Ljava/util/ArrayList;

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;->statusIcons:Ljava/util/ArrayList;

    new-instance v0, Lcom/android/systemui/newstatusbar/data/IconData;

    const-string v1, "status_icon"

    invoke-direct {v0, p1, v1}, Lcom/android/systemui/newstatusbar/data/IconData;-><init>(Landroid/content/Context;Ljava/lang/String;)V

    const/4 v1, 0x0

    new-array v2, v1, [Ljava/lang/String;

    invoke-virtual {v0, v2}, Lcom/android/systemui/newstatusbar/data/IconData;->addKeys([Ljava/lang/String;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    new-instance v2, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController$1;

    invoke-direct {v2, p0}, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController$1;-><init>(Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;)V

    invoke-virtual {v0, v2}, Lcom/android/systemui/newstatusbar/data/Data;->addListener(Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/data/Data;->update()Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/data/IconData;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;->currStatusData:Lcom/android/systemui/newstatusbar/data/IconData;

    new-instance v0, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController$NotificationIconData;

    const-string v2, "notif_icon"

    invoke-direct {v0, p1, v2}, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController$NotificationIconData;-><init>(Landroid/content/Context;Ljava/lang/String;)V

    new-array v1, v1, [Ljava/lang/String;

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController$NotificationIconData;->addKeys([Ljava/lang/String;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    new-instance v1, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController$2;

    invoke-direct {v1, p0}, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController$2;-><init>(Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;)V

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/data/Data;->addListener(Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/data/Data;->update()Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/data/IconData;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;->currNotificationData:Lcom/android/systemui/newstatusbar/data/IconData;

    return-void
.end method

.method static synthetic access$000(Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;)Ljava/util/ArrayList;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;->statusIcons:Ljava/util/ArrayList;

    return-object v0
.end method

.method static synthetic access$100(Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;)Ljava/util/ArrayList;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;->notificationIcons:Ljava/util/ArrayList;

    return-object v0
.end method


# virtual methods
.method public addCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V
    .registers 2

    return-void
.end method

.method public addCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;Z)V
    .registers 4

    if-eqz p2, :cond_5

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;->statusIcons:Ljava/util/ArrayList;

    goto :goto_7

    :cond_5
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;->notificationIcons:Ljava/util/ArrayList;

    :goto_7
    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    return-void
.end method

.method public bridge synthetic addCallBack(Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;)V
    .registers 2

    check-cast p1, Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;

    invoke-virtual {p0, p1}, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;->addCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V

    return-void
.end method

.method public getCurrData(Z)Lcom/android/systemui/newstatusbar/data/IconData;
    .registers 3

    if-eqz p1, :cond_5

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;->currStatusData:Lcom/android/systemui/newstatusbar/data/IconData;

    goto :goto_7

    :cond_5
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;->currNotificationData:Lcom/android/systemui/newstatusbar/data/IconData;

    :goto_7
    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/data/IconData;->copy()Lcom/android/systemui/newstatusbar/data/IconData;

    move-result-object v0

    return-object v0
.end method

.method public isStatusIcon(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)Z
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;->statusIcons:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->contains(Ljava/lang/Object;)Z

    move-result v0

    return v0
.end method

.method public onCustomChanged(Ljava/lang/String;)V
    .registers 2

    return-void
.end method

.method public removeCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V
    .registers 2

    return-void
.end method

.method public removeCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;Z)V
    .registers 4

    if-eqz p2, :cond_5

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;->statusIcons:Ljava/util/ArrayList;

    goto :goto_7

    :cond_5
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;->notificationIcons:Ljava/util/ArrayList;

    :goto_7
    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    return-void
.end method

.method public bridge synthetic removeCallBack(Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;)V
    .registers 2

    check-cast p1, Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;

    invoke-virtual {p0, p1}, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;->removeCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_controllers_StatusBarIconViewController',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
