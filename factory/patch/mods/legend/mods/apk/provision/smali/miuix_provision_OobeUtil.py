TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/provision/OobeUtil.smali'
CLASS_FALLBACK_NAMES = ['OobeUtil.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field public static final BUILD_DEVICE:Ljava/lang/String;', '.field public static final SUPPORT_FOLD:Z']

PATCHES = [
    {
        'id': 'miuix_provision_OobeUtil__needFastAnimation',
        'method': '.method public static needFastAnimation()Z',
        'method_name': 'needFastAnimation',
        'method_anchors': ['invoke-static {}, Lmiuix/provision/OobeUtil;->isGreaterOrEqualMIUI130()Z', 'if-eqz v0, :cond_0', 'sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-nez v0, :cond_0', 'invoke-static {}, Lmiuix/provision/OobeUtil;->isL2orL3()Z', 'return v0', 'return v0'],
        'type': 'method_replace',
        'search': """.method public static needFastAnimation()Z
    .registers 1

    invoke-static {}, Lmiuix/provision/OobeUtil;->isGreaterOrEqualMIUI130()Z

    move-result v0

    if-eqz v0, :cond_0

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_0

    invoke-static {}, Lmiuix/provision/OobeUtil;->isL2orL3()Z

    const/4 v0, 0x1

    return v0

    :cond_0
    const/4 v0, 0x0

    return v0
.end method""",
        'replacement': """.method public static needFastAnimation()Z
    .registers 1

    const/4 v0, 0x1

    return v0

    invoke-static {}, Lmiuix/provision/OobeUtil;->isGreaterOrEqualMIUI130()Z

    move-result v0

    if-eqz v0, :cond_0

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_0

    invoke-static {}, Lmiuix/provision/OobeUtil;->isL2orL3()Z

    const/4 v0, 0x1

    return v0

    :cond_0
    const/4 v0, 0x0

    return v0
.end method""",
        'required': True,
        'policy_status': 'BUILD_FLAG_PARTIALLY_SKIPPED',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_provision_OobeUtil__setTranslucentNavigationBar',
        'method': '.method public static setTranslucentNavigationBar(Landroid/view/Window;)V',
        'method_name': 'setTranslucentNavigationBar',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_0', 'invoke-virtual {p0, v0}, Landroid/view/Window;->addFlags(I)V', 'return-void'],
        'type': 'policy_skip',
        'search': """.method public static setTranslucentNavigationBar(Landroid/view/Window;)V
    .registers 2

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    const/high16 v0, 0x8000000

    invoke-virtual {p0, v0}, Landroid/view/Window;->addFlags(I)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method public static setTranslucentNavigationBar(Landroid/view/Window;)V
    .registers 2

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    const/high16 v0, 0x8000000

    invoke-virtual {p0, v0}, Landroid/view/Window;->addFlags(I)V

    :cond_0
    return-void
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
]
