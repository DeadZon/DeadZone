TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/app/widget/SecondaryTabExpandContainerView.smali'
CLASS_FALLBACK_NAMES = ['SecondaryTabExpandContainerView.smali']
CLASS_ANCHORS = ['.super Lmiuix/appcompat/internal/app/widget/SecondaryTabContainerView;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_app_widget_SecondaryTabExpandContainerView__getDefaultTabTextStyle',
        'method': '.method protected getDefaultTabTextStyle()I',
        'method_name': 'getDefaultTabTextStyle',
        'method_anchors': ['sget p0, Lmiuix/appcompat/R$attr;->actionBarTabTextSecondaryExpandStyle:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected getDefaultTabTextStyle()I
    .registers 1

    sget p0, Lmiuix/appcompat/R$attr;->actionBarTabTextSecondaryExpandStyle:I

    return p0
.end method""",
        'replacement': """.method protected getDefaultTabTextStyle()I
    .registers 1

    goto :goto_0

    nop

    :goto_0
    sget p0, Lmiuix/appcompat/R$attr;->actionBarTabTextSecondaryExpandStyle:I

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
        'id': 'miuix_appcompat_internal_app_widget_SecondaryTabExpandContainerView__getTabActivatedTextStyle',
        'method': '.method protected getTabActivatedTextStyle()I',
        'method_name': 'getTabActivatedTextStyle',
        'method_anchors': ['sget p0, Lmiuix/appcompat/R$attr;->actionBarTabActivatedTextSecondaryExpandStyle:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected getTabActivatedTextStyle()I
    .registers 1

    sget p0, Lmiuix/appcompat/R$attr;->actionBarTabActivatedTextSecondaryExpandStyle:I

    return p0
.end method""",
        'replacement': """.method protected getTabActivatedTextStyle()I
    .registers 1

    goto :goto_0

    nop

    :goto_0
    sget p0, Lmiuix/appcompat/R$attr;->actionBarTabActivatedTextSecondaryExpandStyle:I

    goto :goto_1

    nop

    :goto_1
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
