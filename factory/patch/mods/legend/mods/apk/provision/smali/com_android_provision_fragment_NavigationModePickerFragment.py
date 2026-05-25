TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/fragment/NavigationModePickerFragment.smali'
CLASS_FALLBACK_NAMES = ['NavigationModePickerFragment.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/fragment/BaseFragment;', '.field private static final TAG:Ljava/lang/String; = "NavigationModePickerFragment"']

PATCHES = [
    {
        'id': 'com_android_provision_fragment_NavigationModePickerFragment__getImageVirtualKeyRes',
        'method': '.method private getImageVirtualKeyRes()I',
        'method_name': 'getImageVirtualKeyRes',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_0', 'sget p0, Lcom/android/provision/R$drawable;->image_virtual_key_global:I', 'return p0', 'iget-object p0, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mActivity:Landroid/app/Activity;', 'invoke-static {p0}, Lcom/android/provision/Utils;->isFoldLarge(Landroid/content/Context;)Z', 'if-eqz p0, :cond_1', 'sget p0, Lcom/android/provision/R$drawable;->image_virtual_key_fold:I'],
        'type': 'policy_skip',
        'search': """.method private getImageVirtualKeyRes()I
    .registers 2

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    sget p0, Lcom/android/provision/R$drawable;->image_virtual_key_global:I

    return p0

    :cond_0
    iget-object p0, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mActivity:Landroid/app/Activity;

    invoke-static {p0}, Lcom/android/provision/Utils;->isFoldLarge(Landroid/content/Context;)Z

    move-result p0

    if-eqz p0, :cond_1

    sget p0, Lcom/android/provision/R$drawable;->image_virtual_key_fold:I

    return p0

    :cond_1
    sget p0, Lcom/android/provision/R$drawable;->image_virtual_key:I

    return p0
.end method""",
        'replacement': """.method private getImageVirtualKeyRes()I
    .registers 2

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    sget p0, Lcom/android/provision/R$drawable;->image_virtual_key_global:I

    return p0

    :cond_0
    iget-object p0, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mActivity:Landroid/app/Activity;

    invoke-static {p0}, Lcom/android/provision/Utils;->isFoldLarge(Landroid/content/Context;)Z

    move-result p0

    if-eqz p0, :cond_1

    sget p0, Lcom/android/provision/R$drawable;->image_virtual_key_fold:I

    return p0

    :cond_1
    sget p0, Lcom/android/provision/R$drawable;->image_virtual_key:I

    return p0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_fragment_NavigationModePickerFragment__getLottieRes',
        'method': '.method private getLottieRes()Ljava/lang/String;',
        'method_name': 'getLottieRes',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_0', 'const-string p0, "navigation_gestures_global.json"', 'return-object p0', 'iget-object p0, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mActivity:Landroid/app/Activity;', 'invoke-static {p0}, Lcom/android/provision/Utils;->isFoldLarge(Landroid/content/Context;)Z', 'if-eqz p0, :cond_1', 'const-string p0, "navigation_gestures_fold.json"'],
        'type': 'policy_skip',
        'search': """.method private getLottieRes()Ljava/lang/String;
    .registers 2

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    const-string p0, "navigation_gestures_global.json"

    return-object p0

    :cond_0
    iget-object p0, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mActivity:Landroid/app/Activity;

    invoke-static {p0}, Lcom/android/provision/Utils;->isFoldLarge(Landroid/content/Context;)Z

    move-result p0

    if-eqz p0, :cond_1

    const-string p0, "navigation_gestures_fold.json"

    return-object p0

    :cond_1
    const-string p0, "navigation_gestures.json"

    return-object p0
.end method""",
        'replacement': """.method private getLottieRes()Ljava/lang/String;
    .registers 2

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    const-string p0, "navigation_gestures_global.json"

    return-object p0

    :cond_0
    iget-object p0, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mActivity:Landroid/app/Activity;

    invoke-static {p0}, Lcom/android/provision/Utils;->isFoldLarge(Landroid/content/Context;)Z

    move-result p0

    if-eqz p0, :cond_1

    const-string p0, "navigation_gestures_fold.json"

    return-object p0

    :cond_1
    const-string p0, "navigation_gestures.json"

    return-object p0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_fragment_NavigationModePickerFragment__getName',
        'method': '.method protected getName()Ljava/lang/String;',
        'method_name': 'getName',
        'method_anchors': ['const-string p0, "NavigationModePickerFragment"', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getName()Ljava/lang/String;
    .registers 1

    const-string p0, "NavigationModePickerFragment"

    return-object p0
.end method""",
        'replacement': """.method protected getName()Ljava/lang/String;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    const-string p0, "NavigationModePickerFragment"

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_fragment_NavigationModePickerFragment__onViewCreated',
        'method': '.method public onViewCreated(Landroid/view/View;Landroid/os/Bundle;)V',
        'method_name': 'onViewCreated',
        'method_anchors': ['invoke-super {p0, p1, p2}, Landroidx/fragment/app/Fragment;->onViewCreated(Landroid/view/View;Landroid/os/Bundle;)V', 'invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;', 'iput-object v0, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mActivity:Landroid/app/Activity;', 'const-string v1, "NavigationModePickerFragment"', 'if-nez v0, :cond_0', 'const-string p0, "mActivity is null"', 'invoke-static {v1, p0}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I', 'return-void'],
        'type': 'method_replace',
        'search': """.method public onViewCreated(Landroid/view/View;Landroid/os/Bundle;)V
    .registers 6

    invoke-super {p0, p1, p2}, Landroidx/fragment/app/Fragment;->onViewCreated(Landroid/view/View;Landroid/os/Bundle;)V

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    iput-object v0, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mActivity:Landroid/app/Activity;

    const-string v1, "NavigationModePickerFragment"

    if-nez v0, :cond_0

    const-string p0, "mActivity is null"

    invoke-static {v1, p0}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    return-void

    :cond_0
    sget v0, Lcom/android/provision/R$id;->navigation_visual_check_group:I

    invoke-virtual {p1, v0}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Lmiuix/visual/check/VisualCheckGroup;

    iput-object v0, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mVisualCheckGroup:Lmiuix/visual/check/VisualCheckGroup;

    sget v0, Lcom/android/provision/R$id;->full_screen_gesture:I

    invoke-virtual {p1, v0}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Lmiuix/visual/check/VisualCheckBox;

    iput-object v0, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mFullScreenGestureCheckBox:Lmiuix/visual/check/VisualCheckBox;

    sget v0, Lcom/android/provision/R$id;->virtual_key:I

    invoke-virtual {p1, v0}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Lmiuix/visual/check/VisualCheckBox;

    iput-object v0, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mVirtualKeyCheckBox:Lmiuix/visual/check/VisualCheckBox;

    sget v0, Lcom/android/provision/R$id;->study_full_screen_gesture:I

    invoke-virtual {p1, v0}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v0

    iput-object v0, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mStudyGesture:Landroid/view/View;

    sget v0, Lcom/android/provision/R$id;->lottie_view_full_screen:I

    invoke-virtual {p1, v0}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Lcom/airbnb/lottie/LottieAnimationView;

    iput-object v0, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mFullScreenLottieView:Lcom/airbnb/lottie/LottieAnimationView;

    sget v0, Lcom/android/provision/R$id;->image_view_virtual_keys:I

    invoke-virtual {p1, v0}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/ImageView;

    iput-object v0, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mVirtualKeyImageView:Landroid/widget/ImageView;

    sget v0, Lcom/android/provision/R$id;->full_screen_gesture_hint:I

    invoke-virtual {p1, v0}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/TextView;

    iput-object v0, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mFullScreenHint:Landroid/widget/TextView;

    sget v0, Lcom/android/provision/R$id;->virtual_key_hint:I

    invoke-virtual {p1, v0}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object p1

    check-cast p1, Landroid/widget/TextView;

    iput-object p1, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mVirtualKeyHint:Landroid/widget/TextView;

    iget-object p1, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mActivity:Landroid/app/Activity;

    invoke-static {p1}, Lcom/android/provision/Utils;->getNextView(Landroid/app/Activity;)Landroid/widget/Button;

    move-result-object p1

    iget-object v0, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mFullScreenLottieView:Lcom/airbnb/lottie/LottieAnimationView;

    if-eqz v0, :cond_1

    iget-object v0, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mActivity:Landroid/app/Activity;

    invoke-static {v0}, Lcom/android/provision/Utils;->isFoldLarge(Landroid/content/Context;)Z

    move-result v0

    if-eqz v0, :cond_1

    iget-object v0, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mFullScreenLottieView:Lcom/airbnb/lottie/LottieAnimationView;

    invoke-direct {p0}, Lcom/android/provision/fragment/NavigationModePickerFragment;->getLottieRes()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v0, v2}, Lcom/airbnb/lottie/LottieAnimationView;->setAnimation(Ljava/lang/String;)V

    :cond_1
    iget-object v0, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mVirtualKeyImageView:Landroid/widget/ImageView;

    if-eqz v0, :cond_2

    invoke-direct {p0}, Lcom/android/provision/fragment/NavigationModePickerFragment;->getImageVirtualKeyRes()I

    move-result v0

    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    invoke-static {v0}, Lcom/android/provision/manager/PreLoadManager;->getDrawablePreLoad(Ljava/lang/Integer;)Landroid/graphics/drawable/Drawable;

    move-result-object v0

    iget-object v2, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mVirtualKeyImageView:Landroid/widget/ImageView;

    invoke-virtual {v2, v0}, Landroid/widget/ImageView;->setImageDrawable(Landroid/graphics/drawable/Drawable;)V

    :cond_2
    invoke-direct {p0}, Lcom/android/provision/fragment/NavigationModePickerFragment;->setApplyNavigationBarMode()V

    invoke-direct {p0}, Lcom/android/provision/fragment/NavigationModePickerFragment;->calModeVisualWidth()V

    if-eqz p2, :cond_3

    iget-boolean v0, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->isFoldOrFlip:Z

    if-eqz v0, :cond_3

    const-string v0, "is_virtual_key"

    const/4 v2, 0x0

    invoke-virtual {p2, v0, v2}, Landroid/os/Bundle;->getBoolean(Ljava/lang/String;Z)Z

    move-result p2

    xor-int/lit8 v0, p2, 0x1

    invoke-direct {p0, v0}, Lcom/android/provision/fragment/NavigationModePickerFragment;->pickEvents(Z)V

    xor-int/lit8 v0, p2, 0x1

    invoke-direct {p0, v0}, Lcom/android/provision/fragment/NavigationModePickerFragment;->updateCheckBoxState(Z)V

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "restore state "

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v0, p2}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p2

    invoke-static {v1, p2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    :cond_3
    iget-object p2, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mVisualCheckGroup:Lmiuix/visual/check/VisualCheckGroup;

    new-instance v0, Lcom/android/provision/fragment/NavigationModePickerFragment$$ExternalSyntheticLambda0;

    invoke-direct {v0, p0}, Lcom/android/provision/fragment/NavigationModePickerFragment$$ExternalSyntheticLambda0;-><init>(Lcom/android/provision/fragment/NavigationModePickerFragment;)V

    invoke-virtual {p2, v0}, Lmiuix/visual/check/VisualCheckGroup;->setOnCheckedChangeListener(Lmiuix/visual/check/VisualCheckGroup$OnCheckedChangeListener;)V

    iget-object p2, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mStudyGesture:Landroid/view/View;

    new-instance v0, Lcom/android/provision/fragment/NavigationModePickerFragment$$ExternalSyntheticLambda1;

    invoke-direct {v0, p0}, Lcom/android/provision/fragment/NavigationModePickerFragment$$ExternalSyntheticLambda1;-><init>(Lcom/android/provision/fragment/NavigationModePickerFragment;)V

    invoke-virtual {p2, v0}, Landroid/view/View;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    new-instance p2, Lcom/android/provision/fragment/NavigationModePickerFragment$$ExternalSyntheticLambda2;

    invoke-direct {p2, p0}, Lcom/android/provision/fragment/NavigationModePickerFragment$$ExternalSyntheticLambda2;-><init>(Lcom/android/provision/fragment/NavigationModePickerFragment;)V

    invoke-virtual {p1, p2}, Landroid/widget/Button;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez p1, :cond_4

    invoke-static {}, Lmiui/enterprise/RestrictionsHelperStub;->getInstance()Lmiui/enterprise/IRestrictionsHelper;

    move-result-object p1

    invoke-interface {p1}, Lmiui/enterprise/IRestrictionsHelper;->isFullScreenGesturesRestriction()Z

    move-result p1

    if-eqz p1, :cond_4

    iget-object p0, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mVirtualKeyCheckBox:Lmiuix/visual/check/VisualCheckBox;

    const/4 p1, 0x1

    invoke-virtual {p0, p1}, Lmiuix/visual/check/VisualCheckBox;->setChecked(Z)V

    :cond_4
    return-void
.end method""",
        'replacement': """.method public onViewCreated(Landroid/view/View;Landroid/os/Bundle;)V
    .registers 6

    invoke-super {p0, p1, p2}, Landroidx/fragment/app/Fragment;->onViewCreated(Landroid/view/View;Landroid/os/Bundle;)V

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    iput-object v0, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mActivity:Landroid/app/Activity;

    const-string v1, "NavigationModePickerFragment"

    if-nez v0, :cond_0

    const-string p0, "mActivity is null"

    invoke-static {v1, p0}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    return-void

    :cond_0
    sget v0, Lcom/android/provision/R$id;->navigation_visual_check_group:I

    invoke-virtual {p1, v0}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Lmiuix/visual/check/VisualCheckGroup;

    iput-object v0, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mVisualCheckGroup:Lmiuix/visual/check/VisualCheckGroup;

    sget v0, Lcom/android/provision/R$id;->full_screen_gesture:I

    invoke-virtual {p1, v0}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Lmiuix/visual/check/VisualCheckBox;

    iput-object v0, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mFullScreenGestureCheckBox:Lmiuix/visual/check/VisualCheckBox;

    sget v0, Lcom/android/provision/R$id;->virtual_key:I

    invoke-virtual {p1, v0}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Lmiuix/visual/check/VisualCheckBox;

    iput-object v0, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mVirtualKeyCheckBox:Lmiuix/visual/check/VisualCheckBox;

    sget v0, Lcom/android/provision/R$id;->study_full_screen_gesture:I

    invoke-virtual {p1, v0}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v0

    iput-object v0, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mStudyGesture:Landroid/view/View;

    sget v0, Lcom/android/provision/R$id;->lottie_view_full_screen:I

    invoke-virtual {p1, v0}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Lcom/airbnb/lottie/LottieAnimationView;

    iput-object v0, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mFullScreenLottieView:Lcom/airbnb/lottie/LottieAnimationView;

    sget v0, Lcom/android/provision/R$id;->image_view_virtual_keys:I

    invoke-virtual {p1, v0}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/ImageView;

    iput-object v0, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mVirtualKeyImageView:Landroid/widget/ImageView;

    sget v0, Lcom/android/provision/R$id;->full_screen_gesture_hint:I

    invoke-virtual {p1, v0}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/TextView;

    iput-object v0, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mFullScreenHint:Landroid/widget/TextView;

    sget v0, Lcom/android/provision/R$id;->virtual_key_hint:I

    invoke-virtual {p1, v0}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object p1

    check-cast p1, Landroid/widget/TextView;

    iput-object p1, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mVirtualKeyHint:Landroid/widget/TextView;

    iget-object p1, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mActivity:Landroid/app/Activity;

    invoke-static {p1}, Lcom/android/provision/Utils;->getNextView(Landroid/app/Activity;)Landroid/widget/Button;

    move-result-object p1

    iget-object v0, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mFullScreenLottieView:Lcom/airbnb/lottie/LottieAnimationView;

    if-eqz v0, :cond_1

    iget-object v0, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mActivity:Landroid/app/Activity;

    invoke-static {v0}, Lcom/android/provision/Utils;->isFoldLarge(Landroid/content/Context;)Z

    move-result v0

    if-eqz v0, :cond_1

    iget-object v0, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mFullScreenLottieView:Lcom/airbnb/lottie/LottieAnimationView;

    invoke-direct {p0}, Lcom/android/provision/fragment/NavigationModePickerFragment;->getLottieRes()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v0, v2}, Lcom/airbnb/lottie/LottieAnimationView;->setAnimation(Ljava/lang/String;)V

    :cond_1
    iget-object v0, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mVirtualKeyImageView:Landroid/widget/ImageView;

    if-eqz v0, :cond_2

    invoke-direct {p0}, Lcom/android/provision/fragment/NavigationModePickerFragment;->getImageVirtualKeyRes()I

    move-result v0

    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    invoke-static {v0}, Lcom/android/provision/manager/PreLoadManager;->getDrawablePreLoad(Ljava/lang/Integer;)Landroid/graphics/drawable/Drawable;

    move-result-object v0

    iget-object v2, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mVirtualKeyImageView:Landroid/widget/ImageView;

    invoke-virtual {v2, v0}, Landroid/widget/ImageView;->setImageDrawable(Landroid/graphics/drawable/Drawable;)V

    :cond_2
    invoke-direct {p0}, Lcom/android/provision/fragment/NavigationModePickerFragment;->setApplyNavigationBarMode()V

    invoke-direct {p0}, Lcom/android/provision/fragment/NavigationModePickerFragment;->calModeVisualWidth()V

    if-eqz p2, :cond_3

    iget-boolean v0, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->isFoldOrFlip:Z

    if-eqz v0, :cond_3

    const-string v0, "is_virtual_key"

    const/4 v2, 0x0

    invoke-virtual {p2, v0, v2}, Landroid/os/Bundle;->getBoolean(Ljava/lang/String;Z)Z

    move-result p2

    xor-int/lit8 v0, p2, 0x1

    invoke-direct {p0, v0}, Lcom/android/provision/fragment/NavigationModePickerFragment;->pickEvents(Z)V

    xor-int/lit8 v0, p2, 0x1

    invoke-direct {p0, v0}, Lcom/android/provision/fragment/NavigationModePickerFragment;->updateCheckBoxState(Z)V

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "restore state "

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v0, p2}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p2

    invoke-static {v1, p2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    :cond_3
    iget-object p2, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mVisualCheckGroup:Lmiuix/visual/check/VisualCheckGroup;

    new-instance v0, Lcom/android/provision/fragment/NavigationModePickerFragment$$ExternalSyntheticLambda0;

    invoke-direct {v0, p0}, Lcom/android/provision/fragment/NavigationModePickerFragment$$ExternalSyntheticLambda0;-><init>(Lcom/android/provision/fragment/NavigationModePickerFragment;)V

    invoke-virtual {p2, v0}, Lmiuix/visual/check/VisualCheckGroup;->setOnCheckedChangeListener(Lmiuix/visual/check/VisualCheckGroup$OnCheckedChangeListener;)V

    iget-object p2, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mStudyGesture:Landroid/view/View;

    new-instance v0, Lcom/android/provision/fragment/NavigationModePickerFragment$$ExternalSyntheticLambda1;

    invoke-direct {v0, p0}, Lcom/android/provision/fragment/NavigationModePickerFragment$$ExternalSyntheticLambda1;-><init>(Lcom/android/provision/fragment/NavigationModePickerFragment;)V

    invoke-virtual {p2, v0}, Landroid/view/View;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    new-instance p2, Lcom/android/provision/fragment/NavigationModePickerFragment$$ExternalSyntheticLambda2;

    invoke-direct {p2, p0}, Lcom/android/provision/fragment/NavigationModePickerFragment$$ExternalSyntheticLambda2;-><init>(Lcom/android/provision/fragment/NavigationModePickerFragment;)V

    invoke-virtual {p1, p2}, Landroid/widget/Button;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    sget-boolean p1, Lmiui/os/Build;->IS_ALPHA_BUILD:Z

    if-nez p1, :cond_4

    invoke-static {}, Lmiui/enterprise/RestrictionsHelperStub;->getInstance()Lmiui/enterprise/IRestrictionsHelper;

    move-result-object p1

    invoke-interface {p1}, Lmiui/enterprise/IRestrictionsHelper;->isFullScreenGesturesRestriction()Z

    move-result p1

    if-eqz p1, :cond_4

    iget-object p0, p0, Lcom/android/provision/fragment/NavigationModePickerFragment;->mVirtualKeyCheckBox:Lmiuix/visual/check/VisualCheckBox;

    const/4 p1, 0x1

    invoke-virtual {p0, p1}, Lmiuix/visual/check/VisualCheckBox;->setChecked(Z)V

    :cond_4
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
