TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/mgl/physics/FixtureProxy.smali'
CLASS_FALLBACK_NAMES = ['FixtureProxy.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'miuix_mgl_physics_FixtureProxy__finalize',
        'method': '.method protected finalize()V',
        'method_name': 'finalize',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/mgl/physics/FixtureProxy;->delete()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected finalize()V
    .registers 1

    invoke-virtual {p0}, Lmiuix/mgl/physics/FixtureProxy;->delete()V

    return-void
.end method""",
        'replacement': """.method protected finalize()V
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    invoke-virtual {p0}, Lmiuix/mgl/physics/FixtureProxy;->delete()V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
