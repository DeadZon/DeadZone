"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/statusbar/policy/MyKeyguardStateController.smali'
CLASS_FALLBACK_NAMES = ['MyKeyguardStateController.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;
.super Ljava/lang/Object;

# interfaces
.implements Lcom/android/systemui/statusbar/policy/ControllerExpandHeight$CallBack;
.implements Lcom/android/systemui/plugins/statusbar/StatusBarStateController$StateListener;
.implements Lcom/android/systemui/statusbar/policy/KeyguardStateController$Callback;
.implements Landroid/hardware/display/DisplayManager$DisplayListener;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/android/systemui/statusbar/policy/MyKeyguardStateController$CallBack;
    }
.end annotation


# static fields
.field public static final STATE_DOZE:I = 0x3

.field public static final STATE_DOZE_SUSPEND:I = 0x4

.field public static final STATE_OFF:I = 0x1

.field public static final STATE_ON:I = 0x2

.field public static final STATE_ON_SUSPEND:I = 0x6

.field public static final STATE_VR:I = 0x5

.field private static final TAG:Ljava/lang/String; = "MyKeyguardStateController"

.field private static final sMyKeyguardStateController:Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;
    .annotation build Landroid/annotation/SuppressLint;
        value = {
            "StaticFieldLeak"
        }
    .end annotation
.end field


# instance fields
.field private displayManager:Landroid/hardware/display/DisplayManager;

.field private isControlOpen:Z

.field private isExpandOpen:Z

.field private isOnKeyguard:Z

.field private final keyguardStateController:Lcom/android/systemui/statusbar/policy/KeyguardStateController;

.field private final mHandler:Landroid/os/Handler;
    .annotation build Landroid/annotation/SuppressLint;
        value = {
            "HandlerLeak"
        }
    .end annotation
.end field

.field private final mListener:Ljava/util/ArrayList;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/ArrayList",
            "<",
            "Lcom/android/systemui/statusbar/policy/MyKeyguardStateController$CallBack;",
            ">;"
        }
    .end annotation
.end field

.field private final mStatusBarStateController:Lcom/android/systemui/plugins/statusbar/StatusBarStateController;


# direct methods
.method static constructor <clinit>()V
    .registers 1

    new-instance v0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;

    invoke-direct {v0}, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;-><init>()V

    sput-object v0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->sMyKeyguardStateController:Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;

    return-void
.end method

.method public constructor <init>()V
    .registers 4

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    new-instance v1, Ljava/util/ArrayList;

    invoke-direct {v1}, Ljava/util/ArrayList;-><init>()V

    iput-object v1, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->mListener:Ljava/util/ArrayList;

    const/4 v1, 0x0

    iput-boolean v1, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->isOnKeyguard:Z

    new-instance v1, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController$1;

    invoke-direct {v1, p0}, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController$1;-><init>(Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;)V

    iput-object v1, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->mHandler:Landroid/os/Handler;

    const-class v1, Lcom/android/systemui/statusbar/policy/KeyguardStateController;

    invoke-static {v1}, Lcom/android/systemui/Dependency;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/systemui/statusbar/policy/KeyguardStateController;

    iput-object v1, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->keyguardStateController:Lcom/android/systemui/statusbar/policy/KeyguardStateController;

    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->keyguardStateController:Lcom/android/systemui/statusbar/policy/KeyguardStateController;

    invoke-interface {v1, p0}, Lcom/android/systemui/statusbar/policy/KeyguardStateController;->addCallback(Ljava/lang/Object;)V

    invoke-static {}, Landroid/preference/SettingsMezoHelper;->getCon()Landroid/content/Context;

    move-result-object v0

    if-eqz v0, :cond_3e

    const-string v1, "display"

    invoke-virtual {v0, v1}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Landroid/hardware/display/DisplayManager;

    iput-object v1, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->displayManager:Landroid/hardware/display/DisplayManager;

    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->displayManager:Landroid/hardware/display/DisplayManager;

    if-eqz v1, :cond_3e

    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->displayManager:Landroid/hardware/display/DisplayManager;

    iget-object v2, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->mHandler:Landroid/os/Handler;

    invoke-virtual {v1, p0, v2}, Landroid/hardware/display/DisplayManager;->registerDisplayListener(Landroid/hardware/display/DisplayManager$DisplayListener;Landroid/os/Handler;)V

    :cond_3e
    const-class v1, Lcom/android/systemui/plugins/statusbar/StatusBarStateController;

    invoke-static {v1}, Lcom/android/systemui/Dependency;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/systemui/plugins/statusbar/StatusBarStateController;

    iput-object v1, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->mStatusBarStateController:Lcom/android/systemui/plugins/statusbar/StatusBarStateController;

    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->mStatusBarStateController:Lcom/android/systemui/plugins/statusbar/StatusBarStateController;

    invoke-interface {v1, p0}, Lcom/android/systemui/plugins/statusbar/StatusBarStateController;->addCallback(Lcom/android/systemui/plugins/statusbar/StatusBarStateController$StateListener;)V

    invoke-static {}, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->getInstance()Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;

    move-result-object v1

    invoke-virtual {v1, p0}, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->addCallBack(Lcom/android/systemui/statusbar/policy/ControllerExpandHeight$CallBack;)V

    return-void
