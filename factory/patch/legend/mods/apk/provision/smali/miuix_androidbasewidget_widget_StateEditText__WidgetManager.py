TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/androidbasewidget/widget/StateEditText$WidgetManager.smali'
CLASS_FALLBACK_NAMES = ['StateEditText$WidgetManager.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'miuix_androidbasewidget_widget_StateEditText__WidgetManager__onAttached',
        'method': '.method protected onAttached(Lmiuix/androidbasewidget/widget/StateEditText;)V',
        'method_name': 'onAttached',
        'method_anchors': ['return-void'],
        'type': 'method_replace',
        'search': """.method protected onAttached(Lmiuix/androidbasewidget/widget/StateEditText;)V
    .registers 2

    return-void
.end method""",
        'replacement': """.method protected onAttached(Lmiuix/androidbasewidget/widget/StateEditText;)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_androidbasewidget_widget_StateEditText__WidgetManager__onDetached',
        'method': '.method protected onDetached()V',
        'method_name': 'onDetached',
        'method_anchors': ['return-void'],
        'type': 'method_replace',
        'search': """.method protected onDetached()V
    .registers 1

    return-void
.end method""",
        'replacement': """.method protected onDetached()V
    .registers 1

    goto :goto_0

    nop

    :goto_0
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
