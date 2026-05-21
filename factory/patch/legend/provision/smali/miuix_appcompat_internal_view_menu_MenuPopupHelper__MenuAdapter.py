TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/view/menu/MenuPopupHelper$MenuAdapter.smali'
CLASS_FALLBACK_NAMES = ['MenuPopupHelper$MenuAdapter.smali']
CLASS_ANCHORS = ['.super Landroid/widget/BaseAdapter;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_view_menu_MenuPopupHelper__MenuAdapter__findExpandedIndex',
        'method': '.method findExpandedIndex()V',
        'method_name': 'findExpandedIndex',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/MenuPopupHelper$MenuAdapter;->this$0:Lmiuix/appcompat/internal/view/menu/MenuPopupHelper;', 'invoke-static {v0}, Lmiuix/appcompat/internal/view/menu/MenuPopupHelper;->access$400(Lmiuix/appcompat/internal/view/menu/MenuPopupHelper;)Lmiuix/appcompat/internal/view/menu/MenuBuilder;', 'invoke-virtual {v0}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->getExpandedItem()Lmiuix/appcompat/internal/view/menu/MenuItemImpl;', 'if-eqz v0, :cond_1', 'iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/MenuPopupHelper$MenuAdapter;->this$0:Lmiuix/appcompat/internal/view/menu/MenuPopupHelper;', 'invoke-static {v1}, Lmiuix/appcompat/internal/view/menu/MenuPopupHelper;->access$400(Lmiuix/appcompat/internal/view/menu/MenuPopupHelper;)Lmiuix/appcompat/internal/view/menu/MenuBuilder;', 'invoke-virtual {v1}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->getNonActionItems()Ljava/util/ArrayList;', 'invoke-virtual {v1}, Ljava/util/ArrayList;->size()I'],
        'type': 'method_replace',
        'search': """.method findExpandedIndex()V
    .registers 6

    iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/MenuPopupHelper$MenuAdapter;->this$0:Lmiuix/appcompat/internal/view/menu/MenuPopupHelper;

    invoke-static {v0}, Lmiuix/appcompat/internal/view/menu/MenuPopupHelper;->access$400(Lmiuix/appcompat/internal/view/menu/MenuPopupHelper;)Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    move-result-object v0

    invoke-virtual {v0}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->getExpandedItem()Lmiuix/appcompat/internal/view/menu/MenuItemImpl;

    move-result-object v0

    if-eqz v0, :cond_1

    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/MenuPopupHelper$MenuAdapter;->this$0:Lmiuix/appcompat/internal/view/menu/MenuPopupHelper;

    invoke-static {v1}, Lmiuix/appcompat/internal/view/menu/MenuPopupHelper;->access$400(Lmiuix/appcompat/internal/view/menu/MenuPopupHelper;)Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    move-result-object v1

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

    iput v3, p0, Lmiuix/appcompat/internal/view/menu/MenuPopupHelper$MenuAdapter;->mExpandedIndex:I

    return-void

    :cond_0
    add-int/lit8 v3, v3, 0x1

    goto :goto_0

    :cond_1
    const/4 v0, -0x1

    iput v0, p0, Lmiuix/appcompat/internal/view/menu/MenuPopupHelper$MenuAdapter;->mExpandedIndex:I

    return-void
.end method""",
        'replacement': """.method findExpandedIndex()V
    .registers 6

    goto :goto_10

    nop

    :goto_0
    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/MenuPopupHelper$MenuAdapter;->this$0:Lmiuix/appcompat/internal/view/menu/MenuPopupHelper;

    goto :goto_14

    nop

    :goto_1
    iput v3, p0, Lmiuix/appcompat/internal/view/menu/MenuPopupHelper$MenuAdapter;->mExpandedIndex:I

    goto :goto_c

    nop

    :goto_2
    invoke-virtual {v1}, Ljava/util/ArrayList;->size()I

    move-result v2

    goto :goto_5

    nop

    :goto_3
    invoke-virtual {v1, v3}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v4

    goto :goto_7

    nop

    :goto_4
    iput v0, p0, Lmiuix/appcompat/internal/view/menu/MenuPopupHelper$MenuAdapter;->mExpandedIndex:I

    goto :goto_f

    nop

    :goto_5
    const/4 v3, 0x0

    :goto_6
    goto :goto_e

    nop

    :goto_7
    check-cast v4, Lmiuix/appcompat/internal/view/menu/MenuItemImpl;

    goto :goto_15

    nop

    :goto_8
    add-int/lit8 v3, v3, 0x1

    goto :goto_a

    nop

    :goto_9
    if-nez v0, :cond_0

    goto :goto_b

    :cond_0
    goto :goto_0

    nop

    :goto_a
    goto :goto_6

    :goto_b
    goto :goto_11

    nop

    :goto_c
    return-void

    :goto_d
    goto :goto_8

    nop

    :goto_e
    if-lt v3, v2, :cond_1

    goto :goto_b

    :cond_1
    goto :goto_3

    nop

    :goto_f
    return-void

    :goto_10
    iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/MenuPopupHelper$MenuAdapter;->this$0:Lmiuix/appcompat/internal/view/menu/MenuPopupHelper;

    goto :goto_13

    nop

    :goto_11
    const/4 v0, -0x1

    goto :goto_4

    nop

    :goto_12
    invoke-virtual {v1}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->getNonActionItems()Ljava/util/ArrayList;

    move-result-object v1

    goto :goto_2

    nop

    :goto_13
    invoke-static {v0}, Lmiuix/appcompat/internal/view/menu/MenuPopupHelper;->access$400(Lmiuix/appcompat/internal/view/menu/MenuPopupHelper;)Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    move-result-object v0

    goto :goto_16

    nop

    :goto_14
    invoke-static {v1}, Lmiuix/appcompat/internal/view/menu/MenuPopupHelper;->access$400(Lmiuix/appcompat/internal/view/menu/MenuPopupHelper;)Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    move-result-object v1

    goto :goto_12

    nop

    :goto_15
    if-eq v4, v0, :cond_2

    goto :goto_d

    :cond_2
    goto :goto_1

    nop

    :goto_16
    invoke-virtual {v0}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->getExpandedItem()Lmiuix/appcompat/internal/view/menu/MenuItemImpl;

    move-result-object v0

    goto :goto_9

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
