TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/fragment/StartupFragment.smali'
CLASS_FALLBACK_NAMES = ['StartupFragment.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/fragment/BaseFragment;', '.implements Lcom/android/provision/IOnFocusListener;', '.field private static final BOOT_AUDIO:Ljava/lang/String; = "boot_audio"', '.field private static final CLICK_TIME_DURATION:I = 0x7d0', '.field private static final LTR_LAYOUT:I = 0x2', '.field private static final QR_APPLICATION_ACTION:Ljava/lang/String; = "com.miui.qr.QR_LAUNCHE_ACTION"']

PATCHES = [
    {
        'id': 'com_android_provision_fragment_StartupFragment__isNeedInitNfc',
        'method': '.method private isNeedInitNfc()Z',
        'method_name': 'isNeedInitNfc',
        'method_anchors': ['new-instance p0, Ljava/lang/StringBuilder;', 'invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V', 'const-string v0, "isNeedInitNfc:"', 'invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;', 'invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;', 'const-string v1, "StartupFragment"'],
        'type': 'policy_skip',
        'search': """.method private isNeedInitNfc()Z
    .registers 3

    new-instance p0, Ljava/lang/StringBuilder;

    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v0, "isNeedInitNfc:"

    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    const-string v1, "StartupFragment"

    invoke-static {v1, p0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    return v0
.end method""",
        'replacement': """.method private isNeedInitNfc()Z
    .registers 3

    new-instance p0, Ljava/lang/StringBuilder;

    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v0, "isNeedInitNfc:"

    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    const-string v1, "StartupFragment"

    invoke-static {v1, p0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    return v0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
]
