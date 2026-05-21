TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/app/PairingDialog.smali'
CLASS_FALLBACK_NAMES = ['PairingDialog.smali']
CLASS_ANCHORS = ['.super Lmiuix/appcompat/app/AlertDialog;']

PATCHES = [
    {
        'id': 'miuix_appcompat_app_PairingDialog__onCreate',
        'method': '.method protected onCreate(Landroid/os/Bundle;)V',
        'method_name': 'onCreate',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/app/AlertDialog;->mAlert:Lmiuix/appcompat/app/AlertController;', 'iget-boolean v1, p0, Lmiuix/appcompat/app/PairingDialog;->mNavigationBarHiddenEnabled:Z', 'if-eqz v1, :cond_0', 'iget-boolean v1, p0, Lmiuix/appcompat/app/PairingDialog;->mIsFullScreenGestureMode:Z', 'if-eqz v1, :cond_0', 'invoke-virtual {v0, v1}, Lmiuix/appcompat/app/AlertController;->setNavigationHiddenEnabled(Z)V', 'iget-object v0, p0, Lmiuix/appcompat/app/PairingDialog;->mContext:Landroid/content/Context;', 'invoke-virtual {v0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;'],
        'type': 'method_replace',
        'search': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 7

    iget-object v0, p0, Lmiuix/appcompat/app/AlertDialog;->mAlert:Lmiuix/appcompat/app/AlertController;

    iget-boolean v1, p0, Lmiuix/appcompat/app/PairingDialog;->mNavigationBarHiddenEnabled:Z

    const/4 v2, 0x1

    const/4 v3, 0x0

    if-eqz v1, :cond_0

    iget-boolean v1, p0, Lmiuix/appcompat/app/PairingDialog;->mIsFullScreenGestureMode:Z

    if-eqz v1, :cond_0

    move v1, v2

    goto :goto_0

    :cond_0
    move v1, v3

    :goto_0
    invoke-virtual {v0, v1}, Lmiuix/appcompat/app/AlertController;->setNavigationHiddenEnabled(Z)V

    iget-object v0, p0, Lmiuix/appcompat/app/PairingDialog;->mContext:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    invoke-virtual {v0}, Landroid/content/res/Resources;->getConfiguration()Landroid/content/res/Configuration;

    move-result-object v0

    invoke-direct {p0, v0}, Lmiuix/appcompat/app/PairingDialog;->updateParentPanelFixedHeight(Landroid/content/res/Configuration;)I

    invoke-virtual {p0}, Landroid/app/Dialog;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-static {v0}, Landroid/view/LayoutInflater;->from(Landroid/content/Context;)Landroid/view/LayoutInflater;

    move-result-object v0

    sget v1, Lmiuix/appcompat/R$layout;->miuix_appcompat_pairing_dialog_content:I

    const/4 v4, 0x0

    invoke-virtual {v0, v1, v4}, Landroid/view/LayoutInflater;->inflate(ILandroid/view/ViewGroup;)Landroid/view/View;

    move-result-object v0

    invoke-direct {p0, v0}, Lmiuix/appcompat/app/PairingDialog;->beforeInstallDialogContent(Landroid/view/View;)V

    invoke-direct {p0}, Lmiuix/appcompat/app/PairingDialog;->setupTitle()V

    invoke-direct {p0}, Lmiuix/appcompat/app/PairingDialog;->setupMessageView()V

    invoke-direct {p0}, Lmiuix/appcompat/app/PairingDialog;->setupCustomContent()V

    invoke-direct {p0}, Lmiuix/appcompat/app/PairingDialog;->setupLabelImage()V

    invoke-virtual {p0, v0}, Lmiuix/appcompat/app/AlertDialog;->setView(Landroid/view/View;)V

    invoke-super {p0, p1}, Lmiuix/appcompat/app/AlertDialog;->onCreate(Landroid/os/Bundle;)V

    invoke-direct {p0}, Lmiuix/appcompat/app/PairingDialog;->afterInstallDialogContent()V

    iget-object p1, p0, Lmiuix/appcompat/app/PairingDialog;->mDialogParentPanel:Lmiuix/appcompat/internal/widget/DialogParentPanel2;

    invoke-direct {p0, p1}, Lmiuix/appcompat/app/PairingDialog;->setParentPanelConfigChangedCallback(Lmiuix/appcompat/internal/widget/DialogParentPanel2;)V

    iget-object p1, p0, Lmiuix/appcompat/app/PairingDialog;->mDialogParentPanel:Lmiuix/appcompat/internal/widget/DialogParentPanel2;

    iget-object v0, p0, Lmiuix/appcompat/app/PairingDialog;->mDialogContentPanel:Landroid/view/ViewGroup;

    iget-object v1, p0, Lmiuix/appcompat/app/PairingDialog;->mDialogButtonPanel:Landroid/view/ViewGroup;

    invoke-direct {p0, p1, v0, v1}, Lmiuix/appcompat/app/PairingDialog;->fixedButtonPanelToBottom(Landroid/view/ViewGroup;Landroid/view/ViewGroup;Landroid/view/ViewGroup;)V

    iget-object p1, p0, Lmiuix/appcompat/app/PairingDialog;->mDialogParentPanel:Lmiuix/appcompat/internal/widget/DialogParentPanel2;

    if-eqz p1, :cond_1

    iget-object v0, p0, Lmiuix/appcompat/app/PairingDialog;->mContext:Landroid/content/Context;

    invoke-direct {p0, v0}, Lmiuix/appcompat/app/PairingDialog;->getPanelCornerRadius(Landroid/content/Context;)F

    move-result v0

    invoke-virtual {p1, v0}, Lmiuix/appcompat/internal/widget/DialogParentPanel2;->setCornerRadius(F)V

    iget-object p1, p0, Lmiuix/appcompat/app/PairingDialog;->mDialogParentPanel:Lmiuix/appcompat/internal/widget/DialogParentPanel2;

    invoke-virtual {p1}, Landroid/widget/LinearLayout;->getPaddingStart()I

    move-result v0

    iget-object v1, p0, Lmiuix/appcompat/app/PairingDialog;->mDialogParentPanel:Lmiuix/appcompat/internal/widget/DialogParentPanel2;

    invoke-virtual {v1}, Landroid/widget/LinearLayout;->getPaddingEnd()I

    move-result v1

    iget v4, p0, Lmiuix/appcompat/app/PairingDialog;->mDialogParentPanelPaddingBottom:I

    invoke-virtual {p1, v0, v3, v1, v4}, Landroid/widget/LinearLayout;->setPadding(IIII)V

    :cond_1
    iget-object p1, p0, Lmiuix/appcompat/app/PairingDialog;->mDialogButtonPanel:Landroid/view/ViewGroup;

    if-eqz p1, :cond_3

    instance-of v0, p1, Lmiuix/appcompat/internal/widget/DialogButtonPanel;

    if-eqz v0, :cond_2

    check-cast p1, Lmiuix/appcompat/internal/widget/DialogButtonPanel;

    invoke-virtual {p1, v2}, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->setCustomPaddingEnabled(Z)V

    iget-object p1, p0, Lmiuix/appcompat/app/PairingDialog;->mDialogButtonPanel:Landroid/view/ViewGroup;

    check-cast p1, Lmiuix/appcompat/internal/widget/DialogButtonPanel;

    iget v0, p0, Lmiuix/appcompat/app/PairingDialog;->mDialogButtonPanelHPadding:I

    invoke-virtual {p1, v0}, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->setCustomPaddingHorizontal(I)V

    :cond_2
    iget-object p1, p0, Lmiuix/appcompat/app/PairingDialog;->mDialogButtonPanel:Landroid/view/ViewGroup;

    iget v0, p0, Lmiuix/appcompat/app/PairingDialog;->mDialogButtonPanelHPadding:I

    invoke-virtual {p1}, Landroid/view/ViewGroup;->getPaddingTop()I

    move-result v1

    iget v2, p0, Lmiuix/appcompat/app/PairingDialog;->mDialogButtonPanelHPadding:I

    iget-object v4, p0, Lmiuix/appcompat/app/PairingDialog;->mDialogButtonPanel:Landroid/view/ViewGroup;

    invoke-virtual {v4}, Landroid/view/ViewGroup;->getPaddingBottom()I

    move-result v4

    invoke-virtual {p1, v0, v1, v2, v4}, Landroid/view/ViewGroup;->setPadding(IIII)V

    iget-object p1, p0, Lmiuix/appcompat/app/PairingDialog;->mDialogButtonPanel:Landroid/view/ViewGroup;

    invoke-virtual {p1}, Landroid/view/ViewGroup;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object p1

    instance-of v0, p1, Landroid/view/ViewGroup$MarginLayoutParams;

    if-eqz v0, :cond_3

    check-cast p1, Landroid/view/ViewGroup$MarginLayoutParams;

    iput v3, p1, Landroid/view/ViewGroup$MarginLayoutParams;->topMargin:I

    :cond_3
    sget p1, Lmiuix/appcompat/R$id;->pairingClosable:I

    invoke-virtual {p0, p1}, Landroidx/appcompat/app/AppCompatDialog;->findViewById(I)Landroid/view/View;

    move-result-object p1

    check-cast p1, Landroid/widget/ImageView;

    if-eqz p1, :cond_4

    new-instance v0, Lmiuix/appcompat/app/PairingDialog$1;

    invoke-direct {v0, p0}, Lmiuix/appcompat/app/PairingDialog$1;-><init>(Lmiuix/appcompat/app/PairingDialog;)V

    invoke-virtual {p1, v0}, Landroid/widget/ImageView;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    invoke-static {p1}, Lmiuix/internal/util/AnimHelper;->addPressAnim(Landroid/view/View;)V

    :cond_4
    invoke-direct {p0}, Lmiuix/appcompat/app/PairingDialog;->adjustSpringBackEnabled()V

    return-void
.end method""",
        'replacement': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 7

    goto :goto_50

    nop

    :goto_0
    const/4 v2, 0x1

    goto :goto_46

    nop

    :goto_1
    invoke-direct {p0}, Lmiuix/appcompat/app/PairingDialog;->setupCustomContent()V

    goto :goto_10

    nop

    :goto_2
    invoke-direct {p0}, Lmiuix/appcompat/app/PairingDialog;->adjustSpringBackEnabled()V

    goto :goto_44

    nop

    :goto_3
    iget-object v0, p0, Lmiuix/appcompat/app/PairingDialog;->mContext:Landroid/content/Context;

    goto :goto_27

    nop

    :goto_4
    iget-object p1, p0, Lmiuix/appcompat/app/PairingDialog;->mDialogButtonPanel:Landroid/view/ViewGroup;

    goto :goto_28

    nop

    :goto_5
    iget-object p1, p0, Lmiuix/appcompat/app/PairingDialog;->mDialogButtonPanel:Landroid/view/ViewGroup;

    goto :goto_2a

    nop

    :goto_6
    new-instance v0, Lmiuix/appcompat/app/PairingDialog$1;

    goto :goto_42

    nop

    :goto_7
    invoke-virtual {v0}, Landroid/content/res/Resources;->getConfiguration()Landroid/content/res/Configuration;

    move-result-object v0

    goto :goto_18

    nop

    :goto_8
    iget-object v0, p0, Lmiuix/appcompat/app/PairingDialog;->mContext:Landroid/content/Context;

    goto :goto_4a

    nop

    :goto_9
    iget-object v4, p0, Lmiuix/appcompat/app/PairingDialog;->mDialogButtonPanel:Landroid/view/ViewGroup;

    goto :goto_1d

    nop

    :goto_a
    move v1, v2

    goto :goto_1b

    nop

    :goto_b
    invoke-direct {p0, p1}, Lmiuix/appcompat/app/PairingDialog;->setParentPanelConfigChangedCallback(Lmiuix/appcompat/internal/widget/DialogParentPanel2;)V

    goto :goto_43

    nop

    :goto_c
    check-cast p1, Landroid/view/ViewGroup$MarginLayoutParams;

    goto :goto_48

    nop

    :goto_d
    invoke-virtual {p1, v0}, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->setCustomPaddingHorizontal(I)V

    :goto_e
    goto :goto_51

    nop

    :goto_f
    invoke-virtual {p1, v2}, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->setCustomPaddingEnabled(Z)V

    goto :goto_11

    nop

    :goto_10
    invoke-direct {p0}, Lmiuix/appcompat/app/PairingDialog;->setupLabelImage()V

    goto :goto_32

    nop

    :goto_11
    iget-object p1, p0, Lmiuix/appcompat/app/PairingDialog;->mDialogButtonPanel:Landroid/view/ViewGroup;

    goto :goto_19

    nop

    :goto_12
    invoke-virtual {p1, v0, v3, v1, v4}, Landroid/widget/LinearLayout;->setPadding(IIII)V

    :goto_13
    goto :goto_4

    nop

    :goto_14
    if-nez v0, :cond_0

    goto :goto_49

    :cond_0
    goto :goto_c

    nop

    :goto_15
    check-cast p1, Lmiuix/appcompat/internal/widget/DialogButtonPanel;

    goto :goto_f

    nop

    :goto_16
    iget-object v0, p0, Lmiuix/appcompat/app/PairingDialog;->mDialogContentPanel:Landroid/view/ViewGroup;

    goto :goto_3a

    nop

    :goto_17
    if-nez v1, :cond_1

    goto :goto_1c

    :cond_1
    goto :goto_29

    nop

    :goto_18
    invoke-direct {p0, v0}, Lmiuix/appcompat/app/PairingDialog;->updateParentPanelFixedHeight(Landroid/content/res/Configuration;)I

    goto :goto_40

    nop

    :goto_19
    check-cast p1, Lmiuix/appcompat/internal/widget/DialogButtonPanel;

    goto :goto_4b

    nop

    :goto_1a
    invoke-virtual {p0, p1}, Landroidx/appcompat/app/AppCompatDialog;->findViewById(I)Landroid/view/View;

    move-result-object p1

    goto :goto_36

    nop

    :goto_1b
    goto :goto_2f

    :goto_1c
    goto :goto_2e

    nop

    :goto_1d
    invoke-virtual {v4}, Landroid/view/ViewGroup;->getPaddingBottom()I

    move-result v4

    goto :goto_22

    nop

    :goto_1e
    sget v1, Lmiuix/appcompat/R$layout;->miuix_appcompat_pairing_dialog_content:I

    goto :goto_33

    nop

    :goto_1f
    if-nez p1, :cond_2

    goto :goto_13

    :cond_2
    goto :goto_8

    nop

    :goto_20
    invoke-direct {p0, p1, v0, v1}, Lmiuix/appcompat/app/PairingDialog;->fixedButtonPanelToBottom(Landroid/view/ViewGroup;Landroid/view/ViewGroup;Landroid/view/ViewGroup;)V

    goto :goto_25

    nop

    :goto_21
    invoke-direct {p0}, Lmiuix/appcompat/app/PairingDialog;->afterInstallDialogContent()V

    goto :goto_23

    nop

    :goto_22
    invoke-virtual {p1, v0, v1, v2, v4}, Landroid/view/ViewGroup;->setPadding(IIII)V

    goto :goto_5

    nop

    :goto_23
    iget-object p1, p0, Lmiuix/appcompat/app/PairingDialog;->mDialogParentPanel:Lmiuix/appcompat/internal/widget/DialogParentPanel2;

    goto :goto_b

    nop

    :goto_24
    iget v0, p0, Lmiuix/appcompat/app/PairingDialog;->mDialogButtonPanelHPadding:I

    goto :goto_31

    nop

    :goto_25
    iget-object p1, p0, Lmiuix/appcompat/app/PairingDialog;->mDialogParentPanel:Lmiuix/appcompat/internal/widget/DialogParentPanel2;

    goto :goto_1f

    nop

    :goto_26
    invoke-direct {p0}, Lmiuix/appcompat/app/PairingDialog;->setupTitle()V

    goto :goto_3c

    nop

    :goto_27
    invoke-virtual {v0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    goto :goto_7

    nop

    :goto_28
    if-nez p1, :cond_3

    goto :goto_49

    :cond_3
    goto :goto_3d

    nop

    :goto_29
    iget-boolean v1, p0, Lmiuix/appcompat/app/PairingDialog;->mIsFullScreenGestureMode:Z

    goto :goto_3e

    nop

    :goto_2a
    invoke-virtual {p1}, Landroid/view/ViewGroup;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object p1

    goto :goto_41

    nop

    :goto_2b
    iget-boolean v1, p0, Lmiuix/appcompat/app/PairingDialog;->mNavigationBarHiddenEnabled:Z

    goto :goto_0

    nop

    :goto_2c
    invoke-virtual {p1}, Landroid/widget/LinearLayout;->getPaddingStart()I

    move-result v0

    goto :goto_34

    nop

    :goto_2d
    iget v4, p0, Lmiuix/appcompat/app/PairingDialog;->mDialogParentPanelPaddingBottom:I

    goto :goto_12

    nop

    :goto_2e
    move v1, v3

    :goto_2f
    goto :goto_35

    nop

    :goto_30
    invoke-direct {p0, v0}, Lmiuix/appcompat/app/PairingDialog;->beforeInstallDialogContent(Landroid/view/View;)V

    goto :goto_26

    nop

    :goto_31
    invoke-virtual {p1}, Landroid/view/ViewGroup;->getPaddingTop()I

    move-result v1

    goto :goto_38

    nop

    :goto_32
    invoke-virtual {p0, v0}, Lmiuix/appcompat/app/AlertDialog;->setView(Landroid/view/View;)V

    goto :goto_53

    nop

    :goto_33
    const/4 v4, 0x0

    goto :goto_39

    nop

    :goto_34
    iget-object v1, p0, Lmiuix/appcompat/app/PairingDialog;->mDialogParentPanel:Lmiuix/appcompat/internal/widget/DialogParentPanel2;

    goto :goto_45

    nop

    :goto_35
    invoke-virtual {v0, v1}, Lmiuix/appcompat/app/AlertController;->setNavigationHiddenEnabled(Z)V

    goto :goto_3

    nop

    :goto_36
    check-cast p1, Landroid/widget/ImageView;

    goto :goto_47

    nop

    :goto_37
    if-nez v0, :cond_4

    goto :goto_e

    :cond_4
    goto :goto_15

    nop

    :goto_38
    iget v2, p0, Lmiuix/appcompat/app/PairingDialog;->mDialogButtonPanelHPadding:I

    goto :goto_9

    nop

    :goto_39
    invoke-virtual {v0, v1, v4}, Landroid/view/LayoutInflater;->inflate(ILandroid/view/ViewGroup;)Landroid/view/View;

    move-result-object v0

    goto :goto_30

    nop

    :goto_3a
    iget-object v1, p0, Lmiuix/appcompat/app/PairingDialog;->mDialogButtonPanel:Landroid/view/ViewGroup;

    goto :goto_20

    nop

    :goto_3b
    invoke-virtual {p1, v0}, Lmiuix/appcompat/internal/widget/DialogParentPanel2;->setCornerRadius(F)V

    goto :goto_4d

    nop

    :goto_3c
    invoke-direct {p0}, Lmiuix/appcompat/app/PairingDialog;->setupMessageView()V

    goto :goto_1

    nop

    :goto_3d
    instance-of v0, p1, Lmiuix/appcompat/internal/widget/DialogButtonPanel;

    goto :goto_37

    nop

    :goto_3e
    if-nez v1, :cond_5

    goto :goto_1c

    :cond_5
    goto :goto_a

    nop

    :goto_3f
    invoke-static {v0}, Landroid/view/LayoutInflater;->from(Landroid/content/Context;)Landroid/view/LayoutInflater;

    move-result-object v0

    goto :goto_1e

    nop

    :goto_40
    invoke-virtual {p0}, Landroid/app/Dialog;->getContext()Landroid/content/Context;

    move-result-object v0

    goto :goto_3f

    nop

    :goto_41
    instance-of v0, p1, Landroid/view/ViewGroup$MarginLayoutParams;

    goto :goto_14

    nop

    :goto_42
    invoke-direct {v0, p0}, Lmiuix/appcompat/app/PairingDialog$1;-><init>(Lmiuix/appcompat/app/PairingDialog;)V

    goto :goto_4c

    nop

    :goto_43
    iget-object p1, p0, Lmiuix/appcompat/app/PairingDialog;->mDialogParentPanel:Lmiuix/appcompat/internal/widget/DialogParentPanel2;

    goto :goto_16

    nop

    :goto_44
    return-void

    :goto_45
    invoke-virtual {v1}, Landroid/widget/LinearLayout;->getPaddingEnd()I

    move-result v1

    goto :goto_2d

    nop

    :goto_46
    const/4 v3, 0x0

    goto :goto_17

    nop

    :goto_47
    if-nez p1, :cond_6

    goto :goto_4f

    :cond_6
    goto :goto_6

    nop

    :goto_48
    iput v3, p1, Landroid/view/ViewGroup$MarginLayoutParams;->topMargin:I

    :goto_49
    goto :goto_52

    nop

    :goto_4a
    invoke-direct {p0, v0}, Lmiuix/appcompat/app/PairingDialog;->getPanelCornerRadius(Landroid/content/Context;)F

    move-result v0

    goto :goto_3b

    nop

    :goto_4b
    iget v0, p0, Lmiuix/appcompat/app/PairingDialog;->mDialogButtonPanelHPadding:I

    goto :goto_d

    nop

    :goto_4c
    invoke-virtual {p1, v0}, Landroid/widget/ImageView;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    goto :goto_4e

    nop

    :goto_4d
    iget-object p1, p0, Lmiuix/appcompat/app/PairingDialog;->mDialogParentPanel:Lmiuix/appcompat/internal/widget/DialogParentPanel2;

    goto :goto_2c

    nop

    :goto_4e
    invoke-static {p1}, Lmiuix/internal/util/AnimHelper;->addPressAnim(Landroid/view/View;)V

    :goto_4f
    goto :goto_2

    nop

    :goto_50
    iget-object v0, p0, Lmiuix/appcompat/app/AlertDialog;->mAlert:Lmiuix/appcompat/app/AlertController;

    goto :goto_2b

    nop

    :goto_51
    iget-object p1, p0, Lmiuix/appcompat/app/PairingDialog;->mDialogButtonPanel:Landroid/view/ViewGroup;

    goto :goto_24

    nop

    :goto_52
    sget p1, Lmiuix/appcompat/R$id;->pairingClosable:I

    goto :goto_1a

    nop

    :goto_53
    invoke-super {p0, p1}, Lmiuix/appcompat/app/AlertDialog;->onCreate(Landroid/os/Bundle;)V

    goto :goto_21

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
