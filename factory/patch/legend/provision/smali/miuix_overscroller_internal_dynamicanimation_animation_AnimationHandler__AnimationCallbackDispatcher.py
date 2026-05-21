TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/overscroller/internal/dynamicanimation/animation/AnimationHandler$AnimationCallbackDispatcher.smali'
CLASS_FALLBACK_NAMES = ['AnimationHandler$AnimationCallbackDispatcher.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'miuix_overscroller_internal_dynamicanimation_animation_AnimationHandler__AnimationCallbackDispatcher__dispatchAnimationFrame',
        'method': '.method dispatchAnimationFrame(J)V',
        'method_name': 'dispatchAnimationFrame',
        'method_anchors': ['iget-object v0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler$AnimationCallbackDispatcher;->this$0:Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler;', 'invoke-static {v0, p1, p2}, Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler;->access$000(Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler;J)V', 'iget-object p1, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler$AnimationCallbackDispatcher;->this$0:Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler;', 'invoke-static {p1}, Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler;->access$100(Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler;)Ljava/util/ArrayList;', 'invoke-virtual {p1}, Ljava/util/ArrayList;->size()I', 'if-lez p1, :cond_0', 'iget-object p0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler$AnimationCallbackDispatcher;->this$0:Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler;', 'invoke-virtual {p0}, Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler;->getProvider()Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler$AnimationFrameCallbackProvider;'],
        'type': 'method_replace',
        'search': """.method dispatchAnimationFrame(J)V
    .registers 4

    iget-object v0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler$AnimationCallbackDispatcher;->this$0:Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler;

    invoke-static {v0, p1, p2}, Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler;->access$000(Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler;J)V

    iget-object p1, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler$AnimationCallbackDispatcher;->this$0:Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler;

    invoke-static {p1}, Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler;->access$100(Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler;)Ljava/util/ArrayList;

    move-result-object p1

    invoke-virtual {p1}, Ljava/util/ArrayList;->size()I

    move-result p1

    if-lez p1, :cond_0

    iget-object p0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler$AnimationCallbackDispatcher;->this$0:Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler;

    invoke-virtual {p0}, Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler;->getProvider()Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler$AnimationFrameCallbackProvider;

    move-result-object p0

    invoke-virtual {p0}, Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler$AnimationFrameCallbackProvider;->postFrameCallback()V

    :cond_0
    return-void
.end method""",
        'replacement': """.method dispatchAnimationFrame(J)V
    .registers 4

    goto :goto_7

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler$AnimationCallbackDispatcher;->this$0:Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler;

    goto :goto_8

    nop

    :goto_1
    return-void

    :goto_2
    invoke-static {v0, p1, p2}, Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler;->access$000(Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler;J)V

    goto :goto_4

    nop

    :goto_3
    if-gtz p1, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_0

    nop

    :goto_4
    iget-object p1, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler$AnimationCallbackDispatcher;->this$0:Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler;

    goto :goto_a

    nop

    :goto_5
    invoke-virtual {p0}, Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler$AnimationFrameCallbackProvider;->postFrameCallback()V

    :goto_6
    goto :goto_1

    nop

    :goto_7
    iget-object v0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler$AnimationCallbackDispatcher;->this$0:Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler;

    goto :goto_2

    nop

    :goto_8
    invoke-virtual {p0}, Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler;->getProvider()Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler$AnimationFrameCallbackProvider;

    move-result-object p0

    goto :goto_5

    nop

    :goto_9
    invoke-virtual {p1}, Ljava/util/ArrayList;->size()I

    move-result p1

    goto :goto_3

    nop

    :goto_a
    invoke-static {p1}, Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler;->access$100(Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler;)Ljava/util/ArrayList;

    move-result-object p1

    goto :goto_9

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
