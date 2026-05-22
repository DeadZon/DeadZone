TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/springback/view/SpringBackLayout.smali'
CLASS_FALLBACK_NAMES = ['SpringBackLayout.smali']
CLASS_ANCHORS = ['.super Landroid/view/ViewGroup;', '.implements Landroidx/core/view/NestedScrollingParent3;', '.implements Landroidx/core/view/NestedScrollingChild3;', '.implements Lmiuix/core/view/NestedCurrentFling;']

PATCHES = [
    {
        'id': 'miuix_springback_view_SpringBackLayout__getSpringBackRange',
        'method': '.method protected getSpringBackRange(I)I',
        'method_name': 'getSpringBackRange',
        'method_anchors': ['if-ne p1, v0, :cond_0', 'iget p0, p0, Lmiuix/springback/view/SpringBackLayout;->mScreenHeight:I', 'return p0', 'iget p0, p0, Lmiuix/springback/view/SpringBackLayout;->mScreenWidth:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected getSpringBackRange(I)I
    .registers 3

    const/4 v0, 0x2

    if-ne p1, v0, :cond_0

    iget p0, p0, Lmiuix/springback/view/SpringBackLayout;->mScreenHeight:I

    return p0

    :cond_0
    iget p0, p0, Lmiuix/springback/view/SpringBackLayout;->mScreenWidth:I

    return p0
.end method""",
        'replacement': """.method protected getSpringBackRange(I)I
    .registers 3

    goto :goto_5

    nop

    :goto_0
    if-eq p1, v0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_6

    nop

    :goto_1
    iget p0, p0, Lmiuix/springback/view/SpringBackLayout;->mScreenWidth:I

    goto :goto_2

    nop

    :goto_2
    return p0

    :goto_3
    return p0

    :goto_4
    goto :goto_1

    nop

    :goto_5
    const/4 v0, 0x2

    goto :goto_0

    nop

    :goto_6
    iget p0, p0, Lmiuix/springback/view/SpringBackLayout;->mScreenHeight:I

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_springback_view_SpringBackLayout__obtainDampingDistance',
        'method': '.method protected obtainDampingDistance(FI)F',
        'method_name': 'obtainDampingDistance',
        'method_anchors': ['invoke-static {p1, p0}, Ljava/lang/Math;->min(FF)F', 'invoke-static {p0, p1, v0, v1}, Ljava/lang/Math;->pow(DD)D', 'invoke-static {p0, p1, v0, v1}, Ljava/lang/Math;->pow(DD)D', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected obtainDampingDistance(FI)F
    .registers 7

    const/high16 p0, 0x3f800000

    invoke-static {p1, p0}, Ljava/lang/Math;->min(FF)F

    move-result p0

    float-to-double p0, p0

    const-wide/high16 v0, 0x4008000000000000L

    invoke-static {p0, p1, v0, v1}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v2

    div-double/2addr v2, v0

    const-wide/high16 v0, 0x4000000000000000L

    invoke-static {p0, p1, v0, v1}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v0

    sub-double/2addr v2, v0

    add-double/2addr v2, p0

    double-to-float p0, v2

    int-to-float p1, p2

    mul-float/2addr p0, p1

    return p0
.end method""",
        'replacement': """.method protected obtainDampingDistance(FI)F
    .registers 7

    goto :goto_b

    nop

    :goto_0
    div-double/2addr v2, v0

    goto :goto_6

    nop

    :goto_1
    float-to-double p0, p0

    goto :goto_8

    nop

    :goto_2
    double-to-float p0, v2

    goto :goto_5

    nop

    :goto_3
    invoke-static {p0, p1, v0, v1}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v2

    goto :goto_0

    nop

    :goto_4
    invoke-static {p0, p1, v0, v1}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v0

    goto :goto_d

    nop

    :goto_5
    int-to-float p1, p2

    goto :goto_9

    nop

    :goto_6
    const-wide/high16 v0, 0x4000000000000000L

    goto :goto_4

    nop

    :goto_7
    add-double/2addr v2, p0

    goto :goto_2

    nop

    :goto_8
    const-wide/high16 v0, 0x4008000000000000L

    goto :goto_3

    nop

    :goto_9
    mul-float/2addr p0, p1

    goto :goto_c

    nop

    :goto_a
    invoke-static {p1, p0}, Ljava/lang/Math;->min(FF)F

    move-result p0

    goto :goto_1

    nop

    :goto_b
    const/high16 p0, 0x3f800000

    goto :goto_a

    nop

    :goto_c
    return p0

    :goto_d
    sub-double/2addr v2, v0

    goto :goto_7

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_springback_view_SpringBackLayout__obtainMaxSpringBackDistance',
        'method': '.method protected obtainMaxSpringBackDistance(I)F',
        'method_name': 'obtainMaxSpringBackDistance',
        'method_anchors': ['invoke-virtual {p0, p1}, Lmiuix/springback/view/SpringBackLayout;->getSpringBackRange(I)I', 'invoke-virtual {p0, v0, p1}, Lmiuix/springback/view/SpringBackLayout;->obtainDampingDistance(FI)F', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected obtainMaxSpringBackDistance(I)F
    .registers 3

    const/high16 v0, 0x3f800000

    invoke-virtual {p0, p1}, Lmiuix/springback/view/SpringBackLayout;->getSpringBackRange(I)I

    move-result p1

    invoke-virtual {p0, v0, p1}, Lmiuix/springback/view/SpringBackLayout;->obtainDampingDistance(FI)F

    move-result p0

    return p0
.end method""",
        'replacement': """.method protected obtainMaxSpringBackDistance(I)F
    .registers 3

    goto :goto_3

    nop

    :goto_0
    return p0

    :goto_1
    invoke-virtual {p0, v0, p1}, Lmiuix/springback/view/SpringBackLayout;->obtainDampingDistance(FI)F

    move-result p0

    goto :goto_0

    nop

    :goto_2
    invoke-virtual {p0, p1}, Lmiuix/springback/view/SpringBackLayout;->getSpringBackRange(I)I

    move-result p1

    goto :goto_1

    nop

    :goto_3
    const/high16 v0, 0x3f800000

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_springback_view_SpringBackLayout__obtainSpringBackDistance',
        'method': '.method protected obtainSpringBackDistance(FI)F',
        'method_name': 'obtainSpringBackDistance',
        'method_anchors': ['invoke-virtual {p0, p2}, Lmiuix/springback/view/SpringBackLayout;->getSpringBackRange(I)I', 'invoke-static {p1}, Ljava/lang/Math;->abs(F)F', 'invoke-static {p1, v0}, Ljava/lang/Math;->min(FF)F', 'invoke-virtual {p0, p1, p2}, Lmiuix/springback/view/SpringBackLayout;->obtainDampingDistance(FI)F', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected obtainSpringBackDistance(FI)F
    .registers 4

    invoke-virtual {p0, p2}, Lmiuix/springback/view/SpringBackLayout;->getSpringBackRange(I)I

    move-result p2

    invoke-static {p1}, Ljava/lang/Math;->abs(F)F

    move-result p1

    int-to-float v0, p2

    div-float/2addr p1, v0

    const/high16 v0, 0x3f800000

    invoke-static {p1, v0}, Ljava/lang/Math;->min(FF)F

    move-result p1

    invoke-virtual {p0, p1, p2}, Lmiuix/springback/view/SpringBackLayout;->obtainDampingDistance(FI)F

    move-result p0

    return p0
.end method""",
        'replacement': """.method protected obtainSpringBackDistance(FI)F
    .registers 4

    goto :goto_5

    nop

    :goto_0
    return p0

    :goto_1
    invoke-static {p1}, Ljava/lang/Math;->abs(F)F

    move-result p1

    goto :goto_6

    nop

    :goto_2
    const/high16 v0, 0x3f800000

    goto :goto_7

    nop

    :goto_3
    div-float/2addr p1, v0

    goto :goto_2

    nop

    :goto_4
    invoke-virtual {p0, p1, p2}, Lmiuix/springback/view/SpringBackLayout;->obtainDampingDistance(FI)F

    move-result p0

    goto :goto_0

    nop

    :goto_5
    invoke-virtual {p0, p2}, Lmiuix/springback/view/SpringBackLayout;->getSpringBackRange(I)I

    move-result p2

    goto :goto_1

    nop

    :goto_6
    int-to-float v0, p2

    goto :goto_3

    nop

    :goto_7
    invoke-static {p1, v0}, Ljava/lang/Math;->min(FF)F

    move-result p1

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_springback_view_SpringBackLayout__obtainTouchDistance',
        'method': '.method protected obtainTouchDistance(FFI)F',
        'method_name': 'obtainTouchDistance',
        'method_anchors': ['invoke-virtual {p0, p3}, Lmiuix/springback/view/SpringBackLayout;->getSpringBackRange(I)I', 'invoke-static {p1}, Ljava/lang/Math;->abs(F)F', 'invoke-static {p2}, Ljava/lang/Math;->abs(F)F', 'if-gez p3, :cond_0', 'invoke-static {p2, p3, v0, v1}, Ljava/lang/Math;->pow(DD)D', 'invoke-static {p0, p1, v2, v3}, Ljava/lang/Math;->pow(DD)D', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected obtainTouchDistance(FFI)F
    .registers 8

    invoke-virtual {p0, p3}, Lmiuix/springback/view/SpringBackLayout;->getSpringBackRange(I)I

    move-result p0

    invoke-static {p1}, Ljava/lang/Math;->abs(F)F

    move-result p3

    invoke-static {p2}, Ljava/lang/Math;->abs(F)F

    move-result v0

    cmpg-float p3, p3, v0

    if-gez p3, :cond_0

    goto :goto_0

    :cond_0
    move p1, p2

    :goto_0
    int-to-double p2, p0

    const-wide v0, 0x3fe5555555555555L

    invoke-static {p2, p3, v0, v1}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v0

    int-to-float p0, p0

    const/high16 v2, 0x40400000

    mul-float/2addr p1, v2

    sub-float/2addr p0, p1

    float-to-double p0, p0

    const-wide v2, 0x3fd5555555555555L

    invoke-static {p0, p1, v2, v3}, Ljava/lang/Math;->pow(DD)D

    move-result-wide p0

    mul-double/2addr v0, p0

    sub-double/2addr p2, v0

    double-to-float p0, p2

    return p0
.end method""",
        'replacement': """.method protected obtainTouchDistance(FFI)F
    .registers 8

    goto :goto_2

    nop

    :goto_0
    invoke-static {p0, p1, v2, v3}, Ljava/lang/Math;->pow(DD)D

    move-result-wide p0

    goto :goto_5

    nop

    :goto_1
    mul-float/2addr p1, v2

    goto :goto_4

    nop

    :goto_2
    invoke-virtual {p0, p3}, Lmiuix/springback/view/SpringBackLayout;->getSpringBackRange(I)I

    move-result p0

    goto :goto_10

    nop

    :goto_3
    float-to-double p0, p0

    goto :goto_12

    nop

    :goto_4
    sub-float/2addr p0, p1

    goto :goto_3

    nop

    :goto_5
    mul-double/2addr v0, p0

    goto :goto_11

    nop

    :goto_6
    double-to-float p0, p2

    goto :goto_16

    nop

    :goto_7
    const/high16 v2, 0x40400000

    goto :goto_1

    nop

    :goto_8
    invoke-static {p2}, Ljava/lang/Math;->abs(F)F

    move-result v0

    goto :goto_e

    nop

    :goto_9
    const-wide v0, 0x3fe5555555555555L

    goto :goto_15

    nop

    :goto_a
    move p1, p2

    :goto_b
    goto :goto_c

    nop

    :goto_c
    int-to-double p2, p0

    goto :goto_9

    nop

    :goto_d
    int-to-float p0, p0

    goto :goto_7

    nop

    :goto_e
    cmpg-float p3, p3, v0

    goto :goto_f

    nop

    :goto_f
    if-ltz p3, :cond_0

    goto :goto_14

    :cond_0
    goto :goto_13

    nop

    :goto_10
    invoke-static {p1}, Ljava/lang/Math;->abs(F)F

    move-result p3

    goto :goto_8

    nop

    :goto_11
    sub-double/2addr p2, v0

    goto :goto_6

    nop

    :goto_12
    const-wide v2, 0x3fd5555555555555L

    goto :goto_0

    nop

    :goto_13
    goto :goto_b

    :goto_14
    goto :goto_a

    nop

    :goto_15
    invoke-static {p2, p3, v0, v1}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v0

    goto :goto_d

    nop

    :goto_16
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_springback_view_SpringBackLayout__onConfigurationChanged',
        'method': '.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V',
        'method_name': 'onConfigurationChanged',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/view/ViewGroup;->onConfigurationChanged(Landroid/content/res/Configuration;)V', 'invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;', 'invoke-static {p1}, Lmiuix/core/util/EnvStateManager;->getScreenSize(Landroid/content/Context;)Landroid/graphics/Point;', 'iget v0, p1, Landroid/graphics/Point;->x:I', 'iput v0, p0, Lmiuix/springback/view/SpringBackLayout;->mScreenWidth:I', 'iget p1, p1, Landroid/graphics/Point;->y:I', 'iput p1, p0, Lmiuix/springback/view/SpringBackLayout;->mScreenHeight:I', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 3

    invoke-super {p0, p1}, Landroid/view/ViewGroup;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;

    move-result-object p1

    invoke-static {p1}, Lmiuix/core/util/EnvStateManager;->getScreenSize(Landroid/content/Context;)Landroid/graphics/Point;

    move-result-object p1

    iget v0, p1, Landroid/graphics/Point;->x:I

    iput v0, p0, Lmiuix/springback/view/SpringBackLayout;->mScreenWidth:I

    iget p1, p1, Landroid/graphics/Point;->y:I

    iput p1, p0, Lmiuix/springback/view/SpringBackLayout;->mScreenHeight:I

    return-void
.end method""",
        'replacement': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 3

    goto :goto_3

    nop

    :goto_0
    iput v0, p0, Lmiuix/springback/view/SpringBackLayout;->mScreenWidth:I

    goto :goto_4

    nop

    :goto_1
    invoke-static {p1}, Lmiuix/core/util/EnvStateManager;->getScreenSize(Landroid/content/Context;)Landroid/graphics/Point;

    move-result-object p1

    goto :goto_7

    nop

    :goto_2
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;

    move-result-object p1

    goto :goto_1

    nop

    :goto_3
    invoke-super {p0, p1}, Landroid/view/ViewGroup;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    goto :goto_2

    nop

    :goto_4
    iget p1, p1, Landroid/graphics/Point;->y:I

    goto :goto_6

    nop

    :goto_5
    return-void

    :goto_6
    iput p1, p0, Lmiuix/springback/view/SpringBackLayout;->mScreenHeight:I

    goto :goto_5

    nop

    :goto_7
    iget v0, p1, Landroid/graphics/Point;->x:I

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_springback_view_SpringBackLayout__onFinishInflate',
        'method': '.method protected onFinishInflate()V',
        'method_name': 'onFinishInflate',
        'method_anchors': ['invoke-super {p0}, Landroid/view/ViewGroup;->onFinishInflate()V', 'invoke-virtual {p0}, Landroid/view/ViewGroup;->getPaddingTop()I', 'iput v0, p0, Lmiuix/springback/view/SpringBackLayout;->mInitPaddingTop:I', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onFinishInflate()V
    .registers 2

    invoke-super {p0}, Landroid/view/ViewGroup;->onFinishInflate()V

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getPaddingTop()I

    move-result v0

    iput v0, p0, Lmiuix/springback/view/SpringBackLayout;->mInitPaddingTop:I

    return-void
.end method""",
        'replacement': """.method protected onFinishInflate()V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    iput v0, p0, Lmiuix/springback/view/SpringBackLayout;->mInitPaddingTop:I

    goto :goto_2

    nop

    :goto_1
    invoke-super {p0}, Landroid/view/ViewGroup;->onFinishInflate()V

    goto :goto_3

    nop

    :goto_2
    return-void

    :goto_3
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getPaddingTop()I

    move-result v0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_springback_view_SpringBackLayout__onLayout',
        'method': '.method protected onLayout(ZIIII)V',
        'method_name': 'onLayout',
        'method_anchors': ['iget-object p1, p0, Lmiuix/springback/view/SpringBackLayout;->mTarget:Landroid/view/View;', 'invoke-virtual {p1}, Landroid/view/View;->getVisibility()I', 'if-eq p1, p2, :cond_0', 'iget-object p1, p0, Lmiuix/springback/view/SpringBackLayout;->mTarget:Landroid/view/View;', 'invoke-virtual {p1}, Landroid/view/View;->getMeasuredWidth()I', 'iget-object p2, p0, Lmiuix/springback/view/SpringBackLayout;->mTarget:Landroid/view/View;', 'invoke-virtual {p2}, Landroid/view/View;->getMeasuredHeight()I', 'invoke-virtual {p0}, Landroid/view/ViewGroup;->getPaddingLeft()I'],
        'type': 'method_replace',
        'search': """.method protected onLayout(ZIIII)V
    .registers 6

    iget-object p1, p0, Lmiuix/springback/view/SpringBackLayout;->mTarget:Landroid/view/View;

    invoke-virtual {p1}, Landroid/view/View;->getVisibility()I

    move-result p1

    const/16 p2, 0x8

    if-eq p1, p2, :cond_0

    iget-object p1, p0, Lmiuix/springback/view/SpringBackLayout;->mTarget:Landroid/view/View;

    invoke-virtual {p1}, Landroid/view/View;->getMeasuredWidth()I

    move-result p1

    iget-object p2, p0, Lmiuix/springback/view/SpringBackLayout;->mTarget:Landroid/view/View;

    invoke-virtual {p2}, Landroid/view/View;->getMeasuredHeight()I

    move-result p2

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getPaddingLeft()I

    move-result p3

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getPaddingTop()I

    move-result p4

    iget-object p0, p0, Lmiuix/springback/view/SpringBackLayout;->mTarget:Landroid/view/View;

    add-int/2addr p1, p3

    add-int/2addr p2, p4

    invoke-virtual {p0, p3, p4, p1, p2}, Landroid/view/View;->layout(IIII)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onLayout(ZIIII)V
    .registers 6

    goto :goto_d

    nop

    :goto_0
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getPaddingLeft()I

    move-result p3

    goto :goto_c

    nop

    :goto_1
    iget-object p1, p0, Lmiuix/springback/view/SpringBackLayout;->mTarget:Landroid/view/View;

    goto :goto_4

    nop

    :goto_2
    return-void

    :goto_3
    add-int/2addr p1, p3

    goto :goto_f

    nop

    :goto_4
    invoke-virtual {p1}, Landroid/view/View;->getMeasuredWidth()I

    move-result p1

    goto :goto_8

    nop

    :goto_5
    const/16 p2, 0x8

    goto :goto_7

    nop

    :goto_6
    iget-object p0, p0, Lmiuix/springback/view/SpringBackLayout;->mTarget:Landroid/view/View;

    goto :goto_3

    nop

    :goto_7
    if-ne p1, p2, :cond_0

    goto :goto_a

    :cond_0
    goto :goto_1

    nop

    :goto_8
    iget-object p2, p0, Lmiuix/springback/view/SpringBackLayout;->mTarget:Landroid/view/View;

    goto :goto_b

    nop

    :goto_9
    invoke-virtual {p0, p3, p4, p1, p2}, Landroid/view/View;->layout(IIII)V

    :goto_a
    goto :goto_2

    nop

    :goto_b
    invoke-virtual {p2}, Landroid/view/View;->getMeasuredHeight()I

    move-result p2

    goto :goto_0

    nop

    :goto_c
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getPaddingTop()I

    move-result p4

    goto :goto_6

    nop

    :goto_d
    iget-object p1, p0, Lmiuix/springback/view/SpringBackLayout;->mTarget:Landroid/view/View;

    goto :goto_e

    nop

    :goto_e
    invoke-virtual {p1}, Landroid/view/View;->getVisibility()I

    move-result p1

    goto :goto_5

    nop

    :goto_f
    add-int/2addr p2, p4

    goto :goto_9

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_springback_view_SpringBackLayout__onScrollChanged',
        'method': '.method protected onScrollChanged(IIII)V',
        'method_name': 'onScrollChanged',
        'method_anchors': ['invoke-super {p0, p1, p2, p3, p4}, Landroid/view/ViewGroup;->onScrollChanged(IIII)V', 'iget-object p0, p0, Lmiuix/springback/view/SpringBackLayout;->mOnScrollChangeListeners:Ljava/util/List;', 'invoke-interface {p0}, Ljava/util/List;->iterator()Ljava/util/Iterator;', 'invoke-interface {p0}, Ljava/util/Iterator;->hasNext()Z', 'if-nez p1, :cond_0', 'return-void', 'invoke-interface {p0}, Ljava/util/Iterator;->next()Ljava/lang/Object;', 'invoke-static {p0}, Landroidx/appcompat/app/ToolbarActionBar$$ExternalSyntheticThrowCCEIfNotNull0;->m(Ljava/lang/Object;)V'],
        'type': 'method_replace',
        'search': """.method protected onScrollChanged(IIII)V
    .registers 5

    invoke-super {p0, p1, p2, p3, p4}, Landroid/view/ViewGroup;->onScrollChanged(IIII)V

    iget-object p0, p0, Lmiuix/springback/view/SpringBackLayout;->mOnScrollChangeListeners:Ljava/util/List;

    invoke-interface {p0}, Ljava/util/List;->iterator()Ljava/util/Iterator;

    move-result-object p0

    invoke-interface {p0}, Ljava/util/Iterator;->hasNext()Z

    move-result p1

    if-nez p1, :cond_0

    return-void

    :cond_0
    invoke-interface {p0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object p0

    invoke-static {p0}, Landroidx/appcompat/app/ToolbarActionBar$$ExternalSyntheticThrowCCEIfNotNull0;->m(Ljava/lang/Object;)V

    const/4 p0, 0x0

    throw p0
.end method""",
        'replacement': """.method protected onScrollChanged(IIII)V
    .registers 5

    goto :goto_5

    nop

    :goto_0
    return-void

    :goto_1
    goto :goto_7

    nop

    :goto_2
    iget-object p0, p0, Lmiuix/springback/view/SpringBackLayout;->mOnScrollChangeListeners:Ljava/util/List;

    goto :goto_4

    nop

    :goto_3
    invoke-interface {p0}, Ljava/util/Iterator;->hasNext()Z

    move-result p1

    goto :goto_a

    nop

    :goto_4
    invoke-interface {p0}, Ljava/util/List;->iterator()Ljava/util/Iterator;

    move-result-object p0

    goto :goto_3

    nop

    :goto_5
    invoke-super {p0, p1, p2, p3, p4}, Landroid/view/ViewGroup;->onScrollChanged(IIII)V

    goto :goto_2

    nop

    :goto_6
    const/4 p0, 0x0

    goto :goto_9

    nop

    :goto_7
    invoke-interface {p0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object p0

    goto :goto_8

    nop

    :goto_8
    invoke-static {p0}, Landroidx/appcompat/app/ToolbarActionBar$$ExternalSyntheticThrowCCEIfNotNull0;->m(Ljava/lang/Object;)V

    goto :goto_6

    nop

    :goto_9
    throw p0

    :goto_a
    if-eqz p1, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_springback_view_SpringBackLayout__init',
        'method': '.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V',
        'method_name': '<init>',
        'method_anchors': ['invoke-direct {p0, p1, p2}, Landroid/view/ViewGroup;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V', 'iput v0, p0, Lmiuix/springback/view/SpringBackLayout;->mActivePointerId:I', 'iput v1, p0, Lmiuix/springback/view/SpringBackLayout;->consumeNestFlingCounter:I', 'iput-object v3, p0, Lmiuix/springback/view/SpringBackLayout;->mParentScrollConsumed:[I', 'iput-object v3, p0, Lmiuix/springback/view/SpringBackLayout;->mParentOffsetInWindow:[I', 'iput-object v3, p0, Lmiuix/springback/view/SpringBackLayout;->mNestedScrollingV2ConsumedCompat:[I', 'new-instance v3, Ljava/util/ArrayList;', 'invoke-direct {v3}, Ljava/util/ArrayList;-><init>()V'],
        'type': 'method_replace',
        'search': """.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 7

    invoke-direct {p0, p1, p2}, Landroid/view/ViewGroup;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    const/4 v0, -0x1

    iput v0, p0, Lmiuix/springback/view/SpringBackLayout;->mActivePointerId:I

    const/4 v1, 0x0

    iput v1, p0, Lmiuix/springback/view/SpringBackLayout;->consumeNestFlingCounter:I

    const/4 v2, 0x2

    new-array v3, v2, [I

    iput-object v3, p0, Lmiuix/springback/view/SpringBackLayout;->mParentScrollConsumed:[I

    new-array v3, v2, [I

    iput-object v3, p0, Lmiuix/springback/view/SpringBackLayout;->mParentOffsetInWindow:[I

    new-array v3, v2, [I

    iput-object v3, p0, Lmiuix/springback/view/SpringBackLayout;->mNestedScrollingV2ConsumedCompat:[I

    new-instance v3, Ljava/util/ArrayList;

    invoke-direct {v3}, Ljava/util/ArrayList;-><init>()V

    iput-object v3, p0, Lmiuix/springback/view/SpringBackLayout;->mOnScrollChangeListeners:Ljava/util/List;

    iput v1, p0, Lmiuix/springback/view/SpringBackLayout;->mScrollState:I

    new-instance v3, Landroidx/core/view/NestedScrollingParentHelper;

    invoke-direct {v3, p0}, Landroidx/core/view/NestedScrollingParentHelper;-><init>(Landroid/view/ViewGroup;)V

    iput-object v3, p0, Lmiuix/springback/view/SpringBackLayout;->mNestedScrollingParentHelper:Landroidx/core/view/NestedScrollingParentHelper;

    invoke-static {p0}, Lmiuix/core/view/NestedScrollingChildHelper;->obtain(Landroid/view/View;)Landroidx/core/view/NestedScrollingChildHelper;

    move-result-object v3

    iput-object v3, p0, Lmiuix/springback/view/SpringBackLayout;->mNestedScrollingChildHelper:Landroidx/core/view/NestedScrollingChildHelper;

    invoke-static {p1}, Landroid/view/ViewConfiguration;->get(Landroid/content/Context;)Landroid/view/ViewConfiguration;

    move-result-object v3

    invoke-virtual {v3}, Landroid/view/ViewConfiguration;->getScaledTouchSlop()I

    move-result v3

    iput v3, p0, Lmiuix/springback/view/SpringBackLayout;->mTouchSlop:I

    sget-object v3, Lmiuix/springback/R$styleable;->SpringBackLayout:[I

    invoke-virtual {p1, p2, v3}, Landroid/content/Context;->obtainStyledAttributes(Landroid/util/AttributeSet;[I)Landroid/content/res/TypedArray;

    move-result-object p2

    sget v3, Lmiuix/springback/R$styleable;->SpringBackLayout_scrollableView:I

    invoke-virtual {p2, v3, v0}, Landroid/content/res/TypedArray;->getResourceId(II)I

    move-result v0

    iput v0, p0, Lmiuix/springback/view/SpringBackLayout;->mTargetId:I

    sget v0, Lmiuix/springback/R$styleable;->SpringBackLayout_scrollOrientation:I

    invoke-virtual {p2, v0, v2}, Landroid/content/res/TypedArray;->getInt(II)I

    move-result v0

    iput v0, p0, Lmiuix/springback/view/SpringBackLayout;->mOriginScrollOrientation:I

    sget v0, Lmiuix/springback/R$styleable;->SpringBackLayout_springBackMode:I

    const/4 v2, 0x3

    invoke-virtual {p2, v0, v2}, Landroid/content/res/TypedArray;->getInt(II)I

    move-result v0

    iput v0, p0, Lmiuix/springback/view/SpringBackLayout;->mSpringBackMode:I

    invoke-virtual {p2}, Landroid/content/res/TypedArray;->recycle()V

    new-instance p2, Lmiuix/springback/view/SpringScroller;

    invoke-direct {p2}, Lmiuix/springback/view/SpringScroller;-><init>()V

    iput-object p2, p0, Lmiuix/springback/view/SpringBackLayout;->mSpringScroller:Lmiuix/springback/view/SpringScroller;

    new-instance p2, Lmiuix/springback/view/SpringBackLayoutHelper;

    iget v0, p0, Lmiuix/springback/view/SpringBackLayout;->mOriginScrollOrientation:I

    invoke-direct {p2, p0, v0}, Lmiuix/springback/view/SpringBackLayoutHelper;-><init>(Landroid/view/ViewGroup;I)V

    iput-object p2, p0, Lmiuix/springback/view/SpringBackLayout;->mHelper:Lmiuix/springback/view/SpringBackLayoutHelper;

    const/4 p2, 0x1

    invoke-virtual {p0, p2}, Lmiuix/springback/view/SpringBackLayout;->setNestedScrollingEnabled(Z)V

    invoke-static {p1}, Lmiuix/core/util/EnvStateManager;->getScreenSize(Landroid/content/Context;)Landroid/graphics/Point;

    move-result-object p1

    iget v0, p1, Landroid/graphics/Point;->x:I

    iput v0, p0, Lmiuix/springback/view/SpringBackLayout;->mScreenWidth:I

    iget p1, p1, Landroid/graphics/Point;->y:I

    iput p1, p0, Lmiuix/springback/view/SpringBackLayout;->mScreenHeight:I

    sget-boolean p1, Lmiuix/os/Build;->IS_INTERNATIONAL_BUILD:Z

    iput-boolean p1, p0, Lmiuix/springback/view/SpringBackLayout;->mInGlobalRomMode:Z

    if-eqz p1, :cond_0

    iput-boolean v1, p0, Lmiuix/springback/view/SpringBackLayout;->mSpringBackEnable:Z

    return-void

    :cond_0
    iput-boolean p2, p0, Lmiuix/springback/view/SpringBackLayout;->mSpringBackEnable:Z

    return-void
.end method""",
        'replacement': """.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 7

    invoke-direct {p0, p1, p2}, Landroid/view/ViewGroup;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    const/4 v0, -0x1

    iput v0, p0, Lmiuix/springback/view/SpringBackLayout;->mActivePointerId:I

    const/4 v1, 0x0

    iput v1, p0, Lmiuix/springback/view/SpringBackLayout;->consumeNestFlingCounter:I

    const/4 v2, 0x2

    new-array v3, v2, [I

    iput-object v3, p0, Lmiuix/springback/view/SpringBackLayout;->mParentScrollConsumed:[I

    new-array v3, v2, [I

    iput-object v3, p0, Lmiuix/springback/view/SpringBackLayout;->mParentOffsetInWindow:[I

    new-array v3, v2, [I

    iput-object v3, p0, Lmiuix/springback/view/SpringBackLayout;->mNestedScrollingV2ConsumedCompat:[I

    new-instance v3, Ljava/util/ArrayList;

    invoke-direct {v3}, Ljava/util/ArrayList;-><init>()V

    iput-object v3, p0, Lmiuix/springback/view/SpringBackLayout;->mOnScrollChangeListeners:Ljava/util/List;

    iput v1, p0, Lmiuix/springback/view/SpringBackLayout;->mScrollState:I

    new-instance v3, Landroidx/core/view/NestedScrollingParentHelper;

    invoke-direct {v3, p0}, Landroidx/core/view/NestedScrollingParentHelper;-><init>(Landroid/view/ViewGroup;)V

    iput-object v3, p0, Lmiuix/springback/view/SpringBackLayout;->mNestedScrollingParentHelper:Landroidx/core/view/NestedScrollingParentHelper;

    invoke-static {p0}, Lmiuix/core/view/NestedScrollingChildHelper;->obtain(Landroid/view/View;)Landroidx/core/view/NestedScrollingChildHelper;

    move-result-object v3

    iput-object v3, p0, Lmiuix/springback/view/SpringBackLayout;->mNestedScrollingChildHelper:Landroidx/core/view/NestedScrollingChildHelper;

    invoke-static {p1}, Landroid/view/ViewConfiguration;->get(Landroid/content/Context;)Landroid/view/ViewConfiguration;

    move-result-object v3

    invoke-virtual {v3}, Landroid/view/ViewConfiguration;->getScaledTouchSlop()I

    move-result v3

    iput v3, p0, Lmiuix/springback/view/SpringBackLayout;->mTouchSlop:I

    sget-object v3, Lmiuix/springback/R$styleable;->SpringBackLayout:[I

    invoke-virtual {p1, p2, v3}, Landroid/content/Context;->obtainStyledAttributes(Landroid/util/AttributeSet;[I)Landroid/content/res/TypedArray;

    move-result-object p2

    sget v3, Lmiuix/springback/R$styleable;->SpringBackLayout_scrollableView:I

    invoke-virtual {p2, v3, v0}, Landroid/content/res/TypedArray;->getResourceId(II)I

    move-result v0

    iput v0, p0, Lmiuix/springback/view/SpringBackLayout;->mTargetId:I

    sget v0, Lmiuix/springback/R$styleable;->SpringBackLayout_scrollOrientation:I

    invoke-virtual {p2, v0, v2}, Landroid/content/res/TypedArray;->getInt(II)I

    move-result v0

    iput v0, p0, Lmiuix/springback/view/SpringBackLayout;->mOriginScrollOrientation:I

    sget v0, Lmiuix/springback/R$styleable;->SpringBackLayout_springBackMode:I

    const/4 v2, 0x3

    invoke-virtual {p2, v0, v2}, Landroid/content/res/TypedArray;->getInt(II)I

    move-result v0

    iput v0, p0, Lmiuix/springback/view/SpringBackLayout;->mSpringBackMode:I

    invoke-virtual {p2}, Landroid/content/res/TypedArray;->recycle()V

    new-instance p2, Lmiuix/springback/view/SpringScroller;

    invoke-direct {p2}, Lmiuix/springback/view/SpringScroller;-><init>()V

    iput-object p2, p0, Lmiuix/springback/view/SpringBackLayout;->mSpringScroller:Lmiuix/springback/view/SpringScroller;

    new-instance p2, Lmiuix/springback/view/SpringBackLayoutHelper;

    iget v0, p0, Lmiuix/springback/view/SpringBackLayout;->mOriginScrollOrientation:I

    invoke-direct {p2, p0, v0}, Lmiuix/springback/view/SpringBackLayoutHelper;-><init>(Landroid/view/ViewGroup;I)V

    iput-object p2, p0, Lmiuix/springback/view/SpringBackLayout;->mHelper:Lmiuix/springback/view/SpringBackLayoutHelper;

    const/4 p2, 0x1

    invoke-virtual {p0, p2}, Lmiuix/springback/view/SpringBackLayout;->setNestedScrollingEnabled(Z)V

    invoke-static {p1}, Lmiuix/core/util/EnvStateManager;->getScreenSize(Landroid/content/Context;)Landroid/graphics/Point;

    move-result-object p1

    iget v0, p1, Landroid/graphics/Point;->x:I

    iput v0, p0, Lmiuix/springback/view/SpringBackLayout;->mScreenWidth:I

    iget p1, p1, Landroid/graphics/Point;->y:I

    iput p1, p0, Lmiuix/springback/view/SpringBackLayout;->mScreenHeight:I

    sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    iput-boolean p1, p0, Lmiuix/springback/view/SpringBackLayout;->mInGlobalRomMode:Z

    if-eqz p1, :cond_0

    iput-boolean v1, p0, Lmiuix/springback/view/SpringBackLayout;->mSpringBackEnable:Z

    return-void

    :cond_0
    iput-boolean p2, p0, Lmiuix/springback/view/SpringBackLayout;->mSpringBackEnable:Z

    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
