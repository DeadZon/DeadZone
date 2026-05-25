TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/app/floatingactivity/FloatingActivitySwitcher.smali'
CLASS_FALLBACK_NAMES = ['FloatingActivitySwitcher.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field private static final mActivityInfoStack:Ljava/util/HashMap;']

PATCHES = [
    {
        'id': 'miuix_appcompat_app_floatingactivity_FloatingActivitySwitcher__getActivity',
        'method': '.method getActivity(Ljava/lang/String;I)Lmiuix/appcompat/app/AppCompatActivity;',
        'method_name': 'getActivity',
        'method_anchors': ['iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/FloatingActivitySwitcher;->mActivityCache:Landroid/util/SparseArray;', 'invoke-virtual {p0, p2}, Landroid/util/SparseArray;->get(I)Ljava/lang/Object;', 'check-cast p0, Ljava/util/ArrayList;', 'if-eqz p0, :cond_1', 'invoke-virtual {p0}, Ljava/util/ArrayList;->size()I', 'if-ge v0, p2, :cond_1', 'invoke-virtual {p0, v0}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;', 'check-cast v1, Lmiuix/appcompat/app/AppCompatActivity;'],
        'type': 'method_replace',
        'search': """.method getActivity(Ljava/lang/String;I)Lmiuix/appcompat/app/AppCompatActivity;
    .registers 6

    iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/FloatingActivitySwitcher;->mActivityCache:Landroid/util/SparseArray;

    invoke-virtual {p0, p2}, Landroid/util/SparseArray;->get(I)Ljava/lang/Object;

    move-result-object p0

    check-cast p0, Ljava/util/ArrayList;

    if-eqz p0, :cond_1

    invoke-virtual {p0}, Ljava/util/ArrayList;->size()I

    move-result p2

    const/4 v0, 0x0

    :cond_0
    if-ge v0, p2, :cond_1

    invoke-virtual {p0, v0}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v1

    add-int/lit8 v0, v0, 0x1

    check-cast v1, Lmiuix/appcompat/app/AppCompatActivity;

    invoke-virtual {v1}, Lmiuix/appcompat/app/AppCompatActivity;->getActivityIdentity()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v2, p1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v2

    if-eqz v2, :cond_0

    return-object v1

    :cond_1
    const/4 p0, 0x0

    return-object p0
.end method""",
        'replacement': """.method getActivity(Ljava/lang/String;I)Lmiuix/appcompat/app/AppCompatActivity;
    .registers 6

    goto :goto_e

    nop

    :goto_0
    check-cast v1, Lmiuix/appcompat/app/AppCompatActivity;

    goto :goto_8

    nop

    :goto_1
    invoke-virtual {p0, p2}, Landroid/util/SparseArray;->get(I)Ljava/lang/Object;

    move-result-object p0

    goto :goto_9

    nop

    :goto_2
    if-nez p0, :cond_0

    goto :goto_d

    :cond_0
    goto :goto_7

    nop

    :goto_3
    const/4 v0, 0x0

    :goto_4
    goto :goto_a

    nop

    :goto_5
    add-int/lit8 v0, v0, 0x1

    goto :goto_0

    nop

    :goto_6
    invoke-virtual {p0, v0}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v1

    goto :goto_5

    nop

    :goto_7
    invoke-virtual {p0}, Ljava/util/ArrayList;->size()I

    move-result p2

    goto :goto_3

    nop

    :goto_8
    invoke-virtual {v1}, Lmiuix/appcompat/app/AppCompatActivity;->getActivityIdentity()Ljava/lang/String;

    move-result-object v2

    goto :goto_10

    nop

    :goto_9
    check-cast p0, Ljava/util/ArrayList;

    goto :goto_2

    nop

    :goto_a
    if-lt v0, p2, :cond_1

    goto :goto_d

    :cond_1
    goto :goto_6

    nop

    :goto_b
    return-object p0

    :goto_c
    return-object v1

    :goto_d
    goto :goto_11

    nop

    :goto_e
    iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/FloatingActivitySwitcher;->mActivityCache:Landroid/util/SparseArray;

    goto :goto_1

    nop

    :goto_f
    if-nez v2, :cond_2

    goto :goto_4

    :cond_2
    goto :goto_c

    nop

    :goto_10
    invoke-virtual {v2, p1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v2

    goto :goto_f

    nop

    :goto_11
    const/4 p0, 0x0

    goto :goto_b

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_floatingactivity_FloatingActivitySwitcher__getActivityIndex',
        'method': '.method getActivityIndex(Lmiuix/appcompat/app/AppCompatActivity;)I',
        'method_name': 'getActivityIndex',
        'method_anchors': ['if-eqz p1, :cond_0', 'iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/FloatingActivitySwitcher;->mActivityCache:Landroid/util/SparseArray;', 'invoke-virtual {p1}, Landroid/app/Activity;->getTaskId()I', 'invoke-virtual {p0, v0}, Landroid/util/SparseArray;->get(I)Ljava/lang/Object;', 'check-cast p0, Ljava/util/ArrayList;', 'if-eqz p0, :cond_0', 'invoke-virtual {p0, p1}, Ljava/util/ArrayList;->indexOf(Ljava/lang/Object;)I', 'return p0'],
        'type': 'method_replace',
        'search': """.method getActivityIndex(Lmiuix/appcompat/app/AppCompatActivity;)I
    .registers 3

    if-eqz p1, :cond_0

    iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/FloatingActivitySwitcher;->mActivityCache:Landroid/util/SparseArray;

    invoke-virtual {p1}, Landroid/app/Activity;->getTaskId()I

    move-result v0

    invoke-virtual {p0, v0}, Landroid/util/SparseArray;->get(I)Ljava/lang/Object;

    move-result-object p0

    check-cast p0, Ljava/util/ArrayList;

    if-eqz p0, :cond_0

    invoke-virtual {p0, p1}, Ljava/util/ArrayList;->indexOf(Ljava/lang/Object;)I

    move-result p0

    return p0

    :cond_0
    const/4 p0, -0x1

    return p0
.end method""",
        'replacement': """.method getActivityIndex(Lmiuix/appcompat/app/AppCompatActivity;)I
    .registers 3

    goto :goto_a

    nop

    :goto_0
    check-cast p0, Ljava/util/ArrayList;

    goto :goto_5

    nop

    :goto_1
    return p0

    :goto_2
    goto :goto_6

    nop

    :goto_3
    invoke-virtual {p1}, Landroid/app/Activity;->getTaskId()I

    move-result v0

    goto :goto_8

    nop

    :goto_4
    iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/FloatingActivitySwitcher;->mActivityCache:Landroid/util/SparseArray;

    goto :goto_3

    nop

    :goto_5
    if-nez p0, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_9

    nop

    :goto_6
    const/4 p0, -0x1

    goto :goto_7

    nop

    :goto_7
    return p0

    :goto_8
    invoke-virtual {p0, v0}, Landroid/util/SparseArray;->get(I)Ljava/lang/Object;

    move-result-object p0

    goto :goto_0

    nop

    :goto_9
    invoke-virtual {p0, p1}, Ljava/util/ArrayList;->indexOf(Ljava/lang/Object;)I

    move-result p0

    goto :goto_1

    nop

    :goto_a
    if-nez p1, :cond_1

    goto :goto_2

    :cond_1
    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_floatingactivity_FloatingActivitySwitcher__getActivityList',
        'method': '.method getActivityList(I)Ljava/util/ArrayList;',
        'method_name': 'getActivityList',
        'method_anchors': ['iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/FloatingActivitySwitcher;->mActivityCache:Landroid/util/SparseArray;', 'invoke-virtual {p0, p1}, Landroid/util/SparseArray;->get(I)Ljava/lang/Object;', 'check-cast p0, Ljava/util/ArrayList;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method getActivityList(I)Ljava/util/ArrayList;
    .registers 2

    iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/FloatingActivitySwitcher;->mActivityCache:Landroid/util/SparseArray;

    invoke-virtual {p0, p1}, Landroid/util/SparseArray;->get(I)Ljava/lang/Object;

    move-result-object p0

    check-cast p0, Ljava/util/ArrayList;

    return-object p0
.end method""",
        'replacement': """.method getActivityList(I)Ljava/util/ArrayList;
    .registers 2

    goto :goto_3

    nop

    :goto_0
    invoke-virtual {p0, p1}, Landroid/util/SparseArray;->get(I)Ljava/lang/Object;

    move-result-object p0

    goto :goto_2

    nop

    :goto_1
    return-object p0

    :goto_2
    check-cast p0, Ljava/util/ArrayList;

    goto :goto_1

    nop

    :goto_3
    iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/FloatingActivitySwitcher;->mActivityCache:Landroid/util/SparseArray;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_floatingactivity_FloatingActivitySwitcher__getLastActivityPanel',
        'method': '.method getLastActivityPanel()Landroid/view/View;',
        'method_name': 'getLastActivityPanel',
        'method_anchors': ['iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/FloatingActivitySwitcher;->mLastActivityPanel:Ljava/lang/ref/WeakReference;', 'if-nez p0, :cond_0', 'return-object p0', 'invoke-virtual {p0}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;', 'check-cast p0, Landroid/view/View;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method getLastActivityPanel()Landroid/view/View;
    .registers 1

    iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/FloatingActivitySwitcher;->mLastActivityPanel:Ljava/lang/ref/WeakReference;

    if-nez p0, :cond_0

    const/4 p0, 0x0

    return-object p0

    :cond_0
    invoke-virtual {p0}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;

    move-result-object p0

    check-cast p0, Landroid/view/View;

    return-object p0
.end method""",
        'replacement': """.method getLastActivityPanel()Landroid/view/View;
    .registers 1

    goto :goto_5

    nop

    :goto_0
    return-object p0

    :goto_1
    goto :goto_7

    nop

    :goto_2
    if-eqz p0, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_3

    nop

    :goto_3
    const/4 p0, 0x0

    goto :goto_0

    nop

    :goto_4
    return-object p0

    :goto_5
    iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/FloatingActivitySwitcher;->mLastActivityPanel:Ljava/lang/ref/WeakReference;

    goto :goto_2

    nop

    :goto_6
    check-cast p0, Landroid/view/View;

    goto :goto_4

    nop

    :goto_7
    invoke-virtual {p0}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;

    move-result-object p0

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_floatingactivity_FloatingActivitySwitcher__getPreviousActivity',
        'method': '.method getPreviousActivity(Lmiuix/appcompat/app/AppCompatActivity;)Lmiuix/appcompat/app/AppCompatActivity;',
        'method_name': 'getPreviousActivity',
        'method_anchors': ['if-eqz p1, :cond_2', 'iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/FloatingActivitySwitcher;->mActivityCache:Landroid/util/SparseArray;', 'invoke-virtual {p1}, Landroid/app/Activity;->getTaskId()I', 'invoke-virtual {p0, v0}, Landroid/util/SparseArray;->get(I)Ljava/lang/Object;', 'check-cast p0, Ljava/util/ArrayList;', 'if-eqz p0, :cond_0', 'invoke-virtual {p0, p1}, Ljava/util/ArrayList;->indexOf(Ljava/lang/Object;)I', 'if-lez p1, :cond_2'],
        'type': 'method_replace',
        'search': """.method getPreviousActivity(Lmiuix/appcompat/app/AppCompatActivity;)Lmiuix/appcompat/app/AppCompatActivity;
    .registers 5

    if-eqz p1, :cond_2

    iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/FloatingActivitySwitcher;->mActivityCache:Landroid/util/SparseArray;

    invoke-virtual {p1}, Landroid/app/Activity;->getTaskId()I

    move-result v0

    invoke-virtual {p0, v0}, Landroid/util/SparseArray;->get(I)Ljava/lang/Object;

    move-result-object p0

    check-cast p0, Ljava/util/ArrayList;

    if-eqz p0, :cond_0

    invoke-virtual {p0, p1}, Ljava/util/ArrayList;->indexOf(Ljava/lang/Object;)I

    move-result p1

    goto :goto_0

    :cond_0
    const/4 p1, -0x1

    :goto_0
    if-lez p1, :cond_2

    add-int/lit8 p1, p1, -0x1

    move v0, p1

    :goto_1
    if-ltz v0, :cond_2

    invoke-virtual {p0, p1}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lmiuix/appcompat/app/AppCompatActivity;

    invoke-virtual {v1}, Lmiuix/appcompat/app/AppCompatActivity;->isFinishing()Z

    move-result v2

    if-nez v2, :cond_1

    return-object v1

    :cond_1
    add-int/lit8 v0, v0, -0x1

    goto :goto_1

    :cond_2
    const/4 p0, 0x0

    return-object p0
.end method""",
        'replacement': """.method getPreviousActivity(Lmiuix/appcompat/app/AppCompatActivity;)Lmiuix/appcompat/app/AppCompatActivity;
    .registers 5

    goto :goto_12

    nop

    :goto_0
    if-gez v0, :cond_0

    goto :goto_e

    :cond_0
    goto :goto_4

    nop

    :goto_1
    const/4 p0, 0x0

    goto :goto_f

    nop

    :goto_2
    move v0, p1

    :goto_3
    goto :goto_0

    nop

    :goto_4
    invoke-virtual {p0, p1}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v1

    goto :goto_b

    nop

    :goto_5
    iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/FloatingActivitySwitcher;->mActivityCache:Landroid/util/SparseArray;

    goto :goto_11

    nop

    :goto_6
    goto :goto_19

    :goto_7
    goto :goto_18

    nop

    :goto_8
    if-eqz v2, :cond_1

    goto :goto_17

    :cond_1
    goto :goto_16

    nop

    :goto_9
    invoke-virtual {v1}, Lmiuix/appcompat/app/AppCompatActivity;->isFinishing()Z

    move-result v2

    goto :goto_8

    nop

    :goto_a
    invoke-virtual {p0, v0}, Landroid/util/SparseArray;->get(I)Ljava/lang/Object;

    move-result-object p0

    goto :goto_10

    nop

    :goto_b
    check-cast v1, Lmiuix/appcompat/app/AppCompatActivity;

    goto :goto_9

    nop

    :goto_c
    add-int/lit8 p1, p1, -0x1

    goto :goto_2

    nop

    :goto_d
    goto :goto_3

    :goto_e
    goto :goto_1

    nop

    :goto_f
    return-object p0

    :goto_10
    check-cast p0, Ljava/util/ArrayList;

    goto :goto_13

    nop

    :goto_11
    invoke-virtual {p1}, Landroid/app/Activity;->getTaskId()I

    move-result v0

    goto :goto_a

    nop

    :goto_12
    if-nez p1, :cond_2

    goto :goto_e

    :cond_2
    goto :goto_5

    nop

    :goto_13
    if-nez p0, :cond_3

    goto :goto_7

    :cond_3
    goto :goto_14

    nop

    :goto_14
    invoke-virtual {p0, p1}, Ljava/util/ArrayList;->indexOf(Ljava/lang/Object;)I

    move-result p1

    goto :goto_6

    nop

    :goto_15
    add-int/lit8 v0, v0, -0x1

    goto :goto_d

    nop

    :goto_16
    return-object v1

    :goto_17
    goto :goto_15

    nop

    :goto_18
    const/4 p1, -0x1

    :goto_19
    goto :goto_1a

    nop

    :goto_1a
    if-gtz p1, :cond_4

    goto :goto_e

    :cond_4
    goto :goto_c

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_floatingactivity_FloatingActivitySwitcher__setLastActivityPanel',
        'method': '.method setLastActivityPanel(Landroid/view/View;)V',
        'method_name': 'setLastActivityPanel',
        'method_anchors': ['new-instance v0, Ljava/lang/ref/WeakReference;', 'invoke-direct {v0, p1}, Ljava/lang/ref/WeakReference;-><init>(Ljava/lang/Object;)V', 'iput-object v0, p0, Lmiuix/appcompat/app/floatingactivity/FloatingActivitySwitcher;->mLastActivityPanel:Ljava/lang/ref/WeakReference;', 'return-void'],
        'type': 'method_replace',
        'search': """.method setLastActivityPanel(Landroid/view/View;)V
    .registers 3

    new-instance v0, Ljava/lang/ref/WeakReference;

    invoke-direct {v0, p1}, Ljava/lang/ref/WeakReference;-><init>(Ljava/lang/Object;)V

    iput-object v0, p0, Lmiuix/appcompat/app/floatingactivity/FloatingActivitySwitcher;->mLastActivityPanel:Ljava/lang/ref/WeakReference;

    return-void
.end method""",
        'replacement': """.method setLastActivityPanel(Landroid/view/View;)V
    .registers 3

    goto :goto_0

    nop

    :goto_0
    new-instance v0, Ljava/lang/ref/WeakReference;

    goto :goto_2

    nop

    :goto_1
    iput-object v0, p0, Lmiuix/appcompat/app/floatingactivity/FloatingActivitySwitcher;->mLastActivityPanel:Ljava/lang/ref/WeakReference;

    goto :goto_3

    nop

    :goto_2
    invoke-direct {v0, p1}, Ljava/lang/ref/WeakReference;-><init>(Ljava/lang/Object;)V

    goto :goto_1

    nop

    :goto_3
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
