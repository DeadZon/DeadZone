TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/pickerwidget/widget/NumberPicker$SoundPlayHandler.smali'
CLASS_FALLBACK_NAMES = ['NumberPicker$SoundPlayHandler.smali']
CLASS_ANCHORS = ['.super Landroid/os/Handler;', '.field private static final sPlayerContainer:Lmiuix/pickerwidget/widget/NumberPicker$SoundPlayHandler$SoundPlayerContainer;']

PATCHES = [
    {
        'id': 'miuix_pickerwidget_widget_NumberPicker__SoundPlayHandler__init',
        'method': '.method init(Landroid/content/Context;I)V',
        'method_name': 'init',
        'method_anchors': ['invoke-virtual {p0, v0, p2, v0}, Landroid/os/Handler;->obtainMessage(III)Landroid/os/Message;', 'iput-object p1, p2, Landroid/os/Message;->obj:Ljava/lang/Object;', 'invoke-virtual {p0, p2}, Landroid/os/Handler;->sendMessage(Landroid/os/Message;)Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method init(Landroid/content/Context;I)V
    .registers 4

    const/4 v0, 0x0

    invoke-virtual {p0, v0, p2, v0}, Landroid/os/Handler;->obtainMessage(III)Landroid/os/Message;

    move-result-object p2

    iput-object p1, p2, Landroid/os/Message;->obj:Ljava/lang/Object;

    invoke-virtual {p0, p2}, Landroid/os/Handler;->sendMessage(Landroid/os/Message;)Z

    return-void
.end method""",
        'replacement': """.method init(Landroid/content/Context;I)V
    .registers 4

    goto :goto_2

    nop

    :goto_0
    invoke-virtual {p0, p2}, Landroid/os/Handler;->sendMessage(Landroid/os/Message;)Z

    goto :goto_3

    nop

    :goto_1
    invoke-virtual {p0, v0, p2, v0}, Landroid/os/Handler;->obtainMessage(III)Landroid/os/Message;

    move-result-object p2

    goto :goto_4

    nop

    :goto_2
    const/4 v0, 0x0

    goto :goto_1

    nop

    :goto_3
    return-void

    :goto_4
    iput-object p1, p2, Landroid/os/Message;->obj:Ljava/lang/Object;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_pickerwidget_widget_NumberPicker__SoundPlayHandler__play',
        'method': '.method play()V',
        'method_name': 'play',
        'method_anchors': ['invoke-virtual {p0, v0}, Landroid/os/Handler;->obtainMessage(I)Landroid/os/Message;', 'invoke-virtual {p0, v0}, Landroid/os/Handler;->sendMessage(Landroid/os/Message;)Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method play()V
    .registers 2

    const/4 v0, 0x1

    invoke-virtual {p0, v0}, Landroid/os/Handler;->obtainMessage(I)Landroid/os/Message;

    move-result-object v0

    invoke-virtual {p0, v0}, Landroid/os/Handler;->sendMessage(Landroid/os/Message;)Z

    return-void
.end method""",
        'replacement': """.method play()V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    const/4 v0, 0x1

    goto :goto_2

    nop

    :goto_2
    invoke-virtual {p0, v0}, Landroid/os/Handler;->obtainMessage(I)Landroid/os/Message;

    move-result-object v0

    goto :goto_3

    nop

    :goto_3
    invoke-virtual {p0, v0}, Landroid/os/Handler;->sendMessage(Landroid/os/Message;)Z

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_pickerwidget_widget_NumberPicker__SoundPlayHandler__release',
        'method': '.method release(I)V',
        'method_name': 'release',
        'method_anchors': ['invoke-virtual {p0, v0, p1, v1}, Landroid/os/Handler;->obtainMessage(III)Landroid/os/Message;', 'invoke-virtual {p0, p1}, Landroid/os/Handler;->sendMessage(Landroid/os/Message;)Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method release(I)V
    .registers 4

    const/4 v0, 0x2

    const/4 v1, 0x0

    invoke-virtual {p0, v0, p1, v1}, Landroid/os/Handler;->obtainMessage(III)Landroid/os/Message;

    move-result-object p1

    invoke-virtual {p0, p1}, Landroid/os/Handler;->sendMessage(Landroid/os/Message;)Z

    return-void
.end method""",
        'replacement': """.method release(I)V
    .registers 4

    goto :goto_3

    nop

    :goto_0
    invoke-virtual {p0, p1}, Landroid/os/Handler;->sendMessage(Landroid/os/Message;)Z

    goto :goto_4

    nop

    :goto_1
    invoke-virtual {p0, v0, p1, v1}, Landroid/os/Handler;->obtainMessage(III)Landroid/os/Message;

    move-result-object p1

    goto :goto_0

    nop

    :goto_2
    const/4 v1, 0x0

    goto :goto_1

    nop

    :goto_3
    const/4 v0, 0x2

    goto :goto_2

    nop

    :goto_4
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_pickerwidget_widget_NumberPicker__SoundPlayHandler__stop',
        'method': '.method stop()V',
        'method_name': 'stop',
        'method_anchors': ['invoke-virtual {p0, v0}, Landroid/os/Handler;->removeMessages(I)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method stop()V
    .registers 2

    const/4 v0, 0x1

    invoke-virtual {p0, v0}, Landroid/os/Handler;->removeMessages(I)V

    return-void
.end method""",
        'replacement': """.method stop()V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    const/4 v0, 0x1

    goto :goto_2

    nop

    :goto_2
    invoke-virtual {p0, v0}, Landroid/os/Handler;->removeMessages(I)V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
