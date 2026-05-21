TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/recyclerview/widget/RecyclerView.smali'
CLASS_FALLBACK_NAMES = ['RecyclerView.smali']
CLASS_ANCHORS = ['.super Landroidx/recyclerview/widget/SpringRecyclerView;']

PATCHES = [
    {
        'id': 'miuix_recyclerview_widget_RecyclerView__onFocusChanged',
        'method': '.method protected onFocusChanged(ZILandroid/graphics/Rect;)V',
        'method_name': 'onFocusChanged',
        'method_anchors': ['invoke-super {p0, p1, p2, p3}, Landroid/view/ViewGroup;->onFocusChanged(ZILandroid/graphics/Rect;)V', 'iget-object p0, p0, Lmiuix/recyclerview/widget/RecyclerView;->mGetSpeedForDynamicRefreshRate:Lmiuix/recyclerview/tool/GetSpeedForDynamicRefreshRate;', 'if-eqz p0, :cond_0', 'invoke-virtual {p0, p1}, Lmiuix/recyclerview/tool/GetSpeedForDynamicRefreshRate;->onFocusChange(Z)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onFocusChanged(ZILandroid/graphics/Rect;)V
    .registers 4

    invoke-super {p0, p1, p2, p3}, Landroid/view/ViewGroup;->onFocusChanged(ZILandroid/graphics/Rect;)V

    iget-object p0, p0, Lmiuix/recyclerview/widget/RecyclerView;->mGetSpeedForDynamicRefreshRate:Lmiuix/recyclerview/tool/GetSpeedForDynamicRefreshRate;

    if-eqz p0, :cond_0

    invoke-virtual {p0, p1}, Lmiuix/recyclerview/tool/GetSpeedForDynamicRefreshRate;->onFocusChange(Z)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onFocusChanged(ZILandroid/graphics/Rect;)V
    .registers 4

    goto :goto_2

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/recyclerview/widget/RecyclerView;->mGetSpeedForDynamicRefreshRate:Lmiuix/recyclerview/tool/GetSpeedForDynamicRefreshRate;

    goto :goto_1

    nop

    :goto_1
    if-nez p0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_3

    nop

    :goto_2
    invoke-super {p0, p1, p2, p3}, Landroid/view/ViewGroup;->onFocusChanged(ZILandroid/graphics/Rect;)V

    goto :goto_0

    nop

    :goto_3
    invoke-virtual {p0, p1}, Lmiuix/recyclerview/tool/GetSpeedForDynamicRefreshRate;->onFocusChange(Z)V

    :goto_4
    goto :goto_5

    nop

    :goto_5
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
