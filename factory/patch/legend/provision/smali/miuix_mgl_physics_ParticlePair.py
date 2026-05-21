TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/mgl/physics/ParticlePair.smali'
CLASS_FALLBACK_NAMES = ['ParticlePair.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'miuix_mgl_physics_ParticlePair__finalize',
        'method': '.method protected finalize()V',
        'method_name': 'finalize',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/mgl/physics/ParticlePair;->delete()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected finalize()V
    .registers 1

    invoke-virtual {p0}, Lmiuix/mgl/physics/ParticlePair;->delete()V

    return-void
.end method""",
        'replacement': """.method protected finalize()V
    .registers 1

    goto :goto_0

    nop

    :goto_0
    invoke-virtual {p0}, Lmiuix/mgl/physics/ParticlePair;->delete()V

    goto :goto_1

    nop

    :goto_1
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
