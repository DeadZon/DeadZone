TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/springback/view/SpringBackLayoutHelper.smali'
CLASS_FALLBACK_NAMES = ['SpringBackLayoutHelper.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'miuix_springback_view_SpringBackLayoutHelper__checkOrientation',
        'method': '.method checkOrientation(Landroid/view/MotionEvent;)V',
        'method_name': 'checkOrientation',
        'method_anchors': ['invoke-virtual {p1}, Landroid/view/MotionEvent;->getActionMasked()I', 'if-eqz v0, :cond_6', 'if-eq v0, v2, :cond_5', 'if-eq v0, v3, :cond_0', 'if-eq v0, p1, :cond_5', 'iget v0, p0, Lmiuix/springback/view/SpringBackLayoutHelper;->mActivePointerId:I', 'if-ne v0, v1, :cond_1', 'invoke-virtual {p1, v0}, Landroid/view/MotionEvent;->findPointerIndex(I)I'],
        'type': 'method_replace',
        'search': """.method checkOrientation(Landroid/view/MotionEvent;)V
    .registers 7

    invoke-virtual {p1}, Landroid/view/MotionEvent;->getActionMasked()I

    move-result v0

    const/4 v1, 0x0

    if-eqz v0, :cond_6

    const/4 v2, 0x1

    if-eq v0, v2, :cond_5

    const/4 v3, 0x2

    if-eq v0, v3, :cond_0

    const/4 p1, 0x3

    if-eq v0, p1, :cond_5

    goto :goto_1

    :cond_0
    iget v0, p0, Lmiuix/springback/view/SpringBackLayoutHelper;->mActivePointerId:I

    const/4 v1, -0x1

    if-ne v0, v1, :cond_1

    goto :goto_1

    :cond_1
    invoke-virtual {p1, v0}, Landroid/view/MotionEvent;->findPointerIndex(I)I

    move-result v0

    if-gez v0, :cond_2

    goto :goto_1

    :cond_2
    invoke-virtual {p1, v0}, Landroid/view/MotionEvent;->getY(I)F

    move-result v1

    invoke-virtual {p1, v0}, Landroid/view/MotionEvent;->getX(I)F

    move-result p1

    iget v0, p0, Lmiuix/springback/view/SpringBackLayoutHelper;->mInitialDownY:F

    sub-float/2addr v1, v0

    iget v0, p0, Lmiuix/springback/view/SpringBackLayoutHelper;->mInitialDownX:F

    sub-float/2addr p1, v0

    invoke-static {p1}, Ljava/lang/Math;->abs(F)F

    move-result v0

    iget v4, p0, Lmiuix/springback/view/SpringBackLayoutHelper;->mTouchSlop:I

    int-to-float v4, v4

    cmpl-float v0, v0, v4

    if-gtz v0, :cond_3

    invoke-static {v1}, Ljava/lang/Math;->abs(F)F

    move-result v0

    iget v4, p0, Lmiuix/springback/view/SpringBackLayoutHelper;->mTouchSlop:I

    int-to-float v4, v4

    cmpl-float v0, v0, v4

    if-lez v0, :cond_7

    :cond_3
    invoke-static {p1}, Ljava/lang/Math;->abs(F)F

    move-result p1

    invoke-static {v1}, Ljava/lang/Math;->abs(F)F

    move-result v0

    cmpl-float p1, p1, v0

    if-lez p1, :cond_4

    goto :goto_0

    :cond_4
    move v2, v3

    :goto_0
    iput v2, p0, Lmiuix/springback/view/SpringBackLayoutHelper;->mScrollOrientation:I

    return-void

    :cond_5
    iput v1, p0, Lmiuix/springback/view/SpringBackLayoutHelper;->mScrollOrientation:I

    iget-object p0, p0, Lmiuix/springback/view/SpringBackLayoutHelper;->mTarget:Landroid/view/ViewGroup;

    invoke-virtual {p0, v1}, Landroid/view/ViewGroup;->requestDisallowInterceptTouchEvent(Z)V

    return-void

    :cond_6
    invoke-virtual {p1, v1}, Landroid/view/MotionEvent;->getPointerId(I)I

    move-result v0

    iput v0, p0, Lmiuix/springback/view/SpringBackLayoutHelper;->mActivePointerId:I

    invoke-virtual {p1, v0}, Landroid/view/MotionEvent;->findPointerIndex(I)I

    move-result v0

    if-gez v0, :cond_8

    :cond_7
    :goto_1
    return-void

    :cond_8
    invoke-virtual {p1, v0}, Landroid/view/MotionEvent;->getY(I)F

    move-result v2

    iput v2, p0, Lmiuix/springback/view/SpringBackLayoutHelper;->mInitialDownY:F

    invoke-virtual {p1, v0}, Landroid/view/MotionEvent;->getX(I)F

    move-result p1

    iput p1, p0, Lmiuix/springback/view/SpringBackLayoutHelper;->mInitialDownX:F

    iput v1, p0, Lmiuix/springback/view/SpringBackLayoutHelper;->mScrollOrientation:I

    return-void
.end method""",
        'replacement': """.method checkOrientation(Landroid/view/MotionEvent;)V
    .registers 7

    goto :goto_2e

    nop

    :goto_0
    iget v0, p0, Lmiuix/springback/view/SpringBackLayoutHelper;->mInitialDownY:F

    goto :goto_1a

    nop

    :goto_1
    invoke-virtual {p1, v0}, Landroid/view/MotionEvent;->getX(I)F

    move-result p1

    goto :goto_d

    nop

    :goto_2
    invoke-virtual {p0, v1}, Landroid/view/ViewGroup;->requestDisallowInterceptTouchEvent(Z)V

    goto :goto_15

    nop

    :goto_3
    if-eq v0, v1, :cond_0

    goto :goto_2b

    :cond_0
    goto :goto_2a

    nop

    :goto_4
    iput v1, p0, Lmiuix/springback/view/SpringBackLayoutHelper;->mScrollOrientation:I

    goto :goto_a

    nop

    :goto_5
    iget v0, p0, Lmiuix/springback/view/SpringBackLayoutHelper;->mInitialDownX:F

    goto :goto_e

    nop

    :goto_6
    if-ltz v0, :cond_1

    goto :goto_24

    :cond_1
    goto :goto_23

    nop

    :goto_7
    const/4 v2, 0x1

    goto :goto_39

    nop

    :goto_8
    iget v4, p0, Lmiuix/springback/view/SpringBackLayoutHelper;->mTouchSlop:I

    goto :goto_20

    nop

    :goto_9
    iget v0, p0, Lmiuix/springback/view/SpringBackLayoutHelper;->mActivePointerId:I

    goto :goto_38

    nop

    :goto_a
    return-void

    :goto_b
    goto :goto_30

    :goto_c
    goto :goto_9

    nop

    :goto_d
    iput p1, p0, Lmiuix/springback/view/SpringBackLayoutHelper;->mInitialDownX:F

    goto :goto_4

    nop

    :goto_e
    sub-float/2addr p1, v0

    goto :goto_10

    nop

    :goto_f
    const/4 p1, 0x3

    goto :goto_2c

    nop

    :goto_10
    invoke-static {p1}, Ljava/lang/Math;->abs(F)F

    move-result v0

    goto :goto_8

    nop

    :goto_11
    const/4 v1, 0x0

    goto :goto_2d

    nop

    :goto_12
    invoke-virtual {p1, v0}, Landroid/view/MotionEvent;->findPointerIndex(I)I

    move-result v0

    goto :goto_6

    nop

    :goto_13
    iput v1, p0, Lmiuix/springback/view/SpringBackLayoutHelper;->mScrollOrientation:I

    goto :goto_1d

    nop

    :goto_14
    invoke-virtual {p1, v0}, Landroid/view/MotionEvent;->getY(I)F

    move-result v2

    goto :goto_40

    nop

    :goto_15
    return-void

    :goto_16
    goto :goto_22

    nop

    :goto_17
    cmpl-float v0, v0, v4

    goto :goto_25

    nop

    :goto_18
    return-void

    :goto_19
    goto :goto_14

    nop

    :goto_1a
    sub-float/2addr v1, v0

    goto :goto_5

    nop

    :goto_1b
    invoke-static {p1}, Ljava/lang/Math;->abs(F)F

    move-result p1

    goto :goto_41

    nop

    :goto_1c
    invoke-virtual {p1, v0}, Landroid/view/MotionEvent;->getX(I)F

    move-result p1

    goto :goto_0

    nop

    :goto_1d
    iget-object p0, p0, Lmiuix/springback/view/SpringBackLayoutHelper;->mTarget:Landroid/view/ViewGroup;

    goto :goto_2

    nop

    :goto_1e
    invoke-static {v1}, Ljava/lang/Math;->abs(F)F

    move-result v0

    goto :goto_1f

    nop

    :goto_1f
    iget v4, p0, Lmiuix/springback/view/SpringBackLayoutHelper;->mTouchSlop:I

    goto :goto_3f

    nop

    :goto_20
    int-to-float v4, v4

    goto :goto_3b

    nop

    :goto_21
    invoke-virtual {p1, v0}, Landroid/view/MotionEvent;->findPointerIndex(I)I

    move-result v0

    goto :goto_2f

    nop

    :goto_22
    invoke-virtual {p1, v1}, Landroid/view/MotionEvent;->getPointerId(I)I

    move-result v0

    goto :goto_32

    nop

    :goto_23
    goto :goto_30

    :goto_24
    goto :goto_31

    nop

    :goto_25
    if-gtz v0, :cond_2

    goto :goto_30

    :cond_2
    :goto_26
    goto :goto_1b

    nop

    :goto_27
    if-gtz p1, :cond_3

    goto :goto_36

    :cond_3
    goto :goto_35

    nop

    :goto_28
    return-void

    :goto_29
    goto :goto_13

    nop

    :goto_2a
    goto :goto_30

    :goto_2b
    goto :goto_12

    nop

    :goto_2c
    if-ne v0, p1, :cond_4

    goto :goto_29

    :cond_4
    goto :goto_b

    nop

    :goto_2d
    if-nez v0, :cond_5

    goto :goto_16

    :cond_5
    goto :goto_7

    nop

    :goto_2e
    invoke-virtual {p1}, Landroid/view/MotionEvent;->getActionMasked()I

    move-result v0

    goto :goto_11

    nop

    :goto_2f
    if-ltz v0, :cond_6

    goto :goto_19

    :cond_6
    :goto_30
    goto :goto_18

    nop

    :goto_31
    invoke-virtual {p1, v0}, Landroid/view/MotionEvent;->getY(I)F

    move-result v1

    goto :goto_1c

    nop

    :goto_32
    iput v0, p0, Lmiuix/springback/view/SpringBackLayoutHelper;->mActivePointerId:I

    goto :goto_21

    nop

    :goto_33
    if-lez v0, :cond_7

    goto :goto_26

    :cond_7
    goto :goto_1e

    nop

    :goto_34
    if-ne v0, v3, :cond_8

    goto :goto_c

    :cond_8
    goto :goto_f

    nop

    :goto_35
    goto :goto_3e

    :goto_36
    goto :goto_3d

    nop

    :goto_37
    cmpl-float p1, p1, v0

    goto :goto_27

    nop

    :goto_38
    const/4 v1, -0x1

    goto :goto_3

    nop

    :goto_39
    if-ne v0, v2, :cond_9

    goto :goto_29

    :cond_9
    goto :goto_3c

    nop

    :goto_3a
    iput v2, p0, Lmiuix/springback/view/SpringBackLayoutHelper;->mScrollOrientation:I

    goto :goto_28

    nop

    :goto_3b
    cmpl-float v0, v0, v4

    goto :goto_33

    nop

    :goto_3c
    const/4 v3, 0x2

    goto :goto_34

    nop

    :goto_3d
    move v2, v3

    :goto_3e
    goto :goto_3a

    nop

    :goto_3f
    int-to-float v4, v4

    goto :goto_17

    nop

    :goto_40
    iput v2, p0, Lmiuix/springback/view/SpringBackLayoutHelper;->mInitialDownY:F

    goto :goto_1

    nop

    :goto_41
    invoke-static {v1}, Ljava/lang/Math;->abs(F)F

    move-result v0

    goto :goto_37

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
