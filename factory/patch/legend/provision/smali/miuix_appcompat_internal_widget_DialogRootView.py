TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/widget/DialogRootView.smali'
CLASS_FALLBACK_NAMES = ['DialogRootView.smali']
CLASS_ANCHORS = ['.super Landroid/widget/FrameLayout;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_widget_DialogRootView__onAttachedToWindow',
        'method': '.method protected onAttachedToWindow()V',
        'method_name': 'onAttachedToWindow',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/FrameLayout;->onAttachedToWindow()V', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;', 'iget-object p0, p0, Lmiuix/appcompat/internal/widget/DialogRootView;->mComponentCallbacks:Landroid/content/ComponentCallbacks;', 'invoke-virtual {v0, p0}, Landroid/content/Context;->registerComponentCallbacks(Landroid/content/ComponentCallbacks;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onAttachedToWindow()V
    .registers 2

    invoke-super {p0}, Landroid/widget/FrameLayout;->onAttachedToWindow()V

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;

    move-result-object v0

    iget-object p0, p0, Lmiuix/appcompat/internal/widget/DialogRootView;->mComponentCallbacks:Landroid/content/ComponentCallbacks;

    invoke-virtual {v0, p0}, Landroid/content/Context;->registerComponentCallbacks(Landroid/content/ComponentCallbacks;)V

    return-void
.end method""",
        'replacement': """.method protected onAttachedToWindow()V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    invoke-virtual {v0, p0}, Landroid/content/Context;->registerComponentCallbacks(Landroid/content/ComponentCallbacks;)V

    goto :goto_2

    nop

    :goto_1
    invoke-super {p0}, Landroid/widget/FrameLayout;->onAttachedToWindow()V

    goto :goto_4

    nop

    :goto_2
    return-void

    :goto_3
    iget-object p0, p0, Lmiuix/appcompat/internal/widget/DialogRootView;->mComponentCallbacks:Landroid/content/ComponentCallbacks;

    goto :goto_0

    nop

    :goto_4
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;

    move-result-object v0

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_widget_DialogRootView__onConfigurationChanged',
        'method': '.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V',
        'method_name': 'onConfigurationChanged',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/widget/FrameLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;', 'invoke-static {v0}, Lmiuix/autodensity/DensityUtil;->findAutoDensityContextWrapper(Landroid/content/Context;)Lmiuix/autodensity/AutoDensityContextWrapper;', 'if-eqz v0, :cond_0', 'invoke-virtual {v0}, Lmiuix/autodensity/AutoDensityContextWrapper;->getOriginConfiguration()Landroid/content/res/Configuration;', 'invoke-virtual {v0, p1}, Landroid/content/res/Configuration;->setTo(Landroid/content/res/Configuration;)V', 'iget-boolean v0, p0, Lmiuix/appcompat/internal/widget/DialogRootView;->mNotifyConfigChanged:Z', 'if-nez v0, :cond_0'],
        'type': 'method_replace',
        'search': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 3

    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-static {v0}, Lmiuix/autodensity/DensityUtil;->findAutoDensityContextWrapper(Landroid/content/Context;)Lmiuix/autodensity/AutoDensityContextWrapper;

    move-result-object v0

    if-eqz v0, :cond_0

    invoke-virtual {v0}, Lmiuix/autodensity/AutoDensityContextWrapper;->getOriginConfiguration()Landroid/content/res/Configuration;

    move-result-object v0

    invoke-virtual {v0, p1}, Landroid/content/res/Configuration;->setTo(Landroid/content/res/Configuration;)V

    iget-boolean v0, p0, Lmiuix/appcompat/internal/widget/DialogRootView;->mNotifyConfigChanged:Z

    if-nez v0, :cond_0

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;

    move-result-object p0

    invoke-static {p0, p1}, Lmiuix/autodensity/AutoDensityConfig;->updateDensityOverrideConfiguration(Landroid/content/Context;Landroid/content/res/Configuration;)Landroid/content/res/Configuration;

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 3

    goto :goto_7

    nop

    :goto_0
    if-eqz v0, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_2

    nop

    :goto_1
    invoke-virtual {v0}, Lmiuix/autodensity/AutoDensityContextWrapper;->getOriginConfiguration()Landroid/content/res/Configuration;

    move-result-object v0

    goto :goto_6

    nop

    :goto_2
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;

    move-result-object p0

    goto :goto_4

    nop

    :goto_3
    return-void

    :goto_4
    invoke-static {p0, p1}, Lmiuix/autodensity/AutoDensityConfig;->updateDensityOverrideConfiguration(Landroid/content/Context;Landroid/content/res/Configuration;)Landroid/content/res/Configuration;

    :goto_5
    goto :goto_3

    nop

    :goto_6
    invoke-virtual {v0, p1}, Landroid/content/res/Configuration;->setTo(Landroid/content/res/Configuration;)V

    goto :goto_b

    nop

    :goto_7
    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    goto :goto_9

    nop

    :goto_8
    if-nez v0, :cond_1

    goto :goto_5

    :cond_1
    goto :goto_1

    nop

    :goto_9
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;

    move-result-object v0

    goto :goto_a

    nop

    :goto_a
    invoke-static {v0}, Lmiuix/autodensity/DensityUtil;->findAutoDensityContextWrapper(Landroid/content/Context;)Lmiuix/autodensity/AutoDensityContextWrapper;

    move-result-object v0

    goto :goto_8

    nop

    :goto_b
    iget-boolean v0, p0, Lmiuix/appcompat/internal/widget/DialogRootView;->mNotifyConfigChanged:Z

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_widget_DialogRootView__onDetachedFromWindow',
        'method': '.method protected onDetachedFromWindow()V',
        'method_name': 'onDetachedFromWindow',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/FrameLayout;->onDetachedFromWindow()V', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;', 'iget-object v1, p0, Lmiuix/appcompat/internal/widget/DialogRootView;->mComponentCallbacks:Landroid/content/ComponentCallbacks;', 'invoke-virtual {v0, v1}, Landroid/content/Context;->unregisterComponentCallbacks(Landroid/content/ComponentCallbacks;)V', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;', 'invoke-static {p0}, Lmiuix/autodensity/DensityUtil;->findAutoDensityContextWrapper(Landroid/content/Context;)Lmiuix/autodensity/AutoDensityContextWrapper;', 'if-eqz p0, :cond_0', 'invoke-virtual {p0}, Lmiuix/autodensity/AutoDensityContextWrapper;->restoreOriginConfig()V'],
        'type': 'method_replace',
        'search': """.method protected onDetachedFromWindow()V
    .registers 3

    invoke-super {p0}, Landroid/widget/FrameLayout;->onDetachedFromWindow()V

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;

    move-result-object v0

    iget-object v1, p0, Lmiuix/appcompat/internal/widget/DialogRootView;->mComponentCallbacks:Landroid/content/ComponentCallbacks;

    invoke-virtual {v0, v1}, Landroid/content/Context;->unregisterComponentCallbacks(Landroid/content/ComponentCallbacks;)V

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;

    move-result-object p0

    invoke-static {p0}, Lmiuix/autodensity/DensityUtil;->findAutoDensityContextWrapper(Landroid/content/Context;)Lmiuix/autodensity/AutoDensityContextWrapper;

    move-result-object p0

    if-eqz p0, :cond_0

    invoke-virtual {p0}, Lmiuix/autodensity/AutoDensityContextWrapper;->restoreOriginConfig()V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onDetachedFromWindow()V
    .registers 3

    goto :goto_5

    nop

    :goto_0
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;

    move-result-object v0

    goto :goto_1

    nop

    :goto_1
    iget-object v1, p0, Lmiuix/appcompat/internal/widget/DialogRootView;->mComponentCallbacks:Landroid/content/ComponentCallbacks;

    goto :goto_2

    nop

    :goto_2
    invoke-virtual {v0, v1}, Landroid/content/Context;->unregisterComponentCallbacks(Landroid/content/ComponentCallbacks;)V

    goto :goto_9

    nop

    :goto_3
    invoke-virtual {p0}, Lmiuix/autodensity/AutoDensityContextWrapper;->restoreOriginConfig()V

    :goto_4
    goto :goto_8

    nop

    :goto_5
    invoke-super {p0}, Landroid/widget/FrameLayout;->onDetachedFromWindow()V

    goto :goto_0

    nop

    :goto_6
    if-nez p0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_3

    nop

    :goto_7
    invoke-static {p0}, Lmiuix/autodensity/DensityUtil;->findAutoDensityContextWrapper(Landroid/content/Context;)Lmiuix/autodensity/AutoDensityContextWrapper;

    move-result-object p0

    goto :goto_6

    nop

    :goto_8
    return-void

    :goto_9
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;

    move-result-object p0

    goto :goto_7

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_widget_DialogRootView__onLayout',
        'method': '.method protected onLayout(ZIIII)V',
        'method_name': 'onLayout',
        'method_anchors': ['invoke-super/range {p0 .. p5}, Landroid/widget/FrameLayout;->onLayout(ZIIII)V', 'iget-boolean p1, p0, Lmiuix/appcompat/internal/widget/DialogRootView;->mNotifyConfigChanged:Z', 'if-eqz p1, :cond_2', 'iput-boolean p1, p0, Lmiuix/appcompat/internal/widget/DialogRootView;->mViewConfigChangedDispatched:Z', 'iput-boolean p1, p0, Lmiuix/appcompat/internal/widget/DialogRootView;->mNotifyConfigChanged:Z', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->getResources()Landroid/content/res/Resources;', 'invoke-virtual {p1}, Landroid/content/res/Resources;->getConfiguration()Landroid/content/res/Configuration;', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;'],
        'type': 'method_replace',
        'search': """.method protected onLayout(ZIIII)V
    .registers 15

    invoke-super/range {p0 .. p5}, Landroid/widget/FrameLayout;->onLayout(ZIIII)V

    iget-boolean p1, p0, Lmiuix/appcompat/internal/widget/DialogRootView;->mNotifyConfigChanged:Z

    if-eqz p1, :cond_2

    const/4 p1, 0x0

    iput-boolean p1, p0, Lmiuix/appcompat/internal/widget/DialogRootView;->mViewConfigChangedDispatched:Z

    iput-boolean p1, p0, Lmiuix/appcompat/internal/widget/DialogRootView;->mNotifyConfigChanged:Z

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getResources()Landroid/content/res/Resources;

    move-result-object p1

    invoke-virtual {p1}, Landroid/content/res/Resources;->getConfiguration()Landroid/content/res/Configuration;

    move-result-object p1

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-static {v0}, Lmiuix/autodensity/DensityUtil;->findAutoDensityContextWrapper(Landroid/content/Context;)Lmiuix/autodensity/AutoDensityContextWrapper;

    move-result-object v6

    if-eqz v6, :cond_0

    invoke-virtual {v6}, Lmiuix/autodensity/AutoDensityContextWrapper;->getOriginConfiguration()Landroid/content/res/Configuration;

    move-result-object v0

    invoke-virtual {v0, p1}, Landroid/content/res/Configuration;->setTo(Landroid/content/res/Configuration;)V

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-static {v0, p1}, Lmiuix/autodensity/AutoDensityConfig;->updateDensityOverrideConfiguration(Landroid/content/Context;Landroid/content/res/Configuration;)Landroid/content/res/Configuration;

    :cond_0
    iget v7, p1, Landroid/content/res/Configuration;->screenWidthDp:I

    iget p1, p1, Landroid/content/res/Configuration;->screenHeightDp:I

    iget-object v0, p0, Lmiuix/appcompat/internal/widget/DialogRootView;->mCallback:Lmiuix/appcompat/internal/widget/DialogRootView$ConfigurationChangedCallback;

    if-eqz v0, :cond_1

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getResources()Landroid/content/res/Resources;

    move-result-object v1

    invoke-virtual {v1}, Landroid/content/res/Resources;->getConfiguration()Landroid/content/res/Configuration;

    move-result-object v1

    move v2, p2

    move v3, p3

    move v4, p4

    move v5, p5

    invoke-interface/range {v0 .. v5}, Lmiuix/appcompat/internal/widget/DialogRootView$ConfigurationChangedCallback;->onConfigurationChanged(Landroid/content/res/Configuration;IIII)V

    :cond_1
    new-instance v0, Lmiuix/appcompat/internal/widget/DialogRootView$2;

    move-object v1, p0

    move v4, p1

    move v5, p2

    move v8, p5

    move-object v2, v6

    move v3, v7

    move v6, p3

    move v7, p4

    invoke-direct/range {v0 .. v8}, Lmiuix/appcompat/internal/widget/DialogRootView$2;-><init>(Lmiuix/appcompat/internal/widget/DialogRootView;Lmiuix/autodensity/AutoDensityContextWrapper;IIIIII)V

    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->post(Ljava/lang/Runnable;)Z

    :cond_2
    return-void
.end method""",
        'replacement': """.method protected onLayout(ZIIII)V
    .registers 15

    goto :goto_1f

    nop

    :goto_0
    new-instance v0, Lmiuix/appcompat/internal/widget/DialogRootView$2;

    goto :goto_9

    nop

    :goto_1
    iput-boolean p1, p0, Lmiuix/appcompat/internal/widget/DialogRootView;->mViewConfigChangedDispatched:Z

    goto :goto_26

    nop

    :goto_2
    iget-boolean p1, p0, Lmiuix/appcompat/internal/widget/DialogRootView;->mNotifyConfigChanged:Z

    goto :goto_27

    nop

    :goto_3
    move v5, p5

    goto :goto_16

    nop

    :goto_4
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;

    move-result-object v0

    goto :goto_c

    nop

    :goto_5
    move v2, p2

    goto :goto_24

    nop

    :goto_6
    iget p1, p1, Landroid/content/res/Configuration;->screenHeightDp:I

    goto :goto_19

    nop

    :goto_7
    move-object v2, v6

    goto :goto_e

    nop

    :goto_8
    move v8, p5

    goto :goto_7

    nop

    :goto_9
    move-object v1, p0

    goto :goto_18

    nop

    :goto_a
    invoke-virtual {v1}, Landroid/content/res/Resources;->getConfiguration()Landroid/content/res/Configuration;

    move-result-object v1

    goto :goto_5

    nop

    :goto_b
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getResources()Landroid/content/res/Resources;

    move-result-object v1

    goto :goto_a

    nop

    :goto_c
    invoke-static {v0, p1}, Lmiuix/autodensity/AutoDensityConfig;->updateDensityOverrideConfiguration(Landroid/content/Context;Landroid/content/res/Configuration;)Landroid/content/res/Configuration;

    :goto_d
    goto :goto_f

    nop

    :goto_e
    move v3, v7

    goto :goto_1b

    nop

    :goto_f
    iget v7, p1, Landroid/content/res/Configuration;->screenWidthDp:I

    goto :goto_6

    nop

    :goto_10
    if-nez v6, :cond_0

    goto :goto_d

    :cond_0
    goto :goto_13

    nop

    :goto_11
    move v4, p4

    goto :goto_3

    nop

    :goto_12
    move v7, p4

    goto :goto_25

    nop

    :goto_13
    invoke-virtual {v6}, Lmiuix/autodensity/AutoDensityContextWrapper;->getOriginConfiguration()Landroid/content/res/Configuration;

    move-result-object v0

    goto :goto_28

    nop

    :goto_14
    invoke-virtual {p1}, Landroid/content/res/Resources;->getConfiguration()Landroid/content/res/Configuration;

    move-result-object p1

    goto :goto_1c

    nop

    :goto_15
    move v5, p2

    goto :goto_8

    nop

    :goto_16
    invoke-interface/range {v0 .. v5}, Lmiuix/appcompat/internal/widget/DialogRootView$ConfigurationChangedCallback;->onConfigurationChanged(Landroid/content/res/Configuration;IIII)V

    :goto_17
    goto :goto_0

    nop

    :goto_18
    move v4, p1

    goto :goto_15

    nop

    :goto_19
    iget-object v0, p0, Lmiuix/appcompat/internal/widget/DialogRootView;->mCallback:Lmiuix/appcompat/internal/widget/DialogRootView$ConfigurationChangedCallback;

    goto :goto_23

    nop

    :goto_1a
    const/4 p1, 0x0

    goto :goto_1

    nop

    :goto_1b
    move v6, p3

    goto :goto_12

    nop

    :goto_1c
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;

    move-result-object v0

    goto :goto_1d

    nop

    :goto_1d
    invoke-static {v0}, Lmiuix/autodensity/DensityUtil;->findAutoDensityContextWrapper(Landroid/content/Context;)Lmiuix/autodensity/AutoDensityContextWrapper;

    move-result-object v6

    goto :goto_10

    nop

    :goto_1e
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getResources()Landroid/content/res/Resources;

    move-result-object p1

    goto :goto_14

    nop

    :goto_1f
    invoke-super/range {p0 .. p5}, Landroid/widget/FrameLayout;->onLayout(ZIIII)V

    goto :goto_2

    nop

    :goto_20
    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->post(Ljava/lang/Runnable;)Z

    :goto_21
    goto :goto_22

    nop

    :goto_22
    return-void

    :goto_23
    if-nez v0, :cond_1

    goto :goto_17

    :cond_1
    goto :goto_b

    nop

    :goto_24
    move v3, p3

    goto :goto_11

    nop

    :goto_25
    invoke-direct/range {v0 .. v8}, Lmiuix/appcompat/internal/widget/DialogRootView$2;-><init>(Lmiuix/appcompat/internal/widget/DialogRootView;Lmiuix/autodensity/AutoDensityContextWrapper;IIIIII)V

    goto :goto_20

    nop

    :goto_26
    iput-boolean p1, p0, Lmiuix/appcompat/internal/widget/DialogRootView;->mNotifyConfigChanged:Z

    goto :goto_1e

    nop

    :goto_27
    if-nez p1, :cond_2

    goto :goto_21

    :cond_2
    goto :goto_1a

    nop

    :goto_28
    invoke-virtual {v0, p1}, Landroid/content/res/Configuration;->setTo(Landroid/content/res/Configuration;)V

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
