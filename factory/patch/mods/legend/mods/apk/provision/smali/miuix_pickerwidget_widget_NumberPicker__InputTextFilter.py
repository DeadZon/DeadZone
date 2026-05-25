TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/pickerwidget/widget/NumberPicker$InputTextFilter.smali'
CLASS_FALLBACK_NAMES = ['NumberPicker$InputTextFilter.smali']
CLASS_ANCHORS = ['.super Landroid/text/method/NumberKeyListener;']

PATCHES = [
    {
        'id': 'miuix_pickerwidget_widget_NumberPicker__InputTextFilter__getAcceptedChars',
        'method': '.method protected getAcceptedChars()[C',
        'method_name': 'getAcceptedChars',
        'method_anchors': ['invoke-static {}, Lmiuix/pickerwidget/widget/NumberPicker;->access$600()[C', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getAcceptedChars()[C
    .registers 1

    invoke-static {}, Lmiuix/pickerwidget/widget/NumberPicker;->access$600()[C

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected getAcceptedChars()[C
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    invoke-static {}, Lmiuix/pickerwidget/widget/NumberPicker;->access$600()[C

    move-result-object p0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
