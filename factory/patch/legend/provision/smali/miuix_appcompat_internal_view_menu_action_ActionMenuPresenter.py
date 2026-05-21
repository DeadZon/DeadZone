TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/view/menu/action/ActionMenuPresenter.smali'
CLASS_FALLBACK_NAMES = ['ActionMenuPresenter.smali']
CLASS_ANCHORS = ['.super Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_view_menu_action_ActionMenuPresenter__createOverflowMenuButton',
        'method': '.method protected createOverflowMenuButton(Landroid/content/Context;)Landroid/view/View;',
        'method_name': 'createOverflowMenuButton',
        'method_anchors': ['new-instance v0, Lmiuix/appcompat/internal/view/menu/action/OverflowMenuButton;', 'iget v2, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->mOverflowMenuAttrs:I', 'invoke-direct {v0, p1, v1, v2}, Lmiuix/appcompat/internal/view/menu/action/OverflowMenuButton;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V', 'new-instance p1, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter$$ExternalSyntheticLambda0;', 'invoke-direct {p1, p0}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter$$ExternalSyntheticLambda0;-><init>(Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;)V', 'invoke-virtual {v0, p1}, Lmiuix/appcompat/internal/view/menu/action/OverflowMenuButton;->setOnOverflowMenuButtonClickListener(Lmiuix/appcompat/internal/view/menu/action/OverflowMenuButton$OnOverflowMenuButtonClickListener;)V', 'return-object v0'],
        'type': 'method_replace',
        'search': """.method protected createOverflowMenuButton(Landroid/content/Context;)Landroid/view/View;
    .registers 5

    new-instance v0, Lmiuix/appcompat/internal/view/menu/action/OverflowMenuButton;

    const/4 v1, 0x0

    iget v2, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->mOverflowMenuAttrs:I

    invoke-direct {v0, p1, v1, v2}, Lmiuix/appcompat/internal/view/menu/action/OverflowMenuButton;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    new-instance p1, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter$$ExternalSyntheticLambda0;

    invoke-direct {p1, p0}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter$$ExternalSyntheticLambda0;-><init>(Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;)V

    invoke-virtual {v0, p1}, Lmiuix/appcompat/internal/view/menu/action/OverflowMenuButton;->setOnOverflowMenuButtonClickListener(Lmiuix/appcompat/internal/view/menu/action/OverflowMenuButton$OnOverflowMenuButtonClickListener;)V

    return-object v0
.end method""",
        'replacement': """.method protected createOverflowMenuButton(Landroid/content/Context;)Landroid/view/View;
    .registers 5

    goto :goto_7

    nop

    :goto_0
    invoke-direct {v0, p1, v1, v2}, Lmiuix/appcompat/internal/view/menu/action/OverflowMenuButton;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    goto :goto_1

    nop

    :goto_1
    new-instance p1, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter$$ExternalSyntheticLambda0;

    goto :goto_5

    nop

    :goto_2
    return-object v0

    :goto_3
    invoke-virtual {v0, p1}, Lmiuix/appcompat/internal/view/menu/action/OverflowMenuButton;->setOnOverflowMenuButtonClickListener(Lmiuix/appcompat/internal/view/menu/action/OverflowMenuButton$OnOverflowMenuButtonClickListener;)V

    goto :goto_2

    nop

    :goto_4
    iget v2, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->mOverflowMenuAttrs:I

    goto :goto_0

    nop

    :goto_5
    invoke-direct {p1, p0}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter$$ExternalSyntheticLambda0;-><init>(Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;)V

    goto :goto_3

    nop

    :goto_6
    const/4 v1, 0x0

    goto :goto_4

    nop

    :goto_7
    new-instance v0, Lmiuix/appcompat/internal/view/menu/action/OverflowMenuButton;

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_action_ActionMenuPresenter__getDefaultMaxItemCount',
        'method': '.method protected getDefaultMaxItemCount()I',
        'method_name': 'getDefaultMaxItemCount',
        'method_anchors': ['iget-object p0, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mContext:Landroid/content/Context;', 'if-eqz p0, :cond_0', 'sget v1, Lmiuix/appcompat/R$attr;->actionMenuItemLimit:I', 'invoke-static {p0, v1, v0}, Lmiuix/internal/util/AttributeResolver;->resolveInt(Landroid/content/Context;II)I', 'return p0', 'return v0'],
        'type': 'method_replace',
        'search': """.method protected getDefaultMaxItemCount()I
    .registers 3

    iget-object p0, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mContext:Landroid/content/Context;

    const/4 v0, 0x5

    if-eqz p0, :cond_0

    sget v1, Lmiuix/appcompat/R$attr;->actionMenuItemLimit:I

    invoke-static {p0, v1, v0}, Lmiuix/internal/util/AttributeResolver;->resolveInt(Landroid/content/Context;II)I

    move-result p0

    return p0

    :cond_0
    return v0
.end method""",
        'replacement': """.method protected getDefaultMaxItemCount()I
    .registers 3

    goto :goto_2

    nop

    :goto_0
    sget v1, Lmiuix/appcompat/R$attr;->actionMenuItemLimit:I

    goto :goto_5

    nop

    :goto_1
    if-nez p0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_0

    nop

    :goto_2
    iget-object p0, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mContext:Landroid/content/Context;

    goto :goto_7

    nop

    :goto_3
    return p0

    :goto_4
    goto :goto_6

    nop

    :goto_5
    invoke-static {p0, v1, v0}, Lmiuix/internal/util/AttributeResolver;->resolveInt(Landroid/content/Context;II)I

    move-result p0

    goto :goto_3

    nop

    :goto_6
    return v0

    :goto_7
    const/4 v0, 0x5

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_action_ActionMenuPresenter__getOverflowMenu',
        'method': '.method protected getOverflowMenu()Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter$OverflowMenu;',
        'method_name': 'getOverflowMenu',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->shouldShowPopupOverflow()Z', 'if-eqz v0, :cond_0', 'new-instance v1, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter$PopupOverflowMenu;', 'iget-object v3, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mContext:Landroid/content/Context;', 'iget-object v4, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;', 'iget-object v5, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->mOverflowButton:Landroid/view/View;', 'iget-object v6, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->mDecorView:Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;', 'invoke-direct/range {v1 .. v7}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter$PopupOverflowMenu;-><init>(Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;Landroid/content/Context;Lmiuix/appcompat/internal/view/menu/MenuBuilder;Landroid/view/View;Landroid/view/View;Z)V'],
        'type': 'method_replace',
        'search': """.method protected getOverflowMenu()Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter$OverflowMenu;
    .registers 9

    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->shouldShowPopupOverflow()Z

    move-result v0

    if-eqz v0, :cond_0

    new-instance v1, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter$PopupOverflowMenu;

    iget-object v3, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mContext:Landroid/content/Context;

    iget-object v4, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    iget-object v5, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->mOverflowButton:Landroid/view/View;

    iget-object v6, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->mDecorView:Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;

    const/4 v7, 0x1

    move-object v2, p0

    invoke-direct/range {v1 .. v7}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter$PopupOverflowMenu;-><init>(Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;Landroid/content/Context;Lmiuix/appcompat/internal/view/menu/MenuBuilder;Landroid/view/View;Landroid/view/View;Z)V

    return-object v1

    :cond_0
    move-object v2, p0

    iget-object p0, v2, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->mListOverflowMenu:Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter$OverflowMenu;

    if-nez p0, :cond_1

    new-instance p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter$ListOverflowMenu;

    const/4 v0, 0x0

    invoke-direct {p0, v2, v0}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter$ListOverflowMenu;-><init>(Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter$1;)V

    iput-object p0, v2, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->mListOverflowMenu:Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter$OverflowMenu;

    :cond_1
    iget-object p0, v2, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->mListOverflowMenu:Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter$OverflowMenu;

    return-object p0
.end method""",
        'replacement': """.method protected getOverflowMenu()Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter$OverflowMenu;
    .registers 9

    goto :goto_13

    nop

    :goto_0
    invoke-direct/range {v1 .. v7}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter$PopupOverflowMenu;-><init>(Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;Landroid/content/Context;Lmiuix/appcompat/internal/view/menu/MenuBuilder;Landroid/view/View;Landroid/view/View;Z)V

    goto :goto_d

    nop

    :goto_1
    iget-object v5, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->mOverflowButton:Landroid/view/View;

    goto :goto_11

    nop

    :goto_2
    iget-object v3, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mContext:Landroid/content/Context;

    goto :goto_f

    nop

    :goto_3
    move-object v2, p0

    goto :goto_12

    nop

    :goto_4
    const/4 v0, 0x0

    goto :goto_8

    nop

    :goto_5
    if-eqz p0, :cond_0

    goto :goto_7

    :cond_0
    goto :goto_15

    nop

    :goto_6
    iput-object p0, v2, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->mListOverflowMenu:Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter$OverflowMenu;

    :goto_7
    goto :goto_14

    nop

    :goto_8
    invoke-direct {p0, v2, v0}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter$ListOverflowMenu;-><init>(Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter$1;)V

    goto :goto_6

    nop

    :goto_9
    new-instance v1, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter$PopupOverflowMenu;

    goto :goto_2

    nop

    :goto_a
    move-object v2, p0

    goto :goto_0

    nop

    :goto_b
    return-object p0

    :goto_c
    if-nez v0, :cond_1

    goto :goto_e

    :cond_1
    goto :goto_9

    nop

    :goto_d
    return-object v1

    :goto_e
    goto :goto_3

    nop

    :goto_f
    iget-object v4, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    goto :goto_1

    nop

    :goto_10
    const/4 v7, 0x1

    goto :goto_a

    nop

    :goto_11
    iget-object v6, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->mDecorView:Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;

    goto :goto_10

    nop

    :goto_12
    iget-object p0, v2, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->mListOverflowMenu:Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter$OverflowMenu;

    goto :goto_5

    nop

    :goto_13
    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->shouldShowPopupOverflow()Z

    move-result v0

    goto :goto_c

    nop

    :goto_14
    iget-object p0, v2, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->mListOverflowMenu:Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter$OverflowMenu;

    goto :goto_b

    nop

    :goto_15
    new-instance p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter$ListOverflowMenu;

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_action_ActionMenuPresenter__getOverflowMenuAnimationGravity',
        'method': '.method protected getOverflowMenuAnimationGravity(Landroid/view/View;)I',
        'method_name': 'getOverflowMenuAnimationGravity',
        'method_anchors': ['return p0'],
        'type': 'method_replace',
        'search': """.method protected getOverflowMenuAnimationGravity(Landroid/view/View;)I
    .registers 2

    const/4 p0, -0x1

    return p0
.end method""",
        'replacement': """.method protected getOverflowMenuAnimationGravity(Landroid/view/View;)I
    .registers 2

    goto :goto_0

    nop

    :goto_0
    const/4 p0, -0x1

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
        'id': 'miuix_appcompat_internal_view_menu_action_ActionMenuPresenter__getOverflowMenuItem',
        'method': '.method protected getOverflowMenuItem()Lmiuix/appcompat/internal/view/menu/MenuItemImpl;',
        'method_name': 'getOverflowMenuItem',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->mOverflowMenuItem:Lmiuix/appcompat/internal/view/menu/MenuItemImpl;', 'if-nez v0, :cond_0', 'iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;', 'sget v3, Lmiuix/appcompat/R$id;->more:I', 'iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mContext:Landroid/content/Context;', 'sget v2, Lmiuix/appcompat/R$string;->more:I', 'invoke-virtual {v0, v2}, Landroid/content/Context;->getString(I)Ljava/lang/String;', 'invoke-static/range {v1 .. v7}, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->createMenuItemImpl(Lmiuix/appcompat/internal/view/menu/MenuBuilder;IIIILjava/lang/CharSequence;I)Lmiuix/appcompat/internal/view/menu/MenuItemImpl;'],
        'type': 'method_replace',
        'search': """.method protected getOverflowMenuItem()Lmiuix/appcompat/internal/view/menu/MenuItemImpl;
    .registers 9

    iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->mOverflowMenuItem:Lmiuix/appcompat/internal/view/menu/MenuItemImpl;

    if-nez v0, :cond_0

    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    sget v3, Lmiuix/appcompat/R$id;->more:I

    iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mContext:Landroid/content/Context;

    sget v2, Lmiuix/appcompat/R$string;->more:I

    invoke-virtual {v0, v2}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    const/4 v7, 0x0

    const/4 v2, 0x0

    const/4 v4, 0x0

    const/4 v5, 0x0

    invoke-static/range {v1 .. v7}, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->createMenuItemImpl(Lmiuix/appcompat/internal/view/menu/MenuBuilder;IIIILjava/lang/CharSequence;I)Lmiuix/appcompat/internal/view/menu/MenuItemImpl;

    move-result-object v0

    iput-object v0, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->mOverflowMenuItem:Lmiuix/appcompat/internal/view/menu/MenuItemImpl;

    :cond_0
    iget-object p0, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->mOverflowMenuItem:Lmiuix/appcompat/internal/view/menu/MenuItemImpl;

    return-object p0
.end method""",
        'replacement': """.method protected getOverflowMenuItem()Lmiuix/appcompat/internal/view/menu/MenuItemImpl;
    .registers 9

    goto :goto_0

    nop

    :goto_0
    iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->mOverflowMenuItem:Lmiuix/appcompat/internal/view/menu/MenuItemImpl;

    goto :goto_6

    nop

    :goto_1
    iget-object p0, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->mOverflowMenuItem:Lmiuix/appcompat/internal/view/menu/MenuItemImpl;

    goto :goto_f

    nop

    :goto_2
    const/4 v2, 0x0

    goto :goto_7

    nop

    :goto_3
    iput-object v0, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->mOverflowMenuItem:Lmiuix/appcompat/internal/view/menu/MenuItemImpl;

    :goto_4
    goto :goto_1

    nop

    :goto_5
    const/4 v5, 0x0

    goto :goto_b

    nop

    :goto_6
    if-eqz v0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_a

    nop

    :goto_7
    const/4 v4, 0x0

    goto :goto_5

    nop

    :goto_8
    sget v2, Lmiuix/appcompat/R$string;->more:I

    goto :goto_e

    nop

    :goto_9
    sget v3, Lmiuix/appcompat/R$id;->more:I

    goto :goto_c

    nop

    :goto_a
    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    goto :goto_9

    nop

    :goto_b
    invoke-static/range {v1 .. v7}, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->createMenuItemImpl(Lmiuix/appcompat/internal/view/menu/MenuBuilder;IIIILjava/lang/CharSequence;I)Lmiuix/appcompat/internal/view/menu/MenuItemImpl;

    move-result-object v0

    goto :goto_3

    nop

    :goto_c
    iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mContext:Landroid/content/Context;

    goto :goto_8

    nop

    :goto_d
    const/4 v7, 0x0

    goto :goto_2

    nop

    :goto_e
    invoke-virtual {v0, v2}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    goto :goto_d

    nop

    :goto_f
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_action_ActionMenuPresenter__isConvertViewTypeAllowed',
        'method': '.method protected isConvertViewTypeAllowed(Landroid/view/View;)Z',
        'method_name': 'isConvertViewTypeAllowed',
        'method_anchors': ['return p0'],
        'type': 'method_replace',
        'search': """.method protected isConvertViewTypeAllowed(Landroid/view/View;)Z
    .registers 2

    instance-of p0, p1, Lmiuix/appcompat/internal/view/menu/action/ActionMenuItemView;

    return p0
.end method""",
        'replacement': """.method protected isConvertViewTypeAllowed(Landroid/view/View;)Z
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    instance-of p0, p1, Lmiuix/appcompat/internal/view/menu/action/ActionMenuItemView;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_action_ActionMenuPresenter__shouldShowPopupOverflow',
        'method': '.method protected shouldShowPopupOverflow()Z',
        'method_name': 'shouldShowPopupOverflow',
        'method_anchors': ['iget-object p0, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->mOverflowButton:Landroid/view/View;', 'if-eqz p0, :cond_0', 'invoke-virtual {p0}, Landroid/view/View;->getParent()Landroid/view/ViewParent;', 'if-eqz p0, :cond_0', 'return p0', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected shouldShowPopupOverflow()Z
    .registers 1

    iget-object p0, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->mOverflowButton:Landroid/view/View;

    if-eqz p0, :cond_0

    invoke-virtual {p0}, Landroid/view/View;->getParent()Landroid/view/ViewParent;

    move-result-object p0

    if-eqz p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method protected shouldShowPopupOverflow()Z
    .registers 1

    goto :goto_1

    nop

    :goto_0
    const/4 p0, 0x0

    goto :goto_4

    nop

    :goto_1
    iget-object p0, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->mOverflowButton:Landroid/view/View;

    goto :goto_7

    nop

    :goto_2
    return p0

    :goto_3
    goto :goto_0

    nop

    :goto_4
    return p0

    :goto_5
    const/4 p0, 0x1

    goto :goto_2

    nop

    :goto_6
    invoke-virtual {p0}, Landroid/view/View;->getParent()Landroid/view/ViewParent;

    move-result-object p0

    goto :goto_8

    nop

    :goto_7
    if-nez p0, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_6

    nop

    :goto_8
    if-nez p0, :cond_1

    goto :goto_3

    :cond_1
    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
