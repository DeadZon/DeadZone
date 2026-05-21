TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/androidbasewidget/adapter/FragmentStateAdapter.smali'
CLASS_FALLBACK_NAMES = ['FragmentStateAdapter.smali']
CLASS_ANCHORS = ['.super Landroidx/recyclerview/widget/RecyclerView$Adapter;', '.implements Lmiuix/androidbasewidget/adapter/StatefulAdapter;']

PATCHES = [
    {
        'id': 'miuix_androidbasewidget_adapter_FragmentStateAdapter__addViewToContainer',
        'method': '.method addViewToContainer(Landroid/view/View;Landroid/widget/FrameLayout;)V',
        'method_name': 'addViewToContainer',
        'method_anchors': ['invoke-virtual {p2}, Landroid/widget/FrameLayout;->getChildCount()I', 'if-gt p0, v0, :cond_3', 'invoke-virtual {p1}, Landroid/view/View;->getParent()Landroid/view/ViewParent;', 'if-ne p0, p2, :cond_0', 'return-void', 'invoke-virtual {p2}, Landroid/widget/FrameLayout;->getChildCount()I', 'if-lez p0, :cond_1', 'invoke-virtual {p2}, Landroid/widget/FrameLayout;->removeAllViews()V'],
        'type': 'method_replace',
        'search': """.method addViewToContainer(Landroid/view/View;Landroid/widget/FrameLayout;)V
    .registers 4

    invoke-virtual {p2}, Landroid/widget/FrameLayout;->getChildCount()I

    move-result p0

    const/4 v0, 0x1

    if-gt p0, v0, :cond_3

    invoke-virtual {p1}, Landroid/view/View;->getParent()Landroid/view/ViewParent;

    move-result-object p0

    if-ne p0, p2, :cond_0

    return-void

    :cond_0
    invoke-virtual {p2}, Landroid/widget/FrameLayout;->getChildCount()I

    move-result p0

    if-lez p0, :cond_1

    invoke-virtual {p2}, Landroid/widget/FrameLayout;->removeAllViews()V

    :cond_1
    invoke-virtual {p1}, Landroid/view/View;->getParent()Landroid/view/ViewParent;

    move-result-object p0

    if-eqz p0, :cond_2

    invoke-virtual {p1}, Landroid/view/View;->getParent()Landroid/view/ViewParent;

    move-result-object p0

    check-cast p0, Landroid/view/ViewGroup;

    invoke-virtual {p0, p1}, Landroid/view/ViewGroup;->removeView(Landroid/view/View;)V

    :cond_2
    invoke-virtual {p2, p1}, Landroid/widget/FrameLayout;->addView(Landroid/view/View;)V

    return-void

    :cond_3
    new-instance p0, Ljava/lang/IllegalStateException;

    const-string p1, "Design assumption violated."

    invoke-direct {p0, p1}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    throw p0
.end method""",
        'replacement': """.method addViewToContainer(Landroid/view/View;Landroid/widget/FrameLayout;)V
    .registers 4

    goto :goto_2

    nop

    :goto_0
    if-nez p0, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_c

    nop

    :goto_1
    invoke-virtual {p1}, Landroid/view/View;->getParent()Landroid/view/ViewParent;

    move-result-object p0

    goto :goto_0

    nop

    :goto_2
    invoke-virtual {p2}, Landroid/widget/FrameLayout;->getChildCount()I

    move-result p0

    goto :goto_13

    nop

    :goto_3
    invoke-virtual {p2}, Landroid/widget/FrameLayout;->getChildCount()I

    move-result p0

    goto :goto_f

    nop

    :goto_4
    invoke-direct {p0, p1}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    goto :goto_b

    nop

    :goto_5
    invoke-virtual {p0, p1}, Landroid/view/ViewGroup;->removeView(Landroid/view/View;)V

    :goto_6
    goto :goto_17

    nop

    :goto_7
    invoke-virtual {p2}, Landroid/widget/FrameLayout;->removeAllViews()V

    :goto_8
    goto :goto_1

    nop

    :goto_9
    return-void

    :goto_a
    goto :goto_3

    nop

    :goto_b
    throw p0

    :goto_c
    invoke-virtual {p1}, Landroid/view/View;->getParent()Landroid/view/ViewParent;

    move-result-object p0

    goto :goto_16

    nop

    :goto_d
    return-void

    :goto_e
    goto :goto_12

    nop

    :goto_f
    if-gtz p0, :cond_1

    goto :goto_8

    :cond_1
    goto :goto_7

    nop

    :goto_10
    if-eq p0, p2, :cond_2

    goto :goto_a

    :cond_2
    goto :goto_9

    nop

    :goto_11
    if-le p0, v0, :cond_3

    goto :goto_e

    :cond_3
    goto :goto_14

    nop

    :goto_12
    new-instance p0, Ljava/lang/IllegalStateException;

    goto :goto_15

    nop

    :goto_13
    const/4 v0, 0x1

    goto :goto_11

    nop

    :goto_14
    invoke-virtual {p1}, Landroid/view/View;->getParent()Landroid/view/ViewParent;

    move-result-object p0

    goto :goto_10

    nop

    :goto_15
    const-string p1, "Design assumption violated."

    goto :goto_4

    nop

    :goto_16
    check-cast p0, Landroid/view/ViewGroup;

    goto :goto_5

    nop

    :goto_17
    invoke-virtual {p2, p1}, Landroid/widget/FrameLayout;->addView(Landroid/view/View;)V

    goto :goto_d

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_androidbasewidget_adapter_FragmentStateAdapter__gcFragments',
        'method': '.method gcFragments()V',
        'method_name': 'gcFragments',
        'method_anchors': ['iget-boolean v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mHasStaleFragments:Z', 'if-eqz v0, :cond_5', 'invoke-virtual {p0}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->shouldDelayFragmentTransactions()Z', 'if-eqz v0, :cond_0', 'new-instance v0, Landroidx/collection/ArraySet;', 'invoke-direct {v0}, Landroidx/collection/ArraySet;-><init>()V', 'iget-object v3, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mFragments:Landroidx/collection/LongSparseArray;', 'invoke-virtual {v3}, Landroidx/collection/LongSparseArray;->size()I'],
        'type': 'method_replace',
        'search': """.method gcFragments()V
    .registers 7

    iget-boolean v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mHasStaleFragments:Z

    if-eqz v0, :cond_5

    invoke-virtual {p0}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->shouldDelayFragmentTransactions()Z

    move-result v0

    if-eqz v0, :cond_0

    goto :goto_3

    :cond_0
    new-instance v0, Landroidx/collection/ArraySet;

    invoke-direct {v0}, Landroidx/collection/ArraySet;-><init>()V

    const/4 v1, 0x0

    move v2, v1

    :goto_0
    iget-object v3, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mFragments:Landroidx/collection/LongSparseArray;

    invoke-virtual {v3}, Landroidx/collection/LongSparseArray;->size()I

    move-result v3

    if-ge v2, v3, :cond_2

    iget-object v3, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mFragments:Landroidx/collection/LongSparseArray;

    invoke-virtual {v3, v2}, Landroidx/collection/LongSparseArray;->keyAt(I)J

    move-result-wide v3

    invoke-virtual {p0, v3, v4}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->containsItem(J)Z

    move-result v5

    if-nez v5, :cond_1

    invoke-static {v3, v4}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v5

    invoke-interface {v0, v5}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    iget-object v5, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mItemIdToViewHolder:Landroidx/collection/LongSparseArray;

    invoke-virtual {v5, v3, v4}, Landroidx/collection/LongSparseArray;->remove(J)V

    :cond_1
    add-int/lit8 v2, v2, 0x1

    goto :goto_0

    :cond_2
    iget-boolean v2, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mIsInGracePeriod:Z

    if-nez v2, :cond_4

    iput-boolean v1, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mHasStaleFragments:Z

    :goto_1
    iget-object v2, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mFragments:Landroidx/collection/LongSparseArray;

    invoke-virtual {v2}, Landroidx/collection/LongSparseArray;->size()I

    move-result v2

    if-ge v1, v2, :cond_4

    iget-object v2, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mFragments:Landroidx/collection/LongSparseArray;

    invoke-virtual {v2, v1}, Landroidx/collection/LongSparseArray;->keyAt(I)J

    move-result-wide v2

    invoke-direct {p0, v2, v3}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->isFragmentViewBound(J)Z

    move-result v4

    if-nez v4, :cond_3

    invoke-static {v2, v3}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v2

    invoke-interface {v0, v2}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    :cond_3
    add-int/lit8 v1, v1, 0x1

    goto :goto_1

    :cond_4
    invoke-interface {v0}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_2
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_5

    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Ljava/lang/Long;

    invoke-virtual {v1}, Ljava/lang/Long;->longValue()J

    move-result-wide v1

    invoke-direct {p0, v1, v2}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->removeFragment(J)V

    goto :goto_2

    :cond_5
    :goto_3
    return-void
.end method""",
        'replacement': """.method gcFragments()V
    .registers 7

    goto :goto_b

    nop

    :goto_0
    invoke-static {v2, v3}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v2

    goto :goto_21

    nop

    :goto_1
    if-lt v2, v3, :cond_0

    goto :goto_33

    :cond_0
    goto :goto_1c

    nop

    :goto_2
    if-nez v0, :cond_1

    goto :goto_8

    :cond_1
    goto :goto_1d

    nop

    :goto_3
    iget-object v5, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mItemIdToViewHolder:Landroidx/collection/LongSparseArray;

    goto :goto_26

    nop

    :goto_4
    return-void

    :goto_5
    goto :goto_8

    :goto_6
    goto :goto_18

    nop

    :goto_7
    goto :goto_24

    :goto_8
    goto :goto_4

    nop

    :goto_9
    invoke-interface {v0, v5}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    goto :goto_3

    nop

    :goto_a
    invoke-virtual {v2, v1}, Landroidx/collection/LongSparseArray;->keyAt(I)J

    move-result-wide v2

    goto :goto_19

    nop

    :goto_b
    iget-boolean v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mHasStaleFragments:Z

    goto :goto_2

    nop

    :goto_c
    move v2, v1

    :goto_d
    goto :goto_35

    nop

    :goto_e
    if-lt v1, v2, :cond_2

    goto :goto_11

    :cond_2
    goto :goto_2a

    nop

    :goto_f
    invoke-direct {p0, v1, v2}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->removeFragment(J)V

    goto :goto_7

    nop

    :goto_10
    goto :goto_15

    :goto_11
    goto :goto_23

    nop

    :goto_12
    if-eqz v2, :cond_3

    goto :goto_11

    :cond_3
    goto :goto_14

    nop

    :goto_13
    invoke-virtual {v1}, Ljava/lang/Long;->longValue()J

    move-result-wide v1

    goto :goto_f

    nop

    :goto_14
    iput-boolean v1, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mHasStaleFragments:Z

    :goto_15
    goto :goto_1e

    nop

    :goto_16
    add-int/lit8 v2, v2, 0x1

    goto :goto_32

    nop

    :goto_17
    invoke-direct {v0}, Landroidx/collection/ArraySet;-><init>()V

    goto :goto_31

    nop

    :goto_18
    new-instance v0, Landroidx/collection/ArraySet;

    goto :goto_17

    nop

    :goto_19
    invoke-direct {p0, v2, v3}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->isFragmentViewBound(J)Z

    move-result v4

    goto :goto_2f

    nop

    :goto_1a
    check-cast v1, Ljava/lang/Long;

    goto :goto_13

    nop

    :goto_1b
    if-nez v1, :cond_4

    goto :goto_8

    :cond_4
    goto :goto_1f

    nop

    :goto_1c
    iget-object v3, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mFragments:Landroidx/collection/LongSparseArray;

    goto :goto_34

    nop

    :goto_1d
    invoke-virtual {p0}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->shouldDelayFragmentTransactions()Z

    move-result v0

    goto :goto_2e

    nop

    :goto_1e
    iget-object v2, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mFragments:Landroidx/collection/LongSparseArray;

    goto :goto_30

    nop

    :goto_1f
    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    goto :goto_1a

    nop

    :goto_20
    invoke-static {v3, v4}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v5

    goto :goto_9

    nop

    :goto_21
    invoke-interface {v0, v2}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    :goto_22
    goto :goto_29

    nop

    :goto_23
    invoke-interface {v0}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_24
    goto :goto_2d

    nop

    :goto_25
    if-eqz v5, :cond_5

    goto :goto_27

    :cond_5
    goto :goto_20

    nop

    :goto_26
    invoke-virtual {v5, v3, v4}, Landroidx/collection/LongSparseArray;->remove(J)V

    :goto_27
    goto :goto_16

    nop

    :goto_28
    invoke-virtual {p0, v3, v4}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->containsItem(J)Z

    move-result v5

    goto :goto_25

    nop

    :goto_29
    add-int/lit8 v1, v1, 0x1

    goto :goto_10

    nop

    :goto_2a
    iget-object v2, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mFragments:Landroidx/collection/LongSparseArray;

    goto :goto_a

    nop

    :goto_2b
    iget-boolean v2, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mIsInGracePeriod:Z

    goto :goto_12

    nop

    :goto_2c
    invoke-virtual {v3}, Landroidx/collection/LongSparseArray;->size()I

    move-result v3

    goto :goto_1

    nop

    :goto_2d
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    goto :goto_1b

    nop

    :goto_2e
    if-nez v0, :cond_6

    goto :goto_6

    :cond_6
    goto :goto_5

    nop

    :goto_2f
    if-eqz v4, :cond_7

    goto :goto_22

    :cond_7
    goto :goto_0

    nop

    :goto_30
    invoke-virtual {v2}, Landroidx/collection/LongSparseArray;->size()I

    move-result v2

    goto :goto_e

    nop

    :goto_31
    const/4 v1, 0x0

    goto :goto_c

    nop

    :goto_32
    goto :goto_d

    :goto_33
    goto :goto_2b

    nop

    :goto_34
    invoke-virtual {v3, v2}, Landroidx/collection/LongSparseArray;->keyAt(I)J

    move-result-wide v3

    goto :goto_28

    nop

    :goto_35
    iget-object v3, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mFragments:Landroidx/collection/LongSparseArray;

    goto :goto_2c

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_androidbasewidget_adapter_FragmentStateAdapter__placeFragmentInViewHolder',
        'method': '.method placeFragmentInViewHolder(Lmiuix/androidbasewidget/adapter/FragmentViewHolder;)V',
        'method_name': 'placeFragmentInViewHolder',
        'method_anchors': ['iget-object v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mFragments:Landroidx/collection/LongSparseArray;', 'invoke-virtual {p1}, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->getItemId()J', 'invoke-virtual {v0, v1, v2}, Landroidx/collection/LongSparseArray;->get(J)Ljava/lang/Object;', 'check-cast v0, Landroidx/fragment/app/Fragment;', 'const-string v1, "Design assumption violated."', 'if-eqz v0, :cond_8', 'invoke-virtual {p1}, Lmiuix/androidbasewidget/adapter/FragmentViewHolder;->getContainer()Landroid/widget/FrameLayout;', 'invoke-virtual {v0}, Landroidx/fragment/app/Fragment;->getView()Landroid/view/View;'],
        'type': 'method_replace',
        'search': """.method placeFragmentInViewHolder(Lmiuix/androidbasewidget/adapter/FragmentViewHolder;)V
    .registers 7

    iget-object v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mFragments:Landroidx/collection/LongSparseArray;

    invoke-virtual {p1}, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->getItemId()J

    move-result-wide v1

    invoke-virtual {v0, v1, v2}, Landroidx/collection/LongSparseArray;->get(J)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroidx/fragment/app/Fragment;

    const-string v1, "Design assumption violated."

    if-eqz v0, :cond_8

    invoke-virtual {p1}, Lmiuix/androidbasewidget/adapter/FragmentViewHolder;->getContainer()Landroid/widget/FrameLayout;

    move-result-object v2

    invoke-virtual {v0}, Landroidx/fragment/app/Fragment;->getView()Landroid/view/View;

    move-result-object v3

    invoke-virtual {v0}, Landroidx/fragment/app/Fragment;->isAdded()Z

    move-result v4

    if-nez v4, :cond_1

    if-nez v3, :cond_0

    goto :goto_0

    :cond_0
    new-instance p0, Ljava/lang/IllegalStateException;

    invoke-direct {p0, v1}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    throw p0

    :cond_1
    :goto_0
    invoke-virtual {v0}, Landroidx/fragment/app/Fragment;->isAdded()Z

    move-result v1

    if-eqz v1, :cond_2

    if-nez v3, :cond_2

    invoke-direct {p0, v0, v2}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->scheduleViewAttach(Landroidx/fragment/app/Fragment;Landroid/widget/FrameLayout;)V

    return-void

    :cond_2
    invoke-virtual {v0}, Landroidx/fragment/app/Fragment;->isAdded()Z

    move-result v1

    if-eqz v1, :cond_3

    if-eqz v3, :cond_3

    invoke-virtual {v3}, Landroid/view/View;->getParent()Landroid/view/ViewParent;

    move-result-object v1

    if-eqz v1, :cond_3

    invoke-virtual {v3}, Landroid/view/View;->getParent()Landroid/view/ViewParent;

    move-result-object p1

    if-eq p1, v2, :cond_6

    invoke-virtual {p0, v3, v2}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->addViewToContainer(Landroid/view/View;Landroid/widget/FrameLayout;)V

    return-void

    :cond_3
    invoke-virtual {v0}, Landroidx/fragment/app/Fragment;->isAdded()Z

    move-result v1

    if-eqz v1, :cond_4

    invoke-virtual {p0, v3, v2}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->addViewToContainer(Landroid/view/View;Landroid/widget/FrameLayout;)V

    return-void

    :cond_4
    invoke-virtual {p0}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->shouldDelayFragmentTransactions()Z

    move-result v1

    if-nez v1, :cond_5

    invoke-direct {p0, v0, v2}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->scheduleViewAttach(Landroidx/fragment/app/Fragment;Landroid/widget/FrameLayout;)V

    iget-object v1, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mFragmentManager:Landroidx/fragment/app/FragmentManager;

    invoke-virtual {v1}, Landroidx/fragment/app/FragmentManager;->beginTransaction()Landroidx/fragment/app/FragmentTransaction;

    move-result-object v1

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "f"

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p1}, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->getItemId()J

    move-result-wide v3

    invoke-virtual {v2, v3, v4}, Ljava/lang/StringBuilder;->append(J)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p1

    invoke-virtual {v1, v0, p1}, Landroidx/fragment/app/FragmentTransaction;->add(Landroidx/fragment/app/Fragment;Ljava/lang/String;)Landroidx/fragment/app/FragmentTransaction;

    move-result-object p1

    sget-object v1, Landroidx/lifecycle/Lifecycle$State;->STARTED:Landroidx/lifecycle/Lifecycle$State;

    invoke-virtual {p1, v0, v1}, Landroidx/fragment/app/FragmentTransaction;->setMaxLifecycle(Landroidx/fragment/app/Fragment;Landroidx/lifecycle/Lifecycle$State;)Landroidx/fragment/app/FragmentTransaction;

    move-result-object p1

    invoke-virtual {p1}, Landroidx/fragment/app/FragmentTransaction;->commitNow()V

    iget-object p0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mFragmentMaxLifecycleEnforcer:Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;

    const/4 p1, 0x0

    invoke-virtual {p0, p1}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->updateFragmentMaxLifecycle(Z)V

    return-void

    :cond_5
    iget-object v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mFragmentManager:Landroidx/fragment/app/FragmentManager;

    invoke-virtual {v0}, Landroidx/fragment/app/FragmentManager;->isDestroyed()Z

    move-result v0

    if-eqz v0, :cond_7

    :cond_6
    return-void

    :cond_7
    iget-object v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mLifecycle:Landroidx/lifecycle/Lifecycle;

    new-instance v1, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$2;

    invoke-direct {v1, p0, p1}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$2;-><init>(Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;Lmiuix/androidbasewidget/adapter/FragmentViewHolder;)V

    invoke-virtual {v0, v1}, Landroidx/lifecycle/Lifecycle;->addObserver(Landroidx/lifecycle/LifecycleObserver;)V

    return-void

    :cond_8
    new-instance p0, Ljava/lang/IllegalStateException;

    invoke-direct {p0, v1}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    throw p0
.end method""",
        'replacement': """.method placeFragmentInViewHolder(Lmiuix/androidbasewidget/adapter/FragmentViewHolder;)V
    .registers 7

    goto :goto_30

    nop

    :goto_0
    invoke-virtual {v1}, Landroidx/fragment/app/FragmentManager;->beginTransaction()Landroidx/fragment/app/FragmentTransaction;

    move-result-object v1

    goto :goto_3b

    nop

    :goto_1
    invoke-virtual {v1, v0, p1}, Landroidx/fragment/app/FragmentTransaction;->add(Landroidx/fragment/app/Fragment;Ljava/lang/String;)Landroidx/fragment/app/FragmentTransaction;

    move-result-object p1

    goto :goto_1c

    nop

    :goto_2
    iget-object v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mFragmentManager:Landroidx/fragment/app/FragmentManager;

    goto :goto_44

    nop

    :goto_3
    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_34

    nop

    :goto_4
    if-eqz v3, :cond_0

    goto :goto_27

    :cond_0
    goto :goto_1e

    nop

    :goto_5
    if-eqz v1, :cond_1

    goto :goto_3a

    :cond_1
    goto :goto_b

    nop

    :goto_6
    invoke-virtual {v0, v1, v2}, Landroidx/collection/LongSparseArray;->get(J)Ljava/lang/Object;

    move-result-object v0

    goto :goto_2b

    nop

    :goto_7
    invoke-virtual {v0}, Landroidx/fragment/app/Fragment;->isAdded()Z

    move-result v1

    goto :goto_21

    nop

    :goto_8
    invoke-virtual {v0}, Landroidx/fragment/app/Fragment;->isAdded()Z

    move-result v1

    goto :goto_1b

    nop

    :goto_9
    if-ne p1, v2, :cond_2

    goto :goto_43

    :cond_2
    goto :goto_38

    nop

    :goto_a
    new-instance p0, Ljava/lang/IllegalStateException;

    goto :goto_10

    nop

    :goto_b
    invoke-direct {p0, v0, v2}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->scheduleViewAttach(Landroidx/fragment/app/Fragment;Landroid/widget/FrameLayout;)V

    goto :goto_23

    nop

    :goto_c
    if-nez v3, :cond_3

    goto :goto_3d

    :cond_3
    goto :goto_47

    nop

    :goto_d
    const-string v1, "Design assumption violated."

    goto :goto_2c

    nop

    :goto_e
    throw p0

    :goto_f
    goto :goto_19

    nop

    :goto_10
    invoke-direct {p0, v1}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    goto :goto_11

    nop

    :goto_11
    throw p0

    :goto_12
    return-void

    :goto_13
    goto :goto_a

    nop

    :goto_14
    invoke-direct {p0, v1}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    goto :goto_e

    nop

    :goto_15
    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p1

    goto :goto_1

    nop

    :goto_16
    invoke-virtual {p1, v0, v1}, Landroidx/fragment/app/FragmentTransaction;->setMaxLifecycle(Landroidx/fragment/app/Fragment;Landroidx/lifecycle/Lifecycle$State;)Landroidx/fragment/app/FragmentTransaction;

    move-result-object p1

    goto :goto_28

    nop

    :goto_17
    invoke-virtual {v3}, Landroid/view/View;->getParent()Landroid/view/ViewParent;

    move-result-object p1

    goto :goto_9

    nop

    :goto_18
    invoke-virtual {p0, v3, v2}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->addViewToContainer(Landroid/view/View;Landroid/widget/FrameLayout;)V

    goto :goto_24

    nop

    :goto_19
    invoke-virtual {v0}, Landroidx/fragment/app/Fragment;->isAdded()Z

    move-result v1

    goto :goto_35

    nop

    :goto_1a
    invoke-virtual {p0}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->shouldDelayFragmentTransactions()Z

    move-result v1

    goto :goto_5

    nop

    :goto_1b
    if-nez v1, :cond_4

    goto :goto_3d

    :cond_4
    goto :goto_c

    nop

    :goto_1c
    sget-object v1, Landroidx/lifecycle/Lifecycle$State;->STARTED:Landroidx/lifecycle/Lifecycle$State;

    goto :goto_16

    nop

    :goto_1d
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_33

    nop

    :goto_1e
    invoke-direct {p0, v0, v2}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->scheduleViewAttach(Landroidx/fragment/app/Fragment;Landroid/widget/FrameLayout;)V

    goto :goto_26

    nop

    :goto_1f
    iget-object v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mLifecycle:Landroidx/lifecycle/Lifecycle;

    goto :goto_31

    nop

    :goto_20
    invoke-virtual {v2, v3, v4}, Ljava/lang/StringBuilder;->append(J)Ljava/lang/StringBuilder;

    goto :goto_15

    nop

    :goto_21
    if-nez v1, :cond_5

    goto :goto_25

    :cond_5
    goto :goto_18

    nop

    :goto_22
    invoke-virtual {v0}, Landroidx/fragment/app/Fragment;->getView()Landroid/view/View;

    move-result-object v3

    goto :goto_2d

    nop

    :goto_23
    iget-object v1, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mFragmentManager:Landroidx/fragment/app/FragmentManager;

    goto :goto_0

    nop

    :goto_24
    return-void

    :goto_25
    goto :goto_1a

    nop

    :goto_26
    return-void

    :goto_27
    goto :goto_8

    nop

    :goto_28
    invoke-virtual {p1}, Landroidx/fragment/app/FragmentTransaction;->commitNow()V

    goto :goto_48

    nop

    :goto_29
    if-nez v1, :cond_6

    goto :goto_3d

    :cond_6
    goto :goto_17

    nop

    :goto_2a
    invoke-virtual {p0, p1}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->updateFragmentMaxLifecycle(Z)V

    goto :goto_39

    nop

    :goto_2b
    check-cast v0, Landroidx/fragment/app/Fragment;

    goto :goto_d

    nop

    :goto_2c
    if-nez v0, :cond_7

    goto :goto_13

    :cond_7
    goto :goto_37

    nop

    :goto_2d
    invoke-virtual {v0}, Landroidx/fragment/app/Fragment;->isAdded()Z

    move-result v4

    goto :goto_36

    nop

    :goto_2e
    invoke-virtual {v0, v1}, Landroidx/lifecycle/Lifecycle;->addObserver(Landroidx/lifecycle/LifecycleObserver;)V

    goto :goto_12

    nop

    :goto_2f
    new-instance p0, Ljava/lang/IllegalStateException;

    goto :goto_14

    nop

    :goto_30
    iget-object v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mFragments:Landroidx/collection/LongSparseArray;

    goto :goto_49

    nop

    :goto_31
    new-instance v1, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$2;

    goto :goto_3e

    nop

    :goto_32
    if-eqz v3, :cond_8

    goto :goto_46

    :cond_8
    goto :goto_45

    nop

    :goto_33
    invoke-virtual {p1}, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->getItemId()J

    move-result-wide v3

    goto :goto_20

    nop

    :goto_34
    const-string v3, "f"

    goto :goto_1d

    nop

    :goto_35
    if-nez v1, :cond_9

    goto :goto_27

    :cond_9
    goto :goto_4

    nop

    :goto_36
    if-eqz v4, :cond_a

    goto :goto_f

    :cond_a
    goto :goto_32

    nop

    :goto_37
    invoke-virtual {p1}, Lmiuix/androidbasewidget/adapter/FragmentViewHolder;->getContainer()Landroid/widget/FrameLayout;

    move-result-object v2

    goto :goto_22

    nop

    :goto_38
    invoke-virtual {p0, v3, v2}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->addViewToContainer(Landroid/view/View;Landroid/widget/FrameLayout;)V

    goto :goto_3c

    nop

    :goto_39
    return-void

    :goto_3a
    goto :goto_2

    nop

    :goto_3b
    new-instance v2, Ljava/lang/StringBuilder;

    goto :goto_3

    nop

    :goto_3c
    return-void

    :goto_3d
    goto :goto_7

    nop

    :goto_3e
    invoke-direct {v1, p0, p1}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$2;-><init>(Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;Lmiuix/androidbasewidget/adapter/FragmentViewHolder;)V

    goto :goto_2e

    nop

    :goto_3f
    return-void

    :goto_40
    goto :goto_1f

    nop

    :goto_41
    const/4 p1, 0x0

    goto :goto_2a

    nop

    :goto_42
    if-nez v0, :cond_b

    goto :goto_40

    :cond_b
    :goto_43
    goto :goto_3f

    nop

    :goto_44
    invoke-virtual {v0}, Landroidx/fragment/app/FragmentManager;->isDestroyed()Z

    move-result v0

    goto :goto_42

    nop

    :goto_45
    goto :goto_f

    :goto_46
    goto :goto_2f

    nop

    :goto_47
    invoke-virtual {v3}, Landroid/view/View;->getParent()Landroid/view/ViewParent;

    move-result-object v1

    goto :goto_29

    nop

    :goto_48
    iget-object p0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mFragmentMaxLifecycleEnforcer:Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;

    goto :goto_41

    nop

    :goto_49
    invoke-virtual {p1}, Landroidx/recyclerview/widget/RecyclerView$ViewHolder;->getItemId()J

    move-result-wide v1

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_androidbasewidget_adapter_FragmentStateAdapter__shouldDelayFragmentTransactions',
        'method': '.method shouldDelayFragmentTransactions()Z',
        'method_name': 'shouldDelayFragmentTransactions',
        'method_anchors': ['iget-object p0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mFragmentManager:Landroidx/fragment/app/FragmentManager;', 'invoke-virtual {p0}, Landroidx/fragment/app/FragmentManager;->isStateSaved()Z', 'return p0'],
        'type': 'method_replace',
        'search': """.method shouldDelayFragmentTransactions()Z
    .registers 1

    iget-object p0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mFragmentManager:Landroidx/fragment/app/FragmentManager;

    invoke-virtual {p0}, Landroidx/fragment/app/FragmentManager;->isStateSaved()Z

    move-result p0

    return p0
.end method""",
        'replacement': """.method shouldDelayFragmentTransactions()Z
    .registers 1

    goto :goto_1

    nop

    :goto_0
    invoke-virtual {p0}, Landroidx/fragment/app/FragmentManager;->isStateSaved()Z

    move-result p0

    goto :goto_2

    nop

    :goto_1
    iget-object p0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mFragmentManager:Landroidx/fragment/app/FragmentManager;

    goto :goto_0

    nop

    :goto_2
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
