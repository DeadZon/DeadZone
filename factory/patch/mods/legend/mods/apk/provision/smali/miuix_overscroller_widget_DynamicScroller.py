TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/overscroller/widget/DynamicScroller.smali'
CLASS_FALLBACK_NAMES = ['DynamicScroller.smali']
CLASS_ANCHORS = ['.super Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;', '.implements Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$FinalValueListener;']

PATCHES = [
    {
        'id': 'miuix_overscroller_widget_DynamicScroller__continueWhenFinished',
        'method': '.method continueWhenFinished()Z',
        'method_name': 'continueWhenFinished',
        'method_anchors': ['iget-object v0, p0, Lmiuix/overscroller/widget/DynamicScroller;->mHandler:Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;', 'if-eqz v0, :cond_0', 'invoke-virtual {v0}, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->continueWhenFinished()Z', 'if-eqz v0, :cond_0', 'const-string v0, "checking have more work when finish"', 'invoke-static {v0}, Lmiuix/overscroller/widget/OverScrollLogger;->debug(Ljava/lang/String;)V', 'invoke-virtual {p0}, Lmiuix/overscroller/widget/DynamicScroller;->update()Z', 'return p0'],
        'type': 'method_replace',
        'search': """.method continueWhenFinished()Z
    .registers 2

    iget-object v0, p0, Lmiuix/overscroller/widget/DynamicScroller;->mHandler:Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;

    if-eqz v0, :cond_0

    invoke-virtual {v0}, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->continueWhenFinished()Z

    move-result v0

    if-eqz v0, :cond_0

    const-string v0, "checking have more work when finish"

    invoke-static {v0}, Lmiuix/overscroller/widget/OverScrollLogger;->debug(Ljava/lang/String;)V

    invoke-virtual {p0}, Lmiuix/overscroller/widget/DynamicScroller;->update()Z

    const/4 p0, 0x1

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method continueWhenFinished()Z
    .registers 2

    goto :goto_9

    nop

    :goto_0
    return p0

    :goto_1
    if-nez v0, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_7

    nop

    :goto_2
    const/4 p0, 0x0

    goto :goto_0

    nop

    :goto_3
    if-nez v0, :cond_1

    goto :goto_5

    :cond_1
    goto :goto_8

    nop

    :goto_4
    return p0

    :goto_5
    goto :goto_2

    nop

    :goto_6
    const/4 p0, 0x1

    goto :goto_4

    nop

    :goto_7
    const-string v0, "checking have more work when finish"

    goto :goto_a

    nop

    :goto_8
    invoke-virtual {v0}, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->continueWhenFinished()Z

    move-result v0

    goto :goto_1

    nop

    :goto_9
    iget-object v0, p0, Lmiuix/overscroller/widget/DynamicScroller;->mHandler:Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;

    goto :goto_3

    nop

    :goto_a
    invoke-static {v0}, Lmiuix/overscroller/widget/OverScrollLogger;->debug(Ljava/lang/String;)V

    goto :goto_b

    nop

    :goto_b
    invoke-virtual {p0}, Lmiuix/overscroller/widget/DynamicScroller;->update()Z

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_widget_DynamicScroller__finish',
        'method': '.method finish()V',
        'method_name': 'finish',
        'method_anchors': ['const-string v0, "finish scroller"', 'invoke-static {v0}, Lmiuix/overscroller/widget/OverScrollLogger;->debug(Ljava/lang/String;)V', 'invoke-virtual {p0}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->getFinal()I', 'invoke-virtual {p0, v0}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setCurrentPosition(I)V', 'invoke-virtual {p0, v0}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setFinished(Z)V', 'invoke-direct {p0}, Lmiuix/overscroller/widget/DynamicScroller;->resetHandler()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method finish()V
    .registers 2

    const-string v0, "finish scroller"

    invoke-static {v0}, Lmiuix/overscroller/widget/OverScrollLogger;->debug(Ljava/lang/String;)V

    invoke-virtual {p0}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->getFinal()I

    move-result v0

    invoke-virtual {p0, v0}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setCurrentPosition(I)V

    const/4 v0, 0x1

    invoke-virtual {p0, v0}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setFinished(Z)V

    invoke-direct {p0}, Lmiuix/overscroller/widget/DynamicScroller;->resetHandler()V

    return-void
.end method""",
        'replacement': """.method finish()V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    const-string v0, "finish scroller"

    goto :goto_1

    nop

    :goto_1
    invoke-static {v0}, Lmiuix/overscroller/widget/OverScrollLogger;->debug(Ljava/lang/String;)V

    goto :goto_6

    nop

    :goto_2
    const/4 v0, 0x1

    goto :goto_4

    nop

    :goto_3
    invoke-direct {p0}, Lmiuix/overscroller/widget/DynamicScroller;->resetHandler()V

    goto :goto_7

    nop

    :goto_4
    invoke-virtual {p0, v0}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setFinished(Z)V

    goto :goto_3

    nop

    :goto_5
    invoke-virtual {p0, v0}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setCurrentPosition(I)V

    goto :goto_2

    nop

    :goto_6
    invoke-virtual {p0}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->getFinal()I

    move-result v0

    goto :goto_5

    nop

    :goto_7
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_widget_DynamicScroller__fling',
        'method': '.method fling(IIIII)V',
        'method_name': 'fling',
        'method_anchors': ['invoke-static {p1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;', 'invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;', 'invoke-static {p3}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;', 'invoke-static {p4}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;', 'invoke-static {p5}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;', 'const-string v1, "FLING: start(%d) velocity(%d) boundary(%d, %d) over(%d)"', 'invoke-static {v1, v0}, Lmiuix/overscroller/widget/OverScrollLogger;->debug(Ljava/lang/String;[Ljava/lang/Object;)V', 'invoke-direct {p0}, Lmiuix/overscroller/widget/DynamicScroller;->resetHandler()V'],
        'type': 'method_replace',
        'search': """.method fling(IIIII)V
    .registers 12

    invoke-static {p1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    invoke-static {p3}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v2

    invoke-static {p4}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v3

    invoke-static {p5}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v4

    filled-new-array {v0, v1, v2, v3, v4}, [Ljava/lang/Object;

    move-result-object v0

    const-string v1, "FLING: start(%d) velocity(%d) boundary(%d, %d) over(%d)"

    invoke-static {v1, v0}, Lmiuix/overscroller/widget/OverScrollLogger;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    invoke-direct {p0}, Lmiuix/overscroller/widget/DynamicScroller;->resetHandler()V

    if-nez p2, :cond_0

    invoke-virtual {p0, p1}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setCurrentPosition(I)V

    invoke-virtual {p0, p1}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setStart(I)V

    invoke-virtual {p0, p1}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setFinal(I)V

    const/4 p1, 0x0

    invoke-virtual {p0, p1}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setDuration(I)V

    const/4 p1, 0x1

    invoke-virtual {p0, p1}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setFinished(Z)V

    return-void

    :cond_0
    int-to-double v0, p2

    invoke-virtual {p0, v0, v1}, Lmiuix/overscroller/widget/DynamicScroller;->updateStiffness(D)V

    if-gt p1, p4, :cond_1

    if-ge p1, p3, :cond_2

    :cond_1
    move v5, p4

    move p4, p2

    move p2, p3

    move p3, v5

    goto :goto_0

    :cond_2
    invoke-direct/range {p0 .. p5}, Lmiuix/overscroller/widget/DynamicScroller;->doFling(IIIII)V

    return-void

    :goto_0
    invoke-direct/range {p0 .. p5}, Lmiuix/overscroller/widget/DynamicScroller;->startAfterEdge(IIIII)V

    return-void
.end method""",
        'replacement': """.method fling(IIIII)V
    .registers 12

    goto :goto_1f

    nop

    :goto_0
    if-lt p1, p3, :cond_0

    goto :goto_13

    :cond_0
    :goto_1
    goto :goto_11

    nop

    :goto_2
    filled-new-array {v0, v1, v2, v3, v4}, [Ljava/lang/Object;

    move-result-object v0

    goto :goto_21

    nop

    :goto_3
    invoke-direct/range {p0 .. p5}, Lmiuix/overscroller/widget/DynamicScroller;->startAfterEdge(IIIII)V

    goto :goto_7

    nop

    :goto_4
    return-void

    :goto_5
    goto :goto_3

    nop

    :goto_6
    invoke-direct/range {p0 .. p5}, Lmiuix/overscroller/widget/DynamicScroller;->doFling(IIIII)V

    goto :goto_4

    nop

    :goto_7
    return-void

    :goto_8
    invoke-virtual {p0, p1}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setCurrentPosition(I)V

    goto :goto_9

    nop

    :goto_9
    invoke-virtual {p0, p1}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setStart(I)V

    goto :goto_10

    nop

    :goto_a
    return-void

    :goto_b
    goto :goto_15

    nop

    :goto_c
    const/4 p1, 0x1

    goto :goto_19

    nop

    :goto_d
    invoke-static {p3}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v2

    goto :goto_1b

    nop

    :goto_e
    invoke-direct {p0}, Lmiuix/overscroller/widget/DynamicScroller;->resetHandler()V

    goto :goto_18

    nop

    :goto_f
    move p3, v5

    goto :goto_12

    nop

    :goto_10
    invoke-virtual {p0, p1}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setFinal(I)V

    goto :goto_1d

    nop

    :goto_11
    move v5, p4

    goto :goto_22

    nop

    :goto_12
    goto :goto_5

    :goto_13
    goto :goto_6

    nop

    :goto_14
    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    goto :goto_d

    nop

    :goto_15
    int-to-double v0, p2

    goto :goto_1a

    nop

    :goto_16
    if-le p1, p4, :cond_1

    goto :goto_1

    :cond_1
    goto :goto_0

    nop

    :goto_17
    invoke-static {p5}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v4

    goto :goto_2

    nop

    :goto_18
    if-eqz p2, :cond_2

    goto :goto_b

    :cond_2
    goto :goto_8

    nop

    :goto_19
    invoke-virtual {p0, p1}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setFinished(Z)V

    goto :goto_a

    nop

    :goto_1a
    invoke-virtual {p0, v0, v1}, Lmiuix/overscroller/widget/DynamicScroller;->updateStiffness(D)V

    goto :goto_16

    nop

    :goto_1b
    invoke-static {p4}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v3

    goto :goto_17

    nop

    :goto_1c
    move p2, p3

    goto :goto_f

    nop

    :goto_1d
    const/4 p1, 0x0

    goto :goto_1e

    nop

    :goto_1e
    invoke-virtual {p0, p1}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setDuration(I)V

    goto :goto_c

    nop

    :goto_1f
    invoke-static {p1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    goto :goto_14

    nop

    :goto_20
    invoke-static {v1, v0}, Lmiuix/overscroller/widget/OverScrollLogger;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    goto :goto_e

    nop

    :goto_21
    const-string v1, "FLING: start(%d) velocity(%d) boundary(%d, %d) over(%d)"

    goto :goto_20

    nop

    :goto_22
    move p4, p2

    goto :goto_1c

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_widget_DynamicScroller__notifyEdgeReached',
        'method': '.method notifyEdgeReached(III)V',
        'method_name': 'notifyEdgeReached',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->getState()I', 'if-nez v0, :cond_1', 'iget-object v0, p0, Lmiuix/overscroller/widget/DynamicScroller;->mHandler:Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;', 'if-eqz v0, :cond_0', 'invoke-direct {p0}, Lmiuix/overscroller/widget/DynamicScroller;->resetHandler()V', 'invoke-virtual {p0}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->getCurrVelocity()F', 'invoke-direct/range {v1 .. v6}, Lmiuix/overscroller/widget/DynamicScroller;->startAfterEdge(IIIII)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method notifyEdgeReached(III)V
    .registers 11

    invoke-virtual {p0}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->getState()I

    move-result v0

    if-nez v0, :cond_1

    iget-object v0, p0, Lmiuix/overscroller/widget/DynamicScroller;->mHandler:Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;

    if-eqz v0, :cond_0

    invoke-direct {p0}, Lmiuix/overscroller/widget/DynamicScroller;->resetHandler()V

    :cond_0
    invoke-virtual {p0}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->getCurrVelocity()F

    move-result v0

    float-to-int v5, v0

    move v4, p2

    move-object v1, p0

    move v2, p1

    move v3, p2

    move v6, p3

    invoke-direct/range {v1 .. v6}, Lmiuix/overscroller/widget/DynamicScroller;->startAfterEdge(IIIII)V

    :cond_1
    return-void
.end method""",
        'replacement': """.method notifyEdgeReached(III)V
    .registers 11

    goto :goto_c

    nop

    :goto_0
    invoke-virtual {p0}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->getCurrVelocity()F

    move-result v0

    goto :goto_7

    nop

    :goto_1
    return-void

    :goto_2
    move v4, p2

    goto :goto_f

    nop

    :goto_3
    move v6, p3

    goto :goto_8

    nop

    :goto_4
    if-nez v0, :cond_0

    goto :goto_b

    :cond_0
    goto :goto_a

    nop

    :goto_5
    move v2, p1

    goto :goto_d

    nop

    :goto_6
    iget-object v0, p0, Lmiuix/overscroller/widget/DynamicScroller;->mHandler:Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;

    goto :goto_4

    nop

    :goto_7
    float-to-int v5, v0

    goto :goto_2

    nop

    :goto_8
    invoke-direct/range {v1 .. v6}, Lmiuix/overscroller/widget/DynamicScroller;->startAfterEdge(IIIII)V

    :goto_9
    goto :goto_1

    nop

    :goto_a
    invoke-direct {p0}, Lmiuix/overscroller/widget/DynamicScroller;->resetHandler()V

    :goto_b
    goto :goto_0

    nop

    :goto_c
    invoke-virtual {p0}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->getState()I

    move-result v0

    goto :goto_e

    nop

    :goto_d
    move v3, p2

    goto :goto_3

    nop

    :goto_e
    if-eqz v0, :cond_1

    goto :goto_9

    :cond_1
    goto :goto_6

    nop

    :goto_f
    move-object v1, p0

    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_widget_DynamicScroller__setFinalPosition',
        'method': '.method setFinalPosition(I)V',
        'method_name': 'setFinalPosition',
        'method_anchors': ['invoke-super {p0, p1}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setFinalPosition(I)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method setFinalPosition(I)V
    .registers 2

    invoke-super {p0, p1}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setFinalPosition(I)V

    return-void
.end method""",
        'replacement': """.method setFinalPosition(I)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0, p1}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setFinalPosition(I)V

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
        'id': 'miuix_overscroller_widget_DynamicScroller__springback',
        'method': '.method springback(III)Z',
        'method_name': 'springback',
        'method_anchors': ['invoke-static {p1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;', 'invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;', 'invoke-static {p3}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;', 'const-string v3, "SPRING_BACK start(%d) boundary(%d, %d)"', 'invoke-static {v3, v1}, Lmiuix/overscroller/widget/OverScrollLogger;->debug(Ljava/lang/String;[Ljava/lang/Object;)V', 'iget-object v1, p0, Lmiuix/overscroller/widget/DynamicScroller;->mHandler:Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;', 'if-eqz v1, :cond_0', 'invoke-direct {p0}, Lmiuix/overscroller/widget/DynamicScroller;->resetHandler()V'],
        'type': 'method_replace',
        'search': """.method springback(III)Z
    .registers 11

    invoke-static {p1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v3

    invoke-static {p3}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v4

    filled-new-array {v1, v3, v4}, [Ljava/lang/Object;

    move-result-object v1

    const-string v3, "SPRING_BACK start(%d) boundary(%d, %d)"

    invoke-static {v3, v1}, Lmiuix/overscroller/widget/OverScrollLogger;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    iget-object v1, p0, Lmiuix/overscroller/widget/DynamicScroller;->mHandler:Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;

    if-eqz v1, :cond_0

    invoke-direct {p0}, Lmiuix/overscroller/widget/DynamicScroller;->resetHandler()V

    :cond_0
    const/4 v6, 0x1

    if-ge p1, p2, :cond_1

    const/4 v3, 0x0

    const/4 v5, 0x0

    const/4 v1, 0x1

    move-object v0, p0

    move v2, p1

    move v4, p2

    invoke-direct/range {v0 .. v5}, Lmiuix/overscroller/widget/DynamicScroller;->doSpring(IIFII)V

    goto :goto_0

    :cond_1
    if-le p1, p3, :cond_2

    const/4 v3, 0x0

    const/4 v5, 0x0

    const/4 v1, 0x1

    move-object v0, p0

    move v2, p1

    move v4, p3

    invoke-direct/range {v0 .. v5}, Lmiuix/overscroller/widget/DynamicScroller;->doSpring(IIFII)V

    goto :goto_0

    :cond_2
    invoke-virtual/range {p0 .. p1}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setCurrentPosition(I)V

    invoke-virtual/range {p0 .. p1}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setStart(I)V

    invoke-virtual/range {p0 .. p1}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setFinal(I)V

    const/4 v1, 0x0

    invoke-virtual {p0, v1}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setDuration(I)V

    invoke-virtual {p0, v6}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setFinished(Z)V

    :goto_0
    invoke-virtual {p0}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->isFinished()Z

    move-result v0

    xor-int/2addr v0, v6

    return v0
.end method""",
        'replacement': """.method springback(III)Z
    .registers 11

    goto :goto_3

    nop

    :goto_0
    const/4 v5, 0x0

    goto :goto_f

    nop

    :goto_1
    move-object v0, p0

    goto :goto_6

    nop

    :goto_2
    invoke-virtual/range {p0 .. p1}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setCurrentPosition(I)V

    goto :goto_16

    nop

    :goto_3
    invoke-static {p1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    goto :goto_9

    nop

    :goto_4
    xor-int/2addr v0, v6

    goto :goto_24

    nop

    :goto_5
    iget-object v1, p0, Lmiuix/overscroller/widget/DynamicScroller;->mHandler:Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;

    goto :goto_25

    nop

    :goto_6
    move v2, p1

    goto :goto_8

    nop

    :goto_7
    if-gt p1, p3, :cond_0

    goto :goto_12

    :cond_0
    goto :goto_27

    nop

    :goto_8
    move v4, p3

    goto :goto_d

    nop

    :goto_9
    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v3

    goto :goto_22

    nop

    :goto_a
    goto :goto_18

    :goto_b
    goto :goto_7

    nop

    :goto_c
    if-lt p1, p2, :cond_1

    goto :goto_b

    :cond_1
    goto :goto_10

    nop

    :goto_d
    invoke-direct/range {v0 .. v5}, Lmiuix/overscroller/widget/DynamicScroller;->doSpring(IIFII)V

    goto :goto_11

    nop

    :goto_e
    move v2, p1

    goto :goto_1a

    nop

    :goto_f
    const/4 v1, 0x1

    goto :goto_14

    nop

    :goto_10
    const/4 v3, 0x0

    goto :goto_0

    nop

    :goto_11
    goto :goto_18

    :goto_12
    goto :goto_2

    nop

    :goto_13
    filled-new-array {v1, v3, v4}, [Ljava/lang/Object;

    move-result-object v1

    goto :goto_20

    nop

    :goto_14
    move-object v0, p0

    goto :goto_e

    nop

    :goto_15
    invoke-virtual/range {p0 .. p1}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setFinal(I)V

    goto :goto_21

    nop

    :goto_16
    invoke-virtual/range {p0 .. p1}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setStart(I)V

    goto :goto_15

    nop

    :goto_17
    invoke-virtual {p0, v6}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setFinished(Z)V

    :goto_18
    goto :goto_1e

    nop

    :goto_19
    invoke-direct/range {v0 .. v5}, Lmiuix/overscroller/widget/DynamicScroller;->doSpring(IIFII)V

    goto :goto_a

    nop

    :goto_1a
    move v4, p2

    goto :goto_19

    nop

    :goto_1b
    invoke-direct {p0}, Lmiuix/overscroller/widget/DynamicScroller;->resetHandler()V

    :goto_1c
    goto :goto_23

    nop

    :goto_1d
    invoke-static {v3, v1}, Lmiuix/overscroller/widget/OverScrollLogger;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    goto :goto_5

    nop

    :goto_1e
    invoke-virtual {p0}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->isFinished()Z

    move-result v0

    goto :goto_4

    nop

    :goto_1f
    const/4 v1, 0x1

    goto :goto_1

    nop

    :goto_20
    const-string v3, "SPRING_BACK start(%d) boundary(%d, %d)"

    goto :goto_1d

    nop

    :goto_21
    const/4 v1, 0x0

    goto :goto_28

    nop

    :goto_22
    invoke-static {p3}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v4

    goto :goto_13

    nop

    :goto_23
    const/4 v6, 0x1

    goto :goto_c

    nop

    :goto_24
    return v0

    :goto_25
    if-nez v1, :cond_2

    goto :goto_1c

    :cond_2
    goto :goto_1b

    nop

    :goto_26
    const/4 v5, 0x0

    goto :goto_1f

    nop

    :goto_27
    const/4 v3, 0x0

    goto :goto_26

    nop

    :goto_28
    invoke-virtual {p0, v1}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setDuration(I)V

    goto :goto_17

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_widget_DynamicScroller__update',
        'method': '.method update()Z',
        'method_name': 'update',
        'method_anchors': ['iget-object v0, p0, Lmiuix/overscroller/widget/DynamicScroller;->mHandler:Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;', 'if-nez v0, :cond_0', 'const-string p0, "no handler found, aborting"', 'invoke-static {p0}, Lmiuix/overscroller/widget/OverScrollLogger;->debug(Ljava/lang/String;)V', 'return p0', 'invoke-virtual {v0}, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->update()Z', 'iget-object v1, p0, Lmiuix/overscroller/widget/DynamicScroller;->mHandler:Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;', 'iget v1, v1, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mValue:I'],
        'type': 'method_replace',
        'search': """.method update()Z
    .registers 5

    iget-object v0, p0, Lmiuix/overscroller/widget/DynamicScroller;->mHandler:Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;

    if-nez v0, :cond_0

    const-string p0, "no handler found, aborting"

    invoke-static {p0}, Lmiuix/overscroller/widget/OverScrollLogger;->debug(Ljava/lang/String;)V

    const/4 p0, 0x0

    return p0

    :cond_0
    invoke-virtual {v0}, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->update()Z

    move-result v0

    iget-object v1, p0, Lmiuix/overscroller/widget/DynamicScroller;->mHandler:Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;

    iget v1, v1, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mValue:I

    invoke-virtual {p0, v1}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setCurrentPosition(I)V

    iget-object v1, p0, Lmiuix/overscroller/widget/DynamicScroller;->mHandler:Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;

    iget v1, v1, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mVelocity:F

    invoke-virtual {p0, v1}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setCurrVelocity(F)V

    invoke-virtual {p0}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->getState()I

    move-result v1

    const/4 v2, 0x2

    const/4 v3, 0x1

    if-ne v1, v2, :cond_1

    iget-object v1, p0, Lmiuix/overscroller/widget/DynamicScroller;->mHandler:Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;

    iget v1, v1, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mValue:I

    int-to-float v1, v1

    invoke-static {v1}, Ljava/lang/Math;->signum(F)F

    move-result v1

    iget-object v2, p0, Lmiuix/overscroller/widget/DynamicScroller;->mHandler:Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;

    iget v2, v2, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mVelocity:F

    invoke-static {v2}, Ljava/lang/Math;->signum(F)F

    move-result v2

    mul-float/2addr v1, v2

    const/4 v2, 0x0

    cmpg-float v1, v1, v2

    if-gez v1, :cond_1

    const-string v1, "State Changed: BALLISTIC -> CUBIC"

    invoke-static {v1}, Lmiuix/overscroller/widget/OverScrollLogger;->debug(Ljava/lang/String;)V

    invoke-virtual {p0, v3}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setState(I)V

    :cond_1
    xor-int/lit8 p0, v0, 0x1

    return p0
.end method""",
        'replacement': """.method update()Z
    .registers 5

    goto :goto_0

    nop

    :goto_0
    iget-object v0, p0, Lmiuix/overscroller/widget/DynamicScroller;->mHandler:Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;

    goto :goto_f

    nop

    :goto_1
    invoke-virtual {v0}, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->update()Z

    move-result v0

    goto :goto_d

    nop

    :goto_2
    const/4 v2, 0x2

    goto :goto_c

    nop

    :goto_3
    iget v1, v1, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mValue:I

    goto :goto_6

    nop

    :goto_4
    iget-object v2, p0, Lmiuix/overscroller/widget/DynamicScroller;->mHandler:Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;

    goto :goto_20

    nop

    :goto_5
    invoke-virtual {p0}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->getState()I

    move-result v1

    goto :goto_2

    nop

    :goto_6
    invoke-virtual {p0, v1}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setCurrentPosition(I)V

    goto :goto_19

    nop

    :goto_7
    iget v1, v1, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mVelocity:F

    goto :goto_18

    nop

    :goto_8
    return p0

    :goto_9
    cmpg-float v1, v1, v2

    goto :goto_12

    nop

    :goto_a
    iget v1, v1, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mValue:I

    goto :goto_1b

    nop

    :goto_b
    const/4 p0, 0x0

    goto :goto_1c

    nop

    :goto_c
    const/4 v3, 0x1

    goto :goto_17

    nop

    :goto_d
    iget-object v1, p0, Lmiuix/overscroller/widget/DynamicScroller;->mHandler:Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;

    goto :goto_3

    nop

    :goto_e
    invoke-static {p0}, Lmiuix/overscroller/widget/OverScrollLogger;->debug(Ljava/lang/String;)V

    goto :goto_b

    nop

    :goto_f
    if-eqz v0, :cond_0

    goto :goto_1d

    :cond_0
    goto :goto_10

    nop

    :goto_10
    const-string p0, "no handler found, aborting"

    goto :goto_e

    nop

    :goto_11
    iget-object v1, p0, Lmiuix/overscroller/widget/DynamicScroller;->mHandler:Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;

    goto :goto_a

    nop

    :goto_12
    if-ltz v1, :cond_1

    goto :goto_22

    :cond_1
    goto :goto_15

    nop

    :goto_13
    mul-float/2addr v1, v2

    goto :goto_1f

    nop

    :goto_14
    invoke-static {v2}, Ljava/lang/Math;->signum(F)F

    move-result v2

    goto :goto_13

    nop

    :goto_15
    const-string v1, "State Changed: BALLISTIC -> CUBIC"

    goto :goto_1a

    nop

    :goto_16
    xor-int/lit8 p0, v0, 0x1

    goto :goto_8

    nop

    :goto_17
    if-eq v1, v2, :cond_2

    goto :goto_22

    :cond_2
    goto :goto_11

    nop

    :goto_18
    invoke-virtual {p0, v1}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setCurrVelocity(F)V

    goto :goto_5

    nop

    :goto_19
    iget-object v1, p0, Lmiuix/overscroller/widget/DynamicScroller;->mHandler:Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;

    goto :goto_7

    nop

    :goto_1a
    invoke-static {v1}, Lmiuix/overscroller/widget/OverScrollLogger;->debug(Ljava/lang/String;)V

    goto :goto_21

    nop

    :goto_1b
    int-to-float v1, v1

    goto :goto_1e

    nop

    :goto_1c
    return p0

    :goto_1d
    goto :goto_1

    nop

    :goto_1e
    invoke-static {v1}, Ljava/lang/Math;->signum(F)F

    move-result v1

    goto :goto_4

    nop

    :goto_1f
    const/4 v2, 0x0

    goto :goto_9

    nop

    :goto_20
    iget v2, v2, Lmiuix/overscroller/widget/DynamicScroller$OverScrollHandler;->mVelocity:F

    goto :goto_14

    nop

    :goto_21
    invoke-virtual {p0, v3}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setState(I)V

    :goto_22
    goto :goto_16

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
