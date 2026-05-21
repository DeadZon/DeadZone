TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/utils/RequestThread.smali'
CLASS_FALLBACK_NAMES = ['RequestThread.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Thread;', '.field private static final REQUEST_INTERVAL_TIME:I = 0xfa0', '.field private static final REQUREST_MAX_ERROR:I = 0x3', '.field private static final TAG:Ljava/lang/String; = "RequestThread"']

PATCHES = [
    {
        'id': 'com_android_provision_utils_RequestThread__class_delete',
        'type': 'class_delete',
        'search': """.class public Lcom/android/provision/utils/RequestThread;
.super Ljava/lang/Thread;


# static fields
.field private static final REQUEST_INTERVAL_TIME:I = 0xfa0

.field private static final REQUREST_MAX_ERROR:I = 0x3

.field private static final TAG:Ljava/lang/String; = "RequestThread"


# instance fields
.field private mContextRef:Ljava/lang/ref/WeakReference;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/lang/ref/WeakReference<",
            "Landroid/content/Context;",
            ">;"
        }
    .end annotation
.end field

.field private url:Ljava/lang/String;


# direct methods
.method public constructor <init>(Ljava/lang/String;Landroid/content/Context;)V
    .registers 3

    invoke-direct {p0}, Ljava/lang/Thread;-><init>()V

    iput-object p1, p0, Lcom/android/provision/utils/RequestThread;->url:Ljava/lang/String;

    new-instance p1, Ljava/lang/ref/WeakReference;

    invoke-direct {p1, p2}, Ljava/lang/ref/WeakReference;-><init>(Ljava/lang/Object;)V

    iput-object p1, p0, Lcom/android/provision/utils/RequestThread;->mContextRef:Ljava/lang/ref/WeakReference;

    return-void
.end method


# virtual methods
.method public run()V
    .registers 7

    const/4 v0, 0x0

    :goto_0
    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->getRecommendedOperation()I

    move-result v1

    const/4 v2, -0x1

    if-ne v1, v2, :cond_3

    iget-object v1, p0, Lcom/android/provision/utils/RequestThread;->mContextRef:Ljava/lang/ref/WeakReference;

    invoke-virtual {v1}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Landroid/content/Context;

    invoke-static {v1}, Lcom/android/provision/Utils;->networkAvailable(Landroid/content/Context;)Z

    move-result v1

    if-eqz v1, :cond_3

    const/4 v1, 0x3

    if-ge v0, v1, :cond_3

    iget-object v1, p0, Lcom/android/provision/utils/RequestThread;->url:Ljava/lang/String;

    const/4 v3, 0x0

    invoke-static {v1, v3}, Lcom/android/provision/http/NetRequestor;->request(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    invoke-static {v1}, Lcom/android/provision/utils/RequestUtils;->parseContent(Ljava/lang/String;)I

    move-result v1

    const/16 v3, 0x198

    const-string v4, " , thread: "

    const-string v5, "RequestThread"

    if-eq v1, v3, :cond_2

    if-ne v1, v2, :cond_0

    goto :goto_1

    :cond_0
    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "request ok, operation: "

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v2, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;

    move-result-object v3

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-static {v5, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    const/4 v2, 0x1

    if-ne v1, v2, :cond_1

    iget-object v2, p0, Lcom/android/provision/utils/RequestThread;->mContextRef:Ljava/lang/ref/WeakReference;

    invoke-virtual {v2}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;

    move-result-object v2

    check-cast v2, Landroid/content/Context;

    invoke-static {v2}, Lcom/android/provision/utils/RequestUtils;->activeAuraApk(Landroid/content/Context;)V

    :cond_1
    invoke-static {v1}, Lcom/android/provision/DefaultPreferenceHelper;->setRecommendedOperation(I)V

    goto :goto_0

    :cond_2
    :goto_1
    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "request error, operation: "

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v2, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;

    move-result-object v1

    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-static {v5, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    add-int/lit8 v0, v0, 0x1

    const-wide/16 v1, 0xfa0

    :try_start_0
    invoke-static {v1, v2}, Ljava/lang/Thread;->sleep(J)V
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_0

    :catch_0
    move-exception p0

    const-string v0, "thread interruptedException:"

    invoke-static {v5, v0, p0}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    :cond_3
    return-void
.end method
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
