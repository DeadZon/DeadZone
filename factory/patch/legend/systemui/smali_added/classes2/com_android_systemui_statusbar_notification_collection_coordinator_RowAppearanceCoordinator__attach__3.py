"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator$attach$3.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator$attach$3.smali'
CLASS_FALLBACK_NAMES = ['RowAppearanceCoordinator$attach$3.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_statusbar_notification_collection_coord',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public final Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator$attach$3;\n.super Landroid/database/ContentObserver;\n\n\n# instance fields\n.field public final synthetic $tmp0:Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator;\n\n\n# direct methods\n.method public constructor <init>(Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator;Landroid/os/Handler;)V\n    .registers 3\n\n    iput-object p1, p0, Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator$attach$3;->$tmp0:Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator;\n\n    invoke-direct {p0, p2}, Landroid/database/ContentObserver;-><init>(Landroid/os/Handler;)V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public final onChange(Z)V\n    .registers 2\n\n    iget-object p0, p0, Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator$attach$3;->$tmp0:Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator;\n\n    invoke-virtual {p0}, Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator;->updateExpandTopNotification()V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
