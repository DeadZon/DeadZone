TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/app/AlertController.smali'
CLASS_FALLBACK_NAMES = ['AlertController.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'miuix_appcompat_app_AlertController__hasPendingDismiss',
        'method': '.method hasPendingDismiss()Z',
        'method_name': 'hasPendingDismiss',
        'method_anchors': ['iget-boolean p0, p0, Lmiuix/appcompat/app/AlertController;->mHasPendingDismiss:Z', 'return p0'],
        'type': 'method_replace',
        'search': """.method hasPendingDismiss()Z
    .registers 1

    iget-boolean p0, p0, Lmiuix/appcompat/app/AlertController;->mHasPendingDismiss:Z

    return p0
.end method""",
        'replacement': """.method hasPendingDismiss()Z
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget-boolean p0, p0, Lmiuix/appcompat/app/AlertController;->mHasPendingDismiss:Z

    goto :goto_1

    nop

    :goto_1
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_AlertController__isDialogImmersive',
        'method': '.method isDialogImmersive()Z',
        'method_name': 'isDialogImmersive',
        'method_anchors': ['iget-boolean p0, p0, Lmiuix/appcompat/app/AlertController;->mIsEnableImmersive:Z', 'if-eqz p0, :cond_0', 'return p0', 'return p0'],
        'type': 'method_replace',
        'search': """.method isDialogImmersive()Z
    .registers 1

    iget-boolean p0, p0, Lmiuix/appcompat/app/AlertController;->mIsEnableImmersive:Z

    if-eqz p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method isDialogImmersive()Z
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget-boolean p0, p0, Lmiuix/appcompat/app/AlertController;->mIsEnableImmersive:Z

    goto :goto_1

    nop

    :goto_1
    if-nez p0, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_6

    nop

    :goto_2
    return p0

    :goto_3
    const/4 p0, 0x0

    goto :goto_2

    nop

    :goto_4
    return p0

    :goto_5
    goto :goto_3

    nop

    :goto_6
    const/4 p0, 0x1

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_AlertController__isShowingAnimation',
        'method': '.method isShowingAnimation()Z',
        'method_name': 'isShowingAnimation',
        'method_anchors': ['iget-wide v0, p0, Lmiuix/appcompat/app/AlertController;->mShowUpTimeMillis:J', 'invoke-static {}, Landroid/os/SystemClock;->uptimeMillis()J', 'invoke-static {v0, v1}, Ljava/lang/Math;->abs(J)J', 'invoke-virtual {p0}, Lmiuix/appcompat/app/AlertController;->isDialogImmersive()Z', 'if-nez v2, :cond_0', 'iget-wide v5, p0, Lmiuix/appcompat/app/AlertController;->mNonImmersiveDialogShowAnimDuration:J', 'if-gez v0, :cond_0', 'iget-boolean v1, p0, Lmiuix/appcompat/app/AlertController;->mEnableEnterAnim:Z'],
        'type': 'method_replace',
        'search': """.method isShowingAnimation()Z
    .registers 8

    iget-wide v0, p0, Lmiuix/appcompat/app/AlertController;->mShowUpTimeMillis:J

    invoke-static {}, Landroid/os/SystemClock;->uptimeMillis()J

    move-result-wide v2

    sub-long/2addr v0, v2

    invoke-static {v0, v1}, Ljava/lang/Math;->abs(J)J

    move-result-wide v0

    invoke-virtual {p0}, Lmiuix/appcompat/app/AlertController;->isDialogImmersive()Z

    move-result v2

    const/4 v3, 0x0

    const/4 v4, 0x1

    if-nez v2, :cond_0

    iget-wide v5, p0, Lmiuix/appcompat/app/AlertController;->mNonImmersiveDialogShowAnimDuration:J

    cmp-long v0, v0, v5

    if-gez v0, :cond_0

    move v0, v4

    goto :goto_0

    :cond_0
    move v0, v3

    :goto_0
    iget-boolean v1, p0, Lmiuix/appcompat/app/AlertController;->mEnableEnterAnim:Z

    if-eqz v1, :cond_2

    iget-boolean p0, p0, Lmiuix/appcompat/app/AlertController;->mIsDialogAnimating:Z

    if-nez p0, :cond_1

    if-eqz v0, :cond_2

    :cond_1
    return v4

    :cond_2
    return v3
.end method""",
        'replacement': """.method isShowingAnimation()Z
    .registers 8

    goto :goto_a

    nop

    :goto_0
    if-nez v0, :cond_0

    goto :goto_e

    :cond_0
    :goto_1
    goto :goto_d

    nop

    :goto_2
    invoke-virtual {p0}, Lmiuix/appcompat/app/AlertController;->isDialogImmersive()Z

    move-result v2

    goto :goto_9

    nop

    :goto_3
    if-eqz v2, :cond_1

    goto :goto_18

    :cond_1
    goto :goto_6

    nop

    :goto_4
    if-eqz p0, :cond_2

    goto :goto_1

    :cond_2
    goto :goto_0

    nop

    :goto_5
    invoke-static {v0, v1}, Ljava/lang/Math;->abs(J)J

    move-result-wide v0

    goto :goto_2

    nop

    :goto_6
    iget-wide v5, p0, Lmiuix/appcompat/app/AlertController;->mNonImmersiveDialogShowAnimDuration:J

    goto :goto_f

    nop

    :goto_7
    if-nez v1, :cond_3

    goto :goto_e

    :cond_3
    goto :goto_11

    nop

    :goto_8
    move v0, v4

    goto :goto_17

    nop

    :goto_9
    const/4 v3, 0x0

    goto :goto_c

    nop

    :goto_a
    iget-wide v0, p0, Lmiuix/appcompat/app/AlertController;->mShowUpTimeMillis:J

    goto :goto_16

    nop

    :goto_b
    iget-boolean v1, p0, Lmiuix/appcompat/app/AlertController;->mEnableEnterAnim:Z

    goto :goto_7

    nop

    :goto_c
    const/4 v4, 0x1

    goto :goto_3

    nop

    :goto_d
    return v4

    :goto_e
    goto :goto_10

    nop

    :goto_f
    cmp-long v0, v0, v5

    goto :goto_15

    nop

    :goto_10
    return v3

    :goto_11
    iget-boolean p0, p0, Lmiuix/appcompat/app/AlertController;->mIsDialogAnimating:Z

    goto :goto_4

    nop

    :goto_12
    move v0, v3

    :goto_13
    goto :goto_b

    nop

    :goto_14
    sub-long/2addr v0, v2

    goto :goto_5

    nop

    :goto_15
    if-ltz v0, :cond_4

    goto :goto_18

    :cond_4
    goto :goto_8

    nop

    :goto_16
    invoke-static {}, Landroid/os/SystemClock;->uptimeMillis()J

    move-result-wide v2

    goto :goto_14

    nop

    :goto_17
    goto :goto_13

    :goto_18
    goto :goto_12

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_AlertController__safeMoveView',
        'method': '.method protected safeMoveView(Landroid/view/View;Landroid/view/ViewGroup;)V',
        'method_name': 'safeMoveView',
        'method_anchors': ['invoke-virtual {p1}, Landroid/view/View;->getParent()Landroid/view/ViewParent;', 'check-cast p0, Landroid/view/ViewGroup;', 'if-ne p0, p2, :cond_0', 'return-void', 'if-eqz p0, :cond_1', 'invoke-virtual {p0, p1}, Landroid/view/ViewGroup;->removeView(Landroid/view/View;)V', 'invoke-virtual {p2, p1}, Landroid/view/ViewGroup;->addView(Landroid/view/View;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected safeMoveView(Landroid/view/View;Landroid/view/ViewGroup;)V
    .registers 3

    invoke-virtual {p1}, Landroid/view/View;->getParent()Landroid/view/ViewParent;

    move-result-object p0

    check-cast p0, Landroid/view/ViewGroup;

    if-ne p0, p2, :cond_0

    return-void

    :cond_0
    if-eqz p0, :cond_1

    invoke-virtual {p0, p1}, Landroid/view/ViewGroup;->removeView(Landroid/view/View;)V

    :cond_1
    invoke-virtual {p2, p1}, Landroid/view/ViewGroup;->addView(Landroid/view/View;)V

    return-void
.end method""",
        'replacement': """.method protected safeMoveView(Landroid/view/View;Landroid/view/ViewGroup;)V
    .registers 3

    goto :goto_3

    nop

    :goto_0
    invoke-virtual {p0, p1}, Landroid/view/ViewGroup;->removeView(Landroid/view/View;)V

    :goto_1
    goto :goto_2

    nop

    :goto_2
    invoke-virtual {p2, p1}, Landroid/view/ViewGroup;->addView(Landroid/view/View;)V

    goto :goto_6

    nop

    :goto_3
    invoke-virtual {p1}, Landroid/view/View;->getParent()Landroid/view/ViewParent;

    move-result-object p0

    goto :goto_9

    nop

    :goto_4
    if-nez p0, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_0

    nop

    :goto_5
    if-eq p0, p2, :cond_1

    goto :goto_8

    :cond_1
    goto :goto_7

    nop

    :goto_6
    return-void

    :goto_7
    return-void

    :goto_8
    goto :goto_4

    nop

    :goto_9
    check-cast p0, Landroid/view/ViewGroup;

    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_AlertController__safeRemoveFromParent',
        'method': '.method protected safeRemoveFromParent(Landroid/view/View;)V',
        'method_name': 'safeRemoveFromParent',
        'method_anchors': ['invoke-virtual {p1}, Landroid/view/View;->getParent()Landroid/view/ViewParent;', 'check-cast p0, Landroid/view/ViewGroup;', 'if-eqz p0, :cond_0', 'invoke-virtual {p0, p1}, Landroid/view/ViewGroup;->removeView(Landroid/view/View;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected safeRemoveFromParent(Landroid/view/View;)V
    .registers 2

    invoke-virtual {p1}, Landroid/view/View;->getParent()Landroid/view/ViewParent;

    move-result-object p0

    check-cast p0, Landroid/view/ViewGroup;

    if-eqz p0, :cond_0

    invoke-virtual {p0, p1}, Landroid/view/ViewGroup;->removeView(Landroid/view/View;)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected safeRemoveFromParent(Landroid/view/View;)V
    .registers 2

    goto :goto_5

    nop

    :goto_0
    invoke-virtual {p0, p1}, Landroid/view/ViewGroup;->removeView(Landroid/view/View;)V

    :goto_1
    goto :goto_3

    nop

    :goto_2
    check-cast p0, Landroid/view/ViewGroup;

    goto :goto_4

    nop

    :goto_3
    return-void

    :goto_4
    if-nez p0, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_0

    nop

    :goto_5
    invoke-virtual {p1}, Landroid/view/View;->getParent()Landroid/view/ViewParent;

    move-result-object p0

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_AlertController__setAsyncInflatePanelEnable',
        'method': '.method setAsyncInflatePanelEnable(Z)V',
        'method_name': 'setAsyncInflatePanelEnable',
        'method_anchors': ['iput-boolean p1, p0, Lmiuix/appcompat/app/AlertController;->mAsyncInflatePanelEnabled:Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method setAsyncInflatePanelEnable(Z)V
    .registers 2

    iput-boolean p1, p0, Lmiuix/appcompat/app/AlertController;->mAsyncInflatePanelEnabled:Z

    return-void
.end method""",
        'replacement': """.method setAsyncInflatePanelEnable(Z)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    iput-boolean p1, p0, Lmiuix/appcompat/app/AlertController;->mAsyncInflatePanelEnabled:Z

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_AlertController__setButtonForceVertical',
        'method': '.method setButtonForceVertical(Z)V',
        'method_name': 'setButtonForceVertical',
        'method_anchors': ['iput-boolean p1, p0, Lmiuix/appcompat/app/AlertController;->mButtonForceVertical:Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method setButtonForceVertical(Z)V
    .registers 2

    iput-boolean p1, p0, Lmiuix/appcompat/app/AlertController;->mButtonForceVertical:Z

    return-void
.end method""",
        'replacement': """.method setButtonForceVertical(Z)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    iput-boolean p1, p0, Lmiuix/appcompat/app/AlertController;->mButtonForceVertical:Z

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
        'id': 'miuix_appcompat_app_AlertController__setDiscardImeAnimEnabled',
        'method': '.method setDiscardImeAnimEnabled(Z)V',
        'method_name': 'setDiscardImeAnimEnabled',
        'method_anchors': ['iput-boolean p1, p0, Lmiuix/appcompat/app/AlertController;->mDiscardImeAnimEnabled:Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method setDiscardImeAnimEnabled(Z)V
    .registers 2

    iput-boolean p1, p0, Lmiuix/appcompat/app/AlertController;->mDiscardImeAnimEnabled:Z

    return-void
.end method""",
        'replacement': """.method setDiscardImeAnimEnabled(Z)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    iput-boolean p1, p0, Lmiuix/appcompat/app/AlertController;->mDiscardImeAnimEnabled:Z

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_AlertController__setEnableEnterAnim',
        'method': '.method setEnableEnterAnim(Z)V',
        'method_name': 'setEnableEnterAnim',
        'method_anchors': ['iput-boolean p1, p0, Lmiuix/appcompat/app/AlertController;->mEnableEnterAnim:Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method setEnableEnterAnim(Z)V
    .registers 2

    iput-boolean p1, p0, Lmiuix/appcompat/app/AlertController;->mEnableEnterAnim:Z

    return-void
.end method""",
        'replacement': """.method setEnableEnterAnim(Z)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    iput-boolean p1, p0, Lmiuix/appcompat/app/AlertController;->mEnableEnterAnim:Z

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
        'id': 'miuix_appcompat_app_AlertController__setEnableImmersive',
        'method': '.method setEnableImmersive(Z)V',
        'method_name': 'setEnableImmersive',
        'method_anchors': ['iput-boolean p1, p0, Lmiuix/appcompat/app/AlertController;->mIsEnableImmersive:Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method setEnableImmersive(Z)V
    .registers 2

    iput-boolean p1, p0, Lmiuix/appcompat/app/AlertController;->mIsEnableImmersive:Z

    return-void
.end method""",
        'replacement': """.method setEnableImmersive(Z)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    iput-boolean p1, p0, Lmiuix/appcompat/app/AlertController;->mIsEnableImmersive:Z

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
        'id': 'miuix_appcompat_app_AlertController__setLiteVersion',
        'method': '.method setLiteVersion(I)V',
        'method_name': 'setLiteVersion',
        'method_anchors': ['iput p1, p0, Lmiuix/appcompat/app/AlertController;->mLiteVersion:I', 'return-void'],
        'type': 'method_replace',
        'search': """.method setLiteVersion(I)V
    .registers 2

    iput p1, p0, Lmiuix/appcompat/app/AlertController;->mLiteVersion:I

    return-void
.end method""",
        'replacement': """.method setLiteVersion(I)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    iput p1, p0, Lmiuix/appcompat/app/AlertController;->mLiteVersion:I

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_AlertController__setNonImmersiveDialogHeight',
        'method': '.method setNonImmersiveDialogHeight(I)V',
        'method_name': 'setNonImmersiveDialogHeight',
        'method_anchors': ['iput p1, p0, Lmiuix/appcompat/app/AlertController;->mNonImmersiveDialogHeight:I', 'return-void'],
        'type': 'method_replace',
        'search': """.method setNonImmersiveDialogHeight(I)V
    .registers 2

    iput p1, p0, Lmiuix/appcompat/app/AlertController;->mNonImmersiveDialogHeight:I

    return-void
.end method""",
        'replacement': """.method setNonImmersiveDialogHeight(I)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    iput p1, p0, Lmiuix/appcompat/app/AlertController;->mNonImmersiveDialogHeight:I

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
        'id': 'miuix_appcompat_app_AlertController__setPendingDismiss',
        'method': '.method setPendingDismiss(Z)V',
        'method_name': 'setPendingDismiss',
        'method_anchors': ['iput-boolean p1, p0, Lmiuix/appcompat/app/AlertController;->mHasPendingDismiss:Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method setPendingDismiss(Z)V
    .registers 2

    iput-boolean p1, p0, Lmiuix/appcompat/app/AlertController;->mHasPendingDismiss:Z

    return-void
.end method""",
        'replacement': """.method setPendingDismiss(Z)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    iput-boolean p1, p0, Lmiuix/appcompat/app/AlertController;->mHasPendingDismiss:Z

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_AlertController__setPreferLandscape',
        'method': '.method setPreferLandscape(Z)V',
        'method_name': 'setPreferLandscape',
        'method_anchors': ['iput-boolean p1, p0, Lmiuix/appcompat/app/AlertController;->mPreferLandscape:Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method setPreferLandscape(Z)V
    .registers 2

    iput-boolean p1, p0, Lmiuix/appcompat/app/AlertController;->mPreferLandscape:Z

    return-void
.end method""",
        'replacement': """.method setPreferLandscape(Z)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    iput-boolean p1, p0, Lmiuix/appcompat/app/AlertController;->mPreferLandscape:Z

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_AlertController__setPrimaryButtonFirstEnabled',
        'method': '.method setPrimaryButtonFirstEnabled(Z)V',
        'method_name': 'setPrimaryButtonFirstEnabled',
        'method_anchors': ['iput-boolean p1, p0, Lmiuix/appcompat/app/AlertController;->mPrimaryButtonFirstEnabled:Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method setPrimaryButtonFirstEnabled(Z)V
    .registers 2

    iput-boolean p1, p0, Lmiuix/appcompat/app/AlertController;->mPrimaryButtonFirstEnabled:Z

    return-void
.end method""",
        'replacement': """.method setPrimaryButtonFirstEnabled(Z)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    iput-boolean p1, p0, Lmiuix/appcompat/app/AlertController;->mPrimaryButtonFirstEnabled:Z

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_AlertController__setUseForceFlipCutout',
        'method': '.method setUseForceFlipCutout(Z)V',
        'method_name': 'setUseForceFlipCutout',
        'method_anchors': ['iput-boolean p1, p0, Lmiuix/appcompat/app/AlertController;->mUseForceFlipCutout:Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method setUseForceFlipCutout(Z)V
    .registers 2

    iput-boolean p1, p0, Lmiuix/appcompat/app/AlertController;->mUseForceFlipCutout:Z

    return-void
.end method""",
        'replacement': """.method setUseForceFlipCutout(Z)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    iput-boolean p1, p0, Lmiuix/appcompat/app/AlertController;->mUseForceFlipCutout:Z

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
