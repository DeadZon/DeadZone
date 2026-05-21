TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/activities/DefaultActivity$CloudBackupState.smali'
CLASS_FALLBACK_NAMES = ['DefaultActivity$CloudBackupState.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/activities/DefaultActivity$State;']

PATCHES = [
    {
        'id': 'com_android_provision_activities_DefaultActivity__CloudBackupState__isAvailable',
        'method': '.method public isAvailable(Z)Z',
        'method_name': 'isAvailable',
        'method_anchors': ['sget-boolean v0, Lmiui/enterprise/EnterpriseManagerStub;->ENTERPRISE_ACTIVATED:Z', 'if-eqz v0, :cond_0', 'return v1', 'sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_1', 'return v1', 'invoke-super {p0, p1}, Lcom/android/provision/activities/DefaultActivity$State;->isAvailable(Z)Z', 'if-nez p1, :cond_2'],
        'type': 'policy_skip',
        'search': """.method public isAvailable(Z)Z
    .registers 6

    sget-boolean v0, Lmiui/enterprise/EnterpriseManagerStub;->ENTERPRISE_ACTIVATED:Z

    const/4 v1, 0x0

    if-eqz v0, :cond_0

    return v1

    :cond_0
    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_1

    return v1

    :cond_1
    invoke-super {p0, p1}, Lcom/android/provision/activities/DefaultActivity$State;->isAvailable(Z)Z

    move-result p1

    if-nez p1, :cond_2

    return v1

    :cond_2
    iget-object p1, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {p1}, Lcom/android/provision/activities/DefaultActivity;->checkHuanjiFinish(Landroid/content/Context;)Z

    move-result p1

    const-string v0, "Provision_DefaultActivity"

    if-nez p1, :cond_7

    iget-object p1, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    invoke-virtual {p1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p1

    const-string v2, "key_is_backup_exist"

    const/4 v3, 0x1

    invoke-static {p1, v2, v3}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result p1

    if-eq p1, v3, :cond_3

    goto :goto_0

    :cond_3
    iget-object p1, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {p1}, Lcom/android/provision/Utils;->isNetworkAvailable(Landroid/content/Context;)Z

    move-result p1

    if-nez p1, :cond_4

    iget-object p1, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    invoke-virtual {p1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p1

    const-string v2, "huanji_request_cache"

    invoke-static {p1, v2, v1}, Landroid/provider/Settings$Secure;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result p1

    if-eq p1, v3, :cond_4

    const-string p0, "CloudBackupState skip, because network unavailable or huanji_request_cache is 0"

    invoke-static {v0, p0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    return v1

    :cond_4
    invoke-static {}, Lcom/android/provision/activities/DefaultActivity;->-$$Nest$sfgetMiMoverDirect()I

    move-result p1

    const/4 v0, 0x2

    if-ne p1, v0, :cond_6

    invoke-virtual {p0}, Lcom/android/provision/activities/DefaultActivity$CloudBackupState;->isAccountExist()Z

    move-result p1

    if-nez p1, :cond_5

    iget-object p1, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {p1}, Lcom/android/provision/activities/DefaultActivity$CloudBackupState;->isHuanjiRestoreSupported(Landroid/content/Context;)Z

    move-result p1

    if-eqz p1, :cond_6

    :cond_5
    iget-object p0, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    const-string p1, "com.xiaomi.account"

    invoke-static {p0, p1}, Lcom/android/provision/Utils;->queryCTAStatus(Landroid/content/Context;Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_6

    return v3

    :cond_6
    return v1

    :cond_7
    :goto_0
    const-string p0, "CloudBackupState skip, because huanji is finish or key_is_backup_exist is 0"

    invoke-static {v0, p0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    return v1
.end method""",
        'replacement': """.method public isAvailable(Z)Z
    .registers 6

    sget-boolean v0, Lmiui/enterprise/EnterpriseManagerStub;->ENTERPRISE_ACTIVATED:Z

    const/4 v1, 0x0

    if-eqz v0, :cond_0

    return v1

    :cond_0
    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_1

    return v1

    :cond_1
    invoke-super {p0, p1}, Lcom/android/provision/activities/DefaultActivity$State;->isAvailable(Z)Z

    move-result p1

    if-nez p1, :cond_2

    return v1

    :cond_2
    iget-object p1, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {p1}, Lcom/android/provision/activities/DefaultActivity;->checkHuanjiFinish(Landroid/content/Context;)Z

    move-result p1

    const-string v0, "Provision_DefaultActivity"

    if-nez p1, :cond_7

    iget-object p1, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    invoke-virtual {p1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p1

    const-string v2, "key_is_backup_exist"

    const/4 v3, 0x1

    invoke-static {p1, v2, v3}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result p1

    if-eq p1, v3, :cond_3

    goto :goto_0

    :cond_3
    iget-object p1, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {p1}, Lcom/android/provision/Utils;->isNetworkAvailable(Landroid/content/Context;)Z

    move-result p1

    if-nez p1, :cond_4

    iget-object p1, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    invoke-virtual {p1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p1

    const-string v2, "huanji_request_cache"

    invoke-static {p1, v2, v1}, Landroid/provider/Settings$Secure;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result p1

    if-eq p1, v3, :cond_4

    const-string p0, "CloudBackupState skip, because network unavailable or huanji_request_cache is 0"

    invoke-static {v0, p0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    return v1

    :cond_4
    invoke-static {}, Lcom/android/provision/activities/DefaultActivity;->-$$Nest$sfgetMiMoverDirect()I

    move-result p1

    const/4 v0, 0x2

    if-ne p1, v0, :cond_6

    invoke-virtual {p0}, Lcom/android/provision/activities/DefaultActivity$CloudBackupState;->isAccountExist()Z

    move-result p1

    if-nez p1, :cond_5

    iget-object p1, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {p1}, Lcom/android/provision/activities/DefaultActivity$CloudBackupState;->isHuanjiRestoreSupported(Landroid/content/Context;)Z

    move-result p1

    if-eqz p1, :cond_6

    :cond_5
    iget-object p0, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    const-string p1, "com.xiaomi.account"

    invoke-static {p0, p1}, Lcom/android/provision/Utils;->queryCTAStatus(Landroid/content/Context;Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_6

    return v3

    :cond_6
    return v1

    :cond_7
    :goto_0
    const-string p0, "CloudBackupState skip, because huanji is finish or key_is_backup_exist is 0"

    invoke-static {v0, p0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    return v1
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_activities_DefaultActivity__CloudBackupState__isHuanjiRestoreSupported',
        'method': '.method public static isHuanjiRestoreSupported(Landroid/content/Context;)Z',
        'method_name': 'isHuanjiRestoreSupported',
        'method_anchors': ['if-eqz p0, :cond_2', 'sget-boolean v1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-nez v1, :cond_2', 'invoke-static {}, Lcom/android/provision/Utils;->isTabletDevice()Z', 'if-eqz v1, :cond_0', 'new-instance v1, Landroid/content/Intent;', 'const-string v2, "com.intent.action.HuanjiProvision"', 'invoke-direct {v1, v2}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V'],
        'type': 'policy_skip',
        'search': """.method public static isHuanjiRestoreSupported(Landroid/content/Context;)Z
    .registers 4

    const/4 v0, 0x0

    if-eqz p0, :cond_2

    sget-boolean v1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v1, :cond_2

    invoke-static {}, Lcom/android/provision/Utils;->isTabletDevice()Z

    move-result v1

    if-eqz v1, :cond_0

    goto :goto_0

    :cond_0
    new-instance v1, Landroid/content/Intent;

    const-string v2, "com.intent.action.HuanjiProvision"

    invoke-direct {v1, v2}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    const-string v2, "com.miui.huanji"

    invoke-virtual {v1, v2}, Landroid/content/Intent;->setPackage(Ljava/lang/String;)Landroid/content/Intent;

    invoke-virtual {p0}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object p0

    invoke-virtual {v1, p0}, Landroid/content/Intent;->resolveActivity(Landroid/content/pm/PackageManager;)Landroid/content/ComponentName;

    move-result-object p0

    if-nez p0, :cond_1

    return v0

    :cond_1
    const/4 p0, 0x1

    return p0

    :cond_2
    :goto_0
    return v0
.end method""",
        'replacement': """.method public static isHuanjiRestoreSupported(Landroid/content/Context;)Z
    .registers 4

    const/4 v0, 0x0

    if-eqz p0, :cond_2

    sget-boolean v1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v1, :cond_2

    invoke-static {}, Lcom/android/provision/Utils;->isTabletDevice()Z

    move-result v1

    if-eqz v1, :cond_0

    goto :goto_0

    :cond_0
    new-instance v1, Landroid/content/Intent;

    const-string v2, "com.intent.action.HuanjiProvision"

    invoke-direct {v1, v2}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    const-string v2, "com.miui.huanji"

    invoke-virtual {v1, v2}, Landroid/content/Intent;->setPackage(Ljava/lang/String;)Landroid/content/Intent;

    invoke-virtual {p0}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object p0

    invoke-virtual {v1, p0}, Landroid/content/Intent;->resolveActivity(Landroid/content/pm/PackageManager;)Landroid/content/ComponentName;

    move-result-object p0

    if-nez p0, :cond_1

    return v0

    :cond_1
    const/4 p0, 0x1

    return p0

    :cond_2
    :goto_0
    return v0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
]
