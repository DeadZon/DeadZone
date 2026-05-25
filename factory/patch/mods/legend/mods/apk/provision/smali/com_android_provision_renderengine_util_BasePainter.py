TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/renderengine/util/BasePainter.smali'
CLASS_FALLBACK_NAMES = ['BasePainter.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'com_android_provision_renderengine_util_BasePainter__getCompId',
        'method': '.method protected getCompId()I',
        'method_name': 'getCompId',
        'method_anchors': ['return p0'],
        'type': 'method_replace',
        'search': """.method protected getCompId()I
    .registers 1

    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method protected getCompId()I
    .registers 1

    goto :goto_0

    nop

    :goto_0
    const/4 p0, 0x0

    goto :goto_1

    nop

    :goto_1
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_renderengine_util_BasePainter__getFragId',
        'method': '.method protected getFragId()I',
        'method_name': 'getFragId',
        'method_anchors': ['return p0'],
        'type': 'method_replace',
        'search': """.method protected getFragId()I
    .registers 1

    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method protected getFragId()I
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    const/4 p0, 0x0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_renderengine_util_BasePainter__getVertId',
        'method': '.method protected getVertId()I',
        'method_name': 'getVertId',
        'method_anchors': ['sget p0, Lcom/android/provision/R$raw;->vertex_shader:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected getVertId()I
    .registers 1

    sget p0, Lcom/android/provision/R$raw;->vertex_shader:I

    return p0
.end method""",
        'replacement': """.method protected getVertId()I
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    sget p0, Lcom/android/provision/R$raw;->vertex_shader:I

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_renderengine_util_BasePainter__initMKey',
        'method': '.method protected initMKey()V',
        'method_name': 'initMKey',
        'method_anchors': ['new-instance v0, Lcom/android/provision/renderengine/util/MaterialRepo$MKey;', 'invoke-virtual {p0}, Lcom/android/provision/renderengine/util/BasePainter;->getVertId()I', 'invoke-virtual {p0}, Lcom/android/provision/renderengine/util/BasePainter;->getFragId()I', 'invoke-direct {v0, v1, v2}, Lcom/android/provision/renderengine/util/MaterialRepo$MKey;-><init>(II)V', 'iput-object v0, p0, Lcom/android/provision/renderengine/util/BasePainter;->key:Lcom/android/provision/renderengine/util/MaterialRepo$MKey;', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected initMKey()V
    .registers 4

    new-instance v0, Lcom/android/provision/renderengine/util/MaterialRepo$MKey;

    invoke-virtual {p0}, Lcom/android/provision/renderengine/util/BasePainter;->getVertId()I

    move-result v1

    invoke-virtual {p0}, Lcom/android/provision/renderengine/util/BasePainter;->getFragId()I

    move-result v2

    invoke-direct {v0, v1, v2}, Lcom/android/provision/renderengine/util/MaterialRepo$MKey;-><init>(II)V

    iput-object v0, p0, Lcom/android/provision/renderengine/util/BasePainter;->key:Lcom/android/provision/renderengine/util/MaterialRepo$MKey;

    return-void
.end method""",
        'replacement': """.method protected initMKey()V
    .registers 4

    goto :goto_2

    nop

    :goto_0
    return-void

    :goto_1
    iput-object v0, p0, Lcom/android/provision/renderengine/util/BasePainter;->key:Lcom/android/provision/renderengine/util/MaterialRepo$MKey;

    goto :goto_0

    nop

    :goto_2
    new-instance v0, Lcom/android/provision/renderengine/util/MaterialRepo$MKey;

    goto :goto_5

    nop

    :goto_3
    invoke-direct {v0, v1, v2}, Lcom/android/provision/renderengine/util/MaterialRepo$MKey;-><init>(II)V

    goto :goto_1

    nop

    :goto_4
    invoke-virtual {p0}, Lcom/android/provision/renderengine/util/BasePainter;->getFragId()I

    move-result v2

    goto :goto_3

    nop

    :goto_5
    invoke-virtual {p0}, Lcom/android/provision/renderengine/util/BasePainter;->getVertId()I

    move-result v1

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_renderengine_util_BasePainter__initPrimitive',
        'method': '.method protected initPrimitive()Lmiuix/mgl/Primitive;',
        'method_name': 'initPrimitive',
        'method_anchors': ['iget-object p0, p0, Lcom/android/provision/renderengine/util/BasePainter;->renderContext:Lcom/android/provision/renderengine/util/RenderContext;', 'invoke-virtual {p0}, Lcom/android/provision/renderengine/util/RenderContext;->getMaterialRepo()Lcom/android/provision/renderengine/util/MaterialRepo;', 'invoke-virtual {p0}, Lcom/android/provision/renderengine/util/MaterialRepo;->getDefaultPrimitive()Lmiuix/mgl/Primitive;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected initPrimitive()Lmiuix/mgl/Primitive;
    .registers 1

    iget-object p0, p0, Lcom/android/provision/renderengine/util/BasePainter;->renderContext:Lcom/android/provision/renderengine/util/RenderContext;

    invoke-virtual {p0}, Lcom/android/provision/renderengine/util/RenderContext;->getMaterialRepo()Lcom/android/provision/renderengine/util/MaterialRepo;

    move-result-object p0

    invoke-virtual {p0}, Lcom/android/provision/renderengine/util/MaterialRepo;->getDefaultPrimitive()Lmiuix/mgl/Primitive;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected initPrimitive()Lmiuix/mgl/Primitive;
    .registers 1

    goto :goto_3

    nop

    :goto_0
    invoke-virtual {p0}, Lcom/android/provision/renderengine/util/MaterialRepo;->getDefaultPrimitive()Lmiuix/mgl/Primitive;

    move-result-object p0

    goto :goto_1

    nop

    :goto_1
    return-object p0

    :goto_2
    invoke-virtual {p0}, Lcom/android/provision/renderengine/util/RenderContext;->getMaterialRepo()Lcom/android/provision/renderengine/util/MaterialRepo;

    move-result-object p0

    goto :goto_0

    nop

    :goto_3
    iget-object p0, p0, Lcom/android/provision/renderengine/util/BasePainter;->renderContext:Lcom/android/provision/renderengine/util/RenderContext;

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
