TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/fragment/OtherSettingsFragment$6.smali'
CLASS_FALLBACK_NAMES = ['OtherSettingsFragment$6.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Landroidx/preference/Preference$OnPreferenceChangeListener;']

PATCHES = [
    {
        'id': 'com_android_provision_fragment_OtherSettingsFragment__6__onPreferenceChange',
        'method': '.method public onPreferenceChange(Landroidx/preference/Preference;Ljava/lang/Object;)Z',
        'method_name': 'onPreferenceChange',
        'method_anchors': ['new-instance p1, Ljava/lang/StringBuilder;', 'invoke-direct {p1}, Ljava/lang/StringBuilder;-><init>()V', 'const-string v0, "onPreferenceChange: "', 'invoke-virtual {p1, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'invoke-virtual {p2}, Ljava/lang/Object;->toString()Ljava/lang/String;', 'invoke-virtual {p1, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'invoke-virtual {p1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;', 'const-string v0, "OtherSettingsFragment"'],
        'type': 'policy_skip',
        'search': """.method public onPreferenceChange(Landroidx/preference/Preference;Ljava/lang/Object;)Z
    .registers 5

    new-instance p1, Ljava/lang/StringBuilder;

    invoke-direct {p1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v0, "onPreferenceChange: "

    invoke-virtual {p1, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p2}, Ljava/lang/Object;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-virtual {p1, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p1

    const-string v0, "OtherSettingsFragment"

    invoke-static {v0, p1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    check-cast p2, Ljava/lang/Boolean;

    invoke-virtual {p2}, Ljava/lang/Boolean;->booleanValue()Z

    move-result p1

    const/4 p2, 0x1

    if-nez p1, :cond_1

    new-instance p1, Lmiuix/appcompat/app/AlertDialog$Builder;

    iget-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment$6;->this$0:Lcom/android/provision/fragment/OtherSettingsFragment;

    invoke-virtual {v0}, Landroidx/fragment/app/Fragment;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-direct {p1, v0}, Lmiuix/appcompat/app/AlertDialog$Builder;-><init>(Landroid/content/Context;)V

    invoke-virtual {p1, p2}, Lmiuix/appcompat/app/AlertDialog$Builder;->setCancelable(Z)Lmiuix/appcompat/app/AlertDialog$Builder;

    move-result-object p1

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    sget v0, Lcom/android/provision/R$string;->other_settings_ad_dialog_content_for_global:I

    goto :goto_0

    :cond_0
    sget v0, Lcom/android/provision/R$string;->other_settings_ad_dialog_content:I

    :goto_0
    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertDialog$Builder;->setMessage(I)Lmiuix/appcompat/app/AlertDialog$Builder;

    move-result-object p1

    sget v0, Lcom/android/provision/R$string;->other_settings_ad_dialog_agree:I

    new-instance v1, Lcom/android/provision/fragment/OtherSettingsFragment$6$3;

    invoke-direct {v1, p0}, Lcom/android/provision/fragment/OtherSettingsFragment$6$3;-><init>(Lcom/android/provision/fragment/OtherSettingsFragment$6;)V

    invoke-virtual {p1, v0, v1}, Lmiuix/appcompat/app/AlertDialog$Builder;->setPositiveButton(ILandroid/content/DialogInterface$OnClickListener;)Lmiuix/appcompat/app/AlertDialog$Builder;

    move-result-object p1

    sget v0, Lcom/android/provision/R$string;->other_settings_ad_dialog_disagree:I

    new-instance v1, Lcom/android/provision/fragment/OtherSettingsFragment$6$2;

    invoke-direct {v1, p0}, Lcom/android/provision/fragment/OtherSettingsFragment$6$2;-><init>(Lcom/android/provision/fragment/OtherSettingsFragment$6;)V

    invoke-virtual {p1, v0, v1}, Lmiuix/appcompat/app/AlertDialog$Builder;->setNegativeButton(ILandroid/content/DialogInterface$OnClickListener;)Lmiuix/appcompat/app/AlertDialog$Builder;

    move-result-object p1

    new-instance v0, Lcom/android/provision/fragment/OtherSettingsFragment$6$1;

    invoke-direct {v0, p0}, Lcom/android/provision/fragment/OtherSettingsFragment$6$1;-><init>(Lcom/android/provision/fragment/OtherSettingsFragment$6;)V

    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertDialog$Builder;->setOnCancelListener(Landroid/content/DialogInterface$OnCancelListener;)Lmiuix/appcompat/app/AlertDialog$Builder;

    move-result-object p0

    invoke-virtual {p0}, Lmiuix/appcompat/app/AlertDialog$Builder;->show()Lmiuix/appcompat/app/AlertDialog;

    goto :goto_1

    :cond_1
    iget-object p0, p0, Lcom/android/provision/fragment/OtherSettingsFragment$6;->this$0:Lcom/android/provision/fragment/OtherSettingsFragment;

    invoke-static {p0}, Lcom/android/provision/fragment/OtherSettingsFragment;->-$$Nest$fgetmPersonalizedAdPreference(Lcom/android/provision/fragment/OtherSettingsFragment;)Landroidx/preference/CheckBoxPreference;

    move-result-object p0

    sget p1, Lcom/android/provision/R$string;->other_settings_ad_enable_summary:I

    invoke-virtual {p0, p1}, Landroidx/preference/Preference;->setSummary(I)V

    :goto_1
    return p2
.end method""",
        'replacement': """.method public onPreferenceChange(Landroidx/preference/Preference;Ljava/lang/Object;)Z
    .registers 5

    new-instance p1, Ljava/lang/StringBuilder;

    invoke-direct {p1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v0, "onPreferenceChange: "

    invoke-virtual {p1, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p2}, Ljava/lang/Object;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-virtual {p1, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p1

    const-string v0, "OtherSettingsFragment"

    invoke-static {v0, p1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    check-cast p2, Ljava/lang/Boolean;

    invoke-virtual {p2}, Ljava/lang/Boolean;->booleanValue()Z

    move-result p1

    const/4 p2, 0x1

    if-nez p1, :cond_1

    new-instance p1, Lmiuix/appcompat/app/AlertDialog$Builder;

    iget-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment$6;->this$0:Lcom/android/provision/fragment/OtherSettingsFragment;

    invoke-virtual {v0}, Landroidx/fragment/app/Fragment;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-direct {p1, v0}, Lmiuix/appcompat/app/AlertDialog$Builder;-><init>(Landroid/content/Context;)V

    invoke-virtual {p1, p2}, Lmiuix/appcompat/app/AlertDialog$Builder;->setCancelable(Z)Lmiuix/appcompat/app/AlertDialog$Builder;

    move-result-object p1

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    sget v0, Lcom/android/provision/R$string;->other_settings_ad_dialog_content_for_global:I

    goto :goto_0

    :cond_0
    sget v0, Lcom/android/provision/R$string;->other_settings_ad_dialog_content:I

    :goto_0
    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertDialog$Builder;->setMessage(I)Lmiuix/appcompat/app/AlertDialog$Builder;

    move-result-object p1

    sget v0, Lcom/android/provision/R$string;->other_settings_ad_dialog_agree:I

    new-instance v1, Lcom/android/provision/fragment/OtherSettingsFragment$6$3;

    invoke-direct {v1, p0}, Lcom/android/provision/fragment/OtherSettingsFragment$6$3;-><init>(Lcom/android/provision/fragment/OtherSettingsFragment$6;)V

    invoke-virtual {p1, v0, v1}, Lmiuix/appcompat/app/AlertDialog$Builder;->setPositiveButton(ILandroid/content/DialogInterface$OnClickListener;)Lmiuix/appcompat/app/AlertDialog$Builder;

    move-result-object p1

    sget v0, Lcom/android/provision/R$string;->other_settings_ad_dialog_disagree:I

    new-instance v1, Lcom/android/provision/fragment/OtherSettingsFragment$6$2;

    invoke-direct {v1, p0}, Lcom/android/provision/fragment/OtherSettingsFragment$6$2;-><init>(Lcom/android/provision/fragment/OtherSettingsFragment$6;)V

    invoke-virtual {p1, v0, v1}, Lmiuix/appcompat/app/AlertDialog$Builder;->setNegativeButton(ILandroid/content/DialogInterface$OnClickListener;)Lmiuix/appcompat/app/AlertDialog$Builder;

    move-result-object p1

    new-instance v0, Lcom/android/provision/fragment/OtherSettingsFragment$6$1;

    invoke-direct {v0, p0}, Lcom/android/provision/fragment/OtherSettingsFragment$6$1;-><init>(Lcom/android/provision/fragment/OtherSettingsFragment$6;)V

    invoke-virtual {p1, v0}, Lmiuix/appcompat/app/AlertDialog$Builder;->setOnCancelListener(Landroid/content/DialogInterface$OnCancelListener;)Lmiuix/appcompat/app/AlertDialog$Builder;

    move-result-object p0

    invoke-virtual {p0}, Lmiuix/appcompat/app/AlertDialog$Builder;->show()Lmiuix/appcompat/app/AlertDialog;

    goto :goto_1

    :cond_1
    iget-object p0, p0, Lcom/android/provision/fragment/OtherSettingsFragment$6;->this$0:Lcom/android/provision/fragment/OtherSettingsFragment;

    invoke-static {p0}, Lcom/android/provision/fragment/OtherSettingsFragment;->-$$Nest$fgetmPersonalizedAdPreference(Lcom/android/provision/fragment/OtherSettingsFragment;)Landroidx/preference/CheckBoxPreference;

    move-result-object p0

    sget p1, Lcom/android/provision/R$string;->other_settings_ad_enable_summary:I

    invoke-virtual {p0, p1}, Landroidx/preference/Preference;->setSummary(I)V

    :goto_1
    return p2
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
]
