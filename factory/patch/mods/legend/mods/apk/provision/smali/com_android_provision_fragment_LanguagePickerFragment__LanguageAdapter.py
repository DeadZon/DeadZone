TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/fragment/LanguagePickerFragment$LanguageAdapter.smali'
CLASS_FALLBACK_NAMES = ['LanguagePickerFragment$LanguageAdapter.smali']
CLASS_ANCHORS = ['.super Landroid/widget/ArrayAdapter;']

PATCHES = [
    {
        'id': 'com_android_provision_fragment_LanguagePickerFragment__LanguageAdapter__getView',
        'method': '.method public getView(ILandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;',
        'method_name': 'getView',
        'method_anchors': ['invoke-super {p0, p1, p2, p3}, Landroid/widget/ArrayAdapter;->getView(ILandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;', 'sget p3, Lcom/android/provision/R$id;->item_title:I', 'invoke-virtual {p2, p3}, Landroid/view/View;->findViewById(I)Landroid/view/View;', 'check-cast p3, Landroid/widget/TextView;', 'invoke-virtual {p3, v0}, Landroid/widget/TextView;->setTextDirection(I)V', 'invoke-virtual {p3, v0}, Landroid/widget/TextView;->setGravity(I)V', 'sget v0, Lcom/android/provision/R$id;->item_icon:I', 'invoke-virtual {p2, v0}, Landroid/view/View;->findViewById(I)Landroid/view/View;'],
        'type': 'policy_skip',
        'search': """.method public getView(ILandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;
    .registers 10

    invoke-super {p0, p1, p2, p3}, Landroid/widget/ArrayAdapter;->getView(ILandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;

    move-result-object p2

    sget p3, Lcom/android/provision/R$id;->item_title:I

    invoke-virtual {p2, p3}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object p3

    check-cast p3, Landroid/widget/TextView;

    const/4 v0, 0x3

    invoke-virtual {p3, v0}, Landroid/widget/TextView;->setTextDirection(I)V

    const v0, 0x800003

    invoke-virtual {p3, v0}, Landroid/widget/TextView;->setGravity(I)V

    sget v0, Lcom/android/provision/R$id;->item_icon:I

    invoke-virtual {p2, v0}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/ImageView;

    invoke-virtual {p0, p1}, Landroid/widget/ArrayAdapter;->getItem(I)Ljava/lang/Object;

    move-result-object p1

    check-cast p1, Lcom/android/internal/app/LocalePicker$LocaleInfo;

    sget-boolean v1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    const/4 v2, 0x4

    const/4 v3, 0x0

    if-eqz v1, :cond_0

    iget-object v1, p0, Lcom/android/provision/fragment/LanguagePickerFragment$LanguageAdapter;->this$0:Lcom/android/provision/fragment/LanguagePickerFragment;

    invoke-static {v1}, Lcom/android/provision/fragment/LanguagePickerFragment;->-$$Nest$fgetmTitle(Lcom/android/provision/fragment/LanguagePickerFragment;)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {p1}, Lcom/android/internal/app/LocalePicker$LocaleInfo;->toString()Ljava/lang/String;

    move-result-object v4

    invoke-static {v1, v4}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result v1

    if-eqz v1, :cond_0

    invoke-virtual {p2, v3}, Landroid/view/View;->setEnabled(Z)V

    invoke-virtual {p3, v3}, Landroid/widget/TextView;->setEnabled(Z)V

    sget v1, Lcom/android/provision/R$color;->miuix_color_transparent:I

    invoke-virtual {p2, v1}, Landroid/view/View;->setBackgroundResource(I)V

    const/4 v1, 0x0

    invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setImageDrawable(Landroid/graphics/drawable/Drawable;)V

    invoke-virtual {v0, v2}, Landroid/widget/ImageView;->setVisibility(I)V

    iget-object v0, p0, Lcom/android/provision/fragment/LanguagePickerFragment$LanguageAdapter;->this$0:Lcom/android/provision/fragment/LanguagePickerFragment;

    invoke-virtual {v0}, Landroidx/fragment/app/Fragment;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    sget v1, Lcom/android/provision/R$string;->language_picker_other_languages_title:I

    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object v0

    invoke-virtual {p3, v0}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    iget-object p0, p0, Lcom/android/provision/fragment/LanguagePickerFragment$LanguageAdapter;->this$0:Lcom/android/provision/fragment/LanguagePickerFragment;

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getResources()Landroid/content/res/Resources;

    move-result-object p0

    sget p3, Lcom/android/provision/R$string;->language_disabled_description:I

    invoke-virtual {p1}, Lcom/android/internal/app/LocalePicker$LocaleInfo;->getLabel()Ljava/lang/String;

    move-result-object p1

    filled-new-array {p1}, [Ljava/lang/Object;

    move-result-object p1

    invoke-virtual {p0, p3, p1}, Landroid/content/res/Resources;->getString(I[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object p0

    invoke-virtual {p2, p0}, Landroid/view/View;->setContentDescription(Ljava/lang/CharSequence;)V

    goto :goto_0

    :cond_0
    const/4 v1, 0x1

    invoke-virtual {p2, v1}, Landroid/view/View;->setEnabled(Z)V

    invoke-virtual {p3, v1}, Landroid/widget/TextView;->setEnabled(Z)V

    sget v4, Lcom/android/provision/R$drawable;->list_item_background_radius_common:I

    invoke-virtual {p2, v4}, Landroid/view/View;->setBackgroundResource(I)V

    iget-object v4, p0, Lcom/android/provision/fragment/LanguagePickerFragment$LanguageAdapter;->this$0:Lcom/android/provision/fragment/LanguagePickerFragment;

    invoke-virtual {v4}, Landroidx/fragment/app/Fragment;->getResources()Landroid/content/res/Resources;

    move-result-object v4

    sget v5, Lcom/android/provision/R$drawable;->language_picker_btn_radio:I

    invoke-virtual {v4, v5}, Landroid/content/res/Resources;->getDrawable(I)Landroid/graphics/drawable/Drawable;

    move-result-object v4

    invoke-virtual {v0, v4}, Landroid/widget/ImageView;->setImageDrawable(Landroid/graphics/drawable/Drawable;)V

    invoke-virtual {p1}, Lcom/android/internal/app/LocalePicker$LocaleInfo;->getLocale()Ljava/util/Locale;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/Object;->toString()Ljava/lang/String;

    move-result-object v4

    iget-object v5, p0, Lcom/android/provision/fragment/LanguagePickerFragment$LanguageAdapter;->this$0:Lcom/android/provision/fragment/LanguagePickerFragment;

    invoke-static {v5}, Lcom/android/provision/fragment/LanguagePickerFragment;->-$$Nest$fgetmSelectedLanguage(Lcom/android/provision/fragment/LanguagePickerFragment;)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v4

    if-eqz v4, :cond_1

    invoke-virtual {v0, v3}, Landroid/widget/ImageView;->setVisibility(I)V

    invoke-virtual {p3, v1}, Landroid/widget/TextView;->setSelected(Z)V

    iget-object p0, p0, Lcom/android/provision/fragment/LanguagePickerFragment$LanguageAdapter;->this$0:Lcom/android/provision/fragment/LanguagePickerFragment;

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getResources()Landroid/content/res/Resources;

    move-result-object p0

    sget p3, Lcom/android/provision/R$string;->language_selected_description:I

    invoke-virtual {p1}, Lcom/android/internal/app/LocalePicker$LocaleInfo;->getLabel()Ljava/lang/String;

    move-result-object p1

    filled-new-array {p1}, [Ljava/lang/Object;

    move-result-object p1

    invoke-virtual {p0, p3, p1}, Landroid/content/res/Resources;->getString(I[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object p0

    invoke-virtual {p2, p0}, Landroid/view/View;->setContentDescription(Ljava/lang/CharSequence;)V

    goto :goto_0

    :cond_1
    invoke-virtual {v0, v2}, Landroid/widget/ImageView;->setVisibility(I)V

    invoke-virtual {p3, v3}, Landroid/widget/TextView;->setSelected(Z)V

    iget-object p0, p0, Lcom/android/provision/fragment/LanguagePickerFragment$LanguageAdapter;->this$0:Lcom/android/provision/fragment/LanguagePickerFragment;

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getResources()Landroid/content/res/Resources;

    move-result-object p0

    sget p3, Lcom/android/provision/R$string;->language_unselected_description:I

    invoke-virtual {p1}, Lcom/android/internal/app/LocalePicker$LocaleInfo;->getLabel()Ljava/lang/String;

    move-result-object p1

    filled-new-array {p1}, [Ljava/lang/Object;

    move-result-object p1

    invoke-virtual {p0, p3, p1}, Landroid/content/res/Resources;->getString(I[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object p0

    invoke-virtual {p2, p0}, Landroid/view/View;->setContentDescription(Ljava/lang/CharSequence;)V

    :goto_0
    new-instance p0, Lcom/android/provision/fragment/LanguagePickerFragment$CustomAccessibilityDelegate;

    invoke-direct {p0}, Lcom/android/provision/fragment/LanguagePickerFragment$CustomAccessibilityDelegate;-><init>()V

    invoke-virtual {p2, p0}, Landroid/view/View;->setAccessibilityDelegate(Landroid/view/View$AccessibilityDelegate;)V

    return-object p2
.end method""",
        'replacement': """.method public getView(ILandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;
    .registers 10

    invoke-super {p0, p1, p2, p3}, Landroid/widget/ArrayAdapter;->getView(ILandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;

    move-result-object p2

    sget p3, Lcom/android/provision/R$id;->item_title:I

    invoke-virtual {p2, p3}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object p3

    check-cast p3, Landroid/widget/TextView;

    const/4 v0, 0x3

    invoke-virtual {p3, v0}, Landroid/widget/TextView;->setTextDirection(I)V

    const v0, 0x800003

    invoke-virtual {p3, v0}, Landroid/widget/TextView;->setGravity(I)V

    sget v0, Lcom/android/provision/R$id;->item_icon:I

    invoke-virtual {p2, v0}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/ImageView;

    invoke-virtual {p0, p1}, Landroid/widget/ArrayAdapter;->getItem(I)Ljava/lang/Object;

    move-result-object p1

    check-cast p1, Lcom/android/internal/app/LocalePicker$LocaleInfo;

    sget-boolean v1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    const/4 v2, 0x4

    const/4 v3, 0x0

    if-eqz v1, :cond_0

    iget-object v1, p0, Lcom/android/provision/fragment/LanguagePickerFragment$LanguageAdapter;->this$0:Lcom/android/provision/fragment/LanguagePickerFragment;

    invoke-static {v1}, Lcom/android/provision/fragment/LanguagePickerFragment;->-$$Nest$fgetmTitle(Lcom/android/provision/fragment/LanguagePickerFragment;)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {p1}, Lcom/android/internal/app/LocalePicker$LocaleInfo;->toString()Ljava/lang/String;

    move-result-object v4

    invoke-static {v1, v4}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result v1

    if-eqz v1, :cond_0

    invoke-virtual {p2, v3}, Landroid/view/View;->setEnabled(Z)V

    invoke-virtual {p3, v3}, Landroid/widget/TextView;->setEnabled(Z)V

    sget v1, Lcom/android/provision/R$color;->miuix_color_transparent:I

    invoke-virtual {p2, v1}, Landroid/view/View;->setBackgroundResource(I)V

    const/4 v1, 0x0

    invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setImageDrawable(Landroid/graphics/drawable/Drawable;)V

    invoke-virtual {v0, v2}, Landroid/widget/ImageView;->setVisibility(I)V

    iget-object v0, p0, Lcom/android/provision/fragment/LanguagePickerFragment$LanguageAdapter;->this$0:Lcom/android/provision/fragment/LanguagePickerFragment;

    invoke-virtual {v0}, Landroidx/fragment/app/Fragment;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    sget v1, Lcom/android/provision/R$string;->language_picker_other_languages_title:I

    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object v0

    invoke-virtual {p3, v0}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    iget-object p0, p0, Lcom/android/provision/fragment/LanguagePickerFragment$LanguageAdapter;->this$0:Lcom/android/provision/fragment/LanguagePickerFragment;

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getResources()Landroid/content/res/Resources;

    move-result-object p0

    sget p3, Lcom/android/provision/R$string;->language_disabled_description:I

    invoke-virtual {p1}, Lcom/android/internal/app/LocalePicker$LocaleInfo;->getLabel()Ljava/lang/String;

    move-result-object p1

    filled-new-array {p1}, [Ljava/lang/Object;

    move-result-object p1

    invoke-virtual {p0, p3, p1}, Landroid/content/res/Resources;->getString(I[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object p0

    invoke-virtual {p2, p0}, Landroid/view/View;->setContentDescription(Ljava/lang/CharSequence;)V

    goto :goto_0

    :cond_0
    const/4 v1, 0x1

    invoke-virtual {p2, v1}, Landroid/view/View;->setEnabled(Z)V

    invoke-virtual {p3, v1}, Landroid/widget/TextView;->setEnabled(Z)V

    sget v4, Lcom/android/provision/R$drawable;->list_item_background_radius_common:I

    invoke-virtual {p2, v4}, Landroid/view/View;->setBackgroundResource(I)V

    iget-object v4, p0, Lcom/android/provision/fragment/LanguagePickerFragment$LanguageAdapter;->this$0:Lcom/android/provision/fragment/LanguagePickerFragment;

    invoke-virtual {v4}, Landroidx/fragment/app/Fragment;->getResources()Landroid/content/res/Resources;

    move-result-object v4

    sget v5, Lcom/android/provision/R$drawable;->language_picker_btn_radio:I

    invoke-virtual {v4, v5}, Landroid/content/res/Resources;->getDrawable(I)Landroid/graphics/drawable/Drawable;

    move-result-object v4

    invoke-virtual {v0, v4}, Landroid/widget/ImageView;->setImageDrawable(Landroid/graphics/drawable/Drawable;)V

    invoke-virtual {p1}, Lcom/android/internal/app/LocalePicker$LocaleInfo;->getLocale()Ljava/util/Locale;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/Object;->toString()Ljava/lang/String;

    move-result-object v4

    iget-object v5, p0, Lcom/android/provision/fragment/LanguagePickerFragment$LanguageAdapter;->this$0:Lcom/android/provision/fragment/LanguagePickerFragment;

    invoke-static {v5}, Lcom/android/provision/fragment/LanguagePickerFragment;->-$$Nest$fgetmSelectedLanguage(Lcom/android/provision/fragment/LanguagePickerFragment;)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v4

    if-eqz v4, :cond_1

    invoke-virtual {v0, v3}, Landroid/widget/ImageView;->setVisibility(I)V

    invoke-virtual {p3, v1}, Landroid/widget/TextView;->setSelected(Z)V

    iget-object p0, p0, Lcom/android/provision/fragment/LanguagePickerFragment$LanguageAdapter;->this$0:Lcom/android/provision/fragment/LanguagePickerFragment;

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getResources()Landroid/content/res/Resources;

    move-result-object p0

    sget p3, Lcom/android/provision/R$string;->language_selected_description:I

    invoke-virtual {p1}, Lcom/android/internal/app/LocalePicker$LocaleInfo;->getLabel()Ljava/lang/String;

    move-result-object p1

    filled-new-array {p1}, [Ljava/lang/Object;

    move-result-object p1

    invoke-virtual {p0, p3, p1}, Landroid/content/res/Resources;->getString(I[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object p0

    invoke-virtual {p2, p0}, Landroid/view/View;->setContentDescription(Ljava/lang/CharSequence;)V

    goto :goto_0

    :cond_1
    invoke-virtual {v0, v2}, Landroid/widget/ImageView;->setVisibility(I)V

    invoke-virtual {p3, v3}, Landroid/widget/TextView;->setSelected(Z)V

    iget-object p0, p0, Lcom/android/provision/fragment/LanguagePickerFragment$LanguageAdapter;->this$0:Lcom/android/provision/fragment/LanguagePickerFragment;

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getResources()Landroid/content/res/Resources;

    move-result-object p0

    sget p3, Lcom/android/provision/R$string;->language_unselected_description:I

    invoke-virtual {p1}, Lcom/android/internal/app/LocalePicker$LocaleInfo;->getLabel()Ljava/lang/String;

    move-result-object p1

    filled-new-array {p1}, [Ljava/lang/Object;

    move-result-object p1

    invoke-virtual {p0, p3, p1}, Landroid/content/res/Resources;->getString(I[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object p0

    invoke-virtual {p2, p0}, Landroid/view/View;->setContentDescription(Ljava/lang/CharSequence;)V

    :goto_0
    new-instance p0, Lcom/android/provision/fragment/LanguagePickerFragment$CustomAccessibilityDelegate;

    invoke-direct {p0}, Lcom/android/provision/fragment/LanguagePickerFragment$CustomAccessibilityDelegate;-><init>()V

    invoke-virtual {p2, p0}, Landroid/view/View;->setAccessibilityDelegate(Landroid/view/View$AccessibilityDelegate;)V

    return-object p2
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_fragment_LanguagePickerFragment__LanguageAdapter__isEnabled',
        'method': '.method public isEnabled(I)Z',
        'method_name': 'isEnabled',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_1', 'iget-object v0, p0, Lcom/android/provision/fragment/LanguagePickerFragment$LanguageAdapter;->this$0:Lcom/android/provision/fragment/LanguagePickerFragment;', 'invoke-static {v0}, Lcom/android/provision/fragment/LanguagePickerFragment;->-$$Nest$fgetmTitle(Lcom/android/provision/fragment/LanguagePickerFragment;)Ljava/lang/String;', 'invoke-virtual {p0, p1}, Landroid/widget/ArrayAdapter;->getItem(I)Ljava/lang/Object;', 'check-cast p0, Lcom/android/internal/app/LocalePicker$LocaleInfo;', 'invoke-virtual {p0}, Lcom/android/internal/app/LocalePicker$LocaleInfo;->toString()Ljava/lang/String;', 'invoke-static {v0, p0}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z'],
        'type': 'policy_skip',
        'search': """.method public isEnabled(I)Z
    .registers 3

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_1

    iget-object v0, p0, Lcom/android/provision/fragment/LanguagePickerFragment$LanguageAdapter;->this$0:Lcom/android/provision/fragment/LanguagePickerFragment;

    invoke-static {v0}, Lcom/android/provision/fragment/LanguagePickerFragment;->-$$Nest$fgetmTitle(Lcom/android/provision/fragment/LanguagePickerFragment;)Ljava/lang/String;

    move-result-object v0

    invoke-virtual {p0, p1}, Landroid/widget/ArrayAdapter;->getItem(I)Ljava/lang/Object;

    move-result-object p0

    check-cast p0, Lcom/android/internal/app/LocalePicker$LocaleInfo;

    invoke-virtual {p0}, Lcom/android/internal/app/LocalePicker$LocaleInfo;->toString()Ljava/lang/String;

    move-result-object p0

    invoke-static {v0, p0}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result p0

    if-nez p0, :cond_0

    goto :goto_0

    :cond_0
    const/4 p0, 0x0

    return p0

    :cond_1
    :goto_0
    const/4 p0, 0x1

    return p0
.end method""",
        'replacement': """.method public isEnabled(I)Z
    .registers 3

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_1

    iget-object v0, p0, Lcom/android/provision/fragment/LanguagePickerFragment$LanguageAdapter;->this$0:Lcom/android/provision/fragment/LanguagePickerFragment;

    invoke-static {v0}, Lcom/android/provision/fragment/LanguagePickerFragment;->-$$Nest$fgetmTitle(Lcom/android/provision/fragment/LanguagePickerFragment;)Ljava/lang/String;

    move-result-object v0

    invoke-virtual {p0, p1}, Landroid/widget/ArrayAdapter;->getItem(I)Ljava/lang/Object;

    move-result-object p0

    check-cast p0, Lcom/android/internal/app/LocalePicker$LocaleInfo;

    invoke-virtual {p0}, Lcom/android/internal/app/LocalePicker$LocaleInfo;->toString()Ljava/lang/String;

    move-result-object p0

    invoke-static {v0, p0}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result p0

    if-nez p0, :cond_0

    goto :goto_0

    :cond_0
    const/4 p0, 0x0

    return p0

    :cond_1
    :goto_0
    const/4 p0, 0x1

    return p0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
]
