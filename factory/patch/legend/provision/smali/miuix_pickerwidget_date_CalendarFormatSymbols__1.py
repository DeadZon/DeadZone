TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/pickerwidget/date/CalendarFormatSymbols$1.smali'
CLASS_FALLBACK_NAMES = ['CalendarFormatSymbols$1.smali']
CLASS_ANCHORS = ['.super Lmiuix/core/util/SoftReferenceSingleton;']

PATCHES = [
    {
        'id': 'miuix_pickerwidget_date_CalendarFormatSymbols__1__createInstance',
        'method': '.method protected bridge synthetic createInstance(Ljava/lang/Object;)Ljava/lang/Object;',
        'method_name': 'createInstance',
        'method_anchors': ['invoke-virtual {p0, p1}, Lmiuix/pickerwidget/date/CalendarFormatSymbols$1;->createInstance(Ljava/lang/Object;)Lmiuix/pickerwidget/date/CalendarFormatSymbols;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected bridge synthetic createInstance(Ljava/lang/Object;)Ljava/lang/Object;
    .registers 2

    invoke-virtual {p0, p1}, Lmiuix/pickerwidget/date/CalendarFormatSymbols$1;->createInstance(Ljava/lang/Object;)Lmiuix/pickerwidget/date/CalendarFormatSymbols;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected bridge synthetic createInstance(Ljava/lang/Object;)Ljava/lang/Object;
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    invoke-virtual {p0, p1}, Lmiuix/pickerwidget/date/CalendarFormatSymbols$1;->createInstance(Ljava/lang/Object;)Lmiuix/pickerwidget/date/CalendarFormatSymbols;

    move-result-object p0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_pickerwidget_date_CalendarFormatSymbols__1__updateInstance',
        'method': '.method protected bridge synthetic updateInstance(Ljava/lang/Object;Ljava/lang/Object;)V',
        'method_name': 'updateInstance',
        'method_anchors': ['check-cast p1, Lmiuix/pickerwidget/date/CalendarFormatSymbols;', 'invoke-virtual {p0, p1, p2}, Lmiuix/pickerwidget/date/CalendarFormatSymbols$1;->updateInstance(Lmiuix/pickerwidget/date/CalendarFormatSymbols;Ljava/lang/Object;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected bridge synthetic updateInstance(Ljava/lang/Object;Ljava/lang/Object;)V
    .registers 3

    check-cast p1, Lmiuix/pickerwidget/date/CalendarFormatSymbols;

    invoke-virtual {p0, p1, p2}, Lmiuix/pickerwidget/date/CalendarFormatSymbols$1;->updateInstance(Lmiuix/pickerwidget/date/CalendarFormatSymbols;Ljava/lang/Object;)V

    return-void
.end method""",
        'replacement': """.method protected bridge synthetic updateInstance(Ljava/lang/Object;Ljava/lang/Object;)V
    .registers 3

    goto :goto_0

    nop

    :goto_0
    check-cast p1, Lmiuix/pickerwidget/date/CalendarFormatSymbols;

    goto :goto_2

    nop

    :goto_1
    return-void

    :goto_2
    invoke-virtual {p0, p1, p2}, Lmiuix/pickerwidget/date/CalendarFormatSymbols$1;->updateInstance(Lmiuix/pickerwidget/date/CalendarFormatSymbols;Ljava/lang/Object;)V

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_pickerwidget_date_CalendarFormatSymbols__1__createInstance',
        'method': '.method protected createInstance(Ljava/lang/Object;)Lmiuix/pickerwidget/date/CalendarFormatSymbols;',
        'method_name': 'createInstance',
        'method_anchors': ['new-instance p0, Lmiuix/pickerwidget/date/CalendarFormatSymbols;', 'check-cast p1, Landroid/content/Context;', 'invoke-direct {p0, p1, v0}, Lmiuix/pickerwidget/date/CalendarFormatSymbols;-><init>(Landroid/content/Context;Lmiuix/pickerwidget/date/CalendarFormatSymbols$1;)V', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected createInstance(Ljava/lang/Object;)Lmiuix/pickerwidget/date/CalendarFormatSymbols;
    .registers 3

    new-instance p0, Lmiuix/pickerwidget/date/CalendarFormatSymbols;

    check-cast p1, Landroid/content/Context;

    const/4 v0, 0x0

    invoke-direct {p0, p1, v0}, Lmiuix/pickerwidget/date/CalendarFormatSymbols;-><init>(Landroid/content/Context;Lmiuix/pickerwidget/date/CalendarFormatSymbols$1;)V

    return-object p0
.end method""",
        'replacement': """.method protected createInstance(Ljava/lang/Object;)Lmiuix/pickerwidget/date/CalendarFormatSymbols;
    .registers 3

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    new-instance p0, Lmiuix/pickerwidget/date/CalendarFormatSymbols;

    goto :goto_3

    nop

    :goto_2
    invoke-direct {p0, p1, v0}, Lmiuix/pickerwidget/date/CalendarFormatSymbols;-><init>(Landroid/content/Context;Lmiuix/pickerwidget/date/CalendarFormatSymbols$1;)V

    goto :goto_0

    nop

    :goto_3
    check-cast p1, Landroid/content/Context;

    goto :goto_4

    nop

    :goto_4
    const/4 v0, 0x0

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_pickerwidget_date_CalendarFormatSymbols__1__updateInstance',
        'method': '.method protected updateInstance(Lmiuix/pickerwidget/date/CalendarFormatSymbols;Ljava/lang/Object;)V',
        'method_name': 'updateInstance',
        'method_anchors': ['invoke-super {p0, p1, p2}, Lmiuix/core/util/SoftReferenceSingleton;->updateInstance(Ljava/lang/Object;Ljava/lang/Object;)V', 'check-cast p2, Landroid/content/Context;', 'invoke-static {p1, p2}, Lmiuix/pickerwidget/date/CalendarFormatSymbols;->access$100(Lmiuix/pickerwidget/date/CalendarFormatSymbols;Landroid/content/Context;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected updateInstance(Lmiuix/pickerwidget/date/CalendarFormatSymbols;Ljava/lang/Object;)V
    .registers 3

    invoke-super {p0, p1, p2}, Lmiuix/core/util/SoftReferenceSingleton;->updateInstance(Ljava/lang/Object;Ljava/lang/Object;)V

    check-cast p2, Landroid/content/Context;

    invoke-static {p1, p2}, Lmiuix/pickerwidget/date/CalendarFormatSymbols;->access$100(Lmiuix/pickerwidget/date/CalendarFormatSymbols;Landroid/content/Context;)V

    return-void
.end method""",
        'replacement': """.method protected updateInstance(Lmiuix/pickerwidget/date/CalendarFormatSymbols;Ljava/lang/Object;)V
    .registers 3

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0, p1, p2}, Lmiuix/core/util/SoftReferenceSingleton;->updateInstance(Ljava/lang/Object;Ljava/lang/Object;)V

    goto :goto_2

    nop

    :goto_1
    invoke-static {p1, p2}, Lmiuix/pickerwidget/date/CalendarFormatSymbols;->access$100(Lmiuix/pickerwidget/date/CalendarFormatSymbols;Landroid/content/Context;)V

    goto :goto_3

    nop

    :goto_2
    check-cast p2, Landroid/content/Context;

    goto :goto_1

    nop

    :goto_3
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