.end method

.method static synthetic access$000(Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;Z)V
    .registers 2

    invoke-direct {p0, p1}, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->updateInternal(Z)V

    return-void
.end method

.method public static declared-synchronized getInstance()Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;
    .registers 4

    const-class v2, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;

    monitor-enter v2

    :try_start_3
    const-class v3, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;

    monitor-enter v3
    :try_end_6
    .catchall {:try_start_3 .. :try_end_6} :catchall_e

    :try_start_6
    sget-object v0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->sMyKeyguardStateController:Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;

    monitor-exit v3
    :try_end_9
    .catchall {:try_start_6 .. :try_end_9} :catchall_b

    monitor-exit v2

    return-object v0

    :catchall_b
    move-exception v1

    :try_start_c
    monitor-exit v3
    :try_end_d
    .catchall {:try_start_c .. :try_end_d} :catchall_b

    :try_start_d
    throw v1
    :try_end_e
    .catchall {:try_start_d .. :try_end_e} :catchall_e

    :catchall_e
    move-exception v1

    monitor-exit v2

    throw v1
.end method

.method private isOnKeyguard()Z
    .registers 2

    iget-boolean v0, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->isControlOpen:Z

    if-nez v0, :cond_a

    iget-boolean v0, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->isExpandOpen:Z

    if-nez v0, :cond_a

    const/4 v0, 0x1

    :goto_9
    return v0

    :cond_a
    const/4 v0, 0x0

    goto :goto_9
.end method

.method private isScreenOn(I)Z
    .registers 3

    const/4 v0, 0x2

    if-ne p1, v0, :cond_5

    const/4 v0, 0x1

    :goto_4
    return v0

    :cond_5
    const/4 v0, 0x0

    goto :goto_4
.end method

.method private updateInternal(Z)V
    .registers 5

    iget-boolean v1, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->isOnKeyguard:Z

    if-eq v1, p1, :cond_1c

    iput-boolean p1, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->isOnKeyguard:Z

    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->mListener:Ljava/util/ArrayList;

    invoke-virtual {v1}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :goto_c
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    if-eqz v2, :cond_1c

    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController$CallBack;

    invoke-interface {v0, p1}, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController$CallBack;->onKeyguardStateChange(Z)V

    goto :goto_c

    :cond_1c
    return-void
.end method

