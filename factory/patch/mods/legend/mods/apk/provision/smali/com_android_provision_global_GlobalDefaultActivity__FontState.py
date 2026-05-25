TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/global/GlobalDefaultActivity$FontState.smali'
CLASS_FALLBACK_NAMES = ['GlobalDefaultActivity$FontState.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/global/GlobalDefaultActivity$State;']

PATCHES = [
    {
        'id': 'com_android_provision_global_GlobalDefaultActivity__FontState__isAvailable',
        'method': '.method public isAvailable(Z)Z',
        'method_name': 'isAvailable',
        'method_anchors': ['const-string p1, "GlobalDefaultActivity"', 'const-string v0, " here is FontState isAvailable func "', 'invoke-static {p1, v0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I', 'iget-object p1, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;', 'invoke-static {p1}, Lcom/android/provision/Utils;->isAlreadyEnterFontStyleFromGms(Landroid/content/Context;)Z', 'if-nez p1, :cond_0', 'invoke-static {}, Lcom/android/provision/Utils;->isMiSansSupportLanguages()Z', 'if-eqz p1, :cond_0'],
        'type': 'method_replace',
        'search': """.method public isAvailable(Z)Z
    .registers 3

    const-string p1, "GlobalDefaultActivity"

    const-string v0, " here is FontState isAvailable func "

    invoke-static {p1, v0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    iget-object p1, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {p1}, Lcom/android/provision/Utils;->isAlreadyEnterFontStyleFromGms(Landroid/content/Context;)Z

    move-result p1

    if-nez p1, :cond_0

    invoke-static {}, Lcom/android/provision/Utils;->isMiSansSupportLanguages()Z

    move-result p1

    if-eqz p1, :cond_0

    iget-object p1, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {p1}, Lcom/android/provision/fragment/FontStyleFragment;->getFontList(Landroid/content/Context;)Ljava/util/List;

    move-result-object p1

    invoke-interface {p1}, Ljava/util/List;->size()I

    move-result p1

    const/4 v0, 0x2

    if-ne p1, v0, :cond_0

    invoke-static {}, Lcom/android/provision/Utils;->isFoldDevice()Z

    move-result p1

    if-nez p1, :cond_0

    iget-object p0, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {p0}, Lcom/android/provision/Utils;->isInProvisionState(Landroid/content/Context;)Z

    move-result p0

    if-nez p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method public isAvailable(Z)Z
    .registers 3

    const/4 v0, 0x0

    return v0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
