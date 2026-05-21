TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/transition/ChangeBounds$ViewBounds.smali'
CLASS_FALLBACK_NAMES = ['ChangeBounds$ViewBounds.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'miuix_transition_ChangeBounds__ViewBounds__getBottom',
        'method': '.method getBottom()I',
        'method_name': 'getBottom',
        'method_anchors': ['iget p0, p0, Lmiuix/transition/ChangeBounds$ViewBounds;->bottom:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method getBottom()I
    .registers 1

    iget p0, p0, Lmiuix/transition/ChangeBounds$ViewBounds;->bottom:I

    return p0
.end method""",
        'replacement': """.method getBottom()I
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget p0, p0, Lmiuix/transition/ChangeBounds$ViewBounds;->bottom:I

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
        'id': 'miuix_transition_ChangeBounds__ViewBounds__getLeft',
        'method': '.method getLeft()I',
        'method_name': 'getLeft',
        'method_anchors': ['iget p0, p0, Lmiuix/transition/ChangeBounds$ViewBounds;->left:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method getLeft()I
    .registers 1

    iget p0, p0, Lmiuix/transition/ChangeBounds$ViewBounds;->left:I

    return p0
.end method""",
        'replacement': """.method getLeft()I
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    iget p0, p0, Lmiuix/transition/ChangeBounds$ViewBounds;->left:I

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_transition_ChangeBounds__ViewBounds__getRight',
        'method': '.method getRight()I',
        'method_name': 'getRight',
        'method_anchors': ['iget p0, p0, Lmiuix/transition/ChangeBounds$ViewBounds;->right:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method getRight()I
    .registers 1

    iget p0, p0, Lmiuix/transition/ChangeBounds$ViewBounds;->right:I

    return p0
.end method""",
        'replacement': """.method getRight()I
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget p0, p0, Lmiuix/transition/ChangeBounds$ViewBounds;->right:I

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
        'id': 'miuix_transition_ChangeBounds__ViewBounds__getTop',
        'method': '.method getTop()I',
        'method_name': 'getTop',
        'method_anchors': ['iget p0, p0, Lmiuix/transition/ChangeBounds$ViewBounds;->top:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method getTop()I
    .registers 1

    iget p0, p0, Lmiuix/transition/ChangeBounds$ViewBounds;->top:I

    return p0
.end method""",
        'replacement': """.method getTop()I
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget p0, p0, Lmiuix/transition/ChangeBounds$ViewBounds;->top:I

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
