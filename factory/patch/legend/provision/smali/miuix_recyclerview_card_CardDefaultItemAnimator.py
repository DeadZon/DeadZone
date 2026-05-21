TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/recyclerview/card/CardDefaultItemAnimator.smali'
CLASS_FALLBACK_NAMES = ['CardDefaultItemAnimator.smali']
CLASS_ANCHORS = ['.super Landroidx/recyclerview/widget/SimpleItemAnimator;', '.field private static final INTERPOLATOR:Landroid/animation/TimeInterpolator;']

PATCHES = [
    {
        'id': 'miuix_recyclerview_card_CardDefaultItemAnimator__animateAddImpl',
        'method': '.method animateAddImpl(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)V',
        'method_name': 'animateAddImpl',
        'method_anchors': ['iget-object v0, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;', 'invoke-virtual {v0}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;', 'iget-object v2, p0, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->mAddAnimations:Ljava/util/ArrayList;', 'invoke-virtual {v2, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z', 'sget-object v2, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->INTERPOLATOR:Landroid/animation/TimeInterpolator;', 'invoke-virtual {v1, v2}, Landroid/view/ViewPropertyAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)Landroid/view/ViewPropertyAnimator;', 'invoke-virtual {v1, v2}, Landroid/view/ViewPropertyAnimator;->alpha(F)Landroid/view/ViewPropertyAnimator;', 'invoke-virtual {p0}, Landroidx/recyclerview/widget/RecyclerView$ItemAnimator;->getAddDuration()J'],
        'type': 'method_replace',
        'search': """.method animateAddImpl(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)V
    .registers 7

    iget-object v0, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    invoke-virtual {v0}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object v1

    iget-object v2, p0, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->mAddAnimations:Ljava/util/ArrayList;

    invoke-virtual {v2, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    sget-object v2, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->INTERPOLATOR:Landroid/animation/TimeInterpolator;

    invoke-virtual {v1, v2}, Landroid/view/ViewPropertyAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)Landroid/view/ViewPropertyAnimator;

    const/high16 v2, 0x3f800000

    invoke-virtual {v1, v2}, Landroid/view/ViewPropertyAnimator;->alpha(F)Landroid/view/ViewPropertyAnimator;

    move-result-object v2

    invoke-virtual {p0}, Landroidx/recyclerview/widget/RecyclerView$ItemAnimator;->getAddDuration()J

    move-result-wide v3

    invoke-virtual {v2, v3, v4}, Landroid/view/ViewPropertyAnimator;->setDuration(J)Landroid/view/ViewPropertyAnimator;

    move-result-object v2

    new-instance v3, Lmiuix/recyclerview/card/CardDefaultItemAnimator$2;

    invoke-direct {v3, p0, p1, v0, v1}, Lmiuix/recyclerview/card/CardDefaultItemAnimator$2;-><init>(Lmiuix/recyclerview/card/CardDefaultItemAnimator;Landroidx/recyclerview/widget/RecyclerView$ViewHolder;Landroid/view/View;Landroid/view/ViewPropertyAnimator;)V

    invoke-virtual {v2, v3}, Landroid/view/ViewPropertyAnimator;->setListener(Landroid/animation/Animator$AnimatorListener;)Landroid/view/ViewPropertyAnimator;

    move-result-object p0

    invoke-virtual {p0}, Landroid/view/ViewPropertyAnimator;->start()V

    return-void
.end method""",
        'replacement': """.method animateAddImpl(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)V
    .registers 7

    goto :goto_b

    nop

    :goto_0
    invoke-virtual {p0}, Landroidx/recyclerview/widget/RecyclerView$ItemAnimator;->getAddDuration()J

    move-result-wide v3

    goto :goto_6

    nop

    :goto_1
    invoke-direct {v3, p0, p1, v0, v1}, Lmiuix/recyclerview/card/CardDefaultItemAnimator$2;-><init>(Lmiuix/recyclerview/card/CardDefaultItemAnimator;Landroidx/recyclerview/widget/RecyclerView$ViewHolder;Landroid/view/View;Landroid/view/ViewPropertyAnimator;)V

    goto :goto_d

    nop

    :goto_2
    new-instance v3, Lmiuix/recyclerview/card/CardDefaultItemAnimator$2;

    goto :goto_1

    nop

    :goto_3
    return-void

    :goto_4
    invoke-virtual {v2, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_c

    nop

    :goto_5
    invoke-virtual {v1, v2}, Landroid/view/ViewPropertyAnimator;->alpha(F)Landroid/view/ViewPropertyAnimator;

    move-result-object v2

    goto :goto_0

    nop

    :goto_6
    invoke-virtual {v2, v3, v4}, Landroid/view/ViewPropertyAnimator;->setDuration(J)Landroid/view/ViewPropertyAnimator;

    move-result-object v2

    goto :goto_2

    nop

    :goto_7
    invoke-virtual {p0}, Landroid/view/ViewPropertyAnimator;->start()V

    goto :goto_3

    nop

    :goto_8
    invoke-virtual {v0}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object v1

    goto :goto_a

    nop

    :goto_9
    invoke-virtual {v1, v2}, Landroid/view/ViewPropertyAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)Landroid/view/ViewPropertyAnimator;

    goto :goto_e

    nop

    :goto_a
    iget-object v2, p0, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->mAddAnimations:Ljava/util/ArrayList;

    goto :goto_4

    nop

    :goto_b
    iget-object v0, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    goto :goto_8

    nop

    :goto_c
    sget-object v2, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->INTERPOLATOR:Landroid/animation/TimeInterpolator;

    goto :goto_9

    nop

    :goto_d
    invoke-virtual {v2, v3}, Landroid/view/ViewPropertyAnimator;->setListener(Landroid/animation/Animator$AnimatorListener;)Landroid/view/ViewPropertyAnimator;

    move-result-object p0

    goto :goto_7

    nop

    :goto_e
    const/high16 v2, 0x3f800000

    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_recyclerview_card_CardDefaultItemAnimator__animateChangeImpl',
        'method': '.method animateChangeImpl(Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;)V',
        'method_name': 'animateChangeImpl',
        'method_anchors': ['invoke-static {p1}, Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;->access$100(Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;)Landroidx/recyclerview/widget/RecyclerView$ViewHolder;', 'if-nez v0, :cond_0', 'iget-object v0, v0, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;', 'invoke-static {p1}, Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;->access$500(Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;)Landroidx/recyclerview/widget/RecyclerView$ViewHolder;', 'if-eqz v2, :cond_1', 'iget-object v1, v2, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;', 'if-eqz v0, :cond_2', 'invoke-virtual {v0}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;'],
        'type': 'method_replace',
        'search': """.method animateChangeImpl(Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;)V
    .registers 9

    invoke-static {p1}, Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;->access$100(Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;)Landroidx/recyclerview/widget/RecyclerView$ViewHolder;

    move-result-object v0

    const/4 v1, 0x0

    if-nez v0, :cond_0

    move-object v0, v1

    goto :goto_0

    :cond_0
    iget-object v0, v0, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    :goto_0
    invoke-static {p1}, Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;->access$500(Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;)Landroidx/recyclerview/widget/RecyclerView$ViewHolder;

    move-result-object v2

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

    iget-object v4, p0, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->mChangeAnimations:Ljava/util/ArrayList;

    invoke-static {p1}, Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;->access$100(Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;)Landroidx/recyclerview/widget/RecyclerView$ViewHolder;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    sget-object v4, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->INTERPOLATOR:Landroid/animation/TimeInterpolator;

    invoke-virtual {v3, v4}, Landroid/view/ViewPropertyAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)Landroid/view/ViewPropertyAnimator;

    invoke-static {p1}, Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;->access$600(Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;)I

    move-result v4

    int-to-float v4, v4

    invoke-static {p1}, Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;->access$700(Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;)I

    move-result v5

    int-to-float v5, v5

    sub-float/2addr v4, v5

    invoke-static {p1}, Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;->access$800(Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;)I

    move-result v5

    int-to-float v5, v5

    invoke-static {p1}, Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;->access$900(Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;)I

    move-result v6

    int-to-float v6, v6

    sub-float/2addr v5, v6

    invoke-virtual {v3, v4}, Landroid/view/ViewPropertyAnimator;->translationX(F)Landroid/view/ViewPropertyAnimator;

    invoke-virtual {v3, v5}, Landroid/view/ViewPropertyAnimator;->translationY(F)Landroid/view/ViewPropertyAnimator;

    invoke-virtual {v3, v2}, Landroid/view/ViewPropertyAnimator;->alpha(F)Landroid/view/ViewPropertyAnimator;

    move-result-object v4

    new-instance v5, Lmiuix/recyclerview/card/CardDefaultItemAnimator$4;

    invoke-direct {v5, p0, p1, v3, v0}, Lmiuix/recyclerview/card/CardDefaultItemAnimator$4;-><init>(Lmiuix/recyclerview/card/CardDefaultItemAnimator;Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;Landroid/view/ViewPropertyAnimator;Landroid/view/View;)V

    invoke-virtual {v4, v5}, Landroid/view/ViewPropertyAnimator;->setListener(Landroid/animation/Animator$AnimatorListener;)Landroid/view/ViewPropertyAnimator;

    move-result-object v0

    invoke-virtual {v0}, Landroid/view/ViewPropertyAnimator;->start()V

    :cond_2
    if-eqz v1, :cond_3

    invoke-virtual {v1}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object v0

    iget-object v3, p0, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->mChangeAnimations:Ljava/util/ArrayList;

    invoke-static {p1}, Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;->access$500(Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;)Landroidx/recyclerview/widget/RecyclerView$ViewHolder;

    move-result-object v4

    invoke-virtual {v3, v4}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    sget-object v3, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->INTERPOLATOR:Landroid/animation/TimeInterpolator;

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

    new-instance v3, Lmiuix/recyclerview/card/CardDefaultItemAnimator$5;

    invoke-direct {v3, p0, p1, v0, v1}, Lmiuix/recyclerview/card/CardDefaultItemAnimator$5;-><init>(Lmiuix/recyclerview/card/CardDefaultItemAnimator;Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;Landroid/view/ViewPropertyAnimator;Landroid/view/View;)V

    invoke-virtual {v2, v3}, Landroid/view/ViewPropertyAnimator;->setListener(Landroid/animation/Animator$AnimatorListener;)Landroid/view/ViewPropertyAnimator;

    move-result-object p0

    invoke-virtual {p0}, Landroid/view/ViewPropertyAnimator;->start()V

    :cond_3
    return-void
.end method""",
        'replacement': """.method animateChangeImpl(Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;)V
    .registers 9

    goto :goto_20

    nop

    :goto_0
    invoke-static {p1}, Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;->access$500(Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;)Landroidx/recyclerview/widget/RecyclerView$ViewHolder;

    move-result-object v2

    goto :goto_e

    nop

    :goto_1
    if-nez v1, :cond_0

    goto :goto_15

    :cond_0
    goto :goto_2

    nop

    :goto_2
    invoke-virtual {v1}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object v0

    goto :goto_a

    nop

    :goto_3
    invoke-static {p1}, Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;->access$600(Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;)I

    move-result v4

    goto :goto_31

    nop

    :goto_4
    invoke-static {p1}, Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;->access$100(Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;)Landroidx/recyclerview/widget/RecyclerView$ViewHolder;

    move-result-object v5

    goto :goto_29

    nop

    :goto_5
    invoke-direct {v3, p0, p1, v0, v1}, Lmiuix/recyclerview/card/CardDefaultItemAnimator$5;-><init>(Lmiuix/recyclerview/card/CardDefaultItemAnimator;Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;Landroid/view/ViewPropertyAnimator;Landroid/view/View;)V

    goto :goto_1f

    nop

    :goto_6
    sub-float/2addr v4, v5

    goto :goto_11

    nop

    :goto_7
    invoke-virtual {v0, v3}, Landroid/view/ViewPropertyAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)Landroid/view/ViewPropertyAnimator;

    goto :goto_32

    nop

    :goto_8
    invoke-virtual {v3, v4, v5}, Landroid/view/ViewPropertyAnimator;->setDuration(J)Landroid/view/ViewPropertyAnimator;

    move-result-object v3

    goto :goto_27

    nop

    :goto_9
    const/4 v1, 0x0

    goto :goto_1a

    nop

    :goto_a
    iget-object v3, p0, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->mChangeAnimations:Ljava/util/ArrayList;

    goto :goto_25

    nop

    :goto_b
    int-to-float v5, v5

    goto :goto_23

    nop

    :goto_c
    sget-object v3, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->INTERPOLATOR:Landroid/animation/TimeInterpolator;

    goto :goto_7

    nop

    :goto_d
    const/4 v2, 0x0

    goto :goto_39

    nop

    :goto_e
    if-nez v2, :cond_1

    goto :goto_2e

    :cond_1
    goto :goto_2d

    nop

    :goto_f
    invoke-virtual {v0}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object v3

    goto :goto_17

    nop

    :goto_10
    new-instance v5, Lmiuix/recyclerview/card/CardDefaultItemAnimator$4;

    goto :goto_38

    nop

    :goto_11
    invoke-static {p1}, Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;->access$800(Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;)I

    move-result v5

    goto :goto_b

    nop

    :goto_12
    invoke-virtual {v0}, Landroid/view/ViewPropertyAnimator;->start()V

    :goto_13
    goto :goto_1

    nop

    :goto_14
    invoke-virtual {p0}, Landroid/view/ViewPropertyAnimator;->start()V

    :goto_15
    goto :goto_33

    nop

    :goto_16
    int-to-float v6, v6

    goto :goto_21

    nop

    :goto_17
    invoke-virtual {p0}, Landroidx/recyclerview/widget/RecyclerView$ItemAnimator;->getChangeDuration()J

    move-result-wide v4

    goto :goto_8

    nop

    :goto_18
    invoke-virtual {v3, v4}, Landroid/view/ViewPropertyAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)Landroid/view/ViewPropertyAnimator;

    goto :goto_3

    nop

    :goto_19
    invoke-virtual {v3, v5}, Landroid/view/ViewPropertyAnimator;->translationY(F)Landroid/view/ViewPropertyAnimator;

    goto :goto_22

    nop

    :goto_1a
    if-eqz v0, :cond_2

    goto :goto_2b

    :cond_2
    goto :goto_1d

    nop

    :goto_1b
    iget-object v0, v0, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    :goto_1c
    goto :goto_0

    nop

    :goto_1d
    move-object v0, v1

    goto :goto_2a

    nop

    :goto_1e
    invoke-virtual {v2, v3}, Landroid/view/ViewPropertyAnimator;->alpha(F)Landroid/view/ViewPropertyAnimator;

    move-result-object v2

    goto :goto_36

    nop

    :goto_1f
    invoke-virtual {v2, v3}, Landroid/view/ViewPropertyAnimator;->setListener(Landroid/animation/Animator$AnimatorListener;)Landroid/view/ViewPropertyAnimator;

    move-result-object p0

    goto :goto_14

    nop

    :goto_20
    invoke-static {p1}, Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;->access$100(Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;)Landroidx/recyclerview/widget/RecyclerView$ViewHolder;

    move-result-object v0

    goto :goto_9

    nop

    :goto_21
    sub-float/2addr v5, v6

    goto :goto_30

    nop

    :goto_22
    invoke-virtual {v3, v2}, Landroid/view/ViewPropertyAnimator;->alpha(F)Landroid/view/ViewPropertyAnimator;

    move-result-object v4

    goto :goto_10

    nop

    :goto_23
    invoke-static {p1}, Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;->access$900(Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;)I

    move-result v6

    goto :goto_16

    nop

    :goto_24
    invoke-virtual {p0}, Landroidx/recyclerview/widget/RecyclerView$ItemAnimator;->getChangeDuration()J

    move-result-wide v3

    goto :goto_2c

    nop

    :goto_25
    invoke-static {p1}, Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;->access$500(Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;)Landroidx/recyclerview/widget/RecyclerView$ViewHolder;

    move-result-object v4

    goto :goto_37

    nop

    :goto_26
    invoke-virtual {v4, v5}, Landroid/view/ViewPropertyAnimator;->setListener(Landroid/animation/Animator$AnimatorListener;)Landroid/view/ViewPropertyAnimator;

    move-result-object v0

    goto :goto_12

    nop

    :goto_27
    iget-object v4, p0, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->mChangeAnimations:Ljava/util/ArrayList;

    goto :goto_4

    nop

    :goto_28
    invoke-static {p1}, Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;->access$700(Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;)I

    move-result v5

    goto :goto_2f

    nop

    :goto_29
    invoke-virtual {v4, v5}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_34

    nop

    :goto_2a
    goto :goto_1c

    :goto_2b
    goto :goto_1b

    nop

    :goto_2c
    invoke-virtual {v2, v3, v4}, Landroid/view/ViewPropertyAnimator;->setDuration(J)Landroid/view/ViewPropertyAnimator;

    move-result-object v2

    goto :goto_3a

    nop

    :goto_2d
    iget-object v1, v2, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    :goto_2e
    goto :goto_d

    nop

    :goto_2f
    int-to-float v5, v5

    goto :goto_6

    nop

    :goto_30
    invoke-virtual {v3, v4}, Landroid/view/ViewPropertyAnimator;->translationX(F)Landroid/view/ViewPropertyAnimator;

    goto :goto_19

    nop

    :goto_31
    int-to-float v4, v4

    goto :goto_28

    nop

    :goto_32
    invoke-virtual {v0, v2}, Landroid/view/ViewPropertyAnimator;->translationX(F)Landroid/view/ViewPropertyAnimator;

    move-result-object v3

    goto :goto_35

    nop

    :goto_33
    return-void

    :goto_34
    sget-object v4, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->INTERPOLATOR:Landroid/animation/TimeInterpolator;

    goto :goto_18

    nop

    :goto_35
    invoke-virtual {v3, v2}, Landroid/view/ViewPropertyAnimator;->translationY(F)Landroid/view/ViewPropertyAnimator;

    move-result-object v2

    goto :goto_24

    nop

    :goto_36
    new-instance v3, Lmiuix/recyclerview/card/CardDefaultItemAnimator$5;

    goto :goto_5

    nop

    :goto_37
    invoke-virtual {v3, v4}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_c

    nop

    :goto_38
    invoke-direct {v5, p0, p1, v3, v0}, Lmiuix/recyclerview/card/CardDefaultItemAnimator$4;-><init>(Lmiuix/recyclerview/card/CardDefaultItemAnimator;Lmiuix/recyclerview/card/CardDefaultItemAnimator$ChangeInfo;Landroid/view/ViewPropertyAnimator;Landroid/view/View;)V

    goto :goto_26

    nop

    :goto_39
    if-nez v0, :cond_3

    goto :goto_13

    :cond_3
    goto :goto_f

    nop

    :goto_3a
    const/high16 v3, 0x3f800000

    goto :goto_1e

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_recyclerview_card_CardDefaultItemAnimator__animateMoveImpl',
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

    iget-object p2, p0, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->mMoveAnimations:Ljava/util/ArrayList;

    invoke-virtual {p2, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    sget-object p2, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->INTERPOLATOR:Landroid/animation/TimeInterpolator;

    invoke-virtual {v6, p2}, Landroid/view/ViewPropertyAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)Landroid/view/ViewPropertyAnimator;

    invoke-virtual {p0}, Landroidx/recyclerview/widget/RecyclerView$ItemAnimator;->getMoveDuration()J

    move-result-wide p2

    invoke-virtual {v6, p2, p3}, Landroid/view/ViewPropertyAnimator;->setDuration(J)Landroid/view/ViewPropertyAnimator;

    move-result-object p2

    new-instance v0, Lmiuix/recyclerview/card/CardDefaultItemAnimator$3;

    move-object v1, p0

    move-object v2, p1

    invoke-direct/range {v0 .. v6}, Lmiuix/recyclerview/card/CardDefaultItemAnimator$3;-><init>(Lmiuix/recyclerview/card/CardDefaultItemAnimator;Landroidx/recyclerview/widget/RecyclerView$ViewHolder;ILandroid/view/View;ILandroid/view/ViewPropertyAnimator;)V

    invoke-virtual {p2, v0}, Landroid/view/ViewPropertyAnimator;->setListener(Landroid/animation/Animator$AnimatorListener;)Landroid/view/ViewPropertyAnimator;

    move-result-object p0

    invoke-virtual {p0}, Landroid/view/ViewPropertyAnimator;->start()V

    return-void
