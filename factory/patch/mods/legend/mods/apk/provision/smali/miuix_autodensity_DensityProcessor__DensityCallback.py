TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/autodensity/DensityProcessor$DensityCallback.smali'
CLASS_FALLBACK_NAMES = ['DensityProcessor$DensityCallback.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Landroid/hardware/display/DisplayManager$DisplayListener;', '.implements Landroid/content/ComponentCallbacks;']

PATCHES = [
    {
        'id': 'miuix_autodensity_DensityProcessor__DensityCallback__addOnAttachStateChangeListener',
        'method': '.method addOnAttachStateChangeListener(Landroid/view/View$OnAttachStateChangeListener;)V',
        'method_name': 'addOnAttachStateChangeListener',
        'method_anchors': ['new-instance v0, Ljava/lang/ref/WeakReference;', 'invoke-direct {v0, p1}, Ljava/lang/ref/WeakReference;-><init>(Ljava/lang/Object;)V', 'iput-object v0, p0, Lmiuix/autodensity/DensityProcessor$DensityCallback;->mDecorViewListener:Ljava/lang/ref/WeakReference;', 'return-void'],
        'type': 'method_replace',
        'search': """.method addOnAttachStateChangeListener(Landroid/view/View$OnAttachStateChangeListener;)V
    .registers 3

    new-instance v0, Ljava/lang/ref/WeakReference;

    invoke-direct {v0, p1}, Ljava/lang/ref/WeakReference;-><init>(Ljava/lang/Object;)V

    iput-object v0, p0, Lmiuix/autodensity/DensityProcessor$DensityCallback;->mDecorViewListener:Ljava/lang/ref/WeakReference;

    return-void
.end method""",
        'replacement': """.method addOnAttachStateChangeListener(Landroid/view/View$OnAttachStateChangeListener;)V
    .registers 3

    goto :goto_3

    nop

    :goto_0
    iput-object v0, p0, Lmiuix/autodensity/DensityProcessor$DensityCallback;->mDecorViewListener:Ljava/lang/ref/WeakReference;

    goto :goto_2

    nop

    :goto_1
    invoke-direct {v0, p1}, Ljava/lang/ref/WeakReference;-><init>(Ljava/lang/Object;)V

    goto :goto_0

    nop

    :goto_2
    return-void

    :goto_3
    new-instance v0, Ljava/lang/ref/WeakReference;

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_autodensity_DensityProcessor__DensityCallback__clear',
        'method': '.method clear()V',
        'method_name': 'clear',
        'method_anchors': ['iget-object v0, p0, Lmiuix/autodensity/DensityProcessor$DensityCallback;->mActivityRefs:Ljava/lang/ref/WeakReference;', 'if-eqz v0, :cond_0', 'invoke-virtual {v0}, Ljava/lang/ref/WeakReference;->clear()V', 'iget-object p0, p0, Lmiuix/autodensity/DensityProcessor$DensityCallback;->mDecorViewListener:Ljava/lang/ref/WeakReference;', 'if-eqz p0, :cond_1', 'invoke-virtual {p0}, Ljava/lang/ref/WeakReference;->clear()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method clear()V
    .registers 2

    iget-object v0, p0, Lmiuix/autodensity/DensityProcessor$DensityCallback;->mActivityRefs:Ljava/lang/ref/WeakReference;

    if-eqz v0, :cond_0

    invoke-virtual {v0}, Ljava/lang/ref/WeakReference;->clear()V

    :cond_0
    iget-object p0, p0, Lmiuix/autodensity/DensityProcessor$DensityCallback;->mDecorViewListener:Ljava/lang/ref/WeakReference;

    if-eqz p0, :cond_1

    invoke-virtual {p0}, Ljava/lang/ref/WeakReference;->clear()V

    :cond_1
    return-void
.end method""",
        'replacement': """.method clear()V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    if-nez p0, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_2

    nop

    :goto_1
    iget-object v0, p0, Lmiuix/autodensity/DensityProcessor$DensityCallback;->mActivityRefs:Ljava/lang/ref/WeakReference;

    goto :goto_4

    nop

    :goto_2
    invoke-virtual {p0}, Ljava/lang/ref/WeakReference;->clear()V

    :goto_3
    goto :goto_5

    nop

    :goto_4
    if-nez v0, :cond_1

    goto :goto_7

    :cond_1
    goto :goto_6

    nop

    :goto_5
    return-void

    :goto_6
    invoke-virtual {v0}, Ljava/lang/ref/WeakReference;->clear()V

    :goto_7
    goto :goto_8

    nop

    :goto_8
    iget-object p0, p0, Lmiuix/autodensity/DensityProcessor$DensityCallback;->mDecorViewListener:Ljava/lang/ref/WeakReference;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_autodensity_DensityProcessor__DensityCallback__removeOnAttachStateChangeListener',
        'method': '.method removeOnAttachStateChangeListener(Landroid/app/Activity;)V',
        'method_name': 'removeOnAttachStateChangeListener',
        'method_anchors': ['iget-object p0, p0, Lmiuix/autodensity/DensityProcessor$DensityCallback;->mDecorViewListener:Ljava/lang/ref/WeakReference;', 'if-eqz p0, :cond_0', 'invoke-virtual {p0}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;', 'check-cast p0, Landroid/view/View$OnAttachStateChangeListener;', 'if-eqz p0, :cond_0', 'invoke-virtual {p1}, Landroid/app/Activity;->getWindow()Landroid/view/Window;', 'invoke-virtual {p1}, Landroid/view/Window;->getDecorView()Landroid/view/View;', 'invoke-virtual {p1, p0}, Landroid/view/View;->removeOnAttachStateChangeListener(Landroid/view/View$OnAttachStateChangeListener;)V'],
        'type': 'method_replace',
        'search': """.method removeOnAttachStateChangeListener(Landroid/app/Activity;)V
    .registers 2

    iget-object p0, p0, Lmiuix/autodensity/DensityProcessor$DensityCallback;->mDecorViewListener:Ljava/lang/ref/WeakReference;

    if-eqz p0, :cond_0

    invoke-virtual {p0}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;

    move-result-object p0

    check-cast p0, Landroid/view/View$OnAttachStateChangeListener;

    if-eqz p0, :cond_0

    invoke-virtual {p1}, Landroid/app/Activity;->getWindow()Landroid/view/Window;

    move-result-object p1

    invoke-virtual {p1}, Landroid/view/Window;->getDecorView()Landroid/view/View;

    move-result-object p1

    invoke-virtual {p1, p0}, Landroid/view/View;->removeOnAttachStateChangeListener(Landroid/view/View$OnAttachStateChangeListener;)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method removeOnAttachStateChangeListener(Landroid/app/Activity;)V
    .registers 2

    goto :goto_3

    nop

    :goto_0
    if-nez p0, :cond_0

    goto :goto_9

    :cond_0
    goto :goto_1

    nop

    :goto_1
    invoke-virtual {p0}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;

    move-result-object p0

    goto :goto_4

    nop

    :goto_2
    invoke-virtual {p1}, Landroid/app/Activity;->getWindow()Landroid/view/Window;

    move-result-object p1

    goto :goto_6

    nop

    :goto_3
    iget-object p0, p0, Lmiuix/autodensity/DensityProcessor$DensityCallback;->mDecorViewListener:Ljava/lang/ref/WeakReference;

    goto :goto_0

    nop

    :goto_4
    check-cast p0, Landroid/view/View$OnAttachStateChangeListener;

    goto :goto_7

    nop

    :goto_5
    return-void

    :goto_6
    invoke-virtual {p1}, Landroid/view/Window;->getDecorView()Landroid/view/View;

    move-result-object p1

    goto :goto_8

    nop

    :goto_7
    if-nez p0, :cond_1

    goto :goto_9

    :cond_1
    goto :goto_2

    nop

    :goto_8
    invoke-virtual {p1, p0}, Landroid/view/View;->removeOnAttachStateChangeListener(Landroid/view/View$OnAttachStateChangeListener;)V

    :goto_9
    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
