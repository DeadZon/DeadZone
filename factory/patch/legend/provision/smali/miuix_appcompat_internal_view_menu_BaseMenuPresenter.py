TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/view/menu/BaseMenuPresenter.smali'
CLASS_FALLBACK_NAMES = ['BaseMenuPresenter.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Lmiuix/appcompat/internal/view/menu/MenuPresenter;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_view_menu_BaseMenuPresenter__addItemView',
        'method': '.method protected addItemView(Landroid/view/View;I)V',
        'method_name': 'addItemView',
        'method_anchors': ['invoke-virtual {p1}, Landroid/view/View;->getParent()Landroid/view/ViewParent;', 'check-cast v0, Landroid/view/ViewGroup;', 'if-eqz v0, :cond_0', 'invoke-virtual {v0, p1}, Landroid/view/ViewGroup;->removeView(Landroid/view/View;)V', 'iget-object p0, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mMenuView:Lmiuix/appcompat/internal/view/menu/MenuView;', 'check-cast p0, Landroid/view/ViewGroup;', 'invoke-virtual {p0, p1, p2}, Landroid/view/ViewGroup;->addView(Landroid/view/View;I)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected addItemView(Landroid/view/View;I)V
    .registers 4

    invoke-virtual {p1}, Landroid/view/View;->getParent()Landroid/view/ViewParent;

    move-result-object v0

    check-cast v0, Landroid/view/ViewGroup;

    if-eqz v0, :cond_0

    invoke-virtual {v0, p1}, Landroid/view/ViewGroup;->removeView(Landroid/view/View;)V

    :cond_0
    iget-object p0, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mMenuView:Lmiuix/appcompat/internal/view/menu/MenuView;

    check-cast p0, Landroid/view/ViewGroup;

    invoke-virtual {p0, p1, p2}, Landroid/view/ViewGroup;->addView(Landroid/view/View;I)V

    return-void
.end method""",
        'replacement': """.method protected addItemView(Landroid/view/View;I)V
    .registers 4

    goto :goto_3

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/appcompat/internal/view/menu/BaseMenuPresenter;->mMenuView:Lmiuix/appcompat/internal/view/menu/MenuView;

    goto :goto_4

    nop

    :goto_1
    check-cast v0, Landroid/view/ViewGroup;

    goto :goto_2

    nop

    :goto_2
    if-nez v0, :cond_0

    goto :goto_7

    :cond_0
    goto :goto_6

    nop

    :goto_3
    invoke-virtual {p1}, Landroid/view/View;->getParent()Landroid/view/ViewParent;

    move-result-object v0

    goto :goto_1

    nop

    :goto_4
    check-cast p0, Landroid/view/ViewGroup;

    goto :goto_5

    nop

    :goto_5
    invoke-virtual {p0, p1, p2}, Landroid/view/ViewGroup;->addView(Landroid/view/View;I)V

    goto :goto_8

    nop

    :goto_6
    invoke-virtual {v0, p1}, Landroid/view/ViewGroup;->removeView(Landroid/view/View;)V

    :goto_7
    goto :goto_0

    nop

    :goto_8
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
