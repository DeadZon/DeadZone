TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/pickerwidget/internal/widget/ProperPaddingViewGroup.smali'
CLASS_FALLBACK_NAMES = ['ProperPaddingViewGroup.smali']
CLASS_ANCHORS = ['.super Landroid/view/ViewGroup;']

PATCHES = [
    {
        'id': 'miuix_pickerwidget_internal_widget_ProperPaddingViewGroup__onFinishInflate',
        'method': '.method protected onFinishInflate()V',
        'method_name': 'onFinishInflate',
        'method_anchors': ['invoke-super {p0}, Landroid/view/ViewGroup;->onFinishInflate()V', 'invoke-virtual {p0}, Landroid/view/ViewGroup;->getChildCount()I', 'if-gt v0, v1, :cond_0', 'invoke-virtual {p0, v0}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;', 'iput-object v0, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mChildView:Landroid/view/View;', 'return-void', 'new-instance p0, Ljava/lang/IllegalStateException;', 'const-string v0, "Only one child view can be added into the ProperPaddingViewGroup!"'],
        'type': 'method_replace',
        'search': """.method protected onFinishInflate()V
    .registers 3

    invoke-super {p0}, Landroid/view/ViewGroup;->onFinishInflate()V

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getChildCount()I

    move-result v0

    const/4 v1, 0x1

    if-gt v0, v1, :cond_0

    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;

    move-result-object v0

    iput-object v0, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mChildView:Landroid/view/View;

    return-void

    :cond_0
    new-instance p0, Ljava/lang/IllegalStateException;

    const-string v0, "Only one child view can be added into the ProperPaddingViewGroup!"

    invoke-direct {p0, v0}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    throw p0
.end method""",
        'replacement': """.method protected onFinishInflate()V
    .registers 3

    goto :goto_7

    nop

    :goto_0
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getChildCount()I

    move-result v0

    goto :goto_b

    nop

    :goto_1
    return-void

    :goto_2
    goto :goto_5

    nop

    :goto_3
    throw p0

    :goto_4
    const/4 v0, 0x0

    goto :goto_8

    nop

    :goto_5
    new-instance p0, Ljava/lang/IllegalStateException;

    goto :goto_6

    nop

    :goto_6
    const-string v0, "Only one child view can be added into the ProperPaddingViewGroup!"

    goto :goto_9

    nop

    :goto_7
    invoke-super {p0}, Landroid/view/ViewGroup;->onFinishInflate()V

    goto :goto_0

    nop

    :goto_8
    invoke-virtual {p0, v0}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;

    move-result-object v0

    goto :goto_a

    nop

    :goto_9
    invoke-direct {p0, v0}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    goto :goto_3

    nop

    :goto_a
    iput-object v0, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mChildView:Landroid/view/View;

    goto :goto_1

    nop

    :goto_b
    const/4 v1, 0x1

    goto :goto_c

    nop

    :goto_c
    if-le v0, v1, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_pickerwidget_internal_widget_ProperPaddingViewGroup__onLayout',
        'method': '.method protected onLayout(ZIIII)V',
        'method_name': 'onLayout',
        'method_anchors': ['invoke-static {p0}, Lmiuix/internal/util/ViewUtils;->isLayoutRtl(Landroid/view/View;)Z', 'if-eqz p1, :cond_0', 'iget p1, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mPaddingEnd:I', 'iget p1, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mPaddingStart:I', 'iget-object p2, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mChildView:Landroid/view/View;', 'invoke-virtual {p2}, Landroid/view/View;->getMeasuredWidth()I', 'iget-object p3, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mChildView:Landroid/view/View;', 'invoke-virtual {p3}, Landroid/view/View;->getMeasuredHeight()I'],
        'type': 'method_replace',
        'search': """.method protected onLayout(ZIIII)V
    .registers 6

    invoke-static {p0}, Lmiuix/internal/util/ViewUtils;->isLayoutRtl(Landroid/view/View;)Z

    move-result p1

    if-eqz p1, :cond_0

    iget p1, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mPaddingEnd:I

    goto :goto_0

    :cond_0
    iget p1, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mPaddingStart:I

    :goto_0
    iget-object p2, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mChildView:Landroid/view/View;

    invoke-virtual {p2}, Landroid/view/View;->getMeasuredWidth()I

    move-result p2

    add-int/2addr p2, p1

    iget-object p3, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mChildView:Landroid/view/View;

    invoke-virtual {p3}, Landroid/view/View;->getMeasuredHeight()I

    move-result p3

    iget-object p0, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mChildView:Landroid/view/View;

    const/4 p4, 0x0

    invoke-virtual {p0, p1, p4, p2, p3}, Landroid/view/View;->layout(IIII)V

    return-void
.end method""",
        'replacement': """.method protected onLayout(ZIIII)V
    .registers 6

    goto :goto_b

    nop

    :goto_0
    add-int/2addr p2, p1

    goto :goto_4

    nop

    :goto_1
    const/4 p4, 0x0

    goto :goto_3

    nop

    :goto_2
    iget-object p0, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mChildView:Landroid/view/View;

    goto :goto_1

    nop

    :goto_3
    invoke-virtual {p0, p1, p4, p2, p3}, Landroid/view/View;->layout(IIII)V

    goto :goto_5

    nop

    :goto_4
    iget-object p3, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mChildView:Landroid/view/View;

    goto :goto_6

    nop

    :goto_5
    return-void

    :goto_6
    invoke-virtual {p3}, Landroid/view/View;->getMeasuredHeight()I

    move-result p3

    goto :goto_2

    nop

    :goto_7
    if-nez p1, :cond_0

    goto :goto_f

    :cond_0
    goto :goto_a

    nop

    :goto_8
    iget p1, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mPaddingStart:I

    :goto_9
    goto :goto_c

    nop

    :goto_a
    iget p1, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mPaddingEnd:I

    goto :goto_e

    nop

    :goto_b
    invoke-static {p0}, Lmiuix/internal/util/ViewUtils;->isLayoutRtl(Landroid/view/View;)Z

    move-result p1

    goto :goto_7

    nop

    :goto_c
    iget-object p2, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mChildView:Landroid/view/View;

    goto :goto_d

    nop

    :goto_d
    invoke-virtual {p2}, Landroid/view/View;->getMeasuredWidth()I

    move-result p2

    goto :goto_0

    nop

    :goto_e
    goto :goto_9

    :goto_f
    goto :goto_8

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_pickerwidget_internal_widget_ProperPaddingViewGroup__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['invoke-static {p1}, Landroid/view/View$MeasureSpec;->getSize(I)I', 'iget v2, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->DENSITY:F', 'iget-boolean v4, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mFixedHorizontalPadding:Z', 'if-eqz v4, :cond_0', 'iget v1, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mFixedHorizontalPaddingStart:I', 'iput v1, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mPaddingStart:I', 'iget v1, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mFixedHorizontalPaddingEnd:I', 'iput v1, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mPaddingEnd:I'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 9

    invoke-static {p1}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v0

    int-to-float v1, v0

    iget v2, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->DENSITY:F

    div-float v3, v1, v2

    iget-boolean v4, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mFixedHorizontalPadding:Z

    const/4 v5, 0x0

    if-eqz v4, :cond_0

    iget v1, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mFixedHorizontalPaddingStart:I

    iput v1, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mPaddingStart:I

    iget v1, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mFixedHorizontalPaddingEnd:I

    iput v1, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mPaddingEnd:I

    goto :goto_0

    :cond_0
    const/high16 v4, 0x43aa0000

    cmpg-float v3, v3, v4

    if-gtz v3, :cond_2

    const/high16 v3, 0x43910000

    mul-float/2addr v2, v3

    sub-float/2addr v1, v2

    float-to-int v1, v1

    div-int/lit8 v1, v1, 0x2

    if-gez v1, :cond_1

    move v1, v5

    :cond_1
    iget v2, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mSmallHorizontalPaddingStart:I

    div-int/lit8 v1, v1, 0x2

    add-int/2addr v2, v1

    iput v2, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mPaddingStart:I

    iget v2, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mSmallHorizontalPaddingEnd:I

    add-int/2addr v2, v1

    iput v2, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mPaddingEnd:I

    goto :goto_0

    :cond_2
    iget v1, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mHorizontalPaddingStart:I

    iput v1, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mPaddingStart:I

    iget v1, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mHorizontalPaddingEnd:I

    iput v1, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mPaddingEnd:I

    :goto_0
    iget-object v1, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mChildView:Landroid/view/View;

    invoke-virtual {v1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v1

    iget-object v2, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mChildView:Landroid/view/View;

    iget v3, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mPaddingStart:I

    iget v4, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mPaddingEnd:I

    add-int/2addr v3, v4

    iget v1, v1, Landroid/view/ViewGroup$LayoutParams;->width:I

    invoke-static {p1, v3, v1}, Landroid/view/ViewGroup;->getChildMeasureSpec(III)I

    move-result p1

    iget-object v1, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mChildView:Landroid/view/View;

    invoke-virtual {v1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v1

    iget v1, v1, Landroid/view/ViewGroup$LayoutParams;->height:I

    invoke-static {p2, v5, v1}, Landroid/view/ViewGroup;->getChildMeasureSpec(III)I

    move-result p2

    invoke-virtual {v2, p1, p2}, Landroid/view/View;->measure(II)V

    iget-object p1, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mChildView:Landroid/view/View;

    invoke-virtual {p1}, Landroid/view/View;->getMeasuredHeight()I

    move-result p1

    invoke-virtual {p0, v0, p1}, Landroid/view/ViewGroup;->setMeasuredDimension(II)V

    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 9

    goto :goto_1a

    nop

    :goto_0
    float-to-int v1, v1

    goto :goto_32

    nop

    :goto_1
    iget v1, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mFixedHorizontalPaddingStart:I

    goto :goto_36

    nop

    :goto_2
    const/high16 v4, 0x43aa0000

    goto :goto_a

    nop

    :goto_3
    iget-object v2, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mChildView:Landroid/view/View;

    goto :goto_22

    nop

    :goto_4
    iget-boolean v4, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mFixedHorizontalPadding:Z

    goto :goto_1e

    nop

    :goto_5
    invoke-virtual {p1}, Landroid/view/View;->getMeasuredHeight()I

    move-result p1

    goto :goto_21

    nop

    :goto_6
    if-nez v4, :cond_0

    goto :goto_29

    :cond_0
    goto :goto_1

    nop

    :goto_7
    add-int/2addr v3, v4

    goto :goto_25

    nop

    :goto_8
    add-int/2addr v2, v1

    goto :goto_c

    nop

    :goto_9
    iget v1, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mFixedHorizontalPaddingEnd:I

    goto :goto_35

    nop

    :goto_a
    cmpg-float v3, v3, v4

    goto :goto_34

    nop

    :goto_b
    iget v2, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->DENSITY:F

    goto :goto_16

    nop

    :goto_c
    iput v2, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mPaddingEnd:I

    goto :goto_13

    nop

    :goto_d
    int-to-float v1, v0

    goto :goto_b

    nop

    :goto_e
    iget v2, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mSmallHorizontalPaddingEnd:I

    goto :goto_8

    nop

    :goto_f
    iget v1, v1, Landroid/view/ViewGroup$LayoutParams;->height:I

    goto :goto_31

    nop

    :goto_10
    invoke-virtual {v1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v1

    goto :goto_3

    nop

    :goto_11
    iget v2, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mSmallHorizontalPaddingStart:I

    goto :goto_2b

    nop

    :goto_12
    mul-float/2addr v2, v3

    goto :goto_1d

    nop

    :goto_13
    goto :goto_30

    :goto_14
    goto :goto_2a

    nop

    :goto_15
    return-void

    :goto_16
    div-float v3, v1, v2

    goto :goto_4

    nop

    :goto_17
    iget v4, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mPaddingEnd:I

    goto :goto_7

    nop

    :goto_18
    add-int/2addr v2, v1

    goto :goto_2e

    nop

    :goto_19
    const/high16 v3, 0x43910000

    goto :goto_12

    nop

    :goto_1a
    invoke-static {p1}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v0

    goto :goto_d

    nop

    :goto_1b
    if-ltz v1, :cond_1

    goto :goto_20

    :cond_1
    goto :goto_1f

    nop

    :goto_1c
    invoke-virtual {v2, p1, p2}, Landroid/view/View;->measure(II)V

    goto :goto_26

    nop

    :goto_1d
    sub-float/2addr v1, v2

    goto :goto_0

    nop

    :goto_1e
    const/4 v5, 0x0

    goto :goto_6

    nop

    :goto_1f
    move v1, v5

    :goto_20
    goto :goto_11

    nop

    :goto_21
    invoke-virtual {p0, v0, p1}, Landroid/view/ViewGroup;->setMeasuredDimension(II)V

    goto :goto_15

    nop

    :goto_22
    iget v3, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mPaddingStart:I

    goto :goto_17

    nop

    :goto_23
    invoke-virtual {v1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v1

    goto :goto_f

    nop

    :goto_24
    iget v1, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mHorizontalPaddingEnd:I

    goto :goto_2f

    nop

    :goto_25
    iget v1, v1, Landroid/view/ViewGroup$LayoutParams;->width:I

    goto :goto_33

    nop

    :goto_26
    iget-object p1, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mChildView:Landroid/view/View;

    goto :goto_5

    nop

    :goto_27
    iget-object v1, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mChildView:Landroid/view/View;

    goto :goto_10

    nop

    :goto_28
    goto :goto_30

    :goto_29
    goto :goto_2

    nop

    :goto_2a
    iget v1, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mHorizontalPaddingStart:I

    goto :goto_2d

    nop

    :goto_2b
    div-int/lit8 v1, v1, 0x2

    goto :goto_18

    nop

    :goto_2c
    iget-object v1, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mChildView:Landroid/view/View;

    goto :goto_23

    nop

    :goto_2d
    iput v1, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mPaddingStart:I

    goto :goto_24

    nop

    :goto_2e
    iput v2, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mPaddingStart:I

    goto :goto_e

    nop

    :goto_2f
    iput v1, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mPaddingEnd:I

    :goto_30
    goto :goto_27

    nop

    :goto_31
    invoke-static {p2, v5, v1}, Landroid/view/ViewGroup;->getChildMeasureSpec(III)I

    move-result p2

    goto :goto_1c

    nop

    :goto_32
    div-int/lit8 v1, v1, 0x2

    goto :goto_1b

    nop

    :goto_33
    invoke-static {p1, v3, v1}, Landroid/view/ViewGroup;->getChildMeasureSpec(III)I

    move-result p1

    goto :goto_2c

    nop

    :goto_34
    if-lez v3, :cond_2

    goto :goto_14

    :cond_2
    goto :goto_19

    nop

    :goto_35
    iput v1, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mPaddingEnd:I

    goto :goto_28

    nop

    :goto_36
    iput v1, p0, Lmiuix/pickerwidget/internal/widget/ProperPaddingViewGroup;->mPaddingStart:I

    goto :goto_9

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
