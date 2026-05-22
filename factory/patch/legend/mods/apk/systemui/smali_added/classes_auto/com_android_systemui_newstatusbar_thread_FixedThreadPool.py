"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/thread/FixedThreadPool.smali'
CLASS_FALLBACK_NAMES = ['FixedThreadPool.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/thread/FixedThreadPool;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/android/systemui/newstatusbar/thread/FixedThreadPool$LocalThreadFactory;
    }
.end annotation


# static fields
.field private static final DEFAULT_MAX_THREAD_NUMBER:I = 0x6

.field private static final INSTANCE:Lcom/android/systemui/newstatusbar/thread/FixedThreadPool;


# instance fields
.field private final mService:Ljava/util/concurrent/ExecutorService;


# direct methods
.method static constructor <clinit>()V
    .registers 1

    new-instance v0, Lcom/android/systemui/newstatusbar/thread/FixedThreadPool;

    invoke-direct {v0}, Lcom/android/systemui/newstatusbar/thread/FixedThreadPool;-><init>()V

    sput-object v0, Lcom/android/systemui/newstatusbar/thread/FixedThreadPool;->INSTANCE:Lcom/android/systemui/newstatusbar/thread/FixedThreadPool;

    return-void
.end method

.method private constructor <init>()V
    .registers 3

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    new-instance v0, Lcom/android/systemui/newstatusbar/thread/FixedThreadPool$LocalThreadFactory;

    invoke-direct {v0}, Lcom/android/systemui/newstatusbar/thread/FixedThreadPool$LocalThreadFactory;-><init>()V

    const/4 v1, 0x6

    invoke-static {v1, v0}, Ljava/util/concurrent/Executors;->newFixedThreadPool(ILjava/util/concurrent/ThreadFactory;)Ljava/util/concurrent/ExecutorService;

    move-result-object v0

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/thread/FixedThreadPool;->mService:Ljava/util/concurrent/ExecutorService;

    return-void
.end method

.method public static getInstance()Lcom/android/systemui/newstatusbar/thread/FixedThreadPool;
    .registers 1

    sget-object v0, Lcom/android/systemui/newstatusbar/thread/FixedThreadPool;->INSTANCE:Lcom/android/systemui/newstatusbar/thread/FixedThreadPool;

    return-object v0
.end method


# virtual methods
.method public execute(Ljava/lang/Runnable;)V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/thread/FixedThreadPool;->mService:Ljava/util/concurrent/ExecutorService;

    invoke-interface {v0, p1}, Ljava/util/concurrent/ExecutorService;->execute(Ljava/lang/Runnable;)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_thread_FixedThreadPool',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
