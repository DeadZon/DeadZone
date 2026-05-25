TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/widget/NestedScrollViewExpander.smali'
CLASS_FALLBACK_NAMES = ['NestedScrollViewExpander.smali']
CLASS_ANCHORS = ['.super Landroid/view/ViewGroup;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_widget_NestedScrollViewExpander__onLayout',
        'method': '.method protected onLayout(ZIIII)V',
        'method_name': 'onLayout',
        'method_anchors': ['invoke-virtual {p0}, Landroid/view/ViewGroup;->getChildCount()I', 'if-ge p5, p1, :cond_0', 'invoke-virtual {p0, p5}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;', 'invoke-virtual {v0}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;', 'check-cast v1, Landroid/view/ViewGroup$MarginLayoutParams;', 'invoke-virtual {v0}, Landroid/view/View;->getMeasuredWidth()I', 'invoke-virtual {v0}, Landroid/view/View;->getMeasuredHeight()I', 'iget v5, v1, Landroid/view/ViewGroup$MarginLayoutParams;->leftMargin:I'],
        'type': 'method_replace',
        'search': """.method protected onLayout(ZIIII)V
    .registers 13

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getChildCount()I

    move-result p1

    const/4 p5, 0x0

    :goto_0
    if-ge p5, p1, :cond_0

    invoke-virtual {p0, p5}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;

    move-result-object v0

    invoke-virtual {v0}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v1

    check-cast v1, Landroid/view/ViewGroup$MarginLayoutParams;

    invoke-virtual {v0}, Landroid/view/View;->getMeasuredWidth()I

    move-result v2

    invoke-virtual {v0}, Landroid/view/View;->getMeasuredHeight()I

    move-result v3

    sub-int v4, p4, p2

    sub-int/2addr v4, v2

    div-int/lit8 v4, v4, 0x2

    add-int/2addr v4, p2

    iget v5, v1, Landroid/view/ViewGroup$MarginLayoutParams;->leftMargin:I

    add-int/2addr v4, v5

    iget v5, v1, Landroid/view/ViewGroup$MarginLayoutParams;->rightMargin:I

    sub-int/2addr v4, v5

    iget v5, v1, Landroid/view/ViewGroup$MarginLayoutParams;->topMargin:I

    add-int/2addr v5, p3

    add-int/2addr v2, v4

    add-int v6, v5, v3

    invoke-virtual {v0, v4, v5, v2, v6}, Landroid/view/View;->layout(IIII)V

    iget v0, v1, Landroid/view/ViewGroup$MarginLayoutParams;->topMargin:I

    add-int/2addr p3, v0

    add-int/2addr p3, v3

    iget v0, v1, Landroid/view/ViewGroup$MarginLayoutParams;->bottomMargin:I

    add-int/2addr p3, v0

    add-int/lit8 p5, p5, 0x1

    goto :goto_0

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onLayout(ZIIII)V
    .registers 13

    goto :goto_a

    nop

    :goto_0
    invoke-virtual {v0}, Landroid/view/View;->getMeasuredHeight()I

    move-result v3

    goto :goto_8

    nop

    :goto_1
    iget v5, v1, Landroid/view/ViewGroup$MarginLayoutParams;->topMargin:I

    goto :goto_5

    nop

    :goto_2
    add-int v6, v5, v3

    goto :goto_16

    nop

    :goto_3
    invoke-virtual {v0}, Landroid/view/View;->getMeasuredWidth()I

    move-result v2

    goto :goto_0

    nop

    :goto_4
    add-int/2addr v4, v5

    goto :goto_b

    nop

    :goto_5
    add-int/2addr v5, p3

    goto :goto_d

    nop

    :goto_6
    const/4 p5, 0x0

    :goto_7
    goto :goto_c

    nop

    :goto_8
    sub-int v4, p4, p2

    goto :goto_17

    nop

    :goto_9
    add-int/2addr p3, v3

    goto :goto_1e

    nop

    :goto_a
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getChildCount()I

    move-result p1

    goto :goto_6

    nop

    :goto_b
    iget v5, v1, Landroid/view/ViewGroup$MarginLayoutParams;->rightMargin:I

    goto :goto_e

    nop

    :goto_c
    if-lt p5, p1, :cond_0

    goto :goto_11

    :cond_0
    goto :goto_18

    nop

    :goto_d
    add-int/2addr v2, v4

    goto :goto_2

    nop

    :goto_e
    sub-int/2addr v4, v5

    goto :goto_1

    nop

    :goto_f
    return-void

    :goto_10
    goto :goto_7

    :goto_11
    goto :goto_f

    nop

    :goto_12
    iget v0, v1, Landroid/view/ViewGroup$MarginLayoutParams;->topMargin:I

    goto :goto_14

    nop

    :goto_13
    check-cast v1, Landroid/view/ViewGroup$MarginLayoutParams;

    goto :goto_3

    nop

    :goto_14
    add-int/2addr p3, v0

    goto :goto_9

    nop

    :goto_15
    iget v5, v1, Landroid/view/ViewGroup$MarginLayoutParams;->leftMargin:I

    goto :goto_4

    nop

    :goto_16
    invoke-virtual {v0, v4, v5, v2, v6}, Landroid/view/View;->layout(IIII)V

    goto :goto_12

    nop

    :goto_17
    sub-int/2addr v4, v2

    goto :goto_1c

    nop

    :goto_18
    invoke-virtual {p0, p5}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;

    move-result-object v0

    goto :goto_1a

    nop

    :goto_19
    add-int/2addr v4, p2

    goto :goto_15

    nop

    :goto_1a
    invoke-virtual {v0}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v1

    goto :goto_13

    nop

    :goto_1b
    add-int/lit8 p5, p5, 0x1

    goto :goto_10

    nop

    :goto_1c
    div-int/lit8 v4, v4, 0x2

    goto :goto_19

    nop

    :goto_1d
    add-int/2addr p3, v0

    goto :goto_1b

    nop

    :goto_1e
    iget v0, v1, Landroid/view/ViewGroup$MarginLayoutParams;->bottomMargin:I

    goto :goto_1d

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_widget_NestedScrollViewExpander__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['iget v1, v0, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;->mParentHeightMeasureSpec:I', 'invoke-static {v1}, Landroid/view/View$MeasureSpec;->getMode(I)I', 'if-nez v1, :cond_0', 'invoke-static/range {p1 .. p1}, Landroid/view/View$MeasureSpec;->getSize(I)I', 'invoke-virtual {v0}, Landroid/view/ViewGroup;->getChildCount()I', 'if-ge v10, v8, :cond_5', 'invoke-virtual {v0, v10}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;', 'invoke-virtual {v2}, Landroid/view/View;->getVisibility()I'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 19

    move-object/from16 v0, p0

    iget v1, v0, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;->mParentHeightMeasureSpec:I

    invoke-static {v1}, Landroid/view/View$MeasureSpec;->getMode(I)I

    move-result v1

    if-nez v1, :cond_0

    const/high16 v1, -0x80000000

    :cond_0
    move v6, v1

    invoke-static/range {p1 .. p1}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v7

    invoke-virtual {v0}, Landroid/view/ViewGroup;->getChildCount()I

    move-result v8

    const/4 v10, 0x0

    const/4 v11, 0x0

    const/4 v12, 0x0

    const/4 v13, 0x0

    const/4 v14, 0x0

    :goto_0
    const/16 v1, 0x8

    if-ge v10, v8, :cond_5

    invoke-virtual {v0, v10}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;

    move-result-object v2

    invoke-virtual {v2}, Landroid/view/View;->getVisibility()I

    move-result v3

    if-ne v3, v1, :cond_1

    goto :goto_2

    :cond_1
    iget-object v1, v0, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;->mExpandView:Landroid/view/View;

    const/4 v15, 0x1

    if-eq v1, v2, :cond_2

    invoke-virtual {v2}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v1

    check-cast v1, Landroid/view/ViewGroup$MarginLayoutParams;

    const/4 v3, 0x0

    const/4 v5, 0x0

    move/from16 v4, p2

    move-object v9, v1

    move-object v1, v2

    move/from16 v2, p1

    invoke-virtual/range {v0 .. v5}, Landroid/view/ViewGroup;->measureChildWithMargins(Landroid/view/View;IIII)V

    invoke-virtual {v1}, Landroid/view/View;->getMeasuredHeight()I

    move-result v2

    iget v3, v9, Landroid/view/ViewGroup$MarginLayoutParams;->topMargin:I

    add-int/2addr v2, v3

    iget v3, v9, Landroid/view/ViewGroup$MarginLayoutParams;->bottomMargin:I

    add-int/2addr v2, v3

    add-int/2addr v11, v2

    invoke-virtual {v1}, Landroid/view/View;->getId()I

    move-result v2

    sget v3, Lmiuix/appcompat/R$id;->contentView:I

    if-ne v2, v3, :cond_3

    invoke-virtual {v1}, Landroid/view/View;->getMeasuredHeight()I

    move-result v2

    iget v3, v9, Landroid/view/ViewGroup$MarginLayoutParams;->topMargin:I

    add-int/2addr v2, v3

    iget v3, v9, Landroid/view/ViewGroup$MarginLayoutParams;->bottomMargin:I

    add-int v14, v2, v3

    move v12, v15

    goto :goto_1

    :cond_2
    move-object v1, v2

    :cond_3
    :goto_1
    invoke-virtual {v1}, Landroid/view/View;->getId()I

    move-result v1

    sget v2, Lmiuix/appcompat/R$id;->buttonPanel:I

    if-ne v1, v2, :cond_4

    move v13, v15

    :cond_4
    :goto_2
    add-int/lit8 v10, v10, 0x1

    goto :goto_0

    :cond_5
    iget v2, v0, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;->mParentHeightMeasureSpec:I

    invoke-static {v2}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v2

    sub-int v3, v2, v11

    iget-object v4, v0, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;->mExpandView:Landroid/view/View;

    if-eqz v4, :cond_8

    invoke-virtual {v4}, Landroid/view/View;->getVisibility()I

    move-result v4

    if-eq v4, v1, :cond_8

    iget-object v1, v0, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;->mExpandView:Landroid/view/View;

    invoke-virtual {v1}, Landroid/view/View;->getMinimumHeight()I

    move-result v1

    if-ge v3, v1, :cond_6

    iget-object v1, v0, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;->mExpandView:Landroid/view/View;

    invoke-virtual {v1}, Landroid/view/View;->getMinimumHeight()I

    move-result v3

    :cond_6
    iget-object v1, v0, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;->mExpandView:Landroid/view/View;

    invoke-virtual {v1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v1

    move-object v8, v1

    check-cast v8, Landroid/view/ViewGroup$MarginLayoutParams;

    if-eqz v12, :cond_7

    if-nez v13, :cond_7

    if-lt v14, v2, :cond_7

    iget-object v1, v0, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;->mExpandView:Landroid/view/View;

    const/4 v3, 0x0

    const/4 v5, 0x0

    move/from16 v2, p1

    move/from16 v4, p2

    invoke-virtual/range {v0 .. v5}, Landroid/view/ViewGroup;->measureChildWithMargins(Landroid/view/View;IIII)V

    goto :goto_3

    :cond_7
    iget-object v1, v0, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;->mExpandView:Landroid/view/View;

    invoke-static {v3, v6}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v4

    const/4 v5, 0x0

    const/4 v3, 0x0

    move/from16 v2, p1

    invoke-virtual/range {v0 .. v5}, Landroid/view/ViewGroup;->measureChildWithMargins(Landroid/view/View;IIII)V

    :goto_3
    iget-object v1, v0, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;->mExpandView:Landroid/view/View;

    invoke-virtual {v1}, Landroid/view/View;->getMeasuredHeight()I

    move-result v1

    iget v2, v8, Landroid/view/ViewGroup$MarginLayoutParams;->topMargin:I

    add-int/2addr v1, v2

    iget v2, v8, Landroid/view/ViewGroup$MarginLayoutParams;->bottomMargin:I

    add-int v9, v1, v2

    goto :goto_4

    :cond_8
    const/4 v9, 0x0

    :goto_4
    add-int/2addr v9, v11

    invoke-virtual {v0, v7, v9}, Landroid/view/ViewGroup;->setMeasuredDimension(II)V

    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 19

    goto :goto_c

    nop

    :goto_0
    invoke-virtual {v2}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v1

    goto :goto_51

    nop

    :goto_1
    return-void

    :goto_2
    move/from16 v2, p1

    goto :goto_16

    nop

    :goto_3
    if-eq v3, v1, :cond_0

    goto :goto_61

    :cond_0
    goto :goto_60

    nop

    :goto_4
    invoke-static {v1}, Landroid/view/View$MeasureSpec;->getMode(I)I

    move-result v1

    goto :goto_54

    nop

    :goto_5
    iget v2, v0, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;->mParentHeightMeasureSpec:I

    goto :goto_1f

    nop

    :goto_6
    invoke-virtual {v2}, Landroid/view/View;->getVisibility()I

    move-result v3

    goto :goto_3

    nop

    :goto_7
    invoke-virtual {v1}, Landroid/view/View;->getMeasuredHeight()I

    move-result v2

    goto :goto_22

    nop

    :goto_8
    invoke-virtual {v0, v7, v9}, Landroid/view/ViewGroup;->setMeasuredDimension(II)V

    goto :goto_1

    nop

    :goto_9
    iget v3, v9, Landroid/view/ViewGroup$MarginLayoutParams;->bottomMargin:I

    goto :goto_46

    nop

    :goto_a
    const/4 v15, 0x1

    goto :goto_56

    nop

    :goto_b
    add-int/lit8 v10, v10, 0x1

    goto :goto_2a

    nop

    :goto_c
    move-object/from16 v0, p0

    goto :goto_50

    nop

    :goto_d
    add-int/2addr v11, v2

    goto :goto_2e

    nop

    :goto_e
    const/16 v1, 0x8

    goto :goto_66

    nop

    :goto_f
    move-object v1, v2

    :goto_10
    goto :goto_52

    nop

    :goto_11
    iget-object v1, v0, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;->mExpandView:Landroid/view/View;

    goto :goto_3a

    nop

    :goto_12
    if-eq v2, v3, :cond_1

    goto :goto_10

    :cond_1
    goto :goto_7

    nop

    :goto_13
    iget-object v1, v0, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;->mExpandView:Landroid/view/View;

    goto :goto_44

    nop

    :goto_14
    add-int/2addr v2, v3

    goto :goto_9

    nop

    :goto_15
    invoke-virtual {v1}, Landroid/view/View;->getMeasuredHeight()I

    move-result v2

    goto :goto_1d

    nop

    :goto_16
    move/from16 v4, p2

    goto :goto_19

    nop

    :goto_17
    invoke-virtual/range {v0 .. v5}, Landroid/view/ViewGroup;->measureChildWithMargins(Landroid/view/View;IIII)V

    :goto_18
    goto :goto_4a

    nop

    :goto_19
    invoke-virtual/range {v0 .. v5}, Landroid/view/ViewGroup;->measureChildWithMargins(Landroid/view/View;IIII)V

    goto :goto_37

    nop

    :goto_1a
    iget-object v1, v0, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;->mExpandView:Landroid/view/View;

    goto :goto_3b

    nop

    :goto_1b
    if-nez v4, :cond_2

    goto :goto_5b

    :cond_2
    goto :goto_43

    nop

    :goto_1c
    iget v2, v8, Landroid/view/ViewGroup$MarginLayoutParams;->topMargin:I

    goto :goto_1e

    nop

    :goto_1d
    iget v3, v9, Landroid/view/ViewGroup$MarginLayoutParams;->topMargin:I

    goto :goto_14

    nop

    :goto_1e
    add-int/2addr v1, v2

    goto :goto_57

    nop

    :goto_1f
    invoke-static {v2}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v2

    goto :goto_64

    nop

    :goto_20
    iget v3, v9, Landroid/view/ViewGroup$MarginLayoutParams;->bottomMargin:I

    goto :goto_48

    nop

    :goto_21
    const/4 v13, 0x0

    goto :goto_24

    nop

    :goto_22
    iget v3, v9, Landroid/view/ViewGroup$MarginLayoutParams;->topMargin:I

    goto :goto_5d

    nop

    :goto_23
    if-ne v4, v1, :cond_3

    goto :goto_5b

    :cond_3
    goto :goto_31

    nop

    :goto_24
    const/4 v14, 0x0

    :goto_25
    goto :goto_e

    nop

    :goto_26
    add-int v9, v1, v2

    goto :goto_5a

    nop

    :goto_27
    const/4 v5, 0x0

    goto :goto_63

    nop

    :goto_28
    const/4 v9, 0x0

    :goto_29
    goto :goto_4f

    nop

    :goto_2a
    goto :goto_25

    :goto_2b
    goto :goto_5

    nop

    :goto_2c
    invoke-virtual {v1}, Landroid/view/View;->getMeasuredHeight()I

    move-result v1

    goto :goto_1c

    nop

    :goto_2d
    iget-object v1, v0, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;->mExpandView:Landroid/view/View;

    goto :goto_a

    nop

    :goto_2e
    invoke-virtual {v1}, Landroid/view/View;->getId()I

    move-result v2

    goto :goto_36

    nop

    :goto_2f
    iget-object v1, v0, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;->mExpandView:Landroid/view/View;

    goto :goto_6c

    nop

    :goto_30
    move-object v9, v1

    goto :goto_49

    nop

    :goto_31
    iget-object v1, v0, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;->mExpandView:Landroid/view/View;

    goto :goto_45

    nop

    :goto_32
    if-eq v1, v2, :cond_4

    goto :goto_40

    :cond_4
    goto :goto_3f

    nop

    :goto_33
    move/from16 v4, p2

    goto :goto_30

    nop

    :goto_34
    if-eqz v13, :cond_5

    goto :goto_38

    :cond_5
    goto :goto_55

    nop

    :goto_35
    sget v2, Lmiuix/appcompat/R$id;->buttonPanel:I

    goto :goto_32

    nop

    :goto_36
    sget v3, Lmiuix/appcompat/R$id;->contentView:I

    goto :goto_12

    nop

    :goto_37
    goto :goto_18

    :goto_38
    goto :goto_2f

    nop

    :goto_39
    move/from16 v2, p1

    goto :goto_17

    nop

    :goto_3a
    const/4 v3, 0x0

    goto :goto_6b

    nop

    :goto_3b
    invoke-virtual {v1}, Landroid/view/View;->getMinimumHeight()I

    move-result v3

    :goto_3c
    goto :goto_13

    nop

    :goto_3d
    const/4 v11, 0x0

    goto :goto_3e

    nop

    :goto_3e
    const/4 v12, 0x0

    goto :goto_21

    nop

    :goto_3f
    move v13, v15

    :goto_40
    goto :goto_b

    nop

    :goto_41
    const/high16 v1, -0x80000000

    :goto_42
    goto :goto_4e

    nop

    :goto_43
    invoke-virtual {v4}, Landroid/view/View;->getVisibility()I

    move-result v4

    goto :goto_23

    nop

    :goto_44
    invoke-virtual {v1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v1

    goto :goto_68

    nop

    :goto_45
    invoke-virtual {v1}, Landroid/view/View;->getMinimumHeight()I

    move-result v1

    goto :goto_5c

    nop

    :goto_46
    add-int/2addr v2, v3

    goto :goto_d

    nop

    :goto_47
    const/4 v10, 0x0

    goto :goto_3d

    nop

    :goto_48
    add-int v14, v2, v3

    goto :goto_59

    nop

    :goto_49
    move-object v1, v2

    goto :goto_62

    nop

    :goto_4a
    iget-object v1, v0, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;->mExpandView:Landroid/view/View;

    goto :goto_2c

    nop

    :goto_4b
    goto :goto_10

    :goto_4c
    goto :goto_f

    nop

    :goto_4d
    if-nez v12, :cond_6

    goto :goto_38

    :cond_6
    goto :goto_34

    nop

    :goto_4e
    move v6, v1

    goto :goto_58

    nop

    :goto_4f
    add-int/2addr v9, v11

    goto :goto_8

    nop

    :goto_50
    iget v1, v0, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;->mParentHeightMeasureSpec:I

    goto :goto_4

    nop

    :goto_51
    check-cast v1, Landroid/view/ViewGroup$MarginLayoutParams;

    goto :goto_5e

    nop

    :goto_52
    invoke-virtual {v1}, Landroid/view/View;->getId()I

    move-result v1

    goto :goto_35

    nop

    :goto_53
    check-cast v8, Landroid/view/ViewGroup$MarginLayoutParams;

    goto :goto_4d

    nop

    :goto_54
    if-eqz v1, :cond_7

    goto :goto_42

    :cond_7
    goto :goto_41

    nop

    :goto_55
    if-ge v14, v2, :cond_8

    goto :goto_38

    :cond_8
    goto :goto_11

    nop

    :goto_56
    if-ne v1, v2, :cond_9

    goto :goto_4c

    :cond_9
    goto :goto_0

    nop

    :goto_57
    iget v2, v8, Landroid/view/ViewGroup$MarginLayoutParams;->bottomMargin:I

    goto :goto_26

    nop

    :goto_58
    invoke-static/range {p1 .. p1}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v7

    goto :goto_5f

    nop

    :goto_59
    move v12, v15

    goto :goto_4b

    nop

    :goto_5a
    goto :goto_29

    :goto_5b
    goto :goto_28

    nop

    :goto_5c
    if-lt v3, v1, :cond_a

    goto :goto_3c

    :cond_a
    goto :goto_1a

    nop

    :goto_5d
    add-int/2addr v2, v3

    goto :goto_20

    nop

    :goto_5e
    const/4 v3, 0x0

    goto :goto_65

    nop

    :goto_5f
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getChildCount()I

    move-result v8

    goto :goto_47

    nop

    :goto_60
    goto :goto_40

    :goto_61
    goto :goto_2d

    nop

    :goto_62
    move/from16 v2, p1

    goto :goto_67

    nop

    :goto_63
    const/4 v3, 0x0

    goto :goto_39

    nop

    :goto_64
    sub-int v3, v2, v11

    goto :goto_69

    nop

    :goto_65
    const/4 v5, 0x0

    goto :goto_33

    nop

    :goto_66
    if-lt v10, v8, :cond_b

    goto :goto_2b

    :cond_b
    goto :goto_6a

    nop

    :goto_67
    invoke-virtual/range {v0 .. v5}, Landroid/view/ViewGroup;->measureChildWithMargins(Landroid/view/View;IIII)V

    goto :goto_15

    nop

    :goto_68
    move-object v8, v1

    goto :goto_53

    nop

    :goto_69
    iget-object v4, v0, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;->mExpandView:Landroid/view/View;

    goto :goto_1b

    nop

    :goto_6a
    invoke-virtual {v0, v10}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;

    move-result-object v2

    goto :goto_6

    nop

    :goto_6b
    const/4 v5, 0x0

    goto :goto_2

    nop

    :goto_6c
    invoke-static {v3, v6}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v4

    goto :goto_27

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_widget_NestedScrollViewExpander__setParentHeightMeasureSpec',
        'method': '.method setParentHeightMeasureSpec(I)V',
        'method_name': 'setParentHeightMeasureSpec',
        'method_anchors': ['iput p1, p0, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;->mParentHeightMeasureSpec:I', 'return-void'],
        'type': 'method_replace',
        'search': """.method setParentHeightMeasureSpec(I)V
    .registers 2

    iput p1, p0, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;->mParentHeightMeasureSpec:I

    return-void
.end method""",
        'replacement': """.method setParentHeightMeasureSpec(I)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    iput p1, p0, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;->mParentHeightMeasureSpec:I

    goto :goto_1

    nop

    :goto_1
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
