"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/thread/ThreadUtils.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/thread/ThreadUtils.smali'
CLASS_FALLBACK_NAMES = ['ThreadUtils.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_thread_ThreadUtils',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public Lcom/android/systemui/newstatusbar/thread/ThreadUtils;\n.super Ljava/lang/Object;\n\n\n# annotations\n.annotation system Ldalvik/annotation/MemberClasses;\n    value = {\n        Lcom/android/systemui/newstatusbar/thread/ThreadUtils$HandlerHolder;\n    }\n.end annotation\n\n\n# direct methods\n.method private constructor <init>()V\n    .registers 1\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n\n.method public static getUiThreadHandler()Landroid/os/Handler;\n    .registers 1\n\n    sget-object v0, Lcom/android/systemui/newstatusbar/thread/ThreadUtils$HandlerHolder;->INSTANCE:Landroid/os/Handler;\n\n    return-object v0\n.end method\n\n.method public static postDelayedOnUiThread(Ljava/lang/Runnable;J)V\n    .registers 4\n\n    invoke-static {}, Lcom/android/systemui/newstatusbar/thread/ThreadUtils;->getUiThreadHandler()Landroid/os/Handler;\n\n    move-result-object v0\n\n    invoke-virtual {v0, p0, p1, p2}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z\n\n    return-void\n.end method\n\n.method public static postOnUiThread(Ljava/lang/Runnable;)V\n    .registers 2\n\n    invoke-static {}, Lcom/android/systemui/newstatusbar/thread/ThreadUtils;->getUiThreadHandler()Landroid/os/Handler;\n\n    move-result-object v0\n\n    invoke-virtual {v0, p0}, Landroid/os/Handler;->post(Ljava/lang/Runnable;)Z\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
