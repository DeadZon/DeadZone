TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/flexible/template/AbstractMarkTemplate.smali'
CLASS_FALLBACK_NAMES = ['AbstractMarkTemplate.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Lmiuix/flexible/template/IHyperCellTemplate;', '.implements Lmiuix/flexible/mark/MarkHelper$IParamsGetter;', '.field protected static final NOT_SET:I = 0x7fffffff']

PATCHES = [
    {
        'id': 'miuix_flexible_template_AbstractMarkTemplate__dp2px',
        'method': '.method protected dp2px(F)I',
        'method_name': 'dp2px',
        'method_anchors': ['iget p0, p0, Lmiuix/flexible/template/AbstractMarkTemplate;->mDensity:F', 'invoke-static {p0, p1}, Lmiuix/core/util/MiuixUIUtils;->dp2px(FF)I', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected dp2px(F)I
    .registers 2

    iget p0, p0, Lmiuix/flexible/template/AbstractMarkTemplate;->mDensity:F

    invoke-static {p0, p1}, Lmiuix/core/util/MiuixUIUtils;->dp2px(FF)I

    move-result p0

    return p0
.end method""",
        'replacement': """.method protected dp2px(F)I
    .registers 2

    goto :goto_0

    nop

    :goto_0
    iget p0, p0, Lmiuix/flexible/template/AbstractMarkTemplate;->mDensity:F

    goto :goto_2

    nop

    :goto_1
    return p0

    :goto_2
    invoke-static {p0, p1}, Lmiuix/core/util/MiuixUIUtils;->dp2px(FF)I

    move-result p0

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_flexible_template_AbstractMarkTemplate__findViewByAreaId',
        'method': '.method protected findViewByAreaId(Landroid/view/ViewGroup;I)Landroid/view/View;',
        'method_name': 'findViewByAreaId',
        'method_anchors': ['if-eqz p0, :cond_0', 'check-cast p1, Lmiuix/flexible/view/HyperCellLayout;', 'invoke-virtual {p1, p2}, Lmiuix/flexible/view/HyperCellLayout;->findViewByAreaId(I)Landroid/view/View;', 'return-object p0', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected findViewByAreaId(Landroid/view/ViewGroup;I)Landroid/view/View;
    .registers 3

    instance-of p0, p1, Lmiuix/flexible/view/HyperCellLayout;

    if-eqz p0, :cond_0

    check-cast p1, Lmiuix/flexible/view/HyperCellLayout;

    invoke-virtual {p1, p2}, Lmiuix/flexible/view/HyperCellLayout;->findViewByAreaId(I)Landroid/view/View;

    move-result-object p0

    return-object p0

    :cond_0
    const/4 p0, 0x0

    return-object p0
.end method""",
        'replacement': """.method protected findViewByAreaId(Landroid/view/ViewGroup;I)Landroid/view/View;
    .registers 3

    goto :goto_3

    nop

    :goto_0
    check-cast p1, Lmiuix/flexible/view/HyperCellLayout;

    goto :goto_4

    nop

    :goto_1
    const/4 p0, 0x0

    goto :goto_5

    nop

    :goto_2
    if-nez p0, :cond_0

    goto :goto_7

    :cond_0
    goto :goto_0

    nop

    :goto_3
    instance-of p0, p1, Lmiuix/flexible/view/HyperCellLayout;

    goto :goto_2

    nop

    :goto_4
    invoke-virtual {p1, p2}, Lmiuix/flexible/view/HyperCellLayout;->findViewByAreaId(I)Landroid/view/View;

    move-result-object p0

    goto :goto_6

    nop

    :goto_5
    return-object p0

    :goto_6
    return-object p0

    :goto_7
    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_flexible_template_AbstractMarkTemplate__getChildViewLayoutParamsSafe',
        'method': '.method protected getChildViewLayoutParamsSafe(Landroid/view/View;)Lmiuix/flexible/view/HyperCellLayout$LayoutParams;',
        'method_name': 'getChildViewLayoutParamsSafe',
        'method_anchors': ['invoke-virtual {p1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;', 'if-eqz v0, :cond_0', 'check-cast p0, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;', 'return-object p0', 'new-instance v0, Ljava/lang/IllegalArgumentException;', 'new-instance v1, Ljava/lang/StringBuilder;', 'invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V', 'const-string v2, "LayoutParams "'],
        'type': 'method_replace',
        'search': """.method protected getChildViewLayoutParamsSafe(Landroid/view/View;)Lmiuix/flexible/view/HyperCellLayout$LayoutParams;
    .registers 5

    invoke-virtual {p1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object p0

    instance-of v0, p0, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;

    if-eqz v0, :cond_0

    check-cast p0, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;

    return-object p0

    :cond_0
    new-instance v0, Ljava/lang/IllegalArgumentException;

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "LayoutParams "

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v1, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    const-string p0, " of child view "

    invoke-virtual {v1, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v1, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    const-string p0, " is not instance of HyperCellLayout.LayoutParams! Context is "

    invoke-virtual {v1, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p1}, Landroid/view/View;->getContext()Landroid/content/Context;

    move-result-object p0

    invoke-virtual {v1, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    invoke-direct {v0, p0}, Ljava/lang/IllegalArgumentException;-><init>(Ljava/lang/String;)V

    throw v0
.end method""",
        'replacement': """.method protected getChildViewLayoutParamsSafe(Landroid/view/View;)Lmiuix/flexible/view/HyperCellLayout$LayoutParams;
    .registers 5

    goto :goto_d

    nop

    :goto_0
    new-instance v0, Ljava/lang/IllegalArgumentException;

    goto :goto_4

    nop

    :goto_1
    invoke-virtual {v1, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_e

    nop

    :goto_2
    invoke-virtual {v1, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_f

    nop

    :goto_3
    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_11

    nop

    :goto_4
    new-instance v1, Ljava/lang/StringBuilder;

    goto :goto_6

    nop

    :goto_5
    if-nez v0, :cond_0

    goto :goto_a

    :cond_0
    goto :goto_b

    nop

    :goto_6
    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_10

    nop

    :goto_7
    invoke-direct {v0, p0}, Ljava/lang/IllegalArgumentException;-><init>(Ljava/lang/String;)V

    goto :goto_8

    nop

    :goto_8
    throw v0

    :goto_9
    return-object p0

    :goto_a
    goto :goto_0

    nop

    :goto_b
    check-cast p0, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;

    goto :goto_9

    nop

    :goto_c
    invoke-virtual {v1, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_14

    nop

    :goto_d
    invoke-virtual {p1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object p0

    goto :goto_13

    nop

    :goto_e
    invoke-virtual {v1, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_15

    nop

    :goto_f
    invoke-virtual {p1}, Landroid/view/View;->getContext()Landroid/content/Context;

    move-result-object p0

    goto :goto_c

    nop

    :goto_10
    const-string v2, "LayoutParams "

    goto :goto_3

    nop

    :goto_11
    invoke-virtual {v1, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_12

    nop

    :goto_12
    const-string p0, " of child view "

    goto :goto_1

    nop

    :goto_13
    instance-of v0, p0, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;

    goto :goto_5

    nop

    :goto_14
    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    goto :goto_7

    nop

    :goto_15
    const-string p0, " is not instance of HyperCellLayout.LayoutParams! Context is "

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_flexible_template_AbstractMarkTemplate__getViewNodePriority',
        'method': '.method protected getViewNodePriority(Lmiuix/flexible/mark/ViewNode;)I',
        'method_name': 'getViewNodePriority',
        'method_anchors': ['invoke-virtual {p1}, Lmiuix/flexible/mark/ViewNode;->getView()Landroid/view/View;', 'if-eqz v0, :cond_0', 'invoke-virtual {p1}, Lmiuix/flexible/mark/ViewNode;->getView()Landroid/view/View;', 'invoke-virtual {p0, p1}, Lmiuix/flexible/template/AbstractMarkTemplate;->getChildViewLayoutParamsSafe(Landroid/view/View;)Lmiuix/flexible/view/HyperCellLayout$LayoutParams;', 'invoke-virtual {p0}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getPriority()I', 'return p0', 'if-eqz v0, :cond_1', 'check-cast p1, Lmiuix/flexible/mark/ViewList;'],
        'type': 'method_replace',
        'search': """.method protected getViewNodePriority(Lmiuix/flexible/mark/ViewNode;)I
    .registers 4

    invoke-virtual {p1}, Lmiuix/flexible/mark/ViewNode;->getView()Landroid/view/View;

    move-result-object v0

    if-eqz v0, :cond_0

    invoke-virtual {p1}, Lmiuix/flexible/mark/ViewNode;->getView()Landroid/view/View;

    move-result-object p1

    invoke-virtual {p0, p1}, Lmiuix/flexible/template/AbstractMarkTemplate;->getChildViewLayoutParamsSafe(Landroid/view/View;)Lmiuix/flexible/view/HyperCellLayout$LayoutParams;

    move-result-object p0

    invoke-virtual {p0}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getPriority()I

    move-result p0

    return p0

    :cond_0
    instance-of v0, p1, Lmiuix/flexible/mark/ViewList;

    const/4 v1, 0x0

    if-eqz v0, :cond_1

    check-cast p1, Lmiuix/flexible/mark/ViewList;

    invoke-virtual {p1}, Lmiuix/flexible/mark/ViewList;->getList()Ljava/util/List;

    move-result-object p1

    invoke-interface {p1, v1}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object p1

    check-cast p1, Lmiuix/flexible/mark/ViewNode;

    invoke-virtual {p0, p1}, Lmiuix/flexible/template/AbstractMarkTemplate;->getViewNodePriority(Lmiuix/flexible/mark/ViewNode;)I

    move-result p0

    return p0

    :cond_1
    return v1
.end method""",
        'replacement': """.method protected getViewNodePriority(Lmiuix/flexible/mark/ViewNode;)I
    .registers 4

    goto :goto_10

    nop

    :goto_0
    invoke-virtual {p1}, Lmiuix/flexible/mark/ViewList;->getList()Ljava/util/List;

    move-result-object p1

    goto :goto_b

    nop

    :goto_1
    invoke-virtual {p0, p1}, Lmiuix/flexible/template/AbstractMarkTemplate;->getChildViewLayoutParamsSafe(Landroid/view/View;)Lmiuix/flexible/view/HyperCellLayout$LayoutParams;

    move-result-object p0

    goto :goto_7

    nop

    :goto_2
    return p0

    :goto_3
    goto :goto_11

    nop

    :goto_4
    check-cast p1, Lmiuix/flexible/mark/ViewNode;

    goto :goto_e

    nop

    :goto_5
    invoke-virtual {p1}, Lmiuix/flexible/mark/ViewNode;->getView()Landroid/view/View;

    move-result-object p1

    goto :goto_1

    nop

    :goto_6
    instance-of v0, p1, Lmiuix/flexible/mark/ViewList;

    goto :goto_c

    nop

    :goto_7
    invoke-virtual {p0}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getPriority()I

    move-result p0

    goto :goto_8

    nop

    :goto_8
    return p0

    :goto_9
    goto :goto_6

    nop

    :goto_a
    check-cast p1, Lmiuix/flexible/mark/ViewList;

    goto :goto_0

    nop

    :goto_b
    invoke-interface {p1, v1}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object p1

    goto :goto_4

    nop

    :goto_c
    const/4 v1, 0x0

    goto :goto_f

    nop

    :goto_d
    if-nez v0, :cond_0

    goto :goto_9

    :cond_0
    goto :goto_5

    nop

    :goto_e
    invoke-virtual {p0, p1}, Lmiuix/flexible/template/AbstractMarkTemplate;->getViewNodePriority(Lmiuix/flexible/mark/ViewNode;)I

    move-result p0

    goto :goto_2

    nop

    :goto_f
    if-nez v0, :cond_1

    goto :goto_3

    :cond_1
    goto :goto_a

    nop

    :goto_10
    invoke-virtual {p1}, Lmiuix/flexible/mark/ViewNode;->getView()Landroid/view/View;

    move-result-object v0

    goto :goto_d

    nop

    :goto_11
    return v1
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_flexible_template_AbstractMarkTemplate__hasMatchParentChild',
        'method': '.method protected hasMatchParentChild(Lmiuix/flexible/mark/ViewList;I)Z',
        'method_name': 'hasMatchParentChild',
        'method_anchors': ['invoke-virtual {p1}, Lmiuix/flexible/mark/ViewList;->getList()Ljava/util/List;', 'invoke-interface {p1}, Ljava/util/List;->iterator()Ljava/util/Iterator;', 'invoke-interface {p1}, Ljava/util/Iterator;->hasNext()Z', 'if-eqz v0, :cond_3', 'invoke-interface {p1}, Ljava/util/Iterator;->next()Ljava/lang/Object;', 'check-cast v0, Lmiuix/flexible/mark/ViewNode;', 'if-eqz v1, :cond_1', 'check-cast v0, Lmiuix/flexible/mark/ViewList;'],
        'type': 'method_replace',
        'search': """.method protected hasMatchParentChild(Lmiuix/flexible/mark/ViewList;I)Z
    .registers 6

    invoke-virtual {p1}, Lmiuix/flexible/mark/ViewList;->getList()Ljava/util/List;

    move-result-object p1

    invoke-interface {p1}, Ljava/util/List;->iterator()Ljava/util/Iterator;

    move-result-object p1

    :cond_0
    invoke-interface {p1}, Ljava/util/Iterator;->hasNext()Z

    move-result v0

    if-eqz v0, :cond_3

    invoke-interface {p1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lmiuix/flexible/mark/ViewNode;

    instance-of v1, v0, Lmiuix/flexible/mark/ViewList;

    const/4 v2, 0x1

    if-eqz v1, :cond_1

    check-cast v0, Lmiuix/flexible/mark/ViewList;

    invoke-virtual {p0, v0, p2}, Lmiuix/flexible/template/AbstractMarkTemplate;->hasMatchParentChild(Lmiuix/flexible/mark/ViewList;I)Z

    move-result v0

    if-eqz v0, :cond_0

    return v2

    :cond_1
    invoke-virtual {v0}, Lmiuix/flexible/mark/ViewNode;->getView()Landroid/view/View;

    move-result-object v1

    if-eqz v1, :cond_0

    invoke-virtual {v0}, Lmiuix/flexible/mark/ViewNode;->getView()Landroid/view/View;

    move-result-object v0

    invoke-virtual {p0, v0}, Lmiuix/flexible/template/AbstractMarkTemplate;->getChildViewLayoutParamsSafe(Landroid/view/View;)Lmiuix/flexible/view/HyperCellLayout$LayoutParams;

    move-result-object v0

    const/4 v1, -0x1

    if-ne p2, v2, :cond_2

    iget v0, v0, Landroid/view/ViewGroup$MarginLayoutParams;->width:I

    if-ne v0, v1, :cond_0

    goto :goto_0

    :cond_2
    iget v0, v0, Landroid/view/ViewGroup$MarginLayoutParams;->height:I

    if-ne v0, v1, :cond_0

    :goto_0
    return v2

    :cond_3
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method protected hasMatchParentChild(Lmiuix/flexible/mark/ViewList;I)Z
    .registers 6

    goto :goto_1a

    nop

    :goto_0
    invoke-interface {p1}, Ljava/util/List;->iterator()Ljava/util/Iterator;

    move-result-object p1

    :goto_1
    goto :goto_1d

    nop

    :goto_2
    const/4 v2, 0x1

    goto :goto_17

    nop

    :goto_3
    if-nez v1, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_d

    nop

    :goto_4
    if-eq v0, v1, :cond_1

    goto :goto_1

    :cond_1
    :goto_5
    goto :goto_10

    nop

    :goto_6
    return v2

    :goto_7
    goto :goto_1c

    nop

    :goto_8
    goto :goto_5

    :goto_9
    goto :goto_18

    nop

    :goto_a
    invoke-interface {p1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v0

    goto :goto_15

    nop

    :goto_b
    if-nez v0, :cond_2

    goto :goto_11

    :cond_2
    goto :goto_a

    nop

    :goto_c
    const/4 p0, 0x0

    goto :goto_1b

    nop

    :goto_d
    invoke-virtual {v0}, Lmiuix/flexible/mark/ViewNode;->getView()Landroid/view/View;

    move-result-object v0

    goto :goto_1f

    nop

    :goto_e
    invoke-virtual {p0, v0, p2}, Lmiuix/flexible/template/AbstractMarkTemplate;->hasMatchParentChild(Lmiuix/flexible/mark/ViewList;I)Z

    move-result v0

    goto :goto_14

    nop

    :goto_f
    check-cast v0, Lmiuix/flexible/mark/ViewList;

    goto :goto_e

    nop

    :goto_10
    return v2

    :goto_11
    goto :goto_c

    nop

    :goto_12
    if-eq p2, v2, :cond_3

    goto :goto_9

    :cond_3
    goto :goto_16

    nop

    :goto_13
    instance-of v1, v0, Lmiuix/flexible/mark/ViewList;

    goto :goto_2

    nop

    :goto_14
    if-nez v0, :cond_4

    goto :goto_1

    :cond_4
    goto :goto_6

    nop

    :goto_15
    check-cast v0, Lmiuix/flexible/mark/ViewNode;

    goto :goto_13

    nop

    :goto_16
    iget v0, v0, Landroid/view/ViewGroup$MarginLayoutParams;->width:I

    goto :goto_19

    nop

    :goto_17
    if-nez v1, :cond_5

    goto :goto_7

    :cond_5
    goto :goto_f

    nop

    :goto_18
    iget v0, v0, Landroid/view/ViewGroup$MarginLayoutParams;->height:I

    goto :goto_4

    nop

    :goto_19
    if-eq v0, v1, :cond_6

    goto :goto_1

    :cond_6
    goto :goto_8

    nop

    :goto_1a
    invoke-virtual {p1}, Lmiuix/flexible/mark/ViewList;->getList()Ljava/util/List;

    move-result-object p1

    goto :goto_0

    nop

    :goto_1b
    return p0

    :goto_1c
    invoke-virtual {v0}, Lmiuix/flexible/mark/ViewNode;->getView()Landroid/view/View;

    move-result-object v1

    goto :goto_3

    nop

    :goto_1d
    invoke-interface {p1}, Ljava/util/Iterator;->hasNext()Z

    move-result v0

    goto :goto_b

    nop

    :goto_1e
    const/4 v1, -0x1

    goto :goto_12

    nop

    :goto_1f
    invoke-virtual {p0, v0}, Lmiuix/flexible/template/AbstractMarkTemplate;->getChildViewLayoutParamsSafe(Landroid/view/View;)Lmiuix/flexible/view/HyperCellLayout$LayoutParams;

    move-result-object v0

    goto :goto_1e

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_flexible_template_AbstractMarkTemplate__setGravity',
        'method': '.method protected setGravity(Lmiuix/flexible/view/HyperCellLayout$LayoutParams;Lmiuix/flexible/view/HyperCellLayout$LayoutParams;)V',
        'method_name': 'setGravity',
        'method_anchors': ['invoke-virtual {p1}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getCustomParams()I', 'if-nez p0, :cond_0', 'invoke-virtual {p2}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getGravity()I', 'if-eq p0, v0, :cond_0', 'invoke-virtual {p2}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getGravity()I', 'invoke-virtual {p1, p0}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->setGravity(I)Lmiuix/flexible/view/HyperCellLayout$LayoutParams;', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected setGravity(Lmiuix/flexible/view/HyperCellLayout$LayoutParams;Lmiuix/flexible/view/HyperCellLayout$LayoutParams;)V
    .registers 4

    invoke-virtual {p1}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getCustomParams()I

    move-result p0

    and-int/lit8 p0, p0, 0x1

    if-nez p0, :cond_0

    invoke-virtual {p2}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getGravity()I

    move-result p0

    const v0, 0x7fffffff

    if-eq p0, v0, :cond_0

    invoke-virtual {p2}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getGravity()I

    move-result p0

    invoke-virtual {p1, p0}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->setGravity(I)Lmiuix/flexible/view/HyperCellLayout$LayoutParams;

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected setGravity(Lmiuix/flexible/view/HyperCellLayout$LayoutParams;Lmiuix/flexible/view/HyperCellLayout$LayoutParams;)V
    .registers 4

    goto :goto_9

    nop

    :goto_0
    invoke-virtual {p1, p0}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->setGravity(I)Lmiuix/flexible/view/HyperCellLayout$LayoutParams;

    :goto_1
    goto :goto_5

    nop

    :goto_2
    if-ne p0, v0, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_3

    nop

    :goto_3
    invoke-virtual {p2}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getGravity()I

    move-result p0

    goto :goto_0

    nop

    :goto_4
    const v0, 0x7fffffff

    goto :goto_2

    nop

    :goto_5
    return-void

    :goto_6
    if-eqz p0, :cond_1

    goto :goto_1

    :cond_1
    goto :goto_8

    nop

    :goto_7
    and-int/lit8 p0, p0, 0x1

    goto :goto_6

    nop

    :goto_8
    invoke-virtual {p2}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getGravity()I

    move-result p0

    goto :goto_4

    nop

    :goto_9
    invoke-virtual {p1}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getCustomParams()I

    move-result p0

    goto :goto_7

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_flexible_template_AbstractMarkTemplate__setMargin',
        'method': '.method protected setMargin(Lmiuix/flexible/view/HyperCellLayout$LayoutParams;Lmiuix/flexible/view/HyperCellLayout$LayoutParams;)V',
        'method_name': 'setMargin',
        'method_anchors': ['invoke-virtual {p1}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getCustomParams()I', 'if-nez v0, :cond_0', 'invoke-virtual {p2}, Landroid/view/ViewGroup$MarginLayoutParams;->getMarginStart()I', 'if-eq v0, v1, :cond_0', 'invoke-virtual {p2}, Landroid/view/ViewGroup$MarginLayoutParams;->getMarginStart()I', 'invoke-virtual {p0, v0}, Lmiuix/flexible/template/AbstractMarkTemplate;->dp2px(F)I', 'invoke-virtual {p1, v0}, Landroid/view/ViewGroup$MarginLayoutParams;->setMarginStart(I)V', 'invoke-virtual {p1}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getCustomParams()I'],
        'type': 'method_replace',
        'search': """.method protected setMargin(Lmiuix/flexible/view/HyperCellLayout$LayoutParams;Lmiuix/flexible/view/HyperCellLayout$LayoutParams;)V
    .registers 5

    invoke-virtual {p1}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getCustomParams()I

    move-result v0

    and-int/lit8 v0, v0, 0x2

    const v1, 0x7fffffff

    if-nez v0, :cond_0

    invoke-virtual {p2}, Landroid/view/ViewGroup$MarginLayoutParams;->getMarginStart()I

    move-result v0

    if-eq v0, v1, :cond_0

    invoke-virtual {p2}, Landroid/view/ViewGroup$MarginLayoutParams;->getMarginStart()I

    move-result v0

    int-to-float v0, v0

    invoke-virtual {p0, v0}, Lmiuix/flexible/template/AbstractMarkTemplate;->dp2px(F)I

    move-result v0

    invoke-virtual {p1, v0}, Landroid/view/ViewGroup$MarginLayoutParams;->setMarginStart(I)V

    :cond_0
    invoke-virtual {p1}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getCustomParams()I

    move-result v0

    and-int/lit8 v0, v0, 0x4

    if-nez v0, :cond_1

    invoke-virtual {p2}, Landroid/view/ViewGroup$MarginLayoutParams;->getMarginEnd()I

    move-result v0

    if-eq v0, v1, :cond_1

    invoke-virtual {p2}, Landroid/view/ViewGroup$MarginLayoutParams;->getMarginEnd()I

    move-result v0

    int-to-float v0, v0

    invoke-virtual {p0, v0}, Lmiuix/flexible/template/AbstractMarkTemplate;->dp2px(F)I

    move-result v0

    invoke-virtual {p1, v0}, Landroid/view/ViewGroup$MarginLayoutParams;->setMarginEnd(I)V

    :cond_1
    invoke-virtual {p1}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getCustomParams()I

    move-result v0

    and-int/lit8 v0, v0, 0x8

    if-nez v0, :cond_2

    iget v0, p2, Landroid/view/ViewGroup$MarginLayoutParams;->topMargin:I

    if-eq v0, v1, :cond_2

    int-to-float v0, v0

    invoke-virtual {p0, v0}, Lmiuix/flexible/template/AbstractMarkTemplate;->dp2px(F)I

    move-result v0

    iput v0, p1, Landroid/view/ViewGroup$MarginLayoutParams;->topMargin:I

    :cond_2
    invoke-virtual {p1}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getCustomParams()I

    move-result v0

    and-int/lit8 v0, v0, 0x10

    if-nez v0, :cond_3

    iget p2, p2, Landroid/view/ViewGroup$MarginLayoutParams;->bottomMargin:I

    if-eq p2, v1, :cond_3

    int-to-float p2, p2

    invoke-virtual {p0, p2}, Lmiuix/flexible/template/AbstractMarkTemplate;->dp2px(F)I

    move-result p0

    iput p0, p1, Landroid/view/ViewGroup$MarginLayoutParams;->bottomMargin:I

    :cond_3
    return-void
.end method""",
        'replacement': """.method protected setMargin(Lmiuix/flexible/view/HyperCellLayout$LayoutParams;Lmiuix/flexible/view/HyperCellLayout$LayoutParams;)V
    .registers 5

    goto :goto_7

    nop

    :goto_0
    if-ne p2, v1, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_24

    nop

    :goto_1
    iput p0, p1, Landroid/view/ViewGroup$MarginLayoutParams;->bottomMargin:I

    :goto_2
    goto :goto_16

    nop

    :goto_3
    invoke-virtual {p1}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getCustomParams()I

    move-result v0

    goto :goto_1a

    nop

    :goto_4
    if-ne v0, v1, :cond_1

    goto :goto_12

    :cond_1
    goto :goto_1c

    nop

    :goto_5
    invoke-virtual {p1}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getCustomParams()I

    move-result v0

    goto :goto_10

    nop

    :goto_6
    int-to-float v0, v0

    goto :goto_21

    nop

    :goto_7
    invoke-virtual {p1}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getCustomParams()I

    move-result v0

    goto :goto_18

    nop

    :goto_8
    if-eqz v0, :cond_2

    goto :goto_2

    :cond_2
    goto :goto_13

    nop

    :goto_9
    invoke-virtual {p2}, Landroid/view/ViewGroup$MarginLayoutParams;->getMarginEnd()I

    move-result v0

    goto :goto_4

    nop

    :goto_a
    and-int/lit8 v0, v0, 0x10

    goto :goto_8

    nop

    :goto_b
    invoke-virtual {p0, v0}, Lmiuix/flexible/template/AbstractMarkTemplate;->dp2px(F)I

    move-result v0

    goto :goto_14

    nop

    :goto_c
    iget v0, p2, Landroid/view/ViewGroup$MarginLayoutParams;->topMargin:I

    goto :goto_25

    nop

    :goto_d
    if-eqz v0, :cond_3

    goto :goto_12

    :cond_3
    goto :goto_9

    nop

    :goto_e
    iput v0, p1, Landroid/view/ViewGroup$MarginLayoutParams;->topMargin:I

    :goto_f
    goto :goto_1d

    nop

    :goto_10
    and-int/lit8 v0, v0, 0x8

    goto :goto_22

    nop

    :goto_11
    invoke-virtual {p1, v0}, Landroid/view/ViewGroup$MarginLayoutParams;->setMarginEnd(I)V

    :goto_12
    goto :goto_5

    nop

    :goto_13
    iget p2, p2, Landroid/view/ViewGroup$MarginLayoutParams;->bottomMargin:I

    goto :goto_0

    nop

    :goto_14
    invoke-virtual {p1, v0}, Landroid/view/ViewGroup$MarginLayoutParams;->setMarginStart(I)V

    :goto_15
    goto :goto_3

    nop

    :goto_16
    return-void

    :goto_17
    if-ne v0, v1, :cond_4

    goto :goto_15

    :cond_4
    goto :goto_1e

    nop

    :goto_18
    and-int/lit8 v0, v0, 0x2

    goto :goto_1f

    nop

    :goto_19
    int-to-float v0, v0

    goto :goto_20

    nop

    :goto_1a
    and-int/lit8 v0, v0, 0x4

    goto :goto_d

    nop

    :goto_1b
    if-eqz v0, :cond_5

    goto :goto_15

    :cond_5
    goto :goto_23

    nop

    :goto_1c
    invoke-virtual {p2}, Landroid/view/ViewGroup$MarginLayoutParams;->getMarginEnd()I

    move-result v0

    goto :goto_19

    nop

    :goto_1d
    invoke-virtual {p1}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getCustomParams()I

    move-result v0

    goto :goto_a

    nop

    :goto_1e
    invoke-virtual {p2}, Landroid/view/ViewGroup$MarginLayoutParams;->getMarginStart()I

    move-result v0

    goto :goto_27

    nop

    :goto_1f
    const v1, 0x7fffffff

    goto :goto_1b

    nop

    :goto_20
    invoke-virtual {p0, v0}, Lmiuix/flexible/template/AbstractMarkTemplate;->dp2px(F)I

    move-result v0

    goto :goto_11

    nop

    :goto_21
    invoke-virtual {p0, v0}, Lmiuix/flexible/template/AbstractMarkTemplate;->dp2px(F)I

    move-result v0

    goto :goto_e

    nop

    :goto_22
    if-eqz v0, :cond_6

    goto :goto_f

    :cond_6
    goto :goto_c

    nop

    :goto_23
    invoke-virtual {p2}, Landroid/view/ViewGroup$MarginLayoutParams;->getMarginStart()I

    move-result v0

    goto :goto_17

    nop

    :goto_24
    int-to-float p2, p2

    goto :goto_26

    nop

    :goto_25
    if-ne v0, v1, :cond_7

    goto :goto_f

    :cond_7
    goto :goto_6

    nop

    :goto_26
    invoke-virtual {p0, p2}, Lmiuix/flexible/template/AbstractMarkTemplate;->dp2px(F)I

    move-result p0

    goto :goto_1

    nop

    :goto_27
    int-to-float v0, v0

    goto :goto_b

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_flexible_template_AbstractMarkTemplate__setPriority',
        'method': '.method protected setPriority(Lmiuix/flexible/view/HyperCellLayout$LayoutParams;Lmiuix/flexible/view/HyperCellLayout$LayoutParams;)V',
        'method_name': 'setPriority',
        'method_anchors': ['invoke-virtual {p1}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getCustomParams()I', 'if-nez p0, :cond_0', 'invoke-virtual {p2}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getPriority()I', 'if-eq p0, v0, :cond_0', 'invoke-virtual {p2}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getPriority()I', 'invoke-virtual {p1, p0}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->setPriority(I)Lmiuix/flexible/view/HyperCellLayout$LayoutParams;', 'invoke-virtual {p1}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getCustomParams()I', 'if-nez p0, :cond_1'],
        'type': 'method_replace',
        'search': """.method protected setPriority(Lmiuix/flexible/view/HyperCellLayout$LayoutParams;Lmiuix/flexible/view/HyperCellLayout$LayoutParams;)V
    .registers 4

    invoke-virtual {p1}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getCustomParams()I

    move-result p0

    and-int/lit16 p0, p0, 0x80

    const v0, 0x7fffffff

    if-nez p0, :cond_0

    invoke-virtual {p2}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getPriority()I

    move-result p0

    if-eq p0, v0, :cond_0

    invoke-virtual {p2}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getPriority()I

    move-result p0

    invoke-virtual {p1, p0}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->setPriority(I)Lmiuix/flexible/view/HyperCellLayout$LayoutParams;

    :cond_0
    invoke-virtual {p1}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getCustomParams()I

    move-result p0

    and-int/lit16 p0, p0, 0x100

    if-nez p0, :cond_1

    invoke-virtual {p2}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getGroupPriority()I

    move-result p0

    if-eq p0, v0, :cond_1

    invoke-virtual {p2}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getGroupPriority()I

    move-result p0

    invoke-virtual {p1, p0}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->setGroupPriority(I)Lmiuix/flexible/view/HyperCellLayout$LayoutParams;

    :cond_1
    return-void
.end method""",
        'replacement': """.method protected setPriority(Lmiuix/flexible/view/HyperCellLayout$LayoutParams;Lmiuix/flexible/view/HyperCellLayout$LayoutParams;)V
    .registers 4

    goto :goto_10

    nop

    :goto_0
    and-int/lit16 p0, p0, 0x80

    goto :goto_d

    nop

    :goto_1
    if-ne p0, v0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_f

    nop

    :goto_2
    if-ne p0, v0, :cond_1

    goto :goto_b

    :cond_1
    goto :goto_9

    nop

    :goto_3
    invoke-virtual {p1, p0}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->setGroupPriority(I)Lmiuix/flexible/view/HyperCellLayout$LayoutParams;

    :goto_4
    goto :goto_6

    nop

    :goto_5
    if-eqz p0, :cond_2

    goto :goto_4

    :cond_2
    goto :goto_7

    nop

    :goto_6
    return-void

    :goto_7
    invoke-virtual {p2}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getGroupPriority()I

    move-result p0

    goto :goto_1

    nop

    :goto_8
    invoke-virtual {p1}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getCustomParams()I

    move-result p0

    goto :goto_11

    nop

    :goto_9
    invoke-virtual {p2}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getPriority()I

    move-result p0

    goto :goto_a

    nop

    :goto_a
    invoke-virtual {p1, p0}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->setPriority(I)Lmiuix/flexible/view/HyperCellLayout$LayoutParams;

    :goto_b
    goto :goto_8

    nop

    :goto_c
    if-eqz p0, :cond_3

    goto :goto_b

    :cond_3
    goto :goto_e

    nop

    :goto_d
    const v0, 0x7fffffff

    goto :goto_c

    nop

    :goto_e
    invoke-virtual {p2}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getPriority()I

    move-result p0

    goto :goto_2

    nop

    :goto_f
    invoke-virtual {p2}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getGroupPriority()I

    move-result p0

    goto :goto_3

    nop

    :goto_10
    invoke-virtual {p1}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getCustomParams()I

    move-result p0

    goto :goto_0

    nop

    :goto_11
    and-int/lit16 p0, p0, 0x100

    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_flexible_template_AbstractMarkTemplate__setWidthHeight',
        'method': '.method protected setWidthHeight(Lmiuix/flexible/view/HyperCellLayout$LayoutParams;Lmiuix/flexible/view/HyperCellLayout$LayoutParams;)V',
        'method_name': 'setWidthHeight',
        'method_anchors': ['invoke-virtual {p1}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getCustomParams()I', 'if-nez p0, :cond_0', 'iget p0, p2, Landroid/view/ViewGroup$MarginLayoutParams;->width:I', 'if-eq p0, v0, :cond_0', 'iput p0, p1, Landroid/view/ViewGroup$MarginLayoutParams;->width:I', 'invoke-virtual {p1}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getCustomParams()I', 'if-nez p0, :cond_1', 'iget p0, p2, Landroid/view/ViewGroup$MarginLayoutParams;->height:I'],
        'type': 'method_replace',
        'search': """.method protected setWidthHeight(Lmiuix/flexible/view/HyperCellLayout$LayoutParams;Lmiuix/flexible/view/HyperCellLayout$LayoutParams;)V
    .registers 4

    invoke-virtual {p1}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getCustomParams()I

    move-result p0

    and-int/lit8 p0, p0, 0x20

    const v0, 0x7fffffff

    if-nez p0, :cond_0

    iget p0, p2, Landroid/view/ViewGroup$MarginLayoutParams;->width:I

    if-eq p0, v0, :cond_0

    iput p0, p1, Landroid/view/ViewGroup$MarginLayoutParams;->width:I

    :cond_0
    invoke-virtual {p1}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getCustomParams()I

    move-result p0

    and-int/lit8 p0, p0, 0x40

    if-nez p0, :cond_1

    iget p0, p2, Landroid/view/ViewGroup$MarginLayoutParams;->height:I

    if-eq p0, v0, :cond_1

    iput p0, p1, Landroid/view/ViewGroup$MarginLayoutParams;->height:I

    :cond_1
    return-void
.end method""",
        'replacement': """.method protected setWidthHeight(Lmiuix/flexible/view/HyperCellLayout$LayoutParams;Lmiuix/flexible/view/HyperCellLayout$LayoutParams;)V
    .registers 4

    goto :goto_3

    nop

    :goto_0
    and-int/lit8 p0, p0, 0x40

    goto :goto_d

    nop

    :goto_1
    iput p0, p1, Landroid/view/ViewGroup$MarginLayoutParams;->width:I

    :goto_2
    goto :goto_a

    nop

    :goto_3
    invoke-virtual {p1}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getCustomParams()I

    move-result p0

    goto :goto_e

    nop

    :goto_4
    iget p0, p2, Landroid/view/ViewGroup$MarginLayoutParams;->width:I

    goto :goto_9

    nop

    :goto_5
    iput p0, p1, Landroid/view/ViewGroup$MarginLayoutParams;->height:I

    :goto_6
    goto :goto_f

    nop

    :goto_7
    iget p0, p2, Landroid/view/ViewGroup$MarginLayoutParams;->height:I

    goto :goto_c

    nop

    :goto_8
    const v0, 0x7fffffff

    goto :goto_b

    nop

    :goto_9
    if-ne p0, v0, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_1

    nop

    :goto_a
    invoke-virtual {p1}, Lmiuix/flexible/view/HyperCellLayout$LayoutParams;->getCustomParams()I

    move-result p0

    goto :goto_0

    nop

    :goto_b
    if-eqz p0, :cond_1

    goto :goto_2

    :cond_1
    goto :goto_4

    nop

    :goto_c
    if-ne p0, v0, :cond_2

    goto :goto_6

    :cond_2
    goto :goto_5

    nop

    :goto_d
    if-eqz p0, :cond_3

    goto :goto_6

    :cond_3
    goto :goto_7

    nop

    :goto_e
    and-int/lit8 p0, p0, 0x20

    goto :goto_8

    nop

    :goto_f
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
