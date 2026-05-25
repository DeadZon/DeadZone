"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/statusbar/policy/ControllerExpandHeight.smali'
CLASS_FALLBACK_NAMES = ['ControllerExpandHeight.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;
.super Ljava/lang/Object;

# interfaces
.implements Lcom/android/systemui/statusbar/phone/StatusBarWindowCallback;
.implements Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager$OnWindowChangeListener;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/android/systemui/statusbar/policy/ControllerExpandHeight$CallBack;
    }
.end annotation


# static fields
.field private static final TAG:Ljava/lang/String;

.field public static isInLockScreen:Z

.field private static final sControllerExpandHeight:Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;
    .annotation build Landroid/annotation/SuppressLint;
        value = {
            "StaticFieldLeak"
        }
    .end annotation
.end field


# instance fields
.field private final handler:Landroid/os/Handler;

.field private isControlShow:Z

.field private isExpandShow:Z

.field public isPassword:Z

.field private mBlurSwitched:Z

.field private mExpandHeight:F

.field private final mListener:Ljava/util/ArrayList;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/ArrayList",
            "<",
            "Lcom/android/systemui/statusbar/policy/ControllerExpandHeight$CallBack;",
            ">;"
        }
    .end annotation
.end field

.field private final updateControlRunable:Ljava/lang/Runnable;


