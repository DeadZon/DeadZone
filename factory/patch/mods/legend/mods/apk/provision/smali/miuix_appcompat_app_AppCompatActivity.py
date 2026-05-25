TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/app/AppCompatActivity.smali'
CLASS_FALLBACK_NAMES = ['AppCompatActivity.smali']
CLASS_ANCHORS = ['.super Landroidx/fragment/app/FragmentActivity;', '.implements Lmiuix/appcompat/app/IActivity;', '.implements Lmiuix/appcompat/app/floatingactivity/IActivitySwitcherAnimation;', '.implements Lmiuix/responsive/interfaces/IResponsive;']

PATCHES = [
    {
        'id': 'miuix_appcompat_app_AppCompatActivity__afterConfigurationChanged',
        'method': '.method protected afterConfigurationChanged(Landroid/content/res/Configuration;)V',
        'method_name': 'afterConfigurationChanged',
        'method_anchors': ['iget-object p0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mAppDelegate:Lmiuix/appcompat/app/AppDelegate;', 'invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AppDelegate;->afterConfigurationChanged(Landroid/content/res/Configuration;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected afterConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 2

    iget-object p0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mAppDelegate:Lmiuix/appcompat/app/AppDelegate;

    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AppDelegate;->afterConfigurationChanged(Landroid/content/res/Configuration;)V

    return-void
.end method""",
        'replacement': """.method protected afterConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mAppDelegate:Lmiuix/appcompat/app/AppDelegate;

    goto :goto_1

    nop

    :goto_1
    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AppDelegate;->afterConfigurationChanged(Landroid/content/res/Configuration;)V

    goto :goto_2

    nop

    :goto_2
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_AppCompatActivity__beforeConfigurationChanged',
        'method': '.method protected beforeConfigurationChanged(Landroid/content/res/Configuration;)V',
        'method_name': 'beforeConfigurationChanged',
        'method_anchors': ['iget-object p0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mAppDelegate:Lmiuix/appcompat/app/AppDelegate;', 'invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AppDelegate;->beforeConfigurationChanged(Landroid/content/res/Configuration;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected beforeConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 2

    iget-object p0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mAppDelegate:Lmiuix/appcompat/app/AppDelegate;

    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AppDelegate;->beforeConfigurationChanged(Landroid/content/res/Configuration;)V

    return-void
.end method""",
        'replacement': """.method protected beforeConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    iget-object p0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mAppDelegate:Lmiuix/appcompat/app/AppDelegate;

    goto :goto_2

    nop

    :goto_2
    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AppDelegate;->beforeConfigurationChanged(Landroid/content/res/Configuration;)V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_AppCompatActivity__isRegisterResponsive',
        'method': '.method protected isRegisterResponsive()Z',
        'method_name': 'isRegisterResponsive',
        'method_anchors': ['iget-object p0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mAppDelegate:Lmiuix/appcompat/app/AppDelegate;', 'invoke-virtual {p0}, Lmiuix/appcompat/app/AppDelegate;->isRegisterResponsive()Z', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected isRegisterResponsive()Z
    .registers 1

    iget-object p0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mAppDelegate:Lmiuix/appcompat/app/AppDelegate;

    invoke-virtual {p0}, Lmiuix/appcompat/app/AppDelegate;->isRegisterResponsive()Z

    move-result p0

    return p0
.end method""",
        'replacement': """.method protected isRegisterResponsive()Z
    .registers 1

    goto :goto_1

    nop

    :goto_0
    invoke-virtual {p0}, Lmiuix/appcompat/app/AppDelegate;->isRegisterResponsive()Z

    move-result p0

    goto :goto_2

    nop

    :goto_1
    iget-object p0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mAppDelegate:Lmiuix/appcompat/app/AppDelegate;

    goto :goto_0

    nop

    :goto_2
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_AppCompatActivity__isResponsiveEnabled',
        'method': '.method protected isResponsiveEnabled()Z',
        'method_name': 'isResponsiveEnabled',
        'method_anchors': ['return p0'],
        'type': 'method_replace',
        'search': """.method protected isResponsiveEnabled()Z
    .registers 1

    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method protected isResponsiveEnabled()Z
    .registers 1

    goto :goto_0

    nop

    :goto_0
    const/4 p0, 0x0

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
        'id': 'miuix_appcompat_app_AppCompatActivity__onCreate',
        'method': '.method protected onCreate(Landroid/os/Bundle;)V',
        'method_name': 'onCreate',
        'method_anchors': ['invoke-static {p0}, Lmiuix/core/util/EnvStateManager;->markWindowInfoDirty(Landroid/content/Context;)V', 'iget-object v0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mAppDelegate:Lmiuix/appcompat/app/AppDelegate;', 'invoke-virtual {p0}, Lmiuix/appcompat/app/AppCompatActivity;->isResponsiveEnabled()Z', 'invoke-virtual {v0, v1}, Lmiuix/appcompat/app/AppDelegate;->setResponsiveEnabled(Z)V', 'iget-object v0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mAppDelegate:Lmiuix/appcompat/app/AppDelegate;', 'invoke-virtual {v0, p1}, Lmiuix/appcompat/app/AppDelegate;->onCreate(Landroid/os/Bundle;)V', 'invoke-static {p0, p1, v0}, Lmiuix/core/util/EnvStateManager;->getWindowInfo(Landroid/content/Context;Landroid/content/res/Configuration;Z)Lmiuix/core/util/WindowBaseInfo;', 'iput-object p1, p0, Lmiuix/appcompat/app/AppCompatActivity;->mWindowInfo:Lmiuix/core/util/WindowBaseInfo;'],
        'type': 'method_replace',
        'search': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 4

    invoke-static {p0}, Lmiuix/core/util/EnvStateManager;->markWindowInfoDirty(Landroid/content/Context;)V

    iget-object v0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mAppDelegate:Lmiuix/appcompat/app/AppDelegate;

    invoke-virtual {p0}, Lmiuix/appcompat/app/AppCompatActivity;->isResponsiveEnabled()Z

    move-result v1

    invoke-virtual {v0, v1}, Lmiuix/appcompat/app/AppDelegate;->setResponsiveEnabled(Z)V

    iget-object v0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mAppDelegate:Lmiuix/appcompat/app/AppDelegate;

    invoke-virtual {v0, p1}, Lmiuix/appcompat/app/AppDelegate;->onCreate(Landroid/os/Bundle;)V

    const/4 p1, 0x0

    const/4 v0, 0x1

    invoke-static {p0, p1, v0}, Lmiuix/core/util/EnvStateManager;->getWindowInfo(Landroid/content/Context;Landroid/content/res/Configuration;Z)Lmiuix/core/util/WindowBaseInfo;

    move-result-object p1

    iput-object p1, p0, Lmiuix/appcompat/app/AppCompatActivity;->mWindowInfo:Lmiuix/core/util/WindowBaseInfo;

    invoke-static {p0}, Lmiuix/core/util/MiuixUIUtils;->isTallFontLang(Landroid/content/Context;)Z

    move-result p1

    if-eqz p1, :cond_0

    const/16 p1, 0x10

    goto :goto_0

    :cond_0
    const/16 p1, 0x1b

    :goto_0
    iput p1, p0, Lmiuix/appcompat/app/AppCompatActivity;->mInputViewLimitTextSizeDp:I

    invoke-virtual {p0}, Landroid/app/Activity;->getWindow()Landroid/view/Window;

    move-result-object p1

    invoke-virtual {p1}, Landroid/view/Window;->getDecorView()Landroid/view/View;

    move-result-object p1

    new-instance v0, Lmiuix/appcompat/app/AppCompatActivity$$ExternalSyntheticLambda0;

    invoke-direct {v0, p0}, Lmiuix/appcompat/app/AppCompatActivity$$ExternalSyntheticLambda0;-><init>(Lmiuix/appcompat/app/AppCompatActivity;)V

    invoke-virtual {p1, v0}, Landroid/view/View;->post(Ljava/lang/Runnable;)Z

    return-void
.end method""",
        'replacement': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 4

    goto :goto_d

    nop

    :goto_0
    const/16 p1, 0x10

    goto :goto_13

    nop

    :goto_1
    iget-object v0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mAppDelegate:Lmiuix/appcompat/app/AppDelegate;

    goto :goto_10

    nop

    :goto_2
    invoke-direct {v0, p0}, Lmiuix/appcompat/app/AppCompatActivity$$ExternalSyntheticLambda0;-><init>(Lmiuix/appcompat/app/AppCompatActivity;)V

    goto :goto_4

    nop

    :goto_3
    new-instance v0, Lmiuix/appcompat/app/AppCompatActivity$$ExternalSyntheticLambda0;

    goto :goto_2

    nop

    :goto_4
    invoke-virtual {p1, v0}, Landroid/view/View;->post(Ljava/lang/Runnable;)Z

    goto :goto_12

    nop

    :goto_5
    const/4 p1, 0x0

    goto :goto_e

    nop

    :goto_6
    const/16 p1, 0x1b

    :goto_7
    goto :goto_16

    nop

    :goto_8
    invoke-static {p0, p1, v0}, Lmiuix/core/util/EnvStateManager;->getWindowInfo(Landroid/content/Context;Landroid/content/res/Configuration;Z)Lmiuix/core/util/WindowBaseInfo;

    move-result-object p1

    goto :goto_17

    nop

    :goto_9
    invoke-virtual {p1}, Landroid/view/Window;->getDecorView()Landroid/view/View;

    move-result-object p1

    goto :goto_3

    nop

    :goto_a
    if-nez p1, :cond_0

    goto :goto_14

    :cond_0
    goto :goto_0

    nop

    :goto_b
    iget-object v0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mAppDelegate:Lmiuix/appcompat/app/AppDelegate;

    goto :goto_15

    nop

    :goto_c
    invoke-static {p0}, Lmiuix/core/util/MiuixUIUtils;->isTallFontLang(Landroid/content/Context;)Z

    move-result p1

    goto :goto_a

    nop

    :goto_d
    invoke-static {p0}, Lmiuix/core/util/EnvStateManager;->markWindowInfoDirty(Landroid/content/Context;)V

    goto :goto_1

    nop

    :goto_e
    const/4 v0, 0x1

    goto :goto_8

    nop

    :goto_f
    invoke-virtual {v0, v1}, Lmiuix/appcompat/app/AppDelegate;->setResponsiveEnabled(Z)V

    goto :goto_b

    nop

    :goto_10
    invoke-virtual {p0}, Lmiuix/appcompat/app/AppCompatActivity;->isResponsiveEnabled()Z

    move-result v1

    goto :goto_f

    nop

    :goto_11
    invoke-virtual {p0}, Landroid/app/Activity;->getWindow()Landroid/view/Window;

    move-result-object p1

    goto :goto_9

    nop

    :goto_12
    return-void

    :goto_13
    goto :goto_7

    :goto_14
    goto :goto_6

    nop

    :goto_15
    invoke-virtual {v0, p1}, Lmiuix/appcompat/app/AppDelegate;->onCreate(Landroid/os/Bundle;)V

    goto :goto_5

    nop

    :goto_16
    iput p1, p0, Lmiuix/appcompat/app/AppCompatActivity;->mInputViewLimitTextSizeDp:I

    goto :goto_11

    nop

    :goto_17
    iput-object p1, p0, Lmiuix/appcompat/app/AppCompatActivity;->mWindowInfo:Lmiuix/core/util/WindowBaseInfo;

    goto :goto_c

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_AppCompatActivity__onDestroy',
        'method': '.method protected onDestroy()V',
        'method_name': 'onDestroy',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mAppDelegate:Lmiuix/appcompat/app/AppDelegate;', 'invoke-virtual {v0}, Lmiuix/appcompat/app/AppDelegate;->onDestroy()V', 'invoke-static {p0}, Lmiuix/core/util/EnvStateManager;->removeInfoOfContext(Landroid/content/Context;)V', 'iput-object v0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mWindowInfo:Lmiuix/core/util/WindowBaseInfo;', 'invoke-super {p0}, Landroidx/fragment/app/FragmentActivity;->onDestroy()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onDestroy()V
    .registers 2

    iget-object v0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mAppDelegate:Lmiuix/appcompat/app/AppDelegate;

    invoke-virtual {v0}, Lmiuix/appcompat/app/AppDelegate;->onDestroy()V

    invoke-static {p0}, Lmiuix/core/util/EnvStateManager;->removeInfoOfContext(Landroid/content/Context;)V

    const/4 v0, 0x0

    iput-object v0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mWindowInfo:Lmiuix/core/util/WindowBaseInfo;

    invoke-super {p0}, Landroidx/fragment/app/FragmentActivity;->onDestroy()V

    return-void
.end method""",
        'replacement': """.method protected onDestroy()V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    invoke-static {p0}, Lmiuix/core/util/EnvStateManager;->removeInfoOfContext(Landroid/content/Context;)V

    goto :goto_2

    nop

    :goto_1
    iget-object v0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mAppDelegate:Lmiuix/appcompat/app/AppDelegate;

    goto :goto_4

    nop

    :goto_2
    const/4 v0, 0x0

    goto :goto_6

    nop

    :goto_3
    invoke-super {p0}, Landroidx/fragment/app/FragmentActivity;->onDestroy()V

    goto :goto_5

    nop

    :goto_4
    invoke-virtual {v0}, Lmiuix/appcompat/app/AppDelegate;->onDestroy()V

    goto :goto_0

    nop

    :goto_5
    return-void

    :goto_6
    iput-object v0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mWindowInfo:Lmiuix/core/util/WindowBaseInfo;

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_AppCompatActivity__onPostResume',
        'method': '.method protected onPostResume()V',
        'method_name': 'onPostResume',
        'method_anchors': ['iget-object p0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mAppDelegate:Lmiuix/appcompat/app/AppDelegate;', 'invoke-virtual {p0}, Lmiuix/appcompat/app/AppDelegate;->onPostResume()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onPostResume()V
    .registers 1

    iget-object p0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mAppDelegate:Lmiuix/appcompat/app/AppDelegate;

    invoke-virtual {p0}, Lmiuix/appcompat/app/AppDelegate;->onPostResume()V

    return-void
.end method""",
        'replacement': """.method protected onPostResume()V
    .registers 1

    goto :goto_2

    nop

    :goto_0
    invoke-virtual {p0}, Lmiuix/appcompat/app/AppDelegate;->onPostResume()V

    goto :goto_1

    nop

    :goto_1
    return-void

    :goto_2
    iget-object p0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mAppDelegate:Lmiuix/appcompat/app/AppDelegate;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_AppCompatActivity__onRestoreInstanceState',
        'method': '.method protected onRestoreInstanceState(Landroid/os/Bundle;)V',
        'method_name': 'onRestoreInstanceState',
        'method_anchors': ['iget-object p0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mAppDelegate:Lmiuix/appcompat/app/AppDelegate;', 'invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AppDelegate;->onRestoreInstanceState(Landroid/os/Bundle;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onRestoreInstanceState(Landroid/os/Bundle;)V
    .registers 2

    iget-object p0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mAppDelegate:Lmiuix/appcompat/app/AppDelegate;

    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AppDelegate;->onRestoreInstanceState(Landroid/os/Bundle;)V

    return-void
.end method""",
        'replacement': """.method protected onRestoreInstanceState(Landroid/os/Bundle;)V
    .registers 2

    goto :goto_2

    nop

    :goto_0
    return-void

    :goto_1
    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AppDelegate;->onRestoreInstanceState(Landroid/os/Bundle;)V

    goto :goto_0

    nop

    :goto_2
    iget-object p0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mAppDelegate:Lmiuix/appcompat/app/AppDelegate;

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_AppCompatActivity__onSaveInstanceState',
        'method': '.method protected onSaveInstanceState(Landroid/os/Bundle;)V',
        'method_name': 'onSaveInstanceState',
        'method_anchors': ['iget-object p0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mAppDelegate:Lmiuix/appcompat/app/AppDelegate;', 'invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AppDelegate;->onSaveInstanceState(Landroid/os/Bundle;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onSaveInstanceState(Landroid/os/Bundle;)V
    .registers 2

    iget-object p0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mAppDelegate:Lmiuix/appcompat/app/AppDelegate;

    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AppDelegate;->onSaveInstanceState(Landroid/os/Bundle;)V

    return-void
.end method""",
        'replacement': """.method protected onSaveInstanceState(Landroid/os/Bundle;)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mAppDelegate:Lmiuix/appcompat/app/AppDelegate;

    goto :goto_2

    nop

    :goto_1
    return-void

    :goto_2
    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AppDelegate;->onSaveInstanceState(Landroid/os/Bundle;)V

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_AppCompatActivity__onStop',
        'method': '.method protected onStop()V',
        'method_name': 'onStop',
        'method_anchors': ['iget-object p0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mAppDelegate:Lmiuix/appcompat/app/AppDelegate;', 'invoke-virtual {p0}, Lmiuix/appcompat/app/AppDelegate;->onStop()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onStop()V
    .registers 1

    iget-object p0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mAppDelegate:Lmiuix/appcompat/app/AppDelegate;

    invoke-virtual {p0}, Lmiuix/appcompat/app/AppDelegate;->onStop()V

    return-void
.end method""",
        'replacement': """.method protected onStop()V
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mAppDelegate:Lmiuix/appcompat/app/AppDelegate;

    goto :goto_2

    nop

    :goto_1
    return-void

    :goto_2
    invoke-virtual {p0}, Lmiuix/appcompat/app/AppDelegate;->onStop()V

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_AppCompatActivity__onTitleChanged',
        'method': '.method protected onTitleChanged(Ljava/lang/CharSequence;I)V',
        'method_name': 'onTitleChanged',
        'method_anchors': ['invoke-super {p0, p1, p2}, Landroid/app/Activity;->onTitleChanged(Ljava/lang/CharSequence;I)V', 'iget-object p0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mAppDelegate:Lmiuix/appcompat/app/AppDelegate;', 'invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AppDelegate;->setTitle(Ljava/lang/CharSequence;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onTitleChanged(Ljava/lang/CharSequence;I)V
    .registers 3

    invoke-super {p0, p1, p2}, Landroid/app/Activity;->onTitleChanged(Ljava/lang/CharSequence;I)V

    iget-object p0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mAppDelegate:Lmiuix/appcompat/app/AppDelegate;

    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AppDelegate;->setTitle(Ljava/lang/CharSequence;)V

    return-void
.end method""",
        'replacement': """.method protected onTitleChanged(Ljava/lang/CharSequence;I)V
    .registers 3

    goto :goto_3

    nop

    :goto_0
    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AppDelegate;->setTitle(Ljava/lang/CharSequence;)V

    goto :goto_2

    nop

    :goto_1
    iget-object p0, p0, Lmiuix/appcompat/app/AppCompatActivity;->mAppDelegate:Lmiuix/appcompat/app/AppDelegate;

    goto :goto_0

    nop

    :goto_2
    return-void

    :goto_3
    invoke-super {p0, p1, p2}, Landroid/app/Activity;->onTitleChanged(Ljava/lang/CharSequence;I)V

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
