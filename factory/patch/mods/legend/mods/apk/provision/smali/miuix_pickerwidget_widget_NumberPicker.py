TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/pickerwidget/widget/NumberPicker.smali'
CLASS_FALLBACK_NAMES = ['NumberPicker.smali']
CLASS_ANCHORS = ['.super Landroid/widget/LinearLayout;', '.field private static final DEFAULT_LAYOUT_RESOURCE_ID:I', '.field private static final DIGIT_CHARACTERS:[C', '.field private static final PRESSED_STATE_SET:[I', '.field static final TWO_DIGIT_FORMATTER:Lmiuix/pickerwidget/widget/NumberPicker$Formatter;', '.field private static final sIdGenerator:Ljava/util/concurrent/atomic/AtomicInteger;']

PATCHES = [
    {
        'id': 'miuix_pickerwidget_widget_NumberPicker__drawableStateChanged',
        'method': '.method protected drawableStateChanged()V',
        'method_name': 'drawableStateChanged',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/LinearLayout;->drawableStateChanged()V', 'invoke-direct {p0}, Lmiuix/pickerwidget/widget/NumberPicker;->tryComputeMaxWidth()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected drawableStateChanged()V
    .registers 1

    invoke-super {p0}, Landroid/widget/LinearLayout;->drawableStateChanged()V

    invoke-direct {p0}, Lmiuix/pickerwidget/widget/NumberPicker;->tryComputeMaxWidth()V

    return-void
.end method""",
        'replacement': """.method protected drawableStateChanged()V
    .registers 1

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0}, Landroid/widget/LinearLayout;->drawableStateChanged()V

    goto :goto_2

    nop

    :goto_1
    return-void

    :goto_2
    invoke-direct {p0}, Lmiuix/pickerwidget/widget/NumberPicker;->tryComputeMaxWidth()V

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_pickerwidget_widget_NumberPicker__getBottomFadingEdgeStrength',
        'method': '.method protected getBottomFadingEdgeStrength()F',
        'method_name': 'getBottomFadingEdgeStrength',
        'method_anchors': ['return p0'],
        'type': 'method_replace',
        'search': """.method protected getBottomFadingEdgeStrength()F
    .registers 1

    const p0, 0x3f666666

    return p0
.end method""",
        'replacement': """.method protected getBottomFadingEdgeStrength()F
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    const p0, 0x3f666666

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_pickerwidget_widget_NumberPicker__getDisplayedMaxText',
        'method': '.method protected getDisplayedMaxText()Ljava/lang/String;',
        'method_name': 'getDisplayedMaxText',
        'method_anchors': ['iget-object p0, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mDisplayedMaxText:Ljava/lang/String;', 'if-nez p0, :cond_0', 'const-string p0, ""', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getDisplayedMaxText()Ljava/lang/String;
    .registers 1

    iget-object p0, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mDisplayedMaxText:Ljava/lang/String;

    if-nez p0, :cond_0

    const-string p0, ""

    :cond_0
    return-object p0
.end method""",
        'replacement': """.method protected getDisplayedMaxText()Ljava/lang/String;
    .registers 1

    goto :goto_3

    nop

    :goto_0
    const-string p0, ""

    :goto_1
    goto :goto_2

    nop

    :goto_2
    return-object p0

    :goto_3
    iget-object p0, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mDisplayedMaxText:Ljava/lang/String;

    goto :goto_4

    nop

    :goto_4
    if-eqz p0, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_pickerwidget_widget_NumberPicker__getDisplayedMaxTextWidth',
        'method': '.method protected getDisplayedMaxTextWidth()F',
        'method_name': 'getDisplayedMaxTextWidth',
        'method_anchors': ['iget-object v0, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mSelectorWheelPaint:Landroid/graphics/Paint;', 'invoke-virtual {v0}, Landroid/graphics/Paint;->getTextSize()F', 'iget-object v1, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mSelectorWheelPaint:Landroid/graphics/Paint;', 'iget v2, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mOriginTextSizeHighlight:I', 'invoke-virtual {v1, v2}, Landroid/graphics/Paint;->setTextSize(F)V', 'iget-object v1, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mSelectorWheelPaint:Landroid/graphics/Paint;', 'invoke-virtual {p0}, Lmiuix/pickerwidget/widget/NumberPicker;->getDisplayedMaxText()Ljava/lang/String;', 'invoke-virtual {v1, v2}, Landroid/graphics/Paint;->measureText(Ljava/lang/String;)F'],
        'type': 'method_replace',
        'search': """.method protected getDisplayedMaxTextWidth()F
    .registers 4

    iget-object v0, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mSelectorWheelPaint:Landroid/graphics/Paint;

    invoke-virtual {v0}, Landroid/graphics/Paint;->getTextSize()F

    move-result v0

    iget-object v1, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mSelectorWheelPaint:Landroid/graphics/Paint;

    iget v2, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mOriginTextSizeHighlight:I

    int-to-float v2, v2

    invoke-virtual {v1, v2}, Landroid/graphics/Paint;->setTextSize(F)V

    iget-object v1, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mSelectorWheelPaint:Landroid/graphics/Paint;

    invoke-virtual {p0}, Lmiuix/pickerwidget/widget/NumberPicker;->getDisplayedMaxText()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v2}, Landroid/graphics/Paint;->measureText(Ljava/lang/String;)F

    move-result v1

    iget-object p0, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mSelectorWheelPaint:Landroid/graphics/Paint;

    invoke-virtual {p0, v0}, Landroid/graphics/Paint;->setTextSize(F)V

    return v1