# direct methods
.method static constructor <clinit>()V
    .registers 1

    new-instance v0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;

    invoke-direct {v0}, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;-><init>()V

    sput-object v0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->sControllerExpandHeight:Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;

    const-class v0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;

    invoke-virtual {v0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object v0

    sput-object v0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->TAG:Ljava/lang/String;

    const/4 v0, 0x0

    sput-boolean v0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->isInLockScreen:Z

    return-void
.end method

.method private constructor <init>()V
    .registers 3

    const/4 v1, 0x0

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->mListener:Ljava/util/ArrayList;

    iput-boolean v1, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->isExpandShow:Z

    iput-boolean v1, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->isControlShow:Z

    iput-boolean v1, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->isPassword:Z

    const/4 v0, 0x0

    iput v0, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->mExpandHeight:F

    iput-boolean v1, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->mBlurSwitched:Z

    new-instance v0, Landroid/os/Handler;

    invoke-static {}, Landroid/os/Looper;->getMainLooper()Landroid/os/Looper;

    move-result-object v1

    invoke-direct {v0, v1}, Landroid/os/Handler;-><init>(Landroid/os/Looper;)V

    iput-object v0, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->handler:Landroid/os/Handler;

    new-instance v0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight$1;

    invoke-direct {v0, p0}, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight$1;-><init>(Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;)V

    iput-object v0, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->updateControlRunable:Ljava/lang/Runnable;

    return-void
.end method

.method static synthetic access$000(Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;Z)V
    .registers 2

    invoke-direct {p0, p1}, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->updateControl(Z)V

    return-void
.end method

.method public static declared-synchronized getInstance()Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;
    .registers 4

    const-class v2, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;

    monitor-enter v2

    :try_start_3
    const-class v3, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;

    monitor-enter v3
    :try_end_6
    .catchall {:try_start_3 .. :try_end_6} :catchall_e

    :try_start_6
    sget-object v0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->sControllerExpandHeight:Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;

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

.method private updateControl(Z)V
    .registers 5

    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->mListener:Ljava/util/ArrayList;

    invoke-virtual {v1}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :goto_6
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    if-eqz v2, :cond_16

    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight$CallBack;

    invoke-interface {v0, p1}, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight$CallBack;->onControlHeightChange(Z)V

    goto :goto_6

    :cond_16
    return-void
.end method

.method private updateExpand(Z)V
    .registers 2

    invoke-direct {p0, p1}, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->updateExpandInternal(Z)V

    return-void
.end method

.method private updateExpandInternal(Z)V
    .registers 5

    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->mListener:Ljava/util/ArrayList;

    invoke-virtual {v1}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :goto_6
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    if-eqz v2, :cond_16

    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight$CallBack;

    invoke-interface {v0, p1}, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight$CallBack;->onExpandHeightChange(Z)V

    goto :goto_6

    :cond_16
    return-void
.end method

.method private updateNCSwitch(Z)V
    .registers 5

    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->mListener:Ljava/util/ArrayList;

    invoke-virtual {v1}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :goto_6
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    if-eqz v2, :cond_16

    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight$CallBack;

    invoke-interface {v0, p1}, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight$CallBack;->onNCSwithChange(Z)V

    goto :goto_6

    :cond_16
    return-void
.end method


# virtual methods
.method public addCallBack(Lcom/android/systemui/statusbar/policy/ControllerExpandHeight$CallBack;)V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->mListener:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    return-void
.end method

.method public handleConntrolNotificationSwitch()V
    .registers 3

    const/4 v1, 0x0

    const/4 v0, 0x1

    invoke-direct {p0, v0}, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->updateNCSwitch(Z)V

    iput-boolean v1, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->isControlShow:Z

    iput-boolean v0, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->isExpandShow:Z

    invoke-direct {p0, v1}, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->updateControl(Z)V

    invoke-direct {p0, v0}, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->updateExpandInternal(Z)V

    return-void
.end method

.method public handleNotificationConntrolSwitch()V
    .registers 3

    const/4 v1, 0x1

    const/4 v0, 0x0

    invoke-direct {p0, v0}, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->updateNCSwitch(Z)V

    iput-boolean v1, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->isControlShow:Z

    iput-boolean v0, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->isExpandShow:Z

    invoke-direct {p0, v0}, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->updateExpandInternal(Z)V

    invoke-direct {p0, v1}, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->updateControl(Z)V

    return-void
.end method

.method public isControlShow()Z
    .registers 2

    iget-boolean v0, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->isControlShow:Z

    return v0
.end method

.method public onControllHeightChange(F)V
    .registers 6

    const/4 v3, 0x1

    const/high16 v2, 0x42a00000  # 80.0f

    iget v0, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->mExpandHeight:F

    iput p1, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->mExpandHeight:F

    cmpg-float v1, v0, v2

    if-ltz v1, :cond_f

    cmpl-float v1, p1, v2

    if-ltz v1, :cond_20

    :cond_f
    cmpg-float v1, v0, v2

    if-gez v1, :cond_20

    cmpl-float v1, p1, v2

    if-ltz v1, :cond_20

    iget-boolean v1, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->isControlShow:Z

    if-nez v1, :cond_20

    iput-boolean v3, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->isControlShow:Z

    invoke-direct {p0, v3}, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->updateControl(Z)V

    :cond_20
    return-void
.end method

.method public onControllHeightChange(Z)V
    .registers 6

    iget-object v0, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->handler:Landroid/os/Handler;

    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->updateControlRunable:Ljava/lang/Runnable;

    invoke-virtual {v0, v1}, Landroid/os/Handler;->removeCallbacks(Ljava/lang/Runnable;)V

    iget-boolean v0, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->isControlShow:Z

    if-eq p1, v0, :cond_18

    iput-boolean p1, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->isControlShow:Z

    if-eqz p1, :cond_19

    iget-object v0, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->handler:Landroid/os/Handler;

    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->updateControlRunable:Ljava/lang/Runnable;

    const-wide/16 v2, 0x78

    invoke-virtual {v0, v1, v2, v3}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z

    :cond_18
    :goto_18
    return-void

    :cond_19
    invoke-direct {p0, p1}, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->updateControl(Z)V

    goto :goto_18
.end method

.method public onExpandChange(Z)V
    .registers 2

    invoke-virtual {p0, p1}, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->onControllHeightChange(Z)V

    return-void
.end method

.method public onExpandHeightChange(I)V
    .registers 6

    const/4 v3, 0x5

    const/4 v2, 0x1

    const/4 v1, 0x0

    if-le p1, v3, :cond_13

    iget-boolean v0, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->isExpandShow:Z

    if-nez v0, :cond_13

    iget-boolean v0, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->isPassword:Z

    if-nez v0, :cond_13

    iput-boolean v2, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->isExpandShow:Z

    invoke-direct {p0, v2}, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->updateExpand(Z)V

    :cond_12
    :goto_12
    return-void

    :cond_13
    iget-boolean v0, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->isExpandShow:Z

    if-eqz v0, :cond_12

    if-le p1, v3, :cond_1d

    iget-boolean v0, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->isPassword:Z

    if-eqz v0, :cond_12

    :cond_1d
    iput-boolean v1, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->isExpandShow:Z

    invoke-direct {p0, v1}, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->updateExpand(Z)V

    goto :goto_12
.end method

.method public onStateChanged(ZZZ)V
    .registers 5

    iput-boolean p3, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->isPassword:Z

    invoke-static {}, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->getInstance()Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->onKeyguardShowingChanged()V

    if-nez p1, :cond_d

    if-eqz p3, :cond_11

    :cond_d
    const/4 v0, 0x1

    :goto_e
    sput-boolean v0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->isInLockScreen:Z

    return-void

    :cond_11
    const/4 v0, 0x0

    goto :goto_e
.end method

.method public removeCallBack(Lcom/android/systemui/statusbar/policy/ControllerExpandHeight$CallBack;)V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->mListener:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    return-void
.end method

.method public setblurSwitched(Z)V
    .registers 2

    iput-boolean p1, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->mBlurSwitched:Z

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_statusbar_policy_ControllerExpandHeight',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
