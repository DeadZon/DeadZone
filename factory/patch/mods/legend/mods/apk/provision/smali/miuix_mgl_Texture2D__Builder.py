TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/mgl/Texture2D$Builder.smali'
CLASS_FALLBACK_NAMES = ['Texture2D$Builder.smali']
CLASS_ANCHORS = ['.super Lmiuix/mgl/utils/NativeObject;']

PATCHES = [
    {
        'id': 'miuix_mgl_Texture2D__Builder__onDestroyNativeObject',
        'method': '.method protected onDestroyNativeObject(J)V',
        'method_name': 'onDestroyNativeObject',
        'method_anchors': ['invoke-static {p1, p2}, Lmiuix/mgl/Texture2D$Builder;->nDestroyBuilder(J)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onDestroyNativeObject(J)V
    .registers 3

    invoke-static {p1, p2}, Lmiuix/mgl/Texture2D$Builder;->nDestroyBuilder(J)V

    return-void
.end method""",
        'replacement': """.method protected onDestroyNativeObject(J)V
    .registers 3

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    invoke-static {p1, p2}, Lmiuix/mgl/Texture2D$Builder;->nDestroyBuilder(J)V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