.end method""",
        'replacement': """.method protected getDisplayedMaxTextWidth()F
    .registers 4

    goto :goto_5

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mSelectorWheelPaint:Landroid/graphics/Paint;

    goto :goto_9

    nop

    :goto_1
    invoke-virtual {v1, v2}, Landroid/graphics/Paint;->setTextSize(F)V

    goto :goto_8

    nop

    :goto_2
    iget-object v1, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mSelectorWheelPaint:Landroid/graphics/Paint;

    goto :goto_7

    nop

    :goto_3
    invoke-virtual {v1, v2}, Landroid/graphics/Paint;->measureText(Ljava/lang/String;)F

    move-result v1

    goto :goto_0

    nop

    :goto_4
    invoke-virtual {p0}, Lmiuix/pickerwidget/widget/NumberPicker;->getDisplayedMaxText()Ljava/lang/String;

    move-result-object v2

    goto :goto_3

    nop

    :goto_5
    iget-object v0, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mSelectorWheelPaint:Landroid/graphics/Paint;

    goto :goto_a

    nop

    :goto_6
    return v1

    :goto_7
    iget v2, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mOriginTextSizeHighlight:I

    goto :goto_b

    nop

    :goto_8
    iget-object v1, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mSelectorWheelPaint:Landroid/graphics/Paint;

    goto :goto_4

    nop

    :goto_9
    invoke-virtual {p0, v0}, Landroid/graphics/Paint;->setTextSize(F)V

    goto :goto_6

    nop

    :goto_a
    invoke-virtual {v0}, Landroid/graphics/Paint;->getTextSize()F

    move-result v0

    goto :goto_2

    nop

    :goto_b
    int-to-float v2, v2

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_pickerwidget_widget_NumberPicker__getLabelWidth',
        'method': '.method protected getLabelWidth()F',
        'method_name': 'getLabelWidth',
        'method_anchors': ['iget-object v0, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mLabel:Ljava/lang/CharSequence;', 'invoke-static {v0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z', 'if-nez v0, :cond_0', 'invoke-direct {p0}, Lmiuix/pickerwidget/widget/NumberPicker;->isInternationalBuild()Z', 'if-nez v0, :cond_0', 'iget-object v0, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mLabelPaint:Landroid/graphics/Paint;', 'iget-object p0, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mLabel:Ljava/lang/CharSequence;', 'invoke-interface {p0}, Ljava/lang/CharSequence;->toString()Ljava/lang/String;'],
        'type': 'method_replace',
        'search': """.method protected getLabelWidth()F
    .registers 2

    iget-object v0, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mLabel:Ljava/lang/CharSequence;

    invoke-static {v0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v0

    if-nez v0, :cond_0

    invoke-direct {p0}, Lmiuix/pickerwidget/widget/NumberPicker;->isInternationalBuild()Z

    move-result v0

    if-nez v0, :cond_0

    iget-object v0, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mLabelPaint:Landroid/graphics/Paint;

    iget-object p0, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mLabel:Ljava/lang/CharSequence;

    invoke-interface {p0}, Ljava/lang/CharSequence;->toString()Ljava/lang/String;

    move-result-object p0

    invoke-virtual {v0, p0}, Landroid/graphics/Paint;->measureText(Ljava/lang/String;)F

    move-result p0

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method protected getLabelWidth()F
    .registers 2

    goto :goto_0

    nop

    :goto_0
    iget-object v0, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mLabel:Ljava/lang/CharSequence;

    goto :goto_b

    nop

    :goto_1
    invoke-interface {p0}, Ljava/lang/CharSequence;->toString()Ljava/lang/String;

    move-result-object p0

    goto :goto_c

    nop

    :goto_2
    return p0

    :goto_3
    goto :goto_9

    nop

    :goto_4
    if-eqz v0, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_a

    nop

    :goto_5
    return p0

    :goto_6
    iget-object p0, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mLabel:Ljava/lang/CharSequence;

    goto :goto_1

    nop

    :goto_7
    if-eqz v0, :cond_1

    goto :goto_3

    :cond_1
    goto :goto_8

    nop

    :goto_8
    invoke-direct {p0}, Lmiuix/pickerwidget/widget/NumberPicker;->isInternationalBuild()Z

    move-result v0

    goto :goto_4

    nop

    :goto_9
    const/4 p0, 0x0

    goto :goto_5

    nop

    :goto_a
    iget-object v0, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mLabelPaint:Landroid/graphics/Paint;

    goto :goto_6

    nop

    :goto_b
    invoke-static {v0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v0

    goto :goto_7

    nop

    :goto_c
    invoke-virtual {v0, p0}, Landroid/graphics/Paint;->measureText(Ljava/lang/String;)F

    move-result p0

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_pickerwidget_widget_NumberPicker__getTopFadingEdgeStrength',
        'method': '.method protected getTopFadingEdgeStrength()F',
        'method_name': 'getTopFadingEdgeStrength',
        'method_anchors': ['return p0'],
        'type': 'method_replace',
        'search': """.method protected getTopFadingEdgeStrength()F
    .registers 1

    const p0, 0x3f666666

    return p0
