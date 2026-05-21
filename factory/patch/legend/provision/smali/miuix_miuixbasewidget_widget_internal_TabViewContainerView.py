TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/miuixbasewidget/widget/internal/TabViewContainerView.smali'
CLASS_FALLBACK_NAMES = ['TabViewContainerView.smali']
CLASS_ANCHORS = ['.super Landroid/widget/FrameLayout;']

PATCHES = [
    {
        'id': 'miuix_miuixbasewidget_widget_internal_TabViewContainerView__onConfigurationChanged',
        'method': '.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V',
        'method_name': 'onConfigurationChanged',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/widget/FrameLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V', 'iget p1, p1, Landroid/content/res/Configuration;->densityDpi:I', 'iget v0, p0, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->mDensityDpi:I', 'if-eq p1, v0, :cond_0', 'iput p1, p0, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->mDensityDpi:I', 'invoke-direct {p0}, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->updateLayoutParams()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 3

    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    iget p1, p1, Landroid/content/res/Configuration;->densityDpi:I

    iget v0, p0, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->mDensityDpi:I

    if-eq p1, v0, :cond_0

    iput p1, p0, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->mDensityDpi:I

    invoke-direct {p0}, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->updateLayoutParams()V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 3

    goto :goto_5

    nop

    :goto_0
    iput p1, p0, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->mDensityDpi:I

    goto :goto_2

    nop

    :goto_1
    iget v0, p0, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->mDensityDpi:I

    goto :goto_7

    nop

    :goto_2
    invoke-direct {p0}, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->updateLayoutParams()V

    :goto_3
    goto :goto_6

    nop

    :goto_4
    iget p1, p1, Landroid/content/res/Configuration;->densityDpi:I

    goto :goto_1

    nop

    :goto_5
    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    goto :goto_4

    nop

    :goto_6
    return-void

    :goto_7
    if-ne p1, v0, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_miuixbasewidget_widget_internal_TabViewContainerView__onLayout',
        'method': '.method protected onLayout(ZIIII)V',
        'method_name': 'onLayout',
        'method_anchors': ['invoke-virtual {p0}, Landroid/widget/FrameLayout;->getChildCount()I', 'iget v3, p0, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->mVerticalPaddingTop:I', 'iget-boolean p2, p0, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->mLayoutCenter:Z', 'if-eqz p2, :cond_0', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingStart()I', 'iget p3, p0, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->mChildrenTotalWidth:I', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingStart()I', 'if-ge p3, p1, :cond_2'],
        'type': 'method_replace',
        'search': """.method protected onLayout(ZIIII)V
    .registers 12

    sub-int/2addr p4, p2

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getChildCount()I

    move-result p1

    iget v3, p0, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->mVerticalPaddingTop:I

    iget-boolean p2, p0, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->mLayoutCenter:Z

    if-eqz p2, :cond_0

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingStart()I

    move-result p2

    iget p3, p0, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->mChildrenTotalWidth:I

    sub-int/2addr p4, p3

    div-int/lit8 p4, p4, 0x2

    add-int/2addr p2, p4

    goto :goto_0

    :cond_0
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingStart()I

    move-result p2

    :goto_0
    const/4 p3, 0x0

    move v2, p2

    :goto_1
    if-ge p3, p1, :cond_2

    invoke-virtual {p0, p3}, Landroid/widget/FrameLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v1

    invoke-direct {p0, v1}, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->isViewGone(Landroid/view/View;)Z

    move-result p2

    if-nez p2, :cond_1

    invoke-virtual {v1}, Landroid/view/View;->getMeasuredWidth()I

    move-result p2

    add-int v4, v2, p2

    invoke-virtual {v1}, Landroid/view/View;->getMeasuredHeight()I

    move-result p2

    add-int v5, v3, p2

    move-object v0, p0

    invoke-static/range {v0 .. v5}, Lmiuix/internal/util/ViewUtils;->layoutChildView(Landroid/view/ViewGroup;Landroid/view/View;IIII)V

    iget p0, v0, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->mGapBetweenTabs:I

    add-int/2addr v4, p0

    move v2, v4

    goto :goto_2

    :cond_1
    move-object v0, p0

    :goto_2
    add-int/lit8 p3, p3, 0x1

    move-object p0, v0

    goto :goto_1

    :cond_2
    return-void
.end method""",
        'replacement': """.method protected onLayout(ZIIII)V
    .registers 12

    goto :goto_b

    nop

    :goto_0
    if-nez p2, :cond_0

    goto :goto_1f

    :cond_0
    goto :goto_11

    nop

    :goto_1
    iget-boolean p2, p0, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->mLayoutCenter:Z

    goto :goto_0

    nop

    :goto_2
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingStart()I

    move-result p2

    :goto_3
    goto :goto_1b

    nop

    :goto_4
    invoke-virtual {v1}, Landroid/view/View;->getMeasuredHeight()I

    move-result p2

    goto :goto_9

    nop

    :goto_5
    if-eqz p2, :cond_1

    goto :goto_1d

    :cond_1
    goto :goto_14

    nop

    :goto_6
    div-int/lit8 p4, p4, 0x2

    goto :goto_21

    nop

    :goto_7
    invoke-direct {p0, v1}, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->isViewGone(Landroid/view/View;)Z

    move-result p2

    goto :goto_5

    nop

    :goto_8
    add-int v4, v2, p2

    goto :goto_4

    nop

    :goto_9
    add-int v5, v3, p2

    goto :goto_e

    nop

    :goto_a
    invoke-static/range {v0 .. v5}, Lmiuix/internal/util/ViewUtils;->layoutChildView(Landroid/view/ViewGroup;Landroid/view/View;IIII)V

    goto :goto_15

    nop

    :goto_b
    sub-int/2addr p4, p2

    goto :goto_24

    nop

    :goto_c
    add-int/lit8 p3, p3, 0x1

    goto :goto_18

    nop

    :goto_d
    add-int/2addr v4, p0

    goto :goto_19

    nop

    :goto_e
    move-object v0, p0

    goto :goto_a

    nop

    :goto_f
    move-object v0, p0

    :goto_10
    goto :goto_c

    nop

    :goto_11
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingStart()I

    move-result p2

    goto :goto_17

    nop

    :goto_12
    move v2, p2

    :goto_13
    goto :goto_20

    nop

    :goto_14
    invoke-virtual {v1}, Landroid/view/View;->getMeasuredWidth()I

    move-result p2

    goto :goto_8

    nop

    :goto_15
    iget p0, v0, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->mGapBetweenTabs:I

    goto :goto_d

    nop

    :goto_16
    return-void

    :goto_17
    iget p3, p0, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->mChildrenTotalWidth:I

    goto :goto_25

    nop

    :goto_18
    move-object p0, v0

    goto :goto_22

    nop

    :goto_19
    move v2, v4

    goto :goto_1c

    nop

    :goto_1a
    iget v3, p0, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->mVerticalPaddingTop:I

    goto :goto_1

    nop

    :goto_1b
    const/4 p3, 0x0

    goto :goto_12

    nop

    :goto_1c
    goto :goto_10

    :goto_1d
    goto :goto_f

    nop

    :goto_1e
    goto :goto_3

    :goto_1f
    goto :goto_2

    nop

    :goto_20
    if-lt p3, p1, :cond_2

    goto :goto_23

    :cond_2
    goto :goto_26

    nop

    :goto_21
    add-int/2addr p2, p4

    goto :goto_1e

    nop

    :goto_22
    goto :goto_13

    :goto_23
    goto :goto_16

    nop

    :goto_24
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getChildCount()I

    move-result p1

    goto :goto_1a

    nop

    :goto_25
    sub-int/2addr p4, p3

    goto :goto_6

    nop

    :goto_26
    invoke-virtual {p0, p3}, Landroid/widget/FrameLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v1

    goto :goto_7

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_miuixbasewidget_widget_internal_TabViewContainerView__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['iput-boolean v0, p0, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->mLayoutCenter:Z', 'iput v0, p0, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->mChildrenTotalWidth:I', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->getChildCount()I', 'if-ge v0, v1, :cond_1', 'invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->getChildAt(I)Landroid/view/View;', 'invoke-direct {p0, v3}, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->isViewGone(Landroid/view/View;)Z', 'if-nez v3, :cond_0', 'if-gtz v2, :cond_2'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 7

    const/4 v0, 0x0

    iput-boolean v0, p0, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->mLayoutCenter:Z

    iput v0, p0, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->mChildrenTotalWidth:I

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getChildCount()I

    move-result v1

    move v2, v0

    :goto_0
    if-ge v0, v1, :cond_1

    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v3

    invoke-direct {p0, v3}, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->isViewGone(Landroid/view/View;)Z

    move-result v3

    if-nez v3, :cond_0

    add-int/lit8 v2, v2, 0x1

    :cond_0
    add-int/lit8 v0, v0, 0x1

    goto :goto_0

    :cond_1
    if-gtz v2, :cond_2

    invoke-super {p0, p1, p2}, Landroid/widget/FrameLayout;->onMeasure(II)V

    return-void

    :cond_2
    iget v0, p0, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->mLayoutMode:I

    const/4 v1, 0x2

    if-ne v0, v1, :cond_3

    invoke-direct {p0, p1, p2, v2}, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->measureByWrapMode(III)V

    return-void

    :cond_3
    if-nez v0, :cond_4

    goto :goto_1

    :cond_4
    const/4 v1, 0x1

    if-ne v0, v1, :cond_6

    invoke-direct {p0, p1, p2, v2}, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->measureByWideMode(III)Z

    move-result v0

    if-eqz v0, :cond_5

    :goto_1
    invoke-direct {p0, p1, p2, v2}, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->measureByCompatMode(III)V

    return-void

    :cond_5
    iput-boolean v1, p0, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->mLayoutCenter:Z

    return-void

    :cond_6
    new-instance p1, Ljava/lang/IllegalStateException;

    new-instance p2, Ljava/lang/StringBuilder;

    invoke-direct {p2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v0, "Unexpected layout mode: "

    invoke-virtual {p2, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget p0, p0, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->mLayoutMode:I

    invoke-virtual {p2, p0}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {p2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    invoke-direct {p1, p0}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    throw p1
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 7

    goto :goto_23

    nop

    :goto_0
    invoke-direct {p2}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_14

    nop

    :goto_1
    iput v0, p0, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->mChildrenTotalWidth:I

    goto :goto_1b

    nop

    :goto_2
    const/4 v1, 0x1

    goto :goto_20

    nop

    :goto_3
    invoke-direct {p0, v3}, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->isViewGone(Landroid/view/View;)Z

    move-result v3

    goto :goto_2d

    nop

    :goto_4
    return-void

    :goto_5
    goto :goto_18

    nop

    :goto_6
    invoke-super {p0, p1, p2}, Landroid/widget/FrameLayout;->onMeasure(II)V

    goto :goto_e

    nop

    :goto_7
    iget p0, p0, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->mLayoutMode:I

    goto :goto_17

    nop

    :goto_8
    move v2, v0

    :goto_9
    goto :goto_12

    nop

    :goto_a
    return-void

    :goto_b
    goto :goto_2c

    nop

    :goto_c
    invoke-virtual {p2, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_7

    nop

    :goto_d
    invoke-direct {p0, p1, p2, v2}, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->measureByWideMode(III)Z

    move-result v0

    goto :goto_1d

    nop

    :goto_e
    return-void

    :goto_f
    goto :goto_15

    nop

    :goto_10
    goto :goto_1e

    :goto_11
    goto :goto_2

    nop

    :goto_12
    if-lt v0, v1, :cond_0

    goto :goto_22

    :cond_0
    goto :goto_1f

    nop

    :goto_13
    iput-boolean v0, p0, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->mLayoutCenter:Z

    goto :goto_1

    nop

    :goto_14
    const-string v0, "Unexpected layout mode: "

    goto :goto_c

    nop

    :goto_15
    iget v0, p0, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->mLayoutMode:I

    goto :goto_1c

    nop

    :goto_16
    invoke-direct {p0, p1, p2, v2}, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->measureByCompatMode(III)V

    goto :goto_25

    nop

    :goto_17
    invoke-virtual {p2, p0}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_2a

    nop

    :goto_18
    new-instance p1, Ljava/lang/IllegalStateException;

    goto :goto_2b

    nop

    :goto_19
    throw p1

    :goto_1a
    invoke-direct {p1, p0}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    goto :goto_19

    nop

    :goto_1b
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getChildCount()I

    move-result v1

    goto :goto_8

    nop

    :goto_1c
    const/4 v1, 0x2

    goto :goto_30

    nop

    :goto_1d
    if-nez v0, :cond_1

    goto :goto_26

    :cond_1
    :goto_1e
    goto :goto_16

    nop

    :goto_1f
    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v3

    goto :goto_3

    nop

    :goto_20
    if-eq v0, v1, :cond_2

    goto :goto_5

    :cond_2
    goto :goto_d

    nop

    :goto_21
    goto :goto_9

    :goto_22
    goto :goto_24

    nop

    :goto_23
    const/4 v0, 0x0

    goto :goto_13

    nop

    :goto_24
    if-lez v2, :cond_3

    goto :goto_f

    :cond_3
    goto :goto_6

    nop

    :goto_25
    return-void

    :goto_26
    goto :goto_29

    nop

    :goto_27
    add-int/lit8 v2, v2, 0x1

    :goto_28
    goto :goto_2f

    nop

    :goto_29
    iput-boolean v1, p0, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->mLayoutCenter:Z

    goto :goto_4

    nop

    :goto_2a
    invoke-virtual {p2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    goto :goto_1a

    nop

    :goto_2b
    new-instance p2, Ljava/lang/StringBuilder;

    goto :goto_0

    nop

    :goto_2c
    if-eqz v0, :cond_4

    goto :goto_11

    :cond_4
    goto :goto_10

    nop

    :goto_2d
    if-eqz v3, :cond_5

    goto :goto_28

    :cond_5
    goto :goto_27

    nop

    :goto_2e
    invoke-direct {p0, p1, p2, v2}, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->measureByWrapMode(III)V

    goto :goto_a

    nop

    :goto_2f
    add-int/lit8 v0, v0, 0x1

    goto :goto_21

    nop

    :goto_30
    if-eq v0, v1, :cond_6

    goto :goto_b

    :cond_6
    goto :goto_2e

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
