TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/androidbasewidget/adapter/FragmentViewHolder.smali'
CLASS_FALLBACK_NAMES = ['FragmentViewHolder.smali']
CLASS_ANCHORS = ['.super Landroidx/recyclerview/widget/RecyclerView$ViewHolder;']

PATCHES = [
    {
        'id': 'miuix_androidbasewidget_adapter_FragmentViewHolder__getContainer',
        'method': '.method getContainer()Landroid/widget/FrameLayout;',
        'method_name': 'getContainer',
        'method_anchors': ['iget-object p0, p0, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;', 'check-cast p0, Landroid/widget/FrameLayout;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method getContainer()Landroid/widget/FrameLayout;
    .registers 1

    iget-object p0, p0, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    check-cast p0, Landroid/widget/FrameLayout;

    return-object p0
.end method""",
        'replacement': """.method getContainer()Landroid/widget/FrameLayout;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    iget-object p0, p0, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    goto :goto_2

    nop

    :goto_2
    check-cast p0, Landroid/widget/FrameLayout;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
