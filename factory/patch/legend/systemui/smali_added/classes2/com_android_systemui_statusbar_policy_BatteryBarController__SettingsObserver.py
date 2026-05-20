"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/statusbar/policy/BatteryBarController$SettingsObserver.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/statusbar/policy/BatteryBarController$SettingsObserver.smali'
CLASS_FALLBACK_NAMES = ['BatteryBarController$SettingsObserver.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_statusbar_policy_BatteryBarController$S',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/statusbar/policy/BatteryBarController$SettingsObserver;\n.super Landroid/database/ContentObserver;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingClass;\n    value = Lcom/android/systemui/statusbar/policy/BatteryBarController;\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = "SettingsObserver"\n.end annotation\n\n\n# instance fields\n.field final synthetic this$0:Lcom/android/systemui/statusbar/policy/BatteryBarController;\n\n\n# direct methods\n.method public constructor <init>(Lcom/android/systemui/statusbar/policy/BatteryBarController;Landroid/os/Handler;)V\n    .registers 3\n\n    iput-object p1, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController$SettingsObserver;->this$0:Lcom/android/systemui/statusbar/policy/BatteryBarController;\n\n    invoke-direct {p0, p2}, Landroid/database/ContentObserver;-><init>(Landroid/os/Handler;)V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method observe()V\n    .registers 4\n\n    goto :goto_b\n\n    nop\n\n    :goto_0\n    const-string v1, "battery_bar_thickness"\n\n    goto :goto_5\n\n    nop\n\n    :goto_1\n    invoke-virtual {v0, v1, v2, p0}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V\n\n    goto :goto_0\n\n    nop\n\n    :goto_2\n    invoke-static {v1}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;\n\n    move-result-object v1\n\n    goto :goto_1\n\n    nop\n\n    :goto_3\n    invoke-virtual {v1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;\n\n    move-result-object v0\n\n    goto :goto_a\n\n    nop\n\n    :goto_4\n    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController$SettingsObserver;->this$0:Lcom/android/systemui/statusbar/policy/BatteryBarController;\n\n    goto :goto_7\n\n    nop\n\n    :goto_5\n    invoke-static {v1}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;\n\n    move-result-object v1\n\n    goto :goto_9\n\n    nop\n\n    :goto_6\n    return-void\n\n    :goto_7\n    invoke-static {v1}, Lcom/android/systemui/statusbar/policy/BatteryBarController;->access$000(Lcom/android/systemui/statusbar/policy/BatteryBarController;)Landroid/content/Context;\n\n    move-result-object v1\n\n    goto :goto_3\n\n    nop\n\n    :goto_8\n    const-string v1, "battery_bar_style"\n\n    goto :goto_2\n\n    nop\n\n    :goto_9\n    invoke-virtual {v0, v1, v2, p0}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V\n\n    goto :goto_6\n\n    nop\n\n    :goto_a\n    const-string v1, "battery_bar"\n\n    goto :goto_d\n\n    nop\n\n    :goto_b\n    const/4 v2, 0x0\n\n    goto :goto_4\n\n    nop\n\n    :goto_c\n    invoke-virtual {v0, v1, v2, p0}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V\n\n    goto :goto_8\n\n    nop\n\n    :goto_d\n    invoke-static {v1}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;\n\n    move-result-object v1\n\n    goto :goto_c\n\n    nop\n.end method\n\n.method public onChange(Z)V\n    .registers 3\n\n    iget-object v0, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController$SettingsObserver;->this$0:Lcom/android/systemui/statusbar/policy/BatteryBarController;\n\n    invoke-virtual {v0}, Lcom/android/systemui/statusbar/policy/BatteryBarController;->updateSettings()V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
