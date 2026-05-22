TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer.smali'
CLASS_FALLBACK_NAMES = ['FragmentStateAdapter$FragmentMaxLifecycleEnforcer.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'miuix_androidbasewidget_adapter_FragmentStateAdapter__FragmentMaxLifecycleEnforcer__register',
        'method': '.method register(Landroidx/recyclerview/widget/RecyclerView;)V',
        'method_name': 'register',
        'method_anchors': ['invoke-direct {p0, p1}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->inferViewPager(Landroidx/recyclerview/widget/RecyclerView;)Landroidx/viewpager2/widget/OriginalViewPager2;', 'iput-object p1, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mViewPager:Landroidx/viewpager2/widget/OriginalViewPager2;', 'new-instance p1, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer$1;', 'invoke-direct {p1, p0}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer$1;-><init>(Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;)V', 'iput-object p1, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mPageChangeCallback:Landroidx/viewpager2/widget/OriginalViewPager2$OnPageChangeCallback;', 'iget-object v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mViewPager:Landroidx/viewpager2/widget/OriginalViewPager2;', 'invoke-virtual {v0, p1}, Landroidx/viewpager2/widget/OriginalViewPager2;->registerOnPageChangeCallback(Landroidx/viewpager2/widget/OriginalViewPager2$OnPageChangeCallback;)V', 'new-instance p1, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer$2;'],
        'type': 'method_replace',
        'search': """.method register(Landroidx/recyclerview/widget/RecyclerView;)V
    .registers 3

    invoke-direct {p0, p1}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->inferViewPager(Landroidx/recyclerview/widget/RecyclerView;)Landroidx/viewpager2/widget/OriginalViewPager2;

    move-result-object p1

    iput-object p1, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mViewPager:Landroidx/viewpager2/widget/OriginalViewPager2;

    new-instance p1, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer$1;

    invoke-direct {p1, p0}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer$1;-><init>(Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;)V

    iput-object p1, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mPageChangeCallback:Landroidx/viewpager2/widget/OriginalViewPager2$OnPageChangeCallback;

    iget-object v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mViewPager:Landroidx/viewpager2/widget/OriginalViewPager2;

    invoke-virtual {v0, p1}, Landroidx/viewpager2/widget/OriginalViewPager2;->registerOnPageChangeCallback(Landroidx/viewpager2/widget/OriginalViewPager2$OnPageChangeCallback;)V

    new-instance p1, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer$2;

    invoke-direct {p1, p0}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer$2;-><init>(Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;)V

    iput-object p1, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mDataObserver:Landroidx/recyclerview/widget/RecyclerView$AdapterDataObserver;

    iget-object v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->this$0:Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;

    invoke-virtual {v0, p1}, Landroidx/recyclerview/widget/RecyclerView$Adapter;->registerAdapterDataObserver(Landroidx/recyclerview/widget/RecyclerView$AdapterDataObserver;)V

    new-instance p1, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer$3;

    invoke-direct {p1, p0}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer$3;-><init>(Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;)V

    iput-object p1, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mLifecycleObserver:Landroidx/lifecycle/LifecycleEventObserver;

    iget-object p0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->this$0:Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;

    iget-object p0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mLifecycle:Landroidx/lifecycle/Lifecycle;

    invoke-virtual {p0, p1}, Landroidx/lifecycle/Lifecycle;->addObserver(Landroidx/lifecycle/LifecycleObserver;)V

    return-void
.end method""",
        'replacement': """.method register(Landroidx/recyclerview/widget/RecyclerView;)V
    .registers 3

    goto :goto_2

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mLifecycle:Landroidx/lifecycle/Lifecycle;

    goto :goto_11

    nop

    :goto_1
    new-instance p1, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer$2;

    goto :goto_7

    nop

    :goto_2
    invoke-direct {p0, p1}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->inferViewPager(Landroidx/recyclerview/widget/RecyclerView;)Landroidx/viewpager2/widget/OriginalViewPager2;

    move-result-object p1

    goto :goto_5

    nop

    :goto_3
    invoke-direct {p1, p0}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer$3;-><init>(Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;)V

    goto :goto_d

    nop

    :goto_4
    new-instance p1, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer$3;

    goto :goto_3

    nop

    :goto_5
    iput-object p1, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mViewPager:Landroidx/viewpager2/widget/OriginalViewPager2;

    goto :goto_f

    nop

    :goto_6
    iput-object p1, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mDataObserver:Landroidx/recyclerview/widget/RecyclerView$AdapterDataObserver;

    goto :goto_c

    nop

    :goto_7
    invoke-direct {p1, p0}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer$2;-><init>(Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;)V

    goto :goto_6

    nop

    :goto_8
    iget-object v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mViewPager:Landroidx/viewpager2/widget/OriginalViewPager2;

    goto :goto_e

    nop

    :goto_9
    iget-object p0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->this$0:Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;

    goto :goto_0

    nop

    :goto_a
    iput-object p1, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mPageChangeCallback:Landroidx/viewpager2/widget/OriginalViewPager2$OnPageChangeCallback;

    goto :goto_8

    nop

    :goto_b
    return-void

    :goto_c
    iget-object v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->this$0:Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;

    goto :goto_10

    nop

    :goto_d
    iput-object p1, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mLifecycleObserver:Landroidx/lifecycle/LifecycleEventObserver;

    goto :goto_9

    nop

    :goto_e
    invoke-virtual {v0, p1}, Landroidx/viewpager2/widget/OriginalViewPager2;->registerOnPageChangeCallback(Landroidx/viewpager2/widget/OriginalViewPager2$OnPageChangeCallback;)V

    goto :goto_1

    nop

    :goto_f
    new-instance p1, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer$1;

    goto :goto_12

    nop

    :goto_10
    invoke-virtual {v0, p1}, Landroidx/recyclerview/widget/RecyclerView$Adapter;->registerAdapterDataObserver(Landroidx/recyclerview/widget/RecyclerView$AdapterDataObserver;)V

    goto :goto_4

    nop

    :goto_11
    invoke-virtual {p0, p1}, Landroidx/lifecycle/Lifecycle;->addObserver(Landroidx/lifecycle/LifecycleObserver;)V

    goto :goto_b

    nop

    :goto_12
    invoke-direct {p1, p0}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer$1;-><init>(Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;)V

    goto :goto_a

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_androidbasewidget_adapter_FragmentStateAdapter__FragmentMaxLifecycleEnforcer__unregister',
        'method': '.method unregister(Landroidx/recyclerview/widget/RecyclerView;)V',
        'method_name': 'unregister',
        'method_anchors': ['invoke-direct {p0, p1}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->inferViewPager(Landroidx/recyclerview/widget/RecyclerView;)Landroidx/viewpager2/widget/OriginalViewPager2;', 'iget-object v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mPageChangeCallback:Landroidx/viewpager2/widget/OriginalViewPager2$OnPageChangeCallback;', 'invoke-virtual {p1, v0}, Landroidx/viewpager2/widget/OriginalViewPager2;->unregisterOnPageChangeCallback(Landroidx/viewpager2/widget/OriginalViewPager2$OnPageChangeCallback;)V', 'iget-object p1, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->this$0:Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;', 'iget-object v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mDataObserver:Landroidx/recyclerview/widget/RecyclerView$AdapterDataObserver;', 'invoke-virtual {p1, v0}, Landroidx/recyclerview/widget/RecyclerView$Adapter;->unregisterAdapterDataObserver(Landroidx/recyclerview/widget/RecyclerView$AdapterDataObserver;)V', 'iget-object p1, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->this$0:Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;', 'iget-object p1, p1, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mLifecycle:Landroidx/lifecycle/Lifecycle;'],
        'type': 'method_replace',
        'search': """.method unregister(Landroidx/recyclerview/widget/RecyclerView;)V
    .registers 3

    invoke-direct {p0, p1}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->inferViewPager(Landroidx/recyclerview/widget/RecyclerView;)Landroidx/viewpager2/widget/OriginalViewPager2;

    move-result-object p1

    iget-object v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mPageChangeCallback:Landroidx/viewpager2/widget/OriginalViewPager2$OnPageChangeCallback;

    invoke-virtual {p1, v0}, Landroidx/viewpager2/widget/OriginalViewPager2;->unregisterOnPageChangeCallback(Landroidx/viewpager2/widget/OriginalViewPager2$OnPageChangeCallback;)V

    iget-object p1, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->this$0:Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;

    iget-object v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mDataObserver:Landroidx/recyclerview/widget/RecyclerView$AdapterDataObserver;

    invoke-virtual {p1, v0}, Landroidx/recyclerview/widget/RecyclerView$Adapter;->unregisterAdapterDataObserver(Landroidx/recyclerview/widget/RecyclerView$AdapterDataObserver;)V

    iget-object p1, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->this$0:Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;

    iget-object p1, p1, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mLifecycle:Landroidx/lifecycle/Lifecycle;

    iget-object v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mLifecycleObserver:Landroidx/lifecycle/LifecycleEventObserver;

    invoke-virtual {p1, v0}, Landroidx/lifecycle/Lifecycle;->removeObserver(Landroidx/lifecycle/LifecycleObserver;)V

    const/4 p1, 0x0

    iput-object p1, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mViewPager:Landroidx/viewpager2/widget/OriginalViewPager2;

    return-void
.end method""",
        'replacement': """.method unregister(Landroidx/recyclerview/widget/RecyclerView;)V
    .registers 3

    goto :goto_b

    nop

    :goto_0
    iget-object v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mDataObserver:Landroidx/recyclerview/widget/RecyclerView$AdapterDataObserver;

    goto :goto_a

    nop

    :goto_1
    iget-object p1, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->this$0:Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;

    goto :goto_7

    nop

    :goto_2
    iget-object p1, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->this$0:Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;

    goto :goto_0

    nop

    :goto_3
    invoke-virtual {p1, v0}, Landroidx/lifecycle/Lifecycle;->removeObserver(Landroidx/lifecycle/LifecycleObserver;)V

    goto :goto_4

    nop

    :goto_4
    const/4 p1, 0x0

    goto :goto_5

    nop

    :goto_5
    iput-object p1, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mViewPager:Landroidx/viewpager2/widget/OriginalViewPager2;

    goto :goto_c

    nop

    :goto_6
    iget-object v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mPageChangeCallback:Landroidx/viewpager2/widget/OriginalViewPager2$OnPageChangeCallback;

    goto :goto_9

    nop

    :goto_7
    iget-object p1, p1, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mLifecycle:Landroidx/lifecycle/Lifecycle;

    goto :goto_8

    nop

    :goto_8
    iget-object v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mLifecycleObserver:Landroidx/lifecycle/LifecycleEventObserver;

    goto :goto_3

    nop

    :goto_9
    invoke-virtual {p1, v0}, Landroidx/viewpager2/widget/OriginalViewPager2;->unregisterOnPageChangeCallback(Landroidx/viewpager2/widget/OriginalViewPager2$OnPageChangeCallback;)V

    goto :goto_2

    nop

    :goto_a
    invoke-virtual {p1, v0}, Landroidx/recyclerview/widget/RecyclerView$Adapter;->unregisterAdapterDataObserver(Landroidx/recyclerview/widget/RecyclerView$AdapterDataObserver;)V

    goto :goto_1

    nop

    :goto_b
    invoke-direct {p0, p1}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->inferViewPager(Landroidx/recyclerview/widget/RecyclerView;)Landroidx/viewpager2/widget/OriginalViewPager2;

    move-result-object p1

    goto :goto_6

    nop

    :goto_c
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_androidbasewidget_adapter_FragmentStateAdapter__FragmentMaxLifecycleEnforcer__updateFragmentMaxLifecycle',
        'method': '.method updateFragmentMaxLifecycle(Z)V',
        'method_name': 'updateFragmentMaxLifecycle',
        'method_anchors': ['iget-object v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->this$0:Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;', 'invoke-virtual {v0}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->shouldDelayFragmentTransactions()Z', 'if-eqz v0, :cond_0', 'iget-object v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mViewPager:Landroidx/viewpager2/widget/OriginalViewPager2;', 'invoke-virtual {v0}, Landroidx/viewpager2/widget/OriginalViewPager2;->getScrollState()I', 'if-eqz v0, :cond_1', 'iget-object v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->this$0:Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;', 'iget-object v0, v0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mFragments:Landroidx/collection/LongSparseArray;'],
        'type': 'method_replace',
        'search': """.method updateFragmentMaxLifecycle(Z)V
    .registers 10

    iget-object v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->this$0:Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;

    invoke-virtual {v0}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->shouldDelayFragmentTransactions()Z

    move-result v0

    if-eqz v0, :cond_0

    goto :goto_4

    :cond_0
    iget-object v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mViewPager:Landroidx/viewpager2/widget/OriginalViewPager2;

    invoke-virtual {v0}, Landroidx/viewpager2/widget/OriginalViewPager2;->getScrollState()I

    move-result v0

    if-eqz v0, :cond_1

    goto :goto_4

    :cond_1
    iget-object v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->this$0:Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;

    iget-object v0, v0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mFragments:Landroidx/collection/LongSparseArray;

    invoke-virtual {v0}, Landroidx/collection/LongSparseArray;->isEmpty()Z

    move-result v0

    if-nez v0, :cond_b

    iget-object v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->this$0:Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;

    invoke-virtual {v0}, Landroidx/recyclerview/widget/RecyclerView$Adapter;->getItemCount()I

    move-result v0

    if-nez v0, :cond_2

    goto :goto_4

    :cond_2
    iget-object v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mViewPager:Landroidx/viewpager2/widget/OriginalViewPager2;

    invoke-virtual {v0}, Landroidx/viewpager2/widget/OriginalViewPager2;->getCurrentItem()I

    move-result v0

    iget-object v1, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->this$0:Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;

    invoke-virtual {v1}, Landroidx/recyclerview/widget/RecyclerView$Adapter;->getItemCount()I

    move-result v1

    if-lt v0, v1, :cond_3

    goto :goto_4

    :cond_3
    iget-object v1, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->this$0:Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;

    invoke-virtual {v1, v0}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->getItemId(I)J

    move-result-wide v0

    iget-wide v2, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mPrimaryItemId:J

    cmp-long v2, v0, v2

    if-nez v2, :cond_4

    if-nez p1, :cond_4

    goto :goto_4

    :cond_4
    iget-object p1, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->this$0:Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;

    iget-object p1, p1, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mFragments:Landroidx/collection/LongSparseArray;

    invoke-virtual {p1, v0, v1}, Landroidx/collection/LongSparseArray;->get(J)Ljava/lang/Object;

    move-result-object p1

    check-cast p1, Landroidx/fragment/app/Fragment;

    if-eqz p1, :cond_b

    invoke-virtual {p1}, Landroidx/fragment/app/Fragment;->isAdded()Z

    move-result p1

    if-nez p1, :cond_5

    goto :goto_4

    :cond_5
    iput-wide v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mPrimaryItemId:J

    iget-object p1, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->this$0:Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;

    iget-object p1, p1, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mFragmentManager:Landroidx/fragment/app/FragmentManager;

    invoke-virtual {p1}, Landroidx/fragment/app/FragmentManager;->beginTransaction()Landroidx/fragment/app/FragmentTransaction;

    move-result-object p1

    const/4 v0, 0x0

    const/4 v1, 0x0

    move v2, v0

    :goto_0
    iget-object v3, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->this$0:Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;

    iget-object v3, v3, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mFragments:Landroidx/collection/LongSparseArray;

    invoke-virtual {v3}, Landroidx/collection/LongSparseArray;->size()I

    move-result v3

    if-ge v2, v3, :cond_9

    iget-object v3, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->this$0:Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;

    iget-object v3, v3, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mFragments:Landroidx/collection/LongSparseArray;

    invoke-virtual {v3, v2}, Landroidx/collection/LongSparseArray;->keyAt(I)J

    move-result-wide v3

    iget-object v5, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->this$0:Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;

    iget-object v5, v5, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mFragments:Landroidx/collection/LongSparseArray;

    invoke-virtual {v5, v2}, Landroidx/collection/LongSparseArray;->valueAt(I)Ljava/lang/Object;

    move-result-object v5

    check-cast v5, Landroidx/fragment/app/Fragment;

    invoke-virtual {v5}, Landroidx/fragment/app/Fragment;->isAdded()Z

    move-result v6

    if-nez v6, :cond_6

    goto :goto_3

    :cond_6
    iget-wide v6, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mPrimaryItemId:J

    cmp-long v6, v3, v6

    if-eqz v6, :cond_7

    sget-object v6, Landroidx/lifecycle/Lifecycle$State;->STARTED:Landroidx/lifecycle/Lifecycle$State;

    invoke-virtual {p1, v5, v6}, Landroidx/fragment/app/FragmentTransaction;->setMaxLifecycle(Landroidx/fragment/app/Fragment;Landroidx/lifecycle/Lifecycle$State;)Landroidx/fragment/app/FragmentTransaction;

    goto :goto_1

    :cond_7
    move-object v1, v5

    :goto_1
    iget-wide v6, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mPrimaryItemId:J

    cmp-long v3, v3, v6

    if-nez v3, :cond_8

    const/4 v3, 0x1

    goto :goto_2

    :cond_8
    move v3, v0

    :goto_2
    invoke-virtual {v5, v3}, Landroidx/fragment/app/Fragment;->setMenuVisibility(Z)V

    :goto_3
    add-int/lit8 v2, v2, 0x1

    goto :goto_0

    :cond_9
    if-eqz v1, :cond_a

    sget-object p0, Landroidx/lifecycle/Lifecycle$State;->RESUMED:Landroidx/lifecycle/Lifecycle$State;

    invoke-virtual {p1, v1, p0}, Landroidx/fragment/app/FragmentTransaction;->setMaxLifecycle(Landroidx/fragment/app/Fragment;Landroidx/lifecycle/Lifecycle$State;)Landroidx/fragment/app/FragmentTransaction;

    :cond_a
    invoke-virtual {p1}, Landroidx/fragment/app/FragmentTransaction;->isEmpty()Z

    move-result p0

    if-nez p0, :cond_b

    invoke-virtual {p1}, Landroidx/fragment/app/FragmentTransaction;->commitNow()V

    :cond_b
    :goto_4
    return-void
.end method""",
        'replacement': """.method updateFragmentMaxLifecycle(Z)V
    .registers 10

    goto :goto_36

    nop

    :goto_0
    if-eqz p1, :cond_0

    goto :goto_5b

    :cond_0
    goto :goto_5a

    nop

    :goto_1
    goto :goto_48

    :goto_2
    goto :goto_35

    nop

    :goto_3
    iget-object v5, v5, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mFragments:Landroidx/collection/LongSparseArray;

    goto :goto_13

    nop

    :goto_4
    goto :goto_1c

    :goto_5
    goto :goto_7

    nop

    :goto_6
    if-eqz v0, :cond_1

    goto :goto_1c

    :cond_1
    goto :goto_18

    nop

    :goto_7
    iget-object v1, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->this$0:Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;

    goto :goto_31

    nop

    :goto_8
    const/4 v3, 0x1

    goto :goto_33

    nop

    :goto_9
    move-object v1, v5

    :goto_a
    goto :goto_30

    nop

    :goto_b
    check-cast v5, Landroidx/fragment/app/Fragment;

    goto :goto_3f

    nop

    :goto_c
    invoke-virtual {p1}, Landroidx/fragment/app/FragmentManager;->beginTransaction()Landroidx/fragment/app/FragmentTransaction;

    move-result-object p1

    goto :goto_32

    nop

    :goto_d
    check-cast p1, Landroidx/fragment/app/Fragment;

    goto :goto_14

    nop

    :goto_e
    invoke-virtual {p1}, Landroidx/fragment/app/Fragment;->isAdded()Z

    move-result p1

    goto :goto_0

    nop

    :goto_f
    sget-object p0, Landroidx/lifecycle/Lifecycle$State;->RESUMED:Landroidx/lifecycle/Lifecycle$State;

    goto :goto_49

    nop

    :goto_10
    invoke-virtual {v0}, Landroidx/recyclerview/widget/RecyclerView$Adapter;->getItemCount()I

    move-result v0

    goto :goto_43

    nop

    :goto_11
    goto :goto_1c

    :goto_12
    goto :goto_1f

    nop

    :goto_13
    invoke-virtual {v5, v2}, Landroidx/collection/LongSparseArray;->valueAt(I)Ljava/lang/Object;

    move-result-object v5

    goto :goto_b

    nop

    :goto_14
    if-nez p1, :cond_2

    goto :goto_1c

    :cond_2
    goto :goto_e

    nop

    :goto_15
    if-eqz v6, :cond_3

    goto :goto_2

    :cond_3
    goto :goto_1

    nop

    :goto_16
    invoke-virtual {v0}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->shouldDelayFragmentTransactions()Z

    move-result v0

    goto :goto_57

    nop

    :goto_17
    iput-wide v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mPrimaryItemId:J

    goto :goto_45

    nop

    :goto_18
    iget-object v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->this$0:Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;

    goto :goto_10

    nop

    :goto_19
    iget-object v3, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->this$0:Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;

    goto :goto_28

    nop

    :goto_1a
    iget-object v3, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->this$0:Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;

    goto :goto_2a

    nop

    :goto_1b
    invoke-virtual {p1}, Landroidx/fragment/app/FragmentTransaction;->commitNow()V

    :goto_1c
    goto :goto_38

    nop

    :goto_1d
    if-eqz v3, :cond_4

    goto :goto_34

    :cond_4
    goto :goto_8

    nop

    :goto_1e
    invoke-virtual {p1, v5, v6}, Landroidx/fragment/app/FragmentTransaction;->setMaxLifecycle(Landroidx/fragment/app/Fragment;Landroidx/lifecycle/Lifecycle$State;)Landroidx/fragment/app/FragmentTransaction;

    goto :goto_4c

    nop

    :goto_1f
    iget-object p1, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->this$0:Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;

    goto :goto_26

    nop

    :goto_20
    goto :goto_1c

    :goto_21
    goto :goto_5d

    nop

    :goto_22
    invoke-virtual {v3}, Landroidx/collection/LongSparseArray;->size()I

    move-result v3

    goto :goto_3a

    nop

    :goto_23
    iget-object p1, p1, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mFragmentManager:Landroidx/fragment/app/FragmentManager;

    goto :goto_c

    nop

    :goto_24
    cmp-long v2, v0, v2

    goto :goto_59

    nop

    :goto_25
    if-nez v6, :cond_5

    goto :goto_4d

    :cond_5
    goto :goto_2f

    nop

    :goto_26
    iget-object p1, p1, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mFragments:Landroidx/collection/LongSparseArray;

    goto :goto_56

    nop

    :goto_27
    cmp-long v3, v3, v6

    goto :goto_1d

    nop

    :goto_28
    iget-object v3, v3, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mFragments:Landroidx/collection/LongSparseArray;

    goto :goto_29

    nop

    :goto_29
    invoke-virtual {v3, v2}, Landroidx/collection/LongSparseArray;->keyAt(I)J

    move-result-wide v3

    goto :goto_4b

    nop

    :goto_2a
    iget-object v3, v3, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mFragments:Landroidx/collection/LongSparseArray;

    goto :goto_22

    nop

    :goto_2b
    add-int/lit8 v2, v2, 0x1

    goto :goto_40

    nop

    :goto_2c
    iget-wide v2, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mPrimaryItemId:J

    goto :goto_24

    nop

    :goto_2d
    if-nez v1, :cond_6

    goto :goto_4a

    :cond_6
    goto :goto_f

    nop

    :goto_2e
    iget-object v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mViewPager:Landroidx/viewpager2/widget/OriginalViewPager2;

    goto :goto_37

    nop

    :goto_2f
    sget-object v6, Landroidx/lifecycle/Lifecycle$State;->STARTED:Landroidx/lifecycle/Lifecycle$State;

    goto :goto_1e

    nop

    :goto_30
    iget-wide v6, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mPrimaryItemId:J

    goto :goto_27

    nop

    :goto_31
    invoke-virtual {v1, v0}, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->getItemId(I)J

    move-result-wide v0

    goto :goto_2c

    nop

    :goto_32
    const/4 v0, 0x0

    goto :goto_42

    nop

    :goto_33
    goto :goto_60

    :goto_34
    goto :goto_5f

    nop

    :goto_35
    iget-wide v6, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mPrimaryItemId:J

    goto :goto_54

    nop

    :goto_36
    iget-object v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->this$0:Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;

    goto :goto_16

    nop

    :goto_37
    invoke-virtual {v0}, Landroidx/viewpager2/widget/OriginalViewPager2;->getScrollState()I

    move-result v0

    goto :goto_39

    nop

    :goto_38
    return-void

    :goto_39
    if-nez v0, :cond_7

    goto :goto_21

    :cond_7
    goto :goto_20

    nop

    :goto_3a
    if-lt v2, v3, :cond_8

    goto :goto_41

    :cond_8
    goto :goto_19

    nop

    :goto_3b
    move v2, v0

    :goto_3c
    goto :goto_1a

    nop

    :goto_3d
    goto :goto_1c

    :goto_3e
    goto :goto_4f

    nop

    :goto_3f
    invoke-virtual {v5}, Landroidx/fragment/app/Fragment;->isAdded()Z

    move-result v6

    goto :goto_15

    nop

    :goto_40
    goto :goto_3c

    :goto_41
    goto :goto_2d

    nop

    :goto_42
    const/4 v1, 0x0

    goto :goto_3b

    nop

    :goto_43
    if-eqz v0, :cond_9

    goto :goto_3e

    :cond_9
    goto :goto_3d

    nop

    :goto_44
    invoke-virtual {v0}, Landroidx/collection/LongSparseArray;->isEmpty()Z

    move-result v0

    goto :goto_6

    nop

    :goto_45
    iget-object p1, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->this$0:Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;

    goto :goto_23

    nop

    :goto_46
    iget-object v0, v0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;->mFragments:Landroidx/collection/LongSparseArray;

    goto :goto_44

    nop

    :goto_47
    invoke-virtual {v5, v3}, Landroidx/fragment/app/Fragment;->setMenuVisibility(Z)V

    :goto_48
    goto :goto_2b

    nop

    :goto_49
    invoke-virtual {p1, v1, p0}, Landroidx/fragment/app/FragmentTransaction;->setMaxLifecycle(Landroidx/fragment/app/Fragment;Landroidx/lifecycle/Lifecycle$State;)Landroidx/fragment/app/FragmentTransaction;

    :goto_4a
    goto :goto_4e

    nop

    :goto_4b
    iget-object v5, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->this$0:Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;

    goto :goto_3

    nop

    :goto_4c
    goto :goto_a

    :goto_4d
    goto :goto_9

    nop

    :goto_4e
    invoke-virtual {p1}, Landroidx/fragment/app/FragmentTransaction;->isEmpty()Z

    move-result p0

    goto :goto_55

    nop

    :goto_4f
    iget-object v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->mViewPager:Landroidx/viewpager2/widget/OriginalViewPager2;

    goto :goto_50

    nop

    :goto_50
    invoke-virtual {v0}, Landroidx/viewpager2/widget/OriginalViewPager2;->getCurrentItem()I

    move-result v0

    goto :goto_5c

    nop

    :goto_51
    goto :goto_1c

    :goto_52
    goto :goto_2e

    nop

    :goto_53
    if-eqz p1, :cond_a

    goto :goto_12

    :cond_a
    goto :goto_11

    nop

    :goto_54
    cmp-long v6, v3, v6

    goto :goto_25

    nop

    :goto_55
    if-eqz p0, :cond_b

    goto :goto_1c

    :cond_b
    goto :goto_1b

    nop

    :goto_56
    invoke-virtual {p1, v0, v1}, Landroidx/collection/LongSparseArray;->get(J)Ljava/lang/Object;

    move-result-object p1

    goto :goto_d

    nop

    :goto_57
    if-nez v0, :cond_c

    goto :goto_52

    :cond_c
    goto :goto_51

    nop

    :goto_58
    invoke-virtual {v1}, Landroidx/recyclerview/widget/RecyclerView$Adapter;->getItemCount()I

    move-result v1

    goto :goto_5e

    nop

    :goto_59
    if-eqz v2, :cond_d

    goto :goto_12

    :cond_d
    goto :goto_53

    nop

    :goto_5a
    goto :goto_1c

    :goto_5b
    goto :goto_17

    nop

    :goto_5c
    iget-object v1, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->this$0:Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;

    goto :goto_58

    nop

    :goto_5d
    iget-object v0, p0, Lmiuix/androidbasewidget/adapter/FragmentStateAdapter$FragmentMaxLifecycleEnforcer;->this$0:Lmiuix/androidbasewidget/adapter/FragmentStateAdapter;

    goto :goto_46

    nop

    :goto_5e
    if-ge v0, v1, :cond_e

    goto :goto_5

    :cond_e
    goto :goto_4

    nop

    :goto_5f
    move v3, v0

    :goto_60
    goto :goto_47

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
