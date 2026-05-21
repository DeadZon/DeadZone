TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/popupwidget/widget/PopupWindow.smali'
CLASS_FALLBACK_NAMES = ['PopupWindow.smali']
CLASS_ANCHORS = ['.super Landroid/widget/PopupWindow;']

PATCHES = [
    {
        'id': 'miuix_popupwidget_widget_PopupWindow__checkMaxHeight',
        'method': '.method protected checkMaxHeight(Landroid/graphics/Rect;Landroid/graphics/Rect;)I',
        'method_name': 'checkMaxHeight',
        'method_anchors': ['iget p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mMaxAllowedHeight:I', 'invoke-virtual {p1}, Landroid/graphics/Rect;->height()I', 'iget v0, p2, Landroid/graphics/Rect;->top:I', 'iget p2, p2, Landroid/graphics/Rect;->bottom:I', 'invoke-static {p0, p1}, Ljava/lang/Math;->min(II)I', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected checkMaxHeight(Landroid/graphics/Rect;Landroid/graphics/Rect;)I
    .registers 4

    iget p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mMaxAllowedHeight:I

    invoke-virtual {p1}, Landroid/graphics/Rect;->height()I

    move-result p1

    iget v0, p2, Landroid/graphics/Rect;->top:I

    sub-int/2addr p1, v0

    iget p2, p2, Landroid/graphics/Rect;->bottom:I

    sub-int/2addr p1, p2

    invoke-static {p0, p1}, Ljava/lang/Math;->min(II)I

    move-result p0

    return p0
.end method""",
        'replacement': """.method protected checkMaxHeight(Landroid/graphics/Rect;Landroid/graphics/Rect;)I
    .registers 4

    goto :goto_3

    nop

    :goto_0
    iget p2, p2, Landroid/graphics/Rect;->bottom:I

    goto :goto_6

    nop

    :goto_1
    return p0

    :goto_2
    iget v0, p2, Landroid/graphics/Rect;->top:I

    goto :goto_7

    nop

    :goto_3
    iget p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mMaxAllowedHeight:I

    goto :goto_5

    nop

    :goto_4
    invoke-static {p0, p1}, Ljava/lang/Math;->min(II)I

    move-result p0

    goto :goto_1

    nop

    :goto_5
    invoke-virtual {p1}, Landroid/graphics/Rect;->height()I

    move-result p1

    goto :goto_2

    nop

    :goto_6
    sub-int/2addr p1, p2

    goto :goto_4

    nop

    :goto_7
    sub-int/2addr p1, v0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_popupwidget_widget_PopupWindow__checkMaxWidth',
        'method': '.method protected checkMaxWidth(Landroid/graphics/Rect;Landroid/graphics/Rect;)I',
        'method_name': 'checkMaxWidth',
        'method_anchors': ['iget p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mMaxAllowedWidth:I', 'invoke-virtual {p1}, Landroid/graphics/Rect;->width()I', 'iget v0, p2, Landroid/graphics/Rect;->left:I', 'iget p2, p2, Landroid/graphics/Rect;->right:I', 'invoke-static {p0, p1}, Ljava/lang/Math;->min(II)I', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected checkMaxWidth(Landroid/graphics/Rect;Landroid/graphics/Rect;)I
    .registers 4

    iget p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mMaxAllowedWidth:I

    invoke-virtual {p1}, Landroid/graphics/Rect;->width()I

    move-result p1

    iget v0, p2, Landroid/graphics/Rect;->left:I

    sub-int/2addr p1, v0

    iget p2, p2, Landroid/graphics/Rect;->right:I

    sub-int/2addr p1, p2

    invoke-static {p0, p1}, Ljava/lang/Math;->min(II)I

    move-result p0

    return p0
.end method""",
        'replacement': """.method protected checkMaxWidth(Landroid/graphics/Rect;Landroid/graphics/Rect;)I
    .registers 4

    goto :goto_6

    nop

    :goto_0
    iget p2, p2, Landroid/graphics/Rect;->right:I

    goto :goto_2

    nop

    :goto_1
    invoke-static {p0, p1}, Ljava/lang/Math;->min(II)I

    move-result p0

    goto :goto_4

    nop

    :goto_2
    sub-int/2addr p1, p2

    goto :goto_1

    nop

    :goto_3
    invoke-virtual {p1}, Landroid/graphics/Rect;->width()I

    move-result p1

    goto :goto_7

    nop

    :goto_4
    return p0

    :goto_5
    sub-int/2addr p1, v0

    goto :goto_0

    nop

    :goto_6
    iget p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mMaxAllowedWidth:I

    goto :goto_3

    nop

    :goto_7
    iget v0, p2, Landroid/graphics/Rect;->left:I

    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_popupwidget_widget_PopupWindow__checkMinWidth',
        'method': '.method protected checkMinWidth(Landroid/graphics/Rect;Landroid/graphics/Rect;)I',
        'method_name': 'checkMinWidth',
        'method_anchors': ['iget p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mMinAllowedWidth:I', 'invoke-virtual {p1}, Landroid/graphics/Rect;->width()I', 'iget v0, p2, Landroid/graphics/Rect;->left:I', 'iget p2, p2, Landroid/graphics/Rect;->right:I', 'invoke-static {p0, p1}, Ljava/lang/Math;->min(II)I', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected checkMinWidth(Landroid/graphics/Rect;Landroid/graphics/Rect;)I
    .registers 4

    iget p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mMinAllowedWidth:I

    invoke-virtual {p1}, Landroid/graphics/Rect;->width()I

    move-result p1

    iget v0, p2, Landroid/graphics/Rect;->left:I

    sub-int/2addr p1, v0

    iget p2, p2, Landroid/graphics/Rect;->right:I

    sub-int/2addr p1, p2

    invoke-static {p0, p1}, Ljava/lang/Math;->min(II)I

    move-result p0

    return p0
.end method""",
        'replacement': """.method protected checkMinWidth(Landroid/graphics/Rect;Landroid/graphics/Rect;)I
    .registers 4

    goto :goto_7

    nop

    :goto_0
    iget p2, p2, Landroid/graphics/Rect;->right:I

    goto :goto_6

    nop

    :goto_1
    invoke-static {p0, p1}, Ljava/lang/Math;->min(II)I

    move-result p0

    goto :goto_2

    nop

    :goto_2
    return p0

    :goto_3
    iget v0, p2, Landroid/graphics/Rect;->left:I

    goto :goto_5

    nop

    :goto_4
    invoke-virtual {p1}, Landroid/graphics/Rect;->width()I

    move-result p1

    goto :goto_3

    nop

    :goto_5
    sub-int/2addr p1, v0

    goto :goto_0

    nop

    :goto_6
    sub-int/2addr p1, p2

    goto :goto_1

    nop

    :goto_7
    iget p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mMinAllowedWidth:I

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_popupwidget_widget_PopupWindow__computePopupContentSize',
        'method': '.method protected computePopupContentSize()V',
        'method_name': 'computePopupContentSize',
        'method_anchors': ['const-string v0, "PopupWindow"', 'const-string v1, "computePopupContentSize"', 'invoke-static {v0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I', 'iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mAdapter:Landroid/widget/ListAdapter;', 'if-eqz v0, :cond_0', 'iget-object v1, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;', 'iget-object v3, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContext:Landroid/content/Context;', 'invoke-virtual {p0, v0, v2, v3}, Lmiuix/popupwidget/widget/PopupWindow;->getItemViewBounds(Landroid/widget/ListAdapter;Landroid/view/ViewGroup;Landroid/content/Context;)[[I'],
        'type': 'method_replace',
        'search': """.method protected computePopupContentSize()V
    .registers 5

    const-string v0, "PopupWindow"

    const-string v1, "computePopupContentSize"

    invoke-static {v0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mAdapter:Landroid/widget/ListAdapter;

    if-eqz v0, :cond_0

    iget-object v1, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    const/4 v2, 0x0

    iget-object v3, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContext:Landroid/content/Context;

    invoke-virtual {p0, v0, v2, v3}, Lmiuix/popupwidget/widget/PopupWindow;->getItemViewBounds(Landroid/widget/ListAdapter;Landroid/view/ViewGroup;Landroid/content/Context;)[[I

    move-result-object v0

    iput-object v0, v1, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mItemViewBounds:[[I

    goto :goto_0

    :cond_0
    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    invoke-virtual {p0, v0}, Lmiuix/popupwidget/widget/PopupWindow;->getContentViewBounds(Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;)V

    :goto_0
    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowStrategy:Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;

    iget-object p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    invoke-interface {v0, p0}, Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;->measureContentSize(Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;)V

    return-void
.end method""",
        'replacement': """.method protected computePopupContentSize()V
    .registers 5

    goto :goto_a

    nop

    :goto_0
    const/4 v2, 0x0

    goto :goto_4

    nop

    :goto_1
    invoke-static {v0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_9

    nop

    :goto_2
    iput-object v0, v1, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mItemViewBounds:[[I

    goto :goto_10

    nop

    :goto_3
    iget-object p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    goto :goto_12

    nop

    :goto_4
    iget-object v3, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContext:Landroid/content/Context;

    goto :goto_c

    nop

    :goto_5
    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    goto :goto_d

    nop

    :goto_6
    return-void

    :goto_7
    if-nez v0, :cond_0

    goto :goto_11

    :cond_0
    goto :goto_8

    nop

    :goto_8
    iget-object v1, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    goto :goto_0

    nop

    :goto_9
    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mAdapter:Landroid/widget/ListAdapter;

    goto :goto_7

    nop

    :goto_a
    const-string v0, "PopupWindow"

    goto :goto_f

    nop

    :goto_b
    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowStrategy:Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;

    goto :goto_3

    nop

    :goto_c
    invoke-virtual {p0, v0, v2, v3}, Lmiuix/popupwidget/widget/PopupWindow;->getItemViewBounds(Landroid/widget/ListAdapter;Landroid/view/ViewGroup;Landroid/content/Context;)[[I

    move-result-object v0

    goto :goto_2

    nop

    :goto_d
    invoke-virtual {p0, v0}, Lmiuix/popupwidget/widget/PopupWindow;->getContentViewBounds(Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;)V

    :goto_e
    goto :goto_b

    nop

    :goto_f
    const-string v1, "computePopupContentSize"

    goto :goto_1

    nop

    :goto_10
    goto :goto_e

    :goto_11
    goto :goto_5

    nop

    :goto_12
    invoke-interface {v0, p0}, Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;->measureContentSize(Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;)V

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_popupwidget_widget_PopupWindow__getContentViewBounds',
        'method': '.method protected getContentViewBounds(Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;)V',
        'method_name': 'getContentViewBounds',
        'method_anchors': ['iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContentView:Landroid/view/View;', 'if-eqz v0, :cond_0', 'iget-object v0, p1, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mContentViewBounds:Landroid/graphics/Rect;', 'invoke-virtual {v0, v1, v1, v1, v1}, Landroid/graphics/Rect;->set(IIII)V', 'iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContentView:Landroid/view/View;', 'invoke-virtual {v0, v1, v1}, Landroid/view/View;->measure(II)V', 'iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContentView:Landroid/view/View;', 'invoke-virtual {v0}, Landroid/view/View;->getMeasuredWidth()I'],
        'type': 'method_replace',
        'search': """.method protected getContentViewBounds(Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;)V
    .registers 4

    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContentView:Landroid/view/View;

    if-eqz v0, :cond_0

    iget-object v0, p1, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mContentViewBounds:Landroid/graphics/Rect;

    const/4 v1, 0x0

    invoke-virtual {v0, v1, v1, v1, v1}, Landroid/graphics/Rect;->set(IIII)V

    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContentView:Landroid/view/View;

    invoke-virtual {v0, v1, v1}, Landroid/view/View;->measure(II)V

    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContentView:Landroid/view/View;

    invoke-virtual {v0}, Landroid/view/View;->getMeasuredWidth()I

    move-result v0

    iget-object p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContentView:Landroid/view/View;

    invoke-virtual {p0}, Landroid/view/View;->getMeasuredHeight()I

    move-result p0

    iget-object p1, p1, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mContentViewBounds:Landroid/graphics/Rect;

    invoke-virtual {p1, v1, v1, v0, p0}, Landroid/graphics/Rect;->set(IIII)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected getContentViewBounds(Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;)V
    .registers 4

    goto :goto_9

    nop

    :goto_0
    invoke-virtual {v0}, Landroid/view/View;->getMeasuredWidth()I

    move-result v0

    goto :goto_1

    nop

    :goto_1
    iget-object p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContentView:Landroid/view/View;

    goto :goto_7

    nop

    :goto_2
    iget-object p1, p1, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mContentViewBounds:Landroid/graphics/Rect;

    goto :goto_b

    nop

    :goto_3
    return-void

    :goto_4
    invoke-virtual {v0, v1, v1, v1, v1}, Landroid/graphics/Rect;->set(IIII)V

    goto :goto_5

    nop

    :goto_5
    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContentView:Landroid/view/View;

    goto :goto_e

    nop

    :goto_6
    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContentView:Landroid/view/View;

    goto :goto_0

    nop

    :goto_7
    invoke-virtual {p0}, Landroid/view/View;->getMeasuredHeight()I

    move-result p0

    goto :goto_2

    nop

    :goto_8
    if-nez v0, :cond_0

    goto :goto_c

    :cond_0
    goto :goto_a

    nop

    :goto_9
    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContentView:Landroid/view/View;

    goto :goto_8

    nop

    :goto_a
    iget-object v0, p1, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mContentViewBounds:Landroid/graphics/Rect;

    goto :goto_d

    nop

    :goto_b
    invoke-virtual {p1, v1, v1, v0, p0}, Landroid/graphics/Rect;->set(IIII)V

    :goto_c
    goto :goto_3

    nop

    :goto_d
    const/4 v1, 0x0

    goto :goto_4

    nop

    :goto_e
    invoke-virtual {v0, v1, v1}, Landroid/view/View;->measure(II)V

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_popupwidget_widget_PopupWindow__getDecorView',
        'method': '.method protected getDecorView()Landroid/view/View;',
        'method_name': 'getDecorView',
        'method_anchors': ['iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mFenceDecor:Ljava/lang/ref/WeakReference;', 'if-eqz v0, :cond_1', 'invoke-virtual {v0}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;', 'if-nez v0, :cond_0', 'iget-object p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mFenceDecor:Ljava/lang/ref/WeakReference;', 'invoke-virtual {p0}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;', 'check-cast p0, Landroid/view/View;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getDecorView()Landroid/view/View;
    .registers 2

    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mFenceDecor:Ljava/lang/ref/WeakReference;

    if-eqz v0, :cond_1

    invoke-virtual {v0}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;

    move-result-object v0

    if-nez v0, :cond_0

    goto :goto_0

    :cond_0
    iget-object p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mFenceDecor:Ljava/lang/ref/WeakReference;

    invoke-virtual {p0}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;

    move-result-object p0

    check-cast p0, Landroid/view/View;

    return-object p0

    :cond_1
    :goto_0
    iget-object p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mAnchorView:Ljava/lang/ref/WeakReference;

    if-eqz p0, :cond_2

    invoke-virtual {p0}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;

    move-result-object p0

    check-cast p0, Landroid/view/View;

    invoke-virtual {p0}, Landroid/view/View;->getRootView()Landroid/view/View;

    move-result-object p0

    return-object p0

    :cond_2
    const/4 p0, 0x0

    return-object p0
.end method""",
        'replacement': """.method protected getDecorView()Landroid/view/View;
    .registers 2

    goto :goto_c

    nop

    :goto_0
    if-nez v0, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_11

    nop

    :goto_1
    iget-object p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mAnchorView:Ljava/lang/ref/WeakReference;

    goto :goto_a

    nop

    :goto_2
    return-object p0

    :goto_3
    goto :goto_1

    nop

    :goto_4
    check-cast p0, Landroid/view/View;

    goto :goto_2

    nop

    :goto_5
    invoke-virtual {p0}, Landroid/view/View;->getRootView()Landroid/view/View;

    move-result-object p0

    goto :goto_6

    nop

    :goto_6
    return-object p0

    :goto_7
    goto :goto_d

    nop

    :goto_8
    goto :goto_3

    :goto_9
    goto :goto_13

    nop

    :goto_a
    if-nez p0, :cond_1

    goto :goto_7

    :cond_1
    goto :goto_b

    nop

    :goto_b
    invoke-virtual {p0}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;

    move-result-object p0

    goto :goto_10

    nop

    :goto_c
    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mFenceDecor:Ljava/lang/ref/WeakReference;

    goto :goto_0

    nop

    :goto_d
    const/4 p0, 0x0

    goto :goto_12

    nop

    :goto_e
    if-eqz v0, :cond_2

    goto :goto_9

    :cond_2
    goto :goto_8

    nop

    :goto_f
    invoke-virtual {p0}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;

    move-result-object p0

    goto :goto_4

    nop

    :goto_10
    check-cast p0, Landroid/view/View;

    goto :goto_5

    nop

    :goto_11
    invoke-virtual {v0}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;

    move-result-object v0

    goto :goto_e

    nop

    :goto_12
    return-object p0

    :goto_13
    iget-object p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mFenceDecor:Ljava/lang/ref/WeakReference;

    goto :goto_f

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_popupwidget_widget_PopupWindow__getItemViewBounds',
        'method': '.method protected getItemViewBounds(Landroid/widget/ListAdapter;Landroid/view/ViewGroup;Landroid/content/Context;)[[I',
        'method_name': 'getItemViewBounds',
        'method_anchors': ['iget-object p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;', 'iget p0, p0, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mMaxWidth:I', 'invoke-static {p0, v0}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I', 'invoke-static {v0, v0}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I', 'invoke-interface {p1}, Landroid/widget/ListAdapter;->getCount()I', 'sget-object v3, Ljava/lang/Integer;->TYPE:Ljava/lang/Class;', 'invoke-static {v3, v4}, Ljava/lang/reflect/Array;->newInstance(Ljava/lang/Class;[I)Ljava/lang/Object;', 'check-cast v3, [[I'],
        'type': 'method_replace',
        'search': """.method protected getItemViewBounds(Landroid/widget/ListAdapter;Landroid/view/ViewGroup;Landroid/content/Context;)[[I
    .registers 15

    iget-object p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    iget p0, p0, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mMaxWidth:I

    const/high16 v0, -0x80000000

    invoke-static {p0, v0}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p0

    const/4 v0, 0x0

    invoke-static {v0, v0}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v1

    invoke-interface {p1}, Landroid/widget/ListAdapter;->getCount()I

    move-result v2

    const/4 v3, 0x2

    new-array v4, v3, [I

    const/4 v5, 0x1

    aput v3, v4, v5

    aput v2, v4, v0

    sget-object v3, Ljava/lang/Integer;->TYPE:Ljava/lang/Class;

    invoke-static {v3, v4}, Ljava/lang/reflect/Array;->newInstance(Ljava/lang/Class;[I)Ljava/lang/Object;

    move-result-object v3

    check-cast v3, [[I

    const/4 v4, 0x0

    move v6, v0

    move v7, v6

    move-object v8, v4

    :goto_0
    if-ge v6, v2, :cond_2

    invoke-interface {p1, v6}, Landroid/widget/ListAdapter;->getItemViewType(I)I

    move-result v9

    if-eq v9, v7, :cond_0

    move-object v8, v4

    move v7, v9

    :cond_0
    if-nez p2, :cond_1

    new-instance p2, Landroid/widget/FrameLayout;

    invoke-direct {p2, p3}, Landroid/widget/FrameLayout;-><init>(Landroid/content/Context;)V

    :cond_1
    invoke-interface {p1, v6, v8, p2}, Landroid/widget/ListAdapter;->getView(ILandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;

    move-result-object v8

    invoke-virtual {v8, p0, v1}, Landroid/view/View;->measure(II)V

    aget-object v9, v3, v6

    invoke-virtual {v8}, Landroid/view/View;->getMeasuredWidth()I

    move-result v10

    aput v10, v9, v0

    aget-object v9, v3, v6

    invoke-virtual {v8}, Landroid/view/View;->getMeasuredHeight()I

    move-result v10

    aput v10, v9, v5

    add-int/lit8 v6, v6, 0x1

    goto :goto_0

    :cond_2
    return-object v3
.end method""",
        'replacement': """.method protected getItemViewBounds(Landroid/widget/ListAdapter;Landroid/view/ViewGroup;Landroid/content/Context;)[[I
    .registers 15

    goto :goto_18

    nop

    :goto_0
    invoke-interface {p1, v6, v8, p2}, Landroid/widget/ListAdapter;->getView(ILandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;

    move-result-object v8

    goto :goto_27

    nop

    :goto_1
    invoke-virtual {v8}, Landroid/view/View;->getMeasuredWidth()I

    move-result v10

    goto :goto_13

    nop

    :goto_2
    move v7, v6

    goto :goto_10

    nop

    :goto_3
    const/4 v3, 0x2

    goto :goto_1e

    nop

    :goto_4
    new-instance p2, Landroid/widget/FrameLayout;

    goto :goto_16

    nop

    :goto_5
    return-object v3

    :goto_6
    aget-object v9, v3, v6

    goto :goto_26

    nop

    :goto_7
    if-eqz p2, :cond_0

    goto :goto_17

    :cond_0
    goto :goto_4

    nop

    :goto_8
    const/4 v5, 0x1

    goto :goto_23

    nop

    :goto_9
    aput v10, v9, v5

    goto :goto_1f

    nop

    :goto_a
    const/4 v0, 0x0

    goto :goto_1c

    nop

    :goto_b
    goto :goto_11

    :goto_c
    goto :goto_5

    nop

    :goto_d
    move v7, v9

    :goto_e
    goto :goto_7

    nop

    :goto_f
    const/high16 v0, -0x80000000

    goto :goto_29

    nop

    :goto_10
    move-object v8, v4

    :goto_11
    goto :goto_25

    nop

    :goto_12
    check-cast v3, [[I

    goto :goto_14

    nop

    :goto_13
    aput v10, v9, v0

    goto :goto_6

    nop

    :goto_14
    const/4 v4, 0x0

    goto :goto_1a

    nop

    :goto_15
    invoke-interface {p1}, Landroid/widget/ListAdapter;->getCount()I

    move-result v2

    goto :goto_3

    nop

    :goto_16
    invoke-direct {p2, p3}, Landroid/widget/FrameLayout;-><init>(Landroid/content/Context;)V

    :goto_17
    goto :goto_0

    nop

    :goto_18
    iget-object p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    goto :goto_21

    nop

    :goto_19
    if-ne v9, v7, :cond_1

    goto :goto_e

    :cond_1
    goto :goto_22

    nop

    :goto_1a
    move v6, v0

    goto :goto_2

    nop

    :goto_1b
    invoke-interface {p1, v6}, Landroid/widget/ListAdapter;->getItemViewType(I)I

    move-result v9

    goto :goto_19

    nop

    :goto_1c
    invoke-static {v0, v0}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v1

    goto :goto_15

    nop

    :goto_1d
    invoke-static {v3, v4}, Ljava/lang/reflect/Array;->newInstance(Ljava/lang/Class;[I)Ljava/lang/Object;

    move-result-object v3

    goto :goto_12

    nop

    :goto_1e
    new-array v4, v3, [I

    goto :goto_8

    nop

    :goto_1f
    add-int/lit8 v6, v6, 0x1

    goto :goto_b

    nop

    :goto_20
    aput v2, v4, v0

    goto :goto_24

    nop

    :goto_21
    iget p0, p0, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mMaxWidth:I

    goto :goto_f

    nop

    :goto_22
    move-object v8, v4

    goto :goto_d

    nop

    :goto_23
    aput v3, v4, v5

    goto :goto_20

    nop

    :goto_24
    sget-object v3, Ljava/lang/Integer;->TYPE:Ljava/lang/Class;

    goto :goto_1d

    nop

    :goto_25
    if-lt v6, v2, :cond_2

    goto :goto_c

    :cond_2
    goto :goto_1b

    nop

    :goto_26
    invoke-virtual {v8}, Landroid/view/View;->getMeasuredHeight()I

    move-result v10

    goto :goto_9

    nop

    :goto_27
    invoke-virtual {v8, p0, v1}, Landroid/view/View;->measure(II)V

    goto :goto_28

    nop

    :goto_28
    aget-object v9, v3, v6

    goto :goto_1

    nop

    :goto_29
    invoke-static {p0, v0}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p0

    goto :goto_a

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_popupwidget_widget_PopupWindow__prepareContentView',
        'method': '.method protected prepareContentView()V',
        'method_name': 'prepareContentView',
        'method_anchors': ['iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mRootView:Landroid/widget/FrameLayout;', 'invoke-super {p0, v0}, Landroid/widget/PopupWindow;->setContentView(Landroid/view/View;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected prepareContentView()V
    .registers 2

    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mRootView:Landroid/widget/FrameLayout;

    invoke-super {p0, v0}, Landroid/widget/PopupWindow;->setContentView(Landroid/view/View;)V

    return-void
.end method""",
        'replacement': """.method protected prepareContentView()V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mRootView:Landroid/widget/FrameLayout;

    goto :goto_1

    nop

    :goto_1
    invoke-super {p0, v0}, Landroid/widget/PopupWindow;->setContentView(Landroid/view/View;)V

    goto :goto_2

    nop

    :goto_2
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_popupwidget_widget_PopupWindow__prepareWindowElevation',
        'method': '.method protected prepareWindowElevation(Landroid/view/View;I)V',
        'method_name': 'prepareWindowElevation',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/popupwidget/widget/PopupWindow;->shouldSetElevation()Z', 'if-nez v0, :cond_0', 'return-void', 'sget-boolean v0, Lmiuix/core/util/MiShadowUtils;->SUPPORT_MI_SHADOW:Z', 'if-eqz v0, :cond_1', 'invoke-virtual {p1}, Landroid/view/View;->getContext()Landroid/content/Context;', 'invoke-virtual {p2}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;', 'invoke-virtual {p2}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;'],
        'type': 'method_replace',
        'search': """.method protected prepareWindowElevation(Landroid/view/View;I)V
    .registers 6

    invoke-virtual {p0}, Lmiuix/popupwidget/widget/PopupWindow;->shouldSetElevation()Z

    move-result v0

    if-nez v0, :cond_0

    return-void

    :cond_0
    sget-boolean v0, Lmiuix/core/util/MiShadowUtils;->SUPPORT_MI_SHADOW:Z

    if-eqz v0, :cond_1

    invoke-virtual {p1}, Landroid/view/View;->getContext()Landroid/content/Context;

    move-result-object p2

    invoke-virtual {p2}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object p2

    invoke-virtual {p2}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;

    move-result-object p2

    iget p2, p2, Landroid/util/DisplayMetrics;->density:F

    iget v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mShadowColor:I

    const/4 v1, 0x0

    mul-float/2addr v1, p2

    const/high16 v2, 0x41d00000

    mul-float/2addr p2, v2

    iget p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mElevation:I

    int-to-float p0, p0

    invoke-static {p1, v0, v1, p2, p0}, Lmiuix/core/util/MiShadowUtils;->setMiShadow(Landroid/view/View;IFFF)V

    return-void

    :cond_1
    int-to-float p2, p2

    invoke-virtual {p1, p2}, Landroid/view/View;->setElevation(F)V

    invoke-virtual {p0, p1}, Lmiuix/popupwidget/widget/PopupWindow;->setPopupShadowAlpha(Landroid/view/View;)V

    return-void
.end method""",
        'replacement': """.method protected prepareWindowElevation(Landroid/view/View;I)V
    .registers 6

    goto :goto_12

    nop

    :goto_0
    int-to-float p0, p0

    goto :goto_10

    nop

    :goto_1
    return-void

    :goto_2
    goto :goto_6

    nop

    :goto_3
    iget p2, p2, Landroid/util/DisplayMetrics;->density:F

    goto :goto_5

    nop

    :goto_4
    invoke-virtual {p1, p2}, Landroid/view/View;->setElevation(F)V

    goto :goto_13

    nop

    :goto_5
    iget v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mShadowColor:I

    goto :goto_e

    nop

    :goto_6
    sget-boolean v0, Lmiuix/core/util/MiShadowUtils;->SUPPORT_MI_SHADOW:Z

    goto :goto_f

    nop

    :goto_7
    if-eqz v0, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_1

    nop

    :goto_8
    invoke-virtual {p2}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object p2

    goto :goto_14

    nop

    :goto_9
    int-to-float p2, p2

    goto :goto_4

    nop

    :goto_a
    const/high16 v2, 0x41d00000

    goto :goto_b

    nop

    :goto_b
    mul-float/2addr p2, v2

    goto :goto_11

    nop

    :goto_c
    return-void

    :goto_d
    goto :goto_9

    nop

    :goto_e
    const/4 v1, 0x0

    goto :goto_17

    nop

    :goto_f
    if-nez v0, :cond_1

    goto :goto_d

    :cond_1
    goto :goto_16

    nop

    :goto_10
    invoke-static {p1, v0, v1, p2, p0}, Lmiuix/core/util/MiShadowUtils;->setMiShadow(Landroid/view/View;IFFF)V

    goto :goto_c

    nop

    :goto_11
    iget p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mElevation:I

    goto :goto_0

    nop

    :goto_12
    invoke-virtual {p0}, Lmiuix/popupwidget/widget/PopupWindow;->shouldSetElevation()Z

    move-result v0

    goto :goto_7

    nop

    :goto_13
    invoke-virtual {p0, p1}, Lmiuix/popupwidget/widget/PopupWindow;->setPopupShadowAlpha(Landroid/view/View;)V

    goto :goto_15

    nop

    :goto_14
    invoke-virtual {p2}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;

    move-result-object p2

    goto :goto_3

    nop

    :goto_15
    return-void

    :goto_16
    invoke-virtual {p1}, Landroid/view/View;->getContext()Landroid/content/Context;

    move-result-object p2

    goto :goto_8

    nop

    :goto_17
    mul-float/2addr v1, p2

    goto :goto_a

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_popupwidget_widget_PopupWindow__setAnimationStyleByGravity',
        'method': '.method protected setAnimationStyleByGravity(I)V',
        'method_name': 'setAnimationStyleByGravity',
        'method_anchors': ['sget v0, Lmiuix/popupwidget/R$style;->Animation_PopupWindow_ImmersionMenu:I', 'if-ne p1, v1, :cond_0', 'sget v0, Lmiuix/popupwidget/R$style;->Animation_PopupWindow_ImmersionMenu_LeftTop:I', 'if-ne p1, v1, :cond_1', 'sget v0, Lmiuix/popupwidget/R$style;->Animation_PopupWindow_ImmersionMenu_LeftBottom:I', 'if-ne p1, v1, :cond_2', 'sget v0, Lmiuix/popupwidget/R$style;->Animation_PopupWindow_ImmersionMenu_RightTop:I', 'if-ne p1, v1, :cond_3'],
        'type': 'method_replace',
        'search': """.method protected setAnimationStyleByGravity(I)V
    .registers 4

    sget v0, Lmiuix/popupwidget/R$style;->Animation_PopupWindow_ImmersionMenu:I

    const/16 v1, 0x33

    if-ne p1, v1, :cond_0

    sget v0, Lmiuix/popupwidget/R$style;->Animation_PopupWindow_ImmersionMenu_LeftTop:I

    goto :goto_0

    :cond_0
    const/16 v1, 0x53

    if-ne p1, v1, :cond_1

    sget v0, Lmiuix/popupwidget/R$style;->Animation_PopupWindow_ImmersionMenu_LeftBottom:I

    goto :goto_0

    :cond_1
    const/16 v1, 0x35

    if-ne p1, v1, :cond_2

    sget v0, Lmiuix/popupwidget/R$style;->Animation_PopupWindow_ImmersionMenu_RightTop:I

    goto :goto_0

    :cond_2
    const/16 v1, 0x55

    if-ne p1, v1, :cond_3

    sget v0, Lmiuix/popupwidget/R$style;->Animation_PopupWindow_ImmersionMenu_RightBottom:I

    goto :goto_0

    :cond_3
    const/16 v1, 0x30

    if-ne p1, v1, :cond_4

    sget v0, Lmiuix/popupwidget/R$style;->Animation_PopupWindow_ImmersionMenu_Top:I

    goto :goto_0

    :cond_4
    const/16 v1, 0x50

    if-ne p1, v1, :cond_5

    sget v0, Lmiuix/popupwidget/R$style;->Animation_PopupWindow_ImmersionMenu_Bottom:I

    goto :goto_0

    :cond_5
    const/16 v1, 0x11

    if-ne p1, v1, :cond_6

    sget v0, Lmiuix/popupwidget/R$style;->Animation_PopupWindow_ImmersionMenu_Center:I

    :cond_6
    :goto_0
    invoke-super {p0, v0}, Landroid/widget/PopupWindow;->setAnimationStyle(I)V

    return-void
.end method""",
        'replacement': """.method protected setAnimationStyleByGravity(I)V
    .registers 4

    goto :goto_c

    nop

    :goto_0
    goto :goto_17

    :goto_1
    goto :goto_4

    nop

    :goto_2
    const/16 v1, 0x35

    goto :goto_6

    nop

    :goto_3
    return-void

    :goto_4
    const/16 v1, 0x30

    goto :goto_19

    nop

    :goto_5
    if-eq p1, v1, :cond_0

    goto :goto_17

    :cond_0
    goto :goto_16

    nop

    :goto_6
    if-eq p1, v1, :cond_1

    goto :goto_20

    :cond_1
    goto :goto_10

    nop

    :goto_7
    const/16 v1, 0x33

    goto :goto_13

    nop

    :goto_8
    sget v0, Lmiuix/popupwidget/R$style;->Animation_PopupWindow_ImmersionMenu_Bottom:I

    goto :goto_23

    nop

    :goto_9
    goto :goto_17

    :goto_a
    goto :goto_2

    nop

    :goto_b
    const/16 v1, 0x53

    goto :goto_12

    nop

    :goto_c
    sget v0, Lmiuix/popupwidget/R$style;->Animation_PopupWindow_ImmersionMenu:I

    goto :goto_7

    nop

    :goto_d
    const/16 v1, 0x11

    goto :goto_5

    nop

    :goto_e
    sget v0, Lmiuix/popupwidget/R$style;->Animation_PopupWindow_ImmersionMenu_LeftTop:I

    goto :goto_21

    nop

    :goto_f
    invoke-super {p0, v0}, Landroid/widget/PopupWindow;->setAnimationStyle(I)V

    goto :goto_3

    nop

    :goto_10
    sget v0, Lmiuix/popupwidget/R$style;->Animation_PopupWindow_ImmersionMenu_RightTop:I

    goto :goto_1f

    nop

    :goto_11
    if-eq p1, v1, :cond_2

    goto :goto_1

    :cond_2
    goto :goto_1a

    nop

    :goto_12
    if-eq p1, v1, :cond_3

    goto :goto_a

    :cond_3
    goto :goto_1b

    nop

    :goto_13
    if-eq p1, v1, :cond_4

    goto :goto_22

    :cond_4
    goto :goto_e

    nop

    :goto_14
    const/16 v1, 0x50

    goto :goto_18

    nop

    :goto_15
    sget v0, Lmiuix/popupwidget/R$style;->Animation_PopupWindow_ImmersionMenu_Top:I

    goto :goto_1c

    nop

    :goto_16
    sget v0, Lmiuix/popupwidget/R$style;->Animation_PopupWindow_ImmersionMenu_Center:I

    :goto_17
    goto :goto_f

    nop

    :goto_18
    if-eq p1, v1, :cond_5

    goto :goto_24

    :cond_5
    goto :goto_8

    nop

    :goto_19
    if-eq p1, v1, :cond_6

    goto :goto_1d

    :cond_6
    goto :goto_15

    nop

    :goto_1a
    sget v0, Lmiuix/popupwidget/R$style;->Animation_PopupWindow_ImmersionMenu_RightBottom:I

    goto :goto_0

    nop

    :goto_1b
    sget v0, Lmiuix/popupwidget/R$style;->Animation_PopupWindow_ImmersionMenu_LeftBottom:I

    goto :goto_9

    nop

    :goto_1c
    goto :goto_17

    :goto_1d
    goto :goto_14

    nop

    :goto_1e
    const/16 v1, 0x55

    goto :goto_11

    nop

    :goto_1f
    goto :goto_17

    :goto_20
    goto :goto_1e

    nop

    :goto_21
    goto :goto_17

    :goto_22
    goto :goto_b

    nop

    :goto_23
    goto :goto_17

    :goto_24
    goto :goto_d

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_popupwidget_widget_PopupWindow__setPopupShadowAlpha',
        'method': '.method protected setPopupShadowAlpha(Landroid/view/View;)V',
        'method_name': 'setPopupShadowAlpha',
        'method_anchors': ['iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContext:Landroid/content/Context;', 'invoke-static {v0}, Lmiuix/core/util/EnvStateManager;->isFreeFormMode(Landroid/content/Context;)Z', 'if-eqz v0, :cond_0', 'invoke-virtual {p1, p0}, Landroid/view/View;->setOutlineProvider(Landroid/view/ViewOutlineProvider;)V', 'return-void', 'new-instance v0, Lmiuix/popupwidget/widget/PopupWindow$6;', 'invoke-direct {v0, p0}, Lmiuix/popupwidget/widget/PopupWindow$6;-><init>(Lmiuix/popupwidget/widget/PopupWindow;)V', 'invoke-virtual {p1, v0}, Landroid/view/View;->setOutlineProvider(Landroid/view/ViewOutlineProvider;)V'],
        'type': 'method_replace',
        'search': """.method protected setPopupShadowAlpha(Landroid/view/View;)V
    .registers 3

    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContext:Landroid/content/Context;

    invoke-static {v0}, Lmiuix/core/util/EnvStateManager;->isFreeFormMode(Landroid/content/Context;)Z

    move-result v0

    if-eqz v0, :cond_0

    const/4 p0, 0x0

    invoke-virtual {p1, p0}, Landroid/view/View;->setOutlineProvider(Landroid/view/ViewOutlineProvider;)V

    return-void

    :cond_0
    new-instance v0, Lmiuix/popupwidget/widget/PopupWindow$6;

    invoke-direct {v0, p0}, Lmiuix/popupwidget/widget/PopupWindow$6;-><init>(Lmiuix/popupwidget/widget/PopupWindow;)V

    invoke-virtual {p1, v0}, Landroid/view/View;->setOutlineProvider(Landroid/view/ViewOutlineProvider;)V

    iget-object p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContext:Landroid/content/Context;

    sget v0, Lmiuix/popupwidget/R$color;->miuix_appcompat_drop_down_menu_spot_shadow_color:I

    invoke-virtual {p0, v0}, Landroid/content/Context;->getColor(I)I

    move-result p0

    invoke-virtual {p1, p0}, Landroid/view/View;->setOutlineSpotShadowColor(I)V

    return-void
.end method""",
        'replacement': """.method protected setPopupShadowAlpha(Landroid/view/View;)V
    .registers 3

    goto :goto_6

    nop

    :goto_0
    invoke-direct {v0, p0}, Lmiuix/popupwidget/widget/PopupWindow$6;-><init>(Lmiuix/popupwidget/widget/PopupWindow;)V

    goto :goto_d

    nop

    :goto_1
    new-instance v0, Lmiuix/popupwidget/widget/PopupWindow$6;

    goto :goto_0

    nop

    :goto_2
    iget-object p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContext:Landroid/content/Context;

    goto :goto_3

    nop

    :goto_3
    sget v0, Lmiuix/popupwidget/R$color;->miuix_appcompat_drop_down_menu_spot_shadow_color:I

    goto :goto_c

    nop

    :goto_4
    invoke-static {v0}, Lmiuix/core/util/EnvStateManager;->isFreeFormMode(Landroid/content/Context;)Z

    move-result v0

    goto :goto_8

    nop

    :goto_5
    const/4 p0, 0x0

    goto :goto_7

    nop

    :goto_6
    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContext:Landroid/content/Context;

    goto :goto_4

    nop

    :goto_7
    invoke-virtual {p1, p0}, Landroid/view/View;->setOutlineProvider(Landroid/view/ViewOutlineProvider;)V

    goto :goto_a

    nop

    :goto_8
    if-nez v0, :cond_0

    goto :goto_b

    :cond_0
    goto :goto_5

    nop

    :goto_9
    invoke-virtual {p1, p0}, Landroid/view/View;->setOutlineSpotShadowColor(I)V

    goto :goto_e

    nop

    :goto_a
    return-void

    :goto_b
    goto :goto_1

    nop

    :goto_c
    invoke-virtual {p0, v0}, Landroid/content/Context;->getColor(I)I

    move-result p0

    goto :goto_9

    nop

    :goto_d
    invoke-virtual {p1, v0}, Landroid/view/View;->setOutlineProvider(Landroid/view/ViewOutlineProvider;)V

    goto :goto_2

    nop

    :goto_e
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_popupwidget_widget_PopupWindow__shouldSetElevation',
        'method': '.method protected shouldSetElevation()Z',
        'method_name': 'shouldSetElevation',
        'method_anchors': ['iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContext:Landroid/content/Context;', 'const-string v1, "accessibility"', 'invoke-virtual {v0, v1}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;', 'check-cast v0, Landroid/view/accessibility/AccessibilityManager;', 'invoke-virtual {v0}, Landroid/view/accessibility/AccessibilityManager;->isEnabled()Z', 'if-eqz v1, :cond_0', 'invoke-virtual {v0}, Landroid/view/accessibility/AccessibilityManager;->isTouchExplorationEnabled()Z', 'iget-boolean p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mHasShadow:Z'],
        'type': 'method_replace',
        'search': """.method protected shouldSetElevation()Z
    .registers 3

    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContext:Landroid/content/Context;

    const-string v1, "accessibility"

    invoke-virtual {v0, v1}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/view/accessibility/AccessibilityManager;

    invoke-virtual {v0}, Landroid/view/accessibility/AccessibilityManager;->isEnabled()Z

    move-result v1

    if-eqz v1, :cond_0

    invoke-virtual {v0}, Landroid/view/accessibility/AccessibilityManager;->isTouchExplorationEnabled()Z

    move-result v0

    :cond_0
    iget-boolean p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mHasShadow:Z

    if-eqz p0, :cond_1

    const/4 p0, 0x1

    return p0

    :cond_1
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method protected shouldSetElevation()Z
    .registers 3

    goto :goto_7

    nop

    :goto_0
    invoke-virtual {v0}, Landroid/view/accessibility/AccessibilityManager;->isTouchExplorationEnabled()Z

    move-result v0

    :goto_1
    goto :goto_5

    nop

    :goto_2
    if-nez p0, :cond_0

    goto :goto_e

    :cond_0
    goto :goto_6

    nop

    :goto_3
    invoke-virtual {v0}, Landroid/view/accessibility/AccessibilityManager;->isEnabled()Z

    move-result v1

    goto :goto_c

    nop

    :goto_4
    const/4 p0, 0x0

    goto :goto_8

    nop

    :goto_5
    iget-boolean p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mHasShadow:Z

    goto :goto_2

    nop

    :goto_6
    const/4 p0, 0x1

    goto :goto_d

    nop

    :goto_7
    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContext:Landroid/content/Context;

    goto :goto_9

    nop

    :goto_8
    return p0

    :goto_9
    const-string v1, "accessibility"

    goto :goto_b

    nop

    :goto_a
    check-cast v0, Landroid/view/accessibility/AccessibilityManager;

    goto :goto_3

    nop

    :goto_b
    invoke-virtual {v0, v1}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object v0

    goto :goto_a

    nop

    :goto_c
    if-nez v1, :cond_1

    goto :goto_1

    :cond_1
    goto :goto_0

    nop

    :goto_d
    return p0

    :goto_e
    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_popupwidget_widget_PopupWindow__showWithAnim',
        'method': '.method protected showWithAnim(I)V',
        'method_name': 'showWithAnim',
        'method_anchors': ['iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mAnimHelper:Lmiuix/popupwidget/widget/PopupAnimHelper;', 'if-eqz v0, :cond_3', 'iget-boolean v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mWindowAnimationEnabled:Z', 'if-eqz v0, :cond_0', 'iget v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mDimAmount:F', 'if-nez v1, :cond_2', 'iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContext:Landroid/content/Context;', 'invoke-static {v0}, Lmiuix/internal/util/ViewUtils;->isNightMode(Landroid/content/Context;)Z'],
        'type': 'method_replace',
        'search': """.method protected showWithAnim(I)V
    .registers 4

    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mAnimHelper:Lmiuix/popupwidget/widget/PopupAnimHelper;

    if-eqz v0, :cond_3

    iget-boolean v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mWindowAnimationEnabled:Z

    if-eqz v0, :cond_0

    goto :goto_1

    :cond_0
    iget v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mDimAmount:F

    const v1, 0x7f7fffff

    cmpl-float v1, v0, v1

    if-nez v1, :cond_2

    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContext:Landroid/content/Context;

    invoke-static {v0}, Lmiuix/internal/util/ViewUtils;->isNightMode(Landroid/content/Context;)Z

    move-result v0

    if-eqz v0, :cond_1

    sget v0, Lmiuix/theme/token/DimToken;->DIM_DARK:F

    goto :goto_0

    :cond_1
    sget v0, Lmiuix/theme/token/DimToken;->DIM_LIGHT:F

    :cond_2
    :goto_0
    iget-object v1, p0, Lmiuix/popupwidget/widget/PopupWindow;->mAnimHelper:Lmiuix/popupwidget/widget/PopupAnimHelper;

    invoke-virtual {v1, v0}, Lmiuix/popupwidget/widget/PopupAnimHelper;->setDimValue(F)V

    iget-object p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mAnimHelper:Lmiuix/popupwidget/widget/PopupAnimHelper;

    invoke-virtual {p0, p1}, Lmiuix/popupwidget/widget/PopupAnimHelper;->showWithAnim(I)V

    return-void

    :cond_3
    :goto_1
    invoke-virtual {p0, p1}, Lmiuix/popupwidget/widget/PopupWindow;->setAnimationStyleByGravity(I)V

    return-void
.end method""",
        'replacement': """.method protected showWithAnim(I)V
    .registers 4

    goto :goto_12

    nop

    :goto_0
    const v1, 0x7f7fffff

    goto :goto_5

    nop

    :goto_1
    if-nez v0, :cond_0

    goto :goto_d

    :cond_0
    goto :goto_b

    nop

    :goto_2
    if-nez v0, :cond_1

    goto :goto_9

    :cond_1
    goto :goto_13

    nop

    :goto_3
    sget v0, Lmiuix/theme/token/DimToken;->DIM_LIGHT:F

    :goto_4
    goto :goto_10

    nop

    :goto_5
    cmpl-float v1, v0, v1

    goto :goto_19

    nop

    :goto_6
    iget-object p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mAnimHelper:Lmiuix/popupwidget/widget/PopupAnimHelper;

    goto :goto_17

    nop

    :goto_7
    invoke-virtual {v1, v0}, Lmiuix/popupwidget/widget/PopupAnimHelper;->setDimValue(F)V

    goto :goto_6

    nop

    :goto_8
    goto :goto_4

    :goto_9
    goto :goto_3

    nop

    :goto_a
    invoke-virtual {p0, p1}, Lmiuix/popupwidget/widget/PopupWindow;->setAnimationStyleByGravity(I)V

    goto :goto_11

    nop

    :goto_b
    iget-boolean v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mWindowAnimationEnabled:Z

    goto :goto_15

    nop

    :goto_c
    return-void

    :goto_d
    goto :goto_a

    nop

    :goto_e
    goto :goto_d

    :goto_f
    goto :goto_14

    nop

    :goto_10
    iget-object v1, p0, Lmiuix/popupwidget/widget/PopupWindow;->mAnimHelper:Lmiuix/popupwidget/widget/PopupAnimHelper;

    goto :goto_7

    nop

    :goto_11
    return-void

    :goto_12
    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mAnimHelper:Lmiuix/popupwidget/widget/PopupAnimHelper;

    goto :goto_1

    nop

    :goto_13
    sget v0, Lmiuix/theme/token/DimToken;->DIM_DARK:F

    goto :goto_8

    nop

    :goto_14
    iget v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mDimAmount:F

    goto :goto_0

    nop

    :goto_15
    if-nez v0, :cond_2

    goto :goto_f

    :cond_2
    goto :goto_e

    nop

    :goto_16
    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContext:Landroid/content/Context;

    goto :goto_18

    nop

    :goto_17
    invoke-virtual {p0, p1}, Lmiuix/popupwidget/widget/PopupAnimHelper;->showWithAnim(I)V

    goto :goto_c

    nop

    :goto_18
    invoke-static {v0}, Lmiuix/internal/util/ViewUtils;->isNightMode(Landroid/content/Context;)Z

    move-result v0

    goto :goto_2

    nop

    :goto_19
    if-eqz v1, :cond_3

    goto :goto_4

    :cond_3
    goto :goto_16

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_popupwidget_widget_PopupWindow__superSetContentViewWithoutClip',
        'method': '.method protected superSetContentViewWithoutClip(Landroid/view/View;)V',
        'method_name': 'superSetContentViewWithoutClip',
        'method_anchors': ['iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mRootView:Landroid/widget/FrameLayout;', 'invoke-virtual {v0}, Landroid/widget/FrameLayout;->removeAllViews()V', 'iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mRootView:Landroid/widget/FrameLayout;', 'invoke-virtual {v0, p1}, Landroid/widget/FrameLayout;->addView(Landroid/view/View;)V', 'iput-object p1, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContentView:Landroid/view/View;', 'iget-object p1, p0, Lmiuix/popupwidget/widget/PopupWindow;->mRootView:Landroid/widget/FrameLayout;', 'invoke-super {p0, p1}, Landroid/widget/PopupWindow;->setContentView(Landroid/view/View;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected superSetContentViewWithoutClip(Landroid/view/View;)V
    .registers 3

    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mRootView:Landroid/widget/FrameLayout;

    invoke-virtual {v0}, Landroid/widget/FrameLayout;->removeAllViews()V

    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mRootView:Landroid/widget/FrameLayout;

    invoke-virtual {v0, p1}, Landroid/widget/FrameLayout;->addView(Landroid/view/View;)V

    iput-object p1, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContentView:Landroid/view/View;

    iget-object p1, p0, Lmiuix/popupwidget/widget/PopupWindow;->mRootView:Landroid/widget/FrameLayout;

    invoke-super {p0, p1}, Landroid/widget/PopupWindow;->setContentView(Landroid/view/View;)V

    return-void
.end method""",
        'replacement': """.method protected superSetContentViewWithoutClip(Landroid/view/View;)V
    .registers 3

    goto :goto_5

    nop

    :goto_0
    iput-object p1, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContentView:Landroid/view/View;

    goto :goto_4

    nop

    :goto_1
    invoke-virtual {v0}, Landroid/widget/FrameLayout;->removeAllViews()V

    goto :goto_2

    nop

    :goto_2
    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mRootView:Landroid/widget/FrameLayout;

    goto :goto_7

    nop

    :goto_3
    invoke-super {p0, p1}, Landroid/widget/PopupWindow;->setContentView(Landroid/view/View;)V

    goto :goto_6

    nop

    :goto_4
    iget-object p1, p0, Lmiuix/popupwidget/widget/PopupWindow;->mRootView:Landroid/widget/FrameLayout;

    goto :goto_3

    nop

    :goto_5
    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mRootView:Landroid/widget/FrameLayout;

    goto :goto_1

    nop

    :goto_6
    return-void

    :goto_7
    invoke-virtual {v0, p1}, Landroid/widget/FrameLayout;->addView(Landroid/view/View;)V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_popupwidget_widget_PopupWindow__superShowAtLocation',
        'method': '.method protected superShowAtLocation(Landroid/view/View;III)V',
        'method_name': 'superShowAtLocation',
        'method_anchors': ['invoke-super {p0, p1, p2, p3, p4}, Landroid/widget/PopupWindow;->showAtLocation(Landroid/view/View;III)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected superShowAtLocation(Landroid/view/View;III)V
    .registers 5

    invoke-super {p0, p1, p2, p3, p4}, Landroid/widget/PopupWindow;->showAtLocation(Landroid/view/View;III)V

    return-void
.end method""",
        'replacement': """.method protected superShowAtLocation(Landroid/view/View;III)V
    .registers 5

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0, p1, p2, p3, p4}, Landroid/widget/PopupWindow;->showAtLocation(Landroid/view/View;III)V

    goto :goto_1

    nop

    :goto_1
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_popupwidget_widget_PopupWindow__updateLocation',
        'method': '.method protected updateLocation(Landroid/view/View;)V',
        'method_name': 'updateLocation',
        'method_anchors': ['invoke-virtual {p0}, Landroid/widget/PopupWindow;->isShowing()Z', 'if-eqz v0, :cond_0', 'invoke-virtual {p0}, Lmiuix/popupwidget/widget/PopupWindow;->computePopupContentSize()V', 'iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;', 'iget-object v0, v0, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mAnchorViewBounds:Landroid/graphics/Rect;', 'invoke-static {p1, v0}, Lmiuix/internal/util/ViewUtils;->getBoundsInWindow(Landroid/view/View;Landroid/graphics/Rect;)V', 'iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowStrategy:Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;', 'iget-object v1, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;'],
        'type': 'method_replace',
        'search': """.method protected updateLocation(Landroid/view/View;)V
    .registers 7

    invoke-virtual {p0}, Landroid/widget/PopupWindow;->isShowing()Z

    move-result v0

    if-eqz v0, :cond_0

    invoke-virtual {p0}, Lmiuix/popupwidget/widget/PopupWindow;->computePopupContentSize()V

    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    iget-object v0, v0, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mAnchorViewBounds:Landroid/graphics/Rect;

    invoke-static {p1, v0}, Lmiuix/internal/util/ViewUtils;->getBoundsInWindow(Landroid/view/View;Landroid/graphics/Rect;)V

    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowStrategy:Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;

    iget-object v1, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    invoke-interface {v0, v1}, Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;->getXInWindow(Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;)I

    move-result v0

    iget-object v1, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowStrategy:Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;

    iget-object v2, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    invoke-interface {v1, v2}, Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;->getYInWindow(Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;)I

    move-result v1

    iget-object v2, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    iget v2, v2, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mFinalPopupWidth:I

    invoke-virtual {p0, v2}, Landroid/widget/PopupWindow;->setWidth(I)V

    iget-object v2, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    iget v2, v2, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mFinalPopupHeight:I

    invoke-virtual {p0, v2}, Landroid/widget/PopupWindow;->setHeight(I)V

    iget-object v2, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    iget v3, v2, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mFinalPopupWidth:I

    iget v2, v2, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mFinalPopupHeight:I

    invoke-virtual {p0, v0, v1, v3, v2}, Landroid/widget/PopupWindow;->update(IIII)V

    iget-object v2, p0, Lmiuix/popupwidget/widget/PopupWindow;->mAnimHelper:Lmiuix/popupwidget/widget/PopupAnimHelper;

    if-eqz v2, :cond_0

    new-instance v2, Landroid/graphics/Rect;

    iget-object v3, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    iget v4, v3, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mFinalPopupWidth:I

    add-int/2addr v4, v0

    iget v3, v3, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mFinalPopupHeight:I

    add-int/2addr v3, v1

    invoke-direct {v2, v0, v1, v4, v3}, Landroid/graphics/Rect;-><init>(IIII)V

    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    iget-object v0, v0, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mAnchorViewBounds:Landroid/graphics/Rect;

    const/4 v1, 0x0

    invoke-virtual {p1}, Landroid/view/View;->getLayoutDirection()I

    move-result p1

    invoke-static {v0, v2, v1, p1}, Lmiuix/popupwidget/widget/PopupWindow;->computeGravity(Landroid/graphics/Rect;Landroid/graphics/Rect;II)I

    move-result p1

    iget-object p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mAnimHelper:Lmiuix/popupwidget/widget/PopupAnimHelper;

    invoke-virtual {p0, p1}, Lmiuix/popupwidget/widget/PopupAnimHelper;->update(I)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected updateLocation(Landroid/view/View;)V
    .registers 7

    goto :goto_16

    nop

    :goto_0
    iget-object v0, v0, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mAnchorViewBounds:Landroid/graphics/Rect;

    goto :goto_9

    nop

    :goto_1
    invoke-interface {v1, v2}, Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;->getYInWindow(Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;)I

    move-result v1

    goto :goto_6

    nop

    :goto_2
    invoke-virtual {p1}, Landroid/view/View;->getLayoutDirection()I

    move-result p1

    goto :goto_17

    nop

    :goto_3
    iget-object v0, v0, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mAnchorViewBounds:Landroid/graphics/Rect;

    goto :goto_c

    nop

    :goto_4
    add-int/2addr v3, v1

    goto :goto_1a

    nop

    :goto_5
    if-nez v0, :cond_0

    goto :goto_1c

    :cond_0
    goto :goto_14

    nop

    :goto_6
    iget-object v2, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    goto :goto_1e

    nop

    :goto_7
    iget-object v2, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    goto :goto_20

    nop

    :goto_8
    iget-object v2, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    goto :goto_1

    nop

    :goto_9
    invoke-static {p1, v0}, Lmiuix/internal/util/ViewUtils;->getBoundsInWindow(Landroid/view/View;Landroid/graphics/Rect;)V

    goto :goto_25

    nop

    :goto_a
    iget v4, v3, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mFinalPopupWidth:I

    goto :goto_1d

    nop

    :goto_b
    iget-object v1, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowStrategy:Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;

    goto :goto_8

    nop

    :goto_c
    const/4 v1, 0x0

    goto :goto_2

    nop

    :goto_d
    invoke-virtual {p0, v2}, Landroid/widget/PopupWindow;->setWidth(I)V

    goto :goto_19

    nop

    :goto_e
    iget-object p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mAnimHelper:Lmiuix/popupwidget/widget/PopupAnimHelper;

    goto :goto_1b

    nop

    :goto_f
    iget v2, v2, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mFinalPopupHeight:I

    goto :goto_27

    nop

    :goto_10
    iget-object v1, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    goto :goto_24

    nop

    :goto_11
    iget v3, v3, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mFinalPopupHeight:I

    goto :goto_4

    nop

    :goto_12
    iget-object v2, p0, Lmiuix/popupwidget/widget/PopupWindow;->mAnimHelper:Lmiuix/popupwidget/widget/PopupAnimHelper;

    goto :goto_1f

    nop

    :goto_13
    new-instance v2, Landroid/graphics/Rect;

    goto :goto_23

    nop

    :goto_14
    invoke-virtual {p0}, Lmiuix/popupwidget/widget/PopupWindow;->computePopupContentSize()V

    goto :goto_15

    nop

    :goto_15
    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    goto :goto_0

    nop

    :goto_16
    invoke-virtual {p0}, Landroid/widget/PopupWindow;->isShowing()Z

    move-result v0

    goto :goto_5

    nop

    :goto_17
    invoke-static {v0, v2, v1, p1}, Lmiuix/popupwidget/widget/PopupWindow;->computeGravity(Landroid/graphics/Rect;Landroid/graphics/Rect;II)I

    move-result p1

    goto :goto_e

    nop

    :goto_18
    iget v2, v2, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mFinalPopupHeight:I

    goto :goto_21

    nop

    :goto_19
    iget-object v2, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    goto :goto_18

    nop

    :goto_1a
    invoke-direct {v2, v0, v1, v4, v3}, Landroid/graphics/Rect;-><init>(IIII)V

    goto :goto_26

    nop

    :goto_1b
    invoke-virtual {p0, p1}, Lmiuix/popupwidget/widget/PopupAnimHelper;->update(I)V

    :goto_1c
    goto :goto_22

    nop

    :goto_1d
    add-int/2addr v4, v0

    goto :goto_11

    nop

    :goto_1e
    iget v2, v2, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mFinalPopupWidth:I

    goto :goto_d

    nop

    :goto_1f
    if-nez v2, :cond_1

    goto :goto_1c

    :cond_1
    goto :goto_13

    nop

    :goto_20
    iget v3, v2, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mFinalPopupWidth:I

    goto :goto_f

    nop

    :goto_21
    invoke-virtual {p0, v2}, Landroid/widget/PopupWindow;->setHeight(I)V

    goto :goto_7

    nop

    :goto_22
    return-void

    :goto_23
    iget-object v3, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    goto :goto_a

    nop

    :goto_24
    invoke-interface {v0, v1}, Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;->getXInWindow(Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;)I

    move-result v0

    goto :goto_b

    nop

    :goto_25
    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowStrategy:Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;

    goto :goto_10

    nop

    :goto_26
    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    goto :goto_3

    nop

    :goto_27
    invoke-virtual {p0, v0, v1, v3, v2}, Landroid/widget/PopupWindow;->update(IIII)V

    goto :goto_12

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_popupwidget_widget_PopupWindow__updateSafeInsets',
        'method': '.method protected updateSafeInsets(Landroid/view/View;)Landroid/graphics/Rect;',
        'method_name': 'updateSafeInsets',
        'method_anchors': ['iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContext:Landroid/content/Context;', 'iget p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mMinSafeInsetDimen:I', 'invoke-static {v0, p1, p0}, Lmiuix/popupwidget/widget/PopupWindow;->updateSafeInsetsByDecor(Landroid/content/Context;Landroid/view/View;I)Landroid/graphics/Rect;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected updateSafeInsets(Landroid/view/View;)Landroid/graphics/Rect;
    .registers 3

    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContext:Landroid/content/Context;

    iget p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mMinSafeInsetDimen:I

    invoke-static {v0, p1, p0}, Lmiuix/popupwidget/widget/PopupWindow;->updateSafeInsetsByDecor(Landroid/content/Context;Landroid/view/View;I)Landroid/graphics/Rect;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected updateSafeInsets(Landroid/view/View;)Landroid/graphics/Rect;
    .registers 3

    goto :goto_0

    nop

    :goto_0
    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContext:Landroid/content/Context;

    goto :goto_2

    nop

    :goto_1
    invoke-static {v0, p1, p0}, Lmiuix/popupwidget/widget/PopupWindow;->updateSafeInsetsByDecor(Landroid/content/Context;Landroid/view/View;I)Landroid/graphics/Rect;

    move-result-object p0

    goto :goto_3

    nop

    :goto_2
    iget p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mMinSafeInsetDimen:I

    goto :goto_1

    nop

    :goto_3
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
