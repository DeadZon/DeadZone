"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController.smali'
CLASS_FALLBACK_NAMES = ['NotifHeaderTransitionController.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_controllers_NotifHeaderTra',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;\n.super Lcom/android/systemui/plugins/controllers/ControllerExt;\n\n\n# annotations\n.annotation system Ldalvik/annotation/Signature;\n    value = {\n        "Lcom/android/systemui/plugins/controllers/ControllerExt<",\n        "Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;",\n        ">;"\n    }\n.end annotation\n\n\n# instance fields\n.field private final parent:Ljava/util/ArrayList;\n    .annotation system Ldalvik/annotation/Signature;\n        value = {\n            "Ljava/util/ArrayList<",\n            "Lcom/android/systemui/newstatusbar/layouts/HeaderParent;",\n            ">;"\n        }\n    .end annotation\n.end field\n\n\n# direct methods\n.method public constructor <init>(Landroid/content/Context;)V\n    .registers 3\n\n    invoke-direct {p0, p1}, Lcom/android/systemui/plugins/controllers/ControllerExt;-><init>(Landroid/content/Context;)V\n\n    new-instance v0, Ljava/util/ArrayList;\n\n    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V\n\n    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;->parent:Ljava/util/ArrayList;\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public onAlphaChange(F)V\n    .registers 5\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;->parent:Ljava/util/ArrayList;\n\n    invoke-virtual {v0}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;\n\n    move-result-object v0\n\n    :goto_0\n    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z\n\n    move-result v1\n\n    if-eqz v1, :cond_2\n\n    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;\n\n    move-result-object v1\n\n    check-cast v1, Lcom/android/systemui/newstatusbar/layouts/HeaderParent;\n\n    if-eqz v1, :cond_1\n\n    invoke-virtual {v1, p1}, Lcom/android/systemui/newstatusbar/layouts/HeaderParent;->setAlpha(F)V\n\n    const v2, 0x3f666666\n\n    cmpl-float v2, p1, v2\n\n    if-lez v2, :cond_0\n\n    const/4 v2, 0x0\n\n    goto :goto_1\n\n    :cond_0\n    const/4 v2, 0x4\n\n    :goto_1\n    invoke-virtual {v1, v2}, Lcom/android/systemui/newstatusbar/layouts/HeaderParent;->setVisibility(I)V\n\n    :cond_1\n    goto :goto_0\n\n    :cond_2\n    return-void\n.end method\n\n.method public setParent(Lcom/android/systemui/newstatusbar/layouts/HeaderParent;)V\n    .registers 3\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;->parent:Ljava/util/ArrayList;\n\n    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
