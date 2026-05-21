TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/pickerwidget/widget/DatePicker.smali'
CLASS_FALLBACK_NAMES = ['DatePicker.smali']
CLASS_ANCHORS = ['.super Landroid/widget/FrameLayout;', '.field private static final LOG_TAG:Ljava/lang/String;']

PATCHES = [
    {
        'id': 'miuix_pickerwidget_widget_DatePicker__dispatchRestoreInstanceState',
        'method': '.method protected dispatchRestoreInstanceState(Landroid/util/SparseArray;)V',
        'method_name': 'dispatchRestoreInstanceState',
        'method_anchors': ['invoke-virtual {p0, p1}, Landroid/widget/FrameLayout;->dispatchThawSelfOnly(Landroid/util/SparseArray;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected dispatchRestoreInstanceState(Landroid/util/SparseArray;)V
    .registers 2

    invoke-virtual {p0, p1}, Landroid/widget/FrameLayout;->dispatchThawSelfOnly(Landroid/util/SparseArray;)V

    return-void
.end method""",
        'replacement': """.method protected dispatchRestoreInstanceState(Landroid/util/SparseArray;)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    invoke-virtual {p0, p1}, Landroid/widget/FrameLayout;->dispatchThawSelfOnly(Landroid/util/SparseArray;)V

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
        'id': 'miuix_pickerwidget_widget_DatePicker__onConfigurationChanged',
        'method': '.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V',
        'method_name': 'onConfigurationChanged',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/widget/FrameLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V', 'iget-object p1, p1, Landroid/content/res/Configuration;->locale:Ljava/util/Locale;', 'invoke-direct {p0, p1}, Lmiuix/pickerwidget/widget/DatePicker;->setCurrentLocale(Ljava/util/Locale;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 2

    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    iget-object p1, p1, Landroid/content/res/Configuration;->locale:Ljava/util/Locale;

    invoke-direct {p0, p1}, Lmiuix/pickerwidget/widget/DatePicker;->setCurrentLocale(Ljava/util/Locale;)V

    return-void
.end method""",
        'replacement': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    goto :goto_2

    nop

    :goto_1
    return-void

    :goto_2
    iget-object p1, p1, Landroid/content/res/Configuration;->locale:Ljava/util/Locale;

    goto :goto_3

    nop

    :goto_3
    invoke-direct {p0, p1}, Lmiuix/pickerwidget/widget/DatePicker;->setCurrentLocale(Ljava/util/Locale;)V

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_pickerwidget_widget_DatePicker__onRestoreInstanceState',
        'method': '.method protected onRestoreInstanceState(Landroid/os/Parcelable;)V',
        'method_name': 'onRestoreInstanceState',
        'method_anchors': ['check-cast p1, Lmiuix/pickerwidget/widget/DatePicker$SavedState;', 'invoke-virtual {p1}, Landroid/view/View$BaseSavedState;->getSuperState()Landroid/os/Parcelable;', 'invoke-super {p0, v0}, Landroid/widget/FrameLayout;->onRestoreInstanceState(Landroid/os/Parcelable;)V', 'invoke-static {p1}, Lmiuix/pickerwidget/widget/DatePicker$SavedState;->access$1100(Lmiuix/pickerwidget/widget/DatePicker$SavedState;)I', 'invoke-static {p1}, Lmiuix/pickerwidget/widget/DatePicker$SavedState;->access$1200(Lmiuix/pickerwidget/widget/DatePicker$SavedState;)I', 'invoke-static {p1}, Lmiuix/pickerwidget/widget/DatePicker$SavedState;->access$1300(Lmiuix/pickerwidget/widget/DatePicker$SavedState;)I', 'invoke-direct {p0, v0, v1, v2}, Lmiuix/pickerwidget/widget/DatePicker;->setDate(III)V', 'iget-boolean v0, p0, Lmiuix/pickerwidget/widget/DatePicker;->mIsLunarMode:Z'],
        'type': 'method_replace',
        'search': """.method protected onRestoreInstanceState(Landroid/os/Parcelable;)V
    .registers 5

    check-cast p1, Lmiuix/pickerwidget/widget/DatePicker$SavedState;

    invoke-virtual {p1}, Landroid/view/View$BaseSavedState;->getSuperState()Landroid/os/Parcelable;

    move-result-object v0

    invoke-super {p0, v0}, Landroid/widget/FrameLayout;->onRestoreInstanceState(Landroid/os/Parcelable;)V

    invoke-static {p1}, Lmiuix/pickerwidget/widget/DatePicker$SavedState;->access$1100(Lmiuix/pickerwidget/widget/DatePicker$SavedState;)I

    move-result v0

    invoke-static {p1}, Lmiuix/pickerwidget/widget/DatePicker$SavedState;->access$1200(Lmiuix/pickerwidget/widget/DatePicker$SavedState;)I

    move-result v1

    invoke-static {p1}, Lmiuix/pickerwidget/widget/DatePicker$SavedState;->access$1300(Lmiuix/pickerwidget/widget/DatePicker$SavedState;)I

    move-result v2

    invoke-direct {p0, v0, v1, v2}, Lmiuix/pickerwidget/widget/DatePicker;->setDate(III)V

    iget-boolean v0, p0, Lmiuix/pickerwidget/widget/DatePicker;->mIsLunarMode:Z

    invoke-static {p1}, Lmiuix/pickerwidget/widget/DatePicker$SavedState;->access$1400(Lmiuix/pickerwidget/widget/DatePicker$SavedState;)Z

    move-result v1

    if-eq v0, v1, :cond_0

    invoke-static {p1}, Lmiuix/pickerwidget/widget/DatePicker$SavedState;->access$1400(Lmiuix/pickerwidget/widget/DatePicker$SavedState;)Z

    move-result p1

    iput-boolean p1, p0, Lmiuix/pickerwidget/widget/DatePicker;->mIsLunarMode:Z

    invoke-direct {p0}, Lmiuix/pickerwidget/widget/DatePicker;->resetMonthsDisplayedValues()V

    :cond_0
    invoke-direct {p0}, Lmiuix/pickerwidget/widget/DatePicker;->updateSpinners()V

    return-void
.end method""",
        'replacement': """.method protected onRestoreInstanceState(Landroid/os/Parcelable;)V
    .registers 5

    goto :goto_f

    nop

    :goto_0
    invoke-static {p1}, Lmiuix/pickerwidget/widget/DatePicker$SavedState;->access$1200(Lmiuix/pickerwidget/widget/DatePicker$SavedState;)I

    move-result v1

    goto :goto_6

    nop

    :goto_1
    invoke-virtual {p1}, Landroid/view/View$BaseSavedState;->getSuperState()Landroid/os/Parcelable;

    move-result-object v0

    goto :goto_c

    nop

    :goto_2
    invoke-direct {p0}, Lmiuix/pickerwidget/widget/DatePicker;->updateSpinners()V

    goto :goto_b

    nop

    :goto_3
    invoke-direct {p0, v0, v1, v2}, Lmiuix/pickerwidget/widget/DatePicker;->setDate(III)V

    goto :goto_5

    nop

    :goto_4
    if-ne v0, v1, :cond_0

    goto :goto_9

    :cond_0
    goto :goto_a

    nop

    :goto_5
    iget-boolean v0, p0, Lmiuix/pickerwidget/widget/DatePicker;->mIsLunarMode:Z

    goto :goto_d

    nop

    :goto_6
    invoke-static {p1}, Lmiuix/pickerwidget/widget/DatePicker$SavedState;->access$1300(Lmiuix/pickerwidget/widget/DatePicker$SavedState;)I

    move-result v2

    goto :goto_3

    nop

    :goto_7
    iput-boolean p1, p0, Lmiuix/pickerwidget/widget/DatePicker;->mIsLunarMode:Z

    goto :goto_8

    nop

    :goto_8
    invoke-direct {p0}, Lmiuix/pickerwidget/widget/DatePicker;->resetMonthsDisplayedValues()V

    :goto_9
    goto :goto_2

    nop

    :goto_a
    invoke-static {p1}, Lmiuix/pickerwidget/widget/DatePicker$SavedState;->access$1400(Lmiuix/pickerwidget/widget/DatePicker$SavedState;)Z

    move-result p1

    goto :goto_7

    nop

    :goto_b
    return-void

    :goto_c
    invoke-super {p0, v0}, Landroid/widget/FrameLayout;->onRestoreInstanceState(Landroid/os/Parcelable;)V

    goto :goto_e

    nop

    :goto_d
    invoke-static {p1}, Lmiuix/pickerwidget/widget/DatePicker$SavedState;->access$1400(Lmiuix/pickerwidget/widget/DatePicker$SavedState;)Z

    move-result v1

    goto :goto_4

    nop

    :goto_e
    invoke-static {p1}, Lmiuix/pickerwidget/widget/DatePicker$SavedState;->access$1100(Lmiuix/pickerwidget/widget/DatePicker$SavedState;)I

    move-result v0

    goto :goto_0

    nop

    :goto_f
    check-cast p1, Lmiuix/pickerwidget/widget/DatePicker$SavedState;

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_pickerwidget_widget_DatePicker__onSaveInstanceState',
        'method': '.method protected onSaveInstanceState()Landroid/os/Parcelable;',
        'method_name': 'onSaveInstanceState',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/FrameLayout;->onSaveInstanceState()Landroid/os/Parcelable;', 'iget-object v0, p0, Lmiuix/pickerwidget/widget/DatePicker;->mCurrentDate:Lmiuix/pickerwidget/date/Calendar;', 'invoke-virtual {v0, v2}, Lmiuix/pickerwidget/date/Calendar;->get(I)I', 'iget-object v0, p0, Lmiuix/pickerwidget/widget/DatePicker;->mCurrentDate:Lmiuix/pickerwidget/date/Calendar;', 'invoke-virtual {v0, v3}, Lmiuix/pickerwidget/date/Calendar;->get(I)I', 'iget-object v0, p0, Lmiuix/pickerwidget/widget/DatePicker;->mCurrentDate:Lmiuix/pickerwidget/date/Calendar;', 'invoke-virtual {v0, v4}, Lmiuix/pickerwidget/date/Calendar;->get(I)I', 'new-instance v0, Lmiuix/pickerwidget/widget/DatePicker$SavedState;'],
        'type': 'method_replace',
        'search': """.method protected onSaveInstanceState()Landroid/os/Parcelable;
    .registers 8

    invoke-super {p0}, Landroid/widget/FrameLayout;->onSaveInstanceState()Landroid/os/Parcelable;

    move-result-object v1

    iget-object v0, p0, Lmiuix/pickerwidget/widget/DatePicker;->mCurrentDate:Lmiuix/pickerwidget/date/Calendar;

    const/4 v2, 0x1

    invoke-virtual {v0, v2}, Lmiuix/pickerwidget/date/Calendar;->get(I)I

    move-result v2

    iget-object v0, p0, Lmiuix/pickerwidget/widget/DatePicker;->mCurrentDate:Lmiuix/pickerwidget/date/Calendar;

    const/4 v3, 0x5

    invoke-virtual {v0, v3}, Lmiuix/pickerwidget/date/Calendar;->get(I)I

    move-result v3

    iget-object v0, p0, Lmiuix/pickerwidget/widget/DatePicker;->mCurrentDate:Lmiuix/pickerwidget/date/Calendar;

    const/16 v4, 0x9

    invoke-virtual {v0, v4}, Lmiuix/pickerwidget/date/Calendar;->get(I)I

    move-result v4

    new-instance v0, Lmiuix/pickerwidget/widget/DatePicker$SavedState;

    iget-boolean v5, p0, Lmiuix/pickerwidget/widget/DatePicker;->mIsLunarMode:Z

    const/4 v6, 0x0

    invoke-direct/range {v0 .. v6}, Lmiuix/pickerwidget/widget/DatePicker$SavedState;-><init>(Landroid/os/Parcelable;IIIZLmiuix/pickerwidget/widget/DatePicker$1;)V

    return-object v0
.end method""",
        'replacement': """.method protected onSaveInstanceState()Landroid/os/Parcelable;
    .registers 8

    goto :goto_1

    nop

    :goto_0
    iget-boolean v5, p0, Lmiuix/pickerwidget/widget/DatePicker;->mIsLunarMode:Z

    goto :goto_b

    nop

    :goto_1
    invoke-super {p0}, Landroid/widget/FrameLayout;->onSaveInstanceState()Landroid/os/Parcelable;

    move-result-object v1

    goto :goto_5

    nop

    :goto_2
    invoke-virtual {v0, v2}, Lmiuix/pickerwidget/date/Calendar;->get(I)I

    move-result v2

    goto :goto_c

    nop

    :goto_3
    invoke-virtual {v0, v3}, Lmiuix/pickerwidget/date/Calendar;->get(I)I

    move-result v3

    goto :goto_6

    nop

    :goto_4
    const/4 v3, 0x5

    goto :goto_3

    nop

    :goto_5
    iget-object v0, p0, Lmiuix/pickerwidget/widget/DatePicker;->mCurrentDate:Lmiuix/pickerwidget/date/Calendar;

    goto :goto_a

    nop

    :goto_6
    iget-object v0, p0, Lmiuix/pickerwidget/widget/DatePicker;->mCurrentDate:Lmiuix/pickerwidget/date/Calendar;

    goto :goto_d

    nop

    :goto_7
    invoke-virtual {v0, v4}, Lmiuix/pickerwidget/date/Calendar;->get(I)I

    move-result v4

    goto :goto_e

    nop

    :goto_8
    return-object v0

    :goto_9
    invoke-direct/range {v0 .. v6}, Lmiuix/pickerwidget/widget/DatePicker$SavedState;-><init>(Landroid/os/Parcelable;IIIZLmiuix/pickerwidget/widget/DatePicker$1;)V

    goto :goto_8

    nop

    :goto_a
    const/4 v2, 0x1

    goto :goto_2

    nop

    :goto_b
    const/4 v6, 0x0

    goto :goto_9

    nop

    :goto_c
    iget-object v0, p0, Lmiuix/pickerwidget/widget/DatePicker;->mCurrentDate:Lmiuix/pickerwidget/date/Calendar;

    goto :goto_4

    nop

    :goto_d
    const/16 v4, 0x9

    goto :goto_7

    nop

    :goto_e
    new-instance v0, Lmiuix/pickerwidget/widget/DatePicker$SavedState;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
