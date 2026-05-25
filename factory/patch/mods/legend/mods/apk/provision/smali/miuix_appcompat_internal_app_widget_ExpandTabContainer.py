TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/app/widget/ExpandTabContainer.smali'
CLASS_FALLBACK_NAMES = ['ExpandTabContainer.smali']
CLASS_ANCHORS = ['.super Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_app_widget_ExpandTabContainer__getDefaultTabTextStyle',
        'method': '.method getDefaultTabTextStyle()I',
        'method_name': 'getDefaultTabTextStyle',
        'method_anchors': ['sget p0, Lmiuix/appcompat/R$attr;->actionBarTabTextExpandStyle:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method getDefaultTabTextStyle()I
    .registers 1

    sget p0, Lmiuix/appcompat/R$attr;->actionBarTabTextExpandStyle:I

    return p0
.end method""",
        'replacement': """.method getDefaultTabTextStyle()I
    .registers 1

    goto :goto_0

    nop

    :goto_0
    sget p0, Lmiuix/appcompat/R$attr;->actionBarTabTextExpandStyle:I

    goto :goto_1

    nop

    :goto_1
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ExpandTabContainer__getTabBarLayoutRes',
        'method': '.method getTabBarLayoutRes()I',
        'method_name': 'getTabBarLayoutRes',
        'method_anchors': ['sget p0, Lmiuix/appcompat/R$layout;->miuix_appcompat_action_bar_tabbar_expand:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method getTabBarLayoutRes()I
    .registers 1

    sget p0, Lmiuix/appcompat/R$layout;->miuix_appcompat_action_bar_tabbar_expand:I

    return p0
.end method""",
        'replacement': """.method getTabBarLayoutRes()I
    .registers 1

    goto :goto_0

    nop

    :goto_0
    sget p0, Lmiuix/appcompat/R$layout;->miuix_appcompat_action_bar_tabbar_expand:I

    goto :goto_1

    nop

    :goto_1
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ExpandTabContainer__getTabContainerHeight',
        'method': '.method getTabContainerHeight()I',
        'method_name': 'getTabContainerHeight',
        'method_anchors': ['return p0'],
        'type': 'method_replace',
        'search': """.method getTabContainerHeight()I
    .registers 1

    const/4 p0, -0x2

    return p0
.end method""",
        'replacement': """.method getTabContainerHeight()I
    .registers 1

    goto :goto_0

    nop

    :goto_0
    const/4 p0, -0x2

    goto :goto_1

    nop

    :goto_1
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ExpandTabContainer__getTabViewMarginHorizontal',
        'method': '.method getTabViewMarginHorizontal()I',
        'method_name': 'getTabViewMarginHorizontal',
        'method_anchors': ['invoke-virtual {p0}, Landroid/widget/HorizontalScrollView;->getContext()Landroid/content/Context;', 'invoke-virtual {p0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;', 'sget v0, Lmiuix/appcompat/R$dimen;->miuix_appcompat_action_bar_tab_expand_margin:I', 'invoke-virtual {p0, v0}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I', 'return p0'],
        'type': 'method_replace',
        'search': """.method getTabViewMarginHorizontal()I
    .registers 2

    invoke-virtual {p0}, Landroid/widget/HorizontalScrollView;->getContext()Landroid/content/Context;

    move-result-object p0

    invoke-virtual {p0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object p0

    sget v0, Lmiuix/appcompat/R$dimen;->miuix_appcompat_action_bar_tab_expand_margin:I

    invoke-virtual {p0, v0}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result p0

    return p0
.end method""",
        'replacement': """.method getTabViewMarginHorizontal()I
    .registers 2

    goto :goto_4

    nop

    :goto_0
    return p0

    :goto_1
    sget v0, Lmiuix/appcompat/R$dimen;->miuix_appcompat_action_bar_tab_expand_margin:I

    goto :goto_2

    nop

    :goto_2
    invoke-virtual {p0, v0}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result p0

    goto :goto_0

    nop

    :goto_3
    invoke-virtual {p0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object p0

    goto :goto_1

    nop

    :goto_4
    invoke-virtual {p0}, Landroid/widget/HorizontalScrollView;->getContext()Landroid/content/Context;

    move-result-object p0

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
