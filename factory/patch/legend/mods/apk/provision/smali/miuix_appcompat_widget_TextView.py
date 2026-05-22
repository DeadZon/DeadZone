TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/widget/TextView.smali'
CLASS_FALLBACK_NAMES = ['TextView.smali']
CLASS_ANCHORS = ['.super Landroidx/appcompat/widget/AppCompatTextView;', '.field private static final TEXT_COLOR_PROPERTY:Lmiuix/animation/property/ColorProperty;']

PATCHES = [
    {
        'id': 'miuix_appcompat_widget_TextView__drawableStateChanged',
        'method': '.method protected drawableStateChanged()V',
        'method_name': 'drawableStateChanged',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/widget/TextView;->mFolmeAnimator:Lmiuix/animation/IFolme;', 'if-nez v0, :cond_0', 'invoke-super {p0}, Landroidx/appcompat/widget/AppCompatTextView;->drawableStateChanged()V', 'return-void', 'invoke-virtual {p0}, Landroid/widget/TextView;->getCurrentTextColor()I', 'invoke-super {p0}, Landroidx/appcompat/widget/AppCompatTextView;->drawableStateChanged()V', 'invoke-virtual {p0}, Landroid/widget/TextView;->getCurrentTextColor()I', 'iget-object v2, p0, Lmiuix/appcompat/widget/TextView;->mCurrentTextColorStateList:Landroid/content/res/ColorStateList;'],
        'type': 'method_replace',
        'search': """.method protected drawableStateChanged()V
    .registers 5

    iget-object v0, p0, Lmiuix/appcompat/widget/TextView;->mFolmeAnimator:Lmiuix/animation/IFolme;

    if-nez v0, :cond_0

    invoke-super {p0}, Landroidx/appcompat/widget/AppCompatTextView;->drawableStateChanged()V

    return-void

    :cond_0
    invoke-virtual {p0}, Landroid/widget/TextView;->getCurrentTextColor()I

    move-result v0

    invoke-super {p0}, Landroidx/appcompat/widget/AppCompatTextView;->drawableStateChanged()V

    invoke-virtual {p0}, Landroid/widget/TextView;->getCurrentTextColor()I

    move-result v1

    iget-object v2, p0, Lmiuix/appcompat/widget/TextView;->mCurrentTextColorStateList:Landroid/content/res/ColorStateList;

    if-eqz v2, :cond_1

    invoke-virtual {p0}, Landroid/widget/TextView;->getDrawableState()[I

    move-result-object v1

    iget-object v3, p0, Lmiuix/appcompat/widget/TextView;->mCurrentTextColorStateList:Landroid/content/res/ColorStateList;

    invoke-virtual {v3}, Landroid/content/res/ColorStateList;->getDefaultColor()I

    move-result v3

    invoke-virtual {v2, v1, v3}, Landroid/content/res/ColorStateList;->getColorForState([II)I

    move-result v1

    :cond_1
    if-eq v0, v1, :cond_2

    iput v0, p0, Lmiuix/appcompat/widget/TextView;->mCurrentTextColorInAnim:I

    invoke-virtual {p0, v1}, Lmiuix/appcompat/widget/TextView;->startTextColorTransition(I)V

    :cond_2
    return-void
.end method""",
        'replacement': """.method protected drawableStateChanged()V
    .registers 5

    goto :goto_1

    nop

    :goto_0
    invoke-super {p0}, Landroidx/appcompat/widget/AppCompatTextView;->drawableStateChanged()V

    goto :goto_c

    nop

    :goto_1
    iget-object v0, p0, Lmiuix/appcompat/widget/TextView;->mFolmeAnimator:Lmiuix/animation/IFolme;

    goto :goto_2

    nop

    :goto_2
    if-eqz v0, :cond_0

    goto :goto_e

    :cond_0
    goto :goto_7

    nop

    :goto_3
    iput v0, p0, Lmiuix/appcompat/widget/TextView;->mCurrentTextColorInAnim:I

    goto :goto_a

    nop

    :goto_4
    invoke-virtual {v2, v1, v3}, Landroid/content/res/ColorStateList;->getColorForState([II)I

    move-result v1

    :goto_5
    goto :goto_13

    nop

    :goto_6
    iget-object v2, p0, Lmiuix/appcompat/widget/TextView;->mCurrentTextColorStateList:Landroid/content/res/ColorStateList;

    goto :goto_9

    nop

    :goto_7
    invoke-super {p0}, Landroidx/appcompat/widget/AppCompatTextView;->drawableStateChanged()V

    goto :goto_d

    nop

    :goto_8
    invoke-virtual {p0}, Landroid/widget/TextView;->getCurrentTextColor()I

    move-result v0

    goto :goto_0

    nop

    :goto_9
    if-nez v2, :cond_1

    goto :goto_5

    :cond_1
    goto :goto_11

    nop

    :goto_a
    invoke-virtual {p0, v1}, Lmiuix/appcompat/widget/TextView;->startTextColorTransition(I)V

    :goto_b
    goto :goto_10

    nop

    :goto_c
    invoke-virtual {p0}, Landroid/widget/TextView;->getCurrentTextColor()I

    move-result v1

    goto :goto_6

    nop

    :goto_d
    return-void

    :goto_e
    goto :goto_8

    nop

    :goto_f
    invoke-virtual {v3}, Landroid/content/res/ColorStateList;->getDefaultColor()I

    move-result v3

    goto :goto_4

    nop

    :goto_10
    return-void

    :goto_11
    invoke-virtual {p0}, Landroid/widget/TextView;->getDrawableState()[I

    move-result-object v1

    goto :goto_12

    nop

    :goto_12
    iget-object v3, p0, Lmiuix/appcompat/widget/TextView;->mCurrentTextColorStateList:Landroid/content/res/ColorStateList;

    goto :goto_f

    nop

    :goto_13
    if-ne v0, v1, :cond_2

    goto :goto_b

    :cond_2
    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_widget_TextView__onDetachedFromWindow',
        'method': '.method protected onDetachedFromWindow()V',
        'method_name': 'onDetachedFromWindow',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/TextView;->onDetachedFromWindow()V', 'iget-object v0, p0, Lmiuix/appcompat/widget/TextView;->mFolmeAnimator:Lmiuix/animation/IFolme;', 'if-eqz v0, :cond_0', 'invoke-interface {v0}, Lmiuix/animation/IFolme;->state()Lmiuix/animation/IStateStyle;', 'invoke-interface {v0}, Lmiuix/animation/ICancelableStyle;->cancel()V', 'iget-object v0, p0, Lmiuix/appcompat/widget/TextView;->mInitAnimatorTask:Ljava/lang/Runnable;', 'invoke-virtual {p0, v0}, Landroid/widget/TextView;->removeCallbacks(Ljava/lang/Runnable;)Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onDetachedFromWindow()V
    .registers 2

    invoke-super {p0}, Landroid/widget/TextView;->onDetachedFromWindow()V

    iget-object v0, p0, Lmiuix/appcompat/widget/TextView;->mFolmeAnimator:Lmiuix/animation/IFolme;

    if-eqz v0, :cond_0

    invoke-interface {v0}, Lmiuix/animation/IFolme;->state()Lmiuix/animation/IStateStyle;

    move-result-object v0

    invoke-interface {v0}, Lmiuix/animation/ICancelableStyle;->cancel()V

    :cond_0
    iget-object v0, p0, Lmiuix/appcompat/widget/TextView;->mInitAnimatorTask:Ljava/lang/Runnable;

    invoke-virtual {p0, v0}, Landroid/widget/TextView;->removeCallbacks(Ljava/lang/Runnable;)Z

    return-void
.end method""",
        'replacement': """.method protected onDetachedFromWindow()V
    .registers 2

    goto :goto_8

    nop

    :goto_0
    return-void

    :goto_1
    invoke-interface {v0}, Lmiuix/animation/IFolme;->state()Lmiuix/animation/IStateStyle;

    move-result-object v0

    goto :goto_5

    nop

    :goto_2
    if-nez v0, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_1

    nop

    :goto_3
    invoke-virtual {p0, v0}, Landroid/widget/TextView;->removeCallbacks(Ljava/lang/Runnable;)Z

    goto :goto_0

    nop

    :goto_4
    iget-object v0, p0, Lmiuix/appcompat/widget/TextView;->mInitAnimatorTask:Ljava/lang/Runnable;

    goto :goto_3

    nop

    :goto_5
    invoke-interface {v0}, Lmiuix/animation/ICancelableStyle;->cancel()V

    :goto_6
    goto :goto_4

    nop

    :goto_7
    iget-object v0, p0, Lmiuix/appcompat/widget/TextView;->mFolmeAnimator:Lmiuix/animation/IFolme;

    goto :goto_2

    nop

    :goto_8
    invoke-super {p0}, Landroid/widget/TextView;->onDetachedFromWindow()V

    goto :goto_7

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
