TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/fragment/LocalePickerFragment.smali'
CLASS_FALLBACK_NAMES = ['LocalePickerFragment.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/fragment/BaseListFragment;', '.field private static final DURATION_SEARCH_VIEW_ANIMATION:I = 0x12c', '.field private static final PREF_SELECTED_LOCALE:Ljava/lang/String; = "pref_selected_locale"', '.field private static final TAG:Ljava/lang/String; = "LocalPickerFragment"']

PATCHES = [
    {
        'id': 'com_android_provision_fragment_LocalePickerFragment__onCreate',
        'method': '.method public onCreate(Landroid/os/Bundle;)V',
        'method_name': 'onCreate',
        'method_anchors': ['invoke-super {p0, p1}, Landroidx/fragment/app/Fragment;->onCreate(Landroid/os/Bundle;)V', 'invoke-static {}, Lmiui/os/MiuiInit;->getCustVariants()[Ljava/lang/String;', 'if-eqz p1, :cond_9', 'if-eqz v0, :cond_9', 'invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->getShowDefaultRegions()[Ljava/lang/String;', 'if-eqz v0, :cond_0', 'if-lez v1, :cond_0', 'if-ge v0, v1, :cond_1'],
        'type': 'policy_skip',
        'search': """.method public onCreate(Landroid/os/Bundle;)V
    .registers 7

    invoke-super {p0, p1}, Landroidx/fragment/app/Fragment;->onCreate(Landroid/os/Bundle;)V

    invoke-static {}, Lmiui/os/MiuiInit;->getCustVariants()[Ljava/lang/String;

    move-result-object p1

    if-eqz p1, :cond_9

    array-length v0, p1

    if-eqz v0, :cond_9

    invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->getShowDefaultRegions()[Ljava/lang/String;

    move-result-object v0

    if-eqz v0, :cond_0

    array-length v1, v0

    if-lez v1, :cond_0

    move-object p1, v0

    :cond_0
    const/4 v0, 0x0

    :goto_0
    array-length v1, p1

    if-ge v0, v1, :cond_1

    new-instance v1, Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;

    const/4 v2, 0x0

    invoke-direct {v1, p0, v2}, Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;-><init>(Lcom/android/provision/fragment/LocalePickerFragment;Lcom/android/provision/fragment/LocalePickerFragment-IA;)V

    aget-object v2, p1, v0

    iput-object v2, v1, Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;->countryCode:Ljava/lang/String;

    new-instance v2, Ljava/util/Locale;

    invoke-static {}, Ljava/util/Locale;->getDefault()Ljava/util/Locale;

    move-result-object v3

    invoke-virtual {v3}, Ljava/util/Locale;->getLanguage()Ljava/lang/String;

    move-result-object v3

    aget-object v4, p1, v0

    invoke-direct {v2, v3, v4}, Ljava/util/Locale;-><init>(Ljava/lang/String;Ljava/lang/String;)V

    invoke-virtual {v2}, Ljava/util/Locale;->getDisplayCountry()Ljava/lang/String;

    move-result-object v2

    invoke-direct {p0, v2}, Lcom/android/provision/fragment/LocalePickerFragment;->displayNameAdaptation(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v2

    iput-object v2, v1, Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;->displayName:Ljava/lang/String;

    iget-object v2, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mLocales:Ljava/util/ArrayList;

    invoke-virtual {v2, v1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    add-int/lit8 v0, v0, 0x1

    goto :goto_0

    :cond_1
    iget-object p1, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mLocales:Ljava/util/ArrayList;

    new-instance v0, Lcom/android/provision/fragment/LocalePickerFragment$AlphabetComparator;

    invoke-direct {v0, p0}, Lcom/android/provision/fragment/LocalePickerFragment$AlphabetComparator;-><init>(Lcom/android/provision/fragment/LocalePickerFragment;)V

    invoke-static {p1, v0}, Ljava/util/Collections;->sort(Ljava/util/List;Ljava/util/Comparator;)V

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p1

    invoke-static {p1}, Landroidx/preference/PreferenceManager;->getDefaultSharedPreferences(Landroid/content/Context;)Landroid/content/SharedPreferences;

    move-result-object p1

    const-string v0, "pref_selected_locale"

    const-string v1, ""

    invoke-interface {p1, v0, v1}, Landroid/content/SharedPreferences;->getString(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object p1

    iput-object p1, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mCountryCode:Ljava/lang/String;

    invoke-static {p1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result p1

    const/4 v0, 0x1

    if-nez p1, :cond_2

    iput-boolean v0, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mNextButtonEnabled:Z

    return-void

    :cond_2
    sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz p1, :cond_6

    invoke-static {}, Lcom/android/provision/Utils;->getLanguage()Ljava/lang/String;

    move-result-object p1

    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->getLastLanguage()Ljava/lang/String;

    move-result-object v1

    invoke-static {}, Lcom/android/provision/utils/MccHelper;->getInstance()Lcom/android/provision/utils/MccHelper;

    move-result-object v2

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v3

    invoke-virtual {v2, v3, p1}, Lcom/android/provision/utils/MccHelper;->initRecommendRegions(Landroid/content/Context;Ljava/lang/String;)V

    invoke-virtual {v1, p1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_3

    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->getLastLocale()Ljava/lang/String;

    move-result-object p1

    invoke-static {p1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v1

    if-nez v1, :cond_7

    iput-boolean v0, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mNextButtonEnabled:Z

    iput-object p1, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mCountryCode:Ljava/lang/String;

    return-void

    :cond_3
    invoke-static {}, Lcom/android/provision/Utils;->getRegion()Ljava/lang/String;

    move-result-object v1

    invoke-static {v1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v2

    if-nez v2, :cond_4

    iput-boolean v0, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mNextButtonEnabled:Z

    iput-object v1, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mCountryCode:Ljava/lang/String;

    goto :goto_1

    :cond_4
    invoke-static {}, Lcom/android/provision/utils/MccHelper;->getInstance()Lcom/android/provision/utils/MccHelper;

    move-result-object v1

    invoke-virtual {v1, p1}, Lcom/android/provision/utils/MccHelper;->getRecommendRegion(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    invoke-static {v1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v2

    if-nez v2, :cond_5

    iput-boolean v0, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mNextButtonEnabled:Z

    iput-object v1, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mCountryCode:Ljava/lang/String;

    :cond_5
    :goto_1
    iget-object p0, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mCountryCode:Ljava/lang/String;

    invoke-static {p0}, Lcom/android/provision/DefaultPreferenceHelper;->setLastLocale(Ljava/lang/String;)V

    invoke-static {p1}, Lcom/android/provision/DefaultPreferenceHelper;->setLastLanguage(Ljava/lang/String;)V

    return-void

    :cond_6
    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->getLastLocale()Ljava/lang/String;

    move-result-object p1

    invoke-static {p1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v1

    if-eqz v1, :cond_8

    invoke-static {}, Lcom/android/provision/Utils;->getRegion()Ljava/lang/String;

    move-result-object p1

    invoke-static {p1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v1

    if-nez v1, :cond_7

    iput-boolean v0, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mNextButtonEnabled:Z

    iput-object p1, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mCountryCode:Ljava/lang/String;

    :cond_7
    return-void

    :cond_8
    iput-boolean v0, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mNextButtonEnabled:Z

    iput-object p1, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mCountryCode:Ljava/lang/String;

    return-void

    :cond_9
    invoke-direct {p0}, Lcom/android/provision/fragment/LocalePickerFragment;->finishSetup()V

    return-void
.end method""",
        'replacement': """.method public onCreate(Landroid/os/Bundle;)V
    .registers 7

    invoke-super {p0, p1}, Landroidx/fragment/app/Fragment;->onCreate(Landroid/os/Bundle;)V

    invoke-static {}, Lmiui/os/MiuiInit;->getCustVariants()[Ljava/lang/String;

    move-result-object p1

    if-eqz p1, :cond_9

    array-length v0, p1

    if-eqz v0, :cond_9

    invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->getShowDefaultRegions()[Ljava/lang/String;

    move-result-object v0

    if-eqz v0, :cond_0

    array-length v1, v0

    if-lez v1, :cond_0

    move-object p1, v0

    :cond_0
    const/4 v0, 0x0

    :goto_0
    array-length v1, p1

    if-ge v0, v1, :cond_1

    new-instance v1, Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;

    const/4 v2, 0x0

    invoke-direct {v1, p0, v2}, Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;-><init>(Lcom/android/provision/fragment/LocalePickerFragment;Lcom/android/provision/fragment/LocalePickerFragment-IA;)V

    aget-object v2, p1, v0

    iput-object v2, v1, Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;->countryCode:Ljava/lang/String;

    new-instance v2, Ljava/util/Locale;

    invoke-static {}, Ljava/util/Locale;->getDefault()Ljava/util/Locale;

    move-result-object v3

    invoke-virtual {v3}, Ljava/util/Locale;->getLanguage()Ljava/lang/String;

    move-result-object v3

    aget-object v4, p1, v0

    invoke-direct {v2, v3, v4}, Ljava/util/Locale;-><init>(Ljava/lang/String;Ljava/lang/String;)V

    invoke-virtual {v2}, Ljava/util/Locale;->getDisplayCountry()Ljava/lang/String;

    move-result-object v2

    invoke-direct {p0, v2}, Lcom/android/provision/fragment/LocalePickerFragment;->displayNameAdaptation(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v2

    iput-object v2, v1, Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;->displayName:Ljava/lang/String;

    iget-object v2, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mLocales:Ljava/util/ArrayList;

    invoke-virtual {v2, v1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    add-int/lit8 v0, v0, 0x1

    goto :goto_0

    :cond_1
    iget-object p1, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mLocales:Ljava/util/ArrayList;

    new-instance v0, Lcom/android/provision/fragment/LocalePickerFragment$AlphabetComparator;

    invoke-direct {v0, p0}, Lcom/android/provision/fragment/LocalePickerFragment$AlphabetComparator;-><init>(Lcom/android/provision/fragment/LocalePickerFragment;)V

    invoke-static {p1, v0}, Ljava/util/Collections;->sort(Ljava/util/List;Ljava/util/Comparator;)V

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p1

    invoke-static {p1}, Landroidx/preference/PreferenceManager;->getDefaultSharedPreferences(Landroid/content/Context;)Landroid/content/SharedPreferences;

    move-result-object p1

    const-string v0, "pref_selected_locale"

    const-string v1, ""

    invoke-interface {p1, v0, v1}, Landroid/content/SharedPreferences;->getString(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object p1

    iput-object p1, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mCountryCode:Ljava/lang/String;

    invoke-static {p1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result p1

    const/4 v0, 0x1

    if-nez p1, :cond_2

    iput-boolean v0, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mNextButtonEnabled:Z

    return-void

    :cond_2
    sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz p1, :cond_6

    invoke-static {}, Lcom/android/provision/Utils;->getLanguage()Ljava/lang/String;

    move-result-object p1

    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->getLastLanguage()Ljava/lang/String;

    move-result-object v1

    invoke-static {}, Lcom/android/provision/utils/MccHelper;->getInstance()Lcom/android/provision/utils/MccHelper;

    move-result-object v2

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v3

    invoke-virtual {v2, v3, p1}, Lcom/android/provision/utils/MccHelper;->initRecommendRegions(Landroid/content/Context;Ljava/lang/String;)V

    invoke-virtual {v1, p1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_3

    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->getLastLocale()Ljava/lang/String;

    move-result-object p1

    invoke-static {p1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v1

    if-nez v1, :cond_7

    iput-boolean v0, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mNextButtonEnabled:Z

    iput-object p1, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mCountryCode:Ljava/lang/String;

    return-void

    :cond_3
    invoke-static {}, Lcom/android/provision/Utils;->getRegion()Ljava/lang/String;

    move-result-object v1

    invoke-static {v1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v2

    if-nez v2, :cond_4

    iput-boolean v0, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mNextButtonEnabled:Z

    iput-object v1, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mCountryCode:Ljava/lang/String;

    goto :goto_1

    :cond_4
    invoke-static {}, Lcom/android/provision/utils/MccHelper;->getInstance()Lcom/android/provision/utils/MccHelper;

    move-result-object v1

    invoke-virtual {v1, p1}, Lcom/android/provision/utils/MccHelper;->getRecommendRegion(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    invoke-static {v1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v2

    if-nez v2, :cond_5

    iput-boolean v0, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mNextButtonEnabled:Z

    iput-object v1, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mCountryCode:Ljava/lang/String;

    :cond_5
    :goto_1
    iget-object p0, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mCountryCode:Ljava/lang/String;

    invoke-static {p0}, Lcom/android/provision/DefaultPreferenceHelper;->setLastLocale(Ljava/lang/String;)V

    invoke-static {p1}, Lcom/android/provision/DefaultPreferenceHelper;->setLastLanguage(Ljava/lang/String;)V

    return-void

    :cond_6
    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->getLastLocale()Ljava/lang/String;

    move-result-object p1

    invoke-static {p1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v1

    if-eqz v1, :cond_8

    invoke-static {}, Lcom/android/provision/Utils;->getRegion()Ljava/lang/String;

    move-result-object p1

    invoke-static {p1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v1

    if-nez v1, :cond_7

    iput-boolean v0, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mNextButtonEnabled:Z

    iput-object p1, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mCountryCode:Ljava/lang/String;

    :cond_7
    return-void

    :cond_8
    iput-boolean v0, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mNextButtonEnabled:Z

    iput-object p1, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mCountryCode:Ljava/lang/String;

    return-void

    :cond_9
    invoke-direct {p0}, Lcom/android/provision/fragment/LocalePickerFragment;->finishSetup()V

    return-void
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_fragment_LocalePickerFragment__onViewCreated',
        'method': '.method public onViewCreated(Landroid/view/View;Landroid/os/Bundle;)V',
        'method_name': 'onViewCreated',
        'method_anchors': ['invoke-super {p0, p1, p2}, Landroidx/fragment/app/ListFragment;->onViewCreated(Landroid/view/View;Landroid/os/Bundle;)V', 'invoke-virtual {p1, p2}, Landroid/view/View;->findViewById(I)Landroid/view/View;', 'check-cast p2, Landroid/widget/ListView;', 'iput-object p2, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mListView:Landroid/widget/ListView;', 'new-instance v0, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;', 'iget-object v2, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mActivity:Landroid/app/Activity;', 'sget v3, Lcom/android/provision/R$layout;->local_list_item_view:I', 'sget v4, Lcom/android/provision/R$id;->item_view:I'],
        'type': 'policy_skip',
        'search': """.method public onViewCreated(Landroid/view/View;Landroid/os/Bundle;)V
    .registers 9

    invoke-super {p0, p1, p2}, Landroidx/fragment/app/ListFragment;->onViewCreated(Landroid/view/View;Landroid/os/Bundle;)V

    const p2, 0x102000a

    invoke-virtual {p1, p2}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object p2

    check-cast p2, Landroid/widget/ListView;

    iput-object p2, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mListView:Landroid/widget/ListView;

    new-instance v0, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;

    iget-object v2, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mActivity:Landroid/app/Activity;

    sget v3, Lcom/android/provision/R$layout;->local_list_item_view:I

    sget v4, Lcom/android/provision/R$id;->item_view:I

    iget-object v5, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mLocales:Ljava/util/ArrayList;

    move-object v1, p0

    invoke-direct/range {v0 .. v5}, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;-><init>(Lcom/android/provision/fragment/LocalePickerFragment;Landroid/content/Context;IILjava/util/List;)V

    iput-object v0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mLocalesAdapter:Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;

    iget-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mListView:Landroid/widget/ListView;

    invoke-virtual {p0, v0}, Landroid/widget/ListView;->setAdapter(Landroid/widget/ListAdapter;)V

    iget-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mListView:Landroid/widget/ListView;

    iget-object p2, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mOnItemClickListener:Landroid/widget/AdapterView$OnItemClickListener;

    invoke-virtual {p0, p2}, Landroid/widget/ListView;->setOnItemClickListener(Landroid/widget/AdapterView$OnItemClickListener;)V

    iget-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mListView:Landroid/widget/ListView;

    iget-object p2, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mOnTouchListener:Landroid/view/View$OnTouchListener;

    invoke-virtual {p0, p2}, Landroid/widget/ListView;->setOnTouchListener(Landroid/view/View$OnTouchListener;)V

    iget-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mListView:Landroid/widget/ListView;

    const/4 p2, 0x2

    invoke-virtual {p0, p2}, Landroid/widget/ListView;->setOverScrollMode(I)V

    invoke-virtual {v1}, Landroidx/fragment/app/Fragment;->getView()Landroid/view/View;

    move-result-object p0

    if-eqz p0, :cond_0

    invoke-direct {v1}, Lcom/android/provision/fragment/LocalePickerFragment;->scrollToCurrentLocation()V

    :cond_0
    invoke-virtual {v1}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p0

    if-nez p0, :cond_1

    goto :goto_0

    :cond_1
    invoke-virtual {v1}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p0

    invoke-static {p0}, Lcom/android/provision/Utils;->getNextView(Landroid/app/Activity;)Landroid/widget/Button;

    move-result-object p0

    iput-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mNext:Landroid/view/View;

    iget-boolean p2, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mNextButtonEnabled:Z

    invoke-virtual {p0, p2}, Landroid/view/View;->setEnabled(Z)V

    iget-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mNext:Landroid/view/View;

    new-instance p2, Lcom/android/provision/fragment/LocalePickerFragment$1;

    invoke-direct {p2, v1}, Lcom/android/provision/fragment/LocalePickerFragment$1;-><init>(Lcom/android/provision/fragment/LocalePickerFragment;)V

    invoke-virtual {p0, p2}, Landroid/view/View;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz p0, :cond_2

    new-instance p0, Lcom/android/provision/fragment/LocalePickerFragment$SearchTouchListener;

    invoke-direct {p0, v1}, Lcom/android/provision/fragment/LocalePickerFragment$SearchTouchListener;-><init>(Lcom/android/provision/fragment/LocalePickerFragment;)V

    iput-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mTouchListener:Lcom/android/provision/fragment/LocalePickerFragment$SearchTouchListener;

    sget p0, Lcom/android/provision/R$id;->root_view:I

    invoke-virtual {p1, p0}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object p0

    check-cast p0, Landroid/view/ViewGroup;

    iput-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mRoot:Landroid/view/ViewGroup;

    iget-object p2, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mTouchListener:Lcom/android/provision/fragment/LocalePickerFragment$SearchTouchListener;

    invoke-virtual {p0, p2}, Landroid/view/ViewGroup;->setOnTouchListener(Landroid/view/View$OnTouchListener;)V

    sget p0, Lcom/android/provision/R$id;->transparent_cover:I

    invoke-virtual {p1, p0}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object p0

    iput-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mTransparentCover:Landroid/view/View;

    sget p0, Lcom/android/provision/R$id;->page_layout:I

    invoke-virtual {p1, p0}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object p0

    check-cast p0, Landroid/view/ViewGroup;

    iput-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mPageView:Landroid/view/ViewGroup;

    new-instance p0, Lcom/android/provision/fragment/LocalePickerFragment$SearchFocusChangeListener;

    invoke-direct {p0, v1}, Lcom/android/provision/fragment/LocalePickerFragment$SearchFocusChangeListener;-><init>(Lcom/android/provision/fragment/LocalePickerFragment;)V

    iput-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mSearchFocuChangeListener:Lcom/android/provision/fragment/LocalePickerFragment$SearchFocusChangeListener;

    new-instance p0, Lcom/android/provision/fragment/LocalePickerFragment$SearchTextWatcher;

    invoke-direct {p0, v1}, Lcom/android/provision/fragment/LocalePickerFragment$SearchTextWatcher;-><init>(Lcom/android/provision/fragment/LocalePickerFragment;)V

    iput-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mSearchTextWatcher:Lcom/android/provision/fragment/LocalePickerFragment$SearchTextWatcher;

    new-instance p0, Lcom/android/provision/fragment/LocalePickerFragment$SeachEditTextBackkeyListener;

    invoke-direct {p0, v1}, Lcom/android/provision/fragment/LocalePickerFragment$SeachEditTextBackkeyListener;-><init>(Lcom/android/provision/fragment/LocalePickerFragment;)V

    iput-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mBackKeyListener:Lcom/android/provision/fragment/LocalePickerFragment$SeachEditTextBackkeyListener;

    sget p0, Lcom/android/provision/R$id;->search_view:I

    invoke-virtual {p1, p0}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object p0

    iput-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mSearchView:Landroid/view/View;

    const/4 p1, 0x0

    invoke-virtual {p0, p1}, Landroid/view/View;->setVisibility(I)V

    iget-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mSearchView:Landroid/view/View;

    sget p1, Lcom/android/provision/R$id;->search_input:I

    invoke-virtual {p0, p1}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object p0

    check-cast p0, Lsrc/com/android/provision/widget/SearchEditText;

    iput-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mSearchInputView:Lsrc/com/android/provision/widget/SearchEditText;

    iget-object p1, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mSearchFocuChangeListener:Lcom/android/provision/fragment/LocalePickerFragment$SearchFocusChangeListener;

    invoke-virtual {p0, p1}, Landroid/widget/EditText;->setOnFocusChangeListener(Landroid/view/View$OnFocusChangeListener;)V

    iget-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mSearchInputView:Lsrc/com/android/provision/widget/SearchEditText;

    iget-object p1, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mSearchTextWatcher:Lcom/android/provision/fragment/LocalePickerFragment$SearchTextWatcher;

    invoke-virtual {p0, p1}, Landroid/widget/EditText;->addTextChangedListener(Landroid/text/TextWatcher;)V

    iget-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mSearchInputView:Lsrc/com/android/provision/widget/SearchEditText;

    iget-object p1, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mBackKeyListener:Lcom/android/provision/fragment/LocalePickerFragment$SeachEditTextBackkeyListener;

    invoke-virtual {p0, p1}, Lsrc/com/android/provision/widget/SearchEditText;->addBackKeyListener(Lsrc/com/android/provision/widget/SearchEditText$OnEditTextBackKeyListener;)V

    iget-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mSearchView:Landroid/view/View;

    sget p1, Lcom/android/provision/R$id;->search_container:I

    invoke-virtual {p0, p1}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object p0

    check-cast p0, Landroid/view/ViewGroup;

    iput-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mSearchContainer:Landroid/view/ViewGroup;

    new-instance p1, Lcom/android/provision/fragment/LocalePickerFragment$SearchAnimatorUpdateListener;

    invoke-direct {p1, p0}, Lcom/android/provision/fragment/LocalePickerFragment$SearchAnimatorUpdateListener;-><init>(Landroid/view/ViewGroup;)V

    iput-object p1, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mSearchAnimatorUpdateListener:Lcom/android/provision/fragment/LocalePickerFragment$SearchAnimatorUpdateListener;

    new-instance p0, Lcom/android/provision/fragment/LocalePickerFragment$LayoutAnimatorListener;

    iget-object p1, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mPageView:Landroid/view/ViewGroup;

    invoke-direct {p0, v1, p1}, Lcom/android/provision/fragment/LocalePickerFragment$LayoutAnimatorListener;-><init>(Lcom/android/provision/fragment/LocalePickerFragment;Landroid/view/ViewGroup;)V

    iput-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mLayoutAnimatorListener:Lcom/android/provision/fragment/LocalePickerFragment$LayoutAnimatorListener;

    :cond_2
    :goto_0
    return-void
.end method""",
        'replacement': """.method public onViewCreated(Landroid/view/View;Landroid/os/Bundle;)V
    .registers 9

    invoke-super {p0, p1, p2}, Landroidx/fragment/app/ListFragment;->onViewCreated(Landroid/view/View;Landroid/os/Bundle;)V

    const p2, 0x102000a

    invoke-virtual {p1, p2}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object p2

    check-cast p2, Landroid/widget/ListView;

    iput-object p2, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mListView:Landroid/widget/ListView;

    new-instance v0, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;

    iget-object v2, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mActivity:Landroid/app/Activity;

    sget v3, Lcom/android/provision/R$layout;->local_list_item_view:I

    sget v4, Lcom/android/provision/R$id;->item_view:I

    iget-object v5, p0, Lcom/android/provision/fragment/LocalePickerFragment;->mLocales:Ljava/util/ArrayList;

    move-object v1, p0

    invoke-direct/range {v0 .. v5}, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;-><init>(Lcom/android/provision/fragment/LocalePickerFragment;Landroid/content/Context;IILjava/util/List;)V

    iput-object v0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mLocalesAdapter:Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;

    iget-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mListView:Landroid/widget/ListView;

    invoke-virtual {p0, v0}, Landroid/widget/ListView;->setAdapter(Landroid/widget/ListAdapter;)V

    iget-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mListView:Landroid/widget/ListView;

    iget-object p2, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mOnItemClickListener:Landroid/widget/AdapterView$OnItemClickListener;

    invoke-virtual {p0, p2}, Landroid/widget/ListView;->setOnItemClickListener(Landroid/widget/AdapterView$OnItemClickListener;)V

    iget-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mListView:Landroid/widget/ListView;

    iget-object p2, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mOnTouchListener:Landroid/view/View$OnTouchListener;

    invoke-virtual {p0, p2}, Landroid/widget/ListView;->setOnTouchListener(Landroid/view/View$OnTouchListener;)V

    iget-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mListView:Landroid/widget/ListView;

    const/4 p2, 0x2

    invoke-virtual {p0, p2}, Landroid/widget/ListView;->setOverScrollMode(I)V

    invoke-virtual {v1}, Landroidx/fragment/app/Fragment;->getView()Landroid/view/View;

    move-result-object p0

    if-eqz p0, :cond_0

    invoke-direct {v1}, Lcom/android/provision/fragment/LocalePickerFragment;->scrollToCurrentLocation()V

    :cond_0
    invoke-virtual {v1}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p0

    if-nez p0, :cond_1

    goto :goto_0

    :cond_1
    invoke-virtual {v1}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p0

    invoke-static {p0}, Lcom/android/provision/Utils;->getNextView(Landroid/app/Activity;)Landroid/widget/Button;

    move-result-object p0

    iput-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mNext:Landroid/view/View;

    iget-boolean p2, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mNextButtonEnabled:Z

    invoke-virtual {p0, p2}, Landroid/view/View;->setEnabled(Z)V

    iget-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mNext:Landroid/view/View;

    new-instance p2, Lcom/android/provision/fragment/LocalePickerFragment$1;

    invoke-direct {p2, v1}, Lcom/android/provision/fragment/LocalePickerFragment$1;-><init>(Lcom/android/provision/fragment/LocalePickerFragment;)V

    invoke-virtual {p0, p2}, Landroid/view/View;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz p0, :cond_2

    new-instance p0, Lcom/android/provision/fragment/LocalePickerFragment$SearchTouchListener;

    invoke-direct {p0, v1}, Lcom/android/provision/fragment/LocalePickerFragment$SearchTouchListener;-><init>(Lcom/android/provision/fragment/LocalePickerFragment;)V

    iput-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mTouchListener:Lcom/android/provision/fragment/LocalePickerFragment$SearchTouchListener;

    sget p0, Lcom/android/provision/R$id;->root_view:I

    invoke-virtual {p1, p0}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object p0

    check-cast p0, Landroid/view/ViewGroup;

    iput-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mRoot:Landroid/view/ViewGroup;

    iget-object p2, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mTouchListener:Lcom/android/provision/fragment/LocalePickerFragment$SearchTouchListener;

    invoke-virtual {p0, p2}, Landroid/view/ViewGroup;->setOnTouchListener(Landroid/view/View$OnTouchListener;)V

    sget p0, Lcom/android/provision/R$id;->transparent_cover:I

    invoke-virtual {p1, p0}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object p0

    iput-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mTransparentCover:Landroid/view/View;

    sget p0, Lcom/android/provision/R$id;->page_layout:I

    invoke-virtual {p1, p0}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object p0

    check-cast p0, Landroid/view/ViewGroup;

    iput-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mPageView:Landroid/view/ViewGroup;

    new-instance p0, Lcom/android/provision/fragment/LocalePickerFragment$SearchFocusChangeListener;

    invoke-direct {p0, v1}, Lcom/android/provision/fragment/LocalePickerFragment$SearchFocusChangeListener;-><init>(Lcom/android/provision/fragment/LocalePickerFragment;)V

    iput-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mSearchFocuChangeListener:Lcom/android/provision/fragment/LocalePickerFragment$SearchFocusChangeListener;

    new-instance p0, Lcom/android/provision/fragment/LocalePickerFragment$SearchTextWatcher;

    invoke-direct {p0, v1}, Lcom/android/provision/fragment/LocalePickerFragment$SearchTextWatcher;-><init>(Lcom/android/provision/fragment/LocalePickerFragment;)V

    iput-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mSearchTextWatcher:Lcom/android/provision/fragment/LocalePickerFragment$SearchTextWatcher;

    new-instance p0, Lcom/android/provision/fragment/LocalePickerFragment$SeachEditTextBackkeyListener;

    invoke-direct {p0, v1}, Lcom/android/provision/fragment/LocalePickerFragment$SeachEditTextBackkeyListener;-><init>(Lcom/android/provision/fragment/LocalePickerFragment;)V

    iput-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mBackKeyListener:Lcom/android/provision/fragment/LocalePickerFragment$SeachEditTextBackkeyListener;

    sget p0, Lcom/android/provision/R$id;->search_view:I

    invoke-virtual {p1, p0}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object p0

    iput-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mSearchView:Landroid/view/View;

    const/4 p1, 0x0

    invoke-virtual {p0, p1}, Landroid/view/View;->setVisibility(I)V

    iget-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mSearchView:Landroid/view/View;

    sget p1, Lcom/android/provision/R$id;->search_input:I

    invoke-virtual {p0, p1}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object p0

    check-cast p0, Lsrc/com/android/provision/widget/SearchEditText;

    iput-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mSearchInputView:Lsrc/com/android/provision/widget/SearchEditText;

    iget-object p1, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mSearchFocuChangeListener:Lcom/android/provision/fragment/LocalePickerFragment$SearchFocusChangeListener;

    invoke-virtual {p0, p1}, Landroid/widget/EditText;->setOnFocusChangeListener(Landroid/view/View$OnFocusChangeListener;)V

    iget-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mSearchInputView:Lsrc/com/android/provision/widget/SearchEditText;

    iget-object p1, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mSearchTextWatcher:Lcom/android/provision/fragment/LocalePickerFragment$SearchTextWatcher;

    invoke-virtual {p0, p1}, Landroid/widget/EditText;->addTextChangedListener(Landroid/text/TextWatcher;)V

    iget-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mSearchInputView:Lsrc/com/android/provision/widget/SearchEditText;

    iget-object p1, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mBackKeyListener:Lcom/android/provision/fragment/LocalePickerFragment$SeachEditTextBackkeyListener;

    invoke-virtual {p0, p1}, Lsrc/com/android/provision/widget/SearchEditText;->addBackKeyListener(Lsrc/com/android/provision/widget/SearchEditText$OnEditTextBackKeyListener;)V

    iget-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mSearchView:Landroid/view/View;

    sget p1, Lcom/android/provision/R$id;->search_container:I

    invoke-virtual {p0, p1}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object p0

    check-cast p0, Landroid/view/ViewGroup;

    iput-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mSearchContainer:Landroid/view/ViewGroup;

    new-instance p1, Lcom/android/provision/fragment/LocalePickerFragment$SearchAnimatorUpdateListener;

    invoke-direct {p1, p0}, Lcom/android/provision/fragment/LocalePickerFragment$SearchAnimatorUpdateListener;-><init>(Landroid/view/ViewGroup;)V

    iput-object p1, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mSearchAnimatorUpdateListener:Lcom/android/provision/fragment/LocalePickerFragment$SearchAnimatorUpdateListener;

    new-instance p0, Lcom/android/provision/fragment/LocalePickerFragment$LayoutAnimatorListener;

    iget-object p1, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mPageView:Landroid/view/ViewGroup;

    invoke-direct {p0, v1, p1}, Lcom/android/provision/fragment/LocalePickerFragment$LayoutAnimatorListener;-><init>(Lcom/android/provision/fragment/LocalePickerFragment;Landroid/view/ViewGroup;)V

    iput-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment;->mLayoutAnimatorListener:Lcom/android/provision/fragment/LocalePickerFragment$LayoutAnimatorListener;

    :cond_2
    :goto_0
    return-void
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
]
