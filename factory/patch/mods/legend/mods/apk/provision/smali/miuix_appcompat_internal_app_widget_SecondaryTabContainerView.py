TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/app/widget/SecondaryTabContainerView.smali'
CLASS_FALLBACK_NAMES = ['SecondaryTabContainerView.smali']
CLASS_ANCHORS = ['.super Lmiuix/miuixbasewidget/widget/FilterSortView2;', '.implements Lmiuix/appcompat/internal/app/widget/SecondaryTabBar;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_app_widget_SecondaryTabContainerView__getTabContainerHeight',
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
        'id': 'miuix_appcompat_internal_app_widget_SecondaryTabContainerView__getDefaultTabTextStyle',
        'method': '.method protected getDefaultTabTextStyle()I',
        'method_name': 'getDefaultTabTextStyle',
        'method_anchors': ['sget p0, Lmiuix/appcompat/R$attr;->actionBarTabTextSecondaryStyle:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected getDefaultTabTextStyle()I
    .registers 1

    sget p0, Lmiuix/appcompat/R$attr;->actionBarTabTextSecondaryStyle:I

    return p0
.end method""",
        'replacement': """.method protected getDefaultTabTextStyle()I
    .registers 1

    goto :goto_0

    nop

    :goto_0
    sget p0, Lmiuix/appcompat/R$attr;->actionBarTabTextSecondaryStyle:I

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
        'id': 'miuix_appcompat_internal_app_widget_SecondaryTabContainerView__getTabActivatedTextStyle',
        'method': '.method protected getTabActivatedTextStyle()I',
        'method_name': 'getTabActivatedTextStyle',
        'method_anchors': ['sget p0, Lmiuix/appcompat/R$attr;->actionBarTabActivatedTextSecondaryStyle:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected getTabActivatedTextStyle()I
    .registers 1

    sget p0, Lmiuix/appcompat/R$attr;->actionBarTabActivatedTextSecondaryStyle:I

    return p0
.end method""",
        'replacement': """.method protected getTabActivatedTextStyle()I
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    sget p0, Lmiuix/appcompat/R$attr;->actionBarTabActivatedTextSecondaryStyle:I

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_SecondaryTabContainerView__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['iget v0, p0, Lmiuix/appcompat/internal/app/widget/SecondaryTabContainerView;->mContentHeight:I', 'if-eq v0, v1, :cond_0', 'invoke-static {v0, p2}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I', 'invoke-super {p0, p1, p2}, Lmiuix/miuixbasewidget/widget/FilterSortView2;->onMeasure(II)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 5

    iget v0, p0, Lmiuix/appcompat/internal/app/widget/SecondaryTabContainerView;->mContentHeight:I

    const/4 v1, -0x2

    if-eq v0, v1, :cond_0

    const/high16 p2, 0x40000000

    invoke-static {v0, p2}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p2

    :cond_0
    invoke-super {p0, p1, p2}, Lmiuix/miuixbasewidget/widget/FilterSortView2;->onMeasure(II)V

    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 5

    goto :goto_5

    nop

    :goto_0
    return-void

    :goto_1
    const/high16 p2, 0x40000000

    goto :goto_6

    nop

    :goto_2
    const/4 v1, -0x2

    goto :goto_3

    nop

    :goto_3
    if-ne v0, v1, :cond_0

    goto :goto_7

    :cond_0
    goto :goto_1

    nop

    :goto_4
    invoke-super {p0, p1, p2}, Lmiuix/miuixbasewidget/widget/FilterSortView2;->onMeasure(II)V

    goto :goto_0

    nop

    :goto_5
    iget v0, p0, Lmiuix/appcompat/internal/app/widget/SecondaryTabContainerView;->mContentHeight:I

    goto :goto_2

    nop

    :goto_6
    invoke-static {v0, p2}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p2

    :goto_7
    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_SecondaryTabContainerView__setContentHeight',
        'method': '.method protected setContentHeight(I)V',
        'method_name': 'setContentHeight',
        'method_anchors': ['iget v0, p0, Lmiuix/appcompat/internal/app/widget/SecondaryTabContainerView;->mContentHeight:I', 'if-eq v0, p1, :cond_0', 'iput p1, p0, Lmiuix/appcompat/internal/app/widget/SecondaryTabContainerView;->mContentHeight:I', 'invoke-virtual {p0}, Landroid/widget/HorizontalScrollView;->requestLayout()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected setContentHeight(I)V
    .registers 3

    iget v0, p0, Lmiuix/appcompat/internal/app/widget/SecondaryTabContainerView;->mContentHeight:I

    if-eq v0, p1, :cond_0

    iput p1, p0, Lmiuix/appcompat/internal/app/widget/SecondaryTabContainerView;->mContentHeight:I

    invoke-virtual {p0}, Landroid/widget/HorizontalScrollView;->requestLayout()V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected setContentHeight(I)V
    .registers 3

    goto :goto_3

    nop

    :goto_0
    return-void

    :goto_1
    invoke-virtual {p0}, Landroid/widget/HorizontalScrollView;->requestLayout()V

    :goto_2
    goto :goto_0

    nop

    :goto_3
    iget v0, p0, Lmiuix/appcompat/internal/app/widget/SecondaryTabContainerView;->mContentHeight:I

    goto :goto_4

    nop

    :goto_4
    if-ne v0, p1, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_5

    nop

    :goto_5
    iput p1, p0, Lmiuix/appcompat/internal/app/widget/SecondaryTabContainerView;->mContentHeight:I

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
