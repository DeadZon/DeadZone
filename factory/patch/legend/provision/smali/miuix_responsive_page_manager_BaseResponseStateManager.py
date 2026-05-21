TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/responsive/page/manager/BaseResponseStateManager.smali'
CLASS_FALLBACK_NAMES = ['BaseResponseStateManager.smali']
CLASS_ANCHORS = ['.super Lmiuix/responsive/page/manager/BaseStateManager;']

PATCHES = [
    {
        'id': 'miuix_responsive_page_manager_BaseResponseStateManager__parseResponsiveViews',
        'method': '.method parseResponsiveViews(Landroid/content/Context;Landroid/view/View;Landroid/util/AttributeSet;Ljava/lang/String;)V',
        'method_name': 'parseResponsiveViews',
        'method_anchors': ['iget-object v0, p0, Lmiuix/responsive/page/manager/BaseResponseStateManager;->mRootView:Landroid/view/View;', 'if-nez v0, :cond_0', 'iput-object p2, p0, Lmiuix/responsive/page/manager/BaseResponseStateManager;->mRootView:Landroid/view/View;', 'sget-object v0, Lmiuix/core/R$styleable;->ResponsiveSpec:[I', 'invoke-virtual {p1, p3, v0}, Landroid/content/Context;->obtainStyledAttributes(Landroid/util/AttributeSet;[I)Landroid/content/res/TypedArray;', 'const-string p3, "\\\\."', 'invoke-virtual {p4, p3}, Ljava/lang/String;->split(Ljava/lang/String;)[Ljava/lang/String;', 'if-le p3, v0, :cond_1'],
        'type': 'method_replace',
        'search': """.method parseResponsiveViews(Landroid/content/Context;Landroid/view/View;Landroid/util/AttributeSet;Ljava/lang/String;)V
    .registers 7

    iget-object v0, p0, Lmiuix/responsive/page/manager/BaseResponseStateManager;->mRootView:Landroid/view/View;

    if-nez v0, :cond_0

    iput-object p2, p0, Lmiuix/responsive/page/manager/BaseResponseStateManager;->mRootView:Landroid/view/View;

    :cond_0
    sget-object v0, Lmiuix/core/R$styleable;->ResponsiveSpec:[I

    invoke-virtual {p1, p3, v0}, Landroid/content/Context;->obtainStyledAttributes(Landroid/util/AttributeSet;[I)Landroid/content/res/TypedArray;

    move-result-object p1

    const-string p3, "\\."

    invoke-virtual {p4, p3}, Ljava/lang/String;->split(Ljava/lang/String;)[Ljava/lang/String;

    move-result-object p3

    array-length p3, p3

    const/4 v0, 0x1

    const/4 v1, -0x1

    if-le p3, v0, :cond_1

    invoke-static {p4}, Lmiuix/reflect/Reflects;->forName(Ljava/lang/String;)Ljava/lang/Class;

    move-result-object p3

    const-class p4, Lmiuix/responsive/interfaces/IViewResponsive;

    invoke-virtual {p4, p3}, Ljava/lang/Class;->isAssignableFrom(Ljava/lang/Class;)Z

    move-result p3

    if-eqz p3, :cond_1

    sget p3, Lmiuix/core/R$styleable;->ResponsiveSpec_android_id:I

    invoke-virtual {p1, p3, v1}, Landroid/content/res/TypedArray;->getResourceId(II)I

    move-result p3

    if-eq p3, v1, :cond_1

    iget-object p4, p0, Lmiuix/responsive/page/manager/BaseResponseStateManager;->mViewResponsives:Landroid/util/ArrayMap;

    invoke-static {p3}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p3

    const/4 v0, 0x0

    invoke-virtual {p4, p3, v0}, Landroid/util/ArrayMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    :cond_1
    sget p3, Lmiuix/core/R$styleable;->ResponsiveSpec_effectiveScreenOrientation:I

    const/4 p4, 0x0

    invoke-virtual {p1, p3, p4}, Landroid/content/res/TypedArray;->getInteger(II)I

    move-result p3

    if-eqz p3, :cond_2

    sget p2, Lmiuix/core/R$styleable;->ResponsiveSpec_android_id:I

    invoke-virtual {p1, p2, v1}, Landroid/content/res/TypedArray;->getResourceId(II)I

    move-result p2

    if-eq p2, v1, :cond_4

    new-instance p4, Lmiuix/responsive/map/ResponsiveViewSpec;

    invoke-direct {p4, p2}, Lmiuix/responsive/map/ResponsiveViewSpec;-><init>(I)V

    invoke-virtual {p4, p3}, Lmiuix/responsive/map/ResponsiveViewSpec;->setEffectiveScreenOrientation(I)V

    iget-object p0, p0, Lmiuix/responsive/page/manager/BaseResponseStateManager;->mResponsiveViewGroup:Landroid/util/ArrayMap;

    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p2

    invoke-virtual {p0, p2, p4}, Landroid/util/ArrayMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_0

    :cond_2
    sget p3, Lmiuix/core/R$styleable;->ResponsiveSpec_hideInScreenMode:I

    invoke-virtual {p1, p3, p4}, Landroid/content/res/TypedArray;->getInteger(II)I

    move-result p3

    if-eqz p3, :cond_4

    iget-object p4, p0, Lmiuix/responsive/page/manager/BaseResponseStateManager;->mResponsiveMapChild:Landroid/util/ArrayMap;

    invoke-virtual {p4, p2}, Landroid/util/ArrayMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p4

    check-cast p4, Ljava/util/List;

    if-nez p4, :cond_3

    new-instance p4, Ljava/util/ArrayList;

    invoke-direct {p4}, Ljava/util/ArrayList;-><init>()V

    iget-object v0, p0, Lmiuix/responsive/page/manager/BaseResponseStateManager;->mResponsiveMapChild:Landroid/util/ArrayMap;

    invoke-virtual {v0, p2, p4}, Landroid/util/ArrayMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    invoke-direct {p0, p2}, Lmiuix/responsive/page/manager/BaseResponseStateManager;->bindResponseView(Landroid/view/View;)V

    check-cast p2, Landroid/view/ViewGroup;

    invoke-direct {p0, p2}, Lmiuix/responsive/page/manager/BaseResponseStateManager;->injectOnHierarchyChangeListener(Landroid/view/ViewGroup;)V

    :cond_3
    sget p0, Lmiuix/core/R$styleable;->ResponsiveSpec_android_id:I

    invoke-virtual {p1, p0, v1}, Landroid/content/res/TypedArray;->getResourceId(II)I

    move-result p0

    if-eq p0, v1, :cond_4

    new-instance p2, Lmiuix/responsive/map/ResponsiveViewSpec;

    invoke-direct {p2, p0, p3}, Lmiuix/responsive/map/ResponsiveViewSpec;-><init>(II)V

    invoke-interface {p4, p2}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    :cond_4
    :goto_0
    invoke-virtual {p1}, Landroid/content/res/TypedArray;->recycle()V

    return-void
.end method""",
        'replacement': """.method parseResponsiveViews(Landroid/content/Context;Landroid/view/View;Landroid/util/AttributeSet;Ljava/lang/String;)V
    .registers 7

    goto :goto_c

    nop

    :goto_0
    new-instance p2, Lmiuix/responsive/map/ResponsiveViewSpec;

    goto :goto_7

    nop

    :goto_1
    if-nez p3, :cond_0

    goto :goto_11

    :cond_0
    goto :goto_b

    nop

    :goto_2
    if-eqz v0, :cond_1

    goto :goto_5

    :cond_1
    goto :goto_4

    nop

    :goto_3
    iget-object p0, p0, Lmiuix/responsive/page/manager/BaseResponseStateManager;->mResponsiveViewGroup:Landroid/util/ArrayMap;

    goto :goto_1f

    nop

    :goto_4
    iput-object p2, p0, Lmiuix/responsive/page/manager/BaseResponseStateManager;->mRootView:Landroid/view/View;

    :goto_5
    goto :goto_2e

    nop

    :goto_6
    if-nez p3, :cond_2

    goto :goto_18

    :cond_2
    goto :goto_35

    nop

    :goto_7
    invoke-direct {p2, p0, p3}, Lmiuix/responsive/map/ResponsiveViewSpec;-><init>(II)V

    goto :goto_17

    nop

    :goto_8
    invoke-virtual {p4, p3, v0}, Landroid/util/ArrayMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    :goto_9
    goto :goto_1e

    nop

    :goto_a
    array-length p3, p3

    goto :goto_f

    nop

    :goto_b
    sget p2, Lmiuix/core/R$styleable;->ResponsiveSpec_android_id:I

    goto :goto_37

    nop

    :goto_c
    iget-object v0, p0, Lmiuix/responsive/page/manager/BaseResponseStateManager;->mRootView:Landroid/view/View;

    goto :goto_2

    nop

    :goto_d
    check-cast p4, Ljava/util/List;

    goto :goto_33

    nop

    :goto_e
    invoke-virtual {p1, p3, p4}, Landroid/content/res/TypedArray;->getInteger(II)I

    move-result p3

    goto :goto_1

    nop

    :goto_f
    const/4 v0, 0x1

    goto :goto_3a

    nop

    :goto_10
    goto :goto_18

    :goto_11
    goto :goto_2b

    nop

    :goto_12
    invoke-virtual {p4, p2}, Landroid/util/ArrayMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p4

    goto :goto_d

    nop

    :goto_13
    invoke-virtual {p4, p3}, Ljava/lang/Class;->isAssignableFrom(Ljava/lang/Class;)Z

    move-result p3

    goto :goto_29

    nop

    :goto_14
    if-ne p2, v1, :cond_3

    goto :goto_18

    :cond_3
    goto :goto_19

    nop

    :goto_15
    if-ne p0, v1, :cond_4

    goto :goto_18

    :cond_4
    goto :goto_0

    nop

    :goto_16
    if-ne p3, v1, :cond_5

    goto :goto_9

    :cond_5
    goto :goto_20

    nop

    :goto_17
    invoke-interface {p4, p2}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    :goto_18
    goto :goto_1c

    nop

    :goto_19
    new-instance p4, Lmiuix/responsive/map/ResponsiveViewSpec;

    goto :goto_1b

    nop

    :goto_1a
    new-instance p4, Ljava/util/ArrayList;

    goto :goto_2f

    nop

    :goto_1b
    invoke-direct {p4, p2}, Lmiuix/responsive/map/ResponsiveViewSpec;-><init>(I)V

    goto :goto_3e

    nop

    :goto_1c
    invoke-virtual {p1}, Landroid/content/res/TypedArray;->recycle()V

    goto :goto_39

    nop

    :goto_1d
    const/4 v0, 0x0

    goto :goto_8

    nop

    :goto_1e
    sget p3, Lmiuix/core/R$styleable;->ResponsiveSpec_effectiveScreenOrientation:I

    goto :goto_30

    nop

    :goto_1f
    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p2

    goto :goto_36

    nop

    :goto_20
    iget-object p4, p0, Lmiuix/responsive/page/manager/BaseResponseStateManager;->mViewResponsives:Landroid/util/ArrayMap;

    goto :goto_2a

    nop

    :goto_21
    iget-object v0, p0, Lmiuix/responsive/page/manager/BaseResponseStateManager;->mResponsiveMapChild:Landroid/util/ArrayMap;

    goto :goto_22

    nop

    :goto_22
    invoke-virtual {v0, p2, p4}, Landroid/util/ArrayMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_31

    nop

    :goto_23
    invoke-static {p4}, Lmiuix/reflect/Reflects;->forName(Ljava/lang/String;)Ljava/lang/Class;

    move-result-object p3

    goto :goto_26

    nop

    :goto_24
    invoke-virtual {p1, p0, v1}, Landroid/content/res/TypedArray;->getResourceId(II)I

    move-result p0

    goto :goto_15

    nop

    :goto_25
    invoke-virtual {p1, p3, v0}, Landroid/content/Context;->obtainStyledAttributes(Landroid/util/AttributeSet;[I)Landroid/content/res/TypedArray;

    move-result-object p1

    goto :goto_32

    nop

    :goto_26
    const-class p4, Lmiuix/responsive/interfaces/IViewResponsive;

    goto :goto_13

    nop

    :goto_27
    invoke-direct {p0, p2}, Lmiuix/responsive/page/manager/BaseResponseStateManager;->injectOnHierarchyChangeListener(Landroid/view/ViewGroup;)V

    :goto_28
    goto :goto_38

    nop

    :goto_29
    if-nez p3, :cond_6

    goto :goto_9

    :cond_6
    goto :goto_2d

    nop

    :goto_2a
    invoke-static {p3}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p3

    goto :goto_1d

    nop

    :goto_2b
    sget p3, Lmiuix/core/R$styleable;->ResponsiveSpec_hideInScreenMode:I

    goto :goto_3d

    nop

    :goto_2c
    check-cast p2, Landroid/view/ViewGroup;

    goto :goto_27

    nop

    :goto_2d
    sget p3, Lmiuix/core/R$styleable;->ResponsiveSpec_android_id:I

    goto :goto_3c

    nop

    :goto_2e
    sget-object v0, Lmiuix/core/R$styleable;->ResponsiveSpec:[I

    goto :goto_25

    nop

    :goto_2f
    invoke-direct {p4}, Ljava/util/ArrayList;-><init>()V

    goto :goto_21

    nop

    :goto_30
    const/4 p4, 0x0

    goto :goto_e

    nop

    :goto_31
    invoke-direct {p0, p2}, Lmiuix/responsive/page/manager/BaseResponseStateManager;->bindResponseView(Landroid/view/View;)V

    goto :goto_2c

    nop

    :goto_32
    const-string p3, "\\."

    goto :goto_3b

    nop

    :goto_33
    if-eqz p4, :cond_7

    goto :goto_28

    :cond_7
    goto :goto_1a

    nop

    :goto_34
    if-gt p3, v0, :cond_8

    goto :goto_9

    :cond_8
    goto :goto_23

    nop

    :goto_35
    iget-object p4, p0, Lmiuix/responsive/page/manager/BaseResponseStateManager;->mResponsiveMapChild:Landroid/util/ArrayMap;

    goto :goto_12

    nop

    :goto_36
    invoke-virtual {p0, p2, p4}, Landroid/util/ArrayMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_10

    nop

    :goto_37
    invoke-virtual {p1, p2, v1}, Landroid/content/res/TypedArray;->getResourceId(II)I

    move-result p2

    goto :goto_14

    nop

    :goto_38
    sget p0, Lmiuix/core/R$styleable;->ResponsiveSpec_android_id:I

    goto :goto_24

    nop

    :goto_39
    return-void

    :goto_3a
    const/4 v1, -0x1

    goto :goto_34

    nop

    :goto_3b
    invoke-virtual {p4, p3}, Ljava/lang/String;->split(Ljava/lang/String;)[Ljava/lang/String;

    move-result-object p3

    goto :goto_a

    nop

    :goto_3c
    invoke-virtual {p1, p3, v1}, Landroid/content/res/TypedArray;->getResourceId(II)I

    move-result p3

    goto :goto_16

    nop

    :goto_3d
    invoke-virtual {p1, p3, p4}, Landroid/content/res/TypedArray;->getInteger(II)I

    move-result p3

    goto :goto_6

    nop

    :goto_3e
    invoke-virtual {p4, p3}, Lmiuix/responsive/map/ResponsiveViewSpec;->setEffectiveScreenOrientation(I)V

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_responsive_page_manager_BaseResponseStateManager__notifyResponseChange',
        'method': '.method protected notifyResponseChange(Landroid/content/res/Configuration;Lmiuix/responsive/map/ResponsiveState;Z)V',
        'method_name': 'notifyResponseChange',
        'method_anchors': ['new-instance v0, Lmiuix/responsive/map/ScreenSpec;', 'invoke-direct {v0}, Lmiuix/responsive/map/ScreenSpec;-><init>()V', 'if-eqz p2, :cond_0', 'invoke-virtual {p2, v0}, Lmiuix/responsive/map/ResponsiveState;->toScreenSpec(Lmiuix/responsive/map/ScreenSpec;)V', 'iget-object p2, p0, Lmiuix/responsive/page/manager/BaseResponseStateManager;->mPageInfo:Lmiuix/responsive/interfaces/IResponsive;', 'invoke-interface {p2, p1, v0, p3}, Lmiuix/responsive/interfaces/IResponsive;->dispatchResponsiveLayout(Landroid/content/res/Configuration;Lmiuix/responsive/map/ScreenSpec;Z)V', 'iget-object p2, p0, Lmiuix/responsive/page/manager/BaseResponseStateManager;->mResponsiveMap:Landroid/util/ArrayMap;', 'invoke-virtual {p2}, Landroid/util/ArrayMap;->keySet()Ljava/util/Set;'],
        'type': 'method_replace',
        'search': """.method protected notifyResponseChange(Landroid/content/res/Configuration;Lmiuix/responsive/map/ResponsiveState;Z)V
    .registers 7

    new-instance v0, Lmiuix/responsive/map/ScreenSpec;

    invoke-direct {v0}, Lmiuix/responsive/map/ScreenSpec;-><init>()V

    if-eqz p2, :cond_0

    invoke-virtual {p2, v0}, Lmiuix/responsive/map/ResponsiveState;->toScreenSpec(Lmiuix/responsive/map/ScreenSpec;)V

    :cond_0
    iget-object p2, p0, Lmiuix/responsive/page/manager/BaseResponseStateManager;->mPageInfo:Lmiuix/responsive/interfaces/IResponsive;

    invoke-interface {p2, p1, v0, p3}, Lmiuix/responsive/interfaces/IResponsive;->dispatchResponsiveLayout(Landroid/content/res/Configuration;Lmiuix/responsive/map/ScreenSpec;Z)V

    iget-object p2, p0, Lmiuix/responsive/page/manager/BaseResponseStateManager;->mResponsiveMap:Landroid/util/ArrayMap;

    invoke-virtual {p2}, Landroid/util/ArrayMap;->keySet()Ljava/util/Set;

    move-result-object p2

    invoke-interface {p2}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object p2

    :cond_1
    :goto_0
    invoke-interface {p2}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_2

    invoke-interface {p2}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Landroid/view/View;

    iget-object v2, p0, Lmiuix/responsive/page/manager/BaseResponseStateManager;->mResponsiveMap:Landroid/util/ArrayMap;

    invoke-virtual {v2, v1}, Landroid/util/ArrayMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lmiuix/responsive/interfaces/IResponsive;

    if-eqz v1, :cond_1

    invoke-interface {v1, p1, v0, p3}, Lmiuix/responsive/interfaces/IResponsive;->dispatchResponsiveLayout(Landroid/content/res/Configuration;Lmiuix/responsive/map/ScreenSpec;Z)V

    goto :goto_0

    :cond_2
    iget-object p1, p0, Lmiuix/responsive/page/manager/BaseResponseStateManager;->mViewResponsives:Landroid/util/ArrayMap;

    invoke-virtual {p1}, Landroid/util/ArrayMap;->keySet()Ljava/util/Set;

    move-result-object p1

    invoke-interface {p1}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object p1

    invoke-interface {p1}, Ljava/util/Iterator;->hasNext()Z

    move-result p2

    if-nez p2, :cond_3

    return-void

    :cond_3
    invoke-interface {p1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object p1

    check-cast p1, Ljava/lang/Integer;

    iget-object p2, p0, Lmiuix/responsive/page/manager/BaseResponseStateManager;->mViewResponsives:Landroid/util/ArrayMap;

    invoke-virtual {p2, p1}, Landroid/util/ArrayMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p2

    invoke-static {p2}, Landroidx/appcompat/app/ToolbarActionBar$$ExternalSyntheticThrowCCEIfNotNull0;->m(Ljava/lang/Object;)V

    iget-object p2, p0, Lmiuix/responsive/page/manager/BaseResponseStateManager;->mRootView:Landroid/view/View;

    invoke-virtual {p1}, Ljava/lang/Integer;->intValue()I

    move-result p3

    invoke-virtual {p2, p3}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object p2

    invoke-static {p2}, Landroidx/appcompat/app/ToolbarActionBar$$ExternalSyntheticThrowCCEIfNotNull0;->m(Ljava/lang/Object;)V

    iget-object p0, p0, Lmiuix/responsive/page/manager/BaseResponseStateManager;->mViewResponsives:Landroid/util/ArrayMap;

    const/4 p2, 0x0

    invoke-virtual {p0, p1, p2}, Landroid/util/ArrayMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    throw p2
.end method""",
        'replacement': """.method protected notifyResponseChange(Landroid/content/res/Configuration;Lmiuix/responsive/map/ResponsiveState;Z)V
    .registers 7

    goto :goto_14

    nop

    :goto_0
    iget-object p2, p0, Lmiuix/responsive/page/manager/BaseResponseStateManager;->mResponsiveMap:Landroid/util/ArrayMap;

    goto :goto_1f

    nop

    :goto_1
    invoke-virtual {p2, p1}, Landroid/util/ArrayMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p2

    goto :goto_1a

    nop

    :goto_2
    invoke-virtual {p1}, Landroid/util/ArrayMap;->keySet()Ljava/util/Set;

    move-result-object p1

    goto :goto_29

    nop

    :goto_3
    throw p2

    :goto_4
    invoke-static {p2}, Landroidx/appcompat/app/ToolbarActionBar$$ExternalSyntheticThrowCCEIfNotNull0;->m(Ljava/lang/Object;)V

    goto :goto_f

    nop

    :goto_5
    return-void

    :goto_6
    goto :goto_d

    nop

    :goto_7
    invoke-interface {v1, p1, v0, p3}, Lmiuix/responsive/interfaces/IResponsive;->dispatchResponsiveLayout(Landroid/content/res/Configuration;Lmiuix/responsive/map/ScreenSpec;Z)V

    goto :goto_1c

    nop

    :goto_8
    invoke-interface {p2}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object p2

    :goto_9
    goto :goto_a

    nop

    :goto_a
    invoke-interface {p2}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    goto :goto_26

    nop

    :goto_b
    if-nez p2, :cond_0

    goto :goto_12

    :cond_0
    goto :goto_11

    nop

    :goto_c
    invoke-interface {p2, p1, v0, p3}, Lmiuix/responsive/interfaces/IResponsive;->dispatchResponsiveLayout(Landroid/content/res/Configuration;Lmiuix/responsive/map/ScreenSpec;Z)V

    goto :goto_0

    nop

    :goto_d
    invoke-interface {p1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object p1

    goto :goto_22

    nop

    :goto_e
    iget-object p2, p0, Lmiuix/responsive/page/manager/BaseResponseStateManager;->mPageInfo:Lmiuix/responsive/interfaces/IResponsive;

    goto :goto_c

    nop

    :goto_f
    iget-object p0, p0, Lmiuix/responsive/page/manager/BaseResponseStateManager;->mViewResponsives:Landroid/util/ArrayMap;

    goto :goto_13

    nop

    :goto_10
    check-cast v1, Lmiuix/responsive/interfaces/IResponsive;

    goto :goto_1b

    nop

    :goto_11
    invoke-virtual {p2, v0}, Lmiuix/responsive/map/ResponsiveState;->toScreenSpec(Lmiuix/responsive/map/ScreenSpec;)V

    :goto_12
    goto :goto_e

    nop

    :goto_13
    const/4 p2, 0x0

    goto :goto_23

    nop

    :goto_14
    new-instance v0, Lmiuix/responsive/map/ScreenSpec;

    goto :goto_25

    nop

    :goto_15
    check-cast v1, Landroid/view/View;

    goto :goto_27

    nop

    :goto_16
    iget-object p1, p0, Lmiuix/responsive/page/manager/BaseResponseStateManager;->mViewResponsives:Landroid/util/ArrayMap;

    goto :goto_2

    nop

    :goto_17
    iget-object p2, p0, Lmiuix/responsive/page/manager/BaseResponseStateManager;->mRootView:Landroid/view/View;

    goto :goto_24

    nop

    :goto_18
    invoke-interface {p1}, Ljava/util/Iterator;->hasNext()Z

    move-result p2

    goto :goto_21

    nop

    :goto_19
    iget-object p2, p0, Lmiuix/responsive/page/manager/BaseResponseStateManager;->mViewResponsives:Landroid/util/ArrayMap;

    goto :goto_1

    nop

    :goto_1a
    invoke-static {p2}, Landroidx/appcompat/app/ToolbarActionBar$$ExternalSyntheticThrowCCEIfNotNull0;->m(Ljava/lang/Object;)V

    goto :goto_17

    nop

    :goto_1b
    if-nez v1, :cond_1

    goto :goto_9

    :cond_1
    goto :goto_7

    nop

    :goto_1c
    goto :goto_9

    :goto_1d
    goto :goto_16

    nop

    :goto_1e
    invoke-interface {p2}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    goto :goto_15

    nop

    :goto_1f
    invoke-virtual {p2}, Landroid/util/ArrayMap;->keySet()Ljava/util/Set;

    move-result-object p2

    goto :goto_8

    nop

    :goto_20
    invoke-virtual {v2, v1}, Landroid/util/ArrayMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v1

    goto :goto_10

    nop

    :goto_21
    if-eqz p2, :cond_2

    goto :goto_6

    :cond_2
    goto :goto_5

    nop

    :goto_22
    check-cast p1, Ljava/lang/Integer;

    goto :goto_19

    nop

    :goto_23
    invoke-virtual {p0, p1, p2}, Landroid/util/ArrayMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_3

    nop

    :goto_24
    invoke-virtual {p1}, Ljava/lang/Integer;->intValue()I

    move-result p3

    goto :goto_28

    nop

    :goto_25
    invoke-direct {v0}, Lmiuix/responsive/map/ScreenSpec;-><init>()V

    goto :goto_b

    nop

    :goto_26
    if-nez v1, :cond_3

    goto :goto_1d

    :cond_3
    goto :goto_1e

    nop

    :goto_27
    iget-object v2, p0, Lmiuix/responsive/page/manager/BaseResponseStateManager;->mResponsiveMap:Landroid/util/ArrayMap;

    goto :goto_20

    nop

    :goto_28
    invoke-virtual {p2, p3}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object p2

    goto :goto_4

    nop

    :goto_29
    invoke-interface {p1}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object p1

    goto :goto_18

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_responsive_page_manager_BaseResponseStateManager__onDestroy',
        'method': '.method protected onDestroy()V',
        'method_name': 'onDestroy',
        'method_anchors': ['invoke-static {}, Lmiuix/responsive/map/ResponsiveStateManager;->getInstance()Lmiuix/responsive/map/ResponsiveStateManager;', 'invoke-virtual {p0}, Lmiuix/responsive/page/manager/BaseStateManager;->getContext()Landroid/content/Context;', 'invoke-virtual {v0, p0}, Lmiuix/responsive/map/ResponsiveStateManager;->remove(Landroid/content/Context;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onDestroy()V
    .registers 2

    invoke-static {}, Lmiuix/responsive/map/ResponsiveStateManager;->getInstance()Lmiuix/responsive/map/ResponsiveStateManager;

    move-result-object v0

    invoke-virtual {p0}, Lmiuix/responsive/page/manager/BaseStateManager;->getContext()Landroid/content/Context;

    move-result-object p0

    invoke-virtual {v0, p0}, Lmiuix/responsive/map/ResponsiveStateManager;->remove(Landroid/content/Context;)V

    return-void
.end method""",
        'replacement': """.method protected onDestroy()V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    invoke-virtual {v0, p0}, Lmiuix/responsive/map/ResponsiveStateManager;->remove(Landroid/content/Context;)V

    goto :goto_3

    nop

    :goto_1
    invoke-static {}, Lmiuix/responsive/map/ResponsiveStateManager;->getInstance()Lmiuix/responsive/map/ResponsiveStateManager;

    move-result-object v0

    goto :goto_2

    nop

    :goto_2
    invoke-virtual {p0}, Lmiuix/responsive/page/manager/BaseStateManager;->getContext()Landroid/content/Context;

    move-result-object p0

    goto :goto_0

    nop

    :goto_3
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
