TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/spring/view/SpringHelper$AxisHandler.smali'
CLASS_FALLBACK_NAMES = ['SpringHelper$AxisHandler.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'miuix_spring_view_SpringHelper__AxisHandler__handleNestedPreScroll',
        'method': '.method handleNestedPreScroll([I[IZ)Z',
        'method_name': 'handleNestedPreScroll',
        'method_anchors': ['iget v0, p0, Lmiuix/spring/view/SpringHelper$AxisHandler;->mAxis:I', 'if-eqz v0, :cond_2', 'invoke-virtual {p0}, Lmiuix/spring/view/SpringHelper$AxisHandler;->canScroll()Z', 'if-eqz v2, :cond_2', 'iget v2, p0, Lmiuix/spring/view/SpringHelper$AxisHandler;->mDistance:F', 'if-nez v3, :cond_0', 'invoke-static {v2}, Ljava/lang/Integer;->signum(I)I', 'if-lez v2, :cond_1'],
        'type': 'method_replace',
        'search': """.method handleNestedPreScroll([I[IZ)Z
    .registers 8

    iget v0, p0, Lmiuix/spring/view/SpringHelper$AxisHandler;->mAxis:I

    aget v0, p1, v0

    const/4 v1, 0x0

    if-eqz v0, :cond_2

    invoke-virtual {p0}, Lmiuix/spring/view/SpringHelper$AxisHandler;->canScroll()Z

    move-result v2

    if-eqz v2, :cond_2

    iget v2, p0, Lmiuix/spring/view/SpringHelper$AxisHandler;->mDistance:F

    const/4 v3, 0x0

    cmpl-float v3, v2, v3

    if-nez v3, :cond_0

    goto :goto_0

    :cond_0
    float-to-int v2, v2

    invoke-static {v2}, Ljava/lang/Integer;->signum(I)I

    move-result v2

    mul-int/2addr v2, v0

    if-lez v2, :cond_1

    return v1

    :cond_1
    iget v1, p0, Lmiuix/spring/view/SpringHelper$AxisHandler;->mAxis:I

    invoke-direct {p0, v0, p2, p3}, Lmiuix/spring/view/SpringHelper$AxisHandler;->release(I[IZ)I

    move-result p0

    aput p0, p1, v1

    const/4 p0, 0x1

    return p0

    :cond_2
    :goto_0
    return v1
.end method""",
        'replacement': """.method handleNestedPreScroll([I[IZ)Z
    .registers 8

    goto :goto_a

    nop

    :goto_0
    aget v0, p1, v0

    goto :goto_6

    nop

    :goto_1
    float-to-int v2, v2

    goto :goto_f

    nop

    :goto_2
    mul-int/2addr v2, v0

    goto :goto_7

    nop

    :goto_3
    const/4 p0, 0x1

    goto :goto_14

    nop

    :goto_4
    cmpl-float v3, v2, v3

    goto :goto_5

    nop

    :goto_5
    if-eqz v3, :cond_0

    goto :goto_c

    :cond_0
    goto :goto_b

    nop

    :goto_6
    const/4 v1, 0x0

    goto :goto_e

    nop

    :goto_7
    if-gtz v2, :cond_1

    goto :goto_18

    :cond_1
    goto :goto_17

    nop

    :goto_8
    return v1

    :goto_9
    aput p0, p1, v1

    goto :goto_3

    nop

    :goto_a
    iget v0, p0, Lmiuix/spring/view/SpringHelper$AxisHandler;->mAxis:I

    goto :goto_0

    nop

    :goto_b
    goto :goto_15

    :goto_c
    goto :goto_1

    nop

    :goto_d
    if-nez v2, :cond_2

    goto :goto_15

    :cond_2
    goto :goto_16

    nop

    :goto_e
    if-nez v0, :cond_3

    goto :goto_15

    :cond_3
    goto :goto_10

    nop

    :goto_f
    invoke-static {v2}, Ljava/lang/Integer;->signum(I)I

    move-result v2

    goto :goto_2

    nop

    :goto_10
    invoke-virtual {p0}, Lmiuix/spring/view/SpringHelper$AxisHandler;->canScroll()Z

    move-result v2

    goto :goto_d

    nop

    :goto_11
    const/4 v3, 0x0

    goto :goto_4

    nop

    :goto_12
    invoke-direct {p0, v0, p2, p3}, Lmiuix/spring/view/SpringHelper$AxisHandler;->release(I[IZ)I

    move-result p0

    goto :goto_9

    nop

    :goto_13
    iget v1, p0, Lmiuix/spring/view/SpringHelper$AxisHandler;->mAxis:I

    goto :goto_12

    nop

    :goto_14
    return p0

    :goto_15
    goto :goto_8

    nop

    :goto_16
    iget v2, p0, Lmiuix/spring/view/SpringHelper$AxisHandler;->mDistance:F

    goto :goto_11

    nop

    :goto_17
    return v1

    :goto_18
    goto :goto_13

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_spring_view_SpringHelper__AxisHandler__handleNestedScroll',
        'method': '.method handleNestedScroll(I[II[I)Z',
        'method_name': 'handleNestedScroll',
        'method_anchors': ['iget-object p2, p0, Lmiuix/spring/view/SpringHelper$AxisHandler;->this$0:Lmiuix/spring/view/SpringHelper;', 'invoke-virtual {p2}, Lmiuix/spring/view/SpringHelper;->springAvailable()Z', 'if-eqz p2, :cond_1', 'if-nez p3, :cond_0', 'invoke-direct {p0, p1, p4, v0}, Lmiuix/spring/view/SpringHelper$AxisHandler;->pull(I[IZ)Z', 'return p0', 'return v0'],
        'type': 'method_replace',
        'search': """.method handleNestedScroll(I[II[I)Z
    .registers 6

    iget-object p2, p0, Lmiuix/spring/view/SpringHelper$AxisHandler;->this$0:Lmiuix/spring/view/SpringHelper;

    invoke-virtual {p2}, Lmiuix/spring/view/SpringHelper;->springAvailable()Z

    move-result p2

    const/4 v0, 0x0

    if-eqz p2, :cond_1

    if-nez p3, :cond_0

    const/4 v0, 0x1

    :cond_0
    invoke-direct {p0, p1, p4, v0}, Lmiuix/spring/view/SpringHelper$AxisHandler;->pull(I[IZ)Z

    move-result p0

    return p0

    :cond_1
    return v0
.end method""",
        'replacement': """.method handleNestedScroll(I[II[I)Z
    .registers 6

    goto :goto_3

    nop

    :goto_0
    if-eqz p3, :cond_0

    goto :goto_a

    :cond_0
    goto :goto_9

    nop

    :goto_1
    invoke-virtual {p2}, Lmiuix/spring/view/SpringHelper;->springAvailable()Z

    move-result p2

    goto :goto_8

    nop

    :goto_2
    invoke-direct {p0, p1, p4, v0}, Lmiuix/spring/view/SpringHelper$AxisHandler;->pull(I[IZ)Z

    move-result p0

    goto :goto_4

    nop

    :goto_3
    iget-object p2, p0, Lmiuix/spring/view/SpringHelper$AxisHandler;->this$0:Lmiuix/spring/view/SpringHelper;

    goto :goto_1

    nop

    :goto_4
    return p0

    :goto_5
    goto :goto_7

    nop

    :goto_6
    if-nez p2, :cond_1

    goto :goto_5

    :cond_1
    goto :goto_0

    nop

    :goto_7
    return v0

    :goto_8
    const/4 v0, 0x0

    goto :goto_6

    nop

    :goto_9
    const/4 v0, 0x1

    :goto_a
    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
