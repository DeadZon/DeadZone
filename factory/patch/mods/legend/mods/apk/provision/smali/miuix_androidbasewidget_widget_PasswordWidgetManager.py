TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/androidbasewidget/widget/PasswordWidgetManager.smali'
CLASS_FALLBACK_NAMES = ['PasswordWidgetManager.smali']
CLASS_ANCHORS = ['.super Lmiuix/androidbasewidget/widget/StateEditText$WidgetManager;', '.field private static final CHECKED_STATE_SET:[I']

PATCHES = [
    {
        'id': 'miuix_androidbasewidget_widget_PasswordWidgetManager__onDetached',
        'method': '.method protected onDetached()V',
        'method_name': 'onDetached',
        'method_anchors': ['invoke-super {p0}, Lmiuix/androidbasewidget/widget/StateEditText$WidgetManager;->onDetached()V', 'iget-object p0, p0, Lmiuix/androidbasewidget/widget/PasswordWidgetManager;->mMaster:Lmiuix/androidbasewidget/widget/StateEditText;', 'if-eqz p0, :cond_0', 'invoke-virtual {p0, v0}, Landroid/widget/EditText;->setTransformationMethod(Landroid/text/method/TransformationMethod;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onDetached()V
    .registers 2

    invoke-super {p0}, Lmiuix/androidbasewidget/widget/StateEditText$WidgetManager;->onDetached()V

    iget-object p0, p0, Lmiuix/androidbasewidget/widget/PasswordWidgetManager;->mMaster:Lmiuix/androidbasewidget/widget/StateEditText;

    if-eqz p0, :cond_0

    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Landroid/widget/EditText;->setTransformationMethod(Landroid/text/method/TransformationMethod;)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onDetached()V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0}, Lmiuix/androidbasewidget/widget/StateEditText$WidgetManager;->onDetached()V

    goto :goto_6

    nop

    :goto_1
    invoke-virtual {p0, v0}, Landroid/widget/EditText;->setTransformationMethod(Landroid/text/method/TransformationMethod;)V

    :goto_2
    goto :goto_5

    nop

    :goto_3
    const/4 v0, 0x0

    goto :goto_1

    nop

    :goto_4
    if-nez p0, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_3

    nop

    :goto_5
    return-void

    :goto_6
    iget-object p0, p0, Lmiuix/androidbasewidget/widget/PasswordWidgetManager;->mMaster:Lmiuix/androidbasewidget/widget/StateEditText;

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_androidbasewidget_widget_PasswordWidgetManager__onPopulateNodeForVirtualView',
        'method': '.method protected onPopulateNodeForVirtualView(ILandroidx/core/view/accessibility/AccessibilityNodeInfoCompat;)V',
        'method_name': 'onPopulateNodeForVirtualView',
        'method_anchors': ['invoke-virtual {p2, p1}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setCheckable(Z)V', 'iget-boolean p1, p0, Lmiuix/androidbasewidget/widget/PasswordWidgetManager;->mIsChecked:Z', 'invoke-virtual {p2, p1}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setChecked(Z)V', 'invoke-virtual {p1}, Ljava/lang/Class;->getName()Ljava/lang/String;', 'invoke-virtual {p2, p1}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setClassName(Ljava/lang/CharSequence;)V', 'iget-object p0, p0, Lmiuix/androidbasewidget/widget/PasswordWidgetManager;->mContext:Landroid/content/Context;', 'sget p1, Lmiuix/androidbasewidget/R$string;->miuix_show_password:I', 'invoke-virtual {p0, p1}, Landroid/content/Context;->getString(I)Ljava/lang/String;'],
        'type': 'method_replace',
        'search': """.method protected onPopulateNodeForVirtualView(ILandroidx/core/view/accessibility/AccessibilityNodeInfoCompat;)V
    .registers 3

    const/4 p1, 0x1

    invoke-virtual {p2, p1}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setCheckable(Z)V

    iget-boolean p1, p0, Lmiuix/androidbasewidget/widget/PasswordWidgetManager;->mIsChecked:Z

    invoke-virtual {p2, p1}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setChecked(Z)V

    const-class p1, Landroid/widget/Switch;

    invoke-virtual {p1}, Ljava/lang/Class;->getName()Ljava/lang/String;

    move-result-object p1

    invoke-virtual {p2, p1}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setClassName(Ljava/lang/CharSequence;)V

    iget-object p0, p0, Lmiuix/androidbasewidget/widget/PasswordWidgetManager;->mContext:Landroid/content/Context;

    sget p1, Lmiuix/androidbasewidget/R$string;->miuix_show_password:I

    invoke-virtual {p0, p1}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object p0

    invoke-virtual {p2, p0}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setContentDescription(Ljava/lang/CharSequence;)V

    return-void
.end method""",
        'replacement': """.method protected onPopulateNodeForVirtualView(ILandroidx/core/view/accessibility/AccessibilityNodeInfoCompat;)V
    .registers 3

    goto :goto_1

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/androidbasewidget/widget/PasswordWidgetManager;->mContext:Landroid/content/Context;

    goto :goto_2

    nop

    :goto_1
    const/4 p1, 0x1

    goto :goto_7

    nop

    :goto_2
    sget p1, Lmiuix/androidbasewidget/R$string;->miuix_show_password:I

    goto :goto_4

    nop

    :goto_3
    const-class p1, Landroid/widget/Switch;

    goto :goto_9

    nop

    :goto_4
    invoke-virtual {p0, p1}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object p0

    goto :goto_b

    nop

    :goto_5
    invoke-virtual {p2, p1}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setChecked(Z)V

    goto :goto_3

    nop

    :goto_6
    return-void

    :goto_7
    invoke-virtual {p2, p1}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setCheckable(Z)V

    goto :goto_a

    nop

    :goto_8
    invoke-virtual {p2, p1}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setClassName(Ljava/lang/CharSequence;)V

    goto :goto_0

    nop

    :goto_9
    invoke-virtual {p1}, Ljava/lang/Class;->getName()Ljava/lang/String;

    move-result-object p1

    goto :goto_8

    nop

    :goto_a
    iget-boolean p1, p0, Lmiuix/androidbasewidget/widget/PasswordWidgetManager;->mIsChecked:Z

    goto :goto_5

    nop

    :goto_b
    invoke-virtual {p2, p0}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setContentDescription(Ljava/lang/CharSequence;)V

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
