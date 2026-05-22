TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/controller/StateHelper.smali'
CLASS_FALLBACK_NAMES = ['StateHelper.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field static final DEFAULT_INT_PROPERTY:Lmiuix/animation/property/IntValueProperty;', '.field static final DEFAULT_PROPERTY:Lmiuix/animation/property/ValueProperty;']

PATCHES = [
    {
        'id': 'miuix_animation_controller_StateHelper__parse',
        'method': '.method varargs parse(Lmiuix/animation/IAnimTarget;Lmiuix/animation/controller/AnimState;Lmiuix/animation/base/AnimConfigLink;Z[Ljava/lang/Object;)V',
        'method_name': 'parse',
        'method_anchors': ['if-nez v0, :cond_0', 'if-eqz v1, :cond_1', 'invoke-virtual {p2}, Lmiuix/animation/controller/AnimState;->getTag()Ljava/lang/Object;', 'invoke-virtual {v1, v2}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z', 'if-eqz v1, :cond_1', 'if-ge v7, v0, :cond_7', 'if-eqz p4, :cond_4', 'if-ge v1, v2, :cond_2'],
        'type': 'method_replace',
        'search': """.method varargs parse(Lmiuix/animation/IAnimTarget;Lmiuix/animation/controller/AnimState;Lmiuix/animation/base/AnimConfigLink;Z[Ljava/lang/Object;)V
    .registers 16

    array-length v0, p5

    if-nez v0, :cond_0

    goto :goto_3

    :cond_0
    const/4 v0, 0x0

    aget-object v1, p5, v0

    const/4 v9, 0x1

    if-eqz v1, :cond_1

    invoke-virtual {p2}, Lmiuix/animation/controller/AnimState;->getTag()Ljava/lang/Object;

    move-result-object v2

    invoke-virtual {v1, v2}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_1

    move v0, v9

    :cond_1
    move v7, v0

    :goto_0
    array-length v0, p5

    if-ge v7, v0, :cond_7

    aget-object v4, p5, v7

    const/4 v0, 0x0

    if-eqz p4, :cond_4

    add-int/lit8 v1, v7, 0x1

    array-length v2, p5

    if-ge v1, v2, :cond_2

    aget-object v2, p5, v1

    goto :goto_1

    :cond_2
    move-object v2, v0

    :goto_1
    instance-of v3, v4, Ljava/lang/String;

    if-eqz v3, :cond_3

    instance-of v3, v2, Ljava/lang/String;

    if-eqz v3, :cond_3

    move v7, v1

    goto :goto_0

    :cond_3
    const/4 v1, 0x2

    move-object v5, v2

    goto :goto_2

    :cond_4
    move-object v5, v0

    move v1, v9

    :goto_2
    add-int/2addr v1, v7

    array-length v2, p5

    if-ge v1, v2, :cond_5

    aget-object v0, p5, v1

    :cond_5
    move-object v6, v0

    instance-of v0, v4, Ljava/lang/String;

    if-eqz v0, :cond_6

    instance-of v0, v6, Ljava/lang/String;

    if-eqz v0, :cond_6

    add-int/lit8 v7, v7, 0x1

    goto :goto_0

    :cond_6
    move-object v0, p0

    move-object v1, p1

    move-object v2, p2

    move-object v3, p3

    move-object v8, p5

    invoke-direct/range {v0 .. v8}, Lmiuix/animation/controller/StateHelper;->setPropertyAndValue(Lmiuix/animation/IAnimTarget;Lmiuix/animation/controller/AnimState;Lmiuix/animation/base/AnimConfigLink;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;I[Ljava/lang/Object;)I

    move-result v7

    goto :goto_0

    :cond_7
    :goto_3
    return-void
.end method""",
        'replacement': """.method varargs parse(Lmiuix/animation/IAnimTarget;Lmiuix/animation/controller/AnimState;Lmiuix/animation/base/AnimConfigLink;Z[Ljava/lang/Object;)V
    .registers 16

    goto :goto_30

    nop

    :goto_0
    const/4 v0, 0x0

    goto :goto_39

    nop

    :goto_1
    return-void

    :goto_2
    if-nez v0, :cond_0

    goto :goto_18

    :cond_0
    goto :goto_a

    nop

    :goto_3
    aget-object v1, p5, v0

    goto :goto_1c

    nop

    :goto_4
    if-nez v0, :cond_1

    goto :goto_18

    :cond_1
    goto :goto_2f

    nop

    :goto_5
    goto :goto_16

    :goto_6
    goto :goto_3a

    nop

    :goto_7
    array-length v2, p5

    goto :goto_2a

    nop

    :goto_8
    if-lt v7, v0, :cond_2

    goto :goto_33

    :cond_2
    goto :goto_31

    nop

    :goto_9
    const/4 v1, 0x2

    goto :goto_23

    nop

    :goto_a
    instance-of v0, v6, Ljava/lang/String;

    goto :goto_4

    nop

    :goto_b
    array-length v2, p5

    goto :goto_20

    nop

    :goto_c
    move-object v6, v0

    goto :goto_2e

    nop

    :goto_d
    if-eqz v0, :cond_3

    goto :goto_37

    :cond_3
    goto :goto_36

    nop

    :goto_e
    add-int/lit8 v1, v7, 0x1

    goto :goto_7

    nop

    :goto_f
    goto :goto_28

    :goto_10
    goto :goto_9

    nop

    :goto_11
    aget-object v0, p5, v1

    :goto_12
    goto :goto_c

    nop

    :goto_13
    move-object v2, p2

    goto :goto_19

    nop

    :goto_14
    move-object v8, p5

    goto :goto_24

    nop

    :goto_15
    move v1, v9

    :goto_16
    goto :goto_3f

    nop

    :goto_17
    goto :goto_28

    :goto_18
    goto :goto_2c

    nop

    :goto_19
    move-object v3, p3

    goto :goto_14

    nop

    :goto_1a
    move v0, v9

    :goto_1b
    goto :goto_27

    nop

    :goto_1c
    const/4 v9, 0x1

    goto :goto_2b

    nop

    :goto_1d
    if-nez v3, :cond_4

    goto :goto_10

    :cond_4
    goto :goto_21

    nop

    :goto_1e
    move-object v2, v0

    :goto_1f
    goto :goto_38

    nop

    :goto_20
    if-lt v1, v2, :cond_5

    goto :goto_12

    :cond_5
    goto :goto_11

    nop

    :goto_21
    move v7, v1

    goto :goto_f

    nop

    :goto_22
    if-nez v1, :cond_6

    goto :goto_1b

    :cond_6
    goto :goto_1a

    nop

    :goto_23
    move-object v5, v2

    goto :goto_5

    nop

    :goto_24
    invoke-direct/range {v0 .. v8}, Lmiuix/animation/controller/StateHelper;->setPropertyAndValue(Lmiuix/animation/IAnimTarget;Lmiuix/animation/controller/AnimState;Lmiuix/animation/base/AnimConfigLink;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;I[Ljava/lang/Object;)I

    move-result v7

    goto :goto_32

    nop

    :goto_25
    if-nez v3, :cond_7

    goto :goto_10

    :cond_7
    goto :goto_35

    nop

    :goto_26
    invoke-virtual {v1, v2}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v1

    goto :goto_22

    nop

    :goto_27
    move v7, v0

    :goto_28
    goto :goto_2d

    nop

    :goto_29
    aget-object v2, p5, v1

    goto :goto_3c

    nop

    :goto_2a
    if-lt v1, v2, :cond_8

    goto :goto_3d

    :cond_8
    goto :goto_29

    nop

    :goto_2b
    if-nez v1, :cond_9

    goto :goto_1b

    :cond_9
    goto :goto_3b

    nop

    :goto_2c
    move-object v0, p0

    goto :goto_3e

    nop

    :goto_2d
    array-length v0, p5

    goto :goto_8

    nop

    :goto_2e
    instance-of v0, v4, Ljava/lang/String;

    goto :goto_2

    nop

    :goto_2f
    add-int/lit8 v7, v7, 0x1

    goto :goto_17

    nop

    :goto_30
    array-length v0, p5

    goto :goto_d

    nop

    :goto_31
    aget-object v4, p5, v7

    goto :goto_0

    nop

    :goto_32
    goto :goto_28

    :goto_33
    goto :goto_1

    nop

    :goto_34
    const/4 v0, 0x0

    goto :goto_3

    nop

    :goto_35
    instance-of v3, v2, Ljava/lang/String;

    goto :goto_1d

    nop

    :goto_36
    goto :goto_33

    :goto_37
    goto :goto_34

    nop

    :goto_38
    instance-of v3, v4, Ljava/lang/String;

    goto :goto_25

    nop

    :goto_39
    if-nez p4, :cond_a

    goto :goto_6

    :cond_a
    goto :goto_e

    nop

    :goto_3a
    move-object v5, v0

    goto :goto_15

    nop

    :goto_3b
    invoke-virtual {p2}, Lmiuix/animation/controller/AnimState;->getTag()Ljava/lang/Object;

    move-result-object v2

    goto :goto_26

    nop

    :goto_3c
    goto :goto_1f

    :goto_3d
    goto :goto_1e

    nop

    :goto_3e
    move-object v1, p1

    goto :goto_13

    nop

    :goto_3f
    add-int/2addr v1, v7

    goto :goto_b

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
