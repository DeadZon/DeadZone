TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/widget/CustomVideoView.smali'
CLASS_FALLBACK_NAMES = ['CustomVideoView.smali']
CLASS_ANCHORS = ['.super Landroid/widget/VideoView;']

PATCHES = [
    {
        'id': 'com_android_provision_widget_CustomVideoView__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['invoke-virtual {p0}, Landroid/widget/VideoView;->getWidth()I', 'invoke-static {v0, p1}, Landroid/widget/VideoView;->getDefaultSize(II)I', 'invoke-virtual {p0}, Landroid/widget/VideoView;->getHeight()I', 'invoke-static {v0, p2}, Landroid/widget/VideoView;->getDefaultSize(II)I', 'invoke-virtual {p0, p1, p2}, Landroid/widget/VideoView;->setMeasuredDimension(II)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 4

    invoke-virtual {p0}, Landroid/widget/VideoView;->getWidth()I

    move-result v0

    invoke-static {v0, p1}, Landroid/widget/VideoView;->getDefaultSize(II)I

    move-result p1

    invoke-virtual {p0}, Landroid/widget/VideoView;->getHeight()I

    move-result v0

    invoke-static {v0, p2}, Landroid/widget/VideoView;->getDefaultSize(II)I

    move-result p2

    invoke-virtual {p0, p1, p2}, Landroid/widget/VideoView;->setMeasuredDimension(II)V

    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 4

    goto :goto_2

    nop

    :goto_0
    invoke-virtual {p0, p1, p2}, Landroid/widget/VideoView;->setMeasuredDimension(II)V

    goto :goto_1

    nop

    :goto_1
    return-void

    :goto_2
    invoke-virtual {p0}, Landroid/widget/VideoView;->getWidth()I

    move-result v0

    goto :goto_4

    nop

    :goto_3
    invoke-virtual {p0}, Landroid/widget/VideoView;->getHeight()I

    move-result v0

    goto :goto_5

    nop

    :goto_4
    invoke-static {v0, p1}, Landroid/widget/VideoView;->getDefaultSize(II)I

    move-result p1

    goto :goto_3

    nop

    :goto_5
    invoke-static {v0, p2}, Landroid/widget/VideoView;->getDefaultSize(II)I

    move-result p2

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
