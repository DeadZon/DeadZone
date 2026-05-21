TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/airbnb/lottie/parser/DropShadowEffectParser.smali'
CLASS_FALLBACK_NAMES = ['DropShadowEffectParser.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field private static final DROP_SHADOW_EFFECT_NAMES:Lcom/airbnb/lottie/parser/moshi/JsonReader$Options;', '.field private static final INNER_EFFECT_NAMES:Lcom/airbnb/lottie/parser/moshi/JsonReader$Options;']

PATCHES = [
    {
        'id': 'com_airbnb_lottie_parser_DropShadowEffectParser__parse',
        'method': '.method parse(Lcom/airbnb/lottie/parser/moshi/JsonReader;Lcom/airbnb/lottie/LottieComposition;)Lcom/airbnb/lottie/parser/DropShadowEffect;',
        'method_name': 'parse',
        'method_anchors': ['invoke-virtual {p1}, Lcom/airbnb/lottie/parser/moshi/JsonReader;->hasNext()Z', 'if-eqz v0, :cond_2', 'sget-object v0, Lcom/airbnb/lottie/parser/DropShadowEffectParser;->DROP_SHADOW_EFFECT_NAMES:Lcom/airbnb/lottie/parser/moshi/JsonReader$Options;', 'invoke-virtual {p1, v0}, Lcom/airbnb/lottie/parser/moshi/JsonReader;->selectName(Lcom/airbnb/lottie/parser/moshi/JsonReader$Options;)I', 'if-eqz v0, :cond_0', 'invoke-virtual {p1}, Lcom/airbnb/lottie/parser/moshi/JsonReader;->skipName()V', 'invoke-virtual {p1}, Lcom/airbnb/lottie/parser/moshi/JsonReader;->skipValue()V', 'invoke-virtual {p1}, Lcom/airbnb/lottie/parser/moshi/JsonReader;->beginArray()V'],
        'type': 'method_replace',
        'search': """.method parse(Lcom/airbnb/lottie/parser/moshi/JsonReader;Lcom/airbnb/lottie/LottieComposition;)Lcom/airbnb/lottie/parser/DropShadowEffect;
    .registers 10

    :goto_0
    invoke-virtual {p1}, Lcom/airbnb/lottie/parser/moshi/JsonReader;->hasNext()Z

    move-result v0

    if-eqz v0, :cond_2

    sget-object v0, Lcom/airbnb/lottie/parser/DropShadowEffectParser;->DROP_SHADOW_EFFECT_NAMES:Lcom/airbnb/lottie/parser/moshi/JsonReader$Options;

    invoke-virtual {p1, v0}, Lcom/airbnb/lottie/parser/moshi/JsonReader;->selectName(Lcom/airbnb/lottie/parser/moshi/JsonReader$Options;)I

    move-result v0

    if-eqz v0, :cond_0

    invoke-virtual {p1}, Lcom/airbnb/lottie/parser/moshi/JsonReader;->skipName()V

    invoke-virtual {p1}, Lcom/airbnb/lottie/parser/moshi/JsonReader;->skipValue()V

    goto :goto_0

    :cond_0
    invoke-virtual {p1}, Lcom/airbnb/lottie/parser/moshi/JsonReader;->beginArray()V

    :goto_1
    invoke-virtual {p1}, Lcom/airbnb/lottie/parser/moshi/JsonReader;->hasNext()Z

    move-result v0

    if-eqz v0, :cond_1

    invoke-direct {p0, p1, p2}, Lcom/airbnb/lottie/parser/DropShadowEffectParser;->maybeParseInnerEffect(Lcom/airbnb/lottie/parser/moshi/JsonReader;Lcom/airbnb/lottie/LottieComposition;)V

    goto :goto_1

    :cond_1
    invoke-virtual {p1}, Lcom/airbnb/lottie/parser/moshi/JsonReader;->endArray()V

    goto :goto_0

    :cond_2
    iget-object v2, p0, Lcom/airbnb/lottie/parser/DropShadowEffectParser;->color:Lcom/airbnb/lottie/model/animatable/AnimatableColorValue;

    if-eqz v2, :cond_3

    iget-object v3, p0, Lcom/airbnb/lottie/parser/DropShadowEffectParser;->opacity:Lcom/airbnb/lottie/model/animatable/AnimatableFloatValue;

    if-eqz v3, :cond_3

    iget-object v4, p0, Lcom/airbnb/lottie/parser/DropShadowEffectParser;->direction:Lcom/airbnb/lottie/model/animatable/AnimatableFloatValue;

    if-eqz v4, :cond_3

    iget-object v5, p0, Lcom/airbnb/lottie/parser/DropShadowEffectParser;->distance:Lcom/airbnb/lottie/model/animatable/AnimatableFloatValue;

    if-eqz v5, :cond_3

    iget-object v6, p0, Lcom/airbnb/lottie/parser/DropShadowEffectParser;->radius:Lcom/airbnb/lottie/model/animatable/AnimatableFloatValue;

    if-eqz v6, :cond_3

    new-instance v1, Lcom/airbnb/lottie/parser/DropShadowEffect;

    invoke-direct/range {v1 .. v6}, Lcom/airbnb/lottie/parser/DropShadowEffect;-><init>(Lcom/airbnb/lottie/model/animatable/AnimatableColorValue;Lcom/airbnb/lottie/model/animatable/AnimatableFloatValue;Lcom/airbnb/lottie/model/animatable/AnimatableFloatValue;Lcom/airbnb/lottie/model/animatable/AnimatableFloatValue;Lcom/airbnb/lottie/model/animatable/AnimatableFloatValue;)V

    return-object v1

    :cond_3
    const/4 p0, 0x0

    return-object p0
.end method""",
        'replacement': """.method parse(Lcom/airbnb/lottie/parser/moshi/JsonReader;Lcom/airbnb/lottie/LottieComposition;)Lcom/airbnb/lottie/parser/DropShadowEffect;
    .registers 10

    :goto_0
    goto :goto_1e

    nop

    :goto_1
    if-nez v0, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_18

    nop

    :goto_2
    goto :goto_13

    :goto_3
    goto :goto_1a

    nop

    :goto_4
    iget-object v5, p0, Lcom/airbnb/lottie/parser/DropShadowEffectParser;->distance:Lcom/airbnb/lottie/model/animatable/AnimatableFloatValue;

    goto :goto_16

    nop

    :goto_5
    iget-object v4, p0, Lcom/airbnb/lottie/parser/DropShadowEffectParser;->direction:Lcom/airbnb/lottie/model/animatable/AnimatableFloatValue;

    goto :goto_a

    nop

    :goto_6
    goto :goto_0

    :goto_7
    goto :goto_1c

    nop

    :goto_8
    invoke-virtual {p1}, Lcom/airbnb/lottie/parser/moshi/JsonReader;->skipValue()V

    goto :goto_14

    nop

    :goto_9
    iget-object v3, p0, Lcom/airbnb/lottie/parser/DropShadowEffectParser;->opacity:Lcom/airbnb/lottie/model/animatable/AnimatableFloatValue;

    goto :goto_b

    nop

    :goto_a
    if-nez v4, :cond_1

    goto :goto_10

    :cond_1
    goto :goto_4

    nop

    :goto_b
    if-nez v3, :cond_2

    goto :goto_10

    :cond_2
    goto :goto_5

    nop

    :goto_c
    invoke-virtual {p1}, Lcom/airbnb/lottie/parser/moshi/JsonReader;->hasNext()Z

    move-result v0

    goto :goto_1

    nop

    :goto_d
    return-object p0

    :goto_e
    invoke-direct/range {v1 .. v6}, Lcom/airbnb/lottie/parser/DropShadowEffect;-><init>(Lcom/airbnb/lottie/model/animatable/AnimatableColorValue;Lcom/airbnb/lottie/model/animatable/AnimatableFloatValue;Lcom/airbnb/lottie/model/animatable/AnimatableFloatValue;Lcom/airbnb/lottie/model/animatable/AnimatableFloatValue;Lcom/airbnb/lottie/model/animatable/AnimatableFloatValue;)V

    goto :goto_f

    nop

    :goto_f
    return-object v1

    :goto_10
    goto :goto_22

    nop

    :goto_11
    if-nez v2, :cond_3

    goto :goto_10

    :cond_3
    goto :goto_9

    nop

    :goto_12
    invoke-virtual {p1}, Lcom/airbnb/lottie/parser/moshi/JsonReader;->beginArray()V

    :goto_13
    goto :goto_c

    nop

    :goto_14
    goto :goto_0

    :goto_15
    goto :goto_12

    nop

    :goto_16
    if-nez v5, :cond_4

    goto :goto_10

    :cond_4
    goto :goto_21

    nop

    :goto_17
    invoke-virtual {p1}, Lcom/airbnb/lottie/parser/moshi/JsonReader;->skipName()V

    goto :goto_8

    nop

    :goto_18
    invoke-direct {p0, p1, p2}, Lcom/airbnb/lottie/parser/DropShadowEffectParser;->maybeParseInnerEffect(Lcom/airbnb/lottie/parser/moshi/JsonReader;Lcom/airbnb/lottie/LottieComposition;)V

    goto :goto_2

    nop

    :goto_19
    invoke-virtual {p1, v0}, Lcom/airbnb/lottie/parser/moshi/JsonReader;->selectName(Lcom/airbnb/lottie/parser/moshi/JsonReader$Options;)I

    move-result v0

    goto :goto_1f

    nop

    :goto_1a
    invoke-virtual {p1}, Lcom/airbnb/lottie/parser/moshi/JsonReader;->endArray()V

    goto :goto_6

    nop

    :goto_1b
    if-nez v0, :cond_5

    goto :goto_7

    :cond_5
    goto :goto_23

    nop

    :goto_1c
    iget-object v2, p0, Lcom/airbnb/lottie/parser/DropShadowEffectParser;->color:Lcom/airbnb/lottie/model/animatable/AnimatableColorValue;

    goto :goto_11

    nop

    :goto_1d
    new-instance v1, Lcom/airbnb/lottie/parser/DropShadowEffect;

    goto :goto_e

    nop

    :goto_1e
    invoke-virtual {p1}, Lcom/airbnb/lottie/parser/moshi/JsonReader;->hasNext()Z

    move-result v0

    goto :goto_1b

    nop

    :goto_1f
    if-nez v0, :cond_6

    goto :goto_15

    :cond_6
    goto :goto_17

    nop

    :goto_20
    if-nez v6, :cond_7

    goto :goto_10

    :cond_7
    goto :goto_1d

    nop

    :goto_21
    iget-object v6, p0, Lcom/airbnb/lottie/parser/DropShadowEffectParser;->radius:Lcom/airbnb/lottie/model/animatable/AnimatableFloatValue;

    goto :goto_20

    nop

    :goto_22
    const/4 p0, 0x0

    goto :goto_d

    nop

    :goto_23
    sget-object v0, Lcom/airbnb/lottie/parser/DropShadowEffectParser;->DROP_SHADOW_EFFECT_NAMES:Lcom/airbnb/lottie/parser/moshi/JsonReader$Options;

    goto :goto_19

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
