TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/mgl/Primitive$Builder.smali'
CLASS_FALLBACK_NAMES = ['Primitive$Builder.smali']
CLASS_ANCHORS = ['.super Lmiuix/mgl/utils/NativeObject;']

PATCHES = [
    {
        'id': 'miuix_mgl_Primitive__Builder__onDestroyNativeObject',
        'method': '.method protected onDestroyNativeObject(J)V',
        'method_name': 'onDestroyNativeObject',
        'method_anchors': ['invoke-static {p1, p2}, Lmiuix/mgl/Primitive$Builder;->nDestroyBuilder(J)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onDestroyNativeObject(J)V
    .registers 3

    invoke-static {p1, p2}, Lmiuix/mgl/Primitive$Builder;->nDestroyBuilder(J)V

    return-void
.end method""",
        'replacement': """.method protected onDestroyNativeObject(J)V
    .registers 3

    goto :goto_0

    nop

    :goto_0
    invoke-static {p1, p2}, Lmiuix/mgl/Primitive$Builder;->nDestroyBuilder(J)V

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
