"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/controllers/ElementController.smali'
CLASS_FALLBACK_NAMES = ['ElementController.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/controllers/ElementController;
.super Lcom/android/systemui/plugins/controllers/ControllerExt;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/android/systemui/newstatusbar/controllers/ElementController$NotCalculateHoleInLine;,
        Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;,
        Lcom/android/systemui/newstatusbar/controllers/ElementController$CenterElementPosition;,
        Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;,
        Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;,
        Lcom/android/systemui/newstatusbar/controllers/ElementController$CallBack;
    }
.end annotation

.annotation system Ldalvik/annotation/Signature;
    value = {
        "Lcom/android/systemui/plugins/controllers/ControllerExt",
        "<",
        "Lcom/android/systemui/newstatusbar/controllers/ElementController$CallBack;",
        ">;"
    }
.end annotation


# instance fields
.field public centerElementPosition:Lcom/android/systemui/newstatusbar/controllers/ElementController$CenterElementPosition;

.field private darkChangeCount:I

.field public horizontalPaddingForCorners:I

.field public isDrip:Z

.field public isHole:Z

.field public isPromptVisible:Z

.field public final islandController:Lcom/android/systemui/newstatusbar/controllers/IslandController;

.field private lastTimeDarkChange:J

.field public leftElementPosition:Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;

.field public leftWidthToCamera:I

.field public mCameraWidth:I

.field public mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

.field public notCalculateHoleInLine:Lcom/android/systemui/newstatusbar/controllers/ElementController$NotCalculateHoleInLine;

.field private final notificationIconContainers:Ljava/util/ArrayList;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/ArrayList",
            "<",
            "Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;",
            ">;"
        }
    .end annotation
.end field

.field private notificationShadeWindowControllerImpl:Lcom/android/systemui/shade/NotificationShadeWindowControllerImpl;

.field private final records:Ljava/util/ArrayList;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/ArrayList",
            "<",
            "Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;",
            ">;"
        }
    .end annotation
.end field

.field private final sKeyAirModeChange:Ljava/lang/String;

.field private final sKeyCenterElemEnableInIsland:Ljava/lang/String;

.field private final sKeyElementPositionChange:Ljava/lang/String;

