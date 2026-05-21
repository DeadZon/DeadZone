TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/view/menu/ExpandedMenuView.smali'
CLASS_FALLBACK_NAMES = ['ExpandedMenuView.smali']
CLASS_ANCHORS = ['.super Landroid/widget/ListView;', '.implements Lmiuix/appcompat/internal/view/menu/MenuBuilder$ItemInvoker;', '.implements Lmiuix/appcompat/internal/view/menu/MenuView;', '.implements Landroid/widget/AdapterView$OnItemClickListener;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_view_menu_ExpandedMenuView__onDetachedFromWindow',
        'method': '.method protected onDetachedFromWindow()V',
        'method_name': 'onDetachedFromWindow',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/ListView;->onDetachedFromWindow()V', 'invoke-virtual {p0, v0}, Landroid/widget/ListView;->setChildrenDrawingCacheEnabled(Z)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onDetachedFromWindow()V
    .registers 2

    invoke-super {p0}, Landroid/widget/ListView;->onDetachedFromWindow()V

    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Landroid/widget/ListView;->setChildrenDrawingCacheEnabled(Z)V

    return-void
.end method""",
        'replacement': """.method protected onDetachedFromWindow()V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0}, Landroid/widget/ListView;->onDetachedFromWindow()V

    goto :goto_1

    nop

    :goto_1
    const/4 v0, 0x0

    goto :goto_2

    nop

    :goto_2
    invoke-virtual {p0, v0}, Landroid/widget/ListView;->setChildrenDrawingCacheEnabled(Z)V

    goto :goto_3

    nop

    :goto_3
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
