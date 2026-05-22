"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/controllers/SimTypeController.smali'
CLASS_FALLBACK_NAMES = ['SimTypeController.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/controllers/SimTypeController;
.super Lcom/android/systemui/plugins/controllers/ControllerExt;

# interfaces
.implements Landroid/preference/CustomUpdater$CustomReceiver;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/android/systemui/newstatusbar/controllers/SimTypeController$CallBack;
    }
.end annotation

.annotation system Ldalvik/annotation/Signature;
    value = {
        "Lcom/android/systemui/plugins/controllers/ControllerExt<",
        "Lcom/android/systemui/newstatusbar/controllers/SimTypeController$CallBack;",
        ">;",
        "Landroid/preference/CustomUpdater$CustomReceiver;"
    }
.end annotation


# static fields
.field private static instance:Lcom/android/systemui/newstatusbar/controllers/SimTypeController; = null

.field private static final key:Ljava/lang/String; = "sim_type_style"


# instance fields
.field private isCustomSimType:Z


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 4

    invoke-direct {p0, p1}, Lcom/android/systemui/plugins/controllers/ControllerExt;-><init>(Landroid/content/Context;)V

    sput-object p0, Lcom/android/systemui/newstatusbar/controllers/SimTypeController;->instance:Lcom/android/systemui/newstatusbar/controllers/SimTypeController;

    invoke-static {}, Landroid/preference/CustomUpdater;->getInstance()Landroid/preference/CustomUpdater;

    move-result-object v0

    const-string v1, "sim_type_style"

    invoke-virtual {v0, p0, v1}, Landroid/preference/CustomUpdater;->addCustomReceiver(Landroid/preference/CustomUpdater$CustomReceiver;Ljava/lang/String;)V

    invoke-static {v1}, Landroid/preference/SettingsMezoHelper;->getBoolofSettings(Ljava/lang/String;)Z

    move-result v0

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/controllers/SimTypeController;->isCustomSimType:Z

    return-void
.end method

.method public static getInstance()Lcom/android/systemui/newstatusbar/controllers/SimTypeController;
    .registers 2

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/SimTypeController;

    monitor-enter v0

    :try_start_3
    sget-object v1, Lcom/android/systemui/newstatusbar/controllers/SimTypeController;->instance:Lcom/android/systemui/newstatusbar/controllers/SimTypeController;

    monitor-exit v0

    return-object v1

    :catchall_7
    move-exception v1

    monitor-exit v0
    :try_end_9
    .catchall {:try_start_3 .. :try_end_9} :catchall_7

    throw v1
.end method

.method private update()V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/SimTypeController;->callBacks:Ljava/util/ArrayList;

    invoke-virtual {v0}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_6
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_16

    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/systemui/newstatusbar/controllers/SimTypeController$CallBack;

    invoke-interface {v1}, Lcom/android/systemui/newstatusbar/controllers/SimTypeController$CallBack;->onSimTypeChange()V

    goto :goto_6

    :cond_16
    return-void
.end method


# virtual methods
.method public isCustomSimType()Z
    .registers 2

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/controllers/SimTypeController;->isCustomSimType:Z

    return v0
.end method

.method public onCustomChanged(Ljava/lang/String;)V
    .registers 4

    const-string v0, "sim_type_style"

    invoke-virtual {v0, p1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_11

    invoke-static {v0}, Landroid/preference/SettingsMezoHelper;->getBoolofSettings1(Ljava/lang/String;)Z

    move-result v0

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/controllers/SimTypeController;->isCustomSimType:Z

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/SimTypeController;->update()V

    :cond_11
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_controllers_SimTypeController',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
