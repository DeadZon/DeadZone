"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/controllers/SimTypeController.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/controllers/SimTypeController.smali'
CLASS_FALLBACK_NAMES = ['SimTypeController.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_controllers_SimTypeControl',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public Lcom/android/systemui/newstatusbar/controllers/SimTypeController;\n.super Lcom/android/systemui/plugins/controllers/ControllerExt;\n\n# interfaces\n.implements Landroid/preference/CustomUpdater$CustomReceiver;\n\n\n# annotations\n.annotation system Ldalvik/annotation/MemberClasses;\n    value = {\n        Lcom/android/systemui/newstatusbar/controllers/SimTypeController$CallBack;\n    }\n.end annotation\n\n.annotation system Ldalvik/annotation/Signature;\n    value = {\n        "Lcom/android/systemui/plugins/controllers/ControllerExt<",\n        "Lcom/android/systemui/newstatusbar/controllers/SimTypeController$CallBack;",\n        ">;",\n        "Landroid/preference/CustomUpdater$CustomReceiver;"\n    }\n.end annotation\n\n\n# static fields\n.field private static instance:Lcom/android/systemui/newstatusbar/controllers/SimTypeController; = null\n\n.field private static final key:Ljava/lang/String; = "sim_type_style"\n\n\n# instance fields\n.field private isCustomSimType:Z\n\n\n# direct methods\n.method public constructor <init>(Landroid/content/Context;)V\n    .registers 4\n\n    invoke-direct {p0, p1}, Lcom/android/systemui/plugins/controllers/ControllerExt;-><init>(Landroid/content/Context;)V\n\n    sput-object p0, Lcom/android/systemui/newstatusbar/controllers/SimTypeController;->instance:Lcom/android/systemui/newstatusbar/controllers/SimTypeController;\n\n    invoke-static {}, Landroid/preference/CustomUpdater;->getInstance()Landroid/preference/CustomUpdater;\n\n    move-result-object v0\n\n    const-string v1, "sim_type_style"\n\n    invoke-virtual {v0, p0, v1}, Landroid/preference/CustomUpdater;->addCustomReceiver(Landroid/preference/CustomUpdater$CustomReceiver;Ljava/lang/String;)V\n\n    invoke-static {v1}, Landroid/preference/SettingsMezoHelper;->getBoolofSettings(Ljava/lang/String;)Z\n\n    move-result v0\n\n    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/controllers/SimTypeController;->isCustomSimType:Z\n\n    return-void\n.end method\n\n.method public static getInstance()Lcom/android/systemui/newstatusbar/controllers/SimTypeController;\n    .registers 2\n\n    const-class v0, Lcom/android/systemui/newstatusbar/controllers/SimTypeController;\n\n    monitor-enter v0\n\n    :try_start_0\n    sget-object v1, Lcom/android/systemui/newstatusbar/controllers/SimTypeController;->instance:Lcom/android/systemui/newstatusbar/controllers/SimTypeController;\n\n    monitor-exit v0\n\n    return-object v1\n\n    :catchall_0\n    move-exception v1\n\n    monitor-exit v0\n    :try_end_0\n    .catchall {:try_start_0 .. :try_end_0} :catchall_0\n\n    throw v1\n.end method\n\n.method private update()V\n    .registers 3\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/SimTypeController;->callBacks:Ljava/util/ArrayList;\n\n    invoke-virtual {v0}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;\n\n    move-result-object v0\n\n    :goto_0\n    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z\n\n    move-result v1\n\n    if-eqz v1, :cond_0\n\n    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;\n\n    move-result-object v1\n\n    check-cast v1, Lcom/android/systemui/newstatusbar/controllers/SimTypeController$CallBack;\n\n    invoke-interface {v1}, Lcom/android/systemui/newstatusbar/controllers/SimTypeController$CallBack;->onSimTypeChange()V\n\n    goto :goto_0\n\n    :cond_0\n    return-void\n.end method\n\n\n# virtual methods\n.method public isCustomSimType()Z\n    .registers 2\n\n    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/controllers/SimTypeController;->isCustomSimType:Z\n\n    return v0\n.end method\n\n.method public onCustomChanged(Ljava/lang/String;)V\n    .registers 4\n\n    const-string v0, "sim_type_style"\n\n    invoke-virtual {v0, p1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z\n\n    move-result v1\n\n    if-eqz v1, :cond_0\n\n    invoke-static {v0}, Landroid/preference/SettingsMezoHelper;->getBoolofSettings1(Ljava/lang/String;)Z\n\n    move-result v0\n\n    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/controllers/SimTypeController;->isCustomSimType:Z\n\n    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/SimTypeController;->update()V\n\n    :cond_0\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
