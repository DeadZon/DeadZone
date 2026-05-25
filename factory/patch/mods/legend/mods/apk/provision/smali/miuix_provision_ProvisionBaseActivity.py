TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/provision/ProvisionBaseActivity.smali'
CLASS_FALLBACK_NAMES = ['ProvisionBaseActivity.smali']
CLASS_ANCHORS = ['.super Lmiuix/appcompat/app/AppCompatActivity;', '.implements Lmiuix/provision/ProvisionAnimHelper$AnimListener;', '.field private static final SETTINGS_NEW_FEATURE:Ljava/lang/String; = "new_feature"']

PATCHES = [
    {
        'id': 'miuix_provision_ProvisionBaseActivity__adaptFoldContainerMargin',
        'method': '.method protected adaptFoldContainerMargin(Landroid/util/DisplayMetrics;F)V',
        'method_name': 'adaptFoldContainerMargin',
        'method_anchors': ['iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionContainer:Landroid/view/View;', 'if-nez v0, :cond_0', 'invoke-static {}, Lmiuix/provision/OobeUtil;->isFoldDevice()Z', 'if-nez v0, :cond_1', 'invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;', 'sget v1, Lmiuix/provision/R$dimen;->provision_container_content_width:I', 'invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I', 'iget v1, p1, Landroid/util/DisplayMetrics;->widthPixels:I'],
        'type': 'method_replace',
        'search': """.method protected adaptFoldContainerMargin(Landroid/util/DisplayMetrics;F)V
    .registers 6

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionContainer:Landroid/view/View;

    if-nez v0, :cond_0

    goto :goto_0

    :cond_0
    invoke-static {}, Lmiuix/provision/OobeUtil;->isFoldDevice()Z

    move-result v0

    if-nez v0, :cond_1

    goto :goto_0

    :cond_1
    invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    sget v1, Lmiuix/provision/R$dimen;->provision_container_content_width:I

    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I

    move-result v0

    iget v1, p1, Landroid/util/DisplayMetrics;->widthPixels:I

    sub-int/2addr v1, v0

    div-int/lit8 v1, v1, 0x2

    invoke-direct {p0, v1}, Lmiuix/provision/ProvisionBaseActivity;->setContainerMargin(I)V

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "adaptContainerMargin windowWidth: "

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget p1, p1, Landroid/util/DisplayMetrics;->widthPixels:I

    int-to-float p1, p1

    div-float/2addr p1, p2

    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(F)Ljava/lang/StringBuilder;

    const-string p1, " marginHorizontal: "

    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    int-to-float p1, v1

    div-float/2addr p1, p2

    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(F)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p1

    const-string p2, "OobeUtil2"

    invoke-static {p2, p1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->isImageStyleLayout()Z

    move-result p1

    if-eqz p1, :cond_2

    iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionContainer:Landroid/view/View;

    const/4 p1, 0x0

    invoke-virtual {p0, p1, p1, p1, p1}, Landroid/view/View;->setPadding(IIII)V

    :cond_2
    :goto_0
    return-void
.end method""",
        'replacement': """.method protected adaptFoldContainerMargin(Landroid/util/DisplayMetrics;F)V
    .registers 6

    goto :goto_23

    nop

    :goto_0
    sub-int/2addr v1, v0

    goto :goto_9

    nop

    :goto_1
    iget v1, p1, Landroid/util/DisplayMetrics;->widthPixels:I

    goto :goto_0

    nop

    :goto_2
    iget p1, p1, Landroid/util/DisplayMetrics;->widthPixels:I

    goto :goto_d

    nop

    :goto_3
    iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionContainer:Landroid/view/View;

    goto :goto_14

    nop

    :goto_4
    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_16

    nop

    :goto_5
    div-float/2addr p1, p2

    goto :goto_25

    nop

    :goto_6
    invoke-direct {p0, v1}, Lmiuix/provision/ProvisionBaseActivity;->setContainerMargin(I)V

    goto :goto_7

    nop

    :goto_7
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_1f

    nop

    :goto_8
    if-eqz v0, :cond_0

    goto :goto_19

    :cond_0
    goto :goto_18

    nop

    :goto_9
    div-int/lit8 v1, v1, 0x2

    goto :goto_6

    nop

    :goto_a
    goto :goto_22

    :goto_b
    goto :goto_13

    nop

    :goto_c
    const-string p1, " marginHorizontal: "

    goto :goto_4

    nop

    :goto_d
    int-to-float p1, p1

    goto :goto_5

    nop

    :goto_e
    if-eqz v0, :cond_1

    goto :goto_b

    :cond_1
    goto :goto_a

    nop

    :goto_f
    invoke-static {}, Lmiuix/provision/OobeUtil;->isFoldDevice()Z

    move-result v0

    goto :goto_e

    nop

    :goto_10
    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_2

    nop

    :goto_11
    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->isImageStyleLayout()Z

    move-result p1

    goto :goto_15

    nop

    :goto_12
    const-string p2, "OobeUtil2"

    goto :goto_1e

    nop

    :goto_13
    invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    goto :goto_1b

    nop

    :goto_14
    const/4 p1, 0x0

    goto :goto_21

    nop

    :goto_15
    if-nez p1, :cond_2

    goto :goto_22

    :cond_2
    goto :goto_3

    nop

    :goto_16
    int-to-float p1, v1

    goto :goto_17

    nop

    :goto_17
    div-float/2addr p1, p2

    goto :goto_1a

    nop

    :goto_18
    goto :goto_22

    :goto_19
    goto :goto_f

    nop

    :goto_1a
    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(F)Ljava/lang/StringBuilder;

    goto :goto_1c

    nop

    :goto_1b
    sget v1, Lmiuix/provision/R$dimen;->provision_container_content_width:I

    goto :goto_24

    nop

    :goto_1c
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p1

    goto :goto_12

    nop

    :goto_1d
    const-string v2, "adaptContainerMargin windowWidth: "

    goto :goto_10

    nop

    :goto_1e
    invoke-static {p2, p1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_11

    nop

    :goto_1f
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_1d

    nop

    :goto_20
    return-void

    :goto_21
    invoke-virtual {p0, p1, p1, p1, p1}, Landroid/view/View;->setPadding(IIII)V

    :goto_22
    goto :goto_20

    nop

    :goto_23
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionContainer:Landroid/view/View;

    goto :goto_8

    nop

    :goto_24
    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I

    move-result v0

    goto :goto_1

    nop

    :goto_25
    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(F)Ljava/lang/StringBuilder;

    goto :goto_c

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_provision_ProvisionBaseActivity__adaptPadContainerExtraPadding',
        'method': '.method protected adaptPadContainerExtraPadding(I)V',
        'method_name': 'adaptPadContainerExtraPadding',
        'method_anchors': ['iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionContainer:Landroid/view/View;', 'if-nez v0, :cond_0', 'sget-boolean v0, Lmiui/os/Build;->IS_TABLET:Z', 'if-eqz v0, :cond_2', 'invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->isNeedAdaptImageStyle()Z', 'if-nez v0, :cond_2', 'invoke-static {p0}, Lmiuix/provision/OobeUtil;->isLandOrientation(Landroid/content/Context;)Z', 'if-eqz v0, :cond_1'],
        'type': 'method_replace',
        'search': """.method protected adaptPadContainerExtraPadding(I)V
    .registers 6

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionContainer:Landroid/view/View;

    if-nez v0, :cond_0

    goto :goto_1

    :cond_0
    sget-boolean v0, Lmiui/os/Build;->IS_TABLET:Z

    if-eqz v0, :cond_2

    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->isNeedAdaptImageStyle()Z

    move-result v0

    if-nez v0, :cond_2

    invoke-static {p0}, Lmiuix/provision/OobeUtil;->isLandOrientation(Landroid/content/Context;)Z

    move-result v0

    if-eqz v0, :cond_1

    invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    sget v1, Lmiuix/provision/R$dimen;->provision_container_padding_horizontal_pad_land:I

    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I

    move-result v0

    goto :goto_0

    :cond_1
    invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    sget v1, Lmiuix/provision/R$dimen;->provision_container_padding_horizontal_pad_port:I

    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I

    move-result v0

    :goto_0
    iget-object v1, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionContainer:Landroid/view/View;

    invoke-virtual {v1}, Landroid/view/View;->getPaddingTop()I

    move-result v2

    iget-object v3, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionContainer:Landroid/view/View;

    invoke-virtual {v3}, Landroid/view/View;->getPaddingBottom()I

    move-result v3

    invoke-virtual {v1, v0, v2, v0, v3}, Landroid/view/View;->setPadding(IIII)V

    invoke-direct {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setContainerMargin(I)V

    new-instance p0, Ljava/lang/StringBuilder;

    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v0, "adaptContainerMargin: "

    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    const-string p1, "OobeUtil2"

    invoke-static {p1, p0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    :cond_2
    :goto_1
    return-void
.end method""",
        'replacement': """.method protected adaptPadContainerExtraPadding(I)V
    .registers 6

    goto :goto_11

    nop

    :goto_0
    const-string v0, "adaptContainerMargin: "

    goto :goto_18

    nop

    :goto_1
    goto :goto_14

    :goto_2
    goto :goto_1f

    nop

    :goto_3
    if-eqz v0, :cond_0

    goto :goto_1b

    :cond_0
    goto :goto_10

    nop

    :goto_4
    if-nez v0, :cond_1

    goto :goto_1b

    :cond_1
    goto :goto_17

    nop

    :goto_5
    invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    goto :goto_20

    nop

    :goto_6
    if-eqz v0, :cond_2

    goto :goto_b

    :cond_2
    goto :goto_a

    nop

    :goto_7
    invoke-virtual {v3}, Landroid/view/View;->getPaddingBottom()I

    move-result v3

    goto :goto_12

    nop

    :goto_8
    const-string p1, "OobeUtil2"

    goto :goto_1a

    nop

    :goto_9
    iget-object v1, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionContainer:Landroid/view/View;

    goto :goto_15

    nop

    :goto_a
    goto :goto_1b

    :goto_b
    goto :goto_c

    nop

    :goto_c
    sget-boolean v0, Lmiui/os/Build;->IS_TABLET:Z

    goto :goto_4

    nop

    :goto_d
    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_19

    nop

    :goto_e
    if-nez v0, :cond_3

    goto :goto_2

    :cond_3
    goto :goto_5

    nop

    :goto_f
    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_0

    nop

    :goto_10
    invoke-static {p0}, Lmiuix/provision/OobeUtil;->isLandOrientation(Landroid/content/Context;)Z

    move-result v0

    goto :goto_e

    nop

    :goto_11
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionContainer:Landroid/view/View;

    goto :goto_6

    nop

    :goto_12
    invoke-virtual {v1, v0, v2, v0, v3}, Landroid/view/View;->setPadding(IIII)V

    goto :goto_1d

    nop

    :goto_13
    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I

    move-result v0

    :goto_14
    goto :goto_9

    nop

    :goto_15
    invoke-virtual {v1}, Landroid/view/View;->getPaddingTop()I

    move-result v2

    goto :goto_16

    nop

    :goto_16
    iget-object v3, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionContainer:Landroid/view/View;

    goto :goto_7

    nop

    :goto_17
    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->isNeedAdaptImageStyle()Z

    move-result v0

    goto :goto_3

    nop

    :goto_18
    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_d

    nop

    :goto_19
    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    goto :goto_8

    nop

    :goto_1a
    invoke-static {p1, p0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    :goto_1b
    goto :goto_22

    nop

    :goto_1c
    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I

    move-result v0

    goto :goto_1

    nop

    :goto_1d
    invoke-direct {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setContainerMargin(I)V

    goto :goto_21

    nop

    :goto_1e
    sget v1, Lmiuix/provision/R$dimen;->provision_container_padding_horizontal_pad_port:I

    goto :goto_13

    nop

    :goto_1f
    invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    goto :goto_1e

    nop

    :goto_20
    sget v1, Lmiuix/provision/R$dimen;->provision_container_padding_horizontal_pad_land:I

    goto :goto_1c

    nop

    :goto_21
    new-instance p0, Ljava/lang/StringBuilder;

    goto :goto_f

    nop

    :goto_22
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_provision_ProvisionBaseActivity__adaptPadImageStyleLayout',
        'method': '.method protected adaptPadImageStyleLayout(Landroid/util/DisplayMetrics;)V',
        'method_name': 'adaptPadImageStyleLayout',
        'method_anchors': ['iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionContainer:Landroid/view/View;', 'if-nez v0, :cond_0', 'invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->isNeedAdaptImageStyle()Z', 'if-eqz v0, :cond_1', 'iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionContainer:Landroid/view/View;', 'invoke-virtual {v0, v1, v1, v1, v1}, Landroid/view/View;->setPadding(IIII)V', 'invoke-static {p0}, Lmiuix/core/util/EnvStateManager;->getScreenShortEdge(Landroid/content/Context;)I', 'iget p1, p1, Landroid/util/DisplayMetrics;->widthPixels:I'],
        'type': 'method_replace',
        'search': """.method protected adaptPadImageStyleLayout(Landroid/util/DisplayMetrics;)V
    .registers 6

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionContainer:Landroid/view/View;

    if-nez v0, :cond_0

    goto :goto_0

    :cond_0
    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->isNeedAdaptImageStyle()Z

    move-result v0

    if-eqz v0, :cond_1

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionContainer:Landroid/view/View;

    const/4 v1, 0x0

    invoke-virtual {v0, v1, v1, v1, v1}, Landroid/view/View;->setPadding(IIII)V

    invoke-static {p0}, Lmiuix/core/util/EnvStateManager;->getScreenShortEdge(Landroid/content/Context;)I

    move-result v0

    int-to-double v0, v0

    const-wide v2, 0x3fe3333333333333L

    mul-double/2addr v0, v2

    double-to-int v0, v0

    iget p1, p1, Landroid/util/DisplayMetrics;->widthPixels:I

    sub-int/2addr p1, v0

    div-int/lit8 p1, p1, 0x2

    invoke-direct {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setContainerMargin(I)V

    :cond_1
    :goto_0
    return-void
.end method""",
        'replacement': """.method protected adaptPadImageStyleLayout(Landroid/util/DisplayMetrics;)V
    .registers 6

    goto :goto_1

    nop

    :goto_0
    invoke-virtual {v0, v1, v1, v1, v1}, Landroid/view/View;->setPadding(IIII)V

    goto :goto_f

    nop

    :goto_1
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionContainer:Landroid/view/View;

    goto :goto_a

    nop

    :goto_2
    if-nez v0, :cond_0

    goto :goto_e

    :cond_0
    goto :goto_10

    nop

    :goto_3
    goto :goto_e

    :goto_4
    goto :goto_11

    nop

    :goto_5
    sub-int/2addr p1, v0

    goto :goto_6

    nop

    :goto_6
    div-int/lit8 p1, p1, 0x2

    goto :goto_d

    nop

    :goto_7
    iget p1, p1, Landroid/util/DisplayMetrics;->widthPixels:I

    goto :goto_5

    nop

    :goto_8
    const/4 v1, 0x0

    goto :goto_0

    nop

    :goto_9
    int-to-double v0, v0

    goto :goto_c

    nop

    :goto_a
    if-eqz v0, :cond_1

    goto :goto_4

    :cond_1
    goto :goto_3

    nop

    :goto_b
    double-to-int v0, v0

    goto :goto_7

    nop

    :goto_c
    const-wide v2, 0x3fe3333333333333L

    goto :goto_12

    nop

    :goto_d
    invoke-direct {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setContainerMargin(I)V

    :goto_e
    goto :goto_13

    nop

    :goto_f
    invoke-static {p0}, Lmiuix/core/util/EnvStateManager;->getScreenShortEdge(Landroid/content/Context;)I

    move-result v0

    goto :goto_9

    nop

    :goto_10
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionContainer:Landroid/view/View;

    goto :goto_8

    nop

    :goto_11
    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->isNeedAdaptImageStyle()Z

    move-result v0

    goto :goto_2

    nop

    :goto_12
    mul-double/2addr v0, v2

    goto :goto_b

    nop

    :goto_13
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_provision_ProvisionBaseActivity__delayEnableButton',
        'method': '.method protected delayEnableButton()V',
        'method_name': 'delayEnableButton',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->needDelayButton()Z', 'if-nez v0, :cond_0', 'return-void', 'invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->needSuperButtonInitial()Z', 'if-eqz v0, :cond_1', 'invoke-virtual {p0, v3}, Lmiuix/provision/ProvisionBaseActivity;->updateButtonState(Z)V', 'iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mH:Landroid/os/Handler;', 'new-instance v3, Lmiuix/provision/ProvisionBaseActivity$$ExternalSyntheticLambda1;'],
        'type': 'method_replace',
        'search': """.method protected delayEnableButton()V
    .registers 5

    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->needDelayButton()Z

    move-result v0

    if-nez v0, :cond_0

    return-void

    :cond_0
    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->needSuperButtonInitial()Z

    move-result v0

    const-wide/16 v1, 0x3e8

    const/4 v3, 0x0

    if-eqz v0, :cond_1

    invoke-virtual {p0, v3}, Lmiuix/provision/ProvisionBaseActivity;->updateButtonState(Z)V

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mH:Landroid/os/Handler;

    new-instance v3, Lmiuix/provision/ProvisionBaseActivity$$ExternalSyntheticLambda1;

    invoke-direct {v3, p0}, Lmiuix/provision/ProvisionBaseActivity$$ExternalSyntheticLambda1;-><init>(Lmiuix/provision/ProvisionBaseActivity;)V

    invoke-virtual {v0, v3, v1, v2}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z

    return-void

    :cond_1
    invoke-virtual {p0, v3}, Lmiuix/provision/ProvisionBaseActivity;->updateBackButtonState(Z)V

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mH:Landroid/os/Handler;

    new-instance v3, Lmiuix/provision/ProvisionBaseActivity$$ExternalSyntheticLambda2;

    invoke-direct {v3, p0}, Lmiuix/provision/ProvisionBaseActivity$$ExternalSyntheticLambda2;-><init>(Lmiuix/provision/ProvisionBaseActivity;)V

    invoke-virtual {v0, v3, v1, v2}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z

    return-void
.end method""",
        'replacement': """.method protected delayEnableButton()V
    .registers 5

    goto :goto_5

    nop

    :goto_0
    const-wide/16 v1, 0x3e8

    goto :goto_b

    nop

    :goto_1
    new-instance v3, Lmiuix/provision/ProvisionBaseActivity$$ExternalSyntheticLambda2;

    goto :goto_a

    nop

    :goto_2
    return-void

    :goto_3
    goto :goto_11

    nop

    :goto_4
    invoke-virtual {v0, v3, v1, v2}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z

    goto :goto_2

    nop

    :goto_5
    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->needDelayButton()Z

    move-result v0

    goto :goto_c

    nop

    :goto_6
    new-instance v3, Lmiuix/provision/ProvisionBaseActivity$$ExternalSyntheticLambda1;

    goto :goto_13

    nop

    :goto_7
    return-void

    :goto_8
    goto :goto_e

    nop

    :goto_9
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mH:Landroid/os/Handler;

    goto :goto_1

    nop

    :goto_a
    invoke-direct {v3, p0}, Lmiuix/provision/ProvisionBaseActivity$$ExternalSyntheticLambda2;-><init>(Lmiuix/provision/ProvisionBaseActivity;)V

    goto :goto_10

    nop

    :goto_b
    const/4 v3, 0x0

    goto :goto_d

    nop

    :goto_c
    if-eqz v0, :cond_0

    goto :goto_8

    :cond_0
    goto :goto_7

    nop

    :goto_d
    if-nez v0, :cond_1

    goto :goto_3

    :cond_1
    goto :goto_12

    nop

    :goto_e
    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->needSuperButtonInitial()Z

    move-result v0

    goto :goto_0

    nop

    :goto_f
    return-void

    :goto_10
    invoke-virtual {v0, v3, v1, v2}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z

    goto :goto_f

    nop

    :goto_11
    invoke-virtual {p0, v3}, Lmiuix/provision/ProvisionBaseActivity;->updateBackButtonState(Z)V

    goto :goto_9

    nop

    :goto_12
    invoke-virtual {p0, v3}, Lmiuix/provision/ProvisionBaseActivity;->updateButtonState(Z)V

    goto :goto_14

    nop

    :goto_13
    invoke-direct {v3, p0}, Lmiuix/provision/ProvisionBaseActivity$$ExternalSyntheticLambda1;-><init>(Lmiuix/provision/ProvisionBaseActivity;)V

    goto :goto_4

    nop

    :goto_14
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mH:Landroid/os/Handler;

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_provision_ProvisionBaseActivity__getConfig',
        'method': '.method protected getConfig()Lmiuix/appcompat/app/GroupButtonsConfig;',
        'method_name': 'getConfig',
        'method_anchors': ['invoke-static {}, Lmiuix/appcompat/app/GroupButtonsConfig;->createBuilder()Lmiuix/appcompat/app/GroupButtonsConfig$Builder;', 'sget v1, Lmiuix/provision/R$string;->provision_next:I', 'invoke-virtual {p0, v1}, Landroid/app/Activity;->getText(I)Ljava/lang/CharSequence;', 'invoke-virtual {v0, v2, v1}, Lmiuix/appcompat/app/GroupButtonsConfig$Builder;->setButton(ILjava/lang/CharSequence;)Lmiuix/appcompat/app/GroupButtonsConfig$Builder;', 'sget v0, Lmiuix/provision/R$string;->provision_skip_underline:I', 'invoke-virtual {p0, v0}, Landroid/app/Activity;->getText(I)Ljava/lang/CharSequence;', 'invoke-virtual/range {v3 .. v9}, Lmiuix/appcompat/app/GroupButtonsConfig$Builder;->setButton(ILjava/lang/CharSequence;Landroid/view/View$OnClickListener;Landroid/view/View$OnLongClickListener;ZZ)Lmiuix/appcompat/app/GroupButtonsConfig$Builder;', 'invoke-virtual {p0}, Lmiuix/appcompat/app/GroupButtonsConfig$Builder;->build()Lmiuix/appcompat/app/GroupButtonsConfig;'],
        'type': 'method_replace',
        'search': """.method protected getConfig()Lmiuix/appcompat/app/GroupButtonsConfig;
    .registers 11

    invoke-static {}, Lmiuix/appcompat/app/GroupButtonsConfig;->createBuilder()Lmiuix/appcompat/app/GroupButtonsConfig$Builder;

    move-result-object v0

    sget v1, Lmiuix/provision/R$string;->provision_next:I

    invoke-virtual {p0, v1}, Landroid/app/Activity;->getText(I)Ljava/lang/CharSequence;

    move-result-object v1

    const/4 v2, 0x0

    invoke-virtual {v0, v2, v1}, Lmiuix/appcompat/app/GroupButtonsConfig$Builder;->setButton(ILjava/lang/CharSequence;)Lmiuix/appcompat/app/GroupButtonsConfig$Builder;

    move-result-object v3

    sget v0, Lmiuix/provision/R$string;->provision_skip_underline:I

    invoke-virtual {p0, v0}, Landroid/app/Activity;->getText(I)Ljava/lang/CharSequence;

    move-result-object v5

    const/4 v8, 0x1

    const/4 v9, 0x0

    const/4 v4, 0x1

    const/4 v6, 0x0

    const/4 v7, 0x0

    invoke-virtual/range {v3 .. v9}, Lmiuix/appcompat/app/GroupButtonsConfig$Builder;->setButton(ILjava/lang/CharSequence;Landroid/view/View$OnClickListener;Landroid/view/View$OnLongClickListener;ZZ)Lmiuix/appcompat/app/GroupButtonsConfig$Builder;

    move-result-object p0

    invoke-virtual {p0}, Lmiuix/appcompat/app/GroupButtonsConfig$Builder;->build()Lmiuix/appcompat/app/GroupButtonsConfig;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected getConfig()Lmiuix/appcompat/app/GroupButtonsConfig;
    .registers 11

    goto :goto_3

    nop

    :goto_0
    invoke-virtual/range {v3 .. v9}, Lmiuix/appcompat/app/GroupButtonsConfig$Builder;->setButton(ILjava/lang/CharSequence;Landroid/view/View$OnClickListener;Landroid/view/View$OnLongClickListener;ZZ)Lmiuix/appcompat/app/GroupButtonsConfig$Builder;

    move-result-object p0

    goto :goto_6

    nop

    :goto_1
    return-object p0

    :goto_2
    const/4 v4, 0x1

    goto :goto_d

    nop

    :goto_3
    invoke-static {}, Lmiuix/appcompat/app/GroupButtonsConfig;->createBuilder()Lmiuix/appcompat/app/GroupButtonsConfig$Builder;

    move-result-object v0

    goto :goto_b

    nop

    :goto_4
    invoke-virtual {v0, v2, v1}, Lmiuix/appcompat/app/GroupButtonsConfig$Builder;->setButton(ILjava/lang/CharSequence;)Lmiuix/appcompat/app/GroupButtonsConfig$Builder;

    move-result-object v3

    goto :goto_5

    nop

    :goto_5
    sget v0, Lmiuix/provision/R$string;->provision_skip_underline:I

    goto :goto_a

    nop

    :goto_6
    invoke-virtual {p0}, Lmiuix/appcompat/app/GroupButtonsConfig$Builder;->build()Lmiuix/appcompat/app/GroupButtonsConfig;

    move-result-object p0

    goto :goto_1

    nop

    :goto_7
    const/4 v8, 0x1

    goto :goto_8

    nop

    :goto_8
    const/4 v9, 0x0

    goto :goto_2

    nop

    :goto_9
    const/4 v7, 0x0

    goto :goto_0

    nop

    :goto_a
    invoke-virtual {p0, v0}, Landroid/app/Activity;->getText(I)Ljava/lang/CharSequence;

    move-result-object v5

    goto :goto_7

    nop

    :goto_b
    sget v1, Lmiuix/provision/R$string;->provision_next:I

    goto :goto_c

    nop

    :goto_c
    invoke-virtual {p0, v1}, Landroid/app/Activity;->getText(I)Ljava/lang/CharSequence;

    move-result-object v1

    goto :goto_e

    nop

    :goto_d
    const/4 v6, 0x0

    goto :goto_9

    nop

    :goto_e
    const/4 v2, 0x0

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_provision_ProvisionBaseActivity__getTitleLayoutHeight',
        'method': '.method protected getTitleLayoutHeight()I',
        'method_name': 'getTitleLayoutHeight',
        'method_anchors': ['iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mLottieAnimationView:Lcom/airbnb/lottie/LottieAnimationView;', 'if-nez p0, :cond_0', 'return p0', 'invoke-virtual {p0}, Landroid/widget/ImageView;->getHeight()I', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected getTitleLayoutHeight()I
    .registers 1

    iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mLottieAnimationView:Lcom/airbnb/lottie/LottieAnimationView;

    if-nez p0, :cond_0

    const/4 p0, 0x0

    return p0

    :cond_0
    invoke-virtual {p0}, Landroid/widget/ImageView;->getHeight()I

    move-result p0

    return p0
.end method""",
        'replacement': """.method protected getTitleLayoutHeight()I
    .registers 1

    goto :goto_3

    nop

    :goto_0
    if-eqz p0, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_6

    nop

    :goto_1
    return p0

    :goto_2
    goto :goto_5

    nop

    :goto_3
    iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mLottieAnimationView:Lcom/airbnb/lottie/LottieAnimationView;

    goto :goto_0

    nop

    :goto_4
    return p0

    :goto_5
    invoke-virtual {p0}, Landroid/widget/ImageView;->getHeight()I

    move-result p0

    goto :goto_4

    nop

    :goto_6
    const/4 p0, 0x0

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_provision_ProvisionBaseActivity__getXiaoAiSupportVersion',
        'method': '.method protected getXiaoAiSupportVersion()I',
        'method_name': 'getXiaoAiSupportVersion',
        'method_anchors': ['return p0'],
        'type': 'method_replace',
        'search': """.method protected getXiaoAiSupportVersion()I
    .registers 1

    const/4 p0, 0x1

    return p0
.end method""",
        'replacement': """.method protected getXiaoAiSupportVersion()I
    .registers 1

    goto :goto_0

    nop

    :goto_0
    const/4 p0, 0x1

    goto :goto_1

    nop

    :goto_1
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_provision_ProvisionBaseActivity__immersionEnable',
        'method': '.method protected immersionEnable()Z',
        'method_name': 'immersionEnable',
        'method_anchors': ['return p0'],
        'type': 'method_replace',
        'search': """.method protected immersionEnable()Z
    .registers 1

    const/4 p0, 0x1

    return p0
.end method""",
        'replacement': """.method protected immersionEnable()Z
    .registers 1

    goto :goto_0

    nop

    :goto_0
    const/4 p0, 0x1

    goto :goto_1

    nop

    :goto_1
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_provision_ProvisionBaseActivity__immersionExtend',
        'method': '.method protected immersionExtend()V',
        'method_name': 'immersionExtend',
        'method_anchors': ['return-void'],
        'type': 'method_replace',
        'search': """.method protected immersionExtend()V
    .registers 1

    return-void
.end method""",
        'replacement': """.method protected immersionExtend()V
    .registers 1

    goto :goto_0

    nop

    :goto_0
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_provision_ProvisionBaseActivity__isAnimEnded',
        'method': '.method protected isAnimEnded()Z',
        'method_name': 'isAnimEnded',
        'method_anchors': ['iget-boolean v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mHasPreview:Z', 'if-nez v0, :cond_0', 'return v1', 'iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionAnimHelper:Lmiuix/provision/ProvisionAnimHelper;', 'if-eqz p0, :cond_1', 'invoke-virtual {p0}, Lmiuix/provision/ProvisionAnimHelper;->isAnimEnded()Z', 'return p0', 'return v1'],
        'type': 'method_replace',
        'search': """.method protected isAnimEnded()Z
    .registers 3

    iget-boolean v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mHasPreview:Z

    const/4 v1, 0x1

    if-nez v0, :cond_0

    return v1

    :cond_0
    iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionAnimHelper:Lmiuix/provision/ProvisionAnimHelper;

    if-eqz p0, :cond_1

    invoke-virtual {p0}, Lmiuix/provision/ProvisionAnimHelper;->isAnimEnded()Z

    move-result p0

    return p0

    :cond_1
    return v1
.end method""",
        'replacement': """.method protected isAnimEnded()Z
    .registers 3

    goto :goto_a

    nop

    :goto_0
    const/4 v1, 0x1

    goto :goto_8

    nop

    :goto_1
    invoke-virtual {p0}, Lmiuix/provision/ProvisionAnimHelper;->isAnimEnded()Z

    move-result p0

    goto :goto_5

    nop

    :goto_2
    iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionAnimHelper:Lmiuix/provision/ProvisionAnimHelper;

    goto :goto_7

    nop

    :goto_3
    return v1

    :goto_4
    goto :goto_2

    nop

    :goto_5
    return p0

    :goto_6
    goto :goto_9

    nop

    :goto_7
    if-nez p0, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_1

    nop

    :goto_8
    if-eqz v0, :cond_1

    goto :goto_4

    :cond_1
    goto :goto_3

    nop

    :goto_9
    return v1

    :goto_a
    iget-boolean v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mHasPreview:Z

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_provision_ProvisionBaseActivity__isBackBtnEnable',
        'method': '.method protected isBackBtnEnable()Z',
        'method_name': 'isBackBtnEnable',
        'method_anchors': ['iget-boolean p0, p0, Lmiuix/provision/ProvisionBaseActivity;->isBackBtnEnable:Z', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected isBackBtnEnable()Z
    .registers 1

    iget-boolean p0, p0, Lmiuix/provision/ProvisionBaseActivity;->isBackBtnEnable:Z

    return p0
.end method""",
        'replacement': """.method protected isBackBtnEnable()Z
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget-boolean p0, p0, Lmiuix/provision/ProvisionBaseActivity;->isBackBtnEnable:Z

    goto :goto_1

    nop

    :goto_1
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_provision_ProvisionBaseActivity__isNeedDefaultPadding',
        'method': '.method protected isNeedDefaultPadding()Z',
        'method_name': 'isNeedDefaultPadding',
        'method_anchors': ['return p0'],
        'type': 'method_replace',
        'search': """.method protected isNeedDefaultPadding()Z
    .registers 1

    const/4 p0, 0x1

    return p0
.end method""",
        'replacement': """.method protected isNeedDefaultPadding()Z
    .registers 1

    goto :goto_0

    nop

    :goto_0
    const/4 p0, 0x1

    goto :goto_1

    nop

    :goto_1
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_provision_ProvisionBaseActivity__isOtherAnimEnd',
        'method': '.method protected isOtherAnimEnd()Z',
        'method_name': 'isOtherAnimEnd',
        'method_anchors': ['return p0'],
        'type': 'method_replace',
        'search': """.method protected isOtherAnimEnd()Z
    .registers 1

    const/4 p0, 0x1

    return p0
.end method""",
        'replacement': """.method protected isOtherAnimEnd()Z
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    const/4 p0, 0x1

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_provision_ProvisionBaseActivity__isShowNavigation',
        'method': '.method protected isShowNavigation()Z',
        'method_name': 'isShowNavigation',
        'method_anchors': ['return p0'],
        'type': 'method_replace',
        'search': """.method protected isShowNavigation()Z
    .registers 1

    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method protected isShowNavigation()Z
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    const/4 p0, 0x0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_provision_ProvisionBaseActivity__onBackButtonClick',
        'method': '.method protected onBackButtonClick()V',
        'method_name': 'onBackButtonClick',
        'method_anchors': ['return-void'],
        'type': 'method_replace',
        'search': """.method protected onBackButtonClick()V
    .registers 1

    return-void
.end method""",
        'replacement': """.method protected onBackButtonClick()V
    .registers 1

    goto :goto_0

    nop

    :goto_0
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_provision_ProvisionBaseActivity__onCreate',
        'method': '.method protected onCreate(Landroid/os/Bundle;)V',
        'method_name': 'onCreate',
        'method_anchors': ['invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V', 'invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->setExtraHorizontalPaddingEnable(Z)V', 'invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->setExtraPaddingApplyToContentEnable(Z)V', 'invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->immersionEnable()Z', 'const-string v1, "OobeUtil2"', 'if-eqz v0, :cond_0', 'invoke-direct {p0}, Lmiuix/provision/ProvisionBaseActivity;->isProvisionImmersionEnable()Z', 'if-eqz v0, :cond_0'],
        'type': 'method_replace',
        'search': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 9

    invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    const/4 p1, 0x1

    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->setExtraHorizontalPaddingEnable(Z)V

    const/4 p1, 0x0

    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->setExtraPaddingApplyToContentEnable(Z)V

    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->immersionEnable()Z

    move-result v0

    const-string v1, "OobeUtil2"

    if-eqz v0, :cond_0

    invoke-direct {p0}, Lmiuix/provision/ProvisionBaseActivity;->isProvisionImmersionEnable()Z

    move-result v0

    if-eqz v0, :cond_0

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "onCreate immersionEnable: "

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->isShowNavigation()Z

    move-result v2

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v1, v0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->isShowNavigation()Z

    move-result v0

    invoke-static {p0, v0}, Lmiuix/provision/ImmersionBarUtils;->autoAdapterGestureLine(Landroid/app/Activity;Z)V

    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->immersionExtend()V

    :cond_0
    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->hasPreview()Z

    move-result v0

    iput-boolean v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mHasPreview:Z

    invoke-static {p0}, Lmiuix/provision/OobeUtil;->androidGoOrNativeAdapt(Landroid/content/Context;)Z

    move-result v0

    if-eqz v0, :cond_c

    iget-boolean v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mIsCompatibleMode:Z

    if-nez v0, :cond_c

    sget v0, Lmiuix/provision/R$layout;->provision_main_activity:I

    invoke-virtual {p0, v0}, Lmiuix/appcompat/app/AppCompatActivity;->setContentView(I)V

    sget v0, Lmiuix/provision/R$id;->provision_lyt:I

    invoke-virtual {p0, v0}, Landroid/app/Activity;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/LinearLayout;

    iput-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionLyt:Landroid/widget/LinearLayout;

    sget v0, Lmiuix/provision/R$id;->provision_container:I

    invoke-virtual {p0, v0}, Landroid/app/Activity;->findViewById(I)Landroid/view/View;

    move-result-object v0

    iput-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionContainer:Landroid/view/View;

    sget v0, Lmiuix/provision/R$id;->new_back_icon:I

    invoke-virtual {p0, v0}, Landroid/app/Activity;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/ImageView;

    iput-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mNewBackBtn:Landroid/widget/ImageView;

    sget v0, Lmiuix/provision/R$id;->actionbar_end_view:I

    invoke-virtual {p0, v0}, Landroid/app/Activity;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/ImageView;

    iput-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mActionBarEndView:Landroid/widget/ImageView;

    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->getConfig()Lmiuix/appcompat/app/GroupButtonsConfig;

    move-result-object v0

    iput-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mConfig:Lmiuix/appcompat/app/GroupButtonsConfig;

    invoke-virtual {p0, v0}, Lmiuix/appcompat/app/AppCompatActivity;->addGroupButtons(Lmiuix/appcompat/app/GroupButtonsConfig;)V

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mConfig:Lmiuix/appcompat/app/GroupButtonsConfig;

    invoke-virtual {v0}, Lmiuix/appcompat/app/GroupButtonsConfig;->getPrimaryButton()Lmiuix/appcompat/widget/Button;

    move-result-object v0

    iput-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mConfirmButton:Landroid/widget/Button;

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mConfig:Lmiuix/appcompat/app/GroupButtonsConfig;

    invoke-virtual {v0}, Lmiuix/appcompat/app/GroupButtonsConfig;->getSecondaryButton()Lmiuix/appcompat/widget/Button;

    move-result-object v0

    iput-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mSkipButton:Landroid/widget/Button;

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mConfirmButton:Landroid/widget/Button;

    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->hasNavigationButton()Z

    move-result v2

    const/16 v3, 0x8

    if-eqz v2, :cond_1

    move v2, p1

    goto :goto_0

    :cond_1
    move v2, v3

    :goto_0
    invoke-virtual {v0, v2}, Landroid/widget/Button;->setVisibility(I)V

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mConfirmButton:Landroid/widget/Button;

    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->needLongClickEvent()Z

    move-result v2

    invoke-virtual {v0, v2}, Landroid/widget/Button;->setLongClickable(Z)V

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mSkipButton:Landroid/widget/Button;

    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->needLongClickEvent()Z

    move-result v2

    invoke-virtual {v0, v2}, Landroid/widget/Button;->setLongClickable(Z)V

    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->superButtonClickListener()Z

    move-result v0

    if-eqz v0, :cond_2

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mNewBackBtn:Landroid/widget/ImageView;

    iget-object v2, p0, Lmiuix/provision/ProvisionBaseActivity;->mBackListener:Landroid/view/View$OnClickListener;

    invoke-virtual {v0, v2}, Landroid/widget/ImageView;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mConfirmButton:Landroid/widget/Button;

    iget-object v2, p0, Lmiuix/provision/ProvisionBaseActivity;->mNextClickListener:Landroid/view/View$OnClickListener;

    invoke-virtual {v0, v2}, Landroid/widget/Button;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mSkipButton:Landroid/widget/Button;

    iget-object v2, p0, Lmiuix/provision/ProvisionBaseActivity;->mSkipClickListener:Landroid/view/View$OnClickListener;

    invoke-virtual {v0, v2}, Landroid/widget/Button;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    :cond_2
    invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    invoke-virtual {v0}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;

    move-result-object v0

    iget v2, v0, Landroid/util/DisplayMetrics;->density:F

    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    const-string v5, " current density is "

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v2}, Ljava/lang/StringBuilder;->append(F)Ljava/lang/StringBuilder;

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    invoke-static {v1, v4}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->setDefaultPadding()V

    iget-object v1, p0, Lmiuix/provision/ProvisionBaseActivity;->mConfirmButton:Landroid/widget/Button;

    invoke-virtual {p0, v1}, Lmiuix/provision/ProvisionBaseActivity;->setExtraPaddingBottom(Landroid/widget/Button;)V

    invoke-virtual {p0, v0, v2}, Lmiuix/provision/ProvisionBaseActivity;->adaptFoldContainerMargin(Landroid/util/DisplayMetrics;F)V

    invoke-virtual {p0, v0}, Lmiuix/provision/ProvisionBaseActivity;->adaptPadImageStyleLayout(Landroid/util/DisplayMetrics;)V

    sget v0, Lmiuix/provision/R$id;->provision_title_space:I

    invoke-virtual {p0, v0}, Landroid/app/Activity;->findViewById(I)Landroid/view/View;

    move-result-object v0

    iput-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mTitleSpace:Landroid/view/View;

    sget v0, Lmiuix/provision/R$id;->lottie_animation_view:I

    invoke-virtual {p0, v0}, Landroid/app/Activity;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Lcom/airbnb/lottie/LottieAnimationView;

    iput-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mLottieAnimationView:Lcom/airbnb/lottie/LottieAnimationView;

    sget v0, Lmiuix/provision/R$id;->provision_lyt_title:I

    invoke-virtual {p0, v0}, Landroid/app/Activity;->findViewById(I)Landroid/view/View;

    move-result-object v0

    iput-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mTitleLayout:Landroid/view/View;

    sget v0, Lmiuix/provision/R$id;->provision_title:I

    invoke-virtual {p0, v0}, Landroid/app/Activity;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Lmiuix/appcompat/widget/TextView;

    iput-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mTitle:Lmiuix/appcompat/widget/TextView;

    sget v0, Lmiuix/provision/R$id;->provision_lyt_subtitle:I

    invoke-virtual {p0, v0}, Landroid/app/Activity;->findViewById(I)Landroid/view/View;

    move-result-object v0

    iput-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mSubTitleLayout:Landroid/view/View;

    sget v0, Lmiuix/provision/R$id;->provision_sub_title:I

    invoke-virtual {p0, v0}, Landroid/app/Activity;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Lmiuix/appcompat/widget/TextView;

    iput-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mSubTitle:Lmiuix/appcompat/widget/TextView;

    sget v0, Lmiuix/provision/R$id;->provision_preview_img:I

    invoke-virtual {p0, v0}, Landroid/app/Activity;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/ImageView;

    iput-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mImageView:Landroid/widget/ImageView;

    sget v0, Lmiuix/provision/R$id;->video_display_surfaceview:I

    invoke-virtual {p0, v0}, Landroid/app/Activity;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/view/TextureView;

    iput-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mDisplayView:Landroid/view/TextureView;

    new-instance v0, Landroid/media/MediaPlayer;

    invoke-direct {v0}, Landroid/media/MediaPlayer;-><init>()V

    iput-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mMediaPlayer:Landroid/media/MediaPlayer;

    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->hasNewPageAnim()Z

    move-result v0

    if-eqz v0, :cond_3

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_3

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mDisplayView:Landroid/view/TextureView;

    invoke-virtual {v0, p1}, Landroid/view/TextureView;->setVisibility(I)V

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mDisplayView:Landroid/view/TextureView;

    iget-object v1, p0, Lmiuix/provision/ProvisionBaseActivity;->mSurfaceTextureListener:Landroid/view/TextureView$SurfaceTextureListener;

    invoke-virtual {v0, v1}, Landroid/view/TextureView;->setSurfaceTextureListener(Landroid/view/TextureView$SurfaceTextureListener;)V

    :cond_3
    invoke-static {p0}, Lmiuix/provision/OobeUtil;->isFoldLarge(Landroid/content/Context;)Z

    move-result v0

    if-eqz v0, :cond_4

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mTitleLayout:Landroid/view/View;

    invoke-virtual {v0}, Landroid/view/View;->getPaddingStart()I

    move-result v1

    iget-object v2, p0, Lmiuix/provision/ProvisionBaseActivity;->mTitleLayout:Landroid/view/View;

    invoke-virtual {v2}, Landroid/view/View;->getPaddingTop()I

    move-result v2

    iget-object v4, p0, Lmiuix/provision/ProvisionBaseActivity;->mTitleLayout:Landroid/view/View;

    invoke-virtual {v4}, Landroid/view/View;->getPaddingEnd()I

    move-result v4

    invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;

    move-result-object v5

    sget v6, Lmiuix/provision/R$dimen;->provision_title_padding_bottom_fold:I

    invoke-virtual {v5, v6}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result v5

    invoke-virtual {v0, v1, v2, v4, v5}, Landroid/view/View;->setPaddingRelative(IIII)V

    :cond_4
    invoke-static {p0}, Lmiuix/provision/OobeUtil;->isTabletPort(Landroid/content/Context;)Z

    move-result v0

    if-eqz v0, :cond_5

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mTitleSpace:Landroid/view/View;

    invoke-virtual {v0, p1}, Landroid/view/View;->setVisibility(I)V

    :cond_5
    iget-boolean v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mHasPreview:Z

    if-nez v0, :cond_b

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mLottieAnimationView:Lcom/airbnb/lottie/LottieAnimationView;

    invoke-virtual {v0, v3}, Landroid/widget/ImageView;->setVisibility(I)V

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mTitleSpace:Landroid/view/View;

    if-eqz v0, :cond_6

    invoke-virtual {v0}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v0

    invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;

    move-result-object v1

    sget v2, Lmiuix/provision/R$dimen;->provision_space_between_actionbar_title_pad_port_no_lottie:I

    invoke-virtual {v1, v2}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result v1

    iput v1, v0, Landroid/view/ViewGroup$LayoutParams;->height:I

    iget-object v1, p0, Lmiuix/provision/ProvisionBaseActivity;->mTitleSpace:Landroid/view/View;

    invoke-virtual {v1, v0}, Landroid/view/View;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    :cond_6
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mSubTitleLayout:Landroid/view/View;

    invoke-virtual {v0, p1}, Landroid/view/View;->setVisibility(I)V

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mSubTitle:Lmiuix/appcompat/widget/TextView;

    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->hasSubTitle()Z

    move-result v1

    if-eqz v1, :cond_7

    move v3, p1

    :cond_7
    invoke-virtual {v0, v3}, Landroid/widget/TextView;->setVisibility(I)V

    invoke-static {p0}, Lmiuix/provision/OobeUtil;->isTabletLand(Landroid/content/Context;)Z

    move-result v0

    if-eqz v0, :cond_8

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mSubTitleLayout:Landroid/view/View;

    invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;

    move-result-object v1

    sget v2, Lmiuix/provision/R$dimen;->provision_subtitle_lyt_min_height_pad_land:I

    invoke-virtual {v1, v2}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result v1

    invoke-virtual {v0, v1}, Landroid/view/View;->setMinimumHeight(I)V

    goto :goto_1

    :cond_8
    invoke-static {p0}, Lmiuix/provision/OobeUtil;->isTabletPort(Landroid/content/Context;)Z

    move-result v0

    if-eqz v0, :cond_9

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mSubTitleLayout:Landroid/view/View;

    invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;

    move-result-object v1

    sget v2, Lmiuix/provision/R$dimen;->provision_subtitle_lyt_min_height_pad_port:I

    invoke-virtual {v1, v2}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result v1

    invoke-virtual {v0, v1}, Landroid/view/View;->setMinimumHeight(I)V

    :cond_9
    :goto_1
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mTitleLayout:Landroid/view/View;

    invoke-virtual {v0}, Landroid/view/View;->getPaddingStart()I

    move-result v1

    sget-boolean v2, Lmiui/os/Build;->IS_TABLET:Z

    if-eqz v2, :cond_a

    move v2, p1

    goto :goto_2

    :cond_a
    invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;

    move-result-object v2

    sget v3, Lmiuix/provision/R$dimen;->provision_title_padding_top_no_lottie:I

    invoke-virtual {v2, v3}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result v2

    :goto_2
    iget-object v3, p0, Lmiuix/provision/ProvisionBaseActivity;->mTitleLayout:Landroid/view/View;

    invoke-virtual {v3}, Landroid/view/View;->getPaddingEnd()I

    move-result v3

    invoke-virtual {v0, v1, v2, v3, p1}, Landroid/view/View;->setPaddingRelative(IIII)V

    :cond_b
    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->delayEnableButton()V

    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->setBackButtonContentDescription()V

    :cond_c
    invoke-virtual {p0}, Landroid/app/Activity;->getWindow()Landroid/view/Window;

    move-result-object p1

    invoke-static {p1}, Lmiuix/provision/OobeUtil;->setTranslucentNavigationBar(Landroid/view/Window;)V

    invoke-virtual {p0}, Landroid/app/Activity;->getPackageName()Ljava/lang/String;

    move-result-object p1

    const-string v0, "com.miui.voicetrigger"

    invoke-virtual {p1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result p1

    if-eqz p1, :cond_d

    invoke-virtual {p0}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p1

    const-string v0, "new_feature"

    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->getXiaoAiSupportVersion()I

    move-result p0

    invoke-static {p1, v0, p0}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    :cond_d
    return-void
.end method""",
        'replacement': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 9

    goto :goto_96

    nop

    :goto_0
    sget v2, Lmiuix/provision/R$dimen;->provision_subtitle_lyt_min_height_pad_port:I

    goto :goto_b3

    nop

    :goto_1
    invoke-virtual {v0}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v0

    goto :goto_c6

    nop

    :goto_2
    goto :goto_78

    :goto_3
    goto :goto_77

    nop

    :goto_4
    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    goto :goto_2c

    nop

    :goto_5
    iget-object v2, p0, Lmiuix/provision/ProvisionBaseActivity;->mNextClickListener:Landroid/view/View$OnClickListener;

    goto :goto_9a

    nop

    :goto_6
    invoke-virtual {v0}, Landroid/view/View;->getPaddingStart()I

    move-result v1

    goto :goto_b

    nop

    :goto_7
    const/16 v3, 0x8

    goto :goto_52

    nop

    :goto_8
    iput-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mSubTitleLayout:Landroid/view/View;

    goto :goto_d5

    nop

    :goto_9
    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->getConfig()Lmiuix/appcompat/app/GroupButtonsConfig;

    move-result-object v0

    goto :goto_a5

    nop

    :goto_a
    iget-object v2, p0, Lmiuix/provision/ProvisionBaseActivity;->mTitleLayout:Landroid/view/View;

    goto :goto_41

    nop

    :goto_b
    sget-boolean v2, Lmiui/os/Build;->IS_TABLET:Z

    goto :goto_d0

    nop

    :goto_c
    invoke-virtual {v5, v6}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result v5

    goto :goto_25

    nop

    :goto_d
    invoke-virtual {p0}, Landroid/app/Activity;->getWindow()Landroid/view/Window;

    move-result-object p1

    goto :goto_46

    nop

    :goto_e
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_27

    nop

    :goto_f
    sget v0, Lmiuix/provision/R$layout;->provision_main_activity:I

    goto :goto_8d

    nop

    :goto_10
    invoke-static {p0}, Lmiuix/provision/OobeUtil;->isTabletPort(Landroid/content/Context;)Z

    move-result v0

    goto :goto_2b

    nop

    :goto_11
    const/4 p1, 0x0

    goto :goto_70

    nop

    :goto_12
    invoke-direct {p0}, Lmiuix/provision/ProvisionBaseActivity;->isProvisionImmersionEnable()Z

    move-result v0

    goto :goto_ae

    nop

    :goto_13
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mTitleLayout:Landroid/view/View;

    goto :goto_6

    nop

    :goto_14
    iput-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mNewBackBtn:Landroid/widget/ImageView;

    goto :goto_2d

    nop

    :goto_15
    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->isShowNavigation()Z

    move-result v2

    goto :goto_6a

    nop

    :goto_16
    iget-object v2, p0, Lmiuix/provision/ProvisionBaseActivity;->mBackListener:Landroid/view/View$OnClickListener;

    goto :goto_7b

    nop

    :goto_17
    sget v3, Lmiuix/provision/R$dimen;->provision_title_padding_top_no_lottie:I

    goto :goto_21

    nop

    :goto_18
    invoke-virtual {v4}, Landroid/view/View;->getPaddingEnd()I

    move-result v4

    goto :goto_c2

    nop

    :goto_19
    const-string v0, "new_feature"

    goto :goto_5e

    nop

    :goto_1a
    new-instance v4, Ljava/lang/StringBuilder;

    goto :goto_9e

    nop

    :goto_1b
    iput-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mTitleLayout:Landroid/view/View;

    goto :goto_1f

    nop

    :goto_1c
    const-string v0, "com.miui.voicetrigger"

    goto :goto_a0

    nop

    :goto_1d
    if-nez v0, :cond_0

    goto :goto_58

    :cond_0
    goto :goto_12

    nop

    :goto_1e
    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->immersionEnable()Z

    move-result v0

    goto :goto_76

    nop

    :goto_1f
    sget v0, Lmiuix/provision/R$id;->provision_title:I

    goto :goto_56

    nop

    :goto_20
    if-nez v0, :cond_1

    goto :goto_c8

    :cond_1
    goto :goto_ce

    nop

    :goto_21
    invoke-virtual {v2, v3}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result v2

    :goto_22
    goto :goto_b8

    nop

    :goto_23
    goto :goto_a8

    :goto_24
    goto :goto_10

    nop

    :goto_25
    invoke-virtual {v0, v1, v2, v4, v5}, Landroid/view/View;->setPaddingRelative(IIII)V

    :goto_26
    goto :goto_8e

    nop

    :goto_27
    const-string v2, "onCreate immersionEnable: "

    goto :goto_6c

    nop

    :goto_28
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mConfirmButton:Landroid/widget/Button;

    goto :goto_d9

    nop

    :goto_29
    if-nez v1, :cond_2

    goto :goto_75

    :cond_2
    goto :goto_74

    nop

    :goto_2a
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mConfig:Lmiuix/appcompat/app/GroupButtonsConfig;

    goto :goto_7a

    nop

    :goto_2b
    if-nez v0, :cond_3

    goto :goto_a8

    :cond_3
    goto :goto_aa

    nop

    :goto_2c
    invoke-static {v1, v4}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_63

    nop

    :goto_2d
    sget v0, Lmiuix/provision/R$id;->actionbar_end_view:I

    goto :goto_bb

    nop

    :goto_2e
    check-cast v0, Lcom/airbnb/lottie/LottieAnimationView;

    goto :goto_82

    nop

    :goto_2f
    invoke-virtual {p0, v0}, Landroid/app/Activity;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_60

    nop

    :goto_30
    new-instance v0, Landroid/media/MediaPlayer;

    goto :goto_93

    nop

    :goto_31
    sget v2, Lmiuix/provision/R$dimen;->provision_subtitle_lyt_min_height_pad_land:I

    goto :goto_64

    nop

    :goto_32
    sget v0, Lmiuix/provision/R$id;->new_back_icon:I

    goto :goto_5d

    nop

    :goto_33
    iput-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mTitleSpace:Landroid/view/View;

    goto :goto_e1

    nop

    :goto_34
    invoke-static {p1, v0, p0}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    :goto_35
    goto :goto_a4

    nop

    :goto_36
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mSubTitleLayout:Landroid/view/View;

    goto :goto_c4

    nop

    :goto_37
    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->needLongClickEvent()Z

    move-result v2

    goto :goto_54

    nop

    :goto_38
    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->needLongClickEvent()Z

    move-result v2

    goto :goto_3a

    nop

    :goto_39
    if-nez v0, :cond_4

    goto :goto_24

    :cond_4
    goto :goto_de

    nop

    :goto_3a
    invoke-virtual {v0, v2}, Landroid/widget/Button;->setLongClickable(Z)V

    goto :goto_a6

    nop

    :goto_3b
    invoke-virtual {v1, v0}, Landroid/view/View;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    :goto_3c
    goto :goto_36

    nop

    :goto_3d
    invoke-static {v1, v0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_49

    nop

    :goto_3e
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mDisplayView:Landroid/view/TextureView;

    goto :goto_a3

    nop

    :goto_3f
    sget v0, Lmiuix/provision/R$id;->provision_preview_img:I

    goto :goto_c9

    nop

    :goto_40
    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->hasPreview()Z

    move-result v0

    goto :goto_5a

    nop

    :goto_41
    invoke-virtual {v2}, Landroid/view/View;->getPaddingTop()I

    move-result v2

    goto :goto_98

    nop

    :goto_42
    if-nez v0, :cond_5

    goto :goto_bf

    :cond_5
    goto :goto_4a

    nop

    :goto_43
    iget-object v2, p0, Lmiuix/provision/ProvisionBaseActivity;->mSkipClickListener:Landroid/view/View$OnClickListener;

    goto :goto_c7

    nop

    :goto_44
    iput-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mImageView:Landroid/widget/ImageView;

    goto :goto_a9

    nop

    :goto_45
    sget v0, Lmiuix/provision/R$id;->provision_lyt:I

    goto :goto_b0

    nop

    :goto_46
    invoke-static {p1}, Lmiuix/provision/OobeUtil;->setTranslucentNavigationBar(Landroid/view/Window;)V

    goto :goto_cb

    nop

    :goto_47
    sget v6, Lmiuix/provision/R$dimen;->provision_title_padding_bottom_fold:I

    goto :goto_c

    nop

    :goto_48
    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->delayEnableButton()V

    goto :goto_c0

    nop

    :goto_49
    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->isShowNavigation()Z

    move-result v0

    goto :goto_8b

    nop

    :goto_4a
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mTitleSpace:Landroid/view/View;

    goto :goto_be

    nop

    :goto_4b
    if-nez p1, :cond_6

    goto :goto_35

    :cond_6
    goto :goto_e0

    nop

    :goto_4c
    invoke-virtual {v0, v3}, Landroid/widget/ImageView;->setVisibility(I)V

    goto :goto_68

    nop

    :goto_4d
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    goto :goto_3d

    nop

    :goto_4e
    iget-boolean v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mIsCompatibleMode:Z

    goto :goto_79

    nop

    :goto_4f
    sget v0, Lmiuix/provision/R$id;->provision_lyt_title:I

    goto :goto_d8

    nop

    :goto_50
    move v2, p1

    goto :goto_87

    nop

    :goto_51
    check-cast v0, Landroid/widget/ImageView;

    goto :goto_62

    nop

    :goto_52
    if-nez v2, :cond_7

    goto :goto_3

    :cond_7
    goto :goto_67

    nop

    :goto_53
    if-eqz v0, :cond_8

    goto :goto_80

    :cond_8
    goto :goto_3e

    nop

    :goto_54
    invoke-virtual {v0, v2}, Landroid/widget/Button;->setLongClickable(Z)V

    goto :goto_a1

    nop

    :goto_55
    invoke-virtual {v0, v3}, Landroid/widget/TextView;->setVisibility(I)V

    goto :goto_b7

    nop

    :goto_56
    invoke-virtual {p0, v0}, Landroid/app/Activity;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_b9

    nop

    :goto_57
    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->immersionExtend()V

    :goto_58
    goto :goto_40

    nop

    :goto_59
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_e

    nop

    :goto_5a
    iput-boolean v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mHasPreview:Z

    goto :goto_81

    nop

    :goto_5b
    invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    goto :goto_66

    nop

    :goto_5c
    invoke-virtual {v0, v1}, Landroid/view/View;->setMinimumHeight(I)V

    goto :goto_23

    nop

    :goto_5d
    invoke-virtual {p0, v0}, Landroid/app/Activity;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_7e

    nop

    :goto_5e
    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->getXiaoAiSupportVersion()I

    move-result p0

    goto :goto_34

    nop

    :goto_5f
    if-nez v0, :cond_9

    goto :goto_c1

    :cond_9
    goto :goto_4e

    nop

    :goto_60
    check-cast v0, Landroid/view/TextureView;

    goto :goto_b1

    nop

    :goto_61
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mConfirmButton:Landroid/widget/Button;

    goto :goto_5

    nop

    :goto_62
    iput-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mActionBarEndView:Landroid/widget/ImageView;

    goto :goto_9

    nop

    :goto_63
    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->setDefaultPadding()V

    goto :goto_d2

    nop

    :goto_64
    invoke-virtual {v1, v2}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result v1

    goto :goto_5c

    nop

    :goto_65
    if-eqz v0, :cond_a

    goto :goto_ac

    :cond_a
    goto :goto_d6

    nop

    :goto_66
    invoke-virtual {v0}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;

    move-result-object v0

    goto :goto_69

    nop

    :goto_67
    move v2, p1

    goto :goto_2

    nop

    :goto_68
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mTitleSpace:Landroid/view/View;

    goto :goto_6b

    nop

    :goto_69
    iget v2, v0, Landroid/util/DisplayMetrics;->density:F

    goto :goto_1a

    nop

    :goto_6a
    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    goto :goto_4d

    nop

    :goto_6b
    if-nez v0, :cond_b

    goto :goto_3c

    :cond_b
    goto :goto_1

    nop

    :goto_6c
    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_15

    nop

    :goto_6d
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mConfirmButton:Landroid/widget/Button;

    goto :goto_38

    nop

    :goto_6e
    invoke-virtual {v0}, Lmiuix/appcompat/app/GroupButtonsConfig;->getSecondaryButton()Lmiuix/appcompat/widget/Button;

    move-result-object v0

    goto :goto_cd

    nop

    :goto_6f
    iget-object v1, p0, Lmiuix/provision/ProvisionBaseActivity;->mTitleSpace:Landroid/view/View;

    goto :goto_3b

    nop

    :goto_70
    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->setExtraPaddingApplyToContentEnable(Z)V

    goto :goto_1e

    nop

    :goto_71
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mDisplayView:Landroid/view/TextureView;

    goto :goto_8f

    nop

    :goto_72
    invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;

    move-result-object v2

    goto :goto_17

    nop

    :goto_73
    invoke-virtual {p0, v1}, Lmiuix/provision/ProvisionBaseActivity;->setExtraPaddingBottom(Landroid/widget/Button;)V

    goto :goto_89

    nop

    :goto_74
    move v3, p1

    :goto_75
    goto :goto_55

    nop

    :goto_76
    const-string v1, "OobeUtil2"

    goto :goto_1d

    nop

    :goto_77
    move v2, v3

    :goto_78
    goto :goto_b5

    nop

    :goto_79
    if-eqz v0, :cond_c

    goto :goto_c1

    :cond_c
    goto :goto_f

    nop

    :goto_7a
    invoke-virtual {v0}, Lmiuix/appcompat/app/GroupButtonsConfig;->getPrimaryButton()Lmiuix/appcompat/widget/Button;

    move-result-object v0

    goto :goto_ba

    nop

    :goto_7b
    invoke-virtual {v0, v2}, Landroid/widget/ImageView;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    goto :goto_61

    nop

    :goto_7c
    invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;

    move-result-object v1

    goto :goto_31

    nop

    :goto_7d
    invoke-virtual {p0, v0}, Landroid/app/Activity;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_8

    nop

    :goto_7e
    check-cast v0, Landroid/widget/ImageView;

    goto :goto_14

    nop

    :goto_7f
    invoke-virtual {v0, v1}, Landroid/view/TextureView;->setSurfaceTextureListener(Landroid/view/TextureView$SurfaceTextureListener;)V

    :goto_80
    goto :goto_c3

    nop

    :goto_81
    invoke-static {p0}, Lmiuix/provision/OobeUtil;->androidGoOrNativeAdapt(Landroid/content/Context;)Z

    move-result v0

    goto :goto_5f

    nop

    :goto_82
    iput-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mLottieAnimationView:Lcom/airbnb/lottie/LottieAnimationView;

    goto :goto_4f

    nop

    :goto_83
    invoke-virtual {p0, v0}, Landroid/app/Activity;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_2e

    nop

    :goto_84
    invoke-virtual {v0}, Landroid/view/View;->getPaddingStart()I

    move-result v1

    goto :goto_a

    nop

    :goto_85
    invoke-virtual {p0, v0}, Landroid/app/Activity;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_33

    nop

    :goto_86
    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->setExtraHorizontalPaddingEnable(Z)V

    goto :goto_11

    nop

    :goto_87
    goto :goto_22

    :goto_88
    goto :goto_72

    nop

    :goto_89
    invoke-virtual {p0, v0, v2}, Lmiuix/provision/ProvisionBaseActivity;->adaptFoldContainerMargin(Landroid/util/DisplayMetrics;F)V

    goto :goto_dd

    nop

    :goto_8a
    invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;

    move-result-object v1

    goto :goto_0

    nop

    :goto_8b
    invoke-static {p0, v0}, Lmiuix/provision/ImmersionBarUtils;->autoAdapterGestureLine(Landroid/app/Activity;Z)V

    goto :goto_57

    nop

    :goto_8c
    iput-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionContainer:Landroid/view/View;

    goto :goto_32

    nop

    :goto_8d
    invoke-virtual {p0, v0}, Lmiuix/appcompat/app/AppCompatActivity;->setContentView(I)V

    goto :goto_45

    nop

    :goto_8e
    invoke-static {p0}, Lmiuix/provision/OobeUtil;->isTabletPort(Landroid/content/Context;)Z

    move-result v0

    goto :goto_42

    nop

    :goto_8f
    iget-object v1, p0, Lmiuix/provision/ProvisionBaseActivity;->mSurfaceTextureListener:Landroid/view/TextureView$SurfaceTextureListener;

    goto :goto_7f

    nop

    :goto_90
    invoke-virtual {v4, v2}, Ljava/lang/StringBuilder;->append(F)Ljava/lang/StringBuilder;

    goto :goto_4

    nop

    :goto_91
    iput-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mMediaPlayer:Landroid/media/MediaPlayer;

    goto :goto_b6

    nop

    :goto_92
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mSubTitle:Lmiuix/appcompat/widget/TextView;

    goto :goto_c5

    nop

    :goto_93
    invoke-direct {v0}, Landroid/media/MediaPlayer;-><init>()V

    goto :goto_91

    nop

    :goto_94
    iput v1, v0, Landroid/view/ViewGroup$LayoutParams;->height:I

    goto :goto_6f

    nop

    :goto_95
    check-cast v0, Lmiuix/appcompat/widget/TextView;

    goto :goto_af

    nop

    :goto_96
    invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    goto :goto_ca

    nop

    :goto_97
    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_90

    nop

    :goto_98
    iget-object v4, p0, Lmiuix/provision/ProvisionBaseActivity;->mTitleLayout:Landroid/view/View;

    goto :goto_18

    nop

    :goto_99
    check-cast v0, Landroid/widget/LinearLayout;

    goto :goto_dc

    nop

    :goto_9a
    invoke-virtual {v0, v2}, Landroid/widget/Button;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    goto :goto_d4

    nop

    :goto_9b
    iget-boolean v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mHasPreview:Z

    goto :goto_65

    nop

    :goto_9c
    sget v2, Lmiuix/provision/R$dimen;->provision_space_between_actionbar_title_pad_port_no_lottie:I

    goto :goto_b4

    nop

    :goto_9d
    iput-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mTitle:Lmiuix/appcompat/widget/TextView;

    goto :goto_d3

    nop

    :goto_9e
    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_bd

    nop

    :goto_9f
    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    goto :goto_53

    nop

    :goto_a0
    invoke-virtual {p1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result p1

    goto :goto_4b

    nop

    :goto_a1
    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->superButtonClickListener()Z

    move-result v0

    goto :goto_20

    nop

    :goto_a2
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mConfig:Lmiuix/appcompat/app/GroupButtonsConfig;

    goto :goto_6e

    nop

    :goto_a3
    invoke-virtual {v0, p1}, Landroid/view/TextureView;->setVisibility(I)V

    goto :goto_71

    nop

    :goto_a4
    return-void

    :goto_a5
    iput-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mConfig:Lmiuix/appcompat/app/GroupButtonsConfig;

    goto :goto_d1

    nop

    :goto_a6
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mSkipButton:Landroid/widget/Button;

    goto :goto_37

    nop

    :goto_a7
    invoke-virtual {v0, v1}, Landroid/view/View;->setMinimumHeight(I)V

    :goto_a8
    goto :goto_13

    nop

    :goto_a9
    sget v0, Lmiuix/provision/R$id;->video_display_surfaceview:I

    goto :goto_2f

    nop

    :goto_aa
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mSubTitleLayout:Landroid/view/View;

    goto :goto_8a

    nop

    :goto_ab
    invoke-virtual {v0, v1, v2, v3, p1}, Landroid/view/View;->setPaddingRelative(IIII)V

    :goto_ac
    goto :goto_48

    nop

    :goto_ad
    sget v0, Lmiuix/provision/R$id;->provision_container:I

    goto :goto_df

    nop

    :goto_ae
    if-nez v0, :cond_d

    goto :goto_58

    :cond_d
    goto :goto_59

    nop

    :goto_af
    iput-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mSubTitle:Lmiuix/appcompat/widget/TextView;

    goto :goto_3f

    nop

    :goto_b0
    invoke-virtual {p0, v0}, Landroid/app/Activity;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_99

    nop

    :goto_b1
    iput-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mDisplayView:Landroid/view/TextureView;

    goto :goto_30

    nop

    :goto_b2
    if-nez v0, :cond_e

    goto :goto_80

    :cond_e
    goto :goto_9f

    nop

    :goto_b3
    invoke-virtual {v1, v2}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result v1

    goto :goto_a7

    nop

    :goto_b4
    invoke-virtual {v1, v2}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result v1

    goto :goto_94

    nop

    :goto_b5
    invoke-virtual {v0, v2}, Landroid/widget/Button;->setVisibility(I)V

    goto :goto_6d

    nop

    :goto_b6
    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->hasNewPageAnim()Z

    move-result v0

    goto :goto_b2

    nop

    :goto_b7
    invoke-static {p0}, Lmiuix/provision/OobeUtil;->isTabletLand(Landroid/content/Context;)Z

    move-result v0

    goto :goto_39

    nop

    :goto_b8
    iget-object v3, p0, Lmiuix/provision/ProvisionBaseActivity;->mTitleLayout:Landroid/view/View;

    goto :goto_da

    nop

    :goto_b9
    check-cast v0, Lmiuix/appcompat/widget/TextView;

    goto :goto_9d

    nop

    :goto_ba
    iput-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mConfirmButton:Landroid/widget/Button;

    goto :goto_a2

    nop

    :goto_bb
    invoke-virtual {p0, v0}, Landroid/app/Activity;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_51

    nop

    :goto_bc
    invoke-virtual {p0, v0}, Landroid/app/Activity;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_95

    nop

    :goto_bd
    const-string v5, " current density is "

    goto :goto_97

    nop

    :goto_be
    invoke-virtual {v0, p1}, Landroid/view/View;->setVisibility(I)V

    :goto_bf
    goto :goto_9b

    nop

    :goto_c0
    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->setBackButtonContentDescription()V

    :goto_c1
    goto :goto_d

    nop

    :goto_c2
    invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;

    move-result-object v5

    goto :goto_47

    nop

    :goto_c3
    invoke-static {p0}, Lmiuix/provision/OobeUtil;->isFoldLarge(Landroid/content/Context;)Z

    move-result v0

    goto :goto_cc

    nop

    :goto_c4
    invoke-virtual {v0, p1}, Landroid/view/View;->setVisibility(I)V

    goto :goto_92

    nop

    :goto_c5
    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->hasSubTitle()Z

    move-result v1

    goto :goto_29

    nop

    :goto_c6
    invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;

    move-result-object v1

    goto :goto_9c

    nop

    :goto_c7
    invoke-virtual {v0, v2}, Landroid/widget/Button;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    :goto_c8
    goto :goto_5b

    nop

    :goto_c9
    invoke-virtual {p0, v0}, Landroid/app/Activity;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_db

    nop

    :goto_ca
    const/4 p1, 0x1

    goto :goto_86

    nop

    :goto_cb
    invoke-virtual {p0}, Landroid/app/Activity;->getPackageName()Ljava/lang/String;

    move-result-object p1

    goto :goto_1c

    nop

    :goto_cc
    if-nez v0, :cond_f

    goto :goto_26

    :cond_f
    goto :goto_cf

    nop

    :goto_cd
    iput-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mSkipButton:Landroid/widget/Button;

    goto :goto_28

    nop

    :goto_ce
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mNewBackBtn:Landroid/widget/ImageView;

    goto :goto_16

    nop

    :goto_cf
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mTitleLayout:Landroid/view/View;

    goto :goto_84

    nop

    :goto_d0
    if-nez v2, :cond_10

    goto :goto_88

    :cond_10
    goto :goto_50

    nop

    :goto_d1
    invoke-virtual {p0, v0}, Lmiuix/appcompat/app/AppCompatActivity;->addGroupButtons(Lmiuix/appcompat/app/GroupButtonsConfig;)V

    goto :goto_2a

    nop

    :goto_d2
    iget-object v1, p0, Lmiuix/provision/ProvisionBaseActivity;->mConfirmButton:Landroid/widget/Button;

    goto :goto_73

    nop

    :goto_d3
    sget v0, Lmiuix/provision/R$id;->provision_lyt_subtitle:I

    goto :goto_7d

    nop

    :goto_d4
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mSkipButton:Landroid/widget/Button;

    goto :goto_43

    nop

    :goto_d5
    sget v0, Lmiuix/provision/R$id;->provision_sub_title:I

    goto :goto_bc

    nop

    :goto_d6
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mLottieAnimationView:Lcom/airbnb/lottie/LottieAnimationView;

    goto :goto_4c

    nop

    :goto_d7
    sget v0, Lmiuix/provision/R$id;->provision_title_space:I

    goto :goto_85

    nop

    :goto_d8
    invoke-virtual {p0, v0}, Landroid/app/Activity;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_1b

    nop

    :goto_d9
    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->hasNavigationButton()Z

    move-result v2

    goto :goto_7

    nop

    :goto_da
    invoke-virtual {v3}, Landroid/view/View;->getPaddingEnd()I

    move-result v3

    goto :goto_ab

    nop

    :goto_db
    check-cast v0, Landroid/widget/ImageView;

    goto :goto_44

    nop

    :goto_dc
    iput-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionLyt:Landroid/widget/LinearLayout;

    goto :goto_ad

    nop

    :goto_dd
    invoke-virtual {p0, v0}, Lmiuix/provision/ProvisionBaseActivity;->adaptPadImageStyleLayout(Landroid/util/DisplayMetrics;)V

    goto :goto_d7

    nop

    :goto_de
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mSubTitleLayout:Landroid/view/View;

    goto :goto_7c

    nop

    :goto_df
    invoke-virtual {p0, v0}, Landroid/app/Activity;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_8c

    nop

    :goto_e0
    invoke-virtual {p0}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p1

    goto :goto_19

    nop

    :goto_e1
    sget v0, Lmiuix/provision/R$id;->lottie_animation_view:I

    goto :goto_83

    nop
.end method""",
        'required': True,
        'policy_status': 'BUILD_FLAG_PARTIALLY_SKIPPED',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_provision_ProvisionBaseActivity__onDestroy',
        'method': '.method protected onDestroy()V',
        'method_name': 'onDestroy',
        'method_anchors': ['invoke-super {p0}, Lmiuix/appcompat/app/AppCompatActivity;->onDestroy()V', 'iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mImageView:Landroid/widget/ImageView;', 'if-eqz v0, :cond_0', 'invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setImageDrawable(Landroid/graphics/drawable/Drawable;)V', 'iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mLottieAnimationView:Lcom/airbnb/lottie/LottieAnimationView;', 'if-eqz v0, :cond_1', 'invoke-virtual {v0}, Lcom/airbnb/lottie/LottieAnimationView;->cancelAnimation()V', 'iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mLottieAnimationView:Lcom/airbnb/lottie/LottieAnimationView;'],
        'type': 'method_replace',
        'search': """.method protected onDestroy()V
    .registers 3

    invoke-super {p0}, Lmiuix/appcompat/app/AppCompatActivity;->onDestroy()V

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mImageView:Landroid/widget/ImageView;

    const/4 v1, 0x0

    if-eqz v0, :cond_0

    invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setImageDrawable(Landroid/graphics/drawable/Drawable;)V

    :cond_0
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mLottieAnimationView:Lcom/airbnb/lottie/LottieAnimationView;

    if-eqz v0, :cond_1

    invoke-virtual {v0}, Lcom/airbnb/lottie/LottieAnimationView;->cancelAnimation()V

    iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mLottieAnimationView:Lcom/airbnb/lottie/LottieAnimationView;

    invoke-virtual {p0, v1}, Lcom/airbnb/lottie/LottieAnimationView;->setImageDrawable(Landroid/graphics/drawable/Drawable;)V

    :cond_1
    return-void
.end method""",
        'replacement': """.method protected onDestroy()V
    .registers 3

    goto :goto_8

    nop

    :goto_0
    return-void

    :goto_1
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mLottieAnimationView:Lcom/airbnb/lottie/LottieAnimationView;

    goto :goto_b

    nop

    :goto_2
    const/4 v1, 0x0

    goto :goto_4

    nop

    :goto_3
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mImageView:Landroid/widget/ImageView;

    goto :goto_2

    nop

    :goto_4
    if-nez v0, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_5

    nop

    :goto_5
    invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setImageDrawable(Landroid/graphics/drawable/Drawable;)V

    :goto_6
    goto :goto_1

    nop

    :goto_7
    iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mLottieAnimationView:Lcom/airbnb/lottie/LottieAnimationView;

    goto :goto_9

    nop

    :goto_8
    invoke-super {p0}, Lmiuix/appcompat/app/AppCompatActivity;->onDestroy()V

    goto :goto_3

    nop

    :goto_9
    invoke-virtual {p0, v1}, Lcom/airbnb/lottie/LottieAnimationView;->setImageDrawable(Landroid/graphics/drawable/Drawable;)V

    :goto_a
    goto :goto_0

    nop

    :goto_b
    if-nez v0, :cond_1

    goto :goto_a

    :cond_1
    goto :goto_c

    nop

    :goto_c
    invoke-virtual {v0}, Lcom/airbnb/lottie/LottieAnimationView;->cancelAnimation()V

    goto :goto_7

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_provision_ProvisionBaseActivity__onNextButtonClick',
        'method': '.method protected onNextButtonClick()V',
        'method_name': 'onNextButtonClick',
        'method_anchors': ['return-void'],
        'type': 'method_replace',
        'search': """.method protected onNextButtonClick()V
    .registers 1

    return-void
.end method""",
        'replacement': """.method protected onNextButtonClick()V
    .registers 1

    goto :goto_0

    nop

    :goto_0
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_provision_ProvisionBaseActivity__onResume',
        'method': '.method protected onResume()V',
        'method_name': 'onResume',
        'method_anchors': ['invoke-super {p0}, Landroidx/fragment/app/FragmentActivity;->onResume()V', 'invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->immersionEnable()Z', 'if-eqz v0, :cond_0', 'invoke-direct {p0}, Lmiuix/provision/ProvisionBaseActivity;->isProvisionImmersionEnable()Z', 'if-eqz v0, :cond_0', 'new-instance v0, Ljava/lang/StringBuilder;', 'invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V', 'const-string v1, "onResume immersionEnable: "'],
        'type': 'method_replace',
        'search': """.method protected onResume()V
    .registers 3

    invoke-super {p0}, Landroidx/fragment/app/FragmentActivity;->onResume()V

    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->immersionEnable()Z

    move-result v0

    if-eqz v0, :cond_0

    invoke-direct {p0}, Lmiuix/provision/ProvisionBaseActivity;->isProvisionImmersionEnable()Z

    move-result v0

    if-eqz v0, :cond_0

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v1, "onResume immersionEnable: "

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->isShowNavigation()Z

    move-result v1

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    const-string v1, "OobeUtil2"

    invoke-static {v1, v0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->isShowNavigation()Z

    move-result v0

    invoke-static {p0, v0}, Lmiuix/provision/ImmersionBarUtils;->autoAdapterGestureLine(Landroid/app/Activity;Z)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onResume()V
    .registers 3

    goto :goto_8

    nop

    :goto_0
    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->immersionEnable()Z

    move-result v0

    goto :goto_10

    nop

    :goto_1
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    goto :goto_c

    nop

    :goto_2
    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->isShowNavigation()Z

    move-result v0

    goto :goto_3

    nop

    :goto_3
    invoke-static {p0, v0}, Lmiuix/provision/ImmersionBarUtils;->autoAdapterGestureLine(Landroid/app/Activity;Z)V

    :goto_4
    goto :goto_d

    nop

    :goto_5
    invoke-direct {p0}, Lmiuix/provision/ProvisionBaseActivity;->isProvisionImmersionEnable()Z

    move-result v0

    goto :goto_9

    nop

    :goto_6
    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->isShowNavigation()Z

    move-result v1

    goto :goto_1

    nop

    :goto_7
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_f

    nop

    :goto_8
    invoke-super {p0}, Landroidx/fragment/app/FragmentActivity;->onResume()V

    goto :goto_0

    nop

    :goto_9
    if-nez v0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_e

    nop

    :goto_a
    invoke-static {v1, v0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_2

    nop

    :goto_b
    const-string v1, "OobeUtil2"

    goto :goto_a

    nop

    :goto_c
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    goto :goto_b

    nop

    :goto_d
    return-void

    :goto_e
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_7

    nop

    :goto_f
    const-string v1, "onResume immersionEnable: "

    goto :goto_11

    nop

    :goto_10
    if-nez v0, :cond_1

    goto :goto_4

    :cond_1
    goto :goto_5

    nop

    :goto_11
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_provision_ProvisionBaseActivity__onSkipButtonClick',
        'method': '.method protected onSkipButtonClick()V',
        'method_name': 'onSkipButtonClick',
        'method_anchors': ['return-void'],
        'type': 'method_replace',
        'search': """.method protected onSkipButtonClick()V
    .registers 1

    return-void
.end method""",
        'replacement': """.method protected onSkipButtonClick()V
    .registers 1

    goto :goto_0

    nop

    :goto_0
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_provision_ProvisionBaseActivity__onStart',
        'method': '.method protected onStart()V',
        'method_name': 'onStart',
        'method_anchors': ['invoke-super {p0}, Landroidx/fragment/app/FragmentActivity;->onStart()V', 'iget-boolean v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mHasPreview:Z', 'if-eqz v0, :cond_0', 'invoke-static {p0}, Lmiuix/provision/OobeUtil;->androidGoOrNativeAdapt(Landroid/content/Context;)Z', 'if-eqz v0, :cond_0', 'iget-boolean v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mIsCompatibleMode:Z', 'if-nez v0, :cond_0', 'new-instance v0, Lmiuix/provision/ProvisionAnimHelper;'],
        'type': 'method_replace',
        'search': """.method protected onStart()V
    .registers 3

    invoke-super {p0}, Landroidx/fragment/app/FragmentActivity;->onStart()V

    iget-boolean v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mHasPreview:Z

    if-eqz v0, :cond_0

    invoke-static {p0}, Lmiuix/provision/OobeUtil;->androidGoOrNativeAdapt(Landroid/content/Context;)Z

    move-result v0

    if-eqz v0, :cond_0

    iget-boolean v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mIsCompatibleMode:Z

    if-nez v0, :cond_0

    new-instance v0, Lmiuix/provision/ProvisionAnimHelper;

    iget-object v1, p0, Lmiuix/provision/ProvisionBaseActivity;->mH:Landroid/os/Handler;

    invoke-direct {v0, p0, v1}, Lmiuix/provision/ProvisionAnimHelper;-><init>(Landroid/content/Context;Landroid/os/Handler;)V

    iput-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionAnimHelper:Lmiuix/provision/ProvisionAnimHelper;

    invoke-virtual {v0}, Lmiuix/provision/ProvisionAnimHelper;->registerAnimService()V

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionAnimHelper:Lmiuix/provision/ProvisionAnimHelper;

    invoke-virtual {v0, p0}, Lmiuix/provision/ProvisionAnimHelper;->setAnimListener(Lmiuix/provision/ProvisionAnimHelper$AnimListener;)V

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionAnimHelper:Lmiuix/provision/ProvisionAnimHelper;

    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->getTitleLayoutHeight()I

    move-result p0

    invoke-virtual {v0, p0}, Lmiuix/provision/ProvisionAnimHelper;->setAnimY(I)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onStart()V
    .registers 3

    goto :goto_12

    nop

    :goto_0
    if-nez v0, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_b

    nop

    :goto_1
    invoke-virtual {v0, p0}, Lmiuix/provision/ProvisionAnimHelper;->setAnimY(I)V

    :goto_2
    goto :goto_3

    nop

    :goto_3
    return-void

    :goto_4
    invoke-direct {v0, p0, v1}, Lmiuix/provision/ProvisionAnimHelper;-><init>(Landroid/content/Context;Landroid/os/Handler;)V

    goto :goto_10

    nop

    :goto_5
    iget-object v1, p0, Lmiuix/provision/ProvisionBaseActivity;->mH:Landroid/os/Handler;

    goto :goto_4

    nop

    :goto_6
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionAnimHelper:Lmiuix/provision/ProvisionAnimHelper;

    goto :goto_e

    nop

    :goto_7
    iget-boolean v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mHasPreview:Z

    goto :goto_a

    nop

    :goto_8
    new-instance v0, Lmiuix/provision/ProvisionAnimHelper;

    goto :goto_5

    nop

    :goto_9
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionAnimHelper:Lmiuix/provision/ProvisionAnimHelper;

    goto :goto_d

    nop

    :goto_a
    if-nez v0, :cond_1

    goto :goto_2

    :cond_1
    goto :goto_11

    nop

    :goto_b
    iget-boolean v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mIsCompatibleMode:Z

    goto :goto_f

    nop

    :goto_c
    invoke-virtual {v0}, Lmiuix/provision/ProvisionAnimHelper;->registerAnimService()V

    goto :goto_6

    nop

    :goto_d
    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->getTitleLayoutHeight()I

    move-result p0

    goto :goto_1

    nop

    :goto_e
    invoke-virtual {v0, p0}, Lmiuix/provision/ProvisionAnimHelper;->setAnimListener(Lmiuix/provision/ProvisionAnimHelper$AnimListener;)V

    goto :goto_9

    nop

    :goto_f
    if-eqz v0, :cond_2

    goto :goto_2

    :cond_2
    goto :goto_8

    nop

    :goto_10
    iput-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionAnimHelper:Lmiuix/provision/ProvisionAnimHelper;

    goto :goto_c

    nop

    :goto_11
    invoke-static {p0}, Lmiuix/provision/OobeUtil;->androidGoOrNativeAdapt(Landroid/content/Context;)Z

    move-result v0

    goto :goto_0

    nop

    :goto_12
    invoke-super {p0}, Landroidx/fragment/app/FragmentActivity;->onStart()V

    goto :goto_7

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_provision_ProvisionBaseActivity__setAnimationFrame',
        'method': '.method protected setAnimationFrame(I)V',
        'method_name': 'setAnimationFrame',
        'method_anchors': ['iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mLottieAnimationView:Lcom/airbnb/lottie/LottieAnimationView;', 'if-eqz p0, :cond_0', 'invoke-virtual {p0, p1}, Lcom/airbnb/lottie/LottieAnimationView;->setFrame(I)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected setAnimationFrame(I)V
    .registers 2

    iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mLottieAnimationView:Lcom/airbnb/lottie/LottieAnimationView;

    if-eqz p0, :cond_0

    invoke-virtual {p0, p1}, Lcom/airbnb/lottie/LottieAnimationView;->setFrame(I)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected setAnimationFrame(I)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mLottieAnimationView:Lcom/airbnb/lottie/LottieAnimationView;

    goto :goto_1

    nop

    :goto_1
    if-nez p0, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_2

    nop

    :goto_2
    invoke-virtual {p0, p1}, Lcom/airbnb/lottie/LottieAnimationView;->setFrame(I)V

    :goto_3
    goto :goto_4

    nop

    :goto_4
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_provision_ProvisionBaseActivity__setAnimationProgress',
        'method': '.method protected setAnimationProgress(F)V',
        'method_name': 'setAnimationProgress',
        'method_anchors': ['iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mLottieAnimationView:Lcom/airbnb/lottie/LottieAnimationView;', 'if-eqz p0, :cond_0', 'invoke-virtual {p0, p1}, Lcom/airbnb/lottie/LottieAnimationView;->setProgress(F)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected setAnimationProgress(F)V
    .registers 2

    iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mLottieAnimationView:Lcom/airbnb/lottie/LottieAnimationView;

    if-eqz p0, :cond_0

    invoke-virtual {p0, p1}, Lcom/airbnb/lottie/LottieAnimationView;->setProgress(F)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected setAnimationProgress(F)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mLottieAnimationView:Lcom/airbnb/lottie/LottieAnimationView;

    goto :goto_4

    nop

    :goto_1
    invoke-virtual {p0, p1}, Lcom/airbnb/lottie/LottieAnimationView;->setProgress(F)V

    :goto_2
    goto :goto_3

    nop

    :goto_3
    return-void

    :goto_4
    if-nez p0, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_provision_ProvisionBaseActivity__setAnimationView',
        'method': '.method protected setAnimationView(I)V',
        'method_name': 'setAnimationView',
        'method_anchors': ['iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mLottieAnimationView:Lcom/airbnb/lottie/LottieAnimationView;', 'if-eqz v0, :cond_1', 'invoke-virtual {v0, p1}, Lcom/airbnb/lottie/LottieAnimationView;->setAnimation(I)V', 'invoke-static {}, Lmiuix/provision/OobeUtil;->isMiuiLite()Z', 'if-eqz p1, :cond_0', 'iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mLottieAnimationView:Lcom/airbnb/lottie/LottieAnimationView;', 'invoke-virtual {p0, p1}, Lcom/airbnb/lottie/LottieAnimationView;->setProgress(F)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected setAnimationView(I)V
    .registers 3

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mLottieAnimationView:Lcom/airbnb/lottie/LottieAnimationView;

    if-eqz v0, :cond_1

    invoke-virtual {v0, p1}, Lcom/airbnb/lottie/LottieAnimationView;->setAnimation(I)V

    invoke-static {}, Lmiuix/provision/OobeUtil;->isMiuiLite()Z

    move-result p1

    if-eqz p1, :cond_0

    iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mLottieAnimationView:Lcom/airbnb/lottie/LottieAnimationView;

    const/high16 p1, 0x3f800000

    invoke-virtual {p0, p1}, Lcom/airbnb/lottie/LottieAnimationView;->setProgress(F)V

    return-void

    :cond_0
    iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mLottieAnimationView:Lcom/airbnb/lottie/LottieAnimationView;

    invoke-virtual {p0}, Lcom/airbnb/lottie/LottieAnimationView;->playAnimation()V

    :cond_1
    return-void
.end method""",
        'replacement': """.method protected setAnimationView(I)V
    .registers 3

    goto :goto_d

    nop

    :goto_0
    if-nez v0, :cond_0

    goto :goto_a

    :cond_0
    goto :goto_3

    nop

    :goto_1
    invoke-virtual {p0, p1}, Lcom/airbnb/lottie/LottieAnimationView;->setProgress(F)V

    goto :goto_7

    nop

    :goto_2
    invoke-static {}, Lmiuix/provision/OobeUtil;->isMiuiLite()Z

    move-result p1

    goto :goto_b

    nop

    :goto_3
    invoke-virtual {v0, p1}, Lcom/airbnb/lottie/LottieAnimationView;->setAnimation(I)V

    goto :goto_2

    nop

    :goto_4
    return-void

    :goto_5
    const/high16 p1, 0x3f800000

    goto :goto_1

    nop

    :goto_6
    iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mLottieAnimationView:Lcom/airbnb/lottie/LottieAnimationView;

    goto :goto_5

    nop

    :goto_7
    return-void

    :goto_8
    goto :goto_c

    nop

    :goto_9
    invoke-virtual {p0}, Lcom/airbnb/lottie/LottieAnimationView;->playAnimation()V

    :goto_a
    goto :goto_4

    nop

    :goto_b
    if-nez p1, :cond_1

    goto :goto_8

    :cond_1
    goto :goto_6

    nop

    :goto_c
    iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mLottieAnimationView:Lcom/airbnb/lottie/LottieAnimationView;

    goto :goto_9

    nop

    :goto_d
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mLottieAnimationView:Lcom/airbnb/lottie/LottieAnimationView;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_provision_ProvisionBaseActivity__setAnimationView',
        'method': '.method protected setAnimationView(Ljava/lang/String;)V',
        'method_name': 'setAnimationView',
        'method_anchors': ['iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mLottieAnimationView:Lcom/airbnb/lottie/LottieAnimationView;', 'if-eqz v0, :cond_1', 'invoke-virtual {v0, p1}, Lcom/airbnb/lottie/LottieAnimationView;->setAnimation(Ljava/lang/String;)V', 'invoke-static {}, Lmiuix/provision/OobeUtil;->isMiuiLite()Z', 'if-eqz p1, :cond_0', 'iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mLottieAnimationView:Lcom/airbnb/lottie/LottieAnimationView;', 'invoke-virtual {p0, p1}, Lcom/airbnb/lottie/LottieAnimationView;->setProgress(F)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected setAnimationView(Ljava/lang/String;)V
    .registers 3

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mLottieAnimationView:Lcom/airbnb/lottie/LottieAnimationView;

    if-eqz v0, :cond_1

    invoke-virtual {v0, p1}, Lcom/airbnb/lottie/LottieAnimationView;->setAnimation(Ljava/lang/String;)V

    invoke-static {}, Lmiuix/provision/OobeUtil;->isMiuiLite()Z

    move-result p1

    if-eqz p1, :cond_0

    iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mLottieAnimationView:Lcom/airbnb/lottie/LottieAnimationView;

    const/high16 p1, 0x3f800000

    invoke-virtual {p0, p1}, Lcom/airbnb/lottie/LottieAnimationView;->setProgress(F)V

    return-void

    :cond_0
    iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mLottieAnimationView:Lcom/airbnb/lottie/LottieAnimationView;

    invoke-virtual {p0}, Lcom/airbnb/lottie/LottieAnimationView;->playAnimation()V

    :cond_1
    return-void
.end method""",
        'replacement': """.method protected setAnimationView(Ljava/lang/String;)V
    .registers 3

    goto :goto_7

    nop

    :goto_0
    invoke-static {}, Lmiuix/provision/OobeUtil;->isMiuiLite()Z

    move-result p1

    goto :goto_2

    nop

    :goto_1
    return-void

    :goto_2
    if-nez p1, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_3

    nop

    :goto_3
    iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mLottieAnimationView:Lcom/airbnb/lottie/LottieAnimationView;

    goto :goto_c

    nop

    :goto_4
    return-void

    :goto_5
    goto :goto_8

    nop

    :goto_6
    if-nez v0, :cond_1

    goto :goto_b

    :cond_1
    goto :goto_9

    nop

    :goto_7
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mLottieAnimationView:Lcom/airbnb/lottie/LottieAnimationView;

    goto :goto_6

    nop

    :goto_8
    iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mLottieAnimationView:Lcom/airbnb/lottie/LottieAnimationView;

    goto :goto_a

    nop

    :goto_9
    invoke-virtual {v0, p1}, Lcom/airbnb/lottie/LottieAnimationView;->setAnimation(Ljava/lang/String;)V

    goto :goto_0

    nop

    :goto_a
    invoke-virtual {p0}, Lcom/airbnb/lottie/LottieAnimationView;->playAnimation()V

    :goto_b
    goto :goto_1

    nop

    :goto_c
    const/high16 p1, 0x3f800000

    goto :goto_d

    nop

    :goto_d
    invoke-virtual {p0, p1}, Lcom/airbnb/lottie/LottieAnimationView;->setProgress(F)V

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_provision_ProvisionBaseActivity__setBackButtonContentDescription',
        'method': '.method protected setBackButtonContentDescription()V',
        'method_name': 'setBackButtonContentDescription',
        'method_anchors': ['iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mNewBackBtn:Landroid/widget/ImageView;', 'if-eqz v0, :cond_0', 'sget v1, Lmiuix/provision/R$string;->provision_back:I', 'invoke-virtual {p0, v1}, Landroid/app/Activity;->getString(I)Ljava/lang/String;', 'invoke-virtual {v0, p0}, Landroid/widget/ImageView;->setContentDescription(Ljava/lang/CharSequence;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected setBackButtonContentDescription()V
    .registers 3

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mNewBackBtn:Landroid/widget/ImageView;

    if-eqz v0, :cond_0

    sget v1, Lmiuix/provision/R$string;->provision_back:I

    invoke-virtual {p0, v1}, Landroid/app/Activity;->getString(I)Ljava/lang/String;

    move-result-object p0

    invoke-virtual {v0, p0}, Landroid/widget/ImageView;->setContentDescription(Ljava/lang/CharSequence;)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected setBackButtonContentDescription()V
    .registers 3

    goto :goto_3

    nop

    :goto_0
    sget v1, Lmiuix/provision/R$string;->provision_back:I

    goto :goto_2

    nop

    :goto_1
    return-void

    :goto_2
    invoke-virtual {p0, v1}, Landroid/app/Activity;->getString(I)Ljava/lang/String;

    move-result-object p0

    goto :goto_4

    nop

    :goto_3
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mNewBackBtn:Landroid/widget/ImageView;

    goto :goto_6

    nop

    :goto_4
    invoke-virtual {v0, p0}, Landroid/widget/ImageView;->setContentDescription(Ljava/lang/CharSequence;)V

    :goto_5
    goto :goto_1

    nop

    :goto_6
    if-nez v0, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_provision_ProvisionBaseActivity__setDefaultPadding',
        'method': '.method protected setDefaultPadding()V',
        'method_name': 'setDefaultPadding',
        'method_anchors': ['iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionContainer:Landroid/view/View;', 'if-nez v0, :cond_0', 'invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->isNeedDefaultPadding()Z', 'if-eqz v0, :cond_1', 'return-void', 'iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionContainer:Landroid/view/View;', 'invoke-virtual {p0, v0, v0, v0, v0}, Landroid/view/View;->setPadding(IIII)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected setDefaultPadding()V
    .registers 2

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionContainer:Landroid/view/View;

    if-nez v0, :cond_0

    goto :goto_0

    :cond_0
    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->isNeedDefaultPadding()Z

    move-result v0

    if-eqz v0, :cond_1

    :goto_0
    return-void

    :cond_1
    iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionContainer:Landroid/view/View;

    const/4 v0, 0x0

    invoke-virtual {p0, v0, v0, v0, v0}, Landroid/view/View;->setPadding(IIII)V

    return-void
.end method""",
        'replacement': """.method protected setDefaultPadding()V
    .registers 2

    goto :goto_6

    nop

    :goto_0
    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->isNeedDefaultPadding()Z

    move-result v0

    goto :goto_b

    nop

    :goto_1
    return-void

    :goto_2
    goto :goto_5

    nop

    :goto_3
    if-eqz v0, :cond_0

    goto :goto_8

    :cond_0
    goto :goto_7

    nop

    :goto_4
    return-void

    :goto_5
    iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionContainer:Landroid/view/View;

    goto :goto_a

    nop

    :goto_6
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionContainer:Landroid/view/View;

    goto :goto_3

    nop

    :goto_7
    goto :goto_c

    :goto_8
    goto :goto_0

    nop

    :goto_9
    invoke-virtual {p0, v0, v0, v0, v0}, Landroid/view/View;->setPadding(IIII)V

    goto :goto_4

    nop

    :goto_a
    const/4 v0, 0x0

    goto :goto_9

    nop

    :goto_b
    if-nez v0, :cond_1

    goto :goto_2

    :cond_1
    :goto_c
    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_provision_ProvisionBaseActivity__setExtraPaddingBottom',
        'method': '.method protected setExtraPaddingBottom(Landroid/widget/Button;)V',
        'method_name': 'setExtraPaddingBottom',
        'method_anchors': ['if-nez p1, :cond_0', 'return-void', 'invoke-virtual {p1}, Landroid/widget/Button;->getParent()Landroid/view/ViewParent;', 'check-cast p1, Landroid/widget/LinearLayout;', 'invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;', 'sget v1, Lmiuix/provision/R$dimen;->group_buttons_layout_extra_padding_bottom:I', 'invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I', 'sget-boolean v1, Lmiui/os/Build;->IS_TABLET:Z'],
        'type': 'method_replace',
        'search': """.method protected setExtraPaddingBottom(Landroid/widget/Button;)V
    .registers 6

    if-nez p1, :cond_0

    return-void

    :cond_0
    invoke-virtual {p1}, Landroid/widget/Button;->getParent()Landroid/view/ViewParent;

    move-result-object p1

    check-cast p1, Landroid/widget/LinearLayout;

    invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    sget v1, Lmiuix/provision/R$dimen;->group_buttons_layout_extra_padding_bottom:I

    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I

    move-result v0

    sget-boolean v1, Lmiui/os/Build;->IS_TABLET:Z

    if-eqz v1, :cond_2

    invoke-static {p0}, Lmiuix/provision/OobeUtil;->isLandOrientation(Landroid/content/Context;)Z

    move-result v0

    if-eqz v0, :cond_1

    invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;

    move-result-object p0

    sget v0, Lmiuix/provision/R$dimen;->group_buttons_layout_extra_padding_bottom_pad_land:I

    invoke-virtual {p0, v0}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I

    move-result p0

    :goto_0
    move v0, p0

    goto :goto_1

    :cond_1
    invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;

    move-result-object p0

    sget v0, Lmiuix/provision/R$dimen;->group_buttons_layout_extra_padding_bottom_pad_port:I

    invoke-virtual {p0, v0}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I

    move-result p0

    goto :goto_0

    :cond_2
    :goto_1
    invoke-virtual {p1}, Landroid/widget/LinearLayout;->getPaddingLeft()I

    move-result p0

    invoke-virtual {p1}, Landroid/widget/LinearLayout;->getPaddingTop()I

    move-result v1

    invoke-virtual {p1}, Landroid/widget/LinearLayout;->getPaddingRight()I

    move-result v2

    invoke-virtual {p1}, Landroid/widget/LinearLayout;->getPaddingBottom()I

    move-result v3

    add-int/2addr v3, v0

    invoke-virtual {p1, p0, v1, v2, v3}, Landroid/widget/LinearLayout;->setPadding(IIII)V

    return-void
.end method""",
        'replacement': """.method protected setExtraPaddingBottom(Landroid/widget/Button;)V
    .registers 6

    goto :goto_b

    nop

    :goto_0
    invoke-virtual {p1}, Landroid/widget/LinearLayout;->getPaddingLeft()I

    move-result p0

    goto :goto_16

    nop

    :goto_1
    check-cast p1, Landroid/widget/LinearLayout;

    goto :goto_17

    nop

    :goto_2
    sget v1, Lmiuix/provision/R$dimen;->group_buttons_layout_extra_padding_bottom:I

    goto :goto_4

    nop

    :goto_3
    invoke-static {p0}, Lmiuix/provision/OobeUtil;->isLandOrientation(Landroid/content/Context;)Z

    move-result v0

    goto :goto_12

    nop

    :goto_4
    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I

    move-result v0

    goto :goto_6

    nop

    :goto_5
    invoke-virtual {p0, v0}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I

    move-result p0

    goto :goto_18

    nop

    :goto_6
    sget-boolean v1, Lmiui/os/Build;->IS_TABLET:Z

    goto :goto_8

    nop

    :goto_7
    invoke-virtual {p1}, Landroid/widget/LinearLayout;->getPaddingRight()I

    move-result v2

    goto :goto_1d

    nop

    :goto_8
    if-nez v1, :cond_0

    goto :goto_19

    :cond_0
    goto :goto_3

    nop

    :goto_9
    add-int/2addr v3, v0

    goto :goto_a

    nop

    :goto_a
    invoke-virtual {p1, p0, v1, v2, v3}, Landroid/widget/LinearLayout;->setPadding(IIII)V

    goto :goto_c

    nop

    :goto_b
    if-eqz p1, :cond_1

    goto :goto_10

    :cond_1
    goto :goto_f

    nop

    :goto_c
    return-void

    :goto_d
    invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;

    move-result-object p0

    goto :goto_1e

    nop

    :goto_e
    invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;

    move-result-object p0

    goto :goto_15

    nop

    :goto_f
    return-void

    :goto_10
    goto :goto_11

    nop

    :goto_11
    invoke-virtual {p1}, Landroid/widget/Button;->getParent()Landroid/view/ViewParent;

    move-result-object p1

    goto :goto_1

    nop

    :goto_12
    if-nez v0, :cond_2

    goto :goto_14

    :cond_2
    goto :goto_d

    nop

    :goto_13
    goto :goto_19

    :goto_14
    goto :goto_e

    nop

    :goto_15
    sget v0, Lmiuix/provision/R$dimen;->group_buttons_layout_extra_padding_bottom_pad_port:I

    goto :goto_5

    nop

    :goto_16
    invoke-virtual {p1}, Landroid/widget/LinearLayout;->getPaddingTop()I

    move-result v1

    goto :goto_7

    nop

    :goto_17
    invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    goto :goto_2

    nop

    :goto_18
    goto :goto_1c

    :goto_19
    goto :goto_0

    nop

    :goto_1a
    move v0, p0

    goto :goto_13

    nop

    :goto_1b
    invoke-virtual {p0, v0}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I

    move-result p0

    :goto_1c
    goto :goto_1a

    nop

    :goto_1d
    invoke-virtual {p1}, Landroid/widget/LinearLayout;->getPaddingBottom()I

    move-result v3

    goto :goto_9

    nop

    :goto_1e
    sget v0, Lmiuix/provision/R$dimen;->group_buttons_layout_extra_padding_bottom_pad_land:I

    goto :goto_1b

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