.end method""",
        'replacement': """.method protected getTopFadingEdgeStrength()F
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    const p0, 0x3f666666

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_pickerwidget_widget_NumberPicker__onAttachedToWindow',
        'method': '.method protected onAttachedToWindow()V',
        'method_name': 'onAttachedToWindow',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/LinearLayout;->onAttachedToWindow()V', 'invoke-direct {p0}, Lmiuix/pickerwidget/widget/NumberPicker;->initSoundPlayer()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onAttachedToWindow()V
    .registers 1

    invoke-super {p0}, Landroid/widget/LinearLayout;->onAttachedToWindow()V

    invoke-direct {p0}, Lmiuix/pickerwidget/widget/NumberPicker;->initSoundPlayer()V

    return-void
.end method""",
        'replacement': """.method protected onAttachedToWindow()V
    .registers 1

    goto :goto_1

    nop

    :goto_0
    invoke-direct {p0}, Lmiuix/pickerwidget/widget/NumberPicker;->initSoundPlayer()V

    goto :goto_2

    nop

    :goto_1
    invoke-super {p0}, Landroid/widget/LinearLayout;->onAttachedToWindow()V

    goto :goto_0

    nop

    :goto_2
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_pickerwidget_widget_NumberPicker__onConfigurationChanged',
        'method': '.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V',
        'method_name': 'onConfigurationChanged',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/widget/LinearLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V', 'invoke-direct {p0}, Lmiuix/pickerwidget/widget/NumberPicker;->initThreshHolds()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 2

    invoke-super {p0, p1}, Landroid/widget/LinearLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    invoke-direct {p0}, Lmiuix/pickerwidget/widget/NumberPicker;->initThreshHolds()V

    return-void
