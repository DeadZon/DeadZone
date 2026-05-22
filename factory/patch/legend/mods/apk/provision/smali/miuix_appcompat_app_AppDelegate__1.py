TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/app/AppDelegate$1.smali'
CLASS_FALLBACK_NAMES = ['AppDelegate$1.smali']
CLASS_ANCHORS = ['.super Lmiuix/responsive/page/manager/BaseResponseStateManager;']

PATCHES = [
    {
        'id': 'miuix_appcompat_app_AppDelegate__1__getContext',
        'method': '.method protected getContext()Landroid/content/Context;',
        'method_name': 'getContext',
        'method_anchors': ['iget-object p0, p0, Lmiuix/appcompat/app/AppDelegate$1;->this$0:Lmiuix/appcompat/app/AppDelegate;', 'iget-object p0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActivity:Lmiuix/appcompat/app/AppCompatActivity;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getContext()Landroid/content/Context;
    .registers 1

    iget-object p0, p0, Lmiuix/appcompat/app/AppDelegate$1;->this$0:Lmiuix/appcompat/app/AppDelegate;

    iget-object p0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActivity:Lmiuix/appcompat/app/AppCompatActivity;

    return-object p0
.end method""",
        'replacement': """.method protected getContext()Landroid/content/Context;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/appcompat/app/AppDelegate$1;->this$0:Lmiuix/appcompat/app/AppDelegate;

    goto :goto_1

    nop

    :goto_1
    iget-object p0, p0, Lmiuix/appcompat/app/ActionBarDelegateImpl;->mActivity:Lmiuix/appcompat/app/AppCompatActivity;

    goto :goto_2

    nop

    :goto_2
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
