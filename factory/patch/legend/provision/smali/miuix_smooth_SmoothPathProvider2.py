TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/smooth/SmoothPathProvider2.smali'
CLASS_FALLBACK_NAMES = ['SmoothPathProvider2.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'miuix_smooth_SmoothPathProvider2__getKsi',
        'method': '.method getKsi()F',
        'method_name': 'getKsi',
        'method_anchors': ['iget p0, p0, Lmiuix/smooth/SmoothPathProvider2;->mKsi:F', 'return p0'],
        'type': 'method_replace',
        'search': """.method getKsi()F
    .registers 1

    iget p0, p0, Lmiuix/smooth/SmoothPathProvider2;->mKsi:F

    return p0
.end method""",
        'replacement': """.method getKsi()F
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    iget p0, p0, Lmiuix/smooth/SmoothPathProvider2;->mKsi:F

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_smooth_SmoothPathProvider2__getSmooth',
        'method': '.method getSmooth()F',
        'method_name': 'getSmooth',
        'method_anchors': ['iget p0, p0, Lmiuix/smooth/SmoothPathProvider2;->mSmooth:F', 'return p0'],
        'type': 'method_replace',
        'search': """.method getSmooth()F
    .registers 1

    iget p0, p0, Lmiuix/smooth/SmoothPathProvider2;->mSmooth:F

    return p0
.end method""",
        'replacement': """.method getSmooth()F
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    iget p0, p0, Lmiuix/smooth/SmoothPathProvider2;->mSmooth:F

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
