TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/internal/widget/ArrowActionSheet.smali'
CLASS_FALLBACK_NAMES = ['ArrowActionSheet.smali']
CLASS_ANCHORS = ['.super Lmiuix/appcompat/app/AlertDialog;', '.implements Lmiuix/internal/widget/ActionSheet$IActionSheet;']

PATCHES = [
    {
        'id': 'miuix_internal_widget_ArrowActionSheet__createAlertActionSheet',
        'method': '.method protected createAlertActionSheet(Landroid/view/View;)Lmiuix/internal/widget/AlertActionSheet;',
        'method_name': 'createAlertActionSheet',
        'method_anchors': ['new-instance v0, Lmiuix/internal/widget/AlertActionSheet;', 'iget-object v1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mContext:Landroid/content/Context;', 'invoke-direct {v0, v1}, Lmiuix/internal/widget/AlertActionSheet;-><init>(Landroid/content/Context;)V', 'invoke-virtual {v0, p1}, Lmiuix/internal/widget/AlertActionSheet;->setArrowActionAnchor(Landroid/view/View;)V', 'iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mArrowMode:Lmiuix/internal/widget/ActionSheet$ArrowMode;', 'invoke-virtual {v0, p1}, Lmiuix/internal/widget/AlertActionSheet;->setArrowMode(Lmiuix/internal/widget/ActionSheet$ArrowMode;)V', 'invoke-virtual {p0}, Lmiuix/internal/widget/ArrowActionSheet;->isCanceledOnTouchOutside()Z', 'invoke-virtual {v0, p1}, Lmiuix/internal/widget/AlertActionSheet;->setCanceledOnTouchOutside(Z)V'],
        'type': 'method_replace',
        'search': """.method protected createAlertActionSheet(Landroid/view/View;)Lmiuix/internal/widget/AlertActionSheet;
    .registers 5

    new-instance v0, Lmiuix/internal/widget/AlertActionSheet;

    iget-object v1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mContext:Landroid/content/Context;

    invoke-direct {v0, v1}, Lmiuix/internal/widget/AlertActionSheet;-><init>(Landroid/content/Context;)V

    invoke-virtual {v0, p1}, Lmiuix/internal/widget/AlertActionSheet;->setArrowActionAnchor(Landroid/view/View;)V

    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mArrowMode:Lmiuix/internal/widget/ActionSheet$ArrowMode;

    invoke-virtual {v0, p1}, Lmiuix/internal/widget/AlertActionSheet;->setArrowMode(Lmiuix/internal/widget/ActionSheet$ArrowMode;)V

    invoke-virtual {p0}, Lmiuix/internal/widget/ArrowActionSheet;->isCanceledOnTouchOutside()Z

    move-result p1

    invoke-virtual {v0, p1}, Lmiuix/internal/widget/AlertActionSheet;->setCanceledOnTouchOutside(Z)V

    invoke-virtual {p0}, Lmiuix/internal/widget/ArrowActionSheet;->isHapticFeedbackEnabled()Z

    move-result p1

    invoke-virtual {v0, p1}, Lmiuix/internal/widget/AlertActionSheet;->setHapticFeedbackEnabled(Z)V

    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getMessage()Ljava/lang/CharSequence;

    move-result-object p1

    if-eqz p1, :cond_0

    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getMessage()Ljava/lang/CharSequence;

    move-result-object p1

    invoke-virtual {v0, p1}, Lmiuix/internal/widget/AlertActionSheet;->setMessage(Ljava/lang/CharSequence;)V

    :cond_0
    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getActionItems()[Ljava/lang/CharSequence;

    move-result-object p1

    if-eqz p1, :cond_1

    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getItemClickListener()Landroid/content/DialogInterface$OnClickListener;

    move-result-object p1

    if-eqz p1, :cond_1

    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getActionItems()[Ljava/lang/CharSequence;

    move-result-object p1

    iget-object v1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {v1}, Lmiuix/internal/widget/ActionSheetController;->getItemClickListener()Landroid/content/DialogInterface$OnClickListener;

    move-result-object v1

    invoke-virtual {v0, p1, v1}, Lmiuix/internal/widget/AlertActionSheet;->setActionItems([Ljava/lang/CharSequence;Landroid/content/DialogInterface$OnClickListener;)V

    :cond_1
    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getActionItems()[Ljava/lang/CharSequence;

    move-result-object p1

    if-eqz p1, :cond_2

    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getItemClickListener()Landroid/content/DialogInterface$OnClickListener;

    move-result-object p1

    if-eqz p1, :cond_2

    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getItemTypes()[Lmiuix/internal/widget/ActionSheet$ActionSheetItemType;

    move-result-object p1

    if-eqz p1, :cond_2

    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getActionItems()[Ljava/lang/CharSequence;

    move-result-object p1

    iget-object v1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {v1}, Lmiuix/internal/widget/ActionSheetController;->getItemTypes()[Lmiuix/internal/widget/ActionSheet$ActionSheetItemType;

    move-result-object v1

    iget-object v2, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {v2}, Lmiuix/internal/widget/ActionSheetController;->getItemClickListener()Landroid/content/DialogInterface$OnClickListener;

    move-result-object v2

    invoke-virtual {v0, p1, v1, v2}, Lmiuix/internal/widget/AlertActionSheet;->setActionItems([Ljava/lang/CharSequence;[Lmiuix/internal/widget/ActionSheet$ActionSheetItemType;Landroid/content/DialogInterface$OnClickListener;)V

    :cond_2
    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getShowAnimListener()Lmiuix/appcompat/app/AlertDialog$OnDialogShowAnimListener;

    move-result-object p1

    if-eqz p1, :cond_3

    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getShowAnimListener()Lmiuix/appcompat/app/AlertDialog$OnDialogShowAnimListener;

    move-result-object p1

    invoke-virtual {v0, p1}, Lmiuix/internal/widget/AlertActionSheet;->setOnShowAnimListener(Lmiuix/appcompat/app/AlertDialog$OnDialogShowAnimListener;)V

    :cond_3
    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnShowListener()Landroid/content/DialogInterface$OnShowListener;

    move-result-object p1

    if-eqz p1, :cond_4

    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnShowListener()Landroid/content/DialogInterface$OnShowListener;

    move-result-object p1

    invoke-virtual {v0, p1}, Lmiuix/internal/widget/AlertActionSheet;->setActionSheetOnShowListener(Landroid/content/DialogInterface$OnShowListener;)V

    :cond_4
    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnDismissListener()Landroid/content/DialogInterface$OnDismissListener;

    move-result-object p1

    if-eqz p1, :cond_5

    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnDismissListener()Landroid/content/DialogInterface$OnDismissListener;

    move-result-object p1

    invoke-virtual {v0, p1}, Lmiuix/internal/widget/AlertActionSheet;->setActionSheetOnDismissListener(Landroid/content/DialogInterface$OnDismissListener;)V

    :cond_5
    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnKeyListener()Landroid/content/DialogInterface$OnKeyListener;

    move-result-object p1

    if-eqz p1, :cond_6

    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnKeyListener()Landroid/content/DialogInterface$OnKeyListener;

    move-result-object p1

    invoke-virtual {v0, p1}, Landroid/app/Dialog;->setOnKeyListener(Landroid/content/DialogInterface$OnKeyListener;)V

    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnKeyListener()Landroid/content/DialogInterface$OnKeyListener;

    move-result-object p1

    invoke-virtual {v0, p1}, Lmiuix/internal/widget/AlertActionSheet;->setActionSheetOnKeyListener(Landroid/content/DialogInterface$OnKeyListener;)V

    :cond_6
    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getListViewAdapter()Landroid/widget/ListAdapter;

    move-result-object p1

    if-eqz p1, :cond_7

    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getListViewAdapter()Landroid/widget/ListAdapter;

    move-result-object p1

    invoke-virtual {v0, p1}, Lmiuix/internal/widget/AlertActionSheet;->setListViewAdapter(Landroid/widget/ListAdapter;)V

    :cond_7
    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnCancelListener()Landroid/content/DialogInterface$OnCancelListener;

    move-result-object p1

    if-eqz p1, :cond_8

    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnCancelListener()Landroid/content/DialogInterface$OnCancelListener;

    move-result-object p1

    invoke-virtual {v0, p1}, Landroid/app/Dialog;->setOnCancelListener(Landroid/content/DialogInterface$OnCancelListener;)V

    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnCancelListener()Landroid/content/DialogInterface$OnCancelListener;

    move-result-object p1

    invoke-virtual {v0, p1}, Lmiuix/internal/widget/AlertActionSheet;->setActionSheetOnCancelListener(Landroid/content/DialogInterface$OnCancelListener;)V

    :cond_8
    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getConfigurationChangedListener()Lmiuix/appcompat/app/AlertDialog$OnConfigurationChangedListener;

    iget-object p0, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p0}, Lmiuix/internal/widget/ActionSheetController;->getItemProvider()Lmiuix/appcompat/app/AccessibilityDelegateProvider;

    return-object v0
.end method""",
        'replacement': """.method protected createAlertActionSheet(Landroid/view/View;)Lmiuix/internal/widget/AlertActionSheet;
    .registers 5

    goto :goto_4c

    nop

    :goto_0
    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_3c

    nop

    :goto_1
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getItemClickListener()Landroid/content/DialogInterface$OnClickListener;

    move-result-object p1

    goto :goto_2

    nop

    :goto_2
    if-nez p1, :cond_0

    goto :goto_16

    :cond_0
    goto :goto_59

    nop

    :goto_3
    invoke-virtual {v0, p1, v1, v2}, Lmiuix/internal/widget/AlertActionSheet;->setActionItems([Ljava/lang/CharSequence;[Lmiuix/internal/widget/ActionSheet$ActionSheetItemType;Landroid/content/DialogInterface$OnClickListener;)V

    :goto_4
    goto :goto_40

    nop

    :goto_5
    iget-object v1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_45

    nop

    :goto_6
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnShowListener()Landroid/content/DialogInterface$OnShowListener;

    move-result-object p1

    goto :goto_1f

    nop

    :goto_7
    invoke-virtual {v0, p1}, Lmiuix/internal/widget/AlertActionSheet;->setListViewAdapter(Landroid/widget/ListAdapter;)V

    :goto_8
    goto :goto_2d

    nop

    :goto_9
    invoke-virtual {v0, p1}, Lmiuix/internal/widget/AlertActionSheet;->setActionSheetOnKeyListener(Landroid/content/DialogInterface$OnKeyListener;)V

    :goto_a
    goto :goto_18

    nop

    :goto_b
    iget-object v1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mContext:Landroid/content/Context;

    goto :goto_50

    nop

    :goto_c
    invoke-virtual {v2}, Lmiuix/internal/widget/ActionSheetController;->getItemClickListener()Landroid/content/DialogInterface$OnClickListener;

    move-result-object v2

    goto :goto_3

    nop

    :goto_d
    invoke-virtual {v0, p1}, Landroid/app/Dialog;->setOnKeyListener(Landroid/content/DialogInterface$OnKeyListener;)V

    goto :goto_0

    nop

    :goto_e
    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_38

    nop

    :goto_f
    invoke-virtual {p0}, Lmiuix/internal/widget/ArrowActionSheet;->isHapticFeedbackEnabled()Z

    move-result p1

    goto :goto_36

    nop

    :goto_10
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getListViewAdapter()Landroid/widget/ListAdapter;

    move-result-object p1

    goto :goto_7

    nop

    :goto_11
    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_47

    nop

    :goto_12
    invoke-virtual {v0, p1}, Lmiuix/internal/widget/AlertActionSheet;->setActionSheetOnDismissListener(Landroid/content/DialogInterface$OnDismissListener;)V

    :goto_13
    goto :goto_e

    nop

    :goto_14
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getItemClickListener()Landroid/content/DialogInterface$OnClickListener;

    move-result-object p1

    goto :goto_48

    nop

    :goto_15
    invoke-virtual {v0, p1, v1}, Lmiuix/internal/widget/AlertActionSheet;->setActionItems([Ljava/lang/CharSequence;Landroid/content/DialogInterface$OnClickListener;)V

    :goto_16
    goto :goto_30

    nop

    :goto_17
    if-nez p1, :cond_1

    goto :goto_20

    :cond_1
    goto :goto_22

    nop

    :goto_18
    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_5f

    nop

    :goto_19
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnDismissListener()Landroid/content/DialogInterface$OnDismissListener;

    move-result-object p1

    goto :goto_44

    nop

    :goto_1a
    invoke-virtual {p0}, Lmiuix/internal/widget/ActionSheetController;->getItemProvider()Lmiuix/appcompat/app/AccessibilityDelegateProvider;

    goto :goto_4f

    nop

    :goto_1b
    invoke-virtual {v0, p1}, Lmiuix/internal/widget/AlertActionSheet;->setArrowMode(Lmiuix/internal/widget/ActionSheet$ArrowMode;)V

    goto :goto_37

    nop

    :goto_1c
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getMessage()Ljava/lang/CharSequence;

    move-result-object p1

    goto :goto_4a

    nop

    :goto_1d
    if-nez p1, :cond_2

    goto :goto_a

    :cond_2
    goto :goto_43

    nop

    :goto_1e
    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_1

    nop

    :goto_1f
    invoke-virtual {v0, p1}, Lmiuix/internal/widget/AlertActionSheet;->setActionSheetOnShowListener(Landroid/content/DialogInterface$OnShowListener;)V

    :goto_20
    goto :goto_55

    nop

    :goto_21
    if-nez p1, :cond_3

    goto :goto_8

    :cond_3
    goto :goto_46

    nop

    :goto_22
    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_6

    nop

    :goto_23
    invoke-virtual {v0, p1}, Lmiuix/internal/widget/AlertActionSheet;->setCanceledOnTouchOutside(Z)V

    goto :goto_f

    nop

    :goto_24
    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_49

    nop

    :goto_25
    if-nez p1, :cond_4

    goto :goto_4

    :cond_4
    goto :goto_42

    nop

    :goto_26
    invoke-virtual {v0, p1}, Lmiuix/internal/widget/AlertActionSheet;->setMessage(Ljava/lang/CharSequence;)V

    :goto_27
    goto :goto_39

    nop

    :goto_28
    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_5b

    nop

    :goto_29
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getActionItems()[Ljava/lang/CharSequence;

    move-result-object p1

    goto :goto_3e

    nop

    :goto_2a
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getActionItems()[Ljava/lang/CharSequence;

    move-result-object p1

    goto :goto_3b

    nop

    :goto_2b
    invoke-virtual {v0, p1}, Lmiuix/internal/widget/AlertActionSheet;->setOnShowAnimListener(Lmiuix/appcompat/app/AlertDialog$OnDialogShowAnimListener;)V

    :goto_2c
    goto :goto_28

    nop

    :goto_2d
    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_56

    nop

    :goto_2e
    iget-object v2, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_c

    nop

    :goto_2f
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getShowAnimListener()Lmiuix/appcompat/app/AlertDialog$OnDialogShowAnimListener;

    move-result-object p1

    goto :goto_31

    nop

    :goto_30
    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_32

    nop

    :goto_31
    if-nez p1, :cond_5

    goto :goto_2c

    :cond_5
    goto :goto_24

    nop

    :goto_32
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getActionItems()[Ljava/lang/CharSequence;

    move-result-object p1

    goto :goto_61

    nop

    :goto_33
    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_1c

    nop

    :goto_34
    invoke-virtual {v0, p1}, Lmiuix/internal/widget/AlertActionSheet;->setArrowActionAnchor(Landroid/view/View;)V

    goto :goto_3f

    nop

    :goto_35
    invoke-virtual {v0, p1}, Landroid/app/Dialog;->setOnCancelListener(Landroid/content/DialogInterface$OnCancelListener;)V

    goto :goto_4b

    nop

    :goto_36
    invoke-virtual {v0, p1}, Lmiuix/internal/widget/AlertActionSheet;->setHapticFeedbackEnabled(Z)V

    goto :goto_33

    nop

    :goto_37
    invoke-virtual {p0}, Lmiuix/internal/widget/ArrowActionSheet;->isCanceledOnTouchOutside()Z

    move-result p1

    goto :goto_23

    nop

    :goto_38
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnKeyListener()Landroid/content/DialogInterface$OnKeyListener;

    move-result-object p1

    goto :goto_1d

    nop

    :goto_39
    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_2a

    nop

    :goto_3a
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnCancelListener()Landroid/content/DialogInterface$OnCancelListener;

    move-result-object p1

    goto :goto_51

    nop

    :goto_3b
    if-nez p1, :cond_6

    goto :goto_16

    :cond_6
    goto :goto_1e

    nop

    :goto_3c
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnKeyListener()Landroid/content/DialogInterface$OnKeyListener;

    move-result-object p1

    goto :goto_9

    nop

    :goto_3d
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnCancelListener()Landroid/content/DialogInterface$OnCancelListener;

    move-result-object p1

    goto :goto_35

    nop

    :goto_3e
    iget-object v1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_5d

    nop

    :goto_3f
    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mArrowMode:Lmiuix/internal/widget/ActionSheet$ArrowMode;

    goto :goto_1b

    nop

    :goto_40
    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_2f

    nop

    :goto_41
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getItemTypes()[Lmiuix/internal/widget/ActionSheet$ActionSheetItemType;

    move-result-object p1

    goto :goto_25

    nop

    :goto_42
    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_54

    nop

    :goto_43
    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_4e

    nop

    :goto_44
    if-nez p1, :cond_7

    goto :goto_13

    :cond_7
    goto :goto_11

    nop

    :goto_45
    invoke-virtual {v1}, Lmiuix/internal/widget/ActionSheetController;->getItemTypes()[Lmiuix/internal/widget/ActionSheet$ActionSheetItemType;

    move-result-object v1

    goto :goto_2e

    nop

    :goto_46
    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_10

    nop

    :goto_47
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnDismissListener()Landroid/content/DialogInterface$OnDismissListener;

    move-result-object p1

    goto :goto_12

    nop

    :goto_48
    if-nez p1, :cond_8

    goto :goto_4

    :cond_8
    goto :goto_5a

    nop

    :goto_49
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getShowAnimListener()Lmiuix/appcompat/app/AlertDialog$OnDialogShowAnimListener;

    move-result-object p1

    goto :goto_2b

    nop

    :goto_4a
    if-nez p1, :cond_9

    goto :goto_27

    :cond_9
    goto :goto_53

    nop

    :goto_4b
    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_3a

    nop

    :goto_4c
    new-instance v0, Lmiuix/internal/widget/AlertActionSheet;

    goto :goto_b

    nop

    :goto_4d
    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_5c

    nop

    :goto_4e
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnKeyListener()Landroid/content/DialogInterface$OnKeyListener;

    move-result-object p1

    goto :goto_d

    nop

    :goto_4f
    return-object v0

    :goto_50
    invoke-direct {v0, v1}, Lmiuix/internal/widget/AlertActionSheet;-><init>(Landroid/content/Context;)V

    goto :goto_34

    nop

    :goto_51
    invoke-virtual {v0, p1}, Lmiuix/internal/widget/AlertActionSheet;->setActionSheetOnCancelListener(Landroid/content/DialogInterface$OnCancelListener;)V

    :goto_52
    goto :goto_4d

    nop

    :goto_53
    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_60

    nop

    :goto_54
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getActionItems()[Ljava/lang/CharSequence;

    move-result-object p1

    goto :goto_5

    nop

    :goto_55
    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_19

    nop

    :goto_56
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnCancelListener()Landroid/content/DialogInterface$OnCancelListener;

    move-result-object p1

    goto :goto_62

    nop

    :goto_57
    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_14

    nop

    :goto_58
    iget-object p0, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_1a

    nop

    :goto_59
    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_29

    nop

    :goto_5a
    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_41

    nop

    :goto_5b
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnShowListener()Landroid/content/DialogInterface$OnShowListener;

    move-result-object p1

    goto :goto_17

    nop

    :goto_5c
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getConfigurationChangedListener()Lmiuix/appcompat/app/AlertDialog$OnConfigurationChangedListener;

    goto :goto_58

    nop

    :goto_5d
    invoke-virtual {v1}, Lmiuix/internal/widget/ActionSheetController;->getItemClickListener()Landroid/content/DialogInterface$OnClickListener;

    move-result-object v1

    goto :goto_15

    nop

    :goto_5e
    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_3d

    nop

    :goto_5f
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getListViewAdapter()Landroid/widget/ListAdapter;

    move-result-object p1

    goto :goto_21

    nop

    :goto_60
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getMessage()Ljava/lang/CharSequence;

    move-result-object p1

    goto :goto_26

    nop

    :goto_61
    if-nez p1, :cond_a

    goto :goto_4

    :cond_a
    goto :goto_57

    nop

    :goto_62
    if-nez p1, :cond_b

    goto :goto_52

    :cond_b
    goto :goto_5e

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_widget_ArrowActionSheet__dismissForShiftWithoutAnimation',
        'method': '.method protected dismissForShiftWithoutAnimation()V',
        'method_name': 'dismissForShiftWithoutAnimation',
        'method_anchors': ['invoke-virtual {p0, v0}, Lmiuix/internal/widget/ArrowActionSheet;->setIsDismissForShift(Z)V', 'invoke-virtual {p0}, Lmiuix/internal/widget/ArrowActionSheet;->dismissWithoutAnimation()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected dismissForShiftWithoutAnimation()V
    .registers 2

    const/4 v0, 0x1

    invoke-virtual {p0, v0}, Lmiuix/internal/widget/ArrowActionSheet;->setIsDismissForShift(Z)V

    invoke-virtual {p0}, Lmiuix/internal/widget/ArrowActionSheet;->dismissWithoutAnimation()V

    return-void
.end method""",
        'replacement': """.method protected dismissForShiftWithoutAnimation()V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    invoke-virtual {p0, v0}, Lmiuix/internal/widget/ArrowActionSheet;->setIsDismissForShift(Z)V

    goto :goto_3

    nop

    :goto_1
    const/4 v0, 0x1

    goto :goto_0

    nop

    :goto_2
    return-void

    :goto_3
    invoke-virtual {p0}, Lmiuix/internal/widget/ArrowActionSheet;->dismissWithoutAnimation()V

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_widget_ArrowActionSheet__dismissWithAnimationExistDecorView',
        'method': '.method protected dismissWithAnimationExistDecorView(Landroid/view/View;)V',
        'method_name': 'dismissWithAnimationExistDecorView',
        'method_anchors': ['invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;', 'invoke-virtual {p1}, Landroid/view/View;->getHandler()Landroid/os/Handler;', 'invoke-virtual {v1}, Landroid/os/Handler;->getLooper()Landroid/os/Looper;', 'invoke-virtual {v1}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;', 'if-ne v0, v1, :cond_0', 'iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;', 'iget-object p0, p0, Lmiuix/appcompat/app/AlertDialog;->mOnDismiss:Lmiuix/appcompat/widget/DialogAnimHelper$OnDismiss;', 'invoke-virtual {p1, p0}, Lmiuix/internal/widget/ActionSheetController;->dismiss(Lmiuix/appcompat/widget/DialogAnimHelper$OnDismiss;)V'],
        'type': 'method_replace',
        'search': """.method protected dismissWithAnimationExistDecorView(Landroid/view/View;)V
    .registers 4

    invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;

    move-result-object v0

    invoke-virtual {p1}, Landroid/view/View;->getHandler()Landroid/os/Handler;

    move-result-object v1

    invoke-virtual {v1}, Landroid/os/Handler;->getLooper()Landroid/os/Looper;

    move-result-object v1

    invoke-virtual {v1}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;

    move-result-object v1

    if-ne v0, v1, :cond_0

    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    iget-object p0, p0, Lmiuix/appcompat/app/AlertDialog;->mOnDismiss:Lmiuix/appcompat/widget/DialogAnimHelper$OnDismiss;

    invoke-virtual {p1, p0}, Lmiuix/internal/widget/ActionSheetController;->dismiss(Lmiuix/appcompat/widget/DialogAnimHelper$OnDismiss;)V

    return-void

    :cond_0
    new-instance v0, Lmiuix/internal/widget/ArrowActionSheet$$ExternalSyntheticLambda0;

    invoke-direct {v0, p0}, Lmiuix/internal/widget/ArrowActionSheet$$ExternalSyntheticLambda0;-><init>(Lmiuix/internal/widget/ArrowActionSheet;)V

    invoke-virtual {p1, v0}, Landroid/view/View;->post(Ljava/lang/Runnable;)Z

    return-void
.end method""",
        'replacement': """.method protected dismissWithAnimationExistDecorView(Landroid/view/View;)V
    .registers 4

    goto :goto_b

    nop

    :goto_0
    return-void

    :goto_1
    invoke-virtual {p1}, Landroid/view/View;->getHandler()Landroid/os/Handler;

    move-result-object v1

    goto :goto_7

    nop

    :goto_2
    invoke-virtual {v1}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;

    move-result-object v1

    goto :goto_9

    nop

    :goto_3
    invoke-virtual {p1, v0}, Landroid/view/View;->post(Ljava/lang/Runnable;)Z

    goto :goto_0

    nop

    :goto_4
    new-instance v0, Lmiuix/internal/widget/ArrowActionSheet$$ExternalSyntheticLambda0;

    goto :goto_a

    nop

    :goto_5
    invoke-virtual {p1, p0}, Lmiuix/internal/widget/ActionSheetController;->dismiss(Lmiuix/appcompat/widget/DialogAnimHelper$OnDismiss;)V

    goto :goto_c

    nop

    :goto_6
    iget-object p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_8

    nop

    :goto_7
    invoke-virtual {v1}, Landroid/os/Handler;->getLooper()Landroid/os/Looper;

    move-result-object v1

    goto :goto_2

    nop

    :goto_8
    iget-object p0, p0, Lmiuix/appcompat/app/AlertDialog;->mOnDismiss:Lmiuix/appcompat/widget/DialogAnimHelper$OnDismiss;

    goto :goto_5

    nop

    :goto_9
    if-eq v0, v1, :cond_0

    goto :goto_d

    :cond_0
    goto :goto_6

    nop

    :goto_a
    invoke-direct {v0, p0}, Lmiuix/internal/widget/ArrowActionSheet$$ExternalSyntheticLambda0;-><init>(Lmiuix/internal/widget/ArrowActionSheet;)V

    goto :goto_3

    nop

    :goto_b
    invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;

    move-result-object v0

    goto :goto_1

    nop

    :goto_c
    return-void

    :goto_d
    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_widget_ArrowActionSheet__isDismissForShift',
        'method': '.method protected isDismissForShift()Z',
        'method_name': 'isDismissForShift',
        'method_anchors': ['iget-boolean p0, p0, Lmiuix/internal/widget/ArrowActionSheet;->mIsDismissForShift:Z', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected isDismissForShift()Z
    .registers 1

    iget-boolean p0, p0, Lmiuix/internal/widget/ArrowActionSheet;->mIsDismissForShift:Z

    return p0
.end method""",
        'replacement': """.method protected isDismissForShift()Z
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    iget-boolean p0, p0, Lmiuix/internal/widget/ArrowActionSheet;->mIsDismissForShift:Z

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_widget_ArrowActionSheet__isFromAlertShape',
        'method': '.method protected isFromAlertShape()Z',
        'method_name': 'isFromAlertShape',
        'method_anchors': ['iget-boolean p0, p0, Lmiuix/internal/widget/ArrowActionSheet;->mIsFromAlertShape:Z', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected isFromAlertShape()Z
    .registers 1

    iget-boolean p0, p0, Lmiuix/internal/widget/ArrowActionSheet;->mIsFromAlertShape:Z

    return p0
.end method""",
        'replacement': """.method protected isFromAlertShape()Z
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    iget-boolean p0, p0, Lmiuix/internal/widget/ArrowActionSheet;->mIsFromAlertShape:Z

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_widget_ArrowActionSheet__onCreate',
        'method': '.method protected onCreate(Landroid/os/Bundle;)V',
        'method_name': 'onCreate',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/appcompat/app/AlertDialog;->isSystemSpecialUiThread()Z', 'if-eqz v0, :cond_0', 'iget-object v0, p0, Lmiuix/appcompat/app/AlertDialog;->mLifecycleOwnerCompat:Lmiuix/appcompat/app/AlertDialog$LifecycleOwnerCompat;', 'if-eqz v0, :cond_0', 'invoke-virtual {v0}, Lmiuix/appcompat/app/AlertDialog$LifecycleOwnerCompat;->onCreate()V', 'invoke-virtual {p0}, Landroid/app/Dialog;->getWindow()Landroid/view/Window;', 'invoke-virtual {v0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;', 'invoke-virtual {v0, v1}, Landroid/view/Window;->setWindowAnimations(I)V'],
        'type': 'method_replace',
        'search': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 4

    invoke-virtual {p0}, Lmiuix/appcompat/app/AlertDialog;->isSystemSpecialUiThread()Z

    move-result v0

    if-eqz v0, :cond_0

    iget-object v0, p0, Lmiuix/appcompat/app/AlertDialog;->mLifecycleOwnerCompat:Lmiuix/appcompat/app/AlertDialog$LifecycleOwnerCompat;

    if-eqz v0, :cond_0

    invoke-virtual {v0}, Lmiuix/appcompat/app/AlertDialog$LifecycleOwnerCompat;->onCreate()V

    :cond_0
    invoke-virtual {p0}, Landroid/app/Dialog;->getWindow()Landroid/view/Window;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    const/4 v1, 0x0

    invoke-virtual {v0, v1}, Landroid/view/Window;->setWindowAnimations(I)V

    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AlertDialog;->superOnCreate(Landroid/os/Bundle;)V

    iget-object p0, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p0, p1}, Lmiuix/internal/widget/ActionSheetController;->installContent(Landroid/os/Bundle;)V

    return-void
.end method""",
        'replacement': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 4

    goto :goto_2

    nop

    :goto_0
    invoke-virtual {p0}, Landroid/app/Dialog;->getWindow()Landroid/view/Window;

    move-result-object v0

    goto :goto_1

    nop

    :goto_1
    invoke-virtual {v0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    goto :goto_c

    nop

    :goto_2
    invoke-virtual {p0}, Lmiuix/appcompat/app/AlertDialog;->isSystemSpecialUiThread()Z

    move-result v0

    goto :goto_d

    nop

    :goto_3
    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AlertDialog;->superOnCreate(Landroid/os/Bundle;)V

    goto :goto_4

    nop

    :goto_4
    iget-object p0, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_5

    nop

    :goto_5
    invoke-virtual {p0, p1}, Lmiuix/internal/widget/ActionSheetController;->installContent(Landroid/os/Bundle;)V

    goto :goto_a

    nop

    :goto_6
    invoke-virtual {v0}, Lmiuix/appcompat/app/AlertDialog$LifecycleOwnerCompat;->onCreate()V

    :goto_7
    goto :goto_0

    nop

    :goto_8
    iget-object v0, p0, Lmiuix/appcompat/app/AlertDialog;->mLifecycleOwnerCompat:Lmiuix/appcompat/app/AlertDialog$LifecycleOwnerCompat;

    goto :goto_b

    nop

    :goto_9
    invoke-virtual {v0, v1}, Landroid/view/Window;->setWindowAnimations(I)V

    goto :goto_3

    nop

    :goto_a
    return-void

    :goto_b
    if-nez v0, :cond_0

    goto :goto_7

    :cond_0
    goto :goto_6

    nop

    :goto_c
    const/4 v1, 0x0

    goto :goto_9

    nop

    :goto_d
    if-nez v0, :cond_1

    goto :goto_7

    :cond_1
    goto :goto_8

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_widget_ArrowActionSheet__onStart',
        'method': '.method protected onStart()V',
        'method_name': 'onStart',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/appcompat/app/AlertDialog;->superOnStart()V', 'iget-object p0, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;', 'invoke-virtual {p0}, Lmiuix/internal/widget/ActionSheetController;->onStart()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onStart()V
    .registers 1

    invoke-virtual {p0}, Lmiuix/appcompat/app/AlertDialog;->superOnStart()V

    iget-object p0, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p0}, Lmiuix/internal/widget/ActionSheetController;->onStart()V

    return-void
.end method""",
        'replacement': """.method protected onStart()V
    .registers 1

    goto :goto_3

    nop

    :goto_0
    invoke-virtual {p0}, Lmiuix/internal/widget/ActionSheetController;->onStart()V

    goto :goto_2

    nop

    :goto_1
    iget-object p0, p0, Lmiuix/internal/widget/ArrowActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_0

    nop

    :goto_2
    return-void

    :goto_3
    invoke-virtual {p0}, Lmiuix/appcompat/app/AlertDialog;->superOnStart()V

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_widget_ArrowActionSheet__onStop',
        'method': '.method protected onStop()V',
        'method_name': 'onStop',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/appcompat/app/AlertDialog;->isSystemSpecialUiThread()Z', 'if-eqz v0, :cond_0', 'iget-object v0, p0, Lmiuix/appcompat/app/AlertDialog;->mLifecycleOwnerCompat:Lmiuix/appcompat/app/AlertDialog$LifecycleOwnerCompat;', 'if-eqz v0, :cond_0', 'invoke-virtual {v0}, Lmiuix/appcompat/app/AlertDialog$LifecycleOwnerCompat;->onStopBefore()V', 'invoke-virtual {p0}, Lmiuix/appcompat/app/AlertDialog;->superOnStop()V', 'invoke-virtual {p0}, Lmiuix/appcompat/app/AlertDialog;->isSystemSpecialUiThread()Z', 'if-eqz v0, :cond_1'],
        'type': 'method_replace',
        'search': """.method protected onStop()V
    .registers 2

    invoke-virtual {p0}, Lmiuix/appcompat/app/AlertDialog;->isSystemSpecialUiThread()Z

    move-result v0

    if-eqz v0, :cond_0

    iget-object v0, p0, Lmiuix/appcompat/app/AlertDialog;->mLifecycleOwnerCompat:Lmiuix/appcompat/app/AlertDialog$LifecycleOwnerCompat;

    if-eqz v0, :cond_0

    invoke-virtual {v0}, Lmiuix/appcompat/app/AlertDialog$LifecycleOwnerCompat;->onStopBefore()V

    :cond_0
    invoke-virtual {p0}, Lmiuix/appcompat/app/AlertDialog;->superOnStop()V

    invoke-virtual {p0}, Lmiuix/appcompat/app/AlertDialog;->isSystemSpecialUiThread()Z

    move-result v0

    if-eqz v0, :cond_1

    iget-object p0, p0, Lmiuix/appcompat/app/AlertDialog;->mLifecycleOwnerCompat:Lmiuix/appcompat/app/AlertDialog$LifecycleOwnerCompat;

    if-eqz p0, :cond_1

    invoke-virtual {p0}, Lmiuix/appcompat/app/AlertDialog$LifecycleOwnerCompat;->onStopAfter()V

    :cond_1
    return-void
.end method""",
        'replacement': """.method protected onStop()V
    .registers 2

    goto :goto_5

    nop

    :goto_0
    if-nez p0, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_1

    nop

    :goto_1
    invoke-virtual {p0}, Lmiuix/appcompat/app/AlertDialog$LifecycleOwnerCompat;->onStopAfter()V

    :goto_2
    goto :goto_d

    nop

    :goto_3
    if-nez v0, :cond_1

    goto :goto_8

    :cond_1
    goto :goto_7

    nop

    :goto_4
    iget-object p0, p0, Lmiuix/appcompat/app/AlertDialog;->mLifecycleOwnerCompat:Lmiuix/appcompat/app/AlertDialog$LifecycleOwnerCompat;

    goto :goto_0

    nop

    :goto_5
    invoke-virtual {p0}, Lmiuix/appcompat/app/AlertDialog;->isSystemSpecialUiThread()Z

    move-result v0

    goto :goto_9

    nop

    :goto_6
    if-nez v0, :cond_2

    goto :goto_2

    :cond_2
    goto :goto_4

    nop

    :goto_7
    invoke-virtual {v0}, Lmiuix/appcompat/app/AlertDialog$LifecycleOwnerCompat;->onStopBefore()V

    :goto_8
    goto :goto_c

    nop

    :goto_9
    if-nez v0, :cond_3

    goto :goto_8

    :cond_3
    goto :goto_b

    nop

    :goto_a
    invoke-virtual {p0}, Lmiuix/appcompat/app/AlertDialog;->isSystemSpecialUiThread()Z

    move-result v0

    goto :goto_6

    nop

    :goto_b
    iget-object v0, p0, Lmiuix/appcompat/app/AlertDialog;->mLifecycleOwnerCompat:Lmiuix/appcompat/app/AlertDialog$LifecycleOwnerCompat;

    goto :goto_3

    nop

    :goto_c
    invoke-virtual {p0}, Lmiuix/appcompat/app/AlertDialog;->superOnStop()V

    goto :goto_a

    nop

    :goto_d
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_widget_ArrowActionSheet__setIsDismissForShift',
        'method': '.method protected setIsDismissForShift(Z)V',
        'method_name': 'setIsDismissForShift',
        'method_anchors': ['iput-boolean p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mIsDismissForShift:Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected setIsDismissForShift(Z)V
    .registers 2

    iput-boolean p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mIsDismissForShift:Z

    return-void
.end method""",
        'replacement': """.method protected setIsDismissForShift(Z)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    iput-boolean p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mIsDismissForShift:Z

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_widget_ArrowActionSheet__setIsFromAlertShape',
        'method': '.method protected setIsFromAlertShape(Z)V',
        'method_name': 'setIsFromAlertShape',
        'method_anchors': ['iput-boolean p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mIsFromAlertShape:Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected setIsFromAlertShape(Z)V
    .registers 2

    iput-boolean p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mIsFromAlertShape:Z

    return-void
.end method""",
        'replacement': """.method protected setIsFromAlertShape(Z)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    iput-boolean p1, p0, Lmiuix/internal/widget/ArrowActionSheet;->mIsFromAlertShape:Z

    goto :goto_1

    nop

    :goto_1
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