.method private updateKeyguard(Z)V
    .registers 8

    const/16 v4, 0x65

    const/4 v1, 0x0

    iget-object v0, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->mHandler:Landroid/os/Handler;

    invoke-virtual {v0, v4}, Landroid/os/Handler;->removeMessages(I)V

    iget-object v2, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->mHandler:Landroid/os/Handler;

    iget-object v3, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->mHandler:Landroid/os/Handler;

    if-eqz p1, :cond_19

    const/4 v0, 0x1

    :goto_f
    invoke-virtual {v3, v4, v0, v1}, Landroid/os/Handler;->obtainMessage(III)Landroid/os/Message;

    move-result-object v0

    const-wide/16 v4, 0xc8

    invoke-virtual {v2, v0, v4, v5}, Landroid/os/Handler;->sendMessageDelayed(Landroid/os/Message;J)Z

    return-void

    :cond_19
    move v0, v1

    goto :goto_f
.end method

.method private updateScreenOn(Z)V
    .registers 5

    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->mListener:Ljava/util/ArrayList;

    invoke-virtual {v1}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :goto_6
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    if-eqz v2, :cond_16

    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController$CallBack;

    invoke-interface {v0, p1}, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController$CallBack;->onScreenOnStateChange(Z)V

    goto :goto_6

    :cond_16
    return-void
.end method


# virtual methods
.method public addCallBack(Lcom/android/systemui/statusbar/policy/MyKeyguardStateController$CallBack;)V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->mListener:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    return-void
.end method

.method public onControlHeightChange(Z)V
    .registers 2

    iput-boolean p1, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->isControlOpen:Z

    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->onKeyguardShowingChanged()V

    return-void
.end method

.method public onDisplayAdded(I)V
    .registers 2

    return-void
.end method

.method public onDisplayChanged(I)V
    .registers 8

    const/4 v4, 0x1

    const/4 v5, 0x0

    if-nez p1, :cond_2f

    iget-object v3, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->displayManager:Landroid/hardware/display/DisplayManager;

    invoke-virtual {v3, p1}, Landroid/hardware/display/DisplayManager;->getDisplay(I)Landroid/view/Display;

    move-result-object v3

    invoke-virtual {v3}, Landroid/view/Display;->getState()I

    move-result v3

    invoke-direct {p0, v3}, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->isScreenOn(I)Z

    move-result v2

    iget-object v3, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->keyguardStateController:Lcom/android/systemui/statusbar/policy/KeyguardStateController;

    invoke-interface {v3}, Lcom/android/systemui/statusbar/policy/KeyguardStateController;->isUnlocked()Z

    move-result v1

    iget-object v3, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->mStatusBarStateController:Lcom/android/systemui/plugins/statusbar/StatusBarStateController;

    invoke-interface {v3}, Lcom/android/systemui/plugins/statusbar/StatusBarStateController;->isDozing()Z

    move-result v0

    if-eqz v1, :cond_30

    if-eqz v2, :cond_30

    if-nez v0, :cond_30

    move v3, v4

    :goto_25
    invoke-direct {p0, v3}, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->updateKeyguard(Z)V

    if-eqz v2, :cond_32

    if-nez v0, :cond_32

    :goto_2c
    invoke-direct {p0, v4}, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->updateScreenOn(Z)V

    :cond_2f
    return-void

    :cond_30
    move v3, v5

    goto :goto_25

    :cond_32
    move v4, v5

    goto :goto_2c
.end method

.method public onDisplayRemoved(I)V
    .registers 2

    return-void
.end method

