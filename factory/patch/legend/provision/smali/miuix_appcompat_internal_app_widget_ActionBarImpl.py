TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/app/widget/ActionBarImpl.smali'
CLASS_FALLBACK_NAMES = ['ActionBarImpl.smali']
CLASS_ANCHORS = ['.super Lmiuix/appcompat/app/ActionBar;', '.field private static final UNINITIALIZED_OFFSET:Ljava/lang/Integer;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarImpl__animateToMode',
        'method': '.method animateToMode(Z)V',
        'method_name': 'animateToMode',
        'method_anchors': ['if-eqz p1, :cond_0', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->showForActionMode()V', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->hideForActionMode()V', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionModeView:Lmiuix/appcompat/internal/app/widget/ActionModeView;', 'invoke-interface {v0, p1}, Lmiuix/appcompat/internal/app/widget/ActionModeView;->animateToVisibility(Z)V', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mTabScrollView:Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView;', 'if-eqz v0, :cond_1', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionView:Lmiuix/appcompat/internal/app/widget/ActionBarView;'],
        'type': 'method_replace',
        'search': """.method animateToMode(Z)V
    .registers 4

    if-eqz p1, :cond_0

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->showForActionMode()V

    goto :goto_0

    :cond_0
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->hideForActionMode()V

    :goto_0
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionModeView:Lmiuix/appcompat/internal/app/widget/ActionModeView;

    invoke-interface {v0, p1}, Lmiuix/appcompat/internal/app/widget/ActionModeView;->animateToVisibility(Z)V

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mTabScrollView:Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView;

    if-eqz v0, :cond_1

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    invoke-virtual {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->isTightTitleWithEmbeddedTabs()Z

    move-result v0

    if-nez v0, :cond_1

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    invoke-virtual {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->isCollapsed()Z

    move-result v0

    if-eqz v0, :cond_1

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mTabScrollView:Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView;

    xor-int/lit8 v1, p1, 0x1

    invoke-virtual {v0, v1}, Landroid/widget/HorizontalScrollView;->setEnabled(Z)V

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mExpandTabScrollView:Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView;

    xor-int/lit8 v1, p1, 0x1

    invoke-virtual {v0, v1}, Landroid/widget/HorizontalScrollView;->setEnabled(Z)V

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mSecondaryTabScrollView:Lmiuix/appcompat/internal/app/widget/SecondaryTabBar;

    invoke-interface {v0}, Lmiuix/appcompat/internal/app/widget/SecondaryTabBar;->asViewGroup()Landroid/view/ViewGroup;

    move-result-object v0

    xor-int/lit8 v1, p1, 0x1

    invoke-virtual {v0, v1}, Landroid/view/ViewGroup;->setEnabled(Z)V

    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mSecondaryExpandTabScrollView:Lmiuix/appcompat/internal/app/widget/SecondaryTabBar;

    invoke-interface {p0}, Lmiuix/appcompat/internal/app/widget/SecondaryTabBar;->asViewGroup()Landroid/view/ViewGroup;

    move-result-object p0

    xor-int/lit8 p1, p1, 0x1

    invoke-virtual {p0, p1}, Landroid/view/ViewGroup;->setEnabled(Z)V

    :cond_1
    return-void
.end method""",
        'replacement': """.method animateToMode(Z)V
    .registers 4

    goto :goto_17

    nop

    :goto_0
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mTabScrollView:Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView;

    goto :goto_16

    nop

    :goto_1
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->showForActionMode()V

    goto :goto_10

    nop

    :goto_2
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_a

    nop

    :goto_3
    xor-int/lit8 v1, p1, 0x1

    goto :goto_12

    nop

    :goto_4
    invoke-virtual {p0, p1}, Landroid/view/ViewGroup;->setEnabled(Z)V

    :goto_5
    goto :goto_1d

    nop

    :goto_6
    invoke-virtual {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->isCollapsed()Z

    move-result v0

    goto :goto_1a

    nop

    :goto_7
    invoke-interface {v0}, Lmiuix/appcompat/internal/app/widget/SecondaryTabBar;->asViewGroup()Landroid/view/ViewGroup;

    move-result-object v0

    goto :goto_e

    nop

    :goto_8
    invoke-interface {p0}, Lmiuix/appcompat/internal/app/widget/SecondaryTabBar;->asViewGroup()Landroid/view/ViewGroup;

    move-result-object p0

    goto :goto_1e

    nop

    :goto_9
    xor-int/lit8 v1, p1, 0x1

    goto :goto_f

    nop

    :goto_a
    invoke-virtual {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->isTightTitleWithEmbeddedTabs()Z

    move-result v0

    goto :goto_13

    nop

    :goto_b
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mTabScrollView:Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView;

    goto :goto_9

    nop

    :goto_c
    invoke-interface {v0, p1}, Lmiuix/appcompat/internal/app/widget/ActionModeView;->animateToVisibility(Z)V

    goto :goto_0

    nop

    :goto_d
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mSecondaryTabScrollView:Lmiuix/appcompat/internal/app/widget/SecondaryTabBar;

    goto :goto_7

    nop

    :goto_e
    xor-int/lit8 v1, p1, 0x1

    goto :goto_19

    nop

    :goto_f
    invoke-virtual {v0, v1}, Landroid/widget/HorizontalScrollView;->setEnabled(Z)V

    goto :goto_1f

    nop

    :goto_10
    goto :goto_15

    :goto_11
    goto :goto_14

    nop

    :goto_12
    invoke-virtual {v0, v1}, Landroid/widget/HorizontalScrollView;->setEnabled(Z)V

    goto :goto_d

    nop

    :goto_13
    if-eqz v0, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_1c

    nop

    :goto_14
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->hideForActionMode()V

    :goto_15
    goto :goto_18

    nop

    :goto_16
    if-nez v0, :cond_1

    goto :goto_5

    :cond_1
    goto :goto_2

    nop

    :goto_17
    if-nez p1, :cond_2

    goto :goto_11

    :cond_2
    goto :goto_1

    nop

    :goto_18
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionModeView:Lmiuix/appcompat/internal/app/widget/ActionModeView;

    goto :goto_c

    nop

    :goto_19
    invoke-virtual {v0, v1}, Landroid/view/ViewGroup;->setEnabled(Z)V

    goto :goto_1b

    nop

    :goto_1a
    if-nez v0, :cond_3

    goto :goto_5

    :cond_3
    goto :goto_b

    nop

    :goto_1b
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mSecondaryExpandTabScrollView:Lmiuix/appcompat/internal/app/widget/SecondaryTabBar;

    goto :goto_8

    nop

    :goto_1c
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_6

    nop

    :goto_1d
    return-void

    :goto_1e
    xor-int/lit8 p1, p1, 0x1

    goto :goto_4

    nop

    :goto_1f
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mExpandTabScrollView:Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView;

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarImpl__getTopOffsetForCoordinateView',
        'method': '.method getTopOffsetForCoordinateView(Landroid/view/View;)I',
        'method_name': 'getTopOffsetForCoordinateView',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCoordinateOffsetViewSet:Ljava/util/HashMap;', 'invoke-virtual {v0, p1}, Ljava/util/HashMap;->containsKey(Ljava/lang/Object;)Z', 'if-eqz v0, :cond_0', 'invoke-direct {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->getCoordinateOffsetViewTopOffsetOrDefault(Landroid/view/View;)Ljava/lang/Integer;', 'invoke-virtual {p0}, Ljava/lang/Integer;->intValue()I', 'return p0', 'return p0'],
        'type': 'method_replace',
        'search': """.method getTopOffsetForCoordinateView(Landroid/view/View;)I
    .registers 3

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCoordinateOffsetViewSet:Ljava/util/HashMap;

    invoke-virtual {v0, p1}, Ljava/util/HashMap;->containsKey(Ljava/lang/Object;)Z

    move-result v0

    if-eqz v0, :cond_0

    invoke-direct {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->getCoordinateOffsetViewTopOffsetOrDefault(Landroid/view/View;)Ljava/lang/Integer;

    move-result-object p0

    invoke-virtual {p0}, Ljava/lang/Integer;->intValue()I

    move-result p0

    return p0

    :cond_0
    const/4 p0, -0x1

    return p0
.end method""",
        'replacement': """.method getTopOffsetForCoordinateView(Landroid/view/View;)I
    .registers 3

    goto :goto_6

    nop

    :goto_0
    invoke-virtual {v0, p1}, Ljava/util/HashMap;->containsKey(Ljava/lang/Object;)Z

    move-result v0

    goto :goto_5

    nop

    :goto_1
    return p0

    :goto_2
    goto :goto_3

    nop

    :goto_3
    const/4 p0, -0x1

    goto :goto_7

    nop

    :goto_4
    invoke-direct {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->getCoordinateOffsetViewTopOffsetOrDefault(Landroid/view/View;)Ljava/lang/Integer;

    move-result-object p0

    goto :goto_8

    nop

    :goto_5
    if-nez v0, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_4

    nop

    :goto_6
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCoordinateOffsetViewSet:Ljava/util/HashMap;

    goto :goto_0

    nop

    :goto_7
    return p0

    :goto_8
    invoke-virtual {p0}, Ljava/lang/Integer;->intValue()I

    move-result p0

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarImpl__getTopViewHeight',
        'method': '.method getTopViewHeight()I',
        'method_name': 'getTopViewHeight',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionMode:Landroid/view/ActionMode;', 'if-eqz v0, :cond_0', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionModeView:Lmiuix/appcompat/internal/app/widget/ActionModeView;', 'if-eqz v0, :cond_0', 'invoke-interface {v0}, Lmiuix/appcompat/internal/app/widget/ActionModeView;->getViewHeight()I', 'return p0', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionView:Lmiuix/appcompat/internal/app/widget/ActionBarView;', 'invoke-virtual {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->isCollapsed()Z'],
        'type': 'method_replace',
        'search': """.method getTopViewHeight()I
    .registers 2

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionMode:Landroid/view/ActionMode;

    if-eqz v0, :cond_0

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionModeView:Lmiuix/appcompat/internal/app/widget/ActionModeView;

    if-eqz v0, :cond_0

    invoke-interface {v0}, Lmiuix/appcompat/internal/app/widget/ActionModeView;->getViewHeight()I

    move-result p0

    return p0

    :cond_0
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    invoke-virtual {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->isCollapsed()Z

    move-result v0

    if-eqz v0, :cond_1

    const/4 p0, 0x0

    return p0

    :cond_1
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->getCollapsedHeight()I

    move-result p0

    return p0
.end method""",
        'replacement': """.method getTopViewHeight()I
    .registers 2

    goto :goto_7

    nop

    :goto_0
    return p0

    :goto_1
    goto :goto_c

    nop

    :goto_2
    invoke-virtual {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->isCollapsed()Z

    move-result v0

    goto :goto_4

    nop

    :goto_3
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_2

    nop

    :goto_4
    if-nez v0, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_e

    nop

    :goto_5
    if-nez v0, :cond_1

    goto :goto_b

    :cond_1
    goto :goto_8

    nop

    :goto_6
    return p0

    :goto_7
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionMode:Landroid/view/ActionMode;

    goto :goto_f

    nop

    :goto_8
    invoke-interface {v0}, Lmiuix/appcompat/internal/app/widget/ActionModeView;->getViewHeight()I

    move-result p0

    goto :goto_a

    nop

    :goto_9
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->getCollapsedHeight()I

    move-result p0

    goto :goto_6

    nop

    :goto_a
    return p0

    :goto_b
    goto :goto_3

    nop

    :goto_c
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_9

    nop

    :goto_d
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionModeView:Lmiuix/appcompat/internal/app/widget/ActionModeView;

    goto :goto_5

    nop

    :goto_e
    const/4 p0, 0x0

    goto :goto_0

    nop

    :goto_f
    if-nez v0, :cond_2

    goto :goto_b

    :cond_2
    goto :goto_d

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarImpl__hideForActionMode',
        'method': '.method hideForActionMode()V',
        'method_name': 'hideForActionMode',
        'method_anchors': ['iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mShowingForMode:Z', 'if-eqz v0, :cond_2', 'iput-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mShowingForMode:Z', 'iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionView:Lmiuix/appcompat/internal/app/widget/ActionBarView;', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->getDisplayOptions()I', 'if-eqz v2, :cond_0', 'invoke-virtual {v1, v2}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->onActionModeEnd(Z)V', 'invoke-direct {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->updateVisibility(Z)V'],
        'type': 'method_replace',
        'search': """.method hideForActionMode()V
    .registers 5

    iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mShowingForMode:Z

    if-eqz v0, :cond_2

    const/4 v0, 0x0

    iput-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mShowingForMode:Z

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->getDisplayOptions()I

    move-result v2

    const v3, 0x8000

    and-int/2addr v2, v3

    if-eqz v2, :cond_0

    const/4 v2, 0x1

    goto :goto_0

    :cond_0
    move v2, v0

    :goto_0
    invoke-virtual {v1, v2}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->onActionModeEnd(Z)V

    invoke-direct {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->updateVisibility(Z)V

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionModeView:Lmiuix/appcompat/internal/app/widget/ActionModeView;

    instance-of v0, v0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;

    if-eqz v0, :cond_1

    iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCurrentResizable:Z

    invoke-virtual {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->setResizable(Z)V

    goto :goto_1

    :cond_1
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContainerView:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    invoke-virtual {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->finishActionMode()V

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionModeView:Lmiuix/appcompat/internal/app/widget/ActionModeView;

    check-cast v0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;

    invoke-virtual {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->isResizable()Z

    move-result v0

    iput-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCurrentResizable:Z

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionModeView:Lmiuix/appcompat/internal/app/widget/ActionModeView;

    check-cast v0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;

    invoke-virtual {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->getExpandState()I

    move-result v0

    iput v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCurrentExpandState:I

    iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCurrentResizable:Z

    invoke-virtual {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->setResizable(Z)V

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    iget v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCurrentExpandState:I

    invoke-virtual {v0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->setExpandState(I)V

    :goto_1
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    iget p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCurrentAccessibilityImportant:I

    invoke-virtual {v0, p0}, Landroid/view/ViewGroup;->setImportantForAccessibility(I)V

    :cond_2
    return-void
.end method""",
        'replacement': """.method hideForActionMode()V
    .registers 5

    goto :goto_3

    nop

    :goto_0
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionModeView:Lmiuix/appcompat/internal/app/widget/ActionModeView;

    goto :goto_24

    nop

    :goto_1
    invoke-virtual {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->setResizable(Z)V

    goto :goto_19

    nop

    :goto_2
    iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCurrentResizable:Z

    goto :goto_1e

    nop

    :goto_3
    iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mShowingForMode:Z

    goto :goto_1d

    nop

    :goto_4
    const v3, 0x8000

    goto :goto_26

    nop

    :goto_5
    invoke-virtual {v0, p0}, Landroid/view/ViewGroup;->setImportantForAccessibility(I)V

    :goto_6
    goto :goto_15

    nop

    :goto_7
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->getDisplayOptions()I

    move-result v2

    goto :goto_4

    nop

    :goto_8
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContainerView:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_25

    nop

    :goto_9
    const/4 v2, 0x1

    goto :goto_a

    nop

    :goto_a
    goto :goto_13

    :goto_b
    goto :goto_12

    nop

    :goto_c
    iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCurrentResizable:Z

    goto :goto_1

    nop

    :goto_d
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_7

    nop

    :goto_e
    const/4 v0, 0x0

    goto :goto_17

    nop

    :goto_f
    check-cast v0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;

    goto :goto_18

    nop

    :goto_10
    iget p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCurrentAccessibilityImportant:I

    goto :goto_5

    nop

    :goto_11
    invoke-direct {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->updateVisibility(Z)V

    goto :goto_2a

    nop

    :goto_12
    move v2, v0

    :goto_13
    goto :goto_27

    nop

    :goto_14
    if-nez v2, :cond_0

    goto :goto_b

    :cond_0
    goto :goto_9

    nop

    :goto_15
    return-void

    :goto_16
    iput-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCurrentResizable:Z

    goto :goto_0

    nop

    :goto_17
    iput-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mShowingForMode:Z

    goto :goto_d

    nop

    :goto_18
    invoke-virtual {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->isResizable()Z

    move-result v0

    goto :goto_16

    nop

    :goto_19
    goto :goto_21

    :goto_1a
    goto :goto_8

    nop

    :goto_1b
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_10

    nop

    :goto_1c
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_2b

    nop

    :goto_1d
    if-nez v0, :cond_1

    goto :goto_6

    :cond_1
    goto :goto_e

    nop

    :goto_1e
    invoke-virtual {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->setResizable(Z)V

    goto :goto_1c

    nop

    :goto_1f
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionModeView:Lmiuix/appcompat/internal/app/widget/ActionModeView;

    goto :goto_f

    nop

    :goto_20
    invoke-virtual {v0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->setExpandState(I)V

    :goto_21
    goto :goto_1b

    nop

    :goto_22
    iput v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCurrentExpandState:I

    goto :goto_2

    nop

    :goto_23
    instance-of v0, v0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;

    goto :goto_28

    nop

    :goto_24
    check-cast v0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;

    goto :goto_29

    nop

    :goto_25
    invoke-virtual {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->finishActionMode()V

    goto :goto_1f

    nop

    :goto_26
    and-int/2addr v2, v3

    goto :goto_14

    nop

    :goto_27
    invoke-virtual {v1, v2}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->onActionModeEnd(Z)V

    goto :goto_11

    nop

    :goto_28
    if-nez v0, :cond_2

    goto :goto_1a

    :cond_2
    goto :goto_c

    nop

    :goto_29
    invoke-virtual {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->getExpandState()I

    move-result v0

    goto :goto_22

    nop

    :goto_2a
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionModeView:Lmiuix/appcompat/internal/app/widget/ActionModeView;

    goto :goto_23

    nop

    :goto_2b
    iget v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCurrentExpandState:I

    goto :goto_20

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarImpl__isShowHideAnimationEnabled',
        'method': '.method isShowHideAnimationEnabled()Z',
        'method_name': 'isShowHideAnimationEnabled',
        'method_anchors': ['iget-boolean p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mShowHideAnimationEnabled:Z', 'return p0'],
        'type': 'method_replace',
        'search': """.method isShowHideAnimationEnabled()Z
    .registers 1

    iget-boolean p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mShowHideAnimationEnabled:Z

    return p0
.end method""",
        'replacement': """.method isShowHideAnimationEnabled()Z
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget-boolean p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mShowHideAnimationEnabled:Z

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
        'id': 'miuix_appcompat_internal_app_widget_ActionBarImpl__createActionBarCoordinateListener',
        'method': '.method protected createActionBarCoordinateListener()Lmiuix/appcompat/internal/app/widget/ActionBarCoordinateListener;',
        'method_name': 'createActionBarCoordinateListener',
        'method_anchors': ['new-instance v0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl$$ExternalSyntheticLambda0;', 'invoke-direct {v0, p0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl$$ExternalSyntheticLambda0;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarImpl;)V', 'return-object v0'],
        'type': 'method_replace',
        'search': """.method protected createActionBarCoordinateListener()Lmiuix/appcompat/internal/app/widget/ActionBarCoordinateListener;
    .registers 2

    new-instance v0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl$$ExternalSyntheticLambda0;

    invoke-direct {v0, p0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl$$ExternalSyntheticLambda0;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarImpl;)V

    return-object v0
.end method""",
        'replacement': """.method protected createActionBarCoordinateListener()Lmiuix/appcompat/internal/app/widget/ActionBarCoordinateListener;
    .registers 2

    goto :goto_1

    nop

    :goto_0
    invoke-direct {v0, p0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl$$ExternalSyntheticLambda0;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarImpl;)V

    goto :goto_2

    nop

    :goto_1
    new-instance v0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl$$ExternalSyntheticLambda0;

    goto :goto_0

    nop

    :goto_2
    return-object v0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarImpl__init',
        'method': '.method protected init(Landroid/view/ViewGroup;)V',
        'method_name': 'init',
        'method_anchors': ['if-nez p1, :cond_0', 'return-void', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContext:Landroid/content/Context;', 'sget v1, Lmiuix/appcompat/R$attr;->actionBarStrategy:I', 'invoke-static {v0, v1}, Lmiuix/internal/util/AttributeResolver;->resolveTypedValue(Landroid/content/Context;I)Landroid/util/TypedValue;', 'if-eqz v0, :cond_1', 'iget-object v0, v0, Landroid/util/TypedValue;->string:Ljava/lang/CharSequence;', 'invoke-interface {v0}, Ljava/lang/CharSequence;->toString()Ljava/lang/String;'],
        'type': 'method_replace',
        'search': """.method protected init(Landroid/view/ViewGroup;)V
    .registers 6

    if-nez p1, :cond_0

    return-void

    :cond_0
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContext:Landroid/content/Context;

    sget v1, Lmiuix/appcompat/R$attr;->actionBarStrategy:I

    invoke-static {v0, v1}, Lmiuix/internal/util/AttributeResolver;->resolveTypedValue(Landroid/content/Context;I)Landroid/util/TypedValue;

    move-result-object v0

    const/4 v1, 0x0

    if-eqz v0, :cond_1

    :try_start_0
    iget-object v0, v0, Landroid/util/TypedValue;->string:Ljava/lang/CharSequence;

    invoke-interface {v0}, Ljava/lang/CharSequence;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Ljava/lang/Class;->forName(Ljava/lang/String;)Ljava/lang/Class;

    move-result-object v0

    new-array v2, v1, [Ljava/lang/Class;

    const/4 v2, 0x0

    invoke-virtual {v0, v2}, Ljava/lang/Class;->getDeclaredConstructor([Ljava/lang/Class;)Ljava/lang/reflect/Constructor;

    move-result-object v0

    invoke-virtual {v0, v2}, Ljava/lang/reflect/Constructor;->newInstance([Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lmiuix/appcompat/app/strategy/IActionBarStrategy;

    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionBarStrategy:Lmiuix/appcompat/app/strategy/IActionBarStrategy;
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    :catch_0
    :cond_1
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContext:Landroid/content/Context;

    invoke-static {v0}, Lmiuix/core/util/EnvStateManager;->getWindowInfo(Landroid/content/Context;)Lmiuix/core/util/WindowBaseInfo;

    move-result-object v0

    iget v0, v0, Lmiuix/core/util/WindowBaseInfo;->windowMode:I

    iput v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mWindowMode:I

    move-object v0, p1

    check-cast v0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;

    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mOverlayLayout:Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;

    invoke-virtual {v0, p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->setActionBar(Lmiuix/appcompat/app/ActionBar;)V

    sget v0, Lmiuix/appcompat/R$id;->action_bar:I

    invoke-virtual {p1, v0}, Landroid/view/ViewGroup;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;

    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    if-eqz v0, :cond_2

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mExtraPaddingPolicy:Lmiuix/container/ExtraPaddingPolicy;

    if-eqz v2, :cond_2

    invoke-virtual {v0, v2}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->setExtraPaddingPolicy(Lmiuix/container/ExtraPaddingPolicy;)V

    :cond_2
    sget v0, Lmiuix/appcompat/R$id;->action_context_bar:I

    invoke-virtual {p1, v0}, Landroid/view/ViewGroup;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;

    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContextView:Lmiuix/appcompat/internal/app/widget/ActionBarContextView;

    sget v0, Lmiuix/appcompat/R$id;->action_bar_container:I

    invoke-virtual {p1, v0}, Landroid/view/ViewGroup;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContainerView:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    sget v0, Lmiuix/appcompat/R$id;->split_action_bar:I

    invoke-virtual {p1, v0}, Landroid/view/ViewGroup;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mSplitView:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    sget v0, Lmiuix/appcompat/R$id;->content_mask:I

    invoke-virtual {p1, v0}, Landroid/view/ViewGroup;->findViewById(I)Landroid/view/View;

    move-result-object p1

    iput-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContentMask:Landroid/view/View;

    if-eqz p1, :cond_3

    new-instance p1, Lmiuix/appcompat/internal/app/widget/ActionBarImpl$3;

    invoke-direct {p1, p0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl$3;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarImpl;)V

    iput-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContentMaskOnClickListener:Landroid/view/View$OnClickListener;

    :cond_3
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    if-nez p1, :cond_5

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContextView:Lmiuix/appcompat/internal/app/widget/ActionBarContextView;

    if-nez v0, :cond_5

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContainerView:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    if-eqz v0, :cond_4

    goto :goto_0

    :cond_4
    new-instance p1, Ljava/lang/IllegalStateException;

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object p0

    invoke-virtual {p0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object p0

    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string p0, " can only be used with a compatible window decor layout"

    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    invoke-direct {p1, p0}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    throw p1

    :cond_5
    :goto_0
    invoke-virtual {p1}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->isSplitActionBar()Z

    move-result p1

    iput p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContextDisplayMode:I

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    invoke-virtual {p1}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->getDisplayOptions()I

    move-result p1

    and-int/lit8 p1, p1, 0x4

    const/4 v0, 0x1

    if-eqz p1, :cond_6

    move p1, v0

    goto :goto_1

    :cond_6
    move p1, v1

    :goto_1
    if-eqz p1, :cond_7

    iput-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mDisplayHomeAsUpSet:Z

    :cond_7
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContext:Landroid/content/Context;

    invoke-static {v2}, Lmiuix/appcompat/internal/view/ActionBarPolicy;->get(Landroid/content/Context;)Lmiuix/appcompat/internal/view/ActionBarPolicy;

    move-result-object v2

    invoke-virtual {v2}, Lmiuix/appcompat/internal/view/ActionBarPolicy;->enableHomeButtonByDefault()Z

    move-result v3

    if-nez v3, :cond_9

    if-eqz p1, :cond_8

    goto :goto_2

    :cond_8
    move p1, v1

    goto :goto_3

    :cond_9
    :goto_2
    move p1, v0

    :goto_3
    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->setHomeButtonEnabled(Z)V

    invoke-virtual {v2}, Lmiuix/appcompat/internal/view/ActionBarPolicy;->hasEmbeddedTabs()Z

    move-result p1

    invoke-direct {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->setHasEmbeddedTabs(Z)V

    invoke-static {}, Lmiuix/core/util/MiuiBlurUtils;->isEnable()Z

    move-result p1

    if-eqz p1, :cond_a

    invoke-static {}, Lmiuix/internal/util/LiteUtils;->isCommonLiteStrategy()Z

    move-result p1

    if-nez p1, :cond_a

    goto :goto_4

    :cond_a
    move v0, v1

    :goto_4
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContainerView:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    if-eqz p1, :cond_b

    invoke-virtual {p1, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->setSupportBlur(Z)V

    :cond_b
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mSplitView:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    if-eqz p1, :cond_c

    invoke-virtual {p1, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->setSupportBlur(Z)V

    :cond_c
    if-eqz v0, :cond_f

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContext:Landroid/content/Context;

    sget v0, Lmiuix/appcompat/R$attr;->bgBlurOptions:I

    invoke-static {p1, v0, v1}, Lmiuix/internal/util/AttributeResolver;->resolveInt(Landroid/content/Context;II)I

    move-result p1

    if-eqz p1, :cond_f

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->getDisplayOptions()I

    move-result v0

    and-int/lit8 v1, p1, 0x1

    if-eqz v1, :cond_d

    const v1, 0x8000

    or-int/2addr v0, v1

    :cond_d
    and-int/lit8 p1, p1, 0x2

    if-eqz p1, :cond_e

    or-int/lit16 v0, v0, 0x4000

    :cond_e
    invoke-virtual {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->setDisplayOptions(I)V

    :cond_f
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionBarStrategy:Lmiuix/appcompat/app/strategy/IActionBarStrategy;

    if-nez p1, :cond_10

    new-instance p1, Lmiuix/appcompat/app/strategy/CommonActionBarStrategy;

    invoke-direct {p1}, Lmiuix/appcompat/app/strategy/CommonActionBarStrategy;-><init>()V

    iput-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionBarStrategy:Lmiuix/appcompat/app/strategy/IActionBarStrategy;

    :cond_10
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mOverlayLayout:Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;

    invoke-virtual {p1}, Landroid/widget/FrameLayout;->getViewTreeObserver()Landroid/view/ViewTreeObserver;

    move-result-object p1

    new-instance v0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl$4;

    invoke-direct {v0, p0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl$4;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarImpl;)V

    invoke-virtual {p1, v0}, Landroid/view/ViewTreeObserver;->addOnPreDrawListener(Landroid/view/ViewTreeObserver$OnPreDrawListener;)V

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mOverlayLayout:Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;

    new-instance v0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl$5;

    invoke-direct {v0, p0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl$5;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarImpl;)V

    invoke-virtual {p1, v0}, Landroid/widget/FrameLayout;->addOnLayoutChangeListener(Landroid/view/View$OnLayoutChangeListener;)V

    return-void
.end method""",
        'replacement': """.method protected init(Landroid/view/ViewGroup;)V
    .registers 6

    goto :goto_20

    nop

    :goto_0
    check-cast v0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_9

    nop

    :goto_1
    if-eqz v3, :cond_0

    goto :goto_87

    :cond_0
    goto :goto_f

    nop

    :goto_2
    sget v0, Lmiuix/appcompat/R$id;->action_bar_container:I

    goto :goto_8a

    nop

    :goto_3
    invoke-virtual {p1}, Landroid/widget/FrameLayout;->getViewTreeObserver()Landroid/view/ViewTreeObserver;

    move-result-object p1

    goto :goto_45

    nop

    :goto_4
    const-string p0, " can only be used with a compatible window decor layout"

    goto :goto_32

    nop

    :goto_5
    and-int/lit8 p1, p1, 0x2

    goto :goto_1d

    nop

    :goto_6
    if-nez v0, :cond_1

    goto :goto_89

    :cond_1
    goto :goto_74

    nop

    :goto_7
    if-eqz v0, :cond_2

    goto :goto_23

    :cond_2
    goto :goto_3a

    nop

    :goto_8
    invoke-direct {p1, p0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl$3;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarImpl;)V

    goto :goto_5a

    nop

    :goto_9
    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mSplitView:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_66

    nop

    :goto_a
    if-nez p1, :cond_3

    goto :goto_8e

    :cond_3
    goto :goto_8d

    nop

    :goto_b
    invoke-virtual {p1, v0}, Landroid/view/ViewGroup;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_0

    nop

    :goto_c
    return-void

    :goto_d
    invoke-virtual {p1, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->setSupportBlur(Z)V

    :goto_e
    goto :goto_69

    nop

    :goto_f
    if-nez p1, :cond_4

    goto :goto_60

    :cond_4
    goto :goto_5f

    nop

    :goto_10
    and-int/lit8 p1, p1, 0x4

    goto :goto_83

    nop

    :goto_11
    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_4

    nop

    :goto_12
    sget v1, Lmiuix/appcompat/R$attr;->actionBarStrategy:I

    goto :goto_4c

    nop

    :goto_13
    sget v0, Lmiuix/appcompat/R$id;->split_action_bar:I

    goto :goto_b

    nop

    :goto_14
    invoke-static {p1, v0, v1}, Lmiuix/internal/util/AttributeResolver;->resolveInt(Landroid/content/Context;II)I

    move-result p1

    goto :goto_62

    nop

    :goto_15
    new-instance p1, Lmiuix/appcompat/internal/app/widget/ActionBarImpl$3;

    goto :goto_8

    nop

    :goto_16
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_2f

    nop

    :goto_17
    if-nez v0, :cond_5

    goto :goto_4f

    :cond_5
    goto :goto_4e

    nop

    :goto_18
    iput-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionBarStrategy:Lmiuix/appcompat/app/strategy/IActionBarStrategy;

    :goto_19
    goto :goto_7b

    nop

    :goto_1a
    invoke-virtual {p1, v0}, Landroid/view/ViewTreeObserver;->addOnPreDrawListener(Landroid/view/ViewTreeObserver$OnPreDrawListener;)V

    goto :goto_64

    nop

    :goto_1b
    invoke-direct {p1, p0}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    goto :goto_22

    nop

    :goto_1c
    invoke-virtual {v2}, Lmiuix/appcompat/internal/view/ActionBarPolicy;->enableHomeButtonByDefault()Z

    move-result v3

    goto :goto_1

    nop

    :goto_1d
    if-nez p1, :cond_6

    goto :goto_2c

    :cond_6
    goto :goto_2b

    nop

    :goto_1e
    move v0, v1

    :goto_1f
    goto :goto_81

    nop

    :goto_20
    if-eqz p1, :cond_7

    goto :goto_79

    :cond_7
    goto :goto_78

    nop

    :goto_21
    if-eqz p1, :cond_8

    goto :goto_80

    :cond_8
    goto :goto_7f

    nop

    :goto_22
    throw p1

    :goto_23
    goto :goto_39

    nop

    :goto_24
    invoke-static {v0}, Lmiuix/core/util/EnvStateManager;->getWindowInfo(Landroid/content/Context;)Lmiuix/core/util/WindowBaseInfo;

    move-result-object v0

    goto :goto_42

    nop

    :goto_25
    check-cast v0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_38

    nop

    :goto_26
    invoke-direct {v0, p0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl$5;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarImpl;)V

    goto :goto_36

    nop

    :goto_27
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_47

    nop

    :goto_28
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContext:Landroid/content/Context;

    goto :goto_33

    nop

    :goto_29
    move-object v0, p1

    goto :goto_73

    nop

    :goto_2a
    if-nez v2, :cond_9

    goto :goto_6c

    :cond_9
    goto :goto_6b

    nop

    :goto_2b
    or-int/lit16 v0, v0, 0x4000

    :goto_2c
    goto :goto_88

    nop

    :goto_2d
    move p1, v1

    goto :goto_86

    nop

    :goto_2e
    new-instance v0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl$5;

    goto :goto_26

    nop

    :goto_2f
    invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object p0

    goto :goto_61

    nop

    :goto_30
    sget v0, Lmiuix/appcompat/R$attr;->bgBlurOptions:I

    goto :goto_14

    nop

    :goto_31
    move p1, v0

    goto :goto_40

    nop

    :goto_32
    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_54

    nop

    :goto_33
    invoke-static {v2}, Lmiuix/appcompat/internal/view/ActionBarPolicy;->get(Landroid/content/Context;)Lmiuix/appcompat/internal/view/ActionBarPolicy;

    move-result-object v2

    goto :goto_1c

    nop

    :goto_34
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContext:Landroid/content/Context;

    goto :goto_12

    nop

    :goto_35
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->getDisplayOptions()I

    move-result v0

    goto :goto_70

    nop

    :goto_36
    invoke-virtual {p1, v0}, Landroid/widget/FrameLayout;->addOnLayoutChangeListener(Landroid/view/View$OnLayoutChangeListener;)V

    goto :goto_c

    nop

    :goto_37
    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContextView:Lmiuix/appcompat/internal/app/widget/ActionBarContextView;

    goto :goto_2

    nop

    :goto_38
    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContainerView:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_13

    nop

    :goto_39
    invoke-virtual {p1}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->isSplitActionBar()Z

    move-result p1

    goto :goto_5e

    nop

    :goto_3a
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContainerView:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_17

    nop

    :goto_3b
    move p1, v0

    :goto_3c
    goto :goto_8f

    nop

    :goto_3d
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_4d

    nop

    :goto_3e
    if-nez p1, :cond_a

    goto :goto_5b

    :cond_a
    goto :goto_15

    nop

    :goto_3f
    check-cast v0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;

    goto :goto_37

    nop

    :goto_40
    goto :goto_68

    :goto_41
    goto :goto_67

    nop

    :goto_42
    iget v0, v0, Lmiuix/core/util/WindowBaseInfo;->windowMode:I

    goto :goto_8c

    nop

    :goto_43
    invoke-virtual {p1, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->setSupportBlur(Z)V

    :goto_44
    goto :goto_6

    nop

    :goto_45
    new-instance v0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl$4;

    goto :goto_49

    nop

    :goto_46
    iput-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContentMask:Landroid/view/View;

    goto :goto_3e

    nop

    :goto_47
    if-eqz p1, :cond_b

    goto :goto_23

    :cond_b
    goto :goto_75

    nop

    :goto_48
    new-instance p1, Lmiuix/appcompat/app/strategy/CommonActionBarStrategy;

    goto :goto_7a

    nop

    :goto_49
    invoke-direct {v0, p0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl$4;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarImpl;)V

    goto :goto_1a

    nop

    :goto_4a
    if-nez v0, :cond_c

    goto :goto_6c

    :cond_c
    goto :goto_57

    nop

    :goto_4b
    const/4 v1, 0x0

    goto :goto_55

    nop

    :goto_4c
    invoke-static {v0, v1}, Lmiuix/internal/util/AttributeResolver;->resolveTypedValue(Landroid/content/Context;I)Landroid/util/TypedValue;

    move-result-object v0

    goto :goto_4b

    nop

    :goto_4d
    invoke-virtual {p1}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->getDisplayOptions()I

    move-result p1

    goto :goto_10

    nop

    :goto_4e
    goto :goto_23

    :goto_4f
    goto :goto_63

    nop

    :goto_50
    invoke-virtual {v0, p0}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->setActionBar(Lmiuix/appcompat/app/ActionBar;)V

    goto :goto_84

    nop

    :goto_51
    invoke-virtual {p1, v0}, Landroid/view/ViewGroup;->findViewById(I)Landroid/view/View;

    move-result-object p1

    goto :goto_46

    nop

    :goto_52
    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_4a

    nop

    :goto_53
    invoke-virtual {p1, v0}, Landroid/view/ViewGroup;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_3f

    nop

    :goto_54
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    goto :goto_1b

    nop

    :goto_55
    if-nez v0, :cond_d

    goto :goto_56

    :cond_d
    :try_start_0
    iget-object v0, v0, Landroid/util/TypedValue;->string:Ljava/lang/CharSequence;

    invoke-interface {v0}, Ljava/lang/CharSequence;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Ljava/lang/Class;->forName(Ljava/lang/String;)Ljava/lang/Class;

    move-result-object v0

    new-array v2, v1, [Ljava/lang/Class;

    const/4 v2, 0x0

    invoke-virtual {v0, v2}, Ljava/lang/Class;->getDeclaredConstructor([Ljava/lang/Class;)Ljava/lang/reflect/Constructor;

    move-result-object v0

    invoke-virtual {v0, v2}, Ljava/lang/reflect/Constructor;->newInstance([Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lmiuix/appcompat/app/strategy/IActionBarStrategy;

    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionBarStrategy:Lmiuix/appcompat/app/strategy/IActionBarStrategy;
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    :catch_0
    :goto_56
    goto :goto_6e

    nop

    :goto_57
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mExtraPaddingPolicy:Lmiuix/container/ExtraPaddingPolicy;

    goto :goto_2a

    nop

    :goto_58
    sget v0, Lmiuix/appcompat/R$id;->action_context_bar:I

    goto :goto_53

    nop

    :goto_59
    if-nez p1, :cond_e

    goto :goto_e

    :cond_e
    goto :goto_d

    nop

    :goto_5a
    iput-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContentMaskOnClickListener:Landroid/view/View$OnClickListener;

    :goto_5b
    goto :goto_27

    nop

    :goto_5c
    or-int/2addr v0, v1

    :goto_5d
    goto :goto_5

    nop

    :goto_5e
    iput p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContextDisplayMode:I

    goto :goto_3d

    nop

    :goto_5f
    goto :goto_87

    :goto_60
    goto :goto_2d

    nop

    :goto_61
    invoke-virtual {p0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object p0

    goto :goto_11

    nop

    :goto_62
    if-nez p1, :cond_f

    goto :goto_89

    :cond_f
    goto :goto_35

    nop

    :goto_63
    new-instance p1, Ljava/lang/IllegalStateException;

    goto :goto_82

    nop

    :goto_64
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mOverlayLayout:Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;

    goto :goto_2e

    nop

    :goto_65
    if-nez p1, :cond_10

    goto :goto_80

    :cond_10
    goto :goto_6d

    nop

    :goto_66
    sget v0, Lmiuix/appcompat/R$id;->content_mask:I

    goto :goto_51

    nop

    :goto_67
    move p1, v1

    :goto_68
    goto :goto_a

    nop

    :goto_69
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mSplitView:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_76

    nop

    :goto_6a
    if-nez v1, :cond_11

    goto :goto_5d

    :cond_11
    goto :goto_71

    nop

    :goto_6b
    invoke-virtual {v0, v2}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->setExtraPaddingPolicy(Lmiuix/container/ExtraPaddingPolicy;)V

    :goto_6c
    goto :goto_58

    nop

    :goto_6d
    invoke-static {}, Lmiuix/internal/util/LiteUtils;->isCommonLiteStrategy()Z

    move-result p1

    goto :goto_21

    nop

    :goto_6e
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContext:Landroid/content/Context;

    goto :goto_24

    nop

    :goto_6f
    invoke-virtual {p1, v0}, Landroid/view/ViewGroup;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_85

    nop

    :goto_70
    and-int/lit8 v1, p1, 0x1

    goto :goto_6a

    nop

    :goto_71
    const v1, 0x8000

    goto :goto_5c

    nop

    :goto_72
    invoke-direct {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->setHasEmbeddedTabs(Z)V

    goto :goto_90

    nop

    :goto_73
    check-cast v0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;

    goto :goto_7e

    nop

    :goto_74
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContext:Landroid/content/Context;

    goto :goto_30

    nop

    :goto_75
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContextView:Lmiuix/appcompat/internal/app/widget/ActionBarContextView;

    goto :goto_7

    nop

    :goto_76
    if-nez p1, :cond_12

    goto :goto_44

    :cond_12
    goto :goto_43

    nop

    :goto_77
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionBarStrategy:Lmiuix/appcompat/app/strategy/IActionBarStrategy;

    goto :goto_8b

    nop

    :goto_78
    return-void

    :goto_79
    goto :goto_34

    nop

    :goto_7a
    invoke-direct {p1}, Lmiuix/appcompat/app/strategy/CommonActionBarStrategy;-><init>()V

    goto :goto_18

    nop

    :goto_7b
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mOverlayLayout:Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;

    goto :goto_3

    nop

    :goto_7c
    if-nez p1, :cond_13

    goto :goto_41

    :cond_13
    goto :goto_31

    nop

    :goto_7d
    invoke-virtual {v2}, Lmiuix/appcompat/internal/view/ActionBarPolicy;->hasEmbeddedTabs()Z

    move-result p1

    goto :goto_72

    nop

    :goto_7e
    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mOverlayLayout:Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;

    goto :goto_50

    nop

    :goto_7f
    goto :goto_1f

    :goto_80
    goto :goto_1e

    nop

    :goto_81
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContainerView:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_59

    nop

    :goto_82
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_16

    nop

    :goto_83
    const/4 v0, 0x1

    goto :goto_7c

    nop

    :goto_84
    sget v0, Lmiuix/appcompat/R$id;->action_bar:I

    goto :goto_6f

    nop

    :goto_85
    check-cast v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_52

    nop

    :goto_86
    goto :goto_3c

    :goto_87
    goto :goto_3b

    nop

    :goto_88
    invoke-virtual {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->setDisplayOptions(I)V

    :goto_89
    goto :goto_77

    nop

    :goto_8a
    invoke-virtual {p1, v0}, Landroid/view/ViewGroup;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_25

    nop

    :goto_8b
    if-eqz p1, :cond_14

    goto :goto_19

    :cond_14
    goto :goto_48

    nop

    :goto_8c
    iput v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mWindowMode:I

    goto :goto_29

    nop

    :goto_8d
    iput-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mDisplayHomeAsUpSet:Z

    :goto_8e
    goto :goto_28

    nop

    :goto_8f
    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->setHomeButtonEnabled(Z)V

    goto :goto_7d

    nop

    :goto_90
    invoke-static {}, Lmiuix/core/util/MiuiBlurUtils;->isEnable()Z

    move-result p1

    goto :goto_65

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarImpl__setExtraPaddingPolicy',
        'method': '.method setExtraPaddingPolicy(Lmiuix/container/ExtraPaddingPolicy;)V',
        'method_name': 'setExtraPaddingPolicy',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mExtraPaddingPolicy:Lmiuix/container/ExtraPaddingPolicy;', 'if-eq v0, p1, :cond_1', 'iput-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mExtraPaddingPolicy:Lmiuix/container/ExtraPaddingPolicy;', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionView:Lmiuix/appcompat/internal/app/widget/ActionBarView;', 'if-eqz v0, :cond_0', 'invoke-virtual {v0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->setExtraPaddingPolicy(Lmiuix/container/ExtraPaddingPolicy;)V', 'iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mSearchActionModeView:Lmiuix/appcompat/internal/app/widget/SearchActionModeView;', 'if-eqz p1, :cond_1'],
        'type': 'method_replace',
        'search': """.method setExtraPaddingPolicy(Lmiuix/container/ExtraPaddingPolicy;)V
    .registers 3

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mExtraPaddingPolicy:Lmiuix/container/ExtraPaddingPolicy;

    if-eq v0, p1, :cond_1

    iput-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mExtraPaddingPolicy:Lmiuix/container/ExtraPaddingPolicy;

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    if-eqz v0, :cond_0

    invoke-virtual {v0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->setExtraPaddingPolicy(Lmiuix/container/ExtraPaddingPolicy;)V

    :cond_0
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mSearchActionModeView:Lmiuix/appcompat/internal/app/widget/SearchActionModeView;

    if-eqz p1, :cond_1

    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mExtraPaddingPolicy:Lmiuix/container/ExtraPaddingPolicy;

    invoke-virtual {p1, p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->setExtraPaddingPolicy(Lmiuix/container/ExtraPaddingPolicy;)V

    :cond_1
    return-void
.end method""",
        'replacement': """.method setExtraPaddingPolicy(Lmiuix/container/ExtraPaddingPolicy;)V
    .registers 3

    goto :goto_b

    nop

    :goto_0
    if-nez v0, :cond_0

    goto :goto_9

    :cond_0
    goto :goto_8

    nop

    :goto_1
    return-void

    :goto_2
    if-nez p1, :cond_1

    goto :goto_7

    :cond_1
    goto :goto_5

    nop

    :goto_3
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mSearchActionModeView:Lmiuix/appcompat/internal/app/widget/SearchActionModeView;

    goto :goto_2

    nop

    :goto_4
    if-ne v0, p1, :cond_2

    goto :goto_7

    :cond_2
    goto :goto_c

    nop

    :goto_5
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mExtraPaddingPolicy:Lmiuix/container/ExtraPaddingPolicy;

    goto :goto_6

    nop

    :goto_6
    invoke-virtual {p1, p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->setExtraPaddingPolicy(Lmiuix/container/ExtraPaddingPolicy;)V

    :goto_7
    goto :goto_1

    nop

    :goto_8
    invoke-virtual {v0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->setExtraPaddingPolicy(Lmiuix/container/ExtraPaddingPolicy;)V

    :goto_9
    goto :goto_3

    nop

    :goto_a
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_0

    nop

    :goto_b
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mExtraPaddingPolicy:Lmiuix/container/ExtraPaddingPolicy;

    goto :goto_4

    nop

    :goto_c
    iput-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mExtraPaddingPolicy:Lmiuix/container/ExtraPaddingPolicy;

    goto :goto_a

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarImpl__showForActionMode',
        'method': '.method showForActionMode()V',
        'method_name': 'showForActionMode',
        'method_anchors': ['iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mShowingForMode:Z', 'if-nez v0, :cond_2', 'iput-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mShowingForMode:Z', 'invoke-direct {p0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->updateVisibility(Z)V', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->getExpandState()I', 'iput v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCurrentExpandState:I', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->isResizable()Z', 'iput-boolean v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCurrentResizable:Z'],
        'type': 'method_replace',
        'search': """.method showForActionMode()V
    .registers 6

    iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mShowingForMode:Z

    if-nez v0, :cond_2

    const/4 v0, 0x1

    iput-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mShowingForMode:Z

    const/4 v1, 0x0

    invoke-direct {p0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->updateVisibility(Z)V

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->getExpandState()I

    move-result v2

    iput v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCurrentExpandState:I

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->isResizable()Z

    move-result v2

    iput-boolean v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCurrentResizable:Z

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionModeView:Lmiuix/appcompat/internal/app/widget/ActionModeView;

    instance-of v2, v2, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;

    if-eqz v2, :cond_0

    invoke-virtual {p0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->setResizable(Z)V

    goto :goto_0

    :cond_0
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContainerView:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    invoke-virtual {v2}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->startActionMode()V

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionModeView:Lmiuix/appcompat/internal/app/widget/ActionModeView;

    check-cast v2, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;

    iget v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCurrentExpandState:I

    invoke-virtual {v2, v3}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->setExpandState(I)V

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionModeView:Lmiuix/appcompat/internal/app/widget/ActionModeView;

    check-cast v2, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;

    iget-boolean v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCurrentResizable:Z

    invoke-virtual {v2, v3}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->setResizable(Z)V

    :goto_0
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    invoke-virtual {v2}, Landroid/view/ViewGroup;->getImportantForAccessibility()I

    move-result v2

    iput v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCurrentAccessibilityImportant:I

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    const/4 v3, 0x4

    invoke-virtual {v2, v3}, Landroid/view/ViewGroup;->setImportantForAccessibility(I)V

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    iget-object v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionModeView:Lmiuix/appcompat/internal/app/widget/ActionModeView;

    instance-of v3, v3, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->getDisplayOptions()I

    move-result p0

    const v4, 0x8000

    and-int/2addr p0, v4

    if-eqz p0, :cond_1

    goto :goto_1

    :cond_1
    move v0, v1

    :goto_1
    invoke-virtual {v2, v3, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->onActionModeStart(ZZ)V

    :cond_2
    return-void
.end method""",
        'replacement': """.method showForActionMode()V
    .registers 6

    goto :goto_27

    nop

    :goto_0
    const/4 v1, 0x0

    goto :goto_1e

    nop

    :goto_1
    instance-of v2, v2, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;

    goto :goto_2c

    nop

    :goto_2
    invoke-virtual {v2, v3}, Landroid/view/ViewGroup;->setImportantForAccessibility(I)V

    goto :goto_a

    nop

    :goto_3
    iget-object v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionModeView:Lmiuix/appcompat/internal/app/widget/ActionModeView;

    goto :goto_6

    nop

    :goto_4
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->getDisplayOptions()I

    move-result p0

    goto :goto_f

    nop

    :goto_5
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContainerView:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_12

    nop

    :goto_6
    instance-of v3, v3, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;

    goto :goto_4

    nop

    :goto_7
    iput-boolean v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCurrentResizable:Z

    goto :goto_b

    nop

    :goto_8
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->isResizable()Z

    move-result v2

    goto :goto_7

    nop

    :goto_9
    and-int/2addr p0, v4

    goto :goto_1d

    nop

    :goto_a
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_3

    nop

    :goto_b
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionModeView:Lmiuix/appcompat/internal/app/widget/ActionModeView;

    goto :goto_1

    nop

    :goto_c
    iput v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCurrentAccessibilityImportant:I

    goto :goto_15

    nop

    :goto_d
    move v0, v1

    :goto_e
    goto :goto_16

    nop

    :goto_f
    const v4, 0x8000

    goto :goto_9

    nop

    :goto_10
    check-cast v2, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;

    goto :goto_29

    nop

    :goto_11
    return-void

    :goto_12
    invoke-virtual {v2}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->startActionMode()V

    goto :goto_1c

    nop

    :goto_13
    goto :goto_19

    :goto_14
    goto :goto_5

    nop

    :goto_15
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_2d

    nop

    :goto_16
    invoke-virtual {v2, v3, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->onActionModeStart(ZZ)V

    :goto_17
    goto :goto_11

    nop

    :goto_18
    invoke-virtual {v2, v3}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->setResizable(Z)V

    :goto_19
    goto :goto_2b

    nop

    :goto_1a
    invoke-virtual {p0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->setResizable(Z)V

    goto :goto_13

    nop

    :goto_1b
    iput v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCurrentExpandState:I

    goto :goto_8

    nop

    :goto_1c
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionModeView:Lmiuix/appcompat/internal/app/widget/ActionModeView;

    goto :goto_10

    nop

    :goto_1d
    if-nez p0, :cond_0

    goto :goto_26

    :cond_0
    goto :goto_25

    nop

    :goto_1e
    invoke-direct {p0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->updateVisibility(Z)V

    goto :goto_22

    nop

    :goto_1f
    if-eqz v0, :cond_1

    goto :goto_17

    :cond_1
    goto :goto_2e

    nop

    :goto_20
    iput-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mShowingForMode:Z

    goto :goto_0

    nop

    :goto_21
    iget-boolean v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCurrentResizable:Z

    goto :goto_18

    nop

    :goto_22
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->getExpandState()I

    move-result v2

    goto :goto_1b

    nop

    :goto_23
    invoke-virtual {v2}, Landroid/view/ViewGroup;->getImportantForAccessibility()I

    move-result v2

    goto :goto_c

    nop

    :goto_24
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionModeView:Lmiuix/appcompat/internal/app/widget/ActionModeView;

    goto :goto_2a

    nop

    :goto_25
    goto :goto_e

    :goto_26
    goto :goto_d

    nop

    :goto_27
    iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mShowingForMode:Z

    goto :goto_1f

    nop

    :goto_28
    invoke-virtual {v2, v3}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->setExpandState(I)V

    goto :goto_24

    nop

    :goto_29
    iget v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCurrentExpandState:I

    goto :goto_28

    nop

    :goto_2a
    check-cast v2, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;

    goto :goto_21

    nop

    :goto_2b
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mActionView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_23

    nop

    :goto_2c
    if-nez v2, :cond_2

    goto :goto_14

    :cond_2
    goto :goto_1a

    nop

    :goto_2d
    const/4 v3, 0x4

    goto :goto_2

    nop

    :goto_2e
    const/4 v0, 0x1

    goto :goto_20

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarImpl__updateContentInsetForNestedObserver',
        'method': '.method updateContentInsetForNestedObserver(Landroid/graphics/Rect;)V',
        'method_name': 'updateContentInsetForNestedObserver',
        'method_anchors': ['iput-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContentInset:Landroid/graphics/Rect;', 'iget v0, p1, Landroid/graphics/Rect;->top:I', 'iget v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContentInsetTop:I', 'iput v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContentInsetTop:I', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mNestedContentInsetObserverSet:Ljava/util/HashSet;', 'invoke-virtual {v0}, Ljava/util/HashSet;->iterator()Ljava/util/Iterator;', 'invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z', 'if-eqz v2, :cond_0'],
        'type': 'method_replace',
        'search': """.method updateContentInsetForNestedObserver(Landroid/graphics/Rect;)V
    .registers 7

    iput-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContentInset:Landroid/graphics/Rect;

    iget v0, p1, Landroid/graphics/Rect;->top:I

    iget v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContentInsetTop:I

    sub-int v1, v0, v1

    iput v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContentInsetTop:I

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mNestedContentInsetObserverSet:Ljava/util/HashSet;

    invoke-virtual {v0}, Ljava/util/HashSet;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_0
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    if-eqz v2, :cond_0

    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v2

    check-cast v2, Lmiuix/core/view/NestedContentInsetObserver;

    invoke-interface {v2, p1}, Lmiuix/core/view/NestedContentInsetObserver;->onContentInsetChanged(Landroid/graphics/Rect;)V

    goto :goto_0

    :cond_0
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCoordinateOffsetViewSet:Ljava/util/HashMap;

    invoke-virtual {p1}, Ljava/util/HashMap;->keySet()Ljava/util/Set;

    move-result-object p1

    invoke-interface {p1}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object p1

    :cond_1
    :goto_1
    invoke-interface {p1}, Ljava/util/Iterator;->hasNext()Z

    move-result v0

    if-eqz v0, :cond_5

    invoke-interface {p1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/view/View;

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCoordinateOffsetViewSet:Ljava/util/HashMap;

    invoke-virtual {v2, v0}, Ljava/util/HashMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v2

    check-cast v2, Ljava/lang/Integer;

    if-nez v2, :cond_2

    goto :goto_1

    :cond_2
    if-eqz v1, :cond_1

    sget-object v3, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->UNINITIALIZED_OFFSET:Ljava/lang/Integer;

    invoke-virtual {v2, v3}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v3

    const/4 v4, 0x0

    if-eqz v3, :cond_3

    invoke-static {v4}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v2

    goto :goto_2

    :cond_3
    invoke-virtual {v2}, Ljava/lang/Integer;->intValue()I

    move-result v3

    if-nez v3, :cond_4

    goto :goto_1

    :cond_4
    :goto_2
    invoke-virtual {v2}, Ljava/lang/Integer;->intValue()I

    move-result v2

    add-int/2addr v2, v1

    invoke-static {v4, v2}, Ljava/lang/Math;->max(II)I

    move-result v2

    iget-object v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCoordinateOffsetViewSet:Ljava/util/HashMap;

    invoke-static {v2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v4

    invoke-virtual {v3, v0, v4}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    invoke-direct {p0, v0, v2}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->doUpdateTopOffsetForCoordinateView(Landroid/view/View;I)V

    goto :goto_1

    :cond_5
    return-void
.end method""",
        'replacement': """.method updateContentInsetForNestedObserver(Landroid/graphics/Rect;)V
    .registers 7

    goto :goto_0

    nop

    :goto_0
    iput-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContentInset:Landroid/graphics/Rect;

    goto :goto_24

    nop

    :goto_1
    invoke-virtual {v2}, Ljava/lang/Integer;->intValue()I

    move-result v3

    goto :goto_b

    nop

    :goto_2
    goto :goto_15

    :goto_3
    goto :goto_5

    nop

    :goto_4
    iget-object v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCoordinateOffsetViewSet:Ljava/util/HashMap;

    goto :goto_7

    nop

    :goto_5
    if-nez v1, :cond_0

    goto :goto_15

    :cond_0
    goto :goto_8

    nop

    :goto_6
    if-nez v2, :cond_1

    goto :goto_17

    :cond_1
    goto :goto_25

    nop

    :goto_7
    invoke-static {v2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v4

    goto :goto_19

    nop

    :goto_8
    sget-object v3, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->UNINITIALIZED_OFFSET:Ljava/lang/Integer;

    goto :goto_29

    nop

    :goto_9
    return-void

    :goto_a
    check-cast v0, Landroid/view/View;

    goto :goto_31

    nop

    :goto_b
    if-eqz v3, :cond_2

    goto :goto_30

    :cond_2
    goto :goto_2f

    nop

    :goto_c
    invoke-static {v4}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v2

    goto :goto_1b

    nop

    :goto_d
    invoke-virtual {v2, v0}, Ljava/util/HashMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v2

    goto :goto_23

    nop

    :goto_e
    if-nez v3, :cond_3

    goto :goto_1c

    :cond_3
    goto :goto_c

    nop

    :goto_f
    const/4 v4, 0x0

    goto :goto_e

    nop

    :goto_10
    invoke-virtual {v0}, Ljava/util/HashSet;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_11
    goto :goto_21

    nop

    :goto_12
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCoordinateOffsetViewSet:Ljava/util/HashMap;

    goto :goto_32

    nop

    :goto_13
    invoke-virtual {v2}, Ljava/lang/Integer;->intValue()I

    move-result v2

    goto :goto_1f

    nop

    :goto_14
    invoke-interface {p1}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object p1

    :goto_15
    goto :goto_18

    nop

    :goto_16
    goto :goto_11

    :goto_17
    goto :goto_12

    nop

    :goto_18
    invoke-interface {p1}, Ljava/util/Iterator;->hasNext()Z

    move-result v0

    goto :goto_2b

    nop

    :goto_19
    invoke-virtual {v3, v0, v4}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_27

    nop

    :goto_1a
    invoke-interface {v2, p1}, Lmiuix/core/view/NestedContentInsetObserver;->onContentInsetChanged(Landroid/graphics/Rect;)V

    goto :goto_16

    nop

    :goto_1b
    goto :goto_30

    :goto_1c
    goto :goto_1

    nop

    :goto_1d
    goto :goto_15

    :goto_1e
    goto :goto_9

    nop

    :goto_1f
    add-int/2addr v2, v1

    goto :goto_2d

    nop

    :goto_20
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mNestedContentInsetObserverSet:Ljava/util/HashSet;

    goto :goto_10

    nop

    :goto_21
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    goto :goto_6

    nop

    :goto_22
    if-eqz v2, :cond_4

    goto :goto_3

    :cond_4
    goto :goto_2

    nop

    :goto_23
    check-cast v2, Ljava/lang/Integer;

    goto :goto_22

    nop

    :goto_24
    iget v0, p1, Landroid/graphics/Rect;->top:I

    goto :goto_2c

    nop

    :goto_25
    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v2

    goto :goto_28

    nop

    :goto_26
    iput v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContentInsetTop:I

    goto :goto_20

    nop

    :goto_27
    invoke-direct {p0, v0, v2}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->doUpdateTopOffsetForCoordinateView(Landroid/view/View;I)V

    goto :goto_1d

    nop

    :goto_28
    check-cast v2, Lmiuix/core/view/NestedContentInsetObserver;

    goto :goto_1a

    nop

    :goto_29
    invoke-virtual {v2, v3}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v3

    goto :goto_f

    nop

    :goto_2a
    invoke-interface {p1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v0

    goto :goto_a

    nop

    :goto_2b
    if-nez v0, :cond_5

    goto :goto_1e

    :cond_5
    goto :goto_2a

    nop

    :goto_2c
    iget v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContentInsetTop:I

    goto :goto_2e

    nop

    :goto_2d
    invoke-static {v4, v2}, Ljava/lang/Math;->max(II)I

    move-result v2

    goto :goto_4

    nop

    :goto_2e
    sub-int v1, v0, v1

    goto :goto_26

    nop

    :goto_2f
    goto :goto_15

    :goto_30
    goto :goto_13

    nop

    :goto_31
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCoordinateOffsetViewSet:Ljava/util/HashMap;

    goto :goto_d

    nop

    :goto_32
    invoke-virtual {p1}, Ljava/util/HashMap;->keySet()Ljava/util/Set;

    move-result-object p1

    goto :goto_14

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarImpl__updateCoordinateOffsetView',
        'method': '.method updateCoordinateOffsetView()V',
        'method_name': 'updateCoordinateOffsetView',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCoordinateOffsetViewSet:Ljava/util/HashMap;', 'invoke-virtual {v0}, Ljava/util/HashMap;->size()I', 'if-nez v0, :cond_0', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mNestedContentInsetObserverSet:Ljava/util/HashSet;', 'invoke-virtual {v0}, Ljava/util/HashSet;->size()I', 'if-nez v0, :cond_0', 'iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContainerView:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;', 'invoke-virtual {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->setActionBarCoordinateListener(Lmiuix/appcompat/internal/app/widget/ActionBarCoordinateListener;)V'],
        'type': 'method_replace',
        'search': """.method updateCoordinateOffsetView()V
    .registers 4

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCoordinateOffsetViewSet:Ljava/util/HashMap;

    invoke-virtual {v0}, Ljava/util/HashMap;->size()I

    move-result v0

    if-nez v0, :cond_0

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mNestedContentInsetObserverSet:Ljava/util/HashSet;

    invoke-virtual {v0}, Ljava/util/HashSet;->size()I

    move-result v0

    if-nez v0, :cond_0

    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContainerView:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->setActionBarCoordinateListener(Lmiuix/appcompat/internal/app/widget/ActionBarCoordinateListener;)V

    return-void

    :cond_0
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCoordinateOffsetViewSet:Ljava/util/HashMap;

    invoke-virtual {v0}, Ljava/util/HashMap;->keySet()Ljava/util/Set;

    move-result-object v0

    invoke-interface {v0}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_0
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_1

    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Landroid/view/View;

    invoke-direct {p0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->getCoordinateOffsetViewTopOffsetOrDefault(Landroid/view/View;)Ljava/lang/Integer;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/Integer;->intValue()I

    move-result v2

    invoke-direct {p0, v1, v2}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->doUpdateTopOffsetForCoordinateView(Landroid/view/View;I)V

    goto :goto_0

    :cond_1
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mNestedContentInsetObserverSet:Ljava/util/HashSet;

    invoke-virtual {v0}, Ljava/util/HashSet;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_1
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_2

    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lmiuix/core/view/NestedContentInsetObserver;

    check-cast v1, Landroid/view/View;

    const/4 v2, 0x0

    invoke-direct {p0, v1, v2}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->doUpdateTopOffsetForCoordinateView(Landroid/view/View;I)V

    goto :goto_1

    :cond_2
    return-void
.end method""",
        'replacement': """.method updateCoordinateOffsetView()V
    .registers 4

    goto :goto_20

    nop

    :goto_0
    const/4 v0, 0x0

    goto :goto_23

    nop

    :goto_1
    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    goto :goto_f

    nop

    :goto_2
    invoke-virtual {v2}, Ljava/lang/Integer;->intValue()I

    move-result v2

    goto :goto_1d

    nop

    :goto_3
    return-void

    :goto_4
    if-nez v1, :cond_0

    goto :goto_d

    :cond_0
    goto :goto_1

    nop

    :goto_5
    if-eqz v0, :cond_1

    goto :goto_11

    :cond_1
    goto :goto_17

    nop

    :goto_6
    invoke-virtual {v0}, Ljava/util/HashSet;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_7
    goto :goto_1f

    nop

    :goto_8
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mNestedContentInsetObserverSet:Ljava/util/HashSet;

    goto :goto_6

    nop

    :goto_9
    check-cast v1, Lmiuix/core/view/NestedContentInsetObserver;

    goto :goto_b

    nop

    :goto_a
    if-nez v1, :cond_2

    goto :goto_15

    :cond_2
    goto :goto_16

    nop

    :goto_b
    check-cast v1, Landroid/view/View;

    goto :goto_1b

    nop

    :goto_c
    goto :goto_1a

    :goto_d
    goto :goto_8

    nop

    :goto_e
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCoordinateOffsetViewSet:Ljava/util/HashMap;

    goto :goto_24

    nop

    :goto_f
    check-cast v1, Landroid/view/View;

    goto :goto_1e

    nop

    :goto_10
    return-void

    :goto_11
    goto :goto_e

    nop

    :goto_12
    if-eqz v0, :cond_3

    goto :goto_11

    :cond_3
    goto :goto_18

    nop

    :goto_13
    invoke-direct {p0, v1, v2}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->doUpdateTopOffsetForCoordinateView(Landroid/view/View;I)V

    goto :goto_14

    nop

    :goto_14
    goto :goto_7

    :goto_15
    goto :goto_3

    nop

    :goto_16
    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    goto :goto_9

    nop

    :goto_17
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mNestedContentInsetObserverSet:Ljava/util/HashSet;

    goto :goto_1c

    nop

    :goto_18
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContainerView:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_0

    nop

    :goto_19
    invoke-interface {v0}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_1a
    goto :goto_21

    nop

    :goto_1b
    const/4 v2, 0x0

    goto :goto_13

    nop

    :goto_1c
    invoke-virtual {v0}, Ljava/util/HashSet;->size()I

    move-result v0

    goto :goto_12

    nop

    :goto_1d
    invoke-direct {p0, v1, v2}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->doUpdateTopOffsetForCoordinateView(Landroid/view/View;I)V

    goto :goto_c

    nop

    :goto_1e
    invoke-direct {p0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->getCoordinateOffsetViewTopOffsetOrDefault(Landroid/view/View;)Ljava/lang/Integer;

    move-result-object v2

    goto :goto_2

    nop

    :goto_1f
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    goto :goto_a

    nop

    :goto_20
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCoordinateOffsetViewSet:Ljava/util/HashMap;

    goto :goto_22

    nop

    :goto_21
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    goto :goto_4

    nop

    :goto_22
    invoke-virtual {v0}, Ljava/util/HashMap;->size()I

    move-result v0

    goto :goto_5

    nop

    :goto_23
    invoke-virtual {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->setActionBarCoordinateListener(Lmiuix/appcompat/internal/app/widget/ActionBarCoordinateListener;)V

    goto :goto_10

    nop

    :goto_24
    invoke-virtual {v0}, Ljava/util/HashMap;->keySet()Ljava/util/Set;

    move-result-object v0

    goto :goto_19

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarImpl__updateTopOffsetOnNestedPreScroll',
        'method': '.method updateTopOffsetOnNestedPreScroll(Landroid/view/View;I)I',
        'method_name': 'updateTopOffsetOnNestedPreScroll',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCoordinateOffsetViewSet:Ljava/util/HashMap;', 'invoke-virtual {v0, p1}, Ljava/util/HashMap;->containsKey(Ljava/lang/Object;)Z', 'if-eqz v0, :cond_0', 'invoke-direct {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->getCoordinateOffsetViewTopOffsetOrDefault(Landroid/view/View;)Ljava/lang/Integer;', 'invoke-virtual {v0}, Ljava/lang/Integer;->intValue()I', 'if-le v1, p2, :cond_0', 'iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCoordinateOffsetViewSet:Ljava/util/HashMap;', 'invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;'],
        'type': 'method_replace',
        'search': """.method updateTopOffsetOnNestedPreScroll(Landroid/view/View;I)I
    .registers 6

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCoordinateOffsetViewSet:Ljava/util/HashMap;

    invoke-virtual {v0, p1}, Ljava/util/HashMap;->containsKey(Ljava/lang/Object;)Z

    move-result v0

    if-eqz v0, :cond_0

    invoke-direct {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->getCoordinateOffsetViewTopOffsetOrDefault(Landroid/view/View;)Ljava/lang/Integer;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/Integer;->intValue()I

    move-result v1

    if-le v1, p2, :cond_0

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCoordinateOffsetViewSet:Ljava/util/HashMap;

    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v2

    invoke-virtual {v1, p1, v2}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    invoke-direct {p0, p1, p2}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->doUpdateTopOffsetForCoordinateView(Landroid/view/View;I)V

    invoke-virtual {v0}, Ljava/lang/Integer;->intValue()I

    move-result p0

    sub-int/2addr p0, p2

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method updateTopOffsetOnNestedPreScroll(Landroid/view/View;I)I
    .registers 6

    goto :goto_8

    nop

    :goto_0
    if-nez v0, :cond_0

    goto :goto_a

    :cond_0
    goto :goto_3

    nop

    :goto_1
    invoke-virtual {v1, p1, v2}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_d

    nop

    :goto_2
    return p0

    :goto_3
    invoke-direct {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->getCoordinateOffsetViewTopOffsetOrDefault(Landroid/view/View;)Ljava/lang/Integer;

    move-result-object v0

    goto :goto_e

    nop

    :goto_4
    invoke-virtual {v0}, Ljava/lang/Integer;->intValue()I

    move-result p0

    goto :goto_b

    nop

    :goto_5
    if-gt v1, p2, :cond_1

    goto :goto_a

    :cond_1
    goto :goto_f

    nop

    :goto_6
    const/4 p0, 0x0

    goto :goto_2

    nop

    :goto_7
    invoke-virtual {v0, p1}, Ljava/util/HashMap;->containsKey(Ljava/lang/Object;)Z

    move-result v0

    goto :goto_0

    nop

    :goto_8
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCoordinateOffsetViewSet:Ljava/util/HashMap;

    goto :goto_7

    nop

    :goto_9
    return p0

    :goto_a
    goto :goto_6

    nop

    :goto_b
    sub-int/2addr p0, p2

    goto :goto_9

    nop

    :goto_c
    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v2

    goto :goto_1

    nop

    :goto_d
    invoke-direct {p0, p1, p2}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->doUpdateTopOffsetForCoordinateView(Landroid/view/View;I)V

    goto :goto_4

    nop

    :goto_e
    invoke-virtual {v0}, Ljava/lang/Integer;->intValue()I

    move-result v1

    goto :goto_5

    nop

    :goto_f
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCoordinateOffsetViewSet:Ljava/util/HashMap;

    goto :goto_c

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarImpl__updateTopOffsetOnNestedScroll',
        'method': '.method updateTopOffsetOnNestedScroll(Landroid/view/View;I)I',
        'method_name': 'updateTopOffsetOnNestedScroll',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCoordinateOffsetViewSet:Ljava/util/HashMap;', 'invoke-virtual {v0}, Ljava/util/HashMap;->keySet()Ljava/util/Set;', 'invoke-interface {v0}, Ljava/util/Set;->iterator()Ljava/util/Iterator;', 'invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z', 'if-eqz v3, :cond_2', 'invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;', 'check-cast v3, Landroid/view/View;', 'invoke-direct {p0, v3}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->getCoordinateOffsetViewTopOffsetOrDefault(Landroid/view/View;)Ljava/lang/Integer;'],
        'type': 'method_replace',
        'search': """.method updateTopOffsetOnNestedScroll(Landroid/view/View;I)I
    .registers 11

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCoordinateOffsetViewSet:Ljava/util/HashMap;

    invoke-virtual {v0}, Ljava/util/HashMap;->keySet()Ljava/util/Set;

    move-result-object v0

    invoke-interface {v0}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object v0

    const/4 v1, 0x0

    move v2, v1

    :cond_0
    :goto_0
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v3

    if-eqz v3, :cond_2

    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v3

    check-cast v3, Landroid/view/View;

    invoke-direct {p0, v3}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->getCoordinateOffsetViewTopOffsetOrDefault(Landroid/view/View;)Ljava/lang/Integer;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/Integer;->intValue()I

    move-result v4

    sub-int v5, v4, p2

    iget-object v6, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContentInset:Landroid/graphics/Rect;

    if-nez v6, :cond_1

    move v6, v1

    goto :goto_1

    :cond_1
    iget v6, v6, Landroid/graphics/Rect;->top:I

    :goto_1
    invoke-static {v5, v6}, Ljava/lang/Math;->min(II)I

    move-result v5

    if-ge v4, v5, :cond_0

    iget-object v6, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCoordinateOffsetViewSet:Ljava/util/HashMap;

    invoke-static {v5}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v7

    invoke-virtual {v6, v3, v7}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    invoke-direct {p0, v3, v5}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->doUpdateTopOffsetForCoordinateView(Landroid/view/View;I)V

    if-ne p1, v3, :cond_0

    sub-int v2, v4, v5

    goto :goto_0

    :cond_2
    return v2
.end method""",
        'replacement': """.method updateTopOffsetOnNestedScroll(Landroid/view/View;I)I
    .registers 11

    goto :goto_10

    nop

    :goto_0
    sub-int v2, v4, v5

    goto :goto_6

    nop

    :goto_1
    if-lt v4, v5, :cond_0

    goto :goto_1b

    :cond_0
    goto :goto_9

    nop

    :goto_2
    invoke-direct {p0, v3, v5}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->doUpdateTopOffsetForCoordinateView(Landroid/view/View;I)V

    goto :goto_1d

    nop

    :goto_3
    if-eqz v6, :cond_1

    goto :goto_19

    :cond_1
    goto :goto_b

    nop

    :goto_4
    sub-int v5, v4, p2

    goto :goto_13

    nop

    :goto_5
    const/4 v1, 0x0

    goto :goto_1a

    nop

    :goto_6
    goto :goto_1b

    :goto_7
    goto :goto_1e

    nop

    :goto_8
    invoke-static {v5}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v7

    goto :goto_14

    nop

    :goto_9
    iget-object v6, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCoordinateOffsetViewSet:Ljava/util/HashMap;

    goto :goto_8

    nop

    :goto_a
    invoke-static {v5, v6}, Ljava/lang/Math;->min(II)I

    move-result v5

    goto :goto_1

    nop

    :goto_b
    move v6, v1

    goto :goto_18

    nop

    :goto_c
    if-nez v3, :cond_2

    goto :goto_7

    :cond_2
    goto :goto_17

    nop

    :goto_d
    invoke-virtual {v0}, Ljava/util/HashMap;->keySet()Ljava/util/Set;

    move-result-object v0

    goto :goto_e

    nop

    :goto_e
    invoke-interface {v0}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object v0

    goto :goto_5

    nop

    :goto_f
    invoke-virtual {v4}, Ljava/lang/Integer;->intValue()I

    move-result v4

    goto :goto_4

    nop

    :goto_10
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCoordinateOffsetViewSet:Ljava/util/HashMap;

    goto :goto_d

    nop

    :goto_11
    check-cast v3, Landroid/view/View;

    goto :goto_1c

    nop

    :goto_12
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v3

    goto :goto_c

    nop

    :goto_13
    iget-object v6, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContentInset:Landroid/graphics/Rect;

    goto :goto_3

    nop

    :goto_14
    invoke-virtual {v6, v3, v7}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_2

    nop

    :goto_15
    iget v6, v6, Landroid/graphics/Rect;->top:I

    :goto_16
    goto :goto_a

    nop

    :goto_17
    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v3

    goto :goto_11

    nop

    :goto_18
    goto :goto_16

    :goto_19
    goto :goto_15

    nop

    :goto_1a
    move v2, v1

    :goto_1b
    goto :goto_12

    nop

    :goto_1c
    invoke-direct {p0, v3}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->getCoordinateOffsetViewTopOffsetOrDefault(Landroid/view/View;)Ljava/lang/Integer;

    move-result-object v4

    goto :goto_f

    nop

    :goto_1d
    if-eq p1, v3, :cond_3

    goto :goto_1b

    :cond_3
    goto :goto_0

    nop

    :goto_1e
    return v2
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarImpl__updateTopOffsetOnPostScroll',
        'method': '.method updateTopOffsetOnPostScroll(Landroid/view/View;I)V',
        'method_name': 'updateTopOffsetOnPostScroll',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCoordinateOffsetViewSet:Ljava/util/HashMap;', 'invoke-virtual {v0}, Ljava/util/HashMap;->keySet()Ljava/util/Set;', 'invoke-interface {v0}, Ljava/util/Set;->iterator()Ljava/util/Iterator;', 'invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z', 'if-eqz v1, :cond_2', 'invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;', 'check-cast v1, Landroid/view/View;', 'if-ne p1, v1, :cond_0'],
        'type': 'method_replace',
        'search': """.method updateTopOffsetOnPostScroll(Landroid/view/View;I)V
    .registers 8

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCoordinateOffsetViewSet:Ljava/util/HashMap;

    invoke-virtual {v0}, Ljava/util/HashMap;->keySet()Ljava/util/Set;

    move-result-object v0

    invoke-interface {v0}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :cond_0
    :goto_0
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_2

    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Landroid/view/View;

    if-ne p1, v1, :cond_0

    invoke-direct {p0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->getCoordinateOffsetViewTopOffsetOrDefault(Landroid/view/View;)Ljava/lang/Integer;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/Integer;->intValue()I

    move-result v2

    iget-object v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContentInset:Landroid/graphics/Rect;

    if-nez v3, :cond_1

    const/4 v3, 0x0

    goto :goto_1

    :cond_1
    iget v3, v3, Landroid/graphics/Rect;->top:I

    :goto_1
    invoke-static {p2, v3}, Ljava/lang/Math;->min(II)I

    move-result v3

    if-eq v2, v3, :cond_0

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCoordinateOffsetViewSet:Ljava/util/HashMap;

    invoke-static {v3}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v4

    invoke-virtual {v2, v1, v4}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    invoke-direct {p0, v1, v3}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->doUpdateTopOffsetForCoordinateView(Landroid/view/View;I)V

    goto :goto_0

    :cond_2
    return-void
.end method""",
        'replacement': """.method updateTopOffsetOnPostScroll(Landroid/view/View;I)V
    .registers 8

    goto :goto_12

    nop

    :goto_0
    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    goto :goto_f

    nop

    :goto_1
    iget-object v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mContentInset:Landroid/graphics/Rect;

    goto :goto_13

    nop

    :goto_2
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    goto :goto_a

    nop

    :goto_3
    if-eq p1, v1, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_11

    nop

    :goto_4
    invoke-direct {p0, v1, v3}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->doUpdateTopOffsetForCoordinateView(Landroid/view/View;I)V

    goto :goto_d

    nop

    :goto_5
    invoke-interface {v0}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_6
    goto :goto_2

    nop

    :goto_7
    invoke-virtual {v0}, Ljava/util/HashMap;->keySet()Ljava/util/Set;

    move-result-object v0

    goto :goto_5

    nop

    :goto_8
    iget v3, v3, Landroid/graphics/Rect;->top:I

    :goto_9
    goto :goto_c

    nop

    :goto_a
    if-nez v1, :cond_1

    goto :goto_e

    :cond_1
    goto :goto_0

    nop

    :goto_b
    return-void

    :goto_c
    invoke-static {p2, v3}, Ljava/lang/Math;->min(II)I

    move-result v3

    goto :goto_15

    nop

    :goto_d
    goto :goto_6

    :goto_e
    goto :goto_b

    nop

    :goto_f
    check-cast v1, Landroid/view/View;

    goto :goto_3

    nop

    :goto_10
    invoke-static {v3}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v4

    goto :goto_17

    nop

    :goto_11
    invoke-direct {p0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->getCoordinateOffsetViewTopOffsetOrDefault(Landroid/view/View;)Ljava/lang/Integer;

    move-result-object v2

    goto :goto_1a

    nop

    :goto_12
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCoordinateOffsetViewSet:Ljava/util/HashMap;

    goto :goto_7

    nop

    :goto_13
    if-eqz v3, :cond_2

    goto :goto_19

    :cond_2
    goto :goto_16

    nop

    :goto_14
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarImpl;->mCoordinateOffsetViewSet:Ljava/util/HashMap;

    goto :goto_10

    nop

    :goto_15
    if-ne v2, v3, :cond_3

    goto :goto_6

    :cond_3
    goto :goto_14

    nop

    :goto_16
    const/4 v3, 0x0

    goto :goto_18

    nop

    :goto_17
    invoke-virtual {v2, v1, v4}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_4

    nop

    :goto_18
    goto :goto_9

    :goto_19
    goto :goto_8

    nop

    :goto_1a
    invoke-virtual {v2}, Ljava/lang/Integer;->intValue()I

    move-result v2

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
