TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/mgl/physics/Draw.smali'
CLASS_FALLBACK_NAMES = ['Draw.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field public static final AABB_BIT:I = 0x4', '.field public static final CENTER_OF_MASS_BIT:I = 0x10', '.field public static final PAIR_BIT:I = 0x8', '.field public static final PARTICLE_BIT:I = 0x20', '.field public static final SHAPE_BIT:I = 0x1']

PATCHES = [
    {
        'id': 'miuix_mgl_physics_Draw__finalize',
        'method': '.method protected finalize()V',
        'method_name': 'finalize',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/mgl/physics/Draw;->delete()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected finalize()V
    .registers 1

    invoke-virtual {p0}, Lmiuix/mgl/physics/Draw;->delete()V

    return-void
.end method""",
        'replacement': """.method protected finalize()V
    .registers 1

    goto :goto_0

    nop

    :goto_0
    invoke-virtual {p0}, Lmiuix/mgl/physics/Draw;->delete()V

    goto :goto_1

    nop

    :goto_1
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_mgl_physics_Draw__swigDirectorDisconnect',
        'method': '.method protected swigDirectorDisconnect()V',
        'method_name': 'swigDirectorDisconnect',
        'method_anchors': ['iput-boolean v0, p0, Lmiuix/mgl/physics/Draw;->swigCMemOwn:Z', 'invoke-virtual {p0}, Lmiuix/mgl/physics/Draw;->delete()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected swigDirectorDisconnect()V
    .registers 2

    const/4 v0, 0x0

    iput-boolean v0, p0, Lmiuix/mgl/physics/Draw;->swigCMemOwn:Z

    invoke-virtual {p0}, Lmiuix/mgl/physics/Draw;->delete()V

    return-void
.end method""",
        'replacement': """.method protected swigDirectorDisconnect()V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    const/4 v0, 0x0

    goto :goto_2

    nop

    :goto_2
    iput-boolean v0, p0, Lmiuix/mgl/physics/Draw;->swigCMemOwn:Z

    goto :goto_3

    nop

    :goto_3
    invoke-virtual {p0}, Lmiuix/mgl/physics/Draw;->delete()V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
