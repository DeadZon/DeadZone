TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/recyclerview/widget/MiuiDefaultItemAnimator.smali'
CLASS_FALLBACK_NAMES = ['MiuiDefaultItemAnimator.smali']
CLASS_ANCHORS = ['.super Landroidx/recyclerview/widget/SimpleItemAnimator;', '.field static final INTERPOLATOR:Landroid/animation/TimeInterpolator;']

PATCHES = [
    {
        'id': 'miuix_recyclerview_widget_MiuiDefaultItemAnimator__animateAddImpl',
        'method': '.method animateAddImpl(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)V',
        'method_name': 'animateAddImpl',
        'method_anchors': ['iget-object v0, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;', 'invoke-virtual {v0}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;', 'iget-object v2, p0, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->mAddAnimations:Ljava/util/ArrayList;', 'invoke-virtual {v2, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z', 'sget-object v2, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->INTERPOLATOR:Landroid/animation/TimeInterpolator;', 'invoke-virtual {v1, v2}, Landroid/view/ViewPropertyAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)Landroid/view/ViewPropertyAnimator;', 'invoke-virtual {v1, v2}, Landroid/view/ViewPropertyAnimator;->alpha(F)Landroid/view/ViewPropertyAnimator;', 'invoke-virtual {p0}, Landroidx/recyclerview/widget/RecyclerView$ItemAnimator;->getAddDuration()J'],
        'type': 'method_replace',
        'search': """.method animateAddImpl(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)V
    .registers 7

    iget-object v0, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    invoke-virtual {v0}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object v1

    iget-object v2, p0, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->mAddAnimations:Ljava/util/ArrayList;

    invoke-virtual {v2, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    sget-object v2, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->INTERPOLATOR:Landroid/animation/TimeInterpolator;

    invoke-virtual {v1, v2}, Landroid/view/ViewPropertyAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)Landroid/view/ViewPropertyAnimator;

    const/high16 v2, 0x3f800000

    invoke-virtual {v1, v2}, Landroid/view/ViewPropertyAnimator;->alpha(F)Landroid/view/ViewPropertyAnimator;

    move-result-object v2

    invoke-virtual {p0}, Landroidx/recyclerview/widget/RecyclerView$ItemAnimator;->getAddDuration()J

    move-result-wide v3

    invoke-virtual {v2, v3, v4}, Landroid/view/ViewPropertyAnimator;->setDuration(J)Landroid/view/ViewPropertyAnimator;

    move-result-object v2

    new-instance v3, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$5;

    invoke-direct {v3, p0, p1, v0, v1}, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$5;-><init>(Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;Landroidx/recyclerview/widget/RecyclerView$ViewHolder;Landroid/view/View;Landroid/view/ViewPropertyAnimator;)V

    invoke-virtual {v2, v3}, Landroid/view/ViewPropertyAnimator;->setListener(Landroid/animation/Animator$AnimatorListener;)Landroid/view/ViewPropertyAnimator;

    move-result-object p0

    invoke-virtual {p0}, Landroid/view/ViewPropertyAnimator;->start()V

    return-void
.end method""",
        'replacement': """.method animateAddImpl(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)V
    .registers 7

    goto :goto_c

    nop

    :goto_0
    sget-object v2, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->INTERPOLATOR:Landroid/animation/TimeInterpolator;

    goto :goto_4

    nop

    :goto_1
    invoke-virtual {v1, v2}, Landroid/view/ViewPropertyAnimator;->alpha(F)Landroid/view/ViewPropertyAnimator;

    move-result-object v2

    goto :goto_9

    nop

    :goto_2
    iget-object v2, p0, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->mAddAnimations:Ljava/util/ArrayList;

    goto :goto_8

    nop

    :goto_3
    new-instance v3, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$5;

    goto :goto_e

    nop

    :goto_4
    invoke-virtual {v1, v2}, Landroid/view/ViewPropertyAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)Landroid/view/ViewPropertyAnimator;

    goto :goto_7

    nop

    :goto_5
    invoke-virtual {v2, v3}, Landroid/view/ViewPropertyAnimator;->setListener(Landroid/animation/Animator$AnimatorListener;)Landroid/view/ViewPropertyAnimator;

    move-result-object p0

    goto :goto_6

    nop

    :goto_6
    invoke-virtual {p0}, Landroid/view/ViewPropertyAnimator;->start()V

    goto :goto_a

    nop

    :goto_7
    const/high16 v2, 0x3f800000

    goto :goto_1

    nop

    :goto_8
    invoke-virtual {v2, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_0

    nop

    :goto_9
    invoke-virtual {p0}, Landroidx/recyclerview/widget/RecyclerView$ItemAnimator;->getAddDuration()J

    move-result-wide v3

    goto :goto_b

    nop

    :goto_a
    return-void

    :goto_b
    invoke-virtual {v2, v3, v4}, Landroid/view/ViewPropertyAnimator;->setDuration(J)Landroid/view/ViewPropertyAnimator;

    move-result-object v2

    goto :goto_3

    nop

    :goto_c
    iget-object v0, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    goto :goto_d

    nop

    :goto_d
    invoke-virtual {v0}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object v1

    goto :goto_2

    nop

    :goto_e
    invoke-direct {v3, p0, p1, v0, v1}, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$5;-><init>(Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;Landroidx/recyclerview/widget/RecyclerView$ViewHolder;Landroid/view/View;Landroid/view/ViewPropertyAnimator;)V

    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_recyclerview_widget_MiuiDefaultItemAnimator__animateChangeImpl',
        'method': '.method animateChangeImpl(Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$ChangeInfo;)V',
        'method_name': 'animateChangeImpl',
        'method_anchors': ['iget-object v0, p1, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$ChangeInfo;->oldHolder:Landroidx/recyclerview/widget/RecyclerView$ViewHolder;', 'if-nez v0, :cond_0', 'iget-object v0, v0, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;', 'iget-object v2, p1, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$ChangeInfo;->newHolder:Landroidx/recyclerview/widget/RecyclerView$ViewHolder;', 'if-eqz v2, :cond_1', 'iget-object v1, v2, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;', 'if-eqz v0, :cond_2', 'invoke-virtual {v0}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;'],
        'type': 'method_replace',
        'search': """.method animateChangeImpl(Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$ChangeInfo;)V
    .registers 9

    iget-object v0, p1, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$ChangeInfo;->oldHolder:Landroidx/recyclerview/widget/RecyclerView$ViewHolder;

    const/4 v1, 0x0

    if-nez v0, :cond_0

    move-object v0, v1

    goto :goto_0

    :cond_0
    iget-object v0, v0, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    :goto_0
    iget-object v2, p1, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$ChangeInfo;->newHolder:Landroidx/recyclerview/widget/RecyclerView$ViewHolder;

    if-eqz v2, :cond_1

    iget-object v1, v2, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    :cond_1
    const/4 v2, 0x0

    if-eqz v0, :cond_2

    invoke-virtual {v0}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object v3

    invoke-virtual {p0}, Landroidx/recyclerview/widget/RecyclerView$ItemAnimator;->getChangeDuration()J

    move-result-wide v4

    invoke-virtual {v3, v4, v5}, Landroid/view/ViewPropertyAnimator;->setDuration(J)Landroid/view/ViewPropertyAnimator;

    move-result-object v3

    iget-object v4, p0, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->mChangeAnimations:Ljava/util/ArrayList;

    iget-object v5, p1, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$ChangeInfo;->oldHolder:Landroidx/recyclerview/widget/RecyclerView$ViewHolder;

    invoke-virtual {v4, v5}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    sget-object v4, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->INTERPOLATOR:Landroid/animation/TimeInterpolator;

    invoke-virtual {v3, v4}, Landroid/view/ViewPropertyAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)Landroid/view/ViewPropertyAnimator;

    iget v4, p1, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$ChangeInfo;->toX:I

    int-to-float v4, v4

    iget v5, p1, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$ChangeInfo;->fromX:I

    int-to-float v5, v5

    sub-float/2addr v4, v5

    iget v5, p1, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$ChangeInfo;->toY:I

    int-to-float v5, v5

    iget v6, p1, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$ChangeInfo;->fromY:I

    int-to-float v6, v6

    sub-float/2addr v5, v6

    invoke-virtual {v3, v4}, Landroid/view/ViewPropertyAnimator;->translationX(F)Landroid/view/ViewPropertyAnimator;

    invoke-virtual {v3, v5}, Landroid/view/ViewPropertyAnimator;->translationY(F)Landroid/view/ViewPropertyAnimator;

    invoke-virtual {v3, v2}, Landroid/view/ViewPropertyAnimator;->alpha(F)Landroid/view/ViewPropertyAnimator;

    move-result-object v4

    new-instance v5, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$7;

    invoke-direct {v5, p0, p1, v3, v0}, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$7;-><init>(Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$ChangeInfo;Landroid/view/ViewPropertyAnimator;Landroid/view/View;)V

    invoke-virtual {v4, v5}, Landroid/view/ViewPropertyAnimator;->setListener(Landroid/animation/Animator$AnimatorListener;)Landroid/view/ViewPropertyAnimator;

    move-result-object v0

    invoke-virtual {v0}, Landroid/view/ViewPropertyAnimator;->start()V

    :cond_2
    if-eqz v1, :cond_3

    invoke-virtual {v1}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object v0

    iget-object v3, p0, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->mChangeAnimations:Ljava/util/ArrayList;

    iget-object v4, p1, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$ChangeInfo;->newHolder:Landroidx/recyclerview/widget/RecyclerView$ViewHolder;

    invoke-virtual {v3, v4}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    sget-object v3, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->INTERPOLATOR:Landroid/animation/TimeInterpolator;

    invoke-virtual {v0, v3}, Landroid/view/ViewPropertyAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)Landroid/view/ViewPropertyAnimator;

    invoke-virtual {v0, v2}, Landroid/view/ViewPropertyAnimator;->translationX(F)Landroid/view/ViewPropertyAnimator;

    move-result-object v3

    invoke-virtual {v3, v2}, Landroid/view/ViewPropertyAnimator;->translationY(F)Landroid/view/ViewPropertyAnimator;

    move-result-object v2

    invoke-virtual {p0}, Landroidx/recyclerview/widget/RecyclerView$ItemAnimator;->getChangeDuration()J

    move-result-wide v3

    invoke-virtual {v2, v3, v4}, Landroid/view/ViewPropertyAnimator;->setDuration(J)Landroid/view/ViewPropertyAnimator;

    move-result-object v2

    const/high16 v3, 0x3f800000

    invoke-virtual {v2, v3}, Landroid/view/ViewPropertyAnimator;->alpha(F)Landroid/view/ViewPropertyAnimator;

    move-result-object v2

    new-instance v3, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$8;

    invoke-direct {v3, p0, p1, v0, v1}, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$8;-><init>(Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$ChangeInfo;Landroid/view/ViewPropertyAnimator;Landroid/view/View;)V

    invoke-virtual {v2, v3}, Landroid/view/ViewPropertyAnimator;->setListener(Landroid/animation/Animator$AnimatorListener;)Landroid/view/ViewPropertyAnimator;

    move-result-object p0

    invoke-virtual {p0}, Landroid/view/ViewPropertyAnimator;->start()V

    :cond_3
    return-void
