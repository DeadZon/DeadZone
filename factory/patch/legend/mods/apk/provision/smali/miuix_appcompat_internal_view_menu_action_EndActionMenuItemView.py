TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/view/menu/action/EndActionMenuItemView.smali'
CLASS_FALLBACK_NAMES = ['EndActionMenuItemView.smali']
CLASS_ANCHORS = ['.super Landroid/widget/LinearLayout;', '.implements Lmiuix/appcompat/internal/view/menu/MenuView$ItemView;', '.implements Lmiuix/animation/ViewHoverListener;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_view_menu_action_EndActionMenuItemView__onConfigurationChanged',
        'method': '.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V',
        'method_name': 'onConfigurationChanged',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/widget/LinearLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 2

    invoke-super {p0, p1}, Landroid/widget/LinearLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    return-void
.end method""",
        'replacement': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0, p1}, Landroid/widget/LinearLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    goto :goto_1

    nop

    :goto_1
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
