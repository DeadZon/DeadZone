TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/app/floatingactivity/helper/TabletFloatingActivityHelper.smali'
CLASS_FALLBACK_NAMES = ['TabletFloatingActivityHelper.smali']
CLASS_ANCHORS = ['.super Lmiuix/appcompat/app/floatingactivity/helper/BaseFloatingActivityHelper;']

PATCHES = [
    {
        'id': 'miuix_appcompat_app_floatingactivity_helper_TabletFloatingActivityHelper__isFloatingWindow',
        'method': '.method protected isFloatingWindow()Z',
        'method_name': 'isFloatingWindow',
        'method_anchors': ['iget-boolean p0, p0, Lmiuix/appcompat/app/floatingactivity/helper/TabletFloatingActivityHelper;->mIsFloatingWindow:Z', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected isFloatingWindow()Z
    .registers 1

    iget-boolean p0, p0, Lmiuix/appcompat/app/floatingactivity/helper/TabletFloatingActivityHelper;->mIsFloatingWindow:Z

    return p0
.end method""",
        'replacement': """.method protected isFloatingWindow()Z
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    iget-boolean p0, p0, Lmiuix/appcompat/app/floatingactivity/helper/TabletFloatingActivityHelper;->mIsFloatingWindow:Z

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
