"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/plugins/controllers/ControllerExt.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/plugins/controllers/ControllerExt.smali'
CLASS_FALLBACK_NAMES = ['ControllerExt.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_plugins_controllers_ControllerExt',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public Lcom/android/systemui/plugins/controllers/ControllerExt;\n.super Ljava/lang/Object;\n\n\n# annotations\n.annotation system Ldalvik/annotation/MemberClasses;\n    value = {\n        Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;,\n        Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;\n    }\n.end annotation\n\n.annotation system Ldalvik/annotation/Signature;\n    value = {\n        "<Cl::",\n        "Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;",\n        ">",\n        "Ljava/lang/Object;"\n    }\n.end annotation\n\n\n# instance fields\n.field protected final callBacks:Ljava/util/ArrayList;\n    .annotation system Ldalvik/annotation/Signature;\n        value = {\n            "Ljava/util/ArrayList",\n            "<TCl;>;"\n        }\n    .end annotation\n.end field\n\n.field protected context:Landroid/content/Context;\n\n\n# direct methods\n.method public constructor <init>(Landroid/content/Context;)V\n    .registers 3\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    new-instance v0, Ljava/util/ArrayList;\n\n    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V\n\n    iput-object v0, p0, Lcom/android/systemui/plugins/controllers/ControllerExt;->callBacks:Ljava/util/ArrayList;\n\n    iput-object p1, p0, Lcom/android/systemui/plugins/controllers/ControllerExt;->context:Landroid/content/Context;\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public addCallBack(Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;)V\n    .registers 4\n    .annotation system Ldalvik/annotation/Signature;\n        value = {\n            "(TCl;)V"\n        }\n    .end annotation\n\n    iget-object v1, p0, Lcom/android/systemui/plugins/controllers/ControllerExt;->callBacks:Ljava/util/ArrayList;\n\n    monitor-enter v1\n\n    :try_start_0\n    iget-object v0, p0, Lcom/android/systemui/plugins/controllers/ControllerExt;->callBacks:Ljava/util/ArrayList;\n\n    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z\n\n    monitor-exit v1\n\n    return-void\n\n    :catchall_0\n    move-exception v0\n\n    monitor-exit v1\n    :try_end_0\n    .catchall {:try_start_0 .. :try_end_0} :catchall_0\n\n    throw v0\n.end method\n\n.method public onSettingsChange()V\n    .registers 1\n\n    return-void\n.end method\n\n.method public onSettingsChange(Landroid/net/Uri;)V\n    .registers 2\n\n    return-void\n.end method\n\n.method public onSettingsChange(Ljava/lang/String;)V\n    .registers 2\n\n    return-void\n.end method\n\n.method public removeCallBack(Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;)V\n    .registers 4\n    .annotation system Ldalvik/annotation/Signature;\n        value = {\n            "(TCl;)V"\n        }\n    .end annotation\n\n    iget-object v1, p0, Lcom/android/systemui/plugins/controllers/ControllerExt;->callBacks:Ljava/util/ArrayList;\n\n    monitor-enter v1\n\n    :try_start_0\n    iget-object v0, p0, Lcom/android/systemui/plugins/controllers/ControllerExt;->callBacks:Ljava/util/ArrayList;\n\n    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z\n\n    monitor-exit v1\n\n    return-void\n\n    :catchall_0\n    move-exception v0\n\n    monitor-exit v1\n    :try_end_0\n    .catchall {:try_start_0 .. :try_end_0} :catchall_0\n\n    throw v0\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
