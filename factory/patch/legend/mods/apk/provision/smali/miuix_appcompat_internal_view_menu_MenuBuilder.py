TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/view/menu/MenuBuilder.smali'
CLASS_FALLBACK_NAMES = ['MenuBuilder.smali']
CLASS_ANCHORS = ['.super Lcom/android/internal/view/menu/MenuBuilder;', '.field private static final sCategoryToOrder:[I']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_view_menu_MenuBuilder__dispatchMenuItemSelected',
        'method': '.method dispatchMenuItemSelected(Lmiuix/appcompat/internal/view/menu/MenuBuilder;Landroid/view/MenuItem;)Z',
        'method_name': 'dispatchMenuItemSelected',
        'method_anchors': ['iget-object p0, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mCallback:Lmiuix/appcompat/internal/view/menu/MenuBuilder$Callback;', 'if-eqz p0, :cond_0', 'invoke-interface {p0, p1, p2}, Lmiuix/appcompat/internal/view/menu/MenuBuilder$Callback;->onMenuItemSelected(Lmiuix/appcompat/internal/view/menu/MenuBuilder;Landroid/view/MenuItem;)Z', 'if-eqz p0, :cond_0', 'return p0', 'return p0'],
        'type': 'method_replace',
        'search': """.method dispatchMenuItemSelected(Lmiuix/appcompat/internal/view/menu/MenuBuilder;Landroid/view/MenuItem;)Z
    .registers 3

    iget-object p0, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mCallback:Lmiuix/appcompat/internal/view/menu/MenuBuilder$Callback;

    if-eqz p0, :cond_0

    invoke-interface {p0, p1, p2}, Lmiuix/appcompat/internal/view/menu/MenuBuilder$Callback;->onMenuItemSelected(Lmiuix/appcompat/internal/view/menu/MenuBuilder;Landroid/view/MenuItem;)Z

    move-result p0

    if-eqz p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method dispatchMenuItemSelected(Lmiuix/appcompat/internal/view/menu/MenuBuilder;Landroid/view/MenuItem;)Z
    .registers 3

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mCallback:Lmiuix/appcompat/internal/view/menu/MenuBuilder$Callback;

    goto :goto_3

    nop

    :goto_1
    const/4 p0, 0x1

    goto :goto_5

    nop

    :goto_2
    const/4 p0, 0x0

    goto :goto_7

    nop

    :goto_3
    if-nez p0, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_4

    nop

    :goto_4
    invoke-interface {p0, p1, p2}, Lmiuix/appcompat/internal/view/menu/MenuBuilder$Callback;->onMenuItemSelected(Lmiuix/appcompat/internal/view/menu/MenuBuilder;Landroid/view/MenuItem;)Z

    move-result p0

    goto :goto_8

    nop

    :goto_5
    return p0

    :goto_6
    goto :goto_2

    nop

    :goto_7
    return p0

    :goto_8
    if-nez p0, :cond_1

    goto :goto_6

    :cond_1
    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_MenuBuilder__closeInternal',
        'method': '.method final closeInternal(Z)V',
        'method_name': 'closeInternal',
        'method_anchors': ['iget-boolean v0, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mIsClosing:Z', 'if-eqz v0, :cond_0', 'return-void', 'iput-boolean v0, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mIsClosing:Z', 'iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mPresenters:Ljava/util/concurrent/CopyOnWriteArrayList;', 'invoke-virtual {v0}, Ljava/util/concurrent/CopyOnWriteArrayList;->iterator()Ljava/util/Iterator;', 'invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z', 'if-eqz v1, :cond_2'],
        'type': 'method_replace',
        'search': """.method final closeInternal(Z)V
    .registers 5

    iget-boolean v0, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mIsClosing:Z

    if-eqz v0, :cond_0

    return-void

    :cond_0
    const/4 v0, 0x1

    iput-boolean v0, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mIsClosing:Z

    iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mPresenters:Ljava/util/concurrent/CopyOnWriteArrayList;

    invoke-virtual {v0}, Ljava/util/concurrent/CopyOnWriteArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_0
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_2

    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Ljava/lang/ref/WeakReference;

    invoke-virtual {v1}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;

    move-result-object v2

    check-cast v2, Lmiuix/appcompat/internal/view/menu/MenuPresenter;

    if-nez v2, :cond_1

    iget-object v2, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mPresenters:Ljava/util/concurrent/CopyOnWriteArrayList;

    invoke-virtual {v2, v1}, Ljava/util/concurrent/CopyOnWriteArrayList;->remove(Ljava/lang/Object;)Z

    goto :goto_0

    :cond_1
    invoke-interface {v2, p0, p1}, Lmiuix/appcompat/internal/view/menu/MenuPresenter;->onCloseMenu(Lmiuix/appcompat/internal/view/menu/MenuBuilder;Z)V

    goto :goto_0

    :cond_2
    const/4 p1, 0x0

    iput-boolean p1, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mIsClosing:Z

    return-void
