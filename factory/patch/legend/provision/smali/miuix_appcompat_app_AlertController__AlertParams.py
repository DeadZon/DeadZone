TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/app/AlertController$AlertParams.smali'
CLASS_FALLBACK_NAMES = ['AlertController$AlertParams.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'miuix_appcompat_app_AlertController__AlertParams__apply',
        'method': '.method apply(Lmiuix/appcompat/app/AlertController;)V',
        'method_name': 'apply',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mCustomTitleView:Landroid/view/View;', 'if-eqz v0, :cond_0', 'invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setCustomTitle(Landroid/view/View;)V', 'iget-object v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mTitle:Ljava/lang/CharSequence;', 'if-eqz v0, :cond_1', 'invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setTitle(Ljava/lang/CharSequence;)V', 'iget-object v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mIcon:Landroid/graphics/drawable/Drawable;', 'if-eqz v0, :cond_2'],
        'type': 'method_replace',
        'search': """.method apply(Lmiuix/appcompat/app/AlertController;)V
    .registers 6

    iget-object v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mCustomTitleView:Landroid/view/View;

    if-eqz v0, :cond_0

    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setCustomTitle(Landroid/view/View;)V

    goto :goto_0

    :cond_0
    iget-object v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mTitle:Ljava/lang/CharSequence;

    if-eqz v0, :cond_1

    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setTitle(Ljava/lang/CharSequence;)V

    :cond_1
    iget-object v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mIcon:Landroid/graphics/drawable/Drawable;

    if-eqz v0, :cond_2

    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setIcon(Landroid/graphics/drawable/Drawable;)V

    :cond_2
    iget v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mIconId:I

    if-eqz v0, :cond_3

    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setIcon(I)V

    :cond_3
    iget v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mIconAttrId:I

    if-eqz v0, :cond_4

    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->getIconAttributeResId(I)I

    move-result v0

    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setIcon(I)V

    :cond_4
    iget-boolean v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mSmallIcon:Z

    if-eqz v0, :cond_5

    const/4 v0, 0x1

    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setUseSmallIcon(Z)V

    :cond_5
    iget v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->iconWidth:I

    if-eqz v0, :cond_6

    iget v1, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->iconHeight:I

    if-eqz v1, :cond_6

    invoke-virtual {p1, v0, v1}, Lmiuix/appcompat/app/AlertController;->setIconSize(II)V

    :cond_6
    :goto_0
    iget-object v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mMessage:Ljava/lang/CharSequence;

    if-eqz v0, :cond_7

    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setMessage(Ljava/lang/CharSequence;)V

    :cond_7
    iget-object v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mComment:Ljava/lang/CharSequence;

    if-eqz v0, :cond_8

    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setComment(Ljava/lang/CharSequence;)V

    :cond_8
    iget-object v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mPositiveButtonText:Ljava/lang/CharSequence;

    const/4 v1, 0x0

    if-eqz v0, :cond_9

    const/4 v2, -0x1

    iget-object v3, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mPositiveButtonListener:Landroid/content/DialogInterface$OnClickListener;

    invoke-virtual {p1, v2, v0, v3, v1}, Lmiuix/appcompat/app/AlertController;->setButton(ILjava/lang/CharSequence;Landroid/content/DialogInterface$OnClickListener;Landroid/os/Message;)V

    :cond_9
    iget-object v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mNegativeButtonText:Ljava/lang/CharSequence;

    if-eqz v0, :cond_a

    const/4 v2, -0x2

    iget-object v3, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mNegativeButtonListener:Landroid/content/DialogInterface$OnClickListener;

    invoke-virtual {p1, v2, v0, v3, v1}, Lmiuix/appcompat/app/AlertController;->setButton(ILjava/lang/CharSequence;Landroid/content/DialogInterface$OnClickListener;Landroid/os/Message;)V

    :cond_a
    iget-object v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mNeutralButtonText:Ljava/lang/CharSequence;

    if-eqz v0, :cond_b

    const/4 v2, -0x3

    iget-object v3, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mNeutralButtonListener:Landroid/content/DialogInterface$OnClickListener;

    invoke-virtual {p1, v2, v0, v3, v1}, Lmiuix/appcompat/app/AlertController;->setButton(ILjava/lang/CharSequence;Landroid/content/DialogInterface$OnClickListener;Landroid/os/Message;)V

    :cond_b
    iget-object v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mExtraButtonList:Ljava/util/List;

    if-eqz v0, :cond_c

    new-instance v0, Ljava/util/ArrayList;

    iget-object v2, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mExtraButtonList:Ljava/util/List;

    invoke-direct {v0, v2}, Ljava/util/ArrayList;-><init>(Ljava/util/Collection;)V

    invoke-static {p1, v0}, Lmiuix/appcompat/app/AlertController;->access$502(Lmiuix/appcompat/app/AlertController;Ljava/util/List;)Ljava/util/List;

    :cond_c
    iget-object v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mItems:[Ljava/lang/CharSequence;

    if-nez v0, :cond_d

    iget-object v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mCursor:Landroid/database/Cursor;

    if-nez v0, :cond_d

    iget-object v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mAdapter:Landroid/widget/ListAdapter;

    if-eqz v0, :cond_e

    :cond_d
    invoke-direct {p0, p1}, Lmiuix/appcompat/app/AlertController$AlertParams;->createListView(Lmiuix/appcompat/app/AlertController;)V

    :cond_e
    iget-object v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mView:Landroid/view/View;

    if-eqz v0, :cond_f

    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setView(Landroid/view/View;)V

    goto :goto_1

    :cond_f
    iget v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mViewLayoutResId:I

    if-eqz v0, :cond_10

    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setView(I)V

    :cond_10
    :goto_1
    iget-object v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mCheckBoxMessage:Ljava/lang/CharSequence;

    if-eqz v0, :cond_11

    iget-boolean v2, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mIsChecked:Z

    invoke-virtual {p1, v2, v0}, Lmiuix/appcompat/app/AlertController;->setCheckBox(ZLjava/lang/CharSequence;)V

    :cond_11
    iget-boolean v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mHapticFeedbackEnabled:Z

    iput-boolean v0, p1, Lmiuix/appcompat/app/AlertController;->mHapticFeedbackEnabled:Z

    iget-boolean v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mEnableDialogImmersive:Z

    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setEnableImmersive(Z)V

    iget v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mNonImmersiveDialogHeight:I

    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setNonImmersiveDialogHeight(I)V

    iget v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mLiteVersion:I

    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setLiteVersion(I)V

    iget-boolean v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mPreferLandscape:Z

    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setPreferLandscape(Z)V

    iget-boolean v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mButtonForceVertical:Z

    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setButtonForceVertical(Z)V

    iget-boolean v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mPrimaryButtonFirstEnabled:Z

    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setPrimaryButtonFirstEnabled(Z)V

    iget-boolean v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mAsyncInflatePanelEnabled:Z

    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setAsyncInflatePanelEnable(Z)V

    iget-boolean v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mDiscardImeAnimEnabled:Z

    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setDiscardImeAnimEnabled(Z)V

    invoke-virtual {p1, v1}, Lmiuix/appcompat/app/AlertController;->setPanelSizeChangedListener(Lmiuix/appcompat/app/AlertDialog$OnPanelSizeChangedListener;)V

    invoke-virtual {p1, v1}, Lmiuix/appcompat/app/AlertController;->setConfigurationChangedListener(Lmiuix/appcompat/app/AlertDialog$OnConfigurationChangedListener;)V

    iget-boolean v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mEnableEnterAnim:Z

    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setEnableEnterAnim(Z)V

    iget-boolean p0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mUseForceFlipCutout:Z

    invoke-virtual {p1, p0}, Lmiuix/appcompat/app/AlertController;->setUseForceFlipCutout(Z)V

    return-void
.end method""",
        'replacement': """.method apply(Lmiuix/appcompat/app/AlertController;)V
    .registers 6

    goto :goto_6b

    nop

    :goto_0
    invoke-static {p1, v0}, Lmiuix/appcompat/app/AlertController;->access$502(Lmiuix/appcompat/app/AlertController;Ljava/util/List;)Ljava/util/List;

    :goto_1
    goto :goto_56

    nop

    :goto_2
    return-void

    :goto_3
    iget-object v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mAdapter:Landroid/widget/ListAdapter;

    goto :goto_25

    nop

    :goto_4
    iget-object v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mIcon:Landroid/graphics/drawable/Drawable;

    goto :goto_47

    nop

    :goto_5
    const/4 v1, 0x0

    goto :goto_66

    nop

    :goto_6
    iget-object v3, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mNeutralButtonListener:Landroid/content/DialogInterface$OnClickListener;

    goto :goto_1a

    nop

    :goto_7
    const/4 v2, -0x1

    goto :goto_4e

    nop

    :goto_8
    iget-boolean v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mSmallIcon:Z

    goto :goto_5e

    nop

    :goto_9
    iget-boolean v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mDiscardImeAnimEnabled:Z

    goto :goto_2b

    nop

    :goto_a
    invoke-virtual {p1, v1}, Lmiuix/appcompat/app/AlertController;->setConfigurationChangedListener(Lmiuix/appcompat/app/AlertDialog$OnConfigurationChangedListener;)V

    goto :goto_2c

    nop

    :goto_b
    invoke-virtual {p1, p0}, Lmiuix/appcompat/app/AlertController;->setUseForceFlipCutout(Z)V

    goto :goto_2

    nop

    :goto_c
    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setAsyncInflatePanelEnable(Z)V

    goto :goto_9

    nop

    :goto_d
    if-nez v0, :cond_0

    goto :goto_6f

    :cond_0
    goto :goto_34

    nop

    :goto_e
    iget-boolean v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mHapticFeedbackEnabled:Z

    goto :goto_1d

    nop

    :goto_f
    if-nez v0, :cond_1

    goto :goto_1

    :cond_1
    goto :goto_46

    nop

    :goto_10
    iget v1, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->iconHeight:I

    goto :goto_24

    nop

    :goto_11
    iget-object v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mCheckBoxMessage:Ljava/lang/CharSequence;

    goto :goto_61

    nop

    :goto_12
    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setView(I)V

    :goto_13
    goto :goto_11

    nop

    :goto_14
    if-nez v0, :cond_2

    goto :goto_6a

    :cond_2
    goto :goto_20

    nop

    :goto_15
    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setMessage(Ljava/lang/CharSequence;)V

    :goto_16
    goto :goto_42

    nop

    :goto_17
    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setNonImmersiveDialogHeight(I)V

    goto :goto_4a

    nop

    :goto_18
    if-nez v0, :cond_3

    goto :goto_13

    :cond_3
    goto :goto_12

    nop

    :goto_19
    iget-object v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mNegativeButtonText:Ljava/lang/CharSequence;

    goto :goto_d

    nop

    :goto_1a
    invoke-virtual {p1, v2, v0, v3, v1}, Lmiuix/appcompat/app/AlertController;->setButton(ILjava/lang/CharSequence;Landroid/content/DialogInterface$OnClickListener;Landroid/os/Message;)V

    :goto_1b
    goto :goto_31

    nop

    :goto_1c
    iget-boolean v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mPreferLandscape:Z

    goto :goto_55

    nop

    :goto_1d
    iput-boolean v0, p1, Lmiuix/appcompat/app/AlertController;->mHapticFeedbackEnabled:Z

    goto :goto_35

    nop

    :goto_1e
    iget v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->iconWidth:I

    goto :goto_40

    nop

    :goto_1f
    if-eqz v0, :cond_4

    goto :goto_26

    :cond_4
    goto :goto_3

    nop

    :goto_20
    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->getIconAttributeResId(I)I

    move-result v0

    goto :goto_69

    nop

    :goto_21
    iget-object v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mView:Landroid/view/View;

    goto :goto_62

    nop

    :goto_22
    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setIcon(Landroid/graphics/drawable/Drawable;)V

    :goto_23
    goto :goto_38

    nop

    :goto_24
    if-nez v1, :cond_5

    goto :goto_59

    :cond_5
    goto :goto_58

    nop

    :goto_25
    if-nez v0, :cond_6

    goto :goto_2f

    :cond_6
    :goto_26
    goto :goto_2e

    nop

    :goto_27
    if-nez v0, :cond_7

    goto :goto_51

    :cond_7
    goto :goto_50

    nop

    :goto_28
    if-nez v0, :cond_8

    goto :goto_49

    :cond_8
    goto :goto_48

    nop

    :goto_29
    goto :goto_13

    :goto_2a
    goto :goto_64

    nop

    :goto_2b
    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setDiscardImeAnimEnabled(Z)V

    goto :goto_54

    nop

    :goto_2c
    iget-boolean v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mEnableEnterAnim:Z

    goto :goto_53

    nop

    :goto_2d
    iget-object v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mTitle:Ljava/lang/CharSequence;

    goto :goto_71

    nop

    :goto_2e
    invoke-direct {p0, p1}, Lmiuix/appcompat/app/AlertController$AlertParams;->createListView(Lmiuix/appcompat/app/AlertController;)V

    :goto_2f
    goto :goto_21

    nop

    :goto_30
    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setCustomTitle(Landroid/view/View;)V

    goto :goto_6c

    nop

    :goto_31
    iget-object v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mExtraButtonList:Ljava/util/List;

    goto :goto_f

    nop

    :goto_32
    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setTitle(Ljava/lang/CharSequence;)V

    :goto_33
    goto :goto_4

    nop

    :goto_34
    const/4 v2, -0x2

    goto :goto_70

    nop

    :goto_35
    iget-boolean v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mEnableDialogImmersive:Z

    goto :goto_3e

    nop

    :goto_36
    iget v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mIconAttrId:I

    goto :goto_14

    nop

    :goto_37
    iget-object v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mMessage:Ljava/lang/CharSequence;

    goto :goto_39

    nop

    :goto_38
    iget v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mIconId:I

    goto :goto_27

    nop

    :goto_39
    if-nez v0, :cond_9

    goto :goto_16

    :cond_9
    goto :goto_15

    nop

    :goto_3a
    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setUseSmallIcon(Z)V

    :goto_3b
    goto :goto_1e

    nop

    :goto_3c
    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setLiteVersion(I)V

    goto :goto_1c

    nop

    :goto_3d
    iget-object v2, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mExtraButtonList:Ljava/util/List;

    goto :goto_4c

    nop

    :goto_3e
    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setEnableImmersive(Z)V

    goto :goto_45

    nop

    :goto_3f
    const/4 v2, -0x3

    goto :goto_6

    nop

    :goto_40
    if-nez v0, :cond_a

    goto :goto_59

    :cond_a
    goto :goto_10

    nop

    :goto_41
    const/4 v0, 0x1

    goto :goto_3a

    nop

    :goto_42
    iget-object v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mComment:Ljava/lang/CharSequence;

    goto :goto_28

    nop

    :goto_43
    iget-boolean v2, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mIsChecked:Z

    goto :goto_5f

    nop

    :goto_44
    if-nez v0, :cond_b

    goto :goto_6d

    :cond_b
    goto :goto_30

    nop

    :goto_45
    iget v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mNonImmersiveDialogHeight:I

    goto :goto_17

    nop

    :goto_46
    new-instance v0, Ljava/util/ArrayList;

    goto :goto_3d

    nop

    :goto_47
    if-nez v0, :cond_c

    goto :goto_23

    :cond_c
    goto :goto_22

    nop

    :goto_48
    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setComment(Ljava/lang/CharSequence;)V

    :goto_49
    goto :goto_67

    nop

    :goto_4a
    iget v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mLiteVersion:I

    goto :goto_3c

    nop

    :goto_4b
    iget-object v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mCursor:Landroid/database/Cursor;

    goto :goto_1f

    nop

    :goto_4c
    invoke-direct {v0, v2}, Ljava/util/ArrayList;-><init>(Ljava/util/Collection;)V

    goto :goto_0

    nop

    :goto_4d
    iget-boolean v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mPrimaryButtonFirstEnabled:Z

    goto :goto_5a

    nop

    :goto_4e
    iget-object v3, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mPositiveButtonListener:Landroid/content/DialogInterface$OnClickListener;

    goto :goto_5c

    nop

    :goto_4f
    if-eqz v0, :cond_d

    goto :goto_26

    :cond_d
    goto :goto_4b

    nop

    :goto_50
    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setIcon(I)V

    :goto_51
    goto :goto_36

    nop

    :goto_52
    iget-boolean v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mAsyncInflatePanelEnabled:Z

    goto :goto_c

    nop

    :goto_53
    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setEnableEnterAnim(Z)V

    goto :goto_57

    nop

    :goto_54
    invoke-virtual {p1, v1}, Lmiuix/appcompat/app/AlertController;->setPanelSizeChangedListener(Lmiuix/appcompat/app/AlertDialog$OnPanelSizeChangedListener;)V

    goto :goto_a

    nop

    :goto_55
    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setPreferLandscape(Z)V

    goto :goto_63

    nop

    :goto_56
    iget-object v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mItems:[Ljava/lang/CharSequence;

    goto :goto_4f

    nop

    :goto_57
    iget-boolean p0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mUseForceFlipCutout:Z

    goto :goto_b

    nop

    :goto_58
    invoke-virtual {p1, v0, v1}, Lmiuix/appcompat/app/AlertController;->setIconSize(II)V

    :goto_59
    goto :goto_37

    nop

    :goto_5a
    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setPrimaryButtonFirstEnabled(Z)V

    goto :goto_52

    nop

    :goto_5b
    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setView(Landroid/view/View;)V

    goto :goto_29

    nop

    :goto_5c
    invoke-virtual {p1, v2, v0, v3, v1}, Lmiuix/appcompat/app/AlertController;->setButton(ILjava/lang/CharSequence;Landroid/content/DialogInterface$OnClickListener;Landroid/os/Message;)V

    :goto_5d
    goto :goto_19

    nop

    :goto_5e
    if-nez v0, :cond_e

    goto :goto_3b

    :cond_e
    goto :goto_41

    nop

    :goto_5f
    invoke-virtual {p1, v2, v0}, Lmiuix/appcompat/app/AlertController;->setCheckBox(ZLjava/lang/CharSequence;)V

    :goto_60
    goto :goto_e

    nop

    :goto_61
    if-nez v0, :cond_f

    goto :goto_60

    :cond_f
    goto :goto_43

    nop

    :goto_62
    if-nez v0, :cond_10

    goto :goto_2a

    :cond_10
    goto :goto_5b

    nop

    :goto_63
    iget-boolean v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mButtonForceVertical:Z

    goto :goto_68

    nop

    :goto_64
    iget v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mViewLayoutResId:I

    goto :goto_18

    nop

    :goto_65
    if-nez v0, :cond_11

    goto :goto_1b

    :cond_11
    goto :goto_3f

    nop

    :goto_66
    if-nez v0, :cond_12

    goto :goto_5d

    :cond_12
    goto :goto_7

    nop

    :goto_67
    iget-object v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mPositiveButtonText:Ljava/lang/CharSequence;

    goto :goto_5

    nop

    :goto_68
    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setButtonForceVertical(Z)V

    goto :goto_4d

    nop

    :goto_69
    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertController;->setIcon(I)V

    :goto_6a
    goto :goto_8

    nop

    :goto_6b
    iget-object v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mCustomTitleView:Landroid/view/View;

    goto :goto_44

    nop

    :goto_6c
    goto :goto_59

    :goto_6d
    goto :goto_2d

    nop

    :goto_6e
    invoke-virtual {p1, v2, v0, v3, v1}, Lmiuix/appcompat/app/AlertController;->setButton(ILjava/lang/CharSequence;Landroid/content/DialogInterface$OnClickListener;Landroid/os/Message;)V

    :goto_6f
    goto :goto_72

    nop

    :goto_70
    iget-object v3, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mNegativeButtonListener:Landroid/content/DialogInterface$OnClickListener;

    goto :goto_6e

    nop

    :goto_71
    if-nez v0, :cond_13

    goto :goto_33

    :cond_13
    goto :goto_32

    nop

    :goto_72
    iget-object v0, p0, Lmiuix/appcompat/app/AlertController$AlertParams;->mNeutralButtonText:Ljava/lang/CharSequence;

    goto :goto_65

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
