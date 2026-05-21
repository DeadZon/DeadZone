TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/app/widget/CollapseTabContainer.smali'
CLASS_FALLBACK_NAMES = ['CollapseTabContainer.smali']
CLASS_ANCHORS = ['.super Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_app_widget_CollapseTabContainer__getDefaultTabTextStyle',
        'method': '.method getDefaultTabTextStyle()I',
        'method_name': 'getDefaultTabTextStyle',
        'method_anchors': ['return p0'],
        'type': 'method_replace',
        'search': """.method getDefaultTabTextStyle()I
    .registers 1

    const p0, 0x10102f5

    return p0
.end method""",
        'replacement': """.method getDefaultTabTextStyle()I
    .registers 1

    goto :goto_0

    nop

    :goto_0
    const p0, 0x10102f5

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
        'id': 'miuix_appcompat_internal_app_widget_CollapseTabContainer__getTabBarLayoutRes',
        'method': '.method getTabBarLayoutRes()I',
        'method_name': 'getTabBarLayoutRes',
        'method_anchors': ['sget p0, Lmiuix/appcompat/R$layout;->miuix_appcompat_action_bar_tabbar:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method getTabBarLayoutRes()I
    .registers 1

    sget p0, Lmiuix/appcompat/R$layout;->miuix_appcompat_action_bar_tabbar:I

    return p0
.end method""",
        'replacement': """.method getTabBarLayoutRes()I
    .registers 1

    goto :goto_0

    nop

    :goto_0
    sget p0, Lmiuix/appcompat/R$layout;->miuix_appcompat_action_bar_tabbar:I

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
        'id': 'miuix_appcompat_internal_app_widget_CollapseTabContainer__getTabContainerHeight',
        'method': '.method getTabContainerHeight()I',
        'method_name': 'getTabContainerHeight',
        'method_anchors': ['invoke-virtual {p0}, Landroid/widget/HorizontalScrollView;->getContext()Landroid/content/Context;', 'invoke-static {p0}, Lmiuix/appcompat/internal/view/ActionBarPolicy;->get(Landroid/content/Context;)Lmiuix/appcompat/internal/view/ActionBarPolicy;', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/view/ActionBarPolicy;->getTabContainerHeight()I', 'return p0'],
        'type': 'method_replace',
        'search': """.method getTabContainerHeight()I
    .registers 1

    invoke-virtual {p0}, Landroid/widget/HorizontalScrollView;->getContext()Landroid/content/Context;

    move-result-object p0

    invoke-static {p0}, Lmiuix/appcompat/internal/view/ActionBarPolicy;->get(Landroid/content/Context;)Lmiuix/appcompat/internal/view/ActionBarPolicy;

    move-result-object p0

    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/ActionBarPolicy;->getTabContainerHeight()I

    move-result p0

    return p0
.end method""",
        'replacement': """.method getTabContainerHeight()I
    .registers 1

    goto :goto_0

    nop

    :goto_0
    invoke-virtual {p0}, Landroid/widget/HorizontalScrollView;->getContext()Landroid/content/Context;

    move-result-object p0

    goto :goto_1

    nop

    :goto_1
    invoke-static {p0}, Lmiuix/appcompat/internal/view/ActionBarPolicy;->get(Landroid/content/Context;)Lmiuix/appcompat/internal/view/ActionBarPolicy;

    move-result-object p0

    goto :goto_3

    nop

    :goto_2
    return p0

    :goto_3
    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/ActionBarPolicy;->getTabContainerHeight()I

    move-result p0

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_CollapseTabContainer__onLayout',
        'method': '.method protected onLayout(ZIIII)V',
        'method_name': 'onLayout',
        'method_anchors': ['invoke-super/range {p0 .. p5}, Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView;->onLayout(ZIIII)V', 'invoke-virtual {p0}, Landroid/widget/HorizontalScrollView;->getMeasuredHeight()I', 'iget-object p3, p0, Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView;->mTabLayout:Landroid/widget/LinearLayout;', 'invoke-virtual {p3}, Landroid/widget/LinearLayout;->getMeasuredHeight()I', 'iget-object p4, p0, Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView;->mTabLayout:Landroid/widget/LinearLayout;', 'invoke-virtual {p4}, Landroid/widget/LinearLayout;->getMeasuredWidth()I', 'iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView;->mTabLayout:Landroid/widget/LinearLayout;', 'invoke-virtual {p0, p2, p1, p4, p3}, Landroid/widget/LinearLayout;->layout(IIII)V'],
        'type': 'method_replace',
        'search': """.method protected onLayout(ZIIII)V
    .registers 6

    invoke-super/range {p0 .. p5}, Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView;->onLayout(ZIIII)V

    invoke-virtual {p0}, Landroid/widget/HorizontalScrollView;->getMeasuredHeight()I

    move-result p1

    iget-object p3, p0, Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView;->mTabLayout:Landroid/widget/LinearLayout;

    invoke-virtual {p3}, Landroid/widget/LinearLayout;->getMeasuredHeight()I

    move-result p3

    iget-object p4, p0, Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView;->mTabLayout:Landroid/widget/LinearLayout;

    invoke-virtual {p4}, Landroid/widget/LinearLayout;->getMeasuredWidth()I

    move-result p4

    sub-int/2addr p1, p3

    div-int/lit8 p1, p1, 0x2

    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView;->mTabLayout:Landroid/widget/LinearLayout;

    add-int/2addr p3, p1

    invoke-virtual {p0, p2, p1, p4, p3}, Landroid/widget/LinearLayout;->layout(IIII)V

    return-void
.end method""",
        'replacement': """.method protected onLayout(ZIIII)V
    .registers 6

    goto :goto_1

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView;->mTabLayout:Landroid/widget/LinearLayout;

    goto :goto_b

    nop

    :goto_1
    invoke-super/range {p0 .. p5}, Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView;->onLayout(ZIIII)V

    goto :goto_7

    nop

    :goto_2
    invoke-virtual {p0, p2, p1, p4, p3}, Landroid/widget/LinearLayout;->layout(IIII)V

    goto :goto_5

    nop

    :goto_3
    iget-object p3, p0, Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView;->mTabLayout:Landroid/widget/LinearLayout;

    goto :goto_9

    nop

    :goto_4
    iget-object p4, p0, Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView;->mTabLayout:Landroid/widget/LinearLayout;

    goto :goto_6

    nop

    :goto_5
    return-void

    :goto_6
    invoke-virtual {p4}, Landroid/widget/LinearLayout;->getMeasuredWidth()I

    move-result p4

    goto :goto_a

    nop

    :goto_7
    invoke-virtual {p0}, Landroid/widget/HorizontalScrollView;->getMeasuredHeight()I

    move-result p1

    goto :goto_3

    nop

    :goto_8
    div-int/lit8 p1, p1, 0x2

    goto :goto_0

    nop

    :goto_9
    invoke-virtual {p3}, Landroid/widget/LinearLayout;->getMeasuredHeight()I

    move-result p3

    goto :goto_4

    nop

    :goto_a
    sub-int/2addr p1, p3

    goto :goto_8

    nop

    :goto_b
    add-int/2addr p3, p1

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
