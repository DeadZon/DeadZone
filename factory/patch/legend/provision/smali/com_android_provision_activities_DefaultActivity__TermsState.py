TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/activities/DefaultActivity$TermsState.smali'
CLASS_FALLBACK_NAMES = ['DefaultActivity$TermsState.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/activities/DefaultActivity$State;']

PATCHES = [
    {
        'id': 'com_android_provision_activities_DefaultActivity__TermsState__isAvailable',
        'method': '.method public isAvailable(Z)Z',
        'method_name': 'isAvailable',
        'method_anchors': ['sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'return p0'],
        'type': 'policy_skip',
        'search': """.method public isAvailable(Z)Z
    .registers 2

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    return p0
.end method""",
        'replacement': """.method public isAvailable(Z)Z
    .registers 2

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    return p0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
]
