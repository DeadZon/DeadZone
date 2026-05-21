TARGET_APK = 'PowerKeeper.apk'
TARGET_CLASS = 'com/miui/powerkeeper/utils/GmsObserver.smali'
CLASS_FALLBACK_NAMES = ['GmsObserver.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field private static final GMS_BACKUP_PKG:Ljava/lang/String; = "com.google.android.backuptransport"', '.field private static final GOOGLE_ACCOUNT_TYPE:Ljava/lang/String; = "com.google"', '.field private static final MSG_UPDATE_CLOUD:I = 0x0', '.field private static final MSG_UPDATE_GMS_STATE:I = 0x1', '.field private static final TAG:Ljava/lang/String; = "PowerKeeper.GMS"']

PATCHES = [
    {
        'id': 'com_miui_powerkeeper_utils_GmsObserver__isGmsControlEnabled',
        'method': '.method private isGmsControlEnabled()Z',
        'method_name': 'isGmsControlEnabled',
        'method_anchors': ['iget-object v0, p0, Lcom/miui/powerkeeper/utils/GmsObserver;->mContext:Landroid/content/Context;', 'const-string v1, "com.android.vending"', 'invoke-static {v0, v1}, Lcom/miui/powerkeeper/provider/UserConfigureHelper;->getUserConfigureHelperByPkg(Landroid/content/Context;Ljava/lang/String;)Lcom/miui/powerkeeper/provider/UserConfigureHelper;', 'iput-object v0, p0, Lcom/miui/powerkeeper/utils/GmsObserver;->mGmsUserConfigure:Lcom/miui/powerkeeper/provider/UserConfigureHelper;', 'invoke-virtual {v0}, Lcom/miui/powerkeeper/provider/UserConfigureHelper;->getBgControl()Ljava/lang/String;', 'const-string v0, "noRestrict"', 'invoke-virtual {p0, v0}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z', 'return p0'],
        'type': 'method_replace',
        'search': """.method private isGmsControlEnabled()Z
    .registers 3

    iget-object v0, p0, Lcom/miui/powerkeeper/utils/GmsObserver;->mContext:Landroid/content/Context;

    const-string v1, "com.android.vending"

    invoke-static {v0, v1}, Lcom/miui/powerkeeper/provider/UserConfigureHelper;->getUserConfigureHelperByPkg(Landroid/content/Context;Ljava/lang/String;)Lcom/miui/powerkeeper/provider/UserConfigureHelper;

    move-result-object v0

    iput-object v0, p0, Lcom/miui/powerkeeper/utils/GmsObserver;->mGmsUserConfigure:Lcom/miui/powerkeeper/provider/UserConfigureHelper;

    invoke-virtual {v0}, Lcom/miui/powerkeeper/provider/UserConfigureHelper;->getBgControl()Ljava/lang/String;

    move-result-object p0

    const-string v0, "noRestrict"

    invoke-virtual {p0, v0}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result p0

    xor-int/lit8 p0, p0, 0x1

    return p0
.end method""",
        'replacement': """.method private isGmsControlEnabled()Z
    .registers 3

    iget-object v0, p0, Lcom/miui/powerkeeper/utils/GmsObserver;->mContext:Landroid/content/Context;

    const-string v1, "com.android.vending"

    invoke-static {v0, v1}, Lcom/miui/powerkeeper/provider/UserConfigureHelper;->getUserConfigureHelperByPkg(Landroid/content/Context;Ljava/lang/String;)Lcom/miui/powerkeeper/provider/UserConfigureHelper;

    move-result-object v0

    iput-object v0, p0, Lcom/miui/powerkeeper/utils/GmsObserver;->mGmsUserConfigure:Lcom/miui/powerkeeper/provider/UserConfigureHelper;

    invoke-virtual {v0}, Lcom/miui/powerkeeper/provider/UserConfigureHelper;->getBgControl()Ljava/lang/String;

    move-result-object p0

    const-string v0, "noRestrict"

    invoke-virtual {p0, v0}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result p0

    xor-int/lit8 p0, p0, 0x1

    const/4 p0, 0x0

    return p0
.end method""",
        'required': True,
        'flag_rewrite_count': 0,
        'reason': 'PowerKeeper smali rule generated from comparison output.',
    },
    {
        'id': 'com_miui_powerkeeper_utils_GmsObserver__updateGoogleSync',
        'method': '.method private updateGoogleSync(Z)V',
        'method_name': 'updateGoogleSync',
        'method_anchors': ['sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method private updateGoogleSync(Z)V
    .registers 2

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    return-void
.end method""",
        'replacement': """.method private updateGoogleSync(Z)V
    .registers 2

    sget-boolean p0, Lmiui/os/Build;->IS_MIUI:Z

    return-void
.end method""",
        'required': True,
        'flag_rewrite_count': 1,
        'reason': 'PowerKeeper smali rule generated from comparison output.',
    },
    {
        'id': 'com_miui_powerkeeper_utils_GmsObserver__init',
        'method': '.method public constructor <init>(Landroid/content/Context;)V',
        'method_name': '<init>',
        'method_anchors': ['invoke-direct {p0}, Ljava/lang/Object;-><init>()V', 'new-instance v0, Ljava/util/HashSet;', 'invoke-direct {v0}, Ljava/util/HashSet;-><init>()V', 'iput-object v0, p0, Lcom/miui/powerkeeper/utils/GmsObserver;->mGmsApps:Ljava/util/Set;', 'const-string v0, "com.google.android.gsf.login"', 'const-string v1, "com.android.vending"', 'const-string v2, "com.google.android.gms"', 'const-string v3, "com.google.android.gsf"'],
        'type': 'method_replace',
        'search': """.method public constructor <init>(Landroid/content/Context;)V
    .registers 6

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    new-instance v0, Ljava/util/HashSet;

    invoke-direct {v0}, Ljava/util/HashSet;-><init>()V

    iput-object v0, p0, Lcom/miui/powerkeeper/utils/GmsObserver;->mGmsApps:Ljava/util/Set;

    const-string v0, "com.google.android.gsf.login"

    const-string v1, "com.android.vending"

    const-string v2, "com.google.android.gms"

    const-string v3, "com.google.android.gsf"

    filled-new-array {v2, v3, v0, v1}, [Ljava/lang/String;

    move-result-object v0

    iput-object v0, p0, Lcom/miui/powerkeeper/utils/GmsObserver;->mGmsCoreApps:[Ljava/lang/String;

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/miui/powerkeeper/utils/GmsObserver;->mGmsControlInited:Z

    sget-boolean v1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    xor-int/lit8 v1, v1, 0x1

    iput-boolean v1, p0, Lcom/miui/powerkeeper/utils/GmsObserver;->defaultState:Z

    new-instance v1, Ljava/util/ArrayList;

    invoke-direct {v1}, Ljava/util/ArrayList;-><init>()V

    iput-object v1, p0, Lcom/miui/powerkeeper/utils/GmsObserver;->mCallbacks:Ljava/util/List;

    new-instance v1, Landroid/util/LocalLog;

    const/16 v3, 0x32

    invoke-direct {v1, v3}, Landroid/util/LocalLog;-><init>(I)V

    iput-object v1, p0, Lcom/miui/powerkeeper/utils/GmsObserver;->mReachabilityHistoryLog:Landroid/util/LocalLog;

    new-instance v1, Landroid/util/LocalLog;

    const/16 v3, 0x100

    invoke-direct {v1, v3}, Landroid/util/LocalLog;-><init>(I)V

    iput-object v1, p0, Lcom/miui/powerkeeper/utils/GmsObserver;->mWakelockBlockHistoryLog:Landroid/util/LocalLog;

    new-instance v1, Lcom/miui/powerkeeper/utils/GmsObserver$1;

    invoke-direct {v1, p0}, Lcom/miui/powerkeeper/utils/GmsObserver$1;-><init>(Lcom/miui/powerkeeper/utils/GmsObserver;)V

    iput-object v1, p0, Lcom/miui/powerkeeper/utils/GmsObserver;->mReceiver:Landroid/content/BroadcastReceiver;

    new-instance v1, Lcom/miui/powerkeeper/utils/GmsObserver$2;

    invoke-static {}, Lcom/miui/powerkeeper/PowerKeeperManager;->getThread()Landroid/os/HandlerThread;

    move-result-object v3

    invoke-virtual {v3}, Landroid/os/HandlerThread;->getLooper()Landroid/os/Looper;

    move-result-object v3

    invoke-direct {v1, p0, v3}, Lcom/miui/powerkeeper/utils/GmsObserver$2;-><init>(Lcom/miui/powerkeeper/utils/GmsObserver;Landroid/os/Looper;)V

    iput-object v1, p0, Lcom/miui/powerkeeper/utils/GmsObserver;->mHandler:Landroid/os/Handler;

    new-instance v1, Lcom/miui/powerkeeper/utils/GmsObserver$3;

    invoke-direct {v1, p0}, Lcom/miui/powerkeeper/utils/GmsObserver$3;-><init>(Lcom/miui/powerkeeper/utils/GmsObserver;)V

    iput-object v1, p0, Lcom/miui/powerkeeper/utils/GmsObserver;->mFunctionListener:Lcom/miui/powerkeeper/cloudcontrol/CloudFunctionConfig$ICloudFunctionListener;

    new-instance v1, Lcom/miui/powerkeeper/utils/GmsObserver$5;

    invoke-direct {v1, p0}, Lcom/miui/powerkeeper/utils/GmsObserver$5;-><init>(Lcom/miui/powerkeeper/utils/GmsObserver;)V

    iput-object v1, p0, Lcom/miui/powerkeeper/utils/GmsObserver;->mFeedBackGoogleNetworkListener:Lcom/miui/powerkeeper/PowerKeeperInterface$p;

    const-string v1, "PowerKeeper.GMS"

    const-string v3, "gms observer created"

    invoke-static {v1, v3}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    iput-object p1, p0, Lcom/miui/powerkeeper/utils/GmsObserver;->mContext:Landroid/content/Context;

    invoke-static {p1, v2}, Lcom/miui/powerkeeper/utils/PackageUtil;->getUidByPackageName(Landroid/content/Context;Ljava/lang/String;)I

    move-result p1

    iput p1, p0, Lcom/miui/powerkeeper/utils/GmsObserver;->mGmsUid:I

    iput-boolean v0, p0, Lcom/miui/powerkeeper/utils/GmsObserver;->mGmsBlocked:Z

    return-void
.end method""",
        'replacement': """.method public constructor <init>(Landroid/content/Context;)V
    .registers 6

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    new-instance v0, Ljava/util/HashSet;

    invoke-direct {v0}, Ljava/util/HashSet;-><init>()V

    iput-object v0, p0, Lcom/miui/powerkeeper/utils/GmsObserver;->mGmsApps:Ljava/util/Set;

    const-string v0, "com.google.android.gsf.login"

    const-string v1, "com.android.vending"

    const-string v2, "com.google.android.gms"

    const-string v3, "com.google.android.gsf"

    filled-new-array {v2, v3, v0, v1}, [Ljava/lang/String;

    move-result-object v0

    iput-object v0, p0, Lcom/miui/powerkeeper/utils/GmsObserver;->mGmsCoreApps:[Ljava/lang/String;

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/miui/powerkeeper/utils/GmsObserver;->mGmsControlInited:Z

    sget-boolean v1, Lmiui/os/Build;->IS_MIUI:Z

    xor-int/lit8 v1, v1, 0x1

    iput-boolean v1, p0, Lcom/miui/powerkeeper/utils/GmsObserver;->defaultState:Z

    new-instance v1, Ljava/util/ArrayList;

    invoke-direct {v1}, Ljava/util/ArrayList;-><init>()V

    iput-object v1, p0, Lcom/miui/powerkeeper/utils/GmsObserver;->mCallbacks:Ljava/util/List;

    new-instance v1, Landroid/util/LocalLog;

    const/16 v3, 0x32

    invoke-direct {v1, v3}, Landroid/util/LocalLog;-><init>(I)V

    iput-object v1, p0, Lcom/miui/powerkeeper/utils/GmsObserver;->mReachabilityHistoryLog:Landroid/util/LocalLog;

    new-instance v1, Landroid/util/LocalLog;

    const/16 v3, 0x100

    invoke-direct {v1, v3}, Landroid/util/LocalLog;-><init>(I)V

    iput-object v1, p0, Lcom/miui/powerkeeper/utils/GmsObserver;->mWakelockBlockHistoryLog:Landroid/util/LocalLog;

    new-instance v1, Lcom/miui/powerkeeper/utils/GmsObserver$1;

    invoke-direct {v1, p0}, Lcom/miui/powerkeeper/utils/GmsObserver$1;-><init>(Lcom/miui/powerkeeper/utils/GmsObserver;)V

    iput-object v1, p0, Lcom/miui/powerkeeper/utils/GmsObserver;->mReceiver:Landroid/content/BroadcastReceiver;

    new-instance v1, Lcom/miui/powerkeeper/utils/GmsObserver$2;

    invoke-static {}, Lcom/miui/powerkeeper/PowerKeeperManager;->getThread()Landroid/os/HandlerThread;

    move-result-object v3

    invoke-virtual {v3}, Landroid/os/HandlerThread;->getLooper()Landroid/os/Looper;

    move-result-object v3

    invoke-direct {v1, p0, v3}, Lcom/miui/powerkeeper/utils/GmsObserver$2;-><init>(Lcom/miui/powerkeeper/utils/GmsObserver;Landroid/os/Looper;)V

    iput-object v1, p0, Lcom/miui/powerkeeper/utils/GmsObserver;->mHandler:Landroid/os/Handler;

    new-instance v1, Lcom/miui/powerkeeper/utils/GmsObserver$3;

    invoke-direct {v1, p0}, Lcom/miui/powerkeeper/utils/GmsObserver$3;-><init>(Lcom/miui/powerkeeper/utils/GmsObserver;)V

    iput-object v1, p0, Lcom/miui/powerkeeper/utils/GmsObserver;->mFunctionListener:Lcom/miui/powerkeeper/cloudcontrol/CloudFunctionConfig$ICloudFunctionListener;

    new-instance v1, Lcom/miui/powerkeeper/utils/GmsObserver$5;

    invoke-direct {v1, p0}, Lcom/miui/powerkeeper/utils/GmsObserver$5;-><init>(Lcom/miui/powerkeeper/utils/GmsObserver;)V

    iput-object v1, p0, Lcom/miui/powerkeeper/utils/GmsObserver;->mFeedBackGoogleNetworkListener:Lcom/miui/powerkeeper/PowerKeeperInterface$p;

    const-string v1, "PowerKeeper.GMS"

    const-string v3, "gms observer created"

    invoke-static {v1, v3}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    iput-object p1, p0, Lcom/miui/powerkeeper/utils/GmsObserver;->mContext:Landroid/content/Context;

    invoke-static {p1, v2}, Lcom/miui/powerkeeper/utils/PackageUtil;->getUidByPackageName(Landroid/content/Context;Ljava/lang/String;)I

    move-result p1

    iput p1, p0, Lcom/miui/powerkeeper/utils/GmsObserver;->mGmsUid:I

    iput-boolean v0, p0, Lcom/miui/powerkeeper/utils/GmsObserver;->mGmsBlocked:Z

    return-void
.end method""",
        'required': True,
        'flag_rewrite_count': 1,
        'reason': 'PowerKeeper smali rule generated from comparison output.',
    },
]
