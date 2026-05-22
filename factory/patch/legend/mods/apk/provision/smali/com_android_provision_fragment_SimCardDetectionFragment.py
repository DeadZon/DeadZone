TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/fragment/SimCardDetectionFragment.smali'
CLASS_FALLBACK_NAMES = ['SimCardDetectionFragment.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/fragment/BaseFragment;', '.field private static final CLOSE_DIALOG:I = 0x1', '.field private static final DELAY_SWITCH_SIM:I = 0x2', '.field private static final DETECTING_TIME:I = 0xbb8', '.field private static final DETECTING_TIME_SHORT:I = 0x3e8', '.field public static final EXTRA_MUTISIMSETTINGS_FORCE_SKIPED:Ljava/lang/String; = "extra_mutisimsettings_force_skiped"']

PATCHES = [
    {
        'id': 'com_android_provision_fragment_SimCardDetectionFragment__getName',
        'method': '.method protected getName()Ljava/lang/String;',
        'method_name': 'getName',
        'method_anchors': ['const-string p0, "SimCardDetectionFragment"', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getName()Ljava/lang/String;
    .registers 1

    const-string p0, "SimCardDetectionFragment"

    return-object p0
.end method""",
        'replacement': """.method protected getName()Ljava/lang/String;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    const-string p0, "SimCardDetectionFragment"

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
