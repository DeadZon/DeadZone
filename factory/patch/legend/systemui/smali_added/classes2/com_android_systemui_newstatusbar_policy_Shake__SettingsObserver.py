"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/policy/Shake$SettingsObserver.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/policy/Shake$SettingsObserver.smali'
CLASS_FALLBACK_NAMES = ['Shake$SettingsObserver.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_policy_Shake$SettingsObser',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/newstatusbar/policy/Shake$SettingsObserver;\n.super Landroid/database/ContentObserver;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingClass;\n    value = Lcom/android/systemui/newstatusbar/policy/Shake;\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = "SettingsObserver"\n.end annotation\n\n\n# instance fields\n.field final synthetic this$0:Lcom/android/systemui/newstatusbar/policy/Shake;\n\n\n# direct methods\n.method constructor <init>(Lcom/android/systemui/newstatusbar/policy/Shake;Landroid/os/Handler;)V\n    .registers 3\n\n    iput-object p1, p0, Lcom/android/systemui/newstatusbar/policy/Shake$SettingsObserver;->this$0:Lcom/android/systemui/newstatusbar/policy/Shake;\n\n    invoke-direct {p0, p2}, Landroid/database/ContentObserver;-><init>(Landroid/os/Handler;)V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method observe()V\n    .registers 4\n\n    goto :goto_1\n\n    nop\n\n    :goto_0\n    return-void\n\n    :goto_1\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/policy/Shake$SettingsObserver;->this$0:Lcom/android/systemui/newstatusbar/policy/Shake;\n\n    goto :goto_7\n\n    nop\n\n    :goto_2\n    invoke-static {v1}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;\n\n    move-result-object v1\n\n    goto :goto_5\n\n    nop\n\n    :goto_3\n    const-string v1, "shake_mobile"\n\n    goto :goto_2\n\n    nop\n\n    :goto_4\n    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;\n\n    move-result-object v0\n\n    goto :goto_3\n\n    nop\n\n    :goto_5\n    const/4 v2, 0x0\n\n    goto :goto_6\n\n    nop\n\n    :goto_6\n    invoke-virtual {v0, v1, v2, p0}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V\n\n    goto :goto_0\n\n    nop\n\n    :goto_7\n    iget-object v0, v0, Lcom/android/systemui/newstatusbar/policy/Shake;->mContext:Landroid/content/Context;\n\n    goto :goto_4\n\n    nop\n.end method\n\n.method public onChange(Z)V\n    .registers 4\n\n    const-string v0, "shake_mobile"\n\n    const/4 v1, 0x1\n\n    invoke-static {v0, v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I\n\n    move-result v0\n\n    if-lez v0, :cond_0\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/policy/Shake$SettingsObserver;->this$0:Lcom/android/systemui/newstatusbar/policy/Shake;\n\n    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/policy/Shake;->registerOnOffScreenListener()V\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/policy/Shake$SettingsObserver;->this$0:Lcom/android/systemui/newstatusbar/policy/Shake;\n\n    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/policy/Shake;->registerSensorListener()V\n\n    return-void\n\n    :cond_0\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/policy/Shake$SettingsObserver;->this$0:Lcom/android/systemui/newstatusbar/policy/Shake;\n\n    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/policy/Shake;->unregisterOnOffScreenListener()V\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/policy/Shake$SettingsObserver;->this$0:Lcom/android/systemui/newstatusbar/policy/Shake;\n\n    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/policy/Shake;->unregisterSensorListener()V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
