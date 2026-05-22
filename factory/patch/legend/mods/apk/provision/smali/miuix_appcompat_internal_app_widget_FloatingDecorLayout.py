TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/app/widget/FloatingDecorLayout.smali'
CLASS_FALLBACK_NAMES = ['FloatingDecorLayout.smali']
CLASS_ANCHORS = ['.super Landroid/widget/FrameLayout;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_app_widget_FloatingDecorLayout__fitSystemWindows',
        'method': '.method protected fitSystemWindows(Landroid/graphics/Rect;)Z',
        'method_name': 'fitSystemWindows',
        'method_anchors': ['sget v0, Lmiuix/appcompat/R$id;->action_bar_overlay_layout:I', 'invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;', 'check-cast v0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;', 'if-eqz v0, :cond_0', 'invoke-virtual {v0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->fitSystemWindows(Landroid/graphics/Rect;)Z', 'iput v0, p1, Landroid/graphics/Rect;->top:I', 'iput v0, p1, Landroid/graphics/Rect;->bottom:I', 'invoke-super {p0, p1}, Landroid/widget/FrameLayout;->fitSystemWindows(Landroid/graphics/Rect;)Z'],
        'type': 'method_replace',
        'search': """.method protected fitSystemWindows(Landroid/graphics/Rect;)Z
    .registers 3

    sget v0, Lmiuix/appcompat/R$id;->action_bar_overlay_layout:I

    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;

    if-eqz v0, :cond_0

    invoke-virtual {v0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->fitSystemWindows(Landroid/graphics/Rect;)Z

    :cond_0
    const/4 v0, 0x0

    iput v0, p1, Landroid/graphics/Rect;->top:I

    iput v0, p1, Landroid/graphics/Rect;->bottom:I

    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->fitSystemWindows(Landroid/graphics/Rect;)Z

    move-result p0

    return p0
.end method""",
        'replacement': """.method protected fitSystemWindows(Landroid/graphics/Rect;)Z
    .registers 3

    goto :goto_7

    nop

    :goto_0
    if-nez v0, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_5

    nop

    :goto_1
    iput v0, p1, Landroid/graphics/Rect;->top:I

    goto :goto_3

    nop

    :goto_2
    return p0

    :goto_3
    iput v0, p1, Landroid/graphics/Rect;->bottom:I

    goto :goto_a

    nop

    :goto_4
    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_8

    nop

    :goto_5
    invoke-virtual {v0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->fitSystemWindows(Landroid/graphics/Rect;)Z

    :goto_6
    goto :goto_9

    nop

    :goto_7
    sget v0, Lmiuix/appcompat/R$id;->action_bar_overlay_layout:I

    goto :goto_4

    nop

    :goto_8
    check-cast v0, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;

    goto :goto_0

    nop

    :goto_9
    const/4 v0, 0x0

    goto :goto_1

    nop

    :goto_a
    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->fitSystemWindows(Landroid/graphics/Rect;)Z

    move-result p0

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
