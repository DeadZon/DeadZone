"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/statusbar/phone/RefreshMezoStatusbar.smali'
CLASS_FALLBACK_NAMES = ['RefreshMezoStatusbar.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/statusbar/phone/RefreshMezoStatusbar;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/android/systemui/statusbar/phone/RefreshMezoStatusbar$1;
    }
.end annotation


# static fields
.field private static final instance:Lcom/android/systemui/statusbar/phone/RefreshMezoStatusbar;


# instance fields
.field surfaces:Lcom/android/systemui/statusbar/phone/CentralSurfacesImpl;


# direct methods
.method static constructor <clinit>()V
    .registers 1

    new-instance v0, Lcom/android/systemui/statusbar/phone/RefreshMezoStatusbar;

    invoke-direct {v0}, Lcom/android/systemui/statusbar/phone/RefreshMezoStatusbar;-><init>()V

    sput-object v0, Lcom/android/systemui/statusbar/phone/RefreshMezoStatusbar;->instance:Lcom/android/systemui/statusbar/phone/RefreshMezoStatusbar;

    return-void
.end method

.method public constructor <init>()V
    .registers 1

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method static forceStopPackage(Ljava/lang/String;Landroid/app/ActivityManager;)V
    .registers 9

    :try_start_0
    const-class v2, Landroid/app/ActivityManager;

    const-string v3, "forceStopPackage"

    const/4 v4, 0x1

    new-array v4, v4, [Ljava/lang/Class;

    const/4 v5, 0x0

    const-class v6, Ljava/lang/String;

    aput-object v6, v4, v5

    invoke-virtual {v2, v3, v4}, Ljava/lang/Class;->getMethod(Ljava/lang/String;[Ljava/lang/Class;)Ljava/lang/reflect/Method;

    move-result-object v1

    const/4 v2, 0x1

    new-array v2, v2, [Ljava/lang/Object;

    const/4 v3, 0x0

    aput-object p0, v2, v3

    invoke-virtual {v1, p1, v2}, Ljava/lang/reflect/Method;->invoke(Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object;
    :try_end_19
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_19} :catch_1a

    :goto_19
    return-void

    :catch_1a
    move-exception v0

    const-string v2, "Mezologs"

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    const-string v4, "forceStopPackage: "

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-static {v2, v3}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_19
.end method

.method public static getInstance()Lcom/android/systemui/statusbar/phone/RefreshMezoStatusbar;
    .registers 1

    sget-object v0, Lcom/android/systemui/statusbar/phone/RefreshMezoStatusbar;->instance:Lcom/android/systemui/statusbar/phone/RefreshMezoStatusbar;

    return-object v0
.end method

.method private getIntentFilter()Landroid/content/IntentFilter;
    .registers 3

    new-instance v0, Landroid/content/IntentFilter;

    invoke-direct {v0}, Landroid/content/IntentFilter;-><init>()V

    const-string v1, "my.intent.action.REFRESH_STATUSBAR"

    invoke-virtual {v0, v1}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    const-string v1, "my.intent.action.REFRESH_SYSTEMUI"

    invoke-virtual {v0, v1}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    const-string v1, "my.intent.action.REFRESH_SPOOF"

    invoke-virtual {v0, v1}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    const-string v1, "my.intent.action.KILL_VAULT"

    invoke-virtual {v0, v1}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    return-object v0
.end method


# virtual methods
.method public register(Lcom/android/systemui/statusbar/phone/CentralSurfacesImpl;)V
    .registers 7

    iput-object p1, p0, Lcom/android/systemui/statusbar/phone/RefreshMezoStatusbar;->surfaces:Lcom/android/systemui/statusbar/phone/CentralSurfacesImpl;

    const/4 v0, 0x0

    iget-object v1, p0, Lcom/android/systemui/statusbar/phone/RefreshMezoStatusbar;->surfaces:Lcom/android/systemui/statusbar/phone/CentralSurfacesImpl;

    iget-object v1, v1, Lcom/android/systemui/statusbar/phone/CentralSurfacesImpl;->mBroadcastDispatcher:Lcom/android/systemui/broadcast/BroadcastDispatcher;

    new-instance v2, Lcom/android/systemui/statusbar/phone/RefreshMezoStatusbar$1;

    iget-object v3, p0, Lcom/android/systemui/statusbar/phone/RefreshMezoStatusbar;->surfaces:Lcom/android/systemui/statusbar/phone/CentralSurfacesImpl;

    invoke-direct {v2, v3}, Lcom/android/systemui/statusbar/phone/RefreshMezoStatusbar$1;-><init>(Lcom/android/systemui/statusbar/phone/CentralSurfacesImpl;)V

    invoke-direct {p0}, Lcom/android/systemui/statusbar/phone/RefreshMezoStatusbar;->getIntentFilter()Landroid/content/IntentFilter;

    move-result-object v3

    const/4 v4, 0x0

    invoke-virtual {v1, v2, v3, v4, v0}, Lcom/android/systemui/broadcast/BroadcastDispatcher;->registerReceiver(Landroid/content/BroadcastReceiver;Landroid/content/IntentFilter;Ljava/util/concurrent/Executor;Landroid/os/UserHandle;)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_statusbar_phone_RefreshMezoStatusbar',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
