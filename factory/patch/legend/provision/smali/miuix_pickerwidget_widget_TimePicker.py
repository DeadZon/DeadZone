TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/pickerwidget/widget/TimePicker.smali'
CLASS_FALLBACK_NAMES = ['TimePicker.smali']
CLASS_ANCHORS = ['.super Landroid/widget/FrameLayout;', '.field private static final NO_OP_CHANGE_LISTENER:Lmiuix/pickerwidget/widget/TimePicker$OnTimeChangedListener;']

PATCHES = [
    {
        'id': 'miuix_pickerwidget_widget_TimePicker__onConfigurationChanged',
        'method': '.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V',
        'method_name': 'onConfigurationChanged',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/widget/FrameLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V', 'iget-object p1, p1, Landroid/content/res/Configuration;->locale:Ljava/util/Locale;', 'invoke-direct {p0, p1}, Lmiuix/pickerwidget/widget/TimePicker;->setCurrentLocale(Ljava/util/Locale;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 2

    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    iget-object p1, p1, Landroid/content/res/Configuration;->locale:Ljava/util/Locale;

    invoke-direct {p0, p1}, Lmiuix/pickerwidget/widget/TimePicker;->setCurrentLocale(Ljava/util/Locale;)V

    return-void
.end method""",
        'replacement': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    goto :goto_1

    nop

    :goto_1
    iget-object p1, p1, Landroid/content/res/Configuration;->locale:Ljava/util/Locale;

    goto :goto_3

    nop

    :goto_2
    return-void

    :goto_3
    invoke-direct {p0, p1}, Lmiuix/pickerwidget/widget/TimePicker;->setCurrentLocale(Ljava/util/Locale;)V

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_pickerwidget_widget_TimePicker__onRestoreInstanceState',
        'method': '.method protected onRestoreInstanceState(Landroid/os/Parcelable;)V',
        'method_name': 'onRestoreInstanceState',
        'method_anchors': ['check-cast p1, Lmiuix/pickerwidget/widget/TimePicker$SavedState;', 'invoke-virtual {p1}, Landroid/view/View$BaseSavedState;->getSuperState()Landroid/os/Parcelable;', 'invoke-super {p0, v0}, Landroid/widget/FrameLayout;->onRestoreInstanceState(Landroid/os/Parcelable;)V', 'invoke-virtual {p1}, Lmiuix/pickerwidget/widget/TimePicker$SavedState;->getHour()I', 'invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;', 'invoke-virtual {p0, v0}, Lmiuix/pickerwidget/widget/TimePicker;->setCurrentHour(Ljava/lang/Integer;)V', 'invoke-virtual {p1}, Lmiuix/pickerwidget/widget/TimePicker$SavedState;->getMinute()I', 'invoke-static {p1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;'],
        'type': 'method_replace',
        'search': """.method protected onRestoreInstanceState(Landroid/os/Parcelable;)V
    .registers 3

    check-cast p1, Lmiuix/pickerwidget/widget/TimePicker$SavedState;

    invoke-virtual {p1}, Landroid/view/View$BaseSavedState;->getSuperState()Landroid/os/Parcelable;

    move-result-object v0

    invoke-super {p0, v0}, Landroid/widget/FrameLayout;->onRestoreInstanceState(Landroid/os/Parcelable;)V

    invoke-virtual {p1}, Lmiuix/pickerwidget/widget/TimePicker$SavedState;->getHour()I

    move-result v0

    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    invoke-virtual {p0, v0}, Lmiuix/pickerwidget/widget/TimePicker;->setCurrentHour(Ljava/lang/Integer;)V

    invoke-virtual {p1}, Lmiuix/pickerwidget/widget/TimePicker$SavedState;->getMinute()I

    move-result p1

    invoke-static {p1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p1

    invoke-virtual {p0, p1}, Lmiuix/pickerwidget/widget/TimePicker;->setCurrentMinute(Ljava/lang/Integer;)V

    return-void
.end method""",
        'replacement': """.method protected onRestoreInstanceState(Landroid/os/Parcelable;)V
    .registers 3

    goto :goto_9

    nop

    :goto_0
    invoke-virtual {p0, p1}, Lmiuix/pickerwidget/widget/TimePicker;->setCurrentMinute(Ljava/lang/Integer;)V

    goto :goto_8

    nop

    :goto_1
    invoke-virtual {p1}, Lmiuix/pickerwidget/widget/TimePicker$SavedState;->getMinute()I

    move-result p1

    goto :goto_4

    nop

    :goto_2
    invoke-virtual {p1}, Lmiuix/pickerwidget/widget/TimePicker$SavedState;->getHour()I

    move-result v0

    goto :goto_7

    nop

    :goto_3
    invoke-super {p0, v0}, Landroid/widget/FrameLayout;->onRestoreInstanceState(Landroid/os/Parcelable;)V

    goto :goto_2

    nop

    :goto_4
    invoke-static {p1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p1

    goto :goto_0

    nop

    :goto_5
    invoke-virtual {p0, v0}, Lmiuix/pickerwidget/widget/TimePicker;->setCurrentHour(Ljava/lang/Integer;)V

    goto :goto_1

    nop

    :goto_6
    invoke-virtual {p1}, Landroid/view/View$BaseSavedState;->getSuperState()Landroid/os/Parcelable;

    move-result-object v0

    goto :goto_3

    nop

    :goto_7
    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    goto :goto_5

    nop

    :goto_8
    return-void

    :goto_9
    check-cast p1, Lmiuix/pickerwidget/widget/TimePicker$SavedState;

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_pickerwidget_widget_TimePicker__onSaveInstanceState',
        'method': '.method protected onSaveInstanceState()Landroid/os/Parcelable;',
        'method_name': 'onSaveInstanceState',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/FrameLayout;->onSaveInstanceState()Landroid/os/Parcelable;', 'new-instance v1, Lmiuix/pickerwidget/widget/TimePicker$SavedState;', 'invoke-virtual {p0}, Lmiuix/pickerwidget/widget/TimePicker;->getCurrentHour()Ljava/lang/Integer;', 'invoke-virtual {v2}, Ljava/lang/Integer;->intValue()I', 'invoke-virtual {p0}, Lmiuix/pickerwidget/widget/TimePicker;->getCurrentMinute()Ljava/lang/Integer;', 'invoke-virtual {p0}, Ljava/lang/Integer;->intValue()I', 'invoke-direct {v1, v0, v2, p0, v3}, Lmiuix/pickerwidget/widget/TimePicker$SavedState;-><init>(Landroid/os/Parcelable;IILmiuix/pickerwidget/widget/TimePicker$1;)V', 'return-object v1'],
        'type': 'method_replace',
        'search': """.method protected onSaveInstanceState()Landroid/os/Parcelable;
    .registers 5

    invoke-super {p0}, Landroid/widget/FrameLayout;->onSaveInstanceState()Landroid/os/Parcelable;

    move-result-object v0

    new-instance v1, Lmiuix/pickerwidget/widget/TimePicker$SavedState;

    invoke-virtual {p0}, Lmiuix/pickerwidget/widget/TimePicker;->getCurrentHour()Ljava/lang/Integer;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/Integer;->intValue()I

    move-result v2

    invoke-virtual {p0}, Lmiuix/pickerwidget/widget/TimePicker;->getCurrentMinute()Ljava/lang/Integer;

    move-result-object p0

    invoke-virtual {p0}, Ljava/lang/Integer;->intValue()I

    move-result p0

    const/4 v3, 0x0

    invoke-direct {v1, v0, v2, p0, v3}, Lmiuix/pickerwidget/widget/TimePicker$SavedState;-><init>(Landroid/os/Parcelable;IILmiuix/pickerwidget/widget/TimePicker$1;)V

    return-object v1
.end method""",
        'replacement': """.method protected onSaveInstanceState()Landroid/os/Parcelable;
    .registers 5

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0}, Landroid/widget/FrameLayout;->onSaveInstanceState()Landroid/os/Parcelable;

    move-result-object v0

    goto :goto_6

    nop

    :goto_1
    invoke-virtual {p0}, Ljava/lang/Integer;->intValue()I

    move-result p0

    goto :goto_2

    nop

    :goto_2
    const/4 v3, 0x0

    goto :goto_3

    nop

    :goto_3
    invoke-direct {v1, v0, v2, p0, v3}, Lmiuix/pickerwidget/widget/TimePicker$SavedState;-><init>(Landroid/os/Parcelable;IILmiuix/pickerwidget/widget/TimePicker$1;)V

    goto :goto_5

    nop

    :goto_4
    invoke-virtual {v2}, Ljava/lang/Integer;->intValue()I

    move-result v2

    goto :goto_8

    nop

    :goto_5
    return-object v1

    :goto_6
    new-instance v1, Lmiuix/pickerwidget/widget/TimePicker$SavedState;

    goto :goto_7

    nop

    :goto_7
    invoke-virtual {p0}, Lmiuix/pickerwidget/widget/TimePicker;->getCurrentHour()Ljava/lang/Integer;

    move-result-object v2

    goto :goto_4

    nop

    :goto_8
    invoke-virtual {p0}, Lmiuix/pickerwidget/widget/TimePicker;->getCurrentMinute()Ljava/lang/Integer;

    move-result-object p0

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
