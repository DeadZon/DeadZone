TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/styles/ColorStateEffect.smali'
CLASS_FALLBACK_NAMES = ['ColorStateEffect.smali']
CLASS_ANCHORS = ['.super Lmiuix/animation/styles/DrawableStateEffect;', '.field private static final ACTIVATE_ENTER_CONFIG:Lmiuix/animation/base/AnimConfig;', '.field private static final ACTIVATE_EXIT_CONFIG:Lmiuix/animation/base/AnimConfig;', '.field private static final DISABLE_ENTER_CONFIG:Lmiuix/animation/base/AnimConfig;', '.field private static final DISABLE_EXIT_CONFIG:Lmiuix/animation/base/AnimConfig;', '.field private static final HOVER_ENTER_CONFIG:Lmiuix/animation/base/AnimConfig;']

PATCHES = [
    {
        'id': 'miuix_animation_styles_ColorStateEffect__getActivateEnterConfig',
        'method': '.method protected getActivateEnterConfig()Lmiuix/animation/base/AnimConfig;',
        'method_name': 'getActivateEnterConfig',
        'method_anchors': ['sget-object p0, Lmiuix/animation/styles/ColorStateEffect;->ACTIVATE_ENTER_CONFIG:Lmiuix/animation/base/AnimConfig;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getActivateEnterConfig()Lmiuix/animation/base/AnimConfig;
    .registers 1

    sget-object p0, Lmiuix/animation/styles/ColorStateEffect;->ACTIVATE_ENTER_CONFIG:Lmiuix/animation/base/AnimConfig;

    return-object p0
.end method""",
        'replacement': """.method protected getActivateEnterConfig()Lmiuix/animation/base/AnimConfig;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    sget-object p0, Lmiuix/animation/styles/ColorStateEffect;->ACTIVATE_ENTER_CONFIG:Lmiuix/animation/base/AnimConfig;

    goto :goto_1

    nop

    :goto_1
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_styles_ColorStateEffect__getActivateExitConfig',
        'method': '.method protected getActivateExitConfig()Lmiuix/animation/base/AnimConfig;',
        'method_name': 'getActivateExitConfig',
        'method_anchors': ['sget-object p0, Lmiuix/animation/styles/ColorStateEffect;->ACTIVATE_EXIT_CONFIG:Lmiuix/animation/base/AnimConfig;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getActivateExitConfig()Lmiuix/animation/base/AnimConfig;
    .registers 1

    sget-object p0, Lmiuix/animation/styles/ColorStateEffect;->ACTIVATE_EXIT_CONFIG:Lmiuix/animation/base/AnimConfig;

    return-object p0
.end method""",
        'replacement': """.method protected getActivateExitConfig()Lmiuix/animation/base/AnimConfig;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    sget-object p0, Lmiuix/animation/styles/ColorStateEffect;->ACTIVATE_EXIT_CONFIG:Lmiuix/animation/base/AnimConfig;

    goto :goto_1

    nop

    :goto_1
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_styles_ColorStateEffect__getDisableEnterConfig',
        'method': '.method protected getDisableEnterConfig()Lmiuix/animation/base/AnimConfig;',
        'method_name': 'getDisableEnterConfig',
        'method_anchors': ['sget-object p0, Lmiuix/animation/styles/ColorStateEffect;->DISABLE_ENTER_CONFIG:Lmiuix/animation/base/AnimConfig;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getDisableEnterConfig()Lmiuix/animation/base/AnimConfig;
    .registers 1

    sget-object p0, Lmiuix/animation/styles/ColorStateEffect;->DISABLE_ENTER_CONFIG:Lmiuix/animation/base/AnimConfig;

    return-object p0
.end method""",
        'replacement': """.method protected getDisableEnterConfig()Lmiuix/animation/base/AnimConfig;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    sget-object p0, Lmiuix/animation/styles/ColorStateEffect;->DISABLE_ENTER_CONFIG:Lmiuix/animation/base/AnimConfig;

    goto :goto_1

    nop

    :goto_1
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_styles_ColorStateEffect__getDisableExitConfig',
        'method': '.method protected getDisableExitConfig()Lmiuix/animation/base/AnimConfig;',
        'method_name': 'getDisableExitConfig',
        'method_anchors': ['sget-object p0, Lmiuix/animation/styles/ColorStateEffect;->DISABLE_EXIT_CONFIG:Lmiuix/animation/base/AnimConfig;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getDisableExitConfig()Lmiuix/animation/base/AnimConfig;
    .registers 1

    sget-object p0, Lmiuix/animation/styles/ColorStateEffect;->DISABLE_EXIT_CONFIG:Lmiuix/animation/base/AnimConfig;

    return-object p0
.end method""",
        'replacement': """.method protected getDisableExitConfig()Lmiuix/animation/base/AnimConfig;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    sget-object p0, Lmiuix/animation/styles/ColorStateEffect;->DISABLE_EXIT_CONFIG:Lmiuix/animation/base/AnimConfig;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_styles_ColorStateEffect__getHoverEnterConfig',
        'method': '.method protected getHoverEnterConfig()Lmiuix/animation/base/AnimConfig;',
        'method_name': 'getHoverEnterConfig',
        'method_anchors': ['sget-object p0, Lmiuix/animation/styles/ColorStateEffect;->HOVER_ENTER_CONFIG:Lmiuix/animation/base/AnimConfig;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getHoverEnterConfig()Lmiuix/animation/base/AnimConfig;
    .registers 1

    sget-object p0, Lmiuix/animation/styles/ColorStateEffect;->HOVER_ENTER_CONFIG:Lmiuix/animation/base/AnimConfig;

    return-object p0
.end method""",
        'replacement': """.method protected getHoverEnterConfig()Lmiuix/animation/base/AnimConfig;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    sget-object p0, Lmiuix/animation/styles/ColorStateEffect;->HOVER_ENTER_CONFIG:Lmiuix/animation/base/AnimConfig;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_styles_ColorStateEffect__getHoverExitConfig',
        'method': '.method protected getHoverExitConfig()Lmiuix/animation/base/AnimConfig;',
        'method_name': 'getHoverExitConfig',
        'method_anchors': ['sget-object p0, Lmiuix/animation/styles/ColorStateEffect;->HOVER_EXIT_CONFIG:Lmiuix/animation/base/AnimConfig;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getHoverExitConfig()Lmiuix/animation/base/AnimConfig;
    .registers 1

    sget-object p0, Lmiuix/animation/styles/ColorStateEffect;->HOVER_EXIT_CONFIG:Lmiuix/animation/base/AnimConfig;

    return-object p0
.end method""",
        'replacement': """.method protected getHoverExitConfig()Lmiuix/animation/base/AnimConfig;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    sget-object p0, Lmiuix/animation/styles/ColorStateEffect;->HOVER_EXIT_CONFIG:Lmiuix/animation/base/AnimConfig;

    goto :goto_1

    nop

    :goto_1
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_styles_ColorStateEffect__getNormalEnterConfig',
        'method': '.method protected getNormalEnterConfig()Lmiuix/animation/base/AnimConfig;',
        'method_name': 'getNormalEnterConfig',
        'method_anchors': ['sget-object p0, Lmiuix/animation/styles/ColorStateEffect;->NORMAL_ENTER_CONFIG:Lmiuix/animation/base/AnimConfig;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getNormalEnterConfig()Lmiuix/animation/base/AnimConfig;
    .registers 1

    sget-object p0, Lmiuix/animation/styles/ColorStateEffect;->NORMAL_ENTER_CONFIG:Lmiuix/animation/base/AnimConfig;

    return-object p0
.end method""",
        'replacement': """.method protected getNormalEnterConfig()Lmiuix/animation/base/AnimConfig;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    sget-object p0, Lmiuix/animation/styles/ColorStateEffect;->NORMAL_ENTER_CONFIG:Lmiuix/animation/base/AnimConfig;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_styles_ColorStateEffect__getNormalExitConfig',
        'method': '.method protected getNormalExitConfig()Lmiuix/animation/base/AnimConfig;',
        'method_name': 'getNormalExitConfig',
        'method_anchors': ['sget-object p0, Lmiuix/animation/styles/ColorStateEffect;->NORMAL_EXIT_CONFIG:Lmiuix/animation/base/AnimConfig;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getNormalExitConfig()Lmiuix/animation/base/AnimConfig;
    .registers 1

    sget-object p0, Lmiuix/animation/styles/ColorStateEffect;->NORMAL_EXIT_CONFIG:Lmiuix/animation/base/AnimConfig;

    return-object p0
.end method""",
        'replacement': """.method protected getNormalExitConfig()Lmiuix/animation/base/AnimConfig;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    sget-object p0, Lmiuix/animation/styles/ColorStateEffect;->NORMAL_EXIT_CONFIG:Lmiuix/animation/base/AnimConfig;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_styles_ColorStateEffect__getPressEnterConfig',
        'method': '.method protected getPressEnterConfig()Lmiuix/animation/base/AnimConfig;',
        'method_name': 'getPressEnterConfig',
        'method_anchors': ['sget-object p0, Lmiuix/animation/styles/ColorStateEffect;->PRESS_ENTER_CONFIG:Lmiuix/animation/base/AnimConfig;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getPressEnterConfig()Lmiuix/animation/base/AnimConfig;
    .registers 1

    sget-object p0, Lmiuix/animation/styles/ColorStateEffect;->PRESS_ENTER_CONFIG:Lmiuix/animation/base/AnimConfig;

    return-object p0
.end method""",
        'replacement': """.method protected getPressEnterConfig()Lmiuix/animation/base/AnimConfig;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    sget-object p0, Lmiuix/animation/styles/ColorStateEffect;->PRESS_ENTER_CONFIG:Lmiuix/animation/base/AnimConfig;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_styles_ColorStateEffect__getPressExitConfig',
        'method': '.method protected getPressExitConfig()Lmiuix/animation/base/AnimConfig;',
        'method_name': 'getPressExitConfig',
        'method_anchors': ['sget-object p0, Lmiuix/animation/styles/ColorStateEffect;->PRESS_EXIT_CONFIG:Lmiuix/animation/base/AnimConfig;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getPressExitConfig()Lmiuix/animation/base/AnimConfig;
    .registers 1

    sget-object p0, Lmiuix/animation/styles/ColorStateEffect;->PRESS_EXIT_CONFIG:Lmiuix/animation/base/AnimConfig;

    return-object p0
.end method""",
        'replacement': """.method protected getPressExitConfig()Lmiuix/animation/base/AnimConfig;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    sget-object p0, Lmiuix/animation/styles/ColorStateEffect;->PRESS_EXIT_CONFIG:Lmiuix/animation/base/AnimConfig;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
