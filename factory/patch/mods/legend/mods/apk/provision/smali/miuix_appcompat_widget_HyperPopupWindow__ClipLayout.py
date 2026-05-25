TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/widget/HyperPopupWindow$ClipLayout.smali'
CLASS_FALLBACK_NAMES = ['HyperPopupWindow$ClipLayout.smali']
CLASS_ANCHORS = ['.super Landroid/widget/FrameLayout;']

PATCHES = [
    {
        'id': 'miuix_appcompat_widget_HyperPopupWindow__ClipLayout__onAttachedToWindow',
        'method': '.method protected onAttachedToWindow()V',
        'method_name': 'onAttachedToWindow',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/FrameLayout;->onAttachedToWindow()V', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->findOnBackInvokedDispatcher()Landroid/window/OnBackInvokedDispatcher;', 'iput-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;->dispatcher:Landroid/window/OnBackInvokedDispatcher;', 'iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;', 'new-instance v1, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout$$ExternalSyntheticLambda0;', 'invoke-direct {v1, v0}, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout$$ExternalSyntheticLambda0;-><init>(Lmiuix/appcompat/widget/HyperPopupWindow;)V', 'iput-object v1, p0, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;->backCallBack:Landroid/window/OnBackInvokedCallback;', 'iget-object p0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;->dispatcher:Landroid/window/OnBackInvokedDispatcher;'],
        'type': 'method_replace',
        'search': """.method protected onAttachedToWindow()V
    .registers 3

    invoke-super {p0}, Landroid/widget/FrameLayout;->onAttachedToWindow()V

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->findOnBackInvokedDispatcher()Landroid/window/OnBackInvokedDispatcher;

    move-result-object v0

    iput-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;->dispatcher:Landroid/window/OnBackInvokedDispatcher;

    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    new-instance v1, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout$$ExternalSyntheticLambda0;

    invoke-direct {v1, v0}, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout$$ExternalSyntheticLambda0;-><init>(Lmiuix/appcompat/widget/HyperPopupWindow;)V

    iput-object v1, p0, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;->backCallBack:Landroid/window/OnBackInvokedCallback;

    iget-object p0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;->dispatcher:Landroid/window/OnBackInvokedDispatcher;

    if-eqz p0, :cond_0

    const v0, 0xf4240

    invoke-interface {p0, v0, v1}, Landroid/window/OnBackInvokedDispatcher;->registerOnBackInvokedCallback(ILandroid/window/OnBackInvokedCallback;)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onAttachedToWindow()V
    .registers 3

    goto :goto_3

    nop

    :goto_0
    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;->this$0:Lmiuix/appcompat/widget/HyperPopupWindow;

    goto :goto_c

    nop

    :goto_1
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->findOnBackInvokedDispatcher()Landroid/window/OnBackInvokedDispatcher;

    move-result-object v0

    goto :goto_6

    nop

    :goto_2
    iput-object v1, p0, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;->backCallBack:Landroid/window/OnBackInvokedCallback;

    goto :goto_7

    nop

    :goto_3
    invoke-super {p0}, Landroid/widget/FrameLayout;->onAttachedToWindow()V

    goto :goto_1

    nop

    :goto_4
    const v0, 0xf4240

    goto :goto_9

    nop

    :goto_5
    invoke-direct {v1, v0}, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout$$ExternalSyntheticLambda0;-><init>(Lmiuix/appcompat/widget/HyperPopupWindow;)V

    goto :goto_2

    nop

    :goto_6
    iput-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;->dispatcher:Landroid/window/OnBackInvokedDispatcher;

    goto :goto_0

    nop

    :goto_7
    iget-object p0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;->dispatcher:Landroid/window/OnBackInvokedDispatcher;

    goto :goto_b

    nop

    :goto_8
    return-void

    :goto_9
    invoke-interface {p0, v0, v1}, Landroid/window/OnBackInvokedDispatcher;->registerOnBackInvokedCallback(ILandroid/window/OnBackInvokedCallback;)V

    :goto_a
    goto :goto_8

    nop

    :goto_b
    if-nez p0, :cond_0

    goto :goto_a

    :cond_0
    goto :goto_4

    nop

    :goto_c
    new-instance v1, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout$$ExternalSyntheticLambda0;

    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_widget_HyperPopupWindow__ClipLayout__onDetachedFromWindow',
        'method': '.method protected onDetachedFromWindow()V',
        'method_name': 'onDetachedFromWindow',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/FrameLayout;->onDetachedFromWindow()V', 'iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;->dispatcher:Landroid/window/OnBackInvokedDispatcher;', 'if-eqz v0, :cond_0', 'iget-object p0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;->backCallBack:Landroid/window/OnBackInvokedCallback;', 'invoke-interface {v0, p0}, Landroid/window/OnBackInvokedDispatcher;->unregisterOnBackInvokedCallback(Landroid/window/OnBackInvokedCallback;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onDetachedFromWindow()V
    .registers 2

    invoke-super {p0}, Landroid/widget/FrameLayout;->onDetachedFromWindow()V

    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;->dispatcher:Landroid/window/OnBackInvokedDispatcher;

    if-eqz v0, :cond_0

    iget-object p0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;->backCallBack:Landroid/window/OnBackInvokedCallback;

    invoke-interface {v0, p0}, Landroid/window/OnBackInvokedDispatcher;->unregisterOnBackInvokedCallback(Landroid/window/OnBackInvokedCallback;)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onDetachedFromWindow()V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    iget-object v0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;->dispatcher:Landroid/window/OnBackInvokedDispatcher;

    goto :goto_4

    nop

    :goto_1
    invoke-super {p0}, Landroid/widget/FrameLayout;->onDetachedFromWindow()V

    goto :goto_0

    nop

    :goto_2
    return-void

    :goto_3
    iget-object p0, p0, Lmiuix/appcompat/widget/HyperPopupWindow$ClipLayout;->backCallBack:Landroid/window/OnBackInvokedCallback;

    goto :goto_5

    nop

    :goto_4
    if-nez v0, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_3

    nop

    :goto_5
    invoke-interface {v0, p0}, Landroid/window/OnBackInvokedDispatcher;->unregisterOnBackInvokedCallback(Landroid/window/OnBackInvokedCallback;)V

    :goto_6
    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
