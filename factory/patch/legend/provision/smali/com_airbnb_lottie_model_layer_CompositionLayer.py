TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/airbnb/lottie/model/layer/CompositionLayer.smali'
CLASS_FALLBACK_NAMES = ['CompositionLayer.smali']
CLASS_ANCHORS = ['.super Lcom/airbnb/lottie/model/layer/BaseLayer;']

PATCHES = [
    {
        'id': 'com_airbnb_lottie_model_layer_CompositionLayer__drawLayer',
        'method': '.method drawLayer(Landroid/graphics/Canvas;Landroid/graphics/Matrix;I)V',
        'method_name': 'drawLayer',
        'method_anchors': ['const-string v0, "CompositionLayer#draw"', 'invoke-static {v0}, Lcom/airbnb/lottie/L;->beginSection(Ljava/lang/String;)V', 'iget-object v1, p0, Lcom/airbnb/lottie/model/layer/CompositionLayer;->newClipRect:Landroid/graphics/RectF;', 'iget-object v2, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->layerModel:Lcom/airbnb/lottie/model/layer/Layer;', 'invoke-virtual {v2}, Lcom/airbnb/lottie/model/layer/Layer;->getPreCompWidth()I', 'iget-object v3, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->layerModel:Lcom/airbnb/lottie/model/layer/Layer;', 'invoke-virtual {v3}, Lcom/airbnb/lottie/model/layer/Layer;->getPreCompHeight()I', 'invoke-virtual {v1, v4, v4, v2, v3}, Landroid/graphics/RectF;->set(FFFF)V'],
        'type': 'method_replace',
        'search': """.method drawLayer(Landroid/graphics/Canvas;Landroid/graphics/Matrix;I)V
    .registers 10

    const-string v0, "CompositionLayer#draw"

    invoke-static {v0}, Lcom/airbnb/lottie/L;->beginSection(Ljava/lang/String;)V

    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/CompositionLayer;->newClipRect:Landroid/graphics/RectF;

    iget-object v2, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->layerModel:Lcom/airbnb/lottie/model/layer/Layer;

    invoke-virtual {v2}, Lcom/airbnb/lottie/model/layer/Layer;->getPreCompWidth()I

    move-result v2

    int-to-float v2, v2

    iget-object v3, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->layerModel:Lcom/airbnb/lottie/model/layer/Layer;

    invoke-virtual {v3}, Lcom/airbnb/lottie/model/layer/Layer;->getPreCompHeight()I

    move-result v3

    int-to-float v3, v3

    const/4 v4, 0x0

    invoke-virtual {v1, v4, v4, v2, v3}, Landroid/graphics/RectF;->set(FFFF)V

    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/CompositionLayer;->newClipRect:Landroid/graphics/RectF;

    invoke-virtual {p2, v1}, Landroid/graphics/Matrix;->mapRect(Landroid/graphics/RectF;)Z

    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->lottieDrawable:Lcom/airbnb/lottie/LottieDrawable;

    invoke-virtual {v1}, Lcom/airbnb/lottie/LottieDrawable;->isApplyingOpacityToLayersEnabled()Z

    move-result v1

    const/16 v2, 0xff

    const/4 v3, 0x1

    if-eqz v1, :cond_0

    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/CompositionLayer;->layers:Ljava/util/List;

    invoke-interface {v1}, Ljava/util/List;->size()I

    move-result v1

    if-le v1, v3, :cond_0

    if-eq p3, v2, :cond_0

    move v1, v3

    goto :goto_0

    :cond_0
    const/4 v1, 0x0

    :goto_0
    if-eqz v1, :cond_1

    iget-object v4, p0, Lcom/airbnb/lottie/model/layer/CompositionLayer;->layerPaint:Landroid/graphics/Paint;

    invoke-virtual {v4, p3}, Landroid/graphics/Paint;->setAlpha(I)V

    iget-object v4, p0, Lcom/airbnb/lottie/model/layer/CompositionLayer;->newClipRect:Landroid/graphics/RectF;

    iget-object v5, p0, Lcom/airbnb/lottie/model/layer/CompositionLayer;->layerPaint:Landroid/graphics/Paint;

    invoke-static {p1, v4, v5}, Lcom/airbnb/lottie/utils/Utils;->saveLayerCompat(Landroid/graphics/Canvas;Landroid/graphics/RectF;Landroid/graphics/Paint;)V

    goto :goto_1

    :cond_1
    invoke-virtual {p1}, Landroid/graphics/Canvas;->save()I

    :goto_1
    if-eqz v1, :cond_2

    move p3, v2

    :cond_2
    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/CompositionLayer;->layers:Ljava/util/List;

    invoke-interface {v1}, Ljava/util/List;->size()I

    move-result v1

    sub-int/2addr v1, v3

    :goto_2
    if-ltz v1, :cond_6

    iget-boolean v2, p0, Lcom/airbnb/lottie/model/layer/CompositionLayer;->clipToCompositionBounds:Z

    if-nez v2, :cond_3

    iget-object v2, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->layerModel:Lcom/airbnb/lottie/model/layer/Layer;

    invoke-virtual {v2}, Lcom/airbnb/lottie/model/layer/Layer;->getName()Ljava/lang/String;

    move-result-object v2

    const-string v4, "__container"

    invoke-virtual {v4, v2}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v2

    if-eqz v2, :cond_3

    goto :goto_3

    :cond_3
    iget-object v2, p0, Lcom/airbnb/lottie/model/layer/CompositionLayer;->newClipRect:Landroid/graphics/RectF;

    invoke-virtual {v2}, Landroid/graphics/RectF;->isEmpty()Z

    move-result v2

    if-nez v2, :cond_4

    iget-object v2, p0, Lcom/airbnb/lottie/model/layer/CompositionLayer;->newClipRect:Landroid/graphics/RectF;

    invoke-virtual {p1, v2}, Landroid/graphics/Canvas;->clipRect(Landroid/graphics/RectF;)Z

    move-result v2

    goto :goto_4

    :cond_4
    :goto_3
    move v2, v3

    :goto_4
    if-eqz v2, :cond_5

    iget-object v2, p0, Lcom/airbnb/lottie/model/layer/CompositionLayer;->layers:Ljava/util/List;

    invoke-interface {v2, v1}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v2

    check-cast v2, Lcom/airbnb/lottie/model/layer/BaseLayer;

    invoke-virtual {v2, p1, p2, p3}, Lcom/airbnb/lottie/model/layer/BaseLayer;->draw(Landroid/graphics/Canvas;Landroid/graphics/Matrix;I)V

    :cond_5
    add-int/lit8 v1, v1, -0x1

    goto :goto_2

    :cond_6
    invoke-virtual {p1}, Landroid/graphics/Canvas;->restore()V

    invoke-static {v0}, Lcom/airbnb/lottie/L;->endSection(Ljava/lang/String;)F

    return-void
.end method""",
        'replacement': """.method drawLayer(Landroid/graphics/Canvas;Landroid/graphics/Matrix;I)V
    .registers 10

    goto :goto_14

    nop

    :goto_0
    invoke-virtual {p1, v2}, Landroid/graphics/Canvas;->clipRect(Landroid/graphics/RectF;)Z

    move-result v2

    goto :goto_2

    nop

    :goto_1
    if-nez v2, :cond_0

    goto :goto_21

    :cond_0
    goto :goto_1a

    nop

    :goto_2
    goto :goto_12

    :goto_3
    goto :goto_11

    nop

    :goto_4
    if-nez v1, :cond_1

    goto :goto_44

    :cond_1
    goto :goto_2d

    nop

    :goto_5
    const/4 v4, 0x0

    goto :goto_37

    nop

    :goto_6
    if-nez v2, :cond_2

    goto :goto_29

    :cond_2
    goto :goto_28

    nop

    :goto_7
    return-void

    :goto_8
    move v1, v3

    goto :goto_43

    nop

    :goto_9
    sub-int/2addr v1, v3

    :goto_a
    goto :goto_40

    nop

    :goto_b
    add-int/lit8 v1, v1, -0x1

    goto :goto_31

    nop

    :goto_c
    iget-object v4, p0, Lcom/airbnb/lottie/model/layer/CompositionLayer;->layerPaint:Landroid/graphics/Paint;

    goto :goto_16

    nop

    :goto_d
    iget-object v3, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->layerModel:Lcom/airbnb/lottie/model/layer/Layer;

    goto :goto_23

    nop

    :goto_e
    if-nez v1, :cond_3

    goto :goto_27

    :cond_3
    goto :goto_26

    nop

    :goto_f
    iget-boolean v2, p0, Lcom/airbnb/lottie/model/layer/CompositionLayer;->clipToCompositionBounds:Z

    goto :goto_48

    nop

    :goto_10
    if-eqz v2, :cond_4

    goto :goto_3

    :cond_4
    goto :goto_3f

    nop

    :goto_11
    move v2, v3

    :goto_12
    goto :goto_1

    nop

    :goto_13
    invoke-static {v0}, Lcom/airbnb/lottie/L;->endSection(Ljava/lang/String;)F

    goto :goto_7

    nop

    :goto_14
    const-string v0, "CompositionLayer#draw"

    goto :goto_42

    nop

    :goto_15
    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/CompositionLayer;->newClipRect:Landroid/graphics/RectF;

    goto :goto_1c

    nop

    :goto_16
    invoke-virtual {v4, p3}, Landroid/graphics/Paint;->setAlpha(I)V

    goto :goto_24

    nop

    :goto_17
    invoke-virtual {v2}, Lcom/airbnb/lottie/model/layer/Layer;->getName()Ljava/lang/String;

    move-result-object v2

    goto :goto_46

    nop

    :goto_18
    goto :goto_3a

    :goto_19
    goto :goto_39

    nop

    :goto_1a
    iget-object v2, p0, Lcom/airbnb/lottie/model/layer/CompositionLayer;->layers:Ljava/util/List;

    goto :goto_2b

    nop

    :goto_1b
    invoke-interface {v1}, Ljava/util/List;->size()I

    move-result v1

    goto :goto_2f

    nop

    :goto_1c
    iget-object v2, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->layerModel:Lcom/airbnb/lottie/model/layer/Layer;

    goto :goto_2c

    nop

    :goto_1d
    invoke-virtual {p1}, Landroid/graphics/Canvas;->restore()V

    goto :goto_13

    nop

    :goto_1e
    const/4 v3, 0x1

    goto :goto_4

    nop

    :goto_1f
    invoke-virtual {v1}, Lcom/airbnb/lottie/LottieDrawable;->isApplyingOpacityToLayersEnabled()Z

    move-result v1

    goto :goto_34

    nop

    :goto_20
    invoke-virtual {v2, p1, p2, p3}, Lcom/airbnb/lottie/model/layer/BaseLayer;->draw(Landroid/graphics/Canvas;Landroid/graphics/Matrix;I)V

    :goto_21
    goto :goto_b

    nop

    :goto_22
    if-nez v1, :cond_5

    goto :goto_19

    :cond_5
    goto :goto_c

    nop

    :goto_23
    invoke-virtual {v3}, Lcom/airbnb/lottie/model/layer/Layer;->getPreCompHeight()I

    move-result v3

    goto :goto_2e

    nop

    :goto_24
    iget-object v4, p0, Lcom/airbnb/lottie/model/layer/CompositionLayer;->newClipRect:Landroid/graphics/RectF;

    goto :goto_36

    nop

    :goto_25
    invoke-virtual {v4, v2}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v2

    goto :goto_6

    nop

    :goto_26
    move p3, v2

    :goto_27
    goto :goto_3b

    nop

    :goto_28
    goto :goto_3

    :goto_29
    goto :goto_41

    nop

    :goto_2a
    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->lottieDrawable:Lcom/airbnb/lottie/LottieDrawable;

    goto :goto_1f

    nop

    :goto_2b
    invoke-interface {v2, v1}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v2

    goto :goto_35

    nop

    :goto_2c
    invoke-virtual {v2}, Lcom/airbnb/lottie/model/layer/Layer;->getPreCompWidth()I

    move-result v2

    goto :goto_45

    nop

    :goto_2d
    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/CompositionLayer;->layers:Ljava/util/List;

    goto :goto_1b

    nop

    :goto_2e
    int-to-float v3, v3

    goto :goto_5

    nop

    :goto_2f
    if-gt v1, v3, :cond_6

    goto :goto_44

    :cond_6
    goto :goto_4a

    nop

    :goto_30
    invoke-virtual {v2}, Landroid/graphics/RectF;->isEmpty()Z

    move-result v2

    goto :goto_10

    nop

    :goto_31
    goto :goto_a

    :goto_32
    goto :goto_1d

    nop

    :goto_33
    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/CompositionLayer;->newClipRect:Landroid/graphics/RectF;

    goto :goto_38

    nop

    :goto_34
    const/16 v2, 0xff

    goto :goto_1e

    nop

    :goto_35
    check-cast v2, Lcom/airbnb/lottie/model/layer/BaseLayer;

    goto :goto_20

    nop

    :goto_36
    iget-object v5, p0, Lcom/airbnb/lottie/model/layer/CompositionLayer;->layerPaint:Landroid/graphics/Paint;

    goto :goto_47

    nop

    :goto_37
    invoke-virtual {v1, v4, v4, v2, v3}, Landroid/graphics/RectF;->set(FFFF)V

    goto :goto_33

    nop

    :goto_38
    invoke-virtual {p2, v1}, Landroid/graphics/Matrix;->mapRect(Landroid/graphics/RectF;)Z

    goto :goto_2a

    nop

    :goto_39
    invoke-virtual {p1}, Landroid/graphics/Canvas;->save()I

    :goto_3a
    goto :goto_e

    nop

    :goto_3b
    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/CompositionLayer;->layers:Ljava/util/List;

    goto :goto_49

    nop

    :goto_3c
    const/4 v1, 0x0

    :goto_3d
    goto :goto_22

    nop

    :goto_3e
    iget-object v2, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->layerModel:Lcom/airbnb/lottie/model/layer/Layer;

    goto :goto_17

    nop

    :goto_3f
    iget-object v2, p0, Lcom/airbnb/lottie/model/layer/CompositionLayer;->newClipRect:Landroid/graphics/RectF;

    goto :goto_0

    nop

    :goto_40
    if-gez v1, :cond_7

    goto :goto_32

    :cond_7
    goto :goto_f

    nop

    :goto_41
    iget-object v2, p0, Lcom/airbnb/lottie/model/layer/CompositionLayer;->newClipRect:Landroid/graphics/RectF;

    goto :goto_30

    nop

    :goto_42
    invoke-static {v0}, Lcom/airbnb/lottie/L;->beginSection(Ljava/lang/String;)V

    goto :goto_15

    nop

    :goto_43
    goto :goto_3d

    :goto_44
    goto :goto_3c

    nop

    :goto_45
    int-to-float v2, v2

    goto :goto_d

    nop

    :goto_46
    const-string v4, "__container"

    goto :goto_25

    nop

    :goto_47
    invoke-static {p1, v4, v5}, Lcom/airbnb/lottie/utils/Utils;->saveLayerCompat(Landroid/graphics/Canvas;Landroid/graphics/RectF;Landroid/graphics/Paint;)V

    goto :goto_18

    nop

    :goto_48
    if-eqz v2, :cond_8

    goto :goto_29

    :cond_8
    goto :goto_3e

    nop

    :goto_49
    invoke-interface {v1}, Ljava/util/List;->size()I

    move-result v1

    goto :goto_9

    nop

    :goto_4a
    if-ne p3, v2, :cond_9

    goto :goto_44

    :cond_9
    goto :goto_8

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_model_layer_CompositionLayer__resolveChildKeyPath',
        'method': '.method protected resolveChildKeyPath(Lcom/airbnb/lottie/model/KeyPath;ILjava/util/List;Lcom/airbnb/lottie/model/KeyPath;)V',
        'method_name': 'resolveChildKeyPath',
        'method_anchors': ['iget-object v1, p0, Lcom/airbnb/lottie/model/layer/CompositionLayer;->layers:Ljava/util/List;', 'invoke-interface {v1}, Ljava/util/List;->size()I', 'if-ge v0, v1, :cond_0', 'iget-object v1, p0, Lcom/airbnb/lottie/model/layer/CompositionLayer;->layers:Ljava/util/List;', 'invoke-interface {v1, v0}, Ljava/util/List;->get(I)Ljava/lang/Object;', 'check-cast v1, Lcom/airbnb/lottie/model/layer/BaseLayer;', 'invoke-virtual {v1, p1, p2, p3, p4}, Lcom/airbnb/lottie/model/layer/BaseLayer;->resolveKeyPath(Lcom/airbnb/lottie/model/KeyPath;ILjava/util/List;Lcom/airbnb/lottie/model/KeyPath;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected resolveChildKeyPath(Lcom/airbnb/lottie/model/KeyPath;ILjava/util/List;Lcom/airbnb/lottie/model/KeyPath;)V
    .registers 7

    const/4 v0, 0x0

    :goto_0
    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/CompositionLayer;->layers:Ljava/util/List;

    invoke-interface {v1}, Ljava/util/List;->size()I

    move-result v1

    if-ge v0, v1, :cond_0

    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/CompositionLayer;->layers:Ljava/util/List;

    invoke-interface {v1, v0}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/airbnb/lottie/model/layer/BaseLayer;

    invoke-virtual {v1, p1, p2, p3, p4}, Lcom/airbnb/lottie/model/layer/BaseLayer;->resolveKeyPath(Lcom/airbnb/lottie/model/KeyPath;ILjava/util/List;Lcom/airbnb/lottie/model/KeyPath;)V

    add-int/lit8 v0, v0, 0x1

    goto :goto_0

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected resolveChildKeyPath(Lcom/airbnb/lottie/model/KeyPath;ILjava/util/List;Lcom/airbnb/lottie/model/KeyPath;)V
    .registers 7

    goto :goto_b

    nop

    :goto_0
    add-int/lit8 v0, v0, 0x1

    goto :goto_4

    nop

    :goto_1
    invoke-virtual {v1, p1, p2, p3, p4}, Lcom/airbnb/lottie/model/layer/BaseLayer;->resolveKeyPath(Lcom/airbnb/lottie/model/KeyPath;ILjava/util/List;Lcom/airbnb/lottie/model/KeyPath;)V

    goto :goto_0

    nop

    :goto_2
    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/CompositionLayer;->layers:Ljava/util/List;

    goto :goto_7

    nop

    :goto_3
    invoke-interface {v1, v0}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v1

    goto :goto_9

    nop

    :goto_4
    goto :goto_c

    :goto_5
    goto :goto_8

    nop

    :goto_6
    if-lt v0, v1, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_a

    nop

    :goto_7
    invoke-interface {v1}, Ljava/util/List;->size()I

    move-result v1

    goto :goto_6

    nop

    :goto_8
    return-void

    :goto_9
    check-cast v1, Lcom/airbnb/lottie/model/layer/BaseLayer;

    goto :goto_1

    nop

    :goto_a
    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/CompositionLayer;->layers:Ljava/util/List;

    goto :goto_3

    nop

    :goto_b
    const/4 v0, 0x0

    :goto_c
    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
