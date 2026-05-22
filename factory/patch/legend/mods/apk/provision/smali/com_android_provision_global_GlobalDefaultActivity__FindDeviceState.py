TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/global/GlobalDefaultActivity$FindDeviceState.smali'
CLASS_FALLBACK_NAMES = ['GlobalDefaultActivity$FindDeviceState.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/global/GlobalDefaultActivity$State;']

PATCHES = [
    {
        'id': 'com_android_provision_global_GlobalDefaultActivity__FindDeviceState__isAvailable',
        'method': '.method public isAvailable(Z)Z',
        'method_name': 'isAvailable',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-nez v0, :cond_0', 'invoke-super {p0, p1}, Lcom/android/provision/global/GlobalDefaultActivity$State;->isAvailable(Z)Z', 'if-eqz p1, :cond_0', 'iget-object p1, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;', 'invoke-static {p1}, Lcom/android/provision/Utils;->isInProvisionState(Landroid/content/Context;)Z', 'if-nez p1, :cond_0', 'iget-object p1, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;'],
        'type': 'policy_skip',
        'search': """.method public isAvailable(Z)Z
    .registers 4

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    const/4 v1, 0x0

    if-nez v0, :cond_0

    invoke-super {p0, p1}, Lcom/android/provision/global/GlobalDefaultActivity$State;->isAvailable(Z)Z

    move-result p1

    if-eqz p1, :cond_0

    iget-object p1, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {p1}, Lcom/android/provision/Utils;->isInProvisionState(Landroid/content/Context;)Z

    move-result p1

    if-nez p1, :cond_0

    iget-object p1, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {p1}, Lmiui/accounts/ExtraAccountManager;->getXiaomiAccount(Landroid/content/Context;)Landroid/accounts/Account;

    move-result-object p1

    if-eqz p1, :cond_0

    iget-object p1, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    invoke-direct {p0, p1}, Lcom/android/provision/global/GlobalDefaultActivity$FindDeviceState;->getLastSessionUserId(Landroid/content/Context;)Ljava/lang/String;

    move-result-object p1

    invoke-static {p1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result p1

    if-eqz p1, :cond_0

    iget-boolean p1, p0, Lcom/android/provision/global/GlobalDefaultActivity$FindDeviceState;->mPasswordLogin:Z

    if-eqz p1, :cond_0

    iget-object p0, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p0

    const-string p1, "provision_findDevice_enabled"

    invoke-static {p0, p1, v1}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result p0

    if-nez p0, :cond_0

    invoke-static {}, Lcom/android/provision/Utils;->isRedmiDigitOrNoteSeries()Z

    move-result p0

    if-eqz p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    return v1
.end method""",
        'replacement': """.method public isAvailable(Z)Z
    .registers 4

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    const/4 v1, 0x0

    if-nez v0, :cond_0

    invoke-super {p0, p1}, Lcom/android/provision/global/GlobalDefaultActivity$State;->isAvailable(Z)Z

    move-result p1

    if-eqz p1, :cond_0

    iget-object p1, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {p1}, Lcom/android/provision/Utils;->isInProvisionState(Landroid/content/Context;)Z

    move-result p1

    if-nez p1, :cond_0

    iget-object p1, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {p1}, Lmiui/accounts/ExtraAccountManager;->getXiaomiAccount(Landroid/content/Context;)Landroid/accounts/Account;

    move-result-object p1

    if-eqz p1, :cond_0

    iget-object p1, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    invoke-direct {p0, p1}, Lcom/android/provision/global/GlobalDefaultActivity$FindDeviceState;->getLastSessionUserId(Landroid/content/Context;)Ljava/lang/String;

    move-result-object p1

    invoke-static {p1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result p1

    if-eqz p1, :cond_0

    iget-boolean p1, p0, Lcom/android/provision/global/GlobalDefaultActivity$FindDeviceState;->mPasswordLogin:Z

    if-eqz p1, :cond_0

    iget-object p0, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p0

    const-string p1, "provision_findDevice_enabled"

    invoke-static {p0, p1, v1}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result p0

    if-nez p0, :cond_0

    invoke-static {}, Lcom/android/provision/Utils;->isRedmiDigitOrNoteSeries()Z

    move-result p0

    if-eqz p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    return v1
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
]
