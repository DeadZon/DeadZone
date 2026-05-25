TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/app/widget/AbsActionBarView.smali'
CLASS_FALLBACK_NAMES = ['AbsActionBarView.smali']
CLASS_ANCHORS = ['.super Landroid/view/ViewGroup;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_app_widget_AbsActionBarView__bindActionBarTransitionListeners',
        'method': '.method bindActionBarTransitionListeners(Ljava/util/List;)V',
        'method_name': 'bindActionBarTransitionListeners',
        'method_anchors': ['iput-object p1, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mActionBarTransitionListeners:Ljava/util/List;', 'return-void'],
        'type': 'method_replace',
        'search': """.method bindActionBarTransitionListeners(Ljava/util/List;)V
    .registers 2

    iput-object p1, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mActionBarTransitionListeners:Ljava/util/List;

    return-void
.end method""",
        'replacement': """.method bindActionBarTransitionListeners(Ljava/util/List;)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    iput-object p1, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mActionBarTransitionListeners:Ljava/util/List;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_AbsActionBarView__getActionBarStyle',
        'method': '.method getActionBarStyle()I',
        'method_name': 'getActionBarStyle',
        'method_anchors': ['return p0'],
        'type': 'method_replace',
        'search': """.method getActionBarStyle()I
    .registers 1

    const p0, 0x10102ce

    return p0
.end method""",
        'replacement': """.method getActionBarStyle()I
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    const p0, 0x10102ce

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_AbsActionBarView__measureChildView',
        'method': '.method protected measureChildView(Landroid/view/View;III)I',
        'method_name': 'measureChildView',
        'method_anchors': ['invoke-static {p2, p0}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I', 'invoke-virtual {p1, p0, p3}, Landroid/view/View;->measure(II)V', 'invoke-virtual {p1}, Landroid/view/View;->getMeasuredWidth()I', 'invoke-static {p0, p2}, Ljava/lang/Math;->max(II)I', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected measureChildView(Landroid/view/View;III)I
    .registers 5

    const/high16 p0, -0x80000000

    invoke-static {p2, p0}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p0

    invoke-virtual {p1, p0, p3}, Landroid/view/View;->measure(II)V

    invoke-virtual {p1}, Landroid/view/View;->getMeasuredWidth()I

    move-result p0

    sub-int/2addr p2, p0

    sub-int/2addr p2, p4

    const/4 p0, 0x0

    invoke-static {p0, p2}, Ljava/lang/Math;->max(II)I

    move-result p0

    return p0
.end method""",
        'replacement': """.method protected measureChildView(Landroid/view/View;III)I
    .registers 5

    goto :goto_5

    nop

    :goto_0
    invoke-virtual {p1}, Landroid/view/View;->getMeasuredWidth()I

    move-result p0

    goto :goto_2

    nop

    :goto_1
    const/4 p0, 0x0

    goto :goto_3

    nop

    :goto_2
    sub-int/2addr p2, p0

    goto :goto_6

    nop

    :goto_3
    invoke-static {p0, p2}, Ljava/lang/Math;->max(II)I

    move-result p0

    goto :goto_8

    nop

    :goto_4
    invoke-static {p2, p0}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p0

    goto :goto_7

    nop

    :goto_5
    const/high16 p0, -0x80000000

    goto :goto_4

    nop

    :goto_6
    sub-int/2addr p2, p4

    goto :goto_1

    nop

    :goto_7
    invoke-virtual {p1, p0, p3}, Landroid/view/View;->measure(II)V

    goto :goto_0

    nop

    :goto_8
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_AbsActionBarView__onAnimatedExpandStateChanged',
        'method': '.method protected onAnimatedExpandStateChanged(II)V',
        'method_name': 'onAnimatedExpandStateChanged',
        'method_anchors': ['return-void'],
        'type': 'method_replace',
        'search': """.method protected onAnimatedExpandStateChanged(II)V
    .registers 3

    return-void
.end method""",
        'replacement': """.method protected onAnimatedExpandStateChanged(II)V
    .registers 3

    goto :goto_0

    nop

    :goto_0
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_AbsActionBarView__onConfigurationChanged',
        'method': '.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V',
        'method_name': 'onConfigurationChanged',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/view/ViewGroup;->onConfigurationChanged(Landroid/content/res/Configuration;)V', 'iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mSplitWhenNarrow:Z', 'if-eqz v0, :cond_0', 'invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;', 'invoke-virtual {v0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;', 'sget v1, Lmiuix/appcompat/R$bool;->abc_split_action_bar_is_narrow:I', 'invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getBoolean(I)Z', 'invoke-virtual {p0, v0}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->setSplitActionBar(Z)V'],
        'type': 'method_replace',
        'search': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 4

    invoke-super {p0, p1}, Landroid/view/ViewGroup;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mSplitWhenNarrow:Z

    if-eqz v0, :cond_0

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-virtual {v0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    sget v1, Lmiuix/appcompat/R$bool;->abc_split_action_bar_is_narrow:I

    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v0

    invoke-virtual {p0, v0}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->setSplitActionBar(Z)V

    :cond_0
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mActionMenuPresenter:Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;

    if-eqz p0, :cond_1

    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    :cond_1
    return-void
.end method""",
        'replacement': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 4

    goto :goto_9

    nop

    :goto_0
    return-void

    :goto_1
    iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mSplitWhenNarrow:Z

    goto :goto_c

    nop

    :goto_2
    invoke-virtual {p0, v0}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->setSplitActionBar(Z)V

    :goto_3
    goto :goto_d

    nop

    :goto_4
    if-nez p0, :cond_0

    goto :goto_7

    :cond_0
    goto :goto_6

    nop

    :goto_5
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;

    move-result-object v0

    goto :goto_b

    nop

    :goto_6
    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    :goto_7
    goto :goto_0

    nop

    :goto_8
    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v0

    goto :goto_2

    nop

    :goto_9
    invoke-super {p0, p1}, Landroid/view/ViewGroup;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    goto :goto_1

    nop

    :goto_a
    sget v1, Lmiuix/appcompat/R$bool;->abc_split_action_bar_is_narrow:I

    goto :goto_8

    nop

    :goto_b
    invoke-virtual {v0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    goto :goto_a

    nop

    :goto_c
    if-nez v0, :cond_1

    goto :goto_3

    :cond_1
    goto :goto_5

    nop

    :goto_d
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mActionMenuPresenter:Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_AbsActionBarView__onExpandStateChanged',
        'method': '.method protected onExpandStateChanged(II)V',
        'method_name': 'onExpandStateChanged',
        'method_anchors': ['return-void'],
        'type': 'method_replace',
        'search': """.method protected onExpandStateChanged(II)V
    .registers 3

    return-void
.end method""",
        'replacement': """.method protected onExpandStateChanged(II)V
    .registers 3

    goto :goto_0

    nop

    :goto_0
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_AbsActionBarView__positionChild',
        'method': '.method protected positionChild(Landroid/view/View;III)I',
        'method_name': 'positionChild',
        'method_anchors': ['invoke-virtual/range {v0 .. v5}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->positionChild(Landroid/view/View;IIIZ)I', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected positionChild(Landroid/view/View;III)I
    .registers 11

    const/4 v5, 0x1

    move-object v0, p0

    move-object v1, p1

    move v2, p2

    move v3, p3

    move v4, p4

    invoke-virtual/range {v0 .. v5}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->positionChild(Landroid/view/View;IIIZ)I

    move-result p0

    return p0
.end method""",
        'replacement': """.method protected positionChild(Landroid/view/View;III)I
    .registers 11

    goto :goto_3

    nop

    :goto_0
    move v2, p2

    goto :goto_4

    nop

    :goto_1
    return p0

    :goto_2
    move v4, p4

    goto :goto_6

    nop

    :goto_3
    const/4 v5, 0x1

    goto :goto_5

    nop

    :goto_4
    move v3, p3

    goto :goto_2

    nop

    :goto_5
    move-object v0, p0

    goto :goto_7

    nop

    :goto_6
    invoke-virtual/range {v0 .. v5}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->positionChild(Landroid/view/View;IIIZ)I

    move-result p0

    goto :goto_1

    nop

    :goto_7
    move-object v1, p1

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_AbsActionBarView__positionChild',
        'method': '.method protected positionChild(Landroid/view/View;IIIZ)I',
        'method_name': 'positionChild',
        'method_anchors': ['invoke-virtual {p1}, Landroid/view/View;->getMeasuredWidth()I', 'invoke-virtual {p1}, Landroid/view/View;->getMeasuredHeight()I', 'if-nez p5, :cond_0', 'iget p3, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mTitleMinHeight:I', 'invoke-static/range {v2 .. v7}, Lmiuix/internal/util/ViewUtils;->layoutChildView(Landroid/view/ViewGroup;Landroid/view/View;IIII)V', 'return v0'],
        'type': 'method_replace',
        'search': """.method protected positionChild(Landroid/view/View;IIIZ)I
    .registers 14

    invoke-virtual {p1}, Landroid/view/View;->getMeasuredWidth()I

    move-result v0

    invoke-virtual {p1}, Landroid/view/View;->getMeasuredHeight()I

    move-result v1

    sub-int/2addr p4, v1

    div-int/lit8 p4, p4, 0x2

    add-int/2addr p3, p4

    if-nez p5, :cond_0

    iget p3, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mTitleMinHeight:I

    sub-int/2addr p3, v1

    div-int/lit8 p3, p3, 0x2

    :cond_0
    move v5, p3

    add-int v6, p2, v0

    add-int v7, v5, v1

    move-object v2, p0

    move-object v3, p1

    move v4, p2

    invoke-static/range {v2 .. v7}, Lmiuix/internal/util/ViewUtils;->layoutChildView(Landroid/view/ViewGroup;Landroid/view/View;IIII)V

    return v0
.end method""",
        'replacement': """.method protected positionChild(Landroid/view/View;IIIZ)I
    .registers 14

    goto :goto_f

    nop

    :goto_0
    invoke-virtual {p1}, Landroid/view/View;->getMeasuredHeight()I

    move-result v1

    goto :goto_3

    nop

    :goto_1
    invoke-static/range {v2 .. v7}, Lmiuix/internal/util/ViewUtils;->layoutChildView(Landroid/view/ViewGroup;Landroid/view/View;IIII)V

    goto :goto_4

    nop

    :goto_2
    move-object v3, p1

    goto :goto_c

    nop

    :goto_3
    sub-int/2addr p4, v1

    goto :goto_11

    nop

    :goto_4
    return v0

    :goto_5
    sub-int/2addr p3, v1

    goto :goto_a

    nop

    :goto_6
    add-int v7, v5, v1

    goto :goto_10

    nop

    :goto_7
    if-eqz p5, :cond_0

    goto :goto_b

    :cond_0
    goto :goto_8

    nop

    :goto_8
    iget p3, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mTitleMinHeight:I

    goto :goto_5

    nop

    :goto_9
    add-int/2addr p3, p4

    goto :goto_7

    nop

    :goto_a
    div-int/lit8 p3, p3, 0x2

    :goto_b
    goto :goto_d

    nop

    :goto_c
    move v4, p2

    goto :goto_1

    nop

    :goto_d
    move v5, p3

    goto :goto_e

    nop

    :goto_e
    add-int v6, p2, v0

    goto :goto_6

    nop

    :goto_f
    invoke-virtual {p1}, Landroid/view/View;->getMeasuredWidth()I

    move-result v0

    goto :goto_0

    nop

    :goto_10
    move-object v2, p0

    goto :goto_2

    nop

    :goto_11
    div-int/lit8 p4, p4, 0x2

    goto :goto_9

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_AbsActionBarView__positionChildInverse',
        'method': '.method protected positionChildInverse(Landroid/view/View;III)I',
        'method_name': 'positionChildInverse',
        'method_anchors': ['invoke-virtual {p1}, Landroid/view/View;->getMeasuredWidth()I', 'invoke-virtual {p1}, Landroid/view/View;->getMeasuredHeight()I', 'iget v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mTitleMinHeight:I', 'invoke-static/range {v1 .. v6}, Lmiuix/internal/util/ViewUtils;->layoutChildView(Landroid/view/ViewGroup;Landroid/view/View;IIII)V', 'return p3'],
        'type': 'method_replace',
        'search': """.method protected positionChildInverse(Landroid/view/View;III)I
    .registers 12

    invoke-virtual {p1}, Landroid/view/View;->getMeasuredWidth()I

    move-result p3

    invoke-virtual {p1}, Landroid/view/View;->getMeasuredHeight()I

    move-result p4

    iget v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mTitleMinHeight:I

    sub-int/2addr v0, p4

    div-int/lit8 v4, v0, 0x2

    sub-int v3, p2, p3

    add-int v6, v4, p4

    move-object v1, p0

    move-object v2, p1

    move v5, p2

    invoke-static/range {v1 .. v6}, Lmiuix/internal/util/ViewUtils;->layoutChildView(Landroid/view/ViewGroup;Landroid/view/View;IIII)V

    return p3
.end method""",
        'replacement': """.method protected positionChildInverse(Landroid/view/View;III)I
    .registers 12

    goto :goto_b

    nop

    :goto_0
    add-int v6, v4, p4

    goto :goto_7

    nop

    :goto_1
    invoke-static/range {v1 .. v6}, Lmiuix/internal/util/ViewUtils;->layoutChildView(Landroid/view/ViewGroup;Landroid/view/View;IIII)V

    goto :goto_5

    nop

    :goto_2
    iget v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mTitleMinHeight:I

    goto :goto_9

    nop

    :goto_3
    invoke-virtual {p1}, Landroid/view/View;->getMeasuredHeight()I

    move-result p4

    goto :goto_2

    nop

    :goto_4
    move v5, p2

    goto :goto_1

    nop

    :goto_5
    return p3

    :goto_6
    sub-int v3, p2, p3

    goto :goto_0

    nop

    :goto_7
    move-object v1, p0

    goto :goto_8

    nop

    :goto_8
    move-object v2, p1

    goto :goto_4

    nop

    :goto_9
    sub-int/2addr v0, p4

    goto :goto_a

    nop

    :goto_a
    div-int/lit8 v4, v0, 0x2

    goto :goto_6

    nop

    :goto_b
    invoke-virtual {p1}, Landroid/view/View;->getMeasuredWidth()I

    move-result p3

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_AbsActionBarView__positionChildWithOffset',
        'method': '.method protected positionChildWithOffset(Landroid/view/View;IIIZI)I',
        'method_name': 'positionChildWithOffset',
        'method_anchors': ['invoke-virtual {p1}, Landroid/view/View;->getMeasuredWidth()I', 'invoke-virtual {p1}, Landroid/view/View;->getMeasuredHeight()I', 'if-nez p5, :cond_0', 'iget p3, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mTitleMinHeight:I', 'invoke-static/range {v2 .. v7}, Lmiuix/internal/util/ViewUtils;->layoutChildView(Landroid/view/ViewGroup;Landroid/view/View;IIII)V', 'return v0'],
        'type': 'method_replace',
        'search': """.method protected positionChildWithOffset(Landroid/view/View;IIIZI)I
    .registers 15

    invoke-virtual {p1}, Landroid/view/View;->getMeasuredWidth()I

    move-result v0

    invoke-virtual {p1}, Landroid/view/View;->getMeasuredHeight()I

    move-result v1

    sub-int/2addr p4, v1

    div-int/lit8 p4, p4, 0x2

    add-int/2addr p3, p4

    if-nez p5, :cond_0

    iget p3, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mTitleMinHeight:I

    sub-int/2addr p3, v1

    div-int/lit8 p3, p3, 0x2

    :cond_0
    move v5, p3

    add-int v4, p2, p6

    add-int/2addr p2, v0

    add-int v6, p2, p6

    add-int v7, v5, v1

    move-object v2, p0

    move-object v3, p1

    invoke-static/range {v2 .. v7}, Lmiuix/internal/util/ViewUtils;->layoutChildView(Landroid/view/ViewGroup;Landroid/view/View;IIII)V

    add-int/2addr v0, p6

    return v0
.end method""",
        'replacement': """.method protected positionChildWithOffset(Landroid/view/View;IIIZI)I
    .registers 15

    goto :goto_8

    nop

    :goto_0
    add-int v7, v5, v1

    goto :goto_3

    nop

    :goto_1
    move v5, p3

    goto :goto_10

    nop

    :goto_2
    add-int/2addr p2, v0

    goto :goto_c

    nop

    :goto_3
    move-object v2, p0

    goto :goto_7

    nop

    :goto_4
    div-int/lit8 p3, p3, 0x2

    :goto_5
    goto :goto_1

    nop

    :goto_6
    add-int/2addr v0, p6

    goto :goto_12

    nop

    :goto_7
    move-object v3, p1

    goto :goto_f

    nop

    :goto_8
    invoke-virtual {p1}, Landroid/view/View;->getMeasuredWidth()I

    move-result v0

    goto :goto_11

    nop

    :goto_9
    div-int/lit8 p4, p4, 0x2

    goto :goto_d

    nop

    :goto_a
    sub-int/2addr p3, v1

    goto :goto_4

    nop

    :goto_b
    iget p3, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mTitleMinHeight:I

    goto :goto_a

    nop

    :goto_c
    add-int v6, p2, p6

    goto :goto_0

    nop

    :goto_d
    add-int/2addr p3, p4

    goto :goto_13

    nop

    :goto_e
    sub-int/2addr p4, v1

    goto :goto_9

    nop

    :goto_f
    invoke-static/range {v2 .. v7}, Lmiuix/internal/util/ViewUtils;->layoutChildView(Landroid/view/ViewGroup;Landroid/view/View;IIII)V

    goto :goto_6

    nop

    :goto_10
    add-int v4, p2, p6

    goto :goto_2

    nop

    :goto_11
    invoke-virtual {p1}, Landroid/view/View;->getMeasuredHeight()I

    move-result v1

    goto :goto_e

    nop

    :goto_12
    return v0

    :goto_13
    if-eqz p5, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_b

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_AbsActionBarView__setActionMenuItemLimit',
        'method': '.method protected setActionMenuItemLimit(I)V',
        'method_name': 'setActionMenuItemLimit',
        'method_anchors': ['iput p1, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mMaxActionMenuItemCount:I', 'iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mActionMenuPresenter:Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;', 'if-eqz p0, :cond_0', 'if-nez v0, :cond_0', 'invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->setItemLimit(I)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected setActionMenuItemLimit(I)V
    .registers 3

    iput p1, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mMaxActionMenuItemCount:I

    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mActionMenuPresenter:Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;

    if-eqz p0, :cond_0

    instance-of v0, p0, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuPresenter;

    if-nez v0, :cond_0

    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->setItemLimit(I)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected setActionMenuItemLimit(I)V
    .registers 3

    goto :goto_7

    nop

    :goto_0
    return-void

    :goto_1
    if-nez p0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_5

    nop

    :goto_2
    if-eqz v0, :cond_1

    goto :goto_4

    :cond_1
    goto :goto_3

    nop

    :goto_3
    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->setItemLimit(I)V

    :goto_4
    goto :goto_0

    nop

    :goto_5
    instance-of v0, p0, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuPresenter;

    goto :goto_2

    nop

    :goto_6
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mActionMenuPresenter:Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;

    goto :goto_1

    nop

    :goto_7
    iput p1, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mMaxActionMenuItemCount:I

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_AbsActionBarView__setExpandStateByUser',
        'method': '.method protected setExpandStateByUser(I)V',
        'method_name': 'setExpandStateByUser',
        'method_anchors': ['if-eq p1, v0, :cond_0', 'iput-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mUserSetExpandState:Z', 'iput p1, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mUserExpandState:I', 'return-void', 'iput-boolean p1, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mUserSetExpandState:Z', 'iput v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mUserExpandState:I', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected setExpandStateByUser(I)V
    .registers 3

    const/4 v0, -0x1

    if-eq p1, v0, :cond_0

    const/4 v0, 0x1

    iput-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mUserSetExpandState:Z

    iput p1, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mUserExpandState:I

    return-void

    :cond_0
    const/4 p1, 0x0

    iput-boolean p1, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mUserSetExpandState:Z

    iput v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mUserExpandState:I

    return-void
.end method""",
        'replacement': """.method protected setExpandStateByUser(I)V
    .registers 3

    goto :goto_8

    nop

    :goto_0
    const/4 v0, 0x1

    goto :goto_a

    nop

    :goto_1
    iput v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mUserExpandState:I

    goto :goto_3

    nop

    :goto_2
    const/4 p1, 0x0

    goto :goto_9

    nop

    :goto_3
    return-void

    :goto_4
    return-void

    :goto_5
    goto :goto_2

    nop

    :goto_6
    if-ne p1, v0, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_0

    nop

    :goto_7
    iput p1, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mUserExpandState:I

    goto :goto_4

    nop

    :goto_8
    const/4 v0, -0x1

    goto :goto_6

    nop

    :goto_9
    iput-boolean p1, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mUserSetExpandState:Z

    goto :goto_1

    nop

    :goto_a
    iput-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mUserSetExpandState:Z

    goto :goto_7

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
