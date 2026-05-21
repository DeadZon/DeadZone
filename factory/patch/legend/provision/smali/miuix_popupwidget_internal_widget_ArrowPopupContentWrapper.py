TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/popupwidget/internal/widget/ArrowPopupContentWrapper.smali'
CLASS_FALLBACK_NAMES = ['ArrowPopupContentWrapper.smali']
CLASS_ANCHORS = ['.super Landroid/widget/LinearLayout;']

PATCHES = [
    {
        'id': 'miuix_popupwidget_internal_widget_ArrowPopupContentWrapper__dispatchDraw',
        'method': '.method protected dispatchDraw(Landroid/graphics/Canvas;)V',
        'method_name': 'dispatchDraw',
        'method_anchors': ['invoke-virtual {p0}, Landroid/widget/LinearLayout;->getWidth()I', 'invoke-virtual {p0}, Landroid/widget/LinearLayout;->getHeight()I', 'invoke-virtual/range {v1 .. v7}, Landroid/graphics/Canvas;->saveLayer(FFFFLandroid/graphics/Paint;I)I', 'invoke-super {p0, v1}, Landroid/widget/LinearLayout;->dispatchDraw(Landroid/graphics/Canvas;)V', 'iget-object p1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mMask1:Landroid/graphics/Bitmap;', 'invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingLeft()I', 'invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingTop()I', 'iget-object v3, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mPaint:Landroid/graphics/Paint;'],
        'type': 'method_replace',
        'search': """.method protected dispatchDraw(Landroid/graphics/Canvas;)V
    .registers 10

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getWidth()I

    move-result v0

    int-to-float v4, v0

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getHeight()I

    move-result v0

    int-to-float v5, v0

    const/4 v6, 0x0

    const/16 v7, 0x1f

    const/4 v2, 0x0

    const/4 v3, 0x0

    move-object v1, p1

    invoke-virtual/range {v1 .. v7}, Landroid/graphics/Canvas;->saveLayer(FFFFLandroid/graphics/Paint;I)I

    invoke-super {p0, v1}, Landroid/widget/LinearLayout;->dispatchDraw(Landroid/graphics/Canvas;)V

    iget-object p1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mMask1:Landroid/graphics/Bitmap;

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingLeft()I

    move-result v0

    int-to-float v0, v0

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingTop()I

    move-result v2

    int-to-float v2, v2

    iget-object v3, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mPaint:Landroid/graphics/Paint;

    invoke-virtual {v1, p1, v0, v2, v3}, Landroid/graphics/Canvas;->drawBitmap(Landroid/graphics/Bitmap;FFLandroid/graphics/Paint;)V

    iget-object p1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mMask2:Landroid/graphics/Bitmap;

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getWidth()I

    move-result v0

    iget-object v2, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mMask2:Landroid/graphics/Bitmap;

    invoke-virtual {v2}, Landroid/graphics/Bitmap;->getWidth()I

    move-result v2

    sub-int/2addr v0, v2

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingRight()I

    move-result v2

    sub-int/2addr v0, v2

    int-to-float v0, v0

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingTop()I

    move-result v2

    int-to-float v2, v2

    iget-object v3, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mPaint:Landroid/graphics/Paint;

    invoke-virtual {v1, p1, v0, v2, v3}, Landroid/graphics/Canvas;->drawBitmap(Landroid/graphics/Bitmap;FFLandroid/graphics/Paint;)V

    iget-object p1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mMask3:Landroid/graphics/Bitmap;

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingLeft()I

    move-result v0

    int-to-float v0, v0

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getHeight()I

    move-result v2

    iget-object v3, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mMask3:Landroid/graphics/Bitmap;

    invoke-virtual {v3}, Landroid/graphics/Bitmap;->getHeight()I

    move-result v3

    sub-int/2addr v2, v3

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingBottom()I

    move-result v3

    sub-int/2addr v2, v3

    int-to-float v2, v2

    iget-object v3, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mPaint:Landroid/graphics/Paint;

    invoke-virtual {v1, p1, v0, v2, v3}, Landroid/graphics/Canvas;->drawBitmap(Landroid/graphics/Bitmap;FFLandroid/graphics/Paint;)V

    iget-object p1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mMask4:Landroid/graphics/Bitmap;

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getWidth()I

    move-result v0

    iget-object v2, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mMask4:Landroid/graphics/Bitmap;

    invoke-virtual {v2}, Landroid/graphics/Bitmap;->getWidth()I

    move-result v2

    sub-int/2addr v0, v2

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingRight()I

    move-result v2

    sub-int/2addr v0, v2

    int-to-float v0, v0

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getHeight()I

    move-result v2

    iget-object v3, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mMask4:Landroid/graphics/Bitmap;

    invoke-virtual {v3}, Landroid/graphics/Bitmap;->getHeight()I

    move-result v3

    sub-int/2addr v2, v3

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingBottom()I

    move-result v3

    sub-int/2addr v2, v3

    int-to-float v2, v2

    iget-object p0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mPaint:Landroid/graphics/Paint;

    invoke-virtual {v1, p1, v0, v2, p0}, Landroid/graphics/Canvas;->drawBitmap(Landroid/graphics/Bitmap;FFLandroid/graphics/Paint;)V

    invoke-virtual {v1}, Landroid/graphics/Canvas;->restore()V

    return-void
.end method""",
        'replacement': """.method protected dispatchDraw(Landroid/graphics/Canvas;)V
    .registers 10

    goto :goto_11

    nop

    :goto_0
    iget-object p1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mMask3:Landroid/graphics/Bitmap;

    goto :goto_19

    nop

    :goto_1
    sub-int/2addr v0, v2

    goto :goto_2a

    nop

    :goto_2
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingTop()I

    move-result v2

    goto :goto_12

    nop

    :goto_3
    iget-object v3, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mMask3:Landroid/graphics/Bitmap;

    goto :goto_e

    nop

    :goto_4
    int-to-float v4, v0

    goto :goto_2d

    nop

    :goto_5
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getWidth()I

    move-result v0

    goto :goto_20

    nop

    :goto_6
    iget-object v3, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mPaint:Landroid/graphics/Paint;

    goto :goto_2f

    nop

    :goto_7
    invoke-virtual {v1, p1, v0, v2, p0}, Landroid/graphics/Canvas;->drawBitmap(Landroid/graphics/Bitmap;FFLandroid/graphics/Paint;)V

    goto :goto_16

    nop

    :goto_8
    sub-int/2addr v2, v3

    goto :goto_c

    nop

    :goto_9
    invoke-virtual {v2}, Landroid/graphics/Bitmap;->getWidth()I

    move-result v2

    goto :goto_1

    nop

    :goto_a
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getHeight()I

    move-result v2

    goto :goto_3

    nop

    :goto_b
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getHeight()I

    move-result v2

    goto :goto_22

    nop

    :goto_c
    int-to-float v2, v2

    goto :goto_6

    nop

    :goto_d
    int-to-float v0, v0

    goto :goto_b

    nop

    :goto_e
    invoke-virtual {v3}, Landroid/graphics/Bitmap;->getHeight()I

    move-result v3

    goto :goto_10

    nop

    :goto_f
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingBottom()I

    move-result v3

    goto :goto_8

    nop

    :goto_10
    sub-int/2addr v2, v3

    goto :goto_f

    nop

    :goto_11
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getWidth()I

    move-result v0

    goto :goto_4

    nop

    :goto_12
    int-to-float v2, v2

    goto :goto_31

    nop

    :goto_13
    invoke-virtual/range {v1 .. v7}, Landroid/graphics/Canvas;->saveLayer(FFFFLandroid/graphics/Paint;I)I

    goto :goto_1f

    nop

    :goto_14
    invoke-virtual {v1, p1, v0, v2, v3}, Landroid/graphics/Canvas;->drawBitmap(Landroid/graphics/Bitmap;FFLandroid/graphics/Paint;)V

    goto :goto_1c

    nop

    :goto_15
    iget-object p1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mMask4:Landroid/graphics/Bitmap;

    goto :goto_3c

    nop

    :goto_16
    invoke-virtual {v1}, Landroid/graphics/Canvas;->restore()V

    goto :goto_37

    nop

    :goto_17
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingLeft()I

    move-result v0

    goto :goto_24

    nop

    :goto_18
    move-object v1, p1

    goto :goto_13

    nop

    :goto_19
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingLeft()I

    move-result v0

    goto :goto_36

    nop

    :goto_1a
    const/4 v3, 0x0

    goto :goto_18

    nop

    :goto_1b
    iget-object p0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mPaint:Landroid/graphics/Paint;

    goto :goto_7

    nop

    :goto_1c
    iget-object p1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mMask2:Landroid/graphics/Bitmap;

    goto :goto_5

    nop

    :goto_1d
    sub-int/2addr v0, v2

    goto :goto_d

    nop

    :goto_1e
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingRight()I

    move-result v2

    goto :goto_1d

    nop

    :goto_1f
    invoke-super {p0, v1}, Landroid/widget/LinearLayout;->dispatchDraw(Landroid/graphics/Canvas;)V

    goto :goto_2c

    nop

    :goto_20
    iget-object v2, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mMask2:Landroid/graphics/Bitmap;

    goto :goto_9

    nop

    :goto_21
    int-to-float v2, v2

    goto :goto_1b

    nop

    :goto_22
    iget-object v3, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mMask4:Landroid/graphics/Bitmap;

    goto :goto_26

    nop

    :goto_23
    const/4 v2, 0x0

    goto :goto_1a

    nop

    :goto_24
    int-to-float v0, v0

    goto :goto_2

    nop

    :goto_25
    iget-object v2, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mMask4:Landroid/graphics/Bitmap;

    goto :goto_33

    nop

    :goto_26
    invoke-virtual {v3}, Landroid/graphics/Bitmap;->getHeight()I

    move-result v3

    goto :goto_39

    nop

    :goto_27
    const/4 v6, 0x0

    goto :goto_3a

    nop

    :goto_28
    invoke-virtual {v1, p1, v0, v2, v3}, Landroid/graphics/Canvas;->drawBitmap(Landroid/graphics/Bitmap;FFLandroid/graphics/Paint;)V

    goto :goto_0

    nop

    :goto_29
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingBottom()I

    move-result v3

    goto :goto_32

    nop

    :goto_2a
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingRight()I

    move-result v2

    goto :goto_34

    nop

    :goto_2b
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingTop()I

    move-result v2

    goto :goto_38

    nop

    :goto_2c
    iget-object p1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mMask1:Landroid/graphics/Bitmap;

    goto :goto_17

    nop

    :goto_2d
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getHeight()I

    move-result v0

    goto :goto_2e

    nop

    :goto_2e
    int-to-float v5, v0

    goto :goto_27

    nop

    :goto_2f
    invoke-virtual {v1, p1, v0, v2, v3}, Landroid/graphics/Canvas;->drawBitmap(Landroid/graphics/Bitmap;FFLandroid/graphics/Paint;)V

    goto :goto_15

    nop

    :goto_30
    sub-int/2addr v0, v2

    goto :goto_1e

    nop

    :goto_31
    iget-object v3, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mPaint:Landroid/graphics/Paint;

    goto :goto_14

    nop

    :goto_32
    sub-int/2addr v2, v3

    goto :goto_21

    nop

    :goto_33
    invoke-virtual {v2}, Landroid/graphics/Bitmap;->getWidth()I

    move-result v2

    goto :goto_30

    nop

    :goto_34
    sub-int/2addr v0, v2

    goto :goto_3b

    nop

    :goto_35
    iget-object v3, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mPaint:Landroid/graphics/Paint;

    goto :goto_28

    nop

    :goto_36
    int-to-float v0, v0

    goto :goto_a

    nop

    :goto_37
    return-void

    :goto_38
    int-to-float v2, v2

    goto :goto_35

    nop

    :goto_39
    sub-int/2addr v2, v3

    goto :goto_29

    nop

    :goto_3a
    const/16 v7, 0x1f

    goto :goto_23

    nop

    :goto_3b
    int-to-float v0, v0

    goto :goto_2b

    nop

    :goto_3c
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getWidth()I

    move-result v0

    goto :goto_25

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_popupwidget_internal_widget_ArrowPopupContentWrapper__onDraw',
        'method': '.method protected onDraw(Landroid/graphics/Canvas;)V',
        'method_name': 'onDraw',
        'method_anchors': ['invoke-super/range {p0 .. p1}, Landroid/widget/LinearLayout;->onDraw(Landroid/graphics/Canvas;)V', 'invoke-static {v0}, Landroidx/core/view/ViewCompat;->getLayoutDirection(Landroid/view/View;)I', 'if-ne v1, v2, :cond_0', 'iput-boolean v1, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mIsRtl:Z', 'iget-object v1, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mPath:Landroid/graphics/Path;', 'if-eqz v1, :cond_1', 'invoke-virtual {v1}, Landroid/graphics/Path;->reset()V', 'invoke-virtual {v0}, Landroid/widget/LinearLayout;->getWidth()I'],
        'type': 'method_replace',
        'search': """.method protected onDraw(Landroid/graphics/Canvas;)V
    .registers 18

    move-object/from16 v0, p0

    invoke-super/range {p0 .. p1}, Landroid/widget/LinearLayout;->onDraw(Landroid/graphics/Canvas;)V

    invoke-static {v0}, Landroidx/core/view/ViewCompat;->getLayoutDirection(Landroid/view/View;)I

    move-result v1

    const/4 v2, 0x1

    if-ne v1, v2, :cond_0

    move v1, v2

    goto :goto_0

    :cond_0
    const/4 v1, 0x0

    :goto_0
    iput-boolean v1, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mIsRtl:Z

    iget-object v1, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mPath:Landroid/graphics/Path;

    if-eqz v1, :cond_1

    invoke-virtual {v1}, Landroid/graphics/Path;->reset()V

    :cond_1
    invoke-virtual {v0}, Landroid/widget/LinearLayout;->getWidth()I

    move-result v1

    int-to-float v1, v1

    invoke-virtual {v0}, Landroid/widget/LinearLayout;->getHeight()I

    move-result v3

    int-to-float v3, v3

    iget v5, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->paddingTop:F

    iget v4, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->paddingBottom:F

    sub-float v6, v3, v4

    iget v3, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->paddingStart:F

    iget v4, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->paddingEnd:F

    sub-float v4, v1, v4

    iget v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mArrowMode:I

    const/16 v8, 0x10

    const/16 v9, 0x8

    if-eq v7, v9, :cond_2

    if-ne v7, v8, :cond_4

    :cond_2
    iget v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mArrowHorizonOffset:F

    iget v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->radius:F

    add-float v11, v3, v10

    iget v12, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->density:F

    const/high16 v13, 0x41600000

    mul-float v14, v12, v13

    add-float/2addr v11, v14

    const/high16 v14, 0x40000000

    div-float v14, v1, v14

    sub-float/2addr v11, v14

    cmpg-float v11, v7, v11

    if-gez v11, :cond_3

    add-float/2addr v10, v3

    mul-float/2addr v12, v13

    add-float/2addr v10, v12

    sub-float/2addr v10, v14

    iput v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mArrowHorizonOffset:F

    goto :goto_1

    :cond_3
    sub-float v11, v4, v10

    mul-float v15, v12, v13

    sub-float/2addr v11, v15

    sub-float/2addr v11, v14

    cmpl-float v7, v7, v11

    if-lez v7, :cond_4

    sub-float v7, v4, v10

    mul-float/2addr v12, v13

    sub-float/2addr v7, v12

    sub-float/2addr v7, v14

    iput v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mArrowHorizonOffset:F

    :cond_4
    :goto_1
    iget-object v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p0:Landroid/graphics/PointF;

    iget v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->radius:F

    add-float/2addr v10, v3

    invoke-virtual {v7, v10, v5}, Landroid/graphics/PointF;->set(FF)V

    iget-object v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p1:Landroid/graphics/PointF;

    iget v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->radius:F

    add-float/2addr v10, v5

    invoke-virtual {v7, v4, v10}, Landroid/graphics/PointF;->set(FF)V

    iget-object v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p2:Landroid/graphics/PointF;

    iget v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->radius:F

    sub-float v10, v6, v10

    invoke-virtual {v7, v4, v10}, Landroid/graphics/PointF;->set(FF)V

    iget-object v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p3:Landroid/graphics/PointF;

    iget v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->radius:F

    sub-float v10, v4, v10

    invoke-virtual {v7, v10, v6}, Landroid/graphics/PointF;->set(FF)V

    iget-object v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p4:Landroid/graphics/PointF;

    iget v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->radius:F

    add-float/2addr v10, v3

    invoke-virtual {v7, v10, v6}, Landroid/graphics/PointF;->set(FF)V

    iget-object v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p5:Landroid/graphics/PointF;

    iget v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->radius:F

    sub-float v10, v6, v10

    invoke-virtual {v7, v3, v10}, Landroid/graphics/PointF;->set(FF)V

    iget-object v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p6:Landroid/graphics/PointF;

    iget v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->radius:F

    add-float/2addr v10, v5

    invoke-virtual {v7, v3, v10}, Landroid/graphics/PointF;->set(FF)V

    iget-object v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p7:Landroid/graphics/PointF;

    iget v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->radius:F

    sub-float v10, v4, v10

    invoke-virtual {v7, v10, v5}, Landroid/graphics/PointF;->set(FF)V

    iget-boolean v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mIsRtl:Z

    const/16 v10, 0xa

    if-nez v7, :cond_5

    iget v11, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mArrowMode:I

    if-eq v11, v10, :cond_6

    :cond_5
    const/16 v11, 0x9

    if-eqz v7, :cond_7

    iget v12, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mArrowMode:I

    if-ne v12, v11, :cond_7

    :cond_6
    iget v1, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->density:F

    move v7, v6

    iget-object v6, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p0:Landroid/graphics/PointF;

    move v2, v3

    move v3, v4

    move v4, v5

    move v5, v7

    iget-object v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p2:Landroid/graphics/PointF;

    iget-object v8, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p3:Landroid/graphics/PointF;

    iget-object v9, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p4:Landroid/graphics/PointF;

    iget-object v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p5:Landroid/graphics/PointF;

    iget-object v11, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p6:Landroid/graphics/PointF;

    invoke-direct/range {v0 .. v11}, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->drawTopRightArrow(FFFFFLandroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;)V

    goto :goto_2

    :cond_7
    iget v12, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mArrowMode:I

    if-ne v12, v9, :cond_8

    iget v2, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->density:F

    iget-object v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p0:Landroid/graphics/PointF;

    iget-object v8, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p1:Landroid/graphics/PointF;

    iget-object v9, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p2:Landroid/graphics/PointF;

    iget-object v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p3:Landroid/graphics/PointF;

    iget-object v11, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p4:Landroid/graphics/PointF;

    iget-object v12, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p5:Landroid/graphics/PointF;

    iget-object v13, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p6:Landroid/graphics/PointF;

    iget-object v14, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p7:Landroid/graphics/PointF;

    invoke-direct/range {v0 .. v14}, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->drawTopArrow(FFFFFFLandroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;)V

    goto :goto_2

    :cond_8
    if-nez v7, :cond_9

    if-eq v12, v11, :cond_a

    :cond_9
    if-eqz v7, :cond_b

    if-ne v12, v10, :cond_b

    :cond_a
    iget v1, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->radius:F

    iget v2, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->density:F

    iget-object v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p1:Landroid/graphics/PointF;

    iget-object v8, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p2:Landroid/graphics/PointF;

    iget-object v9, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p3:Landroid/graphics/PointF;

    iget-object v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p4:Landroid/graphics/PointF;

    iget-object v11, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p5:Landroid/graphics/PointF;

    iget-object v12, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p6:Landroid/graphics/PointF;

    iget-object v13, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p7:Landroid/graphics/PointF;

    invoke-direct/range {v0 .. v13}, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->drawTopLeftArrow(FFFFFFLandroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;)V

    goto :goto_2

    :cond_b
    const/16 v9, 0x20

    if-nez v7, :cond_c

    if-ne v12, v9, :cond_c

    iget v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mRtlMode:I

    if-ne v10, v2, :cond_f

    :cond_c
    const/16 v10, 0x40

    if-eqz v7, :cond_d

    if-ne v12, v10, :cond_d

    iget v11, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mRtlMode:I

    if-nez v11, :cond_f

    :cond_d
    if-eqz v7, :cond_e

    if-ne v12, v9, :cond_e

    iget v11, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mRtlMode:I

    if-eqz v11, :cond_f

    :cond_e
    if-nez v7, :cond_10

    if-ne v12, v10, :cond_10

    iget v11, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mRtlMode:I

    if-ne v11, v2, :cond_10

    :cond_f
    iget v1, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->radius:F

    iget v2, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->density:F

    iget-object v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p0:Landroid/graphics/PointF;

    iget-object v8, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p1:Landroid/graphics/PointF;

    iget-object v9, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p2:Landroid/graphics/PointF;

    iget-object v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p3:Landroid/graphics/PointF;

    iget-object v11, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p4:Landroid/graphics/PointF;

    iget-object v12, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p5:Landroid/graphics/PointF;

    iget-object v13, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p6:Landroid/graphics/PointF;

    invoke-direct/range {v0 .. v13}, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->drawLeftArrow(FFFFFFLandroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;)V

    goto :goto_2

    :cond_10
    if-nez v7, :cond_11

    if-eq v12, v10, :cond_14

    :cond_11
    if-eqz v7, :cond_12

    if-ne v12, v9, :cond_12

    iget v11, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mRtlMode:I

    if-ne v11, v2, :cond_14

    :cond_12
    if-eqz v7, :cond_13

    if-eq v12, v10, :cond_14

    :cond_13
    if-nez v7, :cond_15

    if-ne v12, v9, :cond_15

    :cond_14
    iget v1, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->radius:F

    iget v2, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->density:F

    iget-object v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p0:Landroid/graphics/PointF;

    iget-object v8, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p1:Landroid/graphics/PointF;

    iget-object v9, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p2:Landroid/graphics/PointF;

    iget-object v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p3:Landroid/graphics/PointF;

    iget-object v11, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p4:Landroid/graphics/PointF;

    iget-object v12, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p5:Landroid/graphics/PointF;

    iget-object v13, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p6:Landroid/graphics/PointF;

    invoke-direct/range {v0 .. v13}, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->drawRightArrow(FFFFFFLandroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;)V

    goto :goto_2

    :cond_15
    const/16 v2, 0x11

    if-nez v7, :cond_16

    if-eq v12, v2, :cond_17

    :cond_16
    const/16 v9, 0x12

    if-eqz v7, :cond_18

    if-ne v12, v9, :cond_18

    :cond_17
    iget v1, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->radius:F

    iget v2, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->density:F

    iget-object v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p0:Landroid/graphics/PointF;

    iget-object v8, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p1:Landroid/graphics/PointF;

    iget-object v9, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p2:Landroid/graphics/PointF;

    iget-object v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p4:Landroid/graphics/PointF;

    iget-object v11, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p5:Landroid/graphics/PointF;

    iget-object v12, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p6:Landroid/graphics/PointF;

    invoke-direct/range {v0 .. v12}, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->drawBottomRightArrow(FFFFFFLandroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;)V

    goto :goto_2

    :cond_18
    if-ne v12, v8, :cond_19

    iget v2, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->radius:F

    move v7, v6

    move v6, v5

    move v5, v4

    move v4, v3

    iget v3, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->density:F

    iget-object v8, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p0:Landroid/graphics/PointF;

    iget-object v9, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p1:Landroid/graphics/PointF;

    iget-object v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p2:Landroid/graphics/PointF;

    iget-object v11, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p3:Landroid/graphics/PointF;

    iget-object v12, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p4:Landroid/graphics/PointF;

    iget-object v13, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p5:Landroid/graphics/PointF;

    iget-object v14, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p6:Landroid/graphics/PointF;

    invoke-direct/range {v0 .. v14}, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->drawBottomArrow(FFFFFFFLandroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;)V

    goto :goto_2

    :cond_19
    if-nez v7, :cond_1a

    if-eq v12, v9, :cond_1b

    :cond_1a
    if-eqz v7, :cond_1c

    if-ne v12, v2, :cond_1c

    :cond_1b
    iget v1, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->radius:F

    iget v2, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->density:F

    iget-object v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p0:Landroid/graphics/PointF;

    iget-object v8, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p1:Landroid/graphics/PointF;

    iget-object v9, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p2:Landroid/graphics/PointF;

    iget-object v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p3:Landroid/graphics/PointF;

    iget-object v11, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p6:Landroid/graphics/PointF;

    invoke-direct/range {v0 .. v11}, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->drawBottomLeftArrow(FFFFFFLandroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;)V

    :cond_1c
    :goto_2
    iget-object v1, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mBackgroundPaint:Landroid/graphics/Paint;

    if-eqz v1, :cond_1d

    iget-object v0, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mPath:Landroid/graphics/Path;

    if-eqz v0, :cond_1d

    move-object/from16 v2, p1

    invoke-virtual {v2, v0, v1}, Landroid/graphics/Canvas;->drawPath(Landroid/graphics/Path;Landroid/graphics/Paint;)V

    :cond_1d
    return-void
.end method""",
        'replacement': """.method protected onDraw(Landroid/graphics/Canvas;)V
    .registers 18

    goto :goto_c

    nop

    :goto_0
    invoke-direct/range {v0 .. v11}, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->drawBottomLeftArrow(FFFFFFLandroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;)V

    :goto_1
    goto :goto_9b

    nop

    :goto_2
    iget-object v9, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p2:Landroid/graphics/PointF;

    goto :goto_87

    nop

    :goto_3
    iget-object v8, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p2:Landroid/graphics/PointF;

    goto :goto_cb

    nop

    :goto_4
    iget-object v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p7:Landroid/graphics/PointF;

    goto :goto_f8

    nop

    :goto_5
    invoke-direct/range {v0 .. v12}, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->drawBottomRightArrow(FFFFFFLandroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;)V

    goto :goto_4c

    nop

    :goto_6
    iget-object v12, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p5:Landroid/graphics/PointF;

    goto :goto_79

    nop

    :goto_7
    iget-object v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p0:Landroid/graphics/PointF;

    goto :goto_ff

    nop

    :goto_8
    iget v2, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->density:F

    goto :goto_54

    nop

    :goto_9
    if-gtz v7, :cond_0

    goto :goto_6b

    :cond_0
    goto :goto_27

    nop

    :goto_a
    if-nez v11, :cond_1

    goto :goto_78

    :cond_1
    :goto_b
    goto :goto_ca

    nop

    :goto_c
    move-object/from16 v0, p0

    goto :goto_b8

    nop

    :goto_d
    iget-object v6, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p0:Landroid/graphics/PointF;

    goto :goto_104

    nop

    :goto_e
    const/16 v9, 0x20

    goto :goto_8b

    nop

    :goto_f
    iget-object v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p4:Landroid/graphics/PointF;

    goto :goto_e8

    nop

    :goto_10
    iget-object v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p0:Landroid/graphics/PointF;

    goto :goto_66

    nop

    :goto_11
    const/high16 v13, 0x41600000

    goto :goto_1c

    nop

    :goto_12
    invoke-direct/range {v0 .. v11}, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->drawTopRightArrow(FFFFFLandroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;)V

    goto :goto_24

    nop

    :goto_13
    iget-object v13, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p6:Landroid/graphics/PointF;

    goto :goto_c0

    nop

    :goto_14
    move v4, v3

    goto :goto_57

    nop

    :goto_15
    mul-float/2addr v12, v13

    goto :goto_50

    nop

    :goto_16
    goto :goto_10b

    :goto_17
    goto :goto_10a

    nop

    :goto_18
    iget v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mArrowHorizonOffset:F

    goto :goto_c9

    nop

    :goto_19
    iget-object v8, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p1:Landroid/graphics/PointF;

    goto :goto_9f

    nop

    :goto_1a
    iget-object v11, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p4:Landroid/graphics/PointF;

    goto :goto_6

    nop

    :goto_1b
    sub-float/2addr v10, v14

    goto :goto_22

    nop

    :goto_1c
    mul-float v14, v12, v13

    goto :goto_5e

    nop

    :goto_1d
    if-eqz v7, :cond_2

    goto :goto_44

    :cond_2
    goto :goto_43

    nop

    :goto_1e
    mul-float/2addr v12, v13

    goto :goto_ab

    nop

    :goto_1f
    invoke-virtual {v1}, Landroid/graphics/Path;->reset()V

    :goto_20
    goto :goto_28

    nop

    :goto_21
    if-eq v12, v9, :cond_3

    goto :goto_b

    :cond_3
    goto :goto_62

    nop

    :goto_22
    iput v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mArrowHorizonOffset:F

    goto :goto_ef

    nop

    :goto_23
    iget-object v11, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p4:Landroid/graphics/PointF;

    goto :goto_df

    nop

    :goto_24
    goto :goto_1

    :goto_25
    goto :goto_f9

    nop

    :goto_26
    sub-float/2addr v11, v14

    goto :goto_fb

    nop

    :goto_27
    sub-float v7, v4, v10

    goto :goto_1e

    nop

    :goto_28
    invoke-virtual {v0}, Landroid/widget/LinearLayout;->getWidth()I

    move-result v1

    goto :goto_8f

    nop

    :goto_29
    invoke-virtual {v7, v10, v5}, Landroid/graphics/PointF;->set(FF)V

    goto :goto_63

    nop

    :goto_2a
    iget-object v11, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p3:Landroid/graphics/PointF;

    goto :goto_81

    nop

    :goto_2b
    move v4, v5

    goto :goto_3f

    nop

    :goto_2c
    invoke-virtual {v7, v10, v6}, Landroid/graphics/PointF;->set(FF)V

    goto :goto_fd

    nop

    :goto_2d
    iget v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mRtlMode:I

    goto :goto_94

    nop

    :goto_2e
    if-nez v7, :cond_4

    goto :goto_b

    :cond_4
    goto :goto_21

    nop

    :goto_2f
    iget v5, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->paddingTop:F

    goto :goto_89

    nop

    :goto_30
    iget-object v11, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p5:Landroid/graphics/PointF;

    goto :goto_e4

    nop

    :goto_31
    iget v2, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->density:F

    goto :goto_b5

    nop

    :goto_32
    iget-object v14, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p6:Landroid/graphics/PointF;

    goto :goto_e3

    nop

    :goto_33
    iget-object v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p0:Landroid/graphics/PointF;

    goto :goto_d8

    nop

    :goto_34
    goto :goto_1

    :goto_35
    goto :goto_69

    nop

    :goto_36
    if-nez v7, :cond_5

    goto :goto_4f

    :cond_5
    goto :goto_10d

    nop

    :goto_37
    invoke-virtual {v7, v10, v6}, Landroid/graphics/PointF;->set(FF)V

    goto :goto_72

    nop

    :goto_38
    iget-object v9, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p4:Landroid/graphics/PointF;

    goto :goto_bd

    nop

    :goto_39
    if-eq v12, v9, :cond_6

    goto :goto_95

    :cond_6
    goto :goto_2d

    nop

    :goto_3a
    add-float/2addr v10, v3

    goto :goto_3c

    nop

    :goto_3b
    invoke-virtual {v7, v4, v10}, Landroid/graphics/PointF;->set(FF)V

    goto :goto_3e

    nop

    :goto_3c
    invoke-virtual {v7, v10, v5}, Landroid/graphics/PointF;->set(FF)V

    goto :goto_8d

    nop

    :goto_3d
    iget-object v13, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p6:Landroid/graphics/PointF;

    goto :goto_f7

    nop

    :goto_3e
    iget-object v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p3:Landroid/graphics/PointF;

    goto :goto_c4

    nop

    :goto_3f
    move v5, v7

    goto :goto_96

    nop

    :goto_40
    iget-object v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p0:Landroid/graphics/PointF;

    goto :goto_af

    nop

    :goto_41
    sub-float v10, v6, v10

    goto :goto_c6

    nop

    :goto_42
    move v6, v5

    goto :goto_c8

    nop

    :goto_43
    if-ne v12, v11, :cond_7

    goto :goto_ba

    :cond_7
    :goto_44
    goto :goto_86

    nop

    :goto_45
    iget v1, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->radius:F

    goto :goto_84

    nop

    :goto_46
    iget-object v13, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p7:Landroid/graphics/PointF;

    goto :goto_a4

    nop

    :goto_47
    if-eq v12, v9, :cond_8

    goto :goto_4d

    :cond_8
    :goto_48
    goto :goto_8a

    nop

    :goto_49
    if-eq v12, v2, :cond_9

    goto :goto_1

    :cond_9
    :goto_4a
    goto :goto_a9

    nop

    :goto_4b
    iget-object v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p3:Landroid/graphics/PointF;

    goto :goto_d7

    nop

    :goto_4c
    goto :goto_1

    :goto_4d
    goto :goto_101

    nop

    :goto_4e
    if-eqz v11, :cond_a

    goto :goto_78

    :cond_a
    :goto_4f
    goto :goto_2e

    nop

    :goto_50
    add-float/2addr v10, v12

    goto :goto_1b

    nop

    :goto_51
    sub-float v10, v4, v10

    goto :goto_29

    nop

    :goto_52
    add-float v11, v3, v10

    goto :goto_105

    nop

    :goto_53
    iget v4, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->paddingEnd:F

    goto :goto_85

    nop

    :goto_54
    iget-object v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p1:Landroid/graphics/PointF;

    goto :goto_3

    nop

    :goto_55
    sub-float/2addr v11, v14

    goto :goto_9d

    nop

    :goto_56
    iget-object v9, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p2:Landroid/graphics/PointF;

    goto :goto_eb

    nop

    :goto_57
    iget v3, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->density:F

    goto :goto_d6

    nop

    :goto_58
    sub-float v6, v3, v4

    goto :goto_61

    nop

    :goto_59
    iget v12, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mArrowMode:I

    goto :goto_ac

    nop

    :goto_5a
    int-to-float v3, v3

    goto :goto_2f

    nop

    :goto_5b
    iget v2, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->density:F

    goto :goto_91

    nop

    :goto_5c
    if-eq v11, v2, :cond_b

    goto :goto_db

    :cond_b
    :goto_5d
    goto :goto_64

    nop

    :goto_5e
    add-float/2addr v11, v14

    goto :goto_cd

    nop

    :goto_5f
    if-ne v12, v9, :cond_c

    goto :goto_4a

    :cond_c
    :goto_60
    goto :goto_e7

    nop

    :goto_61
    iget v3, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->paddingStart:F

    goto :goto_53

    nop

    :goto_62
    iget v11, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mRtlMode:I

    goto :goto_a

    nop

    :goto_63
    iget-boolean v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mIsRtl:Z

    goto :goto_b1

    nop

    :goto_64
    if-nez v7, :cond_d

    goto :goto_b4

    :cond_d
    goto :goto_b3

    nop

    :goto_65
    iget v11, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mRtlMode:I

    goto :goto_4e

    nop

    :goto_66
    iget v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->radius:F

    goto :goto_3a

    nop

    :goto_67
    const/16 v2, 0x11

    goto :goto_109

    nop

    :goto_68
    div-float v14, v1, v14

    goto :goto_26

    nop

    :goto_69
    if-eqz v7, :cond_e

    goto :goto_60

    :cond_e
    goto :goto_5f

    nop

    :goto_6a
    iput v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mArrowHorizonOffset:F

    :goto_6b
    goto :goto_10

    nop

    :goto_6c
    if-eq v1, v2, :cond_f

    goto :goto_17

    :cond_f
    goto :goto_88

    nop

    :goto_6d
    iget v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mArrowMode:I

    goto :goto_cc

    nop

    :goto_6e
    move v7, v6

    goto :goto_42

    nop

    :goto_6f
    iget-object v12, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p5:Landroid/graphics/PointF;

    goto :goto_3d

    nop

    :goto_70
    if-eqz v7, :cond_10

    goto :goto_107

    :cond_10
    goto :goto_d3

    nop

    :goto_71
    mul-float v15, v12, v13

    goto :goto_c5

    nop

    :goto_72
    iget-object v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p4:Landroid/graphics/PointF;

    goto :goto_d1

    nop

    :goto_73
    invoke-direct/range {v0 .. v13}, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->drawRightArrow(FFFFFFLandroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;)V

    goto :goto_e9

    nop

    :goto_74
    sub-float v10, v4, v10

    goto :goto_37

    nop

    :goto_75
    iget v1, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->density:F

    goto :goto_e5

    nop

    :goto_76
    iget-object v8, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p3:Landroid/graphics/PointF;

    goto :goto_38

    nop

    :goto_77
    if-eq v11, v2, :cond_11

    goto :goto_98

    :cond_11
    :goto_78
    goto :goto_45

    nop

    :goto_79
    iget-object v13, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p6:Landroid/graphics/PointF;

    goto :goto_73

    nop

    :goto_7a
    invoke-virtual {v2, v0, v1}, Landroid/graphics/Canvas;->drawPath(Landroid/graphics/Path;Landroid/graphics/Paint;)V

    :goto_7b
    goto :goto_102

    nop

    :goto_7c
    if-nez v7, :cond_12

    goto :goto_5d

    :cond_12
    goto :goto_9e

    nop

    :goto_7d
    sub-float v10, v6, v10

    goto :goto_3b

    nop

    :goto_7e
    sub-float v11, v4, v10

    goto :goto_71

    nop

    :goto_7f
    if-eqz v7, :cond_13

    goto :goto_ea

    :cond_13
    goto :goto_da

    nop

    :goto_80
    iget-object v9, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p2:Landroid/graphics/PointF;

    goto :goto_108

    nop

    :goto_81
    iget-object v12, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p4:Landroid/graphics/PointF;

    goto :goto_de

    nop

    :goto_82
    iget-object v0, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mPath:Landroid/graphics/Path;

    goto :goto_dd

    nop

    :goto_83
    add-float/2addr v10, v5

    goto :goto_ec

    nop

    :goto_84
    iget v2, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->density:F

    goto :goto_40

    nop

    :goto_85
    sub-float v4, v1, v4

    goto :goto_6d

    nop

    :goto_86
    if-nez v7, :cond_14

    goto :goto_bf

    :cond_14
    goto :goto_b9

    nop

    :goto_87
    iget-object v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p3:Landroid/graphics/PointF;

    goto :goto_23

    nop

    :goto_88
    move v1, v2

    goto :goto_16

    nop

    :goto_89
    iget v4, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->paddingBottom:F

    goto :goto_58

    nop

    :goto_8a
    iget v1, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->radius:F

    goto :goto_e1

    nop

    :goto_8b
    if-eqz v7, :cond_15

    goto :goto_95

    :cond_15
    goto :goto_39

    nop

    :goto_8c
    iget v2, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->density:F

    goto :goto_33

    nop

    :goto_8d
    iget-object v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p1:Landroid/graphics/PointF;

    goto :goto_f3

    nop

    :goto_8e
    if-nez v7, :cond_16

    goto :goto_25

    :cond_16
    goto :goto_59

    nop

    :goto_8f
    int-to-float v1, v1

    goto :goto_93

    nop

    :goto_90
    iget v1, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->radius:F

    goto :goto_31

    nop

    :goto_91
    iget-object v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p0:Landroid/graphics/PointF;

    goto :goto_103

    nop

    :goto_92
    iget v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->radius:F

    goto :goto_41

    nop

    :goto_93
    invoke-virtual {v0}, Landroid/widget/LinearLayout;->getHeight()I

    move-result v3

    goto :goto_5a

    nop

    :goto_94
    if-eq v10, v2, :cond_17

    goto :goto_78

    :cond_17
    :goto_95
    goto :goto_f5

    nop

    :goto_96
    iget-object v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p2:Landroid/graphics/PointF;

    goto :goto_76

    nop

    :goto_97
    goto :goto_1

    :goto_98
    goto :goto_e2

    nop

    :goto_99
    const/16 v9, 0x12

    goto :goto_b2

    nop

    :goto_9a
    invoke-direct/range {v0 .. v14}, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->drawTopArrow(FFFFFFLandroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;)V

    goto :goto_a1

    nop

    :goto_9b
    iget-object v1, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mBackgroundPaint:Landroid/graphics/Paint;

    goto :goto_f1

    nop

    :goto_9c
    iget v11, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mRtlMode:I

    goto :goto_5c

    nop

    :goto_9d
    cmpl-float v7, v7, v11

    goto :goto_9

    nop

    :goto_9e
    if-eq v12, v9, :cond_18

    goto :goto_5d

    :cond_18
    goto :goto_9c

    nop

    :goto_9f
    iget-object v9, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p2:Landroid/graphics/PointF;

    goto :goto_d2

    nop

    :goto_a0
    iget-object v11, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p6:Landroid/graphics/PointF;

    goto :goto_0

    nop

    :goto_a1
    goto :goto_1

    :goto_a2
    goto :goto_1d

    nop

    :goto_a3
    iget-object v12, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p6:Landroid/graphics/PointF;

    goto :goto_46

    nop

    :goto_a4
    invoke-direct/range {v0 .. v13}, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->drawTopLeftArrow(FFFFFFLandroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;)V

    goto :goto_be

    nop

    :goto_a5
    if-eq v7, v8, :cond_19

    goto :goto_6b

    :cond_19
    :goto_a6
    goto :goto_18

    nop

    :goto_a7
    move-object/from16 v2, p1

    goto :goto_7a

    nop

    :goto_a8
    iput-boolean v1, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mIsRtl:Z

    goto :goto_c2

    nop

    :goto_a9
    iget v1, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->radius:F

    goto :goto_5b

    nop

    :goto_aa
    if-ltz v11, :cond_1a

    goto :goto_f0

    :cond_1a
    goto :goto_d5

    nop

    :goto_ab
    sub-float/2addr v7, v12

    goto :goto_10e

    nop

    :goto_ac
    if-eq v12, v11, :cond_1b

    goto :goto_25

    :cond_1b
    :goto_ad
    goto :goto_75

    nop

    :goto_ae
    if-eq v12, v10, :cond_1c

    goto :goto_98

    :cond_1c
    goto :goto_d0

    nop

    :goto_af
    iget-object v8, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p1:Landroid/graphics/PointF;

    goto :goto_2

    nop

    :goto_b0
    iget-object v9, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p2:Landroid/graphics/PointF;

    goto :goto_4b

    nop

    :goto_b1
    const/16 v10, 0xa

    goto :goto_70

    nop

    :goto_b2
    if-nez v7, :cond_1d

    goto :goto_4d

    :cond_1d
    goto :goto_47

    nop

    :goto_b3
    if-ne v12, v10, :cond_1e

    goto :goto_db

    :cond_1e
    :goto_b4
    goto :goto_7f

    nop

    :goto_b5
    iget-object v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p0:Landroid/graphics/PointF;

    goto :goto_19

    nop

    :goto_b6
    if-ne v7, v9, :cond_1f

    goto :goto_a6

    :cond_1f
    goto :goto_a5

    nop

    :goto_b7
    iget-object v11, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p6:Landroid/graphics/PointF;

    goto :goto_12

    nop

    :goto_b8
    invoke-super/range {p0 .. p1}, Landroid/widget/LinearLayout;->onDraw(Landroid/graphics/Canvas;)V

    goto :goto_dc

    nop

    :goto_b9
    if-eq v12, v10, :cond_20

    goto :goto_bf

    :cond_20
    :goto_ba
    goto :goto_fe

    nop

    :goto_bb
    const/16 v9, 0x8

    goto :goto_b6

    nop

    :goto_bc
    iget v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->radius:F

    goto :goto_7d

    nop

    :goto_bd
    iget-object v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p5:Landroid/graphics/PointF;

    goto :goto_b7

    nop

    :goto_be
    goto :goto_1

    :goto_bf
    goto :goto_e

    nop

    :goto_c0
    invoke-direct/range {v0 .. v13}, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->drawLeftArrow(FFFFFFLandroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;)V

    goto :goto_97

    nop

    :goto_c1
    if-nez v1, :cond_21

    goto :goto_20

    :cond_21
    goto :goto_1f

    nop

    :goto_c2
    iget-object v1, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mPath:Landroid/graphics/Path;

    goto :goto_c1

    nop

    :goto_c3
    iget-object v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p6:Landroid/graphics/PointF;

    goto :goto_10c

    nop

    :goto_c4
    iget v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->radius:F

    goto :goto_74

    nop

    :goto_c5
    sub-float/2addr v11, v15

    goto :goto_55

    nop

    :goto_c6
    invoke-virtual {v7, v3, v10}, Landroid/graphics/PointF;->set(FF)V

    goto :goto_c3

    nop

    :goto_c7
    iget v2, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->radius:F

    goto :goto_6e

    nop

    :goto_c8
    move v5, v4

    goto :goto_14

    nop

    :goto_c9
    iget v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->radius:F

    goto :goto_52

    nop

    :goto_ca
    if-eqz v7, :cond_22

    goto :goto_98

    :cond_22
    goto :goto_ae

    nop

    :goto_cb
    iget-object v9, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p3:Landroid/graphics/PointF;

    goto :goto_f

    nop

    :goto_cc
    const/16 v8, 0x10

    goto :goto_bb

    nop

    :goto_cd
    const/high16 v14, 0x40000000

    goto :goto_68

    nop

    :goto_ce
    if-ne v12, v2, :cond_23

    goto :goto_48

    :cond_23
    :goto_cf
    goto :goto_99

    nop

    :goto_d0
    iget v11, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mRtlMode:I

    goto :goto_77

    nop

    :goto_d1
    iget v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->radius:F

    goto :goto_fa

    nop

    :goto_d2
    iget-object v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p3:Landroid/graphics/PointF;

    goto :goto_1a

    nop

    :goto_d3
    iget v11, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mArrowMode:I

    goto :goto_106

    nop

    :goto_d4
    const/4 v2, 0x1

    goto :goto_6c

    nop

    :goto_d5
    add-float/2addr v10, v3

    goto :goto_15

    nop

    :goto_d6
    iget-object v8, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p0:Landroid/graphics/PointF;

    goto :goto_e0

    nop

    :goto_d7
    iget-object v11, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p4:Landroid/graphics/PointF;

    goto :goto_6f

    nop

    :goto_d8
    iget-object v8, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p1:Landroid/graphics/PointF;

    goto :goto_b0

    nop

    :goto_d9
    invoke-virtual {v7, v4, v10}, Landroid/graphics/PointF;->set(FF)V

    goto :goto_f6

    nop

    :goto_da
    if-eq v12, v9, :cond_24

    goto :goto_ea

    :cond_24
    :goto_db
    goto :goto_90

    nop

    :goto_dc
    invoke-static {v0}, Landroidx/core/view/ViewCompat;->getLayoutDirection(Landroid/view/View;)I

    move-result v1

    goto :goto_d4

    nop

    :goto_dd
    if-nez v0, :cond_25

    goto :goto_7b

    :cond_25
    goto :goto_a7

    nop

    :goto_de
    iget-object v13, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p5:Landroid/graphics/PointF;

    goto :goto_32

    nop

    :goto_df
    iget-object v12, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p5:Landroid/graphics/PointF;

    goto :goto_13

    nop

    :goto_e0
    iget-object v9, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p1:Landroid/graphics/PointF;

    goto :goto_e6

    nop

    :goto_e1
    iget v2, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->density:F

    goto :goto_7

    nop

    :goto_e2
    if-eqz v7, :cond_26

    goto :goto_ee

    :cond_26
    goto :goto_ed

    nop

    :goto_e3
    invoke-direct/range {v0 .. v14}, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->drawBottomArrow(FFFFFFFLandroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;Landroid/graphics/PointF;)V

    goto :goto_34

    nop

    :goto_e4
    iget-object v12, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p6:Landroid/graphics/PointF;

    goto :goto_5

    nop

    :goto_e5
    move v7, v6

    goto :goto_d

    nop

    :goto_e6
    iget-object v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p2:Landroid/graphics/PointF;

    goto :goto_2a

    nop

    :goto_e7
    if-nez v7, :cond_27

    goto :goto_1

    :cond_27
    goto :goto_49

    nop

    :goto_e8
    iget-object v11, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p5:Landroid/graphics/PointF;

    goto :goto_a3

    nop

    :goto_e9
    goto :goto_1

    :goto_ea
    goto :goto_67

    nop

    :goto_eb
    iget-object v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p3:Landroid/graphics/PointF;

    goto :goto_a0

    nop

    :goto_ec
    invoke-virtual {v7, v3, v10}, Landroid/graphics/PointF;->set(FF)V

    goto :goto_4

    nop

    :goto_ed
    if-ne v12, v10, :cond_28

    goto :goto_db

    :cond_28
    :goto_ee
    goto :goto_7c

    nop

    :goto_ef
    goto :goto_6b

    :goto_f0
    goto :goto_7e

    nop

    :goto_f1
    if-nez v1, :cond_29

    goto :goto_7b

    :cond_29
    goto :goto_82

    nop

    :goto_f2
    const/16 v11, 0x9

    goto :goto_8e

    nop

    :goto_f3
    iget v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->radius:F

    goto :goto_100

    nop

    :goto_f4
    move v3, v4

    goto :goto_2b

    nop

    :goto_f5
    const/16 v10, 0x40

    goto :goto_36

    nop

    :goto_f6
    iget-object v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p2:Landroid/graphics/PointF;

    goto :goto_bc

    nop

    :goto_f7
    iget-object v14, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p7:Landroid/graphics/PointF;

    goto :goto_9a

    nop

    :goto_f8
    iget v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->radius:F

    goto :goto_51

    nop

    :goto_f9
    iget v12, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->mArrowMode:I

    goto :goto_fc

    nop

    :goto_fa
    add-float/2addr v10, v3

    goto :goto_2c

    nop

    :goto_fb
    cmpg-float v11, v7, v11

    goto :goto_aa

    nop

    :goto_fc
    if-eq v12, v9, :cond_2a

    goto :goto_a2

    :cond_2a
    goto :goto_8c

    nop

    :goto_fd
    iget-object v7, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p5:Landroid/graphics/PointF;

    goto :goto_92

    nop

    :goto_fe
    iget v1, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->radius:F

    goto :goto_8

    nop

    :goto_ff
    iget-object v8, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p1:Landroid/graphics/PointF;

    goto :goto_80

    nop

    :goto_100
    add-float/2addr v10, v5

    goto :goto_d9

    nop

    :goto_101
    if-eq v12, v8, :cond_2b

    goto :goto_35

    :cond_2b
    goto :goto_c7

    nop

    :goto_102
    return-void

    :goto_103
    iget-object v8, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p1:Landroid/graphics/PointF;

    goto :goto_56

    nop

    :goto_104
    move v2, v3

    goto :goto_f4

    nop

    :goto_105
    iget v12, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->density:F

    goto :goto_11

    nop

    :goto_106
    if-ne v11, v10, :cond_2c

    goto :goto_ad

    :cond_2c
    :goto_107
    goto :goto_f2

    nop

    :goto_108
    iget-object v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->p4:Landroid/graphics/PointF;

    goto :goto_30

    nop

    :goto_109
    if-eqz v7, :cond_2d

    goto :goto_cf

    :cond_2d
    goto :goto_ce

    nop

    :goto_10a
    const/4 v1, 0x0

    :goto_10b
    goto :goto_a8

    nop

    :goto_10c
    iget v10, v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->radius:F

    goto :goto_83

    nop

    :goto_10d
    if-eq v12, v10, :cond_2e

    goto :goto_4f

    :cond_2e
    goto :goto_65

    nop

    :goto_10e
    sub-float/2addr v7, v14

    goto :goto_6a

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
