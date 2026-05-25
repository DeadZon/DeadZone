TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/airbnb/lottie/utils/LottieValueAnimator.smali'
CLASS_FALLBACK_NAMES = ['LottieValueAnimator.smali']
CLASS_ANCHORS = ['.super Lcom/airbnb/lottie/utils/BaseLottieAnimator;', '.implements Landroid/view/Choreographer$FrameCallback;']

PATCHES = [
    {
        'id': 'com_airbnb_lottie_utils_LottieValueAnimator__notifyCancel',
        'method': '.method notifyCancel()V',
        'method_name': 'notifyCancel',
        'method_anchors': ['invoke-super {p0}, Lcom/airbnb/lottie/utils/BaseLottieAnimator;->notifyCancel()V', 'invoke-direct {p0}, Lcom/airbnb/lottie/utils/LottieValueAnimator;->isReversed()Z', 'invoke-virtual {p0, v0}, Lcom/airbnb/lottie/utils/BaseLottieAnimator;->notifyEnd(Z)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method notifyCancel()V
    .registers 2

    invoke-super {p0}, Lcom/airbnb/lottie/utils/BaseLottieAnimator;->notifyCancel()V

    invoke-direct {p0}, Lcom/airbnb/lottie/utils/LottieValueAnimator;->isReversed()Z

    move-result v0

    invoke-virtual {p0, v0}, Lcom/airbnb/lottie/utils/BaseLottieAnimator;->notifyEnd(Z)V

    return-void
.end method""",
        'replacement': """.method notifyCancel()V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    invoke-direct {p0}, Lcom/airbnb/lottie/utils/LottieValueAnimator;->isReversed()Z

    move-result v0

    goto :goto_2

    nop

    :goto_1
    invoke-super {p0}, Lcom/airbnb/lottie/utils/BaseLottieAnimator;->notifyCancel()V

    goto :goto_0

    nop

    :goto_2
    invoke-virtual {p0, v0}, Lcom/airbnb/lottie/utils/BaseLottieAnimator;->notifyEnd(Z)V

    goto :goto_3

    nop

    :goto_3
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_utils_LottieValueAnimator__postFrameCallback',
        'method': '.method protected postFrameCallback()V',
        'method_name': 'postFrameCallback',
        'method_anchors': ['invoke-virtual {p0}, Lcom/airbnb/lottie/utils/LottieValueAnimator;->isRunning()Z', 'if-eqz v0, :cond_0', 'invoke-virtual {p0, v0}, Lcom/airbnb/lottie/utils/LottieValueAnimator;->removeFrameCallback(Z)V', 'invoke-static {}, Landroid/view/Choreographer;->getInstance()Landroid/view/Choreographer;', 'invoke-virtual {v0, p0}, Landroid/view/Choreographer;->postFrameCallback(Landroid/view/Choreographer$FrameCallback;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected postFrameCallback()V
    .registers 2

    invoke-virtual {p0}, Lcom/airbnb/lottie/utils/LottieValueAnimator;->isRunning()Z

    move-result v0

    if-eqz v0, :cond_0

    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Lcom/airbnb/lottie/utils/LottieValueAnimator;->removeFrameCallback(Z)V

    invoke-static {}, Landroid/view/Choreographer;->getInstance()Landroid/view/Choreographer;

    move-result-object v0

    invoke-virtual {v0, p0}, Landroid/view/Choreographer;->postFrameCallback(Landroid/view/Choreographer$FrameCallback;)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected postFrameCallback()V
    .registers 2

    goto :goto_2

    nop

    :goto_0
    if-nez v0, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_3

    nop

    :goto_1
    invoke-virtual {p0, v0}, Lcom/airbnb/lottie/utils/LottieValueAnimator;->removeFrameCallback(Z)V

    goto :goto_7

    nop

    :goto_2
    invoke-virtual {p0}, Lcom/airbnb/lottie/utils/LottieValueAnimator;->isRunning()Z

    move-result v0

    goto :goto_0

    nop

    :goto_3
    const/4 v0, 0x0

    goto :goto_1

    nop

    :goto_4
    return-void

    :goto_5
    invoke-virtual {v0, p0}, Landroid/view/Choreographer;->postFrameCallback(Landroid/view/Choreographer$FrameCallback;)V

    :goto_6
    goto :goto_4

    nop

    :goto_7
    invoke-static {}, Landroid/view/Choreographer;->getInstance()Landroid/view/Choreographer;

    move-result-object v0

    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_utils_LottieValueAnimator__removeFrameCallback',
        'method': '.method protected removeFrameCallback()V',
        'method_name': 'removeFrameCallback',
        'method_anchors': ['invoke-virtual {p0, v0}, Lcom/airbnb/lottie/utils/LottieValueAnimator;->removeFrameCallback(Z)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected removeFrameCallback()V
    .registers 2

    const/4 v0, 0x1

    invoke-virtual {p0, v0}, Lcom/airbnb/lottie/utils/LottieValueAnimator;->removeFrameCallback(Z)V

    return-void
.end method""",
        'replacement': """.method protected removeFrameCallback()V
    .registers 2

    goto :goto_2

    nop

    :goto_0
    invoke-virtual {p0, v0}, Lcom/airbnb/lottie/utils/LottieValueAnimator;->removeFrameCallback(Z)V

    goto :goto_1

    nop

    :goto_1
    return-void

    :goto_2
    const/4 v0, 0x1

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_utils_LottieValueAnimator__removeFrameCallback',
        'method': '.method protected removeFrameCallback(Z)V',
        'method_name': 'removeFrameCallback',
        'method_anchors': ['invoke-static {}, Landroid/view/Choreographer;->getInstance()Landroid/view/Choreographer;', 'invoke-virtual {v0, p0}, Landroid/view/Choreographer;->removeFrameCallback(Landroid/view/Choreographer$FrameCallback;)V', 'if-eqz p1, :cond_0', 'iput-boolean p1, p0, Lcom/airbnb/lottie/utils/LottieValueAnimator;->running:Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected removeFrameCallback(Z)V
    .registers 3

    invoke-static {}, Landroid/view/Choreographer;->getInstance()Landroid/view/Choreographer;

    move-result-object v0

    invoke-virtual {v0, p0}, Landroid/view/Choreographer;->removeFrameCallback(Landroid/view/Choreographer$FrameCallback;)V

    if-eqz p1, :cond_0

    const/4 p1, 0x0

    iput-boolean p1, p0, Lcom/airbnb/lottie/utils/LottieValueAnimator;->running:Z

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected removeFrameCallback(Z)V
    .registers 3

    goto :goto_6

    nop

    :goto_0
    invoke-virtual {v0, p0}, Landroid/view/Choreographer;->removeFrameCallback(Landroid/view/Choreographer$FrameCallback;)V

    goto :goto_1

    nop

    :goto_1
    if-nez p1, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_3

    nop

    :goto_2
    return-void

    :goto_3
    const/4 p1, 0x0

    goto :goto_4

    nop

    :goto_4
    iput-boolean p1, p0, Lcom/airbnb/lottie/utils/LottieValueAnimator;->running:Z

    :goto_5
    goto :goto_2

    nop

    :goto_6
    invoke-static {}, Landroid/view/Choreographer;->getInstance()Landroid/view/Choreographer;

    move-result-object v0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
