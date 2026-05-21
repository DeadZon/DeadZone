TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/mgl/AssetParser.smali'
CLASS_FALLBACK_NAMES = ['AssetParser.smali']
CLASS_ANCHORS = ['.super Lmiuix/mgl/utils/NativeObject;']

PATCHES = [
    {
        'id': 'miuix_mgl_AssetParser__onDestroyNativeObject',
        'method': '.method protected onDestroyNativeObject(J)V',
        'method_name': 'onDestroyNativeObject',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/mgl/utils/NativeObject;->getNativeObject()J', 'invoke-static {p0, p1}, Lmiuix/mgl/AssetParser;->nDestroyParser(J)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onDestroyNativeObject(J)V
    .registers 3

    invoke-virtual {p0}, Lmiuix/mgl/utils/NativeObject;->getNativeObject()J

    move-result-wide p0

    invoke-static {p0, p1}, Lmiuix/mgl/AssetParser;->nDestroyParser(J)V

    return-void
.end method""",
        'replacement': """.method protected onDestroyNativeObject(J)V
    .registers 3

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    invoke-virtual {p0}, Lmiuix/mgl/utils/NativeObject;->getNativeObject()J

    move-result-wide p0

    goto :goto_2

    nop

    :goto_2
    invoke-static {p0, p1}, Lmiuix/mgl/AssetParser;->nDestroyParser(J)V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
