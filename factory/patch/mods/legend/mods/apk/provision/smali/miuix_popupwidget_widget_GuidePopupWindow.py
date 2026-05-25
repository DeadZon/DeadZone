TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/popupwidget/widget/GuidePopupWindow.smali'
CLASS_FALLBACK_NAMES = ['GuidePopupWindow.smali']
CLASS_ANCHORS = ['.super Lmiuix/popupwidget/widget/ArrowPopupWindow;']

PATCHES = [
    {
        'id': 'miuix_popupwidget_widget_GuidePopupWindow__onPrepareWindow',
        'method': '.method protected onPrepareWindow()V',
        'method_name': 'onPrepareWindow',
        'method_anchors': ['invoke-super {p0}, Lmiuix/popupwidget/widget/ArrowPopupWindow;->onPrepareWindow()V', 'iput v0, p0, Lmiuix/popupwidget/widget/GuidePopupWindow;->mShowDuration:I', 'invoke-virtual {p0, v0}, Landroid/widget/PopupWindow;->setFocusable(Z)V', 'invoke-virtual {p0}, Lmiuix/popupwidget/widget/ArrowPopupWindow;->getLayoutInflater()Landroid/view/LayoutInflater;', 'sget v1, Lmiuix/popupwidget/R$layout;->miuix_appcompat_guide_popup_content_view:I', 'invoke-virtual {v0, v1, v2, v3}, Landroid/view/LayoutInflater;->inflate(ILandroid/view/ViewGroup;Z)Landroid/view/View;', 'check-cast v0, Landroid/widget/LinearLayout;', 'iput-object v0, p0, Lmiuix/popupwidget/widget/GuidePopupWindow;->mGuideView:Landroid/widget/LinearLayout;'],
        'type': 'method_replace',
        'search': """.method protected onPrepareWindow()V
    .registers 5

    invoke-super {p0}, Lmiuix/popupwidget/widget/ArrowPopupWindow;->onPrepareWindow()V

    const/16 v0, 0x1388

    iput v0, p0, Lmiuix/popupwidget/widget/GuidePopupWindow;->mShowDuration:I

    const/4 v0, 0x1

    invoke-virtual {p0, v0}, Landroid/widget/PopupWindow;->setFocusable(Z)V

    invoke-virtual {p0}, Lmiuix/popupwidget/widget/ArrowPopupWindow;->getLayoutInflater()Landroid/view/LayoutInflater;

    move-result-object v0

    sget v1, Lmiuix/popupwidget/R$layout;->miuix_appcompat_guide_popup_content_view:I

    const/4 v2, 0x0

    const/4 v3, 0x0

    invoke-virtual {v0, v1, v2, v3}, Landroid/view/LayoutInflater;->inflate(ILandroid/view/ViewGroup;Z)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/LinearLayout;

    iput-object v0, p0, Lmiuix/popupwidget/widget/GuidePopupWindow;->mGuideView:Landroid/widget/LinearLayout;

    invoke-virtual {p0, v0}, Lmiuix/popupwidget/widget/ArrowPopupWindow;->setContentView(Landroid/view/View;)V

    iget-object v0, p0, Lmiuix/popupwidget/widget/ArrowPopupWindow;->mArrowPopupView:Lmiuix/popupwidget/internal/widget/ArrowPopupView;

    invoke-virtual {v0, v3}, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->enableShowingAnimation(Z)V

    invoke-direct {p0}, Lmiuix/popupwidget/widget/GuidePopupWindow;->setAccessibilityDelegate()V

    return-void
.end method""",
        'replacement': """.method protected onPrepareWindow()V
    .registers 5

    goto :goto_f

    nop

    :goto_0
    invoke-virtual {p0, v0}, Landroid/widget/PopupWindow;->setFocusable(Z)V

    goto :goto_9

    nop

    :goto_1
    check-cast v0, Landroid/widget/LinearLayout;

    goto :goto_7

    nop

    :goto_2
    invoke-virtual {p0, v0}, Lmiuix/popupwidget/widget/ArrowPopupWindow;->setContentView(Landroid/view/View;)V

    goto :goto_d

    nop

    :goto_3
    return-void

    :goto_4
    iput v0, p0, Lmiuix/popupwidget/widget/GuidePopupWindow;->mShowDuration:I

    goto :goto_6

    nop

    :goto_5
    const/4 v3, 0x0

    goto :goto_c

    nop

    :goto_6
    const/4 v0, 0x1

    goto :goto_0

    nop

    :goto_7
    iput-object v0, p0, Lmiuix/popupwidget/widget/GuidePopupWindow;->mGuideView:Landroid/widget/LinearLayout;

    goto :goto_2

    nop

    :goto_8
    invoke-virtual {v0, v3}, Lmiuix/popupwidget/internal/widget/ArrowPopupView;->enableShowingAnimation(Z)V

    goto :goto_e

    nop

    :goto_9
    invoke-virtual {p0}, Lmiuix/popupwidget/widget/ArrowPopupWindow;->getLayoutInflater()Landroid/view/LayoutInflater;

    move-result-object v0

    goto :goto_10

    nop

    :goto_a
    const/4 v2, 0x0

    goto :goto_5

    nop

    :goto_b
    const/16 v0, 0x1388

    goto :goto_4

    nop

    :goto_c
    invoke-virtual {v0, v1, v2, v3}, Landroid/view/LayoutInflater;->inflate(ILandroid/view/ViewGroup;Z)Landroid/view/View;

    move-result-object v0

    goto :goto_1

    nop

    :goto_d
    iget-object v0, p0, Lmiuix/popupwidget/widget/ArrowPopupWindow;->mArrowPopupView:Lmiuix/popupwidget/internal/widget/ArrowPopupView;

    goto :goto_8

    nop

    :goto_e
    invoke-direct {p0}, Lmiuix/popupwidget/widget/GuidePopupWindow;->setAccessibilityDelegate()V

    goto :goto_3

    nop

    :goto_f
    invoke-super {p0}, Lmiuix/popupwidget/widget/ArrowPopupWindow;->onPrepareWindow()V

    goto :goto_b

    nop

    :goto_10
    sget v1, Lmiuix/popupwidget/R$layout;->miuix_appcompat_guide_popup_content_view:I

    goto :goto_a

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
