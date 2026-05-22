TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/utils/CloudConfigRequestThread.smali'
CLASS_FALLBACK_NAMES = ['CloudConfigRequestThread.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Thread;', '.field private static final REQUEST_INTERVAL_TIME:I = 0xfa0', '.field private static final REQUREST_MAX_ERROR:I = 0x3', '.field private static final TAG:Ljava/lang/String; = "CloudConfigRequest"']

PATCHES = [
    {
        'id': 'com_android_provision_utils_CloudConfigRequestThread__class_delete',
        'type': 'class_delete',
        'search': """.class public Lcom/android/provision/utils/CloudConfigRequestThread;
.super Ljava/lang/Thread;


# static fields
.field private static final REQUEST_INTERVAL_TIME:I = 0xfa0

.field private static final REQUREST_MAX_ERROR:I = 0x3

.field private static final TAG:Ljava/lang/String; = "CloudConfigRequest"


# instance fields
.field private isSuccess:Z

.field private mConfigKey:Ljava/lang/String;

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
.method public constructor <init>(Ljava/lang/String;Ljava/lang/String;Landroid/content/Context;)V
    .registers 4

    invoke-direct {p0}, Ljava/lang/Thread;-><init>()V

    iput-object p1, p0, Lcom/android/provision/utils/CloudConfigRequestThread;->url:Ljava/lang/String;

    iput-object p2, p0, Lcom/android/provision/utils/CloudConfigRequestThread;->mConfigKey:Ljava/lang/String;

    new-instance p1, Ljava/lang/ref/WeakReference;

    invoke-direct {p1, p3}, Ljava/lang/ref/WeakReference;-><init>(Ljava/lang/Object;)V

    iput-object p1, p0, Lcom/android/provision/utils/CloudConfigRequestThread;->mContextRef:Ljava/lang/ref/WeakReference;

    return-void
.end method

.method public static parseContent(Ljava/lang/String;Ljava/lang/String;)I
    .registers 8

    const-string v0, "CloudConfigRequest"

    const-string v1, "time_out_response"

    invoke-static {v1, p0}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result v1

    if-eqz v1, :cond_0

    const/16 p0, 0x198

    return p0

    :cond_0
    const-string v1, "exception_response"

    invoke-static {v1, p0}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result v1

    const/4 v2, -0x1

    if-eqz v1, :cond_1

    return v2

    :cond_1
    :try_start_0
    new-instance v1, Lorg/json/JSONObject;

    invoke-direct {v1, p0}, Lorg/json/JSONObject;-><init>(Ljava/lang/String;)V

    const-string p0, "head"

    invoke-virtual {v1, p0}, Lorg/json/JSONObject;->getJSONObject(Ljava/lang/String;)Lorg/json/JSONObject;

    move-result-object p0

    const-string v3, "code"

    invoke-virtual {p0, v3}, Lorg/json/JSONObject;->getInt(Ljava/lang/String;)I

    move-result p0

    const/16 v3, 0xc8

    if-ne p0, v3, :cond_8

    const-string p0, "data"

    invoke-virtual {v1, p0}, Lorg/json/JSONObject;->getJSONObject(Ljava/lang/String;)Lorg/json/JSONObject;

    move-result-object p0

    const-string v1, "list"

    invoke-virtual {p0, v1}, Lorg/json/JSONObject;->getJSONArray(Ljava/lang/String;)Lorg/json/JSONArray;

    move-result-object p0

    invoke-virtual {p0}, Ljava/lang/Object;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-static {v0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    invoke-virtual {p0}, Lorg/json/JSONArray;->length()I

    move-result v1

    if-ltz v1, :cond_7

    invoke-virtual {p1}, Ljava/lang/Object;->hashCode()I

    move-result v1

    const v3, -0x413905be

    const/4 v4, 0x1

    const/4 v5, 0x0

    if-eq v1, v3, :cond_3

    const v3, 0x693106f3

    if-eq v1, v3, :cond_2

    goto :goto_0

    :cond_2
    const-string v1, "carousel_switch"

    invoke-virtual {p1, v1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result p1

    if-eqz p1, :cond_4

    move p1, v5

    goto :goto_1

    :catch_0
    move-exception p0

    goto :goto_2

    :cond_3
    const-string v1, "drawer_switch"

    invoke-virtual {p1, v1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result p1
    :try_end_0
    .catch Lorg/json/JSONException; {:try_start_0 .. :try_end_0} :catch_0

    if-eqz p1, :cond_4

    move p1, v4

    goto :goto_1

    :cond_4
    :goto_0
    move p1, v2

    :goto_1
    const-string v1, "content"

    if-eqz p1, :cond_6

    if-eq p1, v4, :cond_5

    :try_start_1
    const-string p0, "remote configKey is invalided!"

    invoke-static {v0, p0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    return v5

    :cond_5
    invoke-virtual {p0, v5}, Lorg/json/JSONArray;->get(I)Ljava/lang/Object;

    move-result-object p0

    check-cast p0, Lorg/json/JSONObject;

    invoke-virtual {p0, v1}, Lorg/json/JSONObject;->getJSONObject(Ljava/lang/String;)Lorg/json/JSONObject;

    move-result-object p0

    const-string p1, "enable_drawer"

    invoke-virtual {p0, p1}, Lorg/json/JSONObject;->getBoolean(Ljava/lang/String;)Z

    move-result p0

    return p0

    :cond_6
    invoke-virtual {p0, v5}, Lorg/json/JSONArray;->get(I)Ljava/lang/Object;

    move-result-object p0

    check-cast p0, Lorg/json/JSONObject;

    invoke-virtual {p0, v1}, Lorg/json/JSONObject;->getJSONObject(Ljava/lang/String;)Lorg/json/JSONObject;

    move-result-object p0

    const-string p1, "enable_carousel"

    invoke-virtual {p0, p1}, Lorg/json/JSONObject;->getBoolean(Ljava/lang/String;)Z

    move-result p0

    return p0

    :cond_7
    const-string p0, "jsonArray.length() < 0"

    invoke-static {v0, p0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_3

    :cond_8
    new-instance p1, Ljava/lang/StringBuilder;

    invoke-direct {p1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v1, "request failed statusCode:"

    invoke-virtual {p1, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p1, p0}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {p1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    invoke-static {v0, p0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I
    :try_end_1
    .catch Lorg/json/JSONException; {:try_start_1 .. :try_end_1} :catch_0

    goto :goto_3

    :goto_2
    const-string p1, "parseContent exception"

    invoke-static {v0, p1, p0}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    :goto_3
    return v2
.end method


# virtual methods
.method public run()V
    .registers 8

    const/4 v0, 0x1

    const/4 v1, 0x0

    :goto_0
    iget-boolean v2, p0, Lcom/android/provision/utils/CloudConfigRequestThread;->isSuccess:Z

    if-nez v2, :cond_4

    iget-object v2, p0, Lcom/android/provision/utils/CloudConfigRequestThread;->mContextRef:Ljava/lang/ref/WeakReference;

    invoke-virtual {v2}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;

    move-result-object v2

    check-cast v2, Landroid/content/Context;

    invoke-static {v2}, Lcom/android/provision/Utils;->networkAvailable(Landroid/content/Context;)Z

    move-result v2

    if-eqz v2, :cond_4

    const/4 v2, 0x3

    if-ge v1, v2, :cond_4

    iget-object v2, p0, Lcom/android/provision/utils/CloudConfigRequestThread;->url:Ljava/lang/String;

    const/4 v3, 0x0

    invoke-static {v2, v3}, Lcom/android/provision/http/NetRequestor;->request(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v2

    iget-object v3, p0, Lcom/android/provision/utils/CloudConfigRequestThread;->mConfigKey:Ljava/lang/String;

    invoke-static {v2, v3}, Lcom/android/provision/utils/CloudConfigRequestThread;->parseContent(Ljava/lang/String;Ljava/lang/String;)I

    move-result v2

    const/16 v3, 0x198

    const-string v4, " , thread: "

    const-string v5, "CloudConfigRequest"

    if-eq v2, v3, :cond_3

    const/4 v3, -0x1

    if-ne v2, v3, :cond_0

    goto :goto_1

    :cond_0
    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    const-string v6, "request ok, operation: "

    invoke-virtual {v3, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v3, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    const-string v6, " , mConfigKey:"

    invoke-virtual {v3, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object v6, p0, Lcom/android/provision/utils/CloudConfigRequestThread;->mConfigKey:Ljava/lang/String;

    invoke-virtual {v3, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;

    move-result-object v4

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-static {v5, v3}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    iput-boolean v0, p0, Lcom/android/provision/utils/CloudConfigRequestThread;->isSuccess:Z

    iget-object v3, p0, Lcom/android/provision/utils/CloudConfigRequestThread;->mConfigKey:Ljava/lang/String;

    invoke-virtual {v3}, Ljava/lang/Object;->hashCode()I

    const-string v4, "drawer_switch"

    invoke-virtual {v3, v4}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v4

    if-nez v4, :cond_2

    const-string v4, "carousel_switch"

    invoke-virtual {v3, v4}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v3

    if-nez v3, :cond_1

    const-string v2, "remote configKey is invalided!"

    invoke-static {v5, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_0

    :cond_1
    invoke-static {v2}, Lcom/android/provision/DefaultPreferenceHelper;->setCarouselEnable(I)V

    goto :goto_0

    :cond_2
    invoke-static {v2}, Lcom/android/provision/DefaultPreferenceHelper;->setDrawerEnable(I)V

    goto :goto_0

    :cond_3
    :goto_1
    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    const-string v6, "request error, operation: "

    invoke-virtual {v3, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v3, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;

    move-result-object v2

    invoke-virtual {v3, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-static {v5, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    add-int/2addr v1, v0

    const-wide/16 v2, 0xfa0

    :try_start_0
    invoke-static {v2, v3}, Ljava/lang/Thread;->sleep(J)V
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_0

    :catch_0
    move-exception p0

    const-string v0, "thread interruptedException:"

    invoke-static {v5, v0, p0}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    :cond_4
    return-void
.end method
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
