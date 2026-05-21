TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/airbnb/lottie/model/layer/TextLayer.smali'
CLASS_FALLBACK_NAMES = ['TextLayer.smali']
CLASS_ANCHORS = ['.super Lcom/airbnb/lottie/model/layer/BaseLayer;']

PATCHES = [
    {
        'id': 'com_airbnb_lottie_model_layer_TextLayer__drawLayer',
        'method': '.method drawLayer(Landroid/graphics/Canvas;Landroid/graphics/Matrix;I)V',
        'method_name': 'drawLayer',
        'method_anchors': ['invoke-virtual {p1}, Landroid/graphics/Canvas;->save()I', 'iget-object p3, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->lottieDrawable:Lcom/airbnb/lottie/LottieDrawable;', 'invoke-virtual {p3}, Lcom/airbnb/lottie/LottieDrawable;->useTextGlyphs()Z', 'if-nez p3, :cond_0', 'invoke-virtual {p1, p2}, Landroid/graphics/Canvas;->concat(Landroid/graphics/Matrix;)V', 'iget-object p3, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->textAnimation:Lcom/airbnb/lottie/animation/keyframe/TextKeyframeAnimation;', 'invoke-virtual {p3}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getValue()Ljava/lang/Object;', 'check-cast p3, Lcom/airbnb/lottie/model/DocumentData;'],
        'type': 'method_replace',
        'search': """.method drawLayer(Landroid/graphics/Canvas;Landroid/graphics/Matrix;I)V
    .registers 9

    invoke-virtual {p1}, Landroid/graphics/Canvas;->save()I

    iget-object p3, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->lottieDrawable:Lcom/airbnb/lottie/LottieDrawable;

    invoke-virtual {p3}, Lcom/airbnb/lottie/LottieDrawable;->useTextGlyphs()Z

    move-result p3

    if-nez p3, :cond_0

    invoke-virtual {p1, p2}, Landroid/graphics/Canvas;->concat(Landroid/graphics/Matrix;)V

    :cond_0
    iget-object p3, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->textAnimation:Lcom/airbnb/lottie/animation/keyframe/TextKeyframeAnimation;

    invoke-virtual {p3}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getValue()Ljava/lang/Object;

    move-result-object p3

    check-cast p3, Lcom/airbnb/lottie/model/DocumentData;

    iget-object v0, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->composition:Lcom/airbnb/lottie/LottieComposition;

    invoke-virtual {v0}, Lcom/airbnb/lottie/LottieComposition;->getFonts()Ljava/util/Map;

    move-result-object v0

    iget-object v1, p3, Lcom/airbnb/lottie/model/DocumentData;->fontName:Ljava/lang/String;

    invoke-interface {v0, v1}, Ljava/util/Map;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/airbnb/lottie/model/Font;

    if-nez v0, :cond_1

    invoke-virtual {p1}, Landroid/graphics/Canvas;->restore()V

    return-void

    :cond_1
    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->colorCallbackAnimation:Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;

    if-eqz v1, :cond_2

    iget-object v2, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->fillPaint:Landroid/graphics/Paint;

    invoke-virtual {v1}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getValue()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Ljava/lang/Integer;

    invoke-virtual {v1}, Ljava/lang/Integer;->intValue()I

    move-result v1

    invoke-virtual {v2, v1}, Landroid/graphics/Paint;->setColor(I)V

    goto :goto_0

    :cond_2
    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->colorAnimation:Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;

    if-eqz v1, :cond_3

    iget-object v2, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->fillPaint:Landroid/graphics/Paint;

    invoke-virtual {v1}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getValue()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Ljava/lang/Integer;

    invoke-virtual {v1}, Ljava/lang/Integer;->intValue()I

    move-result v1

    invoke-virtual {v2, v1}, Landroid/graphics/Paint;->setColor(I)V

    goto :goto_0

    :cond_3
    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->fillPaint:Landroid/graphics/Paint;

    iget v2, p3, Lcom/airbnb/lottie/model/DocumentData;->color:I

    invoke-virtual {v1, v2}, Landroid/graphics/Paint;->setColor(I)V

    :goto_0
    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->strokeColorCallbackAnimation:Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;

    if-eqz v1, :cond_4

    iget-object v2, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->strokePaint:Landroid/graphics/Paint;

    invoke-virtual {v1}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getValue()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Ljava/lang/Integer;

    invoke-virtual {v1}, Ljava/lang/Integer;->intValue()I

    move-result v1

    invoke-virtual {v2, v1}, Landroid/graphics/Paint;->setColor(I)V

    goto :goto_1

    :cond_4
    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->strokeColorAnimation:Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;

    if-eqz v1, :cond_5

    iget-object v2, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->strokePaint:Landroid/graphics/Paint;

    invoke-virtual {v1}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getValue()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Ljava/lang/Integer;

    invoke-virtual {v1}, Ljava/lang/Integer;->intValue()I

    move-result v1

    invoke-virtual {v2, v1}, Landroid/graphics/Paint;->setColor(I)V

    goto :goto_1

    :cond_5
    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->strokePaint:Landroid/graphics/Paint;

    iget v2, p3, Lcom/airbnb/lottie/model/DocumentData;->strokeColor:I

    invoke-virtual {v1, v2}, Landroid/graphics/Paint;->setColor(I)V

    :goto_1
    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->transform:Lcom/airbnb/lottie/animation/keyframe/TransformKeyframeAnimation;

    invoke-virtual {v1}, Lcom/airbnb/lottie/animation/keyframe/TransformKeyframeAnimation;->getOpacity()Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;

    move-result-object v1

    const/16 v2, 0x64

    if-nez v1, :cond_6

    move v1, v2

    goto :goto_2

    :cond_6
    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->transform:Lcom/airbnb/lottie/animation/keyframe/TransformKeyframeAnimation;

    invoke-virtual {v1}, Lcom/airbnb/lottie/animation/keyframe/TransformKeyframeAnimation;->getOpacity()Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;

    move-result-object v1

    invoke-virtual {v1}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getValue()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Ljava/lang/Integer;

    invoke-virtual {v1}, Ljava/lang/Integer;->intValue()I

    move-result v1

    :goto_2
    mul-int/lit16 v1, v1, 0xff

    div-int/2addr v1, v2

    iget-object v2, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->fillPaint:Landroid/graphics/Paint;

    invoke-virtual {v2, v1}, Landroid/graphics/Paint;->setAlpha(I)V

    iget-object v2, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->strokePaint:Landroid/graphics/Paint;

    invoke-virtual {v2, v1}, Landroid/graphics/Paint;->setAlpha(I)V

    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->strokeWidthCallbackAnimation:Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;

    if-eqz v1, :cond_7

    iget-object v2, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->strokePaint:Landroid/graphics/Paint;

    invoke-virtual {v1}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getValue()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Ljava/lang/Float;

    invoke-virtual {v1}, Ljava/lang/Float;->floatValue()F

    move-result v1

    invoke-virtual {v2, v1}, Landroid/graphics/Paint;->setStrokeWidth(F)V

    goto :goto_3

    :cond_7
    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->strokeWidthAnimation:Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;

    if-eqz v1, :cond_8

    iget-object v2, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->strokePaint:Landroid/graphics/Paint;

    invoke-virtual {v1}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getValue()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Ljava/lang/Float;

    invoke-virtual {v1}, Ljava/lang/Float;->floatValue()F

    move-result v1

    invoke-virtual {v2, v1}, Landroid/graphics/Paint;->setStrokeWidth(F)V

    goto :goto_3

    :cond_8
    invoke-static {p2}, Lcom/airbnb/lottie/utils/Utils;->getScale(Landroid/graphics/Matrix;)F

    move-result v1

    iget-object v2, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->strokePaint:Landroid/graphics/Paint;

    iget v3, p3, Lcom/airbnb/lottie/model/DocumentData;->strokeWidth:F

    invoke-static {}, Lcom/airbnb/lottie/utils/Utils;->dpScale()F

    move-result v4

    mul-float/2addr v3, v4

    mul-float/2addr v3, v1

    invoke-virtual {v2, v3}, Landroid/graphics/Paint;->setStrokeWidth(F)V

    :goto_3
    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->lottieDrawable:Lcom/airbnb/lottie/LottieDrawable;

    invoke-virtual {v1}, Lcom/airbnb/lottie/LottieDrawable;->useTextGlyphs()Z

    move-result v1

    if-eqz v1, :cond_9

    invoke-direct {p0, p3, p2, v0, p1}, Lcom/airbnb/lottie/model/layer/TextLayer;->drawTextGlyphs(Lcom/airbnb/lottie/model/DocumentData;Landroid/graphics/Matrix;Lcom/airbnb/lottie/model/Font;Landroid/graphics/Canvas;)V

    goto :goto_4

    :cond_9
    invoke-direct {p0, p3, v0, p1}, Lcom/airbnb/lottie/model/layer/TextLayer;->drawTextWithFont(Lcom/airbnb/lottie/model/DocumentData;Lcom/airbnb/lottie/model/Font;Landroid/graphics/Canvas;)V

    :goto_4
    invoke-virtual {p1}, Landroid/graphics/Canvas;->restore()V

    return-void
.end method""",
        'replacement': """.method drawLayer(Landroid/graphics/Canvas;Landroid/graphics/Matrix;I)V
    .registers 9

    goto :goto_60

    nop

    :goto_0
    mul-int/lit16 v1, v1, 0xff

    goto :goto_47

    nop

    :goto_1
    invoke-virtual {v1}, Lcom/airbnb/lottie/animation/keyframe/TransformKeyframeAnimation;->getOpacity()Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;

    move-result-object v1

    goto :goto_2d

    nop

    :goto_2
    invoke-virtual {v1}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getValue()Ljava/lang/Object;

    move-result-object v1

    goto :goto_11

    nop

    :goto_3
    invoke-direct {p0, p3, v0, p1}, Lcom/airbnb/lottie/model/layer/TextLayer;->drawTextWithFont(Lcom/airbnb/lottie/model/DocumentData;Lcom/airbnb/lottie/model/Font;Landroid/graphics/Canvas;)V

    :goto_4
    goto :goto_1c

    nop

    :goto_5
    check-cast v1, Ljava/lang/Integer;

    goto :goto_6f

    nop

    :goto_6
    if-eqz p3, :cond_0

    goto :goto_5d

    :cond_0
    goto :goto_5c

    nop

    :goto_7
    invoke-virtual {v1}, Ljava/lang/Float;->floatValue()F

    move-result v1

    goto :goto_4b

    nop

    :goto_8
    goto :goto_23

    :goto_9
    goto :goto_4a

    nop

    :goto_a
    if-nez v1, :cond_1

    goto :goto_51

    :cond_1
    goto :goto_5a

    nop

    :goto_b
    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->strokePaint:Landroid/graphics/Paint;

    goto :goto_44

    nop

    :goto_c
    mul-float/2addr v3, v4

    goto :goto_4d

    nop

    :goto_d
    invoke-virtual {v1}, Ljava/lang/Integer;->intValue()I

    move-result v1

    :goto_e
    goto :goto_0

    nop

    :goto_f
    return-void

    :goto_10
    goto :goto_32

    nop

    :goto_11
    check-cast v1, Ljava/lang/Integer;

    goto :goto_34

    nop

    :goto_12
    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->strokeColorCallbackAnimation:Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;

    goto :goto_a

    nop

    :goto_13
    invoke-direct {p0, p3, p2, v0, p1}, Lcom/airbnb/lottie/model/layer/TextLayer;->drawTextGlyphs(Lcom/airbnb/lottie/model/DocumentData;Landroid/graphics/Matrix;Lcom/airbnb/lottie/model/Font;Landroid/graphics/Canvas;)V

    goto :goto_2f

    nop

    :goto_14
    invoke-static {p2}, Lcom/airbnb/lottie/utils/Utils;->getScale(Landroid/graphics/Matrix;)F

    move-result v1

    goto :goto_21

    nop

    :goto_15
    invoke-virtual {v2, v1}, Landroid/graphics/Paint;->setColor(I)V

    goto :goto_48

    nop

    :goto_16
    invoke-virtual {v1}, Ljava/lang/Integer;->intValue()I

    move-result v1

    goto :goto_71

    nop

    :goto_17
    if-nez v1, :cond_2

    goto :goto_49

    :cond_2
    goto :goto_58

    nop

    :goto_18
    check-cast p3, Lcom/airbnb/lottie/model/DocumentData;

    goto :goto_36

    nop

    :goto_19
    if-eqz v0, :cond_3

    goto :goto_10

    :cond_3
    goto :goto_2b

    nop

    :goto_1a
    invoke-virtual {v2, v1}, Landroid/graphics/Paint;->setAlpha(I)V

    goto :goto_67

    nop

    :goto_1b
    if-nez v1, :cond_4

    goto :goto_56

    :cond_4
    goto :goto_2c

    nop

    :goto_1c
    invoke-virtual {p1}, Landroid/graphics/Canvas;->restore()V

    goto :goto_1f

    nop

    :goto_1d
    iget-object v2, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->fillPaint:Landroid/graphics/Paint;

    goto :goto_2

    nop

    :goto_1e
    invoke-virtual {v0}, Lcom/airbnb/lottie/LottieComposition;->getFonts()Ljava/util/Map;

    move-result-object v0

    goto :goto_6e

    nop

    :goto_1f
    return-void

    :goto_20
    invoke-virtual {v1}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getValue()Ljava/lang/Object;

    move-result-object v1

    goto :goto_70

    nop

    :goto_21
    iget-object v2, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->strokePaint:Landroid/graphics/Paint;

    goto :goto_25

    nop

    :goto_22
    invoke-virtual {v1, v2}, Landroid/graphics/Paint;->setColor(I)V

    :goto_23
    goto :goto_12

    nop

    :goto_24
    invoke-virtual {v2, v1}, Landroid/graphics/Paint;->setColor(I)V

    goto :goto_42

    nop

    :goto_25
    iget v3, p3, Lcom/airbnb/lottie/model/DocumentData;->strokeWidth:F

    goto :goto_62

    nop

    :goto_26
    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->strokeWidthCallbackAnimation:Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;

    goto :goto_4c

    nop

    :goto_27
    goto :goto_e

    :goto_28
    goto :goto_5f

    nop

    :goto_29
    invoke-virtual {p3}, Lcom/airbnb/lottie/LottieDrawable;->useTextGlyphs()Z

    move-result p3

    goto :goto_6

    nop

    :goto_2a
    if-nez v1, :cond_5

    goto :goto_30

    :cond_5
    goto :goto_13

    nop

    :goto_2b
    invoke-virtual {p1}, Landroid/graphics/Canvas;->restore()V

    goto :goto_f

    nop

    :goto_2c
    iget-object v2, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->strokePaint:Landroid/graphics/Paint;

    goto :goto_63

    nop

    :goto_2d
    const/16 v2, 0x64

    goto :goto_46

    nop

    :goto_2e
    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->fillPaint:Landroid/graphics/Paint;

    goto :goto_3b

    nop

    :goto_2f
    goto :goto_4

    :goto_30
    goto :goto_3

    nop

    :goto_31
    invoke-virtual {v1}, Lcom/airbnb/lottie/animation/keyframe/TransformKeyframeAnimation;->getOpacity()Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;

    move-result-object v1

    goto :goto_35

    nop

    :goto_32
    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->colorCallbackAnimation:Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;

    goto :goto_5b

    nop

    :goto_33
    invoke-virtual {v1}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getValue()Ljava/lang/Object;

    move-result-object v1

    goto :goto_52

    nop

    :goto_34
    invoke-virtual {v1}, Ljava/lang/Integer;->intValue()I

    move-result v1

    goto :goto_24

    nop

    :goto_35
    invoke-virtual {v1}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getValue()Ljava/lang/Object;

    move-result-object v1

    goto :goto_65

    nop

    :goto_36
    iget-object v0, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->composition:Lcom/airbnb/lottie/LottieComposition;

    goto :goto_1e

    nop

    :goto_37
    invoke-virtual {v1, v2}, Landroid/graphics/Paint;->setColor(I)V

    :goto_38
    goto :goto_66

    nop

    :goto_39
    move v1, v2

    goto :goto_27

    nop

    :goto_3a
    iget-object v2, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->fillPaint:Landroid/graphics/Paint;

    goto :goto_1a

    nop

    :goto_3b
    iget v2, p3, Lcom/airbnb/lottie/model/DocumentData;->color:I

    goto :goto_22

    nop

    :goto_3c
    invoke-virtual {v2, v1}, Landroid/graphics/Paint;->setAlpha(I)V

    goto :goto_26

    nop

    :goto_3d
    iget-object v2, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->fillPaint:Landroid/graphics/Paint;

    goto :goto_68

    nop

    :goto_3e
    invoke-virtual {v2, v1}, Landroid/graphics/Paint;->setStrokeWidth(F)V

    goto :goto_3f

    nop

    :goto_3f
    goto :goto_6b

    :goto_40
    goto :goto_4e

    nop

    :goto_41
    check-cast v1, Ljava/lang/Float;

    goto :goto_7

    nop

    :goto_42
    goto :goto_23

    :goto_43
    goto :goto_2e

    nop

    :goto_44
    iget v2, p3, Lcom/airbnb/lottie/model/DocumentData;->strokeColor:I

    goto :goto_37

    nop

    :goto_45
    if-nez v1, :cond_6

    goto :goto_43

    :cond_6
    goto :goto_1d

    nop

    :goto_46
    if-eqz v1, :cond_7

    goto :goto_28

    :cond_7
    goto :goto_39

    nop

    :goto_47
    div-int/2addr v1, v2

    goto :goto_3a

    nop

    :goto_48
    goto :goto_38

    :goto_49
    goto :goto_b

    nop

    :goto_4a
    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->colorAnimation:Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;

    goto :goto_45

    nop

    :goto_4b
    invoke-virtual {v2, v1}, Landroid/graphics/Paint;->setStrokeWidth(F)V

    goto :goto_55

    nop

    :goto_4c
    if-nez v1, :cond_8

    goto :goto_40

    :cond_8
    goto :goto_57

    nop

    :goto_4d
    mul-float/2addr v3, v1

    goto :goto_6a

    nop

    :goto_4e
    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->strokeWidthAnimation:Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;

    goto :goto_1b

    nop

    :goto_4f
    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->lottieDrawable:Lcom/airbnb/lottie/LottieDrawable;

    goto :goto_6c

    nop

    :goto_50
    goto :goto_38

    :goto_51
    goto :goto_74

    nop

    :goto_52
    check-cast v1, Ljava/lang/Integer;

    goto :goto_16

    nop

    :goto_53
    invoke-virtual {v1}, Ljava/lang/Integer;->intValue()I

    move-result v1

    goto :goto_5e

    nop

    :goto_54
    iget-object p3, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->textAnimation:Lcom/airbnb/lottie/animation/keyframe/TextKeyframeAnimation;

    goto :goto_61

    nop

    :goto_55
    goto :goto_6b

    :goto_56
    goto :goto_14

    nop

    :goto_57
    iget-object v2, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->strokePaint:Landroid/graphics/Paint;

    goto :goto_20

    nop

    :goto_58
    iget-object v2, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->strokePaint:Landroid/graphics/Paint;

    goto :goto_59

    nop

    :goto_59
    invoke-virtual {v1}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getValue()Ljava/lang/Object;

    move-result-object v1

    goto :goto_5

    nop

    :goto_5a
    iget-object v2, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->strokePaint:Landroid/graphics/Paint;

    goto :goto_33

    nop

    :goto_5b
    if-nez v1, :cond_9

    goto :goto_9

    :cond_9
    goto :goto_3d

    nop

    :goto_5c
    invoke-virtual {p1, p2}, Landroid/graphics/Canvas;->concat(Landroid/graphics/Matrix;)V

    :goto_5d
    goto :goto_54

    nop

    :goto_5e
    invoke-virtual {v2, v1}, Landroid/graphics/Paint;->setColor(I)V

    goto :goto_8

    nop

    :goto_5f
    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->transform:Lcom/airbnb/lottie/animation/keyframe/TransformKeyframeAnimation;

    goto :goto_31

    nop

    :goto_60
    invoke-virtual {p1}, Landroid/graphics/Canvas;->save()I

    goto :goto_69

    nop

    :goto_61
    invoke-virtual {p3}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getValue()Ljava/lang/Object;

    move-result-object p3

    goto :goto_18

    nop

    :goto_62
    invoke-static {}, Lcom/airbnb/lottie/utils/Utils;->dpScale()F

    move-result v4

    goto :goto_c

    nop

    :goto_63
    invoke-virtual {v1}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getValue()Ljava/lang/Object;

    move-result-object v1

    goto :goto_41

    nop

    :goto_64
    invoke-interface {v0, v1}, Ljava/util/Map;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    goto :goto_6d

    nop

    :goto_65
    check-cast v1, Ljava/lang/Integer;

    goto :goto_d

    nop

    :goto_66
    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/BaseLayer;->transform:Lcom/airbnb/lottie/animation/keyframe/TransformKeyframeAnimation;

    goto :goto_1

    nop

    :goto_67
    iget-object v2, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->strokePaint:Landroid/graphics/Paint;

    goto :goto_3c

    nop

    :goto_68
    invoke-virtual {v1}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getValue()Ljava/lang/Object;

    move-result-object v1

    goto :goto_73

    nop

    :goto_69
    iget-object p3, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->lottieDrawable:Lcom/airbnb/lottie/LottieDrawable;

    goto :goto_29

    nop

    :goto_6a
    invoke-virtual {v2, v3}, Landroid/graphics/Paint;->setStrokeWidth(F)V

    :goto_6b
    goto :goto_4f

    nop

    :goto_6c
    invoke-virtual {v1}, Lcom/airbnb/lottie/LottieDrawable;->useTextGlyphs()Z

    move-result v1

    goto :goto_2a

    nop

    :goto_6d
    check-cast v0, Lcom/airbnb/lottie/model/Font;

    goto :goto_19

    nop

    :goto_6e
    iget-object v1, p3, Lcom/airbnb/lottie/model/DocumentData;->fontName:Ljava/lang/String;

    goto :goto_64

    nop

    :goto_6f
    invoke-virtual {v1}, Ljava/lang/Integer;->intValue()I

    move-result v1

    goto :goto_15

    nop

    :goto_70
    check-cast v1, Ljava/lang/Float;

    goto :goto_72

    nop

    :goto_71
    invoke-virtual {v2, v1}, Landroid/graphics/Paint;->setColor(I)V

    goto :goto_50

    nop

    :goto_72
    invoke-virtual {v1}, Ljava/lang/Float;->floatValue()F

    move-result v1

    goto :goto_3e

    nop

    :goto_73
    check-cast v1, Ljava/lang/Integer;

    goto :goto_53

    nop

    :goto_74
    iget-object v1, p0, Lcom/airbnb/lottie/model/layer/TextLayer;->strokeColorAnimation:Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;

    goto :goto_17

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
