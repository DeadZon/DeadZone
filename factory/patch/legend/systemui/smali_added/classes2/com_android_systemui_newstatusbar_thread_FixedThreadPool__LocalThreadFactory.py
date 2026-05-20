"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/thread/FixedThreadPool$LocalThreadFactory.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/thread/FixedThreadPool$LocalThreadFactory.smali'
CLASS_FALLBACK_NAMES = ['FixedThreadPool$LocalThreadFactory.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_thread_FixedThreadPool$Loc',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public Lcom/android/systemui/newstatusbar/thread/FixedThreadPool$LocalThreadFactory;\n.super Ljava/lang/Object;\n\n# interfaces\n.implements Ljava/util/concurrent/ThreadFactory;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingClass;\n    value = Lcom/android/systemui/newstatusbar/thread/FixedThreadPool;\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x9\n    name = "LocalThreadFactory"\n.end annotation\n\n\n# direct methods\n.method public constructor <init>()V\n    .registers 1\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public newThread(Ljava/lang/Runnable;)Ljava/lang/Thread;\n    .registers 3\n\n    new-instance v0, Ljava/lang/Thread;\n\n    invoke-direct {v0, p1}, Ljava/lang/Thread;-><init>(Ljava/lang/Runnable;)V\n\n    return-object v0\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
