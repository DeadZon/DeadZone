TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/app/floatingactivity/FloatingLifecycleObserver.smali'
CLASS_FALLBACK_NAMES = ['FloatingLifecycleObserver.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Landroidx/lifecycle/LifecycleObserver;']

PATCHES = [
    {
        'id': 'miuix_appcompat_app_floatingactivity_FloatingLifecycleObserver__getActivityIdentity',
        'method': '.method protected getActivityIdentity()Ljava/lang/String;',
        'method_name': 'getActivityIdentity',
        'method_anchors': ['iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/FloatingLifecycleObserver;->mActivityIdentity:Ljava/lang/String;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getActivityIdentity()Ljava/lang/String;
    .registers 1

    iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/FloatingLifecycleObserver;->mActivityIdentity:Ljava/lang/String;

    return-object p0
.end method""",
        'replacement': """.method protected getActivityIdentity()Ljava/lang/String;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/FloatingLifecycleObserver;->mActivityIdentity:Ljava/lang/String;

    goto :goto_1

    nop

    :goto_1
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_floatingactivity_FloatingLifecycleObserver__getActivityTaskId',
        'method': '.method protected getActivityTaskId()I',
        'method_name': 'getActivityTaskId',
        'method_anchors': ['iget p0, p0, Lmiuix/appcompat/app/floatingactivity/FloatingLifecycleObserver;->mActivityTaskId:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected getActivityTaskId()I
    .registers 1

    iget p0, p0, Lmiuix/appcompat/app/floatingactivity/FloatingLifecycleObserver;->mActivityTaskId:I

    return p0
.end method""",
        'replacement': """.method protected getActivityTaskId()I
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    iget p0, p0, Lmiuix/appcompat/app/floatingactivity/FloatingLifecycleObserver;->mActivityTaskId:I

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
