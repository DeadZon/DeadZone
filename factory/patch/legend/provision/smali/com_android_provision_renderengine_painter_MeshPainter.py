TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/renderengine/painter/MeshPainter.smali'
CLASS_FALLBACK_NAMES = ['MeshPainter.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/renderengine/util/BasePainter;']

PATCHES = [
    {
        'id': 'com_android_provision_renderengine_painter_MeshPainter__getPatchAttribute',
        'method': '.method getPatchAttribute(II)V',
        'method_name': 'getPatchAttribute',
        'method_anchors': ['iget-object v1, v0, Lcom/android/provision/renderengine/painter/MeshPainter;->gridPoints:[[Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;', 'iget-object v0, v0, Lcom/android/provision/renderengine/painter/MeshPainter;->patches:[[Lcom/android/provision/renderengine/painter/MeshPainter$Patch;', 'iget v6, v3, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->x:F', 'iget v7, v5, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->x:F', 'iget v12, v2, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->x:F', 'iget v13, v1, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->x:F', 'iget v12, v3, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->dy:F', 'iget v13, v5, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->dy:F'],
        'type': 'method_replace',
        'search': """.method getPatchAttribute(II)V
    .registers 20

    move-object/from16 v0, p0

    iget-object v1, v0, Lcom/android/provision/renderengine/painter/MeshPainter;->gridPoints:[[Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;

    aget-object v2, v1, p1

    aget-object v3, v2, p2

    const/4 v4, 0x1

    add-int/lit8 v5, p1, 0x1

    aget-object v1, v1, v5

    aget-object v5, v1, p2

    add-int/lit8 v6, p2, 0x1

    aget-object v2, v2, v6

    aget-object v1, v1, v6

    iget-object v0, v0, Lcom/android/provision/renderengine/painter/MeshPainter;->patches:[[Lcom/android/provision/renderengine/painter/MeshPainter$Patch;

    aget-object v0, v0, p1

    aget-object v0, v0, p2

    iget v6, v3, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->x:F

    iget v7, v5, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->x:F

    const/4 v8, 0x0

    const/4 v9, 0x4

    new-array v10, v9, [F

    const/4 v11, 0x0

    aput v6, v10, v11

    aput v7, v10, v4

    const/4 v6, 0x2

    aput v8, v10, v6

    const/4 v7, 0x3

    aput v8, v10, v7

    iget v12, v2, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->x:F

    iget v13, v1, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->x:F

    new-array v14, v9, [F

    aput v12, v14, v11

    aput v13, v14, v4

    aput v8, v14, v6

    aput v8, v14, v7

    iget v12, v3, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->dy:F

    iget v13, v5, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->dy:F

    new-array v15, v9, [F

    aput v12, v15, v11

    aput v13, v15, v4

    aput v8, v15, v6

    aput v8, v15, v7

    iget v12, v2, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->dy:F

    iget v13, v1, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->dy:F

    move/from16 v16, v4

    new-array v4, v9, [F

    aput v12, v4, v11

    aput v13, v4, v16

    aput v8, v4, v6

    aput v8, v4, v7

    filled-new-array {v10, v14, v15, v4}, [[F

    move-result-object v4

    iput-object v4, v0, Lcom/android/provision/renderengine/painter/MeshPainter$Patch;->x:[[F

    iget v4, v3, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->y:F

    iget v10, v5, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->y:F

    iget v12, v3, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->dx:F

    iget v13, v5, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->dx:F

    new-array v14, v9, [F

    aput v4, v14, v11

    aput v10, v14, v16

    aput v12, v14, v6

    aput v13, v14, v7

    iget v4, v2, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->y:F

    iget v10, v1, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->y:F

    iget v12, v2, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->dx:F

    iget v13, v1, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->dx:F

    new-array v15, v9, [F

    aput v4, v15, v11

    aput v10, v15, v16

    aput v12, v15, v6

    aput v13, v15, v7

    new-array v4, v9, [F

    fill-array-data v4, :array_0

    new-array v10, v9, [F

    fill-array-data v10, :array_1

    filled-new-array {v14, v15, v4, v10}, [[F

    move-result-object v4

    iput-object v4, v0, Lcom/android/provision/renderengine/painter/MeshPainter$Patch;->y:[[F

    iget v4, v3, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->r:F

    iget v10, v5, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->r:F

    new-array v12, v9, [F

    aput v4, v12, v11

    aput v10, v12, v16

    aput v8, v12, v6

    aput v8, v12, v7

    iget v4, v2, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->r:F

    iget v10, v1, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->r:F

    new-array v13, v9, [F

    aput v4, v13, v11

    aput v10, v13, v16

    aput v8, v13, v6

    aput v8, v13, v7

    new-array v4, v9, [F

    fill-array-data v4, :array_2

    new-array v10, v9, [F

    fill-array-data v10, :array_3

    filled-new-array {v12, v13, v4, v10}, [[F

    move-result-object v4

    iput-object v4, v0, Lcom/android/provision/renderengine/painter/MeshPainter$Patch;->r:[[F

    iget v4, v3, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->g:F

    iget v10, v5, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->g:F

    new-array v12, v9, [F

    aput v4, v12, v11

    aput v10, v12, v16

    aput v8, v12, v6

    aput v8, v12, v7

    iget v4, v2, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->g:F

    iget v10, v1, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->g:F

    new-array v13, v9, [F

    aput v4, v13, v11

    aput v10, v13, v16

    aput v8, v13, v6

    aput v8, v13, v7

    new-array v4, v9, [F

    fill-array-data v4, :array_4

    new-array v10, v9, [F

    fill-array-data v10, :array_5

    filled-new-array {v12, v13, v4, v10}, [[F

    move-result-object v4

    iput-object v4, v0, Lcom/android/provision/renderengine/painter/MeshPainter$Patch;->g:[[F

    iget v3, v3, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->b:F

    iget v4, v5, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->b:F

    new-array v5, v9, [F

    aput v3, v5, v11

    aput v4, v5, v16

    aput v8, v5, v6

    aput v8, v5, v7

    iget v2, v2, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->b:F

    iget v1, v1, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->b:F

    new-array v3, v9, [F

    aput v2, v3, v11

    aput v1, v3, v16

    aput v8, v3, v6

    aput v8, v3, v7

    new-array v1, v9, [F

    fill-array-data v1, :array_6

    new-array v2, v9, [F

    fill-array-data v2, :array_7

    filled-new-array {v5, v3, v1, v2}, [[F

    move-result-object v1

    iput-object v1, v0, Lcom/android/provision/renderengine/painter/MeshPainter$Patch;->b:[[F

    return-void

    nop

    :array_0
    .array-data 4
        0x0
        0x0
        0x0
        0x0
    .end array-data

    :array_1
    .array-data 4
        0x0
        0x0
        0x0
        0x0
    .end array-data

    :array_2
    .array-data 4
        0x0
        0x0
        0x0
        0x0
    .end array-data

    :array_3
    .array-data 4
        0x0
        0x0
        0x0
        0x0
    .end array-data

    :array_4
    .array-data 4
        0x0
        0x0
        0x0
        0x0
    .end array-data

    :array_5
    .array-data 4
        0x0
        0x0
        0x0
        0x0
    .end array-data

    :array_6
    .array-data 4
        0x0
        0x0
        0x0
        0x0
    .end array-data

    :array_7
    .array-data 4
        0x0
        0x0
        0x0
        0x0
    .end array-data
.end method""",
        'replacement': """.method getPatchAttribute(II)V
    .registers 20

    goto :goto_6f

    nop

    :goto_0
    iget v1, v1, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->b:F

    goto :goto_77

    nop

    :goto_1
    aput v4, v5, v16

    goto :goto_76

    nop

    :goto_2
    aput v4, v12, v11

    goto :goto_15

    nop

    :goto_3
    iget v12, v2, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->dy:F

    goto :goto_3f

    nop

    :goto_4
    iget v4, v3, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->r:F

    goto :goto_c

    nop

    :goto_5
    aput v8, v13, v7

    goto :goto_47

    nop

    :goto_6
    aput v8, v13, v6

    goto :goto_35

    nop

    :goto_7
    new-array v1, v9, [F

    fill-array-data v1, :array_6

    goto :goto_10

    nop

    :goto_8
    aget-object v0, v0, p1

    goto :goto_64

    nop

    :goto_9
    new-array v13, v9, [F

    goto :goto_e

    nop

    :goto_a
    aput v8, v14, v7

    goto :goto_5e

    nop

    :goto_b
    aput v10, v13, v16

    goto :goto_33

    nop

    :goto_c
    iget v10, v5, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->r:F

    goto :goto_1f

    nop

    :goto_d
    const/4 v7, 0x3

    goto :goto_1d

    nop

    :goto_e
    aput v4, v13, v11

    goto :goto_62

    nop

    :goto_f
    aput v4, v13, v11

    goto :goto_b

    nop

    :goto_10
    new-array v2, v9, [F

    fill-array-data v2, :array_7

    goto :goto_27

    nop

    :goto_11
    iget v10, v5, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->g:F

    goto :goto_6c

    nop

    :goto_12
    aput v4, v14, v11

    goto :goto_53

    nop

    :goto_13
    new-array v5, v9, [F

    goto :goto_72

    nop

    :goto_14
    aput v4, v12, v11

    goto :goto_18

    nop

    :goto_15
    aput v10, v12, v16

    goto :goto_24

    nop

    :goto_16
    aput v1, v3, v16

    goto :goto_4a

    nop

    :goto_17
    new-array v4, v9, [F

    fill-array-data v4, :array_0

    goto :goto_5f

    nop

    :goto_18
    aput v10, v12, v16

    goto :goto_61

    nop

    :goto_19
    aget-object v1, v1, v5

    goto :goto_3b

    nop

    :goto_1a
    aput v8, v15, v6

    goto :goto_46

    nop

    :goto_1b
    iget-object v0, v0, Lcom/android/provision/renderengine/painter/MeshPainter;->patches:[[Lcom/android/provision/renderengine/painter/MeshPainter$Patch;

    goto :goto_8

    nop

    :goto_1c
    iget v4, v2, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->r:F

    goto :goto_4d

    nop

    :goto_1d
    aput v8, v10, v7

    goto :goto_1e

    nop

    :goto_1e
    iget v12, v2, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->x:F

    goto :goto_60

    nop

    :goto_1f
    new-array v12, v9, [F

    goto :goto_14

    nop

    :goto_20
    aput v8, v4, v6

    goto :goto_4f

    nop

    :goto_21
    iget v4, v2, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->g:F

    goto :goto_75

    nop

    :goto_22
    aput v13, v14, v7

    goto :goto_26

    nop

    :goto_23
    new-array v13, v9, [F

    goto :goto_f

    nop

    :goto_24
    aput v8, v12, v6

    goto :goto_63

    nop

    :goto_25
    aput v13, v4, v16

    goto :goto_20

    nop

    :goto_26
    iget v4, v2, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->y:F

    goto :goto_2f

    nop

    :goto_27
    filled-new-array {v5, v3, v1, v2}, [[F

    move-result-object v1

    goto :goto_30

    nop

    :goto_28
    new-array v14, v9, [F

    goto :goto_6d

    nop

    :goto_29
    aput v6, v10, v11

    goto :goto_52

    nop

    :goto_2a
    iget v7, v5, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->x:F

    goto :goto_4c

    nop

    :goto_2b
    move/from16 v16, v4

    goto :goto_44

    nop

    :goto_2c
    aput v8, v3, v7

    goto :goto_7

    nop

    :goto_2d
    new-array v10, v9, [F

    goto :goto_36

    nop

    :goto_2e
    iget v12, v2, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->dx:F

    goto :goto_5d

    nop

    :goto_2f
    iget v10, v1, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->y:F

    goto :goto_2e

    nop

    :goto_30
    iput-object v1, v0, Lcom/android/provision/renderengine/painter/MeshPainter$Patch;->b:[[F

    goto :goto_5b

    nop

    :goto_31
    iget v4, v5, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->b:F

    goto :goto_13

    nop

    :goto_32
    aput v8, v12, v7

    goto :goto_1c

    nop

    :goto_33
    aput v8, v13, v6

    goto :goto_5

    nop

    :goto_34
    aput v12, v4, v11

    goto :goto_25

    nop

    :goto_35
    aput v8, v13, v7

    goto :goto_45

    nop

    :goto_36
    const/4 v11, 0x0

    goto :goto_29

    nop

    :goto_37
    iget v12, v3, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->dx:F

    goto :goto_7b

    nop

    :goto_38
    aget-object v1, v1, v6

    goto :goto_1b

    nop

    :goto_39
    const/4 v6, 0x2

    goto :goto_7d

    nop

    :goto_3a
    iget v3, v3, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->b:F

    goto :goto_31

    nop

    :goto_3b
    aget-object v5, v1, p2

    goto :goto_73

    nop

    :goto_3c
    filled-new-array {v10, v14, v15, v4}, [[F

    move-result-object v4

    goto :goto_42

    nop

    :goto_3d
    iget-object v1, v0, Lcom/android/provision/renderengine/painter/MeshPainter;->gridPoints:[[Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;

    goto :goto_66

    nop

    :goto_3e
    filled-new-array {v14, v15, v4, v10}, [[F

    move-result-object v4

    goto :goto_50

    nop

    :goto_3f
    iget v13, v1, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->dy:F

    goto :goto_2b

    nop

    :goto_40
    aput v4, v15, v11

    goto :goto_7e

    nop

    :goto_41
    aput v2, v3, v11

    goto :goto_16

    nop

    :goto_42
    iput-object v4, v0, Lcom/android/provision/renderengine/painter/MeshPainter$Patch;->x:[[F

    goto :goto_57

    nop

    :goto_43
    aput v12, v15, v11

    goto :goto_79

    nop

    :goto_44
    new-array v4, v9, [F

    goto :goto_34

    nop

    :goto_45
    new-array v4, v9, [F

    fill-array-data v4, :array_4

    goto :goto_7a

    nop

    :goto_46
    aput v8, v15, v7

    goto :goto_3

    nop

    :goto_47
    new-array v4, v9, [F

    fill-array-data v4, :array_2

    goto :goto_78

    nop

    :goto_48
    filled-new-array {v12, v13, v4, v10}, [[F

    move-result-object v4

    goto :goto_6e

    nop

    :goto_49
    iget v2, v2, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->b:F

    goto :goto_0

    nop

    :goto_4a
    aput v8, v3, v6

    goto :goto_2c

    nop

    :goto_4b
    const/4 v9, 0x4

    goto :goto_2d

    nop

    :goto_4c
    const/4 v8, 0x0

    goto :goto_4b

    nop

    :goto_4d
    iget v10, v1, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->r:F

    goto :goto_23

    nop

    :goto_4e
    const/4 v4, 0x1

    goto :goto_68

    nop

    :goto_4f
    aput v8, v4, v7

    goto :goto_3c

    nop

    :goto_50
    iput-object v4, v0, Lcom/android/provision/renderengine/painter/MeshPainter$Patch;->y:[[F

    goto :goto_4

    nop

    :goto_51
    iget v4, v3, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->g:F

    goto :goto_11

    nop

    :goto_52
    aput v7, v10, v4

    goto :goto_39

    nop

    :goto_53
    aput v10, v14, v16

    goto :goto_69

    nop

    :goto_54
    aput v8, v5, v7

    goto :goto_49

    nop

    :goto_55
    new-array v15, v9, [F

    goto :goto_40

    nop

    :goto_56
    aput v8, v14, v6

    goto :goto_a

    nop

    :goto_57
    iget v4, v3, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->y:F

    goto :goto_6a

    nop

    :goto_58
    filled-new-array {v12, v13, v4, v10}, [[F

    move-result-object v4

    goto :goto_67

    nop

    :goto_59
    aget-object v3, v2, p2

    goto :goto_4e

    nop

    :goto_5a
    aget-object v2, v2, v6

    goto :goto_38

    nop

    :goto_5b
    return-void

    :array_0
    .array-data 4
        0x0
        0x0
        0x0
        0x0
    .end array-data

    :array_1
    .array-data 4
        0x0
        0x0
        0x0
        0x0
    .end array-data

    :array_2
    .array-data 4
        0x0
        0x0
        0x0
        0x0
    .end array-data

    :array_3
    .array-data 4
        0x0
        0x0
        0x0
        0x0
    .end array-data

    :array_4
    .array-data 4
        0x0
        0x0
        0x0
        0x0
    .end array-data

    :array_5
    .array-data 4
        0x0
        0x0
        0x0
        0x0
    .end array-data

    :array_6
    .array-data 4
        0x0
        0x0
        0x0
        0x0
    .end array-data

    :array_7
    .array-data 4
        0x0
        0x0
        0x0
        0x0
    .end array-data

    :goto_5c
    aput v13, v14, v4

    goto :goto_56

    nop

    :goto_5d
    iget v13, v1, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->dx:F

    goto :goto_55

    nop

    :goto_5e
    iget v12, v3, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->dy:F

    goto :goto_6b

    nop

    :goto_5f
    new-array v10, v9, [F

    fill-array-data v10, :array_1

    goto :goto_3e

    nop

    :goto_60
    iget v13, v1, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->x:F

    goto :goto_28

    nop

    :goto_61
    aput v8, v12, v6

    goto :goto_32

    nop

    :goto_62
    aput v10, v13, v16

    goto :goto_6

    nop

    :goto_63
    aput v8, v12, v7

    goto :goto_21

    nop

    :goto_64
    aget-object v0, v0, p2

    goto :goto_74

    nop

    :goto_65
    new-array v14, v9, [F

    goto :goto_12

    nop

    :goto_66
    aget-object v2, v1, p1

    goto :goto_59

    nop

    :goto_67
    iput-object v4, v0, Lcom/android/provision/renderengine/painter/MeshPainter$Patch;->r:[[F

    goto :goto_51

    nop

    :goto_68
    add-int/lit8 v5, p1, 0x1

    goto :goto_19

    nop

    :goto_69
    aput v12, v14, v6

    goto :goto_22

    nop

    :goto_6a
    iget v10, v5, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->y:F

    goto :goto_37

    nop

    :goto_6b
    iget v13, v5, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->dy:F

    goto :goto_7c

    nop

    :goto_6c
    new-array v12, v9, [F

    goto :goto_2

    nop

    :goto_6d
    aput v12, v14, v11

    goto :goto_5c

    nop

    :goto_6e
    iput-object v4, v0, Lcom/android/provision/renderengine/painter/MeshPainter$Patch;->g:[[F

    goto :goto_3a

    nop

    :goto_6f
    move-object/from16 v0, p0

    goto :goto_3d

    nop

    :goto_70
    aput v12, v15, v6

    goto :goto_71

    nop

    :goto_71
    aput v13, v15, v7

    goto :goto_17

    nop

    :goto_72
    aput v3, v5, v11

    goto :goto_1

    nop

    :goto_73
    add-int/lit8 v6, p2, 0x1

    goto :goto_5a

    nop

    :goto_74
    iget v6, v3, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->x:F

    goto :goto_2a

    nop

    :goto_75
    iget v10, v1, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->g:F

    goto :goto_9

    nop

    :goto_76
    aput v8, v5, v6

    goto :goto_54

    nop

    :goto_77
    new-array v3, v9, [F

    goto :goto_41

    nop

    :goto_78
    new-array v10, v9, [F

    fill-array-data v10, :array_3

    goto :goto_58

    nop

    :goto_79
    aput v13, v15, v4

    goto :goto_1a

    nop

    :goto_7a
    new-array v10, v9, [F

    fill-array-data v10, :array_5

    goto :goto_48

    nop

    :goto_7b
    iget v13, v5, Lcom/android/provision/renderengine/painter/MeshPainter$GridPoint;->dx:F

    goto :goto_65

    nop

    :goto_7c
    new-array v15, v9, [F

    goto :goto_43

    nop

    :goto_7d
    aput v8, v10, v6

    goto :goto_d

    nop

    :goto_7e
    aput v10, v15, v16

    goto :goto_70

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_renderengine_painter_MeshPainter__getFragId',
        'method': '.method protected getFragId()I',
        'method_name': 'getFragId',
        'method_anchors': ['sget p0, Lcom/android/provision/R$raw;->mesh_fragment_shader:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected getFragId()I
    .registers 1

    sget p0, Lcom/android/provision/R$raw;->mesh_fragment_shader:I

    return p0
.end method""",
        'replacement': """.method protected getFragId()I
    .registers 1

    goto :goto_0

    nop

    :goto_0
    sget p0, Lcom/android/provision/R$raw;->mesh_fragment_shader:I

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
        'id': 'com_android_provision_renderengine_painter_MeshPainter__getVertId',
        'method': '.method protected getVertId()I',
        'method_name': 'getVertId',
        'method_anchors': ['sget p0, Lcom/android/provision/R$raw;->mesh_vertex_shader:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected getVertId()I
    .registers 1

    sget p0, Lcom/android/provision/R$raw;->mesh_vertex_shader:I

    return p0
.end method""",
        'replacement': """.method protected getVertId()I
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    sget p0, Lcom/android/provision/R$raw;->mesh_vertex_shader:I

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
