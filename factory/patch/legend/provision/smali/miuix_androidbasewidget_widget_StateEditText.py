TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/androidbasewidget/widget/StateEditText.smali'
CLASS_FALLBACK_NAMES = ['StateEditText.smali']
CLASS_ANCHORS = ['.super Lmiuix/androidbasewidget/widget/EditText;', '.field private static final WIDGET_MANAGER_CONSTRUCTOR_SIGNATURE:[Ljava/lang/Class;']

PATCHES = [
    {
        'id': 'miuix_androidbasewidget_widget_StateEditText__onDraw',
        'method': '.method protected onDraw(Landroid/graphics/Canvas;)V',
        'method_name': 'onDraw',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/widget/EditText;->onDraw(Landroid/graphics/Canvas;)V', 'invoke-direct {p0, p1}, Lmiuix/androidbasewidget/widget/StateEditText;->drawExtraWidget(Landroid/graphics/Canvas;)V', 'invoke-direct {p0, p1}, Lmiuix/androidbasewidget/widget/StateEditText;->drawLabel(Landroid/graphics/Canvas;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onDraw(Landroid/graphics/Canvas;)V
    .registers 2

    invoke-super {p0, p1}, Landroid/widget/EditText;->onDraw(Landroid/graphics/Canvas;)V

    invoke-direct {p0, p1}, Lmiuix/androidbasewidget/widget/StateEditText;->drawExtraWidget(Landroid/graphics/Canvas;)V

    invoke-direct {p0, p1}, Lmiuix/androidbasewidget/widget/StateEditText;->drawLabel(Landroid/graphics/Canvas;)V

    return-void
.end method""",
        'replacement': """.method protected onDraw(Landroid/graphics/Canvas;)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    invoke-direct {p0, p1}, Lmiuix/androidbasewidget/widget/StateEditText;->drawLabel(Landroid/graphics/Canvas;)V

    goto :goto_3

    nop

    :goto_1
    invoke-super {p0, p1}, Landroid/widget/EditText;->onDraw(Landroid/graphics/Canvas;)V

    goto :goto_2

    nop

    :goto_2
    invoke-direct {p0, p1}, Lmiuix/androidbasewidget/widget/StateEditText;->drawExtraWidget(Landroid/graphics/Canvas;)V

    goto :goto_0

    nop

    :goto_3
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_androidbasewidget_widget_StateEditText__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['invoke-super {p0, p1, p2}, Lmiuix/androidbasewidget/widget/EditText;->onMeasure(II)V', 'iget-object p1, p0, Lmiuix/androidbasewidget/widget/StateEditText;->mLabel:Ljava/lang/String;', 'invoke-static {p1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z', 'if-nez p1, :cond_1', 'iget-object p1, p0, Lmiuix/androidbasewidget/widget/StateEditText;->mLabelLayout:Landroid/text/StaticLayout;', 'if-eqz p1, :cond_1', 'iget p1, p0, Lmiuix/androidbasewidget/widget/StateEditText;->mLabelMaxWidth:I', 'if-nez p1, :cond_0'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 3

    invoke-super {p0, p1, p2}, Lmiuix/androidbasewidget/widget/EditText;->onMeasure(II)V

    iget-object p1, p0, Lmiuix/androidbasewidget/widget/StateEditText;->mLabel:Ljava/lang/String;

    invoke-static {p1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result p1

    if-nez p1, :cond_1

    iget-object p1, p0, Lmiuix/androidbasewidget/widget/StateEditText;->mLabelLayout:Landroid/text/StaticLayout;

    if-eqz p1, :cond_1

    iget p1, p0, Lmiuix/androidbasewidget/widget/StateEditText;->mLabelMaxWidth:I

    if-nez p1, :cond_0

    iget p1, p0, Lmiuix/androidbasewidget/widget/StateEditText;->mLabelLength:I

    invoke-virtual {p0}, Landroid/widget/EditText;->getMeasuredWidth()I

    move-result p2

    div-int/lit8 p2, p2, 0x2

    if-le p1, p2, :cond_0

    invoke-virtual {p0}, Landroid/widget/EditText;->getMeasuredWidth()I

    move-result p1

    div-int/lit8 p1, p1, 0x2

    iput p1, p0, Lmiuix/androidbasewidget/widget/StateEditText;->mLabelLength:I

    invoke-direct {p0}, Lmiuix/androidbasewidget/widget/StateEditText;->createLabelLayout()V

    :cond_0
    iget-object p1, p0, Lmiuix/androidbasewidget/widget/StateEditText;->mLabelLayout:Landroid/text/StaticLayout;

    invoke-virtual {p1}, Landroid/text/StaticLayout;->getHeight()I

    move-result p1

    invoke-virtual {p0}, Landroid/widget/EditText;->getPaddingTop()I

    move-result p2

    add-int/2addr p1, p2

    invoke-virtual {p0}, Landroid/widget/EditText;->getPaddingBottom()I

    move-result p2

    add-int/2addr p1, p2

    invoke-virtual {p0}, Landroid/widget/EditText;->getMeasuredHeight()I

    move-result p2

    if-le p1, p2, :cond_1

    invoke-virtual {p0}, Landroid/widget/EditText;->getMeasuredWidth()I

    move-result p2

    invoke-virtual {p0, p2, p1}, Landroid/widget/EditText;->setMeasuredDimension(II)V

    :cond_1
    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 3

    goto :goto_b

    nop

    :goto_0
    iget p1, p0, Lmiuix/androidbasewidget/widget/StateEditText;->mLabelLength:I

    goto :goto_f

    nop

    :goto_1
    add-int/2addr p1, p2

    goto :goto_7

    nop

    :goto_2
    return-void

    :goto_3
    iget-object p1, p0, Lmiuix/androidbasewidget/widget/StateEditText;->mLabelLayout:Landroid/text/StaticLayout;

    goto :goto_17

    nop

    :goto_4
    iput p1, p0, Lmiuix/androidbasewidget/widget/StateEditText;->mLabelLength:I

    goto :goto_19

    nop

    :goto_5
    if-eqz p1, :cond_0

    goto :goto_a

    :cond_0
    goto :goto_12

    nop

    :goto_6
    invoke-virtual {p0}, Landroid/widget/EditText;->getPaddingBottom()I

    move-result p2

    goto :goto_1

    nop

    :goto_7
    invoke-virtual {p0}, Landroid/widget/EditText;->getMeasuredHeight()I

    move-result p2

    goto :goto_18

    nop

    :goto_8
    add-int/2addr p1, p2

    goto :goto_6

    nop

    :goto_9
    invoke-virtual {p0, p2, p1}, Landroid/widget/EditText;->setMeasuredDimension(II)V

    :goto_a
    goto :goto_2

    nop

    :goto_b
    invoke-super {p0, p1, p2}, Lmiuix/androidbasewidget/widget/EditText;->onMeasure(II)V

    goto :goto_c

    nop

    :goto_c
    iget-object p1, p0, Lmiuix/androidbasewidget/widget/StateEditText;->mLabel:Ljava/lang/String;

    goto :goto_d

    nop

    :goto_d
    invoke-static {p1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result p1

    goto :goto_5

    nop

    :goto_e
    if-eqz p1, :cond_1

    goto :goto_1a

    :cond_1
    goto :goto_0

    nop

    :goto_f
    invoke-virtual {p0}, Landroid/widget/EditText;->getMeasuredWidth()I

    move-result p2

    goto :goto_13

    nop

    :goto_10
    invoke-virtual {p0}, Landroid/widget/EditText;->getMeasuredWidth()I

    move-result p1

    goto :goto_1c

    nop

    :goto_11
    invoke-virtual {p0}, Landroid/widget/EditText;->getMeasuredWidth()I

    move-result p2

    goto :goto_9

    nop

    :goto_12
    iget-object p1, p0, Lmiuix/androidbasewidget/widget/StateEditText;->mLabelLayout:Landroid/text/StaticLayout;

    goto :goto_14

    nop

    :goto_13
    div-int/lit8 p2, p2, 0x2

    goto :goto_15

    nop

    :goto_14
    if-nez p1, :cond_2

    goto :goto_a

    :cond_2
    goto :goto_1b

    nop

    :goto_15
    if-gt p1, p2, :cond_3

    goto :goto_1a

    :cond_3
    goto :goto_10

    nop

    :goto_16
    invoke-virtual {p0}, Landroid/widget/EditText;->getPaddingTop()I

    move-result p2

    goto :goto_8

    nop

    :goto_17
    invoke-virtual {p1}, Landroid/text/StaticLayout;->getHeight()I

    move-result p1

    goto :goto_16

    nop

    :goto_18
    if-gt p1, p2, :cond_4

    goto :goto_a

    :cond_4
    goto :goto_11

    nop

    :goto_19
    invoke-direct {p0}, Lmiuix/androidbasewidget/widget/StateEditText;->createLabelLayout()V

    :goto_1a
    goto :goto_3

    nop

    :goto_1b
    iget p1, p0, Lmiuix/androidbasewidget/widget/StateEditText;->mLabelMaxWidth:I

    goto :goto_e

    nop

    :goto_1c
    div-int/lit8 p1, p1, 0x2

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
