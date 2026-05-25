TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/ble/miconnect/MiConnectAdvData$tlv.smali'
CLASS_FALLBACK_NAMES = ['MiConnectAdvData$tlv.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'com_android_provision_ble_miconnect_MiConnectAdvData__tlv__getByteArrayValue',
        'method': '.method getByteArrayValue()[B',
        'method_name': 'getByteArrayValue',
        'method_anchors': ['iget-object p0, p0, Lcom/android/provision/ble/miconnect/MiConnectAdvData$tlv;->value:[B', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method getByteArrayValue()[B
    .registers 1

    iget-object p0, p0, Lcom/android/provision/ble/miconnect/MiConnectAdvData$tlv;->value:[B

    return-object p0
.end method""",
        'replacement': """.method getByteArrayValue()[B
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p0, Lcom/android/provision/ble/miconnect/MiConnectAdvData$tlv;->value:[B

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
        'id': 'com_android_provision_ble_miconnect_MiConnectAdvData__tlv__getByteValue',
        'method': '.method getByteValue(I)B',
        'method_name': 'getByteValue',
        'method_anchors': ['iget-object p0, p0, Lcom/android/provision/ble/miconnect/MiConnectAdvData$tlv;->value:[B', 'if-ge p1, v0, :cond_0', 'return p0', 'return p0'],
        'type': 'method_replace',
        'search': """.method getByteValue(I)B
    .registers 3

    iget-object p0, p0, Lcom/android/provision/ble/miconnect/MiConnectAdvData$tlv;->value:[B

    array-length v0, p0

    if-ge p1, v0, :cond_0

    aget-byte p0, p0, p1

    return p0

    :cond_0
    const/16 p0, 0x7f

    return p0
.end method""",
        'replacement': """.method getByteValue(I)B
    .registers 3

    goto :goto_3

    nop

    :goto_0
    return p0

    :goto_1
    if-lt p1, v0, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_6

    nop

    :goto_2
    array-length v0, p0

    goto :goto_1

    nop

    :goto_3
    iget-object p0, p0, Lcom/android/provision/ble/miconnect/MiConnectAdvData$tlv;->value:[B

    goto :goto_2

    nop

    :goto_4
    return p0

    :goto_5
    goto :goto_7

    nop

    :goto_6
    aget-byte p0, p0, p1

    goto :goto_4

    nop

    :goto_7
    const/16 p0, 0x7f

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_ble_miconnect_MiConnectAdvData__tlv__getIntArrayValue',
        'method': '.method getIntArrayValue()[I',
        'method_name': 'getIntArrayValue',
        'method_anchors': ['iget-object p0, p0, Lcom/android/provision/ble/miconnect/MiConnectAdvData$tlv;->value:[B', 'invoke-static {p0}, Lcom/android/provision/ble/miconnect/TypeUtil;->toIntArray([B)[I', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method getIntArrayValue()[I
    .registers 1

    iget-object p0, p0, Lcom/android/provision/ble/miconnect/MiConnectAdvData$tlv;->value:[B

    invoke-static {p0}, Lcom/android/provision/ble/miconnect/TypeUtil;->toIntArray([B)[I

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method getIntArrayValue()[I
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    iget-object p0, p0, Lcom/android/provision/ble/miconnect/MiConnectAdvData$tlv;->value:[B

    goto :goto_2

    nop

    :goto_2
    invoke-static {p0}, Lcom/android/provision/ble/miconnect/TypeUtil;->toIntArray([B)[I

    move-result-object p0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_ble_miconnect_MiConnectAdvData__tlv__getIntArrayValueLast',
        'method': '.method getIntArrayValueLast()I',
        'method_name': 'getIntArrayValueLast',
        'method_anchors': ['iget-object v0, p0, Lcom/android/provision/ble/miconnect/MiConnectAdvData$tlv;->value:[B', 'invoke-static {v0}, Lcom/android/provision/ble/miconnect/TypeUtil;->toIntArray([B)[I', 'iget-object p0, p0, Lcom/android/provision/ble/miconnect/MiConnectAdvData$tlv;->value:[B', 'invoke-static {p0}, Lcom/android/provision/ble/miconnect/TypeUtil;->toIntArray([B)[I', 'return p0'],
        'type': 'method_replace',
        'search': """.method getIntArrayValueLast()I
    .registers 2

    iget-object v0, p0, Lcom/android/provision/ble/miconnect/MiConnectAdvData$tlv;->value:[B

    invoke-static {v0}, Lcom/android/provision/ble/miconnect/TypeUtil;->toIntArray([B)[I

    move-result-object v0

    iget-object p0, p0, Lcom/android/provision/ble/miconnect/MiConnectAdvData$tlv;->value:[B

    invoke-static {p0}, Lcom/android/provision/ble/miconnect/TypeUtil;->toIntArray([B)[I

    move-result-object p0

    array-length p0, p0

    add-int/lit8 p0, p0, -0x1

    aget p0, v0, p0

    return p0
.end method""",
        'replacement': """.method getIntArrayValueLast()I
    .registers 2

    goto :goto_0

    nop

    :goto_0
    iget-object v0, p0, Lcom/android/provision/ble/miconnect/MiConnectAdvData$tlv;->value:[B

    goto :goto_3

    nop

    :goto_1
    invoke-static {p0}, Lcom/android/provision/ble/miconnect/TypeUtil;->toIntArray([B)[I

    move-result-object p0

    goto :goto_7

    nop

    :goto_2
    aget p0, v0, p0

    goto :goto_6

    nop

    :goto_3
    invoke-static {v0}, Lcom/android/provision/ble/miconnect/TypeUtil;->toIntArray([B)[I

    move-result-object v0

    goto :goto_5

    nop

    :goto_4
    add-int/lit8 p0, p0, -0x1

    goto :goto_2

    nop

    :goto_5
    iget-object p0, p0, Lcom/android/provision/ble/miconnect/MiConnectAdvData$tlv;->value:[B

    goto :goto_1

    nop

    :goto_6
    return p0

    :goto_7
    array-length p0, p0

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_ble_miconnect_MiConnectAdvData__tlv__getIntValue',
        'method': '.method getIntValue(I)I',
        'method_name': 'getIntValue',
        'method_anchors': ['iget-object p0, p0, Lcom/android/provision/ble/miconnect/MiConnectAdvData$tlv;->value:[B', 'if-ge p1, v0, :cond_4', 'if-ge p1, v0, :cond_0', 'if-ge v2, v3, :cond_1', 'if-ge v2, v3, :cond_2', 'if-ge p1, v2, :cond_3', 'return p0', 'return p0'],
        'type': 'method_replace',
        'search': """.method getIntValue(I)I
    .registers 6

    iget-object p0, p0, Lcom/android/provision/ble/miconnect/MiConnectAdvData$tlv;->value:[B

    array-length v0, p0

    add-int/lit8 v0, v0, 0x3

    div-int/lit8 v0, v0, 0x4

    if-ge p1, v0, :cond_4

    mul-int/lit8 p1, p1, 0x4

    array-length v0, p0

    const/4 v1, 0x0

    if-ge p1, v0, :cond_0

    aget-byte v0, p0, p1

    and-int/lit16 v0, v0, 0xff

    goto :goto_0

    :cond_0
    move v0, v1

    :goto_0
    add-int/lit8 v2, p1, 0x1

    array-length v3, p0

    if-ge v2, v3, :cond_1

    aget-byte v2, p0, v2

    and-int/lit16 v2, v2, 0xff

    goto :goto_1

    :cond_1
    move v2, v1

    :goto_1
    shl-int/lit8 v2, v2, 0x8

    or-int/2addr v0, v2

    add-int/lit8 v2, p1, 0x2

    array-length v3, p0

    if-ge v2, v3, :cond_2

    aget-byte v2, p0, v2

    and-int/lit16 v2, v2, 0xff

    goto :goto_2

    :cond_2
    move v2, v1

    :goto_2
    shl-int/lit8 v2, v2, 0x10

    or-int/2addr v0, v2

    add-int/lit8 p1, p1, 0x3

    array-length v2, p0

    if-ge p1, v2, :cond_3

    aget-byte p0, p0, p1

    and-int/lit16 v1, p0, 0xff

    :cond_3
    shl-int/lit8 p0, v1, 0x18

    or-int/2addr p0, v0

    return p0

    :cond_4
    const p0, 0x7fffffff

    return p0
.end method""",
        'replacement': """.method getIntValue(I)I
    .registers 6

    goto :goto_16

    nop

    :goto_0
    goto :goto_29

    :goto_1
    goto :goto_28

    nop

    :goto_2
    add-int/lit8 v2, p1, 0x1

    goto :goto_13

    nop

    :goto_3
    shl-int/lit8 v2, v2, 0x10

    goto :goto_2a

    nop

    :goto_4
    aget-byte v0, p0, p1

    goto :goto_c

    nop

    :goto_5
    if-lt p1, v2, :cond_0

    goto :goto_10

    :cond_0
    goto :goto_15

    nop

    :goto_6
    const/4 v1, 0x0

    goto :goto_2d

    nop

    :goto_7
    add-int/lit8 v2, p1, 0x2

    goto :goto_17

    nop

    :goto_8
    and-int/lit16 v2, v2, 0xff

    goto :goto_11

    nop

    :goto_9
    move v2, v1

    :goto_a
    goto :goto_3

    nop

    :goto_b
    div-int/lit8 v0, v0, 0x4

    goto :goto_24

    nop

    :goto_c
    and-int/lit16 v0, v0, 0xff

    goto :goto_0

    nop

    :goto_d
    aget-byte v2, p0, v2

    goto :goto_8

    nop

    :goto_e
    add-int/lit8 p1, p1, 0x3

    goto :goto_23

    nop

    :goto_f
    and-int/lit16 v1, p0, 0xff

    :goto_10
    goto :goto_27

    nop

    :goto_11
    goto :goto_a

    :goto_12
    goto :goto_9

    nop

    :goto_13
    array-length v3, p0

    goto :goto_2f

    nop

    :goto_14
    add-int/lit8 v0, v0, 0x3

    goto :goto_b

    nop

    :goto_15
    aget-byte p0, p0, p1

    goto :goto_f

    nop

    :goto_16
    iget-object p0, p0, Lcom/android/provision/ble/miconnect/MiConnectAdvData$tlv;->value:[B

    goto :goto_18

    nop

    :goto_17
    array-length v3, p0

    goto :goto_22

    nop

    :goto_18
    array-length v0, p0

    goto :goto_14

    nop

    :goto_19
    and-int/lit16 v2, v2, 0xff

    goto :goto_1a

    nop

    :goto_1a
    goto :goto_26

    :goto_1b
    goto :goto_25

    nop

    :goto_1c
    mul-int/lit8 p1, p1, 0x4

    goto :goto_2b

    nop

    :goto_1d
    or-int/2addr v0, v2

    goto :goto_7

    nop

    :goto_1e
    return p0

    :goto_1f
    goto :goto_20

    nop

    :goto_20
    const p0, 0x7fffffff

    goto :goto_21

    nop

    :goto_21
    return p0

    :goto_22
    if-lt v2, v3, :cond_1

    goto :goto_12

    :cond_1
    goto :goto_d

    nop

    :goto_23
    array-length v2, p0

    goto :goto_5

    nop

    :goto_24
    if-lt p1, v0, :cond_2

    goto :goto_1f

    :cond_2
    goto :goto_1c

    nop

    :goto_25
    move v2, v1

    :goto_26
    goto :goto_2e

    nop

    :goto_27
    shl-int/lit8 p0, v1, 0x18

    goto :goto_2c

    nop

    :goto_28
    move v0, v1

    :goto_29
    goto :goto_2

    nop

    :goto_2a
    or-int/2addr v0, v2

    goto :goto_e

    nop

    :goto_2b
    array-length v0, p0

    goto :goto_6

    nop

    :goto_2c
    or-int/2addr p0, v0

    goto :goto_1e

    nop

    :goto_2d
    if-lt p1, v0, :cond_3

    goto :goto_1

    :cond_3
    goto :goto_4

    nop

    :goto_2e
    shl-int/lit8 v2, v2, 0x8

    goto :goto_1d

    nop

    :goto_2f
    if-lt v2, v3, :cond_4

    goto :goto_1b

    :cond_4
    goto :goto_30

    nop

    :goto_30
    aget-byte v2, p0, v2

    goto :goto_19

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_ble_miconnect_MiConnectAdvData__tlv__getType',
        'method': '.method getType()I',
        'method_name': 'getType',
        'method_anchors': ['iget p0, p0, Lcom/android/provision/ble/miconnect/MiConnectAdvData$tlv;->type:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method getType()I
    .registers 1

    iget p0, p0, Lcom/android/provision/ble/miconnect/MiConnectAdvData$tlv;->type:I

    return p0
.end method""",
        'replacement': """.method getType()I
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    iget p0, p0, Lcom/android/provision/ble/miconnect/MiConnectAdvData$tlv;->type:I

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
