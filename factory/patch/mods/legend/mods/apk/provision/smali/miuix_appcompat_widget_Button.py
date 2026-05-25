TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/widget/Button.smali'
CLASS_FALLBACK_NAMES = ['Button.smali']
CLASS_ANCHORS = ['.super Landroidx/appcompat/widget/AppCompatButton;', '.implements Lmiuix/view/BlurableWidget;', '.field private static final TEXT_COLOR_PROPERTY:Lmiuix/animation/property/ColorProperty;']

PATCHES = [
    {
        'id': 'miuix_appcompat_widget_Button__drawableStateChanged',
        'method': '.method protected drawableStateChanged()V',
        'method_name': 'drawableStateChanged',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/widget/Button;->mFolmeAnimator:Lmiuix/animation/IFolme;', 'if-nez v0, :cond_0', 'invoke-super {p0}, Landroidx/appcompat/widget/AppCompatButton;->drawableStateChanged()V', 'return-void', 'invoke-virtual {p0}, Landroid/widget/Button;->getCurrentTextColor()I', 'invoke-super {p0}, Landroidx/appcompat/widget/AppCompatButton;->drawableStateChanged()V', 'invoke-virtual {p0}, Landroid/widget/Button;->getCurrentTextColor()I', 'iget-object v2, p0, Lmiuix/appcompat/widget/Button;->mCurrentTextColorStateList:Landroid/content/res/ColorStateList;'],
        'type': 'method_replace',
        'search': """.method protected drawableStateChanged()V
    .registers 5

    iget-object v0, p0, Lmiuix/appcompat/widget/Button;->mFolmeAnimator:Lmiuix/animation/IFolme;

    if-nez v0, :cond_0

    invoke-super {p0}, Landroidx/appcompat/widget/AppCompatButton;->drawableStateChanged()V

    return-void

    :cond_0
    invoke-virtual {p0}, Landroid/widget/Button;->getCurrentTextColor()I

    move-result v0

    invoke-super {p0}, Landroidx/appcompat/widget/AppCompatButton;->drawableStateChanged()V

    invoke-virtual {p0}, Landroid/widget/Button;->getCurrentTextColor()I

    move-result v1

    iget-object v2, p0, Lmiuix/appcompat/widget/Button;->mCurrentTextColorStateList:Landroid/content/res/ColorStateList;

    if-eqz v2, :cond_1

    invoke-virtual {p0}, Landroid/widget/Button;->getDrawableState()[I

    move-result-object v1

    iget-object v3, p0, Lmiuix/appcompat/widget/Button;->mCurrentTextColorStateList:Landroid/content/res/ColorStateList;

    invoke-virtual {v3}, Landroid/content/res/ColorStateList;->getDefaultColor()I

    move-result v3

    invoke-virtual {v2, v1, v3}, Landroid/content/res/ColorStateList;->getColorForState([II)I

    move-result v1

    :cond_1
    if-eq v0, v1, :cond_2

    iput v0, p0, Lmiuix/appcompat/widget/Button;->mCurrentTextColorInAnim:I

    invoke-virtual {p0, v1}, Lmiuix/appcompat/widget/Button;->startTextColorTransition(I)V

    :cond_2
    return-void
.end method""",
        'replacement': """.method protected drawableStateChanged()V
    .registers 5

    goto :goto_3

    nop

    :goto_0
    return-void

    :goto_1
    goto :goto_e

    nop

    :goto_2
    iget-object v3, p0, Lmiuix/appcompat/widget/Button;->mCurrentTextColorStateList:Landroid/content/res/ColorStateList;

    goto :goto_f

    nop

    :goto_3
    iget-object v0, p0, Lmiuix/appcompat/widget/Button;->mFolmeAnimator:Lmiuix/animation/IFolme;

    goto :goto_4

    nop

    :goto_4
    if-eqz v0, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_13

    nop

    :goto_5
    return-void

    :goto_6
    iput v0, p0, Lmiuix/appcompat/widget/Button;->mCurrentTextColorInAnim:I

    goto :goto_b

    nop

    :goto_7
    invoke-virtual {p0}, Landroid/widget/Button;->getDrawableState()[I

    move-result-object v1

    goto :goto_2

    nop

    :goto_8
    invoke-super {p0}, Landroidx/appcompat/widget/AppCompatButton;->drawableStateChanged()V

    goto :goto_d

    nop

    :goto_9
    iget-object v2, p0, Lmiuix/appcompat/widget/Button;->mCurrentTextColorStateList:Landroid/content/res/ColorStateList;

    goto :goto_a

    nop

    :goto_a
    if-nez v2, :cond_1

    goto :goto_11

    :cond_1
    goto :goto_7

    nop

    :goto_b
    invoke-virtual {p0, v1}, Lmiuix/appcompat/widget/Button;->startTextColorTransition(I)V

    :goto_c
    goto :goto_5

    nop

    :goto_d
    invoke-virtual {p0}, Landroid/widget/Button;->getCurrentTextColor()I

    move-result v1

    goto :goto_9

    nop

    :goto_e
    invoke-virtual {p0}, Landroid/widget/Button;->getCurrentTextColor()I

    move-result v0

    goto :goto_8

    nop

    :goto_f
    invoke-virtual {v3}, Landroid/content/res/ColorStateList;->getDefaultColor()I

    move-result v3

    goto :goto_10

    nop

    :goto_10
    invoke-virtual {v2, v1, v3}, Landroid/content/res/ColorStateList;->getColorForState([II)I

    move-result v1

    :goto_11
    goto :goto_12

    nop

    :goto_12
    if-ne v0, v1, :cond_2

    goto :goto_c

    :cond_2
    goto :goto_6

    nop

    :goto_13
    invoke-super {p0}, Landroidx/appcompat/widget/AppCompatButton;->drawableStateChanged()V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_widget_Button__onConfigurationChanged',
        'method': '.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V',
        'method_name': 'onConfigurationChanged',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/widget/Button;->onConfigurationChanged(Landroid/content/res/Configuration;)V', 'invoke-virtual {p0}, Lmiuix/appcompat/widget/Button;->updateMaterialEffect()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 2

    invoke-super {p0, p1}, Landroid/widget/Button;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    invoke-virtual {p0}, Lmiuix/appcompat/widget/Button;->updateMaterialEffect()V

    return-void
.end method""",
        'replacement': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    invoke-super {p0, p1}, Landroid/widget/Button;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    goto :goto_2

    nop

    :goto_2
    invoke-virtual {p0}, Lmiuix/appcompat/widget/Button;->updateMaterialEffect()V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_widget_Button__onDetachedFromWindow',
        'method': '.method protected onDetachedFromWindow()V',
        'method_name': 'onDetachedFromWindow',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/Button;->onDetachedFromWindow()V', 'iget-object v0, p0, Lmiuix/appcompat/widget/Button;->mFolmeAnimator:Lmiuix/animation/IFolme;', 'if-eqz v0, :cond_0', 'invoke-interface {v0}, Lmiuix/animation/IFolme;->state()Lmiuix/animation/IStateStyle;', 'invoke-interface {v0}, Lmiuix/animation/ICancelableStyle;->cancel()V', 'iget-object v0, p0, Lmiuix/appcompat/widget/Button;->mInitAnimatorTask:Ljava/lang/Runnable;', 'invoke-virtual {p0, v0}, Landroid/widget/Button;->removeCallbacks(Ljava/lang/Runnable;)Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onDetachedFromWindow()V
    .registers 2

    invoke-super {p0}, Landroid/widget/Button;->onDetachedFromWindow()V

    iget-object v0, p0, Lmiuix/appcompat/widget/Button;->mFolmeAnimator:Lmiuix/animation/IFolme;

    if-eqz v0, :cond_0

    invoke-interface {v0}, Lmiuix/animation/IFolme;->state()Lmiuix/animation/IStateStyle;

    move-result-object v0

    invoke-interface {v0}, Lmiuix/animation/ICancelableStyle;->cancel()V

    :cond_0
    iget-object v0, p0, Lmiuix/appcompat/widget/Button;->mInitAnimatorTask:Ljava/lang/Runnable;

    invoke-virtual {p0, v0}, Landroid/widget/Button;->removeCallbacks(Ljava/lang/Runnable;)Z

    return-void
.end method""",
        'replacement': """.method protected onDetachedFromWindow()V
    .registers 2

    goto :goto_4

    nop

    :goto_0
    if-nez v0, :cond_0

    goto :goto_7

    :cond_0
    goto :goto_5

    nop

    :goto_1
    return-void

    :goto_2
    iget-object v0, p0, Lmiuix/appcompat/widget/Button;->mInitAnimatorTask:Ljava/lang/Runnable;

    goto :goto_8

    nop

    :goto_3
    iget-object v0, p0, Lmiuix/appcompat/widget/Button;->mFolmeAnimator:Lmiuix/animation/IFolme;

    goto :goto_0

    nop

    :goto_4
    invoke-super {p0}, Landroid/widget/Button;->onDetachedFromWindow()V

    goto :goto_3

    nop

    :goto_5
    invoke-interface {v0}, Lmiuix/animation/IFolme;->state()Lmiuix/animation/IStateStyle;

    move-result-object v0

    goto :goto_6

    nop

    :goto_6
    invoke-interface {v0}, Lmiuix/animation/ICancelableStyle;->cancel()V

    :goto_7
    goto :goto_2

    nop

    :goto_8
    invoke-virtual {p0, v0}, Landroid/widget/Button;->removeCallbacks(Ljava/lang/Runnable;)Z

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_widget_Button__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['invoke-super {p0, p1, p2}, Landroid/widget/Button;->onMeasure(II)V', 'invoke-virtual {p0}, Landroid/widget/Button;->getMaxWidth()I', 'invoke-virtual {p0}, Landroid/widget/Button;->getMeasuredWidth()I', 'invoke-static {p1, p2}, Ljava/lang/Math;->min(II)I', 'invoke-virtual {p0}, Landroid/widget/Button;->getMeasuredHeight()I', 'invoke-virtual {p0, p1, p2}, Landroid/widget/Button;->setMeasuredDimension(II)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 3

    invoke-super {p0, p1, p2}, Landroid/widget/Button;->onMeasure(II)V

    invoke-virtual {p0}, Landroid/widget/Button;->getMaxWidth()I

    move-result p1

    invoke-virtual {p0}, Landroid/widget/Button;->getMeasuredWidth()I

    move-result p2

    invoke-static {p1, p2}, Ljava/lang/Math;->min(II)I

    move-result p1

    invoke-virtual {p0}, Landroid/widget/Button;->getMeasuredHeight()I

    move-result p2

    invoke-virtual {p0, p1, p2}, Landroid/widget/Button;->setMeasuredDimension(II)V

    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 3

    goto :goto_4

    nop

    :goto_0
    invoke-virtual {p0, p1, p2}, Landroid/widget/Button;->setMeasuredDimension(II)V

    goto :goto_2

    nop

    :goto_1
    invoke-virtual {p0}, Landroid/widget/Button;->getMeasuredHeight()I

    move-result p2

    goto :goto_0

    nop

    :goto_2
    return-void

    :goto_3
    invoke-virtual {p0}, Landroid/widget/Button;->getMeasuredWidth()I

    move-result p2

    goto :goto_5

    nop

    :goto_4
    invoke-super {p0, p1, p2}, Landroid/widget/Button;->onMeasure(II)V

    goto :goto_6

    nop

    :goto_5
    invoke-static {p1, p2}, Ljava/lang/Math;->min(II)I

    move-result p1

    goto :goto_1

    nop

    :goto_6
    invoke-virtual {p0}, Landroid/widget/Button;->getMaxWidth()I

    move-result p1

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
