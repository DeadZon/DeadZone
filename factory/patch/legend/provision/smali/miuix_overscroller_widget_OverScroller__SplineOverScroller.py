TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/overscroller/widget/OverScroller$SplineOverScroller.smali'
CLASS_FALLBACK_NAMES = ['OverScroller$SplineOverScroller.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field private static final SPLINE_POSITION:[F', '.field private static final SPLINE_TIME:[F']

PATCHES = [
    {
        'id': 'miuix_overscroller_widget_OverScroller__SplineOverScroller__computeScrollOffset',
        'method': '.method computeScrollOffset()Z',
        'method_name': 'computeScrollOffset',
        'method_anchors': ['iget-object v1, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSpringOperator:Lmiuix/animation/physics/SpringOperator;', 'if-eqz v1, :cond_4', 'iget-boolean v1, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinished:Z', 'if-eqz v1, :cond_0', 'iget-boolean v1, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mLastStep:Z', 'if-eqz v1, :cond_1', 'iput-boolean v3, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinished:Z', 'iget-wide v1, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D'],
        'type': 'method_replace',
        'search': """.method computeScrollOffset()Z
    .registers 21

    move-object/from16 v0, p0

    iget-object v1, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSpringOperator:Lmiuix/animation/physics/SpringOperator;

    const/4 v2, 0x0

    if-eqz v1, :cond_4

    iget-boolean v1, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinished:Z

    if-eqz v1, :cond_0

    goto :goto_2

    :cond_0
    iget-boolean v1, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mLastStep:Z

    const/4 v3, 0x1

    if-eqz v1, :cond_1

    iput-boolean v3, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinished:Z

    iget-wide v1, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    iput-wide v1, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D

    return v3

    :cond_1
    invoke-static {}, Lmiuix/view/animation/AnimationUtils;->currentAnimationTimeNanos()J

    move-result-wide v4

    iget-wide v6, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStartTime:J

    sub-long v6, v4, v6

    long-to-double v6, v6

    const-wide v8, 0x41cdcd6500000000L

    div-double/2addr v6, v8

    const-wide v8, 0x3f90624de0000000L

    invoke-static {v6, v7, v8, v9}, Ljava/lang/Math;->min(DD)D

    move-result-wide v6

    const-wide/16 v10, 0x0

    cmpl-double v1, v6, v10

    if-nez v1, :cond_2

    move-wide/from16 v17, v8

    goto :goto_0

    :cond_2
    move-wide/from16 v17, v6

    :goto_0
    iput-wide v4, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStartTime:J

    iget-object v10, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSpringAnimData:Lmiuix/animation/internal/AnimData;

    iget-wide v4, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D

    iput-wide v4, v10, Lmiuix/animation/internal/AnimData;->startValue:D

    iget-wide v4, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    iput-wide v4, v10, Lmiuix/animation/internal/AnimData;->targetValue:D

    iget-wide v4, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D

    iput-wide v4, v10, Lmiuix/animation/internal/AnimData;->value:D

    iget-object v1, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSpringFactor:[D

    aget-wide v11, v1, v2

    iget-object v1, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSpringParams:[D

    aget-wide v13, v1, v3

    const/4 v2, 0x2

    aget-wide v15, v1, v2

    const/16 v19, 0x0

    invoke-static/range {v10 .. v19}, Lmiuix/animation/physics/SpringOperator;->updateValues(Lmiuix/animation/internal/AnimData;DDDDZ)V

    iget-object v1, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSpringAnimData:Lmiuix/animation/internal/AnimData;

    iget-wide v4, v1, Lmiuix/animation/internal/AnimData;->value:D

    iput-wide v4, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D

    iget-wide v1, v1, Lmiuix/animation/internal/AnimData;->velocity:D

    iput-wide v1, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrVelocity:D

    iget-wide v1, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    invoke-virtual {v0, v4, v5, v1, v2}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->isAtEquilibrium(DD)Z

    move-result v1

    if-eqz v1, :cond_3

    iput-boolean v3, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mLastStep:Z

    goto :goto_1

    :cond_3
    iget-wide v1, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D

    iput-wide v1, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D

    :goto_1
    return v3

    :cond_4
    :goto_2
    return v2
.end method""",
        'replacement': """.method computeScrollOffset()Z
    .registers 21

    goto :goto_4

    nop

    :goto_0
    iput-wide v1, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D

    :goto_1
    goto :goto_c

    nop

    :goto_2
    iput-wide v4, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D

    goto :goto_23

    nop

    :goto_3
    const-wide v8, 0x3f90624de0000000L

    goto :goto_39

    nop

    :goto_4
    move-object/from16 v0, p0

    goto :goto_34

    nop

    :goto_5
    iget-wide v4, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D

    goto :goto_2b

    nop

    :goto_6
    iget-boolean v1, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinished:Z

    goto :goto_a

    nop

    :goto_7
    move-wide/from16 v17, v8

    goto :goto_20

    nop

    :goto_8
    const/16 v19, 0x0

    goto :goto_1f

    nop

    :goto_9
    iget-object v10, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSpringAnimData:Lmiuix/animation/internal/AnimData;

    goto :goto_5

    nop

    :goto_a
    if-nez v1, :cond_0

    goto :goto_10

    :cond_0
    goto :goto_f

    nop

    :goto_b
    long-to-double v6, v6

    goto :goto_22

    nop

    :goto_c
    return v3

    :goto_d
    goto :goto_1d

    nop

    :goto_e
    if-nez v1, :cond_1

    goto :goto_d

    :cond_1
    goto :goto_6

    nop

    :goto_f
    goto :goto_d

    :goto_10
    goto :goto_16

    nop

    :goto_11
    iget-wide v4, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    goto :goto_1e

    nop

    :goto_12
    iput-wide v4, v10, Lmiuix/animation/internal/AnimData;->value:D

    goto :goto_33

    nop

    :goto_13
    iget-wide v1, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    goto :goto_2a

    nop

    :goto_14
    invoke-static {}, Lmiuix/view/animation/AnimationUtils;->currentAnimationTimeNanos()J

    move-result-wide v4

    goto :goto_2f

    nop

    :goto_15
    const-wide/16 v10, 0x0

    goto :goto_17

    nop

    :goto_16
    iget-boolean v1, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mLastStep:Z

    goto :goto_19

    nop

    :goto_17
    cmpl-double v1, v6, v10

    goto :goto_18

    nop

    :goto_18
    if-eqz v1, :cond_2

    goto :goto_21

    :cond_2
    goto :goto_7

    nop

    :goto_19
    const/4 v3, 0x1

    goto :goto_25

    nop

    :goto_1a
    aget-wide v13, v1, v3

    goto :goto_1c

    nop

    :goto_1b
    aget-wide v11, v1, v2

    goto :goto_26

    nop

    :goto_1c
    const/4 v2, 0x2

    goto :goto_3d

    nop

    :goto_1d
    return v2

    :goto_1e
    iput-wide v4, v10, Lmiuix/animation/internal/AnimData;->targetValue:D

    goto :goto_27

    nop

    :goto_1f
    invoke-static/range {v10 .. v19}, Lmiuix/animation/physics/SpringOperator;->updateValues(Lmiuix/animation/internal/AnimData;DDDDZ)V

    goto :goto_29

    nop

    :goto_20
    goto :goto_2d

    :goto_21
    goto :goto_2c

    nop

    :goto_22
    const-wide v8, 0x41cdcd6500000000L

    goto :goto_3f

    nop

    :goto_23
    iget-wide v1, v1, Lmiuix/animation/internal/AnimData;->velocity:D

    goto :goto_38

    nop

    :goto_24
    const/4 v2, 0x0

    goto :goto_e

    nop

    :goto_25
    if-nez v1, :cond_3

    goto :goto_32

    :cond_3
    goto :goto_37

    nop

    :goto_26
    iget-object v1, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSpringParams:[D

    goto :goto_1a

    nop

    :goto_27
    iget-wide v4, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D

    goto :goto_12

    nop

    :goto_28
    iget-wide v4, v1, Lmiuix/animation/internal/AnimData;->value:D

    goto :goto_2

    nop

    :goto_29
    iget-object v1, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSpringAnimData:Lmiuix/animation/internal/AnimData;

    goto :goto_28

    nop

    :goto_2a
    iput-wide v1, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D

    goto :goto_31

    nop

    :goto_2b
    iput-wide v4, v10, Lmiuix/animation/internal/AnimData;->startValue:D

    goto :goto_11

    nop

    :goto_2c
    move-wide/from16 v17, v6

    :goto_2d
    goto :goto_36

    nop

    :goto_2e
    sub-long v6, v4, v6

    goto :goto_b

    nop

    :goto_2f
    iget-wide v6, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStartTime:J

    goto :goto_2e

    nop

    :goto_30
    iget-wide v1, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    goto :goto_3a

    nop

    :goto_31
    return v3

    :goto_32
    goto :goto_14

    nop

    :goto_33
    iget-object v1, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSpringFactor:[D

    goto :goto_1b

    nop

    :goto_34
    iget-object v1, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSpringOperator:Lmiuix/animation/physics/SpringOperator;

    goto :goto_24

    nop

    :goto_35
    iget-wide v1, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D

    goto :goto_0

    nop

    :goto_36
    iput-wide v4, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStartTime:J

    goto :goto_9

    nop

    :goto_37
    iput-boolean v3, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinished:Z

    goto :goto_13

    nop

    :goto_38
    iput-wide v1, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrVelocity:D

    goto :goto_30

    nop

    :goto_39
    invoke-static {v6, v7, v8, v9}, Ljava/lang/Math;->min(DD)D

    move-result-wide v6

    goto :goto_15

    nop

    :goto_3a
    invoke-virtual {v0, v4, v5, v1, v2}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->isAtEquilibrium(DD)Z

    move-result v1

    goto :goto_3e

    nop

    :goto_3b
    goto :goto_1

    :goto_3c
    goto :goto_35

    nop

    :goto_3d
    aget-wide v15, v1, v2

    goto :goto_8

    nop

    :goto_3e
    if-nez v1, :cond_4

    goto :goto_3c

    :cond_4
    goto :goto_40

    nop

    :goto_3f
    div-double/2addr v6, v8

    goto :goto_3

    nop

    :goto_40
    iput-boolean v3, v0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mLastStep:Z

    goto :goto_3b

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_widget_OverScroller__SplineOverScroller__continueWhenFinished',
        'method': '.method continueWhenFinished()Z',
        'method_name': 'continueWhenFinished',
        'method_anchors': ['iget v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mState:I', 'if-eqz v0, :cond_2', 'if-eq v0, v3, :cond_1', 'if-eq v0, v5, :cond_0', 'iget-wide v5, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStartTime:J', 'iget v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mDuration:I', 'iput-wide v5, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStartTime:J', 'iget-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D'],
        'type': 'method_replace',
        'search': """.method continueWhenFinished()Z
    .registers 10

    iget v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mState:I

    const-wide/32 v1, 0xf4240

    const/4 v3, 0x1

    const/4 v4, 0x0

    if-eqz v0, :cond_2

    if-eq v0, v3, :cond_1

    const/4 v5, 0x2

    if-eq v0, v5, :cond_0

    goto :goto_0

    :cond_0
    iget-wide v5, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStartTime:J

    iget v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mDuration:I

    int-to-long v7, v0

    mul-long/2addr v7, v1

    add-long/2addr v5, v7

    iput-wide v5, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStartTime:J

    iget-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    double-to-int v0, v0

    iget-wide v1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D

    double-to-int v1, v1

    invoke-direct {p0, v0, v1, v4}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->startSpringback(III)V

    goto :goto_0

    :cond_1
    return v4

    :cond_2
    iget v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mDuration:I

    iget v5, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSplineDuration:I

    if-ge v0, v5, :cond_3

    iget-wide v4, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    iput-wide v4, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D

    iput-wide v4, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D

    iget-wide v4, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrVelocity:D

    double-to-int v0, v4

    int-to-double v4, v0

    iput-wide v4, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mVelocity:D

    double-to-int v0, v4

    invoke-static {v0}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->getDeceleration(I)F

    move-result v0

    iput v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mDeceleration:F

    iget-wide v4, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStartTime:J

    iget v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mDuration:I

    int-to-long v6, v0

    mul-long/2addr v6, v1

    add-long/2addr v4, v6

    iput-wide v4, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStartTime:J

    invoke-direct {p0}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->onEdgeReached()V

    :goto_0
    invoke-virtual {p0}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->update()Z

    return v3

    :cond_3
    return v4
.end method""",
        'replacement': """.method continueWhenFinished()Z
    .registers 10

    goto :goto_2b

    nop

    :goto_0
    mul-long/2addr v7, v1

    goto :goto_24

    nop

    :goto_1
    return v4

    :goto_2
    invoke-virtual {p0}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->update()Z

    goto :goto_3

    nop

    :goto_3
    return v3

    :goto_4
    goto :goto_1

    nop

    :goto_5
    if-ne v0, v3, :cond_0

    goto :goto_19

    :cond_0
    goto :goto_1a

    nop

    :goto_6
    double-to-int v1, v1

    goto :goto_f

    nop

    :goto_7
    const/4 v3, 0x1

    goto :goto_15

    nop

    :goto_8
    int-to-long v6, v0

    goto :goto_11

    nop

    :goto_9
    return v4

    :goto_a
    goto :goto_2d

    nop

    :goto_b
    double-to-int v0, v4

    goto :goto_1b

    nop

    :goto_c
    if-ne v0, v5, :cond_1

    goto :goto_31

    :cond_1
    goto :goto_30

    nop

    :goto_d
    iget-wide v1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D

    goto :goto_6

    nop

    :goto_e
    int-to-long v7, v0

    goto :goto_0

    nop

    :goto_f
    invoke-direct {p0, v0, v1, v4}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->startSpringback(III)V

    goto :goto_18

    nop

    :goto_10
    iget-wide v4, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrVelocity:D

    goto :goto_1d

    nop

    :goto_11
    mul-long/2addr v6, v1

    goto :goto_2e

    nop

    :goto_12
    iput-wide v4, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mVelocity:D

    goto :goto_b

    nop

    :goto_13
    iget-wide v4, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    goto :goto_1f

    nop

    :goto_14
    iget-wide v4, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStartTime:J

    goto :goto_20

    nop

    :goto_15
    const/4 v4, 0x0

    goto :goto_26

    nop

    :goto_16
    if-lt v0, v5, :cond_2

    goto :goto_4

    :cond_2
    goto :goto_13

    nop

    :goto_17
    const-wide/32 v1, 0xf4240

    goto :goto_7

    nop

    :goto_18
    goto :goto_23

    :goto_19
    goto :goto_9

    nop

    :goto_1a
    const/4 v5, 0x2

    goto :goto_c

    nop

    :goto_1b
    invoke-static {v0}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->getDeceleration(I)F

    move-result v0

    goto :goto_1c

    nop

    :goto_1c
    iput v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mDeceleration:F

    goto :goto_14

    nop

    :goto_1d
    double-to-int v0, v4

    goto :goto_25

    nop

    :goto_1e
    iget-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    goto :goto_2c

    nop

    :goto_1f
    iput-wide v4, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D

    goto :goto_29

    nop

    :goto_20
    iget v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mDuration:I

    goto :goto_8

    nop

    :goto_21
    iget v5, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSplineDuration:I

    goto :goto_16

    nop

    :goto_22
    invoke-direct {p0}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->onEdgeReached()V

    :goto_23
    goto :goto_2

    nop

    :goto_24
    add-long/2addr v5, v7

    goto :goto_28

    nop

    :goto_25
    int-to-double v4, v0

    goto :goto_12

    nop

    :goto_26
    if-nez v0, :cond_3

    goto :goto_a

    :cond_3
    goto :goto_5

    nop

    :goto_27
    iget-wide v5, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStartTime:J

    goto :goto_2a

    nop

    :goto_28
    iput-wide v5, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStartTime:J

    goto :goto_1e

    nop

    :goto_29
    iput-wide v4, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D

    goto :goto_10

    nop

    :goto_2a
    iget v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mDuration:I

    goto :goto_e

    nop

    :goto_2b
    iget v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mState:I

    goto :goto_17

    nop

    :goto_2c
    double-to-int v0, v0

    goto :goto_d

    nop

    :goto_2d
    iget v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mDuration:I

    goto :goto_21

    nop

    :goto_2e
    add-long/2addr v4, v6

    goto :goto_2f

    nop

    :goto_2f
    iput-wide v4, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStartTime:J

    goto :goto_22

    nop

    :goto_30
    goto :goto_23

    :goto_31
    goto :goto_27

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_widget_OverScroller__SplineOverScroller__getCurrVelocity',
        'method': '.method final getCurrVelocity()F',
        'method_name': 'getCurrVelocity',
        'method_anchors': ['iget-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrVelocity:D', 'return p0'],
        'type': 'method_replace',
        'search': """.method final getCurrVelocity()F
    .registers 3

    iget-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrVelocity:D

    double-to-float p0, v0

    return p0
.end method""",
        'replacement': """.method final getCurrVelocity()F
    .registers 3

    goto :goto_0

    nop

    :goto_0
    iget-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrVelocity:D

    goto :goto_1

    nop

    :goto_1
    double-to-float p0, v0

    goto :goto_2

    nop

    :goto_2
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_widget_OverScroller__SplineOverScroller__getCurrentPosition',
        'method': '.method final getCurrentPosition()I',
        'method_name': 'getCurrentPosition',
        'method_anchors': ['iget-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D', 'return p0'],
        'type': 'method_replace',
        'search': """.method final getCurrentPosition()I
    .registers 3

    iget-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D

    double-to-int p0, v0

    return p0
.end method""",
        'replacement': """.method final getCurrentPosition()I
    .registers 3

    goto :goto_0

    nop

    :goto_0
    iget-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D

    goto :goto_2

    nop

    :goto_1
    return p0

    :goto_2
    double-to-int p0, v0

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_widget_OverScroller__SplineOverScroller__getFinal',
        'method': '.method final getFinal()I',
        'method_name': 'getFinal',
        'method_anchors': ['iget-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D', 'return p0'],
        'type': 'method_replace',
        'search': """.method final getFinal()I
    .registers 3

    iget-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    double-to-int p0, v0

    return p0
.end method""",
        'replacement': """.method final getFinal()I
    .registers 3

    goto :goto_0

    nop

    :goto_0
    iget-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    goto :goto_2

    nop

    :goto_1
    return p0

    :goto_2
    double-to-int p0, v0

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_widget_OverScroller__SplineOverScroller__getStart',
        'method': '.method final getStart()I',
        'method_name': 'getStart',
        'method_anchors': ['iget-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D', 'return p0'],
        'type': 'method_replace',
        'search': """.method final getStart()I
    .registers 3

    iget-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D

    double-to-int p0, v0

    return p0
.end method""",
        'replacement': """.method final getStart()I
    .registers 3

    goto :goto_0

    nop

    :goto_0
    iget-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D

    goto :goto_2

    nop

    :goto_1
    return p0

    :goto_2
    double-to-int p0, v0

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_widget_OverScroller__SplineOverScroller__getState',
        'method': '.method final getState()I',
        'method_name': 'getState',
        'method_anchors': ['iget p0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mState:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method final getState()I
    .registers 1

    iget p0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mState:I

    return p0
.end method""",
        'replacement': """.method final getState()I
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget p0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mState:I

    goto :goto_1

    nop

    :goto_1
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_widget_OverScroller__SplineOverScroller__isFinished',
        'method': '.method final isFinished()Z',
        'method_name': 'isFinished',
        'method_anchors': ['iget-boolean p0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinished:Z', 'return p0'],
        'type': 'method_replace',
        'search': """.method final isFinished()Z
    .registers 1

    iget-boolean p0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinished:Z

    return p0
.end method""",
        'replacement': """.method final isFinished()Z
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget-boolean p0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinished:Z

    goto :goto_1

    nop

    :goto_1
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_widget_OverScroller__SplineOverScroller__setCurrVelocity',
        'method': '.method final setCurrVelocity(F)V',
        'method_name': 'setCurrVelocity',
        'method_anchors': ['iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrVelocity:D', 'return-void'],
        'type': 'method_replace',
        'search': """.method final setCurrVelocity(F)V
    .registers 4

    float-to-double v0, p1

    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrVelocity:D

    return-void
.end method""",
        'replacement': """.method final setCurrVelocity(F)V
    .registers 4

    goto :goto_0

    nop

    :goto_0
    float-to-double v0, p1

    goto :goto_1

    nop

    :goto_1
    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrVelocity:D

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
        'id': 'miuix_overscroller_widget_OverScroller__SplineOverScroller__setCurrentPosition',
        'method': '.method final setCurrentPosition(I)V',
        'method_name': 'setCurrentPosition',
        'method_anchors': ['iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D', 'return-void'],
        'type': 'method_replace',
        'search': """.method final setCurrentPosition(I)V
    .registers 4

    int-to-double v0, p1

    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D

    return-void
.end method""",
        'replacement': """.method final setCurrentPosition(I)V
    .registers 4

    goto :goto_2

    nop

    :goto_0
    return-void

    :goto_1
    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D

    goto :goto_0

    nop

    :goto_2
    int-to-double v0, p1

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_widget_OverScroller__SplineOverScroller__setDuration',
        'method': '.method final setDuration(I)V',
        'method_name': 'setDuration',
        'method_anchors': ['iput p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mDuration:I', 'return-void'],
        'type': 'method_replace',
        'search': """.method final setDuration(I)V
    .registers 2

    iput p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mDuration:I

    return-void
.end method""",
        'replacement': """.method final setDuration(I)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    iput p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mDuration:I

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_widget_OverScroller__SplineOverScroller__setFinal',
        'method': '.method final setFinal(I)V',
        'method_name': 'setFinal',
        'method_anchors': ['iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D', 'return-void'],
        'type': 'method_replace',
        'search': """.method final setFinal(I)V
    .registers 4

    int-to-double v0, p1

    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    return-void
.end method""",
        'replacement': """.method final setFinal(I)V
    .registers 4

    goto :goto_2

    nop

    :goto_0
    return-void

    :goto_1
    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    goto :goto_0

    nop

    :goto_2
    int-to-double v0, p1

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_widget_OverScroller__SplineOverScroller__setFinished',
        'method': '.method final setFinished(Z)V',
        'method_name': 'setFinished',
        'method_anchors': ['iput-boolean p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinished:Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method final setFinished(Z)V
    .registers 2

    iput-boolean p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinished:Z

    return-void
.end method""",
        'replacement': """.method final setFinished(Z)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    iput-boolean p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinished:Z

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
        'id': 'miuix_overscroller_widget_OverScroller__SplineOverScroller__setStart',
        'method': '.method final setStart(I)V',
        'method_name': 'setStart',
        'method_anchors': ['iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D', 'return-void'],
        'type': 'method_replace',
        'search': """.method final setStart(I)V
    .registers 4

    int-to-double v0, p1

    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D

    return-void
.end method""",
        'replacement': """.method final setStart(I)V
    .registers 4

    goto :goto_0

    nop

    :goto_0
    int-to-double v0, p1

    goto :goto_1

    nop

    :goto_1
    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D

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
        'id': 'miuix_overscroller_widget_OverScroller__SplineOverScroller__setStartTime',
        'method': '.method final setStartTime(J)V',
        'method_name': 'setStartTime',
        'method_anchors': ['iput-wide p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStartTime:J', 'return-void'],
        'type': 'method_replace',
        'search': """.method final setStartTime(J)V
    .registers 3

    iput-wide p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStartTime:J

    return-void
.end method""",
        'replacement': """.method final setStartTime(J)V
    .registers 3

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    iput-wide p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStartTime:J

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_widget_OverScroller__SplineOverScroller__setState',
        'method': '.method final setState(I)V',
        'method_name': 'setState',
        'method_anchors': ['iput p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mState:I', 'return-void'],
        'type': 'method_replace',
        'search': """.method final setState(I)V
    .registers 2

    iput p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mState:I

    return-void
.end method""",
        'replacement': """.method final setState(I)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    iput p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mState:I

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
        'id': 'miuix_overscroller_widget_OverScroller__SplineOverScroller__finish',
        'method': '.method finish()V',
        'method_name': 'finish',
        'method_anchors': ['iget-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D', 'iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D', 'iput-boolean v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinished:Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method finish()V
    .registers 3

    iget-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D

    const/4 v0, 0x1

    iput-boolean v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinished:Z

    return-void
.end method""",
        'replacement': """.method finish()V
    .registers 3

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    iget-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    goto :goto_4

    nop

    :goto_2
    const/4 v0, 0x1

    goto :goto_3

    nop

    :goto_3
    iput-boolean v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinished:Z

    goto :goto_0

    nop

    :goto_4
    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_widget_OverScroller__SplineOverScroller__fling',
        'method': '.method fling(IIIII)V',
        'method_name': 'fling',
        'method_anchors': ['iput p5, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mOver:I', 'iput-boolean p5, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinished:Z', 'iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mVelocity:D', 'iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrVelocity:D', 'iput p5, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSplineDuration:I', 'iput p5, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mDuration:I', 'invoke-static {}, Lmiuix/view/animation/AnimationUtils;->currentAnimationTimeNanos()J', 'iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStartTime:J'],
        'type': 'method_replace',
        'search': """.method fling(IIIII)V
    .registers 10

    iput p5, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mOver:I

    const/4 p5, 0x0

    iput-boolean p5, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinished:Z

    int-to-double v0, p2

    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mVelocity:D

    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrVelocity:D

    iput p5, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSplineDuration:I

    iput p5, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mDuration:I

    invoke-static {}, Lmiuix/view/animation/AnimationUtils;->currentAnimationTimeNanos()J

    move-result-wide v0

    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStartTime:J

    int-to-double v0, p1

    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D

    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D

    if-gt p1, p4, :cond_4

    if-ge p1, p3, :cond_0

    goto :goto_1

    :cond_0
    iput p5, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mState:I

    if-eqz p2, :cond_1

    invoke-direct {p0, p2}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->getSplineFlingDuration(I)I

    move-result p5

    iput p5, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSplineDuration:I

    iput p5, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mDuration:I

    invoke-direct {p0, p2}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->getSplineFlingDistance(I)D

    move-result-wide v0

    goto :goto_0

    :cond_1
    const-wide/16 v0, 0x0

    :goto_0
    int-to-float p2, p2

    invoke-static {p2}, Ljava/lang/Math;->signum(F)F

    move-result p2

    float-to-double v2, p2

    mul-double/2addr v0, v2

    double-to-int p2, v0

    iput p2, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSplineDistance:I

    add-int/2addr p1, p2

    int-to-double p1, p1

    iput-wide p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    int-to-double v0, p3

    cmpg-double p5, p1, v0

    if-gez p5, :cond_2

    iget-wide v2, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D

    double-to-int p5, v2

    double-to-int p1, p1

    invoke-direct {p0, p5, p1, p3}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->adjustDuration(III)V

    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    :cond_2
    iget-wide p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    int-to-double v0, p4

    cmpl-double p3, p1, v0

    if-lez p3, :cond_3

    iget-wide v2, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D

    double-to-int p3, v2

    double-to-int p1, p1

    invoke-direct {p0, p3, p1, p4}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->adjustDuration(III)V

    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    :cond_3
    return-void

    :cond_4
    :goto_1
    invoke-direct {p0, p1, p3, p4, p2}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->startAfterEdge(IIII)V

    return-void
.end method""",
        'replacement': """.method fling(IIIII)V
    .registers 10

    goto :goto_7

    nop

    :goto_0
    invoke-direct {p0, p2}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->getSplineFlingDistance(I)D

    move-result-wide v0

    goto :goto_37

    nop

    :goto_1
    invoke-direct {p0, p5, p1, p3}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->adjustDuration(III)V

    goto :goto_1b

    nop

    :goto_2
    goto :goto_2f

    :goto_3
    goto :goto_24

    nop

    :goto_4
    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D

    goto :goto_36

    nop

    :goto_5
    double-to-int p5, v2

    goto :goto_1a

    nop

    :goto_6
    iput-boolean p5, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinished:Z

    goto :goto_32

    nop

    :goto_7
    iput p5, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mOver:I

    goto :goto_20

    nop

    :goto_8
    if-gtz p3, :cond_0

    goto :goto_e

    :cond_0
    goto :goto_30

    nop

    :goto_9
    double-to-int p1, p1

    goto :goto_34

    nop

    :goto_a
    const-wide/16 v0, 0x0

    :goto_b
    goto :goto_35

    nop

    :goto_c
    iput p5, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSplineDuration:I

    goto :goto_31

    nop

    :goto_d
    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    :goto_e
    goto :goto_2e

    nop

    :goto_f
    add-int/2addr p1, p2

    goto :goto_18

    nop

    :goto_10
    cmpg-double p5, p1, v0

    goto :goto_12

    nop

    :goto_11
    if-nez p2, :cond_1

    goto :goto_38

    :cond_1
    goto :goto_14

    nop

    :goto_12
    if-ltz p5, :cond_2

    goto :goto_1c

    :cond_2
    goto :goto_17

    nop

    :goto_13
    iput-wide p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    goto :goto_2b

    nop

    :goto_14
    invoke-direct {p0, p2}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->getSplineFlingDuration(I)I

    move-result p5

    goto :goto_1f

    nop

    :goto_15
    double-to-int p3, v2

    goto :goto_9

    nop

    :goto_16
    iput p2, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSplineDistance:I

    goto :goto_f

    nop

    :goto_17
    iget-wide v2, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D

    goto :goto_5

    nop

    :goto_18
    int-to-double p1, p1

    goto :goto_13

    nop

    :goto_19
    invoke-static {p2}, Ljava/lang/Math;->signum(F)F

    move-result p2

    goto :goto_33

    nop

    :goto_1a
    double-to-int p1, p1

    goto :goto_1

    nop

    :goto_1b
    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    :goto_1c
    goto :goto_1e

    nop

    :goto_1d
    double-to-int p2, v0

    goto :goto_16

    nop

    :goto_1e
    iget-wide p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    goto :goto_27

    nop

    :goto_1f
    iput p5, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSplineDuration:I

    goto :goto_2c

    nop

    :goto_20
    const/4 p5, 0x0

    goto :goto_6

    nop

    :goto_21
    mul-double/2addr v0, v2

    goto :goto_1d

    nop

    :goto_22
    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStartTime:J

    goto :goto_28

    nop

    :goto_23
    cmpl-double p3, p1, v0

    goto :goto_8

    nop

    :goto_24
    iput p5, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mState:I

    goto :goto_11

    nop

    :goto_25
    invoke-direct {p0, p1, p3, p4, p2}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->startAfterEdge(IIII)V

    goto :goto_3a

    nop

    :goto_26
    if-lt p1, p3, :cond_3

    goto :goto_3

    :cond_3
    goto :goto_2

    nop

    :goto_27
    int-to-double v0, p4

    goto :goto_23

    nop

    :goto_28
    int-to-double v0, p1

    goto :goto_4

    nop

    :goto_29
    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mVelocity:D

    goto :goto_39

    nop

    :goto_2a
    invoke-static {}, Lmiuix/view/animation/AnimationUtils;->currentAnimationTimeNanos()J

    move-result-wide v0

    goto :goto_22

    nop

    :goto_2b
    int-to-double v0, p3

    goto :goto_10

    nop

    :goto_2c
    iput p5, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mDuration:I

    goto :goto_0

    nop

    :goto_2d
    if-le p1, p4, :cond_4

    goto :goto_2f

    :cond_4
    goto :goto_26

    nop

    :goto_2e
    return-void

    :goto_2f
    goto :goto_25

    nop

    :goto_30
    iget-wide v2, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D

    goto :goto_15

    nop

    :goto_31
    iput p5, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mDuration:I

    goto :goto_2a

    nop

    :goto_32
    int-to-double v0, p2

    goto :goto_29

    nop

    :goto_33
    float-to-double v2, p2

    goto :goto_21

    nop

    :goto_34
    invoke-direct {p0, p3, p1, p4}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->adjustDuration(III)V

    goto :goto_d

    nop

    :goto_35
    int-to-float p2, p2

    goto :goto_19

    nop

    :goto_36
    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D

    goto :goto_2d

    nop

    :goto_37
    goto :goto_b

    :goto_38
    goto :goto_a

    nop

    :goto_39
    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrVelocity:D

    goto :goto_c

    nop

    :goto_3a
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_widget_OverScroller__SplineOverScroller__isAtEquilibrium',
        'method': '.method isAtEquilibrium(DD)Z',
        'method_name': 'isAtEquilibrium',
        'method_anchors': ['invoke-static {p1, p2}, Ljava/lang/Math;->abs(D)D', 'if-gez p0, :cond_0', 'return p0', 'return p0'],
        'type': 'method_replace',
        'search': """.method isAtEquilibrium(DD)Z
    .registers 5

    sub-double/2addr p1, p3

    invoke-static {p1, p2}, Ljava/lang/Math;->abs(D)D

    move-result-wide p0

    const-wide/high16 p2, 0x3ff0000000000000L

    cmpg-double p0, p0, p2

    if-gez p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method isAtEquilibrium(DD)Z
    .registers 5

    goto :goto_9

    nop

    :goto_0
    if-ltz p0, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_7

    nop

    :goto_1
    return p0

    :goto_2
    goto :goto_4

    nop

    :goto_3
    invoke-static {p1, p2}, Ljava/lang/Math;->abs(D)D

    move-result-wide p0

    goto :goto_8

    nop

    :goto_4
    const/4 p0, 0x0

    goto :goto_6

    nop

    :goto_5
    cmpg-double p0, p0, p2

    goto :goto_0

    nop

    :goto_6
    return p0

    :goto_7
    const/4 p0, 0x1

    goto :goto_1

    nop

    :goto_8
    const-wide/high16 p2, 0x3ff0000000000000L

    goto :goto_5

    nop

    :goto_9
    sub-double/2addr p1, p3

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_widget_OverScroller__SplineOverScroller__notifyEdgeReached',
        'method': '.method notifyEdgeReached(III)V',
        'method_name': 'notifyEdgeReached',
        'method_anchors': ['iget v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mState:I', 'if-nez v0, :cond_0', 'iput p3, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mOver:I', 'invoke-static {}, Lmiuix/view/animation/AnimationUtils;->currentAnimationTimeNanos()J', 'iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStartTime:J', 'iget-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrVelocity:D', 'invoke-direct {p0, p1, p2, p2, p3}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->startAfterEdge(IIII)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method notifyEdgeReached(III)V
    .registers 6

    iget v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mState:I

    if-nez v0, :cond_0

    iput p3, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mOver:I

    invoke-static {}, Lmiuix/view/animation/AnimationUtils;->currentAnimationTimeNanos()J

    move-result-wide v0

    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStartTime:J

    iget-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrVelocity:D

    double-to-int p3, v0

    invoke-direct {p0, p1, p2, p2, p3}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->startAfterEdge(IIII)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method notifyEdgeReached(III)V
    .registers 6

    goto :goto_9

    nop

    :goto_0
    iput p3, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mOver:I

    goto :goto_8

    nop

    :goto_1
    invoke-direct {p0, p1, p2, p2, p3}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->startAfterEdge(IIII)V

    :goto_2
    goto :goto_4

    nop

    :goto_3
    if-eqz v0, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_0

    nop

    :goto_4
    return-void

    :goto_5
    double-to-int p3, v0

    goto :goto_1

    nop

    :goto_6
    iget-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrVelocity:D

    goto :goto_5

    nop

    :goto_7
    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStartTime:J

    goto :goto_6

    nop

    :goto_8
    invoke-static {}, Lmiuix/view/animation/AnimationUtils;->currentAnimationTimeNanos()J

    move-result-wide v0

    goto :goto_7

    nop

    :goto_9
    iget v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mState:I

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_widget_OverScroller__SplineOverScroller__setFinalPosition',
        'method': '.method setFinalPosition(I)V',
        'method_name': 'setFinalPosition',
        'method_anchors': ['iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D', 'iput-boolean p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinished:Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method setFinalPosition(I)V
    .registers 4

    int-to-double v0, p1

    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    const/4 p1, 0x0

    iput-boolean p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinished:Z

    return-void
.end method""",
        'replacement': """.method setFinalPosition(I)V
    .registers 4

    goto :goto_1

    nop

    :goto_0
    const/4 p1, 0x0

    goto :goto_4

    nop

    :goto_1
    int-to-double v0, p1

    goto :goto_2

    nop

    :goto_2
    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    goto :goto_0

    nop

    :goto_3
    return-void

    :goto_4
    iput-boolean p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinished:Z

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_widget_OverScroller__SplineOverScroller__springback',
        'method': '.method springback(III)Z',
        'method_name': 'springback',
        'method_anchors': ['iput-boolean v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinished:Z', 'iput-wide v1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D', 'iput-wide v1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D', 'iput-wide v1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D', 'iput-wide v1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mVelocity:D', 'invoke-static {}, Lmiuix/view/animation/AnimationUtils;->currentAnimationTimeNanos()J', 'iput-wide v1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStartTime:J', 'iput v1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mDuration:I'],
        'type': 'method_replace',
        'search': """.method springback(III)Z
    .registers 7

    const/4 v0, 0x1

    iput-boolean v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinished:Z

    int-to-double v1, p1

    iput-wide v1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    iput-wide v1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D

    iput-wide v1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D

    const-wide/16 v1, 0x0

    iput-wide v1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mVelocity:D

    invoke-static {}, Lmiuix/view/animation/AnimationUtils;->currentAnimationTimeNanos()J

    move-result-wide v1

    iput-wide v1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStartTime:J

    const/4 v1, 0x0

    iput v1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mDuration:I

    if-ge p1, p2, :cond_0

    invoke-direct {p0, p1, p2, v1}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->startSpringback(III)V

    goto :goto_0

    :cond_0
    if-le p1, p3, :cond_1

    invoke-direct {p0, p1, p3, v1}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->startSpringback(III)V

    :cond_1
    :goto_0
    iget-boolean p0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinished:Z

    xor-int/2addr p0, v0

    return p0
.end method""",
        'replacement': """.method springback(III)Z
    .registers 7

    goto :goto_4

    nop

    :goto_0
    invoke-direct {p0, p1, p2, v1}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->startSpringback(III)V

    goto :goto_7

    nop

    :goto_1
    iput-wide v1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    goto :goto_e

    nop

    :goto_2
    iput v1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mDuration:I

    goto :goto_d

    nop

    :goto_3
    iput-wide v1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D

    goto :goto_14

    nop

    :goto_4
    const/4 v0, 0x1

    goto :goto_13

    nop

    :goto_5
    invoke-static {}, Lmiuix/view/animation/AnimationUtils;->currentAnimationTimeNanos()J

    move-result-wide v1

    goto :goto_f

    nop

    :goto_6
    iget-boolean p0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinished:Z

    goto :goto_12

    nop

    :goto_7
    goto :goto_c

    :goto_8
    goto :goto_10

    nop

    :goto_9
    return p0

    :goto_a
    const/4 v1, 0x0

    goto :goto_2

    nop

    :goto_b
    invoke-direct {p0, p1, p3, v1}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->startSpringback(III)V

    :goto_c
    goto :goto_6

    nop

    :goto_d
    if-lt p1, p2, :cond_0

    goto :goto_8

    :cond_0
    goto :goto_0

    nop

    :goto_e
    iput-wide v1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D

    goto :goto_3

    nop

    :goto_f
    iput-wide v1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStartTime:J

    goto :goto_a

    nop

    :goto_10
    if-gt p1, p3, :cond_1

    goto :goto_c

    :cond_1
    goto :goto_b

    nop

    :goto_11
    iput-wide v1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mVelocity:D

    goto :goto_5

    nop

    :goto_12
    xor-int/2addr p0, v0

    goto :goto_9

    nop

    :goto_13
    iput-boolean v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinished:Z

    goto :goto_15

    nop

    :goto_14
    const-wide/16 v1, 0x0

    goto :goto_11

    nop

    :goto_15
    int-to-double v1, p1

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_widget_OverScroller__SplineOverScroller__startScroll',
        'method': '.method startScroll(III)V',
        'method_name': 'startScroll',
        'method_anchors': ['iput-boolean v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinished:Z', 'iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D', 'iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D', 'iput-wide p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D', 'invoke-static {}, Lmiuix/view/animation/AnimationUtils;->currentAnimationTimeNanos()J', 'iput-wide p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStartTime:J', 'iput p3, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mDuration:I', 'iput p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mDeceleration:F'],
        'type': 'method_replace',
        'search': """.method startScroll(III)V
    .registers 6

    const/4 v0, 0x0

    iput-boolean v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinished:Z

    int-to-double v0, p1

    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D

    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D

    add-int/2addr p1, p2

    int-to-double p1, p1

    iput-wide p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    invoke-static {}, Lmiuix/view/animation/AnimationUtils;->currentAnimationTimeNanos()J

    move-result-wide p1

    iput-wide p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStartTime:J

    iput p3, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mDuration:I

    const/4 p1, 0x0

    iput p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mDeceleration:F

    const-wide/16 p1, 0x0

    iput-wide p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mVelocity:D

    return-void
.end method""",
        'replacement': """.method startScroll(III)V
    .registers 6

    goto :goto_c

    nop

    :goto_0
    const/4 p1, 0x0

    goto :goto_d

    nop

    :goto_1
    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D

    goto :goto_7

    nop

    :goto_2
    invoke-static {}, Lmiuix/view/animation/AnimationUtils;->currentAnimationTimeNanos()J

    move-result-wide p1

    goto :goto_4

    nop

    :goto_3
    return-void

    :goto_4
    iput-wide p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStartTime:J

    goto :goto_6

    nop

    :goto_5
    iput-boolean v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinished:Z

    goto :goto_f

    nop

    :goto_6
    iput p3, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mDuration:I

    goto :goto_0

    nop

    :goto_7
    add-int/2addr p1, p2

    goto :goto_a

    nop

    :goto_8
    iput-wide p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mVelocity:D

    goto :goto_3

    nop

    :goto_9
    iput-wide p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    goto :goto_2

    nop

    :goto_a
    int-to-double p1, p1

    goto :goto_9

    nop

    :goto_b
    const-wide/16 p1, 0x0

    goto :goto_8

    nop

    :goto_c
    const/4 v0, 0x0

    goto :goto_5

    nop

    :goto_d
    iput p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mDeceleration:F

    goto :goto_b

    nop

    :goto_e
    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D

    goto :goto_1

    nop

    :goto_f
    int-to-double v0, p1

    goto :goto_e

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_widget_OverScroller__SplineOverScroller__startScrollByFling',
        'method': '.method startScrollByFling(FII)V',
        'method_name': 'startScrollByFling',
        'method_anchors': ['iput-boolean v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinished:Z', 'iput-boolean v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mLastStep:Z', 'invoke-virtual {p0, v0}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setState(I)V', 'iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mOriginStart:D', 'iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D', 'iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D', 'iput-wide p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D', 'invoke-static {}, Lmiuix/view/animation/AnimationUtils;->currentAnimationTimeNanos()J'],
        'type': 'method_replace',
        'search': """.method startScrollByFling(FII)V
    .registers 6

    const/4 v0, 0x0

    iput-boolean v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinished:Z

    iput-boolean v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mLastStep:Z

    invoke-virtual {p0, v0}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setState(I)V

    float-to-double v0, p1

    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mOriginStart:D

    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D

    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D

    int-to-float p2, p2

    add-float/2addr p1, p2

    float-to-double p1, p1

    iput-wide p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    invoke-static {}, Lmiuix/view/animation/AnimationUtils;->currentAnimationTimeNanos()J

    move-result-wide p1

    iput-wide p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStartTime:J

    int-to-double p1, p3

    iput-wide p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mVelocity:D

    iput-wide p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrVelocity:D

    new-instance p1, Lmiuix/animation/physics/SpringOperator;

    invoke-direct {p1}, Lmiuix/animation/physics/SpringOperator;-><init>()V

    iput-object p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSpringOperator:Lmiuix/animation/physics/SpringOperator;

    const/4 p1, 0x2

    new-array p1, p1, [D

    fill-array-data p1, :array_0

    iput-object p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSpringFactor:[D

    new-instance p1, Lmiuix/animation/internal/AnimData;

    invoke-direct {p1}, Lmiuix/animation/internal/AnimData;-><init>()V

    iput-object p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSpringAnimData:Lmiuix/animation/internal/AnimData;

    iget-wide p2, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D

    iput-wide p2, p1, Lmiuix/animation/internal/AnimData;->startValue:D

    iget-wide p2, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    iput-wide p2, p1, Lmiuix/animation/internal/AnimData;->targetValue:D

    iget-wide p2, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D

    iput-wide p2, p1, Lmiuix/animation/internal/AnimData;->value:D

    iget-wide p2, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrVelocity:D

    iput-wide p2, p1, Lmiuix/animation/internal/AnimData;->velocity:D

    const/4 p1, 0x3

    new-array p1, p1, [D

    iput-object p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSpringParams:[D

    iget-object p2, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSpringOperator:Lmiuix/animation/physics/SpringOperator;

    iget-object p0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSpringFactor:[D

    invoke-virtual {p2, p0, p1}, Lmiuix/animation/physics/SpringOperator;->getParameters([D[D)V

    return-void

    :array_0
    .array-data 8
        0x3fefae147ae147aeL
        0x3fd999999999999aL
    .end array-data
.end method""",
        'replacement': """.method startScrollByFling(FII)V
    .registers 6

    goto :goto_16

    nop

    :goto_0
    iget-wide p2, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D

    goto :goto_d

    nop

    :goto_1
    iput-boolean v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mLastStep:Z

    goto :goto_13

    nop

    :goto_2
    const/4 p1, 0x2

    goto :goto_f

    nop

    :goto_3
    iget-wide p2, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrVelocity:D

    goto :goto_1f

    nop

    :goto_4
    invoke-static {}, Lmiuix/view/animation/AnimationUtils;->currentAnimationTimeNanos()J

    move-result-wide p1

    goto :goto_1b

    nop

    :goto_5
    iput-wide p2, p1, Lmiuix/animation/internal/AnimData;->targetValue:D

    goto :goto_0

    nop

    :goto_6
    invoke-direct {p1}, Lmiuix/animation/physics/SpringOperator;-><init>()V

    goto :goto_1c

    nop

    :goto_7
    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mOriginStart:D

    goto :goto_1d

    nop

    :goto_8
    iget-object p2, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSpringOperator:Lmiuix/animation/physics/SpringOperator;

    goto :goto_c

    nop

    :goto_9
    iput-object p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSpringParams:[D

    goto :goto_8

    nop

    :goto_a
    iget-wide p2, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    goto :goto_5

    nop

    :goto_b
    iget-wide p2, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D

    goto :goto_17

    nop

    :goto_c
    iget-object p0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSpringFactor:[D

    goto :goto_1a

    nop

    :goto_d
    iput-wide p2, p1, Lmiuix/animation/internal/AnimData;->value:D

    goto :goto_3

    nop

    :goto_e
    int-to-double p1, p3

    goto :goto_11

    nop

    :goto_f
    new-array p1, p1, [D

    fill-array-data p1, :array_0

    goto :goto_23

    nop

    :goto_10
    return-void

    nop

    :array_0
    .array-data 8
        0x3fefae147ae147aeL
        0x3fd999999999999aL
    .end array-data

    :goto_11
    iput-wide p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mVelocity:D

    goto :goto_28

    nop

    :goto_12
    new-instance p1, Lmiuix/animation/physics/SpringOperator;

    goto :goto_6

    nop

    :goto_13
    invoke-virtual {p0, v0}, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->setState(I)V

    goto :goto_1e

    nop

    :goto_14
    new-array p1, p1, [D

    goto :goto_9

    nop

    :goto_15
    iput-boolean v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinished:Z

    goto :goto_1

    nop

    :goto_16
    const/4 v0, 0x0

    goto :goto_15

    nop

    :goto_17
    iput-wide p2, p1, Lmiuix/animation/internal/AnimData;->startValue:D

    goto :goto_a

    nop

    :goto_18
    const/4 p1, 0x3

    goto :goto_14

    nop

    :goto_19
    float-to-double p1, p1

    goto :goto_25

    nop

    :goto_1a
    invoke-virtual {p2, p0, p1}, Lmiuix/animation/physics/SpringOperator;->getParameters([D[D)V

    goto :goto_10

    nop

    :goto_1b
    iput-wide p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStartTime:J

    goto :goto_e

    nop

    :goto_1c
    iput-object p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSpringOperator:Lmiuix/animation/physics/SpringOperator;

    goto :goto_2

    nop

    :goto_1d
    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D

    goto :goto_21

    nop

    :goto_1e
    float-to-double v0, p1

    goto :goto_7

    nop

    :goto_1f
    iput-wide p2, p1, Lmiuix/animation/internal/AnimData;->velocity:D

    goto :goto_18

    nop

    :goto_20
    int-to-float p2, p2

    goto :goto_26

    nop

    :goto_21
    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D

    goto :goto_20

    nop

    :goto_22
    iput-object p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSpringAnimData:Lmiuix/animation/internal/AnimData;

    goto :goto_b

    nop

    :goto_23
    iput-object p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSpringFactor:[D

    goto :goto_24

    nop

    :goto_24
    new-instance p1, Lmiuix/animation/internal/AnimData;

    goto :goto_27

    nop

    :goto_25
    iput-wide p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    goto :goto_4

    nop

    :goto_26
    add-float/2addr p1, p2

    goto :goto_19

    nop

    :goto_27
    invoke-direct {p1}, Lmiuix/animation/internal/AnimData;-><init>()V

    goto :goto_22

    nop

    :goto_28
    iput-wide p1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrVelocity:D

    goto :goto_12

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_widget_OverScroller__SplineOverScroller__update',
        'method': '.method update()Z',
        'method_name': 'update',
        'method_anchors': ['invoke-static {}, Lmiuix/view/animation/AnimationUtils;->currentAnimationTimeNanos()J', 'iget-wide v2, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStartTime:J', 'if-nez v2, :cond_1', 'iget p0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mDuration:I', 'if-lez p0, :cond_0', 'return v4', 'return v3', 'iget v2, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mDuration:I'],
        'type': 'method_replace',
        'search': """.method update()Z
    .registers 10

    invoke-static {}, Lmiuix/view/animation/AnimationUtils;->currentAnimationTimeNanos()J

    move-result-wide v0

    iget-wide v2, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStartTime:J

    sub-long/2addr v0, v2

    const-wide/16 v2, 0x0

    cmp-long v2, v0, v2

    const/4 v3, 0x0

    const/4 v4, 0x1

    if-nez v2, :cond_1

    iget p0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mDuration:I

    if-lez p0, :cond_0

    return v4

    :cond_0
    return v3

    :cond_1
    iget v2, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mDuration:I

    int-to-long v5, v2

    const-wide/32 v7, 0xf4240

    mul-long/2addr v5, v7

    cmp-long v5, v0, v5

    if-lez v5, :cond_2

    return v3

    :cond_2
    iget v3, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mState:I

    if-eqz v3, :cond_5

    const/high16 v5, 0x40000000

    if-eq v3, v4, :cond_4

    const/4 v2, 0x2

    if-eq v3, v2, :cond_3

    const-wide/16 v0, 0x0

    goto :goto_2

    :cond_3
    long-to-double v0, v0

    const-wide v2, 0x41cdcd6500000000L

    div-double/2addr v0, v2

    double-to-float v0, v0

    iget-wide v1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mVelocity:D

    iget v3, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mDeceleration:F

    mul-float v6, v3, v0

    float-to-double v6, v6

    add-double/2addr v6, v1

    iput-wide v6, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrVelocity:D

    float-to-double v6, v0

    mul-double/2addr v1, v6

    mul-float/2addr v3, v0

    mul-float/2addr v3, v0

    div-float/2addr v3, v5

    float-to-double v5, v3

    add-double v0, v1, v5

    goto :goto_2

    :cond_4
    long-to-float v0, v0

    int-to-float v1, v2

    div-float/2addr v0, v1

    mul-float v1, v0, v0

    iget-wide v2, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mVelocity:D

    double-to-float v2, v2

    invoke-static {v2}, Ljava/lang/Math;->signum(F)F

    move-result v2

    iget v3, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mOver:I

    int-to-float v6, v3

    mul-float/2addr v6, v2

    const/high16 v7, 0x40400000

    mul-float/2addr v7, v1

    mul-float/2addr v5, v0

    mul-float/2addr v5, v1

    sub-float/2addr v7, v5

    mul-float/2addr v6, v7

    float-to-double v5, v6

    int-to-float v3, v3

    mul-float/2addr v2, v3

    const/high16 v3, 0x40c00000

    mul-float/2addr v2, v3

    neg-float v0, v0

    add-float/2addr v0, v1

    mul-float/2addr v2, v0

    float-to-double v0, v2

    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrVelocity:D

    :goto_0
    move-wide v0, v5

    goto :goto_2

    :cond_5
    long-to-float v0, v0

    iget v1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSplineDuration:I

    int-to-long v2, v1

    mul-long/2addr v2, v7

    long-to-float v2, v2

    div-float/2addr v0, v2

    const/high16 v2, 0x42c80000

    mul-float v3, v0, v2

    float-to-int v3, v3

    const/16 v5, 0x64

    if-ge v3, v5, :cond_6

    int-to-float v5, v3

    div-float/2addr v5, v2

    add-int/lit8 v6, v3, 0x1

    int-to-float v7, v6

    div-float/2addr v7, v2

    sget-object v2, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->SPLINE_POSITION:[F

    aget v3, v2, v3

    aget v2, v2, v6

    sub-float/2addr v2, v3

    sub-float/2addr v7, v5

    div-float/2addr v2, v7

    sub-float/2addr v0, v5

    mul-float/2addr v0, v2

    add-float/2addr v3, v0

    goto :goto_1

    :cond_6
    const/high16 v3, 0x3f800000

    const/4 v2, 0x0

    :goto_1
    iget v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSplineDistance:I

    int-to-float v5, v0

    mul-float/2addr v3, v5

    float-to-double v5, v3

    int-to-float v0, v0

    mul-float/2addr v2, v0

    int-to-float v0, v1

    div-float/2addr v2, v0

    const/high16 v0, 0x447a0000

    mul-float/2addr v2, v0

    float-to-double v0, v2

    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrVelocity:D

    goto :goto_0

    :goto_2
    iget-wide v2, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D

    invoke-static {v0, v1}, Ljava/lang/Math;->round(D)J

    move-result-wide v0

    long-to-int v0, v0

    int-to-double v0, v0

    add-double/2addr v2, v0

    iput-wide v2, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D

    return v4
.end method""",
        'replacement': """.method update()Z
    .registers 10

    goto :goto_4

    nop

    :goto_0
    iput-wide v6, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrVelocity:D

    goto :goto_29

    nop

    :goto_1
    sub-float/2addr v0, v5

    goto :goto_52

    nop

    :goto_2
    iget v2, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mDuration:I

    goto :goto_19

    nop

    :goto_3
    div-float/2addr v0, v2

    goto :goto_a

    nop

    :goto_4
    invoke-static {}, Lmiuix/view/animation/AnimationUtils;->currentAnimationTimeNanos()J

    move-result-wide v0

    goto :goto_6

    nop

    :goto_5
    div-float/2addr v3, v5

    goto :goto_3e

    nop

    :goto_6
    iget-wide v2, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStartTime:J

    goto :goto_2c

    nop

    :goto_7
    if-lt v3, v5, :cond_0

    goto :goto_4b

    :cond_0
    goto :goto_2d

    nop

    :goto_8
    if-ne v3, v2, :cond_1

    goto :goto_6a

    :cond_1
    goto :goto_e

    nop

    :goto_9
    mul-float v1, v0, v0

    goto :goto_13

    nop

    :goto_a
    const/high16 v2, 0x42c80000

    goto :goto_35

    nop

    :goto_b
    mul-double/2addr v1, v6

    goto :goto_22

    nop

    :goto_c
    const-wide/32 v7, 0xf4240

    goto :goto_60

    nop

    :goto_d
    sub-float/2addr v7, v5

    goto :goto_41

    nop

    :goto_e
    const-wide/16 v0, 0x0

    goto :goto_69

    nop

    :goto_f
    long-to-double v0, v0

    goto :goto_5d

    nop

    :goto_10
    goto :goto_47

    :goto_11
    goto :goto_15

    nop

    :goto_12
    const/high16 v5, 0x40000000

    goto :goto_1e

    nop

    :goto_13
    iget-wide v2, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mVelocity:D

    goto :goto_6c

    nop

    :goto_14
    int-to-float v7, v6

    goto :goto_45

    nop

    :goto_15
    long-to-float v0, v0

    goto :goto_63

    nop

    :goto_16
    mul-float/2addr v2, v0

    goto :goto_6d

    nop

    :goto_17
    const/high16 v7, 0x40400000

    goto :goto_7d

    nop

    :goto_18
    int-to-float v1, v2

    goto :goto_2b

    nop

    :goto_19
    int-to-long v5, v2

    goto :goto_c

    nop

    :goto_1a
    if-eqz v2, :cond_2

    goto :goto_62

    :cond_2
    goto :goto_5f

    nop

    :goto_1b
    mul-float v6, v3, v0

    goto :goto_2f

    nop

    :goto_1c
    const/4 v2, 0x0

    :goto_1d
    goto :goto_7b

    nop

    :goto_1e
    if-ne v3, v4, :cond_3

    goto :goto_54

    :cond_3
    goto :goto_56

    nop

    :goto_1f
    cmp-long v2, v0, v2

    goto :goto_70

    nop

    :goto_20
    long-to-float v2, v2

    goto :goto_3

    nop

    :goto_21
    int-to-float v3, v3

    goto :goto_6f

    nop

    :goto_22
    mul-float/2addr v3, v0

    goto :goto_33

    nop

    :goto_23
    neg-float v0, v0

    goto :goto_42

    nop

    :goto_24
    float-to-double v0, v2

    goto :goto_57

    nop

    :goto_25
    long-to-int v0, v0

    goto :goto_4d

    nop

    :goto_26
    if-gtz v5, :cond_4

    goto :goto_81

    :cond_4
    goto :goto_80

    nop

    :goto_27
    float-to-int v3, v3

    goto :goto_4f

    nop

    :goto_28
    iget v3, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mDeceleration:F

    goto :goto_1b

    nop

    :goto_29
    float-to-double v6, v0

    goto :goto_b

    nop

    :goto_2a
    const/high16 v3, 0x40c00000

    goto :goto_30

    nop

    :goto_2b
    div-float/2addr v0, v1

    goto :goto_9

    nop

    :goto_2c
    sub-long/2addr v0, v2

    goto :goto_7f

    nop

    :goto_2d
    int-to-float v5, v3

    goto :goto_3d

    nop

    :goto_2e
    iget-wide v2, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D

    goto :goto_4c

    nop

    :goto_2f
    float-to-double v6, v6

    goto :goto_3c

    nop

    :goto_30
    mul-float/2addr v2, v3

    goto :goto_23

    nop

    :goto_31
    int-to-float v0, v0

    goto :goto_55

    nop

    :goto_32
    aget v2, v2, v6

    goto :goto_7a

    nop

    :goto_33
    mul-float/2addr v3, v0

    goto :goto_5

    nop

    :goto_34
    add-double/2addr v2, v0

    goto :goto_36

    nop

    :goto_35
    mul-float v3, v0, v2

    goto :goto_27

    nop

    :goto_36
    iput-wide v2, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D

    goto :goto_58

    nop

    :goto_37
    float-to-double v5, v3

    goto :goto_31

    nop

    :goto_38
    mul-float/2addr v5, v0

    goto :goto_5e

    nop

    :goto_39
    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrVelocity:D

    :goto_3a
    goto :goto_50

    nop

    :goto_3b
    mul-float/2addr v6, v7

    goto :goto_67

    nop

    :goto_3c
    add-double/2addr v6, v1

    goto :goto_0

    nop

    :goto_3d
    div-float/2addr v5, v2

    goto :goto_65

    nop

    :goto_3e
    float-to-double v5, v3

    goto :goto_78

    nop

    :goto_3f
    int-to-long v2, v1

    goto :goto_43

    nop

    :goto_40
    iget-wide v1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mVelocity:D

    goto :goto_28

    nop

    :goto_41
    div-float/2addr v2, v7

    goto :goto_1

    nop

    :goto_42
    add-float/2addr v0, v1

    goto :goto_16

    nop

    :goto_43
    mul-long/2addr v2, v7

    goto :goto_20

    nop

    :goto_44
    invoke-static {v2}, Ljava/lang/Math;->signum(F)F

    move-result v2

    goto :goto_72

    nop

    :goto_45
    div-float/2addr v7, v2

    goto :goto_7e

    nop

    :goto_46
    goto :goto_3a

    :goto_47
    goto :goto_2e

    nop

    :goto_48
    mul-float/2addr v6, v2

    goto :goto_17

    nop

    :goto_49
    double-to-float v0, v0

    goto :goto_40

    nop

    :goto_4a
    goto :goto_1d

    :goto_4b
    goto :goto_64

    nop

    :goto_4c
    invoke-static {v0, v1}, Ljava/lang/Math;->round(D)J

    move-result-wide v0

    goto :goto_25

    nop

    :goto_4d
    int-to-double v0, v0

    goto :goto_34

    nop

    :goto_4e
    mul-float/2addr v2, v0

    goto :goto_24

    nop

    :goto_4f
    const/16 v5, 0x64

    goto :goto_7

    nop

    :goto_50
    move-wide v0, v5

    goto :goto_10

    nop

    :goto_51
    if-gtz p0, :cond_5

    goto :goto_75

    :cond_5
    goto :goto_74

    nop

    :goto_52
    mul-float/2addr v0, v2

    goto :goto_66

    nop

    :goto_53
    goto :goto_47

    :goto_54
    goto :goto_59

    nop

    :goto_55
    mul-float/2addr v2, v0

    goto :goto_6e

    nop

    :goto_56
    const/4 v2, 0x2

    goto :goto_8

    nop

    :goto_57
    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrVelocity:D

    goto :goto_46

    nop

    :goto_58
    return v4

    :goto_59
    long-to-float v0, v0

    goto :goto_18

    nop

    :goto_5a
    cmp-long v5, v0, v5

    goto :goto_26

    nop

    :goto_5b
    iget v3, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mState:I

    goto :goto_82

    nop

    :goto_5c
    div-double/2addr v0, v2

    goto :goto_49

    nop

    :goto_5d
    const-wide v2, 0x41cdcd6500000000L

    goto :goto_5c

    nop

    :goto_5e
    mul-float/2addr v5, v1

    goto :goto_7c

    nop

    :goto_5f
    iget p0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mDuration:I

    goto :goto_51

    nop

    :goto_60
    mul-long/2addr v5, v7

    goto :goto_5a

    nop

    :goto_61
    return v3

    :goto_62
    goto :goto_2

    nop

    :goto_63
    iget v1, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSplineDuration:I

    goto :goto_3f

    nop

    :goto_64
    const/high16 v3, 0x3f800000

    goto :goto_1c

    nop

    :goto_65
    add-int/lit8 v6, v3, 0x1

    goto :goto_14

    nop

    :goto_66
    add-float/2addr v3, v0

    goto :goto_4a

    nop

    :goto_67
    float-to-double v5, v6

    goto :goto_21

    nop

    :goto_68
    int-to-float v6, v3

    goto :goto_48

    nop

    :goto_69
    goto :goto_47

    :goto_6a
    goto :goto_f

    nop

    :goto_6b
    aget v3, v2, v3

    goto :goto_32

    nop

    :goto_6c
    double-to-float v2, v2

    goto :goto_44

    nop

    :goto_6d
    float-to-double v0, v2

    goto :goto_39

    nop

    :goto_6e
    int-to-float v0, v1

    goto :goto_73

    nop

    :goto_6f
    mul-float/2addr v2, v3

    goto :goto_2a

    nop

    :goto_70
    const/4 v3, 0x0

    goto :goto_76

    nop

    :goto_71
    const/high16 v0, 0x447a0000

    goto :goto_4e

    nop

    :goto_72
    iget v3, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mOver:I

    goto :goto_68

    nop

    :goto_73
    div-float/2addr v2, v0

    goto :goto_71

    nop

    :goto_74
    return v4

    :goto_75
    goto :goto_61

    nop

    :goto_76
    const/4 v4, 0x1

    goto :goto_1a

    nop

    :goto_77
    int-to-float v5, v0

    goto :goto_79

    nop

    :goto_78
    add-double v0, v1, v5

    goto :goto_53

    nop

    :goto_79
    mul-float/2addr v3, v5

    goto :goto_37

    nop

    :goto_7a
    sub-float/2addr v2, v3

    goto :goto_d

    nop

    :goto_7b
    iget v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mSplineDistance:I

    goto :goto_77

    nop

    :goto_7c
    sub-float/2addr v7, v5

    goto :goto_3b

    nop

    :goto_7d
    mul-float/2addr v7, v1

    goto :goto_38

    nop

    :goto_7e
    sget-object v2, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->SPLINE_POSITION:[F

    goto :goto_6b

    nop

    :goto_7f
    const-wide/16 v2, 0x0

    goto :goto_1f

    nop

    :goto_80
    return v3

    :goto_81
    goto :goto_5b

    nop

    :goto_82
    if-nez v3, :cond_6

    goto :goto_11

    :cond_6
    goto :goto_12

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_widget_OverScroller__SplineOverScroller__updateScroll',
        'method': '.method updateScroll(F)V',
        'method_name': 'updateScroll',
        'method_anchors': ['iget-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D', 'iget-wide v4, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D', 'invoke-static {v2, v3}, Ljava/lang/Math;->round(D)J', 'iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D', 'return-void'],
        'type': 'method_replace',
        'search': """.method updateScroll(F)V
    .registers 8

    iget-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D

    float-to-double v2, p1

    iget-wide v4, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    sub-double/2addr v4, v0

    mul-double/2addr v2, v4

    invoke-static {v2, v3}, Ljava/lang/Math;->round(D)J

    move-result-wide v2

    long-to-double v2, v2

    add-double/2addr v0, v2

    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D

    return-void
.end method""",
        'replacement': """.method updateScroll(F)V
    .registers 8

    goto :goto_5

    nop

    :goto_0
    iget-wide v4, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mFinal:D

    goto :goto_6

    nop

    :goto_1
    float-to-double v2, p1

    goto :goto_0

    nop

    :goto_2
    invoke-static {v2, v3}, Ljava/lang/Math;->round(D)J

    move-result-wide v2

    goto :goto_9

    nop

    :goto_3
    add-double/2addr v0, v2

    goto :goto_4

    nop

    :goto_4
    iput-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mCurrentPosition:D

    goto :goto_7

    nop

    :goto_5
    iget-wide v0, p0, Lmiuix/overscroller/widget/OverScroller$SplineOverScroller;->mStart:D

    goto :goto_1

    nop

    :goto_6
    sub-double/2addr v4, v0

    goto :goto_8

    nop

    :goto_7
    return-void

    :goto_8
    mul-double/2addr v2, v4

    goto :goto_2

    nop

    :goto_9
    long-to-double v2, v2

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
