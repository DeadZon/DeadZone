TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/app/widget/ActionBarOverlayLayout.smali'
CLASS_FALLBACK_NAMES = ['ActionBarOverlayLayout.smali']
CLASS_ANCHORS = ['.super Landroid/widget/FrameLayout;', '.implements Landroidx/core/view/NestedScrollingParent3;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarOverlayLayout__getDeviceType',
        'method': '.method getDeviceType()I',
        'method_name': 'getDeviceType',
        'method_anchors': ['iget p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mDeviceType:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method getDeviceType()I
    .registers 1

    iget p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mDeviceType:I

    return p0
.end method""",
        'replacement': """.method getDeviceType()I
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    iget p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mDeviceType:I

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarOverlayLayout__isBottomAnimating',
        'method': '.method isBottomAnimating()Z',
        'method_name': 'isBottomAnimating',
        'method_anchors': ['iget-boolean p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mAnimating:Z', 'return p0'],
        'type': 'method_replace',
        'search': """.method isBottomAnimating()Z
    .registers 1

    iget-boolean p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mAnimating:Z

    return p0
.end method""",
        'replacement': """.method isBottomAnimating()Z
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    iget-boolean p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mAnimating:Z

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarOverlayLayout__dispatchDraw',
        'method': '.method protected dispatchDraw(Landroid/graphics/Canvas;)V',
        'method_name': 'dispatchDraw',
        'method_anchors': ['iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentAutoFitSystemWindow:Z', 'if-eqz v0, :cond_0', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentHeaderBackground:Landroid/graphics/drawable/Drawable;', 'if-eqz v0, :cond_0', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->getRight()I', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->getLeft()I', 'iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseContentInsets:Landroid/graphics/Rect;', 'iget v2, v2, Landroid/graphics/Rect;->top:I'],
        'type': 'method_replace',
        'search': """.method protected dispatchDraw(Landroid/graphics/Canvas;)V
    .registers 6

    iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentAutoFitSystemWindow:Z

    if-eqz v0, :cond_0

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentHeaderBackground:Landroid/graphics/drawable/Drawable;

    if-eqz v0, :cond_0

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getRight()I

    move-result v1

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getLeft()I

    move-result v2

    sub-int/2addr v1, v2

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseContentInsets:Landroid/graphics/Rect;

    iget v2, v2, Landroid/graphics/Rect;->top:I

    const/4 v3, 0x0

    invoke-virtual {v0, v3, v3, v1, v2}, Landroid/graphics/drawable/Drawable;->setBounds(IIII)V

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentHeaderBackground:Landroid/graphics/drawable/Drawable;

    invoke-virtual {v0, p1}, Landroid/graphics/drawable/Drawable;->draw(Landroid/graphics/Canvas;)V

    :cond_0
    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->dispatchDraw(Landroid/graphics/Canvas;)V

    return-void
.end method""",
        'replacement': """.method protected dispatchDraw(Landroid/graphics/Canvas;)V
    .registers 6

    goto :goto_b

    nop

    :goto_0
    if-nez v0, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_a

    nop

    :goto_1
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentHeaderBackground:Landroid/graphics/drawable/Drawable;

    goto :goto_2

    nop

    :goto_2
    invoke-virtual {v0, p1}, Landroid/graphics/drawable/Drawable;->draw(Landroid/graphics/Canvas;)V

    :goto_3
    goto :goto_4

    nop

    :goto_4
    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->dispatchDraw(Landroid/graphics/Canvas;)V

    goto :goto_f

    nop

    :goto_5
    if-nez v0, :cond_1

    goto :goto_3

    :cond_1
    goto :goto_d

    nop

    :goto_6
    sub-int/2addr v1, v2

    goto :goto_c

    nop

    :goto_7
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getLeft()I

    move-result v2

    goto :goto_6

    nop

    :goto_8
    iget v2, v2, Landroid/graphics/Rect;->top:I

    goto :goto_e

    nop

    :goto_9
    invoke-virtual {v0, v3, v3, v1, v2}, Landroid/graphics/drawable/Drawable;->setBounds(IIII)V

    goto :goto_1

    nop

    :goto_a
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentHeaderBackground:Landroid/graphics/drawable/Drawable;

    goto :goto_5

    nop

    :goto_b
    iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentAutoFitSystemWindow:Z

    goto :goto_0

    nop

    :goto_c
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseContentInsets:Landroid/graphics/Rect;

    goto :goto_8

    nop

    :goto_d
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getRight()I

    move-result v1

    goto :goto_7

    nop

    :goto_e
    const/4 v3, 0x0

    goto :goto_9

    nop

    :goto_f
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarOverlayLayout__fitSystemWindows',
        'method': '.method protected fitSystemWindows(Landroid/graphics/Rect;)Z',
        'method_name': 'fitSystemWindows',
        'method_anchors': ['iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mLayoutStable:Z', 'invoke-direct {p0, p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->dispatchInsetsIgnoreVisibility(Landroid/view/ViewGroup;Z)V', 'invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->isLayoutHideNavigation()Z', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->isTranslucentStatus()Z', 'iput v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mSystemBarsInsetBottom:I', 'iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mOriginalInset:Landroid/graphics/Rect;', 'invoke-virtual {v1, p1}, Landroid/graphics/Rect;->set(Landroid/graphics/Rect;)V', 'iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;'],
        'type': 'method_replace',
        'search': """.method protected fitSystemWindows(Landroid/graphics/Rect;)Z
    .registers 16

    iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mLayoutStable:Z

    invoke-direct {p0, p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->dispatchInsetsIgnoreVisibility(Landroid/view/ViewGroup;Z)V

    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->isLayoutHideNavigation()Z

    move-result v3

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->isTranslucentStatus()Z

    move-result v2

    const/4 v0, 0x0

    iput v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mSystemBarsInsetBottom:I

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mOriginalInset:Landroid/graphics/Rect;

    invoke-virtual {v1, p1}, Landroid/graphics/Rect;->set(Landroid/graphics/Rect;)V

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    invoke-virtual {v1, p1}, Landroid/graphics/Rect;->set(Landroid/graphics/Rect;)V

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseInnerInsets:Landroid/graphics/Rect;

    invoke-virtual {v1, p1}, Landroid/graphics/Rect;->set(Landroid/graphics/Rect;)V

    invoke-static {p0}, Landroidx/core/view/ViewCompat;->getRootWindowInsets(Landroid/view/View;)Landroidx/core/view/WindowInsetsCompat;

    move-result-object p1

    if-eqz p1, :cond_1

    iget-boolean v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mLayoutStable:Z

    if-eqz v1, :cond_0

    invoke-static {}, Landroidx/core/view/WindowInsetsCompat$Type;->systemBars()I

    move-result v1

    invoke-virtual {p1, v1}, Landroidx/core/view/WindowInsetsCompat;->getInsetsIgnoringVisibility(I)Landroidx/core/graphics/Insets;

    move-result-object v1

    invoke-static {}, Landroidx/core/view/WindowInsetsCompat$Type;->systemBars()I

    move-result v4

    invoke-static {}, Landroidx/core/view/WindowInsetsCompat$Type;->displayCutout()I

    move-result v5

    or-int/2addr v4, v5

    invoke-virtual {p1, v4}, Landroidx/core/view/WindowInsetsCompat;->getInsetsIgnoringVisibility(I)Landroidx/core/graphics/Insets;

    move-result-object v4

    goto :goto_0

    :cond_0
    invoke-static {}, Landroidx/core/view/WindowInsetsCompat$Type;->systemBars()I

    move-result v1

    invoke-virtual {p1, v1}, Landroidx/core/view/WindowInsetsCompat;->getInsets(I)Landroidx/core/graphics/Insets;

    move-result-object v1

    invoke-static {}, Landroidx/core/view/WindowInsetsCompat$Type;->systemBars()I

    move-result v4

    invoke-static {}, Landroidx/core/view/WindowInsetsCompat$Type;->displayCutout()I

    move-result v5

    or-int/2addr v4, v5

    invoke-virtual {p1, v4}, Landroidx/core/view/WindowInsetsCompat;->getInsets(I)Landroidx/core/graphics/Insets;

    move-result-object v4

    :goto_0
    iget v1, v1, Landroidx/core/graphics/Insets;->bottom:I

    iput v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mSystemBarsInsetBottom:I

    invoke-static {}, Landroidx/core/view/WindowInsetsCompat$Type;->ime()I

    move-result v1

    invoke-virtual {p1, v1}, Landroidx/core/view/WindowInsetsCompat;->getInsets(I)Landroidx/core/graphics/Insets;

    move-result-object v1

    iget v1, v1, Landroidx/core/graphics/Insets;->bottom:I

    iput v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mImeInsetBottom:I

    iget-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    iget v6, v4, Landroidx/core/graphics/Insets;->left:I

    iput v6, v5, Landroid/graphics/Rect;->left:I

    iget v4, v4, Landroidx/core/graphics/Insets;->right:I

    iput v4, v5, Landroid/graphics/Rect;->right:I

    iget v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mSystemBarsInsetBottom:I

    iput v4, v5, Landroid/graphics/Rect;->bottom:I

    iget-boolean v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mSqueezeContentByIme:Z

    if-eqz v4, :cond_1

    if-lez v1, :cond_1

    iput v0, v5, Landroid/graphics/Rect;->bottom:I

    :cond_1
    if-nez v3, :cond_3

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    iput v0, v1, Landroid/graphics/Rect;->bottom:I

    iget-boolean v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mLayoutStable:Z

    invoke-direct {p0, p1, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->isNavigationBarToLeftEdge(Landroidx/core/view/WindowInsetsCompat;Z)Z

    move-result v1

    if-eqz v1, :cond_2

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    iput v0, v1, Landroid/graphics/Rect;->left:I

    :cond_2
    iget-boolean v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mLayoutStable:Z

    invoke-direct {p0, p1, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->isNavigationBarToRightEdge(Landroidx/core/view/WindowInsetsCompat;Z)Z

    move-result p1

    if-eqz p1, :cond_3

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    iput v0, p1, Landroid/graphics/Rect;->right:I

    :cond_3
    iget-boolean p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mIsMiuixFloating:Z

    if-nez p1, :cond_4

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mInsetsConfig:Lmiuix/view/WindowInsetsController$InsetsConfig;

    if-eqz p1, :cond_5

    iget-boolean p1, p1, Lmiuix/view/WindowInsetsController$InsetsConfig;->isFloatingMode:Z

    if-eqz p1, :cond_5

    :cond_4
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseInnerInsets:Landroid/graphics/Rect;

    iget v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mInsetTopInMiuixFloating:I

    iput v1, p1, Landroid/graphics/Rect;->top:I

    iput v0, p1, Landroid/graphics/Rect;->left:I

    iput v0, p1, Landroid/graphics/Rect;->right:I

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseContentInsets:Landroid/graphics/Rect;

    iget v1, v1, Landroid/graphics/Rect;->top:I

    iput v1, p1, Landroid/graphics/Rect;->top:I

    iput v0, p1, Landroid/graphics/Rect;->bottom:I

    iput v0, p1, Landroid/graphics/Rect;->left:I

    iput v0, p1, Landroid/graphics/Rect;->right:I

    :cond_5
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;

    move-result-object p1

    invoke-static {p1}, Lmiuix/core/util/MiuixUIUtils;->renderContentInCutoutArea(Landroid/content/Context;)Z

    move-result p1

    if-eqz p1, :cond_7

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseInnerInsets:Landroid/graphics/Rect;

    iput v0, p1, Landroid/graphics/Rect;->left:I

    iput v0, p1, Landroid/graphics/Rect;->right:I

    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->getDisplayCoutInsets()Landroidx/core/graphics/Insets;

    move-result-object p1

    invoke-direct {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->isCutoutToLeftEdge(Landroidx/core/graphics/Insets;)Z

    move-result v1

    if-eqz v1, :cond_6

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    iput v0, v1, Landroid/graphics/Rect;->left:I

    :cond_6
    invoke-direct {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->isCutoutToRightEdge(Landroidx/core/graphics/Insets;)Z

    move-result p1

    if-eqz p1, :cond_7

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    iput v0, p1, Landroid/graphics/Rect;->right:I

    :cond_7
    iget-boolean p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mOverlayMode:Z

    if-eqz p1, :cond_8

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->updateCurrentContentInsetInOverlayMode()V

    goto :goto_1

    :cond_8
    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->updateCurrentContentInset()V

    :goto_1
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->isRootSubDecor()Z

    move-result p1

    if-nez p1, :cond_a

    if-eqz v3, :cond_9

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseInnerInsets:Landroid/graphics/Rect;

    iget p1, p1, Landroid/graphics/Rect;->bottom:I

    iget v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mSystemBarsInsetBottom:I

    if-eq p1, v1, :cond_a

    :cond_9
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseInnerInsets:Landroid/graphics/Rect;

    iput v0, p1, Landroid/graphics/Rect;->bottom:I

    :cond_a
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mInsetsConfig:Lmiuix/view/WindowInsetsController$InsetsConfig;

    if-eqz p1, :cond_e

    iget-boolean v1, p1, Lmiuix/view/WindowInsetsController$InsetsConfig;->isFloatingMode:Z

    if-nez v1, :cond_e

    iget-boolean v1, p1, Lmiuix/view/WindowInsetsController$InsetsConfig;->ignoreLeftInset:Z

    if-eqz v1, :cond_b

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseInnerInsets:Landroid/graphics/Rect;

    iput v0, v1, Landroid/graphics/Rect;->left:I

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    iput v0, v1, Landroid/graphics/Rect;->left:I

    :cond_b
    iget-boolean v1, p1, Lmiuix/view/WindowInsetsController$InsetsConfig;->ignoreTopInset:Z

    if-eqz v1, :cond_c

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseInnerInsets:Landroid/graphics/Rect;

    iput v0, v1, Landroid/graphics/Rect;->top:I

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    iput v0, v1, Landroid/graphics/Rect;->top:I

    :cond_c
    iget-boolean v1, p1, Lmiuix/view/WindowInsetsController$InsetsConfig;->ignoreRightInset:Z

    if-eqz v1, :cond_d

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseInnerInsets:Landroid/graphics/Rect;

    iput v0, v1, Landroid/graphics/Rect;->right:I

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    iput v0, v1, Landroid/graphics/Rect;->right:I

    :cond_d
    iget-boolean p1, p1, Lmiuix/view/WindowInsetsController$InsetsConfig;->ignoreBottomInset:Z

    if-eqz p1, :cond_e

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseInnerInsets:Landroid/graphics/Rect;

    iput v0, p1, Landroid/graphics/Rect;->bottom:I

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    iput v0, p1, Landroid/graphics/Rect;->bottom:I

    :cond_e
    iget v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mImeInsetBottom:I

    iget-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseInnerInsets:Landroid/graphics/Rect;

    iget-object v6, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseContentInsets:Landroid/graphics/Rect;

    move-object v1, p0

    invoke-direct/range {v1 .. v6}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->computeFitSystemInsets(ZZILandroid/graphics/Rect;Landroid/graphics/Rect;)V

    move-object v7, v1

    iget-object p0, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarTop:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    const/4 p1, 0x1

    if-eqz p0, :cond_12

    if-eqz v2, :cond_f

    iget-object v1, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseInnerInsets:Landroid/graphics/Rect;

    invoke-virtual {p0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->setPendingInsets(Landroid/graphics/Rect;)V

    :cond_f
    iget-object p0, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionMode:Landroid/view/ActionMode;

    instance-of v1, p0, Lmiuix/appcompat/internal/view/SearchActionModeImpl;

    if-eqz v1, :cond_10

    check-cast p0, Lmiuix/appcompat/internal/view/SearchActionModeImpl;

    iget-object v1, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseInnerInsets:Landroid/graphics/Rect;

    invoke-virtual {p0, v1}, Lmiuix/appcompat/internal/view/SearchActionModeImpl;->setPendingInsets(Landroid/graphics/Rect;)V

    :cond_10
    iget-object v8, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarTop:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    iget-object v9, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    invoke-virtual {v7}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->isRootSubDecor()Z

    move-result p0

    if-eqz p0, :cond_11

    if-nez v2, :cond_11

    move v11, p1

    goto :goto_2

    :cond_11
    move v11, v0

    :goto_2
    const/4 v12, 0x1

    const/4 v13, 0x0

    const/4 v10, 0x1

    invoke-direct/range {v7 .. v13}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->applyInsetsByMargin(Landroid/view/View;Landroid/graphics/Rect;ZZZZ)Z

    move-result p0

    goto :goto_3

    :cond_12
    move p0, v0

    :goto_3
    iget-object v1, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarContextView:Lmiuix/appcompat/internal/app/widget/ActionBarContextView;

    if-eqz v1, :cond_13

    iget-object v2, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    invoke-virtual {v1, v2}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->setPendingInset(Landroid/graphics/Rect;)V

    :cond_13
    iget-object v1, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarBottom:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    if-eqz v1, :cond_17

    iget-object v2, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    invoke-virtual {v1, v2}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->setPendingInsets(Landroid/graphics/Rect;)V

    iget-object v1, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentMaskInsets:Landroid/graphics/Rect;

    iget-object v2, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseInnerInsets:Landroid/graphics/Rect;

    invoke-virtual {v1, v2}, Landroid/graphics/Rect;->set(Landroid/graphics/Rect;)V

    new-instance v1, Landroid/graphics/Rect;

    invoke-direct {v1}, Landroid/graphics/Rect;-><init>()V

    iget-object v2, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseContentInsets:Landroid/graphics/Rect;

    invoke-virtual {v1, v2}, Landroid/graphics/Rect;->set(Landroid/graphics/Rect;)V

    iget-boolean v2, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mIsFloatingWindow:Z

    if-nez v2, :cond_14

    iget-object v2, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mInsetsConfig:Lmiuix/view/WindowInsetsController$InsetsConfig;

    if-eqz v2, :cond_15

    iget-boolean v2, v2, Lmiuix/view/WindowInsetsController$InsetsConfig;->isFloatingMode:Z

    if-eqz v2, :cond_15

    :cond_14
    iput v0, v1, Landroid/graphics/Rect;->bottom:I

    :cond_15
    iget-boolean v1, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mSqueezeContentByIme:Z

    if-eqz v1, :cond_16

    new-instance v9, Landroid/graphics/Rect;

    iget-object v1, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    invoke-direct {v9, v1}, Landroid/graphics/Rect;-><init>(Landroid/graphics/Rect;)V

    iget-object v1, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseContentInsets:Landroid/graphics/Rect;

    iget v1, v1, Landroid/graphics/Rect;->bottom:I

    iput v1, v9, Landroid/graphics/Rect;->bottom:I

    iget-object v8, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarBottom:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    const/4 v12, 0x1

    const/4 v13, 0x1

    const/4 v10, 0x1

    const/4 v11, 0x0

    invoke-direct/range {v7 .. v13}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->applyInsetsByMargin(Landroid/view/View;Landroid/graphics/Rect;ZZZZ)Z

    move-result v1

    :goto_4
    or-int/2addr p0, v1

    goto :goto_5

    :cond_16
    iget-object v8, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarBottom:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    iget-object v9, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    const/4 v12, 0x1

    const/4 v13, 0x0

    const/4 v10, 0x1

    const/4 v11, 0x0

    invoke-direct/range {v7 .. v13}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->applyInsetsByMargin(Landroid/view/View;Landroid/graphics/Rect;ZZZZ)Z

    move-result v1

    goto :goto_4

    :cond_17
    :goto_5
    iget-object v1, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    if-eqz v1, :cond_18

    iget-object v2, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    invoke-virtual {v1, v2}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->setPendingInset(Landroid/graphics/Rect;)V

    :cond_18
    iget-object v1, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mLastBaseContentInsets:Landroid/graphics/Rect;

    iget-object v2, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseContentInsets:Landroid/graphics/Rect;

    invoke-virtual {v1, v2}, Landroid/graphics/Rect;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-nez v1, :cond_19

    iget-object p0, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mLastBaseContentInsets:Landroid/graphics/Rect;

    iget-object v1, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseContentInsets:Landroid/graphics/Rect;

    invoke-virtual {p0, v1}, Landroid/graphics/Rect;->set(Landroid/graphics/Rect;)V

    move p0, p1

    :cond_19
    if-eqz p0, :cond_1a

    invoke-virtual {v7}, Landroid/widget/FrameLayout;->requestLayout()V

    :cond_1a
    iget-object p0, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarTop:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    if-nez p0, :cond_1b

    iget-object p0, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarBottom:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    if-nez p0, :cond_1b

    move p0, p1

    goto :goto_6

    :cond_1b
    move p0, v0

    :goto_6
    invoke-virtual {v7}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->isRootSubDecor()Z

    move-result v1

    if-eqz v1, :cond_1c

    if-nez p0, :cond_1c

    return p1

    :cond_1c
    return v0
.end method""",
        'replacement': """.method protected fitSystemWindows(Landroid/graphics/Rect;)Z
    .registers 16

    goto :goto_f

    nop

    :goto_0
    invoke-virtual {v1, p1}, Landroid/graphics/Rect;->set(Landroid/graphics/Rect;)V

    goto :goto_2

    nop

    :goto_1
    or-int/2addr p0, v1

    goto :goto_e7

    nop

    :goto_2
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    goto :goto_3d

    nop

    :goto_3
    if-nez p1, :cond_0

    goto :goto_10a

    :cond_0
    goto :goto_6b

    nop

    :goto_4
    iget v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mSystemBarsInsetBottom:I

    goto :goto_d9

    nop

    :goto_5
    invoke-virtual {v1, v2}, Landroid/graphics/Rect;->equals(Ljava/lang/Object;)Z

    move-result v1

    goto :goto_80

    nop

    :goto_6
    goto :goto_9f

    :goto_7
    goto :goto_44

    nop

    :goto_8
    if-nez v1, :cond_1

    goto :goto_22

    :cond_1
    goto :goto_e3

    nop

    :goto_9
    iget v1, v1, Landroid/graphics/Rect;->bottom:I

    goto :goto_5c

    nop

    :goto_a
    iget-object v8, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarBottom:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_9b

    nop

    :goto_b
    iget-object p0, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarTop:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_4d

    nop

    :goto_c
    iput v0, p1, Landroid/graphics/Rect;->left:I

    goto :goto_ef

    nop

    :goto_d
    if-eqz v3, :cond_2

    goto :goto_35

    :cond_2
    goto :goto_1d

    nop

    :goto_e
    move-object v7, v1

    goto :goto_1c

    nop

    :goto_f
    iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mLayoutStable:Z

    goto :goto_76

    nop

    :goto_10
    iput v0, v5, Landroid/graphics/Rect;->bottom:I

    :goto_11
    goto :goto_d

    nop

    :goto_12
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    goto :goto_13

    nop

    :goto_13
    iput v0, v1, Landroid/graphics/Rect;->top:I

    :goto_14
    goto :goto_dd

    nop

    :goto_15
    iput v4, v5, Landroid/graphics/Rect;->bottom:I

    goto :goto_85

    nop

    :goto_16
    iget v1, v1, Landroidx/core/graphics/Insets;->bottom:I

    goto :goto_42

    nop

    :goto_17
    iput v0, v1, Landroid/graphics/Rect;->bottom:I

    goto :goto_d6

    nop

    :goto_18
    invoke-virtual {p1, v1}, Landroidx/core/view/WindowInsetsCompat;->getInsetsIgnoringVisibility(I)Landroidx/core/graphics/Insets;

    move-result-object v1

    goto :goto_f0

    nop

    :goto_19
    iget v1, v1, Landroid/graphics/Rect;->top:I

    goto :goto_fa

    nop

    :goto_1a
    iget-object v1, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarContextView:Lmiuix/appcompat/internal/app/widget/ActionBarContextView;

    goto :goto_6c

    nop

    :goto_1b
    iget-boolean v1, p1, Lmiuix/view/WindowInsetsController$InsetsConfig;->ignoreTopInset:Z

    goto :goto_a6

    nop

    :goto_1c
    iget-object p0, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarTop:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_b2

    nop

    :goto_1d
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    goto :goto_17

    nop

    :goto_1e
    if-eqz v2, :cond_3

    goto :goto_84

    :cond_3
    goto :goto_d2

    nop

    :goto_1f
    invoke-direct/range {v7 .. v13}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->applyInsetsByMargin(Landroid/view/View;Landroid/graphics/Rect;ZZZZ)Z

    move-result v1

    :goto_20
    goto :goto_1

    nop

    :goto_21
    return p1

    :goto_22
    goto :goto_c5

    nop

    :goto_23
    iget-object v9, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    goto :goto_97

    nop

    :goto_24
    invoke-virtual {v7}, Landroid/widget/FrameLayout;->requestLayout()V

    :goto_25
    goto :goto_b

    nop

    :goto_26
    invoke-direct {p0, p1, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->isNavigationBarToLeftEdge(Landroidx/core/view/WindowInsetsCompat;Z)Z

    move-result v1

    goto :goto_46

    nop

    :goto_27
    if-nez p1, :cond_4

    goto :goto_10a

    :cond_4
    goto :goto_d0

    nop

    :goto_28
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseInnerInsets:Landroid/graphics/Rect;

    goto :goto_70

    nop

    :goto_29
    goto :goto_69

    :goto_2a
    goto :goto_68

    nop

    :goto_2b
    invoke-virtual {v1, v2}, Landroid/graphics/Rect;->set(Landroid/graphics/Rect;)V

    goto :goto_c9

    nop

    :goto_2c
    iget-boolean p1, p1, Lmiuix/view/WindowInsetsController$InsetsConfig;->ignoreBottomInset:Z

    goto :goto_27

    nop

    :goto_2d
    iget-object v1, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarBottom:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_a5

    nop

    :goto_2e
    iput v0, p1, Landroid/graphics/Rect;->right:I

    :goto_2f
    goto :goto_9d

    nop

    :goto_30
    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->getDisplayCoutInsets()Landroidx/core/graphics/Insets;

    move-result-object p1

    goto :goto_8b

    nop

    :goto_31
    move v11, p1

    goto :goto_29

    nop

    :goto_32
    invoke-direct/range {v1 .. v6}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->computeFitSystemInsets(ZZILandroid/graphics/Rect;Landroid/graphics/Rect;)V

    goto :goto_e

    nop

    :goto_33
    iget-object v1, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_ad

    nop

    :goto_34
    iput v0, p1, Landroid/graphics/Rect;->right:I

    :goto_35
    goto :goto_91

    nop

    :goto_36
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mInsetsConfig:Lmiuix/view/WindowInsetsController$InsetsConfig;

    goto :goto_3

    nop

    :goto_37
    iget v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mSystemBarsInsetBottom:I

    goto :goto_15

    nop

    :goto_38
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseInnerInsets:Landroid/graphics/Rect;

    goto :goto_95

    nop

    :goto_39
    if-eqz p0, :cond_5

    goto :goto_ce

    :cond_5
    goto :goto_4c

    nop

    :goto_3a
    iget-object p0, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionMode:Landroid/view/ActionMode;

    goto :goto_c4

    nop

    :goto_3b
    iget-boolean v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mLayoutStable:Z

    goto :goto_6a

    nop

    :goto_3c
    iget-boolean v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mLayoutStable:Z

    goto :goto_106

    nop

    :goto_3d
    invoke-virtual {v1, p1}, Landroid/graphics/Rect;->set(Landroid/graphics/Rect;)V

    goto :goto_7e

    nop

    :goto_3e
    invoke-virtual {p1, v4}, Landroidx/core/view/WindowInsetsCompat;->getInsetsIgnoringVisibility(I)Landroidx/core/graphics/Insets;

    move-result-object v4

    goto :goto_6

    nop

    :goto_3f
    iget-object v1, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseInnerInsets:Landroid/graphics/Rect;

    goto :goto_49

    nop

    :goto_40
    const/4 v10, 0x1

    goto :goto_94

    nop

    :goto_41
    iput v0, p1, Landroid/graphics/Rect;->bottom:I

    goto :goto_c7

    nop

    :goto_42
    iput v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mImeInsetBottom:I

    goto :goto_10f

    nop

    :goto_43
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseInnerInsets:Landroid/graphics/Rect;

    goto :goto_ec

    nop

    :goto_44
    invoke-static {}, Landroidx/core/view/WindowInsetsCompat$Type;->systemBars()I

    move-result v1

    goto :goto_bf

    nop

    :goto_45
    iget v6, v4, Landroidx/core/graphics/Insets;->left:I

    goto :goto_d5

    nop

    :goto_46
    if-nez v1, :cond_6

    goto :goto_e0

    :cond_6
    goto :goto_79

    nop

    :goto_47
    iget-object v6, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseContentInsets:Landroid/graphics/Rect;

    goto :goto_93

    nop

    :goto_48
    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->isLayoutHideNavigation()Z

    move-result v3

    goto :goto_bc

    nop

    :goto_49
    invoke-virtual {p0, v1}, Lmiuix/appcompat/internal/view/SearchActionModeImpl;->setPendingInsets(Landroid/graphics/Rect;)V

    :goto_4a
    goto :goto_de

    nop

    :goto_4b
    if-eqz p1, :cond_7

    goto :goto_54

    :cond_7
    goto :goto_75

    nop

    :goto_4c
    move p0, p1

    goto :goto_cd

    nop

    :goto_4d
    if-eqz p0, :cond_8

    goto :goto_ce

    :cond_8
    goto :goto_bb

    nop

    :goto_4e
    iget-object v2, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseContentInsets:Landroid/graphics/Rect;

    goto :goto_102

    nop

    :goto_4f
    iput v0, v1, Landroid/graphics/Rect;->bottom:I

    :goto_50
    goto :goto_f6

    nop

    :goto_51
    iput v0, v1, Landroid/graphics/Rect;->left:I

    :goto_52
    goto :goto_1b

    nop

    :goto_53
    iput v0, p1, Landroid/graphics/Rect;->bottom:I

    :goto_54
    goto :goto_36

    nop

    :goto_55
    const/4 v11, 0x0

    goto :goto_1f

    nop

    :goto_56
    iput v0, v1, Landroid/graphics/Rect;->right:I

    goto :goto_b3

    nop

    :goto_57
    invoke-static {}, Landroidx/core/view/WindowInsetsCompat$Type;->displayCutout()I

    move-result v5

    goto :goto_ee

    nop

    :goto_58
    if-nez p0, :cond_9

    goto :goto_fc

    :cond_9
    goto :goto_8c

    nop

    :goto_59
    const/4 v10, 0x1

    goto :goto_b6

    nop

    :goto_5a
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    goto :goto_f5

    nop

    :goto_5b
    if-nez p0, :cond_a

    goto :goto_2a

    :cond_a
    goto :goto_67

    nop

    :goto_5c
    iput v1, v9, Landroid/graphics/Rect;->bottom:I

    goto :goto_f8

    nop

    :goto_5d
    if-nez p1, :cond_b

    goto :goto_35

    :cond_b
    goto :goto_ac

    nop

    :goto_5e
    invoke-virtual {v1, v2}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->setPendingInsets(Landroid/graphics/Rect;)V

    goto :goto_b8

    nop

    :goto_5f
    goto :goto_b5

    :goto_60
    goto :goto_b4

    nop

    :goto_61
    iput v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mSystemBarsInsetBottom:I

    goto :goto_c6

    nop

    :goto_62
    const/4 v12, 0x1

    goto :goto_b9

    nop

    :goto_63
    if-nez p1, :cond_c

    goto :goto_2f

    :cond_c
    goto :goto_10c

    nop

    :goto_64
    if-nez p1, :cond_d

    goto :goto_f2

    :cond_d
    goto :goto_7b

    nop

    :goto_65
    if-nez v1, :cond_e

    goto :goto_87

    :cond_e
    goto :goto_92

    nop

    :goto_66
    const/4 v12, 0x1

    goto :goto_72

    nop

    :goto_67
    if-eqz v2, :cond_f

    goto :goto_2a

    :cond_f
    goto :goto_31

    nop

    :goto_68
    move v11, v0

    :goto_69
    goto :goto_66

    nop

    :goto_6a
    if-nez v1, :cond_10

    goto :goto_7

    :cond_10
    goto :goto_f3

    nop

    :goto_6b
    iget-boolean v1, p1, Lmiuix/view/WindowInsetsController$InsetsConfig;->isFloatingMode:Z

    goto :goto_7f

    nop

    :goto_6c
    if-nez v1, :cond_11

    goto :goto_10e

    :cond_11
    goto :goto_8f

    nop

    :goto_6d
    invoke-virtual {p1, v1}, Landroidx/core/view/WindowInsetsCompat;->getInsets(I)Landroidx/core/graphics/Insets;

    move-result-object v1

    goto :goto_16

    nop

    :goto_6e
    if-nez v1, :cond_12

    goto :goto_108

    :cond_12
    goto :goto_81

    nop

    :goto_6f
    if-eqz p1, :cond_13

    goto :goto_99

    :cond_13
    goto :goto_eb

    nop

    :goto_70
    iput v0, v1, Landroid/graphics/Rect;->left:I

    goto :goto_d7

    nop

    :goto_71
    const/4 v0, 0x0

    goto :goto_61

    nop

    :goto_72
    const/4 v13, 0x0

    goto :goto_40

    nop

    :goto_73
    move p0, v0

    :goto_74
    goto :goto_1a

    nop

    :goto_75
    if-nez v3, :cond_14

    goto :goto_da

    :cond_14
    goto :goto_b0

    nop

    :goto_76
    invoke-direct {p0, p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->dispatchInsetsIgnoreVisibility(Landroid/view/ViewGroup;Z)V

    goto :goto_48

    nop

    :goto_77
    iget-object v1, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    goto :goto_aa

    nop

    :goto_78
    invoke-virtual {v7}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->isRootSubDecor()Z

    move-result v1

    goto :goto_8

    nop

    :goto_79
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    goto :goto_df

    nop

    :goto_7a
    invoke-static {}, Landroidx/core/view/WindowInsetsCompat$Type;->ime()I

    move-result v1

    goto :goto_6d

    nop

    :goto_7b
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    goto :goto_f1

    nop

    :goto_7c
    if-nez v1, :cond_15

    goto :goto_e8

    :cond_15
    goto :goto_c3

    nop

    :goto_7d
    iget-boolean v1, p1, Lmiuix/view/WindowInsetsController$InsetsConfig;->ignoreLeftInset:Z

    goto :goto_103

    nop

    :goto_7e
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseInnerInsets:Landroid/graphics/Rect;

    goto :goto_c1

    nop

    :goto_7f
    if-eqz v1, :cond_16

    goto :goto_10a

    :cond_16
    goto :goto_7d

    nop

    :goto_80
    if-eqz v1, :cond_17

    goto :goto_dc

    :cond_17
    goto :goto_ae

    nop

    :goto_81
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseInnerInsets:Landroid/graphics/Rect;

    goto :goto_56

    nop

    :goto_82
    if-nez v1, :cond_18

    goto :goto_4a

    :cond_18
    goto :goto_b7

    nop

    :goto_83
    if-nez v2, :cond_19

    goto :goto_50

    :cond_19
    :goto_84
    goto :goto_4f

    nop

    :goto_85
    iget-boolean v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mSqueezeContentByIme:Z

    goto :goto_f7

    nop

    :goto_86
    iput v0, v1, Landroid/graphics/Rect;->left:I

    :goto_87
    goto :goto_ff

    nop

    :goto_88
    iput v0, p1, Landroid/graphics/Rect;->bottom:I

    goto :goto_100

    nop

    :goto_89
    iget-boolean v2, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mIsFloatingWindow:Z

    goto :goto_1e

    nop

    :goto_8a
    or-int/2addr v4, v5

    goto :goto_3e

    nop

    :goto_8b
    invoke-direct {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->isCutoutToLeftEdge(Landroidx/core/graphics/Insets;)Z

    move-result v1

    goto :goto_65

    nop

    :goto_8c
    if-nez v2, :cond_1a

    goto :goto_cb

    :cond_1a
    goto :goto_b1

    nop

    :goto_8d
    const/4 v13, 0x0

    goto :goto_59

    nop

    :goto_8e
    if-nez v2, :cond_1b

    goto :goto_50

    :cond_1b
    goto :goto_110

    nop

    :goto_8f
    iget-object v2, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    goto :goto_10d

    nop

    :goto_90
    iput v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mSystemBarsInsetBottom:I

    goto :goto_7a

    nop

    :goto_91
    iget-boolean p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mIsMiuixFloating:Z

    goto :goto_6f

    nop

    :goto_92
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    goto :goto_86

    nop

    :goto_93
    move-object v1, p0

    goto :goto_32

    nop

    :goto_94
    invoke-direct/range {v7 .. v13}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->applyInsetsByMargin(Landroid/view/View;Landroid/graphics/Rect;ZZZZ)Z

    move-result p0

    goto :goto_fb

    nop

    :goto_95
    iget v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mInsetTopInMiuixFloating:I

    goto :goto_a8

    nop

    :goto_96
    const/4 v12, 0x1

    goto :goto_8d

    nop

    :goto_97
    invoke-virtual {v7}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->isRootSubDecor()Z

    move-result p0

    goto :goto_5b

    nop

    :goto_98
    if-nez p1, :cond_1c

    goto :goto_2f

    :cond_1c
    :goto_99
    goto :goto_38

    nop

    :goto_9a
    const/4 v10, 0x1

    goto :goto_55

    nop

    :goto_9b
    iget-object v9, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    goto :goto_96

    nop

    :goto_9c
    iget-boolean p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mOverlayMode:Z

    goto :goto_d3

    nop

    :goto_9d
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;

    move-result-object p1

    goto :goto_e4

    nop

    :goto_9e
    invoke-virtual {p1, v4}, Landroidx/core/view/WindowInsetsCompat;->getInsets(I)Landroidx/core/graphics/Insets;

    move-result-object v4

    :goto_9f
    goto :goto_f9

    nop

    :goto_a0
    move p0, v0

    :goto_a1
    goto :goto_78

    nop

    :goto_a2
    iget-object v2, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseContentInsets:Landroid/graphics/Rect;

    goto :goto_5

    nop

    :goto_a3
    iput v0, p1, Landroid/graphics/Rect;->right:I

    goto :goto_30

    nop

    :goto_a4
    iget v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mImeInsetBottom:I

    goto :goto_af

    nop

    :goto_a5
    if-nez v1, :cond_1d

    goto :goto_e2

    :cond_1d
    goto :goto_d4

    nop

    :goto_a6
    if-nez v1, :cond_1e

    goto :goto_14

    :cond_1e
    goto :goto_c0

    nop

    :goto_a7
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->updateCurrentContentInsetInOverlayMode()V

    goto :goto_5f

    nop

    :goto_a8
    iput v1, p1, Landroid/graphics/Rect;->top:I

    goto :goto_c

    nop

    :goto_a9
    invoke-static {}, Landroidx/core/view/WindowInsetsCompat$Type;->displayCutout()I

    move-result v5

    goto :goto_8a

    nop

    :goto_aa
    invoke-direct {v9, v1}, Landroid/graphics/Rect;-><init>(Landroid/graphics/Rect;)V

    goto :goto_e6

    nop

    :goto_ab
    iget-object v1, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mLastBaseContentInsets:Landroid/graphics/Rect;

    goto :goto_a2

    nop

    :goto_ac
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    goto :goto_34

    nop

    :goto_ad
    if-nez v1, :cond_1f

    goto :goto_be

    :cond_1f
    goto :goto_d8

    nop

    :goto_ae
    iget-object p0, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mLastBaseContentInsets:Landroid/graphics/Rect;

    goto :goto_d1

    nop

    :goto_af
    iget-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseInnerInsets:Landroid/graphics/Rect;

    goto :goto_47

    nop

    :goto_b0
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseInnerInsets:Landroid/graphics/Rect;

    goto :goto_105

    nop

    :goto_b1
    iget-object v1, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseInnerInsets:Landroid/graphics/Rect;

    goto :goto_ca

    nop

    :goto_b2
    const/4 p1, 0x1

    goto :goto_58

    nop

    :goto_b3
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    goto :goto_107

    nop

    :goto_b4
    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->updateCurrentContentInset()V

    :goto_b5
    goto :goto_fd

    nop

    :goto_b6
    const/4 v11, 0x0

    goto :goto_104

    nop

    :goto_b7
    check-cast p0, Lmiuix/appcompat/internal/view/SearchActionModeImpl;

    goto :goto_3f

    nop

    :goto_b8
    iget-object v1, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentMaskInsets:Landroid/graphics/Rect;

    goto :goto_fe

    nop

    :goto_b9
    const/4 v13, 0x1

    goto :goto_9a

    nop

    :goto_ba
    invoke-direct {v1}, Landroid/graphics/Rect;-><init>()V

    goto :goto_4e

    nop

    :goto_bb
    iget-object p0, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarBottom:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_39

    nop

    :goto_bc
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->isTranslucentStatus()Z

    move-result v2

    goto :goto_71

    nop

    :goto_bd
    invoke-virtual {v1, v2}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->setPendingInset(Landroid/graphics/Rect;)V

    :goto_be
    goto :goto_ab

    nop

    :goto_bf
    invoke-virtual {p1, v1}, Landroidx/core/view/WindowInsetsCompat;->getInsets(I)Landroidx/core/graphics/Insets;

    move-result-object v1

    goto :goto_e5

    nop

    :goto_c0
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseInnerInsets:Landroid/graphics/Rect;

    goto :goto_cf

    nop

    :goto_c1
    invoke-virtual {v1, p1}, Landroid/graphics/Rect;->set(Landroid/graphics/Rect;)V

    goto :goto_10b

    nop

    :goto_c2
    invoke-virtual {p0, v1}, Landroid/graphics/Rect;->set(Landroid/graphics/Rect;)V

    goto :goto_db

    nop

    :goto_c3
    new-instance v9, Landroid/graphics/Rect;

    goto :goto_77

    nop

    :goto_c4
    instance-of v1, p0, Lmiuix/appcompat/internal/view/SearchActionModeImpl;

    goto :goto_82

    nop

    :goto_c5
    return v0

    :goto_c6
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mOriginalInset:Landroid/graphics/Rect;

    goto :goto_0

    nop

    :goto_c7
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    goto :goto_109

    nop

    :goto_c8
    if-gtz v1, :cond_20

    goto :goto_11

    :cond_20
    goto :goto_10

    nop

    :goto_c9
    new-instance v1, Landroid/graphics/Rect;

    goto :goto_ba

    nop

    :goto_ca
    invoke-virtual {p0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->setPendingInsets(Landroid/graphics/Rect;)V

    :goto_cb
    goto :goto_3a

    nop

    :goto_cc
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseInnerInsets:Landroid/graphics/Rect;

    goto :goto_53

    nop

    :goto_cd
    goto :goto_a1

    :goto_ce
    goto :goto_a0

    nop

    :goto_cf
    iput v0, v1, Landroid/graphics/Rect;->top:I

    goto :goto_12

    nop

    :goto_d0
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseInnerInsets:Landroid/graphics/Rect;

    goto :goto_41

    nop

    :goto_d1
    iget-object v1, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseContentInsets:Landroid/graphics/Rect;

    goto :goto_c2

    nop

    :goto_d2
    iget-object v2, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mInsetsConfig:Lmiuix/view/WindowInsetsController$InsetsConfig;

    goto :goto_8e

    nop

    :goto_d3
    if-nez p1, :cond_21

    goto :goto_60

    :cond_21
    goto :goto_a7

    nop

    :goto_d4
    iget-object v2, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    goto :goto_5e

    nop

    :goto_d5
    iput v6, v5, Landroid/graphics/Rect;->left:I

    goto :goto_101

    nop

    :goto_d6
    iget-boolean v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mLayoutStable:Z

    goto :goto_26

    nop

    :goto_d7
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    goto :goto_51

    nop

    :goto_d8
    iget-object v2, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    goto :goto_bd

    nop

    :goto_d9
    if-ne p1, v1, :cond_22

    goto :goto_54

    :cond_22
    :goto_da
    goto :goto_cc

    nop

    :goto_db
    move p0, p1

    :goto_dc
    goto :goto_ea

    nop

    :goto_dd
    iget-boolean v1, p1, Lmiuix/view/WindowInsetsController$InsetsConfig;->ignoreRightInset:Z

    goto :goto_6e

    nop

    :goto_de
    iget-object v8, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarTop:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_23

    nop

    :goto_df
    iput v0, v1, Landroid/graphics/Rect;->left:I

    :goto_e0
    goto :goto_3c

    nop

    :goto_e1
    goto :goto_20

    :goto_e2
    goto :goto_33

    nop

    :goto_e3
    if-eqz p0, :cond_23

    goto :goto_22

    :cond_23
    goto :goto_21

    nop

    :goto_e4
    invoke-static {p1}, Lmiuix/core/util/MiuixUIUtils;->renderContentInCutoutArea(Landroid/content/Context;)Z

    move-result p1

    goto :goto_e9

    nop

    :goto_e5
    invoke-static {}, Landroidx/core/view/WindowInsetsCompat$Type;->systemBars()I

    move-result v4

    goto :goto_57

    nop

    :goto_e6
    iget-object v1, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseContentInsets:Landroid/graphics/Rect;

    goto :goto_9

    nop

    :goto_e7
    goto :goto_e2

    :goto_e8
    goto :goto_a

    nop

    :goto_e9
    if-nez p1, :cond_24

    goto :goto_f2

    :cond_24
    goto :goto_43

    nop

    :goto_ea
    if-nez p0, :cond_25

    goto :goto_25

    :cond_25
    goto :goto_24

    nop

    :goto_eb
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mInsetsConfig:Lmiuix/view/WindowInsetsController$InsetsConfig;

    goto :goto_63

    nop

    :goto_ec
    iput v0, p1, Landroid/graphics/Rect;->left:I

    goto :goto_a3

    nop

    :goto_ed
    if-nez p1, :cond_26

    goto :goto_11

    :cond_26
    goto :goto_3b

    nop

    :goto_ee
    or-int/2addr v4, v5

    goto :goto_9e

    nop

    :goto_ef
    iput v0, p1, Landroid/graphics/Rect;->right:I

    goto :goto_5a

    nop

    :goto_f0
    invoke-static {}, Landroidx/core/view/WindowInsetsCompat$Type;->systemBars()I

    move-result v4

    goto :goto_a9

    nop

    :goto_f1
    iput v0, p1, Landroid/graphics/Rect;->right:I

    :goto_f2
    goto :goto_9c

    nop

    :goto_f3
    invoke-static {}, Landroidx/core/view/WindowInsetsCompat$Type;->systemBars()I

    move-result v1

    goto :goto_18

    nop

    :goto_f4
    iput v4, v5, Landroid/graphics/Rect;->right:I

    goto :goto_37

    nop

    :goto_f5
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseContentInsets:Landroid/graphics/Rect;

    goto :goto_19

    nop

    :goto_f6
    iget-boolean v1, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mSqueezeContentByIme:Z

    goto :goto_7c

    nop

    :goto_f7
    if-nez v4, :cond_27

    goto :goto_11

    :cond_27
    goto :goto_c8

    nop

    :goto_f8
    iget-object v8, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarBottom:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_62

    nop

    :goto_f9
    iget v1, v1, Landroidx/core/graphics/Insets;->bottom:I

    goto :goto_90

    nop

    :goto_fa
    iput v1, p1, Landroid/graphics/Rect;->top:I

    goto :goto_88

    nop

    :goto_fb
    goto :goto_74

    :goto_fc
    goto :goto_73

    nop

    :goto_fd
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->isRootSubDecor()Z

    move-result p1

    goto :goto_4b

    nop

    :goto_fe
    iget-object v2, v7, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseInnerInsets:Landroid/graphics/Rect;

    goto :goto_2b

    nop

    :goto_ff
    invoke-direct {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->isCutoutToRightEdge(Landroidx/core/graphics/Insets;)Z

    move-result p1

    goto :goto_64

    nop

    :goto_100
    iput v0, p1, Landroid/graphics/Rect;->left:I

    goto :goto_2e

    nop

    :goto_101
    iget v4, v4, Landroidx/core/graphics/Insets;->right:I

    goto :goto_f4

    nop

    :goto_102
    invoke-virtual {v1, v2}, Landroid/graphics/Rect;->set(Landroid/graphics/Rect;)V

    goto :goto_89

    nop

    :goto_103
    if-nez v1, :cond_28

    goto :goto_52

    :cond_28
    goto :goto_28

    nop

    :goto_104
    invoke-direct/range {v7 .. v13}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->applyInsetsByMargin(Landroid/view/View;Landroid/graphics/Rect;ZZZZ)Z

    move-result v1

    goto :goto_e1

    nop

    :goto_105
    iget p1, p1, Landroid/graphics/Rect;->bottom:I

    goto :goto_4

    nop

    :goto_106
    invoke-direct {p0, p1, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->isNavigationBarToRightEdge(Landroidx/core/view/WindowInsetsCompat;Z)Z

    move-result p1

    goto :goto_5d

    nop

    :goto_107
    iput v0, v1, Landroid/graphics/Rect;->right:I

    :goto_108
    goto :goto_2c

    nop

    :goto_109
    iput v0, p1, Landroid/graphics/Rect;->bottom:I

    :goto_10a
    goto :goto_a4

    nop

    :goto_10b
    invoke-static {p0}, Landroidx/core/view/ViewCompat;->getRootWindowInsets(Landroid/view/View;)Landroidx/core/view/WindowInsetsCompat;

    move-result-object p1

    goto :goto_ed

    nop

    :goto_10c
    iget-boolean p1, p1, Lmiuix/view/WindowInsetsController$InsetsConfig;->isFloatingMode:Z

    goto :goto_98

    nop

    :goto_10d
    invoke-virtual {v1, v2}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->setPendingInset(Landroid/graphics/Rect;)V

    :goto_10e
    goto :goto_2d

    nop

    :goto_10f
    iget-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    goto :goto_45

    nop

    :goto_110
    iget-boolean v2, v2, Lmiuix/view/WindowInsetsController$InsetsConfig;->isFloatingMode:Z

    goto :goto_83

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarOverlayLayout__getBottomInset',
        'method': '.method protected getBottomInset()I',
        'method_name': 'getBottomInset',
        'method_anchors': ['iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarBottom:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;', 'if-eqz p0, :cond_0', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->getInsetHeight()I', 'return p0', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected getBottomInset()I
    .registers 1

    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarBottom:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    if-eqz p0, :cond_0

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->getInsetHeight()I

    move-result p0

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method protected getBottomInset()I
    .registers 1

    goto :goto_2

    nop

    :goto_0
    const/4 p0, 0x0

    goto :goto_5

    nop

    :goto_1
    if-nez p0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_6

    nop

    :goto_2
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarBottom:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_1

    nop

    :goto_3
    return p0

    :goto_4
    goto :goto_0

    nop

    :goto_5
    return p0

    :goto_6
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->getInsetHeight()I

    move-result p0

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarOverlayLayout__onAttachedToWindow',
        'method': '.method protected onAttachedToWindow()V',
        'method_name': 'onAttachedToWindow',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/FrameLayout;->onAttachedToWindow()V', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->requestFitSystemWindows()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onAttachedToWindow()V
    .registers 1

    invoke-super {p0}, Landroid/widget/FrameLayout;->onAttachedToWindow()V

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->requestFitSystemWindows()V

    return-void
.end method""",
        'replacement': """.method protected onAttachedToWindow()V
    .registers 1

    goto :goto_1

    nop

    :goto_0
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->requestFitSystemWindows()V

    goto :goto_2

    nop

    :goto_1
    invoke-super {p0}, Landroid/widget/FrameLayout;->onAttachedToWindow()V

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
        'id': 'miuix_appcompat_internal_app_widget_ActionBarOverlayLayout__onConfigurationChanged',
        'method': '.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V',
        'method_name': 'onConfigurationChanged',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/widget/FrameLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;', 'new-instance v1, Ljava/lang/StringBuilder;', 'invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V', 'const-string v2, "->processActionBarOverlayLayout ConfigurationChanged newConfig.densityDpi "', 'invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'iget v2, p1, Landroid/content/res/Configuration;->densityDpi:I', 'invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;'],
        'type': 'method_replace',
        'search': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 5

    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;

    move-result-object v0

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "->processActionBarOverlayLayout ConfigurationChanged newConfig.densityDpi "

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget v2, p1, Landroid/content/res/Configuration;->densityDpi:I

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-static {v1}, Lmiuix/autodensity/DebugUtil;->printDensityLog(Ljava/lang/String;)V

    invoke-static {}, Lmiuix/autodensity/DensityConfigManager;->getInstance()Lmiuix/autodensity/DensityConfigManager;

    move-result-object v1

    invoke-virtual {v1, v0, p1}, Lmiuix/autodensity/DensityConfigManager;->tryUpdateConfig(Landroid/content/Context;Landroid/content/res/Configuration;)Z

    invoke-static {v0}, Lmiuix/autodensity/AutoDensityConfig;->updateDensity(Landroid/content/Context;)V

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mFloatingWindowSize:Lmiuix/appcompat/app/floatingactivity/FloatingABOLayoutSpec;

    invoke-virtual {p1}, Lmiuix/appcompat/app/floatingactivity/FloatingABOLayoutSpec;->onConfigurationChanged()V

    new-instance p1, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout$$ExternalSyntheticLambda1;

    invoke-direct {p1, p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout$$ExternalSyntheticLambda1;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;)V

    invoke-virtual {p0, p1}, Landroid/widget/FrameLayout;->post(Ljava/lang/Runnable;)Z

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContextMenu:Lmiuix/appcompat/internal/view/menu/context/ContextMenuBuilder;

    if-eqz p1, :cond_0

    invoke-virtual {p1}, Lmiuix/appcompat/internal/view/menu/context/ContextMenuBuilder;->isContextMenuPopupWindowShowing()Z

    move-result p1

    if-eqz p1, :cond_0

    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContextMenu:Lmiuix/appcompat/internal/view/menu/context/ContextMenuBuilder;

    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/context/ContextMenuBuilder;->refreshContextMenuPopupWindow()V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 5

    goto :goto_8

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContextMenu:Lmiuix/appcompat/internal/view/menu/context/ContextMenuBuilder;

    goto :goto_3

    nop

    :goto_1
    invoke-static {v0}, Lmiuix/autodensity/AutoDensityConfig;->updateDensity(Landroid/content/Context;)V

    goto :goto_c

    nop

    :goto_2
    invoke-virtual {p1}, Lmiuix/appcompat/internal/view/menu/context/ContextMenuBuilder;->isContextMenuPopupWindowShowing()Z

    move-result p1

    goto :goto_13

    nop

    :goto_3
    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/context/ContextMenuBuilder;->refreshContextMenuPopupWindow()V

    :goto_4
    goto :goto_6

    nop

    :goto_5
    invoke-virtual {p1}, Lmiuix/appcompat/app/floatingactivity/FloatingABOLayoutSpec;->onConfigurationChanged()V

    goto :goto_f

    nop

    :goto_6
    return-void

    :goto_7
    new-instance v1, Ljava/lang/StringBuilder;

    goto :goto_17

    nop

    :goto_8
    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    goto :goto_12

    nop

    :goto_9
    iget v2, p1, Landroid/content/res/Configuration;->densityDpi:I

    goto :goto_a

    nop

    :goto_a
    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_11

    nop

    :goto_b
    const-string v2, "->processActionBarOverlayLayout ConfigurationChanged newConfig.densityDpi "

    goto :goto_14

    nop

    :goto_c
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mFloatingWindowSize:Lmiuix/appcompat/app/floatingactivity/FloatingABOLayoutSpec;

    goto :goto_5

    nop

    :goto_d
    invoke-virtual {v1, v0, p1}, Lmiuix/autodensity/DensityConfigManager;->tryUpdateConfig(Landroid/content/Context;Landroid/content/res/Configuration;)Z

    goto :goto_1

    nop

    :goto_e
    if-nez p1, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_2

    nop

    :goto_f
    new-instance p1, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout$$ExternalSyntheticLambda1;

    goto :goto_19

    nop

    :goto_10
    invoke-virtual {p0, p1}, Landroid/widget/FrameLayout;->post(Ljava/lang/Runnable;)Z

    goto :goto_15

    nop

    :goto_11
    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    goto :goto_18

    nop

    :goto_12
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;

    move-result-object v0

    goto :goto_7

    nop

    :goto_13
    if-nez p1, :cond_1

    goto :goto_4

    :cond_1
    goto :goto_0

    nop

    :goto_14
    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_9

    nop

    :goto_15
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContextMenu:Lmiuix/appcompat/internal/view/menu/context/ContextMenuBuilder;

    goto :goto_e

    nop

    :goto_16
    invoke-static {}, Lmiuix/autodensity/DensityConfigManager;->getInstance()Lmiuix/autodensity/DensityConfigManager;

    move-result-object v1

    goto :goto_d

    nop

    :goto_17
    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_b

    nop

    :goto_18
    invoke-static {v1}, Lmiuix/autodensity/DebugUtil;->printDensityLog(Ljava/lang/String;)V

    goto :goto_16

    nop

    :goto_19
    invoke-direct {p1, p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout$$ExternalSyntheticLambda1;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;)V

    goto :goto_10

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarOverlayLayout__onDetachedFromWindow',
        'method': '.method protected onDetachedFromWindow()V',
        'method_name': 'onDetachedFromWindow',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/FrameLayout;->onDetachedFromWindow()V', 'invoke-virtual {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->setContentInsetStateCallback(Lmiuix/appcompat/app/IContentInsetState;)V', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mExtraPaddingObserver:Ljava/util/List;', 'if-eqz v0, :cond_0', 'invoke-interface {v0}, Ljava/util/List;->clear()V', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mGroupButtonPanelView:Lmiuix/appcompat/app/GroupButtonsPanel;', 'if-eqz v0, :cond_1', 'iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mOnContainerViewLayoutChangeListener:Landroid/view/View$OnLayoutChangeListener;'],
        'type': 'method_replace',
        'search': """.method protected onDetachedFromWindow()V
    .registers 2

    invoke-super {p0}, Landroid/widget/FrameLayout;->onDetachedFromWindow()V

    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->setContentInsetStateCallback(Lmiuix/appcompat/app/IContentInsetState;)V

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mExtraPaddingObserver:Ljava/util/List;

    if-eqz v0, :cond_0

    invoke-interface {v0}, Ljava/util/List;->clear()V

    :cond_0
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mGroupButtonPanelView:Lmiuix/appcompat/app/GroupButtonsPanel;

    if-eqz v0, :cond_1

    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mOnContainerViewLayoutChangeListener:Landroid/view/View$OnLayoutChangeListener;

    if-eqz p0, :cond_1

    invoke-virtual {v0, p0}, Landroid/widget/FrameLayout;->removeOnLayoutChangeListener(Landroid/view/View$OnLayoutChangeListener;)V

    :cond_1
    return-void
.end method""",
        'replacement': """.method protected onDetachedFromWindow()V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    if-nez v0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_d

    nop

    :goto_1
    invoke-super {p0}, Landroid/widget/FrameLayout;->onDetachedFromWindow()V

    goto :goto_c

    nop

    :goto_2
    return-void

    :goto_3
    invoke-virtual {v0, p0}, Landroid/widget/FrameLayout;->removeOnLayoutChangeListener(Landroid/view/View$OnLayoutChangeListener;)V

    :goto_4
    goto :goto_2

    nop

    :goto_5
    if-nez v0, :cond_1

    goto :goto_b

    :cond_1
    goto :goto_a

    nop

    :goto_6
    if-nez p0, :cond_2

    goto :goto_4

    :cond_2
    goto :goto_3

    nop

    :goto_7
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mExtraPaddingObserver:Ljava/util/List;

    goto :goto_5

    nop

    :goto_8
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mGroupButtonPanelView:Lmiuix/appcompat/app/GroupButtonsPanel;

    goto :goto_0

    nop

    :goto_9
    invoke-virtual {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->setContentInsetStateCallback(Lmiuix/appcompat/app/IContentInsetState;)V

    goto :goto_7

    nop

    :goto_a
    invoke-interface {v0}, Ljava/util/List;->clear()V

    :goto_b
    goto :goto_8

    nop

    :goto_c
    const/4 v0, 0x0

    goto :goto_9

    nop

    :goto_d
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mOnContainerViewLayoutChangeListener:Landroid/view/View$OnLayoutChangeListener;

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarOverlayLayout__onFinishInflate',
        'method': '.method protected onFinishInflate()V',
        'method_name': 'onFinishInflate',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/FrameLayout;->onFinishInflate()V', 'invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->pullChildren()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onFinishInflate()V
    .registers 1

    invoke-super {p0}, Landroid/widget/FrameLayout;->onFinishInflate()V

    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->pullChildren()V

    return-void
.end method""",
        'replacement': """.method protected onFinishInflate()V
    .registers 1

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0}, Landroid/widget/FrameLayout;->onFinishInflate()V

    goto :goto_1

    nop

    :goto_1
    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->pullChildren()V

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
        'id': 'miuix_appcompat_internal_app_widget_ActionBarOverlayLayout__onLayout',
        'method': '.method protected onLayout(ZIIII)V',
        'method_name': 'onLayout',
        'method_anchors': ['invoke-super/range {p0 .. p5}, Landroid/widget/FrameLayout;->onLayout(ZIIII)V', 'iget-boolean p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mOverlayMode:Z', 'if-eqz p1, :cond_0', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->updateCurrentContentInsetInOverlayMode()V', 'iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mExtraPaddingPolicy:Lmiuix/container/ExtraPaddingPolicy;', 'if-eqz p1, :cond_2', 'invoke-virtual {p1}, Lmiuix/container/ExtraPaddingPolicy;->isEnable()Z', 'if-eqz p1, :cond_2'],
        'type': 'method_replace',
        'search': """.method protected onLayout(ZIIII)V
    .registers 13

    invoke-super/range {p0 .. p5}, Landroid/widget/FrameLayout;->onLayout(ZIIII)V

    iget-boolean p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mOverlayMode:Z

    if-eqz p1, :cond_0

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->updateCurrentContentInsetInOverlayMode()V

    :cond_0
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mExtraPaddingPolicy:Lmiuix/container/ExtraPaddingPolicy;

    const/4 p2, 0x0

    if-eqz p1, :cond_2

    invoke-virtual {p1}, Lmiuix/container/ExtraPaddingPolicy;->isEnable()Z

    move-result p1

    if-eqz p1, :cond_2

    iget-boolean p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mShouldExtraPaddingHorizontalNotifyChanged:Z

    if-eqz p1, :cond_1

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mExtraPaddingObserver:Ljava/util/List;

    if-eqz p1, :cond_1

    iput-boolean p2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mShouldExtraPaddingHorizontalNotifyChanged:Z

    move p1, p2

    :goto_0
    iget-object p3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mExtraPaddingObserver:Ljava/util/List;

    invoke-interface {p3}, Ljava/util/List;->size()I

    move-result p3

    if-ge p1, p3, :cond_1

    iget-object p3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mExtraPaddingObserver:Ljava/util/List;

    invoke-interface {p3, p1}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object p3

    check-cast p3, Lmiuix/container/ExtraPaddingObserver;

    iget p4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mExtraHorizontalPadding:I

    invoke-interface {p3, p4}, Lmiuix/container/ExtraPaddingObserver;->onExtraPaddingChanged(I)V

    add-int/lit8 p1, p1, 0x1

    goto :goto_0

    :cond_1
    iget-boolean p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mExtraPaddingApplyToContentEnable:Z

    if-eqz p1, :cond_2

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mExtraPaddingPolicy:Lmiuix/container/ExtraPaddingPolicy;

    iget-object p3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentView:Landroid/view/View;

    invoke-virtual {p1, p3}, Lmiuix/container/ExtraPaddingPolicy;->applyExtraPadding(Landroid/view/View;)V

    :cond_2
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBar:Lmiuix/appcompat/app/ActionBar;

    if-eqz p1, :cond_3

    iget-boolean p3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mIsInSearchMode:Z

    if-nez p3, :cond_3

    check-cast p1, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;

    invoke-virtual {p1}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->updateCoordinateOffsetView()V

    :cond_3
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;

    move-result-object p1

    iget-object p3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mUserInsetsConfig:Lmiuix/view/WindowInsetsController$InsetsConfig;

    if-nez p3, :cond_7

    invoke-static {p0}, Landroidx/core/view/ViewCompat;->getRootWindowInsets(Landroid/view/View;)Landroidx/core/view/WindowInsetsCompat;

    move-result-object p3

    if-eqz p3, :cond_7

    iget-boolean p4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mLayoutStable:Z

    if-eqz p4, :cond_4

    invoke-static {}, Landroidx/core/view/WindowInsetsCompat$Type;->systemBars()I

    move-result p4

    invoke-static {}, Landroidx/core/view/WindowInsetsCompat$Type;->displayCutout()I

    move-result p5

    or-int/2addr p4, p5

    invoke-virtual {p3, p4}, Landroidx/core/view/WindowInsetsCompat;->getInsetsIgnoringVisibility(I)Landroidx/core/graphics/Insets;

    move-result-object p3

    goto :goto_1

    :cond_4
    invoke-static {}, Landroidx/core/view/WindowInsetsCompat$Type;->systemBars()I

    move-result p4

    invoke-static {}, Landroidx/core/view/WindowInsetsCompat$Type;->displayCutout()I

    move-result p5

    or-int/2addr p4, p5

    invoke-virtual {p3, p4}, Landroidx/core/view/WindowInsetsCompat;->getInsets(I)Landroidx/core/graphics/Insets;

    move-result-object p3

    :goto_1
    invoke-static {p1}, Lmiuix/core/util/EnvStateManager;->getScreenSize(Landroid/content/Context;)Landroid/graphics/Point;

    move-result-object p1

    iget p1, p1, Landroid/graphics/Point;->x:I

    const/4 p4, -0x1

    if-eq p1, p4, :cond_7

    const/4 p4, 0x2

    new-array p4, p4, [I

    invoke-virtual {p0, p4}, Landroid/widget/FrameLayout;->getLocationOnScreen([I)V

    aget p4, p4, p2

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getWidth()I

    move-result p5

    add-int/2addr p5, p4

    sub-int/2addr p1, p5

    iget p5, p3, Landroidx/core/graphics/Insets;->left:I

    const/4 v0, 0x1

    if-lt p4, p5, :cond_5

    move v3, v0

    goto :goto_2

    :cond_5
    move v3, p2

    :goto_2
    iget p3, p3, Landroidx/core/graphics/Insets;->right:I

    if-lt p1, p3, :cond_6

    move v5, v0

    goto :goto_3

    :cond_6
    move v5, p2

    :goto_3
    invoke-static {p0}, Lmiuix/core/util/MiuixUIUtils;->isLayoutHideNavigation(Landroid/view/View;)Z

    move-result v2

    const/4 v4, 0x0

    const/4 v6, 0x0

    const/4 v1, 0x0

    move-object v0, p0

    invoke-direct/range {v0 .. v6}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->applyInternalWindowInsets(ZZZZZZ)V

    :cond_7
    return-void
.end method""",
        'replacement': """.method protected onLayout(ZIIII)V
    .registers 13

    goto :goto_50

    nop

    :goto_0
    invoke-virtual {p0, p4}, Landroid/widget/FrameLayout;->getLocationOnScreen([I)V

    goto :goto_43

    nop

    :goto_1
    iget-object p3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mUserInsetsConfig:Lmiuix/view/WindowInsetsController$InsetsConfig;

    goto :goto_7

    nop

    :goto_2
    invoke-static {p1}, Lmiuix/core/util/EnvStateManager;->getScreenSize(Landroid/content/Context;)Landroid/graphics/Point;

    move-result-object p1

    goto :goto_1f

    nop

    :goto_3
    invoke-static {}, Landroidx/core/view/WindowInsetsCompat$Type;->systemBars()I

    move-result p4

    goto :goto_37

    nop

    :goto_4
    invoke-virtual {p3, p4}, Landroidx/core/view/WindowInsetsCompat;->getInsets(I)Landroidx/core/graphics/Insets;

    move-result-object p3

    :goto_5
    goto :goto_2

    nop

    :goto_6
    const/4 p2, 0x0

    goto :goto_58

    nop

    :goto_7
    if-eqz p3, :cond_0

    goto :goto_30

    :cond_0
    goto :goto_16

    nop

    :goto_8
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBar:Lmiuix/appcompat/app/ActionBar;

    goto :goto_14

    nop

    :goto_9
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->updateCurrentContentInsetInOverlayMode()V

    :goto_a
    goto :goto_17

    nop

    :goto_b
    if-nez p4, :cond_1

    goto :goto_21

    :cond_1
    goto :goto_3

    nop

    :goto_c
    move p1, p2

    :goto_d
    goto :goto_11

    nop

    :goto_e
    goto :goto_4e

    :goto_f
    goto :goto_4d

    nop

    :goto_10
    add-int/2addr p5, p4

    goto :goto_1d

    nop

    :goto_11
    iget-object p3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mExtraPaddingObserver:Ljava/util/List;

    goto :goto_36

    nop

    :goto_12
    goto :goto_d

    :goto_13
    goto :goto_2b

    nop

    :goto_14
    if-nez p1, :cond_2

    goto :goto_3d

    :cond_2
    goto :goto_18

    nop

    :goto_15
    const/4 p4, 0x2

    goto :goto_25

    nop

    :goto_16
    invoke-static {p0}, Landroidx/core/view/ViewCompat;->getRootWindowInsets(Landroid/view/View;)Landroidx/core/view/WindowInsetsCompat;

    move-result-object p3

    goto :goto_56

    nop

    :goto_17
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mExtraPaddingPolicy:Lmiuix/container/ExtraPaddingPolicy;

    goto :goto_6

    nop

    :goto_18
    iget-boolean p3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mIsInSearchMode:Z

    goto :goto_2d

    nop

    :goto_19
    if-ge p4, p5, :cond_3

    goto :goto_29

    :cond_3
    goto :goto_47

    nop

    :goto_1a
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mExtraPaddingObserver:Ljava/util/List;

    goto :goto_46

    nop

    :goto_1b
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getWidth()I

    move-result p5

    goto :goto_10

    nop

    :goto_1c
    invoke-interface {p3, p4}, Lmiuix/container/ExtraPaddingObserver;->onExtraPaddingChanged(I)V

    goto :goto_27

    nop

    :goto_1d
    sub-int/2addr p1, p5

    goto :goto_26

    nop

    :goto_1e
    iget-boolean p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mShouldExtraPaddingHorizontalNotifyChanged:Z

    goto :goto_55

    nop

    :goto_1f
    iget p1, p1, Landroid/graphics/Point;->x:I

    goto :goto_5c

    nop

    :goto_20
    goto :goto_5

    :goto_21
    goto :goto_44

    nop

    :goto_22
    invoke-virtual {p1, p3}, Lmiuix/container/ExtraPaddingPolicy;->applyExtraPadding(Landroid/view/View;)V

    :goto_23
    goto :goto_8

    nop

    :goto_24
    iget-object p3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentView:Landroid/view/View;

    goto :goto_22

    nop

    :goto_25
    new-array p4, p4, [I

    goto :goto_0

    nop

    :goto_26
    iget p5, p3, Landroidx/core/graphics/Insets;->left:I

    goto :goto_42

    nop

    :goto_27
    add-int/lit8 p1, p1, 0x1

    goto :goto_12

    nop

    :goto_28
    goto :goto_53

    :goto_29
    goto :goto_52

    nop

    :goto_2a
    if-ge p1, p3, :cond_4

    goto :goto_f

    :cond_4
    goto :goto_33

    nop

    :goto_2b
    iget-boolean p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mExtraPaddingApplyToContentEnable:Z

    goto :goto_48

    nop

    :goto_2c
    invoke-static {}, Landroidx/core/view/WindowInsetsCompat$Type;->displayCutout()I

    move-result p5

    goto :goto_3a

    nop

    :goto_2d
    if-eqz p3, :cond_5

    goto :goto_3d

    :cond_5
    goto :goto_39

    nop

    :goto_2e
    if-ne p1, p4, :cond_6

    goto :goto_30

    :cond_6
    goto :goto_15

    nop

    :goto_2f
    invoke-direct/range {v0 .. v6}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->applyInternalWindowInsets(ZZZZZZ)V

    :goto_30
    goto :goto_41

    nop

    :goto_31
    move-object v0, p0

    goto :goto_2f

    nop

    :goto_32
    iget p4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mExtraHorizontalPadding:I

    goto :goto_1c

    nop

    :goto_33
    move v5, v0

    goto :goto_e

    nop

    :goto_34
    iget-boolean p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mOverlayMode:Z

    goto :goto_4f

    nop

    :goto_35
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mExtraPaddingPolicy:Lmiuix/container/ExtraPaddingPolicy;

    goto :goto_24

    nop

    :goto_36
    invoke-interface {p3}, Ljava/util/List;->size()I

    move-result p3

    goto :goto_4c

    nop

    :goto_37
    invoke-static {}, Landroidx/core/view/WindowInsetsCompat$Type;->displayCutout()I

    move-result p5

    goto :goto_38

    nop

    :goto_38
    or-int/2addr p4, p5

    goto :goto_3e

    nop

    :goto_39
    check-cast p1, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;

    goto :goto_3c

    nop

    :goto_3a
    or-int/2addr p4, p5

    goto :goto_4

    nop

    :goto_3b
    const/4 v1, 0x0

    goto :goto_31

    nop

    :goto_3c
    invoke-virtual {p1}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->updateCoordinateOffsetView()V

    :goto_3d
    goto :goto_51

    nop

    :goto_3e
    invoke-virtual {p3, p4}, Landroidx/core/view/WindowInsetsCompat;->getInsetsIgnoringVisibility(I)Landroidx/core/graphics/Insets;

    move-result-object p3

    goto :goto_20

    nop

    :goto_3f
    iget-object p3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mExtraPaddingObserver:Ljava/util/List;

    goto :goto_5b

    nop

    :goto_40
    invoke-virtual {p1}, Lmiuix/container/ExtraPaddingPolicy;->isEnable()Z

    move-result p1

    goto :goto_54

    nop

    :goto_41
    return-void

    :goto_42
    const/4 v0, 0x1

    goto :goto_19

    nop

    :goto_43
    aget p4, p4, p2

    goto :goto_1b

    nop

    :goto_44
    invoke-static {}, Landroidx/core/view/WindowInsetsCompat$Type;->systemBars()I

    move-result p4

    goto :goto_2c

    nop

    :goto_45
    iput-boolean p2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mShouldExtraPaddingHorizontalNotifyChanged:Z

    goto :goto_c

    nop

    :goto_46
    if-nez p1, :cond_7

    goto :goto_13

    :cond_7
    goto :goto_45

    nop

    :goto_47
    move v3, v0

    goto :goto_28

    nop

    :goto_48
    if-nez p1, :cond_8

    goto :goto_23

    :cond_8
    goto :goto_35

    nop

    :goto_49
    iget p3, p3, Landroidx/core/graphics/Insets;->right:I

    goto :goto_2a

    nop

    :goto_4a
    invoke-static {p0}, Lmiuix/core/util/MiuixUIUtils;->isLayoutHideNavigation(Landroid/view/View;)Z

    move-result v2

    goto :goto_4b

    nop

    :goto_4b
    const/4 v4, 0x0

    goto :goto_59

    nop

    :goto_4c
    if-lt p1, p3, :cond_9

    goto :goto_13

    :cond_9
    goto :goto_3f

    nop

    :goto_4d
    move v5, p2

    :goto_4e
    goto :goto_4a

    nop

    :goto_4f
    if-nez p1, :cond_a

    goto :goto_a

    :cond_a
    goto :goto_9

    nop

    :goto_50
    invoke-super/range {p0 .. p5}, Landroid/widget/FrameLayout;->onLayout(ZIIII)V

    goto :goto_34

    nop

    :goto_51
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;

    move-result-object p1

    goto :goto_1

    nop

    :goto_52
    move v3, p2

    :goto_53
    goto :goto_49

    nop

    :goto_54
    if-nez p1, :cond_b

    goto :goto_23

    :cond_b
    goto :goto_1e

    nop

    :goto_55
    if-nez p1, :cond_c

    goto :goto_13

    :cond_c
    goto :goto_1a

    nop

    :goto_56
    if-nez p3, :cond_d

    goto :goto_30

    :cond_d
    goto :goto_57

    nop

    :goto_57
    iget-boolean p4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mLayoutStable:Z

    goto :goto_b

    nop

    :goto_58
    if-nez p1, :cond_e

    goto :goto_23

    :cond_e
    goto :goto_40

    nop

    :goto_59
    const/4 v6, 0x0

    goto :goto_3b

    nop

    :goto_5a
    check-cast p3, Lmiuix/container/ExtraPaddingObserver;

    goto :goto_32

    nop

    :goto_5b
    invoke-interface {p3, p1}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object p3

    goto :goto_5a

    nop

    :goto_5c
    const/4 p4, -0x1

    goto :goto_2e

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarOverlayLayout__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mFloatingWindowSize:Lmiuix/appcompat/app/floatingactivity/FloatingABOLayoutSpec;', 'invoke-virtual {v1, v2}, Lmiuix/appcompat/app/floatingactivity/FloatingABOLayoutSpec;->getWidthMeasureSpec(I)I', 'iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mFloatingWindowSize:Lmiuix/appcompat/app/floatingactivity/FloatingABOLayoutSpec;', 'invoke-virtual {v1, v3}, Lmiuix/appcompat/app/floatingactivity/FloatingABOLayoutSpec;->getHeightMeasureSpec(I)I', 'iget-object v6, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentView:Landroid/view/View;', 'iget-object v7, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentMask:Landroid/view/View;', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->getChildCount()I', 'if-ge v9, v1, :cond_2'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 18

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mFloatingWindowSize:Lmiuix/appcompat/app/floatingactivity/FloatingABOLayoutSpec;

    move/from16 v2, p1

    invoke-virtual {v1, v2}, Lmiuix/appcompat/app/floatingactivity/FloatingABOLayoutSpec;->getWidthMeasureSpec(I)I

    move-result v2

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mFloatingWindowSize:Lmiuix/appcompat/app/floatingactivity/FloatingABOLayoutSpec;

    move/from16 v3, p2

    invoke-virtual {v1, v3}, Lmiuix/appcompat/app/floatingactivity/FloatingABOLayoutSpec;->getHeightMeasureSpec(I)I

    move-result v4

    iget-object v6, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentView:Landroid/view/View;

    iget-object v7, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentMask:Landroid/view/View;

    const/4 v8, 0x0

    move v9, v8

    move v10, v9

    move v11, v10

    move v12, v11

    :goto_0
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getChildCount()I

    move-result v1

    const/16 v3, 0x8

    if-ge v9, v1, :cond_2

    invoke-virtual {p0, v9}, Landroid/widget/FrameLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v1

    if-eq v1, v6, :cond_0

    if-eq v1, v7, :cond_0

    invoke-virtual {v1}, Landroid/view/View;->getVisibility()I

    move-result v5

    if-ne v5, v3, :cond_1

    :cond_0
    move v13, v2

    move v14, v4

    goto :goto_1

    :cond_1
    const/4 v3, 0x0

    const/4 v5, 0x0

    move-object v0, p0

    invoke-virtual/range {v0 .. v5}, Landroid/widget/FrameLayout;->measureChildWithMargins(Landroid/view/View;IIII)V

    move v13, v2

    move v14, v4

    invoke-virtual {v1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v2

    check-cast v2, Landroid/widget/FrameLayout$LayoutParams;

    invoke-virtual {v1}, Landroid/view/View;->getMeasuredWidth()I

    move-result v3

    iget v4, v2, Landroid/widget/FrameLayout$LayoutParams;->leftMargin:I

    add-int/2addr v3, v4

    iget v4, v2, Landroid/widget/FrameLayout$LayoutParams;->rightMargin:I

    add-int/2addr v3, v4

    invoke-static {v10, v3}, Ljava/lang/Math;->max(II)I

    move-result v10

    invoke-virtual {v1}, Landroid/view/View;->getMeasuredHeight()I

    move-result v3

    iget v4, v2, Landroid/widget/FrameLayout$LayoutParams;->topMargin:I

    add-int/2addr v3, v4

    iget v2, v2, Landroid/widget/FrameLayout$LayoutParams;->bottomMargin:I

    add-int/2addr v3, v2

    invoke-static {v11, v3}, Ljava/lang/Math;->max(II)I

    move-result v11

    invoke-virtual {v1}, Landroid/view/View;->getMeasuredState()I

    move-result v1

    invoke-static {v12, v1}, Landroid/widget/FrameLayout;->combineMeasuredStates(II)I

    move-result v12

    :goto_1
    add-int/lit8 v9, v9, 0x1

    move v2, v13

    move v4, v14

    goto :goto_0

    :cond_2
    move v13, v2

    move v14, v4

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarTop:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    if-eqz v1, :cond_3

    invoke-virtual {v1}, Landroid/widget/FrameLayout;->getVisibility()I

    move-result v1

    if-eq v1, v3, :cond_3

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarTop:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    invoke-virtual {v1}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result v1

    goto :goto_2

    :cond_3
    move v1, v8

    :goto_2
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->getBottomInset()I

    move-result v2

    iget-object v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    if-eqz v3, :cond_4

    invoke-virtual {v3}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->isSplitActionBar()Z

    move-result v3

    if-eqz v3, :cond_4

    move v3, v2

    goto :goto_3

    :cond_4
    move v3, v8

    :goto_3
    iget-object v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mInnerInsets:Landroid/graphics/Rect;

    iget-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseInnerInsets:Landroid/graphics/Rect;

    invoke-virtual {v4, v5}, Landroid/graphics/Rect;->set(Landroid/graphics/Rect;)V

    iget-object v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentInsets:Landroid/graphics/Rect;

    iget-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseContentInsets:Landroid/graphics/Rect;

    invoke-virtual {v4, v5}, Landroid/graphics/Rect;->set(Landroid/graphics/Rect;)V

    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->isLayoutHideNavigation()Z

    move-result v4

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->isTranslucentStatus()Z

    move-result v5

    if-eqz v5, :cond_5

    if-lez v1, :cond_5

    iget-object v9, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentInsets:Landroid/graphics/Rect;

    iput v8, v9, Landroid/graphics/Rect;->top:I

    :cond_5
    iget-boolean v9, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mOverlayMode:Z

    if-nez v9, :cond_6

    iget-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentInsets:Landroid/graphics/Rect;

    iget v9, v5, Landroid/graphics/Rect;->top:I

    add-int/2addr v9, v1

    iput v9, v5, Landroid/graphics/Rect;->top:I

    iget v1, v5, Landroid/graphics/Rect;->bottom:I

    add-int/2addr v1, v3

    iput v1, v5, Landroid/graphics/Rect;->bottom:I

    goto :goto_5

    :cond_6
    if-eqz v5, :cond_7

    if-lez v1, :cond_8

    iget-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mInnerInsets:Landroid/graphics/Rect;

    iput v1, v5, Landroid/graphics/Rect;->top:I

    goto :goto_4

    :cond_7
    iget-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mInnerInsets:Landroid/graphics/Rect;

    iget v9, v5, Landroid/graphics/Rect;->top:I

    add-int/2addr v9, v1

    iput v9, v5, Landroid/graphics/Rect;->top:I

    :cond_8
    :goto_4
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mInnerInsets:Landroid/graphics/Rect;

    iget v5, v1, Landroid/graphics/Rect;->bottom:I

    add-int/2addr v5, v3

    iput v5, v1, Landroid/graphics/Rect;->bottom:I

    :goto_5
    iget-boolean v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mIsFloatingTheme:Z

    const/4 v9, 0x2

    if-eqz v1, :cond_9

    iget-boolean v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mIsFloatingWindow:Z

    if-nez v1, :cond_c

    :cond_9
    if-eqz v4, :cond_c

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getResources()Landroid/content/res/Resources;

    move-result-object v1

    invoke-virtual {v1}, Landroid/content/res/Resources;->getConfiguration()Landroid/content/res/Configuration;

    move-result-object v1

    iget v1, v1, Landroid/content/res/Configuration;->orientation:I

    if-ne v1, v9, :cond_a

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentInsets:Landroid/graphics/Rect;

    iput v8, v1, Landroid/graphics/Rect;->right:I

    iput v8, v1, Landroid/graphics/Rect;->left:I

    :cond_a
    if-nez v2, :cond_c

    iget-boolean v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mSqueezeContentByIme:Z

    if-eqz v1, :cond_b

    iget v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mImeInsetBottom:I

    if-gtz v1, :cond_c

    :cond_b
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentInsets:Landroid/graphics/Rect;

    iput v8, v1, Landroid/graphics/Rect;->bottom:I

    :cond_c
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->isBottomAnimating()Z

    move-result v1

    if-nez v1, :cond_d

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentInsets:Landroid/graphics/Rect;

    const/4 v5, 0x1

    move-object v1, v6

    const/4 v6, 0x1

    const/4 v3, 0x1

    const/4 v4, 0x1

    move-object v0, p0

    invoke-direct/range {v0 .. v6}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->applyInsetsByMargin(Landroid/view/View;Landroid/graphics/Rect;ZZZZ)Z

    const/4 v2, 0x0

    iput-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mAnimateContentMarginBottomInsets:Landroid/graphics/Rect;

    goto :goto_6

    :cond_d
    move-object v1, v6

    :goto_6
    iget-boolean v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mOverlayMode:Z

    if-nez v2, :cond_e

    invoke-virtual {v1}, Landroid/view/View;->getPaddingLeft()I

    move-result v2

    invoke-virtual {v1}, Landroid/view/View;->getPaddingRight()I

    move-result v3

    invoke-virtual {v1}, Landroid/view/View;->getPaddingBottom()I

    move-result v4

    invoke-virtual {v1, v2, v8, v3, v4}, Landroid/view/View;->setPadding(IIII)V

    :cond_e
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mLastInnerInsets:Landroid/graphics/Rect;

    iget-object v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mInnerInsets:Landroid/graphics/Rect;

    invoke-virtual {v2, v3}, Landroid/graphics/Rect;->equals(Ljava/lang/Object;)Z

    move-result v2

    if-eqz v2, :cond_f

    iget-boolean v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mRequestFitSystemWindow:Z

    if-eqz v2, :cond_10

    :cond_f
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mLastInnerInsets:Landroid/graphics/Rect;

    iget-object v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mInnerInsets:Landroid/graphics/Rect;

    invoke-virtual {v2, v3}, Landroid/graphics/Rect;->set(Landroid/graphics/Rect;)V

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseInnerInsets:Landroid/graphics/Rect;

    invoke-super {p0, v2}, Landroid/widget/FrameLayout;->fitSystemWindows(Landroid/graphics/Rect;)Z

    iput-boolean v8, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mRequestFitSystemWindow:Z

    :cond_10
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->isTranslucentStatus()Z

    move-result v2

    if-eqz v2, :cond_12

    iget-boolean v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentAutoFitSystemWindow:Z

    if-eqz v2, :cond_12

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentHeaderBackground:Landroid/graphics/drawable/Drawable;

    if-eqz v2, :cond_11

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getRight()I

    move-result v3

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getLeft()I

    move-result v4

    sub-int/2addr v3, v4

    iget-object v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseContentInsets:Landroid/graphics/Rect;

    iget v4, v4, Landroid/graphics/Rect;->top:I

    invoke-virtual {v2, v8, v8, v3, v4}, Landroid/graphics/drawable/Drawable;->setBounds(IIII)V

    goto :goto_7

    :cond_11
    const v2, 0x1020002

    invoke-virtual {p0, v2}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v2

    check-cast v2, Landroid/view/ViewGroup;

    if-eqz v2, :cond_12

    invoke-virtual {v2}, Landroid/view/ViewGroup;->getChildCount()I

    move-result v3

    const/4 v4, 0x1

    if-ne v3, v4, :cond_12

    invoke-virtual {v2, v8}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;

    move-result-object v2

    invoke-virtual {v2}, Landroid/view/View;->getPaddingLeft()I

    move-result v3

    invoke-virtual {v2}, Landroid/view/View;->getPaddingRight()I

    move-result v4

    invoke-virtual {v2}, Landroid/view/View;->getPaddingBottom()I

    move-result v5

    invoke-virtual {v2, v3, v8, v4, v5}, Landroid/view/View;->setPadding(IIII)V

    :cond_12
    :goto_7
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mExtraPaddingPolicy:Lmiuix/container/ExtraPaddingPolicy;

    if-eqz v2, :cond_13

    invoke-virtual {v2}, Lmiuix/container/ExtraPaddingPolicy;->isEnable()Z

    move-result v2

    if-eqz v2, :cond_13

    invoke-static {v13}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v2

    invoke-static {v14}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v3

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;

    move-result-object v4

    iget-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mExtraPaddingPolicy:Lmiuix/container/ExtraPaddingPolicy;

    invoke-direct {p0, v4, v5, v2, v3}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->updateExtraPaddingHorizontal(Landroid/content/Context;Lmiuix/container/ExtraPaddingPolicy;II)V

    iget-boolean v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mExtraPaddingApplyToContentEnable:Z

    if-eqz v3, :cond_13

    invoke-static {v13}, Landroid/view/View$MeasureSpec;->getMode(I)I

    move-result v3

    iget v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mExtraHorizontalPadding:I

    mul-int/2addr v4, v9

    sub-int/2addr v2, v4

    invoke-static {v2, v3}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v2

    goto :goto_8

    :cond_13
    move v2, v13

    :goto_8
    const/4 v3, 0x0

    const/4 v5, 0x0

    move-object v0, p0

    move v4, v14

    invoke-virtual/range {v0 .. v5}, Landroid/widget/FrameLayout;->measureChildWithMargins(Landroid/view/View;IIII)V

    invoke-virtual {v1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v2

    check-cast v2, Landroid/widget/FrameLayout$LayoutParams;

    invoke-virtual {v1}, Landroid/view/View;->getMeasuredWidth()I

    move-result v3

    iget v4, v2, Landroid/widget/FrameLayout$LayoutParams;->leftMargin:I

    add-int/2addr v3, v4

    iget v4, v2, Landroid/widget/FrameLayout$LayoutParams;->rightMargin:I

    add-int/2addr v3, v4

    invoke-static {v10, v3}, Ljava/lang/Math;->max(II)I

    move-result v8

    invoke-virtual {v1}, Landroid/view/View;->getMeasuredHeight()I

    move-result v3

    iget v4, v2, Landroid/widget/FrameLayout$LayoutParams;->topMargin:I

    add-int/2addr v3, v4

    iget v2, v2, Landroid/widget/FrameLayout$LayoutParams;->bottomMargin:I

    add-int/2addr v3, v2

    invoke-static {v11, v3}, Ljava/lang/Math;->max(II)I

    move-result v9

    invoke-virtual {v1}, Landroid/view/View;->getMeasuredState()I

    move-result v1

    invoke-static {v12, v1}, Landroid/widget/FrameLayout;->combineMeasuredStates(II)I

    move-result v10

    if-eqz v7, :cond_14

    invoke-virtual {v7}, Landroid/view/View;->getVisibility()I

    move-result v1

    if-nez v1, :cond_14

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentMaskInsets:Landroid/graphics/Rect;

    const/4 v5, 0x1

    const/4 v6, 0x1

    const/4 v3, 0x1

    const/4 v4, 0x0

    move-object v0, p0

    move-object v1, v7

    invoke-direct/range {v0 .. v6}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->applyInsetsByMargin(Landroid/view/View;Landroid/graphics/Rect;ZZZZ)Z

    const/4 v3, 0x0

    const/4 v5, 0x0

    move v2, v13

    move v4, v14

    invoke-virtual/range {v0 .. v5}, Landroid/widget/FrameLayout;->measureChildWithMargins(Landroid/view/View;IIII)V

    goto :goto_9

    :cond_14
    move v2, v13

    move v4, v14

    :goto_9
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingLeft()I

    move-result v1

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingRight()I

    move-result v3

    add-int/2addr v1, v3

    add-int/2addr v8, v1

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingTop()I

    move-result v1

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingBottom()I

    move-result v3

    add-int/2addr v1, v3

    add-int/2addr v9, v1

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getSuggestedMinimumHeight()I

    move-result v1

    invoke-static {v9, v1}, Ljava/lang/Math;->max(II)I

    move-result v1

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getSuggestedMinimumWidth()I

    move-result v3

    invoke-static {v8, v3}, Ljava/lang/Math;->max(II)I

    move-result v3

    invoke-static {v3, v2, v10}, Landroid/widget/FrameLayout;->resolveSizeAndState(III)I

    move-result v2

    shl-int/lit8 v3, v10, 0x10

    invoke-static {v1, v4, v3}, Landroid/widget/FrameLayout;->resolveSizeAndState(III)I

    move-result v1

    invoke-virtual {p0, v2, v1}, Landroid/widget/FrameLayout;->setMeasuredDimension(II)V

    new-instance v1, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout$$ExternalSyntheticLambda0;

    invoke-direct {v1, p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout$$ExternalSyntheticLambda0;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;)V

    invoke-virtual {p0, v1}, Landroid/widget/FrameLayout;->post(Ljava/lang/Runnable;)Z

    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 18

    goto :goto_5

    nop

    :goto_0
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentHeaderBackground:Landroid/graphics/drawable/Drawable;

    goto :goto_63

    nop

    :goto_1
    iget v1, v1, Landroid/content/res/Configuration;->orientation:I

    goto :goto_c

    nop

    :goto_2
    const/4 v5, 0x1

    goto :goto_a3

    nop

    :goto_3
    add-int/2addr v9, v1

    goto :goto_59

    nop

    :goto_4
    iget v4, v2, Landroid/widget/FrameLayout$LayoutParams;->leftMargin:I

    goto :goto_2a

    nop

    :goto_5
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mFloatingWindowSize:Lmiuix/appcompat/app/floatingactivity/FloatingABOLayoutSpec;

    goto :goto_89

    nop

    :goto_6
    if-nez v1, :cond_0

    goto :goto_ea

    :cond_0
    goto :goto_2f

    nop

    :goto_7
    if-eqz v9, :cond_1

    goto :goto_102

    :cond_1
    goto :goto_b2

    nop

    :goto_8
    invoke-virtual {v1, v2, v8, v3, v4}, Landroid/view/View;->setPadding(IIII)V

    :goto_9
    goto :goto_31

    nop

    :goto_a
    const/4 v9, 0x2

    goto :goto_6

    nop

    :goto_b
    add-int/2addr v3, v4

    goto :goto_98

    nop

    :goto_c
    if-eq v1, v9, :cond_2

    goto :goto_5d

    :cond_2
    goto :goto_a1

    nop

    :goto_d
    iget-boolean v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mRequestFitSystemWindow:Z

    goto :goto_4d

    nop

    :goto_e
    move v4, v14

    :goto_f
    goto :goto_60

    nop

    :goto_10
    if-ne v1, v3, :cond_3

    goto :goto_25

    :cond_3
    goto :goto_11d

    nop

    :goto_11
    check-cast v2, Landroid/widget/FrameLayout$LayoutParams;

    goto :goto_ad

    nop

    :goto_12
    add-int/2addr v3, v2

    goto :goto_10e

    nop

    :goto_13
    iget-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseInnerInsets:Landroid/graphics/Rect;

    goto :goto_5f

    nop

    :goto_14
    goto :goto_e3

    :goto_15
    goto :goto_c5

    nop

    :goto_16
    invoke-virtual {v7}, Landroid/view/View;->getVisibility()I

    move-result v1

    goto :goto_a4

    nop

    :goto_17
    move v2, v13

    goto :goto_e

    nop

    :goto_18
    iget-boolean v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mIsFloatingTheme:Z

    goto :goto_a

    nop

    :goto_19
    invoke-virtual {p0, v1}, Landroid/widget/FrameLayout;->post(Ljava/lang/Runnable;)Z

    goto :goto_41

    nop

    :goto_1a
    check-cast v2, Landroid/widget/FrameLayout$LayoutParams;

    goto :goto_80

    nop

    :goto_1b
    move v11, v10

    goto :goto_f2

    nop

    :goto_1c
    invoke-virtual {v2}, Landroid/view/View;->getPaddingRight()I

    move-result v4

    goto :goto_30

    nop

    :goto_1d
    iget v4, v2, Landroid/widget/FrameLayout$LayoutParams;->topMargin:I

    goto :goto_26

    nop

    :goto_1e
    invoke-virtual {v1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v2

    goto :goto_11

    nop

    :goto_1f
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->isBottomAnimating()Z

    move-result v1

    goto :goto_7a

    nop

    :goto_20
    invoke-static {v10, v3}, Ljava/lang/Math;->max(II)I

    move-result v10

    goto :goto_7f

    nop

    :goto_21
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getChildCount()I

    move-result v1

    goto :goto_64

    nop

    :goto_22
    invoke-direct {p0, v4, v5, v2, v3}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->updateExtraPaddingHorizontal(Landroid/content/Context;Lmiuix/container/ExtraPaddingPolicy;II)V

    goto :goto_d6

    nop

    :goto_23
    if-nez v5, :cond_4

    goto :goto_29

    :cond_4
    goto :goto_cf

    nop

    :goto_24
    goto :goto_95

    :goto_25
    goto :goto_94

    nop

    :goto_26
    add-int/2addr v3, v4

    goto :goto_af

    nop

    :goto_27
    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->isLayoutHideNavigation()Z

    move-result v4

    goto :goto_37

    nop

    :goto_28
    iput v8, v9, Landroid/graphics/Rect;->top:I

    :goto_29
    goto :goto_c7

    nop

    :goto_2a
    add-int/2addr v3, v4

    goto :goto_6a

    nop

    :goto_2b
    move v14, v4

    goto :goto_9a

    nop

    :goto_2c
    iget v2, v2, Landroid/widget/FrameLayout$LayoutParams;->bottomMargin:I

    goto :goto_12

    nop

    :goto_2d
    move v10, v9

    goto :goto_1b

    nop

    :goto_2e
    invoke-virtual {p0, v2}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v2

    goto :goto_aa

    nop

    :goto_2f
    iget-boolean v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mIsFloatingWindow:Z

    goto :goto_e9

    nop

    :goto_30
    invoke-virtual {v2}, Landroid/view/View;->getPaddingBottom()I

    move-result v5

    goto :goto_e2

    nop

    :goto_31
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mLastInnerInsets:Landroid/graphics/Rect;

    goto :goto_e7

    nop

    :goto_32
    invoke-static {v12, v1}, Landroid/widget/FrameLayout;->combineMeasuredStates(II)I

    move-result v12

    :goto_33
    goto :goto_39

    nop

    :goto_34
    invoke-static {v12, v1}, Landroid/widget/FrameLayout;->combineMeasuredStates(II)I

    move-result v10

    goto :goto_108

    nop

    :goto_35
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentInsets:Landroid/graphics/Rect;

    goto :goto_2

    nop

    :goto_36
    if-nez v2, :cond_5

    goto :goto_4e

    :cond_5
    goto :goto_d

    nop

    :goto_37
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->isTranslucentStatus()Z

    move-result v5

    goto :goto_23

    nop

    :goto_38
    invoke-virtual/range {v0 .. v5}, Landroid/widget/FrameLayout;->measureChildWithMargins(Landroid/view/View;IIII)V

    goto :goto_65

    nop

    :goto_39
    add-int/lit8 v9, v9, 0x1

    goto :goto_8b

    nop

    :goto_3a
    add-int/2addr v1, v3

    goto :goto_85

    nop

    :goto_3b
    goto :goto_f3

    :goto_3c
    goto :goto_10a

    nop

    :goto_3d
    invoke-virtual {v1}, Landroid/view/View;->getMeasuredState()I

    move-result v1

    goto :goto_32

    nop

    :goto_3e
    add-int/2addr v8, v1

    goto :goto_119

    nop

    :goto_3f
    iget-object v6, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentView:Landroid/view/View;

    goto :goto_104

    nop

    :goto_40
    const/4 v6, 0x1

    goto :goto_de

    nop

    :goto_41
    return-void

    :goto_42
    const/4 v4, 0x1

    goto :goto_106

    nop

    :goto_43
    move v3, v2

    goto :goto_ed

    nop

    :goto_44
    invoke-virtual {v1}, Landroid/content/res/Resources;->getConfiguration()Landroid/content/res/Configuration;

    move-result-object v1

    goto :goto_1

    nop

    :goto_45
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getSuggestedMinimumWidth()I

    move-result v3

    goto :goto_62

    nop

    :goto_46
    move v14, v4

    goto :goto_1e

    nop

    :goto_47
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->isTranslucentStatus()Z

    move-result v2

    goto :goto_88

    nop

    :goto_48
    invoke-virtual {p0, v2, v1}, Landroid/widget/FrameLayout;->setMeasuredDimension(II)V

    goto :goto_fe

    nop

    :goto_49
    iput v8, v1, Landroid/graphics/Rect;->right:I

    goto :goto_5c

    nop

    :goto_4a
    invoke-direct/range {v0 .. v6}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->applyInsetsByMargin(Landroid/view/View;Landroid/graphics/Rect;ZZZZ)Z

    goto :goto_ff

    nop

    :goto_4b
    invoke-virtual {v2, v3}, Landroid/graphics/Rect;->equals(Ljava/lang/Object;)Z

    move-result v2

    goto :goto_36

    nop

    :goto_4c
    invoke-virtual/range {v0 .. v5}, Landroid/widget/FrameLayout;->measureChildWithMargins(Landroid/view/View;IIII)V

    goto :goto_100

    nop

    :goto_4d
    if-nez v2, :cond_6

    goto :goto_b6

    :cond_6
    :goto_4e
    goto :goto_8e

    nop

    :goto_4f
    add-int/2addr v3, v4

    goto :goto_20

    nop

    :goto_50
    invoke-virtual {v1}, Landroid/view/View;->getMeasuredState()I

    move-result v1

    goto :goto_34

    nop

    :goto_51
    iput v8, v1, Landroid/graphics/Rect;->bottom:I

    :goto_52
    goto :goto_1f

    nop

    :goto_53
    const/4 v5, 0x1

    goto :goto_40

    nop

    :goto_54
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mInnerInsets:Landroid/graphics/Rect;

    goto :goto_d0

    nop

    :goto_55
    invoke-virtual {v2, v3}, Landroid/graphics/Rect;->set(Landroid/graphics/Rect;)V

    goto :goto_e5

    nop

    :goto_56
    if-nez v2, :cond_7

    goto :goto_90

    :cond_7
    goto :goto_113

    nop

    :goto_57
    const/4 v3, 0x0

    goto :goto_c8

    nop

    :goto_58
    iget-boolean v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentAutoFitSystemWindow:Z

    goto :goto_be

    nop

    :goto_59
    iput v9, v5, Landroid/graphics/Rect;->top:I

    :goto_5a
    goto :goto_54

    nop

    :goto_5b
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingRight()I

    move-result v3

    goto :goto_f8

    nop

    :goto_5c
    iput v8, v1, Landroid/graphics/Rect;->left:I

    :goto_5d
    goto :goto_111

    nop

    :goto_5e
    if-nez v3, :cond_8

    goto :goto_ee

    :cond_8
    goto :goto_43

    nop

    :goto_5f
    invoke-virtual {v4, v5}, Landroid/graphics/Rect;->set(Landroid/graphics/Rect;)V

    goto :goto_f6

    nop

    :goto_60
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingLeft()I

    move-result v1

    goto :goto_5b

    nop

    :goto_61
    invoke-virtual {v2}, Landroid/view/ViewGroup;->getChildCount()I

    move-result v3

    goto :goto_42

    nop

    :goto_62
    invoke-static {v8, v3}, Ljava/lang/Math;->max(II)I

    move-result v3

    goto :goto_a7

    nop

    :goto_63
    if-nez v2, :cond_9

    goto :goto_15

    :cond_9
    goto :goto_66

    nop

    :goto_64
    const/16 v3, 0x8

    goto :goto_112

    nop

    :goto_65
    move v13, v2

    goto :goto_46

    nop

    :goto_66
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getRight()I

    move-result v3

    goto :goto_83

    nop

    :goto_67
    move v4, v14

    goto :goto_4c

    nop

    :goto_68
    goto :goto_5a

    :goto_69
    goto :goto_a9

    nop

    :goto_6a
    iget v4, v2, Landroid/widget/FrameLayout$LayoutParams;->rightMargin:I

    goto :goto_b

    nop

    :goto_6b
    invoke-virtual {v2}, Landroid/view/View;->getPaddingLeft()I

    move-result v3

    goto :goto_1c

    nop

    :goto_6c
    iget v9, v5, Landroid/graphics/Rect;->top:I

    goto :goto_11b

    nop

    :goto_6d
    const/4 v4, 0x0

    goto :goto_11c

    nop

    :goto_6e
    move v13, v2

    goto :goto_dc

    nop

    :goto_6f
    invoke-virtual/range {v0 .. v5}, Landroid/widget/FrameLayout;->measureChildWithMargins(Landroid/view/View;IIII)V

    goto :goto_a5

    nop

    :goto_70
    invoke-static {v13}, Landroid/view/View$MeasureSpec;->getMode(I)I

    move-result v3

    goto :goto_76

    nop

    :goto_71
    sub-int/2addr v3, v4

    goto :goto_82

    nop

    :goto_72
    iget-boolean v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mSqueezeContentByIme:Z

    goto :goto_da

    nop

    :goto_73
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->getBottomInset()I

    move-result v2

    goto :goto_b1

    nop

    :goto_74
    if-nez v3, :cond_a

    goto :goto_90

    :cond_a
    goto :goto_70

    nop

    :goto_75
    invoke-virtual {v1, v3}, Lmiuix/appcompat/app/floatingactivity/FloatingABOLayoutSpec;->getHeightMeasureSpec(I)I

    move-result v4

    goto :goto_3f

    nop

    :goto_76
    iget v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mExtraHorizontalPadding:I

    goto :goto_c3

    nop

    :goto_77
    move v3, v8

    :goto_78
    goto :goto_118

    nop

    :goto_79
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingBottom()I

    move-result v3

    goto :goto_3a

    nop

    :goto_7a
    if-eqz v1, :cond_b

    goto :goto_10c

    :cond_b
    goto :goto_35

    nop

    :goto_7b
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;

    move-result-object v4

    goto :goto_9c

    nop

    :goto_7c
    if-ne v1, v6, :cond_c

    goto :goto_7e

    :cond_c
    goto :goto_f5

    nop

    :goto_7d
    if-eq v5, v3, :cond_d

    goto :goto_9e

    :cond_d
    :goto_7e
    goto :goto_6e

    nop

    :goto_7f
    invoke-virtual {v1}, Landroid/view/View;->getMeasuredHeight()I

    move-result v3

    goto :goto_1d

    nop

    :goto_80
    invoke-virtual {v1}, Landroid/view/View;->getMeasuredWidth()I

    move-result v3

    goto :goto_4

    nop

    :goto_81
    if-gtz v1, :cond_e

    goto :goto_5a

    :cond_e
    goto :goto_b0

    nop

    :goto_82
    iget-object v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseContentInsets:Landroid/graphics/Rect;

    goto :goto_d8

    nop

    :goto_83
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getLeft()I

    move-result v4

    goto :goto_71

    nop

    :goto_84
    move v4, v14

    goto :goto_6f

    nop

    :goto_85
    add-int/2addr v9, v1

    goto :goto_cb

    nop

    :goto_86
    add-int/2addr v1, v3

    goto :goto_115

    nop

    :goto_87
    iget v4, v2, Landroid/widget/FrameLayout$LayoutParams;->rightMargin:I

    goto :goto_4f

    nop

    :goto_88
    if-nez v2, :cond_f

    goto :goto_e3

    :cond_f
    goto :goto_58

    nop

    :goto_89
    move/from16 v2, p1

    goto :goto_ce

    nop

    :goto_8a
    iget v1, v5, Landroid/graphics/Rect;->bottom:I

    goto :goto_86

    nop

    :goto_8b
    move v2, v13

    goto :goto_9f

    nop

    :goto_8c
    invoke-virtual {v2, v8}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;

    move-result-object v2

    goto :goto_6b

    nop

    :goto_8d
    iget v4, v2, Landroid/widget/FrameLayout$LayoutParams;->leftMargin:I

    goto :goto_c6

    nop

    :goto_8e
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mLastInnerInsets:Landroid/graphics/Rect;

    goto :goto_df

    nop

    :goto_8f
    goto :goto_97

    :goto_90
    goto :goto_96

    nop

    :goto_91
    invoke-virtual {v1}, Landroid/view/View;->getPaddingRight()I

    move-result v3

    goto :goto_ae

    nop

    :goto_92
    invoke-virtual {v1}, Landroid/widget/FrameLayout;->getVisibility()I

    move-result v1

    goto :goto_10

    nop

    :goto_93
    invoke-virtual {p0, v9}, Landroid/widget/FrameLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v1

    goto :goto_7c

    nop

    :goto_94
    move v1, v8

    :goto_95
    goto :goto_73

    nop

    :goto_96
    move v2, v13

    :goto_97
    goto :goto_9b

    nop

    :goto_98
    invoke-static {v10, v3}, Ljava/lang/Math;->max(II)I

    move-result v8

    goto :goto_cc

    nop

    :goto_99
    invoke-virtual {v1}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result v1

    goto :goto_24

    nop

    :goto_9a
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarTop:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_a8

    nop

    :goto_9b
    const/4 v3, 0x0

    goto :goto_f1

    nop

    :goto_9c
    iget-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mExtraPaddingPolicy:Lmiuix/container/ExtraPaddingPolicy;

    goto :goto_22

    nop

    :goto_9d
    goto :goto_33

    :goto_9e
    goto :goto_bf

    nop

    :goto_9f
    move v4, v14

    goto :goto_3b

    nop

    :goto_a0
    invoke-static {v1, v4, v3}, Landroid/widget/FrameLayout;->resolveSizeAndState(III)I

    move-result v1

    goto :goto_48

    nop

    :goto_a1
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentInsets:Landroid/graphics/Rect;

    goto :goto_49

    nop

    :goto_a2
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getResources()Landroid/content/res/Resources;

    move-result-object v1

    goto :goto_44

    nop

    :goto_a3
    move-object v1, v6

    goto :goto_fa

    nop

    :goto_a4
    if-eqz v1, :cond_10

    goto :goto_a6

    :cond_10
    goto :goto_f4

    nop

    :goto_a5
    goto :goto_f

    :goto_a6
    goto :goto_17

    nop

    :goto_a7
    invoke-static {v3, v2, v10}, Landroid/widget/FrameLayout;->resolveSizeAndState(III)I

    move-result v2

    goto :goto_ec

    nop

    :goto_a8
    if-nez v1, :cond_11

    goto :goto_25

    :cond_11
    goto :goto_92

    nop

    :goto_a9
    iget-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mInnerInsets:Landroid/graphics/Rect;

    goto :goto_d4

    nop

    :goto_aa
    check-cast v2, Landroid/view/ViewGroup;

    goto :goto_c9

    nop

    :goto_ab
    const/4 v5, 0x0

    goto :goto_cd

    nop

    :goto_ac
    iget v4, v2, Landroid/widget/FrameLayout$LayoutParams;->topMargin:I

    goto :goto_11e

    nop

    :goto_ad
    invoke-virtual {v1}, Landroid/view/View;->getMeasuredWidth()I

    move-result v3

    goto :goto_8d

    nop

    :goto_ae
    invoke-virtual {v1}, Landroid/view/View;->getPaddingBottom()I

    move-result v4

    goto :goto_8

    nop

    :goto_af
    iget v2, v2, Landroid/widget/FrameLayout$LayoutParams;->bottomMargin:I

    goto :goto_d3

    nop

    :goto_b0
    iget-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mInnerInsets:Landroid/graphics/Rect;

    goto :goto_e6

    nop

    :goto_b1
    iget-object v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_109

    nop

    :goto_b2
    iget-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentInsets:Landroid/graphics/Rect;

    goto :goto_6c

    nop

    :goto_b3
    invoke-direct {v1, p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout$$ExternalSyntheticLambda0;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;)V

    goto :goto_19

    nop

    :goto_b4
    invoke-static {v2, v3}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v2

    goto :goto_8f

    nop

    :goto_b5
    iput-boolean v8, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mRequestFitSystemWindow:Z

    :goto_b6
    goto :goto_47

    nop

    :goto_b7
    sub-int/2addr v2, v4

    goto :goto_b4

    nop

    :goto_b8
    invoke-virtual {v1}, Landroid/view/View;->getVisibility()I

    move-result v5

    goto :goto_7d

    nop

    :goto_b9
    move-object v1, v6

    :goto_ba
    goto :goto_103

    nop

    :goto_bb
    iget-object v9, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentInsets:Landroid/graphics/Rect;

    goto :goto_28

    nop

    :goto_bc
    if-nez v4, :cond_12

    goto :goto_52

    :cond_12
    goto :goto_a2

    nop

    :goto_bd
    iput v9, v5, Landroid/graphics/Rect;->top:I

    goto :goto_8a

    nop

    :goto_be
    if-nez v2, :cond_13

    goto :goto_e3

    :cond_13
    goto :goto_0

    nop

    :goto_bf
    const/4 v3, 0x0

    goto :goto_ab

    nop

    :goto_c0
    invoke-static {v13}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v2

    goto :goto_107

    nop

    :goto_c1
    iput v5, v1, Landroid/graphics/Rect;->bottom:I

    :goto_c2
    goto :goto_18

    nop

    :goto_c3
    mul-int/2addr v4, v9

    goto :goto_b7

    nop

    :goto_c4
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mExtraPaddingPolicy:Lmiuix/container/ExtraPaddingPolicy;

    goto :goto_56

    nop

    :goto_c5
    const v2, 0x1020002

    goto :goto_2e

    nop

    :goto_c6
    add-int/2addr v3, v4

    goto :goto_87

    nop

    :goto_c7
    iget-boolean v9, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mOverlayMode:Z

    goto :goto_7

    nop

    :goto_c8
    const/4 v5, 0x0

    goto :goto_f9

    nop

    :goto_c9
    if-nez v2, :cond_14

    goto :goto_e3

    :cond_14
    goto :goto_61

    nop

    :goto_ca
    const/4 v4, 0x1

    goto :goto_10f

    nop

    :goto_cb
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getSuggestedMinimumHeight()I

    move-result v1

    goto :goto_105

    nop

    :goto_cc
    invoke-virtual {v1}, Landroid/view/View;->getMeasuredHeight()I

    move-result v3

    goto :goto_ac

    nop

    :goto_cd
    move-object v0, p0

    goto :goto_38

    nop

    :goto_ce
    invoke-virtual {v1, v2}, Lmiuix/appcompat/app/floatingactivity/FloatingABOLayoutSpec;->getWidthMeasureSpec(I)I

    move-result v2

    goto :goto_e1

    nop

    :goto_cf
    if-gtz v1, :cond_15

    goto :goto_29

    :cond_15
    goto :goto_bb

    nop

    :goto_d0
    iget v5, v1, Landroid/graphics/Rect;->bottom:I

    goto :goto_116

    nop

    :goto_d1
    move/from16 v3, p2

    goto :goto_75

    nop

    :goto_d2
    move-object v0, p0

    goto :goto_67

    nop

    :goto_d3
    add-int/2addr v3, v2

    goto :goto_f7

    nop

    :goto_d4
    iget v9, v5, Landroid/graphics/Rect;->top:I

    goto :goto_3

    nop

    :goto_d5
    const/4 v8, 0x0

    goto :goto_e0

    nop

    :goto_d6
    iget-boolean v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mExtraPaddingApplyToContentEnable:Z

    goto :goto_74

    nop

    :goto_d7
    invoke-super {p0, v2}, Landroid/widget/FrameLayout;->fitSystemWindows(Landroid/graphics/Rect;)Z

    goto :goto_b5

    nop

    :goto_d8
    iget v4, v4, Landroid/graphics/Rect;->top:I

    goto :goto_e4

    nop

    :goto_d9
    const/4 v3, 0x1

    goto :goto_ca

    nop

    :goto_da
    if-nez v1, :cond_16

    goto :goto_f0

    :cond_16
    goto :goto_10d

    nop

    :goto_db
    move-object v1, v7

    goto :goto_11a

    nop

    :goto_dc
    move v14, v4

    goto :goto_9d

    nop

    :goto_dd
    invoke-virtual {v4, v5}, Landroid/graphics/Rect;->set(Landroid/graphics/Rect;)V

    goto :goto_27

    nop

    :goto_de
    const/4 v3, 0x1

    goto :goto_6d

    nop

    :goto_df
    iget-object v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mInnerInsets:Landroid/graphics/Rect;

    goto :goto_55

    nop

    :goto_e0
    move v9, v8

    goto :goto_2d

    nop

    :goto_e1
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mFloatingWindowSize:Lmiuix/appcompat/app/floatingactivity/FloatingABOLayoutSpec;

    goto :goto_d1

    nop

    :goto_e2
    invoke-virtual {v2, v3, v8, v4, v5}, Landroid/view/View;->setPadding(IIII)V

    :goto_e3
    goto :goto_c4

    nop

    :goto_e4
    invoke-virtual {v2, v8, v8, v3, v4}, Landroid/graphics/drawable/Drawable;->setBounds(IIII)V

    goto :goto_14

    nop

    :goto_e5
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseInnerInsets:Landroid/graphics/Rect;

    goto :goto_d7

    nop

    :goto_e6
    iput v1, v5, Landroid/graphics/Rect;->top:I

    goto :goto_68

    nop

    :goto_e7
    iget-object v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mInnerInsets:Landroid/graphics/Rect;

    goto :goto_4b

    nop

    :goto_e8
    if-nez v2, :cond_17

    goto :goto_90

    :cond_17
    goto :goto_c0

    nop

    :goto_e9
    if-eqz v1, :cond_18

    goto :goto_52

    :cond_18
    :goto_ea
    goto :goto_bc

    nop

    :goto_eb
    iget-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBaseContentInsets:Landroid/graphics/Rect;

    goto :goto_dd

    nop

    :goto_ec
    shl-int/lit8 v3, v10, 0x10

    goto :goto_a0

    nop

    :goto_ed
    goto :goto_78

    :goto_ee
    goto :goto_77

    nop

    :goto_ef
    if-lez v1, :cond_19

    goto :goto_52

    :cond_19
    :goto_f0
    goto :goto_fd

    nop

    :goto_f1
    const/4 v5, 0x0

    goto :goto_d2

    nop

    :goto_f2
    move v12, v11

    :goto_f3
    goto :goto_21

    nop

    :goto_f4
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentMaskInsets:Landroid/graphics/Rect;

    goto :goto_53

    nop

    :goto_f5
    if-ne v1, v7, :cond_1a

    goto :goto_7e

    :cond_1a
    goto :goto_b8

    nop

    :goto_f6
    iget-object v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentInsets:Landroid/graphics/Rect;

    goto :goto_eb

    nop

    :goto_f7
    invoke-static {v11, v3}, Ljava/lang/Math;->max(II)I

    move-result v11

    goto :goto_3d

    nop

    :goto_f8
    add-int/2addr v1, v3

    goto :goto_3e

    nop

    :goto_f9
    move v2, v13

    goto :goto_84

    nop

    :goto_fa
    const/4 v6, 0x1

    goto :goto_d9

    nop

    :goto_fb
    invoke-virtual {v3}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->isSplitActionBar()Z

    move-result v3

    goto :goto_5e

    nop

    :goto_fc
    if-nez v5, :cond_1b

    goto :goto_69

    :cond_1b
    goto :goto_81

    nop

    :goto_fd
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentInsets:Landroid/graphics/Rect;

    goto :goto_51

    nop

    :goto_fe
    new-instance v1, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout$$ExternalSyntheticLambda0;

    goto :goto_b3

    nop

    :goto_ff
    const/4 v2, 0x0

    goto :goto_110

    nop

    :goto_100
    invoke-virtual {v1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v2

    goto :goto_1a

    nop

    :goto_101
    goto :goto_c2

    :goto_102
    goto :goto_fc

    nop

    :goto_103
    iget-boolean v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mOverlayMode:Z

    goto :goto_114

    nop

    :goto_104
    iget-object v7, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mContentMask:Landroid/view/View;

    goto :goto_d5

    nop

    :goto_105
    invoke-static {v9, v1}, Ljava/lang/Math;->max(II)I

    move-result v1

    goto :goto_45

    nop

    :goto_106
    if-eq v3, v4, :cond_1c

    goto :goto_e3

    :cond_1c
    goto :goto_8c

    nop

    :goto_107
    invoke-static {v14}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v3

    goto :goto_7b

    nop

    :goto_108
    if-nez v7, :cond_1d

    goto :goto_a6

    :cond_1d
    goto :goto_16

    nop

    :goto_109
    if-nez v3, :cond_1e

    goto :goto_ee

    :cond_1e
    goto :goto_fb

    nop

    :goto_10a
    move v13, v2

    goto :goto_2b

    nop

    :goto_10b
    goto :goto_ba

    :goto_10c
    goto :goto_b9

    nop

    :goto_10d
    iget v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mImeInsetBottom:I

    goto :goto_ef

    nop

    :goto_10e
    invoke-static {v11, v3}, Ljava/lang/Math;->max(II)I

    move-result v9

    goto :goto_50

    nop

    :goto_10f
    move-object v0, p0

    goto :goto_4a

    nop

    :goto_110
    iput-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mAnimateContentMarginBottomInsets:Landroid/graphics/Rect;

    goto :goto_10b

    nop

    :goto_111
    if-eqz v2, :cond_1f

    goto :goto_52

    :cond_1f
    goto :goto_72

    nop

    :goto_112
    if-lt v9, v1, :cond_20

    goto :goto_3c

    :cond_20
    goto :goto_93

    nop

    :goto_113
    invoke-virtual {v2}, Lmiuix/container/ExtraPaddingPolicy;->isEnable()Z

    move-result v2

    goto :goto_e8

    nop

    :goto_114
    if-eqz v2, :cond_21

    goto :goto_9

    :cond_21
    goto :goto_117

    nop

    :goto_115
    iput v1, v5, Landroid/graphics/Rect;->bottom:I

    goto :goto_101

    nop

    :goto_116
    add-int/2addr v5, v3

    goto :goto_c1

    nop

    :goto_117
    invoke-virtual {v1}, Landroid/view/View;->getPaddingLeft()I

    move-result v2

    goto :goto_91

    nop

    :goto_118
    iget-object v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mInnerInsets:Landroid/graphics/Rect;

    goto :goto_13

    nop

    :goto_119
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingTop()I

    move-result v1

    goto :goto_79

    nop

    :goto_11a
    invoke-direct/range {v0 .. v6}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->applyInsetsByMargin(Landroid/view/View;Landroid/graphics/Rect;ZZZZ)Z

    goto :goto_57

    nop

    :goto_11b
    add-int/2addr v9, v1

    goto :goto_bd

    nop

    :goto_11c
    move-object v0, p0

    goto :goto_db

    nop

    :goto_11d
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarTop:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_99

    nop

    :goto_11e
    add-int/2addr v3, v4

    goto :goto_2c

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarOverlayLayout__updateBottomMenuMode',
        'method': '.method protected updateBottomMenuMode()V',
        'method_name': 'updateBottomMenuMode',
        'method_anchors': ['iget v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBottomMenuModeConfig:I', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;', 'invoke-virtual {v1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;', 'invoke-virtual {v1}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;', 'iget v1, v1, Landroid/util/DisplayMetrics;->density:F', 'if-nez v0, :cond_1', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->getMeasuredWidth()I', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;'],
        'type': 'method_replace',
        'search': """.method protected updateBottomMenuMode()V
    .registers 8

    iget v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBottomMenuModeConfig:I

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;

    move-result-object v1

    invoke-virtual {v1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v1

    invoke-virtual {v1}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;

    move-result-object v1

    iget v1, v1, Landroid/util/DisplayMetrics;->density:F

    const/4 v2, 0x3

    const/16 v3, 0x280

    const/high16 v4, 0x3f800000

    const/4 v5, 0x2

    if-nez v0, :cond_1

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getMeasuredWidth()I

    move-result v0

    int-to-float v0, v0

    mul-float/2addr v0, v4

    div-float/2addr v0, v1

    float-to-int v0, v0

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;

    move-result-object v6

    invoke-static {v6}, Lmiuix/core/util/EnvStateManager;->getWindowSize(Landroid/content/Context;)Landroid/graphics/Point;

    move-result-object v6

    iget v6, v6, Landroid/graphics/Point;->x:I

    int-to-float v6, v6

    mul-float/2addr v6, v4

    div-float/2addr v6, v1

    float-to-int v1, v6

    iget v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mDeviceType:I

    if-ne v4, v5, :cond_0

    const/16 v4, 0x19a

    if-le v0, v4, :cond_0

    if-le v1, v3, :cond_0

    :goto_0
    move v0, v2

    goto :goto_1

    :cond_0
    move v0, v5

    goto :goto_1

    :cond_1
    const/4 v6, 0x1

    if-ne v0, v6, :cond_2

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-static {v0}, Lmiuix/core/util/EnvStateManager;->getWindowSize(Landroid/content/Context;)Landroid/graphics/Point;

    move-result-object v0

    iget v0, v0, Landroid/graphics/Point;->x:I

    int-to-float v0, v0

    mul-float/2addr v0, v4

    div-float/2addr v0, v1

    float-to-int v0, v0

    iget v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mDeviceType:I

    if-ne v1, v5, :cond_0

    if-le v0, v3, :cond_0

    goto :goto_0

    :cond_2
    :goto_1
    iget v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBottomMenuMode:I

    if-eq v0, v1, :cond_4

    iput v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBottomMenuMode:I

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarContextView:Lmiuix/appcompat/internal/app/widget/ActionBarContextView;

    if-eqz v1, :cond_3

    invoke-virtual {v1, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->setBottomMenuMode(I)V

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarContextView:Lmiuix/appcompat/internal/app/widget/ActionBarContextView;

    invoke-virtual {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->refreshBottomMenu()V

    :cond_3
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    if-eqz v0, :cond_4

    iget v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBottomMenuMode:I

    invoke-virtual {v0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->setBottomMenuMode(I)V

    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->refreshBottomMenu()V

    :cond_4
    return-void
.end method""",
        'replacement': """.method protected updateBottomMenuMode()V
    .registers 8

    goto :goto_1a

    nop

    :goto_0
    invoke-virtual {v0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->setBottomMenuMode(I)V

    goto :goto_10

    nop

    :goto_1
    if-eqz v0, :cond_0

    goto :goto_3a

    :cond_0
    goto :goto_3e

    nop

    :goto_2
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->refreshBottomMenu()V

    :goto_3
    goto :goto_2e

    nop

    :goto_4
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;

    move-result-object v1

    goto :goto_c

    nop

    :goto_5
    goto :goto_20

    :goto_6
    goto :goto_19

    nop

    :goto_7
    mul-float/2addr v0, v4

    goto :goto_23

    nop

    :goto_8
    div-float/2addr v0, v1

    goto :goto_28

    nop

    :goto_9
    move v0, v5

    goto :goto_39

    nop

    :goto_a
    const/16 v4, 0x19a

    goto :goto_2b

    nop

    :goto_b
    iget v1, v1, Landroid/util/DisplayMetrics;->density:F

    goto :goto_1b

    nop

    :goto_c
    invoke-virtual {v1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v1

    goto :goto_36

    nop

    :goto_d
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarContextView:Lmiuix/appcompat/internal/app/widget/ActionBarContextView;

    goto :goto_11

    nop

    :goto_e
    const/high16 v4, 0x3f800000

    goto :goto_13

    nop

    :goto_f
    invoke-virtual {v1, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->setBottomMenuMode(I)V

    goto :goto_d

    nop

    :goto_10
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_2

    nop

    :goto_11
    invoke-virtual {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->refreshBottomMenu()V

    :goto_12
    goto :goto_2f

    nop

    :goto_13
    const/4 v5, 0x2

    goto :goto_1

    nop

    :goto_14
    goto :goto_6

    :goto_15
    goto :goto_9

    nop

    :goto_16
    float-to-int v1, v6

    goto :goto_31

    nop

    :goto_17
    if-nez v1, :cond_1

    goto :goto_12

    :cond_1
    goto :goto_f

    nop

    :goto_18
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;

    move-result-object v0

    goto :goto_32

    nop

    :goto_19
    iget v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBottomMenuMode:I

    goto :goto_1c

    nop

    :goto_1a
    iget v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBottomMenuModeConfig:I

    goto :goto_4

    nop

    :goto_1b
    const/4 v2, 0x3

    goto :goto_25

    nop

    :goto_1c
    if-ne v0, v1, :cond_2

    goto :goto_3

    :cond_2
    goto :goto_22

    nop

    :goto_1d
    int-to-float v0, v0

    goto :goto_7

    nop

    :goto_1e
    const/4 v6, 0x1

    goto :goto_29

    nop

    :goto_1f
    if-gt v1, v3, :cond_3

    goto :goto_15

    :cond_3
    :goto_20
    goto :goto_34

    nop

    :goto_21
    div-float/2addr v6, v1

    goto :goto_16

    nop

    :goto_22
    iput v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBottomMenuMode:I

    goto :goto_3c

    nop

    :goto_23
    div-float/2addr v0, v1

    goto :goto_30

    nop

    :goto_24
    int-to-float v6, v6

    goto :goto_2c

    nop

    :goto_25
    const/16 v3, 0x280

    goto :goto_e

    nop

    :goto_26
    iget v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBottomMenuMode:I

    goto :goto_0

    nop

    :goto_27
    if-nez v0, :cond_4

    goto :goto_3

    :cond_4
    goto :goto_26

    nop

    :goto_28
    float-to-int v0, v0

    goto :goto_33

    nop

    :goto_29
    if-eq v0, v6, :cond_5

    goto :goto_6

    :cond_5
    goto :goto_18

    nop

    :goto_2a
    iget v6, v6, Landroid/graphics/Point;->x:I

    goto :goto_24

    nop

    :goto_2b
    if-gt v0, v4, :cond_6

    goto :goto_15

    :cond_6
    goto :goto_1f

    nop

    :goto_2c
    mul-float/2addr v6, v4

    goto :goto_21

    nop

    :goto_2d
    invoke-static {v6}, Lmiuix/core/util/EnvStateManager;->getWindowSize(Landroid/content/Context;)Landroid/graphics/Point;

    move-result-object v6

    goto :goto_2a

    nop

    :goto_2e
    return-void

    :goto_2f
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_27

    nop

    :goto_30
    float-to-int v0, v0

    goto :goto_3f

    nop

    :goto_31
    iget v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mDeviceType:I

    goto :goto_37

    nop

    :goto_32
    invoke-static {v0}, Lmiuix/core/util/EnvStateManager;->getWindowSize(Landroid/content/Context;)Landroid/graphics/Point;

    move-result-object v0

    goto :goto_35

    nop

    :goto_33
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;

    move-result-object v6

    goto :goto_2d

    nop

    :goto_34
    move v0, v2

    goto :goto_14

    nop

    :goto_35
    iget v0, v0, Landroid/graphics/Point;->x:I

    goto :goto_1d

    nop

    :goto_36
    invoke-virtual {v1}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;

    move-result-object v1

    goto :goto_b

    nop

    :goto_37
    if-eq v4, v5, :cond_7

    goto :goto_15

    :cond_7
    goto :goto_a

    nop

    :goto_38
    int-to-float v0, v0

    goto :goto_40

    nop

    :goto_39
    goto :goto_6

    :goto_3a
    goto :goto_1e

    nop

    :goto_3b
    if-gt v0, v3, :cond_8

    goto :goto_15

    :cond_8
    goto :goto_5

    nop

    :goto_3c
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarContextView:Lmiuix/appcompat/internal/app/widget/ActionBarContextView;

    goto :goto_17

    nop

    :goto_3d
    if-eq v1, v5, :cond_9

    goto :goto_15

    :cond_9
    goto :goto_3b

    nop

    :goto_3e
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getMeasuredWidth()I

    move-result v0

    goto :goto_38

    nop

    :goto_3f
    iget v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mDeviceType:I

    goto :goto_3d

    nop

    :goto_40
    mul-float/2addr v0, v4

    goto :goto_8

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarOverlayLayout__updateCurrentContentInsetInOverlayMode',
        'method': '.method updateCurrentContentInsetInOverlayMode()V',
        'method_name': 'updateCurrentContentInsetInOverlayMode',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mCurrentContentInset:Landroid/graphics/Rect;', 'iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;', 'invoke-virtual {v0, v1}, Landroid/graphics/Rect;->set(Landroid/graphics/Rect;)V', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBar:Lmiuix/appcompat/app/ActionBar;', 'if-eqz v0, :cond_2', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarTop:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;', 'if-eqz v0, :cond_2', 'invoke-virtual {v0}, Landroid/widget/FrameLayout;->getVisibility()I'],
        'type': 'method_replace',
        'search': """.method updateCurrentContentInsetInOverlayMode()V
    .registers 5

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mCurrentContentInset:Landroid/graphics/Rect;

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    invoke-virtual {v0, v1}, Landroid/graphics/Rect;->set(Landroid/graphics/Rect;)V

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBar:Lmiuix/appcompat/app/ActionBar;

    const/4 v1, 0x0

    if-eqz v0, :cond_2

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarTop:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    if-eqz v0, :cond_2

    invoke-virtual {v0}, Landroid/widget/FrameLayout;->getVisibility()I

    move-result v0

    const/16 v2, 0x8

    if-eq v0, v2, :cond_2

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarTop:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    invoke-virtual {v0}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result v0

    if-lez v0, :cond_2

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBar:Lmiuix/appcompat/app/ActionBar;

    check-cast v0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;

    invoke-virtual {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->getTopViewHeight()I

    move-result v0

    iget-boolean v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mEnableWindowStatusBarInsets:Z

    if-eqz v2, :cond_0

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    iget v2, v2, Landroid/graphics/Rect;->top:I

    goto :goto_0

    :cond_0
    move v2, v1

    :goto_0
    add-int/2addr v0, v2

    iget-boolean v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mIsMiuixFloating:Z

    if-eqz v2, :cond_1

    iget v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mInsetTopInMiuixFloating:I

    goto :goto_1

    :cond_1
    move v2, v1

    :goto_1
    add-int/2addr v0, v2

    int-to-float v0, v0

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarTop:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    invoke-virtual {v2}, Landroid/widget/FrameLayout;->getTranslationY()F

    move-result v2

    add-float/2addr v0, v2

    float-to-int v0, v0

    invoke-static {v1, v0}, Ljava/lang/Math;->max(II)I

    move-result v1

    :cond_2
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->getBottomInset()I

    move-result v0

    iget v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBottomExtraInset:I

    invoke-static {v0, v2}, Ljava/lang/Math;->max(II)I

    move-result v0

    iget v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBottomMenuExtraInset:I

    invoke-static {v0, v2}, Ljava/lang/Math;->max(II)I

    move-result v0

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mGroupButtonInsetsRect:Landroid/graphics/Rect;

    iget v2, v2, Landroid/graphics/Rect;->bottom:I

    invoke-static {v0, v2}, Ljava/lang/Math;->max(II)I

    move-result v0

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->isTranslucentStatus()Z

    move-result v2

    if-eqz v2, :cond_3

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    iget v2, v2, Landroid/graphics/Rect;->top:I

    if-ge v1, v2, :cond_3

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mCurrentContentInset:Landroid/graphics/Rect;

    iput v2, v1, Landroid/graphics/Rect;->top:I

    goto :goto_2

    :cond_3
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mCurrentContentInset:Landroid/graphics/Rect;

    iput v1, v2, Landroid/graphics/Rect;->top:I

    :goto_2
    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->isLayoutHideNavigation()Z

    move-result v1

    if-eqz v1, :cond_4

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    iget v1, v1, Landroid/graphics/Rect;->bottom:I

    if-ge v0, v1, :cond_4

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mCurrentContentInset:Landroid/graphics/Rect;

    iput v1, v0, Landroid/graphics/Rect;->bottom:I

    goto :goto_3

    :cond_4
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mCurrentContentInset:Landroid/graphics/Rect;

    iput v0, v1, Landroid/graphics/Rect;->bottom:I

    :goto_3
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mCurrentContentInset:Landroid/graphics/Rect;

    iget v1, v0, Landroid/graphics/Rect;->left:I

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    iget v3, v2, Landroid/graphics/Rect;->left:I

    if-ge v1, v3, :cond_5

    iput v3, v0, Landroid/graphics/Rect;->left:I

    :cond_5
    iget v1, v0, Landroid/graphics/Rect;->right:I

    iget v2, v2, Landroid/graphics/Rect;->right:I

    if-ge v1, v2, :cond_6

    iput v2, v0, Landroid/graphics/Rect;->right:I

    :cond_6
    invoke-direct {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->dispatchContentInset(Landroid/graphics/Rect;)V

    return-void
.end method""",
        'replacement': """.method updateCurrentContentInsetInOverlayMode()V
    .registers 5

    goto :goto_46

    nop

    :goto_0
    int-to-float v0, v0

    goto :goto_4b

    nop

    :goto_1
    iget v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mInsetTopInMiuixFloating:I

    goto :goto_24

    nop

    :goto_2
    invoke-virtual {v0, v1}, Landroid/graphics/Rect;->set(Landroid/graphics/Rect;)V

    goto :goto_4

    nop

    :goto_3
    check-cast v0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;

    goto :goto_28

    nop

    :goto_4
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBar:Lmiuix/appcompat/app/ActionBar;

    goto :goto_1d

    nop

    :goto_5
    invoke-virtual {v2}, Landroid/widget/FrameLayout;->getTranslationY()F

    move-result v2

    goto :goto_b

    nop

    :goto_6
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->isTranslucentStatus()Z

    move-result v2

    goto :goto_8

    nop

    :goto_7
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarTop:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_2d

    nop

    :goto_8
    if-nez v2, :cond_0

    goto :goto_44

    :cond_0
    goto :goto_19

    nop

    :goto_9
    iget v2, v2, Landroid/graphics/Rect;->top:I

    goto :goto_c

    nop

    :goto_a
    if-lt v1, v3, :cond_1

    goto :goto_21

    :cond_1
    goto :goto_20

    nop

    :goto_b
    add-float/2addr v0, v2

    goto :goto_40

    nop

    :goto_c
    goto :goto_14

    :goto_d
    goto :goto_13

    nop

    :goto_e
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mCurrentContentInset:Landroid/graphics/Rect;

    goto :goto_26

    nop

    :goto_f
    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->isLayoutHideNavigation()Z

    move-result v1

    goto :goto_45

    nop

    :goto_10
    iget v2, v2, Landroid/graphics/Rect;->top:I

    goto :goto_1f

    nop

    :goto_11
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    goto :goto_2

    nop

    :goto_12
    invoke-direct {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->dispatchContentInset(Landroid/graphics/Rect;)V

    goto :goto_52

    nop

    :goto_13
    move v2, v1

    :goto_14
    goto :goto_2e

    nop

    :goto_15
    if-nez v0, :cond_2

    goto :goto_54

    :cond_2
    goto :goto_2b

    nop

    :goto_16
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->getBottomInset()I

    move-result v0

    goto :goto_1a

    nop

    :goto_17
    const/16 v2, 0x8

    goto :goto_18

    nop

    :goto_18
    if-ne v0, v2, :cond_3

    goto :goto_54

    :cond_3
    goto :goto_7

    nop

    :goto_19
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    goto :goto_10

    nop

    :goto_1a
    iget v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBottomExtraInset:I

    goto :goto_32

    nop

    :goto_1b
    iget v1, v0, Landroid/graphics/Rect;->left:I

    goto :goto_2f

    nop

    :goto_1c
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mCurrentContentInset:Landroid/graphics/Rect;

    goto :goto_3d

    nop

    :goto_1d
    const/4 v1, 0x0

    goto :goto_51

    nop

    :goto_1e
    add-int/2addr v0, v2

    goto :goto_0

    nop

    :goto_1f
    if-lt v1, v2, :cond_4

    goto :goto_44

    :cond_4
    goto :goto_e

    nop

    :goto_20
    iput v3, v0, Landroid/graphics/Rect;->left:I

    :goto_21
    goto :goto_36

    nop

    :goto_22
    iget v1, v1, Landroid/graphics/Rect;->bottom:I

    goto :goto_48

    nop

    :goto_23
    iget-boolean v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mIsMiuixFloating:Z

    goto :goto_4f

    nop

    :goto_24
    goto :goto_3c

    :goto_25
    goto :goto_3b

    nop

    :goto_26
    iput v2, v1, Landroid/graphics/Rect;->top:I

    goto :goto_43

    nop

    :goto_27
    iget v2, v2, Landroid/graphics/Rect;->right:I

    goto :goto_35

    nop

    :goto_28
    invoke-virtual {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->getTopViewHeight()I

    move-result v0

    goto :goto_34

    nop

    :goto_29
    iput v0, v1, Landroid/graphics/Rect;->bottom:I

    :goto_2a
    goto :goto_30

    nop

    :goto_2b
    invoke-virtual {v0}, Landroid/widget/FrameLayout;->getVisibility()I

    move-result v0

    goto :goto_17

    nop

    :goto_2c
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mGroupButtonInsetsRect:Landroid/graphics/Rect;

    goto :goto_37

    nop

    :goto_2d
    invoke-virtual {v0}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result v0

    goto :goto_31

    nop

    :goto_2e
    add-int/2addr v0, v2

    goto :goto_23

    nop

    :goto_2f
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    goto :goto_4c

    nop

    :goto_30
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mCurrentContentInset:Landroid/graphics/Rect;

    goto :goto_1b

    nop

    :goto_31
    if-gtz v0, :cond_5

    goto :goto_54

    :cond_5
    goto :goto_50

    nop

    :goto_32
    invoke-static {v0, v2}, Ljava/lang/Math;->max(II)I

    move-result v0

    goto :goto_3f

    nop

    :goto_33
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mCurrentContentInset:Landroid/graphics/Rect;

    goto :goto_41

    nop

    :goto_34
    iget-boolean v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mEnableWindowStatusBarInsets:Z

    goto :goto_38

    nop

    :goto_35
    if-lt v1, v2, :cond_6

    goto :goto_4e

    :cond_6
    goto :goto_4d

    nop

    :goto_36
    iget v1, v0, Landroid/graphics/Rect;->right:I

    goto :goto_27

    nop

    :goto_37
    iget v2, v2, Landroid/graphics/Rect;->bottom:I

    goto :goto_56

    nop

    :goto_38
    if-nez v2, :cond_7

    goto :goto_d

    :cond_7
    goto :goto_47

    nop

    :goto_39
    invoke-static {v0, v2}, Ljava/lang/Math;->max(II)I

    move-result v0

    goto :goto_2c

    nop

    :goto_3a
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarTop:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_15

    nop

    :goto_3b
    move v2, v1

    :goto_3c
    goto :goto_1e

    nop

    :goto_3d
    iput v1, v2, Landroid/graphics/Rect;->top:I

    :goto_3e
    goto :goto_f

    nop

    :goto_3f
    iget v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mBottomMenuExtraInset:I

    goto :goto_39

    nop

    :goto_40
    float-to-int v0, v0

    goto :goto_53

    nop

    :goto_41
    iput v1, v0, Landroid/graphics/Rect;->bottom:I

    goto :goto_49

    nop

    :goto_42
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mCurrentContentInset:Landroid/graphics/Rect;

    goto :goto_29

    nop

    :goto_43
    goto :goto_3e

    :goto_44
    goto :goto_1c

    nop

    :goto_45
    if-nez v1, :cond_8

    goto :goto_4a

    :cond_8
    goto :goto_55

    nop

    :goto_46
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mCurrentContentInset:Landroid/graphics/Rect;

    goto :goto_11

    nop

    :goto_47
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    goto :goto_9

    nop

    :goto_48
    if-lt v0, v1, :cond_9

    goto :goto_4a

    :cond_9
    goto :goto_33

    nop

    :goto_49
    goto :goto_2a

    :goto_4a
    goto :goto_42

    nop

    :goto_4b
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBarTop:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_5

    nop

    :goto_4c
    iget v3, v2, Landroid/graphics/Rect;->left:I

    goto :goto_a

    nop

    :goto_4d
    iput v2, v0, Landroid/graphics/Rect;->right:I

    :goto_4e
    goto :goto_12

    nop

    :goto_4f
    if-nez v2, :cond_a

    goto :goto_25

    :cond_a
    goto :goto_1

    nop

    :goto_50
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mActionBar:Lmiuix/appcompat/app/ActionBar;

    goto :goto_3

    nop

    :goto_51
    if-nez v0, :cond_b

    goto :goto_54

    :cond_b
    goto :goto_3a

    nop

    :goto_52
    return-void

    :goto_53
    invoke-static {v1, v0}, Ljava/lang/Math;->max(II)I

    move-result v1

    :goto_54
    goto :goto_16

    nop

    :goto_55
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->mThemeCompatSystemInset:Landroid/graphics/Rect;

    goto :goto_22

    nop

    :goto_56
    invoke-static {v0, v2}, Ljava/lang/Math;->max(II)I

    move-result v0

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
