TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/mgl/physics/CircleShape.smali'
CLASS_FALLBACK_NAMES = ['CircleShape.smali']
CLASS_ANCHORS = ['.super Lmiuix/mgl/physics/Shape;']

PATCHES = [
    {
        'id': 'miuix_mgl_physics_CircleShape__finalize',
        'method': '.method protected finalize()V',
        'method_name': 'finalize',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/mgl/physics/CircleShape;->delete()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected finalize()V
    .registers 1

    invoke-virtual {p0}, Lmiuix/mgl/physics/CircleShape;->delete()V

    return-void
.end method""",
        'replacement': """.method protected finalize()V
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    invoke-virtual {p0}, Lmiuix/mgl/physics/CircleShape;->delete()V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
