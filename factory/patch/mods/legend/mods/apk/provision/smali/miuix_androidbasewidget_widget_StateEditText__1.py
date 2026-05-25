TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/androidbasewidget/widget/StateEditText$1.smali'
CLASS_FALLBACK_NAMES = ['StateEditText$1.smali']
CLASS_ANCHORS = ['.super Landroidx/customview/widget/ExploreByTouchHelper;']

PATCHES = [
    {
        'id': 'miuix_androidbasewidget_widget_StateEditText__1__getVirtualViewAt',
        'method': '.method protected getVirtualViewAt(FF)I',
        'method_name': 'getVirtualViewAt',
        'method_anchors': ['iget-object v0, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;', 'invoke-static {v0}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;', 'if-nez v0, :cond_0', 'return v1', 'iget-object v2, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;', 'invoke-static {v2}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;', 'if-ge v0, v2, :cond_2', 'iget-object v2, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;'],
        'type': 'method_replace',
        'search': """.method protected getVirtualViewAt(FF)I
    .registers 11

    iget-object v0, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    invoke-static {v0}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;

    move-result-object v0

    const/high16 v1, -0x80000000

    if-nez v0, :cond_0

    return v1

    :cond_0
    const/4 v0, 0x0

    :goto_0
    iget-object v2, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    invoke-static {v2}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;

    move-result-object v2

    array-length v2, v2

    if-ge v0, v2, :cond_2

    iget-object v2, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    invoke-virtual {v2}, Landroid/widget/EditText;->getScrollX()I

    move-result v2

    iget-object v3, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    invoke-static {v3}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;

    move-result-object v3

    aget-object v3, v3, v0

    invoke-virtual {v3}, Landroid/graphics/drawable/Drawable;->getBounds()Landroid/graphics/Rect;

    move-result-object v3

    new-instance v4, Landroid/graphics/Rect;

    iget v5, v3, Landroid/graphics/Rect;->left:I

    sub-int/2addr v5, v2

    iget v6, v3, Landroid/graphics/Rect;->top:I

    iget v7, v3, Landroid/graphics/Rect;->right:I

    sub-int/2addr v7, v2

    iget v2, v3, Landroid/graphics/Rect;->bottom:I

    invoke-direct {v4, v5, v6, v7, v2}, Landroid/graphics/Rect;-><init>(IIII)V

    float-to-int v2, p1

    float-to-int v3, p2

    invoke-virtual {v4, v2, v3}, Landroid/graphics/Rect;->contains(II)Z

    move-result v2

    if-eqz v2, :cond_1

    iget-object v2, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    invoke-static {v2}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;

    move-result-object v2

    aget-object v2, v2, v0

    invoke-virtual {v2}, Landroid/graphics/drawable/Drawable;->isVisible()Z

    move-result v2

    if-eqz v2, :cond_1

    return v0

    :cond_1
    add-int/lit8 v0, v0, 0x1

    goto :goto_0

    :cond_2
    return v1
.end method""",
        'replacement': """.method protected getVirtualViewAt(FF)I
    .registers 11

    goto :goto_3

    nop

    :goto_0
    iget v5, v3, Landroid/graphics/Rect;->left:I

    goto :goto_25

    nop

    :goto_1
    const/4 v0, 0x0

    :goto_2
    goto :goto_8

    nop

    :goto_3
    iget-object v0, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    goto :goto_c

    nop

    :goto_4
    float-to-int v3, p2

    goto :goto_1d

    nop

    :goto_5
    iget v7, v3, Landroid/graphics/Rect;->right:I

    goto :goto_1b

    nop

    :goto_6
    if-lt v0, v2, :cond_0

    goto :goto_1f

    :cond_0
    goto :goto_13

    nop

    :goto_7
    array-length v2, v2

    goto :goto_6

    nop

    :goto_8
    iget-object v2, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    goto :goto_28

    nop

    :goto_9
    invoke-virtual {v2}, Landroid/widget/EditText;->getScrollX()I

    move-result v2

    goto :goto_11

    nop

    :goto_a
    return v0

    :goto_b
    goto :goto_16

    nop

    :goto_c
    invoke-static {v0}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;

    move-result-object v0

    goto :goto_19

    nop

    :goto_d
    if-eqz v0, :cond_1

    goto :goto_22

    :cond_1
    goto :goto_21

    nop

    :goto_e
    float-to-int v2, p1

    goto :goto_4

    nop

    :goto_f
    invoke-direct {v4, v5, v6, v7, v2}, Landroid/graphics/Rect;-><init>(IIII)V

    goto :goto_e

    nop

    :goto_10
    iget-object v2, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    goto :goto_17

    nop

    :goto_11
    iget-object v3, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    goto :goto_1a

    nop

    :goto_12
    iget v2, v3, Landroid/graphics/Rect;->bottom:I

    goto :goto_f

    nop

    :goto_13
    iget-object v2, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    goto :goto_9

    nop

    :goto_14
    invoke-virtual {v3}, Landroid/graphics/drawable/Drawable;->getBounds()Landroid/graphics/Rect;

    move-result-object v3

    goto :goto_18

    nop

    :goto_15
    if-nez v2, :cond_2

    goto :goto_b

    :cond_2
    goto :goto_10

    nop

    :goto_16
    add-int/lit8 v0, v0, 0x1

    goto :goto_1e

    nop

    :goto_17
    invoke-static {v2}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;

    move-result-object v2

    goto :goto_23

    nop

    :goto_18
    new-instance v4, Landroid/graphics/Rect;

    goto :goto_0

    nop

    :goto_19
    const/high16 v1, -0x80000000

    goto :goto_d

    nop

    :goto_1a
    invoke-static {v3}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;

    move-result-object v3

    goto :goto_1c

    nop

    :goto_1b
    sub-int/2addr v7, v2

    goto :goto_12

    nop

    :goto_1c
    aget-object v3, v3, v0

    goto :goto_14

    nop

    :goto_1d
    invoke-virtual {v4, v2, v3}, Landroid/graphics/Rect;->contains(II)Z

    move-result v2

    goto :goto_15

    nop

    :goto_1e
    goto :goto_2

    :goto_1f
    goto :goto_26

    nop

    :goto_20
    iget v6, v3, Landroid/graphics/Rect;->top:I

    goto :goto_5

    nop

    :goto_21
    return v1

    :goto_22
    goto :goto_1

    nop

    :goto_23
    aget-object v2, v2, v0

    goto :goto_27

    nop

    :goto_24
    if-nez v2, :cond_3

    goto :goto_b

    :cond_3
    goto :goto_a

    nop

    :goto_25
    sub-int/2addr v5, v2

    goto :goto_20

    nop

    :goto_26
    return v1

    :goto_27
    invoke-virtual {v2}, Landroid/graphics/drawable/Drawable;->isVisible()Z

    move-result v2

    goto :goto_24

    nop

    :goto_28
    invoke-static {v2}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;

    move-result-object v2

    goto :goto_7

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_androidbasewidget_widget_StateEditText__1__getVisibleVirtualViews',
        'method': '.method protected getVisibleVirtualViews(Ljava/util/List;)V',
        'method_name': 'getVisibleVirtualViews',
        'method_anchors': ['iget-object v0, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;', 'invoke-static {v0}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;', 'if-eqz v0, :cond_2', 'iget-object v0, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;', 'invoke-static {v0}, Lmiuix/androidbasewidget/widget/StateEditText;->access$100(Lmiuix/androidbasewidget/widget/StateEditText;)Z', 'if-eqz v0, :cond_0', 'iget-object v1, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;', 'invoke-static {v1}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;'],
        'type': 'method_replace',
        'search': """.method protected getVisibleVirtualViews(Ljava/util/List;)V
    .registers 4

    iget-object v0, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    invoke-static {v0}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;

    move-result-object v0

    if-eqz v0, :cond_2

    iget-object v0, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    invoke-static {v0}, Lmiuix/androidbasewidget/widget/StateEditText;->access$100(Lmiuix/androidbasewidget/widget/StateEditText;)Z

    move-result v0

    if-eqz v0, :cond_0

    goto :goto_1

    :cond_0
    const/4 v0, 0x0

    :goto_0
    iget-object v1, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    invoke-static {v1}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;

    move-result-object v1

    array-length v1, v1

    if-ge v0, v1, :cond_2

    iget-object v1, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    invoke-static {v1}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;

    move-result-object v1

    aget-object v1, v1, v0

    invoke-virtual {v1}, Landroid/graphics/drawable/Drawable;->isVisible()Z

    move-result v1

    if-eqz v1, :cond_1

    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    invoke-interface {p1, v1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    :cond_1
    add-int/lit8 v0, v0, 0x1

    goto :goto_0

    :cond_2
    :goto_1
    return-void
.end method""",
        'replacement': """.method protected getVisibleVirtualViews(Ljava/util/List;)V
    .registers 4

    goto :goto_8

    nop

    :goto_0
    if-lt v0, v1, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_19

    nop

    :goto_1
    array-length v1, v1

    goto :goto_0

    nop

    :goto_2
    goto :goto_d

    :goto_3
    goto :goto_e

    nop

    :goto_4
    invoke-static {v1}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;

    move-result-object v1

    goto :goto_1

    nop

    :goto_5
    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    goto :goto_14

    nop

    :goto_6
    invoke-static {v1}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;

    move-result-object v1

    goto :goto_16

    nop

    :goto_7
    if-nez v0, :cond_1

    goto :goto_18

    :cond_1
    goto :goto_17

    nop

    :goto_8
    iget-object v0, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    goto :goto_11

    nop

    :goto_9
    add-int/lit8 v0, v0, 0x1

    goto :goto_2

    nop

    :goto_a
    invoke-static {v0}, Lmiuix/androidbasewidget/widget/StateEditText;->access$100(Lmiuix/androidbasewidget/widget/StateEditText;)Z

    move-result v0

    goto :goto_7

    nop

    :goto_b
    if-nez v1, :cond_2

    goto :goto_15

    :cond_2
    goto :goto_5

    nop

    :goto_c
    const/4 v0, 0x0

    :goto_d
    goto :goto_12

    nop

    :goto_e
    return-void

    :goto_f
    if-nez v0, :cond_3

    goto :goto_3

    :cond_3
    goto :goto_13

    nop

    :goto_10
    invoke-virtual {v1}, Landroid/graphics/drawable/Drawable;->isVisible()Z

    move-result v1

    goto :goto_b

    nop

    :goto_11
    invoke-static {v0}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;

    move-result-object v0

    goto :goto_f

    nop

    :goto_12
    iget-object v1, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    goto :goto_4

    nop

    :goto_13
    iget-object v0, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    goto :goto_a

    nop

    :goto_14
    invoke-interface {p1, v1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    :goto_15
    goto :goto_9

    nop

    :goto_16
    aget-object v1, v1, v0

    goto :goto_10

    nop

    :goto_17
    goto :goto_3

    :goto_18
    goto :goto_c

    nop

    :goto_19
    iget-object v1, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_androidbasewidget_widget_StateEditText__1__onPerformActionForVirtualView',
        'method': '.method protected onPerformActionForVirtualView(IILandroid/os/Bundle;)Z',
        'method_name': 'onPerformActionForVirtualView',
        'method_anchors': ['iget-object p3, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;', 'invoke-static {p3}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;', 'if-eqz p3, :cond_3', 'if-eq p2, p3, :cond_0', 'iget-object p3, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;', 'invoke-static {p3}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;', 'if-ge p2, p3, :cond_3', 'if-ne p1, p2, :cond_2'],
        'type': 'method_replace',
        'search': """.method protected onPerformActionForVirtualView(IILandroid/os/Bundle;)Z
    .registers 16

    iget-object p3, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    invoke-static {p3}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;

    move-result-object p3

    const/4 v0, 0x0

    if-eqz p3, :cond_3

    const/16 p3, 0x10

    if-eq p2, p3, :cond_0

    goto :goto_2

    :cond_0
    move p2, v0

    :goto_0
    iget-object p3, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    invoke-static {p3}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;

    move-result-object p3

    array-length p3, p3

    if-ge p2, p3, :cond_3

    if-ne p1, p2, :cond_2

    invoke-virtual {p0, p1}, Landroidx/customview/widget/ExploreByTouchHelper;->invalidateVirtualView(I)V

    iget-object p1, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    invoke-static {p1}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;

    move-result-object p1

    aget-object p1, p1, p2

    invoke-virtual {p1}, Landroid/graphics/drawable/Drawable;->getBounds()Landroid/graphics/Rect;

    move-result-object p1

    invoke-virtual {p1}, Landroid/graphics/Rect;->centerX()I

    move-result p1

    iget-object p3, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    invoke-virtual {p3}, Landroid/widget/EditText;->getScrollX()I

    move-result p3

    sub-int/2addr p1, p3

    iget-object p3, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    invoke-static {p3}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;

    move-result-object p3

    aget-object p3, p3, p2

    invoke-virtual {p3}, Landroid/graphics/drawable/Drawable;->getBounds()Landroid/graphics/Rect;

    move-result-object p3

    invoke-virtual {p3}, Landroid/graphics/Rect;->centerY()I

    move-result p3

    invoke-static {}, Landroid/os/SystemClock;->uptimeMillis()J

    move-result-wide v0

    invoke-static {}, Landroid/os/SystemClock;->uptimeMillis()J

    move-result-wide v2

    int-to-float v5, p1

    int-to-float v6, p3

    const/4 v7, 0x0

    const/4 v4, 0x0

    invoke-static/range {v0 .. v7}, Landroid/view/MotionEvent;->obtain(JJIFFI)Landroid/view/MotionEvent;

    move-result-object p1

    iget-object p3, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    invoke-static {p3, p1}, Lmiuix/androidbasewidget/widget/StateEditText;->access$300(Lmiuix/androidbasewidget/widget/StateEditText;Landroid/view/MotionEvent;)Z

    invoke-virtual {p1}, Landroid/view/MotionEvent;->recycle()V

    move v9, v5

    invoke-static {}, Landroid/os/SystemClock;->uptimeMillis()J

    move-result-wide v4

    move v10, v6

    invoke-static {}, Landroid/os/SystemClock;->uptimeMillis()J

    move-result-wide v6

    const/4 v8, 0x1

    const/4 v11, 0x0

    invoke-static/range {v4 .. v11}, Landroid/view/MotionEvent;->obtain(JJIFFI)Landroid/view/MotionEvent;

    move-result-object p1

    iget-object p3, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    invoke-static {p3, p1}, Lmiuix/androidbasewidget/widget/StateEditText;->access$300(Lmiuix/androidbasewidget/widget/StateEditText;Landroid/view/MotionEvent;)Z

    invoke-virtual {p1}, Landroid/view/MotionEvent;->recycle()V

    iget-object p1, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    invoke-static {p1}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;

    move-result-object p1

    aget-object p1, p1, p2

    invoke-virtual {p1}, Landroid/graphics/drawable/Drawable;->isVisible()Z

    move-result p1

    if-nez p1, :cond_1

    const/high16 p1, 0x10000

    invoke-virtual {p0, p2, p1}, Landroidx/customview/widget/ExploreByTouchHelper;->sendEventForVirtualView(II)Z

    iget-object p0, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    const p1, 0x8000

    invoke-virtual {p0, p1}, Landroid/widget/EditText;->sendAccessibilityEvent(I)V

    goto :goto_1

    :cond_1
    const/16 p1, 0x80

    invoke-virtual {p0, p2, p1}, Landroidx/customview/widget/ExploreByTouchHelper;->sendEventForVirtualView(II)Z

    :goto_1
    const/4 p0, 0x1

    return p0

    :cond_2
    add-int/lit8 p2, p2, 0x1

    goto :goto_0

    :cond_3
    :goto_2
    return v0
.end method""",
        'replacement': """.method protected onPerformActionForVirtualView(IILandroid/os/Bundle;)Z
    .registers 16

    goto :goto_2

    nop

    :goto_0
    invoke-virtual {p1}, Landroid/graphics/drawable/Drawable;->getBounds()Landroid/graphics/Rect;

    move-result-object p1

    goto :goto_2d

    nop

    :goto_1
    iget-object p0, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    goto :goto_25

    nop

    :goto_2
    iget-object p3, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    goto :goto_9

    nop

    :goto_3
    move p2, v0

    :goto_4
    goto :goto_38

    nop

    :goto_5
    sub-int/2addr p1, p3

    goto :goto_3d

    nop

    :goto_6
    invoke-static {p3}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;

    move-result-object p3

    goto :goto_35

    nop

    :goto_7
    if-eq p1, p2, :cond_0

    goto :goto_3f

    :cond_0
    goto :goto_43

    nop

    :goto_8
    const/16 p1, 0x80

    goto :goto_36

    nop

    :goto_9
    invoke-static {p3}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;

    move-result-object p3

    goto :goto_2c

    nop

    :goto_a
    invoke-static {p1}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;

    move-result-object p1

    goto :goto_34

    nop

    :goto_b
    goto :goto_37

    :goto_c
    goto :goto_8

    nop

    :goto_d
    invoke-static/range {v4 .. v11}, Landroid/view/MotionEvent;->obtain(JJIFFI)Landroid/view/MotionEvent;

    move-result-object p1

    goto :goto_1b

    nop

    :goto_e
    const/high16 p1, 0x10000

    goto :goto_45

    nop

    :goto_f
    goto :goto_41

    :goto_10
    goto :goto_3

    nop

    :goto_11
    if-lt p2, p3, :cond_1

    goto :goto_41

    :cond_1
    goto :goto_7

    nop

    :goto_12
    invoke-virtual {p3}, Landroid/graphics/Rect;->centerY()I

    move-result p3

    goto :goto_15

    nop

    :goto_13
    iget-object p3, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    goto :goto_21

    nop

    :goto_14
    const/4 v11, 0x0

    goto :goto_d

    nop

    :goto_15
    invoke-static {}, Landroid/os/SystemClock;->uptimeMillis()J

    move-result-wide v0

    goto :goto_1c

    nop

    :goto_16
    iget-object p3, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    goto :goto_1f

    nop

    :goto_17
    const/4 v4, 0x0

    goto :goto_23

    nop

    :goto_18
    invoke-virtual {p1}, Landroid/graphics/drawable/Drawable;->isVisible()Z

    move-result p1

    goto :goto_22

    nop

    :goto_19
    add-int/lit8 p2, p2, 0x1

    goto :goto_40

    nop

    :goto_1a
    const/4 p0, 0x1

    goto :goto_3e

    nop

    :goto_1b
    iget-object p3, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    goto :goto_27

    nop

    :goto_1c
    invoke-static {}, Landroid/os/SystemClock;->uptimeMillis()J

    move-result-wide v2

    goto :goto_30

    nop

    :goto_1d
    const/4 v7, 0x0

    goto :goto_17

    nop

    :goto_1e
    move v9, v5

    goto :goto_3b

    nop

    :goto_1f
    invoke-static {p3, p1}, Lmiuix/androidbasewidget/widget/StateEditText;->access$300(Lmiuix/androidbasewidget/widget/StateEditText;Landroid/view/MotionEvent;)Z

    goto :goto_28

    nop

    :goto_20
    iget-object p1, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    goto :goto_44

    nop

    :goto_21
    invoke-virtual {p3}, Landroid/widget/EditText;->getScrollX()I

    move-result p3

    goto :goto_5

    nop

    :goto_22
    if-eqz p1, :cond_2

    goto :goto_c

    :cond_2
    goto :goto_e

    nop

    :goto_23
    invoke-static/range {v0 .. v7}, Landroid/view/MotionEvent;->obtain(JJIFFI)Landroid/view/MotionEvent;

    move-result-object p1

    goto :goto_16

    nop

    :goto_24
    int-to-float v6, p3

    goto :goto_1d

    nop

    :goto_25
    const p1, 0x8000

    goto :goto_3a

    nop

    :goto_26
    move v10, v6

    goto :goto_31

    nop

    :goto_27
    invoke-static {p3, p1}, Lmiuix/androidbasewidget/widget/StateEditText;->access$300(Lmiuix/androidbasewidget/widget/StateEditText;Landroid/view/MotionEvent;)Z

    goto :goto_46

    nop

    :goto_28
    invoke-virtual {p1}, Landroid/view/MotionEvent;->recycle()V

    goto :goto_1e

    nop

    :goto_29
    aget-object p1, p1, p2

    goto :goto_18

    nop

    :goto_2a
    invoke-virtual {p3}, Landroid/graphics/drawable/Drawable;->getBounds()Landroid/graphics/Rect;

    move-result-object p3

    goto :goto_12

    nop

    :goto_2b
    return v0

    :goto_2c
    const/4 v0, 0x0

    goto :goto_32

    nop

    :goto_2d
    invoke-virtual {p1}, Landroid/graphics/Rect;->centerX()I

    move-result p1

    goto :goto_13

    nop

    :goto_2e
    invoke-static {p3}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;

    move-result-object p3

    goto :goto_33

    nop

    :goto_2f
    const/4 v8, 0x1

    goto :goto_14

    nop

    :goto_30
    int-to-float v5, p1

    goto :goto_24

    nop

    :goto_31
    invoke-static {}, Landroid/os/SystemClock;->uptimeMillis()J

    move-result-wide v6

    goto :goto_2f

    nop

    :goto_32
    if-nez p3, :cond_3

    goto :goto_41

    :cond_3
    goto :goto_3c

    nop

    :goto_33
    array-length p3, p3

    goto :goto_11

    nop

    :goto_34
    aget-object p1, p1, p2

    goto :goto_0

    nop

    :goto_35
    aget-object p3, p3, p2

    goto :goto_2a

    nop

    :goto_36
    invoke-virtual {p0, p2, p1}, Landroidx/customview/widget/ExploreByTouchHelper;->sendEventForVirtualView(II)Z

    :goto_37
    goto :goto_1a

    nop

    :goto_38
    iget-object p3, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    goto :goto_2e

    nop

    :goto_39
    iget-object p1, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    goto :goto_a

    nop

    :goto_3a
    invoke-virtual {p0, p1}, Landroid/widget/EditText;->sendAccessibilityEvent(I)V

    goto :goto_b

    nop

    :goto_3b
    invoke-static {}, Landroid/os/SystemClock;->uptimeMillis()J

    move-result-wide v4

    goto :goto_26

    nop

    :goto_3c
    const/16 p3, 0x10

    goto :goto_42

    nop

    :goto_3d
    iget-object p3, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    goto :goto_6

    nop

    :goto_3e
    return p0

    :goto_3f
    goto :goto_19

    nop

    :goto_40
    goto :goto_4

    :goto_41
    goto :goto_2b

    nop

    :goto_42
    if-ne p2, p3, :cond_4

    goto :goto_10

    :cond_4
    goto :goto_f

    nop

    :goto_43
    invoke-virtual {p0, p1}, Landroidx/customview/widget/ExploreByTouchHelper;->invalidateVirtualView(I)V

    goto :goto_39

    nop

    :goto_44
    invoke-static {p1}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;

    move-result-object p1

    goto :goto_29

    nop

    :goto_45
    invoke-virtual {p0, p2, p1}, Landroidx/customview/widget/ExploreByTouchHelper;->sendEventForVirtualView(II)Z

    goto :goto_1

    nop

    :goto_46
    invoke-virtual {p1}, Landroid/view/MotionEvent;->recycle()V

    goto :goto_20

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_androidbasewidget_widget_StateEditText__1__onPopulateNodeForVirtualView',
        'method': '.method protected onPopulateNodeForVirtualView(ILandroidx/core/view/accessibility/AccessibilityNodeInfoCompat;)V',
        'method_name': 'onPopulateNodeForVirtualView',
        'method_anchors': ['iget-object v0, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;', 'invoke-static {v0}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;', 'if-nez v0, :cond_0', 'iget-object v1, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;', 'invoke-static {v1}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;', 'if-ge v0, v1, :cond_2', 'if-ne p1, v0, :cond_1', 'invoke-virtual {p2, v1}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setVisibleToUser(Z)V'],
        'type': 'method_replace',
        'search': """.method protected onPopulateNodeForVirtualView(ILandroidx/core/view/accessibility/AccessibilityNodeInfoCompat;)V
    .registers 6

    iget-object v0, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    invoke-static {v0}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;

    move-result-object v0

    if-nez v0, :cond_0

    goto :goto_1

    :cond_0
    const/4 v0, 0x0

    :goto_0
    iget-object v1, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    invoke-static {v1}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;

    move-result-object v1

    array-length v1, v1

    if-ge v0, v1, :cond_2

    if-ne p1, v0, :cond_1

    const/4 v1, 0x1

    invoke-virtual {p2, v1}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setVisibleToUser(Z)V

    invoke-virtual {p2, v1}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setAccessibilityFocused(Z)V

    invoke-virtual {p2, v1}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setFocusable(Z)V

    invoke-virtual {p2, v1}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setClickable(Z)V

    iget-object v1, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    invoke-static {v1}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;

    move-result-object v1

    aget-object v1, v1, v0

    invoke-virtual {v1}, Landroid/graphics/drawable/Drawable;->getBounds()Landroid/graphics/Rect;

    move-result-object v1

    const-string v2, ""

    invoke-virtual {p2, v2}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setText(Ljava/lang/CharSequence;)V

    invoke-virtual {p2, v1}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setBoundsInParent(Landroid/graphics/Rect;)V

    const-class v1, Landroid/widget/Button;

    invoke-virtual {v1}, Ljava/lang/Class;->getName()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {p2, v1}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setClassName(Ljava/lang/CharSequence;)V

    const/16 v1, 0x10

    invoke-virtual {p2, v1}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->addAction(I)V

    iget-object v1, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    invoke-static {v1}, Lmiuix/androidbasewidget/widget/StateEditText;->access$200(Lmiuix/androidbasewidget/widget/StateEditText;)Lmiuix/androidbasewidget/widget/StateEditText$WidgetManager;

    move-result-object v1

    invoke-virtual {v1, v0, p2}, Lmiuix/androidbasewidget/widget/StateEditText$WidgetManager;->onPopulateNodeForVirtualView(ILandroidx/core/view/accessibility/AccessibilityNodeInfoCompat;)V

    :cond_1
    add-int/lit8 v0, v0, 0x1

    goto :goto_0

    :cond_2
    :goto_1
    return-void
.end method""",
        'replacement': """.method protected onPopulateNodeForVirtualView(ILandroidx/core/view/accessibility/AccessibilityNodeInfoCompat;)V
    .registers 6

    goto :goto_16

    nop

    :goto_0
    invoke-static {v1}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;

    move-result-object v1

    goto :goto_11

    nop

    :goto_1
    add-int/lit8 v0, v0, 0x1

    goto :goto_19

    nop

    :goto_2
    invoke-virtual {v1, v0, p2}, Lmiuix/androidbasewidget/widget/StateEditText$WidgetManager;->onPopulateNodeForVirtualView(ILandroidx/core/view/accessibility/AccessibilityNodeInfoCompat;)V

    :goto_3
    goto :goto_1

    nop

    :goto_4
    invoke-virtual {p2, v1}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setFocusable(Z)V

    goto :goto_1b

    nop

    :goto_5
    array-length v1, v1

    goto :goto_b

    nop

    :goto_6
    invoke-static {v1}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;

    move-result-object v1

    goto :goto_5

    nop

    :goto_7
    invoke-virtual {p2, v1}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setClassName(Ljava/lang/CharSequence;)V

    goto :goto_1e

    nop

    :goto_8
    invoke-virtual {p2, v1}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setVisibleToUser(Z)V

    goto :goto_1d

    nop

    :goto_9
    invoke-virtual {v1}, Landroid/graphics/drawable/Drawable;->getBounds()Landroid/graphics/Rect;

    move-result-object v1

    goto :goto_15

    nop

    :goto_a
    invoke-virtual {p2, v1}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->addAction(I)V

    goto :goto_22

    nop

    :goto_b
    if-lt v0, v1, :cond_0

    goto :goto_1a

    :cond_0
    goto :goto_e

    nop

    :goto_c
    const-class v1, Landroid/widget/Button;

    goto :goto_d

    nop

    :goto_d
    invoke-virtual {v1}, Ljava/lang/Class;->getName()Ljava/lang/String;

    move-result-object v1

    goto :goto_7

    nop

    :goto_e
    if-eq p1, v0, :cond_1

    goto :goto_3

    :cond_1
    goto :goto_18

    nop

    :goto_f
    invoke-virtual {p2, v1}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setBoundsInParent(Landroid/graphics/Rect;)V

    goto :goto_c

    nop

    :goto_10
    invoke-virtual {p2, v2}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setText(Ljava/lang/CharSequence;)V

    goto :goto_f

    nop

    :goto_11
    aget-object v1, v1, v0

    goto :goto_9

    nop

    :goto_12
    if-eqz v0, :cond_2

    goto :goto_20

    :cond_2
    goto :goto_1f

    nop

    :goto_13
    const/4 v0, 0x0

    :goto_14
    goto :goto_21

    nop

    :goto_15
    const-string v2, ""

    goto :goto_10

    nop

    :goto_16
    iget-object v0, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    goto :goto_17

    nop

    :goto_17
    invoke-static {v0}, Lmiuix/androidbasewidget/widget/StateEditText;->access$000(Lmiuix/androidbasewidget/widget/StateEditText;)[Landroid/graphics/drawable/Drawable;

    move-result-object v0

    goto :goto_12

    nop

    :goto_18
    const/4 v1, 0x1

    goto :goto_8

    nop

    :goto_19
    goto :goto_14

    :goto_1a
    goto :goto_24

    nop

    :goto_1b
    invoke-virtual {p2, v1}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setClickable(Z)V

    goto :goto_1c

    nop

    :goto_1c
    iget-object v1, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    goto :goto_0

    nop

    :goto_1d
    invoke-virtual {p2, v1}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setAccessibilityFocused(Z)V

    goto :goto_4

    nop

    :goto_1e
    const/16 v1, 0x10

    goto :goto_a

    nop

    :goto_1f
    goto :goto_1a

    :goto_20
    goto :goto_13

    nop

    :goto_21
    iget-object v1, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    goto :goto_6

    nop

    :goto_22
    iget-object v1, p0, Lmiuix/androidbasewidget/widget/StateEditText$1;->this$0:Lmiuix/androidbasewidget/widget/StateEditText;

    goto :goto_23

    nop

    :goto_23
    invoke-static {v1}, Lmiuix/androidbasewidget/widget/StateEditText;->access$200(Lmiuix/androidbasewidget/widget/StateEditText;)Lmiuix/androidbasewidget/widget/StateEditText$WidgetManager;

    move-result-object v1

    goto :goto_2

    nop

    :goto_24
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
