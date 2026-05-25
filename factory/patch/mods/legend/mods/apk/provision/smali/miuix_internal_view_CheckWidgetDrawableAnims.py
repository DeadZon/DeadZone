TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/internal/view/CheckWidgetDrawableAnims.smali'
CLASS_FALLBACK_NAMES = ['CheckWidgetDrawableAnims.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'miuix_internal_view_CheckWidgetDrawableAnims__startPressedAnim',
        'method': '.method protected startPressedAnim(ZZ)V',
        'method_name': 'startPressedAnim',
        'method_anchors': ['if-eqz p2, :cond_a', 'invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;', 'invoke-static {}, Landroid/os/Looper;->getMainLooper()Landroid/os/Looper;', 'invoke-virtual {v0}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;', 'if-eq p2, v0, :cond_0', 'iget-object p2, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mPressedScaleAnim:Lmiuix/animation/physics/SpringAnimation;', 'invoke-virtual {p2}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z', 'if-nez p2, :cond_1'],
        'type': 'method_replace',
        'search': """.method protected startPressedAnim(ZZ)V
    .registers 4

    if-eqz p2, :cond_a

    invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;

    move-result-object p2

    invoke-static {}, Landroid/os/Looper;->getMainLooper()Landroid/os/Looper;

    move-result-object v0

    invoke-virtual {v0}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;

    move-result-object v0

    if-eq p2, v0, :cond_0

    goto :goto_0

    :cond_0
    iget-object p2, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mPressedScaleAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p2}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p2

    if-nez p2, :cond_1

    iget-object p2, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mPressedScaleAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p2}, Lmiuix/animation/physics/SpringAnimation;->start()V

    :cond_1
    iget-object p2, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mParentPressAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p2}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p2

    if-nez p2, :cond_2

    iget-object p2, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mParentPressAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p2}, Lmiuix/animation/physics/SpringAnimation;->start()V

    :cond_2
    if-nez p1, :cond_3

    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mPressedBlackAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p1

    if-nez p1, :cond_3

    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mPressedBlackAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p1}, Lmiuix/animation/physics/SpringAnimation;->start()V

    :cond_3
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlackAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p1

    if-eqz p1, :cond_4

    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlackAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->cancel()V

    :cond_4
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->unPressedScaleAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p1

    if-eqz p1, :cond_5

    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->unPressedScaleAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->cancel()V

    :cond_5
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mParentUnPressAlphaAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p1

    if-eqz p1, :cond_6

    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mParentUnPressAlphaAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->cancel()V

    :cond_6
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mParentCheckedUnPressScaleAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p1

    if-eqz p1, :cond_7

    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mParentCheckedUnPressScaleAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->cancel()V

    :cond_7
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mParentUnCheckedUnPressScaleAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p1

    if-eqz p1, :cond_8

    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mParentUnCheckedUnPressScaleAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->cancel()V

    :cond_8
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlueHideAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p1

    if-eqz p1, :cond_9

    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlueHideAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->cancel()V

    :cond_9
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlueShowAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p1

    if-eqz p1, :cond_a

    iget-object p0, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlueShowAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p0}, Lmiuix/animation/physics/DynamicAnimation;->cancel()V

    :cond_a
    :goto_0
    return-void
.end method""",
        'replacement': """.method protected startPressedAnim(ZZ)V
    .registers 4

    goto :goto_29

    nop

    :goto_0
    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->cancel()V

    :goto_1
    goto :goto_11

    nop

    :goto_2
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mParentUnCheckedUnPressScaleAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_39

    nop

    :goto_3
    invoke-virtual {v0}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;

    move-result-object v0

    goto :goto_6

    nop

    :goto_4
    if-eqz p2, :cond_0

    goto :goto_37

    :cond_0
    goto :goto_a

    nop

    :goto_5
    return-void

    :goto_6
    if-ne p2, v0, :cond_1

    goto :goto_30

    :cond_1
    goto :goto_2f

    nop

    :goto_7
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mParentCheckedUnPressScaleAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_1a

    nop

    :goto_8
    iget-object p2, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mParentPressAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_1c

    nop

    :goto_9
    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p1

    goto :goto_17

    nop

    :goto_a
    iget-object p2, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mPressedScaleAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_36

    nop

    :goto_b
    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->cancel()V

    :goto_c
    goto :goto_20

    nop

    :goto_d
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlueShowAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_1e

    nop

    :goto_e
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->unPressedScaleAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_41

    nop

    :goto_f
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlackAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_34

    nop

    :goto_10
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mParentUnPressAlphaAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_b

    nop

    :goto_11
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mParentUnPressAlphaAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_27

    nop

    :goto_12
    invoke-virtual {p2}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p2

    goto :goto_4

    nop

    :goto_13
    invoke-static {}, Landroid/os/Looper;->getMainLooper()Landroid/os/Looper;

    move-result-object v0

    goto :goto_3

    nop

    :goto_14
    invoke-virtual {p2}, Lmiuix/animation/physics/SpringAnimation;->start()V

    :goto_15
    goto :goto_1f

    nop

    :goto_16
    if-nez p1, :cond_2

    goto :goto_22

    :cond_2
    goto :goto_1d

    nop

    :goto_17
    if-nez p1, :cond_3

    goto :goto_35

    :cond_3
    goto :goto_f

    nop

    :goto_18
    if-eqz p2, :cond_4

    goto :goto_15

    :cond_4
    goto :goto_38

    nop

    :goto_19
    if-nez p1, :cond_5

    goto :goto_3e

    :cond_5
    goto :goto_3a

    nop

    :goto_1a
    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->cancel()V

    :goto_1b
    goto :goto_2

    nop

    :goto_1c
    invoke-virtual {p2}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p2

    goto :goto_18

    nop

    :goto_1d
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mParentUnCheckedUnPressScaleAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_21

    nop

    :goto_1e
    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p1

    goto :goto_2d

    nop

    :goto_1f
    if-eqz p1, :cond_6

    goto :goto_2c

    :cond_6
    goto :goto_28

    nop

    :goto_20
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mParentCheckedUnPressScaleAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_33

    nop

    :goto_21
    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->cancel()V

    :goto_22
    goto :goto_2a

    nop

    :goto_23
    if-nez p1, :cond_7

    goto :goto_1b

    :cond_7
    goto :goto_7

    nop

    :goto_24
    if-eqz p1, :cond_8

    goto :goto_2c

    :cond_8
    goto :goto_44

    nop

    :goto_25
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlackAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_9

    nop

    :goto_26
    invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;

    move-result-object p2

    goto :goto_13

    nop

    :goto_27
    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p1

    goto :goto_3c

    nop

    :goto_28
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mPressedBlackAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_42

    nop

    :goto_29
    if-nez p2, :cond_9

    goto :goto_40

    :cond_9
    goto :goto_26

    nop

    :goto_2a
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlueHideAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_32

    nop

    :goto_2b
    invoke-virtual {p1}, Lmiuix/animation/physics/SpringAnimation;->start()V

    :goto_2c
    goto :goto_25

    nop

    :goto_2d
    if-nez p1, :cond_a

    goto :goto_40

    :cond_a
    goto :goto_2e

    nop

    :goto_2e
    iget-object p0, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlueShowAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_3f

    nop

    :goto_2f
    goto :goto_40

    :goto_30
    goto :goto_3b

    nop

    :goto_31
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->unPressedScaleAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_0

    nop

    :goto_32
    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p1

    goto :goto_19

    nop

    :goto_33
    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p1

    goto :goto_23

    nop

    :goto_34
    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->cancel()V

    :goto_35
    goto :goto_e

    nop

    :goto_36
    invoke-virtual {p2}, Lmiuix/animation/physics/SpringAnimation;->start()V

    :goto_37
    goto :goto_8

    nop

    :goto_38
    iget-object p2, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mParentPressAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_14

    nop

    :goto_39
    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p1

    goto :goto_16

    nop

    :goto_3a
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlueHideAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_3d

    nop

    :goto_3b
    iget-object p2, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mPressedScaleAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_12

    nop

    :goto_3c
    if-nez p1, :cond_b

    goto :goto_c

    :cond_b
    goto :goto_10

    nop

    :goto_3d
    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->cancel()V

    :goto_3e
    goto :goto_d

    nop

    :goto_3f
    invoke-virtual {p0}, Lmiuix/animation/physics/DynamicAnimation;->cancel()V

    :goto_40
    goto :goto_5

    nop

    :goto_41
    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p1

    goto :goto_43

    nop

    :goto_42
    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p1

    goto :goto_24

    nop

    :goto_43
    if-nez p1, :cond_c

    goto :goto_1

    :cond_c
    goto :goto_31

    nop

    :goto_44
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mPressedBlackAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_2b

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_view_CheckWidgetDrawableAnims__startUnPressedAnim',
        'method': '.method protected startUnPressedAnim(ZZ)V',
        'method_name': 'startUnPressedAnim',
        'method_anchors': ['if-eqz p2, :cond_c', 'invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;', 'invoke-static {}, Landroid/os/Looper;->getMainLooper()Landroid/os/Looper;', 'invoke-virtual {v0}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;', 'if-eq p2, v0, :cond_0', 'iget-object p2, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mPressedScaleAnim:Lmiuix/animation/physics/SpringAnimation;', 'invoke-virtual {p2}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z', 'if-eqz p2, :cond_1'],
        'type': 'method_replace',
        'search': """.method protected startUnPressedAnim(ZZ)V
    .registers 5

    if-eqz p2, :cond_c

    invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;

    move-result-object p2

    invoke-static {}, Landroid/os/Looper;->getMainLooper()Landroid/os/Looper;

    move-result-object v0

    invoke-virtual {v0}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;

    move-result-object v0

    if-eq p2, v0, :cond_0

    goto :goto_1

    :cond_0
    iget-object p2, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mPressedScaleAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p2}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p2

    if-eqz p2, :cond_1

    iget-object p2, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mPressedScaleAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p2}, Lmiuix/animation/physics/DynamicAnimation;->cancel()V

    :cond_1
    iget-object p2, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mParentPressAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p2}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p2

    if-eqz p2, :cond_2

    iget-object p2, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mParentPressAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p2}, Lmiuix/animation/physics/DynamicAnimation;->cancel()V

    :cond_2
    iget-object p2, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mPressedBlackAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p2}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p2

    if-eqz p2, :cond_3

    iget-object p2, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mPressedBlackAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p2}, Lmiuix/animation/physics/DynamicAnimation;->cancel()V

    :cond_3
    iget-object p2, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlackAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p2}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p2

    if-nez p2, :cond_4

    iget-object p2, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlackAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p2}, Lmiuix/animation/physics/SpringAnimation;->start()V

    :cond_4
    if-eqz p1, :cond_8

    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlueHideAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p1

    if-eqz p1, :cond_5

    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlueHideAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->cancel()V

    :cond_5
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlueShowAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p1

    if-nez p1, :cond_6

    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlueShowAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p1}, Lmiuix/animation/physics/SpringAnimation;->start()V

    :cond_6
    new-instance p1, Landroid/os/Handler;

    invoke-direct {p1}, Landroid/os/Handler;-><init>()V

    new-instance p2, Lmiuix/internal/view/CheckWidgetDrawableAnims$7;

    invoke-direct {p2, p0}, Lmiuix/internal/view/CheckWidgetDrawableAnims$7;-><init>(Lmiuix/internal/view/CheckWidgetDrawableAnims;)V

    const-wide/16 v0, 0x32

    invoke-virtual {p1, p2, v0, v1}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z

    iget-boolean p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mIsSingleSelection:Z

    if-eqz p1, :cond_7

    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->unPressedScaleAnim:Lmiuix/animation/physics/SpringAnimation;

    const/high16 p2, 0x41200000

    invoke-virtual {p1, p2}, Lmiuix/animation/physics/DynamicAnimation;->setStartVelocity(F)Lmiuix/animation/physics/DynamicAnimation;

    goto :goto_0

    :cond_7
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->unPressedScaleAnim:Lmiuix/animation/physics/SpringAnimation;

    const/high16 p2, 0x40a00000

    invoke-virtual {p1, p2}, Lmiuix/animation/physics/DynamicAnimation;->setStartVelocity(F)Lmiuix/animation/physics/DynamicAnimation;

    goto :goto_0

    :cond_8
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlueShowAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p1

    if-eqz p1, :cond_9

    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlueShowAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->cancel()V

    :cond_9
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlueHideAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p1

    if-nez p1, :cond_a

    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlueHideAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p1}, Lmiuix/animation/physics/SpringAnimation;->start()V

    :cond_a
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mParentUnCheckedUnPressScaleAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p1

    if-nez p1, :cond_b

    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mParentUnCheckedUnPressScaleAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p1}, Lmiuix/animation/physics/SpringAnimation;->start()V

    :cond_b
    :goto_0
    iget-object p0, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->unPressedScaleAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p0}, Lmiuix/animation/physics/SpringAnimation;->start()V

    return-void

    :cond_c
    :goto_1
    const/high16 p2, 0x437f0000

    if-eqz p1, :cond_d

    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mBlueDrawable:Lmiuix/internal/view/CheckWidgetCircleDrawable;

    iget-object p0, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlueShowAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p0}, Lmiuix/animation/physics/SpringAnimation;->getSpring()Lmiuix/animation/physics/SpringForce;

    move-result-object p0

    invoke-virtual {p0}, Lmiuix/animation/physics/SpringForce;->getFinalPosition()F

    move-result p0

    mul-float/2addr p0, p2

    float-to-int p0, p0

    invoke-virtual {p1, p0}, Lmiuix/internal/view/CheckWidgetCircleDrawable;->setAlpha(I)V

    return-void

    :cond_d
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mBlueDrawable:Lmiuix/internal/view/CheckWidgetCircleDrawable;

    iget-object p0, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlueHideAnim:Lmiuix/animation/physics/SpringAnimation;

    invoke-virtual {p0}, Lmiuix/animation/physics/SpringAnimation;->getSpring()Lmiuix/animation/physics/SpringForce;

    move-result-object p0

    invoke-virtual {p0}, Lmiuix/animation/physics/SpringForce;->getFinalPosition()F

    move-result p0

    mul-float/2addr p0, p2

    float-to-int p0, p0

    invoke-virtual {p1, p0}, Lmiuix/internal/view/CheckWidgetCircleDrawable;->setAlpha(I)V

    return-void
