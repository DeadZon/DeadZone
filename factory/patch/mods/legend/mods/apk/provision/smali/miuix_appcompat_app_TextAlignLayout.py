TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/app/TextAlignLayout.smali'
CLASS_FALLBACK_NAMES = ['TextAlignLayout.smali']
CLASS_ANCHORS = ['.super Landroid/widget/LinearLayout;']

PATCHES = [
    {
        'id': 'miuix_appcompat_app_TextAlignLayout__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['invoke-super {p0, p1, p2}, Landroid/widget/LinearLayout;->onMeasure(II)V', 'invoke-virtual {p0}, Landroid/widget/LinearLayout;->getChildCount()I', 'if-ge v1, p1, :cond_4', 'invoke-virtual {p0, v1}, Landroid/widget/LinearLayout;->getChildAt(I)Landroid/view/View;', 'if-eqz v2, :cond_3', 'if-eqz v4, :cond_3', 'check-cast v2, Landroid/widget/TextView;', 'invoke-virtual {v2}, Landroid/widget/TextView;->getLineCount()I'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 8

    invoke-super {p0, p1, p2}, Landroid/widget/LinearLayout;->onMeasure(II)V

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getChildCount()I

    move-result p1

    const/4 p2, 0x1

    const/4 v0, 0x0

    move v2, p2

    move v1, v0

    :goto_0
    if-ge v1, p1, :cond_4

    invoke-virtual {p0, v1}, Landroid/widget/LinearLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v3

    if-eqz v2, :cond_3

    instance-of v4, v3, Landroid/widget/TextView;

    if-eqz v4, :cond_3

    move-object v2, v3

    check-cast v2, Landroid/widget/TextView;

    invoke-virtual {v2}, Landroid/widget/TextView;->getLineCount()I

    move-result v4

    if-gt v4, p2, :cond_0

    iget-boolean v4, p0, Lmiuix/appcompat/app/TextAlignLayout;->mDialogPanelHasCheckbox:Z

    if-nez v4, :cond_0

    move v4, p2

    goto :goto_1

    :cond_0
    move v4, v0

    :goto_1
    if-eqz v4, :cond_1

    invoke-virtual {v2, p2}, Landroid/widget/TextView;->setGravity(I)V

    goto :goto_3

    :cond_1
    invoke-static {v3}, Lmiuix/internal/util/ViewUtils;->isLayoutRtl(Landroid/view/View;)Z

    move-result v3

    if-eqz v3, :cond_2

    const/4 v3, 0x5

    goto :goto_2

    :cond_2
    const/4 v3, 0x3

    :goto_2
    invoke-virtual {v2, v3}, Landroid/widget/TextView;->setGravity(I)V

    :goto_3
    move v2, v4

    :cond_3
    add-int/lit8 v1, v1, 0x1

    goto :goto_0

    :cond_4
    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 8

    goto :goto_1d

    nop

    :goto_0
    move v2, v4

    :goto_1
    goto :goto_a

    nop

    :goto_2
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getChildCount()I

    move-result p1

    goto :goto_20

    nop

    :goto_3
    invoke-virtual {p0, v1}, Landroid/widget/LinearLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v3

    goto :goto_16

    nop

    :goto_4
    if-eqz v4, :cond_0

    goto :goto_9

    :cond_0
    goto :goto_1c

    nop

    :goto_5
    instance-of v4, v3, Landroid/widget/TextView;

    goto :goto_13

    nop

    :goto_6
    goto :goto_15

    :goto_7
    goto :goto_1a

    nop

    :goto_8
    goto :goto_22

    :goto_9
    goto :goto_21

    nop

    :goto_a
    add-int/lit8 v1, v1, 0x1

    goto :goto_1e

    nop

    :goto_b
    invoke-virtual {v2}, Landroid/widget/TextView;->getLineCount()I

    move-result v4

    goto :goto_12

    nop

    :goto_c
    goto :goto_f

    :goto_d
    goto :goto_e

    nop

    :goto_e
    const/4 v3, 0x3

    :goto_f
    goto :goto_14

    nop

    :goto_10
    if-nez v4, :cond_1

    goto :goto_7

    :cond_1
    goto :goto_1b

    nop

    :goto_11
    const/4 v0, 0x0

    goto :goto_17

    nop

    :goto_12
    if-le v4, p2, :cond_2

    goto :goto_9

    :cond_2
    goto :goto_29

    nop

    :goto_13
    if-nez v4, :cond_3

    goto :goto_1

    :cond_3
    goto :goto_24

    nop

    :goto_14
    invoke-virtual {v2, v3}, Landroid/widget/TextView;->setGravity(I)V

    :goto_15
    goto :goto_0

    nop

    :goto_16
    if-nez v2, :cond_4

    goto :goto_1

    :cond_4
    goto :goto_5

    nop

    :goto_17
    move v2, p2

    goto :goto_27

    nop

    :goto_18
    return-void

    :goto_19
    if-lt v1, p1, :cond_5

    goto :goto_1f

    :cond_5
    goto :goto_3

    nop

    :goto_1a
    invoke-static {v3}, Lmiuix/internal/util/ViewUtils;->isLayoutRtl(Landroid/view/View;)Z

    move-result v3

    goto :goto_26

    nop

    :goto_1b
    invoke-virtual {v2, p2}, Landroid/widget/TextView;->setGravity(I)V

    goto :goto_6

    nop

    :goto_1c
    move v4, p2

    goto :goto_8

    nop

    :goto_1d
    invoke-super {p0, p1, p2}, Landroid/widget/LinearLayout;->onMeasure(II)V

    goto :goto_2

    nop

    :goto_1e
    goto :goto_28

    :goto_1f
    goto :goto_18

    nop

    :goto_20
    const/4 p2, 0x1

    goto :goto_11

    nop

    :goto_21
    move v4, v0

    :goto_22
    goto :goto_10

    nop

    :goto_23
    check-cast v2, Landroid/widget/TextView;

    goto :goto_b

    nop

    :goto_24
    move-object v2, v3

    goto :goto_23

    nop

    :goto_25
    const/4 v3, 0x5

    goto :goto_c

    nop

    :goto_26
    if-nez v3, :cond_6

    goto :goto_d

    :cond_6
    goto :goto_25

    nop

    :goto_27
    move v1, v0

    :goto_28
    goto :goto_19

    nop

    :goto_29
    iget-boolean v4, p0, Lmiuix/appcompat/app/TextAlignLayout;->mDialogPanelHasCheckbox:Z

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