.end method""",
        'replacement': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 2

    goto :goto_2

    nop

    :goto_0
    return-void

    :goto_1
    invoke-direct {p0}, Lmiuix/pickerwidget/widget/NumberPicker;->initThreshHolds()V

    goto :goto_0

    nop

    :goto_2
    invoke-super {p0, p1}, Landroid/widget/LinearLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_pickerwidget_widget_NumberPicker__onDetachedFromWindow',
        'method': '.method protected onDetachedFromWindow()V',
        'method_name': 'onDetachedFromWindow',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/LinearLayout;->onDetachedFromWindow()V', 'invoke-direct {p0}, Lmiuix/pickerwidget/widget/NumberPicker;->releaseSoundPlayer()V', 'invoke-direct {p0}, Lmiuix/pickerwidget/widget/NumberPicker;->removeAllCallbacks()V', 'const-string p0, "NumberPicker_sound_play"', 'invoke-static {p0}, Lmiuix/pickerwidget/internal/util/async/WorkerThreads;->releaseWorker(Ljava/lang/String;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onDetachedFromWindow()V
    .registers 1

    invoke-super {p0}, Landroid/widget/LinearLayout;->onDetachedFromWindow()V

    invoke-direct {p0}, Lmiuix/pickerwidget/widget/NumberPicker;->releaseSoundPlayer()V

    invoke-direct {p0}, Lmiuix/pickerwidget/widget/NumberPicker;->removeAllCallbacks()V

    const-string p0, "NumberPicker_sound_play"

    invoke-static {p0}, Lmiuix/pickerwidget/internal/util/async/WorkerThreads;->releaseWorker(Ljava/lang/String;)V

    return-void
.end method""",
        'replacement': """.method protected onDetachedFromWindow()V
    .registers 1

    goto :goto_3

    nop

    :goto_0
    const-string p0, "NumberPicker_sound_play"

    goto :goto_2

    nop

    :goto_1
    return-void

    :goto_2
    invoke-static {p0}, Lmiuix/pickerwidget/internal/util/async/WorkerThreads;->releaseWorker(Ljava/lang/String;)V

    goto :goto_1

    nop

    :goto_3
    invoke-super {p0}, Landroid/widget/LinearLayout;->onDetachedFromWindow()V

    goto :goto_5

    nop

    :goto_4
    invoke-direct {p0}, Lmiuix/pickerwidget/widget/NumberPicker;->removeAllCallbacks()V

    goto :goto_0

    nop

    :goto_5
    invoke-direct {p0}, Lmiuix/pickerwidget/widget/NumberPicker;->releaseSoundPlayer()V

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_pickerwidget_widget_NumberPicker__onDraw',
        'method': '.method protected onDraw(Landroid/graphics/Canvas;)V',
        'method_name': 'onDraw',
        'method_anchors': ['iget-boolean v0, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mHasSelectorWheel:Z', 'if-nez v0, :cond_0', 'invoke-super {p0, p1}, Landroid/widget/LinearLayout;->onDraw(Landroid/graphics/Canvas;)V', 'return-void', 'invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingLeft()I', 'invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingRight()I', 'invoke-virtual {p0}, Landroid/widget/LinearLayout;->getRight()I', 'invoke-virtual {p0}, Landroid/widget/LinearLayout;->getLeft()I'],
        'type': 'method_replace',
        'search': """.method protected onDraw(Landroid/graphics/Canvas;)V
    .registers 6

    iget-boolean v0, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mHasSelectorWheel:Z

    if-nez v0, :cond_0

    invoke-super {p0, p1}, Landroid/widget/LinearLayout;->onDraw(Landroid/graphics/Canvas;)V

    return-void

    :cond_0
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingLeft()I

    move-result v0

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingRight()I

    move-result v1

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getRight()I

    move-result v2

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getLeft()I

    move-result v3

    sub-int/2addr v2, v3

    add-int/2addr v2, v0

    sub-int/2addr v2, v1

    div-int/lit8 v2, v2, 0x2

    int-to-float v0, v2

    iget v1, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mInitialScrollOffset:I

    iget v2, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mSelectorElementHeight:I

    add-int/2addr v1, v2

    int-to-float v1, v1

    invoke-direct {p0, p1, v0, v1}, Lmiuix/pickerwidget/widget/NumberPicker;->drawScrollValue(Landroid/graphics/Canvas;FF)F

    move-result v2

    invoke-direct {p0, p1, v0, v1, v2}, Lmiuix/pickerwidget/widget/NumberPicker;->drawLabelText(Landroid/graphics/Canvas;FFF)V

    return-void
