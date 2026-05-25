"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/controllers/IslandController.smali'
CLASS_FALLBACK_NAMES = ['IslandController.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/controllers/IslandController;
.super Lcom/android/systemui/plugins/controllers/ControllerExt;

# interfaces
.implements Lcom/android/systemui/statusbar/OnIslandStatusChangedListener;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable;,
        Lcom/android/systemui/newstatusbar/controllers/IslandController$OnIslandChangeListener;
    }
.end annotation

.annotation system Ldalvik/annotation/Signature;
    value = {
        "Lcom/android/systemui/plugins/controllers/ControllerExt<",
        "Lcom/android/systemui/newstatusbar/controllers/IslandController$OnIslandChangeListener;",
        ">;",
        "Lcom/android/systemui/statusbar/OnIslandStatusChangedListener;"
    }
.end annotation


# instance fields
.field TAG:Ljava/lang/String;

.field private allWidth:I

.field private final errorRunable:Lcom/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable;

.field private final handler:Landroid/os/Handler;

.field private isShown:Z

.field private leftWidth:I

.field private rightWidth:I


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 4

    invoke-direct {p0, p1}, Lcom/android/systemui/plugins/controllers/ControllerExt;-><init>(Landroid/content/Context;)V

    new-instance v0, Lcom/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable;

    invoke-direct {v0}, Lcom/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController;->errorRunable:Lcom/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable;

    new-instance v0, Landroid/os/Handler;

    invoke-static {}, Landroid/os/Looper;->myLooper()Landroid/os/Looper;

    move-result-object v1

    invoke-direct {v0, v1}, Landroid/os/Handler;-><init>(Landroid/os/Looper;)V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController;->handler:Landroid/os/Handler;

    sget-object v0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->TAG:Ljava/lang/String;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController;->TAG:Ljava/lang/String;

    return-void
.end method

.method private getMetrics()Landroid/util/DisplayMetrics;
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController;->context:Landroid/content/Context;

    const-string v1, "window"

    invoke-virtual {v0, v1}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/view/WindowManager;

    invoke-interface {v0}, Landroid/view/WindowManager;->getDefaultDisplay()Landroid/view/Display;

    move-result-object v0

    new-instance v1, Landroid/util/DisplayMetrics;

    invoke-direct {v1}, Landroid/util/DisplayMetrics;-><init>()V

    invoke-virtual {v0, v1}, Landroid/view/Display;->getRealMetrics(Landroid/util/DisplayMetrics;)V

    return-object v1
.end method

.method private maybeError(Landroid/graphics/Rect;)V
    .registers 6

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController;->handler:Landroid/os/Handler;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController;->errorRunable:Lcom/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable;

    invoke-virtual {v0, v1}, Landroid/os/Handler;->removeCallbacks(Ljava/lang/Runnable;)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController;->errorRunable:Lcom/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable;

    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable;->setController(Lcom/android/systemui/newstatusbar/controllers/IslandController;)Lcom/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable;

    move-result-object v0

    invoke-virtual {v0, p1}, Lcom/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable;->setRect(Landroid/graphics/Rect;)Lcom/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable;

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController;->handler:Landroid/os/Handler;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController;->errorRunable:Lcom/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable;

    const-wide/16 v2, 0x2bc

    invoke-virtual {v0, v1, v2, v3}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z

    return-void
.end method


# virtual methods
.method public addCallBack(Lcom/android/systemui/newstatusbar/controllers/IslandController$OnIslandChangeListener;)V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController;->callBacks:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->contains(Ljava/lang/Object;)Z

    move-result v0

    if-nez v0, :cond_b

    invoke-super {p0, p1}, Lcom/android/systemui/plugins/controllers/ControllerExt;->addCallBack(Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;)V

    :cond_b
    return-void
.end method

.method public bridge synthetic addCallBack(Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;)V
    .registers 2

    check-cast p1, Lcom/android/systemui/newstatusbar/controllers/IslandController$OnIslandChangeListener;

    invoke-virtual {p0, p1}, Lcom/android/systemui/newstatusbar/controllers/IslandController;->addCallBack(Lcom/android/systemui/newstatusbar/controllers/IslandController$OnIslandChangeListener;)V

    return-void
.end method

.method public clearCallbaks()V
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController;->callBacks:Ljava/util/ArrayList;

    invoke-virtual {v0}, Ljava/util/ArrayList;->clear()V

    return-void
.end method

.method public getAllWidth()I
    .registers 2

    iget v0, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController;->allWidth:I

    return v0
.end method

.method public getLeftWidth()I
    .registers 2

    iget v0, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController;->leftWidth:I

    return v0
.end method

.method public getRealHeight()I
    .registers 2

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/IslandController;->getMetrics()Landroid/util/DisplayMetrics;

    move-result-object v0

    iget v0, v0, Landroid/util/DisplayMetrics;->heightPixels:I

    return v0
.end method

