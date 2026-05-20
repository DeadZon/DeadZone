"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/statusbar/views/MiuiStatusIconContainer$NfcSettingObserver.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/statusbar/views/MiuiStatusIconContainer$NfcSettingObserver.smali'
CLASS_FALLBACK_NAMES = ['MiuiStatusIconContainer$NfcSettingObserver.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_statusbar_views_MiuiStatusIconContainer',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public final Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer$NfcSettingObserver;\n.super Landroid/database/ContentObserver;\n\n\n# instance fields\n.field private final host:Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer;\n\n\n# direct methods\n.method public constructor <init>(Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer;Landroid/os/Handler;)V\n    .registers 3\n\n    iput-object p1, p0, Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer$NfcSettingObserver;->host:Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer;\n\n    invoke-direct {p0, p2}, Landroid/database/ContentObserver;-><init>(Landroid/os/Handler;)V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public onChange(Z)V\n    .registers 2\n\n    iget-object p1, p0, Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer$NfcSettingObserver;->host:Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer;\n\n    invoke-virtual {p1}, Landroid/view/View;->requestLayout()V\n\n    invoke-virtual {p1}, Landroid/view/View;->invalidate()V\n\n    return-void\n.end method\n\n.method public onChange(ZLandroid/net/Uri;)V\n    .registers 3\n\n    invoke-virtual {p0, p1}, Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer$NfcSettingObserver;->onChange(Z)V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