.end method""",
        'replacement': """.method protected onDraw(Landroid/graphics/Canvas;)V
    .registers 6

    goto :goto_13

    nop

    :goto_0
    iget v1, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mInitialScrollOffset:I

    goto :goto_b

    nop

    :goto_1
    sub-int/2addr v2, v3

    goto :goto_12

    nop

    :goto_2
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingLeft()I

    move-result v0

    goto :goto_c

    nop

    :goto_3
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getLeft()I

    move-result v3

    goto :goto_1

    nop

    :goto_4
    div-int/lit8 v2, v2, 0x2

    goto :goto_d

    nop

    :goto_5
    if-eqz v0, :cond_0

    goto :goto_11

    :cond_0
    goto :goto_f

    nop

    :goto_6
    invoke-direct {p0, p1, v0, v1, v2}, Lmiuix/pickerwidget/widget/NumberPicker;->drawLabelText(Landroid/graphics/Canvas;FFF)V

    goto :goto_8

    nop

    :goto_7
    int-to-float v1, v1

    goto :goto_e

    nop

    :goto_8
    return-void

    :goto_9
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getRight()I

    move-result v2

    goto :goto_3

    nop

    :goto_a
    add-int/2addr v1, v2

    goto :goto_7

    nop

    :goto_b
    iget v2, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mSelectorElementHeight:I

    goto :goto_a

    nop

    :goto_c
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingRight()I

    move-result v1

    goto :goto_9

    nop

    :goto_d
    int-to-float v0, v2

    goto :goto_0

    nop

    :goto_e
    invoke-direct {p0, p1, v0, v1}, Lmiuix/pickerwidget/widget/NumberPicker;->drawScrollValue(Landroid/graphics/Canvas;FF)F

    move-result v2

    goto :goto_6

    nop

    :goto_f
    invoke-super {p0, p1}, Landroid/widget/LinearLayout;->onDraw(Landroid/graphics/Canvas;)V

    goto :goto_10

    nop

    :goto_10
    return-void

    :goto_11
    goto :goto_2

    nop

    :goto_12
    add-int/2addr v2, v0

    goto :goto_14

    nop

    :goto_13
    iget-boolean v0, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mHasSelectorWheel:Z

    goto :goto_5

    nop

    :goto_14
    sub-int/2addr v2, v1

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_pickerwidget_widget_NumberPicker__onLayout',
        'method': '.method protected onLayout(ZIIII)V',
        'method_name': 'onLayout',
        'method_anchors': ['iget-boolean v0, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mHasSelectorWheel:Z', 'if-nez v0, :cond_0', 'invoke-super/range {p0 .. p5}, Landroid/widget/LinearLayout;->onLayout(ZIIII)V', 'return-void', 'invoke-virtual {p0}, Landroid/widget/LinearLayout;->getMeasuredWidth()I', 'invoke-virtual {p0}, Landroid/widget/LinearLayout;->getMeasuredHeight()I', 'iget-object p4, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mInputText:Landroid/widget/EditText;', 'invoke-virtual {p4}, Landroid/widget/EditText;->getMeasuredWidth()I'],
        'type': 'method_replace',
        'search': """.method protected onLayout(ZIIII)V
    .registers 12

    iget-boolean v0, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mHasSelectorWheel:Z

    if-nez v0, :cond_0

    invoke-super/range {p0 .. p5}, Landroid/widget/LinearLayout;->onLayout(ZIIII)V

    return-void

    :cond_0
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getMeasuredWidth()I

    move-result p2

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getMeasuredHeight()I

    move-result p3

    iget-object p4, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mInputText:Landroid/widget/EditText;

    invoke-virtual {p4}, Landroid/widget/EditText;->getMeasuredWidth()I

    move-result p4

    iget-object p5, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mInputText:Landroid/widget/EditText;

    invoke-virtual {p5}, Landroid/widget/EditText;->getMeasuredHeight()I

    move-result p5

    sub-int/2addr p2, p4

    div-int/lit8 p2, p2, 0x2

    sub-int/2addr p3, p5

    div-int/lit8 p3, p3, 0x2

    add-int/2addr p4, p2

    add-int/2addr p5, p3

    iget-object v0, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mInputText:Landroid/widget/EditText;

    invoke-virtual {v0, p2, p3, p4, p5}, Landroid/widget/EditText;->layout(IIII)V

    if-eqz p1, :cond_1

    invoke-direct {p0}, Lmiuix/pickerwidget/widget/NumberPicker;->initializeSelectorWheel()V

    invoke-direct {p0}, Lmiuix/pickerwidget/widget/NumberPicker;->initializeFadingEdges()V

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getHeight()I

    move-result p1

    iget p2, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mSelectionDividersDistance:I

    sub-int/2addr p1, p2

    div-int/lit8 p1, p1, 0x2

    iget p3, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mSelectionDividerHeight:I

    sub-int/2addr p1, p3

    iput p1, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mTopSelectionDividerTop:I

    mul-int/lit8 p3, p3, 0x2

    add-int/2addr p1, p3

    add-int/2addr p1, p2

    iput p1, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mBottomSelectionDividerBottom:I

    :cond_1
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getRight()I

    move-result p1

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getLeft()I

    move-result p2

    sub-int/2addr p1, p2

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingLeft()I

    move-result p2

    add-int/2addr p1, p2

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingRight()I

    move-result p2

    sub-int/2addr p1, p2

    int-to-float p1, p1

    const/high16 p2, 0x40000000

    div-float/2addr p1, p2

    invoke-direct {p0, p1}, Lmiuix/pickerwidget/widget/NumberPicker;->trimLabelTextSize(F)V

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getBackground()Landroid/graphics/drawable/Drawable;

    move-result-object p1

    iget p2, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mMaxWidth:I

    add-int/lit8 p2, p2, 0x14

    iget-boolean p3, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mMeasureBackgroundEnabled:Z

    if-eqz p3, :cond_5

    instance-of p3, p1, Landroid/graphics/drawable/StateListDrawable;

    if-eqz p3, :cond_5

    check-cast p1, Landroid/graphics/drawable/StateListDrawable;

    invoke-virtual {p1}, Landroid/graphics/drawable/StateListDrawable;->getStateCount()I

    move-result p3

    const/4 p4, 0x0

    move p5, p4

    :goto_0
    if-ge p5, p3, :cond_5

    invoke-virtual {p1, p5}, Landroid/graphics/drawable/StateListDrawable;->getStateDrawable(I)Landroid/graphics/drawable/Drawable;

    move-result-object v0

    instance-of v1, v0, Landroid/graphics/drawable/LayerDrawable;

    if-eqz v1, :cond_4

    check-cast v0, Landroid/graphics/drawable/LayerDrawable;

    invoke-virtual {v0}, Landroid/graphics/drawable/LayerDrawable;->getNumberOfLayers()I

    move-result v1

    move v2, p4

    :goto_1
    if-ge v2, v1, :cond_4

    invoke-virtual {v0, v2}, Landroid/graphics/drawable/LayerDrawable;->getId(I)I

    move-result v3

    invoke-virtual {v0, v3}, Landroid/graphics/drawable/LayerDrawable;->findDrawableByLayerId(I)Landroid/graphics/drawable/Drawable;

    move-result-object v3

    instance-of v4, v3, Landroid/graphics/drawable/GradientDrawable;

    if-eqz v4, :cond_3

    check-cast v3, Landroid/graphics/drawable/GradientDrawable;

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getWidth()I

    move-result v4

    if-le v4, p2, :cond_2

    move v4, p2

    goto :goto_2

    :cond_2
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getWidth()I

    move-result v4

    :goto_2
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getHeight()I

    move-result v5

    invoke-virtual {v3, v4, v5}, Landroid/graphics/drawable/GradientDrawable;->setSize(II)V

    :cond_3
    add-int/lit8 v2, v2, 0x1

    goto :goto_1

    :cond_4
    add-int/lit8 p5, p5, 0x1

    goto :goto_0

    :cond_5
    return-void
.end method""",
        'replacement': """.method protected onLayout(ZIIII)V
    .registers 12

    goto :goto_15

    nop

    :goto_0
    iget-object p4, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mInputText:Landroid/widget/EditText;

    goto :goto_2b

    nop

    :goto_1
    if-nez p3, :cond_0

    goto :goto_1e

    :cond_0
    goto :goto_29

    nop

    :goto_2
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getWidth()I

    move-result v4

    goto :goto_27

    nop

    :goto_3
    invoke-virtual {v0, v2}, Landroid/graphics/drawable/LayerDrawable;->getId(I)I

    move-result v3

    goto :goto_10

    nop

    :goto_4
    sub-int/2addr p1, p2

    goto :goto_51

    nop

    :goto_5
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getMeasuredWidth()I

    move-result p2

    goto :goto_13

    nop

    :goto_6
    div-int/lit8 p3, p3, 0x2

    goto :goto_1c

    nop

    :goto_7
    div-int/lit8 p2, p2, 0x2

    goto :goto_30

    nop

    :goto_8
    invoke-direct {p0}, Lmiuix/pickerwidget/widget/NumberPicker;->initializeSelectorWheel()V

    goto :goto_21

    nop

    :goto_9
    add-int/2addr p1, p3

    goto :goto_57

    nop

    :goto_a
    add-int/lit8 p2, p2, 0x14

    goto :goto_33

    nop

    :goto_b
    return-void

    :goto_c
    goto :goto_19

    :goto_d
    goto :goto_18

    nop

    :goto_e
    sub-int/2addr p2, p4

    goto :goto_7

    nop

    :goto_f
    if-nez p1, :cond_1

    goto :goto_4a

    :cond_1
    goto :goto_8

    nop

    :goto_10
    invoke-virtual {v0, v3}, Landroid/graphics/drawable/LayerDrawable;->findDrawableByLayerId(I)Landroid/graphics/drawable/Drawable;

    move-result-object v3

    goto :goto_39

    nop

    :goto_11
    invoke-super/range {p0 .. p5}, Landroid/widget/LinearLayout;->onLayout(ZIIII)V

    goto :goto_52

    nop

    :goto_12
    const/4 p4, 0x0

    goto :goto_1f

    nop

    :goto_13
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getMeasuredHeight()I

    move-result p3

    goto :goto_0

    nop

    :goto_14
    check-cast v3, Landroid/graphics/drawable/GradientDrawable;

    goto :goto_2

    nop

    :goto_15
    iget-boolean v0, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mHasSelectorWheel:Z

    goto :goto_1a

    nop

    :goto_16
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingRight()I

    move-result p2

    goto :goto_50

    nop

    :goto_17
    check-cast v0, Landroid/graphics/drawable/LayerDrawable;

    goto :goto_3c

    nop

    :goto_18
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getWidth()I

    move-result v4

    :goto_19
    goto :goto_56

    nop

    :goto_1a
    if-eqz v0, :cond_2

    goto :goto_53

    :cond_2
    goto :goto_11

    nop

    :goto_1b
    invoke-virtual {p5}, Landroid/widget/EditText;->getMeasuredHeight()I

    move-result p5

    goto :goto_e

    nop

    :goto_1c
    add-int/2addr p4, p2

    goto :goto_4e

    nop

    :goto_1d
    goto :goto_20

    :goto_1e
    goto :goto_b

    nop

    :goto_1f
    move p5, p4

    :goto_20
    goto :goto_26

    nop

    :goto_21
    invoke-direct {p0}, Lmiuix/pickerwidget/widget/NumberPicker;->initializeFadingEdges()V

    goto :goto_2d

    nop

    :goto_22
    goto :goto_55

    :goto_23
    goto :goto_3e

    nop

    :goto_24
    if-nez v1, :cond_3

    goto :goto_23

    :cond_3
    goto :goto_17

    nop

    :goto_25
    div-float/2addr p1, p2

    goto :goto_4d

    nop

    :goto_26
    if-lt p5, p3, :cond_4

    goto :goto_1e

    :cond_4
    goto :goto_32

    nop

    :goto_27
    if-gt v4, p2, :cond_5

    goto :goto_d

    :cond_5
    goto :goto_2e

    nop

    :goto_28
    const/high16 p2, 0x40000000

    goto :goto_25

    nop

    :goto_29
    check-cast p1, Landroid/graphics/drawable/StateListDrawable;

    goto :goto_46

    nop

    :goto_2a
    iget p2, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mSelectionDividersDistance:I

    goto :goto_48

    nop

    :goto_2b
    invoke-virtual {p4}, Landroid/widget/EditText;->getMeasuredWidth()I

    move-result p4

    goto :goto_3d

    nop

    :goto_2c
    if-nez p3, :cond_6

    goto :goto_1e

    :cond_6
    goto :goto_36

    nop

    :goto_2d
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getHeight()I

    move-result p1

    goto :goto_2a

    nop

    :goto_2e
    move v4, p2

    goto :goto_c

    nop

    :goto_2f
    instance-of v1, v0, Landroid/graphics/drawable/LayerDrawable;

    goto :goto_24

    nop

    :goto_30
    sub-int/2addr p3, p5

    goto :goto_6

    nop

    :goto_31
    iput p1, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mTopSelectionDividerTop:I

    goto :goto_3f

    nop

    :goto_32
    invoke-virtual {p1, p5}, Landroid/graphics/drawable/StateListDrawable;->getStateDrawable(I)Landroid/graphics/drawable/Drawable;

    move-result-object v0

    goto :goto_2f

    nop

    :goto_33
    iget-boolean p3, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mMeasureBackgroundEnabled:Z

    goto :goto_2c

    nop

    :goto_34
    if-lt v2, v1, :cond_7

    goto :goto_23

    :cond_7
    goto :goto_3

    nop

    :goto_35
    iget p3, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mSelectionDividerHeight:I

    goto :goto_3b

    nop

    :goto_36
    instance-of p3, p1, Landroid/graphics/drawable/StateListDrawable;

    goto :goto_1

    nop

    :goto_37
    if-nez v4, :cond_8

    goto :goto_42

    :cond_8
    goto :goto_14

    nop

    :goto_38
    int-to-float p1, p1

    goto :goto_28

    nop

    :goto_39
    instance-of v4, v3, Landroid/graphics/drawable/GradientDrawable;

    goto :goto_37

    nop

    :goto_3a
    div-int/lit8 p1, p1, 0x2

    goto :goto_35

    nop

    :goto_3b
    sub-int/2addr p1, p3

    goto :goto_31

    nop

    :goto_3c
    invoke-virtual {v0}, Landroid/graphics/drawable/LayerDrawable;->getNumberOfLayers()I

    move-result v1

    goto :goto_54

    nop

    :goto_3d
    iget-object p5, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mInputText:Landroid/widget/EditText;

    goto :goto_1b

    nop

    :goto_3e
    add-int/lit8 p5, p5, 0x1

    goto :goto_1d

    nop

    :goto_3f
    mul-int/lit8 p3, p3, 0x2

    goto :goto_9

    nop

    :goto_40
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getBackground()Landroid/graphics/drawable/Drawable;

    move-result-object p1

    goto :goto_43

    nop

    :goto_41
    invoke-virtual {v3, v4, v5}, Landroid/graphics/drawable/GradientDrawable;->setSize(II)V

    :goto_42
    goto :goto_4c

    nop

    :goto_43
    iget p2, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mMaxWidth:I

    goto :goto_a

    nop

    :goto_44
    add-int/2addr p1, p2

    goto :goto_16

    nop

    :goto_45
    iget-object v0, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mInputText:Landroid/widget/EditText;

    goto :goto_4f

    nop

    :goto_46
    invoke-virtual {p1}, Landroid/graphics/drawable/StateListDrawable;->getStateCount()I

    move-result p3

    goto :goto_12

    nop

    :goto_47
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getLeft()I

    move-result p2

    goto :goto_4

    nop

    :goto_48
    sub-int/2addr p1, p2

    goto :goto_3a

    nop

    :goto_49
    iput p1, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mBottomSelectionDividerBottom:I

    :goto_4a
    goto :goto_4b

    nop

    :goto_4b
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getRight()I

    move-result p1

    goto :goto_47

    nop

    :goto_4c
    add-int/lit8 v2, v2, 0x1

    goto :goto_22

    nop

    :goto_4d
    invoke-direct {p0, p1}, Lmiuix/pickerwidget/widget/NumberPicker;->trimLabelTextSize(F)V

    goto :goto_40

    nop

    :goto_4e
    add-int/2addr p5, p3

    goto :goto_45

    nop

    :goto_4f
    invoke-virtual {v0, p2, p3, p4, p5}, Landroid/widget/EditText;->layout(IIII)V

    goto :goto_f

    nop

    :goto_50
    sub-int/2addr p1, p2

    goto :goto_38

    nop

    :goto_51
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingLeft()I

    move-result p2

    goto :goto_44

    nop

    :goto_52
    return-void

    :goto_53
    goto :goto_5

    nop

    :goto_54
    move v2, p4

    :goto_55
    goto :goto_34

    nop

    :goto_56
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getHeight()I

    move-result v5

    goto :goto_41

    nop

    :goto_57
    add-int/2addr p1, p2

    goto :goto_49

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_pickerwidget_widget_NumberPicker__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['iget-boolean v0, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mHasSelectorWheel:Z', 'if-nez v0, :cond_0', 'invoke-super {p0, p1, p2}, Landroid/widget/LinearLayout;->onMeasure(II)V', 'return-void', 'iget v0, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mMaxWidth:I', 'invoke-direct {p0, p1, v0}, Lmiuix/pickerwidget/widget/NumberPicker;->makeMeasureSpec(II)I', 'iget v1, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mMaxHeight:I', 'invoke-direct {p0, p2, v1}, Lmiuix/pickerwidget/widget/NumberPicker;->makeMeasureSpec(II)I'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 5

    iget-boolean v0, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mHasSelectorWheel:Z

    if-nez v0, :cond_0

    invoke-super {p0, p1, p2}, Landroid/widget/LinearLayout;->onMeasure(II)V

    return-void

    :cond_0
    iget v0, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mMaxWidth:I

    invoke-direct {p0, p1, v0}, Lmiuix/pickerwidget/widget/NumberPicker;->makeMeasureSpec(II)I

    move-result v0

    iget v1, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mMaxHeight:I

    invoke-direct {p0, p2, v1}, Lmiuix/pickerwidget/widget/NumberPicker;->makeMeasureSpec(II)I

    move-result v1

    invoke-super {p0, v0, v1}, Landroid/widget/LinearLayout;->onMeasure(II)V

    iget v0, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mMinWidth:I

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getMeasuredWidth()I

    move-result v1

    invoke-direct {p0, v0, v1, p1}, Lmiuix/pickerwidget/widget/NumberPicker;->resolveSizeAndStateRespectingMinSize(III)I

    move-result p1

    iget v0, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mMinHeight:I

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getMeasuredHeight()I

    move-result v1

    invoke-direct {p0, v0, v1, p2}, Lmiuix/pickerwidget/widget/NumberPicker;->resolveSizeAndStateRespectingMinSize(III)I

    move-result p2

    invoke-virtual {p0, p1, p2}, Landroid/widget/LinearLayout;->setMeasuredDimension(II)V

    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 5

    goto :goto_d

    nop

    :goto_0
    iget v0, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mMaxWidth:I

    goto :goto_a

    nop

    :goto_1
    iget v0, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mMinHeight:I

    goto :goto_9

    nop

    :goto_2
    invoke-virtual {p0, p1, p2}, Landroid/widget/LinearLayout;->setMeasuredDimension(II)V

    goto :goto_8

    nop

    :goto_3
    iget v0, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mMinWidth:I

    goto :goto_c

    nop

    :goto_4
    invoke-super {p0, v0, v1}, Landroid/widget/LinearLayout;->onMeasure(II)V

    goto :goto_3

    nop

    :goto_5
    invoke-direct {p0, p2, v1}, Lmiuix/pickerwidget/widget/NumberPicker;->makeMeasureSpec(II)I

    move-result v1

    goto :goto_4

    nop

    :goto_6
    iget v1, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mMaxHeight:I

    goto :goto_5

    nop

    :goto_7
    invoke-super {p0, p1, p2}, Landroid/widget/LinearLayout;->onMeasure(II)V

    goto :goto_e

    nop

    :goto_8
    return-void

    :goto_9
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getMeasuredHeight()I

    move-result v1

    goto :goto_10

    nop

    :goto_a
    invoke-direct {p0, p1, v0}, Lmiuix/pickerwidget/widget/NumberPicker;->makeMeasureSpec(II)I

    move-result v0

    goto :goto_6

    nop

    :goto_b
    if-eqz v0, :cond_0

    goto :goto_f

    :cond_0
    goto :goto_7

    nop

    :goto_c
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getMeasuredWidth()I

    move-result v1

    goto :goto_11

    nop

    :goto_d
    iget-boolean v0, p0, Lmiuix/pickerwidget/widget/NumberPicker;->mHasSelectorWheel:Z

    goto :goto_b

    nop

    :goto_e
    return-void

    :goto_f
    goto :goto_0

    nop

    :goto_10
    invoke-direct {p0, v0, v1, p2}, Lmiuix/pickerwidget/widget/NumberPicker;->resolveSizeAndStateRespectingMinSize(III)I

    move-result p2

    goto :goto_2

    nop

    :goto_11
    invoke-direct {p0, v0, v1, p1}, Lmiuix/pickerwidget/widget/NumberPicker;->resolveSizeAndStateRespectingMinSize(III)I

    move-result p1

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
