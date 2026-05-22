"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/controllers/DarkController.smali'
CLASS_FALLBACK_NAMES = ['DarkController.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/controllers/DarkController;
.super Lcom/android/systemui/plugins/controllers/ControllerExt;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/android/systemui/newstatusbar/controllers/DarkController$DarkReceiver;
    }
.end annotation

.annotation system Ldalvik/annotation/Signature;
    value = {
        "Lcom/android/systemui/plugins/controllers/ControllerExt<",
        "Lcom/android/systemui/newstatusbar/controllers/DarkController$DarkReceiver;",
        ">;"
    }
.end annotation


# instance fields
.field private currColorSlotA:I

.field private currColorSlotB:I

.field private final handler:Landroid/os/Handler;


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 4

    invoke-direct {p0, p1}, Lcom/android/systemui/plugins/controllers/ControllerExt;-><init>(Landroid/content/Context;)V

    new-instance v0, Landroid/os/Handler;

    invoke-static {}, Landroid/os/Looper;->myLooper()Landroid/os/Looper;

    move-result-object v1

    invoke-direct {v0, v1}, Landroid/os/Handler;-><init>(Landroid/os/Looper;)V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/DarkController;->handler:Landroid/os/Handler;

    return-void
.end method

.method static synthetic access$000(Lcom/android/systemui/newstatusbar/controllers/DarkController;)V
    .registers 1

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/DarkController;->update()V

    return-void
.end method

.method private update()V
    .registers 5

    iget v0, p0, Lcom/android/systemui/newstatusbar/controllers/DarkController;->currColorSlotA:I

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/DarkController;->callBacks:Ljava/util/ArrayList;

    invoke-virtual {v1}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :goto_8
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    if-eqz v2, :cond_1a

    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v2

    check-cast v2, Lcom/android/systemui/newstatusbar/controllers/DarkController$DarkReceiver;

    sget-object v3, Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;->slotA:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    invoke-interface {v2, v0, v3}, Lcom/android/systemui/newstatusbar/controllers/DarkController$DarkReceiver;->onDarkChanged(ILcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)V

    goto :goto_8

    :cond_1a
    iget v0, p0, Lcom/android/systemui/newstatusbar/controllers/DarkController;->currColorSlotB:I

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/DarkController;->callBacks:Ljava/util/ArrayList;

    invoke-virtual {v1}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :goto_22
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    if-eqz v2, :cond_34

    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v2

    check-cast v2, Lcom/android/systemui/newstatusbar/controllers/DarkController$DarkReceiver;

    sget-object v3, Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;->slotB:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    invoke-interface {v2, v0, v3}, Lcom/android/systemui/newstatusbar/controllers/DarkController$DarkReceiver;->onDarkChanged(ILcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)V

    goto :goto_22

    :cond_34
    return-void
.end method


# virtual methods
.method public addCallBack(Lcom/android/systemui/newstatusbar/controllers/DarkController$DarkReceiver;)V
    .registers 4

    invoke-super {p0, p1}, Lcom/android/systemui/plugins/controllers/ControllerExt;->addCallBack(Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;)V

    iget v0, p0, Lcom/android/systemui/newstatusbar/controllers/DarkController;->currColorSlotA:I

    if-eqz v0, :cond_c

    sget-object v1, Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;->slotA:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    invoke-interface {p1, v0, v1}, Lcom/android/systemui/newstatusbar/controllers/DarkController$DarkReceiver;->onDarkChanged(ILcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)V

    :cond_c
    iget v0, p0, Lcom/android/systemui/newstatusbar/controllers/DarkController;->currColorSlotB:I

    if-eqz v0, :cond_17

    iget v0, p0, Lcom/android/systemui/newstatusbar/controllers/DarkController;->currColorSlotA:I

    sget-object v1, Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;->slotB:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    invoke-interface {p1, v0, v1}, Lcom/android/systemui/newstatusbar/controllers/DarkController$DarkReceiver;->onDarkChanged(ILcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)V

    :cond_17
    return-void
.end method

.method public bridge synthetic addCallBack(Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;)V
    .registers 2

    check-cast p1, Lcom/android/systemui/newstatusbar/controllers/DarkController$DarkReceiver;

    invoke-virtual {p0, p1}, Lcom/android/systemui/newstatusbar/controllers/DarkController;->addCallBack(Lcom/android/systemui/newstatusbar/controllers/DarkController$DarkReceiver;)V

    return-void
.end method

.method public setColor(ILcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)V
    .registers 5

    sget-object v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;->slotA:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    if-ne p2, v0, :cond_7

    iput p1, p0, Lcom/android/systemui/newstatusbar/controllers/DarkController;->currColorSlotA:I

    goto :goto_9

    :cond_7
    iput p1, p0, Lcom/android/systemui/newstatusbar/controllers/DarkController;->currColorSlotB:I

    :goto_9
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/DarkController;->handler:Landroid/os/Handler;

    new-instance v1, Lcom/android/systemui/newstatusbar/controllers/DarkController$1;

    invoke-direct {v1, p0}, Lcom/android/systemui/newstatusbar/controllers/DarkController$1;-><init>(Lcom/android/systemui/newstatusbar/controllers/DarkController;)V

    invoke-virtual {v0, v1}, Landroid/os/Handler;->post(Ljava/lang/Runnable;)Z

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_controllers_DarkController',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
