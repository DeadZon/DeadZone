TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/view/menu/action/EndActionMenuPresenter.smali'
CLASS_FALLBACK_NAMES = ['EndActionMenuPresenter.smali']
CLASS_ANCHORS = ['.super Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_view_menu_action_EndActionMenuPresenter__createOverflowMenuButton',
        'method': '.method protected createOverflowMenuButton(Landroid/content/Context;)Landroid/view/View;',
        'method_name': 'createOverflowMenuButton',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mMenuView:Lmiuix/appcompat/internal/view/menu/MenuView;', 'check-cast v0, Landroid/view/ViewGroup;', 'if-nez v0, :cond_0', 'return-object v1', 'iget-object v2, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;', 'sget v4, Lmiuix/appcompat/R$id;->more:I', 'sget v3, Lmiuix/appcompat/R$string;->more:I', 'invoke-virtual {p1, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;'],
        'type': 'method_replace',
        'search': """.method protected createOverflowMenuButton(Landroid/content/Context;)Landroid/view/View;
    .registers 11

    iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mMenuView:Lmiuix/appcompat/internal/view/menu/MenuView;

    check-cast v0, Landroid/view/ViewGroup;

    const/4 v1, 0x0

    if-nez v0, :cond_0

    return-object v1

    :cond_0
    iget-object v2, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    sget v4, Lmiuix/appcompat/R$id;->more:I

    sget v3, Lmiuix/appcompat/R$string;->more:I

    invoke-virtual {p1, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v7

    const/4 v8, 0x2

    const/4 v3, 0x0

    const/4 v5, 0x0

    const/4 v6, 0x0

    invoke-static/range {v2 .. v8}, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->createMenuItemImpl(Lmiuix/appcompat/internal/view/menu/MenuBuilder;IIIILjava/lang/CharSequence;I)Lmiuix/appcompat/internal/view/menu/MenuItemImpl;

    move-result-object v2

    iget-object v3, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    invoke-virtual {v3}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->stopDispatchingItemsChanged()V

    sget v3, Lmiuix/appcompat/R$attr;->endActionMoreButtonIcon:I

    filled-new-array {v3}, [I

    move-result-object v3

    invoke-virtual {p1, v3}, Landroid/content/Context;->obtainStyledAttributes([I)Landroid/content/res/TypedArray;

    move-result-object p1

    const/4 v3, 0x0

    invoke-virtual {p1, v3}, Landroid/content/res/TypedArray;->getDrawable(I)Landroid/graphics/drawable/Drawable;

    move-result-object v5

    invoke-virtual {p1}, Landroid/content/res/TypedArray;->recycle()V

    invoke-virtual {v2, v5}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->setIcon(Landroid/graphics/drawable/Drawable;)Landroid/view/MenuItem;

    new-instance p1, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuPresenter$$ExternalSyntheticLambda0;

    invoke-direct {p1, p0}, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuPresenter$$ExternalSyntheticLambda0;-><init>(Lmiuix/appcompat/internal/view/menu/action/EndActionMenuPresenter;)V

    invoke-virtual {v2, p1}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->setOnMenuItemClickListener(Landroid/view/MenuItem$OnMenuItemClickListener;)Landroid/view/MenuItem;

    iget-object p1, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    invoke-virtual {p1, v3}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->setPreventDispatchingItemsChanged(Z)V

    invoke-virtual {p0, v2, v1, v0}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->getItemView(Lmiuix/appcompat/internal/view/menu/MenuItemImpl;Landroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;

    move-result-object p1

    invoke-virtual {p1, v4}, Landroid/view/View;->setId(I)V

    iput-object v2, p0, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuPresenter;->mMoreButtonItem:Lmiuix/appcompat/internal/view/menu/MenuItemImpl;

    invoke-virtual {v2, p1}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->setView(Landroid/view/View;)V

    return-object p1
.end method""",
        'replacement': """.method protected createOverflowMenuButton(Landroid/content/Context;)Landroid/view/View;
    .registers 11

    goto :goto_c

    nop

    :goto_0
    sget v3, Lmiuix/appcompat/R$attr;->endActionMoreButtonIcon:I

    goto :goto_17

    nop

    :goto_1
    sget v3, Lmiuix/appcompat/R$string;->more:I

    goto :goto_f

    nop

    :goto_2
    iget-object v2, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    goto :goto_8

    nop

    :goto_3
    invoke-virtual {p0, v2, v1, v0}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->getItemView(Lmiuix/appcompat/internal/view/menu/MenuItemImpl;Landroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;

    move-result-object p1

    goto :goto_19

    nop

    :goto_4
    invoke-virtual {v2, p1}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->setOnMenuItemClickListener(Landroid/view/MenuItem$OnMenuItemClickListener;)Landroid/view/MenuItem;

    goto :goto_21

    nop

    :goto_5
    invoke-static/range {v2 .. v8}, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->createMenuItemImpl(Lmiuix/appcompat/internal/view/menu/MenuBuilder;IIIILjava/lang/CharSequence;I)Lmiuix/appcompat/internal/view/menu/MenuItemImpl;

    move-result-object v2

    goto :goto_a

    nop

    :goto_6
    invoke-virtual {p1, v3}, Landroid/content/res/TypedArray;->getDrawable(I)Landroid/graphics/drawable/Drawable;

    move-result-object v5

    goto :goto_16

    nop

    :goto_7
    return-object p1

    :goto_8
    sget v4, Lmiuix/appcompat/R$id;->more:I

    goto :goto_1

    nop

    :goto_9
    const/4 v3, 0x0

    goto :goto_15

    nop

    :goto_a
    iget-object v3, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    goto :goto_1c

    nop

    :goto_b
    const/4 v8, 0x2

    goto :goto_9

    nop

    :goto_c
    iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mMenuView:Lmiuix/appcompat/internal/view/menu/MenuView;

    goto :goto_18

    nop

    :goto_d
    const/4 v1, 0x0

    goto :goto_12

    nop

    :goto_e
    iput-object v2, p0, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuPresenter;->mMoreButtonItem:Lmiuix/appcompat/internal/view/menu/MenuItemImpl;

    goto :goto_1f

    nop

    :goto_f
    invoke-virtual {p1, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v7

    goto :goto_b

    nop

    :goto_10
    invoke-direct {p1, p0}, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuPresenter$$ExternalSyntheticLambda0;-><init>(Lmiuix/appcompat/internal/view/menu/action/EndActionMenuPresenter;)V

    goto :goto_4

    nop

    :goto_11
    invoke-virtual {p1, v3}, Landroid/content/Context;->obtainStyledAttributes([I)Landroid/content/res/TypedArray;

    move-result-object p1

    goto :goto_1b

    nop

    :goto_12
    if-eqz v0, :cond_0

    goto :goto_14

    :cond_0
    goto :goto_13

    nop

    :goto_13
    return-object v1

    :goto_14
    goto :goto_2

    nop

    :goto_15
    const/4 v5, 0x0

    goto :goto_20

    nop

    :goto_16
    invoke-virtual {p1}, Landroid/content/res/TypedArray;->recycle()V

    goto :goto_1e

    nop

    :goto_17
    filled-new-array {v3}, [I

    move-result-object v3

    goto :goto_11

    nop

    :goto_18
    check-cast v0, Landroid/view/ViewGroup;

    goto :goto_d

    nop

    :goto_19
    invoke-virtual {p1, v4}, Landroid/view/View;->setId(I)V

    goto :goto_e

    nop

    :goto_1a
    new-instance p1, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuPresenter$$ExternalSyntheticLambda0;

    goto :goto_10

    nop

    :goto_1b
    const/4 v3, 0x0

    goto :goto_6

    nop

    :goto_1c
    invoke-virtual {v3}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->stopDispatchingItemsChanged()V

    goto :goto_0

    nop

    :goto_1d
    invoke-virtual {p1, v3}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->setPreventDispatchingItemsChanged(Z)V

    goto :goto_3

    nop

    :goto_1e
    invoke-virtual {v2, v5}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->setIcon(Landroid/graphics/drawable/Drawable;)Landroid/view/MenuItem;

    goto :goto_1a

    nop

    :goto_1f
    invoke-virtual {v2, p1}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->setView(Landroid/view/View;)V

    goto :goto_7

    nop

    :goto_20
    const/4 v6, 0x0

    goto :goto_5

    nop

    :goto_21
    iget-object p1, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    goto :goto_1d

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_action_EndActionMenuPresenter__getDefaultMaxItemCount',
        'method': '.method protected getDefaultMaxItemCount()I',
        'method_name': 'getDefaultMaxItemCount',
        'method_anchors': ['iget-object p0, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mContext:Landroid/content/Context;', 'if-eqz p0, :cond_0', 'invoke-virtual {p0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;', 'sget v0, Lmiuix/appcompat/R$integer;->action_bar_end_menu_max_item_count:I', 'invoke-virtual {p0, v0}, Landroid/content/res/Resources;->getInteger(I)I', 'return p0', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected getDefaultMaxItemCount()I
    .registers 2

    iget-object p0, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mContext:Landroid/content/Context;

    if-eqz p0, :cond_0

    invoke-virtual {p0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object p0

    sget v0, Lmiuix/appcompat/R$integer;->action_bar_end_menu_max_item_count:I

    invoke-virtual {p0, v0}, Landroid/content/res/Resources;->getInteger(I)I

    move-result p0

    return p0

    :cond_0
    const/4 p0, 0x5

    return p0
.end method""",
        'replacement': """.method protected getDefaultMaxItemCount()I
    .registers 2

    goto :goto_7

    nop

    :goto_0
    return p0

    :goto_1
    goto :goto_8

    nop

    :goto_2
    invoke-virtual {p0, v0}, Landroid/content/res/Resources;->getInteger(I)I

    move-result p0

    goto :goto_0

    nop

    :goto_3
    sget v0, Lmiuix/appcompat/R$integer;->action_bar_end_menu_max_item_count:I

    goto :goto_2

    nop

    :goto_4
    invoke-virtual {p0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object p0

    goto :goto_3

    nop

    :goto_5
    if-nez p0, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_4

    nop

    :goto_6
    return p0

    :goto_7
    iget-object p0, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mContext:Landroid/content/Context;

    goto :goto_5

    nop

    :goto_8
    const/4 p0, 0x5

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_action_EndActionMenuPresenter__getOverflowMenuAnimationGravity',
        'method': '.method protected getOverflowMenuAnimationGravity(Landroid/view/View;)I',
        'method_name': 'getOverflowMenuAnimationGravity',
        'method_anchors': ['invoke-static {p1}, Lmiuix/internal/util/ViewUtils;->isLayoutRtl(Landroid/view/View;)Z', 'if-eqz p0, :cond_0', 'return p0', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected getOverflowMenuAnimationGravity(Landroid/view/View;)I
    .registers 2

    invoke-static {p1}, Lmiuix/internal/util/ViewUtils;->isLayoutRtl(Landroid/view/View;)Z

    move-result p0

    if-eqz p0, :cond_0

    const/16 p0, 0x33

    return p0

    :cond_0
    const/16 p0, 0x35

    return p0
.end method""",
        'replacement': """.method protected getOverflowMenuAnimationGravity(Landroid/view/View;)I
    .registers 2

    goto :goto_0

    nop

    :goto_0
    invoke-static {p1}, Lmiuix/internal/util/ViewUtils;->isLayoutRtl(Landroid/view/View;)Z

    move-result p0

    goto :goto_3

    nop

    :goto_1
    const/16 p0, 0x33

    goto :goto_4

    nop

    :goto_2
    return p0

    :goto_3
    if-nez p0, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_1

    nop

    :goto_4
    return p0

    :goto_5
    goto :goto_6

    nop

    :goto_6
    const/16 p0, 0x35

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_action_EndActionMenuPresenter__isConvertViewTypeAllowed',
        'method': '.method protected isConvertViewTypeAllowed(Landroid/view/View;)Z',
        'method_name': 'isConvertViewTypeAllowed',
        'method_anchors': ['if-eqz p1, :cond_1', 'iget-object p0, p0, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuPresenter;->mMoreButtonItem:Lmiuix/appcompat/internal/view/menu/MenuItemImpl;', 'if-eqz p0, :cond_0', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->getView()Landroid/view/View;', 'if-ne p0, p1, :cond_0', 'if-eqz p1, :cond_1', 'if-nez p0, :cond_1', 'return v1'],
        'type': 'method_replace',
        'search': """.method protected isConvertViewTypeAllowed(Landroid/view/View;)Z
    .registers 4

    const/4 v0, 0x0

    if-eqz p1, :cond_1

    iget-object p0, p0, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuPresenter;->mMoreButtonItem:Lmiuix/appcompat/internal/view/menu/MenuItemImpl;

    const/4 v1, 0x1

    if-eqz p0, :cond_0

    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->getView()Landroid/view/View;

    move-result-object p0

    if-ne p0, p1, :cond_0

    move p0, v1

    goto :goto_0

    :cond_0
    move p0, v0

    :goto_0
    instance-of p1, p1, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuItemView;

    if-eqz p1, :cond_1

    if-nez p0, :cond_1

    return v1

    :cond_1
    return v0
.end method""",
        'replacement': """.method protected isConvertViewTypeAllowed(Landroid/view/View;)Z
    .registers 4

    goto :goto_3

    nop

    :goto_0
    move p0, v1

    goto :goto_1

    nop

    :goto_1
    goto :goto_6

    :goto_2
    goto :goto_5

    nop

    :goto_3
    const/4 v0, 0x0

    goto :goto_c

    nop

    :goto_4
    const/4 v1, 0x1

    goto :goto_e

    nop

    :goto_5
    move p0, v0

    :goto_6
    goto :goto_8

    nop

    :goto_7
    if-eqz p0, :cond_0

    goto :goto_11

    :cond_0
    goto :goto_10

    nop

    :goto_8
    instance-of p1, p1, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuItemView;

    goto :goto_a

    nop

    :goto_9
    iget-object p0, p0, Lmiuix/appcompat/internal/view/menu/action/EndActionMenuPresenter;->mMoreButtonItem:Lmiuix/appcompat/internal/view/menu/MenuItemImpl;

    goto :goto_4

    nop

    :goto_a
    if-nez p1, :cond_1

    goto :goto_11

    :cond_1
    goto :goto_7

    nop

    :goto_b
    return v0

    :goto_c
    if-nez p1, :cond_2

    goto :goto_11

    :cond_2
    goto :goto_9

    nop

    :goto_d
    if-eq p0, p1, :cond_3

    goto :goto_2

    :cond_3
    goto :goto_0

    nop

    :goto_e
    if-nez p0, :cond_4

    goto :goto_2

    :cond_4
    goto :goto_f

    nop

    :goto_f
    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->getView()Landroid/view/View;

    move-result-object p0

    goto :goto_d

    nop

    :goto_10
    return v1

    :goto_11
    goto :goto_b

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
