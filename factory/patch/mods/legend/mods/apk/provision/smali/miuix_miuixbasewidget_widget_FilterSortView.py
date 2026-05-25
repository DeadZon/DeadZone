TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/miuixbasewidget/widget/FilterSortView.smali'
CLASS_FALLBACK_NAMES = ['FilterSortView.smali']
CLASS_ANCHORS = ['.super Landroidx/constraintlayout/widget/ConstraintLayout;']

PATCHES = [
    {
        'id': 'miuix_miuixbasewidget_widget_FilterSortView__onConfigurationChanged',
        'method': '.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V',
        'method_name': 'onConfigurationChanged',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/view/ViewGroup;->onConfigurationChanged(Landroid/content/res/Configuration;)V', 'iput-boolean p1, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mFilteredUpdated:Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 2

    invoke-super {p0, p1}, Landroid/view/ViewGroup;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    const/4 p1, 0x0

    iput-boolean p1, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mFilteredUpdated:Z

    return-void
.end method""",
        'replacement': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    iput-boolean p1, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mFilteredUpdated:Z

    goto :goto_3

    nop

    :goto_1
    invoke-super {p0, p1}, Landroid/view/ViewGroup;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    goto :goto_2

    nop

    :goto_2
    const/4 p1, 0x0

    goto :goto_0

    nop

    :goto_3
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_miuixbasewidget_widget_FilterSortView__onLayout',
        'method': '.method protected onLayout(ZIIII)V',
        'method_name': 'onLayout',
        'method_anchors': ['invoke-super/range {p0 .. p5}, Landroidx/constraintlayout/widget/ConstraintLayout;->onLayout(ZIIII)V', 'iget-object p1, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mBackgroundTabView:Lmiuix/miuixbasewidget/widget/FilterSortView$TabView;', 'invoke-virtual {p1}, Landroid/widget/LinearLayout;->getVisibility()I', 'if-eq p1, p2, :cond_0', 'iget-object p1, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mBackgroundTabView:Lmiuix/miuixbasewidget/widget/FilterSortView$TabView;', 'invoke-virtual {p1}, Landroid/widget/LinearLayout;->getLeft()I', 'iget p2, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mPadding:I', 'iget-object p3, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mBackgroundTabView:Lmiuix/miuixbasewidget/widget/FilterSortView$TabView;'],
        'type': 'method_replace',
        'search': """.method protected onLayout(ZIIII)V
    .registers 6

    invoke-super/range {p0 .. p5}, Landroidx/constraintlayout/widget/ConstraintLayout;->onLayout(ZIIII)V

    iget-object p1, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mBackgroundTabView:Lmiuix/miuixbasewidget/widget/FilterSortView$TabView;

    invoke-virtual {p1}, Landroid/widget/LinearLayout;->getVisibility()I

    move-result p1

    const/16 p2, 0x8

    if-eq p1, p2, :cond_0

    iget-object p1, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mBackgroundTabView:Lmiuix/miuixbasewidget/widget/FilterSortView$TabView;

    invoke-virtual {p1}, Landroid/widget/LinearLayout;->getLeft()I

    move-result p1

    iget p2, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mPadding:I

    iget-object p3, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mBackgroundTabView:Lmiuix/miuixbasewidget/widget/FilterSortView$TabView;

    invoke-virtual {p3}, Landroid/widget/LinearLayout;->getMeasuredWidth()I

    move-result p3

    add-int/2addr p3, p1

    iget-object p4, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mBackgroundTabView:Lmiuix/miuixbasewidget/widget/FilterSortView$TabView;

    invoke-virtual {p4}, Landroid/widget/LinearLayout;->getMeasuredHeight()I

    move-result p4

    add-int/2addr p4, p2

    iget-object p5, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mBackgroundTabView:Lmiuix/miuixbasewidget/widget/FilterSortView$TabView;

    invoke-virtual {p5, p1, p2, p3, p4}, Landroid/widget/LinearLayout;->layout(IIII)V

    :cond_0
    iget p1, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mFilteredId:I

    const/4 p2, -0x1

    if-eq p1, p2, :cond_1

    iget-boolean p2, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mFilteredUpdated:Z

    if-nez p2, :cond_1

    invoke-virtual {p0, p1}, Landroid/view/ViewGroup;->findViewById(I)Landroid/view/View;

    move-result-object p1

    check-cast p1, Lmiuix/miuixbasewidget/widget/FilterSortView$TabView;

    if-eqz p1, :cond_1

    invoke-direct {p0, p1}, Lmiuix/miuixbasewidget/widget/FilterSortView;->updateFiltered(Lmiuix/miuixbasewidget/widget/FilterSortView$TabView;)V

    invoke-virtual {p1}, Landroid/widget/LinearLayout;->getWidth()I

    move-result p1

    if-lez p1, :cond_1

    const/4 p1, 0x1

    iput-boolean p1, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mFilteredUpdated:Z

    :cond_1
    return-void
.end method""",
        'replacement': """.method protected onLayout(ZIIII)V
    .registers 6

    goto :goto_3

    nop

    :goto_0
    invoke-virtual {p4}, Landroid/widget/LinearLayout;->getMeasuredHeight()I

    move-result p4

    goto :goto_10

    nop

    :goto_1
    if-nez p1, :cond_0

    goto :goto_8

    :cond_0
    goto :goto_18

    nop

    :goto_2
    if-ne p1, p2, :cond_1

    goto :goto_8

    :cond_1
    goto :goto_15

    nop

    :goto_3
    invoke-super/range {p0 .. p5}, Landroidx/constraintlayout/widget/ConstraintLayout;->onLayout(ZIIII)V

    goto :goto_19

    nop

    :goto_4
    check-cast p1, Lmiuix/miuixbasewidget/widget/FilterSortView$TabView;

    goto :goto_1

    nop

    :goto_5
    iget p2, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mPadding:I

    goto :goto_17

    nop

    :goto_6
    const/4 p2, -0x1

    goto :goto_2

    nop

    :goto_7
    iput-boolean p1, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mFilteredUpdated:Z

    :goto_8
    goto :goto_1c

    nop

    :goto_9
    iget-object p1, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mBackgroundTabView:Lmiuix/miuixbasewidget/widget/FilterSortView$TabView;

    goto :goto_1d

    nop

    :goto_a
    const/16 p2, 0x8

    goto :goto_16

    nop

    :goto_b
    add-int/2addr p3, p1

    goto :goto_f

    nop

    :goto_c
    invoke-virtual {p1}, Landroid/widget/LinearLayout;->getWidth()I

    move-result p1

    goto :goto_1f

    nop

    :goto_d
    invoke-virtual {p5, p1, p2, p3, p4}, Landroid/widget/LinearLayout;->layout(IIII)V

    :goto_e
    goto :goto_12

    nop

    :goto_f
    iget-object p4, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mBackgroundTabView:Lmiuix/miuixbasewidget/widget/FilterSortView$TabView;

    goto :goto_0

    nop

    :goto_10
    add-int/2addr p4, p2

    goto :goto_1a

    nop

    :goto_11
    invoke-virtual {p0, p1}, Landroid/view/ViewGroup;->findViewById(I)Landroid/view/View;

    move-result-object p1

    goto :goto_4

    nop

    :goto_12
    iget p1, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mFilteredId:I

    goto :goto_6

    nop

    :goto_13
    const/4 p1, 0x1

    goto :goto_7

    nop

    :goto_14
    if-eqz p2, :cond_2

    goto :goto_8

    :cond_2
    goto :goto_11

    nop

    :goto_15
    iget-boolean p2, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mFilteredUpdated:Z

    goto :goto_14

    nop

    :goto_16
    if-ne p1, p2, :cond_3

    goto :goto_e

    :cond_3
    goto :goto_9

    nop

    :goto_17
    iget-object p3, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mBackgroundTabView:Lmiuix/miuixbasewidget/widget/FilterSortView$TabView;

    goto :goto_1e

    nop

    :goto_18
    invoke-direct {p0, p1}, Lmiuix/miuixbasewidget/widget/FilterSortView;->updateFiltered(Lmiuix/miuixbasewidget/widget/FilterSortView$TabView;)V

    goto :goto_c

    nop

    :goto_19
    iget-object p1, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mBackgroundTabView:Lmiuix/miuixbasewidget/widget/FilterSortView$TabView;

    goto :goto_1b

    nop

    :goto_1a
    iget-object p5, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mBackgroundTabView:Lmiuix/miuixbasewidget/widget/FilterSortView$TabView;

    goto :goto_d

    nop

    :goto_1b
    invoke-virtual {p1}, Landroid/widget/LinearLayout;->getVisibility()I

    move-result p1

    goto :goto_a

    nop

    :goto_1c
    return-void

    :goto_1d
    invoke-virtual {p1}, Landroid/widget/LinearLayout;->getLeft()I

    move-result p1

    goto :goto_5

    nop

    :goto_1e
    invoke-virtual {p3}, Landroid/widget/LinearLayout;->getMeasuredWidth()I

    move-result p3

    goto :goto_b

    nop

    :goto_1f
    if-gtz p1, :cond_4

    goto :goto_8

    :cond_4
    goto :goto_13

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_miuixbasewidget_widget_FilterSortView__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['invoke-super {p0, p1, p2}, Landroidx/constraintlayout/widget/ConstraintLayout;->onMeasure(II)V', 'iget p1, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mFilteredId:I', 'if-eq p1, p2, :cond_0', 'iget-object p1, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mBackgroundTabView:Lmiuix/miuixbasewidget/widget/FilterSortView$TabView;', 'invoke-virtual {p1}, Landroid/widget/LinearLayout;->getVisibility()I', 'if-eq p1, p2, :cond_0', 'iget p1, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mFilteredId:I', 'invoke-virtual {p0, p1}, Landroid/view/ViewGroup;->findViewById(I)Landroid/view/View;'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 5

    invoke-super {p0, p1, p2}, Landroidx/constraintlayout/widget/ConstraintLayout;->onMeasure(II)V

    iget p1, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mFilteredId:I

    const/4 p2, -0x1

    if-eq p1, p2, :cond_0

    iget-object p1, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mBackgroundTabView:Lmiuix/miuixbasewidget/widget/FilterSortView$TabView;

    invoke-virtual {p1}, Landroid/widget/LinearLayout;->getVisibility()I

    move-result p1

    const/16 p2, 0x8

    if-eq p1, p2, :cond_0

    iget p1, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mFilteredId:I

    invoke-virtual {p0, p1}, Landroid/view/ViewGroup;->findViewById(I)Landroid/view/View;

    move-result-object p1

    check-cast p1, Lmiuix/miuixbasewidget/widget/FilterSortView$TabView;

    iget-object p2, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mBackgroundTabView:Lmiuix/miuixbasewidget/widget/FilterSortView$TabView;

    invoke-virtual {p1}, Landroid/widget/LinearLayout;->getMeasuredWidth()I

    move-result p1

    const/high16 v0, 0x40000000

    invoke-static {p1, v0}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p1

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getMeasuredHeight()I

    move-result v1

    iget p0, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mPadding:I

    mul-int/lit8 p0, p0, 0x2

    sub-int/2addr v1, p0

    invoke-static {v1, v0}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p0

    invoke-virtual {p2, p1, p0}, Landroid/widget/LinearLayout;->measure(II)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 5

    goto :goto_1

    nop

    :goto_0
    invoke-virtual {p1}, Landroid/widget/LinearLayout;->getMeasuredWidth()I

    move-result p1

    goto :goto_11

    nop

    :goto_1
    invoke-super {p0, p1, p2}, Landroidx/constraintlayout/widget/ConstraintLayout;->onMeasure(II)V

    goto :goto_5

    nop

    :goto_2
    invoke-virtual {p2, p1, p0}, Landroid/widget/LinearLayout;->measure(II)V

    :goto_3
    goto :goto_13

    nop

    :goto_4
    mul-int/lit8 p0, p0, 0x2

    goto :goto_d

    nop

    :goto_5
    iget p1, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mFilteredId:I

    goto :goto_12

    nop

    :goto_6
    invoke-virtual {p0, p1}, Landroid/view/ViewGroup;->findViewById(I)Landroid/view/View;

    move-result-object p1

    goto :goto_10

    nop

    :goto_7
    iget p1, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mFilteredId:I

    goto :goto_6

    nop

    :goto_8
    invoke-virtual {p1}, Landroid/widget/LinearLayout;->getVisibility()I

    move-result p1

    goto :goto_f

    nop

    :goto_9
    iget p0, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mPadding:I

    goto :goto_4

    nop

    :goto_a
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getMeasuredHeight()I

    move-result v1

    goto :goto_9

    nop

    :goto_b
    invoke-static {p1, v0}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p1

    goto :goto_a

    nop

    :goto_c
    iget-object p1, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mBackgroundTabView:Lmiuix/miuixbasewidget/widget/FilterSortView$TabView;

    goto :goto_8

    nop

    :goto_d
    sub-int/2addr v1, p0

    goto :goto_14

    nop

    :goto_e
    iget-object p2, p0, Lmiuix/miuixbasewidget/widget/FilterSortView;->mBackgroundTabView:Lmiuix/miuixbasewidget/widget/FilterSortView$TabView;

    goto :goto_0

    nop

    :goto_f
    const/16 p2, 0x8

    goto :goto_16

    nop

    :goto_10
    check-cast p1, Lmiuix/miuixbasewidget/widget/FilterSortView$TabView;

    goto :goto_e

    nop

    :goto_11
    const/high16 v0, 0x40000000

    goto :goto_b

    nop

    :goto_12
    const/4 p2, -0x1

    goto :goto_15

    nop

    :goto_13
    return-void

    :goto_14
    invoke-static {v1, v0}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p0

    goto :goto_2

    nop

    :goto_15
    if-ne p1, p2, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_c

    nop

    :goto_16
    if-ne p1, p2, :cond_1

    goto :goto_3

    :cond_1
    goto :goto_7

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
