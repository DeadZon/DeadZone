TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/FontSizeAdjustView.smali'
CLASS_FALLBACK_NAMES = ['FontSizeAdjustView.smali']
CLASS_ANCHORS = ['.super Landroid/view/View;']

PATCHES = [
    {
        'id': 'com_android_provision_FontSizeAdjustView__onDraw',
        'method': '.method protected onDraw(Landroid/graphics/Canvas;)V',
        'method_name': 'onDraw',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/view/View;->onDraw(Landroid/graphics/Canvas;)V', 'iget v1, p0, Lcom/android/provision/FontSizeAdjustView;->mPointCount:I', 'if-ge v0, v1, :cond_1', 'iget v1, p0, Lcom/android/provision/FontSizeAdjustView;->mCurrentPointIndex:I', 'if-ne v0, v1, :cond_0', 'iget-object v1, p0, Lcom/android/provision/FontSizeAdjustView;->mPointPaint:Landroid/graphics/Paint;', 'iget v2, p0, Lcom/android/provision/FontSizeAdjustView;->mBigPointColor:I', 'invoke-virtual {v1, v2}, Landroid/graphics/Paint;->setColor(I)V'],
        'type': 'method_replace',
        'search': """.method protected onDraw(Landroid/graphics/Canvas;)V
    .registers 7

    invoke-super {p0, p1}, Landroid/view/View;->onDraw(Landroid/graphics/Canvas;)V

    const/4 v0, 0x0

    :goto_0
    iget v1, p0, Lcom/android/provision/FontSizeAdjustView;->mPointCount:I

    if-ge v0, v1, :cond_1

    iget v1, p0, Lcom/android/provision/FontSizeAdjustView;->mCurrentPointIndex:I

    if-ne v0, v1, :cond_0

    iget-object v1, p0, Lcom/android/provision/FontSizeAdjustView;->mPointPaint:Landroid/graphics/Paint;

    iget v2, p0, Lcom/android/provision/FontSizeAdjustView;->mBigPointColor:I

    invoke-virtual {v1, v2}, Landroid/graphics/Paint;->setColor(I)V

    iget-object v1, p0, Lcom/android/provision/FontSizeAdjustView;->mPointsXList:Ljava/util/List;

    invoke-interface {v1, v0}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Ljava/lang/Float;

    invoke-virtual {v1}, Ljava/lang/Float;->floatValue()F

    move-result v1

    iget v2, p0, Lcom/android/provision/FontSizeAdjustView;->mPointsY:F

    iget v3, p0, Lcom/android/provision/FontSizeAdjustView;->mBigPointsRadius:F

    iget-object v4, p0, Lcom/android/provision/FontSizeAdjustView;->mPointPaint:Landroid/graphics/Paint;

    invoke-virtual {p1, v1, v2, v3, v4}, Landroid/graphics/Canvas;->drawCircle(FFFLandroid/graphics/Paint;)V

    iget-object v1, p0, Lcom/android/provision/FontSizeAdjustView;->mPointPaint:Landroid/graphics/Paint;

    iget v2, p0, Lcom/android/provision/FontSizeAdjustView;->mBigPointCenterColor:I

    invoke-virtual {v1, v2}, Landroid/graphics/Paint;->setColor(I)V

    iget-object v1, p0, Lcom/android/provision/FontSizeAdjustView;->mPointsXList:Ljava/util/List;

    invoke-interface {v1, v0}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Ljava/lang/Float;

    invoke-virtual {v1}, Ljava/lang/Float;->floatValue()F

    move-result v1

    iget v2, p0, Lcom/android/provision/FontSizeAdjustView;->mPointsY:F

    iget v3, p0, Lcom/android/provision/FontSizeAdjustView;->mPointsRadius:F

    iget-object v4, p0, Lcom/android/provision/FontSizeAdjustView;->mPointPaint:Landroid/graphics/Paint;

    invoke-virtual {p1, v1, v2, v3, v4}, Landroid/graphics/Canvas;->drawCircle(FFFLandroid/graphics/Paint;)V

    goto :goto_1

    :cond_0
    iget-object v1, p0, Lcom/android/provision/FontSizeAdjustView;->mPointPaint:Landroid/graphics/Paint;

    iget v2, p0, Lcom/android/provision/FontSizeAdjustView;->mSmallPointColor:I

    invoke-virtual {v1, v2}, Landroid/graphics/Paint;->setColor(I)V

    iget-object v1, p0, Lcom/android/provision/FontSizeAdjustView;->mPointsXList:Ljava/util/List;

    invoke-interface {v1, v0}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Ljava/lang/Float;

    invoke-virtual {v1}, Ljava/lang/Float;->floatValue()F

    move-result v1

    iget v2, p0, Lcom/android/provision/FontSizeAdjustView;->mPointsY:F

    iget v3, p0, Lcom/android/provision/FontSizeAdjustView;->mPointsRadius:F

    iget-object v4, p0, Lcom/android/provision/FontSizeAdjustView;->mPointPaint:Landroid/graphics/Paint;

    invoke-virtual {p1, v1, v2, v3, v4}, Landroid/graphics/Canvas;->drawCircle(FFFLandroid/graphics/Paint;)V

    :goto_1
    add-int/lit8 v0, v0, 0x1

    goto :goto_0

    :cond_1
    return-void
.end method""",
        'replacement': """.method protected onDraw(Landroid/graphics/Canvas;)V
    .registers 7

    goto :goto_19

    nop

    :goto_0
    goto :goto_28

    :goto_1
    goto :goto_2c

    nop

    :goto_2
    iget v2, p0, Lcom/android/provision/FontSizeAdjustView;->mPointsY:F

    goto :goto_1c

    nop

    :goto_3
    check-cast v1, Ljava/lang/Float;

    goto :goto_8

    nop

    :goto_4
    invoke-interface {v1, v0}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v1

    goto :goto_13

    nop

    :goto_5
    invoke-virtual {p1, v1, v2, v3, v4}, Landroid/graphics/Canvas;->drawCircle(FFFLandroid/graphics/Paint;)V

    :goto_6
    goto :goto_b

    nop

    :goto_7
    iget v2, p0, Lcom/android/provision/FontSizeAdjustView;->mBigPointCenterColor:I

    goto :goto_1b

    nop

    :goto_8
    invoke-virtual {v1}, Ljava/lang/Float;->floatValue()F

    move-result v1

    goto :goto_10

    nop

    :goto_9
    goto :goto_6

    :goto_a
    goto :goto_21

    nop

    :goto_b
    add-int/lit8 v0, v0, 0x1

    goto :goto_0

    nop

    :goto_c
    iget v3, p0, Lcom/android/provision/FontSizeAdjustView;->mPointsRadius:F

    goto :goto_14

    nop

    :goto_d
    iget-object v4, p0, Lcom/android/provision/FontSizeAdjustView;->mPointPaint:Landroid/graphics/Paint;

    goto :goto_1d

    nop

    :goto_e
    invoke-interface {v1, v0}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v1

    goto :goto_25

    nop

    :goto_f
    iget v3, p0, Lcom/android/provision/FontSizeAdjustView;->mPointsRadius:F

    goto :goto_26

    nop

    :goto_10
    iget v2, p0, Lcom/android/provision/FontSizeAdjustView;->mPointsY:F

    goto :goto_c

    nop

    :goto_11
    invoke-virtual {p1, v1, v2, v3, v4}, Landroid/graphics/Canvas;->drawCircle(FFFLandroid/graphics/Paint;)V

    goto :goto_9

    nop

    :goto_12
    iget v1, p0, Lcom/android/provision/FontSizeAdjustView;->mPointCount:I

    goto :goto_2e

    nop

    :goto_13
    check-cast v1, Ljava/lang/Float;

    goto :goto_17

    nop

    :goto_14
    iget-object v4, p0, Lcom/android/provision/FontSizeAdjustView;->mPointPaint:Landroid/graphics/Paint;

    goto :goto_11

    nop

    :goto_15
    iget v2, p0, Lcom/android/provision/FontSizeAdjustView;->mPointsY:F

    goto :goto_f

    nop

    :goto_16
    invoke-interface {v1, v0}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v1

    goto :goto_3

    nop

    :goto_17
    invoke-virtual {v1}, Ljava/lang/Float;->floatValue()F

    move-result v1

    goto :goto_2

    nop

    :goto_18
    iget v2, p0, Lcom/android/provision/FontSizeAdjustView;->mSmallPointColor:I

    goto :goto_1a

    nop

    :goto_19
    invoke-super {p0, p1}, Landroid/view/View;->onDraw(Landroid/graphics/Canvas;)V

    goto :goto_27

    nop

    :goto_1a
    invoke-virtual {v1, v2}, Landroid/graphics/Paint;->setColor(I)V

    goto :goto_23

    nop

    :goto_1b
    invoke-virtual {v1, v2}, Landroid/graphics/Paint;->setColor(I)V

    goto :goto_1f

    nop

    :goto_1c
    iget v3, p0, Lcom/android/provision/FontSizeAdjustView;->mBigPointsRadius:F

    goto :goto_d

    nop

    :goto_1d
    invoke-virtual {p1, v1, v2, v3, v4}, Landroid/graphics/Canvas;->drawCircle(FFFLandroid/graphics/Paint;)V

    goto :goto_29

    nop

    :goto_1e
    iget v2, p0, Lcom/android/provision/FontSizeAdjustView;->mBigPointColor:I

    goto :goto_2a

    nop

    :goto_1f
    iget-object v1, p0, Lcom/android/provision/FontSizeAdjustView;->mPointsXList:Ljava/util/List;

    goto :goto_16

    nop

    :goto_20
    iget v1, p0, Lcom/android/provision/FontSizeAdjustView;->mCurrentPointIndex:I

    goto :goto_24

    nop

    :goto_21
    iget-object v1, p0, Lcom/android/provision/FontSizeAdjustView;->mPointPaint:Landroid/graphics/Paint;

    goto :goto_18

    nop

    :goto_22
    iget-object v1, p0, Lcom/android/provision/FontSizeAdjustView;->mPointsXList:Ljava/util/List;

    goto :goto_4

    nop

    :goto_23
    iget-object v1, p0, Lcom/android/provision/FontSizeAdjustView;->mPointsXList:Ljava/util/List;

    goto :goto_e

    nop

    :goto_24
    if-eq v0, v1, :cond_0

    goto :goto_a

    :cond_0
    goto :goto_2d

    nop

    :goto_25
    check-cast v1, Ljava/lang/Float;

    goto :goto_2b

    nop

    :goto_26
    iget-object v4, p0, Lcom/android/provision/FontSizeAdjustView;->mPointPaint:Landroid/graphics/Paint;

    goto :goto_5

    nop

    :goto_27
    const/4 v0, 0x0

    :goto_28
    goto :goto_12

    nop

    :goto_29
    iget-object v1, p0, Lcom/android/provision/FontSizeAdjustView;->mPointPaint:Landroid/graphics/Paint;

    goto :goto_7

    nop

    :goto_2a
    invoke-virtual {v1, v2}, Landroid/graphics/Paint;->setColor(I)V

    goto :goto_22

    nop

    :goto_2b
    invoke-virtual {v1}, Ljava/lang/Float;->floatValue()F

    move-result v1

    goto :goto_15

    nop

    :goto_2c
    return-void

    :goto_2d
    iget-object v1, p0, Lcom/android/provision/FontSizeAdjustView;->mPointPaint:Landroid/graphics/Paint;

    goto :goto_1e

    nop

    :goto_2e
    if-lt v0, v1, :cond_1

    goto :goto_1

    :cond_1
    goto :goto_20

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_FontSizeAdjustView__onLayout',
        'method': '.method protected onLayout(ZIIII)V',
        'method_name': 'onLayout',
        'method_anchors': ['invoke-super/range {p0 .. p5}, Landroid/view/View;->onLayout(ZIIII)V', 'invoke-virtual {p0}, Landroid/view/View;->getHeight()I', 'iput p1, p0, Lcom/android/provision/FontSizeAdjustView;->mPointsY:F', 'invoke-virtual {p0}, Landroid/view/View;->getWidth()I', 'invoke-virtual {p0}, Landroid/view/View;->getHeight()I', 'iget p2, p0, Lcom/android/provision/FontSizeAdjustView;->mPointCount:I', 'iget-object p2, p0, Lcom/android/provision/FontSizeAdjustView;->mPointsXList:Ljava/util/List;', 'invoke-interface {p2}, Ljava/util/List;->clear()V'],
        'type': 'method_replace',
        'search': """.method protected onLayout(ZIIII)V
    .registers 6

    invoke-super/range {p0 .. p5}, Landroid/view/View;->onLayout(ZIIII)V

    invoke-virtual {p0}, Landroid/view/View;->getHeight()I

    move-result p1

    div-int/lit8 p1, p1, 0x2

    int-to-float p1, p1

    iput p1, p0, Lcom/android/provision/FontSizeAdjustView;->mPointsY:F

    invoke-virtual {p0}, Landroid/view/View;->getWidth()I

    move-result p1

    invoke-virtual {p0}, Landroid/view/View;->getHeight()I

    move-result p2

    sub-int/2addr p1, p2

    iget p2, p0, Lcom/android/provision/FontSizeAdjustView;->mPointCount:I

    add-int/lit8 p2, p2, -0x1

    div-int/2addr p1, p2

    int-to-float p1, p1

    iget-object p2, p0, Lcom/android/provision/FontSizeAdjustView;->mPointsXList:Ljava/util/List;

    invoke-interface {p2}, Ljava/util/List;->clear()V

    const/4 p2, 0x0

    :goto_0
    iget p3, p0, Lcom/android/provision/FontSizeAdjustView;->mPointCount:I

    if-ge p2, p3, :cond_0

    iget-object p3, p0, Lcom/android/provision/FontSizeAdjustView;->mPointsXList:Ljava/util/List;

    invoke-virtual {p0}, Landroid/view/View;->getHeight()I

    move-result p4

    div-int/lit8 p4, p4, 0x2

    int-to-float p4, p4

    int-to-float p5, p2

    mul-float/2addr p5, p1

    add-float/2addr p4, p5

    invoke-static {p4}, Ljava/lang/Float;->valueOf(F)Ljava/lang/Float;

    move-result-object p4

    invoke-interface {p3, p4}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    add-int/lit8 p2, p2, 0x1

    goto :goto_0

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onLayout(ZIIII)V
    .registers 6

    goto :goto_1b

    nop

    :goto_0
    iget-object p2, p0, Lcom/android/provision/FontSizeAdjustView;->mPointsXList:Ljava/util/List;

    goto :goto_b

    nop

    :goto_1
    return-void

    :goto_2
    sub-int/2addr p1, p2

    goto :goto_f

    nop

    :goto_3
    iget p3, p0, Lcom/android/provision/FontSizeAdjustView;->mPointCount:I

    goto :goto_d

    nop

    :goto_4
    invoke-static {p4}, Ljava/lang/Float;->valueOf(F)Ljava/lang/Float;

    move-result-object p4

    goto :goto_5

    nop

    :goto_5
    invoke-interface {p3, p4}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    goto :goto_1a

    nop

    :goto_6
    invoke-virtual {p0}, Landroid/view/View;->getHeight()I

    move-result p4

    goto :goto_16

    nop

    :goto_7
    goto :goto_1d

    :goto_8
    goto :goto_1

    nop

    :goto_9
    mul-float/2addr p5, p1

    goto :goto_a

    nop

    :goto_a
    add-float/2addr p4, p5

    goto :goto_4

    nop

    :goto_b
    invoke-interface {p2}, Ljava/util/List;->clear()V

    goto :goto_1c

    nop

    :goto_c
    invoke-virtual {p0}, Landroid/view/View;->getHeight()I

    move-result p2

    goto :goto_2

    nop

    :goto_d
    if-lt p2, p3, :cond_0

    goto :goto_8

    :cond_0
    goto :goto_14

    nop

    :goto_e
    invoke-virtual {p0}, Landroid/view/View;->getHeight()I

    move-result p1

    goto :goto_18

    nop

    :goto_f
    iget p2, p0, Lcom/android/provision/FontSizeAdjustView;->mPointCount:I

    goto :goto_19

    nop

    :goto_10
    int-to-float p4, p4

    goto :goto_12

    nop

    :goto_11
    div-int/2addr p1, p2

    goto :goto_1e

    nop

    :goto_12
    int-to-float p5, p2

    goto :goto_9

    nop

    :goto_13
    iput p1, p0, Lcom/android/provision/FontSizeAdjustView;->mPointsY:F

    goto :goto_17

    nop

    :goto_14
    iget-object p3, p0, Lcom/android/provision/FontSizeAdjustView;->mPointsXList:Ljava/util/List;

    goto :goto_6

    nop

    :goto_15
    int-to-float p1, p1

    goto :goto_13

    nop

    :goto_16
    div-int/lit8 p4, p4, 0x2

    goto :goto_10

    nop

    :goto_17
    invoke-virtual {p0}, Landroid/view/View;->getWidth()I

    move-result p1

    goto :goto_c

    nop

    :goto_18
    div-int/lit8 p1, p1, 0x2

    goto :goto_15

    nop

    :goto_19
    add-int/lit8 p2, p2, -0x1

    goto :goto_11

    nop

    :goto_1a
    add-int/lit8 p2, p2, 0x1

    goto :goto_7

    nop

    :goto_1b
    invoke-super/range {p0 .. p5}, Landroid/view/View;->onLayout(ZIIII)V

    goto :goto_e

    nop

    :goto_1c
    const/4 p2, 0x0

    :goto_1d
    goto :goto_3

    nop

    :goto_1e
    int-to-float p1, p1

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
