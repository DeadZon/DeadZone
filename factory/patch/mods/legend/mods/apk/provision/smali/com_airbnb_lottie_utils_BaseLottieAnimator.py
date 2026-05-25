TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/airbnb/lottie/utils/BaseLottieAnimator.smali'
CLASS_FALLBACK_NAMES = ['BaseLottieAnimator.smali']
CLASS_ANCHORS = ['.super Landroid/animation/ValueAnimator;']

PATCHES = [
    {
        'id': 'com_airbnb_lottie_utils_BaseLottieAnimator__notifyCancel',
        'method': '.method notifyCancel()V',
        'method_name': 'notifyCancel',
        'method_anchors': ['iget-object v0, p0, Lcom/airbnb/lottie/utils/BaseLottieAnimator;->listeners:Ljava/util/Set;', 'invoke-interface {v0}, Ljava/util/Set;->iterator()Ljava/util/Iterator;', 'invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z', 'if-eqz v1, :cond_0', 'invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;', 'check-cast v1, Landroid/animation/Animator$AnimatorListener;', 'invoke-interface {v1, p0}, Landroid/animation/Animator$AnimatorListener;->onAnimationCancel(Landroid/animation/Animator;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method notifyCancel()V
    .registers 3

    iget-object v0, p0, Lcom/airbnb/lottie/utils/BaseLottieAnimator;->listeners:Ljava/util/Set;

    invoke-interface {v0}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_0
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_0

    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Landroid/animation/Animator$AnimatorListener;

    invoke-interface {v1, p0}, Landroid/animation/Animator$AnimatorListener;->onAnimationCancel(Landroid/animation/Animator;)V

    goto :goto_0

    :cond_0
    return-void
.end method""",
        'replacement': """.method notifyCancel()V
    .registers 3

    goto :goto_4

    nop

    :goto_0
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    goto :goto_8

    nop

    :goto_1
    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    goto :goto_7

    nop

    :goto_2
    invoke-interface {v1, p0}, Landroid/animation/Animator$AnimatorListener;->onAnimationCancel(Landroid/animation/Animator;)V

    goto :goto_9

    nop

    :goto_3
    return-void

    :goto_4
    iget-object v0, p0, Lcom/airbnb/lottie/utils/BaseLottieAnimator;->listeners:Ljava/util/Set;

    goto :goto_5

    nop

    :goto_5
    invoke-interface {v0}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_6
    goto :goto_0

    nop

    :goto_7
    check-cast v1, Landroid/animation/Animator$AnimatorListener;

    goto :goto_2

    nop

    :goto_8
    if-nez v1, :cond_0

    goto :goto_a

    :cond_0
    goto :goto_1

    nop

    :goto_9
    goto :goto_6

    :goto_a
    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_utils_BaseLottieAnimator__notifyEnd',
        'method': '.method notifyEnd(Z)V',
        'method_name': 'notifyEnd',
        'method_anchors': ['iget-object v0, p0, Lcom/airbnb/lottie/utils/BaseLottieAnimator;->listeners:Ljava/util/Set;', 'invoke-interface {v0}, Ljava/util/Set;->iterator()Ljava/util/Iterator;', 'invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z', 'if-eqz v1, :cond_0', 'invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;', 'check-cast v1, Landroid/animation/Animator$AnimatorListener;', 'invoke-interface {v1, p0, p1}, Landroid/animation/Animator$AnimatorListener;->onAnimationEnd(Landroid/animation/Animator;Z)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method notifyEnd(Z)V
    .registers 4

    iget-object v0, p0, Lcom/airbnb/lottie/utils/BaseLottieAnimator;->listeners:Ljava/util/Set;

    invoke-interface {v0}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_0
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_0

    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Landroid/animation/Animator$AnimatorListener;

    invoke-interface {v1, p0, p1}, Landroid/animation/Animator$AnimatorListener;->onAnimationEnd(Landroid/animation/Animator;Z)V

    goto :goto_0

    :cond_0
    return-void
.end method""",
        'replacement': """.method notifyEnd(Z)V
    .registers 4

    goto :goto_0

    nop

    :goto_0
    iget-object v0, p0, Lcom/airbnb/lottie/utils/BaseLottieAnimator;->listeners:Ljava/util/Set;

    goto :goto_4

    nop

    :goto_1
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    goto :goto_a

    nop

    :goto_2
    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    goto :goto_3

    nop

    :goto_3
    check-cast v1, Landroid/animation/Animator$AnimatorListener;

    goto :goto_6

    nop

    :goto_4
    invoke-interface {v0}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_5
    goto :goto_1

    nop

    :goto_6
    invoke-interface {v1, p0, p1}, Landroid/animation/Animator$AnimatorListener;->onAnimationEnd(Landroid/animation/Animator;Z)V

    goto :goto_8

    nop

    :goto_7
    return-void

    :goto_8
    goto :goto_5

    :goto_9
    goto :goto_7

    nop

    :goto_a
    if-nez v1, :cond_0

    goto :goto_9

    :cond_0
    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_utils_BaseLottieAnimator__notifyRepeat',
        'method': '.method notifyRepeat()V',
        'method_name': 'notifyRepeat',
        'method_anchors': ['iget-object v0, p0, Lcom/airbnb/lottie/utils/BaseLottieAnimator;->listeners:Ljava/util/Set;', 'invoke-interface {v0}, Ljava/util/Set;->iterator()Ljava/util/Iterator;', 'invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z', 'if-eqz v1, :cond_0', 'invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;', 'check-cast v1, Landroid/animation/Animator$AnimatorListener;', 'invoke-interface {v1, p0}, Landroid/animation/Animator$AnimatorListener;->onAnimationRepeat(Landroid/animation/Animator;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method notifyRepeat()V
    .registers 3

    iget-object v0, p0, Lcom/airbnb/lottie/utils/BaseLottieAnimator;->listeners:Ljava/util/Set;

    invoke-interface {v0}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_0
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_0

    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Landroid/animation/Animator$AnimatorListener;

    invoke-interface {v1, p0}, Landroid/animation/Animator$AnimatorListener;->onAnimationRepeat(Landroid/animation/Animator;)V

    goto :goto_0

    :cond_0
    return-void
.end method""",
        'replacement': """.method notifyRepeat()V
    .registers 3

    goto :goto_4

    nop

    :goto_0
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    goto :goto_9

    nop

    :goto_1
    check-cast v1, Landroid/animation/Animator$AnimatorListener;

    goto :goto_a

    nop

    :goto_2
    return-void

    :goto_3
    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    goto :goto_1

    nop

    :goto_4
    iget-object v0, p0, Lcom/airbnb/lottie/utils/BaseLottieAnimator;->listeners:Ljava/util/Set;

    goto :goto_7

    nop

    :goto_5
    goto :goto_8

    :goto_6
    goto :goto_2

    nop

    :goto_7
    invoke-interface {v0}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_8
    goto :goto_0

    nop

    :goto_9
    if-nez v1, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_3

    nop

    :goto_a
    invoke-interface {v1, p0}, Landroid/animation/Animator$AnimatorListener;->onAnimationRepeat(Landroid/animation/Animator;)V

    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_utils_BaseLottieAnimator__notifyStart',
        'method': '.method notifyStart(Z)V',
        'method_name': 'notifyStart',
        'method_anchors': ['iget-object v0, p0, Lcom/airbnb/lottie/utils/BaseLottieAnimator;->listeners:Ljava/util/Set;', 'invoke-interface {v0}, Ljava/util/Set;->iterator()Ljava/util/Iterator;', 'invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z', 'if-eqz v1, :cond_0', 'invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;', 'check-cast v1, Landroid/animation/Animator$AnimatorListener;', 'invoke-interface {v1, p0, p1}, Landroid/animation/Animator$AnimatorListener;->onAnimationStart(Landroid/animation/Animator;Z)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method notifyStart(Z)V
    .registers 4

    iget-object v0, p0, Lcom/airbnb/lottie/utils/BaseLottieAnimator;->listeners:Ljava/util/Set;

    invoke-interface {v0}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_0
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_0

    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Landroid/animation/Animator$AnimatorListener;

    invoke-interface {v1, p0, p1}, Landroid/animation/Animator$AnimatorListener;->onAnimationStart(Landroid/animation/Animator;Z)V

    goto :goto_0

    :cond_0
    return-void
.end method""",
        'replacement': """.method notifyStart(Z)V
    .registers 4

    goto :goto_a

    nop

    :goto_0
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    goto :goto_5

    nop

    :goto_1
    goto :goto_7

    :goto_2
    goto :goto_4

    nop

    :goto_3
    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    goto :goto_9

    nop

    :goto_4
    return-void

    :goto_5
    if-nez v1, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_3

    nop

    :goto_6
    invoke-interface {v0}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_7
    goto :goto_0

    nop

    :goto_8
    invoke-interface {v1, p0, p1}, Landroid/animation/Animator$AnimatorListener;->onAnimationStart(Landroid/animation/Animator;Z)V

    goto :goto_1

    nop

    :goto_9
    check-cast v1, Landroid/animation/Animator$AnimatorListener;

    goto :goto_8

    nop

    :goto_a
    iget-object v0, p0, Lcom/airbnb/lottie/utils/BaseLottieAnimator;->listeners:Ljava/util/Set;

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_utils_BaseLottieAnimator__notifyUpdate',
        'method': '.method notifyUpdate()V',
        'method_name': 'notifyUpdate',
        'method_anchors': ['iget-object v0, p0, Lcom/airbnb/lottie/utils/BaseLottieAnimator;->updateListeners:Ljava/util/Set;', 'invoke-interface {v0}, Ljava/util/Set;->iterator()Ljava/util/Iterator;', 'invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z', 'if-eqz v1, :cond_0', 'invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;', 'check-cast v1, Landroid/animation/ValueAnimator$AnimatorUpdateListener;', 'invoke-interface {v1, p0}, Landroid/animation/ValueAnimator$AnimatorUpdateListener;->onAnimationUpdate(Landroid/animation/ValueAnimator;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method notifyUpdate()V
    .registers 3

    iget-object v0, p0, Lcom/airbnb/lottie/utils/BaseLottieAnimator;->updateListeners:Ljava/util/Set;

    invoke-interface {v0}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_0
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_0

    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Landroid/animation/ValueAnimator$AnimatorUpdateListener;

    invoke-interface {v1, p0}, Landroid/animation/ValueAnimator$AnimatorUpdateListener;->onAnimationUpdate(Landroid/animation/ValueAnimator;)V

    goto :goto_0

    :cond_0
    return-void
.end method""",
        'replacement': """.method notifyUpdate()V
    .registers 3

    goto :goto_9

    nop

    :goto_0
    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    goto :goto_a

    nop

    :goto_1
    return-void

    :goto_2
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    goto :goto_3

    nop

    :goto_3
    if-nez v1, :cond_0

    goto :goto_8

    :cond_0
    goto :goto_0

    nop

    :goto_4
    invoke-interface {v0}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_5
    goto :goto_2

    nop

    :goto_6
    invoke-interface {v1, p0}, Landroid/animation/ValueAnimator$AnimatorUpdateListener;->onAnimationUpdate(Landroid/animation/ValueAnimator;)V

    goto :goto_7

    nop

    :goto_7
    goto :goto_5

    :goto_8
    goto :goto_1

    nop

    :goto_9
    iget-object v0, p0, Lcom/airbnb/lottie/utils/BaseLottieAnimator;->updateListeners:Ljava/util/Set;

    goto :goto_4

    nop

    :goto_a
    check-cast v1, Landroid/animation/ValueAnimator$AnimatorUpdateListener;

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
