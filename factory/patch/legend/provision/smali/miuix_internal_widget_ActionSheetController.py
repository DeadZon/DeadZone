TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/internal/widget/ActionSheetController.smali'
CLASS_FALLBACK_NAMES = ['ActionSheetController.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'miuix_internal_widget_ActionSheetController__checkAndClearFocus',
        'method': '.method protected checkAndClearFocus()V',
        'method_name': 'checkAndClearFocus',
        'method_anchors': ['iget-object p0, p0, Lmiuix/internal/widget/ActionSheetController;->mWindow:Landroid/view/Window;', 'invoke-virtual {p0}, Landroid/view/Window;->getCurrentFocus()Landroid/view/View;', 'if-eqz p0, :cond_0', 'invoke-virtual {p0}, Landroid/view/View;->clearFocus()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected checkAndClearFocus()V
    .registers 1

    iget-object p0, p0, Lmiuix/internal/widget/ActionSheetController;->mWindow:Landroid/view/Window;

    invoke-virtual {p0}, Landroid/view/Window;->getCurrentFocus()Landroid/view/View;

    move-result-object p0

    if-eqz p0, :cond_0

    invoke-virtual {p0}, Landroid/view/View;->clearFocus()V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected checkAndClearFocus()V
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    iget-object p0, p0, Lmiuix/internal/widget/ActionSheetController;->mWindow:Landroid/view/Window;

    goto :goto_2

    nop

    :goto_2
    invoke-virtual {p0}, Landroid/view/Window;->getCurrentFocus()Landroid/view/View;

    move-result-object p0

    goto :goto_5

    nop

    :goto_3
    invoke-virtual {p0}, Landroid/view/View;->clearFocus()V

    :goto_4
    goto :goto_0

    nop

    :goto_5
    if-nez p0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_widget_ActionSheetController__isShowingAnimation',
        'method': '.method protected isShowingAnimation()Z',
        'method_name': 'isShowingAnimation',
        'method_anchors': ['iget-boolean v0, p0, Lmiuix/internal/widget/ActionSheetController;->mEnableEnterAnim:Z', 'if-eqz v0, :cond_0', 'iget-boolean p0, p0, Lmiuix/internal/widget/ActionSheetController;->mIsDialogAnimating:Z', 'if-eqz p0, :cond_0', 'return p0', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected isShowingAnimation()Z
    .registers 2

    iget-boolean v0, p0, Lmiuix/internal/widget/ActionSheetController;->mEnableEnterAnim:Z

    if-eqz v0, :cond_0

    iget-boolean p0, p0, Lmiuix/internal/widget/ActionSheetController;->mIsDialogAnimating:Z

    if-eqz p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method protected isShowingAnimation()Z
    .registers 2

    goto :goto_5

    nop

    :goto_0
    if-nez p0, :cond_0

    goto :goto_8

    :cond_0
    goto :goto_1

    nop

    :goto_1
    const/4 p0, 0x1

    goto :goto_7

    nop

    :goto_2
    iget-boolean p0, p0, Lmiuix/internal/widget/ActionSheetController;->mIsDialogAnimating:Z

    goto :goto_0

    nop

    :goto_3
    return p0

    :goto_4
    const/4 p0, 0x0

    goto :goto_3

    nop

    :goto_5
    iget-boolean v0, p0, Lmiuix/internal/widget/ActionSheetController;->mEnableEnterAnim:Z

    goto :goto_6

    nop

    :goto_6
    if-nez v0, :cond_1

    goto :goto_8

    :cond_1
    goto :goto_2

    nop

    :goto_7
    return p0

    :goto_8
    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_widget_ActionSheetController__setPendingDismiss',
        'method': '.method protected setPendingDismiss(Z)V',
        'method_name': 'setPendingDismiss',
        'method_anchors': ['iput-boolean p1, p0, Lmiuix/internal/widget/ActionSheetController;->mHasPendingDismiss:Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected setPendingDismiss(Z)V
    .registers 2

    iput-boolean p1, p0, Lmiuix/internal/widget/ActionSheetController;->mHasPendingDismiss:Z

    return-void
.end method""",
        'replacement': """.method protected setPendingDismiss(Z)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    iput-boolean p1, p0, Lmiuix/internal/widget/ActionSheetController;->mHasPendingDismiss:Z

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_widget_ActionSheetController__translateContentPanel',
        'method': '.method protected translateContentPanel(I)V',
        'method_name': 'translateContentPanel',
        'method_anchors': ['iget-object v0, p0, Lmiuix/internal/widget/ActionSheetController;->mContentPanel:Landroid/view/ViewGroup;', 'if-nez v0, :cond_0', 'return-void', 'invoke-virtual {v0}, Landroid/view/ViewGroup;->animate()Landroid/view/ViewPropertyAnimator;', 'invoke-virtual {v0}, Landroid/view/ViewPropertyAnimator;->cancel()V', 'iget-object p0, p0, Lmiuix/internal/widget/ActionSheetController;->mContentPanel:Landroid/view/ViewGroup;', 'invoke-virtual {p0, p1}, Landroid/view/ViewGroup;->setTranslationY(F)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected translateContentPanel(I)V
    .registers 3

    iget-object v0, p0, Lmiuix/internal/widget/ActionSheetController;->mContentPanel:Landroid/view/ViewGroup;

    if-nez v0, :cond_0

    return-void

    :cond_0
    invoke-virtual {v0}, Landroid/view/ViewGroup;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object v0

    invoke-virtual {v0}, Landroid/view/ViewPropertyAnimator;->cancel()V

    iget-object p0, p0, Lmiuix/internal/widget/ActionSheetController;->mContentPanel:Landroid/view/ViewGroup;

    int-to-float p1, p1

    invoke-virtual {p0, p1}, Landroid/view/ViewGroup;->setTranslationY(F)V

    return-void
.end method""",
        'replacement': """.method protected translateContentPanel(I)V
    .registers 3

    goto :goto_7

    nop

    :goto_0
    invoke-virtual {p0, p1}, Landroid/view/ViewGroup;->setTranslationY(F)V

    goto :goto_9

    nop

    :goto_1
    iget-object p0, p0, Lmiuix/internal/widget/ActionSheetController;->mContentPanel:Landroid/view/ViewGroup;

    goto :goto_8

    nop

    :goto_2
    invoke-virtual {v0}, Landroid/view/ViewGroup;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object v0

    goto :goto_5

    nop

    :goto_3
    return-void

    :goto_4
    goto :goto_2

    nop

    :goto_5
    invoke-virtual {v0}, Landroid/view/ViewPropertyAnimator;->cancel()V

    goto :goto_1

    nop

    :goto_6
    if-eqz v0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_3

    nop

    :goto_7
    iget-object v0, p0, Lmiuix/internal/widget/ActionSheetController;->mContentPanel:Landroid/view/ViewGroup;

    goto :goto_6

    nop

    :goto_8
    int-to-float p1, p1

    goto :goto_0

    nop

    :goto_9
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
