TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView.smali'
CLASS_FALLBACK_NAMES = ['ResponsiveActionMenuView.smali']
CLASS_ANCHORS = ['.super Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_view_menu_action_ResponsiveActionMenuView__clearBackground',
        'method': '.method protected clearBackground()V',
        'method_name': 'clearBackground',
        'method_anchors': ['invoke-virtual {p0, v0}, Landroid/widget/LinearLayout;->setBackground(Landroid/graphics/drawable/Drawable;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected clearBackground()V
    .registers 2

    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Landroid/widget/LinearLayout;->setBackground(Landroid/graphics/drawable/Drawable;)V

    return-void
.end method""",
        'replacement': """.method protected clearBackground()V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    const/4 v0, 0x0

    goto :goto_2

    nop

    :goto_1
    return-void

    :goto_2
    invoke-virtual {p0, v0}, Landroid/widget/LinearLayout;->setBackground(Landroid/graphics/drawable/Drawable;)V

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_action_ResponsiveActionMenuView__onAttachedToWindow',
        'method': '.method protected onAttachedToWindow()V',
        'method_name': 'onAttachedToWindow',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/LinearLayout;->onAttachedToWindow()V', 'sget-boolean v0, Lmiuix/core/util/MiShadowUtils;->SUPPORT_MI_SHADOW:Z', 'if-eqz v0, :cond_1', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->isSuspend()Z', 'if-eqz v0, :cond_0', 'invoke-virtual {p0, p0}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->clipParent(Landroid/view/View;)V', 'iget v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mSuspendMenuMiShadowColor:I', 'iget v1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mSuspendMenuMiShadowRadiusOffsetX:F'],
        'type': 'method_replace',
        'search': """.method protected onAttachedToWindow()V
    .registers 5

    invoke-super {p0}, Landroid/widget/LinearLayout;->onAttachedToWindow()V

    sget-boolean v0, Lmiuix/core/util/MiShadowUtils;->SUPPORT_MI_SHADOW:Z

    if-eqz v0, :cond_1

    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->isSuspend()Z

    move-result v0

    if-eqz v0, :cond_0

    invoke-virtual {p0, p0}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->clipParent(Landroid/view/View;)V

    iget v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mSuspendMenuMiShadowColor:I

    iget v1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mSuspendMenuMiShadowRadiusOffsetX:F

    iget v2, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mSuspendMenuMiShadowRadiusOffsetY:F

    iget v3, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mSuspendMenuBackgroundRadius:I

    int-to-float v3, v3

    invoke-static {p0, v0, v1, v2, v3}, Lmiuix/core/util/MiShadowUtils;->setMiShadow(Landroid/view/View;IFFF)V

    return-void

    :cond_0
    invoke-direct {p0, p0}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->restoreParentClipState(Landroid/view/View;)V

    invoke-static {p0}, Lmiuix/core/util/MiShadowUtils;->clearMiShadow(Landroid/view/View;)V

    return-void

    :cond_1
    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->isSuspend()Z

    move-result v0

    if-eqz v0, :cond_2

    iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuOutShadowView:Lmiuix/appcompat/internal/view/OutDropShadowView;

    if-nez v0, :cond_3

    new-instance v0, Landroid/widget/FrameLayout$LayoutParams;

    const/4 v1, 0x0

    invoke-direct {v0, v1, v1}, Landroid/widget/FrameLayout$LayoutParams;-><init>(II)V

    new-instance v1, Lmiuix/appcompat/internal/view/OutDropShadowView;

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getContext()Landroid/content/Context;

    move-result-object v2

    invoke-direct {v1, v2}, Lmiuix/appcompat/internal/view/OutDropShadowView;-><init>(Landroid/content/Context;)V

    iput-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuOutShadowView:Lmiuix/appcompat/internal/view/OutDropShadowView;

    iget v2, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mSuspendMenuBackgroundRadius:I

    invoke-virtual {v1, v2}, Lmiuix/appcompat/internal/view/OutDropShadowView;->setShadowHostViewRadius(I)V

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getParent()Landroid/view/ViewParent;

    move-result-object v1

    check-cast v1, Landroid/view/ViewGroup;

    iget-object v2, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuOutShadowView:Lmiuix/appcompat/internal/view/OutDropShadowView;

    invoke-virtual {v1, v2, v0}, Landroid/view/ViewGroup;->addView(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    new-instance v0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView$$ExternalSyntheticLambda0;

    invoke-direct {v0, p0}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView$$ExternalSyntheticLambda0;-><init>(Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;)V

    iput-object v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mParentLayoutChangeListener:Landroid/view/View$OnLayoutChangeListener;

    invoke-virtual {v1, v0}, Landroid/view/ViewGroup;->addOnLayoutChangeListener(Landroid/view/View$OnLayoutChangeListener;)V

    return-void

    :cond_2
    iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuOutShadowView:Lmiuix/appcompat/internal/view/OutDropShadowView;

    if-eqz v0, :cond_3

    invoke-virtual {v0}, Lmiuix/appcompat/internal/view/OutDropShadowView;->onWillRemoved()V

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getParent()Landroid/view/ViewParent;

    move-result-object v0

    check-cast v0, Landroid/view/ViewGroup;

    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mParentLayoutChangeListener:Landroid/view/View$OnLayoutChangeListener;

    invoke-virtual {v0, v1}, Landroid/view/ViewGroup;->removeOnLayoutChangeListener(Landroid/view/View$OnLayoutChangeListener;)V

    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuOutShadowView:Lmiuix/appcompat/internal/view/OutDropShadowView;

    invoke-virtual {v0, v1}, Landroid/view/ViewGroup;->removeView(Landroid/view/View;)V

    const/4 v0, 0x0

    iput-object v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuOutShadowView:Lmiuix/appcompat/internal/view/OutDropShadowView;

    :cond_3
    return-void
.end method""",
        'replacement': """.method protected onAttachedToWindow()V
    .registers 5

    goto :goto_33

    nop

    :goto_0
    int-to-float v3, v3

    goto :goto_35

    nop

    :goto_1
    return-void

    :goto_2
    goto :goto_34

    nop

    :goto_3
    const/4 v1, 0x0

    goto :goto_1e

    nop

    :goto_4
    iget v2, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mSuspendMenuBackgroundRadius:I

    goto :goto_25

    nop

    :goto_5
    if-nez v0, :cond_0

    goto :goto_1b

    :cond_0
    goto :goto_23

    nop

    :goto_6
    iput-object v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mParentLayoutChangeListener:Landroid/view/View$OnLayoutChangeListener;

    goto :goto_2b

    nop

    :goto_7
    check-cast v0, Landroid/view/ViewGroup;

    goto :goto_9

    nop

    :goto_8
    iget v3, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mSuspendMenuBackgroundRadius:I

    goto :goto_0

    nop

    :goto_9
    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mParentLayoutChangeListener:Landroid/view/View$OnLayoutChangeListener;

    goto :goto_26

    nop

    :goto_a
    new-instance v0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView$$ExternalSyntheticLambda0;

    goto :goto_10

    nop

    :goto_b
    if-nez v0, :cond_1

    goto :goto_13

    :cond_1
    goto :goto_21

    nop

    :goto_c
    invoke-static {p0}, Lmiuix/core/util/MiShadowUtils;->clearMiShadow(Landroid/view/View;)V

    goto :goto_1

    nop

    :goto_d
    iput-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuOutShadowView:Lmiuix/appcompat/internal/view/OutDropShadowView;

    goto :goto_4

    nop

    :goto_e
    if-nez v0, :cond_2

    goto :goto_2

    :cond_2
    goto :goto_2e

    nop

    :goto_f
    iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuOutShadowView:Lmiuix/appcompat/internal/view/OutDropShadowView;

    goto :goto_b

    nop

    :goto_10
    invoke-direct {v0, p0}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView$$ExternalSyntheticLambda0;-><init>(Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;)V

    goto :goto_6

    nop

    :goto_11
    invoke-direct {p0, p0}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->restoreParentClipState(Landroid/view/View;)V

    goto :goto_c

    nop

    :goto_12
    iput-object v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuOutShadowView:Lmiuix/appcompat/internal/view/OutDropShadowView;

    :goto_13
    goto :goto_1c

    nop

    :goto_14
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getParent()Landroid/view/ViewParent;

    move-result-object v1

    goto :goto_1d

    nop

    :goto_15
    if-eqz v0, :cond_3

    goto :goto_13

    :cond_3
    goto :goto_31

    nop

    :goto_16
    new-instance v1, Lmiuix/appcompat/internal/view/OutDropShadowView;

    goto :goto_2c

    nop

    :goto_17
    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuOutShadowView:Lmiuix/appcompat/internal/view/OutDropShadowView;

    goto :goto_22

    nop

    :goto_18
    iget v2, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mSuspendMenuMiShadowRadiusOffsetY:F

    goto :goto_8

    nop

    :goto_19
    iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuOutShadowView:Lmiuix/appcompat/internal/view/OutDropShadowView;

    goto :goto_15

    nop

    :goto_1a
    return-void

    :goto_1b
    goto :goto_11

    nop

    :goto_1c
    return-void

    :goto_1d
    check-cast v1, Landroid/view/ViewGroup;

    goto :goto_2d

    nop

    :goto_1e
    invoke-direct {v0, v1, v1}, Landroid/widget/FrameLayout$LayoutParams;-><init>(II)V

    goto :goto_16

    nop

    :goto_1f
    iget v1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mSuspendMenuMiShadowRadiusOffsetX:F

    goto :goto_18

    nop

    :goto_20
    invoke-virtual {v1, v2, v0}, Landroid/view/ViewGroup;->addView(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    goto :goto_a

    nop

    :goto_21
    invoke-virtual {v0}, Lmiuix/appcompat/internal/view/OutDropShadowView;->onWillRemoved()V

    goto :goto_30

    nop

    :goto_22
    invoke-virtual {v0, v1}, Landroid/view/ViewGroup;->removeView(Landroid/view/View;)V

    goto :goto_28

    nop

    :goto_23
    invoke-virtual {p0, p0}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->clipParent(Landroid/view/View;)V

    goto :goto_32

    nop

    :goto_24
    invoke-direct {v1, v2}, Lmiuix/appcompat/internal/view/OutDropShadowView;-><init>(Landroid/content/Context;)V

    goto :goto_d

    nop

    :goto_25
    invoke-virtual {v1, v2}, Lmiuix/appcompat/internal/view/OutDropShadowView;->setShadowHostViewRadius(I)V

    goto :goto_14

    nop

    :goto_26
    invoke-virtual {v0, v1}, Landroid/view/ViewGroup;->removeOnLayoutChangeListener(Landroid/view/View$OnLayoutChangeListener;)V

    goto :goto_17

    nop

    :goto_27
    if-nez v0, :cond_4

    goto :goto_2a

    :cond_4
    goto :goto_19

    nop

    :goto_28
    const/4 v0, 0x0

    goto :goto_12

    nop

    :goto_29
    return-void

    :goto_2a
    goto :goto_f

    nop

    :goto_2b
    invoke-virtual {v1, v0}, Landroid/view/ViewGroup;->addOnLayoutChangeListener(Landroid/view/View$OnLayoutChangeListener;)V

    goto :goto_29

    nop

    :goto_2c
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getContext()Landroid/content/Context;

    move-result-object v2

    goto :goto_24

    nop

    :goto_2d
    iget-object v2, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuOutShadowView:Lmiuix/appcompat/internal/view/OutDropShadowView;

    goto :goto_20

    nop

    :goto_2e
    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->isSuspend()Z

    move-result v0

    goto :goto_5

    nop

    :goto_2f
    sget-boolean v0, Lmiuix/core/util/MiShadowUtils;->SUPPORT_MI_SHADOW:Z

    goto :goto_e

    nop

    :goto_30
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getParent()Landroid/view/ViewParent;

    move-result-object v0

    goto :goto_7

    nop

    :goto_31
    new-instance v0, Landroid/widget/FrameLayout$LayoutParams;

    goto :goto_3

    nop

    :goto_32
    iget v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mSuspendMenuMiShadowColor:I

    goto :goto_1f

    nop

    :goto_33
    invoke-super {p0}, Landroid/widget/LinearLayout;->onAttachedToWindow()V

    goto :goto_2f

    nop

    :goto_34
    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->isSuspend()Z

    move-result v0

    goto :goto_27

    nop

    :goto_35
    invoke-static {p0, v0, v1, v2, v3}, Lmiuix/core/util/MiShadowUtils;->setMiShadow(Landroid/view/View;IFFF)V

    goto :goto_1a

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_action_ResponsiveActionMenuView__onLayout',
        'method': '.method protected onLayout(ZIIII)V',
        'method_name': 'onLayout',
        'method_anchors': ['invoke-virtual {p0}, Landroid/widget/LinearLayout;->getMeasuredWidth()I', 'invoke-virtual {p0}, Landroid/widget/LinearLayout;->getMeasuredHeight()I', 'iget-boolean v1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mHasOnlyCustomView:Z', 'if-eqz v1, :cond_1', 'iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;', 'if-eqz v1, :cond_0', 'invoke-virtual {v1}, Landroid/view/View;->getVisibility()I', 'if-eq v1, v2, :cond_0'],
        'type': 'method_replace',
        'search': """.method protected onLayout(ZIIII)V
    .registers 18

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getMeasuredWidth()I

    move-result v6

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getMeasuredHeight()I

    move-result v7

    iget-boolean v1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mHasOnlyCustomView:Z

    const/16 v2, 0x8

    const/4 v3, 0x0

    move v4, v3

    if-eqz v1, :cond_1

    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    if-eqz v1, :cond_0

    invoke-virtual {v1}, Landroid/view/View;->getVisibility()I

    move-result v1

    if-eq v1, v2, :cond_0

    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    move v2, v4

    invoke-virtual {v1}, Landroid/view/View;->getMeasuredWidth()I

    move-result v4

    iget-object v5, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    invoke-virtual {v5}, Landroid/view/View;->getMeasuredHeight()I

    move-result v5

    move-object v0, p0

    invoke-static/range {v0 .. v5}, Lmiuix/internal/util/ViewUtils;->layoutChildView(Landroid/view/ViewGroup;Landroid/view/View;IIII)V

    :cond_0
    return-void

    :cond_1
    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    const/4 v8, 0x0

    if-eqz v1, :cond_2

    invoke-virtual {v1}, Landroid/view/View;->getVisibility()I

    move-result v1

    if-eq v1, v2, :cond_2

    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    move v2, v4

    invoke-virtual {v1}, Landroid/view/View;->getMeasuredWidth()I

    move-result v4

    iget-object v5, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    invoke-virtual {v5}, Landroid/view/View;->getMeasuredHeight()I

    move-result v5

    move-object v0, p0

    invoke-static/range {v0 .. v5}, Lmiuix/internal/util/ViewUtils;->layoutChildView(Landroid/view/ViewGroup;Landroid/view/View;IIII)V

    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    invoke-virtual {v1}, Landroid/view/View;->getMeasuredHeight()I

    move-result v1

    iget v2, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mOffSet:I

    sub-int v3, v1, v2

    if-gez v3, :cond_2

    move v3, v8

    :cond_2
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getChildCount()I

    move-result v9

    invoke-direct {p0}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->getActionMenuItemCount()I

    move-result v1

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingStart()I

    move-result v2

    sub-int v2, v6, v2

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingEnd()I

    move-result v4

    sub-int/2addr v2, v4

    iget v4, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuItemWidth:I

    mul-int/2addr v4, v1

    const/4 v10, 0x1

    sub-int/2addr v1, v10

    iget v5, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuItemGap:I

    mul-int/2addr v1, v5

    add-int/2addr v4, v1

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingStart()I

    move-result v1

    sub-int/2addr v2, v4

    div-int/lit8 v2, v2, 0x2

    add-int/2addr v1, v2

    move v2, v1

    move v11, v8

    :goto_0
    if-ge v11, v9, :cond_4

    invoke-virtual {p0, v11}, Landroid/widget/LinearLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v1

    invoke-direct {p0, v1}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->isNotActionMenuItemChild(Landroid/view/View;)Z

    move-result v4

    if-eqz v4, :cond_3

    move v5, v7

    goto :goto_1

    :cond_3
    invoke-virtual {v1}, Landroid/view/View;->getMeasuredWidth()I

    move-result v4

    add-int/2addr v4, v2

    move-object v0, p0

    move v5, v7

    invoke-static/range {v0 .. v5}, Lmiuix/internal/util/ViewUtils;->layoutChildView(Landroid/view/ViewGroup;Landroid/view/View;IIII)V

    invoke-virtual {v1}, Landroid/view/View;->getMeasuredWidth()I

    move-result v1

    iget v4, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuItemGap:I

    add-int/2addr v1, v4

    add-int/2addr v2, v1

    :goto_1
    add-int/lit8 v11, v11, 0x1

    move v7, v5

    goto :goto_0

    :cond_4
    move v5, v7

    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->isEnableBlur()Z

    move-result v1

    if-eqz v1, :cond_5

    if-lez v6, :cond_5

    if-lez v5, :cond_5

    move v8, v10

    :cond_5
    invoke-virtual {p0, v8}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->applyBlur(Z)V

    return-void
.end method""",
        'replacement': """.method protected onLayout(ZIIII)V
    .registers 18

    goto :goto_49

    nop

    :goto_0
    add-int/2addr v2, v1

    :goto_1
    goto :goto_41

    nop

    :goto_2
    invoke-virtual {v1}, Landroid/view/View;->getMeasuredWidth()I

    move-result v4

    goto :goto_28

    nop

    :goto_3
    const/16 v2, 0x8

    goto :goto_5

    nop

    :goto_4
    div-int/lit8 v2, v2, 0x2

    goto :goto_22

    nop

    :goto_5
    const/4 v3, 0x0

    goto :goto_3e

    nop

    :goto_6
    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    goto :goto_2c

    nop

    :goto_7
    if-nez v1, :cond_0

    goto :goto_d

    :cond_0
    goto :goto_39

    nop

    :goto_8
    iget-object v5, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    goto :goto_40

    nop

    :goto_9
    goto :goto_1

    :goto_a
    goto :goto_2

    nop

    :goto_b
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getChildCount()I

    move-result v9

    goto :goto_42

    nop

    :goto_c
    move v8, v10

    :goto_d
    goto :goto_55

    nop

    :goto_e
    mul-int/2addr v1, v5

    goto :goto_57

    nop

    :goto_f
    invoke-static/range {v0 .. v5}, Lmiuix/internal/util/ViewUtils;->layoutChildView(Landroid/view/ViewGroup;Landroid/view/View;IIII)V

    :goto_10
    goto :goto_17

    nop

    :goto_11
    invoke-static/range {v0 .. v5}, Lmiuix/internal/util/ViewUtils;->layoutChildView(Landroid/view/ViewGroup;Landroid/view/View;IIII)V

    goto :goto_6

    nop

    :goto_12
    move-object v0, p0

    goto :goto_11

    nop

    :goto_13
    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    goto :goto_4c

    nop

    :goto_14
    move v5, v7

    goto :goto_9

    nop

    :goto_15
    invoke-direct {p0, v1}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->isNotActionMenuItemChild(Landroid/view/View;)Z

    move-result v4

    goto :goto_48

    nop

    :goto_16
    move v2, v1

    goto :goto_3b

    nop

    :goto_17
    return-void

    :goto_18
    goto :goto_21

    nop

    :goto_19
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingEnd()I

    move-result v4

    goto :goto_25

    nop

    :goto_1a
    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    goto :goto_37

    nop

    :goto_1b
    invoke-virtual {p0, v11}, Landroid/widget/LinearLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v1

    goto :goto_15

    nop

    :goto_1c
    sub-int v3, v1, v2

    goto :goto_38

    nop

    :goto_1d
    invoke-virtual {v1}, Landroid/view/View;->getVisibility()I

    move-result v1

    goto :goto_4b

    nop

    :goto_1e
    sub-int/2addr v2, v4

    goto :goto_4

    nop

    :goto_1f
    goto :goto_3c

    :goto_20
    goto :goto_56

    nop

    :goto_21
    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    goto :goto_54

    nop

    :goto_22
    add-int/2addr v1, v2

    goto :goto_16

    nop

    :goto_23
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getMeasuredHeight()I

    move-result v7

    goto :goto_59

    nop

    :goto_24
    mul-int/2addr v4, v1

    goto :goto_2a

    nop

    :goto_25
    sub-int/2addr v2, v4

    goto :goto_3d

    nop

    :goto_26
    invoke-virtual {v1}, Landroid/view/View;->getMeasuredWidth()I

    move-result v1

    goto :goto_44

    nop

    :goto_27
    if-lt v11, v9, :cond_1

    goto :goto_20

    :cond_1
    goto :goto_1b

    nop

    :goto_28
    add-int/2addr v4, v2

    goto :goto_3a

    nop

    :goto_29
    if-nez v1, :cond_2

    goto :goto_18

    :cond_2
    goto :goto_4a

    nop

    :goto_2a
    const/4 v10, 0x1

    goto :goto_2d

    nop

    :goto_2b
    add-int/2addr v1, v4

    goto :goto_0

    nop

    :goto_2c
    invoke-virtual {v1}, Landroid/view/View;->getMeasuredHeight()I

    move-result v1

    goto :goto_33

    nop

    :goto_2d
    sub-int/2addr v1, v10

    goto :goto_53

    nop

    :goto_2e
    invoke-virtual {v1}, Landroid/view/View;->getVisibility()I

    move-result v1

    goto :goto_58

    nop

    :goto_2f
    if-nez v1, :cond_3

    goto :goto_52

    :cond_3
    goto :goto_2e

    nop

    :goto_30
    return-void

    :goto_31
    move v7, v5

    goto :goto_1f

    nop

    :goto_32
    invoke-virtual {v1}, Landroid/view/View;->getMeasuredWidth()I

    move-result v4

    goto :goto_8

    nop

    :goto_33
    iget v2, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mOffSet:I

    goto :goto_1c

    nop

    :goto_34
    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->isEnableBlur()Z

    move-result v1

    goto :goto_7

    nop

    :goto_35
    invoke-virtual {v1}, Landroid/view/View;->getMeasuredWidth()I

    move-result v4

    goto :goto_4e

    nop

    :goto_36
    move-object v0, p0

    goto :goto_f

    nop

    :goto_37
    move v2, v4

    goto :goto_32

    nop

    :goto_38
    if-ltz v3, :cond_4

    goto :goto_52

    :cond_4
    goto :goto_51

    nop

    :goto_39
    if-gtz v6, :cond_5

    goto :goto_d

    :cond_5
    goto :goto_3f

    nop

    :goto_3a
    move-object v0, p0

    goto :goto_43

    nop

    :goto_3b
    move v11, v8

    :goto_3c
    goto :goto_27

    nop

    :goto_3d
    iget v4, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuItemWidth:I

    goto :goto_24

    nop

    :goto_3e
    move v4, v3

    goto :goto_29

    nop

    :goto_3f
    if-gtz v5, :cond_6

    goto :goto_d

    :cond_6
    goto :goto_c

    nop

    :goto_40
    invoke-virtual {v5}, Landroid/view/View;->getMeasuredHeight()I

    move-result v5

    goto :goto_12

    nop

    :goto_41
    add-int/lit8 v11, v11, 0x1

    goto :goto_31

    nop

    :goto_42
    invoke-direct {p0}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->getActionMenuItemCount()I

    move-result v1

    goto :goto_47

    nop

    :goto_43
    move v5, v7

    goto :goto_46

    nop

    :goto_44
    iget v4, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuItemGap:I

    goto :goto_2b

    nop

    :goto_45
    invoke-virtual {v5}, Landroid/view/View;->getMeasuredHeight()I

    move-result v5

    goto :goto_36

    nop

    :goto_46
    invoke-static/range {v0 .. v5}, Lmiuix/internal/util/ViewUtils;->layoutChildView(Landroid/view/ViewGroup;Landroid/view/View;IIII)V

    goto :goto_26

    nop

    :goto_47
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingStart()I

    move-result v2

    goto :goto_4f

    nop

    :goto_48
    if-nez v4, :cond_7

    goto :goto_a

    :cond_7
    goto :goto_14

    nop

    :goto_49
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getMeasuredWidth()I

    move-result v6

    goto :goto_23

    nop

    :goto_4a
    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    goto :goto_50

    nop

    :goto_4b
    if-ne v1, v2, :cond_8

    goto :goto_10

    :cond_8
    goto :goto_13

    nop

    :goto_4c
    move v2, v4

    goto :goto_35

    nop

    :goto_4d
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingStart()I

    move-result v1

    goto :goto_1e

    nop

    :goto_4e
    iget-object v5, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    goto :goto_45

    nop

    :goto_4f
    sub-int v2, v6, v2

    goto :goto_19

    nop

    :goto_50
    if-nez v1, :cond_9

    goto :goto_10

    :cond_9
    goto :goto_1d

    nop

    :goto_51
    move v3, v8

    :goto_52
    goto :goto_b

    nop

    :goto_53
    iget v5, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuItemGap:I

    goto :goto_e

    nop

    :goto_54
    const/4 v8, 0x0

    goto :goto_2f

    nop

    :goto_55
    invoke-virtual {p0, v8}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->applyBlur(Z)V

    goto :goto_30

    nop

    :goto_56
    move v5, v7

    goto :goto_34

    nop

    :goto_57
    add-int/2addr v4, v1

    goto :goto_4d

    nop

    :goto_58
    if-ne v1, v2, :cond_a

    goto :goto_52

    :cond_a
    goto :goto_1a

    nop

    :goto_59
    iget-boolean v1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mHasOnlyCustomView:Z

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_action_ResponsiveActionMenuView__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['iput-boolean v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mHasOnlyCustomView:Z', 'iput-boolean v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mIsEmpty:Z', 'invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingBottom()I', 'invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingTop()I', 'invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingLeft()I', 'invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingRight()I', 'invoke-virtual {p0}, Landroid/widget/LinearLayout;->getChildCount()I', 'invoke-direct {p0}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->getActionMenuItemCount()I'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 16

    const/4 v0, 0x0

    iput-boolean v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mHasOnlyCustomView:Z

    iput-boolean v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mIsEmpty:Z

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingBottom()I

    move-result v1

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingTop()I

    move-result v2

    add-int/2addr v2, v1

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingLeft()I

    move-result v3

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingRight()I

    move-result v4

    add-int/2addr v3, v4

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getChildCount()I

    move-result v4

    invoke-direct {p0}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->getActionMenuItemCount()I

    move-result v5

    invoke-static {p1}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result p1

    const/16 v6, 0x8

    const/4 v7, 0x1

    const/high16 v8, 0x40000000

    if-eqz v4, :cond_5

    if-nez v5, :cond_0

    goto :goto_1

    :cond_0
    iget-boolean v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mSuspendEnabled:Z

    if-eqz v0, :cond_2

    iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mContext:Landroid/content/Context;

    const/high16 v4, 0x42e60000

    invoke-static {v0, v4}, Lmiuix/core/util/MiuixUIUtils;->dp2px(Landroid/content/Context;F)I

    move-result v0

    iput v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuItemWidth:I

    iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mContext:Landroid/content/Context;

    const/high16 v4, 0x42a00000

    invoke-static {v0, v4}, Lmiuix/core/util/MiuixUIUtils;->dp2px(Landroid/content/Context;F)I

    move-result v0

    const/high16 v4, -0x80000000

    invoke-static {v0, v4}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v4

    add-int/lit8 v9, v5, -0x1

    iget v10, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuItemGap:I

    mul-int/2addr v9, v10

    iget v10, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuItemWidth:I

    mul-int/2addr v10, v5

    add-int/2addr v10, v9

    iget v11, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mSuspendMenuMinMargin:I

    mul-int/lit8 v12, v11, 0x2

    sub-int v12, p1, v12

    if-lt v10, v12, :cond_1

    sub-int/2addr p1, v3

    mul-int/lit8 v11, v11, 0x2

    sub-int/2addr p1, v11

    sub-int/2addr p1, v9

    div-int/2addr p1, v5

    iput p1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuItemWidth:I

    :cond_1
    iget p1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuItemWidth:I

    invoke-static {p1, v8}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p1

    invoke-direct {p0, p1, v4, v7}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->measureActionMenuItem(IIZ)V

    invoke-direct {p0}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->getMaxChildrenTotalHeight()I

    move-result p1

    iget v4, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mSuspendItemCenterExtraUp:I

    mul-int/lit8 v4, v4, 0x2

    add-int/2addr p1, v4

    sub-int p1, v0, p1

    div-int/lit8 p1, p1, 0x2

    invoke-direct {p0, p1}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->resetActionMenuItemPaddingTop(I)V

    iput v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuItemHeight:I

    iget p1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuItemWidth:I

    mul-int/2addr p1, v5

    add-int/2addr p1, v3

    add-int/2addr p1, v9

    iget v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mSuspendMenuMinWidth:I

    invoke-static {p1, v0}, Ljava/lang/Math;->max(II)I

    move-result p1

    goto :goto_0

    :cond_2
    sub-int v0, p1, v3

    add-int/lit8 v3, v5, -0x1

    iget v4, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuItemGap:I

    mul-int/2addr v3, v4

    sub-int/2addr v0, v3

    div-int/2addr v0, v5

    iput v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuItemWidth:I

    iget v3, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mBottomMenuItemHeight:I

    add-int/2addr v3, v1

    invoke-static {v0, v8}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v0

    invoke-static {v3, v8}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v4

    iget-boolean v5, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mSuspendEnabled:Z

    invoke-direct {p0, v0, v4, v5}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->measureActionMenuItem(IIZ)V

    iput v3, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuItemHeight:I

    :goto_0
    iget v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuItemHeight:I

    add-int/2addr v0, v2

    iget-boolean v3, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mSuspendEnabled:Z

    if-nez v3, :cond_3

    sub-int/2addr v0, v1

    :cond_3
    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    if-eqz v1, :cond_4

    invoke-virtual {v1}, Landroid/view/View;->getVisibility()I

    move-result v1

    if-eq v1, v6, :cond_4

    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    invoke-virtual {v1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v1

    check-cast v1, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;

    iget-object v3, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    invoke-static {p1, v8}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v4

    iget v1, v1, Landroid/widget/LinearLayout$LayoutParams;->height:I

    invoke-static {p2, v2, v1}, Landroid/widget/LinearLayout;->getChildMeasureSpec(III)I

    move-result p2

    invoke-virtual {v3, v4, p2}, Landroid/view/View;->measure(II)V

    iget-object p2, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    invoke-direct {p0}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->getCustomViewClipBounds()Landroid/graphics/Rect;

    move-result-object v1

    invoke-virtual {p2, v1}, Landroid/view/View;->setClipBounds(Landroid/graphics/Rect;)V

    iget-object p2, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    invoke-virtual {p2}, Landroid/view/View;->getMeasuredHeight()I

    move-result p2

    add-int/2addr v0, p2

    iget p2, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mOffSet:I

    sub-int/2addr v0, p2

    :cond_4
    invoke-virtual {p0, p1, v0}, Landroid/widget/LinearLayout;->setMeasuredDimension(II)V

    invoke-direct {p0}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->keepHidden()V

    return-void

    :cond_5
    :goto_1
    iput v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuItemHeight:I

    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    if-eqz v1, :cond_9

    invoke-virtual {v1}, Landroid/view/View;->getVisibility()I

    move-result v1

    if-ne v1, v6, :cond_6

    goto :goto_4

    :cond_6
    iput-boolean v7, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mHasOnlyCustomView:Z

    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    invoke-virtual {v1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v1

    check-cast v1, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;

    iget-boolean v3, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mSuspendEnabled:Z

    if-eqz v3, :cond_7

    iget-object v3, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    iget v4, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mSuspendMenuMinMargin:I

    mul-int/lit8 v4, v4, 0x2

    sub-int/2addr p1, v4

    invoke-static {p1, v8}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p1

    iget v1, v1, Landroid/widget/LinearLayout$LayoutParams;->height:I

    invoke-static {p2, v2, v1}, Landroid/widget/LinearLayout;->getChildMeasureSpec(III)I

    move-result p2

    invoke-virtual {v3, p1, p2}, Landroid/view/View;->measure(II)V

    goto :goto_2

    :cond_7
    iget-object v3, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    invoke-static {p1, v8}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p1

    iget v1, v1, Landroid/widget/LinearLayout$LayoutParams;->height:I

    invoke-static {p2, v2, v1}, Landroid/widget/LinearLayout;->getChildMeasureSpec(III)I

    move-result p2

    invoke-virtual {v3, p1, p2}, Landroid/view/View;->measure(II)V

    :goto_2
    iget-object p1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    invoke-direct {p0}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->getCustomViewClipBounds()Landroid/graphics/Rect;

    move-result-object p2

    invoke-virtual {p1, p2}, Landroid/view/View;->setClipBounds(Landroid/graphics/Rect;)V

    iget-object p1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    invoke-virtual {p1}, Landroid/view/View;->getMeasuredWidth()I

    move-result p1

    iget-object p2, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    invoke-virtual {p2}, Landroid/view/View;->getMeasuredHeight()I

    move-result p2

    add-int/2addr p2, v2

    iget v1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mOffSet:I

    sub-int/2addr p2, v1

    if-gez p2, :cond_8

    goto :goto_3

    :cond_8
    move v0, p2

    :goto_3
    invoke-virtual {p0, p1, v0}, Landroid/widget/LinearLayout;->setMeasuredDimension(II)V

    goto :goto_5

    :cond_9
    :goto_4
    iput-boolean v7, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mIsEmpty:Z

    invoke-virtual {p0, v0, v0}, Landroid/widget/LinearLayout;->setMeasuredDimension(II)V

    :goto_5
    invoke-direct {p0}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->keepHidden()V

    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 16

    goto :goto_15

    nop

    :goto_0
    invoke-virtual {p0, p1, v0}, Landroid/widget/LinearLayout;->setMeasuredDimension(II)V

    goto :goto_1c

    nop

    :goto_1
    mul-int/lit8 v4, v4, 0x2

    goto :goto_32

    nop

    :goto_2
    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    goto :goto_55

    nop

    :goto_3
    iget v4, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mSuspendMenuMinMargin:I

    goto :goto_68

    nop

    :goto_4
    iget-object v3, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    goto :goto_2c

    nop

    :goto_5
    iput v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuItemWidth:I

    goto :goto_11

    nop

    :goto_6
    iget-boolean v5, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mSuspendEnabled:Z

    goto :goto_7c

    nop

    :goto_7
    iget-object v3, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    goto :goto_3

    nop

    :goto_8
    iget v10, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuItemGap:I

    goto :goto_9f

    nop

    :goto_9
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getChildCount()I

    move-result v4

    goto :goto_85

    nop

    :goto_a
    check-cast v1, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;

    goto :goto_78

    nop

    :goto_b
    invoke-direct {p0, p1}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->resetActionMenuItemPaddingTop(I)V

    goto :goto_4f

    nop

    :goto_c
    invoke-static {v0, v4}, Lmiuix/core/util/MiuixUIUtils;->dp2px(Landroid/content/Context;F)I

    move-result v0

    goto :goto_5

    nop

    :goto_d
    invoke-direct {p0, p1, v4, v7}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->measureActionMenuItem(IIZ)V

    goto :goto_67

    nop

    :goto_e
    if-nez v1, :cond_0

    goto :goto_1d

    :cond_0
    goto :goto_6c

    nop

    :goto_f
    check-cast v1, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;

    goto :goto_99

    nop

    :goto_10
    sub-int/2addr p1, v11

    goto :goto_37

    nop

    :goto_11
    iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mContext:Landroid/content/Context;

    goto :goto_22

    nop

    :goto_12
    goto :goto_9c

    :goto_13
    goto :goto_9b

    nop

    :goto_14
    invoke-direct {p0}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->keepHidden()V

    goto :goto_58

    nop

    :goto_15
    const/4 v0, 0x0

    goto :goto_47

    nop

    :goto_16
    iget-boolean v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mSuspendEnabled:Z

    goto :goto_5e

    nop

    :goto_17
    add-int/lit8 v3, v5, -0x1

    goto :goto_33

    nop

    :goto_18
    add-int/2addr p1, v3

    goto :goto_83

    nop

    :goto_19
    if-ltz p2, :cond_1

    goto :goto_13

    :cond_1
    goto :goto_12

    nop

    :goto_1a
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingBottom()I

    move-result v1

    goto :goto_a1

    nop

    :goto_1b
    if-nez v1, :cond_2

    goto :goto_4d

    :cond_2
    goto :goto_7e

    nop

    :goto_1c
    goto :goto_98

    :goto_1d
    goto :goto_7d

    nop

    :goto_1e
    iget-object p2, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    goto :goto_72

    nop

    :goto_1f
    invoke-static {p1}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result p1

    goto :goto_29

    nop

    :goto_20
    add-int/2addr v3, v1

    goto :goto_89

    nop

    :goto_21
    sub-int/2addr p1, v3

    goto :goto_6e

    nop

    :goto_22
    const/high16 v4, 0x42a00000

    goto :goto_5f

    nop

    :goto_23
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingRight()I

    move-result v4

    goto :goto_77

    nop

    :goto_24
    iget-object p1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    goto :goto_80

    nop

    :goto_25
    iget v3, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mBottomMenuItemHeight:I

    goto :goto_20

    nop

    :goto_26
    add-int/2addr v0, v2

    goto :goto_56

    nop

    :goto_27
    goto :goto_59

    :goto_28
    goto :goto_16

    nop

    :goto_29
    const/16 v6, 0x8

    goto :goto_36

    nop

    :goto_2a
    iput v3, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuItemHeight:I

    :goto_2b
    goto :goto_62

    nop

    :goto_2c
    invoke-static {p1, v8}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p1

    goto :goto_6a

    nop

    :goto_2d
    mul-int/2addr p1, v5

    goto :goto_18

    nop

    :goto_2e
    goto :goto_2b

    :goto_2f
    goto :goto_64

    nop

    :goto_30
    if-nez v4, :cond_3

    goto :goto_59

    :cond_3
    goto :goto_31

    nop

    :goto_31
    if-eqz v5, :cond_4

    goto :goto_28

    :cond_4
    goto :goto_27

    nop

    :goto_32
    add-int/2addr p1, v4

    goto :goto_63

    nop

    :goto_33
    iget v4, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuItemGap:I

    goto :goto_8e

    nop

    :goto_34
    invoke-virtual {p0, p1, v0}, Landroid/widget/LinearLayout;->setMeasuredDimension(II)V

    goto :goto_14

    nop

    :goto_35
    sub-int/2addr p2, v1

    goto :goto_19

    nop

    :goto_36
    const/4 v7, 0x1

    goto :goto_79

    nop

    :goto_37
    sub-int/2addr p1, v9

    goto :goto_38

    nop

    :goto_38
    div-int/2addr p1, v5

    goto :goto_9d

    nop

    :goto_39
    iput-boolean v7, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mHasOnlyCustomView:Z

    goto :goto_3c

    nop

    :goto_3a
    add-int/lit8 v9, v5, -0x1

    goto :goto_8

    nop

    :goto_3b
    sub-int/2addr p1, v4

    goto :goto_48

    nop

    :goto_3c
    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    goto :goto_41

    nop

    :goto_3d
    iget p2, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mOffSet:I

    goto :goto_4c

    nop

    :goto_3e
    const/high16 v4, -0x80000000

    goto :goto_7a

    nop

    :goto_3f
    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    goto :goto_e

    nop

    :goto_40
    invoke-direct {p0}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->keepHidden()V

    goto :goto_42

    nop

    :goto_41
    invoke-virtual {v1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v1

    goto :goto_f

    nop

    :goto_42
    return-void

    :goto_43
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingLeft()I

    move-result v3

    goto :goto_23

    nop

    :goto_44
    if-eqz v3, :cond_5

    goto :goto_5d

    :cond_5
    goto :goto_5c

    nop

    :goto_45
    invoke-static {p2, v2, v1}, Landroid/widget/LinearLayout;->getChildMeasureSpec(III)I

    move-result p2

    goto :goto_74

    nop

    :goto_46
    invoke-virtual {v3, p1, p2}, Landroid/view/View;->measure(II)V

    goto :goto_65

    nop

    :goto_47
    iput-boolean v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mHasOnlyCustomView:Z

    goto :goto_87

    nop

    :goto_48
    invoke-static {p1, v8}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p1

    goto :goto_8b

    nop

    :goto_49
    iget v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mSuspendMenuMinWidth:I

    goto :goto_91

    nop

    :goto_4a
    iget-object p2, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    goto :goto_84

    nop

    :goto_4b
    iget p1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuItemWidth:I

    goto :goto_2d

    nop

    :goto_4c
    sub-int/2addr v0, p2

    :goto_4d
    goto :goto_34

    nop

    :goto_4e
    invoke-static {p2, v2, v1}, Landroid/widget/LinearLayout;->getChildMeasureSpec(III)I

    move-result p2

    goto :goto_a3

    nop

    :goto_4f
    iput v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuItemHeight:I

    goto :goto_4b

    nop

    :goto_50
    if-eq v1, v6, :cond_6

    goto :goto_5b

    :cond_6
    goto :goto_5a

    nop

    :goto_51
    sub-int v12, p1, v12

    goto :goto_9a

    nop

    :goto_52
    add-int/2addr v2, v1

    goto :goto_43

    nop

    :goto_53
    invoke-virtual {p2, v1}, Landroid/view/View;->setClipBounds(Landroid/graphics/Rect;)V

    goto :goto_4a

    nop

    :goto_54
    iput v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuItemWidth:I

    goto :goto_25

    nop

    :goto_55
    invoke-virtual {v1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v1

    goto :goto_a

    nop

    :goto_56
    iget-boolean v3, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mSuspendEnabled:Z

    goto :goto_44

    nop

    :goto_57
    mul-int/lit8 v12, v11, 0x2

    goto :goto_51

    nop

    :goto_58
    return-void

    :goto_59
    goto :goto_88

    nop

    :goto_5a
    goto :goto_1d

    :goto_5b
    goto :goto_39

    nop

    :goto_5c
    sub-int/2addr v0, v1

    :goto_5d
    goto :goto_8a

    nop

    :goto_5e
    if-nez v0, :cond_7

    goto :goto_2f

    :cond_7
    goto :goto_70

    nop

    :goto_5f
    invoke-static {v0, v4}, Lmiuix/core/util/MiuixUIUtils;->dp2px(Landroid/content/Context;F)I

    move-result v0

    goto :goto_3e

    nop

    :goto_60
    sub-int/2addr v0, v3

    goto :goto_81

    nop

    :goto_61
    if-ne v1, v6, :cond_8

    goto :goto_4d

    :cond_8
    goto :goto_2

    nop

    :goto_62
    iget v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuItemHeight:I

    goto :goto_26

    nop

    :goto_63
    sub-int p1, v0, p1

    goto :goto_95

    nop

    :goto_64
    sub-int v0, p1, v3

    goto :goto_17

    nop

    :goto_65
    goto :goto_75

    :goto_66
    goto :goto_4

    nop

    :goto_67
    invoke-direct {p0}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->getMaxChildrenTotalHeight()I

    move-result p1

    goto :goto_73

    nop

    :goto_68
    mul-int/lit8 v4, v4, 0x2

    goto :goto_3b

    nop

    :goto_69
    iget v1, v1, Landroid/widget/LinearLayout$LayoutParams;->height:I

    goto :goto_4e

    nop

    :goto_6a
    iget v1, v1, Landroid/widget/LinearLayout$LayoutParams;->height:I

    goto :goto_45

    nop

    :goto_6b
    invoke-static {v3, v8}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v4

    goto :goto_6

    nop

    :goto_6c
    invoke-virtual {v1}, Landroid/view/View;->getVisibility()I

    move-result v1

    goto :goto_50

    nop

    :goto_6d
    invoke-static {p1, v8}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v4

    goto :goto_69

    nop

    :goto_6e
    mul-int/lit8 v11, v11, 0x2

    goto :goto_10

    nop

    :goto_6f
    invoke-virtual {p2}, Landroid/view/View;->getMeasuredHeight()I

    move-result p2

    goto :goto_7f

    nop

    :goto_70
    iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mContext:Landroid/content/Context;

    goto :goto_a0

    nop

    :goto_71
    iget v1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mOffSet:I

    goto :goto_35

    nop

    :goto_72
    invoke-direct {p0}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->getCustomViewClipBounds()Landroid/graphics/Rect;

    move-result-object v1

    goto :goto_53

    nop

    :goto_73
    iget v4, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mSuspendItemCenterExtraUp:I

    goto :goto_1

    nop

    :goto_74
    invoke-virtual {v3, p1, p2}, Landroid/view/View;->measure(II)V

    :goto_75
    goto :goto_8d

    nop

    :goto_76
    add-int/2addr v0, p2

    goto :goto_3d

    nop

    :goto_77
    add-int/2addr v3, v4

    goto :goto_9

    nop

    :goto_78
    iget-object v3, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    goto :goto_6d

    nop

    :goto_79
    const/high16 v8, 0x40000000

    goto :goto_30

    nop

    :goto_7a
    invoke-static {v0, v4}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v4

    goto :goto_3a

    nop

    :goto_7b
    invoke-direct {p0}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->getCustomViewClipBounds()Landroid/graphics/Rect;

    move-result-object p2

    goto :goto_8f

    nop

    :goto_7c
    invoke-direct {p0, v0, v4, v5}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->measureActionMenuItem(IIZ)V

    goto :goto_2a

    nop

    :goto_7d
    iput-boolean v7, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mIsEmpty:Z

    goto :goto_97

    nop

    :goto_7e
    invoke-virtual {v1}, Landroid/view/View;->getVisibility()I

    move-result v1

    goto :goto_61

    nop

    :goto_7f
    add-int/2addr p2, v2

    goto :goto_71

    nop

    :goto_80
    invoke-virtual {p1}, Landroid/view/View;->getMeasuredWidth()I

    move-result p1

    goto :goto_90

    nop

    :goto_81
    div-int/2addr v0, v5

    goto :goto_54

    nop

    :goto_82
    iget p1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuItemWidth:I

    goto :goto_8c

    nop

    :goto_83
    add-int/2addr p1, v9

    goto :goto_49

    nop

    :goto_84
    invoke-virtual {p2}, Landroid/view/View;->getMeasuredHeight()I

    move-result p2

    goto :goto_76

    nop

    :goto_85
    invoke-direct {p0}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->getActionMenuItemCount()I

    move-result v5

    goto :goto_1f

    nop

    :goto_86
    if-nez v3, :cond_9

    goto :goto_66

    :cond_9
    goto :goto_7

    nop

    :goto_87
    iput-boolean v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mIsEmpty:Z

    goto :goto_1a

    nop

    :goto_88
    iput v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuItemHeight:I

    goto :goto_3f

    nop

    :goto_89
    invoke-static {v0, v8}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v0

    goto :goto_6b

    nop

    :goto_8a
    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    goto :goto_1b

    nop

    :goto_8b
    iget v1, v1, Landroid/widget/LinearLayout$LayoutParams;->height:I

    goto :goto_92

    nop

    :goto_8c
    invoke-static {p1, v8}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p1

    goto :goto_d

    nop

    :goto_8d
    iget-object p1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    goto :goto_7b

    nop

    :goto_8e
    mul-int/2addr v3, v4

    goto :goto_60

    nop

    :goto_8f
    invoke-virtual {p1, p2}, Landroid/view/View;->setClipBounds(Landroid/graphics/Rect;)V

    goto :goto_24

    nop

    :goto_90
    iget-object p2, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mCustomView:Landroid/view/View;

    goto :goto_6f

    nop

    :goto_91
    invoke-static {p1, v0}, Ljava/lang/Math;->max(II)I

    move-result p1

    goto :goto_2e

    nop

    :goto_92
    invoke-static {p2, v2, v1}, Landroid/widget/LinearLayout;->getChildMeasureSpec(III)I

    move-result p2

    goto :goto_46

    nop

    :goto_93
    iget v10, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuItemWidth:I

    goto :goto_94

    nop

    :goto_94
    mul-int/2addr v10, v5

    goto :goto_a2

    nop

    :goto_95
    div-int/lit8 p1, p1, 0x2

    goto :goto_b

    nop

    :goto_96
    iget v11, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mSuspendMenuMinMargin:I

    goto :goto_57

    nop

    :goto_97
    invoke-virtual {p0, v0, v0}, Landroid/widget/LinearLayout;->setMeasuredDimension(II)V

    :goto_98
    goto :goto_40

    nop

    :goto_99
    iget-boolean v3, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mSuspendEnabled:Z

    goto :goto_86

    nop

    :goto_9a
    if-ge v10, v12, :cond_a

    goto :goto_9e

    :cond_a
    goto :goto_21

    nop

    :goto_9b
    move v0, p2

    :goto_9c
    goto :goto_0

    nop

    :goto_9d
    iput p1, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->mMenuItemWidth:I

    :goto_9e
    goto :goto_82

    nop

    :goto_9f
    mul-int/2addr v9, v10

    goto :goto_93

    nop

    :goto_a0
    const/high16 v4, 0x42e60000

    goto :goto_c

    nop

    :goto_a1
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getPaddingTop()I

    move-result v2

    goto :goto_52

    nop

    :goto_a2
    add-int/2addr v10, v9

    goto :goto_96

    nop

    :goto_a3
    invoke-virtual {v3, v4, p2}, Landroid/view/View;->measure(II)V

    goto :goto_1e

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_action_ResponsiveActionMenuView__onRestoreInstanceState',
        'method': '.method protected onRestoreInstanceState(Landroid/os/Parcelable;)V',
        'method_name': 'onRestoreInstanceState',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/widget/LinearLayout;->onRestoreInstanceState(Landroid/os/Parcelable;)V', 'invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->applyBlur(Z)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onRestoreInstanceState(Landroid/os/Parcelable;)V
    .registers 2

    invoke-super {p0, p1}, Landroid/widget/LinearLayout;->onRestoreInstanceState(Landroid/os/Parcelable;)V

    const/4 p1, 0x0

    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->applyBlur(Z)V

    return-void
.end method""",
        'replacement': """.method protected onRestoreInstanceState(Landroid/os/Parcelable;)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    invoke-super {p0, p1}, Landroid/widget/LinearLayout;->onRestoreInstanceState(Landroid/os/Parcelable;)V

    goto :goto_3

    nop

    :goto_2
    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->applyBlur(Z)V

    goto :goto_0

    nop

    :goto_3
    const/4 p1, 0x0

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_action_ResponsiveActionMenuView__resetBackground',
        'method': '.method protected resetBackground()V',
        'method_name': 'resetBackground',
        'method_anchors': ['invoke-direct {p0}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->updateBackground()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected resetBackground()V
    .registers 1

    invoke-direct {p0}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->updateBackground()V

    return-void
.end method""",
        'replacement': """.method protected resetBackground()V
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    invoke-direct {p0}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->updateBackground()V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
