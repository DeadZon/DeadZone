TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/utils/CloudConfigRequest.smali'
CLASS_FALLBACK_NAMES = ['CloudConfigRequest.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field public static final CAROUSEL_ENABLE:Ljava/lang/String; = "carousel_switch"', '.field private static final CLOUD_CONFIG_URL:Ljava/lang/String; = "https://api.setting.intl.miui.com/setting/v1/config?"', '.field private static final CLOUD_CONFIG_URL_DEBUG:Ljava/lang/String; = "https://sandbox.api.setting.intl.miui.com/setting/v1/config?"', '.field public static final DRAWER_ENABLE:Ljava/lang/String; = "drawer_switch"', '.field private static final TAG:Ljava/lang/String; = "CloudConfigRequestUtils"']

PATCHES = [
    {
        'id': 'com_android_provision_utils_CloudConfigRequest__class_delete',
        'type': 'class_delete',
        'search': """.class public Lcom/android/provision/utils/CloudConfigRequest;
.super Ljava/lang/Object;


# static fields
.field public static final CAROUSEL_ENABLE:Ljava/lang/String; = "carousel_switch"

.field private static final CLOUD_CONFIG_URL:Ljava/lang/String; = "https://api.setting.intl.miui.com/setting/v1/config?"

.field private static final CLOUD_CONFIG_URL_DEBUG:Ljava/lang/String; = "https://sandbox.api.setting.intl.miui.com/setting/v1/config?"

.field public static final DRAWER_ENABLE:Ljava/lang/String; = "drawer_switch"

.field private static final TAG:Ljava/lang/String; = "CloudConfigRequestUtils"


# instance fields
.field private isDebug:Z

.field private mCloudConfigThread:Lcom/android/provision/utils/CloudConfigRequestThread;


# direct methods
.method public constructor <init>()V
    .registers 2

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    const/4 v0, 0x0

    iput-object v0, p0, Lcom/android/provision/utils/CloudConfigRequest;->mCloudConfigThread:Lcom/android/provision/utils/CloudConfigRequestThread;

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/android/provision/utils/CloudConfigRequest;->isDebug:Z

    return-void
.end method

.method private static getBaseRequestParams()Ljava/util/TreeMap;
    .registers 3
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "()",
            "Ljava/util/TreeMap<",
            "Ljava/lang/String;",
            "Ljava/lang/String;",
            ">;"
        }
    .end annotation

    new-instance v0, Ljava/util/TreeMap;

    invoke-direct {v0}, Ljava/util/TreeMap;-><init>()V

    const-string v1, "app_id"

    const-string v2, "GLOBAL_PROVISION"

    invoke-virtual {v0, v1, v2}, Ljava/util/TreeMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    const-string v1, "miui_version"

    invoke-static {}, Lcom/android/provision/Utils;->getMiuiVersion()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v0, v1, v2}, Ljava/util/TreeMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    const-string v1, "os_version"

    invoke-static {}, Lcom/android/provision/Utils;->getOsVersion()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v0, v1, v2}, Ljava/util/TreeMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    const-string v1, "d"

    invoke-static {}, Lcom/android/provision/Utils;->getModel()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v0, v1, v2}, Ljava/util/TreeMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    invoke-static {}, Ljava/util/Locale;->getDefault()Ljava/util/Locale;

    move-result-object v1

    invoke-virtual {v1}, Ljava/util/Locale;->getLanguage()Ljava/lang/String;

    move-result-object v1

    const-string v2, "l"

    invoke-virtual {v0, v2, v1}, Ljava/util/TreeMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    invoke-static {}, Lcom/android/provision/Utils;->getMiuiVersionType()Ljava/lang/String;

    move-result-object v1

    invoke-static {v1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v1

    if-nez v1, :cond_0

    const-string v1, "t"

    invoke-static {}, Lcom/android/provision/Utils;->getMiuiVersionType()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v0, v1, v2}, Ljava/util/TreeMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    :cond_0
    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object v1

    invoke-virtual {v1}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

    move-result-object v1

    const-string v2, "pkg"

    invoke-virtual {v0, v2, v1}, Ljava/util/TreeMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v1

    invoke-static {v1, v2}, Ljava/lang/String;->valueOf(J)Ljava/lang/String;

    move-result-object v1

    const-string v2, "timestamp"

    invoke-virtual {v0, v2, v1}, Ljava/util/TreeMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    return-object v0
.end method


# virtual methods
.method public cloudConfigRequest(Ljava/lang/String;Ljava/lang/String;Landroid/content/Context;)V
    .registers 5

    invoke-virtual {p0, p1, p2}, Lcom/android/provision/utils/CloudConfigRequest;->getRequestUrl(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object p1

    iget-object v0, p0, Lcom/android/provision/utils/CloudConfigRequest;->mCloudConfigThread:Lcom/android/provision/utils/CloudConfigRequestThread;

    if-nez v0, :cond_0

    new-instance v0, Lcom/android/provision/utils/CloudConfigRequestThread;

    invoke-direct {v0, p1, p2, p3}, Lcom/android/provision/utils/CloudConfigRequestThread;-><init>(Ljava/lang/String;Ljava/lang/String;Landroid/content/Context;)V

    iput-object v0, p0, Lcom/android/provision/utils/CloudConfigRequest;->mCloudConfigThread:Lcom/android/provision/utils/CloudConfigRequestThread;

    goto :goto_0

    :cond_0
    invoke-virtual {v0}, Ljava/lang/Thread;->interrupt()V

    new-instance v0, Lcom/android/provision/utils/CloudConfigRequestThread;

    invoke-direct {v0, p1, p2, p3}, Lcom/android/provision/utils/CloudConfigRequestThread;-><init>(Ljava/lang/String;Ljava/lang/String;Landroid/content/Context;)V

    iput-object v0, p0, Lcom/android/provision/utils/CloudConfigRequest;->mCloudConfigThread:Lcom/android/provision/utils/CloudConfigRequestThread;

    :goto_0
    invoke-static {p3}, Lcom/android/provision/Utils;->networkAvailable(Landroid/content/Context;)Z

    move-result p1

    if-eqz p1, :cond_1

    iget-object p1, p0, Lcom/android/provision/utils/CloudConfigRequest;->mCloudConfigThread:Lcom/android/provision/utils/CloudConfigRequestThread;

    invoke-virtual {p1}, Ljava/lang/Thread;->getState()Ljava/lang/Thread$State;

    move-result-object p1

    sget-object p2, Ljava/lang/Thread$State;->NEW:Ljava/lang/Thread$State;

    if-ne p1, p2, :cond_1

    iget-object p0, p0, Lcom/android/provision/utils/CloudConfigRequest;->mCloudConfigThread:Lcom/android/provision/utils/CloudConfigRequestThread;

    invoke-virtual {p0}, Ljava/lang/Thread;->start()V

    :cond_1
    return-void
.end method

.method public getRequestUrl(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    .registers 5

    invoke-static {}, Lcom/android/provision/utils/CloudConfigRequest;->getBaseRequestParams()Ljava/util/TreeMap;

    move-result-object v0

    const-string v1, "cids"

    invoke-virtual {v0, v1, p2}, Ljava/util/TreeMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    const-string p2, "r"

    invoke-virtual {v0, p2, p1}, Ljava/util/TreeMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    const-string p1, "sign"

    invoke-static {v0}, Lcom/android/provision/utils/MD5Utils;->getVerificationSignature(Ljava/util/SortedMap;)Ljava/lang/String;

    move-result-object p2

    invoke-virtual {v0, p1, p2}, Ljava/util/TreeMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    invoke-static {v0}, Lcom/android/provision/utils/MD5Utils;->getConvertedParams(Ljava/util/SortedMap;)Ljava/lang/String;

    move-result-object p1

    new-instance p2, Ljava/lang/StringBuilder;

    invoke-direct {p2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v0, "CloudConfigRequestUtils: "

    invoke-virtual {p2, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p2, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p2

    const-string v0, "CloudConfigRequestUtils"

    invoke-static {v0, p2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    iget-boolean p0, p0, Lcom/android/provision/utils/CloudConfigRequest;->isDebug:Z

    if-eqz p0, :cond_0

    new-instance p0, Ljava/lang/StringBuilder;

    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    const-string p2, "https://sandbox.api.setting.intl.miui.com/setting/v1/config?"

    invoke-virtual {p0, p2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    return-object p0

    :cond_0
    new-instance p0, Ljava/lang/StringBuilder;

    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    const-string p2, "https://api.setting.intl.miui.com/setting/v1/config?"

    invoke-virtual {p0, p2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    return-object p0
.end method
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
