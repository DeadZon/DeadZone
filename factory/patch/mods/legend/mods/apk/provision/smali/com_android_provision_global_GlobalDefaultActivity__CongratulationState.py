TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/global/GlobalDefaultActivity$CongratulationState.smali'
CLASS_FALLBACK_NAMES = ['GlobalDefaultActivity$CongratulationState.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/global/GlobalDefaultActivity$State;']

PATCHES = [
    {
        'id': 'com_android_provision_global_GlobalDefaultActivity__CongratulationState__onLeave',
        'method': '.method public onLeave()V',
        'method_name': 'onLeave',
        'method_anchors': ['invoke-super {p0}, Lcom/android/provision/global/GlobalDefaultActivity$State;->onLeave()V', 'iget-object v0, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;', 'invoke-static {v0}, Lcom/android/provision/Utils;->isAlreadyEnterFontStyleFromGms(Landroid/content/Context;)Z', 'if-nez v0, :cond_1', 'sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_0', 'iget-object v0, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;', 'invoke-static {v0}, Lcom/android/provision/utils/FontStyleUtils;->getLocalFontId(Landroid/content/Context;)Ljava/lang/String;'],
        'type': 'method_replace',
        'search': """.method public onLeave()V
    .registers 3

    invoke-super {p0}, Lcom/android/provision/global/GlobalDefaultActivity$State;->onLeave()V

    iget-object v0, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {v0}, Lcom/android/provision/Utils;->isAlreadyEnterFontStyleFromGms(Landroid/content/Context;)Z

    move-result v0

    if-nez v0, :cond_1

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    iget-object v0, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {v0}, Lcom/android/provision/utils/FontStyleUtils;->getLocalFontId(Landroid/content/Context;)Ljava/lang/String;

    move-result-object v0

    const-string v1, "10"

    invoke-virtual {v1, v0}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result v0

    if-eqz v0, :cond_0

    iget-object v0, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {v0, v1}, Lcom/android/provision/utils/FontStyleUtils;->applyFont(Landroid/content/Context;Ljava/lang/String;)V

    goto :goto_0

    :cond_0
    iget-object v0, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    sget-object v1, Lcom/android/provision/utils/FontStyleUtils;->MISANS_FONT_ID:Ljava/lang/String;

    invoke-static {v0, v1}, Lcom/android/provision/utils/FontStyleUtils;->applyFont(Landroid/content/Context;Ljava/lang/String;)V

    :cond_1
    :goto_0
    invoke-static {}, Lcom/android/provision/Utils;->isTabletDevice()Z

    move-result v0

    if-eqz v0, :cond_2

    iget-object v0, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    const/4 v1, 0x1

    invoke-static {v0, v1}, Lcom/android/provision/Utils;->setNavigationBarFullScreen(Landroid/content/Context;Z)V

    goto :goto_1

    :cond_2
    iget-object v0, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->isPrefFullscreen()Z

    move-result v1

    invoke-static {v0, v1}, Lcom/android/provision/Utils;->setNavigationBarFullScreen(Landroid/content/Context;Z)V

    :goto_1
    iget-object v0, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    if-eqz v0, :cond_3

    invoke-static {v0}, Lcom/android/provision/Utils;->isGestureLineShow(Landroid/content/Context;)Z

    move-result v0

    if-nez v0, :cond_3

    iget-object p0, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    const/4 v0, 0x0

    invoke-static {p0, v0}, Lcom/android/provision/Utils;->hideGestureLine(Landroid/content/Context;Z)V

    :cond_3
    return-void
.end method""",
        'replacement': """.method public onLeave()V
    .registers 3

    invoke-super {p0}, Lcom/android/provision/global/GlobalDefaultActivity$State;->onLeave()V

    iget-object v0, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {v0}, Lcom/android/provision/Utils;->isAlreadyEnterFontStyleFromGms(Landroid/content/Context;)Z

    move-result v0

    if-nez v0, :cond_1

    sget-boolean v0, Lmiui/os/Build;->IS_ALPHA_BUILD:Z

    if-eqz v0, :cond_0

    iget-object v0, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {v0}, Lcom/android/provision/utils/FontStyleUtils;->getLocalFontId(Landroid/content/Context;)Ljava/lang/String;

    move-result-object v0

    const-string v1, "10"

    invoke-virtual {v1, v0}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result v0

    if-eqz v0, :cond_0

    iget-object v0, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {v0, v1}, Lcom/android/provision/utils/FontStyleUtils;->applyFont(Landroid/content/Context;Ljava/lang/String;)V

    goto :goto_0

    :cond_0
    iget-object v0, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    sget-object v1, Lcom/android/provision/utils/FontStyleUtils;->MISANS_FONT_ID:Ljava/lang/String;

    invoke-static {v0, v1}, Lcom/android/provision/utils/FontStyleUtils;->applyFont(Landroid/content/Context;Ljava/lang/String;)V

    :cond_1
    :goto_0
    invoke-static {}, Lcom/android/provision/Utils;->isTabletDevice()Z

    move-result v0

    if-eqz v0, :cond_2

    iget-object v0, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    const/4 v1, 0x1

    invoke-static {v0, v1}, Lcom/android/provision/Utils;->setNavigationBarFullScreen(Landroid/content/Context;Z)V

    goto :goto_1

    :cond_2
    iget-object v0, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->isPrefFullscreen()Z

    move-result v1

    invoke-static {v0, v1}, Lcom/android/provision/Utils;->setNavigationBarFullScreen(Landroid/content/Context;Z)V

    :goto_1
    iget-object v0, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    if-eqz v0, :cond_3

    invoke-static {v0}, Lcom/android/provision/Utils;->isGestureLineShow(Landroid/content/Context;)Z

    move-result v0

    if-nez v0, :cond_3

    iget-object p0, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    const/4 v0, 0x0

    invoke-static {p0, v0}, Lcom/android/provision/Utils;->hideGestureLine(Landroid/content/Context;Z)V

    :cond_3
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
