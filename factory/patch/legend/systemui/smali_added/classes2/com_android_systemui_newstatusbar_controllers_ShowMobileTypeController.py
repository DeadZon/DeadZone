"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/controllers/ShowMobileTypeController.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/controllers/ShowMobileTypeController.smali'
CLASS_FALLBACK_NAMES = ['ShowMobileTypeController.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_controllers_ShowMobileType',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public Lcom/android/systemui/newstatusbar/controllers/ShowMobileTypeController;\n.super Lcom/android/systemui/plugins/controllers/ControllerExt;\n\n\n# annotations\n.annotation system Ldalvik/annotation/Signature;\n    value = {\n        "Lcom/android/systemui/plugins/controllers/ControllerExt",\n        "<",\n        "Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;",\n        ">;"\n    }\n.end annotation\n\n\n# instance fields\n.field private final list:Ljava/util/ArrayList;\n    .annotation system Ldalvik/annotation/Signature;\n        value = {\n            "Ljava/util/ArrayList",\n            "<",\n            "Lcom/android/systemui/MiuiOperatorCustomizedPolicy;",\n            ">;"\n        }\n    .end annotation\n.end field\n\n\n# direct methods\n.method public constructor <init>(Landroid/content/Context;)V\n    .registers 6\n\n    invoke-direct {p0, p1}, Lcom/android/systemui/plugins/controllers/ControllerExt;-><init>(Landroid/content/Context;)V\n\n    new-instance v0, Ljava/util/ArrayList;\n\n    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V\n\n    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/ShowMobileTypeController;->list:Ljava/util/ArrayList;\n\n    new-instance v0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;\n\n    const/4 v1, 0x1\n\n    new-array v1, v1, [Ljava/lang/String;\n\n    const/4 v2, 0x0\n\n    const-string v3, "show_type_name_mobile"\n\n    aput-object v3, v1, v2\n\n    invoke-direct {v0, p0, v1}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;-><init>(Lcom/android/systemui/plugins/controllers/ControllerExt;[Ljava/lang/String;)V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public addPolicy(Lcom/android/systemui/MiuiOperatorCustomizedPolicy;)V\n    .registers 3\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/ShowMobileTypeController;->list:Ljava/util/ArrayList;\n\n    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z\n\n    return-void\n.end method\n\n.method public onSettingsChange(Ljava/lang/String;)V\n    .registers 6\n\n    iget-object v2, p0, Lcom/android/systemui/newstatusbar/controllers/ShowMobileTypeController;->list:Ljava/util/ArrayList;\n\n    invoke-virtual {v2}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;\n\n    move-result-object v2\n\n    :cond_0\n    invoke-interface {v2}, Ljava/util/Iterator;->hasNext()Z\n\n    move-result v3\n\n    if-eqz v3, :cond_1\n\n    invoke-interface {v2}, Ljava/util/Iterator;->next()Ljava/lang/Object;\n\n    move-result-object v1\n\n    check-cast v1, Lcom/android/systemui/MiuiOperatorCustomizedPolicy;\n\n    const/4 v0, 0x0\n\n    :goto_0\n    iget-object v3, v1, Lcom/android/systemui/MiuiOperatorCustomizedPolicy;->mOperators:Landroid/util/SparseArray;\n\n    invoke-virtual {v3}, Landroid/util/SparseArray;->size()I\n\n    move-result v3\n\n    if-ge v0, v3, :cond_0\n\n    iget-object v3, v1, Lcom/android/systemui/MiuiOperatorCustomizedPolicy;->mOperators:Landroid/util/SparseArray;\n\n    invoke-virtual {v3, v0}, Landroid/util/SparseArray;->keyAt(I)I\n\n    move-result v3\n\n    invoke-virtual {v1, v3}, Lcom/android/systemui/MiuiOperatorCustomizedPolicy;->updateMiuiOperatorConfig(I)V\n\n    add-int/lit8 v0, v0, 0x1\n\n    goto :goto_0\n\n    :cond_1\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
