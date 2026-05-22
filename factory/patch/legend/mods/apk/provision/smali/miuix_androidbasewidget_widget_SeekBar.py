TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/androidbasewidget/widget/SeekBar.smali'
CLASS_FALLBACK_NAMES = ['SeekBar.smali']
CLASS_ANCHORS = ['.super Landroidx/appcompat/widget/AppCompatSeekBar;', '.field private static final PROPERTY_DRAW_PROGRESS:Lmiuix/animation/property/IntValueProperty;', '.field private static final PROPERTY_PROGRESS:Lmiuix/animation/property/IntValueProperty;']

PATCHES = [
    {
        'id': 'miuix_androidbasewidget_widget_SeekBar__onDraw',
        'method': '.method protected declared-synchronized onDraw(Landroid/graphics/Canvas;)V',
        'method_name': 'onDraw',
        'method_anchors': ['iget-boolean v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mIsThumbTheme:Z', 'if-eqz v2, :cond_1d', 'iget-object v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mOvalDrawable:Landroid/graphics/drawable/Drawable;', 'if-eqz v2, :cond_1', 'invoke-virtual {v1}, Landroid/widget/SeekBar;->isEnabled()Z', 'if-nez v2, :cond_0', 'iget-object v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mOvalDrawable:Landroid/graphics/drawable/Drawable;', 'invoke-virtual {v2, v3}, Landroid/graphics/drawable/Drawable;->setAlpha(I)V'],
        'type': 'method_replace',
        'search': """.method protected declared-synchronized onDraw(Landroid/graphics/Canvas;)V
    .registers 22

    move-object/from16 v1, p0

    move-object/from16 v0, p1

    monitor-enter p0

    :try_start_0
    iget-boolean v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mIsThumbTheme:Z

    if-eqz v2, :cond_1d

    iget-object v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mOvalDrawable:Landroid/graphics/drawable/Drawable;

    if-eqz v2, :cond_1

    invoke-virtual {v1}, Landroid/widget/SeekBar;->isEnabled()Z

    move-result v2

    if-nez v2, :cond_0

    iget-object v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mOvalDrawable:Landroid/graphics/drawable/Drawable;

    const/16 v3, 0xb2

    invoke-virtual {v2, v3}, Landroid/graphics/drawable/Drawable;->setAlpha(I)V

    goto :goto_0

    :catchall_0
    move-exception v0

    goto :goto_f

    :cond_0
    iget-object v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mOvalDrawable:Landroid/graphics/drawable/Drawable;

    const/16 v3, 0xff

    invoke-virtual {v2, v3}, Landroid/graphics/drawable/Drawable;->setAlpha(I)V

    :cond_1
    :goto_0
    invoke-static {v1}, Landroidx/core/view/ViewCompat;->getLayoutDirection(Landroid/view/View;)I

    move-result v2

    const/4 v4, 0x1

    if-ne v2, v4, :cond_2

    move v2, v4

    goto :goto_1

    :cond_2
    const/4 v2, 0x0

    :goto_1
    invoke-virtual {v1}, Landroid/widget/SeekBar;->getWidth()I

    move-result v5

    int-to-float v5, v5

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getMaxHeight()I

    move-result v6

    int-to-float v6, v6

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getWidth()I

    move-result v7

    int-to-float v7, v7

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getResources()Landroid/content/res/Resources;

    move-result-object v8

    sget v9, Lmiuix/androidbasewidget/R$dimen;->miuix_appcompat_seekbar_progress_custom_bg_radius:I

    invoke-virtual {v8, v9}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I

    move-result v8

    int-to-float v8, v8

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingTop()I

    move-result v9

    int-to-float v9, v9

    add-float v10, v9, v6

    invoke-direct {v1}, Lmiuix/androidbasewidget/widget/SeekBar;->getMinWrapper()I

    move-result v11

    const/high16 v12, 0x3f800000

    if-eqz v2, :cond_3

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getMax()I

    move-result v13

    int-to-float v13, v13

    iget v14, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mDrawProgress:F

    sub-float/2addr v13, v14

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getMax()I

    move-result v14

    sub-int/2addr v14, v11

    int-to-float v14, v14

    mul-float/2addr v14, v12

    div-float/2addr v13, v14

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingStart()I

    move-result v14

    int-to-float v14, v14

    sub-float v14, v5, v14

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingEnd()I

    move-result v15

    int-to-float v15, v15

    sub-float/2addr v14, v15

    mul-float/2addr v13, v14

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingEnd()I

    move-result v14

    :goto_2
    int-to-float v14, v14

    add-float/2addr v13, v14

    goto :goto_3

    :cond_3
    iget v13, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mDrawProgress:F

    int-to-float v14, v11

    sub-float/2addr v13, v14

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getMax()I

    move-result v14

    sub-int/2addr v14, v11

    int-to-float v14, v14

    div-float/2addr v13, v14

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingStart()I

    move-result v14

    int-to-float v14, v14

    sub-float v14, v5, v14

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingEnd()I

    move-result v15

    int-to-float v15, v15

    sub-float/2addr v14, v15

    mul-float/2addr v13, v14

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingStart()I

    move-result v14

    goto :goto_2

    :goto_3
    iget-boolean v14, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mBalanceEnabled:Z

    if-eqz v14, :cond_5

    if-eqz v2, :cond_4

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getMax()I

    move-result v14

    iget v15, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mBalanceProgress:I

    sub-int/2addr v14, v15

    int-to-float v14, v14

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getMax()I

    move-result v15

    sub-int/2addr v15, v11

    int-to-float v15, v15

    mul-float/2addr v15, v12

    div-float/2addr v14, v15

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingStart()I

    move-result v12

    int-to-float v12, v12

    sub-float v12, v5, v12

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingEnd()I

    move-result v15

    int-to-float v15, v15

    sub-float/2addr v12, v15

    mul-float/2addr v14, v12

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingEnd()I

    move-result v12

    int-to-float v12, v12

    add-float/2addr v14, v12

    goto :goto_4

    :cond_4
    iget v12, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mBalanceProgress:I

    sub-int/2addr v12, v11

    int-to-float v12, v12

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getMax()I

    move-result v14

    sub-int/2addr v14, v11

    int-to-float v14, v14

    div-float/2addr v12, v14

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingStart()I

    move-result v14

    int-to-float v14, v14

    sub-float v14, v5, v14

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingEnd()I

    move-result v15

    int-to-float v15, v15

    sub-float/2addr v14, v15

    mul-float/2addr v12, v14

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingStart()I

    move-result v14

    int-to-float v14, v14

    add-float/2addr v14, v12

    goto :goto_4

    :cond_5
    const/4 v14, 0x0

    :goto_4
    iget v12, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mDefaultScalePrimaryColor:I

    iget v15, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mDefaultScaleSecondaryColor:I

    const/high16 v16, 0x40000000

    div-float v6, v6, v16

    add-float/2addr v6, v9

    iget v3, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mThumbHeight:I

    int-to-float v3, v3

    div-float v3, v3, v16

    sub-float v3, v6, v3

    float-to-int v3, v3

    iget-object v4, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mBackgroundDrawable:Landroid/graphics/drawable/Drawable;

    if-nez v4, :cond_8

    move/from16 v17, v2

    iget-object v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mProgressDrawable:Landroid/graphics/drawable/Drawable;

    if-eqz v2, :cond_6

    goto :goto_5

    :cond_6
    iget-object v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mLayerDrawable:Landroid/graphics/drawable/Drawable;

    if-eqz v2, :cond_7

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingStart()I

    move-result v4

    int-to-float v4, v4

    sub-float/2addr v4, v8

    float-to-int v4, v4

    float-to-int v7, v9

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingEnd()I

    move-result v9

    int-to-float v9, v9

    sub-float v9, v5, v9

    add-float/2addr v9, v8

    float-to-int v8, v9

    float-to-int v9, v10

    invoke-virtual {v2, v4, v7, v8, v9}, Landroid/graphics/drawable/Drawable;->setBounds(IIII)V

    iget-object v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mLayerDrawable:Landroid/graphics/drawable/Drawable;

    invoke-virtual {v2, v0}, Landroid/graphics/drawable/Drawable;->draw(Landroid/graphics/Canvas;)V

    :cond_7
    move/from16 v18, v5

    goto :goto_8

    :cond_8
    move/from16 v17, v2

    :goto_5
    if-eqz v4, :cond_9

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingStart()I

    move-result v2

    int-to-float v2, v2

    sub-float/2addr v2, v8

    float-to-int v2, v2

    move/from16 v18, v5

    float-to-int v5, v9

    move/from16 v19, v7

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingEnd()I

    move-result v7

    int-to-float v7, v7

    sub-float v7, v19, v7

    add-float/2addr v7, v8

    float-to-int v7, v7

    move/from16 v19, v8

    float-to-int v8, v10

    invoke-virtual {v4, v2, v5, v7, v8}, Landroid/graphics/drawable/Drawable;->setBounds(IIII)V

    iget-object v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mBackgroundDrawable:Landroid/graphics/drawable/Drawable;

    invoke-virtual {v2, v0}, Landroid/graphics/drawable/Drawable;->draw(Landroid/graphics/Canvas;)V

    goto :goto_6

    :cond_9
    move/from16 v18, v5

    move/from16 v19, v8

    :goto_6
    iget-object v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mProgressDrawable:Landroid/graphics/drawable/Drawable;

    if-eqz v2, :cond_f

    if-eqz v17, :cond_c

    iget-boolean v4, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mBalanceEnabled:Z

    if-eqz v4, :cond_b

    cmpl-float v4, v13, v14

    if-lez v4, :cond_a

    sub-float v14, v14, v19

    float-to-int v4, v14

    float-to-int v5, v9

    add-float v8, v13, v19

    float-to-int v7, v8

    float-to-int v8, v10

    invoke-virtual {v2, v4, v5, v7, v8}, Landroid/graphics/drawable/Drawable;->setBounds(IIII)V

    goto :goto_7

    :cond_a
    sub-float v4, v13, v19

    float-to-int v4, v4

    float-to-int v5, v9

    add-float v14, v14, v19

    float-to-int v7, v14

    float-to-int v8, v10

    invoke-virtual {v2, v4, v5, v7, v8}, Landroid/graphics/drawable/Drawable;->setBounds(IIII)V

    goto :goto_7

    :cond_b
    sub-float v4, v13, v19

    float-to-int v4, v4

    float-to-int v5, v9

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingEnd()I

    move-result v7

    int-to-float v7, v7

    sub-float v7, v18, v7

    add-float v7, v7, v19

    float-to-int v7, v7

    float-to-int v8, v10

    invoke-virtual {v2, v4, v5, v7, v8}, Landroid/graphics/drawable/Drawable;->setBounds(IIII)V

    goto :goto_7

    :cond_c
    iget-boolean v4, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mBalanceEnabled:Z

    if-eqz v4, :cond_e

    cmpl-float v4, v13, v14

    if-lez v4, :cond_d

    sub-float v14, v14, v19

    float-to-int v4, v14

    float-to-int v5, v9

    add-float v8, v13, v19

    float-to-int v7, v8

    float-to-int v8, v10

    invoke-virtual {v2, v4, v5, v7, v8}, Landroid/graphics/drawable/Drawable;->setBounds(IIII)V

    goto :goto_7

    :cond_d
    sub-float v4, v13, v19

    float-to-int v4, v4

    float-to-int v5, v9

    add-float v14, v14, v19

    float-to-int v7, v14

    float-to-int v8, v10

    invoke-virtual {v2, v4, v5, v7, v8}, Landroid/graphics/drawable/Drawable;->setBounds(IIII)V

    goto :goto_7

    :cond_e
    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingStart()I

    move-result v4

    int-to-float v4, v4

    sub-float v4, v4, v19

    float-to-int v4, v4

    float-to-int v5, v9

    add-float v8, v13, v19

    float-to-int v7, v8

    float-to-int v8, v10

    invoke-virtual {v2, v4, v5, v7, v8}, Landroid/graphics/drawable/Drawable;->setBounds(IIII)V

    :goto_7
    iget-object v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mProgressDrawable:Landroid/graphics/drawable/Drawable;

    invoke-virtual {v2, v0}, Landroid/graphics/drawable/Drawable;->draw(Landroid/graphics/Canvas;)V

    :cond_f
    :goto_8
    iget-boolean v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mMiddleEnabled:Z

    if-eqz v2, :cond_10

    iget-boolean v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mBalanceEnabled:Z

    if-nez v2, :cond_10

    iget v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mProgress:I

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getMax()I

    move-result v4

    sub-int/2addr v4, v11

    div-int/lit8 v4, v4, 0x2

    add-int/2addr v4, v11

    if-ge v2, v4, :cond_10

    iget-object v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mPaint:Landroid/graphics/Paint;

    invoke-virtual {v2, v15}, Landroid/graphics/Paint;->setColor(I)V

    div-float v5, v18, v16

    iget v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mScaleRadius:F

    iget-object v4, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mPaint:Landroid/graphics/Paint;

    invoke-virtual {v0, v5, v6, v2, v4}, Landroid/graphics/Canvas;->drawCircle(FFFLandroid/graphics/Paint;)V

    :cond_10
    iget-boolean v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mScaleEnabled:Z

    if-eqz v2, :cond_17

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getMax()I

    move-result v2

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingStart()I

    move-result v4

    int-to-float v4, v4

    sub-float v5, v18, v4

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingEnd()I

    move-result v4

    int-to-float v4, v4

    sub-float/2addr v5, v4

    int-to-float v4, v2

    div-float/2addr v5, v4

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getLayoutDirection()I

    move-result v4

    const/4 v7, 0x0

    :goto_9
    if-gt v7, v2, :cond_17

    iget v8, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mProgress:I

    if-eq v7, v8, :cond_13

    int-to-float v8, v7

    iget v9, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mDrawProgress:F

    cmpg-float v10, v8, v9

    if-gez v10, :cond_12

    iget-object v8, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mPaint:Landroid/graphics/Paint;

    invoke-virtual {v8, v12}, Landroid/graphics/Paint;->setColor(I)V

    :cond_11
    :goto_a
    const/4 v8, 0x1

    goto :goto_b

    :cond_12
    cmpl-float v8, v8, v9

    if-lez v8, :cond_11

    iget-object v8, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mPaint:Landroid/graphics/Paint;

    invoke-virtual {v8, v15}, Landroid/graphics/Paint;->setColor(I)V

    goto :goto_a

    :cond_13
    int-to-float v9, v8

    iget v10, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mDrawProgress:F

    cmpl-float v9, v9, v10

    if-lez v9, :cond_14

    iget-object v8, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mPaint:Landroid/graphics/Paint;

    invoke-virtual {v8, v15}, Landroid/graphics/Paint;->setColor(I)V

    goto :goto_a

    :cond_14
    int-to-float v8, v8

    cmpl-float v8, v8, v10

    if-nez v8, :cond_15

    iget-object v8, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mPaint:Landroid/graphics/Paint;

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getResources()Landroid/content/res/Resources;

    move-result-object v9

    sget v10, Lmiuix/androidbasewidget/R$color;->miuix_appcompat_transparent:I

    invoke-virtual {v9, v10}, Landroid/content/res/Resources;->getColor(I)I

    move-result v9

    invoke-virtual {v8, v9}, Landroid/graphics/Paint;->setColor(I)V

    goto :goto_a

    :cond_15
    iget-object v8, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mPaint:Landroid/graphics/Paint;

    invoke-virtual {v8, v12}, Landroid/graphics/Paint;->setColor(I)V

    goto :goto_a

    :goto_b
    if-ne v4, v8, :cond_16

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingEnd()I

    move-result v9

    int-to-float v9, v9

    sub-float v9, v18, v9

    int-to-float v10, v7

    mul-float/2addr v10, v5

    sub-float/2addr v9, v10

    goto :goto_c

    :cond_16
    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingStart()I

    move-result v9

    int-to-float v9, v9

    int-to-float v10, v7

    mul-float/2addr v10, v5

    add-float/2addr v9, v10

    :goto_c
    iget v10, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mScaleRadius:F

    iget-object v14, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mPaint:Landroid/graphics/Paint;

    invoke-virtual {v0, v9, v6, v10, v14}, Landroid/graphics/Canvas;->drawCircle(FFFLandroid/graphics/Paint;)V

    add-int/lit8 v7, v7, 0x1

    goto :goto_9

    :cond_17
    iget-boolean v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mMiddleEnabled:Z

    if-nez v2, :cond_18

    iget-boolean v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mBalanceEnabled:Z

    if-eqz v2, :cond_1c

    :cond_18
    iget-boolean v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mBalanceEnabled:Z

    const v4, 0x3e4ccccd

    if-eqz v2, :cond_1b

    iget v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mDrawProgress:F

    iget v5, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mBalanceProgress:I

    int-to-float v5, v5

    cmpl-float v5, v2, v5

    if-nez v5, :cond_19

    iget-object v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mPaint:Landroid/graphics/Paint;

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getResources()Landroid/content/res/Resources;

    move-result-object v4

    sget v5, Lmiuix/androidbasewidget/R$color;->miuix_appcompat_transparent:I

    invoke-virtual {v4, v5}, Landroid/content/res/Resources;->getColor(I)I

    move-result v4

    invoke-virtual {v2, v4}, Landroid/graphics/Paint;->setColor(I)V

    div-float v5, v18, v16

    iget v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mScaleRadius:F

    iget-object v4, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mPaint:Landroid/graphics/Paint;

    invoke-virtual {v0, v5, v6, v2, v4}, Landroid/graphics/Canvas;->drawCircle(FFFLandroid/graphics/Paint;)V

    goto :goto_d

    :cond_19
    invoke-virtual {v1}, Landroid/widget/SeekBar;->getMax()I

    move-result v5

    sub-int/2addr v5, v11

    int-to-float v5, v5

    div-float v5, v5, v16

    int-to-float v7, v11

    add-float/2addr v5, v7

    add-float/2addr v5, v4

    cmpl-float v2, v2, v5

    if-gtz v2, :cond_1a

    iget v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mDrawProgress:F

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getMax()I

    move-result v5

    sub-int/2addr v5, v11

    int-to-float v5, v5

    div-float v5, v5, v16

    add-float/2addr v5, v7

    sub-float/2addr v5, v4

    cmpg-float v2, v2, v5

    if-gez v2, :cond_1c

    :cond_1a
    iget-object v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mPaint:Landroid/graphics/Paint;

    invoke-virtual {v2, v12}, Landroid/graphics/Paint;->setColor(I)V

    div-float v5, v18, v16

    iget v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mScaleRadius:F

    iget-object v4, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mPaint:Landroid/graphics/Paint;

    invoke-virtual {v0, v5, v6, v2, v4}, Landroid/graphics/Canvas;->drawCircle(FFFLandroid/graphics/Paint;)V

    goto :goto_d

    :cond_1b
    iget v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mDrawProgress:F

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getMax()I

    move-result v5

    sub-int/2addr v5, v11

    int-to-float v5, v5

    div-float v5, v5, v16

    int-to-float v7, v11

    add-float/2addr v5, v7

    add-float/2addr v5, v4

    cmpl-float v2, v2, v5

    if-lez v2, :cond_1c

    iget-object v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mPaint:Landroid/graphics/Paint;

    invoke-virtual {v2, v12}, Landroid/graphics/Paint;->setColor(I)V

    div-float v5, v18, v16

    iget v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mScaleRadius:F

    iget-object v4, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mPaint:Landroid/graphics/Paint;

    invoke-virtual {v0, v5, v6, v2, v4}, Landroid/graphics/Canvas;->drawCircle(FFFLandroid/graphics/Paint;)V

    :cond_1c
    :goto_d
    iget-object v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mThumbDrawable:Landroid/graphics/drawable/Drawable;

    if-eqz v2, :cond_1e

    iget v4, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mThumbWidth:I

    int-to-float v5, v4

    div-float v5, v5, v16

    sub-float v5, v13, v5

    float-to-int v5, v5

    int-to-float v4, v4

    div-float v4, v4, v16

    add-float/2addr v13, v4

    float-to-int v4, v13

    iget v6, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mThumbHeight:I

    add-int/2addr v6, v3

    invoke-virtual {v2, v5, v3, v4, v6}, Landroid/graphics/drawable/Drawable;->setBounds(IIII)V

    iget-object v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mThumbDrawable:Landroid/graphics/drawable/Drawable;

    invoke-virtual {v2, v0}, Landroid/graphics/drawable/Drawable;->draw(Landroid/graphics/Canvas;)V

    goto :goto_e

    :cond_1d
    invoke-super/range {p0 .. p1}, Landroidx/appcompat/widget/AppCompatSeekBar;->onDraw(Landroid/graphics/Canvas;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    :cond_1e
    :goto_e
    monitor-exit p0

    return-void

    :goto_f
    :try_start_1
    monitor-exit p0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    throw v0
.end method""",
        'replacement': """.method protected declared-synchronized onDraw(Landroid/graphics/Canvas;)V
    .registers 22

    goto :goto_2

    nop

    :goto_0
    return-void

    :goto_1
    :try_start_0
    monitor-exit p0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_15

    nop

    :goto_2
    move-object/from16 v1, p0

    goto :goto_14

    nop

    :goto_3
    monitor-enter p0

    :try_start_1
    iget-boolean v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mIsThumbTheme:Z

    if-eqz v2, :cond_1d

    iget-object v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mOvalDrawable:Landroid/graphics/drawable/Drawable;

    if-eqz v2, :cond_1

    invoke-virtual {v1}, Landroid/widget/SeekBar;->isEnabled()Z

    move-result v2

    if-nez v2, :cond_0

    iget-object v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mOvalDrawable:Landroid/graphics/drawable/Drawable;

    const/16 v3, 0xb2

    invoke-virtual {v2, v3}, Landroid/graphics/drawable/Drawable;->setAlpha(I)V

    goto :goto_4

    :catchall_0
    move-exception v0

    goto :goto_1

    :cond_0
    iget-object v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mOvalDrawable:Landroid/graphics/drawable/Drawable;

    const/16 v3, 0xff

    invoke-virtual {v2, v3}, Landroid/graphics/drawable/Drawable;->setAlpha(I)V

    :cond_1
    :goto_4
    invoke-static {v1}, Landroidx/core/view/ViewCompat;->getLayoutDirection(Landroid/view/View;)I

    move-result v2

    const/4 v4, 0x1

    if-ne v2, v4, :cond_2

    move v2, v4

    goto :goto_5

    :cond_2
    const/4 v2, 0x0

    :goto_5
    invoke-virtual {v1}, Landroid/widget/SeekBar;->getWidth()I

    move-result v5

    int-to-float v5, v5

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getMaxHeight()I

    move-result v6

    int-to-float v6, v6

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getWidth()I

    move-result v7

    int-to-float v7, v7

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getResources()Landroid/content/res/Resources;

    move-result-object v8

    sget v9, Lmiuix/androidbasewidget/R$dimen;->miuix_appcompat_seekbar_progress_custom_bg_radius:I

    invoke-virtual {v8, v9}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I

    move-result v8

    int-to-float v8, v8

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingTop()I

    move-result v9

    int-to-float v9, v9

    add-float v10, v9, v6

    invoke-direct {v1}, Lmiuix/androidbasewidget/widget/SeekBar;->getMinWrapper()I

    move-result v11

    const/high16 v12, 0x3f800000

    if-eqz v2, :cond_3

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getMax()I

    move-result v13

    int-to-float v13, v13

    iget v14, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mDrawProgress:F

    sub-float/2addr v13, v14

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getMax()I

    move-result v14

    sub-int/2addr v14, v11

    int-to-float v14, v14

    mul-float/2addr v14, v12

    div-float/2addr v13, v14

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingStart()I

    move-result v14

    int-to-float v14, v14

    sub-float v14, v5, v14

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingEnd()I

    move-result v15

    int-to-float v15, v15

    sub-float/2addr v14, v15

    mul-float/2addr v13, v14

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingEnd()I

    move-result v14

    :goto_6
    int-to-float v14, v14

    add-float/2addr v13, v14

    goto :goto_7

    :cond_3
    iget v13, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mDrawProgress:F

    int-to-float v14, v11

    sub-float/2addr v13, v14

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getMax()I

    move-result v14

    sub-int/2addr v14, v11

    int-to-float v14, v14

    div-float/2addr v13, v14

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingStart()I

    move-result v14

    int-to-float v14, v14

    sub-float v14, v5, v14

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingEnd()I

    move-result v15

    int-to-float v15, v15

    sub-float/2addr v14, v15

    mul-float/2addr v13, v14

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingStart()I

    move-result v14

    goto :goto_6

    :goto_7
    iget-boolean v14, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mBalanceEnabled:Z

    if-eqz v14, :cond_5

    if-eqz v2, :cond_4

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getMax()I

    move-result v14

    iget v15, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mBalanceProgress:I

    sub-int/2addr v14, v15

    int-to-float v14, v14

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getMax()I

    move-result v15

    sub-int/2addr v15, v11

    int-to-float v15, v15

    mul-float/2addr v15, v12

    div-float/2addr v14, v15

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingStart()I

    move-result v12

    int-to-float v12, v12

    sub-float v12, v5, v12

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingEnd()I

    move-result v15

    int-to-float v15, v15

    sub-float/2addr v12, v15

    mul-float/2addr v14, v12

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingEnd()I

    move-result v12

    int-to-float v12, v12

    add-float/2addr v14, v12

    goto :goto_8

    :cond_4
    iget v12, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mBalanceProgress:I

    sub-int/2addr v12, v11

    int-to-float v12, v12

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getMax()I

    move-result v14

    sub-int/2addr v14, v11

    int-to-float v14, v14

    div-float/2addr v12, v14

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingStart()I

    move-result v14

    int-to-float v14, v14

    sub-float v14, v5, v14

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingEnd()I

    move-result v15

    int-to-float v15, v15

    sub-float/2addr v14, v15

    mul-float/2addr v12, v14

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingStart()I

    move-result v14

    int-to-float v14, v14

    add-float/2addr v14, v12

    goto :goto_8

    :cond_5
    const/4 v14, 0x0

    :goto_8
    iget v12, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mDefaultScalePrimaryColor:I

    iget v15, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mDefaultScaleSecondaryColor:I

    const/high16 v16, 0x40000000

    div-float v6, v6, v16

    add-float/2addr v6, v9

    iget v3, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mThumbHeight:I

    int-to-float v3, v3

    div-float v3, v3, v16

    sub-float v3, v6, v3

    float-to-int v3, v3

    iget-object v4, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mBackgroundDrawable:Landroid/graphics/drawable/Drawable;

    if-nez v4, :cond_8

    move/from16 v17, v2

    iget-object v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mProgressDrawable:Landroid/graphics/drawable/Drawable;

    if-eqz v2, :cond_6

    goto :goto_9

    :cond_6
    iget-object v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mLayerDrawable:Landroid/graphics/drawable/Drawable;

    if-eqz v2, :cond_7

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingStart()I

    move-result v4

    int-to-float v4, v4

    sub-float/2addr v4, v8

    float-to-int v4, v4

    float-to-int v7, v9

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingEnd()I

    move-result v9

    int-to-float v9, v9

    sub-float v9, v5, v9

    add-float/2addr v9, v8

    float-to-int v8, v9

    float-to-int v9, v10

    invoke-virtual {v2, v4, v7, v8, v9}, Landroid/graphics/drawable/Drawable;->setBounds(IIII)V

    iget-object v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mLayerDrawable:Landroid/graphics/drawable/Drawable;

    invoke-virtual {v2, v0}, Landroid/graphics/drawable/Drawable;->draw(Landroid/graphics/Canvas;)V

    :cond_7
    move/from16 v18, v5

    goto :goto_c

    :cond_8
    move/from16 v17, v2

    :goto_9
    if-eqz v4, :cond_9

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingStart()I

    move-result v2

    int-to-float v2, v2

    sub-float/2addr v2, v8

    float-to-int v2, v2

    move/from16 v18, v5

    float-to-int v5, v9

    move/from16 v19, v7

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingEnd()I

    move-result v7

    int-to-float v7, v7

    sub-float v7, v19, v7

    add-float/2addr v7, v8

    float-to-int v7, v7

    move/from16 v19, v8

    float-to-int v8, v10

    invoke-virtual {v4, v2, v5, v7, v8}, Landroid/graphics/drawable/Drawable;->setBounds(IIII)V

    iget-object v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mBackgroundDrawable:Landroid/graphics/drawable/Drawable;

    invoke-virtual {v2, v0}, Landroid/graphics/drawable/Drawable;->draw(Landroid/graphics/Canvas;)V

    goto :goto_a

    :cond_9
    move/from16 v18, v5

    move/from16 v19, v8

    :goto_a
    iget-object v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mProgressDrawable:Landroid/graphics/drawable/Drawable;

    if-eqz v2, :cond_f

    if-eqz v17, :cond_c

    iget-boolean v4, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mBalanceEnabled:Z

    if-eqz v4, :cond_b

    cmpl-float v4, v13, v14

    if-lez v4, :cond_a

    sub-float v14, v14, v19

    float-to-int v4, v14

    float-to-int v5, v9

    add-float v8, v13, v19

    float-to-int v7, v8

    float-to-int v8, v10

    invoke-virtual {v2, v4, v5, v7, v8}, Landroid/graphics/drawable/Drawable;->setBounds(IIII)V

    goto :goto_b

    :cond_a
    sub-float v4, v13, v19

    float-to-int v4, v4

    float-to-int v5, v9

    add-float v14, v14, v19

    float-to-int v7, v14

    float-to-int v8, v10

    invoke-virtual {v2, v4, v5, v7, v8}, Landroid/graphics/drawable/Drawable;->setBounds(IIII)V

    goto :goto_b

    :cond_b
    sub-float v4, v13, v19

    float-to-int v4, v4

    float-to-int v5, v9

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingEnd()I

    move-result v7

    int-to-float v7, v7

    sub-float v7, v18, v7

    add-float v7, v7, v19

    float-to-int v7, v7

    float-to-int v8, v10

    invoke-virtual {v2, v4, v5, v7, v8}, Landroid/graphics/drawable/Drawable;->setBounds(IIII)V

    goto :goto_b

    :cond_c
    iget-boolean v4, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mBalanceEnabled:Z

    if-eqz v4, :cond_e

    cmpl-float v4, v13, v14

    if-lez v4, :cond_d

    sub-float v14, v14, v19

    float-to-int v4, v14

    float-to-int v5, v9

    add-float v8, v13, v19

    float-to-int v7, v8

    float-to-int v8, v10

    invoke-virtual {v2, v4, v5, v7, v8}, Landroid/graphics/drawable/Drawable;->setBounds(IIII)V

    goto :goto_b

    :cond_d
    sub-float v4, v13, v19

    float-to-int v4, v4

    float-to-int v5, v9

    add-float v14, v14, v19

    float-to-int v7, v14

    float-to-int v8, v10

    invoke-virtual {v2, v4, v5, v7, v8}, Landroid/graphics/drawable/Drawable;->setBounds(IIII)V

    goto :goto_b

    :cond_e
    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingStart()I

    move-result v4

    int-to-float v4, v4

    sub-float v4, v4, v19

    float-to-int v4, v4

    float-to-int v5, v9

    add-float v8, v13, v19

    float-to-int v7, v8

    float-to-int v8, v10

    invoke-virtual {v2, v4, v5, v7, v8}, Landroid/graphics/drawable/Drawable;->setBounds(IIII)V

    :goto_b
    iget-object v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mProgressDrawable:Landroid/graphics/drawable/Drawable;

    invoke-virtual {v2, v0}, Landroid/graphics/drawable/Drawable;->draw(Landroid/graphics/Canvas;)V

    :cond_f
    :goto_c
    iget-boolean v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mMiddleEnabled:Z

    if-eqz v2, :cond_10

    iget-boolean v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mBalanceEnabled:Z

    if-nez v2, :cond_10

    iget v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mProgress:I

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getMax()I

    move-result v4

    sub-int/2addr v4, v11

    div-int/lit8 v4, v4, 0x2

    add-int/2addr v4, v11

    if-ge v2, v4, :cond_10

    iget-object v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mPaint:Landroid/graphics/Paint;

    invoke-virtual {v2, v15}, Landroid/graphics/Paint;->setColor(I)V

    div-float v5, v18, v16

    iget v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mScaleRadius:F

    iget-object v4, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mPaint:Landroid/graphics/Paint;

    invoke-virtual {v0, v5, v6, v2, v4}, Landroid/graphics/Canvas;->drawCircle(FFFLandroid/graphics/Paint;)V

    :cond_10
    iget-boolean v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mScaleEnabled:Z

    if-eqz v2, :cond_17

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getMax()I

    move-result v2

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingStart()I

    move-result v4

    int-to-float v4, v4

    sub-float v5, v18, v4

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingEnd()I

    move-result v4

    int-to-float v4, v4

    sub-float/2addr v5, v4

    int-to-float v4, v2

    div-float/2addr v5, v4

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getLayoutDirection()I

    move-result v4

    const/4 v7, 0x0

    :goto_d
    if-gt v7, v2, :cond_17

    iget v8, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mProgress:I

    if-eq v7, v8, :cond_13

    int-to-float v8, v7

    iget v9, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mDrawProgress:F

    cmpg-float v10, v8, v9

    if-gez v10, :cond_12

    iget-object v8, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mPaint:Landroid/graphics/Paint;

    invoke-virtual {v8, v12}, Landroid/graphics/Paint;->setColor(I)V

    :cond_11
    :goto_e
    const/4 v8, 0x1

    goto :goto_f

    :cond_12
    cmpl-float v8, v8, v9

    if-lez v8, :cond_11

    iget-object v8, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mPaint:Landroid/graphics/Paint;

    invoke-virtual {v8, v15}, Landroid/graphics/Paint;->setColor(I)V

    goto :goto_e

    :cond_13
    int-to-float v9, v8

    iget v10, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mDrawProgress:F

    cmpl-float v9, v9, v10

    if-lez v9, :cond_14

    iget-object v8, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mPaint:Landroid/graphics/Paint;

    invoke-virtual {v8, v15}, Landroid/graphics/Paint;->setColor(I)V

    goto :goto_e

    :cond_14
    int-to-float v8, v8

    cmpl-float v8, v8, v10

    if-nez v8, :cond_15

    iget-object v8, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mPaint:Landroid/graphics/Paint;

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getResources()Landroid/content/res/Resources;

    move-result-object v9

    sget v10, Lmiuix/androidbasewidget/R$color;->miuix_appcompat_transparent:I

    invoke-virtual {v9, v10}, Landroid/content/res/Resources;->getColor(I)I

    move-result v9

    invoke-virtual {v8, v9}, Landroid/graphics/Paint;->setColor(I)V

    goto :goto_e

    :cond_15
    iget-object v8, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mPaint:Landroid/graphics/Paint;

    invoke-virtual {v8, v12}, Landroid/graphics/Paint;->setColor(I)V

    goto :goto_e

    :goto_f
    if-ne v4, v8, :cond_16

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingEnd()I

    move-result v9

    int-to-float v9, v9

    sub-float v9, v18, v9

    int-to-float v10, v7

    mul-float/2addr v10, v5

    sub-float/2addr v9, v10

    goto :goto_10

    :cond_16
    invoke-virtual {v1}, Landroid/widget/SeekBar;->getPaddingStart()I

    move-result v9

    int-to-float v9, v9

    int-to-float v10, v7

    mul-float/2addr v10, v5

    add-float/2addr v9, v10

    :goto_10
    iget v10, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mScaleRadius:F

    iget-object v14, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mPaint:Landroid/graphics/Paint;

    invoke-virtual {v0, v9, v6, v10, v14}, Landroid/graphics/Canvas;->drawCircle(FFFLandroid/graphics/Paint;)V

    add-int/lit8 v7, v7, 0x1

    goto :goto_d

    :cond_17
    iget-boolean v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mMiddleEnabled:Z

    if-nez v2, :cond_18

    iget-boolean v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mBalanceEnabled:Z

    if-eqz v2, :cond_1c

    :cond_18
    iget-boolean v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mBalanceEnabled:Z

    const v4, 0x3e4ccccd

    if-eqz v2, :cond_1b

    iget v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mDrawProgress:F

    iget v5, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mBalanceProgress:I

    int-to-float v5, v5

    cmpl-float v5, v2, v5

    if-nez v5, :cond_19

    iget-object v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mPaint:Landroid/graphics/Paint;

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getResources()Landroid/content/res/Resources;

    move-result-object v4

    sget v5, Lmiuix/androidbasewidget/R$color;->miuix_appcompat_transparent:I

    invoke-virtual {v4, v5}, Landroid/content/res/Resources;->getColor(I)I

    move-result v4

    invoke-virtual {v2, v4}, Landroid/graphics/Paint;->setColor(I)V

    div-float v5, v18, v16

    iget v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mScaleRadius:F

    iget-object v4, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mPaint:Landroid/graphics/Paint;

    invoke-virtual {v0, v5, v6, v2, v4}, Landroid/graphics/Canvas;->drawCircle(FFFLandroid/graphics/Paint;)V

    goto :goto_11

    :cond_19
    invoke-virtual {v1}, Landroid/widget/SeekBar;->getMax()I

    move-result v5

    sub-int/2addr v5, v11

    int-to-float v5, v5

    div-float v5, v5, v16

    int-to-float v7, v11

    add-float/2addr v5, v7

    add-float/2addr v5, v4

    cmpl-float v2, v2, v5

    if-gtz v2, :cond_1a

    iget v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mDrawProgress:F

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getMax()I

    move-result v5

    sub-int/2addr v5, v11

    int-to-float v5, v5

    div-float v5, v5, v16

    add-float/2addr v5, v7

    sub-float/2addr v5, v4

    cmpg-float v2, v2, v5

    if-gez v2, :cond_1c

    :cond_1a
    iget-object v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mPaint:Landroid/graphics/Paint;

    invoke-virtual {v2, v12}, Landroid/graphics/Paint;->setColor(I)V

    div-float v5, v18, v16

    iget v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mScaleRadius:F

    iget-object v4, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mPaint:Landroid/graphics/Paint;

    invoke-virtual {v0, v5, v6, v2, v4}, Landroid/graphics/Canvas;->drawCircle(FFFLandroid/graphics/Paint;)V

    goto :goto_11

    :cond_1b
    iget v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mDrawProgress:F

    invoke-virtual {v1}, Landroid/widget/SeekBar;->getMax()I

    move-result v5

    sub-int/2addr v5, v11

    int-to-float v5, v5

    div-float v5, v5, v16

    int-to-float v7, v11

    add-float/2addr v5, v7

    add-float/2addr v5, v4

    cmpl-float v2, v2, v5

    if-lez v2, :cond_1c

    iget-object v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mPaint:Landroid/graphics/Paint;

    invoke-virtual {v2, v12}, Landroid/graphics/Paint;->setColor(I)V

    div-float v5, v18, v16

    iget v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mScaleRadius:F

    iget-object v4, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mPaint:Landroid/graphics/Paint;

    invoke-virtual {v0, v5, v6, v2, v4}, Landroid/graphics/Canvas;->drawCircle(FFFLandroid/graphics/Paint;)V

    :cond_1c
    :goto_11
    iget-object v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mThumbDrawable:Landroid/graphics/drawable/Drawable;

    if-eqz v2, :cond_1e

    iget v4, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mThumbWidth:I

    int-to-float v5, v4

    div-float v5, v5, v16

    sub-float v5, v13, v5

    float-to-int v5, v5

    int-to-float v4, v4

    div-float v4, v4, v16

    add-float/2addr v13, v4

    float-to-int v4, v13

    iget v6, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mThumbHeight:I

    add-int/2addr v6, v3

    invoke-virtual {v2, v5, v3, v4, v6}, Landroid/graphics/drawable/Drawable;->setBounds(IIII)V

    iget-object v2, v1, Lmiuix/androidbasewidget/widget/SeekBar;->mThumbDrawable:Landroid/graphics/drawable/Drawable;

    invoke-virtual {v2, v0}, Landroid/graphics/drawable/Drawable;->draw(Landroid/graphics/Canvas;)V

    goto :goto_12

    :cond_1d
    invoke-super/range {p0 .. p1}, Landroidx/appcompat/widget/AppCompatSeekBar;->onDraw(Landroid/graphics/Canvas;)V
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    :cond_1e
    :goto_12
    goto :goto_13

    nop

    :goto_13
    monitor-exit p0

    goto :goto_0

    nop

    :goto_14
    move-object/from16 v0, p1

    goto :goto_3

    nop

    :goto_15
    throw v0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_androidbasewidget_widget_SeekBar__drawableStateChanged',
        'method': '.method protected drawableStateChanged()V',
        'method_name': 'drawableStateChanged',
        'method_anchors': ['invoke-super {p0}, Landroidx/appcompat/widget/AppCompatSeekBar;->drawableStateChanged()V', 'invoke-direct {p0}, Lmiuix/androidbasewidget/widget/SeekBar;->updatePrimaryColor()V', 'invoke-virtual {p0}, Landroid/widget/SeekBar;->getProgressDrawable()Landroid/graphics/drawable/Drawable;', 'if-eqz v0, :cond_1', 'invoke-virtual {p0}, Landroid/widget/SeekBar;->isEnabled()Z', 'if-eqz v1, :cond_0', 'iget p0, p0, Lmiuix/androidbasewidget/widget/SeekBar;->mDisabledProgressAlpha:F', 'invoke-virtual {v0, p0}, Landroid/graphics/drawable/Drawable;->setAlpha(I)V'],
        'type': 'method_replace',
        'search': """.method protected drawableStateChanged()V
    .registers 3

    invoke-super {p0}, Landroidx/appcompat/widget/AppCompatSeekBar;->drawableStateChanged()V

    invoke-direct {p0}, Lmiuix/androidbasewidget/widget/SeekBar;->updatePrimaryColor()V

    invoke-virtual {p0}, Landroid/widget/SeekBar;->getProgressDrawable()Landroid/graphics/drawable/Drawable;

    move-result-object v0

    if-eqz v0, :cond_1

    invoke-virtual {p0}, Landroid/widget/SeekBar;->isEnabled()Z

    move-result v1

    if-eqz v1, :cond_0

    const/16 p0, 0xff

    goto :goto_0

    :cond_0
    const/high16 v1, 0x437f0000

    iget p0, p0, Lmiuix/androidbasewidget/widget/SeekBar;->mDisabledProgressAlpha:F

    mul-float/2addr p0, v1

    float-to-int p0, p0

    :goto_0
    invoke-virtual {v0, p0}, Landroid/graphics/drawable/Drawable;->setAlpha(I)V

    :cond_1
    return-void
.end method""",
        'replacement': """.method protected drawableStateChanged()V
    .registers 3

    goto :goto_7

    nop

    :goto_0
    invoke-virtual {v0, p0}, Landroid/graphics/drawable/Drawable;->setAlpha(I)V

    :goto_1
    goto :goto_3

    nop

    :goto_2
    if-nez v1, :cond_0

    goto :goto_f

    :cond_0
    goto :goto_d

    nop

    :goto_3
    return-void

    :goto_4
    if-nez v0, :cond_1

    goto :goto_1

    :cond_1
    goto :goto_c

    nop

    :goto_5
    float-to-int p0, p0

    :goto_6
    goto :goto_0

    nop

    :goto_7
    invoke-super {p0}, Landroidx/appcompat/widget/AppCompatSeekBar;->drawableStateChanged()V

    goto :goto_b

    nop

    :goto_8
    mul-float/2addr p0, v1

    goto :goto_5

    nop

    :goto_9
    const/high16 v1, 0x437f0000

    goto :goto_a

    nop

    :goto_a
    iget p0, p0, Lmiuix/androidbasewidget/widget/SeekBar;->mDisabledProgressAlpha:F

    goto :goto_8

    nop

    :goto_b
    invoke-direct {p0}, Lmiuix/androidbasewidget/widget/SeekBar;->updatePrimaryColor()V

    goto :goto_10

    nop

    :goto_c
    invoke-virtual {p0}, Landroid/widget/SeekBar;->isEnabled()Z

    move-result v1

    goto :goto_2

    nop

    :goto_d
    const/16 p0, 0xff

    goto :goto_e

    nop

    :goto_e
    goto :goto_6

    :goto_f
    goto :goto_9

    nop

    :goto_10
    invoke-virtual {p0}, Landroid/widget/SeekBar;->getProgressDrawable()Landroid/graphics/drawable/Drawable;

    move-result-object v0

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
