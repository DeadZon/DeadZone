TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/slidingwidget/widget/SlidingSwitchCompat.smali'
CLASS_FALLBACK_NAMES = ['SlidingSwitchCompat.smali']
CLASS_ANCHORS = ['.super Landroidx/appcompat/widget/SwitchCompat;']

PATCHES = [
    {
        'id': 'miuix_slidingwidget_widget_SlidingSwitchCompat__drawableStateChanged',
        'method': '.method protected drawableStateChanged()V',
        'method_name': 'drawableStateChanged',
        'method_anchors': ['invoke-super {p0}, Landroidx/appcompat/widget/SwitchCompat;->drawableStateChanged()V', 'iget-object p0, p0, Lmiuix/slidingwidget/widget/SlidingSwitchCompat;->mHelper:Lmiuix/slidingwidget/widget/SlidingButtonHelper;', 'if-eqz p0, :cond_0', 'invoke-virtual {p0}, Lmiuix/slidingwidget/widget/SlidingButtonHelper;->setSliderDrawState()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected drawableStateChanged()V
    .registers 1

    invoke-super {p0}, Landroidx/appcompat/widget/SwitchCompat;->drawableStateChanged()V

    iget-object p0, p0, Lmiuix/slidingwidget/widget/SlidingSwitchCompat;->mHelper:Lmiuix/slidingwidget/widget/SlidingButtonHelper;

    if-eqz p0, :cond_0

    invoke-virtual {p0}, Lmiuix/slidingwidget/widget/SlidingButtonHelper;->setSliderDrawState()V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected drawableStateChanged()V
    .registers 1

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0}, Landroidx/appcompat/widget/SwitchCompat;->drawableStateChanged()V

    goto :goto_5

    nop

    :goto_1
    if-nez p0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_3

    nop

    :goto_2
    return-void

    :goto_3
    invoke-virtual {p0}, Lmiuix/slidingwidget/widget/SlidingButtonHelper;->setSliderDrawState()V

    :goto_4
    goto :goto_2

    nop

    :goto_5
    iget-object p0, p0, Lmiuix/slidingwidget/widget/SlidingSwitchCompat;->mHelper:Lmiuix/slidingwidget/widget/SlidingButtonHelper;

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_slidingwidget_widget_SlidingSwitchCompat__onDraw',
        'method': '.method protected onDraw(Landroid/graphics/Canvas;)V',
        'method_name': 'onDraw',
        'method_anchors': ['iget-object v0, p0, Lmiuix/slidingwidget/widget/SlidingSwitchCompat;->mHelper:Lmiuix/slidingwidget/widget/SlidingButtonHelper;', 'if-nez v0, :cond_0', 'invoke-super {p0, p1}, Landroidx/appcompat/widget/SwitchCompat;->onDraw(Landroid/graphics/Canvas;)V', 'return-void', 'invoke-virtual {v0, p1}, Lmiuix/slidingwidget/widget/SlidingButtonHelper;->onDraw(Landroid/graphics/Canvas;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onDraw(Landroid/graphics/Canvas;)V
    .registers 3

    iget-object v0, p0, Lmiuix/slidingwidget/widget/SlidingSwitchCompat;->mHelper:Lmiuix/slidingwidget/widget/SlidingButtonHelper;

    if-nez v0, :cond_0

    invoke-super {p0, p1}, Landroidx/appcompat/widget/SwitchCompat;->onDraw(Landroid/graphics/Canvas;)V

    return-void

    :cond_0
    invoke-virtual {v0, p1}, Lmiuix/slidingwidget/widget/SlidingButtonHelper;->onDraw(Landroid/graphics/Canvas;)V

    return-void
.end method""",
        'replacement': """.method protected onDraw(Landroid/graphics/Canvas;)V
    .registers 3

    goto :goto_6

    nop

    :goto_0
    invoke-virtual {v0, p1}, Lmiuix/slidingwidget/widget/SlidingButtonHelper;->onDraw(Landroid/graphics/Canvas;)V

    goto :goto_5

    nop

    :goto_1
    if-eqz v0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_2

    nop

    :goto_2
    invoke-super {p0, p1}, Landroidx/appcompat/widget/SwitchCompat;->onDraw(Landroid/graphics/Canvas;)V

    goto :goto_3

    nop

    :goto_3
    return-void

    :goto_4
    goto :goto_0

    nop

    :goto_5
    return-void

    :goto_6
    iget-object v0, p0, Lmiuix/slidingwidget/widget/SlidingSwitchCompat;->mHelper:Lmiuix/slidingwidget/widget/SlidingButtonHelper;

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_slidingwidget_widget_SlidingSwitchCompat__onSetAlpha',
        'method': '.method protected onSetAlpha(I)Z',
        'method_name': 'onSetAlpha',
        'method_anchors': ['return p0'],
        'type': 'method_replace',
        'search': """.method protected onSetAlpha(I)Z
    .registers 2

    const/4 p0, 0x1

    return p0
.end method""",
        'replacement': """.method protected onSetAlpha(I)Z
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    const/4 p0, 0x1

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_slidingwidget_widget_SlidingSwitchCompat__verifyDrawable',
        'method': '.method protected verifyDrawable(Landroid/graphics/drawable/Drawable;)Z',
        'method_name': 'verifyDrawable',
        'method_anchors': ['invoke-super {p0, p1}, Landroidx/appcompat/widget/SwitchCompat;->verifyDrawable(Landroid/graphics/drawable/Drawable;)Z', 'if-nez v0, :cond_1', 'iget-object p0, p0, Lmiuix/slidingwidget/widget/SlidingSwitchCompat;->mHelper:Lmiuix/slidingwidget/widget/SlidingButtonHelper;', 'if-eqz p0, :cond_0', 'invoke-virtual {p0, p1}, Lmiuix/slidingwidget/widget/SlidingButtonHelper;->verifyDrawable(Landroid/graphics/drawable/Drawable;)Z', 'if-eqz p0, :cond_0', 'return p0', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected verifyDrawable(Landroid/graphics/drawable/Drawable;)Z
    .registers 3

    invoke-super {p0, p1}, Landroidx/appcompat/widget/SwitchCompat;->verifyDrawable(Landroid/graphics/drawable/Drawable;)Z

    move-result v0

    if-nez v0, :cond_1

    iget-object p0, p0, Lmiuix/slidingwidget/widget/SlidingSwitchCompat;->mHelper:Lmiuix/slidingwidget/widget/SlidingButtonHelper;

    if-eqz p0, :cond_0

    invoke-virtual {p0, p1}, Lmiuix/slidingwidget/widget/SlidingButtonHelper;->verifyDrawable(Landroid/graphics/drawable/Drawable;)Z

    move-result p0

    if-eqz p0, :cond_0

    goto :goto_0

    :cond_0
    const/4 p0, 0x0

    return p0

    :cond_1
    :goto_0
    const/4 p0, 0x1

    return p0
.end method""",
        'replacement': """.method protected verifyDrawable(Landroid/graphics/drawable/Drawable;)Z
    .registers 3

    goto :goto_7

    nop

    :goto_0
    const/4 p0, 0x1

    goto :goto_8

    nop

    :goto_1
    if-eqz v0, :cond_0

    goto :goto_c

    :cond_0
    goto :goto_3

    nop

    :goto_2
    invoke-virtual {p0, p1}, Lmiuix/slidingwidget/widget/SlidingButtonHelper;->verifyDrawable(Landroid/graphics/drawable/Drawable;)Z

    move-result p0

    goto :goto_6

    nop

    :goto_3
    iget-object p0, p0, Lmiuix/slidingwidget/widget/SlidingSwitchCompat;->mHelper:Lmiuix/slidingwidget/widget/SlidingButtonHelper;

    goto :goto_5

    nop

    :goto_4
    const/4 p0, 0x0

    goto :goto_b

    nop

    :goto_5
    if-nez p0, :cond_1

    goto :goto_a

    :cond_1
    goto :goto_2

    nop

    :goto_6
    if-nez p0, :cond_2

    goto :goto_a

    :cond_2
    goto :goto_9

    nop

    :goto_7
    invoke-super {p0, p1}, Landroidx/appcompat/widget/SwitchCompat;->verifyDrawable(Landroid/graphics/drawable/Drawable;)Z

    move-result v0

    goto :goto_1

    nop

    :goto_8
    return p0

    :goto_9
    goto :goto_c

    :goto_a
    goto :goto_4

    nop

    :goto_b
    return p0

    :goto_c
    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