.field private final sKeysCutout:[Ljava/lang/String;

.field private final sKeysVisibleElement:[Ljava/lang/String;

.field public statusBarHeight:I


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 10

    const/4 v7, 0x4

    const/4 v6, 0x3

    const/4 v5, 0x2

    const/4 v4, 0x1

    const/4 v3, 0x0

    invoke-direct {p0, p1}, Lcom/android/systemui/plugins/controllers/ControllerExt;-><init>(Landroid/content/Context;)V

    iput v3, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->darkChangeCount:I

    const/4 v0, 0x7

    new-array v0, v0, [Ljava/lang/String;

    const-string v1, "status_bar_element_cutout_padding"

    aput-object v1, v0, v3

    const-string v1, "status_bar_element_cutout_type"

    aput-object v1, v0, v4

    const-string v1, "status_bar_element_cutout_camera_width"

    aput-object v1, v0, v5

    const-string v1, "status_bar_element_cutout_center"

    aput-object v1, v0, v6

    const-string v1, "status_bar_element_cutout_left"

    aput-object v1, v0, v7

    const/4 v1, 0x5

    const-string v2, "status_bar_element_cutout_padding_left_camera"

    aput-object v2, v0, v1

    const/4 v1, 0x6

    const-string v2, "status_bar_element_cutout_left_not_calculate"

    aput-object v2, v0, v1

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->sKeysCutout:[Ljava/lang/String;

    const/16 v0, 0xb

    new-array v0, v0, [Ljava/lang/String;

    const-string v1, "elem_status_element_visible"

    aput-object v1, v0, v3

    const-string v1, "elem_clock_element_visible"

    aput-object v1, v0, v4

    const-string v1, "elem_bat_element_visible"

    aput-object v1, v0, v5

    const-string v1, "elem_net1_element_visible"

    aput-object v1, v0, v6

    const-string v1, "elem_net2_element_visible"

    aput-object v1, v0, v7

    const/4 v1, 0x5

    const-string v2, "elem_wifi_element_visible"

    aput-object v2, v0, v1

    const/4 v1, 0x6

    const-string v2, "elem_notif_element_visible"

    aput-object v2, v0, v1

    const/4 v1, 0x7

    const-string v2, "elem_speed_element_visible"

    aput-object v2, v0, v1

    const/16 v1, 0x8

    const-string v2, "elem_weather_element_visible"

    aput-object v2, v0, v1

    const/16 v1, 0x9

    const-string v2, "elem_date_element_visible"

    aput-object v2, v0, v1

    const/16 v1, 0xa

    const-string v2, "elem_prompt_element_visible"

    aput-object v2, v0, v1

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->sKeysVisibleElement:[Ljava/lang/String;

    const-string v0, "air_mode_change"

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->sKeyAirModeChange:Ljava/lang/String;

    const-string v0, "status_bar_elem_position"

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->sKeyElementPositionChange:Ljava/lang/String;

    const-string v0, "status_bar_elem_center_in_island"

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->sKeyCenterElemEnableInIsland:Ljava/lang/String;

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/IslandController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/IslandController;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->islandController:Lcom/android/systemui/newstatusbar/controllers/IslandController;

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->notificationIconContainers:Ljava/util/ArrayList;

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->records:Ljava/util/ArrayList;

    new-instance v0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->sKeysCutout:[Ljava/lang/String;

    invoke-direct {v0, p0, v1}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;-><init>(Lcom/android/systemui/plugins/controllers/ControllerExt;[Ljava/lang/String;)V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->sKeysVisibleElement:[Ljava/lang/String;

    invoke-virtual {v0, v1}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->addKeys([Ljava/lang/String;)Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    move-result-object v0

    new-array v1, v6, [Ljava/lang/String;

    const-string v2, "air_mode_change"

    aput-object v2, v1, v3

    const-string v2, "status_bar_elem_position"

    aput-object v2, v1, v4

    const-string v2, "status_bar_elem_center_in_island"

    aput-object v2, v1, v5

    invoke-virtual {v0, v1}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->addKeys([Ljava/lang/String;)Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    return-void
.end method

.method private fullUpdate()V
    .registers 4

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->records:Ljava/util/ArrayList;

    invoke-virtual {v1}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :goto_6
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    if-eqz v2, :cond_18

    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;

    iget-object v2, v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    invoke-virtual {v2}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->fullUpdate()V

    goto :goto_6

    :cond_18
    return-void
.end method

.method private getMainLayout(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)Lcom/android/systemui/newstatusbar/layouts/MainLayout;
    .registers 5

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->records:Ljava/util/ArrayList;

    invoke-virtual {v1}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :cond_6
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    if-eqz v2, :cond_19

    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;

    iget-object v2, v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;->slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    if-ne v2, p1, :cond_6

    iget-object v1, v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    :goto_18
    return-object v1

    :cond_19
    const/4 v1, 0x0

    goto :goto_18
.end method

.method private updateAirMode()V
    .registers 4

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->records:Ljava/util/ArrayList;

    invoke-virtual {v1}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :goto_6
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    if-eqz v2, :cond_18

    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;

    iget-object v2, v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    invoke-virtual {v2}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->updateAirMode()V

    goto :goto_6

    :cond_18
    return-void
.end method

.method private updateAlgoritm()V
    .registers 4

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->records:Ljava/util/ArrayList;

    invoke-virtual {v1}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :goto_6
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    if-eqz v2, :cond_18

    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;

    iget-object v2, v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    invoke-virtual {v2}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->updateAlgoritm()V

    goto :goto_6

    :cond_18
    return-void
.end method

.method private updateElementVisibility()V
    .registers 4

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->records:Ljava/util/ArrayList;

    invoke-virtual {v1}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :goto_6
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    if-eqz v2, :cond_18

    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;

    iget-object v2, v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    invoke-virtual {v2}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->updateElementVisibility()V

    goto :goto_6

    :cond_18
    return-void
.end method


# virtual methods
.method public clearNetSpeed()V
    .registers 4

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->records:Ljava/util/ArrayList;

    invoke-virtual {v1}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :goto_6
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    if-eqz v2, :cond_1c

    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;

    iget-object v2, v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;->slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    invoke-virtual {p0, v2}, Lcom/android/systemui/newstatusbar/controllers/ElementController;->getNetSpeedGroup(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)Landroid/view/ViewGroup;

    move-result-object v2

    invoke-virtual {v2}, Landroid/view/ViewGroup;->removeAllViews()V

    goto :goto_6

    :cond_1c
    return-void
.end method

.method public clearSim1()V
    .registers 4

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->records:Ljava/util/ArrayList;

    invoke-virtual {v1}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :goto_6
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    if-eqz v2, :cond_1c

    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;

    iget-object v2, v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;->slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    invoke-virtual {p0, v2}, Lcom/android/systemui/newstatusbar/controllers/ElementController;->getSim1Group(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)Landroid/view/ViewGroup;

    move-result-object v2

    invoke-virtual {v2}, Landroid/view/ViewGroup;->removeAllViews()V

    goto :goto_6

    :cond_1c
    return-void
.end method

.method public clearSim2()V
    .registers 4

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->records:Ljava/util/ArrayList;

    invoke-virtual {v1}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :goto_6
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    if-eqz v2, :cond_1c

    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;

    iget-object v2, v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;->slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    invoke-virtual {p0, v2}, Lcom/android/systemui/newstatusbar/controllers/ElementController;->getSim2Group(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)Landroid/view/ViewGroup;

    move-result-object v2

    invoke-virtual {v2}, Landroid/view/ViewGroup;->removeAllViews()V

    goto :goto_6

    :cond_1c
    return-void
.end method

.method public clearWiFi()V
    .registers 4

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->records:Ljava/util/ArrayList;

    invoke-virtual {v1}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :goto_6
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    if-eqz v2, :cond_1c

    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;

    iget-object v2, v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;->slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    invoke-virtual {p0, v2}, Lcom/android/systemui/newstatusbar/controllers/ElementController;->getWiFiGroup(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)Landroid/view/ViewGroup;

    move-result-object v2

    invoke-virtual {v2}, Landroid/view/ViewGroup;->removeAllViews()V

    goto :goto_6

    :cond_1c
    return-void
.end method

.method public getDispather(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;Lcom/android/systemui/newstatusbar/policy/ISlots;)Lcom/android/systemui/plugins/DarkIconDispatcher;
    .registers 6

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->records:Ljava/util/ArrayList;

    invoke-virtual {v1}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :cond_6
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    if-eqz v2, :cond_22

    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;

    iget-object v2, v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;->slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    if-ne v2, p1, :cond_6

    iget-object v1, v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;->dispatcher:Lcom/android/systemui/plugins/DarkIconDispatcher;

    if-nez v1, :cond_1f

    iget-object v1, v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;->dispatchers:Ljava/util/ArrayList;

    invoke-virtual {v1, p2}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    :cond_1f
    iget-object v1, v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;->dispatcher:Lcom/android/systemui/plugins/DarkIconDispatcher;

    :goto_21
    return-object v1

    :cond_22
    const/4 v1, 0x0

    goto :goto_21
.end method

.method public getNetSpeedGroup(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)Landroid/view/ViewGroup;
    .registers 4

    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/controllers/ElementController;->getMainLayout(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    move-result-object v0

    if-nez v0, :cond_8

    const/4 v1, 0x0

    :goto_7
    return-object v1

    :cond_8
    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getSpeedLayout()Landroid/view/ViewGroup;

    move-result-object v1

    goto :goto_7
.end method

.method public getSim1Group(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)Landroid/view/ViewGroup;
    .registers 4

    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/controllers/ElementController;->getMainLayout(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    move-result-object v0

    if-nez v0, :cond_8

    const/4 v1, 0x0

    :goto_7
    return-object v1

    :cond_8
    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getSim1Layout()Landroid/view/ViewGroup;

    move-result-object v1

    goto :goto_7
.end method

.method public getSim2Group(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)Landroid/view/ViewGroup;
    .registers 4

    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/controllers/ElementController;->getMainLayout(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    move-result-object v0

    if-nez v0, :cond_8

    const/4 v1, 0x0

    :goto_7
    return-object v1

    :cond_8
    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getSim2Layout()Landroid/view/ViewGroup;

    move-result-object v1

    goto :goto_7
.end method

.method public getWiFiGroup(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)Landroid/view/ViewGroup;
    .registers 4

    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/controllers/ElementController;->getMainLayout(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    move-result-object v0

    if-nez v0, :cond_8

    const/4 v1, 0x0

    :goto_7
    return-object v1

    :cond_8
    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getWiFiLayout()Landroid/view/ViewGroup;

    move-result-object v1

    goto :goto_7
.end method

.method public onManagerCreated(Lcom/android/systemui/plugins/DarkIconDispatcher;Lcom/android/systemui/statusbar/phone/StatusBarLocation;)V
    .registers 6

    sget-object v0, Lcom/android/systemui/statusbar/phone/StatusBarLocation;->HOME:Lcom/android/systemui/statusbar/phone/StatusBarLocation;

    if-ne p2, v0, :cond_1f

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->records:Ljava/util/ArrayList;

    invoke-virtual {v0}, Ljava/util/ArrayList;->size()I

    move-result v0

    if-lez v0, :cond_1f

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->records:Ljava/util/ArrayList;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->records:Ljava/util/ArrayList;

    invoke-virtual {v1}, Ljava/util/ArrayList;->size()I

    move-result v1

    add-int/lit8 v1, v1, -0x1

    invoke-virtual {v0, v1}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;

    invoke-virtual {v0, p1}, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;->setDispatcher(Lcom/android/systemui/plugins/DarkIconDispatcher;)V

    :cond_1f
    sget-object v0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->TAG:Ljava/lang/String;

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "onManagerCreated: "

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {p1}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/Class;->getName()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-static {v0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    return-void
.end method

.method public onSettingsChange(Ljava/lang/String;)V
    .registers 3

    const-string v0, "status_bar_elem_position"

    invoke-virtual {v0, p1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-eqz v0, :cond_c

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/ElementController;->fullUpdate()V

    :cond_b
    :goto_b
    return-void

    :cond_c
    const-string v0, "air_mode_change"

    invoke-virtual {v0, p1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-eqz v0, :cond_18

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/ElementController;->updateAirMode()V

    goto :goto_b

    :cond_18
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->sKeysVisibleElement:[Ljava/lang/String;

    invoke-static {v0}, Ljava/util/Arrays;->asList([Ljava/lang/Object;)Ljava/util/List;

    move-result-object v0

    invoke-interface {v0, p1}, Ljava/util/List;->contains(Ljava/lang/Object;)Z

    move-result v0

    if-eqz v0, :cond_28

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/ElementController;->updateElementVisibility()V

    goto :goto_b

    :cond_28
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->sKeysCutout:[Ljava/lang/String;

    invoke-static {v0}, Ljava/util/Arrays;->asList([Ljava/lang/Object;)Ljava/util/List;

    move-result-object v0

    invoke-interface {v0, p1}, Ljava/util/List;->contains(Ljava/lang/Object;)Z

    move-result v0

    if-nez v0, :cond_3c

    const-string v0, "status_bar_elem_center_in_island"

    invoke-virtual {v0, p1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-eqz v0, :cond_b

    :cond_3c
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/controllers/ElementController;->updateCutoutType()V

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/ElementController;->updateAlgoritm()V

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/ElementController;->fullUpdate()V

    goto :goto_b
.end method

.method public setMainLayout(Lcom/android/systemui/newstatusbar/layouts/MainLayout;)V
    .registers 5

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->records:Ljava/util/ArrayList;

    invoke-virtual {v0}, Ljava/util/ArrayList;->size()I

    move-result v0

    const/4 v1, 0x2

    if-ne v0, v1, :cond_15

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->records:Ljava/util/ArrayList;

    invoke-virtual {v0}, Ljava/util/ArrayList;->clear()V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->islandController:Lcom/android/systemui/newstatusbar/controllers/IslandController;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/controllers/IslandController;->clearCallbaks()V

    :cond_15
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->records:Ljava/util/ArrayList;

    new-instance v2, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->records:Ljava/util/ArrayList;

    invoke-virtual {v0}, Ljava/util/ArrayList;->size()I

    move-result v0

    if-lez v0, :cond_2a

    sget-object v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;->slotB:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    :goto_23
    invoke-direct {v2, p1, v0}, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;-><init>(Lcom/android/systemui/newstatusbar/layouts/MainLayout;Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)V

    invoke-virtual {v1, v2}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    return-void

    :cond_2a
    sget-object v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;->slotA:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    goto :goto_23
.end method

.method public setNotificationIconContainer(Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;)V
    .registers 4

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->notificationIconContainers:Ljava/util/ArrayList;

    invoke-virtual {v0}, Ljava/util/ArrayList;->size()I

    move-result v0

    const/4 v1, 0x2

    if-ne v0, v1, :cond_e

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->notificationIconContainers:Ljava/util/ArrayList;

    invoke-virtual {v0}, Ljava/util/ArrayList;->clear()V

    :cond_e
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->notificationIconContainers:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    return-void
.end method

.method public updateCutoutType()V
    .registers 6

    const/4 v3, 0x0

    const/4 v4, 0x2

    const/4 v2, 0x1

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->sKeysCutout:[Ljava/lang/String;

    aget-object v1, v1, v2

    invoke-static {v1, v2}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v0

    if-ne v0, v2, :cond_6f

    move v1, v2

    :goto_e
    iput-boolean v1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->isDrip:Z

    if-ne v0, v4, :cond_71

    :goto_12
    iput-boolean v2, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->isHole:Z

    if-lez v0, :cond_73

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->sKeysCutout:[Ljava/lang/String;

    aget-object v1, v1, v4

    const/16 v2, 0x1e

    invoke-static {v1, v2}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v1

    :goto_20
    iput v1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->mCameraWidth:I

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->sKeysCutout:[Ljava/lang/String;

    aget-object v1, v1, v3

    const/16 v2, 0x19

    invoke-static {v1, v2}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v1

    iput v1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->horizontalPaddingForCorners:I

    invoke-static {}, Lcom/android/systemui/newstatusbar/controllers/ElementController$CenterElementPosition;->values()[Lcom/android/systemui/newstatusbar/controllers/ElementController$CenterElementPosition;

    move-result-object v1

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->sKeysCutout:[Ljava/lang/String;

    const/4 v3, 0x3

    aget-object v2, v2, v3

    invoke-static {v2, v4}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v2

    aget-object v1, v1, v2

    iput-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->centerElementPosition:Lcom/android/systemui/newstatusbar/controllers/ElementController$CenterElementPosition;

    invoke-static {}, Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;->values()[Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;

    move-result-object v1

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->sKeysCutout:[Ljava/lang/String;

    const/4 v3, 0x4

    aget-object v2, v2, v3

    invoke-static {v2, v4}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v2

    aget-object v1, v1, v2

    iput-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->leftElementPosition:Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->sKeysCutout:[Ljava/lang/String;

    const/4 v2, 0x5

    aget-object v1, v1, v2

    const/16 v2, 0x4b

    invoke-static {v1, v2}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v1

    iput v1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->leftWidthToCamera:I

    invoke-static {}, Lcom/android/systemui/newstatusbar/controllers/ElementController$NotCalculateHoleInLine;->values()[Lcom/android/systemui/newstatusbar/controllers/ElementController$NotCalculateHoleInLine;

    move-result-object v1

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->sKeysCutout:[Ljava/lang/String;

    const/4 v3, 0x6

    aget-object v2, v2, v3

    invoke-static {v2, v4}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v2

    aget-object v1, v1, v2

    iput-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->notCalculateHoleInLine:Lcom/android/systemui/newstatusbar/controllers/ElementController$NotCalculateHoleInLine;

    return-void

    :cond_6f
    move v1, v3

    goto :goto_e

    :cond_71
    move v2, v3

    goto :goto_12

    :cond_73
    move v1, v3

    goto :goto_20
.end method

.method public updateHeight(I)V
    .registers 5

    iput p1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->statusBarHeight:I

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->isDoubleStatusBar()Z

    move-result v1

    if-eqz v1, :cond_10

    iget v1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->statusBarHeight:I

    div-int/lit8 v1, v1, 0x2

    iput v1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->statusBarHeight:I

    :cond_10
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->notificationIconContainers:Ljava/util/ArrayList;

    invoke-virtual {v1}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :cond_16
    :goto_16
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    if-eqz v2, :cond_28

    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;

    if-eqz v0, :cond_16

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->initDimens()V

    goto :goto_16

    :cond_28
    return-void
.end method

.method public updateMainLayouts()V
    .registers 4

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->records:Ljava/util/ArrayList;

    invoke-virtual {v1}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :goto_6
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    if-eqz v2, :cond_18

    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;

    iget-object v2, v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    invoke-virtual {v2}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->updateMainLayout()V

    goto :goto_6

    :cond_18
    return-void
.end method

.method public updateShowNetworkSpeed(Z)V
    .registers 2

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_controllers_ElementController',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
