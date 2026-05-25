TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/internal/widget/AlertActionSheet.smali'
CLASS_FALLBACK_NAMES = ['AlertActionSheet.smali']
CLASS_ANCHORS = ['.super Lmiuix/appcompat/app/AlertDialog;', '.implements Lmiuix/internal/widget/ActionSheet$IActionSheet;']

PATCHES = [
    {
        'id': 'miuix_internal_widget_AlertActionSheet__createArrowActionSheet',
        'method': '.method protected createArrowActionSheet(Landroid/view/View;)Lmiuix/internal/widget/ArrowActionSheet;',
        'method_name': 'createArrowActionSheet',
        'method_anchors': ['iput-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mArrowActionAnchor:Landroid/view/View;', 'new-instance v0, Lmiuix/internal/widget/ArrowActionSheet;', 'iget-object v1, p0, Lmiuix/internal/widget/AlertActionSheet;->mContext:Landroid/content/Context;', 'invoke-direct {v0, v1, p1}, Lmiuix/internal/widget/ArrowActionSheet;-><init>(Landroid/content/Context;Landroid/view/View;)V', 'iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mArrowMode:Lmiuix/internal/widget/ActionSheet$ArrowMode;', 'invoke-virtual {v0, p1}, Lmiuix/internal/widget/ArrowActionSheet;->setArrowMode(Lmiuix/internal/widget/ActionSheet$ArrowMode;)V', 'invoke-virtual {p0}, Lmiuix/internal/widget/AlertActionSheet;->isHapticFeedbackEnabled()Z', 'invoke-virtual {v0, p1}, Lmiuix/internal/widget/ArrowActionSheet;->setHapticFeedbackEnabled(Z)V'],
        'type': 'method_replace',
        'search': """.method protected createArrowActionSheet(Landroid/view/View;)Lmiuix/internal/widget/ArrowActionSheet;
    .registers 5

    iput-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mArrowActionAnchor:Landroid/view/View;

    new-instance v0, Lmiuix/internal/widget/ArrowActionSheet;

    iget-object v1, p0, Lmiuix/internal/widget/AlertActionSheet;->mContext:Landroid/content/Context;

    invoke-direct {v0, v1, p1}, Lmiuix/internal/widget/ArrowActionSheet;-><init>(Landroid/content/Context;Landroid/view/View;)V

    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mArrowMode:Lmiuix/internal/widget/ActionSheet$ArrowMode;

    invoke-virtual {v0, p1}, Lmiuix/internal/widget/ArrowActionSheet;->setArrowMode(Lmiuix/internal/widget/ActionSheet$ArrowMode;)V

    invoke-virtual {p0}, Lmiuix/internal/widget/AlertActionSheet;->isHapticFeedbackEnabled()Z

    move-result p1

    invoke-virtual {v0, p1}, Lmiuix/internal/widget/ArrowActionSheet;->setHapticFeedbackEnabled(Z)V

    invoke-virtual {p0}, Lmiuix/internal/widget/AlertActionSheet;->isCanceledOnTouchOutside()Z

    move-result p1

    invoke-virtual {v0, p1}, Lmiuix/internal/widget/ArrowActionSheet;->setCanceledOnTouchOutside(Z)V

    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getMessage()Ljava/lang/CharSequence;

    move-result-object p1

    if-eqz p1, :cond_0

    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getMessage()Ljava/lang/CharSequence;

    move-result-object p1

    invoke-virtual {v0, p1}, Lmiuix/internal/widget/ArrowActionSheet;->setMessage(Ljava/lang/CharSequence;)V

    :cond_0
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getActionItems()[Ljava/lang/CharSequence;

    move-result-object p1

    if-eqz p1, :cond_1

    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getItemClickListener()Landroid/content/DialogInterface$OnClickListener;

    move-result-object p1

    if-eqz p1, :cond_1

    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getActionItems()[Ljava/lang/CharSequence;

    move-result-object p1

    iget-object v1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {v1}, Lmiuix/internal/widget/ActionSheetController;->getItemClickListener()Landroid/content/DialogInterface$OnClickListener;

    move-result-object v1

    invoke-virtual {v0, p1, v1}, Lmiuix/internal/widget/ArrowActionSheet;->setActionItems([Ljava/lang/CharSequence;Landroid/content/DialogInterface$OnClickListener;)V

    :cond_1
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getActionItems()[Ljava/lang/CharSequence;

    move-result-object p1

    if-eqz p1, :cond_2

    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getItemClickListener()Landroid/content/DialogInterface$OnClickListener;

    move-result-object p1

    if-eqz p1, :cond_2

    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getItemTypes()[Lmiuix/internal/widget/ActionSheet$ActionSheetItemType;

    move-result-object p1

    if-eqz p1, :cond_2

    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getActionItems()[Ljava/lang/CharSequence;

    move-result-object p1

    iget-object v1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {v1}, Lmiuix/internal/widget/ActionSheetController;->getItemTypes()[Lmiuix/internal/widget/ActionSheet$ActionSheetItemType;

    move-result-object v1

    iget-object v2, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {v2}, Lmiuix/internal/widget/ActionSheetController;->getItemClickListener()Landroid/content/DialogInterface$OnClickListener;

    move-result-object v2

    invoke-virtual {v0, p1, v1, v2}, Lmiuix/internal/widget/ArrowActionSheet;->setActionItems([Ljava/lang/CharSequence;[Lmiuix/internal/widget/ActionSheet$ActionSheetItemType;Landroid/content/DialogInterface$OnClickListener;)V

    :cond_2
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getShowAnimListener()Lmiuix/appcompat/app/AlertDialog$OnDialogShowAnimListener;

    move-result-object p1

    if-eqz p1, :cond_3

    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getShowAnimListener()Lmiuix/appcompat/app/AlertDialog$OnDialogShowAnimListener;

    move-result-object p1

    invoke-virtual {v0, p1}, Lmiuix/internal/widget/ArrowActionSheet;->setOnShowAnimListener(Lmiuix/appcompat/app/AlertDialog$OnDialogShowAnimListener;)V

    :cond_3
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnShowListener()Landroid/content/DialogInterface$OnShowListener;

    move-result-object p1

    if-eqz p1, :cond_4

    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnShowListener()Landroid/content/DialogInterface$OnShowListener;

    move-result-object p1

    invoke-virtual {v0, p1}, Lmiuix/internal/widget/ArrowActionSheet;->setActionSheetOnShowListener(Landroid/content/DialogInterface$OnShowListener;)V

    :cond_4
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnDismissListener()Landroid/content/DialogInterface$OnDismissListener;

    move-result-object p1

    if-eqz p1, :cond_5

    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnDismissListener()Landroid/content/DialogInterface$OnDismissListener;

    move-result-object p1

    invoke-virtual {v0, p1}, Lmiuix/internal/widget/ArrowActionSheet;->setActionSheetOnDismissListener(Landroid/content/DialogInterface$OnDismissListener;)V

    :cond_5
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnKeyListener()Landroid/content/DialogInterface$OnKeyListener;

    move-result-object p1

    if-eqz p1, :cond_6

    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnKeyListener()Landroid/content/DialogInterface$OnKeyListener;

    move-result-object p1

    invoke-virtual {v0, p1}, Landroid/app/Dialog;->setOnKeyListener(Landroid/content/DialogInterface$OnKeyListener;)V

    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnKeyListener()Landroid/content/DialogInterface$OnKeyListener;

    move-result-object p1

    invoke-virtual {v0, p1}, Lmiuix/internal/widget/ArrowActionSheet;->setActionSheetOnKeyListener(Landroid/content/DialogInterface$OnKeyListener;)V

    :cond_6
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getListViewAdapter()Landroid/widget/ListAdapter;

    move-result-object p1

    if-eqz p1, :cond_7

    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getListViewAdapter()Landroid/widget/ListAdapter;

    move-result-object p1

    invoke-virtual {v0, p1}, Lmiuix/internal/widget/ArrowActionSheet;->setListViewAdapter(Landroid/widget/ListAdapter;)V

    :cond_7
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnCancelListener()Landroid/content/DialogInterface$OnCancelListener;

    move-result-object p1

    if-eqz p1, :cond_8

    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnCancelListener()Landroid/content/DialogInterface$OnCancelListener;

    move-result-object p1

    invoke-virtual {v0, p1}, Landroid/app/Dialog;->setOnCancelListener(Landroid/content/DialogInterface$OnCancelListener;)V

    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnCancelListener()Landroid/content/DialogInterface$OnCancelListener;

    move-result-object p1

    invoke-virtual {v0, p1}, Lmiuix/internal/widget/ArrowActionSheet;->setActionSheetOnCancelListener(Landroid/content/DialogInterface$OnCancelListener;)V

    :cond_8
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getConfigurationChangedListener()Lmiuix/appcompat/app/AlertDialog$OnConfigurationChangedListener;

    iget-object p0, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p0}, Lmiuix/internal/widget/ActionSheetController;->getItemProvider()Lmiuix/appcompat/app/AccessibilityDelegateProvider;

    return-object v0
.end method""",
        'replacement': """.method protected createArrowActionSheet(Landroid/view/View;)Lmiuix/internal/widget/ArrowActionSheet;
    .registers 5

    goto :goto_4b

    nop

    :goto_0
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getActionItems()[Ljava/lang/CharSequence;

    move-result-object p1

    goto :goto_45

    nop

    :goto_1
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnDismissListener()Landroid/content/DialogInterface$OnDismissListener;

    move-result-object p1

    goto :goto_2

    nop

    :goto_2
    if-nez p1, :cond_0

    goto :goto_19

    :cond_0
    goto :goto_32

    nop

    :goto_3
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getActionItems()[Ljava/lang/CharSequence;

    move-result-object p1

    goto :goto_5

    nop

    :goto_4
    invoke-virtual {v1}, Lmiuix/internal/widget/ActionSheetController;->getItemTypes()[Lmiuix/internal/widget/ActionSheet$ActionSheetItemType;

    move-result-object v1

    goto :goto_4d

    nop

    :goto_5
    if-nez p1, :cond_1

    goto :goto_2b

    :cond_1
    goto :goto_13

    nop

    :goto_6
    invoke-virtual {v0, p1, v1}, Lmiuix/internal/widget/ArrowActionSheet;->setActionItems([Ljava/lang/CharSequence;Landroid/content/DialogInterface$OnClickListener;)V

    :goto_7
    goto :goto_1e

    nop

    :goto_8
    invoke-virtual {v2}, Lmiuix/internal/widget/ActionSheetController;->getItemClickListener()Landroid/content/DialogInterface$OnClickListener;

    move-result-object v2

    goto :goto_2a

    nop

    :goto_9
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_1

    nop

    :goto_a
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_58

    nop

    :goto_b
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_35

    nop

    :goto_c
    invoke-virtual {p0}, Lmiuix/internal/widget/ActionSheetController;->getItemProvider()Lmiuix/appcompat/app/AccessibilityDelegateProvider;

    goto :goto_1a

    nop

    :goto_d
    invoke-virtual {v0, p1}, Lmiuix/internal/widget/ArrowActionSheet;->setOnShowAnimListener(Lmiuix/appcompat/app/AlertDialog$OnDialogShowAnimListener;)V

    :goto_e
    goto :goto_55

    nop

    :goto_f
    invoke-virtual {v0, p1}, Lmiuix/internal/widget/ArrowActionSheet;->setActionSheetOnKeyListener(Landroid/content/DialogInterface$OnKeyListener;)V

    :goto_10
    goto :goto_b

    nop

    :goto_11
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getMessage()Ljava/lang/CharSequence;

    move-result-object p1

    goto :goto_24

    nop

    :goto_12
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnShowListener()Landroid/content/DialogInterface$OnShowListener;

    move-result-object p1

    goto :goto_5e

    nop

    :goto_13
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_62

    nop

    :goto_14
    if-nez p1, :cond_2

    goto :goto_3f

    :cond_2
    goto :goto_4e

    nop

    :goto_15
    invoke-virtual {v0, p1}, Lmiuix/internal/widget/ArrowActionSheet;->setMessage(Ljava/lang/CharSequence;)V

    :goto_16
    goto :goto_3b

    nop

    :goto_17
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_44

    nop

    :goto_18
    invoke-virtual {v0, p1}, Lmiuix/internal/widget/ArrowActionSheet;->setActionSheetOnDismissListener(Landroid/content/DialogInterface$OnDismissListener;)V

    :goto_19
    goto :goto_40

    nop

    :goto_1a
    return-object v0

    :goto_1b
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_52

    nop

    :goto_1c
    if-nez p1, :cond_3

    goto :goto_5f

    :cond_3
    goto :goto_28

    nop

    :goto_1d
    if-nez p1, :cond_4

    goto :goto_10

    :cond_4
    goto :goto_a

    nop

    :goto_1e
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_3

    nop

    :goto_1f
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getItemTypes()[Lmiuix/internal/widget/ActionSheet$ActionSheetItemType;

    move-result-object p1

    goto :goto_34

    nop

    :goto_20
    invoke-virtual {v0, p1}, Landroid/app/Dialog;->setOnKeyListener(Landroid/content/DialogInterface$OnKeyListener;)V

    goto :goto_1b

    nop

    :goto_21
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnCancelListener()Landroid/content/DialogInterface$OnCancelListener;

    move-result-object p1

    goto :goto_59

    nop

    :goto_22
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getActionItems()[Ljava/lang/CharSequence;

    move-result-object p1

    goto :goto_42

    nop

    :goto_23
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnShowListener()Landroid/content/DialogInterface$OnShowListener;

    move-result-object p1

    goto :goto_1c

    nop

    :goto_24
    if-nez p1, :cond_5

    goto :goto_16

    :cond_5
    goto :goto_53

    nop

    :goto_25
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_11

    nop

    :goto_26
    new-instance v0, Lmiuix/internal/widget/ArrowActionSheet;

    goto :goto_4c

    nop

    :goto_27
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getConfigurationChangedListener()Lmiuix/appcompat/app/AlertDialog$OnConfigurationChangedListener;

    goto :goto_3a

    nop

    :goto_28
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_12

    nop

    :goto_29
    if-nez p1, :cond_6

    goto :goto_e

    :cond_6
    goto :goto_48

    nop

    :goto_2a
    invoke-virtual {v0, p1, v1, v2}, Lmiuix/internal/widget/ArrowActionSheet;->setActionItems([Ljava/lang/CharSequence;[Lmiuix/internal/widget/ActionSheet$ActionSheetItemType;Landroid/content/DialogInterface$OnClickListener;)V

    :goto_2b
    goto :goto_5a

    nop

    :goto_2c
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_56

    nop

    :goto_2d
    if-nez p1, :cond_7

    goto :goto_7

    :cond_7
    goto :goto_60

    nop

    :goto_2e
    invoke-virtual {v1}, Lmiuix/internal/widget/ActionSheetController;->getItemClickListener()Landroid/content/DialogInterface$OnClickListener;

    move-result-object v1

    goto :goto_6

    nop

    :goto_2f
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_61

    nop

    :goto_30
    invoke-virtual {p0}, Lmiuix/internal/widget/AlertActionSheet;->isCanceledOnTouchOutside()Z

    move-result p1

    goto :goto_39

    nop

    :goto_31
    invoke-virtual {v0, p1}, Lmiuix/internal/widget/ArrowActionSheet;->setHapticFeedbackEnabled(Z)V

    goto :goto_30

    nop

    :goto_32
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_41

    nop

    :goto_33
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getListViewAdapter()Landroid/widget/ListAdapter;

    move-result-object p1

    goto :goto_3e

    nop

    :goto_34
    if-nez p1, :cond_8

    goto :goto_2b

    :cond_8
    goto :goto_49

    nop

    :goto_35
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getListViewAdapter()Landroid/widget/ListAdapter;

    move-result-object p1

    goto :goto_14

    nop

    :goto_36
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnKeyListener()Landroid/content/DialogInterface$OnKeyListener;

    move-result-object p1

    goto :goto_1d

    nop

    :goto_37
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getMessage()Ljava/lang/CharSequence;

    move-result-object p1

    goto :goto_15

    nop

    :goto_38
    invoke-virtual {p0}, Lmiuix/internal/widget/AlertActionSheet;->isHapticFeedbackEnabled()Z

    move-result p1

    goto :goto_31

    nop

    :goto_39
    invoke-virtual {v0, p1}, Lmiuix/internal/widget/ArrowActionSheet;->setCanceledOnTouchOutside(Z)V

    goto :goto_25

    nop

    :goto_3a
    iget-object p0, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_c

    nop

    :goto_3b
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_0

    nop

    :goto_3c
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_27

    nop

    :goto_3d
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mArrowMode:Lmiuix/internal/widget/ActionSheet$ArrowMode;

    goto :goto_5b

    nop

    :goto_3e
    invoke-virtual {v0, p1}, Lmiuix/internal/widget/ArrowActionSheet;->setListViewAdapter(Landroid/widget/ListAdapter;)V

    :goto_3f
    goto :goto_17

    nop

    :goto_40
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_36

    nop

    :goto_41
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnDismissListener()Landroid/content/DialogInterface$OnDismissListener;

    move-result-object p1

    goto :goto_18

    nop

    :goto_42
    iget-object v1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_4

    nop

    :goto_43
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getActionItems()[Ljava/lang/CharSequence;

    move-result-object p1

    goto :goto_57

    nop

    :goto_44
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnCancelListener()Landroid/content/DialogInterface$OnCancelListener;

    move-result-object p1

    goto :goto_5c

    nop

    :goto_45
    if-nez p1, :cond_9

    goto :goto_7

    :cond_9
    goto :goto_2c

    nop

    :goto_46
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getShowAnimListener()Lmiuix/appcompat/app/AlertDialog$OnDialogShowAnimListener;

    move-result-object p1

    goto :goto_29

    nop

    :goto_47
    if-nez p1, :cond_a

    goto :goto_2b

    :cond_a
    goto :goto_4a

    nop

    :goto_48
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_5d

    nop

    :goto_49
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_22

    nop

    :goto_4a
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_1f

    nop

    :goto_4b
    iput-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mArrowActionAnchor:Landroid/view/View;

    goto :goto_26

    nop

    :goto_4c
    iget-object v1, p0, Lmiuix/internal/widget/AlertActionSheet;->mContext:Landroid/content/Context;

    goto :goto_54

    nop

    :goto_4d
    iget-object v2, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_8

    nop

    :goto_4e
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_33

    nop

    :goto_4f
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_21

    nop

    :goto_50
    invoke-virtual {v0, p1}, Lmiuix/internal/widget/ArrowActionSheet;->setActionSheetOnCancelListener(Landroid/content/DialogInterface$OnCancelListener;)V

    :goto_51
    goto :goto_3c

    nop

    :goto_52
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnKeyListener()Landroid/content/DialogInterface$OnKeyListener;

    move-result-object p1

    goto :goto_f

    nop

    :goto_53
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_37

    nop

    :goto_54
    invoke-direct {v0, v1, p1}, Lmiuix/internal/widget/ArrowActionSheet;-><init>(Landroid/content/Context;Landroid/view/View;)V

    goto :goto_3d

    nop

    :goto_55
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_23

    nop

    :goto_56
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getItemClickListener()Landroid/content/DialogInterface$OnClickListener;

    move-result-object p1

    goto :goto_2d

    nop

    :goto_57
    iget-object v1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_2e

    nop

    :goto_58
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnKeyListener()Landroid/content/DialogInterface$OnKeyListener;

    move-result-object p1

    goto :goto_20

    nop

    :goto_59
    invoke-virtual {v0, p1}, Landroid/app/Dialog;->setOnCancelListener(Landroid/content/DialogInterface$OnCancelListener;)V

    goto :goto_2f

    nop

    :goto_5a
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_46

    nop

    :goto_5b
    invoke-virtual {v0, p1}, Lmiuix/internal/widget/ArrowActionSheet;->setArrowMode(Lmiuix/internal/widget/ActionSheet$ArrowMode;)V

    goto :goto_38

    nop

    :goto_5c
    if-nez p1, :cond_b

    goto :goto_51

    :cond_b
    goto :goto_4f

    nop

    :goto_5d
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getShowAnimListener()Lmiuix/appcompat/app/AlertDialog$OnDialogShowAnimListener;

    move-result-object p1

    goto :goto_d

    nop

    :goto_5e
    invoke-virtual {v0, p1}, Lmiuix/internal/widget/ArrowActionSheet;->setActionSheetOnShowListener(Landroid/content/DialogInterface$OnShowListener;)V

    :goto_5f
    goto :goto_9

    nop

    :goto_60
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_43

    nop

    :goto_61
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getOnCancelListener()Landroid/content/DialogInterface$OnCancelListener;

    move-result-object p1

    goto :goto_50

    nop

    :goto_62
    invoke-virtual {p1}, Lmiuix/internal/widget/ActionSheetController;->getItemClickListener()Landroid/content/DialogInterface$OnClickListener;

    move-result-object p1

    goto :goto_47

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_widget_AlertActionSheet__dismissForShiftWithoutAnimation',
        'method': '.method protected dismissForShiftWithoutAnimation()V',
        'method_name': 'dismissForShiftWithoutAnimation',
        'method_anchors': ['invoke-virtual {p0, v0}, Lmiuix/internal/widget/AlertActionSheet;->setIsDismissForShift(Z)V', 'invoke-virtual {p0}, Lmiuix/internal/widget/AlertActionSheet;->dismissWithoutAnimation()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected dismissForShiftWithoutAnimation()V
    .registers 2

    const/4 v0, 0x1

    invoke-virtual {p0, v0}, Lmiuix/internal/widget/AlertActionSheet;->setIsDismissForShift(Z)V

    invoke-virtual {p0}, Lmiuix/internal/widget/AlertActionSheet;->dismissWithoutAnimation()V

    return-void
.end method""",
        'replacement': """.method protected dismissForShiftWithoutAnimation()V
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
    invoke-virtual {p0, v0}, Lmiuix/internal/widget/AlertActionSheet;->setIsDismissForShift(Z)V

    goto :goto_3

    nop

    :goto_3
    invoke-virtual {p0}, Lmiuix/internal/widget/AlertActionSheet;->dismissWithoutAnimation()V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_widget_AlertActionSheet__dismissWithAnimationExistDecorView',
        'method': '.method protected dismissWithAnimationExistDecorView(Landroid/view/View;)V',
        'method_name': 'dismissWithAnimationExistDecorView',
        'method_anchors': ['invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;', 'invoke-virtual {p1}, Landroid/view/View;->getHandler()Landroid/os/Handler;', 'invoke-virtual {v1}, Landroid/os/Handler;->getLooper()Landroid/os/Looper;', 'invoke-virtual {v1}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;', 'if-ne v0, v1, :cond_0', 'iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;', 'iget-object p0, p0, Lmiuix/appcompat/app/AlertDialog;->mOnDismiss:Lmiuix/appcompat/widget/DialogAnimHelper$OnDismiss;', 'invoke-virtual {p1, p0}, Lmiuix/internal/widget/ActionSheetController;->dismiss(Lmiuix/appcompat/widget/DialogAnimHelper$OnDismiss;)V'],
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

    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    iget-object p0, p0, Lmiuix/appcompat/app/AlertDialog;->mOnDismiss:Lmiuix/appcompat/widget/DialogAnimHelper$OnDismiss;

    invoke-virtual {p1, p0}, Lmiuix/internal/widget/ActionSheetController;->dismiss(Lmiuix/appcompat/widget/DialogAnimHelper$OnDismiss;)V

    return-void

    :cond_0
    new-instance v0, Lmiuix/internal/widget/AlertActionSheet$$ExternalSyntheticLambda0;

    invoke-direct {v0, p0}, Lmiuix/internal/widget/AlertActionSheet$$ExternalSyntheticLambda0;-><init>(Lmiuix/internal/widget/AlertActionSheet;)V

    invoke-virtual {p1, v0}, Landroid/view/View;->post(Ljava/lang/Runnable;)Z

    return-void
.end method""",
        'replacement': """.method protected dismissWithAnimationExistDecorView(Landroid/view/View;)V
    .registers 4

    goto :goto_5

    nop

    :goto_0
    return-void

    :goto_1
    invoke-virtual {p1, v0}, Landroid/view/View;->post(Ljava/lang/Runnable;)Z

    goto :goto_0

    nop

    :goto_2
    invoke-direct {v0, p0}, Lmiuix/internal/widget/AlertActionSheet$$ExternalSyntheticLambda0;-><init>(Lmiuix/internal/widget/AlertActionSheet;)V

    goto :goto_1

    nop

    :goto_3
    return-void

    :goto_4
    goto :goto_7

    nop

    :goto_5
    invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;

    move-result-object v0

    goto :goto_8

    nop

    :goto_6
    invoke-virtual {v1}, Landroid/os/Handler;->getLooper()Landroid/os/Looper;

    move-result-object v1

    goto :goto_9

    nop

    :goto_7
    new-instance v0, Lmiuix/internal/widget/AlertActionSheet$$ExternalSyntheticLambda0;

    goto :goto_2

    nop

    :goto_8
    invoke-virtual {p1}, Landroid/view/View;->getHandler()Landroid/os/Handler;

    move-result-object v1

    goto :goto_6

    nop

    :goto_9
    invoke-virtual {v1}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;

    move-result-object v1

    goto :goto_d

    nop

    :goto_a
    invoke-virtual {p1, p0}, Lmiuix/internal/widget/ActionSheetController;->dismiss(Lmiuix/appcompat/widget/DialogAnimHelper$OnDismiss;)V

    goto :goto_3

    nop

    :goto_b
    iget-object p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_c

    nop

    :goto_c
    iget-object p0, p0, Lmiuix/appcompat/app/AlertDialog;->mOnDismiss:Lmiuix/appcompat/widget/DialogAnimHelper$OnDismiss;

    goto :goto_a

    nop

    :goto_d
    if-eq v0, v1, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_b

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_widget_AlertActionSheet__isDismissForShift',
        'method': '.method protected isDismissForShift()Z',
        'method_name': 'isDismissForShift',
        'method_anchors': ['iget-boolean p0, p0, Lmiuix/internal/widget/AlertActionSheet;->mIsDismissForShift:Z', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected isDismissForShift()Z
    .registers 1

    iget-boolean p0, p0, Lmiuix/internal/widget/AlertActionSheet;->mIsDismissForShift:Z

    return p0
.end method""",
        'replacement': """.method protected isDismissForShift()Z
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    iget-boolean p0, p0, Lmiuix/internal/widget/AlertActionSheet;->mIsDismissForShift:Z

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_widget_AlertActionSheet__isFromArrowShape',
        'method': '.method protected isFromArrowShape()Z',
        'method_name': 'isFromArrowShape',
        'method_anchors': ['iget-boolean p0, p0, Lmiuix/internal/widget/AlertActionSheet;->mIsFromArrowShape:Z', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected isFromArrowShape()Z
    .registers 1

    iget-boolean p0, p0, Lmiuix/internal/widget/AlertActionSheet;->mIsFromArrowShape:Z

    return p0
.end method""",
        'replacement': """.method protected isFromArrowShape()Z
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    iget-boolean p0, p0, Lmiuix/internal/widget/AlertActionSheet;->mIsFromArrowShape:Z

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_widget_AlertActionSheet__onCreate',
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

    iget-object p0, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p0, p1}, Lmiuix/internal/widget/ActionSheetController;->installContent(Landroid/os/Bundle;)V

    return-void
.end method""",
        'replacement': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 4

    goto :goto_1

    nop

    :goto_0
    if-nez v0, :cond_0

    goto :goto_8

    :cond_0
    goto :goto_7

    nop

    :goto_1
    invoke-virtual {p0}, Lmiuix/appcompat/app/AlertDialog;->isSystemSpecialUiThread()Z

    move-result v0

    goto :goto_a

    nop

    :goto_2
    invoke-virtual {v0, v1}, Landroid/view/Window;->setWindowAnimations(I)V

    goto :goto_b

    nop

    :goto_3
    invoke-virtual {v0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    goto :goto_6

    nop

    :goto_4
    iget-object p0, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_9

    nop

    :goto_5
    return-void

    :goto_6
    const/4 v1, 0x0

    goto :goto_2

    nop

    :goto_7
    invoke-virtual {v0}, Lmiuix/appcompat/app/AlertDialog$LifecycleOwnerCompat;->onCreate()V

    :goto_8
    goto :goto_c

    nop

    :goto_9
    invoke-virtual {p0, p1}, Lmiuix/internal/widget/ActionSheetController;->installContent(Landroid/os/Bundle;)V

    goto :goto_5

    nop

    :goto_a
    if-nez v0, :cond_1

    goto :goto_8

    :cond_1
    goto :goto_d

    nop

    :goto_b
    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AlertDialog;->superOnCreate(Landroid/os/Bundle;)V

    goto :goto_4

    nop

    :goto_c
    invoke-virtual {p0}, Landroid/app/Dialog;->getWindow()Landroid/view/Window;

    move-result-object v0

    goto :goto_3

    nop

    :goto_d
    iget-object v0, p0, Lmiuix/appcompat/app/AlertDialog;->mLifecycleOwnerCompat:Lmiuix/appcompat/app/AlertDialog$LifecycleOwnerCompat;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_widget_AlertActionSheet__onStart',
        'method': '.method protected onStart()V',
        'method_name': 'onStart',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/appcompat/app/AlertDialog;->superOnStart()V', 'iget-object p0, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;', 'invoke-virtual {p0}, Lmiuix/internal/widget/ActionSheetController;->onStart()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onStart()V
    .registers 1

    invoke-virtual {p0}, Lmiuix/appcompat/app/AlertDialog;->superOnStart()V

    iget-object p0, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    invoke-virtual {p0}, Lmiuix/internal/widget/ActionSheetController;->onStart()V

    return-void
.end method""",
        'replacement': """.method protected onStart()V
    .registers 1

    goto :goto_2

    nop

    :goto_0
    return-void

    :goto_1
    invoke-virtual {p0}, Lmiuix/internal/widget/ActionSheetController;->onStart()V

    goto :goto_0

    nop

    :goto_2
    invoke-virtual {p0}, Lmiuix/appcompat/app/AlertDialog;->superOnStart()V

    goto :goto_3

    nop

    :goto_3
    iget-object p0, p0, Lmiuix/internal/widget/AlertActionSheet;->mActionController:Lmiuix/internal/widget/ActionSheetController;

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_widget_AlertActionSheet__onStop',
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

    goto :goto_a

    nop

    :goto_0
    invoke-virtual {p0}, Lmiuix/appcompat/app/AlertDialog$LifecycleOwnerCompat;->onStopAfter()V

    :goto_1
    goto :goto_8

    nop

    :goto_2
    iget-object p0, p0, Lmiuix/appcompat/app/AlertDialog;->mLifecycleOwnerCompat:Lmiuix/appcompat/app/AlertDialog$LifecycleOwnerCompat;

    goto :goto_3

    nop

    :goto_3
    if-nez p0, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_0

    nop

    :goto_4
    invoke-virtual {p0}, Lmiuix/appcompat/app/AlertDialog;->isSystemSpecialUiThread()Z

    move-result v0

    goto :goto_b

    nop

    :goto_5
    invoke-virtual {p0}, Lmiuix/appcompat/app/AlertDialog;->superOnStop()V

    goto :goto_4

    nop

    :goto_6
    if-nez v0, :cond_1

    goto :goto_d

    :cond_1
    goto :goto_7

    nop

    :goto_7
    iget-object v0, p0, Lmiuix/appcompat/app/AlertDialog;->mLifecycleOwnerCompat:Lmiuix/appcompat/app/AlertDialog$LifecycleOwnerCompat;

    goto :goto_9

    nop

    :goto_8
    return-void

    :goto_9
    if-nez v0, :cond_2

    goto :goto_d

    :cond_2
    goto :goto_c

    nop

    :goto_a
    invoke-virtual {p0}, Lmiuix/appcompat/app/AlertDialog;->isSystemSpecialUiThread()Z

    move-result v0

    goto :goto_6

    nop

    :goto_b
    if-nez v0, :cond_3

    goto :goto_1

    :cond_3
    goto :goto_2

    nop

    :goto_c
    invoke-virtual {v0}, Lmiuix/appcompat/app/AlertDialog$LifecycleOwnerCompat;->onStopBefore()V

    :goto_d
    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_widget_AlertActionSheet__setIsDismissForShift',
        'method': '.method protected setIsDismissForShift(Z)V',
        'method_name': 'setIsDismissForShift',
        'method_anchors': ['iput-boolean p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mIsDismissForShift:Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected setIsDismissForShift(Z)V
    .registers 2

    iput-boolean p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mIsDismissForShift:Z

    return-void
.end method""",
        'replacement': """.method protected setIsDismissForShift(Z)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    iput-boolean p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mIsDismissForShift:Z

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_widget_AlertActionSheet__setIsFromArrowShape',
        'method': '.method protected setIsFromArrowShape(Z)V',
        'method_name': 'setIsFromArrowShape',
        'method_anchors': ['iput-boolean p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mIsFromArrowShape:Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected setIsFromArrowShape(Z)V
    .registers 2

    iput-boolean p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mIsFromArrowShape:Z

    return-void
.end method""",
        'replacement': """.method protected setIsFromArrowShape(Z)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    iput-boolean p1, p0, Lmiuix/internal/widget/AlertActionSheet;->mIsFromArrowShape:Z

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
