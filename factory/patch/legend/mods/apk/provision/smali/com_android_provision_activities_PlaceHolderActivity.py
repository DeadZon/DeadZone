TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/activities/PlaceHolderActivity.smali'
CLASS_FALLBACK_NAMES = ['PlaceHolderActivity.smali']
CLASS_ANCHORS = ['.super Lmiuix/appcompat/app/AppCompatActivity;', '.field private static final TAG:Ljava/lang/String; = "PlaceHolderActivity"']

PATCHES = [
    {
        'id': 'com_android_provision_activities_PlaceHolderActivity__onCreate',
        'method': '.method protected onCreate(Landroid/os/Bundle;)V',
        'method_name': 'onCreate',
        'method_anchors': ['invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V', 'new-instance p1, Ljava/lang/StringBuilder;', 'invoke-direct {p1}, Ljava/lang/StringBuilder;-><init>()V', 'const-string v0, " onCreate PlaceHolderActivity "', 'invoke-virtual {p1, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'invoke-virtual {p1, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;', 'invoke-virtual {p1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;', 'const-string v0, "PlaceHolderActivity"'],
        'type': 'method_replace',
        'search': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 3

    invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    new-instance p1, Ljava/lang/StringBuilder;

    invoke-direct {p1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v0, " onCreate PlaceHolderActivity "

    invoke-virtual {p1, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p1, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {p1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p1

    const-string v0, "PlaceHolderActivity"

    invoke-static {v0, p1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    invoke-direct {p0}, Lcom/android/provision/activities/PlaceHolderActivity;->registerFoldCallback()V

    return-void
.end method""",
        'replacement': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 3

    goto :goto_5

    nop

    :goto_0
    invoke-direct {p1}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_4

    nop

    :goto_1
    invoke-static {v0, p1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_a

    nop

    :goto_2
    invoke-virtual {p1, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_7

    nop

    :goto_3
    const-string v0, "PlaceHolderActivity"

    goto :goto_1

    nop

    :goto_4
    const-string v0, " onCreate PlaceHolderActivity "

    goto :goto_2

    nop

    :goto_5
    invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    goto :goto_8

    nop

    :goto_6
    return-void

    :goto_7
    invoke-virtual {p1, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_9

    nop

    :goto_8
    new-instance p1, Ljava/lang/StringBuilder;

    goto :goto_0

    nop

    :goto_9
    invoke-virtual {p1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p1

    goto :goto_3

    nop

    :goto_a
    invoke-direct {p0}, Lcom/android/provision/activities/PlaceHolderActivity;->registerFoldCallback()V

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_PlaceHolderActivity__onDestroy',
        'method': '.method protected onDestroy()V',
        'method_name': 'onDestroy',
        'method_anchors': ['invoke-super {p0}, Lmiuix/appcompat/app/AppCompatActivity;->onDestroy()V', 'invoke-direct {p0}, Lcom/android/provision/activities/PlaceHolderActivity;->unRegisterFoldCallback()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onDestroy()V
    .registers 1

    invoke-super {p0}, Lmiuix/appcompat/app/AppCompatActivity;->onDestroy()V

    invoke-direct {p0}, Lcom/android/provision/activities/PlaceHolderActivity;->unRegisterFoldCallback()V

    return-void
.end method""",
        'replacement': """.method protected onDestroy()V
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    invoke-super {p0}, Lmiuix/appcompat/app/AppCompatActivity;->onDestroy()V

    goto :goto_2

    nop

    :goto_2
    invoke-direct {p0}, Lcom/android/provision/activities/PlaceHolderActivity;->unRegisterFoldCallback()V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_PlaceHolderActivity__onResume',
        'method': '.method protected onResume()V',
        'method_name': 'onResume',
        'method_anchors': ['invoke-super {p0}, Landroidx/fragment/app/FragmentActivity;->onResume()V', 'const-string v0, "PlaceHolderActivity"', 'const-string v1, " here is onResume"', 'invoke-static {v0, v1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I', 'invoke-direct {p0}, Lcom/android/provision/activities/PlaceHolderActivity;->tryFinish()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onResume()V
    .registers 3

    invoke-super {p0}, Landroidx/fragment/app/FragmentActivity;->onResume()V

    const-string v0, "PlaceHolderActivity"

    const-string v1, " here is onResume"

    invoke-static {v0, v1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    invoke-direct {p0}, Lcom/android/provision/activities/PlaceHolderActivity;->tryFinish()V

    return-void
.end method""",
        'replacement': """.method protected onResume()V
    .registers 3

    goto :goto_3

    nop

    :goto_0
    const-string v1, " here is onResume"

    goto :goto_5

    nop

    :goto_1
    const-string v0, "PlaceHolderActivity"

    goto :goto_0

    nop

    :goto_2
    return-void

    :goto_3
    invoke-super {p0}, Landroidx/fragment/app/FragmentActivity;->onResume()V

    goto :goto_1

    nop

    :goto_4
    invoke-direct {p0}, Lcom/android/provision/activities/PlaceHolderActivity;->tryFinish()V

    goto :goto_2

    nop

    :goto_5
    invoke-static {v0, v1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
