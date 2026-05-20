"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/MiuiPhoneStatusBarViewSettingsController.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/MiuiPhoneStatusBarViewSettingsController.smali'
CLASS_FALLBACK_NAMES = ['MiuiPhoneStatusBarViewSettingsController.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_MiuiPhoneStatusBarViewSett',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarViewSettingsController;\n.super Lcom/android/systemui/plugins/controllers/ControllerExt;\n\n\n# annotations\n.annotation system Ldalvik/annotation/MemberClasses;\n    value = {\n        Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarViewSettingsController$CallBack;\n    }\n.end annotation\n\n.annotation system Ldalvik/annotation/Signature;\n    value = {\n        "Lcom/android/systemui/plugins/controllers/ControllerExt<",\n        "Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarViewSettingsController$CallBack;",\n        ">;"\n    }\n.end annotation\n\n\n# direct methods\n.method public constructor <init>(Landroid/content/Context;)V\n    .registers 6\n\n    invoke-direct {p0, p1}, Lcom/android/systemui/plugins/controllers/ControllerExt;-><init>(Landroid/content/Context;)V\n\n    new-instance v0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;\n\n    const-string v1, "custom_status_bar_top"\n\n    const-string v2, "custom_status_bar_left_right"\n\n    const-string v3, "custom_statusbar_dialog_open"\n\n    filled-new-array {v1, v2, v3}, [Ljava/lang/String;\n\n    move-result-object v1\n\n    invoke-direct {v0, p0, v1}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;-><init>(Lcom/android/systemui/plugins/controllers/ControllerExt;[Ljava/lang/String;)V\n\n    new-instance v0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;\n\n    const-string v1, "custom_status_bar_height"\n\n    filled-new-array {v1}, [Ljava/lang/String;\n\n    move-result-object v1\n\n    sget-object v2, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;->Global:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;\n\n    invoke-direct {v0, p0, v1, v2}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;-><init>(Lcom/android/systemui/plugins/controllers/ControllerExt;[Ljava/lang/String;Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;)V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public onSettingsChange(Ljava/lang/String;)V\n    .registers 4\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarViewSettingsController;->callBacks:Ljava/util/ArrayList;\n\n    invoke-virtual {v0}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;\n\n    move-result-object v0\n\n    :goto_0\n    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z\n\n    move-result v1\n\n    if-eqz v1, :cond_0\n\n    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;\n\n    move-result-object v1\n\n    check-cast v1, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarViewSettingsController$CallBack;\n\n    invoke-interface {v1, p1}, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarViewSettingsController$CallBack;->onSettingsChange(Ljava/lang/String;)V\n\n    goto :goto_0\n\n    :cond_0\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
