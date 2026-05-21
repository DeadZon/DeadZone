TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/androidbasewidget/widget/ClearableEditText.smali'
CLASS_FALLBACK_NAMES = ['ClearableEditText.smali']
CLASS_ANCHORS = ['.super Lmiuix/androidbasewidget/widget/EditText;', '.field private static final EMPTY_STATE_SET:[I']

PATCHES = [
    {
        'id': 'miuix_androidbasewidget_widget_ClearableEditText__dispatchHoverEvent',
        'method': '.method protected dispatchHoverEvent(Landroid/view/MotionEvent;)Z',
        'method_name': 'dispatchHoverEvent',
        'method_anchors': ['iget-object v0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText;->mAccessHelper:Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;', 'if-eqz v0, :cond_0', 'iget-boolean v1, p0, Lmiuix/androidbasewidget/widget/ClearableEditText;->mShown:Z', 'if-eqz v1, :cond_0', 'invoke-virtual {v0, p1}, Landroidx/customview/widget/ExploreByTouchHelper;->dispatchHoverEvent(Landroid/view/MotionEvent;)Z', 'if-eqz v0, :cond_0', 'return p0', 'invoke-super {p0, p1}, Landroid/widget/EditText;->dispatchHoverEvent(Landroid/view/MotionEvent;)Z'],
        'type': 'method_replace',
        'search': """.method protected dispatchHoverEvent(Landroid/view/MotionEvent;)Z
    .registers 4

    iget-object v0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText;->mAccessHelper:Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;

    if-eqz v0, :cond_0

    iget-boolean v1, p0, Lmiuix/androidbasewidget/widget/ClearableEditText;->mShown:Z

    if-eqz v1, :cond_0

    invoke-virtual {v0, p1}, Landroidx/customview/widget/ExploreByTouchHelper;->dispatchHoverEvent(Landroid/view/MotionEvent;)Z

    move-result v0

    if-eqz v0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    invoke-super {p0, p1}, Landroid/widget/EditText;->dispatchHoverEvent(Landroid/view/MotionEvent;)Z

    move-result p0

    return p0
.end method""",
        'replacement': """.method protected dispatchHoverEvent(Landroid/view/MotionEvent;)Z
    .registers 4

    goto :goto_7

    nop

    :goto_0
    return p0

    :goto_1
    goto :goto_2

    nop

    :goto_2
    invoke-super {p0, p1}, Landroid/widget/EditText;->dispatchHoverEvent(Landroid/view/MotionEvent;)Z

    move-result p0

    goto :goto_9

    nop

    :goto_3
    if-nez v1, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_6

    nop

    :goto_4
    iget-boolean v1, p0, Lmiuix/androidbasewidget/widget/ClearableEditText;->mShown:Z

    goto :goto_3

    nop

    :goto_5
    if-nez v0, :cond_1

    goto :goto_1

    :cond_1
    goto :goto_a

    nop

    :goto_6
    invoke-virtual {v0, p1}, Landroidx/customview/widget/ExploreByTouchHelper;->dispatchHoverEvent(Landroid/view/MotionEvent;)Z

    move-result v0

    goto :goto_5

    nop

    :goto_7
    iget-object v0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText;->mAccessHelper:Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;

    goto :goto_8

    nop

    :goto_8
    if-nez v0, :cond_2

    goto :goto_1

    :cond_2
    goto :goto_4

    nop

    :goto_9
    return p0

    :goto_a
    const/4 p0, 0x1

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_androidbasewidget_widget_ClearableEditText__drawableStateChanged',
        'method': '.method protected drawableStateChanged()V',
        'method_name': 'drawableStateChanged',
        'method_anchors': ['invoke-super {p0}, Landroidx/appcompat/widget/AppCompatEditText;->drawableStateChanged()V', 'iget-object v0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText;->mDrawable:Landroid/graphics/drawable/Drawable;', 'if-eqz v0, :cond_0', 'invoke-virtual {p0}, Landroid/widget/EditText;->getDrawableState()[I', 'iget-object v1, p0, Lmiuix/androidbasewidget/widget/ClearableEditText;->mDrawable:Landroid/graphics/drawable/Drawable;', 'if-eqz v1, :cond_0', 'invoke-virtual {v1}, Landroid/graphics/drawable/Drawable;->isStateful()Z', 'if-eqz v1, :cond_0'],
        'type': 'method_replace',
        'search': """.method protected drawableStateChanged()V
    .registers 3

    invoke-super {p0}, Landroidx/appcompat/widget/AppCompatEditText;->drawableStateChanged()V

    iget-object v0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText;->mDrawable:Landroid/graphics/drawable/Drawable;

    if-eqz v0, :cond_0

    invoke-virtual {p0}, Landroid/widget/EditText;->getDrawableState()[I

    move-result-object v0

    iget-object v1, p0, Lmiuix/androidbasewidget/widget/ClearableEditText;->mDrawable:Landroid/graphics/drawable/Drawable;

    if-eqz v1, :cond_0

    invoke-virtual {v1}, Landroid/graphics/drawable/Drawable;->isStateful()Z

    move-result v1

    if-eqz v1, :cond_0

    iget-object v1, p0, Lmiuix/androidbasewidget/widget/ClearableEditText;->mDrawable:Landroid/graphics/drawable/Drawable;

    invoke-virtual {v1, v0}, Landroid/graphics/drawable/Drawable;->setState([I)Z

    move-result v0

    if-eqz v0, :cond_0

    iget-object v0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText;->mDrawable:Landroid/graphics/drawable/Drawable;

    invoke-virtual {p0, v0}, Landroid/widget/EditText;->invalidateDrawable(Landroid/graphics/drawable/Drawable;)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected drawableStateChanged()V
    .registers 3

    goto :goto_c

    nop

    :goto_0
    if-nez v0, :cond_0

    goto :goto_a

    :cond_0
    goto :goto_d

    nop

    :goto_1
    iget-object v0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText;->mDrawable:Landroid/graphics/drawable/Drawable;

    goto :goto_9

    nop

    :goto_2
    invoke-virtual {v1, v0}, Landroid/graphics/drawable/Drawable;->setState([I)Z

    move-result v0

    goto :goto_e

    nop

    :goto_3
    if-nez v1, :cond_1

    goto :goto_a

    :cond_1
    goto :goto_8

    nop

    :goto_4
    iget-object v1, p0, Lmiuix/androidbasewidget/widget/ClearableEditText;->mDrawable:Landroid/graphics/drawable/Drawable;

    goto :goto_b

    nop

    :goto_5
    invoke-virtual {v1}, Landroid/graphics/drawable/Drawable;->isStateful()Z

    move-result v1

    goto :goto_3

    nop

    :goto_6
    return-void

    :goto_7
    iget-object v0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText;->mDrawable:Landroid/graphics/drawable/Drawable;

    goto :goto_0

    nop

    :goto_8
    iget-object v1, p0, Lmiuix/androidbasewidget/widget/ClearableEditText;->mDrawable:Landroid/graphics/drawable/Drawable;

    goto :goto_2

    nop

    :goto_9
    invoke-virtual {p0, v0}, Landroid/widget/EditText;->invalidateDrawable(Landroid/graphics/drawable/Drawable;)V

    :goto_a
    goto :goto_6

    nop

    :goto_b
    if-nez v1, :cond_2

    goto :goto_a

    :cond_2
    goto :goto_5

    nop

    :goto_c
    invoke-super {p0}, Landroidx/appcompat/widget/AppCompatEditText;->drawableStateChanged()V

    goto :goto_7

    nop

    :goto_d
    invoke-virtual {p0}, Landroid/widget/EditText;->getDrawableState()[I

    move-result-object v0

    goto :goto_4

    nop

    :goto_e
    if-nez v0, :cond_3

    goto :goto_a

    :cond_3
    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_androidbasewidget_widget_ClearableEditText__onAttachedToWindow',
        'method': '.method protected onAttachedToWindow()V',
        'method_name': 'onAttachedToWindow',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/EditText;->onAttachedToWindow()V', 'iget-object v0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText;->mTextWatcher:Lmiuix/androidbasewidget/widget/ClearableEditText$ShowWidgetTextWatcher;', 'invoke-virtual {p0, v0}, Landroid/widget/EditText;->removeTextChangedListener(Landroid/text/TextWatcher;)V', 'iget-object v0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText;->mTextWatcher:Lmiuix/androidbasewidget/widget/ClearableEditText$ShowWidgetTextWatcher;', 'invoke-virtual {p0, v0}, Landroid/widget/EditText;->addTextChangedListener(Landroid/text/TextWatcher;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onAttachedToWindow()V
    .registers 2

    invoke-super {p0}, Landroid/widget/EditText;->onAttachedToWindow()V

    iget-object v0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText;->mTextWatcher:Lmiuix/androidbasewidget/widget/ClearableEditText$ShowWidgetTextWatcher;

    invoke-virtual {p0, v0}, Landroid/widget/EditText;->removeTextChangedListener(Landroid/text/TextWatcher;)V

    iget-object v0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText;->mTextWatcher:Lmiuix/androidbasewidget/widget/ClearableEditText$ShowWidgetTextWatcher;

    invoke-virtual {p0, v0}, Landroid/widget/EditText;->addTextChangedListener(Landroid/text/TextWatcher;)V

    return-void
.end method""",
        'replacement': """.method protected onAttachedToWindow()V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0}, Landroid/widget/EditText;->onAttachedToWindow()V

    goto :goto_3

    nop

    :goto_1
    return-void

    :goto_2
    invoke-virtual {p0, v0}, Landroid/widget/EditText;->addTextChangedListener(Landroid/text/TextWatcher;)V

    goto :goto_1

    nop

    :goto_3
    iget-object v0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText;->mTextWatcher:Lmiuix/androidbasewidget/widget/ClearableEditText$ShowWidgetTextWatcher;

    goto :goto_4

    nop

    :goto_4
    invoke-virtual {p0, v0}, Landroid/widget/EditText;->removeTextChangedListener(Landroid/text/TextWatcher;)V

    goto :goto_5

    nop

    :goto_5
    iget-object v0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText;->mTextWatcher:Lmiuix/androidbasewidget/widget/ClearableEditText$ShowWidgetTextWatcher;

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_androidbasewidget_widget_ClearableEditText__onCreateDrawableState',
        'method': '.method protected onCreateDrawableState(I)[I',
        'method_name': 'onCreateDrawableState',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/widget/EditText;->onCreateDrawableState(I)[I', 'iget-boolean p0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText;->mShown:Z', 'if-nez p0, :cond_0', 'sget-object p0, Lmiuix/androidbasewidget/widget/ClearableEditText;->EMPTY_STATE_SET:[I', 'invoke-static {p1, p0}, Landroid/widget/EditText;->mergeDrawableStates([I[I)[I', 'return-object p1'],
        'type': 'method_replace',
        'search': """.method protected onCreateDrawableState(I)[I
    .registers 2

    add-int/lit8 p1, p1, 0x1

    invoke-super {p0, p1}, Landroid/widget/EditText;->onCreateDrawableState(I)[I

    move-result-object p1

    iget-boolean p0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText;->mShown:Z

    if-nez p0, :cond_0

    sget-object p0, Lmiuix/androidbasewidget/widget/ClearableEditText;->EMPTY_STATE_SET:[I

    invoke-static {p1, p0}, Landroid/widget/EditText;->mergeDrawableStates([I[I)[I

    :cond_0
    return-object p1
.end method""",
        'replacement': """.method protected onCreateDrawableState(I)[I
    .registers 2

    goto :goto_7

    nop

    :goto_0
    if-eqz p0, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_1

    nop

    :goto_1
    sget-object p0, Lmiuix/androidbasewidget/widget/ClearableEditText;->EMPTY_STATE_SET:[I

    goto :goto_5

    nop

    :goto_2
    invoke-super {p0, p1}, Landroid/widget/EditText;->onCreateDrawableState(I)[I

    move-result-object p1

    goto :goto_3

    nop

    :goto_3
    iget-boolean p0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText;->mShown:Z

    goto :goto_0

    nop

    :goto_4
    return-object p1

    :goto_5
    invoke-static {p1, p0}, Landroid/widget/EditText;->mergeDrawableStates([I[I)[I

    :goto_6
    goto :goto_4

    nop

    :goto_7
    add-int/lit8 p1, p1, 0x1

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_androidbasewidget_widget_ClearableEditText__onDetachedFromWindow',
        'method': '.method protected onDetachedFromWindow()V',
        'method_name': 'onDetachedFromWindow',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/EditText;->onDetachedFromWindow()V', 'iget-object v0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText;->mTextWatcher:Lmiuix/androidbasewidget/widget/ClearableEditText$ShowWidgetTextWatcher;', 'invoke-virtual {p0, v0}, Landroid/widget/EditText;->removeTextChangedListener(Landroid/text/TextWatcher;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onDetachedFromWindow()V
    .registers 2

    invoke-super {p0}, Landroid/widget/EditText;->onDetachedFromWindow()V

    iget-object v0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText;->mTextWatcher:Lmiuix/androidbasewidget/widget/ClearableEditText$ShowWidgetTextWatcher;

    invoke-virtual {p0, v0}, Landroid/widget/EditText;->removeTextChangedListener(Landroid/text/TextWatcher;)V

    return-void
.end method""",
        'replacement': """.method protected onDetachedFromWindow()V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    invoke-super {p0}, Landroid/widget/EditText;->onDetachedFromWindow()V

    goto :goto_2

    nop

    :goto_2
    iget-object v0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText;->mTextWatcher:Lmiuix/androidbasewidget/widget/ClearableEditText$ShowWidgetTextWatcher;

    goto :goto_3

    nop

    :goto_3
    invoke-virtual {p0, v0}, Landroid/widget/EditText;->removeTextChangedListener(Landroid/text/TextWatcher;)V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_androidbasewidget_widget_ClearableEditText__verifyDrawable',
        'method': '.method protected verifyDrawable(Landroid/graphics/drawable/Drawable;)Z',
        'method_name': 'verifyDrawable',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/widget/EditText;->verifyDrawable(Landroid/graphics/drawable/Drawable;)Z', 'if-nez v0, :cond_1', 'iget-object p0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText;->mDrawable:Landroid/graphics/drawable/Drawable;', 'if-ne p1, p0, :cond_0', 'return p0', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected verifyDrawable(Landroid/graphics/drawable/Drawable;)Z
    .registers 3

    invoke-super {p0, p1}, Landroid/widget/EditText;->verifyDrawable(Landroid/graphics/drawable/Drawable;)Z

    move-result v0

    if-nez v0, :cond_1

    iget-object p0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText;->mDrawable:Landroid/graphics/drawable/Drawable;

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

    goto :goto_2

    nop

    :goto_0
    if-eqz v0, :cond_0

    goto :goto_9

    :cond_0
    goto :goto_5

    nop

    :goto_1
    const/4 p0, 0x1

    goto :goto_6

    nop

    :goto_2
    invoke-super {p0, p1}, Landroid/widget/EditText;->verifyDrawable(Landroid/graphics/drawable/Drawable;)Z

    move-result v0

    goto :goto_0

    nop

    :goto_3
    goto :goto_9

    :goto_4
    goto :goto_7

    nop

    :goto_5
    iget-object p0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText;->mDrawable:Landroid/graphics/drawable/Drawable;

    goto :goto_a

    nop

    :goto_6
    return p0

    :goto_7
    const/4 p0, 0x0

    goto :goto_8

    nop

    :goto_8
    return p0

    :goto_9
    goto :goto_1

    nop

    :goto_a
    if-eq p1, p0, :cond_1

    goto :goto_4

    :cond_1
    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
