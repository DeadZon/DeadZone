TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/ProvisionApplication.smali'
CLASS_FALLBACK_NAMES = ['ProvisionApplication.smali']
CLASS_ANCHORS = ['.super Lmiuix/app/Application;', '.implements Lmiuix/autodensity/IDensity;', '.field private static final TAG:Ljava/lang/String; = "ProvisionApplication"']

PATCHES = [
    {
        'id': 'com_android_provision_ProvisionApplication__onCreate',
        'method': '.method public onCreate()V',
        'method_name': 'onCreate',
        'method_anchors': ['invoke-super {p0}, Lmiuix/app/Application;->onCreate()V', 'invoke-static {}, Lcom/android/provision/utils/LifecycleHandler;->create()Lcom/android/provision/utils/LifecycleHandler;', 'invoke-virtual {p0, v0}, Landroid/app/Application;->registerActivityLifecycleCallbacks(Landroid/app/Application$ActivityLifecycleCallbacks;)V', 'invoke-static {p0}, Lmiuix/autodensity/AutoDensityConfig;->init(Landroid/app/Application;)Lmiuix/autodensity/AutoDensityConfig;', 'sput-object p0, Lcom/android/provision/ProvisionApplication;->sContext:Landroid/content/Context;', 'invoke-static {p0}, Lcom/android/provision/utils/OTHelper;->initialize(Landroid/content/Context;)V', 'invoke-direct {p0}, Lcom/android/provision/ProvisionApplication;->registerBootReceiver()V', 'sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z'],
        'type': 'policy_skip',
        'search': """.method public onCreate()V
    .registers 3

    invoke-super {p0}, Lmiuix/app/Application;->onCreate()V

    invoke-static {}, Lcom/android/provision/utils/LifecycleHandler;->create()Lcom/android/provision/utils/LifecycleHandler;

    move-result-object v0

    invoke-virtual {p0, v0}, Landroid/app/Application;->registerActivityLifecycleCallbacks(Landroid/app/Application$ActivityLifecycleCallbacks;)V

    invoke-static {p0}, Lmiuix/autodensity/AutoDensityConfig;->init(Landroid/app/Application;)Lmiuix/autodensity/AutoDensityConfig;

    sput-object p0, Lcom/android/provision/ProvisionApplication;->sContext:Landroid/content/Context;

    invoke-static {p0}, Lcom/android/provision/utils/OTHelper;->initialize(Landroid/content/Context;)V

    invoke-direct {p0}, Lcom/android/provision/ProvisionApplication;->registerBootReceiver()V

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    invoke-static {}, Lcom/android/provision/utils/MccHelper;->getInstance()Lcom/android/provision/utils/MccHelper;

    move-result-object v0

    invoke-virtual {v0, p0}, Lcom/android/provision/utils/MccHelper;->init(Landroid/content/Context;)V

    :cond_0
    invoke-static {}, Lcom/android/provision/utils/MediaPlayerPool;->get()Lcom/android/provision/utils/MediaPlayerPool;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/provision/utils/MediaPlayerPool;->acquireDefault()V

    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-static {v0}, Lcom/android/provision/Utils;->setupProvisionResources(Landroid/content/Context;)V

    const-string v0, "ProvisionApplication"

    const-string v1, "setupProvisionResources when application create"

    invoke-static {v0, v1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    invoke-static {}, Lcom/android/provision/animtool/LanguagePreLoadManager;->preLoadTextureView()V

    invoke-static {}, Lcom/android/provision/manager/PreLoadActivityLifeCallback;->create()Lcom/android/provision/manager/PreLoadActivityLifeCallback;

    move-result-object v0

    invoke-virtual {p0, v0}, Landroid/app/Application;->registerActivityLifecycleCallbacks(Landroid/app/Application$ActivityLifecycleCallbacks;)V

    invoke-static {}, Lcom/android/provision/manager/PreLoadManager;->get()Lcom/android/provision/manager/PreLoadManager;

    move-result-object v0

    invoke-virtual {v0, p0}, Lcom/android/provision/manager/PreLoadManager;->init(Landroid/app/Application;)V

    invoke-static {p0}, Lcom/android/provision/utils/ImmersiveUtils;->enableImmersion(Landroid/content/Context;)V

    invoke-direct {p0}, Lcom/android/provision/ProvisionApplication;->preloadAnimations()V

    return-void
.end method""",
        'replacement': """.method public onCreate()V
    .registers 3

    invoke-super {p0}, Lmiuix/app/Application;->onCreate()V

    invoke-static {}, Lcom/android/provision/utils/LifecycleHandler;->create()Lcom/android/provision/utils/LifecycleHandler;

    move-result-object v0

    invoke-virtual {p0, v0}, Landroid/app/Application;->registerActivityLifecycleCallbacks(Landroid/app/Application$ActivityLifecycleCallbacks;)V

    invoke-static {p0}, Lmiuix/autodensity/AutoDensityConfig;->init(Landroid/app/Application;)Lmiuix/autodensity/AutoDensityConfig;

    sput-object p0, Lcom/android/provision/ProvisionApplication;->sContext:Landroid/content/Context;

    invoke-static {p0}, Lcom/android/provision/utils/OTHelper;->initialize(Landroid/content/Context;)V

    invoke-direct {p0}, Lcom/android/provision/ProvisionApplication;->registerBootReceiver()V

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    invoke-static {}, Lcom/android/provision/utils/MccHelper;->getInstance()Lcom/android/provision/utils/MccHelper;

    move-result-object v0

    invoke-virtual {v0, p0}, Lcom/android/provision/utils/MccHelper;->init(Landroid/content/Context;)V

    :cond_0
    invoke-static {}, Lcom/android/provision/utils/MediaPlayerPool;->get()Lcom/android/provision/utils/MediaPlayerPool;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/provision/utils/MediaPlayerPool;->acquireDefault()V

    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-static {v0}, Lcom/android/provision/Utils;->setupProvisionResources(Landroid/content/Context;)V

    const-string v0, "ProvisionApplication"

    const-string v1, "setupProvisionResources when application create"

    invoke-static {v0, v1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    invoke-static {}, Lcom/android/provision/animtool/LanguagePreLoadManager;->preLoadTextureView()V

    invoke-static {}, Lcom/android/provision/manager/PreLoadActivityLifeCallback;->create()Lcom/android/provision/manager/PreLoadActivityLifeCallback;

    move-result-object v0

    invoke-virtual {p0, v0}, Landroid/app/Application;->registerActivityLifecycleCallbacks(Landroid/app/Application$ActivityLifecycleCallbacks;)V

    invoke-static {}, Lcom/android/provision/manager/PreLoadManager;->get()Lcom/android/provision/manager/PreLoadManager;

    move-result-object v0

    invoke-virtual {v0, p0}, Lcom/android/provision/manager/PreLoadManager;->init(Landroid/app/Application;)V

    invoke-static {p0}, Lcom/android/provision/utils/ImmersiveUtils;->enableImmersion(Landroid/content/Context;)V

    invoke-direct {p0}, Lcom/android/provision/ProvisionApplication;->preloadAnimations()V

    return-void
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
]
