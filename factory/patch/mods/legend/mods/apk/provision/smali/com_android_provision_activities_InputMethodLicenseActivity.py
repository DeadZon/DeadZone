TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/activities/InputMethodLicenseActivity.smali'
CLASS_FALLBACK_NAMES = ['InputMethodLicenseActivity.smali']
CLASS_ANCHORS = ['.super Lmiuix/appcompat/app/AppCompatActivity;', '.implements Landroid/content/DialogInterface$OnCancelListener;', '.implements Landroid/content/DialogInterface$OnClickListener;']

PATCHES = [
    {
        'id': 'com_android_provision_activities_InputMethodLicenseActivity__onCreate',
        'method': '.method protected onCreate(Landroid/os/Bundle;)V',
        'method_name': 'onCreate',
        'method_anchors': ['invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V', 'invoke-virtual {p0}, Landroid/app/Activity;->getIntent()Landroid/content/Intent;', 'sget-object v0, Lcom/android/provision/activities/InputMethodLicenseActivity;->URL:Ljava/lang/String;', 'invoke-virtual {p1, v0}, Landroid/content/Intent;->getStringExtra(Ljava/lang/String;)Ljava/lang/String;', 'iput-object p1, p0, Lcom/android/provision/activities/InputMethodLicenseActivity;->mUrl:Ljava/lang/String;', 'new-instance p1, Landroid/webkit/WebView;', 'invoke-direct {p1, p0}, Landroid/webkit/WebView;-><init>(Landroid/content/Context;)V', 'iput-object p1, p0, Lcom/android/provision/activities/InputMethodLicenseActivity;->mWebView:Landroid/webkit/WebView;'],
        'type': 'method_replace',
        'search': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 4

    invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    invoke-virtual {p0}, Landroid/app/Activity;->getIntent()Landroid/content/Intent;

    move-result-object p1

    sget-object v0, Lcom/android/provision/activities/InputMethodLicenseActivity;->URL:Ljava/lang/String;

    invoke-virtual {p1, v0}, Landroid/content/Intent;->getStringExtra(Ljava/lang/String;)Ljava/lang/String;

    move-result-object p1

    iput-object p1, p0, Lcom/android/provision/activities/InputMethodLicenseActivity;->mUrl:Ljava/lang/String;

    new-instance p1, Landroid/webkit/WebView;

    invoke-direct {p1, p0}, Landroid/webkit/WebView;-><init>(Landroid/content/Context;)V

    iput-object p1, p0, Lcom/android/provision/activities/InputMethodLicenseActivity;->mWebView:Landroid/webkit/WebView;

    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->setContentView(Landroid/view/View;)V

    iget-object p1, p0, Lcom/android/provision/activities/InputMethodLicenseActivity;->mWebView:Landroid/webkit/WebView;

    invoke-virtual {p1}, Landroid/webkit/WebView;->getSettings()Landroid/webkit/WebSettings;

    move-result-object p1

    const/4 v0, 0x1

    invoke-virtual {p1, v0}, Landroid/webkit/WebSettings;->setJavaScriptEnabled(Z)V

    iget-object p1, p0, Lcom/android/provision/activities/InputMethodLicenseActivity;->mWebView:Landroid/webkit/WebView;

    new-instance v1, Lcom/android/provision/activities/InputMethodLicenseActivity$1;

    invoke-direct {v1, p0}, Lcom/android/provision/activities/InputMethodLicenseActivity$1;-><init>(Lcom/android/provision/activities/InputMethodLicenseActivity;)V

    invoke-virtual {p1, v1}, Landroid/webkit/WebView;->setWebViewClient(Landroid/webkit/WebViewClient;)V

    iget-object p1, p0, Lcom/android/provision/activities/InputMethodLicenseActivity;->mWebView:Landroid/webkit/WebView;

    new-instance v1, Lcom/android/provision/activities/InputMethodLicenseActivity$2;

    invoke-direct {v1, p0}, Lcom/android/provision/activities/InputMethodLicenseActivity$2;-><init>(Lcom/android/provision/activities/InputMethodLicenseActivity;)V

    invoke-virtual {p1, v1}, Landroid/webkit/WebView;->setWebChromeClient(Landroid/webkit/WebChromeClient;)V

    iget-object p1, p0, Lcom/android/provision/activities/InputMethodLicenseActivity;->mWebView:Landroid/webkit/WebView;

    iget-object v1, p0, Lcom/android/provision/activities/InputMethodLicenseActivity;->mUrl:Ljava/lang/String;

    invoke-virtual {p1, v1}, Landroid/webkit/WebView;->loadUrl(Ljava/lang/String;)V

    const-string p1, ""

    const/4 v1, 0x0

    invoke-static {p0, p1, p1, v0, v1}, Landroid/app/ProgressDialog;->show(Landroid/content/Context;Ljava/lang/CharSequence;Ljava/lang/CharSequence;ZZ)Landroid/app/ProgressDialog;

    move-result-object p1

    invoke-virtual {p1, v1}, Landroid/app/ProgressDialog;->setProgressStyle(I)V

    iput-object p1, p0, Lcom/android/provision/activities/InputMethodLicenseActivity;->mSpinnerDlg:Landroid/app/ProgressDialog;

    return-void
.end method""",
        'replacement': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 4

    goto :goto_19

    nop

    :goto_0
    new-instance p1, Landroid/webkit/WebView;

    goto :goto_1d

    nop

    :goto_1
    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->setContentView(Landroid/view/View;)V

    goto :goto_1c

    nop

    :goto_2
    const/4 v0, 0x1

    goto :goto_12

    nop

    :goto_3
    iput-object p1, p0, Lcom/android/provision/activities/InputMethodLicenseActivity;->mUrl:Ljava/lang/String;

    goto :goto_0

    nop

    :goto_4
    invoke-virtual {p1, v1}, Landroid/app/ProgressDialog;->setProgressStyle(I)V

    goto :goto_c

    nop

    :goto_5
    return-void

    :goto_6
    invoke-virtual {p1, v1}, Landroid/webkit/WebView;->setWebViewClient(Landroid/webkit/WebViewClient;)V

    goto :goto_16

    nop

    :goto_7
    iget-object p1, p0, Lcom/android/provision/activities/InputMethodLicenseActivity;->mWebView:Landroid/webkit/WebView;

    goto :goto_1b

    nop

    :goto_8
    invoke-virtual {p1, v1}, Landroid/webkit/WebView;->setWebChromeClient(Landroid/webkit/WebChromeClient;)V

    goto :goto_7

    nop

    :goto_9
    sget-object v0, Lcom/android/provision/activities/InputMethodLicenseActivity;->URL:Ljava/lang/String;

    goto :goto_15

    nop

    :goto_a
    const/4 v1, 0x0

    goto :goto_1a

    nop

    :goto_b
    invoke-direct {v1, p0}, Lcom/android/provision/activities/InputMethodLicenseActivity$1;-><init>(Lcom/android/provision/activities/InputMethodLicenseActivity;)V

    goto :goto_6

    nop

    :goto_c
    iput-object p1, p0, Lcom/android/provision/activities/InputMethodLicenseActivity;->mSpinnerDlg:Landroid/app/ProgressDialog;

    goto :goto_5

    nop

    :goto_d
    new-instance v1, Lcom/android/provision/activities/InputMethodLicenseActivity$1;

    goto :goto_b

    nop

    :goto_e
    new-instance v1, Lcom/android/provision/activities/InputMethodLicenseActivity$2;

    goto :goto_10

    nop

    :goto_f
    iget-object p1, p0, Lcom/android/provision/activities/InputMethodLicenseActivity;->mWebView:Landroid/webkit/WebView;

    goto :goto_d

    nop

    :goto_10
    invoke-direct {v1, p0}, Lcom/android/provision/activities/InputMethodLicenseActivity$2;-><init>(Lcom/android/provision/activities/InputMethodLicenseActivity;)V

    goto :goto_8

    nop

    :goto_11
    iput-object p1, p0, Lcom/android/provision/activities/InputMethodLicenseActivity;->mWebView:Landroid/webkit/WebView;

    goto :goto_1

    nop

    :goto_12
    invoke-virtual {p1, v0}, Landroid/webkit/WebSettings;->setJavaScriptEnabled(Z)V

    goto :goto_f

    nop

    :goto_13
    const-string p1, ""

    goto :goto_a

    nop

    :goto_14
    invoke-virtual {p1, v1}, Landroid/webkit/WebView;->loadUrl(Ljava/lang/String;)V

    goto :goto_13

    nop

    :goto_15
    invoke-virtual {p1, v0}, Landroid/content/Intent;->getStringExtra(Ljava/lang/String;)Ljava/lang/String;

    move-result-object p1

    goto :goto_3

    nop

    :goto_16
    iget-object p1, p0, Lcom/android/provision/activities/InputMethodLicenseActivity;->mWebView:Landroid/webkit/WebView;

    goto :goto_e

    nop

    :goto_17
    invoke-virtual {p0}, Landroid/app/Activity;->getIntent()Landroid/content/Intent;

    move-result-object p1

    goto :goto_9

    nop

    :goto_18
    invoke-virtual {p1}, Landroid/webkit/WebView;->getSettings()Landroid/webkit/WebSettings;

    move-result-object p1

    goto :goto_2

    nop

    :goto_19
    invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    goto :goto_17

    nop

    :goto_1a
    invoke-static {p0, p1, p1, v0, v1}, Landroid/app/ProgressDialog;->show(Landroid/content/Context;Ljava/lang/CharSequence;Ljava/lang/CharSequence;ZZ)Landroid/app/ProgressDialog;

    move-result-object p1

    goto :goto_4

    nop

    :goto_1b
    iget-object v1, p0, Lcom/android/provision/activities/InputMethodLicenseActivity;->mUrl:Ljava/lang/String;

    goto :goto_14

    nop

    :goto_1c
    iget-object p1, p0, Lcom/android/provision/activities/InputMethodLicenseActivity;->mWebView:Landroid/webkit/WebView;

    goto :goto_18

    nop

    :goto_1d
    invoke-direct {p1, p0}, Landroid/webkit/WebView;-><init>(Landroid/content/Context;)V

    goto :goto_11

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_InputMethodLicenseActivity__onDestroy',
        'method': '.method protected onDestroy()V',
        'method_name': 'onDestroy',
        'method_anchors': ['invoke-direct {p0}, Lcom/android/provision/activities/InputMethodLicenseActivity;->dismissSpinnerDlg()V', 'invoke-super {p0}, Lmiuix/appcompat/app/AppCompatActivity;->onDestroy()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onDestroy()V
    .registers 1

    invoke-direct {p0}, Lcom/android/provision/activities/InputMethodLicenseActivity;->dismissSpinnerDlg()V

    invoke-super {p0}, Lmiuix/appcompat/app/AppCompatActivity;->onDestroy()V

    return-void
.end method""",
        'replacement': """.method protected onDestroy()V
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    invoke-direct {p0}, Lcom/android/provision/activities/InputMethodLicenseActivity;->dismissSpinnerDlg()V

    goto :goto_2

    nop

    :goto_2
    invoke-super {p0}, Lmiuix/appcompat/app/AppCompatActivity;->onDestroy()V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_InputMethodLicenseActivity__onPause',
        'method': '.method protected onPause()V',
        'method_name': 'onPause',
        'method_anchors': ['invoke-super {p0}, Landroidx/fragment/app/FragmentActivity;->onPause()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onPause()V
    .registers 1

    invoke-super {p0}, Landroidx/fragment/app/FragmentActivity;->onPause()V

    return-void
.end method""",
        'replacement': """.method protected onPause()V
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    invoke-super {p0}, Landroidx/fragment/app/FragmentActivity;->onPause()V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_InputMethodLicenseActivity__onResume',
        'method': '.method protected onResume()V',
        'method_name': 'onResume',
        'method_anchors': ['invoke-super {p0}, Landroidx/fragment/app/FragmentActivity;->onResume()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onResume()V
    .registers 1

    invoke-super {p0}, Landroidx/fragment/app/FragmentActivity;->onResume()V

    return-void
.end method""",
        'replacement': """.method protected onResume()V
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    invoke-super {p0}, Landroidx/fragment/app/FragmentActivity;->onResume()V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
