TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/androidbasewidget/widget/AppCompatCheckedTextView.smali'
CLASS_FALLBACK_NAMES = ['AppCompatCheckedTextView.smali']
CLASS_ANCHORS = ['.super Landroidx/appcompat/widget/AppCompatCheckedTextView;']

PATCHES = [
    {
        'id': 'miuix_androidbasewidget_widget_AppCompatCheckedTextView__onAttachedToWindow',
        'method': '.method protected onAttachedToWindow()V',
        'method_name': 'onAttachedToWindow',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/CheckedTextView;->onAttachedToWindow()V', 'invoke-virtual {p0}, Landroid/widget/CheckedTextView;->getParent()Landroid/view/ViewParent;', 'check-cast v0, Landroid/view/View;', 'if-eqz v0, :cond_0', 'invoke-virtual {v0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;', 'invoke-virtual {v0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;', 'const-string v4, "RecyclerView"', 'invoke-virtual {v0, v4}, Ljava/lang/String;->contains(Ljava/lang/CharSequence;)Z'],
        'type': 'method_replace',
        'search': """.method protected onAttachedToWindow()V
    .registers 6

    invoke-super {p0}, Landroid/widget/CheckedTextView;->onAttachedToWindow()V

    invoke-virtual {p0}, Landroid/widget/CheckedTextView;->getParent()Landroid/view/ViewParent;

    move-result-object v0

    check-cast v0, Landroid/view/View;

    instance-of v1, v0, Landroid/widget/ListView;

    const/4 v2, 0x1

    const/4 v3, 0x0

    if-eqz v0, :cond_0

    invoke-virtual {v0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object v0

    const-string v4, "RecyclerView"

    invoke-virtual {v0, v4}, Ljava/lang/String;->contains(Ljava/lang/CharSequence;)Z

    move-result v0

    if-eqz v0, :cond_0

    move v0, v2

    goto :goto_0

    :cond_0
    move v0, v3

    :goto_0
    if-nez v1, :cond_1

    if-nez v0, :cond_1

    new-array v0, v2, [Landroid/view/View;

    aput-object p0, v0, v3

    invoke-static {v0}, Lmiuix/animation/Folme;->useAt([Landroid/view/View;)Lmiuix/animation/IFolme;

    move-result-object v0

    invoke-interface {v0}, Lmiuix/animation/IFolme;->hover()Lmiuix/animation/IHoverStyle;

    move-result-object v0

    sget-object v1, Lmiuix/animation/IHoverStyle$HoverEffect;->NORMAL:Lmiuix/animation/IHoverStyle$HoverEffect;

    invoke-interface {v0, v1}, Lmiuix/animation/IHoverStyle;->setEffect(Lmiuix/animation/IHoverStyle$HoverEffect;)Lmiuix/animation/IHoverStyle;

    move-result-object v0

    new-array v1, v3, [Lmiuix/animation/base/AnimConfig;

    invoke-interface {v0, p0, v1}, Lmiuix/animation/IHoverStyle;->handleHoverOf(Landroid/view/View;[Lmiuix/animation/base/AnimConfig;)V

    return-void

    :cond_1
    invoke-virtual {p0}, Landroid/widget/CheckedTextView;->isClickable()Z

    move-result v0

    if-nez v0, :cond_3

    invoke-virtual {p0}, Landroid/widget/CheckedTextView;->getForeground()Landroid/graphics/drawable/Drawable;

    move-result-object v0

    if-eqz v0, :cond_2

    new-instance v0, Lmiuix/androidbasewidget/widget/AppCompatCheckedTextView$$ExternalSyntheticLambda0;

    invoke-direct {v0}, Lmiuix/androidbasewidget/widget/AppCompatCheckedTextView$$ExternalSyntheticLambda0;-><init>()V

    invoke-virtual {p0, v0}, Landroid/widget/CheckedTextView;->setOnHoverListener(Landroid/view/View$OnHoverListener;)V

    return-void

    :cond_2
    new-array v0, v2, [Landroid/view/View;

    aput-object p0, v0, v3

    invoke-static {v0}, Lmiuix/animation/Folme;->useAt([Landroid/view/View;)Lmiuix/animation/IFolme;

    move-result-object v0

    invoke-interface {v0}, Lmiuix/animation/IFolme;->hover()Lmiuix/animation/IHoverStyle;

    move-result-object v0

    sget-object v1, Lmiuix/animation/IHoverStyle$HoverEffect;->NORMAL:Lmiuix/animation/IHoverStyle$HoverEffect;

    invoke-interface {v0, v1}, Lmiuix/animation/IHoverStyle;->setEffect(Lmiuix/animation/IHoverStyle$HoverEffect;)Lmiuix/animation/IHoverStyle;

    move-result-object v0

    new-array v1, v3, [Lmiuix/animation/base/AnimConfig;

    invoke-interface {v0, p0, v1}, Lmiuix/animation/IHoverStyle;->handleHoverOf(Landroid/view/View;[Lmiuix/animation/base/AnimConfig;)V

    :cond_3
    return-void
.end method""",
        'replacement': """.method protected onAttachedToWindow()V
    .registers 6

    goto :goto_21

    nop

    :goto_0
    invoke-interface {v0, v1}, Lmiuix/animation/IHoverStyle;->setEffect(Lmiuix/animation/IHoverStyle$HoverEffect;)Lmiuix/animation/IHoverStyle;

    move-result-object v0

    goto :goto_29

    nop

    :goto_1
    move v0, v3

    :goto_2
    goto :goto_2d

    nop

    :goto_3
    const-string v4, "RecyclerView"

    goto :goto_17

    nop

    :goto_4
    if-nez v0, :cond_0

    goto :goto_d

    :cond_0
    goto :goto_14

    nop

    :goto_5
    const/4 v2, 0x1

    goto :goto_1e

    nop

    :goto_6
    invoke-virtual {v0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object v0

    goto :goto_3

    nop

    :goto_7
    invoke-virtual {p0}, Landroid/widget/CheckedTextView;->getForeground()Landroid/graphics/drawable/Drawable;

    move-result-object v0

    goto :goto_4

    nop

    :goto_8
    return-void

    :goto_9
    goto :goto_18

    nop

    :goto_a
    new-array v0, v2, [Landroid/view/View;

    goto :goto_11

    nop

    :goto_b
    invoke-virtual {p0, v0}, Landroid/widget/CheckedTextView;->setOnHoverListener(Landroid/view/View$OnHoverListener;)V

    goto :goto_c

    nop

    :goto_c
    return-void

    :goto_d
    goto :goto_25

    nop

    :goto_e
    return-void

    :goto_f
    invoke-interface {v0, p0, v1}, Lmiuix/animation/IHoverStyle;->handleHoverOf(Landroid/view/View;[Lmiuix/animation/base/AnimConfig;)V

    goto :goto_8

    nop

    :goto_10
    invoke-interface {v0}, Lmiuix/animation/IFolme;->hover()Lmiuix/animation/IHoverStyle;

    move-result-object v0

    goto :goto_12

    nop

    :goto_11
    aput-object p0, v0, v3

    goto :goto_27

    nop

    :goto_12
    sget-object v1, Lmiuix/animation/IHoverStyle$HoverEffect;->NORMAL:Lmiuix/animation/IHoverStyle$HoverEffect;

    goto :goto_0

    nop

    :goto_13
    invoke-virtual {v0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object v0

    goto :goto_6

    nop

    :goto_14
    new-instance v0, Lmiuix/androidbasewidget/widget/AppCompatCheckedTextView$$ExternalSyntheticLambda0;

    goto :goto_16

    nop

    :goto_15
    sget-object v1, Lmiuix/animation/IHoverStyle$HoverEffect;->NORMAL:Lmiuix/animation/IHoverStyle$HoverEffect;

    goto :goto_1d

    nop

    :goto_16
    invoke-direct {v0}, Lmiuix/androidbasewidget/widget/AppCompatCheckedTextView$$ExternalSyntheticLambda0;-><init>()V

    goto :goto_b

    nop

    :goto_17
    invoke-virtual {v0, v4}, Ljava/lang/String;->contains(Ljava/lang/CharSequence;)Z

    move-result v0

    goto :goto_28

    nop

    :goto_18
    invoke-virtual {p0}, Landroid/widget/CheckedTextView;->isClickable()Z

    move-result v0

    goto :goto_2c

    nop

    :goto_19
    goto :goto_2

    :goto_1a
    goto :goto_1

    nop

    :goto_1b
    new-array v1, v3, [Lmiuix/animation/base/AnimConfig;

    goto :goto_2e

    nop

    :goto_1c
    invoke-static {v0}, Lmiuix/animation/Folme;->useAt([Landroid/view/View;)Lmiuix/animation/IFolme;

    move-result-object v0

    goto :goto_24

    nop

    :goto_1d
    invoke-interface {v0, v1}, Lmiuix/animation/IHoverStyle;->setEffect(Lmiuix/animation/IHoverStyle$HoverEffect;)Lmiuix/animation/IHoverStyle;

    move-result-object v0

    goto :goto_1b

    nop

    :goto_1e
    const/4 v3, 0x0

    goto :goto_20

    nop

    :goto_1f
    if-eqz v0, :cond_1

    goto :goto_9

    :cond_1
    goto :goto_a

    nop

    :goto_20
    if-nez v0, :cond_2

    goto :goto_1a

    :cond_2
    goto :goto_13

    nop

    :goto_21
    invoke-super {p0}, Landroid/widget/CheckedTextView;->onAttachedToWindow()V

    goto :goto_2a

    nop

    :goto_22
    aput-object p0, v0, v3

    goto :goto_1c

    nop

    :goto_23
    instance-of v1, v0, Landroid/widget/ListView;

    goto :goto_5

    nop

    :goto_24
    invoke-interface {v0}, Lmiuix/animation/IFolme;->hover()Lmiuix/animation/IHoverStyle;

    move-result-object v0

    goto :goto_15

    nop

    :goto_25
    new-array v0, v2, [Landroid/view/View;

    goto :goto_22

    nop

    :goto_26
    move v0, v2

    goto :goto_19

    nop

    :goto_27
    invoke-static {v0}, Lmiuix/animation/Folme;->useAt([Landroid/view/View;)Lmiuix/animation/IFolme;

    move-result-object v0

    goto :goto_10

    nop

    :goto_28
    if-nez v0, :cond_3

    goto :goto_1a

    :cond_3
    goto :goto_26

    nop

    :goto_29
    new-array v1, v3, [Lmiuix/animation/base/AnimConfig;

    goto :goto_f

    nop

    :goto_2a
    invoke-virtual {p0}, Landroid/widget/CheckedTextView;->getParent()Landroid/view/ViewParent;

    move-result-object v0

    goto :goto_2b

    nop

    :goto_2b
    check-cast v0, Landroid/view/View;

    goto :goto_23

    nop

    :goto_2c
    if-eqz v0, :cond_4

    goto :goto_2f

    :cond_4
    goto :goto_7

    nop

    :goto_2d
    if-eqz v1, :cond_5

    goto :goto_9

    :cond_5
    goto :goto_1f

    nop

    :goto_2e
    invoke-interface {v0, p0, v1}, Lmiuix/animation/IHoverStyle;->handleHoverOf(Landroid/view/View;[Lmiuix/animation/base/AnimConfig;)V

    :goto_2f
    goto :goto_e

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
