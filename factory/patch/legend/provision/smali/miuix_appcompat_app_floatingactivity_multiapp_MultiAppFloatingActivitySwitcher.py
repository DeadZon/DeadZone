TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher.smali'
CLASS_FALLBACK_NAMES = ['MultiAppFloatingActivitySwitcher.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'miuix_appcompat_app_floatingactivity_multiapp_MultiAppFloatingActivitySwitcher__checkBg',
        'method': '.method checkBg(ILjava/lang/String;)V',
        'method_name': 'checkBg',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->mActivityCache:Landroid/util/SparseArray;', 'invoke-virtual {v0, p1}, Landroid/util/SparseArray;->get(I)Ljava/lang/Object;', 'check-cast v0, Ljava/util/ArrayList;', 'if-eqz v0, :cond_0', 'invoke-virtual {v0}, Ljava/util/ArrayList;->size()I', 'if-gt v0, v1, :cond_1', 'invoke-virtual {p0, p1}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getServicePageCount(I)I', 'if-le v0, v1, :cond_2'],
        'type': 'method_replace',
        'search': """.method checkBg(ILjava/lang/String;)V
    .registers 5

    iget-object v0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->mActivityCache:Landroid/util/SparseArray;

    invoke-virtual {v0, p1}, Landroid/util/SparseArray;->get(I)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Ljava/util/ArrayList;

    const/4 v1, 0x1

    if-eqz v0, :cond_0

    invoke-virtual {v0}, Ljava/util/ArrayList;->size()I

    move-result v0

    if-gt v0, v1, :cond_1

    :cond_0
    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getServicePageCount(I)I

    move-result v0

    if-le v0, v1, :cond_2

    :cond_1
    invoke-direct {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getActivitySpec(ILjava/lang/String;)Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;

    move-result-object p0

    if-eqz p0, :cond_2

    iget p1, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;->serviceNotifyIndex:I

    if-lez p1, :cond_2

    iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;->activity:Lmiuix/appcompat/app/AppCompatActivity;

    if-eqz p0, :cond_2

    invoke-virtual {p0}, Lmiuix/appcompat/app/AppCompatActivity;->hideFloatingDimBackground()V

    :cond_2
    return-void
.end method""",
        'replacement': """.method checkBg(ILjava/lang/String;)V
    .registers 5

    goto :goto_2

    nop

    :goto_0
    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getServicePageCount(I)I

    move-result v0

    goto :goto_9

    nop

    :goto_1
    return-void

    :goto_2
    iget-object v0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->mActivityCache:Landroid/util/SparseArray;

    goto :goto_12

    nop

    :goto_3
    if-nez v0, :cond_0

    goto :goto_8

    :cond_0
    goto :goto_e

    nop

    :goto_4
    if-gtz p1, :cond_1

    goto :goto_10

    :cond_1
    goto :goto_b

    nop

    :goto_5
    check-cast v0, Ljava/util/ArrayList;

    goto :goto_c

    nop

    :goto_6
    if-nez p0, :cond_2

    goto :goto_10

    :cond_2
    goto :goto_f

    nop

    :goto_7
    if-le v0, v1, :cond_3

    goto :goto_a

    :cond_3
    :goto_8
    goto :goto_0

    nop

    :goto_9
    if-gt v0, v1, :cond_4

    goto :goto_10

    :cond_4
    :goto_a
    goto :goto_11

    nop

    :goto_b
    iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;->activity:Lmiuix/appcompat/app/AppCompatActivity;

    goto :goto_6

    nop

    :goto_c
    const/4 v1, 0x1

    goto :goto_3

    nop

    :goto_d
    if-nez p0, :cond_5

    goto :goto_10

    :cond_5
    goto :goto_13

    nop

    :goto_e
    invoke-virtual {v0}, Ljava/util/ArrayList;->size()I

    move-result v0

    goto :goto_7

    nop

    :goto_f
    invoke-virtual {p0}, Lmiuix/appcompat/app/AppCompatActivity;->hideFloatingDimBackground()V

    :goto_10
    goto :goto_1

    nop

    :goto_11
    invoke-direct {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getActivitySpec(ILjava/lang/String;)Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;

    move-result-object p0

    goto :goto_d

    nop

    :goto_12
    invoke-virtual {v0, p1}, Landroid/util/SparseArray;->get(I)Ljava/lang/Object;

    move-result-object v0

    goto :goto_5

    nop

    :goto_13
    iget p1, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;->serviceNotifyIndex:I

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_floatingactivity_multiapp_MultiAppFloatingActivitySwitcher__clearActivitySpecTask',
        'method': '.method clearActivitySpecTask(ILjava/lang/String;)V',
        'method_name': 'clearActivitySpecTask',
        'method_anchors': ['invoke-direct {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getActivitySpec(ILjava/lang/String;)Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;', 'if-eqz p0, :cond_0', 'iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;->pendingTasks:Ljava/util/List;', 'invoke-interface {p0}, Ljava/util/List;->clear()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method clearActivitySpecTask(ILjava/lang/String;)V
    .registers 3

    invoke-direct {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getActivitySpec(ILjava/lang/String;)Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;

    move-result-object p0

    if-eqz p0, :cond_0

    iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;->pendingTasks:Ljava/util/List;

    invoke-interface {p0}, Ljava/util/List;->clear()V

    :cond_0
    return-void
.end method""",
        'replacement': """.method clearActivitySpecTask(ILjava/lang/String;)V
    .registers 3

    goto :goto_1

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;->pendingTasks:Ljava/util/List;

    goto :goto_3

    nop

    :goto_1
    invoke-direct {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getActivitySpec(ILjava/lang/String;)Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;

    move-result-object p0

    goto :goto_5

    nop

    :goto_2
    return-void

    :goto_3
    invoke-interface {p0}, Ljava/util/List;->clear()V

    :goto_4
    goto :goto_2

    nop

    :goto_5
    if-nez p0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_floatingactivity_multiapp_MultiAppFloatingActivitySwitcher__destroy',
        'method': '.method destroy()V',
        'method_name': 'destroy',
        'method_anchors': ['iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->mActivityCache:Landroid/util/SparseArray;', 'invoke-virtual {p0}, Landroid/util/SparseArray;->size()I', 'if-nez p0, :cond_0', 'sput-object p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->sInstance:Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;', 'return-void'],
        'type': 'method_replace',
        'search': """.method destroy()V
    .registers 1

    iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->mActivityCache:Landroid/util/SparseArray;

    invoke-virtual {p0}, Landroid/util/SparseArray;->size()I

    move-result p0

    if-nez p0, :cond_0

    const/4 p0, 0x0

    sput-object p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->sInstance:Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;

    :cond_0
    return-void
.end method""",
        'replacement': """.method destroy()V
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->mActivityCache:Landroid/util/SparseArray;

    goto :goto_6

    nop

    :goto_1
    if-eqz p0, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_2

    nop

    :goto_2
    const/4 p0, 0x0

    goto :goto_4

    nop

    :goto_3
    return-void

    :goto_4
    sput-object p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->sInstance:Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;

    :goto_5
    goto :goto_3

    nop

    :goto_6
    invoke-virtual {p0}, Landroid/util/SparseArray;->size()I

    move-result p0

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_floatingactivity_multiapp_MultiAppFloatingActivitySwitcher__getActivity',
        'method': '.method getActivity(ILjava/lang/String;)Lmiuix/appcompat/app/AppCompatActivity;',
        'method_name': 'getActivity',
        'method_anchors': ['invoke-direct {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getActivitySpec(ILjava/lang/String;)Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;', 'if-eqz p0, :cond_0', 'iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;->activity:Lmiuix/appcompat/app/AppCompatActivity;', 'return-object p0', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method getActivity(ILjava/lang/String;)Lmiuix/appcompat/app/AppCompatActivity;
    .registers 3

    invoke-direct {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getActivitySpec(ILjava/lang/String;)Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;

    move-result-object p0

    if-eqz p0, :cond_0

    iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;->activity:Lmiuix/appcompat/app/AppCompatActivity;

    return-object p0

    :cond_0
    const/4 p0, 0x0

    return-object p0
.end method""",
        'replacement': """.method getActivity(ILjava/lang/String;)Lmiuix/appcompat/app/AppCompatActivity;
    .registers 3

    goto :goto_4

    nop

    :goto_0
    return-object p0

    :goto_1
    goto :goto_6

    nop

    :goto_2
    return-object p0

    :goto_3
    if-nez p0, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_5

    nop

    :goto_4
    invoke-direct {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getActivitySpec(ILjava/lang/String;)Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;

    move-result-object p0

    goto :goto_3

    nop

    :goto_5
    iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;->activity:Lmiuix/appcompat/app/AppCompatActivity;

    goto :goto_0

    nop

    :goto_6
    const/4 p0, 0x0

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_floatingactivity_multiapp_MultiAppFloatingActivitySwitcher__getCurrentPageCount',
        'method': '.method getCurrentPageCount(I)I',
        'method_name': 'getCurrentPageCount',
        'method_anchors': ['iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->mActivityCache:Landroid/util/SparseArray;', 'invoke-virtual {p0, p1}, Landroid/util/SparseArray;->get(I)Ljava/lang/Object;', 'check-cast p0, Ljava/util/ArrayList;', 'if-eqz p0, :cond_0', 'invoke-virtual {p0}, Ljava/util/ArrayList;->size()I', 'return p0', 'return p0'],
        'type': 'method_replace',
        'search': """.method getCurrentPageCount(I)I
    .registers 2

    iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->mActivityCache:Landroid/util/SparseArray;

    invoke-virtual {p0, p1}, Landroid/util/SparseArray;->get(I)Ljava/lang/Object;

    move-result-object p0

    check-cast p0, Ljava/util/ArrayList;

    if-eqz p0, :cond_0

    invoke-virtual {p0}, Ljava/util/ArrayList;->size()I

    move-result p0

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method getCurrentPageCount(I)I
    .registers 2

    goto :goto_8

    nop

    :goto_0
    if-nez p0, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_4

    nop

    :goto_1
    invoke-virtual {p0, p1}, Landroid/util/SparseArray;->get(I)Ljava/lang/Object;

    move-result-object p0

    goto :goto_2

    nop

    :goto_2
    check-cast p0, Ljava/util/ArrayList;

    goto :goto_0

    nop

    :goto_3
    const/4 p0, 0x0

    goto :goto_7

    nop

    :goto_4
    invoke-virtual {p0}, Ljava/util/ArrayList;->size()I

    move-result p0

    goto :goto_5

    nop

    :goto_5
    return p0

    :goto_6
    goto :goto_3

    nop

    :goto_7
    return p0

    :goto_8
    iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->mActivityCache:Landroid/util/SparseArray;

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_floatingactivity_multiapp_MultiAppFloatingActivitySwitcher__getIdentity',
        'method': '.method getIdentity(Ljava/lang/Object;I)Ljava/lang/String;',
        'method_name': 'getIdentity',
        'method_anchors': ['new-instance p0, Ljava/lang/StringBuilder;', 'invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V', 'invoke-virtual {p1}, Ljava/lang/Object;->hashCode()I', 'invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;', 'const-string p1, ":"', 'invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'invoke-virtual {p0, p2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;', 'invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;'],
        'type': 'method_replace',
        'search': """.method getIdentity(Ljava/lang/Object;I)Ljava/lang/String;
    .registers 3

    new-instance p0, Ljava/lang/StringBuilder;

    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {p1}, Ljava/lang/Object;->hashCode()I

    move-result p1

    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    const-string p1, ":"

    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0, p2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method getIdentity(Ljava/lang/Object;I)Ljava/lang/String;
    .registers 3

    goto :goto_4

    nop

    :goto_0
    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_2

    nop

    :goto_1
    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_6

    nop

    :goto_2
    const-string p1, ":"

    goto :goto_5

    nop

    :goto_3
    invoke-virtual {p0, p2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_7

    nop

    :goto_4
    new-instance p0, Ljava/lang/StringBuilder;

    goto :goto_1

    nop

    :goto_5
    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_3

    nop

    :goto_6
    invoke-virtual {p1}, Ljava/lang/Object;->hashCode()I

    move-result p1

    goto :goto_0

    nop

    :goto_7
    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    goto :goto_8

    nop

    :goto_8
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_floatingactivity_multiapp_MultiAppFloatingActivitySwitcher__getLastActivityPanel',
        'method': '.method getLastActivityPanel()Landroid/view/View;',
        'method_name': 'getLastActivityPanel',
        'method_anchors': ['iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->mLastActivityPanel:Ljava/lang/ref/WeakReference;', 'if-nez p0, :cond_0', 'return-object p0', 'invoke-virtual {p0}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;', 'check-cast p0, Landroid/view/View;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method getLastActivityPanel()Landroid/view/View;
    .registers 1

    iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->mLastActivityPanel:Ljava/lang/ref/WeakReference;

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
    if-eqz p0, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_1

    nop

    :goto_1
    const/4 p0, 0x0

    goto :goto_2

    nop

    :goto_2
    return-object p0

    :goto_3
    goto :goto_7

    nop

    :goto_4
    return-object p0

    :goto_5
    iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->mLastActivityPanel:Ljava/lang/ref/WeakReference;

    goto :goto_0

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
        'id': 'miuix_appcompat_app_floatingactivity_multiapp_MultiAppFloatingActivitySwitcher__getServicePageCount',
        'method': '.method getServicePageCount(I)I',
        'method_name': 'getServicePageCount',
        'method_anchors': ['new-instance v0, Landroid/os/Bundle;', 'invoke-direct {v0}, Landroid/os/Bundle;-><init>()V', 'const-string v1, "key_task_id"', 'invoke-virtual {v0, v1, p1}, Landroid/os/Bundle;->putInt(Ljava/lang/String;I)V', 'invoke-direct {p0, v1, v0}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->notifyService(ILandroid/os/Bundle;)Landroid/os/Bundle;', 'if-eqz v0, :cond_0', 'invoke-static {v1}, Ljava/lang/String;->valueOf(I)Ljava/lang/String;', 'invoke-virtual {v0, v1}, Landroid/os/Bundle;->getInt(Ljava/lang/String;)I'],
        'type': 'method_replace',
        'search': """.method getServicePageCount(I)I
    .registers 6

    new-instance v0, Landroid/os/Bundle;

    invoke-direct {v0}, Landroid/os/Bundle;-><init>()V

    const-string v1, "key_task_id"

    invoke-virtual {v0, v1, p1}, Landroid/os/Bundle;->putInt(Ljava/lang/String;I)V

    const/4 v1, 0x6

    invoke-direct {p0, v1, v0}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->notifyService(ILandroid/os/Bundle;)Landroid/os/Bundle;

    move-result-object v0

    const/4 v2, 0x0

    if-eqz v0, :cond_0

    invoke-static {v1}, Ljava/lang/String;->valueOf(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Landroid/os/Bundle;->getInt(Ljava/lang/String;)I

    move-result v0

    goto :goto_0

    :cond_0
    move v0, v2

    :goto_0
    iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->mActivityCache:Landroid/util/SparseArray;

    invoke-virtual {p0, p1}, Landroid/util/SparseArray;->get(I)Ljava/lang/Object;

    move-result-object p0

    check-cast p0, Ljava/util/ArrayList;

    if-eqz p0, :cond_2

    invoke-virtual {p0}, Ljava/util/ArrayList;->size()I

    move-result p1

    :cond_1
    :goto_1
    if-ge v2, p1, :cond_2

    invoke-virtual {p0, v2}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v1

    add-int/lit8 v2, v2, 0x1

    check-cast v1, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;

    iget v1, v1, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;->index:I

    add-int/lit8 v3, v1, 0x1

    if-le v3, v0, :cond_1

    add-int/lit8 v1, v1, 0x1

    move v0, v1

    goto :goto_1

    :cond_2
    return v0
.end method""",
        'replacement': """.method getServicePageCount(I)I
    .registers 6

    goto :goto_0

    nop

    :goto_0
    new-instance v0, Landroid/os/Bundle;

    goto :goto_1d

    nop

    :goto_1
    if-nez v0, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_16

    nop

    :goto_2
    goto :goto_a

    :goto_3
    goto :goto_9

    nop

    :goto_4
    invoke-virtual {v0, v1, p1}, Landroid/os/Bundle;->putInt(Ljava/lang/String;I)V

    goto :goto_17

    nop

    :goto_5
    check-cast v1, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;

    goto :goto_13

    nop

    :goto_6
    invoke-virtual {p0, v2}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v1

    goto :goto_1c

    nop

    :goto_7
    if-nez p0, :cond_1

    goto :goto_1a

    :cond_1
    goto :goto_b

    nop

    :goto_8
    if-gt v3, v0, :cond_2

    goto :goto_c

    :cond_2
    goto :goto_12

    nop

    :goto_9
    move v0, v2

    :goto_a
    goto :goto_f

    nop

    :goto_b
    invoke-virtual {p0}, Ljava/util/ArrayList;->size()I

    move-result p1

    :goto_c
    goto :goto_15

    nop

    :goto_d
    add-int/lit8 v3, v1, 0x1

    goto :goto_8

    nop

    :goto_e
    invoke-virtual {v0, v1}, Landroid/os/Bundle;->getInt(Ljava/lang/String;)I

    move-result v0

    goto :goto_2

    nop

    :goto_f
    iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->mActivityCache:Landroid/util/SparseArray;

    goto :goto_1f

    nop

    :goto_10
    check-cast p0, Ljava/util/ArrayList;

    goto :goto_7

    nop

    :goto_11
    const/4 v2, 0x0

    goto :goto_1

    nop

    :goto_12
    add-int/lit8 v1, v1, 0x1

    goto :goto_1b

    nop

    :goto_13
    iget v1, v1, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;->index:I

    goto :goto_d

    nop

    :goto_14
    return v0

    :goto_15
    if-lt v2, p1, :cond_3

    goto :goto_1a

    :cond_3
    goto :goto_6

    nop

    :goto_16
    invoke-static {v1}, Ljava/lang/String;->valueOf(I)Ljava/lang/String;

    move-result-object v1

    goto :goto_e

    nop

    :goto_17
    const/4 v1, 0x6

    goto :goto_1e

    nop

    :goto_18
    const-string v1, "key_task_id"

    goto :goto_4

    nop

    :goto_19
    goto :goto_c

    :goto_1a
    goto :goto_14

    nop

    :goto_1b
    move v0, v1

    goto :goto_19

    nop

    :goto_1c
    add-int/lit8 v2, v2, 0x1

    goto :goto_5

    nop

    :goto_1d
    invoke-direct {v0}, Landroid/os/Bundle;-><init>()V

    goto :goto_18

    nop

    :goto_1e
    invoke-direct {p0, v1, v0}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->notifyService(ILandroid/os/Bundle;)Landroid/os/Bundle;

    move-result-object v0

    goto :goto_11

    nop

    :goto_1f
    invoke-virtual {p0, p1}, Landroid/util/SparseArray;->get(I)Ljava/lang/Object;

    move-result-object p0

    goto :goto_10

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_floatingactivity_multiapp_MultiAppFloatingActivitySwitcher__isAboveActivityFinishing',
        'method': '.method isAboveActivityFinishing(ILjava/lang/String;)Z',
        'method_name': 'isAboveActivityFinishing',
        'method_anchors': ['invoke-direct {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getActivitySpec(ILjava/lang/String;)Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;', 'if-nez p2, :cond_0', 'return v0', 'new-instance v1, Landroid/os/Bundle;', 'invoke-direct {v1}, Landroid/os/Bundle;-><init>()V', 'iget-object p2, p2, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;->serviceNotify:Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ServiceNotify;', 'invoke-virtual {p2}, Ljava/lang/Object;->hashCode()I', 'invoke-static {p2}, Ljava/lang/String;->valueOf(I)Ljava/lang/String;'],
        'type': 'method_replace',
        'search': """.method isAboveActivityFinishing(ILjava/lang/String;)Z
    .registers 6

    invoke-direct {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getActivitySpec(ILjava/lang/String;)Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;

    move-result-object p2

    const/4 v0, 0x0

    if-nez p2, :cond_0

    return v0

    :cond_0
    new-instance v1, Landroid/os/Bundle;

    invoke-direct {v1}, Landroid/os/Bundle;-><init>()V

    iget-object p2, p2, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;->serviceNotify:Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ServiceNotify;

    invoke-virtual {p2}, Ljava/lang/Object;->hashCode()I

    move-result p2

    invoke-static {p2}, Ljava/lang/String;->valueOf(I)Ljava/lang/String;

    move-result-object p2

    const-string v2, "key_request_identity"

    invoke-virtual {v1, v2, p2}, Landroid/os/Bundle;->putString(Ljava/lang/String;Ljava/lang/String;)V

    const-string p2, "key_task_id"

    invoke-virtual {v1, p2, p1}, Landroid/os/Bundle;->putInt(Ljava/lang/String;I)V

    const/16 p1, 0x9

    invoke-direct {p0, p1, v1}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->notifyService(ILandroid/os/Bundle;)Landroid/os/Bundle;

    move-result-object p0

    if-eqz p0, :cond_1

    const-string p1, "check_finishing"

    invoke-virtual {p0, p1}, Landroid/os/Bundle;->getBoolean(Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_1

    const/4 p0, 0x1

    return p0

    :cond_1
    return v0
.end method""",
        'replacement': """.method isAboveActivityFinishing(ILjava/lang/String;)Z
    .registers 6

    goto :goto_e

    nop

    :goto_0
    invoke-virtual {v1, v2, p2}, Landroid/os/Bundle;->putString(Ljava/lang/String;Ljava/lang/String;)V

    goto :goto_b

    nop

    :goto_1
    const-string v2, "key_request_identity"

    goto :goto_0

    nop

    :goto_2
    return p0

    :goto_3
    goto :goto_10

    nop

    :goto_4
    invoke-virtual {p0, p1}, Landroid/os/Bundle;->getBoolean(Ljava/lang/String;)Z

    move-result p0

    goto :goto_15

    nop

    :goto_5
    invoke-static {p2}, Ljava/lang/String;->valueOf(I)Ljava/lang/String;

    move-result-object p2

    goto :goto_1

    nop

    :goto_6
    if-nez p0, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_14

    nop

    :goto_7
    invoke-direct {p0, p1, v1}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->notifyService(ILandroid/os/Bundle;)Landroid/os/Bundle;

    move-result-object p0

    goto :goto_6

    nop

    :goto_8
    const/4 v0, 0x0

    goto :goto_17

    nop

    :goto_9
    invoke-virtual {v1, p2, p1}, Landroid/os/Bundle;->putInt(Ljava/lang/String;I)V

    goto :goto_11

    nop

    :goto_a
    new-instance v1, Landroid/os/Bundle;

    goto :goto_d

    nop

    :goto_b
    const-string p2, "key_task_id"

    goto :goto_9

    nop

    :goto_c
    const/4 p0, 0x1

    goto :goto_2

    nop

    :goto_d
    invoke-direct {v1}, Landroid/os/Bundle;-><init>()V

    goto :goto_f

    nop

    :goto_e
    invoke-direct {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getActivitySpec(ILjava/lang/String;)Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;

    move-result-object p2

    goto :goto_8

    nop

    :goto_f
    iget-object p2, p2, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;->serviceNotify:Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ServiceNotify;

    goto :goto_16

    nop

    :goto_10
    return v0

    :goto_11
    const/16 p1, 0x9

    goto :goto_7

    nop

    :goto_12
    return v0

    :goto_13
    goto :goto_a

    nop

    :goto_14
    const-string p1, "check_finishing"

    goto :goto_4

    nop

    :goto_15
    if-nez p0, :cond_1

    goto :goto_3

    :cond_1
    goto :goto_c

    nop

    :goto_16
    invoke-virtual {p2}, Ljava/lang/Object;->hashCode()I

    move-result p2

    goto :goto_5

    nop

    :goto_17
    if-eqz p2, :cond_2

    goto :goto_13

    :cond_2
    goto :goto_12

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_floatingactivity_multiapp_MultiAppFloatingActivitySwitcher__isServiceAvailable',
        'method': '.method isServiceAvailable()Z',
        'method_name': 'isServiceAvailable',
        'method_anchors': ['iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->mIFloatingService:Lmiuix/appcompat/app/floatingactivity/multiapp/IFloatingService;', 'if-eqz p0, :cond_0', 'return p0', 'return p0'],
        'type': 'method_replace',
        'search': """.method isServiceAvailable()Z
    .registers 1

    iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->mIFloatingService:Lmiuix/appcompat/app/floatingactivity/multiapp/IFloatingService;

    if-eqz p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method isServiceAvailable()Z
    .registers 1

    goto :goto_6

    nop

    :goto_0
    return p0

    :goto_1
    goto :goto_5

    nop

    :goto_2
    return p0

    :goto_3
    if-nez p0, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_4

    nop

    :goto_4
    const/4 p0, 0x1

    goto :goto_0

    nop

    :goto_5
    const/4 p0, 0x0

    goto :goto_2

    nop

    :goto_6
    iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->mIFloatingService:Lmiuix/appcompat/app/floatingactivity/multiapp/IFloatingService;

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_floatingactivity_multiapp_MultiAppFloatingActivitySwitcher__markActivityOpenEnterAnimExecutedInternal',
        'method': '.method markActivityOpenEnterAnimExecutedInternal(ILjava/lang/String;)V',
        'method_name': 'markActivityOpenEnterAnimExecutedInternal',
        'method_anchors': ['invoke-direct {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getActivitySpec(ILjava/lang/String;)Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;', 'if-eqz p0, :cond_0', 'iput-boolean p1, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;->isOpenEnterAnimExecuted:Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method markActivityOpenEnterAnimExecutedInternal(ILjava/lang/String;)V
    .registers 3

    invoke-direct {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getActivitySpec(ILjava/lang/String;)Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;

    move-result-object p0

    if-eqz p0, :cond_0

    const/4 p1, 0x1

    iput-boolean p1, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;->isOpenEnterAnimExecuted:Z

    :cond_0
    return-void
.end method""",
        'replacement': """.method markActivityOpenEnterAnimExecutedInternal(ILjava/lang/String;)V
    .registers 3

    goto :goto_3

    nop

    :goto_0
    return-void

    :goto_1
    if-nez p0, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_2

    nop

    :goto_2
    const/4 p1, 0x1

    goto :goto_4

    nop

    :goto_3
    invoke-direct {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getActivitySpec(ILjava/lang/String;)Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;

    move-result-object p0

    goto :goto_1

    nop

    :goto_4
    iput-boolean p1, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;->isOpenEnterAnimExecuted:Z

    :goto_5
    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_floatingactivity_multiapp_MultiAppFloatingActivitySwitcher__notifyPreviousActivitySlide',
        'method': '.method notifyPreviousActivitySlide(ILjava/lang/String;)V',
        'method_name': 'notifyPreviousActivitySlide',
        'method_anchors': ['invoke-direct {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getActivitySpec(ILjava/lang/String;)Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;', 'if-nez p1, :cond_0', 'return-void', 'new-instance p2, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$2;', 'invoke-direct {p2, p0, p1}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$2;-><init>(Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;)V', 'invoke-virtual {p0}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->isServiceAvailable()Z', 'if-eqz p0, :cond_1', 'invoke-interface {p2}, Ljava/lang/Runnable;->run()V'],
        'type': 'method_replace',
        'search': """.method notifyPreviousActivitySlide(ILjava/lang/String;)V
    .registers 3

    invoke-direct {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getActivitySpec(ILjava/lang/String;)Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;

    move-result-object p1

    if-nez p1, :cond_0

    return-void

    :cond_0
    new-instance p2, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$2;

    invoke-direct {p2, p0, p1}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$2;-><init>(Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;)V

    invoke-virtual {p0}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->isServiceAvailable()Z

    move-result p0

    if-eqz p0, :cond_1

    invoke-interface {p2}, Ljava/lang/Runnable;->run()V

    return-void

    :cond_1
    iget-object p0, p1, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;->pendingTasks:Ljava/util/List;

    invoke-interface {p0, p2}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    return-void
.end method""",
        'replacement': """.method notifyPreviousActivitySlide(ILjava/lang/String;)V
    .registers 3

    goto :goto_8

    nop

    :goto_0
    return-void

    :goto_1
    goto :goto_5

    nop

    :goto_2
    return-void

    :goto_3
    invoke-direct {p2, p0, p1}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$2;-><init>(Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;)V

    goto :goto_d

    nop

    :goto_4
    invoke-interface {p0, p2}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    goto :goto_2

    nop

    :goto_5
    new-instance p2, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$2;

    goto :goto_3

    nop

    :goto_6
    return-void

    :goto_7
    goto :goto_9

    nop

    :goto_8
    invoke-direct {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getActivitySpec(ILjava/lang/String;)Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;

    move-result-object p1

    goto :goto_b

    nop

    :goto_9
    iget-object p0, p1, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;->pendingTasks:Ljava/util/List;

    goto :goto_4

    nop

    :goto_a
    invoke-interface {p2}, Ljava/lang/Runnable;->run()V

    goto :goto_6

    nop

    :goto_b
    if-eqz p1, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_0

    nop

    :goto_c
    if-nez p0, :cond_1

    goto :goto_7

    :cond_1
    goto :goto_a

    nop

    :goto_d
    invoke-virtual {p0}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->isServiceAvailable()Z

    move-result p0

    goto :goto_c

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_floatingactivity_multiapp_MultiAppFloatingActivitySwitcher__postEnterAnimationTask',
        'method': '.method postEnterAnimationTask(ILjava/lang/String;Ljava/lang/Runnable;)V',
        'method_name': 'postEnterAnimationTask',
        'method_anchors': ['invoke-virtual {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->isActivityOpenEnterAnimExecuted(ILjava/lang/String;)Z', 'if-eqz v0, :cond_0', 'invoke-virtual {p0, p1}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getCurrentPageCount(I)I', 'if-gt v0, v1, :cond_1', 'invoke-virtual {p0, p1}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getServicePageCount(I)I', 'if-le v0, v1, :cond_2', 'invoke-virtual {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->markActivityOpenEnterAnimExecutedInternal(ILjava/lang/String;)V', 'invoke-virtual {p0}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->isServiceAvailable()Z'],
        'type': 'method_replace',
        'search': """.method postEnterAnimationTask(ILjava/lang/String;Ljava/lang/Runnable;)V
    .registers 6

    invoke-virtual {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->isActivityOpenEnterAnimExecuted(ILjava/lang/String;)Z

    move-result v0

    if-eqz v0, :cond_0

    goto :goto_0

    :cond_0
    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getCurrentPageCount(I)I

    move-result v0

    const/4 v1, 0x1

    if-gt v0, v1, :cond_1

    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getServicePageCount(I)I

    move-result v0

    if-le v0, v1, :cond_2

    :cond_1
    invoke-virtual {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->markActivityOpenEnterAnimExecutedInternal(ILjava/lang/String;)V

    :cond_2
    invoke-virtual {p0}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->isServiceAvailable()Z

    move-result v0

    if-eqz v0, :cond_3

    invoke-interface {p3}, Ljava/lang/Runnable;->run()V

    return-void

    :cond_3
    invoke-direct {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getActivitySpec(ILjava/lang/String;)Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;

    move-result-object p0

    if-eqz p0, :cond_4

    iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;->pendingTasks:Ljava/util/List;

    invoke-interface {p0, p3}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    :cond_4
    :goto_0
    return-void
.end method""",
        'replacement': """.method postEnterAnimationTask(ILjava/lang/String;Ljava/lang/Runnable;)V
    .registers 6

    goto :goto_a

    nop

    :goto_0
    const/4 v1, 0x1

    goto :goto_d

    nop

    :goto_1
    goto :goto_16

    :goto_2
    goto :goto_11

    nop

    :goto_3
    invoke-direct {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getActivitySpec(ILjava/lang/String;)Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;

    move-result-object p0

    goto :goto_e

    nop

    :goto_4
    invoke-virtual {p0}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->isServiceAvailable()Z

    move-result v0

    goto :goto_10

    nop

    :goto_5
    return-void

    :goto_6
    goto :goto_3

    nop

    :goto_7
    iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;->pendingTasks:Ljava/util/List;

    goto :goto_15

    nop

    :goto_8
    if-gt v0, v1, :cond_0

    goto :goto_13

    :cond_0
    :goto_9
    goto :goto_12

    nop

    :goto_a
    invoke-virtual {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->isActivityOpenEnterAnimExecuted(ILjava/lang/String;)Z

    move-result v0

    goto :goto_14

    nop

    :goto_b
    return-void

    :goto_c
    invoke-interface {p3}, Ljava/lang/Runnable;->run()V

    goto :goto_5

    nop

    :goto_d
    if-le v0, v1, :cond_1

    goto :goto_9

    :cond_1
    goto :goto_f

    nop

    :goto_e
    if-nez p0, :cond_2

    goto :goto_16

    :cond_2
    goto :goto_7

    nop

    :goto_f
    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getServicePageCount(I)I

    move-result v0

    goto :goto_8

    nop

    :goto_10
    if-nez v0, :cond_3

    goto :goto_6

    :cond_3
    goto :goto_c

    nop

    :goto_11
    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getCurrentPageCount(I)I

    move-result v0

    goto :goto_0

    nop

    :goto_12
    invoke-virtual {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->markActivityOpenEnterAnimExecutedInternal(ILjava/lang/String;)V

    :goto_13
    goto :goto_4

    nop

    :goto_14
    if-nez v0, :cond_4

    goto :goto_2

    :cond_4
    goto :goto_1

    nop

    :goto_15
    invoke-interface {p0, p3}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    :goto_16
    goto :goto_b

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_floatingactivity_multiapp_MultiAppFloatingActivitySwitcher__remove',
        'method': '.method remove(ILjava/lang/String;)V',
        'method_name': 'remove',
        'method_anchors': ['invoke-direct {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getActivitySpec(ILjava/lang/String;)Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;', 'if-eqz v0, :cond_1', 'iget-object v1, v0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;->activity:Lmiuix/appcompat/app/AppCompatActivity;', 'if-eqz v1, :cond_1', 'invoke-direct {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->unRegisterActivityFromService(ILjava/lang/String;)V', 'iget-object p2, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->mActivityCache:Landroid/util/SparseArray;', 'invoke-virtual {p2, p1}, Landroid/util/SparseArray;->get(I)Ljava/lang/Object;', 'check-cast p2, Ljava/util/ArrayList;'],
        'type': 'method_replace',
        'search': """.method remove(ILjava/lang/String;)V
    .registers 5

    invoke-direct {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getActivitySpec(ILjava/lang/String;)Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;

    move-result-object v0

    if-eqz v0, :cond_1

    iget-object v1, v0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;->activity:Lmiuix/appcompat/app/AppCompatActivity;

    if-eqz v1, :cond_1

    invoke-direct {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->unRegisterActivityFromService(ILjava/lang/String;)V

    iget-object p2, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->mActivityCache:Landroid/util/SparseArray;

    invoke-virtual {p2, p1}, Landroid/util/SparseArray;->get(I)Ljava/lang/Object;

    move-result-object p2

    check-cast p2, Ljava/util/ArrayList;

    if-eqz p2, :cond_0

    invoke-virtual {p2, v0}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    invoke-virtual {p2}, Ljava/util/ArrayList;->isEmpty()Z

    move-result p2

    if-eqz p2, :cond_0

    iget-object p2, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->mActivityCache:Landroid/util/SparseArray;

    invoke-virtual {p2, p1}, Landroid/util/SparseArray;->remove(I)V

    :cond_0
    iget-object p1, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->mActivityCache:Landroid/util/SparseArray;

    invoke-virtual {p1}, Landroid/util/SparseArray;->size()I

    move-result p1

    if-nez p1, :cond_1

    iget-object p1, v0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;->activity:Lmiuix/appcompat/app/AppCompatActivity;

    invoke-direct {p0, p1}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->unbindService(Landroid/content/Context;)V

    invoke-virtual {p0}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->clear()V

    :cond_1
    return-void
.end method""",
        'replacement': """.method remove(ILjava/lang/String;)V
    .registers 5

    goto :goto_11

    nop

    :goto_0
    if-nez v0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_16

    nop

    :goto_1
    if-nez p2, :cond_1

    goto :goto_f

    :cond_1
    goto :goto_9

    nop

    :goto_2
    iget-object p1, v0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;->activity:Lmiuix/appcompat/app/AppCompatActivity;

    goto :goto_d

    nop

    :goto_3
    invoke-virtual {p0}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->clear()V

    :goto_4
    goto :goto_c

    nop

    :goto_5
    if-nez v1, :cond_2

    goto :goto_4

    :cond_2
    goto :goto_15

    nop

    :goto_6
    invoke-virtual {p2, v0}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    goto :goto_8

    nop

    :goto_7
    iget-object p1, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->mActivityCache:Landroid/util/SparseArray;

    goto :goto_12

    nop

    :goto_8
    invoke-virtual {p2}, Ljava/util/ArrayList;->isEmpty()Z

    move-result p2

    goto :goto_1

    nop

    :goto_9
    iget-object p2, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->mActivityCache:Landroid/util/SparseArray;

    goto :goto_e

    nop

    :goto_a
    invoke-virtual {p2, p1}, Landroid/util/SparseArray;->get(I)Ljava/lang/Object;

    move-result-object p2

    goto :goto_14

    nop

    :goto_b
    if-nez p2, :cond_3

    goto :goto_f

    :cond_3
    goto :goto_6

    nop

    :goto_c
    return-void

    :goto_d
    invoke-direct {p0, p1}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->unbindService(Landroid/content/Context;)V

    goto :goto_3

    nop

    :goto_e
    invoke-virtual {p2, p1}, Landroid/util/SparseArray;->remove(I)V

    :goto_f
    goto :goto_7

    nop

    :goto_10
    if-eqz p1, :cond_4

    goto :goto_4

    :cond_4
    goto :goto_2

    nop

    :goto_11
    invoke-direct {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getActivitySpec(ILjava/lang/String;)Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;

    move-result-object v0

    goto :goto_0

    nop

    :goto_12
    invoke-virtual {p1}, Landroid/util/SparseArray;->size()I

    move-result p1

    goto :goto_10

    nop

    :goto_13
    iget-object p2, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->mActivityCache:Landroid/util/SparseArray;

    goto :goto_a

    nop

    :goto_14
    check-cast p2, Ljava/util/ArrayList;

    goto :goto_b

    nop

    :goto_15
    invoke-direct {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->unRegisterActivityFromService(ILjava/lang/String;)V

    goto :goto_13

    nop

    :goto_16
    iget-object v1, v0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;->activity:Lmiuix/appcompat/app/AppCompatActivity;

    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_floatingactivity_multiapp_MultiAppFloatingActivitySwitcher__saveBitmap',
        'method': '.method saveBitmap(Landroid/graphics/Bitmap;ILjava/lang/String;)V',
        'method_name': 'saveBitmap',
        'method_anchors': ['if-nez p1, :cond_0', 'invoke-direct {p0, p2, p3}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getActivitySpec(ILjava/lang/String;)Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;', 'if-nez p3, :cond_1', 'return-void', 'invoke-virtual {p1}, Landroid/graphics/Bitmap;->getByteCount()I', 'invoke-static {v2}, Ljava/nio/ByteBuffer;->allocate(I)Ljava/nio/ByteBuffer;', 'invoke-virtual {p1, v0}, Landroid/graphics/Bitmap;->copyPixelsToBuffer(Ljava/nio/Buffer;)V', 'iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->mIFloatingService:Lmiuix/appcompat/app/floatingactivity/multiapp/IFloatingService;'],
        'type': 'method_replace',
        'search': """.method saveBitmap(Landroid/graphics/Bitmap;ILjava/lang/String;)V
    .registers 11

    if-nez p1, :cond_0

    goto :goto_0

    :cond_0
    invoke-direct {p0, p2, p3}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getActivitySpec(ILjava/lang/String;)Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;

    move-result-object p3

    if-nez p3, :cond_1

    :goto_0
    return-void

    :cond_1
    invoke-virtual {p1}, Landroid/graphics/Bitmap;->getByteCount()I

    move-result v2

    invoke-static {v2}, Ljava/nio/ByteBuffer;->allocate(I)Ljava/nio/ByteBuffer;

    move-result-object v0

    invoke-virtual {p1, v0}, Landroid/graphics/Bitmap;->copyPixelsToBuffer(Ljava/nio/Buffer;)V

    iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->mIFloatingService:Lmiuix/appcompat/app/floatingactivity/multiapp/IFloatingService;

    invoke-virtual {v0}, Ljava/nio/ByteBuffer;->array()[B

    move-result-object v1

    invoke-virtual {p1}, Landroid/graphics/Bitmap;->getWidth()I

    move-result v3

    invoke-virtual {p1}, Landroid/graphics/Bitmap;->getHeight()I

    move-result v4

    iget-object p1, p3, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;->serviceNotify:Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ServiceNotify;

    invoke-virtual {p1}, Ljava/lang/Object;->hashCode()I

    move-result p1

    invoke-static {p1}, Ljava/lang/String;->valueOf(I)Ljava/lang/String;

    move-result-object v5

    move-object v0, p0

    move v6, p2

    invoke-static/range {v0 .. v6}, Lmiuix/appcompat/app/floatingactivity/MemoryFileUtil;->sendToFdServer(Lmiuix/appcompat/app/floatingactivity/multiapp/IFloatingService;[BIIILjava/lang/String;I)V

    return-void
.end method""",
        'replacement': """.method saveBitmap(Landroid/graphics/Bitmap;ILjava/lang/String;)V
    .registers 11

    goto :goto_b

    nop

    :goto_0
    invoke-virtual {p1}, Ljava/lang/Object;->hashCode()I

    move-result p1

    goto :goto_8

    nop

    :goto_1
    invoke-static {v2}, Ljava/nio/ByteBuffer;->allocate(I)Ljava/nio/ByteBuffer;

    move-result-object v0

    goto :goto_4

    nop

    :goto_2
    iget-object p0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->mIFloatingService:Lmiuix/appcompat/app/floatingactivity/multiapp/IFloatingService;

    goto :goto_13

    nop

    :goto_3
    invoke-virtual {p1}, Landroid/graphics/Bitmap;->getWidth()I

    move-result v3

    goto :goto_d

    nop

    :goto_4
    invoke-virtual {p1, v0}, Landroid/graphics/Bitmap;->copyPixelsToBuffer(Ljava/nio/Buffer;)V

    goto :goto_2

    nop

    :goto_5
    return-void

    :goto_6
    goto :goto_9

    nop

    :goto_7
    move v6, p2

    goto :goto_14

    nop

    :goto_8
    invoke-static {p1}, Ljava/lang/String;->valueOf(I)Ljava/lang/String;

    move-result-object v5

    goto :goto_a

    nop

    :goto_9
    invoke-virtual {p1}, Landroid/graphics/Bitmap;->getByteCount()I

    move-result v2

    goto :goto_1

    nop

    :goto_a
    move-object v0, p0

    goto :goto_7

    nop

    :goto_b
    if-eqz p1, :cond_0

    goto :goto_11

    :cond_0
    goto :goto_10

    nop

    :goto_c
    invoke-direct {p0, p2, p3}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getActivitySpec(ILjava/lang/String;)Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;

    move-result-object p3

    goto :goto_e

    nop

    :goto_d
    invoke-virtual {p1}, Landroid/graphics/Bitmap;->getHeight()I

    move-result v4

    goto :goto_12

    nop

    :goto_e
    if-eqz p3, :cond_1

    goto :goto_6

    :cond_1
    :goto_f
    goto :goto_5

    nop

    :goto_10
    goto :goto_f

    :goto_11
    goto :goto_c

    nop

    :goto_12
    iget-object p1, p3, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;->serviceNotify:Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ServiceNotify;

    goto :goto_0

    nop

    :goto_13
    invoke-virtual {v0}, Ljava/nio/ByteBuffer;->array()[B

    move-result-object v1

    goto :goto_3

    nop

    :goto_14
    invoke-static/range {v0 .. v6}, Lmiuix/appcompat/app/floatingactivity/MemoryFileUtil;->sendToFdServer(Lmiuix/appcompat/app/floatingactivity/multiapp/IFloatingService;[BIIILjava/lang/String;I)V

    goto :goto_15

    nop

    :goto_15
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_floatingactivity_multiapp_MultiAppFloatingActivitySwitcher__setLastActivityPanel',
        'method': '.method setLastActivityPanel(Landroid/view/View;)V',
        'method_name': 'setLastActivityPanel',
        'method_anchors': ['new-instance v0, Ljava/lang/ref/WeakReference;', 'invoke-direct {v0, p1}, Ljava/lang/ref/WeakReference;-><init>(Ljava/lang/Object;)V', 'iput-object v0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->mLastActivityPanel:Ljava/lang/ref/WeakReference;', 'return-void'],
        'type': 'method_replace',
        'search': """.method setLastActivityPanel(Landroid/view/View;)V
    .registers 3

    new-instance v0, Ljava/lang/ref/WeakReference;

    invoke-direct {v0, p1}, Ljava/lang/ref/WeakReference;-><init>(Ljava/lang/Object;)V

    iput-object v0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->mLastActivityPanel:Ljava/lang/ref/WeakReference;

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
    iput-object v0, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->mLastActivityPanel:Ljava/lang/ref/WeakReference;

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
    {
        'id': 'miuix_appcompat_app_floatingactivity_multiapp_MultiAppFloatingActivitySwitcher__updateResumeState',
        'method': '.method updateResumeState(ILjava/lang/String;Z)V',
        'method_name': 'updateResumeState',
        'method_anchors': ['invoke-direct {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getActivitySpec(ILjava/lang/String;)Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;', 'if-eqz p0, :cond_0', 'iput-boolean p3, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;->resumed:Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method updateResumeState(ILjava/lang/String;Z)V
    .registers 4

    invoke-direct {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getActivitySpec(ILjava/lang/String;)Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;

    move-result-object p0

    if-eqz p0, :cond_0

    iput-boolean p3, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;->resumed:Z

    :cond_0
    return-void
.end method""",
        'replacement': """.method updateResumeState(ILjava/lang/String;Z)V
    .registers 4

    goto :goto_4

    nop

    :goto_0
    if-nez p0, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_1

    nop

    :goto_1
    iput-boolean p3, p0, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;->resumed:Z

    :goto_2
    goto :goto_3

    nop

    :goto_3
    return-void

    :goto_4
    invoke-direct {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher;->getActivitySpec(ILjava/lang/String;)Lmiuix/appcompat/app/floatingactivity/multiapp/MultiAppFloatingActivitySwitcher$ActivitySpec;

    move-result-object p0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
