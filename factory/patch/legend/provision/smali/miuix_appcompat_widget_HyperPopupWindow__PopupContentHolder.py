TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/widget/HyperPopupWindow$PopupContentHolder.smali'
CLASS_FALLBACK_NAMES = ['HyperPopupWindow$PopupContentHolder.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'miuix_appcompat_widget_HyperPopupWindow__PopupContentHolder__inflate',
        'method': '.method inflate()V',
        'method_name': 'inflate',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContentView:Lmiuix/smooth/SmoothFrameLayout2;', 'if-nez v0, :cond_2', 'iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContext:Landroid/content/Context;', 'invoke-static {v0}, Landroid/view/LayoutInflater;->from(Landroid/content/Context;)Landroid/view/LayoutInflater;', 'sget v1, Lmiuix/appcompat/R$layout;->miuix_appcompat_hyper_popup_list:I', 'invoke-virtual {v0, v1, v2}, Landroid/view/LayoutInflater;->inflate(ILandroid/view/ViewGroup;)Landroid/view/View;', 'check-cast v0, Lmiuix/smooth/SmoothFrameLayout2;', 'iput-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContentView:Lmiuix/smooth/SmoothFrameLayout2;'],
        'type': 'method_replace',
        'search': """.method inflate()V
    .registers 4

    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContentView:Lmiuix/smooth/SmoothFrameLayout2;

    if-nez v0, :cond_2

    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContext:Landroid/content/Context;

    invoke-static {v0}, Landroid/view/LayoutInflater;->from(Landroid/content/Context;)Landroid/view/LayoutInflater;

    move-result-object v0

    sget v1, Lmiuix/appcompat/R$layout;->miuix_appcompat_hyper_popup_list:I

    const/4 v2, 0x0

    invoke-virtual {v0, v1, v2}, Landroid/view/LayoutInflater;->inflate(ILandroid/view/ViewGroup;)Landroid/view/View;

    move-result-object v0

    check-cast v0, Lmiuix/smooth/SmoothFrameLayout2;

    iput-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContentView:Lmiuix/smooth/SmoothFrameLayout2;

    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContext:Landroid/content/Context;

    sget v1, Lmiuix/appcompat/R$attr;->immersionWindowBackground:I

    invoke-static {v0, v1}, Lmiuix/internal/util/AttributeResolver;->resolveDrawable(Landroid/content/Context;I)Landroid/graphics/drawable/Drawable;

    move-result-object v0

    instance-of v1, v0, Lmiuix/smooth/SmoothContainerDrawable2;

    if-eqz v1, :cond_0

    move-object v1, v0

    check-cast v1, Lmiuix/smooth/SmoothContainerDrawable2;

    iget-object v2, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-static {v2}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$2900(Lmiuix/appcompat/widget/HyperPopupWindow;)F

    move-result v2

    invoke-virtual {v1, v2}, Lmiuix/smooth/SmoothContainerDrawable2;->setCornerRadius(F)V

    :cond_0
    if-eqz v0, :cond_1

    iget-object v1, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContentView:Lmiuix/smooth/SmoothFrameLayout2;

    invoke-virtual {v1, v0}, Landroid/widget/FrameLayout;->setBackground(Landroid/graphics/drawable/Drawable;)V

    :cond_1
    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContentView:Lmiuix/smooth/SmoothFrameLayout2;

    sget v1, Lmiuix/appcompat/R$id;->spring_back:I

    invoke-virtual {v0, v1}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    iget-object v1, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContentView:Lmiuix/smooth/SmoothFrameLayout2;

    new-instance v2, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder$1;

    invoke-direct {v2, p0, v0}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder$1;-><init>(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;Landroid/view/View;)V

    invoke-virtual {v1, v2}, Landroid/widget/FrameLayout;->addOnLayoutChangeListener(Landroid/view/View$OnLayoutChangeListener;)V

    :cond_2
    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContentView:Lmiuix/smooth/SmoothFrameLayout2;

    const v1, 0x102000a

    invoke-virtual {v0, v1}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/ListView;

    iput-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mListView:Landroid/widget/ListView;

    if-eqz v0, :cond_3

    new-instance v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder$2;

    invoke-direct {v1, p0}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder$2;-><init>(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)V

    invoke-virtual {v0, v1}, Landroid/widget/ListView;->setOnTouchListener(Landroid/view/View$OnTouchListener;)V

    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mListView:Landroid/widget/ListView;

    new-instance v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder$$ExternalSyntheticLambda0;

    invoke-direct {v1, p0}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder$$ExternalSyntheticLambda0;-><init>(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)V

    invoke-virtual {v0, v1}, Landroid/widget/ListView;->setOnItemClickListener(Landroid/widget/AdapterView$OnItemClickListener;)V

    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mListView:Landroid/widget/ListView;

    iget-object p0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mAdapter:Landroid/widget/ListAdapter;

    invoke-virtual {v0, p0}, Landroid/widget/ListView;->setAdapter(Landroid/widget/ListAdapter;)V

    :cond_3
    return-void
.end method""",
        'replacement': """.method inflate()V
    .registers 4

    goto :goto_22

    nop

    :goto_0
    invoke-virtual {v1, v2}, Lmiuix/smooth/SmoothContainerDrawable2;->setCornerRadius(F)V

    :goto_1
    goto :goto_a

    nop

    :goto_2
    if-nez v0, :cond_0

    goto :goto_25

    :cond_0
    goto :goto_2f

    nop

    :goto_3
    iput-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mListView:Landroid/widget/ListView;

    goto :goto_2

    nop

    :goto_4
    invoke-direct {v1, p0}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder$2;-><init>(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)V

    goto :goto_c

    nop

    :goto_5
    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContext:Landroid/content/Context;

    goto :goto_6

    nop

    :goto_6
    invoke-static {v0}, Landroid/view/LayoutInflater;->from(Landroid/content/Context;)Landroid/view/LayoutInflater;

    move-result-object v0

    goto :goto_d

    nop

    :goto_7
    invoke-direct {v1, p0}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder$$ExternalSyntheticLambda0;-><init>(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)V

    goto :goto_1f

    nop

    :goto_8
    invoke-virtual {v1, v0}, Landroid/widget/FrameLayout;->setBackground(Landroid/graphics/drawable/Drawable;)V

    :goto_9
    goto :goto_1b

    nop

    :goto_a
    if-nez v0, :cond_1

    goto :goto_9

    :cond_1
    goto :goto_2c

    nop

    :goto_b
    if-nez v1, :cond_2

    goto :goto_1

    :cond_2
    goto :goto_13

    nop

    :goto_c
    invoke-virtual {v0, v1}, Landroid/widget/ListView;->setOnTouchListener(Landroid/view/View$OnTouchListener;)V

    goto :goto_f

    nop

    :goto_d
    sget v1, Lmiuix/appcompat/R$layout;->miuix_appcompat_hyper_popup_list:I

    goto :goto_10

    nop

    :goto_e
    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mListView:Landroid/widget/ListView;

    goto :goto_27

    nop

    :goto_f
    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mListView:Landroid/widget/ListView;

    goto :goto_28

    nop

    :goto_10
    const/4 v2, 0x0

    goto :goto_1d

    nop

    :goto_11
    invoke-virtual {v1, v2}, Landroid/widget/FrameLayout;->addOnLayoutChangeListener(Landroid/view/View$OnLayoutChangeListener;)V

    :goto_12
    goto :goto_26

    nop

    :goto_13
    move-object v1, v0

    goto :goto_29

    nop

    :goto_14
    invoke-direct {v2, p0, v0}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder$1;-><init>(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;Landroid/view/View;)V

    goto :goto_11

    nop

    :goto_15
    iget-object v1, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContentView:Lmiuix/smooth/SmoothFrameLayout2;

    goto :goto_31

    nop

    :goto_16
    check-cast v0, Landroid/widget/ListView;

    goto :goto_3

    nop

    :goto_17
    if-eqz v0, :cond_3

    goto :goto_12

    :cond_3
    goto :goto_5

    nop

    :goto_18
    iget-object v2, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_1c

    nop

    :goto_19
    sget v1, Lmiuix/appcompat/R$attr;->immersionWindowBackground:I

    goto :goto_20

    nop

    :goto_1a
    invoke-virtual {v0, v1}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_15

    nop

    :goto_1b
    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContentView:Lmiuix/smooth/SmoothFrameLayout2;

    goto :goto_2e

    nop

    :goto_1c
    invoke-static {v2}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$2900(Lmiuix/appcompat/widget/HyperPopupWindow;)F

    move-result v2

    goto :goto_0

    nop

    :goto_1d
    invoke-virtual {v0, v1, v2}, Landroid/view/LayoutInflater;->inflate(ILandroid/view/ViewGroup;)Landroid/view/View;

    move-result-object v0

    goto :goto_1e

    nop

    :goto_1e
    check-cast v0, Lmiuix/smooth/SmoothFrameLayout2;

    goto :goto_2d

    nop

    :goto_1f
    invoke-virtual {v0, v1}, Landroid/widget/ListView;->setOnItemClickListener(Landroid/widget/AdapterView$OnItemClickListener;)V

    goto :goto_e

    nop

    :goto_20
    invoke-static {v0, v1}, Lmiuix/internal/util/AttributeResolver;->resolveDrawable(Landroid/content/Context;I)Landroid/graphics/drawable/Drawable;

    move-result-object v0

    goto :goto_2a

    nop

    :goto_21
    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContext:Landroid/content/Context;

    goto :goto_19

    nop

    :goto_22
    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContentView:Lmiuix/smooth/SmoothFrameLayout2;

    goto :goto_17

    nop

    :goto_23
    return-void

    :goto_24
    invoke-virtual {v0, p0}, Landroid/widget/ListView;->setAdapter(Landroid/widget/ListAdapter;)V

    :goto_25
    goto :goto_23

    nop

    :goto_26
    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContentView:Lmiuix/smooth/SmoothFrameLayout2;

    goto :goto_30

    nop

    :goto_27
    iget-object p0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mAdapter:Landroid/widget/ListAdapter;

    goto :goto_24

    nop

    :goto_28
    new-instance v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder$$ExternalSyntheticLambda0;

    goto :goto_7

    nop

    :goto_29
    check-cast v1, Lmiuix/smooth/SmoothContainerDrawable2;

    goto :goto_18

    nop

    :goto_2a
    instance-of v1, v0, Lmiuix/smooth/SmoothContainerDrawable2;

    goto :goto_b

    nop

    :goto_2b
    invoke-virtual {v0, v1}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_16

    nop

    :goto_2c
    iget-object v1, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContentView:Lmiuix/smooth/SmoothFrameLayout2;

    goto :goto_8

    nop

    :goto_2d
    iput-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContentView:Lmiuix/smooth/SmoothFrameLayout2;

    goto :goto_21

    nop

    :goto_2e
    sget v1, Lmiuix/appcompat/R$id;->spring_back:I

    goto :goto_1a

    nop

    :goto_2f
    new-instance v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder$2;

    goto :goto_4

    nop

    :goto_30
    const v1, 0x102000a

    goto :goto_2b

    nop

    :goto_31
    new-instance v2, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder$1;

    goto :goto_14

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_widget_HyperPopupWindow__PopupContentHolder__setMenuListAccessibilityDelegate',
        'method': '.method protected setMenuListAccessibilityDelegate()V',
        'method_name': 'setMenuListAccessibilityDelegate',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;', 'invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$100(Lmiuix/appcompat/widget/HyperPopupWindow;)Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;', 'if-eqz v0, :cond_1', 'iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mListView:Landroid/widget/ListView;', 'if-nez v0, :cond_0', 'new-instance v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder$4;', 'invoke-direct {v1, p0}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder$4;-><init>(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)V', 'invoke-static {v0, v1}, Landroidx/core/view/ViewCompat;->setAccessibilityDelegate(Landroid/view/View;Landroidx/core/view/AccessibilityDelegateCompat;)V'],
        'type': 'method_replace',
        'search': """.method protected setMenuListAccessibilityDelegate()V
    .registers 3

    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$100(Lmiuix/appcompat/widget/HyperPopupWindow;)Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    move-result-object v0

    if-eqz v0, :cond_1

    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mListView:Landroid/widget/ListView;

    if-nez v0, :cond_0

    goto :goto_0

    :cond_0
    new-instance v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder$4;

    invoke-direct {v1, p0}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder$4;-><init>(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)V

    invoke-static {v0, v1}, Landroidx/core/view/ViewCompat;->setAccessibilityDelegate(Landroid/view/View;Landroidx/core/view/AccessibilityDelegateCompat;)V

    :cond_1
    :goto_0
    return-void
.end method""",
        'replacement': """.method protected setMenuListAccessibilityDelegate()V
    .registers 3

    goto :goto_b

    nop

    :goto_0
    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mListView:Landroid/widget/ListView;

    goto :goto_3

    nop

    :goto_1
    invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$100(Lmiuix/appcompat/widget/HyperPopupWindow;)Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    move-result-object v0

    goto :goto_8

    nop

    :goto_2
    new-instance v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder$4;

    goto :goto_a

    nop

    :goto_3
    if-eqz v0, :cond_0

    goto :goto_7

    :cond_0
    goto :goto_6

    nop

    :goto_4
    invoke-static {v0, v1}, Landroidx/core/view/ViewCompat;->setAccessibilityDelegate(Landroid/view/View;Landroidx/core/view/AccessibilityDelegateCompat;)V

    :goto_5
    goto :goto_9

    nop

    :goto_6
    goto :goto_5

    :goto_7
    goto :goto_2

    nop

    :goto_8
    if-nez v0, :cond_1

    goto :goto_5

    :cond_1
    goto :goto_0

    nop

    :goto_9
    return-void

    :goto_a
    invoke-direct {v1, p0}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder$4;-><init>(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)V

    goto :goto_4

    nop

    :goto_b
    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_widget_HyperPopupWindow__PopupContentHolder__setMinWidth',
        'method': '.method protected setMinWidth(I)V',
        'method_name': 'setMinWidth',
        'method_anchors': ['iput p1, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mMinWidth:I', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected setMinWidth(I)V
    .registers 2

    iput p1, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mMinWidth:I

    return-void
.end method""",
        'replacement': """.method protected setMinWidth(I)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    iput p1, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mMinWidth:I

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_widget_HyperPopupWindow__PopupContentHolder__setAdapter',
        'method': '.method setAdapter(Landroid/widget/ListAdapter;)V',
        'method_name': 'setAdapter',
        'method_anchors': ['iput-object p1, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mAdapter:Landroid/widget/ListAdapter;', 'return-void'],
        'type': 'method_replace',
        'search': """.method setAdapter(Landroid/widget/ListAdapter;)V
    .registers 2

    iput-object p1, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mAdapter:Landroid/widget/ListAdapter;

    return-void
.end method""",
        'replacement': """.method setAdapter(Landroid/widget/ListAdapter;)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    iput-object p1, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mAdapter:Landroid/widget/ListAdapter;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_widget_HyperPopupWindow__PopupContentHolder__setItemClickListener',
        'method': '.method setItemClickListener(Landroid/widget/AdapterView$OnItemClickListener;)V',
        'method_name': 'setItemClickListener',
        'method_anchors': ['iput-object p1, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mOnItemClickListener:Landroid/widget/AdapterView$OnItemClickListener;', 'return-void'],
        'type': 'method_replace',
        'search': """.method setItemClickListener(Landroid/widget/AdapterView$OnItemClickListener;)V
    .registers 2

    iput-object p1, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mOnItemClickListener:Landroid/widget/AdapterView$OnItemClickListener;

    return-void
.end method""",
        'replacement': """.method setItemClickListener(Landroid/widget/AdapterView$OnItemClickListener;)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    iput-object p1, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mOnItemClickListener:Landroid/widget/AdapterView$OnItemClickListener;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_widget_HyperPopupWindow__PopupContentHolder__show',
        'method': '.method show(Landroid/view/View;Landroid/view/ViewGroup;Landroid/graphics/Rect;Z)Z',
        'method_name': 'show',
        'method_anchors': ['iget-object v3, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;', 'iget-object v8, v3, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mAnchorViewBounds:Landroid/graphics/Rect;', 'if-eqz p4, :cond_0', 'iget v2, v8, Landroid/graphics/Rect;->left:I', 'iget-object v4, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;', 'invoke-static {v4}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$3000(Lmiuix/appcompat/widget/HyperPopupWindow;)I', 'iput v2, v8, Landroid/graphics/Rect;->left:I', 'iget v2, v8, Landroid/graphics/Rect;->top:I'],
        'type': 'method_replace',
        'search': """.method show(Landroid/view/View;Landroid/view/ViewGroup;Landroid/graphics/Rect;Z)Z
    .registers 27

    move-object/from16 v1, p0

    move-object/from16 v0, p3

    iget-object v3, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    iget-object v8, v3, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mAnchorViewBounds:Landroid/graphics/Rect;

    if-eqz p4, :cond_0

    iget v2, v8, Landroid/graphics/Rect;->left:I

    iget-object v4, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-static {v4}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$3000(Lmiuix/appcompat/widget/HyperPopupWindow;)I

    move-result v4

    sub-int/2addr v2, v4

    iput v2, v8, Landroid/graphics/Rect;->left:I

    iget v2, v8, Landroid/graphics/Rect;->top:I

    iget-object v4, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-static {v4}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$3000(Lmiuix/appcompat/widget/HyperPopupWindow;)I

    move-result v4

    sub-int/2addr v2, v4

    iput v2, v8, Landroid/graphics/Rect;->top:I

    iget v2, v8, Landroid/graphics/Rect;->right:I

    iget-object v4, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-static {v4}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$3000(Lmiuix/appcompat/widget/HyperPopupWindow;)I

    move-result v4

    sub-int/2addr v2, v4

    iput v2, v8, Landroid/graphics/Rect;->right:I

    iget v2, v8, Landroid/graphics/Rect;->bottom:I

    iget-object v4, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-static {v4}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$3000(Lmiuix/appcompat/widget/HyperPopupWindow;)I

    move-result v4

    sub-int/2addr v2, v4

    iput v2, v8, Landroid/graphics/Rect;->bottom:I

    :cond_0
    iget-object v2, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mAdapter:Landroid/widget/ListAdapter;

    iget-object v4, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mListView:Landroid/widget/ListView;

    iget-object v5, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContext:Landroid/content/Context;

    iget v6, v3, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mMaxWidth:I

    iget v7, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mMinWidth:I

    invoke-static {v2, v4, v5, v6, v7}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$3100(Landroid/widget/ListAdapter;Landroid/view/ViewGroup;Landroid/content/Context;II)[[I

    move-result-object v2

    iput-object v2, v3, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mItemViewBounds:[[I

    iget-object v2, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mPopupWindowStrategy:Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;

    invoke-interface {v2, v3}, Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;->measureContentSize(Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;)V

    iget-object v2, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mPopupWindowStrategy:Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;

    invoke-interface {v2, v3}, Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;->getXInWindow(Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;)I

    move-result v4

    iget-object v2, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mPopupWindowStrategy:Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;

    invoke-interface {v2, v3}, Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;->getYInWindow(Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;)I

    move-result v5

    iget v6, v3, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mFinalPopupWidth:I

    iget v7, v3, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mFinalPopupHeight:I

    iget-object v2, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mBoundsRect:Landroid/graphics/Rect;

    add-int v9, v4, v6

    add-int v10, v5, v7

    invoke-virtual {v2, v4, v5, v9, v10}, Landroid/graphics/Rect;->set(IIII)V

    iget-object v2, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-static {v2}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$3200(Lmiuix/appcompat/widget/HyperPopupWindow;)Z

    move-result v2

    if-eqz v2, :cond_1

    iget-object v2, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-static/range {v2 .. v7}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$3300(Lmiuix/appcompat/widget/HyperPopupWindow;Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;IIII)V

    :cond_1
    if-nez p4, :cond_5

    iget-object v3, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContentView:Lmiuix/smooth/SmoothFrameLayout2;

    div-int/lit8 v9, v9, 0x2

    invoke-virtual {v8}, Landroid/graphics/Rect;->centerX()I

    move-result v10

    const/4 v11, 0x0

    if-le v9, v10, :cond_2

    move v9, v11

    goto :goto_0

    :cond_2
    int-to-float v9, v6

    :goto_0
    invoke-virtual {v3, v9}, Landroid/widget/FrameLayout;->setPivotX(F)V

    iget-object v3, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContentView:Lmiuix/smooth/SmoothFrameLayout2;

    iget v8, v8, Landroid/graphics/Rect;->top:I

    if-le v5, v8, :cond_3

    goto :goto_1

    :cond_3
    int-to-float v11, v7

    :goto_1
    invoke-virtual {v3, v11}, Landroid/widget/FrameLayout;->setPivotY(F)V

    new-instance v3, Landroid/widget/FrameLayout$LayoutParams;

    invoke-direct {v3, v6, v7}, Landroid/widget/FrameLayout$LayoutParams;-><init>(II)V

    iget-object v6, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-static {v6}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$3200(Lmiuix/appcompat/widget/HyperPopupWindow;)Z

    move-result v6

    if-eqz v6, :cond_4

    iget v6, v0, Landroid/graphics/Rect;->left:I

    sub-int/2addr v4, v6

    iput v4, v3, Landroid/widget/FrameLayout$LayoutParams;->leftMargin:I

    iget v0, v0, Landroid/graphics/Rect;->top:I

    sub-int/2addr v5, v0

    iput v5, v3, Landroid/widget/FrameLayout$LayoutParams;->topMargin:I

    :cond_4
    iget-object v0, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContentView:Lmiuix/smooth/SmoothFrameLayout2;

    invoke-virtual {v0, v3}, Landroid/widget/FrameLayout;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    iget-object v0, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$800(Lmiuix/appcompat/widget/HyperPopupWindow;)Landroid/view/ViewGroup;

    move-result-object v3

    iget-object v1, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContentView:Lmiuix/smooth/SmoothFrameLayout2;

    invoke-static {v0, v3, v1}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$3400(Lmiuix/appcompat/widget/HyperPopupWindow;Landroid/view/ViewGroup;Landroid/view/View;)V

    const/16 v20, 0x1

    goto :goto_2

    :cond_5
    iget-object v3, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-static {v3}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$100(Lmiuix/appcompat/widget/HyperPopupWindow;)Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    move-result-object v3

    iget-object v3, v3, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mBoundsRect:Landroid/graphics/Rect;

    iget-object v7, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mBoundsRect:Landroid/graphics/Rect;

    invoke-static {v3, v7}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$3500(Landroid/graphics/Rect;Landroid/graphics/Rect;)Landroid/graphics/Rect;

    move-result-object v7

    iget-object v11, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    new-instance v12, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;

    iget-object v13, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    iget-object v14, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContext:Landroid/content/Context;

    invoke-direct {v12, v13, v14}, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;-><init>(Lmiuix/appcompat/widget/HyperPopupWindow;Landroid/content/Context;)V

    invoke-static {v11, v12}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$2302(Lmiuix/appcompat/widget/HyperPopupWindow;Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;)Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;

    iget-object v11, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-static {v11}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$2300(Lmiuix/appcompat/widget/HyperPopupWindow;)Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;

    move-result-object v11

    const/4 v12, 0x0

    invoke-virtual {v11, v12}, Landroid/widget/FrameLayout;->setBackgroundColor(I)V

    iget-object v11, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-static {v11}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$2300(Lmiuix/appcompat/widget/HyperPopupWindow;)Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;

    move-result-object v11

    iget-object v13, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-static {v13}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$2900(Lmiuix/appcompat/widget/HyperPopupWindow;)F

    move-result v13

    invoke-virtual {v11, v13}, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;->setRadius(F)V

    iget-object v11, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-static {v11}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$2300(Lmiuix/appcompat/widget/HyperPopupWindow;)Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;

    move-result-object v11

    iget-object v13, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-static {v13}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$3600(Lmiuix/appcompat/widget/HyperPopupWindow;)I

    move-result v13

    iget-object v14, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-static {v14}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$3700(Lmiuix/appcompat/widget/HyperPopupWindow;)I

    move-result v14

    mul-int/lit8 v14, v14, 0x2

    add-int/2addr v13, v14

    int-to-float v13, v13

    invoke-virtual {v11, v13}, Landroid/widget/FrameLayout;->setElevation(F)V

    iget v11, v3, Landroid/graphics/Rect;->left:I

    iget v13, v7, Landroid/graphics/Rect;->left:I

    sub-int/2addr v11, v13

    iget v13, v3, Landroid/graphics/Rect;->top:I

    iget v14, v7, Landroid/graphics/Rect;->top:I

    sub-int/2addr v13, v14

    invoke-virtual {v3}, Landroid/graphics/Rect;->width()I

    move-result v14

    add-int/2addr v14, v11

    invoke-virtual {v3}, Landroid/graphics/Rect;->height()I

    move-result v3

    add-int/2addr v3, v13

    move v15, v9

    invoke-virtual {v7}, Landroid/graphics/Rect;->width()I

    move-result v9

    invoke-virtual {v7}, Landroid/graphics/Rect;->height()I

    move-result v16

    iget-object v2, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-static {v2}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$2300(Lmiuix/appcompat/widget/HyperPopupWindow;)Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;

    move-result-object v2

    invoke-virtual {v2, v11, v13, v14, v3}, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;->setClipBounds(IIII)V

    iget-object v2, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-static {v2}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$2300(Lmiuix/appcompat/widget/HyperPopupWindow;)Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;

    move-result-object v2

    invoke-virtual {v2}, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;->refreshClipPath()V

    new-instance v2, Landroid/widget/FrameLayout$LayoutParams;

    invoke-virtual {v7}, Landroid/graphics/Rect;->width()I

    move-result v12

    move/from16 v18, v3

    invoke-virtual {v7}, Landroid/graphics/Rect;->height()I

    move-result v3

    invoke-direct {v2, v12, v3}, Landroid/widget/FrameLayout$LayoutParams;-><init>(II)V

    iget v3, v7, Landroid/graphics/Rect;->left:I

    iget v12, v0, Landroid/graphics/Rect;->left:I

    sub-int/2addr v3, v12

    iput v3, v2, Landroid/widget/FrameLayout$LayoutParams;->leftMargin:I

    iget v3, v7, Landroid/graphics/Rect;->top:I

    iget v0, v0, Landroid/graphics/Rect;->top:I

    sub-int/2addr v3, v0

    iput v3, v2, Landroid/widget/FrameLayout$LayoutParams;->topMargin:I

    iget-object v0, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$2300(Lmiuix/appcompat/widget/HyperPopupWindow;)Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;

    move-result-object v0

    invoke-virtual {v0, v2}, Landroid/widget/FrameLayout;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    iget-object v0, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$2300(Lmiuix/appcompat/widget/HyperPopupWindow;)Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;

    move-result-object v0

    move-object/from16 v2, p2

    invoke-virtual {v2, v0}, Landroid/view/ViewGroup;->addView(Landroid/view/View;)V

    iget v0, v8, Landroid/graphics/Rect;->left:I

    iget v2, v7, Landroid/graphics/Rect;->left:I

    sub-int v12, v0, v2

    iget v0, v8, Landroid/graphics/Rect;->top:I

    iget v3, v7, Landroid/graphics/Rect;->top:I

    sub-int/2addr v0, v3

    move/from16 v19, v2

    iget v2, v8, Landroid/graphics/Rect;->right:I

    sub-int v2, v2, v19

    move/from16 p2, v3

    iget v3, v8, Landroid/graphics/Rect;->bottom:I

    sub-int v3, v3, p2

    sub-int v4, v4, v19

    sub-int v5, v5, p2

    sub-int v15, v15, v19

    sub-int v19, v10, p2

    new-instance v10, Landroid/widget/FrameLayout$LayoutParams;

    move/from16 p2, v4

    sub-int v4, v15, p2

    move/from16 p3, v5

    sub-int v5, v19, p3

    invoke-direct {v10, v4, v5}, Landroid/widget/FrameLayout$LayoutParams;-><init>(II)V

    iget-object v4, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContentView:Lmiuix/smooth/SmoothFrameLayout2;

    invoke-virtual {v4, v10}, Landroid/widget/FrameLayout;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    new-instance v4, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;

    iget-object v5, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    iget-object v10, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContext:Landroid/content/Context;

    invoke-direct {v4, v5, v10}, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;-><init>(Lmiuix/appcompat/widget/HyperPopupWindow;Landroid/content/Context;)V

    new-instance v5, Landroid/widget/FrameLayout$LayoutParams;

    invoke-virtual {v7}, Landroid/graphics/Rect;->width()I

    move-result v10

    invoke-virtual {v7}, Landroid/graphics/Rect;->height()I

    move-result v7

    invoke-direct {v5, v10, v7}, Landroid/widget/FrameLayout$LayoutParams;-><init>(II)V

    invoke-virtual {v4, v5}, Landroid/widget/FrameLayout;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    const/4 v5, 0x0

    invoke-virtual {v4, v5}, Landroid/widget/FrameLayout;->setBackgroundColor(I)V

    invoke-virtual {v4, v12, v0, v2, v3}, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;->setClipBounds(IIII)V

    invoke-virtual {v4}, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;->refreshClipPath()V

    iget-object v5, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContentView:Lmiuix/smooth/SmoothFrameLayout2;

    invoke-virtual {v4, v5}, Landroid/widget/FrameLayout;->addView(Landroid/view/View;)V

    iget-object v5, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-static {v5}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$2300(Lmiuix/appcompat/widget/HyperPopupWindow;)Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;

    move-result-object v5

    invoke-virtual {v5, v4}, Landroid/widget/FrameLayout;->addView(Landroid/view/View;)V

    iget-object v5, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-static {v5, v4}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$2402(Lmiuix/appcompat/widget/HyperPopupWindow;Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;)Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;

    new-instance v4, Lmiuix/appcompat/widget/HyperPopupWindow$ViewBounds;

    iget-object v5, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContentView:Lmiuix/smooth/SmoothFrameLayout2;

    invoke-direct {v4, v5}, Lmiuix/appcompat/widget/HyperPopupWindow$ViewBounds;-><init>(Landroid/view/View;)V

    iput-object v4, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mViewBounds:Lmiuix/appcompat/widget/HyperPopupWindow$ViewBounds;

    invoke-virtual {v4, v6}, Lmiuix/appcompat/widget/HyperPopupWindow$ViewBounds;->setMeasureWidth(I)V

    iget-object v4, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-static {v4}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$100(Lmiuix/appcompat/widget/HyperPopupWindow;)Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    move-result-object v4

    const/4 v5, 0x1

    iput-boolean v5, v4, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mIsInAnimation:Z

    iget-object v4, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-static {v4}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$400(Lmiuix/appcompat/widget/HyperPopupWindow;)Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    move-result-object v4

    iput-boolean v5, v4, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mIsInAnimation:Z

    iget-object v4, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContentView:Lmiuix/smooth/SmoothFrameLayout2;

    invoke-virtual {v4}, Landroid/widget/FrameLayout;->getViewTreeObserver()Landroid/view/ViewTreeObserver;

    move-result-object v4

    move-object v6, v4

    move v4, v11

    move/from16 v11, v16

    move/from16 v16, v2

    move-object v2, v8

    move v8, v14

    move v14, v0

    new-instance v0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder$3;

    move/from16 v17, v5

    const/4 v5, 0x0

    const/4 v7, 0x0

    move-object/from16 v21, v6

    move v6, v13

    move/from16 v20, v17

    move/from16 v10, v18

    move/from16 v13, p2

    move/from16 v18, v3

    move/from16 v17, v15

    move-object/from16 v3, p1

    move/from16 v15, p3

    invoke-direct/range {v0 .. v19}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder$3;-><init>(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;Landroid/graphics/Rect;Landroid/view/View;IIIIIIIIIIIIIIII)V

    move-object/from16 v6, v21

    invoke-virtual {v6, v0}, Landroid/view/ViewTreeObserver;->addOnPreDrawListener(Landroid/view/ViewTreeObserver$OnPreDrawListener;)V

    :goto_2
    return v20
.end method""",
        'replacement': """.method show(Landroid/view/View;Landroid/view/ViewGroup;Landroid/graphics/Rect;Z)Z
    .registers 27

    goto :goto_9c

    nop

    :goto_0
    iput-boolean v5, v4, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mIsInAnimation:Z

    goto :goto_75

    nop

    :goto_1
    iput v2, v8, Landroid/graphics/Rect;->bottom:I

    :goto_2
    goto :goto_e6

    nop

    :goto_3
    invoke-static {v11}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$2300(Lmiuix/appcompat/widget/HyperPopupWindow;)Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;

    move-result-object v11

    goto :goto_ad

    nop

    :goto_4
    invoke-interface {v2, v3}, Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;->getXInWindow(Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;)I

    move-result v4

    goto :goto_eb

    nop

    :goto_5
    iget-object v4, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_da

    nop

    :goto_6
    iget-object v0, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_8

    nop

    :goto_7
    invoke-virtual {v4, v10}, Landroid/widget/FrameLayout;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    goto :goto_61

    nop

    :goto_8
    invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$2300(Lmiuix/appcompat/widget/HyperPopupWindow;)Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;

    move-result-object v0

    goto :goto_c9

    nop

    :goto_9
    invoke-virtual {v4, v5}, Landroid/widget/FrameLayout;->setBackgroundColor(I)V

    goto :goto_89

    nop

    :goto_a
    sub-int/2addr v2, v4

    goto :goto_29

    nop

    :goto_b
    add-int v9, v4, v6

    goto :goto_74

    nop

    :goto_c
    iget-object v5, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_36

    nop

    :goto_d
    iput v4, v3, Landroid/widget/FrameLayout$LayoutParams;->leftMargin:I

    goto :goto_6e

    nop

    :goto_e
    invoke-static {v11, v12}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$2302(Lmiuix/appcompat/widget/HyperPopupWindow;Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;)Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;

    goto :goto_f

    nop

    :goto_f
    iget-object v11, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_4a

    nop

    :goto_10
    iget v12, v0, Landroid/graphics/Rect;->left:I

    goto :goto_bc

    nop

    :goto_11
    move v8, v14

    goto :goto_52

    nop

    :goto_12
    iput v2, v8, Landroid/graphics/Rect;->left:I

    goto :goto_24

    nop

    :goto_13
    move v9, v11

    goto :goto_63

    nop

    :goto_14
    sub-int/2addr v13, v14

    goto :goto_c2

    nop

    :goto_15
    new-instance v0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder$3;

    goto :goto_ca

    nop

    :goto_16
    iput-object v2, v3, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mItemViewBounds:[[I

    goto :goto_c8

    nop

    :goto_17
    sub-int v4, v15, p2

    goto :goto_a0

    nop

    :goto_18
    iget-object v13, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_56

    nop

    :goto_19
    move/from16 v18, v3

    goto :goto_a8

    nop

    :goto_1a
    invoke-interface {v2, v3}, Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;->measureContentSize(Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;)V

    goto :goto_92

    nop

    :goto_1b
    iget-object v0, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_f2

    nop

    :goto_1c
    invoke-virtual {v4}, Landroid/widget/FrameLayout;->getViewTreeObserver()Landroid/view/ViewTreeObserver;

    move-result-object v4

    goto :goto_40

    nop

    :goto_1d
    invoke-direct {v12, v13, v14}, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;-><init>(Lmiuix/appcompat/widget/HyperPopupWindow;Landroid/content/Context;)V

    goto :goto_e

    nop

    :goto_1e
    iget v2, v8, Landroid/graphics/Rect;->left:I

    goto :goto_df

    nop

    :goto_1f
    return v20

    :goto_20
    sub-int/2addr v4, v6

    goto :goto_d

    nop

    :goto_21
    invoke-direct {v3, v6, v7}, Landroid/widget/FrameLayout$LayoutParams;-><init>(II)V

    goto :goto_71

    nop

    :goto_22
    mul-int/lit8 v14, v14, 0x2

    goto :goto_62

    nop

    :goto_23
    invoke-direct {v4, v5}, Lmiuix/appcompat/widget/HyperPopupWindow$ViewBounds;-><init>(Landroid/view/View;)V

    goto :goto_ce

    nop

    :goto_24
    iget v2, v8, Landroid/graphics/Rect;->top:I

    goto :goto_91

    nop

    :goto_25
    sub-int v19, v10, p2

    goto :goto_3e

    nop

    :goto_26
    invoke-interface {v2, v3}, Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;->getYInWindow(Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;)I

    move-result v5

    goto :goto_60

    nop

    :goto_27
    iget-object v4, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContentView:Lmiuix/smooth/SmoothFrameLayout2;

    goto :goto_7

    nop

    :goto_28
    new-instance v3, Landroid/widget/FrameLayout$LayoutParams;

    goto :goto_21

    nop

    :goto_29
    iput v2, v8, Landroid/graphics/Rect;->top:I

    goto :goto_d1

    nop

    :goto_2a
    iget v7, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mMinWidth:I

    goto :goto_a9

    nop

    :goto_2b
    invoke-virtual {v0, v3}, Landroid/widget/FrameLayout;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    goto :goto_2e

    nop

    :goto_2c
    sub-int/2addr v3, v0

    goto :goto_48

    nop

    :goto_2d
    iget-object v4, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_55

    nop

    :goto_2e
    iget-object v0, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_d7

    nop

    :goto_2f
    iget-object v3, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContentView:Lmiuix/smooth/SmoothFrameLayout2;

    goto :goto_d6

    nop

    :goto_30
    invoke-virtual {v8}, Landroid/graphics/Rect;->centerX()I

    move-result v10

    goto :goto_d9

    nop

    :goto_31
    sub-int/2addr v2, v4

    goto :goto_1

    nop

    :goto_32
    invoke-static/range {v2 .. v7}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$3300(Lmiuix/appcompat/widget/HyperPopupWindow;Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;IIII)V

    :goto_33
    goto :goto_38

    nop

    :goto_34
    if-gt v9, v10, :cond_0

    goto :goto_64

    :cond_0
    goto :goto_13

    nop

    :goto_35
    sub-int/2addr v5, v0

    goto :goto_93

    nop

    :goto_36
    invoke-static {v5}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$2300(Lmiuix/appcompat/widget/HyperPopupWindow;)Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;

    move-result-object v5

    goto :goto_c3

    nop

    :goto_37
    invoke-virtual {v3, v11}, Landroid/widget/FrameLayout;->setPivotY(F)V

    goto :goto_28

    nop

    :goto_38
    if-eqz p4, :cond_1

    goto :goto_7a

    :cond_1
    goto :goto_2f

    nop

    :goto_39
    invoke-static {v13}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$3600(Lmiuix/appcompat/widget/HyperPopupWindow;)I

    move-result v13

    goto :goto_8e

    nop

    :goto_3a
    move/from16 p2, v4

    goto :goto_17

    nop

    :goto_3b
    invoke-direct {v5, v10, v7}, Landroid/widget/FrameLayout$LayoutParams;-><init>(II)V

    goto :goto_96

    nop

    :goto_3c
    move/from16 p2, v3

    goto :goto_99

    nop

    :goto_3d
    iget v11, v3, Landroid/graphics/Rect;->left:I

    goto :goto_57

    nop

    :goto_3e
    new-instance v10, Landroid/widget/FrameLayout$LayoutParams;

    goto :goto_3a

    nop

    :goto_3f
    invoke-virtual {v2}, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;->refreshClipPath()V

    goto :goto_e7

    nop

    :goto_40
    move-object v6, v4

    goto :goto_9e

    nop

    :goto_41
    iget-object v2, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mBoundsRect:Landroid/graphics/Rect;

    goto :goto_b

    nop

    :goto_42
    invoke-direct {v2, v12, v3}, Landroid/widget/FrameLayout$LayoutParams;-><init>(II)V

    goto :goto_50

    nop

    :goto_43
    int-to-float v9, v6

    :goto_44
    goto :goto_5e

    nop

    :goto_45
    iget v13, v3, Landroid/graphics/Rect;->top:I

    goto :goto_97

    nop

    :goto_46
    iget-object v10, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContext:Landroid/content/Context;

    goto :goto_8f

    nop

    :goto_47
    iget v0, v8, Landroid/graphics/Rect;->top:I

    goto :goto_a3

    nop

    :goto_48
    iput v3, v2, Landroid/widget/FrameLayout$LayoutParams;->topMargin:I

    goto :goto_1b

    nop

    :goto_49
    invoke-virtual {v7}, Landroid/graphics/Rect;->height()I

    move-result v7

    goto :goto_3b

    nop

    :goto_4a
    invoke-static {v11}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$2300(Lmiuix/appcompat/widget/HyperPopupWindow;)Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;

    move-result-object v11

    goto :goto_c0

    nop

    :goto_4b
    if-gt v5, v8, :cond_2

    goto :goto_d5

    :cond_2
    goto :goto_d4

    nop

    :goto_4c
    add-int/2addr v14, v11

    goto :goto_e8

    nop

    :goto_4d
    iget-object v7, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mBoundsRect:Landroid/graphics/Rect;

    goto :goto_d0

    nop

    :goto_4e
    iget-object v2, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_b4

    nop

    :goto_4f
    iget-object v11, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_6f

    nop

    :goto_50
    iget v3, v7, Landroid/graphics/Rect;->left:I

    goto :goto_10

    nop

    :goto_51
    if-nez v6, :cond_3

    goto :goto_94

    :cond_3
    goto :goto_67

    nop

    :goto_52
    move v14, v0

    goto :goto_15

    nop

    :goto_53
    add-int/2addr v3, v13

    goto :goto_6c

    nop

    :goto_54
    iget-object v3, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_b2

    nop

    :goto_55
    invoke-static {v4}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$3000(Lmiuix/appcompat/widget/HyperPopupWindow;)I

    move-result v4

    goto :goto_8a

    nop

    :goto_56
    iget-object v14, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContext:Landroid/content/Context;

    goto :goto_1d

    nop

    :goto_57
    iget v13, v7, Landroid/graphics/Rect;->left:I

    goto :goto_7d

    nop

    :goto_58
    invoke-static {v0, v3, v1}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$3400(Lmiuix/appcompat/widget/HyperPopupWindow;Landroid/view/ViewGroup;Landroid/view/View;)V

    goto :goto_de

    nop

    :goto_59
    move v6, v13

    goto :goto_9d

    nop

    :goto_5a
    iget v6, v3, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mMaxWidth:I

    goto :goto_2a

    nop

    :goto_5b
    iget-object v4, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_a5

    nop

    :goto_5c
    iget-object v8, v3, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mAnchorViewBounds:Landroid/graphics/Rect;

    goto :goto_bd

    nop

    :goto_5d
    invoke-static {v4}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$100(Lmiuix/appcompat/widget/HyperPopupWindow;)Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    move-result-object v4

    goto :goto_b8

    nop

    :goto_5e
    invoke-virtual {v3, v9}, Landroid/widget/FrameLayout;->setPivotX(F)V

    goto :goto_a7

    nop

    :goto_5f
    iget-object v5, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContext:Landroid/content/Context;

    goto :goto_5a

    nop

    :goto_60
    iget v6, v3, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mFinalPopupWidth:I

    goto :goto_ab

    nop

    :goto_61
    new-instance v4, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;

    goto :goto_ea

    nop

    :goto_62
    add-int/2addr v13, v14

    goto :goto_9a

    nop

    :goto_63
    goto :goto_44

    :goto_64
    goto :goto_43

    nop

    :goto_65
    iget-object v0, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContentView:Lmiuix/smooth/SmoothFrameLayout2;

    goto :goto_2b

    nop

    :goto_66
    move/from16 v10, v18

    goto :goto_b7

    nop

    :goto_67
    iget v6, v0, Landroid/graphics/Rect;->left:I

    goto :goto_20

    nop

    :goto_68
    sub-int v12, v0, v2

    goto :goto_47

    nop

    :goto_69
    iget-object v3, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    goto :goto_5c

    nop

    :goto_6a
    invoke-virtual {v2, v4, v5, v9, v10}, Landroid/graphics/Rect;->set(IIII)V

    goto :goto_c6

    nop

    :goto_6b
    iget-object v5, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_70

    nop

    :goto_6c
    move v15, v9

    goto :goto_e9

    nop

    :goto_6d
    iget v3, v7, Landroid/graphics/Rect;->top:I

    goto :goto_b1

    nop

    :goto_6e
    iget v0, v0, Landroid/graphics/Rect;->top:I

    goto :goto_35

    nop

    :goto_6f
    new-instance v12, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;

    goto :goto_18

    nop

    :goto_70
    invoke-static {v5, v4}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$2402(Lmiuix/appcompat/widget/HyperPopupWindow;Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;)Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;

    goto :goto_a2

    nop

    :goto_71
    iget-object v6, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_ee

    nop

    :goto_72
    invoke-static {v2}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$2300(Lmiuix/appcompat/widget/HyperPopupWindow;)Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;

    move-result-object v2

    goto :goto_ec

    nop

    :goto_73
    move-object/from16 v0, p3

    goto :goto_69

    nop

    :goto_74
    add-int v10, v5, v7

    goto :goto_6a

    nop

    :goto_75
    iget-object v4, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContentView:Lmiuix/smooth/SmoothFrameLayout2;

    goto :goto_1c

    nop

    :goto_76
    iget v2, v8, Landroid/graphics/Rect;->right:I

    goto :goto_af

    nop

    :goto_77
    iget-object v13, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_39

    nop

    :goto_78
    iput v3, v2, Landroid/widget/FrameLayout$LayoutParams;->leftMargin:I

    goto :goto_6d

    nop

    :goto_79
    goto :goto_e3

    :goto_7a
    goto :goto_54

    nop

    :goto_7b
    const/4 v7, 0x0

    goto :goto_bb

    nop

    :goto_7c
    iget-object v11, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_3

    nop

    :goto_7d
    sub-int/2addr v11, v13

    goto :goto_45

    nop

    :goto_7e
    invoke-virtual {v11, v13}, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;->setRadius(F)V

    goto :goto_84

    nop

    :goto_7f
    iput-boolean v5, v4, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mIsInAnimation:Z

    goto :goto_5b

    nop

    :goto_80
    invoke-static {v4}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$3000(Lmiuix/appcompat/widget/HyperPopupWindow;)I

    move-result v4

    goto :goto_dd

    nop

    :goto_81
    iget-object v5, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContentView:Lmiuix/smooth/SmoothFrameLayout2;

    goto :goto_86

    nop

    :goto_82
    invoke-virtual {v7}, Landroid/graphics/Rect;->height()I

    move-result v16

    goto :goto_e5

    nop

    :goto_83
    invoke-virtual {v4}, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;->refreshClipPath()V

    goto :goto_81

    nop

    :goto_84
    iget-object v11, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_9b

    nop

    :goto_85
    invoke-direct/range {v0 .. v19}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder$3;-><init>(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;Landroid/graphics/Rect;Landroid/view/View;IIIIIIIIIIIIIIII)V

    goto :goto_f3

    nop

    :goto_86
    invoke-virtual {v4, v5}, Landroid/widget/FrameLayout;->addView(Landroid/view/View;)V

    goto :goto_c

    nop

    :goto_87
    iget-object v2, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_32

    nop

    :goto_88
    iget v0, v8, Landroid/graphics/Rect;->left:I

    goto :goto_9f

    nop

    :goto_89
    invoke-virtual {v4, v12, v0, v2, v3}, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;->setClipBounds(IIII)V

    goto :goto_83

    nop

    :goto_8a
    sub-int/2addr v2, v4

    goto :goto_cd

    nop

    :goto_8b
    iget-object v1, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContentView:Lmiuix/smooth/SmoothFrameLayout2;

    goto :goto_58

    nop

    :goto_8c
    invoke-virtual {v7}, Landroid/graphics/Rect;->width()I

    move-result v12

    goto :goto_a6

    nop

    :goto_8d
    new-instance v5, Landroid/widget/FrameLayout$LayoutParams;

    goto :goto_98

    nop

    :goto_8e
    iget-object v14, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_cb

    nop

    :goto_8f
    invoke-direct {v4, v5, v10}, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;-><init>(Lmiuix/appcompat/widget/HyperPopupWindow;Landroid/content/Context;)V

    goto :goto_8d

    nop

    :goto_90
    iget v8, v8, Landroid/graphics/Rect;->top:I

    goto :goto_4b

    nop

    :goto_91
    iget-object v4, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_b6

    nop

    :goto_92
    iget-object v2, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mPopupWindowStrategy:Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;

    goto :goto_4

    nop

    :goto_93
    iput v5, v3, Landroid/widget/FrameLayout$LayoutParams;->topMargin:I

    :goto_94
    goto :goto_65

    nop

    :goto_95
    invoke-static {v2}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$3200(Lmiuix/appcompat/widget/HyperPopupWindow;)Z

    move-result v2

    goto :goto_d3

    nop

    :goto_96
    invoke-virtual {v4, v5}, Landroid/widget/FrameLayout;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    goto :goto_ed

    nop

    :goto_97
    iget v14, v7, Landroid/graphics/Rect;->top:I

    goto :goto_14

    nop

    :goto_98
    invoke-virtual {v7}, Landroid/graphics/Rect;->width()I

    move-result v10

    goto :goto_49

    nop

    :goto_99
    iget v3, v8, Landroid/graphics/Rect;->bottom:I

    goto :goto_bf

    nop

    :goto_9a
    int-to-float v13, v13

    goto :goto_ac

    nop

    :goto_9b
    invoke-static {v11}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$2300(Lmiuix/appcompat/widget/HyperPopupWindow;)Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;

    move-result-object v11

    goto :goto_77

    nop

    :goto_9c
    move-object/from16 v1, p0

    goto :goto_73

    nop

    :goto_9d
    move/from16 v20, v17

    goto :goto_66

    nop

    :goto_9e
    move v4, v11

    goto :goto_d2

    nop

    :goto_9f
    iget v2, v7, Landroid/graphics/Rect;->left:I

    goto :goto_68

    nop

    :goto_a0
    move/from16 p3, v5

    goto :goto_b9

    nop

    :goto_a1
    move-object v2, v8

    goto :goto_11

    nop

    :goto_a2
    new-instance v4, Lmiuix/appcompat/widget/HyperPopupWindow$ViewBounds;

    goto :goto_db

    nop

    :goto_a3
    iget v3, v7, Landroid/graphics/Rect;->top:I

    goto :goto_ba

    nop

    :goto_a4
    sub-int v15, v15, v19

    goto :goto_25

    nop

    :goto_a5
    invoke-static {v4}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$400(Lmiuix/appcompat/widget/HyperPopupWindow;)Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    move-result-object v4

    goto :goto_0

    nop

    :goto_a6
    move/from16 v18, v3

    goto :goto_ef

    nop

    :goto_a7
    iget-object v3, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContentView:Lmiuix/smooth/SmoothFrameLayout2;

    goto :goto_90

    nop

    :goto_a8
    move/from16 v17, v15

    goto :goto_c4

    nop

    :goto_a9
    invoke-static {v2, v4, v5, v6, v7}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$3100(Landroid/widget/ListAdapter;Landroid/view/ViewGroup;Landroid/content/Context;II)[[I

    move-result-object v2

    goto :goto_16

    nop

    :goto_aa
    move/from16 v15, p3

    goto :goto_85

    nop

    :goto_ab
    iget v7, v3, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mFinalPopupHeight:I

    goto :goto_41

    nop

    :goto_ac
    invoke-virtual {v11, v13}, Landroid/widget/FrameLayout;->setElevation(F)V

    goto :goto_3d

    nop

    :goto_ad
    iget-object v13, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_b3

    nop

    :goto_ae
    invoke-virtual {v11, v12}, Landroid/widget/FrameLayout;->setBackgroundColor(I)V

    goto :goto_7c

    nop

    :goto_af
    sub-int v2, v2, v19

    goto :goto_3c

    nop

    :goto_b0
    move/from16 v19, v2

    goto :goto_76

    nop

    :goto_b1
    iget v0, v0, Landroid/graphics/Rect;->top:I

    goto :goto_2c

    nop

    :goto_b2
    invoke-static {v3}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$100(Lmiuix/appcompat/widget/HyperPopupWindow;)Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    move-result-object v3

    goto :goto_dc

    nop

    :goto_b3
    invoke-static {v13}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$2900(Lmiuix/appcompat/widget/HyperPopupWindow;)F

    move-result v13

    goto :goto_7e

    nop

    :goto_b4
    invoke-static {v2}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$2300(Lmiuix/appcompat/widget/HyperPopupWindow;)Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;

    move-result-object v2

    goto :goto_3f

    nop

    :goto_b5
    iget-object v4, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_5d

    nop

    :goto_b6
    invoke-static {v4}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$3000(Lmiuix/appcompat/widget/HyperPopupWindow;)I

    move-result v4

    goto :goto_a

    nop

    :goto_b7
    move/from16 v13, p2

    goto :goto_19

    nop

    :goto_b8
    const/4 v5, 0x1

    goto :goto_7f

    nop

    :goto_b9
    sub-int v5, v19, p3

    goto :goto_cc

    nop

    :goto_ba
    sub-int/2addr v0, v3

    goto :goto_b0

    nop

    :goto_bb
    move-object/from16 v21, v6

    goto :goto_59

    nop

    :goto_bc
    sub-int/2addr v3, v12

    goto :goto_78

    nop

    :goto_bd
    if-nez p4, :cond_4

    goto :goto_2

    :cond_4
    goto :goto_1e

    nop

    :goto_be
    iget v2, v8, Landroid/graphics/Rect;->bottom:I

    goto :goto_5

    nop

    :goto_bf
    sub-int v3, v3, p2

    goto :goto_c5

    nop

    :goto_c0
    const/4 v12, 0x0

    goto :goto_ae

    nop

    :goto_c1
    iget-object v4, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mListView:Landroid/widget/ListView;

    goto :goto_5f

    nop

    :goto_c2
    invoke-virtual {v3}, Landroid/graphics/Rect;->width()I

    move-result v14

    goto :goto_4c

    nop

    :goto_c3
    invoke-virtual {v5, v4}, Landroid/widget/FrameLayout;->addView(Landroid/view/View;)V

    goto :goto_6b

    nop

    :goto_c4
    move-object/from16 v3, p1

    goto :goto_aa

    nop

    :goto_c5
    sub-int v4, v4, v19

    goto :goto_cf

    nop

    :goto_c6
    iget-object v2, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_95

    nop

    :goto_c7
    invoke-virtual {v0, v2}, Landroid/widget/FrameLayout;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    goto :goto_6

    nop

    :goto_c8
    iget-object v2, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mPopupWindowStrategy:Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;

    goto :goto_1a

    nop

    :goto_c9
    move-object/from16 v2, p2

    goto :goto_f1

    nop

    :goto_ca
    move/from16 v17, v5

    goto :goto_e4

    nop

    :goto_cb
    invoke-static {v14}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$3700(Lmiuix/appcompat/widget/HyperPopupWindow;)I

    move-result v14

    goto :goto_22

    nop

    :goto_cc
    invoke-direct {v10, v4, v5}, Landroid/widget/FrameLayout$LayoutParams;-><init>(II)V

    goto :goto_27

    nop

    :goto_cd
    iput v2, v8, Landroid/graphics/Rect;->right:I

    goto :goto_be

    nop

    :goto_ce
    iput-object v4, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mViewBounds:Lmiuix/appcompat/widget/HyperPopupWindow$ViewBounds;

    goto :goto_f0

    nop

    :goto_cf
    sub-int v5, v5, p2

    goto :goto_a4

    nop

    :goto_d0
    invoke-static {v3, v7}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$3500(Landroid/graphics/Rect;Landroid/graphics/Rect;)Landroid/graphics/Rect;

    move-result-object v7

    goto :goto_4f

    nop

    :goto_d1
    iget v2, v8, Landroid/graphics/Rect;->right:I

    goto :goto_2d

    nop

    :goto_d2
    move/from16 v11, v16

    goto :goto_d8

    nop

    :goto_d3
    if-nez v2, :cond_5

    goto :goto_33

    :cond_5
    goto :goto_87

    nop

    :goto_d4
    goto :goto_e1

    :goto_d5
    goto :goto_e0

    nop

    :goto_d6
    div-int/lit8 v9, v9, 0x2

    goto :goto_30

    nop

    :goto_d7
    invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$800(Lmiuix/appcompat/widget/HyperPopupWindow;)Landroid/view/ViewGroup;

    move-result-object v3

    goto :goto_8b

    nop

    :goto_d8
    move/from16 v16, v2

    goto :goto_a1

    nop

    :goto_d9
    const/4 v11, 0x0

    goto :goto_34

    nop

    :goto_da
    invoke-static {v4}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$3000(Lmiuix/appcompat/widget/HyperPopupWindow;)I

    move-result v4

    goto :goto_31

    nop

    :goto_db
    iget-object v5, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContentView:Lmiuix/smooth/SmoothFrameLayout2;

    goto :goto_23

    nop

    :goto_dc
    iget-object v3, v3, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mBoundsRect:Landroid/graphics/Rect;

    goto :goto_4d

    nop

    :goto_dd
    sub-int/2addr v2, v4

    goto :goto_12

    nop

    :goto_de
    const/16 v20, 0x1

    goto :goto_79

    nop

    :goto_df
    iget-object v4, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_80

    nop

    :goto_e0
    int-to-float v11, v7

    :goto_e1
    goto :goto_37

    nop

    :goto_e2
    invoke-virtual {v6, v0}, Landroid/view/ViewTreeObserver;->addOnPreDrawListener(Landroid/view/ViewTreeObserver$OnPreDrawListener;)V

    :goto_e3
    goto :goto_1f

    nop

    :goto_e4
    const/4 v5, 0x0

    goto :goto_7b

    nop

    :goto_e5
    iget-object v2, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_72

    nop

    :goto_e6
    iget-object v2, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mAdapter:Landroid/widget/ListAdapter;

    goto :goto_c1

    nop

    :goto_e7
    new-instance v2, Landroid/widget/FrameLayout$LayoutParams;

    goto :goto_8c

    nop

    :goto_e8
    invoke-virtual {v3}, Landroid/graphics/Rect;->height()I

    move-result v3

    goto :goto_53

    nop

    :goto_e9
    invoke-virtual {v7}, Landroid/graphics/Rect;->width()I

    move-result v9

    goto :goto_82

    nop

    :goto_ea
    iget-object v5, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_46

    nop

    :goto_eb
    iget-object v2, v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mPopupWindowStrategy:Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;

    goto :goto_26

    nop

    :goto_ec
    invoke-virtual {v2, v11, v13, v14, v3}, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;->setClipBounds(IIII)V

    goto :goto_4e

    nop

    :goto_ed
    const/4 v5, 0x0

    goto :goto_9

    nop

    :goto_ee
    invoke-static {v6}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$3200(Lmiuix/appcompat/widget/HyperPopupWindow;)Z

    move-result v6

    goto :goto_51

    nop

    :goto_ef
    invoke-virtual {v7}, Landroid/graphics/Rect;->height()I

    move-result v3

    goto :goto_42

    nop

    :goto_f0
    invoke-virtual {v4, v6}, Lmiuix/appcompat/widget/HyperPopupWindow$ViewBounds;->setMeasureWidth(I)V

    goto :goto_b5

    nop

    :goto_f1
    invoke-virtual {v2, v0}, Landroid/view/ViewGroup;->addView(Landroid/view/View;)V

    goto :goto_88

    nop

    :goto_f2
    invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$2300(Lmiuix/appcompat/widget/HyperPopupWindow;)Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;

    move-result-object v0

    goto :goto_c7

    nop

    :goto_f3
    move-object/from16 v6, v21

    goto :goto_e2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_widget_HyperPopupWindow__PopupContentHolder__update',
        'method': '.method update()Z',
        'method_name': 'update',
        'method_anchors': ['iget-object v1, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;', 'iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;', 'invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$4100(Lmiuix/appcompat/widget/HyperPopupWindow;)Landroid/graphics/Rect;', 'invoke-static {v0, v2}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$4002(Lmiuix/appcompat/widget/HyperPopupWindow;Landroid/graphics/Rect;)Landroid/graphics/Rect;', 'iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mAdapter:Landroid/widget/ListAdapter;', 'iget-object v2, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mListView:Landroid/widget/ListView;', 'iget-object v3, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContext:Landroid/content/Context;', 'iget v4, v1, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mMaxWidth:I'],
        'type': 'method_replace',
        'search': """.method update()Z
    .registers 9

    iget-object v1, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$4100(Lmiuix/appcompat/widget/HyperPopupWindow;)Landroid/graphics/Rect;

    move-result-object v2

    invoke-static {v0, v2}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$4002(Lmiuix/appcompat/widget/HyperPopupWindow;Landroid/graphics/Rect;)Landroid/graphics/Rect;

    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mAdapter:Landroid/widget/ListAdapter;

    iget-object v2, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mListView:Landroid/widget/ListView;

    iget-object v3, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContext:Landroid/content/Context;

    iget v4, v1, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mMaxWidth:I

    iget v5, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mMinWidth:I

    invoke-static {v0, v2, v3, v4, v5}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$3100(Landroid/widget/ListAdapter;Landroid/view/ViewGroup;Landroid/content/Context;II)[[I

    move-result-object v0

    iput-object v0, v1, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mItemViewBounds:[[I

    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mPopupWindowStrategy:Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;

    invoke-interface {v0, v1}, Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;->measureContentSize(Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;)V

    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mPopupWindowStrategy:Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;

    invoke-interface {v0, v1}, Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;->getXInWindow(Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;)I

    move-result v2

    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mPopupWindowStrategy:Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;

    invoke-interface {v0, v1}, Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;->getYInWindow(Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;)I

    move-result v3

    iget v4, v1, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mFinalPopupWidth:I

    iget v5, v1, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mFinalPopupHeight:I

    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mBoundsRect:Landroid/graphics/Rect;

    add-int v6, v2, v4

    add-int v7, v3, v5

    invoke-virtual {v0, v2, v3, v6, v7}, Landroid/graphics/Rect;->set(IIII)V

    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$3200(Lmiuix/appcompat/widget/HyperPopupWindow;)Z

    move-result v0

    if-eqz v0, :cond_0

    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-static/range {v0 .. v5}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$3300(Lmiuix/appcompat/widget/HyperPopupWindow;Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;IIII)V

    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$4000(Lmiuix/appcompat/widget/HyperPopupWindow;)Landroid/graphics/Rect;

    move-result-object v0

    invoke-virtual {v0}, Landroid/graphics/Rect;->width()I

    move-result v0

    iget-object v1, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-static {v1}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$4000(Lmiuix/appcompat/widget/HyperPopupWindow;)Landroid/graphics/Rect;

    move-result-object v1

    invoke-virtual {v1}, Landroid/graphics/Rect;->height()I

    move-result v1

    iget-object v2, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-virtual {v2, v0}, Landroid/widget/PopupWindow;->setWidth(I)V

    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-virtual {v0, v1}, Landroid/widget/PopupWindow;->setHeight(I)V

    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$4000(Lmiuix/appcompat/widget/HyperPopupWindow;)Landroid/graphics/Rect;

    move-result-object v1

    iget v1, v1, Landroid/graphics/Rect;->left:I

    iget-object v2, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-static {v2}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$4000(Lmiuix/appcompat/widget/HyperPopupWindow;)Landroid/graphics/Rect;

    move-result-object v2

    iget v2, v2, Landroid/graphics/Rect;->top:I

    iget-object v3, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mBoundsRect:Landroid/graphics/Rect;

    invoke-virtual {v3}, Landroid/graphics/Rect;->width()I

    move-result v3

    iget-object p0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mBoundsRect:Landroid/graphics/Rect;

    invoke-virtual {p0}, Landroid/graphics/Rect;->height()I

    move-result p0

    invoke-virtual {v0, v1, v2, v3, p0}, Landroid/widget/PopupWindow;->update(IIII)V

    goto :goto_0

    :cond_0
    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mBoundsRect:Landroid/graphics/Rect;

    invoke-virtual {v0}, Landroid/graphics/Rect;->width()I

    move-result v0

    iget-object v1, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mBoundsRect:Landroid/graphics/Rect;

    invoke-virtual {v1}, Landroid/graphics/Rect;->height()I

    move-result v1

    iget-object v2, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-virtual {v2, v0}, Landroid/widget/PopupWindow;->setWidth(I)V

    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    invoke-virtual {v0, v1}, Landroid/widget/PopupWindow;->setHeight(I)V

    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    iget-object v1, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mBoundsRect:Landroid/graphics/Rect;

    iget v2, v1, Landroid/graphics/Rect;->left:I

    iget v3, v1, Landroid/graphics/Rect;->top:I

    invoke-virtual {v1}, Landroid/graphics/Rect;->width()I

    move-result v1

    iget-object p0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mBoundsRect:Landroid/graphics/Rect;

    invoke-virtual {p0}, Landroid/graphics/Rect;->height()I

    move-result p0

    invoke-virtual {v0, v2, v3, v1, p0}, Landroid/widget/PopupWindow;->update(IIII)V

    :goto_0
    const/4 p0, 0x1

    return p0
.end method""",
        'replacement': """.method update()Z
    .registers 9

    goto :goto_1d

    nop

    :goto_0
    invoke-interface {v0, v1}, Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;->getYInWindow(Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;)I

    move-result v3

    goto :goto_2e

    nop

    :goto_1
    iget v1, v1, Landroid/graphics/Rect;->left:I

    goto :goto_21

    nop

    :goto_2
    invoke-virtual {v1}, Landroid/graphics/Rect;->width()I

    move-result v1

    goto :goto_5

    nop

    :goto_3
    invoke-virtual {v0, v2, v3, v1, p0}, Landroid/widget/PopupWindow;->update(IIII)V

    :goto_4
    goto :goto_19

    nop

    :goto_5
    iget-object p0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mBoundsRect:Landroid/graphics/Rect;

    goto :goto_3c

    nop

    :goto_6
    iget-object v2, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_16

    nop

    :goto_7
    iget-object v1, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_3b

    nop

    :goto_8
    invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$4100(Lmiuix/appcompat/widget/HyperPopupWindow;)Landroid/graphics/Rect;

    move-result-object v2

    goto :goto_23

    nop

    :goto_9
    iget-object v1, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mBoundsRect:Landroid/graphics/Rect;

    goto :goto_31

    nop

    :goto_a
    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_39

    nop

    :goto_b
    add-int v7, v3, v5

    goto :goto_15

    nop

    :goto_c
    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mPopupWindowStrategy:Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;

    goto :goto_0

    nop

    :goto_d
    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_8

    nop

    :goto_e
    invoke-virtual {v0, v1}, Landroid/widget/PopupWindow;->setHeight(I)V

    goto :goto_14

    nop

    :goto_f
    invoke-interface {v0, v1}, Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;->getXInWindow(Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;)I

    move-result v2

    goto :goto_c

    nop

    :goto_10
    invoke-static {v0, v2, v3, v4, v5}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$3100(Landroid/widget/ListAdapter;Landroid/view/ViewGroup;Landroid/content/Context;II)[[I

    move-result-object v0

    goto :goto_3d

    nop

    :goto_11
    iget-object v3, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mContext:Landroid/content/Context;

    goto :goto_3e

    nop

    :goto_12
    iget-object v3, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mBoundsRect:Landroid/graphics/Rect;

    goto :goto_2d

    nop

    :goto_13
    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_28

    nop

    :goto_14
    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_17

    nop

    :goto_15
    invoke-virtual {v0, v2, v3, v6, v7}, Landroid/graphics/Rect;->set(IIII)V

    goto :goto_40

    nop

    :goto_16
    invoke-virtual {v2, v0}, Landroid/widget/PopupWindow;->setWidth(I)V

    goto :goto_13

    nop

    :goto_17
    iget-object v1, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mBoundsRect:Landroid/graphics/Rect;

    goto :goto_1f

    nop

    :goto_18
    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mBoundsRect:Landroid/graphics/Rect;

    goto :goto_25

    nop

    :goto_19
    const/4 p0, 0x1

    goto :goto_1c

    nop

    :goto_1a
    invoke-virtual {v0, v1, v2, v3, p0}, Landroid/widget/PopupWindow;->update(IIII)V

    goto :goto_35

    nop

    :goto_1b
    iget-object p0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mBoundsRect:Landroid/graphics/Rect;

    goto :goto_33

    nop

    :goto_1c
    return p0

    :goto_1d
    iget-object v1, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    goto :goto_d

    nop

    :goto_1e
    invoke-interface {v0, v1}, Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;->measureContentSize(Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;)V

    goto :goto_44

    nop

    :goto_1f
    iget v2, v1, Landroid/graphics/Rect;->left:I

    goto :goto_20

    nop

    :goto_20
    iget v3, v1, Landroid/graphics/Rect;->top:I

    goto :goto_2

    nop

    :goto_21
    iget-object v2, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_2b

    nop

    :goto_22
    iget-object v2, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_27

    nop

    :goto_23
    invoke-static {v0, v2}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$4002(Lmiuix/appcompat/widget/HyperPopupWindow;Landroid/graphics/Rect;)Landroid/graphics/Rect;

    goto :goto_24

    nop

    :goto_24
    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mAdapter:Landroid/widget/ListAdapter;

    goto :goto_41

    nop

    :goto_25
    invoke-virtual {v0}, Landroid/graphics/Rect;->width()I

    move-result v0

    goto :goto_9

    nop

    :goto_26
    invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$3200(Lmiuix/appcompat/widget/HyperPopupWindow;)Z

    move-result v0

    goto :goto_2f

    nop

    :goto_27
    invoke-virtual {v2, v0}, Landroid/widget/PopupWindow;->setWidth(I)V

    goto :goto_32

    nop

    :goto_28
    invoke-virtual {v0, v1}, Landroid/widget/PopupWindow;->setHeight(I)V

    goto :goto_34

    nop

    :goto_29
    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mPopupWindowStrategy:Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;

    goto :goto_1e

    nop

    :goto_2a
    iget v5, v1, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mFinalPopupHeight:I

    goto :goto_38

    nop

    :goto_2b
    invoke-static {v2}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$4000(Lmiuix/appcompat/widget/HyperPopupWindow;)Landroid/graphics/Rect;

    move-result-object v2

    goto :goto_2c

    nop

    :goto_2c
    iget v2, v2, Landroid/graphics/Rect;->top:I

    goto :goto_12

    nop

    :goto_2d
    invoke-virtual {v3}, Landroid/graphics/Rect;->width()I

    move-result v3

    goto :goto_1b

    nop

    :goto_2e
    iget v4, v1, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mFinalPopupWidth:I

    goto :goto_2a

    nop

    :goto_2f
    if-nez v0, :cond_0

    goto :goto_36

    :cond_0
    goto :goto_43

    nop

    :goto_30
    invoke-static/range {v0 .. v5}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$3300(Lmiuix/appcompat/widget/HyperPopupWindow;Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;IIII)V

    goto :goto_a

    nop

    :goto_31
    invoke-virtual {v1}, Landroid/graphics/Rect;->height()I

    move-result v1

    goto :goto_22

    nop

    :goto_32
    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_e

    nop

    :goto_33
    invoke-virtual {p0}, Landroid/graphics/Rect;->height()I

    move-result p0

    goto :goto_1a

    nop

    :goto_34
    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_3f

    nop

    :goto_35
    goto :goto_4

    :goto_36
    goto :goto_18

    nop

    :goto_37
    invoke-virtual {v1}, Landroid/graphics/Rect;->height()I

    move-result v1

    goto :goto_6

    nop

    :goto_38
    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mBoundsRect:Landroid/graphics/Rect;

    goto :goto_45

    nop

    :goto_39
    invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$4000(Lmiuix/appcompat/widget/HyperPopupWindow;)Landroid/graphics/Rect;

    move-result-object v0

    goto :goto_42

    nop

    :goto_3a
    iget v5, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mMinWidth:I

    goto :goto_10

    nop

    :goto_3b
    invoke-static {v1}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$4000(Lmiuix/appcompat/widget/HyperPopupWindow;)Landroid/graphics/Rect;

    move-result-object v1

    goto :goto_37

    nop

    :goto_3c
    invoke-virtual {p0}, Landroid/graphics/Rect;->height()I

    move-result p0

    goto :goto_3

    nop

    :goto_3d
    iput-object v0, v1, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mItemViewBounds:[[I

    goto :goto_29

    nop

    :goto_3e
    iget v4, v1, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mMaxWidth:I

    goto :goto_3a

    nop

    :goto_3f
    invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow;->access$4000(Lmiuix/appcompat/widget/HyperPopupWindow;)Landroid/graphics/Rect;

    move-result-object v1

    goto :goto_1

    nop

    :goto_40
    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_26

    nop

    :goto_41
    iget-object v2, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mListView:Landroid/widget/ListView;

    goto :goto_11

    nop

    :goto_42
    invoke-virtual {v0}, Landroid/graphics/Rect;->width()I

    move-result v0

    goto :goto_7

    nop

    :goto_43
    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_30

    nop

    :goto_44
    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->mPopupWindowStrategy:Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;

    goto :goto_f

    nop

    :goto_45
    add-int v6, v2, v4

    goto :goto_b

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
