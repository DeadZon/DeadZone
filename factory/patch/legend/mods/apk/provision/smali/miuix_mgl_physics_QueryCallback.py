TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/mgl/physics/QueryCallback.smali'
CLASS_FALLBACK_NAMES = ['QueryCallback.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'miuix_mgl_physics_QueryCallback__finalize',
        'method': '.method protected finalize()V',
        'method_name': 'finalize',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/mgl/physics/QueryCallback;->delete()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected finalize()V
    .registers 1

    invoke-virtual {p0}, Lmiuix/mgl/physics/QueryCallback;->delete()V

    return-void
.end method""",
        'replacement': """.method protected finalize()V
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    invoke-virtual {p0}, Lmiuix/mgl/physics/QueryCallback;->delete()V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_mgl_physics_QueryCallback__swigDirectorDisconnect',
        'method': '.method protected swigDirectorDisconnect()V',
        'method_name': 'swigDirectorDisconnect',
        'method_anchors': ['iput-boolean v0, p0, Lmiuix/mgl/physics/QueryCallback;->swigCMemOwn:Z', 'invoke-virtual {p0}, Lmiuix/mgl/physics/QueryCallback;->delete()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected swigDirectorDisconnect()V
    .registers 2

    const/4 v0, 0x0

    iput-boolean v0, p0, Lmiuix/mgl/physics/QueryCallback;->swigCMemOwn:Z

    invoke-virtual {p0}, Lmiuix/mgl/physics/QueryCallback;->delete()V

    return-void
.end method""",
        'replacement': """.method protected swigDirectorDisconnect()V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    invoke-virtual {p0}, Lmiuix/mgl/physics/QueryCallback;->delete()V

    goto :goto_3

    nop

    :goto_1
    const/4 v0, 0x0

    goto :goto_2

    nop

    :goto_2
    iput-boolean v0, p0, Lmiuix/mgl/physics/QueryCallback;->swigCMemOwn:Z

    goto :goto_0

    nop

    :goto_3
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
