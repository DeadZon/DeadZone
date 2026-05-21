TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/core/widget/NestedScrollView.smali'
CLASS_FALLBACK_NAMES = ['NestedScrollView.smali']
CLASS_ANCHORS = ['.super Landroid/widget/FrameLayout;', '.implements Landroidx/core/view/NestedScrollingParent3;', '.implements Landroidx/core/view/NestedScrollingChild3;', '.implements Landroidx/core/view/ScrollingView;', '.implements Lmiuix/core/view/NestedContentInsetObserver;', '.field private static final ACCESSIBILITY_DELEGATE:Lmiuix/core/widget/NestedScrollView$AccessibilityDelegate;']

PATCHES = [
    {
        'id': 'miuix_core_widget_NestedScrollView__getScrollRange',
        'method': '.method getScrollRange()I',
        'method_name': 'getScrollRange',
        'method_anchors': ['invoke-virtual {p0}, Landroid/widget/FrameLayout;->getChildCount()I', 'if-lez v0, :cond_0', 'invoke-virtual {p0, v1}, Landroid/widget/FrameLayout;->getChildAt(I)Landroid/view/View;', 'invoke-virtual {v0}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;', 'check-cast v2, Landroid/widget/FrameLayout$LayoutParams;', 'invoke-virtual {v0}, Landroid/view/View;->getHeight()I', 'iget v3, v2, Landroid/widget/FrameLayout$LayoutParams;->topMargin:I', 'iget v2, v2, Landroid/widget/FrameLayout$LayoutParams;->bottomMargin:I'],
        'type': 'method_replace',
        'search': """.method getScrollRange()I
    .registers 5

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getChildCount()I

    move-result v0

    const/4 v1, 0x0

    if-lez v0, :cond_0

    invoke-virtual {p0, v1}, Landroid/widget/FrameLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v0

    invoke-virtual {v0}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v2

    check-cast v2, Landroid/widget/FrameLayout$LayoutParams;

    invoke-virtual {v0}, Landroid/view/View;->getHeight()I

    move-result v0

    iget v3, v2, Landroid/widget/FrameLayout$LayoutParams;->topMargin:I

    add-int/2addr v0, v3

    iget v2, v2, Landroid/widget/FrameLayout$LayoutParams;->bottomMargin:I

    add-int/2addr v0, v2

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getHeight()I

    move-result v2

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingTop()I

    move-result v3

    sub-int/2addr v2, v3

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingBottom()I

    move-result p0

    sub-int/2addr v2, p0

    sub-int/2addr v0, v2

    invoke-static {v1, v0}, Ljava/lang/Math;->max(II)I

    move-result p0

    return p0

    :cond_0
    return v1
.end method""",
        'replacement': """.method getScrollRange()I
    .registers 5

    goto :goto_13

    nop

    :goto_0
    sub-int/2addr v0, v2

    goto :goto_c

    nop

    :goto_1
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingTop()I

    move-result v3

    goto :goto_4

    nop

    :goto_2
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getHeight()I

    move-result v2

    goto :goto_1

    nop

    :goto_3
    iget v2, v2, Landroid/widget/FrameLayout$LayoutParams;->bottomMargin:I

    goto :goto_7

    nop

    :goto_4
    sub-int/2addr v2, v3

    goto :goto_a

    nop

    :goto_5
    invoke-virtual {v0}, Landroid/view/View;->getHeight()I

    move-result v0

    goto :goto_d

    nop

    :goto_6
    invoke-virtual {v0}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v2

    goto :goto_11

    nop

    :goto_7
    add-int/2addr v0, v2

    goto :goto_2

    nop

    :goto_8
    add-int/2addr v0, v3

    goto :goto_3

    nop

    :goto_9
    sub-int/2addr v2, p0

    goto :goto_0

    nop

    :goto_a
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingBottom()I

    move-result p0

    goto :goto_9

    nop

    :goto_b
    const/4 v1, 0x0

    goto :goto_12

    nop

    :goto_c
    invoke-static {v1, v0}, Ljava/lang/Math;->max(II)I

    move-result p0

    goto :goto_e

    nop

    :goto_d
    iget v3, v2, Landroid/widget/FrameLayout$LayoutParams;->topMargin:I

    goto :goto_8

    nop

    :goto_e
    return p0

    :goto_f
    goto :goto_14

    nop

    :goto_10
    invoke-virtual {p0, v1}, Landroid/widget/FrameLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v0

    goto :goto_6

    nop

    :goto_11
    check-cast v2, Landroid/widget/FrameLayout$LayoutParams;

    goto :goto_5

    nop

    :goto_12
    if-gtz v0, :cond_0

    goto :goto_f

    :cond_0
    goto :goto_10

    nop

    :goto_13
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getChildCount()I

    move-result v0

    goto :goto_b

    nop

    :goto_14
    return v1
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_core_widget_NestedScrollView__overScrollByCompat',
        'method': '.method overScrollByCompat(IIIIIIIIZ)Z',
        'method_name': 'overScrollByCompat',
        'method_anchors': ['invoke-virtual {p0}, Landroid/widget/FrameLayout;->getOverScrollMode()I', 'invoke-virtual {p0}, Lmiuix/core/widget/NestedScrollView;->computeHorizontalScrollRange()I', 'invoke-virtual {p0}, Lmiuix/core/widget/NestedScrollView;->computeHorizontalScrollExtent()I', 'if-le v1, v2, :cond_0', 'invoke-virtual {p0}, Lmiuix/core/widget/NestedScrollView;->computeVerticalScrollRange()I', 'invoke-virtual {p0}, Lmiuix/core/widget/NestedScrollView;->computeVerticalScrollExtent()I', 'if-le v2, v5, :cond_1', 'if-eqz v0, :cond_3'],
        'type': 'method_replace',
        'search': """.method overScrollByCompat(IIIIIIIIZ)Z
    .registers 21

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getOverScrollMode()I

    move-result v0

    invoke-virtual {p0}, Lmiuix/core/widget/NestedScrollView;->computeHorizontalScrollRange()I

    move-result v1

    invoke-virtual {p0}, Lmiuix/core/widget/NestedScrollView;->computeHorizontalScrollExtent()I

    move-result v2

    const/4 v3, 0x0

    const/4 v4, 0x1

    if-le v1, v2, :cond_0

    move v1, v4

    goto :goto_0

    :cond_0
    move v1, v3

    :goto_0
    invoke-virtual {p0}, Lmiuix/core/widget/NestedScrollView;->computeVerticalScrollRange()I

    move-result v2

    invoke-virtual {p0}, Lmiuix/core/widget/NestedScrollView;->computeVerticalScrollExtent()I

    move-result v5

    if-le v2, v5, :cond_1

    move v2, v4

    goto :goto_1

    :cond_1
    move v2, v3

    :goto_1
    if-eqz v0, :cond_3

    if-ne v0, v4, :cond_2

    if-eqz v1, :cond_2

    goto :goto_2

    :cond_2
    move v1, v3

    goto :goto_3

    :cond_3
    :goto_2
    move v1, v4

    :goto_3
    if-eqz v0, :cond_5

    if-ne v0, v4, :cond_4

    if-eqz v2, :cond_4

    goto :goto_4

    :cond_4
    move v0, v3

    goto :goto_5

    :cond_5
    :goto_4
    move v0, v4

    :goto_5
    add-int v2, p3, p1

    if-nez v1, :cond_6

    move v1, v3

    goto :goto_6

    :cond_6
    move/from16 v1, p7

    :goto_6
    add-int v5, p4, p2

    if-nez v0, :cond_7

    move v0, v3

    goto :goto_7

    :cond_7
    move/from16 v0, p8

    :goto_7
    neg-int v6, v1

    add-int v1, v1, p5

    neg-int v7, v0

    add-int v0, v0, p6

    if-le v2, v1, :cond_8

    move v2, v1

    move v1, v4

    goto :goto_8

    :cond_8
    if-ge v2, v6, :cond_9

    move v1, v4

    move v2, v6

    goto :goto_8

    :cond_9
    move v1, v3

    :goto_8
    if-le v5, v0, :cond_a

    move v5, v0

    move v0, v4

    goto :goto_9

    :cond_a
    if-ge v5, v7, :cond_b

    move v0, v4

    move v5, v7

    goto :goto_9

    :cond_b
    move v0, v3

    :goto_9
    if-eqz v0, :cond_c

    invoke-virtual {p0, v4}, Lmiuix/core/widget/NestedScrollView;->hasNestedScrollingParent(I)Z

    move-result v6

    if-nez v6, :cond_c

    iget-object v6, p0, Lmiuix/core/widget/NestedScrollView;->mScroller:Lmiuix/overscroller/widget/OverScroller;

    const/4 v7, 0x0

    invoke-virtual {p0}, Lmiuix/core/widget/NestedScrollView;->getScrollRange()I

    move-result v8

    const/4 v9, 0x0

    const/4 v10, 0x0

    move p2, v2

    move p3, v5

    move-object p1, v6

    move/from16 p6, v7

    move/from16 p7, v8

    move p4, v9

    move/from16 p5, v10

    invoke-virtual/range {p1 .. p7}, Lmiuix/overscroller/widget/OverScroller;->springBack(IIIIII)Z

    move v6, p2

    goto :goto_a

    :cond_c
    move v6, v2

    :goto_a
    invoke-virtual {p0, v6, v5, v1, v0}, Lmiuix/core/widget/NestedScrollView;->onOverScrolled(IIZZ)V

    if-nez v1, :cond_e

    if-eqz v0, :cond_d

    goto :goto_b

    :cond_d
    return v3

    :cond_e
    :goto_b
    return v4
.end method""",
        'replacement': """.method overScrollByCompat(IIIIIIIIZ)Z
    .registers 21

    goto :goto_69

    nop

    :goto_0
    move/from16 v1, p7

    :goto_1
    goto :goto_65

    nop

    :goto_2
    if-nez v2, :cond_0

    goto :goto_4d

    :cond_0
    goto :goto_4c

    nop

    :goto_3
    const/4 v9, 0x0

    goto :goto_21

    nop

    :goto_4
    invoke-virtual {p0, v6, v5, v1, v0}, Lmiuix/core/widget/NestedScrollView;->onOverScrolled(IIZZ)V

    goto :goto_61

    nop

    :goto_5
    move v2, v3

    :goto_6
    goto :goto_5b

    nop

    :goto_7
    move v0, v4

    :goto_8
    goto :goto_1a

    nop

    :goto_9
    if-gt v2, v5, :cond_1

    goto :goto_6d

    :cond_1
    goto :goto_3a

    nop

    :goto_a
    move p3, v5

    goto :goto_11

    nop

    :goto_b
    if-eqz v0, :cond_2

    goto :goto_23

    :cond_2
    goto :goto_1b

    nop

    :goto_c
    goto :goto_42

    :goto_d
    goto :goto_41

    nop

    :goto_e
    return v4

    :goto_f
    move v1, v4

    goto :goto_67

    nop

    :goto_10
    if-nez v0, :cond_3

    goto :goto_50

    :cond_3
    goto :goto_4f

    nop

    :goto_11
    move-object p1, v6

    goto :goto_53

    nop

    :goto_12
    invoke-virtual {p0, v4}, Lmiuix/core/widget/NestedScrollView;->hasNestedScrollingParent(I)Z

    move-result v6

    goto :goto_5a

    nop

    :goto_13
    if-gt v1, v2, :cond_4

    goto :goto_60

    :cond_4
    goto :goto_51

    nop

    :goto_14
    const/4 v4, 0x1

    goto :goto_13

    nop

    :goto_15
    return v3

    :goto_16
    goto :goto_e

    nop

    :goto_17
    goto :goto_40

    :goto_18
    goto :goto_2b

    nop

    :goto_19
    invoke-virtual {p0}, Lmiuix/core/widget/NestedScrollView;->computeVerticalScrollRange()I

    move-result v2

    goto :goto_6a

    nop

    :goto_1a
    add-int v2, p3, p1

    goto :goto_59

    nop

    :goto_1b
    move v0, v3

    goto :goto_22

    nop

    :goto_1c
    move v0, v4

    goto :goto_3e

    nop

    :goto_1d
    goto :goto_4b

    :goto_1e
    goto :goto_4a

    nop

    :goto_1f
    const/4 v7, 0x0

    goto :goto_2c

    nop

    :goto_20
    neg-int v7, v0

    goto :goto_58

    nop

    :goto_21
    const/4 v10, 0x0

    goto :goto_3b

    nop

    :goto_22
    goto :goto_29

    :goto_23
    goto :goto_28

    nop

    :goto_24
    goto :goto_1

    :goto_25
    goto :goto_0

    nop

    :goto_26
    if-gt v2, v1, :cond_5

    goto :goto_68

    :cond_5
    goto :goto_52

    nop

    :goto_27
    move v6, p2

    goto :goto_1d

    nop

    :goto_28
    move/from16 v0, p8

    :goto_29
    goto :goto_66

    nop

    :goto_2a
    move v5, v0

    goto :goto_5c

    nop

    :goto_2b
    move v1, v3

    goto :goto_3f

    nop

    :goto_2c
    invoke-virtual {p0}, Lmiuix/core/widget/NestedScrollView;->getScrollRange()I

    move-result v8

    goto :goto_3

    nop

    :goto_2d
    goto :goto_48

    :goto_2e
    goto :goto_3d

    nop

    :goto_2f
    move v1, v4

    :goto_30
    goto :goto_34

    nop

    :goto_31
    if-eq v0, v4, :cond_6

    goto :goto_4d

    :cond_6
    goto :goto_2

    nop

    :goto_32
    const/4 v3, 0x0

    goto :goto_14

    nop

    :goto_33
    move p4, v9

    goto :goto_39

    nop

    :goto_34
    if-nez v0, :cond_7

    goto :goto_57

    :cond_7
    goto :goto_31

    nop

    :goto_35
    move v0, v3

    goto :goto_56

    nop

    :goto_36
    move/from16 p7, v8

    goto :goto_33

    nop

    :goto_37
    if-gt v5, v0, :cond_8

    goto :goto_2e

    :cond_8
    goto :goto_2a

    nop

    :goto_38
    invoke-virtual {p0}, Lmiuix/core/widget/NestedScrollView;->computeHorizontalScrollExtent()I

    move-result v2

    goto :goto_32

    nop

    :goto_39
    move/from16 p5, v10

    goto :goto_64

    nop

    :goto_3a
    move v2, v4

    goto :goto_6c

    nop

    :goto_3b
    move p2, v2

    goto :goto_a

    nop

    :goto_3c
    move v1, v4

    goto :goto_43

    nop

    :goto_3d
    if-lt v5, v7, :cond_9

    goto :goto_55

    :cond_9
    goto :goto_1c

    nop

    :goto_3e
    move v5, v7

    goto :goto_54

    nop

    :goto_3f
    goto :goto_30

    :goto_40
    goto :goto_2f

    nop

    :goto_41
    move v1, v3

    :goto_42
    goto :goto_37

    nop

    :goto_43
    move v2, v6

    goto :goto_c

    nop

    :goto_44
    move v1, v3

    :goto_45
    goto :goto_19

    nop

    :goto_46
    iget-object v6, p0, Lmiuix/core/widget/NestedScrollView;->mScroller:Lmiuix/overscroller/widget/OverScroller;

    goto :goto_1f

    nop

    :goto_47
    move v0, v3

    :goto_48
    goto :goto_63

    nop

    :goto_49
    if-eq v0, v4, :cond_a

    goto :goto_18

    :cond_a
    goto :goto_62

    nop

    :goto_4a
    move v6, v2

    :goto_4b
    goto :goto_4

    nop

    :goto_4c
    goto :goto_57

    :goto_4d
    goto :goto_35

    nop

    :goto_4e
    if-lt v2, v6, :cond_b

    goto :goto_d

    :cond_b
    goto :goto_3c

    nop

    :goto_4f
    goto :goto_16

    :goto_50
    goto :goto_15

    nop

    :goto_51
    move v1, v4

    goto :goto_5f

    nop

    :goto_52
    move v2, v1

    goto :goto_f

    nop

    :goto_53
    move/from16 p6, v7

    goto :goto_36

    nop

    :goto_54
    goto :goto_48

    :goto_55
    goto :goto_47

    nop

    :goto_56
    goto :goto_8

    :goto_57
    goto :goto_7

    nop

    :goto_58
    add-int v0, v0, p6

    goto :goto_26

    nop

    :goto_59
    if-eqz v1, :cond_c

    goto :goto_25

    :cond_c
    goto :goto_5e

    nop

    :goto_5a
    if-eqz v6, :cond_d

    goto :goto_1e

    :cond_d
    goto :goto_46

    nop

    :goto_5b
    if-nez v0, :cond_e

    goto :goto_40

    :cond_e
    goto :goto_49

    nop

    :goto_5c
    move v0, v4

    goto :goto_2d

    nop

    :goto_5d
    add-int v1, v1, p5

    goto :goto_20

    nop

    :goto_5e
    move v1, v3

    goto :goto_24

    nop

    :goto_5f
    goto :goto_45

    :goto_60
    goto :goto_44

    nop

    :goto_61
    if-eqz v1, :cond_f

    goto :goto_16

    :cond_f
    goto :goto_10

    nop

    :goto_62
    if-nez v1, :cond_10

    goto :goto_18

    :cond_10
    goto :goto_17

    nop

    :goto_63
    if-nez v0, :cond_11

    goto :goto_1e

    :cond_11
    goto :goto_12

    nop

    :goto_64
    invoke-virtual/range {p1 .. p7}, Lmiuix/overscroller/widget/OverScroller;->springBack(IIIIII)Z

    goto :goto_27

    nop

    :goto_65
    add-int v5, p4, p2

    goto :goto_b

    nop

    :goto_66
    neg-int v6, v1

    goto :goto_5d

    nop

    :goto_67
    goto :goto_42

    :goto_68
    goto :goto_4e

    nop

    :goto_69
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getOverScrollMode()I

    move-result v0

    goto :goto_6b

    nop

    :goto_6a
    invoke-virtual {p0}, Lmiuix/core/widget/NestedScrollView;->computeVerticalScrollExtent()I

    move-result v5

    goto :goto_9

    nop

    :goto_6b
    invoke-virtual {p0}, Lmiuix/core/widget/NestedScrollView;->computeHorizontalScrollRange()I

    move-result v1

    goto :goto_38

    nop

    :goto_6c
    goto :goto_6

    :goto_6d
    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_core_widget_NestedScrollView__computeScrollDeltaToGetChildRectOnScreen',
        'method': '.method protected computeScrollDeltaToGetChildRectOnScreen(Landroid/graphics/Rect;)I',
        'method_name': 'computeScrollDeltaToGetChildRectOnScreen',
        'method_anchors': ['invoke-virtual {p0}, Landroid/widget/FrameLayout;->getChildCount()I', 'if-nez v0, :cond_0', 'return v1', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->getHeight()I', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->getScrollY()I', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->getVerticalFadingEdgeLength()I', 'iget v5, p1, Landroid/graphics/Rect;->top:I', 'if-lez v5, :cond_1'],
        'type': 'method_replace',
        'search': """.method protected computeScrollDeltaToGetChildRectOnScreen(Landroid/graphics/Rect;)I
    .registers 12

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getChildCount()I

    move-result v0

    const/4 v1, 0x0

    if-nez v0, :cond_0

    return v1

    :cond_0
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getHeight()I

    move-result v0

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getScrollY()I

    move-result v2

    add-int v3, v2, v0

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getVerticalFadingEdgeLength()I

    move-result v4

    iget v5, p1, Landroid/graphics/Rect;->top:I

    if-lez v5, :cond_1

    add-int/2addr v2, v4

    :cond_1
    invoke-virtual {p0, v1}, Landroid/widget/FrameLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v5

    invoke-virtual {v5}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v6

    check-cast v6, Landroid/widget/FrameLayout$LayoutParams;

    iget v7, p1, Landroid/graphics/Rect;->bottom:I

    invoke-virtual {v5}, Landroid/view/View;->getHeight()I

    move-result v8

    iget v9, v6, Landroid/widget/FrameLayout$LayoutParams;->topMargin:I

    add-int/2addr v8, v9

    iget v9, v6, Landroid/widget/FrameLayout$LayoutParams;->bottomMargin:I

    add-int/2addr v8, v9

    if-ge v7, v8, :cond_2

    sub-int v4, v3, v4

    goto :goto_0

    :cond_2
    move v4, v3

    :goto_0
    iget v7, p1, Landroid/graphics/Rect;->bottom:I

    if-le v7, v4, :cond_4

    iget v8, p1, Landroid/graphics/Rect;->top:I

    if-le v8, v2, :cond_4

    invoke-virtual {p1}, Landroid/graphics/Rect;->height()I

    move-result p0

    if-le p0, v0, :cond_3

    iget p0, p1, Landroid/graphics/Rect;->top:I

    sub-int/2addr p0, v2

    goto :goto_1

    :cond_3
    iget p0, p1, Landroid/graphics/Rect;->bottom:I

    sub-int/2addr p0, v4

    :goto_1
    invoke-virtual {v5}, Landroid/view/View;->getBottom()I

    move-result p1

    iget v0, v6, Landroid/widget/FrameLayout$LayoutParams;->bottomMargin:I

    add-int/2addr p1, v0

    sub-int/2addr p1, v3

    invoke-static {p0, p1}, Ljava/lang/Math;->min(II)I

    move-result p0

    return p0

    :cond_4
    iget v3, p1, Landroid/graphics/Rect;->top:I

    if-ge v3, v2, :cond_6

    if-ge v7, v4, :cond_6

    invoke-virtual {p1}, Landroid/graphics/Rect;->height()I

    move-result v3

    if-le v3, v0, :cond_5

    iget p1, p1, Landroid/graphics/Rect;->bottom:I

    sub-int/2addr v4, p1

    sub-int/2addr v1, v4

    goto :goto_2

    :cond_5
    iget p1, p1, Landroid/graphics/Rect;->top:I

    sub-int/2addr v2, p1

    sub-int/2addr v1, v2

    :goto_2
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getScrollY()I

    move-result p0

    neg-int p0, p0

    invoke-static {v1, p0}, Ljava/lang/Math;->max(II)I

    move-result p0

    return p0

    :cond_6
    return v1
.end method""",
        'replacement': """.method protected computeScrollDeltaToGetChildRectOnScreen(Landroid/graphics/Rect;)I
    .registers 12

    goto :goto_20

    nop

    :goto_0
    goto :goto_a

    :goto_1
    goto :goto_2f

    nop

    :goto_2
    invoke-virtual {v5}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v6

    goto :goto_26

    nop

    :goto_3
    invoke-static {v1, p0}, Ljava/lang/Math;->max(II)I

    move-result p0

    goto :goto_1a

    nop

    :goto_4
    iget v8, p1, Landroid/graphics/Rect;->top:I

    goto :goto_25

    nop

    :goto_5
    if-gt p0, v0, :cond_0

    goto :goto_24

    :cond_0
    goto :goto_38

    nop

    :goto_6
    invoke-virtual {p0, v1}, Landroid/widget/FrameLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v5

    goto :goto_2

    nop

    :goto_7
    if-lt v7, v8, :cond_1

    goto :goto_3d

    :cond_1
    goto :goto_27

    nop

    :goto_8
    invoke-virtual {p1}, Landroid/graphics/Rect;->height()I

    move-result p0

    goto :goto_5

    nop

    :goto_9
    sub-int/2addr v1, v2

    :goto_a
    goto :goto_36

    nop

    :goto_b
    sub-int/2addr p0, v2

    goto :goto_23

    nop

    :goto_c
    invoke-virtual {v5}, Landroid/view/View;->getHeight()I

    move-result v8

    goto :goto_19

    nop

    :goto_d
    add-int v3, v2, v0

    goto :goto_43

    nop

    :goto_e
    add-int/2addr v8, v9

    goto :goto_7

    nop

    :goto_f
    const/4 v1, 0x0

    goto :goto_39

    nop

    :goto_10
    invoke-static {p0, p1}, Ljava/lang/Math;->min(II)I

    move-result p0

    goto :goto_3e

    nop

    :goto_11
    iget v3, p1, Landroid/graphics/Rect;->top:I

    goto :goto_2e

    nop

    :goto_12
    if-gt v7, v4, :cond_2

    goto :goto_3f

    :cond_2
    goto :goto_4

    nop

    :goto_13
    add-int/2addr p1, v0

    goto :goto_2a

    nop

    :goto_14
    iget v7, p1, Landroid/graphics/Rect;->bottom:I

    goto :goto_c

    nop

    :goto_15
    invoke-virtual {p1}, Landroid/graphics/Rect;->height()I

    move-result v3

    goto :goto_2d

    nop

    :goto_16
    add-int/2addr v2, v4

    :goto_17
    goto :goto_6

    nop

    :goto_18
    iget p0, p1, Landroid/graphics/Rect;->bottom:I

    goto :goto_1e

    nop

    :goto_19
    iget v9, v6, Landroid/widget/FrameLayout$LayoutParams;->topMargin:I

    goto :goto_40

    nop

    :goto_1a
    return p0

    :goto_1b
    goto :goto_29

    nop

    :goto_1c
    if-gtz v5, :cond_3

    goto :goto_17

    :cond_3
    goto :goto_16

    nop

    :goto_1d
    iget v5, p1, Landroid/graphics/Rect;->top:I

    goto :goto_1c

    nop

    :goto_1e
    sub-int/2addr p0, v4

    :goto_1f
    goto :goto_22

    nop

    :goto_20
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getChildCount()I

    move-result v0

    goto :goto_f

    nop

    :goto_21
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getScrollY()I

    move-result v2

    goto :goto_d

    nop

    :goto_22
    invoke-virtual {v5}, Landroid/view/View;->getBottom()I

    move-result p1

    goto :goto_28

    nop

    :goto_23
    goto :goto_1f

    :goto_24
    goto :goto_18

    nop

    :goto_25
    if-gt v8, v2, :cond_4

    goto :goto_3f

    :cond_4
    goto :goto_8

    nop

    :goto_26
    check-cast v6, Landroid/widget/FrameLayout$LayoutParams;

    goto :goto_14

    nop

    :goto_27
    sub-int v4, v3, v4

    goto :goto_3c

    nop

    :goto_28
    iget v0, v6, Landroid/widget/FrameLayout$LayoutParams;->bottomMargin:I

    goto :goto_13

    nop

    :goto_29
    return v1

    :goto_2a
    sub-int/2addr p1, v3

    goto :goto_10

    nop

    :goto_2b
    sub-int/2addr v2, p1

    goto :goto_9

    nop

    :goto_2c
    neg-int p0, p0

    goto :goto_3

    nop

    :goto_2d
    if-gt v3, v0, :cond_5

    goto :goto_1

    :cond_5
    goto :goto_42

    nop

    :goto_2e
    if-lt v3, v2, :cond_6

    goto :goto_1b

    :cond_6
    goto :goto_37

    nop

    :goto_2f
    iget p1, p1, Landroid/graphics/Rect;->top:I

    goto :goto_2b

    nop

    :goto_30
    iget v9, v6, Landroid/widget/FrameLayout$LayoutParams;->bottomMargin:I

    goto :goto_e

    nop

    :goto_31
    sub-int/2addr v4, p1

    goto :goto_41

    nop

    :goto_32
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getHeight()I

    move-result v0

    goto :goto_21

    nop

    :goto_33
    iget v7, p1, Landroid/graphics/Rect;->bottom:I

    goto :goto_12

    nop

    :goto_34
    move v4, v3

    :goto_35
    goto :goto_33

    nop

    :goto_36
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getScrollY()I

    move-result p0

    goto :goto_2c

    nop

    :goto_37
    if-lt v7, v4, :cond_7

    goto :goto_1b

    :cond_7
    goto :goto_15

    nop

    :goto_38
    iget p0, p1, Landroid/graphics/Rect;->top:I

    goto :goto_b

    nop

    :goto_39
    if-eqz v0, :cond_8

    goto :goto_3b

    :cond_8
    goto :goto_3a

    nop

    :goto_3a
    return v1

    :goto_3b
    goto :goto_32

    nop

    :goto_3c
    goto :goto_35

    :goto_3d
    goto :goto_34

    nop

    :goto_3e
    return p0

    :goto_3f
    goto :goto_11

    nop

    :goto_40
    add-int/2addr v8, v9

    goto :goto_30

    nop

    :goto_41
    sub-int/2addr v1, v4

    goto :goto_0

    nop

    :goto_42
    iget p1, p1, Landroid/graphics/Rect;->bottom:I

    goto :goto_31

    nop

    :goto_43
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getVerticalFadingEdgeLength()I

    move-result v4

    goto :goto_1d

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_core_widget_NestedScrollView__getBottomFadingEdgeStrength',
        'method': '.method protected getBottomFadingEdgeStrength()F',
        'method_name': 'getBottomFadingEdgeStrength',
        'method_anchors': ['invoke-virtual {p0}, Landroid/widget/FrameLayout;->getChildCount()I', 'if-nez v0, :cond_0', 'return p0', 'invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->getChildAt(I)Landroid/view/View;', 'invoke-virtual {v0}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;', 'check-cast v1, Landroid/widget/FrameLayout$LayoutParams;', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->getVerticalFadingEdgeLength()I', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->getHeight()I'],
        'type': 'method_replace',
        'search': """.method protected getBottomFadingEdgeStrength()F
    .registers 6

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getChildCount()I

    move-result v0

    if-nez v0, :cond_0

    const/4 p0, 0x0

    return p0

    :cond_0
    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v0

    invoke-virtual {v0}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v1

    check-cast v1, Landroid/widget/FrameLayout$LayoutParams;

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getVerticalFadingEdgeLength()I

    move-result v2

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getHeight()I

    move-result v3

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingBottom()I

    move-result v4

    sub-int/2addr v3, v4

    invoke-virtual {v0}, Landroid/view/View;->getBottom()I

    move-result v0

    iget v1, v1, Landroid/widget/FrameLayout$LayoutParams;->bottomMargin:I

    add-int/2addr v0, v1

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getScrollY()I

    move-result p0

    sub-int/2addr v0, p0

    sub-int/2addr v0, v3

    if-ge v0, v2, :cond_1

    int-to-float p0, v0

    int-to-float v0, v2

    div-float/2addr p0, v0

    return p0

    :cond_1
    const/high16 p0, 0x3f800000

    return p0
.end method""",
        'replacement': """.method protected getBottomFadingEdgeStrength()F
    .registers 6

    goto :goto_11

    nop

    :goto_0
    const/high16 p0, 0x3f800000

    goto :goto_a

    nop

    :goto_1
    invoke-virtual {v0}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v1

    goto :goto_12

    nop

    :goto_2
    iget v1, v1, Landroid/widget/FrameLayout$LayoutParams;->bottomMargin:I

    goto :goto_6

    nop

    :goto_3
    sub-int/2addr v0, p0

    goto :goto_5

    nop

    :goto_4
    int-to-float p0, v0

    goto :goto_d

    nop

    :goto_5
    sub-int/2addr v0, v3

    goto :goto_c

    nop

    :goto_6
    add-int/2addr v0, v1

    goto :goto_14

    nop

    :goto_7
    sub-int/2addr v3, v4

    goto :goto_8

    nop

    :goto_8
    invoke-virtual {v0}, Landroid/view/View;->getBottom()I

    move-result v0

    goto :goto_2

    nop

    :goto_9
    if-eqz v0, :cond_0

    goto :goto_f

    :cond_0
    goto :goto_16

    nop

    :goto_a
    return p0

    :goto_b
    const/4 v0, 0x0

    goto :goto_19

    nop

    :goto_c
    if-lt v0, v2, :cond_1

    goto :goto_18

    :cond_1
    goto :goto_4

    nop

    :goto_d
    int-to-float v0, v2

    goto :goto_13

    nop

    :goto_e
    return p0

    :goto_f
    goto :goto_b

    nop

    :goto_10
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingBottom()I

    move-result v4

    goto :goto_7

    nop

    :goto_11
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getChildCount()I

    move-result v0

    goto :goto_9

    nop

    :goto_12
    check-cast v1, Landroid/widget/FrameLayout$LayoutParams;

    goto :goto_15

    nop

    :goto_13
    div-float/2addr p0, v0

    goto :goto_17

    nop

    :goto_14
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getScrollY()I

    move-result p0

    goto :goto_3

    nop

    :goto_15
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getVerticalFadingEdgeLength()I

    move-result v2

    goto :goto_1a

    nop

    :goto_16
    const/4 p0, 0x0

    goto :goto_e

    nop

    :goto_17
    return p0

    :goto_18
    goto :goto_0

    nop

    :goto_19
    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v0

    goto :goto_1

    nop

    :goto_1a
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getHeight()I

    move-result v3

    goto :goto_10

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_core_widget_NestedScrollView__getTopFadingEdgeStrength',
        'method': '.method protected getTopFadingEdgeStrength()F',
        'method_name': 'getTopFadingEdgeStrength',
        'method_anchors': ['invoke-virtual {p0}, Landroid/widget/FrameLayout;->getChildCount()I', 'if-nez v0, :cond_0', 'return p0', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->getVerticalFadingEdgeLength()I', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->getScrollY()I', 'if-ge p0, v0, :cond_1', 'return p0', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected getTopFadingEdgeStrength()F
    .registers 2

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getChildCount()I

    move-result v0

    if-nez v0, :cond_0

    const/4 p0, 0x0

    return p0

    :cond_0
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getVerticalFadingEdgeLength()I

    move-result v0

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getScrollY()I

    move-result p0

    if-ge p0, v0, :cond_1

    int-to-float p0, p0

    int-to-float v0, v0

    div-float/2addr p0, v0

    return p0

    :cond_1
    const/high16 p0, 0x3f800000

    return p0
.end method""",
        'replacement': """.method protected getTopFadingEdgeStrength()F
    .registers 2

    goto :goto_a

    nop

    :goto_0
    int-to-float p0, p0

    goto :goto_8

    nop

    :goto_1
    return p0

    :goto_2
    goto :goto_5

    nop

    :goto_3
    if-lt p0, v0, :cond_0

    goto :goto_e

    :cond_0
    goto :goto_0

    nop

    :goto_4
    if-eqz v0, :cond_1

    goto :goto_2

    :cond_1
    goto :goto_7

    nop

    :goto_5
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getVerticalFadingEdgeLength()I

    move-result v0

    goto :goto_c

    nop

    :goto_6
    const/high16 p0, 0x3f800000

    goto :goto_9

    nop

    :goto_7
    const/4 p0, 0x0

    goto :goto_1

    nop

    :goto_8
    int-to-float v0, v0

    goto :goto_b

    nop

    :goto_9
    return p0

    :goto_a
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getChildCount()I

    move-result v0

    goto :goto_4

    nop

    :goto_b
    div-float/2addr p0, v0

    goto :goto_d

    nop

    :goto_c
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getScrollY()I

    move-result p0

    goto :goto_3

    nop

    :goto_d
    return p0

    :goto_e
    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_core_widget_NestedScrollView__measureChild',
        'method': '.method protected measureChild(Landroid/view/View;II)V',
        'method_name': 'measureChild',
        'method_anchors': ['invoke-virtual {p1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingLeft()I', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingRight()I', 'iget p0, p3, Landroid/view/ViewGroup$LayoutParams;->width:I', 'invoke-static {p2, v0, p0}, Landroid/widget/FrameLayout;->getChildMeasureSpec(III)I', 'invoke-static {p2, p2}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I', 'invoke-virtual {p1, p0, p2}, Landroid/view/View;->measure(II)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected measureChild(Landroid/view/View;II)V
    .registers 5

    invoke-virtual {p1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object p3

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingLeft()I

    move-result v0

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingRight()I

    move-result p0

    add-int/2addr v0, p0

    iget p0, p3, Landroid/view/ViewGroup$LayoutParams;->width:I

    invoke-static {p2, v0, p0}, Landroid/widget/FrameLayout;->getChildMeasureSpec(III)I

    move-result p0

    const/4 p2, 0x0

    invoke-static {p2, p2}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p2

    invoke-virtual {p1, p0, p2}, Landroid/view/View;->measure(II)V

    return-void
.end method""",
        'replacement': """.method protected measureChild(Landroid/view/View;II)V
    .registers 5

    goto :goto_3

    nop

    :goto_0
    invoke-virtual {p1, p0, p2}, Landroid/view/View;->measure(II)V

    goto :goto_6

    nop

    :goto_1
    invoke-static {p2, p2}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p2

    goto :goto_0

    nop

    :goto_2
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingRight()I

    move-result p0

    goto :goto_9

    nop

    :goto_3
    invoke-virtual {p1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object p3

    goto :goto_7

    nop

    :goto_4
    iget p0, p3, Landroid/view/ViewGroup$LayoutParams;->width:I

    goto :goto_8

    nop

    :goto_5
    const/4 p2, 0x0

    goto :goto_1

    nop

    :goto_6
    return-void

    :goto_7
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingLeft()I

    move-result v0

    goto :goto_2

    nop

    :goto_8
    invoke-static {p2, v0, p0}, Landroid/widget/FrameLayout;->getChildMeasureSpec(III)I

    move-result p0

    goto :goto_5

    nop

    :goto_9
    add-int/2addr v0, p0

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_core_widget_NestedScrollView__measureChildWithMargins',
        'method': '.method protected measureChildWithMargins(Landroid/view/View;IIII)V',
        'method_name': 'measureChildWithMargins',
        'method_anchors': ['invoke-virtual {p1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;', 'check-cast p4, Landroid/view/ViewGroup$MarginLayoutParams;', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingLeft()I', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingRight()I', 'iget p0, p4, Landroid/view/ViewGroup$MarginLayoutParams;->leftMargin:I', 'iget p0, p4, Landroid/view/ViewGroup$MarginLayoutParams;->rightMargin:I', 'iget p0, p4, Landroid/view/ViewGroup$MarginLayoutParams;->width:I', 'invoke-static {p2, p5, p0}, Landroid/widget/FrameLayout;->getChildMeasureSpec(III)I'],
        'type': 'method_replace',
        'search': """.method protected measureChildWithMargins(Landroid/view/View;IIII)V
    .registers 6

    invoke-virtual {p1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object p4

    check-cast p4, Landroid/view/ViewGroup$MarginLayoutParams;

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingLeft()I

    move-result p5

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingRight()I

    move-result p0

    add-int/2addr p5, p0

    iget p0, p4, Landroid/view/ViewGroup$MarginLayoutParams;->leftMargin:I

    add-int/2addr p5, p0

    iget p0, p4, Landroid/view/ViewGroup$MarginLayoutParams;->rightMargin:I

    add-int/2addr p5, p0

    add-int/2addr p5, p3

    iget p0, p4, Landroid/view/ViewGroup$MarginLayoutParams;->width:I

    invoke-static {p2, p5, p0}, Landroid/widget/FrameLayout;->getChildMeasureSpec(III)I

    move-result p0

    iget p2, p4, Landroid/view/ViewGroup$MarginLayoutParams;->topMargin:I

    iget p3, p4, Landroid/view/ViewGroup$MarginLayoutParams;->bottomMargin:I

    add-int/2addr p2, p3

    const/4 p3, 0x0

    invoke-static {p2, p3}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p2

    invoke-virtual {p1, p0, p2}, Landroid/view/View;->measure(II)V

    return-void
.end method""",
        'replacement': """.method protected measureChildWithMargins(Landroid/view/View;IIII)V
    .registers 6

    goto :goto_b

    nop

    :goto_0
    const/4 p3, 0x0

    goto :goto_a

    nop

    :goto_1
    invoke-static {p2, p5, p0}, Landroid/widget/FrameLayout;->getChildMeasureSpec(III)I

    move-result p0

    goto :goto_11

    nop

    :goto_2
    add-int/2addr p5, p0

    goto :goto_8

    nop

    :goto_3
    check-cast p4, Landroid/view/ViewGroup$MarginLayoutParams;

    goto :goto_10

    nop

    :goto_4
    return-void

    :goto_5
    add-int/2addr p5, p0

    goto :goto_9

    nop

    :goto_6
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingRight()I

    move-result p0

    goto :goto_12

    nop

    :goto_7
    iget p0, p4, Landroid/view/ViewGroup$MarginLayoutParams;->leftMargin:I

    goto :goto_5

    nop

    :goto_8
    add-int/2addr p5, p3

    goto :goto_f

    nop

    :goto_9
    iget p0, p4, Landroid/view/ViewGroup$MarginLayoutParams;->rightMargin:I

    goto :goto_2

    nop

    :goto_a
    invoke-static {p2, p3}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p2

    goto :goto_c

    nop

    :goto_b
    invoke-virtual {p1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object p4

    goto :goto_3

    nop

    :goto_c
    invoke-virtual {p1, p0, p2}, Landroid/view/View;->measure(II)V

    goto :goto_4

    nop

    :goto_d
    add-int/2addr p2, p3

    goto :goto_0

    nop

    :goto_e
    iget p3, p4, Landroid/view/ViewGroup$MarginLayoutParams;->bottomMargin:I

    goto :goto_d

    nop

    :goto_f
    iget p0, p4, Landroid/view/ViewGroup$MarginLayoutParams;->width:I

    goto :goto_1

    nop

    :goto_10
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingLeft()I

    move-result p5

    goto :goto_6

    nop

    :goto_11
    iget p2, p4, Landroid/view/ViewGroup$MarginLayoutParams;->topMargin:I

    goto :goto_e

    nop

    :goto_12
    add-int/2addr p5, p0

    goto :goto_7

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_core_widget_NestedScrollView__onFinishInflate',
        'method': '.method protected onFinishInflate()V',
        'method_name': 'onFinishInflate',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/FrameLayout;->onFinishInflate()V', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingTop()I', 'iput v0, p0, Lmiuix/core/widget/NestedScrollView;->mInitPaddingTop:I', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onFinishInflate()V
    .registers 2

    invoke-super {p0}, Landroid/widget/FrameLayout;->onFinishInflate()V

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingTop()I

    move-result v0

    iput v0, p0, Lmiuix/core/widget/NestedScrollView;->mInitPaddingTop:I

    return-void
.end method""",
        'replacement': """.method protected onFinishInflate()V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingTop()I

    move-result v0

    goto :goto_3

    nop

    :goto_1
    invoke-super {p0}, Landroid/widget/FrameLayout;->onFinishInflate()V

    goto :goto_0

    nop

    :goto_2
    return-void

    :goto_3
    iput v0, p0, Lmiuix/core/widget/NestedScrollView;->mInitPaddingTop:I

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_core_widget_NestedScrollView__onLayout',
        'method': '.method protected onLayout(ZIIII)V',
        'method_name': 'onLayout',
        'method_anchors': ['invoke-super/range {p0 .. p5}, Landroid/widget/FrameLayout;->onLayout(ZIIII)V', 'iput-boolean p1, p0, Lmiuix/core/widget/NestedScrollView;->mIsLayoutDirty:Z', 'iget-object p2, p0, Lmiuix/core/widget/NestedScrollView;->mChildToScrollTo:Landroid/view/View;', 'if-eqz p2, :cond_0', 'invoke-static {p2, p0}, Lmiuix/core/widget/NestedScrollView;->isViewDescendantOf(Landroid/view/View;Landroid/view/View;)Z', 'if-eqz p2, :cond_0', 'iget-object p2, p0, Lmiuix/core/widget/NestedScrollView;->mChildToScrollTo:Landroid/view/View;', 'invoke-direct {p0, p2}, Lmiuix/core/widget/NestedScrollView;->scrollToChild(Landroid/view/View;)V'],
        'type': 'method_replace',
        'search': """.method protected onLayout(ZIIII)V
    .registers 7

    invoke-super/range {p0 .. p5}, Landroid/widget/FrameLayout;->onLayout(ZIIII)V

    const/4 p1, 0x0

    iput-boolean p1, p0, Lmiuix/core/widget/NestedScrollView;->mIsLayoutDirty:Z

    iget-object p2, p0, Lmiuix/core/widget/NestedScrollView;->mChildToScrollTo:Landroid/view/View;

    if-eqz p2, :cond_0

    invoke-static {p2, p0}, Lmiuix/core/widget/NestedScrollView;->isViewDescendantOf(Landroid/view/View;Landroid/view/View;)Z

    move-result p2

    if-eqz p2, :cond_0

    iget-object p2, p0, Lmiuix/core/widget/NestedScrollView;->mChildToScrollTo:Landroid/view/View;

    invoke-direct {p0, p2}, Lmiuix/core/widget/NestedScrollView;->scrollToChild(Landroid/view/View;)V

    :cond_0
    const/4 p2, 0x0

    iput-object p2, p0, Lmiuix/core/widget/NestedScrollView;->mChildToScrollTo:Landroid/view/View;

    iget-boolean p4, p0, Lmiuix/core/widget/NestedScrollView;->mIsLaidOut:Z

    if-nez p4, :cond_3

    iget-object p4, p0, Lmiuix/core/widget/NestedScrollView;->mSavedState:Lmiuix/core/widget/NestedScrollView$SavedState;

    if-eqz p4, :cond_1

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getScrollX()I

    move-result p4

    iget-object v0, p0, Lmiuix/core/widget/NestedScrollView;->mSavedState:Lmiuix/core/widget/NestedScrollView$SavedState;

    iget v0, v0, Lmiuix/core/widget/NestedScrollView$SavedState;->scrollPosition:I

    invoke-virtual {p0, p4, v0}, Lmiuix/core/widget/NestedScrollView;->scrollTo(II)V

    iput-object p2, p0, Lmiuix/core/widget/NestedScrollView;->mSavedState:Lmiuix/core/widget/NestedScrollView$SavedState;

    :cond_1
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getChildCount()I

    move-result p2

    if-lez p2, :cond_2

    invoke-virtual {p0, p1}, Landroid/widget/FrameLayout;->getChildAt(I)Landroid/view/View;

    move-result-object p1

    invoke-virtual {p1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object p2

    check-cast p2, Landroid/widget/FrameLayout$LayoutParams;

    invoke-virtual {p1}, Landroid/view/View;->getMeasuredHeight()I

    move-result p1

    iget p4, p2, Landroid/widget/FrameLayout$LayoutParams;->topMargin:I

    add-int/2addr p1, p4

    iget p2, p2, Landroid/widget/FrameLayout$LayoutParams;->bottomMargin:I

    add-int/2addr p1, p2

    :cond_2
    sub-int/2addr p5, p3

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingTop()I

    move-result p2

    sub-int/2addr p5, p2

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingBottom()I

    move-result p2

    sub-int/2addr p5, p2

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getScrollY()I

    move-result p2

    invoke-static {p2, p5, p1}, Lmiuix/core/widget/NestedScrollView;->clamp(III)I

    move-result p1

    if-eq p1, p2, :cond_3

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getScrollX()I

    move-result p2

    invoke-virtual {p0, p2, p1}, Lmiuix/core/widget/NestedScrollView;->scrollTo(II)V

    :cond_3
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getScrollX()I

    move-result p1

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getScrollY()I

    move-result p2

    invoke-virtual {p0, p1, p2}, Lmiuix/core/widget/NestedScrollView;->scrollTo(II)V

    const/4 p1, 0x1

    iput-boolean p1, p0, Lmiuix/core/widget/NestedScrollView;->mIsLaidOut:Z

    return-void
.end method""",
        'replacement': """.method protected onLayout(ZIIII)V
    .registers 7

    goto :goto_2d

    nop

    :goto_0
    invoke-static {p2, p0}, Lmiuix/core/widget/NestedScrollView;->isViewDescendantOf(Landroid/view/View;Landroid/view/View;)Z

    move-result p2

    goto :goto_1d

    nop

    :goto_1
    invoke-direct {p0, p2}, Lmiuix/core/widget/NestedScrollView;->scrollToChild(Landroid/view/View;)V

    :goto_2
    goto :goto_9

    nop

    :goto_3
    iget p4, p2, Landroid/widget/FrameLayout$LayoutParams;->topMargin:I

    goto :goto_4

    nop

    :goto_4
    add-int/2addr p1, p4

    goto :goto_12

    nop

    :goto_5
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getScrollX()I

    move-result p1

    goto :goto_10

    nop

    :goto_6
    if-gtz p2, :cond_0

    goto :goto_22

    :cond_0
    goto :goto_26

    nop

    :goto_7
    check-cast p2, Landroid/widget/FrameLayout$LayoutParams;

    goto :goto_a

    nop

    :goto_8
    if-nez p4, :cond_1

    goto :goto_2f

    :cond_1
    goto :goto_1e

    nop

    :goto_9
    const/4 p2, 0x0

    goto :goto_30

    nop

    :goto_a
    invoke-virtual {p1}, Landroid/view/View;->getMeasuredHeight()I

    move-result p1

    goto :goto_3

    nop

    :goto_b
    invoke-virtual {p0, p2, p1}, Lmiuix/core/widget/NestedScrollView;->scrollTo(II)V

    :goto_c
    goto :goto_5

    nop

    :goto_d
    iget-object v0, p0, Lmiuix/core/widget/NestedScrollView;->mSavedState:Lmiuix/core/widget/NestedScrollView$SavedState;

    goto :goto_25

    nop

    :goto_e
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getScrollY()I

    move-result p2

    goto :goto_2c

    nop

    :goto_f
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getChildCount()I

    move-result p2

    goto :goto_6

    nop

    :goto_10
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getScrollY()I

    move-result p2

    goto :goto_29

    nop

    :goto_11
    if-nez p2, :cond_2

    goto :goto_2

    :cond_2
    goto :goto_0

    nop

    :goto_12
    iget p2, p2, Landroid/widget/FrameLayout$LayoutParams;->bottomMargin:I

    goto :goto_21

    nop

    :goto_13
    if-eqz p4, :cond_3

    goto :goto_c

    :cond_3
    goto :goto_17

    nop

    :goto_14
    iget-boolean p4, p0, Lmiuix/core/widget/NestedScrollView;->mIsLaidOut:Z

    goto :goto_13

    nop

    :goto_15
    iget-object p2, p0, Lmiuix/core/widget/NestedScrollView;->mChildToScrollTo:Landroid/view/View;

    goto :goto_1

    nop

    :goto_16
    sub-int/2addr p5, p2

    goto :goto_2a

    nop

    :goto_17
    iget-object p4, p0, Lmiuix/core/widget/NestedScrollView;->mSavedState:Lmiuix/core/widget/NestedScrollView$SavedState;

    goto :goto_8

    nop

    :goto_18
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getScrollX()I

    move-result p2

    goto :goto_b

    nop

    :goto_19
    if-ne p1, p2, :cond_4

    goto :goto_c

    :cond_4
    goto :goto_18

    nop

    :goto_1a
    const/4 p1, 0x1

    goto :goto_1b

    nop

    :goto_1b
    iput-boolean p1, p0, Lmiuix/core/widget/NestedScrollView;->mIsLaidOut:Z

    goto :goto_23

    nop

    :goto_1c
    iput-boolean p1, p0, Lmiuix/core/widget/NestedScrollView;->mIsLayoutDirty:Z

    goto :goto_1f

    nop

    :goto_1d
    if-nez p2, :cond_5

    goto :goto_2

    :cond_5
    goto :goto_15

    nop

    :goto_1e
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getScrollX()I

    move-result p4

    goto :goto_d

    nop

    :goto_1f
    iget-object p2, p0, Lmiuix/core/widget/NestedScrollView;->mChildToScrollTo:Landroid/view/View;

    goto :goto_11

    nop

    :goto_20
    invoke-virtual {p0, p4, v0}, Lmiuix/core/widget/NestedScrollView;->scrollTo(II)V

    goto :goto_2e

    nop

    :goto_21
    add-int/2addr p1, p2

    :goto_22
    goto :goto_27

    nop

    :goto_23
    return-void

    :goto_24
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingTop()I

    move-result p2

    goto :goto_16

    nop

    :goto_25
    iget v0, v0, Lmiuix/core/widget/NestedScrollView$SavedState;->scrollPosition:I

    goto :goto_20

    nop

    :goto_26
    invoke-virtual {p0, p1}, Landroid/widget/FrameLayout;->getChildAt(I)Landroid/view/View;

    move-result-object p1

    goto :goto_31

    nop

    :goto_27
    sub-int/2addr p5, p3

    goto :goto_24

    nop

    :goto_28
    sub-int/2addr p5, p2

    goto :goto_e

    nop

    :goto_29
    invoke-virtual {p0, p1, p2}, Lmiuix/core/widget/NestedScrollView;->scrollTo(II)V

    goto :goto_1a

    nop

    :goto_2a
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingBottom()I

    move-result p2

    goto :goto_28

    nop

    :goto_2b
    const/4 p1, 0x0

    goto :goto_1c

    nop

    :goto_2c
    invoke-static {p2, p5, p1}, Lmiuix/core/widget/NestedScrollView;->clamp(III)I

    move-result p1

    goto :goto_19

    nop

    :goto_2d
    invoke-super/range {p0 .. p5}, Landroid/widget/FrameLayout;->onLayout(ZIIII)V

    goto :goto_2b

    nop

    :goto_2e
    iput-object p2, p0, Lmiuix/core/widget/NestedScrollView;->mSavedState:Lmiuix/core/widget/NestedScrollView$SavedState;

    :goto_2f
    goto :goto_f

    nop

    :goto_30
    iput-object p2, p0, Lmiuix/core/widget/NestedScrollView;->mChildToScrollTo:Landroid/view/View;

    goto :goto_14

    nop

    :goto_31
    invoke-virtual {p1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object p2

    goto :goto_7

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_core_widget_NestedScrollView__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['invoke-super {p0, p1, p2}, Landroid/widget/FrameLayout;->onMeasure(II)V', 'iget-boolean v0, p0, Lmiuix/core/widget/NestedScrollView;->mFillViewport:Z', 'if-nez v0, :cond_0', 'invoke-static {p2}, Landroid/view/View$MeasureSpec;->getMode(I)I', 'if-nez p2, :cond_1', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->getChildCount()I', 'if-lez p2, :cond_2', 'invoke-virtual {p0, p2}, Landroid/widget/FrameLayout;->getChildAt(I)Landroid/view/View;'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 7

    invoke-super {p0, p1, p2}, Landroid/widget/FrameLayout;->onMeasure(II)V

    iget-boolean v0, p0, Lmiuix/core/widget/NestedScrollView;->mFillViewport:Z

    if-nez v0, :cond_0

    goto :goto_0

    :cond_0
    invoke-static {p2}, Landroid/view/View$MeasureSpec;->getMode(I)I

    move-result p2

    if-nez p2, :cond_1

    goto :goto_0

    :cond_1
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getChildCount()I

    move-result p2

    if-lez p2, :cond_2

    const/4 p2, 0x0

    invoke-virtual {p0, p2}, Landroid/widget/FrameLayout;->getChildAt(I)Landroid/view/View;

    move-result-object p2

    invoke-virtual {p2}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v0

    check-cast v0, Landroid/widget/FrameLayout$LayoutParams;

    invoke-virtual {p2}, Landroid/view/View;->getMeasuredHeight()I

    move-result v1

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result v2

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingTop()I

    move-result v3

    sub-int/2addr v2, v3

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingBottom()I

    move-result v3

    sub-int/2addr v2, v3

    iget v3, v0, Landroid/widget/FrameLayout$LayoutParams;->topMargin:I

    sub-int/2addr v2, v3

    iget v3, v0, Landroid/widget/FrameLayout$LayoutParams;->bottomMargin:I

    sub-int/2addr v2, v3

    if-ge v1, v2, :cond_2

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingLeft()I

    move-result v1

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingRight()I

    move-result p0

    add-int/2addr v1, p0

    iget p0, v0, Landroid/widget/FrameLayout$LayoutParams;->leftMargin:I

    add-int/2addr v1, p0

    iget p0, v0, Landroid/widget/FrameLayout$LayoutParams;->rightMargin:I

    add-int/2addr v1, p0

    iget p0, v0, Landroid/widget/FrameLayout$LayoutParams;->width:I

    invoke-static {p1, v1, p0}, Landroid/widget/FrameLayout;->getChildMeasureSpec(III)I

    move-result p0

    const/high16 p1, 0x40000000

    invoke-static {v2, p1}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p1

    invoke-virtual {p2, p0, p1}, Landroid/view/View;->measure(II)V

    :cond_2
    :goto_0
    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 7

    goto :goto_1c

    nop

    :goto_0
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingBottom()I

    move-result v3

    goto :goto_27

    nop

    :goto_1
    if-eqz v0, :cond_0

    goto :goto_11

    :cond_0
    goto :goto_10

    nop

    :goto_2
    iget v3, v0, Landroid/widget/FrameLayout$LayoutParams;->bottomMargin:I

    goto :goto_c

    nop

    :goto_3
    if-eqz p2, :cond_1

    goto :goto_20

    :cond_1
    goto :goto_1f

    nop

    :goto_4
    iget p0, v0, Landroid/widget/FrameLayout$LayoutParams;->leftMargin:I

    goto :goto_14

    nop

    :goto_5
    const/high16 p1, 0x40000000

    goto :goto_21

    nop

    :goto_6
    iget v3, v0, Landroid/widget/FrameLayout$LayoutParams;->topMargin:I

    goto :goto_26

    nop

    :goto_7
    const/4 p2, 0x0

    goto :goto_1e

    nop

    :goto_8
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result v2

    goto :goto_e

    nop

    :goto_9
    if-gtz p2, :cond_2

    goto :goto_24

    :cond_2
    goto :goto_7

    nop

    :goto_a
    check-cast v0, Landroid/widget/FrameLayout$LayoutParams;

    goto :goto_12

    nop

    :goto_b
    invoke-static {p1, v1, p0}, Landroid/widget/FrameLayout;->getChildMeasureSpec(III)I

    move-result p0

    goto :goto_5

    nop

    :goto_c
    sub-int/2addr v2, v3

    goto :goto_22

    nop

    :goto_d
    add-int/2addr v1, p0

    goto :goto_4

    nop

    :goto_e
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingTop()I

    move-result v3

    goto :goto_1d

    nop

    :goto_f
    return-void

    :goto_10
    goto :goto_24

    :goto_11
    goto :goto_17

    nop

    :goto_12
    invoke-virtual {p2}, Landroid/view/View;->getMeasuredHeight()I

    move-result v1

    goto :goto_8

    nop

    :goto_13
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getChildCount()I

    move-result p2

    goto :goto_9

    nop

    :goto_14
    add-int/2addr v1, p0

    goto :goto_16

    nop

    :goto_15
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingRight()I

    move-result p0

    goto :goto_d

    nop

    :goto_16
    iget p0, v0, Landroid/widget/FrameLayout$LayoutParams;->rightMargin:I

    goto :goto_1b

    nop

    :goto_17
    invoke-static {p2}, Landroid/view/View$MeasureSpec;->getMode(I)I

    move-result p2

    goto :goto_3

    nop

    :goto_18
    iget-boolean v0, p0, Lmiuix/core/widget/NestedScrollView;->mFillViewport:Z

    goto :goto_1

    nop

    :goto_19
    invoke-virtual {p2}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v0

    goto :goto_a

    nop

    :goto_1a
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingLeft()I

    move-result v1

    goto :goto_15

    nop

    :goto_1b
    add-int/2addr v1, p0

    goto :goto_25

    nop

    :goto_1c
    invoke-super {p0, p1, p2}, Landroid/widget/FrameLayout;->onMeasure(II)V

    goto :goto_18

    nop

    :goto_1d
    sub-int/2addr v2, v3

    goto :goto_0

    nop

    :goto_1e
    invoke-virtual {p0, p2}, Landroid/widget/FrameLayout;->getChildAt(I)Landroid/view/View;

    move-result-object p2

    goto :goto_19

    nop

    :goto_1f
    goto :goto_24

    :goto_20
    goto :goto_13

    nop

    :goto_21
    invoke-static {v2, p1}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p1

    goto :goto_23

    nop

    :goto_22
    if-lt v1, v2, :cond_3

    goto :goto_24

    :cond_3
    goto :goto_1a

    nop

    :goto_23
    invoke-virtual {p2, p0, p1}, Landroid/view/View;->measure(II)V

    :goto_24
    goto :goto_f

    nop

    :goto_25
    iget p0, v0, Landroid/widget/FrameLayout$LayoutParams;->width:I

    goto :goto_b

    nop

    :goto_26
    sub-int/2addr v2, v3

    goto :goto_2

    nop

    :goto_27
    sub-int/2addr v2, v3

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_core_widget_NestedScrollView__onOverScrolled',
        'method': '.method protected onOverScrolled(IIZZ)V',
        'method_name': 'onOverScrolled',
        'method_anchors': ['invoke-super {p0, p1, p2}, Landroid/widget/FrameLayout;->scrollTo(II)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onOverScrolled(IIZZ)V
    .registers 5

    invoke-super {p0, p1, p2}, Landroid/widget/FrameLayout;->scrollTo(II)V

    return-void
.end method""",
        'replacement': """.method protected onOverScrolled(IIZZ)V
    .registers 5

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0, p1, p2}, Landroid/widget/FrameLayout;->scrollTo(II)V

    goto :goto_1

    nop

    :goto_1
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_core_widget_NestedScrollView__onRequestFocusInDescendants',
        'method': '.method protected onRequestFocusInDescendants(ILandroid/graphics/Rect;)Z',
        'method_name': 'onRequestFocusInDescendants',
        'method_anchors': ['if-ne p1, v0, :cond_0', 'if-ne p1, v0, :cond_1', 'if-nez p2, :cond_2', 'invoke-static {}, Landroid/view/FocusFinder;->getInstance()Landroid/view/FocusFinder;', 'invoke-virtual {v0, p0, v1, p1}, Landroid/view/FocusFinder;->findNextFocus(Landroid/view/ViewGroup;Landroid/view/View;I)Landroid/view/View;', 'invoke-static {}, Landroid/view/FocusFinder;->getInstance()Landroid/view/FocusFinder;', 'invoke-virtual {v0, p0, p2, p1}, Landroid/view/FocusFinder;->findNextFocusFromRect(Landroid/view/ViewGroup;Landroid/graphics/Rect;I)Landroid/view/View;', 'if-nez v0, :cond_3'],
        'type': 'method_replace',
        'search': """.method protected onRequestFocusInDescendants(ILandroid/graphics/Rect;)Z
    .registers 5

    const/4 v0, 0x2

    if-ne p1, v0, :cond_0

    const/16 p1, 0x82

    goto :goto_0

    :cond_0
    const/4 v0, 0x1

    if-ne p1, v0, :cond_1

    const/16 p1, 0x21

    :cond_1
    :goto_0
    if-nez p2, :cond_2

    invoke-static {}, Landroid/view/FocusFinder;->getInstance()Landroid/view/FocusFinder;

    move-result-object v0

    const/4 v1, 0x0

    invoke-virtual {v0, p0, v1, p1}, Landroid/view/FocusFinder;->findNextFocus(Landroid/view/ViewGroup;Landroid/view/View;I)Landroid/view/View;

    move-result-object v0

    goto :goto_1

    :cond_2
    invoke-static {}, Landroid/view/FocusFinder;->getInstance()Landroid/view/FocusFinder;

    move-result-object v0

    invoke-virtual {v0, p0, p2, p1}, Landroid/view/FocusFinder;->findNextFocusFromRect(Landroid/view/ViewGroup;Landroid/graphics/Rect;I)Landroid/view/View;

    move-result-object v0

    :goto_1
    const/4 v1, 0x0

    if-nez v0, :cond_3

    return v1

    :cond_3
    invoke-direct {p0, v0}, Lmiuix/core/widget/NestedScrollView;->isOffScreen(Landroid/view/View;)Z

    move-result p0

    if-eqz p0, :cond_4

    return v1

    :cond_4
    invoke-virtual {v0, p1, p2}, Landroid/view/View;->requestFocus(ILandroid/graphics/Rect;)Z

    move-result p0

    return p0
.end method""",
        'replacement': """.method protected onRequestFocusInDescendants(ILandroid/graphics/Rect;)Z
    .registers 5

    goto :goto_10

    nop

    :goto_0
    return v1

    :goto_1
    goto :goto_3

    nop

    :goto_2
    const/4 v1, 0x0

    goto :goto_11

    nop

    :goto_3
    invoke-direct {p0, v0}, Lmiuix/core/widget/NestedScrollView;->isOffScreen(Landroid/view/View;)Z

    move-result p0

    goto :goto_c

    nop

    :goto_4
    invoke-static {}, Landroid/view/FocusFinder;->getInstance()Landroid/view/FocusFinder;

    move-result-object v0

    goto :goto_6

    nop

    :goto_5
    if-eqz v0, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_0

    nop

    :goto_6
    invoke-virtual {v0, p0, p2, p1}, Landroid/view/FocusFinder;->findNextFocusFromRect(Landroid/view/ViewGroup;Landroid/graphics/Rect;I)Landroid/view/View;

    move-result-object v0

    :goto_7
    goto :goto_d

    nop

    :goto_8
    invoke-virtual {v0, p1, p2}, Landroid/view/View;->requestFocus(ILandroid/graphics/Rect;)Z

    move-result p0

    goto :goto_1b

    nop

    :goto_9
    if-eq p1, v0, :cond_1

    goto :goto_17

    :cond_1
    goto :goto_f

    nop

    :goto_a
    const/16 p1, 0x21

    :goto_b
    goto :goto_13

    nop

    :goto_c
    if-nez p0, :cond_2

    goto :goto_15

    :cond_2
    goto :goto_14

    nop

    :goto_d
    const/4 v1, 0x0

    goto :goto_5

    nop

    :goto_e
    invoke-static {}, Landroid/view/FocusFinder;->getInstance()Landroid/view/FocusFinder;

    move-result-object v0

    goto :goto_2

    nop

    :goto_f
    const/16 p1, 0x82

    goto :goto_16

    nop

    :goto_10
    const/4 v0, 0x2

    goto :goto_9

    nop

    :goto_11
    invoke-virtual {v0, p0, v1, p1}, Landroid/view/FocusFinder;->findNextFocus(Landroid/view/ViewGroup;Landroid/view/View;I)Landroid/view/View;

    move-result-object v0

    goto :goto_18

    nop

    :goto_12
    if-eq p1, v0, :cond_3

    goto :goto_b

    :cond_3
    goto :goto_a

    nop

    :goto_13
    if-eqz p2, :cond_4

    goto :goto_19

    :cond_4
    goto :goto_e

    nop

    :goto_14
    return v1

    :goto_15
    goto :goto_8

    nop

    :goto_16
    goto :goto_b

    :goto_17
    goto :goto_1a

    nop

    :goto_18
    goto :goto_7

    :goto_19
    goto :goto_4

    nop

    :goto_1a
    const/4 v0, 0x1

    goto :goto_12

    nop

    :goto_1b
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_core_widget_NestedScrollView__onRestoreInstanceState',
        'method': '.method protected onRestoreInstanceState(Landroid/os/Parcelable;)V',
        'method_name': 'onRestoreInstanceState',
        'method_anchors': ['if-nez v0, :cond_0', 'invoke-super {p0, p1}, Landroid/widget/FrameLayout;->onRestoreInstanceState(Landroid/os/Parcelable;)V', 'return-void', 'check-cast p1, Lmiuix/core/widget/NestedScrollView$SavedState;', 'invoke-virtual {p1}, Landroid/view/View$BaseSavedState;->getSuperState()Landroid/os/Parcelable;', 'invoke-super {p0, v0}, Landroid/widget/FrameLayout;->onRestoreInstanceState(Landroid/os/Parcelable;)V', 'iput-object p1, p0, Lmiuix/core/widget/NestedScrollView;->mSavedState:Lmiuix/core/widget/NestedScrollView$SavedState;', 'invoke-virtual {p0}, Lmiuix/core/widget/NestedScrollView;->requestLayout()V'],
        'type': 'method_replace',
        'search': """.method protected onRestoreInstanceState(Landroid/os/Parcelable;)V
    .registers 3

    instance-of v0, p1, Lmiuix/core/widget/NestedScrollView$SavedState;

    if-nez v0, :cond_0

    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->onRestoreInstanceState(Landroid/os/Parcelable;)V

    return-void

    :cond_0
    check-cast p1, Lmiuix/core/widget/NestedScrollView$SavedState;

    invoke-virtual {p1}, Landroid/view/View$BaseSavedState;->getSuperState()Landroid/os/Parcelable;

    move-result-object v0

    invoke-super {p0, v0}, Landroid/widget/FrameLayout;->onRestoreInstanceState(Landroid/os/Parcelable;)V

    iput-object p1, p0, Lmiuix/core/widget/NestedScrollView;->mSavedState:Lmiuix/core/widget/NestedScrollView$SavedState;

    invoke-virtual {p0}, Lmiuix/core/widget/NestedScrollView;->requestLayout()V

    return-void
.end method""",
        'replacement': """.method protected onRestoreInstanceState(Landroid/os/Parcelable;)V
    .registers 3

    goto :goto_8

    nop

    :goto_0
    if-eqz v0, :cond_0

    goto :goto_a

    :cond_0
    goto :goto_6

    nop

    :goto_1
    invoke-super {p0, v0}, Landroid/widget/FrameLayout;->onRestoreInstanceState(Landroid/os/Parcelable;)V

    goto :goto_4

    nop

    :goto_2
    check-cast p1, Lmiuix/core/widget/NestedScrollView$SavedState;

    goto :goto_5

    nop

    :goto_3
    return-void

    :goto_4
    iput-object p1, p0, Lmiuix/core/widget/NestedScrollView;->mSavedState:Lmiuix/core/widget/NestedScrollView$SavedState;

    goto :goto_7

    nop

    :goto_5
    invoke-virtual {p1}, Landroid/view/View$BaseSavedState;->getSuperState()Landroid/os/Parcelable;

    move-result-object v0

    goto :goto_1

    nop

    :goto_6
    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->onRestoreInstanceState(Landroid/os/Parcelable;)V

    goto :goto_9

    nop

    :goto_7
    invoke-virtual {p0}, Lmiuix/core/widget/NestedScrollView;->requestLayout()V

    goto :goto_3

    nop

    :goto_8
    instance-of v0, p1, Lmiuix/core/widget/NestedScrollView$SavedState;

    goto :goto_0

    nop

    :goto_9
    return-void

    :goto_a
    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_core_widget_NestedScrollView__onSaveInstanceState',
        'method': '.method protected onSaveInstanceState()Landroid/os/Parcelable;',
        'method_name': 'onSaveInstanceState',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/FrameLayout;->onSaveInstanceState()Landroid/os/Parcelable;', 'new-instance v1, Lmiuix/core/widget/NestedScrollView$SavedState;', 'invoke-direct {v1, v0}, Lmiuix/core/widget/NestedScrollView$SavedState;-><init>(Landroid/os/Parcelable;)V', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->getScrollY()I', 'iput p0, v1, Lmiuix/core/widget/NestedScrollView$SavedState;->scrollPosition:I', 'return-object v1'],
        'type': 'method_replace',
        'search': """.method protected onSaveInstanceState()Landroid/os/Parcelable;
    .registers 3

    invoke-super {p0}, Landroid/widget/FrameLayout;->onSaveInstanceState()Landroid/os/Parcelable;

    move-result-object v0

    new-instance v1, Lmiuix/core/widget/NestedScrollView$SavedState;

    invoke-direct {v1, v0}, Lmiuix/core/widget/NestedScrollView$SavedState;-><init>(Landroid/os/Parcelable;)V

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getScrollY()I

    move-result p0

    iput p0, v1, Lmiuix/core/widget/NestedScrollView$SavedState;->scrollPosition:I

    return-object v1
.end method""",
        'replacement': """.method protected onSaveInstanceState()Landroid/os/Parcelable;
    .registers 3

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0}, Landroid/widget/FrameLayout;->onSaveInstanceState()Landroid/os/Parcelable;

    move-result-object v0

    goto :goto_2

    nop

    :goto_1
    invoke-direct {v1, v0}, Lmiuix/core/widget/NestedScrollView$SavedState;-><init>(Landroid/os/Parcelable;)V

    goto :goto_3

    nop

    :goto_2
    new-instance v1, Lmiuix/core/widget/NestedScrollView$SavedState;

    goto :goto_1

    nop

    :goto_3
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getScrollY()I

    move-result p0

    goto :goto_5

    nop

    :goto_4
    return-object v1

    :goto_5
    iput p0, v1, Lmiuix/core/widget/NestedScrollView$SavedState;->scrollPosition:I

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_core_widget_NestedScrollView__onScrollChanged',
        'method': '.method protected onScrollChanged(IIII)V',
        'method_name': 'onScrollChanged',
        'method_anchors': ['invoke-super {p0, p1, p2, p3, p4}, Landroid/widget/FrameLayout;->onScrollChanged(IIII)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onScrollChanged(IIII)V
    .registers 5

    invoke-super {p0, p1, p2, p3, p4}, Landroid/widget/FrameLayout;->onScrollChanged(IIII)V

    return-void
.end method""",
        'replacement': """.method protected onScrollChanged(IIII)V
    .registers 5

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0, p1, p2, p3, p4}, Landroid/widget/FrameLayout;->onScrollChanged(IIII)V

    goto :goto_1

    nop

    :goto_1
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_core_widget_NestedScrollView__onSizeChanged',
        'method': '.method protected onSizeChanged(IIII)V',
        'method_name': 'onSizeChanged',
        'method_anchors': ['invoke-super {p0, p1, p2, p3, p4}, Landroid/widget/FrameLayout;->onSizeChanged(IIII)V', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->findFocus()Landroid/view/View;', 'if-eqz p1, :cond_1', 'if-ne p0, p1, :cond_0', 'invoke-static {p1, p0}, Lmiuix/core/widget/NestedScrollView;->isViewDescendantOf(Landroid/view/View;Landroid/view/View;)Z', 'if-eqz p2, :cond_1', 'invoke-direct {p0, p1, p2, p4}, Lmiuix/core/widget/NestedScrollView;->isWithinDeltaOfScreen(Landroid/view/View;II)Z', 'if-eqz p2, :cond_1'],
        'type': 'method_replace',
        'search': """.method protected onSizeChanged(IIII)V
    .registers 5

    invoke-super {p0, p1, p2, p3, p4}, Landroid/widget/FrameLayout;->onSizeChanged(IIII)V

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->findFocus()Landroid/view/View;

    move-result-object p1

    if-eqz p1, :cond_1

    if-ne p0, p1, :cond_0

    goto :goto_0

    :cond_0
    invoke-static {p1, p0}, Lmiuix/core/widget/NestedScrollView;->isViewDescendantOf(Landroid/view/View;Landroid/view/View;)Z

    move-result p2

    if-eqz p2, :cond_1

    const/4 p2, 0x0

    invoke-direct {p0, p1, p2, p4}, Lmiuix/core/widget/NestedScrollView;->isWithinDeltaOfScreen(Landroid/view/View;II)Z

    move-result p2

    if-eqz p2, :cond_1

    iget-object p2, p0, Lmiuix/core/widget/NestedScrollView;->mTempRect:Landroid/graphics/Rect;

    invoke-virtual {p1, p2}, Landroid/view/View;->getDrawingRect(Landroid/graphics/Rect;)V

    iget-object p2, p0, Lmiuix/core/widget/NestedScrollView;->mTempRect:Landroid/graphics/Rect;

    invoke-virtual {p0, p1, p2}, Landroid/widget/FrameLayout;->offsetDescendantRectToMyCoords(Landroid/view/View;Landroid/graphics/Rect;)V

    iget-object p1, p0, Lmiuix/core/widget/NestedScrollView;->mTempRect:Landroid/graphics/Rect;

    invoke-virtual {p0, p1}, Lmiuix/core/widget/NestedScrollView;->computeScrollDeltaToGetChildRectOnScreen(Landroid/graphics/Rect;)I

    move-result p1

    invoke-direct {p0, p1}, Lmiuix/core/widget/NestedScrollView;->doScrollY(I)V

    :cond_1
    :goto_0
    return-void
.end method""",
        'replacement': """.method protected onSizeChanged(IIII)V
    .registers 5

    goto :goto_2

    nop

    :goto_0
    invoke-virtual {p0, p1, p2}, Landroid/widget/FrameLayout;->offsetDescendantRectToMyCoords(Landroid/view/View;Landroid/graphics/Rect;)V

    goto :goto_8

    nop

    :goto_1
    return-void

    :goto_2
    invoke-super {p0, p1, p2, p3, p4}, Landroid/widget/FrameLayout;->onSizeChanged(IIII)V

    goto :goto_e

    nop

    :goto_3
    goto :goto_12

    :goto_4
    goto :goto_10

    nop

    :goto_5
    if-nez p2, :cond_0

    goto :goto_12

    :cond_0
    goto :goto_f

    nop

    :goto_6
    invoke-virtual {p0, p1}, Lmiuix/core/widget/NestedScrollView;->computeScrollDeltaToGetChildRectOnScreen(Landroid/graphics/Rect;)I

    move-result p1

    goto :goto_11

    nop

    :goto_7
    if-nez p1, :cond_1

    goto :goto_12

    :cond_1
    goto :goto_9

    nop

    :goto_8
    iget-object p1, p0, Lmiuix/core/widget/NestedScrollView;->mTempRect:Landroid/graphics/Rect;

    goto :goto_6

    nop

    :goto_9
    if-eq p0, p1, :cond_2

    goto :goto_4

    :cond_2
    goto :goto_3

    nop

    :goto_a
    iget-object p2, p0, Lmiuix/core/widget/NestedScrollView;->mTempRect:Landroid/graphics/Rect;

    goto :goto_0

    nop

    :goto_b
    invoke-direct {p0, p1, p2, p4}, Lmiuix/core/widget/NestedScrollView;->isWithinDeltaOfScreen(Landroid/view/View;II)Z

    move-result p2

    goto :goto_13

    nop

    :goto_c
    invoke-virtual {p1, p2}, Landroid/view/View;->getDrawingRect(Landroid/graphics/Rect;)V

    goto :goto_a

    nop

    :goto_d
    iget-object p2, p0, Lmiuix/core/widget/NestedScrollView;->mTempRect:Landroid/graphics/Rect;

    goto :goto_c

    nop

    :goto_e
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->findFocus()Landroid/view/View;

    move-result-object p1

    goto :goto_7

    nop

    :goto_f
    const/4 p2, 0x0

    goto :goto_b

    nop

    :goto_10
    invoke-static {p1, p0}, Lmiuix/core/widget/NestedScrollView;->isViewDescendantOf(Landroid/view/View;Landroid/view/View;)Z

    move-result p2

    goto :goto_5

    nop

    :goto_11
    invoke-direct {p0, p1}, Lmiuix/core/widget/NestedScrollView;->doScrollY(I)V

    :goto_12
    goto :goto_1

    nop

    :goto_13
    if-nez p2, :cond_3

    goto :goto_12

    :cond_3
    goto :goto_d

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_core_widget_NestedScrollView__smoothScrollTo',
        'method': '.method smoothScrollTo(IIZ)V',
        'method_name': 'smoothScrollTo',
        'method_anchors': ['invoke-virtual {p0}, Landroid/widget/FrameLayout;->getScrollX()I', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->getScrollY()I', 'invoke-direct {p0, p1, p2, p3}, Lmiuix/core/widget/NestedScrollView;->smoothScrollBy(IIZ)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method smoothScrollTo(IIZ)V
    .registers 5

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getScrollX()I

    move-result v0

    sub-int/2addr p1, v0

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getScrollY()I

    move-result v0

    sub-int/2addr p2, v0

    invoke-direct {p0, p1, p2, p3}, Lmiuix/core/widget/NestedScrollView;->smoothScrollBy(IIZ)V

    return-void
.end method""",
        'replacement': """.method smoothScrollTo(IIZ)V
    .registers 5

    goto :goto_5

    nop

    :goto_0
    invoke-direct {p0, p1, p2, p3}, Lmiuix/core/widget/NestedScrollView;->smoothScrollBy(IIZ)V

    goto :goto_3

    nop

    :goto_1
    sub-int/2addr p1, v0

    goto :goto_4

    nop

    :goto_2
    sub-int/2addr p2, v0

    goto :goto_0

    nop

    :goto_3
    return-void

    :goto_4
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getScrollY()I

    move-result v0

    goto :goto_2

    nop

    :goto_5
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getScrollX()I

    move-result v0

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