.method public getRealWidth()I
    .registers 2

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/IslandController;->getMetrics()Landroid/util/DisplayMetrics;

    move-result-object v0

    iget v0, v0, Landroid/util/DisplayMetrics;->widthPixels:I

    return v0
.end method

.method public getRightWidth()I
    .registers 2

    iget v0, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController;->rightWidth:I

    return v0
.end method

.method public isShown()Z
    .registers 2

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController;->isShown:Z

    return v0
.end method

.method public onIslandSizeChanged(Landroid/graphics/Rect;Z)V
    .registers 10

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    iget-object v0, v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController;->isShown:Z

    const/4 v2, 0x0

    if-eqz v1, :cond_4f

    if-eqz v0, :cond_4f

    const/4 v1, 0x2

    new-array v3, v1, [I

    invoke-virtual {v0, v3}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getLocationOnScreen([I)V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/controllers/IslandController;->getRealWidth()I

    move-result v4

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getWidth()I

    move-result v5

    sub-int/2addr v4, v5

    aget v5, v3, v2

    mul-int/2addr v5, v1

    sub-int/2addr v4, v5

    div-int/2addr v4, v1

    add-int/lit8 v4, v4, 0xf

    iget v1, p1, Landroid/graphics/Rect;->left:I

    aget v2, v3, v2

    sub-int/2addr v1, v2

    sub-int/2addr v1, v4

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getWidth()I

    move-result v2

    invoke-virtual {p1}, Landroid/graphics/Rect;->width()I

    move-result v5

    sub-int/2addr v2, v5

    sub-int/2addr v2, v1

    invoke-virtual {p1}, Landroid/graphics/Rect;->width()I

    move-result v5

    iput v5, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController;->allWidth:I

    sub-int v5, v1, v4

    iput v5, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController;->leftWidth:I

    sub-int v6, v2, v4

    iput v6, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController;->rightWidth:I

    if-ltz v5, :cond_4b

    if-gez v6, :cond_4a

    goto :goto_4b

    :cond_4a
    goto :goto_55

    :cond_4b
    :goto_4b
    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/controllers/IslandController;->maybeError(Landroid/graphics/Rect;)V

    return-void

    :cond_4f
    iput v2, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController;->rightWidth:I

    iput v2, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController;->leftWidth:I

    iput v2, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController;->allWidth:I

    :goto_55
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController;->callBacks:Ljava/util/ArrayList;

    invoke-virtual {v1}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :goto_5b
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    if-eqz v2, :cond_72

    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v2

    check-cast v2, Lcom/android/systemui/newstatusbar/controllers/IslandController$OnIslandChangeListener;

    iget v3, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController;->leftWidth:I

    iget v4, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController;->rightWidth:I

    invoke-interface {v2, v3, v4}, Lcom/android/systemui/newstatusbar/controllers/IslandController$OnIslandChangeListener;->onIslandSizeChange(II)V

    invoke-interface {v2, p1}, Lcom/android/systemui/newstatusbar/controllers/IslandController$OnIslandChangeListener;->onIslandSizeChange(Landroid/graphics/Rect;)V

    goto :goto_5b

    :cond_72
    return-void
.end method

.method public onIslandStatusChanged(ZZZ)V
    .registers 6

    iput-boolean p1, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController;->isShown:Z

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController;->callBacks:Ljava/util/ArrayList;

    invoke-virtual {v0}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_8
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_18

    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/systemui/newstatusbar/controllers/IslandController$OnIslandChangeListener;

    invoke-interface {v1, p1}, Lcom/android/systemui/newstatusbar/controllers/IslandController$OnIslandChangeListener;->onIslandShowChange(Z)V

    goto :goto_8

    :cond_18
    if-nez p1, :cond_21

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController;->handler:Landroid/os/Handler;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController;->errorRunable:Lcom/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable;

    invoke-virtual {v0, v1}, Landroid/os/Handler;->removeCallbacks(Ljava/lang/Runnable;)V

    :cond_21
    return-void
.end method

.method public setController(Lcom/android/systemui/statusbar/StatusBarIslandControllerImpl;)V
    .registers 3

    iget-object v0, p1, Lcom/android/systemui/statusbar/StatusBarIslandControllerImpl;->islandStateHandler:Lcom/android/systemui/statusbar/StatusBarIslandControllerImpl$IslandStateHandler;

    iget-object v0, v0, Lcom/android/systemui/statusbar/StatusBarIslandControllerImpl$IslandStateHandler;->onIslandStateChangedListeners:Ljava/util/Set;

    invoke-interface {v0, p0}, Ljava/util/Set;->contains(Ljava/lang/Object;)Z

    move-result v0

    if-nez v0, :cond_d

    invoke-virtual {p1, p0}, Lcom/android/systemui/statusbar/StatusBarIslandControllerImpl;->addOnIslandStatusChangedListener(Lcom/android/systemui/statusbar/OnIslandStatusChangedListener;)V

    :cond_d
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_controllers_IslandController',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
