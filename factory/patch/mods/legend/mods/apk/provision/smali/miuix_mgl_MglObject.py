TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/mgl/MglObject.smali'
CLASS_FALLBACK_NAMES = ['MglObject.smali']
CLASS_ANCHORS = ['.super Lmiuix/mgl/utils/NativeObject;']

PATCHES = [
    {
        'id': 'miuix_mgl_MglObject__onDestroyNativeObject',
        'method': '.method protected onDestroyNativeObject(J)V',
        'method_name': 'onDestroyNativeObject',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/mgl/utils/NativeObject;->getNativeObject()J', 'iget-boolean p0, p0, Lmiuix/mgl/MglObject;->mDestroyGraphicResource:Z', 'invoke-static {p1, p2, p0}, Lmiuix/mgl/MglObject;->nDestroyMglObject(JZ)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onDestroyNativeObject(J)V
    .registers 3

    invoke-virtual {p0}, Lmiuix/mgl/utils/NativeObject;->getNativeObject()J

    move-result-wide p1

    iget-boolean p0, p0, Lmiuix/mgl/MglObject;->mDestroyGraphicResource:Z

    invoke-static {p1, p2, p0}, Lmiuix/mgl/MglObject;->nDestroyMglObject(JZ)V

    return-void
.end method""",
        'replacement': """.method protected onDestroyNativeObject(J)V
    .registers 3

    goto :goto_0

    nop

    :goto_0
    invoke-virtual {p0}, Lmiuix/mgl/utils/NativeObject;->getNativeObject()J

    move-result-wide p1

    goto :goto_1

    nop

    :goto_1
    iget-boolean p0, p0, Lmiuix/mgl/MglObject;->mDestroyGraphicResource:Z

    goto :goto_3

    nop

    :goto_2
    return-void

    :goto_3
    invoke-static {p1, p2, p0}, Lmiuix/mgl/MglObject;->nDestroyMglObject(JZ)V

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
