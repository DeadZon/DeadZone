TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/popupwidget/internal/widget/ArrowPopupView.smali'
CLASS_FALLBACK_NAMES = ['ArrowPopupView.smali']
CLASS_ANCHORS = ['.super Landroid/widget/FrameLayout;', '.implements Landroid/view/View$OnTouchListener;']

PATCHES = [
    {
        'id': 'miuix_popupwidget_internal_widget_ArrowPopupView__onConfigurationChanged',
        'method': '.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V',
        'method_name': 'onConfigurationChanged',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/widget/FrameLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V', 'invoke-virtual {p0}, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->getContentView()Landroid/view/View;', 'if-eqz p1, :cond_0', 'new-instance v0, Lmiuix/popupwidget/internal/widget/ArrowPopupView$6;', 'invoke-direct {v0, p0, p1}, Lmiuix/popupwidget/internal/widget/ArrowPopupView$6;-><init>(Lmiuix/popupwidget/internal/widget/ArrowPopupView;Landroid/view/View;)V', 'invoke-virtual {p1, v0}, Landroid/view/View;->post(Ljava/lang/Runnable;)Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 3

    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    invoke-virtual {p0}, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->getContentView()Landroid/view/View;

    move-result-object p1

    if-eqz p1, :cond_0

    new-instance v0, Lmiuix/popupwidget/internal/widget/ArrowPopupView$6;

    invoke-direct {v0, p0, p1}, Lmiuix/popupwidget/internal/widget/ArrowPopupView$6;-><init>(Lmiuix/popupwidget/internal/widget/ArrowPopupView;Landroid/view/View;)V

    invoke-virtual {p1, v0}, Landroid/view/View;->post(Ljava/lang/Runnable;)Z

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 3

    goto :goto_1

    nop

    :goto_0
    if-nez p1, :cond_0

    goto :goto_7

    :cond_0
    goto :goto_4

    nop

    :goto_1
    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    goto :goto_3

    nop

    :goto_2
    invoke-direct {v0, p0, p1}, Lmiuix/popupwidget/internal/widget/ArrowPopupView$6;-><init>(Lmiuix/popupwidget/internal/widget/ArrowPopupView;Landroid/view/View;)V

    goto :goto_6

    nop

    :goto_3
    invoke-virtual {p0}, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->getContentView()Landroid/view/View;

    move-result-object p1

    goto :goto_0

    nop

    :goto_4
    new-instance v0, Lmiuix/popupwidget/internal/widget/ArrowPopupView$6;

    goto :goto_2

    nop

    :goto_5
    return-void

    :goto_6
    invoke-virtual {p1, v0}, Landroid/view/View;->post(Ljava/lang/Runnable;)Z

    :goto_7
    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_popupwidget_internal_widget_ArrowPopupView__onDetachedFromWindow',
        'method': '.method protected onDetachedFromWindow()V',
        'method_name': 'onDetachedFromWindow',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/FrameLayout;->onDetachedFromWindow()V', 'iget-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mAnchor:Landroid/view/View;', 'if-eqz v0, :cond_0', 'iget-object v1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mAnchorTrackListener:Landroid/view/View$OnLayoutChangeListener;', 'invoke-virtual {v0, v1}, Landroid/view/View;->removeOnLayoutChangeListener(Landroid/view/View$OnLayoutChangeListener;)V', 'iget-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mAnchor:Landroid/view/View;', 'iget-object p0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrowLayoutTask:Ljava/lang/Runnable;', 'invoke-virtual {v0, p0}, Landroid/view/View;->removeCallbacks(Ljava/lang/Runnable;)Z'],
        'type': 'method_replace',
        'search': """.method protected onDetachedFromWindow()V
    .registers 3

    invoke-super {p0}, Landroid/widget/FrameLayout;->onDetachedFromWindow()V

    iget-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mAnchor:Landroid/view/View;

    if-eqz v0, :cond_0

    iget-object v1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mAnchorTrackListener:Landroid/view/View$OnLayoutChangeListener;

    invoke-virtual {v0, v1}, Landroid/view/View;->removeOnLayoutChangeListener(Landroid/view/View$OnLayoutChangeListener;)V

    iget-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mAnchor:Landroid/view/View;

    iget-object p0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrowLayoutTask:Ljava/lang/Runnable;

    invoke-virtual {v0, p0}, Landroid/view/View;->removeCallbacks(Ljava/lang/Runnable;)Z

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onDetachedFromWindow()V
    .registers 3

    goto :goto_3

    nop

    :goto_0
    iget-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mAnchor:Landroid/view/View;

    goto :goto_9

    nop

    :goto_1
    iget-object v1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mAnchorTrackListener:Landroid/view/View$OnLayoutChangeListener;

    goto :goto_5

    nop

    :goto_2
    return-void

    :goto_3
    invoke-super {p0}, Landroid/widget/FrameLayout;->onDetachedFromWindow()V

    goto :goto_6

    nop

    :goto_4
    if-nez v0, :cond_0

    goto :goto_8

    :cond_0
    goto :goto_1

    nop

    :goto_5
    invoke-virtual {v0, v1}, Landroid/view/View;->removeOnLayoutChangeListener(Landroid/view/View$OnLayoutChangeListener;)V

    goto :goto_0

    nop

    :goto_6
    iget-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mAnchor:Landroid/view/View;

    goto :goto_4

    nop

    :goto_7
    invoke-virtual {v0, p0}, Landroid/view/View;->removeCallbacks(Ljava/lang/Runnable;)Z

    :goto_8
    goto :goto_2

    nop

    :goto_9
    iget-object p0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrowLayoutTask:Ljava/lang/Runnable;

    goto :goto_7

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_popupwidget_internal_widget_ArrowPopupView__onDraw',
        'method': '.method protected onDraw(Landroid/graphics/Canvas;)V',
        'method_name': 'onDraw',
        'method_anchors': ['iget-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mBackground:Landroid/graphics/drawable/Drawable;', 'if-eqz v0, :cond_0', 'return-void', 'iget v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mSpaceLeft:I', 'iget-object v1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mContentFrameWrapper:Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;', 'invoke-virtual {v1}, Landroid/widget/LinearLayout;->getWidth()I', 'iget v1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mSpaceTop:I', 'iget-object v2, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mContentFrameWrapper:Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;'],
        'type': 'method_replace',
        'search': """.method protected onDraw(Landroid/graphics/Canvas;)V
    .registers 16

    iget-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mBackground:Landroid/graphics/drawable/Drawable;

    if-eqz v0, :cond_0

    return-void

    :cond_0
    iget v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mSpaceLeft:I

    iget-object v1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mContentFrameWrapper:Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;

    invoke-virtual {v1}, Landroid/widget/LinearLayout;->getWidth()I

    move-result v1

    div-int/lit8 v1, v1, 0x2

    add-int/2addr v0, v1

    iget v1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mSpaceTop:I

    iget-object v2, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mContentFrameWrapper:Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;

    invoke-virtual {v2}, Landroid/widget/LinearLayout;->getHeight()I

    move-result v2

    div-int/lit8 v2, v2, 0x2

    add-int/2addr v1, v2

    iget v2, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrowMode:I

    const/16 v3, 0x40

    const/16 v4, 0x20

    const/16 v5, 0x10

    const/16 v6, 0x8

    const/4 v7, 0x0

    const/4 v8, 0x0

    if-eq v2, v6, :cond_4

    if-eq v2, v5, :cond_3

    if-eq v2, v4, :cond_2

    if-eq v2, v3, :cond_1

    move v2, v7

    move v9, v8

    move v10, v9

    goto :goto_0

    :cond_1
    iget v2, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrowSpaceTop:I

    iget-object v9, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrow:Landroidx/appcompat/widget/AppCompatImageView;

    invoke-virtual {v9}, Landroid/widget/ImageView;->getMeasuredHeight()I

    move-result v9

    div-int/lit8 v9, v9, 0x2

    add-int/2addr v2, v9

    iget v9, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mSpaceTop:I

    sub-int v9, v2, v9

    iget-object v10, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mContentFrameWrapper:Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;

    invoke-virtual {v10}, Landroid/widget/LinearLayout;->getBottom()I

    move-result v10

    sub-int/2addr v10, v2

    const/high16 v2, 0x42b40000

    goto :goto_0

    :cond_2
    iget v2, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrowSpaceTop:I

    iget-object v9, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrow:Landroidx/appcompat/widget/AppCompatImageView;

    invoke-virtual {v9}, Landroid/widget/ImageView;->getMeasuredHeight()I

    move-result v9

    div-int/lit8 v9, v9, 0x2

    add-int/2addr v2, v9

    iget-object v9, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mContentFrameWrapper:Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;

    invoke-virtual {v9}, Landroid/widget/LinearLayout;->getBottom()I

    move-result v9

    sub-int/2addr v9, v2

    iget v10, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mSpaceTop:I

    sub-int v10, v2, v10

    const/high16 v2, -0x3d4c0000

    goto :goto_0

    :cond_3
    iget v2, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrowSpaceLeft:I

    iget-object v9, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrow:Landroidx/appcompat/widget/AppCompatImageView;

    invoke-virtual {v9}, Landroid/widget/ImageView;->getMeasuredWidth()I

    move-result v9

    div-int/lit8 v9, v9, 0x2

    add-int/2addr v2, v9

    iget-object v9, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mContentFrameWrapper:Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;

    invoke-virtual {v9}, Landroid/widget/LinearLayout;->getRight()I

    move-result v9

    sub-int/2addr v9, v2

    iget v10, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mSpaceLeft:I

    sub-int v10, v2, v10

    const/high16 v2, 0x43340000

    goto :goto_0

    :cond_4
    iget v2, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrowSpaceLeft:I

    iget-object v9, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrow:Landroidx/appcompat/widget/AppCompatImageView;

    invoke-virtual {v9}, Landroid/widget/ImageView;->getMeasuredWidth()I

    move-result v9

    div-int/lit8 v9, v9, 0x2

    add-int/2addr v2, v9

    iget v9, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mSpaceLeft:I

    sub-int v9, v2, v9

    iget-object v10, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mContentFrameWrapper:Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;

    invoke-virtual {v10}, Landroid/widget/LinearLayout;->getRight()I

    move-result v10

    sub-int/2addr v10, v2

    move v2, v7

    :goto_0
    invoke-virtual {p1}, Landroid/graphics/Canvas;->save()I

    move-result v11

    int-to-float v12, v0

    int-to-float v13, v1

    invoke-virtual {p1, v2, v12, v13}, Landroid/graphics/Canvas;->rotate(FFF)V

    iget v2, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrowMode:I

    if-eq v2, v6, :cond_7

    if-eq v2, v5, :cond_7

    if-eq v2, v4, :cond_5

    if-eq v2, v3, :cond_5

    goto :goto_5

    :cond_5
    iget-object v2, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mContentFrameWrapper:Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;

    invoke-virtual {v2}, Landroid/widget/LinearLayout;->getHeight()I

    move-result v2

    div-int/lit8 v2, v2, 0x2

    sub-int/2addr v0, v2

    int-to-float v0, v0

    iget-object v2, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mContentFrameWrapper:Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;

    invoke-virtual {v2}, Landroid/widget/LinearLayout;->getWidth()I

    move-result v2

    div-int/lit8 v2, v2, 0x2

    sub-int/2addr v1, v2

    int-to-float v1, v1

    invoke-virtual {p1, v0, v1}, Landroid/graphics/Canvas;->translate(FF)V

    iget-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mBackgroundLeft:Landroid/graphics/drawable/Drawable;

    iget-object v1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mContentFrameWrapper:Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;

    invoke-virtual {v1}, Landroid/widget/LinearLayout;->getWidth()I

    move-result v1

    invoke-virtual {v0, v8, v8, v9, v1}, Landroid/graphics/drawable/Drawable;->setBounds(IIII)V

    invoke-direct {p0}, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->isLeftMode()Z

    move-result v0

    if-eqz v0, :cond_6

    iget v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mTranslationValue:I

    :goto_1
    int-to-float v0, v0

    goto :goto_2

    :cond_6
    iget v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mTranslationValue:I

    neg-int v0, v0

    goto :goto_1

    :goto_2
    invoke-virtual {p1, v7, v0}, Landroid/graphics/Canvas;->translate(FF)V

    iget-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mBackgroundLeft:Landroid/graphics/drawable/Drawable;

    invoke-virtual {v0, p1}, Landroid/graphics/drawable/Drawable;->draw(Landroid/graphics/Canvas;)V

    int-to-float v0, v9

    invoke-virtual {p1, v0, v7}, Landroid/graphics/Canvas;->translate(FF)V

    iget-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mBackgroundRight:Landroid/graphics/drawable/Drawable;

    iget-object v1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mContentFrameWrapper:Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;

    invoke-virtual {v1}, Landroid/widget/LinearLayout;->getWidth()I

    move-result v1

    invoke-virtual {v0, v8, v8, v10, v1}, Landroid/graphics/drawable/Drawable;->setBounds(IIII)V

    iget-object p0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mBackgroundRight:Landroid/graphics/drawable/Drawable;

    invoke-virtual {p0, p1}, Landroid/graphics/drawable/Drawable;->draw(Landroid/graphics/Canvas;)V

    goto :goto_5

    :cond_7
    iget v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mSpaceLeft:I

    int-to-float v0, v0

    iget v1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mSpaceTop:I

    int-to-float v1, v1

    invoke-virtual {p1, v0, v1}, Landroid/graphics/Canvas;->translate(FF)V

    iget-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mBackgroundLeft:Landroid/graphics/drawable/Drawable;

    iget-object v1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mContentFrameWrapper:Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;

    invoke-virtual {v1}, Landroid/widget/LinearLayout;->getHeight()I

    move-result v1

    invoke-virtual {v0, v8, v8, v9, v1}, Landroid/graphics/drawable/Drawable;->setBounds(IIII)V

    invoke-direct {p0}, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->isTopMode()Z

    move-result v0

    if-eqz v0, :cond_8

    iget v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mTranslationValue:I

    :goto_3
    int-to-float v0, v0

    goto :goto_4

    :cond_8
    iget v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mTranslationValue:I

    neg-int v0, v0

    goto :goto_3

    :goto_4
    invoke-virtual {p1, v7, v0}, Landroid/graphics/Canvas;->translate(FF)V

    iget-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mBackgroundLeft:Landroid/graphics/drawable/Drawable;

    invoke-virtual {v0, p1}, Landroid/graphics/drawable/Drawable;->draw(Landroid/graphics/Canvas;)V

    int-to-float v0, v9

    invoke-virtual {p1, v0, v7}, Landroid/graphics/Canvas;->translate(FF)V

    iget-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mBackgroundRight:Landroid/graphics/drawable/Drawable;

    iget-object v1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mContentFrameWrapper:Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;

    invoke-virtual {v1}, Landroid/widget/LinearLayout;->getHeight()I

    move-result v1

    invoke-virtual {v0, v8, v8, v10, v1}, Landroid/graphics/drawable/Drawable;->setBounds(IIII)V

    iget-object p0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mBackgroundRight:Landroid/graphics/drawable/Drawable;

    invoke-virtual {p0, p1}, Landroid/graphics/drawable/Drawable;->draw(Landroid/graphics/Canvas;)V

    :goto_5
    invoke-virtual {p1, v11}, Landroid/graphics/Canvas;->restoreToCount(I)V

    return-void
.end method""",
        'replacement': """.method protected onDraw(Landroid/graphics/Canvas;)V
    .registers 16

    goto :goto_3d

    nop

    :goto_0
    div-int/lit8 v1, v1, 0x2

    goto :goto_78

    nop

    :goto_1
    invoke-direct {p0}, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->isLeftMode()Z

    move-result v0

    goto :goto_57

    nop

    :goto_2
    move v2, v7

    goto :goto_43

    nop

    :goto_3
    iget-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mBackgroundRight:Landroid/graphics/drawable/Drawable;

    goto :goto_6b

    nop

    :goto_4
    div-int/lit8 v9, v9, 0x2

    goto :goto_27

    nop

    :goto_5
    invoke-virtual {p1, v0, v1}, Landroid/graphics/Canvas;->translate(FF)V

    goto :goto_9b

    nop

    :goto_6
    invoke-virtual {v10}, Landroid/widget/LinearLayout;->getBottom()I

    move-result v10

    goto :goto_d

    nop

    :goto_7
    add-int/2addr v2, v9

    goto :goto_2b

    nop

    :goto_8
    iget v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mSpaceLeft:I

    goto :goto_6d

    nop

    :goto_9
    int-to-float v12, v0

    goto :goto_23

    nop

    :goto_a
    iget-object v9, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mContentFrameWrapper:Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;

    goto :goto_9a

    nop

    :goto_b
    sub-int v10, v2, v10

    goto :goto_16

    nop

    :goto_c
    iget v10, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mSpaceLeft:I

    goto :goto_13

    nop

    :goto_d
    sub-int/2addr v10, v2

    goto :goto_97

    nop

    :goto_e
    if-ne v2, v5, :cond_0

    goto :goto_87

    :cond_0
    goto :goto_3e

    nop

    :goto_f
    iget v1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mSpaceTop:I

    goto :goto_4d

    nop

    :goto_10
    const/16 v5, 0x10

    goto :goto_39

    nop

    :goto_11
    div-int/lit8 v9, v9, 0x2

    goto :goto_7

    nop

    :goto_12
    invoke-virtual {p1, v11}, Landroid/graphics/Canvas;->restoreToCount(I)V

    goto :goto_17

    nop

    :goto_13
    sub-int v10, v2, v10

    goto :goto_48

    nop

    :goto_14
    iget-object v9, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrow:Landroidx/appcompat/widget/AppCompatImageView;

    goto :goto_70

    nop

    :goto_15
    div-int/lit8 v9, v9, 0x2

    goto :goto_8c

    nop

    :goto_16
    const/high16 v2, -0x3d4c0000

    goto :goto_86

    nop

    :goto_17
    return-void

    :goto_18
    div-int/lit8 v2, v2, 0x2

    goto :goto_80

    nop

    :goto_19
    invoke-virtual {v9}, Landroid/widget/LinearLayout;->getBottom()I

    move-result v9

    goto :goto_36

    nop

    :goto_1a
    iget-object v9, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrow:Landroidx/appcompat/widget/AppCompatImageView;

    goto :goto_67

    nop

    :goto_1b
    iget-object p0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mBackgroundRight:Landroid/graphics/drawable/Drawable;

    goto :goto_8f

    nop

    :goto_1c
    invoke-virtual {p1, v7, v0}, Landroid/graphics/Canvas;->translate(FF)V

    goto :goto_51

    nop

    :goto_1d
    invoke-virtual {v1}, Landroid/widget/LinearLayout;->getWidth()I

    move-result v1

    goto :goto_3c

    nop

    :goto_1e
    move v10, v9

    goto :goto_20

    nop

    :goto_1f
    invoke-virtual {v9}, Landroid/widget/ImageView;->getMeasuredHeight()I

    move-result v9

    goto :goto_15

    nop

    :goto_20
    goto :goto_6a

    :goto_21
    goto :goto_65

    nop

    :goto_22
    iget-object p0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mBackgroundRight:Landroid/graphics/drawable/Drawable;

    goto :goto_4f

    nop

    :goto_23
    int-to-float v13, v1

    goto :goto_3f

    nop

    :goto_24
    invoke-virtual {p1}, Landroid/graphics/Canvas;->save()I

    move-result v11

    goto :goto_9

    nop

    :goto_25
    goto :goto_90

    :goto_26
    goto :goto_8

    nop

    :goto_27
    add-int/2addr v2, v9

    goto :goto_a

    nop

    :goto_28
    sub-int/2addr v1, v2

    goto :goto_93

    nop

    :goto_29
    invoke-virtual {v1}, Landroid/widget/LinearLayout;->getWidth()I

    move-result v1

    goto :goto_7d

    nop

    :goto_2a
    invoke-virtual {v9}, Landroid/widget/ImageView;->getMeasuredWidth()I

    move-result v9

    goto :goto_4

    nop

    :goto_2b
    iget v9, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mSpaceLeft:I

    goto :goto_59

    nop

    :goto_2c
    iget v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mTranslationValue:I

    :goto_2d
    goto :goto_85

    nop

    :goto_2e
    invoke-virtual {v0, v8, v8, v9, v1}, Landroid/graphics/drawable/Drawable;->setBounds(IIII)V

    goto :goto_58

    nop

    :goto_2f
    iget v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mTranslationValue:I

    goto :goto_37

    nop

    :goto_30
    add-int/2addr v1, v2

    goto :goto_a4

    nop

    :goto_31
    const/16 v3, 0x40

    goto :goto_73

    nop

    :goto_32
    iget v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mSpaceLeft:I

    goto :goto_8e

    nop

    :goto_33
    goto :goto_5b

    :goto_34
    goto :goto_1c

    nop

    :goto_35
    invoke-virtual {p1, v0, v7}, Landroid/graphics/Canvas;->translate(FF)V

    goto :goto_41

    nop

    :goto_36
    sub-int/2addr v9, v2

    goto :goto_72

    nop

    :goto_37
    neg-int v0, v0

    goto :goto_33

    nop

    :goto_38
    iget v2, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrowMode:I

    goto :goto_8a

    nop

    :goto_39
    const/16 v6, 0x8

    goto :goto_94

    nop

    :goto_3a
    if-ne v2, v6, :cond_1

    goto :goto_7f

    :cond_1
    goto :goto_e

    nop

    :goto_3b
    invoke-virtual {v1}, Landroid/widget/LinearLayout;->getWidth()I

    move-result v1

    goto :goto_0

    nop

    :goto_3c
    invoke-virtual {v0, v8, v8, v10, v1}, Landroid/graphics/drawable/Drawable;->setBounds(IIII)V

    goto :goto_22

    nop

    :goto_3d
    iget-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mBackground:Landroid/graphics/drawable/Drawable;

    goto :goto_74

    nop

    :goto_3e
    if-ne v2, v4, :cond_2

    goto :goto_47

    :cond_2
    goto :goto_62

    nop

    :goto_3f
    invoke-virtual {p1, v2, v12, v13}, Landroid/graphics/Canvas;->rotate(FFF)V

    goto :goto_38

    nop

    :goto_40
    iget-object v9, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mContentFrameWrapper:Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;

    goto :goto_19

    nop

    :goto_41
    iget-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mBackgroundRight:Landroid/graphics/drawable/Drawable;

    goto :goto_6f

    nop

    :goto_42
    iget v2, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrowSpaceLeft:I

    goto :goto_1a

    nop

    :goto_43
    move v9, v8

    goto :goto_1e

    nop

    :goto_44
    div-int/lit8 v9, v9, 0x2

    goto :goto_89

    nop

    :goto_45
    const/4 v8, 0x0

    goto :goto_3a

    nop

    :goto_46
    goto :goto_6a

    :goto_47
    goto :goto_88

    nop

    :goto_48
    const/high16 v2, 0x43340000

    goto :goto_7e

    nop

    :goto_49
    invoke-virtual {p1, v7, v0}, Landroid/graphics/Canvas;->translate(FF)V

    goto :goto_92

    nop

    :goto_4a
    int-to-float v1, v1

    goto :goto_5

    nop

    :goto_4b
    invoke-virtual {p1, v0, v7}, Landroid/graphics/Canvas;->translate(FF)V

    goto :goto_3

    nop

    :goto_4c
    invoke-virtual {v0, v8, v8, v10, v1}, Landroid/graphics/drawable/Drawable;->setBounds(IIII)V

    goto :goto_1b

    nop

    :goto_4d
    iget-object v2, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mContentFrameWrapper:Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;

    goto :goto_68

    nop

    :goto_4e
    iget v2, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrowSpaceLeft:I

    goto :goto_53

    nop

    :goto_4f
    invoke-virtual {p0, p1}, Landroid/graphics/drawable/Drawable;->draw(Landroid/graphics/Canvas;)V

    goto :goto_25

    nop

    :goto_50
    iget-object v1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mContentFrameWrapper:Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;

    goto :goto_75

    nop

    :goto_51
    iget-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mBackgroundLeft:Landroid/graphics/drawable/Drawable;

    goto :goto_7c

    nop

    :goto_52
    iget-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mBackgroundLeft:Landroid/graphics/drawable/Drawable;

    goto :goto_63

    nop

    :goto_53
    iget-object v9, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrow:Landroidx/appcompat/widget/AppCompatImageView;

    goto :goto_2a

    nop

    :goto_54
    iget-object v9, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrow:Landroidx/appcompat/widget/AppCompatImageView;

    goto :goto_1f

    nop

    :goto_55
    iget-object v10, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mContentFrameWrapper:Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;

    goto :goto_6

    nop

    :goto_56
    iget-object v10, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mContentFrameWrapper:Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;

    goto :goto_71

    nop

    :goto_57
    if-nez v0, :cond_3

    goto :goto_99

    :cond_3
    goto :goto_5a

    nop

    :goto_58
    invoke-direct {p0}, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->isTopMode()Z

    move-result v0

    goto :goto_5e

    nop

    :goto_59
    sub-int v9, v2, v9

    goto :goto_56

    nop

    :goto_5a
    iget v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mTranslationValue:I

    :goto_5b
    goto :goto_5d

    nop

    :goto_5c
    iget v9, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mSpaceTop:I

    goto :goto_83

    nop

    :goto_5d
    int-to-float v0, v0

    goto :goto_98

    nop

    :goto_5e
    if-nez v0, :cond_4

    goto :goto_a1

    :cond_4
    goto :goto_2c

    nop

    :goto_5f
    iget-object v2, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mContentFrameWrapper:Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;

    goto :goto_81

    nop

    :goto_60
    int-to-float v0, v9

    goto :goto_35

    nop

    :goto_61
    iget v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mTranslationValue:I

    goto :goto_66

    nop

    :goto_62
    if-ne v2, v3, :cond_5

    goto :goto_21

    :cond_5
    goto :goto_2

    nop

    :goto_63
    iget-object v1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mContentFrameWrapper:Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;

    goto :goto_29

    nop

    :goto_64
    if-ne v2, v4, :cond_6

    goto :goto_9d

    :cond_6
    goto :goto_a2

    nop

    :goto_65
    iget v2, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrowSpaceTop:I

    goto :goto_54

    nop

    :goto_66
    neg-int v0, v0

    goto :goto_9e

    nop

    :goto_67
    invoke-virtual {v9}, Landroid/widget/ImageView;->getMeasuredWidth()I

    move-result v9

    goto :goto_11

    nop

    :goto_68
    invoke-virtual {v2}, Landroid/widget/LinearLayout;->getHeight()I

    move-result v2

    goto :goto_79

    nop

    :goto_69
    move v2, v7

    :goto_6a
    goto :goto_24

    nop

    :goto_6b
    iget-object v1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mContentFrameWrapper:Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;

    goto :goto_84

    nop

    :goto_6c
    sub-int/2addr v9, v2

    goto :goto_c

    nop

    :goto_6d
    int-to-float v0, v0

    goto :goto_a3

    nop

    :goto_6e
    div-int/lit8 v2, v2, 0x2

    goto :goto_28

    nop

    :goto_6f
    iget-object v1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mContentFrameWrapper:Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;

    goto :goto_1d

    nop

    :goto_70
    invoke-virtual {v9}, Landroid/widget/ImageView;->getMeasuredHeight()I

    move-result v9

    goto :goto_44

    nop

    :goto_71
    invoke-virtual {v10}, Landroid/widget/LinearLayout;->getRight()I

    move-result v10

    goto :goto_8b

    nop

    :goto_72
    iget v10, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mSpaceTop:I

    goto :goto_b

    nop

    :goto_73
    const/16 v4, 0x20

    goto :goto_10

    nop

    :goto_74
    if-nez v0, :cond_7

    goto :goto_96

    :cond_7
    goto :goto_95

    nop

    :goto_75
    invoke-virtual {v1}, Landroid/widget/LinearLayout;->getHeight()I

    move-result v1

    goto :goto_2e

    nop

    :goto_76
    invoke-virtual {v2}, Landroid/widget/LinearLayout;->getHeight()I

    move-result v2

    goto :goto_18

    nop

    :goto_77
    int-to-float v0, v0

    goto :goto_5f

    nop

    :goto_78
    add-int/2addr v0, v1

    goto :goto_f

    nop

    :goto_79
    div-int/lit8 v2, v2, 0x2

    goto :goto_30

    nop

    :goto_7a
    iget-object v2, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mContentFrameWrapper:Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;

    goto :goto_76

    nop

    :goto_7b
    invoke-virtual {v0, p1}, Landroid/graphics/drawable/Drawable;->draw(Landroid/graphics/Canvas;)V

    goto :goto_91

    nop

    :goto_7c
    invoke-virtual {v0, p1}, Landroid/graphics/drawable/Drawable;->draw(Landroid/graphics/Canvas;)V

    goto :goto_60

    nop

    :goto_7d
    invoke-virtual {v0, v8, v8, v9, v1}, Landroid/graphics/drawable/Drawable;->setBounds(IIII)V

    goto :goto_1

    nop

    :goto_7e
    goto :goto_6a

    :goto_7f
    goto :goto_42

    nop

    :goto_80
    sub-int/2addr v0, v2

    goto :goto_77

    nop

    :goto_81
    invoke-virtual {v2}, Landroid/widget/LinearLayout;->getWidth()I

    move-result v2

    goto :goto_6e

    nop

    :goto_82
    invoke-virtual {p1, v0, v1}, Landroid/graphics/Canvas;->translate(FF)V

    goto :goto_52

    nop

    :goto_83
    sub-int v9, v2, v9

    goto :goto_55

    nop

    :goto_84
    invoke-virtual {v1}, Landroid/widget/LinearLayout;->getHeight()I

    move-result v1

    goto :goto_4c

    nop

    :goto_85
    int-to-float v0, v0

    goto :goto_a0

    nop

    :goto_86
    goto :goto_6a

    :goto_87
    goto :goto_4e

    nop

    :goto_88
    iget v2, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrowSpaceTop:I

    goto :goto_14

    nop

    :goto_89
    add-int/2addr v2, v9

    goto :goto_40

    nop

    :goto_8a
    if-ne v2, v6, :cond_8

    goto :goto_26

    :cond_8
    goto :goto_8d

    nop

    :goto_8b
    sub-int/2addr v10, v2

    goto :goto_69

    nop

    :goto_8c
    add-int/2addr v2, v9

    goto :goto_5c

    nop

    :goto_8d
    if-ne v2, v5, :cond_9

    goto :goto_26

    :cond_9
    goto :goto_64

    nop

    :goto_8e
    iget-object v1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mContentFrameWrapper:Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;

    goto :goto_3b

    nop

    :goto_8f
    invoke-virtual {p0, p1}, Landroid/graphics/drawable/Drawable;->draw(Landroid/graphics/Canvas;)V

    :goto_90
    goto :goto_12

    nop

    :goto_91
    int-to-float v0, v9

    goto :goto_4b

    nop

    :goto_92
    iget-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mBackgroundLeft:Landroid/graphics/drawable/Drawable;

    goto :goto_7b

    nop

    :goto_93
    int-to-float v1, v1

    goto :goto_82

    nop

    :goto_94
    const/4 v7, 0x0

    goto :goto_45

    nop

    :goto_95
    return-void

    :goto_96
    goto :goto_32

    nop

    :goto_97
    const/high16 v2, 0x42b40000

    goto :goto_46

    nop

    :goto_98
    goto :goto_34

    :goto_99
    goto :goto_2f

    nop

    :goto_9a
    invoke-virtual {v9}, Landroid/widget/LinearLayout;->getRight()I

    move-result v9

    goto :goto_6c

    nop

    :goto_9b
    iget-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mBackgroundLeft:Landroid/graphics/drawable/Drawable;

    goto :goto_50

    nop

    :goto_9c
    goto :goto_90

    :goto_9d
    goto :goto_7a

    nop

    :goto_9e
    goto :goto_2d

    :goto_9f
    goto :goto_49

    nop

    :goto_a0
    goto :goto_9f

    :goto_a1
    goto :goto_61

    nop

    :goto_a2
    if-ne v2, v3, :cond_a

    goto :goto_9d

    :cond_a
    goto :goto_9c

    nop

    :goto_a3
    iget v1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mSpaceTop:I

    goto :goto_4a

    nop

    :goto_a4
    iget v2, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrowMode:I

    goto :goto_31

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_popupwidget_internal_widget_ArrowPopupView__onFinishInflate',
        'method': '.method protected onFinishInflate()V',
        'method_name': 'onFinishInflate',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/FrameLayout;->onFinishInflate()V', 'sget v0, Lmiuix/popupwidget/R$id;->popup_arrow:I', 'invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;', 'check-cast v0, Landroidx/appcompat/widget/AppCompatImageView;', 'iput-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrow:Landroidx/appcompat/widget/AppCompatImageView;', 'invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;', 'check-cast v0, Landroid/widget/FrameLayout;', 'iput-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mContentFrame:Landroid/widget/FrameLayout;'],
        'type': 'method_replace',
        'search': """.method protected onFinishInflate()V
    .registers 3

    invoke-super {p0}, Landroid/widget/FrameLayout;->onFinishInflate()V

    sget v0, Lmiuix/popupwidget/R$id;->popup_arrow:I

    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroidx/appcompat/widget/AppCompatImageView;

    iput-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrow:Landroidx/appcompat/widget/AppCompatImageView;

    const v0, 0x1020002

    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/FrameLayout;

    iput-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mContentFrame:Landroid/widget/FrameLayout;

    sget v0, Lmiuix/popupwidget/R$id;->content_wrapper:I

    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;

    iput-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mContentFrameWrapper:Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;

    iget v1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrowBackgroundPaintColor:I

    invoke-virtual {v0, v1}, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->setArrowBackgroundPaintColor(I)V

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-virtual {v0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    sget v1, Lmiuix/popupwidget/R$dimen;->miuix_appcompat_arrow_popup_view_min_height:I

    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result v0

    iget-object v1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mContentFrameWrapper:Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;

    invoke-virtual {v1, v0}, Landroid/widget/LinearLayout;->setMinimumHeight(I)V

    iget-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mBackgroundLeft:Landroid/graphics/drawable/Drawable;

    if-eqz v0, :cond_0

    iget-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mBackgroundRight:Landroid/graphics/drawable/Drawable;

    if-eqz v0, :cond_0

    new-instance v0, Landroid/graphics/Rect;

    invoke-direct {v0}, Landroid/graphics/Rect;-><init>()V

    iget-object v1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mBackgroundLeft:Landroid/graphics/drawable/Drawable;

    invoke-virtual {v1, v0}, Landroid/graphics/drawable/Drawable;->getPadding(Landroid/graphics/Rect;)Z

    iget-object v1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mContentFrameWrapper:Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;

    iget v0, v0, Landroid/graphics/Rect;->top:I

    invoke-virtual {v1, v0, v0, v0, v0}, Landroid/widget/LinearLayout;->setPadding(IIII)V

    :cond_0
    sget v0, Lmiuix/popupwidget/R$id;->title_layout:I

    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/LinearLayout;

    iput-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mTitleLayout:Landroid/widget/LinearLayout;

    iget-object v1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mTitleBackground:Landroid/graphics/drawable/Drawable;

    invoke-virtual {v0, v1}, Landroid/widget/LinearLayout;->setBackground(Landroid/graphics/drawable/Drawable;)V

    const v0, 0x1020016

    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroidx/appcompat/widget/AppCompatTextView;

    iput-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mTitleText:Landroidx/appcompat/widget/AppCompatTextView;

    const v0, 0x102001a

    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroidx/appcompat/widget/AppCompatButton;

    iput-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mPositiveButton:Landroidx/appcompat/widget/AppCompatButton;

    const v0, 0x1020019

    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroidx/appcompat/widget/AppCompatButton;

    iput-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mNegativeButton:Landroidx/appcompat/widget/AppCompatButton;

    new-instance v0, Lmiuix/popupwidget/internal/widget/ArrowPopupView$WrapperOnClickListener;

    invoke-direct {v0, p0}, Lmiuix/popupwidget/internal/widget/ArrowPopupView$WrapperOnClickListener;-><init>(Lmiuix/popupwidget/internal/widget/ArrowPopupView;)V

    iput-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mPositiveClickListener:Lmiuix/popupwidget/internal/widget/ArrowPopupView$WrapperOnClickListener;

    new-instance v0, Lmiuix/popupwidget/internal/widget/ArrowPopupView$WrapperOnClickListener;

    invoke-direct {v0, p0}, Lmiuix/popupwidget/internal/widget/ArrowPopupView$WrapperOnClickListener;-><init>(Lmiuix/popupwidget/internal/widget/ArrowPopupView;)V

    iput-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mNegativeClickListener:Lmiuix/popupwidget/internal/widget/ArrowPopupView$WrapperOnClickListener;

    iget-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mPositiveButton:Landroidx/appcompat/widget/AppCompatButton;

    iget-object v1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mPositiveClickListener:Lmiuix/popupwidget/internal/widget/ArrowPopupView$WrapperOnClickListener;

    invoke-virtual {v0, v1}, Landroid/widget/Button;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    iget-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mNegativeButton:Landroidx/appcompat/widget/AppCompatButton;

    iget-object p0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mNegativeClickListener:Lmiuix/popupwidget/internal/widget/ArrowPopupView$WrapperOnClickListener;

    invoke-virtual {v0, p0}, Landroid/widget/Button;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    return-void
.end method""",
        'replacement': """.method protected onFinishInflate()V
    .registers 3

    goto :goto_39

    nop

    :goto_0
    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result v0

    goto :goto_29

    nop

    :goto_1
    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_2f

    nop

    :goto_2
    iget v0, v0, Landroid/graphics/Rect;->top:I

    goto :goto_15

    nop

    :goto_3
    iget-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mPositiveButton:Landroidx/appcompat/widget/AppCompatButton;

    goto :goto_11

    nop

    :goto_4
    iget-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mNegativeButton:Landroidx/appcompat/widget/AppCompatButton;

    goto :goto_7

    nop

    :goto_5
    iput-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mNegativeClickListener:Lmiuix/popupwidget/internal/widget/ArrowPopupView$WrapperOnClickListener;

    goto :goto_3

    nop

    :goto_6
    invoke-direct {v0, p0}, Lmiuix/popupwidget/internal/widget/ArrowPopupView$WrapperOnClickListener;-><init>(Lmiuix/popupwidget/internal/widget/ArrowPopupView;)V

    goto :goto_5

    nop

    :goto_7
    iget-object p0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mNegativeClickListener:Lmiuix/popupwidget/internal/widget/ArrowPopupView$WrapperOnClickListener;

    goto :goto_f

    nop

    :goto_8
    iget-object v1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mContentFrameWrapper:Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;

    goto :goto_2

    nop

    :goto_9
    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_36

    nop

    :goto_a
    iput-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mTitleLayout:Landroid/widget/LinearLayout;

    goto :goto_1e

    nop

    :goto_b
    const v0, 0x1020019

    goto :goto_12

    nop

    :goto_c
    new-instance v0, Lmiuix/popupwidget/internal/widget/ArrowPopupView$WrapperOnClickListener;

    goto :goto_2d

    nop

    :goto_d
    sget v0, Lmiuix/popupwidget/R$id;->content_wrapper:I

    goto :goto_1

    nop

    :goto_e
    const v0, 0x1020016

    goto :goto_18

    nop

    :goto_f
    invoke-virtual {v0, p0}, Landroid/widget/Button;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    goto :goto_1b

    nop

    :goto_10
    const v0, 0x1020002

    goto :goto_2b

    nop

    :goto_11
    iget-object v1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mPositiveClickListener:Lmiuix/popupwidget/internal/widget/ArrowPopupView$WrapperOnClickListener;

    goto :goto_31

    nop

    :goto_12
    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_30

    nop

    :goto_13
    sget v0, Lmiuix/popupwidget/R$id;->title_layout:I

    goto :goto_19

    nop

    :goto_14
    iput-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrow:Landroidx/appcompat/widget/AppCompatImageView;

    goto :goto_10

    nop

    :goto_15
    invoke-virtual {v1, v0, v0, v0, v0}, Landroid/widget/LinearLayout;->setPadding(IIII)V

    :goto_16
    goto :goto_13

    nop

    :goto_17
    sget v0, Lmiuix/popupwidget/R$id;->popup_arrow:I

    goto :goto_9

    nop

    :goto_18
    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_1f

    nop

    :goto_19
    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_2c

    nop

    :goto_1a
    if-nez v0, :cond_0

    goto :goto_16

    :cond_0
    goto :goto_3c

    nop

    :goto_1b
    return-void

    :goto_1c
    iput-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mNegativeButton:Landroidx/appcompat/widget/AppCompatButton;

    goto :goto_c

    nop

    :goto_1d
    iput-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mPositiveButton:Landroidx/appcompat/widget/AppCompatButton;

    goto :goto_b

    nop

    :goto_1e
    iget-object v1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mTitleBackground:Landroid/graphics/drawable/Drawable;

    goto :goto_24

    nop

    :goto_1f
    check-cast v0, Landroidx/appcompat/widget/AppCompatTextView;

    goto :goto_32

    nop

    :goto_20
    iget v1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrowBackgroundPaintColor:I

    goto :goto_33

    nop

    :goto_21
    invoke-virtual {v0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    goto :goto_38

    nop

    :goto_22
    invoke-virtual {v1, v0}, Landroid/widget/LinearLayout;->setMinimumHeight(I)V

    goto :goto_3d

    nop

    :goto_23
    const v0, 0x102001a

    goto :goto_3a

    nop

    :goto_24
    invoke-virtual {v0, v1}, Landroid/widget/LinearLayout;->setBackground(Landroid/graphics/drawable/Drawable;)V

    goto :goto_e

    nop

    :goto_25
    invoke-direct {v0}, Landroid/graphics/Rect;-><init>()V

    goto :goto_2a

    nop

    :goto_26
    iput-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mPositiveClickListener:Lmiuix/popupwidget/internal/widget/ArrowPopupView$WrapperOnClickListener;

    goto :goto_2e

    nop

    :goto_27
    iput-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mContentFrame:Landroid/widget/FrameLayout;

    goto :goto_d

    nop

    :goto_28
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;

    move-result-object v0

    goto :goto_21

    nop

    :goto_29
    iget-object v1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mContentFrameWrapper:Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;

    goto :goto_22

    nop

    :goto_2a
    iget-object v1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mBackgroundLeft:Landroid/graphics/drawable/Drawable;

    goto :goto_35

    nop

    :goto_2b
    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_37

    nop

    :goto_2c
    check-cast v0, Landroid/widget/LinearLayout;

    goto :goto_a

    nop

    :goto_2d
    invoke-direct {v0, p0}, Lmiuix/popupwidget/internal/widget/ArrowPopupView$WrapperOnClickListener;-><init>(Lmiuix/popupwidget/internal/widget/ArrowPopupView;)V

    goto :goto_26

    nop

    :goto_2e
    new-instance v0, Lmiuix/popupwidget/internal/widget/ArrowPopupView$WrapperOnClickListener;

    goto :goto_6

    nop

    :goto_2f
    check-cast v0, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;

    goto :goto_34

    nop

    :goto_30
    check-cast v0, Landroidx/appcompat/widget/AppCompatButton;

    goto :goto_1c

    nop

    :goto_31
    invoke-virtual {v0, v1}, Landroid/widget/Button;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    goto :goto_4

    nop

    :goto_32
    iput-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mTitleText:Landroidx/appcompat/widget/AppCompatTextView;

    goto :goto_23

    nop

    :goto_33
    invoke-virtual {v0, v1}, Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;->setArrowBackgroundPaintColor(I)V

    goto :goto_28

    nop

    :goto_34
    iput-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mContentFrameWrapper:Lmiuix/popupwidget/internal/widget/ArrowPopupContentWrapper;

    goto :goto_20

    nop

    :goto_35
    invoke-virtual {v1, v0}, Landroid/graphics/drawable/Drawable;->getPadding(Landroid/graphics/Rect;)Z

    goto :goto_8

    nop

    :goto_36
    check-cast v0, Landroidx/appcompat/widget/AppCompatImageView;

    goto :goto_14

    nop

    :goto_37
    check-cast v0, Landroid/widget/FrameLayout;

    goto :goto_27

    nop

    :goto_38
    sget v1, Lmiuix/popupwidget/R$dimen;->miuix_appcompat_arrow_popup_view_min_height:I

    goto :goto_0

    nop

    :goto_39
    invoke-super {p0}, Landroid/widget/FrameLayout;->onFinishInflate()V

    goto :goto_17

    nop

    :goto_3a
    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_3e

    nop

    :goto_3b
    new-instance v0, Landroid/graphics/Rect;

    goto :goto_25

    nop

    :goto_3c
    iget-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mBackgroundRight:Landroid/graphics/drawable/Drawable;

    goto :goto_3f

    nop

    :goto_3d
    iget-object v0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mBackgroundLeft:Landroid/graphics/drawable/Drawable;

    goto :goto_1a

    nop

    :goto_3e
    check-cast v0, Landroidx/appcompat/widget/AppCompatButton;

    goto :goto_1d

    nop

    :goto_3f
    if-nez v0, :cond_1

    goto :goto_16

    :cond_1
    goto :goto_3b

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_popupwidget_internal_widget_ArrowPopupView__onLayout',
        'method': '.method protected onLayout(ZIIII)V',
        'method_name': 'onLayout',
        'method_anchors': ['iget-object p1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mAnchor:Landroid/view/View;', 'invoke-virtual {p1}, Landroid/view/View;->isAttachedToWindow()Z', 'if-nez p1, :cond_1', 'iget-object p1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrowPopupWindow:Lmiuix/popupwidget/widget/ArrowPopupWindow;', 'invoke-virtual {p1}, Landroid/widget/PopupWindow;->isShowing()Z', 'if-eqz p1, :cond_0', 'iget-object p0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrowPopupWindow:Lmiuix/popupwidget/widget/ArrowPopupWindow;', 'invoke-virtual {p0}, Landroid/widget/PopupWindow;->dismiss()V'],
        'type': 'method_replace',
        'search': """.method protected onLayout(ZIIII)V
    .registers 6

    iget-object p1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mAnchor:Landroid/view/View;

    invoke-virtual {p1}, Landroid/view/View;->isAttachedToWindow()Z

    move-result p1

    if-nez p1, :cond_1

    iget-object p1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrowPopupWindow:Lmiuix/popupwidget/widget/ArrowPopupWindow;

    invoke-virtual {p1}, Landroid/widget/PopupWindow;->isShowing()Z

    move-result p1

    if-eqz p1, :cond_0

    iget-object p0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrowPopupWindow:Lmiuix/popupwidget/widget/ArrowPopupWindow;

    invoke-virtual {p0}, Landroid/widget/PopupWindow;->dismiss()V

    :cond_0
    return-void

    :cond_1
    iget p1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrowMode:I

    if-nez p1, :cond_2

    invoke-direct {p0}, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->adjustArrowMode()V

    :cond_2
    iget p1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrowMode:I

    invoke-direct {p0, p1}, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->updateArrowDrawable(I)V

    invoke-direct {p0}, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->arrowLayout()V

    const/4 p1, 0x1

    iput-boolean p1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mHasFirstLayout:Z

    return-void
.end method""",
        'replacement': """.method protected onLayout(ZIIII)V
    .registers 6

    goto :goto_14

    nop

    :goto_0
    if-eqz p1, :cond_0

    goto :goto_13

    :cond_0
    goto :goto_12

    nop

    :goto_1
    if-nez p1, :cond_1

    goto :goto_d

    :cond_1
    goto :goto_11

    nop

    :goto_2
    invoke-virtual {p1}, Landroid/widget/PopupWindow;->isShowing()Z

    move-result p1

    goto :goto_1

    nop

    :goto_3
    return-void

    :goto_4
    const/4 p1, 0x1

    goto :goto_e

    nop

    :goto_5
    return-void

    :goto_6
    goto :goto_b

    nop

    :goto_7
    iget-object p1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrowPopupWindow:Lmiuix/popupwidget/widget/ArrowPopupWindow;

    goto :goto_2

    nop

    :goto_8
    invoke-direct {p0, p1}, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->updateArrowDrawable(I)V

    goto :goto_9

    nop

    :goto_9
    invoke-direct {p0}, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->arrowLayout()V

    goto :goto_4

    nop

    :goto_a
    invoke-virtual {p1}, Landroid/view/View;->isAttachedToWindow()Z

    move-result p1

    goto :goto_f

    nop

    :goto_b
    iget p1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrowMode:I

    goto :goto_0

    nop

    :goto_c
    invoke-virtual {p0}, Landroid/widget/PopupWindow;->dismiss()V

    :goto_d
    goto :goto_5

    nop

    :goto_e
    iput-boolean p1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mHasFirstLayout:Z

    goto :goto_3

    nop

    :goto_f
    if-eqz p1, :cond_2

    goto :goto_6

    :cond_2
    goto :goto_7

    nop

    :goto_10
    iget p1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrowMode:I

    goto :goto_8

    nop

    :goto_11
    iget-object p0, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mArrowPopupWindow:Lmiuix/popupwidget/widget/ArrowPopupWindow;

    goto :goto_c

    nop

    :goto_12
    invoke-direct {p0}, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->adjustArrowMode()V

    :goto_13
    goto :goto_10

    nop

    :goto_14
    iget-object p1, p0, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->mAnchor:Landroid/view/View;

    goto :goto_a

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
