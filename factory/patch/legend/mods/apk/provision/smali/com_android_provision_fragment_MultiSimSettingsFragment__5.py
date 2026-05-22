TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/fragment/MultiSimSettingsFragment$5.smali'
CLASS_FALLBACK_NAMES = ['MultiSimSettingsFragment$5.smali']
CLASS_ANCHORS = ['.super Landroid/os/AsyncTask;']

PATCHES = [
    {
        'id': 'com_android_provision_fragment_MultiSimSettingsFragment__5__doInBackground',
        'method': '.method protected bridge synthetic doInBackground([Ljava/lang/Object;)Ljava/lang/Object;',
        'method_name': 'doInBackground',
        'method_anchors': ['check-cast p1, [Ljava/lang/Integer;', 'invoke-virtual {p0, p1}, Lcom/android/provision/fragment/MultiSimSettingsFragment$5;->doInBackground([Ljava/lang/Integer;)Ljava/lang/Void;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected bridge synthetic doInBackground([Ljava/lang/Object;)Ljava/lang/Object;
    .registers 2

    check-cast p1, [Ljava/lang/Integer;

    invoke-virtual {p0, p1}, Lcom/android/provision/fragment/MultiSimSettingsFragment$5;->doInBackground([Ljava/lang/Integer;)Ljava/lang/Void;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected bridge synthetic doInBackground([Ljava/lang/Object;)Ljava/lang/Object;
    .registers 2

    goto :goto_2

    nop

    :goto_0
    return-object p0

    :goto_1
    invoke-virtual {p0, p1}, Lcom/android/provision/fragment/MultiSimSettingsFragment$5;->doInBackground([Ljava/lang/Integer;)Ljava/lang/Void;

    move-result-object p0

    goto :goto_0

    nop

    :goto_2
    check-cast p1, [Ljava/lang/Integer;

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_fragment_MultiSimSettingsFragment__5__onPostExecute',
        'method': '.method protected bridge synthetic onPostExecute(Ljava/lang/Object;)V',
        'method_name': 'onPostExecute',
        'method_anchors': ['check-cast p1, Ljava/lang/Void;', 'invoke-virtual {p0, p1}, Lcom/android/provision/fragment/MultiSimSettingsFragment$5;->onPostExecute(Ljava/lang/Void;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected bridge synthetic onPostExecute(Ljava/lang/Object;)V
    .registers 2

    check-cast p1, Ljava/lang/Void;

    invoke-virtual {p0, p1}, Lcom/android/provision/fragment/MultiSimSettingsFragment$5;->onPostExecute(Ljava/lang/Void;)V

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
    invoke-virtual {p0, p1}, Lcom/android/provision/fragment/MultiSimSettingsFragment$5;->onPostExecute(Ljava/lang/Void;)V

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_fragment_MultiSimSettingsFragment__5__onPostExecute',
        'method': '.method protected onPostExecute(Ljava/lang/Void;)V',
        'method_name': 'onPostExecute',
        'method_anchors': ['iget-object p0, p0, Lcom/android/provision/fragment/MultiSimSettingsFragment$5;->this$0:Lcom/android/provision/fragment/MultiSimSettingsFragment;', 'const-string p1, "pref_key_voice_data"', 'invoke-static {p0, p1, v0}, Lcom/android/provision/fragment/MultiSimSettingsFragment;->-$$Nest$menablePreference(Lcom/android/provision/fragment/MultiSimSettingsFragment;Ljava/lang/String;Z)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onPostExecute(Ljava/lang/Void;)V
    .registers 3

    iget-object p0, p0, Lcom/android/provision/fragment/MultiSimSettingsFragment$5;->this$0:Lcom/android/provision/fragment/MultiSimSettingsFragment;

    const-string p1, "pref_key_voice_data"

    const/4 v0, 0x1

    invoke-static {p0, p1, v0}, Lcom/android/provision/fragment/MultiSimSettingsFragment;->-$$Nest$menablePreference(Lcom/android/provision/fragment/MultiSimSettingsFragment;Ljava/lang/String;Z)V

    return-void
.end method""",
        'replacement': """.method protected onPostExecute(Ljava/lang/Void;)V
    .registers 3

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p0, Lcom/android/provision/fragment/MultiSimSettingsFragment$5;->this$0:Lcom/android/provision/fragment/MultiSimSettingsFragment;

    goto :goto_4

    nop

    :goto_1
    const/4 v0, 0x1

    goto :goto_3

    nop

    :goto_2
    return-void

    :goto_3
    invoke-static {p0, p1, v0}, Lcom/android/provision/fragment/MultiSimSettingsFragment;->-$$Nest$menablePreference(Lcom/android/provision/fragment/MultiSimSettingsFragment;Ljava/lang/String;Z)V

    goto :goto_2

    nop

    :goto_4
    const-string p1, "pref_key_voice_data"

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_fragment_MultiSimSettingsFragment__5__doInBackground',
        'method': '.method protected varargs doInBackground([Ljava/lang/Integer;)Ljava/lang/Void;',
        'method_name': 'doInBackground',
        'method_anchors': ['invoke-static {}, Lmiui/telephony/SubscriptionManager;->getDefault()Lmiui/telephony/SubscriptionManager;', 'invoke-virtual {p1}, Ljava/lang/Integer;->intValue()I', 'invoke-virtual {p0, p1}, Lmiui/telephony/SubscriptionManager;->setDefaultDataSlotId(I)V', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected varargs doInBackground([Ljava/lang/Integer;)Ljava/lang/Void;
    .registers 3

    invoke-static {}, Lmiui/telephony/SubscriptionManager;->getDefault()Lmiui/telephony/SubscriptionManager;

    move-result-object p0

    const/4 v0, 0x0

    aget-object p1, p1, v0

    invoke-virtual {p1}, Ljava/lang/Integer;->intValue()I

    move-result p1

    invoke-virtual {p0, p1}, Lmiui/telephony/SubscriptionManager;->setDefaultDataSlotId(I)V

    const/4 p0, 0x0

    return-object p0
.end method""",
        'replacement': """.method protected varargs doInBackground([Ljava/lang/Integer;)Ljava/lang/Void;
    .registers 3

    goto :goto_4

    nop

    :goto_0
    aget-object p1, p1, v0

    goto :goto_1

    nop

    :goto_1
    invoke-virtual {p1}, Ljava/lang/Integer;->intValue()I

    move-result p1

    goto :goto_5

    nop

    :goto_2
    return-object p0

    :goto_3
    const/4 v0, 0x0

    goto :goto_0

    nop

    :goto_4
    invoke-static {}, Lmiui/telephony/SubscriptionManager;->getDefault()Lmiui/telephony/SubscriptionManager;

    move-result-object p0

    goto :goto_3

    nop

    :goto_5
    invoke-virtual {p0, p1}, Lmiui/telephony/SubscriptionManager;->setDefaultDataSlotId(I)V

    goto :goto_6

    nop

    :goto_6
    const/4 p0, 0x0

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
