TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/pickerwidget/widget/NumberPickerGroup.smali'
CLASS_FALLBACK_NAMES = ['NumberPickerGroup.smali']
CLASS_ANCHORS = ['.super Landroid/widget/LinearLayout;']

PATCHES = [
    {
        'id': 'miuix_pickerwidget_widget_NumberPickerGroup__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['invoke-super {p0, p1, p2}, Landroid/widget/LinearLayout;->onMeasure(II)V', 'invoke-virtual {p0}, Landroid/widget/LinearLayout;->getOrientation()I', 'if-nez p1, :cond_7', 'invoke-virtual {p0}, Landroid/widget/LinearLayout;->getChildCount()I', 'if-ge v1, p1, :cond_2', 'invoke-virtual {p0, v1}, Landroid/widget/LinearLayout;->getChildAt(I)Landroid/view/View;', 'if-eqz v8, :cond_1', 'check-cast v7, Lmiuix/pickerwidget/widget/NumberPicker;'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 14

    invoke-super {p0, p1, p2}, Landroid/widget/LinearLayout;->onMeasure(II)V

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getOrientation()I

    move-result p1

    if-nez p1, :cond_7

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getChildCount()I

    move-result p1

    const/4 p2, 0x0

    const/4 v0, 0x0

    move v1, p2

    move v6, v1

    move v2, v0

    move v3, v2

    move v4, v3

    move v5, v4

    :goto_0
    if-ge v1, p1, :cond_2

    invoke-virtual {p0, v1}, Landroid/widget/LinearLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v7

    instance-of v8, v7, Lmiuix/pickerwidget/widget/NumberPicker;

    if-eqz v8, :cond_1

    check-cast v7, Lmiuix/pickerwidget/widget/NumberPicker;

    invoke-virtual {v7}, Lmiuix/pickerwidget/widget/NumberPicker;->getDisplayedMaxTextWidth()F

    move-result v8

    add-float/2addr v5, v8

    invoke-virtual {v7}, Lmiuix/pickerwidget/widget/NumberPicker;->getOriginalLabelWidth()F

    move-result v8

    cmpl-float v9, v8, v0

    if-lez v9, :cond_0

    add-float/2addr v3, v8

    invoke-virtual {v7}, Lmiuix/pickerwidget/widget/NumberPicker;->getMarginLabelLeft()I

    move-result v8

    int-to-float v8, v8

    add-float/2addr v4, v8

    :cond_0
    invoke-virtual {v7}, Lmiuix/pickerwidget/widget/NumberPicker;->getOriginTextSizeHighlight()I

    move-result v7

    int-to-float v7, v7

    invoke-static {v2, v7}, Ljava/lang/Math;->max(FF)F

    move-result v2

    goto :goto_1

    :cond_1
    invoke-virtual {v7}, Landroid/view/View;->getMeasuredWidth()I

    move-result v7

    add-int/2addr v6, v7

    :goto_1
    add-int/lit8 v1, v1, 0x1

    goto :goto_0

    :cond_2
    iget-object v1, p0, Lmiuix/pickerwidget/widget/NumberPickerGroup;->mValuePaint:Landroid/graphics/Paint;

    invoke-virtual {v1, v2}, Landroid/graphics/Paint;->setTextSize(F)V

    iget-object v1, p0, Lmiuix/pickerwidget/widget/NumberPickerGroup;->mValuePaint:Landroid/graphics/Paint;

    const-string v7, "    "

    invoke-virtual {v1, v7}, Landroid/graphics/Paint;->measureText(Ljava/lang/String;)F

    move-result v1

    const/high16 v7, 0x40000000

    mul-float/2addr v3, v7

    mul-float/2addr v4, v7

    add-float/2addr v5, v3

    add-float/2addr v5, v1

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getMeasuredWidth()I

    move-result v3

    sub-int/2addr v3, v6

    int-to-float v3, v3

    sub-float/2addr v3, v4

    div-float v4, v3, v5

    const/high16 v6, 0x3f800000

    cmpg-float v6, v4, v6

    if-gez v6, :cond_3

    mul-float/2addr v4, v2

    goto :goto_2

    :cond_3
    move v4, v2

    :goto_2
    cmpg-float v6, v4, v2

    if-gtz v6, :cond_7

    :goto_3
    if-ge p2, p1, :cond_7

    invoke-virtual {p0, p2}, Landroid/widget/LinearLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v6

    instance-of v8, v6, Lmiuix/pickerwidget/widget/NumberPicker;

    if-eqz v8, :cond_6

    move-object v8, v6

    check-cast v8, Lmiuix/pickerwidget/widget/NumberPicker;

    float-to-int v9, v4

    invoke-virtual {v8, v9}, Lmiuix/pickerwidget/widget/NumberPicker;->setTextSizeHighlight(I)V

    invoke-virtual {v8}, Lmiuix/pickerwidget/widget/NumberPicker;->getOriginTextSizeHint()I

    move-result v9

    int-to-float v9, v9

    mul-float/2addr v9, v4

    div-float/2addr v9, v2

    float-to-int v9, v9

    invoke-virtual {v8, v9}, Lmiuix/pickerwidget/widget/NumberPicker;->setTextSizeHint(I)V

    invoke-virtual {v8}, Lmiuix/pickerwidget/widget/NumberPicker;->getOriginalLabelWidth()F

    move-result v9

    cmpl-float v9, v9, v0

    if-lez v9, :cond_4

    invoke-virtual {v8}, Lmiuix/pickerwidget/widget/NumberPicker;->getMarginLabelLeft()I

    move-result v9

    mul-int/lit8 v9, v9, 0x2

    int-to-float v9, v9

    goto :goto_4

    :cond_4
    move v9, v0

    :goto_4
    invoke-direct {p0, v8}, Lmiuix/pickerwidget/widget/NumberPickerGroup;->isDayNumberPicker(Lmiuix/pickerwidget/widget/NumberPicker;)Z

    move-result v10

    if-eqz v10, :cond_5

    invoke-virtual {v8}, Lmiuix/pickerwidget/widget/NumberPicker;->getDisplayedMaxTextWidth()F

    move-result v10

    add-float/2addr v10, v1

    invoke-virtual {v8}, Lmiuix/pickerwidget/widget/NumberPicker;->getOriginalLabelWidth()F

    move-result v8

    :goto_5
    mul-float/2addr v8, v7

    add-float/2addr v10, v8

    mul-float/2addr v10, v3

    div-float/2addr v10, v5

    add-float/2addr v9, v10

    float-to-int v8, v9

    goto :goto_6

    :cond_5
    invoke-virtual {v8}, Lmiuix/pickerwidget/widget/NumberPicker;->getDisplayedMaxTextWidth()F

    move-result v10

    invoke-virtual {v8}, Lmiuix/pickerwidget/widget/NumberPicker;->getOriginalLabelWidth()F

    move-result v8

    goto :goto_5

    :goto_6
    invoke-virtual {v6}, Landroid/view/View;->getMeasuredHeight()I

    move-result v9

    const/high16 v10, 0x40000000

    invoke-static {v8, v10}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v8

    invoke-static {v9, v10}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v9

    invoke-virtual {v6, v8, v9}, Landroid/view/View;->measure(II)V

    :cond_6
    add-int/lit8 p2, p2, 0x1

    goto :goto_3

    :cond_7
    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 14

    goto :goto_1d

    nop

    :goto_0
    div-float/2addr v9, v2

    goto :goto_44

    nop

    :goto_1
    if-nez v8, :cond_0

    goto :goto_41

    :cond_0
    goto :goto_57

    nop

    :goto_2
    int-to-float v3, v3

    goto :goto_45

    nop

    :goto_3
    add-float/2addr v3, v8

    goto :goto_1e

    nop

    :goto_4
    add-float/2addr v5, v1

    goto :goto_67

    nop

    :goto_5
    add-int/lit8 v1, v1, 0x1

    goto :goto_4b

    nop

    :goto_6
    mul-float/2addr v9, v4

    goto :goto_0

    nop

    :goto_7
    const/4 v0, 0x0

    goto :goto_d

    nop

    :goto_8
    invoke-virtual {v7}, Landroid/view/View;->getMeasuredWidth()I

    move-result v7

    goto :goto_4d

    nop

    :goto_9
    instance-of v8, v7, Lmiuix/pickerwidget/widget/NumberPicker;

    goto :goto_68

    nop

    :goto_a
    mul-int/lit8 v9, v9, 0x2

    goto :goto_48

    nop

    :goto_b
    invoke-virtual {v8}, Lmiuix/pickerwidget/widget/NumberPicker;->getDisplayedMaxTextWidth()F

    move-result v10

    goto :goto_6c

    nop

    :goto_c
    instance-of v8, v6, Lmiuix/pickerwidget/widget/NumberPicker;

    goto :goto_1

    nop

    :goto_d
    move v1, p2

    goto :goto_27

    nop

    :goto_e
    invoke-virtual {v8, v9}, Lmiuix/pickerwidget/widget/NumberPicker;->setTextSizeHighlight(I)V

    goto :goto_19

    nop

    :goto_f
    mul-float/2addr v3, v7

    goto :goto_58

    nop

    :goto_10
    move v4, v2

    :goto_11
    goto :goto_34

    nop

    :goto_12
    invoke-virtual {v7}, Lmiuix/pickerwidget/widget/NumberPicker;->getOriginTextSizeHighlight()I

    move-result v7

    goto :goto_16

    nop

    :goto_13
    iget-object v1, p0, Lmiuix/pickerwidget/widget/NumberPickerGroup;->mValuePaint:Landroid/graphics/Paint;

    goto :goto_26

    nop

    :goto_14
    invoke-virtual {v7}, Lmiuix/pickerwidget/widget/NumberPicker;->getDisplayedMaxTextWidth()F

    move-result v8

    goto :goto_47

    nop

    :goto_15
    invoke-virtual {v6}, Landroid/view/View;->getMeasuredHeight()I

    move-result v9

    goto :goto_1a

    nop

    :goto_16
    int-to-float v7, v7

    goto :goto_3a

    nop

    :goto_17
    if-ltz v6, :cond_1

    goto :goto_62

    :cond_1
    goto :goto_2d

    nop

    :goto_18
    invoke-virtual {v7}, Lmiuix/pickerwidget/widget/NumberPicker;->getOriginalLabelWidth()F

    move-result v8

    goto :goto_33

    nop

    :goto_19
    invoke-virtual {v8}, Lmiuix/pickerwidget/widget/NumberPicker;->getOriginTextSizeHint()I

    move-result v9

    goto :goto_28

    nop

    :goto_1a
    const/high16 v10, 0x40000000

    goto :goto_73

    nop

    :goto_1b
    check-cast v7, Lmiuix/pickerwidget/widget/NumberPicker;

    goto :goto_14

    nop

    :goto_1c
    const/4 p2, 0x0

    goto :goto_7

    nop

    :goto_1d
    invoke-super {p0, p1, p2}, Landroid/widget/LinearLayout;->onMeasure(II)V

    goto :goto_52

    nop

    :goto_1e
    invoke-virtual {v7}, Lmiuix/pickerwidget/widget/NumberPicker;->getMarginLabelLeft()I

    move-result v8

    goto :goto_43

    nop

    :goto_1f
    goto :goto_56

    :goto_20
    goto :goto_55

    nop

    :goto_21
    invoke-virtual {v8}, Lmiuix/pickerwidget/widget/NumberPicker;->getOriginalLabelWidth()F

    move-result v8

    :goto_22
    goto :goto_23

    nop

    :goto_23
    mul-float/2addr v8, v7

    goto :goto_4a

    nop

    :goto_24
    if-gtz v9, :cond_2

    goto :goto_20

    :cond_2
    goto :goto_38

    nop

    :goto_25
    cmpl-float v9, v9, v0

    goto :goto_24

    nop

    :goto_26
    const-string v7, "    "

    goto :goto_6d

    nop

    :goto_27
    move v6, v1

    goto :goto_72

    nop

    :goto_28
    int-to-float v9, v9

    goto :goto_6

    nop

    :goto_29
    add-float/2addr v5, v3

    goto :goto_4

    nop

    :goto_2a
    float-to-int v8, v9

    goto :goto_3c

    nop

    :goto_2b
    invoke-virtual {p0, p2}, Landroid/widget/LinearLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v6

    goto :goto_c

    nop

    :goto_2c
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getChildCount()I

    move-result p1

    goto :goto_1c

    nop

    :goto_2d
    mul-float/2addr v4, v2

    goto :goto_61

    nop

    :goto_2e
    return-void

    :goto_2f
    iget-object v1, p0, Lmiuix/pickerwidget/widget/NumberPickerGroup;->mValuePaint:Landroid/graphics/Paint;

    goto :goto_30

    nop

    :goto_30
    invoke-virtual {v1, v2}, Landroid/graphics/Paint;->setTextSize(F)V

    goto :goto_13

    nop

    :goto_31
    if-eqz p1, :cond_3

    goto :goto_6f

    :cond_3
    goto :goto_2c

    nop

    :goto_32
    move v3, v2

    goto :goto_51

    nop

    :goto_33
    cmpl-float v9, v8, v0

    goto :goto_3f

    nop

    :goto_34
    cmpg-float v6, v4, v2

    goto :goto_5d

    nop

    :goto_35
    const/high16 v7, 0x40000000

    goto :goto_f

    nop

    :goto_36
    goto :goto_4e

    :goto_37
    goto :goto_8

    nop

    :goto_38
    invoke-virtual {v8}, Lmiuix/pickerwidget/widget/NumberPicker;->getMarginLabelLeft()I

    move-result v9

    goto :goto_a

    nop

    :goto_39
    invoke-virtual {v8}, Lmiuix/pickerwidget/widget/NumberPicker;->getOriginalLabelWidth()F

    move-result v9

    goto :goto_25

    nop

    :goto_3a
    invoke-static {v2, v7}, Ljava/lang/Math;->max(FF)F

    move-result v2

    goto :goto_36

    nop

    :goto_3b
    invoke-virtual {v8, v9}, Lmiuix/pickerwidget/widget/NumberPicker;->setTextSizeHint(I)V

    goto :goto_39

    nop

    :goto_3c
    goto :goto_60

    :goto_3d
    goto :goto_5b

    nop

    :goto_3e
    invoke-virtual {p0, v1}, Landroid/widget/LinearLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v7

    goto :goto_9

    nop

    :goto_3f
    if-gtz v9, :cond_4

    goto :goto_66

    :cond_4
    goto :goto_3

    nop

    :goto_40
    invoke-virtual {v6, v8, v9}, Landroid/view/View;->measure(II)V

    :goto_41
    goto :goto_46

    nop

    :goto_42
    div-float v4, v3, v5

    goto :goto_63

    nop

    :goto_43
    int-to-float v8, v8

    goto :goto_65

    nop

    :goto_44
    float-to-int v9, v9

    goto :goto_3b

    nop

    :goto_45
    sub-float/2addr v3, v4

    goto :goto_42

    nop

    :goto_46
    add-int/lit8 p2, p2, 0x1

    goto :goto_6e

    nop

    :goto_47
    add-float/2addr v5, v8

    goto :goto_18

    nop

    :goto_48
    int-to-float v9, v9

    goto :goto_1f

    nop

    :goto_49
    if-nez v10, :cond_5

    goto :goto_3d

    :cond_5
    goto :goto_b

    nop

    :goto_4a
    add-float/2addr v10, v8

    goto :goto_5c

    nop

    :goto_4b
    goto :goto_6a

    :goto_4c
    goto :goto_2f

    nop

    :goto_4d
    add-int/2addr v6, v7

    :goto_4e
    goto :goto_5

    nop

    :goto_4f
    cmpg-float v6, v4, v6

    goto :goto_17

    nop

    :goto_50
    div-float/2addr v10, v5

    goto :goto_64

    nop

    :goto_51
    move v4, v3

    goto :goto_69

    nop

    :goto_52
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getOrientation()I

    move-result p1

    goto :goto_31

    nop

    :goto_53
    sub-int/2addr v3, v6

    goto :goto_2

    nop

    :goto_54
    invoke-virtual {v8}, Lmiuix/pickerwidget/widget/NumberPicker;->getOriginalLabelWidth()F

    move-result v8

    goto :goto_5f

    nop

    :goto_55
    move v9, v0

    :goto_56
    goto :goto_71

    nop

    :goto_57
    move-object v8, v6

    goto :goto_70

    nop

    :goto_58
    mul-float/2addr v4, v7

    goto :goto_29

    nop

    :goto_59
    if-lt p2, p1, :cond_6

    goto :goto_6f

    :cond_6
    goto :goto_2b

    nop

    :goto_5a
    if-lt v1, p1, :cond_7

    goto :goto_4c

    :cond_7
    goto :goto_3e

    nop

    :goto_5b
    invoke-virtual {v8}, Lmiuix/pickerwidget/widget/NumberPicker;->getDisplayedMaxTextWidth()F

    move-result v10

    goto :goto_54

    nop

    :goto_5c
    mul-float/2addr v10, v3

    goto :goto_50

    nop

    :goto_5d
    if-lez v6, :cond_8

    goto :goto_6f

    :cond_8
    :goto_5e
    goto :goto_59

    nop

    :goto_5f
    goto :goto_22

    :goto_60
    goto :goto_15

    nop

    :goto_61
    goto :goto_11

    :goto_62
    goto :goto_10

    nop

    :goto_63
    const/high16 v6, 0x3f800000

    goto :goto_4f

    nop

    :goto_64
    add-float/2addr v9, v10

    goto :goto_2a

    nop

    :goto_65
    add-float/2addr v4, v8

    :goto_66
    goto :goto_12

    nop

    :goto_67
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getMeasuredWidth()I

    move-result v3

    goto :goto_53

    nop

    :goto_68
    if-nez v8, :cond_9

    goto :goto_37

    :cond_9
    goto :goto_1b

    nop

    :goto_69
    move v5, v4

    :goto_6a
    goto :goto_5a

    nop

    :goto_6b
    float-to-int v9, v4

    goto :goto_e

    nop

    :goto_6c
    add-float/2addr v10, v1

    goto :goto_21

    nop

    :goto_6d
    invoke-virtual {v1, v7}, Landroid/graphics/Paint;->measureText(Ljava/lang/String;)F

    move-result v1

    goto :goto_35

    nop

    :goto_6e
    goto :goto_5e

    :goto_6f
    goto :goto_2e

    nop

    :goto_70
    check-cast v8, Lmiuix/pickerwidget/widget/NumberPicker;

    goto :goto_6b

    nop

    :goto_71
    invoke-direct {p0, v8}, Lmiuix/pickerwidget/widget/NumberPickerGroup;->isDayNumberPicker(Lmiuix/pickerwidget/widget/NumberPicker;)Z

    move-result v10

    goto :goto_49

    nop

    :goto_72
    move v2, v0

    goto :goto_32

    nop

    :goto_73
    invoke-static {v8, v10}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v8

    goto :goto_74

    nop

    :goto_74
    invoke-static {v9, v10}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v9

    goto :goto_40

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
