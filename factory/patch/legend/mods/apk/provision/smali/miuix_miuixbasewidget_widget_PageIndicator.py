TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/miuixbasewidget/widget/PageIndicator.smali'
CLASS_FALLBACK_NAMES = ['PageIndicator.smali']
CLASS_ANCHORS = ['.super Landroid/view/View;']

PATCHES = [
    {
        'id': 'miuix_miuixbasewidget_widget_PageIndicator__onDraw',
        'method': '.method protected onDraw(Landroid/graphics/Canvas;)V',
        'method_name': 'onDraw',
        'method_anchors': ['invoke-static {p0}, Lmiuix/internal/util/ViewUtils;->isLayoutRtl(Landroid/view/View;)Z', 'iput-boolean v0, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mIsRtl:Z', 'iget v1, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mHorizontalPadding:I', 'iget v2, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mIndicatorRadius:F', 'iget v3, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mVerticalPadding:F', 'if-eqz v0, :cond_2', 'iget v0, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mIndicatorCount:I', 'if-ge v2, v0, :cond_5'],
        'type': 'method_replace',
        'search': """.method protected onDraw(Landroid/graphics/Canvas;)V
    .registers 12

    invoke-static {p0}, Lmiuix/internal/util/ViewUtils;->isLayoutRtl(Landroid/view/View;)Z

    move-result v0

    iput-boolean v0, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mIsRtl:Z

    iget v1, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mHorizontalPadding:I

    int-to-float v1, v1

    iget v2, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mIndicatorRadius:F

    add-float/2addr v1, v2

    iget v3, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mVerticalPadding:F

    add-float v7, v3, v2

    const/4 v2, 0x0

    if-eqz v0, :cond_2

    move v6, v1

    :goto_0
    iget v0, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mIndicatorCount:I

    if-ge v2, v0, :cond_5

    iget v1, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mCurrentPosition:I

    sub-int v3, v0, v1

    add-int/lit8 v3, v3, -0x1

    if-ne v2, v3, :cond_0

    iget-object v0, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mEvaluator:Landroidx/vectordrawable/graphics/drawable/ArgbEvaluator;

    iget v1, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mCurrentPositionOffset:F

    iget v3, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mSelectedColor:I

    invoke-static {v3}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v3

    iget v4, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mUnselectedColor:I

    invoke-static {v4}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v4

    invoke-virtual {v0, v1, v3, v4}, Landroidx/vectordrawable/graphics/drawable/ArgbEvaluator;->evaluate(FLjava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Ljava/lang/Integer;

    invoke-virtual {v0}, Ljava/lang/Integer;->intValue()I

    move-result v0

    :goto_1
    move v9, v0

    goto :goto_2

    :cond_0
    sub-int/2addr v0, v1

    add-int/lit8 v0, v0, -0x2

    if-ne v2, v0, :cond_1

    iget-object v0, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mEvaluator:Landroidx/vectordrawable/graphics/drawable/ArgbEvaluator;

    iget v1, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mCurrentPositionOffset:F

    iget v3, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mUnselectedColor:I

    invoke-static {v3}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v3

    iget v4, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mSelectedColor:I

    invoke-static {v4}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v4

    invoke-virtual {v0, v1, v3, v4}, Landroidx/vectordrawable/graphics/drawable/ArgbEvaluator;->evaluate(FLjava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Ljava/lang/Integer;

    invoke-virtual {v0}, Ljava/lang/Integer;->intValue()I

    move-result v0

    goto :goto_1

    :cond_1
    iget v0, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mUnselectedColor:I

    goto :goto_1

    :goto_2
    iget v8, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mIndicatorRadius:F

    move-object v4, p0

    move-object v5, p1

    invoke-direct/range {v4 .. v9}, Lmiuix/miuixbasewidget/widget/PageIndicator;->drawIndicator(Landroid/graphics/Canvas;FFFI)V

    iget p0, v4, Lmiuix/miuixbasewidget/widget/PageIndicator;->mIndicatorInterval:F

    add-float/2addr v6, p0

    add-int/lit8 v2, v2, 0x1

    move-object p0, v4

    goto :goto_0

    :cond_2
    move-object v4, p0

    move-object v5, p1

    move v6, v1

    :goto_3
    iget p0, v4, Lmiuix/miuixbasewidget/widget/PageIndicator;->mIndicatorCount:I

    if-ge v2, p0, :cond_5

    iget p0, v4, Lmiuix/miuixbasewidget/widget/PageIndicator;->mCurrentPosition:I

    if-ne v2, p0, :cond_3

    iget-object p0, v4, Lmiuix/miuixbasewidget/widget/PageIndicator;->mEvaluator:Landroidx/vectordrawable/graphics/drawable/ArgbEvaluator;

    iget p1, v4, Lmiuix/miuixbasewidget/widget/PageIndicator;->mCurrentPositionOffset:F

    iget v0, v4, Lmiuix/miuixbasewidget/widget/PageIndicator;->mSelectedColor:I

    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    iget v1, v4, Lmiuix/miuixbasewidget/widget/PageIndicator;->mUnselectedColor:I

    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    invoke-virtual {p0, p1, v0, v1}, Landroidx/vectordrawable/graphics/drawable/ArgbEvaluator;->evaluate(FLjava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    check-cast p0, Ljava/lang/Integer;

    invoke-virtual {p0}, Ljava/lang/Integer;->intValue()I

    move-result p0

    :goto_4
    move v9, p0

    goto :goto_5

    :cond_3
    add-int/lit8 p0, p0, 0x1

    if-ne v2, p0, :cond_4

    iget-object p0, v4, Lmiuix/miuixbasewidget/widget/PageIndicator;->mEvaluator:Landroidx/vectordrawable/graphics/drawable/ArgbEvaluator;

    iget p1, v4, Lmiuix/miuixbasewidget/widget/PageIndicator;->mCurrentPositionOffset:F

    iget v0, v4, Lmiuix/miuixbasewidget/widget/PageIndicator;->mUnselectedColor:I

    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    iget v1, v4, Lmiuix/miuixbasewidget/widget/PageIndicator;->mSelectedColor:I

    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    invoke-virtual {p0, p1, v0, v1}, Landroidx/vectordrawable/graphics/drawable/ArgbEvaluator;->evaluate(FLjava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    check-cast p0, Ljava/lang/Integer;

    invoke-virtual {p0}, Ljava/lang/Integer;->intValue()I

    move-result p0

    goto :goto_4

    :cond_4
    iget p0, v4, Lmiuix/miuixbasewidget/widget/PageIndicator;->mUnselectedColor:I

    goto :goto_4

    :goto_5
    iget v8, v4, Lmiuix/miuixbasewidget/widget/PageIndicator;->mIndicatorRadius:F

    invoke-direct/range {v4 .. v9}, Lmiuix/miuixbasewidget/widget/PageIndicator;->drawIndicator(Landroid/graphics/Canvas;FFFI)V

    iget p0, v4, Lmiuix/miuixbasewidget/widget/PageIndicator;->mIndicatorInterval:F

    add-float/2addr v6, p0

    add-int/lit8 v2, v2, 0x1

    goto :goto_3

    :cond_5
    return-void
.end method""",
        'replacement': """.method protected onDraw(Landroid/graphics/Canvas;)V
    .registers 12

    goto :goto_12

    nop

    :goto_0
    invoke-virtual {v0}, Ljava/lang/Integer;->intValue()I

    move-result v0

    goto :goto_41

    nop

    :goto_1
    iget p1, v4, Lmiuix/miuixbasewidget/widget/PageIndicator;->mCurrentPositionOffset:F

    goto :goto_11

    nop

    :goto_2
    iget p0, v4, Lmiuix/miuixbasewidget/widget/PageIndicator;->mIndicatorCount:I

    goto :goto_5

    nop

    :goto_3
    add-int/lit8 v2, v2, 0x1

    goto :goto_33

    nop

    :goto_4
    add-float/2addr v6, p0

    goto :goto_3

    nop

    :goto_5
    if-lt v2, p0, :cond_0

    goto :goto_4b

    :cond_0
    goto :goto_46

    nop

    :goto_6
    invoke-virtual {p0, p1, v0, v1}, Landroidx/vectordrawable/graphics/drawable/ArgbEvaluator;->evaluate(FLjava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    goto :goto_37

    nop

    :goto_7
    iget v2, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mIndicatorRadius:F

    goto :goto_8

    nop

    :goto_8
    add-float/2addr v1, v2

    goto :goto_2a

    nop

    :goto_9
    invoke-direct/range {v4 .. v9}, Lmiuix/miuixbasewidget/widget/PageIndicator;->drawIndicator(Landroid/graphics/Canvas;FFFI)V

    goto :goto_19

    nop

    :goto_a
    check-cast v0, Ljava/lang/Integer;

    goto :goto_0

    nop

    :goto_b
    goto :goto_32

    :goto_c
    goto :goto_66

    nop

    :goto_d
    iget v8, v4, Lmiuix/miuixbasewidget/widget/PageIndicator;->mIndicatorRadius:F

    goto :goto_9

    nop

    :goto_e
    move-object v5, p1

    goto :goto_23

    nop

    :goto_f
    goto :goto_2d

    :goto_10
    goto :goto_4d

    nop

    :goto_11
    iget v0, v4, Lmiuix/miuixbasewidget/widget/PageIndicator;->mSelectedColor:I

    goto :goto_54

    nop

    :goto_12
    invoke-static {p0}, Lmiuix/internal/util/ViewUtils;->isLayoutRtl(Landroid/view/View;)Z

    move-result v0

    goto :goto_17

    nop

    :goto_13
    move-object v5, p1

    goto :goto_21

    nop

    :goto_14
    sub-int/2addr v0, v1

    goto :goto_1b

    nop

    :goto_15
    goto :goto_1e

    :goto_16
    goto :goto_45

    nop

    :goto_17
    iput-boolean v0, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mIsRtl:Z

    goto :goto_64

    nop

    :goto_18
    invoke-static {v3}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v3

    goto :goto_40

    nop

    :goto_19
    iget p0, v4, Lmiuix/miuixbasewidget/widget/PageIndicator;->mIndicatorInterval:F

    goto :goto_3f

    nop

    :goto_1a
    iget v1, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mCurrentPositionOffset:F

    goto :goto_5b

    nop

    :goto_1b
    add-int/lit8 v0, v0, -0x2

    goto :goto_38

    nop

    :goto_1c
    int-to-float v1, v1

    goto :goto_7

    nop

    :goto_1d
    move v6, v1

    :goto_1e
    goto :goto_55

    nop

    :goto_1f
    invoke-static {v4}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v4

    goto :goto_51

    nop

    :goto_20
    invoke-virtual {p0}, Ljava/lang/Integer;->intValue()I

    move-result p0

    goto :goto_34

    nop

    :goto_21
    move v6, v1

    :goto_22
    goto :goto_2

    nop

    :goto_23
    invoke-direct/range {v4 .. v9}, Lmiuix/miuixbasewidget/widget/PageIndicator;->drawIndicator(Landroid/graphics/Canvas;FFFI)V

    goto :goto_5e

    nop

    :goto_24
    iget v0, v4, Lmiuix/miuixbasewidget/widget/PageIndicator;->mUnselectedColor:I

    goto :goto_5f

    nop

    :goto_25
    if-lt v2, v0, :cond_1

    goto :goto_4b

    :cond_1
    goto :goto_28

    nop

    :goto_26
    iget v1, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mCurrentPositionOffset:F

    goto :goto_58

    nop

    :goto_27
    iget-object p0, v4, Lmiuix/miuixbasewidget/widget/PageIndicator;->mEvaluator:Landroidx/vectordrawable/graphics/drawable/ArgbEvaluator;

    goto :goto_1

    nop

    :goto_28
    iget v1, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mCurrentPosition:I

    goto :goto_2e

    nop

    :goto_29
    return-void

    :goto_2a
    iget v3, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mVerticalPadding:F

    goto :goto_5a

    nop

    :goto_2b
    move v9, p0

    goto :goto_b

    nop

    :goto_2c
    invoke-virtual {v0}, Ljava/lang/Integer;->intValue()I

    move-result v0

    :goto_2d
    goto :goto_48

    nop

    :goto_2e
    sub-int v3, v0, v1

    goto :goto_53

    nop

    :goto_2f
    iget v1, v4, Lmiuix/miuixbasewidget/widget/PageIndicator;->mUnselectedColor:I

    goto :goto_4c

    nop

    :goto_30
    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    goto :goto_44

    nop

    :goto_31
    goto :goto_5d

    :goto_32
    goto :goto_d

    nop

    :goto_33
    move-object p0, v4

    goto :goto_15

    nop

    :goto_34
    goto :goto_5d

    :goto_35
    goto :goto_57

    nop

    :goto_36
    add-int/lit8 v2, v2, 0x1

    goto :goto_4a

    nop

    :goto_37
    check-cast p0, Ljava/lang/Integer;

    goto :goto_5c

    nop

    :goto_38
    if-eq v2, v0, :cond_2

    goto :goto_42

    :cond_2
    goto :goto_3a

    nop

    :goto_39
    iget-object v0, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mEvaluator:Landroidx/vectordrawable/graphics/drawable/ArgbEvaluator;

    goto :goto_1a

    nop

    :goto_3a
    iget-object v0, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mEvaluator:Landroidx/vectordrawable/graphics/drawable/ArgbEvaluator;

    goto :goto_26

    nop

    :goto_3b
    if-eq v2, v3, :cond_3

    goto :goto_4f

    :cond_3
    goto :goto_39

    nop

    :goto_3c
    iget p1, v4, Lmiuix/miuixbasewidget/widget/PageIndicator;->mCurrentPositionOffset:F

    goto :goto_24

    nop

    :goto_3d
    invoke-static {v4}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v4

    goto :goto_43

    nop

    :goto_3e
    check-cast v0, Ljava/lang/Integer;

    goto :goto_2c

    nop

    :goto_3f
    add-float/2addr v6, p0

    goto :goto_36

    nop

    :goto_40
    iget v4, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mUnselectedColor:I

    goto :goto_3d

    nop

    :goto_41
    goto :goto_2d

    :goto_42
    goto :goto_60

    nop

    :goto_43
    invoke-virtual {v0, v1, v3, v4}, Landroidx/vectordrawable/graphics/drawable/ArgbEvaluator;->evaluate(FLjava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    goto :goto_3e

    nop

    :goto_44
    invoke-virtual {p0, p1, v0, v1}, Landroidx/vectordrawable/graphics/drawable/ArgbEvaluator;->evaluate(FLjava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    goto :goto_63

    nop

    :goto_45
    move-object v4, p0

    goto :goto_13

    nop

    :goto_46
    iget p0, v4, Lmiuix/miuixbasewidget/widget/PageIndicator;->mCurrentPosition:I

    goto :goto_52

    nop

    :goto_47
    if-nez v0, :cond_4

    goto :goto_16

    :cond_4
    goto :goto_1d

    nop

    :goto_48
    move v9, v0

    goto :goto_4e

    nop

    :goto_49
    if-eq v2, p0, :cond_5

    goto :goto_35

    :cond_5
    goto :goto_61

    nop

    :goto_4a
    goto :goto_22

    :goto_4b
    goto :goto_29

    nop

    :goto_4c
    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    goto :goto_6

    nop

    :goto_4d
    iget v8, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mIndicatorRadius:F

    goto :goto_62

    nop

    :goto_4e
    goto :goto_10

    :goto_4f
    goto :goto_14

    nop

    :goto_50
    iget v4, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mSelectedColor:I

    goto :goto_1f

    nop

    :goto_51
    invoke-virtual {v0, v1, v3, v4}, Landroidx/vectordrawable/graphics/drawable/ArgbEvaluator;->evaluate(FLjava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    goto :goto_a

    nop

    :goto_52
    if-eq v2, p0, :cond_6

    goto :goto_c

    :cond_6
    goto :goto_27

    nop

    :goto_53
    add-int/lit8 v3, v3, -0x1

    goto :goto_3b

    nop

    :goto_54
    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    goto :goto_2f

    nop

    :goto_55
    iget v0, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mIndicatorCount:I

    goto :goto_25

    nop

    :goto_56
    const/4 v2, 0x0

    goto :goto_47

    nop

    :goto_57
    iget p0, v4, Lmiuix/miuixbasewidget/widget/PageIndicator;->mUnselectedColor:I

    goto :goto_31

    nop

    :goto_58
    iget v3, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mUnselectedColor:I

    goto :goto_59

    nop

    :goto_59
    invoke-static {v3}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v3

    goto :goto_50

    nop

    :goto_5a
    add-float v7, v3, v2

    goto :goto_56

    nop

    :goto_5b
    iget v3, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mSelectedColor:I

    goto :goto_18

    nop

    :goto_5c
    invoke-virtual {p0}, Ljava/lang/Integer;->intValue()I

    move-result p0

    :goto_5d
    goto :goto_2b

    nop

    :goto_5e
    iget p0, v4, Lmiuix/miuixbasewidget/widget/PageIndicator;->mIndicatorInterval:F

    goto :goto_4

    nop

    :goto_5f
    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    goto :goto_65

    nop

    :goto_60
    iget v0, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mUnselectedColor:I

    goto :goto_f

    nop

    :goto_61
    iget-object p0, v4, Lmiuix/miuixbasewidget/widget/PageIndicator;->mEvaluator:Landroidx/vectordrawable/graphics/drawable/ArgbEvaluator;

    goto :goto_3c

    nop

    :goto_62
    move-object v4, p0

    goto :goto_e

    nop

    :goto_63
    check-cast p0, Ljava/lang/Integer;

    goto :goto_20

    nop

    :goto_64
    iget v1, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mHorizontalPadding:I

    goto :goto_1c

    nop

    :goto_65
    iget v1, v4, Lmiuix/miuixbasewidget/widget/PageIndicator;->mSelectedColor:I

    goto :goto_30

    nop

    :goto_66
    add-int/lit8 p0, p0, 0x1

    goto :goto_49

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_miuixbasewidget_widget_PageIndicator__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['iget p1, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mIndicatorCount:I', 'iget p2, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mIndicatorInterval:F', 'iget p2, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mIndicatorRadius:F', 'iget v1, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mHorizontalPadding:I', 'iget v1, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mVerticalPadding:F', 'invoke-virtual {p0, p1, p2}, Landroid/view/View;->setMeasuredDimension(II)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 5

    iget p1, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mIndicatorCount:I

    add-int/lit8 p1, p1, -0x1

    int-to-float p1, p1

    iget p2, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mIndicatorInterval:F

    mul-float/2addr p1, p2

    iget p2, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mIndicatorRadius:F

    const/high16 v0, 0x40000000

    mul-float v1, p2, v0

    add-float/2addr p1, v1

    iget v1, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mHorizontalPadding:I

    mul-int/lit8 v1, v1, 0x2

    int-to-float v1, v1

    add-float/2addr p1, v1

    float-to-int p1, p1

    mul-float/2addr p2, v0

    iget v1, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mVerticalPadding:F

    mul-float/2addr v1, v0

    add-float/2addr p2, v1

    float-to-int p2, p2

    invoke-virtual {p0, p1, p2}, Landroid/view/View;->setMeasuredDimension(II)V

    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 5

    goto :goto_1

    nop

    :goto_0
    add-float/2addr p2, v1

    goto :goto_4

    nop

    :goto_1
    iget p1, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mIndicatorCount:I

    goto :goto_3

    nop

    :goto_2
    mul-float/2addr p1, p2

    goto :goto_10

    nop

    :goto_3
    add-int/lit8 p1, p1, -0x1

    goto :goto_7

    nop

    :goto_4
    float-to-int p2, p2

    goto :goto_9

    nop

    :goto_5
    mul-float/2addr v1, v0

    goto :goto_0

    nop

    :goto_6
    return-void

    :goto_7
    int-to-float p1, p1

    goto :goto_12

    nop

    :goto_8
    add-float/2addr p1, v1

    goto :goto_14

    nop

    :goto_9
    invoke-virtual {p0, p1, p2}, Landroid/view/View;->setMeasuredDimension(II)V

    goto :goto_6

    nop

    :goto_a
    iget v1, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mVerticalPadding:F

    goto :goto_5

    nop

    :goto_b
    mul-int/lit8 v1, v1, 0x2

    goto :goto_c

    nop

    :goto_c
    int-to-float v1, v1

    goto :goto_11

    nop

    :goto_d
    mul-float v1, p2, v0

    goto :goto_8

    nop

    :goto_e
    const/high16 v0, 0x40000000

    goto :goto_d

    nop

    :goto_f
    float-to-int p1, p1

    goto :goto_13

    nop

    :goto_10
    iget p2, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mIndicatorRadius:F

    goto :goto_e

    nop

    :goto_11
    add-float/2addr p1, v1

    goto :goto_f

    nop

    :goto_12
    iget p2, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mIndicatorInterval:F

    goto :goto_2

    nop

    :goto_13
    mul-float/2addr p2, v0

    goto :goto_a

    nop

    :goto_14
    iget v1, p0, Lmiuix/miuixbasewidget/widget/PageIndicator;->mHorizontalPadding:I

    goto :goto_b

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
