TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/app/widget/ActionBarMovableLayout.smali'
CLASS_FALLBACK_NAMES = ['ActionBarMovableLayout.smali']
CLASS_ANCHORS = ['.super Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;', '.field private static final TAG:Ljava/lang/String;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarMovableLayout__ensureTabScrollView',
        'method': '.method ensureTabScrollView()V',
        'method_name': 'ensureTabScrollView',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarTop:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;', 'invoke-virtual {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->getTabContainer()Landroid/view/View;', 'iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mTabScrollView:Landroid/view/View;', 'return-void'],
        'type': 'method_replace',
        'search': """.method ensureTabScrollView()V
    .registers 2

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarTop:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    invoke-virtual {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->getTabContainer()Landroid/view/View;

    move-result-object v0

    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mTabScrollView:Landroid/view/View;

    return-void
.end method""",
        'replacement': """.method ensureTabScrollView()V
    .registers 2

    goto :goto_3

    nop

    :goto_0
    return-void

    :goto_1
    invoke-virtual {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->getTabContainer()Landroid/view/View;

    move-result-object v0

    goto :goto_2

    nop

    :goto_2
    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mTabScrollView:Landroid/view/View;

    goto :goto_0

    nop

    :goto_3
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarTop:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarMovableLayout__applyTranslationY',
        'method': '.method protected applyTranslationY(F)V',
        'method_name': 'applyTranslationY',
        'method_anchors': ['invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->motionToTranslation(F)F', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentView:Landroid/view/View;', 'invoke-virtual {v0, p1}, Landroid/view/View;->setTranslationY(F)V', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->ensureTabScrollView()V', 'iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mTabScrollView:Landroid/view/View;', 'if-eqz p0, :cond_0', 'invoke-virtual {p0, p1}, Landroid/view/View;->setTranslationY(F)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected applyTranslationY(F)V
    .registers 3

    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->motionToTranslation(F)F

    move-result p1

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentView:Landroid/view/View;

    invoke-virtual {v0, p1}, Landroid/view/View;->setTranslationY(F)V

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->ensureTabScrollView()V

    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mTabScrollView:Landroid/view/View;

    if-eqz p0, :cond_0

    invoke-virtual {p0, p1}, Landroid/view/View;->setTranslationY(F)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected applyTranslationY(F)V
    .registers 3

    goto :goto_2

    nop

    :goto_0
    return-void

    :goto_1
    invoke-virtual {v0, p1}, Landroid/view/View;->setTranslationY(F)V

    goto :goto_3

    nop

    :goto_2
    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->motionToTranslation(F)F

    move-result p1

    goto :goto_4

    nop

    :goto_3
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->ensureTabScrollView()V

    goto :goto_8

    nop

    :goto_4
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentView:Landroid/view/View;

    goto :goto_1

    nop

    :goto_5
    invoke-virtual {p0, p1}, Landroid/view/View;->setTranslationY(F)V

    :goto_6
    goto :goto_0

    nop

    :goto_7
    if-nez p0, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_5

    nop

    :goto_8
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mTabScrollView:Landroid/view/View;

    goto :goto_7

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarMovableLayout__computeVerticalScrollExtent',
        'method': '.method protected computeVerticalScrollExtent()I',
        'method_name': 'computeVerticalScrollExtent',
        'method_anchors': ['return p0'],
        'type': 'method_replace',
        'search': """.method protected computeVerticalScrollExtent()I
    .registers 1

    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method protected computeVerticalScrollExtent()I
    .registers 1

    goto :goto_0

    nop

    :goto_0
    const/4 p0, 0x0

    goto :goto_1

    nop

    :goto_1
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarMovableLayout__computeVerticalScrollRange',
        'method': '.method protected computeVerticalScrollRange()I',
        'method_name': 'computeVerticalScrollRange',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->getScrollRange()I', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected computeVerticalScrollRange()I
    .registers 1

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->getScrollRange()I

    move-result p0

    return p0
.end method""",
        'replacement': """.method protected computeVerticalScrollRange()I
    .registers 1

    goto :goto_0

    nop

    :goto_0
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->getScrollRange()I

    move-result p0

    goto :goto_1

    nop

    :goto_1
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarMovableLayout__computeVerticalVelocity',
        'method': '.method protected computeVerticalVelocity()I',
        'method_name': 'computeVerticalVelocity',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mVelocityTracker:Landroid/view/VelocityTracker;', 'iget v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mMaximumVelocity:I', 'invoke-virtual {v0, v2, v1}, Landroid/view/VelocityTracker;->computeCurrentVelocity(IF)V', 'iget p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mActivePointerId:I', 'invoke-virtual {v0, p0}, Landroid/view/VelocityTracker;->getYVelocity(I)F', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected computeVerticalVelocity()I
    .registers 4

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mVelocityTracker:Landroid/view/VelocityTracker;

    iget v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mMaximumVelocity:I

    int-to-float v1, v1

    const/16 v2, 0x3e8

    invoke-virtual {v0, v2, v1}, Landroid/view/VelocityTracker;->computeCurrentVelocity(IF)V

    iget p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mActivePointerId:I

    invoke-virtual {v0, p0}, Landroid/view/VelocityTracker;->getYVelocity(I)F

    move-result p0

    float-to-int p0, p0

    return p0
.end method""",
        'replacement': """.method protected computeVerticalVelocity()I
    .registers 4

    goto :goto_1

    nop

    :goto_0
    invoke-virtual {v0, v2, v1}, Landroid/view/VelocityTracker;->computeCurrentVelocity(IF)V

    goto :goto_7

    nop

    :goto_1
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mVelocityTracker:Landroid/view/VelocityTracker;

    goto :goto_5

    nop

    :goto_2
    invoke-virtual {v0, p0}, Landroid/view/VelocityTracker;->getYVelocity(I)F

    move-result p0

    goto :goto_4

    nop

    :goto_3
    return p0

    :goto_4
    float-to-int p0, p0

    goto :goto_3

    nop

    :goto_5
    iget v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mMaximumVelocity:I

    goto :goto_6

    nop

    :goto_6
    int-to-float v1, v1

    goto :goto_8

    nop

    :goto_7
    iget p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mActivePointerId:I

    goto :goto_2

    nop

    :goto_8
    const/16 v2, 0x3e8

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarMovableLayout__fling',
        'method': '.method protected fling(I)V',
        'method_name': 'fling',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->getOverScrollDistance()I', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->getScrollRange()I', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mScroller:Lmiuix/overscroller/widget/OverScroller;', 'iget v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mMotionY:I', 'invoke-virtual/range {v0 .. v10}, Lmiuix/overscroller/widget/OverScroller;->fling(IIIIIIIIII)V', 'iput-boolean p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mFlinging:Z', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->postInvalidate()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected fling(I)V
    .registers 13

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->getOverScrollDistance()I

    move-result v10

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->getScrollRange()I

    move-result v8

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mScroller:Lmiuix/overscroller/widget/OverScroller;

    iget v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mMotionY:I

    const/4 v7, 0x0

    const/4 v9, 0x0

    const/4 v1, 0x0

    const/4 v3, 0x0

    const/4 v5, 0x0

    const/4 v6, 0x0

    move v4, p1

    invoke-virtual/range {v0 .. v10}, Lmiuix/overscroller/widget/OverScroller;->fling(IIIIIIIIII)V

    const/4 p1, 0x1

    iput-boolean p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mFlinging:Z

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->postInvalidate()V

    return-void
.end method""",
        'replacement': """.method protected fling(I)V
    .registers 13

    goto :goto_8

    nop

    :goto_0
    const/4 v6, 0x0

    goto :goto_2

    nop

    :goto_1
    iput-boolean p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mFlinging:Z

    goto :goto_3

    nop

    :goto_2
    move v4, p1

    goto :goto_e

    nop

    :goto_3
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->postInvalidate()V

    goto :goto_b

    nop

    :goto_4
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mScroller:Lmiuix/overscroller/widget/OverScroller;

    goto :goto_d

    nop

    :goto_5
    const/4 v3, 0x0

    goto :goto_f

    nop

    :goto_6
    const/4 v7, 0x0

    goto :goto_c

    nop

    :goto_7
    const/4 v1, 0x0

    goto :goto_5

    nop

    :goto_8
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->getOverScrollDistance()I

    move-result v10

    goto :goto_9

    nop

    :goto_9
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->getScrollRange()I

    move-result v8

    goto :goto_4

    nop

    :goto_a
    const/4 p1, 0x1

    goto :goto_1

    nop

    :goto_b
    return-void

    :goto_c
    const/4 v9, 0x0

    goto :goto_7

    nop

    :goto_d
    iget v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mMotionY:I

    goto :goto_6

    nop

    :goto_e
    invoke-virtual/range {v0 .. v10}, Lmiuix/overscroller/widget/OverScroller;->fling(IIIIIIIIII)V

    goto :goto_a

    nop

    :goto_f
    const/4 v5, 0x0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarMovableLayout__measureChildWithMargins',
        'method': '.method protected measureChildWithMargins(Landroid/view/View;IIII)V',
        'method_name': 'measureChildWithMargins',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentView:Landroid/view/View;', 'if-eq p1, v0, :cond_0', 'invoke-super/range {p0 .. p5}, Landroid/widget/FrameLayout;->measureChildWithMargins(Landroid/view/View;IIII)V', 'return-void', 'invoke-virtual {p1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;', 'check-cast p5, Landroid/view/ViewGroup$MarginLayoutParams;', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;', 'invoke-virtual {v0}, Landroid/view/ViewGroup;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;'],
        'type': 'method_replace',
        'search': """.method protected measureChildWithMargins(Landroid/view/View;IIII)V
    .registers 9

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentView:Landroid/view/View;

    if-eq p1, v0, :cond_0

    invoke-super/range {p0 .. p5}, Landroid/widget/FrameLayout;->measureChildWithMargins(Landroid/view/View;IIII)V

    return-void

    :cond_0
    invoke-virtual {p1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object p5

    check-cast p5, Landroid/view/ViewGroup$MarginLayoutParams;

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    invoke-virtual {v0}, Landroid/view/ViewGroup;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v0

    check-cast v0, Landroid/view/ViewGroup$MarginLayoutParams;

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingLeft()I

    move-result v1

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingRight()I

    move-result v2

    add-int/2addr v1, v2

    iget v2, p5, Landroid/view/ViewGroup$MarginLayoutParams;->leftMargin:I

    add-int/2addr v1, v2

    iget v2, p5, Landroid/view/ViewGroup$MarginLayoutParams;->rightMargin:I

    add-int/2addr v1, v2

    add-int/2addr v1, p3

    iget p3, p5, Landroid/view/ViewGroup$MarginLayoutParams;->width:I

    invoke-static {p2, v1, p3}, Landroid/widget/FrameLayout;->getChildMeasureSpec(III)I

    move-result p2

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingTop()I

    move-result p3

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingBottom()I

    move-result v1

    add-int/2addr p3, v1

    iget v1, p5, Landroid/view/ViewGroup$MarginLayoutParams;->bottomMargin:I

    add-int/2addr p3, v1

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    invoke-virtual {v1}, Landroid/view/ViewGroup;->getMeasuredHeight()I

    move-result v1

    add-int/2addr p3, v1

    iget v0, v0, Landroid/view/ViewGroup$MarginLayoutParams;->topMargin:I

    add-int/2addr p3, v0

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->getScrollRange()I

    move-result v0

    sub-int/2addr p3, v0

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->getOverScrollDistance()I

    move-result v0

    sub-int/2addr p3, v0

    iget p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mScrollStart:I

    sub-int/2addr p3, p0

    iget p0, p5, Landroid/view/ViewGroup$MarginLayoutParams;->height:I

    invoke-static {p4, p3, p0}, Landroid/widget/FrameLayout;->getChildMeasureSpec(III)I

    move-result p0

    invoke-virtual {p1, p2, p0}, Landroid/view/View;->measure(II)V

    return-void
.end method""",
        'replacement': """.method protected measureChildWithMargins(Landroid/view/View;IIII)V
    .registers 9

    goto :goto_8

    nop

    :goto_0
    sub-int/2addr p3, v0

    goto :goto_7

    nop

    :goto_1
    iget p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mScrollStart:I

    goto :goto_23

    nop

    :goto_2
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingBottom()I

    move-result v1

    goto :goto_e

    nop

    :goto_3
    check-cast p5, Landroid/view/ViewGroup$MarginLayoutParams;

    goto :goto_4

    nop

    :goto_4
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_25

    nop

    :goto_5
    return-void

    :goto_6
    goto :goto_17

    nop

    :goto_7
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->getOverScrollDistance()I

    move-result v0

    goto :goto_26

    nop

    :goto_8
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentView:Landroid/view/View;

    goto :goto_b

    nop

    :goto_9
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingLeft()I

    move-result v1

    goto :goto_1c

    nop

    :goto_a
    check-cast v0, Landroid/view/ViewGroup$MarginLayoutParams;

    goto :goto_9

    nop

    :goto_b
    if-ne p1, v0, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_1b

    nop

    :goto_c
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->getScrollRange()I

    move-result v0

    goto :goto_0

    nop

    :goto_d
    add-int/2addr p3, v1

    goto :goto_11

    nop

    :goto_e
    add-int/2addr p3, v1

    goto :goto_19

    nop

    :goto_f
    add-int/2addr p3, v0

    goto :goto_c

    nop

    :goto_10
    invoke-static {p4, p3, p0}, Landroid/widget/FrameLayout;->getChildMeasureSpec(III)I

    move-result p0

    goto :goto_1f

    nop

    :goto_11
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_14

    nop

    :goto_12
    add-int/2addr v1, v2

    goto :goto_1a

    nop

    :goto_13
    add-int/2addr v1, v2

    goto :goto_24

    nop

    :goto_14
    invoke-virtual {v1}, Landroid/view/ViewGroup;->getMeasuredHeight()I

    move-result v1

    goto :goto_21

    nop

    :goto_15
    add-int/2addr v1, v2

    goto :goto_27

    nop

    :goto_16
    iget p3, p5, Landroid/view/ViewGroup$MarginLayoutParams;->width:I

    goto :goto_20

    nop

    :goto_17
    invoke-virtual {p1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object p5

    goto :goto_3

    nop

    :goto_18
    iget p0, p5, Landroid/view/ViewGroup$MarginLayoutParams;->height:I

    goto :goto_10

    nop

    :goto_19
    iget v1, p5, Landroid/view/ViewGroup$MarginLayoutParams;->bottomMargin:I

    goto :goto_d

    nop

    :goto_1a
    add-int/2addr v1, p3

    goto :goto_16

    nop

    :goto_1b
    invoke-super/range {p0 .. p5}, Landroid/widget/FrameLayout;->measureChildWithMargins(Landroid/view/View;IIII)V

    goto :goto_5

    nop

    :goto_1c
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingRight()I

    move-result v2

    goto :goto_13

    nop

    :goto_1d
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingTop()I

    move-result p3

    goto :goto_2

    nop

    :goto_1e
    iget v0, v0, Landroid/view/ViewGroup$MarginLayoutParams;->topMargin:I

    goto :goto_f

    nop

    :goto_1f
    invoke-virtual {p1, p2, p0}, Landroid/view/View;->measure(II)V

    goto :goto_22

    nop

    :goto_20
    invoke-static {p2, v1, p3}, Landroid/widget/FrameLayout;->getChildMeasureSpec(III)I

    move-result p2

    goto :goto_1d

    nop

    :goto_21
    add-int/2addr p3, v1

    goto :goto_1e

    nop

    :goto_22
    return-void

    :goto_23
    sub-int/2addr p3, p0

    goto :goto_18

    nop

    :goto_24
    iget v2, p5, Landroid/view/ViewGroup$MarginLayoutParams;->leftMargin:I

    goto :goto_15

    nop

    :goto_25
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v0

    goto :goto_a

    nop

    :goto_26
    sub-int/2addr p3, v0

    goto :goto_1

    nop

    :goto_27
    iget v2, p5, Landroid/view/ViewGroup$MarginLayoutParams;->rightMargin:I

    goto :goto_12

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarMovableLayout__motionToTranslation',
        'method': '.method protected motionToTranslation(F)F',
        'method_name': 'motionToTranslation',
        'method_anchors': ['iget v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mOverScrollDistance:I', 'iget p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mScrollRange:I', 'iget p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mScrollStart:I', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->ensureTabScrollView()V', 'iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mTabScrollView:Landroid/view/View;', 'if-eqz p1, :cond_0', 'invoke-virtual {p1}, Landroid/view/View;->getVisibility()I', 'if-nez p1, :cond_0'],
        'type': 'method_replace',
        'search': """.method protected motionToTranslation(F)F
    .registers 3

    iget v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mOverScrollDistance:I

    neg-int v0, v0

    int-to-float v0, v0

    add-float/2addr v0, p1

    iget p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mScrollRange:I

    int-to-float p1, p1

    sub-float/2addr v0, p1

    iget p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mScrollStart:I

    int-to-float p1, p1

    sub-float/2addr v0, p1

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->ensureTabScrollView()V

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mTabScrollView:Landroid/view/View;

    if-eqz p1, :cond_0

    invoke-virtual {p1}, Landroid/view/View;->getVisibility()I

    move-result p1

    if-nez p1, :cond_0

    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mTabScrollView:Landroid/view/View;

    invoke-virtual {p0}, Landroid/view/View;->getHeight()I

    move-result p0

    int-to-float p0, p0

    sub-float/2addr v0, p0

    :cond_0
    return v0
.end method""",
        'replacement': """.method protected motionToTranslation(F)F
    .registers 3

    goto :goto_2

    nop

    :goto_0
    return v0

    :goto_1
    int-to-float p1, p1

    goto :goto_11

    nop

    :goto_2
    iget v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mOverScrollDistance:I

    goto :goto_e

    nop

    :goto_3
    int-to-float p0, p0

    goto :goto_f

    nop

    :goto_4
    iget p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mScrollStart:I

    goto :goto_1

    nop

    :goto_5
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mTabScrollView:Landroid/view/View;

    goto :goto_a

    nop

    :goto_6
    iget p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mScrollRange:I

    goto :goto_9

    nop

    :goto_7
    invoke-virtual {p0}, Landroid/view/View;->getHeight()I

    move-result p0

    goto :goto_3

    nop

    :goto_8
    if-eqz p1, :cond_0

    goto :goto_10

    :cond_0
    goto :goto_b

    nop

    :goto_9
    int-to-float p1, p1

    goto :goto_d

    nop

    :goto_a
    if-nez p1, :cond_1

    goto :goto_10

    :cond_1
    goto :goto_12

    nop

    :goto_b
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mTabScrollView:Landroid/view/View;

    goto :goto_7

    nop

    :goto_c
    add-float/2addr v0, p1

    goto :goto_6

    nop

    :goto_d
    sub-float/2addr v0, p1

    goto :goto_4

    nop

    :goto_e
    neg-int v0, v0

    goto :goto_14

    nop

    :goto_f
    sub-float/2addr v0, p0

    :goto_10
    goto :goto_0

    nop

    :goto_11
    sub-float/2addr v0, p1

    goto :goto_13

    nop

    :goto_12
    invoke-virtual {p1}, Landroid/view/View;->getVisibility()I

    move-result p1

    goto :goto_8

    nop

    :goto_13
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->ensureTabScrollView()V

    goto :goto_5

    nop

    :goto_14
    int-to-float v0, v0

    goto :goto_c

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarMovableLayout__onLayout',
        'method': '.method protected onLayout(ZIIII)V',
        'method_name': 'onLayout',
        'method_anchors': ['invoke-super/range {p0 .. p5}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->onLayout(ZIIII)V', 'iget-boolean p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mInitialMotionYSet:Z', 'if-eqz p1, :cond_1', 'invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->isTabViewVisibilityChanged()Z', 'if-eqz p1, :cond_0', 'iget-boolean p3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mInitialMotionYSet:Z', 'if-nez p3, :cond_3', 'iget p3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mInitialMotionY:I'],
        'type': 'method_replace',
        'search': """.method protected onLayout(ZIIII)V
    .registers 6

    invoke-super/range {p0 .. p5}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->onLayout(ZIIII)V

    iget-boolean p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mInitialMotionYSet:Z

    const/4 p2, 0x1

    if-eqz p1, :cond_1

    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->isTabViewVisibilityChanged()Z

    move-result p1

    if-eqz p1, :cond_0

    goto :goto_0

    :cond_0
    const/4 p1, 0x0

    goto :goto_1

    :cond_1
    :goto_0
    move p1, p2

    :goto_1
    iget-boolean p3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mInitialMotionYSet:Z

    if-nez p3, :cond_3

    iget p3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mInitialMotionY:I

    if-gez p3, :cond_2

    iget p3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mScrollRange:I

    iput p3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mInitialMotionY:I

    :cond_2
    iget p3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mInitialMotionY:I

    iput p3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mMotionY:I

    iput-boolean p2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mInitialMotionYSet:Z

    :cond_3
    if-eqz p1, :cond_4

    iget p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mMotionY:I

    int-to-float p1, p1

    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->applyTranslationY(F)V

    :cond_4
    return-void
.end method""",
        'replacement': """.method protected onLayout(ZIIII)V
    .registers 6

    goto :goto_12

    nop

    :goto_0
    iget p3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mScrollRange:I

    goto :goto_18

    nop

    :goto_1
    iput p3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mMotionY:I

    goto :goto_3

    nop

    :goto_2
    if-nez p1, :cond_0

    goto :goto_8

    :cond_0
    goto :goto_7

    nop

    :goto_3
    iput-boolean p2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mInitialMotionYSet:Z

    :goto_4
    goto :goto_5

    nop

    :goto_5
    if-nez p1, :cond_1

    goto :goto_b

    :cond_1
    goto :goto_14

    nop

    :goto_6
    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->isTabViewVisibilityChanged()Z

    move-result p1

    goto :goto_2

    nop

    :goto_7
    goto :goto_1d

    :goto_8
    goto :goto_10

    nop

    :goto_9
    if-eqz p3, :cond_2

    goto :goto_4

    :cond_2
    goto :goto_e

    nop

    :goto_a
    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->applyTranslationY(F)V

    :goto_b
    goto :goto_11

    nop

    :goto_c
    if-ltz p3, :cond_3

    goto :goto_19

    :cond_3
    goto :goto_0

    nop

    :goto_d
    int-to-float p1, p1

    goto :goto_a

    nop

    :goto_e
    iget p3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mInitialMotionY:I

    goto :goto_c

    nop

    :goto_f
    if-nez p1, :cond_4

    goto :goto_1d

    :cond_4
    goto :goto_6

    nop

    :goto_10
    const/4 p1, 0x0

    goto :goto_1c

    nop

    :goto_11
    return-void

    :goto_12
    invoke-super/range {p0 .. p5}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->onLayout(ZIIII)V

    goto :goto_1a

    nop

    :goto_13
    const/4 p2, 0x1

    goto :goto_f

    nop

    :goto_14
    iget p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mMotionY:I

    goto :goto_d

    nop

    :goto_15
    move p1, p2

    :goto_16
    goto :goto_1b

    nop

    :goto_17
    iget p3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mInitialMotionY:I

    goto :goto_1

    nop

    :goto_18
    iput p3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mInitialMotionY:I

    :goto_19
    goto :goto_17

    nop

    :goto_1a
    iget-boolean p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mInitialMotionYSet:Z

    goto :goto_13

    nop

    :goto_1b
    iget-boolean p3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mInitialMotionYSet:Z

    goto :goto_9

    nop

    :goto_1c
    goto :goto_16

    :goto_1d
    goto :goto_15

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarMovableLayout__onOverScrolled',
        'method': '.method protected onOverScrolled(IIZZ)V',
        'method_name': 'onOverScrolled',
        'method_anchors': ['invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->onScroll(F)V', 'iput p2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mMotionY:I', 'if-nez p2, :cond_0', 'if-eqz p4, :cond_0', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->computeVerticalVelocity()I', 'invoke-static {p0}, Ljava/lang/Math;->abs(I)I', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onOverScrolled(IIZZ)V
    .registers 5

    int-to-float p1, p2

    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->onScroll(F)V

    iput p2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mMotionY:I

    if-nez p2, :cond_0

    if-eqz p4, :cond_0

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->computeVerticalVelocity()I

    move-result p0

    invoke-static {p0}, Ljava/lang/Math;->abs(I)I

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onOverScrolled(IIZZ)V
    .registers 5

    goto :goto_2

    nop

    :goto_0
    invoke-static {p0}, Ljava/lang/Math;->abs(I)I

    :goto_1
    goto :goto_4

    nop

    :goto_2
    int-to-float p1, p2

    goto :goto_6

    nop

    :goto_3
    iput p2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mMotionY:I

    goto :goto_7

    nop

    :goto_4
    return-void

    :goto_5
    if-nez p4, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_8

    nop

    :goto_6
    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->onScroll(F)V

    goto :goto_3

    nop

    :goto_7
    if-eqz p2, :cond_1

    goto :goto_1

    :cond_1
    goto :goto_5

    nop

    :goto_8
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->computeVerticalVelocity()I

    move-result p0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarMovableLayout__onScroll',
        'method': '.method protected onScroll(F)V',
        'method_name': 'onScroll',
        'method_anchors': ['invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->applyTranslationY(F)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onScroll(F)V
    .registers 2

    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->applyTranslationY(F)V

    return-void
.end method""",
        'replacement': """.method protected onScroll(F)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->applyTranslationY(F)V

    goto :goto_1

    nop

    :goto_1
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarMovableLayout__onScrollBegin',
        'method': '.method protected onScrollBegin()V',
        'method_name': 'onScrollBegin',
        'method_anchors': ['return-void'],
        'type': 'method_replace',
        'search': """.method protected onScrollBegin()V
    .registers 1

    return-void
.end method""",
        'replacement': """.method protected onScrollBegin()V
    .registers 1

    goto :goto_0

    nop

    :goto_0
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarMovableLayout__onScrollEnd',
        'method': '.method protected onScrollEnd()V',
        'method_name': 'onScrollEnd',
        'method_anchors': ['iput v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mState:I', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onScrollEnd()V
    .registers 2

    const/4 v0, -0x1

    iput v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mState:I

    return-void
.end method""",
        'replacement': """.method protected onScrollEnd()V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    iput v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mState:I

    goto :goto_2

    nop

    :goto_1
    const/4 v0, -0x1

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
        'id': 'miuix_appcompat_internal_app_widget_ActionBarMovableLayout__overScrollBy',
        'method': '.method protected overScrollBy(IIIIIIIIZ)Z',
        'method_name': 'overScrollBy',
        'method_anchors': ['invoke-virtual {p0}, Landroid/widget/FrameLayout;->getOverScrollMode()I', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->computeVerticalScrollRange()I', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->computeVerticalScrollExtent()I', 'if-le p3, p5, :cond_0', 'if-eqz p1, :cond_2', 'if-ne p1, p7, :cond_1', 'if-eqz p3, :cond_1', 'if-nez p1, :cond_3'],
        'type': 'method_replace',
        'search': """.method protected overScrollBy(IIIIIIIIZ)Z
    .registers 10

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getOverScrollMode()I

    move-result p1

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->computeVerticalScrollRange()I

    move-result p3

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->computeVerticalScrollExtent()I

    move-result p5

    const/4 p7, 0x1

    const/4 p9, 0x0

    if-le p3, p5, :cond_0

    move p3, p7

    goto :goto_0

    :cond_0
    move p3, p9

    :goto_0
    if-eqz p1, :cond_2

    if-ne p1, p7, :cond_1

    if-eqz p3, :cond_1

    goto :goto_1

    :cond_1
    move p1, p9

    goto :goto_2

    :cond_2
    :goto_1
    move p1, p7

    :goto_2
    add-int/2addr p4, p2

    if-nez p1, :cond_3

    move p8, p9

    :cond_3
    add-int/2addr p8, p6

    if-le p4, p8, :cond_4

    move p4, p8

    goto :goto_3

    :cond_4
    if-gez p4, :cond_5

    move p4, p9

    goto :goto_3

    :cond_5
    move p7, p9

    :goto_3
    invoke-virtual {p0, p9, p4, p9, p7}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->onOverScrolled(IIZZ)V

    return p7
.end method""",
        'replacement': """.method protected overScrollBy(IIIIIIIIZ)Z
    .registers 10

    goto :goto_10

    nop

    :goto_0
    move p1, p7

    :goto_1
    goto :goto_12

    nop

    :goto_2
    const/4 p9, 0x0

    goto :goto_d

    nop

    :goto_3
    goto :goto_19

    :goto_4
    goto :goto_18

    nop

    :goto_5
    goto :goto_14

    :goto_6
    goto :goto_13

    nop

    :goto_7
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->computeVerticalScrollExtent()I

    move-result p5

    goto :goto_20

    nop

    :goto_8
    if-nez p3, :cond_0

    goto :goto_25

    :cond_0
    goto :goto_24

    nop

    :goto_9
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->computeVerticalScrollRange()I

    move-result p3

    goto :goto_7

    nop

    :goto_a
    if-eq p1, p7, :cond_1

    goto :goto_25

    :cond_1
    goto :goto_8

    nop

    :goto_b
    add-int/2addr p8, p6

    goto :goto_11

    nop

    :goto_c
    if-eqz p1, :cond_2

    goto :goto_f

    :cond_2
    goto :goto_e

    nop

    :goto_d
    if-gt p3, p5, :cond_3

    goto :goto_4

    :cond_3
    goto :goto_1b

    nop

    :goto_e
    move p8, p9

    :goto_f
    goto :goto_b

    nop

    :goto_10
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getOverScrollMode()I

    move-result p1

    goto :goto_9

    nop

    :goto_11
    if-gt p4, p8, :cond_4

    goto :goto_17

    :cond_4
    goto :goto_15

    nop

    :goto_12
    add-int/2addr p4, p2

    goto :goto_c

    nop

    :goto_13
    move p7, p9

    :goto_14
    goto :goto_22

    nop

    :goto_15
    move p4, p8

    goto :goto_16

    nop

    :goto_16
    goto :goto_14

    :goto_17
    goto :goto_1a

    nop

    :goto_18
    move p3, p9

    :goto_19
    goto :goto_1f

    nop

    :goto_1a
    if-ltz p4, :cond_5

    goto :goto_6

    :cond_5
    goto :goto_21

    nop

    :goto_1b
    move p3, p7

    goto :goto_3

    nop

    :goto_1c
    return p7

    :goto_1d
    goto :goto_1

    :goto_1e
    goto :goto_0

    nop

    :goto_1f
    if-nez p1, :cond_6

    goto :goto_1e

    :cond_6
    goto :goto_a

    nop

    :goto_20
    const/4 p7, 0x1

    goto :goto_2

    nop

    :goto_21
    move p4, p9

    goto :goto_5

    nop

    :goto_22
    invoke-virtual {p0, p9, p4, p9, p7}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->onOverScrolled(IIZZ)V

    goto :goto_1c

    nop

    :goto_23
    move p1, p9

    goto :goto_1d

    nop

    :goto_24
    goto :goto_1e

    :goto_25
    goto :goto_23

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarMovableLayout__shouldStartScroll',
        'method': '.method protected shouldStartScroll(Landroid/view/MotionEvent;)Z',
        'method_name': 'shouldStartScroll',
        'method_anchors': ['iget v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mActivePointerId:I', 'if-ne v0, v2, :cond_0', 'return v1', 'invoke-virtual {p1, v0}, Landroid/view/MotionEvent;->findPointerIndex(I)I', 'if-ne v0, v2, :cond_1', 'sget-object p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->TAG:Ljava/lang/String;', 'const-string p1, "invalid pointer index"', 'invoke-static {p0, p1}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;)I'],
        'type': 'method_replace',
        'search': """.method protected shouldStartScroll(Landroid/view/MotionEvent;)Z
    .registers 11

    iget v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mActivePointerId:I

    const/4 v1, 0x0

    const/4 v2, -0x1

    if-ne v0, v2, :cond_0

    return v1

    :cond_0
    invoke-virtual {p1, v0}, Landroid/view/MotionEvent;->findPointerIndex(I)I

    move-result v0

    if-ne v0, v2, :cond_1

    sget-object p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->TAG:Ljava/lang/String;

    const-string p1, "invalid pointer index"

    invoke-static {p0, p1}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;)I

    return v1

    :cond_1
    invoke-virtual {p1, v0}, Landroid/view/MotionEvent;->getX(I)F

    move-result v2

    invoke-virtual {p1, v0}, Landroid/view/MotionEvent;->getY(I)F

    move-result p1

    iget v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mLastMotionY:F

    sub-float v0, p1, v0

    float-to-int v0, v0

    invoke-static {v0}, Ljava/lang/Math;->abs(I)I

    move-result v3

    iget v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mLastMotionX:F

    sub-float v4, v2, v4

    invoke-static {v4}, Ljava/lang/Math;->abs(F)F

    move-result v4

    float-to-int v4, v4

    iget-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentView:Landroid/view/View;

    float-to-int v6, v2

    float-to-int v7, p1

    invoke-direct {p0, v5, v6, v7}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->inChild(Landroid/view/View;II)Z

    move-result v5

    iget-object v8, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mTabScrollView:Landroid/view/View;

    invoke-direct {p0, v8, v6, v7}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->inChild(Landroid/view/View;II)Z

    move-result v6

    const/4 v7, 0x1

    if-nez v5, :cond_3

    if-eqz v6, :cond_2

    goto :goto_0

    :cond_2
    move v5, v1

    goto :goto_1

    :cond_3
    :goto_0
    move v5, v7

    :goto_1
    if-eqz v5, :cond_4

    iget v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mTouchSlop:I

    if-le v3, v5, :cond_4

    if-le v3, v4, :cond_4

    iget v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mMotionY:I

    if-nez v3, :cond_5

    if-gez v0, :cond_6

    :cond_4
    move v3, v1

    goto :goto_2

    :cond_5
    if-lez v0, :cond_6

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->getOverScrollDistance()I

    :cond_6
    move v3, v7

    :goto_2
    if-eqz v3, :cond_8

    iput p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mLastMotionY:F

    iput v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mLastMotionX:F

    if-lez v0, :cond_7

    move v1, v7

    :cond_7
    iput v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mState:I

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getParent()Landroid/view/ViewParent;

    move-result-object p0

    if-eqz p0, :cond_8

    invoke-interface {p0, v7}, Landroid/view/ViewParent;->requestDisallowInterceptTouchEvent(Z)V

    :cond_8
    return v3
.end method""",
        'replacement': """.method protected shouldStartScroll(Landroid/view/MotionEvent;)Z
    .registers 11

    goto :goto_1a

    nop

    :goto_0
    iget-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentView:Landroid/view/View;

    goto :goto_2c

    nop

    :goto_1
    return v1

    :goto_2
    goto :goto_1c

    nop

    :goto_3
    invoke-virtual {p1, v0}, Landroid/view/MotionEvent;->getY(I)F

    move-result p1

    goto :goto_29

    nop

    :goto_4
    goto :goto_2b

    :goto_5
    goto :goto_d

    nop

    :goto_6
    if-gt v3, v4, :cond_0

    goto :goto_3b

    :cond_0
    goto :goto_22

    nop

    :goto_7
    if-eqz v5, :cond_1

    goto :goto_2b

    :cond_1
    goto :goto_8

    nop

    :goto_8
    if-nez v6, :cond_2

    goto :goto_5

    :cond_2
    goto :goto_4

    nop

    :goto_9
    move v3, v7

    :goto_a
    goto :goto_15

    nop

    :goto_b
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->getOverScrollDistance()I

    :goto_c
    goto :goto_9

    nop

    :goto_d
    move v5, v1

    goto :goto_2a

    nop

    :goto_e
    if-eq v0, v2, :cond_3

    goto :goto_11

    :cond_3
    goto :goto_10

    nop

    :goto_f
    invoke-direct {p0, v5, v6, v7}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->inChild(Landroid/view/View;II)Z

    move-result v5

    goto :goto_19

    nop

    :goto_10
    return v1

    :goto_11
    goto :goto_1d

    nop

    :goto_12
    sub-float v4, v2, v4

    goto :goto_30

    nop

    :goto_13
    float-to-int v0, v0

    goto :goto_14

    nop

    :goto_14
    invoke-static {v0}, Ljava/lang/Math;->abs(I)I

    move-result v3

    goto :goto_16

    nop

    :goto_15
    if-nez v3, :cond_4

    goto :goto_21

    :cond_4
    goto :goto_31

    nop

    :goto_16
    iget v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mLastMotionX:F

    goto :goto_12

    nop

    :goto_17
    const/4 v7, 0x1

    goto :goto_7

    nop

    :goto_18
    iput v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mState:I

    goto :goto_28

    nop

    :goto_19
    iget-object v8, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mTabScrollView:Landroid/view/View;

    goto :goto_38

    nop

    :goto_1a
    iget v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mActivePointerId:I

    goto :goto_3d

    nop

    :goto_1b
    if-gtz v0, :cond_5

    goto :goto_42

    :cond_5
    goto :goto_41

    nop

    :goto_1c
    invoke-virtual {p1, v0}, Landroid/view/MotionEvent;->getX(I)F

    move-result v2

    goto :goto_3

    nop

    :goto_1d
    invoke-virtual {p1, v0}, Landroid/view/MotionEvent;->findPointerIndex(I)I

    move-result v0

    goto :goto_23

    nop

    :goto_1e
    goto :goto_a

    :goto_1f
    goto :goto_40

    nop

    :goto_20
    invoke-interface {p0, v7}, Landroid/view/ViewParent;->requestDisallowInterceptTouchEvent(Z)V

    :goto_21
    goto :goto_2d

    nop

    :goto_22
    iget v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mMotionY:I

    goto :goto_37

    nop

    :goto_23
    if-eq v0, v2, :cond_6

    goto :goto_2

    :cond_6
    goto :goto_25

    nop

    :goto_24
    iget v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mTouchSlop:I

    goto :goto_33

    nop

    :goto_25
    sget-object p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->TAG:Ljava/lang/String;

    goto :goto_3c

    nop

    :goto_26
    if-nez v5, :cond_7

    goto :goto_3b

    :cond_7
    goto :goto_24

    nop

    :goto_27
    float-to-int v4, v4

    goto :goto_0

    nop

    :goto_28
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getParent()Landroid/view/ViewParent;

    move-result-object p0

    goto :goto_2e

    nop

    :goto_29
    iget v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mLastMotionY:F

    goto :goto_35

    nop

    :goto_2a
    goto :goto_3f

    :goto_2b
    goto :goto_3e

    nop

    :goto_2c
    float-to-int v6, v2

    goto :goto_39

    nop

    :goto_2d
    return v3

    :goto_2e
    if-nez p0, :cond_8

    goto :goto_21

    :cond_8
    goto :goto_20

    nop

    :goto_2f
    iput v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mLastMotionX:F

    goto :goto_1b

    nop

    :goto_30
    invoke-static {v4}, Ljava/lang/Math;->abs(F)F

    move-result v4

    goto :goto_27

    nop

    :goto_31
    iput p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mLastMotionY:F

    goto :goto_2f

    nop

    :goto_32
    move v3, v1

    goto :goto_1e

    nop

    :goto_33
    if-gt v3, v5, :cond_9

    goto :goto_3b

    :cond_9
    goto :goto_6

    nop

    :goto_34
    const/4 v2, -0x1

    goto :goto_e

    nop

    :goto_35
    sub-float v0, p1, v0

    goto :goto_13

    nop

    :goto_36
    invoke-static {p0, p1}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_1

    nop

    :goto_37
    if-eqz v3, :cond_a

    goto :goto_1f

    :cond_a
    goto :goto_3a

    nop

    :goto_38
    invoke-direct {p0, v8, v6, v7}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->inChild(Landroid/view/View;II)Z

    move-result v6

    goto :goto_17

    nop

    :goto_39
    float-to-int v7, p1

    goto :goto_f

    nop

    :goto_3a
    if-ltz v0, :cond_b

    goto :goto_c

    :cond_b
    :goto_3b
    goto :goto_32

    nop

    :goto_3c
    const-string p1, "invalid pointer index"

    goto :goto_36

    nop

    :goto_3d
    const/4 v1, 0x0

    goto :goto_34

    nop

    :goto_3e
    move v5, v7

    :goto_3f
    goto :goto_26

    nop

    :goto_40
    if-gtz v0, :cond_c

    goto :goto_c

    :cond_c
    goto :goto_b

    nop

    :goto_41
    move v1, v7

    :goto_42
    goto :goto_18

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarMovableLayout__springBack',
        'method': '.method protected springBack()V',
        'method_name': 'springBack',
        'method_anchors': ['iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mIsSpringBackEnabled:Z', 'if-eqz v0, :cond_1', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->getScrollRange()I', 'iget v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mMotionY:I', 'if-le v3, v1, :cond_0', 'iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mScroller:Lmiuix/overscroller/widget/OverScroller;', 'invoke-virtual/range {v1 .. v6}, Lmiuix/overscroller/widget/OverScroller;->startScroll(IIIII)V', 'invoke-static {p0}, Lmiuix/overscroller/widget/AnimationHelper;->postInvalidateOnAnimation(Landroid/view/View;)V'],
        'type': 'method_replace',
        'search': """.method protected springBack()V
    .registers 8

    iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mIsSpringBackEnabled:Z

    if-eqz v0, :cond_1

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->getScrollRange()I

    move-result v0

    iget v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mMotionY:I

    div-int/lit8 v1, v0, 0x2

    if-le v3, v1, :cond_0

    sub-int/2addr v0, v3

    :goto_0
    move v5, v0

    goto :goto_1

    :cond_0
    neg-int v0, v3

    goto :goto_0

    :goto_1
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mScroller:Lmiuix/overscroller/widget/OverScroller;

    const/4 v4, 0x0

    const/16 v6, 0x320

    const/4 v2, 0x0

    invoke-virtual/range {v1 .. v6}, Lmiuix/overscroller/widget/OverScroller;->startScroll(IIIII)V

    invoke-static {p0}, Lmiuix/overscroller/widget/AnimationHelper;->postInvalidateOnAnimation(Landroid/view/View;)V

    :cond_1
    return-void
.end method""",
        'replacement': """.method protected springBack()V
    .registers 8

    goto :goto_14

    nop

    :goto_0
    goto :goto_10

    :goto_1
    goto :goto_4

    nop

    :goto_2
    div-int/lit8 v1, v0, 0x2

    goto :goto_b

    nop

    :goto_3
    const/4 v4, 0x0

    goto :goto_12

    nop

    :goto_4
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mScroller:Lmiuix/overscroller/widget/OverScroller;

    goto :goto_3

    nop

    :goto_5
    const/4 v2, 0x0

    goto :goto_e

    nop

    :goto_6
    move v5, v0

    goto :goto_c

    nop

    :goto_7
    return-void

    :goto_8
    iget v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mMotionY:I

    goto :goto_2

    nop

    :goto_9
    invoke-static {p0}, Lmiuix/overscroller/widget/AnimationHelper;->postInvalidateOnAnimation(Landroid/view/View;)V

    :goto_a
    goto :goto_7

    nop

    :goto_b
    if-gt v3, v1, :cond_0

    goto :goto_d

    :cond_0
    goto :goto_f

    nop

    :goto_c
    goto :goto_1

    :goto_d
    goto :goto_15

    nop

    :goto_e
    invoke-virtual/range {v1 .. v6}, Lmiuix/overscroller/widget/OverScroller;->startScroll(IIIII)V

    goto :goto_9

    nop

    :goto_f
    sub-int/2addr v0, v3

    :goto_10
    goto :goto_6

    nop

    :goto_11
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->getScrollRange()I

    move-result v0

    goto :goto_8

    nop

    :goto_12
    const/16 v6, 0x320

    goto :goto_5

    nop

    :goto_13
    if-nez v0, :cond_1

    goto :goto_a

    :cond_1
    goto :goto_11

    nop

    :goto_14
    iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarMovableLayout;->mIsSpringBackEnabled:Z

    goto :goto_13

    nop

    :goto_15
    neg-int v0, v3

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
