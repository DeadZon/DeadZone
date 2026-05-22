TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/app/AppDelegate.smali'
CLASS_FALLBACK_NAMES = ['AppDelegate.smali']
CLASS_ANCHORS = ['.super Lmiuix/appcompat/app/ActionBarDelegateImpl;', '.implements Lmiuix/responsive/interfaces/IResponsive;']

PATCHES = [
    {
        'id': 'miuix_appcompat_app_AppDelegate__onCreateImmersionMenu',
        'method': '.method protected onCreateImmersionMenu(Lmiuix/appcompat/internal/view/menu/MenuBuilder;)Z',
        'method_name': 'onCreateImmersionMenu',
        'method_anchors': ['iget-object p0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActivity:Lmiuix/appcompat/app/AppCompatActivity;', 'invoke-virtual {p0, p1}, Landroid/app/Activity;->onCreateOptionsMenu(Landroid/view/Menu;)Z', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected onCreateImmersionMenu(Lmiuix/appcompat/internal/view/menu/MenuBuilder;)Z
    .registers 2

    iget-object p0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActivity:Lmiuix/appcompat/app/AppCompatActivity;

    invoke-virtual {p0, p1}, Landroid/app/Activity;->onCreateOptionsMenu(Landroid/view/Menu;)Z

    move-result p0

    return p0
.end method""",
        'replacement': """.method protected onCreateImmersionMenu(Lmiuix/appcompat/internal/view/menu/MenuBuilder;)Z
    .registers 2

    goto :goto_2

    nop

    :goto_0
    invoke-virtual {p0, p1}, Landroid/app/Activity;->onCreateOptionsMenu(Landroid/view/Menu;)Z

    move-result p0

    goto :goto_1

    nop

    :goto_1
    return p0

    :goto_2
    iget-object p0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActivity:Lmiuix/appcompat/app/AppCompatActivity;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_AppDelegate__onPrepareImmersionMenu',
        'method': '.method protected onPrepareImmersionMenu(Lmiuix/appcompat/internal/view/menu/MenuBuilder;)Z',
        'method_name': 'onPrepareImmersionMenu',
        'method_anchors': ['iget-object p0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActivity:Lmiuix/appcompat/app/AppCompatActivity;', 'invoke-virtual {p0, p1}, Landroid/app/Activity;->onPrepareOptionsMenu(Landroid/view/Menu;)Z', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected onPrepareImmersionMenu(Lmiuix/appcompat/internal/view/menu/MenuBuilder;)Z
    .registers 2

    iget-object p0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActivity:Lmiuix/appcompat/app/AppCompatActivity;

    invoke-virtual {p0, p1}, Landroid/app/Activity;->onPrepareOptionsMenu(Landroid/view/Menu;)Z

    move-result p0

    return p0
.end method""",
        'replacement': """.method protected onPrepareImmersionMenu(Lmiuix/appcompat/internal/view/menu/MenuBuilder;)Z
    .registers 2

    goto :goto_2

    nop

    :goto_0
    invoke-virtual {p0, p1}, Landroid/app/Activity;->onPrepareOptionsMenu(Landroid/view/Menu;)Z

    move-result p0

    goto :goto_1

    nop

    :goto_1
    return p0

    :goto_2
    iget-object p0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActivity:Lmiuix/appcompat/app/AppCompatActivity;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_AppDelegate__setTitle',
        'method': '.method setTitle(Ljava/lang/CharSequence;)V',
        'method_name': 'setTitle',
        'method_anchors': ['iput-object p1, p0, Lmiuix/appcompat/app/AppDelegate;->mTitle:Ljava/lang/CharSequence;', 'iget-object p0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;', 'if-eqz p0, :cond_0', 'invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->setWindowTitle(Ljava/lang/CharSequence;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method setTitle(Ljava/lang/CharSequence;)V
    .registers 2

    iput-object p1, p0, Lmiuix/appcompat/app/AppDelegate;->mTitle:Ljava/lang/CharSequence;

    iget-object p0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    if-eqz p0, :cond_0

    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->setWindowTitle(Ljava/lang/CharSequence;)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method setTitle(Ljava/lang/CharSequence;)V
    .registers 2

    goto :goto_3

    nop

    :goto_0
    if-nez p0, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_1

    nop

    :goto_1
    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->setWindowTitle(Ljava/lang/CharSequence;)V

    :goto_2
    goto :goto_4

    nop

    :goto_3
    iput-object p1, p0, Lmiuix/appcompat/app/AppDelegate;->mTitle:Ljava/lang/CharSequence;

    goto :goto_5

    nop

    :goto_4
    return-void

    :goto_5
    iget-object p0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
