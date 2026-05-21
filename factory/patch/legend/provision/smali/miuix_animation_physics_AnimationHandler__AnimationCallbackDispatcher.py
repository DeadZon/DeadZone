TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/physics/AnimationHandler$AnimationCallbackDispatcher.smali'
CLASS_FALLBACK_NAMES = ['AnimationHandler$AnimationCallbackDispatcher.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'miuix_animation_physics_AnimationHandler__AnimationCallbackDispatcher__dispatchAnimationFrame',
        'method': '.method dispatchAnimationFrame(J)V',
        'method_name': 'dispatchAnimationFrame',
        'method_anchors': ['iget-object v0, p0, Lmiuix/animation/physics/AnimationHandler$AnimationCallbackDispatcher;->this$0:Lmiuix/animation/physics/AnimationHandler;', 'invoke-static {v0, p1, p2}, Lmiuix/animation/physics/AnimationHandler;->access$000(Lmiuix/animation/physics/AnimationHandler;J)V', 'iget-object p1, p0, Lmiuix/animation/physics/AnimationHandler$AnimationCallbackDispatcher;->this$0:Lmiuix/animation/physics/AnimationHandler;', 'invoke-static {p1}, Lmiuix/animation/physics/AnimationHandler;->access$100(Lmiuix/animation/physics/AnimationHandler;)Ljava/util/ArrayList;', 'invoke-virtual {p1}, Ljava/util/ArrayList;->size()I', 'if-lez p1, :cond_0', 'iget-object p0, p0, Lmiuix/animation/physics/AnimationHandler$AnimationCallbackDispatcher;->this$0:Lmiuix/animation/physics/AnimationHandler;', 'invoke-static {p0}, Lmiuix/animation/physics/AnimationHandler;->access$200(Lmiuix/animation/physics/AnimationHandler;)Lmiuix/animation/physics/AnimationHandler$AnimationFrameCallbackProvider;'],
        'type': 'method_replace',
        'search': """.method dispatchAnimationFrame(J)V
    .registers 4

    iget-object v0, p0, Lmiuix/animation/physics/AnimationHandler$AnimationCallbackDispatcher;->this$0:Lmiuix/animation/physics/AnimationHandler;

    invoke-static {v0, p1, p2}, Lmiuix/animation/physics/AnimationHandler;->access$000(Lmiuix/animation/physics/AnimationHandler;J)V

    iget-object p1, p0, Lmiuix/animation/physics/AnimationHandler$AnimationCallbackDispatcher;->this$0:Lmiuix/animation/physics/AnimationHandler;

    invoke-static {p1}, Lmiuix/animation/physics/AnimationHandler;->access$100(Lmiuix/animation/physics/AnimationHandler;)Ljava/util/ArrayList;

    move-result-object p1

    invoke-virtual {p1}, Ljava/util/ArrayList;->size()I

    move-result p1

    if-lez p1, :cond_0

    iget-object p0, p0, Lmiuix/animation/physics/AnimationHandler$AnimationCallbackDispatcher;->this$0:Lmiuix/animation/physics/AnimationHandler;

    invoke-static {p0}, Lmiuix/animation/physics/AnimationHandler;->access$200(Lmiuix/animation/physics/AnimationHandler;)Lmiuix/animation/physics/AnimationHandler$AnimationFrameCallbackProvider;

    move-result-object p0

    invoke-virtual {p0}, Lmiuix/animation/physics/AnimationHandler$AnimationFrameCallbackProvider;->postFrameCallback()V

    :cond_0
    return-void
.end method""",
        'replacement': """.method dispatchAnimationFrame(J)V
    .registers 4

    goto :goto_0

    nop

    :goto_0
    iget-object v0, p0, Lmiuix/animation/physics/AnimationHandler$AnimationCallbackDispatcher;->this$0:Lmiuix/animation/physics/AnimationHandler;

    goto :goto_9

    nop

    :goto_1
    invoke-static {p1}, Lmiuix/animation/physics/AnimationHandler;->access$100(Lmiuix/animation/physics/AnimationHandler;)Ljava/util/ArrayList;

    move-result-object p1

    goto :goto_7

    nop

    :goto_2
    invoke-virtual {p0}, Lmiuix/animation/physics/AnimationHandler$AnimationFrameCallbackProvider;->postFrameCallback()V

    :goto_3
    goto :goto_6

    nop

    :goto_4
    iget-object p0, p0, Lmiuix/animation/physics/AnimationHandler$AnimationCallbackDispatcher;->this$0:Lmiuix/animation/physics/AnimationHandler;

    goto :goto_5

    nop

    :goto_5
    invoke-static {p0}, Lmiuix/animation/physics/AnimationHandler;->access$200(Lmiuix/animation/physics/AnimationHandler;)Lmiuix/animation/physics/AnimationHandler$AnimationFrameCallbackProvider;

    move-result-object p0

    goto :goto_2

    nop

    :goto_6
    return-void

    :goto_7
    invoke-virtual {p1}, Ljava/util/ArrayList;->size()I

    move-result p1

    goto :goto_8

    nop

    :goto_8
    if-gtz p1, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_4

    nop

    :goto_9
    invoke-static {v0, p1, p2}, Lmiuix/animation/physics/AnimationHandler;->access$000(Lmiuix/animation/physics/AnimationHandler;J)V

    goto :goto_a

    nop

    :goto_a
    iget-object p1, p0, Lmiuix/animation/physics/AnimationHandler$AnimationCallbackDispatcher;->this$0:Lmiuix/animation/physics/AnimationHandler;

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
