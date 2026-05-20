"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/statusbar/policy/Prefs.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/statusbar/policy/Prefs.smali'
CLASS_FALLBACK_NAMES = ['Prefs.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_statusbar_policy_Prefs',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public Lcom/android/systemui/statusbar/policy/Prefs;\n.super Ljava/lang/Object;\n\n\n# static fields\n.field public static final GPS_ALERT_PREF:Ljava/lang/String; = "gps_alert_pref"\n\n.field public static final OUTDOOR_MODE_ALERT_PREF:Ljava/lang/String; = "outdoor_mode_alert_pref"\n\n.field private static final SHARED_PREFS_NAME:Ljava/lang/String; = "status_bar"\n\n\n# direct methods\n.method public constructor <init>()V\n    .registers 1\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n\n.method public static edit(Landroid/content/Context;)Landroid/content/SharedPreferences$Editor;\n    .registers 3\n\n    const-string v0, "status_bar"\n\n    const/4 v1, 0x0\n\n    invoke-virtual {p0, v0, v1}, Landroid/content/Context;->getSharedPreferences(Ljava/lang/String;I)Landroid/content/SharedPreferences;\n\n    move-result-object v0\n\n    invoke-interface {v0}, Landroid/content/SharedPreferences;->edit()Landroid/content/SharedPreferences$Editor;\n\n    move-result-object v0\n\n    return-object v0\n.end method\n\n.method public static getLastBatteryLevel(Landroid/content/Context;)I\n    .registers 4\n\n    invoke-static {p0}, Lcom/android/systemui/statusbar/policy/Prefs;->read(Landroid/content/Context;)Landroid/content/SharedPreferences;\n\n    move-result-object v0\n\n    const-string v1, "last_battery_level"\n\n    const/16 v2, 0x32\n\n    invoke-interface {v0, v1, v2}, Landroid/content/SharedPreferences;->getInt(Ljava/lang/String;I)I\n\n    move-result v0\n\n    return v0\n.end method\n\n.method public static read(Landroid/content/Context;)Landroid/content/SharedPreferences;\n    .registers 3\n\n    const-string v0, "status_bar"\n\n    const/4 v1, 0x0\n\n    invoke-virtual {p0, v0, v1}, Landroid/content/Context;->getSharedPreferences(Ljava/lang/String;I)Landroid/content/SharedPreferences;\n\n    move-result-object v0\n\n    return-object v0\n.end method\n\n.method public static setLastBatteryLevel(Landroid/content/Context;I)V\n    .registers 4\n\n    invoke-static {p0}, Lcom/android/systemui/statusbar/policy/Prefs;->edit(Landroid/content/Context;)Landroid/content/SharedPreferences$Editor;\n\n    move-result-object v0\n\n    const-string v1, "last_battery_level"\n\n    invoke-interface {v0, v1, p1}, Landroid/content/SharedPreferences$Editor;->putInt(Ljava/lang/String;I)Landroid/content/SharedPreferences$Editor;\n\n    move-result-object v0\n\n    invoke-interface {v0}, Landroid/content/SharedPreferences$Editor;->commit()Z\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
