"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/clock/ClockLayoutFactory.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/clock/ClockLayoutFactory.smali'
CLASS_FALLBACK_NAMES = ['ClockLayoutFactory.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_clock_ClockLayoutFactory',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public Lcom/android/systemui/newstatusbar/clock/ClockLayoutFactory;\n.super Ljava/lang/Object;\n\n\n# direct methods\n.method public constructor <init>()V\n    .registers 1\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n\n.method public static get(Lcom/android/systemui/newstatusbar/clock/ClockView;Z)Lcom/android/systemui/newstatusbar/clock/ClockLayout;\n    .registers 5\n\n    const/4 p1, 0x1\n\n    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockView;->getContext()Landroid/content/Context;\n\n    move-result-object v0\n\n    if-nez p1, :cond_1\n\n    const-string v1, "statusbar_clock_style"\n\n    const/4 v2, -0x5\n\n    invoke-static {v1, v2}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I\n\n    move-result v1\n\n    if-ne v1, v2, :cond_0\n\n    goto :goto_0\n\n    :cond_0\n    new-instance v1, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;\n\n    invoke-direct {v1, v0, p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;-><init>(Landroid/content/Context;Lcom/android/systemui/newstatusbar/clock/ClockView;)V\n\n    return-object v1\n\n    :cond_1\n    :goto_0\n    new-instance v1, Lcom/android/systemui/newstatusbar/clock/ClockLayout;\n\n    invoke-direct {v1, v0, p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;-><init>(Landroid/content/Context;Lcom/android/systemui/newstatusbar/clock/ClockView;)V\n\n    return-object v1\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
