TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/internal/view/CheckWidgetAnimatedStateListDrawable.smali'
CLASS_FALLBACK_NAMES = ['CheckWidgetAnimatedStateListDrawable.smali']
CLASS_ANCHORS = ['.super Landroid/graphics/drawable/AnimatedStateListDrawable;', '.field private static final TAG:Ljava/lang/String;']

PATCHES = [
    {
        'id': 'miuix_internal_view_CheckWidgetAnimatedStateListDrawable__newCheckWidgetConstantState',
        'method': '.method protected newCheckWidgetConstantState()Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;',
        'method_name': 'newCheckWidgetConstantState',
        'method_anchors': ['new-instance p0, Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;', 'invoke-direct {p0}, Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;-><init>()V', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected newCheckWidgetConstantState()Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;
    .registers 1

    new-instance p0, Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;

    invoke-direct {p0}, Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;-><init>()V

    return-object p0
.end method""",
        'replacement': """.method protected newCheckWidgetConstantState()Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    new-instance p0, Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;

    goto :goto_2

    nop

    :goto_1
    return-object p0

    :goto_2
    invoke-direct {p0}, Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;-><init>()V

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_view_CheckWidgetAnimatedStateListDrawable__setConstantState',
        'method': '.method protected setConstantState(Landroid/graphics/drawable/DrawableContainer$DrawableContainerState;)V',
        'method_name': 'setConstantState',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/graphics/drawable/AnimatedStateListDrawable;->setConstantState(Landroid/graphics/drawable/DrawableContainer$DrawableContainerState;)V', 'iget-object v0, p0, Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable;->mCheckWidgetConstantState:Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;', 'if-nez v0, :cond_0', 'invoke-virtual {p0}, Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable;->newCheckWidgetConstantState()Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;', 'iput-object v0, p0, Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable;->mCheckWidgetConstantState:Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;', 'iget-object p0, p0, Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable;->mCheckWidgetConstantState:Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;', 'iput-object p1, p0, Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;->mParent:Landroid/graphics/drawable/Drawable$ConstantState;', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected setConstantState(Landroid/graphics/drawable/DrawableContainer$DrawableContainerState;)V
    .registers 3

    invoke-super {p0, p1}, Landroid/graphics/drawable/AnimatedStateListDrawable;->setConstantState(Landroid/graphics/drawable/DrawableContainer$DrawableContainerState;)V

    iget-object v0, p0, Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable;->mCheckWidgetConstantState:Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;

    if-nez v0, :cond_0

    invoke-virtual {p0}, Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable;->newCheckWidgetConstantState()Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;

    move-result-object v0

    iput-object v0, p0, Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable;->mCheckWidgetConstantState:Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;

    :cond_0
    iget-object p0, p0, Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable;->mCheckWidgetConstantState:Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;

    iput-object p1, p0, Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;->mParent:Landroid/graphics/drawable/Drawable$ConstantState;

    return-void
.end method""",
        'replacement': """.method protected setConstantState(Landroid/graphics/drawable/DrawableContainer$DrawableContainerState;)V
    .registers 3

    goto :goto_1

    nop

    :goto_0
    iget-object v0, p0, Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable;->mCheckWidgetConstantState:Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;

    goto :goto_8

    nop

    :goto_1
    invoke-super {p0, p1}, Landroid/graphics/drawable/AnimatedStateListDrawable;->setConstantState(Landroid/graphics/drawable/DrawableContainer$DrawableContainerState;)V

    goto :goto_0

    nop

    :goto_2
    iget-object p0, p0, Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable;->mCheckWidgetConstantState:Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;

    goto :goto_3

    nop

    :goto_3
    iput-object p1, p0, Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;->mParent:Landroid/graphics/drawable/Drawable$ConstantState;

    goto :goto_7

    nop

    :goto_4
    iput-object v0, p0, Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable;->mCheckWidgetConstantState:Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;

    :goto_5
    goto :goto_2

    nop

    :goto_6
    invoke-virtual {p0}, Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable;->newCheckWidgetConstantState()Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;

    move-result-object v0

    goto :goto_4

    nop

    :goto_7
    return-void

    :goto_8
    if-eqz v0, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
