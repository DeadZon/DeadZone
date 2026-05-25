TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/view/menu/action/PhoneActionMenuView.smali'
CLASS_FALLBACK_NAMES = ['PhoneActionMenuView.smali']
CLASS_ANCHORS = ['.super Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;', '.field private static final ATTRS:[I']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_view_menu_action_PhoneActionMenuView__getChildDrawingOrder',
        'method': '.method protected getChildDrawingOrder(II)I',
        'method_name': 'getChildDrawingOrder',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mOverflowMenuView:Landroid/view/View;', 'invoke-virtual {p0, v0}, Landroid/widget/LinearLayout;->indexOfChild(Landroid/view/View;)I', 'iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mBackgroundView:Landroid/view/View;', 'invoke-virtual {p0, v1}, Landroid/widget/LinearLayout;->indexOfChild(Landroid/view/View;)I', 'if-nez p2, :cond_1', 'if-eq v0, v2, :cond_0', 'return v0', 'if-eq v1, v2, :cond_2'],
        'type': 'method_replace',
        'search': """.method protected getChildDrawingOrder(II)I
    .registers 7

    iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mOverflowMenuView:Landroid/view/View;

    invoke-virtual {p0, v0}, Landroid/widget/LinearLayout;->indexOfChild(Landroid/view/View;)I

    move-result v0

    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mBackgroundView:Landroid/view/View;

    invoke-virtual {p0, v1}, Landroid/widget/LinearLayout;->indexOfChild(Landroid/view/View;)I

    move-result v1

    const/4 v2, -0x1

    if-nez p2, :cond_1

    if-eq v0, v2, :cond_0

    return v0

    :cond_0
    if-eq v1, v2, :cond_2

    goto :goto_0

    :cond_1
    const/4 v3, 0x1

    if-ne p2, v3, :cond_2

    if-eq v0, v2, :cond_2

    if-eq v1, v2, :cond_2

    :goto_0
    return v1

    :cond_2
    const/4 v2, 0x0

    :goto_1
    if-ge v2, p1, :cond_7

    if-eq v2, v0, :cond_6

    if-ne v2, v1, :cond_3

    goto :goto_3

    :cond_3
    if-ge v2, v0, :cond_4

    add-int/lit8 v3, v2, 0x1

    goto :goto_2

    :cond_4
    move v3, v2

    :goto_2
    if-ge v2, v1, :cond_5

    add-int/lit8 v3, v3, 0x1

    :cond_5
    if-ne v3, p2, :cond_6

    return v2

    :cond_6
    :goto_3
    add-int/lit8 v2, v2, 0x1

    goto :goto_1

    :cond_7
    invoke-super {p0, p1, p2}, Landroid/widget/LinearLayout;->getChildDrawingOrder(II)I

    move-result p0

    return p0
.end method""",
        'replacement': """.method protected getChildDrawingOrder(II)I
    .registers 7

    goto :goto_15

    nop

    :goto_0
    return p0

    :goto_1
    invoke-super {p0, p1, p2}, Landroid/widget/LinearLayout;->getChildDrawingOrder(II)I

    move-result p0

    goto :goto_0

    nop

    :goto_2
    if-eq p2, v3, :cond_0

    goto :goto_25

    :cond_0
    goto :goto_26

    nop

    :goto_3
    goto :goto_12

    :goto_4
    goto :goto_7

    nop

    :goto_5
    return v2

    :goto_6
    goto :goto_18

    nop

    :goto_7
    const/4 v3, 0x1

    goto :goto_2

    nop

    :goto_8
    goto :goto_6

    :goto_9
    goto :goto_2a

    nop

    :goto_a
    goto :goto_f

    :goto_b
    goto :goto_1

    nop

    :goto_c
    if-eq v3, p2, :cond_1

    goto :goto_6

    :cond_1
    goto :goto_5

    nop

    :goto_d
    const/4 v2, -0x1

    goto :goto_17

    nop

    :goto_e
    const/4 v2, 0x0

    :goto_f
    goto :goto_1d

    nop

    :goto_10
    if-eq v2, v1, :cond_2

    goto :goto_9

    :cond_2
    goto :goto_8

    nop

    :goto_11
    if-ne v1, v2, :cond_3

    goto :goto_25

    :cond_3
    :goto_12
    goto :goto_24

    nop

    :goto_13
    goto :goto_20

    :goto_14
    goto :goto_1f

    nop

    :goto_15
    iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mOverflowMenuView:Landroid/view/View;

    goto :goto_29

    nop

    :goto_16
    if-lt v2, v1, :cond_4

    goto :goto_1a

    :cond_4
    goto :goto_19

    nop

    :goto_17
    if-eqz p2, :cond_5

    goto :goto_4

    :cond_5
    goto :goto_1c

    nop

    :goto_18
    add-int/lit8 v2, v2, 0x1

    goto :goto_a

    nop

    :goto_19
    add-int/lit8 v3, v3, 0x1

    :goto_1a
    goto :goto_c

    nop

    :goto_1b
    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mBackgroundView:Landroid/view/View;

    goto :goto_22

    nop

    :goto_1c
    if-ne v0, v2, :cond_6

    goto :goto_28

    :cond_6
    goto :goto_27

    nop

    :goto_1d
    if-lt v2, p1, :cond_7

    goto :goto_b

    :cond_7
    goto :goto_21

    nop

    :goto_1e
    if-ne v1, v2, :cond_8

    goto :goto_25

    :cond_8
    goto :goto_3

    nop

    :goto_1f
    move v3, v2

    :goto_20
    goto :goto_16

    nop

    :goto_21
    if-ne v2, v0, :cond_9

    goto :goto_6

    :cond_9
    goto :goto_10

    nop

    :goto_22
    invoke-virtual {p0, v1}, Landroid/widget/LinearLayout;->indexOfChild(Landroid/view/View;)I

    move-result v1

    goto :goto_d

    nop

    :goto_23
    add-int/lit8 v3, v2, 0x1

    goto :goto_13

    nop

    :goto_24
    return v1

    :goto_25
    goto :goto_e

    nop

    :goto_26
    if-ne v0, v2, :cond_a

    goto :goto_25

    :cond_a
    goto :goto_11

    nop

    :goto_27
    return v0

    :goto_28
    goto :goto_1e

    nop

    :goto_29
    invoke-virtual {p0, v0}, Landroid/widget/LinearLayout;->indexOfChild(Landroid/view/View;)I

    move-result v0

    goto :goto_1b

    nop

    :goto_2a
    if-lt v2, v0, :cond_b

    goto :goto_14

    :cond_b
    goto :goto_23

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_action_PhoneActionMenuView__onLayout',
        'method': '.method protected onLayout(ZIIII)V',
        'method_name': 'onLayout',
        'method_anchors': ['iget-object p1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mOverflowMenuView:Landroid/view/View;', 'if-eqz p1, :cond_0', 'invoke-virtual {p1}, Landroid/view/View;->getMeasuredHeight()I', 'iget-object p1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mOverflowMenuView:Landroid/view/View;', 'invoke-static/range {p0 .. p5}, Lmiuix/internal/util/ViewUtils;->layoutChildView(Landroid/view/ViewGroup;Landroid/view/View;IIII)V', 'iget-object p1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mBackgroundPadding:Landroid/graphics/Rect;', 'iget p1, p1, Landroid/graphics/Rect;->top:I', 'iget-object p1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mBackgroundView:Landroid/view/View;'],
        'type': 'method_replace',
        'search': """.method protected onLayout(ZIIII)V
    .registers 12

    sub-int/2addr p4, p2

    sub-int v5, p5, p3

    iget-object p1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mOverflowMenuView:Landroid/view/View;

    const/4 v0, 0x0

    if-eqz p1, :cond_0

    invoke-virtual {p1}, Landroid/view/View;->getMeasuredHeight()I

    move-result p5

    iget-object p1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mOverflowMenuView:Landroid/view/View;

    const/4 p2, 0x0

    const/4 p3, 0x0

    invoke-static/range {p0 .. p5}, Lmiuix/internal/util/ViewUtils;->layoutChildView(Landroid/view/ViewGroup;Landroid/view/View;IIII)V

    iget-object p1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mBackgroundPadding:Landroid/graphics/Rect;

    iget p1, p1, Landroid/graphics/Rect;->top:I

    sub-int/2addr p5, p1

    move p3, p5

    goto :goto_0

    :cond_0
    move p3, v0

    :goto_0
    iget-object p1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mBackgroundView:Landroid/view/View;

    const/4 p2, 0x0

    move p5, v5

    invoke-static/range {p0 .. p5}, Lmiuix/internal/util/ViewUtils;->layoutChildView(Landroid/view/ViewGroup;Landroid/view/View;IIII)V

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getChildCount()I

    move-result p1

    iget p2, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mMenuItemWidth:I

    sub-int/2addr p4, p2

    shr-int/lit8 p2, p4, 0x1

    move v2, p2

    move p2, v0

    :goto_1
    if-ge p2, p1, :cond_2

    invoke-virtual {p0, p2}, Landroid/widget/LinearLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v1

    invoke-direct {p0, v1}, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->isNotActionMenuItemChild(Landroid/view/View;)Z

    move-result p4

    if-eqz p4, :cond_1

    goto :goto_2

    :cond_1
    invoke-virtual {v1}, Landroid/view/View;->getMeasuredWidth()I

    move-result p4

    add-int v4, v2, p4

    move-object v0, p0

    move v3, p3

    move v5, p5

    invoke-static/range {v0 .. v5}, Lmiuix/internal/util/ViewUtils;->layoutChildView(Landroid/view/ViewGroup;Landroid/view/View;IIII)V

    invoke-virtual {v1}, Landroid/view/View;->getMeasuredWidth()I

    move-result p4

    iget v0, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mMenuItemGap:I

    add-int/2addr p4, v0

    add-int/2addr v2, p4

    :goto_2
    add-int/lit8 p2, p2, 0x1

    goto :goto_1

    :cond_2
    return-void
