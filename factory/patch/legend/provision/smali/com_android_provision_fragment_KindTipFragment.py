TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/fragment/KindTipFragment.smali'
CLASS_FALLBACK_NAMES = ['KindTipFragment.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/fragment/BaseFragment;']

PATCHES = [
    {
        'id': 'com_android_provision_fragment_KindTipFragment__onViewCreated',
        'method': '.method public onViewCreated(Landroid/view/View;Landroid/os/Bundle;)V',
        'method_name': 'onViewCreated',
        'method_anchors': ['invoke-super {p0, p1, p2}, Landroidx/fragment/app/Fragment;->onViewCreated(Landroid/view/View;Landroid/os/Bundle;)V', 'sget p2, Lcom/android/provision/R$drawable;->item_hint_icon_1:I', 'invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;', 'sget p2, Lcom/android/provision/R$drawable;->item_hint_icon_2:I', 'invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;', 'sget p2, Lcom/android/provision/R$drawable;->item_hint_icon_3:I', 'invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;', 'sget p2, Lcom/android/provision/R$drawable;->item_hint_icon_4:I'],
        'type': 'policy_skip',
        'search': """.method public onViewCreated(Landroid/view/View;Landroid/os/Bundle;)V
    .registers 10

    invoke-super {p0, p1, p2}, Landroidx/fragment/app/Fragment;->onViewCreated(Landroid/view/View;Landroid/os/Bundle;)V

    sget p2, Lcom/android/provision/R$drawable;->item_hint_icon_1:I

    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    sget p2, Lcom/android/provision/R$drawable;->item_hint_icon_2:I

    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    sget p2, Lcom/android/provision/R$drawable;->item_hint_icon_3:I

    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v2

    sget p2, Lcom/android/provision/R$drawable;->item_hint_icon_4:I

    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v3

    sget p2, Lcom/android/provision/R$drawable;->item_hint_icon_5:I

    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v4

    sget p2, Lcom/android/provision/R$drawable;->item_hint_icon_6:I

    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v5

    filled-new-array/range {v0 .. v5}, [Ljava/lang/Integer;

    move-result-object p2

    invoke-static {p2}, Ljava/util/Arrays;->asList([Ljava/lang/Object;)Ljava/util/List;

    move-result-object p2

    iput-object p2, p0, Lcom/android/provision/fragment/KindTipFragment;->mImageList:Ljava/util/List;

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getResources()Landroid/content/res/Resources;

    move-result-object p2

    sget v0, Lcom/android/provision/R$string;->kind_note01:I

    invoke-virtual {p2, v0}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getResources()Landroid/content/res/Resources;

    move-result-object p2

    sget v0, Lcom/android/provision/R$string;->kind_note02:I

    invoke-virtual {p2, v0}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object v2

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getResources()Landroid/content/res/Resources;

    move-result-object p2

    sget v0, Lcom/android/provision/R$string;->kind_note03:I

    invoke-virtual {p2, v0}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getResources()Landroid/content/res/Resources;

    move-result-object p2

    sget v0, Lcom/android/provision/R$string;->kind_note04:I

    invoke-virtual {p2, v0}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getResources()Landroid/content/res/Resources;

    move-result-object p2

    sget v0, Lcom/android/provision/R$string;->kind_note05:I

    invoke-virtual {p2, v0}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getResources()Landroid/content/res/Resources;

    move-result-object p2

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    sget v0, Lcom/android/provision/R$string;->kind_note06_global:I

    goto :goto_0

    :cond_0
    sget v0, Lcom/android/provision/R$string;->kind_note06_cn:I

    :goto_0
    invoke-virtual {p2, v0}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object v6

    filled-new-array/range {v1 .. v6}, [Ljava/lang/String;

    move-result-object p2

    invoke-static {p2}, Ljava/util/Arrays;->asList([Ljava/lang/Object;)Ljava/util/List;

    move-result-object p2

    iput-object p2, p0, Lcom/android/provision/fragment/KindTipFragment;->mTextList:Ljava/util/List;

    sget p2, Lcom/android/provision/R$id;->hint_list_view:I

    invoke-virtual {p1, p2}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object p1

    check-cast p1, Landroid/widget/ListView;

    iput-object p1, p0, Lcom/android/provision/fragment/KindTipFragment;->mListView:Landroid/widget/ListView;

    new-instance p1, Lcom/android/provision/adapter/ListViewHintAdapter;

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p2

    iget-object v0, p0, Lcom/android/provision/fragment/KindTipFragment;->mImageList:Ljava/util/List;

    iget-object v1, p0, Lcom/android/provision/fragment/KindTipFragment;->mTextList:Ljava/util/List;

    invoke-direct {p1, p2, v0, v1}, Lcom/android/provision/adapter/ListViewHintAdapter;-><init>(Landroid/content/Context;Ljava/util/List;Ljava/util/List;)V

    iput-object p1, p0, Lcom/android/provision/fragment/KindTipFragment;->mAdapter:Lcom/android/provision/adapter/ListViewHintAdapter;

    iget-object p2, p0, Lcom/android/provision/fragment/KindTipFragment;->mListView:Landroid/widget/ListView;

    invoke-virtual {p2, p1}, Landroid/widget/ListView;->setAdapter(Landroid/widget/ListAdapter;)V

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p1

    invoke-static {p1}, Lcom/android/provision/Utils;->getNextView(Landroid/app/Activity;)Landroid/widget/Button;

    move-result-object p1

    new-instance p2, Lcom/android/provision/fragment/KindTipFragment$$ExternalSyntheticLambda0;

    invoke-direct {p2, p0}, Lcom/android/provision/fragment/KindTipFragment$$ExternalSyntheticLambda0;-><init>(Lcom/android/provision/fragment/KindTipFragment;)V

    invoke-virtual {p1, p2}, Landroid/view/View;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    return-void
.end method""",
        'replacement': """.method public onViewCreated(Landroid/view/View;Landroid/os/Bundle;)V
    .registers 10

    invoke-super {p0, p1, p2}, Landroidx/fragment/app/Fragment;->onViewCreated(Landroid/view/View;Landroid/os/Bundle;)V

    sget p2, Lcom/android/provision/R$drawable;->item_hint_icon_1:I

    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    sget p2, Lcom/android/provision/R$drawable;->item_hint_icon_2:I

    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    sget p2, Lcom/android/provision/R$drawable;->item_hint_icon_3:I

    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v2

    sget p2, Lcom/android/provision/R$drawable;->item_hint_icon_4:I

    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v3

    sget p2, Lcom/android/provision/R$drawable;->item_hint_icon_5:I

    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v4

    sget p2, Lcom/android/provision/R$drawable;->item_hint_icon_6:I

    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v5

    filled-new-array/range {v0 .. v5}, [Ljava/lang/Integer;

    move-result-object p2

    invoke-static {p2}, Ljava/util/Arrays;->asList([Ljava/lang/Object;)Ljava/util/List;

    move-result-object p2

    iput-object p2, p0, Lcom/android/provision/fragment/KindTipFragment;->mImageList:Ljava/util/List;

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getResources()Landroid/content/res/Resources;

    move-result-object p2

    sget v0, Lcom/android/provision/R$string;->kind_note01:I

    invoke-virtual {p2, v0}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getResources()Landroid/content/res/Resources;

    move-result-object p2

    sget v0, Lcom/android/provision/R$string;->kind_note02:I

    invoke-virtual {p2, v0}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object v2

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getResources()Landroid/content/res/Resources;

    move-result-object p2

    sget v0, Lcom/android/provision/R$string;->kind_note03:I

    invoke-virtual {p2, v0}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getResources()Landroid/content/res/Resources;

    move-result-object p2

    sget v0, Lcom/android/provision/R$string;->kind_note04:I

    invoke-virtual {p2, v0}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getResources()Landroid/content/res/Resources;

    move-result-object p2

    sget v0, Lcom/android/provision/R$string;->kind_note05:I

    invoke-virtual {p2, v0}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getResources()Landroid/content/res/Resources;

    move-result-object p2

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    sget v0, Lcom/android/provision/R$string;->kind_note06_global:I

    goto :goto_0

    :cond_0
    sget v0, Lcom/android/provision/R$string;->kind_note06_cn:I

    :goto_0
    invoke-virtual {p2, v0}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object v6

    filled-new-array/range {v1 .. v6}, [Ljava/lang/String;

    move-result-object p2

    invoke-static {p2}, Ljava/util/Arrays;->asList([Ljava/lang/Object;)Ljava/util/List;

    move-result-object p2

    iput-object p2, p0, Lcom/android/provision/fragment/KindTipFragment;->mTextList:Ljava/util/List;

    sget p2, Lcom/android/provision/R$id;->hint_list_view:I

    invoke-virtual {p1, p2}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object p1

    check-cast p1, Landroid/widget/ListView;

    iput-object p1, p0, Lcom/android/provision/fragment/KindTipFragment;->mListView:Landroid/widget/ListView;

    new-instance p1, Lcom/android/provision/adapter/ListViewHintAdapter;

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p2

    iget-object v0, p0, Lcom/android/provision/fragment/KindTipFragment;->mImageList:Ljava/util/List;

    iget-object v1, p0, Lcom/android/provision/fragment/KindTipFragment;->mTextList:Ljava/util/List;

    invoke-direct {p1, p2, v0, v1}, Lcom/android/provision/adapter/ListViewHintAdapter;-><init>(Landroid/content/Context;Ljava/util/List;Ljava/util/List;)V

    iput-object p1, p0, Lcom/android/provision/fragment/KindTipFragment;->mAdapter:Lcom/android/provision/adapter/ListViewHintAdapter;

    iget-object p2, p0, Lcom/android/provision/fragment/KindTipFragment;->mListView:Landroid/widget/ListView;

    invoke-virtual {p2, p1}, Landroid/widget/ListView;->setAdapter(Landroid/widget/ListAdapter;)V

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p1

    invoke-static {p1}, Lcom/android/provision/Utils;->getNextView(Landroid/app/Activity;)Landroid/widget/Button;

    move-result-object p1

    new-instance p2, Lcom/android/provision/fragment/KindTipFragment$$ExternalSyntheticLambda0;

    invoke-direct {p2, p0}, Lcom/android/provision/fragment/KindTipFragment$$ExternalSyntheticLambda0;-><init>(Lcom/android/provision/fragment/KindTipFragment;)V

    invoke-virtual {p1, p2}, Landroid/view/View;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    return-void
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
]
