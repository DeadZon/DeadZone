TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/popupwidget/widget/PopupWindow$ContainerView.smali'
CLASS_FALLBACK_NAMES = ['PopupWindow$ContainerView.smali']
CLASS_ANCHORS = ['.super Landroid/widget/FrameLayout;']

PATCHES = [
    {
        'id': 'miuix_popupwidget_widget_PopupWindow__ContainerView__onConfigurationChanged',
        'method': '.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V',
        'method_name': 'onConfigurationChanged',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/widget/FrameLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V', 'iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow$ContainerView;->this$0:Lmiuix/popupwidget/widget/PopupWindow;', 'invoke-static {v0}, Lmiuix/popupwidget/widget/PopupWindow;->access$600(Lmiuix/popupwidget/widget/PopupWindow;)Z', 'if-eqz v0, :cond_0', 'iget-object p0, p0, Lmiuix/popupwidget/widget/PopupWindow$ContainerView;->this$0:Lmiuix/popupwidget/widget/PopupWindow;', 'invoke-virtual {p0}, Lmiuix/popupwidget/widget/PopupWindow;->dismiss()V', 'return-void', 'iget-object p0, p0, Lmiuix/popupwidget/widget/PopupWindow$ContainerView;->this$0:Lmiuix/popupwidget/widget/PopupWindow;'],
        'type': 'method_replace',
        'search': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 3

    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow$ContainerView;->this$0:Lmiuix/popupwidget/widget/PopupWindow;

    invoke-static {v0}, Lmiuix/popupwidget/widget/PopupWindow;->access$600(Lmiuix/popupwidget/widget/PopupWindow;)Z

    move-result v0

    if-eqz v0, :cond_0

    iget-object p0, p0, Lmiuix/popupwidget/widget/PopupWindow$ContainerView;->this$0:Lmiuix/popupwidget/widget/PopupWindow;

    invoke-virtual {p0}, Lmiuix/popupwidget/widget/PopupWindow;->dismiss()V

    return-void

    :cond_0
    iget-object p0, p0, Lmiuix/popupwidget/widget/PopupWindow$ContainerView;->this$0:Lmiuix/popupwidget/widget/PopupWindow;

    invoke-static {p0, p1}, Lmiuix/popupwidget/widget/PopupWindow;->access$700(Lmiuix/popupwidget/widget/PopupWindow;Landroid/content/res/Configuration;)V

    return-void
.end method""",
        'replacement': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 3

    goto :goto_3

    nop

    :goto_0
    invoke-static {v0}, Lmiuix/popupwidget/widget/PopupWindow;->access$600(Lmiuix/popupwidget/widget/PopupWindow;)Z

    move-result v0

    goto :goto_6

    nop

    :goto_1
    iget-object p0, p0, Lmiuix/popupwidget/widget/PopupWindow$ContainerView;->this$0:Lmiuix/popupwidget/widget/PopupWindow;

    goto :goto_8

    nop

    :goto_2
    return-void

    :goto_3
    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    goto :goto_5

    nop

    :goto_4
    invoke-static {p0, p1}, Lmiuix/popupwidget/widget/PopupWindow;->access$700(Lmiuix/popupwidget/widget/PopupWindow;Landroid/content/res/Configuration;)V

    goto :goto_2

    nop

    :goto_5
    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow$ContainerView;->this$0:Lmiuix/popupwidget/widget/PopupWindow;

    goto :goto_0

    nop

    :goto_6
    if-nez v0, :cond_0

    goto :goto_a

    :cond_0
    goto :goto_1

    nop

    :goto_7
    iget-object p0, p0, Lmiuix/popupwidget/widget/PopupWindow$ContainerView;->this$0:Lmiuix/popupwidget/widget/PopupWindow;

    goto :goto_4

    nop

    :goto_8
    invoke-virtual {p0}, Lmiuix/popupwidget/widget/PopupWindow;->dismiss()V

    goto :goto_9

    nop

    :goto_9
    return-void

    :goto_a
    goto :goto_7

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_popupwidget_widget_PopupWindow__ContainerView__onDetachedFromWindow',
        'method': '.method protected onDetachedFromWindow()V',
        'method_name': 'onDetachedFromWindow',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/FrameLayout;->onDetachedFromWindow()V', 'iget-object p0, p0, Lmiuix/popupwidget/widget/PopupWindow$ContainerView;->this$0:Lmiuix/popupwidget/widget/PopupWindow;', 'invoke-static {p0}, Lmiuix/popupwidget/widget/PopupWindow;->access$500(Lmiuix/popupwidget/widget/PopupWindow;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onDetachedFromWindow()V
    .registers 1

    invoke-super {p0}, Landroid/widget/FrameLayout;->onDetachedFromWindow()V

    iget-object p0, p0, Lmiuix/popupwidget/widget/PopupWindow$ContainerView;->this$0:Lmiuix/popupwidget/widget/PopupWindow;

    invoke-static {p0}, Lmiuix/popupwidget/widget/PopupWindow;->access$500(Lmiuix/popupwidget/widget/PopupWindow;)V

    return-void
.end method""",
        'replacement': """.method protected onDetachedFromWindow()V
    .registers 1

    goto :goto_1

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/popupwidget/widget/PopupWindow$ContainerView;->this$0:Lmiuix/popupwidget/widget/PopupWindow;

    goto :goto_2

    nop

    :goto_1
    invoke-super {p0}, Landroid/widget/FrameLayout;->onDetachedFromWindow()V

    goto :goto_0

    nop

    :goto_2
    invoke-static {p0}, Lmiuix/popupwidget/widget/PopupWindow;->access$500(Lmiuix/popupwidget/widget/PopupWindow;)V

    goto :goto_3

    nop

    :goto_3
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
