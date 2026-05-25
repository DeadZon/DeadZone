TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/popupwidget/widget/ArrowPopupWindow.smali'
CLASS_FALLBACK_NAMES = ['ArrowPopupWindow.smali']
CLASS_ANCHORS = ['.super Landroid/widget/PopupWindow;']

PATCHES = [
    {
        'id': 'miuix_popupwidget_widget_ArrowPopupWindow__getLayoutInflater',
        'method': '.method protected getLayoutInflater()Landroid/view/LayoutInflater;',
        'method_name': 'getLayoutInflater',
        'method_anchors': ['iget-object p0, p0, Lmiuix/popupwidget/widget/ArrowPopupWindow;->mContext:Landroid/content/Context;', 'invoke-static {p0}, Landroid/view/LayoutInflater;->from(Landroid/content/Context;)Landroid/view/LayoutInflater;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getLayoutInflater()Landroid/view/LayoutInflater;
    .registers 1

    iget-object p0, p0, Lmiuix/popupwidget/widget/ArrowPopupWindow;->mContext:Landroid/content/Context;

    invoke-static {p0}, Landroid/view/LayoutInflater;->from(Landroid/content/Context;)Landroid/view/LayoutInflater;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected getLayoutInflater()Landroid/view/LayoutInflater;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    invoke-static {p0}, Landroid/view/LayoutInflater;->from(Landroid/content/Context;)Landroid/view/LayoutInflater;

    move-result-object p0

    goto :goto_2

    nop

    :goto_1
    iget-object p0, p0, Lmiuix/popupwidget/widget/ArrowPopupWindow;->mContext:Landroid/content/Context;

    goto :goto_0

    nop

    :goto_2
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_popupwidget_widget_ArrowPopupWindow__onPrepareWindow',
        'method': '.method protected onPrepareWindow()V',
        'method_name': 'onPrepareWindow',
        'method_anchors': ['return-void'],
        'type': 'method_replace',
        'search': """.method protected onPrepareWindow()V
    .registers 1

    return-void
.end method""",
        'replacement': """.method protected onPrepareWindow()V
    .registers 1

    goto :goto_0

    nop

    :goto_0
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_popupwidget_widget_ArrowPopupWindow__setSuperHeight',
        'method': '.method protected setSuperHeight(I)V',
        'method_name': 'setSuperHeight',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/widget/PopupWindow;->setHeight(I)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected setSuperHeight(I)V
    .registers 2

    invoke-super {p0, p1}, Landroid/widget/PopupWindow;->setHeight(I)V

    return-void
.end method""",
        'replacement': """.method protected setSuperHeight(I)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    invoke-super {p0, p1}, Landroid/widget/PopupWindow;->setHeight(I)V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_popupwidget_widget_ArrowPopupWindow__setSuperWidth',
        'method': '.method protected setSuperWidth(I)V',
        'method_name': 'setSuperWidth',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/widget/PopupWindow;->setWidth(I)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected setSuperWidth(I)V
    .registers 2

    invoke-super {p0, p1}, Landroid/widget/PopupWindow;->setWidth(I)V

    return-void
.end method""",
        'replacement': """.method protected setSuperWidth(I)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    invoke-super {p0, p1}, Landroid/widget/PopupWindow;->setWidth(I)V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
