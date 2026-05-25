TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/widget/NestedScrollViewExpandContainer.smali'
CLASS_FALLBACK_NAMES = ['NestedScrollViewExpandContainer.smali']
CLASS_ANCHORS = ['.super Landroidx/core/widget/NestedScrollView;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_widget_NestedScrollViewExpandContainer__measureChild',
        'method': '.method protected measureChild(Landroid/view/View;II)V',
        'method_name': 'measureChild',
        'method_anchors': ['check-cast v0, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;', 'invoke-virtual {v0, p3}, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;->setParentHeightMeasureSpec(I)V', 'invoke-virtual {p1}, Landroid/view/View;->forceLayout()V', 'invoke-super {p0, p1, p2, p3}, Landroidx/core/widget/NestedScrollView;->measureChild(Landroid/view/View;II)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected measureChild(Landroid/view/View;II)V
    .registers 5

    move-object v0, p1

    check-cast v0, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;

    invoke-virtual {v0, p3}, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;->setParentHeightMeasureSpec(I)V

    invoke-virtual {p1}, Landroid/view/View;->forceLayout()V

    invoke-super {p0, p1, p2, p3}, Landroidx/core/widget/NestedScrollView;->measureChild(Landroid/view/View;II)V

    return-void
.end method""",
        'replacement': """.method protected measureChild(Landroid/view/View;II)V
    .registers 5

    goto :goto_3

    nop

    :goto_0
    return-void

    :goto_1
    invoke-virtual {v0, p3}, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;->setParentHeightMeasureSpec(I)V

    goto :goto_4

    nop

    :goto_2
    invoke-super {p0, p1, p2, p3}, Landroidx/core/widget/NestedScrollView;->measureChild(Landroid/view/View;II)V

    goto :goto_0

    nop

    :goto_3
    move-object v0, p1

    goto :goto_5

    nop

    :goto_4
    invoke-virtual {p1}, Landroid/view/View;->forceLayout()V

    goto :goto_2

    nop

    :goto_5
    check-cast v0, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_widget_NestedScrollViewExpandContainer__measureChildWithMargins',
        'method': '.method protected measureChildWithMargins(Landroid/view/View;IIII)V',
        'method_name': 'measureChildWithMargins',
        'method_anchors': ['check-cast v0, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;', 'invoke-virtual {v0, p4}, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;->setParentHeightMeasureSpec(I)V', 'invoke-virtual {p1}, Landroid/view/View;->forceLayout()V', 'invoke-super/range {p0 .. p5}, Landroidx/core/widget/NestedScrollView;->measureChildWithMargins(Landroid/view/View;IIII)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected measureChildWithMargins(Landroid/view/View;IIII)V
    .registers 7

    move-object v0, p1

    check-cast v0, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;

    invoke-virtual {v0, p4}, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;->setParentHeightMeasureSpec(I)V

    invoke-virtual {p1}, Landroid/view/View;->forceLayout()V

    invoke-super/range {p0 .. p5}, Landroidx/core/widget/NestedScrollView;->measureChildWithMargins(Landroid/view/View;IIII)V

    return-void
.end method""",
        'replacement': """.method protected measureChildWithMargins(Landroid/view/View;IIII)V
    .registers 7

    goto :goto_0

    nop

    :goto_0
    move-object v0, p1

    goto :goto_2

    nop

    :goto_1
    return-void

    :goto_2
    check-cast v0, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;

    goto :goto_4

    nop

    :goto_3
    invoke-super/range {p0 .. p5}, Landroidx/core/widget/NestedScrollView;->measureChildWithMargins(Landroid/view/View;IIII)V

    goto :goto_1

    nop

    :goto_4
    invoke-virtual {v0, p4}, Lmiuix/appcompat/internal/widget/NestedScrollViewExpander;->setParentHeightMeasureSpec(I)V

    goto :goto_5

    nop

    :goto_5
    invoke-virtual {p1}, Landroid/view/View;->forceLayout()V

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
