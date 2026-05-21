TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/fragment/LanguagePickerFragment$DelayTask.smali'
CLASS_FALLBACK_NAMES = ['LanguagePickerFragment$DelayTask.smali']
CLASS_ANCHORS = ['.super Landroid/os/AsyncTask;']

PATCHES = [
    {
        'id': 'com_android_provision_fragment_LanguagePickerFragment__DelayTask__doInBackground',
        'method': '.method protected bridge synthetic doInBackground([Ljava/lang/Object;)Ljava/lang/Object;',
        'method_name': 'doInBackground',
        'method_anchors': ['check-cast p1, [Ljava/lang/Void;', 'invoke-virtual {p0, p1}, Lcom/android/provision/fragment/LanguagePickerFragment$DelayTask;->doInBackground([Ljava/lang/Void;)Ljava/lang/Void;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected bridge synthetic doInBackground([Ljava/lang/Object;)Ljava/lang/Object;
    .registers 2

    check-cast p1, [Ljava/lang/Void;

    invoke-virtual {p0, p1}, Lcom/android/provision/fragment/LanguagePickerFragment$DelayTask;->doInBackground([Ljava/lang/Void;)Ljava/lang/Void;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected bridge synthetic doInBackground([Ljava/lang/Object;)Ljava/lang/Object;
    .registers 2

    goto :goto_0

    nop

    :goto_0
    check-cast p1, [Ljava/lang/Void;

    goto :goto_1

    nop

    :goto_1
    invoke-virtual {p0, p1}, Lcom/android/provision/fragment/LanguagePickerFragment$DelayTask;->doInBackground([Ljava/lang/Void;)Ljava/lang/Void;

    move-result-object p0

    goto :goto_2

    nop

    :goto_2
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_fragment_LanguagePickerFragment__DelayTask__onPostExecute',
        'method': '.method protected bridge synthetic onPostExecute(Ljava/lang/Object;)V',
        'method_name': 'onPostExecute',
        'method_anchors': ['check-cast p1, Ljava/lang/Void;', 'invoke-virtual {p0, p1}, Lcom/android/provision/fragment/LanguagePickerFragment$DelayTask;->onPostExecute(Ljava/lang/Void;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected bridge synthetic onPostExecute(Ljava/lang/Object;)V
    .registers 2

    check-cast p1, Ljava/lang/Void;

    invoke-virtual {p0, p1}, Lcom/android/provision/fragment/LanguagePickerFragment$DelayTask;->onPostExecute(Ljava/lang/Void;)V

    return-void
.end method""",
        'replacement': """.method protected bridge synthetic onPostExecute(Ljava/lang/Object;)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    check-cast p1, Ljava/lang/Void;

    goto :goto_2

    nop

    :goto_1
    return-void

    :goto_2
    invoke-virtual {p0, p1}, Lcom/android/provision/fragment/LanguagePickerFragment$DelayTask;->onPostExecute(Ljava/lang/Void;)V

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_fragment_LanguagePickerFragment__DelayTask__onPostExecute',
        'method': '.method protected onPostExecute(Ljava/lang/Void;)V',
        'method_name': 'onPostExecute',
        'method_anchors': ['iget-object p0, p0, Lcom/android/provision/fragment/LanguagePickerFragment$DelayTask;->this$0:Lcom/android/provision/fragment/LanguagePickerFragment;', 'invoke-static {p0}, Lcom/android/provision/fragment/LanguagePickerFragment;->-$$Nest$mfinishSetup(Lcom/android/provision/fragment/LanguagePickerFragment;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onPostExecute(Ljava/lang/Void;)V
    .registers 2

    iget-object p0, p0, Lcom/android/provision/fragment/LanguagePickerFragment$DelayTask;->this$0:Lcom/android/provision/fragment/LanguagePickerFragment;

    invoke-static {p0}, Lcom/android/provision/fragment/LanguagePickerFragment;->-$$Nest$mfinishSetup(Lcom/android/provision/fragment/LanguagePickerFragment;)V

    return-void
.end method""",
        'replacement': """.method protected onPostExecute(Ljava/lang/Void;)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p0, Lcom/android/provision/fragment/LanguagePickerFragment$DelayTask;->this$0:Lcom/android/provision/fragment/LanguagePickerFragment;

    goto :goto_1

    nop

    :goto_1
    invoke-static {p0}, Lcom/android/provision/fragment/LanguagePickerFragment;->-$$Nest$mfinishSetup(Lcom/android/provision/fragment/LanguagePickerFragment;)V

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
        'id': 'com_android_provision_fragment_LanguagePickerFragment__DelayTask__doInBackground',
        'method': '.method protected varargs doInBackground([Ljava/lang/Void;)Ljava/lang/Void;',
        'method_name': 'doInBackground',
        'method_anchors': ['iget-object p1, p0, Lcom/android/provision/fragment/LanguagePickerFragment$DelayTask;->this$0:Lcom/android/provision/fragment/LanguagePickerFragment;', 'invoke-virtual {p1}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;', 'if-eqz p1, :cond_3', 'invoke-static {}, Ljava/lang/System;->currentTimeMillis()J', 'iget-object p1, p0, Lcom/android/provision/fragment/LanguagePickerFragment$DelayTask;->this$0:Lcom/android/provision/fragment/LanguagePickerFragment;', 'invoke-virtual {p1}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;', 'const-string v2, "input_method"', 'invoke-virtual {p1, v2}, Landroid/app/Activity;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;'],
        'type': 'method_replace',
        'search': """.method protected varargs doInBackground([Ljava/lang/Void;)Ljava/lang/Void;
    .registers 10

    iget-object p1, p0, Lcom/android/provision/fragment/LanguagePickerFragment$DelayTask;->this$0:Lcom/android/provision/fragment/LanguagePickerFragment;

    invoke-virtual {p1}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p1

    if-eqz p1, :cond_3

    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v0

    iget-object p1, p0, Lcom/android/provision/fragment/LanguagePickerFragment$DelayTask;->this$0:Lcom/android/provision/fragment/LanguagePickerFragment;

    invoke-virtual {p1}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p1

    const-string v2, "input_method"

    invoke-virtual {p1, v2}, Landroid/app/Activity;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object p1

    check-cast p1, Landroid/view/inputmethod/InputMethodManager;

    iget-object p0, p0, Lcom/android/provision/fragment/LanguagePickerFragment$DelayTask;->this$0:Lcom/android/provision/fragment/LanguagePickerFragment;

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p0

    invoke-virtual {p0}, Landroid/app/Activity;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object p0

    new-instance v2, Landroid/content/Intent;

    const-string v3, "android.view.InputMethod"

    invoke-direct {v2, v3}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    :goto_0
    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v3

    sub-long/2addr v3, v0

    const-wide/16 v5, 0xfa0

    cmp-long v3, v3, v5

    const-string v4, "Provision_LanguagePickerFragment"

    if-gtz v3, :cond_1

    invoke-virtual {p1}, Landroid/view/inputmethod/InputMethodManager;->getInputMethodList()Ljava/util/List;

    move-result-object v3

    invoke-interface {v3}, Ljava/util/List;->size()I

    move-result v3

    const/4 v5, 0x0

    invoke-virtual {p0, v2, v5}, Landroid/content/pm/PackageManager;->queryIntentServices(Landroid/content/Intent;I)Ljava/util/List;

    move-result-object v5

    invoke-interface {v5}, Ljava/util/List;->size()I

    move-result v5

    new-instance v6, Ljava/lang/StringBuilder;

    invoke-direct {v6}, Ljava/lang/StringBuilder;-><init>()V

    const-string v7, "setLocale doInBackground imeListSize="

    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v6, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    const-string v7, ", imeServicesSize="

    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v6, v5}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v6}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v6

    invoke-static {v4, v6}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    if-ne v3, v5, :cond_0

    goto :goto_1

    :cond_0
    const-wide/16 v5, 0x32

    :try_start_0
    invoke-static {v5, v6}, Ljava/lang/Thread;->sleep(J)V
    :try_end_0
    .catch Ljava/lang/InterruptedException; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_0

    :catch_0
    move-exception v3

    const-string v5, "theread interrupted!"

    invoke-static {v4, v5, v3}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    goto :goto_0

    :cond_1
    :goto_1
    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object p0

    if-eqz p0, :cond_2

    const/4 p0, -0x1

    invoke-static {p0}, Lcom/android/provision/DefaultPreferenceHelper;->setRecommendedOperation(I)V

    invoke-static {p0}, Lcom/android/provision/DefaultPreferenceHelper;->setPreinstallStatusCode(I)V

    invoke-static {}, Lcom/android/provision/provider/ProvisionProvider;->clearTable()V

    :cond_2
    const-string p0, "setLocale doInBackground done"

    invoke-static {v4, p0}, Landroid/util/Log;->v(Ljava/lang/String;Ljava/lang/String;)I

    :cond_3
    const/4 p0, 0x0

    return-object p0
.end method""",
        'replacement': """.method protected varargs doInBackground([Ljava/lang/Void;)Ljava/lang/Void;
    .registers 10

    goto :goto_f

    nop

    :goto_0
    invoke-virtual {v6, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_39

    nop

    :goto_1
    const-string v2, "input_method"

    goto :goto_4

    nop

    :goto_2
    invoke-virtual {p1}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p1

    goto :goto_15

    nop

    :goto_3
    invoke-static {v4, v5, v3}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    goto :goto_13

    nop

    :goto_4
    invoke-virtual {p1, v2}, Landroid/app/Activity;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object p1

    goto :goto_21

    nop

    :goto_5
    invoke-static {v4, v6}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_b

    nop

    :goto_6
    invoke-virtual {p0}, Landroid/app/Activity;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object p0

    goto :goto_1c

    nop

    :goto_7
    const-wide/16 v5, 0xfa0

    goto :goto_26

    nop

    :goto_8
    sub-long/2addr v3, v0

    goto :goto_7

    nop

    :goto_9
    return-object p0

    :goto_a
    const/4 p0, -0x1

    goto :goto_19

    nop

    :goto_b
    if-eq v3, v5, :cond_0

    goto :goto_1e

    :cond_0
    goto :goto_1d

    nop

    :goto_c
    invoke-interface {v5}, Ljava/util/List;->size()I

    move-result v5

    goto :goto_16

    nop

    :goto_d
    if-lez v3, :cond_1

    goto :goto_14

    :cond_1
    goto :goto_2a

    nop

    :goto_e
    goto :goto_37

    :catch_0
    move-exception v3

    goto :goto_24

    nop

    :goto_f
    iget-object p1, p0, Lcom/android/provision/fragment/LanguagePickerFragment$DelayTask;->this$0:Lcom/android/provision/fragment/LanguagePickerFragment;

    goto :goto_2

    nop

    :goto_10
    invoke-static {}, Lcom/android/provision/provider/ProvisionProvider;->clearTable()V

    :goto_11
    goto :goto_1a

    nop

    :goto_12
    iget-object p0, p0, Lcom/android/provision/fragment/LanguagePickerFragment$DelayTask;->this$0:Lcom/android/provision/fragment/LanguagePickerFragment;

    goto :goto_25

    nop

    :goto_13
    goto :goto_37

    :goto_14
    goto :goto_27

    nop

    :goto_15
    if-nez p1, :cond_2

    goto :goto_29

    :cond_2
    goto :goto_2d

    nop

    :goto_16
    new-instance v6, Ljava/lang/StringBuilder;

    goto :goto_34

    nop

    :goto_17
    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v3

    goto :goto_8

    nop

    :goto_18
    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_20

    nop

    :goto_19
    invoke-static {p0}, Lcom/android/provision/DefaultPreferenceHelper;->setRecommendedOperation(I)V

    goto :goto_2e

    nop

    :goto_1a
    const-string p0, "setLocale doInBackground done"

    goto :goto_28

    nop

    :goto_1b
    if-nez p0, :cond_3

    goto :goto_11

    :cond_3
    goto :goto_a

    nop

    :goto_1c
    new-instance v2, Landroid/content/Intent;

    goto :goto_2c

    nop

    :goto_1d
    goto :goto_14

    :goto_1e
    goto :goto_33

    nop

    :goto_1f
    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_0

    nop

    :goto_20
    invoke-virtual {v6, v5}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_22

    nop

    :goto_21
    check-cast p1, Landroid/view/inputmethod/InputMethodManager;

    goto :goto_12

    nop

    :goto_22
    invoke-virtual {v6}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v6

    goto :goto_5

    nop

    :goto_23
    const-string v7, "setLocale doInBackground imeListSize="

    goto :goto_1f

    nop

    :goto_24
    const-string v5, "theread interrupted!"

    goto :goto_3

    nop

    :goto_25
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p0

    goto :goto_6

    nop

    :goto_26
    cmp-long v3, v3, v5

    goto :goto_31

    nop

    :goto_27
    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object p0

    goto :goto_1b

    nop

    :goto_28
    invoke-static {v4, p0}, Landroid/util/Log;->v(Ljava/lang/String;Ljava/lang/String;)I

    :goto_29
    goto :goto_2b

    nop

    :goto_2a
    invoke-virtual {p1}, Landroid/view/inputmethod/InputMethodManager;->getInputMethodList()Ljava/util/List;

    move-result-object v3

    goto :goto_2f

    nop

    :goto_2b
    const/4 p0, 0x0

    goto :goto_9

    nop

    :goto_2c
    const-string v3, "android.view.InputMethod"

    goto :goto_36

    nop

    :goto_2d
    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v0

    goto :goto_35

    nop

    :goto_2e
    invoke-static {p0}, Lcom/android/provision/DefaultPreferenceHelper;->setPreinstallStatusCode(I)V

    goto :goto_10

    nop

    :goto_2f
    invoke-interface {v3}, Ljava/util/List;->size()I

    move-result v3

    goto :goto_30

    nop

    :goto_30
    const/4 v5, 0x0

    goto :goto_38

    nop

    :goto_31
    const-string v4, "Provision_LanguagePickerFragment"

    goto :goto_d

    nop

    :goto_32
    invoke-virtual {p1}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p1

    goto :goto_1

    nop

    :goto_33
    const-wide/16 v5, 0x32

    :try_start_0
    invoke-static {v5, v6}, Ljava/lang/Thread;->sleep(J)V
    :try_end_0
    .catch Ljava/lang/InterruptedException; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_e

    nop

    :goto_34
    invoke-direct {v6}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_23

    nop

    :goto_35
    iget-object p1, p0, Lcom/android/provision/fragment/LanguagePickerFragment$DelayTask;->this$0:Lcom/android/provision/fragment/LanguagePickerFragment;

    goto :goto_32

    nop

    :goto_36
    invoke-direct {v2, v3}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    :goto_37
    goto :goto_17

    nop

    :goto_38
    invoke-virtual {p0, v2, v5}, Landroid/content/pm/PackageManager;->queryIntentServices(Landroid/content/Intent;I)Ljava/util/List;

    move-result-object v5

    goto :goto_c

    nop

    :goto_39
    const-string v7, ", imeServicesSize="

    goto :goto_18

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