.end method""",
        'replacement': """.method final closeInternal(Z)V
    .registers 5

    goto :goto_8

    nop

    :goto_0
    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    goto :goto_a

    nop

    :goto_1
    invoke-virtual {v0}, Ljava/util/concurrent/CopyOnWriteArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_2
    goto :goto_14

    nop

    :goto_3
    invoke-virtual {v1}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;

    move-result-object v2

    goto :goto_11

    nop

    :goto_4
    iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mPresenters:Ljava/util/concurrent/CopyOnWriteArrayList;

    goto :goto_1

    nop

    :goto_5
    return-void

    :goto_6
    goto :goto_19

    nop

    :goto_7
    iput-boolean p1, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mIsClosing:Z

    goto :goto_17

    nop

    :goto_8
    iget-boolean v0, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mIsClosing:Z

    goto :goto_c

    nop

    :goto_9
    invoke-interface {v2, p0, p1}, Lmiuix/appcompat/internal/view/menu/MenuPresenter;->onCloseMenu(Lmiuix/appcompat/internal/view/menu/MenuBuilder;Z)V

    goto :goto_e

    nop

    :goto_a
    check-cast v1, Ljava/lang/ref/WeakReference;

    goto :goto_3

    nop

    :goto_b
    iget-object v2, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mPresenters:Ljava/util/concurrent/CopyOnWriteArrayList;

    goto :goto_d

    nop

    :goto_c
    if-nez v0, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_5

    nop

    :goto_d
    invoke-virtual {v2, v1}, Ljava/util/concurrent/CopyOnWriteArrayList;->remove(Ljava/lang/Object;)Z

    goto :goto_15

    nop

    :goto_e
    goto :goto_2

    :goto_f
    goto :goto_13

    nop

    :goto_10
    iput-boolean v0, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mIsClosing:Z

    goto :goto_4

    nop

    :goto_11
    check-cast v2, Lmiuix/appcompat/internal/view/menu/MenuPresenter;

    goto :goto_12

    nop

    :goto_12
    if-eqz v2, :cond_1

    goto :goto_16

    :cond_1
    goto :goto_b

    nop

    :goto_13
    const/4 p1, 0x0

    goto :goto_7

    nop

    :goto_14
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    goto :goto_18

    nop

    :goto_15
    goto :goto_2

    :goto_16
    goto :goto_9

    nop

    :goto_17
    return-void

    :goto_18
    if-nez v1, :cond_2

    goto :goto_f

    :cond_2
    goto :goto_0

    nop

    :goto_19
    const/4 v0, 0x1

    goto :goto_10

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_MenuBuilder__findItemWithShortcutForKey',
        'method': '.method findItemWithShortcutForKey(ILandroid/view/KeyEvent;)Lmiuix/appcompat/internal/view/menu/MenuItemImpl;',
        'method_name': 'findItemWithShortcutForKey',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mTempShortcutItemList:Ljava/util/ArrayList;', 'invoke-virtual {v0}, Ljava/util/ArrayList;->clear()V', 'invoke-virtual {p0, v0, p1, p2}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->findItemsWithShortcutForKey(Ljava/util/List;ILandroid/view/KeyEvent;)V', 'invoke-virtual {v0}, Ljava/util/ArrayList;->isEmpty()Z', 'if-eqz v1, :cond_0', 'return-object v2', 'invoke-virtual {p2}, Landroid/view/KeyEvent;->getMetaState()I', 'new-instance v3, Landroid/view/KeyCharacterMap$KeyData;'],
        'type': 'method_replace',
        'search': """.method findItemWithShortcutForKey(ILandroid/view/KeyEvent;)Lmiuix/appcompat/internal/view/menu/MenuItemImpl;
    .registers 13

    iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mTempShortcutItemList:Ljava/util/ArrayList;

    invoke-virtual {v0}, Ljava/util/ArrayList;->clear()V

    invoke-virtual {p0, v0, p1, p2}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->findItemsWithShortcutForKey(Ljava/util/List;ILandroid/view/KeyEvent;)V

    invoke-virtual {v0}, Ljava/util/ArrayList;->isEmpty()Z

    move-result v1

    const/4 v2, 0x0

    if-eqz v1, :cond_0

    return-object v2

    :cond_0
    invoke-virtual {p2}, Landroid/view/KeyEvent;->getMetaState()I

    move-result v1

    new-instance v3, Landroid/view/KeyCharacterMap$KeyData;

    invoke-direct {v3}, Landroid/view/KeyCharacterMap$KeyData;-><init>()V

    invoke-virtual {p2, v3}, Landroid/view/KeyEvent;->getKeyData(Landroid/view/KeyCharacterMap$KeyData;)Z

    invoke-virtual {v0}, Ljava/util/ArrayList;->size()I

    move-result p2

    const/4 v4, 0x1

    const/4 v5, 0x0

    if-ne p2, v4, :cond_1

    invoke-virtual {v0, v5}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object p0

    check-cast p0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;

    return-object p0

    :cond_1
    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->isQwertyMode()Z

    move-result p0

    invoke-virtual {v0}, Ljava/util/ArrayList;->size()I

    move-result p2

    move v4, v5

    :cond_2
    if-ge v4, p2, :cond_7

    invoke-virtual {v0, v4}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v6

    add-int/lit8 v4, v4, 0x1

    check-cast v6, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;

    if-eqz p0, :cond_3

    invoke-virtual {v6}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->getAlphabeticShortcut()C

    move-result v7

    goto :goto_0

    :cond_3
    invoke-virtual {v6}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->getNumericShortcut()C

    move-result v7

    :goto_0
    iget-object v8, v3, Landroid/view/KeyCharacterMap$KeyData;->meta:[C

    aget-char v9, v8, v5

    if-ne v7, v9, :cond_4

    and-int/lit8 v9, v1, 0x2

    if-eqz v9, :cond_6

    :cond_4
    const/4 v9, 0x2

    aget-char v8, v8, v9

    if-ne v7, v8, :cond_5

    and-int/lit8 v8, v1, 0x2

    if-nez v8, :cond_6

    :cond_5
    if-eqz p0, :cond_2

    const/16 v8, 0x8

    if-ne v7, v8, :cond_2

    const/16 v7, 0x43

    if-ne p1, v7, :cond_2

    :cond_6
    return-object v6

    :cond_7
    return-object v2
.end method""",
        'replacement': """.method findItemWithShortcutForKey(ILandroid/view/KeyEvent;)Lmiuix/appcompat/internal/view/menu/MenuItemImpl;
    .registers 13

    goto :goto_1d

    nop

    :goto_0
    move v4, v5

    :goto_1
    goto :goto_3

    nop

    :goto_2
    and-int/lit8 v9, v1, 0x2

    goto :goto_34

    nop

    :goto_3
    if-lt v4, p2, :cond_0

    goto :goto_b

    :cond_0
    goto :goto_2d

    nop

    :goto_4
    if-nez v1, :cond_1

    goto :goto_9

    :cond_1
    goto :goto_8

    nop

    :goto_5
    goto :goto_29

    :goto_6
    goto :goto_28

    nop

    :goto_7
    invoke-virtual {p2, v3}, Landroid/view/KeyEvent;->getKeyData(Landroid/view/KeyCharacterMap$KeyData;)Z

    goto :goto_11

    nop

    :goto_8
    return-object v2

    :goto_9
    goto :goto_15

    nop

    :goto_a
    return-object v6

    :goto_b
    goto :goto_1e

    nop

    :goto_c
    add-int/lit8 v4, v4, 0x1

    goto :goto_16

    nop

    :goto_d
    const/4 v9, 0x2

    goto :goto_18

    nop

    :goto_e
    const/4 v4, 0x1

    goto :goto_2e

    nop

    :goto_f
    iget-object v8, v3, Landroid/view/KeyCharacterMap$KeyData;->meta:[C

    goto :goto_2f

    nop

    :goto_10
    if-nez p0, :cond_2

    goto :goto_6

    :cond_2
    goto :goto_14

    nop

    :goto_11
    invoke-virtual {v0}, Ljava/util/ArrayList;->size()I

    move-result p2

    goto :goto_e

    nop

    :goto_12
    invoke-virtual {p0, v0, p1, p2}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->findItemsWithShortcutForKey(Ljava/util/List;ILandroid/view/KeyEvent;)V

    goto :goto_1b

    nop

    :goto_13
    invoke-virtual {v0}, Ljava/util/ArrayList;->clear()V

    goto :goto_12

    nop

    :goto_14
    invoke-virtual {v6}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->getAlphabeticShortcut()C

    move-result v7

    goto :goto_5

    nop

    :goto_15
    invoke-virtual {p2}, Landroid/view/KeyEvent;->getMetaState()I

    move-result v1

    goto :goto_32

    nop

    :goto_16
    check-cast v6, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;

    goto :goto_10

    nop

    :goto_17
    const/4 v2, 0x0

    goto :goto_4

    nop

    :goto_18
    aget-char v8, v8, v9

    goto :goto_26

    nop

    :goto_19
    return-object p0

    :goto_1a
    goto :goto_1c

    nop

    :goto_1b
    invoke-virtual {v0}, Ljava/util/ArrayList;->isEmpty()Z

    move-result v1

    goto :goto_17

    nop

    :goto_1c
    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->isQwertyMode()Z

    move-result p0

    goto :goto_20

    nop

    :goto_1d
    iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mTempShortcutItemList:Ljava/util/ArrayList;

    goto :goto_13

    nop

    :goto_1e
    return-object v2

    :goto_1f
    and-int/lit8 v8, v1, 0x2

    goto :goto_2a

    nop

    :goto_20
    invoke-virtual {v0}, Ljava/util/ArrayList;->size()I

    move-result p2

    goto :goto_0

    nop

    :goto_21
    if-eq v7, v8, :cond_3

    goto :goto_1

    :cond_3
    goto :goto_27

    nop

    :goto_22
    invoke-direct {v3}, Landroid/view/KeyCharacterMap$KeyData;-><init>()V

    goto :goto_7

    nop

    :goto_23
    if-eq p1, v7, :cond_4

    goto :goto_1

    :cond_4
    :goto_24
    goto :goto_a

    nop

    :goto_25
    if-eq p2, v4, :cond_5

    goto :goto_1a

    :cond_5
    goto :goto_2c

    nop

    :goto_26
    if-eq v7, v8, :cond_6

    goto :goto_2b

    :cond_6
    goto :goto_1f

    nop

    :goto_27
    const/16 v7, 0x43

    goto :goto_23

    nop

    :goto_28
    invoke-virtual {v6}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->getNumericShortcut()C

    move-result v7

    :goto_29
    goto :goto_f

    nop

    :goto_2a
    if-eqz v8, :cond_7

    goto :goto_24

    :cond_7
    :goto_2b
    goto :goto_33

    nop

    :goto_2c
    invoke-virtual {v0, v5}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object p0

    goto :goto_30

    nop

    :goto_2d
    invoke-virtual {v0, v4}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v6

    goto :goto_c

    nop

    :goto_2e
    const/4 v5, 0x0

    goto :goto_25

    nop

    :goto_2f
    aget-char v9, v8, v5

    goto :goto_36

    nop

    :goto_30
    check-cast p0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;

    goto :goto_19

    nop

    :goto_31
    const/16 v8, 0x8

    goto :goto_21

    nop

    :goto_32
    new-instance v3, Landroid/view/KeyCharacterMap$KeyData;

    goto :goto_22

    nop

    :goto_33
    if-nez p0, :cond_8

    goto :goto_1

    :cond_8
    goto :goto_31

    nop

    :goto_34
    if-nez v9, :cond_9

    goto :goto_24

    :cond_9
    :goto_35
    goto :goto_d

    nop

    :goto_36
    if-eq v7, v9, :cond_a

    goto :goto_35

    :cond_a
    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_MenuBuilder__findItemsWithShortcutForKey',
        'method': '.method findItemsWithShortcutForKey(Ljava/util/List;ILandroid/view/KeyEvent;)V',
        'method_name': 'findItemsWithShortcutForKey',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->isQwertyMode()Z', 'invoke-virtual {p3}, Landroid/view/KeyEvent;->getMetaState()I', 'new-instance v2, Landroid/view/KeyCharacterMap$KeyData;', 'invoke-direct {v2}, Landroid/view/KeyCharacterMap$KeyData;-><init>()V', 'invoke-virtual {p3, v2}, Landroid/view/KeyEvent;->getKeyData(Landroid/view/KeyCharacterMap$KeyData;)Z', 'if-nez v3, :cond_0', 'if-eq p2, v4, :cond_0', 'iget-object p0, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mItems:Ljava/util/ArrayList;'],
        'type': 'method_replace',
        'search': """.method findItemsWithShortcutForKey(Ljava/util/List;ILandroid/view/KeyEvent;)V
    .registers 15

    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->isQwertyMode()Z

    move-result v0

    invoke-virtual {p3}, Landroid/view/KeyEvent;->getMetaState()I

    move-result v1

    new-instance v2, Landroid/view/KeyCharacterMap$KeyData;

    invoke-direct {v2}, Landroid/view/KeyCharacterMap$KeyData;-><init>()V

    invoke-virtual {p3, v2}, Landroid/view/KeyEvent;->getKeyData(Landroid/view/KeyCharacterMap$KeyData;)Z

    move-result v3

    const/16 v4, 0x43

    if-nez v3, :cond_0

    if-eq p2, v4, :cond_0

    goto :goto_2

    :cond_0
    iget-object p0, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mItems:Ljava/util/ArrayList;

    invoke-virtual {p0}, Ljava/util/ArrayList;->size()I

    move-result v3

    const/4 v5, 0x0

    move v6, v5

    :cond_1
    :goto_0
    if-ge v6, v3, :cond_5

    invoke-virtual {p0, v6}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v7

    add-int/lit8 v6, v6, 0x1

    check-cast v7, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;

    invoke-virtual {v7}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->hasSubMenu()Z

    move-result v8

    if-eqz v8, :cond_2

    invoke-virtual {v7}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->getSubMenu()Landroid/view/SubMenu;

    move-result-object v8

    check-cast v8, Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    invoke-virtual {v8, p1, p2, p3}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->findItemsWithShortcutForKey(Ljava/util/List;ILandroid/view/KeyEvent;)V

    :cond_2
    if-eqz v0, :cond_3

    invoke-virtual {v7}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->getAlphabeticShortcut()C

    move-result v8

    goto :goto_1

    :cond_3
    invoke-virtual {v7}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->getNumericShortcut()C

    move-result v8

    :goto_1
    and-int/lit8 v9, v1, 0x5

    if-nez v9, :cond_1

    if-eqz v8, :cond_1

    iget-object v9, v2, Landroid/view/KeyCharacterMap$KeyData;->meta:[C

    aget-char v10, v9, v5

    if-eq v8, v10, :cond_4

    const/4 v10, 0x2

    aget-char v9, v9, v10

    if-eq v8, v9, :cond_4

    if-eqz v0, :cond_1

    const/16 v9, 0x8

    if-ne v8, v9, :cond_1

    if-ne p2, v4, :cond_1

    :cond_4
    invoke-virtual {v7}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->isEnabled()Z

    move-result v8

    if-eqz v8, :cond_1

    invoke-interface {p1, v7}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    goto :goto_0

    :cond_5
    :goto_2
    return-void
.end method""",
        'replacement': """.method findItemsWithShortcutForKey(Ljava/util/List;ILandroid/view/KeyEvent;)V
    .registers 15

    goto :goto_6

    nop

    :goto_0
    if-eqz v9, :cond_0

    goto :goto_16

    :cond_0
    goto :goto_14

    nop

    :goto_1
    if-nez v0, :cond_1

    goto :goto_1a

    :cond_1
    goto :goto_8

    nop

    :goto_2
    if-eq v8, v9, :cond_2

    goto :goto_16

    :cond_2
    goto :goto_2c

    nop

    :goto_3
    aget-char v9, v9, v10

    goto :goto_10

    nop

    :goto_4
    if-ne p2, v4, :cond_3

    goto :goto_24

    :cond_3
    goto :goto_23

    nop

    :goto_5
    if-eqz v3, :cond_4

    goto :goto_24

    :cond_4
    goto :goto_4

    nop

    :goto_6
    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->isQwertyMode()Z

    move-result v0

    goto :goto_f

    nop

    :goto_7
    and-int/lit8 v9, v1, 0x5

    goto :goto_0

    nop

    :goto_8
    invoke-virtual {v7}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->getAlphabeticShortcut()C

    move-result v8

    goto :goto_19

    nop

    :goto_9
    invoke-virtual {v8, p1, p2, p3}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->findItemsWithShortcutForKey(Ljava/util/List;ILandroid/view/KeyEvent;)V

    :goto_a
    goto :goto_1

    nop

    :goto_b
    check-cast v8, Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    goto :goto_9

    nop

    :goto_c
    if-ne v8, v10, :cond_5

    goto :goto_2d

    :cond_5
    goto :goto_1c

    nop

    :goto_d
    invoke-direct {v2}, Landroid/view/KeyCharacterMap$KeyData;-><init>()V

    goto :goto_2b

    nop

    :goto_e
    if-nez v8, :cond_6

    goto :goto_16

    :cond_6
    goto :goto_2e

    nop

    :goto_f
    invoke-virtual {p3}, Landroid/view/KeyEvent;->getMetaState()I

    move-result v1

    goto :goto_32

    nop

    :goto_10
    if-ne v8, v9, :cond_7

    goto :goto_2d

    :cond_7
    goto :goto_13

    nop

    :goto_11
    return-void

    :goto_12
    invoke-virtual {v7}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->hasSubMenu()Z

    move-result v8

    goto :goto_30

    nop

    :goto_13
    if-nez v0, :cond_8

    goto :goto_16

    :cond_8
    goto :goto_1d

    nop

    :goto_14
    if-nez v8, :cond_9

    goto :goto_16

    :cond_9
    goto :goto_2f

    nop

    :goto_15
    move v6, v5

    :goto_16
    goto :goto_1e

    nop

    :goto_17
    invoke-virtual {v7}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->getNumericShortcut()C

    move-result v8

    :goto_18
    goto :goto_7

    nop

    :goto_19
    goto :goto_18

    :goto_1a
    goto :goto_17

    nop

    :goto_1b
    invoke-virtual {v7}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->getSubMenu()Landroid/view/SubMenu;

    move-result-object v8

    goto :goto_b

    nop

    :goto_1c
    const/4 v10, 0x2

    goto :goto_3

    nop

    :goto_1d
    const/16 v9, 0x8

    goto :goto_2

    nop

    :goto_1e
    if-lt v6, v3, :cond_a

    goto :goto_20

    :cond_a
    goto :goto_29

    nop

    :goto_1f
    goto :goto_16

    :goto_20
    goto :goto_11

    nop

    :goto_21
    const/4 v5, 0x0

    goto :goto_15

    nop

    :goto_22
    invoke-virtual {p0}, Ljava/util/ArrayList;->size()I

    move-result v3

    goto :goto_21

    nop

    :goto_23
    goto :goto_20

    :goto_24
    goto :goto_31

    nop

    :goto_25
    add-int/lit8 v6, v6, 0x1

    goto :goto_27

    nop

    :goto_26
    invoke-virtual {v7}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->isEnabled()Z

    move-result v8

    goto :goto_e

    nop

    :goto_27
    check-cast v7, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;

    goto :goto_12

    nop

    :goto_28
    const/16 v4, 0x43

    goto :goto_5

    nop

    :goto_29
    invoke-virtual {p0, v6}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v7

    goto :goto_25

    nop

    :goto_2a
    aget-char v10, v9, v5

    goto :goto_c

    nop

    :goto_2b
    invoke-virtual {p3, v2}, Landroid/view/KeyEvent;->getKeyData(Landroid/view/KeyCharacterMap$KeyData;)Z

    move-result v3

    goto :goto_28

    nop

    :goto_2c
    if-eq p2, v4, :cond_b

    goto :goto_16

    :cond_b
    :goto_2d
    goto :goto_26

    nop

    :goto_2e
    invoke-interface {p1, v7}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    goto :goto_1f

    nop

    :goto_2f
    iget-object v9, v2, Landroid/view/KeyCharacterMap$KeyData;->meta:[C

    goto :goto_2a

    nop

    :goto_30
    if-nez v8, :cond_c

    goto :goto_a

    :cond_c
    goto :goto_1b

    nop

    :goto_31
    iget-object p0, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mItems:Ljava/util/ArrayList;

    goto :goto_22

    nop

    :goto_32
    new-instance v2, Landroid/view/KeyCharacterMap$KeyData;

    goto :goto_d

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_MenuBuilder__getOptionalIconsVisible',
        'method': '.method getOptionalIconsVisible()Z',
        'method_name': 'getOptionalIconsVisible',
        'method_anchors': ['iget-boolean p0, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mOptionalIconsVisible:Z', 'return p0'],
        'type': 'method_replace',
        'search': """.method getOptionalIconsVisible()Z
    .registers 1

    iget-boolean p0, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mOptionalIconsVisible:Z

    return p0
.end method""",
        'replacement': """.method getOptionalIconsVisible()Z
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget-boolean p0, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mOptionalIconsVisible:Z

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
        'id': 'miuix_appcompat_internal_view_menu_MenuBuilder__getResources',
        'method': '.method getResources()Landroid/content/res/Resources;',
        'method_name': 'getResources',
        'method_anchors': ['iget-object p0, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mResources:Landroid/content/res/Resources;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method getResources()Landroid/content/res/Resources;
    .registers 1

    iget-object p0, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mResources:Landroid/content/res/Resources;

    return-object p0
.end method""",
        'replacement': """.method getResources()Landroid/content/res/Resources;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    iget-object p0, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mResources:Landroid/content/res/Resources;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_MenuBuilder__isQwertyMode',
        'method': '.method isQwertyMode()Z',
        'method_name': 'isQwertyMode',
        'method_anchors': ['iget-boolean p0, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mQwertyMode:Z', 'return p0'],
        'type': 'method_replace',
        'search': """.method isQwertyMode()Z
    .registers 1

    iget-boolean p0, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mQwertyMode:Z

    return p0
.end method""",
        'replacement': """.method isQwertyMode()Z
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    iget-boolean p0, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mQwertyMode:Z

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_MenuBuilder__onItemActionRequestChanged',
        'method': '.method onItemActionRequestChanged(Lmiuix/appcompat/internal/view/menu/MenuItemImpl;)V',
        'method_name': 'onItemActionRequestChanged',
        'method_anchors': ['iput-boolean p1, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mIsActionItemsStale:Z', 'invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->onItemsChanged(Z)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method onItemActionRequestChanged(Lmiuix/appcompat/internal/view/menu/MenuItemImpl;)V
    .registers 2

    const/4 p1, 0x1

    iput-boolean p1, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mIsActionItemsStale:Z

    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->onItemsChanged(Z)V

    return-void
.end method""",
        'replacement': """.method onItemActionRequestChanged(Lmiuix/appcompat/internal/view/menu/MenuItemImpl;)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    const/4 p1, 0x1

    goto :goto_2

    nop

    :goto_2
    iput-boolean p1, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mIsActionItemsStale:Z

    goto :goto_3

    nop

    :goto_3
    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->onItemsChanged(Z)V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_MenuBuilder__onItemVisibleChanged',
        'method': '.method onItemVisibleChanged(Lmiuix/appcompat/internal/view/menu/MenuItemImpl;)V',
        'method_name': 'onItemVisibleChanged',
        'method_anchors': ['iput-boolean p1, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mIsVisibleItemsStale:Z', 'invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->onItemsChanged(Z)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method onItemVisibleChanged(Lmiuix/appcompat/internal/view/menu/MenuItemImpl;)V
    .registers 2

    const/4 p1, 0x1

    iput-boolean p1, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mIsVisibleItemsStale:Z

    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->onItemsChanged(Z)V

    return-void
.end method""",
        'replacement': """.method onItemVisibleChanged(Lmiuix/appcompat/internal/view/menu/MenuItemImpl;)V
    .registers 2

    goto :goto_2

    nop

    :goto_0
    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->onItemsChanged(Z)V

    goto :goto_1

    nop

    :goto_1
    return-void

    :goto_2
    const/4 p1, 0x1

    goto :goto_3

    nop

    :goto_3
    iput-boolean p1, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mIsVisibleItemsStale:Z

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_MenuBuilder__addInternal',
        'method': '.method protected addInternal(IIILjava/lang/CharSequence;)Landroid/view/MenuItem;',
        'method_name': 'addInternal',
        'method_anchors': ['invoke-static {p3}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->getOrdering(I)I', 'new-instance v0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;', 'iget v7, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mDefaultShowAsAction:I', 'invoke-direct/range {v0 .. v7}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;-><init>(Lmiuix/appcompat/internal/view/menu/MenuBuilder;IIIILjava/lang/CharSequence;I)V', 'iget-object p0, v1, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mCurrentMenuInfo:Landroid/view/ContextMenu$ContextMenuInfo;', 'if-eqz p0, :cond_0', 'invoke-virtual {v0, p0}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->setMenuInfo(Landroid/view/ContextMenu$ContextMenuInfo;)V', 'iget-object p0, v1, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mItems:Ljava/util/ArrayList;'],
        'type': 'method_replace',
        'search': """.method protected addInternal(IIILjava/lang/CharSequence;)Landroid/view/MenuItem;
    .registers 13

    invoke-static {p3}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->getOrdering(I)I

    move-result v5

    new-instance v0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;

    iget v7, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mDefaultShowAsAction:I

    move-object v1, p0

    move v2, p1

    move v3, p2

    move v4, p3

    move-object v6, p4

    invoke-direct/range {v0 .. v7}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;-><init>(Lmiuix/appcompat/internal/view/menu/MenuBuilder;IIIILjava/lang/CharSequence;I)V

    iget-object p0, v1, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mCurrentMenuInfo:Landroid/view/ContextMenu$ContextMenuInfo;

    if-eqz p0, :cond_0

    invoke-virtual {v0, p0}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->setMenuInfo(Landroid/view/ContextMenu$ContextMenuInfo;)V

    :cond_0
    iget-object p0, v1, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mItems:Ljava/util/ArrayList;

    invoke-static {p0, v5}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->findInsertIndex(Ljava/util/ArrayList;I)I

    move-result p1

    invoke-virtual {p0, p1, v0}, Ljava/util/ArrayList;->add(ILjava/lang/Object;)V

    const/4 p0, 0x1

    invoke-virtual {v1, p0}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->onItemsChanged(Z)V

    return-object v0
.end method""",
        'replacement': """.method protected addInternal(IIILjava/lang/CharSequence;)Landroid/view/MenuItem;
    .registers 13

    goto :goto_12

    nop

    :goto_0
    iget-object p0, v1, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mItems:Ljava/util/ArrayList;

    goto :goto_6

    nop

    :goto_1
    if-nez p0, :cond_0

    goto :goto_d

    :cond_0
    goto :goto_c

    nop

    :goto_2
    move v4, p3

    goto :goto_7

    nop

    :goto_3
    invoke-virtual {p0, p1, v0}, Ljava/util/ArrayList;->add(ILjava/lang/Object;)V

    goto :goto_11

    nop

    :goto_4
    move-object v1, p0

    goto :goto_a

    nop

    :goto_5
    return-object v0

    :goto_6
    invoke-static {p0, v5}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->findInsertIndex(Ljava/util/ArrayList;I)I

    move-result p1

    goto :goto_3

    nop

    :goto_7
    move-object v6, p4

    goto :goto_9

    nop

    :goto_8
    new-instance v0, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;

    goto :goto_e

    nop

    :goto_9
    invoke-direct/range {v0 .. v7}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;-><init>(Lmiuix/appcompat/internal/view/menu/MenuBuilder;IIIILjava/lang/CharSequence;I)V

    goto :goto_10

    nop

    :goto_a
    move v2, p1

    goto :goto_b

    nop

    :goto_b
    move v3, p2

    goto :goto_2

    nop

    :goto_c
    invoke-virtual {v0, p0}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->setMenuInfo(Landroid/view/ContextMenu$ContextMenuInfo;)V

    :goto_d
    goto :goto_0

    nop

    :goto_e
    iget v7, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mDefaultShowAsAction:I

    goto :goto_4

    nop

    :goto_f
    invoke-virtual {v1, p0}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->onItemsChanged(Z)V

    goto :goto_5

    nop

    :goto_10
    iget-object p0, v1, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mCurrentMenuInfo:Landroid/view/ContextMenu$ContextMenuInfo;

    goto :goto_1

    nop

    :goto_11
    const/4 p0, 0x1

    goto :goto_f

    nop

    :goto_12
    invoke-static {p3}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->getOrdering(I)I

    move-result v5

    goto :goto_8

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_MenuBuilder__getActionViewStatesKey',
        'method': '.method protected getActionViewStatesKey()Ljava/lang/String;',
        'method_name': 'getActionViewStatesKey',
        'method_anchors': ['const-string p0, "android:menu:actionviewstates"', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getActionViewStatesKey()Ljava/lang/String;
    .registers 1

    const-string p0, "android:menu:actionviewstates"

    return-object p0
.end method""",
        'replacement': """.method protected getActionViewStatesKey()Ljava/lang/String;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    const-string p0, "android:menu:actionviewstates"

    goto :goto_1

    nop

    :goto_1
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_MenuBuilder__onItemsChanged',
        'method': '.method protected onItemsChanged(Z)V',
        'method_name': 'onItemsChanged',
        'method_anchors': ['iget-boolean v0, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mPreventDispatchingItemsChanged:Z', 'if-nez v0, :cond_1', 'if-eqz p1, :cond_0', 'iput-boolean v1, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mIsVisibleItemsStale:Z', 'iput-boolean v1, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mIsActionItemsStale:Z', 'invoke-direct {p0, p1}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->dispatchPresenterUpdate(Z)V', 'return-void', 'iput-boolean v1, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mItemsChangedWhileDispatchPrevented:Z'],
        'type': 'method_replace',
        'search': """.method protected onItemsChanged(Z)V
    .registers 4

    iget-boolean v0, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mPreventDispatchingItemsChanged:Z

    const/4 v1, 0x1

    if-nez v0, :cond_1

    if-eqz p1, :cond_0

    iput-boolean v1, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mIsVisibleItemsStale:Z

    iput-boolean v1, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mIsActionItemsStale:Z

    :cond_0
    invoke-direct {p0, p1}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->dispatchPresenterUpdate(Z)V

    return-void

    :cond_1
    iput-boolean v1, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mItemsChangedWhileDispatchPrevented:Z

    return-void
.end method""",
        'replacement': """.method protected onItemsChanged(Z)V
    .registers 4

    goto :goto_5

    nop

    :goto_0
    iput-boolean v1, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mIsActionItemsStale:Z

    :goto_1
    goto :goto_b

    nop

    :goto_2
    if-nez p1, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_4

    nop

    :goto_3
    iput-boolean v1, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mItemsChangedWhileDispatchPrevented:Z

    goto :goto_7

    nop

    :goto_4
    iput-boolean v1, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mIsVisibleItemsStale:Z

    goto :goto_0

    nop

    :goto_5
    iget-boolean v0, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mPreventDispatchingItemsChanged:Z

    goto :goto_a

    nop

    :goto_6
    if-eqz v0, :cond_1

    goto :goto_9

    :cond_1
    goto :goto_2

    nop

    :goto_7
    return-void

    :goto_8
    return-void

    :goto_9
    goto :goto_3

    nop

    :goto_a
    const/4 v1, 0x1

    goto :goto_6

    nop

    :goto_b
    invoke-direct {p0, p1}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->dispatchPresenterUpdate(Z)V

    goto :goto_8

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_MenuBuilder__setHeaderIconInt',
        'method': '.method protected setHeaderIconInt(I)Lmiuix/appcompat/internal/view/menu/MenuBuilder;',
        'method_name': 'setHeaderIconInt',
        'method_anchors': ['invoke-direct/range {v0 .. v5}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->setHeaderInternal(ILjava/lang/CharSequence;ILandroid/graphics/drawable/Drawable;Landroid/view/View;)V', 'return-object v0'],
        'type': 'method_replace',
        'search': """.method protected setHeaderIconInt(I)Lmiuix/appcompat/internal/view/menu/MenuBuilder;
    .registers 8

    const/4 v4, 0x0

    const/4 v5, 0x0

    const/4 v1, 0x0

    const/4 v2, 0x0

    move-object v0, p0

    move v3, p1

    invoke-direct/range {v0 .. v5}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->setHeaderInternal(ILjava/lang/CharSequence;ILandroid/graphics/drawable/Drawable;Landroid/view/View;)V

    return-object v0
.end method""",
        'replacement': """.method protected setHeaderIconInt(I)Lmiuix/appcompat/internal/view/menu/MenuBuilder;
    .registers 8

    goto :goto_5

    nop

    :goto_0
    move-object v0, p0

    goto :goto_1

    nop

    :goto_1
    move v3, p1

    goto :goto_6

    nop

    :goto_2
    const/4 v5, 0x0

    goto :goto_3

    nop

    :goto_3
    const/4 v1, 0x0

    goto :goto_4

    nop

    :goto_4
    const/4 v2, 0x0

    goto :goto_0

    nop

    :goto_5
    const/4 v4, 0x0

    goto :goto_2

    nop

    :goto_6
    invoke-direct/range {v0 .. v5}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->setHeaderInternal(ILjava/lang/CharSequence;ILandroid/graphics/drawable/Drawable;Landroid/view/View;)V

    goto :goto_7

    nop

    :goto_7
    return-object v0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_MenuBuilder__setHeaderIconInt',
        'method': '.method protected setHeaderIconInt(Landroid/graphics/drawable/Drawable;)Lmiuix/appcompat/internal/view/menu/MenuBuilder;',
        'method_name': 'setHeaderIconInt',
        'method_anchors': ['invoke-direct/range {v0 .. v5}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->setHeaderInternal(ILjava/lang/CharSequence;ILandroid/graphics/drawable/Drawable;Landroid/view/View;)V', 'return-object v0'],
        'type': 'method_replace',
        'search': """.method protected setHeaderIconInt(Landroid/graphics/drawable/Drawable;)Lmiuix/appcompat/internal/view/menu/MenuBuilder;
    .registers 8

    const/4 v3, 0x0

    const/4 v5, 0x0

    const/4 v1, 0x0

    const/4 v2, 0x0

    move-object v0, p0

    move-object v4, p1

    invoke-direct/range {v0 .. v5}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->setHeaderInternal(ILjava/lang/CharSequence;ILandroid/graphics/drawable/Drawable;Landroid/view/View;)V

    return-object v0
.end method""",
        'replacement': """.method protected setHeaderIconInt(Landroid/graphics/drawable/Drawable;)Lmiuix/appcompat/internal/view/menu/MenuBuilder;
    .registers 8

    goto :goto_6

    nop

    :goto_0
    const/4 v5, 0x0

    goto :goto_7

    nop

    :goto_1
    invoke-direct/range {v0 .. v5}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->setHeaderInternal(ILjava/lang/CharSequence;ILandroid/graphics/drawable/Drawable;Landroid/view/View;)V

    goto :goto_4

    nop

    :goto_2
    const/4 v2, 0x0

    goto :goto_3

    nop

    :goto_3
    move-object v0, p0

    goto :goto_5

    nop

    :goto_4
    return-object v0

    :goto_5
    move-object v4, p1

    goto :goto_1

    nop

    :goto_6
    const/4 v3, 0x0

    goto :goto_0

    nop

    :goto_7
    const/4 v1, 0x0

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_MenuBuilder__setHeaderTitleInt',
        'method': '.method protected setHeaderTitleInt(I)Lmiuix/appcompat/internal/view/menu/MenuBuilder;',
        'method_name': 'setHeaderTitleInt',
        'method_anchors': ['invoke-direct/range {v0 .. v5}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->setHeaderInternal(ILjava/lang/CharSequence;ILandroid/graphics/drawable/Drawable;Landroid/view/View;)V', 'return-object v0'],
        'type': 'method_replace',
        'search': """.method protected setHeaderTitleInt(I)Lmiuix/appcompat/internal/view/menu/MenuBuilder;
    .registers 8

    const/4 v4, 0x0

    const/4 v5, 0x0

    const/4 v2, 0x0

    const/4 v3, 0x0

    move-object v0, p0

    move v1, p1

    invoke-direct/range {v0 .. v5}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->setHeaderInternal(ILjava/lang/CharSequence;ILandroid/graphics/drawable/Drawable;Landroid/view/View;)V

    return-object v0
.end method""",
        'replacement': """.method protected setHeaderTitleInt(I)Lmiuix/appcompat/internal/view/menu/MenuBuilder;
    .registers 8

    goto :goto_2

    nop

    :goto_0
    move-object v0, p0

    goto :goto_7

    nop

    :goto_1
    const/4 v2, 0x0

    goto :goto_4

    nop

    :goto_2
    const/4 v4, 0x0

    goto :goto_5

    nop

    :goto_3
    return-object v0

    :goto_4
    const/4 v3, 0x0

    goto :goto_0

    nop

    :goto_5
    const/4 v5, 0x0

    goto :goto_1

    nop

    :goto_6
    invoke-direct/range {v0 .. v5}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->setHeaderInternal(ILjava/lang/CharSequence;ILandroid/graphics/drawable/Drawable;Landroid/view/View;)V

    goto :goto_3

    nop

    :goto_7
    move v1, p1

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_MenuBuilder__setHeaderTitleInt',
        'method': '.method protected setHeaderTitleInt(Ljava/lang/CharSequence;)Lmiuix/appcompat/internal/view/menu/MenuBuilder;',
        'method_name': 'setHeaderTitleInt',
        'method_anchors': ['invoke-direct/range {v0 .. v5}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->setHeaderInternal(ILjava/lang/CharSequence;ILandroid/graphics/drawable/Drawable;Landroid/view/View;)V', 'return-object v0'],
        'type': 'method_replace',
        'search': """.method protected setHeaderTitleInt(Ljava/lang/CharSequence;)Lmiuix/appcompat/internal/view/menu/MenuBuilder;
    .registers 8

    const/4 v4, 0x0

    const/4 v5, 0x0

    const/4 v1, 0x0

    const/4 v3, 0x0

    move-object v0, p0

    move-object v2, p1

    invoke-direct/range {v0 .. v5}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->setHeaderInternal(ILjava/lang/CharSequence;ILandroid/graphics/drawable/Drawable;Landroid/view/View;)V

    return-object v0
.end method""",
        'replacement': """.method protected setHeaderTitleInt(Ljava/lang/CharSequence;)Lmiuix/appcompat/internal/view/menu/MenuBuilder;
    .registers 8

    goto :goto_4

    nop

    :goto_0
    return-object v0

    :goto_1
    const/4 v3, 0x0

    goto :goto_2

    nop

    :goto_2
    move-object v0, p0

    goto :goto_3

    nop

    :goto_3
    move-object v2, p1

    goto :goto_5

    nop

    :goto_4
    const/4 v4, 0x0

    goto :goto_7

    nop

    :goto_5
    invoke-direct/range {v0 .. v5}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->setHeaderInternal(ILjava/lang/CharSequence;ILandroid/graphics/drawable/Drawable;Landroid/view/View;)V

    goto :goto_0

    nop

    :goto_6
    const/4 v1, 0x0

    goto :goto_1

    nop

    :goto_7
    const/4 v5, 0x0

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_MenuBuilder__setHeaderViewInt',
        'method': '.method protected setHeaderViewInt(Landroid/view/View;)Lmiuix/appcompat/internal/view/menu/MenuBuilder;',
        'method_name': 'setHeaderViewInt',
        'method_anchors': ['invoke-direct/range {v0 .. v5}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->setHeaderInternal(ILjava/lang/CharSequence;ILandroid/graphics/drawable/Drawable;Landroid/view/View;)V', 'return-object v0'],
        'type': 'method_replace',
        'search': """.method protected setHeaderViewInt(Landroid/view/View;)Lmiuix/appcompat/internal/view/menu/MenuBuilder;
    .registers 8

    const/4 v3, 0x0

    const/4 v4, 0x0

    const/4 v1, 0x0

    const/4 v2, 0x0

    move-object v0, p0

    move-object v5, p1

    invoke-direct/range {v0 .. v5}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->setHeaderInternal(ILjava/lang/CharSequence;ILandroid/graphics/drawable/Drawable;Landroid/view/View;)V

    return-object v0
.end method""",
        'replacement': """.method protected setHeaderViewInt(Landroid/view/View;)Lmiuix/appcompat/internal/view/menu/MenuBuilder;
    .registers 8

    goto :goto_2

    nop

    :goto_0
    invoke-direct/range {v0 .. v5}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->setHeaderInternal(ILjava/lang/CharSequence;ILandroid/graphics/drawable/Drawable;Landroid/view/View;)V

    goto :goto_4

    nop

    :goto_1
    move-object v0, p0

    goto :goto_3

    nop

    :goto_2
    const/4 v3, 0x0

    goto :goto_6

    nop

    :goto_3
    move-object v5, p1

    goto :goto_0

    nop

    :goto_4
    return-object v0

    :goto_5
    const/4 v2, 0x0

    goto :goto_1

    nop

    :goto_6
    const/4 v4, 0x0

    goto :goto_7

    nop

    :goto_7
    const/4 v1, 0x0

    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_MenuBuilder__setExclusiveItemChecked',
        'method': '.method setExclusiveItemChecked(Landroid/view/MenuItem;)V',
        'method_name': 'setExclusiveItemChecked',
        'method_anchors': ['invoke-interface {p1}, Landroid/view/MenuItem;->getGroupId()I', 'iget-object p0, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mItems:Ljava/util/ArrayList;', 'invoke-virtual {p0}, Ljava/util/ArrayList;->size()I', 'if-ge v3, v1, :cond_4', 'invoke-virtual {p0, v3}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;', 'check-cast v4, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;', 'invoke-virtual {v4}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->getGroupId()I', 'if-ne v5, v0, :cond_0'],
        'type': 'method_replace',
        'search': """.method setExclusiveItemChecked(Landroid/view/MenuItem;)V
    .registers 8

    invoke-interface {p1}, Landroid/view/MenuItem;->getGroupId()I

    move-result v0

    iget-object p0, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mItems:Ljava/util/ArrayList;

    invoke-virtual {p0}, Ljava/util/ArrayList;->size()I

    move-result v1

    const/4 v2, 0x0

    move v3, v2

    :cond_0
    :goto_0
    if-ge v3, v1, :cond_4

    invoke-virtual {p0, v3}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v4

    add-int/lit8 v3, v3, 0x1

    check-cast v4, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;

    invoke-virtual {v4}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->getGroupId()I

    move-result v5

    if-ne v5, v0, :cond_0

    invoke-virtual {v4}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->isExclusiveCheckable()Z

    move-result v5

    if-nez v5, :cond_1

    goto :goto_0

    :cond_1
    invoke-virtual {v4}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->isCheckable()Z

    move-result v5

    if-nez v5, :cond_2

    goto :goto_0

    :cond_2
    if-ne v4, p1, :cond_3

    const/4 v5, 0x1

    goto :goto_1

    :cond_3
    move v5, v2

    :goto_1
    invoke-virtual {v4, v5}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->setCheckedInt(Z)V

    goto :goto_0

    :cond_4
    return-void
.end method""",
        'replacement': """.method setExclusiveItemChecked(Landroid/view/MenuItem;)V
    .registers 8

    goto :goto_1d

    nop

    :goto_0
    return-void

    :goto_1
    move v5, v2

    :goto_2
    goto :goto_11

    nop

    :goto_3
    const/4 v5, 0x1

    goto :goto_9

    nop

    :goto_4
    if-eq v4, p1, :cond_0

    goto :goto_a

    :cond_0
    goto :goto_3

    nop

    :goto_5
    if-eqz v5, :cond_1

    goto :goto_1c

    :cond_1
    goto :goto_1b

    nop

    :goto_6
    move v3, v2

    :goto_7
    goto :goto_10

    nop

    :goto_8
    invoke-virtual {p0, v3}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v4

    goto :goto_14

    nop

    :goto_9
    goto :goto_2

    :goto_a
    goto :goto_1

    nop

    :goto_b
    invoke-virtual {v4}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->getGroupId()I

    move-result v5

    goto :goto_f

    nop

    :goto_c
    goto :goto_7

    :goto_d
    goto :goto_13

    nop

    :goto_e
    const/4 v2, 0x0

    goto :goto_6

    nop

    :goto_f
    if-eq v5, v0, :cond_2

    goto :goto_7

    :cond_2
    goto :goto_16

    nop

    :goto_10
    if-lt v3, v1, :cond_3

    goto :goto_18

    :cond_3
    goto :goto_8

    nop

    :goto_11
    invoke-virtual {v4, v5}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->setCheckedInt(Z)V

    goto :goto_17

    nop

    :goto_12
    if-eqz v5, :cond_4

    goto :goto_d

    :cond_4
    goto :goto_c

    nop

    :goto_13
    invoke-virtual {v4}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->isCheckable()Z

    move-result v5

    goto :goto_5

    nop

    :goto_14
    add-int/lit8 v3, v3, 0x1

    goto :goto_15

    nop

    :goto_15
    check-cast v4, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;

    goto :goto_b

    nop

    :goto_16
    invoke-virtual {v4}, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;->isExclusiveCheckable()Z

    move-result v5

    goto :goto_12

    nop

    :goto_17
    goto :goto_7

    :goto_18
    goto :goto_0

    nop

    :goto_19
    invoke-virtual {p0}, Ljava/util/ArrayList;->size()I

    move-result v1

    goto :goto_e

    nop

    :goto_1a
    iget-object p0, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mItems:Ljava/util/ArrayList;

    goto :goto_19

    nop

    :goto_1b
    goto :goto_7

    :goto_1c
    goto :goto_4

    nop

    :goto_1d
    invoke-interface {p1}, Landroid/view/MenuItem;->getGroupId()I

    move-result v0

    goto :goto_1a

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_MenuBuilder__setOptionalIconsVisible',
        'method': '.method setOptionalIconsVisible(Z)V',
        'method_name': 'setOptionalIconsVisible',
        'method_anchors': ['iput-boolean p1, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mOptionalIconsVisible:Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method setOptionalIconsVisible(Z)V
    .registers 2

    iput-boolean p1, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mOptionalIconsVisible:Z

    return-void
.end method""",
        'replacement': """.method setOptionalIconsVisible(Z)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    iput-boolean p1, p0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->mOptionalIconsVisible:Z

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
