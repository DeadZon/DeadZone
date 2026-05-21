TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/androidbasewidget/widget/CheckedTextView.smali'
CLASS_FALLBACK_NAMES = ['CheckedTextView.smali']
CLASS_ANCHORS = ['.super Lmiuix/androidbasewidget/widget/AppCompatCheckedTextView;', '.field private static final CHECKED_STATE_SET:[I']

PATCHES = [
    {
        'id': 'miuix_androidbasewidget_widget_CheckedTextView__drawableStateChanged',
        'method': '.method protected drawableStateChanged()V',
        'method_name': 'drawableStateChanged',
        'method_anchors': ['invoke-super {p0}, Landroidx/appcompat/widget/AppCompatCheckedTextView;->drawableStateChanged()V', 'iget-object v0, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mCheckMarkDrawable:Landroid/graphics/drawable/Drawable;', 'if-eqz v0, :cond_0', 'invoke-virtual {p0}, Landroid/widget/CheckedTextView;->getDrawableState()[I', 'iget-object v1, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mCheckMarkDrawable:Landroid/graphics/drawable/Drawable;', 'invoke-virtual {v1, v0}, Landroid/graphics/drawable/Drawable;->setState([I)Z', 'invoke-virtual {p0}, Landroid/widget/CheckedTextView;->invalidate()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected drawableStateChanged()V
    .registers 3

    invoke-super {p0}, Landroidx/appcompat/widget/AppCompatCheckedTextView;->drawableStateChanged()V

    iget-object v0, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mCheckMarkDrawable:Landroid/graphics/drawable/Drawable;

    if-eqz v0, :cond_0

    invoke-virtual {p0}, Landroid/widget/CheckedTextView;->getDrawableState()[I

    move-result-object v0

    iget-object v1, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mCheckMarkDrawable:Landroid/graphics/drawable/Drawable;

    invoke-virtual {v1, v0}, Landroid/graphics/drawable/Drawable;->setState([I)Z

    invoke-virtual {p0}, Landroid/widget/CheckedTextView;->invalidate()V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected drawableStateChanged()V
    .registers 3

    goto :goto_4

    nop

    :goto_0
    return-void

    :goto_1
    invoke-virtual {p0}, Landroid/widget/CheckedTextView;->getDrawableState()[I

    move-result-object v0

    goto :goto_7

    nop

    :goto_2
    invoke-virtual {p0}, Landroid/widget/CheckedTextView;->invalidate()V

    :goto_3
    goto :goto_0

    nop

    :goto_4
    invoke-super {p0}, Landroidx/appcompat/widget/AppCompatCheckedTextView;->drawableStateChanged()V

    goto :goto_5

    nop

    :goto_5
    iget-object v0, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mCheckMarkDrawable:Landroid/graphics/drawable/Drawable;

    goto :goto_6

    nop

    :goto_6
    if-nez v0, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_1

    nop

    :goto_7
    iget-object v1, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mCheckMarkDrawable:Landroid/graphics/drawable/Drawable;

    goto :goto_8

    nop

    :goto_8
    invoke-virtual {v1, v0}, Landroid/graphics/drawable/Drawable;->setState([I)Z

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_androidbasewidget_widget_CheckedTextView__onConfigurationChanged',
        'method': '.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V',
        'method_name': 'onConfigurationChanged',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/widget/CheckedTextView;->onConfigurationChanged(Landroid/content/res/Configuration;)V', 'invoke-virtual {p0}, Landroid/widget/CheckedTextView;->getContext()Landroid/content/Context;', 'invoke-virtual {p1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;', 'sget v0, Lmiuix/androidbasewidget/R$dimen;->miuix_appcompat_checked_text_view_addition_margin:I', 'invoke-virtual {p1, v0}, Landroid/content/res/Resources;->getDimension(I)F', 'iput p1, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mCheckMarkMarginToText:I', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 3

    invoke-super {p0, p1}, Landroid/widget/CheckedTextView;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    invoke-virtual {p0}, Landroid/widget/CheckedTextView;->getContext()Landroid/content/Context;

    move-result-object p1

    invoke-virtual {p1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object p1

    sget v0, Lmiuix/androidbasewidget/R$dimen;->miuix_appcompat_checked_text_view_addition_margin:I

    invoke-virtual {p1, v0}, Landroid/content/res/Resources;->getDimension(I)F

    move-result p1

    float-to-int p1, p1

    iput p1, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mCheckMarkMarginToText:I

    return-void
.end method""",
        'replacement': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 3

    goto :goto_7

    nop

    :goto_0
    invoke-virtual {p0}, Landroid/widget/CheckedTextView;->getContext()Landroid/content/Context;

    move-result-object p1

    goto :goto_3

    nop

    :goto_1
    float-to-int p1, p1

    goto :goto_5

    nop

    :goto_2
    return-void

    :goto_3
    invoke-virtual {p1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object p1

    goto :goto_6

    nop

    :goto_4
    invoke-virtual {p1, v0}, Landroid/content/res/Resources;->getDimension(I)F

    move-result p1

    goto :goto_1

    nop

    :goto_5
    iput p1, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mCheckMarkMarginToText:I

    goto :goto_2

    nop

    :goto_6
    sget v0, Lmiuix/androidbasewidget/R$dimen;->miuix_appcompat_checked_text_view_addition_margin:I

    goto :goto_4

    nop

    :goto_7
    invoke-super {p0, p1}, Landroid/widget/CheckedTextView;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_androidbasewidget_widget_CheckedTextView__onCreateDrawableState',
        'method': '.method protected onCreateDrawableState(I)[I',
        'method_name': 'onCreateDrawableState',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/widget/CheckedTextView;->onCreateDrawableState(I)[I', 'invoke-virtual {p0}, Landroid/widget/CheckedTextView;->isChecked()Z', 'if-eqz p0, :cond_0', 'sget-object p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->CHECKED_STATE_SET:[I', 'invoke-static {p1, p0}, Landroid/widget/CheckedTextView;->mergeDrawableStates([I[I)[I', 'return-object p1'],
        'type': 'method_replace',
        'search': """.method protected onCreateDrawableState(I)[I
    .registers 2

    add-int/lit8 p1, p1, 0x1

    invoke-super {p0, p1}, Landroid/widget/CheckedTextView;->onCreateDrawableState(I)[I

    move-result-object p1

    invoke-virtual {p0}, Landroid/widget/CheckedTextView;->isChecked()Z

    move-result p0

    if-eqz p0, :cond_0

    sget-object p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->CHECKED_STATE_SET:[I

    invoke-static {p1, p0}, Landroid/widget/CheckedTextView;->mergeDrawableStates([I[I)[I

    :cond_0
    return-object p1
.end method""",
        'replacement': """.method protected onCreateDrawableState(I)[I
    .registers 2

    goto :goto_6

    nop

    :goto_0
    sget-object p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->CHECKED_STATE_SET:[I

    goto :goto_3

    nop

    :goto_1
    if-nez p0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_0

    nop

    :goto_2
    invoke-virtual {p0}, Landroid/widget/CheckedTextView;->isChecked()Z

    move-result p0

    goto :goto_1

    nop

    :goto_3
    invoke-static {p1, p0}, Landroid/widget/CheckedTextView;->mergeDrawableStates([I[I)[I

    :goto_4
    goto :goto_5

    nop

    :goto_5
    return-object p1

    :goto_6
    add-int/lit8 p1, p1, 0x1

    goto :goto_7

    nop

    :goto_7
    invoke-super {p0, p1}, Landroid/widget/CheckedTextView;->onCreateDrawableState(I)[I

    move-result-object p1

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_androidbasewidget_widget_CheckedTextView__onDraw',
        'method': '.method protected onDraw(Landroid/graphics/Canvas;)V',
        'method_name': 'onDraw',
        'method_anchors': ['invoke-virtual {p0}, Landroid/widget/CheckedTextView;->getLayoutDirection()I', 'if-ne v0, v2, :cond_0', 'iget-boolean v0, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mDrawCheckMark:Z', 'if-eqz v0, :cond_1', 'invoke-direct {p0, p1, v2}, Lmiuix/androidbasewidget/widget/CheckedTextView;->drawCheckMark(Landroid/graphics/Canvas;Z)V', 'invoke-virtual {p0}, Lmiuix/androidbasewidget/widget/CheckedTextView;->getCheckMarkDrawable()Landroid/graphics/drawable/Drawable;', 'if-eqz v0, :cond_2', 'invoke-virtual {p0}, Lmiuix/androidbasewidget/widget/CheckedTextView;->getCheckMarkDrawable()Landroid/graphics/drawable/Drawable;'],
        'type': 'method_replace',
        'search': """.method protected onDraw(Landroid/graphics/Canvas;)V
    .registers 5

    invoke-virtual {p0}, Landroid/widget/CheckedTextView;->getLayoutDirection()I

    move-result v0

    const/4 v1, 0x0

    const/4 v2, 0x1

    if-ne v0, v2, :cond_0

    goto :goto_0

    :cond_0
    move v2, v1

    :goto_0
    iget-boolean v0, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mDrawCheckMark:Z

    if-eqz v0, :cond_1

    invoke-direct {p0, p1, v2}, Lmiuix/androidbasewidget/widget/CheckedTextView;->drawCheckMark(Landroid/graphics/Canvas;Z)V

    :cond_1
    invoke-virtual {p0}, Lmiuix/androidbasewidget/widget/CheckedTextView;->getCheckMarkDrawable()Landroid/graphics/drawable/Drawable;

    move-result-object v0

    if-eqz v0, :cond_2

    invoke-virtual {p0}, Lmiuix/androidbasewidget/widget/CheckedTextView;->getCheckMarkDrawable()Landroid/graphics/drawable/Drawable;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object v0

    const-class v1, Landroid/graphics/drawable/StateListDrawable;

    invoke-virtual {v0, v1}, Ljava/lang/Class;->isAssignableFrom(Ljava/lang/Class;)Z

    move-result v0

    iput-boolean v0, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mDrawTextOffsetInRtl:Z

    goto :goto_1

    :cond_2
    iput-boolean v1, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mDrawTextOffsetInRtl:Z

    :goto_1
    if-eqz v2, :cond_3

    iget-boolean v0, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mDrawCheckMark:Z

    if-eqz v0, :cond_3

    iget-boolean v0, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mDrawTextOffsetInRtl:Z

    if-eqz v0, :cond_3

    invoke-virtual {p1}, Landroid/graphics/Canvas;->save()I

    invoke-direct {p0}, Lmiuix/androidbasewidget/widget/CheckedTextView;->getCheckWidth()I

    move-result v0

    int-to-float v0, v0

    const/4 v1, 0x0

    invoke-virtual {p1, v0, v1}, Landroid/graphics/Canvas;->translate(FF)V

    :cond_3
    invoke-super {p0, p1}, Landroid/widget/CheckedTextView;->onDraw(Landroid/graphics/Canvas;)V

    if-eqz v2, :cond_4

    iget-boolean v0, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mDrawCheckMark:Z

    if-eqz v0, :cond_4

    iget-boolean p0, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mDrawTextOffsetInRtl:Z

    if-eqz p0, :cond_4

    invoke-virtual {p1}, Landroid/graphics/Canvas;->restore()V

    :cond_4
    return-void
.end method""",
        'replacement': """.method protected onDraw(Landroid/graphics/Canvas;)V
    .registers 5

    goto :goto_1c

    nop

    :goto_0
    iget-boolean v0, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mDrawCheckMark:Z

    goto :goto_8

    nop

    :goto_1
    invoke-direct {p0}, Lmiuix/androidbasewidget/widget/CheckedTextView;->getCheckWidth()I

    move-result v0

    goto :goto_29

    nop

    :goto_2
    if-nez v2, :cond_0

    goto :goto_1e

    :cond_0
    goto :goto_d

    nop

    :goto_3
    iget-boolean v0, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mDrawCheckMark:Z

    goto :goto_21

    nop

    :goto_4
    return-void

    :goto_5
    goto :goto_12

    :goto_6
    goto :goto_11

    nop

    :goto_7
    if-nez v0, :cond_1

    goto :goto_1e

    :cond_1
    goto :goto_19

    nop

    :goto_8
    if-nez v0, :cond_2

    goto :goto_10

    :cond_2
    goto :goto_1b

    nop

    :goto_9
    const-class v1, Landroid/graphics/drawable/StateListDrawable;

    goto :goto_13

    nop

    :goto_a
    invoke-virtual {p0}, Lmiuix/androidbasewidget/widget/CheckedTextView;->getCheckMarkDrawable()Landroid/graphics/drawable/Drawable;

    move-result-object v0

    goto :goto_26

    nop

    :goto_b
    iput-boolean v0, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mDrawTextOffsetInRtl:Z

    goto :goto_5

    nop

    :goto_c
    if-nez v0, :cond_3

    goto :goto_6

    :cond_3
    goto :goto_a

    nop

    :goto_d
    iget-boolean v0, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mDrawCheckMark:Z

    goto :goto_28

    nop

    :goto_e
    if-nez p0, :cond_4

    goto :goto_10

    :cond_4
    goto :goto_f

    nop

    :goto_f
    invoke-virtual {p1}, Landroid/graphics/Canvas;->restore()V

    :goto_10
    goto :goto_4

    nop

    :goto_11
    iput-boolean v1, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mDrawTextOffsetInRtl:Z

    :goto_12
    goto :goto_2

    nop

    :goto_13
    invoke-virtual {v0, v1}, Ljava/lang/Class;->isAssignableFrom(Ljava/lang/Class;)Z

    move-result v0

    goto :goto_b

    nop

    :goto_14
    invoke-super {p0, p1}, Landroid/widget/CheckedTextView;->onDraw(Landroid/graphics/Canvas;)V

    goto :goto_17

    nop

    :goto_15
    invoke-direct {p0, p1, v2}, Lmiuix/androidbasewidget/widget/CheckedTextView;->drawCheckMark(Landroid/graphics/Canvas;Z)V

    :goto_16
    goto :goto_27

    nop

    :goto_17
    if-nez v2, :cond_5

    goto :goto_10

    :cond_5
    goto :goto_0

    nop

    :goto_18
    iget-boolean v0, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mDrawTextOffsetInRtl:Z

    goto :goto_7

    nop

    :goto_19
    invoke-virtual {p1}, Landroid/graphics/Canvas;->save()I

    goto :goto_1

    nop

    :goto_1a
    const/4 v1, 0x0

    goto :goto_1d

    nop

    :goto_1b
    iget-boolean p0, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mDrawTextOffsetInRtl:Z

    goto :goto_e

    nop

    :goto_1c
    invoke-virtual {p0}, Landroid/widget/CheckedTextView;->getLayoutDirection()I

    move-result v0

    goto :goto_2a

    nop

    :goto_1d
    invoke-virtual {p1, v0, v1}, Landroid/graphics/Canvas;->translate(FF)V

    :goto_1e
    goto :goto_14

    nop

    :goto_1f
    move v2, v1

    :goto_20
    goto :goto_3

    nop

    :goto_21
    if-nez v0, :cond_6

    goto :goto_16

    :cond_6
    goto :goto_15

    nop

    :goto_22
    if-eq v0, v2, :cond_7

    goto :goto_25

    :cond_7
    goto :goto_24

    nop

    :goto_23
    const/4 v2, 0x1

    goto :goto_22

    nop

    :goto_24
    goto :goto_20

    :goto_25
    goto :goto_1f

    nop

    :goto_26
    invoke-virtual {v0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object v0

    goto :goto_9

    nop

    :goto_27
    invoke-virtual {p0}, Lmiuix/androidbasewidget/widget/CheckedTextView;->getCheckMarkDrawable()Landroid/graphics/drawable/Drawable;

    move-result-object v0

    goto :goto_c

    nop

    :goto_28
    if-nez v0, :cond_8

    goto :goto_1e

    :cond_8
    goto :goto_18

    nop

    :goto_29
    int-to-float v0, v0

    goto :goto_1a

    nop

    :goto_2a
    const/4 v1, 0x0

    goto :goto_23

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_androidbasewidget_widget_CheckedTextView__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['invoke-static {p1}, Landroid/view/View$MeasureSpec;->getSize(I)I', 'invoke-direct {p0}, Lmiuix/androidbasewidget/widget/CheckedTextView;->getCheckWidth()I', 'if-lez v1, :cond_2', 'invoke-virtual {p0}, Landroid/widget/CheckedTextView;->getText()Ljava/lang/CharSequence;', 'invoke-static {v3}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z', 'if-eqz v3, :cond_0', 'iput-boolean v4, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mDrawCheckMark:Z', 'invoke-static {p1}, Landroid/view/View$MeasureSpec;->getMode(I)I'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 9

    invoke-static {p1}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v0

    invoke-direct {p0}, Lmiuix/androidbasewidget/widget/CheckedTextView;->getCheckWidth()I

    move-result v1

    const/4 v2, 0x0

    if-lez v1, :cond_2

    invoke-virtual {p0}, Landroid/widget/CheckedTextView;->getText()Ljava/lang/CharSequence;

    move-result-object v3

    invoke-static {v3}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v3

    const/4 v4, 0x1

    if-eqz v3, :cond_0

    iput-boolean v4, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mDrawCheckMark:Z

    invoke-static {p1}, Landroid/view/View$MeasureSpec;->getMode(I)I

    move-result p1

    invoke-static {v1, p1}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p1

    invoke-super {p0, p1, p2}, Landroid/widget/CheckedTextView;->onMeasure(II)V

    invoke-virtual {p0}, Landroid/widget/CheckedTextView;->getMeasuredHeight()I

    move-result p1

    invoke-virtual {p0, v1, p1}, Landroid/widget/CheckedTextView;->setMeasuredDimension(II)V

    return-void

    :cond_0
    invoke-virtual {p0}, Landroid/widget/CheckedTextView;->getPaddingEnd()I

    move-result v3

    sub-int v3, v0, v3

    mul-int/lit8 v5, v1, 0x2

    if-ge v3, v5, :cond_1

    iput-boolean v2, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mDrawCheckMark:Z

    move v1, v2

    goto :goto_0

    :cond_1
    iput-boolean v4, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mDrawCheckMark:Z

    :cond_2
    :goto_0
    invoke-static {p1}, Landroid/view/View$MeasureSpec;->getMode(I)I

    move-result v3

    sub-int/2addr v0, v1

    invoke-static {p1}, Landroid/view/View$MeasureSpec;->getMode(I)I

    move-result p1

    invoke-static {v0, p1}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p1

    const/high16 v0, 0x40000000

    if-ne v3, v0, :cond_4

    invoke-super {p0, p1, p2}, Landroid/widget/CheckedTextView;->onMeasure(II)V

    if-nez v1, :cond_3

    goto :goto_1

    :cond_3
    invoke-virtual {p0}, Landroid/widget/CheckedTextView;->getMeasuredWidth()I

    move-result p1

    add-int/2addr p1, v1

    invoke-virtual {p0}, Landroid/widget/CheckedTextView;->getMeasuredHeight()I

    move-result p2

    invoke-virtual {p0, p1, p2}, Landroid/widget/CheckedTextView;->setMeasuredDimension(II)V

    return-void

    :cond_4
    invoke-virtual {p0}, Landroid/widget/CheckedTextView;->getMinWidth()I

    move-result v0

    iget-boolean v3, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mDrawCheckMark:Z

    if-eqz v3, :cond_5

    invoke-virtual {p0, v2}, Landroid/widget/CheckedTextView;->setMinWidth(I)V

    invoke-virtual {p0, v2}, Landroid/widget/CheckedTextView;->setMinimumWidth(I)V

    :cond_5
    invoke-super {p0, p1, p2}, Landroid/widget/CheckedTextView;->onMeasure(II)V

    if-nez v1, :cond_6

    :goto_1
    return-void

    :cond_6
    invoke-virtual {p0}, Landroid/widget/CheckedTextView;->getMeasuredWidth()I

    move-result p1

    add-int/2addr p1, v1

    invoke-static {p1, v0}, Ljava/lang/Math;->max(II)I

    move-result p1

    invoke-virtual {p0}, Landroid/widget/CheckedTextView;->getMeasuredHeight()I

    move-result p2

    invoke-virtual {p0, p1, p2}, Landroid/widget/CheckedTextView;->setMeasuredDimension(II)V

    invoke-virtual {p0, v0}, Landroid/widget/CheckedTextView;->setMinWidth(I)V

    invoke-virtual {p0, v0}, Landroid/widget/CheckedTextView;->setMinimumWidth(I)V

    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 9

    goto :goto_0

    nop

    :goto_0
    invoke-static {p1}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v0

    goto :goto_37

    nop

    :goto_1
    iget-boolean v3, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mDrawCheckMark:Z

    goto :goto_16

    nop

    :goto_2
    if-lt v3, v5, :cond_0

    goto :goto_20

    :cond_0
    goto :goto_b

    nop

    :goto_3
    invoke-virtual {p0, v0}, Landroid/widget/CheckedTextView;->setMinWidth(I)V

    goto :goto_19

    nop

    :goto_4
    return-void

    :goto_5
    goto :goto_24

    nop

    :goto_6
    return-void

    :goto_7
    goto :goto_3a

    nop

    :goto_8
    invoke-virtual {p0}, Landroid/widget/CheckedTextView;->getMeasuredWidth()I

    move-result p1

    goto :goto_2b

    nop

    :goto_9
    add-int/2addr p1, v1

    goto :goto_11

    nop

    :goto_a
    sub-int/2addr v0, v1

    goto :goto_3c

    nop

    :goto_b
    iput-boolean v2, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mDrawCheckMark:Z

    goto :goto_d

    nop

    :goto_c
    if-eq v3, v0, :cond_1

    goto :goto_7

    :cond_1
    goto :goto_2f

    nop

    :goto_d
    move v1, v2

    goto :goto_1f

    nop

    :goto_e
    return-void

    :goto_f
    goto :goto_22

    nop

    :goto_10
    invoke-virtual {p0}, Landroid/widget/CheckedTextView;->getMeasuredHeight()I

    move-result p2

    goto :goto_39

    nop

    :goto_11
    invoke-static {p1, v0}, Ljava/lang/Math;->max(II)I

    move-result p1

    goto :goto_10

    nop

    :goto_12
    invoke-super {p0, p1, p2}, Landroid/widget/CheckedTextView;->onMeasure(II)V

    goto :goto_36

    nop

    :goto_13
    invoke-super {p0, p1, p2}, Landroid/widget/CheckedTextView;->onMeasure(II)V

    goto :goto_1a

    nop

    :goto_14
    sub-int v3, v0, v3

    goto :goto_32

    nop

    :goto_15
    invoke-virtual {p0, v1, p1}, Landroid/widget/CheckedTextView;->setMeasuredDimension(II)V

    goto :goto_e

    nop

    :goto_16
    if-nez v3, :cond_2

    goto :goto_1e

    :cond_2
    goto :goto_25

    nop

    :goto_17
    goto :goto_1b

    :goto_18
    goto :goto_8

    nop

    :goto_19
    invoke-virtual {p0, v0}, Landroid/widget/CheckedTextView;->setMinimumWidth(I)V

    goto :goto_26

    nop

    :goto_1a
    if-eqz v1, :cond_3

    goto :goto_5

    :cond_3
    :goto_1b
    goto :goto_4

    nop

    :goto_1c
    invoke-virtual {p0}, Landroid/widget/CheckedTextView;->getMeasuredHeight()I

    move-result p2

    goto :goto_33

    nop

    :goto_1d
    invoke-virtual {p0, v2}, Landroid/widget/CheckedTextView;->setMinimumWidth(I)V

    :goto_1e
    goto :goto_13

    nop

    :goto_1f
    goto :goto_2e

    :goto_20
    goto :goto_2d

    nop

    :goto_21
    const/4 v2, 0x0

    goto :goto_30

    nop

    :goto_22
    invoke-virtual {p0}, Landroid/widget/CheckedTextView;->getPaddingEnd()I

    move-result v3

    goto :goto_14

    nop

    :goto_23
    if-eqz v1, :cond_4

    goto :goto_18

    :cond_4
    goto :goto_17

    nop

    :goto_24
    invoke-virtual {p0}, Landroid/widget/CheckedTextView;->getMeasuredWidth()I

    move-result p1

    goto :goto_9

    nop

    :goto_25
    invoke-virtual {p0, v2}, Landroid/widget/CheckedTextView;->setMinWidth(I)V

    goto :goto_1d

    nop

    :goto_26
    return-void

    :goto_27
    invoke-static {p1}, Landroid/view/View$MeasureSpec;->getMode(I)I

    move-result p1

    goto :goto_38

    nop

    :goto_28
    const/high16 v0, 0x40000000

    goto :goto_c

    nop

    :goto_29
    invoke-virtual {p0}, Landroid/widget/CheckedTextView;->getText()Ljava/lang/CharSequence;

    move-result-object v3

    goto :goto_2a

    nop

    :goto_2a
    invoke-static {v3}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v3

    goto :goto_3b

    nop

    :goto_2b
    add-int/2addr p1, v1

    goto :goto_1c

    nop

    :goto_2c
    iput-boolean v4, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mDrawCheckMark:Z

    goto :goto_27

    nop

    :goto_2d
    iput-boolean v4, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mDrawCheckMark:Z

    :goto_2e
    goto :goto_34

    nop

    :goto_2f
    invoke-super {p0, p1, p2}, Landroid/widget/CheckedTextView;->onMeasure(II)V

    goto :goto_23

    nop

    :goto_30
    if-gtz v1, :cond_5

    goto :goto_2e

    :cond_5
    goto :goto_29

    nop

    :goto_31
    if-nez v3, :cond_6

    goto :goto_f

    :cond_6
    goto :goto_2c

    nop

    :goto_32
    mul-int/lit8 v5, v1, 0x2

    goto :goto_2

    nop

    :goto_33
    invoke-virtual {p0, p1, p2}, Landroid/widget/CheckedTextView;->setMeasuredDimension(II)V

    goto :goto_6

    nop

    :goto_34
    invoke-static {p1}, Landroid/view/View$MeasureSpec;->getMode(I)I

    move-result v3

    goto :goto_a

    nop

    :goto_35
    invoke-static {v0, p1}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p1

    goto :goto_28

    nop

    :goto_36
    invoke-virtual {p0}, Landroid/widget/CheckedTextView;->getMeasuredHeight()I

    move-result p1

    goto :goto_15

    nop

    :goto_37
    invoke-direct {p0}, Lmiuix/androidbasewidget/widget/CheckedTextView;->getCheckWidth()I

    move-result v1

    goto :goto_21

    nop

    :goto_38
    invoke-static {v1, p1}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p1

    goto :goto_12

    nop

    :goto_39
    invoke-virtual {p0, p1, p2}, Landroid/widget/CheckedTextView;->setMeasuredDimension(II)V

    goto :goto_3

    nop

    :goto_3a
    invoke-virtual {p0}, Landroid/widget/CheckedTextView;->getMinWidth()I

    move-result v0

    goto :goto_1

    nop

    :goto_3b
    const/4 v4, 0x1

    goto :goto_31

    nop

    :goto_3c
    invoke-static {p1}, Landroid/view/View$MeasureSpec;->getMode(I)I

    move-result p1

    goto :goto_35

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_androidbasewidget_widget_CheckedTextView__onTextChanged',
        'method': '.method protected onTextChanged(Ljava/lang/CharSequence;III)V',
        'method_name': 'onTextChanged',
        'method_anchors': ['invoke-super {p0, p1, p2, p3, p4}, Landroid/widget/CheckedTextView;->onTextChanged(Ljava/lang/CharSequence;III)V', 'invoke-virtual {p0}, Landroid/widget/CheckedTextView;->requestLayout()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onTextChanged(Ljava/lang/CharSequence;III)V
    .registers 5

    invoke-super {p0, p1, p2, p3, p4}, Landroid/widget/CheckedTextView;->onTextChanged(Ljava/lang/CharSequence;III)V

    invoke-virtual {p0}, Landroid/widget/CheckedTextView;->requestLayout()V

    return-void
.end method""",
        'replacement': """.method protected onTextChanged(Ljava/lang/CharSequence;III)V
    .registers 5

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0, p1, p2, p3, p4}, Landroid/widget/CheckedTextView;->onTextChanged(Ljava/lang/CharSequence;III)V

    goto :goto_1

    nop

    :goto_1
    invoke-virtual {p0}, Landroid/widget/CheckedTextView;->requestLayout()V

    goto :goto_2

    nop

    :goto_2
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_androidbasewidget_widget_CheckedTextView__verifyDrawable',
        'method': '.method protected verifyDrawable(Landroid/graphics/drawable/Drawable;)Z',
        'method_name': 'verifyDrawable',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/widget/CheckedTextView;->verifyDrawable(Landroid/graphics/drawable/Drawable;)Z', 'if-nez v0, :cond_1', 'iget-object p0, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mCheckMarkDrawable:Landroid/graphics/drawable/Drawable;', 'if-ne p1, p0, :cond_0', 'return p0', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected verifyDrawable(Landroid/graphics/drawable/Drawable;)Z
    .registers 3

    invoke-super {p0, p1}, Landroid/widget/CheckedTextView;->verifyDrawable(Landroid/graphics/drawable/Drawable;)Z

    move-result v0

    if-nez v0, :cond_1

    iget-object p0, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mCheckMarkDrawable:Landroid/graphics/drawable/Drawable;

    if-ne p1, p0, :cond_0

    goto :goto_0

    :cond_0
    const/4 p0, 0x0

    return p0

    :cond_1
    :goto_0
    const/4 p0, 0x1

    return p0
.end method""",
        'replacement': """.method protected verifyDrawable(Landroid/graphics/drawable/Drawable;)Z
    .registers 3

    goto :goto_6

    nop

    :goto_0
    goto :goto_9

    :goto_1
    goto :goto_3

    nop

    :goto_2
    if-eq p1, p0, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_0

    nop

    :goto_3
    const/4 p0, 0x0

    goto :goto_8

    nop

    :goto_4
    iget-object p0, p0, Lmiuix/androidbasewidget/widget/CheckedTextView;->mCheckMarkDrawable:Landroid/graphics/drawable/Drawable;

    goto :goto_2

    nop

    :goto_5
    return p0

    :goto_6
    invoke-super {p0, p1}, Landroid/widget/CheckedTextView;->verifyDrawable(Landroid/graphics/drawable/Drawable;)Z

    move-result v0

    goto :goto_a

    nop

    :goto_7
    const/4 p0, 0x1

    goto :goto_5

    nop

    :goto_8
    return p0

    :goto_9
    goto :goto_7

    nop

    :goto_a
    if-eqz v0, :cond_1

    goto :goto_9

    :cond_1
    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
