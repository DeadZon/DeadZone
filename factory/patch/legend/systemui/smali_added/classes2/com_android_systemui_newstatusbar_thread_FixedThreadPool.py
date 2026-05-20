"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/thread/FixedThreadPool.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/thread/FixedThreadPool.smali'
CLASS_FALLBACK_NAMES = ['FixedThreadPool.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_thread_FixedThreadPool',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public Lcom/android/systemui/newstatusbar/thread/FixedThreadPool;\n.super Ljava/lang/Object;\n\n\n# annotations\n.annotation system Ldalvik/annotation/MemberClasses;\n    value = {\n        Lcom/android/systemui/newstatusbar/thread/FixedThreadPool$LocalThreadFactory;\n    }\n.end annotation\n\n\n# static fields\n.field private static final DEFAULT_MAX_THREAD_NUMBER:I = 0x6\n\n.field private static final INSTANCE:Lcom/android/systemui/newstatusbar/thread/FixedThreadPool;\n\n\n# instance fields\n.field private final mService:Ljava/util/concurrent/ExecutorService;\n\n\n# direct methods\n.method static constructor <clinit>()V\n    .registers 1\n\n    new-instance v0, Lcom/android/systemui/newstatusbar/thread/FixedThreadPool;\n\n    invoke-direct {v0}, Lcom/android/systemui/newstatusbar/thread/FixedThreadPool;-><init>()V\n\n    sput-object v0, Lcom/android/systemui/newstatusbar/thread/FixedThreadPool;->INSTANCE:Lcom/android/systemui/newstatusbar/thread/FixedThreadPool;\n\n    return-void\n.end method\n\n.method private constructor <init>()V\n    .registers 3\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    new-instance v0, Lcom/android/systemui/newstatusbar/thread/FixedThreadPool$LocalThreadFactory;\n\n    invoke-direct {v0}, Lcom/android/systemui/newstatusbar/thread/FixedThreadPool$LocalThreadFactory;-><init>()V\n\n    const/4 v1, 0x6\n\n    invoke-static {v1, v0}, Ljava/util/concurrent/Executors;->newFixedThreadPool(ILjava/util/concurrent/ThreadFactory;)Ljava/util/concurrent/ExecutorService;\n\n    move-result-object v0\n\n    iput-object v0, p0, Lcom/android/systemui/newstatusbar/thread/FixedThreadPool;->mService:Ljava/util/concurrent/ExecutorService;\n\n    return-void\n.end method\n\n.method public static getInstance()Lcom/android/systemui/newstatusbar/thread/FixedThreadPool;\n    .registers 1\n\n    sget-object v0, Lcom/android/systemui/newstatusbar/thread/FixedThreadPool;->INSTANCE:Lcom/android/systemui/newstatusbar/thread/FixedThreadPool;\n\n    return-object v0\n.end method\n\n\n# virtual methods\n.method public execute(Ljava/lang/Runnable;)V\n    .registers 3\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/thread/FixedThreadPool;->mService:Ljava/util/concurrent/ExecutorService;\n\n    invoke-interface {v0, p1}, Ljava/util/concurrent/ExecutorService;->execute(Ljava/lang/Runnable;)V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