.end method""",
        'replacement': """.method animateChangeImpl(Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$ChangeInfo;)V
    .registers 9

    goto :goto_2

    nop

    :goto_0
    int-to-float v5, v5

    goto :goto_31

    nop

    :goto_1
    invoke-virtual {v0, v3}, Landroid/view/ViewPropertyAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)Landroid/view/ViewPropertyAnimator;

    goto :goto_3

    nop

    :goto_2
    iget-object v0, p1, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$ChangeInfo;->oldHolder:Landroidx/recyclerview/widget/RecyclerView$ViewHolder;

    goto :goto_4

    nop

    :goto_3
    invoke-virtual {v0, v2}, Landroid/view/ViewPropertyAnimator;->translationX(F)Landroid/view/ViewPropertyAnimator;

    move-result-object v3

    goto :goto_21

    nop

    :goto_4
    const/4 v1, 0x0

    goto :goto_8

    nop

    :goto_5
    invoke-virtual {p0}, Landroidx/recyclerview/widget/RecyclerView$ItemAnimator;->getChangeDuration()J

    move-result-wide v4

    goto :goto_1e

    nop

    :goto_6
    return-void

    :goto_7
    if-nez v0, :cond_0

    goto :goto_f

    :cond_0
    goto :goto_32

    nop

    :goto_8
    if-eqz v0, :cond_1

    goto :goto_20

    :cond_1
    goto :goto_19

    nop

    :goto_9
    invoke-virtual {v3, v4}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_2e

    nop

    :goto_a
    iget-object v1, v2, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    :goto_b
    goto :goto_2f

    nop

    :goto_c
    invoke-virtual {p0}, Landroidx/recyclerview/widget/RecyclerView$ItemAnimator;->getChangeDuration()J

    move-result-wide v3

    goto :goto_12

    nop

    :goto_d
    int-to-float v4, v4

    goto :goto_36

    nop

    :goto_e
    invoke-virtual {v0}, Landroid/view/ViewPropertyAnimator;->start()V

    :goto_f
    goto :goto_29

    nop

    :goto_10
    if-nez v2, :cond_2

    goto :goto_b

    :cond_2
    goto :goto_a

    nop

    :goto_11
    iget-object v2, p1, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$ChangeInfo;->newHolder:Landroidx/recyclerview/widget/RecyclerView$ViewHolder;

    goto :goto_10

    nop

    :goto_12
    invoke-virtual {v2, v3, v4}, Landroid/view/ViewPropertyAnimator;->setDuration(J)Landroid/view/ViewPropertyAnimator;

    move-result-object v2

    goto :goto_2d

    nop

    :goto_13
    new-instance v5, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$7;

    goto :goto_16

    nop

    :goto_14
    sget-object v4, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->INTERPOLATOR:Landroid/animation/TimeInterpolator;

    goto :goto_1c

    nop

    :goto_15
    iget v5, p1, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$ChangeInfo;->toY:I

    goto :goto_26

    nop

    :goto_16
    invoke-direct {v5, p0, p1, v3, v0}, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$7;-><init>(Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$ChangeInfo;Landroid/view/ViewPropertyAnimator;Landroid/view/View;)V

    goto :goto_2a

    nop

    :goto_17
    invoke-virtual {v3, v4}, Landroid/view/ViewPropertyAnimator;->translationX(F)Landroid/view/ViewPropertyAnimator;

    goto :goto_33

    nop

    :goto_18
    invoke-virtual {v3, v2}, Landroid/view/ViewPropertyAnimator;->alpha(F)Landroid/view/ViewPropertyAnimator;

    move-result-object v4

    goto :goto_13

    nop

    :goto_19
    move-object v0, v1

    goto :goto_1f

    nop

    :goto_1a
    invoke-virtual {p0}, Landroid/view/ViewPropertyAnimator;->start()V

    :goto_1b
    goto :goto_6

    nop

    :goto_1c
    invoke-virtual {v3, v4}, Landroid/view/ViewPropertyAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)Landroid/view/ViewPropertyAnimator;

    goto :goto_28

    nop

    :goto_1d
    invoke-virtual {v2, v3}, Landroid/view/ViewPropertyAnimator;->alpha(F)Landroid/view/ViewPropertyAnimator;

    move-result-object v2

    goto :goto_2c

    nop

    :goto_1e
    invoke-virtual {v3, v4, v5}, Landroid/view/ViewPropertyAnimator;->setDuration(J)Landroid/view/ViewPropertyAnimator;

    move-result-object v3

    goto :goto_30

    nop

    :goto_1f
    goto :goto_23

    :goto_20
    goto :goto_22

    nop

    :goto_21
    invoke-virtual {v3, v2}, Landroid/view/ViewPropertyAnimator;->translationY(F)Landroid/view/ViewPropertyAnimator;

    move-result-object v2

    goto :goto_c

    nop

    :goto_22
    iget-object v0, v0, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    :goto_23
    goto :goto_11

    nop

    :goto_24
    iget v6, p1, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$ChangeInfo;->fromY:I

    goto :goto_3a

    nop

    :goto_25
    invoke-direct {v3, p0, p1, v0, v1}, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$8;-><init>(Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$ChangeInfo;Landroid/view/ViewPropertyAnimator;Landroid/view/View;)V

    goto :goto_34

    nop

    :goto_26
    int-to-float v5, v5

    goto :goto_24

    nop

    :goto_27
    invoke-virtual {v1}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object v0

    goto :goto_39

    nop

    :goto_28
    iget v4, p1, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$ChangeInfo;->toX:I

    goto :goto_d

    nop

    :goto_29
    if-nez v1, :cond_3

    goto :goto_1b

    :cond_3
    goto :goto_27

    nop

    :goto_2a
    invoke-virtual {v4, v5}, Landroid/view/ViewPropertyAnimator;->setListener(Landroid/animation/Animator$AnimatorListener;)Landroid/view/ViewPropertyAnimator;

    move-result-object v0

    goto :goto_e

    nop

    :goto_2b
    iget-object v5, p1, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$ChangeInfo;->oldHolder:Landroidx/recyclerview/widget/RecyclerView$ViewHolder;

    goto :goto_35

    nop

    :goto_2c
    new-instance v3, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$8;

    goto :goto_25

    nop

    :goto_2d
    const/high16 v3, 0x3f800000

    goto :goto_1d

    nop

    :goto_2e
    sget-object v3, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->INTERPOLATOR:Landroid/animation/TimeInterpolator;

    goto :goto_1

    nop

    :goto_2f
    const/4 v2, 0x0

    goto :goto_7

    nop

    :goto_30
    iget-object v4, p0, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->mChangeAnimations:Ljava/util/ArrayList;

    goto :goto_2b

    nop

    :goto_31
    sub-float/2addr v4, v5

    goto :goto_15

    nop

    :goto_32
    invoke-virtual {v0}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object v3

    goto :goto_5

    nop

    :goto_33
    invoke-virtual {v3, v5}, Landroid/view/ViewPropertyAnimator;->translationY(F)Landroid/view/ViewPropertyAnimator;

    goto :goto_18

    nop

    :goto_34
    invoke-virtual {v2, v3}, Landroid/view/ViewPropertyAnimator;->setListener(Landroid/animation/Animator$AnimatorListener;)Landroid/view/ViewPropertyAnimator;

    move-result-object p0

    goto :goto_1a

    nop

    :goto_35
    invoke-virtual {v4, v5}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_14

    nop

    :goto_36
    iget v5, p1, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$ChangeInfo;->fromX:I

    goto :goto_0

    nop

    :goto_37
    sub-float/2addr v5, v6

    goto :goto_17

    nop

    :goto_38
    iget-object v4, p1, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$ChangeInfo;->newHolder:Landroidx/recyclerview/widget/RecyclerView$ViewHolder;

    goto :goto_9

    nop

    :goto_39
    iget-object v3, p0, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->mChangeAnimations:Ljava/util/ArrayList;

    goto :goto_38

    nop

    :goto_3a
    int-to-float v6, v6

    goto :goto_37

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_recyclerview_widget_MiuiDefaultItemAnimator__animateMoveImpl',
        'method': '.method animateMoveImpl(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;IIII)V',
        'method_name': 'animateMoveImpl',
        'method_anchors': ['iget-object v4, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;', 'if-eqz v3, :cond_0', 'invoke-virtual {v4}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;', 'invoke-virtual {p3, p2}, Landroid/view/ViewPropertyAnimator;->translationX(F)Landroid/view/ViewPropertyAnimator;', 'if-eqz v5, :cond_1', 'invoke-virtual {v4}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;', 'invoke-virtual {p3, p2}, Landroid/view/ViewPropertyAnimator;->translationY(F)Landroid/view/ViewPropertyAnimator;', 'invoke-virtual {v4}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;'],
        'type': 'method_replace',
        'search': """.method animateMoveImpl(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;IIII)V
    .registers 13

    iget-object v4, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    sub-int v3, p4, p2

    sub-int v5, p5, p3

    const/4 p2, 0x0

    if-eqz v3, :cond_0

    invoke-virtual {v4}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object p3

    invoke-virtual {p3, p2}, Landroid/view/ViewPropertyAnimator;->translationX(F)Landroid/view/ViewPropertyAnimator;

    :cond_0
    if-eqz v5, :cond_1

    invoke-virtual {v4}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object p3

    invoke-virtual {p3, p2}, Landroid/view/ViewPropertyAnimator;->translationY(F)Landroid/view/ViewPropertyAnimator;

    :cond_1
    invoke-virtual {v4}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object v6

    iget-object p2, p0, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->mMoveAnimations:Ljava/util/ArrayList;

    invoke-virtual {p2, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    sget-object p2, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->INTERPOLATOR:Landroid/animation/TimeInterpolator;

    invoke-virtual {v6, p2}, Landroid/view/ViewPropertyAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)Landroid/view/ViewPropertyAnimator;

    invoke-virtual {p0}, Landroidx/recyclerview/widget/RecyclerView$ItemAnimator;->getMoveDuration()J

    move-result-wide p2

    invoke-virtual {v6, p2, p3}, Landroid/view/ViewPropertyAnimator;->setDuration(J)Landroid/view/ViewPropertyAnimator;

    move-result-object p2

    new-instance v0, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$6;

    move-object v1, p0

    move-object v2, p1

    invoke-direct/range {v0 .. v6}, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$6;-><init>(Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;Landroidx/recyclerview/widget/RecyclerView$ViewHolder;ILandroid/view/View;ILandroid/view/ViewPropertyAnimator;)V

    invoke-virtual {p2, v0}, Landroid/view/ViewPropertyAnimator;->setListener(Landroid/animation/Animator$AnimatorListener;)Landroid/view/ViewPropertyAnimator;

    move-result-object p0

    invoke-virtual {p0}, Landroid/view/ViewPropertyAnimator;->start()V

    return-void
.end method""",
        'replacement': """.method animateMoveImpl(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;IIII)V
    .registers 13

    goto :goto_19

    nop

    :goto_0
    invoke-virtual {p3, p2}, Landroid/view/ViewPropertyAnimator;->translationY(F)Landroid/view/ViewPropertyAnimator;

    :goto_1
    goto :goto_2

    nop

    :goto_2
    invoke-virtual {v4}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object v6

    goto :goto_14

    nop

    :goto_3
    move-object v1, p0

    goto :goto_9

    nop

    :goto_4
    invoke-virtual {v4}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object p3

    goto :goto_0

    nop

    :goto_5
    if-nez v5, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_4

    nop

    :goto_6
    invoke-virtual {p2, v0}, Landroid/view/ViewPropertyAnimator;->setListener(Landroid/animation/Animator$AnimatorListener;)Landroid/view/ViewPropertyAnimator;

    move-result-object p0

    goto :goto_12

    nop

    :goto_7
    if-nez v3, :cond_1

    goto :goto_b

    :cond_1
    goto :goto_18

    nop

    :goto_8
    sub-int v5, p5, p3

    goto :goto_16

    nop

    :goto_9
    move-object v2, p1

    goto :goto_c

    nop

    :goto_a
    invoke-virtual {p3, p2}, Landroid/view/ViewPropertyAnimator;->translationX(F)Landroid/view/ViewPropertyAnimator;

    :goto_b
    goto :goto_5

    nop

    :goto_c
    invoke-direct/range {v0 .. v6}, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$6;-><init>(Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;Landroidx/recyclerview/widget/RecyclerView$ViewHolder;ILandroid/view/View;ILandroid/view/ViewPropertyAnimator;)V

    goto :goto_6

    nop

    :goto_d
    sget-object p2, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->INTERPOLATOR:Landroid/animation/TimeInterpolator;

    goto :goto_f

    nop

    :goto_e
    invoke-virtual {v6, p2, p3}, Landroid/view/ViewPropertyAnimator;->setDuration(J)Landroid/view/ViewPropertyAnimator;

    move-result-object p2

    goto :goto_11

    nop

    :goto_f
    invoke-virtual {v6, p2}, Landroid/view/ViewPropertyAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)Landroid/view/ViewPropertyAnimator;

    goto :goto_17

    nop

    :goto_10
    return-void

    :goto_11
    new-instance v0, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$6;

    goto :goto_3

    nop

    :goto_12
    invoke-virtual {p0}, Landroid/view/ViewPropertyAnimator;->start()V

    goto :goto_10

    nop

    :goto_13
    invoke-virtual {p2, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_d

    nop

    :goto_14
    iget-object p2, p0, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->mMoveAnimations:Ljava/util/ArrayList;

    goto :goto_13

    nop

    :goto_15
    sub-int v3, p4, p2

    goto :goto_8

    nop

    :goto_16
    const/4 p2, 0x0

    goto :goto_7

    nop

    :goto_17
    invoke-virtual {p0}, Landroidx/recyclerview/widget/RecyclerView$ItemAnimator;->getMoveDuration()J

    move-result-wide p2

    goto :goto_e

    nop

    :goto_18
    invoke-virtual {v4}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object p3

    goto :goto_a

    nop

    :goto_19
    iget-object v4, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    goto :goto_15

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_recyclerview_widget_MiuiDefaultItemAnimator__animateRemoveImpl',
        'method': '.method animateRemoveImpl(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)V',
        'method_name': 'animateRemoveImpl',
        'method_anchors': ['iget-object v0, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;', 'invoke-virtual {v0}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;', 'iget-object v2, p0, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->mRemoveAnimations:Ljava/util/ArrayList;', 'invoke-virtual {v2, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z', 'sget-object v2, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->INTERPOLATOR:Landroid/animation/TimeInterpolator;', 'invoke-virtual {v1, v2}, Landroid/view/ViewPropertyAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)Landroid/view/ViewPropertyAnimator;', 'invoke-virtual {p0}, Landroidx/recyclerview/widget/RecyclerView$ItemAnimator;->getRemoveDuration()J', 'invoke-virtual {v1, v2, v3}, Landroid/view/ViewPropertyAnimator;->setDuration(J)Landroid/view/ViewPropertyAnimator;'],
        'type': 'method_replace',
        'search': """.method animateRemoveImpl(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)V
    .registers 6

    iget-object v0, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    invoke-virtual {v0}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object v1

    iget-object v2, p0, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->mRemoveAnimations:Ljava/util/ArrayList;

    invoke-virtual {v2, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    sget-object v2, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->INTERPOLATOR:Landroid/animation/TimeInterpolator;

    invoke-virtual {v1, v2}, Landroid/view/ViewPropertyAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)Landroid/view/ViewPropertyAnimator;

    invoke-virtual {p0}, Landroidx/recyclerview/widget/RecyclerView$ItemAnimator;->getRemoveDuration()J

    move-result-wide v2

    invoke-virtual {v1, v2, v3}, Landroid/view/ViewPropertyAnimator;->setDuration(J)Landroid/view/ViewPropertyAnimator;

    move-result-object v2

    const/4 v3, 0x0

    invoke-virtual {v2, v3}, Landroid/view/ViewPropertyAnimator;->alpha(F)Landroid/view/ViewPropertyAnimator;

    move-result-object v2

    new-instance v3, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$4;

    invoke-direct {v3, p0, p1, v1, v0}, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$4;-><init>(Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;Landroidx/recyclerview/widget/RecyclerView$ViewHolder;Landroid/view/ViewPropertyAnimator;Landroid/view/View;)V

    invoke-virtual {v2, v3}, Landroid/view/ViewPropertyAnimator;->setListener(Landroid/animation/Animator$AnimatorListener;)Landroid/view/ViewPropertyAnimator;

    move-result-object p0

    invoke-virtual {p0}, Landroid/view/ViewPropertyAnimator;->start()V

    return-void
