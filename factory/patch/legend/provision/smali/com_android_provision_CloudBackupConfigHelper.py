TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/CloudBackupConfigHelper.smali'
CLASS_FALLBACK_NAMES = ['CloudBackupConfigHelper.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field private static final AUTHORITY:Ljava/lang/String; = "com.miui.micloud"', '.field private static final BASE_URI:Landroid/net/Uri;', '.field public static final KEY_CLOUD_RESTORE_CHOSEN:Ljava/lang/String; = "key_xiaomi_cloud_restore_chosen"', '.field public static final KEY_IS_BACKUP_EXIST:Ljava/lang/String; = "key_is_backup_exist"', '.field public static final NO:I = 0x0']

PATCHES = [
    {
        'id': 'com_android_provision_CloudBackupConfigHelper__isInternalBuild',
        'method': '.method public static isInternalBuild()Z',
        'method_name': 'isInternalBuild',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'return v0'],
        'type': 'policy_skip',
        'search': """.method public static isInternalBuild()Z
    .registers 1

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    return v0
.end method""",
        'replacement': """.method public static isInternalBuild()Z
    .registers 1

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    return v0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
]
