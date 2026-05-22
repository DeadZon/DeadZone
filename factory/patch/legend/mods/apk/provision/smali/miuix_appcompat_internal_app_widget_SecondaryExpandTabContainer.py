TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/app/widget/SecondaryExpandTabContainer.smali'
CLASS_FALLBACK_NAMES = ['SecondaryExpandTabContainer.smali']
CLASS_ANCHORS = ['.super Lmiuix/springback/view/SpringBackLayout;', '.implements Lmiuix/appcompat/internal/app/widget/SecondaryTabBar;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_app_widget_SecondaryExpandTabContainer__onLayout',
        'method': '.method protected onLayout(ZIIII)V',
        'method_name': 'onLayout',
        'method_anchors': ['invoke-super/range {p0 .. p5}, Lmiuix/springback/view/SpringBackLayout;->onLayout(ZIIII)V', 'iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/SecondaryExpandTabContainer;->mTabContainer:Lmiuix/appcompat/internal/app/widget/SecondaryTabExpandContainerView;', 'invoke-virtual {p1}, Lmiuix/miuixbasewidget/widget/FilterSortView2;->canScrollHorizontally()Z', 'invoke-virtual {p0, p1}, Lmiuix/springback/view/SpringBackLayout;->setSpringBackEnable(Z)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onLayout(ZIIII)V
    .registers 6

    invoke-super/range {p0 .. p5}, Lmiuix/springback/view/SpringBackLayout;->onLayout(ZIIII)V

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/SecondaryExpandTabContainer;->mTabContainer:Lmiuix/appcompat/internal/app/widget/SecondaryTabExpandContainerView;

    invoke-virtual {p1}, Lmiuix/miuixbasewidget/widget/FilterSortView2;->canScrollHorizontally()Z

    move-result p1

    invoke-virtual {p0, p1}, Lmiuix/springback/view/SpringBackLayout;->setSpringBackEnable(Z)V

    return-void
.end method""",
        'replacement': """.method protected onLayout(ZIIII)V
    .registers 6

    goto :goto_0

    nop

    :goto_0
    invoke-super/range {p0 .. p5}, Lmiuix/springback/view/SpringBackLayout;->onLayout(ZIIII)V

    goto :goto_1

    nop

    :goto_1
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/SecondaryExpandTabContainer;->mTabContainer:Lmiuix/appcompat/internal/app/widget/SecondaryTabExpandContainerView;

    goto :goto_3

    nop

    :goto_2
    invoke-virtual {p0, p1}, Lmiuix/springback/view/SpringBackLayout;->setSpringBackEnable(Z)V

    goto :goto_4

    nop

    :goto_3
    invoke-virtual {p1}, Lmiuix/miuixbasewidget/widget/FilterSortView2;->canScrollHorizontally()Z

    move-result p1

    goto :goto_2

    nop

    :goto_4
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
