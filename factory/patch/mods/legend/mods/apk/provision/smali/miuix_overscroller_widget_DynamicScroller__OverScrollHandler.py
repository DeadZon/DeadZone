TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/overscroller/widget/DynamicScroller$OverScrollHandler.smali'
CLASS_FALLBACK_NAMES = ['DynamicScroller$OverScrollHandler.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'miuix_overscroller_widget_DynamicScroller__OverScrollHandler__cancel',
        'method': '.method cancel()V',
        'method_name': 'cancel',
        'method_anchors': ['iput-wide v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mLastUpdateTime:J', 'iget-object v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimation:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;', 'invoke-virtual {v0}, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->cancel()V', 'iget-object v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimation:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;', 'iget-object p0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mMonitor:Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler$Monitor;', 'invoke-virtual {v0, p0}, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->removeUpdateListener(Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$OnAnimationUpdateListener;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method cancel()V
    .registers 3

    const-wide/16 v0, 0x0

    iput-wide v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mLastUpdateTime:J

    iget-object v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimation:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;

    invoke-virtual {v0}, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->cancel()V

    iget-object v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimation:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;

    iget-object p0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mMonitor:Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler$Monitor;

    invoke-virtual {v0, p0}, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->removeUpdateListener(Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$OnAnimationUpdateListener;)V

    return-void
.end method""",
        'replacement': """.method cancel()V
    .registers 3

    goto :goto_0

    nop

    :goto_0
    const-wide/16 v0, 0x0

    goto :goto_1

    nop

    :goto_1
    iput-wide v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mLastUpdateTime:J

    goto :goto_2

    nop

    :goto_2
    iget-object v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimation:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;

    goto :goto_5

    nop

    :goto_3
    iget-object p0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mMonitor:Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler$Monitor;

    goto :goto_7

    nop

    :goto_4
    return-void

    :goto_5
    invoke-virtual {v0}, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->cancel()V

    goto :goto_6

    nop

    :goto_6
    iget-object v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimation:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;

    goto :goto_3

    nop

    :goto_7
    invoke-virtual {v0, p0}, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->removeUpdateListener(Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$OnAnimationUpdateListener;)V

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_widget_DynamicScroller__OverScrollHandler__continueWhenFinished',
        'method': '.method continueWhenFinished()Z',
        'method_name': 'continueWhenFinished',
        'method_anchors': ['iget-object v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mOnFinishedListener:Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler$OnFinishedListener;', 'if-eqz v0, :cond_0', 'iget v1, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mValue:I', 'iget p0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mVelocity:F', 'invoke-interface {v0, v1, p0}, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler$OnFinishedListener;->whenFinished(FF)Z', 'return p0', 'return p0'],
        'type': 'method_replace',
        'search': """.method continueWhenFinished()Z
    .registers 3

    iget-object v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mOnFinishedListener:Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler$OnFinishedListener;

    if-eqz v0, :cond_0

    iget v1, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mValue:I

    int-to-float v1, v1

    iget p0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mVelocity:F

    invoke-interface {v0, v1, p0}, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler$OnFinishedListener;->whenFinished(FF)Z

    move-result p0

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method continueWhenFinished()Z
    .registers 3

    goto :goto_2

    nop

    :goto_0
    const/4 p0, 0x0

    goto :goto_7

    nop

    :goto_1
    int-to-float v1, v1

    goto :goto_4

    nop

    :goto_2
    iget-object v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mOnFinishedListener:Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler$OnFinishedListener;

    goto :goto_5

    nop

    :goto_3
    invoke-interface {v0, v1, p0}, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler$OnFinishedListener;->whenFinished(FF)Z

    move-result p0

    goto :goto_8

    nop

    :goto_4
    iget p0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mVelocity:F

    goto :goto_3

    nop

    :goto_5
    if-nez v0, :cond_0

    goto :goto_9

    :cond_0
    goto :goto_6

    nop

    :goto_6
    iget v1, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mValue:I

    goto :goto_1

    nop

    :goto_7
    return p0

    :goto_8
    return p0

    :goto_9
    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_widget_DynamicScroller__OverScrollHandler__getAnimation',
        'method': '.method getAnimation()Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;',
        'method_name': 'getAnimation',
        'method_anchors': ['iget-object p0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimation:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method getAnimation()Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;
    .registers 1

    iget-object p0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimation:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;

    return-object p0
.end method""",
        'replacement': """.method getAnimation()Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    iget-object p0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimation:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_widget_DynamicScroller__OverScrollHandler__getOffset',
        'method': '.method getOffset(I)I',
        'method_name': 'getOffset',
        'method_anchors': ['iget p0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mStartValue:I', 'return p1'],
        'type': 'method_replace',
        'search': """.method getOffset(I)I
    .registers 2

    iget p0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mStartValue:I

    sub-int/2addr p1, p0

    return p1
.end method""",
        'replacement': """.method getOffset(I)I
    .registers 2

    goto :goto_2

    nop

    :goto_0
    sub-int/2addr p1, p0

    goto :goto_1

    nop

    :goto_1
    return p1

    :goto_2
    iget p0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mStartValue:I

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_widget_DynamicScroller__OverScrollHandler__setMaxValue',
        'method': '.method setMaxValue(I)V',
        'method_name': 'setMaxValue',
        'method_anchors': ['iget v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mMaxLegalValue:I', 'if-le p1, v0, :cond_0', 'iget v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mStartValue:I', 'invoke-static {p1, v0}, Ljava/lang/Math;->max(II)I', 'iget-object v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimation:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;', 'invoke-virtual {v0, p1}, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->setMaxValue(F)Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;', 'iput p1, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimMaxValue:F', 'return-void'],
        'type': 'method_replace',
        'search': """.method setMaxValue(I)V
    .registers 3

    iget v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mMaxLegalValue:I

    if-le p1, v0, :cond_0

    move p1, v0

    :cond_0
    iget v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mStartValue:I

    sub-int/2addr p1, v0

    const/4 v0, 0x0

    invoke-static {p1, v0}, Ljava/lang/Math;->max(II)I

    move-result p1

    int-to-float p1, p1

    iget-object v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimation:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;

    invoke-virtual {v0, p1}, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->setMaxValue(F)Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;

    iput p1, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimMaxValue:F

    return-void
.end method""",
        'replacement': """.method setMaxValue(I)V
    .registers 3

    goto :goto_9

    nop

    :goto_0
    iget v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mStartValue:I

    goto :goto_5

    nop

    :goto_1
    iget-object v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimation:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;

    goto :goto_b

    nop

    :goto_2
    return-void

    :goto_3
    invoke-static {p1, v0}, Ljava/lang/Math;->max(II)I

    move-result p1

    goto :goto_8

    nop

    :goto_4
    if-gt p1, v0, :cond_0

    goto :goto_7

    :cond_0
    goto :goto_6

    nop

    :goto_5
    sub-int/2addr p1, v0

    goto :goto_a

    nop

    :goto_6
    move p1, v0

    :goto_7
    goto :goto_0

    nop

    :goto_8
    int-to-float p1, p1

    goto :goto_1

    nop

    :goto_9
    iget v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mMaxLegalValue:I

    goto :goto_4

    nop

    :goto_a
    const/4 v0, 0x0

    goto :goto_3

    nop

    :goto_b
    invoke-virtual {v0, p1}, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->setMaxValue(F)Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;

    goto :goto_c

    nop

    :goto_c
    iput p1, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimMaxValue:F

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_widget_DynamicScroller__OverScrollHandler__setMinValue',
        'method': '.method setMinValue(I)V',
        'method_name': 'setMinValue',
        'method_anchors': ['iget v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mMinLegalValue:I', 'if-ge p1, v0, :cond_0', 'iget v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mStartValue:I', 'invoke-static {p1, v0}, Ljava/lang/Math;->min(II)I', 'iget-object v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimation:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;', 'invoke-virtual {v0, p1}, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->setMinValue(F)Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;', 'iput p1, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimMinValue:F', 'return-void'],
        'type': 'method_replace',
        'search': """.method setMinValue(I)V
    .registers 3

    iget v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mMinLegalValue:I

    if-ge p1, v0, :cond_0

    move p1, v0

    :cond_0
    iget v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mStartValue:I

    sub-int/2addr p1, v0

    const/4 v0, 0x0

    invoke-static {p1, v0}, Ljava/lang/Math;->min(II)I

    move-result p1

    int-to-float p1, p1

    iget-object v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimation:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;

    invoke-virtual {v0, p1}, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->setMinValue(F)Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;

    iput p1, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimMinValue:F

    return-void
.end method""",
        'replacement': """.method setMinValue(I)V
    .registers 3

    goto :goto_6

    nop

    :goto_0
    iget v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mStartValue:I

    goto :goto_c

    nop

    :goto_1
    const/4 v0, 0x0

    goto :goto_4

    nop

    :goto_2
    invoke-virtual {v0, p1}, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->setMinValue(F)Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;

    goto :goto_b

    nop

    :goto_3
    return-void

    :goto_4
    invoke-static {p1, v0}, Ljava/lang/Math;->min(II)I

    move-result p1

    goto :goto_a

    nop

    :goto_5
    iget-object v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimation:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;

    goto :goto_2

    nop

    :goto_6
    iget v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mMinLegalValue:I

    goto :goto_9

    nop

    :goto_7
    move p1, v0

    :goto_8
    goto :goto_0

    nop

    :goto_9
    if-lt p1, v0, :cond_0

    goto :goto_8

    :cond_0
    goto :goto_7

    nop

    :goto_a
    int-to-float p1, p1

    goto :goto_5

    nop

    :goto_b
    iput p1, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimMinValue:F

    goto :goto_3

    nop

    :goto_c
    sub-int/2addr p1, v0

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_widget_DynamicScroller__OverScrollHandler__setOnFinishedListener',
        'method': '.method setOnFinishedListener(Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler$OnFinishedListener;)V',
        'method_name': 'setOnFinishedListener',
        'method_anchors': ['iput-object p1, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mOnFinishedListener:Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler$OnFinishedListener;', 'return-void'],
        'type': 'method_replace',
        'search': """.method setOnFinishedListener(Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler$OnFinishedListener;)V
    .registers 2

    iput-object p1, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mOnFinishedListener:Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler$OnFinishedListener;

    return-void
.end method""",
        'replacement': """.method setOnFinishedListener(Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler$OnFinishedListener;)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    iput-object p1, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mOnFinishedListener:Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler$OnFinishedListener;

    goto :goto_1

    nop

    :goto_1
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_widget_DynamicScroller__OverScrollHandler__start',
        'method': '.method start()V',
        'method_name': 'start',
        'method_anchors': ['iget-object v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimation:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;', 'iget-object v1, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mMonitor:Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler$Monitor;', 'invoke-virtual {v0, v1}, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->addUpdateListener(Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$OnAnimationUpdateListener;)Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;', 'iget-object v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimation:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;', 'invoke-virtual {v0, v1}, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->start(Z)V', 'iput-wide v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mLastUpdateTime:J', 'return-void'],
        'type': 'method_replace',
        'search': """.method start()V
    .registers 3

    iget-object v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimation:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;

    iget-object v1, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mMonitor:Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler$Monitor;

    invoke-virtual {v0, v1}, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->addUpdateListener(Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$OnAnimationUpdateListener;)Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;

    iget-object v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimation:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;

    const/4 v1, 0x1

    invoke-virtual {v0, v1}, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->start(Z)V

    const-wide/16 v0, 0x0

    iput-wide v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mLastUpdateTime:J

    return-void
.end method""",
        'replacement': """.method start()V
    .registers 3

    goto :goto_8

    nop

    :goto_0
    iget-object v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimation:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;

    goto :goto_3

    nop

    :goto_1
    return-void

    :goto_2
    iget-object v1, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mMonitor:Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler$Monitor;

    goto :goto_4

    nop

    :goto_3
    const/4 v1, 0x1

    goto :goto_7

    nop

    :goto_4
    invoke-virtual {v0, v1}, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->addUpdateListener(Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$OnAnimationUpdateListener;)Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;

    goto :goto_0

    nop

    :goto_5
    const-wide/16 v0, 0x0

    goto :goto_6

    nop

    :goto_6
    iput-wide v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mLastUpdateTime:J

    goto :goto_1

    nop

    :goto_7
    invoke-virtual {v0, v1}, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->start(Z)V

    goto :goto_5

    nop

    :goto_8
    iget-object v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimation:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_widget_DynamicScroller__OverScrollHandler__update',
        'method': '.method update()Z',
        'method_name': 'update',
        'method_anchors': ['iget-wide v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mLastUpdateTime:J', 'invoke-static {}, Lmiuix/view/animation/AnimationUtils;->currentAnimationTimeNanos()J', 'if-nez v0, :cond_0', 'const-string v0, "update done in this frame, dropping current update request"', 'invoke-static {v0}, Lmiuix/overscroller/widget/OverScrollLogger;->verbose(Ljava/lang/String;)V', 'iget-object p0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimation:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;', 'invoke-virtual {p0}, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->isRunning()Z', 'return p0'],
        'type': 'method_replace',
        'search': """.method update()Z
    .registers 7

    iget-wide v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mLastUpdateTime:J

    invoke-static {}, Lmiuix/view/animation/AnimationUtils;->currentAnimationTimeNanos()J

    move-result-wide v2

    cmp-long v0, v2, v0

    if-nez v0, :cond_0

    const-string v0, "update done in this frame, dropping current update request"

    invoke-static {v0}, Lmiuix/overscroller/widget/OverScrollLogger;->verbose(Ljava/lang/String;)V

    iget-object p0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimation:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;

    invoke-virtual {p0}, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->isRunning()Z

    move-result p0

    xor-int/lit8 p0, p0, 0x1

    return p0

    :cond_0
    iget-object v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimation:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;

    invoke-virtual {v0, v2, v3}, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->doAnimationFrame(J)Z

    move-result v0

    if-eqz v0, :cond_1

    iget-object v1, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimation:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;

    invoke-virtual {v1}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object v1

    iget v4, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mValue:I

    invoke-static {v4}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v4

    iget v5, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mVelocity:F

    invoke-static {v5}, Ljava/lang/Float;->valueOf(F)Ljava/lang/Float;

    move-result-object v5

    filled-new-array {v1, v4, v5}, [Ljava/lang/Object;

    move-result-object v1

    const-string v4, "%s finishing value(%d) velocity(%f)"

    invoke-static {v4, v1}, Lmiuix/overscroller/widget/OverScrollLogger;->verbose(Ljava/lang/String;[Ljava/lang/Object;)V

    iget-object v1, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimation:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;

    iget-object v4, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mMonitor:Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler$Monitor;

    invoke-virtual {v1, v4}, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->removeUpdateListener(Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$OnAnimationUpdateListener;)V

    :cond_1
    iput-wide v2, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mLastUpdateTime:J

    return v0
.end method""",
        'replacement': """.method update()Z
    .registers 7

    goto :goto_12

    nop

    :goto_0
    invoke-virtual {v1, v4}, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->removeUpdateListener(Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$OnAnimationUpdateListener;)V

    :goto_1
    goto :goto_13

    nop

    :goto_2
    filled-new-array {v1, v4, v5}, [Ljava/lang/Object;

    move-result-object v1

    goto :goto_1a

    nop

    :goto_3
    iget-object p0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimation:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;

    goto :goto_b

    nop

    :goto_4
    invoke-static {v5}, Ljava/lang/Float;->valueOf(F)Ljava/lang/Float;

    move-result-object v5

    goto :goto_2

    nop

    :goto_5
    iget-object v1, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimation:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;

    goto :goto_c

    nop

    :goto_6
    iget-object v1, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimation:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;

    goto :goto_d

    nop

    :goto_7
    if-eqz v0, :cond_0

    goto :goto_1c

    :cond_0
    goto :goto_14

    nop

    :goto_8
    invoke-virtual {v1}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object v1

    goto :goto_e

    nop

    :goto_9
    invoke-virtual {v0, v2, v3}, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->doAnimationFrame(J)Z

    move-result v0

    goto :goto_f

    nop

    :goto_a
    invoke-static {v4}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v4

    goto :goto_10

    nop

    :goto_b
    invoke-virtual {p0}, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->isRunning()Z

    move-result p0

    goto :goto_1d

    nop

    :goto_c
    invoke-virtual {v1}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object v1

    goto :goto_8

    nop

    :goto_d
    iget-object v4, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mMonitor:Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler$Monitor;

    goto :goto_0

    nop

    :goto_e
    iget v4, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mValue:I

    goto :goto_a

    nop

    :goto_f
    if-nez v0, :cond_1

    goto :goto_1

    :cond_1
    goto :goto_5

    nop

    :goto_10
    iget v5, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mVelocity:F

    goto :goto_4

    nop

    :goto_11
    cmp-long v0, v2, v0

    goto :goto_7

    nop

    :goto_12
    iget-wide v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mLastUpdateTime:J

    goto :goto_16

    nop

    :goto_13
    iput-wide v2, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mLastUpdateTime:J

    goto :goto_15

    nop

    :goto_14
    const-string v0, "update done in this frame, dropping current update request"

    goto :goto_17

    nop

    :goto_15
    return v0

    :goto_16
    invoke-static {}, Lmiuix/view/animation/AnimationUtils;->currentAnimationTimeNanos()J

    move-result-wide v2

    goto :goto_11

    nop

    :goto_17
    invoke-static {v0}, Lmiuix/overscroller/widget/OverScrollLogger;->verbose(Ljava/lang/String;)V

    goto :goto_3

    nop

    :goto_18
    iget-object v0, p0, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mAnimation:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;

    goto :goto_9

    nop

    :goto_19
    invoke-static {v4, v1}, Lmiuix/overscroller/widget/OverScrollLogger;->verbose(Ljava/lang/String;[Ljava/lang/Object;)V

    goto :goto_6

    nop

    :goto_1a
    const-string v4, "%s finishing value(%d) velocity(%f)"

    goto :goto_19

    nop

    :goto_1b
    return p0

    :goto_1c
    goto :goto_18

    nop

    :goto_1d
    xor-int/lit8 p0, p0, 0x1

    goto :goto_1b

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
