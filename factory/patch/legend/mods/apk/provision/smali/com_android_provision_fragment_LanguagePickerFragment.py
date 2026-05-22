TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/fragment/LanguagePickerFragment.smali'
CLASS_FALLBACK_NAMES = ['LanguagePickerFragment.smali']
CLASS_ANCHORS = ['.super Landroidx/fragment/app/ListFragment;', '.implements Lcom/android/internal/app/LocalePicker$LocaleSelectionListener;']

PATCHES = [
    {
        'id': 'com_android_provision_fragment_LanguagePickerFragment__constructLanguageAdapter',
        'method': '.method private constructLanguageAdapter(Landroid/widget/ArrayAdapter;)Landroid/widget/ArrayAdapter;',
        'method_name': 'constructLanguageAdapter',
        'method_anchors': ['new-instance v5, Ljava/util/ArrayList;', 'invoke-direct {v5}, Ljava/util/ArrayList;-><init>()V', 'invoke-virtual {p1}, Landroid/widget/ArrayAdapter;->getCount()I', 'if-ge v0, v1, :cond_0', 'invoke-virtual {p1, v0}, Landroid/widget/ArrayAdapter;->getItem(I)Ljava/lang/Object;', 'check-cast v1, Lcom/android/internal/app/LocalePicker$LocaleInfo;', 'invoke-virtual {v5, v1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z', 'sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z'],
        'type': 'policy_skip',
        'search': """.method private constructLanguageAdapter(Landroid/widget/ArrayAdapter;)Landroid/widget/ArrayAdapter;
    .registers 8
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Landroid/widget/ArrayAdapter<",
            "Lcom/android/internal/app/LocalePicker$LocaleInfo;",
            ">;)",
            "Landroid/widget/ArrayAdapter<",
            "Lcom/android/internal/app/LocalePicker$LocaleInfo;",
            ">;"
        }
    .end annotation

    new-instance v5, Ljava/util/ArrayList;

    invoke-direct {v5}, Ljava/util/ArrayList;-><init>()V

    const/4 v0, 0x0

    :goto_0
    invoke-virtual {p1}, Landroid/widget/ArrayAdapter;->getCount()I

    move-result v1

    if-ge v0, v1, :cond_0

    invoke-virtual {p1, v0}, Landroid/widget/ArrayAdapter;->getItem(I)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/internal/app/LocalePicker$LocaleInfo;

    invoke-virtual {v5, v1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    add-int/lit8 v0, v0, 0x1

    goto :goto_0

    :cond_0
    sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz p1, :cond_1

    invoke-direct {p0, v5}, Lcom/android/provision/fragment/LanguagePickerFragment;->classifyLocales(Ljava/util/ArrayList;)V

    :cond_1
    new-instance v0, Lcom/android/provision/fragment/LanguagePickerFragment$LanguageAdapter;

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v2

    sget v3, Lcom/android/provision/R$layout;->language_list_item_view:I

    sget v4, Lcom/android/provision/R$id;->item_title:I

    move-object v1, p0

    invoke-direct/range {v0 .. v5}, Lcom/android/provision/fragment/LanguagePickerFragment$LanguageAdapter;-><init>(Lcom/android/provision/fragment/LanguagePickerFragment;Landroid/content/Context;IILjava/util/List;)V

    return-object v0
.end method""",
        'replacement': """.method private constructLanguageAdapter(Landroid/widget/ArrayAdapter;)Landroid/widget/ArrayAdapter;
    .registers 8
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Landroid/widget/ArrayAdapter<",
            "Lcom/android/internal/app/LocalePicker$LocaleInfo;",
            ">;)",
            "Landroid/widget/ArrayAdapter<",
            "Lcom/android/internal/app/LocalePicker$LocaleInfo;",
            ">;"
        }
    .end annotation

    new-instance v5, Ljava/util/ArrayList;

    invoke-direct {v5}, Ljava/util/ArrayList;-><init>()V

    const/4 v0, 0x0

    :goto_0
    invoke-virtual {p1}, Landroid/widget/ArrayAdapter;->getCount()I

    move-result v1

    if-ge v0, v1, :cond_0

    invoke-virtual {p1, v0}, Landroid/widget/ArrayAdapter;->getItem(I)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/internal/app/LocalePicker$LocaleInfo;

    invoke-virtual {v5, v1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    add-int/lit8 v0, v0, 0x1

    goto :goto_0

    :cond_0
    sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz p1, :cond_1

    invoke-direct {p0, v5}, Lcom/android/provision/fragment/LanguagePickerFragment;->classifyLocales(Ljava/util/ArrayList;)V

    :cond_1
    new-instance v0, Lcom/android/provision/fragment/LanguagePickerFragment$LanguageAdapter;

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v2

    sget v3, Lcom/android/provision/R$layout;->language_list_item_view:I

    sget v4, Lcom/android/provision/R$id;->item_title:I

    move-object v1, p0

    invoke-direct/range {v0 .. v5}, Lcom/android/provision/fragment/LanguagePickerFragment$LanguageAdapter;-><init>(Lcom/android/provision/fragment/LanguagePickerFragment;Landroid/content/Context;IILjava/util/List;)V

    return-object v0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_fragment_LanguagePickerFragment__restoreSelectedLanguage',
        'method': '.method private restoreSelectedLanguage()V',
        'method_name': 'restoreSelectedLanguage',
        'method_anchors': ['invoke-static {}, Lcom/android/provision/Utils;->getLanguage()Ljava/lang/String;', 'invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->isFirstSetLanguage()Z', 'if-eqz v1, :cond_1', 'invoke-static {}, Lcom/android/provision/Utils;->getRegionLanguage()Ljava/lang/String;', 'invoke-static {v1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z', 'if-nez v1, :cond_0', 'invoke-direct {p0}, Lcom/android/provision/fragment/LanguagePickerFragment;->getDefaultCustomizedLanguage()Ljava/lang/String;', 'sget-boolean v1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z'],
        'type': 'policy_skip',
        'search': """.method private restoreSelectedLanguage()V
    .registers 4

    invoke-static {}, Lcom/android/provision/Utils;->getLanguage()Ljava/lang/String;

    move-result-object v0

    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->isFirstSetLanguage()Z

    move-result v1

    if-eqz v1, :cond_1

    invoke-static {}, Lcom/android/provision/Utils;->getRegionLanguage()Ljava/lang/String;

    move-result-object v1

    invoke-static {v1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v1

    if-nez v1, :cond_0

    invoke-direct {p0}, Lcom/android/provision/fragment/LanguagePickerFragment;->getDefaultCustomizedLanguage()Ljava/lang/String;

    move-result-object v0

    goto :goto_0

    :cond_0
    sget-boolean v1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v1, :cond_1

    invoke-static {}, Lcom/android/provision/utils/MccHelper;->getInstance()Lcom/android/provision/utils/MccHelper;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/provision/utils/MccHelper;->getRecommendLanguage()Ljava/lang/String;

    move-result-object v0

    :cond_1
    :goto_0
    invoke-static {v0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v1

    const/4 v2, 0x0

    if-eqz v1, :cond_2

    iget-object v0, p0, Lcom/android/provision/fragment/LanguagePickerFragment;->mAdapter:Landroid/widget/ArrayAdapter;

    invoke-virtual {v0, v2}, Landroid/widget/ArrayAdapter;->getItem(I)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/internal/app/LocalePicker$LocaleInfo;

    invoke-virtual {v0}, Lcom/android/internal/app/LocalePicker$LocaleInfo;->getLocale()Ljava/util/Locale;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/Object;->toString()Ljava/lang/String;

    move-result-object v0

    iput v2, p0, Lcom/android/provision/fragment/LanguagePickerFragment;->mSelectedPosition:I

    :cond_2
    iput-object v0, p0, Lcom/android/provision/fragment/LanguagePickerFragment;->mSelectedLanguage:Ljava/lang/String;

    iget v0, p0, Lcom/android/provision/fragment/LanguagePickerFragment;->mSelectedPosition:I

    const/4 v1, -0x1

    if-ne v0, v1, :cond_4

    :goto_1
    iget-object v0, p0, Lcom/android/provision/fragment/LanguagePickerFragment;->mAdapter:Landroid/widget/ArrayAdapter;

    invoke-virtual {v0}, Landroid/widget/ArrayAdapter;->getCount()I

    move-result v0

    if-ge v2, v0, :cond_4

    iget-object v0, p0, Lcom/android/provision/fragment/LanguagePickerFragment;->mSelectedLanguage:Ljava/lang/String;

    iget-object v1, p0, Lcom/android/provision/fragment/LanguagePickerFragment;->mAdapter:Landroid/widget/ArrayAdapter;

    invoke-virtual {v1, v2}, Landroid/widget/ArrayAdapter;->getItem(I)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/internal/app/LocalePicker$LocaleInfo;

    invoke-virtual {v1}, Lcom/android/internal/app/LocalePicker$LocaleInfo;->getLocale()Ljava/util/Locale;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/Object;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result v0

    if-eqz v0, :cond_3

    iput v2, p0, Lcom/android/provision/fragment/LanguagePickerFragment;->mSelectedPosition:I

    invoke-direct {p0, v2}, Lcom/android/provision/fragment/LanguagePickerFragment;->setLanguage(I)V

    return-void

    :cond_3
    add-int/lit8 v2, v2, 0x1

    goto :goto_1

    :cond_4
    return-void
.end method""",
        'replacement': """.method private restoreSelectedLanguage()V
    .registers 4

    invoke-static {}, Lcom/android/provision/Utils;->getLanguage()Ljava/lang/String;

    move-result-object v0

    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->isFirstSetLanguage()Z

    move-result v1

    if-eqz v1, :cond_1

    invoke-static {}, Lcom/android/provision/Utils;->getRegionLanguage()Ljava/lang/String;

    move-result-object v1

    invoke-static {v1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v1

    if-nez v1, :cond_0

    invoke-direct {p0}, Lcom/android/provision/fragment/LanguagePickerFragment;->getDefaultCustomizedLanguage()Ljava/lang/String;

    move-result-object v0

    goto :goto_0

    :cond_0
    sget-boolean v1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v1, :cond_1

    invoke-static {}, Lcom/android/provision/utils/MccHelper;->getInstance()Lcom/android/provision/utils/MccHelper;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/provision/utils/MccHelper;->getRecommendLanguage()Ljava/lang/String;

    move-result-object v0

    :cond_1
    :goto_0
    invoke-static {v0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v1

    const/4 v2, 0x0

    if-eqz v1, :cond_2

    iget-object v0, p0, Lcom/android/provision/fragment/LanguagePickerFragment;->mAdapter:Landroid/widget/ArrayAdapter;

    invoke-virtual {v0, v2}, Landroid/widget/ArrayAdapter;->getItem(I)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/internal/app/LocalePicker$LocaleInfo;

    invoke-virtual {v0}, Lcom/android/internal/app/LocalePicker$LocaleInfo;->getLocale()Ljava/util/Locale;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/Object;->toString()Ljava/lang/String;

    move-result-object v0

    iput v2, p0, Lcom/android/provision/fragment/LanguagePickerFragment;->mSelectedPosition:I

    :cond_2
    iput-object v0, p0, Lcom/android/provision/fragment/LanguagePickerFragment;->mSelectedLanguage:Ljava/lang/String;

    iget v0, p0, Lcom/android/provision/fragment/LanguagePickerFragment;->mSelectedPosition:I

    const/4 v1, -0x1

    if-ne v0, v1, :cond_4

    :goto_1
    iget-object v0, p0, Lcom/android/provision/fragment/LanguagePickerFragment;->mAdapter:Landroid/widget/ArrayAdapter;

    invoke-virtual {v0}, Landroid/widget/ArrayAdapter;->getCount()I

    move-result v0

    if-ge v2, v0, :cond_4

    iget-object v0, p0, Lcom/android/provision/fragment/LanguagePickerFragment;->mSelectedLanguage:Ljava/lang/String;

    iget-object v1, p0, Lcom/android/provision/fragment/LanguagePickerFragment;->mAdapter:Landroid/widget/ArrayAdapter;

    invoke-virtual {v1, v2}, Landroid/widget/ArrayAdapter;->getItem(I)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/internal/app/LocalePicker$LocaleInfo;

    invoke-virtual {v1}, Lcom/android/internal/app/LocalePicker$LocaleInfo;->getLocale()Ljava/util/Locale;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/Object;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result v0

    if-eqz v0, :cond_3

    iput v2, p0, Lcom/android/provision/fragment/LanguagePickerFragment;->mSelectedPosition:I

    invoke-direct {p0, v2}, Lcom/android/provision/fragment/LanguagePickerFragment;->setLanguage(I)V

    return-void

    :cond_3
    add-int/lit8 v2, v2, 0x1

    goto :goto_1

    :cond_4
    return-void
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_fragment_LanguagePickerFragment__onActivityCreated',
        'method': '.method public onActivityCreated(Landroid/os/Bundle;)V',
        'method_name': 'onActivityCreated',
        'method_anchors': ['invoke-super {p0, p1}, Landroidx/fragment/app/Fragment;->onActivityCreated(Landroid/os/Bundle;)V', 'sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz p1, :cond_0', 'invoke-static {}, Lcom/android/provision/utils/MccHelper;->getInstance()Lcom/android/provision/utils/MccHelper;', 'invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;', 'invoke-virtual {p1, v0}, Lcom/android/provision/utils/MccHelper;->initRecommendLanguages(Landroid/content/Context;)V', 'invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;', 'sget v0, Lcom/android/provision/R$layout;->language_list_item_view:I'],
        'type': 'policy_skip',
        'search': """.method public onActivityCreated(Landroid/os/Bundle;)V
    .registers 4

    invoke-super {p0, p1}, Landroidx/fragment/app/Fragment;->onActivityCreated(Landroid/os/Bundle;)V

    sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz p1, :cond_0

    invoke-static {}, Lcom/android/provision/utils/MccHelper;->getInstance()Lcom/android/provision/utils/MccHelper;

    move-result-object p1

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-virtual {p1, v0}, Lcom/android/provision/utils/MccHelper;->initRecommendLanguages(Landroid/content/Context;)V

    :cond_0
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p1

    sget v0, Lcom/android/provision/R$layout;->language_list_item_view:I

    sget v1, Lcom/android/provision/R$id;->item_title:I

    invoke-static {p1, v0, v1}, Lcom/android/internal/app/LocalePicker;->constructAdapter(Landroid/content/Context;II)Landroid/widget/ArrayAdapter;

    move-result-object p1

    invoke-direct {p0, p1}, Lcom/android/provision/fragment/LanguagePickerFragment;->constructLanguageAdapter(Landroid/widget/ArrayAdapter;)Landroid/widget/ArrayAdapter;

    move-result-object p1

    iput-object p1, p0, Lcom/android/provision/fragment/LanguagePickerFragment;->mAdapter:Landroid/widget/ArrayAdapter;

    invoke-direct {p0}, Lcom/android/provision/fragment/LanguagePickerFragment;->restoreSelectedLanguage()V

    iget-object p1, p0, Lcom/android/provision/fragment/LanguagePickerFragment;->mAdapter:Landroid/widget/ArrayAdapter;

    invoke-virtual {p0, p1}, Landroidx/fragment/app/ListFragment;->setListAdapter(Landroid/widget/ListAdapter;)V

    invoke-direct {p0}, Lcom/android/provision/fragment/LanguagePickerFragment;->addContentAlphaAnim()V

    invoke-virtual {p0}, Landroidx/fragment/app/ListFragment;->getListView()Landroid/widget/ListView;

    move-result-object p1

    invoke-virtual {p1}, Landroid/widget/ListView;->getViewTreeObserver()Landroid/view/ViewTreeObserver;

    move-result-object p1

    new-instance v0, Lcom/android/provision/fragment/LanguagePickerFragment$2;

    invoke-direct {v0, p0}, Lcom/android/provision/fragment/LanguagePickerFragment$2;-><init>(Lcom/android/provision/fragment/LanguagePickerFragment;)V

    invoke-virtual {p1, v0}, Landroid/view/ViewTreeObserver;->addOnGlobalLayoutListener(Landroid/view/ViewTreeObserver$OnGlobalLayoutListener;)V

    return-void
.end method""",
        'replacement': """.method public onActivityCreated(Landroid/os/Bundle;)V
    .registers 4

    invoke-super {p0, p1}, Landroidx/fragment/app/Fragment;->onActivityCreated(Landroid/os/Bundle;)V

    sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz p1, :cond_0

    invoke-static {}, Lcom/android/provision/utils/MccHelper;->getInstance()Lcom/android/provision/utils/MccHelper;

    move-result-object p1

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-virtual {p1, v0}, Lcom/android/provision/utils/MccHelper;->initRecommendLanguages(Landroid/content/Context;)V

    :cond_0
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p1

    sget v0, Lcom/android/provision/R$layout;->language_list_item_view:I

    sget v1, Lcom/android/provision/R$id;->item_title:I

    invoke-static {p1, v0, v1}, Lcom/android/internal/app/LocalePicker;->constructAdapter(Landroid/content/Context;II)Landroid/widget/ArrayAdapter;

    move-result-object p1

    invoke-direct {p0, p1}, Lcom/android/provision/fragment/LanguagePickerFragment;->constructLanguageAdapter(Landroid/widget/ArrayAdapter;)Landroid/widget/ArrayAdapter;

    move-result-object p1

    iput-object p1, p0, Lcom/android/provision/fragment/LanguagePickerFragment;->mAdapter:Landroid/widget/ArrayAdapter;

    invoke-direct {p0}, Lcom/android/provision/fragment/LanguagePickerFragment;->restoreSelectedLanguage()V

    iget-object p1, p0, Lcom/android/provision/fragment/LanguagePickerFragment;->mAdapter:Landroid/widget/ArrayAdapter;

    invoke-virtual {p0, p1}, Landroidx/fragment/app/ListFragment;->setListAdapter(Landroid/widget/ListAdapter;)V

    invoke-direct {p0}, Lcom/android/provision/fragment/LanguagePickerFragment;->addContentAlphaAnim()V

    invoke-virtual {p0}, Landroidx/fragment/app/ListFragment;->getListView()Landroid/widget/ListView;

    move-result-object p1

    invoke-virtual {p1}, Landroid/widget/ListView;->getViewTreeObserver()Landroid/view/ViewTreeObserver;

    move-result-object p1

    new-instance v0, Lcom/android/provision/fragment/LanguagePickerFragment$2;

    invoke-direct {v0, p0}, Lcom/android/provision/fragment/LanguagePickerFragment$2;-><init>(Lcom/android/provision/fragment/LanguagePickerFragment;)V

    invoke-virtual {p1, v0}, Landroid/view/ViewTreeObserver;->addOnGlobalLayoutListener(Landroid/view/ViewTreeObserver$OnGlobalLayoutListener;)V

    return-void
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
]
