TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/app/AlertDialog.smali'
CLASS_FALLBACK_NAMES = ['AlertDialog.smali']
CLASS_ANCHORS = ['.super Landroidx/appcompat/app/AppCompatDialog;', '.implements Landroid/content/DialogInterface;', '.field public static final DIALOG_CONTENT_LAYOUT:[I']

PATCHES = [
    {
        'id': 'miuix_appcompat_app_AlertDialog__dismissIfAttachedToWindow',
        'method': '.method protected dismissIfAttachedToWindow(Landroid/view/View;)V',
        'method_name': 'dismissIfAttachedToWindow',
        'method_anchors': ['if-eqz p1, :cond_0', 'invoke-virtual {p1}, Landroid/view/View;->isAttachedToWindow()Z', 'if-nez p1, :cond_0', 'return-void', 'invoke-super {p0}, Landroidx/appcompat/app/AppCompatDialog;->dismiss()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected dismissIfAttachedToWindow(Landroid/view/View;)V
    .registers 2

    if-eqz p1, :cond_0

    invoke-virtual {p1}, Landroid/view/View;->isAttachedToWindow()Z

    move-result p1

    if-nez p1, :cond_0

    return-void

    :cond_0
    invoke-super {p0}, Landroidx/appcompat/app/AppCompatDialog;->dismiss()V

    return-void
.end method""",
        'replacement': """.method protected dismissIfAttachedToWindow(Landroid/view/View;)V
    .registers 2

    goto :goto_2

    nop

    :goto_0
    invoke-super {p0}, Landroidx/appcompat/app/AppCompatDialog;->dismiss()V

    goto :goto_1

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
    invoke-virtual {p1}, Landroid/view/View;->isAttachedToWindow()Z

    move-result p1

    goto :goto_6

    nop

    :goto_4
    return-void

    :goto_5
    goto :goto_0

    nop

    :goto_6
    if-eqz p1, :cond_1

    goto :goto_5

    :cond_1
    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_AlertDialog__dismissWithAnimationExistDecorView',
        'method': '.method protected dismissWithAnimationExistDecorView(Landroid/view/View;)V',
        'method_name': 'dismissWithAnimationExistDecorView',
        'method_anchors': ['invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;', 'invoke-virtual {p1}, Landroid/view/View;->getHandler()Landroid/os/Handler;', 'invoke-virtual {v1}, Landroid/os/Handler;->getLooper()Landroid/os/Looper;', 'invoke-virtual {v1}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;', 'if-ne v0, v1, :cond_0', 'iget-object p1, p0, Lmiuix/appcompat/app/AlertDialog;->mAlert:Lmiuix/appcompat/app/AlertController;', 'iget-object p0, p0, Lmiuix/appcompat/app/AlertDialog;->mOnDismiss:Lmiuix/appcompat/widget/DialogAnimHelper$OnDismiss;', 'invoke-virtual {p1, p0}, Lmiuix/appcompat/app/AlertController;->dismiss(Lmiuix/appcompat/widget/DialogAnimHelper$OnDismiss;)V'],
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

    iget-object p1, p0, Lmiuix/appcompat/app/AlertDialog;->mAlert:Lmiuix/appcompat/app/AlertController;

    iget-object p0, p0, Lmiuix/appcompat/app/AlertDialog;->mOnDismiss:Lmiuix/appcompat/widget/DialogAnimHelper$OnDismiss;

    invoke-virtual {p1, p0}, Lmiuix/appcompat/app/AlertController;->dismiss(Lmiuix/appcompat/widget/DialogAnimHelper$OnDismiss;)V

    return-void

    :cond_0
    new-instance v0, Lmiuix/appcompat/app/AlertDialog$$ExternalSyntheticLambda1;

    invoke-direct {v0, p0}, Lmiuix/appcompat/app/AlertDialog$$ExternalSyntheticLambda1;-><init>(Lmiuix/appcompat/app/AlertDialog;)V

    invoke-virtual {p1, v0}, Landroid/view/View;->post(Ljava/lang/Runnable;)Z

    return-void
.end method""",
        'replacement': """.method protected dismissWithAnimationExistDecorView(Landroid/view/View;)V
    .registers 4

    goto :goto_1

    nop

    :goto_0
    invoke-virtual {p1, p0}, Lmiuix/appcompat/app/AlertController;->dismiss(Lmiuix/appcompat/widget/DialogAnimHelper$OnDismiss;)V

    goto :goto_c

    nop

    :goto_1
    invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;

    move-result-object v0

    goto :goto_2

    nop

    :goto_2
    invoke-virtual {p1}, Landroid/view/View;->getHandler()Landroid/os/Handler;

    move-result-object v1

    goto :goto_5

    nop

    :goto_3
    iget-object p0, p0, Lmiuix/appcompat/app/AlertDialog;->mOnDismiss:Lmiuix/appcompat/widget/DialogAnimHelper$OnDismiss;

    goto :goto_0

    nop

    :goto_4
    if-eq v0, v1, :cond_0

    goto :goto_d

    :cond_0
    goto :goto_6

    nop

    :goto_5
    invoke-virtual {v1}, Landroid/os/Handler;->getLooper()Landroid/os/Looper;

    move-result-object v1

    goto :goto_b

    nop

    :goto_6
    iget-object p1, p0, Lmiuix/appcompat/app/AlertDialog;->mAlert:Lmiuix/appcompat/app/AlertController;

    goto :goto_3

    nop

    :goto_7
    new-instance v0, Lmiuix/appcompat/app/AlertDialog$$ExternalSyntheticLambda1;

    goto :goto_a

    nop

    :goto_8
    invoke-virtual {p1, v0}, Landroid/view/View;->post(Ljava/lang/Runnable;)Z

    goto :goto_9

    nop

    :goto_9
    return-void

    :goto_a
    invoke-direct {v0, p0}, Lmiuix/appcompat/app/AlertDialog$$ExternalSyntheticLambda1;-><init>(Lmiuix/appcompat/app/AlertDialog;)V

    goto :goto_8

    nop

    :goto_b
    invoke-virtual {v1}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;

    move-result-object v1

    goto :goto_4

    nop

    :goto_c
    return-void

    :goto_d
    goto :goto_7

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_AlertDialog__dismissWithAnimationOrNot',
        'method': '.method protected dismissWithAnimationOrNot(Landroid/view/View;)V',
        'method_name': 'dismissWithAnimationOrNot',
        'method_anchors': ['if-eqz p1, :cond_1', 'invoke-virtual {p1}, Landroid/view/View;->getHandler()Landroid/os/Handler;', 'if-eqz v0, :cond_0', 'invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AlertDialog;->dismissWithAnimationExistDecorView(Landroid/view/View;)V', 'return-void', 'invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AlertDialog;->dismissIfAttachedToWindow(Landroid/view/View;)V', 'return-void', 'invoke-super {p0}, Landroidx/appcompat/app/AppCompatDialog;->dismiss()V'],
        'type': 'method_replace',
        'search': """.method protected dismissWithAnimationOrNot(Landroid/view/View;)V
    .registers 3

    if-eqz p1, :cond_1

    invoke-virtual {p1}, Landroid/view/View;->getHandler()Landroid/os/Handler;

    move-result-object v0

    if-eqz v0, :cond_0

    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AlertDialog;->dismissWithAnimationExistDecorView(Landroid/view/View;)V

    return-void

    :cond_0
    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AlertDialog;->dismissIfAttachedToWindow(Landroid/view/View;)V

    return-void

    :cond_1
    invoke-super {p0}, Landroidx/appcompat/app/AppCompatDialog;->dismiss()V

    return-void
.end method""",
        'replacement': """.method protected dismissWithAnimationOrNot(Landroid/view/View;)V
    .registers 3

    goto :goto_2

    nop

    :goto_0
    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AlertDialog;->dismissIfAttachedToWindow(Landroid/view/View;)V

    goto :goto_6

    nop

    :goto_1
    return-void

    :goto_2
    if-nez p1, :cond_0

    goto :goto_7

    :cond_0
    goto :goto_a

    nop

    :goto_3
    invoke-super {p0}, Landroidx/appcompat/app/AppCompatDialog;->dismiss()V

    goto :goto_1

    nop

    :goto_4
    return-void

    :goto_5
    goto :goto_0

    nop

    :goto_6
    return-void

    :goto_7
    goto :goto_3

    nop

    :goto_8
    if-nez v0, :cond_1

    goto :goto_5

    :cond_1
    goto :goto_9

    nop

    :goto_9
    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AlertDialog;->dismissWithAnimationExistDecorView(Landroid/view/View;)V

    goto :goto_4

    nop

    :goto_a
    invoke-virtual {p1}, Landroid/view/View;->getHandler()Landroid/os/Handler;

    move-result-object v0

    goto :goto_8

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_AlertDialog__isSystemSpecialUiThread',
        'method': '.method protected isSystemSpecialUiThread()Z',
        'method_name': 'isSystemSpecialUiThread',
        'method_anchors': ['invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;', 'invoke-virtual {p0}, Ljava/lang/Thread;->getName()Ljava/lang/String;', 'const-string v0, "android.ui"', 'invoke-static {v0, p0}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z', 'if-nez p0, :cond_1', 'invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;', 'invoke-virtual {p0}, Ljava/lang/Thread;->getName()Ljava/lang/String;', 'const-string v0, "android.imms"'],
        'type': 'method_replace',
        'search': """.method protected isSystemSpecialUiThread()Z
    .registers 2

    invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;

    move-result-object p0

    invoke-virtual {p0}, Ljava/lang/Thread;->getName()Ljava/lang/String;

    move-result-object p0

    const-string v0, "android.ui"

    invoke-static {v0, p0}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result p0

    if-nez p0, :cond_1

    invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;

    move-result-object p0

    invoke-virtual {p0}, Ljava/lang/Thread;->getName()Ljava/lang/String;

    move-result-object p0

    const-string v0, "android.imms"

    invoke-static {v0, p0}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result p0

    if-nez p0, :cond_1

    invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;

    move-result-object p0

    invoke-virtual {p0}, Ljava/lang/Thread;->getName()Ljava/lang/String;

    move-result-object p0

    const-string v0, "system_server"

    invoke-static {v0, p0}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result p0

    if-eqz p0, :cond_0

    goto :goto_0

    :cond_0
    const/4 p0, 0x0

    return p0

    :cond_1
    :goto_0
    const/4 p0, 0x1

    return p0
.end method""",
        'replacement': """.method protected isSystemSpecialUiThread()Z
    .registers 2

    goto :goto_a

    nop

    :goto_0
    if-nez p0, :cond_0

    goto :goto_d

    :cond_0
    goto :goto_c

    nop

    :goto_1
    invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;

    move-result-object p0

    goto :goto_11

    nop

    :goto_2
    invoke-virtual {p0}, Ljava/lang/Thread;->getName()Ljava/lang/String;

    move-result-object p0

    goto :goto_8

    nop

    :goto_3
    const/4 p0, 0x0

    goto :goto_5

    nop

    :goto_4
    invoke-static {v0, p0}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result p0

    goto :goto_10

    nop

    :goto_5
    return p0

    :goto_6
    goto :goto_14

    nop

    :goto_7
    if-eqz p0, :cond_1

    goto :goto_6

    :cond_1
    goto :goto_b

    nop

    :goto_8
    const-string v0, "system_server"

    goto :goto_9

    nop

    :goto_9
    invoke-static {v0, p0}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result p0

    goto :goto_0

    nop

    :goto_a
    invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;

    move-result-object p0

    goto :goto_12

    nop

    :goto_b
    invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;

    move-result-object p0

    goto :goto_2

    nop

    :goto_c
    goto :goto_6

    :goto_d
    goto :goto_3

    nop

    :goto_e
    const-string v0, "android.ui"

    goto :goto_4

    nop

    :goto_f
    const-string v0, "android.imms"

    goto :goto_13

    nop

    :goto_10
    if-eqz p0, :cond_2

    goto :goto_6

    :cond_2
    goto :goto_1

    nop

    :goto_11
    invoke-virtual {p0}, Ljava/lang/Thread;->getName()Ljava/lang/String;

    move-result-object p0

    goto :goto_f

    nop

    :goto_12
    invoke-virtual {p0}, Ljava/lang/Thread;->getName()Ljava/lang/String;

    move-result-object p0

    goto :goto_e

    nop

    :goto_13
    invoke-static {v0, p0}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result p0

    goto :goto_7

    nop

    :goto_14
    const/4 p0, 0x1

    goto :goto_15

    nop

    :goto_15
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_AlertDialog__onCreate',
        'method': '.method protected onCreate(Landroid/os/Bundle;)V',
        'method_name': 'onCreate',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/appcompat/app/AlertDialog;->isSystemSpecialUiThread()Z', 'if-eqz v0, :cond_0', 'iget-object v0, p0, Lmiuix/appcompat/app/AlertDialog;->mLifecycleOwnerCompat:Lmiuix/appcompat/app/AlertDialog$LifecycleOwnerCompat;', 'if-eqz v0, :cond_0', 'invoke-virtual {v0}, Lmiuix/appcompat/app/AlertDialog$LifecycleOwnerCompat;->onCreate()V', 'iget-object v0, p0, Lmiuix/appcompat/app/AlertDialog;->mAlert:Lmiuix/appcompat/app/AlertController;', 'invoke-virtual {v0}, Lmiuix/appcompat/app/AlertController;->isDialogImmersive()Z', 'if-nez v0, :cond_1'],
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
    iget-object v0, p0, Lmiuix/appcompat/app/AlertDialog;->mAlert:Lmiuix/appcompat/app/AlertController;

    invoke-virtual {v0}, Lmiuix/appcompat/app/AlertController;->isDialogImmersive()Z

    move-result v0

    if-nez v0, :cond_1

    iget-object v0, p0, Lmiuix/appcompat/app/AlertDialog;->mAlert:Lmiuix/appcompat/app/AlertController;

    iget-boolean v0, v0, Lmiuix/appcompat/app/AlertController;->mEnableEnterAnim:Z

    if-nez v0, :cond_2

    :cond_1
    invoke-virtual {p0}, Landroid/app/Dialog;->getWindow()Landroid/view/Window;

    move-result-object v0

    const/4 v1, 0x0

    invoke-virtual {v0, v1}, Landroid/view/Window;->setWindowAnimations(I)V

    :cond_2
    invoke-super {p0, p1}, Landroidx/appcompat/app/AppCompatDialog;->onCreate(Landroid/os/Bundle;)V

    iget-object p0, p0, Lmiuix/appcompat/app/AlertDialog;->mAlert:Lmiuix/appcompat/app/AlertController;

    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AlertController;->installContent(Landroid/os/Bundle;)V

    return-void
.end method""",
        'replacement': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 4

    goto :goto_4

    nop

    :goto_0
    invoke-virtual {v0}, Lmiuix/appcompat/app/AlertDialog$LifecycleOwnerCompat;->onCreate()V

    :goto_1
    goto :goto_7

    nop

    :goto_2
    iget-boolean v0, v0, Lmiuix/appcompat/app/AlertController;->mEnableEnterAnim:Z

    goto :goto_c

    nop

    :goto_3
    if-nez v0, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_0

    nop

    :goto_4
    invoke-virtual {p0}, Lmiuix/appcompat/app/AlertDialog;->isSystemSpecialUiThread()Z

    move-result v0

    goto :goto_10

    nop

    :goto_5
    invoke-virtual {v0}, Lmiuix/appcompat/app/AlertController;->isDialogImmersive()Z

    move-result v0

    goto :goto_13

    nop

    :goto_6
    const/4 v1, 0x0

    goto :goto_9

    nop

    :goto_7
    iget-object v0, p0, Lmiuix/appcompat/app/AlertDialog;->mAlert:Lmiuix/appcompat/app/AlertController;

    goto :goto_5

    nop

    :goto_8
    return-void

    :goto_9
    invoke-virtual {v0, v1}, Landroid/view/Window;->setWindowAnimations(I)V

    :goto_a
    goto :goto_b

    nop

    :goto_b
    invoke-super {p0, p1}, Landroidx/appcompat/app/AppCompatDialog;->onCreate(Landroid/os/Bundle;)V

    goto :goto_14

    nop

    :goto_c
    if-eqz v0, :cond_1

    goto :goto_a

    :cond_1
    :goto_d
    goto :goto_e

    nop

    :goto_e
    invoke-virtual {p0}, Landroid/app/Dialog;->getWindow()Landroid/view/Window;

    move-result-object v0

    goto :goto_6

    nop

    :goto_f
    iget-object v0, p0, Lmiuix/appcompat/app/AlertDialog;->mLifecycleOwnerCompat:Lmiuix/appcompat/app/AlertDialog$LifecycleOwnerCompat;

    goto :goto_3

    nop

    :goto_10
    if-nez v0, :cond_2

    goto :goto_1

    :cond_2
    goto :goto_f

    nop

    :goto_11
    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AlertController;->installContent(Landroid/os/Bundle;)V

    goto :goto_8

    nop

    :goto_12
    iget-object v0, p0, Lmiuix/appcompat/app/AlertDialog;->mAlert:Lmiuix/appcompat/app/AlertController;

    goto :goto_2

    nop

    :goto_13
    if-eqz v0, :cond_3

    goto :goto_d

    :cond_3
    goto :goto_12

    nop

    :goto_14
    iget-object p0, p0, Lmiuix/appcompat/app/AlertDialog;->mAlert:Lmiuix/appcompat/app/AlertController;

    goto :goto_11

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_AlertDialog__onLayoutReload',
        'method': '.method protected onLayoutReload()V',
        'method_name': 'onLayoutReload',
        'method_anchors': ['return-void'],
        'type': 'method_replace',
        'search': """.method protected onLayoutReload()V
    .registers 1

    return-void
.end method""",
        'replacement': """.method protected onLayoutReload()V
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
        'id': 'miuix_appcompat_app_AlertDialog__onStart',
        'method': '.method protected onStart()V',
        'method_name': 'onStart',
        'method_anchors': ['invoke-super {p0}, Landroid/app/Dialog;->onStart()V', 'iget-object p0, p0, Lmiuix/appcompat/app/AlertDialog;->mAlert:Lmiuix/appcompat/app/AlertController;', 'invoke-virtual {p0}, Lmiuix/appcompat/app/AlertController;->onStart()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onStart()V
    .registers 1

    invoke-super {p0}, Landroid/app/Dialog;->onStart()V

    iget-object p0, p0, Lmiuix/appcompat/app/AlertDialog;->mAlert:Lmiuix/appcompat/app/AlertController;

    invoke-virtual {p0}, Lmiuix/appcompat/app/AlertController;->onStart()V

    return-void
.end method""",
        'replacement': """.method protected onStart()V
    .registers 1

    goto :goto_1

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/appcompat/app/AlertDialog;->mAlert:Lmiuix/appcompat/app/AlertController;

    goto :goto_2

    nop

    :goto_1
    invoke-super {p0}, Landroid/app/Dialog;->onStart()V

    goto :goto_0

    nop

    :goto_2
    invoke-virtual {p0}, Lmiuix/appcompat/app/AlertController;->onStart()V

    goto :goto_3

    nop

    :goto_3
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_AlertDialog__onStop',
        'method': '.method protected onStop()V',
        'method_name': 'onStop',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/appcompat/app/AlertDialog;->isSystemSpecialUiThread()Z', 'if-eqz v0, :cond_0', 'iget-object v0, p0, Lmiuix/appcompat/app/AlertDialog;->mLifecycleOwnerCompat:Lmiuix/appcompat/app/AlertDialog$LifecycleOwnerCompat;', 'if-eqz v0, :cond_0', 'invoke-virtual {v0}, Lmiuix/appcompat/app/AlertDialog$LifecycleOwnerCompat;->onStopBefore()V', 'invoke-super {p0}, Landroidx/appcompat/app/AppCompatDialog;->onStop()V', 'iget-object v0, p0, Lmiuix/appcompat/app/AlertDialog;->mAlert:Lmiuix/appcompat/app/AlertController;', 'invoke-virtual {v0}, Lmiuix/appcompat/app/AlertController;->onStop()V'],
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
    invoke-super {p0}, Landroidx/appcompat/app/AppCompatDialog;->onStop()V

    iget-object v0, p0, Lmiuix/appcompat/app/AlertDialog;->mAlert:Lmiuix/appcompat/app/AlertController;

    invoke-virtual {v0}, Lmiuix/appcompat/app/AlertController;->onStop()V

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

    goto :goto_c

    nop

    :goto_0
    invoke-virtual {p0}, Lmiuix/appcompat/app/AlertDialog;->isSystemSpecialUiThread()Z

    move-result v0

    goto :goto_b

    nop

    :goto_1
    if-nez v0, :cond_0

    goto :goto_a

    :cond_0
    goto :goto_9

    nop

    :goto_2
    invoke-super {p0}, Landroidx/appcompat/app/AppCompatDialog;->onStop()V

    goto :goto_7

    nop

    :goto_3
    if-nez v0, :cond_1

    goto :goto_a

    :cond_1
    goto :goto_8

    nop

    :goto_4
    iget-object p0, p0, Lmiuix/appcompat/app/AlertDialog;->mLifecycleOwnerCompat:Lmiuix/appcompat/app/AlertDialog$LifecycleOwnerCompat;

    goto :goto_f

    nop

    :goto_5
    invoke-virtual {p0}, Lmiuix/appcompat/app/AlertDialog$LifecycleOwnerCompat;->onStopAfter()V

    :goto_6
    goto :goto_d

    nop

    :goto_7
    iget-object v0, p0, Lmiuix/appcompat/app/AlertDialog;->mAlert:Lmiuix/appcompat/app/AlertController;

    goto :goto_e

    nop

    :goto_8
    iget-object v0, p0, Lmiuix/appcompat/app/AlertDialog;->mLifecycleOwnerCompat:Lmiuix/appcompat/app/AlertDialog$LifecycleOwnerCompat;

    goto :goto_1

    nop

    :goto_9
    invoke-virtual {v0}, Lmiuix/appcompat/app/AlertDialog$LifecycleOwnerCompat;->onStopBefore()V

    :goto_a
    goto :goto_2

    nop

    :goto_b
    if-nez v0, :cond_2

    goto :goto_6

    :cond_2
    goto :goto_4

    nop

    :goto_c
    invoke-virtual {p0}, Lmiuix/appcompat/app/AlertDialog;->isSystemSpecialUiThread()Z

    move-result v0

    goto :goto_3

    nop

    :goto_d
    return-void

    :goto_e
    invoke-virtual {v0}, Lmiuix/appcompat/app/AlertController;->onStop()V

    goto :goto_0

    nop

    :goto_f
    if-nez p0, :cond_3

    goto :goto_6

    :cond_3
    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_AlertDialog__setAccessibilityDelegate',
        'method': '.method protected setAccessibilityDelegate(Landroid/view/View;)V',
        'method_name': 'setAccessibilityDelegate',
        'method_anchors': ['if-nez p1, :cond_0', 'return-void', 'iget-object p0, p0, Lmiuix/appcompat/app/AlertDialog;->mShowDescription:Ljava/lang/CharSequence;', 'invoke-static {p1, p0}, Landroidx/core/view/ViewCompat;->setAccessibilityPaneTitle(Landroid/view/View;Ljava/lang/CharSequence;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected setAccessibilityDelegate(Landroid/view/View;)V
    .registers 2

    if-nez p1, :cond_0

    return-void

    :cond_0
    iget-object p0, p0, Lmiuix/appcompat/app/AlertDialog;->mShowDescription:Ljava/lang/CharSequence;

    invoke-static {p1, p0}, Landroidx/core/view/ViewCompat;->setAccessibilityPaneTitle(Landroid/view/View;Ljava/lang/CharSequence;)V

    return-void
.end method""",
        'replacement': """.method protected setAccessibilityDelegate(Landroid/view/View;)V
    .registers 2

    goto :goto_3

    nop

    :goto_0
    return-void

    :goto_1
    return-void

    :goto_2
    goto :goto_4

    nop

    :goto_3
    if-eqz p1, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_1

    nop

    :goto_4
    iget-object p0, p0, Lmiuix/appcompat/app/AlertDialog;->mShowDescription:Ljava/lang/CharSequence;

    goto :goto_5

    nop

    :goto_5
    invoke-static {p1, p0}, Landroidx/core/view/ViewCompat;->setAccessibilityPaneTitle(Landroid/view/View;Ljava/lang/CharSequence;)V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_AlertDialog__superOnAttachedToWindow',
        'method': '.method protected superOnAttachedToWindow()V',
        'method_name': 'superOnAttachedToWindow',
        'method_anchors': ['invoke-super {p0}, Landroid/app/Dialog;->onAttachedToWindow()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected superOnAttachedToWindow()V
    .registers 1

    invoke-super {p0}, Landroid/app/Dialog;->onAttachedToWindow()V

    return-void
.end method""",
        'replacement': """.method protected superOnAttachedToWindow()V
    .registers 1

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0}, Landroid/app/Dialog;->onAttachedToWindow()V

    goto :goto_1

    nop

    :goto_1
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_AlertDialog__superOnCreate',
        'method': '.method protected superOnCreate(Landroid/os/Bundle;)V',
        'method_name': 'superOnCreate',
        'method_anchors': ['invoke-super {p0, p1}, Landroidx/appcompat/app/AppCompatDialog;->onCreate(Landroid/os/Bundle;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected superOnCreate(Landroid/os/Bundle;)V
    .registers 2

    invoke-super {p0, p1}, Landroidx/appcompat/app/AppCompatDialog;->onCreate(Landroid/os/Bundle;)V

    return-void
.end method""",
        'replacement': """.method protected superOnCreate(Landroid/os/Bundle;)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    invoke-super {p0, p1}, Landroidx/appcompat/app/AppCompatDialog;->onCreate(Landroid/os/Bundle;)V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_AlertDialog__superOnStart',
        'method': '.method protected superOnStart()V',
        'method_name': 'superOnStart',
        'method_anchors': ['invoke-super {p0}, Landroid/app/Dialog;->onStart()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected superOnStart()V
    .registers 1

    invoke-super {p0}, Landroid/app/Dialog;->onStart()V

    return-void
.end method""",
        'replacement': """.method protected superOnStart()V
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    invoke-super {p0}, Landroid/app/Dialog;->onStart()V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_AlertDialog__superOnStop',
        'method': '.method protected superOnStop()V',
        'method_name': 'superOnStop',
        'method_anchors': ['invoke-super {p0}, Landroidx/appcompat/app/AppCompatDialog;->onStop()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected superOnStop()V
    .registers 1

    invoke-super {p0}, Landroidx/appcompat/app/AppCompatDialog;->onStop()V

    return-void
.end method""",
        'replacement': """.method protected superOnStop()V
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    invoke-super {p0}, Landroidx/appcompat/app/AppCompatDialog;->onStop()V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
