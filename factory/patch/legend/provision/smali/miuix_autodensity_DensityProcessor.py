TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/autodensity/DensityProcessor.smali'
CLASS_FALLBACK_NAMES = ['DensityProcessor.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'miuix_autodensity_DensityProcessor__onDensityChangedBeforeActivityConfigChanged',
        'method': '.method protected onDensityChangedBeforeActivityConfigChanged(Landroid/app/Activity;Landroid/content/res/Configuration;Lmiuix/core/util/WindowBaseInfo;)V',
        'method_name': 'onDensityChangedBeforeActivityConfigChanged',
        'method_anchors': ['invoke-static {p2, p3}, Lmiuix/core/util/EnvStateManager;->updateWindowSizeByConfig(Landroid/content/res/Configuration;Lmiuix/core/util/WindowBaseInfo;)V', 'invoke-static {p1, p3}, Lmiuix/core/util/EnvStateManager;->updateWindowMode(Landroid/content/Context;Lmiuix/core/util/WindowBaseInfo;)V', 'invoke-static {p1}, Lmiuix/core/util/EnvStateManager;->markEnvStateDirty(Landroid/content/Context;)V', 'invoke-static {p3}, Lmiuix/core/util/EnvStateManager;->markWindowInfoDirty(Lmiuix/core/util/WindowBaseInfo;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onDensityChangedBeforeActivityConfigChanged(Landroid/app/Activity;Landroid/content/res/Configuration;Lmiuix/core/util/WindowBaseInfo;)V
    .registers 4

    invoke-static {p2, p3}, Lmiuix/core/util/EnvStateManager;->updateWindowSizeByConfig(Landroid/content/res/Configuration;Lmiuix/core/util/WindowBaseInfo;)V

    invoke-static {p1, p3}, Lmiuix/core/util/EnvStateManager;->updateWindowMode(Landroid/content/Context;Lmiuix/core/util/WindowBaseInfo;)V

    invoke-static {p1}, Lmiuix/core/util/EnvStateManager;->markEnvStateDirty(Landroid/content/Context;)V

    invoke-static {p3}, Lmiuix/core/util/EnvStateManager;->markWindowInfoDirty(Lmiuix/core/util/WindowBaseInfo;)V

    return-void
.end method""",
        'replacement': """.method protected onDensityChangedBeforeActivityConfigChanged(Landroid/app/Activity;Landroid/content/res/Configuration;Lmiuix/core/util/WindowBaseInfo;)V
    .registers 4

    goto :goto_4

    nop

    :goto_0
    invoke-static {p1, p3}, Lmiuix/core/util/EnvStateManager;->updateWindowMode(Landroid/content/Context;Lmiuix/core/util/WindowBaseInfo;)V

    goto :goto_3

    nop

    :goto_1
    return-void

    :goto_2
    invoke-static {p3}, Lmiuix/core/util/EnvStateManager;->markWindowInfoDirty(Lmiuix/core/util/WindowBaseInfo;)V

    goto :goto_1

    nop

    :goto_3
    invoke-static {p1}, Lmiuix/core/util/EnvStateManager;->markEnvStateDirty(Landroid/content/Context;)V

    goto :goto_2

    nop

    :goto_4
    invoke-static {p2, p3}, Lmiuix/core/util/EnvStateManager;->updateWindowSizeByConfig(Landroid/content/res/Configuration;Lmiuix/core/util/WindowBaseInfo;)V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_autodensity_DensityProcessor__onDensityChangedOnActivityCreated',
        'method': '.method protected onDensityChangedOnActivityCreated(Landroid/app/Activity;)V',
        'method_name': 'onDensityChangedOnActivityCreated',
        'method_anchors': ['invoke-virtual {p0, p1}, Lmiuix/autodensity/DensityProcessor;->registerCallback(Landroid/app/Activity;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onDensityChangedOnActivityCreated(Landroid/app/Activity;)V
    .registers 2

    invoke-virtual {p0, p1}, Lmiuix/autodensity/DensityProcessor;->registerCallback(Landroid/app/Activity;)V

    return-void
.end method""",
        'replacement': """.method protected onDensityChangedOnActivityCreated(Landroid/app/Activity;)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    invoke-virtual {p0, p1}, Lmiuix/autodensity/DensityProcessor;->registerCallback(Landroid/app/Activity;)V

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
        'id': 'miuix_autodensity_DensityProcessor__onDensityChangedOnActivityDisplayChanged',
        'method': '.method protected onDensityChangedOnActivityDisplayChanged(ILandroid/app/Activity;)V',
        'method_name': 'onDensityChangedOnActivityDisplayChanged',
        'method_anchors': ['return-void'],
        'type': 'method_replace',
        'search': """.method protected onDensityChangedOnActivityDisplayChanged(ILandroid/app/Activity;)V
    .registers 3

    return-void
.end method""",
        'replacement': """.method protected onDensityChangedOnActivityDisplayChanged(ILandroid/app/Activity;)V
    .registers 3

    goto :goto_0

    nop

    :goto_0
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_autodensity_DensityProcessor__onDensityChangedOnAppConfigChanged',
        'method': '.method protected onDensityChangedOnAppConfigChanged(Landroid/app/Application;)V',
        'method_name': 'onDensityChangedOnAppConfigChanged',
        'method_anchors': ['return-void'],
        'type': 'method_replace',
        'search': """.method protected onDensityChangedOnAppConfigChanged(Landroid/app/Application;)V
    .registers 2

    return-void
.end method""",
        'replacement': """.method protected onDensityChangedOnAppConfigChanged(Landroid/app/Application;)V
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
    {
        'id': 'miuix_autodensity_DensityProcessor__registerCallback',
        'method': '.method protected registerCallback(Landroid/app/Activity;)V',
        'method_name': 'registerCallback',
        'method_anchors': ['iget-object v0, p0, Lmiuix/autodensity/DensityProcessor;->mDisplayManager:Landroid/hardware/display/DisplayManager;', 'if-nez v0, :cond_0', 'invoke-virtual {p1}, Landroid/app/Activity;->getApplication()Landroid/app/Application;', 'const-string v1, "display"', 'invoke-virtual {v0, v1}, Landroid/app/Application;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;', 'check-cast v0, Landroid/hardware/display/DisplayManager;', 'iput-object v0, p0, Lmiuix/autodensity/DensityProcessor;->mDisplayManager:Landroid/hardware/display/DisplayManager;', 'iget-object v0, p0, Lmiuix/autodensity/DensityProcessor;->mModifier:Ljava/util/HashMap;'],
        'type': 'method_replace',
        'search': """.method protected registerCallback(Landroid/app/Activity;)V
    .registers 5

    iget-object v0, p0, Lmiuix/autodensity/DensityProcessor;->mDisplayManager:Landroid/hardware/display/DisplayManager;

    if-nez v0, :cond_0

    invoke-virtual {p1}, Landroid/app/Activity;->getApplication()Landroid/app/Application;

    move-result-object v0

    const-string v1, "display"

    invoke-virtual {v0, v1}, Landroid/app/Application;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/hardware/display/DisplayManager;

    iput-object v0, p0, Lmiuix/autodensity/DensityProcessor;->mDisplayManager:Landroid/hardware/display/DisplayManager;

    :cond_0
    iget-object v0, p0, Lmiuix/autodensity/DensityProcessor;->mModifier:Ljava/util/HashMap;

    if-nez v0, :cond_1

    new-instance v0, Ljava/util/HashMap;

    invoke-direct {v0}, Ljava/util/HashMap;-><init>()V

    iput-object v0, p0, Lmiuix/autodensity/DensityProcessor;->mModifier:Ljava/util/HashMap;

    :cond_1
    invoke-virtual {p1}, Ljava/lang/Object;->hashCode()I

    move-result v0

    iget-object v1, p0, Lmiuix/autodensity/DensityProcessor;->mModifier:Ljava/util/HashMap;

    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v2

    invoke-virtual {v1, v2}, Ljava/util/HashMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lmiuix/autodensity/DensityProcessor$DensityCallback;

    if-nez v1, :cond_2

    new-instance v1, Lmiuix/autodensity/DensityProcessor$DensityCallback;

    invoke-direct {v1, p0, p1, p0}, Lmiuix/autodensity/DensityProcessor$DensityCallback;-><init>(Lmiuix/autodensity/DensityProcessor;Landroid/app/Activity;Lmiuix/autodensity/DensityProcessor;)V

    iget-object v2, p0, Lmiuix/autodensity/DensityProcessor;->mModifier:Ljava/util/HashMap;

    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    invoke-virtual {v2, v0, v1}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    iget-object v0, p0, Lmiuix/autodensity/DensityProcessor;->mDisplayManager:Landroid/hardware/display/DisplayManager;

    iget-object p0, p0, Lmiuix/autodensity/DensityProcessor;->mUiHandler:Landroid/os/Handler;

    invoke-virtual {v0, v1, p0}, Landroid/hardware/display/DisplayManager;->registerDisplayListener(Landroid/hardware/display/DisplayManager$DisplayListener;Landroid/os/Handler;)V

    invoke-virtual {p1}, Landroid/app/Activity;->getApplication()Landroid/app/Application;

    move-result-object p0

    invoke-virtual {p0, v1}, Landroid/app/Application;->registerComponentCallbacks(Landroid/content/ComponentCallbacks;)V

    invoke-virtual {p1, v1}, Landroid/app/Activity;->registerComponentCallbacks(Landroid/content/ComponentCallbacks;)V

    :cond_2
    return-void
.end method""",
        'replacement': """.method protected registerCallback(Landroid/app/Activity;)V
    .registers 5

    goto :goto_11

    nop

    :goto_0
    invoke-virtual {p0, v1}, Landroid/app/Application;->registerComponentCallbacks(Landroid/content/ComponentCallbacks;)V

    goto :goto_19

    nop

    :goto_1
    check-cast v0, Landroid/hardware/display/DisplayManager;

    goto :goto_17

    nop

    :goto_2
    iget-object p0, p0, Lmiuix/autodensity/DensityProcessor;->mUiHandler:Landroid/os/Handler;

    goto :goto_c

    nop

    :goto_3
    iget-object v0, p0, Lmiuix/autodensity/DensityProcessor;->mDisplayManager:Landroid/hardware/display/DisplayManager;

    goto :goto_2

    nop

    :goto_4
    invoke-virtual {v1, v2}, Ljava/util/HashMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v1

    goto :goto_f

    nop

    :goto_5
    iget-object v1, p0, Lmiuix/autodensity/DensityProcessor;->mModifier:Ljava/util/HashMap;

    goto :goto_1d

    nop

    :goto_6
    invoke-direct {v0}, Ljava/util/HashMap;-><init>()V

    goto :goto_1b

    nop

    :goto_7
    const-string v1, "display"

    goto :goto_10

    nop

    :goto_8
    iget-object v0, p0, Lmiuix/autodensity/DensityProcessor;->mModifier:Ljava/util/HashMap;

    goto :goto_b

    nop

    :goto_9
    iget-object v2, p0, Lmiuix/autodensity/DensityProcessor;->mModifier:Ljava/util/HashMap;

    goto :goto_15

    nop

    :goto_a
    if-eqz v1, :cond_0

    goto :goto_1a

    :cond_0
    goto :goto_12

    nop

    :goto_b
    if-eqz v0, :cond_1

    goto :goto_1c

    :cond_1
    goto :goto_1e

    nop

    :goto_c
    invoke-virtual {v0, v1, p0}, Landroid/hardware/display/DisplayManager;->registerDisplayListener(Landroid/hardware/display/DisplayManager$DisplayListener;Landroid/os/Handler;)V

    goto :goto_d

    nop

    :goto_d
    invoke-virtual {p1}, Landroid/app/Activity;->getApplication()Landroid/app/Application;

    move-result-object p0

    goto :goto_0

    nop

    :goto_e
    invoke-virtual {v2, v0, v1}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_3

    nop

    :goto_f
    check-cast v1, Lmiuix/autodensity/DensityProcessor$DensityCallback;

    goto :goto_a

    nop

    :goto_10
    invoke-virtual {v0, v1}, Landroid/app/Application;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object v0

    goto :goto_1

    nop

    :goto_11
    iget-object v0, p0, Lmiuix/autodensity/DensityProcessor;->mDisplayManager:Landroid/hardware/display/DisplayManager;

    goto :goto_20

    nop

    :goto_12
    new-instance v1, Lmiuix/autodensity/DensityProcessor$DensityCallback;

    goto :goto_13

    nop

    :goto_13
    invoke-direct {v1, p0, p1, p0}, Lmiuix/autodensity/DensityProcessor$DensityCallback;-><init>(Lmiuix/autodensity/DensityProcessor;Landroid/app/Activity;Lmiuix/autodensity/DensityProcessor;)V

    goto :goto_9

    nop

    :goto_14
    invoke-virtual {p1}, Ljava/lang/Object;->hashCode()I

    move-result v0

    goto :goto_5

    nop

    :goto_15
    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    goto :goto_e

    nop

    :goto_16
    invoke-virtual {p1}, Landroid/app/Activity;->getApplication()Landroid/app/Application;

    move-result-object v0

    goto :goto_7

    nop

    :goto_17
    iput-object v0, p0, Lmiuix/autodensity/DensityProcessor;->mDisplayManager:Landroid/hardware/display/DisplayManager;

    :goto_18
    goto :goto_8

    nop

    :goto_19
    invoke-virtual {p1, v1}, Landroid/app/Activity;->registerComponentCallbacks(Landroid/content/ComponentCallbacks;)V

    :goto_1a
    goto :goto_1f

    nop

    :goto_1b
    iput-object v0, p0, Lmiuix/autodensity/DensityProcessor;->mModifier:Ljava/util/HashMap;

    :goto_1c
    goto :goto_14

    nop

    :goto_1d
    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v2

    goto :goto_4

    nop

    :goto_1e
    new-instance v0, Ljava/util/HashMap;

    goto :goto_6

    nop

    :goto_1f
    return-void

    :goto_20
    if-eqz v0, :cond_2

    goto :goto_18

    :cond_2
    goto :goto_16

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_autodensity_DensityProcessor__unregisterCallback',
        'method': '.method protected unregisterCallback(Landroid/app/Activity;)V',
        'method_name': 'unregisterCallback',
        'method_anchors': ['iget-object v0, p0, Lmiuix/autodensity/DensityProcessor;->mModifier:Ljava/util/HashMap;', 'if-eqz v0, :cond_2', 'invoke-virtual {p1}, Ljava/lang/Object;->hashCode()I', 'iget-object v1, p0, Lmiuix/autodensity/DensityProcessor;->mModifier:Ljava/util/HashMap;', 'invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;', 'invoke-virtual {v1, v2}, Ljava/util/HashMap;->get(Ljava/lang/Object;)Ljava/lang/Object;', 'check-cast v1, Lmiuix/autodensity/DensityProcessor$DensityCallback;', 'invoke-static {}, Lmiuix/autodensity/DebugUtil;->isEnableDebug()Z'],
        'type': 'method_replace',
        'search': """.method protected unregisterCallback(Landroid/app/Activity;)V
    .registers 6

    iget-object v0, p0, Lmiuix/autodensity/DensityProcessor;->mModifier:Ljava/util/HashMap;

    if-eqz v0, :cond_2

    invoke-virtual {p1}, Ljava/lang/Object;->hashCode()I

    move-result v0

    iget-object v1, p0, Lmiuix/autodensity/DensityProcessor;->mModifier:Ljava/util/HashMap;

    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v2

    invoke-virtual {v1, v2}, Ljava/util/HashMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lmiuix/autodensity/DensityProcessor$DensityCallback;

    invoke-static {}, Lmiuix/autodensity/DebugUtil;->isEnableDebug()Z

    move-result v2

    if-eqz v2, :cond_0

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "unregisterCallback obj: "

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-static {v2}, Lmiuix/autodensity/DebugUtil;->printDensityLog(Ljava/lang/String;)V

    :cond_0
    if-eqz v1, :cond_1

    invoke-virtual {p0, v1}, Lmiuix/autodensity/DensityProcessor;->unregisterDisplayListener(Lmiuix/autodensity/DensityProcessor$DensityCallback;)V

    invoke-virtual {p1}, Landroid/app/Activity;->getApplication()Landroid/app/Application;

    move-result-object v2

    invoke-virtual {v2, v1}, Landroid/app/Application;->unregisterComponentCallbacks(Landroid/content/ComponentCallbacks;)V

    invoke-virtual {p1, v1}, Landroid/app/Activity;->unregisterComponentCallbacks(Landroid/content/ComponentCallbacks;)V

    invoke-virtual {v1, p1}, Lmiuix/autodensity/DensityProcessor$DensityCallback;->removeOnAttachStateChangeListener(Landroid/app/Activity;)V

    invoke-virtual {v1}, Lmiuix/autodensity/DensityProcessor$DensityCallback;->clear()V

    :cond_1
    iget-object p0, p0, Lmiuix/autodensity/DensityProcessor;->mModifier:Ljava/util/HashMap;

    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p1

    invoke-virtual {p0, p1}, Ljava/util/HashMap;->remove(Ljava/lang/Object;)Ljava/lang/Object;

    :cond_2
    return-void
.end method""",
        'replacement': """.method protected unregisterCallback(Landroid/app/Activity;)V
    .registers 6

    goto :goto_7

    nop

    :goto_0
    invoke-virtual {p0, p1}, Ljava/util/HashMap;->remove(Ljava/lang/Object;)Ljava/lang/Object;

    :goto_1
    goto :goto_e

    nop

    :goto_2
    invoke-static {}, Lmiuix/autodensity/DebugUtil;->isEnableDebug()Z

    move-result v2

    goto :goto_4

    nop

    :goto_3
    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v2

    goto :goto_12

    nop

    :goto_4
    if-nez v2, :cond_0

    goto :goto_10

    :cond_0
    goto :goto_17

    nop

    :goto_5
    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_13

    nop

    :goto_6
    invoke-virtual {p1, v1}, Landroid/app/Activity;->unregisterComponentCallbacks(Landroid/content/ComponentCallbacks;)V

    goto :goto_9

    nop

    :goto_7
    iget-object v0, p0, Lmiuix/autodensity/DensityProcessor;->mModifier:Ljava/util/HashMap;

    goto :goto_1a

    nop

    :goto_8
    invoke-virtual {p0, v1}, Lmiuix/autodensity/DensityProcessor;->unregisterDisplayListener(Lmiuix/autodensity/DensityProcessor$DensityCallback;)V

    goto :goto_19

    nop

    :goto_9
    invoke-virtual {v1, p1}, Lmiuix/autodensity/DensityProcessor$DensityCallback;->removeOnAttachStateChangeListener(Landroid/app/Activity;)V

    goto :goto_1c

    nop

    :goto_a
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_15

    nop

    :goto_b
    invoke-virtual {p1}, Ljava/lang/Object;->hashCode()I

    move-result v0

    goto :goto_16

    nop

    :goto_c
    if-nez v1, :cond_1

    goto :goto_1d

    :cond_1
    goto :goto_8

    nop

    :goto_d
    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    goto :goto_f

    nop

    :goto_e
    return-void

    :goto_f
    invoke-static {v2}, Lmiuix/autodensity/DebugUtil;->printDensityLog(Ljava/lang/String;)V

    :goto_10
    goto :goto_c

    nop

    :goto_11
    check-cast v1, Lmiuix/autodensity/DensityProcessor$DensityCallback;

    goto :goto_2

    nop

    :goto_12
    invoke-virtual {v1, v2}, Ljava/util/HashMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v1

    goto :goto_11

    nop

    :goto_13
    const-string v3, "unregisterCallback obj: "

    goto :goto_a

    nop

    :goto_14
    iget-object p0, p0, Lmiuix/autodensity/DensityProcessor;->mModifier:Ljava/util/HashMap;

    goto :goto_18

    nop

    :goto_15
    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_d

    nop

    :goto_16
    iget-object v1, p0, Lmiuix/autodensity/DensityProcessor;->mModifier:Ljava/util/HashMap;

    goto :goto_3

    nop

    :goto_17
    new-instance v2, Ljava/lang/StringBuilder;

    goto :goto_5

    nop

    :goto_18
    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p1

    goto :goto_0

    nop

    :goto_19
    invoke-virtual {p1}, Landroid/app/Activity;->getApplication()Landroid/app/Application;

    move-result-object v2

    goto :goto_1b

    nop

    :goto_1a
    if-nez v0, :cond_2

    goto :goto_1

    :cond_2
    goto :goto_b

    nop

    :goto_1b
    invoke-virtual {v2, v1}, Landroid/app/Application;->unregisterComponentCallbacks(Landroid/content/ComponentCallbacks;)V

    goto :goto_6

    nop

    :goto_1c
    invoke-virtual {v1}, Lmiuix/autodensity/DensityProcessor$DensityCallback;->clear()V

    :goto_1d
    goto :goto_14

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_autodensity_DensityProcessor__unregisterDisplayListener',
        'method': '.method protected unregisterDisplayListener(Lmiuix/autodensity/DensityProcessor$DensityCallback;)V',
        'method_name': 'unregisterDisplayListener',
        'method_anchors': ['iget-object p0, p0, Lmiuix/autodensity/DensityProcessor;->mDisplayManager:Landroid/hardware/display/DisplayManager;', 'if-eqz p0, :cond_0', 'invoke-virtual {p0, p1}, Landroid/hardware/display/DisplayManager;->unregisterDisplayListener(Landroid/hardware/display/DisplayManager$DisplayListener;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected unregisterDisplayListener(Lmiuix/autodensity/DensityProcessor$DensityCallback;)V
    .registers 2

    iget-object p0, p0, Lmiuix/autodensity/DensityProcessor;->mDisplayManager:Landroid/hardware/display/DisplayManager;

    if-eqz p0, :cond_0

    invoke-virtual {p0, p1}, Landroid/hardware/display/DisplayManager;->unregisterDisplayListener(Landroid/hardware/display/DisplayManager$DisplayListener;)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected unregisterDisplayListener(Lmiuix/autodensity/DensityProcessor$DensityCallback;)V
    .registers 2

    goto :goto_4

    nop

    :goto_0
    return-void

    :goto_1
    if-nez p0, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_2

    nop

    :goto_2
    invoke-virtual {p0, p1}, Landroid/hardware/display/DisplayManager;->unregisterDisplayListener(Landroid/hardware/display/DisplayManager$DisplayListener;)V

    :goto_3
    goto :goto_0

    nop

    :goto_4
    iget-object p0, p0, Lmiuix/autodensity/DensityProcessor;->mDisplayManager:Landroid/hardware/display/DisplayManager;

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
