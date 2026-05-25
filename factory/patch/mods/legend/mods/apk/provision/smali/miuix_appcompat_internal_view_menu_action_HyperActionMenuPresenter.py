TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/view/menu/action/HyperActionMenuPresenter.smali'
CLASS_FALLBACK_NAMES = ['HyperActionMenuPresenter.smali']
CLASS_ANCHORS = ['.super Lmiuix/appcompat/internal/view/menu/action/EndActionMenuPresenter;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_view_menu_action_HyperActionMenuPresenter__getOverflowMenu',
        'method': '.method protected getOverflowMenu()Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter$OverflowMenu;',
        'method_name': 'getOverflowMenu',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->shouldShowPopupOverflow()Z', 'if-eqz v0, :cond_0', 'new-instance v1, Lmiuix/appcompat/internal/view/menu/action/HyperActionMenuPresenter$HyperPopupOverflowMenu;', 'iget-object v3, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mContext:Landroid/content/Context;', 'iget-object v4, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;', 'iget-object v5, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->mOverflowButton:Landroid/view/View;', 'iget-object v6, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->mDecorView:Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;', 'invoke-direct/range {v1 .. v7}, Lmiuix/appcompat/internal/view/menu/action/HyperActionMenuPresenter$HyperPopupOverflowMenu;-><init>(Lmiuix/appcompat/internal/view/menu/action/HyperActionMenuPresenter;Landroid/content/Context;Lmiuix/appcompat/internal/view/menu/MenuBuilder;Landroid/view/View;Landroid/view/View;Z)V'],
        'type': 'method_replace',
        'search': """.method protected getOverflowMenu()Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter$OverflowMenu;
    .registers 9

    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->shouldShowPopupOverflow()Z

    move-result v0

    if-eqz v0, :cond_0

    new-instance v1, Lmiuix/appcompat/internal/view/menu/action/HyperActionMenuPresenter$HyperPopupOverflowMenu;

    iget-object v3, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mContext:Landroid/content/Context;

    iget-object v4, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    iget-object v5, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->mOverflowButton:Landroid/view/View;

    iget-object v6, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->mDecorView:Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;

    const/4 v7, 0x1

    move-object v2, p0

    invoke-direct/range {v1 .. v7}, Lmiuix/appcompat/internal/view/menu/action/HyperActionMenuPresenter$HyperPopupOverflowMenu;-><init>(Lmiuix/appcompat/internal/view/menu/action/HyperActionMenuPresenter;Landroid/content/Context;Lmiuix/appcompat/internal/view/menu/MenuBuilder;Landroid/view/View;Landroid/view/View;Z)V

    iget-object p0, v2, Lmiuix/appcompat/internal/view/menu/action/HyperActionMenuPresenter;->mHyperMenuPrimaryCheckedMap:Ljava/util/Map;

    invoke-virtual {v1, p0}, Lmiuix/appcompat/internal/view/menu/HyperPopupHelper;->restoreHyperMenuPrimaryCheckedData(Ljava/util/Map;)V

    iget-object p0, v2, Lmiuix/appcompat/internal/view/menu/action/HyperActionMenuPresenter;->mHyperMenuSecondaryCheckedMap:Ljava/util/Map;

    invoke-virtual {v1, p0}, Lmiuix/appcompat/internal/view/menu/HyperPopupHelper;->restoreHyperMenuSecondaryCheckedData(Ljava/util/Map;)V

    return-object v1

    :cond_0
    move-object v2, p0

    invoke-super {v2}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->getOverflowMenu()Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter$OverflowMenu;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected getOverflowMenu()Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter$OverflowMenu;
    .registers 9

    goto :goto_11

    nop

    :goto_0
    if-nez v0, :cond_0

    goto :goto_7

    :cond_0
    goto :goto_2

    nop

    :goto_1
    iget-object v4, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    goto :goto_c

    nop

    :goto_2
    new-instance v1, Lmiuix/appcompat/internal/view/menu/action/HyperActionMenuPresenter$HyperPopupOverflowMenu;

    goto :goto_d

    nop

    :goto_3
    move-object v2, p0

    goto :goto_a

    nop

    :goto_4
    invoke-virtual {v1, p0}, Lmiuix/appcompat/internal/view/menu/HyperPopupHelper;->restoreHyperMenuSecondaryCheckedData(Ljava/util/Map;)V

    goto :goto_6

    nop

    :goto_5
    iget-object v6, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->mDecorView:Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;

    goto :goto_12

    nop

    :goto_6
    return-object v1

    :goto_7
    goto :goto_10

    nop

    :goto_8
    iget-object p0, v2, Lmiuix/appcompat/internal/view/menu/action/HyperActionMenuPresenter;->mHyperMenuSecondaryCheckedMap:Ljava/util/Map;

    goto :goto_4

    nop

    :goto_9
    invoke-virtual {v1, p0}, Lmiuix/appcompat/internal/view/menu/HyperPopupHelper;->restoreHyperMenuPrimaryCheckedData(Ljava/util/Map;)V

    goto :goto_8

    nop

    :goto_a
    invoke-direct/range {v1 .. v7}, Lmiuix/appcompat/internal/view/menu/action/HyperActionMenuPresenter$HyperPopupOverflowMenu;-><init>(Lmiuix/appcompat/internal/view/menu/action/HyperActionMenuPresenter;Landroid/content/Context;Lmiuix/appcompat/internal/view/menu/MenuBuilder;Landroid/view/View;Landroid/view/View;Z)V

    goto :goto_b

    nop

    :goto_b
    iget-object p0, v2, Lmiuix/appcompat/internal/view/menu/action/HyperActionMenuPresenter;->mHyperMenuPrimaryCheckedMap:Ljava/util/Map;

    goto :goto_9

    nop

    :goto_c
    iget-object v5, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->mOverflowButton:Landroid/view/View;

    goto :goto_5

    nop

    :goto_d
    iget-object v3, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mContext:Landroid/content/Context;

    goto :goto_1

    nop

    :goto_e
    return-object p0

    :goto_f
    invoke-super {v2}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->getOverflowMenu()Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter$OverflowMenu;

    move-result-object p0

    goto :goto_e

    nop

    :goto_10
    move-object v2, p0

    goto :goto_f

    nop

    :goto_11
    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuPresenter;->shouldShowPopupOverflow()Z

    move-result v0

    goto :goto_0

    nop

    :goto_12
    const/4 v7, 0x1

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
