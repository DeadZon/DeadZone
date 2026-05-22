TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/airbnb/lottie/animation/content/ContentGroup.smali'
CLASS_FALLBACK_NAMES = ['ContentGroup.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Lcom/airbnb/lottie/animation/content/DrawingContent;', '.implements Lcom/airbnb/lottie/animation/content/PathContent;', '.implements Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation$AnimationListener;', '.implements Lcom/airbnb/lottie/model/KeyPathElement;']

PATCHES = [
    {
        'id': 'com_airbnb_lottie_animation_content_ContentGroup__getPathList',
        'method': '.method getPathList()Ljava/util/List;',
        'method_name': 'getPathList',
        'method_anchors': ['iget-object v0, p0, Lcom/airbnb/lottie/animation/content/ContentGroup;->pathContents:Ljava/util/List;', 'if-nez v0, :cond_1', 'new-instance v0, Ljava/util/ArrayList;', 'invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V', 'iput-object v0, p0, Lcom/airbnb/lottie/animation/content/ContentGroup;->pathContents:Ljava/util/List;', 'iget-object v1, p0, Lcom/airbnb/lottie/animation/content/ContentGroup;->contents:Ljava/util/List;', 'invoke-interface {v1}, Ljava/util/List;->size()I', 'if-ge v0, v1, :cond_1'],
        'type': 'method_replace',
        'search': """.method getPathList()Ljava/util/List;
    .registers 4

    iget-object v0, p0, Lcom/airbnb/lottie/animation/content/ContentGroup;->pathContents:Ljava/util/List;

    if-nez v0, :cond_1

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/airbnb/lottie/animation/content/ContentGroup;->pathContents:Ljava/util/List;

    const/4 v0, 0x0

    :goto_0
    iget-object v1, p0, Lcom/airbnb/lottie/animation/content/ContentGroup;->contents:Ljava/util/List;

    invoke-interface {v1}, Ljava/util/List;->size()I

    move-result v1

    if-ge v0, v1, :cond_1

    iget-object v1, p0, Lcom/airbnb/lottie/animation/content/ContentGroup;->contents:Ljava/util/List;

    invoke-interface {v1, v0}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/airbnb/lottie/animation/content/Content;

    instance-of v2, v1, Lcom/airbnb/lottie/animation/content/PathContent;

    if-eqz v2, :cond_0

    iget-object v2, p0, Lcom/airbnb/lottie/animation/content/ContentGroup;->pathContents:Ljava/util/List;

    check-cast v1, Lcom/airbnb/lottie/animation/content/PathContent;

    invoke-interface {v2, v1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    :cond_0
    add-int/lit8 v0, v0, 0x1

    goto :goto_0

    :cond_1
    iget-object p0, p0, Lcom/airbnb/lottie/animation/content/ContentGroup;->pathContents:Ljava/util/List;

    return-object p0
.end method""",
        'replacement': """.method getPathList()Ljava/util/List;
    .registers 4

    goto :goto_11

    nop

    :goto_0
    iget-object v2, p0, Lcom/airbnb/lottie/animation/content/ContentGroup;->pathContents:Ljava/util/List;

    goto :goto_14

    nop

    :goto_1
    if-lt v0, v1, :cond_0

    goto :goto_a

    :cond_0
    goto :goto_15

    nop

    :goto_2
    invoke-interface {v2, v1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    :goto_3
    goto :goto_10

    nop

    :goto_4
    check-cast v1, Lcom/airbnb/lottie/animation/content/Content;

    goto :goto_8

    nop

    :goto_5
    const/4 v0, 0x0

    :goto_6
    goto :goto_13

    nop

    :goto_7
    return-object p0

    :goto_8
    instance-of v2, v1, Lcom/airbnb/lottie/animation/content/PathContent;

    goto :goto_17

    nop

    :goto_9
    goto :goto_6

    :goto_a
    goto :goto_f

    nop

    :goto_b
    invoke-interface {v1}, Ljava/util/List;->size()I

    move-result v1

    goto :goto_1

    nop

    :goto_c
    if-eqz v0, :cond_1

    goto :goto_a

    :cond_1
    goto :goto_16

    nop

    :goto_d
    iput-object v0, p0, Lcom/airbnb/lottie/animation/content/ContentGroup;->pathContents:Ljava/util/List;

    goto :goto_5

    nop

    :goto_e
    invoke-interface {v1, v0}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v1

    goto :goto_4

    nop

    :goto_f
    iget-object p0, p0, Lcom/airbnb/lottie/animation/content/ContentGroup;->pathContents:Ljava/util/List;

    goto :goto_7

    nop

    :goto_10
    add-int/lit8 v0, v0, 0x1

    goto :goto_9

    nop

    :goto_11
    iget-object v0, p0, Lcom/airbnb/lottie/animation/content/ContentGroup;->pathContents:Ljava/util/List;

    goto :goto_c

    nop

    :goto_12
    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    goto :goto_d

    nop

    :goto_13
    iget-object v1, p0, Lcom/airbnb/lottie/animation/content/ContentGroup;->contents:Ljava/util/List;

    goto :goto_b

    nop

    :goto_14
    check-cast v1, Lcom/airbnb/lottie/animation/content/PathContent;

    goto :goto_2

    nop

    :goto_15
    iget-object v1, p0, Lcom/airbnb/lottie/animation/content/ContentGroup;->contents:Ljava/util/List;

    goto :goto_e

    nop

    :goto_16
    new-instance v0, Ljava/util/ArrayList;

    goto :goto_12

    nop

    :goto_17
    if-nez v2, :cond_2

    goto :goto_3

    :cond_2
    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_animation_content_ContentGroup__getTransformationMatrix',
        'method': '.method getTransformationMatrix()Landroid/graphics/Matrix;',
        'method_name': 'getTransformationMatrix',
        'method_anchors': ['iget-object v0, p0, Lcom/airbnb/lottie/animation/content/ContentGroup;->transformAnimation:Lcom/airbnb/lottie/animation/keyframe/TransformKeyframeAnimation;', 'if-eqz v0, :cond_0', 'invoke-virtual {v0}, Lcom/airbnb/lottie/animation/keyframe/TransformKeyframeAnimation;->getMatrix()Landroid/graphics/Matrix;', 'return-object p0', 'iget-object v0, p0, Lcom/airbnb/lottie/animation/content/ContentGroup;->matrix:Landroid/graphics/Matrix;', 'invoke-virtual {v0}, Landroid/graphics/Matrix;->reset()V', 'iget-object p0, p0, Lcom/airbnb/lottie/animation/content/ContentGroup;->matrix:Landroid/graphics/Matrix;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method getTransformationMatrix()Landroid/graphics/Matrix;
    .registers 2

    iget-object v0, p0, Lcom/airbnb/lottie/animation/content/ContentGroup;->transformAnimation:Lcom/airbnb/lottie/animation/keyframe/TransformKeyframeAnimation;

    if-eqz v0, :cond_0

    invoke-virtual {v0}, Lcom/airbnb/lottie/animation/keyframe/TransformKeyframeAnimation;->getMatrix()Landroid/graphics/Matrix;

    move-result-object p0

    return-object p0

    :cond_0
    iget-object v0, p0, Lcom/airbnb/lottie/animation/content/ContentGroup;->matrix:Landroid/graphics/Matrix;

    invoke-virtual {v0}, Landroid/graphics/Matrix;->reset()V

    iget-object p0, p0, Lcom/airbnb/lottie/animation/content/ContentGroup;->matrix:Landroid/graphics/Matrix;

    return-object p0
.end method""",
        'replacement': """.method getTransformationMatrix()Landroid/graphics/Matrix;
    .registers 2

    goto :goto_0

    nop

    :goto_0
    iget-object v0, p0, Lcom/airbnb/lottie/animation/content/ContentGroup;->transformAnimation:Lcom/airbnb/lottie/animation/keyframe/TransformKeyframeAnimation;

    goto :goto_8

    nop

    :goto_1
    invoke-virtual {v0}, Lcom/airbnb/lottie/animation/keyframe/TransformKeyframeAnimation;->getMatrix()Landroid/graphics/Matrix;

    move-result-object p0

    goto :goto_4

    nop

    :goto_2
    iget-object p0, p0, Lcom/airbnb/lottie/animation/content/ContentGroup;->matrix:Landroid/graphics/Matrix;

    goto :goto_3

    nop

    :goto_3
    return-object p0

    :goto_4
    return-object p0

    :goto_5
    goto :goto_6

    nop

    :goto_6
    iget-object v0, p0, Lcom/airbnb/lottie/animation/content/ContentGroup;->matrix:Landroid/graphics/Matrix;

    goto :goto_7

    nop

    :goto_7
    invoke-virtual {v0}, Landroid/graphics/Matrix;->reset()V

    goto :goto_2

    nop

    :goto_8
    if-nez v0, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
