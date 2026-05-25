TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/widget/Spinner.smali'
CLASS_FALLBACK_NAMES = ['Spinner.smali']
CLASS_ANCHORS = ['.super Landroid/widget/Spinner;']

PATCHES = [
    {
        'id': 'miuix_appcompat_widget_Spinner__onConfigurationChanged',
        'method': '.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V',
        'method_name': 'onConfigurationChanged',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/widget/Spinner;->onConfigurationChanged(Landroid/content/res/Configuration;)V', 'invoke-virtual {p0}, Landroid/widget/Spinner;->getContext()Landroid/content/Context;', 'invoke-virtual {p1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;', 'invoke-virtual {p1}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;', 'iget p1, p1, Landroid/util/DisplayMetrics;->density:F', 'iget v0, p0, Lmiuix/appcompat/widget/Spinner;->mLastDensity:F', 'if-eqz v0, :cond_0', 'iput p1, p0, Lmiuix/appcompat/widget/Spinner;->mLastDensity:F'],
        'type': 'method_replace',
        'search': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 3

    invoke-super {p0, p1}, Landroid/widget/Spinner;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    invoke-virtual {p0}, Landroid/widget/Spinner;->getContext()Landroid/content/Context;

    move-result-object p1

    invoke-virtual {p1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object p1

    invoke-virtual {p1}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;

    move-result-object p1

    iget p1, p1, Landroid/util/DisplayMetrics;->density:F

    iget v0, p0, Lmiuix/appcompat/widget/Spinner;->mLastDensity:F

    cmpl-float v0, v0, p1

    if-eqz v0, :cond_0

    iput p1, p0, Lmiuix/appcompat/widget/Spinner;->mLastDensity:F

    invoke-virtual {p0}, Landroid/widget/Spinner;->getOnItemSelectedListener()Landroid/widget/AdapterView$OnItemSelectedListener;

    move-result-object p1

    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Landroid/widget/Spinner;->setOnItemSelectedListener(Landroid/widget/AdapterView$OnItemSelectedListener;)V

    invoke-virtual {p0}, Landroid/widget/Spinner;->getAdapter()Landroid/widget/SpinnerAdapter;

    move-result-object v0

    invoke-virtual {p0, v0}, Lmiuix/appcompat/widget/Spinner;->setAdapter(Landroid/widget/SpinnerAdapter;)V

    new-instance v0, Lmiuix/appcompat/widget/Spinner$1;

    invoke-direct {v0, p0, p1}, Lmiuix/appcompat/widget/Spinner$1;-><init>(Lmiuix/appcompat/widget/Spinner;Landroid/widget/AdapterView$OnItemSelectedListener;)V

    invoke-virtual {p0, v0}, Landroid/widget/Spinner;->post(Ljava/lang/Runnable;)Z

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 3

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0, p1}, Landroid/widget/Spinner;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    goto :goto_9

    nop

    :goto_1
    invoke-virtual {p0}, Landroid/widget/Spinner;->getAdapter()Landroid/widget/SpinnerAdapter;

    move-result-object v0

    goto :goto_7

    nop

    :goto_2
    iget p1, p1, Landroid/util/DisplayMetrics;->density:F

    goto :goto_12

    nop

    :goto_3
    invoke-virtual {p0, v0}, Landroid/widget/Spinner;->post(Ljava/lang/Runnable;)Z

    :goto_4
    goto :goto_e

    nop

    :goto_5
    cmpl-float v0, v0, p1

    goto :goto_b

    nop

    :goto_6
    invoke-direct {v0, p0, p1}, Lmiuix/appcompat/widget/Spinner$1;-><init>(Lmiuix/appcompat/widget/Spinner;Landroid/widget/AdapterView$OnItemSelectedListener;)V

    goto :goto_3

    nop

    :goto_7
    invoke-virtual {p0, v0}, Lmiuix/appcompat/widget/Spinner;->setAdapter(Landroid/widget/SpinnerAdapter;)V

    goto :goto_8

    nop

    :goto_8
    new-instance v0, Lmiuix/appcompat/widget/Spinner$1;

    goto :goto_6

    nop

    :goto_9
    invoke-virtual {p0}, Landroid/widget/Spinner;->getContext()Landroid/content/Context;

    move-result-object p1

    goto :goto_c

    nop

    :goto_a
    const/4 v0, 0x0

    goto :goto_11

    nop

    :goto_b
    if-nez v0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_d

    nop

    :goto_c
    invoke-virtual {p1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object p1

    goto :goto_10

    nop

    :goto_d
    iput p1, p0, Lmiuix/appcompat/widget/Spinner;->mLastDensity:F

    goto :goto_f

    nop

    :goto_e
    return-void

    :goto_f
    invoke-virtual {p0}, Landroid/widget/Spinner;->getOnItemSelectedListener()Landroid/widget/AdapterView$OnItemSelectedListener;

    move-result-object p1

    goto :goto_a

    nop

    :goto_10
    invoke-virtual {p1}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;

    move-result-object p1

    goto :goto_2

    nop

    :goto_11
    invoke-virtual {p0, v0}, Landroid/widget/Spinner;->setOnItemSelectedListener(Landroid/widget/AdapterView$OnItemSelectedListener;)V

    goto :goto_1

    nop

    :goto_12
    iget v0, p0, Lmiuix/appcompat/widget/Spinner;->mLastDensity:F

    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_widget_Spinner__onDetachedFromWindow',
        'method': '.method protected onDetachedFromWindow()V',
        'method_name': 'onDetachedFromWindow',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/Spinner;->onDetachedFromWindow()V', 'iget-object v0, p0, Lmiuix/appcompat/widget/Spinner;->mPopup:Lmiuix/appcompat/widget/Spinner$SpinnerPopup;', 'if-eqz v0, :cond_0', 'invoke-interface {v0}, Lmiuix/appcompat/widget/Spinner$SpinnerPopup;->isShowing()Z', 'if-eqz v0, :cond_0', 'iget-object p0, p0, Lmiuix/appcompat/widget/Spinner;->mPopup:Lmiuix/appcompat/widget/Spinner$SpinnerPopup;', 'invoke-interface {p0}, Lmiuix/appcompat/widget/Spinner$SpinnerPopup;->dismiss()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onDetachedFromWindow()V
    .registers 2

    invoke-super {p0}, Landroid/widget/Spinner;->onDetachedFromWindow()V

    iget-object v0, p0, Lmiuix/appcompat/widget/Spinner;->mPopup:Lmiuix/appcompat/widget/Spinner$SpinnerPopup;

    if-eqz v0, :cond_0

    invoke-interface {v0}, Lmiuix/appcompat/widget/Spinner$SpinnerPopup;->isShowing()Z

    move-result v0

    if-eqz v0, :cond_0

    iget-object p0, p0, Lmiuix/appcompat/widget/Spinner;->mPopup:Lmiuix/appcompat/widget/Spinner$SpinnerPopup;

    invoke-interface {p0}, Lmiuix/appcompat/widget/Spinner$SpinnerPopup;->dismiss()V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onDetachedFromWindow()V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0}, Landroid/widget/Spinner;->onDetachedFromWindow()V

    goto :goto_1

    nop

    :goto_1
    iget-object v0, p0, Lmiuix/appcompat/widget/Spinner;->mPopup:Lmiuix/appcompat/widget/Spinner$SpinnerPopup;

    goto :goto_6

    nop

    :goto_2
    invoke-interface {v0}, Lmiuix/appcompat/widget/Spinner$SpinnerPopup;->isShowing()Z

    move-result v0

    goto :goto_5

    nop

    :goto_3
    invoke-interface {p0}, Lmiuix/appcompat/widget/Spinner$SpinnerPopup;->dismiss()V

    :goto_4
    goto :goto_8

    nop

    :goto_5
    if-nez v0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_7

    nop

    :goto_6
    if-nez v0, :cond_1

    goto :goto_4

    :cond_1
    goto :goto_2

    nop

    :goto_7
    iget-object p0, p0, Lmiuix/appcompat/widget/Spinner;->mPopup:Lmiuix/appcompat/widget/Spinner$SpinnerPopup;

    goto :goto_3

    nop

    :goto_8
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_widget_Spinner__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['invoke-super {p0, p1, p2}, Landroid/widget/Spinner;->onMeasure(II)V', 'iget-object p2, p0, Lmiuix/appcompat/widget/Spinner;->mPopup:Lmiuix/appcompat/widget/Spinner$SpinnerPopup;', 'if-eqz p2, :cond_0', 'invoke-static {p1}, Landroid/view/View$MeasureSpec;->getMode(I)I', 'if-ne p2, v0, :cond_0', 'invoke-virtual {p0}, Landroid/widget/Spinner;->getMeasuredWidth()I', 'invoke-virtual {p0}, Landroid/widget/Spinner;->getAdapter()Landroid/widget/SpinnerAdapter;', 'invoke-virtual {p0}, Landroid/widget/Spinner;->getBackground()Landroid/graphics/drawable/Drawable;'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 5

    invoke-super {p0, p1, p2}, Landroid/widget/Spinner;->onMeasure(II)V

    iget-object p2, p0, Lmiuix/appcompat/widget/Spinner;->mPopup:Lmiuix/appcompat/widget/Spinner$SpinnerPopup;

    if-eqz p2, :cond_0

    invoke-static {p1}, Landroid/view/View$MeasureSpec;->getMode(I)I

    move-result p2

    const/high16 v0, -0x80000000

    if-ne p2, v0, :cond_0

    invoke-virtual {p0}, Landroid/widget/Spinner;->getMeasuredWidth()I

    move-result p2

    invoke-virtual {p0}, Landroid/widget/Spinner;->getAdapter()Landroid/widget/SpinnerAdapter;

    move-result-object v0

    invoke-virtual {p0}, Landroid/widget/Spinner;->getBackground()Landroid/graphics/drawable/Drawable;

    move-result-object v1

    invoke-direct {p0, v0, v1}, Lmiuix/appcompat/widget/Spinner;->compatMeasureSelectItemWidth(Landroid/widget/SpinnerAdapter;Landroid/graphics/drawable/Drawable;)I

    move-result v0

    invoke-static {p2, v0}, Ljava/lang/Math;->min(II)I

    move-result p2

    invoke-static {p1}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result p1

    invoke-static {p2, p1}, Ljava/lang/Math;->min(II)I

    move-result p1

    invoke-virtual {p0}, Landroid/widget/Spinner;->getMeasuredHeight()I

    move-result p2

    invoke-virtual {p0, p1, p2}, Landroid/widget/Spinner;->setMeasuredDimension(II)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 5

    goto :goto_9

    nop

    :goto_0
    invoke-direct {p0, v0, v1}, Lmiuix/appcompat/widget/Spinner;->compatMeasureSelectItemWidth(Landroid/widget/SpinnerAdapter;Landroid/graphics/drawable/Drawable;)I

    move-result v0

    goto :goto_f

    nop

    :goto_1
    invoke-virtual {p0}, Landroid/widget/Spinner;->getAdapter()Landroid/widget/SpinnerAdapter;

    move-result-object v0

    goto :goto_d

    nop

    :goto_2
    invoke-virtual {p0}, Landroid/widget/Spinner;->getMeasuredHeight()I

    move-result p2

    goto :goto_7

    nop

    :goto_3
    if-nez p2, :cond_0

    goto :goto_8

    :cond_0
    goto :goto_6

    nop

    :goto_4
    invoke-static {p2, p1}, Ljava/lang/Math;->min(II)I

    move-result p1

    goto :goto_2

    nop

    :goto_5
    if-eq p2, v0, :cond_1

    goto :goto_8

    :cond_1
    goto :goto_a

    nop

    :goto_6
    invoke-static {p1}, Landroid/view/View$MeasureSpec;->getMode(I)I

    move-result p2

    goto :goto_c

    nop

    :goto_7
    invoke-virtual {p0, p1, p2}, Landroid/widget/Spinner;->setMeasuredDimension(II)V

    :goto_8
    goto :goto_b

    nop

    :goto_9
    invoke-super {p0, p1, p2}, Landroid/widget/Spinner;->onMeasure(II)V

    goto :goto_10

    nop

    :goto_a
    invoke-virtual {p0}, Landroid/widget/Spinner;->getMeasuredWidth()I

    move-result p2

    goto :goto_1

    nop

    :goto_b
    return-void

    :goto_c
    const/high16 v0, -0x80000000

    goto :goto_5

    nop

    :goto_d
    invoke-virtual {p0}, Landroid/widget/Spinner;->getBackground()Landroid/graphics/drawable/Drawable;

    move-result-object v1

    goto :goto_0

    nop

    :goto_e
    invoke-static {p1}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result p1

    goto :goto_4

    nop

    :goto_f
    invoke-static {p2, v0}, Ljava/lang/Math;->min(II)I

    move-result p2

    goto :goto_e

    nop

    :goto_10
    iget-object p2, p0, Lmiuix/appcompat/widget/Spinner;->mPopup:Lmiuix/appcompat/widget/Spinner$SpinnerPopup;

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_widget_Spinner__showPopup',
        'method': '.method showPopup()V',
        'method_name': 'showPopup',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/widget/Spinner;->mPopup:Lmiuix/appcompat/widget/Spinner$SpinnerPopup;', 'invoke-virtual {p0}, Landroid/widget/Spinner;->getTextDirection()I', 'invoke-virtual {p0}, Landroid/widget/Spinner;->getTextAlignment()I', 'invoke-interface {v0, v1, p0}, Lmiuix/appcompat/widget/Spinner$SpinnerPopup;->show(II)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method showPopup()V
    .registers 3

    iget-object v0, p0, Lmiuix/appcompat/widget/Spinner;->mPopup:Lmiuix/appcompat/widget/Spinner$SpinnerPopup;

    invoke-virtual {p0}, Landroid/widget/Spinner;->getTextDirection()I

    move-result v1

    invoke-virtual {p0}, Landroid/widget/Spinner;->getTextAlignment()I

    move-result p0

    invoke-interface {v0, v1, p0}, Lmiuix/appcompat/widget/Spinner$SpinnerPopup;->show(II)V

    return-void
.end method""",
        'replacement': """.method showPopup()V
    .registers 3

    goto :goto_1

    nop

    :goto_0
    invoke-interface {v0, v1, p0}, Lmiuix/appcompat/widget/Spinner$SpinnerPopup;->show(II)V

    goto :goto_4

    nop

    :goto_1
    iget-object v0, p0, Lmiuix/appcompat/widget/Spinner;->mPopup:Lmiuix/appcompat/widget/Spinner$SpinnerPopup;

    goto :goto_2

    nop

    :goto_2
    invoke-virtual {p0}, Landroid/widget/Spinner;->getTextDirection()I

    move-result v1

    goto :goto_3

    nop

    :goto_3
    invoke-virtual {p0}, Landroid/widget/Spinner;->getTextAlignment()I

    move-result p0

    goto :goto_0

    nop

    :goto_4
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_widget_Spinner__showPopup',
        'method': '.method showPopup(FF)V',
        'method_name': 'showPopup',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/widget/Spinner;->mPopup:Lmiuix/appcompat/widget/Spinner$SpinnerPopup;', 'invoke-virtual {p0}, Landroid/widget/Spinner;->getTextDirection()I', 'invoke-virtual {p0}, Landroid/widget/Spinner;->getTextAlignment()I', 'invoke-interface {v0, v1, p0, p1, p2}, Lmiuix/appcompat/widget/Spinner$SpinnerPopup;->show(IIFF)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method showPopup(FF)V
    .registers 5

    iget-object v0, p0, Lmiuix/appcompat/widget/Spinner;->mPopup:Lmiuix/appcompat/widget/Spinner$SpinnerPopup;

    invoke-virtual {p0}, Landroid/widget/Spinner;->getTextDirection()I

    move-result v1

    invoke-virtual {p0}, Landroid/widget/Spinner;->getTextAlignment()I

    move-result p0

    invoke-interface {v0, v1, p0, p1, p2}, Lmiuix/appcompat/widget/Spinner$SpinnerPopup;->show(IIFF)V

    return-void
.end method""",
        'replacement': """.method showPopup(FF)V
    .registers 5

    goto :goto_3

    nop

    :goto_0
    invoke-virtual {p0}, Landroid/widget/Spinner;->getTextDirection()I

    move-result v1

    goto :goto_4

    nop

    :goto_1
    return-void

    :goto_2
    invoke-interface {v0, v1, p0, p1, p2}, Lmiuix/appcompat/widget/Spinner$SpinnerPopup;->show(IIFF)V

    goto :goto_1

    nop

    :goto_3
    iget-object v0, p0, Lmiuix/appcompat/widget/Spinner;->mPopup:Lmiuix/appcompat/widget/Spinner$SpinnerPopup;

    goto :goto_0

    nop

    :goto_4
    invoke-virtual {p0}, Landroid/widget/Spinner;->getTextAlignment()I

    move-result p0

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
