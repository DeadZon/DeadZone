"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/controllers/MainLayoutVisibleController.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/controllers/MainLayoutVisibleController.smali'
CLASS_FALLBACK_NAMES = ['MainLayoutVisibleController.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_controllers_MainLayoutVisi',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;\n.super Ljava/lang/Object;\n\n\n# instance fields\n.field private final TAG:Ljava/lang/String;\n\n.field private isControlShow:Z\n\n.field private isExpandShow:Z\n\n.field private isInLockScreen:Z\n\n.field private isNeedControlVisible:Z\n\n.field private final layout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;\n\n.field private visibilityNotController:I\n\n\n# direct methods\n.method public constructor <init>(Lcom/android/systemui/newstatusbar/layouts/MainLayout;)V\n    .registers 3\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    sget-object v0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->TAG:Ljava/lang/String;\n\n    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->TAG:Ljava/lang/String;\n\n    iput-object p1, p0, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->layout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;\n\n    return-void\n.end method\n\n.method private setMainVisibility(I)V\n    .registers 3\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->layout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;\n\n    invoke-virtual {v0, p1}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->superSetVisibility(I)V\n\n    return-void\n.end method\n\n.method private updateVisibility()V\n    .registers 2\n\n    iget v0, p0, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->visibilityNotController:I\n\n    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->setVisibility(I)V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public setControlShow(Z)V\n    .registers 2\n\n    iput-boolean p1, p0, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->isControlShow:Z\n\n    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->updateVisibility()V\n\n    return-void\n.end method\n\n.method public setExpandShow(Z)V\n    .registers 2\n\n    iput-boolean p1, p0, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->isExpandShow:Z\n\n    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->updateVisibility()V\n\n    return-void\n.end method\n\n.method public setInLockScreen(Z)V\n    .registers 2\n\n    iput-boolean p1, p0, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->isInLockScreen:Z\n\n    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->updateVisibility()V\n\n    return-void\n.end method\n\n.method public setVisibility(I)V\n    .registers 3\n\n    iput p1, p0, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->visibilityNotController:I\n\n    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->isNeedControlVisible:Z\n\n    if-nez v0, :cond_0\n\n    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->setMainVisibility(I)V\n\n    goto :goto_1\n\n    :cond_0\n    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->isInLockScreen:Z\n\n    if-nez v0, :cond_2\n\n    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->isControlShow:Z\n\n    if-nez v0, :cond_2\n\n    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->isExpandShow:Z\n\n    if-eqz v0, :cond_1\n\n    goto :goto_0\n\n    :cond_1\n    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->setMainVisibility(I)V\n\n    goto :goto_1\n\n    :cond_2\n    :goto_0\n    const/4 v0, 0x4\n\n    invoke-direct {p0, v0}, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->setMainVisibility(I)V\n\n    :goto_1\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
