TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/airbnb/lottie/LottieDrawable.smali'
CLASS_FALLBACK_NAMES = ['LottieDrawable.smali']
CLASS_ANCHORS = ['.super Landroid/graphics/drawable/Drawable;', '.implements Landroid/graphics/drawable/Drawable$Callback;', '.implements Landroid/graphics/drawable/Animatable;']

PATCHES = [
    {
        'id': 'com_airbnb_lottie_LottieDrawable__isAnimatingOrWillAnimateOnVisible',
        'method': '.method isAnimatingOrWillAnimateOnVisible()Z',
        'method_name': 'isAnimatingOrWillAnimateOnVisible',
        'method_anchors': ['invoke-virtual {p0}, Landroid/graphics/drawable/Drawable;->isVisible()Z', 'if-eqz v0, :cond_0', 'iget-object p0, p0, Lcom/airbnb/lottie/LottieDrawable;->animator:Lcom/airbnb/lottie/utils/LottieValueAnimator;', 'invoke-virtual {p0}, Lcom/airbnb/lottie/utils/LottieValueAnimator;->isRunning()Z', 'return p0', 'iget-object p0, p0, Lcom/airbnb/lottie/LottieDrawable;->onVisibleAction:Lcom/airbnb/lottie/LottieDrawable$OnVisibleAction;', 'sget-object v0, Lcom/airbnb/lottie/LottieDrawable$OnVisibleAction;->PLAY:Lcom/airbnb/lottie/LottieDrawable$OnVisibleAction;', 'if-eq p0, v0, :cond_2'],
        'type': 'method_replace',
        'search': """.method isAnimatingOrWillAnimateOnVisible()Z
    .registers 2

    invoke-virtual {p0}, Landroid/graphics/drawable/Drawable;->isVisible()Z

    move-result v0

    if-eqz v0, :cond_0

    iget-object p0, p0, Lcom/airbnb/lottie/LottieDrawable;->animator:Lcom/airbnb/lottie/utils/LottieValueAnimator;

    invoke-virtual {p0}, Lcom/airbnb/lottie/utils/LottieValueAnimator;->isRunning()Z

    move-result p0

    return p0

    :cond_0
    iget-object p0, p0, Lcom/airbnb/lottie/LottieDrawable;->onVisibleAction:Lcom/airbnb/lottie/LottieDrawable$OnVisibleAction;

    sget-object v0, Lcom/airbnb/lottie/LottieDrawable$OnVisibleAction;->PLAY:Lcom/airbnb/lottie/LottieDrawable$OnVisibleAction;

    if-eq p0, v0, :cond_2

    sget-object v0, Lcom/airbnb/lottie/LottieDrawable$OnVisibleAction;->RESUME:Lcom/airbnb/lottie/LottieDrawable$OnVisibleAction;

    if-ne p0, v0, :cond_1

    goto :goto_0

    :cond_1
    const/4 p0, 0x0

    return p0

    :cond_2
    :goto_0
    const/4 p0, 0x1

    return p0
.end method""",
        'replacement': """.method isAnimatingOrWillAnimateOnVisible()Z
    .registers 2

    goto :goto_7

    nop

    :goto_0
    sget-object v0, Lcom/airbnb/lottie/LottieDrawable$OnVisibleAction;->RESUME:Lcom/airbnb/lottie/LottieDrawable$OnVisibleAction;

    goto :goto_c

    nop

    :goto_1
    return p0

    :goto_2
    goto :goto_3

    nop

    :goto_3
    iget-object p0, p0, Lcom/airbnb/lottie/LottieDrawable;->onVisibleAction:Lcom/airbnb/lottie/LottieDrawable$OnVisibleAction;

    goto :goto_4

    nop

    :goto_4
    sget-object v0, Lcom/airbnb/lottie/LottieDrawable$OnVisibleAction;->PLAY:Lcom/airbnb/lottie/LottieDrawable$OnVisibleAction;

    goto :goto_d

    nop

    :goto_5
    iget-object p0, p0, Lcom/airbnb/lottie/LottieDrawable;->animator:Lcom/airbnb/lottie/utils/LottieValueAnimator;

    goto :goto_11

    nop

    :goto_6
    if-nez v0, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_5

    nop

    :goto_7
    invoke-virtual {p0}, Landroid/graphics/drawable/Drawable;->isVisible()Z

    move-result v0

    goto :goto_6

    nop

    :goto_8
    const/4 p0, 0x1

    goto :goto_9

    nop

    :goto_9
    return p0

    :goto_a
    return p0

    :goto_b
    goto :goto_8

    nop

    :goto_c
    if-eq p0, v0, :cond_1

    goto :goto_f

    :cond_1
    goto :goto_e

    nop

    :goto_d
    if-ne p0, v0, :cond_2

    goto :goto_b

    :cond_2
    goto :goto_0

    nop

    :goto_e
    goto :goto_b

    :goto_f
    goto :goto_10

    nop

    :goto_10
    const/4 p0, 0x0

    goto :goto_a

    nop

    :goto_11
    invoke-virtual {p0}, Lcom/airbnb/lottie/utils/LottieValueAnimator;->isRunning()Z

    move-result p0

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
