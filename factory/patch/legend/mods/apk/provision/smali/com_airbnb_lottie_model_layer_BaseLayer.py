TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/airbnb/lottie/model/layer/BaseLayer.smali'
CLASS_FALLBACK_NAMES = ['BaseLayer.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Lcom/airbnb/lottie/animation/content/DrawingContent;', '.implements Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation$AnimationListener;', '.implements Lcom/airbnb/lottie/model/KeyPathElement;']

PATCHES = [
    {
        'id': 'com_airbnb_lottie_model_layer_BaseLayer__getLayerModel',
        'method': '.method getLayerModel()Lcom/airbnb/lottie/model/layer/Layer;',
        'method_name': 'getLayerModel',
        'method_anchors': ['iget-object p0, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->layerModel:Lcom/airbnb/lottie/model/layer/Layer;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method getLayerModel()Lcom/airbnb/lottie/model/layer/Layer;
    .registers 1

    iget-object p0, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->layerModel:Lcom/airbnb/lottie/model/layer/Layer;

    return-object p0
.end method""",
        'replacement': """.method getLayerModel()Lcom/airbnb/lottie/model/layer/Layer;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->layerModel:Lcom/airbnb/lottie/model/layer/Layer;

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
        'id': 'com_airbnb_lottie_model_layer_BaseLayer__hasMasksOnThisLayer',
        'method': '.method hasMasksOnThisLayer()Z',
        'method_name': 'hasMasksOnThisLayer',
        'method_anchors': ['iget-object p0, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->mask:Lcom/airbnb/lottie/animation/keyframe/MaskKeyframeAnimation;', 'if-eqz p0, :cond_0', 'invoke-virtual {p0}, Lcom/airbnb/lottie/animation/keyframe/MaskKeyframeAnimation;->getMaskAnimations()Ljava/util/List;', 'invoke-interface {p0}, Ljava/util/List;->isEmpty()Z', 'if-nez p0, :cond_0', 'return p0', 'return p0'],
        'type': 'method_replace',
        'search': """.method hasMasksOnThisLayer()Z
    .registers 1

    iget-object p0, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->mask:Lcom/airbnb/lottie/animation/keyframe/MaskKeyframeAnimation;

    if-eqz p0, :cond_0

    invoke-virtual {p0}, Lcom/airbnb/lottie/animation/keyframe/MaskKeyframeAnimation;->getMaskAnimations()Ljava/util/List;

    move-result-object p0

    invoke-interface {p0}, Ljava/util/List;->isEmpty()Z

    move-result p0

    if-nez p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method hasMasksOnThisLayer()Z
    .registers 1

    goto :goto_5

    nop

    :goto_0
    return p0

    :goto_1
    goto :goto_9

    nop

    :goto_2
    invoke-virtual {p0}, Lcom/airbnb/lottie/animation/keyframe/MaskKeyframeAnimation;->getMaskAnimations()Ljava/util/List;

    move-result-object p0

    goto :goto_7

    nop

    :goto_3
    if-eqz p0, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_4

    nop

    :goto_4
    const/4 p0, 0x1

    goto :goto_0

    nop

    :goto_5
    iget-object p0, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->mask:Lcom/airbnb/lottie/animation/keyframe/MaskKeyframeAnimation;

    goto :goto_8

    nop

    :goto_6
    return p0

    :goto_7
    invoke-interface {p0}, Ljava/util/List;->isEmpty()Z

    move-result p0

    goto :goto_3

    nop

    :goto_8
    if-nez p0, :cond_1

    goto :goto_1

    :cond_1
    goto :goto_2

    nop

    :goto_9
    const/4 p0, 0x0

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_model_layer_BaseLayer__hasMatteOnThisLayer',
        'method': '.method hasMatteOnThisLayer()Z',
        'method_name': 'hasMatteOnThisLayer',
        'method_anchors': ['iget-object p0, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->matteLayer:Lcom/airbnb/lottie/model/layer/BaseLayer;', 'if-eqz p0, :cond_0', 'return p0', 'return p0'],
        'type': 'method_replace',
        'search': """.method hasMatteOnThisLayer()Z
    .registers 1

    iget-object p0, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->matteLayer:Lcom/airbnb/lottie/model/layer/BaseLayer;

    if-eqz p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method hasMatteOnThisLayer()Z
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->matteLayer:Lcom/airbnb/lottie/model/layer/BaseLayer;

    goto :goto_6

    nop

    :goto_1
    const/4 p0, 0x1

    goto :goto_2

    nop

    :goto_2
    return p0

    :goto_3
    goto :goto_5

    nop

    :goto_4
    return p0

    :goto_5
    const/4 p0, 0x0

    goto :goto_4

    nop

    :goto_6
    if-nez p0, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_model_layer_BaseLayer__resolveChildKeyPath',
        'method': '.method resolveChildKeyPath(Lcom/airbnb/lottie/model/KeyPath;ILjava/util/List;Lcom/airbnb/lottie/model/KeyPath;)V',
        'method_name': 'resolveChildKeyPath',
        'method_anchors': ['return-void'],
        'type': 'method_replace',
        'search': """.method resolveChildKeyPath(Lcom/airbnb/lottie/model/KeyPath;ILjava/util/List;Lcom/airbnb/lottie/model/KeyPath;)V
    .registers 5

    return-void
.end method""",
        'replacement': """.method resolveChildKeyPath(Lcom/airbnb/lottie/model/KeyPath;ILjava/util/List;Lcom/airbnb/lottie/model/KeyPath;)V
    .registers 5

    goto :goto_0

    nop

    :goto_0
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_model_layer_BaseLayer__setMatteLayer',
        'method': '.method setMatteLayer(Lcom/airbnb/lottie/model/layer/BaseLayer;)V',
        'method_name': 'setMatteLayer',
        'method_anchors': ['iput-object p1, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->matteLayer:Lcom/airbnb/lottie/model/layer/BaseLayer;', 'return-void'],
        'type': 'method_replace',
        'search': """.method setMatteLayer(Lcom/airbnb/lottie/model/layer/BaseLayer;)V
    .registers 2

    iput-object p1, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->matteLayer:Lcom/airbnb/lottie/model/layer/BaseLayer;

    return-void
.end method""",
        'replacement': """.method setMatteLayer(Lcom/airbnb/lottie/model/layer/BaseLayer;)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    iput-object p1, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->matteLayer:Lcom/airbnb/lottie/model/layer/BaseLayer;

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
        'id': 'com_airbnb_lottie_model_layer_BaseLayer__setOutlineMasksAndMattes',
        'method': '.method setOutlineMasksAndMattes(Z)V',
        'method_name': 'setOutlineMasksAndMattes',
        'method_anchors': ['if-eqz p1, :cond_0', 'iget-object v0, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->outlineMasksAndMattesPaint:Landroid/graphics/Paint;', 'if-nez v0, :cond_0', 'new-instance v0, Lcom/airbnb/lottie/animation/LPaint;', 'invoke-direct {v0}, Lcom/airbnb/lottie/animation/LPaint;-><init>()V', 'iput-object v0, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->outlineMasksAndMattesPaint:Landroid/graphics/Paint;', 'iput-boolean p1, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->outlineMasksAndMattes:Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method setOutlineMasksAndMattes(Z)V
    .registers 3

    if-eqz p1, :cond_0

    iget-object v0, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->outlineMasksAndMattesPaint:Landroid/graphics/Paint;

    if-nez v0, :cond_0

    new-instance v0, Lcom/airbnb/lottie/animation/LPaint;

    invoke-direct {v0}, Lcom/airbnb/lottie/animation/LPaint;-><init>()V

    iput-object v0, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->outlineMasksAndMattesPaint:Landroid/graphics/Paint;

    :cond_0
    iput-boolean p1, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->outlineMasksAndMattes:Z

    return-void
.end method""",
        'replacement': """.method setOutlineMasksAndMattes(Z)V
    .registers 3

    goto :goto_5

    nop

    :goto_0
    iput-boolean p1, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->outlineMasksAndMattes:Z

    goto :goto_4

    nop

    :goto_1
    if-eqz v0, :cond_0

    goto :goto_7

    :cond_0
    goto :goto_3

    nop

    :goto_2
    iget-object v0, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->outlineMasksAndMattesPaint:Landroid/graphics/Paint;

    goto :goto_1

    nop

    :goto_3
    new-instance v0, Lcom/airbnb/lottie/animation/LPaint;

    goto :goto_8

    nop

    :goto_4
    return-void

    :goto_5
    if-nez p1, :cond_1

    goto :goto_7

    :cond_1
    goto :goto_2

    nop

    :goto_6
    iput-object v0, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->outlineMasksAndMattesPaint:Landroid/graphics/Paint;

    :goto_7
    goto :goto_0

    nop

    :goto_8
    invoke-direct {v0}, Lcom/airbnb/lottie/animation/LPaint;-><init>()V

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_model_layer_BaseLayer__setParentLayer',
        'method': '.method setParentLayer(Lcom/airbnb/lottie/model/layer/BaseLayer;)V',
        'method_name': 'setParentLayer',
        'method_anchors': ['iput-object p1, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->parentLayer:Lcom/airbnb/lottie/model/layer/BaseLayer;', 'return-void'],
        'type': 'method_replace',
        'search': """.method setParentLayer(Lcom/airbnb/lottie/model/layer/BaseLayer;)V
    .registers 2

    iput-object p1, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->parentLayer:Lcom/airbnb/lottie/model/layer/BaseLayer;

    return-void
.end method""",
        'replacement': """.method setParentLayer(Lcom/airbnb/lottie/model/layer/BaseLayer;)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    iput-object p1, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->parentLayer:Lcom/airbnb/lottie/model/layer/BaseLayer;

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
        'id': 'com_airbnb_lottie_model_layer_BaseLayer__setProgress',
        'method': '.method setProgress(F)V',
        'method_name': 'setProgress',
        'method_anchors': ['iget-object v0, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->transform:Lcom/airbnb/lottie/animation/keyframe/TransformKeyframeAnimation;', 'invoke-virtual {v0, p1}, Lcom/airbnb/lottie/animation/keyframe/TransformKeyframeAnimation;->setProgress(F)V', 'iget-object v0, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->mask:Lcom/airbnb/lottie/animation/keyframe/MaskKeyframeAnimation;', 'if-eqz v0, :cond_0', 'iget-object v2, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->mask:Lcom/airbnb/lottie/animation/keyframe/MaskKeyframeAnimation;', 'invoke-virtual {v2}, Lcom/airbnb/lottie/animation/keyframe/MaskKeyframeAnimation;->getMaskAnimations()Ljava/util/List;', 'invoke-interface {v2}, Ljava/util/List;->size()I', 'if-ge v0, v2, :cond_0'],
        'type': 'method_replace',
        'search': """.method setProgress(F)V
    .registers 5

    iget-object v0, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->transform:Lcom/airbnb/lottie/animation/keyframe/TransformKeyframeAnimation;

    invoke-virtual {v0, p1}, Lcom/airbnb/lottie/animation/keyframe/TransformKeyframeAnimation;->setProgress(F)V

    iget-object v0, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->mask:Lcom/airbnb/lottie/animation/keyframe/MaskKeyframeAnimation;

    const/4 v1, 0x0

    if-eqz v0, :cond_0

    move v0, v1

    :goto_0
    iget-object v2, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->mask:Lcom/airbnb/lottie/animation/keyframe/MaskKeyframeAnimation;

    invoke-virtual {v2}, Lcom/airbnb/lottie/animation/keyframe/MaskKeyframeAnimation;->getMaskAnimations()Ljava/util/List;

    move-result-object v2

    invoke-interface {v2}, Ljava/util/List;->size()I

    move-result v2

    if-ge v0, v2, :cond_0

    iget-object v2, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->mask:Lcom/airbnb/lottie/animation/keyframe/MaskKeyframeAnimation;

    invoke-virtual {v2}, Lcom/airbnb/lottie/animation/keyframe/MaskKeyframeAnimation;->getMaskAnimations()Ljava/util/List;

    move-result-object v2

    invoke-interface {v2, v0}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v2

    check-cast v2, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;

    invoke-virtual {v2, p1}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->setProgress(F)V

    add-int/lit8 v0, v0, 0x1

    goto :goto_0

    :cond_0
    iget-object v0, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->inOutAnimation:Lcom/airbnb/lottie/animation/keyframe/FloatKeyframeAnimation;

    if-eqz v0, :cond_1

    invoke-virtual {v0, p1}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->setProgress(F)V

    :cond_1
    iget-object v0, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->matteLayer:Lcom/airbnb/lottie/model/layer/BaseLayer;

    if-eqz v0, :cond_2

    invoke-virtual {v0, p1}, Lcom/airbnb/lottie/model/layer/BaseLayer;->setProgress(F)V

    :cond_2
    :goto_1
    iget-object v0, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->animations:Ljava/util/List;

    invoke-interface {v0}, Ljava/util/List;->size()I

    move-result v0

    if-ge v1, v0, :cond_3

    iget-object v0, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->animations:Ljava/util/List;

    invoke-interface {v0, v1}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;

    invoke-virtual {v0, p1}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->setProgress(F)V

    add-int/lit8 v1, v1, 0x1

    goto :goto_1

    :cond_3
    return-void
.end method""",
        'replacement': """.method setProgress(F)V
    .registers 5

    goto :goto_1e

    nop

    :goto_0
    invoke-interface {v2}, Ljava/util/List;->size()I

    move-result v2

    goto :goto_1d

    nop

    :goto_1
    goto :goto_4

    :goto_2
    goto :goto_16

    nop

    :goto_3
    invoke-virtual {v0, p1}, Lcom/airbnb/lottie/model/layer/BaseLayer;->setProgress(F)V

    :goto_4
    goto :goto_14

    nop

    :goto_5
    goto :goto_11

    :goto_6
    goto :goto_8

    nop

    :goto_7
    invoke-interface {v0, v1}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v0

    goto :goto_c

    nop

    :goto_8
    iget-object v0, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->inOutAnimation:Lcom/airbnb/lottie/animation/keyframe/FloatKeyframeAnimation;

    goto :goto_1a

    nop

    :goto_9
    iget-object v2, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->mask:Lcom/airbnb/lottie/animation/keyframe/MaskKeyframeAnimation;

    goto :goto_d

    nop

    :goto_a
    iget-object v0, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->matteLayer:Lcom/airbnb/lottie/model/layer/BaseLayer;

    goto :goto_17

    nop

    :goto_b
    add-int/lit8 v0, v0, 0x1

    goto :goto_5

    nop

    :goto_c
    check-cast v0, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;

    goto :goto_20

    nop

    :goto_d
    invoke-virtual {v2}, Lcom/airbnb/lottie/animation/keyframe/MaskKeyframeAnimation;->getMaskAnimations()Ljava/util/List;

    move-result-object v2

    goto :goto_19

    nop

    :goto_e
    invoke-virtual {v2}, Lcom/airbnb/lottie/animation/keyframe/MaskKeyframeAnimation;->getMaskAnimations()Ljava/util/List;

    move-result-object v2

    goto :goto_0

    nop

    :goto_f
    iget-object v0, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->mask:Lcom/airbnb/lottie/animation/keyframe/MaskKeyframeAnimation;

    goto :goto_1b

    nop

    :goto_10
    move v0, v1

    :goto_11
    goto :goto_24

    nop

    :goto_12
    invoke-virtual {v0, p1}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->setProgress(F)V

    :goto_13
    goto :goto_a

    nop

    :goto_14
    iget-object v0, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->animations:Ljava/util/List;

    goto :goto_25

    nop

    :goto_15
    invoke-virtual {v0, p1}, Lcom/airbnb/lottie/animation/keyframe/TransformKeyframeAnimation;->setProgress(F)V

    goto :goto_f

    nop

    :goto_16
    return-void

    :goto_17
    if-nez v0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_3

    nop

    :goto_18
    if-lt v1, v0, :cond_1

    goto :goto_2

    :cond_1
    goto :goto_21

    nop

    :goto_19
    invoke-interface {v2, v0}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v2

    goto :goto_22

    nop

    :goto_1a
    if-nez v0, :cond_2

    goto :goto_13

    :cond_2
    goto :goto_12

    nop

    :goto_1b
    const/4 v1, 0x0

    goto :goto_1f

    nop

    :goto_1c
    add-int/lit8 v1, v1, 0x1

    goto :goto_1

    nop

    :goto_1d
    if-lt v0, v2, :cond_3

    goto :goto_6

    :cond_3
    goto :goto_9

    nop

    :goto_1e
    iget-object v0, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->transform:Lcom/airbnb/lottie/animation/keyframe/TransformKeyframeAnimation;

    goto :goto_15

    nop

    :goto_1f
    if-nez v0, :cond_4

    goto :goto_6

    :cond_4
    goto :goto_10

    nop

    :goto_20
    invoke-virtual {v0, p1}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->setProgress(F)V

    goto :goto_1c

    nop

    :goto_21
    iget-object v0, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->animations:Ljava/util/List;

    goto :goto_7

    nop

    :goto_22
    check-cast v2, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;

    goto :goto_23

    nop

    :goto_23
    invoke-virtual {v2, p1}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->setProgress(F)V

    goto :goto_b

    nop

    :goto_24
    iget-object v2, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->mask:Lcom/airbnb/lottie/animation/keyframe/MaskKeyframeAnimation;

    goto :goto_e

    nop

    :goto_25
    invoke-interface {v0}, Ljava/util/List;->size()I

    move-result v0

    goto :goto_18

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