.end method""",
        'replacement': """.method protected startUnPressedAnim(ZZ)V
    .registers 5

    goto :goto_49

    nop

    :goto_0
    invoke-virtual {p2}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p2

    goto :goto_1

    nop

    :goto_1
    if-nez p2, :cond_0

    goto :goto_36

    :cond_0
    goto :goto_34

    nop

    :goto_2
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mParentUnCheckedUnPressScaleAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_f

    nop

    :goto_3
    invoke-virtual {p2}, Lmiuix/animation/physics/DynamicAnimation;->cancel()V

    :goto_4
    goto :goto_44

    nop

    :goto_5
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlueShowAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_1f

    nop

    :goto_6
    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p1

    goto :goto_66

    nop

    :goto_7
    iget-boolean p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mIsSingleSelection:Z

    goto :goto_50

    nop

    :goto_8
    invoke-virtual {p2}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p2

    goto :goto_25

    nop

    :goto_9
    invoke-virtual {v0}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;

    move-result-object v0

    goto :goto_5a

    nop

    :goto_a
    iget-object p2, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlackAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_55

    nop

    :goto_b
    new-instance p2, Lmiuix/internal/view/CheckWidgetDrawableAnims$7;

    goto :goto_4c

    nop

    :goto_c
    iget-object p2, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mPressedBlackAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_8

    nop

    :goto_d
    invoke-virtual {p0}, Lmiuix/animation/physics/SpringForce;->getFinalPosition()F

    move-result p0

    goto :goto_28

    nop

    :goto_e
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->unPressedScaleAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_5b

    nop

    :goto_f
    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p1

    goto :goto_4a

    nop

    :goto_10
    invoke-virtual {p1, p0}, Lmiuix/internal/view/CheckWidgetCircleDrawable;->setAlpha(I)V

    goto :goto_54

    nop

    :goto_11
    invoke-static {}, Landroid/os/Looper;->getMainLooper()Landroid/os/Looper;

    move-result-object v0

    goto :goto_9

    nop

    :goto_12
    iget-object p0, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlueShowAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_1c

    nop

    :goto_13
    if-eqz p2, :cond_1

    goto :goto_56

    :cond_1
    goto :goto_a

    nop

    :goto_14
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlueShowAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_60

    nop

    :goto_15
    mul-float/2addr p0, p2

    goto :goto_3e

    nop

    :goto_16
    if-nez p2, :cond_2

    goto :goto_30

    :cond_2
    goto :goto_4d

    nop

    :goto_17
    iget-object p2, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mParentPressAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_2d

    nop

    :goto_18
    iget-object p2, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mPressedScaleAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_0

    nop

    :goto_19
    const-wide/16 v0, 0x32

    goto :goto_53

    nop

    :goto_1a
    if-nez p1, :cond_3

    goto :goto_33

    :cond_3
    goto :goto_24

    nop

    :goto_1b
    iget-object p0, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlueHideAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_48

    nop

    :goto_1c
    invoke-virtual {p0}, Lmiuix/animation/physics/SpringAnimation;->getSpring()Lmiuix/animation/physics/SpringForce;

    move-result-object p0

    goto :goto_20

    nop

    :goto_1d
    iget-object p0, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->unPressedScaleAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_42

    nop

    :goto_1e
    invoke-virtual {p2}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p2

    goto :goto_13

    nop

    :goto_1f
    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p1

    goto :goto_62

    nop

    :goto_20
    invoke-virtual {p0}, Lmiuix/animation/physics/SpringForce;->getFinalPosition()F

    move-result p0

    goto :goto_15

    nop

    :goto_21
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->unPressedScaleAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_4b

    nop

    :goto_22
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlueHideAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_51

    nop

    :goto_23
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlueHideAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_37

    nop

    :goto_24
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mBlueDrawable:Lmiuix/internal/view/CheckWidgetCircleDrawable;

    goto :goto_12

    nop

    :goto_25
    if-nez p2, :cond_4

    goto :goto_4

    :cond_4
    goto :goto_47

    nop

    :goto_26
    return-void

    :goto_27
    goto :goto_3f

    nop

    :goto_28
    mul-float/2addr p0, p2

    goto :goto_3a

    nop

    :goto_29
    new-instance p1, Landroid/os/Handler;

    goto :goto_2c

    nop

    :goto_2a
    if-nez p1, :cond_5

    goto :goto_58

    :cond_5
    goto :goto_5e

    nop

    :goto_2b
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mBlueDrawable:Lmiuix/internal/view/CheckWidgetCircleDrawable;

    goto :goto_1b

    nop

    :goto_2c
    invoke-direct {p1}, Landroid/os/Handler;-><init>()V

    goto :goto_b

    nop

    :goto_2d
    invoke-virtual {p2}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p2

    goto :goto_16

    nop

    :goto_2e
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mParentUnCheckedUnPressScaleAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_4e

    nop

    :goto_2f
    invoke-virtual {p2}, Lmiuix/animation/physics/DynamicAnimation;->cancel()V

    :goto_30
    goto :goto_c

    nop

    :goto_31
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlueHideAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_6

    nop

    :goto_32
    return-void

    :goto_33
    goto :goto_2b

    nop

    :goto_34
    iget-object p2, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mPressedScaleAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_35

    nop

    :goto_35
    invoke-virtual {p2}, Lmiuix/animation/physics/DynamicAnimation;->cancel()V

    :goto_36
    goto :goto_17

    nop

    :goto_37
    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p1

    goto :goto_59

    nop

    :goto_38
    goto :goto_27

    :goto_39
    goto :goto_18

    nop

    :goto_3a
    float-to-int p0, p0

    goto :goto_10

    nop

    :goto_3b
    invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;

    move-result-object p2

    goto :goto_11

    nop

    :goto_3c
    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->cancel()V

    :goto_3d
    goto :goto_5

    nop

    :goto_3e
    float-to-int p0, p0

    goto :goto_5c

    nop

    :goto_3f
    const/high16 p2, 0x437f0000

    goto :goto_1a

    nop

    :goto_40
    goto :goto_4f

    :goto_41
    goto :goto_43

    nop

    :goto_42
    invoke-virtual {p0}, Lmiuix/animation/physics/SpringAnimation;->start()V

    goto :goto_26

    nop

    :goto_43
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlueShowAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_45

    nop

    :goto_44
    iget-object p2, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlackAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_1e

    nop

    :goto_45
    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->isRunning()Z

    move-result p1

    goto :goto_2a

    nop

    :goto_46
    invoke-virtual {p1, p2}, Lmiuix/animation/physics/DynamicAnimation;->setStartVelocity(F)Lmiuix/animation/physics/DynamicAnimation;

    goto :goto_40

    nop

    :goto_47
    iget-object p2, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mPressedBlackAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_3

    nop

    :goto_48
    invoke-virtual {p0}, Lmiuix/animation/physics/SpringAnimation;->getSpring()Lmiuix/animation/physics/SpringForce;

    move-result-object p0

    goto :goto_d

    nop

    :goto_49
    if-nez p2, :cond_6

    goto :goto_27

    :cond_6
    goto :goto_3b

    nop

    :goto_4a
    if-eqz p1, :cond_7

    goto :goto_4f

    :cond_7
    goto :goto_2e

    nop

    :goto_4b
    const/high16 p2, 0x40a00000

    goto :goto_46

    nop

    :goto_4c
    invoke-direct {p2, p0}, Lmiuix/internal/view/CheckWidgetDrawableAnims$7;-><init>(Lmiuix/internal/view/CheckWidgetDrawableAnims;)V

    goto :goto_19

    nop

    :goto_4d
    iget-object p2, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mParentPressAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_2f

    nop

    :goto_4e
    invoke-virtual {p1}, Lmiuix/animation/physics/SpringAnimation;->start()V

    :goto_4f
    goto :goto_1d

    nop

    :goto_50
    if-nez p1, :cond_8

    goto :goto_65

    :cond_8
    goto :goto_e

    nop

    :goto_51
    invoke-virtual {p1}, Lmiuix/animation/physics/SpringAnimation;->start()V

    :goto_52
    goto :goto_2

    nop

    :goto_53
    invoke-virtual {p1, p2, v0, v1}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z

    goto :goto_7

    nop

    :goto_54
    return-void

    :goto_55
    invoke-virtual {p2}, Lmiuix/animation/physics/SpringAnimation;->start()V

    :goto_56
    goto :goto_5f

    nop

    :goto_57
    invoke-virtual {p1}, Lmiuix/animation/physics/DynamicAnimation;->cancel()V

    :goto_58
    goto :goto_31

    nop

    :goto_59
    if-nez p1, :cond_9

    goto :goto_3d

    :cond_9
    goto :goto_63

    nop

    :goto_5a
    if-ne p2, v0, :cond_a

    goto :goto_39

    :cond_a
    goto :goto_38

    nop

    :goto_5b
    const/high16 p2, 0x41200000

    goto :goto_5d

    nop

    :goto_5c
    invoke-virtual {p1, p0}, Lmiuix/internal/view/CheckWidgetCircleDrawable;->setAlpha(I)V

    goto :goto_32

    nop

    :goto_5d
    invoke-virtual {p1, p2}, Lmiuix/animation/physics/DynamicAnimation;->setStartVelocity(F)Lmiuix/animation/physics/DynamicAnimation;

    goto :goto_64

    nop

    :goto_5e
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlueShowAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_57

    nop

    :goto_5f
    if-nez p1, :cond_b

    goto :goto_41

    :cond_b
    goto :goto_23

    nop

    :goto_60
    invoke-virtual {p1}, Lmiuix/animation/physics/SpringAnimation;->start()V

    :goto_61
    goto :goto_29

    nop

    :goto_62
    if-eqz p1, :cond_c

    goto :goto_61

    :cond_c
    goto :goto_14

    nop

    :goto_63
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mUnPressedBlueHideAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_3c

    nop

    :goto_64
    goto :goto_4f

    :goto_65
    goto :goto_21

    nop

    :goto_66
    if-eqz p1, :cond_d

    goto :goto_52

    :cond_d
    goto :goto_22

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_view_CheckWidgetDrawableAnims__verifyChecked',
        'method': '.method protected verifyChecked(ZZ)V',
        'method_name': 'verifyChecked',
        'method_anchors': ['if-eqz p2, :cond_1', 'if-eqz p1, :cond_0', 'iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mBlueDrawable:Lmiuix/internal/view/CheckWidgetCircleDrawable;', 'invoke-virtual {p1, p2}, Lmiuix/internal/view/CheckWidgetCircleDrawable;->setAlpha(I)V', 'iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mBlackDrawable:Lmiuix/internal/view/CheckWidgetCircleDrawable;', 'invoke-virtual {p1, p2}, Lmiuix/internal/view/CheckWidgetCircleDrawable;->setAlpha(I)V', 'iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mBlueDrawable:Lmiuix/internal/view/CheckWidgetCircleDrawable;', 'invoke-virtual {p1, v0}, Lmiuix/internal/view/CheckWidgetCircleDrawable;->setAlpha(I)V'],
        'type': 'method_replace',
        'search': """.method protected verifyChecked(ZZ)V
    .registers 4

    const/4 v0, 0x0

    if-eqz p2, :cond_1

    if-eqz p1, :cond_0

    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mBlueDrawable:Lmiuix/internal/view/CheckWidgetCircleDrawable;

    const/16 p2, 0xff

    invoke-virtual {p1, p2}, Lmiuix/internal/view/CheckWidgetCircleDrawable;->setAlpha(I)V

    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mBlackDrawable:Lmiuix/internal/view/CheckWidgetCircleDrawable;

    const/16 p2, 0x19

    invoke-virtual {p1, p2}, Lmiuix/internal/view/CheckWidgetCircleDrawable;->setAlpha(I)V

    goto :goto_0

    :cond_0
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mBlueDrawable:Lmiuix/internal/view/CheckWidgetCircleDrawable;

    invoke-virtual {p1, v0}, Lmiuix/internal/view/CheckWidgetCircleDrawable;->setAlpha(I)V

    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mBlackDrawable:Lmiuix/internal/view/CheckWidgetCircleDrawable;

    invoke-virtual {p1, v0}, Lmiuix/internal/view/CheckWidgetCircleDrawable;->setAlpha(I)V

    :goto_0
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mGrayDrawable:Lmiuix/internal/view/CheckWidgetCircleDrawable;

    iget p0, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mBackgroundNormalAlpha:I

    invoke-virtual {p1, p0}, Lmiuix/internal/view/CheckWidgetCircleDrawable;->setAlpha(I)V

    return-void

    :cond_1
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mBlueDrawable:Lmiuix/internal/view/CheckWidgetCircleDrawable;

    invoke-virtual {p1, v0}, Lmiuix/internal/view/CheckWidgetCircleDrawable;->setAlpha(I)V

    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mBlackDrawable:Lmiuix/internal/view/CheckWidgetCircleDrawable;

    invoke-virtual {p1, v0}, Lmiuix/internal/view/CheckWidgetCircleDrawable;->setAlpha(I)V

    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mGrayDrawable:Lmiuix/internal/view/CheckWidgetCircleDrawable;

    iget p0, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mBackgroundDisableAlpha:I

    invoke-virtual {p1, p0}, Lmiuix/internal/view/CheckWidgetCircleDrawable;->setAlpha(I)V

    return-void
.end method""",
        'replacement': """.method protected verifyChecked(ZZ)V
    .registers 4

    goto :goto_1c

    nop

    :goto_0
    invoke-virtual {p1, v0}, Lmiuix/internal/view/CheckWidgetCircleDrawable;->setAlpha(I)V

    goto :goto_8

    nop

    :goto_1
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mGrayDrawable:Lmiuix/internal/view/CheckWidgetCircleDrawable;

    goto :goto_15

    nop

    :goto_2
    iget p0, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mBackgroundDisableAlpha:I

    goto :goto_7

    nop

    :goto_3
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mBlackDrawable:Lmiuix/internal/view/CheckWidgetCircleDrawable;

    goto :goto_18

    nop

    :goto_4
    return-void

    :goto_5
    goto :goto_13

    nop

    :goto_6
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mBlackDrawable:Lmiuix/internal/view/CheckWidgetCircleDrawable;

    goto :goto_d

    nop

    :goto_7
    invoke-virtual {p1, p0}, Lmiuix/internal/view/CheckWidgetCircleDrawable;->setAlpha(I)V

    goto :goto_f

    nop

    :goto_8
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mBlackDrawable:Lmiuix/internal/view/CheckWidgetCircleDrawable;

    goto :goto_11

    nop

    :goto_9
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mBlueDrawable:Lmiuix/internal/view/CheckWidgetCircleDrawable;

    goto :goto_0

    nop

    :goto_a
    const/16 p2, 0xff

    goto :goto_17

    nop

    :goto_b
    goto :goto_12

    :goto_c
    goto :goto_9

    nop

    :goto_d
    invoke-virtual {p1, v0}, Lmiuix/internal/view/CheckWidgetCircleDrawable;->setAlpha(I)V

    goto :goto_19

    nop

    :goto_e
    invoke-virtual {p1, p0}, Lmiuix/internal/view/CheckWidgetCircleDrawable;->setAlpha(I)V

    goto :goto_4

    nop

    :goto_f
    return-void

    :goto_10
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mBlueDrawable:Lmiuix/internal/view/CheckWidgetCircleDrawable;

    goto :goto_a

    nop

    :goto_11
    invoke-virtual {p1, v0}, Lmiuix/internal/view/CheckWidgetCircleDrawable;->setAlpha(I)V

    :goto_12
    goto :goto_1

    nop

    :goto_13
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mBlueDrawable:Lmiuix/internal/view/CheckWidgetCircleDrawable;

    goto :goto_14

    nop

    :goto_14
    invoke-virtual {p1, v0}, Lmiuix/internal/view/CheckWidgetCircleDrawable;->setAlpha(I)V

    goto :goto_6

    nop

    :goto_15
    iget p0, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mBackgroundNormalAlpha:I

    goto :goto_e

    nop

    :goto_16
    if-nez p1, :cond_0

    goto :goto_c

    :cond_0
    goto :goto_10

    nop

    :goto_17
    invoke-virtual {p1, p2}, Lmiuix/internal/view/CheckWidgetCircleDrawable;->setAlpha(I)V

    goto :goto_3

    nop

    :goto_18
    const/16 p2, 0x19

    goto :goto_1a

    nop

    :goto_19
    iget-object p1, p0, Lmiuix/internal/view/CheckWidgetDrawableAnims;->mGrayDrawable:Lmiuix/internal/view/CheckWidgetCircleDrawable;

    goto :goto_2

    nop

    :goto_1a
    invoke-virtual {p1, p2}, Lmiuix/internal/view/CheckWidgetCircleDrawable;->setAlpha(I)V

    goto :goto_b

    nop

    :goto_1b
    if-nez p2, :cond_1

    goto :goto_5

    :cond_1
    goto :goto_16

    nop

    :goto_1c
    const/4 v0, 0x0

    goto :goto_1b

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
