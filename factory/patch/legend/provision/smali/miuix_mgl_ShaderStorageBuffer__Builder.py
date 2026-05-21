TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/mgl/ShaderStorageBuffer$Builder.smali'
CLASS_FALLBACK_NAMES = ['ShaderStorageBuffer$Builder.smali']
CLASS_ANCHORS = ['.super Lmiuix/mgl/utils/NativeObject;']

PATCHES = [
    {
        'id': 'miuix_mgl_ShaderStorageBuffer__Builder__onDestroyNativeObject',
        'method': '.method protected onDestroyNativeObject(J)V',
        'method_name': 'onDestroyNativeObject',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/mgl/utils/NativeObject;->getNativeObject()J', 'invoke-static {p0, p1}, Lmiuix/mgl/BufferObject;->nBuilderDestroyBuilder(J)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onDestroyNativeObject(J)V
    .registers 3

    invoke-virtual {p0}, Lmiuix/mgl/utils/NativeObject;->getNativeObject()J

    move-result-wide p0

    invoke-static {p0, p1}, Lmiuix/mgl/BufferObject;->nBuilderDestroyBuilder(J)V

    return-void
.end method""",
        'replacement': """.method protected onDestroyNativeObject(J)V
    .registers 3

    goto :goto_0

    nop

    :goto_0
    invoke-virtual {p0}, Lmiuix/mgl/utils/NativeObject;->getNativeObject()J

    move-result-wide p0

    goto :goto_1

    nop

    :goto_1
    invoke-static {p0, p1}, Lmiuix/mgl/BufferObject;->nBuilderDestroyBuilder(J)V

    goto :goto_2

    nop

    :goto_2
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
