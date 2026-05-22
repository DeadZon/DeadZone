TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer.smali'
CLASS_FALLBACK_NAMES = ['NumberPicker$SoundPlayHandler$SoundPlayerContainer.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'miuix_pickerwidget_widget_NumberPicker__SoundPlayHandler__SoundPlayerContainer__init',
        'method': '.method init(Landroid/content/Context;I)V',
        'method_name': 'init',
        'method_anchors': ['iget-object v0, p0, Lmiuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer;->mSoundPlayer:Landroid/media/SoundPool;', 'if-nez v0, :cond_0', 'new-instance v0, Landroid/media/SoundPool;', 'invoke-direct {v0, v2, v2, v1}, Landroid/media/SoundPool;-><init>(III)V', 'iput-object v0, p0, Lmiuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer;->mSoundPlayer:Landroid/media/SoundPool;', 'sget v1, Lmiuix/pickerwidget/R$raw;->number_picker_value_change:I', 'invoke-virtual {v0, p1, v1, v2}, Landroid/media/SoundPool;->load(Landroid/content/Context;II)I', 'iput p1, p0, Lmiuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer;->mSoundId:I'],
        'type': 'method_replace',
        'search': """.method init(Landroid/content/Context;I)V
    .registers 6

    iget-object v0, p0, Lmiuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer;->mSoundPlayer:Landroid/media/SoundPool;

    if-nez v0, :cond_0

    new-instance v0, Landroid/media/SoundPool;

    const/4 v1, 0x0

    const/4 v2, 0x1

    invoke-direct {v0, v2, v2, v1}, Landroid/media/SoundPool;-><init>(III)V

    iput-object v0, p0, Lmiuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer;->mSoundPlayer:Landroid/media/SoundPool;

    sget v1, Lmiuix/pickerwidget/R$raw;->number_picker_value_change:I

    invoke-virtual {v0, p1, v1, v2}, Landroid/media/SoundPool;->load(Landroid/content/Context;II)I

    move-result p1

    iput p1, p0, Lmiuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer;->mSoundId:I

    :cond_0
    iget-object p0, p0, Lmiuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer;->mRefs:Ljava/util/Set;

    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p1

    invoke-interface {p0, p1}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    return-void
.end method""",
        'replacement': """.method init(Landroid/content/Context;I)V
    .registers 6

    goto :goto_2

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer;->mRefs:Ljava/util/Set;

    goto :goto_c

    nop

    :goto_1
    invoke-virtual {v0, p1, v1, v2}, Landroid/media/SoundPool;->load(Landroid/content/Context;II)I

    move-result p1

    goto :goto_3

    nop

    :goto_2
    iget-object v0, p0, Lmiuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer;->mSoundPlayer:Landroid/media/SoundPool;

    goto :goto_7

    nop

    :goto_3
    iput p1, p0, Lmiuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer;->mSoundId:I

    :goto_4
    goto :goto_0

    nop

    :goto_5
    sget v1, Lmiuix/pickerwidget/R$raw;->number_picker_value_change:I

    goto :goto_1

    nop

    :goto_6
    const/4 v2, 0x1

    goto :goto_e

    nop

    :goto_7
    if-eqz v0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_8

    nop

    :goto_8
    new-instance v0, Landroid/media/SoundPool;

    goto :goto_d

    nop

    :goto_9
    invoke-interface {p0, p1}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    goto :goto_b

    nop

    :goto_a
    iput-object v0, p0, Lmiuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer;->mSoundPlayer:Landroid/media/SoundPool;

    goto :goto_5

    nop

    :goto_b
    return-void

    :goto_c
    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p1

    goto :goto_9

    nop

    :goto_d
    const/4 v1, 0x0

    goto :goto_6

    nop

    :goto_e
    invoke-direct {v0, v2, v2, v1}, Landroid/media/SoundPool;-><init>(III)V

    goto :goto_a

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_pickerwidget_widget_NumberPicker__SoundPlayHandler__SoundPlayerContainer__play',
        'method': '.method play()V',
        'method_name': 'play',
        'method_anchors': ['invoke-static {}, Ljava/lang/System;->currentTimeMillis()J', 'iget-object v2, p0, Lmiuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer;->mSoundPlayer:Landroid/media/SoundPool;', 'if-eqz v2, :cond_0', 'iget-wide v3, p0, Lmiuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer;->mPrevPlayTime:J', 'if-lez v3, :cond_0', 'iget v3, p0, Lmiuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer;->mSoundId:I', 'invoke-virtual/range {v2 .. v8}, Landroid/media/SoundPool;->play(IFFIIF)I', 'iput-wide v0, p0, Lmiuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer;->mPrevPlayTime:J'],
        'type': 'method_replace',
        'search': """.method play()V
    .registers 10

    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v0

    iget-object v2, p0, Lmiuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer;->mSoundPlayer:Landroid/media/SoundPool;

    if-eqz v2, :cond_0

    iget-wide v3, p0, Lmiuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer;->mPrevPlayTime:J

    sub-long v3, v0, v3

    const-wide/16 v5, 0x32

    cmp-long v3, v3, v5

    if-lez v3, :cond_0

    iget v3, p0, Lmiuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer;->mSoundId:I

    const/4 v7, 0x0

    const/high16 v8, 0x3f800000

    const/high16 v4, 0x3f800000

    const/high16 v5, 0x3f800000

    const/4 v6, 0x0

    invoke-virtual/range {v2 .. v8}, Landroid/media/SoundPool;->play(IFFIIF)I

    iput-wide v0, p0, Lmiuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer;->mPrevPlayTime:J

    :cond_0
    return-void
.end method""",
        'replacement': """.method play()V
    .registers 10

    goto :goto_3

    nop

    :goto_0
    return-void

    :goto_1
    const/high16 v8, 0x3f800000

    goto :goto_8

    nop

    :goto_2
    cmp-long v3, v3, v5

    goto :goto_e

    nop

    :goto_3
    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v0

    goto :goto_4

    nop

    :goto_4
    iget-object v2, p0, Lmiuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer;->mSoundPlayer:Landroid/media/SoundPool;

    goto :goto_7

    nop

    :goto_5
    iput-wide v0, p0, Lmiuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer;->mPrevPlayTime:J

    :goto_6
    goto :goto_0

    nop

    :goto_7
    if-nez v2, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_d

    nop

    :goto_8
    const/high16 v4, 0x3f800000

    goto :goto_b

    nop

    :goto_9
    iget v3, p0, Lmiuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer;->mSoundId:I

    goto :goto_a

    nop

    :goto_a
    const/4 v7, 0x0

    goto :goto_1

    nop

    :goto_b
    const/high16 v5, 0x3f800000

    goto :goto_c

    nop

    :goto_c
    const/4 v6, 0x0

    goto :goto_11

    nop

    :goto_d
    iget-wide v3, p0, Lmiuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer;->mPrevPlayTime:J

    goto :goto_f

    nop

    :goto_e
    if-gtz v3, :cond_1

    goto :goto_6

    :cond_1
    goto :goto_9

    nop

    :goto_f
    sub-long v3, v0, v3

    goto :goto_10

    nop

    :goto_10
    const-wide/16 v5, 0x32

    goto :goto_2

    nop

    :goto_11
    invoke-virtual/range {v2 .. v8}, Landroid/media/SoundPool;->play(IFFIIF)I

    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_pickerwidget_widget_NumberPicker__SoundPlayHandler__SoundPlayerContainer__release',
        'method': '.method release(I)V',
        'method_name': 'release',
        'method_anchors': ['iget-object v0, p0, Lmiuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer;->mRefs:Ljava/util/Set;', 'invoke-static {p1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;', 'invoke-interface {v0, p1}, Ljava/util/Set;->remove(Ljava/lang/Object;)Z', 'if-eqz p1, :cond_0', 'iget-object p1, p0, Lmiuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer;->mRefs:Ljava/util/Set;', 'invoke-interface {p1}, Ljava/util/Set;->isEmpty()Z', 'if-eqz p1, :cond_0', 'iget-object p1, p0, Lmiuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer;->mSoundPlayer:Landroid/media/SoundPool;'],
        'type': 'method_replace',
        'search': """.method release(I)V
    .registers 3

    iget-object v0, p0, Lmiuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer;->mRefs:Ljava/util/Set;

    invoke-static {p1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p1

    invoke-interface {v0, p1}, Ljava/util/Set;->remove(Ljava/lang/Object;)Z

    move-result p1

    if-eqz p1, :cond_0

    iget-object p1, p0, Lmiuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer;->mRefs:Ljava/util/Set;

    invoke-interface {p1}, Ljava/util/Set;->isEmpty()Z

    move-result p1

    if-eqz p1, :cond_0

    iget-object p1, p0, Lmiuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer;->mSoundPlayer:Landroid/media/SoundPool;

    if-eqz p1, :cond_0

    invoke-virtual {p1}, Landroid/media/SoundPool;->release()V

    const/4 p1, 0x0

    iput-object p1, p0, Lmiuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer;->mSoundPlayer:Landroid/media/SoundPool;

    :cond_0
    return-void
.end method""",
        'replacement': """.method release(I)V
    .registers 3

    goto :goto_a

    nop

    :goto_0
    invoke-virtual {p1}, Landroid/media/SoundPool;->release()V

    goto :goto_6

    nop

    :goto_1
    iput-object p1, p0, Lmiuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer;->mSoundPlayer:Landroid/media/SoundPool;

    :goto_2
    goto :goto_d

    nop

    :goto_3
    if-nez p1, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_0

    nop

    :goto_4
    if-nez p1, :cond_1

    goto :goto_2

    :cond_1
    goto :goto_8

    nop

    :goto_5
    iget-object p1, p0, Lmiuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer;->mSoundPlayer:Landroid/media/SoundPool;

    goto :goto_3

    nop

    :goto_6
    const/4 p1, 0x0

    goto :goto_1

    nop

    :goto_7
    invoke-static {p1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p1

    goto :goto_c

    nop

    :goto_8
    iget-object p1, p0, Lmiuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer;->mRefs:Ljava/util/Set;

    goto :goto_b

    nop

    :goto_9
    if-nez p1, :cond_2

    goto :goto_2

    :cond_2
    goto :goto_5

    nop

    :goto_a
    iget-object v0, p0, Lmiuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer;->mRefs:Ljava/util/Set;

    goto :goto_7

    nop

    :goto_b
    invoke-interface {p1}, Ljava/util/Set;->isEmpty()Z

    move-result p1

    goto :goto_9

    nop

    :goto_c
    invoke-interface {v0, p1}, Ljava/util/Set;->remove(Ljava/lang/Object;)Z

    move-result p1

    goto :goto_4

    nop

    :goto_d
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
