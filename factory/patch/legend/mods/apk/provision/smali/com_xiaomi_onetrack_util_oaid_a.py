TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/util/oaid/a.smali'
CLASS_FALLBACK_NAMES = ['a.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field private static final a:Ljava/lang/String; = "a"']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_util_oaid_a__class_delete',
        'type': 'class_delete',
        'search': """.class public Lcom/xiaomi/onetrack/util/oaid/a;
.super Ljava/lang/Object;


# static fields
.field private static final a:Ljava/lang/String; = "a"

.field private static volatile b:Lcom/xiaomi/onetrack/util/oaid/a;

.field private static d:J


# instance fields
.field private volatile c:Ljava/lang/String;

.field private final e:I

.field private volatile f:I

.field private g:Z


# direct methods
.method static constructor <clinit>()V
    .registers 0

    return-void
.end method

.method public constructor <init>()V
    .registers 2

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    const-string v0, ""

    iput-object v0, p0, Lcom/xiaomi/onetrack/util/oaid/a;->c:Ljava/lang/String;

    const/4 v0, 0x3

    iput v0, p0, Lcom/xiaomi/onetrack/util/oaid/a;->e:I

    const/4 v0, 0x0

    iput v0, p0, Lcom/xiaomi/onetrack/util/oaid/a;->f:I

    iput-boolean v0, p0, Lcom/xiaomi/onetrack/util/oaid/a;->g:Z

    return-void
.end method

.method public static a()Lcom/xiaomi/onetrack/util/oaid/a;
    .registers 2

    sget-object v0, Lcom/xiaomi/onetrack/util/oaid/a;->b:Lcom/xiaomi/onetrack/util/oaid/a;

    if-nez v0, :cond_1

    const-class v0, Lcom/xiaomi/onetrack/util/oaid/a;

    monitor-enter v0

    :try_start_0
    sget-object v1, Lcom/xiaomi/onetrack/util/oaid/a;->b:Lcom/xiaomi/onetrack/util/oaid/a;

    if-nez v1, :cond_0

    new-instance v1, Lcom/xiaomi/onetrack/util/oaid/a;

    invoke-direct {v1}, Lcom/xiaomi/onetrack/util/oaid/a;-><init>()V

    sput-object v1, Lcom/xiaomi/onetrack/util/oaid/a;->b:Lcom/xiaomi/onetrack/util/oaid/a;

    goto :goto_0

    :catchall_0
    move-exception v1

    goto :goto_1

    :cond_0
    :goto_0
    monitor-exit v0

    goto :goto_2

    :goto_1
    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    throw v1

    :cond_1
    :goto_2
    sget-object v0, Lcom/xiaomi/onetrack/util/oaid/a;->b:Lcom/xiaomi/onetrack/util/oaid/a;

    return-object v0
.end method

.method private d()Z
    .registers 10

    iget v0, p0, Lcom/xiaomi/onetrack/util/oaid/a;->f:I

    const/4 v1, 0x1

    const/4 v2, 0x3

    if-le v0, v2, :cond_0

    return v1

    :cond_0
    invoke-static {}, Landroid/os/SystemClock;->elapsedRealtime()J

    move-result-wide v3

    sget-wide v5, Lcom/xiaomi/onetrack/util/oaid/a;->d:J

    sub-long v5, v3, v5

    invoke-static {v5, v6}, Ljava/lang/Math;->abs(J)J

    move-result-wide v5

    iget v0, p0, Lcom/xiaomi/onetrack/util/oaid/a;->f:I

    if-ne v0, v1, :cond_1

    const-wide/16 v7, 0xbb8

    cmp-long v0, v5, v7

    if-gez v0, :cond_3

    return v1

    :cond_1
    iget v0, p0, Lcom/xiaomi/onetrack/util/oaid/a;->f:I

    const/4 v7, 0x2

    if-ne v0, v7, :cond_2

    const-wide/16 v7, 0x2710

    cmp-long v0, v5, v7

    if-gez v0, :cond_3

    return v1

    :cond_2
    iget v0, p0, Lcom/xiaomi/onetrack/util/oaid/a;->f:I

    if-ne v0, v2, :cond_3

    const-wide/32 v7, 0xea60

    cmp-long v0, v5, v7

    if-gez v0, :cond_3

    return v1

    :cond_3
    sget-object v0, Lcom/xiaomi/onetrack/util/oaid/a;->a:Ljava/lang/String;

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "get time："

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget p0, p0, Lcom/xiaomi/onetrack/util/oaid/a;->f:I

    invoke-virtual {v1, p0}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    invoke-static {v0, p0}, Lcom/xiaomi/onetrack/util/p;->a(Ljava/lang/String;Ljava/lang/String;)V

    sput-wide v3, Lcom/xiaomi/onetrack/util/oaid/a;->d:J

    const/4 p0, 0x0

    return p0
.end method


# virtual methods
.method public a(Landroid/content/Context;)Ljava/lang/String;
    .registers 5

    iget-object v0, p0, Lcom/xiaomi/onetrack/util/oaid/a;->c:Ljava/lang/String;

    monitor-enter v0

    :try_start_0
    invoke-static {}, Lcom/xiaomi/onetrack/util/w;->a()Z

    move-result v1

    if-eqz v1, :cond_1

    sget-boolean p0, Lcom/xiaomi/onetrack/util/p;->a:Z

    if-nez p0, :cond_0

    sget-object p0, Lcom/xiaomi/onetrack/util/oaid/a;->a:Ljava/lang/String;

    const-string p1, "getOaid() throw exception : Don\'t use it on the main thread"

    invoke-static {p0, p1}, Lcom/xiaomi/onetrack/util/p;->b(Ljava/lang/String;Ljava/lang/String;)V

    const-string p0, ""

    monitor-exit v0

    return-object p0

    :catchall_0
    move-exception p0

    goto :goto_0

    :cond_0
    new-instance p0, Ljava/lang/IllegalStateException;

    const-string p1, "Don\'t use it on the main thread"

    invoke-direct {p0, p1}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    throw p0

    :cond_1
    iget-object v1, p0, Lcom/xiaomi/onetrack/util/oaid/a;->c:Ljava/lang/String;

    if-eqz v1, :cond_2

    iget-object v1, p0, Lcom/xiaomi/onetrack/util/oaid/a;->c:Ljava/lang/String;

    const-string v2, ""

    invoke-virtual {v1, v2}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-nez v1, :cond_2

    iget-object p0, p0, Lcom/xiaomi/onetrack/util/oaid/a;->c:Ljava/lang/String;

    monitor-exit v0

    return-object p0

    :cond_2
    invoke-direct {p0}, Lcom/xiaomi/onetrack/util/oaid/a;->d()Z

    move-result v1

    if-eqz v1, :cond_3

    sget-object p1, Lcom/xiaomi/onetrack/util/oaid/a;->a:Ljava/lang/String;

    const-string v1, "isNotAllowedGetOaid"

    invoke-static {p1, v1}, Lcom/xiaomi/onetrack/util/p;->a(Ljava/lang/String;Ljava/lang/String;)V

    iget-object p0, p0, Lcom/xiaomi/onetrack/util/oaid/a;->c:Ljava/lang/String;

    monitor-exit v0

    return-object p0

    :cond_3
    invoke-static {}, Lcom/xiaomi/onetrack/util/q;->a()Z

    move-result v1

    if-eqz v1, :cond_4

    invoke-static {p1}, Lcom/xiaomi/onetrack/util/n;->a(Landroid/content/Context;)Ljava/lang/String;

    move-result-object p1

    iput-object p1, p0, Lcom/xiaomi/onetrack/util/oaid/a;->c:Ljava/lang/String;

    iget p1, p0, Lcom/xiaomi/onetrack/util/oaid/a;->f:I

    add-int/lit8 p1, p1, 0x1

    iput p1, p0, Lcom/xiaomi/onetrack/util/oaid/a;->f:I

    iget-object p0, p0, Lcom/xiaomi/onetrack/util/oaid/a;->c:Ljava/lang/String;

    monitor-exit v0

    return-object p0

    :cond_4
    iget-boolean v1, p0, Lcom/xiaomi/onetrack/util/oaid/a;->g:Z

    if-nez v1, :cond_5

    new-instance v1, Lcom/xiaomi/onetrack/util/oaid/helpers/g;

    invoke-direct {v1}, Lcom/xiaomi/onetrack/util/oaid/helpers/g;-><init>()V

    invoke-virtual {v1, p1}, Lcom/xiaomi/onetrack/util/oaid/helpers/g;->a(Landroid/content/Context;)Ljava/lang/String;

    move-result-object v1

    if-eqz v1, :cond_5

    const-string v2, ""

    invoke-virtual {v1, v2}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v2

    if-nez v2, :cond_5

    iput-object v1, p0, Lcom/xiaomi/onetrack/util/oaid/a;->c:Ljava/lang/String;

    iget p1, p0, Lcom/xiaomi/onetrack/util/oaid/a;->f:I

    add-int/lit8 p1, p1, 0x1

    iput p1, p0, Lcom/xiaomi/onetrack/util/oaid/a;->f:I

    monitor-exit v0

    return-object v1

    :cond_5
    new-instance v1, Lcom/xiaomi/onetrack/util/oaid/helpers/b;

    invoke-direct {v1}, Lcom/xiaomi/onetrack/util/oaid/helpers/b;-><init>()V

    invoke-virtual {v1, p1}, Lcom/xiaomi/onetrack/util/oaid/helpers/b;->a(Landroid/content/Context;)Ljava/lang/String;

    move-result-object p1

    if-eqz p1, :cond_6

    const-string v1, ""

    invoke-virtual {p1, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-nez v1, :cond_6

    iput-object p1, p0, Lcom/xiaomi/onetrack/util/oaid/a;->c:Ljava/lang/String;

    iget v1, p0, Lcom/xiaomi/onetrack/util/oaid/a;->f:I

    add-int/lit8 v1, v1, 0x1

    iput v1, p0, Lcom/xiaomi/onetrack/util/oaid/a;->f:I

    monitor-exit v0

    return-object p1

    :cond_6
    iget p1, p0, Lcom/xiaomi/onetrack/util/oaid/a;->f:I

    add-int/lit8 p1, p1, 0x1

    iput p1, p0, Lcom/xiaomi/onetrack/util/oaid/a;->f:I

    iget-object p0, p0, Lcom/xiaomi/onetrack/util/oaid/a;->c:Ljava/lang/String;

    monitor-exit v0

    return-object p0

    :goto_0
    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    throw p0
.end method
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
