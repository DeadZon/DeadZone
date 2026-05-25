TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/ble/BleManager.smali'
CLASS_FALLBACK_NAMES = ['BleManager.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field private static final IS_MIUI:Z', '.field private static final KEY_MSG_DATA_CONTENT:Ljava/lang/String; = "ble_content"', '.field private static final KEY_MSG_DATA_TRYCOUNT:Ljava/lang/String; = "ble_try_count"', '.field private static final KEY_MSG_MANUFACTURER_ID:Ljava/lang/String; = "manufacturer_id"', '.field public static final MANUFACTURER_SPECIFIC_DATA_ID:I = 0x2bc']

PATCHES = [
    {
        'id': 'com_android_provision_ble_BleManager__initAndOpenBluetooth',
        'method': '.method public initAndOpenBluetooth(Landroid/content/Context;)V',
        'method_name': 'initAndOpenBluetooth',
        'method_anchors': ['const-string v0, "init"', 'const-string v1, "BleManager"', 'invoke-static {v1, v0}, Lcom/android/provision/ble/utils/LogUtils;->d(Ljava/lang/String;Ljava/lang/String;)V', 'sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-nez v0, :cond_4', 'sget-boolean v0, Lcom/android/provision/ble/BleManager;->IS_MIUI:Z', 'if-nez v0, :cond_0', 'invoke-static {p1}, Lcom/android/provision/ble/utils/BleUtils;->isSupportBle(Landroid/content/Context;)Z'],
        'type': 'policy_skip',
        'search': """.method public initAndOpenBluetooth(Landroid/content/Context;)V
    .registers 4

    const-string v0, "init"

    const-string v1, "BleManager"

    invoke-static {v1, v0}, Lcom/android/provision/ble/utils/LogUtils;->d(Ljava/lang/String;Ljava/lang/String;)V

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_4

    sget-boolean v0, Lcom/android/provision/ble/BleManager;->IS_MIUI:Z

    if-nez v0, :cond_0

    goto :goto_0

    :cond_0
    invoke-static {p1}, Lcom/android/provision/ble/utils/BleUtils;->isSupportBle(Landroid/content/Context;)Z

    move-result v0

    if-nez v0, :cond_1

    const-string p0, "init failed, ble not supported"

    invoke-static {v1, p0}, Lcom/android/provision/ble/utils/LogUtils;->w(Ljava/lang/String;Ljava/lang/String;)V

    return-void

    :cond_1
    invoke-static {}, Lcom/android/provision/ble/utils/BleUtils;->isBluetoothEnabled()Z

    move-result v0

    if-eqz v0, :cond_2

    invoke-static {}, Lcom/android/provision/ble/utils/BleUtils;->isBleEnabled()Z

    move-result v0

    if-nez v0, :cond_3

    :cond_2
    invoke-static {}, Lcom/android/provision/ble/utils/BleUtils;->enableBluetooth()Z

    invoke-static {}, Lcom/android/provision/ble/utils/BleUtils;->enable()Z

    :cond_3
    invoke-virtual {p0, p1}, Lcom/android/provision/ble/BleManager;->initOnlyForAdvertise(Landroid/content/Context;)V

    :cond_4
    :goto_0
    return-void
.end method""",
        'replacement': """.method public initAndOpenBluetooth(Landroid/content/Context;)V
    .registers 4

    const-string v0, "init"

    const-string v1, "BleManager"

    invoke-static {v1, v0}, Lcom/android/provision/ble/utils/LogUtils;->d(Ljava/lang/String;Ljava/lang/String;)V

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_4

    sget-boolean v0, Lcom/android/provision/ble/BleManager;->IS_MIUI:Z

    if-nez v0, :cond_0

    goto :goto_0

    :cond_0
    invoke-static {p1}, Lcom/android/provision/ble/utils/BleUtils;->isSupportBle(Landroid/content/Context;)Z

    move-result v0

    if-nez v0, :cond_1

    const-string p0, "init failed, ble not supported"

    invoke-static {v1, p0}, Lcom/android/provision/ble/utils/LogUtils;->w(Ljava/lang/String;Ljava/lang/String;)V

    return-void

    :cond_1
    invoke-static {}, Lcom/android/provision/ble/utils/BleUtils;->isBluetoothEnabled()Z

    move-result v0

    if-eqz v0, :cond_2

    invoke-static {}, Lcom/android/provision/ble/utils/BleUtils;->isBleEnabled()Z

    move-result v0

    if-nez v0, :cond_3

    :cond_2
    invoke-static {}, Lcom/android/provision/ble/utils/BleUtils;->enableBluetooth()Z

    invoke-static {}, Lcom/android/provision/ble/utils/BleUtils;->enable()Z

    :cond_3
    invoke-virtual {p0, p1}, Lcom/android/provision/ble/BleManager;->initOnlyForAdvertise(Landroid/content/Context;)V

    :cond_4
    :goto_0
    return-void
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_ble_BleManager__initOnlyForAdvertise',
        'method': '.method public initOnlyForAdvertise(Landroid/content/Context;)V',
        'method_name': 'initOnlyForAdvertise',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-nez v0, :cond_3', 'sget-boolean v0, Lmiui/os/Build;->IS_MIUI:Z', 'if-nez v0, :cond_0', 'invoke-static {}, Lcom/android/provision/ble/utils/BleUtils;->isBluetoothEnabled()Z', 'iput-boolean v0, p0, Lcom/android/provision/ble/BleManager;->mBluetoothInitialStatus:Z', 'iput-object p1, p0, Lcom/android/provision/ble/BleManager;->mContext:Landroid/content/Context;', 'iget-object p1, p0, Lcom/android/provision/ble/BleManager;->mWorkHandlerThread:Landroid/os/HandlerThread;'],
        'type': 'policy_skip',
        'search': """.method public initOnlyForAdvertise(Landroid/content/Context;)V
    .registers 3

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_3

    sget-boolean v0, Lmiui/os/Build;->IS_MIUI:Z

    if-nez v0, :cond_0

    goto :goto_2

    :cond_0
    invoke-static {}, Lcom/android/provision/ble/utils/BleUtils;->isBluetoothEnabled()Z

    move-result v0

    iput-boolean v0, p0, Lcom/android/provision/ble/BleManager;->mBluetoothInitialStatus:Z

    iput-object p1, p0, Lcom/android/provision/ble/BleManager;->mContext:Landroid/content/Context;

    monitor-enter p0

    :try_start_0
    iget-object p1, p0, Lcom/android/provision/ble/BleManager;->mWorkHandlerThread:Landroid/os/HandlerThread;

    if-nez p1, :cond_1

    new-instance p1, Landroid/os/HandlerThread;

    const-string v0, "workThread"

    invoke-direct {p1, v0}, Landroid/os/HandlerThread;-><init>(Ljava/lang/String;)V

    iput-object p1, p0, Lcom/android/provision/ble/BleManager;->mWorkHandlerThread:Landroid/os/HandlerThread;

    invoke-virtual {p1}, Landroid/os/HandlerThread;->start()V

    goto :goto_0

    :catchall_0
    move-exception p1

    goto :goto_1

    :cond_1
    :goto_0
    iget-object p1, p0, Lcom/android/provision/ble/BleManager;->mHandler:Landroid/os/Handler;

    if-nez p1, :cond_2

    new-instance p1, Lcom/android/provision/ble/BleManager$1;

    iget-object v0, p0, Lcom/android/provision/ble/BleManager;->mWorkHandlerThread:Landroid/os/HandlerThread;

    invoke-virtual {v0}, Landroid/os/HandlerThread;->getLooper()Landroid/os/Looper;

    move-result-object v0

    invoke-direct {p1, p0, v0}, Lcom/android/provision/ble/BleManager$1;-><init>(Lcom/android/provision/ble/BleManager;Landroid/os/Looper;)V

    iput-object p1, p0, Lcom/android/provision/ble/BleManager;->mHandler:Landroid/os/Handler;

    :cond_2
    monitor-exit p0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    const/4 p1, 0x0

    iput-object p1, p0, Lcom/android/provision/ble/BleManager;->mBLEDataFilter:Lcom/android/provision/ble/utils/BleUtils$BLEDataFilter;

    return-void

    :goto_1
    :try_start_1
    monitor-exit p0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    throw p1

    :cond_3
    :goto_2
    return-void
.end method""",
        'replacement': """.method public initOnlyForAdvertise(Landroid/content/Context;)V
    .registers 3

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_3

    sget-boolean v0, Lmiui/os/Build;->IS_MIUI:Z

    if-nez v0, :cond_0

    goto :goto_2

    :cond_0
    invoke-static {}, Lcom/android/provision/ble/utils/BleUtils;->isBluetoothEnabled()Z

    move-result v0

    iput-boolean v0, p0, Lcom/android/provision/ble/BleManager;->mBluetoothInitialStatus:Z

    iput-object p1, p0, Lcom/android/provision/ble/BleManager;->mContext:Landroid/content/Context;

    monitor-enter p0

    :try_start_0
    iget-object p1, p0, Lcom/android/provision/ble/BleManager;->mWorkHandlerThread:Landroid/os/HandlerThread;

    if-nez p1, :cond_1

    new-instance p1, Landroid/os/HandlerThread;

    const-string v0, "workThread"

    invoke-direct {p1, v0}, Landroid/os/HandlerThread;-><init>(Ljava/lang/String;)V

    iput-object p1, p0, Lcom/android/provision/ble/BleManager;->mWorkHandlerThread:Landroid/os/HandlerThread;

    invoke-virtual {p1}, Landroid/os/HandlerThread;->start()V

    goto :goto_0

    :catchall_0
    move-exception p1

    goto :goto_1

    :cond_1
    :goto_0
    iget-object p1, p0, Lcom/android/provision/ble/BleManager;->mHandler:Landroid/os/Handler;

    if-nez p1, :cond_2

    new-instance p1, Lcom/android/provision/ble/BleManager$1;

    iget-object v0, p0, Lcom/android/provision/ble/BleManager;->mWorkHandlerThread:Landroid/os/HandlerThread;

    invoke-virtual {v0}, Landroid/os/HandlerThread;->getLooper()Landroid/os/Looper;

    move-result-object v0

    invoke-direct {p1, p0, v0}, Lcom/android/provision/ble/BleManager$1;-><init>(Lcom/android/provision/ble/BleManager;Landroid/os/Looper;)V

    iput-object p1, p0, Lcom/android/provision/ble/BleManager;->mHandler:Landroid/os/Handler;

    :cond_2
    monitor-exit p0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    const/4 p1, 0x0

    iput-object p1, p0, Lcom/android/provision/ble/BleManager;->mBLEDataFilter:Lcom/android/provision/ble/utils/BleUtils$BLEDataFilter;

    return-void

    :goto_1
    :try_start_1
    monitor-exit p0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    throw p1

    :cond_3
    :goto_2
    return-void
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
]
