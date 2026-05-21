TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/app/GroupButtonsPanel.smali'
CLASS_FALLBACK_NAMES = ['GroupButtonsPanel.smali']
CLASS_ANCHORS = ['.super Landroid/widget/FrameLayout;']

PATCHES = [
    {
        'id': 'miuix_appcompat_app_GroupButtonsPanel__onDetachedFromWindow',
        'method': '.method protected onDetachedFromWindow()V',
        'method_name': 'onDetachedFromWindow',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/FrameLayout;->onDetachedFromWindow()V', 'iget-object v0, p0, Lmiuix/appcompat/app/GroupButtonsPanel;->mResetPanelPaddingBottomRunnable:Ljava/lang/Runnable;', 'if-eqz v0, :cond_0', 'invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->removeCallbacks(Ljava/lang/Runnable;)Z', 'iput-object v0, p0, Lmiuix/appcompat/app/GroupButtonsPanel;->mResetPanelPaddingBottomRunnable:Ljava/lang/Runnable;', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onDetachedFromWindow()V
    .registers 2

    invoke-super {p0}, Landroid/widget/FrameLayout;->onDetachedFromWindow()V

    iget-object v0, p0, Lmiuix/appcompat/app/GroupButtonsPanel;->mResetPanelPaddingBottomRunnable:Ljava/lang/Runnable;

    if-eqz v0, :cond_0

    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->removeCallbacks(Ljava/lang/Runnable;)Z

    const/4 v0, 0x0

    iput-object v0, p0, Lmiuix/appcompat/app/GroupButtonsPanel;->mResetPanelPaddingBottomRunnable:Ljava/lang/Runnable;

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onDetachedFromWindow()V
    .registers 2

    goto :goto_6

    nop

    :goto_0
    if-nez v0, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_1

    nop

    :goto_1
    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->removeCallbacks(Ljava/lang/Runnable;)Z

    goto :goto_2

    nop

    :goto_2
    const/4 v0, 0x0

    goto :goto_4

    nop

    :goto_3
    iget-object v0, p0, Lmiuix/appcompat/app/GroupButtonsPanel;->mResetPanelPaddingBottomRunnable:Ljava/lang/Runnable;

    goto :goto_0

    nop

    :goto_4
    iput-object v0, p0, Lmiuix/appcompat/app/GroupButtonsPanel;->mResetPanelPaddingBottomRunnable:Ljava/lang/Runnable;

    :goto_5
    goto :goto_7

    nop

    :goto_6
    invoke-super {p0}, Landroid/widget/FrameLayout;->onDetachedFromWindow()V

    goto :goto_3

    nop

    :goto_7
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_GroupButtonsPanel__onFinishInflate',
        'method': '.method protected onFinishInflate()V',
        'method_name': 'onFinishInflate',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/FrameLayout;->onFinishInflate()V', 'invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->getChildAt(I)Landroid/view/View;', 'check-cast v0, Landroid/widget/LinearLayout;', 'iput-object v0, p0, Lmiuix/appcompat/app/GroupButtonsPanel;->mContentView:Landroid/widget/LinearLayout;', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onFinishInflate()V
    .registers 2

    invoke-super {p0}, Landroid/widget/FrameLayout;->onFinishInflate()V

    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/LinearLayout;

    iput-object v0, p0, Lmiuix/appcompat/app/GroupButtonsPanel;->mContentView:Landroid/widget/LinearLayout;

    return-void
.end method""",
        'replacement': """.method protected onFinishInflate()V
    .registers 2

    goto :goto_4

    nop

    :goto_0
    iput-object v0, p0, Lmiuix/appcompat/app/GroupButtonsPanel;->mContentView:Landroid/widget/LinearLayout;

    goto :goto_5

    nop

    :goto_1
    check-cast v0, Landroid/widget/LinearLayout;

    goto :goto_0

    nop

    :goto_2
    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v0

    goto :goto_1

    nop

    :goto_3
    const/4 v0, 0x0

    goto :goto_2

    nop

    :goto_4
    invoke-super {p0}, Landroid/widget/FrameLayout;->onFinishInflate()V

    goto :goto_3

    nop

    :goto_5
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_GroupButtonsPanel__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/app/GroupButtonsPanel;->mContentView:Landroid/widget/LinearLayout;', 'invoke-virtual {v0}, Landroid/widget/LinearLayout;->getOrientation()I', 'if-ne v0, v1, :cond_0', 'invoke-static {p1}, Landroid/view/View$MeasureSpec;->getSize(I)I', 'iget v3, p0, Lmiuix/appcompat/app/GroupButtonsPanel;->mOriginPaddingLeft:I', 'iget v3, p0, Lmiuix/appcompat/app/GroupButtonsPanel;->mOriginPaddingRight:I', 'iget v3, p0, Lmiuix/appcompat/app/GroupButtonsPanel;->mButtonGroupMaxWidth:I', 'invoke-static {v3, v2}, Ljava/lang/Math;->min(II)I'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 8

    iget-object v0, p0, Lmiuix/appcompat/app/GroupButtonsPanel;->mContentView:Landroid/widget/LinearLayout;

    invoke-virtual {v0}, Landroid/widget/LinearLayout;->getOrientation()I

    move-result v0

    const/4 v1, 0x1

    if-ne v0, v1, :cond_0

    move v0, v1

    goto :goto_0

    :cond_0
    const/4 v0, 0x0

    :goto_0
    invoke-static {p1}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v2

    iget v3, p0, Lmiuix/appcompat/app/GroupButtonsPanel;->mOriginPaddingLeft:I

    sub-int/2addr v2, v3

    iget v3, p0, Lmiuix/appcompat/app/GroupButtonsPanel;->mOriginPaddingRight:I

    sub-int/2addr v2, v3

    iget v3, p0, Lmiuix/appcompat/app/GroupButtonsPanel;->mButtonGroupMaxWidth:I

    invoke-static {v3, v2}, Ljava/lang/Math;->min(II)I

    move-result v3

    iget v4, p0, Lmiuix/appcompat/app/GroupButtonsPanel;->mButtonGroupMaxWidth:I

    if-ge v4, v2, :cond_1

    if-nez v0, :cond_1

    sub-int v4, v2, v4

    div-int/lit8 v4, v4, 0x2

    iput v4, p0, Lmiuix/appcompat/app/GroupButtonsPanel;->mExtraPadding:I

    :cond_1
    if-eqz v0, :cond_2

    invoke-direct {p0, v3}, Lmiuix/appcompat/app/GroupButtonsPanel;->resizeButtonTextSize(I)V

    goto :goto_1

    :cond_2
    invoke-virtual {p0}, Lmiuix/appcompat/app/GroupButtonsPanel;->getContentVisibleChildCount()I

    move-result v0

    if-lt v0, v1, :cond_3

    iget v1, p0, Lmiuix/appcompat/app/GroupButtonsPanel;->mButtonGroupDividerSize:I

    add-int/lit8 v4, v0, -0x1

    mul-int/2addr v1, v4

    sub-int/2addr v3, v1

    div-int/2addr v3, v0

    invoke-direct {p0, v3}, Lmiuix/appcompat/app/GroupButtonsPanel;->resizeButtonTextSize(I)V

    :cond_3
    :goto_1
    invoke-super {p0, p1, p2}, Landroid/widget/FrameLayout;->onMeasure(II)V

    iget v0, p0, Lmiuix/appcompat/app/GroupButtonsPanel;->mExtraPadding:I

    if-lez v0, :cond_4

    mul-int/lit8 v0, v0, 0x2

    sub-int/2addr v2, v0

    iget v0, p0, Lmiuix/appcompat/app/GroupButtonsPanel;->mOriginPaddingLeft:I

    add-int/2addr v2, v0

    iget v0, p0, Lmiuix/appcompat/app/GroupButtonsPanel;->mOriginPaddingRight:I

    add-int/2addr v2, v0

    invoke-static {p1}, Landroid/view/View$MeasureSpec;->getMode(I)I

    move-result p1

    invoke-static {v2, p1}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p1

    iget-object v0, p0, Lmiuix/appcompat/app/GroupButtonsPanel;->mContentView:Landroid/widget/LinearLayout;

    invoke-virtual {p0, v0, p1, p2}, Landroid/widget/FrameLayout;->measureChild(Landroid/view/View;II)V

    :cond_4
    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 8

    goto :goto_1e

    nop

    :goto_0
    if-nez v0, :cond_0

    goto :goto_2b

    :cond_0
    goto :goto_2f

    nop

    :goto_1
    sub-int v4, v2, v4

    goto :goto_12

    nop

    :goto_2
    iget v0, p0, Lmiuix/appcompat/app/GroupButtonsPanel;->mOriginPaddingLeft:I

    goto :goto_28

    nop

    :goto_3
    div-int/2addr v3, v0

    goto :goto_e

    nop

    :goto_4
    invoke-virtual {p0, v0, p1, p2}, Landroid/widget/FrameLayout;->measureChild(Landroid/view/View;II)V

    :goto_5
    goto :goto_27

    nop

    :goto_6
    sub-int/2addr v2, v3

    goto :goto_2d

    nop

    :goto_7
    invoke-virtual {v0}, Landroid/widget/LinearLayout;->getOrientation()I

    move-result v0

    goto :goto_20

    nop

    :goto_8
    sub-int/2addr v2, v3

    goto :goto_23

    nop

    :goto_9
    mul-int/lit8 v0, v0, 0x2

    goto :goto_b

    nop

    :goto_a
    iget v4, p0, Lmiuix/appcompat/app/GroupButtonsPanel;->mButtonGroupMaxWidth:I

    goto :goto_14

    nop

    :goto_b
    sub-int/2addr v2, v0

    goto :goto_2

    nop

    :goto_c
    sub-int/2addr v3, v1

    goto :goto_3

    nop

    :goto_d
    add-int/2addr v2, v0

    goto :goto_30

    nop

    :goto_e
    invoke-direct {p0, v3}, Lmiuix/appcompat/app/GroupButtonsPanel;->resizeButtonTextSize(I)V

    :goto_f
    goto :goto_2c

    nop

    :goto_10
    if-ge v0, v1, :cond_1

    goto :goto_f

    :cond_1
    goto :goto_18

    nop

    :goto_11
    if-eqz v0, :cond_2

    goto :goto_1d

    :cond_2
    goto :goto_1

    nop

    :goto_12
    div-int/lit8 v4, v4, 0x2

    goto :goto_1c

    nop

    :goto_13
    invoke-static {v2, p1}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p1

    goto :goto_1a

    nop

    :goto_14
    if-lt v4, v2, :cond_3

    goto :goto_1d

    :cond_3
    goto :goto_11

    nop

    :goto_15
    iget v0, p0, Lmiuix/appcompat/app/GroupButtonsPanel;->mExtraPadding:I

    goto :goto_1b

    nop

    :goto_16
    add-int/lit8 v4, v0, -0x1

    goto :goto_24

    nop

    :goto_17
    move v0, v1

    goto :goto_21

    nop

    :goto_18
    iget v1, p0, Lmiuix/appcompat/app/GroupButtonsPanel;->mButtonGroupDividerSize:I

    goto :goto_16

    nop

    :goto_19
    invoke-static {p1}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v2

    goto :goto_2e

    nop

    :goto_1a
    iget-object v0, p0, Lmiuix/appcompat/app/GroupButtonsPanel;->mContentView:Landroid/widget/LinearLayout;

    goto :goto_4

    nop

    :goto_1b
    if-gtz v0, :cond_4

    goto :goto_5

    :cond_4
    goto :goto_9

    nop

    :goto_1c
    iput v4, p0, Lmiuix/appcompat/app/GroupButtonsPanel;->mExtraPadding:I

    :goto_1d
    goto :goto_0

    nop

    :goto_1e
    iget-object v0, p0, Lmiuix/appcompat/app/GroupButtonsPanel;->mContentView:Landroid/widget/LinearLayout;

    goto :goto_7

    nop

    :goto_1f
    invoke-virtual {p0}, Lmiuix/appcompat/app/GroupButtonsPanel;->getContentVisibleChildCount()I

    move-result v0

    goto :goto_10

    nop

    :goto_20
    const/4 v1, 0x1

    goto :goto_26

    nop

    :goto_21
    goto :goto_32

    :goto_22
    goto :goto_31

    nop

    :goto_23
    iget v3, p0, Lmiuix/appcompat/app/GroupButtonsPanel;->mOriginPaddingRight:I

    goto :goto_6

    nop

    :goto_24
    mul-int/2addr v1, v4

    goto :goto_c

    nop

    :goto_25
    iget v0, p0, Lmiuix/appcompat/app/GroupButtonsPanel;->mOriginPaddingRight:I

    goto :goto_d

    nop

    :goto_26
    if-eq v0, v1, :cond_5

    goto :goto_22

    :cond_5
    goto :goto_17

    nop

    :goto_27
    return-void

    :goto_28
    add-int/2addr v2, v0

    goto :goto_25

    nop

    :goto_29
    invoke-static {v3, v2}, Ljava/lang/Math;->min(II)I

    move-result v3

    goto :goto_a

    nop

    :goto_2a
    goto :goto_f

    :goto_2b
    goto :goto_1f

    nop

    :goto_2c
    invoke-super {p0, p1, p2}, Landroid/widget/FrameLayout;->onMeasure(II)V

    goto :goto_15

    nop

    :goto_2d
    iget v3, p0, Lmiuix/appcompat/app/GroupButtonsPanel;->mButtonGroupMaxWidth:I

    goto :goto_29

    nop

    :goto_2e
    iget v3, p0, Lmiuix/appcompat/app/GroupButtonsPanel;->mOriginPaddingLeft:I

    goto :goto_8

    nop

    :goto_2f
    invoke-direct {p0, v3}, Lmiuix/appcompat/app/GroupButtonsPanel;->resizeButtonTextSize(I)V

    goto :goto_2a

    nop

    :goto_30
    invoke-static {p1}, Landroid/view/View$MeasureSpec;->getMode(I)I

    move-result p1

    goto :goto_13

    nop

    :goto_31
    const/4 v0, 0x0

    :goto_32
    goto :goto_19

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
