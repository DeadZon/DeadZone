TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/mgl/Material.smali'
CLASS_FALLBACK_NAMES = ['Material.smali']
CLASS_ANCHORS = ['.super Lmiuix/mgl/MglObject;']

PATCHES = [
    {
        'id': 'miuix_mgl_Material__addRef',
        'method': '.method protected addRef(ILmiuix/mgl/MglObject;)V',
        'method_name': 'addRef',
        'method_anchors': ['iget-object p0, p0, Lmiuix/mgl/Material;->mRefIntKey:Ljava/util/HashMap;', 'invoke-static {p1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;', 'invoke-virtual {p0, p1, p2}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected addRef(ILmiuix/mgl/MglObject;)V
    .registers 3

    iget-object p0, p0, Lmiuix/mgl/Material;->mRefIntKey:Ljava/util/HashMap;

    invoke-static {p1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p1

    invoke-virtual {p0, p1, p2}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    return-void
.end method""",
        'replacement': """.method protected addRef(ILmiuix/mgl/MglObject;)V
    .registers 3

    goto :goto_3

    nop

    :goto_0
    return-void

    :goto_1
    invoke-virtual {p0, p1, p2}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_0

    nop

    :goto_2
    invoke-static {p1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p1

    goto :goto_1

    nop

    :goto_3
    iget-object p0, p0, Lmiuix/mgl/Material;->mRefIntKey:Ljava/util/HashMap;

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_mgl_Material__addRef',
        'method': '.method protected addRef(Ljava/lang/String;Lmiuix/mgl/MglObject;)V',
        'method_name': 'addRef',
        'method_anchors': ['iget-object p0, p0, Lmiuix/mgl/Material;->mRefStringKey:Ljava/util/HashMap;', 'invoke-virtual {p0, p1, p2}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected addRef(Ljava/lang/String;Lmiuix/mgl/MglObject;)V
    .registers 3

    iget-object p0, p0, Lmiuix/mgl/Material;->mRefStringKey:Ljava/util/HashMap;

    invoke-virtual {p0, p1, p2}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    return-void
.end method""",
        'replacement': """.method protected addRef(Ljava/lang/String;Lmiuix/mgl/MglObject;)V
    .registers 3

    goto :goto_2

    nop

    :goto_0
    return-void

    :goto_1
    invoke-virtual {p0, p1, p2}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_0

    nop

    :goto_2
    iget-object p0, p0, Lmiuix/mgl/Material;->mRefStringKey:Ljava/util/HashMap;

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
