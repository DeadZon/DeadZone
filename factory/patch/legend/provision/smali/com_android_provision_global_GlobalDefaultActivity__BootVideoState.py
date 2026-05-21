TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/global/GlobalDefaultActivity$BootVideoState.smali'
CLASS_FALLBACK_NAMES = ['GlobalDefaultActivity$BootVideoState.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/global/GlobalDefaultActivity$State;']

PATCHES = [
    {
        'id': 'com_android_provision_global_GlobalDefaultActivity__BootVideoState__isAvailable',
        'method': '.method public isAvailable(Z)Z',
        'method_name': 'isAvailable',
        'method_anchors': ['invoke-super {p0, p1}, Lcom/android/provision/global/GlobalDefaultActivity$State;->isAvailable(Z)Z', 'if-eqz p1, :cond_1', 'sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz p1, :cond_0', 'iget-object p1, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;', 'invoke-virtual {p1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;', 'sget v1, Lcom/android/provision/R$bool;->support_boot_video:I', 'invoke-virtual {p1, v1}, Landroid/content/res/Resources;->getBoolean(I)Z'],
        'type': 'policy_skip',
        'search': """.method public isAvailable(Z)Z
    .registers 5

    invoke-super {p0, p1}, Lcom/android/provision/global/GlobalDefaultActivity$State;->isAvailable(Z)Z

    move-result p1

    const/4 v0, 0x0

    if-eqz p1, :cond_1

    sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz p1, :cond_0

    goto :goto_0

    :cond_0
    iget-object p1, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    invoke-virtual {p1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object p1

    sget v1, Lcom/android/provision/R$bool;->support_boot_video:I

    invoke-virtual {p1, v1}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result p1

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "isBootVideoExist="

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v1, p1}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    const-string v2, ",mForceSkiped="

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-boolean v2, p0, Lcom/android/provision/global/GlobalDefaultActivity$BootVideoState;->mForceSkiped:Z

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    const-string v2, "GlobalDefaultActivity"

    invoke-static {v2, v1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    if-eqz p1, :cond_1

    iget-boolean p0, p0, Lcom/android/provision/global/GlobalDefaultActivity$BootVideoState;->mForceSkiped:Z

    if-nez p0, :cond_1

    const/4 p0, 0x1

    return p0

    :cond_1
    :goto_0
    return v0
.end method""",
        'replacement': """.method public isAvailable(Z)Z
    .registers 5

    invoke-super {p0, p1}, Lcom/android/provision/global/GlobalDefaultActivity$State;->isAvailable(Z)Z

    move-result p1

    const/4 v0, 0x0

    if-eqz p1, :cond_1

    sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz p1, :cond_0

    goto :goto_0

    :cond_0
    iget-object p1, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    invoke-virtual {p1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object p1

    sget v1, Lcom/android/provision/R$bool;->support_boot_video:I

    invoke-virtual {p1, v1}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result p1

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "isBootVideoExist="

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v1, p1}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    const-string v2, ",mForceSkiped="

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-boolean v2, p0, Lcom/android/provision/global/GlobalDefaultActivity$BootVideoState;->mForceSkiped:Z

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    const-string v2, "GlobalDefaultActivity"

    invoke-static {v2, v1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    if-eqz p1, :cond_1

    iget-boolean p0, p0, Lcom/android/provision/global/GlobalDefaultActivity$BootVideoState;->mForceSkiped:Z

    if-nez p0, :cond_1

    const/4 p0, 0x1

    return p0

    :cond_1
    :goto_0
    return v0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
]
