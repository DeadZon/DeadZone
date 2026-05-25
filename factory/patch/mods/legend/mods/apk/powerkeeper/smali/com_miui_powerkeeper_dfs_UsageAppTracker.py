TARGET_APK = 'PowerKeeper.apk'
TARGET_CLASS = 'com/miui/powerkeeper/dfs/UsageAppTracker.smali'
CLASS_FALLBACK_NAMES = ['UsageAppTracker.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field public static final MSG_DELAY_FOR_STABILIZED:I = 0x0', '.field public static final REASONS:[Ljava/lang/String;', '.field public static final REASON_INDEX_RADIO_SIGNAL:I = 0x1', '.field public static final REASON_INDEX_WIFI_SIGNAL:I = 0x0', '.field public static final TAG:Ljava/lang/String; = "DFS-AppUsageTracker"']

PATCHES = [
    {
        'id': 'com_miui_powerkeeper_dfs_UsageAppTracker__init',
        'method': '.method public constructor <init>(Lcom/miui/powerkeeper/dfs/CloudData;Lcom/miui/powerkeeper/dfs/UsageManager;Landroid/os/Looper;)V',
        'method_name': '<init>',
        'method_anchors': ['invoke-direct {p0}, Ljava/lang/Object;-><init>()V', 'new-instance v0, Ljava/lang/Object;', 'invoke-direct {v0}, Ljava/lang/Object;-><init>()V', 'iput-object v0, p0, Lcom/miui/powerkeeper/dfs/UsageAppTracker;->mTrackingLock:Ljava/lang/Object;', 'iput-object v0, p0, Lcom/miui/powerkeeper/dfs/UsageAppTracker;->mTrackingData:Lcom/miui/powerkeeper/dfs/UsageAppTracker$TrackingData;', 'iput-boolean v0, p0, Lcom/miui/powerkeeper/dfs/UsageAppTracker;->mOnBattery:Z', 'iput-boolean v0, p0, Lcom/miui/powerkeeper/dfs/UsageAppTracker;->mScreenOff:Z', 'iput-boolean v0, p0, Lcom/miui/powerkeeper/dfs/UsageAppTracker;->mVpnEnabled:Z'],
        'type': 'method_replace',
        'search': """.method public constructor <init>(Lcom/miui/powerkeeper/dfs/CloudData;Lcom/miui/powerkeeper/dfs/UsageManager;Landroid/os/Looper;)V
    .registers 6

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    new-instance v0, Ljava/lang/Object;

    invoke-direct {v0}, Ljava/lang/Object;-><init>()V

    iput-object v0, p0, Lcom/miui/powerkeeper/dfs/UsageAppTracker;->mTrackingLock:Ljava/lang/Object;

    const/4 v0, 0x0

    iput-object v0, p0, Lcom/miui/powerkeeper/dfs/UsageAppTracker;->mTrackingData:Lcom/miui/powerkeeper/dfs/UsageAppTracker$TrackingData;

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/miui/powerkeeper/dfs/UsageAppTracker;->mOnBattery:Z

    iput-boolean v0, p0, Lcom/miui/powerkeeper/dfs/UsageAppTracker;->mScreenOff:Z

    iput-boolean v0, p0, Lcom/miui/powerkeeper/dfs/UsageAppTracker;->mVpnEnabled:Z

    iput-boolean v0, p0, Lcom/miui/powerkeeper/dfs/UsageAppTracker;->mWifiApEnabled:Z

    const-wide/16 v0, 0x0

    iput-wide v0, p0, Lcom/miui/powerkeeper/dfs/UsageAppTracker;->mWifiApDurationMs:J

    iput-wide v0, p0, Lcom/miui/powerkeeper/dfs/UsageAppTracker;->mWifiApStartTime:J

    iput-object p1, p0, Lcom/miui/powerkeeper/dfs/UsageAppTracker;->mCloudData:Lcom/miui/powerkeeper/dfs/CloudData;

    iput-object p2, p0, Lcom/miui/powerkeeper/dfs/UsageAppTracker;->mUsageManager:Lcom/miui/powerkeeper/dfs/UsageManager;

    invoke-static {}, Lcom/miui/powerkeeper/PowerKeeperApplication;->b()Landroid/content/Context;

    move-result-object p1

    iput-object p1, p0, Lcom/miui/powerkeeper/dfs/UsageAppTracker;->mContext:Landroid/content/Context;

    sget-boolean p2, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz p2, :cond_0

    const p2, 0x7f010001

    goto :goto_0

    :cond_0
    const/high16 p2, 0x7f010000

    :goto_0
    sget-object v0, Lcom/miui/powerkeeper/dfs/UsageAppTracker;->TRACKING_APPS:Ljava/util/ArrayList;

    invoke-virtual {p1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v1

    invoke-virtual {v1, p2}, Landroid/content/res/Resources;->getStringArray(I)[Ljava/lang/String;

    move-result-object p2

    invoke-static {p2}, Ljava/util/Arrays;->asList([Ljava/lang/Object;)Ljava/util/List;

    move-result-object p2

    invoke-virtual {v0, p2}, Ljava/util/ArrayList;->addAll(Ljava/util/Collection;)Z

    invoke-static {}, Lcom/miui/powerkeeper/PowerKeeperManager;->getInstance()Lcom/miui/powerkeeper/PowerKeeperManager;

    move-result-object p2

    invoke-virtual {p2}, Lcom/miui/powerkeeper/PowerKeeperManager;->isCharging()Z

    move-result p2

    const/4 v0, 0x1

    xor-int/2addr p2, v0

    iput-boolean p2, p0, Lcom/miui/powerkeeper/dfs/UsageAppTracker;->mOnBattery:Z

    const-class p2, Landroid/net/wifi/WifiManager;

    invoke-virtual {p1, p2}, Landroid/content/Context;->getSystemService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object p2

    check-cast p2, Landroid/net/wifi/WifiManager;

    if-eqz p2, :cond_1

    invoke-virtual {p2}, Landroid/net/wifi/WifiManager;->isWifiApEnabled()Z

    move-result p2

    iput-boolean p2, p0, Lcom/miui/powerkeeper/dfs/UsageAppTracker;->mWifiApEnabled:Z

    :cond_1
    const/16 p2, 0x68

    invoke-static {p2}, Lcom/miui/powerkeeper/siming/Subdivisions;->isDisabled(I)Z

    move-result v1

    if-eqz v1, :cond_2

    invoke-static {}, Lcom/miui/powerkeeper/siming/SiMing;->getInstance()Lcom/miui/powerkeeper/siming/SiMing;

    move-result-object v1

    invoke-virtual {v1, p2, v0}, Lcom/miui/powerkeeper/siming/SiMing;->update(IZ)V

    :cond_2
    new-instance p2, Lcom/miui/powerkeeper/dfs/UsageAppTracker$1;

    invoke-direct {p2, p0, p3}, Lcom/miui/powerkeeper/dfs/UsageAppTracker$1;-><init>(Lcom/miui/powerkeeper/dfs/UsageAppTracker;Landroid/os/Looper;)V

    iput-object p2, p0, Lcom/miui/powerkeeper/dfs/UsageAppTracker;->mHandler:Landroid/os/Handler;

    invoke-static {p1}, Lcom/miui/powerkeeper/dfs/UsageMonitor;->getInstance(Landroid/content/Context;)Lcom/miui/powerkeeper/dfs/UsageMonitor;

    move-result-object p1

    new-instance p2, Lcom/miui/powerkeeper/dfs/c;

    invoke-direct {p2, p0}, Lcom/miui/powerkeeper/dfs/c;-><init>(Lcom/miui/powerkeeper/dfs/UsageAppTracker;)V

    invoke-virtual {p1, p2}, Lcom/miui/powerkeeper/dfs/UsageMonitor;->registerUsageCallback(Lcom/miui/powerkeeper/dfs/UsageMonitor$UsageCallback;)V

    return-void
.end method""",
        'replacement': """.method public constructor <init>(Lcom/miui/powerkeeper/dfs/CloudData;Lcom/miui/powerkeeper/dfs/UsageManager;Landroid/os/Looper;)V
    .registers 6

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    new-instance v0, Ljava/lang/Object;

    invoke-direct {v0}, Ljava/lang/Object;-><init>()V

    iput-object v0, p0, Lcom/miui/powerkeeper/dfs/UsageAppTracker;->mTrackingLock:Ljava/lang/Object;

    const/4 v0, 0x0

    iput-object v0, p0, Lcom/miui/powerkeeper/dfs/UsageAppTracker;->mTrackingData:Lcom/miui/powerkeeper/dfs/UsageAppTracker$TrackingData;

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/miui/powerkeeper/dfs/UsageAppTracker;->mOnBattery:Z

    iput-boolean v0, p0, Lcom/miui/powerkeeper/dfs/UsageAppTracker;->mScreenOff:Z

    iput-boolean v0, p0, Lcom/miui/powerkeeper/dfs/UsageAppTracker;->mVpnEnabled:Z

    iput-boolean v0, p0, Lcom/miui/powerkeeper/dfs/UsageAppTracker;->mWifiApEnabled:Z

    const-wide/16 v0, 0x0

    iput-wide v0, p0, Lcom/miui/powerkeeper/dfs/UsageAppTracker;->mWifiApDurationMs:J

    iput-wide v0, p0, Lcom/miui/powerkeeper/dfs/UsageAppTracker;->mWifiApStartTime:J

    iput-object p1, p0, Lcom/miui/powerkeeper/dfs/UsageAppTracker;->mCloudData:Lcom/miui/powerkeeper/dfs/CloudData;

    iput-object p2, p0, Lcom/miui/powerkeeper/dfs/UsageAppTracker;->mUsageManager:Lcom/miui/powerkeeper/dfs/UsageManager;

    invoke-static {}, Lcom/miui/powerkeeper/PowerKeeperApplication;->b()Landroid/content/Context;

    move-result-object p1

    iput-object p1, p0, Lcom/miui/powerkeeper/dfs/UsageAppTracker;->mContext:Landroid/content/Context;

    sget-boolean p2, Lmiui/os/Build;->IS_MIUI:Z

    if-eqz p2, :cond_0

    const p2, 0x7f010001

    goto :goto_0

    :cond_0
    const/high16 p2, 0x7f010000

    :goto_0
    sget-object v0, Lcom/miui/powerkeeper/dfs/UsageAppTracker;->TRACKING_APPS:Ljava/util/ArrayList;

    invoke-virtual {p1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v1

    invoke-virtual {v1, p2}, Landroid/content/res/Resources;->getStringArray(I)[Ljava/lang/String;

    move-result-object p2

    invoke-static {p2}, Ljava/util/Arrays;->asList([Ljava/lang/Object;)Ljava/util/List;

    move-result-object p2

    invoke-virtual {v0, p2}, Ljava/util/ArrayList;->addAll(Ljava/util/Collection;)Z

    invoke-static {}, Lcom/miui/powerkeeper/PowerKeeperManager;->getInstance()Lcom/miui/powerkeeper/PowerKeeperManager;

    move-result-object p2

    invoke-virtual {p2}, Lcom/miui/powerkeeper/PowerKeeperManager;->isCharging()Z

    move-result p2

    const/4 v0, 0x1

    xor-int/2addr p2, v0

    iput-boolean p2, p0, Lcom/miui/powerkeeper/dfs/UsageAppTracker;->mOnBattery:Z

    const-class p2, Landroid/net/wifi/WifiManager;

    invoke-virtual {p1, p2}, Landroid/content/Context;->getSystemService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object p2

    check-cast p2, Landroid/net/wifi/WifiManager;

    if-eqz p2, :cond_1

    invoke-virtual {p2}, Landroid/net/wifi/WifiManager;->isWifiApEnabled()Z

    move-result p2

    iput-boolean p2, p0, Lcom/miui/powerkeeper/dfs/UsageAppTracker;->mWifiApEnabled:Z

    :cond_1
    const/16 p2, 0x68

    invoke-static {p2}, Lcom/miui/powerkeeper/siming/Subdivisions;->isDisabled(I)Z

    move-result v1

    if-eqz v1, :cond_2

    invoke-static {}, Lcom/miui/powerkeeper/siming/SiMing;->getInstance()Lcom/miui/powerkeeper/siming/SiMing;

    move-result-object v1

    invoke-virtual {v1, p2, v0}, Lcom/miui/powerkeeper/siming/SiMing;->update(IZ)V

    :cond_2
    new-instance p2, Lcom/miui/powerkeeper/dfs/UsageAppTracker$1;

    invoke-direct {p2, p0, p3}, Lcom/miui/powerkeeper/dfs/UsageAppTracker$1;-><init>(Lcom/miui/powerkeeper/dfs/UsageAppTracker;Landroid/os/Looper;)V

    iput-object p2, p0, Lcom/miui/powerkeeper/dfs/UsageAppTracker;->mHandler:Landroid/os/Handler;

    invoke-static {p1}, Lcom/miui/powerkeeper/dfs/UsageMonitor;->getInstance(Landroid/content/Context;)Lcom/miui/powerkeeper/dfs/UsageMonitor;

    move-result-object p1

    new-instance p2, Lcom/miui/powerkeeper/dfs/c;

    invoke-direct {p2, p0}, Lcom/miui/powerkeeper/dfs/c;-><init>(Lcom/miui/powerkeeper/dfs/UsageAppTracker;)V

    invoke-virtual {p1, p2}, Lcom/miui/powerkeeper/dfs/UsageMonitor;->registerUsageCallback(Lcom/miui/powerkeeper/dfs/UsageMonitor$UsageCallback;)V

    return-void
.end method""",
        'required': True,
        'flag_rewrite_count': 1,
        'reason': 'PowerKeeper smali rule generated from comparison output.',
    },
]
