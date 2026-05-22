TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/miuixbasewidget/widget/FilterSortView2$TabView.smali'
CLASS_FALLBACK_NAMES = ['FilterSortView2$TabView.smali']
CLASS_ANCHORS = ['.super Landroid/widget/FrameLayout;']

PATCHES = [
    {
        'id': 'miuix_miuixbasewidget_widget_FilterSortView2__TabView__getTabLayoutResource',
        'method': '.method protected getTabLayoutResource()I',
        'method_name': 'getTabLayoutResource',
        'method_anchors': ['sget p0, Lmiuix/miuixbasewidget/R$layout;->miuix_appcompat_filter_sort_tab_view_2:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected getTabLayoutResource()I
    .registers 1

    sget p0, Lmiuix/miuixbasewidget/R$layout;->miuix_appcompat_filter_sort_tab_view_2:I

    return p0
.end method""",
        'replacement': """.method protected getTabLayoutResource()I
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    sget p0, Lmiuix/miuixbasewidget/R$layout;->miuix_appcompat_filter_sort_tab_view_2:I

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_miuixbasewidget_widget_FilterSortView2__TabView__initView',
        'method': '.method protected initView(Ljava/lang/CharSequence;Z)V',
        'method_name': 'initView',
        'method_anchors': ['iget-object v0, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2$TabView;->mArrow:Landroid/widget/ImageView;', 'iget-object v1, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2$TabView;->mArrowIcon:Landroid/graphics/drawable/Drawable;', 'invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setBackground(Landroid/graphics/drawable/Drawable;)V', 'iget-object v0, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2$TabView;->mTextView:Landroid/widget/TextView;', 'invoke-virtual {v0, p1}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V', 'iget-object p1, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2$TabView;->mArrow:Landroid/widget/ImageView;', 'iget v0, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2$TabView;->mIndicatorVisibility:I', 'invoke-virtual {p1, v0}, Landroid/widget/ImageView;->setVisibility(I)V'],
        'type': 'method_replace',
        'search': """.method protected initView(Ljava/lang/CharSequence;Z)V
    .registers 5

    iget-object v0, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2$TabView;->mArrow:Landroid/widget/ImageView;

    iget-object v1, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2$TabView;->mArrowIcon:Landroid/graphics/drawable/Drawable;

    invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setBackground(Landroid/graphics/drawable/Drawable;)V

    iget-object v0, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2$TabView;->mTextView:Landroid/widget/TextView;

    invoke-virtual {v0, p1}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    iget-object p1, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2$TabView;->mArrow:Landroid/widget/ImageView;

    iget v0, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2$TabView;->mIndicatorVisibility:I

    invoke-virtual {p1, v0}, Landroid/widget/ImageView;->setVisibility(I)V

    invoke-direct {p0, p2}, Lmiuix/miuixbasewidget/widget/FilterSortView2$TabView;->setDescending(Z)V

    invoke-direct {p0}, Lmiuix/miuixbasewidget/widget/FilterSortView2$TabView;->updateTextAppearance()V

    return-void
.end method""",
        'replacement': """.method protected initView(Ljava/lang/CharSequence;Z)V
    .registers 5

    goto :goto_3

    nop

    :goto_0
    invoke-virtual {v0, p1}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    goto :goto_1

    nop

    :goto_1
    iget-object p1, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2$TabView;->mArrow:Landroid/widget/ImageView;

    goto :goto_8

    nop

    :goto_2
    return-void

    :goto_3
    iget-object v0, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2$TabView;->mArrow:Landroid/widget/ImageView;

    goto :goto_6

    nop

    :goto_4
    invoke-virtual {p1, v0}, Landroid/widget/ImageView;->setVisibility(I)V

    goto :goto_7

    nop

    :goto_5
    invoke-direct {p0}, Lmiuix/miuixbasewidget/widget/FilterSortView2$TabView;->updateTextAppearance()V

    goto :goto_2

    nop

    :goto_6
    iget-object v1, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2$TabView;->mArrowIcon:Landroid/graphics/drawable/Drawable;

    goto :goto_a

    nop

    :goto_7
    invoke-direct {p0, p2}, Lmiuix/miuixbasewidget/widget/FilterSortView2$TabView;->setDescending(Z)V

    goto :goto_5

    nop

    :goto_8
    iget v0, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2$TabView;->mIndicatorVisibility:I

    goto :goto_4

    nop

    :goto_9
    iget-object v0, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2$TabView;->mTextView:Landroid/widget/TextView;

    goto :goto_0

    nop

    :goto_a
    invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setBackground(Landroid/graphics/drawable/Drawable;)V

    goto :goto_9

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
