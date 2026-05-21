TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/popupwidget/internal/widget/GuidePopupView.smali'
CLASS_FALLBACK_NAMES = ['GuidePopupView.smali']
CLASS_ANCHORS = ['.super Landroid/widget/FrameLayout;', '.implements Landroid/view/View$OnTouchListener;']

PATCHES = [
    {
        'id': 'miuix_popupwidget_internal_widget_GuidePopupView__dispatchDraw',
        'method': '.method protected dispatchDraw(Landroid/graphics/Canvas;)V',
        'method_name': 'dispatchDraw',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/widget/FrameLayout;->dispatchDraw(Landroid/graphics/Canvas;)V', 'invoke-virtual {p1}, Landroid/graphics/Canvas;->save()I', 'iget v0, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mAnchorLocationX:I', 'iget v1, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mAnchorLocationY:I', 'invoke-virtual {p1, v0, v1}, Landroid/graphics/Canvas;->translate(FF)V', 'iget-object v0, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mAnchor:Landroid/view/View;', 'invoke-virtual {v0, v1}, Landroid/view/View;->setDrawingCacheEnabled(Z)V', 'iget-object v0, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mAnchor:Landroid/view/View;'],
        'type': 'method_replace',
        'search': """.method protected dispatchDraw(Landroid/graphics/Canvas;)V
    .registers 5

    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->dispatchDraw(Landroid/graphics/Canvas;)V

    invoke-virtual {p1}, Landroid/graphics/Canvas;->save()I

    iget v0, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mAnchorLocationX:I

    int-to-float v0, v0

    iget v1, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mAnchorLocationY:I

    int-to-float v1, v1

    invoke-virtual {p1, v0, v1}, Landroid/graphics/Canvas;->translate(FF)V

    iget-object v0, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mAnchor:Landroid/view/View;

    const/4 v1, 0x1

    invoke-virtual {v0, v1}, Landroid/view/View;->setDrawingCacheEnabled(Z)V

    iget-object v0, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mAnchor:Landroid/view/View;

    invoke-virtual {v0}, Landroid/view/View;->buildDrawingCache()V

    iget-object v0, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mAnchor:Landroid/view/View;

    invoke-virtual {v0}, Landroid/view/View;->getDrawingCache()Landroid/graphics/Bitmap;

    move-result-object v0

    if-eqz v0, :cond_0

    const/4 v1, 0x0

    const/4 v2, 0x0

    invoke-virtual {p1, v0, v2, v2, v1}, Landroid/graphics/Canvas;->drawBitmap(Landroid/graphics/Bitmap;FFLandroid/graphics/Paint;)V

    :cond_0
    iget-object v0, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mAnchor:Landroid/view/View;

    const/4 v1, 0x0

    invoke-virtual {v0, v1}, Landroid/view/View;->setDrawingCacheEnabled(Z)V

    invoke-virtual {p1}, Landroid/graphics/Canvas;->restore()V

    iget v0, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mArrowMode:I

    iget v1, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mOffsetX:I

    iget v2, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mOffsetY:I

    invoke-direct {p0, p1, v0, v1, v2}, Lmiuix/popupwidget/internal/widget/GuidePopupView;->drawPopup(Landroid/graphics/Canvas;III)V

    iget-boolean v0, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mIsMirrored:Z

    if-eqz v0, :cond_1

    invoke-direct {p0}, Lmiuix/popupwidget/internal/widget/GuidePopupView;->getMirroredMode()I

    move-result v0

    iget v1, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mOffsetX:I

    neg-int v1, v1

    iget v2, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mOffsetY:I

    neg-int v2, v2

    invoke-direct {p0, p1, v0, v1, v2}, Lmiuix/popupwidget/internal/widget/GuidePopupView;->drawPopup(Landroid/graphics/Canvas;III)V

    :cond_1
    return-void
.end method""",
        'replacement': """.method protected dispatchDraw(Landroid/graphics/Canvas;)V
    .registers 5

    goto :goto_3

    nop

    :goto_0
    iget v2, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mOffsetY:I

    goto :goto_1f

    nop

    :goto_1
    invoke-virtual {v0, v1}, Landroid/view/View;->setDrawingCacheEnabled(Z)V

    goto :goto_b

    nop

    :goto_2
    iget v0, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mArrowMode:I

    goto :goto_17

    nop

    :goto_3
    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->dispatchDraw(Landroid/graphics/Canvas;)V

    goto :goto_20

    nop

    :goto_4
    iget v1, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mOffsetX:I

    goto :goto_21

    nop

    :goto_5
    invoke-direct {p0, p1, v0, v1, v2}, Lmiuix/popupwidget/internal/widget/GuidePopupView;->drawPopup(Landroid/graphics/Canvas;III)V

    :goto_6
    goto :goto_c

    nop

    :goto_7
    int-to-float v0, v0

    goto :goto_11

    nop

    :goto_8
    invoke-virtual {p1, v0, v1}, Landroid/graphics/Canvas;->translate(FF)V

    goto :goto_10

    nop

    :goto_9
    invoke-direct {p0}, Lmiuix/popupwidget/internal/widget/GuidePopupView;->getMirroredMode()I

    move-result v0

    goto :goto_4

    nop

    :goto_a
    if-nez v0, :cond_0

    goto :goto_19

    :cond_0
    goto :goto_1c

    nop

    :goto_b
    iget-object v0, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mAnchor:Landroid/view/View;

    goto :goto_1d

    nop

    :goto_c
    return-void

    :goto_d
    invoke-direct {p0, p1, v0, v1, v2}, Lmiuix/popupwidget/internal/widget/GuidePopupView;->drawPopup(Landroid/graphics/Canvas;III)V

    goto :goto_1e

    nop

    :goto_e
    int-to-float v1, v1

    goto :goto_8

    nop

    :goto_f
    iget v2, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mOffsetY:I

    goto :goto_d

    nop

    :goto_10
    iget-object v0, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mAnchor:Landroid/view/View;

    goto :goto_15

    nop

    :goto_11
    iget v1, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mAnchorLocationY:I

    goto :goto_e

    nop

    :goto_12
    const/4 v2, 0x0

    goto :goto_18

    nop

    :goto_13
    iget-object v0, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mAnchor:Landroid/view/View;

    goto :goto_23

    nop

    :goto_14
    if-nez v0, :cond_1

    goto :goto_6

    :cond_1
    goto :goto_9

    nop

    :goto_15
    const/4 v1, 0x1

    goto :goto_1

    nop

    :goto_16
    iget v0, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mAnchorLocationX:I

    goto :goto_7

    nop

    :goto_17
    iget v1, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mOffsetX:I

    goto :goto_f

    nop

    :goto_18
    invoke-virtual {p1, v0, v2, v2, v1}, Landroid/graphics/Canvas;->drawBitmap(Landroid/graphics/Bitmap;FFLandroid/graphics/Paint;)V

    :goto_19
    goto :goto_13

    nop

    :goto_1a
    invoke-virtual {p1}, Landroid/graphics/Canvas;->restore()V

    goto :goto_2

    nop

    :goto_1b
    invoke-virtual {v0, v1}, Landroid/view/View;->setDrawingCacheEnabled(Z)V

    goto :goto_1a

    nop

    :goto_1c
    const/4 v1, 0x0

    goto :goto_12

    nop

    :goto_1d
    invoke-virtual {v0}, Landroid/view/View;->buildDrawingCache()V

    goto :goto_24

    nop

    :goto_1e
    iget-boolean v0, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mIsMirrored:Z

    goto :goto_14

    nop

    :goto_1f
    neg-int v2, v2

    goto :goto_5

    nop

    :goto_20
    invoke-virtual {p1}, Landroid/graphics/Canvas;->save()I

    goto :goto_16

    nop

    :goto_21
    neg-int v1, v1

    goto :goto_0

    nop

    :goto_22
    invoke-virtual {v0}, Landroid/view/View;->getDrawingCache()Landroid/graphics/Bitmap;

    move-result-object v0

    goto :goto_a

    nop

    :goto_23
    const/4 v1, 0x0

    goto :goto_1b

    nop

    :goto_24
    iget-object v0, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mAnchor:Landroid/view/View;

    goto :goto_22

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_popupwidget_internal_widget_GuidePopupView__onFinishInflate',
        'method': '.method protected onFinishInflate()V',
        'method_name': 'onFinishInflate',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/FrameLayout;->onFinishInflate()V', 'sget v0, Lmiuix/popupwidget/R$id;->text_group:I', 'invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;', 'check-cast v0, Landroid/widget/LinearLayout;', 'iput-object v0, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mTextGroup:Landroid/widget/LinearLayout;', 'sget v0, Lmiuix/popupwidget/R$id;->mirrored_text_group:I', 'invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;', 'check-cast v0, Landroid/widget/LinearLayout;'],
        'type': 'method_replace',
        'search': """.method protected onFinishInflate()V
    .registers 2

    invoke-super {p0}, Landroid/widget/FrameLayout;->onFinishInflate()V

    sget v0, Lmiuix/popupwidget/R$id;->text_group:I

    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/LinearLayout;

    iput-object v0, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mTextGroup:Landroid/widget/LinearLayout;

    sget v0, Lmiuix/popupwidget/R$id;->mirrored_text_group:I

    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/LinearLayout;

    iput-object v0, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mMirroredTextGroup:Landroid/widget/LinearLayout;

    return-void
.end method""",
        'replacement': """.method protected onFinishInflate()V
    .registers 2

    goto :goto_5

    nop

    :goto_0
    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_4

    nop

    :goto_1
    iput-object v0, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mTextGroup:Landroid/widget/LinearLayout;

    goto :goto_6

    nop

    :goto_2
    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_7

    nop

    :goto_3
    iput-object v0, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mMirroredTextGroup:Landroid/widget/LinearLayout;

    goto :goto_8

    nop

    :goto_4
    check-cast v0, Landroid/widget/LinearLayout;

    goto :goto_1

    nop

    :goto_5
    invoke-super {p0}, Landroid/widget/FrameLayout;->onFinishInflate()V

    goto :goto_9

    nop

    :goto_6
    sget v0, Lmiuix/popupwidget/R$id;->mirrored_text_group:I

    goto :goto_2

    nop

    :goto_7
    check-cast v0, Landroid/widget/LinearLayout;

    goto :goto_3

    nop

    :goto_8
    return-void

    :goto_9
    sget v0, Lmiuix/popupwidget/R$id;->text_group:I

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_popupwidget_internal_widget_GuidePopupView__onLayout',
        'method': '.method protected onLayout(ZIIII)V',
        'method_name': 'onLayout',
        'method_anchors': ['iget p1, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mAnchorWidth:I', 'if-eqz p1, :cond_0', 'iget p1, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mAnchorHeight:I', 'if-nez p1, :cond_1', 'iget-object p1, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mAnchor:Landroid/view/View;', 'invoke-virtual {p0, p1}, Lmiuix/popupwidget/internal/widget/GuidePopupView;->setAnchor(Landroid/view/View;)V', 'iget-object p1, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mTextGroup:Landroid/widget/LinearLayout;', 'invoke-virtual {p1}, Landroid/widget/LinearLayout;->getMeasuredWidth()I'],
        'type': 'method_replace',
        'search': """.method protected onLayout(ZIIII)V
    .registers 8

    iget p1, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mAnchorWidth:I

    if-eqz p1, :cond_0

    iget p1, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mAnchorHeight:I

    if-nez p1, :cond_1

    :cond_0
    iget-object p1, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mAnchor:Landroid/view/View;

    invoke-virtual {p0, p1}, Lmiuix/popupwidget/internal/widget/GuidePopupView;->setAnchor(Landroid/view/View;)V

    :cond_1
    iget-object p1, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mTextGroup:Landroid/widget/LinearLayout;

    invoke-virtual {p1}, Landroid/widget/LinearLayout;->getMeasuredWidth()I

    move-result p1

    iget-object p2, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mTextGroup:Landroid/widget/LinearLayout;

    invoke-virtual {p2}, Landroid/widget/LinearLayout;->getMeasuredHeight()I

    move-result p2

    int-to-double p3, p1

    const-wide/high16 v0, 0x4000000000000000L

    invoke-static {p3, p4, v0, v1}, Ljava/lang/Math;->pow(DD)D

    move-result-wide p3

    int-to-double p1, p2

    invoke-static {p1, p2, v0, v1}, Ljava/lang/Math;->pow(DD)D

    move-result-wide p1

    add-double/2addr p3, p1

    invoke-static {p3, p4}, Ljava/lang/Math;->sqrt(D)D

    move-result-wide p1

    div-double/2addr p1, v0

    iget p3, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mTextCircleRadius:F

    float-to-double p3, p3

    invoke-static {p1, p2, p3, p4}, Ljava/lang/Math;->max(DD)D

    move-result-wide p1

    double-to-float p1, p1

    iput p1, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mTextCircleRadius:F

    iget-boolean p1, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mIsMirrored:Z

    if-eqz p1, :cond_2

    iget-object p1, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mMirroredTextGroup:Landroid/widget/LinearLayout;

    invoke-virtual {p1}, Landroid/widget/LinearLayout;->getMeasuredWidth()I

    move-result p1

    iget-object p2, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mMirroredTextGroup:Landroid/widget/LinearLayout;

    invoke-virtual {p2}, Landroid/widget/LinearLayout;->getMeasuredHeight()I

    move-result p2

    int-to-double p3, p1

    invoke-static {p3, p4, v0, v1}, Ljava/lang/Math;->pow(DD)D

    move-result-wide p3

    int-to-double p1, p2

    invoke-static {p1, p2, v0, v1}, Ljava/lang/Math;->pow(DD)D

    move-result-wide p1

    add-double/2addr p3, p1

    invoke-static {p3, p4}, Ljava/lang/Math;->sqrt(D)D

    move-result-wide p1

    div-double/2addr p1, v0

    iget p3, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mTextCircleRadius:F

    float-to-double p3, p3

    invoke-static {p1, p2, p3, p4}, Ljava/lang/Math;->max(DD)D

    move-result-wide p1

    double-to-float p1, p1

    iput p1, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mTextCircleRadius:F

    :cond_2
    iget p1, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mArrowMode:I

    const/4 p2, -0x1

    if-ne p1, p2, :cond_3

    invoke-direct {p0}, Lmiuix/popupwidget/internal/widget/GuidePopupView;->adjustArrowMode()V

    return-void

    :cond_3
    invoke-direct {p0}, Lmiuix/popupwidget/internal/widget/GuidePopupView;->arrowLayout()V

    return-void
.end method""",
        'replacement': """.method protected onLayout(ZIIII)V
    .registers 8

    goto :goto_13

    nop

    :goto_0
    invoke-static {p3, p4}, Ljava/lang/Math;->sqrt(D)D

    move-result-wide p1

    goto :goto_a

    nop

    :goto_1
    iget-boolean p1, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mIsMirrored:Z

    goto :goto_2a

    nop

    :goto_2
    invoke-direct {p0}, Lmiuix/popupwidget/internal/widget/GuidePopupView;->arrowLayout()V

    goto :goto_24

    nop

    :goto_3
    invoke-static {p1, p2, v0, v1}, Ljava/lang/Math;->pow(DD)D

    move-result-wide p1

    goto :goto_4

    nop

    :goto_4
    add-double/2addr p3, p1

    goto :goto_d

    nop

    :goto_5
    iput p1, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mTextCircleRadius:F

    :goto_6
    goto :goto_9

    nop

    :goto_7
    int-to-double p3, p1

    goto :goto_1f

    nop

    :goto_8
    invoke-virtual {p1}, Landroid/widget/LinearLayout;->getMeasuredWidth()I

    move-result p1

    goto :goto_25

    nop

    :goto_9
    iget p1, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mArrowMode:I

    goto :goto_1a

    nop

    :goto_a
    div-double/2addr p1, v0

    goto :goto_c

    nop

    :goto_b
    iget-object p2, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mMirroredTextGroup:Landroid/widget/LinearLayout;

    goto :goto_14

    nop

    :goto_c
    iget p3, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mTextCircleRadius:F

    goto :goto_1d

    nop

    :goto_d
    invoke-static {p3, p4}, Ljava/lang/Math;->sqrt(D)D

    move-result-wide p1

    goto :goto_23

    nop

    :goto_e
    iput p1, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mTextCircleRadius:F

    goto :goto_1

    nop

    :goto_f
    float-to-double p3, p3

    goto :goto_12

    nop

    :goto_10
    add-double/2addr p3, p1

    goto :goto_0

    nop

    :goto_11
    invoke-static {p3, p4, v0, v1}, Ljava/lang/Math;->pow(DD)D

    move-result-wide p3

    goto :goto_28

    nop

    :goto_12
    invoke-static {p1, p2, p3, p4}, Ljava/lang/Math;->max(DD)D

    move-result-wide p1

    goto :goto_2b

    nop

    :goto_13
    iget p1, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mAnchorWidth:I

    goto :goto_32

    nop

    :goto_14
    invoke-virtual {p2}, Landroid/widget/LinearLayout;->getMeasuredHeight()I

    move-result p2

    goto :goto_7

    nop

    :goto_15
    const-wide/high16 v0, 0x4000000000000000L

    goto :goto_11

    nop

    :goto_16
    iget p3, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mTextCircleRadius:F

    goto :goto_f

    nop

    :goto_17
    double-to-float p1, p1

    goto :goto_5

    nop

    :goto_18
    return-void

    :goto_19
    goto :goto_2

    nop

    :goto_1a
    const/4 p2, -0x1

    goto :goto_31

    nop

    :goto_1b
    iget-object p1, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mTextGroup:Landroid/widget/LinearLayout;

    goto :goto_8

    nop

    :goto_1c
    invoke-static {p1, p2, p3, p4}, Ljava/lang/Math;->max(DD)D

    move-result-wide p1

    goto :goto_17

    nop

    :goto_1d
    float-to-double p3, p3

    goto :goto_1c

    nop

    :goto_1e
    iget p1, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mAnchorHeight:I

    goto :goto_2e

    nop

    :goto_1f
    invoke-static {p3, p4, v0, v1}, Ljava/lang/Math;->pow(DD)D

    move-result-wide p3

    goto :goto_2d

    nop

    :goto_20
    int-to-double p3, p1

    goto :goto_15

    nop

    :goto_21
    invoke-virtual {p0, p1}, Lmiuix/popupwidget/internal/widget/GuidePopupView;->setAnchor(Landroid/view/View;)V

    :goto_22
    goto :goto_1b

    nop

    :goto_23
    div-double/2addr p1, v0

    goto :goto_16

    nop

    :goto_24
    return-void

    :goto_25
    iget-object p2, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mTextGroup:Landroid/widget/LinearLayout;

    goto :goto_26

    nop

    :goto_26
    invoke-virtual {p2}, Landroid/widget/LinearLayout;->getMeasuredHeight()I

    move-result p2

    goto :goto_20

    nop

    :goto_27
    invoke-static {p1, p2, v0, v1}, Ljava/lang/Math;->pow(DD)D

    move-result-wide p1

    goto :goto_10

    nop

    :goto_28
    int-to-double p1, p2

    goto :goto_3

    nop

    :goto_29
    invoke-virtual {p1}, Landroid/widget/LinearLayout;->getMeasuredWidth()I

    move-result p1

    goto :goto_b

    nop

    :goto_2a
    if-nez p1, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_2c

    nop

    :goto_2b
    double-to-float p1, p1

    goto :goto_e

    nop

    :goto_2c
    iget-object p1, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mMirroredTextGroup:Landroid/widget/LinearLayout;

    goto :goto_29

    nop

    :goto_2d
    int-to-double p1, p2

    goto :goto_27

    nop

    :goto_2e
    if-eqz p1, :cond_1

    goto :goto_22

    :cond_1
    :goto_2f
    goto :goto_33

    nop

    :goto_30
    invoke-direct {p0}, Lmiuix/popupwidget/internal/widget/GuidePopupView;->adjustArrowMode()V

    goto :goto_18

    nop

    :goto_31
    if-eq p1, p2, :cond_2

    goto :goto_19

    :cond_2
    goto :goto_30

    nop

    :goto_32
    if-nez p1, :cond_3

    goto :goto_2f

    :cond_3
    goto :goto_1e

    nop

    :goto_33
    iget-object p1, p0, Lmiuix/popupwidget/internal/widget/GuidePopupView;->mAnchor:Landroid/view/View;

    goto :goto_21

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