.end method""",
        'replacement': """.method animateMoveImpl(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;IIII)V
    .registers 13

    goto :goto_a

    nop

    :goto_0
    invoke-virtual {v4}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object p3

    goto :goto_17

    nop

    :goto_1
    if-nez v5, :cond_0

    goto :goto_18

    :cond_0
    goto :goto_0

    nop

    :goto_2
    sub-int v5, p5, p3

    goto :goto_10

    nop

    :goto_3
    return-void

    :goto_4
    move-object v1, p0

    goto :goto_6

    nop

    :goto_5
    invoke-virtual {v4}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object v6

    goto :goto_9

    nop

    :goto_6
    move-object v2, p1

    goto :goto_15

    nop

    :goto_7
    invoke-virtual {p2, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_14

    nop

    :goto_8
    invoke-virtual {p0}, Landroid/view/ViewPropertyAnimator;->start()V

    goto :goto_3

    nop

    :goto_9
    iget-object p2, p0, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->mMoveAnimations:Ljava/util/ArrayList;

    goto :goto_7

    nop

    :goto_a
    iget-object v4, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    goto :goto_b

    nop

    :goto_b
    sub-int v3, p4, p2

    goto :goto_2

    nop

    :goto_c
    invoke-virtual {v6, p2, p3}, Landroid/view/ViewPropertyAnimator;->setDuration(J)Landroid/view/ViewPropertyAnimator;

    move-result-object p2

    goto :goto_13

    nop

    :goto_d
    invoke-virtual {p3, p2}, Landroid/view/ViewPropertyAnimator;->translationX(F)Landroid/view/ViewPropertyAnimator;

    :goto_e
    goto :goto_1

    nop

    :goto_f
    invoke-virtual {p2, v0}, Landroid/view/ViewPropertyAnimator;->setListener(Landroid/animation/Animator$AnimatorListener;)Landroid/view/ViewPropertyAnimator;

    move-result-object p0

    goto :goto_8

    nop

    :goto_10
    const/4 p2, 0x0

    goto :goto_16

    nop

    :goto_11
    invoke-virtual {p0}, Landroidx/recyclerview/widget/RecyclerView$ItemAnimator;->getMoveDuration()J

    move-result-wide p2

    goto :goto_c

    nop

    :goto_12
    invoke-virtual {v6, p2}, Landroid/view/ViewPropertyAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)Landroid/view/ViewPropertyAnimator;

    goto :goto_11

    nop

    :goto_13
    new-instance v0, Lmiuix/recyclerview/card/CardDefaultItemAnimator$3;

    goto :goto_4

    nop

    :goto_14
    sget-object p2, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->INTERPOLATOR:Landroid/animation/TimeInterpolator;

    goto :goto_12

    nop

    :goto_15
    invoke-direct/range {v0 .. v6}, Lmiuix/recyclerview/card/CardDefaultItemAnimator$3;-><init>(Lmiuix/recyclerview/card/CardDefaultItemAnimator;Landroidx/recyclerview/widget/RecyclerView$ViewHolder;ILandroid/view/View;ILandroid/view/ViewPropertyAnimator;)V

    goto :goto_f

    nop

    :goto_16
    if-nez v3, :cond_1

    goto :goto_e

    :cond_1
    goto :goto_19

    nop

    :goto_17
    invoke-virtual {p3, p2}, Landroid/view/ViewPropertyAnimator;->translationY(F)Landroid/view/ViewPropertyAnimator;

    :goto_18
    goto :goto_5

    nop

    :goto_19
    invoke-virtual {v4}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object p3

    goto :goto_d

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_recyclerview_card_CardDefaultItemAnimator__animateRemoveImpl',
        'method': '.method animateRemoveImpl(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)V',
        'method_name': 'animateRemoveImpl',
        'method_anchors': ['iget-object v0, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;', 'invoke-virtual {v0}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;', 'iget-object v2, p0, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->mRemoveAnimations:Ljava/util/ArrayList;', 'invoke-virtual {v2, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z', 'sget-object v2, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->INTERPOLATOR:Landroid/animation/TimeInterpolator;', 'invoke-virtual {v1, v2}, Landroid/view/ViewPropertyAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)Landroid/view/ViewPropertyAnimator;', 'invoke-virtual {p0}, Landroidx/recyclerview/widget/RecyclerView$ItemAnimator;->getRemoveDuration()J', 'invoke-virtual {v1, v2, v3}, Landroid/view/ViewPropertyAnimator;->setDuration(J)Landroid/view/ViewPropertyAnimator;'],
        'type': 'method_replace',
        'search': """.method animateRemoveImpl(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)V
    .registers 6

    iget-object v0, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    invoke-virtual {v0}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object v1

    iget-object v2, p0, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->mRemoveAnimations:Ljava/util/ArrayList;

    invoke-virtual {v2, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    sget-object v2, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->INTERPOLATOR:Landroid/animation/TimeInterpolator;

    invoke-virtual {v1, v2}, Landroid/view/ViewPropertyAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)Landroid/view/ViewPropertyAnimator;

    invoke-virtual {p0}, Landroidx/recyclerview/widget/RecyclerView$ItemAnimator;->getRemoveDuration()J

    move-result-wide v2

    invoke-virtual {v1, v2, v3}, Landroid/view/ViewPropertyAnimator;->setDuration(J)Landroid/view/ViewPropertyAnimator;

    move-result-object v2

    const/4 v3, 0x0

    invoke-virtual {v2, v3}, Landroid/view/ViewPropertyAnimator;->alpha(F)Landroid/view/ViewPropertyAnimator;

    move-result-object v2

    new-instance v3, Lmiuix/recyclerview/card/CardDefaultItemAnimator$1;

    invoke-direct {v3, p0, p1, v1, v0}, Lmiuix/recyclerview/card/CardDefaultItemAnimator$1;-><init>(Lmiuix/recyclerview/card/CardDefaultItemAnimator;Landroidx/recyclerview/widget/RecyclerView$ViewHolder;Landroid/view/ViewPropertyAnimator;Landroid/view/View;)V

    invoke-virtual {v2, v3}, Landroid/view/ViewPropertyAnimator;->setListener(Landroid/animation/Animator$AnimatorListener;)Landroid/view/ViewPropertyAnimator;

    move-result-object p0

    invoke-virtual {p0}, Landroid/view/ViewPropertyAnimator;->start()V

    return-void
.end method""",
        'replacement': """.method animateRemoveImpl(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)V
    .registers 6

    goto :goto_3

    nop

    :goto_0
    invoke-virtual {p0}, Landroid/view/ViewPropertyAnimator;->start()V

    goto :goto_7

    nop

    :goto_1
    invoke-virtual {v1, v2, v3}, Landroid/view/ViewPropertyAnimator;->setDuration(J)Landroid/view/ViewPropertyAnimator;

    move-result-object v2

    goto :goto_8

    nop

    :goto_2
    invoke-direct {v3, p0, p1, v1, v0}, Lmiuix/recyclerview/card/CardDefaultItemAnimator$1;-><init>(Lmiuix/recyclerview/card/CardDefaultItemAnimator;Landroidx/recyclerview/widget/RecyclerView$ViewHolder;Landroid/view/ViewPropertyAnimator;Landroid/view/View;)V

    goto :goto_6

    nop

    :goto_3
    iget-object v0, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    goto :goto_d

    nop

    :goto_4
    new-instance v3, Lmiuix/recyclerview/card/CardDefaultItemAnimator$1;

    goto :goto_2

    nop

    :goto_5
    invoke-virtual {v2, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_c

    nop

    :goto_6
    invoke-virtual {v2, v3}, Landroid/view/ViewPropertyAnimator;->setListener(Landroid/animation/Animator$AnimatorListener;)Landroid/view/ViewPropertyAnimator;

    move-result-object p0

    goto :goto_0

    nop

    :goto_7
    return-void

    :goto_8
    const/4 v3, 0x0

    goto :goto_b

    nop

    :goto_9
    invoke-virtual {v1, v2}, Landroid/view/ViewPropertyAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)Landroid/view/ViewPropertyAnimator;

    goto :goto_e

    nop

    :goto_a
    iget-object v2, p0, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->mRemoveAnimations:Ljava/util/ArrayList;

    goto :goto_5

    nop

    :goto_b
    invoke-virtual {v2, v3}, Landroid/view/ViewPropertyAnimator;->alpha(F)Landroid/view/ViewPropertyAnimator;

    move-result-object v2

    goto :goto_4

    nop

    :goto_c
    sget-object v2, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->INTERPOLATOR:Landroid/animation/TimeInterpolator;

    goto :goto_9

    nop

    :goto_d
    invoke-virtual {v0}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object v1

    goto :goto_a

    nop

    :goto_e
    invoke-virtual {p0}, Landroidx/recyclerview/widget/RecyclerView$ItemAnimator;->getRemoveDuration()J

    move-result-wide v2

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_recyclerview_card_CardDefaultItemAnimator__cancelAll',
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

    goto :goto_2

    nop

    :goto_0
    invoke-virtual {v0}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object v0

    goto :goto_8

    nop

    :goto_1
    add-int/lit8 p0, p0, -0x1

    goto :goto_a

    nop

    :goto_2
    invoke-interface {p1}, Ljava/util/List;->size()I

    move-result p0

    goto :goto_3

    nop

    :goto_3
    add-int/lit8 p0, p0, -0x1

    :goto_4
    goto :goto_9

    nop

    :goto_5
    check-cast v0, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;

    goto :goto_7

    nop

    :goto_6
    return-void

    :goto_7
    iget-object v0, v0, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    goto :goto_0

    nop

    :goto_8
    invoke-virtual {v0}, Landroid/view/ViewPropertyAnimator;->cancel()V

    goto :goto_1

    nop

    :goto_9
    if-gez p0, :cond_0

    goto :goto_b

    :cond_0
    goto :goto_c

    nop

    :goto_a
    goto :goto_4

    :goto_b
    goto :goto_6

    nop

    :goto_c
    invoke-interface {p1, p0}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v0

    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_recyclerview_card_CardDefaultItemAnimator__dispatchFinishedWhenDone',
        'method': '.method dispatchFinishedWhenDone()V',
        'method_name': 'dispatchFinishedWhenDone',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->isRunning()Z', 'if-nez v0, :cond_0', 'invoke-virtual {p0}, Landroidx/recyclerview/widget/RecyclerView$ItemAnimator;->dispatchAnimationsFinished()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method dispatchFinishedWhenDone()V
    .registers 2

    invoke-virtual {p0}, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->isRunning()Z

    move-result v0

    if-nez v0, :cond_0

    invoke-virtual {p0}, Landroidx/recyclerview/widget/RecyclerView$ItemAnimator;->dispatchAnimationsFinished()V

    :cond_0
    return-void
.end method""",
        'replacement': """.method dispatchFinishedWhenDone()V
    .registers 2

    goto :goto_4

    nop

    :goto_0
    if-eqz v0, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_1

    nop

    :goto_1
    invoke-virtual {p0}, Landroidx/recyclerview/widget/RecyclerView$ItemAnimator;->dispatchAnimationsFinished()V

    :goto_2
    goto :goto_3

    nop

    :goto_3
    return-void

    :goto_4
    invoke-virtual {p0}, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->isRunning()Z

    move-result v0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_recyclerview_card_CardDefaultItemAnimator__onRemoveFromAddition',
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

    goto :goto_2

    nop

    :goto_0
    const/high16 p1, 0x3f800000

    goto :goto_1

    nop

    :goto_1
    invoke-virtual {p0, p1}, Landroid/view/View;->setAlpha(F)V

    goto :goto_3

    nop

    :goto_2
    iget-object p0, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    goto :goto_0

    nop

    :goto_3
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_recyclerview_card_CardDefaultItemAnimator__onRemoveFromMove',
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

    goto :goto_1

    nop

    :goto_0
    invoke-virtual {p0, p1}, Landroid/view/View;->setTranslationX(F)V

    goto :goto_2

    nop

    :goto_1
    iget-object p0, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    goto :goto_4

    nop

    :goto_2
    return-void

    :goto_3
    invoke-virtual {p0, p1}, Landroid/view/View;->setTranslationY(F)V

    goto :goto_0

    nop

    :goto_4
    const/4 p1, 0x0

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_recyclerview_card_CardDefaultItemAnimator__onRemoveFromPendingAddition',
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

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    goto :goto_3

    nop

    :goto_1
    return-void

    :goto_2
    invoke-virtual {p0, p1}, Landroid/view/View;->setAlpha(F)V

    goto :goto_1

    nop

    :goto_3
    const/high16 p1, 0x3f800000

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_recyclerview_card_CardDefaultItemAnimator__onRemoveFromPendingMove',
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

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    goto :goto_4

    nop

    :goto_1
    invoke-virtual {p0, p1}, Landroid/view/View;->setTranslationY(F)V

    goto :goto_2

    nop

    :goto_2
    invoke-virtual {p0, p1}, Landroid/view/View;->setTranslationX(F)V

    goto :goto_3

    nop

    :goto_3
    return-void

    :goto_4
    const/4 p1, 0x0

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_recyclerview_card_CardDefaultItemAnimator__resetAnimation',
        'method': '.method resetAnimation(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)V',
        'method_name': 'resetAnimation',
        'method_anchors': ['sget-object v0, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->sDefaultInterpolator:Landroid/animation/TimeInterpolator;', 'if-nez v0, :cond_0', 'new-instance v0, Landroid/animation/ValueAnimator;', 'invoke-direct {v0}, Landroid/animation/ValueAnimator;-><init>()V', 'invoke-virtual {v0}, Landroid/animation/ValueAnimator;->getInterpolator()Landroid/animation/TimeInterpolator;', 'sput-object v0, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->sDefaultInterpolator:Landroid/animation/TimeInterpolator;', 'iget-object v0, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;', 'invoke-virtual {v0}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;'],
        'type': 'method_replace',
        'search': """.method resetAnimation(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)V
    .registers 4

    sget-object v0, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->sDefaultInterpolator:Landroid/animation/TimeInterpolator;

    if-nez v0, :cond_0

    new-instance v0, Landroid/animation/ValueAnimator;

    invoke-direct {v0}, Landroid/animation/ValueAnimator;-><init>()V

    invoke-virtual {v0}, Landroid/animation/ValueAnimator;->getInterpolator()Landroid/animation/TimeInterpolator;

    move-result-object v0

    sput-object v0, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->sDefaultInterpolator:Landroid/animation/TimeInterpolator;

    :cond_0
    iget-object v0, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    invoke-virtual {v0}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object v0

    sget-object v1, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->sDefaultInterpolator:Landroid/animation/TimeInterpolator;

    invoke-virtual {v0, v1}, Landroid/view/ViewPropertyAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)Landroid/view/ViewPropertyAnimator;

    invoke-virtual {p0, p1}, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->endAnimation(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)V

    return-void
