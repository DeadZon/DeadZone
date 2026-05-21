TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/activities/DefaultActivity$InputMethodState.smali'
CLASS_FALLBACK_NAMES = ['DefaultActivity$InputMethodState.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/activities/DefaultActivity$State;']

PATCHES = [
    {
        'id': 'com_android_provision_activities_DefaultActivity__InputMethodState__domesticAndNotCM',
        'method': '.method private domesticAndNotCM()Z',
        'method_name': 'domesticAndNotCM',
        'method_anchors': ['sget-boolean p0, Lmiui/os/Build;->IS_GLOBAL_BUILD:Z', 'if-nez p0, :cond_0', 'sget-boolean p0, Lmiui/os/Build;->IS_CM_CUSTOMIZATION:Z', 'if-nez p0, :cond_0', 'return p0', 'return p0'],
        'type': 'policy_skip',
        'search': """.method private domesticAndNotCM()Z
    .registers 1

    sget-boolean p0, Lmiui/os/Build;->IS_GLOBAL_BUILD:Z

    if-nez p0, :cond_0

    sget-boolean p0, Lmiui/os/Build;->IS_CM_CUSTOMIZATION:Z

    if-nez p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method private domesticAndNotCM()Z
    .registers 1

    sget-boolean p0, Lmiui/os/Build;->IS_GLOBAL_BUILD:Z

    if-nez p0, :cond_0

    sget-boolean p0, Lmiui/os/Build;->IS_CM_CUSTOMIZATION:Z

    if-nez p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_activities_DefaultActivity__InputMethodState__isAvailable',
        'method': '.method public isAvailable(Z)Z',
        'method_name': 'isAvailable',
        'method_anchors': ['invoke-super {p0, p1}, Lcom/android/provision/activities/DefaultActivity$State;->isAvailable(Z)Z', 'if-eqz p1, :cond_13', 'iget-object p1, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;', 'invoke-static {p1}, Lcom/android/provision/Utils;->isCustSupportImeConfig(Landroid/content/Context;)Z', 'if-eqz p1, :cond_0', 'iget-object p1, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;', 'const-string v1, "input_method"', 'invoke-virtual {p1, v1}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;'],
        'type': 'policy_skip',
        'search': """.method public isAvailable(Z)Z
    .registers 14

    invoke-super {p0, p1}, Lcom/android/provision/activities/DefaultActivity$State;->isAvailable(Z)Z

    move-result p1

    const/4 v0, 0x0

    if-eqz p1, :cond_13

    iget-object p1, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {p1}, Lcom/android/provision/Utils;->isCustSupportImeConfig(Landroid/content/Context;)Z

    move-result p1

    if-eqz p1, :cond_0

    goto :goto_7

    :cond_0
    iget-object p1, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    const-string v1, "input_method"

    invoke-virtual {p1, v1}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object p1

    check-cast p1, Landroid/view/inputmethod/InputMethodManager;

    invoke-direct {p0}, Lcom/android/provision/activities/DefaultActivity$InputMethodState;->needUpdateInputMethod()Z

    move-result v1

    const-string v2, "Provision_DefaultActivity"

    if-eqz v1, :cond_1

    invoke-virtual {p1}, Landroid/view/inputmethod/InputMethodManager;->getInputMethodList()Ljava/util/List;

    move-result-object v1

    invoke-static {v1}, Lcom/android/provision/activities/DefaultActivity$InputMethodState;->updateImmList(Ljava/util/List;)V

    const-string v3, "getInputMethodList updateImmList"

    invoke-static {v2, v3}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_0

    :cond_1
    new-instance v1, Ljava/util/ArrayList;

    sget-object v3, Lcom/android/provision/activities/DefaultActivity$InputMethodState;->tmpImmList:Ljava/util/List;

    invoke-direct {v1, v3}, Ljava/util/ArrayList;-><init>(Ljava/util/Collection;)V

    :goto_0
    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v3

    sput-wide v3, Lcom/android/provision/activities/DefaultActivity$InputMethodState;->loadTime:J

    new-instance v3, Ljava/util/ArrayList;

    sget-object v4, Lcom/android/provision/activities/DefaultActivity$InputMethodState;->tmpImmList:Ljava/util/List;

    invoke-direct {v3, v4}, Ljava/util/ArrayList;-><init>(Ljava/util/Collection;)V

    invoke-static {}, Ljava/util/Locale;->getDefault()Ljava/util/Locale;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/Object;->toString()Ljava/lang/String;

    move-result-object v4

    new-instance v5, Ljava/lang/StringBuilder;

    invoke-direct {v5}, Ljava/lang/StringBuilder;-><init>()V

    const-string v6, "Current local :"

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v5

    invoke-static {v2, v5}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    if-eqz v1, :cond_13

    sget-object v5, Lcom/android/provision/fragment/InputMethodFragment;->sEmojiInputMethodSetDefault:Ljava/util/List;

    invoke-interface {v5, v4}, Ljava/util/List;->contains(Ljava/lang/Object;)Z

    move-result v5

    const/4 v6, 0x1

    if-eqz v5, :cond_a

    invoke-interface {v1}, Ljava/util/List;->size()I

    move-result v5

    sub-int/2addr v5, v6

    const/4 v7, 0x0

    move-object v8, v7

    :goto_1
    if-ltz v5, :cond_4

    invoke-interface {v1, v5}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v9

    check-cast v9, Landroid/view/inputmethod/InputMethodInfo;

    invoke-virtual {v9}, Landroid/view/inputmethod/InputMethodInfo;->getId()Ljava/lang/String;

    move-result-object v10

    const-string v11, "ru.yandex.androidkeyboard/com.android.inputmethod.latin.LatinIME"

    invoke-virtual {v11, v10}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v10

    if-eqz v10, :cond_2

    move-object v7, v9

    goto :goto_2

    :cond_2
    const-string v10, "com.preff.kb.xm/com.preff.kb.LatinIME"

    invoke-virtual {v9}, Landroid/view/inputmethod/InputMethodInfo;->getId()Ljava/lang/String;

    move-result-object v11

    invoke-virtual {v10, v11}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v10

    if-eqz v10, :cond_3

    move-object v8, v9

    :cond_3
    :goto_2
    add-int/lit8 v5, v5, -0x1

    goto :goto_1

    :cond_4
    new-instance v5, Ljava/lang/StringBuilder;

    invoke-direct {v5}, Ljava/lang/StringBuilder;-><init>()V

    const-string v9, "is yandex input: "

    invoke-virtual {v5, v9}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    if-eqz v7, :cond_5

    move v9, v6

    goto :goto_3

    :cond_5
    move v9, v0

    :goto_3
    invoke-virtual {v5, v9}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    const-string v9, ", emoji input: "

    invoke-virtual {v5, v9}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    if-eqz v8, :cond_6

    move v9, v6

    goto :goto_4

    :cond_6
    move v9, v0

    :goto_4
    invoke-virtual {v5, v9}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    const-string v9, ", currentLocal: "

    invoke-virtual {v5, v9}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v5

    invoke-static {v2, v5}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    if-eqz v7, :cond_9

    const-string v5, "ru_RU"

    invoke-virtual {v5, v4}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result v5

    if-eqz v5, :cond_7

    const-string v5, "RU"

    invoke-direct {p0, v5}, Lcom/android/provision/activities/DefaultActivity$InputMethodState;->isSupportYandexInputMethod(Ljava/lang/String;)Z

    move-result v5

    if-nez v5, :cond_8

    :cond_7
    const-string v5, "tr_TR"

    invoke-virtual {v5, v4}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result v5

    if-eqz v5, :cond_9

    const-string v5, "TR"

    invoke-direct {p0, v5}, Lcom/android/provision/activities/DefaultActivity$InputMethodState;->isSupportYandexInputMethod(Ljava/lang/String;)Z

    move-result v5

    if-eqz v5, :cond_9

    :cond_8
    const-string p1, "yandex Input Set"

    invoke-static {v2, p1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    invoke-virtual {v7}, Landroid/view/inputmethod/InputMethodInfo;->getId()Ljava/lang/String;

    move-result-object p1

    invoke-direct {p0, p1, v1, v0}, Lcom/android/provision/activities/DefaultActivity$InputMethodState;->setInputMethod(Ljava/lang/String;Ljava/util/List;Z)V

    return v0

    :cond_9
    if-eqz v8, :cond_a

    const-string p1, "emoji Input Set"

    invoke-static {v2, p1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    invoke-virtual {v8}, Landroid/view/inputmethod/InputMethodInfo;->getId()Ljava/lang/String;

    move-result-object p1

    invoke-direct {p0, p1, v1, v0}, Lcom/android/provision/activities/DefaultActivity$InputMethodState;->setInputMethod(Ljava/lang/String;Ljava/util/List;Z)V

    return v0

    :cond_a
    invoke-interface {v1}, Ljava/util/List;->size()I

    move-result v2

    sub-int/2addr v2, v6

    :goto_5
    if-ltz v2, :cond_d

    invoke-interface {v1, v2}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v5

    check-cast v5, Landroid/view/inputmethod/InputMethodInfo;

    sget-boolean v7, Lmiui/os/Build;->IS_GLOBAL_BUILD:Z

    if-eqz v7, :cond_b

    invoke-direct {p0, v5, v4, p1, v1}, Lcom/android/provision/activities/DefaultActivity$InputMethodState;->setGlobalDefaultInputMethodSucceed(Landroid/view/inputmethod/InputMethodInfo;Ljava/lang/String;Landroid/view/inputmethod/InputMethodManager;Ljava/util/List;)Z

    move-result v7

    if-eqz v7, :cond_b

    return v0

    :cond_b
    sget-object v7, Lcom/android/provision/fragment/InputMethodFragment;->sBlackImmSet:Ljava/util/HashSet;

    invoke-virtual {v5}, Landroid/view/inputmethod/InputMethodInfo;->getId()Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v7, v5}, Ljava/util/HashSet;->contains(Ljava/lang/Object;)Z

    move-result v5

    if-eqz v5, :cond_c

    invoke-interface {v1, v2}, Ljava/util/List;->remove(I)Ljava/lang/Object;

    :cond_c
    add-int/lit8 v2, v2, -0x1

    goto :goto_5

    :cond_d
    invoke-interface {v1}, Ljava/util/List;->size()I

    move-result v2

    if-eq v2, v6, :cond_12

    invoke-static {}, Lcom/android/provision/Utils;->isShieldInputMethods()Z

    move-result v2

    if-eqz v2, :cond_e

    invoke-interface {v1}, Ljava/util/List;->size()I

    move-result v2

    if-le v2, v6, :cond_e

    goto :goto_6

    :cond_e
    invoke-direct {p0, v1}, Lcom/android/provision/activities/DefaultActivity$InputMethodState;->shouldChangeSogouInBo(Ljava/util/List;)Z

    move-result v2

    if-eqz v2, :cond_f

    const-string v0, "com.sohu.inputmethod.sogou.xiaomi/.SogouIME"

    invoke-direct {p0, p1, v0, v3}, Lcom/android/provision/activities/DefaultActivity$InputMethodState;->setDefaultInputMethod(Landroid/view/inputmethod/InputMethodManager;Ljava/lang/String;Ljava/util/List;)Z

    move-result p0

    xor-int/2addr p0, v6

    return p0

    :cond_f
    invoke-direct {p0}, Lcom/android/provision/activities/DefaultActivity$InputMethodState;->domesticAndNotCM()Z

    move-result v2

    if-eqz v2, :cond_10

    invoke-interface {v1}, Ljava/util/List;->size()I

    move-result v2

    if-le v2, v6, :cond_10

    invoke-direct {p0, p1, v3}, Lcom/android/provision/activities/DefaultActivity$InputMethodState;->distributeDefaultInputMethod(Landroid/view/inputmethod/InputMethodManager;Ljava/util/List;)Z

    move-result p0

    xor-int/2addr p0, v6

    return p0

    :cond_10
    invoke-interface {v1}, Ljava/util/List;->size()I

    move-result p0

    if-le p0, v6, :cond_11

    return v6

    :cond_11
    return v0

    :cond_12
    :goto_6
    invoke-interface {v1, v0}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object p1

    check-cast p1, Landroid/view/inputmethod/InputMethodInfo;

    invoke-virtual {p1}, Landroid/view/inputmethod/InputMethodInfo;->getId()Ljava/lang/String;

    move-result-object p1

    invoke-direct {p0, p1, v3, v0}, Lcom/android/provision/activities/DefaultActivity$InputMethodState;->setInputMethod(Ljava/lang/String;Ljava/util/List;Z)V

    :cond_13
    :goto_7
    return v0
.end method""",
        'replacement': """.method public isAvailable(Z)Z
    .registers 14

    invoke-super {p0, p1}, Lcom/android/provision/activities/DefaultActivity$State;->isAvailable(Z)Z

    move-result p1

    const/4 v0, 0x0

    if-eqz p1, :cond_13

    iget-object p1, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {p1}, Lcom/android/provision/Utils;->isCustSupportImeConfig(Landroid/content/Context;)Z

    move-result p1

    if-eqz p1, :cond_0

    goto :goto_7

    :cond_0
    iget-object p1, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    const-string v1, "input_method"

    invoke-virtual {p1, v1}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object p1

    check-cast p1, Landroid/view/inputmethod/InputMethodManager;

    invoke-direct {p0}, Lcom/android/provision/activities/DefaultActivity$InputMethodState;->needUpdateInputMethod()Z

    move-result v1

    const-string v2, "Provision_DefaultActivity"

    if-eqz v1, :cond_1

    invoke-virtual {p1}, Landroid/view/inputmethod/InputMethodManager;->getInputMethodList()Ljava/util/List;

    move-result-object v1

    invoke-static {v1}, Lcom/android/provision/activities/DefaultActivity$InputMethodState;->updateImmList(Ljava/util/List;)V

    const-string v3, "getInputMethodList updateImmList"

    invoke-static {v2, v3}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_0

    :cond_1
    new-instance v1, Ljava/util/ArrayList;

    sget-object v3, Lcom/android/provision/activities/DefaultActivity$InputMethodState;->tmpImmList:Ljava/util/List;

    invoke-direct {v1, v3}, Ljava/util/ArrayList;-><init>(Ljava/util/Collection;)V

    :goto_0
    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v3

    sput-wide v3, Lcom/android/provision/activities/DefaultActivity$InputMethodState;->loadTime:J

    new-instance v3, Ljava/util/ArrayList;

    sget-object v4, Lcom/android/provision/activities/DefaultActivity$InputMethodState;->tmpImmList:Ljava/util/List;

    invoke-direct {v3, v4}, Ljava/util/ArrayList;-><init>(Ljava/util/Collection;)V

    invoke-static {}, Ljava/util/Locale;->getDefault()Ljava/util/Locale;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/Object;->toString()Ljava/lang/String;

    move-result-object v4

    new-instance v5, Ljava/lang/StringBuilder;

    invoke-direct {v5}, Ljava/lang/StringBuilder;-><init>()V

    const-string v6, "Current local :"

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v5

    invoke-static {v2, v5}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    if-eqz v1, :cond_13

    sget-object v5, Lcom/android/provision/fragment/InputMethodFragment;->sEmojiInputMethodSetDefault:Ljava/util/List;

    invoke-interface {v5, v4}, Ljava/util/List;->contains(Ljava/lang/Object;)Z

    move-result v5

    const/4 v6, 0x1

    if-eqz v5, :cond_a

    invoke-interface {v1}, Ljava/util/List;->size()I

    move-result v5

    sub-int/2addr v5, v6

    const/4 v7, 0x0

    move-object v8, v7

    :goto_1
    if-ltz v5, :cond_4

    invoke-interface {v1, v5}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v9

    check-cast v9, Landroid/view/inputmethod/InputMethodInfo;

    invoke-virtual {v9}, Landroid/view/inputmethod/InputMethodInfo;->getId()Ljava/lang/String;

    move-result-object v10

    const-string v11, "ru.yandex.androidkeyboard/com.android.inputmethod.latin.LatinIME"

    invoke-virtual {v11, v10}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v10

    if-eqz v10, :cond_2

    move-object v7, v9

    goto :goto_2

    :cond_2
    const-string v10, "com.preff.kb.xm/com.preff.kb.LatinIME"

    invoke-virtual {v9}, Landroid/view/inputmethod/InputMethodInfo;->getId()Ljava/lang/String;

    move-result-object v11

    invoke-virtual {v10, v11}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v10

    if-eqz v10, :cond_3

    move-object v8, v9

    :cond_3
    :goto_2
    add-int/lit8 v5, v5, -0x1

    goto :goto_1

    :cond_4
    new-instance v5, Ljava/lang/StringBuilder;

    invoke-direct {v5}, Ljava/lang/StringBuilder;-><init>()V

    const-string v9, "is yandex input: "

    invoke-virtual {v5, v9}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    if-eqz v7, :cond_5

    move v9, v6

    goto :goto_3

    :cond_5
    move v9, v0

    :goto_3
    invoke-virtual {v5, v9}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    const-string v9, ", emoji input: "

    invoke-virtual {v5, v9}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    if-eqz v8, :cond_6

    move v9, v6

    goto :goto_4

    :cond_6
    move v9, v0

    :goto_4
    invoke-virtual {v5, v9}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    const-string v9, ", currentLocal: "

    invoke-virtual {v5, v9}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v5

    invoke-static {v2, v5}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    if-eqz v7, :cond_9

    const-string v5, "ru_RU"

    invoke-virtual {v5, v4}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result v5

    if-eqz v5, :cond_7

    const-string v5, "RU"

    invoke-direct {p0, v5}, Lcom/android/provision/activities/DefaultActivity$InputMethodState;->isSupportYandexInputMethod(Ljava/lang/String;)Z

    move-result v5

    if-nez v5, :cond_8

    :cond_7
    const-string v5, "tr_TR"

    invoke-virtual {v5, v4}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result v5

    if-eqz v5, :cond_9

    const-string v5, "TR"

    invoke-direct {p0, v5}, Lcom/android/provision/activities/DefaultActivity$InputMethodState;->isSupportYandexInputMethod(Ljava/lang/String;)Z

    move-result v5

    if-eqz v5, :cond_9

    :cond_8
    const-string p1, "yandex Input Set"

    invoke-static {v2, p1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    invoke-virtual {v7}, Landroid/view/inputmethod/InputMethodInfo;->getId()Ljava/lang/String;

    move-result-object p1

    invoke-direct {p0, p1, v1, v0}, Lcom/android/provision/activities/DefaultActivity$InputMethodState;->setInputMethod(Ljava/lang/String;Ljava/util/List;Z)V

    return v0

    :cond_9
    if-eqz v8, :cond_a

    const-string p1, "emoji Input Set"

    invoke-static {v2, p1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    invoke-virtual {v8}, Landroid/view/inputmethod/InputMethodInfo;->getId()Ljava/lang/String;

    move-result-object p1

    invoke-direct {p0, p1, v1, v0}, Lcom/android/provision/activities/DefaultActivity$InputMethodState;->setInputMethod(Ljava/lang/String;Ljava/util/List;Z)V

    return v0

    :cond_a
    invoke-interface {v1}, Ljava/util/List;->size()I

    move-result v2

    sub-int/2addr v2, v6

    :goto_5
    if-ltz v2, :cond_d

    invoke-interface {v1, v2}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v5

    check-cast v5, Landroid/view/inputmethod/InputMethodInfo;

    sget-boolean v7, Lmiui/os/Build;->IS_GLOBAL_BUILD:Z

    if-eqz v7, :cond_b

    invoke-direct {p0, v5, v4, p1, v1}, Lcom/android/provision/activities/DefaultActivity$InputMethodState;->setGlobalDefaultInputMethodSucceed(Landroid/view/inputmethod/InputMethodInfo;Ljava/lang/String;Landroid/view/inputmethod/InputMethodManager;Ljava/util/List;)Z

    move-result v7

    if-eqz v7, :cond_b

    return v0

    :cond_b
    sget-object v7, Lcom/android/provision/fragment/InputMethodFragment;->sBlackImmSet:Ljava/util/HashSet;

    invoke-virtual {v5}, Landroid/view/inputmethod/InputMethodInfo;->getId()Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v7, v5}, Ljava/util/HashSet;->contains(Ljava/lang/Object;)Z

    move-result v5

    if-eqz v5, :cond_c

    invoke-interface {v1, v2}, Ljava/util/List;->remove(I)Ljava/lang/Object;

    :cond_c
    add-int/lit8 v2, v2, -0x1

    goto :goto_5

    :cond_d
    invoke-interface {v1}, Ljava/util/List;->size()I

    move-result v2

    if-eq v2, v6, :cond_12

    invoke-static {}, Lcom/android/provision/Utils;->isShieldInputMethods()Z

    move-result v2

    if-eqz v2, :cond_e

    invoke-interface {v1}, Ljava/util/List;->size()I

    move-result v2

    if-le v2, v6, :cond_e

    goto :goto_6

    :cond_e
    invoke-direct {p0, v1}, Lcom/android/provision/activities/DefaultActivity$InputMethodState;->shouldChangeSogouInBo(Ljava/util/List;)Z

    move-result v2

    if-eqz v2, :cond_f

    const-string v0, "com.sohu.inputmethod.sogou.xiaomi/.SogouIME"

    invoke-direct {p0, p1, v0, v3}, Lcom/android/provision/activities/DefaultActivity$InputMethodState;->setDefaultInputMethod(Landroid/view/inputmethod/InputMethodManager;Ljava/lang/String;Ljava/util/List;)Z

    move-result p0

    xor-int/2addr p0, v6

    return p0

    :cond_f
    invoke-direct {p0}, Lcom/android/provision/activities/DefaultActivity$InputMethodState;->domesticAndNotCM()Z

    move-result v2

    if-eqz v2, :cond_10

    invoke-interface {v1}, Ljava/util/List;->size()I

    move-result v2

    if-le v2, v6, :cond_10

    invoke-direct {p0, p1, v3}, Lcom/android/provision/activities/DefaultActivity$InputMethodState;->distributeDefaultInputMethod(Landroid/view/inputmethod/InputMethodManager;Ljava/util/List;)Z

    move-result p0

    xor-int/2addr p0, v6

    return p0

    :cond_10
    invoke-interface {v1}, Ljava/util/List;->size()I

    move-result p0

    if-le p0, v6, :cond_11

    return v6

    :cond_11
    return v0

    :cond_12
    :goto_6
    invoke-interface {v1, v0}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object p1

    check-cast p1, Landroid/view/inputmethod/InputMethodInfo;

    invoke-virtual {p1}, Landroid/view/inputmethod/InputMethodInfo;->getId()Ljava/lang/String;

    move-result-object p1

    invoke-direct {p0, p1, v3, v0}, Lcom/android/provision/activities/DefaultActivity$InputMethodState;->setInputMethod(Ljava/lang/String;Ljava/util/List;Z)V

    :cond_13
    :goto_7
    return v0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
]
