TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/api/c.smali'
CLASS_FALLBACK_NAMES = ['c.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_api_c__class_delete',
        'type': 'class_delete',
        'search': """.class public Lcom/xiaomi/onetrack/api/c;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/xiaomi/onetrack/api/c$a;
    }
.end annotation


# static fields
.field private static b:Ljava/lang/String; = "onetrack_broadcast_manager"

.field private static volatile c:Lcom/xiaomi/onetrack/api/c;

.field private static volatile h:Z

.field private static volatile j:Z


# instance fields
.field private d:Landroid/os/Handler;

.field private i:Ljava/util/concurrent/CopyOnWriteArrayList;

.field private k:Ljava/util/concurrent/atomic/AtomicBoolean;

.field private l:Z

.field private m:Z

.field private n:Landroid/content/BroadcastReceiver;

.field private o:Landroid/content/BroadcastReceiver;


# direct methods
.method static constructor <clinit>()V
    .registers 0

    return-void
.end method

.method private constructor <init>()V
    .registers 4

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    new-instance v0, Ljava/util/concurrent/CopyOnWriteArrayList;

    invoke-direct {v0}, Ljava/util/concurrent/CopyOnWriteArrayList;-><init>()V

    iput-object v0, p0, Lcom/xiaomi/onetrack/api/c;->i:Ljava/util/concurrent/CopyOnWriteArrayList;

    new-instance v0, Ljava/util/concurrent/atomic/AtomicBoolean;

    const/4 v1, 0x0

    invoke-direct {v0, v1}, Ljava/util/concurrent/atomic/AtomicBoolean;-><init>(Z)V

    iput-object v0, p0, Lcom/xiaomi/onetrack/api/c;->k:Ljava/util/concurrent/atomic/AtomicBoolean;

    iput-boolean v1, p0, Lcom/xiaomi/onetrack/api/c;->l:Z

    iput-boolean v1, p0, Lcom/xiaomi/onetrack/api/c;->m:Z

    new-instance v0, Lcom/xiaomi/onetrack/api/d;

    invoke-direct {v0, p0}, Lcom/xiaomi/onetrack/api/d;-><init>(Lcom/xiaomi/onetrack/api/c;)V

    iput-object v0, p0, Lcom/xiaomi/onetrack/api/c;->n:Landroid/content/BroadcastReceiver;

    new-instance v0, Lcom/xiaomi/onetrack/api/e;

    invoke-direct {v0, p0}, Lcom/xiaomi/onetrack/api/e;-><init>(Lcom/xiaomi/onetrack/api/c;)V

    iput-object v0, p0, Lcom/xiaomi/onetrack/api/c;->o:Landroid/content/BroadcastReceiver;

    :try_start_0
    new-instance v0, Landroid/os/HandlerThread;

    sget-object v1, Lcom/xiaomi/onetrack/api/c;->b:Ljava/lang/String;

    invoke-direct {v0, v1}, Landroid/os/HandlerThread;-><init>(Ljava/lang/String;)V

    invoke-virtual {v0}, Landroid/os/HandlerThread;->start()V

    new-instance v1, Lcom/xiaomi/onetrack/api/c$a;

    invoke-virtual {v0}, Landroid/os/HandlerThread;->getLooper()Landroid/os/Looper;

    move-result-object v0

    const/4 v2, 0x0

    invoke-direct {v1, p0, v0, v2}, Lcom/xiaomi/onetrack/api/c$a;-><init>(Lcom/xiaomi/onetrack/api/c;Landroid/os/Looper;Lcom/xiaomi/onetrack/api/d;)V

    iput-object v1, p0, Lcom/xiaomi/onetrack/api/c;->d:Landroid/os/Handler;
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    :catchall_0
    return-void
.end method

.method static synthetic a(Lcom/xiaomi/onetrack/api/c;)Landroid/os/Handler;
    .registers 1

    iget-object p0, p0, Lcom/xiaomi/onetrack/api/c;->d:Landroid/os/Handler;

    return-object p0
.end method

.method public static a()Lcom/xiaomi/onetrack/api/c;
    .registers 1

    sget-object v0, Lcom/xiaomi/onetrack/api/c;->c:Lcom/xiaomi/onetrack/api/c;

    if-nez v0, :cond_0

    invoke-static {}, Lcom/xiaomi/onetrack/api/c;->b()V

    :cond_0
    sget-object v0, Lcom/xiaomi/onetrack/api/c;->c:Lcom/xiaomi/onetrack/api/c;

    return-object v0
.end method

.method private a(I)V
    .registers 4

    iget-object p0, p0, Lcom/xiaomi/onetrack/api/c;->i:Ljava/util/concurrent/CopyOnWriteArrayList;

    invoke-virtual {p0}, Ljava/util/concurrent/CopyOnWriteArrayList;->iterator()Ljava/util/Iterator;

    move-result-object p0

    :cond_0
    :goto_0
    invoke-interface {p0}, Ljava/util/Iterator;->hasNext()Z

    move-result v0

    if-eqz v0, :cond_2

    invoke-interface {p0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/xiaomi/onetrack/api/j;

    const/16 v1, 0x64

    if-ne p1, v1, :cond_1

    const/4 v1, 0x1

    invoke-interface {v0, v1}, Lcom/xiaomi/onetrack/api/j;->a(Z)V

    goto :goto_0

    :cond_1
    const/16 v1, 0x65

    if-ne p1, v1, :cond_0

    const/4 v1, 0x0

    invoke-interface {v0, v1}, Lcom/xiaomi/onetrack/api/j;->a(Z)V

    goto :goto_0

    :cond_2
    return-void
.end method

.method static synthetic a(Lcom/xiaomi/onetrack/api/c;I)V
    .registers 2

    invoke-direct {p0, p1}, Lcom/xiaomi/onetrack/api/c;->a(I)V

    return-void
.end method

.method static synthetic b(Lcom/xiaomi/onetrack/api/c;)Ljava/util/concurrent/atomic/AtomicBoolean;
    .registers 1

    iget-object p0, p0, Lcom/xiaomi/onetrack/api/c;->k:Ljava/util/concurrent/atomic/AtomicBoolean;

    return-object p0
.end method

.method public static b()V
    .registers 2

    sget-object v0, Lcom/xiaomi/onetrack/api/c;->c:Lcom/xiaomi/onetrack/api/c;

    if-nez v0, :cond_1

    const-class v0, Lcom/xiaomi/onetrack/api/c;

    monitor-enter v0

    :try_start_0
    sget-object v1, Lcom/xiaomi/onetrack/api/c;->c:Lcom/xiaomi/onetrack/api/c;

    if-nez v1, :cond_0

    new-instance v1, Lcom/xiaomi/onetrack/api/c;

    invoke-direct {v1}, Lcom/xiaomi/onetrack/api/c;-><init>()V

    sput-object v1, Lcom/xiaomi/onetrack/api/c;->c:Lcom/xiaomi/onetrack/api/c;

    goto :goto_0

    :catchall_0
    move-exception v1

    goto :goto_1

    :cond_0
    :goto_0
    monitor-exit v0

    return-void

    :goto_1
    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    throw v1

    :cond_1
    return-void
.end method

.method static synthetic c(Lcom/xiaomi/onetrack/api/c;)Z
    .registers 1

    iget-boolean p0, p0, Lcom/xiaomi/onetrack/api/c;->l:Z

    return p0
.end method

.method static synthetic d(Lcom/xiaomi/onetrack/api/c;)Z
    .registers 1

    iget-boolean p0, p0, Lcom/xiaomi/onetrack/api/c;->m:Z

    return p0
.end method

.method private g()V
    .registers 3

    new-instance v0, Landroid/content/IntentFilter;

    invoke-direct {v0}, Landroid/content/IntentFilter;-><init>()V

    const-string v1, "android.intent.action.SCREEN_ON"

    invoke-virtual {v0, v1}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    const-string v1, "android.intent.action.SCREEN_OFF"

    invoke-virtual {v0, v1}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    invoke-static {}, Lcom/xiaomi/onetrack/f/a;->b()Landroid/content/Context;

    move-result-object v1

    iget-object p0, p0, Lcom/xiaomi/onetrack/api/c;->n:Landroid/content/BroadcastReceiver;

    invoke-virtual {v1, p0, v0}, Landroid/content/Context;->registerReceiver(Landroid/content/BroadcastReceiver;Landroid/content/IntentFilter;)Landroid/content/Intent;

    const-string p0, "BroadcastManager"

    invoke-static {p0}, Lcom/xiaomi/onetrack/util/p;->a(Ljava/lang/String;)Ljava/lang/String;

    move-result-object p0

    const-string v0, "register screen receiver"

    invoke-static {p0, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    return-void
.end method

.method private h()V
    .registers 3

    new-instance v0, Landroid/content/IntentFilter;

    invoke-direct {v0}, Landroid/content/IntentFilter;-><init>()V

    const-string v1, "android.net.conn.CONNECTIVITY_CHANGE"

    invoke-virtual {v0, v1}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    invoke-static {}, Lcom/xiaomi/onetrack/f/a;->b()Landroid/content/Context;

    move-result-object v1

    iget-object p0, p0, Lcom/xiaomi/onetrack/api/c;->o:Landroid/content/BroadcastReceiver;

    invoke-virtual {v1, p0, v0}, Landroid/content/Context;->registerReceiver(Landroid/content/BroadcastReceiver;Landroid/content/IntentFilter;)Landroid/content/Intent;

    const-string p0, "BroadcastManager"

    invoke-static {p0}, Lcom/xiaomi/onetrack/util/p;->a(Ljava/lang/String;)Ljava/lang/String;

    move-result-object p0

    const-string v0, "register net receiver"

    invoke-static {p0, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    return-void
.end method


# virtual methods
.method public a(Lcom/xiaomi/onetrack/api/j;)V
    .registers 3

    iget-object v0, p0, Lcom/xiaomi/onetrack/api/c;->i:Ljava/util/concurrent/CopyOnWriteArrayList;

    invoke-virtual {v0, p1}, Ljava/util/concurrent/CopyOnWriteArrayList;->contains(Ljava/lang/Object;)Z

    move-result v0

    if-nez v0, :cond_0

    iget-object p0, p0, Lcom/xiaomi/onetrack/api/c;->i:Ljava/util/concurrent/CopyOnWriteArrayList;

    invoke-virtual {p0, p1}, Ljava/util/concurrent/CopyOnWriteArrayList;->add(Ljava/lang/Object;)Z

    :cond_0
    return-void
.end method

.method public c()V
    .registers 2

    const/4 v0, 0x1

    iput-boolean v0, p0, Lcom/xiaomi/onetrack/api/c;->l:Z

    return-void
.end method

.method public d()V
    .registers 2

    const/4 v0, 0x1

    iput-boolean v0, p0, Lcom/xiaomi/onetrack/api/c;->m:Z

    return-void
.end method

.method public e()V
    .registers 2

    sget-boolean v0, Lcom/xiaomi/onetrack/api/c;->h:Z

    if-nez v0, :cond_0

    const/4 v0, 0x1

    sput-boolean v0, Lcom/xiaomi/onetrack/api/c;->h:Z

    :try_start_0
    invoke-direct {p0}, Lcom/xiaomi/onetrack/api/c;->g()V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    return-void

    :catchall_0
    const/4 p0, 0x0

    sput-boolean p0, Lcom/xiaomi/onetrack/api/c;->h:Z

    :cond_0
    return-void
.end method

.method public f()V
    .registers 4

    sget-boolean v0, Lcom/xiaomi/onetrack/api/c;->j:Z

    if-nez v0, :cond_0

    const/4 v0, 0x1

    sput-boolean v0, Lcom/xiaomi/onetrack/api/c;->j:Z

    invoke-static {}, Lcom/xiaomi/onetrack/g/c;->b()Z

    move-result v0

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "Get network status for the first time, isNetworkConnected: "

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v1, v0}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    const-string v2, "BroadcastManager"

    invoke-static {v2, v1}, Lcom/xiaomi/onetrack/util/p;->a(Ljava/lang/String;Ljava/lang/String;)V

    invoke-static {v0}, Lcom/xiaomi/onetrack/b/n;->b(Z)V

    :try_start_0
    invoke-direct {p0}, Lcom/xiaomi/onetrack/api/c;->h()V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    return-void

    :catchall_0
    const/4 p0, 0x0

    sput-boolean p0, Lcom/xiaomi/onetrack/api/c;->j:Z

    :cond_0
    return-void
.end method
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
