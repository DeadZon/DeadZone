TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/visual/check/FlowLayout.smali'
CLASS_FALLBACK_NAMES = ['FlowLayout.smali']
CLASS_ANCHORS = ['.super Landroid/view/ViewGroup;']

PATCHES = [
    {
        'id': 'miuix_visual_check_FlowLayout__onLayout',
        'method': '.method protected onLayout(ZIIII)V',
        'method_name': 'onLayout',
        'method_anchors': ['invoke-virtual {v0}, Landroid/view/ViewGroup;->getChildCount()I', 'if-nez v1, :cond_0', 'invoke-static {v0}, Landroidx/core/view/ViewCompat;->getLayoutDirection(Landroid/view/View;)I', 'if-ne v1, v8, :cond_1', 'if-eqz v1, :cond_2', 'invoke-virtual {v0}, Landroid/view/ViewGroup;->getPaddingRight()I', 'invoke-virtual {v0}, Landroid/view/ViewGroup;->getPaddingLeft()I', 'if-eqz v1, :cond_3'],
        'type': 'method_replace',
        'search': """.method protected onLayout(ZIIII)V
    .registers 24

    move-object/from16 v0, p0

    invoke-virtual {v0}, Landroid/view/ViewGroup;->getChildCount()I

    move-result v1

    if-nez v1, :cond_0

    goto :goto_c

    :cond_0
    invoke-static {v0}, Landroidx/core/view/ViewCompat;->getLayoutDirection(Landroid/view/View;)I

    move-result v1

    const/4 v8, 0x1

    if-ne v1, v8, :cond_1

    move v1, v8

    goto :goto_0

    :cond_1
    const/4 v1, 0x0

    :goto_0
    if-eqz v1, :cond_2

    invoke-virtual {v0}, Landroid/view/ViewGroup;->getPaddingRight()I

    move-result v2

    :goto_1
    move v9, v2

    goto :goto_2

    :cond_2
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getPaddingLeft()I

    move-result v2

    goto :goto_1

    :goto_2
    if-eqz v1, :cond_3

    invoke-virtual {v0}, Landroid/view/ViewGroup;->getPaddingLeft()I

    move-result v2

    goto :goto_3

    :cond_3
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getPaddingRight()I

    move-result v2

    :goto_3
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getPaddingTop()I

    move-result v3

    move v4, v3

    invoke-virtual {v0}, Landroid/view/ViewGroup;->getMeasuredWidth()I

    move-result v3

    sub-int v10, v3, v2

    move v11, v4

    move v5, v9

    move v14, v10

    const/4 v6, 0x0

    const/4 v12, 0x0

    const/4 v13, 0x0

    const/4 v15, 0x0

    :goto_4
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getChildCount()I

    move-result v7

    if-ge v12, v7, :cond_b

    invoke-virtual {v0, v12}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;

    move-result-object v7

    invoke-virtual {v7}, Landroid/view/View;->getVisibility()I

    move-result v8

    move/from16 p3, v1

    const/16 v1, 0x8

    if-ne v8, v1, :cond_4

    move/from16 v1, p3

    const/4 v8, 0x1

    goto :goto_b

    :cond_4
    invoke-virtual {v7}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v1

    instance-of v8, v1, Landroid/view/ViewGroup$MarginLayoutParams;

    if-eqz v8, :cond_5

    check-cast v1, Landroid/view/ViewGroup$MarginLayoutParams;

    invoke-static {v1}, Landroidx/core/view/MarginLayoutParamsCompat;->getMarginStart(Landroid/view/ViewGroup$MarginLayoutParams;)I

    move-result v8

    invoke-static {v1}, Landroidx/core/view/MarginLayoutParamsCompat;->getMarginEnd(Landroid/view/ViewGroup$MarginLayoutParams;)I

    move-result v1

    move/from16 v16, v8

    move v8, v1

    goto :goto_5

    :cond_5
    const/4 v8, 0x0

    const/16 v16, 0x0

    :goto_5
    add-int v1, v5, v16

    invoke-virtual {v7}, Landroid/view/View;->getMeasuredWidth()I

    move-result v17

    add-int v1, v1, v17

    move/from16 p4, v2

    iget-boolean v2, v0, Lmiuix/visual/check/FlowLayout;->singleLine:Z

    if-nez v2, :cond_6

    if-le v1, v10, :cond_6

    iget v1, v0, Lmiuix/visual/check/FlowLayout;->lineSpacing:I

    add-int v4, v11, v1

    move/from16 v17, v9

    move v2, v12

    :goto_6
    move v1, v4

    goto :goto_7

    :cond_6
    move/from16 v17, v5

    move v2, v6

    goto :goto_6

    :goto_7
    add-int v4, v17, v16

    invoke-virtual {v7}, Landroid/view/View;->getMeasuredWidth()I

    move-result v5

    add-int/2addr v5, v4

    invoke-virtual {v7}, Landroid/view/View;->getMeasuredHeight()I

    move-result v6

    add-int/2addr v6, v1

    if-eqz p3, :cond_7

    sub-int v4, v3, v5

    sub-int v5, v3, v17

    sub-int v5, v5, v16

    invoke-virtual {v7, v4, v1, v5, v6}, Landroid/view/View;->layout(IIII)V

    goto :goto_8

    :cond_7
    invoke-virtual {v7, v4, v1, v5, v6}, Landroid/view/View;->layout(IIII)V

    :goto_8
    iget v4, v0, Lmiuix/visual/check/FlowLayout;->mLineGravity:I

    const/4 v5, 0x1

    if-eq v4, v5, :cond_8

    if-ne v2, v12, :cond_8

    if-eqz v2, :cond_8

    :goto_9
    if-ge v13, v2, :cond_8

    move v4, v6

    invoke-virtual {v0, v13}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;

    move-result-object v6

    move v5, v15

    move v15, v1

    move/from16 v1, p3

    move-object/from16 p3, v7

    move v7, v4

    move v4, v14

    move v14, v2

    move/from16 v2, p4

    invoke-direct/range {v0 .. v6}, Lmiuix/visual/check/FlowLayout;->offsetView(ZIIIILandroid/view/View;)V

    add-int/lit8 v13, v13, 0x1

    move v6, v7

    move v2, v14

    move-object/from16 v7, p3

    move/from16 p3, v1

    move v14, v4

    move v1, v15

    move v15, v5

    goto :goto_9

    :cond_8
    move v15, v1

    move v14, v2

    move/from16 v1, p3

    move/from16 v2, p4

    move-object/from16 p3, v7

    move v7, v6

    add-int v16, v16, v8

    invoke-virtual/range {p3 .. p3}, Landroid/view/View;->getMeasuredWidth()I

    move-result v4

    add-int v16, v16, v4

    iget v4, v0, Lmiuix/visual/check/FlowLayout;->itemSpacing:I

    add-int v16, v16, v4

    add-int v5, v17, v16

    sub-int v4, v10, v5

    iget v6, v0, Lmiuix/visual/check/FlowLayout;->mLineGravity:I

    const/4 v8, 0x1

    if-eq v6, v8, :cond_9

    invoke-virtual {v0}, Landroid/view/ViewGroup;->getChildCount()I

    move-result v6

    sub-int/2addr v6, v8

    if-ne v12, v6, :cond_9

    move v13, v14

    :goto_a
    if-gt v13, v12, :cond_9

    invoke-virtual {v0, v13}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;

    move-result-object v6

    invoke-direct/range {v0 .. v6}, Lmiuix/visual/check/FlowLayout;->offsetView(ZIIIILandroid/view/View;)V

    add-int/lit8 v13, v13, 0x1

    move-object/from16 v0, p0

    goto :goto_a

    :cond_9
    if-ge v11, v7, :cond_a

    move v11, v7

    :cond_a
    move v6, v14

    move v13, v6

    move v14, v4

    move v4, v15

    move v15, v5

    :goto_b
    add-int/lit8 v12, v12, 0x1

    move-object/from16 v0, p0

    goto :goto_4

    :cond_b
    :goto_c
    return-void
.end method""",
        'replacement': """.method protected onLayout(ZIIII)V
    .registers 24

    goto :goto_4e

    nop

    :goto_0
    add-int v16, v16, v4

    goto :goto_2b

    nop

    :goto_1
    move/from16 v17, v9

    goto :goto_f

    nop

    :goto_2
    goto :goto_8b

    :goto_3
    goto :goto_98

    nop

    :goto_4
    goto :goto_85

    :goto_5
    goto :goto_1e

    nop

    :goto_6
    goto :goto_78

    :goto_7
    goto :goto_5e

    nop

    :goto_8
    add-int/lit8 v12, v12, 0x1

    goto :goto_1d

    nop

    :goto_9
    goto :goto_9e

    :goto_a
    goto :goto_d

    nop

    :goto_b
    goto :goto_3d

    :goto_c
    goto :goto_a0

    nop

    :goto_d
    if-lt v11, v7, :cond_0

    goto :goto_a5

    :cond_0
    goto :goto_a4

    nop

    :goto_e
    if-nez v1, :cond_1

    goto :goto_2a

    :cond_1
    goto :goto_70

    nop

    :goto_f
    move v2, v12

    :goto_10
    goto :goto_7e

    nop

    :goto_11
    move/from16 v2, p4

    goto :goto_67

    nop

    :goto_12
    if-ne v6, v8, :cond_2

    goto :goto_a

    :cond_2
    goto :goto_35

    nop

    :goto_13
    invoke-static {v0}, Landroidx/core/view/ViewCompat;->getLayoutDirection(Landroid/view/View;)I

    move-result v1

    goto :goto_4f

    nop

    :goto_14
    goto :goto_73

    :goto_15
    goto :goto_19

    nop

    :goto_16
    move-object/from16 p3, v7

    goto :goto_8e

    nop

    :goto_17
    const/16 v16, 0x0

    :goto_18
    goto :goto_27

    nop

    :goto_19
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getPaddingLeft()I

    move-result v2

    goto :goto_72

    nop

    :goto_1a
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getMeasuredWidth()I

    move-result v3

    goto :goto_41

    nop

    :goto_1b
    check-cast v1, Landroid/view/ViewGroup$MarginLayoutParams;

    goto :goto_43

    nop

    :goto_1c
    move/from16 v16, v8

    goto :goto_7b

    nop

    :goto_1d
    move-object/from16 v0, p0

    goto :goto_2

    nop

    :goto_1e
    move/from16 v17, v5

    goto :goto_42

    nop

    :goto_1f
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getPaddingTop()I

    move-result v3

    goto :goto_59

    nop

    :goto_20
    move/from16 p4, v2

    goto :goto_a1

    nop

    :goto_21
    add-int v4, v11, v1

    goto :goto_1

    nop

    :goto_22
    goto :goto_49

    :goto_23
    goto :goto_48

    nop

    :goto_24
    move v13, v6

    goto :goto_6d

    nop

    :goto_25
    move v14, v4

    goto :goto_8d

    nop

    :goto_26
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getChildCount()I

    move-result v7

    goto :goto_3e

    nop

    :goto_27
    add-int v1, v5, v16

    goto :goto_95

    nop

    :goto_28
    if-ne v4, v5, :cond_3

    goto :goto_7

    :cond_3
    goto :goto_82

    nop

    :goto_29
    goto :goto_4b

    :goto_2a
    goto :goto_4a

    nop

    :goto_2b
    add-int v5, v17, v16

    goto :goto_6a

    nop

    :goto_2c
    if-lt v13, v2, :cond_4

    goto :goto_7

    :cond_4
    goto :goto_4d

    nop

    :goto_2d
    if-nez p3, :cond_5

    goto :goto_66

    :cond_5
    goto :goto_9c

    nop

    :goto_2e
    move v14, v10

    goto :goto_40

    nop

    :goto_2f
    move/from16 v2, p4

    goto :goto_52

    nop

    :goto_30
    add-int v16, v16, v8

    goto :goto_86

    nop

    :goto_31
    add-int v16, v16, v4

    goto :goto_54

    nop

    :goto_32
    instance-of v8, v1, Landroid/view/ViewGroup$MarginLayoutParams;

    goto :goto_91

    nop

    :goto_33
    add-int/lit8 v13, v13, 0x1

    goto :goto_57

    nop

    :goto_34
    move-object/from16 v7, p3

    goto :goto_7a

    nop

    :goto_35
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getChildCount()I

    move-result v6

    goto :goto_6b

    nop

    :goto_36
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getChildCount()I

    move-result v1

    goto :goto_93

    nop

    :goto_37
    move v15, v1

    goto :goto_99

    nop

    :goto_38
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getPaddingRight()I

    move-result v2

    :goto_39
    goto :goto_47

    nop

    :goto_3a
    const/4 v8, 0x1

    goto :goto_12

    nop

    :goto_3b
    invoke-virtual {v0, v13}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;

    move-result-object v6

    goto :goto_9a

    nop

    :goto_3c
    move v15, v5

    :goto_3d
    goto :goto_8

    nop

    :goto_3e
    if-lt v12, v7, :cond_6

    goto :goto_3

    :cond_6
    goto :goto_80

    nop

    :goto_3f
    invoke-virtual {v7}, Landroid/view/View;->getMeasuredHeight()I

    move-result v6

    goto :goto_83

    nop

    :goto_40
    const/4 v6, 0x0

    goto :goto_5c

    nop

    :goto_41
    sub-int v10, v3, v2

    goto :goto_74

    nop

    :goto_42
    move v2, v6

    goto :goto_84

    nop

    :goto_43
    invoke-static {v1}, Landroidx/core/view/MarginLayoutParamsCompat;->getMarginStart(Landroid/view/ViewGroup$MarginLayoutParams;)I

    move-result v8

    goto :goto_5a

    nop

    :goto_44
    const/4 v13, 0x0

    goto :goto_8a

    nop

    :goto_45
    invoke-virtual {v0, v13}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;

    move-result-object v6

    goto :goto_75

    nop

    :goto_46
    invoke-virtual {v7}, Landroid/view/View;->getMeasuredWidth()I

    move-result v5

    goto :goto_58

    nop

    :goto_47
    move v9, v2

    goto :goto_14

    nop

    :goto_48
    const/4 v1, 0x0

    :goto_49
    goto :goto_8c

    nop

    :goto_4a
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getPaddingRight()I

    move-result v2

    :goto_4b
    goto :goto_1f

    nop

    :goto_4c
    iget v6, v0, Lmiuix/visual/check/FlowLayout;->mLineGravity:I

    goto :goto_3a

    nop

    :goto_4d
    move v4, v6

    goto :goto_3b

    nop

    :goto_4e
    move-object/from16 v0, p0

    goto :goto_36

    nop

    :goto_4f
    const/4 v8, 0x1

    goto :goto_96

    nop

    :goto_50
    if-eq v12, v6, :cond_7

    goto :goto_a

    :cond_7
    goto :goto_9d

    nop

    :goto_51
    const/4 v8, 0x1

    goto :goto_b

    nop

    :goto_52
    move-object/from16 p3, v7

    goto :goto_7f

    nop

    :goto_53
    add-int v4, v17, v16

    goto :goto_46

    nop

    :goto_54
    iget v4, v0, Lmiuix/visual/check/FlowLayout;->itemSpacing:I

    goto :goto_0

    nop

    :goto_55
    const/16 v1, 0x8

    goto :goto_9f

    nop

    :goto_56
    move/from16 v1, p3

    goto :goto_51

    nop

    :goto_57
    move v6, v7

    goto :goto_9b

    nop

    :goto_58
    add-int/2addr v5, v4

    goto :goto_3f

    nop

    :goto_59
    move v4, v3

    goto :goto_1a

    nop

    :goto_5a
    invoke-static {v1}, Landroidx/core/view/MarginLayoutParamsCompat;->getMarginEnd(Landroid/view/ViewGroup$MarginLayoutParams;)I

    move-result v1

    goto :goto_1c

    nop

    :goto_5b
    move-object/from16 v0, p0

    goto :goto_9

    nop

    :goto_5c
    const/4 v12, 0x0

    goto :goto_44

    nop

    :goto_5d
    move v14, v2

    goto :goto_81

    nop

    :goto_5e
    move v15, v1

    goto :goto_5d

    nop

    :goto_5f
    const/4 v8, 0x0

    goto :goto_17

    nop

    :goto_60
    sub-int v5, v5, v16

    goto :goto_69

    nop

    :goto_61
    goto :goto_18

    :goto_62
    goto :goto_5f

    nop

    :goto_63
    if-gt v1, v10, :cond_8

    goto :goto_5

    :cond_8
    goto :goto_a2

    nop

    :goto_64
    if-eqz v2, :cond_9

    goto :goto_5

    :cond_9
    goto :goto_63

    nop

    :goto_65
    goto :goto_89

    :goto_66
    goto :goto_88

    nop

    :goto_67
    invoke-direct/range {v0 .. v6}, Lmiuix/visual/check/FlowLayout;->offsetView(ZIIIILandroid/view/View;)V

    goto :goto_33

    nop

    :goto_68
    add-int/lit8 v13, v13, 0x1

    goto :goto_5b

    nop

    :goto_69
    invoke-virtual {v7, v4, v1, v5, v6}, Landroid/view/View;->layout(IIII)V

    goto :goto_65

    nop

    :goto_6a
    sub-int v4, v10, v5

    goto :goto_4c

    nop

    :goto_6b
    sub-int/2addr v6, v8

    goto :goto_50

    nop

    :goto_6c
    move v4, v15

    goto :goto_3c

    nop

    :goto_6d
    move v14, v4

    goto :goto_6c

    nop

    :goto_6e
    move v15, v5

    goto :goto_6

    nop

    :goto_6f
    invoke-virtual {v7}, Landroid/view/View;->getVisibility()I

    move-result v8

    goto :goto_97

    nop

    :goto_70
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getPaddingLeft()I

    move-result v2

    goto :goto_29

    nop

    :goto_71
    iget v4, v0, Lmiuix/visual/check/FlowLayout;->mLineGravity:I

    goto :goto_87

    nop

    :goto_72
    goto :goto_39

    :goto_73
    goto :goto_e

    nop

    :goto_74
    move v11, v4

    goto :goto_7c

    nop

    :goto_75
    invoke-direct/range {v0 .. v6}, Lmiuix/visual/check/FlowLayout;->offsetView(ZIIIILandroid/view/View;)V

    goto :goto_68

    nop

    :goto_76
    add-int v1, v1, v17

    goto :goto_20

    nop

    :goto_77
    if-nez v2, :cond_a

    goto :goto_7

    :cond_a
    :goto_78
    goto :goto_2c

    nop

    :goto_79
    move v6, v14

    goto :goto_24

    nop

    :goto_7a
    move/from16 p3, v1

    goto :goto_25

    nop

    :goto_7b
    move v8, v1

    goto :goto_61

    nop

    :goto_7c
    move v5, v9

    goto :goto_2e

    nop

    :goto_7d
    move v4, v14

    goto :goto_a3

    nop

    :goto_7e
    move v1, v4

    goto :goto_4

    nop

    :goto_7f
    move v7, v6

    goto :goto_30

    nop

    :goto_80
    invoke-virtual {v0, v12}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;

    move-result-object v7

    goto :goto_6f

    nop

    :goto_81
    move/from16 v1, p3

    goto :goto_2f

    nop

    :goto_82
    if-eq v2, v12, :cond_b

    goto :goto_7

    :cond_b
    goto :goto_77

    nop

    :goto_83
    add-int/2addr v6, v1

    goto :goto_2d

    nop

    :goto_84
    goto :goto_10

    :goto_85
    goto :goto_53

    nop

    :goto_86
    invoke-virtual/range {p3 .. p3}, Landroid/view/View;->getMeasuredWidth()I

    move-result v4

    goto :goto_31

    nop

    :goto_87
    const/4 v5, 0x1

    goto :goto_28

    nop

    :goto_88
    invoke-virtual {v7, v4, v1, v5, v6}, Landroid/view/View;->layout(IIII)V

    :goto_89
    goto :goto_71

    nop

    :goto_8a
    const/4 v15, 0x0

    :goto_8b
    goto :goto_26

    nop

    :goto_8c
    if-nez v1, :cond_c

    goto :goto_15

    :cond_c
    goto :goto_38

    nop

    :goto_8d
    move v1, v15

    goto :goto_6e

    nop

    :goto_8e
    move v7, v4

    goto :goto_7d

    nop

    :goto_8f
    goto :goto_3

    :goto_90
    goto :goto_13

    nop

    :goto_91
    if-nez v8, :cond_d

    goto :goto_62

    :cond_d
    goto :goto_1b

    nop

    :goto_92
    if-le v13, v12, :cond_e

    goto :goto_a

    :cond_e
    goto :goto_45

    nop

    :goto_93
    if-eqz v1, :cond_f

    goto :goto_90

    :cond_f
    goto :goto_8f

    nop

    :goto_94
    sub-int v5, v3, v17

    goto :goto_60

    nop

    :goto_95
    invoke-virtual {v7}, Landroid/view/View;->getMeasuredWidth()I

    move-result v17

    goto :goto_76

    nop

    :goto_96
    if-eq v1, v8, :cond_10

    goto :goto_23

    :cond_10
    goto :goto_a6

    nop

    :goto_97
    move/from16 p3, v1

    goto :goto_55

    nop

    :goto_98
    return-void

    :goto_99
    move/from16 v1, p3

    goto :goto_16

    nop

    :goto_9a
    move v5, v15

    goto :goto_37

    nop

    :goto_9b
    move v2, v14

    goto :goto_34

    nop

    :goto_9c
    sub-int v4, v3, v5

    goto :goto_94

    nop

    :goto_9d
    move v13, v14

    :goto_9e
    goto :goto_92

    nop

    :goto_9f
    if-eq v8, v1, :cond_11

    goto :goto_c

    :cond_11
    goto :goto_56

    nop

    :goto_a0
    invoke-virtual {v7}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v1

    goto :goto_32

    nop

    :goto_a1
    iget-boolean v2, v0, Lmiuix/visual/check/FlowLayout;->singleLine:Z

    goto :goto_64

    nop

    :goto_a2
    iget v1, v0, Lmiuix/visual/check/FlowLayout;->lineSpacing:I

    goto :goto_21

    nop

    :goto_a3
    move v14, v2

    goto :goto_11

    nop

    :goto_a4
    move v11, v7

    :goto_a5
    goto :goto_79

    nop

    :goto_a6
    move v1, v8

    goto :goto_22

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_visual_check_FlowLayout__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['invoke-static/range {p1 .. p1}, Landroid/view/View$MeasureSpec;->getSize(I)I', 'invoke-static/range {p1 .. p1}, Landroid/view/View$MeasureSpec;->getMode(I)I', 'invoke-static/range {p2 .. p2}, Landroid/view/View$MeasureSpec;->getSize(I)I', 'invoke-static/range {p2 .. p2}, Landroid/view/View$MeasureSpec;->getMode(I)I', 'if-eq v2, v5, :cond_1', 'if-ne v2, v5, :cond_0', 'invoke-virtual {v0}, Landroid/view/ViewGroup;->getPaddingLeft()I', 'invoke-virtual {v0}, Landroid/view/ViewGroup;->getPaddingTop()I'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 22

    move-object/from16 v0, p0

    invoke-static/range {p1 .. p1}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v1

    invoke-static/range {p1 .. p1}, Landroid/view/View$MeasureSpec;->getMode(I)I

    move-result v2

    invoke-static/range {p2 .. p2}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v3

    invoke-static/range {p2 .. p2}, Landroid/view/View$MeasureSpec;->getMode(I)I

    move-result v4

    const/high16 v5, -0x80000000

    if-eq v2, v5, :cond_1

    const/high16 v5, 0x40000000

    if-ne v2, v5, :cond_0

    goto :goto_0

    :cond_0
    const v5, 0x7fffffff

    goto :goto_1

    :cond_1
    :goto_0
    move v5, v1

    :goto_1
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getPaddingLeft()I

    move-result v6

    invoke-virtual {v0}, Landroid/view/ViewGroup;->getPaddingTop()I

    move-result v7

    invoke-virtual {v0}, Landroid/view/ViewGroup;->getPaddingRight()I

    move-result v8

    sub-int/2addr v5, v8

    move v9, v7

    const/4 v10, 0x0

    const/4 v11, 0x0

    :goto_2
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getChildCount()I

    move-result v12

    if-ge v10, v12, :cond_8

    invoke-virtual {v0, v10}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;

    move-result-object v12

    invoke-virtual {v12}, Landroid/view/View;->getVisibility()I

    move-result v13

    const/16 v14, 0x8

    if-ne v13, v14, :cond_2

    move/from16 v13, p1

    move/from16 v14, p2

    move/from16 v18, v5

    goto :goto_5

    :cond_2
    move/from16 v13, p1

    move/from16 v14, p2

    invoke-virtual {v0, v12, v13, v14}, Landroid/view/ViewGroup;->measureChild(Landroid/view/View;II)V

    invoke-virtual {v12}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v15

    instance-of v8, v15, Landroid/view/ViewGroup$MarginLayoutParams;

    if-eqz v8, :cond_3

    check-cast v15, Landroid/view/ViewGroup$MarginLayoutParams;

    iget v8, v15, Landroid/view/ViewGroup$MarginLayoutParams;->leftMargin:I

    iget v15, v15, Landroid/view/ViewGroup$MarginLayoutParams;->rightMargin:I

    goto :goto_3

    :cond_3
    const/4 v8, 0x0

    const/4 v15, 0x0

    :goto_3
    add-int v16, v6, v8

    invoke-virtual {v12}, Landroid/view/View;->getMeasuredWidth()I

    move-result v17

    move/from16 v18, v6

    add-int v6, v16, v17

    if-le v6, v5, :cond_4

    iget-boolean v6, v0, Lmiuix/visual/check/FlowLayout;->singleLine:Z

    if-nez v6, :cond_4

    invoke-virtual {v0}, Landroid/view/ViewGroup;->getPaddingLeft()I

    move-result v6

    iget v9, v0, Lmiuix/visual/check/FlowLayout;->lineSpacing:I

    add-int/2addr v9, v7

    goto :goto_4

    :cond_4
    move/from16 v6, v18

    :goto_4
    add-int v16, v6, v8

    invoke-virtual {v12}, Landroid/view/View;->getMeasuredWidth()I

    move-result v17

    move/from16 v18, v5

    add-int v5, v16, v17

    invoke-virtual {v12}, Landroid/view/View;->getMeasuredHeight()I

    move-result v16

    move/from16 v17, v6

    add-int v6, v9, v16

    if-le v5, v11, :cond_5

    move v11, v5

    :cond_5
    add-int/2addr v8, v15

    invoke-virtual {v12}, Landroid/view/View;->getMeasuredWidth()I

    move-result v5

    add-int/2addr v8, v5

    iget v5, v0, Lmiuix/visual/check/FlowLayout;->itemSpacing:I

    add-int/2addr v8, v5

    add-int v5, v17, v8

    invoke-virtual {v0}, Landroid/view/ViewGroup;->getChildCount()I

    move-result v8

    add-int/lit8 v8, v8, -0x1

    if-ne v10, v8, :cond_6

    add-int/2addr v11, v15

    :cond_6
    if-ge v7, v6, :cond_7

    move v7, v6

    :cond_7
    move v6, v5

    :goto_5
    add-int/lit8 v10, v10, 0x1

    move/from16 v5, v18

    goto :goto_2

    :cond_8
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getPaddingRight()I

    move-result v5

    add-int/2addr v11, v5

    invoke-virtual {v0}, Landroid/view/ViewGroup;->getPaddingBottom()I

    move-result v5

    add-int/2addr v7, v5

    invoke-static {v1, v2, v11}, Lmiuix/visual/check/FlowLayout;->getMeasuredDimension(III)I

    move-result v1

    invoke-static {v3, v4, v7}, Lmiuix/visual/check/FlowLayout;->getMeasuredDimension(III)I

    move-result v2

    invoke-virtual {v0, v1, v2}, Landroid/view/ViewGroup;->setMeasuredDimension(II)V

    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 22

    goto :goto_e

    nop

    :goto_0
    return-void

    :goto_1
    add-int/2addr v8, v5

    goto :goto_a

    nop

    :goto_2
    add-int v16, v6, v8

    goto :goto_5b

    nop

    :goto_3
    move v5, v1

    :goto_4
    goto :goto_60

    nop

    :goto_5
    move/from16 v14, p2

    goto :goto_3f

    nop

    :goto_6
    add-int/2addr v11, v5

    goto :goto_4c

    nop

    :goto_7
    const/16 v14, 0x8

    goto :goto_61

    nop

    :goto_8
    add-int/2addr v11, v15

    :goto_9
    goto :goto_2e

    nop

    :goto_a
    add-int v5, v17, v8

    goto :goto_51

    nop

    :goto_b
    invoke-static/range {p2 .. p2}, Landroid/view/View$MeasureSpec;->getMode(I)I

    move-result v4

    goto :goto_5d

    nop

    :goto_c
    add-int v16, v6, v8

    goto :goto_25

    nop

    :goto_d
    add-int/2addr v7, v5

    goto :goto_14

    nop

    :goto_e
    move-object/from16 v0, p0

    goto :goto_5a

    nop

    :goto_f
    invoke-virtual {v12}, Landroid/view/View;->getMeasuredWidth()I

    move-result v5

    goto :goto_3d

    nop

    :goto_10
    if-eq v2, v5, :cond_0

    goto :goto_20

    :cond_0
    goto :goto_1f

    nop

    :goto_11
    invoke-virtual {v12}, Landroid/view/View;->getMeasuredHeight()I

    move-result v16

    goto :goto_17

    nop

    :goto_12
    sub-int/2addr v5, v8

    goto :goto_5c

    nop

    :goto_13
    invoke-static/range {p2 .. p2}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v3

    goto :goto_b

    nop

    :goto_14
    invoke-static {v1, v2, v11}, Lmiuix/visual/check/FlowLayout;->getMeasuredDimension(III)I

    move-result v1

    goto :goto_24

    nop

    :goto_15
    move/from16 v13, p1

    goto :goto_5

    nop

    :goto_16
    if-ne v2, v5, :cond_1

    goto :goto_1b

    :cond_1
    goto :goto_31

    nop

    :goto_17
    move/from16 v17, v6

    goto :goto_4e

    nop

    :goto_18
    move/from16 v13, p1

    goto :goto_3b

    nop

    :goto_19
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getPaddingLeft()I

    move-result v6

    goto :goto_3c

    nop

    :goto_1a
    goto :goto_4

    :goto_1b
    goto :goto_3

    nop

    :goto_1c
    move/from16 v18, v6

    goto :goto_63

    nop

    :goto_1d
    move v7, v6

    :goto_1e
    goto :goto_46

    nop

    :goto_1f
    goto :goto_1b

    :goto_20
    goto :goto_43

    nop

    :goto_21
    iget v5, v0, Lmiuix/visual/check/FlowLayout;->itemSpacing:I

    goto :goto_1

    nop

    :goto_22
    invoke-static/range {p1 .. p1}, Landroid/view/View$MeasureSpec;->getMode(I)I

    move-result v2

    goto :goto_13

    nop

    :goto_23
    add-int/lit8 v10, v10, 0x1

    goto :goto_52

    nop

    :goto_24
    invoke-static {v3, v4, v7}, Lmiuix/visual/check/FlowLayout;->getMeasuredDimension(III)I

    move-result v2

    goto :goto_30

    nop

    :goto_25
    invoke-virtual {v12}, Landroid/view/View;->getMeasuredWidth()I

    move-result v17

    goto :goto_2f

    nop

    :goto_26
    if-gt v5, v11, :cond_2

    goto :goto_45

    :cond_2
    goto :goto_44

    nop

    :goto_27
    iget v8, v15, Landroid/view/ViewGroup$MarginLayoutParams;->leftMargin:I

    goto :goto_2d

    nop

    :goto_28
    add-int v5, v16, v17

    goto :goto_11

    nop

    :goto_29
    invoke-virtual {v12}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v15

    goto :goto_3a

    nop

    :goto_2a
    invoke-virtual {v0, v10}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;

    move-result-object v12

    goto :goto_4b

    nop

    :goto_2b
    goto :goto_47

    :goto_2c
    goto :goto_15

    nop

    :goto_2d
    iget v15, v15, Landroid/view/ViewGroup$MarginLayoutParams;->rightMargin:I

    goto :goto_53

    nop

    :goto_2e
    if-lt v7, v6, :cond_3

    goto :goto_1e

    :cond_3
    goto :goto_1d

    nop

    :goto_2f
    move/from16 v18, v5

    goto :goto_28

    nop

    :goto_30
    invoke-virtual {v0, v1, v2}, Landroid/view/ViewGroup;->setMeasuredDimension(II)V

    goto :goto_0

    nop

    :goto_31
    const/high16 v5, 0x40000000

    goto :goto_10

    nop

    :goto_32
    const/4 v10, 0x0

    goto :goto_4f

    nop

    :goto_33
    if-gt v6, v5, :cond_4

    goto :goto_4a

    :cond_4
    goto :goto_38

    nop

    :goto_34
    move/from16 v6, v18

    :goto_35
    goto :goto_c

    nop

    :goto_36
    if-eq v10, v8, :cond_5

    goto :goto_9

    :cond_5
    goto :goto_8

    nop

    :goto_37
    if-nez v8, :cond_6

    goto :goto_54

    :cond_6
    goto :goto_39

    nop

    :goto_38
    iget-boolean v6, v0, Lmiuix/visual/check/FlowLayout;->singleLine:Z

    goto :goto_5f

    nop

    :goto_39
    check-cast v15, Landroid/view/ViewGroup$MarginLayoutParams;

    goto :goto_27

    nop

    :goto_3a
    instance-of v8, v15, Landroid/view/ViewGroup$MarginLayoutParams;

    goto :goto_37

    nop

    :goto_3b
    move/from16 v14, p2

    goto :goto_41

    nop

    :goto_3c
    iget v9, v0, Lmiuix/visual/check/FlowLayout;->lineSpacing:I

    goto :goto_62

    nop

    :goto_3d
    add-int/2addr v8, v5

    goto :goto_21

    nop

    :goto_3e
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getPaddingRight()I

    move-result v8

    goto :goto_12

    nop

    :goto_3f
    invoke-virtual {v0, v12, v13, v14}, Landroid/view/ViewGroup;->measureChild(Landroid/view/View;II)V

    goto :goto_29

    nop

    :goto_40
    add-int/lit8 v8, v8, -0x1

    goto :goto_36

    nop

    :goto_41
    move/from16 v18, v5

    goto :goto_2b

    nop

    :goto_42
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getChildCount()I

    move-result v12

    goto :goto_48

    nop

    :goto_43
    const v5, 0x7fffffff

    goto :goto_1a

    nop

    :goto_44
    move v11, v5

    :goto_45
    goto :goto_64

    nop

    :goto_46
    move v6, v5

    :goto_47
    goto :goto_23

    nop

    :goto_48
    if-lt v10, v12, :cond_7

    goto :goto_59

    :cond_7
    goto :goto_2a

    nop

    :goto_49
    goto :goto_35

    :goto_4a
    goto :goto_34

    nop

    :goto_4b
    invoke-virtual {v12}, Landroid/view/View;->getVisibility()I

    move-result v13

    goto :goto_7

    nop

    :goto_4c
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getPaddingBottom()I

    move-result v5

    goto :goto_d

    nop

    :goto_4d
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getPaddingRight()I

    move-result v5

    goto :goto_6

    nop

    :goto_4e
    add-int v6, v9, v16

    goto :goto_26

    nop

    :goto_4f
    const/4 v11, 0x0

    :goto_50
    goto :goto_42

    nop

    :goto_51
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getChildCount()I

    move-result v8

    goto :goto_40

    nop

    :goto_52
    move/from16 v5, v18

    goto :goto_58

    nop

    :goto_53
    goto :goto_57

    :goto_54
    goto :goto_5e

    nop

    :goto_55
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getPaddingTop()I

    move-result v7

    goto :goto_3e

    nop

    :goto_56
    const/4 v15, 0x0

    :goto_57
    goto :goto_2

    nop

    :goto_58
    goto :goto_50

    :goto_59
    goto :goto_4d

    nop

    :goto_5a
    invoke-static/range {p1 .. p1}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v1

    goto :goto_22

    nop

    :goto_5b
    invoke-virtual {v12}, Landroid/view/View;->getMeasuredWidth()I

    move-result v17

    goto :goto_1c

    nop

    :goto_5c
    move v9, v7

    goto :goto_32

    nop

    :goto_5d
    const/high16 v5, -0x80000000

    goto :goto_16

    nop

    :goto_5e
    const/4 v8, 0x0

    goto :goto_56

    nop

    :goto_5f
    if-eqz v6, :cond_8

    goto :goto_4a

    :cond_8
    goto :goto_19

    nop

    :goto_60
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getPaddingLeft()I

    move-result v6

    goto :goto_55

    nop

    :goto_61
    if-eq v13, v14, :cond_9

    goto :goto_2c

    :cond_9
    goto :goto_18

    nop

    :goto_62
    add-int/2addr v9, v7

    goto :goto_49

    nop

    :goto_63
    add-int v6, v16, v17

    goto :goto_33

    nop

    :goto_64
    add-int/2addr v8, v15

    goto :goto_f

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
