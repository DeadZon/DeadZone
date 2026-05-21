TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/pickerwidget/widget/DateTimePicker.smali'
CLASS_FALLBACK_NAMES = ['DateTimePicker.smali']
CLASS_ANCHORS = ['.super Landroid/widget/LinearLayout;', '.field private static final sCalCache:Ljava/lang/ThreadLocal;']

PATCHES = [
    {
        'id': 'miuix_pickerwidget_widget_DateTimePicker__dispatchRestoreInstanceState',
        'method': '.method protected dispatchRestoreInstanceState(Landroid/util/SparseArray;)V',
        'method_name': 'dispatchRestoreInstanceState',
        'method_anchors': ['invoke-virtual {p0, p1}, Landroid/widget/LinearLayout;->dispatchThawSelfOnly(Landroid/util/SparseArray;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected dispatchRestoreInstanceState(Landroid/util/SparseArray;)V
    .registers 2

    invoke-virtual {p0, p1}, Landroid/widget/LinearLayout;->dispatchThawSelfOnly(Landroid/util/SparseArray;)V

    return-void
.end method""",
        'replacement': """.method protected dispatchRestoreInstanceState(Landroid/util/SparseArray;)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    invoke-virtual {p0, p1}, Landroid/widget/LinearLayout;->dispatchThawSelfOnly(Landroid/util/SparseArray;)V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_pickerwidget_widget_DateTimePicker__onRestoreInstanceState',
        'method': '.method protected onRestoreInstanceState(Landroid/os/Parcelable;)V',
        'method_name': 'onRestoreInstanceState',
        'method_anchors': ['check-cast p1, Lmiuix/pickerwidget/widget/DateTimePicker$SavedState;', 'invoke-virtual {p1}, Landroid/view/View$BaseSavedState;->getSuperState()Landroid/os/Parcelable;', 'invoke-super {p0, v0}, Landroid/widget/LinearLayout;->onRestoreInstanceState(Landroid/os/Parcelable;)V', 'invoke-static {p1}, Lmiuix/pickerwidget/widget/DateTimePicker$SavedState;->access$100(Lmiuix/pickerwidget/widget/DateTimePicker$SavedState;)Z', 'iput-boolean v0, p0, Lmiuix/pickerwidget/widget/DateTimePicker;->mIsLunarMode:Z', 'invoke-virtual {p1}, Lmiuix/pickerwidget/widget/DateTimePicker$SavedState;->getTimeInMillis()J', 'invoke-virtual {p0, v0, v1}, Lmiuix/pickerwidget/widget/DateTimePicker;->update(J)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onRestoreInstanceState(Landroid/os/Parcelable;)V
    .registers 4

    check-cast p1, Lmiuix/pickerwidget/widget/DateTimePicker$SavedState;

    invoke-virtual {p1}, Landroid/view/View$BaseSavedState;->getSuperState()Landroid/os/Parcelable;

    move-result-object v0

    invoke-super {p0, v0}, Landroid/widget/LinearLayout;->onRestoreInstanceState(Landroid/os/Parcelable;)V

    invoke-static {p1}, Lmiuix/pickerwidget/widget/DateTimePicker$SavedState;->access$100(Lmiuix/pickerwidget/widget/DateTimePicker$SavedState;)Z

    move-result v0

    iput-boolean v0, p0, Lmiuix/pickerwidget/widget/DateTimePicker;->mIsLunarMode:Z

    invoke-virtual {p1}, Lmiuix/pickerwidget/widget/DateTimePicker$SavedState;->getTimeInMillis()J

    move-result-wide v0

    invoke-virtual {p0, v0, v1}, Lmiuix/pickerwidget/widget/DateTimePicker;->update(J)V

    return-void
.end method""",
        'replacement': """.method protected onRestoreInstanceState(Landroid/os/Parcelable;)V
    .registers 4

    goto :goto_0

    nop

    :goto_0
    check-cast p1, Lmiuix/pickerwidget/widget/DateTimePicker$SavedState;

    goto :goto_5

    nop

    :goto_1
    return-void

    :goto_2
    invoke-virtual {p0, v0, v1}, Lmiuix/pickerwidget/widget/DateTimePicker;->update(J)V

    goto :goto_1

    nop

    :goto_3
    invoke-super {p0, v0}, Landroid/widget/LinearLayout;->onRestoreInstanceState(Landroid/os/Parcelable;)V

    goto :goto_7

    nop

    :goto_4
    iput-boolean v0, p0, Lmiuix/pickerwidget/widget/DateTimePicker;->mIsLunarMode:Z

    goto :goto_6

    nop

    :goto_5
    invoke-virtual {p1}, Landroid/view/View$BaseSavedState;->getSuperState()Landroid/os/Parcelable;

    move-result-object v0

    goto :goto_3

    nop

    :goto_6
    invoke-virtual {p1}, Lmiuix/pickerwidget/widget/DateTimePicker$SavedState;->getTimeInMillis()J

    move-result-wide v0

    goto :goto_2

    nop

    :goto_7
    invoke-static {p1}, Lmiuix/pickerwidget/widget/DateTimePicker$SavedState;->access$100(Lmiuix/pickerwidget/widget/DateTimePicker$SavedState;)Z

    move-result v0

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_pickerwidget_widget_DateTimePicker__onSaveInstanceState',
        'method': '.method protected onSaveInstanceState()Landroid/os/Parcelable;',
        'method_name': 'onSaveInstanceState',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/LinearLayout;->onSaveInstanceState()Landroid/os/Parcelable;', 'new-instance v1, Lmiuix/pickerwidget/widget/DateTimePicker$SavedState;', 'invoke-virtual {p0}, Lmiuix/pickerwidget/widget/DateTimePicker;->getTimeInMillis()J', 'iget-boolean p0, p0, Lmiuix/pickerwidget/widget/DateTimePicker;->mIsLunarMode:Z', 'invoke-direct {v1, v0, v2, v3, p0}, Lmiuix/pickerwidget/widget/DateTimePicker$SavedState;-><init>(Landroid/os/Parcelable;JZ)V', 'return-object v1'],
        'type': 'method_replace',
        'search': """.method protected onSaveInstanceState()Landroid/os/Parcelable;
    .registers 5

    invoke-super {p0}, Landroid/widget/LinearLayout;->onSaveInstanceState()Landroid/os/Parcelable;

    move-result-object v0

    new-instance v1, Lmiuix/pickerwidget/widget/DateTimePicker$SavedState;

    invoke-virtual {p0}, Lmiuix/pickerwidget/widget/DateTimePicker;->getTimeInMillis()J

    move-result-wide v2

    iget-boolean p0, p0, Lmiuix/pickerwidget/widget/DateTimePicker;->mIsLunarMode:Z

    invoke-direct {v1, v0, v2, v3, p0}, Lmiuix/pickerwidget/widget/DateTimePicker$SavedState;-><init>(Landroid/os/Parcelable;JZ)V

    return-object v1
.end method""",
        'replacement': """.method protected onSaveInstanceState()Landroid/os/Parcelable;
    .registers 5

    goto :goto_2

    nop

    :goto_0
    return-object v1

    :goto_1
    new-instance v1, Lmiuix/pickerwidget/widget/DateTimePicker$SavedState;

    goto :goto_4

    nop

    :goto_2
    invoke-super {p0}, Landroid/widget/LinearLayout;->onSaveInstanceState()Landroid/os/Parcelable;

    move-result-object v0

    goto :goto_1

    nop

    :goto_3
    invoke-direct {v1, v0, v2, v3, p0}, Lmiuix/pickerwidget/widget/DateTimePicker$SavedState;-><init>(Landroid/os/Parcelable;JZ)V

    goto :goto_0

    nop

    :goto_4
    invoke-virtual {p0}, Lmiuix/pickerwidget/widget/DateTimePicker;->getTimeInMillis()J

    move-result-wide v2

    goto :goto_5

    nop

    :goto_5
    iget-boolean p0, p0, Lmiuix/pickerwidget/widget/DateTimePicker;->mIsLunarMode:Z

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