.end method""",
        'replacement': """.method resetAnimation(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)V
    .registers 4

    goto :goto_9

    nop

    :goto_0
    invoke-virtual {v0, v1}, Landroid/view/ViewPropertyAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)Landroid/view/ViewPropertyAnimator;

    goto :goto_4

    nop

    :goto_1
    iget-object v0, p1, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->itemView:Landroid/view/View;

    goto :goto_3

    nop

    :goto_2
    invoke-virtual {v0}, Landroid/animation/ValueAnimator;->getInterpolator()Landroid/animation/TimeInterpolator;

    move-result-object v0

    goto :goto_b

    nop

    :goto_3
    invoke-virtual {v0}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object v0

    goto :goto_6

    nop

    :goto_4
    invoke-virtual {p0, p1}, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->endAnimation(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)V

    goto :goto_7

    nop

    :goto_5
    invoke-direct {v0}, Landroid/animation/ValueAnimator;-><init>()V

    goto :goto_2

    nop

    :goto_6
    sget-object v1, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->sDefaultInterpolator:Landroid/animation/TimeInterpolator;

    goto :goto_0

    nop

    :goto_7
    return-void

    :goto_8
    if-eqz v0, :cond_0

    goto :goto_c

    :cond_0
    goto :goto_a

    nop

    :goto_9
    sget-object v0, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->sDefaultInterpolator:Landroid/animation/TimeInterpolator;

    goto :goto_8

    nop

    :goto_a
    new-instance v0, Landroid/animation/ValueAnimator;

    goto :goto_5

    nop

    :goto_b
    sput-object v0, Lmiuix/recyclerview/card/CardDefaultItemAnimator;->sDefaultInterpolator:Landroid/animation/TimeInterpolator;

    :goto_c
    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