.end method""",
        'replacement': """.method animateRemoveImpl(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)V
    .registers 6

    goto :goto_0

    nop

    :goto_0
    iget-object v0, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    goto :goto_3

    nop

    :goto_1
    invoke-direct {v3, p0, p1, v1, v0}, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$4;-><init>(Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;Landroidx/recyclerview/widget/RecyclerView$ViewHolder;Landroid/view/ViewPropertyAnimator;Landroid/view/View;)V

    goto :goto_c

    nop

    :goto_2
    const/4 v3, 0x0

    goto :goto_7

    nop

    :goto_3
    invoke-virtual {v0}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object v1

    goto :goto_4

    nop

    :goto_4
    iget-object v2, p0, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->mRemoveAnimations:Ljava/util/ArrayList;

    goto :goto_8

    nop

    :goto_5
    invoke-virtual {v1, v2}, Landroid/view/ViewPropertyAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)Landroid/view/ViewPropertyAnimator;

    goto :goto_a

    nop

    :goto_6
    invoke-virtual {p0}, Landroid/view/ViewPropertyAnimator;->start()V

    goto :goto_d

    nop

    :goto_7
    invoke-virtual {v2, v3}, Landroid/view/ViewPropertyAnimator;->alpha(F)Landroid/view/ViewPropertyAnimator;

    move-result-object v2

    goto :goto_9

    nop

    :goto_8
    invoke-virtual {v2, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_b

    nop

    :goto_9
    new-instance v3, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator$4;

    goto :goto_1

    nop

    :goto_a
    invoke-virtual {p0}, Landroidx/recyclerview/widget/RecyclerView$ItemAnimator;->getRemoveDuration()J

    move-result-wide v2

    goto :goto_e

    nop

    :goto_b
    sget-object v2, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->INTERPOLATOR:Landroid/animation/TimeInterpolator;

    goto :goto_5

    nop

    :goto_c
    invoke-virtual {v2, v3}, Landroid/view/ViewPropertyAnimator;->setListener(Landroid/animation/Animator$AnimatorListener;)Landroid/view/ViewPropertyAnimator;

    move-result-object p0

    goto :goto_6

    nop

    :goto_d
    return-void

    :goto_e
    invoke-virtual {v1, v2, v3}, Landroid/view/ViewPropertyAnimator;->setDuration(J)Landroid/view/ViewPropertyAnimator;

    move-result-object v2

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_recyclerview_widget_MiuiDefaultItemAnimator__cancelAll',
        'method': '.method cancelAll(Ljava/util/List;)V',
        'method_name': 'cancelAll',
        'method_anchors': ['invoke-interface {p1}, Ljava/util/List;->size()I', 'if-ltz p0, :cond_0', 'invoke-interface {p1, p0}, Ljava/util/List;->get(I)Ljava/lang/Object;', 'check-cast v0, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;', 'iget-object v0, v0, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;', 'invoke-virtual {v0}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;', 'invoke-virtual {v0}, Landroid/view/ViewPropertyAnimator;->cancel()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method cancelAll(Ljava/util/List;)V
    .registers 3

    invoke-interface {p1}, Ljava/util/List;->size()I

    move-result p0

    add-int/lit8 p0, p0, -0x1

    :goto_0
    if-ltz p0, :cond_0

    invoke-interface {p1, p0}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;

    iget-object v0, v0, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    invoke-virtual {v0}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object v0

    invoke-virtual {v0}, Landroid/view/ViewPropertyAnimator;->cancel()V

    add-int/lit8 p0, p0, -0x1

    goto :goto_0

    :cond_0
    return-void
.end method""",
        'replacement': """.method cancelAll(Ljava/util/List;)V
    .registers 3

    goto :goto_7

    nop

    :goto_0
    invoke-virtual {v0}, Landroid/view/ViewPropertyAnimator;->cancel()V

    goto :goto_3

    nop

    :goto_1
    add-int/lit8 p0, p0, -0x1

    :goto_2
    goto :goto_9

    nop

    :goto_3
    add-int/lit8 p0, p0, -0x1

    goto :goto_a

    nop

    :goto_4
    invoke-virtual {v0}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object v0

    goto :goto_0

    nop

    :goto_5
    invoke-interface {p1, p0}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v0

    goto :goto_6

    nop

    :goto_6
    check-cast v0, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;

    goto :goto_c

    nop

    :goto_7
    invoke-interface {p1}, Ljava/util/List;->size()I

    move-result p0

    goto :goto_1

    nop

    :goto_8
    return-void

    :goto_9
    if-gez p0, :cond_0

    goto :goto_b

    :cond_0
    goto :goto_5

    nop

    :goto_a
    goto :goto_2

    :goto_b
    goto :goto_8

    nop

    :goto_c
    iget-object v0, v0, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_recyclerview_widget_MiuiDefaultItemAnimator__dispatchFinishedWhenDone',
        'method': '.method dispatchFinishedWhenDone()V',
        'method_name': 'dispatchFinishedWhenDone',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->isRunning()Z', 'if-nez v0, :cond_0', 'invoke-virtual {p0}, Landroidx/recyclerview/widget/RecyclerView$ItemAnimator;->dispatchAnimationsFinished()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method dispatchFinishedWhenDone()V
    .registers 2

    invoke-virtual {p0}, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->isRunning()Z

    move-result v0

    if-nez v0, :cond_0

    invoke-virtual {p0}, Landroidx/recyclerview/widget/RecyclerView$ItemAnimator;->dispatchAnimationsFinished()V

    :cond_0
    return-void
.end method""",
        'replacement': """.method dispatchFinishedWhenDone()V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    invoke-virtual {p0}, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->isRunning()Z

    move-result v0

    goto :goto_2

    nop

    :goto_2
    if-eqz v0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_3

    nop

    :goto_3
    invoke-virtual {p0}, Landroidx/recyclerview/widget/RecyclerView$ItemAnimator;->dispatchAnimationsFinished()V

    :goto_4
    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_recyclerview_widget_MiuiDefaultItemAnimator__onRemoveFromAddition',
        'method': '.method onRemoveFromAddition(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)V',
        'method_name': 'onRemoveFromAddition',
        'method_anchors': ['iget-object p0, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;', 'invoke-virtual {p0, p1}, Landroid/view/View;->setAlpha(F)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method onRemoveFromAddition(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)V
    .registers 2

    iget-object p0, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    const/high16 p1, 0x3f800000

    invoke-virtual {p0, p1}, Landroid/view/View;->setAlpha(F)V

    return-void
.end method""",
        'replacement': """.method onRemoveFromAddition(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    goto :goto_1

    nop

    :goto_1
    const/high16 p1, 0x3f800000

    goto :goto_3

    nop

    :goto_2
    return-void

    :goto_3
    invoke-virtual {p0, p1}, Landroid/view/View;->setAlpha(F)V

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_recyclerview_widget_MiuiDefaultItemAnimator__onRemoveFromMove',
        'method': '.method onRemoveFromMove(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)V',
        'method_name': 'onRemoveFromMove',
        'method_anchors': ['iget-object p0, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;', 'invoke-virtual {p0, p1}, Landroid/view/View;->setTranslationY(F)V', 'invoke-virtual {p0, p1}, Landroid/view/View;->setTranslationX(F)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method onRemoveFromMove(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)V
    .registers 2

    iget-object p0, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    const/4 p1, 0x0

    invoke-virtual {p0, p1}, Landroid/view/View;->setTranslationY(F)V

    invoke-virtual {p0, p1}, Landroid/view/View;->setTranslationX(F)V

    return-void
.end method""",
        'replacement': """.method onRemoveFromMove(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)V
    .registers 2

    goto :goto_3

    nop

    :goto_0
    invoke-virtual {p0, p1}, Landroid/view/View;->setTranslationY(F)V

    goto :goto_4

    nop

    :goto_1
    return-void

    :goto_2
    const/4 p1, 0x0

    goto :goto_0

    nop

    :goto_3
    iget-object p0, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    goto :goto_2

    nop

    :goto_4
    invoke-virtual {p0, p1}, Landroid/view/View;->setTranslationX(F)V

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_recyclerview_widget_MiuiDefaultItemAnimator__onRemoveFromPendingAddition',
        'method': '.method onRemoveFromPendingAddition(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)V',
        'method_name': 'onRemoveFromPendingAddition',
        'method_anchors': ['iget-object p0, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;', 'invoke-virtual {p0, p1}, Landroid/view/View;->setAlpha(F)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method onRemoveFromPendingAddition(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)V
    .registers 2

    iget-object p0, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    const/high16 p1, 0x3f800000

    invoke-virtual {p0, p1}, Landroid/view/View;->setAlpha(F)V

    return-void
.end method""",
        'replacement': """.method onRemoveFromPendingAddition(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)V
    .registers 2

    goto :goto_3

    nop

    :goto_0
    const/high16 p1, 0x3f800000

    goto :goto_2

    nop

    :goto_1
    return-void

    :goto_2
    invoke-virtual {p0, p1}, Landroid/view/View;->setAlpha(F)V

    goto :goto_1

    nop

    :goto_3
    iget-object p0, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_recyclerview_widget_MiuiDefaultItemAnimator__onRemoveFromPendingMove',
        'method': '.method onRemoveFromPendingMove(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)V',
        'method_name': 'onRemoveFromPendingMove',
        'method_anchors': ['iget-object p0, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;', 'invoke-virtual {p0, p1}, Landroid/view/View;->setTranslationY(F)V', 'invoke-virtual {p0, p1}, Landroid/view/View;->setTranslationX(F)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method onRemoveFromPendingMove(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)V
    .registers 2

    iget-object p0, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    const/4 p1, 0x0

    invoke-virtual {p0, p1}, Landroid/view/View;->setTranslationY(F)V

    invoke-virtual {p0, p1}, Landroid/view/View;->setTranslationX(F)V

    return-void
.end method""",
        'replacement': """.method onRemoveFromPendingMove(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)V
    .registers 2

    goto :goto_3

    nop

    :goto_0
    return-void

    :goto_1
    invoke-virtual {p0, p1}, Landroid/view/View;->setTranslationY(F)V

    goto :goto_4

    nop

    :goto_2
    const/4 p1, 0x0

    goto :goto_1

    nop

    :goto_3
    iget-object p0, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    goto :goto_2

    nop

    :goto_4
    invoke-virtual {p0, p1}, Landroid/view/View;->setTranslationX(F)V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_recyclerview_widget_MiuiDefaultItemAnimator__resetAnimation',
        'method': '.method resetAnimation(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)V',
        'method_name': 'resetAnimation',
        'method_anchors': ['sget-object v0, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->sDefaultInterpolator:Landroid/animation/TimeInterpolator;', 'if-nez v0, :cond_0', 'new-instance v0, Landroid/animation/ValueAnimator;', 'invoke-direct {v0}, Landroid/animation/ValueAnimator;-><init>()V', 'invoke-virtual {v0}, Landroid/animation/ValueAnimator;->getInterpolator()Landroid/animation/TimeInterpolator;', 'sput-object v0, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->sDefaultInterpolator:Landroid/animation/TimeInterpolator;', 'iget-object v0, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;', 'invoke-virtual {v0}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;'],
        'type': 'method_replace',
        'search': """.method resetAnimation(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)V
    .registers 4

    sget-object v0, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->sDefaultInterpolator:Landroid/animation/TimeInterpolator;

    if-nez v0, :cond_0

    new-instance v0, Landroid/animation/ValueAnimator;

    invoke-direct {v0}, Landroid/animation/ValueAnimator;-><init>()V

    invoke-virtual {v0}, Landroid/animation/ValueAnimator;->getInterpolator()Landroid/animation/TimeInterpolator;

    move-result-object v0

    sput-object v0, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->sDefaultInterpolator:Landroid/animation/TimeInterpolator;

    :cond_0
    iget-object v0, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    invoke-virtual {v0}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object v0

    sget-object v1, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->sDefaultInterpolator:Landroid/animation/TimeInterpolator;

    invoke-virtual {v0, v1}, Landroid/view/ViewPropertyAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)Landroid/view/ViewPropertyAnimator;

    invoke-virtual {p0, p1}, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->endAnimation(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)V

    return-void
.end method""",
        'replacement': """.method resetAnimation(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)V
    .registers 4

    goto :goto_1

    nop

    :goto_0
    invoke-virtual {v0}, Landroid/animation/ValueAnimator;->getInterpolator()Landroid/animation/TimeInterpolator;

    move-result-object v0

    goto :goto_6

    nop

    :goto_1
    sget-object v0, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->sDefaultInterpolator:Landroid/animation/TimeInterpolator;

    goto :goto_3

    nop

    :goto_2
    invoke-virtual {v0}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object v0

    goto :goto_a

    nop

    :goto_3
    if-eqz v0, :cond_0

    goto :goto_7

    :cond_0
    goto :goto_b

    nop

    :goto_4
    return-void

    :goto_5
    invoke-virtual {p0, p1}, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->endAnimation(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)V

    goto :goto_4

    nop

    :goto_6
    sput-object v0, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->sDefaultInterpolator:Landroid/animation/TimeInterpolator;

    :goto_7
    goto :goto_8

    nop

    :goto_8
    iget-object v0, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    goto :goto_2

    nop

    :goto_9
    invoke-direct {v0}, Landroid/animation/ValueAnimator;-><init>()V

    goto :goto_0

    nop

    :goto_a
    sget-object v1, Lmiuix/recyclerview/widget/MiuiDefaultItemAnimator;->sDefaultInterpolator:Landroid/animation/TimeInterpolator;

    goto :goto_c

    nop

    :goto_b
    new-instance v0, Landroid/animation/ValueAnimator;

    goto :goto_9

    nop

    :goto_c
    invoke-virtual {v0, v1}, Landroid/view/ViewPropertyAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)Landroid/view/ViewPropertyAnimator;

    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
