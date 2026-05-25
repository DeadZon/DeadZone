TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/utils/NetworkUtils.smali'
CLASS_FALLBACK_NAMES = ['NetworkUtils.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field private static final TAG:Ljava/lang/String; = "NetworkUtils"', '.field private static final lock:Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'com_android_provision_utils_NetworkUtils__isCaptivePortalValidated',
        'method': '.method public static isCaptivePortalValidated(Landroid/content/Context;)Z',
        'method_name': 'isCaptivePortalValidated',
        'method_anchors': ['const-string v0, "connectivity"', 'invoke-virtual {p0, v0}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;', 'check-cast v0, Landroid/net/ConnectivityManager;', 'invoke-virtual {v0}, Landroid/net/ConnectivityManager;->getActiveNetworkInfo()Landroid/net/NetworkInfo;', 'const-string v3, "NetworkUtils"', 'if-eqz v1, :cond_5', 'invoke-virtual {v1}, Landroid/net/NetworkInfo;->isConnected()Z', 'if-nez v4, :cond_0'],
        'type': 'policy_skip',
        'search': """.method public static isCaptivePortalValidated(Landroid/content/Context;)Z
    .registers 6

    const-string v0, "connectivity"

    invoke-virtual {p0, v0}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/net/ConnectivityManager;

    invoke-virtual {v0}, Landroid/net/ConnectivityManager;->getActiveNetworkInfo()Landroid/net/NetworkInfo;

    move-result-object v1

    const/4 v2, 0x0

    const-string v3, "NetworkUtils"

    if-eqz v1, :cond_5

    invoke-virtual {v1}, Landroid/net/NetworkInfo;->isConnected()Z

    move-result v4

    if-nez v4, :cond_0

    goto :goto_1

    :cond_0
    invoke-virtual {v1}, Landroid/net/NetworkInfo;->getType()I

    move-result v1

    if-nez v1, :cond_1

    const-string p0, "mobile network"

    invoke-static {v3, p0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    const/4 p0, 0x1

    return p0

    :cond_1
    invoke-virtual {p0}, Landroid/content/Context;->getApplicationContext()Landroid/content/Context;

    move-result-object p0

    const-string v1, "wifi"

    invoke-virtual {p0, v1}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object p0

    check-cast p0, Landroid/net/wifi/WifiManager;

    invoke-virtual {p0}, Landroid/net/wifi/WifiManager;->getConnectionInfo()Landroid/net/wifi/WifiInfo;

    move-result-object v1

    if-eqz v1, :cond_4

    invoke-virtual {v1}, Landroid/net/wifi/WifiInfo;->getNetworkId()I

    move-result v1

    if-gez v1, :cond_2

    goto :goto_0

    :cond_2
    sget-boolean v1, Lmiui/os/Build;->IS_TABLET:Z

    if-eqz v1, :cond_3

    sget-boolean v1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v1, :cond_3

    const-string v1, "tablet check wifiNetworkAvailable"

    invoke-static {v3, v1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    invoke-static {p0, v0}, Lcom/android/provision/utils/NetworkUtils;->checkTableWifiNetworkAvailable(Landroid/net/wifi/WifiManager;Landroid/net/ConnectivityManager;)Z

    move-result p0

    return p0

    :cond_3
    invoke-static {p0, v0}, Lcom/android/provision/utils/NetworkUtils;->wifiNetworkAvailable(Landroid/net/wifi/WifiManager;Landroid/net/ConnectivityManager;)Z

    move-result p0

    return p0

    :cond_4
    :goto_0
    const-string p0, " not found network id"

    invoke-static {v3, p0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    return v2

    :cond_5
    :goto_1
    const-string p0, "network not Connected"

    invoke-static {v3, p0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    return v2
.end method""",
        'replacement': """.method public static isCaptivePortalValidated(Landroid/content/Context;)Z
    .registers 6

    const-string v0, "connectivity"

    invoke-virtual {p0, v0}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/net/ConnectivityManager;

    invoke-virtual {v0}, Landroid/net/ConnectivityManager;->getActiveNetworkInfo()Landroid/net/NetworkInfo;

    move-result-object v1

    const/4 v2, 0x0

    const-string v3, "NetworkUtils"

    if-eqz v1, :cond_5

    invoke-virtual {v1}, Landroid/net/NetworkInfo;->isConnected()Z

    move-result v4

    if-nez v4, :cond_0

    goto :goto_1

    :cond_0
    invoke-virtual {v1}, Landroid/net/NetworkInfo;->getType()I

    move-result v1

    if-nez v1, :cond_1

    const-string p0, "mobile network"

    invoke-static {v3, p0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    const/4 p0, 0x1

    return p0

    :cond_1
    invoke-virtual {p0}, Landroid/content/Context;->getApplicationContext()Landroid/content/Context;

    move-result-object p0

    const-string v1, "wifi"

    invoke-virtual {p0, v1}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object p0

    check-cast p0, Landroid/net/wifi/WifiManager;

    invoke-virtual {p0}, Landroid/net/wifi/WifiManager;->getConnectionInfo()Landroid/net/wifi/WifiInfo;

    move-result-object v1

    if-eqz v1, :cond_4

    invoke-virtual {v1}, Landroid/net/wifi/WifiInfo;->getNetworkId()I

    move-result v1

    if-gez v1, :cond_2

    goto :goto_0

    :cond_2
    sget-boolean v1, Lmiui/os/Build;->IS_TABLET:Z

    if-eqz v1, :cond_3

    sget-boolean v1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v1, :cond_3

    const-string v1, "tablet check wifiNetworkAvailable"

    invoke-static {v3, v1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    invoke-static {p0, v0}, Lcom/android/provision/utils/NetworkUtils;->checkTableWifiNetworkAvailable(Landroid/net/wifi/WifiManager;Landroid/net/ConnectivityManager;)Z

    move-result p0

    return p0

    :cond_3
    invoke-static {p0, v0}, Lcom/android/provision/utils/NetworkUtils;->wifiNetworkAvailable(Landroid/net/wifi/WifiManager;Landroid/net/ConnectivityManager;)Z

    move-result p0

    return p0

    :cond_4
    :goto_0
    const-string p0, " not found network id"

    invoke-static {v3, p0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    return v2

    :cond_5
    :goto_1
    const-string p0, "network not Connected"

    invoke-static {v3, p0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    return v2
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
]
