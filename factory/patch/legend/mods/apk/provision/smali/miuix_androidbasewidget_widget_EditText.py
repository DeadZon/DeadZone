TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/androidbasewidget/widget/EditText.smali'
CLASS_FALLBACK_NAMES = ['EditText.smali']
CLASS_ANCHORS = ['.super Landroidx/appcompat/widget/AppCompatEditText;']

PATCHES = [
    {
        'id': 'miuix_androidbasewidget_widget_EditText__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['invoke-super {p0, p1, p2}, Landroid/widget/EditText;->onMeasure(II)V', 'invoke-direct {p0}, Lmiuix/androidbasewidget/widget/EditText;->canVerticalScroll()Z', 'iput-boolean p1, p0, Lmiuix/androidbasewidget/widget/EditText;->mCanVerticalScroll:Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 3

    invoke-super {p0, p1, p2}, Landroid/widget/EditText;->onMeasure(II)V

    invoke-direct {p0}, Lmiuix/androidbasewidget/widget/EditText;->canVerticalScroll()Z

    move-result p1

    iput-boolean p1, p0, Lmiuix/androidbasewidget/widget/EditText;->mCanVerticalScroll:Z

    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 3

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0, p1, p2}, Landroid/widget/EditText;->onMeasure(II)V

    goto :goto_2

    nop

    :goto_1
    iput-boolean p1, p0, Lmiuix/androidbasewidget/widget/EditText;->mCanVerticalScroll:Z

    goto :goto_3

    nop

    :goto_2
    invoke-direct {p0}, Lmiuix/androidbasewidget/widget/EditText;->canVerticalScroll()Z

    move-result p1

    goto :goto_1

    nop

    :goto_3
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_androidbasewidget_widget_EditText__onScrollChanged',
        'method': '.method protected onScrollChanged(IIII)V',
        'method_name': 'onScrollChanged',
        'method_anchors': ['invoke-super {p0, p1, p2, p3, p4}, Landroid/widget/EditText;->onScrollChanged(IIII)V', 'invoke-direct {p0}, Lmiuix/androidbasewidget/widget/EditText;->canVerticalScroll()Z', 'iput-boolean p1, p0, Lmiuix/androidbasewidget/widget/EditText;->mCanVerticalScroll:Z', 'iget p1, p0, Lmiuix/androidbasewidget/widget/EditText;->mOffsetHeight:I', 'if-eq p2, p1, :cond_1', 'if-nez p2, :cond_0', 'return-void', 'invoke-virtual {p0}, Landroid/widget/EditText;->getParent()Landroid/view/ViewParent;'],
        'type': 'method_replace',
        'search': """.method protected onScrollChanged(IIII)V
    .registers 5

    invoke-super {p0, p1, p2, p3, p4}, Landroid/widget/EditText;->onScrollChanged(IIII)V

    invoke-direct {p0}, Lmiuix/androidbasewidget/widget/EditText;->canVerticalScroll()Z

    move-result p1

    iput-boolean p1, p0, Lmiuix/androidbasewidget/widget/EditText;->mCanVerticalScroll:Z

    iget p1, p0, Lmiuix/androidbasewidget/widget/EditText;->mOffsetHeight:I

    if-eq p2, p1, :cond_1

    if-nez p2, :cond_0

    goto :goto_0

    :cond_0
    return-void

    :cond_1
    :goto_0
    invoke-virtual {p0}, Landroid/widget/EditText;->getParent()Landroid/view/ViewParent;

    move-result-object p1

    if-eqz p1, :cond_2

    const/4 p2, 0x0

    invoke-interface {p1, p2}, Landroid/view/ViewParent;->requestDisallowInterceptTouchEvent(Z)V

    :cond_2
    const/4 p1, 0x1

    iput-boolean p1, p0, Lmiuix/androidbasewidget/widget/EditText;->mReachEdgeFlag:Z

    return-void
.end method""",
        'replacement': """.method protected onScrollChanged(IIII)V
    .registers 5

    goto :goto_5

    nop

    :goto_0
    if-nez p1, :cond_0

    goto :goto_10

    :cond_0
    goto :goto_1

    nop

    :goto_1
    const/4 p2, 0x0

    goto :goto_f

    nop

    :goto_2
    return-void

    :goto_3
    iput-boolean p1, p0, Lmiuix/androidbasewidget/widget/EditText;->mReachEdgeFlag:Z

    goto :goto_2

    nop

    :goto_4
    invoke-virtual {p0}, Landroid/widget/EditText;->getParent()Landroid/view/ViewParent;

    move-result-object p1

    goto :goto_0

    nop

    :goto_5
    invoke-super {p0, p1, p2, p3, p4}, Landroid/widget/EditText;->onScrollChanged(IIII)V

    goto :goto_c

    nop

    :goto_6
    return-void

    :goto_7
    goto :goto_4

    nop

    :goto_8
    goto :goto_7

    :goto_9
    goto :goto_6

    nop

    :goto_a
    iput-boolean p1, p0, Lmiuix/androidbasewidget/widget/EditText;->mCanVerticalScroll:Z

    goto :goto_b

    nop

    :goto_b
    iget p1, p0, Lmiuix/androidbasewidget/widget/EditText;->mOffsetHeight:I

    goto :goto_d

    nop

    :goto_c
    invoke-direct {p0}, Lmiuix/androidbasewidget/widget/EditText;->canVerticalScroll()Z

    move-result p1

    goto :goto_a

    nop

    :goto_d
    if-ne p2, p1, :cond_1

    goto :goto_7

    :cond_1
    goto :goto_11

    nop

    :goto_e
    const/4 p1, 0x1

    goto :goto_3

    nop

    :goto_f
    invoke-interface {p1, p2}, Landroid/view/ViewParent;->requestDisallowInterceptTouchEvent(Z)V

    :goto_10
    goto :goto_e

    nop

    :goto_11
    if-eqz p2, :cond_2

    goto :goto_9

    :cond_2
    goto :goto_8

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