.end method""",
        'replacement': """.method protected onLayout(ZIIII)V
    .registers 12

    goto :goto_1c

    nop

    :goto_0
    const/4 p2, 0x0

    goto :goto_16

    nop

    :goto_1
    move-object v0, p0

    goto :goto_1b

    nop

    :goto_2
    add-int v4, v2, p4

    goto :goto_1

    nop

    :goto_3
    if-lt p2, p1, :cond_0

    goto :goto_a

    :cond_0
    goto :goto_4

    nop

    :goto_4
    invoke-virtual {p0, p2}, Landroid/widget/LinearLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v1

    goto :goto_b

    nop

    :goto_5
    goto :goto_2e

    :goto_6
    goto :goto_14

    nop

    :goto_7
    sub-int/2addr p4, p2

    goto :goto_28

    nop

    :goto_8
    iget-object p1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mOverflowMenuView:Landroid/view/View;

    goto :goto_0

    nop

    :goto_9
    goto :goto_f

    :goto_a
    goto :goto_15

    nop

    :goto_b
    invoke-direct {p0, v1}, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->isNotActionMenuItemChild(Landroid/view/View;)Z

    move-result p4

    goto :goto_c

    nop

    :goto_c
    if-nez p4, :cond_1

    goto :goto_6

    :cond_1
    goto :goto_5

    nop

    :goto_d
    iget v0, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mMenuItemGap:I

    goto :goto_22

    nop

    :goto_e
    move p2, v0

    :goto_f
    goto :goto_3

    nop

    :goto_10
    add-int/lit8 p2, p2, 0x1

    goto :goto_9

    nop

    :goto_11
    if-nez p1, :cond_2

    goto :goto_2b

    :cond_2
    goto :goto_26

    nop

    :goto_12
    iget p1, p1, Landroid/graphics/Rect;->top:I

    goto :goto_18

    nop

    :goto_13
    move v2, p2

    goto :goto_e

    nop

    :goto_14
    invoke-virtual {v1}, Landroid/view/View;->getMeasuredWidth()I

    move-result p4

    goto :goto_2

    nop

    :goto_15
    return-void

    :goto_16
    const/4 p3, 0x0

    goto :goto_21

    nop

    :goto_17
    invoke-static/range {p0 .. p5}, Lmiuix/internal/util/ViewUtils;->layoutChildView(Landroid/view/ViewGroup;Landroid/view/View;IIII)V

    goto :goto_29

    nop

    :goto_18
    sub-int/2addr p5, p1

    goto :goto_31

    nop

    :goto_19
    move p3, v0

    :goto_1a
    goto :goto_23

    nop

    :goto_1b
    move v3, p3

    goto :goto_20

    nop

    :goto_1c
    sub-int/2addr p4, p2

    goto :goto_25

    nop

    :goto_1d
    iget-object p1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mBackgroundPadding:Landroid/graphics/Rect;

    goto :goto_12

    nop

    :goto_1e
    iget p2, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mMenuItemWidth:I

    goto :goto_7

    nop

    :goto_1f
    const/4 p2, 0x0

    goto :goto_2c

    nop

    :goto_20
    move v5, p5

    goto :goto_24

    nop

    :goto_21
    invoke-static/range {p0 .. p5}, Lmiuix/internal/util/ViewUtils;->layoutChildView(Landroid/view/ViewGroup;Landroid/view/View;IIII)V

    goto :goto_1d

    nop

    :goto_22
    add-int/2addr p4, v0

    goto :goto_2d

    nop

    :goto_23
    iget-object p1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mBackgroundView:Landroid/view/View;

    goto :goto_1f

    nop

    :goto_24
    invoke-static/range {v0 .. v5}, Lmiuix/internal/util/ViewUtils;->layoutChildView(Landroid/view/ViewGroup;Landroid/view/View;IIII)V

    goto :goto_30

    nop

    :goto_25
    sub-int v5, p5, p3

    goto :goto_27

    nop

    :goto_26
    invoke-virtual {p1}, Landroid/view/View;->getMeasuredHeight()I

    move-result p5

    goto :goto_8

    nop

    :goto_27
    iget-object p1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mOverflowMenuView:Landroid/view/View;

    goto :goto_2f

    nop

    :goto_28
    shr-int/lit8 p2, p4, 0x1

    goto :goto_13

    nop

    :goto_29
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getChildCount()I

    move-result p1

    goto :goto_1e

    nop

    :goto_2a
    goto :goto_1a

    :goto_2b
    goto :goto_19

    nop

    :goto_2c
    move p5, v5

    goto :goto_17

    nop

    :goto_2d
    add-int/2addr v2, p4

    :goto_2e
    goto :goto_10

    nop

    :goto_2f
    const/4 v0, 0x0

    goto :goto_11

    nop

    :goto_30
    invoke-virtual {v1}, Landroid/view/View;->getMeasuredWidth()I

    move-result p4

    goto :goto_d

    nop

    :goto_31
    move p3, p5

    goto :goto_2a

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_action_PhoneActionMenuView__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['invoke-virtual {p0}, Landroid/widget/LinearLayout;->getChildCount()I', 'invoke-direct {p0}, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->getActionMenuItemCount()I', 'iput v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mActionCount:I', 'if-eqz v6, :cond_8', 'if-nez v1, :cond_0', 'invoke-static {p1}, Landroid/view/View$MeasureSpec;->getSize(I)I', 'iget v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mActionCount:I', 'iget v2, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mMaxActionButtonWidth:I'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 15

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getChildCount()I

    move-result v6

    invoke-direct {p0}, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->getActionMenuItemCount()I

    move-result v1

    iput v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mActionCount:I

    const/4 v7, 0x0

    if-eqz v6, :cond_8

    if-nez v1, :cond_0

    goto :goto_4

    :cond_0
    invoke-static {p1}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v8

    iget v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mActionCount:I

    div-int v1, v8, v1

    iget v2, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mMaxActionButtonWidth:I

    invoke-static {v1, v2}, Ljava/lang/Math;->min(II)I

    move-result v1

    iput v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mMaxActionButtonWidth:I

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getContext()Landroid/content/Context;

    move-result-object v1

    invoke-direct {p0, v1, v8}, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->updateItemGapAdaptByCurrentWidth(Landroid/content/Context;I)V

    iget v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mMaxActionButtonWidth:I

    const/high16 v2, -0x80000000

    invoke-static {v1, v2}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v2

    move v9, v7

    move v10, v9

    move v11, v10

    :goto_0
    if-ge v9, v6, :cond_2

    invoke-virtual {p0, v9}, Landroid/widget/LinearLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v1

    invoke-direct {p0, v1}, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->isNotActionMenuItemChild(Landroid/view/View;)Z

    move-result v3

    if-eqz v3, :cond_1

    goto :goto_1

    :cond_1
    const/4 v3, 0x0

    const/4 v5, 0x0

    move-object v0, p0

    move v4, p2

    invoke-virtual/range {v0 .. v5}, Landroid/widget/LinearLayout;->measureChildWithMargins(Landroid/view/View;IIII)V

    invoke-virtual {v1}, Landroid/view/View;->getMeasuredWidth()I

    move-result v3

    iget v4, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mMaxActionButtonWidth:I

    invoke-static {v3, v4}, Ljava/lang/Math;->min(II)I

    move-result v3

    add-int/2addr v10, v3

    invoke-virtual {v1}, Landroid/view/View;->getMeasuredHeight()I

    move-result v1

    invoke-static {v11, v1}, Ljava/lang/Math;->max(II)I

    move-result v11

    :goto_1
    add-int/lit8 v9, v9, 0x1

    goto :goto_0

    :cond_2
    iget v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mMenuItemGap:I

    iget v2, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mActionCount:I

    add-int/lit8 v3, v2, -0x1

    mul-int/2addr v1, v3

    add-int/2addr v1, v10

    if-le v1, v8, :cond_3

    iput v7, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mMenuItemGap:I

    :cond_3
    iget v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mMenuItemGap:I

    add-int/lit8 v2, v2, -0x1

    mul-int/2addr v1, v2

    add-int/2addr v10, v1

    iput v10, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mMenuItemWidth:I

    iput v11, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mMenuItemHeight:I

    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mOverflowMenuView:Landroid/view/View;

    if-eqz v1, :cond_5

    invoke-virtual {v1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v1

    check-cast v1, Landroid/view/ViewGroup$MarginLayoutParams;

    iget-object v2, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mContext:Landroid/content/Context;

    invoke-static {v2}, Lmiuix/core/util/MiuixUIUtils;->getStatusBarHeight(Landroid/content/Context;)I

    move-result v2

    iput v2, v1, Landroid/view/ViewGroup$MarginLayoutParams;->topMargin:I

    iget v2, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mMenuItemHeight:I

    iput v2, v1, Landroid/view/ViewGroup$MarginLayoutParams;->bottomMargin:I

    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mOverflowMenuView:Landroid/view/View;

    const/4 v3, 0x0

    const/4 v5, 0x0

    move-object v0, p0

    move v2, p1

    move v4, p2

    invoke-virtual/range {v0 .. v5}, Landroid/widget/LinearLayout;->measureChildWithMargins(Landroid/view/View;IIII)V

    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mOverflowMenuView:Landroid/view/View;

    invoke-virtual {v1}, Landroid/view/View;->getMeasuredWidth()I

    move-result v1

    invoke-static {v10, v1}, Ljava/lang/Math;->max(II)I

    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mOverflowMenuView:Landroid/view/View;

    invoke-virtual {v1}, Landroid/view/View;->getMeasuredHeight()I

    move-result v1

    add-int/2addr v11, v1

    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mOverflowMenuState:Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView$OverflowMenuState;

    sget-object v2, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView$OverflowMenuState;->Expanded:Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView$OverflowMenuState;

    if-ne v1, v2, :cond_4

    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mOverflowMenuView:Landroid/view/View;

    const/4 v2, 0x0

    invoke-virtual {v1, v2}, Landroid/view/View;->setTranslationY(F)V

    goto :goto_2

    :cond_4
    sget-object v2, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView$OverflowMenuState;->Collapsed:Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView$OverflowMenuState;

    if-ne v1, v2, :cond_5

    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mOverflowMenuView:Landroid/view/View;

    int-to-float v2, v11

    invoke-virtual {v1, v2}, Landroid/view/View;->setTranslationY(F)V

    :cond_5
    :goto_2
    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mOverflowMenuView:Landroid/view/View;

    if-nez v1, :cond_6

    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mBackgroundPadding:Landroid/graphics/Rect;

    iget v1, v1, Landroid/graphics/Rect;->top:I

    add-int/2addr v11, v1

    :cond_6
    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mBackgroundView:Landroid/view/View;

    iget-object v2, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mOverflowMenuState:Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView$OverflowMenuState;

    sget-object v3, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView$OverflowMenuState;->Collapsed:Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView$OverflowMenuState;

    if-ne v2, v3, :cond_7

    iget-object v2, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mCollapseBackground:Landroid/graphics/drawable/Drawable;

    goto :goto_3

    :cond_7
    iget-object v2, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mExpandBackground:Landroid/graphics/drawable/Drawable;

    :goto_3
    invoke-virtual {v1, v2}, Landroid/view/View;->setBackground(Landroid/graphics/drawable/Drawable;)V

    invoke-virtual {p0, v8, v11}, Landroid/widget/LinearLayout;->setMeasuredDimension(II)V

    return-void

    :cond_8
    :goto_4
    iput v7, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mMenuItemHeight:I

    invoke-virtual {p0, v7, v7}, Landroid/widget/LinearLayout;->setMeasuredDimension(II)V

    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 15

    goto :goto_49

    nop

    :goto_0
    if-eq v1, v2, :cond_0

    goto :goto_48

    :cond_0
    goto :goto_65

    nop

    :goto_1
    mul-int/2addr v1, v3

    goto :goto_1a

    nop

    :goto_2
    invoke-virtual {v1}, Landroid/view/View;->getMeasuredWidth()I

    move-result v1

    goto :goto_32

    nop

    :goto_3
    invoke-virtual {v1}, Landroid/view/View;->getMeasuredWidth()I

    move-result v3

    goto :goto_5

    nop

    :goto_4
    if-lt v9, v6, :cond_1

    goto :goto_68

    :cond_1
    goto :goto_58

    nop

    :goto_5
    iget v4, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mMaxActionButtonWidth:I

    goto :goto_2f

    nop

    :goto_6
    invoke-virtual {v1}, Landroid/view/View;->getMeasuredHeight()I

    move-result v1

    goto :goto_7

    nop

    :goto_7
    invoke-static {v11, v1}, Ljava/lang/Math;->max(II)I

    move-result v11

    :goto_8
    goto :goto_5c

    nop

    :goto_9
    goto :goto_8

    :goto_a
    goto :goto_b

    nop

    :goto_b
    const/4 v3, 0x0

    goto :goto_43

    nop

    :goto_c
    add-int/lit8 v3, v2, -0x1

    goto :goto_1

    nop

    :goto_d
    const/4 v5, 0x0

    goto :goto_44

    nop

    :goto_e
    const/high16 v2, -0x80000000

    goto :goto_46

    nop

    :goto_f
    invoke-static {p1}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v8

    goto :goto_1b

    nop

    :goto_10
    iget-object v2, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mCollapseBackground:Landroid/graphics/drawable/Drawable;

    goto :goto_22

    nop

    :goto_11
    return-void

    :goto_12
    goto :goto_53

    nop

    :goto_13
    sget-object v3, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView$OverflowMenuState;->Collapsed:Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView$OverflowMenuState;

    goto :goto_40

    nop

    :goto_14
    iput v11, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mMenuItemHeight:I

    goto :goto_72

    nop

    :goto_15
    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mOverflowMenuState:Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView$OverflowMenuState;

    goto :goto_39

    nop

    :goto_16
    iget-object v2, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mContext:Landroid/content/Context;

    goto :goto_38

    nop

    :goto_17
    return-void

    :goto_18
    add-int/2addr v10, v1

    goto :goto_73

    nop

    :goto_19
    if-eqz v1, :cond_2

    goto :goto_31

    :cond_2
    goto :goto_66

    nop

    :goto_1a
    add-int/2addr v1, v10

    goto :goto_51

    nop

    :goto_1b
    iget v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mActionCount:I

    goto :goto_28

    nop

    :goto_1c
    iget v2, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mMenuItemHeight:I

    goto :goto_4a

    nop

    :goto_1d
    invoke-virtual/range {v0 .. v5}, Landroid/widget/LinearLayout;->measureChildWithMargins(Landroid/view/View;IIII)V

    goto :goto_2c

    nop

    :goto_1e
    iget v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mMenuItemGap:I

    goto :goto_2e

    nop

    :goto_1f
    invoke-virtual/range {v0 .. v5}, Landroid/widget/LinearLayout;->measureChildWithMargins(Landroid/view/View;IIII)V

    goto :goto_3

    nop

    :goto_20
    iput v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mMaxActionButtonWidth:I

    goto :goto_70

    nop

    :goto_21
    move v10, v9

    goto :goto_6e

    nop

    :goto_22
    goto :goto_4f

    :goto_23
    goto :goto_4e

    nop

    :goto_24
    iget v2, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mActionCount:I

    goto :goto_c

    nop

    :goto_25
    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mBackgroundView:Landroid/view/View;

    goto :goto_6c

    nop

    :goto_26
    iget v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mMenuItemGap:I

    goto :goto_24

    nop

    :goto_27
    invoke-virtual {v1}, Landroid/view/View;->getMeasuredHeight()I

    move-result v1

    goto :goto_3a

    nop

    :goto_28
    div-int v1, v8, v1

    goto :goto_55

    nop

    :goto_29
    move v4, p2

    goto :goto_1f

    nop

    :goto_2a
    goto :goto_12

    :goto_2b
    goto :goto_f

    nop

    :goto_2c
    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mOverflowMenuView:Landroid/view/View;

    goto :goto_2

    nop

    :goto_2d
    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mOverflowMenuView:Landroid/view/View;

    goto :goto_19

    nop

    :goto_2e
    add-int/lit8 v2, v2, -0x1

    goto :goto_61

    nop

    :goto_2f
    invoke-static {v3, v4}, Ljava/lang/Math;->min(II)I

    move-result v3

    goto :goto_62

    nop

    :goto_30
    add-int/2addr v11, v1

    :goto_31
    goto :goto_25

    nop

    :goto_32
    invoke-static {v10, v1}, Ljava/lang/Math;->max(II)I

    goto :goto_50

    nop

    :goto_33
    sget-object v2, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView$OverflowMenuState;->Collapsed:Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView$OverflowMenuState;

    goto :goto_0

    nop

    :goto_34
    if-nez v1, :cond_3

    goto :goto_48

    :cond_3
    goto :goto_63

    nop

    :goto_35
    invoke-virtual {p0, v8, v11}, Landroid/widget/LinearLayout;->setMeasuredDimension(II)V

    goto :goto_11

    nop

    :goto_36
    iput v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mActionCount:I

    goto :goto_4d

    nop

    :goto_37
    move v4, p2

    goto :goto_1d

    nop

    :goto_38
    invoke-static {v2}, Lmiuix/core/util/MiuixUIUtils;->getStatusBarHeight(Landroid/content/Context;)I

    move-result v2

    goto :goto_5b

    nop

    :goto_39
    sget-object v2, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView$OverflowMenuState;->Expanded:Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView$OverflowMenuState;

    goto :goto_6a

    nop

    :goto_3a
    add-int/2addr v11, v1

    goto :goto_15

    nop

    :goto_3b
    iput v7, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mMenuItemGap:I

    :goto_3c
    goto :goto_1e

    nop

    :goto_3d
    invoke-direct {p0}, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->getActionMenuItemCount()I

    move-result v1

    goto :goto_36

    nop

    :goto_3e
    goto :goto_48

    :goto_3f
    goto :goto_33

    nop

    :goto_40
    if-eq v2, v3, :cond_4

    goto :goto_23

    :cond_4
    goto :goto_10

    nop

    :goto_41
    invoke-virtual {v1, v2}, Landroid/view/View;->setTranslationY(F)V

    goto :goto_3e

    nop

    :goto_42
    invoke-direct {p0, v1, v8}, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->updateItemGapAdaptByCurrentWidth(Landroid/content/Context;I)V

    goto :goto_5a

    nop

    :goto_43
    const/4 v5, 0x0

    goto :goto_5e

    nop

    :goto_44
    move-object v0, p0

    goto :goto_4c

    nop

    :goto_45
    const/4 v2, 0x0

    goto :goto_41

    nop

    :goto_46
    invoke-static {v1, v2}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v2

    goto :goto_6d

    nop

    :goto_47
    invoke-virtual {v1, v2}, Landroid/view/View;->setTranslationY(F)V

    :goto_48
    goto :goto_2d

    nop

    :goto_49
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getChildCount()I

    move-result v6

    goto :goto_3d

    nop

    :goto_4a
    iput v2, v1, Landroid/view/ViewGroup$MarginLayoutParams;->bottomMargin:I

    goto :goto_6b

    nop

    :goto_4b
    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mOverflowMenuView:Landroid/view/View;

    goto :goto_45

    nop

    :goto_4c
    move v2, p1

    goto :goto_37

    nop

    :goto_4d
    const/4 v7, 0x0

    goto :goto_59

    nop

    :goto_4e
    iget-object v2, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mExpandBackground:Landroid/graphics/drawable/Drawable;

    :goto_4f
    goto :goto_69

    nop

    :goto_50
    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mOverflowMenuView:Landroid/view/View;

    goto :goto_27

    nop

    :goto_51
    if-gt v1, v8, :cond_5

    goto :goto_3c

    :cond_5
    goto :goto_3b

    nop

    :goto_52
    if-eqz v1, :cond_6

    goto :goto_2b

    :cond_6
    goto :goto_2a

    nop

    :goto_53
    iput v7, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mMenuItemHeight:I

    goto :goto_5f

    nop

    :goto_54
    const/4 v3, 0x0

    goto :goto_d

    nop

    :goto_55
    iget v2, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mMaxActionButtonWidth:I

    goto :goto_64

    nop

    :goto_56
    if-nez v3, :cond_7

    goto :goto_a

    :cond_7
    goto :goto_9

    nop

    :goto_57
    check-cast v1, Landroid/view/ViewGroup$MarginLayoutParams;

    goto :goto_16

    nop

    :goto_58
    invoke-virtual {p0, v9}, Landroid/widget/LinearLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v1

    goto :goto_5d

    nop

    :goto_59
    if-nez v6, :cond_8

    goto :goto_12

    :cond_8
    goto :goto_52

    nop

    :goto_5a
    iget v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mMaxActionButtonWidth:I

    goto :goto_e

    nop

    :goto_5b
    iput v2, v1, Landroid/view/ViewGroup$MarginLayoutParams;->topMargin:I

    goto :goto_1c

    nop

    :goto_5c
    add-int/lit8 v9, v9, 0x1

    goto :goto_67

    nop

    :goto_5d
    invoke-direct {p0, v1}, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->isNotActionMenuItemChild(Landroid/view/View;)Z

    move-result v3

    goto :goto_56

    nop

    :goto_5e
    move-object v0, p0

    goto :goto_29

    nop

    :goto_5f
    invoke-virtual {p0, v7, v7}, Landroid/widget/LinearLayout;->setMeasuredDimension(II)V

    goto :goto_17

    nop

    :goto_60
    int-to-float v2, v11

    goto :goto_47

    nop

    :goto_61
    mul-int/2addr v1, v2

    goto :goto_18

    nop

    :goto_62
    add-int/2addr v10, v3

    goto :goto_6

    nop

    :goto_63
    invoke-virtual {v1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v1

    goto :goto_57

    nop

    :goto_64
    invoke-static {v1, v2}, Ljava/lang/Math;->min(II)I

    move-result v1

    goto :goto_20

    nop

    :goto_65
    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mOverflowMenuView:Landroid/view/View;

    goto :goto_60

    nop

    :goto_66
    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mBackgroundPadding:Landroid/graphics/Rect;

    goto :goto_71

    nop

    :goto_67
    goto :goto_6f

    :goto_68
    goto :goto_26

    nop

    :goto_69
    invoke-virtual {v1, v2}, Landroid/view/View;->setBackground(Landroid/graphics/drawable/Drawable;)V

    goto :goto_35

    nop

    :goto_6a
    if-eq v1, v2, :cond_9

    goto :goto_3f

    :cond_9
    goto :goto_4b

    nop

    :goto_6b
    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mOverflowMenuView:Landroid/view/View;

    goto :goto_54

    nop

    :goto_6c
    iget-object v2, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mOverflowMenuState:Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView$OverflowMenuState;

    goto :goto_13

    nop

    :goto_6d
    move v9, v7

    goto :goto_21

    nop

    :goto_6e
    move v11, v10

    :goto_6f
    goto :goto_4

    nop

    :goto_70
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getContext()Landroid/content/Context;

    move-result-object v1

    goto :goto_42

    nop

    :goto_71
    iget v1, v1, Landroid/graphics/Rect;->top:I

    goto :goto_30

    nop

    :goto_72
    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mOverflowMenuView:Landroid/view/View;

    goto :goto_34

    nop

    :goto_73
    iput v10, p0, Lmiuix/appcompat/internal/view/menu/action/PhoneActionMenuView;->mMenuItemWidth:I

    goto :goto_14

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
