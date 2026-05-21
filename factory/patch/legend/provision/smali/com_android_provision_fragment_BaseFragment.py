TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/fragment/BaseFragment.smali'
CLASS_FALLBACK_NAMES = ['BaseFragment.smali']
CLASS_ANCHORS = ['.super Landroidx/fragment/app/Fragment;']

PATCHES = [
    {
        'id': 'com_android_provision_fragment_BaseFragment__getName',
        'method': '.method protected getName()Ljava/lang/String;',
        'method_name': 'getName',
        'method_anchors': ['invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->isAdded()Z', 'if-eqz v0, :cond_0', 'invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;', 'invoke-virtual {p0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;', 'return-object p0', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getName()Ljava/lang/String;
    .registers 2

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->isAdded()Z

    move-result v0

    if-eqz v0, :cond_0

    invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object p0

    invoke-virtual {p0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object p0

    return-object p0

    :cond_0
    const/4 p0, 0x0

    return-object p0
.end method""",
        'replacement': """.method protected getName()Ljava/lang/String;
    .registers 2

    goto :goto_5

    nop

    :goto_0
    invoke-virtual {p0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object p0

    goto :goto_3

    nop

    :goto_1
    return-object p0

    :goto_2
    const/4 p0, 0x0

    goto :goto_1

    nop

    :goto_3
    return-object p0

    :goto_4
    goto :goto_2

    nop

    :goto_5
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->isAdded()Z

    move-result v0

    goto :goto_6

    nop

    :goto_6
    if-nez v0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_7

    nop

    :goto_7
    invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object p0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_fragment_BaseFragment__recordBottomButtonClick',
        'method': '.method protected recordBottomButtonClick(Ljava/lang/String;)V',
        'method_name': 'recordBottomButtonClick',
        'method_anchors': ['invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;', 'invoke-virtual {p0}, Lcom/android/provision/fragment/BaseFragment;->getName()Ljava/lang/String;', 'invoke-static {v0, p0, p1}, Lcom/android/provision/utils/OTHelper;->rdBottomButtonEvent(Landroid/app/Activity;Ljava/lang/String;Ljava/lang/String;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected recordBottomButtonClick(Ljava/lang/String;)V
    .registers 3

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-virtual {p0}, Lcom/android/provision/fragment/BaseFragment;->getName()Ljava/lang/String;

    move-result-object p0

    invoke-static {v0, p0, p1}, Lcom/android/provision/utils/OTHelper;->rdBottomButtonEvent(Landroid/app/Activity;Ljava/lang/String;Ljava/lang/String;)V

    return-void
.end method""",
        'replacement': """.method protected recordBottomButtonClick(Ljava/lang/String;)V
    .registers 3

    goto :goto_2

    nop

    :goto_0
    return-void

    :goto_1
    invoke-static {v0, p0, p1}, Lcom/android/provision/utils/OTHelper;->rdBottomButtonEvent(Landroid/app/Activity;Ljava/lang/String;Ljava/lang/String;)V

    goto :goto_0

    nop

    :goto_2
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    goto :goto_3

    nop

    :goto_3
    invoke-virtual {p0}, Lcom/android/provision/fragment/BaseFragment;->getName()Ljava/lang/String;

    move-result-object p0

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_fragment_BaseFragment__recordPageStayTime',
        'method': '.method protected recordPageStayTime()V',
        'method_name': 'recordPageStayTime',
        'method_anchors': ['invoke-virtual {p0}, Lcom/android/provision/fragment/BaseFragment;->getName()Ljava/lang/String;', 'invoke-static {}, Ljava/lang/System;->currentTimeMillis()J', 'iget-wide v3, p0, Lcom/android/provision/fragment/BaseFragment;->mUserStayStartTime:J', 'invoke-static {v0, v1, v2}, Lcom/android/provision/utils/OTHelper;->rdPageStayTimeEvent(Ljava/lang/String;J)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected recordPageStayTime()V
    .registers 6

    invoke-virtual {p0}, Lcom/android/provision/fragment/BaseFragment;->getName()Ljava/lang/String;

    move-result-object v0

    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v1

    iget-wide v3, p0, Lcom/android/provision/fragment/BaseFragment;->mUserStayStartTime:J

    sub-long/2addr v1, v3

    invoke-static {v0, v1, v2}, Lcom/android/provision/utils/OTHelper;->rdPageStayTimeEvent(Ljava/lang/String;J)V

    return-void
.end method""",
        'replacement': """.method protected recordPageStayTime()V
    .registers 6

    goto :goto_0

    nop

    :goto_0
    invoke-virtual {p0}, Lcom/android/provision/fragment/BaseFragment;->getName()Ljava/lang/String;

    move-result-object v0

    goto :goto_1

    nop

    :goto_1
    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v1

    goto :goto_3

    nop

    :goto_2
    return-void

    :goto_3
    iget-wide v3, p0, Lcom/android/provision/fragment/BaseFragment;->mUserStayStartTime:J

    goto :goto_4

    nop

    :goto_4
    sub-long/2addr v1, v3

    goto :goto_5

    nop

    :goto_5
    invoke-static {v0, v1, v2}, Lcom/android/provision/utils/OTHelper;->rdPageStayTimeEvent(Ljava/lang/String;J)V

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
