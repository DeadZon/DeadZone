TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/fragment/LocalePickerFragment$SearchFilter.smali'
CLASS_FALLBACK_NAMES = ['LocalePickerFragment$SearchFilter.smali']
CLASS_ANCHORS = ['.super Landroid/widget/Filter;']

PATCHES = [
    {
        'id': 'com_android_provision_fragment_LocalePickerFragment__SearchFilter__performFiltering',
        'method': '.method protected performFiltering(Ljava/lang/CharSequence;)Landroid/widget/Filter$FilterResults;',
        'method_name': 'performFiltering',
        'method_anchors': ['new-instance v0, Landroid/widget/Filter$FilterResults;', 'invoke-direct {v0}, Landroid/widget/Filter$FilterResults;-><init>()V', 'invoke-static {p1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z', 'if-nez v1, :cond_2', 'invoke-interface {p1}, Ljava/lang/CharSequence;->toString()Ljava/lang/String;', 'invoke-virtual {p1}, Ljava/lang/String;->toLowerCase()Ljava/lang/String;', 'new-instance v1, Ljava/util/ArrayList;', 'invoke-direct {v1}, Ljava/util/ArrayList;-><init>()V'],
        'type': 'method_replace',
        'search': """.method protected performFiltering(Ljava/lang/CharSequence;)Landroid/widget/Filter$FilterResults;
    .registers 6

    new-instance v0, Landroid/widget/Filter$FilterResults;

    invoke-direct {v0}, Landroid/widget/Filter$FilterResults;-><init>()V

    invoke-static {p1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v1

    if-nez v1, :cond_2

    invoke-interface {p1}, Ljava/lang/CharSequence;->toString()Ljava/lang/String;

    move-result-object p1

    invoke-virtual {p1}, Ljava/lang/String;->toLowerCase()Ljava/lang/String;

    move-result-object p1

    new-instance v1, Ljava/util/ArrayList;

    invoke-direct {v1}, Ljava/util/ArrayList;-><init>()V

    iget-object p0, p0, Lcom/android/provision/fragment/LocalePickerFragment$SearchFilter;->mOriginalSources:Ljava/util/List;

    invoke-interface {p0}, Ljava/util/List;->iterator()Ljava/util/Iterator;

    move-result-object p0

    :cond_0
    :goto_0
    invoke-interface {p0}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    if-eqz v2, :cond_1

    invoke-interface {p0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v2

    check-cast v2, Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;

    if-eqz v2, :cond_0

    iget-object v3, v2, Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;->countryCode:Ljava/lang/String;

    invoke-static {v3}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v3

    if-nez v3, :cond_0

    iget-object v3, v2, Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;->displayName:Ljava/lang/String;

    invoke-static {v3}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v3

    if-nez v3, :cond_0

    iget-object v3, v2, Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;->displayName:Ljava/lang/String;

    invoke-virtual {v3}, Ljava/lang/String;->toLowerCase()Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v3, p1}, Ljava/lang/String;->contains(Ljava/lang/CharSequence;)Z

    move-result v3

    if-eqz v3, :cond_0

    invoke-interface {v1, v2}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    goto :goto_0

    :cond_1
    invoke-interface {v1}, Ljava/util/List;->size()I

    move-result p0

    iput p0, v0, Landroid/widget/Filter$FilterResults;->count:I

    iput-object v1, v0, Landroid/widget/Filter$FilterResults;->values:Ljava/lang/Object;

    return-object v0

    :cond_2
    iget-object p1, p0, Lcom/android/provision/fragment/LocalePickerFragment$SearchFilter;->mOriginalSources:Ljava/util/List;

    invoke-interface {p1}, Ljava/util/List;->size()I

    move-result p1

    iput p1, v0, Landroid/widget/Filter$FilterResults;->count:I

    iget-object p0, p0, Lcom/android/provision/fragment/LocalePickerFragment$SearchFilter;->mOriginalSources:Ljava/util/List;

    iput-object p0, v0, Landroid/widget/Filter$FilterResults;->values:Ljava/lang/Object;

    return-object v0
.end method""",
        'replacement': """.method protected performFiltering(Ljava/lang/CharSequence;)Landroid/widget/Filter$FilterResults;
    .registers 6

    goto :goto_9

    nop

    :goto_0
    new-instance v1, Ljava/util/ArrayList;

    goto :goto_17

    nop

    :goto_1
    iput-object v1, v0, Landroid/widget/Filter$FilterResults;->values:Ljava/lang/Object;

    goto :goto_d

    nop

    :goto_2
    invoke-static {p1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v1

    goto :goto_1c

    nop

    :goto_3
    iput-object p0, v0, Landroid/widget/Filter$FilterResults;->values:Ljava/lang/Object;

    goto :goto_10

    nop

    :goto_4
    invoke-static {v3}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v3

    goto :goto_16

    nop

    :goto_5
    iget-object v3, v2, Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;->countryCode:Ljava/lang/String;

    goto :goto_6

    nop

    :goto_6
    invoke-static {v3}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v3

    goto :goto_1f

    nop

    :goto_7
    invoke-interface {p0}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    goto :goto_1e

    nop

    :goto_8
    iget-object v3, v2, Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;->displayName:Ljava/lang/String;

    goto :goto_4

    nop

    :goto_9
    new-instance v0, Landroid/widget/Filter$FilterResults;

    goto :goto_b

    nop

    :goto_a
    iget-object p0, p0, Lcom/android/provision/fragment/LocalePickerFragment$SearchFilter;->mOriginalSources:Ljava/util/List;

    goto :goto_3

    nop

    :goto_b
    invoke-direct {v0}, Landroid/widget/Filter$FilterResults;-><init>()V

    goto :goto_2

    nop

    :goto_c
    invoke-virtual {v3}, Ljava/lang/String;->toLowerCase()Ljava/lang/String;

    move-result-object v3

    goto :goto_14

    nop

    :goto_d
    return-object v0

    :goto_e
    goto :goto_11

    nop

    :goto_f
    if-nez v3, :cond_0

    goto :goto_21

    :cond_0
    goto :goto_15

    nop

    :goto_10
    return-object v0

    :goto_11
    iget-object p1, p0, Lcom/android/provision/fragment/LocalePickerFragment$SearchFilter;->mOriginalSources:Ljava/util/List;

    goto :goto_25

    nop

    :goto_12
    invoke-interface {v1}, Ljava/util/List;->size()I

    move-result p0

    goto :goto_1b

    nop

    :goto_13
    iget-object v3, v2, Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;->displayName:Ljava/lang/String;

    goto :goto_c

    nop

    :goto_14
    invoke-virtual {v3, p1}, Ljava/lang/String;->contains(Ljava/lang/CharSequence;)Z

    move-result v3

    goto :goto_f

    nop

    :goto_15
    invoke-interface {v1, v2}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    goto :goto_26

    nop

    :goto_16
    if-eqz v3, :cond_1

    goto :goto_21

    :cond_1
    goto :goto_13

    nop

    :goto_17
    invoke-direct {v1}, Ljava/util/ArrayList;-><init>()V

    goto :goto_23

    nop

    :goto_18
    check-cast v2, Lcom/android/provision/fragment/LocalePickerFragment$LocaleInfo;

    goto :goto_24

    nop

    :goto_19
    invoke-virtual {p1}, Ljava/lang/String;->toLowerCase()Ljava/lang/String;

    move-result-object p1

    goto :goto_0

    nop

    :goto_1a
    invoke-interface {p1}, Ljava/lang/CharSequence;->toString()Ljava/lang/String;

    move-result-object p1

    goto :goto_19

    nop

    :goto_1b
    iput p0, v0, Landroid/widget/Filter$FilterResults;->count:I

    goto :goto_1

    nop

    :goto_1c
    if-eqz v1, :cond_2

    goto :goto_e

    :cond_2
    goto :goto_1a

    nop

    :goto_1d
    iput p1, v0, Landroid/widget/Filter$FilterResults;->count:I

    goto :goto_a

    nop

    :goto_1e
    if-nez v2, :cond_3

    goto :goto_27

    :cond_3
    goto :goto_22

    nop

    :goto_1f
    if-eqz v3, :cond_4

    goto :goto_21

    :cond_4
    goto :goto_8

    nop

    :goto_20
    invoke-interface {p0}, Ljava/util/List;->iterator()Ljava/util/Iterator;

    move-result-object p0

    :goto_21
    goto :goto_7

    nop

    :goto_22
    invoke-interface {p0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v2

    goto :goto_18

    nop

    :goto_23
    iget-object p0, p0, Lcom/android/provision/fragment/LocalePickerFragment$SearchFilter;->mOriginalSources:Ljava/util/List;

    goto :goto_20

    nop

    :goto_24
    if-nez v2, :cond_5

    goto :goto_21

    :cond_5
    goto :goto_5

    nop

    :goto_25
    invoke-interface {p1}, Ljava/util/List;->size()I

    move-result p1

    goto :goto_1d

    nop

    :goto_26
    goto :goto_21

    :goto_27
    goto :goto_12

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_fragment_LocalePickerFragment__SearchFilter__publishResults',
        'method': '.method protected publishResults(Ljava/lang/CharSequence;Landroid/widget/Filter$FilterResults;)V',
        'method_name': 'publishResults',
        'method_anchors': ['if-eqz p2, :cond_0', 'iget-object p1, p2, Landroid/widget/Filter$FilterResults;->values:Ljava/lang/Object;', 'check-cast p1, Ljava/util/ArrayList;', 'iget-object p0, p0, Lcom/android/provision/fragment/LocalePickerFragment$SearchFilter;->mAdapterRef:Ljava/lang/ref/WeakReference;', 'invoke-virtual {p0}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;', 'check-cast p0, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;', 'if-eqz p0, :cond_0', 'invoke-virtual {p0, p1}, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;->setData(Ljava/util/List;)V'],
        'type': 'method_replace',
        'search': """.method protected publishResults(Ljava/lang/CharSequence;Landroid/widget/Filter$FilterResults;)V
    .registers 3

    if-eqz p2, :cond_0

    iget-object p1, p2, Landroid/widget/Filter$FilterResults;->values:Ljava/lang/Object;

    check-cast p1, Ljava/util/ArrayList;

    iget-object p0, p0, Lcom/android/provision/fragment/LocalePickerFragment$SearchFilter;->mAdapterRef:Ljava/lang/ref/WeakReference;

    invoke-virtual {p0}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;

    move-result-object p0

    check-cast p0, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;

    if-eqz p0, :cond_0

    invoke-virtual {p0, p1}, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;->setData(Ljava/util/List;)V

    invoke-virtual {p0}, Landroid/widget/ArrayAdapter;->notifyDataSetChanged()V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected publishResults(Ljava/lang/CharSequence;Landroid/widget/Filter$FilterResults;)V
    .registers 3

    goto :goto_7

    nop

    :goto_0
    iget-object p1, p2, Landroid/widget/Filter$FilterResults;->values:Ljava/lang/Object;

    goto :goto_3

    nop

    :goto_1
    invoke-virtual {p0}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;

    move-result-object p0

    goto :goto_4

    nop

    :goto_2
    iget-object p0, p0, Lcom/android/provision/fragment/LocalePickerFragment$SearchFilter;->mAdapterRef:Ljava/lang/ref/WeakReference;

    goto :goto_1

    nop

    :goto_3
    check-cast p1, Ljava/util/ArrayList;

    goto :goto_2

    nop

    :goto_4
    check-cast p0, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;

    goto :goto_6

    nop

    :goto_5
    return-void

    :goto_6
    if-nez p0, :cond_0

    goto :goto_9

    :cond_0
    goto :goto_a

    nop

    :goto_7
    if-nez p2, :cond_1

    goto :goto_9

    :cond_1
    goto :goto_0

    nop

    :goto_8
    invoke-virtual {p0}, Landroid/widget/ArrayAdapter;->notifyDataSetChanged()V

    :goto_9
    goto :goto_5

    nop

    :goto_a
    invoke-virtual {p0, p1}, Lcom/android/provision/fragment/LocalePickerFragment$LocalesAdapter;->setData(Ljava/util/List;)V

    goto :goto_8

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
