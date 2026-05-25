TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/controller/FolmeTouch$InnerViewTouchListener.smali'
CLASS_FALLBACK_NAMES = ['FolmeTouch$InnerViewTouchListener.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Landroid/view/View$OnTouchListener;']

PATCHES = [
    {
        'id': 'miuix_animation_controller_FolmeTouch__InnerViewTouchListener__removeTouch',
        'method': '.method removeTouch(Lmiuix/animation/controller/FolmeTouch;)Z',
        'method_name': 'removeTouch',
        'method_anchors': ['iget-object v0, p0, Lmiuix/animation/controller/FolmeTouch$InnerViewTouchListener;->mTouchMap:Ljava/util/WeakHashMap;', 'invoke-virtual {v0, p1}, Ljava/util/WeakHashMap;->remove(Ljava/lang/Object;)Ljava/lang/Object;', 'iget-object p0, p0, Lmiuix/animation/controller/FolmeTouch$InnerViewTouchListener;->mTouchMap:Ljava/util/WeakHashMap;', 'invoke-virtual {p0}, Ljava/util/WeakHashMap;->isEmpty()Z', 'return p0'],
        'type': 'method_replace',
        'search': """.method removeTouch(Lmiuix/animation/controller/FolmeTouch;)Z
    .registers 3

    iget-object v0, p0, Lmiuix/animation/controller/FolmeTouch$InnerViewTouchListener;->mTouchMap:Ljava/util/WeakHashMap;

    invoke-virtual {v0, p1}, Ljava/util/WeakHashMap;->remove(Ljava/lang/Object;)Ljava/lang/Object;

    iget-object p0, p0, Lmiuix/animation/controller/FolmeTouch$InnerViewTouchListener;->mTouchMap:Ljava/util/WeakHashMap;

    invoke-virtual {p0}, Ljava/util/WeakHashMap;->isEmpty()Z

    move-result p0

    return p0
.end method""",
        'replacement': """.method removeTouch(Lmiuix/animation/controller/FolmeTouch;)Z
    .registers 3

    goto :goto_0

    nop

    :goto_0
    iget-object v0, p0, Lmiuix/animation/controller/FolmeTouch$InnerViewTouchListener;->mTouchMap:Ljava/util/WeakHashMap;

    goto :goto_4

    nop

    :goto_1
    return p0

    :goto_2
    iget-object p0, p0, Lmiuix/animation/controller/FolmeTouch$InnerViewTouchListener;->mTouchMap:Ljava/util/WeakHashMap;

    goto :goto_3

    nop

    :goto_3
    invoke-virtual {p0}, Ljava/util/WeakHashMap;->isEmpty()Z

    move-result p0

    goto :goto_1

    nop

    :goto_4
    invoke-virtual {v0, p1}, Ljava/util/WeakHashMap;->remove(Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_controller_FolmeTouch__InnerViewTouchListener__addTouch',
        'method': '.method varargs addTouch(Lmiuix/animation/controller/FolmeTouch;[Lmiuix/animation/base/AnimConfig;)V',
        'method_name': 'addTouch',
        'method_anchors': ['iget-object p0, p0, Lmiuix/animation/controller/FolmeTouch$InnerViewTouchListener;->mTouchMap:Ljava/util/WeakHashMap;', 'invoke-virtual {p0, p1, p2}, Ljava/util/WeakHashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;', 'return-void'],
        'type': 'method_replace',
        'search': """.method varargs addTouch(Lmiuix/animation/controller/FolmeTouch;[Lmiuix/animation/base/AnimConfig;)V
    .registers 3

    iget-object p0, p0, Lmiuix/animation/controller/FolmeTouch$InnerViewTouchListener;->mTouchMap:Ljava/util/WeakHashMap;

    invoke-virtual {p0, p1, p2}, Ljava/util/WeakHashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    return-void
.end method""",
        'replacement': """.method varargs addTouch(Lmiuix/animation/controller/FolmeTouch;[Lmiuix/animation/base/AnimConfig;)V
    .registers 3

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/animation/controller/FolmeTouch$InnerViewTouchListener;->mTouchMap:Ljava/util/WeakHashMap;

    goto :goto_2

    nop

    :goto_1
    return-void

    :goto_2
    invoke-virtual {p0, p1, p2}, Ljava/util/WeakHashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
