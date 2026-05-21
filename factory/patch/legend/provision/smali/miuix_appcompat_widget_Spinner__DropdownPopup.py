TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/widget/Spinner$DropdownPopup.smali'
CLASS_FALLBACK_NAMES = ['Spinner$DropdownPopup.smali']
CLASS_ANCHORS = ['.super Lmiuix/popupwidget/widget/PopupWindow;', '.implements Lmiuix/appcompat/widget/Spinner$SpinnerPopup;']

PATCHES = [
    {
        'id': 'miuix_appcompat_widget_Spinner__DropdownPopup__getItemViewBounds',
        'method': '.method protected getItemViewBounds(Landroid/widget/ListAdapter;Landroid/view/ViewGroup;Landroid/content/Context;)[[I',
        'method_name': 'getItemViewBounds',
        'method_anchors': ['if-eqz p1, :cond_1', 'invoke-virtual {p0}, Lmiuix/popupwidget/widget/PopupWindow;->getListView()Landroid/widget/ListView;', 'invoke-interface {p1}, Landroid/widget/ListAdapter;->getCount()I', 'invoke-static {v3, v4}, Ljava/lang/Math;->min(II)I', 'sget-object p3, Ljava/lang/Integer;->TYPE:Ljava/lang/Class;', 'invoke-static {p3, v4}, Ljava/lang/reflect/Array;->newInstance(Ljava/lang/Class;[I)Ljava/lang/Object;', 'check-cast p3, [[I', 'if-ge v4, v3, :cond_0'],
        'type': 'method_replace',
        'search': """.method protected getItemViewBounds(Landroid/widget/ListAdapter;Landroid/view/ViewGroup;Landroid/content/Context;)[[I
    .registers 12

    const/high16 p2, -0x80000000

    const/4 p3, 0x2

    const/4 v0, 0x1

    const/4 v1, 0x0

    if-eqz p1, :cond_1

    invoke-virtual {p0}, Lmiuix/popupwidget/widget/PopupWindow;->getListView()Landroid/widget/ListView;

    move-result-object v2

    invoke-interface {p1}, Landroid/widget/ListAdapter;->getCount()I

    move-result v3

    const/16 v4, 0x8

    invoke-static {v3, v4}, Ljava/lang/Math;->min(II)I

    move-result v3

    new-array v4, p3, [I

    aput p3, v4, v0

    aput v3, v4, v1

    sget-object p3, Ljava/lang/Integer;->TYPE:Ljava/lang/Class;

    invoke-static {p3, v4}, Ljava/lang/reflect/Array;->newInstance(Ljava/lang/Class;[I)Ljava/lang/Object;

    move-result-object p3

    check-cast p3, [[I

    move v4, v1

    :goto_0
    if-ge v4, v3, :cond_0

    const/4 v5, 0x0

    invoke-interface {p1, v4, v5, v2}, Landroid/widget/ListAdapter;->getView(ILandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;

    move-result-object v5

    iget-object v6, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    iget v6, v6, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mMaxWidth:I

    invoke-static {v6, p2}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v6

    invoke-static {v1, v1}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v7

    invoke-virtual {v5, v6, v7}, Landroid/view/View;->measure(II)V

    aget-object v6, p3, v4

    invoke-virtual {v5}, Landroid/view/View;->getMeasuredWidth()I

    move-result v7

    aput v7, v6, v1

    aget-object v6, p3, v4

    invoke-virtual {v5}, Landroid/view/View;->getMeasuredHeight()I

    move-result v5

    aput v5, v6, v0

    add-int/lit8 v4, v4, 0x1

    goto :goto_0

    :cond_0
    return-object p3

    :cond_1
    iget-object p1, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContentView:Landroid/view/View;

    iget-object v2, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    iget v2, v2, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mMaxWidth:I

    invoke-static {v2, p2}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p2

    invoke-static {v1, v1}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v2

    invoke-virtual {p1, p2, v2}, Landroid/view/View;->measure(II)V

    new-array p1, p3, [I

    aput p3, p1, v0

    aput v0, p1, v1

    sget-object p2, Ljava/lang/Integer;->TYPE:Ljava/lang/Class;

    invoke-static {p2, p1}, Ljava/lang/reflect/Array;->newInstance(Ljava/lang/Class;[I)Ljava/lang/Object;

    move-result-object p1

    check-cast p1, [[I

    aget-object p2, p1, v1

    iget-object p3, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContentView:Landroid/view/View;

    invoke-virtual {p3}, Landroid/view/View;->getMeasuredWidth()I

    move-result p3

    aput p3, p2, v1

    aget-object p2, p1, v1

    iget-object p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContentView:Landroid/view/View;

    invoke-virtual {p0}, Landroid/view/View;->getMeasuredHeight()I

    move-result p0

    aput p0, p2, v0

    return-object p1
.end method""",
        'replacement': """.method protected getItemViewBounds(Landroid/widget/ListAdapter;Landroid/view/ViewGroup;Landroid/content/Context;)[[I
    .registers 12

    goto :goto_12

    nop

    :goto_0
    invoke-virtual {p0}, Lmiuix/popupwidget/widget/PopupWindow;->getListView()Landroid/widget/ListView;

    move-result-object v2

    goto :goto_e

    nop

    :goto_1
    invoke-virtual {v5}, Landroid/view/View;->getMeasuredHeight()I

    move-result v5

    goto :goto_2f

    nop

    :goto_2
    invoke-static {v3, v4}, Ljava/lang/Math;->min(II)I

    move-result v3

    goto :goto_33

    nop

    :goto_3
    const/16 v4, 0x8

    goto :goto_2

    nop

    :goto_4
    move v4, v1

    :goto_5
    goto :goto_6

    nop

    :goto_6
    if-lt v4, v3, :cond_0

    goto :goto_38

    :cond_0
    goto :goto_21

    nop

    :goto_7
    check-cast p3, [[I

    goto :goto_4

    nop

    :goto_8
    invoke-static {p2, p1}, Ljava/lang/reflect/Array;->newInstance(Ljava/lang/Class;[I)Ljava/lang/Object;

    move-result-object p1

    goto :goto_24

    nop

    :goto_9
    if-nez p1, :cond_1

    goto :goto_d

    :cond_1
    goto :goto_0

    nop

    :goto_a
    invoke-virtual {v5}, Landroid/view/View;->getMeasuredWidth()I

    move-result v7

    goto :goto_2e

    nop

    :goto_b
    aget-object p2, p1, v1

    goto :goto_1b

    nop

    :goto_c
    return-object p3

    :goto_d
    goto :goto_25

    nop

    :goto_e
    invoke-interface {p1}, Landroid/widget/ListAdapter;->getCount()I

    move-result v3

    goto :goto_3

    nop

    :goto_f
    aput v3, v4, v1

    goto :goto_14

    nop

    :goto_10
    invoke-virtual {p1, p2, v2}, Landroid/view/View;->measure(II)V

    goto :goto_2b

    nop

    :goto_11
    const/4 p3, 0x2

    goto :goto_1c

    nop

    :goto_12
    const/high16 p2, -0x80000000

    goto :goto_11

    nop

    :goto_13
    aput p3, v4, v0

    goto :goto_f

    nop

    :goto_14
    sget-object p3, Ljava/lang/Integer;->TYPE:Ljava/lang/Class;

    goto :goto_2c

    nop

    :goto_15
    iget v2, v2, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mMaxWidth:I

    goto :goto_29

    nop

    :goto_16
    invoke-interface {p1, v4, v5, v2}, Landroid/widget/ListAdapter;->getView(ILandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;

    move-result-object v5

    goto :goto_17

    nop

    :goto_17
    iget-object v6, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    goto :goto_2d

    nop

    :goto_18
    aget-object v6, p3, v4

    goto :goto_a

    nop

    :goto_19
    invoke-virtual {p3}, Landroid/view/View;->getMeasuredWidth()I

    move-result p3

    goto :goto_36

    nop

    :goto_1a
    invoke-static {v6, p2}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v6

    goto :goto_28

    nop

    :goto_1b
    iget-object p0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContentView:Landroid/view/View;

    goto :goto_23

    nop

    :goto_1c
    const/4 v0, 0x1

    goto :goto_32

    nop

    :goto_1d
    invoke-virtual {v5, v6, v7}, Landroid/view/View;->measure(II)V

    goto :goto_18

    nop

    :goto_1e
    aput v0, p1, v1

    goto :goto_2a

    nop

    :goto_1f
    iget-object p3, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContentView:Landroid/view/View;

    goto :goto_19

    nop

    :goto_20
    iget-object v2, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    goto :goto_15

    nop

    :goto_21
    const/4 v5, 0x0

    goto :goto_16

    nop

    :goto_22
    return-object p1

    :goto_23
    invoke-virtual {p0}, Landroid/view/View;->getMeasuredHeight()I

    move-result p0

    goto :goto_34

    nop

    :goto_24
    check-cast p1, [[I

    goto :goto_35

    nop

    :goto_25
    iget-object p1, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContentView:Landroid/view/View;

    goto :goto_20

    nop

    :goto_26
    invoke-static {v1, v1}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v2

    goto :goto_10

    nop

    :goto_27
    aput p3, p1, v0

    goto :goto_1e

    nop

    :goto_28
    invoke-static {v1, v1}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v7

    goto :goto_1d

    nop

    :goto_29
    invoke-static {v2, p2}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p2

    goto :goto_26

    nop

    :goto_2a
    sget-object p2, Ljava/lang/Integer;->TYPE:Ljava/lang/Class;

    goto :goto_8

    nop

    :goto_2b
    new-array p1, p3, [I

    goto :goto_27

    nop

    :goto_2c
    invoke-static {p3, v4}, Ljava/lang/reflect/Array;->newInstance(Ljava/lang/Class;[I)Ljava/lang/Object;

    move-result-object p3

    goto :goto_7

    nop

    :goto_2d
    iget v6, v6, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mMaxWidth:I

    goto :goto_1a

    nop

    :goto_2e
    aput v7, v6, v1

    goto :goto_30

    nop

    :goto_2f
    aput v5, v6, v0

    goto :goto_31

    nop

    :goto_30
    aget-object v6, p3, v4

    goto :goto_1

    nop

    :goto_31
    add-int/lit8 v4, v4, 0x1

    goto :goto_37

    nop

    :goto_32
    const/4 v1, 0x0

    goto :goto_9

    nop

    :goto_33
    new-array v4, p3, [I

    goto :goto_13

    nop

    :goto_34
    aput p0, p2, v0

    goto :goto_22

    nop

    :goto_35
    aget-object p2, p1, v1

    goto :goto_1f

    nop

    :goto_36
    aput p3, p2, v1

    goto :goto_b

    nop

    :goto_37
    goto :goto_5

    :goto_38
    goto :goto_c

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
