TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/airbnb/lottie/model/layer/NullLayer.smali'
CLASS_FALLBACK_NAMES = ['NullLayer.smali']
CLASS_ANCHORS = ['.super Lcom/airbnb/lottie/model/layer/BaseLayer;']

PATCHES = [
    {
        'id': 'com_airbnb_lottie_model_layer_NullLayer__drawLayer',
        'method': '.method drawLayer(Landroid/graphics/Canvas;Landroid/graphics/Matrix;I)V',
        'method_name': 'drawLayer',
        'method_anchors': ['return-void'],
        'type': 'method_replace',
        'search': """.method drawLayer(Landroid/graphics/Canvas;Landroid/graphics/Matrix;I)V
    .registers 4

    return-void
.end method""",
        'replacement': """.method drawLayer(Landroid/graphics/Canvas;Landroid/graphics/Matrix;I)V
    .registers 4

    goto :goto_0

    nop

    :goto_0
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
