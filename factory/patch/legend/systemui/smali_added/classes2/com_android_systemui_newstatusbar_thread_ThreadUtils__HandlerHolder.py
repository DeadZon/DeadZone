"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/thread/ThreadUtils$HandlerHolder.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/thread/ThreadUtils$HandlerHolder.smali'
CLASS_FALLBACK_NAMES = ['ThreadUtils$HandlerHolder.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_thread_ThreadUtils$Handler',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public Lcom/android/systemui/newstatusbar/thread/ThreadUtils$HandlerHolder;\n.super Ljava/lang/Object;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingClass;\n    value = Lcom/android/systemui/newstatusbar/thread/ThreadUtils;\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x9\n    name = "HandlerHolder"\n.end annotation\n\n\n# static fields\n.field public static final INSTANCE:Landroid/os/Handler;\n\n\n# direct methods\n.method static constructor <clinit>()V\n    .registers 2\n\n    new-instance v0, Landroid/os/Handler;\n\n    invoke-static {}, Landroid/os/Looper;->getMainLooper()Landroid/os/Looper;\n\n    move-result-object v1\n\n    invoke-direct {v0, v1}, Landroid/os/Handler;-><init>(Landroid/os/Looper;)V\n\n    sput-object v0, Lcom/android/systemui/newstatusbar/thread/ThreadUtils$HandlerHolder;->INSTANCE:Landroid/os/Handler;\n\n    return-void\n.end method\n\n.method private constructor <init>()V\n    .registers 1\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
