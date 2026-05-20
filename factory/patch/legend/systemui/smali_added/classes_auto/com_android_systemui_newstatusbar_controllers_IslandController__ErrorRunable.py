"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable.smali'
CLASS_FALLBACK_NAMES = ['IslandController$ErrorRunable.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable;
.super Ljava/lang/Object;

# interfaces
.implements Ljava/lang/Runnable;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/systemui/newstatusbar/controllers/IslandController;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0xa
    name = "ErrorRunable"
.end annotation


# instance fields
.field private controller:Lcom/android/systemui/newstatusbar/controllers/IslandController;

.field private final rect:Landroid/graphics/Rect;


# direct methods
.method public constructor <init>()V
    .registers 2

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    new-instance v0, Landroid/graphics/Rect;

    invoke-direct {v0}, Landroid/graphics/Rect;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable;->rect:Landroid/graphics/Rect;

    return-void
.end method

.method public constructor <init>(Landroid/graphics/Rect;Lcom/android/systemui/newstatusbar/controllers/IslandController;)V
    .registers 4

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    new-instance v0, Landroid/graphics/Rect;

    invoke-direct {v0}, Landroid/graphics/Rect;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable;->rect:Landroid/graphics/Rect;

    invoke-virtual {v0, p1}, Landroid/graphics/Rect;->set(Landroid/graphics/Rect;)V

    iput-object p2, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable;->controller:Lcom/android/systemui/newstatusbar/controllers/IslandController;

    return-void
.end method


# virtual methods
.method public run()V
    .registers 4

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable;->controller:Lcom/android/systemui/newstatusbar/controllers/IslandController;

    if-eqz v0, :cond_a

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable;->rect:Landroid/graphics/Rect;

    const/4 v2, 0x0

    invoke-virtual {v0, v1, v2}, Lcom/android/systemui/newstatusbar/controllers/IslandController;->onIslandSizeChanged(Landroid/graphics/Rect;Z)V

    :cond_a
    return-void
.end method

.method public setController(Lcom/android/systemui/newstatusbar/controllers/IslandController;)Lcom/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable;
    .registers 2

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable;->controller:Lcom/android/systemui/newstatusbar/controllers/IslandController;

    return-object p0
.end method

.method public setRect(Landroid/graphics/Rect;)Lcom/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable;
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable;->rect:Landroid/graphics/Rect;

    invoke-virtual {v0, p1}, Landroid/graphics/Rect;->set(Landroid/graphics/Rect;)V

    return-object p0
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_controllers_IslandController_ErrorRunable',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
