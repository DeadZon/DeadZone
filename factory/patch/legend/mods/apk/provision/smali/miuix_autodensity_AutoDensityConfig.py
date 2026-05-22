TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/autodensity/AutoDensityConfig.smali'
CLASS_FALLBACK_NAMES = ['AutoDensityConfig.smali']
CLASS_ANCHORS = ['.super Lmiuix/autodensity/DensityProcessor;', '.field private static final TAG_CONFIG_CHANGE_FRAGMENT:Ljava/lang/String; = "ConfigurationChangeFragment"']

PATCHES = [
    {
        'id': 'miuix_autodensity_AutoDensityConfig__onDensityChangedOnActivityCreated',
        'method': '.method protected onDensityChangedOnActivityCreated(Landroid/app/Activity;)V',
        'method_name': 'onDensityChangedOnActivityCreated',
        'method_anchors': ['invoke-super {p0, p1}, Lmiuix/autodensity/DensityProcessor;->onDensityChangedOnActivityCreated(Landroid/app/Activity;)V', 'invoke-direct {p0, p1}, Lmiuix/autodensity/AutoDensityConfig;->addForOnConfigurationChange(Landroid/app/Activity;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onDensityChangedOnActivityCreated(Landroid/app/Activity;)V
    .registers 2

    invoke-super {p0, p1}, Lmiuix/autodensity/DensityProcessor;->onDensityChangedOnActivityCreated(Landroid/app/Activity;)V

    invoke-direct {p0, p1}, Lmiuix/autodensity/AutoDensityConfig;->addForOnConfigurationChange(Landroid/app/Activity;)V

    return-void
.end method""",
        'replacement': """.method protected onDensityChangedOnActivityCreated(Landroid/app/Activity;)V
    .registers 2

    goto :goto_2

    nop

    :goto_0
    invoke-direct {p0, p1}, Lmiuix/autodensity/AutoDensityConfig;->addForOnConfigurationChange(Landroid/app/Activity;)V

    goto :goto_1

    nop

    :goto_1
    return-void

    :goto_2
    invoke-super {p0, p1}, Lmiuix/autodensity/DensityProcessor;->onDensityChangedOnActivityCreated(Landroid/app/Activity;)V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_autodensity_AutoDensityConfig__onRegisterDensityCallback',
        'method': '.method protected onRegisterDensityCallback(Ljava/lang/Object;)V',
        'method_name': 'onRegisterDensityCallback',
        'method_anchors': ['invoke-static {}, Lmiuix/autodensity/DebugUtil;->isEnableDebug()Z', 'if-eqz p0, :cond_0', 'new-instance p0, Ljava/lang/StringBuilder;', 'invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V', 'const-string v0, "registerCallback obj: "', 'invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;', 'invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;'],
        'type': 'method_replace',
        'search': """.method protected onRegisterDensityCallback(Ljava/lang/Object;)V
    .registers 3

    invoke-static {}, Lmiuix/autodensity/DebugUtil;->isEnableDebug()Z

    move-result p0

    if-eqz p0, :cond_0

    new-instance p0, Ljava/lang/StringBuilder;

    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v0, "registerCallback obj: "

    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    invoke-static {p0}, Lmiuix/autodensity/DebugUtil;->printDensityLog(Ljava/lang/String;)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onRegisterDensityCallback(Ljava/lang/Object;)V
    .registers 3

    goto :goto_9

    nop

    :goto_0
    if-nez p0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_a

    nop

    :goto_1
    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    goto :goto_3

    nop

    :goto_2
    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_8

    nop

    :goto_3
    invoke-static {p0}, Lmiuix/autodensity/DebugUtil;->printDensityLog(Ljava/lang/String;)V

    :goto_4
    goto :goto_7

    nop

    :goto_5
    const-string v0, "registerCallback obj: "

    goto :goto_2

    nop

    :goto_6
    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_5

    nop

    :goto_7
    return-void

    :goto_8
    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_1

    nop

    :goto_9
    invoke-static {}, Lmiuix/autodensity/DebugUtil;->isEnableDebug()Z

    move-result p0

    goto :goto_0

    nop

    :goto_a
    new-instance p0, Ljava/lang/StringBuilder;

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_autodensity_AutoDensityConfig__processBeforeActivityConfigChanged',
        'method': '.method protected processBeforeActivityConfigChanged(Landroid/app/Activity;Landroid/content/res/Configuration;)V',
        'method_name': 'processBeforeActivityConfigChanged',
        'method_anchors': ['invoke-static {}, Lmiuix/autodensity/DebugUtil;->isEnableDebug()Z', 'if-eqz v0, :cond_0', 'const-string v0, "->processBeforeActivityConfigChanged"', 'invoke-static {v0}, Lmiuix/autodensity/DebugUtil;->printDensityLog(Ljava/lang/String;)V', 'invoke-virtual {p1}, Landroid/app/Activity;->getApplication()Landroid/app/Application;', 'invoke-static {v0}, Lmiuix/autodensity/AutoDensityConfig;->isShouldAdaptAutoDensity(Landroid/app/Application;)Z', 'if-eqz v1, :cond_1', 'check-cast v1, Lmiuix/autodensity/IDensity;'],
        'type': 'method_replace',
        'search': """.method protected processBeforeActivityConfigChanged(Landroid/app/Activity;Landroid/content/res/Configuration;)V
    .registers 5

    invoke-static {}, Lmiuix/autodensity/DebugUtil;->isEnableDebug()Z

    move-result v0

    if-eqz v0, :cond_0

    const-string v0, "->processBeforeActivityConfigChanged"

    invoke-static {v0}, Lmiuix/autodensity/DebugUtil;->printDensityLog(Ljava/lang/String;)V

    :cond_0
    invoke-virtual {p1}, Landroid/app/Activity;->getApplication()Landroid/app/Application;

    move-result-object v0

    invoke-static {v0}, Lmiuix/autodensity/AutoDensityConfig;->isShouldAdaptAutoDensity(Landroid/app/Application;)Z

    move-result v0

    instance-of v1, p1, Lmiuix/autodensity/IDensity;

    if-eqz v1, :cond_1

    move-object v1, p1

    check-cast v1, Lmiuix/autodensity/IDensity;

    invoke-interface {v1}, Lmiuix/autodensity/IDensity;->shouldAdaptAutoDensity()Z

    move-result v1

    goto :goto_0

    :cond_1
    move v1, v0

    :goto_0
    if-eqz v1, :cond_3

    invoke-static {p1}, Lmiuix/autodensity/DensityUtil;->updateCustomDensity(Landroid/content/Context;)V

    invoke-static {p1}, Lmiuix/core/util/EnvStateManager;->getWindowInfo(Landroid/content/Context;)Lmiuix/core/util/WindowBaseInfo;

    move-result-object v0

    invoke-virtual {p0, p1, p2, v0}, Lmiuix/autodensity/DensityProcessor;->onDensityChangedBeforeActivityConfigChanged(Landroid/app/Activity;Landroid/content/res/Configuration;Lmiuix/core/util/WindowBaseInfo;)V

    iget p2, v0, Lmiuix/core/util/WindowBaseInfo;->windowMode:I

    invoke-static {p2}, Lmiuix/core/util/ScreenModeHelper;->isInSplitScreenMode(I)Z

    move-result p2

    if-nez p2, :cond_2

    iget p2, v0, Lmiuix/core/util/WindowBaseInfo;->windowMode:I

    invoke-static {p2}, Lmiuix/core/util/ScreenModeHelper;->isInFreeFormMode(I)Z

    :cond_2
    invoke-direct {p0, p1}, Lmiuix/autodensity/AutoDensityConfig;->changeCurrentConfig(Landroid/app/Activity;)V

    return-void

    :cond_3
    if-eqz v0, :cond_5

    invoke-static {p1}, Lmiuix/autodensity/DensityUtil;->restoreDefaultDensity(Landroid/content/Context;)Z

    move-result v0

    invoke-static {p1}, Lmiuix/core/util/EnvStateManager;->getWindowInfo(Landroid/content/Context;)Lmiuix/core/util/WindowBaseInfo;

    move-result-object v1

    invoke-virtual {p0, p1, p2, v1}, Lmiuix/autodensity/DensityProcessor;->onDensityChangedBeforeActivityConfigChanged(Landroid/app/Activity;Landroid/content/res/Configuration;Lmiuix/core/util/WindowBaseInfo;)V

    if-eqz v0, :cond_5

    iget p2, v1, Lmiuix/core/util/WindowBaseInfo;->windowMode:I

    invoke-static {p2}, Lmiuix/core/util/ScreenModeHelper;->isInSplitScreenMode(I)Z

    move-result p2

    if-nez p2, :cond_4

    iget p2, v1, Lmiuix/core/util/WindowBaseInfo;->windowMode:I

    invoke-static {p2}, Lmiuix/core/util/ScreenModeHelper;->isInFreeFormMode(I)Z

    :cond_4
    invoke-direct {p0, p1}, Lmiuix/autodensity/AutoDensityConfig;->changeCurrentConfig(Landroid/app/Activity;)V

    :cond_5
    return-void
.end method""",
        'replacement': """.method protected processBeforeActivityConfigChanged(Landroid/app/Activity;Landroid/content/res/Configuration;)V
    .registers 5

    goto :goto_0

    nop

    :goto_0
    invoke-static {}, Lmiuix/autodensity/DebugUtil;->isEnableDebug()Z

    move-result v0

    goto :goto_13

    nop

    :goto_1
    iget p2, v1, Lmiuix/core/util/WindowBaseInfo;->windowMode:I

    goto :goto_20

    nop

    :goto_2
    return-void

    :goto_3
    goto :goto_16

    nop

    :goto_4
    invoke-direct {p0, p1}, Lmiuix/autodensity/AutoDensityConfig;->changeCurrentConfig(Landroid/app/Activity;)V

    :goto_5
    goto :goto_7

    nop

    :goto_6
    if-eqz p2, :cond_0

    goto :goto_2a

    :cond_0
    goto :goto_b

    nop

    :goto_7
    return-void

    :goto_8
    goto :goto_1a

    :goto_9
    goto :goto_19

    nop

    :goto_a
    invoke-static {p1}, Lmiuix/core/util/EnvStateManager;->getWindowInfo(Landroid/content/Context;)Lmiuix/core/util/WindowBaseInfo;

    move-result-object v1

    goto :goto_26

    nop

    :goto_b
    iget p2, v0, Lmiuix/core/util/WindowBaseInfo;->windowMode:I

    goto :goto_29

    nop

    :goto_c
    invoke-interface {v1}, Lmiuix/autodensity/IDensity;->shouldAdaptAutoDensity()Z

    move-result v1

    goto :goto_8

    nop

    :goto_d
    invoke-direct {p0, p1}, Lmiuix/autodensity/AutoDensityConfig;->changeCurrentConfig(Landroid/app/Activity;)V

    goto :goto_2

    nop

    :goto_e
    invoke-static {p1}, Lmiuix/autodensity/DensityUtil;->restoreDefaultDensity(Landroid/content/Context;)Z

    move-result v0

    goto :goto_a

    nop

    :goto_f
    check-cast v1, Lmiuix/autodensity/IDensity;

    goto :goto_c

    nop

    :goto_10
    invoke-virtual {p0, p1, p2, v0}, Lmiuix/autodensity/DensityProcessor;->onDensityChangedBeforeActivityConfigChanged(Landroid/app/Activity;Landroid/content/res/Configuration;Lmiuix/core/util/WindowBaseInfo;)V

    goto :goto_1e

    nop

    :goto_11
    invoke-static {v0}, Lmiuix/autodensity/DebugUtil;->printDensityLog(Ljava/lang/String;)V

    :goto_12
    goto :goto_23

    nop

    :goto_13
    if-nez v0, :cond_1

    goto :goto_12

    :cond_1
    goto :goto_17

    nop

    :goto_14
    invoke-static {v0}, Lmiuix/autodensity/AutoDensityConfig;->isShouldAdaptAutoDensity(Landroid/app/Application;)Z

    move-result v0

    goto :goto_18

    nop

    :goto_15
    invoke-static {p1}, Lmiuix/autodensity/DensityUtil;->updateCustomDensity(Landroid/content/Context;)V

    goto :goto_1f

    nop

    :goto_16
    if-nez v0, :cond_2

    goto :goto_5

    :cond_2
    goto :goto_e

    nop

    :goto_17
    const-string v0, "->processBeforeActivityConfigChanged"

    goto :goto_11

    nop

    :goto_18
    instance-of v1, p1, Lmiuix/autodensity/IDensity;

    goto :goto_28

    nop

    :goto_19
    move v1, v0

    :goto_1a
    goto :goto_22

    nop

    :goto_1b
    if-nez v0, :cond_3

    goto :goto_5

    :cond_3
    goto :goto_1d

    nop

    :goto_1c
    if-eqz p2, :cond_4

    goto :goto_21

    :cond_4
    goto :goto_1

    nop

    :goto_1d
    iget p2, v1, Lmiuix/core/util/WindowBaseInfo;->windowMode:I

    goto :goto_25

    nop

    :goto_1e
    iget p2, v0, Lmiuix/core/util/WindowBaseInfo;->windowMode:I

    goto :goto_27

    nop

    :goto_1f
    invoke-static {p1}, Lmiuix/core/util/EnvStateManager;->getWindowInfo(Landroid/content/Context;)Lmiuix/core/util/WindowBaseInfo;

    move-result-object v0

    goto :goto_10

    nop

    :goto_20
    invoke-static {p2}, Lmiuix/core/util/ScreenModeHelper;->isInFreeFormMode(I)Z

    :goto_21
    goto :goto_4

    nop

    :goto_22
    if-nez v1, :cond_5

    goto :goto_3

    :cond_5
    goto :goto_15

    nop

    :goto_23
    invoke-virtual {p1}, Landroid/app/Activity;->getApplication()Landroid/app/Application;

    move-result-object v0

    goto :goto_14

    nop

    :goto_24
    move-object v1, p1

    goto :goto_f

    nop

    :goto_25
    invoke-static {p2}, Lmiuix/core/util/ScreenModeHelper;->isInSplitScreenMode(I)Z

    move-result p2

    goto :goto_1c

    nop

    :goto_26
    invoke-virtual {p0, p1, p2, v1}, Lmiuix/autodensity/DensityProcessor;->onDensityChangedBeforeActivityConfigChanged(Landroid/app/Activity;Landroid/content/res/Configuration;Lmiuix/core/util/WindowBaseInfo;)V

    goto :goto_1b

    nop

    :goto_27
    invoke-static {p2}, Lmiuix/core/util/ScreenModeHelper;->isInSplitScreenMode(I)Z

    move-result p2

    goto :goto_6

    nop

    :goto_28
    if-nez v1, :cond_6

    goto :goto_9

    :cond_6
    goto :goto_24

    nop

    :goto_29
    invoke-static {p2}, Lmiuix/core/util/ScreenModeHelper;->isInFreeFormMode(I)Z

    :goto_2a
    goto :goto_d

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_autodensity_AutoDensityConfig__registerCallback',
        'method': '.method protected registerCallback(Landroid/app/Activity;)V',
        'method_name': 'registerCallback',
        'method_anchors': ['invoke-super {p0, p1}, Lmiuix/autodensity/DensityProcessor;->registerCallback(Landroid/app/Activity;)V', 'invoke-direct {p0, p1}, Lmiuix/autodensity/AutoDensityConfig;->tryToAddActivityConfigCallback(Landroid/app/Activity;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected registerCallback(Landroid/app/Activity;)V
    .registers 2

    invoke-super {p0, p1}, Lmiuix/autodensity/DensityProcessor;->registerCallback(Landroid/app/Activity;)V

    invoke-direct {p0, p1}, Lmiuix/autodensity/AutoDensityConfig;->tryToAddActivityConfigCallback(Landroid/app/Activity;)V

    return-void
.end method""",
        'replacement': """.method protected registerCallback(Landroid/app/Activity;)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0, p1}, Lmiuix/autodensity/DensityProcessor;->registerCallback(Landroid/app/Activity;)V

    goto :goto_2

    nop

    :goto_1
    return-void

    :goto_2
    invoke-direct {p0, p1}, Lmiuix/autodensity/AutoDensityConfig;->tryToAddActivityConfigCallback(Landroid/app/Activity;)V

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_autodensity_AutoDensityConfig__updateApplicationDensity',
        'method': '.method updateApplicationDensity(Landroid/app/Application;)V',
        'method_name': 'updateApplicationDensity',
        'method_anchors': ['return-void'],
        'type': 'method_replace',
        'search': """.method updateApplicationDensity(Landroid/app/Application;)V
    .registers 2

    return-void
.end method""",
        'replacement': """.method updateApplicationDensity(Landroid/app/Application;)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
