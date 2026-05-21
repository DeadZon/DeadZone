TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/flexible/view/HyperCellLayout.smali'
CLASS_FALLBACK_NAMES = ['HyperCellLayout.smali']
CLASS_ANCHORS = ['.super Landroid/view/ViewGroup;']

PATCHES = [
    {
        'id': 'miuix_flexible_view_HyperCellLayout__generateDefaultLayoutParams',
        'method': '.method protected bridge synthetic generateDefaultLayoutParams()Landroid/view/ViewGroup$LayoutParams;',
        'method_name': 'generateDefaultLayoutParams',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/flexible/view/HyperCellLayout;->generateDefaultLayoutParams()Lmiuix/flexible/view/HyperCellLayout$LayoutParams;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected bridge synthetic generateDefaultLayoutParams()Landroid/view/ViewGroup$LayoutParams;
    .registers 1

    invoke-virtual {p0}, Lmiuix/flexible/view/HyperCellLayout;->generateDefaultLayoutParams()Lmiuix/flexible/view/HyperCellLayout$LayoutParams;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected bridge synthetic generateDefaultLayoutParams()Landroid/view/ViewGroup$LayoutParams;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    invoke-virtual {p0}, Lmiuix/flexible/view/HyperCellLayout;->generateDefaultLayoutParams()Lmiuix/flexible/view/HyperCellLayout$LayoutParams;

    move-result-object p0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_flexible_view_HyperCellLayout__generateLayoutParams',
        'method': '.method protected bridge synthetic generateLayoutParams(Landroid/view/ViewGroup$LayoutParams;)Landroid/view/ViewGroup$LayoutParams;',
        'method_name': 'generateLayoutParams',
        'method_anchors': ['invoke-virtual {p0, p1}, Lmiuix/flexible/view/HyperCellLayout;->generateLayoutParams(Landroid/view/ViewGroup$LayoutParams;)Lmiuix/flexible/view/HyperCellLayout$LayoutParams;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected bridge synthetic generateLayoutParams(Landroid/view/ViewGroup$LayoutParams;)Landroid/view/ViewGroup$LayoutParams;
    .registers 2

    invoke-virtual {p0, p1}, Lmiuix/flexible/view/HyperCellLayout;->generateLayoutParams(Landroid/view/ViewGroup$LayoutParams;)Lmiuix/flexible/view/HyperCellLayout$LayoutParams;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected bridge synthetic generateLayoutParams(Landroid/view/ViewGroup$LayoutParams;)Landroid/view/ViewGroup$LayoutParams;
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    invoke-virtual {p0, p1}, Lmiuix/flexible/view/HyperCellLayout;->generateLayoutParams(Landroid/view/ViewGroup$LayoutParams;)Lmiuix/flexible/view/HyperCellLayout$LayoutParams;

    move-result-object p0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_flexible_view_HyperCellLayout__checkLayoutParams',
        'method': '.method protected checkLayoutParams(Landroid/view/ViewGroup$LayoutParams;)Z',
        'method_name': 'checkLayoutParams',
        'method_anchors': ['return p0'],
        'type': 'method_replace',
        'search': """.method protected checkLayoutParams(Landroid/view/ViewGroup$LayoutParams;)Z
    .registers 2

    instance-of p0, p1, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;

    return p0
.end method""",
        'replacement': """.method protected checkLayoutParams(Landroid/view/ViewGroup$LayoutParams;)Z
    .registers 2

    goto :goto_0

    nop

    :goto_0
    instance-of p0, p1, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;

    goto :goto_1

    nop

    :goto_1
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_flexible_view_HyperCellLayout__createTemplate',
        'method': '.method protected createTemplate(Landroid/content/Context;Ljava/lang/String;Landroid/util/AttributeSet;)Lmiuix/flexible/template/IHyperCellTemplate;',
        'method_name': 'createTemplate',
        'method_anchors': ['invoke-static {p1, p2}, Lmiuix/flexible/template/TemplateFactory;->get(Landroid/content/Context;Ljava/lang/String;)Lmiuix/flexible/template/IHyperCellTemplate;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected createTemplate(Landroid/content/Context;Ljava/lang/String;Landroid/util/AttributeSet;)Lmiuix/flexible/template/IHyperCellTemplate;
    .registers 4

    invoke-static {p1, p2}, Lmiuix/flexible/template/TemplateFactory;->get(Landroid/content/Context;Ljava/lang/String;)Lmiuix/flexible/template/IHyperCellTemplate;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected createTemplate(Landroid/content/Context;Ljava/lang/String;Landroid/util/AttributeSet;)Lmiuix/flexible/template/IHyperCellTemplate;
    .registers 4

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    invoke-static {p1, p2}, Lmiuix/flexible/template/TemplateFactory;->get(Landroid/content/Context;Ljava/lang/String;)Lmiuix/flexible/template/IHyperCellTemplate;

    move-result-object p0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_flexible_view_HyperCellLayout__generateDefaultLayoutParams',
        'method': '.method protected generateDefaultLayoutParams()Lmiuix/flexible/view/HyperCellLayout$LayoutParams;',
        'method_name': 'generateDefaultLayoutParams',
        'method_anchors': ['new-instance p0, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;', 'invoke-direct {p0, v0, v0}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;-><init>(II)V', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected generateDefaultLayoutParams()Lmiuix/flexible/view/HyperCellLayout$LayoutParams;
    .registers 2

    new-instance p0, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;

    const/4 v0, -0x2

    invoke-direct {p0, v0, v0}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;-><init>(II)V

    return-object p0
.end method""",
        'replacement': """.method protected generateDefaultLayoutParams()Lmiuix/flexible/view/HyperCellLayout$LayoutParams;
    .registers 2

    goto :goto_3

    nop

    :goto_0
    invoke-direct {p0, v0, v0}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;-><init>(II)V

    goto :goto_2

    nop

    :goto_1
    const/4 v0, -0x2

    goto :goto_0

    nop

    :goto_2
    return-object p0

    :goto_3
    new-instance p0, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_flexible_view_HyperCellLayout__generateLayoutParams',
        'method': '.method protected generateLayoutParams(Landroid/view/ViewGroup$LayoutParams;)Lmiuix/flexible/view/HyperCellLayout$LayoutParams;',
        'method_name': 'generateLayoutParams',
        'method_anchors': ['new-instance p0, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;', 'invoke-direct {p0, p1}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;-><init>(Landroid/view/ViewGroup$LayoutParams;)V', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected generateLayoutParams(Landroid/view/ViewGroup$LayoutParams;)Lmiuix/flexible/view/HyperCellLayout$LayoutParams;
    .registers 2

    new-instance p0, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;

    invoke-direct {p0, p1}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;-><init>(Landroid/view/ViewGroup$LayoutParams;)V

    return-object p0
.end method""",
        'replacement': """.method protected generateLayoutParams(Landroid/view/ViewGroup$LayoutParams;)Lmiuix/flexible/view/HyperCellLayout$LayoutParams;
    .registers 2

    goto :goto_0

    nop

    :goto_0
    new-instance p0, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;

    goto :goto_1

    nop

    :goto_1
    invoke-direct {p0, p1}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;-><init>(Landroid/view/ViewGroup$LayoutParams;)V

    goto :goto_2

    nop

    :goto_2
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_flexible_view_HyperCellLayout__onAttachedToWindow',
        'method': '.method protected onAttachedToWindow()V',
        'method_name': 'onAttachedToWindow',
        'method_anchors': ['invoke-super {p0}, Landroid/view/ViewGroup;->onAttachedToWindow()V', 'iget-object v0, p0, Lmiuix/flexible/view/HyperCellLayout;->mTemplate:Lmiuix/flexible/template/IHyperCellTemplate;', 'invoke-interface {v0, p0}, Lmiuix/flexible/template/IHyperCellTemplate;->onAttachedToWindow(Landroid/view/ViewGroup;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onAttachedToWindow()V
    .registers 2

    invoke-super {p0}, Landroid/view/ViewGroup;->onAttachedToWindow()V

    iget-object v0, p0, Lmiuix/flexible/view/HyperCellLayout;->mTemplate:Lmiuix/flexible/template/IHyperCellTemplate;

    invoke-interface {v0, p0}, Lmiuix/flexible/template/IHyperCellTemplate;->onAttachedToWindow(Landroid/view/ViewGroup;)V

    return-void
.end method""",
        'replacement': """.method protected onAttachedToWindow()V
    .registers 2

    goto :goto_2

    nop

    :goto_0
    iget-object v0, p0, Lmiuix/flexible/view/HyperCellLayout;->mTemplate:Lmiuix/flexible/template/IHyperCellTemplate;

    goto :goto_3

    nop

    :goto_1
    return-void

    :goto_2
    invoke-super {p0}, Landroid/view/ViewGroup;->onAttachedToWindow()V

    goto :goto_0

    nop

    :goto_3
    invoke-interface {v0, p0}, Lmiuix/flexible/template/IHyperCellTemplate;->onAttachedToWindow(Landroid/view/ViewGroup;)V

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_flexible_view_HyperCellLayout__onConfigurationChanged',
        'method': '.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V',
        'method_name': 'onConfigurationChanged',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/view/ViewGroup;->onConfigurationChanged(Landroid/content/res/Configuration;)V', 'iget-object v0, p0, Lmiuix/flexible/view/HyperCellLayout;->mTemplate:Lmiuix/flexible/template/IHyperCellTemplate;', 'invoke-interface {v0, p0, p1}, Lmiuix/flexible/template/IHyperCellTemplate;->onConfigurationChanged(Landroid/view/ViewGroup;Landroid/content/res/Configuration;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 3

    invoke-super {p0, p1}, Landroid/view/ViewGroup;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    iget-object v0, p0, Lmiuix/flexible/view/HyperCellLayout;->mTemplate:Lmiuix/flexible/template/IHyperCellTemplate;

    invoke-interface {v0, p0, p1}, Lmiuix/flexible/template/IHyperCellTemplate;->onConfigurationChanged(Landroid/view/ViewGroup;Landroid/content/res/Configuration;)V

    return-void
.end method""",
        'replacement': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 3

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0, p1}, Landroid/view/ViewGroup;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    goto :goto_2

    nop

    :goto_1
    return-void

    :goto_2
    iget-object v0, p0, Lmiuix/flexible/view/HyperCellLayout;->mTemplate:Lmiuix/flexible/template/IHyperCellTemplate;

    goto :goto_3

    nop

    :goto_3
    invoke-interface {v0, p0, p1}, Lmiuix/flexible/template/IHyperCellTemplate;->onConfigurationChanged(Landroid/view/ViewGroup;Landroid/content/res/Configuration;)V

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_flexible_view_HyperCellLayout__onDetachedFromWindow',
        'method': '.method protected onDetachedFromWindow()V',
        'method_name': 'onDetachedFromWindow',
        'method_anchors': ['invoke-super {p0}, Landroid/view/ViewGroup;->onDetachedFromWindow()V', 'iget-object v0, p0, Lmiuix/flexible/view/HyperCellLayout;->mTemplate:Lmiuix/flexible/template/IHyperCellTemplate;', 'invoke-interface {v0, p0}, Lmiuix/flexible/template/IHyperCellTemplate;->onDetachedFromWindow(Landroid/view/ViewGroup;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onDetachedFromWindow()V
    .registers 2

    invoke-super {p0}, Landroid/view/ViewGroup;->onDetachedFromWindow()V

    iget-object v0, p0, Lmiuix/flexible/view/HyperCellLayout;->mTemplate:Lmiuix/flexible/template/IHyperCellTemplate;

    invoke-interface {v0, p0}, Lmiuix/flexible/template/IHyperCellTemplate;->onDetachedFromWindow(Landroid/view/ViewGroup;)V

    return-void
.end method""",
        'replacement': """.method protected onDetachedFromWindow()V
    .registers 2

    goto :goto_3

    nop

    :goto_0
    invoke-interface {v0, p0}, Lmiuix/flexible/template/IHyperCellTemplate;->onDetachedFromWindow(Landroid/view/ViewGroup;)V

    goto :goto_1

    nop

    :goto_1
    return-void

    :goto_2
    iget-object v0, p0, Lmiuix/flexible/view/HyperCellLayout;->mTemplate:Lmiuix/flexible/template/IHyperCellTemplate;

    goto :goto_0

    nop

    :goto_3
    invoke-super {p0}, Landroid/view/ViewGroup;->onDetachedFromWindow()V

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_flexible_view_HyperCellLayout__onFinishInflate',
        'method': '.method protected onFinishInflate()V',
        'method_name': 'onFinishInflate',
        'method_anchors': ['invoke-super {p0}, Landroid/view/ViewGroup;->onFinishInflate()V', 'iget-object v0, p0, Lmiuix/flexible/view/HyperCellLayout;->mTemplate:Lmiuix/flexible/template/IHyperCellTemplate;', 'invoke-interface {v0, p0}, Lmiuix/flexible/template/IHyperCellTemplate;->onFinishInflate(Landroid/view/ViewGroup;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onFinishInflate()V
    .registers 2

    invoke-super {p0}, Landroid/view/ViewGroup;->onFinishInflate()V

    iget-object v0, p0, Lmiuix/flexible/view/HyperCellLayout;->mTemplate:Lmiuix/flexible/template/IHyperCellTemplate;

    invoke-interface {v0, p0}, Lmiuix/flexible/template/IHyperCellTemplate;->onFinishInflate(Landroid/view/ViewGroup;)V

    return-void
.end method""",
        'replacement': """.method protected onFinishInflate()V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    iget-object v0, p0, Lmiuix/flexible/view/HyperCellLayout;->mTemplate:Lmiuix/flexible/template/IHyperCellTemplate;

    goto :goto_3

    nop

    :goto_1
    invoke-super {p0}, Landroid/view/ViewGroup;->onFinishInflate()V

    goto :goto_0

    nop

    :goto_2
    return-void

    :goto_3
    invoke-interface {v0, p0}, Lmiuix/flexible/template/IHyperCellTemplate;->onFinishInflate(Landroid/view/ViewGroup;)V

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_flexible_view_HyperCellLayout__onLayout',
        'method': '.method protected onLayout(ZIIII)V',
        'method_name': 'onLayout',
        'method_anchors': ['iget-object v0, p0, Lmiuix/flexible/view/HyperCellLayout;->mTemplate:Lmiuix/flexible/template/IHyperCellTemplate;', 'invoke-interface/range {v0 .. v6}, Lmiuix/flexible/template/IHyperCellTemplate;->onLayout(Landroid/view/ViewGroup;ZIIII)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onLayout(ZIIII)V
    .registers 13

    iget-object v0, p0, Lmiuix/flexible/view/HyperCellLayout;->mTemplate:Lmiuix/flexible/template/IHyperCellTemplate;

    move-object v1, p0

    move v2, p1

    move v3, p2

    move v4, p3

    move v5, p4

    move v6, p5

    invoke-interface/range {v0 .. v6}, Lmiuix/flexible/template/IHyperCellTemplate;->onLayout(Landroid/view/ViewGroup;ZIIII)V

    return-void
.end method""",
        'replacement': """.method protected onLayout(ZIIII)V
    .registers 13

    goto :goto_2

    nop

    :goto_0
    move v2, p1

    goto :goto_3

    nop

    :goto_1
    move v5, p4

    goto :goto_6

    nop

    :goto_2
    iget-object v0, p0, Lmiuix/flexible/view/HyperCellLayout;->mTemplate:Lmiuix/flexible/template/IHyperCellTemplate;

    goto :goto_4

    nop

    :goto_3
    move v3, p2

    goto :goto_7

    nop

    :goto_4
    move-object v1, p0

    goto :goto_0

    nop

    :goto_5
    invoke-interface/range {v0 .. v6}, Lmiuix/flexible/template/IHyperCellTemplate;->onLayout(Landroid/view/ViewGroup;ZIIII)V

    goto :goto_8

    nop

    :goto_6
    move v6, p5

    goto :goto_5

    nop

    :goto_7
    move v4, p3

    goto :goto_1

    nop

    :goto_8
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_flexible_view_HyperCellLayout__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['iget-object v0, p0, Lmiuix/flexible/view/HyperCellLayout;->mTemplate:Lmiuix/flexible/template/IHyperCellTemplate;', 'invoke-interface {v0, p0, p1, p2}, Lmiuix/flexible/template/IHyperCellTemplate;->onMeasure(Landroid/view/ViewGroup;II)[I', 'invoke-virtual {p0, p2, p1}, Landroid/view/ViewGroup;->setMeasuredDimension(II)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 4

    iget-object v0, p0, Lmiuix/flexible/view/HyperCellLayout;->mTemplate:Lmiuix/flexible/template/IHyperCellTemplate;

    invoke-interface {v0, p0, p1, p2}, Lmiuix/flexible/template/IHyperCellTemplate;->onMeasure(Landroid/view/ViewGroup;II)[I

    move-result-object p1

    const/4 p2, 0x0

    aget p2, p1, p2

    const/4 v0, 0x1

    aget p1, p1, v0

    invoke-virtual {p0, p2, p1}, Landroid/view/ViewGroup;->setMeasuredDimension(II)V

    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 4

    goto :goto_2

    nop

    :goto_0
    const/4 v0, 0x1

    goto :goto_1

    nop

    :goto_1
    aget p1, p1, v0

    goto :goto_5

    nop

    :goto_2
    iget-object v0, p0, Lmiuix/flexible/view/HyperCellLayout;->mTemplate:Lmiuix/flexible/template/IHyperCellTemplate;

    goto :goto_3

    nop

    :goto_3
    invoke-interface {v0, p0, p1, p2}, Lmiuix/flexible/template/IHyperCellTemplate;->onMeasure(Landroid/view/ViewGroup;II)[I

    move-result-object p1

    goto :goto_6

    nop

    :goto_4
    aget p2, p1, p2

    goto :goto_0

    nop

    :goto_5
    invoke-virtual {p0, p2, p1}, Landroid/view/ViewGroup;->setMeasuredDimension(II)V

    goto :goto_7

    nop

    :goto_6
    const/4 p2, 0x0

    goto :goto_4

    nop

    :goto_7
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
