TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/view/menu/ImmersionMenuAdapter.smali'
CLASS_FALLBACK_NAMES = ['ImmersionMenuAdapter.smali']
CLASS_ANCHORS = ['.super Landroid/widget/BaseAdapter;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_view_menu_ImmersionMenuAdapter__checkMenuItem',
        'method': '.method protected checkMenuItem(Landroid/view/MenuItem;)Z',
        'method_name': 'checkMenuItem',
        'method_anchors': ['invoke-interface {p1}, Landroid/view/MenuItem;->isVisible()Z', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected checkMenuItem(Landroid/view/MenuItem;)Z
    .registers 2

    invoke-interface {p1}, Landroid/view/MenuItem;->isVisible()Z

    move-result p0

    return p0
.end method""",
        'replacement': """.method protected checkMenuItem(Landroid/view/MenuItem;)Z
    .registers 2

    goto :goto_0

    nop

    :goto_0
    invoke-interface {p1}, Landroid/view/MenuItem;->isVisible()Z

    move-result p0

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
