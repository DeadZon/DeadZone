TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/view/menu/action/EndActionMenuView.smali'
CLASS_FALLBACK_NAMES = ['EndActionMenuView.smali']
CLASS_ANCHORS = ['.super Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_view_menu_action_EndActionMenuView__onLayout',
        'method': '.method protected onLayout(ZIIII)V',
        'method_name': 'onLayout',
        'method_anchors': ['invoke-virtual {p0}, Landroid/widget/LinearLayout;->getChildCount()I', 'iget p1, p0, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->mStartPadding:I', 'if-ge v1, v0, :cond_1', 'invoke-virtual {p0, v1}, Landroid/widget/LinearLayout;->getChildAt(I)Landroid/view/View;', 'invoke-direct {p0, p1}, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->isNotActionMenuItemChild(Landroid/view/View;)Z', 'if-nez p3, :cond_0', 'invoke-virtual {p1}, Landroid/view/View;->getMeasuredWidth()I', 'invoke-static/range {p0 .. p5}, Lmiuix/internal/util/ViewUtils;->layoutChildView(Landroid/view/ViewGroup;Landroid/view/View;IIII)V'],
        'type': 'method_replace',
        'search': """.method protected onLayout(ZIIII)V
    .registers 8

    sub-int/2addr p5, p3

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getChildCount()I

    move-result v0

    iget p1, p0, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->mStartPadding:I

    const/4 p2, 0x0

    move v1, p2

    move p2, p1

    :goto_0
    if-ge v1, v0, :cond_1

    invoke-virtual {p0, v1}, Landroid/widget/LinearLayout;->getChildAt(I)Landroid/view/View;

    move-result-object p1

    invoke-direct {p0, p1}, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->isNotActionMenuItemChild(Landroid/view/View;)Z

    move-result p3

    if-nez p3, :cond_0

    invoke-virtual {p1}, Landroid/view/View;->getMeasuredWidth()I

    move-result p3

    add-int p4, p2, p3

    const/4 p3, 0x0

    invoke-static/range {p0 .. p5}, Lmiuix/internal/util/ViewUtils;->layoutChildView(Landroid/view/ViewGroup;Landroid/view/View;IIII)V

    invoke-virtual {p1}, Landroid/view/View;->getMeasuredWidth()I

    move-result p1

    iget p3, p0, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->mMenuItemGap:I

    add-int/2addr p1, p3

    add-int/2addr p2, p1

    :cond_0
    add-int/lit8 v1, v1, 0x1

    goto :goto_0

    :cond_1
    return-void
.end method""",
        'replacement': """.method protected onLayout(ZIIII)V
    .registers 8

    goto :goto_3

    nop

    :goto_0
    iget p1, p0, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->mStartPadding:I

    goto :goto_1

    nop

    :goto_1
    const/4 p2, 0x0

    goto :goto_e

    nop

    :goto_2
    return-void

    :goto_3
    sub-int/2addr p5, p3

    goto :goto_a

    nop

    :goto_4
    move p2, p1

    :goto_5
    goto :goto_11

    nop

    :goto_6
    invoke-static/range {p0 .. p5}, Lmiuix/internal/util/ViewUtils;->layoutChildView(Landroid/view/ViewGroup;Landroid/view/View;IIII)V

    goto :goto_13

    nop

    :goto_7
    add-int p4, p2, p3

    goto :goto_c

    nop

    :goto_8
    add-int/2addr p2, p1

    :goto_9
    goto :goto_16

    nop

    :goto_a
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getChildCount()I

    move-result v0

    goto :goto_0

    nop

    :goto_b
    if-eqz p3, :cond_0

    goto :goto_9

    :cond_0
    goto :goto_12

    nop

    :goto_c
    const/4 p3, 0x0

    goto :goto_6

    nop

    :goto_d
    invoke-virtual {p0, v1}, Landroid/widget/LinearLayout;->getChildAt(I)Landroid/view/View;

    move-result-object p1

    goto :goto_f

    nop

    :goto_e
    move v1, p2

    goto :goto_4

    nop

    :goto_f
    invoke-direct {p0, p1}, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->isNotActionMenuItemChild(Landroid/view/View;)Z

    move-result p3

    goto :goto_b

    nop

    :goto_10
    add-int/2addr p1, p3

    goto :goto_8

    nop

    :goto_11
    if-lt v1, v0, :cond_1

    goto :goto_15

    :cond_1
    goto :goto_d

    nop

    :goto_12
    invoke-virtual {p1}, Landroid/view/View;->getMeasuredWidth()I

    move-result p3

    goto :goto_7

    nop

    :goto_13
    invoke-virtual {p1}, Landroid/view/View;->getMeasuredWidth()I

    move-result p1

    goto :goto_17

    nop

    :goto_14
    goto :goto_5

    :goto_15
    goto :goto_2

    nop

    :goto_16
    add-int/lit8 v1, v1, 0x1

    goto :goto_14

    nop

    :goto_17
    iget p3, p0, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->mMenuItemGap:I

    goto :goto_10

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_action_EndActionMenuView__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['invoke-virtual {p0}, Landroid/widget/LinearLayout;->getChildCount()I', 'invoke-direct {p0}, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->getActionMenuItemCount()I', 'iput v1, p0, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->mActionCount:I', 'if-eqz v0, :cond_0', 'if-nez v1, :cond_1', 'invoke-static {p1}, Landroid/view/View$MeasureSpec;->getSize(I)I', 'iget v1, p0, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->mActionCount:I', 'iget v3, p0, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->mMaxActionButtonWidth:I'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 15

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getChildCount()I

    move-result v0

    invoke-direct {p0}, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->getActionMenuItemCount()I

    move-result v1

    iput v1, p0, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->mActionCount:I

    const/4 v2, 0x0

    if-eqz v0, :cond_0

    if-nez v1, :cond_1

    :cond_0
    move-object v4, p0

    goto :goto_2

    :cond_1
    invoke-static {p1}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result p1

    iget v1, p0, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->mActionCount:I

    div-int v1, p1, v1

    iget v3, p0, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->mMaxActionButtonWidth:I

    invoke-static {v1, v3}, Ljava/lang/Math;->min(II)I

    move-result v1

    const/high16 v3, -0x80000000

    invoke-static {v1, v3}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v6

    move v3, v2

    move v10, v3

    move v11, v10

    :goto_0
    if-ge v3, v0, :cond_3

    invoke-virtual {p0, v3}, Landroid/widget/LinearLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v5

    invoke-direct {p0, v5}, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->isNotActionMenuItemChild(Landroid/view/View;)Z

    move-result v4

    if-eqz v4, :cond_2

    move-object v4, p0

    move v8, p2

    goto :goto_1

    :cond_2
    const/4 v7, 0x0

    const/4 v9, 0x0

    move-object v4, p0

    move v8, p2

    invoke-virtual/range {v4 .. v9}, Landroid/widget/LinearLayout;->measureChildWithMargins(Landroid/view/View;IIII)V

    invoke-virtual {v5}, Landroid/view/View;->getMeasuredWidth()I

    move-result p0

    invoke-static {p0, v1}, Ljava/lang/Math;->min(II)I

    move-result p0

    add-int/2addr v10, p0

    invoke-virtual {v5}, Landroid/view/View;->getMeasuredHeight()I

    move-result p0

    invoke-static {v11, p0}, Ljava/lang/Math;->max(II)I

    move-result v11

    :goto_1
    add-int/lit8 v3, v3, 0x1

    move-object p0, v4

    move p2, v8

    goto :goto_0

    :cond_3
    move-object v4, p0

    iget p0, v4, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->mMenuItemGap:I

    iget p2, v4, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->mActionCount:I

    add-int/lit8 p2, p2, -0x1

    mul-int/2addr p0, p2

    iget p2, v4, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->mStartPadding:I

    add-int v0, p2, v10

    add-int/2addr v0, p0

    if-le v0, p1, :cond_4

    iput v2, v4, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->mMenuItemGap:I

    :cond_4
    add-int/2addr v10, p0

    add-int/2addr v10, p2

    iput v10, v4, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->mMenuItemWidth:I

    iput v11, v4, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->mMenuItemHeight:I

    invoke-virtual {v4, v10, v11}, Landroid/widget/LinearLayout;->setMeasuredDimension(II)V

    return-void

    :goto_2
    iput v2, v4, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->mMenuItemHeight:I

    invoke-virtual {v4, v2, v2}, Landroid/widget/LinearLayout;->setMeasuredDimension(II)V

    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 15

    goto :goto_37

    nop

    :goto_0
    move p2, v8

    goto :goto_35

    nop

    :goto_1
    move-object v4, p0

    goto :goto_e

    nop

    :goto_2
    iput v2, v4, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->mMenuItemGap:I

    :goto_3
    goto :goto_40

    nop

    :goto_4
    iget p2, v4, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->mStartPadding:I

    goto :goto_7

    nop

    :goto_5
    div-int v1, p1, v1

    goto :goto_1d

    nop

    :goto_6
    move v8, p2

    goto :goto_17

    nop

    :goto_7
    add-int v0, p2, v10

    goto :goto_41

    nop

    :goto_8
    invoke-virtual {v5}, Landroid/view/View;->getMeasuredHeight()I

    move-result p0

    goto :goto_3b

    nop

    :goto_9
    invoke-static {v1, v3}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v6

    goto :goto_14

    nop

    :goto_a
    invoke-virtual {v5}, Landroid/view/View;->getMeasuredWidth()I

    move-result p0

    goto :goto_29

    nop

    :goto_b
    iget p2, v4, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->mActionCount:I

    goto :goto_16

    nop

    :goto_c
    iput v2, v4, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->mMenuItemHeight:I

    goto :goto_3a

    nop

    :goto_d
    const/4 v9, 0x0

    goto :goto_21

    nop

    :goto_e
    goto :goto_1c

    :goto_f
    goto :goto_2d

    nop

    :goto_10
    iput v11, v4, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->mMenuItemHeight:I

    goto :goto_2c

    nop

    :goto_11
    add-int/2addr v10, p0

    goto :goto_8

    nop

    :goto_12
    add-int/2addr v10, p2

    goto :goto_2e

    nop

    :goto_13
    invoke-direct {p0}, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->getActionMenuItemCount()I

    move-result v1

    goto :goto_28

    nop

    :goto_14
    move v3, v2

    goto :goto_30

    nop

    :goto_15
    invoke-direct {p0, v5}, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->isNotActionMenuItemChild(Landroid/view/View;)Z

    move-result v4

    goto :goto_32

    nop

    :goto_16
    add-int/lit8 p2, p2, -0x1

    goto :goto_22

    nop

    :goto_17
    goto :goto_3c

    :goto_18
    goto :goto_3f

    nop

    :goto_19
    if-eqz v1, :cond_0

    goto :goto_f

    :cond_0
    :goto_1a
    goto :goto_1

    nop

    :goto_1b
    return-void

    :goto_1c
    goto :goto_c

    nop

    :goto_1d
    iget v3, p0, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->mMaxActionButtonWidth:I

    goto :goto_23

    nop

    :goto_1e
    move-object v4, p0

    goto :goto_6

    nop

    :goto_1f
    move v8, p2

    goto :goto_25

    nop

    :goto_20
    return-void

    :goto_21
    move-object v4, p0

    goto :goto_1f

    nop

    :goto_22
    mul-int/2addr p0, p2

    goto :goto_4

    nop

    :goto_23
    invoke-static {v1, v3}, Ljava/lang/Math;->min(II)I

    move-result v1

    goto :goto_39

    nop

    :goto_24
    iget v1, p0, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->mActionCount:I

    goto :goto_5

    nop

    :goto_25
    invoke-virtual/range {v4 .. v9}, Landroid/widget/LinearLayout;->measureChildWithMargins(Landroid/view/View;IIII)V

    goto :goto_a

    nop

    :goto_26
    invoke-virtual {p0, v3}, Landroid/widget/LinearLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v5

    goto :goto_15

    nop

    :goto_27
    add-int/lit8 v3, v3, 0x1

    goto :goto_33

    nop

    :goto_28
    iput v1, p0, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->mActionCount:I

    goto :goto_3d

    nop

    :goto_29
    invoke-static {p0, v1}, Ljava/lang/Math;->min(II)I

    move-result p0

    goto :goto_11

    nop

    :goto_2a
    move v11, v10

    :goto_2b
    goto :goto_34

    nop

    :goto_2c
    invoke-virtual {v4, v10, v11}, Landroid/widget/LinearLayout;->setMeasuredDimension(II)V

    goto :goto_1b

    nop

    :goto_2d
    invoke-static {p1}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result p1

    goto :goto_24

    nop

    :goto_2e
    iput v10, v4, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->mMenuItemWidth:I

    goto :goto_10

    nop

    :goto_2f
    if-nez v0, :cond_1

    goto :goto_1a

    :cond_1
    goto :goto_19

    nop

    :goto_30
    move v10, v3

    goto :goto_2a

    nop

    :goto_31
    if-gt v0, p1, :cond_2

    goto :goto_3

    :cond_2
    goto :goto_2

    nop

    :goto_32
    if-nez v4, :cond_3

    goto :goto_18

    :cond_3
    goto :goto_1e

    nop

    :goto_33
    move-object p0, v4

    goto :goto_0

    nop

    :goto_34
    if-lt v3, v0, :cond_4

    goto :goto_36

    :cond_4
    goto :goto_26

    nop

    :goto_35
    goto :goto_2b

    :goto_36
    goto :goto_38

    nop

    :goto_37
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getChildCount()I

    move-result v0

    goto :goto_13

    nop

    :goto_38
    move-object v4, p0

    goto :goto_3e

    nop

    :goto_39
    const/high16 v3, -0x80000000

    goto :goto_9

    nop

    :goto_3a
    invoke-virtual {v4, v2, v2}, Landroid/widget/LinearLayout;->setMeasuredDimension(II)V

    goto :goto_20

    nop

    :goto_3b
    invoke-static {v11, p0}, Ljava/lang/Math;->max(II)I

    move-result v11

    :goto_3c
    goto :goto_27

    nop

    :goto_3d
    const/4 v2, 0x0

    goto :goto_2f

    nop

    :goto_3e
    iget p0, v4, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuView;->mMenuItemGap:I

    goto :goto_b

    nop

    :goto_3f
    const/4 v7, 0x0

    goto :goto_d

    nop

    :goto_40
    add-int/2addr v10, p0

    goto :goto_12

    nop

    :goto_41
    add-int/2addr v0, p0

    goto :goto_31

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
