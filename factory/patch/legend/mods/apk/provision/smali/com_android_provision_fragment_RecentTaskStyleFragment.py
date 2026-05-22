TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/fragment/RecentTaskStyleFragment.smali'
CLASS_FALLBACK_NAMES = ['RecentTaskStyleFragment.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/fragment/BaseFragment;', '.field public static final MODE_HORIZONTAL:I = 0x1', '.field public static final MODE_STACKED:I = 0x2', '.field public static final MODE_VIRTUAL:I = 0x0', '.field private static final TAG:Ljava/lang/String; = "RecentTaskStyleFragment"']

PATCHES = [
    {
        'id': 'com_android_provision_fragment_RecentTaskStyleFragment__getName',
        'method': '.method protected getName()Ljava/lang/String;',
        'method_name': 'getName',
        'method_anchors': ['const-string p0, "RecentTaskStyleFragment"', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getName()Ljava/lang/String;
    .registers 1

    const-string p0, "RecentTaskStyleFragment"

    return-object p0
.end method""",
        'replacement': """.method protected getName()Ljava/lang/String;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    const-string p0, "RecentTaskStyleFragment"

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
