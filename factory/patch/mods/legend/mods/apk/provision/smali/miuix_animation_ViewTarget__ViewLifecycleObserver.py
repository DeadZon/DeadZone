TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/ViewTarget$ViewLifecycleObserver.smali'
CLASS_FALLBACK_NAMES = ['ViewTarget$ViewLifecycleObserver.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Landroidx/lifecycle/LifecycleObserver;']

PATCHES = [
    {
        'id': 'miuix_animation_ViewTarget__ViewLifecycleObserver__onDestroy',
        'method': '.method onDestroy()V',
        'method_name': 'onDestroy',
        'method_anchors': ['iget-object p0, p0, Lmiuix/animation/ViewTarget$ViewLifecycleObserver;->this$0:Lmiuix/animation/ViewTarget;', 'invoke-static {p0}, Lmiuix/animation/ViewTarget;->access$800(Lmiuix/animation/ViewTarget;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method onDestroy()V
    .registers 1
    .annotation runtime Landroidx/lifecycle/OnLifecycleEvent;
        value = .enum Landroidx/lifecycle/Lifecycle$Event;->ON_DESTROY:Landroidx/lifecycle/Lifecycle$Event;
    .end annotation

    iget-object p0, p0, Lmiuix/animation/ViewTarget$ViewLifecycleObserver;->this$0:Lmiuix/animation/ViewTarget;

    invoke-static {p0}, Lmiuix/animation/ViewTarget;->access$800(Lmiuix/animation/ViewTarget;)V

    return-void
.end method""",
        'replacement': """.method onDestroy()V
    .registers 1
    .annotation runtime Landroidx/lifecycle/OnLifecycleEvent;
        value = .enum Landroidx/lifecycle/Lifecycle$Event;->ON_DESTROY:Landroidx/lifecycle/Lifecycle$Event;
    .end annotation

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/animation/ViewTarget$ViewLifecycleObserver;->this$0:Lmiuix/animation/ViewTarget;

    goto :goto_1

    nop

    :goto_1
    invoke-static {p0}, Lmiuix/animation/ViewTarget;->access$800(Lmiuix/animation/ViewTarget;)V

    goto :goto_2

    nop

    :goto_2
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_ViewTarget__ViewLifecycleObserver__onResume',
        'method': '.method onResume()V',
        'method_name': 'onResume',
        'method_anchors': ['iget-object p0, p0, Lmiuix/animation/ViewTarget$ViewLifecycleObserver;->this$0:Lmiuix/animation/ViewTarget;', 'invoke-static {p0}, Lmiuix/animation/ViewTarget;->access$600(Lmiuix/animation/ViewTarget;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method onResume()V
    .registers 1
    .annotation runtime Landroidx/lifecycle/OnLifecycleEvent;
        value = .enum Landroidx/lifecycle/Lifecycle$Event;->ON_RESUME:Landroidx/lifecycle/Lifecycle$Event;
    .end annotation

    iget-object p0, p0, Lmiuix/animation/ViewTarget$ViewLifecycleObserver;->this$0:Lmiuix/animation/ViewTarget;

    invoke-static {p0}, Lmiuix/animation/ViewTarget;->access$600(Lmiuix/animation/ViewTarget;)V

    return-void
.end method""",
        'replacement': """.method onResume()V
    .registers 1
    .annotation runtime Landroidx/lifecycle/OnLifecycleEvent;
        value = .enum Landroidx/lifecycle/Lifecycle$Event;->ON_RESUME:Landroidx/lifecycle/Lifecycle$Event;
    .end annotation

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    iget-object p0, p0, Lmiuix/animation/ViewTarget$ViewLifecycleObserver;->this$0:Lmiuix/animation/ViewTarget;

    goto :goto_2

    nop

    :goto_2
    invoke-static {p0}, Lmiuix/animation/ViewTarget;->access$600(Lmiuix/animation/ViewTarget;)V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_ViewTarget__ViewLifecycleObserver__onStop',
        'method': '.method onStop()V',
        'method_name': 'onStop',
        'method_anchors': ['invoke-static {}, Lmiuix/animation/Folme;->enableSleep()Z', 'if-eqz v0, :cond_0', 'iget-object p0, p0, Lmiuix/animation/ViewTarget$ViewLifecycleObserver;->this$0:Lmiuix/animation/ViewTarget;', 'invoke-static {p0}, Lmiuix/animation/ViewTarget;->access$700(Lmiuix/animation/ViewTarget;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method onStop()V
    .registers 2
    .annotation runtime Landroidx/lifecycle/OnLifecycleEvent;
        value = .enum Landroidx/lifecycle/Lifecycle$Event;->ON_RESUME:Landroidx/lifecycle/Lifecycle$Event;
    .end annotation

    invoke-static {}, Lmiuix/animation/Folme;->enableSleep()Z

    move-result v0

    if-eqz v0, :cond_0

    iget-object p0, p0, Lmiuix/animation/ViewTarget$ViewLifecycleObserver;->this$0:Lmiuix/animation/ViewTarget;

    invoke-static {p0}, Lmiuix/animation/ViewTarget;->access$700(Lmiuix/animation/ViewTarget;)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method onStop()V
    .registers 2
    .annotation runtime Landroidx/lifecycle/OnLifecycleEvent;
        value = .enum Landroidx/lifecycle/Lifecycle$Event;->ON_RESUME:Landroidx/lifecycle/Lifecycle$Event;
    .end annotation

    goto :goto_2

    nop

    :goto_0
    invoke-static {p0}, Lmiuix/animation/ViewTarget;->access$700(Lmiuix/animation/ViewTarget;)V

    :goto_1
    goto :goto_4

    nop

    :goto_2
    invoke-static {}, Lmiuix/animation/Folme;->enableSleep()Z

    move-result v0

    goto :goto_5

    nop

    :goto_3
    iget-object p0, p0, Lmiuix/animation/ViewTarget$ViewLifecycleObserver;->this$0:Lmiuix/animation/ViewTarget;

    goto :goto_0

    nop

    :goto_4
    return-void

    :goto_5
    if-nez v0, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
