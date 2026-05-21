TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/airbnb/lottie/parser/moshi/JsonReader.smali'
CLASS_FALLBACK_NAMES = ['JsonReader.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Ljava/io/Closeable;', '.field private static final REPLACEMENT_CHARS:[Ljava/lang/String;']

PATCHES = [
    {
        'id': 'com_airbnb_lottie_parser_moshi_JsonReader__pushScope',
        'method': '.method final pushScope(I)V',
        'method_name': 'pushScope',
        'method_anchors': ['iget v0, p0, Lcom/airbnb/lottie/parser/moshi/JsonReader;->stackSize:I', 'iget-object v1, p0, Lcom/airbnb/lottie/parser/moshi/JsonReader;->scopes:[I', 'if-ne v0, v2, :cond_1', 'if-eq v0, v2, :cond_0', 'invoke-static {v1, v0}, Ljava/util/Arrays;->copyOf([II)[I', 'iput-object v0, p0, Lcom/airbnb/lottie/parser/moshi/JsonReader;->scopes:[I', 'iget-object v0, p0, Lcom/airbnb/lottie/parser/moshi/JsonReader;->pathNames:[Ljava/lang/String;', 'invoke-static {v0, v1}, Ljava/util/Arrays;->copyOf([Ljava/lang/Object;I)[Ljava/lang/Object;'],
        'type': 'method_replace',
        'search': """.method final pushScope(I)V
    .registers 5

    iget v0, p0, Lcom/airbnb/lottie/parser/moshi/JsonReader;->stackSize:I

    iget-object v1, p0, Lcom/airbnb/lottie/parser/moshi/JsonReader;->scopes:[I

    array-length v2, v1

    if-ne v0, v2, :cond_1

    const/16 v2, 0x100

    if-eq v0, v2, :cond_0

    array-length v0, v1

    mul-int/lit8 v0, v0, 0x2

    invoke-static {v1, v0}, Ljava/util/Arrays;->copyOf([II)[I

    move-result-object v0

    iput-object v0, p0, Lcom/airbnb/lottie/parser/moshi/JsonReader;->scopes:[I

    iget-object v0, p0, Lcom/airbnb/lottie/parser/moshi/JsonReader;->pathNames:[Ljava/lang/String;

    array-length v1, v0

    mul-int/lit8 v1, v1, 0x2

    invoke-static {v0, v1}, Ljava/util/Arrays;->copyOf([Ljava/lang/Object;I)[Ljava/lang/Object;

    move-result-object v0

    check-cast v0, [Ljava/lang/String;

    iput-object v0, p0, Lcom/airbnb/lottie/parser/moshi/JsonReader;->pathNames:[Ljava/lang/String;

    iget-object v0, p0, Lcom/airbnb/lottie/parser/moshi/JsonReader;->pathIndices:[I

    array-length v1, v0

    mul-int/lit8 v1, v1, 0x2

    invoke-static {v0, v1}, Ljava/util/Arrays;->copyOf([II)[I

    move-result-object v0

    iput-object v0, p0, Lcom/airbnb/lottie/parser/moshi/JsonReader;->pathIndices:[I

    goto :goto_0

    :cond_0
    new-instance p1, Lcom/airbnb/lottie/parser/moshi/JsonDataException;

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v1, "Nesting too deep at "

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Lcom/airbnb/lottie/parser/moshi/JsonReader;->getPath()Ljava/lang/String;

    move-result-object p0

    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    invoke-direct {p1, p0}, Lcom/airbnb/lottie/parser/moshi/JsonDataException;-><init>(Ljava/lang/String;)V

    throw p1

    :cond_1
    :goto_0
    iget-object v0, p0, Lcom/airbnb/lottie/parser/moshi/JsonReader;->scopes:[I

    iget v1, p0, Lcom/airbnb/lottie/parser/moshi/JsonReader;->stackSize:I

    add-int/lit8 v2, v1, 0x1

    iput v2, p0, Lcom/airbnb/lottie/parser/moshi/JsonReader;->stackSize:I

    aput p1, v0, v1

    return-void
.end method""",
        'replacement': """.method final pushScope(I)V
    .registers 5

    goto :goto_21

    nop

    :goto_0
    invoke-virtual {p0}, Lcom/airbnb/lottie/parser/moshi/JsonReader;->getPath()Ljava/lang/String;

    move-result-object p0

    goto :goto_19

    nop

    :goto_1
    iget-object v0, p0, Lcom/airbnb/lottie/parser/moshi/JsonReader;->scopes:[I

    goto :goto_3

    nop

    :goto_2
    iget-object v1, p0, Lcom/airbnb/lottie/parser/moshi/JsonReader;->scopes:[I

    goto :goto_22

    nop

    :goto_3
    iget v1, p0, Lcom/airbnb/lottie/parser/moshi/JsonReader;->stackSize:I

    goto :goto_1e

    nop

    :goto_4
    iput-object v0, p0, Lcom/airbnb/lottie/parser/moshi/JsonReader;->pathNames:[Ljava/lang/String;

    goto :goto_5

    nop

    :goto_5
    iget-object v0, p0, Lcom/airbnb/lottie/parser/moshi/JsonReader;->pathIndices:[I

    goto :goto_24

    nop

    :goto_6
    invoke-static {v0, v1}, Ljava/util/Arrays;->copyOf([II)[I

    move-result-object v0

    goto :goto_27

    nop

    :goto_7
    check-cast v0, [Ljava/lang/String;

    goto :goto_4

    nop

    :goto_8
    iget-object v0, p0, Lcom/airbnb/lottie/parser/moshi/JsonReader;->pathNames:[Ljava/lang/String;

    goto :goto_20

    nop

    :goto_9
    if-eq v0, v2, :cond_0

    goto :goto_c

    :cond_0
    goto :goto_15

    nop

    :goto_a
    invoke-static {v1, v0}, Ljava/util/Arrays;->copyOf([II)[I

    move-result-object v0

    goto :goto_17

    nop

    :goto_b
    throw p1

    :goto_c
    goto :goto_1

    nop

    :goto_d
    mul-int/lit8 v0, v0, 0x2

    goto :goto_a

    nop

    :goto_e
    goto :goto_c

    :goto_f
    goto :goto_10

    nop

    :goto_10
    new-instance p1, Lcom/airbnb/lottie/parser/moshi/JsonDataException;

    goto :goto_16

    nop

    :goto_11
    if-ne v0, v2, :cond_1

    goto :goto_f

    :cond_1
    goto :goto_26

    nop

    :goto_12
    mul-int/lit8 v1, v1, 0x2

    goto :goto_6

    nop

    :goto_13
    return-void

    :goto_14
    mul-int/lit8 v1, v1, 0x2

    goto :goto_1b

    nop

    :goto_15
    const/16 v2, 0x100

    goto :goto_11

    nop

    :goto_16
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_1f

    nop

    :goto_17
    iput-object v0, p0, Lcom/airbnb/lottie/parser/moshi/JsonReader;->scopes:[I

    goto :goto_8

    nop

    :goto_18
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_0

    nop

    :goto_19
    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_1d

    nop

    :goto_1a
    iput v2, p0, Lcom/airbnb/lottie/parser/moshi/JsonReader;->stackSize:I

    goto :goto_1c

    nop

    :goto_1b
    invoke-static {v0, v1}, Ljava/util/Arrays;->copyOf([Ljava/lang/Object;I)[Ljava/lang/Object;

    move-result-object v0

    goto :goto_7

    nop

    :goto_1c
    aput p1, v0, v1

    goto :goto_13

    nop

    :goto_1d
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    goto :goto_23

    nop

    :goto_1e
    add-int/lit8 v2, v1, 0x1

    goto :goto_1a

    nop

    :goto_1f
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_25

    nop

    :goto_20
    array-length v1, v0

    goto :goto_14

    nop

    :goto_21
    iget v0, p0, Lcom/airbnb/lottie/parser/moshi/JsonReader;->stackSize:I

    goto :goto_2

    nop

    :goto_22
    array-length v2, v1

    goto :goto_9

    nop

    :goto_23
    invoke-direct {p1, p0}, Lcom/airbnb/lottie/parser/moshi/JsonDataException;-><init>(Ljava/lang/String;)V

    goto :goto_b

    nop

    :goto_24
    array-length v1, v0

    goto :goto_12

    nop

    :goto_25
    const-string v1, "Nesting too deep at "

    goto :goto_18

    nop

    :goto_26
    array-length v0, v1

    goto :goto_d

    nop

    :goto_27
    iput-object v0, p0, Lcom/airbnb/lottie/parser/moshi/JsonReader;->pathIndices:[I

    goto :goto_e

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_parser_moshi_JsonReader__syntaxError',
        'method': '.method final syntaxError(Ljava/lang/String;)Lcom/airbnb/lottie/parser/moshi/JsonEncodingException;',
        'method_name': 'syntaxError',
        'method_anchors': ['new-instance v0, Lcom/airbnb/lottie/parser/moshi/JsonEncodingException;', 'new-instance v1, Ljava/lang/StringBuilder;', 'invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V', 'invoke-virtual {v1, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'const-string p1, " at path "', 'invoke-virtual {v1, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'invoke-virtual {p0}, Lcom/airbnb/lottie/parser/moshi/JsonReader;->getPath()Ljava/lang/String;', 'invoke-virtual {v1, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;'],
        'type': 'method_replace',
        'search': """.method final syntaxError(Ljava/lang/String;)Lcom/airbnb/lottie/parser/moshi/JsonEncodingException;
    .registers 4

    new-instance v0, Lcom/airbnb/lottie/parser/moshi/JsonEncodingException;

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v1, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string p1, " at path "

    invoke-virtual {v1, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Lcom/airbnb/lottie/parser/moshi/JsonReader;->getPath()Ljava/lang/String;

    move-result-object p0

    invoke-virtual {v1, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    invoke-direct {v0, p0}, Lcom/airbnb/lottie/parser/moshi/JsonEncodingException;-><init>(Ljava/lang/String;)V

    throw v0
.end method""",
        'replacement': """.method final syntaxError(Ljava/lang/String;)Lcom/airbnb/lottie/parser/moshi/JsonEncodingException;
    .registers 4

    goto :goto_7

    nop

    :goto_0
    invoke-virtual {v1, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_2

    nop

    :goto_1
    invoke-virtual {p0}, Lcom/airbnb/lottie/parser/moshi/JsonReader;->getPath()Ljava/lang/String;

    move-result-object p0

    goto :goto_0

    nop

    :goto_2
    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    goto :goto_a

    nop

    :goto_3
    throw v0

    :goto_4
    invoke-virtual {v1, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_5

    nop

    :goto_5
    const-string p1, " at path "

    goto :goto_8

    nop

    :goto_6
    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_4

    nop

    :goto_7
    new-instance v0, Lcom/airbnb/lottie/parser/moshi/JsonEncodingException;

    goto :goto_9

    nop

    :goto_8
    invoke-virtual {v1, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_1

    nop

    :goto_9
    new-instance v1, Ljava/lang/StringBuilder;

    goto :goto_6

    nop

    :goto_a
    invoke-direct {v0, p0}, Lcom/airbnb/lottie/parser/moshi/JsonEncodingException;-><init>(Ljava/lang/String;)V

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
