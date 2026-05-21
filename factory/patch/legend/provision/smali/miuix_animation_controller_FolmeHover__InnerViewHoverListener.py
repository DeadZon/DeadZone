TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/controller/FolmeHover$InnerViewHoverListener.smali'
CLASS_FALLBACK_NAMES = ['FolmeHover$InnerViewHoverListener.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Landroid/view/View$OnHoverListener;']

PATCHES = [
    {
        'id': 'miuix_animation_controller_FolmeHover__InnerViewHoverListener__removeHover',
        'method': '.method removeHover(Lmiuix/animation/controller/FolmeHover;)Z',
        'method_name': 'removeHover',
        'method_anchors': ['iget-object v0, p0, Lmiuix/animation/controller/FolmeHover$InnerViewHoverListener;->mHoverMap:Ljava/util/WeakHashMap;', 'invoke-virtual {v0, p1}, Ljava/util/WeakHashMap;->remove(Ljava/lang/Object;)Ljava/lang/Object;', 'iget-object p0, p0, Lmiuix/animation/controller/FolmeHover$InnerViewHoverListener;->mHoverMap:Ljava/util/WeakHashMap;', 'invoke-virtual {p0}, Ljava/util/WeakHashMap;->isEmpty()Z', 'return p0'],
        'type': 'method_replace',
        'search': """.method removeHover(Lmiuix/animation/controller/FolmeHover;)Z
    .registers 3

    iget-object v0, p0, Lmiuix/animation/controller/FolmeHover$InnerViewHoverListener;->mHoverMap:Ljava/util/WeakHashMap;

    invoke-virtual {v0, p1}, Ljava/util/WeakHashMap;->remove(Ljava/lang/Object;)Ljava/lang/Object;

    iget-object p0, p0, Lmiuix/animation/controller/FolmeHover$InnerViewHoverListener;->mHoverMap:Ljava/util/WeakHashMap;

    invoke-virtual {p0}, Ljava/util/WeakHashMap;->isEmpty()Z

    move-result p0

    return p0
.end method""",
        'replacement': """.method removeHover(Lmiuix/animation/controller/FolmeHover;)Z
    .registers 3

    goto :goto_3

    nop

    :goto_0
    invoke-virtual {v0, p1}, Ljava/util/WeakHashMap;->remove(Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_2

    nop

    :goto_1
    invoke-virtual {p0}, Ljava/util/WeakHashMap;->isEmpty()Z

    move-result p0

    goto :goto_4

    nop

    :goto_2
    iget-object p0, p0, Lmiuix/animation/controller/FolmeHover$InnerViewHoverListener;->mHoverMap:Ljava/util/WeakHashMap;

    goto :goto_1

    nop

    :goto_3
    iget-object v0, p0, Lmiuix/animation/controller/FolmeHover$InnerViewHoverListener;->mHoverMap:Ljava/util/WeakHashMap;

    goto :goto_0

    nop

    :goto_4
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_controller_FolmeHover__InnerViewHoverListener__addHover',
        'method': '.method varargs addHover(Lmiuix/animation/controller/FolmeHover;[Lmiuix/animation/base/AnimConfig;)V',
        'method_name': 'addHover',
        'method_anchors': ['iget-object p0, p0, Lmiuix/animation/controller/FolmeHover$InnerViewHoverListener;->mHoverMap:Ljava/util/WeakHashMap;', 'invoke-virtual {p0, p1, p2}, Ljava/util/WeakHashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;', 'return-void'],
        'type': 'method_replace',
        'search': """.method varargs addHover(Lmiuix/animation/controller/FolmeHover;[Lmiuix/animation/base/AnimConfig;)V
    .registers 3

    iget-object p0, p0, Lmiuix/animation/controller/FolmeHover$InnerViewHoverListener;->mHoverMap:Ljava/util/WeakHashMap;

    invoke-virtual {p0, p1, p2}, Ljava/util/WeakHashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    return-void
.end method""",
        'replacement': """.method varargs addHover(Lmiuix/animation/controller/FolmeHover;[Lmiuix/animation/base/AnimConfig;)V
    .registers 3

    goto :goto_2

    nop

    :goto_0
    invoke-virtual {p0, p1, p2}, Ljava/util/WeakHashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_1

    nop

    :goto_1
    return-void

    :goto_2
    iget-object p0, p0, Lmiuix/animation/controller/FolmeHover$InnerViewHoverListener;->mHoverMap:Ljava/util/WeakHashMap;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
