TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/app/ActionBarDelegateImpl.smali'
CLASS_FALLBACK_NAMES = ['ActionBarDelegateImpl.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Lmiuix/appcompat/app/ActionBarDelegate;', '.implements Lmiuix/container/ExtraPaddingObserver;', '.implements Lmiuix/appcompat/internal/view/menu/MenuPresenter$Callback;', '.implements Lmiuix/appcompat/internal/view/menu/MenuBuilder$Callback;']

PATCHES = [
    {
        'id': 'miuix_appcompat_app_ActionBarDelegateImpl__createMenu',
        'method': '.method protected createMenu()Lmiuix/appcompat/internal/view/menu/MenuBuilder;',
        'method_name': 'createMenu',
        'method_anchors': ['new-instance v0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;', 'invoke-virtual {p0}, Lmiuix/appcompat/app/ActionBarDelegateImpl;->getActionBarThemedContext()Landroid/content/Context;', 'invoke-direct {v0, v1}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;-><init>(Landroid/content/Context;)V', 'invoke-virtual {v0, p0}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->setCallback(Lmiuix/appcompat/internal/view/menu/MenuBuilder$Callback;)V', 'return-object v0'],
        'type': 'method_replace',
        'search': """.method protected createMenu()Lmiuix/appcompat/internal/view/menu/MenuBuilder;
    .registers 3

    new-instance v0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    invoke-virtual {p0}, Lmiuix/appcompat/app/ActionBarDelegateImpl;->getActionBarThemedContext()Landroid/content/Context;

    move-result-object v1

    invoke-direct {v0, v1}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;-><init>(Landroid/content/Context;)V

    invoke-virtual {v0, p0}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->setCallback(Lmiuix/appcompat/internal/view/menu/MenuBuilder$Callback;)V

    return-object v0
.end method""",
        'replacement': """.method protected createMenu()Lmiuix/appcompat/internal/view/menu/MenuBuilder;
    .registers 3

    goto :goto_4

    nop

    :goto_0
    return-object v0

    :goto_1
    invoke-virtual {p0}, Lmiuix/appcompat/app/ActionBarDelegateImpl;->getActionBarThemedContext()Landroid/content/Context;

    move-result-object v1

    goto :goto_3

    nop

    :goto_2
    invoke-virtual {v0, p0}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->setCallback(Lmiuix/appcompat/internal/view/menu/MenuBuilder$Callback;)V

    goto :goto_0

    nop

    :goto_3
    invoke-direct {v0, v1}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;-><init>(Landroid/content/Context;)V

    goto :goto_2

    nop

    :goto_4
    new-instance v0, Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_ActionBarDelegateImpl__getActionBarThemedContext',
        'method': '.method protected final getActionBarThemedContext()Landroid/content/Context;',
        'method_name': 'getActionBarThemedContext',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActivity:Lmiuix/appcompat/app/AppCompatActivity;', 'invoke-virtual {p0}, Lmiuix/appcompat/app/ActionBarDelegateImpl;->getActionBar()Lmiuix/appcompat/app/ActionBar;', 'if-eqz p0, :cond_0', 'invoke-virtual {p0}, Landroidx/appcompat/app/ActionBar;->getThemedContext()Landroid/content/Context;', 'return-object p0', 'return-object v0'],
        'type': 'method_replace',
        'search': """.method protected final getActionBarThemedContext()Landroid/content/Context;
    .registers 2

    iget-object v0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActivity:Lmiuix/appcompat/app/AppCompatActivity;

    invoke-virtual {p0}, Lmiuix/appcompat/app/ActionBarDelegateImpl;->getActionBar()Lmiuix/appcompat/app/ActionBar;

    move-result-object p0

    if-eqz p0, :cond_0

    invoke-virtual {p0}, Landroidx/appcompat/app/ActionBar;->getThemedContext()Landroid/content/Context;

    move-result-object p0

    return-object p0

    :cond_0
    return-object v0
.end method""",
        'replacement': """.method protected final getActionBarThemedContext()Landroid/content/Context;
    .registers 2

    goto :goto_6

    nop

    :goto_0
    invoke-virtual {p0}, Lmiuix/appcompat/app/ActionBarDelegateImpl;->getActionBar()Lmiuix/appcompat/app/ActionBar;

    move-result-object p0

    goto :goto_5

    nop

    :goto_1
    return-object p0

    :goto_2
    goto :goto_4

    nop

    :goto_3
    invoke-virtual {p0}, Landroidx/appcompat/app/ActionBar;->getThemedContext()Landroid/content/Context;

    move-result-object p0

    goto :goto_1

    nop

    :goto_4
    return-object v0

    :goto_5
    if-nez p0, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_3

    nop

    :goto_6
    iget-object v0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActivity:Lmiuix/appcompat/app/AppCompatActivity;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_ActionBarDelegateImpl__getUiOptionsFromMetadata',
        'method': '.method protected final getUiOptionsFromMetadata()Ljava/lang/String;',
        'method_name': 'getUiOptionsFromMetadata',
        'method_anchors': ['iget-object v1, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActivity:Lmiuix/appcompat/app/AppCompatActivity;', 'invoke-virtual {v1}, Landroid/app/Activity;->getPackageManager()Landroid/content/pm/PackageManager;', 'iget-object v2, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActivity:Lmiuix/appcompat/app/AppCompatActivity;', 'invoke-virtual {v2}, Landroid/app/Activity;->getComponentName()Landroid/content/ComponentName;', 'invoke-virtual {v1, v2, v3}, Landroid/content/pm/PackageManager;->getActivityInfo(Landroid/content/ComponentName;I)Landroid/content/pm/ActivityInfo;', 'iget-object v1, v1, Landroid/content/pm/ActivityInfo;->metaData:Landroid/os/Bundle;', 'if-eqz v1, :cond_0', 'const-string v2, "android.support.UI_OPTIONS"'],
        'type': 'method_replace',
        'search': """.method protected final getUiOptionsFromMetadata()Ljava/lang/String;
    .registers 5

    const/4 v0, 0x0

    :try_start_0
    iget-object v1, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActivity:Lmiuix/appcompat/app/AppCompatActivity;

    invoke-virtual {v1}, Landroid/app/Activity;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object v1

    iget-object v2, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActivity:Lmiuix/appcompat/app/AppCompatActivity;

    invoke-virtual {v2}, Landroid/app/Activity;->getComponentName()Landroid/content/ComponentName;

    move-result-object v2

    const/16 v3, 0x80

    invoke-virtual {v1, v2, v3}, Landroid/content/pm/PackageManager;->getActivityInfo(Landroid/content/ComponentName;I)Landroid/content/pm/ActivityInfo;

    move-result-object v1

    iget-object v1, v1, Landroid/content/pm/ActivityInfo;->metaData:Landroid/os/Bundle;

    if-eqz v1, :cond_0

    const-string v2, "android.support.UI_OPTIONS"

    invoke-virtual {v1, v2}, Landroid/os/Bundle;->getString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object p0
    :try_end_0
    .catch Landroid/content/pm/PackageManager$NameNotFoundException; {:try_start_0 .. :try_end_0} :catch_0

    return-object p0

    :cond_0
    return-object v0

    :catch_0
    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "getUiOptionsFromMetadata: Activity \'"

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object p0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActivity:Lmiuix/appcompat/app/AppCompatActivity;

    invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object p0

    invoke-virtual {p0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object p0

    invoke-virtual {v1, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string p0, "\' not in manifest"

    invoke-virtual {v1, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    const-string v1, "ActionBarDelegate"

    invoke-static {v1, p0}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    return-object v0
.end method""",
        'replacement': """.method protected final getUiOptionsFromMetadata()Ljava/lang/String;
    .registers 5

    goto :goto_5

    nop

    :goto_0
    return-object v0

    :catch_0
    goto :goto_4

    nop

    :goto_1
    const-string v2, "getUiOptionsFromMetadata: Activity \'"

    goto :goto_c

    nop

    :goto_2
    invoke-static {v1, p0}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_3

    nop

    :goto_3
    return-object v0

    :goto_4
    new-instance v1, Ljava/lang/StringBuilder;

    goto :goto_6

    nop

    :goto_5
    const/4 v0, 0x0

    :try_start_0
    iget-object v1, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActivity:Lmiuix/appcompat/app/AppCompatActivity;

    invoke-virtual {v1}, Landroid/app/Activity;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object v1

    iget-object v2, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActivity:Lmiuix/appcompat/app/AppCompatActivity;

    invoke-virtual {v2}, Landroid/app/Activity;->getComponentName()Landroid/content/ComponentName;

    move-result-object v2

    const/16 v3, 0x80

    invoke-virtual {v1, v2, v3}, Landroid/content/pm/PackageManager;->getActivityInfo(Landroid/content/ComponentName;I)Landroid/content/pm/ActivityInfo;

    move-result-object v1

    iget-object v1, v1, Landroid/content/pm/ActivityInfo;->metaData:Landroid/os/Bundle;

    if-eqz v1, :cond_0

    const-string v2, "android.support.UI_OPTIONS"

    invoke-virtual {v1, v2}, Landroid/os/Bundle;->getString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object p0
    :try_end_0
    .catch Landroid/content/pm/PackageManager$NameNotFoundException; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_f

    nop

    :goto_6
    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_1

    nop

    :goto_7
    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    goto :goto_a

    nop

    :goto_8
    invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object p0

    goto :goto_e

    nop

    :goto_9
    iget-object p0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActivity:Lmiuix/appcompat/app/AppCompatActivity;

    goto :goto_8

    nop

    :goto_a
    const-string v1, "ActionBarDelegate"

    goto :goto_2

    nop

    :goto_b
    const-string p0, "\' not in manifest"

    goto :goto_d

    nop

    :goto_c
    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_9

    nop

    :goto_d
    invoke-virtual {v1, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_7

    nop

    :goto_e
    invoke-virtual {p0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object p0

    goto :goto_10

    nop

    :goto_f
    return-object p0

    :cond_0
    goto :goto_0

    nop

    :goto_10
    invoke-virtual {v1, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_b

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_ActionBarDelegateImpl__initExtraPaddingPolicy',
        'method': '.method protected initExtraPaddingPolicy()V',
        'method_name': 'initExtraPaddingPolicy',
        'method_anchors': ['iget v0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mDeviceType:I', 'sget v1, Lmiuix/theme/token/ContainerToken;->PADDING_BASE_DP:I', 'sget v2, Lmiuix/theme/token/ContainerToken;->PADDING_HORIZONTAL_COMMON:I', 'invoke-static {v0, v1, v2}, Lmiuix/container/ExtraPaddingPolicy$Builder;->createDefault(III)Lmiuix/container/ExtraPaddingPolicy;', 'iput-object v0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mExtraPaddingPolicy:Lmiuix/container/ExtraPaddingPolicy;', 'if-eqz v0, :cond_0', 'iget-boolean p0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mExtraPaddingEnable:Z', 'invoke-virtual {v0, p0}, Lmiuix/container/ExtraPaddingPolicy;->setEnable(Z)V'],
        'type': 'method_replace',
        'search': """.method protected initExtraPaddingPolicy()V
    .registers 4

    iget v0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mDeviceType:I

    sget v1, Lmiuix/theme/token/ContainerToken;->PADDING_BASE_DP:I

    sget v2, Lmiuix/theme/token/ContainerToken;->PADDING_HORIZONTAL_COMMON:I

    invoke-static {v0, v1, v2}, Lmiuix/container/ExtraPaddingPolicy$Builder;->createDefault(III)Lmiuix/container/ExtraPaddingPolicy;

    move-result-object v0

    iput-object v0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mExtraPaddingPolicy:Lmiuix/container/ExtraPaddingPolicy;

    if-eqz v0, :cond_0

    iget-boolean p0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mExtraPaddingEnable:Z

    invoke-virtual {v0, p0}, Lmiuix/container/ExtraPaddingPolicy;->setEnable(Z)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected initExtraPaddingPolicy()V
    .registers 4

    goto :goto_1

    nop

    :goto_0
    invoke-static {v0, v1, v2}, Lmiuix/container/ExtraPaddingPolicy$Builder;->createDefault(III)Lmiuix/container/ExtraPaddingPolicy;

    move-result-object v0

    goto :goto_2

    nop

    :goto_1
    iget v0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mDeviceType:I

    goto :goto_8

    nop

    :goto_2
    iput-object v0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mExtraPaddingPolicy:Lmiuix/container/ExtraPaddingPolicy;

    goto :goto_7

    nop

    :goto_3
    invoke-virtual {v0, p0}, Lmiuix/container/ExtraPaddingPolicy;->setEnable(Z)V

    :goto_4
    goto :goto_6

    nop

    :goto_5
    sget v2, Lmiuix/theme/token/ContainerToken;->PADDING_HORIZONTAL_COMMON:I

    goto :goto_0

    nop

    :goto_6
    return-void

    :goto_7
    if-nez v0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_9

    nop

    :goto_8
    sget v1, Lmiuix/theme/token/ContainerToken;->PADDING_BASE_DP:I

    goto :goto_5

    nop

    :goto_9
    iget-boolean p0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mExtraPaddingEnable:Z

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_ActionBarDelegateImpl__reopenMenu',
        'method': '.method protected reopenMenu(Lmiuix/appcompat/internal/view/menu/MenuBuilder;Z)V',
        'method_name': 'reopenMenu',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;', 'if-eqz v0, :cond_3', 'invoke-virtual {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->isOverflowReserved()Z', 'if-eqz v0, :cond_3', 'iget-object p1, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;', 'invoke-virtual {p1}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->isOverflowMenuShowing()Z', 'if-eqz p1, :cond_1', 'if-nez p2, :cond_0'],
        'type': 'method_replace',
        'search': """.method protected reopenMenu(Lmiuix/appcompat/internal/view/menu/MenuBuilder;Z)V
    .registers 4

    iget-object v0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    if-eqz v0, :cond_3

    invoke-virtual {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->isOverflowReserved()Z

    move-result v0

    if-eqz v0, :cond_3

    iget-object p1, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    invoke-virtual {p1}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->isOverflowMenuShowing()Z

    move-result p1

    if-eqz p1, :cond_1

    if-nez p2, :cond_0

    goto :goto_0

    :cond_0
    iget-object p0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->hideOverflowMenu()Z

    return-void

    :cond_1
    :goto_0
    iget-object p1, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    invoke-virtual {p1}, Landroid/view/ViewGroup;->getVisibility()I

    move-result p1

    if-nez p1, :cond_2

    iget-object p0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->showOverflowMenu()Z

    :cond_2
    return-void

    :cond_3
    invoke-virtual {p1}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->close()V

    return-void
.end method""",
        'replacement': """.method protected reopenMenu(Lmiuix/appcompat/internal/view/menu/MenuBuilder;Z)V
    .registers 4

    goto :goto_17

    nop

    :goto_0
    return-void

    :goto_1
    return-void

    :goto_2
    goto :goto_b

    nop

    :goto_3
    return-void

    :goto_4
    goto :goto_f

    nop

    :goto_5
    iget-object p0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_13

    nop

    :goto_6
    if-eqz p1, :cond_0

    goto :goto_14

    :cond_0
    goto :goto_5

    nop

    :goto_7
    if-nez v0, :cond_1

    goto :goto_2

    :cond_1
    goto :goto_c

    nop

    :goto_8
    if-nez v0, :cond_2

    goto :goto_2

    :cond_2
    goto :goto_11

    nop

    :goto_9
    if-eqz p2, :cond_3

    goto :goto_e

    :cond_3
    goto :goto_d

    nop

    :goto_a
    invoke-virtual {p1}, Landroid/view/ViewGroup;->getVisibility()I

    move-result p1

    goto :goto_6

    nop

    :goto_b
    invoke-virtual {p1}, Lmiuix/appcompat/internal/view/menu/MenuBuilder;->close()V

    goto :goto_0

    nop

    :goto_c
    invoke-virtual {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->isOverflowReserved()Z

    move-result v0

    goto :goto_8

    nop

    :goto_d
    goto :goto_4

    :goto_e
    goto :goto_15

    nop

    :goto_f
    iget-object p1, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_a

    nop

    :goto_10
    invoke-virtual {p1}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->isOverflowMenuShowing()Z

    move-result p1

    goto :goto_12

    nop

    :goto_11
    iget-object p1, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_10

    nop

    :goto_12
    if-nez p1, :cond_4

    goto :goto_4

    :cond_4
    goto :goto_9

    nop

    :goto_13
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->showOverflowMenu()Z

    :goto_14
    goto :goto_1

    nop

    :goto_15
    iget-object p0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_16

    nop

    :goto_16
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->hideOverflowMenu()Z

    goto :goto_3

    nop

    :goto_17
    iget-object v0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_7

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_ActionBarDelegateImpl__setMenu',
        'method': '.method protected setMenu(Lmiuix/appcompat/internal/view/menu/MenuBuilder;)V',
        'method_name': 'setMenu',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;', 'if-ne p1, v0, :cond_0', 'iput-object p1, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;', 'iget-object v0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;', 'if-eqz v0, :cond_1', 'invoke-virtual {v0, p1, p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->setMenu(Landroid/view/Menu;Lmiuix/appcompat/internal/view/menu/MenuPresenter$Callback;)V', 'iget-object p1, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;', 'invoke-virtual {p1}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->isEndActionMenuEnable()Z'],
        'type': 'method_replace',
        'search': """.method protected setMenu(Lmiuix/appcompat/internal/view/menu/MenuBuilder;)V
    .registers 5

    iget-object v0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    if-ne p1, v0, :cond_0

    goto :goto_0

    :cond_0
    iput-object p1, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    iget-object v0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    if-eqz v0, :cond_1

    invoke-virtual {v0, p1, p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->setMenu(Landroid/view/Menu;Lmiuix/appcompat/internal/view/menu/MenuPresenter$Callback;)V

    iget-object p1, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    invoke-virtual {p1}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->isEndActionMenuEnable()Z

    move-result p1

    if-eqz p1, :cond_1

    iget-object p1, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    iget-object v0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    invoke-virtual {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->getEndMenu()Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    move-result-object v0

    const/4 v1, 0x0

    const/4 v2, 0x0

    invoke-interface {p0, v1, v2, p1, v0}, Lmiuix/appcompat/app/ActionBarDelegate;->onPanelViewAdded(ILandroid/view/View;Landroid/view/Menu;Landroid/view/Menu;)V

    :cond_1
    :goto_0
    return-void
.end method""",
        'replacement': """.method protected setMenu(Lmiuix/appcompat/internal/view/menu/MenuBuilder;)V
    .registers 5

    goto :goto_2

    nop

    :goto_0
    if-nez v0, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_8

    nop

    :goto_1
    iget-object p1, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    goto :goto_10

    nop

    :goto_2
    iget-object v0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    goto :goto_a

    nop

    :goto_3
    iput-object p1, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mMenu:Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    goto :goto_12

    nop

    :goto_4
    invoke-interface {p0, v1, v2, p1, v0}, Lmiuix/appcompat/app/ActionBarDelegate;->onPanelViewAdded(ILandroid/view/View;Landroid/view/Menu;Landroid/view/Menu;)V

    :goto_5
    goto :goto_6

    nop

    :goto_6
    return-void

    :goto_7
    invoke-virtual {v0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->getEndMenu()Lmiuix/appcompat/internal/view/menu/MenuBuilder;

    move-result-object v0

    goto :goto_b

    nop

    :goto_8
    invoke-virtual {v0, p1, p0}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->setMenu(Landroid/view/Menu;Lmiuix/appcompat/internal/view/menu/MenuPresenter$Callback;)V

    goto :goto_c

    nop

    :goto_9
    if-nez p1, :cond_1

    goto :goto_5

    :cond_1
    goto :goto_1

    nop

    :goto_a
    if-eq p1, v0, :cond_2

    goto :goto_e

    :cond_2
    goto :goto_d

    nop

    :goto_b
    const/4 v1, 0x0

    goto :goto_f

    nop

    :goto_c
    iget-object p1, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_11

    nop

    :goto_d
    goto :goto_5

    :goto_e
    goto :goto_3

    nop

    :goto_f
    const/4 v2, 0x0

    goto :goto_4

    nop

    :goto_10
    iget-object v0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_7

    nop

    :goto_11
    invoke-virtual {p1}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->isEndActionMenuEnable()Z

    move-result p1

    goto :goto_9

    nop

    :goto_12
    iget-object v0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
