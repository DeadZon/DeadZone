TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/internal/widget/GroupButton.smali'
CLASS_FALLBACK_NAMES = ['GroupButton.smali']
CLASS_ANCHORS = ['.super Lmiuix/appcompat/widget/Button;', '.field private static final STATE_FIRST_H:[I', '.field private static final STATE_FIRST_V:[I', '.field private static final STATE_LAST_H:[I', '.field private static final STATE_LAST_V:[I', '.field private static final STATE_MIDDLE_H:[I']

PATCHES = [
    {
        'id': 'miuix_internal_widget_GroupButton__onCreateDrawableState',
        'method': '.method protected onCreateDrawableState(I)[I',
        'method_name': 'onCreateDrawableState',
        'method_anchors': ['invoke-virtual {p0}, Landroid/widget/Button;->getParent()Landroid/view/ViewParent;', 'check-cast v0, Landroid/view/ViewGroup;', 'if-nez v0, :cond_0', 'invoke-super {p0, p1}, Landroid/widget/Button;->onCreateDrawableState(I)[I', 'return-object p0', 'if-eqz v1, :cond_e', 'check-cast v1, Landroid/widget/LinearLayout;', 'invoke-virtual {v1}, Landroid/widget/LinearLayout;->getOrientation()I'],
        'type': 'method_replace',
        'search': """.method protected onCreateDrawableState(I)[I
    .registers 12

    invoke-virtual {p0}, Landroid/widget/Button;->getParent()Landroid/view/ViewParent;

    move-result-object v0

    check-cast v0, Landroid/view/ViewGroup;

    if-nez v0, :cond_0

    invoke-super {p0, p1}, Landroid/widget/Button;->onCreateDrawableState(I)[I

    move-result-object p0

    return-object p0

    :cond_0
    instance-of v1, v0, Landroid/widget/LinearLayout;

    if-eqz v1, :cond_e

    move-object v1, v0

    check-cast v1, Landroid/widget/LinearLayout;

    invoke-virtual {v1}, Landroid/widget/LinearLayout;->getOrientation()I

    move-result v1

    invoke-virtual {v0, p0}, Landroid/view/ViewGroup;->indexOfChild(Landroid/view/View;)I

    move-result v2

    const/4 v3, 0x0

    const/4 v4, 0x1

    move v5, v3

    move v6, v5

    move v7, v4

    move v8, v7

    :goto_0
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getChildCount()I

    move-result v9

    if-ge v5, v9, :cond_3

    invoke-virtual {v0, v5}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;

    move-result-object v9

    invoke-virtual {v9}, Landroid/view/View;->getVisibility()I

    move-result v9

    if-nez v9, :cond_2

    add-int/lit8 v6, v6, 0x1

    if-ge v5, v2, :cond_1

    move v7, v3

    :cond_1
    if-le v5, v2, :cond_2

    move v8, v3

    :cond_2
    add-int/lit8 v5, v5, 0x1

    goto :goto_0

    :cond_3
    if-ne v6, v4, :cond_4

    move v3, v4

    :cond_4
    if-ne v1, v4, :cond_8

    add-int/lit8 p1, p1, 0x2

    invoke-super {p0, p1}, Landroid/widget/Button;->onCreateDrawableState(I)[I

    move-result-object p0

    sget-object p1, Lmiuix/internal/widget/GroupButton;->STATE_SINGLE_H:[I

    invoke-static {p0, p1}, Landroid/widget/Button;->mergeDrawableStates([I[I)[I

    if-nez v3, :cond_7

    if-eqz v7, :cond_5

    sget-object p1, Lmiuix/internal/widget/GroupButton;->STATE_FIRST_V:[I

    invoke-static {p0, p1}, Landroid/widget/Button;->mergeDrawableStates([I[I)[I

    return-object p0

    :cond_5
    if-eqz v8, :cond_6

    sget-object p1, Lmiuix/internal/widget/GroupButton;->STATE_LAST_V:[I

    invoke-static {p0, p1}, Landroid/widget/Button;->mergeDrawableStates([I[I)[I

    return-object p0

    :cond_6
    sget-object p1, Lmiuix/internal/widget/GroupButton;->STATE_MIDDLE_V:[I

    invoke-static {p0, p1}, Landroid/widget/Button;->mergeDrawableStates([I[I)[I

    :cond_7
    return-object p0

    :cond_8
    invoke-static {p0}, Landroidx/appcompat/widget/ViewUtils;->isLayoutRtl(Landroid/view/View;)Z

    move-result v0

    add-int/2addr p1, v4

    invoke-super {p0, p1}, Landroid/widget/Button;->onCreateDrawableState(I)[I

    move-result-object p0

    if-eqz v3, :cond_9

    sget-object p1, Lmiuix/internal/widget/GroupButton;->STATE_SINGLE_H:[I

    invoke-static {p0, p1}, Landroid/widget/Button;->mergeDrawableStates([I[I)[I

    return-object p0

    :cond_9
    if-eqz v7, :cond_b

    if-eqz v0, :cond_a

    sget-object p1, Lmiuix/internal/widget/GroupButton;->STATE_LAST_H:[I

    goto :goto_1

    :cond_a
    sget-object p1, Lmiuix/internal/widget/GroupButton;->STATE_FIRST_H:[I

    :goto_1
    invoke-static {p0, p1}, Landroid/widget/Button;->mergeDrawableStates([I[I)[I

    return-object p0

    :cond_b
    if-eqz v8, :cond_d

    if-eqz v0, :cond_c

    sget-object p1, Lmiuix/internal/widget/GroupButton;->STATE_FIRST_H:[I

    goto :goto_2

    :cond_c
    sget-object p1, Lmiuix/internal/widget/GroupButton;->STATE_LAST_H:[I

    :goto_2
    invoke-static {p0, p1}, Landroid/widget/Button;->mergeDrawableStates([I[I)[I

    return-object p0

    :cond_d
    sget-object p1, Lmiuix/internal/widget/GroupButton;->STATE_MIDDLE_H:[I

    invoke-static {p0, p1}, Landroid/widget/Button;->mergeDrawableStates([I[I)[I

    return-object p0

    :cond_e
    invoke-super {p0, p1}, Landroid/widget/Button;->onCreateDrawableState(I)[I

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected onCreateDrawableState(I)[I
    .registers 12

    goto :goto_e

    nop

    :goto_0
    move-object v1, v0

    goto :goto_53

    nop

    :goto_1
    invoke-virtual {v0, v5}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;

    move-result-object v9

    goto :goto_30

    nop

    :goto_2
    return-object p0

    :goto_3
    move v8, v3

    :goto_4
    goto :goto_49

    nop

    :goto_5
    if-eq v6, v4, :cond_0

    goto :goto_18

    :cond_0
    goto :goto_17

    nop

    :goto_6
    sget-object p1, Lmiuix/internal/widget/GroupButton;->STATE_LAST_V:[I

    goto :goto_34

    nop

    :goto_7
    invoke-static {p0, p1}, Landroid/widget/Button;->mergeDrawableStates([I[I)[I

    :goto_8
    goto :goto_3a

    nop

    :goto_9
    return-object p0

    :goto_a
    goto :goto_f

    nop

    :goto_b
    invoke-super {p0, p1}, Landroid/widget/Button;->onCreateDrawableState(I)[I

    move-result-object p0

    goto :goto_43

    nop

    :goto_c
    if-eqz v9, :cond_1

    goto :goto_4

    :cond_1
    goto :goto_50

    nop

    :goto_d
    if-lt v5, v2, :cond_2

    goto :goto_40

    :cond_2
    goto :goto_3f

    nop

    :goto_e
    invoke-virtual {p0}, Landroid/widget/Button;->getParent()Landroid/view/ViewParent;

    move-result-object v0

    goto :goto_29

    nop

    :goto_f
    sget-object p1, Lmiuix/internal/widget/GroupButton;->STATE_MIDDLE_H:[I

    goto :goto_4c

    nop

    :goto_10
    sget-object p1, Lmiuix/internal/widget/GroupButton;->STATE_FIRST_H:[I

    goto :goto_41

    nop

    :goto_11
    return-object p0

    :goto_12
    goto :goto_4a

    nop

    :goto_13
    invoke-static {p0, p1}, Landroid/widget/Button;->mergeDrawableStates([I[I)[I

    goto :goto_25

    nop

    :goto_14
    if-nez v0, :cond_3

    goto :goto_42

    :cond_3
    goto :goto_10

    nop

    :goto_15
    move v7, v4

    goto :goto_19

    nop

    :goto_16
    invoke-static {p0}, Landroidx/appcompat/widget/ViewUtils;->isLayoutRtl(Landroid/view/View;)Z

    move-result v0

    goto :goto_2e

    nop

    :goto_17
    move v3, v4

    :goto_18
    goto :goto_59

    nop

    :goto_19
    move v8, v7

    :goto_1a
    goto :goto_2c

    nop

    :goto_1b
    invoke-virtual {v1}, Landroid/widget/LinearLayout;->getOrientation()I

    move-result v1

    goto :goto_1c

    nop

    :goto_1c
    invoke-virtual {v0, p0}, Landroid/view/ViewGroup;->indexOfChild(Landroid/view/View;)I

    move-result v2

    goto :goto_32

    nop

    :goto_1d
    return-object p0

    :goto_1e
    goto :goto_31

    nop

    :goto_1f
    return-object p0

    :goto_20
    goto :goto_44

    nop

    :goto_21
    if-nez v1, :cond_4

    goto :goto_1e

    :cond_4
    goto :goto_0

    nop

    :goto_22
    sget-object p1, Lmiuix/internal/widget/GroupButton;->STATE_LAST_H:[I

    goto :goto_3d

    nop

    :goto_23
    invoke-static {p0, p1}, Landroid/widget/Button;->mergeDrawableStates([I[I)[I

    goto :goto_9

    nop

    :goto_24
    invoke-static {p0, p1}, Landroid/widget/Button;->mergeDrawableStates([I[I)[I

    goto :goto_45

    nop

    :goto_25
    return-object p0

    :goto_26
    goto :goto_35

    nop

    :goto_27
    if-lt v5, v9, :cond_5

    goto :goto_56

    :cond_5
    goto :goto_1

    nop

    :goto_28
    if-gt v5, v2, :cond_6

    goto :goto_4

    :cond_6
    goto :goto_3

    nop

    :goto_29
    check-cast v0, Landroid/view/ViewGroup;

    goto :goto_2f

    nop

    :goto_2a
    instance-of v1, v0, Landroid/widget/LinearLayout;

    goto :goto_21

    nop

    :goto_2b
    sget-object p1, Lmiuix/internal/widget/GroupButton;->STATE_FIRST_V:[I

    goto :goto_2d

    nop

    :goto_2c
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getChildCount()I

    move-result v9

    goto :goto_27

    nop

    :goto_2d
    invoke-static {p0, p1}, Landroid/widget/Button;->mergeDrawableStates([I[I)[I

    goto :goto_11

    nop

    :goto_2e
    add-int/2addr p1, v4

    goto :goto_4f

    nop

    :goto_2f
    if-eqz v0, :cond_7

    goto :goto_4e

    :cond_7
    goto :goto_5b

    nop

    :goto_30
    invoke-virtual {v9}, Landroid/view/View;->getVisibility()I

    move-result v9

    goto :goto_c

    nop

    :goto_31
    invoke-super {p0, p1}, Landroid/widget/Button;->onCreateDrawableState(I)[I

    move-result-object p0

    goto :goto_2

    nop

    :goto_32
    const/4 v3, 0x0

    goto :goto_5a

    nop

    :goto_33
    add-int/lit8 p1, p1, 0x2

    goto :goto_b

    nop

    :goto_34
    invoke-static {p0, p1}, Landroid/widget/Button;->mergeDrawableStates([I[I)[I

    goto :goto_1f

    nop

    :goto_35
    if-nez v7, :cond_8

    goto :goto_46

    :cond_8
    goto :goto_51

    nop

    :goto_36
    sget-object p1, Lmiuix/internal/widget/GroupButton;->STATE_FIRST_H:[I

    :goto_37
    goto :goto_24

    nop

    :goto_38
    move v5, v3

    goto :goto_52

    nop

    :goto_39
    if-nez v8, :cond_9

    goto :goto_a

    :cond_9
    goto :goto_14

    nop

    :goto_3a
    return-object p0

    :goto_3b
    goto :goto_16

    nop

    :goto_3c
    sget-object p1, Lmiuix/internal/widget/GroupButton;->STATE_SINGLE_H:[I

    goto :goto_13

    nop

    :goto_3d
    goto :goto_37

    :goto_3e
    goto :goto_36

    nop

    :goto_3f
    move v7, v3

    :goto_40
    goto :goto_28

    nop

    :goto_41
    goto :goto_58

    :goto_42
    goto :goto_57

    nop

    :goto_43
    sget-object p1, Lmiuix/internal/widget/GroupButton;->STATE_SINGLE_H:[I

    goto :goto_54

    nop

    :goto_44
    sget-object p1, Lmiuix/internal/widget/GroupButton;->STATE_MIDDLE_V:[I

    goto :goto_7

    nop

    :goto_45
    return-object p0

    :goto_46
    goto :goto_39

    nop

    :goto_47
    if-eqz v3, :cond_a

    goto :goto_8

    :cond_a
    goto :goto_48

    nop

    :goto_48
    if-nez v7, :cond_b

    goto :goto_12

    :cond_b
    goto :goto_2b

    nop

    :goto_49
    add-int/lit8 v5, v5, 0x1

    goto :goto_55

    nop

    :goto_4a
    if-nez v8, :cond_c

    goto :goto_20

    :cond_c
    goto :goto_6

    nop

    :goto_4b
    if-nez v3, :cond_d

    goto :goto_26

    :cond_d
    goto :goto_3c

    nop

    :goto_4c
    invoke-static {p0, p1}, Landroid/widget/Button;->mergeDrawableStates([I[I)[I

    goto :goto_1d

    nop

    :goto_4d
    return-object p0

    :goto_4e
    goto :goto_2a

    nop

    :goto_4f
    invoke-super {p0, p1}, Landroid/widget/Button;->onCreateDrawableState(I)[I

    move-result-object p0

    goto :goto_4b

    nop

    :goto_50
    add-int/lit8 v6, v6, 0x1

    goto :goto_d

    nop

    :goto_51
    if-nez v0, :cond_e

    goto :goto_3e

    :cond_e
    goto :goto_22

    nop

    :goto_52
    move v6, v5

    goto :goto_15

    nop

    :goto_53
    check-cast v1, Landroid/widget/LinearLayout;

    goto :goto_1b

    nop

    :goto_54
    invoke-static {p0, p1}, Landroid/widget/Button;->mergeDrawableStates([I[I)[I

    goto :goto_47

    nop

    :goto_55
    goto :goto_1a

    :goto_56
    goto :goto_5

    nop

    :goto_57
    sget-object p1, Lmiuix/internal/widget/GroupButton;->STATE_LAST_H:[I

    :goto_58
    goto :goto_23

    nop

    :goto_59
    if-eq v1, v4, :cond_f

    goto :goto_3b

    :cond_f
    goto :goto_33

    nop

    :goto_5a
    const/4 v4, 0x1

    goto :goto_38

    nop

    :goto_5b
    invoke-super {p0, p1}, Landroid/widget/Button;->onCreateDrawableState(I)[I

    move-result-object p0

    goto :goto_4d

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
