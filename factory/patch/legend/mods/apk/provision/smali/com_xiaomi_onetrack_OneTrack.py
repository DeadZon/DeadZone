TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/OneTrack.smali'
CLASS_FALLBACK_NAMES = ['OneTrack.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_OneTrack__class_delete',
        'type': 'class_delete',
        'search': """.class public Lcom/xiaomi/onetrack/OneTrack;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/xiaomi/onetrack/OneTrack$NetType;,
        Lcom/xiaomi/onetrack/OneTrack$Mode;,
        Lcom/xiaomi/onetrack/OneTrack$IEventHook;,
        Lcom/xiaomi/onetrack/OneTrack$ICommonPropertyProvider;
    }
.end annotation


# static fields
.field private static a:Z

.field private static volatile b:I

.field private static c:Z

.field private static d:Z


# instance fields
.field private e:Lcom/xiaomi/onetrack/api/m;


# direct methods
.method static constructor <clinit>()V
    .registers 0

    return-void
.end method

.method private constructor <init>(Landroid/content/Context;Lcom/xiaomi/onetrack/Configuration;)V
    .registers 4

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    invoke-virtual {p1}, Landroid/content/Context;->getApplicationContext()Landroid/content/Context;

    move-result-object v0

    invoke-static {v0}, Lcom/xiaomi/onetrack/f/a;->a(Landroid/content/Context;)V

    new-instance v0, Lcom/xiaomi/onetrack/api/m;

    invoke-direct {v0, p1, p2}, Lcom/xiaomi/onetrack/api/m;-><init>(Landroid/content/Context;Lcom/xiaomi/onetrack/Configuration;)V

    iput-object v0, p0, Lcom/xiaomi/onetrack/OneTrack;->e:Lcom/xiaomi/onetrack/api/m;

    new-instance p1, Lcom/xiaomi/onetrack/DefaultEventHook;

    invoke-direct {p1}, Lcom/xiaomi/onetrack/DefaultEventHook;-><init>()V

    invoke-virtual {p0, p1}, Lcom/xiaomi/onetrack/OneTrack;->setEventHook(Lcom/xiaomi/onetrack/OneTrack$IEventHook;)V

    return-void
.end method

.method private static a(Landroid/content/Context;)V
    .registers 2

    if-eqz p0, :cond_0

    invoke-virtual {p0}, Landroid/content/Context;->getApplicationContext()Landroid/content/Context;

    move-result-object p0

    invoke-static {p0}, Lcom/xiaomi/onetrack/f/a;->a(Landroid/content/Context;)V

    return-void

    :cond_0
    new-instance p0, Ljava/lang/IllegalStateException;

    const-string v0, "context is null!"

    invoke-direct {p0, v0}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    throw p0
.end method

.method public static createInstance(Landroid/content/Context;Lcom/xiaomi/onetrack/Configuration;)Lcom/xiaomi/onetrack/OneTrack;
    .registers 3

    new-instance v0, Lcom/xiaomi/onetrack/OneTrack;

    invoke-direct {v0, p0, p1}, Lcom/xiaomi/onetrack/OneTrack;-><init>(Landroid/content/Context;Lcom/xiaomi/onetrack/Configuration;)V

    return-object v0
.end method

.method public static getGlobalBasicModeEnable()I
    .registers 1

    sget v0, Lcom/xiaomi/onetrack/OneTrack;->b:I

    return v0
.end method

.method public static isDisable()Z
    .registers 1

    sget-boolean v0, Lcom/xiaomi/onetrack/OneTrack;->a:Z

    return v0
.end method

.method public static isRestrictGetNetworkInfo()Z
    .registers 1

    sget-boolean v0, Lcom/xiaomi/onetrack/OneTrack;->d:Z

    return v0
.end method

.method public static isUseSystemNetTrafficOnly()Z
    .registers 1

    sget-boolean v0, Lcom/xiaomi/onetrack/OneTrack;->c:Z

    return v0
.end method

.method public static setAccessNetworkEnable(Landroid/content/Context;Z)V
    .registers 2

    invoke-static {p0}, Lcom/xiaomi/onetrack/OneTrack;->a(Landroid/content/Context;)V

    new-instance p0, Lcom/xiaomi/onetrack/OneTrack$1;

    invoke-direct {p0, p1}, Lcom/xiaomi/onetrack/OneTrack$1;-><init>(Z)V

    invoke-static {p0}, Lcom/xiaomi/onetrack/util/i;->a(Ljava/lang/Runnable;)V

    return-void
.end method

.method public static setDebugMode(Z)V
    .registers 1

    invoke-static {p0}, Lcom/xiaomi/onetrack/util/p;->a(Z)V

    return-void
.end method

.method public static setUseSystemNetTrafficOnly()V
    .registers 1

    const/4 v0, 0x1

    sput-boolean v0, Lcom/xiaomi/onetrack/OneTrack;->c:Z

    return-void
.end method


# virtual methods
.method public setEventHook(Lcom/xiaomi/onetrack/OneTrack$IEventHook;)V
    .registers 2

    iget-object p0, p0, Lcom/xiaomi/onetrack/OneTrack;->e:Lcom/xiaomi/onetrack/api/m;

    invoke-virtual {p0, p1}, Lcom/xiaomi/onetrack/api/m;->a(Lcom/xiaomi/onetrack/OneTrack$IEventHook;)V

    return-void
.end method

.method public track(Ljava/lang/String;Ljava/util/Map;)V
    .registers 3

    iget-object p0, p0, Lcom/xiaomi/onetrack/OneTrack;->e:Lcom/xiaomi/onetrack/api/m;

    invoke-virtual {p0, p1, p2}, Lcom/xiaomi/onetrack/api/m;->a(Ljava/lang/String;Ljava/util/Map;)V

    return-void
.end method
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
