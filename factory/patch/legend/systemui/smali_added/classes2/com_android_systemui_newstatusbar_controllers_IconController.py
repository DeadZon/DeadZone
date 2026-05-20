"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/controllers/IconController.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/controllers/IconController.smali'
CLASS_FALLBACK_NAMES = ['IconController.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_controllers_IconController',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public abstract Lcom/android/systemui/newstatusbar/controllers/IconController;\n.super Lcom/android/systemui/plugins/controllers/ControllerExt;\n\n\n# annotations\n.annotation system Ldalvik/annotation/MemberClasses;\n    value = {\n        Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;\n    }\n.end annotation\n\n.annotation system Ldalvik/annotation/Signature;\n    value = {\n        "Lcom/android/systemui/plugins/controllers/ControllerExt<",\n        "Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;",\n        ">;"\n    }\n.end annotation\n\n\n# direct methods\n.method public constructor <init>(Landroid/content/Context;)V\n    .registers 2\n\n    invoke-direct {p0, p1}, Lcom/android/systemui/plugins/controllers/ControllerExt;-><init>(Landroid/content/Context;)V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public abstract addCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V\n.end method\n\n.method public bridge synthetic addCallBack(Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;)V\n    .registers 2\n\n    check-cast p1, Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;\n\n    invoke-virtual {p0, p1}, Lcom/android/systemui/newstatusbar/controllers/IconController;->addCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V\n\n    return-void\n.end method\n\n.method public abstract removeCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V\n.end method\n\n.method public bridge synthetic removeCallBack(Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;)V\n    .registers 2\n\n    check-cast p1, Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;\n\n    invoke-virtual {p0, p1}, Lcom/android/systemui/newstatusbar/controllers/IconController;->removeCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V\n\n    return-void\n.end method\n\n.method public updateCallBacks(Ljava/util/ArrayList;)V\n    .registers 5\n    .annotation system Ldalvik/annotation/Signature;\n        value = {\n            "(",\n            "Ljava/util/ArrayList<",\n            "Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;",\n            ">;)V"\n        }\n    .end annotation\n\n    invoke-virtual {p1}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;\n\n    move-result-object v0\n\n    :goto_0\n    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z\n\n    move-result v1\n\n    if-eqz v1, :cond_1\n\n    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;\n\n    move-result-object v1\n\n    check-cast v1, Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;\n\n    instance-of v2, v1, Landroid/view/View;\n\n    if-eqz v2, :cond_0\n\n    new-instance v2, Lcom/android/systemui/newstatusbar/controllers/IconController$1;\n\n    invoke-direct {v2, p0, v1}, Lcom/android/systemui/newstatusbar/controllers/IconController$1;-><init>(Lcom/android/systemui/newstatusbar/controllers/IconController;Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V\n\n    invoke-interface {v1, v2}, Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;->post(Ljava/lang/Runnable;)Z\n\n    goto :goto_1\n\n    :cond_0\n    invoke-interface {v1}, Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;->onIconChange()V\n\n    :goto_1\n    goto :goto_0\n\n    :cond_1\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
