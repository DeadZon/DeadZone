TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/styles/TintDrawable.smali'
CLASS_FALLBACK_NAMES = ['TintDrawable.smali']
CLASS_ANCHORS = ['.super Landroid/graphics/drawable/Drawable;', '.field private static final sListener:Landroid/view/View$OnAttachStateChangeListener;']

PATCHES = [
    {
        'id': 'miuix_animation_styles_TintDrawable__initTintBuffer',
        'method': '.method declared-synchronized initTintBuffer(I)V',
        'method_name': 'initTintBuffer',
        'method_anchors': ['iget-object v0, p0, Lmiuix/animation/styles/TintDrawable;->mView:Landroid/view/View;', 'if-nez v0, :cond_0', 'return-void', 'invoke-direct {p0, p1}, Lmiuix/animation/styles/TintDrawable;->getRectRoundEnableFromView(I)V', 'iget v0, p0, Lmiuix/animation/styles/TintDrawable;->mTintStyle:I', 'if-eq v0, v1, :cond_4', 'if-eq v0, v1, :cond_5', 'iget-object v0, p0, Lmiuix/animation/styles/TintDrawable;->mView:Landroid/view/View;'],
        'type': 'method_replace',
        'search': """.method declared-synchronized initTintBuffer(I)V
    .registers 4

    monitor-enter p0

    :try_start_0
    iget-object v0, p0, Lmiuix/animation/styles/TintDrawable;->mView:Landroid/view/View;
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    if-nez v0, :cond_0

    monitor-exit p0

    return-void

    :cond_0
    :try_start_1
    invoke-direct {p0, p1}, Lmiuix/animation/styles/TintDrawable;->getRectRoundEnableFromView(I)V

    iget v0, p0, Lmiuix/animation/styles/TintDrawable;->mTintStyle:I

    const/4 v1, 0x2

    if-eq v0, v1, :cond_4

    const/4 v1, 0x4

    if-eq v0, v1, :cond_5

    iget-object v0, p0, Lmiuix/animation/styles/TintDrawable;->mView:Landroid/view/View;

    invoke-virtual {v0}, Landroid/view/View;->getWidth()I

    move-result v0

    iget-object v1, p0, Lmiuix/animation/styles/TintDrawable;->mView:Landroid/view/View;

    invoke-virtual {v1}, Landroid/view/View;->getHeight()I

    move-result v1

    if-lez v0, :cond_2

    if-gtz v1, :cond_1

    goto :goto_0

    :cond_1
    invoke-direct {p0, v0, v1}, Lmiuix/animation/styles/TintDrawable;->createBitmap(II)Z

    move-result v0

    if-eqz v0, :cond_5

    new-instance v0, Lmiuix/animation/styles/TintDrawable$InitTintTask;

    invoke-direct {v0, p0, p1}, Lmiuix/animation/styles/TintDrawable$InitTintTask;-><init>(Lmiuix/animation/styles/TintDrawable;I)V

    iput-object v0, p0, Lmiuix/animation/styles/TintDrawable;->mInitTintTask:Ljava/lang/Runnable;

    iget-object p1, p0, Lmiuix/animation/styles/TintDrawable;->mView:Landroid/view/View;

    invoke-virtual {p1, v0}, Landroid/view/View;->post(Ljava/lang/Runnable;)Z

    goto :goto_1

    :catchall_0
    move-exception p1

    goto :goto_2

    :cond_2
    :goto_0
    invoke-direct {p0}, Lmiuix/animation/styles/TintDrawable;->recycleBitmap()V

    iget-object p1, p0, Lmiuix/animation/styles/TintDrawable;->mInitTintTask:Ljava/lang/Runnable;

    if-eqz p1, :cond_3

    iget-object v0, p0, Lmiuix/animation/styles/TintDrawable;->mView:Landroid/view/View;

    invoke-virtual {v0, p1}, Landroid/view/View;->removeCallbacks(Ljava/lang/Runnable;)Z

    const/4 p1, 0x0

    iput-object p1, p0, Lmiuix/animation/styles/TintDrawable;->mInitTintTask:Ljava/lang/Runnable;
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    :cond_3
    monitor-exit p0

    return-void

    :cond_4
    :try_start_2
    invoke-direct {p0}, Lmiuix/animation/styles/TintDrawable;->tintStyleLoadData()V
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    :cond_5
    :goto_1
    monitor-exit p0

    return-void

    :goto_2
    :try_start_3
    monitor-exit p0
    :try_end_3
    .catchall {:try_start_3 .. :try_end_3} :catchall_0

    throw p1
.end method""",
        'replacement': """.method declared-synchronized initTintBuffer(I)V
    .registers 4

    goto :goto_a

    nop

    :goto_0
    monitor-exit p0

    goto :goto_5

    nop

    :goto_1
    return-void

    :cond_0
    :try_start_0
    invoke-direct {p0}, Lmiuix/animation/styles/TintDrawable;->tintStyleLoadData()V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    :cond_1
    :goto_2
    goto :goto_3

    nop

    :goto_3
    monitor-exit p0

    goto :goto_8

    nop

    :goto_4
    if-eqz v0, :cond_2

    goto :goto_6

    :cond_2
    goto :goto_0

    nop

    :goto_5
    return-void

    :goto_6
    :try_start_1
    invoke-direct {p0, p1}, Lmiuix/animation/styles/TintDrawable;->getRectRoundEnableFromView(I)V

    iget v0, p0, Lmiuix/animation/styles/TintDrawable;->mTintStyle:I

    const/4 v1, 0x2

    if-eq v0, v1, :cond_0

    const/4 v1, 0x4

    if-eq v0, v1, :cond_1

    iget-object v0, p0, Lmiuix/animation/styles/TintDrawable;->mView:Landroid/view/View;

    invoke-virtual {v0}, Landroid/view/View;->getWidth()I

    move-result v0

    iget-object v1, p0, Lmiuix/animation/styles/TintDrawable;->mView:Landroid/view/View;

    invoke-virtual {v1}, Landroid/view/View;->getHeight()I

    move-result v1

    if-lez v0, :cond_4

    if-gtz v1, :cond_3

    goto :goto_7

    :cond_3
    invoke-direct {p0, v0, v1}, Lmiuix/animation/styles/TintDrawable;->createBitmap(II)Z

    move-result v0

    if-eqz v0, :cond_1

    new-instance v0, Lmiuix/animation/styles/TintDrawable$InitTintTask;

    invoke-direct {v0, p0, p1}, Lmiuix/animation/styles/TintDrawable$InitTintTask;-><init>(Lmiuix/animation/styles/TintDrawable;I)V

    iput-object v0, p0, Lmiuix/animation/styles/TintDrawable;->mInitTintTask:Ljava/lang/Runnable;

    iget-object p1, p0, Lmiuix/animation/styles/TintDrawable;->mView:Landroid/view/View;

    invoke-virtual {p1, v0}, Landroid/view/View;->post(Ljava/lang/Runnable;)Z

    goto :goto_2

    :catchall_0
    move-exception p1

    goto :goto_9

    :cond_4
    :goto_7
    invoke-direct {p0}, Lmiuix/animation/styles/TintDrawable;->recycleBitmap()V

    iget-object p1, p0, Lmiuix/animation/styles/TintDrawable;->mInitTintTask:Ljava/lang/Runnable;

    if-eqz p1, :cond_5

    iget-object v0, p0, Lmiuix/animation/styles/TintDrawable;->mView:Landroid/view/View;

    invoke-virtual {v0, p1}, Landroid/view/View;->removeCallbacks(Ljava/lang/Runnable;)Z

    const/4 p1, 0x0

    iput-object p1, p0, Lmiuix/animation/styles/TintDrawable;->mInitTintTask:Ljava/lang/Runnable;
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    :cond_5
    goto :goto_b

    nop

    :goto_8
    return-void

    :goto_9
    :try_start_2
    monitor-exit p0
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    goto :goto_c

    nop

    :goto_a
    monitor-enter p0

    :try_start_3
    iget-object v0, p0, Lmiuix/animation/styles/TintDrawable;->mView:Landroid/view/View;
    :try_end_3
    .catchall {:try_start_3 .. :try_end_3} :catchall_0

    goto :goto_4

    nop

    :goto_b
    monitor-exit p0

    goto :goto_1

    nop

    :goto_c
    throw p1
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_styles_TintDrawable__restoreOriginalDrawable',
        'method': '.method declared-synchronized restoreOriginalDrawable()V',
        'method_name': 'restoreOriginalDrawable',
        'method_anchors': ['invoke-direct {p0}, Lmiuix/animation/styles/TintDrawable;->clear()V', 'iget-object v0, p0, Lmiuix/animation/styles/TintDrawable;->mInitTintTask:Ljava/lang/Runnable;', 'if-eqz v0, :cond_0', 'iget-object v1, p0, Lmiuix/animation/styles/TintDrawable;->mView:Landroid/view/View;', 'invoke-virtual {v1, v0}, Landroid/view/View;->removeCallbacks(Ljava/lang/Runnable;)Z', 'iput-object v0, p0, Lmiuix/animation/styles/TintDrawable;->mInitTintTask:Ljava/lang/Runnable;', 'invoke-virtual {p0}, Landroid/graphics/drawable/Drawable;->invalidateSelf()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method declared-synchronized restoreOriginalDrawable()V
    .registers 3

    monitor-enter p0

    :try_start_0
    invoke-direct {p0}, Lmiuix/animation/styles/TintDrawable;->clear()V

    iget-object v0, p0, Lmiuix/animation/styles/TintDrawable;->mInitTintTask:Ljava/lang/Runnable;

    if-eqz v0, :cond_0

    iget-object v1, p0, Lmiuix/animation/styles/TintDrawable;->mView:Landroid/view/View;

    invoke-virtual {v1, v0}, Landroid/view/View;->removeCallbacks(Ljava/lang/Runnable;)Z

    const/4 v0, 0x0

    iput-object v0, p0, Lmiuix/animation/styles/TintDrawable;->mInitTintTask:Ljava/lang/Runnable;

    goto :goto_0

    :catchall_0
    move-exception v0

    goto :goto_1

    :cond_0
    :goto_0
    invoke-virtual {p0}, Landroid/graphics/drawable/Drawable;->invalidateSelf()V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    monitor-exit p0

    return-void

    :goto_1
    :try_start_1
    monitor-exit p0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    throw v0
.end method""",
        'replacement': """.method declared-synchronized restoreOriginalDrawable()V
    .registers 3

    goto :goto_1

    nop

    :goto_0
    monitor-exit p0

    goto :goto_4

    nop

    :goto_1
    monitor-enter p0

    :try_start_0
    invoke-direct {p0}, Lmiuix/animation/styles/TintDrawable;->clear()V

    iget-object v0, p0, Lmiuix/animation/styles/TintDrawable;->mInitTintTask:Ljava/lang/Runnable;

    if-eqz v0, :cond_0

    iget-object v1, p0, Lmiuix/animation/styles/TintDrawable;->mView:Landroid/view/View;

    invoke-virtual {v1, v0}, Landroid/view/View;->removeCallbacks(Ljava/lang/Runnable;)Z

    const/4 v0, 0x0

    iput-object v0, p0, Lmiuix/animation/styles/TintDrawable;->mInitTintTask:Ljava/lang/Runnable;

    goto :goto_2

    :catchall_0
    move-exception v0

    goto :goto_5

    :cond_0
    :goto_2
    invoke-virtual {p0}, Landroid/graphics/drawable/Drawable;->invalidateSelf()V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_0

    nop

    :goto_3
    throw v0

    :goto_4
    return-void

    :goto_5
    :try_start_1
    monitor-exit p0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_styles_TintDrawable__setHoverCorner',
        'method': '.method setHoverCorner(F)V',
        'method_name': 'setHoverCorner',
        'method_anchors': ['if-eqz v0, :cond_0', 'iget v0, p0, Lmiuix/animation/styles/TintDrawable;->mTintStyle:I', 'iput v0, p0, Lmiuix/animation/styles/TintDrawable;->mTintStyle:I', 'iput p1, p0, Lmiuix/animation/styles/TintDrawable;->mHoverRadius:F', 'return-void'],
        'type': 'method_replace',
        'search': """.method setHoverCorner(F)V
    .registers 3

    const/4 v0, 0x0

    cmpl-float v0, p1, v0

    if-eqz v0, :cond_0

    const/4 v0, 0x4

    goto :goto_0

    :cond_0
    iget v0, p0, Lmiuix/animation/styles/TintDrawable;->mTintStyle:I

    :goto_0
    iput v0, p0, Lmiuix/animation/styles/TintDrawable;->mTintStyle:I

    iput p1, p0, Lmiuix/animation/styles/TintDrawable;->mHoverRadius:F

    return-void
.end method""",
        'replacement': """.method setHoverCorner(F)V
    .registers 3

    goto :goto_9

    nop

    :goto_0
    iget v0, p0, Lmiuix/animation/styles/TintDrawable;->mTintStyle:I

    :goto_1
    goto :goto_5

    nop

    :goto_2
    goto :goto_1

    :goto_3
    goto :goto_0

    nop

    :goto_4
    iput p1, p0, Lmiuix/animation/styles/TintDrawable;->mHoverRadius:F

    goto :goto_8

    nop

    :goto_5
    iput v0, p0, Lmiuix/animation/styles/TintDrawable;->mTintStyle:I

    goto :goto_4

    nop

    :goto_6
    cmpl-float v0, p1, v0

    goto :goto_a

    nop

    :goto_7
    const/4 v0, 0x4

    goto :goto_2

    nop

    :goto_8
    return-void

    :goto_9
    const/4 v0, 0x0

    goto :goto_6

    nop

    :goto_a
    if-nez v0, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_7

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
