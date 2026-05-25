TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/fragment/LocalePickerFragment$LocalesAdapter.smali'
CLASS_FALLBACK_NAMES = ['LocalePickerFragment$LocalesAdapter.smali']
CLASS_ANCHORS = ['.super Landroid/widget/ArrayAdapter;']

PATCHES = [
    {
        'id': 'com_android_provision_fragment_LocalePickerFragment__LocalesAdapter__classifyLocales',
        'method': '.method private classifyLocales(Landroid/content/Context;Ljava/util/List;)V',
        'method_name': 'classifyLocales',
        'method_anchors': ['if-eqz p2, :cond_8', 'invoke-interface {p2}, Ljava/util/List;->size()I', 'if-gtz v0, :cond_0', 'sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_1', 'invoke-static {}, Lcom/android/provision/utils/MccHelper;->getInstance()Lcom/android/provision/utils/MccHelper;', 'invoke-virtual {v0}, Lcom/android/provision/utils/MccHelper;->getRecommendRegions()[Ljava/lang/String;', 'iget-object v0, p0, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;->this$0:Lcom/android/provision/fragment/LocalePickerFragment;'],
        'type': 'policy_skip',
        'search': """.method private classifyLocales(Landroid/content/Context;Ljava/util/List;)V
    .registers 10
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Landroid/content/Context;",
            "Ljava/util/List<",
            "Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;",
            ">;)V"
        }
    .end annotation

    if-eqz p2, :cond_8

    invoke-interface {p2}, Ljava/util/List;->size()I

    move-result v0

    if-gtz v0, :cond_0

    goto :goto_4

    :cond_0
    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_1

    invoke-static {}, Lcom/android/provision/utils/MccHelper;->getInstance()Lcom/android/provision/utils/MccHelper;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/provision/utils/MccHelper;->getRecommendRegions()[Ljava/lang/String;

    move-result-object v0

    goto :goto_0

    :cond_1
    iget-object v0, p0, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;->this$0:Lcom/android/provision/fragment/LocalePickerFragment;

    invoke-virtual {v0}, Landroidx/fragment/app/Fragment;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    sget v1, Lcom/android/provision/R$array;->popular_locales:I

    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getStringArray(I)[Ljava/lang/String;

    move-result-object v0

    :goto_0
    if-eqz v0, :cond_8

    array-length v1, v0

    if-gtz v1, :cond_2

    goto :goto_4

    :cond_2
    invoke-interface {p2}, Ljava/util/List;->size()I

    move-result v1

    array-length v2, v0

    if-ge v1, v2, :cond_3

    goto :goto_4

    :cond_3
    const/4 v1, 0x0

    move v2, v1

    :goto_1
    invoke-interface {p2}, Ljava/util/List;->size()I

    move-result v3

    if-ge v2, v3, :cond_7

    invoke-interface {p2, v2}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v3

    check-cast v3, Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;

    if-nez v3, :cond_4

    goto :goto_3

    :cond_4
    array-length v4, v0

    add-int/2addr v4, v2

    iput v4, v3, Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;->displayOrder:I

    move v4, v1

    :goto_2
    array-length v5, v0

    if-ge v4, v5, :cond_6

    aget-object v5, v0, v4

    invoke-static {v5}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v5

    if-nez v5, :cond_5

    aget-object v5, v0, v4

    iget-object v6, v3, Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;->countryCode:Ljava/lang/String;

    invoke-virtual {v5, v6}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result v5

    if-eqz v5, :cond_5

    iput v4, v3, Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;->displayOrder:I

    :cond_5
    add-int/lit8 v4, v4, 0x1

    goto :goto_2

    :cond_6
    :goto_3
    add-int/lit8 v2, v2, 0x1

    goto :goto_1

    :cond_7
    new-instance v1, Lcom/android/provision/fragment/LocalePickerFragment$PopularLocaleComparator;

    iget-object v2, p0, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;->this$0:Lcom/android/provision/fragment/LocalePickerFragment;

    const/4 v3, 0x0

    invoke-direct {v1, v2, v3}, Lcom/android/provision/fragment/LocalePickerFragment$PopularLocaleComparator;-><init>(Lcom/android/provision/fragment/LocalePickerFragment;Lcom/android/provision/fragment/LocalePickerFragment-IA;)V

    invoke-static {p2, v1}, Ljava/util/Collections;->sort(Ljava/util/List;Ljava/util/Comparator;)V

    new-instance v1, Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;

    iget-object p0, p0, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;->this$0:Lcom/android/provision/fragment/LocalePickerFragment;

    invoke-direct {v1, p0, v3}, Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;-><init>(Lcom/android/provision/fragment/LocalePickerFragment;Lcom/android/provision/fragment/LocalePickerFragment-IA;)V

    invoke-virtual {p1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object p0

    sget p1, Lcom/android/provision/R$string;->locale_picker_other_locale_title:I

    invoke-virtual {p0, p1}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object p0

    iput-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;->displayName:Ljava/lang/String;

    array-length p0, v0

    invoke-interface {p2, p0, v1}, Ljava/util/List;->add(ILjava/lang/Object;)V

    :cond_8
    :goto_4
    return-void
.end method""",
        'replacement': """.method private classifyLocales(Landroid/content/Context;Ljava/util/List;)V
    .registers 10
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Landroid/content/Context;",
            "Ljava/util/List<",
            "Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;",
            ">;)V"
        }
    .end annotation

    if-eqz p2, :cond_8

    invoke-interface {p2}, Ljava/util/List;->size()I

    move-result v0

    if-gtz v0, :cond_0

    goto :goto_4

    :cond_0
    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_1

    invoke-static {}, Lcom/android/provision/utils/MccHelper;->getInstance()Lcom/android/provision/utils/MccHelper;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/provision/utils/MccHelper;->getRecommendRegions()[Ljava/lang/String;

    move-result-object v0

    goto :goto_0

    :cond_1
    iget-object v0, p0, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;->this$0:Lcom/android/provision/fragment/LocalePickerFragment;

    invoke-virtual {v0}, Landroidx/fragment/app/Fragment;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    sget v1, Lcom/android/provision/R$array;->popular_locales:I

    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getStringArray(I)[Ljava/lang/String;

    move-result-object v0

    :goto_0
    if-eqz v0, :cond_8

    array-length v1, v0

    if-gtz v1, :cond_2

    goto :goto_4

    :cond_2
    invoke-interface {p2}, Ljava/util/List;->size()I

    move-result v1

    array-length v2, v0

    if-ge v1, v2, :cond_3

    goto :goto_4

    :cond_3
    const/4 v1, 0x0

    move v2, v1

    :goto_1
    invoke-interface {p2}, Ljava/util/List;->size()I

    move-result v3

    if-ge v2, v3, :cond_7

    invoke-interface {p2, v2}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v3

    check-cast v3, Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;

    if-nez v3, :cond_4

    goto :goto_3

    :cond_4
    array-length v4, v0

    add-int/2addr v4, v2

    iput v4, v3, Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;->displayOrder:I

    move v4, v1

    :goto_2
    array-length v5, v0

    if-ge v4, v5, :cond_6

    aget-object v5, v0, v4

    invoke-static {v5}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v5

    if-nez v5, :cond_5

    aget-object v5, v0, v4

    iget-object v6, v3, Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;->countryCode:Ljava/lang/String;

    invoke-virtual {v5, v6}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result v5

    if-eqz v5, :cond_5

    iput v4, v3, Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;->displayOrder:I

    :cond_5
    add-int/lit8 v4, v4, 0x1

    goto :goto_2

    :cond_6
    :goto_3
    add-int/lit8 v2, v2, 0x1

    goto :goto_1

    :cond_7
    new-instance v1, Lcom/android/provision/fragment/LocalePickerFragment$PopularLocaleComparator;

    iget-object v2, p0, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;->this$0:Lcom/android/provision/fragment/LocalePickerFragment;

    const/4 v3, 0x0

    invoke-direct {v1, v2, v3}, Lcom/android/provision/fragment/LocalePickerFragment$PopularLocaleComparator;-><init>(Lcom/android/provision/fragment/LocalePickerFragment;Lcom/android/provision/fragment/LocalePickerFragment-IA;)V

    invoke-static {p2, v1}, Ljava/util/Collections;->sort(Ljava/util/List;Ljava/util/Comparator;)V

    new-instance v1, Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;

    iget-object p0, p0, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;->this$0:Lcom/android/provision/fragment/LocalePickerFragment;

    invoke-direct {v1, p0, v3}, Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;-><init>(Lcom/android/provision/fragment/LocalePickerFragment;Lcom/android/provision/fragment/LocalePickerFragment-IA;)V

    invoke-virtual {p1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object p0

    sget p1, Lcom/android/provision/R$string;->locale_picker_other_locale_title:I

    invoke-virtual {p0, p1}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object p0

    iput-object p0, v1, Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;->displayName:Ljava/lang/String;

    array-length p0, v0

    invoke-interface {p2, p0, v1}, Ljava/util/List;->add(ILjava/lang/Object;)V

    :cond_8
    :goto_4
    return-void
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_fragment_LocalePickerFragment__LocalesAdapter__init',
        'method': '.method public constructor <init>(Lcom/android/provision/fragment/LocalePickerFragment;Landroid/content/Context;IILjava/util/List;)V',
        'method_name': '<init>',
        'method_anchors': ['iput-object p1, p0, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;->this$0:Lcom/android/provision/fragment/LocalePickerFragment;', 'invoke-direct {p0, p2, p3, p4, p5}, Landroid/widget/ArrayAdapter;-><init>(Landroid/content/Context;IILjava/util/List;)V', 'sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz p1, :cond_1', 'invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->getShowDefaultRegions()[Ljava/lang/String;', 'if-eqz p1, :cond_0', 'if-nez p1, :cond_1', 'invoke-direct {p0, p2, p5}, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;->classifyLocales(Landroid/content/Context;Ljava/util/List;)V'],
        'type': 'policy_skip',
        'search': """.method public constructor <init>(Lcom/android/provision/fragment/LocalePickerFragment;Landroid/content/Context;IILjava/util/List;)V
    .registers 6
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Landroid/content/Context;",
            "II",
            "Ljava/util/List<",
            "Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;",
            ">;)V"
        }
    .end annotation

    iput-object p1, p0, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;->this$0:Lcom/android/provision/fragment/LocalePickerFragment;

    invoke-direct {p0, p2, p3, p4, p5}, Landroid/widget/ArrayAdapter;-><init>(Landroid/content/Context;IILjava/util/List;)V

    sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz p1, :cond_1

    invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->getShowDefaultRegions()[Ljava/lang/String;

    move-result-object p1

    if-eqz p1, :cond_0

    array-length p1, p1

    if-nez p1, :cond_1

    :cond_0
    invoke-direct {p0, p2, p5}, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;->classifyLocales(Landroid/content/Context;Ljava/util/List;)V

    :cond_1
    iput-object p5, p0, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;->mLocales:Ljava/util/List;

    return-void
.end method""",
        'replacement': """.method public constructor <init>(Lcom/android/provision/fragment/LocalePickerFragment;Landroid/content/Context;IILjava/util/List;)V
    .registers 6
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Landroid/content/Context;",
            "II",
            "Ljava/util/List<",
            "Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;",
            ">;)V"
        }
    .end annotation

    iput-object p1, p0, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;->this$0:Lcom/android/provision/fragment/LocalePickerFragment;

    invoke-direct {p0, p2, p3, p4, p5}, Landroid/widget/ArrayAdapter;-><init>(Landroid/content/Context;IILjava/util/List;)V

    sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz p1, :cond_1

    invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->getShowDefaultRegions()[Ljava/lang/String;

    move-result-object p1

    if-eqz p1, :cond_0

    array-length p1, p1

    if-nez p1, :cond_1

    :cond_0
    invoke-direct {p0, p2, p5}, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;->classifyLocales(Landroid/content/Context;Ljava/util/List;)V

    :cond_1
    iput-object p5, p0, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;->mLocales:Ljava/util/List;

    return-void
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_fragment_LocalePickerFragment__LocalesAdapter__getFilter',
        'method': '.method public getFilter()Landroid/widget/Filter;',
        'method_name': 'getFilter',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_1', 'iget-object v0, p0, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;->mFilter:Landroid/widget/Filter;', 'if-nez v0, :cond_0', 'new-instance v0, Lcom/android/provision/fragment/LocalePickerFragment$SearchFilter;', 'iget-object v1, p0, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;->mLocales:Ljava/util/List;', 'invoke-direct {v0, p0, v1}, Lcom/android/provision/fragment/LocalePickerFragment$SearchFilter;-><init>(Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;Ljava/util/List;)V', 'iput-object v0, p0, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;->mFilter:Landroid/widget/Filter;'],
        'type': 'policy_skip',
        'search': """.method public getFilter()Landroid/widget/Filter;
    .registers 3

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_1

    iget-object v0, p0, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;->mFilter:Landroid/widget/Filter;

    if-nez v0, :cond_0

    new-instance v0, Lcom/android/provision/fragment/LocalePickerFragment$SearchFilter;

    iget-object v1, p0, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;->mLocales:Ljava/util/List;

    invoke-direct {v0, p0, v1}, Lcom/android/provision/fragment/LocalePickerFragment$SearchFilter;-><init>(Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;Ljava/util/List;)V

    iput-object v0, p0, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;->mFilter:Landroid/widget/Filter;

    :cond_0
    iget-object p0, p0, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;->mFilter:Landroid/widget/Filter;

    return-object p0

    :cond_1
    const/4 p0, 0x0

    return-object p0
.end method""",
        'replacement': """.method public getFilter()Landroid/widget/Filter;
    .registers 3

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_1

    iget-object v0, p0, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;->mFilter:Landroid/widget/Filter;

    if-nez v0, :cond_0

    new-instance v0, Lcom/android/provision/fragment/LocalePickerFragment$SearchFilter;

    iget-object v1, p0, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;->mLocales:Ljava/util/List;

    invoke-direct {v0, p0, v1}, Lcom/android/provision/fragment/LocalePickerFragment$SearchFilter;-><init>(Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;Ljava/util/List;)V

    iput-object v0, p0, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;->mFilter:Landroid/widget/Filter;

    :cond_0
    iget-object p0, p0, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;->mFilter:Landroid/widget/Filter;

    return-object p0

    :cond_1
    const/4 p0, 0x0

    return-object p0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_fragment_LocalePickerFragment__LocalesAdapter__isEnabled',
        'method': '.method public isEnabled(I)Z',
        'method_name': 'isEnabled',
        'method_anchors': ['invoke-virtual {p0, p1}, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;->getItem(I)Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;', 'sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz p1, :cond_1', 'if-eqz p0, :cond_0', 'iget-object p0, p0, Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;->countryCode:Ljava/lang/String;', 'invoke-static {p0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z', 'if-nez p0, :cond_0', 'return p0'],
        'type': 'policy_skip',
        'search': """.method public isEnabled(I)Z
    .registers 2

    invoke-virtual {p0, p1}, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;->getItem(I)Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;

    move-result-object p0

    sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz p1, :cond_1

    if-eqz p0, :cond_0

    iget-object p0, p0, Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;->countryCode:Ljava/lang/String;

    invoke-static {p0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

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
    .registers 2

    invoke-virtual {p0, p1}, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;->getItem(I)Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;

    move-result-object p0

    sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz p1, :cond_1

    if-eqz p0, :cond_0

    iget-object p0, p0, Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;->countryCode:Ljava/lang/String;

    invoke-static {p0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

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
