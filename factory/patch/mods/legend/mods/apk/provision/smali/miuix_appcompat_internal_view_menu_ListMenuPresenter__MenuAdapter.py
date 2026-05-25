TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/view/menu/ListMenuPresenter$MenuAdapter.smali'
CLASS_FALLBACK_NAMES = ['ListMenuPresenter$MenuAdapter.smali']
CLASS_ANCHORS = ['.super Landroid/widget/BaseAdapter;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_view_menu_ListMenuPresenter__MenuAdapter__findExpandedIndex',
        'method': '.method findExpandedIndex()V',
        'method_name': 'findExpandedIndex',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/ListMenuPresenter$MenuAdapter;->this$0:Lmiuix/appcompat/internal/view/menu/ListMenuPresenter;', 'iget-object v0, v0, Lmiuix/appcompat/internal/view/menu/ListMenuPresenter;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;', 'invoke-virtual {v0}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->getExpandedItem()Lmiuix/appcompat/internal/view/menu/MenuItemImpl;', 'if-eqz v0, :cond_1', 'iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/ListMenuPresenter$MenuAdapter;->this$0:Lmiuix/appcompat/internal/view/menu/ListMenuPresenter;', 'iget-object v1, v1, Lmiuix/appcompat/internal/view/menu/ListMenuPresenter;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;', 'invoke-virtual {v1}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->getNonActionItems()Ljava/util/ArrayList;', 'invoke-virtual {v1}, Ljava/util/ArrayList;->size()I'],
        'type': 'method_replace',
        'search': """.method findExpandedIndex()V
    .registers 6

    iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/ListMenuPresenter$MenuAdapter;->this$0:Lmiuix/appcompat/internal/view/menu/ListMenuPresenter;

    iget-object v0, v0, Lmiuix/appcompat/internal/view/menu/ListMenuPresenter;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    invoke-virtual {v0}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->getExpandedItem()Lmiuix/appcompat/internal/view/menu/MenuItemImpl;

    move-result-object v0

    if-eqz v0, :cond_1

    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/ListMenuPresenter$MenuAdapter;->this$0:Lmiuix/appcompat/internal/view/menu/ListMenuPresenter;

    iget-object v1, v1, Lmiuix/appcompat/internal/view/menu/ListMenuPresenter;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    invoke-virtual {v1}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->getNonActionItems()Ljava/util/ArrayList;

    move-result-object v1

    invoke-virtual {v1}, Ljava/util/ArrayList;->size()I

    move-result v2

    const/4 v3, 0x0

    :goto_0
    if-ge v3, v2, :cond_1

    invoke-virtual {v1, v3}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v4

    check-cast v4, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;

    if-ne v4, v0, :cond_0

    iput v3, p0, Lmiuix/appcompat/internal/view/menu/ListMenuPresenter$MenuAdapter;->mExpandedIndex:I

    return-void

    :cond_0
    add-int/lit8 v3, v3, 0x1

    goto :goto_0

    :cond_1
    const/4 v0, -0x1

    iput v0, p0, Lmiuix/appcompat/internal/view/menu/ListMenuPresenter$MenuAdapter;->mExpandedIndex:I

    return-void
.end method""",
        'replacement': """.method findExpandedIndex()V
    .registers 6

    goto :goto_5

    nop

    :goto_0
    if-nez v0, :cond_0

    goto :goto_9

    :cond_0
    goto :goto_11

    nop

    :goto_1
    const/4 v0, -0x1

    goto :goto_6

    nop

    :goto_2
    return-void

    :goto_3
    goto :goto_b

    nop

    :goto_4
    check-cast v4, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;

    goto :goto_a

    nop

    :goto_5
    iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/ListMenuPresenter$MenuAdapter;->this$0:Lmiuix/appcompat/internal/view/menu/ListMenuPresenter;

    goto :goto_f

    nop

    :goto_6
    iput v0, p0, Lmiuix/appcompat/internal/view/menu/ListMenuPresenter$MenuAdapter;->mExpandedIndex:I

    goto :goto_7

    nop

    :goto_7
    return-void

    :goto_8
    goto :goto_13

    :goto_9
    goto :goto_1

    nop

    :goto_a
    if-eq v4, v0, :cond_1

    goto :goto_3

    :cond_1
    goto :goto_16

    nop

    :goto_b
    add-int/lit8 v3, v3, 0x1

    goto :goto_8

    nop

    :goto_c
    invoke-virtual {v1}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->getNonActionItems()Ljava/util/ArrayList;

    move-result-object v1

    goto :goto_d

    nop

    :goto_d
    invoke-virtual {v1}, Ljava/util/ArrayList;->size()I

    move-result v2

    goto :goto_12

    nop

    :goto_e
    iget-object v1, v1, Lmiuix/appcompat/internal/view/menu/ListMenuPresenter;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    goto :goto_c

    nop

    :goto_f
    iget-object v0, v0, Lmiuix/appcompat/internal/view/menu/ListMenuPresenter;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    goto :goto_10

    nop

    :goto_10
    invoke-virtual {v0}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->getExpandedItem()Lmiuix/appcompat/internal/view/menu/MenuItemImpl;

    move-result-object v0

    goto :goto_0

    nop

    :goto_11
    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/ListMenuPresenter$MenuAdapter;->this$0:Lmiuix/appcompat/internal/view/menu/ListMenuPresenter;

    goto :goto_e

    nop

    :goto_12
    const/4 v3, 0x0

    :goto_13
    goto :goto_14

    nop

    :goto_14
    if-lt v3, v2, :cond_2

    goto :goto_9

    :cond_2
    goto :goto_15

    nop

    :goto_15
    invoke-virtual {v1, v3}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v4

    goto :goto_4

    nop

    :goto_16
    iput v3, p0, Lmiuix/appcompat/internal/view/menu/ListMenuPresenter$MenuAdapter;->mExpandedIndex:I

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
