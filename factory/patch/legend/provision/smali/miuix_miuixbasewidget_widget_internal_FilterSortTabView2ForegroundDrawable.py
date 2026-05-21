TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/miuixbasewidget/widget/internal/FilterSortTabView2ForegroundDrawable.smali'
CLASS_FALLBACK_NAMES = ['FilterSortTabView2ForegroundDrawable.smali']
CLASS_ANCHORS = ['.super Landroid/graphics/drawable/Drawable;', '.field private static final ACTIVATE_ENTER_CONFIG:Lmiuix/animation/base/AnimConfig;', '.field private static final ACTIVATE_EXIT_CONFIG:Lmiuix/animation/base/AnimConfig;', '.field private static final ALPHA_F:Ljava/lang/String; = "alphaF"', '.field private static final HOVER_ENTER_CONFIG:Lmiuix/animation/base/AnimConfig;', '.field private static final HOVER_EXIT_CONFIG:Lmiuix/animation/base/AnimConfig;']

PATCHES = [
    {
        'id': 'miuix_miuixbasewidget_widget_internal_FilterSortTabView2ForegroundDrawable__onBoundsChange',
        'method': '.method protected onBoundsChange(Landroid/graphics/Rect;)V',
        'method_name': 'onBoundsChange',
        'method_anchors': ['iget-object v0, p0, Lmiuix/miuixbasewidget/widget/internal/FilterSortTabView2ForegroundDrawable;->mRect:Landroid/graphics/RectF;', 'invoke-virtual {v0, p1}, Landroid/graphics/RectF;->set(Landroid/graphics/Rect;)V', 'invoke-direct {p0}, Lmiuix/miuixbasewidget/widget/internal/FilterSortTabView2ForegroundDrawable;->calculatePath()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onBoundsChange(Landroid/graphics/Rect;)V
    .registers 3

    iget-object v0, p0, Lmiuix/miuixbasewidget/widget/internal/FilterSortTabView2ForegroundDrawable;->mRect:Landroid/graphics/RectF;

    invoke-virtual {v0, p1}, Landroid/graphics/RectF;->set(Landroid/graphics/Rect;)V

    invoke-direct {p0}, Lmiuix/miuixbasewidget/widget/internal/FilterSortTabView2ForegroundDrawable;->calculatePath()V

    return-void
.end method""",
        'replacement': """.method protected onBoundsChange(Landroid/graphics/Rect;)V
    .registers 3

    goto :goto_0

    nop

    :goto_0
    iget-object v0, p0, Lmiuix/miuixbasewidget/widget/internal/FilterSortTabView2ForegroundDrawable;->mRect:Landroid/graphics/RectF;

    goto :goto_2

    nop

    :goto_1
    return-void

    :goto_2
    invoke-virtual {v0, p1}, Landroid/graphics/RectF;->set(Landroid/graphics/Rect;)V

    goto :goto_3

    nop

    :goto_3
    invoke-direct {p0}, Lmiuix/miuixbasewidget/widget/internal/FilterSortTabView2ForegroundDrawable;->calculatePath()V

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_miuixbasewidget_widget_internal_FilterSortTabView2ForegroundDrawable__onStateChange',
        'method': '.method protected onStateChange([I)Z',
        'method_name': 'onStateChange',
        'method_anchors': ['sget-object v0, Lmiuix/miuixbasewidget/widget/internal/FilterSortTabView2ForegroundDrawable;->STATE_PRESSED:[I', 'invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z', 'if-nez v0, :cond_4', 'sget-object v0, Lmiuix/miuixbasewidget/widget/internal/FilterSortTabView2ForegroundDrawable;->STATE_DRAG_HOVERED:[I', 'invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z', 'if-eqz v0, :cond_0', 'sget-object v0, Lmiuix/miuixbasewidget/widget/internal/FilterSortTabView2ForegroundDrawable;->STATE_HOVERED_ACTIVATED:[I', 'invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z'],
        'type': 'method_replace',
        'search': """.method protected onStateChange([I)Z
    .registers 3

    sget-object v0, Lmiuix/miuixbasewidget/widget/internal/FilterSortTabView2ForegroundDrawable;->STATE_PRESSED:[I

    invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z

    move-result v0

    if-nez v0, :cond_4

    sget-object v0, Lmiuix/miuixbasewidget/widget/internal/FilterSortTabView2ForegroundDrawable;->STATE_DRAG_HOVERED:[I

    invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z

    move-result v0

    if-eqz v0, :cond_0

    goto :goto_0

    :cond_0
    sget-object v0, Lmiuix/miuixbasewidget/widget/internal/FilterSortTabView2ForegroundDrawable;->STATE_HOVERED_ACTIVATED:[I

    invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z

    move-result v0

    if-eqz v0, :cond_1

    invoke-direct {p0}, Lmiuix/miuixbasewidget/widget/internal/FilterSortTabView2ForegroundDrawable;->toHoveredActivatedState()Z

    move-result p0

    return p0

    :cond_1
    sget-object v0, Lmiuix/miuixbasewidget/widget/internal/FilterSortTabView2ForegroundDrawable;->STATE_HOVERED:[I

    invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z

    move-result v0

    if-eqz v0, :cond_2

    invoke-direct {p0}, Lmiuix/miuixbasewidget/widget/internal/FilterSortTabView2ForegroundDrawable;->toHoveredState()Z

    move-result p0

    return p0

    :cond_2
    sget-object v0, Lmiuix/miuixbasewidget/widget/internal/FilterSortTabView2ForegroundDrawable;->STATE_ACTIVATED:[I

    invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z

    move-result p1

    if-eqz p1, :cond_3

    invoke-direct {p0}, Lmiuix/miuixbasewidget/widget/internal/FilterSortTabView2ForegroundDrawable;->toActivatedState()Z

    move-result p0

    return p0

    :cond_3
    invoke-direct {p0}, Lmiuix/miuixbasewidget/widget/internal/FilterSortTabView2ForegroundDrawable;->toNormalState()Z

    move-result p0

    return p0

    :cond_4
    :goto_0
    invoke-direct {p0}, Lmiuix/miuixbasewidget/widget/internal/FilterSortTabView2ForegroundDrawable;->toPressedState()Z

    move-result p0

    return p0
.end method""",
        'replacement': """.method protected onStateChange([I)Z
    .registers 3

    goto :goto_7

    nop

    :goto_0
    invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z

    move-result v0

    goto :goto_10

    nop

    :goto_1
    return p0

    :goto_2
    return p0

    :goto_3
    goto :goto_1c

    nop

    :goto_4
    invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z

    move-result p1

    goto :goto_15

    nop

    :goto_5
    goto :goto_d

    :goto_6
    goto :goto_a

    nop

    :goto_7
    sget-object v0, Lmiuix/miuixbasewidget/widget/internal/FilterSortTabView2ForegroundDrawable;->STATE_PRESSED:[I

    goto :goto_11

    nop

    :goto_8
    if-nez v0, :cond_0

    goto :goto_14

    :cond_0
    goto :goto_18

    nop

    :goto_9
    invoke-direct {p0}, Lmiuix/miuixbasewidget/widget/internal/FilterSortTabView2ForegroundDrawable;->toHoveredState()Z

    move-result p0

    goto :goto_2

    nop

    :goto_a
    sget-object v0, Lmiuix/miuixbasewidget/widget/internal/FilterSortTabView2ForegroundDrawable;->STATE_HOVERED_ACTIVATED:[I

    goto :goto_17

    nop

    :goto_b
    invoke-direct {p0}, Lmiuix/miuixbasewidget/widget/internal/FilterSortTabView2ForegroundDrawable;->toActivatedState()Z

    move-result p0

    goto :goto_1d

    nop

    :goto_c
    return p0

    :goto_d
    goto :goto_12

    nop

    :goto_e
    sget-object v0, Lmiuix/miuixbasewidget/widget/internal/FilterSortTabView2ForegroundDrawable;->STATE_HOVERED:[I

    goto :goto_1a

    nop

    :goto_f
    if-eqz v0, :cond_1

    goto :goto_d

    :cond_1
    goto :goto_19

    nop

    :goto_10
    if-nez v0, :cond_2

    goto :goto_6

    :cond_2
    goto :goto_5

    nop

    :goto_11
    invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z

    move-result v0

    goto :goto_f

    nop

    :goto_12
    invoke-direct {p0}, Lmiuix/miuixbasewidget/widget/internal/FilterSortTabView2ForegroundDrawable;->toPressedState()Z

    move-result p0

    goto :goto_1

    nop

    :goto_13
    return p0

    :goto_14
    goto :goto_e

    nop

    :goto_15
    if-nez p1, :cond_3

    goto :goto_1e

    :cond_3
    goto :goto_b

    nop

    :goto_16
    if-nez v0, :cond_4

    goto :goto_3

    :cond_4
    goto :goto_9

    nop

    :goto_17
    invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z

    move-result v0

    goto :goto_8

    nop

    :goto_18
    invoke-direct {p0}, Lmiuix/miuixbasewidget/widget/internal/FilterSortTabView2ForegroundDrawable;->toHoveredActivatedState()Z

    move-result p0

    goto :goto_13

    nop

    :goto_19
    sget-object v0, Lmiuix/miuixbasewidget/widget/internal/FilterSortTabView2ForegroundDrawable;->STATE_DRAG_HOVERED:[I

    goto :goto_0

    nop

    :goto_1a
    invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z

    move-result v0

    goto :goto_16

    nop

    :goto_1b
    invoke-direct {p0}, Lmiuix/miuixbasewidget/widget/internal/FilterSortTabView2ForegroundDrawable;->toNormalState()Z

    move-result p0

    goto :goto_c

    nop

    :goto_1c
    sget-object v0, Lmiuix/miuixbasewidget/widget/internal/FilterSortTabView2ForegroundDrawable;->STATE_ACTIVATED:[I

    goto :goto_4

    nop

    :goto_1d
    return p0

    :goto_1e
    goto :goto_1b

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
