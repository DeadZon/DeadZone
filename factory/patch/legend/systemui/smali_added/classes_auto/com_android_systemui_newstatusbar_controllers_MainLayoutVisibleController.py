"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/controllers/MainLayoutVisibleController.smali'
CLASS_FALLBACK_NAMES = ['MainLayoutVisibleController.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;
.super Ljava/lang/Object;


# instance fields
.field private final TAG:Ljava/lang/String;

.field private isControlShow:Z

.field private isExpandShow:Z

.field private isInLockScreen:Z

.field private isNeedControlVisible:Z

.field private final layout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

.field private visibilityNotController:I


# direct methods
.method public constructor <init>(Lcom/android/systemui/newstatusbar/layouts/MainLayout;)V
    .registers 3

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    sget-object v0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->TAG:Ljava/lang/String;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->TAG:Ljava/lang/String;

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->layout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    return-void
.end method

.method private setMainVisibility(I)V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->layout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    invoke-virtual {v0, p1}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->superSetVisibility(I)V

    return-void
.end method

.method private updateVisibility()V
    .registers 2

    iget v0, p0, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->visibilityNotController:I

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->setVisibility(I)V

    return-void
.end method


# virtual methods
.method public setControlShow(Z)V
    .registers 2

    iput-boolean p1, p0, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->isControlShow:Z

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->updateVisibility()V

    return-void
.end method

.method public setExpandShow(Z)V
    .registers 2

    iput-boolean p1, p0, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->isExpandShow:Z

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->updateVisibility()V

    return-void
.end method

.method public setInLockScreen(Z)V
    .registers 2

    iput-boolean p1, p0, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->isInLockScreen:Z

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->updateVisibility()V

    return-void
.end method

.method public setVisibility(I)V
    .registers 3

    iput p1, p0, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->visibilityNotController:I

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->isNeedControlVisible:Z

    if-nez v0, :cond_a

    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->setMainVisibility(I)V

    goto :goto_1f

    :cond_a
    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->isInLockScreen:Z

    if-nez v0, :cond_1b

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->isControlShow:Z

    if-nez v0, :cond_1b

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->isExpandShow:Z

    if-eqz v0, :cond_17

    goto :goto_1b

    :cond_17
    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->setMainVisibility(I)V

    goto :goto_1f

    :cond_1b
    :goto_1b
    const/4 v0, 0x4

    invoke-direct {p0, v0}, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->setMainVisibility(I)V

    :goto_1f
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_controllers_MainLayoutVisibleController',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
