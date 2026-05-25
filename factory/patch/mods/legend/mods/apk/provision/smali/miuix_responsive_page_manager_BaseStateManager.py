TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/responsive/page/manager/BaseStateManager.smali'
CLASS_FALLBACK_NAMES = ['BaseStateManager.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'miuix_responsive_page_manager_BaseStateManager__computeResponsiveState',
        'method': '.method protected computeResponsiveState()Lmiuix/responsive/map/ResponsiveState;',
        'method_name': 'computeResponsiveState',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/responsive/page/manager/BaseStateManager;->getContext()Landroid/content/Context;', 'invoke-virtual {p0}, Lmiuix/responsive/page/manager/BaseStateManager;->getContext()Landroid/content/Context;', 'invoke-static {p0}, Lmiuix/core/util/EnvStateManager;->getWindowInfo(Landroid/content/Context;)Lmiuix/core/util/WindowBaseInfo;', 'invoke-static {v0, p0}, Lmiuix/responsive/ResponsiveStateHelper;->computeResponsiveState(Landroid/content/Context;Lmiuix/core/util/WindowBaseInfo;)Lmiuix/responsive/map/ResponsiveState;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected computeResponsiveState()Lmiuix/responsive/map/ResponsiveState;
    .registers 2

    invoke-virtual {p0}, Lmiuix/responsive/page/manager/BaseStateManager;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-virtual {p0}, Lmiuix/responsive/page/manager/BaseStateManager;->getContext()Landroid/content/Context;

    move-result-object p0

    invoke-static {p0}, Lmiuix/core/util/EnvStateManager;->getWindowInfo(Landroid/content/Context;)Lmiuix/core/util/WindowBaseInfo;

    move-result-object p0

    invoke-static {v0, p0}, Lmiuix/responsive/ResponsiveStateHelper;->computeResponsiveState(Landroid/content/Context;Lmiuix/core/util/WindowBaseInfo;)Lmiuix/responsive/map/ResponsiveState;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected computeResponsiveState()Lmiuix/responsive/map/ResponsiveState;
    .registers 2

    goto :goto_3

    nop

    :goto_0
    invoke-virtual {p0}, Lmiuix/responsive/page/manager/BaseStateManager;->getContext()Landroid/content/Context;

    move-result-object p0

    goto :goto_1

    nop

    :goto_1
    invoke-static {p0}, Lmiuix/core/util/EnvStateManager;->getWindowInfo(Landroid/content/Context;)Lmiuix/core/util/WindowBaseInfo;

    move-result-object p0

    goto :goto_4

    nop

    :goto_2
    return-object p0

    :goto_3
    invoke-virtual {p0}, Lmiuix/responsive/page/manager/BaseStateManager;->getContext()Landroid/content/Context;

    move-result-object v0

    goto :goto_0

    nop

    :goto_4
    invoke-static {v0, p0}, Lmiuix/responsive/ResponsiveStateHelper;->computeResponsiveState(Landroid/content/Context;Lmiuix/core/util/WindowBaseInfo;)Lmiuix/responsive/map/ResponsiveState;

    move-result-object p0

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_responsive_page_manager_BaseStateManager__computeResponsiveStateFromConfig',
        'method': '.method protected computeResponsiveStateFromConfig(Landroid/content/res/Configuration;)Lmiuix/responsive/map/ResponsiveState;',
        'method_name': 'computeResponsiveStateFromConfig',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/responsive/page/manager/BaseStateManager;->getContext()Landroid/content/Context;', 'invoke-virtual {p0}, Lmiuix/responsive/page/manager/BaseStateManager;->getContext()Landroid/content/Context;', 'invoke-static {p0}, Lmiuix/core/util/EnvStateManager;->getWindowInfo(Landroid/content/Context;)Lmiuix/core/util/WindowBaseInfo;', 'invoke-static {v0, p0, p1}, Lmiuix/responsive/ResponsiveStateHelper;->computeResponsiveStateOnConfigChanged(Landroid/content/Context;Lmiuix/core/util/WindowBaseInfo;Landroid/content/res/Configuration;)Lmiuix/responsive/map/ResponsiveState;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected computeResponsiveStateFromConfig(Landroid/content/res/Configuration;)Lmiuix/responsive/map/ResponsiveState;
    .registers 3

    invoke-virtual {p0}, Lmiuix/responsive/page/manager/BaseStateManager;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-virtual {p0}, Lmiuix/responsive/page/manager/BaseStateManager;->getContext()Landroid/content/Context;

    move-result-object p0

    invoke-static {p0}, Lmiuix/core/util/EnvStateManager;->getWindowInfo(Landroid/content/Context;)Lmiuix/core/util/WindowBaseInfo;

    move-result-object p0

    invoke-static {v0, p0, p1}, Lmiuix/responsive/ResponsiveStateHelper;->computeResponsiveStateOnConfigChanged(Landroid/content/Context;Lmiuix/core/util/WindowBaseInfo;Landroid/content/res/Configuration;)Lmiuix/responsive/map/ResponsiveState;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected computeResponsiveStateFromConfig(Landroid/content/res/Configuration;)Lmiuix/responsive/map/ResponsiveState;
    .registers 3

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    invoke-virtual {p0}, Lmiuix/responsive/page/manager/BaseStateManager;->getContext()Landroid/content/Context;

    move-result-object v0

    goto :goto_3

    nop

    :goto_2
    invoke-static {p0}, Lmiuix/core/util/EnvStateManager;->getWindowInfo(Landroid/content/Context;)Lmiuix/core/util/WindowBaseInfo;

    move-result-object p0

    goto :goto_4

    nop

    :goto_3
    invoke-virtual {p0}, Lmiuix/responsive/page/manager/BaseStateManager;->getContext()Landroid/content/Context;

    move-result-object p0

    goto :goto_2

    nop

    :goto_4
    invoke-static {v0, p0, p1}, Lmiuix/responsive/ResponsiveStateHelper;->computeResponsiveStateOnConfigChanged(Landroid/content/Context;Lmiuix/core/util/WindowBaseInfo;Landroid/content/res/Configuration;)Lmiuix/responsive/map/ResponsiveState;

    move-result-object p0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_responsive_page_manager_BaseStateManager__isStateEquals',
        'method': '.method protected isStateEquals(Lmiuix/responsive/map/ResponsiveState;Lmiuix/responsive/map/ResponsiveState;)Z',
        'method_name': 'isStateEquals',
        'method_anchors': ['invoke-static {p1, p2}, Ljava/util/Objects;->equals(Ljava/lang/Object;Ljava/lang/Object;)Z', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected isStateEquals(Lmiuix/responsive/map/ResponsiveState;Lmiuix/responsive/map/ResponsiveState;)Z
    .registers 3

    invoke-static {p1, p2}, Ljava/util/Objects;->equals(Ljava/lang/Object;Ljava/lang/Object;)Z

    move-result p0

    return p0
.end method""",
        'replacement': """.method protected isStateEquals(Lmiuix/responsive/map/ResponsiveState;Lmiuix/responsive/map/ResponsiveState;)Z
    .registers 3

    goto :goto_0

    nop

    :goto_0
    invoke-static {p1, p2}, Ljava/util/Objects;->equals(Ljava/lang/Object;Ljava/lang/Object;)Z

    move-result p0

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
        'id': 'miuix_responsive_page_manager_BaseStateManager__onAfterConfigurationChanged',
        'method': '.method protected onAfterConfigurationChanged(Landroid/content/res/Configuration;)V',
        'method_name': 'onAfterConfigurationChanged',
        'method_anchors': ['return-void'],
        'type': 'method_replace',
        'search': """.method protected onAfterConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 2

    return-void
.end method""",
        'replacement': """.method protected onAfterConfigurationChanged(Landroid/content/res/Configuration;)V
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
        'id': 'miuix_responsive_page_manager_BaseStateManager__onBeforeConfigurationChanged',
        'method': '.method protected onBeforeConfigurationChanged(Landroid/content/res/Configuration;)V',
        'method_name': 'onBeforeConfigurationChanged',
        'method_anchors': ['return-void'],
        'type': 'method_replace',
        'search': """.method protected onBeforeConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 2

    return-void
.end method""",
        'replacement': """.method protected onBeforeConfigurationChanged(Landroid/content/res/Configuration;)V
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
