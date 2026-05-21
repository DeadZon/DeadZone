TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/fragment/CongratulationFragment.smali'
CLASS_FALLBACK_NAMES = ['CongratulationFragment.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/fragment/BaseFragment;', '.implements Lcom/android/provision/IOnFocusListener;', '.field private static final TAG:Ljava/lang/String; = "Provision_CongratulationFragment"', '.field private static final URI_LAUNCHER_SETTINGS:Ljava/lang/String;']

PATCHES = [
    {
        'id': 'com_android_provision_fragment_CongratulationFragment__handleInternationalBuild',
        'method': '.method private handleInternationalBuild()V',
        'method_name': 'handleInternationalBuild',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_1', 'iget-boolean v0, p0, Lcom/android/provision/fragment/CongratulationFragment;->isFinishStep:Z', 'if-nez v0, :cond_0', 'invoke-direct {p0}, Lcom/android/provision/fragment/CongratulationFragment;->installPreInstallApp()V', 'invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;', 'invoke-static {p0}, Lcom/android/provision/utils/RequestUtils;->startDTCarrierChannelRequest(Landroid/content/Context;)V', 'invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;'],
        'type': 'method_replace',
        'search': """.method private handleInternationalBuild()V
    .registers 2

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_1

    iget-boolean v0, p0, Lcom/android/provision/fragment/CongratulationFragment;->isFinishStep:Z

    if-nez v0, :cond_0

    invoke-direct {p0}, Lcom/android/provision/fragment/CongratulationFragment;->installPreInstallApp()V

    :cond_0
    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object p0

    invoke-static {p0}, Lcom/android/provision/utils/RequestUtils;->startDTCarrierChannelRequest(Landroid/content/Context;)V

    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object p0

    invoke-static {p0}, Lcom/android/provision/utils/CalendarAutoSwitchManager;->checkIsCotaCarrierCalendar(Landroid/content/Context;)V

    :cond_1
    return-void
.end method""",
        'replacement': """.method private handleInternationalBuild()V
    .registers 2

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_1

    iget-boolean v0, p0, Lcom/android/provision/fragment/CongratulationFragment;->isFinishStep:Z

    if-nez v0, :cond_0

    invoke-direct {p0}, Lcom/android/provision/fragment/CongratulationFragment;->installPreInstallApp()V

    :cond_0
    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object p0

    invoke-static {p0}, Lcom/android/provision/utils/CalendarAutoSwitchManager;->checkIsCotaCarrierCalendar(Landroid/content/Context;)V

    :cond_1
    return-void
.end method""",
        'required': True,
        'policy_status': 'BUILD_FLAG_PARTIALLY_SKIPPED',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
