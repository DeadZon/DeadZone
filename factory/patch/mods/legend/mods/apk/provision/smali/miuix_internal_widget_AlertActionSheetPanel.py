TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/internal/widget/AlertActionSheetPanel.smali'
CLASS_FALLBACK_NAMES = ['AlertActionSheetPanel.smali']
CLASS_ANCHORS = ['.super Landroid/widget/LinearLayout;']

PATCHES = [
    {
        'id': 'miuix_internal_widget_AlertActionSheetPanel__onConfigurationChanged',
        'method': '.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V',
        'method_name': 'onConfigurationChanged',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/widget/LinearLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V', 'iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheetPanel;->mContext:Landroid/content/Context;', 'iget-object v0, p0, Lmiuix/internal/widget/AlertActionSheetPanel;->mScreenSize:Landroid/graphics/Point;', 'invoke-static {p1, v0}, Lmiuix/core/util/WindowUtils;->getScreenSize(Landroid/content/Context;Landroid/graphics/Point;)V', 'iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheetPanel;->mScreenSize:Landroid/graphics/Point;', 'iget p1, p1, Landroid/graphics/Point;->y:I', 'iput p1, p0, Lmiuix/internal/widget/AlertActionSheetPanel;->mMaxHeight:I', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 3

    invoke-super {p0, p1}, Landroid/widget/LinearLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheetPanel;->mContext:Landroid/content/Context;

    iget-object v0, p0, Lmiuix/internal/widget/AlertActionSheetPanel;->mScreenSize:Landroid/graphics/Point;

    invoke-static {p1, v0}, Lmiuix/core/util/WindowUtils;->getScreenSize(Landroid/content/Context;Landroid/graphics/Point;)V

    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheetPanel;->mScreenSize:Landroid/graphics/Point;

    iget p1, p1, Landroid/graphics/Point;->y:I

    int-to-float p1, p1

    const v0, 0x3f333333

    mul-float/2addr p1, v0

    float-to-int p1, p1

    iput p1, p0, Lmiuix/internal/widget/AlertActionSheetPanel;->mMaxHeight:I

    return-void
.end method""",
        'replacement': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 3

    goto :goto_6

    nop

    :goto_0
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheetPanel;->mScreenSize:Landroid/graphics/Point;

    goto :goto_4

    nop

    :goto_1
    mul-float/2addr p1, v0

    goto :goto_9

    nop

    :goto_2
    return-void

    :goto_3
    int-to-float p1, p1

    goto :goto_7

    nop

    :goto_4
    iget p1, p1, Landroid/graphics/Point;->y:I

    goto :goto_3

    nop

    :goto_5
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheetPanel;->mContext:Landroid/content/Context;

    goto :goto_a

    nop

    :goto_6
    invoke-super {p0, p1}, Landroid/widget/LinearLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    goto :goto_5

    nop

    :goto_7
    const v0, 0x3f333333

    goto :goto_1

    nop

    :goto_8
    iput p1, p0, Lmiuix/internal/widget/AlertActionSheetPanel;->mMaxHeight:I

    goto :goto_2

    nop

    :goto_9
    float-to-int p1, p1

    goto :goto_8

    nop

    :goto_a
    iget-object v0, p0, Lmiuix/internal/widget/AlertActionSheetPanel;->mScreenSize:Landroid/graphics/Point;

    goto :goto_b

    nop

    :goto_b
    invoke-static {p1, v0}, Lmiuix/core/util/WindowUtils;->getScreenSize(Landroid/content/Context;Landroid/graphics/Point;)V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_widget_AlertActionSheetPanel__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['invoke-static {p2}, Landroid/view/View$MeasureSpec;->getSize(I)I', 'sget-boolean v1, Lmiuix/os/Build;->IS_FLIP:Z', 'if-eqz v1, :cond_0', 'iget-object v1, p0, Lmiuix/internal/widget/AlertActionSheetPanel;->mContext:Landroid/content/Context;', 'invoke-static {v1}, Lmiuix/os/DeviceHelper;->isTinyScreen(Landroid/content/Context;)Z', 'if-eqz v1, :cond_0', 'iget-object v4, p0, Lmiuix/internal/widget/AlertActionSheetPanel;->mScreenSize:Landroid/graphics/Point;', 'iget v5, v4, Landroid/graphics/Point;->y:I'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 11

    invoke-static {p2}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v0

    sget-boolean v1, Lmiuix/os/Build;->IS_FLIP:Z

    const/4 v2, 0x1

    const/4 v3, 0x0

    if-eqz v1, :cond_0

    iget-object v1, p0, Lmiuix/internal/widget/AlertActionSheetPanel;->mContext:Landroid/content/Context;

    invoke-static {v1}, Lmiuix/os/DeviceHelper;->isTinyScreen(Landroid/content/Context;)Z

    move-result v1

    if-eqz v1, :cond_0

    move v1, v2

    goto :goto_0

    :cond_0
    move v1, v3

    :goto_0
    iget-object v4, p0, Lmiuix/internal/widget/AlertActionSheetPanel;->mScreenSize:Landroid/graphics/Point;

    iget v5, v4, Landroid/graphics/Point;->y:I

    iget v4, v4, Landroid/graphics/Point;->x:I

    if-le v5, v4, :cond_1

    move v4, v2

    goto :goto_1

    :cond_1
    move v4, v3

    :goto_1
    iget-object v6, p0, Lmiuix/internal/widget/AlertActionSheetPanel;->mContext:Landroid/content/Context;

    int-to-float v5, v5

    invoke-static {v6, v5}, Lmiuix/core/util/MiuixUIUtils;->px2dp(Landroid/content/Context;F)I

    move-result v5

    const/16 v6, 0x1f4

    if-lt v5, v6, :cond_2

    move v5, v2

    goto :goto_2

    :cond_2
    move v5, v3

    :goto_2
    iget-object v6, p0, Lmiuix/internal/widget/AlertActionSheetPanel;->mContext:Landroid/content/Context;

    invoke-static {v6}, Lmiuix/core/util/EnvStateManager;->isFreeFormMode(Landroid/content/Context;)Z

    move-result v6

    const/high16 v7, -0x80000000

    if-eqz v6, :cond_3

    invoke-direct {p0}, Lmiuix/internal/widget/AlertActionSheetPanel;->getAvailableMaxHeightInFreeForm()I

    move-result p2

    invoke-static {p2, v7}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p2

    goto :goto_3

    :cond_3
    if-nez v1, :cond_5

    if-nez v4, :cond_4

    if-eqz v5, :cond_5

    :cond_4
    iget v1, p0, Lmiuix/internal/widget/AlertActionSheetPanel;->mMaxHeight:I

    if-le v0, v1, :cond_5

    invoke-static {v1, v7}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p2

    :cond_5
    :goto_3
    invoke-super {p0, p1, p2}, Landroid/widget/LinearLayout;->onMeasure(II)V

    invoke-static {p2}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v0

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getChildCount()I

    move-result v1

    const/4 v4, 0x2

    if-lt v1, v4, :cond_6

    invoke-virtual {p0, v3}, Landroid/widget/LinearLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v1

    check-cast v1, Landroid/view/ViewGroup;

    invoke-virtual {p0, v2}, Landroid/widget/LinearLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v2

    check-cast v2, Landroid/view/ViewGroup;

    goto :goto_4

    :cond_6
    const/4 v1, 0x0

    move-object v2, v1

    :goto_4
    iget v4, p0, Lmiuix/internal/widget/AlertActionSheetPanel;->mSeparateItemMarginTop:I

    if-eqz v2, :cond_7

    invoke-virtual {p0, v2, p1, p2}, Landroid/widget/LinearLayout;->measureChild(Landroid/view/View;II)V

    invoke-virtual {v2}, Landroid/view/ViewGroup;->getMeasuredHeight()I

    move-result v2

    add-int/2addr v4, v2

    goto :goto_5

    :cond_7
    move v2, v3

    :goto_5
    if-eqz v1, :cond_8

    invoke-virtual {p0, v1, p1, p2}, Landroid/widget/LinearLayout;->measureChild(Landroid/view/View;II)V

    invoke-virtual {v1}, Landroid/view/ViewGroup;->getMeasuredHeight()I

    move-result v3

    :cond_8
    add-int/2addr v3, v2

    iget p2, p0, Lmiuix/internal/widget/AlertActionSheetPanel;->mSeparateItemMarginTop:I

    add-int/2addr v3, p2

    if-le v3, v0, :cond_9

    if-eqz v1, :cond_9

    sub-int/2addr v0, v2

    sub-int/2addr v0, p2

    const/high16 p2, 0x40000000

    invoke-static {v0, p2}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p2

    invoke-virtual {v1, p1, p2}, Landroid/view/ViewGroup;->measure(II)V

    invoke-virtual {v1}, Landroid/view/ViewGroup;->getMeasuredHeight()I

    move-result p1

    add-int/2addr v4, p1

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getMeasuredWidth()I

    move-result p1

    invoke-virtual {p0, p1, v4}, Landroid/widget/LinearLayout;->setMeasuredDimension(II)V

    :cond_9
    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 11

    goto :goto_48

    nop

    :goto_0
    iget v4, p0, Lmiuix/internal/widget/AlertActionSheetPanel;->mSeparateItemMarginTop:I

    goto :goto_15

    nop

    :goto_1
    sget-boolean v1, Lmiuix/os/Build;->IS_FLIP:Z

    goto :goto_17

    nop

    :goto_2
    if-nez v1, :cond_0

    goto :goto_35

    :cond_0
    goto :goto_49

    nop

    :goto_3
    sub-int/2addr v0, v2

    goto :goto_27

    nop

    :goto_4
    iget-object v6, p0, Lmiuix/internal/widget/AlertActionSheetPanel;->mContext:Landroid/content/Context;

    goto :goto_4a

    nop

    :goto_5
    if-nez v1, :cond_1

    goto :goto_4e

    :cond_1
    goto :goto_d

    nop

    :goto_6
    add-int/2addr v3, v2

    goto :goto_4f

    nop

    :goto_7
    invoke-static {p2, v7}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p2

    goto :goto_1b

    nop

    :goto_8
    move v4, v3

    :goto_9
    goto :goto_4

    nop

    :goto_a
    move v5, v3

    :goto_b
    goto :goto_45

    nop

    :goto_c
    iget v1, p0, Lmiuix/internal/widget/AlertActionSheetPanel;->mMaxHeight:I

    goto :goto_51

    nop

    :goto_d
    invoke-virtual {p0, v1, p1, p2}, Landroid/widget/LinearLayout;->measureChild(Landroid/view/View;II)V

    goto :goto_4d

    nop

    :goto_e
    const/4 v1, 0x0

    goto :goto_56

    nop

    :goto_f
    if-ge v1, v4, :cond_2

    goto :goto_54

    :cond_2
    goto :goto_21

    nop

    :goto_10
    invoke-static {v6}, Lmiuix/core/util/EnvStateManager;->isFreeFormMode(Landroid/content/Context;)Z

    move-result v6

    goto :goto_39

    nop

    :goto_11
    move v2, v3

    :goto_12
    goto :goto_5

    nop

    :goto_13
    if-eqz v4, :cond_3

    goto :goto_37

    :cond_3
    goto :goto_36

    nop

    :goto_14
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getChildCount()I

    move-result v1

    goto :goto_24

    nop

    :goto_15
    if-nez v2, :cond_4

    goto :goto_3b

    :cond_4
    goto :goto_2e

    nop

    :goto_16
    add-int/2addr v3, p2

    goto :goto_43

    nop

    :goto_17
    const/4 v2, 0x1

    goto :goto_19

    nop

    :goto_18
    iget v4, v4, Landroid/graphics/Point;->x:I

    goto :goto_47

    nop

    :goto_19
    const/4 v3, 0x0

    goto :goto_2

    nop

    :goto_1a
    add-int/2addr v4, p1

    goto :goto_50

    nop

    :goto_1b
    goto :goto_59

    :goto_1c
    goto :goto_55

    nop

    :goto_1d
    iget-object v4, p0, Lmiuix/internal/widget/AlertActionSheetPanel;->mScreenSize:Landroid/graphics/Point;

    goto :goto_22

    nop

    :goto_1e
    move v1, v3

    :goto_1f
    goto :goto_1d

    nop

    :goto_20
    check-cast v2, Landroid/view/ViewGroup;

    goto :goto_53

    nop

    :goto_21
    invoke-virtual {p0, v3}, Landroid/widget/LinearLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v1

    goto :goto_44

    nop

    :goto_22
    iget v5, v4, Landroid/graphics/Point;->y:I

    goto :goto_18

    nop

    :goto_23
    add-int/2addr v4, v2

    goto :goto_3a

    nop

    :goto_24
    const/4 v4, 0x2

    goto :goto_f

    nop

    :goto_25
    move v1, v2

    goto :goto_34

    nop

    :goto_26
    invoke-static {v1}, Lmiuix/os/DeviceHelper;->isTinyScreen(Landroid/content/Context;)Z

    move-result v1

    goto :goto_46

    nop

    :goto_27
    sub-int/2addr v0, p2

    goto :goto_2d

    nop

    :goto_28
    invoke-static {v6, v5}, Lmiuix/core/util/MiuixUIUtils;->px2dp(Landroid/content/Context;F)I

    move-result v5

    goto :goto_3f

    nop

    :goto_29
    goto :goto_9

    :goto_2a
    goto :goto_8

    nop

    :goto_2b
    invoke-virtual {v1}, Landroid/view/ViewGroup;->getMeasuredHeight()I

    move-result p1

    goto :goto_1a

    nop

    :goto_2c
    if-nez v1, :cond_5

    goto :goto_42

    :cond_5
    goto :goto_3

    nop

    :goto_2d
    const/high16 p2, 0x40000000

    goto :goto_31

    nop

    :goto_2e
    invoke-virtual {p0, v2, p1, p2}, Landroid/widget/LinearLayout;->measureChild(Landroid/view/View;II)V

    goto :goto_38

    nop

    :goto_2f
    invoke-direct {p0}, Lmiuix/internal/widget/AlertActionSheetPanel;->getAvailableMaxHeightInFreeForm()I

    move-result p2

    goto :goto_7

    nop

    :goto_30
    invoke-virtual {v1, p1, p2}, Landroid/view/ViewGroup;->measure(II)V

    goto :goto_2b

    nop

    :goto_31
    invoke-static {v0, p2}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p2

    goto :goto_30

    nop

    :goto_32
    move v5, v2

    goto :goto_4b

    nop

    :goto_33
    return-void

    :goto_34
    goto :goto_1f

    :goto_35
    goto :goto_1e

    nop

    :goto_36
    if-nez v5, :cond_6

    goto :goto_59

    :cond_6
    :goto_37
    goto :goto_c

    nop

    :goto_38
    invoke-virtual {v2}, Landroid/view/ViewGroup;->getMeasuredHeight()I

    move-result v2

    goto :goto_23

    nop

    :goto_39
    const/high16 v7, -0x80000000

    goto :goto_3d

    nop

    :goto_3a
    goto :goto_12

    :goto_3b
    goto :goto_11

    nop

    :goto_3c
    invoke-virtual {p0, v2}, Landroid/widget/LinearLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v2

    goto :goto_20

    nop

    :goto_3d
    if-nez v6, :cond_7

    goto :goto_1c

    :cond_7
    goto :goto_2f

    nop

    :goto_3e
    invoke-super {p0, p1, p2}, Landroid/widget/LinearLayout;->onMeasure(II)V

    goto :goto_40

    nop

    :goto_3f
    const/16 v6, 0x1f4

    goto :goto_52

    nop

    :goto_40
    invoke-static {p2}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v0

    goto :goto_14

    nop

    :goto_41
    invoke-virtual {p0, p1, v4}, Landroid/widget/LinearLayout;->setMeasuredDimension(II)V

    :goto_42
    goto :goto_33

    nop

    :goto_43
    if-gt v3, v0, :cond_8

    goto :goto_42

    :cond_8
    goto :goto_2c

    nop

    :goto_44
    check-cast v1, Landroid/view/ViewGroup;

    goto :goto_3c

    nop

    :goto_45
    iget-object v6, p0, Lmiuix/internal/widget/AlertActionSheetPanel;->mContext:Landroid/content/Context;

    goto :goto_10

    nop

    :goto_46
    if-nez v1, :cond_9

    goto :goto_35

    :cond_9
    goto :goto_25

    nop

    :goto_47
    if-gt v5, v4, :cond_a

    goto :goto_2a

    :cond_a
    goto :goto_5a

    nop

    :goto_48
    invoke-static {p2}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v0

    goto :goto_1

    nop

    :goto_49
    iget-object v1, p0, Lmiuix/internal/widget/AlertActionSheetPanel;->mContext:Landroid/content/Context;

    goto :goto_26

    nop

    :goto_4a
    int-to-float v5, v5

    goto :goto_28

    nop

    :goto_4b
    goto :goto_b

    :goto_4c
    goto :goto_a

    nop

    :goto_4d
    invoke-virtual {v1}, Landroid/view/ViewGroup;->getMeasuredHeight()I

    move-result v3

    :goto_4e
    goto :goto_6

    nop

    :goto_4f
    iget p2, p0, Lmiuix/internal/widget/AlertActionSheetPanel;->mSeparateItemMarginTop:I

    goto :goto_16

    nop

    :goto_50
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getMeasuredWidth()I

    move-result p1

    goto :goto_41

    nop

    :goto_51
    if-gt v0, v1, :cond_b

    goto :goto_59

    :cond_b
    goto :goto_58

    nop

    :goto_52
    if-ge v5, v6, :cond_c

    goto :goto_4c

    :cond_c
    goto :goto_32

    nop

    :goto_53
    goto :goto_57

    :goto_54
    goto :goto_e

    nop

    :goto_55
    if-eqz v1, :cond_d

    goto :goto_59

    :cond_d
    goto :goto_13

    nop

    :goto_56
    move-object v2, v1

    :goto_57
    goto :goto_0

    nop

    :goto_58
    invoke-static {v1, v7}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p2

    :goto_59
    goto :goto_3e

    nop

    :goto_5a
    move v4, v2

    goto :goto_29

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
