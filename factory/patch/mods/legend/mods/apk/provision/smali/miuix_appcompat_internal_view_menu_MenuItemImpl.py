TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/view/menu/MenuItemImpl.smali'
CLASS_FALLBACK_NAMES = ['MenuItemImpl.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Landroid/view/MenuItem;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_view_menu_MenuItemImpl__getShortcut',
        'method': '.method getShortcut()C',
        'method_name': 'getShortcut',
        'method_anchors': ['iget-char p0, p0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->mShortcutAlphabeticChar:C', 'return p0'],
        'type': 'method_replace',
        'search': """.method getShortcut()C
    .registers 1

    iget-char p0, p0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->mShortcutAlphabeticChar:C

    return p0
.end method""",
        'replacement': """.method getShortcut()C
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    iget-char p0, p0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->mShortcutAlphabeticChar:C

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_MenuItemImpl__getShortcutLabel',
        'method': '.method getShortcutLabel()Ljava/lang/String;',
        'method_name': 'getShortcutLabel',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->getShortcut()C', 'if-nez p0, :cond_0', 'const-string p0, ""', 'return-object p0', 'new-instance v0, Ljava/lang/StringBuilder;', 'sget-object v1, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->sPrependShortcutLabel:Ljava/lang/String;', 'invoke-direct {v0, v1}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V', 'if-eq p0, v1, :cond_3'],
        'type': 'method_replace',
        'search': """.method getShortcutLabel()Ljava/lang/String;
    .registers 3

    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->getShortcut()C

    move-result p0

    if-nez p0, :cond_0

    const-string p0, ""

    return-object p0

    :cond_0
    new-instance v0, Ljava/lang/StringBuilder;

    sget-object v1, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->sPrependShortcutLabel:Ljava/lang/String;

    invoke-direct {v0, v1}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V

    const/16 v1, 0x8

    if-eq p0, v1, :cond_3

    const/16 v1, 0xa

    if-eq p0, v1, :cond_2

    const/16 v1, 0x20

    if-eq p0, v1, :cond_1

    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(C)Ljava/lang/StringBuilder;

    goto :goto_0

    :cond_1
    sget-object p0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->sSpaceShortcutLabel:Ljava/lang/String;

    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_0

    :cond_2
    sget-object p0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->sEnterShortcutLabel:Ljava/lang/String;

    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_0

    :cond_3
    sget-object p0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->sDeleteShortcutLabel:Ljava/lang/String;

    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :goto_0
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method getShortcutLabel()Ljava/lang/String;
    .registers 3

    goto :goto_9

    nop

    :goto_0
    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :goto_1
    goto :goto_f

    nop

    :goto_2
    goto :goto_1

    :goto_3
    goto :goto_18

    nop

    :goto_4
    return-object p0

    :goto_5
    const/16 v1, 0x8

    goto :goto_12

    nop

    :goto_6
    invoke-direct {v0, v1}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V

    goto :goto_5

    nop

    :goto_7
    goto :goto_1

    :goto_8
    goto :goto_19

    nop

    :goto_9
    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->getShortcut()C

    move-result p0

    goto :goto_1a

    nop

    :goto_a
    return-object p0

    :goto_b
    goto :goto_11

    nop

    :goto_c
    if-ne p0, v1, :cond_0

    goto :goto_1d

    :cond_0
    goto :goto_16

    nop

    :goto_d
    const/16 v1, 0x20

    goto :goto_c

    nop

    :goto_e
    const/16 v1, 0xa

    goto :goto_13

    nop

    :goto_f
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    goto :goto_4

    nop

    :goto_10
    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_7

    nop

    :goto_11
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_17

    nop

    :goto_12
    if-ne p0, v1, :cond_1

    goto :goto_3

    :cond_1
    goto :goto_e

    nop

    :goto_13
    if-ne p0, v1, :cond_2

    goto :goto_8

    :cond_2
    goto :goto_d

    nop

    :goto_14
    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_2

    nop

    :goto_15
    sget-object p0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->sSpaceShortcutLabel:Ljava/lang/String;

    goto :goto_10

    nop

    :goto_16
    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(C)Ljava/lang/StringBuilder;

    goto :goto_1c

    nop

    :goto_17
    sget-object v1, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->sPrependShortcutLabel:Ljava/lang/String;

    goto :goto_6

    nop

    :goto_18
    sget-object p0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->sDeleteShortcutLabel:Ljava/lang/String;

    goto :goto_0

    nop

    :goto_19
    sget-object p0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->sEnterShortcutLabel:Ljava/lang/String;

    goto :goto_14

    nop

    :goto_1a
    if-eqz p0, :cond_3

    goto :goto_b

    :cond_3
    goto :goto_1b

    nop

    :goto_1b
    const-string p0, ""

    goto :goto_a

    nop

    :goto_1c
    goto :goto_1

    :goto_1d
    goto :goto_15

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_MenuItemImpl__getTitleForItemView',
        'method': '.method getTitleForItemView(Lmiuix/appcompat/internal/view/menu/MenuView$ItemView;)Ljava/lang/CharSequence;',
        'method_name': 'getTitleForItemView',
        'method_anchors': ['if-eqz p1, :cond_0', 'invoke-interface {p1}, Lmiuix/appcompat/internal/view/menu/MenuView$ItemView;->prefersCondensedTitle()Z', 'if-eqz p1, :cond_0', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->getTitleCondensed()Ljava/lang/CharSequence;', 'return-object p0', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->getTitle()Ljava/lang/CharSequence;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method getTitleForItemView(Lmiuix/appcompat/internal/view/menu/MenuView$ItemView;)Ljava/lang/CharSequence;
    .registers 2

    if-eqz p1, :cond_0

    invoke-interface {p1}, Lmiuix/appcompat/internal/view/menu/MenuView$ItemView;->prefersCondensedTitle()Z

    move-result p1

    if-eqz p1, :cond_0

    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->getTitleCondensed()Ljava/lang/CharSequence;

    move-result-object p0

    return-object p0

    :cond_0
    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->getTitle()Ljava/lang/CharSequence;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method getTitleForItemView(Lmiuix/appcompat/internal/view/menu/MenuView$ItemView;)Ljava/lang/CharSequence;
    .registers 2

    goto :goto_4

    nop

    :goto_0
    invoke-interface {p1}, Lmiuix/appcompat/internal/view/menu/MenuView$ItemView;->prefersCondensedTitle()Z

    move-result p1

    goto :goto_7

    nop

    :goto_1
    return-object p0

    :goto_2
    goto :goto_3

    nop

    :goto_3
    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->getTitle()Ljava/lang/CharSequence;

    move-result-object p0

    goto :goto_6

    nop

    :goto_4
    if-nez p1, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_0

    nop

    :goto_5
    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->getTitleCondensed()Ljava/lang/CharSequence;

    move-result-object p0

    goto :goto_1

    nop

    :goto_6
    return-object p0

    :goto_7
    if-nez p1, :cond_1

    goto :goto_2

    :cond_1
    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_MenuItemImpl__setSubMenu',
        'method': '.method protected setSubMenu(Lmiuix/appcompat/internal/view/menu/SubMenuBuilder;)V',
        'method_name': 'setSubMenu',
        'method_anchors': ['iput-object p1, p0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->mSubMenu:Lmiuix/appcompat/internal/view/menu/SubMenuBuilder;', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->getTitle()Ljava/lang/CharSequence;', 'invoke-virtual {p1, p0}, Lmiuix/appcompat/internal/view/menu/SubMenuBuilder;->setHeaderTitle(Ljava/lang/CharSequence;)Landroid/view/SubMenu;', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected setSubMenu(Lmiuix/appcompat/internal/view/menu/SubMenuBuilder;)V
    .registers 2

    iput-object p1, p0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->mSubMenu:Lmiuix/appcompat/internal/view/menu/SubMenuBuilder;

    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->getTitle()Ljava/lang/CharSequence;

    move-result-object p0

    invoke-virtual {p1, p0}, Lmiuix/appcompat/internal/view/menu/SubMenuBuilder;->setHeaderTitle(Ljava/lang/CharSequence;)Landroid/view/SubMenu;

    return-void
.end method""",
        'replacement': """.method protected setSubMenu(Lmiuix/appcompat/internal/view/menu/SubMenuBuilder;)V
    .registers 2

    goto :goto_3

    nop

    :goto_0
    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->getTitle()Ljava/lang/CharSequence;

    move-result-object p0

    goto :goto_1

    nop

    :goto_1
    invoke-virtual {p1, p0}, Lmiuix/appcompat/internal/view/menu/SubMenuBuilder;->setHeaderTitle(Ljava/lang/CharSequence;)Landroid/view/SubMenu;

    goto :goto_2

    nop

    :goto_2
    return-void

    :goto_3
    iput-object p1, p0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->mSubMenu:Lmiuix/appcompat/internal/view/menu/SubMenuBuilder;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_MenuItemImpl__setCheckedInt',
        'method': '.method setCheckedInt(Z)V',
        'method_name': 'setCheckedInt',
        'method_anchors': ['iget v0, p0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->mFlags:I', 'if-eqz p1, :cond_0', 'iput p1, p0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->mFlags:I', 'if-eq v0, p1, :cond_1', 'iget-object p0, p0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;', 'invoke-virtual {p0, v2}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->onItemsChanged(Z)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method setCheckedInt(Z)V
    .registers 5

    iget v0, p0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->mFlags:I

    and-int/lit8 v1, v0, -0x3

    const/4 v2, 0x0

    if-eqz p1, :cond_0

    const/4 p1, 0x2

    goto :goto_0

    :cond_0
    move p1, v2

    :goto_0
    or-int/2addr p1, v1

    iput p1, p0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->mFlags:I

    if-eq v0, p1, :cond_1

    iget-object p0, p0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    invoke-virtual {p0, v2}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->onItemsChanged(Z)V

    :cond_1
    return-void
.end method""",
        'replacement': """.method setCheckedInt(Z)V
    .registers 5

    goto :goto_4

    nop

    :goto_0
    invoke-virtual {p0, v2}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->onItemsChanged(Z)V

    :goto_1
    goto :goto_7

    nop

    :goto_2
    goto :goto_e

    :goto_3
    goto :goto_d

    nop

    :goto_4
    iget v0, p0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->mFlags:I

    goto :goto_c

    nop

    :goto_5
    const/4 p1, 0x2

    goto :goto_2

    nop

    :goto_6
    const/4 v2, 0x0

    goto :goto_8

    nop

    :goto_7
    return-void

    :goto_8
    if-nez p1, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_5

    nop

    :goto_9
    or-int/2addr p1, v1

    goto :goto_a

    nop

    :goto_a
    iput p1, p0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->mFlags:I

    goto :goto_f

    nop

    :goto_b
    iget-object p0, p0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    goto :goto_0

    nop

    :goto_c
    and-int/lit8 v1, v0, -0x3

    goto :goto_6

    nop

    :goto_d
    move p1, v2

    :goto_e
    goto :goto_9

    nop

    :goto_f
    if-ne v0, p1, :cond_1

    goto :goto_1

    :cond_1
    goto :goto_b

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_MenuItemImpl__setMenuInfo',
        'method': '.method setMenuInfo(Landroid/view/ContextMenu$ContextMenuInfo;)V',
        'method_name': 'setMenuInfo',
        'method_anchors': ['iput-object p1, p0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->mMenuInfo:Landroid/view/ContextMenu$ContextMenuInfo;', 'return-void'],
        'type': 'method_replace',
        'search': """.method setMenuInfo(Landroid/view/ContextMenu$ContextMenuInfo;)V
    .registers 2

    iput-object p1, p0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->mMenuInfo:Landroid/view/ContextMenu$ContextMenuInfo;

    return-void
.end method""",
        'replacement': """.method setMenuInfo(Landroid/view/ContextMenu$ContextMenuInfo;)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    iput-object p1, p0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->mMenuInfo:Landroid/view/ContextMenu$ContextMenuInfo;

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
        'id': 'miuix_appcompat_internal_view_menu_MenuItemImpl__setVisibleInt',
        'method': '.method setVisibleInt(Z)Z',
        'method_name': 'setVisibleInt',
        'method_anchors': ['iget v0, p0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->mFlags:I', 'if-eqz p1, :cond_0', 'iput p1, p0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->mFlags:I', 'if-eq v0, p1, :cond_1', 'return p0', 'return v2'],
        'type': 'method_replace',
        'search': """.method setVisibleInt(Z)Z
    .registers 5

    iget v0, p0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->mFlags:I

    and-int/lit8 v1, v0, -0x9

    const/4 v2, 0x0

    if-eqz p1, :cond_0

    move p1, v2

    goto :goto_0

    :cond_0
    const/16 p1, 0x8

    :goto_0
    or-int/2addr p1, v1

    iput p1, p0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->mFlags:I

    if-eq v0, p1, :cond_1

    const/4 p0, 0x1

    return p0

    :cond_1
    return v2
.end method""",
        'replacement': """.method setVisibleInt(Z)Z
    .registers 5

    goto :goto_5

    nop

    :goto_0
    and-int/lit8 v1, v0, -0x9

    goto :goto_c

    nop

    :goto_1
    if-ne v0, p1, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_6

    nop

    :goto_2
    iput p1, p0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->mFlags:I

    goto :goto_1

    nop

    :goto_3
    return p0

    :goto_4
    goto :goto_e

    nop

    :goto_5
    iget v0, p0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->mFlags:I

    goto :goto_0

    nop

    :goto_6
    const/4 p0, 0x1

    goto :goto_3

    nop

    :goto_7
    goto :goto_a

    :goto_8
    goto :goto_9

    nop

    :goto_9
    const/16 p1, 0x8

    :goto_a
    goto :goto_d

    nop

    :goto_b
    if-nez p1, :cond_1

    goto :goto_8

    :cond_1
    goto :goto_f

    nop

    :goto_c
    const/4 v2, 0x0

    goto :goto_b

    nop

    :goto_d
    or-int/2addr p1, v1

    goto :goto_2

    nop

    :goto_e
    return v2

    :goto_f
    move p1, v2

    goto :goto_7

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_MenuItemImpl__shouldShowShortcut',
        'method': '.method shouldShowShortcut()Z',
        'method_name': 'shouldShowShortcut',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;', 'invoke-virtual {v0}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->isShortcutsVisible()Z', 'if-eqz v0, :cond_0', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->getShortcut()C', 'if-eqz p0, :cond_0', 'return p0', 'return p0'],
        'type': 'method_replace',
        'search': """.method shouldShowShortcut()Z
    .registers 2

    iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    invoke-virtual {v0}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->isShortcutsVisible()Z

    move-result v0

    if-eqz v0, :cond_0

    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->getShortcut()C

    move-result p0

    if-eqz p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method shouldShowShortcut()Z
    .registers 2

    goto :goto_8

    nop

    :goto_0
    if-nez v0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_1

    nop

    :goto_1
    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->getShortcut()C

    move-result p0

    goto :goto_9

    nop

    :goto_2
    return p0

    :goto_3
    return p0

    :goto_4
    goto :goto_7

    nop

    :goto_5
    const/4 p0, 0x1

    goto :goto_3

    nop

    :goto_6
    invoke-virtual {v0}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->isShortcutsVisible()Z

    move-result v0

    goto :goto_0

    nop

    :goto_7
    const/4 p0, 0x0

    goto :goto_2

    nop

    :goto_8
    iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    goto :goto_6

    nop

    :goto_9
    if-nez p0, :cond_1

    goto :goto_4

    :cond_1
    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
