TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/controller/FolmeTouch$LongClickTask.smali'
CLASS_FALLBACK_NAMES = ['FolmeTouch$LongClickTask.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Ljava/lang/Runnable;']

PATCHES = [
    {
        'id': 'miuix_animation_controller_FolmeTouch__LongClickTask__start',
        'method': '.method start(Lmiuix/animation/controller/FolmeTouch;)V',
        'method_name': 'start',
        'method_anchors': ['iget-object v0, p1, Lmiuix/animation/controller/FolmeBase;->mState:Lmiuix/animation/controller/IFolmeStateStyle;', 'invoke-interface {v0}, Lmiuix/animation/controller/IFolmeStateStyle;->getTarget()Lmiuix/animation/IAnimTarget;', 'if-eqz v1, :cond_0', 'check-cast v0, Lmiuix/animation/ViewTarget;', 'invoke-virtual {v0}, Lmiuix/animation/ViewTarget;->getTargetObject()Landroid/view/View;', 'if-eqz v0, :cond_0', 'new-instance v1, Ljava/lang/ref/WeakReference;', 'invoke-direct {v1, p1}, Ljava/lang/ref/WeakReference;-><init>(Ljava/lang/Object;)V'],
        'type': 'method_replace',
        'search': """.method start(Lmiuix/animation/controller/FolmeTouch;)V
    .registers 5

    iget-object v0, p1, Lmiuix/animation/controller/FolmeBase;->mState:Lmiuix/animation/controller/IFolmeStateStyle;

    invoke-interface {v0}, Lmiuix/animation/controller/IFolmeStateStyle;->getTarget()Lmiuix/animation/IAnimTarget;

    move-result-object v0

    instance-of v1, v0, Lmiuix/animation/ViewTarget;

    if-eqz v1, :cond_0

    check-cast v0, Lmiuix/animation/ViewTarget;

    invoke-virtual {v0}, Lmiuix/animation/ViewTarget;->getTargetObject()Landroid/view/View;

    move-result-object v0

    if-eqz v0, :cond_0

    new-instance v1, Ljava/lang/ref/WeakReference;

    invoke-direct {v1, p1}, Ljava/lang/ref/WeakReference;-><init>(Ljava/lang/Object;)V

    iput-object v1, p0, Lmiuix/animation/controller/FolmeTouch$LongClickTask;->mTouchRef:Ljava/lang/ref/WeakReference;

    invoke-static {}, Landroid/view/ViewConfiguration;->getLongPressTimeout()I

    move-result p1

    int-to-long v1, p1

    invoke-virtual {v0, p0, v1, v2}, Landroid/view/View;->postDelayed(Ljava/lang/Runnable;J)Z

    :cond_0
    return-void
.end method""",
        'replacement': """.method start(Lmiuix/animation/controller/FolmeTouch;)V
    .registers 5

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    iget-object v0, p1, Lmiuix/animation/controller/FolmeBase;->mState:Lmiuix/animation/controller/IFolmeStateStyle;

    goto :goto_a

    nop

    :goto_2
    invoke-virtual {v0, p0, v1, v2}, Landroid/view/View;->postDelayed(Ljava/lang/Runnable;J)Z

    :goto_3
    goto :goto_0

    nop

    :goto_4
    if-nez v0, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_b

    nop

    :goto_5
    invoke-direct {v1, p1}, Ljava/lang/ref/WeakReference;-><init>(Ljava/lang/Object;)V

    goto :goto_8

    nop

    :goto_6
    if-nez v1, :cond_1

    goto :goto_3

    :cond_1
    goto :goto_9

    nop

    :goto_7
    instance-of v1, v0, Lmiuix/animation/ViewTarget;

    goto :goto_6

    nop

    :goto_8
    iput-object v1, p0, Lmiuix/animation/controller/FolmeTouch$LongClickTask;->mTouchRef:Ljava/lang/ref/WeakReference;

    goto :goto_d

    nop

    :goto_9
    check-cast v0, Lmiuix/animation/ViewTarget;

    goto :goto_e

    nop

    :goto_a
    invoke-interface {v0}, Lmiuix/animation/controller/IFolmeStateStyle;->getTarget()Lmiuix/animation/IAnimTarget;

    move-result-object v0

    goto :goto_7

    nop

    :goto_b
    new-instance v1, Ljava/lang/ref/WeakReference;

    goto :goto_5

    nop

    :goto_c
    int-to-long v1, p1

    goto :goto_2

    nop

    :goto_d
    invoke-static {}, Landroid/view/ViewConfiguration;->getLongPressTimeout()I

    move-result p1

    goto :goto_c

    nop

    :goto_e
    invoke-virtual {v0}, Lmiuix/animation/ViewTarget;->getTargetObject()Landroid/view/View;

    move-result-object v0

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_controller_FolmeTouch__LongClickTask__stop',
        'method': '.method stop(Lmiuix/animation/controller/FolmeTouch;)V',
        'method_name': 'stop',
        'method_anchors': ['iget-object p1, p1, Lmiuix/animation/controller/FolmeBase;->mState:Lmiuix/animation/controller/IFolmeStateStyle;', 'invoke-interface {p1}, Lmiuix/animation/controller/IFolmeStateStyle;->getTarget()Lmiuix/animation/IAnimTarget;', 'if-eqz v0, :cond_0', 'check-cast p1, Lmiuix/animation/ViewTarget;', 'invoke-virtual {p1}, Lmiuix/animation/ViewTarget;->getTargetObject()Landroid/view/View;', 'if-eqz p1, :cond_0', 'invoke-virtual {p1, p0}, Landroid/view/View;->removeCallbacks(Ljava/lang/Runnable;)Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method stop(Lmiuix/animation/controller/FolmeTouch;)V
    .registers 3

    iget-object p1, p1, Lmiuix/animation/controller/FolmeBase;->mState:Lmiuix/animation/controller/IFolmeStateStyle;

    invoke-interface {p1}, Lmiuix/animation/controller/IFolmeStateStyle;->getTarget()Lmiuix/animation/IAnimTarget;

    move-result-object p1

    instance-of v0, p1, Lmiuix/animation/ViewTarget;

    if-eqz v0, :cond_0

    check-cast p1, Lmiuix/animation/ViewTarget;

    invoke-virtual {p1}, Lmiuix/animation/ViewTarget;->getTargetObject()Landroid/view/View;

    move-result-object p1

    if-eqz p1, :cond_0

    invoke-virtual {p1, p0}, Landroid/view/View;->removeCallbacks(Ljava/lang/Runnable;)Z

    :cond_0
    return-void
.end method""",
        'replacement': """.method stop(Lmiuix/animation/controller/FolmeTouch;)V
    .registers 3

    goto :goto_7

    nop

    :goto_0
    return-void

    :goto_1
    instance-of v0, p1, Lmiuix/animation/ViewTarget;

    goto :goto_8

    nop

    :goto_2
    invoke-virtual {p1, p0}, Landroid/view/View;->removeCallbacks(Ljava/lang/Runnable;)Z

    :goto_3
    goto :goto_0

    nop

    :goto_4
    if-nez p1, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_2

    nop

    :goto_5
    invoke-virtual {p1}, Lmiuix/animation/ViewTarget;->getTargetObject()Landroid/view/View;

    move-result-object p1

    goto :goto_4

    nop

    :goto_6
    invoke-interface {p1}, Lmiuix/animation/controller/IFolmeStateStyle;->getTarget()Lmiuix/animation/IAnimTarget;

    move-result-object p1

    goto :goto_1

    nop

    :goto_7
    iget-object p1, p1, Lmiuix/animation/controller/FolmeBase;->mState:Lmiuix/animation/controller/IFolmeStateStyle;

    goto :goto_6

    nop

    :goto_8
    if-nez v0, :cond_1

    goto :goto_3

    :cond_1
    goto :goto_9

    nop

    :goto_9
    check-cast p1, Lmiuix/animation/ViewTarget;

    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
