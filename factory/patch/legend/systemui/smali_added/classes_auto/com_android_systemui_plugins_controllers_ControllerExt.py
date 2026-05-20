"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/plugins/controllers/ControllerExt.smali'
CLASS_FALLBACK_NAMES = ['ControllerExt.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/plugins/controllers/ControllerExt;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;,
        Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;
    }
.end annotation

.annotation system Ldalvik/annotation/Signature;
    value = {
        "<Cl::",
        "Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;",
        ">",
        "Ljava/lang/Object;"
    }
.end annotation


# instance fields
.field protected final callBacks:Ljava/util/ArrayList;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/ArrayList",
            "<TCl;>;"
        }
    .end annotation
.end field

.field protected context:Landroid/content/Context;


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 3

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/plugins/controllers/ControllerExt;->callBacks:Ljava/util/ArrayList;

    iput-object p1, p0, Lcom/android/systemui/plugins/controllers/ControllerExt;->context:Landroid/content/Context;

    return-void
.end method


# virtual methods
.method public addCallBack(Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;)V
    .registers 4
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(TCl;)V"
        }
    .end annotation

    iget-object v1, p0, Lcom/android/systemui/plugins/controllers/ControllerExt;->callBacks:Ljava/util/ArrayList;

    monitor-enter v1

    :try_start_3
    iget-object v0, p0, Lcom/android/systemui/plugins/controllers/ControllerExt;->callBacks:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    monitor-exit v1

    return-void

    :catchall_a
    move-exception v0

    monitor-exit v1
    :try_end_c
    .catchall {:try_start_3 .. :try_end_c} :catchall_a

    throw v0
.end method

.method public onSettingsChange()V
    .registers 1

    return-void
.end method

.method public onSettingsChange(Landroid/net/Uri;)V
    .registers 2

    return-void
.end method

.method public onSettingsChange(Ljava/lang/String;)V
    .registers 2

    return-void
.end method

.method public removeCallBack(Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;)V
    .registers 4
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(TCl;)V"
        }
    .end annotation

    iget-object v1, p0, Lcom/android/systemui/plugins/controllers/ControllerExt;->callBacks:Ljava/util/ArrayList;

    monitor-enter v1

    :try_start_3
    iget-object v0, p0, Lcom/android/systemui/plugins/controllers/ControllerExt;->callBacks:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    monitor-exit v1

    return-void

    :catchall_a
    move-exception v0

    monitor-exit v1
    :try_end_c
    .catchall {:try_start_3 .. :try_end_c} :catchall_a

    throw v0
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_plugins_controllers_ControllerExt',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
