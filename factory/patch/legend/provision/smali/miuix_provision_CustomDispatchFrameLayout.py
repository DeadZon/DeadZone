TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/provision/CustomDispatchFrameLayout.smali'
CLASS_FALLBACK_NAMES = ['CustomDispatchFrameLayout.smali']
CLASS_ANCHORS = ['.super Landroid/widget/FrameLayout;']

PATCHES = [
    {
        'id': 'miuix_provision_CustomDispatchFrameLayout__isAnimEnded',
        'method': '.method protected isAnimEnded()Z',
        'method_name': 'isAnimEnded',
        'method_anchors': ['iget-object p0, p0, Lmiuix/provision/CustomDispatchFrameLayout;->mProvisionAnimHelper:Lmiuix/provision/ProvisionAnimHelper;', 'if-eqz p0, :cond_0', 'invoke-virtual {p0}, Lmiuix/provision/ProvisionAnimHelper;->isAnimEnded()Z', 'return p0', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected isAnimEnded()Z
    .registers 1

    iget-object p0, p0, Lmiuix/provision/CustomDispatchFrameLayout;->mProvisionAnimHelper:Lmiuix/provision/ProvisionAnimHelper;

    if-eqz p0, :cond_0

    invoke-virtual {p0}, Lmiuix/provision/ProvisionAnimHelper;->isAnimEnded()Z

    move-result p0

    return p0

    :cond_0
    const/4 p0, 0x1

    return p0
.end method""",
        'replacement': """.method protected isAnimEnded()Z
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/provision/CustomDispatchFrameLayout;->mProvisionAnimHelper:Lmiuix/provision/ProvisionAnimHelper;

    goto :goto_6

    nop

    :goto_1
    return p0

    :goto_2
    return p0

    :goto_3
    goto :goto_4

    nop

    :goto_4
    const/4 p0, 0x1

    goto :goto_1

    nop

    :goto_5
    invoke-virtual {p0}, Lmiuix/provision/ProvisionAnimHelper;->isAnimEnded()Z

    move-result p0

    goto :goto_2

    nop

    :goto_6
    if-nez p0, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
