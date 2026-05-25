TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/app/widget/ActionBarView.smali'
CLASS_FALLBACK_NAMES = ['ActionBarView.smali']
CLASS_ANCHORS = ['.super Lmiuix/appcompat/internal/app/widget/AbsActionBarView;', '.implements Lmiuix/view/ActionModeAnimationListener;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarView__createActionMenuPresenter',
        'method': '.method protected createActionMenuPresenter(Lmiuix/appcompat/internal/view/menu/MenuPresenter$Callback;Z)Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;',
        'method_name': 'createActionMenuPresenter',
        'method_anchors': ['invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->findActionBarOverlayLayout()Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;', 'if-eqz p2, :cond_0', 'new-instance p2, Lmiuix/appcompat/internal/view/menu/action/HyperSplitActionMenuPresenter;', 'iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mContext:Landroid/content/Context;', 'sget v1, Lmiuix/appcompat/R$layout;->miuix_appcompat_responsive_action_menu_layout:I', 'sget v2, Lmiuix/appcompat/R$layout;->miuix_appcompat_action_menu_item_layout:I', 'invoke-direct {p2, p0, v0, v1, v2}, Lmiuix/appcompat/internal/view/menu/action/HyperSplitActionMenuPresenter;-><init>(Landroid/content/Context;Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;II)V', 'new-instance p2, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;'],
        'type': 'method_replace',
        'search': """.method protected createActionMenuPresenter(Lmiuix/appcompat/internal/view/menu/MenuPresenter$Callback;Z)Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;
    .registers 6

    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->findActionBarOverlayLayout()Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;

    move-result-object v0

    if-eqz p2, :cond_0

    new-instance p2, Lmiuix/appcompat/internal/view/menu/action/HyperSplitActionMenuPresenter;

    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mContext:Landroid/content/Context;

    sget v1, Lmiuix/appcompat/R$layout;->miuix_appcompat_responsive_action_menu_layout:I

    sget v2, Lmiuix/appcompat/R$layout;->miuix_appcompat_action_menu_item_layout:I

    invoke-direct {p2, p0, v0, v1, v2}, Lmiuix/appcompat/internal/view/menu/action/HyperSplitActionMenuPresenter;-><init>(Landroid/content/Context;Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;II)V

    goto :goto_0

    :cond_0
    new-instance p2, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;

    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mContext:Landroid/content/Context;

    sget v1, Lmiuix/appcompat/R$layout;->miuix_appcompat_responsive_action_menu_layout:I

    sget v2, Lmiuix/appcompat/R$layout;->miuix_appcompat_action_menu_item_layout:I

    invoke-direct {p2, p0, v0, v1, v2}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;-><init>(Landroid/content/Context;Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;II)V

    :goto_0
    invoke-virtual {p2, p1}, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->setCallback(Lmiuix/appcompat/internal/view/menu/MenuPresenter$Callback;)V

    sget p0, Lmiuix/appcompat/R$id;->action_menu_presenter:I

    invoke-virtual {p2, p0}, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->setId(I)V

    return-object p2
.end method""",
        'replacement': """.method protected createActionMenuPresenter(Lmiuix/appcompat/internal/view/menu/MenuPresenter$Callback;Z)Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;
    .registers 6

    goto :goto_a

    nop

    :goto_0
    invoke-virtual {p2, p1}, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->setCallback(Lmiuix/appcompat/internal/view/menu/MenuPresenter$Callback;)V

    goto :goto_5

    nop

    :goto_1
    new-instance p2, Lmiuix/appcompat/internal/view/menu/action/HyperSplitActionMenuPresenter;

    goto :goto_2

    nop

    :goto_2
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mContext:Landroid/content/Context;

    goto :goto_6

    nop

    :goto_3
    invoke-direct {p2, p0, v0, v1, v2}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;-><init>(Landroid/content/Context;Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;II)V

    :goto_4
    goto :goto_0

    nop

    :goto_5
    sget p0, Lmiuix/appcompat/R$id;->action_menu_presenter:I

    goto :goto_f

    nop

    :goto_6
    sget v1, Lmiuix/appcompat/R$layout;->miuix_appcompat_responsive_action_menu_layout:I

    goto :goto_9

    nop

    :goto_7
    if-nez p2, :cond_0

    goto :goto_e

    :cond_0
    goto :goto_1

    nop

    :goto_8
    new-instance p2, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;

    goto :goto_b

    nop

    :goto_9
    sget v2, Lmiuix/appcompat/R$layout;->miuix_appcompat_action_menu_item_layout:I

    goto :goto_c

    nop

    :goto_a
    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->findActionBarOverlayLayout()Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;

    move-result-object v0

    goto :goto_7

    nop

    :goto_b
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mContext:Landroid/content/Context;

    goto :goto_11

    nop

    :goto_c
    invoke-direct {p2, p0, v0, v1, v2}, Lmiuix/appcompat/internal/view/menu/action/HyperSplitActionMenuPresenter;-><init>(Landroid/content/Context;Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;II)V

    goto :goto_d

    nop

    :goto_d
    goto :goto_4

    :goto_e
    goto :goto_8

    nop

    :goto_f
    invoke-virtual {p2, p0}, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->setId(I)V

    goto :goto_12

    nop

    :goto_10
    sget v2, Lmiuix/appcompat/R$layout;->miuix_appcompat_action_menu_item_layout:I

    goto :goto_3

    nop

    :goto_11
    sget v1, Lmiuix/appcompat/R$layout;->miuix_appcompat_responsive_action_menu_layout:I

    goto :goto_10

    nop

    :goto_12
    return-object p2
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarView__createEndActionMenuPresenter',
        'method': '.method protected createEndActionMenuPresenter(Lmiuix/appcompat/internal/view/menu/MenuPresenter$Callback;Z)Lmiuix/appcompat/internal/view/menu/action/EndActionMenuPresenter;',
        'method_name': 'createEndActionMenuPresenter',
        'method_anchors': ['invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->findActionBarOverlayLayout()Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;', 'if-eqz p2, :cond_0', 'new-instance v0, Lmiuix/appcompat/internal/view/menu/action/HyperActionMenuPresenter;', 'iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mContext:Landroid/content/Context;', 'sget v3, Lmiuix/appcompat/R$layout;->miuix_appcompat_action_end_menu_layout:I', 'sget v4, Lmiuix/appcompat/R$layout;->miuix_appcompat_action_end_menu_item_layout:I', 'sget v5, Lmiuix/appcompat/R$layout;->miuix_appcompat_action_bar_expanded_menu_layout:I', 'sget v6, Lmiuix/appcompat/R$layout;->miuix_appcompat_action_bar_list_menu_item_layout:I'],
        'type': 'method_replace',
        'search': """.method protected createEndActionMenuPresenter(Lmiuix/appcompat/internal/view/menu/MenuPresenter$Callback;Z)Lmiuix/appcompat/internal/view/menu/action/EndActionMenuPresenter;
    .registers 10

    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->findActionBarOverlayLayout()Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;

    move-result-object v2

    if-eqz p2, :cond_0

    new-instance v0, Lmiuix/appcompat/internal/view/menu/action/HyperActionMenuPresenter;

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mContext:Landroid/content/Context;

    sget v3, Lmiuix/appcompat/R$layout;->miuix_appcompat_action_end_menu_layout:I

    sget v4, Lmiuix/appcompat/R$layout;->miuix_appcompat_action_end_menu_item_layout:I

    sget v5, Lmiuix/appcompat/R$layout;->miuix_appcompat_action_bar_expanded_menu_layout:I

    sget v6, Lmiuix/appcompat/R$layout;->miuix_appcompat_action_bar_list_menu_item_layout:I

    invoke-direct/range {v0 .. v6}, Lmiuix/appcompat/internal/view/menu/action/HyperActionMenuPresenter;-><init>(Landroid/content/Context;Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;IIII)V

    goto :goto_0

    :cond_0
    new-instance v0, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuPresenter;

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mContext:Landroid/content/Context;

    sget v3, Lmiuix/appcompat/R$layout;->miuix_appcompat_action_end_menu_layout:I

    sget v4, Lmiuix/appcompat/R$layout;->miuix_appcompat_action_end_menu_item_layout:I

    sget v5, Lmiuix/appcompat/R$layout;->miuix_appcompat_action_bar_expanded_menu_layout:I

    sget v6, Lmiuix/appcompat/R$layout;->miuix_appcompat_action_bar_list_menu_item_layout:I

    invoke-direct/range {v0 .. v6}, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuPresenter;-><init>(Landroid/content/Context;Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;IIII)V

    :goto_0
    invoke-virtual {v0, p1}, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->setCallback(Lmiuix/appcompat/internal/view/menu/MenuPresenter$Callback;)V

    sget p0, Lmiuix/appcompat/R$id;->miuix_action_end_menu_presenter:I

    invoke-virtual {v0, p0}, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->setId(I)V

    return-object v0
.end method""",
        'replacement': """.method protected createEndActionMenuPresenter(Lmiuix/appcompat/internal/view/menu/MenuPresenter$Callback;Z)Lmiuix/appcompat/internal/view/menu/action/EndActionMenuPresenter;
    .registers 10

    goto :goto_8

    nop

    :goto_0
    return-object v0

    :goto_1
    invoke-direct/range {v0 .. v6}, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuPresenter;-><init>(Landroid/content/Context;Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;IIII)V

    :goto_2
    goto :goto_13

    nop

    :goto_3
    sget v4, Lmiuix/appcompat/R$layout;->miuix_appcompat_action_end_menu_item_layout:I

    goto :goto_9

    nop

    :goto_4
    invoke-virtual {v0, p0}, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->setId(I)V

    goto :goto_0

    nop

    :goto_5
    sget v5, Lmiuix/appcompat/R$layout;->miuix_appcompat_action_bar_expanded_menu_layout:I

    goto :goto_b

    nop

    :goto_6
    sget v3, Lmiuix/appcompat/R$layout;->miuix_appcompat_action_end_menu_layout:I

    goto :goto_3

    nop

    :goto_7
    invoke-direct/range {v0 .. v6}, Lmiuix/appcompat/internal/view/menu/action/HyperActionMenuPresenter;-><init>(Landroid/content/Context;Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;IIII)V

    goto :goto_d

    nop

    :goto_8
    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->findActionBarOverlayLayout()Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;

    move-result-object v2

    goto :goto_10

    nop

    :goto_9
    sget v5, Lmiuix/appcompat/R$layout;->miuix_appcompat_action_bar_expanded_menu_layout:I

    goto :goto_a

    nop

    :goto_a
    sget v6, Lmiuix/appcompat/R$layout;->miuix_appcompat_action_bar_list_menu_item_layout:I

    goto :goto_7

    nop

    :goto_b
    sget v6, Lmiuix/appcompat/R$layout;->miuix_appcompat_action_bar_list_menu_item_layout:I

    goto :goto_1

    nop

    :goto_c
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mContext:Landroid/content/Context;

    goto :goto_14

    nop

    :goto_d
    goto :goto_2

    :goto_e
    goto :goto_11

    nop

    :goto_f
    new-instance v0, Lmiuix/appcompat/internal/view/menu/action/HyperActionMenuPresenter;

    goto :goto_16

    nop

    :goto_10
    if-nez p2, :cond_0

    goto :goto_e

    :cond_0
    goto :goto_f

    nop

    :goto_11
    new-instance v0, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuPresenter;

    goto :goto_c

    nop

    :goto_12
    sget v4, Lmiuix/appcompat/R$layout;->miuix_appcompat_action_end_menu_item_layout:I

    goto :goto_5

    nop

    :goto_13
    invoke-virtual {v0, p1}, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->setCallback(Lmiuix/appcompat/internal/view/menu/MenuPresenter$Callback;)V

    goto :goto_15

    nop

    :goto_14
    sget v3, Lmiuix/appcompat/R$layout;->miuix_appcompat_action_end_menu_layout:I

    goto :goto_12

    nop

    :goto_15
    sget p0, Lmiuix/appcompat/R$id;->miuix_action_end_menu_presenter:I

    goto :goto_4

    nop

    :goto_16
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mContext:Landroid/content/Context;

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarView__createExpandedActionViewMenuPresenter',
        'method': '.method protected createExpandedActionViewMenuPresenter()Lmiuix/appcompat/internal/app/widget/ActionBarView$ExpandedActionViewMenuPresenter;',
        'method_name': 'createExpandedActionViewMenuPresenter',
        'method_anchors': ['new-instance v0, Lmiuix/appcompat/internal/app/widget/ActionBarView$ExpandedActionViewMenuPresenter;', 'invoke-direct {v0, p0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarView$ExpandedActionViewMenuPresenter;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarView;Lmiuix/appcompat/internal/app/widget/ActionBarView$1;)V', 'return-object v0'],
        'type': 'method_replace',
        'search': """.method protected createExpandedActionViewMenuPresenter()Lmiuix/appcompat/internal/app/widget/ActionBarView$ExpandedActionViewMenuPresenter;
    .registers 3

    new-instance v0, Lmiuix/appcompat/internal/app/widget/ActionBarView$ExpandedActionViewMenuPresenter;

    const/4 v1, 0x0

    invoke-direct {v0, p0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarView$ExpandedActionViewMenuPresenter;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarView;Lmiuix/appcompat/internal/app/widget/ActionBarView$1;)V

    return-object v0
.end method""",
        'replacement': """.method protected createExpandedActionViewMenuPresenter()Lmiuix/appcompat/internal/app/widget/ActionBarView$ExpandedActionViewMenuPresenter;
    .registers 3

    goto :goto_3

    nop

    :goto_0
    return-object v0

    :goto_1
    invoke-direct {v0, p0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarView$ExpandedActionViewMenuPresenter;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarView;Lmiuix/appcompat/internal/app/widget/ActionBarView$1;)V

    goto :goto_0

    nop

    :goto_2
    const/4 v1, 0x0

    goto :goto_1

    nop

    :goto_3
    new-instance v0, Lmiuix/appcompat/internal/app/widget/ActionBarView$ExpandedActionViewMenuPresenter;

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarView__generateDefaultLayoutParams',
        'method': '.method protected generateDefaultLayoutParams()Landroid/view/ViewGroup$LayoutParams;',
        'method_name': 'generateDefaultLayoutParams',
        'method_anchors': ['new-instance p0, Landroidx/appcompat/app/ActionBar$LayoutParams;', 'invoke-direct {p0, v0}, Landroidx/appcompat/app/ActionBar$LayoutParams;-><init>(I)V', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected generateDefaultLayoutParams()Landroid/view/ViewGroup$LayoutParams;
    .registers 2

    new-instance p0, Landroidx/appcompat/app/ActionBar$LayoutParams;

    const v0, 0x800013

    invoke-direct {p0, v0}, Landroidx/appcompat/app/ActionBar$LayoutParams;-><init>(I)V

    return-object p0
.end method""",
        'replacement': """.method protected generateDefaultLayoutParams()Landroid/view/ViewGroup$LayoutParams;
    .registers 2

    goto :goto_2

    nop

    :goto_0
    return-object p0

    :goto_1
    const v0, 0x800013

    goto :goto_3

    nop

    :goto_2
    new-instance p0, Landroidx/appcompat/app/ActionBar$LayoutParams;

    goto :goto_1

    nop

    :goto_3
    invoke-direct {p0, v0}, Landroidx/appcompat/app/ActionBar$LayoutParams;-><init>(I)V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarView__makeMenuViewShowHide',
        'method': '.method protected makeMenuViewShowHide(Z)V',
        'method_name': 'makeMenuViewShowHide',
        'method_anchors': ['iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mSplitActionBarEnable:Z', 'if-nez v0, :cond_0', 'iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mIsBottomMenuVisible:Z', 'if-ne p1, v0, :cond_1', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;', 'if-nez v0, :cond_2', 'new-instance v0, Lmiuix/appcompat/internal/app/widget/ActionBarView$13;', 'invoke-direct {v0, p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarView$13;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarView;Z)V'],
        'type': 'method_replace',
        'search': """.method protected makeMenuViewShowHide(Z)V
    .registers 6

    iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mSplitActionBarEnable:Z

    if-nez v0, :cond_0

    goto :goto_2

    :cond_0
    iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mIsBottomMenuVisible:Z

    if-ne p1, v0, :cond_1

    goto :goto_2

    :cond_1
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    if-nez v0, :cond_2

    new-instance v0, Lmiuix/appcompat/internal/app/widget/ActionBarView$13;

    invoke-direct {v0, p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarView$13;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarView;Z)V

    invoke-direct {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->scheduleBottomMenuAnimation(Ljava/lang/Runnable;)V

    return-void

    :cond_2
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mSplitView:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    invoke-virtual {v0}, Landroid/widget/FrameLayout;->getParent()Landroid/view/ViewParent;

    move-result-object v0

    check-cast v0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    invoke-virtual {v1}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;->getCollapsedHeight()I

    move-result v1

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    if-eqz p1, :cond_3

    const/4 v3, 0x0

    goto :goto_0

    :cond_3
    int-to-float v3, v1

    :goto_0
    invoke-virtual {v2, v3}, Landroid/widget/LinearLayout;->setTranslationY(F)V

    if-eqz p1, :cond_4

    goto :goto_1

    :cond_4
    const/4 v1, 0x0

    :goto_1
    invoke-virtual {v0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->animateContentMarginBottomByBottomMenu(I)V

    iput-boolean p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mIsBottomMenuVisible:Z

    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    instance-of v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;

    if-eqz v0, :cond_5

    check-cast p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;

    xor-int/lit8 p1, p1, 0x1

    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->setHidden(Z)V

    :cond_5
    :goto_2
    return-void
.end method""",
        'replacement': """.method protected makeMenuViewShowHide(Z)V
    .registers 6

    goto :goto_1b

    nop

    :goto_0
    return-void

    :goto_1
    goto :goto_23

    nop

    :goto_2
    check-cast p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;

    goto :goto_20

    nop

    :goto_3
    const/4 v3, 0x0

    goto :goto_14

    nop

    :goto_4
    const/4 v1, 0x0

    :goto_5
    goto :goto_9

    nop

    :goto_6
    if-eqz v0, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_1c

    nop

    :goto_7
    goto :goto_26

    :goto_8
    goto :goto_a

    nop

    :goto_9
    invoke-virtual {v0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->animateContentMarginBottomByBottomMenu(I)V

    goto :goto_e

    nop

    :goto_a
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    goto :goto_6

    nop

    :goto_b
    iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mIsBottomMenuVisible:Z

    goto :goto_21

    nop

    :goto_c
    check-cast v0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;

    goto :goto_12

    nop

    :goto_d
    if-nez v0, :cond_1

    goto :goto_26

    :cond_1
    goto :goto_2

    nop

    :goto_e
    iput-boolean p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mIsBottomMenuVisible:Z

    goto :goto_16

    nop

    :goto_f
    int-to-float v3, v1

    :goto_10
    goto :goto_1e

    nop

    :goto_11
    invoke-direct {v0, p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarView$13;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarView;Z)V

    goto :goto_22

    nop

    :goto_12
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    goto :goto_27

    nop

    :goto_13
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    goto :goto_18

    nop

    :goto_14
    goto :goto_10

    :goto_15
    goto :goto_f

    nop

    :goto_16
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    goto :goto_1f

    nop

    :goto_17
    if-nez p1, :cond_2

    goto :goto_1a

    :cond_2
    goto :goto_19

    nop

    :goto_18
    if-nez p1, :cond_3

    goto :goto_15

    :cond_3
    goto :goto_3

    nop

    :goto_19
    goto :goto_5

    :goto_1a
    goto :goto_4

    nop

    :goto_1b
    iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mSplitActionBarEnable:Z

    goto :goto_1d

    nop

    :goto_1c
    new-instance v0, Lmiuix/appcompat/internal/app/widget/ActionBarView$13;

    goto :goto_11

    nop

    :goto_1d
    if-eqz v0, :cond_4

    goto :goto_29

    :cond_4
    goto :goto_28

    nop

    :goto_1e
    invoke-virtual {v2, v3}, Landroid/widget/LinearLayout;->setTranslationY(F)V

    goto :goto_17

    nop

    :goto_1f
    instance-of v0, p0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;

    goto :goto_d

    nop

    :goto_20
    xor-int/lit8 p1, p1, 0x1

    goto :goto_25

    nop

    :goto_21
    if-eq p1, v0, :cond_5

    goto :goto_8

    :cond_5
    goto :goto_7

    nop

    :goto_22
    invoke-direct {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->scheduleBottomMenuAnimation(Ljava/lang/Runnable;)V

    goto :goto_0

    nop

    :goto_23
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mSplitView:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_24

    nop

    :goto_24
    invoke-virtual {v0}, Landroid/widget/FrameLayout;->getParent()Landroid/view/ViewParent;

    move-result-object v0

    goto :goto_c

    nop

    :goto_25
    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->setHidden(Z)V

    :goto_26
    goto :goto_2a

    nop

    :goto_27
    invoke-virtual {v1}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;->getCollapsedHeight()I

    move-result v1

    goto :goto_13

    nop

    :goto_28
    goto :goto_26

    :goto_29
    goto :goto_b

    nop

    :goto_2a
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarView__makeMenuViewShowHideWithAnimation',
        'method': '.method protected makeMenuViewShowHideWithAnimation(Z)V',
        'method_name': 'makeMenuViewShowHideWithAnimation',
        'method_anchors': ['iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mIsBottomMenuVisible:Z', 'if-ne p1, v0, :cond_0', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;', 'if-nez v0, :cond_1', 'new-instance v0, Lmiuix/appcompat/internal/app/widget/ActionBarView$11;', 'invoke-direct {v0, p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarView$11;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarView;Z)V', 'invoke-direct {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->scheduleBottomMenuAnimation(Ljava/lang/Runnable;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected makeMenuViewShowHideWithAnimation(Z)V
    .registers 10

    iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mIsBottomMenuVisible:Z

    if-ne p1, v0, :cond_0

    goto :goto_2

    :cond_0
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    if-nez v0, :cond_1

    new-instance v0, Lmiuix/appcompat/internal/app/widget/ActionBarView$11;

    invoke-direct {v0, p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarView$11;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarView;Z)V

    invoke-direct {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->scheduleBottomMenuAnimation(Ljava/lang/Runnable;)V

    return-void

    :cond_1
    iput-boolean p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mIsBottomMenuVisible:Z

    const/4 v1, 0x0

    iput-boolean v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mAnimateStart:Z

    iget-boolean v2, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mSplitActionBarEnable:Z

    if-nez v2, :cond_2

    goto :goto_2

    :cond_2
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getParent()Landroid/view/ViewParent;

    move-result-object v2

    invoke-interface {v2}, Landroid/view/ViewParent;->getParent()Landroid/view/ViewParent;

    move-result-object v2

    check-cast v2, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;

    if-nez v0, :cond_3

    move v3, v1

    goto :goto_0

    :cond_3
    invoke-virtual {v0}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;->getCollapsedHeight()I

    move-result v3

    :goto_0
    if-eqz p1, :cond_4

    move v4, v1

    move p1, v3

    goto :goto_1

    :cond_4
    move p1, v1

    move v4, v3

    :goto_1
    if-eqz v0, :cond_7

    iget-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMenuAnimConfig:Lmiuix/animation/base/AnimConfig;

    if-nez v5, :cond_5

    new-instance v5, Lmiuix/animation/base/AnimConfig;

    invoke-direct {v5}, Lmiuix/animation/base/AnimConfig;-><init>()V

    const/4 v6, 0x2

    new-array v6, v6, [F

    fill-array-data v6, :array_0

    const/4 v7, -0x2

    invoke-virtual {v5, v7, v6}, Lmiuix/animation/base/AnimConfig;->setEase(I[F)Lmiuix/animation/base/AnimConfig;

    move-result-object v5

    iput-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMenuAnimConfig:Lmiuix/animation/base/AnimConfig;

    :cond_5
    iget-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mBottomMenuTransitionListener:Lmiuix/animation/listener/TransitionListener;

    if-eqz v5, :cond_6

    iget-object v6, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMenuAnimConfig:Lmiuix/animation/base/AnimConfig;

    filled-new-array {v5}, [Lmiuix/animation/listener/TransitionListener;

    move-result-object v5

    invoke-virtual {v6, v5}, Lmiuix/animation/base/AnimConfig;->removeListeners([Lmiuix/animation/listener/TransitionListener;)Lmiuix/animation/base/AnimConfig;

    :cond_6
    iget-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMenuAnimConfig:Lmiuix/animation/base/AnimConfig;

    new-instance v6, Lmiuix/appcompat/internal/app/widget/ActionBarView$12;

    invoke-direct {v6, p0, v2, v3}, Lmiuix/appcompat/internal/app/widget/ActionBarView$12;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarView;Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;I)V

    iput-object v6, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mBottomMenuTransitionListener:Lmiuix/animation/listener/TransitionListener;

    filled-new-array {v6}, [Lmiuix/animation/listener/TransitionListener;

    move-result-object v2

    invoke-virtual {v5, v2}, Lmiuix/animation/base/AnimConfig;->addListeners([Lmiuix/animation/listener/TransitionListener;)Lmiuix/animation/base/AnimConfig;

    int-to-float p1, p1

    invoke-virtual {v0, p1}, Landroid/widget/LinearLayout;->setTranslationY(F)V

    new-instance p1, Lmiuix/animation/controller/AnimState;

    const-string v2, "menu_end_state"

    invoke-direct {p1, v2}, Lmiuix/animation/controller/AnimState;-><init>(Ljava/lang/Object;)V

    sget-object v2, Lmiuix/animation/property/ViewProperty;->TRANSLATION_Y:Lmiuix/animation/property/ViewProperty;

    int-to-double v3, v4

    invoke-virtual {p1, v2, v3, v4}, Lmiuix/animation/controller/AnimState;->add(Ljava/lang/Object;D)Lmiuix/animation/controller/AnimState;

    move-result-object p1

    const/4 v2, 0x1

    new-array v3, v2, [Landroid/view/View;

    aput-object v0, v3, v1

    invoke-static {v3}, Lmiuix/animation/Folme;->useAt([Landroid/view/View;)Lmiuix/animation/IFolme;

    move-result-object v1

    invoke-interface {v1}, Lmiuix/animation/IFolme;->state()Lmiuix/animation/IStateStyle;

    move-result-object v1

    iget-object v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMenuAnimConfig:Lmiuix/animation/base/AnimConfig;

    filled-new-array {v3}, [Lmiuix/animation/base/AnimConfig;

    move-result-object v3

    invoke-interface {v1, p1, v3}, Lmiuix/animation/FolmeStyle;->to(Ljava/lang/Object;[Lmiuix/animation/base/AnimConfig;)Lmiuix/animation/IStateStyle;

    instance-of p1, v0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;

    if-eqz p1, :cond_7

    check-cast v0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;

    iget-boolean p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mIsBottomMenuVisible:Z

    xor-int/2addr p0, v2

    invoke-virtual {v0, p0}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->setHidden(Z)V

    :cond_7
    :goto_2
    return-void

    nop

    :array_0
    .array-data 4
        0x3f733333
        0x3e800000
    .end array-data
.end method""",
        'replacement': """.method protected makeMenuViewShowHideWithAnimation(Z)V
    .registers 10

    goto :goto_5

    nop

    :goto_0
    new-array v6, v6, [F

    fill-array-data v6, :array_0

    goto :goto_40

    nop

    :goto_1
    if-nez p1, :cond_0

    goto :goto_1a

    :cond_0
    goto :goto_d

    nop

    :goto_2
    invoke-interface {v1}, Lmiuix/animation/IFolme;->state()Lmiuix/animation/IStateStyle;

    move-result-object v1

    goto :goto_1d

    nop

    :goto_3
    aput-object v0, v3, v1

    goto :goto_34

    nop

    :goto_4
    invoke-direct {v0, p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarView$11;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarView;Z)V

    goto :goto_a

    nop

    :goto_5
    iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mIsBottomMenuVisible:Z

    goto :goto_42

    nop

    :goto_6
    invoke-direct {p1, v2}, Lmiuix/animation/controller/AnimState;-><init>(Ljava/lang/Object;)V

    goto :goto_22

    nop

    :goto_7
    const-string v2, "menu_end_state"

    goto :goto_6

    nop

    :goto_8
    iget-boolean v2, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mSplitActionBarEnable:Z

    goto :goto_41

    nop

    :goto_9
    int-to-double v3, v4

    goto :goto_27

    nop

    :goto_a
    invoke-direct {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->scheduleBottomMenuAnimation(Ljava/lang/Runnable;)V

    goto :goto_f

    nop

    :goto_b
    if-eqz v0, :cond_1

    goto :goto_36

    :cond_1
    goto :goto_4a

    nop

    :goto_c
    iput-boolean p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mIsBottomMenuVisible:Z

    goto :goto_38

    nop

    :goto_d
    check-cast v0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;

    goto :goto_31

    nop

    :goto_e
    new-instance v6, Lmiuix/appcompat/internal/app/widget/ActionBarView$12;

    goto :goto_2d

    nop

    :goto_f
    return-void

    :goto_10
    goto :goto_c

    nop

    :goto_11
    goto :goto_20

    :goto_12
    goto :goto_23

    nop

    :goto_13
    invoke-virtual {v0, p1}, Landroid/widget/LinearLayout;->setTranslationY(F)V

    goto :goto_48

    nop

    :goto_14
    invoke-direct {v5}, Lmiuix/animation/base/AnimConfig;-><init>()V

    goto :goto_3b

    nop

    :goto_15
    iput-object v6, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mBottomMenuTransitionListener:Lmiuix/animation/listener/TransitionListener;

    goto :goto_4d

    nop

    :goto_16
    invoke-virtual {v0}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;->getCollapsedHeight()I

    move-result v3

    :goto_17
    goto :goto_46

    nop

    :goto_18
    if-eqz v5, :cond_2

    goto :goto_4c

    :cond_2
    goto :goto_2c

    nop

    :goto_19
    invoke-virtual {v0, p0}, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;->setHidden(Z)V

    :goto_1a
    goto :goto_2f

    nop

    :goto_1b
    goto :goto_1a

    :goto_1c
    goto :goto_44

    nop

    :goto_1d
    iget-object v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMenuAnimConfig:Lmiuix/animation/base/AnimConfig;

    goto :goto_51

    nop

    :goto_1e
    iget-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMenuAnimConfig:Lmiuix/animation/base/AnimConfig;

    goto :goto_e

    nop

    :goto_1f
    move v4, v3

    :goto_20
    goto :goto_47

    nop

    :goto_21
    instance-of p1, v0, Lmiuix/appcompat/internal/view/menu/action/ResponsiveActionMenuView;

    goto :goto_1

    nop

    :goto_22
    sget-object v2, Lmiuix/animation/property/ViewProperty;->TRANSLATION_Y:Lmiuix/animation/property/ViewProperty;

    goto :goto_9

    nop

    :goto_23
    move p1, v1

    goto :goto_1f

    nop

    :goto_24
    iget-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMenuAnimConfig:Lmiuix/animation/base/AnimConfig;

    goto :goto_18

    nop

    :goto_25
    check-cast v2, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;

    goto :goto_b

    nop

    :goto_26
    const/4 v2, 0x1

    goto :goto_3a

    nop

    :goto_27
    invoke-virtual {p1, v2, v3, v4}, Lmiuix/animation/controller/AnimState;->add(Ljava/lang/Object;D)Lmiuix/animation/controller/AnimState;

    move-result-object p1

    goto :goto_26

    nop

    :goto_28
    move v4, v1

    goto :goto_30

    nop

    :goto_29
    invoke-virtual {v5, v2}, Lmiuix/animation/base/AnimConfig;->addListeners([Lmiuix/animation/listener/TransitionListener;)Lmiuix/animation/base/AnimConfig;

    goto :goto_4e

    nop

    :goto_2a
    filled-new-array {v5}, [Lmiuix/animation/listener/TransitionListener;

    move-result-object v5

    goto :goto_4f

    nop

    :goto_2b
    invoke-interface {v1, p1, v3}, Lmiuix/animation/FolmeStyle;->to(Ljava/lang/Object;[Lmiuix/animation/base/AnimConfig;)Lmiuix/animation/IStateStyle;

    goto :goto_21

    nop

    :goto_2c
    new-instance v5, Lmiuix/animation/base/AnimConfig;

    goto :goto_14

    nop

    :goto_2d
    invoke-direct {v6, p0, v2, v3}, Lmiuix/appcompat/internal/app/widget/ActionBarView$12;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarView;Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;I)V

    goto :goto_15

    nop

    :goto_2e
    invoke-interface {v2}, Landroid/view/ViewParent;->getParent()Landroid/view/ViewParent;

    move-result-object v2

    goto :goto_25

    nop

    :goto_2f
    return-void

    nop

    :array_0
    .array-data 4
        0x3f733333
        0x3e800000
    .end array-data

    :goto_30
    move p1, v3

    goto :goto_11

    nop

    :goto_31
    iget-boolean p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mIsBottomMenuVisible:Z

    goto :goto_43

    nop

    :goto_32
    goto :goto_1a

    :goto_33
    goto :goto_3c

    nop

    :goto_34
    invoke-static {v3}, Lmiuix/animation/Folme;->useAt([Landroid/view/View;)Lmiuix/animation/IFolme;

    move-result-object v1

    goto :goto_2

    nop

    :goto_35
    goto :goto_17

    :goto_36
    goto :goto_16

    nop

    :goto_37
    if-eqz v0, :cond_3

    goto :goto_10

    :cond_3
    goto :goto_49

    nop

    :goto_38
    const/4 v1, 0x0

    goto :goto_3e

    nop

    :goto_39
    iget-object v6, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMenuAnimConfig:Lmiuix/animation/base/AnimConfig;

    goto :goto_2a

    nop

    :goto_3a
    new-array v3, v2, [Landroid/view/View;

    goto :goto_3

    nop

    :goto_3b
    const/4 v6, 0x2

    goto :goto_0

    nop

    :goto_3c
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getParent()Landroid/view/ViewParent;

    move-result-object v2

    goto :goto_2e

    nop

    :goto_3d
    iget-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mBottomMenuTransitionListener:Lmiuix/animation/listener/TransitionListener;

    goto :goto_45

    nop

    :goto_3e
    iput-boolean v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mAnimateStart:Z

    goto :goto_8

    nop

    :goto_3f
    invoke-virtual {v5, v7, v6}, Lmiuix/animation/base/AnimConfig;->setEase(I[F)Lmiuix/animation/base/AnimConfig;

    move-result-object v5

    goto :goto_4b

    nop

    :goto_40
    const/4 v7, -0x2

    goto :goto_3f

    nop

    :goto_41
    if-eqz v2, :cond_4

    goto :goto_33

    :cond_4
    goto :goto_32

    nop

    :goto_42
    if-eq p1, v0, :cond_5

    goto :goto_1c

    :cond_5
    goto :goto_1b

    nop

    :goto_43
    xor-int/2addr p0, v2

    goto :goto_19

    nop

    :goto_44
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    goto :goto_37

    nop

    :goto_45
    if-nez v5, :cond_6

    goto :goto_50

    :cond_6
    goto :goto_39

    nop

    :goto_46
    if-nez p1, :cond_7

    goto :goto_12

    :cond_7
    goto :goto_28

    nop

    :goto_47
    if-nez v0, :cond_8

    goto :goto_1a

    :cond_8
    goto :goto_24

    nop

    :goto_48
    new-instance p1, Lmiuix/animation/controller/AnimState;

    goto :goto_7

    nop

    :goto_49
    new-instance v0, Lmiuix/appcompat/internal/app/widget/ActionBarView$11;

    goto :goto_4

    nop

    :goto_4a
    move v3, v1

    goto :goto_35

    nop

    :goto_4b
    iput-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMenuAnimConfig:Lmiuix/animation/base/AnimConfig;

    :goto_4c
    goto :goto_3d

    nop

    :goto_4d
    filled-new-array {v6}, [Lmiuix/animation/listener/TransitionListener;

    move-result-object v2

    goto :goto_29

    nop

    :goto_4e
    int-to-float p1, p1

    goto :goto_13

    nop

    :goto_4f
    invoke-virtual {v6, v5}, Lmiuix/animation/base/AnimConfig;->removeListeners([Lmiuix/animation/listener/TransitionListener;)Lmiuix/animation/base/AnimConfig;

    :goto_50
    goto :goto_1e

    nop

    :goto_51
    filled-new-array {v3}, [Lmiuix/animation/base/AnimConfig;

    move-result-object v3

    goto :goto_2b

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarView__onAnimatedExpandStateChanged',
        'method': '.method protected onAnimatedExpandStateChanged(II)V',
        'method_name': 'onAnimatedExpandStateChanged',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mStateChangeAnimStateStyle:Lmiuix/animation/IStateStyle;', 'if-eqz v0, :cond_0', 'invoke-interface {v0}, Lmiuix/animation/ICancelableStyle;->cancel()V', 'if-ne p1, v0, :cond_1', 'iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableMainContainer:Landroid/widget/FrameLayout;', 'invoke-virtual {p1}, Landroid/widget/FrameLayout;->getMeasuredHeight()I', 'iget v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableSecondaryTabHeight:I', 'iput p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mPendingHeight:I'],
        'type': 'method_replace',
        'search': """.method protected onAnimatedExpandStateChanged(II)V
    .registers 7

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mStateChangeAnimStateStyle:Lmiuix/animation/IStateStyle;

    if-eqz v0, :cond_0

    invoke-interface {v0}, Lmiuix/animation/ICancelableStyle;->cancel()V

    :cond_0
    const/4 v0, 0x1

    const/4 v1, 0x0

    if-ne p1, v0, :cond_1

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    invoke-virtual {p1}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result p1

    iget v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableSecondaryTabHeight:I

    add-int/2addr p1, v2

    iput p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mPendingHeight:I

    goto :goto_0

    :cond_1
    if-nez p1, :cond_2

    iput v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mPendingHeight:I

    :cond_2
    :goto_0
    new-instance p1, Lmiuix/animation/base/AnimConfig;

    invoke-direct {p1}, Lmiuix/animation/base/AnimConfig;-><init>()V

    new-instance v2, Lmiuix/appcompat/internal/app/widget/ActionBarView$InnerTransitionListener;

    invoke-direct {v2, p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView$InnerTransitionListener;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarView;)V

    filled-new-array {v2}, [Lmiuix/animation/listener/TransitionListener;

    move-result-object v2

    invoke-virtual {p1, v2}, Lmiuix/animation/base/AnimConfig;->addListeners([Lmiuix/animation/listener/TransitionListener;)Lmiuix/animation/base/AnimConfig;

    move-result-object p1

    if-ne p2, v0, :cond_3

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    invoke-virtual {v2}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result v2

    iget v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableSecondaryTabHeight:I

    add-int/2addr v2, v3

    goto :goto_1

    :cond_3
    move v2, v1

    :goto_1
    if-ne p2, v0, :cond_4

    iget-object p2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    const/4 v0, 0x4

    invoke-virtual {p2, v0}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setVisibility(I)V

    goto :goto_2

    :cond_4
    if-nez p2, :cond_5

    iget-object p2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    invoke-virtual {p2, v1}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setVisibility(I)V

    :cond_5
    :goto_2
    new-array p2, v1, [Ljava/lang/Object;

    invoke-static {p2}, Lmiuix/animation/Folme;->useValue([Ljava/lang/Object;)Lmiuix/animation/IStateStyle;

    move-result-object p2

    const-wide/16 v0, 0x1

    invoke-interface {p2, v0, v1}, Lmiuix/animation/FolmeStyle;->setFlags(J)Lmiuix/animation/IStateStyle;

    move-result-object p2

    iget v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mPendingHeight:I

    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    const-string v1, "actionbar_state_change"

    filled-new-array {v1, v0}, [Ljava/lang/Object;

    move-result-object v0

    invoke-interface {p2, v0}, Lmiuix/animation/FolmeStyle;->setTo([Ljava/lang/Object;)Lmiuix/animation/IStateStyle;

    move-result-object p2

    invoke-static {v2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    filled-new-array {v1, v0, p1}, [Ljava/lang/Object;

    move-result-object p1

    invoke-interface {p2, p1}, Lmiuix/animation/FolmeStyle;->to([Ljava/lang/Object;)Lmiuix/animation/IStateStyle;

    move-result-object p1

    iput-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mStateChangeAnimStateStyle:Lmiuix/animation/IStateStyle;

    return-void
.end method""",
        'replacement': """.method protected onAnimatedExpandStateChanged(II)V
    .registers 7

    goto :goto_1b

    nop

    :goto_0
    const-string v1, "actionbar_state_change"

    goto :goto_17

    nop

    :goto_1
    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    goto :goto_0

    nop

    :goto_2
    if-eq p1, v0, :cond_0

    goto :goto_2b

    :cond_0
    goto :goto_16

    nop

    :goto_3
    new-instance v2, Lmiuix/appcompat/internal/app/widget/ActionBarView$InnerTransitionListener;

    goto :goto_1f

    nop

    :goto_4
    invoke-interface {p2, v0, v1}, Lmiuix/animation/FolmeStyle;->setFlags(J)Lmiuix/animation/IStateStyle;

    move-result-object p2

    goto :goto_d

    nop

    :goto_5
    invoke-interface {p2, p1}, Lmiuix/animation/FolmeStyle;->to([Ljava/lang/Object;)Lmiuix/animation/IStateStyle;

    move-result-object p1

    goto :goto_30

    nop

    :goto_6
    goto :goto_23

    :goto_7
    goto :goto_27

    nop

    :goto_8
    invoke-static {v2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    goto :goto_21

    nop

    :goto_9
    invoke-interface {p2, v0}, Lmiuix/animation/FolmeStyle;->setTo([Ljava/lang/Object;)Lmiuix/animation/IStateStyle;

    move-result-object p2

    goto :goto_8

    nop

    :goto_a
    const-wide/16 v0, 0x1

    goto :goto_4

    nop

    :goto_b
    if-eqz p1, :cond_1

    goto :goto_2f

    :cond_1
    goto :goto_2e

    nop

    :goto_c
    invoke-virtual {v2}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result v2

    goto :goto_10

    nop

    :goto_d
    iget v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mPendingHeight:I

    goto :goto_1

    nop

    :goto_e
    const/4 v0, 0x4

    goto :goto_31

    nop

    :goto_f
    iget v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableSecondaryTabHeight:I

    goto :goto_12

    nop

    :goto_10
    iget v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableSecondaryTabHeight:I

    goto :goto_37

    nop

    :goto_11
    invoke-virtual {p1, v2}, Lmiuix/animation/base/AnimConfig;->addListeners([Lmiuix/animation/listener/TransitionListener;)Lmiuix/animation/base/AnimConfig;

    move-result-object p1

    goto :goto_2c

    nop

    :goto_12
    add-int/2addr p1, v2

    goto :goto_18

    nop

    :goto_13
    const/4 v1, 0x0

    goto :goto_2

    nop

    :goto_14
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    goto :goto_c

    nop

    :goto_15
    new-array p2, v1, [Ljava/lang/Object;

    goto :goto_24

    nop

    :goto_16
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    goto :goto_34

    nop

    :goto_17
    filled-new-array {v1, v0}, [Ljava/lang/Object;

    move-result-object v0

    goto :goto_9

    nop

    :goto_18
    iput p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mPendingHeight:I

    goto :goto_2a

    nop

    :goto_19
    invoke-interface {v0}, Lmiuix/animation/ICancelableStyle;->cancel()V

    :goto_1a
    goto :goto_20

    nop

    :goto_1b
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mStateChangeAnimStateStyle:Lmiuix/animation/IStateStyle;

    goto :goto_1c

    nop

    :goto_1c
    if-nez v0, :cond_2

    goto :goto_1a

    :cond_2
    goto :goto_19

    nop

    :goto_1d
    goto :goto_26

    :goto_1e
    goto :goto_25

    nop

    :goto_1f
    invoke-direct {v2, p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView$InnerTransitionListener;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarView;)V

    goto :goto_33

    nop

    :goto_20
    const/4 v0, 0x1

    goto :goto_13

    nop

    :goto_21
    filled-new-array {v1, v0, p1}, [Ljava/lang/Object;

    move-result-object p1

    goto :goto_5

    nop

    :goto_22
    invoke-virtual {p2, v1}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setVisibility(I)V

    :goto_23
    goto :goto_15

    nop

    :goto_24
    invoke-static {p2}, Lmiuix/animation/Folme;->useValue([Ljava/lang/Object;)Lmiuix/animation/IStateStyle;

    move-result-object p2

    goto :goto_a

    nop

    :goto_25
    move v2, v1

    :goto_26
    goto :goto_35

    nop

    :goto_27
    if-eqz p2, :cond_3

    goto :goto_23

    :cond_3
    goto :goto_2d

    nop

    :goto_28
    invoke-direct {p1}, Lmiuix/animation/base/AnimConfig;-><init>()V

    goto :goto_3

    nop

    :goto_29
    new-instance p1, Lmiuix/animation/base/AnimConfig;

    goto :goto_28

    nop

    :goto_2a
    goto :goto_2f

    :goto_2b
    goto :goto_b

    nop

    :goto_2c
    if-eq p2, v0, :cond_4

    goto :goto_1e

    :cond_4
    goto :goto_14

    nop

    :goto_2d
    iget-object p2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    goto :goto_22

    nop

    :goto_2e
    iput v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mPendingHeight:I

    :goto_2f
    goto :goto_29

    nop

    :goto_30
    iput-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mStateChangeAnimStateStyle:Lmiuix/animation/IStateStyle;

    goto :goto_36

    nop

    :goto_31
    invoke-virtual {p2, v0}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setVisibility(I)V

    goto :goto_6

    nop

    :goto_32
    iget-object p2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    goto :goto_e

    nop

    :goto_33
    filled-new-array {v2}, [Lmiuix/animation/listener/TransitionListener;

    move-result-object v2

    goto :goto_11

    nop

    :goto_34
    invoke-virtual {p1}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result p1

    goto :goto_f

    nop

    :goto_35
    if-eq p2, v0, :cond_5

    goto :goto_7

    :cond_5
    goto :goto_32

    nop

    :goto_36
    return-void

    :goto_37
    add-int/2addr v2, v3

    goto :goto_1d

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarView__onAttachedToWindow',
        'method': '.method protected onAttachedToWindow()V',
        'method_name': 'onAttachedToWindow',
        'method_anchors': ['invoke-super {p0}, Landroid/view/ViewGroup;->onAttachedToWindow()V', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;', 'invoke-virtual {v0}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->onAttachedToWindow()V', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;', 'invoke-virtual {v0}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->onAttachedToWindow()V', 'invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->updateBackInvokedCallbackState()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onAttachedToWindow()V
    .registers 2

    invoke-super {p0}, Landroid/view/ViewGroup;->onAttachedToWindow()V

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    invoke-virtual {v0}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->onAttachedToWindow()V

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    invoke-virtual {v0}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->onAttachedToWindow()V

    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->updateBackInvokedCallbackState()V

    return-void
.end method""",
        'replacement': """.method protected onAttachedToWindow()V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0}, Landroid/view/ViewGroup;->onAttachedToWindow()V

    goto :goto_5

    nop

    :goto_1
    invoke-virtual {v0}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->onAttachedToWindow()V

    goto :goto_2

    nop

    :goto_2
    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->updateBackInvokedCallbackState()V

    goto :goto_3

    nop

    :goto_3
    return-void

    :goto_4
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    goto :goto_1

    nop

    :goto_5
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    goto :goto_6

    nop

    :goto_6
    invoke-virtual {v0}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->onAttachedToWindow()V

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarView__onConfigurationChanged',
        'method': '.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V',
        'method_name': 'onConfigurationChanged',
        'method_anchors': ['invoke-super {p0, p1}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->onConfigurationChanged(Landroid/content/res/Configuration;)V', 'invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;', 'sget-object v0, Lmiuix/appcompat/R$styleable;->ActionBar:[I', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->getActionBarStyle()I', 'invoke-virtual {p1, v2, v0, v1, v3}, Landroid/content/Context;->obtainStyledAttributes(Landroid/util/AttributeSet;[III)Landroid/content/res/TypedArray;', 'sget v0, Lmiuix/appcompat/R$styleable;->ActionBar_android_minHeight:I', 'invoke-virtual {p1, v0, v3}, Landroid/content/res/TypedArray;->getLayoutDimension(II)I', 'iput v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mTitleMinHeight:I'],
        'type': 'method_replace',
        'search': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 8

    invoke-super {p0, p1}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;

    move-result-object p1

    sget-object v0, Lmiuix/appcompat/R$styleable;->ActionBar:[I

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->getActionBarStyle()I

    move-result v1

    const/4 v2, 0x0

    const/4 v3, 0x0

    invoke-virtual {p1, v2, v0, v1, v3}, Landroid/content/Context;->obtainStyledAttributes(Landroid/util/AttributeSet;[III)Landroid/content/res/TypedArray;

    move-result-object p1

    sget v0, Lmiuix/appcompat/R$styleable;->ActionBar_android_minHeight:I

    invoke-virtual {p1, v0, v3}, Landroid/content/res/TypedArray;->getLayoutDimension(II)I

    move-result v0

    iput v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mTitleMinHeight:I

    sget v0, Lmiuix/appcompat/R$styleable;->ActionBar_android_maxHeight:I

    invoke-virtual {p1, v0, v3}, Landroid/content/res/TypedArray;->getLayoutDimension(II)I

    move-result v0

    iput v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mTitleMaxHeight:I

    sget v0, Lmiuix/appcompat/R$styleable;->ActionBar_actionBarMaxSizeInLargeFont:I

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mContext:Landroid/content/Context;

    invoke-virtual {v1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v1

    sget v2, Lmiuix/appcompat/R$dimen;->miuix_appcompat_action_bar_large_font_max_height:I

    invoke-virtual {v1, v2}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I

    move-result v1

    invoke-virtual {p1, v0, v1}, Landroid/content/res/TypedArray;->getDimensionPixelSize(II)I

    move-result v0

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mContext:Landroid/content/Context;

    sget v2, Lmiuix/appcompat/R$attr;->actionBarTitleAdaptLargeFont:I

    const/4 v4, 0x1

    invoke-static {v1, v2, v4}, Lmiuix/internal/util/AttributeResolver;->resolveBoolean(Landroid/content/Context;IZ)Z

    move-result v1

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mContext:Landroid/content/Context;

    invoke-static {v2}, Lmiuix/core/util/MiuixUIUtils;->getFontLevel(Landroid/content/Context;)I

    move-result v2

    const/4 v5, 0x2

    if-ne v2, v5, :cond_0

    move v2, v4

    goto :goto_0

    :cond_0
    move v2, v3

    :goto_0
    if-eqz v1, :cond_1

    if-eqz v2, :cond_1

    goto :goto_1

    :cond_1
    iget v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mTitleMaxHeight:I

    :goto_1
    iput v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mTitleMaxHeight:I

    invoke-virtual {p1}, Landroid/content/res/TypedArray;->recycle()V

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getResources()Landroid/content/res/Resources;

    move-result-object p1

    invoke-virtual {p1}, Landroid/content/res/Resources;->getConfiguration()Landroid/content/res/Configuration;

    move-result-object p1

    iput-boolean v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseTitleShowable:Z

    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->updateTightTitle()V

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->getDisplayOptions()I

    move-result v0

    and-int/lit8 v0, v0, 0x8

    if-eqz v0, :cond_3

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseTitle:Lmiuix/appcompat/internal/app/widget/actionbar/CollapseTitle;

    if-eqz v0, :cond_2

    invoke-virtual {v0, p1}, Lmiuix/appcompat/internal/app/widget/actionbar/CollapseTitle;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    :cond_2
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExpandTitle:Lmiuix/appcompat/internal/app/widget/actionbar/ExpandTitle;

    if-eqz v0, :cond_3

    invoke-virtual {v0, p1}, Lmiuix/appcompat/internal/app/widget/actionbar/ExpandTitle;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    :cond_3
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mContext:Landroid/content/Context;

    invoke-virtual {p1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object p1

    invoke-virtual {p1}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;

    move-result-object v0

    iget v0, v0, Landroid/util/DisplayMetrics;->density:F

    iget v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mDensity:F

    cmpl-float v1, v0, v1

    if-eqz v1, :cond_4

    iput v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mDensity:F

    sget v0, Lmiuix/appcompat/R$dimen;->miuix_appcompat_action_bar_title_tab_horizontal_padding:I

    invoke-virtual {p1, v0}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result v0

    iput v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mUncollapseTabPaddingH:I

    sget v0, Lmiuix/appcompat/R$dimen;->miuix_appcompat_action_bar_title_top_padding:I

    invoke-virtual {p1, v0}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result v0

    iput v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExpandTabTopPadding:I

    sget v0, Lmiuix/appcompat/R$dimen;->miuix_appcompat_action_bar_title_bottom_padding:I

    invoke-virtual {p1, v0}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result v0

    iput v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExpandTitlePaddingBottom:I

    sget v0, Lmiuix/appcompat/R$dimen;->miuix_appcompat_action_bar_subtitle_bottom_padding:I

    invoke-virtual {p1, v0}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result v0

    iput v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExpandSubtitlePaddingBottom:I

    sget v0, Lmiuix/appcompat/R$dimen;->miuix_appcompat_action_bar_up_view_margin_start:I

    invoke-virtual {p1, v0}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result v0

    iput v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mTitleUpViewMarginStart:I

    iput v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mTitleUpViewMarginEnd:I

    sget v0, Lmiuix/appcompat/R$dimen;->miuix_appcompat_action_bar_title_padding_gap:I

    invoke-virtual {p1, v0}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result v0

    iput v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mTitleGapPaddingStart:I

    :cond_4
    sget v0, Lmiuix/appcompat/R$dimen;->miuix_appcompat_action_bar_title_horizontal_padding:I

    invoke-virtual {p1, v0}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result v0

    iput v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mUncollapsePaddingH:I

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mSubtitle:Ljava/lang/CharSequence;

    invoke-static {v0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v0

    if-eqz v0, :cond_5

    iget v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExpandTitlePaddingBottom:I

    goto :goto_2

    :cond_5
    iget v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExpandSubtitlePaddingBottom:I

    :goto_2
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    iget v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mUncollapsePaddingH:I

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getResources()Landroid/content/res/Resources;

    move-result-object v3

    sget v4, Lmiuix/appcompat/R$dimen;->miuix_appcompat_action_bar_title_top_padding:I

    invoke-virtual {v3, v4}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result v3

    iget v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mUncollapsePaddingH:I

    invoke-virtual {v1, v2, v3, v4, v0}, Landroid/widget/FrameLayout;->setPaddingRelative(IIII)V

    sget v0, Lmiuix/appcompat/R$dimen;->miuix_appcompat_action_bar_secondary_tab_vertical_padding:I

    invoke-virtual {p1, v0}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result p1

    iput p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mSecondaryTabVerticalPadding:I

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseTabContainer:Landroid/widget/FrameLayout;

    if-eqz p1, :cond_6

    invoke-virtual {p1}, Landroid/widget/FrameLayout;->getPaddingStart()I

    move-result v0

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseTabContainer:Landroid/widget/FrameLayout;

    invoke-virtual {v1}, Landroid/widget/FrameLayout;->getPaddingTop()I

    move-result v1

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseTabContainer:Landroid/widget/FrameLayout;

    invoke-virtual {v2}, Landroid/widget/FrameLayout;->getPaddingEnd()I

    move-result v2

    iget v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mSecondaryTabVerticalPadding:I

    invoke-virtual {p1, v0, v1, v2, v3}, Landroid/widget/FrameLayout;->setPaddingRelative(IIII)V

    :cond_6
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableTabContainer:Landroid/widget/FrameLayout;

    if-eqz p1, :cond_7

    invoke-virtual {p1}, Landroid/widget/FrameLayout;->getPaddingStart()I

    move-result v0

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableTabContainer:Landroid/widget/FrameLayout;

    invoke-virtual {v1}, Landroid/widget/FrameLayout;->getPaddingTop()I

    move-result v1

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableTabContainer:Landroid/widget/FrameLayout;

    invoke-virtual {v2}, Landroid/widget/FrameLayout;->getPaddingEnd()I

    move-result v2

    iget v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mSecondaryTabVerticalPadding:I

    invoke-virtual {p1, v0, v1, v2, v3}, Landroid/widget/FrameLayout;->setPaddingRelative(IIII)V

    :cond_7
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;

    move-result-object p1

    sget v0, Lmiuix/appcompat/R$attr;->actionBarPaddingStart:I

    invoke-static {p1, v0}, Lmiuix/internal/util/AttributeResolver;->resolveDimensionPixelSize(Landroid/content/Context;I)I

    move-result p1

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;

    move-result-object v0

    sget v1, Lmiuix/appcompat/R$attr;->actionBarPaddingEnd:I

    invoke-static {v0, v1}, Lmiuix/internal/util/AttributeResolver;->resolveDimensionPixelSize(Landroid/content/Context;I)I

    move-result v0

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getPaddingTop()I

    move-result v1

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getPaddingBottom()I

    move-result v2

    invoke-virtual {p0, p1, v1, v0, v2}, Landroid/view/ViewGroup;->setPaddingRelative(IIII)V

    iget-boolean p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mTabsExit:Z

    if-eqz p1, :cond_8

    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->updateTabsLayoutParams()V

    :cond_8
    new-instance p1, Lmiuix/appcompat/internal/app/widget/ActionBarView$$ExternalSyntheticLambda0;

    invoke-direct {p1, p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView$$ExternalSyntheticLambda0;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarView;)V

    invoke-virtual {p0, p1}, Landroid/view/ViewGroup;->post(Ljava/lang/Runnable;)Z

    return-void
.end method""",
        'replacement': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 8

    goto :goto_7f

    nop

    :goto_0
    invoke-static {v2}, Lmiuix/core/util/MiuixUIUtils;->getFontLevel(Landroid/content/Context;)I

    move-result v2

    goto :goto_f

    nop

    :goto_1
    sget v0, Lmiuix/appcompat/R$dimen;->miuix_appcompat_action_bar_subtitle_bottom_padding:I

    goto :goto_12

    nop

    :goto_2
    invoke-virtual {p1, v0}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result v0

    goto :goto_18

    nop

    :goto_3
    invoke-virtual {p1, v0}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result v0

    goto :goto_3d

    nop

    :goto_4
    iput v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mUncollapsePaddingH:I

    goto :goto_1d

    nop

    :goto_5
    invoke-virtual {p1, v0}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result v0

    goto :goto_4e

    nop

    :goto_6
    iget v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mSecondaryTabVerticalPadding:I

    goto :goto_63

    nop

    :goto_7
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    goto :goto_15

    nop

    :goto_8
    iput v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExpandTabTopPadding:I

    goto :goto_2f

    nop

    :goto_9
    invoke-virtual {v0, p1}, Lmiuix/appcompat/internal/app/widget/actionbar/ExpandTitle;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    :goto_a
    goto :goto_10

    nop

    :goto_b
    if-nez v1, :cond_0

    goto :goto_72

    :cond_0
    goto :goto_16

    nop

    :goto_c
    iget v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mUncollapsePaddingH:I

    goto :goto_83

    nop

    :goto_d
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;

    move-result-object v0

    goto :goto_61

    nop

    :goto_e
    return-void

    :goto_f
    const/4 v5, 0x2

    goto :goto_76

    nop

    :goto_10
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mContext:Landroid/content/Context;

    goto :goto_6d

    nop

    :goto_11
    invoke-virtual {p1, v2, v0, v1, v3}, Landroid/content/Context;->obtainStyledAttributes(Landroid/util/AttributeSet;[III)Landroid/content/res/TypedArray;

    move-result-object p1

    goto :goto_38

    nop

    :goto_12
    invoke-virtual {p1, v0}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result v0

    goto :goto_1b

    nop

    :goto_13
    invoke-virtual {p1, v0}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result p1

    goto :goto_7c

    nop

    :goto_14
    invoke-virtual {v1}, Landroid/widget/FrameLayout;->getPaddingTop()I

    move-result v1

    goto :goto_3f

    nop

    :goto_15
    iget v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mUncollapsePaddingH:I

    goto :goto_8b

    nop

    :goto_16
    if-nez v2, :cond_1

    goto :goto_72

    :cond_1
    goto :goto_71

    nop

    :goto_17
    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->updateTightTitle()V

    goto :goto_7e

    nop

    :goto_18
    iput v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mTitleUpViewMarginStart:I

    goto :goto_32

    nop

    :goto_19
    iput v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mUncollapseTabPaddingH:I

    goto :goto_67

    nop

    :goto_1a
    sget v0, Lmiuix/appcompat/R$dimen;->miuix_appcompat_action_bar_secondary_tab_vertical_padding:I

    goto :goto_13

    nop

    :goto_1b
    iput v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExpandSubtitlePaddingBottom:I

    goto :goto_5e

    nop

    :goto_1c
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableTabContainer:Landroid/widget/FrameLayout;

    goto :goto_82

    nop

    :goto_1d
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mSubtitle:Ljava/lang/CharSequence;

    goto :goto_2e

    nop

    :goto_1e
    invoke-virtual {v2}, Landroid/widget/FrameLayout;->getPaddingEnd()I

    move-result v2

    goto :goto_6

    nop

    :goto_1f
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getPaddingTop()I

    move-result v1

    goto :goto_6b

    nop

    :goto_20
    sget v2, Lmiuix/appcompat/R$attr;->actionBarTitleAdaptLargeFont:I

    goto :goto_55

    nop

    :goto_21
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExpandTitle:Lmiuix/appcompat/internal/app/widget/actionbar/ExpandTitle;

    goto :goto_70

    nop

    :goto_22
    iget v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExpandSubtitlePaddingBottom:I

    :goto_23
    goto :goto_7

    nop

    :goto_24
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mContext:Landroid/content/Context;

    goto :goto_58

    nop

    :goto_25
    iput-boolean v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseTitleShowable:Z

    goto :goto_17

    nop

    :goto_26
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableTabContainer:Landroid/widget/FrameLayout;

    goto :goto_3a

    nop

    :goto_27
    invoke-virtual {p1, v0}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result v0

    goto :goto_4

    nop

    :goto_28
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;

    move-result-object p1

    goto :goto_3e

    nop

    :goto_29
    iget v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mSecondaryTabVerticalPadding:I

    goto :goto_68

    nop

    :goto_2a
    invoke-static {p1, v0}, Lmiuix/internal/util/AttributeResolver;->resolveDimensionPixelSize(Landroid/content/Context;I)I

    move-result p1

    goto :goto_d

    nop

    :goto_2b
    sget v4, Lmiuix/appcompat/R$dimen;->miuix_appcompat_action_bar_title_top_padding:I

    goto :goto_40

    nop

    :goto_2c
    invoke-virtual {v1, v2}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I

    move-result v1

    goto :goto_74

    nop

    :goto_2d
    and-int/lit8 v0, v0, 0x8

    goto :goto_66

    nop

    :goto_2e
    invoke-static {v0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v0

    goto :goto_34

    nop

    :goto_2f
    sget v0, Lmiuix/appcompat/R$dimen;->miuix_appcompat_action_bar_title_bottom_padding:I

    goto :goto_3

    nop

    :goto_30
    invoke-virtual {p1, v0}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result v0

    goto :goto_8

    nop

    :goto_31
    iput v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mDensity:F

    goto :goto_59

    nop

    :goto_32
    iput v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mTitleUpViewMarginEnd:I

    goto :goto_43

    nop

    :goto_33
    invoke-direct {p1, p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView$$ExternalSyntheticLambda0;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarView;)V

    goto :goto_4c

    nop

    :goto_34
    if-nez v0, :cond_2

    goto :goto_78

    :cond_2
    goto :goto_3b

    nop

    :goto_35
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mContext:Landroid/content/Context;

    goto :goto_20

    nop

    :goto_36
    sget-object v0, Lmiuix/appcompat/R$styleable;->ActionBar:[I

    goto :goto_73

    nop

    :goto_37
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;

    move-result-object p1

    goto :goto_36

    nop

    :goto_38
    sget v0, Lmiuix/appcompat/R$styleable;->ActionBar_android_minHeight:I

    goto :goto_84

    nop

    :goto_39
    invoke-virtual {p0, p1, v1, v0, v2}, Landroid/view/ViewGroup;->setPaddingRelative(IIII)V

    goto :goto_60

    nop

    :goto_3a
    invoke-virtual {v2}, Landroid/widget/FrameLayout;->getPaddingEnd()I

    move-result v2

    goto :goto_29

    nop

    :goto_3b
    iget v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExpandTitlePaddingBottom:I

    goto :goto_77

    nop

    :goto_3c
    const/4 v2, 0x0

    goto :goto_81

    nop

    :goto_3d
    iput v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExpandTitlePaddingBottom:I

    goto :goto_1

    nop

    :goto_3e
    sget v0, Lmiuix/appcompat/R$attr;->actionBarPaddingStart:I

    goto :goto_2a

    nop

    :goto_3f
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseTabContainer:Landroid/widget/FrameLayout;

    goto :goto_1e

    nop

    :goto_40
    invoke-virtual {v3, v4}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result v3

    goto :goto_c

    nop

    :goto_41
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseTabContainer:Landroid/widget/FrameLayout;

    goto :goto_44

    nop

    :goto_42
    if-nez v1, :cond_3

    goto :goto_4f

    :cond_3
    goto :goto_31

    nop

    :goto_43
    sget v0, Lmiuix/appcompat/R$dimen;->miuix_appcompat_action_bar_title_padding_gap:I

    goto :goto_5

    nop

    :goto_44
    if-nez p1, :cond_4

    goto :goto_64

    :cond_4
    goto :goto_57

    nop

    :goto_45
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseTitle:Lmiuix/appcompat/internal/app/widget/actionbar/CollapseTitle;

    goto :goto_6e

    nop

    :goto_46
    invoke-virtual {p1, v0, v3}, Landroid/content/res/TypedArray;->getLayoutDimension(II)I

    move-result v0

    goto :goto_6c

    nop

    :goto_47
    iget v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mTitleMaxHeight:I

    :goto_48
    goto :goto_86

    nop

    :goto_49
    move v2, v3

    :goto_4a
    goto :goto_b

    nop

    :goto_4b
    sget v0, Lmiuix/appcompat/R$styleable;->ActionBar_android_maxHeight:I

    goto :goto_46

    nop

    :goto_4c
    invoke-virtual {p0, p1}, Landroid/view/ViewGroup;->post(Ljava/lang/Runnable;)Z

    goto :goto_e

    nop

    :goto_4d
    move v2, v4

    goto :goto_52

    nop

    :goto_4e
    iput v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mTitleGapPaddingStart:I

    :goto_4f
    goto :goto_56

    nop

    :goto_50
    invoke-virtual {p1}, Landroid/widget/FrameLayout;->getPaddingStart()I

    move-result v0

    goto :goto_7d

    nop

    :goto_51
    invoke-virtual {p1}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;

    move-result-object v0

    goto :goto_5d

    nop

    :goto_52
    goto :goto_4a

    :goto_53
    goto :goto_49

    nop

    :goto_54
    sget v0, Lmiuix/appcompat/R$styleable;->ActionBar_actionBarMaxSizeInLargeFont:I

    goto :goto_24

    nop

    :goto_55
    const/4 v4, 0x1

    goto :goto_5a

    nop

    :goto_56
    sget v0, Lmiuix/appcompat/R$dimen;->miuix_appcompat_action_bar_title_horizontal_padding:I

    goto :goto_27

    nop

    :goto_57
    invoke-virtual {p1}, Landroid/widget/FrameLayout;->getPaddingStart()I

    move-result v0

    goto :goto_5c

    nop

    :goto_58
    invoke-virtual {v1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v1

    goto :goto_8c

    nop

    :goto_59
    sget v0, Lmiuix/appcompat/R$dimen;->miuix_appcompat_action_bar_title_tab_horizontal_padding:I

    goto :goto_75

    nop

    :goto_5a
    invoke-static {v1, v2, v4}, Lmiuix/internal/util/AttributeResolver;->resolveBoolean(Landroid/content/Context;IZ)Z

    move-result v1

    goto :goto_6a

    nop

    :goto_5b
    invoke-virtual {p1}, Landroid/content/res/TypedArray;->recycle()V

    goto :goto_80

    nop

    :goto_5c
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseTabContainer:Landroid/widget/FrameLayout;

    goto :goto_14

    nop

    :goto_5d
    iget v0, v0, Landroid/util/DisplayMetrics;->density:F

    goto :goto_62

    nop

    :goto_5e
    sget v0, Lmiuix/appcompat/R$dimen;->miuix_appcompat_action_bar_up_view_margin_start:I

    goto :goto_2

    nop

    :goto_5f
    cmpl-float v1, v0, v1

    goto :goto_42

    nop

    :goto_60
    iget-boolean p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mTabsExit:Z

    goto :goto_89

    nop

    :goto_61
    sget v1, Lmiuix/appcompat/R$attr;->actionBarPaddingEnd:I

    goto :goto_6f

    nop

    :goto_62
    iget v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mDensity:F

    goto :goto_5f

    nop

    :goto_63
    invoke-virtual {p1, v0, v1, v2, v3}, Landroid/widget/FrameLayout;->setPaddingRelative(IIII)V

    :goto_64
    goto :goto_1c

    nop

    :goto_65
    new-instance p1, Lmiuix/appcompat/internal/app/widget/ActionBarView$$ExternalSyntheticLambda0;

    goto :goto_33

    nop

    :goto_66
    if-nez v0, :cond_5

    goto :goto_a

    :cond_5
    goto :goto_45

    nop

    :goto_67
    sget v0, Lmiuix/appcompat/R$dimen;->miuix_appcompat_action_bar_title_top_padding:I

    goto :goto_30

    nop

    :goto_68
    invoke-virtual {p1, v0, v1, v2, v3}, Landroid/widget/FrameLayout;->setPaddingRelative(IIII)V

    :goto_69
    goto :goto_28

    nop

    :goto_6a
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mContext:Landroid/content/Context;

    goto :goto_0

    nop

    :goto_6b
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getPaddingBottom()I

    move-result v2

    goto :goto_39

    nop

    :goto_6c
    iput v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mTitleMaxHeight:I

    goto :goto_54

    nop

    :goto_6d
    invoke-virtual {p1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object p1

    goto :goto_51

    nop

    :goto_6e
    if-nez v0, :cond_6

    goto :goto_7a

    :cond_6
    goto :goto_79

    nop

    :goto_6f
    invoke-static {v0, v1}, Lmiuix/internal/util/AttributeResolver;->resolveDimensionPixelSize(Landroid/content/Context;I)I

    move-result v0

    goto :goto_1f

    nop

    :goto_70
    if-nez v0, :cond_7

    goto :goto_a

    :cond_7
    goto :goto_9

    nop

    :goto_71
    goto :goto_48

    :goto_72
    goto :goto_47

    nop

    :goto_73
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->getActionBarStyle()I

    move-result v1

    goto :goto_3c

    nop

    :goto_74
    invoke-virtual {p1, v0, v1}, Landroid/content/res/TypedArray;->getDimensionPixelSize(II)I

    move-result v0

    goto :goto_35

    nop

    :goto_75
    invoke-virtual {p1, v0}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result v0

    goto :goto_19

    nop

    :goto_76
    if-eq v2, v5, :cond_8

    goto :goto_53

    :cond_8
    goto :goto_4d

    nop

    :goto_77
    goto :goto_23

    :goto_78
    goto :goto_22

    nop

    :goto_79
    invoke-virtual {v0, p1}, Lmiuix/appcompat/internal/app/widget/actionbar/CollapseTitle;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    :goto_7a
    goto :goto_21

    nop

    :goto_7b
    invoke-virtual {v1}, Landroid/widget/FrameLayout;->getPaddingTop()I

    move-result v1

    goto :goto_26

    nop

    :goto_7c
    iput p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mSecondaryTabVerticalPadding:I

    goto :goto_41

    nop

    :goto_7d
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableTabContainer:Landroid/widget/FrameLayout;

    goto :goto_7b

    nop

    :goto_7e
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->getDisplayOptions()I

    move-result v0

    goto :goto_2d

    nop

    :goto_7f
    invoke-super {p0, p1}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    goto :goto_37

    nop

    :goto_80
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getResources()Landroid/content/res/Resources;

    move-result-object p1

    goto :goto_85

    nop

    :goto_81
    const/4 v3, 0x0

    goto :goto_11

    nop

    :goto_82
    if-nez p1, :cond_9

    goto :goto_69

    :cond_9
    goto :goto_50

    nop

    :goto_83
    invoke-virtual {v1, v2, v3, v4, v0}, Landroid/widget/FrameLayout;->setPaddingRelative(IIII)V

    goto :goto_1a

    nop

    :goto_84
    invoke-virtual {p1, v0, v3}, Landroid/content/res/TypedArray;->getLayoutDimension(II)I

    move-result v0

    goto :goto_8a

    nop

    :goto_85
    invoke-virtual {p1}, Landroid/content/res/Resources;->getConfiguration()Landroid/content/res/Configuration;

    move-result-object p1

    goto :goto_25

    nop

    :goto_86
    iput v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mTitleMaxHeight:I

    goto :goto_5b

    nop

    :goto_87
    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->updateTabsLayoutParams()V

    :goto_88
    goto :goto_65

    nop

    :goto_89
    if-nez p1, :cond_a

    goto :goto_88

    :cond_a
    goto :goto_87

    nop

    :goto_8a
    iput v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mTitleMinHeight:I

    goto :goto_4b

    nop

    :goto_8b
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getResources()Landroid/content/res/Resources;

    move-result-object v3

    goto :goto_2b

    nop

    :goto_8c
    sget v2, Lmiuix/appcompat/R$dimen;->miuix_appcompat_action_bar_large_font_max_height:I

    goto :goto_2c

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarView__onExpandStateChanged',
        'method': '.method protected onExpandStateChanged(II)V',
        'method_name': 'onExpandStateChanged',
        'method_anchors': ['if-ne p1, v2, :cond_0', 'iput v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mPendingHeight:I', 'iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mPostScroller:Landroid/widget/Scroller;', 'invoke-virtual {p1}, Landroid/widget/Scroller;->isFinished()Z', 'if-nez p1, :cond_0', 'iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mPostScroller:Landroid/widget/Scroller;', 'invoke-virtual {p1, v0}, Landroid/widget/Scroller;->forceFinished(Z)V', 'if-ne p2, v2, :cond_1'],
        'type': 'method_replace',
        'search': """.method protected onExpandStateChanged(II)V
    .registers 8

    const/4 v0, 0x1

    const/4 v1, 0x0

    const/4 v2, 0x2

    if-ne p1, v2, :cond_0

    iput v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mPendingHeight:I

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mPostScroller:Landroid/widget/Scroller;

    invoke-virtual {p1}, Landroid/widget/Scroller;->isFinished()Z

    move-result p1

    if-nez p1, :cond_0

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mPostScroller:Landroid/widget/Scroller;

    invoke-virtual {p1, v0}, Landroid/widget/Scroller;->forceFinished(Z)V

    :cond_0
    if-ne p2, v2, :cond_1

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    if-eqz p1, :cond_1

    invoke-virtual {p1, v1}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setVisibility(I)V

    :cond_1
    const/high16 p1, 0x3f800000

    if-ne p2, v0, :cond_4

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    invoke-virtual {v2}, Landroid/widget/FrameLayout;->getAlpha()F

    move-result v2

    const/4 v3, 0x0

    cmpl-float v2, v2, v3

    if-lez v2, :cond_3

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    if-eqz v2, :cond_2

    const/16 v4, 0x14

    invoke-virtual {v2, v3, v1, v4, v0}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setAnimFrom(FIIZ)V

    :cond_2
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    if-eqz v2, :cond_3

    invoke-virtual {v2, p1, v1, v1, v0}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setAnimFrom(FIIZ)V

    :cond_3
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    if-eqz v2, :cond_4

    invoke-virtual {v2, v1}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setVisibility(I)V

    :cond_4
    if-nez p2, :cond_6

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    if-eqz v2, :cond_5

    iget-boolean v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mInActionMode:Z

    if-nez v3, :cond_5

    invoke-virtual {v2, p1, v1, v1, v0}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setAnimFrom(FIIZ)V

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    invoke-virtual {p1, v1}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setVisibility(I)V

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    invoke-virtual {p1}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->onShow()V

    :cond_5
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    if-eqz p1, :cond_7

    const/16 v1, 0x8

    invoke-virtual {p1, v1}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setVisibility(I)V

    goto :goto_0

    :cond_6
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getHeight()I

    move-result p1

    iget v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseTotalHeight:I

    sub-int/2addr p1, v1

    iget v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseSecondaryTabHeight:I

    add-int/2addr p1, v1

    iput p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mPendingHeight:I

    :cond_7
    :goto_0
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mActionBarTransitionListeners:Ljava/util/List;

    invoke-interface {p1}, Ljava/util/List;->size()I

    move-result p1

    if-lez p1, :cond_b

    iget p1, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mExpandStateBeforeResizing:I

    if-ne p1, p2, :cond_8

    iget p1, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mExpandStateOnLayout:I

    if-eq p1, p2, :cond_b

    :cond_8
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mActionBarTransitionListeners:Ljava/util/List;

    invoke-interface {p0}, Ljava/util/List;->iterator()Ljava/util/Iterator;

    move-result-object p0

    :goto_1
    invoke-interface {p0}, Ljava/util/Iterator;->hasNext()Z

    move-result p1

    if-eqz p1, :cond_b

    invoke-interface {p0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object p1

    invoke-static {p1}, Landroidx/appcompat/app/ToolbarActionBar$$ExternalSyntheticThrowCCEIfNotNull0;->m(Ljava/lang/Object;)V

    const/4 p1, 0x0

    if-eq p2, v0, :cond_a

    if-eqz p2, :cond_9

    goto :goto_1

    :cond_9
    throw p1

    :cond_a
    throw p1

    :cond_b
    return-void
.end method""",
        'replacement': """.method protected onExpandStateChanged(II)V
    .registers 8

    goto :goto_1

    nop

    :goto_0
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mActionBarTransitionListeners:Ljava/util/List;

    goto :goto_f

    nop

    :goto_1
    const/4 v0, 0x1

    goto :goto_3

    nop

    :goto_2
    if-eq p2, v0, :cond_0

    goto :goto_39

    :cond_0
    goto :goto_43

    nop

    :goto_3
    const/4 v1, 0x0

    goto :goto_9

    nop

    :goto_4
    iget v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseSecondaryTabHeight:I

    goto :goto_37

    nop

    :goto_5
    if-eqz v3, :cond_1

    goto :goto_19

    :cond_1
    goto :goto_36

    nop

    :goto_6
    if-nez v2, :cond_2

    goto :goto_19

    :cond_2
    goto :goto_2c

    nop

    :goto_7
    if-ne p2, v0, :cond_3

    goto :goto_4a

    :cond_3
    goto :goto_2a

    nop

    :goto_8
    return-void

    :goto_9
    const/4 v2, 0x2

    goto :goto_45

    nop

    :goto_a
    if-nez p1, :cond_4

    goto :goto_3f

    :cond_4
    goto :goto_10

    nop

    :goto_b
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mActionBarTransitionListeners:Ljava/util/List;

    goto :goto_20

    nop

    :goto_c
    invoke-interface {p0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object p1

    goto :goto_4d

    nop

    :goto_d
    if-nez p1, :cond_5

    goto :goto_26

    :cond_5
    goto :goto_c

    nop

    :goto_e
    if-gtz v2, :cond_6

    goto :goto_4f

    :cond_6
    goto :goto_22

    nop

    :goto_f
    invoke-interface {p1}, Ljava/util/List;->size()I

    move-result p1

    goto :goto_12

    nop

    :goto_10
    const/16 v1, 0x8

    goto :goto_4c

    nop

    :goto_11
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    goto :goto_6

    nop

    :goto_12
    if-gtz p1, :cond_7

    goto :goto_26

    :cond_7
    goto :goto_14

    nop

    :goto_13
    if-eqz p1, :cond_8

    goto :goto_48

    :cond_8
    goto :goto_4b

    nop

    :goto_14
    iget p1, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mExpandStateBeforeResizing:I

    goto :goto_16

    nop

    :goto_15
    invoke-virtual {v2}, Landroid/widget/FrameLayout;->getAlpha()F

    move-result v2

    goto :goto_3c

    nop

    :goto_16
    if-eq p1, p2, :cond_9

    goto :goto_54

    :cond_9
    goto :goto_1d

    nop

    :goto_17
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    goto :goto_23

    nop

    :goto_18
    invoke-virtual {p1}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->onShow()V

    :goto_19
    goto :goto_30

    nop

    :goto_1a
    if-nez v2, :cond_a

    goto :goto_42

    :cond_a
    goto :goto_27

    nop

    :goto_1b
    goto :goto_21

    :goto_1c
    goto :goto_49

    nop

    :goto_1d
    iget p1, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mExpandStateOnLayout:I

    goto :goto_53

    nop

    :goto_1e
    invoke-virtual {p1}, Landroid/widget/Scroller;->isFinished()Z

    move-result p1

    goto :goto_13

    nop

    :goto_1f
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    goto :goto_18

    nop

    :goto_20
    invoke-interface {p0}, Ljava/util/List;->iterator()Ljava/util/Iterator;

    move-result-object p0

    :goto_21
    goto :goto_35

    nop

    :goto_22
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    goto :goto_1a

    nop

    :goto_23
    if-nez v2, :cond_b

    goto :goto_39

    :cond_b
    goto :goto_38

    nop

    :goto_24
    iput v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mPendingHeight:I

    goto :goto_44

    nop

    :goto_25
    throw p1

    :goto_26
    goto :goto_8

    nop

    :goto_27
    const/16 v4, 0x14

    goto :goto_41

    nop

    :goto_28
    if-eqz p2, :cond_c

    goto :goto_3b

    :cond_c
    goto :goto_11

    nop

    :goto_29
    const/4 p1, 0x0

    goto :goto_7

    nop

    :goto_2a
    if-nez p2, :cond_d

    goto :goto_1c

    :cond_d
    goto :goto_1b

    nop

    :goto_2b
    sub-int/2addr p1, v1

    goto :goto_4

    nop

    :goto_2c
    iget-boolean v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mInActionMode:Z

    goto :goto_5

    nop

    :goto_2d
    if-nez v2, :cond_e

    goto :goto_4f

    :cond_e
    goto :goto_4e

    nop

    :goto_2e
    if-eq p2, v2, :cond_f

    goto :goto_52

    :cond_f
    goto :goto_33

    nop

    :goto_2f
    const/high16 p1, 0x3f800000

    goto :goto_2

    nop

    :goto_30
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    goto :goto_a

    nop

    :goto_31
    iget v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseTotalHeight:I

    goto :goto_2b

    nop

    :goto_32
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getHeight()I

    move-result p1

    goto :goto_31

    nop

    :goto_33
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    goto :goto_34

    nop

    :goto_34
    if-nez p1, :cond_10

    goto :goto_52

    :cond_10
    goto :goto_51

    nop

    :goto_35
    invoke-interface {p0}, Ljava/util/Iterator;->hasNext()Z

    move-result p1

    goto :goto_d

    nop

    :goto_36
    invoke-virtual {v2, p1, v1, v1, v0}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setAnimFrom(FIIZ)V

    goto :goto_50

    nop

    :goto_37
    add-int/2addr p1, v1

    goto :goto_3e

    nop

    :goto_38
    invoke-virtual {v2, v1}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setVisibility(I)V

    :goto_39
    goto :goto_28

    nop

    :goto_3a
    goto :goto_3f

    :goto_3b
    goto :goto_32

    nop

    :goto_3c
    const/4 v3, 0x0

    goto :goto_46

    nop

    :goto_3d
    invoke-virtual {p1, v1}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setVisibility(I)V

    goto :goto_1f

    nop

    :goto_3e
    iput p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mPendingHeight:I

    :goto_3f
    goto :goto_0

    nop

    :goto_40
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    goto :goto_2d

    nop

    :goto_41
    invoke-virtual {v2, v3, v1, v4, v0}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setAnimFrom(FIIZ)V

    :goto_42
    goto :goto_40

    nop

    :goto_43
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    goto :goto_15

    nop

    :goto_44
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mPostScroller:Landroid/widget/Scroller;

    goto :goto_1e

    nop

    :goto_45
    if-eq p1, v2, :cond_11

    goto :goto_48

    :cond_11
    goto :goto_24

    nop

    :goto_46
    cmpl-float v2, v2, v3

    goto :goto_e

    nop

    :goto_47
    invoke-virtual {p1, v0}, Landroid/widget/Scroller;->forceFinished(Z)V

    :goto_48
    goto :goto_2e

    nop

    :goto_49
    throw p1

    :goto_4a
    goto :goto_25

    nop

    :goto_4b
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mPostScroller:Landroid/widget/Scroller;

    goto :goto_47

    nop

    :goto_4c
    invoke-virtual {p1, v1}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setVisibility(I)V

    goto :goto_3a

    nop

    :goto_4d
    invoke-static {p1}, Landroidx/appcompat/app/ToolbarActionBar$$ExternalSyntheticThrowCCEIfNotNull0;->m(Ljava/lang/Object;)V

    goto :goto_29

    nop

    :goto_4e
    invoke-virtual {v2, p1, v1, v1, v0}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setAnimFrom(FIIZ)V

    :goto_4f
    goto :goto_17

    nop

    :goto_50
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    goto :goto_3d

    nop

    :goto_51
    invoke-virtual {p1, v1}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setVisibility(I)V

    :goto_52
    goto :goto_2f

    nop

    :goto_53
    if-ne p1, p2, :cond_12

    goto :goto_26

    :cond_12
    :goto_54
    goto :goto_b

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarView__onLayout',
        'method': '.method protected onLayout(ZIIII)V',
        'method_name': 'onLayout',
        'method_anchors': ['iget v1, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mTitleMinHeight:I', 'iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMainContainer:Landroid/widget/FrameLayout;', 'invoke-virtual {v2}, Landroid/widget/FrameLayout;->getMeasuredHeight()I', 'invoke-static {v1, v2}, Ljava/lang/Math;->max(II)I', 'iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCustomNavView:Landroid/view/View;', 'if-eqz v2, :cond_0', 'invoke-virtual {v2}, Landroid/view/View;->getParent()Landroid/view/ViewParent;', 'if-ne v2, p0, :cond_0'],
        'type': 'method_replace',
        'search': """.method protected onLayout(ZIIII)V
    .registers 17

    iget v1, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mTitleMinHeight:I

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMainContainer:Landroid/widget/FrameLayout;

    invoke-virtual {v2}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result v2

    invoke-static {v1, v2}, Ljava/lang/Math;->max(II)I

    move-result v1

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCustomNavView:Landroid/view/View;

    if-eqz v2, :cond_0

    invoke-virtual {v2}, Landroid/view/View;->getParent()Landroid/view/ViewParent;

    move-result-object v2

    if-ne v2, p0, :cond_0

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCustomNavView:Landroid/view/View;

    invoke-virtual {v2}, Landroid/view/View;->getMeasuredHeight()I

    move-result v2

    invoke-static {v1, v2}, Ljava/lang/Math;->max(II)I

    move-result v1

    :cond_0
    move v5, v1

    iget v6, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseSecondaryTabHeight:I

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    invoke-virtual {v1}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result v1

    iget v7, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableSecondaryTabHeight:I

    iget v2, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mInnerExpandState:I

    const/4 v3, 0x2

    if-ne v2, v3, :cond_1

    iget v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mPendingHeight:I

    goto :goto_0

    :cond_1
    const/4 v3, 0x1

    if-ne v2, v3, :cond_2

    add-int v2, v1, v7

    goto :goto_0

    :cond_2
    const/4 v2, 0x0

    :goto_0
    sub-int v3, p5, p3

    sub-int v8, v3, v7

    sub-int v9, v8, v2

    add-int v3, v1, v7

    sub-int/2addr v3, v2

    int-to-float v2, v3

    int-to-float v3, v1

    div-float/2addr v2, v3

    const/high16 v3, 0x3f800000

    invoke-static {v3, v2}, Ljava/lang/Math;->min(FF)F

    move-result v2

    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->hasTitle()Z

    move-result v4

    if-nez v4, :cond_3

    if-nez v1, :cond_3

    move v10, v3

    goto :goto_1

    :cond_3
    move v10, v2

    :goto_1
    const/4 v3, 0x0

    move-object v0, p0

    move v1, p1

    move v2, p2

    move v4, p4

    invoke-direct/range {v0 .. v6}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->onLayoutCollapseViews(ZIIIII)V

    move v6, v7

    move v5, v8

    move v3, v9

    move v7, v10

    invoke-virtual/range {v0 .. v7}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->onLayoutExpandViews(ZIIIIIF)V

    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->notifyMenuStateChange()V

    iget-boolean v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mInActionMode:Z

    if-nez v1, :cond_4

    iget-boolean v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mInActionModeAnimating:Z

    if-nez v1, :cond_4

    invoke-direct {p0, v7}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->animateLayoutWithProcess(F)V

    :cond_4
    iput v7, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mLastProcess:F

    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->updateBadgeOnMenuItemViews()V

    return-void
.end method""",
        'replacement': """.method protected onLayout(ZIIII)V
    .registers 17

    goto :goto_2a

    nop

    :goto_0
    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->updateBadgeOnMenuItemViews()V

    goto :goto_2d

    nop

    :goto_1
    const/4 v3, 0x1

    goto :goto_3c

    nop

    :goto_2
    iget-boolean v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mInActionModeAnimating:Z

    goto :goto_1c

    nop

    :goto_3
    move v5, v1

    goto :goto_3a

    nop

    :goto_4
    div-float/2addr v2, v3

    goto :goto_a

    nop

    :goto_5
    int-to-float v2, v3

    goto :goto_35

    nop

    :goto_6
    move v10, v2

    :goto_7
    goto :goto_32

    nop

    :goto_8
    goto :goto_39

    :goto_9
    goto :goto_38

    nop

    :goto_a
    const/high16 v3, 0x3f800000

    goto :goto_3b

    nop

    :goto_b
    invoke-virtual/range {v0 .. v7}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->onLayoutExpandViews(ZIIIIIF)V

    goto :goto_34

    nop

    :goto_c
    invoke-static {v1, v2}, Ljava/lang/Math;->max(II)I

    move-result v1

    :goto_d
    goto :goto_3

    nop

    :goto_e
    invoke-virtual {v1}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result v1

    goto :goto_27

    nop

    :goto_f
    if-eqz v1, :cond_0

    goto :goto_19

    :cond_0
    goto :goto_2

    nop

    :goto_10
    sub-int v3, p5, p3

    goto :goto_24

    nop

    :goto_11
    invoke-direct/range {v0 .. v6}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->onLayoutCollapseViews(ZIIIII)V

    goto :goto_31

    nop

    :goto_12
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCustomNavView:Landroid/view/View;

    goto :goto_3f

    nop

    :goto_13
    iget v2, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mInnerExpandState:I

    goto :goto_21

    nop

    :goto_14
    move v10, v3

    goto :goto_2b

    nop

    :goto_15
    goto :goto_39

    :goto_16
    goto :goto_1

    nop

    :goto_17
    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->hasTitle()Z

    move-result v4

    goto :goto_28

    nop

    :goto_18
    invoke-direct {p0, v7}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->animateLayoutWithProcess(F)V

    :goto_19
    goto :goto_30

    nop

    :goto_1a
    move v5, v8

    goto :goto_1e

    nop

    :goto_1b
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    goto :goto_e

    nop

    :goto_1c
    if-eqz v1, :cond_1

    goto :goto_19

    :cond_1
    goto :goto_18

    nop

    :goto_1d
    invoke-virtual {v2}, Landroid/view/View;->getParent()Landroid/view/ViewParent;

    move-result-object v2

    goto :goto_29

    nop

    :goto_1e
    move v3, v9

    goto :goto_3d

    nop

    :goto_1f
    invoke-virtual {v2}, Landroid/view/View;->getMeasuredHeight()I

    move-result v2

    goto :goto_c

    nop

    :goto_20
    sub-int v9, v8, v2

    goto :goto_40

    nop

    :goto_21
    const/4 v3, 0x2

    goto :goto_44

    nop

    :goto_22
    invoke-static {v1, v2}, Ljava/lang/Math;->max(II)I

    move-result v1

    goto :goto_12

    nop

    :goto_23
    iget v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mPendingHeight:I

    goto :goto_15

    nop

    :goto_24
    sub-int v8, v3, v7

    goto :goto_20

    nop

    :goto_25
    if-eqz v1, :cond_2

    goto :goto_2c

    :cond_2
    goto :goto_14

    nop

    :goto_26
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMainContainer:Landroid/widget/FrameLayout;

    goto :goto_41

    nop

    :goto_27
    iget v7, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableSecondaryTabHeight:I

    goto :goto_13

    nop

    :goto_28
    if-eqz v4, :cond_3

    goto :goto_2c

    :cond_3
    goto :goto_25

    nop

    :goto_29
    if-eq v2, p0, :cond_4

    goto :goto_d

    :cond_4
    goto :goto_3e

    nop

    :goto_2a
    iget v1, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mTitleMinHeight:I

    goto :goto_26

    nop

    :goto_2b
    goto :goto_7

    :goto_2c
    goto :goto_6

    nop

    :goto_2d
    return-void

    :goto_2e
    add-int v2, v1, v7

    goto :goto_8

    nop

    :goto_2f
    sub-int/2addr v3, v2

    goto :goto_5

    nop

    :goto_30
    iput v7, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mLastProcess:F

    goto :goto_0

    nop

    :goto_31
    move v6, v7

    goto :goto_1a

    nop

    :goto_32
    const/4 v3, 0x0

    goto :goto_33

    nop

    :goto_33
    move-object v0, p0

    goto :goto_37

    nop

    :goto_34
    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->notifyMenuStateChange()V

    goto :goto_36

    nop

    :goto_35
    int-to-float v3, v1

    goto :goto_4

    nop

    :goto_36
    iget-boolean v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mInActionMode:Z

    goto :goto_f

    nop

    :goto_37
    move v1, p1

    goto :goto_43

    nop

    :goto_38
    const/4 v2, 0x0

    :goto_39
    goto :goto_10

    nop

    :goto_3a
    iget v6, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseSecondaryTabHeight:I

    goto :goto_1b

    nop

    :goto_3b
    invoke-static {v3, v2}, Ljava/lang/Math;->min(FF)F

    move-result v2

    goto :goto_17

    nop

    :goto_3c
    if-eq v2, v3, :cond_5

    goto :goto_9

    :cond_5
    goto :goto_2e

    nop

    :goto_3d
    move v7, v10

    goto :goto_b

    nop

    :goto_3e
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCustomNavView:Landroid/view/View;

    goto :goto_1f

    nop

    :goto_3f
    if-nez v2, :cond_6

    goto :goto_d

    :cond_6
    goto :goto_1d

    nop

    :goto_40
    add-int v3, v1, v7

    goto :goto_2f

    nop

    :goto_41
    invoke-virtual {v2}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result v2

    goto :goto_22

    nop

    :goto_42
    move v4, p4

    goto :goto_11

    nop

    :goto_43
    move v2, p2

    goto :goto_42

    nop

    :goto_44
    if-eq v2, v3, :cond_7

    goto :goto_16

    :cond_7
    goto :goto_23

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarView__onLayoutExpandViews',
        'method': '.method protected onLayoutExpandViews(ZIIIIIF)V',
        'method_name': 'onLayoutExpandViews',
        'method_anchors': ['invoke-direct {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->hasTitle()Z', 'if-nez v1, :cond_0', 'iget-object v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableMainContainer:Landroid/widget/FrameLayout;', 'iget-object v7, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableTabContainer:Landroid/widget/FrameLayout;', 'invoke-static {v5, v3}, Ljava/lang/Math;->min(FF)F', 'if-gtz v3, :cond_1', 'iget v3, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseSecondaryTabHeight:I', 'if-eqz v1, :cond_2'],
        'type': 'method_replace',
        'search': """.method protected onLayoutExpandViews(ZIIIIIF)V
    .registers 24

    move-object/from16 v0, p0

    move/from16 v2, p2

    move/from16 v4, p4

    move/from16 v6, p5

    invoke-direct {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->hasTitle()Z

    move-result v1

    if-nez v1, :cond_0

    goto :goto_5

    :cond_0
    iget-object v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    iget-object v7, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableTabContainer:Landroid/widget/FrameLayout;

    const/high16 v3, 0x40400000

    mul-float v3, v3, p7

    const/high16 v5, 0x3f800000

    invoke-static {v5, v3}, Ljava/lang/Math;->min(FF)F

    move-result v3

    sub-float/2addr v5, v3

    const/4 v3, 0x0

    cmpg-float v3, v5, v3

    const/4 v8, 0x0

    if-gtz v3, :cond_1

    iget v3, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseSecondaryTabHeight:I

    goto :goto_0

    :cond_1
    move v3, v8

    :goto_0
    if-eqz v1, :cond_2

    invoke-virtual {v1}, Landroid/view/ViewGroup;->getVisibility()I

    move-result v5

    if-nez v5, :cond_2

    invoke-virtual {v1}, Landroid/view/ViewGroup;->getMeasuredHeight()I

    move-result v5

    move v9, v5

    goto :goto_1

    :cond_2
    move v9, v8

    :goto_1
    iget v10, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableSecondaryTabHeight:I

    add-int v5, p3, v9

    add-int/2addr v5, v10

    sub-int/2addr v5, v6

    add-int/2addr v3, v5

    const/4 v11, 0x0

    if-eqz v1, :cond_6

    invoke-virtual {v1}, Landroid/view/ViewGroup;->getVisibility()I

    move-result v5

    if-nez v5, :cond_6

    iget v5, v0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mInnerExpandState:I

    if-eqz v5, :cond_6

    sub-int v5, v6, v9

    invoke-virtual {v1, v2, v5, v4, v6}, Landroid/view/ViewGroup;->layout(IIII)V

    iget-object v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    invoke-direct {v0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->hasTabsInContainer(Landroid/view/ViewGroup;)Z

    move-result v1

    if-eqz v1, :cond_3

    iget-object v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    invoke-virtual {v1, v8}, Landroid/widget/FrameLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v1

    check-cast v1, Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView;

    goto :goto_2

    :cond_3
    move-object v1, v11

    :goto_2
    if-eqz v1, :cond_5

    iget v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mUncollapsePaddingH:I

    invoke-static {v0}, Lmiuix/internal/util/ViewUtils;->isLayoutRtl(Landroid/view/View;)Z

    move-result v12

    if-eqz v12, :cond_4

    iget v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mUncollapsePaddingH:I

    sub-int v5, v4, v5

    invoke-virtual {v1}, Landroid/widget/HorizontalScrollView;->getMeasuredWidth()I

    move-result v12

    sub-int/2addr v5, v12

    :cond_4
    iget v12, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExpandTabTopPadding:I

    invoke-virtual {v1}, Landroid/widget/HorizontalScrollView;->getMeasuredWidth()I

    move-result v13

    add-int/2addr v13, v5

    invoke-virtual {v1}, Landroid/widget/HorizontalScrollView;->getMeasuredHeight()I

    move-result v14

    iget v15, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExpandTabTopPadding:I

    add-int/2addr v14, v15

    invoke-virtual {v1, v5, v12, v13, v14}, Landroid/widget/HorizontalScrollView;->layout(IIII)V

    :cond_5
    iget-object v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    add-int v5, v9, v10

    invoke-direct/range {v0 .. v5}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->clipViewBounds(Landroid/view/View;IIII)V

    :cond_6
    move v12, v3

    if-lez v10, :cond_b

    iget v1, v0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mInnerExpandState:I

    if-eqz v1, :cond_b

    iget v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mUncollapseTabPaddingH:I

    iget v2, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExtraPadding:I

    add-int/2addr v1, v2

    add-int v2, p2, v1

    add-int v5, v6, p6

    sub-int v3, v5, v10

    invoke-virtual {v7}, Landroid/view/ViewGroup;->getMeasuredWidth()I

    move-result v1

    add-int v4, v2, v1

    move-object v1, v7

    invoke-static/range {v0 .. v5}, Lmiuix/internal/util/ViewUtils;->layoutChildView(Landroid/view/ViewGroup;Landroid/view/View;IIII)V

    invoke-direct {v0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->hasTabsInContainer(Landroid/view/ViewGroup;)Z

    move-result v2

    if-eqz v2, :cond_7

    invoke-virtual {v1, v8}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;

    move-result-object v2

    move-object v11, v2

    check-cast v11, Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView;

    :cond_7
    if-eqz v11, :cond_9

    invoke-virtual {v11}, Landroid/widget/HorizontalScrollView;->getMeasuredWidth()I

    move-result v2

    invoke-static {v0}, Lmiuix/internal/util/ViewUtils;->isLayoutRtl(Landroid/view/View;)Z

    move-result v3

    if-eqz v3, :cond_8

    iget v2, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mUncollapseTabPaddingH:I

    mul-int/lit8 v2, v2, 0x2

    sub-int v2, p4, v2

    invoke-virtual {v11}, Landroid/widget/HorizontalScrollView;->getMeasuredWidth()I

    move-result v3

    sub-int/2addr v2, v3

    iget v3, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mUncollapseTabPaddingH:I

    mul-int/lit8 v3, v3, 0x2

    sub-int v3, p4, v3

    goto :goto_3

    :cond_8
    move v3, v2

    move v2, v8

    :goto_3
    invoke-virtual {v11}, Landroid/widget/HorizontalScrollView;->getMeasuredHeight()I

    move-result v4

    invoke-virtual {v11, v2, v8, v3, v4}, Landroid/widget/HorizontalScrollView;->layout(IIII)V

    :cond_9
    if-lt v9, v10, :cond_a

    sub-int v2, v9, v10

    sub-int v3, v12, v2

    goto :goto_4

    :cond_a
    sub-int v3, v12, v9

    :goto_4
    add-int v5, v9, v10

    move/from16 v2, p2

    move/from16 v4, p4

    invoke-direct/range {v0 .. v5}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->clipViewBounds(Landroid/view/View;IIII)V

    :cond_b
    :goto_5
    return-void
.end method""",
        'replacement': """.method protected onLayoutExpandViews(ZIIIIIF)V
    .registers 24

    goto :goto_68

    nop

    :goto_0
    if-nez v11, :cond_0

    goto :goto_d

    :cond_0
    goto :goto_12

    nop

    :goto_1
    iget v15, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExpandTabTopPadding:I

    goto :goto_2a

    nop

    :goto_2
    iget-object v7, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableTabContainer:Landroid/widget/FrameLayout;

    goto :goto_45

    nop

    :goto_3
    if-nez v3, :cond_1

    goto :goto_57

    :cond_1
    goto :goto_26

    nop

    :goto_4
    invoke-direct {v0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->hasTabsInContainer(Landroid/view/ViewGroup;)Z

    move-result v2

    goto :goto_6f

    nop

    :goto_5
    invoke-virtual {v11}, Landroid/widget/HorizontalScrollView;->getMeasuredHeight()I

    move-result v4

    goto :goto_c

    nop

    :goto_6
    invoke-virtual {v11}, Landroid/widget/HorizontalScrollView;->getMeasuredWidth()I

    move-result v3

    goto :goto_5f

    nop

    :goto_7
    add-int v5, v6, p6

    goto :goto_55

    nop

    :goto_8
    invoke-direct {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->hasTitle()Z

    move-result v1

    goto :goto_7b

    nop

    :goto_9
    move-object v1, v11

    :goto_a
    goto :goto_5c

    nop

    :goto_b
    add-int/2addr v5, v10

    goto :goto_2d

    nop

    :goto_c
    invoke-virtual {v11, v2, v8, v3, v4}, Landroid/widget/HorizontalScrollView;->layout(IIII)V

    :goto_d
    goto :goto_6d

    nop

    :goto_e
    invoke-virtual {v1, v8}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;

    move-result-object v2

    goto :goto_64

    nop

    :goto_f
    move v3, v8

    :goto_10
    goto :goto_28

    nop

    :goto_11
    iget-object v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    goto :goto_62

    nop

    :goto_12
    invoke-virtual {v11}, Landroid/widget/HorizontalScrollView;->getMeasuredWidth()I

    move-result v2

    goto :goto_32

    nop

    :goto_13
    cmpg-float v3, v5, v3

    goto :goto_3a

    nop

    :goto_14
    invoke-virtual {v1}, Landroid/widget/HorizontalScrollView;->getMeasuredWidth()I

    move-result v13

    goto :goto_1e

    nop

    :goto_15
    iget v12, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExpandTabTopPadding:I

    goto :goto_14

    nop

    :goto_16
    invoke-virtual {v1}, Landroid/widget/HorizontalScrollView;->getMeasuredHeight()I

    move-result v14

    goto :goto_1

    nop

    :goto_17
    goto :goto_a

    :goto_18
    goto :goto_9

    nop

    :goto_19
    iget-object v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    goto :goto_2

    nop

    :goto_1a
    invoke-virtual {v1, v5, v12, v13, v14}, Landroid/widget/HorizontalScrollView;->layout(IIII)V

    :goto_1b
    goto :goto_77

    nop

    :goto_1c
    const/4 v3, 0x0

    goto :goto_13

    nop

    :goto_1d
    add-int v5, v9, v10

    goto :goto_7c

    nop

    :goto_1e
    add-int/2addr v13, v5

    goto :goto_16

    nop

    :goto_1f
    sub-int v5, v4, v5

    goto :goto_23

    nop

    :goto_20
    add-int v5, v9, v10

    goto :goto_43

    nop

    :goto_21
    const/high16 v5, 0x3f800000

    goto :goto_4c

    nop

    :goto_22
    if-eqz v5, :cond_2

    goto :goto_25

    :cond_2
    goto :goto_39

    nop

    :goto_23
    invoke-virtual {v1}, Landroid/widget/HorizontalScrollView;->getMeasuredWidth()I

    move-result v12

    goto :goto_53

    nop

    :goto_24
    goto :goto_34

    :goto_25
    goto :goto_33

    nop

    :goto_26
    iget v2, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mUncollapseTabPaddingH:I

    goto :goto_5e

    nop

    :goto_27
    move/from16 v4, p4

    goto :goto_69

    nop

    :goto_28
    if-nez v1, :cond_3

    goto :goto_25

    :cond_3
    goto :goto_52

    nop

    :goto_29
    if-lez v3, :cond_4

    goto :goto_49

    :cond_4
    goto :goto_59

    nop

    :goto_2a
    add-int/2addr v14, v15

    goto :goto_1a

    nop

    :goto_2b
    goto :goto_47

    :goto_2c
    goto :goto_46

    nop

    :goto_2d
    sub-int/2addr v5, v6

    goto :goto_3d

    nop

    :goto_2e
    invoke-direct {v0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->hasTabsInContainer(Landroid/view/ViewGroup;)Z

    move-result v1

    goto :goto_38

    nop

    :goto_2f
    move v12, v3

    goto :goto_40

    nop

    :goto_30
    if-nez v1, :cond_5

    goto :goto_42

    :cond_5
    goto :goto_76

    nop

    :goto_31
    sub-int v5, v6, v9

    goto :goto_7f

    nop

    :goto_32
    invoke-static {v0}, Lmiuix/internal/util/ViewUtils;->isLayoutRtl(Landroid/view/View;)Z

    move-result v3

    goto :goto_3

    nop

    :goto_33
    move v9, v8

    :goto_34
    goto :goto_44

    nop

    :goto_35
    mul-int/lit8 v3, v3, 0x2

    goto :goto_66

    nop

    :goto_36
    const/4 v11, 0x0

    goto :goto_4b

    nop

    :goto_37
    iget-object v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    goto :goto_2e

    nop

    :goto_38
    if-nez v1, :cond_6

    goto :goto_18

    :cond_6
    goto :goto_11

    nop

    :goto_39
    invoke-virtual {v1}, Landroid/view/ViewGroup;->getMeasuredHeight()I

    move-result v5

    goto :goto_5d

    nop

    :goto_3a
    const/4 v8, 0x0

    goto :goto_29

    nop

    :goto_3b
    iget v1, v0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mInnerExpandState:I

    goto :goto_30

    nop

    :goto_3c
    if-nez v12, :cond_7

    goto :goto_54

    :cond_7
    goto :goto_50

    nop

    :goto_3d
    add-int/2addr v3, v5

    goto :goto_36

    nop

    :goto_3e
    iget v2, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExtraPadding:I

    goto :goto_4d

    nop

    :goto_3f
    add-int v2, p2, v1

    goto :goto_7

    nop

    :goto_40
    if-gtz v10, :cond_8

    goto :goto_42

    :cond_8
    goto :goto_3b

    nop

    :goto_41
    invoke-direct/range {v0 .. v5}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->clipViewBounds(Landroid/view/View;IIII)V

    :goto_42
    goto :goto_5a

    nop

    :goto_43
    move/from16 v2, p2

    goto :goto_75

    nop

    :goto_44
    iget v10, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableSecondaryTabHeight:I

    goto :goto_6e

    nop

    :goto_45
    const/high16 v3, 0x40400000

    goto :goto_71

    nop

    :goto_46
    sub-int v3, v12, v9

    :goto_47
    goto :goto_20

    nop

    :goto_48
    goto :goto_10

    :goto_49
    goto :goto_f

    nop

    :goto_4a
    invoke-static {v0}, Lmiuix/internal/util/ViewUtils;->isLayoutRtl(Landroid/view/View;)Z

    move-result v12

    goto :goto_3c

    nop

    :goto_4b
    if-nez v1, :cond_9

    goto :goto_7d

    :cond_9
    goto :goto_51

    nop

    :goto_4c
    invoke-static {v5, v3}, Ljava/lang/Math;->min(FF)F

    move-result v3

    goto :goto_7e

    nop

    :goto_4d
    add-int/2addr v1, v2

    goto :goto_3f

    nop

    :goto_4e
    check-cast v11, Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView;

    :goto_4f
    goto :goto_0

    nop

    :goto_50
    iget v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mUncollapsePaddingH:I

    goto :goto_1f

    nop

    :goto_51
    invoke-virtual {v1}, Landroid/view/ViewGroup;->getVisibility()I

    move-result v5

    goto :goto_73

    nop

    :goto_52
    invoke-virtual {v1}, Landroid/view/ViewGroup;->getVisibility()I

    move-result v5

    goto :goto_22

    nop

    :goto_53
    sub-int/2addr v5, v12

    :goto_54
    goto :goto_15

    nop

    :goto_55
    sub-int v3, v5, v10

    goto :goto_61

    nop

    :goto_56
    goto :goto_6b

    :goto_57
    goto :goto_60

    nop

    :goto_58
    iget v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mUncollapsePaddingH:I

    goto :goto_4a

    nop

    :goto_59
    iget v3, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseSecondaryTabHeight:I

    goto :goto_48

    nop

    :goto_5a
    return-void

    :goto_5b
    invoke-static/range {v0 .. v5}, Lmiuix/internal/util/ViewUtils;->layoutChildView(Landroid/view/ViewGroup;Landroid/view/View;IIII)V

    goto :goto_4

    nop

    :goto_5c
    if-nez v1, :cond_a

    goto :goto_1b

    :cond_a
    goto :goto_58

    nop

    :goto_5d
    move v9, v5

    goto :goto_24

    nop

    :goto_5e
    mul-int/lit8 v2, v2, 0x2

    goto :goto_74

    nop

    :goto_5f
    sub-int/2addr v2, v3

    goto :goto_63

    nop

    :goto_60
    move v3, v2

    goto :goto_6a

    nop

    :goto_61
    invoke-virtual {v7}, Landroid/view/ViewGroup;->getMeasuredWidth()I

    move-result v1

    goto :goto_67

    nop

    :goto_62
    invoke-virtual {v1, v8}, Landroid/widget/FrameLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v1

    goto :goto_6c

    nop

    :goto_63
    iget v3, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mUncollapseTabPaddingH:I

    goto :goto_35

    nop

    :goto_64
    move-object v11, v2

    goto :goto_4e

    nop

    :goto_65
    sub-int v3, v12, v2

    goto :goto_2b

    nop

    :goto_66
    sub-int v3, p4, v3

    goto :goto_56

    nop

    :goto_67
    add-int v4, v2, v1

    goto :goto_70

    nop

    :goto_68
    move-object/from16 v0, p0

    goto :goto_72

    nop

    :goto_69
    move/from16 v6, p5

    goto :goto_8

    nop

    :goto_6a
    move v2, v8

    :goto_6b
    goto :goto_5

    nop

    :goto_6c
    check-cast v1, Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView;

    goto :goto_17

    nop

    :goto_6d
    if-ge v9, v10, :cond_b

    goto :goto_2c

    :cond_b
    goto :goto_81

    nop

    :goto_6e
    add-int v5, p3, v9

    goto :goto_b

    nop

    :goto_6f
    if-nez v2, :cond_c

    goto :goto_4f

    :cond_c
    goto :goto_e

    nop

    :goto_70
    move-object v1, v7

    goto :goto_5b

    nop

    :goto_71
    mul-float v3, v3, p7

    goto :goto_21

    nop

    :goto_72
    move/from16 v2, p2

    goto :goto_27

    nop

    :goto_73
    if-eqz v5, :cond_d

    goto :goto_7d

    :cond_d
    goto :goto_78

    nop

    :goto_74
    sub-int v2, p4, v2

    goto :goto_6

    nop

    :goto_75
    move/from16 v4, p4

    goto :goto_41

    nop

    :goto_76
    iget v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mUncollapseTabPaddingH:I

    goto :goto_3e

    nop

    :goto_77
    iget-object v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    goto :goto_1d

    nop

    :goto_78
    iget v5, v0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mInnerExpandState:I

    goto :goto_80

    nop

    :goto_79
    goto :goto_42

    :goto_7a
    goto :goto_19

    nop

    :goto_7b
    if-eqz v1, :cond_e

    goto :goto_7a

    :cond_e
    goto :goto_79

    nop

    :goto_7c
    invoke-direct/range {v0 .. v5}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->clipViewBounds(Landroid/view/View;IIII)V

    :goto_7d
    goto :goto_2f

    nop

    :goto_7e
    sub-float/2addr v5, v3

    goto :goto_1c

    nop

    :goto_7f
    invoke-virtual {v1, v2, v5, v4, v6}, Landroid/view/ViewGroup;->layout(IIII)V

    goto :goto_37

    nop

    :goto_80
    if-nez v5, :cond_f

    goto :goto_7d

    :cond_f
    goto :goto_31

    nop

    :goto_81
    sub-int v2, v9, v10

    goto :goto_65

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarView__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['invoke-virtual {v0}, Landroid/view/ViewGroup;->getChildCount()I', 'if-ge v3, v1, :cond_2', 'invoke-virtual {v0, v3}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;', 'invoke-virtual {v6}, Landroid/view/View;->getVisibility()I', 'if-eq v7, v5, :cond_1', 'iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;', 'if-ne v6, v5, :cond_0', 'invoke-virtual {v5}, Landroid/widget/LinearLayout;->getChildCount()I'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 26

    move-object/from16 v0, p0

    invoke-virtual {v0}, Landroid/view/ViewGroup;->getChildCount()I

    move-result v1

    const/4 v2, 0x0

    move v3, v2

    move v4, v3

    :goto_0
    const/16 v5, 0x8

    if-ge v3, v1, :cond_2

    invoke-virtual {v0, v3}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;

    move-result-object v6

    invoke-virtual {v6}, Landroid/view/View;->getVisibility()I

    move-result v7

    if-eq v7, v5, :cond_1

    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    if-ne v6, v5, :cond_0

    invoke-virtual {v5}, Landroid/widget/LinearLayout;->getChildCount()I

    move-result v5

    if-eqz v5, :cond_1

    :cond_0
    add-int/lit8 v4, v4, 0x1

    :cond_1
    add-int/lit8 v3, v3, 0x1

    goto :goto_0

    :cond_2
    const/4 v1, 0x1

    if-nez v4, :cond_3

    invoke-virtual {v0, v2, v2}, Landroid/view/ViewGroup;->setMeasuredDimension(II)V

    iput-boolean v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mIsCollapsed:Z

    return-void

    :cond_3
    iput-boolean v2, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mIsCollapsed:Z

    invoke-static/range {p1 .. p1}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v3

    iget v4, v0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mTitleMaxHeight:I

    iget v6, v0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mTitleMinHeight:I

    invoke-virtual {v0}, Landroid/view/ViewGroup;->getPaddingTop()I

    move-result v7

    invoke-virtual {v0}, Landroid/view/ViewGroup;->getPaddingBottom()I

    move-result v8

    add-int/2addr v7, v8

    invoke-virtual {v0}, Landroid/view/ViewGroup;->getPaddingStart()I

    move-result v8

    invoke-virtual {v0}, Landroid/view/ViewGroup;->getPaddingEnd()I

    move-result v9

    if-lez v4, :cond_4

    move v10, v4

    goto :goto_1

    :cond_4
    invoke-static/range {p2 .. p2}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v10

    :goto_1
    sub-int/2addr v10, v7

    const/high16 v11, -0x80000000

    invoke-static {v10, v11}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v12

    sub-int v13, v3, v8

    sub-int/2addr v13, v9

    div-int/lit8 v14, v13, 0x2

    invoke-direct {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->hasTitle()Z

    move-result v15

    iget-object v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mStartView:Landroid/view/View;

    if-eqz v1, :cond_5

    invoke-virtual {v1}, Landroid/view/View;->getVisibility()I

    move-result v1

    if-eq v1, v5, :cond_5

    iget-object v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mStartView:Landroid/view/View;

    invoke-virtual {v0, v1, v13, v12, v2}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->measureChildView(Landroid/view/View;III)I

    move-result v13

    iget-object v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mStartView:Landroid/view/View;

    invoke-virtual {v1}, Landroid/view/View;->getMeasuredWidth()I

    move-result v1

    add-int/2addr v8, v1

    iget-object v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mStartView:Landroid/view/View;

    invoke-virtual {v1}, Landroid/view/View;->getMeasuredHeight()I

    move-result v1

    add-int/2addr v1, v7

    goto :goto_2

    :cond_5
    move v1, v2

    :goto_2
    iget-object v11, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mEndView:Landroid/view/View;

    if-eqz v11, :cond_6

    invoke-virtual {v11}, Landroid/view/View;->getVisibility()I

    move-result v11

    if-eq v11, v5, :cond_6

    iget-object v11, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mEndView:Landroid/view/View;

    invoke-virtual {v0, v11, v13, v12, v2}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->measureChildView(Landroid/view/View;III)I

    move-result v13

    iget-object v11, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mEndView:Landroid/view/View;

    invoke-virtual {v11}, Landroid/view/View;->getMeasuredWidth()I

    move-result v11

    add-int/2addr v9, v11

    iget-object v11, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mEndView:Landroid/view/View;

    invoke-virtual {v11}, Landroid/view/View;->getMeasuredHeight()I

    move-result v11

    add-int/2addr v11, v7

    invoke-static {v1, v11}, Ljava/lang/Math;->max(II)I

    move-result v1

    :cond_6
    iget-object v11, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mNavigatorSwitch:Landroid/view/View;

    if-eqz v11, :cond_7

    sget v5, Lmiuix/appcompat/R$id;->miuix_appcompat_navigator_switch_presenter:I

    invoke-virtual {v11, v5}, Landroid/view/View;->getTag(I)Ljava/lang/Object;

    move-result-object v5

    check-cast v5, Lmiuix/appcompat/internal/app/NavigatorSwitchPresenter;

    invoke-virtual {v5, v2, v2}, Lmiuix/appcompat/internal/app/NavigatorSwitchPresenter;->suppressVisibility(ZI)V

    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mNavigatorSwitch:Landroid/view/View;

    invoke-virtual {v5}, Landroid/view/View;->getVisibility()I

    move-result v5

    const/16 v11, 0x8

    if-eq v5, v11, :cond_7

    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mNavigatorSwitch:Landroid/view/View;

    invoke-virtual {v0, v5, v13, v12, v2}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->measureChildView(Landroid/view/View;III)I

    move-result v13

    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mNavigatorSwitch:Landroid/view/View;

    invoke-virtual {v5}, Landroid/view/View;->getMeasuredWidth()I

    move-result v5

    add-int/2addr v8, v5

    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mNavigatorSwitch:Landroid/view/View;

    invoke-virtual {v5}, Landroid/view/View;->getMeasuredHeight()I

    move-result v5

    add-int/2addr v5, v7

    invoke-static {v1, v5}, Ljava/lang/Math;->max(II)I

    move-result v1

    :cond_7
    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mStartView:Landroid/view/View;

    if-eqz v5, :cond_8

    invoke-virtual {v5}, Landroid/view/View;->getVisibility()I

    move-result v5

    if-eqz v5, :cond_8

    iput-boolean v2, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mHasStartView:Z

    :cond_8
    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mNavigatorSwitch:Landroid/view/View;

    if-eqz v5, :cond_9

    invoke-virtual {v5}, Landroid/view/View;->getVisibility()I

    move-result v5

    if-eqz v5, :cond_9

    iput-boolean v2, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mHasNavigatorSwitchView:Z

    :cond_9
    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExpandedActionView:Landroid/view/View;

    if-eqz v5, :cond_a

    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExpandedHomeLayout:Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;

    goto :goto_3

    :cond_a
    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mHomeLayout:Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;

    :goto_3
    iget-object v11, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mStartView:Landroid/view/View;

    if-eqz v11, :cond_b

    if-eqz v5, :cond_b

    const/16 v11, 0x8

    invoke-virtual {v5, v11}, Landroid/widget/FrameLayout;->setVisibility(I)V

    goto :goto_4

    :cond_b
    const/16 v11, 0x8

    :goto_4
    if-eqz v5, :cond_d

    invoke-virtual {v5}, Landroid/widget/FrameLayout;->getVisibility()I

    move-result v2

    if-eq v2, v11, :cond_d

    invoke-virtual {v5}, Landroid/widget/FrameLayout;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v2

    iget v2, v2, Landroid/view/ViewGroup$LayoutParams;->width:I

    if-gez v2, :cond_c

    const/high16 v11, -0x80000000

    invoke-static {v13, v11}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v2

    goto :goto_5

    :cond_c
    const/high16 v11, 0x40000000

    invoke-static {v2, v11}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v2

    :goto_5
    invoke-virtual {v5, v2, v12}, Landroid/widget/FrameLayout;->measure(II)V

    invoke-virtual {v5}, Landroid/widget/FrameLayout;->getMeasuredWidth()I

    move-result v2

    invoke-virtual {v5}, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->getStartOffset()I

    move-result v11

    add-int/2addr v2, v11

    sub-int/2addr v13, v2

    const/4 v11, 0x0

    invoke-static {v11, v13}, Ljava/lang/Math;->max(II)I

    move-result v13

    move/from16 v16, v2

    sub-int v2, v13, v16

    invoke-static {v11, v2}, Ljava/lang/Math;->max(II)I

    move-result v2

    add-int v8, v8, v16

    invoke-virtual {v5}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result v5

    add-int/2addr v5, v7

    invoke-static {v1, v5}, Ljava/lang/Math;->max(II)I

    move-result v1

    goto :goto_6

    :cond_d
    move v2, v14

    :goto_6
    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mEndMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    if-eqz v5, :cond_e

    invoke-virtual {v5}, Landroid/widget/LinearLayout;->getParent()Landroid/view/ViewParent;

    move-result-object v5

    if-ne v5, v0, :cond_e

    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mEndMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    invoke-virtual {v5}, Landroid/widget/LinearLayout;->getVisibility()I

    move-result v5

    const/16 v11, 0x8

    if-eq v5, v11, :cond_e

    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mEndMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    const/4 v11, 0x0

    invoke-virtual {v0, v5, v13, v12, v11}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->measureChildView(Landroid/view/View;III)I

    move-result v13

    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mEndMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    invoke-virtual {v5}, Landroid/widget/LinearLayout;->getMeasuredWidth()I

    move-result v5

    sub-int/2addr v14, v5

    invoke-static {v11, v14}, Ljava/lang/Math;->max(II)I

    move-result v14

    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mEndMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    invoke-virtual {v5}, Landroid/widget/LinearLayout;->getMeasuredWidth()I

    move-result v5

    add-int/2addr v9, v5

    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mEndMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    invoke-virtual {v5}, Landroid/widget/LinearLayout;->getMeasuredHeight()I

    move-result v5

    add-int/2addr v5, v7

    invoke-static {v1, v5}, Ljava/lang/Math;->max(II)I

    move-result v1

    :cond_e
    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mIndeterminateProgressView:Landroid/widget/ProgressBar;

    if-eqz v5, :cond_f

    invoke-virtual {v5}, Landroid/widget/ProgressBar;->getVisibility()I

    move-result v5

    const/16 v11, 0x8

    const/16 v16, 0x2

    if-eq v5, v11, :cond_10

    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mIndeterminateProgressView:Landroid/widget/ProgressBar;

    iget v11, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mProgressBarPadding:I

    mul-int/lit8 v11, v11, 0x2

    invoke-virtual {v0, v5, v13, v12, v11}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->measureChildView(Landroid/view/View;III)I

    move-result v13

    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mIndeterminateProgressView:Landroid/widget/ProgressBar;

    invoke-virtual {v5}, Landroid/widget/ProgressBar;->getMeasuredWidth()I

    move-result v5

    sub-int/2addr v14, v5

    iget v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mProgressBarPadding:I

    mul-int/lit8 v5, v5, 0x2

    sub-int/2addr v14, v5

    const/4 v11, 0x0

    invoke-static {v11, v14}, Ljava/lang/Math;->max(II)I

    move-result v14

    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mIndeterminateProgressView:Landroid/widget/ProgressBar;

    invoke-virtual {v5}, Landroid/widget/ProgressBar;->getMeasuredWidth()I

    move-result v5

    add-int/2addr v9, v5

    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mIndeterminateProgressView:Landroid/widget/ProgressBar;

    invoke-virtual {v5}, Landroid/widget/ProgressBar;->getMeasuredHeight()I

    move-result v5

    add-int/2addr v5, v7

    invoke-static {v1, v5}, Ljava/lang/Math;->max(II)I

    move-result v1

    goto :goto_7

    :cond_f
    const/16 v16, 0x2

    :cond_10
    :goto_7
    invoke-direct {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->isShowTitle()Z

    move-result v5

    if-eqz v5, :cond_11

    invoke-direct {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->updateTitleCenter()V

    :cond_11
    iget-object v11, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExpandedActionView:Landroid/view/View;

    if-nez v11, :cond_12

    if-nez v5, :cond_13

    invoke-virtual {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->getDisplayOptions()I

    move-result v11

    and-int/lit8 v11, v11, 0x20

    if-eqz v11, :cond_12

    goto :goto_8

    :cond_12
    move/from16 v17, v5

    goto :goto_d

    :cond_13
    :goto_8
    iget-object v11, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mTitleUpView:Landroid/view/View;

    if-eqz v11, :cond_12

    invoke-virtual {v11}, Landroid/view/View;->getVisibility()I

    move-result v11

    if-nez v11, :cond_12

    iget-object v11, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mTitleUpView:Landroid/view/View;

    move/from16 v17, v5

    iget-boolean v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mHasStartView:Z

    if-nez v5, :cond_15

    iget-boolean v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mHasNavigatorSwitchView:Z

    if-eqz v5, :cond_14

    goto :goto_9

    :cond_14
    const/4 v5, 0x0

    goto :goto_a

    :cond_15
    :goto_9
    iget v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mTitleUpViewMarginStart:I

    move/from16 v18, v5

    iget v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mTitleUpViewMarginEnd:I

    add-int v5, v18, v5

    :goto_a
    invoke-virtual {v0, v11, v13, v12, v5}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->measureChildView(Landroid/view/View;III)I

    move-result v13

    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mTitleUpView:Landroid/view/View;

    invoke-virtual {v5}, Landroid/view/View;->getMeasuredWidth()I

    move-result v5

    iget-boolean v11, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mHasStartView:Z

    if-nez v11, :cond_17

    iget-boolean v11, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mHasNavigatorSwitchView:Z

    if-eqz v11, :cond_16

    goto :goto_b

    :cond_16
    move/from16 v18, v5

    const/4 v5, 0x0

    goto :goto_c

    :cond_17
    :goto_b
    iget v11, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mTitleUpViewMarginStart:I

    move/from16 v18, v5

    iget v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mTitleUpViewMarginEnd:I

    add-int/2addr v5, v11

    :goto_c
    add-int v5, v18, v5

    add-int/2addr v8, v5

    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mTitleUpView:Landroid/view/View;

    invoke-virtual {v5}, Landroid/view/View;->getMeasuredHeight()I

    move-result v5

    add-int/2addr v5, v7

    invoke-static {v1, v5}, Ljava/lang/Math;->max(II)I

    :goto_d
    iget-object v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExpandedActionView:Landroid/view/View;

    if-eqz v1, :cond_18

    goto :goto_e

    :cond_18
    iget v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mDisplayOptions:I

    and-int/lit8 v1, v1, 0x10

    if-eqz v1, :cond_19

    iget-object v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCustomNavView:Landroid/view/View;

    if-eqz v1, :cond_19

    goto :goto_e

    :cond_19
    const/4 v1, 0x0

    :goto_e
    iget-object v7, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mStartView:Landroid/view/View;

    if-nez v7, :cond_1b

    iget-object v7, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mEndView:Landroid/view/View;

    if-eqz v7, :cond_1a

    goto :goto_f

    :cond_1a
    const/16 v11, 0x8

    goto :goto_10

    :cond_1b
    :goto_f
    if-eqz v1, :cond_1a

    const/16 v11, 0x8

    invoke-virtual {v1, v11}, Landroid/view/View;->setVisibility(I)V

    :goto_10
    if-eqz v1, :cond_29

    invoke-virtual {v1}, Landroid/view/View;->getVisibility()I

    move-result v7

    if-eq v7, v11, :cond_29

    iget-object v7, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mTitleUpView:Landroid/view/View;

    if-eqz v7, :cond_1c

    invoke-virtual {v7}, Landroid/view/View;->getVisibility()I

    move-result v7

    const/4 v11, 0x4

    if-ne v7, v11, :cond_1c

    iget-object v7, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mTitleUpView:Landroid/view/View;

    invoke-virtual {v7}, Landroid/view/View;->getMeasuredWidth()I

    move-result v7

    goto :goto_11

    :cond_1c
    const/4 v7, 0x0

    :goto_11
    invoke-virtual {v1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v11

    invoke-virtual {v0, v11}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->generateLayoutParams(Landroid/view/ViewGroup$LayoutParams;)Landroid/view/ViewGroup$LayoutParams;

    move-result-object v11

    instance-of v5, v11, Landroidx/appcompat/app/ActionBar$LayoutParams;

    if-eqz v5, :cond_1d

    move-object v5, v11

    check-cast v5, Landroidx/appcompat/app/ActionBar$LayoutParams;

    goto :goto_12

    :cond_1d
    const/4 v5, 0x0

    :goto_12
    move/from16 v18, v7

    if-eqz v5, :cond_1e

    iget v7, v5, Landroid/view/ViewGroup$MarginLayoutParams;->leftMargin:I

    move/from16 v19, v7

    iget v7, v5, Landroid/view/ViewGroup$MarginLayoutParams;->rightMargin:I

    add-int v7, v19, v7

    move/from16 v19, v7

    iget v7, v5, Landroid/view/ViewGroup$MarginLayoutParams;->topMargin:I

    move/from16 v20, v7

    iget v7, v5, Landroid/view/ViewGroup$MarginLayoutParams;->bottomMargin:I

    add-int v7, v20, v7

    goto :goto_13

    :cond_1e
    const/4 v7, 0x0

    const/16 v19, 0x0

    :goto_13
    if-gtz v4, :cond_20

    move/from16 v20, v7

    :cond_1f
    const/high16 v7, -0x80000000

    :goto_14
    move/from16 v21, v10

    goto :goto_15

    :cond_20
    move/from16 v20, v7

    iget v7, v11, Landroid/view/ViewGroup$LayoutParams;->height:I

    if-ltz v7, :cond_1f

    const/high16 v7, 0x40000000

    goto :goto_14

    :goto_15
    iget v10, v11, Landroid/view/ViewGroup$LayoutParams;->height:I

    move/from16 v22, v15

    const/4 v15, -0x1

    if-ltz v10, :cond_21

    if-lez v4, :cond_23

    invoke-static {v10, v4}, Ljava/lang/Math;->min(II)I

    move-result v10

    goto :goto_17

    :cond_21
    if-ne v10, v15, :cond_22

    invoke-static {v6, v4}, Ljava/lang/Math;->max(II)I

    move-result v10

    goto :goto_16

    :cond_22
    move/from16 v10, v21

    :goto_16
    sub-int v10, v10, v20

    :cond_23
    :goto_17
    iget v4, v11, Landroid/view/ViewGroup$LayoutParams;->width:I

    const/4 v15, -0x2

    if-eq v4, v15, :cond_24

    const/high16 v15, 0x40000000

    goto :goto_18

    :cond_24
    const/high16 v15, -0x80000000

    :goto_18
    if-ltz v4, :cond_25

    move/from16 v21, v3

    add-int v3, v13, v18

    invoke-static {v4, v3}, Ljava/lang/Math;->min(II)I

    move-result v3

    goto :goto_19

    :cond_25
    move/from16 v21, v3

    add-int v3, v13, v18

    :goto_19
    sub-int v3, v3, v19

    const/4 v4, 0x0

    invoke-static {v4, v3}, Ljava/lang/Math;->max(II)I

    move-result v3

    if-eqz v5, :cond_26

    iget v4, v5, Landroidx/appcompat/app/ActionBar$LayoutParams;->gravity:I

    goto :goto_1a

    :cond_26
    const v4, 0x800013

    :goto_1a
    const v5, 0x800007

    and-int/2addr v4, v5

    const/4 v5, 0x1

    if-ne v4, v5, :cond_27

    iget v4, v11, Landroid/view/ViewGroup$LayoutParams;->width:I

    const/4 v5, -0x1

    if-ne v4, v5, :cond_27

    invoke-static {v2, v14}, Ljava/lang/Math;->min(II)I

    move-result v2

    mul-int/lit8 v3, v2, 0x2

    :cond_27
    iget-object v2, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mNavigatorSwitch:Landroid/view/View;

    if-eqz v2, :cond_28

    invoke-virtual {v2}, Landroid/view/View;->getVisibility()I

    move-result v2

    if-nez v2, :cond_28

    int-to-float v2, v3

    iget-object v3, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mNavigatorSwitch:Landroid/view/View;

    invoke-virtual {v3}, Landroid/view/View;->getMeasuredWidth()I

    move-result v3

    int-to-float v3, v3

    iget-object v4, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mNavigatorSwitch:Landroid/view/View;

    invoke-virtual {v4}, Landroid/view/View;->getAlpha()F

    move-result v4

    const/high16 v5, 0x3f800000

    sub-float/2addr v5, v4

    mul-float/2addr v3, v5

    iget v4, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mTitleUpViewMarginStart:I

    int-to-float v4, v4

    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mNavigatorSwitch:Landroid/view/View;

    invoke-virtual {v5}, Landroid/view/View;->getAlpha()F

    move-result v5

    mul-float/2addr v4, v5

    sub-float/2addr v3, v4

    add-float/2addr v2, v3

    float-to-int v3, v2

    :cond_28
    invoke-static {v3, v15}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v2

    invoke-static {v10, v7}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v3

    invoke-virtual {v1, v2, v3}, Landroid/view/View;->measure(II)V

    invoke-virtual {v1}, Landroid/view/View;->getMeasuredWidth()I

    move-result v2

    add-int v19, v19, v2

    sub-int v19, v19, v18

    sub-int v13, v13, v19

    invoke-virtual {v1}, Landroid/view/View;->getMeasuredHeight()I

    move-result v1

    invoke-static {v6, v1}, Ljava/lang/Math;->max(II)I

    move-result v1

    :goto_1b
    const/4 v11, 0x0

    goto :goto_1c

    :cond_29
    move/from16 v21, v3

    move/from16 v22, v15

    iget-object v2, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseTabs:Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView;

    if-eqz v2, :cond_2a

    const/4 v11, 0x0

    invoke-virtual {v0, v2, v13, v12, v11}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->measureChildView(Landroid/view/View;III)I

    iget-object v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseTabs:Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView;

    invoke-virtual {v1}, Landroid/widget/HorizontalScrollView;->getMeasuredHeight()I

    move-result v1

    invoke-static {v6, v1}, Ljava/lang/Math;->max(II)I

    move-result v1

    goto :goto_1b

    :cond_2a
    if-eqz v1, :cond_2b

    invoke-virtual {v1}, Landroid/view/View;->getVisibility()I

    move-result v1

    const/16 v11, 0x8

    if-ne v1, v11, :cond_2b

    if-nez v17, :cond_2b

    move v1, v6

    const/4 v11, 0x1

    goto :goto_1c

    :cond_2b
    move v1, v6

    goto :goto_1b

    :goto_1c
    iget-object v2, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExpandedActionView:Landroid/view/View;

    if-nez v2, :cond_2e

    if-eqz v17, :cond_2e

    invoke-direct {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->isTitleCenter()Z

    move-result v2

    if-eqz v2, :cond_2d

    if-le v8, v9, :cond_2c

    mul-int/lit8 v8, v8, 0x2

    sub-int v3, v21, v8

    goto :goto_1d

    :cond_2c
    move v3, v13

    :goto_1d
    iget-object v2, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMainContainer:Landroid/widget/FrameLayout;

    const/4 v4, 0x0

    invoke-static {v4, v3}, Ljava/lang/Math;->max(II)I

    move-result v3

    const/high16 v5, -0x80000000

    invoke-static {v3, v5}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v3

    invoke-virtual {v2, v3, v12}, Landroid/widget/FrameLayout;->measure(II)V

    iget-object v2, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMainContainer:Landroid/widget/FrameLayout;

    invoke-virtual {v2}, Landroid/widget/FrameLayout;->getMeasuredWidth()I

    move-result v2

    sub-int/2addr v13, v2

    goto :goto_1e

    :cond_2d
    const/4 v4, 0x0

    iget-object v2, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMainContainer:Landroid/widget/FrameLayout;

    invoke-virtual {v0, v2, v13, v12, v4}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->measureChildView(Landroid/view/View;III)I

    move-result v2

    move v13, v2

    :goto_1e
    iget-object v2, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMainContainer:Landroid/widget/FrameLayout;

    invoke-virtual {v2}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result v2

    invoke-static {v6, v2}, Ljava/lang/Math;->max(II)I

    move-result v2

    goto :goto_1f

    :cond_2e
    move v2, v6

    :goto_1f
    iget-object v3, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    invoke-virtual {v3}, Landroid/widget/FrameLayout;->getChildCount()I

    move-result v3

    if-eqz v3, :cond_30

    if-eqz v22, :cond_2f

    const/4 v3, 0x0

    goto :goto_20

    :cond_2f
    const/high16 v3, 0x40000000

    :goto_20
    iget-object v4, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    move/from16 v5, v21

    const/high16 v7, -0x80000000

    invoke-static {v5, v7}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v8

    const/4 v7, 0x0

    invoke-static {v7, v3}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v3

    invoke-virtual {v4, v8, v3}, Landroid/widget/FrameLayout;->measure(II)V

    goto :goto_21

    :cond_30
    move/from16 v5, v21

    const/4 v7, 0x0

    :goto_21
    invoke-direct {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->shouldMeasureCollapseTabContainer()Z

    move-result v3

    invoke-direct {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->shouldMeasureMovableTabContainer()Z

    move-result v4

    iput v7, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableSecondaryTabHeight:I

    invoke-virtual {v0}, Landroid/view/ViewGroup;->getResources()Landroid/content/res/Resources;

    move-result-object v7

    invoke-virtual {v7}, Landroid/content/res/Resources;->getConfiguration()Landroid/content/res/Configuration;

    move-result-object v7

    iget v7, v7, Landroid/content/res/Configuration;->densityDpi:I

    int-to-float v7, v7

    const/high16 v8, 0x43200000

    div-float/2addr v7, v8

    iget-object v8, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExtraPaddingPolicy:Lmiuix/container/ExtraPaddingPolicy;

    if-eqz v8, :cond_31

    invoke-virtual {v8}, Lmiuix/container/ExtraPaddingPolicy;->isEnable()Z

    move-result v8

    if-eqz v8, :cond_31

    iget-object v8, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExtraPaddingPolicy:Lmiuix/container/ExtraPaddingPolicy;

    invoke-virtual {v8}, Lmiuix/container/ExtraPaddingPolicy;->getExtraPaddingDp()I

    move-result v8

    int-to-float v8, v8

    mul-float/2addr v8, v7

    float-to-int v7, v8

    iput v7, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExtraPadding:I

    const/4 v7, 0x0

    goto :goto_22

    :cond_31
    const/4 v7, 0x0

    iput v7, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExtraPadding:I

    :goto_22
    iget v8, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mUncollapseTabPaddingH:I

    iget v9, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExtraPadding:I

    add-int/2addr v8, v9

    mul-int/lit8 v8, v8, 0x2

    sub-int v8, v5, v8

    invoke-static {v7, v8}, Ljava/lang/Math;->max(II)I

    move-result v8

    iget v9, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mUncollapseTabPaddingH:I

    iget v10, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExtraPadding:I

    add-int/2addr v9, v10

    mul-int/lit8 v9, v9, 0x2

    sub-int v9, v5, v9

    if-eqz v4, :cond_32

    iget-object v4, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableTabContainer:Landroid/widget/FrameLayout;

    const/high16 v10, 0x40000000

    invoke-static {v8, v10}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v8

    invoke-static {v7, v7}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v14

    invoke-virtual {v4, v8, v14}, Landroid/widget/FrameLayout;->measure(II)V

    iget-object v4, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableTabContainer:Landroid/widget/FrameLayout;

    invoke-virtual {v4}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result v4

    iput v4, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableSecondaryTabHeight:I

    goto :goto_23

    :cond_32
    const/high16 v10, 0x40000000

    move v4, v7

    :goto_23
    iput v7, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseSecondaryTabHeight:I

    if-eqz v3, :cond_33

    iget-object v3, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseTabContainer:Landroid/widget/FrameLayout;

    invoke-static {v9, v10}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v8

    invoke-static {v7, v7}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v9

    invoke-virtual {v3, v8, v9}, Landroid/widget/FrameLayout;->measure(II)V

    iget-object v3, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseTabContainer:Landroid/widget/FrameLayout;

    invoke-virtual {v3}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result v3

    iput v3, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseSecondaryTabHeight:I

    goto :goto_24

    :cond_33
    const/4 v3, 0x0

    :goto_24
    iget-object v7, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExpandedActionView:Landroid/view/View;

    if-nez v7, :cond_36

    iget v7, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mNavigationMode:I

    const/4 v8, 0x1

    if-eq v7, v8, :cond_34

    goto :goto_25

    :cond_34
    iget-object v7, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mListNavLayout:Landroid/widget/LinearLayout;

    if-eqz v7, :cond_36

    iget v7, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mItemPadding:I

    if-eqz v17, :cond_35

    mul-int/lit8 v7, v7, 0x2

    :cond_35
    sub-int/2addr v13, v7

    const/4 v7, 0x0

    invoke-static {v7, v13}, Ljava/lang/Math;->max(II)I

    move-result v8

    iget-object v7, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mListNavLayout:Landroid/widget/LinearLayout;

    const/high16 v9, -0x80000000

    invoke-static {v8, v9}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v8

    invoke-virtual {v7, v8, v12}, Landroid/widget/LinearLayout;->measure(II)V

    :cond_36
    :goto_25
    if-eqz v22, :cond_37

    iget-object v7, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    invoke-virtual {v7}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result v7

    goto :goto_26

    :cond_37
    const/4 v7, 0x0

    :goto_26
    add-int v8, v2, v3

    invoke-static {v1, v8}, Ljava/lang/Math;->max(II)I

    move-result v8

    iput v8, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseTotalHeight:I

    invoke-static {v6, v8}, Ljava/lang/Math;->max(II)I

    move-result v6

    iput v6, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseTotalHeight:I

    invoke-static {v1, v2}, Ljava/lang/Math;->max(II)I

    move-result v1

    add-int/2addr v1, v7

    add-int/2addr v1, v4

    iput v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExpandTotalHeight:I

    if-eqz v11, :cond_38

    const/4 v11, 0x0

    invoke-virtual {v0, v5, v11}, Landroid/view/ViewGroup;->setMeasuredDimension(II)V

    const/4 v8, 0x1

    iput-boolean v8, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mIsCollapsed:Z

    return-void

    :cond_38
    const/4 v8, 0x1

    iget v2, v0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mInnerExpandState:I

    move/from16 v4, v16

    if-ne v2, v4, :cond_39

    iget v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseTotalHeight:I

    sub-int v2, v1, v3

    iget v3, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mPendingHeight:I

    add-int/2addr v2, v3

    invoke-static {v2, v1}, Ljava/lang/Math;->max(II)I

    move-result v1

    invoke-virtual {v0, v5, v1}, Landroid/view/ViewGroup;->setMeasuredDimension(II)V

    goto :goto_27

    :cond_39
    if-ne v2, v8, :cond_3a

    invoke-virtual {v0, v5, v1}, Landroid/view/ViewGroup;->setMeasuredDimension(II)V

    goto :goto_27

    :cond_3a
    iget v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseTotalHeight:I

    invoke-virtual {v0, v5, v1}, Landroid/view/ViewGroup;->setMeasuredDimension(II)V

    :goto_27
    iget-object v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mProgressView:Landroid/widget/ProgressBar;

    if-eqz v1, :cond_3b

    invoke-virtual {v1}, Landroid/widget/ProgressBar;->getVisibility()I

    move-result v1

    const/16 v11, 0x8

    if-eq v1, v11, :cond_3b

    iget-object v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mProgressView:Landroid/widget/ProgressBar;

    iget v2, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mProgressBarPadding:I

    const/16 v16, 0x2

    mul-int/lit8 v2, v2, 0x2

    sub-int v3, v5, v2

    const/high16 v10, 0x40000000

    invoke-static {v3, v10}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v2

    invoke-virtual {v0}, Landroid/view/ViewGroup;->getMeasuredHeight()I

    move-result v0

    const/high16 v5, -0x80000000

    invoke-static {v0, v5}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v0

    invoke-virtual {v1, v2, v0}, Landroid/widget/ProgressBar;->measure(II)V

    :cond_3b
    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 26

    goto :goto_15d

    nop

    :goto_0
    invoke-static {v1, v5}, Ljava/lang/Math;->max(II)I

    move-result v1

    :goto_1
    goto :goto_8a

    nop

    :goto_2
    check-cast v5, Landroidx/appcompat/app/ActionBar$LayoutParams;

    goto :goto_1b

    nop

    :goto_3
    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mNavigatorSwitch:Landroid/view/View;

    goto :goto_21b

    nop

    :goto_4
    iput v7, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExtraPadding:I

    :goto_5
    goto :goto_71

    nop

    :goto_6
    const/4 v4, 0x0

    goto :goto_189

    nop

    :goto_7
    invoke-static {v11, v2}, Ljava/lang/Math;->max(II)I

    move-result v2

    goto :goto_198

    nop

    :goto_8
    invoke-static {v10, v4}, Ljava/lang/Math;->min(II)I

    move-result v10

    goto :goto_25

    nop

    :goto_9
    if-gtz v4, :cond_0

    goto :goto_10f

    :cond_0
    goto :goto_10b

    nop

    :goto_a
    invoke-static {v0, v5}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v0

    goto :goto_83

    nop

    :goto_b
    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mNavigatorSwitch:Landroid/view/View;

    goto :goto_24f

    nop

    :goto_c
    iget-object v7, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mListNavLayout:Landroid/widget/LinearLayout;

    goto :goto_1c8

    nop

    :goto_d
    invoke-virtual {v5}, Landroid/widget/ProgressBar;->getMeasuredWidth()I

    move-result v5

    goto :goto_141

    nop

    :goto_e
    if-nez v11, :cond_1

    goto :goto_287

    :cond_1
    goto :goto_f5

    nop

    :goto_f
    invoke-static {v11, v14}, Ljava/lang/Math;->max(II)I

    move-result v14

    goto :goto_68

    nop

    :goto_10
    sub-int v19, v19, v18

    goto :goto_1ae

    nop

    :goto_11
    invoke-direct {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->isTitleCenter()Z

    move-result v2

    goto :goto_28f

    nop

    :goto_12
    invoke-virtual {v5}, Landroid/view/View;->getMeasuredHeight()I

    move-result v5

    goto :goto_236

    nop

    :goto_13
    if-nez v5, :cond_2

    goto :goto_1

    :cond_2
    goto :goto_7d

    nop

    :goto_14
    goto :goto_178

    :goto_15
    goto :goto_1f6

    nop

    :goto_16
    invoke-virtual {v11}, Landroid/view/View;->getMeasuredHeight()I

    move-result v11

    goto :goto_202

    nop

    :goto_17
    int-to-float v2, v3

    goto :goto_113

    nop

    :goto_18
    invoke-virtual {v2}, Landroid/view/View;->getVisibility()I

    move-result v2

    goto :goto_b6

    nop

    :goto_19
    if-nez v7, :cond_3

    goto :goto_1cf

    :cond_3
    goto :goto_1ce

    nop

    :goto_1a
    if-nez v2, :cond_4

    goto :goto_36

    :cond_4
    goto :goto_138

    nop

    :goto_1b
    goto :goto_28e

    :goto_1c
    goto :goto_28d

    nop

    :goto_1d
    const/16 v11, 0x8

    goto :goto_1cc

    nop

    :goto_1e
    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mIndeterminateProgressView:Landroid/widget/ProgressBar;

    goto :goto_15f

    nop

    :goto_1f
    int-to-float v7, v7

    goto :goto_22f

    nop

    :goto_20
    iget v7, v5, Landroid/view/ViewGroup$MarginLayoutParams;->leftMargin:I

    goto :goto_264

    nop

    :goto_21
    invoke-static {v7, v3}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v3

    goto :goto_25a

    nop

    :goto_22
    return-void

    :goto_23
    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    goto :goto_27e

    nop

    :goto_24
    const/4 v15, -0x2

    goto :goto_18d

    nop

    :goto_25
    goto :goto_ab

    :goto_26
    goto :goto_179

    nop

    :goto_27
    if-ne v11, v5, :cond_5

    goto :goto_1ef

    :cond_5
    goto :goto_3d

    nop

    :goto_28
    iget-object v7, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mEndView:Landroid/view/View;

    goto :goto_19

    nop

    :goto_29
    const/4 v11, 0x0

    goto :goto_f

    nop

    :goto_2a
    iget v3, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mPendingHeight:I

    goto :goto_1a7

    nop

    :goto_2b
    move/from16 v20, v7

    :goto_2c
    goto :goto_24a

    nop

    :goto_2d
    invoke-virtual {v5, v2, v12}, Landroid/widget/FrameLayout;->measure(II)V

    goto :goto_ee

    nop

    :goto_2e
    div-float/2addr v7, v8

    goto :goto_10d

    nop

    :goto_2f
    add-int v3, v13, v18

    goto :goto_8b

    nop

    :goto_30
    if-nez v5, :cond_6

    goto :goto_1b4

    :cond_6
    goto :goto_1b3

    nop

    :goto_31
    add-int v7, v19, v7

    goto :goto_6d

    nop

    :goto_32
    iget-object v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mStartView:Landroid/view/View;

    goto :goto_c7

    nop

    :goto_33
    goto :goto_25f

    :goto_34
    goto :goto_1c4

    nop

    :goto_35
    goto :goto_24d

    :goto_36
    goto :goto_1a1

    nop

    :goto_37
    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mStartView:Landroid/view/View;

    goto :goto_7e

    nop

    :goto_38
    iget v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mProgressBarPadding:I

    goto :goto_80

    nop

    :goto_39
    const/4 v15, -0x1

    goto :goto_25d

    nop

    :goto_3a
    const/high16 v5, -0x80000000

    goto :goto_a

    nop

    :goto_3b
    invoke-direct {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->hasTitle()Z

    move-result v15

    goto :goto_132

    nop

    :goto_3c
    invoke-static {v1, v5}, Ljava/lang/Math;->max(II)I

    move-result v1

    goto :goto_280

    nop

    :goto_3d
    iget-object v11, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mEndView:Landroid/view/View;

    goto :goto_bf

    nop

    :goto_3e
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getChildCount()I

    move-result v1

    goto :goto_217

    nop

    :goto_3f
    iget-object v11, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mEndView:Landroid/view/View;

    goto :goto_1ed

    nop

    :goto_40
    invoke-direct {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->shouldMeasureCollapseTabContainer()Z

    move-result v3

    goto :goto_255

    nop

    :goto_41
    goto :goto_276

    :goto_42
    goto :goto_164

    nop

    :goto_43
    div-int/lit8 v14, v13, 0x2

    goto :goto_3b

    nop

    :goto_44
    invoke-static {v10, v11}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v12

    goto :goto_b8

    nop

    :goto_45
    move/from16 v20, v7

    goto :goto_1f8

    nop

    :goto_46
    invoke-virtual {v0, v11, v13, v12, v5}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->measureChildView(Landroid/view/View;III)I

    move-result v13

    goto :goto_1d0

    nop

    :goto_47
    sub-int/2addr v14, v5

    goto :goto_122

    nop

    :goto_48
    if-eq v4, v5, :cond_7

    goto :goto_11d

    :cond_7
    goto :goto_118

    nop

    :goto_49
    if-eqz v2, :cond_8

    goto :goto_74

    :cond_8
    goto :goto_279

    nop

    :goto_4a
    add-int/2addr v7, v8

    goto :goto_219

    nop

    :goto_4b
    const/high16 v3, 0x40000000

    :goto_4c
    goto :goto_95

    nop

    :goto_4d
    goto :goto_4c

    :goto_4e
    goto :goto_4b

    nop

    :goto_4f
    iput-boolean v2, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mHasNavigatorSwitchView:Z

    :goto_50
    goto :goto_b1

    nop

    :goto_51
    iget-object v11, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mStartView:Landroid/view/View;

    goto :goto_e

    nop

    :goto_52
    iget-object v7, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mListNavLayout:Landroid/widget/LinearLayout;

    goto :goto_140

    nop

    :goto_53
    invoke-virtual {v0, v3}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;

    move-result-object v6

    goto :goto_a8

    nop

    :goto_54
    if-nez v2, :cond_9

    goto :goto_90

    :cond_9
    goto :goto_18

    nop

    :goto_55
    invoke-static {v1, v5}, Ljava/lang/Math;->max(II)I

    move-result v1

    goto :goto_14e

    nop

    :goto_56
    goto :goto_1a5

    :goto_57
    goto :goto_45

    nop

    :goto_58
    iget-object v3, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    goto :goto_194

    nop

    :goto_59
    iget-object v11, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mTitleUpView:Landroid/view/View;

    goto :goto_146

    nop

    :goto_5a
    const/high16 v11, 0x40000000

    goto :goto_174

    nop

    :goto_5b
    invoke-virtual {v2, v3, v12}, Landroid/widget/FrameLayout;->measure(II)V

    goto :goto_e9

    nop

    :goto_5c
    if-ne v2, v11, :cond_a

    goto :goto_281

    :cond_a
    goto :goto_b7

    nop

    :goto_5d
    add-float/2addr v2, v3

    goto :goto_8f

    nop

    :goto_5e
    move/from16 v5, v21

    goto :goto_9e

    nop

    :goto_5f
    if-nez v11, :cond_b

    goto :goto_ec

    :cond_b
    goto :goto_eb

    nop

    :goto_60
    add-int/2addr v9, v10

    goto :goto_79

    nop

    :goto_61
    invoke-virtual {v11, v5}, Landroid/view/View;->getTag(I)Ljava/lang/Object;

    move-result-object v5

    goto :goto_8e

    nop

    :goto_62
    invoke-virtual {v8}, Lmiuix/container/ExtraPaddingPolicy;->getExtraPaddingDp()I

    move-result v8

    goto :goto_9f

    nop

    :goto_63
    goto :goto_1c7

    :goto_64
    goto :goto_df

    nop

    :goto_65
    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mEndMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    goto :goto_1c5

    nop

    :goto_66
    if-nez v22, :cond_c

    goto :goto_104

    :cond_c
    goto :goto_fa

    nop

    :goto_67
    iget-object v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mProgressView:Landroid/widget/ProgressBar;

    goto :goto_e4

    nop

    :goto_68
    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mIndeterminateProgressView:Landroid/widget/ProgressBar;

    goto :goto_d

    nop

    :goto_69
    move v2, v6

    :goto_6a
    goto :goto_58

    nop

    :goto_6b
    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mNavigatorSwitch:Landroid/view/View;

    goto :goto_211

    nop

    :goto_6c
    const/4 v8, 0x1

    goto :goto_26a

    nop

    :goto_6d
    move/from16 v19, v7

    goto :goto_15b

    nop

    :goto_6e
    add-int/2addr v5, v7

    goto :goto_0

    nop

    :goto_6f
    const/4 v7, 0x0

    :goto_70
    goto :goto_92

    nop

    :goto_71
    iget v8, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mUncollapseTabPaddingH:I

    goto :goto_ff

    nop

    :goto_72
    if-nez v8, :cond_d

    goto :goto_246

    :cond_d
    goto :goto_260

    nop

    :goto_73
    goto :goto_6a

    :goto_74
    goto :goto_69

    nop

    :goto_75
    invoke-virtual {v5}, Landroid/view/View;->getMeasuredWidth()I

    move-result v5

    goto :goto_1e7

    nop

    :goto_76
    iput v7, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableSecondaryTabHeight:I

    goto :goto_b2

    nop

    :goto_77
    invoke-virtual {v5}, Landroid/widget/LinearLayout;->getVisibility()I

    move-result v5

    goto :goto_a9

    nop

    :goto_78
    invoke-virtual {v7}, Landroid/view/View;->getMeasuredWidth()I

    move-result v7

    goto :goto_183

    nop

    :goto_79
    mul-int/lit8 v9, v9, 0x2

    goto :goto_1bc

    nop

    :goto_7a
    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExpandedHomeLayout:Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;

    goto :goto_f0

    nop

    :goto_7b
    const/4 v1, 0x1

    goto :goto_fd

    nop

    :goto_7c
    invoke-virtual {v11}, Landroid/view/View;->getVisibility()I

    move-result v11

    goto :goto_200

    nop

    :goto_7d
    invoke-virtual {v5}, Landroid/widget/LinearLayout;->getParent()Landroid/view/ViewParent;

    move-result-object v5

    goto :goto_1fa

    nop

    :goto_7e
    if-nez v5, :cond_e

    goto :goto_1b4

    :cond_e
    goto :goto_c2

    nop

    :goto_7f
    if-eq v1, v11, :cond_f

    goto :goto_1b2

    :cond_f
    goto :goto_1fb

    nop

    :goto_80
    mul-int/lit8 v5, v5, 0x2

    goto :goto_185

    nop

    :goto_81
    invoke-virtual {v0, v2, v13, v12, v4}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->measureChildView(Landroid/view/View;III)I

    move-result v2

    goto :goto_1c2

    nop

    :goto_82
    iget-object v3, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseTabContainer:Landroid/widget/FrameLayout;

    goto :goto_c0

    nop

    :goto_83
    invoke-virtual {v1, v2, v0}, Landroid/widget/ProgressBar;->measure(II)V

    :goto_84
    goto :goto_22

    nop

    :goto_85
    goto :goto_bc

    :goto_86
    goto :goto_237

    nop

    :goto_87
    const/4 v11, 0x0

    goto :goto_16e

    nop

    :goto_88
    const/high16 v10, 0x40000000

    goto :goto_9d

    nop

    :goto_89
    if-ne v7, v5, :cond_10

    goto :goto_191

    :cond_10
    goto :goto_23

    nop

    :goto_8a
    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mIndeterminateProgressView:Landroid/widget/ProgressBar;

    goto :goto_1f3

    nop

    :goto_8b
    invoke-static {v4, v3}, Ljava/lang/Math;->min(II)I

    move-result v3

    goto :goto_22d

    nop

    :goto_8c
    if-nez v5, :cond_11

    goto :goto_225

    :cond_11
    goto :goto_224

    nop

    :goto_8d
    invoke-virtual {v3, v8, v9}, Landroid/widget/FrameLayout;->measure(II)V

    goto :goto_249

    nop

    :goto_8e
    check-cast v5, Lmiuix/appcompat/internal/app/NavigatorSwitchPresenter;

    goto :goto_f6

    nop

    :goto_8f
    float-to-int v3, v2

    :goto_90
    goto :goto_107

    nop

    :goto_91
    iget-object v2, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseTabs:Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView;

    goto :goto_1a

    nop

    :goto_92
    invoke-virtual {v1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v11

    goto :goto_150

    nop

    :goto_93
    move v4, v3

    :goto_94
    goto :goto_168

    nop

    :goto_95
    iget-object v4, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    goto :goto_5e

    nop

    :goto_96
    move/from16 v21, v3

    goto :goto_2f

    nop

    :goto_97
    const/high16 v15, 0x40000000

    goto :goto_a6

    nop

    :goto_98
    goto :goto_1c3

    :goto_99
    goto :goto_149

    nop

    :goto_9a
    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mNavigatorSwitch:Landroid/view/View;

    goto :goto_1a3

    nop

    :goto_9b
    if-nez v5, :cond_12

    goto :goto_50

    :cond_12
    goto :goto_4f

    nop

    :goto_9c
    iget v4, v5, Landroidx/appcompat/app/ActionBar$LayoutParams;->gravity:I

    goto :goto_20f

    nop

    :goto_9d
    invoke-static {v3, v10}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v2

    goto :goto_1af

    nop

    :goto_9e
    const/high16 v7, -0x80000000

    goto :goto_112

    nop

    :goto_9f
    int-to-float v8, v8

    goto :goto_144

    nop

    :goto_a0
    add-int/2addr v9, v5

    goto :goto_19b

    nop

    :goto_a1
    if-eq v7, v11, :cond_13

    goto :goto_184

    :cond_13
    goto :goto_19d

    nop

    :goto_a2
    invoke-static {v1, v5}, Ljava/lang/Math;->max(II)I

    move-result v1

    :goto_a3
    goto :goto_37

    nop

    :goto_a4
    const/16 v16, 0x2

    :goto_a5
    goto :goto_1ec

    nop

    :goto_a6
    goto :goto_269

    :goto_a7
    goto :goto_268

    nop

    :goto_a8
    invoke-virtual {v6}, Landroid/view/View;->getVisibility()I

    move-result v7

    goto :goto_89

    nop

    :goto_a9
    const/16 v11, 0x8

    goto :goto_1f0

    nop

    :goto_aa
    sub-int v10, v10, v20

    :goto_ab
    goto :goto_d6

    nop

    :goto_ac
    invoke-virtual {v1}, Landroid/view/View;->getMeasuredHeight()I

    move-result v1

    goto :goto_24c

    nop

    :goto_ad
    iget-object v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mStartView:Landroid/view/View;

    goto :goto_173

    nop

    :goto_ae
    iget-object v8, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExtraPaddingPolicy:Lmiuix/container/ExtraPaddingPolicy;

    goto :goto_62

    nop

    :goto_af
    if-nez v8, :cond_14

    goto :goto_246

    :cond_14
    goto :goto_ae

    nop

    :goto_b0
    const/high16 v11, -0x80000000

    goto :goto_151

    nop

    :goto_b1
    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExpandedActionView:Landroid/view/View;

    goto :goto_d4

    nop

    :goto_b2
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getResources()Landroid/content/res/Resources;

    move-result-object v7

    goto :goto_229

    nop

    :goto_b3
    if-lez v4, :cond_15

    goto :goto_57

    :cond_15
    goto :goto_2b

    nop

    :goto_b4
    add-int/2addr v2, v11

    goto :goto_ea

    nop

    :goto_b5
    iget-boolean v11, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mHasNavigatorSwitchView:Z

    goto :goto_5f

    nop

    :goto_b6
    if-eqz v2, :cond_16

    goto :goto_90

    :cond_16
    goto :goto_17

    nop

    :goto_b7
    invoke-virtual {v5}, Landroid/widget/FrameLayout;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v2

    goto :goto_261

    nop

    :goto_b8
    sub-int v13, v3, v8

    goto :goto_26c

    nop

    :goto_b9
    if-ne v7, v11, :cond_17

    goto :goto_34

    :cond_17
    goto :goto_23d

    nop

    :goto_ba
    invoke-virtual {v4}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result v4

    goto :goto_1d6

    nop

    :goto_bb
    invoke-static {v1, v5}, Ljava/lang/Math;->max(II)I

    :goto_bc
    goto :goto_1f1

    nop

    :goto_bd
    invoke-static {v10, v7}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v3

    goto :goto_170

    nop

    :goto_be
    iput-boolean v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mIsCollapsed:Z

    goto :goto_d1

    nop

    :goto_bf
    invoke-virtual {v0, v11, v13, v12, v2}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->measureChildView(Landroid/view/View;III)I

    move-result v13

    goto :goto_101

    nop

    :goto_c0
    invoke-static {v9, v10}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v8

    goto :goto_ef

    nop

    :goto_c1
    and-int/lit8 v1, v1, 0x10

    goto :goto_1c9

    nop

    :goto_c2
    invoke-virtual {v5}, Landroid/view/View;->getVisibility()I

    move-result v5

    goto :goto_30

    nop

    :goto_c3
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getPaddingEnd()I

    move-result v9

    goto :goto_9

    nop

    :goto_c4
    iget-object v7, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExpandedActionView:Landroid/view/View;

    goto :goto_1f5

    nop

    :goto_c5
    invoke-static {v8, v10}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v8

    goto :goto_228

    nop

    :goto_c6
    mul-int/lit8 v8, v8, 0x2

    goto :goto_274

    nop

    :goto_c7
    invoke-virtual {v1}, Landroid/view/View;->getMeasuredHeight()I

    move-result v1

    goto :goto_1bb

    nop

    :goto_c8
    invoke-static {v3, v5}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v3

    goto :goto_5b

    nop

    :goto_c9
    move/from16 v18, v5

    goto :goto_161

    nop

    :goto_ca
    add-int v8, v2, v3

    goto :goto_1bf

    nop

    :goto_cb
    move v4, v7

    :goto_cc
    goto :goto_242

    nop

    :goto_cd
    const/4 v3, 0x0

    :goto_ce
    goto :goto_c4

    nop

    :goto_cf
    sub-float/2addr v5, v4

    goto :goto_17d

    nop

    :goto_d0
    const/16 v16, 0x2

    goto :goto_1f4

    nop

    :goto_d1
    return-void

    :goto_d2
    goto :goto_fe

    nop

    :goto_d3
    iget v7, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mNavigationMode:I

    goto :goto_6c

    nop

    :goto_d4
    if-nez v5, :cond_18

    goto :goto_f1

    :cond_18
    goto :goto_7a

    nop

    :goto_d5
    if-nez v17, :cond_19

    goto :goto_227

    :cond_19
    goto :goto_226

    nop

    :goto_d6
    iget v4, v11, Landroid/view/ViewGroup$LayoutParams;->width:I

    goto :goto_24

    nop

    :goto_d7
    invoke-virtual {v0, v2, v2}, Landroid/view/ViewGroup;->setMeasuredDimension(II)V

    goto :goto_be

    nop

    :goto_d8
    iget-object v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mStartView:Landroid/view/View;

    goto :goto_28c

    nop

    :goto_d9
    invoke-virtual {v5}, Landroid/widget/LinearLayout;->getMeasuredHeight()I

    move-result v5

    goto :goto_6e

    nop

    :goto_da
    if-nez v3, :cond_1a

    goto :goto_42

    :cond_1a
    goto :goto_23c

    nop

    :goto_db
    invoke-virtual {v0, v2, v13, v12, v11}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->measureChildView(Landroid/view/View;III)I

    goto :goto_1b9

    nop

    :goto_dc
    goto :goto_252

    :goto_dd
    goto :goto_251

    nop

    :goto_de
    sub-int/2addr v13, v2

    goto :goto_98

    nop

    :goto_df
    if-eq v2, v8, :cond_1b

    goto :goto_f9

    :cond_1b
    goto :goto_253

    nop

    :goto_e0
    invoke-virtual {v4}, Landroid/view/View;->getAlpha()F

    move-result v4

    goto :goto_1d5

    nop

    :goto_e1
    goto :goto_21f

    :goto_e2
    goto :goto_201

    nop

    :goto_e3
    move/from16 v20, v7

    goto :goto_13d

    nop

    :goto_e4
    if-nez v1, :cond_1c

    goto :goto_84

    :cond_1c
    goto :goto_e5

    nop

    :goto_e5
    invoke-virtual {v1}, Landroid/widget/ProgressBar;->getVisibility()I

    move-result v1

    goto :goto_131

    nop

    :goto_e6
    invoke-static/range {p2 .. p2}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v10

    :goto_e7
    goto :goto_1e6

    nop

    :goto_e8
    if-nez v11, :cond_1d

    goto :goto_267

    :cond_1d
    goto :goto_266

    nop

    :goto_e9
    iget-object v2, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMainContainer:Landroid/widget/FrameLayout;

    goto :goto_27c

    nop

    :goto_ea
    sub-int/2addr v13, v2

    goto :goto_1a2

    nop

    :goto_eb
    goto :goto_e2

    :goto_ec
    goto :goto_c9

    nop

    :goto_ed
    const/4 v11, 0x0

    goto :goto_258

    nop

    :goto_ee
    invoke-virtual {v5}, Landroid/widget/FrameLayout;->getMeasuredWidth()I

    move-result v2

    goto :goto_1cd

    nop

    :goto_ef
    invoke-static {v7, v7}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v9

    goto :goto_8d

    nop

    :goto_f0
    goto :goto_233

    :goto_f1
    goto :goto_232

    nop

    :goto_f2
    goto :goto_175

    :goto_f3
    goto :goto_5a

    nop

    :goto_f4
    invoke-virtual {v1}, Landroid/view/View;->getVisibility()I

    move-result v1

    goto :goto_16a

    nop

    :goto_f5
    if-nez v5, :cond_1e

    goto :goto_287

    :cond_1e
    goto :goto_1d

    nop

    :goto_f6
    invoke-virtual {v5, v2, v2}, Lmiuix/appcompat/internal/app/NavigatorSwitchPresenter;->suppressVisibility(ZI)V

    goto :goto_6b

    nop

    :goto_f7
    if-lt v3, v1, :cond_1f

    goto :goto_273

    :cond_1f
    goto :goto_53

    nop

    :goto_f8
    goto :goto_1c7

    :goto_f9
    goto :goto_235

    nop

    :goto_fa
    iget-object v7, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    goto :goto_24e

    nop

    :goto_fb
    int-to-float v3, v3

    goto :goto_128

    nop

    :goto_fc
    iget v7, v7, Landroid/content/res/Configuration;->densityDpi:I

    goto :goto_1f

    nop

    :goto_fd
    if-eqz v4, :cond_20

    goto :goto_d2

    :cond_20
    goto :goto_d7

    nop

    :goto_fe
    iput-boolean v2, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mIsCollapsed:Z

    goto :goto_15c

    nop

    :goto_ff
    iget v9, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExtraPadding:I

    goto :goto_1bd

    nop

    :goto_100
    if-nez v11, :cond_21

    goto :goto_1d9

    :cond_21
    goto :goto_87

    nop

    :goto_101
    iget-object v11, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mEndView:Landroid/view/View;

    goto :goto_205

    nop

    :goto_102
    iget-boolean v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mHasStartView:Z

    goto :goto_1b7

    nop

    :goto_103
    goto :goto_1fd

    :goto_104
    goto :goto_1fc

    nop

    :goto_105
    if-nez v1, :cond_22

    goto :goto_117

    :cond_22
    goto :goto_116

    nop

    :goto_106
    invoke-virtual {v1}, Landroid/view/View;->getVisibility()I

    move-result v7

    goto :goto_b9

    nop

    :goto_107
    invoke-static {v3, v15}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v2

    goto :goto_bd

    nop

    :goto_108
    const/4 v7, 0x0

    goto :goto_245

    nop

    :goto_109
    iput v3, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseSecondaryTabHeight:I

    goto :goto_133

    nop

    :goto_10a
    invoke-virtual {v1}, Landroid/widget/HorizontalScrollView;->getMeasuredHeight()I

    move-result v1

    goto :goto_1ea

    nop

    :goto_10b
    move v10, v4

    goto :goto_10e

    nop

    :goto_10c
    sub-int v3, v5, v2

    goto :goto_88

    nop

    :goto_10d
    iget-object v8, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExtraPaddingPolicy:Lmiuix/container/ExtraPaddingPolicy;

    goto :goto_72

    nop

    :goto_10e
    goto :goto_e7

    :goto_10f
    goto :goto_e6

    nop

    :goto_110
    if-eq v4, v5, :cond_23

    goto :goto_11d

    :cond_23
    goto :goto_152

    nop

    :goto_111
    invoke-static {v6, v4}, Ljava/lang/Math;->max(II)I

    move-result v10

    goto :goto_230

    nop

    :goto_112
    invoke-static {v5, v7}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v8

    goto :goto_121

    nop

    :goto_113
    iget-object v3, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mNavigatorSwitch:Landroid/view/View;

    goto :goto_137

    nop

    :goto_114
    sub-int v3, v3, v19

    goto :goto_6

    nop

    :goto_115
    add-int/2addr v5, v7

    goto :goto_3c

    nop

    :goto_116
    goto :goto_17b

    :goto_117
    goto :goto_17a

    nop

    :goto_118
    invoke-static {v2, v14}, Ljava/lang/Math;->min(II)I

    move-result v2

    goto :goto_11c

    nop

    :goto_119
    move/from16 v21, v10

    goto :goto_56

    nop

    :goto_11a
    const/4 v11, 0x1

    goto :goto_1b1

    nop

    :goto_11b
    invoke-static {v1, v2}, Ljava/lang/Math;->max(II)I

    move-result v1

    goto :goto_244

    nop

    :goto_11c
    mul-int/lit8 v3, v2, 0x2

    :goto_11d
    goto :goto_182

    nop

    :goto_11e
    invoke-static {v6, v2}, Ljava/lang/Math;->max(II)I

    move-result v2

    goto :goto_73

    nop

    :goto_11f
    invoke-virtual {v4, v8, v14}, Landroid/widget/FrameLayout;->measure(II)V

    goto :goto_1e2

    nop

    :goto_120
    add-int/2addr v8, v5

    goto :goto_1e3

    nop

    :goto_121
    const/4 v7, 0x0

    goto :goto_21

    nop

    :goto_122
    invoke-static {v11, v14}, Ljava/lang/Math;->max(II)I

    move-result v14

    goto :goto_172

    nop

    :goto_123
    goto :goto_cc

    :goto_124
    goto :goto_221

    nop

    :goto_125
    iget v4, v0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mTitleMaxHeight:I

    goto :goto_12e

    nop

    :goto_126
    invoke-virtual {v1, v11}, Landroid/view/View;->setVisibility(I)V

    :goto_127
    goto :goto_243

    nop

    :goto_128
    iget-object v4, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mNavigatorSwitch:Landroid/view/View;

    goto :goto_e0

    nop

    :goto_129
    add-int v7, v20, v7

    goto :goto_282

    nop

    :goto_12a
    invoke-static {v7, v13}, Ljava/lang/Math;->max(II)I

    move-result v8

    goto :goto_52

    nop

    :goto_12b
    move v3, v13

    :goto_12c
    goto :goto_26f

    nop

    :goto_12d
    mul-int/lit8 v11, v11, 0x2

    goto :goto_157

    nop

    :goto_12e
    iget v6, v0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mTitleMinHeight:I

    goto :goto_193

    nop

    :goto_12f
    move/from16 v18, v5

    goto :goto_263

    nop

    :goto_130
    if-nez v4, :cond_24

    goto :goto_124

    :cond_24
    goto :goto_13c

    nop

    :goto_131
    const/16 v11, 0x8

    goto :goto_1b5

    nop

    :goto_132
    iget-object v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mStartView:Landroid/view/View;

    goto :goto_1b6

    nop

    :goto_133
    goto :goto_ce

    :goto_134
    goto :goto_cd

    nop

    :goto_135
    sget v5, Lmiuix/appcompat/R$id;->miuix_appcompat_navigator_switch_presenter:I

    goto :goto_61

    nop

    :goto_136
    iget v10, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExtraPadding:I

    goto :goto_60

    nop

    :goto_137
    invoke-virtual {v3}, Landroid/view/View;->getMeasuredWidth()I

    move-result v3

    goto :goto_fb

    nop

    :goto_138
    const/4 v11, 0x0

    goto :goto_db

    nop

    :goto_139
    invoke-virtual {v0, v5, v1}, Landroid/view/ViewGroup;->setMeasuredDimension(II)V

    goto :goto_63

    nop

    :goto_13a
    iget-object v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mProgressView:Landroid/widget/ProgressBar;

    goto :goto_256

    nop

    :goto_13b
    iput v7, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExtraPadding:I

    goto :goto_108

    nop

    :goto_13c
    iget-object v4, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableTabContainer:Landroid/widget/FrameLayout;

    goto :goto_19c

    nop

    :goto_13d
    iget v7, v5, Landroid/view/ViewGroup$MarginLayoutParams;->bottomMargin:I

    goto :goto_129

    nop

    :goto_13e
    invoke-virtual {v5}, Landroid/widget/LinearLayout;->getMeasuredWidth()I

    move-result v5

    goto :goto_a0

    nop

    :goto_13f
    iput v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExpandTotalHeight:I

    goto :goto_100

    nop

    :goto_140
    const/high16 v9, -0x80000000

    goto :goto_1da

    nop

    :goto_141
    add-int/2addr v9, v5

    goto :goto_1e

    nop

    :goto_142
    mul-float/2addr v4, v5

    goto :goto_26b

    nop

    :goto_143
    iget-object v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCustomNavView:Landroid/view/View;

    goto :goto_105

    nop

    :goto_144
    mul-float/2addr v8, v7

    goto :goto_17c

    nop

    :goto_145
    invoke-virtual {v5}, Landroid/view/View;->getVisibility()I

    move-result v5

    goto :goto_9b

    nop

    :goto_146
    move/from16 v17, v5

    goto :goto_102

    nop

    :goto_147
    if-nez v7, :cond_25

    goto :goto_184

    :cond_25
    goto :goto_291

    nop

    :goto_148
    if-nez v3, :cond_26

    goto :goto_134

    :cond_26
    goto :goto_82

    nop

    :goto_149
    const/4 v4, 0x0

    goto :goto_1eb

    nop

    :goto_14a
    iget v2, v0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mInnerExpandState:I

    goto :goto_19e

    nop

    :goto_14b
    move v1, v6

    goto :goto_25e

    nop

    :goto_14c
    iget v4, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mTitleUpViewMarginStart:I

    goto :goto_1d1

    nop

    :goto_14d
    add-int/2addr v5, v7

    goto :goto_a2

    nop

    :goto_14e
    goto :goto_a5

    :goto_14f
    goto :goto_a4

    nop

    :goto_150
    invoke-virtual {v0, v11}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->generateLayoutParams(Landroid/view/ViewGroup$LayoutParams;)Landroid/view/ViewGroup$LayoutParams;

    move-result-object v11

    goto :goto_270

    nop

    :goto_151
    invoke-static {v13, v11}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v2

    goto :goto_f2

    nop

    :goto_152
    iget v4, v11, Landroid/view/ViewGroup$LayoutParams;->width:I

    goto :goto_257

    nop

    :goto_153
    goto :goto_127

    :goto_154
    goto :goto_289

    nop

    :goto_155
    if-nez v5, :cond_27

    goto :goto_210

    :cond_27
    goto :goto_9c

    nop

    :goto_156
    add-int/lit8 v3, v3, 0x1

    goto :goto_272

    nop

    :goto_157
    invoke-virtual {v0, v5, v13, v12, v11}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->measureChildView(Landroid/view/View;III)I

    move-result v13

    goto :goto_248

    nop

    :goto_158
    if-nez v11, :cond_28

    goto :goto_a3

    :cond_28
    goto :goto_135

    nop

    :goto_159
    if-ltz v2, :cond_29

    goto :goto_f3

    :cond_29
    goto :goto_b0

    nop

    :goto_15a
    if-eqz v11, :cond_2a

    goto :goto_267

    :cond_2a
    goto :goto_265

    nop

    :goto_15b
    iget v7, v5, Landroid/view/ViewGroup$MarginLayoutParams;->topMargin:I

    goto :goto_e3

    nop

    :goto_15c
    invoke-static/range {p1 .. p1}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v3

    goto :goto_125

    nop

    :goto_15d
    move-object/from16 v0, p0

    goto :goto_3e

    nop

    :goto_15e
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getPaddingBottom()I

    move-result v8

    goto :goto_4a

    nop

    :goto_15f
    invoke-virtual {v5}, Landroid/widget/ProgressBar;->getMeasuredHeight()I

    move-result v5

    goto :goto_27a

    nop

    :goto_160
    move v3, v2

    goto :goto_93

    nop

    :goto_161
    const/4 v5, 0x0

    goto :goto_e1

    nop

    :goto_162
    add-int v3, v13, v18

    :goto_163
    goto :goto_114

    nop

    :goto_164
    move/from16 v5, v21

    goto :goto_275

    nop

    :goto_165
    iget v7, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mItemPadding:I

    goto :goto_d5

    nop

    :goto_166
    const/4 v8, 0x1

    goto :goto_14a

    nop

    :goto_167
    const/4 v7, 0x0

    goto :goto_4

    nop

    :goto_168
    const/16 v5, 0x8

    goto :goto_f7

    nop

    :goto_169
    const v5, 0x800007

    goto :goto_176

    nop

    :goto_16a
    const/16 v11, 0x8

    goto :goto_7f

    nop

    :goto_16b
    invoke-virtual {v5}, Landroid/view/View;->getMeasuredHeight()I

    move-result v5

    goto :goto_14d

    nop

    :goto_16c
    move/from16 v10, v21

    :goto_16d
    goto :goto_aa

    nop

    :goto_16e
    invoke-virtual {v0, v5, v11}, Landroid/view/ViewGroup;->setMeasuredDimension(II)V

    goto :goto_1ac

    nop

    :goto_16f
    const/high16 v11, -0x80000000

    goto :goto_44

    nop

    :goto_170
    invoke-virtual {v1, v2, v3}, Landroid/view/View;->measure(II)V

    goto :goto_27f

    nop

    :goto_171
    sub-int v2, v13, v16

    goto :goto_7

    nop

    :goto_172
    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mEndMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    goto :goto_13e

    nop

    :goto_173
    invoke-virtual {v1}, Landroid/view/View;->getMeasuredWidth()I

    move-result v1

    goto :goto_1e1

    nop

    :goto_174
    invoke-static {v2, v11}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v2

    :goto_175
    goto :goto_2d

    nop

    :goto_176
    and-int/2addr v4, v5

    goto :goto_1c1

    nop

    :goto_177
    add-int v5, v18, v5

    :goto_178
    goto :goto_46

    nop

    :goto_179
    if-eq v10, v15, :cond_2b

    goto :goto_231

    :cond_2b
    goto :goto_111

    nop

    :goto_17a
    const/4 v1, 0x0

    :goto_17b
    goto :goto_26d

    nop

    :goto_17c
    float-to-int v7, v8

    goto :goto_13b

    nop

    :goto_17d
    mul-float/2addr v3, v5

    goto :goto_14c

    nop

    :goto_17e
    invoke-static {v7, v8}, Ljava/lang/Math;->max(II)I

    move-result v8

    goto :goto_1b0

    nop

    :goto_17f
    add-int/2addr v1, v4

    goto :goto_13f

    nop

    :goto_180
    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mEndMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    goto :goto_ed

    nop

    :goto_181
    invoke-static {v2, v1}, Ljava/lang/Math;->max(II)I

    move-result v1

    goto :goto_139

    nop

    :goto_182
    iget-object v2, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mNavigatorSwitch:Landroid/view/View;

    goto :goto_54

    nop

    :goto_183
    goto :goto_70

    :goto_184
    goto :goto_6f

    nop

    :goto_185
    sub-int/2addr v14, v5

    goto :goto_29

    nop

    :goto_186
    if-ne v5, v11, :cond_2c

    goto :goto_a3

    :cond_2c
    goto :goto_3

    nop

    :goto_187
    goto :goto_18c

    :goto_188
    goto :goto_c

    nop

    :goto_189
    invoke-static {v4, v3}, Ljava/lang/Math;->max(II)I

    move-result v3

    goto :goto_155

    nop

    :goto_18a
    if-ne v1, v5, :cond_2d

    goto :goto_dd

    :cond_2d
    goto :goto_d8

    nop

    :goto_18b
    invoke-virtual {v7, v8, v12}, Landroid/widget/LinearLayout;->measure(II)V

    :goto_18c
    goto :goto_66

    nop

    :goto_18d
    if-ne v4, v15, :cond_2e

    goto :goto_a7

    :cond_2e
    goto :goto_97

    nop

    :goto_18e
    const/16 v11, 0x8

    goto :goto_186

    nop

    :goto_18f
    invoke-static {v6, v8}, Ljava/lang/Math;->max(II)I

    move-result v6

    goto :goto_290

    nop

    :goto_190
    add-int/lit8 v4, v4, 0x1

    :goto_191
    goto :goto_156

    nop

    :goto_192
    iget v7, v5, Landroid/view/ViewGroup$MarginLayoutParams;->rightMargin:I

    goto :goto_31

    nop

    :goto_193
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getPaddingTop()I

    move-result v7

    goto :goto_15e

    nop

    :goto_194
    invoke-virtual {v3}, Landroid/widget/FrameLayout;->getChildCount()I

    move-result v3

    goto :goto_da

    nop

    :goto_195
    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mNavigatorSwitch:Landroid/view/View;

    goto :goto_1aa

    nop

    :goto_196
    add-int/2addr v8, v5

    goto :goto_20a

    nop

    :goto_197
    invoke-virtual {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->getDisplayOptions()I

    move-result v11

    goto :goto_23b

    nop

    :goto_198
    add-int v8, v8, v16

    goto :goto_20b

    nop

    :goto_199
    const/16 v11, 0x8

    :goto_19a
    goto :goto_22a

    nop

    :goto_19b
    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mEndMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    goto :goto_d9

    nop

    :goto_19c
    const/high16 v10, 0x40000000

    goto :goto_c5

    nop

    :goto_19d
    iget-object v7, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mTitleUpView:Landroid/view/View;

    goto :goto_78

    nop

    :goto_19e
    move/from16 v4, v16

    goto :goto_1f9

    nop

    :goto_19f
    const/16 v11, 0x8

    goto :goto_153

    nop

    :goto_1a0
    if-eqz v11, :cond_2f

    goto :goto_e2

    :cond_2f
    goto :goto_b5

    nop

    :goto_1a1
    if-nez v1, :cond_30

    goto :goto_1b2

    :cond_30
    goto :goto_f4

    nop

    :goto_1a2
    const/4 v11, 0x0

    goto :goto_1d2

    nop

    :goto_1a3
    invoke-virtual {v5}, Landroid/view/View;->getMeasuredWidth()I

    move-result v5

    goto :goto_196

    nop

    :goto_1a4
    goto :goto_24b

    :goto_1a5
    goto :goto_1e5

    nop

    :goto_1a6
    iget v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseTotalHeight:I

    goto :goto_212

    nop

    :goto_1a7
    add-int/2addr v2, v3

    goto :goto_181

    nop

    :goto_1a8
    if-nez v5, :cond_31

    goto :goto_191

    :cond_31
    :goto_1a9
    goto :goto_190

    nop

    :goto_1aa
    invoke-virtual {v5}, Landroid/view/View;->getAlpha()F

    move-result v5

    goto :goto_142

    nop

    :goto_1ab
    invoke-virtual {v2}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result v2

    goto :goto_11e

    nop

    :goto_1ac
    const/4 v8, 0x1

    goto :goto_1ff

    nop

    :goto_1ad
    invoke-virtual {v5}, Landroid/widget/FrameLayout;->getVisibility()I

    move-result v2

    goto :goto_5c

    nop

    :goto_1ae
    sub-int v13, v13, v19

    goto :goto_ac

    nop

    :goto_1af
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getMeasuredHeight()I

    move-result v0

    goto :goto_3a

    nop

    :goto_1b0
    iget v9, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mUncollapseTabPaddingH:I

    goto :goto_136

    nop

    :goto_1b1
    goto :goto_25f

    :goto_1b2
    goto :goto_14b

    nop

    :goto_1b3
    iput-boolean v2, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mHasStartView:Z

    :goto_1b4
    goto :goto_b

    nop

    :goto_1b5
    if-ne v1, v11, :cond_32

    goto :goto_84

    :cond_32
    goto :goto_13a

    nop

    :goto_1b6
    if-nez v1, :cond_33

    goto :goto_dd

    :cond_33
    goto :goto_259

    nop

    :goto_1b7
    if-eqz v5, :cond_34

    goto :goto_15

    :cond_34
    goto :goto_1de

    nop

    :goto_1b8
    invoke-static {v4, v3}, Ljava/lang/Math;->max(II)I

    move-result v3

    goto :goto_206

    nop

    :goto_1b9
    iget-object v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseTabs:Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView;

    goto :goto_10a

    nop

    :goto_1ba
    const/16 v11, 0x8

    goto :goto_126

    nop

    :goto_1bb
    add-int/2addr v1, v7

    goto :goto_dc

    nop

    :goto_1bc
    sub-int v9, v5, v9

    goto :goto_130

    nop

    :goto_1bd
    add-int/2addr v8, v9

    goto :goto_c6

    nop

    :goto_1be
    mul-int/lit8 v8, v8, 0x2

    goto :goto_214

    nop

    :goto_1bf
    invoke-static {v1, v8}, Ljava/lang/Math;->max(II)I

    move-result v8

    goto :goto_223

    nop

    :goto_1c0
    const/4 v4, 0x0

    goto :goto_1b8

    nop

    :goto_1c1
    const/4 v5, 0x1

    goto :goto_110

    nop

    :goto_1c2
    move v13, v2

    :goto_1c3
    goto :goto_271

    nop

    :goto_1c4
    move/from16 v21, v3

    goto :goto_254

    nop

    :goto_1c5
    invoke-virtual {v5}, Landroid/widget/LinearLayout;->getMeasuredWidth()I

    move-result v5

    goto :goto_47

    nop

    :goto_1c6
    invoke-virtual {v0, v5, v1}, Landroid/view/ViewGroup;->setMeasuredDimension(II)V

    :goto_1c7
    goto :goto_67

    nop

    :goto_1c8
    if-nez v7, :cond_35

    goto :goto_18c

    :cond_35
    goto :goto_165

    nop

    :goto_1c9
    if-nez v1, :cond_36

    goto :goto_117

    :cond_36
    goto :goto_143

    nop

    :goto_1ca
    invoke-direct {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->updateTitleCenter()V

    :goto_1cb
    goto :goto_26e

    nop

    :goto_1cc
    invoke-virtual {v5, v11}, Landroid/widget/FrameLayout;->setVisibility(I)V

    goto :goto_286

    nop

    :goto_1cd
    invoke-virtual {v5}, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->getStartOffset()I

    move-result v11

    goto :goto_b4

    nop

    :goto_1ce
    goto :goto_154

    :goto_1cf
    goto :goto_19f

    nop

    :goto_1d0
    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mTitleUpView:Landroid/view/View;

    goto :goto_75

    nop

    :goto_1d1
    int-to-float v4, v4

    goto :goto_195

    nop

    :goto_1d2
    invoke-static {v11, v13}, Ljava/lang/Math;->max(II)I

    move-result v13

    goto :goto_1d3

    nop

    :goto_1d3
    move/from16 v16, v2

    goto :goto_171

    nop

    :goto_1d4
    add-int v19, v19, v2

    goto :goto_10

    nop

    :goto_1d5
    const/high16 v5, 0x3f800000

    goto :goto_cf

    nop

    :goto_1d6
    iput v4, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableSecondaryTabHeight:I

    goto :goto_123

    nop

    :goto_1d7
    if-gez v7, :cond_37

    goto :goto_2c

    :cond_37
    goto :goto_285

    nop

    :goto_1d8
    return-void

    :goto_1d9
    goto :goto_166

    nop

    :goto_1da
    invoke-static {v8, v9}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v8

    goto :goto_18b

    nop

    :goto_1db
    const/4 v7, 0x0

    goto :goto_292

    nop

    :goto_1dc
    if-ne v5, v11, :cond_38

    goto :goto_a5

    :cond_38
    goto :goto_247

    nop

    :goto_1dd
    const/16 v16, 0x2

    goto :goto_1dc

    nop

    :goto_1de
    iget-boolean v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mHasNavigatorSwitchView:Z

    goto :goto_8c

    nop

    :goto_1df
    iget v11, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mProgressBarPadding:I

    goto :goto_12d

    nop

    :goto_1e0
    if-gt v8, v9, :cond_39

    goto :goto_204

    :cond_39
    goto :goto_1be

    nop

    :goto_1e1
    add-int/2addr v8, v1

    goto :goto_32

    nop

    :goto_1e2
    iget-object v4, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableTabContainer:Landroid/widget/FrameLayout;

    goto :goto_ba

    nop

    :goto_1e3
    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mTitleUpView:Landroid/view/View;

    goto :goto_12

    nop

    :goto_1e4
    invoke-virtual {v11}, Landroid/view/View;->getVisibility()I

    move-result v11

    goto :goto_27

    nop

    :goto_1e5
    iget v10, v11, Landroid/view/ViewGroup$LayoutParams;->height:I

    goto :goto_222

    nop

    :goto_1e6
    sub-int/2addr v10, v7

    goto :goto_16f

    nop

    :goto_1e7
    iget-boolean v11, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mHasStartView:Z

    goto :goto_1a0

    nop

    :goto_1e8
    iget v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mTitleUpViewMarginEnd:I

    goto :goto_177

    nop

    :goto_1e9
    const/4 v5, 0x0

    goto :goto_14

    nop

    :goto_1ea
    invoke-static {v6, v1}, Ljava/lang/Math;->max(II)I

    move-result v1

    goto :goto_35

    nop

    :goto_1eb
    iget-object v2, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMainContainer:Landroid/widget/FrameLayout;

    goto :goto_81

    nop

    :goto_1ec
    invoke-direct {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->isShowTitle()Z

    move-result v5

    goto :goto_25b

    nop

    :goto_1ed
    if-nez v11, :cond_3a

    goto :goto_1ef

    :cond_3a
    goto :goto_1e4

    nop

    :goto_1ee
    invoke-static {v1, v11}, Ljava/lang/Math;->max(II)I

    move-result v1

    :goto_1ef
    goto :goto_27d

    nop

    :goto_1f0
    if-ne v5, v11, :cond_3b

    goto :goto_1

    :cond_3b
    goto :goto_180

    nop

    :goto_1f1
    iget-object v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExpandedActionView:Landroid/view/View;

    goto :goto_238

    nop

    :goto_1f2
    iget-object v11, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mEndView:Landroid/view/View;

    goto :goto_16

    nop

    :goto_1f3
    if-nez v5, :cond_3c

    goto :goto_14f

    :cond_3c
    goto :goto_23f

    nop

    :goto_1f4
    mul-int/lit8 v2, v2, 0x2

    goto :goto_10c

    nop

    :goto_1f5
    if-eqz v7, :cond_3d

    goto :goto_18c

    :cond_3d
    goto :goto_d3

    nop

    :goto_1f6
    iget v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mTitleUpViewMarginStart:I

    goto :goto_215

    nop

    :goto_1f7
    const/16 v11, 0x8

    goto :goto_1dd

    nop

    :goto_1f8
    iget v7, v11, Landroid/view/ViewGroup$LayoutParams;->height:I

    goto :goto_1d7

    nop

    :goto_1f9
    if-eq v2, v4, :cond_3e

    goto :goto_64

    :cond_3e
    goto :goto_1a6

    nop

    :goto_1fa
    if-eq v5, v0, :cond_3f

    goto :goto_1

    :cond_3f
    goto :goto_20e

    nop

    :goto_1fb
    if-eqz v17, :cond_40

    goto :goto_1b2

    :cond_40
    goto :goto_262

    nop

    :goto_1fc
    const/4 v7, 0x0

    :goto_1fd
    goto :goto_ca

    nop

    :goto_1fe
    iget v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mDisplayOptions:I

    goto :goto_c1

    nop

    :goto_1ff
    iput-boolean v8, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mIsCollapsed:Z

    goto :goto_1d8

    nop

    :goto_200
    if-eqz v11, :cond_41

    goto :goto_267

    :cond_41
    goto :goto_59

    nop

    :goto_201
    iget v11, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mTitleUpViewMarginStart:I

    goto :goto_12f

    nop

    :goto_202
    add-int/2addr v11, v7

    goto :goto_1ee

    nop

    :goto_203
    goto :goto_12c

    :goto_204
    goto :goto_12b

    nop

    :goto_205
    invoke-virtual {v11}, Landroid/view/View;->getMeasuredWidth()I

    move-result v11

    goto :goto_213

    nop

    :goto_206
    const/high16 v5, -0x80000000

    goto :goto_c8

    nop

    :goto_207
    invoke-virtual {v5}, Landroid/widget/ProgressBar;->getMeasuredWidth()I

    move-result v5

    goto :goto_23a

    nop

    :goto_208
    if-gez v4, :cond_42

    goto :goto_22e

    :cond_42
    goto :goto_96

    nop

    :goto_209
    const/4 v11, 0x4

    goto :goto_a1

    nop

    :goto_20a
    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mNavigatorSwitch:Landroid/view/View;

    goto :goto_16b

    nop

    :goto_20b
    invoke-virtual {v5}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result v5

    goto :goto_115

    nop

    :goto_20c
    if-nez v11, :cond_43

    goto :goto_267

    :cond_43
    goto :goto_7c

    nop

    :goto_20d
    move/from16 v18, v7

    goto :goto_21a

    nop

    :goto_20e
    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mEndMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    goto :goto_77

    nop

    :goto_20f
    goto :goto_21d

    :goto_210
    goto :goto_21c

    nop

    :goto_211
    invoke-virtual {v5}, Landroid/view/View;->getVisibility()I

    move-result v5

    goto :goto_18e

    nop

    :goto_212
    sub-int v2, v1, v3

    goto :goto_2a

    nop

    :goto_213
    add-int/2addr v9, v11

    goto :goto_1f2

    nop

    :goto_214
    sub-int v3, v21, v8

    goto :goto_203

    nop

    :goto_215
    move/from16 v18, v5

    goto :goto_1e8

    nop

    :goto_216
    invoke-virtual {v5}, Landroid/widget/LinearLayout;->getChildCount()I

    move-result v5

    goto :goto_1a8

    nop

    :goto_217
    const/4 v2, 0x0

    goto :goto_160

    nop

    :goto_218
    if-eqz v7, :cond_44

    goto :goto_154

    :cond_44
    goto :goto_28

    nop

    :goto_219
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getPaddingStart()I

    move-result v8

    goto :goto_c3

    nop

    :goto_21a
    if-nez v5, :cond_45

    goto :goto_283

    :cond_45
    goto :goto_20

    nop

    :goto_21b
    invoke-virtual {v0, v5, v13, v12, v2}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->measureChildView(Landroid/view/View;III)I

    move-result v13

    goto :goto_9a

    nop

    :goto_21c
    const v4, 0x800013

    :goto_21d
    goto :goto_169

    nop

    :goto_21e
    add-int/2addr v5, v11

    :goto_21f
    goto :goto_250

    nop

    :goto_220
    iget-object v2, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExpandedActionView:Landroid/view/View;

    goto :goto_49

    nop

    :goto_221
    const/high16 v10, 0x40000000

    goto :goto_cb

    nop

    :goto_222
    move/from16 v22, v15

    goto :goto_39

    nop

    :goto_223
    iput v8, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseTotalHeight:I

    goto :goto_18f

    nop

    :goto_224
    goto :goto_15

    :goto_225
    goto :goto_1e9

    nop

    :goto_226
    mul-int/lit8 v7, v7, 0x2

    :goto_227
    goto :goto_239

    nop

    :goto_228
    invoke-static {v7, v7}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v14

    goto :goto_11f

    nop

    :goto_229
    invoke-virtual {v7}, Landroid/content/res/Resources;->getConfiguration()Landroid/content/res/Configuration;

    move-result-object v7

    goto :goto_fc

    nop

    :goto_22a
    if-nez v5, :cond_46

    goto :goto_281

    :cond_46
    goto :goto_1ad

    nop

    :goto_22b
    const/4 v7, 0x0

    goto :goto_12a

    nop

    :goto_22c
    const/4 v3, 0x0

    goto :goto_4d

    nop

    :goto_22d
    goto :goto_163

    :goto_22e
    goto :goto_25c

    nop

    :goto_22f
    const/high16 v8, 0x43200000

    goto :goto_2e

    nop

    :goto_230
    goto :goto_16d

    :goto_231
    goto :goto_16c

    nop

    :goto_232
    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mHomeLayout:Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;

    :goto_233
    goto :goto_51

    nop

    :goto_234
    const/4 v11, 0x0

    goto :goto_33

    nop

    :goto_235
    iget v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseTotalHeight:I

    goto :goto_1c6

    nop

    :goto_236
    add-int/2addr v5, v7

    goto :goto_bb

    nop

    :goto_237
    iget-object v11, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mTitleUpView:Landroid/view/View;

    goto :goto_20c

    nop

    :goto_238
    if-nez v1, :cond_47

    goto :goto_241

    :cond_47
    goto :goto_240

    nop

    :goto_239
    sub-int/2addr v13, v7

    goto :goto_22b

    nop

    :goto_23a
    sub-int/2addr v14, v5

    goto :goto_38

    nop

    :goto_23b
    and-int/lit8 v11, v11, 0x20

    goto :goto_e8

    nop

    :goto_23c
    if-nez v22, :cond_48

    goto :goto_4e

    :cond_48
    goto :goto_22c

    nop

    :goto_23d
    iget-object v7, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mTitleUpView:Landroid/view/View;

    goto :goto_147

    nop

    :goto_23e
    invoke-virtual {v3}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result v3

    goto :goto_109

    nop

    :goto_23f
    invoke-virtual {v5}, Landroid/widget/ProgressBar;->getVisibility()I

    move-result v5

    goto :goto_1f7

    nop

    :goto_240
    goto :goto_17b

    :goto_241
    goto :goto_1fe

    nop

    :goto_242
    iput v7, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseSecondaryTabHeight:I

    goto :goto_148

    nop

    :goto_243
    if-nez v1, :cond_49

    goto :goto_34

    :cond_49
    goto :goto_106

    nop

    :goto_244
    add-int/2addr v1, v7

    goto :goto_17f

    nop

    :goto_245
    goto :goto_5

    :goto_246
    goto :goto_167

    nop

    :goto_247
    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mIndeterminateProgressView:Landroid/widget/ProgressBar;

    goto :goto_1df

    nop

    :goto_248
    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mIndeterminateProgressView:Landroid/widget/ProgressBar;

    goto :goto_207

    nop

    :goto_249
    iget-object v3, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseTabContainer:Landroid/widget/FrameLayout;

    goto :goto_23e

    nop

    :goto_24a
    const/high16 v7, -0x80000000

    :goto_24b
    goto :goto_119

    nop

    :goto_24c
    invoke-static {v6, v1}, Ljava/lang/Math;->max(II)I

    move-result v1

    :goto_24d
    goto :goto_234

    nop

    :goto_24e
    invoke-virtual {v7}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result v7

    goto :goto_103

    nop

    :goto_24f
    if-nez v5, :cond_4a

    goto :goto_50

    :cond_4a
    goto :goto_145

    nop

    :goto_250
    add-int v5, v18, v5

    goto :goto_120

    nop

    :goto_251
    move v1, v2

    :goto_252
    goto :goto_3f

    nop

    :goto_253
    invoke-virtual {v0, v5, v1}, Landroid/view/ViewGroup;->setMeasuredDimension(II)V

    goto :goto_f8

    nop

    :goto_254
    move/from16 v22, v15

    goto :goto_91

    nop

    :goto_255
    invoke-direct {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->shouldMeasureMovableTabContainer()Z

    move-result v4

    goto :goto_76

    nop

    :goto_256
    iget v2, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mProgressBarPadding:I

    goto :goto_d0

    nop

    :goto_257
    const/4 v5, -0x1

    goto :goto_48

    nop

    :goto_258
    invoke-virtual {v0, v5, v13, v12, v11}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->measureChildView(Landroid/view/View;III)I

    move-result v13

    goto :goto_65

    nop

    :goto_259
    invoke-virtual {v1}, Landroid/view/View;->getVisibility()I

    move-result v1

    goto :goto_18a

    nop

    :goto_25a
    invoke-virtual {v4, v8, v3}, Landroid/widget/FrameLayout;->measure(II)V

    goto :goto_41

    nop

    :goto_25b
    if-nez v5, :cond_4b

    goto :goto_1cb

    :cond_4b
    goto :goto_1ca

    nop

    :goto_25c
    move/from16 v21, v3

    goto :goto_162

    nop

    :goto_25d
    if-gez v10, :cond_4c

    goto :goto_26

    :cond_4c
    goto :goto_288

    nop

    :goto_25e
    goto :goto_24d

    :goto_25f
    goto :goto_220

    nop

    :goto_260
    invoke-virtual {v8}, Lmiuix/container/ExtraPaddingPolicy;->isEnable()Z

    move-result v8

    goto :goto_af

    nop

    :goto_261
    iget v2, v2, Landroid/view/ViewGroup$LayoutParams;->width:I

    goto :goto_159

    nop

    :goto_262
    move v1, v6

    goto :goto_11a

    nop

    :goto_263
    iget v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mTitleUpViewMarginEnd:I

    goto :goto_21e

    nop

    :goto_264
    move/from16 v19, v7

    goto :goto_192

    nop

    :goto_265
    if-eqz v5, :cond_4d

    goto :goto_86

    :cond_4d
    goto :goto_197

    nop

    :goto_266
    goto :goto_86

    :goto_267
    goto :goto_284

    nop

    :goto_268
    const/high16 v15, -0x80000000

    :goto_269
    goto :goto_208

    nop

    :goto_26a
    if-ne v7, v8, :cond_4e

    goto :goto_188

    :cond_4e
    goto :goto_187

    nop

    :goto_26b
    sub-float/2addr v3, v4

    goto :goto_5d

    nop

    :goto_26c
    sub-int/2addr v13, v9

    goto :goto_43

    nop

    :goto_26d
    iget-object v7, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mStartView:Landroid/view/View;

    goto :goto_218

    nop

    :goto_26e
    iget-object v11, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mExpandedActionView:Landroid/view/View;

    goto :goto_15a

    nop

    :goto_26f
    iget-object v2, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMainContainer:Landroid/widget/FrameLayout;

    goto :goto_1c0

    nop

    :goto_270
    instance-of v5, v11, Landroidx/appcompat/app/ActionBar$LayoutParams;

    goto :goto_28b

    nop

    :goto_271
    iget-object v2, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMainContainer:Landroid/widget/FrameLayout;

    goto :goto_1ab

    nop

    :goto_272
    goto :goto_94

    :goto_273
    goto :goto_7b

    nop

    :goto_274
    sub-int v8, v5, v8

    goto :goto_17e

    nop

    :goto_275
    const/4 v7, 0x0

    :goto_276
    goto :goto_40

    nop

    :goto_277
    move v2, v14

    :goto_278
    goto :goto_28a

    nop

    :goto_279
    if-nez v17, :cond_4f

    goto :goto_74

    :cond_4f
    goto :goto_11

    nop

    :goto_27a
    add-int/2addr v5, v7

    goto :goto_55

    nop

    :goto_27b
    move-object v5, v11

    goto :goto_2

    nop

    :goto_27c
    invoke-virtual {v2}, Landroid/widget/FrameLayout;->getMeasuredWidth()I

    move-result v2

    goto :goto_de

    nop

    :goto_27d
    iget-object v11, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mNavigatorSwitch:Landroid/view/View;

    goto :goto_158

    nop

    :goto_27e
    if-eq v6, v5, :cond_50

    goto :goto_1a9

    :cond_50
    goto :goto_216

    nop

    :goto_27f
    invoke-virtual {v1}, Landroid/view/View;->getMeasuredWidth()I

    move-result v2

    goto :goto_1d4

    nop

    :goto_280
    goto :goto_278

    :goto_281
    goto :goto_277

    nop

    :goto_282
    goto :goto_293

    :goto_283
    goto :goto_1db

    nop

    :goto_284
    move/from16 v17, v5

    goto :goto_85

    nop

    :goto_285
    const/high16 v7, 0x40000000

    goto :goto_1a4

    nop

    :goto_286
    goto :goto_19a

    :goto_287
    goto :goto_199

    nop

    :goto_288
    if-gtz v4, :cond_51

    goto :goto_ab

    :cond_51
    goto :goto_8

    nop

    :goto_289
    if-nez v1, :cond_52

    goto :goto_1cf

    :cond_52
    goto :goto_1ba

    nop

    :goto_28a
    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mEndMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    goto :goto_13

    nop

    :goto_28b
    if-nez v5, :cond_53

    goto :goto_1c

    :cond_53
    goto :goto_27b

    nop

    :goto_28c
    invoke-virtual {v0, v1, v13, v12, v2}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->measureChildView(Landroid/view/View;III)I

    move-result v13

    goto :goto_ad

    nop

    :goto_28d
    const/4 v5, 0x0

    :goto_28e
    goto :goto_20d

    nop

    :goto_28f
    if-nez v2, :cond_54

    goto :goto_99

    :cond_54
    goto :goto_1e0

    nop

    :goto_290
    iput v6, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mCollapseTotalHeight:I

    goto :goto_11b

    nop

    :goto_291
    invoke-virtual {v7}, Landroid/view/View;->getVisibility()I

    move-result v7

    goto :goto_209

    nop

    :goto_292
    const/16 v19, 0x0

    :goto_293
    goto :goto_b3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarView__updateExpandStateOnLayout',
        'method': '.method updateExpandStateOnLayout()Z',
        'method_name': 'updateExpandStateOnLayout',
        'method_anchors': ['iget v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mInnerExpandState:I', 'if-eq v0, v1, :cond_0', 'return v2', 'iget v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mExpandStateOnLayout:I', 'iget v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mPendingHeight:I', 'if-nez v1, :cond_1', 'iget-object v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableMainContainer:Landroid/widget/FrameLayout;', 'invoke-virtual {v4}, Landroid/widget/FrameLayout;->getMeasuredHeight()I'],
        'type': 'method_replace',
        'search': """.method updateExpandStateOnLayout()Z
    .registers 7

    iget v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mInnerExpandState:I

    const/4 v1, 0x2

    const/4 v2, 0x0

    if-eq v0, v1, :cond_0

    return v2

    :cond_0
    iget v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mExpandStateOnLayout:I

    iget v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mPendingHeight:I

    const/4 v3, 0x1

    if-nez v1, :cond_1

    move v0, v2

    goto :goto_0

    :cond_1
    iget-object v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    invoke-virtual {v4}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result v4

    iget v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableSecondaryTabHeight:I

    add-int/2addr v4, v5

    if-ne v1, v4, :cond_2

    move v0, v3

    :cond_2
    :goto_0
    iget v1, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mExpandStateOnLayout:I

    if-eq v1, v0, :cond_3

    iput v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mExpandStateOnLayout:I

    iput v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mExpandStateBeforeResizing:I

    return v3

    :cond_3
    return v2
.end method""",
        'replacement': """.method updateExpandStateOnLayout()Z
    .registers 7

    goto :goto_3

    nop

    :goto_0
    iput v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mExpandStateOnLayout:I

    goto :goto_4

    nop

    :goto_1
    const/4 v1, 0x2

    goto :goto_2

    nop

    :goto_2
    const/4 v2, 0x0

    goto :goto_7

    nop

    :goto_3
    iget v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mInnerExpandState:I

    goto :goto_1

    nop

    :goto_4
    iput v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mExpandStateBeforeResizing:I

    goto :goto_5

    nop

    :goto_5
    return v3

    :goto_6
    goto :goto_e

    nop

    :goto_7
    if-ne v0, v1, :cond_0

    goto :goto_1a

    :cond_0
    goto :goto_19

    nop

    :goto_8
    iget v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableSecondaryTabHeight:I

    goto :goto_17

    nop

    :goto_9
    iget-object v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    goto :goto_10

    nop

    :goto_a
    if-eqz v1, :cond_1

    goto :goto_13

    :cond_1
    goto :goto_11

    nop

    :goto_b
    iget v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mExpandStateOnLayout:I

    goto :goto_18

    nop

    :goto_c
    move v0, v3

    :goto_d
    goto :goto_14

    nop

    :goto_e
    return v2

    :goto_f
    if-eq v1, v4, :cond_2

    goto :goto_d

    :cond_2
    goto :goto_c

    nop

    :goto_10
    invoke-virtual {v4}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result v4

    goto :goto_8

    nop

    :goto_11
    move v0, v2

    goto :goto_12

    nop

    :goto_12
    goto :goto_d

    :goto_13
    goto :goto_9

    nop

    :goto_14
    iget v1, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mExpandStateOnLayout:I

    goto :goto_16

    nop

    :goto_15
    const/4 v3, 0x1

    goto :goto_a

    nop

    :goto_16
    if-ne v1, v0, :cond_3

    goto :goto_6

    :cond_3
    goto :goto_0

    nop

    :goto_17
    add-int/2addr v4, v5

    goto :goto_f

    nop

    :goto_18
    iget v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView;->mPendingHeight:I

    goto :goto_15

    nop

    :goto_19
    return v2

    :goto_1a
    goto :goto_b

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
