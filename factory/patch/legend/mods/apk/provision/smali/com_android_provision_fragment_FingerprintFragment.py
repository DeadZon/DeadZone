TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/fragment/FingerprintFragment.smali'
CLASS_FALLBACK_NAMES = ['FingerprintFragment.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/fragment/BaseFragment;', '.field private static final REQ_FINGERPRINT:I = 0x1']

PATCHES = [
    {
        'id': 'com_android_provision_fragment_FingerprintFragment__getName',
        'method': '.method protected getName()Ljava/lang/String;',
        'method_name': 'getName',
        'method_anchors': ['const-string p0, "FingerprintFragment"', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getName()Ljava/lang/String;
    .registers 1

    const-string p0, "FingerprintFragment"

    return-object p0
.end method""",
        'replacement': """.method protected getName()Ljava/lang/String;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    const-string p0, "FingerprintFragment"

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_fragment_FingerprintFragment__goSkip',
        'method': '.method public goSkip()V',
        'method_name': 'goSkip',
        'method_anchors': ['invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->isShowSetPasswordConfirmDialog()Z', 'if-eqz v0, :cond_0', 'invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;', 'invoke-direct {p0, v0}, Lcom/android/provision/fragment/FingerprintFragment;->showOrangeSetPasswordDialog(Landroid/content/Context;)V', 'return-void', 'invoke-virtual {p0}, Lcom/android/provision/fragment/BaseFragment;->recordPageStayTime()V', 'const-string v0, "next"', 'invoke-virtual {p0, v0}, Lcom/android/provision/fragment/BaseFragment;->recordBottomButtonClick(Ljava/lang/String;)V'],
        'type': 'policy_skip',
        'search': """.method public goSkip()V
    .registers 3

    invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->isShowSetPasswordConfirmDialog()Z

    move-result v0

    if-eqz v0, :cond_0

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-direct {p0, v0}, Lcom/android/provision/fragment/FingerprintFragment;->showOrangeSetPasswordDialog(Landroid/content/Context;)V

    return-void

    :cond_0
    invoke-virtual {p0}, Lcom/android/provision/fragment/BaseFragment;->recordPageStayTime()V

    const-string v0, "next"

    invoke-virtual {p0, v0}, Lcom/android/provision/fragment/BaseFragment;->recordBottomButtonClick(Ljava/lang/String;)V

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_1

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p0

    invoke-virtual {p0}, Landroid/app/Activity;->getIntent()Landroid/content/Intent;

    move-result-object p0

    const/4 v1, -0x1

    invoke-static {v0, p0, v1}, Lcom/android/provision/Utils;->goToNextPage(Landroid/app/Activity;Landroid/content/Intent;I)V

    return-void

    :cond_1
    const/4 v0, 0x1

    invoke-direct {p0, v0}, Lcom/android/provision/fragment/FingerprintFragment;->stepDone(Z)V

    return-void
.end method""",
        'replacement': """.method public goSkip()V
    .registers 3

    invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->isShowSetPasswordConfirmDialog()Z

    move-result v0

    if-eqz v0, :cond_0

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-direct {p0, v0}, Lcom/android/provision/fragment/FingerprintFragment;->showOrangeSetPasswordDialog(Landroid/content/Context;)V

    return-void

    :cond_0
    invoke-virtual {p0}, Lcom/android/provision/fragment/BaseFragment;->recordPageStayTime()V

    const-string v0, "next"

    invoke-virtual {p0, v0}, Lcom/android/provision/fragment/BaseFragment;->recordBottomButtonClick(Ljava/lang/String;)V

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_1

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p0

    invoke-virtual {p0}, Landroid/app/Activity;->getIntent()Landroid/content/Intent;

    move-result-object p0

    const/4 v1, -0x1

    invoke-static {v0, p0, v1}, Lcom/android/provision/Utils;->goToNextPage(Landroid/app/Activity;Landroid/content/Intent;I)V

    return-void

    :cond_1
    const/4 v0, 0x1

    invoke-direct {p0, v0}, Lcom/android/provision/fragment/FingerprintFragment;->stepDone(Z)V

    return-void
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_fragment_FingerprintFragment__onActivityResult',
        'method': '.method public onActivityResult(IILandroid/content/Intent;)V',
        'method_name': 'onActivityResult',
        'method_anchors': ['if-ne p1, p3, :cond_1', 'if-ne p2, p1, :cond_1', 'invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;', 'invoke-virtual {p2}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;', 'const-string v0, "miui_keyguard"', 'invoke-static {p2, v0, v1}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z', 'sget-boolean p2, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz p2, :cond_0'],
        'type': 'policy_skip',
        'search': """.method public onActivityResult(IILandroid/content/Intent;)V
    .registers 6

    const/4 p3, 0x1

    if-ne p1, p3, :cond_1

    const/4 p1, -0x1

    if-ne p2, p1, :cond_1

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p2

    invoke-virtual {p2}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p2

    const-string v0, "miui_keyguard"

    const/4 v1, 0x2

    invoke-static {p2, v0, v1}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    sget-boolean p2, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz p2, :cond_0

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p2

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p3

    invoke-virtual {p3}, Landroid/app/Activity;->getIntent()Landroid/content/Intent;

    move-result-object p3

    invoke-static {p2, p3, p1}, Lcom/android/provision/Utils;->goToNextPage(Landroid/app/Activity;Landroid/content/Intent;I)V

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p0

    invoke-virtual {p0}, Landroid/app/Activity;->finish()V

    return-void

    :cond_0
    invoke-direct {p0, p3}, Lcom/android/provision/fragment/FingerprintFragment;->stepDone(Z)V

    :cond_1
    return-void
.end method""",
        'replacement': """.method public onActivityResult(IILandroid/content/Intent;)V
    .registers 6

    const/4 p3, 0x1

    if-ne p1, p3, :cond_1

    const/4 p1, -0x1

    if-ne p2, p1, :cond_1

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p2

    invoke-virtual {p2}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p2

    const-string v0, "miui_keyguard"

    const/4 v1, 0x2

    invoke-static {p2, v0, v1}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    sget-boolean p2, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz p2, :cond_0

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p2

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p3

    invoke-virtual {p3}, Landroid/app/Activity;->getIntent()Landroid/content/Intent;

    move-result-object p3

    invoke-static {p2, p3, p1}, Lcom/android/provision/Utils;->goToNextPage(Landroid/app/Activity;Landroid/content/Intent;I)V

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p0

    invoke-virtual {p0}, Landroid/app/Activity;->finish()V

    return-void

    :cond_0
    invoke-direct {p0, p3}, Lcom/android/provision/fragment/FingerprintFragment;->stepDone(Z)V

    :cond_1
    return-void
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
]
