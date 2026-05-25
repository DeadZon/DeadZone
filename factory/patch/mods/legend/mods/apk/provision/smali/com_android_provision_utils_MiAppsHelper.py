TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/utils/MiAppsHelper.smali'
CLASS_FALLBACK_NAMES = ['MiAppsHelper.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field public static final GET_APPS_PKG_NAME:Ljava/lang/String; = "com.xiaomi.mipicks"', '.field private static final IN_ROM:Z', '.field public static final MI_APPS_ACTION:Ljava/lang/String; = "com.xiaomi.market.FirstRecommend"', '.field public static final MI_APPS_CONTENT:Ljava/lang/String;', '.field public static final MI_APPS_REF:Ljava/lang/String; = "provision"']

PATCHES = [
    {
        'id': 'com_android_provision_utils_MiAppsHelper__initializeStaticConditions',
        'method': '.method private static initializeStaticConditions()V',
        'method_name': 'initializeStaticConditions',
        'method_anchors': ['sget-boolean v0, Lcom/android/provision/utils/MiAppsHelper;->sStaticConditionsInitialized:Z', 'if-nez v0, :cond_3', 'sget-object v0, Lcom/android/provision/utils/MiAppsHelper;->sLock:Ljava/lang/Object;', 'sget-boolean v1, Lcom/android/provision/utils/MiAppsHelper;->sStaticConditionsInitialized:Z', 'if-nez v1, :cond_2', 'sget-boolean v1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v1, :cond_1', 'invoke-static {}, Lcom/android/provision/Utils;->isGoogleCoopeModels()Z'],
        'type': 'policy_skip',
        'search': """.method private static initializeStaticConditions()V
    .registers 5

    sget-boolean v0, Lcom/android/provision/utils/MiAppsHelper;->sStaticConditionsInitialized:Z

    if-nez v0, :cond_3

    sget-object v0, Lcom/android/provision/utils/MiAppsHelper;->sLock:Ljava/lang/Object;

    monitor-enter v0

    :try_start_0
    sget-boolean v1, Lcom/android/provision/utils/MiAppsHelper;->sStaticConditionsInitialized:Z

    if-nez v1, :cond_2

    sget-boolean v1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    const/4 v2, 0x1

    if-eqz v1, :cond_1

    invoke-static {}, Lcom/android/provision/Utils;->isGoogleCoopeModels()Z

    move-result v1

    if-eqz v1, :cond_0

    goto :goto_0

    :cond_0
    const/4 v1, 0x0

    goto :goto_1

    :catchall_0
    move-exception v1

    goto :goto_2

    :cond_1
    :goto_0
    move v1, v2

    :goto_1
    sput-boolean v1, Lcom/android/provision/utils/MiAppsHelper;->sStaticConditions:Z

    const-string v1, "MiAppsHelper"

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    const-string v4, "shouldSkipMiApps staticConditions: "

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget-boolean v4, Lcom/android/provision/utils/MiAppsHelper;->sStaticConditions:Z

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-static {v1, v3}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    sput-boolean v2, Lcom/android/provision/utils/MiAppsHelper;->sStaticConditionsInitialized:Z

    :cond_2
    monitor-exit v0

    return-void

    :goto_2
    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    throw v1

    :cond_3
    return-void
.end method""",
        'replacement': """.method private static initializeStaticConditions()V
    .registers 5

    sget-boolean v0, Lcom/android/provision/utils/MiAppsHelper;->sStaticConditionsInitialized:Z

    if-nez v0, :cond_3

    sget-object v0, Lcom/android/provision/utils/MiAppsHelper;->sLock:Ljava/lang/Object;

    monitor-enter v0

    :try_start_0
    sget-boolean v1, Lcom/android/provision/utils/MiAppsHelper;->sStaticConditionsInitialized:Z

    if-nez v1, :cond_2

    sget-boolean v1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    const/4 v2, 0x1

    if-eqz v1, :cond_1

    invoke-static {}, Lcom/android/provision/Utils;->isGoogleCoopeModels()Z

    move-result v1

    if-eqz v1, :cond_0

    goto :goto_0

    :cond_0
    const/4 v1, 0x0

    goto :goto_1

    :catchall_0
    move-exception v1

    goto :goto_2

    :cond_1
    :goto_0
    move v1, v2

    :goto_1
    sput-boolean v1, Lcom/android/provision/utils/MiAppsHelper;->sStaticConditions:Z

    const-string v1, "MiAppsHelper"

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    const-string v4, "shouldSkipMiApps staticConditions: "

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget-boolean v4, Lcom/android/provision/utils/MiAppsHelper;->sStaticConditions:Z

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-static {v1, v3}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    sput-boolean v2, Lcom/android/provision/utils/MiAppsHelper;->sStaticConditionsInitialized:Z

    :cond_2
    monitor-exit v0

    return-void

    :goto_2
    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    throw v1

    :cond_3
    return-void
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
]
