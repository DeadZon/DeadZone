TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/visual/check/VisualCheckBox.smali'
CLASS_FALLBACK_NAMES = ['VisualCheckBox.smali']
CLASS_ANCHORS = ['.super Landroid/widget/LinearLayout;']

PATCHES = [
    {
        'id': 'miuix_visual_check_VisualCheckBox__onFinishInflate',
        'method': '.method protected onFinishInflate()V',
        'method_name': 'onFinishInflate',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/LinearLayout;->onFinishInflate()V', 'invoke-virtual {p0}, Landroid/widget/LinearLayout;->getContentDescription()Ljava/lang/CharSequence;', 'invoke-static {v0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z', 'if-eqz v0, :cond_0', 'invoke-direct {p0}, Lmiuix/visual/check/VisualCheckBox;->obtainDescriptionFromChild()Ljava/lang/CharSequence;', 'invoke-static {v0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z', 'if-nez v1, :cond_0', 'invoke-virtual {p0, v0}, Landroid/widget/LinearLayout;->setContentDescription(Ljava/lang/CharSequence;)V'],
        'type': 'method_replace',
        'search': """.method protected onFinishInflate()V
    .registers 3

    invoke-super {p0}, Landroid/widget/LinearLayout;->onFinishInflate()V

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getContentDescription()Ljava/lang/CharSequence;

    move-result-object v0

    invoke-static {v0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v0

    if-eqz v0, :cond_0

    invoke-direct {p0}, Lmiuix/visual/check/VisualCheckBox;->obtainDescriptionFromChild()Ljava/lang/CharSequence;

    move-result-object v0

    invoke-static {v0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v1

    if-nez v1, :cond_0

    invoke-virtual {p0, v0}, Landroid/widget/LinearLayout;->setContentDescription(Ljava/lang/CharSequence;)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onFinishInflate()V
    .registers 3

    goto :goto_1

    nop

    :goto_0
    if-nez v0, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_3

    nop

    :goto_1
    invoke-super {p0}, Landroid/widget/LinearLayout;->onFinishInflate()V

    goto :goto_8

    nop

    :goto_2
    return-void

    :goto_3
    invoke-direct {p0}, Lmiuix/visual/check/VisualCheckBox;->obtainDescriptionFromChild()Ljava/lang/CharSequence;

    move-result-object v0

    goto :goto_7

    nop

    :goto_4
    if-eqz v1, :cond_1

    goto :goto_6

    :cond_1
    goto :goto_5

    nop

    :goto_5
    invoke-virtual {p0, v0}, Landroid/widget/LinearLayout;->setContentDescription(Ljava/lang/CharSequence;)V

    :goto_6
    goto :goto_2

    nop

    :goto_7
    invoke-static {v0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v1

    goto :goto_4

    nop

    :goto_8
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getContentDescription()Ljava/lang/CharSequence;

    move-result-object v0

    goto :goto_9

    nop

    :goto_9
    invoke-static {v0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_visual_check_VisualCheckBox__setOnCheckedChangeWidgetListener',
        'method': '.method setOnCheckedChangeWidgetListener(Lmiuix/visual/check/VisualCheckBox$OnCheckedChangeListener;)V',
        'method_name': 'setOnCheckedChangeWidgetListener',
        'method_anchors': ['iput-object p1, p0, Lmiuix/visual/check/VisualCheckBox;->mOnCheckedChangeWidgetListener:Lmiuix/visual/check/VisualCheckBox$OnCheckedChangeListener;', 'return-void'],
        'type': 'method_replace',
        'search': """.method setOnCheckedChangeWidgetListener(Lmiuix/visual/check/VisualCheckBox$OnCheckedChangeListener;)V
    .registers 2

    iput-object p1, p0, Lmiuix/visual/check/VisualCheckBox;->mOnCheckedChangeWidgetListener:Lmiuix/visual/check/VisualCheckBox$OnCheckedChangeListener;

    return-void
.end method""",
        'replacement': """.method setOnCheckedChangeWidgetListener(Lmiuix/visual/check/VisualCheckBox$OnCheckedChangeListener;)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    iput-object p1, p0, Lmiuix/visual/check/VisualCheckBox;->mOnCheckedChangeWidgetListener:Lmiuix/visual/check/VisualCheckBox$OnCheckedChangeListener;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
