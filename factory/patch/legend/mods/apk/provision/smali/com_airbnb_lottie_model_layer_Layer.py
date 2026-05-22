TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/airbnb/lottie/model/layer/Layer.smali'
CLASS_FALLBACK_NAMES = ['Layer.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'com_airbnb_lottie_model_layer_Layer__getComposition',
        'method': '.method getComposition()Lcom/airbnb/lottie/LottieComposition;',
        'method_name': 'getComposition',
        'method_anchors': ['iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->composition:Lcom/airbnb/lottie/LottieComposition;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method getComposition()Lcom/airbnb/lottie/LottieComposition;
    .registers 1

    iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->composition:Lcom/airbnb/lottie/LottieComposition;

    return-object p0
.end method""",
        'replacement': """.method getComposition()Lcom/airbnb/lottie/LottieComposition;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->composition:Lcom/airbnb/lottie/LottieComposition;

    goto :goto_1

    nop

    :goto_1
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_model_layer_Layer__getInOutKeyframes',
        'method': '.method getInOutKeyframes()Ljava/util/List;',
        'method_name': 'getInOutKeyframes',
        'method_anchors': ['iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->inOutKeyframes:Ljava/util/List;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method getInOutKeyframes()Ljava/util/List;
    .registers 1

    iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->inOutKeyframes:Ljava/util/List;

    return-object p0
.end method""",
        'replacement': """.method getInOutKeyframes()Ljava/util/List;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->inOutKeyframes:Ljava/util/List;

    goto :goto_1

    nop

    :goto_1
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_model_layer_Layer__getMasks',
        'method': '.method getMasks()Ljava/util/List;',
        'method_name': 'getMasks',
        'method_anchors': ['iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->masks:Ljava/util/List;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method getMasks()Ljava/util/List;
    .registers 1

    iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->masks:Ljava/util/List;

    return-object p0
.end method""",
        'replacement': """.method getMasks()Ljava/util/List;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->masks:Ljava/util/List;

    goto :goto_1

    nop

    :goto_1
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_model_layer_Layer__getMatteType',
        'method': '.method getMatteType()Lcom/airbnb/lottie/model/layer/Layer$MatteType;',
        'method_name': 'getMatteType',
        'method_anchors': ['iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->matteType:Lcom/airbnb/lottie/model/layer/Layer$MatteType;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method getMatteType()Lcom/airbnb/lottie/model/layer/Layer$MatteType;
    .registers 1

    iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->matteType:Lcom/airbnb/lottie/model/layer/Layer$MatteType;

    return-object p0
.end method""",
        'replacement': """.method getMatteType()Lcom/airbnb/lottie/model/layer/Layer$MatteType;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->matteType:Lcom/airbnb/lottie/model/layer/Layer$MatteType;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_model_layer_Layer__getName',
        'method': '.method getName()Ljava/lang/String;',
        'method_name': 'getName',
        'method_anchors': ['iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->layerName:Ljava/lang/String;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method getName()Ljava/lang/String;
    .registers 1

    iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->layerName:Ljava/lang/String;

    return-object p0
.end method""",
        'replacement': """.method getName()Ljava/lang/String;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->layerName:Ljava/lang/String;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_model_layer_Layer__getParentId',
        'method': '.method getParentId()J',
        'method_name': 'getParentId',
        'method_anchors': ['iget-wide v0, p0, Lcom/airbnb/lottie/model/layer/Layer;->parentId:J', 'return-wide v0'],
        'type': 'method_replace',
        'search': """.method getParentId()J
    .registers 3

    iget-wide v0, p0, Lcom/airbnb/lottie/model/layer/Layer;->parentId:J

    return-wide v0
.end method""",
        'replacement': """.method getParentId()J
    .registers 3

    goto :goto_0

    nop

    :goto_0
    iget-wide v0, p0, Lcom/airbnb/lottie/model/layer/Layer;->parentId:J

    goto :goto_1

    nop

    :goto_1
    return-wide v0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_model_layer_Layer__getPreCompHeight',
        'method': '.method getPreCompHeight()I',
        'method_name': 'getPreCompHeight',
        'method_anchors': ['iget p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->preCompHeight:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method getPreCompHeight()I
    .registers 1

    iget p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->preCompHeight:I

    return p0
.end method""",
        'replacement': """.method getPreCompHeight()I
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->preCompHeight:I

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
        'id': 'com_airbnb_lottie_model_layer_Layer__getPreCompWidth',
        'method': '.method getPreCompWidth()I',
        'method_name': 'getPreCompWidth',
        'method_anchors': ['iget p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->preCompWidth:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method getPreCompWidth()I
    .registers 1

    iget p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->preCompWidth:I

    return p0
.end method""",
        'replacement': """.method getPreCompWidth()I
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->preCompWidth:I

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
        'id': 'com_airbnb_lottie_model_layer_Layer__getRefId',
        'method': '.method getRefId()Ljava/lang/String;',
        'method_name': 'getRefId',
        'method_anchors': ['iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->refId:Ljava/lang/String;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method getRefId()Ljava/lang/String;
    .registers 1

    iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->refId:Ljava/lang/String;

    return-object p0
.end method""",
        'replacement': """.method getRefId()Ljava/lang/String;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->refId:Ljava/lang/String;

    goto :goto_1

    nop

    :goto_1
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_model_layer_Layer__getShapes',
        'method': '.method getShapes()Ljava/util/List;',
        'method_name': 'getShapes',
        'method_anchors': ['iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->shapes:Ljava/util/List;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method getShapes()Ljava/util/List;
    .registers 1

    iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->shapes:Ljava/util/List;

    return-object p0
.end method""",
        'replacement': """.method getShapes()Ljava/util/List;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->shapes:Ljava/util/List;

    goto :goto_1

    nop

    :goto_1
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_model_layer_Layer__getSolidColor',
        'method': '.method getSolidColor()I',
        'method_name': 'getSolidColor',
        'method_anchors': ['iget p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->solidColor:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method getSolidColor()I
    .registers 1

    iget p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->solidColor:I

    return p0
.end method""",
        'replacement': """.method getSolidColor()I
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->solidColor:I

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
        'id': 'com_airbnb_lottie_model_layer_Layer__getSolidHeight',
        'method': '.method getSolidHeight()I',
        'method_name': 'getSolidHeight',
        'method_anchors': ['iget p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->solidHeight:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method getSolidHeight()I
    .registers 1

    iget p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->solidHeight:I

    return p0
.end method""",
        'replacement': """.method getSolidHeight()I
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->solidHeight:I

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
        'id': 'com_airbnb_lottie_model_layer_Layer__getSolidWidth',
        'method': '.method getSolidWidth()I',
        'method_name': 'getSolidWidth',
        'method_anchors': ['iget p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->solidWidth:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method getSolidWidth()I
    .registers 1

    iget p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->solidWidth:I

    return p0
.end method""",
        'replacement': """.method getSolidWidth()I
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    iget p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->solidWidth:I

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_model_layer_Layer__getStartProgress',
        'method': '.method getStartProgress()F',
        'method_name': 'getStartProgress',
        'method_anchors': ['iget v0, p0, Lcom/airbnb/lottie/model/layer/Layer;->startFrame:F', 'iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->composition:Lcom/airbnb/lottie/LottieComposition;', 'invoke-virtual {p0}, Lcom/airbnb/lottie/LottieComposition;->getDurationFrames()F', 'return v0'],
        'type': 'method_replace',
        'search': """.method getStartProgress()F
    .registers 2

    iget v0, p0, Lcom/airbnb/lottie/model/layer/Layer;->startFrame:F

    iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->composition:Lcom/airbnb/lottie/LottieComposition;

    invoke-virtual {p0}, Lcom/airbnb/lottie/LottieComposition;->getDurationFrames()F

    move-result p0

    div-float/2addr v0, p0

    return v0
.end method""",
        'replacement': """.method getStartProgress()F
    .registers 2

    goto :goto_4

    nop

    :goto_0
    div-float/2addr v0, p0

    goto :goto_3

    nop

    :goto_1
    iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->composition:Lcom/airbnb/lottie/LottieComposition;

    goto :goto_2

    nop

    :goto_2
    invoke-virtual {p0}, Lcom/airbnb/lottie/LottieComposition;->getDurationFrames()F

    move-result p0

    goto :goto_0

    nop

    :goto_3
    return v0

    :goto_4
    iget v0, p0, Lcom/airbnb/lottie/model/layer/Layer;->startFrame:F

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_model_layer_Layer__getText',
        'method': '.method getText()Lcom/airbnb/lottie/model/animatable/AnimatableTextFrame;',
        'method_name': 'getText',
        'method_anchors': ['iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->text:Lcom/airbnb/lottie/model/animatable/AnimatableTextFrame;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method getText()Lcom/airbnb/lottie/model/animatable/AnimatableTextFrame;
    .registers 1

    iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->text:Lcom/airbnb/lottie/model/animatable/AnimatableTextFrame;

    return-object p0
.end method""",
        'replacement': """.method getText()Lcom/airbnb/lottie/model/animatable/AnimatableTextFrame;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->text:Lcom/airbnb/lottie/model/animatable/AnimatableTextFrame;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_model_layer_Layer__getTextProperties',
        'method': '.method getTextProperties()Lcom/airbnb/lottie/model/animatable/AnimatableTextProperties;',
        'method_name': 'getTextProperties',
        'method_anchors': ['iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->textProperties:Lcom/airbnb/lottie/model/animatable/AnimatableTextProperties;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method getTextProperties()Lcom/airbnb/lottie/model/animatable/AnimatableTextProperties;
    .registers 1

    iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->textProperties:Lcom/airbnb/lottie/model/animatable/AnimatableTextProperties;

    return-object p0
.end method""",
        'replacement': """.method getTextProperties()Lcom/airbnb/lottie/model/animatable/AnimatableTextProperties;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->textProperties:Lcom/airbnb/lottie/model/animatable/AnimatableTextProperties;

    goto :goto_1

    nop

    :goto_1
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_model_layer_Layer__getTimeRemapping',
        'method': '.method getTimeRemapping()Lcom/airbnb/lottie/model/animatable/AnimatableFloatValue;',
        'method_name': 'getTimeRemapping',
        'method_anchors': ['iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->timeRemapping:Lcom/airbnb/lottie/model/animatable/AnimatableFloatValue;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method getTimeRemapping()Lcom/airbnb/lottie/model/animatable/AnimatableFloatValue;
    .registers 1

    iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->timeRemapping:Lcom/airbnb/lottie/model/animatable/AnimatableFloatValue;

    return-object p0
.end method""",
        'replacement': """.method getTimeRemapping()Lcom/airbnb/lottie/model/animatable/AnimatableFloatValue;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->timeRemapping:Lcom/airbnb/lottie/model/animatable/AnimatableFloatValue;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_model_layer_Layer__getTimeStretch',
        'method': '.method getTimeStretch()F',
        'method_name': 'getTimeStretch',
        'method_anchors': ['iget p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->timeStretch:F', 'return p0'],
        'type': 'method_replace',
        'search': """.method getTimeStretch()F
    .registers 1

    iget p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->timeStretch:F

    return p0
.end method""",
        'replacement': """.method getTimeStretch()F
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->timeStretch:F

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
        'id': 'com_airbnb_lottie_model_layer_Layer__getTransform',
        'method': '.method getTransform()Lcom/airbnb/lottie/model/animatable/AnimatableTransform;',
        'method_name': 'getTransform',
        'method_anchors': ['iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->transform:Lcom/airbnb/lottie/model/animatable/AnimatableTransform;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method getTransform()Lcom/airbnb/lottie/model/animatable/AnimatableTransform;
    .registers 1

    iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->transform:Lcom/airbnb/lottie/model/animatable/AnimatableTransform;

    return-object p0
.end method""",
        'replacement': """.method getTransform()Lcom/airbnb/lottie/model/animatable/AnimatableTransform;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p0, Lcom/airbnb/lottie/model/layer/Layer;->transform:Lcom/airbnb/lottie/model/animatable/AnimatableTransform;

    goto :goto_1

    nop

    :goto_1
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