.method public onDozingChanged(Z)V
    .registers 7

    const/4 v3, 0x1

    const/4 v4, 0x0

    iget-object v2, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->displayManager:Landroid/hardware/display/DisplayManager;

    invoke-virtual {v2, v4}, Landroid/hardware/display/DisplayManager;->getDisplay(I)Landroid/view/Display;

    move-result-object v2

    invoke-virtual {v2}, Landroid/view/Display;->getState()I

    move-result v2

    invoke-direct {p0, v2}, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->isScreenOn(I)Z

    move-result v1

    iget-object v2, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->keyguardStateController:Lcom/android/systemui/statusbar/policy/KeyguardStateController;

    invoke-interface {v2}, Lcom/android/systemui/statusbar/policy/KeyguardStateController;->isUnlocked()Z

    move-result v0

    if-eqz v0, :cond_28

    if-eqz v1, :cond_28

    if-nez p1, :cond_28

    move v2, v3

    :goto_1d
    invoke-direct {p0, v2}, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->updateKeyguard(Z)V

    if-eqz v1, :cond_2a

    if-nez p1, :cond_2a

    :goto_24
    invoke-direct {p0, v3}, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->updateScreenOn(Z)V

    return-void

    :cond_28
    move v2, v4

    goto :goto_1d

    :cond_2a
    move v3, v4

    goto :goto_24
.end method

.method public onExpandHeightChange(Z)V
    .registers 2

    iput-boolean p1, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->isExpandOpen:Z

    invoke-virtual {p0}, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->onKeyguardShowingChanged()V

    return-void
.end method

.method public onKeyguardFadingAwayChanged()V
    .registers 1

    return-void
.end method

.method public onKeyguardShowingChanged()V
    .registers 10

    const/4 v5, 0x1

    const/4 v6, 0x0

    iget-object v4, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->displayManager:Landroid/hardware/display/DisplayManager;

    invoke-virtual {v4, v6}, Landroid/hardware/display/DisplayManager;->getDisplay(I)Landroid/view/Display;

    move-result-object v4

    invoke-virtual {v4}, Landroid/view/Display;->getState()I

    move-result v4

    invoke-direct {p0, v4}, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->isScreenOn(I)Z

    move-result v2

    iget-object v4, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->keyguardStateController:Lcom/android/systemui/statusbar/policy/KeyguardStateController;

    invoke-interface {v4}, Lcom/android/systemui/statusbar/policy/KeyguardStateController;->isUnlocked()Z

    move-result v1

    iget-object v4, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->mStatusBarStateController:Lcom/android/systemui/plugins/statusbar/StatusBarStateController;

    invoke-interface {v4}, Lcom/android/systemui/plugins/statusbar/StatusBarStateController;->isDozing()Z

    move-result v0

    invoke-static {}, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->getInstance()Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;

    move-result-object v4

    iget-boolean v3, v4, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->isPassword:Z

    if-eqz v1, :cond_5d

    if-eqz v2, :cond_5d

    if-nez v0, :cond_5d

    if-nez v3, :cond_5d

    invoke-direct {p0}, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->isOnKeyguard()Z

    move-result v4

    if-eqz v4, :cond_5d

    move v4, v5

    :goto_31
    invoke-direct {p0, v4}, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->updateKeyguard(Z)V

    if-eqz v2, :cond_5f

    if-nez v0, :cond_5f

    move v4, v5

    :goto_39
    invoke-direct {p0, v4}, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->updateScreenOn(Z)V

    const-string v4, "MyKeyguardStateController"

    new-instance v7, Ljava/lang/StringBuilder;

    invoke-direct {v7}, Ljava/lang/StringBuilder;-><init>()V

    const-string v8, "onKeyguardShowingChanged: "

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    if-eqz v1, :cond_61

    if-eqz v2, :cond_61

    if-nez v0, :cond_61

    if-nez v3, :cond_61

    :goto_51
    invoke-virtual {v7, v5}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    move-result-object v5

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v5

    invoke-static {v4, v5}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    return-void

    :cond_5d
    move v4, v6

    goto :goto_31

    :cond_5f
    move v4, v6

    goto :goto_39

    :cond_61
    move v5, v6

    goto :goto_51
.end method

.method public onUnlockedChanged()V
    .registers 1

    return-void
.end method

.method public removeCallBack(Lcom/android/systemui/statusbar/policy/MyKeyguardStateController$CallBack;)V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->mListener:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_statusbar_policy_MyKeyguardStateController',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
