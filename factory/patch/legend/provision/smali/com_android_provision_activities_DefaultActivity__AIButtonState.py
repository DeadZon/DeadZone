TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/activities/DefaultActivity$AIButtonState.smali'
CLASS_FALLBACK_NAMES = ['DefaultActivity$AIButtonState.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/activities/DefaultActivity$State;', '.field private static final PERSEUS:Ljava/lang/String; = "perseus"']

PATCHES = [
    {
        'id': 'com_android_provision_activities_DefaultActivity__AIButtonState__isAvailable',
        'method': '.method public isAvailable(Z)Z',
        'method_name': 'isAvailable',
        'method_anchors': ['sget-boolean p0, Lmiui/os/Build;->IS_GLOBAL_BUILD:Z', 'if-nez p0, :cond_0', 'const-string p0, "support_ai_task"', 'invoke-static {p0, p1}, Lmiui/util/FeatureParser;->getBoolean(Ljava/lang/String;Z)Z', 'if-eqz p0, :cond_0', 'return p0', 'return p1'],
        'type': 'policy_skip',
        'search': """.method public isAvailable(Z)Z
    .registers 2

    sget-boolean p0, Lmiui/os/Build;->IS_GLOBAL_BUILD:Z

    const/4 p1, 0x0

    if-nez p0, :cond_0

    const-string p0, "support_ai_task"

    invoke-static {p0, p1}, Lmiui/util/FeatureParser;->getBoolean(Ljava/lang/String;Z)Z

    move-result p0

    if-eqz p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    return p1
.end method""",
        'replacement': """.method public isAvailable(Z)Z
    .registers 2

    sget-boolean p0, Lmiui/os/Build;->IS_GLOBAL_BUILD:Z

    const/4 p1, 0x0

    if-nez p0, :cond_0

    const-string p0, "support_ai_task"

    invoke-static {p0, p1}, Lmiui/util/FeatureParser;->getBoolean(Ljava/lang/String;Z)Z

    move-result p0

    if-eqz p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    return p1
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
]
