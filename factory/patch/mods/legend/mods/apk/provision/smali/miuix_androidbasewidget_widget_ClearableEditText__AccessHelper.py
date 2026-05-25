TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/androidbasewidget/widget/ClearableEditText$AccessHelper.smali'
CLASS_FALLBACK_NAMES = ['ClearableEditText$AccessHelper.smali']
CLASS_ANCHORS = ['.super Landroidx/customview/widget/ExploreByTouchHelper;']

PATCHES = [
    {
        'id': 'miuix_androidbasewidget_widget_ClearableEditText__AccessHelper__getVirtualViewAt',
        'method': '.method protected getVirtualViewAt(FF)I',
        'method_name': 'getVirtualViewAt',
        'method_anchors': ['iget-object v0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->this$0:Lmiuix/androidbasewidget/widget/ClearableEditText;', 'invoke-static {v0}, Lmiuix/androidbasewidget/widget/ClearableEditText;->access$000(Lmiuix/androidbasewidget/widget/ClearableEditText;)Z', 'if-eqz v0, :cond_0', 'invoke-direct {p0, p1, p2}, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->isVirtualView(FF)Z', 'if-eqz p0, :cond_0', 'return p0', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected getVirtualViewAt(FF)I
    .registers 4

    iget-object v0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->this$0:Lmiuix/androidbasewidget/widget/ClearableEditText;

    invoke-static {v0}, Lmiuix/androidbasewidget/widget/ClearableEditText;->access$000(Lmiuix/androidbasewidget/widget/ClearableEditText;)Z

    move-result v0

    if-eqz v0, :cond_0

    invoke-direct {p0, p1, p2}, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->isVirtualView(FF)Z

    move-result p0

    if-eqz p0, :cond_0

    const/4 p0, 0x0

    return p0

    :cond_0
    const/high16 p0, -0x80000000

    return p0
.end method""",
        'replacement': """.method protected getVirtualViewAt(FF)I
    .registers 4

    goto :goto_4

    nop

    :goto_0
    invoke-static {v0}, Lmiuix/androidbasewidget/widget/ClearableEditText;->access$000(Lmiuix/androidbasewidget/widget/ClearableEditText;)Z

    move-result v0

    goto :goto_9

    nop

    :goto_1
    invoke-direct {p0, p1, p2}, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->isVirtualView(FF)Z

    move-result p0

    goto :goto_5

    nop

    :goto_2
    return p0

    :goto_3
    goto :goto_8

    nop

    :goto_4
    iget-object v0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->this$0:Lmiuix/androidbasewidget/widget/ClearableEditText;

    goto :goto_0

    nop

    :goto_5
    if-nez p0, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_7

    nop

    :goto_6
    return p0

    :goto_7
    const/4 p0, 0x0

    goto :goto_2

    nop

    :goto_8
    const/high16 p0, -0x80000000

    goto :goto_6

    nop

    :goto_9
    if-nez v0, :cond_1

    goto :goto_3

    :cond_1
    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_androidbasewidget_widget_ClearableEditText__AccessHelper__getVisibleVirtualViews',
        'method': '.method protected getVisibleVirtualViews(Ljava/util/List;)V',
        'method_name': 'getVisibleVirtualViews',
        'method_anchors': ['iget-object p0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->this$0:Lmiuix/androidbasewidget/widget/ClearableEditText;', 'invoke-static {p0}, Lmiuix/androidbasewidget/widget/ClearableEditText;->access$000(Lmiuix/androidbasewidget/widget/ClearableEditText;)Z', 'if-eqz p0, :cond_0', 'invoke-static {p0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;', 'invoke-interface {p1, p0}, Ljava/util/List;->add(Ljava/lang/Object;)Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected getVisibleVirtualViews(Ljava/util/List;)V
    .registers 2

    iget-object p0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->this$0:Lmiuix/androidbasewidget/widget/ClearableEditText;

    invoke-static {p0}, Lmiuix/androidbasewidget/widget/ClearableEditText;->access$000(Lmiuix/androidbasewidget/widget/ClearableEditText;)Z

    move-result p0

    if-eqz p0, :cond_0

    const/4 p0, 0x0

    invoke-static {p0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p0

    invoke-interface {p1, p0}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected getVisibleVirtualViews(Ljava/util/List;)V
    .registers 2

    goto :goto_4

    nop

    :goto_0
    return-void

    :goto_1
    const/4 p0, 0x0

    goto :goto_7

    nop

    :goto_2
    invoke-static {p0}, Lmiuix/androidbasewidget/widget/ClearableEditText;->access$000(Lmiuix/androidbasewidget/widget/ClearableEditText;)Z

    move-result p0

    goto :goto_3

    nop

    :goto_3
    if-nez p0, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_1

    nop

    :goto_4
    iget-object p0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->this$0:Lmiuix/androidbasewidget/widget/ClearableEditText;

    goto :goto_2

    nop

    :goto_5
    invoke-interface {p1, p0}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    :goto_6
    goto :goto_0

    nop

    :goto_7
    invoke-static {p0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p0

    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_androidbasewidget_widget_ClearableEditText__AccessHelper__onPerformActionForVirtualView',
        'method': '.method protected onPerformActionForVirtualView(IILandroid/os/Bundle;)Z',
        'method_name': 'onPerformActionForVirtualView',
        'method_anchors': ['if-ne p1, p3, :cond_0', 'return v0', 'if-eq p2, p1, :cond_1', 'return v0', 'iget-object p1, p0, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->this$0:Lmiuix/androidbasewidget/widget/ClearableEditText;', 'invoke-static {p1}, Lmiuix/androidbasewidget/widget/ClearableEditText;->access$100(Lmiuix/androidbasewidget/widget/ClearableEditText;)V', 'iget-object p1, p0, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->forView:Landroid/view/View;', 'if-eqz p1, :cond_2'],
        'type': 'method_replace',
        'search': """.method protected onPerformActionForVirtualView(IILandroid/os/Bundle;)Z
    .registers 5

    const/high16 p3, -0x80000000

    const/4 v0, 0x0

    if-ne p1, p3, :cond_0

    return v0

    :cond_0
    const/16 p1, 0x10

    if-eq p2, p1, :cond_1

    return v0

    :cond_1
    iget-object p1, p0, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->this$0:Lmiuix/androidbasewidget/widget/ClearableEditText;

    invoke-static {p1}, Lmiuix/androidbasewidget/widget/ClearableEditText;->access$100(Lmiuix/androidbasewidget/widget/ClearableEditText;)V

    iget-object p1, p0, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->forView:Landroid/view/View;

    if-eqz p1, :cond_2

    iget-object p2, p0, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->this$0:Lmiuix/androidbasewidget/widget/ClearableEditText;

    invoke-virtual {p1}, Landroid/view/View;->getContext()Landroid/content/Context;

    move-result-object p1

    invoke-virtual {p2, p1}, Lmiuix/androidbasewidget/widget/ClearableEditText;->isTalkBackActive(Landroid/content/Context;)Z

    move-result p1

    if-eqz p1, :cond_2

    iget-object p0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->forView:Landroid/view/View;

    const p1, 0x8000

    invoke-virtual {p0, p1}, Landroid/view/View;->sendAccessibilityEvent(I)V

    :cond_2
    const/4 p0, 0x1

    return p0
.end method""",
        'replacement': """.method protected onPerformActionForVirtualView(IILandroid/os/Bundle;)Z
    .registers 5

    goto :goto_15

    nop

    :goto_0
    if-ne p2, p1, :cond_0

    goto :goto_14

    :cond_0
    goto :goto_13

    nop

    :goto_1
    if-nez p1, :cond_1

    goto :goto_8

    :cond_1
    goto :goto_d

    nop

    :goto_2
    if-nez p1, :cond_2

    goto :goto_8

    :cond_2
    goto :goto_9

    nop

    :goto_3
    iget-object p1, p0, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->forView:Landroid/view/View;

    goto :goto_1

    nop

    :goto_4
    const/16 p1, 0x10

    goto :goto_0

    nop

    :goto_5
    const/4 p0, 0x1

    goto :goto_11

    nop

    :goto_6
    invoke-virtual {p2, p1}, Lmiuix/androidbasewidget/widget/ClearableEditText;->isTalkBackActive(Landroid/content/Context;)Z

    move-result p1

    goto :goto_2

    nop

    :goto_7
    invoke-virtual {p0, p1}, Landroid/view/View;->sendAccessibilityEvent(I)V

    :goto_8
    goto :goto_5

    nop

    :goto_9
    iget-object p0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->forView:Landroid/view/View;

    goto :goto_f

    nop

    :goto_a
    return v0

    :goto_b
    goto :goto_4

    nop

    :goto_c
    invoke-virtual {p1}, Landroid/view/View;->getContext()Landroid/content/Context;

    move-result-object p1

    goto :goto_6

    nop

    :goto_d
    iget-object p2, p0, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->this$0:Lmiuix/androidbasewidget/widget/ClearableEditText;

    goto :goto_c

    nop

    :goto_e
    iget-object p1, p0, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->this$0:Lmiuix/androidbasewidget/widget/ClearableEditText;

    goto :goto_10

    nop

    :goto_f
    const p1, 0x8000

    goto :goto_7

    nop

    :goto_10
    invoke-static {p1}, Lmiuix/androidbasewidget/widget/ClearableEditText;->access$100(Lmiuix/androidbasewidget/widget/ClearableEditText;)V

    goto :goto_3

    nop

    :goto_11
    return p0

    :goto_12
    if-eq p1, p3, :cond_3

    goto :goto_b

    :cond_3
    goto :goto_a

    nop

    :goto_13
    return v0

    :goto_14
    goto :goto_e

    nop

    :goto_15
    const/high16 p3, -0x80000000

    goto :goto_16

    nop

    :goto_16
    const/4 v0, 0x0

    goto :goto_12

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_androidbasewidget_widget_ClearableEditText__AccessHelper__onPopulateEventForVirtualView',
        'method': '.method protected onPopulateEventForVirtualView(ILandroid/view/accessibility/AccessibilityEvent;)V',
        'method_name': 'onPopulateEventForVirtualView',
        'method_anchors': ['invoke-direct {p0}, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->getDescription()Ljava/lang/CharSequence;', 'invoke-virtual {p2, p0}, Landroid/view/accessibility/AccessibilityEvent;->setContentDescription(Ljava/lang/CharSequence;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onPopulateEventForVirtualView(ILandroid/view/accessibility/AccessibilityEvent;)V
    .registers 3

    invoke-direct {p0}, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->getDescription()Ljava/lang/CharSequence;

    move-result-object p0

    invoke-virtual {p2, p0}, Landroid/view/accessibility/AccessibilityEvent;->setContentDescription(Ljava/lang/CharSequence;)V

    return-void
.end method""",
        'replacement': """.method protected onPopulateEventForVirtualView(ILandroid/view/accessibility/AccessibilityEvent;)V
    .registers 3

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    invoke-direct {p0}, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->getDescription()Ljava/lang/CharSequence;

    move-result-object p0

    goto :goto_2

    nop

    :goto_2
    invoke-virtual {p2, p0}, Landroid/view/accessibility/AccessibilityEvent;->setContentDescription(Ljava/lang/CharSequence;)V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_androidbasewidget_widget_ClearableEditText__AccessHelper__onPopulateNodeForHost',
        'method': '.method protected onPopulateNodeForHost(Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;)V',
        'method_name': 'onPopulateNodeForHost',
        'method_anchors': ['invoke-super {p0, p1}, Landroidx/customview/widget/ExploreByTouchHelper;->onPopulateNodeForHost(Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;)V', 'iget-object p0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->this$0:Lmiuix/androidbasewidget/widget/ClearableEditText;', 'invoke-static {p0}, Lmiuix/androidbasewidget/widget/ClearableEditText;->access$000(Lmiuix/androidbasewidget/widget/ClearableEditText;)Z', 'if-eqz p0, :cond_0', 'invoke-virtual {p0}, Ljava/lang/Class;->getName()Ljava/lang/String;', 'invoke-virtual {p1, p0}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setClassName(Ljava/lang/CharSequence;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onPopulateNodeForHost(Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;)V
    .registers 2

    invoke-super {p0, p1}, Landroidx/customview/widget/ExploreByTouchHelper;->onPopulateNodeForHost(Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;)V

    iget-object p0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->this$0:Lmiuix/androidbasewidget/widget/ClearableEditText;

    invoke-static {p0}, Lmiuix/androidbasewidget/widget/ClearableEditText;->access$000(Lmiuix/androidbasewidget/widget/ClearableEditText;)Z

    move-result p0

    if-eqz p0, :cond_0

    const-class p0, Lmiuix/androidbasewidget/widget/ClearableEditText;

    invoke-virtual {p0}, Ljava/lang/Class;->getName()Ljava/lang/String;

    move-result-object p0

    invoke-virtual {p1, p0}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setClassName(Ljava/lang/CharSequence;)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onPopulateNodeForHost(Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;)V
    .registers 2

    goto :goto_7

    nop

    :goto_0
    invoke-static {p0}, Lmiuix/androidbasewidget/widget/ClearableEditText;->access$000(Lmiuix/androidbasewidget/widget/ClearableEditText;)Z

    move-result p0

    goto :goto_2

    nop

    :goto_1
    return-void

    :goto_2
    if-nez p0, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_8

    nop

    :goto_3
    iget-object p0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->this$0:Lmiuix/androidbasewidget/widget/ClearableEditText;

    goto :goto_0

    nop

    :goto_4
    invoke-virtual {p0}, Ljava/lang/Class;->getName()Ljava/lang/String;

    move-result-object p0

    goto :goto_5

    nop

    :goto_5
    invoke-virtual {p1, p0}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setClassName(Ljava/lang/CharSequence;)V

    :goto_6
    goto :goto_1

    nop

    :goto_7
    invoke-super {p0, p1}, Landroidx/customview/widget/ExploreByTouchHelper;->onPopulateNodeForHost(Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;)V

    goto :goto_3

    nop

    :goto_8
    const-class p0, Lmiuix/androidbasewidget/widget/ClearableEditText;

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_androidbasewidget_widget_ClearableEditText__AccessHelper__onPopulateNodeForVirtualView',
        'method': '.method protected onPopulateNodeForVirtualView(ILandroidx/core/view/accessibility/AccessibilityNodeInfoCompat;)V',
        'method_name': 'onPopulateNodeForVirtualView',
        'method_anchors': ['invoke-virtual {p2, p1}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setVisibleToUser(Z)V', 'invoke-direct {p0}, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->getDescription()Ljava/lang/CharSequence;', 'invoke-virtual {p2, v0}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setContentDescription(Ljava/lang/CharSequence;)V', 'invoke-virtual {p2, v0}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->addAction(I)V', 'invoke-virtual {v0}, Ljava/lang/Class;->getName()Ljava/lang/String;', 'invoke-virtual {p2, v0}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setClassName(Ljava/lang/CharSequence;)V', 'iget-object v0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->mTempParentBounds:Landroid/graphics/Rect;', 'invoke-direct {p0, v0}, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->getChildRect(Landroid/graphics/Rect;)V'],
        'type': 'method_replace',
        'search': """.method protected onPopulateNodeForVirtualView(ILandroidx/core/view/accessibility/AccessibilityNodeInfoCompat;)V
    .registers 4

    const/4 p1, 0x1

    invoke-virtual {p2, p1}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setVisibleToUser(Z)V

    invoke-direct {p0}, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->getDescription()Ljava/lang/CharSequence;

    move-result-object v0

    invoke-virtual {p2, v0}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setContentDescription(Ljava/lang/CharSequence;)V

    const/16 v0, 0x10

    invoke-virtual {p2, v0}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->addAction(I)V

    const-class v0, Landroid/widget/Button;

    invoke-virtual {v0}, Ljava/lang/Class;->getName()Ljava/lang/String;

    move-result-object v0

    invoke-virtual {p2, v0}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setClassName(Ljava/lang/CharSequence;)V

    iget-object v0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->mTempParentBounds:Landroid/graphics/Rect;

    invoke-direct {p0, v0}, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->getChildRect(Landroid/graphics/Rect;)V

    iget-object p0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->mTempParentBounds:Landroid/graphics/Rect;

    invoke-virtual {p2, p0}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setBoundsInParent(Landroid/graphics/Rect;)V

    invoke-virtual {p2, p1}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setClickable(Z)V

    return-void
.end method""",
        'replacement': """.method protected onPopulateNodeForVirtualView(ILandroidx/core/view/accessibility/AccessibilityNodeInfoCompat;)V
    .registers 4

    goto :goto_3

    nop

    :goto_0
    const-class v0, Landroid/widget/Button;

    goto :goto_1

    nop

    :goto_1
    invoke-virtual {v0}, Ljava/lang/Class;->getName()Ljava/lang/String;

    move-result-object v0

    goto :goto_b

    nop

    :goto_2
    invoke-direct {p0}, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->getDescription()Ljava/lang/CharSequence;

    move-result-object v0

    goto :goto_5

    nop

    :goto_3
    const/4 p1, 0x1

    goto :goto_4

    nop

    :goto_4
    invoke-virtual {p2, p1}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setVisibleToUser(Z)V

    goto :goto_2

    nop

    :goto_5
    invoke-virtual {p2, v0}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setContentDescription(Ljava/lang/CharSequence;)V

    goto :goto_c

    nop

    :goto_6
    invoke-virtual {p2, v0}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->addAction(I)V

    goto :goto_0

    nop

    :goto_7
    invoke-direct {p0, v0}, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->getChildRect(Landroid/graphics/Rect;)V

    goto :goto_a

    nop

    :goto_8
    invoke-virtual {p2, p1}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setClickable(Z)V

    goto :goto_e

    nop

    :goto_9
    invoke-virtual {p2, p0}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setBoundsInParent(Landroid/graphics/Rect;)V

    goto :goto_8

    nop

    :goto_a
    iget-object p0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->mTempParentBounds:Landroid/graphics/Rect;

    goto :goto_9

    nop

    :goto_b
    invoke-virtual {p2, v0}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setClassName(Ljava/lang/CharSequence;)V

    goto :goto_d

    nop

    :goto_c
    const/16 v0, 0x10

    goto :goto_6

    nop

    :goto_d
    iget-object v0, p0, Lmiuix/androidbasewidget/widget/ClearableEditText$AccessHelper;->mTempParentBounds:Landroid/graphics/Rect;

    goto :goto_7

    nop

    :goto_e
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
