TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/fragment/LocalePickerFragment$DelayTask.smali'
CLASS_FALLBACK_NAMES = ['LocalePickerFragment$DelayTask.smali']
CLASS_ANCHORS = ['.super Landroid/os/AsyncTask;']

PATCHES = [
    {
        'id': 'com_android_provision_fragment_LocalePickerFragment__DelayTask__doInBackground',
        'method': '.method protected bridge synthetic doInBackground([Ljava/lang/Object;)Ljava/lang/Object;',
        'method_name': 'doInBackground',
        'method_anchors': ['check-cast p1, [Ljava/lang/Void;', 'invoke-virtual {p0, p1}, Lcom/android/provision/fragment/LocalePickerFragment$DelayTask;->doInBackground([Ljava/lang/Void;)Ljava/lang/Void;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected bridge synthetic doInBackground([Ljava/lang/Object;)Ljava/lang/Object;
    .registers 2

    check-cast p1, [Ljava/lang/Void;

    invoke-virtual {p0, p1}, Lcom/android/provision/fragment/LocalePickerFragment$DelayTask;->doInBackground([Ljava/lang/Void;)Ljava/lang/Void;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected bridge synthetic doInBackground([Ljava/lang/Object;)Ljava/lang/Object;
    .registers 2

    goto :goto_0

    nop

    :goto_0
    check-cast p1, [Ljava/lang/Void;

    goto :goto_2

    nop

    :goto_1
    return-object p0

    :goto_2
    invoke-virtual {p0, p1}, Lcom/android/provision/fragment/LocalePickerFragment$DelayTask;->doInBackground([Ljava/lang/Void;)Ljava/lang/Void;

    move-result-object p0

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_fragment_LocalePickerFragment__DelayTask__onPostExecute',
        'method': '.method protected bridge synthetic onPostExecute(Ljava/lang/Object;)V',
        'method_name': 'onPostExecute',
        'method_anchors': ['check-cast p1, Ljava/lang/Void;', 'invoke-virtual {p0, p1}, Lcom/android/provision/fragment/LocalePickerFragment$DelayTask;->onPostExecute(Ljava/lang/Void;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected bridge synthetic onPostExecute(Ljava/lang/Object;)V
    .registers 2

    check-cast p1, Ljava/lang/Void;

    invoke-virtual {p0, p1}, Lcom/android/provision/fragment/LocalePickerFragment$DelayTask;->onPostExecute(Ljava/lang/Void;)V

    return-void
.end method""",
        'replacement': """.method protected bridge synthetic onPostExecute(Ljava/lang/Object;)V
    .registers 2

    goto :goto_2

    nop

    :goto_0
    invoke-virtual {p0, p1}, Lcom/android/provision/fragment/LocalePickerFragment$DelayTask;->onPostExecute(Ljava/lang/Void;)V

    goto :goto_1

    nop

    :goto_1
    return-void

    :goto_2
    check-cast p1, Ljava/lang/Void;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_fragment_LocalePickerFragment__DelayTask__onPostExecute',
        'method': '.method protected onPostExecute(Ljava/lang/Void;)V',
        'method_name': 'onPostExecute',
        'method_anchors': ['const-string p1, "LocalPickerFragment"', 'const-string v0, "DelayTask onPostExecute"', 'invoke-static {p1, v0}, Landroid/util/Log;->v(Ljava/lang/String;Ljava/lang/String;)I', 'invoke-static {}, Ljava/lang/System;->currentTimeMillis()J', 'iget-object p1, p0, Lcom/android/provision/fragment/LocalePickerFragment$DelayTask;->this$0:Lcom/android/provision/fragment/LocalePickerFragment;', 'invoke-static {p1}, Lcom/android/provision/fragment/LocalePickerFragment;->-$$Nest$fgetmStartTime(Lcom/android/provision/fragment/LocalePickerFragment;)J', 'invoke-static {v0, v1}, Ljava/lang/String;->valueOf(J)Ljava/lang/String;', 'const-string v0, "event_local_picker_duration"'],
        'type': 'method_replace',
        'search': """.method protected onPostExecute(Ljava/lang/Void;)V
    .registers 6

    const-string p1, "LocalPickerFragment"

    const-string v0, "DelayTask onPostExecute"

    invoke-static {p1, v0}, Landroid/util/Log;->v(Ljava/lang/String;Ljava/lang/String;)I

    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v0

    iget-object p1, p0, Lcom/android/provision/fragment/LocalePickerFragment$DelayTask;->this$0:Lcom/android/provision/fragment/LocalePickerFragment;

    invoke-static {p1}, Lcom/android/provision/fragment/LocalePickerFragment;->-$$Nest$fgetmStartTime(Lcom/android/provision/fragment/LocalePickerFragment;)J

    move-result-wide v2

    sub-long/2addr v0, v2

    invoke-static {v0, v1}, Ljava/lang/String;->valueOf(J)Ljava/lang/String;

    move-result-object p1

    const-string v0, "event_local_picker_duration"

    const-string v1, "duration"

    invoke-static {v0, v1, p1}, Lcom/android/provision/utils/OTHelper;->rdCountEvent(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V

    iget-object p0, p0, Lcom/android/provision/fragment/LocalePickerFragment$DelayTask;->this$0:Lcom/android/provision/fragment/LocalePickerFragment;

    invoke-static {p0}, Lcom/android/provision/fragment/LocalePickerFragment;->-$$Nest$mfinishSetup(Lcom/android/provision/fragment/LocalePickerFragment;)V

    return-void
.end method""",
        'replacement': """.method protected onPostExecute(Ljava/lang/Void;)V
    .registers 6

    goto :goto_9

    nop

    :goto_0
    invoke-static {p1}, Lcom/android/provision/fragment/LocalePickerFragment;->-$$Nest$fgetmStartTime(Lcom/android/provision/fragment/LocalePickerFragment;)J

    move-result-wide v2

    goto :goto_5

    nop

    :goto_1
    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v0

    goto :goto_2

    nop

    :goto_2
    iget-object p1, p0, Lcom/android/provision/fragment/LocalePickerFragment$DelayTask;->this$0:Lcom/android/provision/fragment/LocalePickerFragment;

    goto :goto_0

    nop

    :goto_3
    invoke-static {p0}, Lcom/android/provision/fragment/LocalePickerFragment;->-$$Nest$mfinishSetup(Lcom/android/provision/fragment/LocalePickerFragment;)V

    goto :goto_a

    nop

    :goto_4
    iget-object p0, p0, Lcom/android/provision/fragment/LocalePickerFragment$DelayTask;->this$0:Lcom/android/provision/fragment/LocalePickerFragment;

    goto :goto_3

    nop

    :goto_5
    sub-long/2addr v0, v2

    goto :goto_8

    nop

    :goto_6
    const-string v1, "duration"

    goto :goto_b

    nop

    :goto_7
    const-string v0, "DelayTask onPostExecute"

    goto :goto_c

    nop

    :goto_8
    invoke-static {v0, v1}, Ljava/lang/String;->valueOf(J)Ljava/lang/String;

    move-result-object p1

    goto :goto_d

    nop

    :goto_9
    const-string p1, "LocalPickerFragment"

    goto :goto_7

    nop

    :goto_a
    return-void

    :goto_b
    invoke-static {v0, v1, p1}, Lcom/android/provision/utils/OTHelper;->rdCountEvent(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V

    goto :goto_4

    nop

    :goto_c
    invoke-static {p1, v0}, Landroid/util/Log;->v(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_1

    nop

    :goto_d
    const-string v0, "event_local_picker_duration"

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_fragment_LocalePickerFragment__DelayTask__doInBackground',
        'method': '.method protected varargs doInBackground([Ljava/lang/Void;)Ljava/lang/Void;',
        'method_name': 'doInBackground',
        'method_anchors': ['iget-object p1, p0, Lcom/android/provision/fragment/LocalePickerFragment$DelayTask;->this$0:Lcom/android/provision/fragment/LocalePickerFragment;', 'invoke-static {p1}, Lcom/android/provision/fragment/LocalePickerFragment;->-$$Nest$fgetmActivity(Lcom/android/provision/fragment/LocalePickerFragment;)Landroid/app/Activity;', 'if-eqz p1, :cond_3', 'invoke-static {}, Ljava/lang/System;->currentTimeMillis()J', 'iget-object p1, p0, Lcom/android/provision/fragment/LocalePickerFragment$DelayTask;->this$0:Lcom/android/provision/fragment/LocalePickerFragment;', 'invoke-static {p1}, Lcom/android/provision/fragment/LocalePickerFragment;->-$$Nest$fgetmActivity(Lcom/android/provision/fragment/LocalePickerFragment;)Landroid/app/Activity;', 'const-string v2, "input_method"', 'invoke-virtual {p1, v2}, Landroid/app/Activity;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;'],
        'type': 'method_replace',
        'search': """.method protected varargs doInBackground([Ljava/lang/Void;)Ljava/lang/Void;
    .registers 11

    iget-object p1, p0, Lcom/android/provision/fragment/LocalePickerFragment$DelayTask;->this$0:Lcom/android/provision/fragment/LocalePickerFragment;

    invoke-static {p1}, Lcom/android/provision/fragment/LocalePickerFragment;->-$$Nest$fgetmActivity(Lcom/android/provision/fragment/LocalePickerFragment;)Landroid/app/Activity;

    move-result-object p1

    if-eqz p1, :cond_3

    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v0

    iget-object p1, p0, Lcom/android/provision/fragment/LocalePickerFragment$DelayTask;->this$0:Lcom/android/provision/fragment/LocalePickerFragment;

    invoke-static {p1}, Lcom/android/provision/fragment/LocalePickerFragment;->-$$Nest$fgetmActivity(Lcom/android/provision/fragment/LocalePickerFragment;)Landroid/app/Activity;

    move-result-object p1

    const-string v2, "input_method"

    invoke-virtual {p1, v2}, Landroid/app/Activity;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object p1

    check-cast p1, Landroid/view/inputmethod/InputMethodManager;

    iget-object v2, p0, Lcom/android/provision/fragment/LocalePickerFragment$DelayTask;->this$0:Lcom/android/provision/fragment/LocalePickerFragment;

    invoke-static {v2}, Lcom/android/provision/fragment/LocalePickerFragment;->-$$Nest$fgetmActivity(Lcom/android/provision/fragment/LocalePickerFragment;)Landroid/app/Activity;

    move-result-object v2

    invoke-virtual {v2}, Landroid/app/Activity;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object v2

    new-instance v3, Landroid/content/Intent;

    const-string v4, "android.view.InputMethod"

    invoke-direct {v3, v4}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    :goto_0
    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v4

    sub-long/2addr v4, v0

    const-wide/16 v6, 0xfa0

    cmp-long v4, v4, v6

    const-string v5, "LocalPickerFragment"

    if-gtz v4, :cond_1

    invoke-virtual {p1}, Landroid/view/inputmethod/InputMethodManager;->getInputMethodList()Ljava/util/List;

    move-result-object v4

    invoke-interface {v4}, Ljava/util/List;->size()I

    move-result v4

    const/4 v6, 0x0

    invoke-virtual {v2, v3, v6}, Landroid/content/pm/PackageManager;->queryIntentServices(Landroid/content/Intent;I)Ljava/util/List;

    move-result-object v6

    invoke-interface {v6}, Ljava/util/List;->size()I

    move-result v6

    new-instance v7, Ljava/lang/StringBuilder;

    invoke-direct {v7}, Ljava/lang/StringBuilder;-><init>()V

    const-string v8, "setLocale doInBackground imeListSize="

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v7, v4}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    const-string v8, ", imeServicesSize="

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v7, v6}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v7}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v7

    invoke-static {v5, v7}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    if-ne v4, v6, :cond_0

    goto :goto_1

    :cond_0
    const-wide/16 v6, 0x32

    :try_start_0
    invoke-static {v6, v7}, Ljava/lang/Thread;->sleep(J)V
    :try_end_0
    .catch Ljava/lang/InterruptedException; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_0

    :catch_0
    move-exception v4

    const-string v6, "theread interrupted!"

    invoke-static {v5, v6, v4}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    goto :goto_0

    :cond_1
    :goto_1
    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object p1

    if-eqz p1, :cond_2

    const/4 p1, -0x1

    invoke-static {p1}, Lcom/android/provision/DefaultPreferenceHelper;->setRecommendedOperation(I)V

    invoke-static {p1}, Lcom/android/provision/DefaultPreferenceHelper;->setPreinstallStatusCode(I)V

    invoke-static {}, Lcom/android/provision/provider/ProvisionProvider;->clearTable()V

    :cond_2
    iget-object p0, p0, Lcom/android/provision/fragment/LocalePickerFragment$DelayTask;->this$0:Lcom/android/provision/fragment/LocalePickerFragment;

    invoke-static {p0}, Lcom/android/provision/fragment/LocalePickerFragment;->-$$Nest$fgetmActivity(Lcom/android/provision/fragment/LocalePickerFragment;)Landroid/app/Activity;

    move-result-object p0

    invoke-static {p0}, Lcom/android/provision/Utils;->setCustImeConfig(Landroid/content/Context;)V

    const-string p0, "setLocale doInBackground done"

    invoke-static {v5, p0}, Landroid/util/Log;->v(Ljava/lang/String;Ljava/lang/String;)I

    :cond_3
    const/4 p0, 0x0

    return-object p0
.end method""",
        'replacement': """.method protected varargs doInBackground([Ljava/lang/Void;)Ljava/lang/Void;
    .registers 11

    goto :goto_36

    nop

    :goto_0
    invoke-static {p0}, Lcom/android/provision/Utils;->setCustImeConfig(Landroid/content/Context;)V

    goto :goto_19

    nop

    :goto_1
    const/4 p0, 0x0

    goto :goto_a

    nop

    :goto_2
    const-string v5, "LocalPickerFragment"

    goto :goto_38

    nop

    :goto_3
    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v4

    goto :goto_32

    nop

    :goto_4
    invoke-virtual {v7, v6}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_c

    nop

    :goto_5
    const-string v8, "setLocale doInBackground imeListSize="

    goto :goto_25

    nop

    :goto_6
    invoke-direct {v7}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_5

    nop

    :goto_7
    const-wide/16 v6, 0xfa0

    goto :goto_30

    nop

    :goto_8
    const-string v8, ", imeServicesSize="

    goto :goto_2d

    nop

    :goto_9
    const-string v2, "input_method"

    goto :goto_2c

    nop

    :goto_a
    return-object p0

    :goto_b
    invoke-interface {v6}, Ljava/util/List;->size()I

    move-result v6

    goto :goto_31

    nop

    :goto_c
    invoke-virtual {v7}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v7

    goto :goto_17

    nop

    :goto_d
    invoke-static {v5, v6, v4}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    goto :goto_22

    nop

    :goto_e
    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v0

    goto :goto_1f

    nop

    :goto_f
    goto :goto_2b

    :catch_0
    move-exception v4

    goto :goto_18

    nop

    :goto_10
    invoke-virtual {p1}, Landroid/view/inputmethod/InputMethodManager;->getInputMethodList()Ljava/util/List;

    move-result-object v4

    goto :goto_26

    nop

    :goto_11
    invoke-static {v2}, Lcom/android/provision/fragment/LocalePickerFragment;->-$$Nest$fgetmActivity(Lcom/android/provision/fragment/LocalePickerFragment;)Landroid/app/Activity;

    move-result-object v2

    goto :goto_27

    nop

    :goto_12
    const-wide/16 v6, 0x32

    :try_start_0
    invoke-static {v6, v7}, Ljava/lang/Thread;->sleep(J)V
    :try_end_0
    .catch Ljava/lang/InterruptedException; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_f

    nop

    :goto_13
    invoke-static {v5, p0}, Landroid/util/Log;->v(Ljava/lang/String;Ljava/lang/String;)I

    :goto_14
    goto :goto_1

    nop

    :goto_15
    iget-object p0, p0, Lcom/android/provision/fragment/LocalePickerFragment$DelayTask;->this$0:Lcom/android/provision/fragment/LocalePickerFragment;

    goto :goto_2f

    nop

    :goto_16
    if-eq v4, v6, :cond_0

    goto :goto_35

    :cond_0
    goto :goto_34

    nop

    :goto_17
    invoke-static {v5, v7}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_16

    nop

    :goto_18
    const-string v6, "theread interrupted!"

    goto :goto_d

    nop

    :goto_19
    const-string p0, "setLocale doInBackground done"

    goto :goto_13

    nop

    :goto_1a
    invoke-static {}, Lcom/android/provision/provider/ProvisionProvider;->clearTable()V

    :goto_1b
    goto :goto_15

    nop

    :goto_1c
    new-instance v3, Landroid/content/Intent;

    goto :goto_37

    nop

    :goto_1d
    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object p1

    goto :goto_3a

    nop

    :goto_1e
    invoke-static {p1}, Lcom/android/provision/fragment/LocalePickerFragment;->-$$Nest$fgetmActivity(Lcom/android/provision/fragment/LocalePickerFragment;)Landroid/app/Activity;

    move-result-object p1

    goto :goto_9

    nop

    :goto_1f
    iget-object p1, p0, Lcom/android/provision/fragment/LocalePickerFragment$DelayTask;->this$0:Lcom/android/provision/fragment/LocalePickerFragment;

    goto :goto_1e

    nop

    :goto_20
    if-nez p1, :cond_1

    goto :goto_14

    :cond_1
    goto :goto_e

    nop

    :goto_21
    invoke-static {p1}, Lcom/android/provision/DefaultPreferenceHelper;->setRecommendedOperation(I)V

    goto :goto_28

    nop

    :goto_22
    goto :goto_2b

    :goto_23
    goto :goto_1d

    nop

    :goto_24
    const/4 v6, 0x0

    goto :goto_39

    nop

    :goto_25
    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_3c

    nop

    :goto_26
    invoke-interface {v4}, Ljava/util/List;->size()I

    move-result v4

    goto :goto_24

    nop

    :goto_27
    invoke-virtual {v2}, Landroid/app/Activity;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object v2

    goto :goto_1c

    nop

    :goto_28
    invoke-static {p1}, Lcom/android/provision/DefaultPreferenceHelper;->setPreinstallStatusCode(I)V

    goto :goto_1a

    nop

    :goto_29
    check-cast p1, Landroid/view/inputmethod/InputMethodManager;

    goto :goto_33

    nop

    :goto_2a
    invoke-direct {v3, v4}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    :goto_2b
    goto :goto_3

    nop

    :goto_2c
    invoke-virtual {p1, v2}, Landroid/app/Activity;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object p1

    goto :goto_29

    nop

    :goto_2d
    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_4

    nop

    :goto_2e
    invoke-static {p1}, Lcom/android/provision/fragment/LocalePickerFragment;->-$$Nest$fgetmActivity(Lcom/android/provision/fragment/LocalePickerFragment;)Landroid/app/Activity;

    move-result-object p1

    goto :goto_20

    nop

    :goto_2f
    invoke-static {p0}, Lcom/android/provision/fragment/LocalePickerFragment;->-$$Nest$fgetmActivity(Lcom/android/provision/fragment/LocalePickerFragment;)Landroid/app/Activity;

    move-result-object p0

    goto :goto_0

    nop

    :goto_30
    cmp-long v4, v4, v6

    goto :goto_2

    nop

    :goto_31
    new-instance v7, Ljava/lang/StringBuilder;

    goto :goto_6

    nop

    :goto_32
    sub-long/2addr v4, v0

    goto :goto_7

    nop

    :goto_33
    iget-object v2, p0, Lcom/android/provision/fragment/LocalePickerFragment$DelayTask;->this$0:Lcom/android/provision/fragment/LocalePickerFragment;

    goto :goto_11

    nop

    :goto_34
    goto :goto_23

    :goto_35
    goto :goto_12

    nop

    :goto_36
    iget-object p1, p0, Lcom/android/provision/fragment/LocalePickerFragment$DelayTask;->this$0:Lcom/android/provision/fragment/LocalePickerFragment;

    goto :goto_2e

    nop

    :goto_37
    const-string v4, "android.view.InputMethod"

    goto :goto_2a

    nop

    :goto_38
    if-lez v4, :cond_2

    goto :goto_23

    :cond_2
    goto :goto_10

    nop

    :goto_39
    invoke-virtual {v2, v3, v6}, Landroid/content/pm/PackageManager;->queryIntentServices(Landroid/content/Intent;I)Ljava/util/List;

    move-result-object v6

    goto :goto_b

    nop

    :goto_3a
    if-nez p1, :cond_3

    goto :goto_1b

    :cond_3
    goto :goto_3b

    nop

    :goto_3b
    const/4 p1, -0x1

    goto :goto_21

    nop

    :goto_3c
    invoke-virtual {v7, v4}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_8

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
