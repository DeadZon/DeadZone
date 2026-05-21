TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ServiceNotify.smali'
CLASS_FALLBACK_NAMES = ['MultiAppFloatingActivitySwitcher$ServiceNotify.smali']
CLASS_ANCHORS = ['.super Lmiuix/appcompat/app/floatingactivity/multiapp/IServiceNotify$Stub;']

PATCHES = [
    {
        'id': 'miuix_appcompat_app_floatingactivity_multiapp_MultiAppFloatingActivitySwitcher__ServiceNotify__getActivityIdentity',
        'method': '.method protected getActivityIdentity()Ljava/lang/String;',
        'method_name': 'getActivityIdentity',
        'method_anchors': ['iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ServiceNotify;->mActivityIdentity:Ljava/lang/String;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getActivityIdentity()Ljava/lang/String;
    .registers 1

    iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ServiceNotify;->mActivityIdentity:Ljava/lang/String;

    return-object p0
.end method""",
        'replacement': """.method protected getActivityIdentity()Ljava/lang/String;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ServiceNotify;->mActivityIdentity:Ljava/lang/String;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_floatingactivity_multiapp_MultiAppFloatingActivitySwitcher__ServiceNotify__getActivityTaskId',
        'method': '.method protected getActivityTaskId()I',
        'method_name': 'getActivityTaskId',
        'method_anchors': ['iget p0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ServiceNotify;->mActivityTaskId:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected getActivityTaskId()I
    .registers 1

    iget p0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ServiceNotify;->mActivityTaskId:I

    return p0
.end method""",
        'replacement': """.method protected getActivityTaskId()I
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget p0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ServiceNotify;->mActivityTaskId:I

    goto :goto_1

    nop

    :goto_1
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
