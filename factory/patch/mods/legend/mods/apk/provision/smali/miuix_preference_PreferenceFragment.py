TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/preference/PreferenceFragment.smali'
CLASS_FALLBACK_NAMES = ['PreferenceFragment.smali']
CLASS_ANCHORS = ['.super Landroidx/preference/PreferenceFragmentCompat;', '.implements Lmiuix/appcompat/app/IFragment;', '.field public static final CARD_STYLE:I = 0x1', '.field private static final DIALOG_FRAGMENT_TAG:Ljava/lang/String; = "androidx.preference.PreferenceFragment.DIALOG"', '.field public static final DISABLE_ALL_CARD_STYLE:I = -0x1', '.field public static final FORCE_CARD_STYLE:I = 0x2']

PATCHES = [
    {
        'id': 'miuix_preference_PreferenceFragment__onCreateAdapter',
        'method': '.method protected final onCreateAdapter(Landroidx/preference/PreferenceScreen;)Landroidx/recyclerview/widget/RecyclerView$Adapter;',
        'method_name': 'onCreateAdapter',
        'method_anchors': ['new-instance v0, Lmiuix/preference/PreferenceGroupAdapter;', 'iget-boolean v1, p0, Lmiuix/preference/PreferenceFragment;->mIsEnableCardStyle:Z', 'iget v2, p0, Lmiuix/preference/PreferenceFragment;->mCardStyle:I', 'invoke-direct {v0, p1, v1, v2}, Lmiuix/preference/PreferenceGroupAdapter;-><init>(Landroidx/preference/PreferenceGroup;ZI)V', 'iput-object v0, p0, Lmiuix/preference/PreferenceFragment;->mGroupAdapter:Lmiuix/preference/PreferenceGroupAdapter;', 'iget-boolean p1, p0, Lmiuix/preference/PreferenceFragment;->mItemSelectable:Z', 'invoke-virtual {v0, p1}, Lmiuix/preference/PreferenceGroupAdapter;->setItemSelectable(Z)V', 'iget-object p1, p0, Lmiuix/preference/PreferenceFragment;->mGroupAdapter:Lmiuix/preference/PreferenceGroupAdapter;'],
        'type': 'method_replace',
        'search': """.method protected final onCreateAdapter(Landroidx/preference/PreferenceScreen;)Landroidx/recyclerview/widget/RecyclerView$Adapter;
    .registers 9

    new-instance v0, Lmiuix/preference/PreferenceGroupAdapter;

    iget-boolean v1, p0, Lmiuix/preference/PreferenceFragment;->mIsEnableCardStyle:Z

    iget v2, p0, Lmiuix/preference/PreferenceFragment;->mCardStyle:I

    invoke-direct {v0, p1, v1, v2}, Lmiuix/preference/PreferenceGroupAdapter;-><init>(Landroidx/preference/PreferenceGroup;ZI)V

    iput-object v0, p0, Lmiuix/preference/PreferenceFragment;->mGroupAdapter:Lmiuix/preference/PreferenceGroupAdapter;

    iget-boolean p1, p0, Lmiuix/preference/PreferenceFragment;->mItemSelectable:Z

    invoke-virtual {v0, p1}, Lmiuix/preference/PreferenceGroupAdapter;->setItemSelectable(Z)V

    iget-object p1, p0, Lmiuix/preference/PreferenceFragment;->mGroupAdapter:Lmiuix/preference/PreferenceGroupAdapter;

    iget v0, p0, Lmiuix/preference/PreferenceFragment;->mExtraHorizontalPadding:I

    invoke-virtual {p1, v0}, Lmiuix/preference/PreferenceGroupAdapter;->setExtraHorizontalPadding(I)Z

    iget-object p1, p0, Lmiuix/preference/PreferenceFragment;->mGroupAdapter:Lmiuix/preference/PreferenceGroupAdapter;

    invoke-virtual {p1}, Landroidx/preference/PreferenceGroupAdapter;->getItemCount()I

    move-result p1

    const/4 v0, 0x1

    if-ge p1, v0, :cond_0

    goto :goto_0

    :cond_0
    const/4 v0, 0x0

    :goto_0
    iput-boolean v0, p0, Lmiuix/preference/PreferenceFragment;->mAdapterInvalid:Z

    iget-object p1, p0, Lmiuix/preference/PreferenceFragment;->mFrameDecoration:Lmiuix/preference/PreferenceFragment$FrameDecoration;

    if-eqz p1, :cond_1

    iget-object v0, p0, Lmiuix/preference/PreferenceFragment;->mGroupAdapter:Lmiuix/preference/PreferenceGroupAdapter;

    iget-object v1, p1, Lmiuix/recyclerview/card/base/BaseDecoration;->mPaint:Landroid/graphics/Paint;

    invoke-static {p1}, Lmiuix/preference/PreferenceFragment$FrameDecoration;->access$1100(Lmiuix/preference/PreferenceFragment$FrameDecoration;)I

    move-result v2

    iget-object p1, p0, Lmiuix/preference/PreferenceFragment;->mFrameDecoration:Lmiuix/preference/PreferenceFragment$FrameDecoration;

    invoke-static {p1}, Lmiuix/preference/PreferenceFragment$FrameDecoration;->access$1200(Lmiuix/preference/PreferenceFragment$FrameDecoration;)I

    move-result v3

    iget-object p1, p0, Lmiuix/preference/PreferenceFragment;->mFrameDecoration:Lmiuix/preference/PreferenceFragment$FrameDecoration;

    invoke-static {p1}, Lmiuix/preference/PreferenceFragment$FrameDecoration;->access$1300(Lmiuix/preference/PreferenceFragment$FrameDecoration;)I

    move-result v4

    iget-object p1, p0, Lmiuix/preference/PreferenceFragment;->mFrameDecoration:Lmiuix/preference/PreferenceFragment$FrameDecoration;

    invoke-static {p1}, Lmiuix/preference/PreferenceFragment$FrameDecoration;->access$1400(Lmiuix/preference/PreferenceFragment$FrameDecoration;)I

    move-result v5

    iget-object p1, p0, Lmiuix/preference/PreferenceFragment;->mFrameDecoration:Lmiuix/preference/PreferenceFragment$FrameDecoration;

    iget v6, p1, Lmiuix/recyclerview/card/base/BaseDecoration;->mCardRadius:I

    invoke-virtual/range {v0 .. v6}, Lmiuix/preference/PreferenceGroupAdapter;->setClipPaint(Landroid/graphics/Paint;IIIII)V

    :cond_1
    iget-object p0, p0, Lmiuix/preference/PreferenceFragment;->mGroupAdapter:Lmiuix/preference/PreferenceGroupAdapter;

    return-object p0
.end method""",
        'replacement': """.method protected final onCreateAdapter(Landroidx/preference/PreferenceScreen;)Landroidx/recyclerview/widget/RecyclerView$Adapter;
    .registers 9

    goto :goto_17

    nop

    :goto_0
    iget-object p1, p0, Lmiuix/preference/PreferenceFragment;->mFrameDecoration:Lmiuix/preference/PreferenceFragment$FrameDecoration;

    goto :goto_6

    nop

    :goto_1
    invoke-virtual {p1, v0}, Lmiuix/preference/PreferenceGroupAdapter;->setExtraHorizontalPadding(I)Z

    goto :goto_16

    nop

    :goto_2
    iget-object p1, p0, Lmiuix/preference/PreferenceFragment;->mFrameDecoration:Lmiuix/preference/PreferenceFragment$FrameDecoration;

    goto :goto_5

    nop

    :goto_3
    invoke-virtual/range {v0 .. v6}, Lmiuix/preference/PreferenceGroupAdapter;->setClipPaint(Landroid/graphics/Paint;IIIII)V

    :goto_4
    goto :goto_11

    nop

    :goto_5
    iget v6, p1, Lmiuix/recyclerview/card/base/BaseDecoration;->mCardRadius:I

    goto :goto_3

    nop

    :goto_6
    invoke-static {p1}, Lmiuix/preference/PreferenceFragment$FrameDecoration;->access$1200(Lmiuix/preference/PreferenceFragment$FrameDecoration;)I

    move-result v3

    goto :goto_7

    nop

    :goto_7
    iget-object p1, p0, Lmiuix/preference/PreferenceFragment;->mFrameDecoration:Lmiuix/preference/PreferenceFragment$FrameDecoration;

    goto :goto_14

    nop

    :goto_8
    if-nez p1, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_20

    nop

    :goto_9
    invoke-static {p1}, Lmiuix/preference/PreferenceFragment$FrameDecoration;->access$1400(Lmiuix/preference/PreferenceFragment$FrameDecoration;)I

    move-result v5

    goto :goto_2

    nop

    :goto_a
    goto :goto_e

    :goto_b
    goto :goto_d

    nop

    :goto_c
    const/4 v0, 0x1

    goto :goto_22

    nop

    :goto_d
    const/4 v0, 0x0

    :goto_e
    goto :goto_10

    nop

    :goto_f
    iget-object v1, p1, Lmiuix/recyclerview/card/base/BaseDecoration;->mPaint:Landroid/graphics/Paint;

    goto :goto_1b

    nop

    :goto_10
    iput-boolean v0, p0, Lmiuix/preference/PreferenceFragment;->mAdapterInvalid:Z

    goto :goto_12

    nop

    :goto_11
    iget-object p0, p0, Lmiuix/preference/PreferenceFragment;->mGroupAdapter:Lmiuix/preference/PreferenceGroupAdapter;

    goto :goto_18

    nop

    :goto_12
    iget-object p1, p0, Lmiuix/preference/PreferenceFragment;->mFrameDecoration:Lmiuix/preference/PreferenceFragment$FrameDecoration;

    goto :goto_8

    nop

    :goto_13
    iget-object p1, p0, Lmiuix/preference/PreferenceFragment;->mFrameDecoration:Lmiuix/preference/PreferenceFragment$FrameDecoration;

    goto :goto_9

    nop

    :goto_14
    invoke-static {p1}, Lmiuix/preference/PreferenceFragment$FrameDecoration;->access$1300(Lmiuix/preference/PreferenceFragment$FrameDecoration;)I

    move-result v4

    goto :goto_13

    nop

    :goto_15
    iget v0, p0, Lmiuix/preference/PreferenceFragment;->mExtraHorizontalPadding:I

    goto :goto_1

    nop

    :goto_16
    iget-object p1, p0, Lmiuix/preference/PreferenceFragment;->mGroupAdapter:Lmiuix/preference/PreferenceGroupAdapter;

    goto :goto_19

    nop

    :goto_17
    new-instance v0, Lmiuix/preference/PreferenceGroupAdapter;

    goto :goto_1c

    nop

    :goto_18
    return-object p0

    :goto_19
    invoke-virtual {p1}, Landroidx/preference/PreferenceGroupAdapter;->getItemCount()I

    move-result p1

    goto :goto_c

    nop

    :goto_1a
    iget-boolean p1, p0, Lmiuix/preference/PreferenceFragment;->mItemSelectable:Z

    goto :goto_1f

    nop

    :goto_1b
    invoke-static {p1}, Lmiuix/preference/PreferenceFragment$FrameDecoration;->access$1100(Lmiuix/preference/PreferenceFragment$FrameDecoration;)I

    move-result v2

    goto :goto_0

    nop

    :goto_1c
    iget-boolean v1, p0, Lmiuix/preference/PreferenceFragment;->mIsEnableCardStyle:Z

    goto :goto_23

    nop

    :goto_1d
    invoke-direct {v0, p1, v1, v2}, Lmiuix/preference/PreferenceGroupAdapter;-><init>(Landroidx/preference/PreferenceGroup;ZI)V

    goto :goto_1e

    nop

    :goto_1e
    iput-object v0, p0, Lmiuix/preference/PreferenceFragment;->mGroupAdapter:Lmiuix/preference/PreferenceGroupAdapter;

    goto :goto_1a

    nop

    :goto_1f
    invoke-virtual {v0, p1}, Lmiuix/preference/PreferenceGroupAdapter;->setItemSelectable(Z)V

    goto :goto_21

    nop

    :goto_20
    iget-object v0, p0, Lmiuix/preference/PreferenceFragment;->mGroupAdapter:Lmiuix/preference/PreferenceGroupAdapter;

    goto :goto_f

    nop

    :goto_21
    iget-object p1, p0, Lmiuix/preference/PreferenceFragment;->mGroupAdapter:Lmiuix/preference/PreferenceGroupAdapter;

    goto :goto_15

    nop

    :goto_22
    if-lt p1, v0, :cond_1

    goto :goto_b

    :cond_1
    goto :goto_a

    nop

    :goto_23
    iget v2, p0, Lmiuix/preference/PreferenceFragment;->mCardStyle:I

    goto :goto_1d

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_preference_PreferenceFragment__getListViewPaddingBottom',
        'method': '.method protected getListViewPaddingBottom()I',
        'method_name': 'getListViewPaddingBottom',
        'method_anchors': ['return p0'],
        'type': 'method_replace',
        'search': """.method protected getListViewPaddingBottom()I
    .registers 1

    const/4 p0, -0x1

    return p0
.end method""",
        'replacement': """.method protected getListViewPaddingBottom()I
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    const/4 p0, -0x1

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_preference_PreferenceFragment__getListViewPaddingTop',
        'method': '.method protected getListViewPaddingTop()I',
        'method_name': 'getListViewPaddingTop',
        'method_anchors': ['return p0'],
        'type': 'method_replace',
        'search': """.method protected getListViewPaddingTop()I
    .registers 1

    const/4 p0, -0x1

    return p0
.end method""",
        'replacement': """.method protected getListViewPaddingTop()I
    .registers 1

    goto :goto_0

    nop

    :goto_0
    const/4 p0, -0x1

    goto :goto_1

    nop

    :goto_1
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_preference_PreferenceFragment__isActionBarOverlay',
        'method': '.method protected isActionBarOverlay()Z',
        'method_name': 'isActionBarOverlay',
        'method_anchors': ['iget-boolean p0, p0, Lmiuix/preference/PreferenceFragment;->mIsOverlayMode:Z', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected isActionBarOverlay()Z
    .registers 1

    iget-boolean p0, p0, Lmiuix/preference/PreferenceFragment;->mIsOverlayMode:Z

    return p0
.end method""",
        'replacement': """.method protected isActionBarOverlay()Z
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    iget-boolean p0, p0, Lmiuix/preference/PreferenceFragment;->mIsOverlayMode:Z

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_preference_PreferenceFragment__isEmbeddedFragment',
        'method': '.method protected isEmbeddedFragment()Z',
        'method_name': 'isEmbeddedFragment',
        'method_anchors': ['return p0'],
        'type': 'method_replace',
        'search': """.method protected isEmbeddedFragment()Z
    .registers 1

    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method protected isEmbeddedFragment()Z
    .registers 1

    goto :goto_0

    nop

    :goto_0
    const/4 p0, 0x0

    goto :goto_1

    nop

    :goto_1
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_preference_PreferenceFragment__isInFloatingWindowMode',
        'method': '.method protected isInFloatingWindowMode()Z',
        'method_name': 'isInFloatingWindowMode',
        'method_anchors': ['invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;', 'if-eqz v0, :cond_0', 'check-cast p0, Lmiuix/appcompat/app/AppCompatActivity;', 'invoke-virtual {p0}, Lmiuix/appcompat/app/AppCompatActivity;->isInFloatingWindowMode()Z', 'return p0', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected isInFloatingWindowMode()Z
    .registers 2

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p0

    instance-of v0, p0, Lmiuix/appcompat/app/AppCompatActivity;

    if-eqz v0, :cond_0

    check-cast p0, Lmiuix/appcompat/app/AppCompatActivity;

    invoke-virtual {p0}, Lmiuix/appcompat/app/AppCompatActivity;->isInFloatingWindowMode()Z

    move-result p0

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method protected isInFloatingWindowMode()Z
    .registers 2

    goto :goto_0

    nop

    :goto_0
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p0

    goto :goto_5

    nop

    :goto_1
    return p0

    :goto_2
    if-nez v0, :cond_0

    goto :goto_7

    :cond_0
    goto :goto_8

    nop

    :goto_3
    const/4 p0, 0x0

    goto :goto_1

    nop

    :goto_4
    invoke-virtual {p0}, Lmiuix/appcompat/app/AppCompatActivity;->isInFloatingWindowMode()Z

    move-result p0

    goto :goto_6

    nop

    :goto_5
    instance-of v0, p0, Lmiuix/appcompat/app/AppCompatActivity;

    goto :goto_2

    nop

    :goto_6
    return p0

    :goto_7
    goto :goto_3

    nop

    :goto_8
    check-cast p0, Lmiuix/appcompat/app/AppCompatActivity;

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_preference_PreferenceFragment__isInMiuiSettingMultiWindowMode',
        'method': '.method protected isInMiuiSettingMultiWindowMode()Z',
        'method_name': 'isInMiuiSettingMultiWindowMode',
        'method_anchors': ['invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;', 'if-eqz p0, :cond_0', 'invoke-virtual {p0}, Landroid/app/Activity;->getIntent()Landroid/content/Intent;', 'invoke-static {p0}, Lmiuix/core/util/IntentUtils;->isIntentFromSettingsSplit(Landroid/content/Intent;)Z', 'return p0', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected isInMiuiSettingMultiWindowMode()Z
    .registers 1

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p0

    if-eqz p0, :cond_0

    invoke-virtual {p0}, Landroid/app/Activity;->getIntent()Landroid/content/Intent;

    move-result-object p0

    invoke-static {p0}, Lmiuix/core/util/IntentUtils;->isIntentFromSettingsSplit(Landroid/content/Intent;)Z

    move-result p0

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method protected isInMiuiSettingMultiWindowMode()Z
    .registers 1

    goto :goto_7

    nop

    :goto_0
    invoke-static {p0}, Lmiuix/core/util/IntentUtils;->isIntentFromSettingsSplit(Landroid/content/Intent;)Z

    move-result p0

    goto :goto_3

    nop

    :goto_1
    const/4 p0, 0x0

    goto :goto_5

    nop

    :goto_2
    invoke-virtual {p0}, Landroid/app/Activity;->getIntent()Landroid/content/Intent;

    move-result-object p0

    goto :goto_0

    nop

    :goto_3
    return p0

    :goto_4
    goto :goto_1

    nop

    :goto_5
    return p0

    :goto_6
    if-nez p0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_2

    nop

    :goto_7
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p0

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
